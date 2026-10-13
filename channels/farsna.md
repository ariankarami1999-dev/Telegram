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
<img src="https://cdn4.telesco.pe/file/S9xYJItOGVSgrARaqBGLz7W6s81Ki0sBw22li7E1yzrInTUSypoPBa-sOzBrSJjdMxVb3YJtIvBjF40kLeBl-ut3oxXt4Qoz7uZVqnvQjRTG7j_IgxcnbxmOZUGVhBvQTXdcje8-Z5IXo8qN-3VCKQNEkJg9WYUaRECBUb7AeZfeN1r_zkmSKoO73xuP1Xy5DtYGal19E6al4f2pwehyw7qocKqNwk-V3qJkqQpkuHe3vyYvs_R8ESrxigpbySp8kfa3gdIfMKuQXmHeVAKLPULRoCkZ7REuiLNW-mx013Uo41ionVX7VbVVr4AoLn34KT8q6IgjKGTBNdeoNDRoRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-468170">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
فرماندار مینودشت گلستان: جسد یکی از مفقودین سیلاب کلاله کشف شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/468170" target="_blank">📅 15:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468169">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e555ede2.mp4?token=EbeQoCeOSAJ3KCpT07G5e7K4okPbDs7x_ADi-gbKxATpZ8C3DblrTRgBZ1yNsXKC7K5vRgdqR4GTtnLZI22yM1Vc4ZmgKUVCLVn93oXKOvzf4qCs1TzMmpsLmYoBAAsjbaH38LHuhWaXewYllB1jipPKKrDGY38tvf6k4zd_LgpmvKdSp37GYz1-hkjTD3lbVHPoP3HgH-fUXi6WNZJgD-M9qUI6Q7cFCU5K97AIYs1l8Z7GZufIgnuw-9rgNlQSsVrGCKL7G44ONjp9kSs770XYVlgHn14wwGTcr_VXn23zKZi6HDsHYHf0PuZdFXbaBYApOFit79z2iYZME0NGdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e555ede2.mp4?token=EbeQoCeOSAJ3KCpT07G5e7K4okPbDs7x_ADi-gbKxATpZ8C3DblrTRgBZ1yNsXKC7K5vRgdqR4GTtnLZI22yM1Vc4ZmgKUVCLVn93oXKOvzf4qCs1TzMmpsLmYoBAAsjbaH38LHuhWaXewYllB1jipPKKrDGY38tvf6k4zd_LgpmvKdSp37GYz1-hkjTD3lbVHPoP3HgH-fUXi6WNZJgD-M9qUI6Q7cFCU5K97AIYs1l8Z7GZufIgnuw-9rgNlQSsVrGCKL7G44ONjp9kSs770XYVlgHn14wwGTcr_VXn23zKZi6HDsHYHf0PuZdFXbaBYApOFit79z2iYZME0NGdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل سازمان هدفمندی یارانه‌ها: منابع مورد نیاز برای افزایش مبلغ کالابرگ از سوی دولت اندیشیده شده و این مبالغ موجود است
@Farsna</div>
<div class="tg-footer">👁️ 627 · <a href="https://t.me/farsna/468169" target="_blank">📅 15:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468168">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACx3CWpRU_vmdL-qPSIqIZIc2ms2d3jJHy1WMVnnWyUBiSoZpNsVBo5fLDbf2kt8Nmj0RND3ldVRpq7MndTmNlDAUfFti7-KKWM4NRYV1i5rTjj3st4c9vonWKQQ6encipskJa4xAeMCHCyoFDU2KMKW0ofAK8KCiJcDVNRVAw6Sf4coi9Wo_2QuqXE_wGv9__-caVl5d0-yiwvZhHEPuMD1tlyud2Vlu9C5l8B_6gJCKICobC8Fu5zt8YkkkhnLAc5VLwrvHHQ4USBz8dazlQzuXBQ_-_VX8K3KswFdACyXNi5LNNcuSSuDpAKDSe2-zAaESdHHaCUES2VUuKisfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۳ انفجار درپی حمله پهپادی به پایتخت عربستان
🔹
منابع عربی از شنیده‌شدن صدای ۳ انفجار در شمال ریاض درپی حملات پهپادی یمن خبر دادند. ائتلاف سعودی هم حملهٔ پهپادی به این شهر را تأیید کرد. @Farsna</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/468168" target="_blank">📅 15:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468166">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شمارهٔ ۱۱۵ اورژانس تهران قطع شد؛ با شماره‌های جایگزین تماس بگیرید
🔹
اورژانس استان تهران از اختلال در شمارهٔ ۱۱۵ خبر داد و اعلام کرد: شهروندان عزیز در صورت برقرارنشدن تماس با ۱۱۵ می‌توانند از طریق شماره‌های زیر با مرکز ارتباطات اورژانس استان تهران تماس بگیرند:
02146015981
02146015619
02146015948
02146015734
02146015732
02146015873
02146015613
02146015703
02146015648
02144896391
02144891399
02144891525
02144896345
02144896376
02144896389
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/farsna/468166" target="_blank">📅 15:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac849176b.mp4?token=NOHRD1wtnVZkB4joMP9u05mvs6RmXpNIQLwyXjbbnMzCev2j3HsWR4Eujvs3qj5t1JK6kF29Kqghjc6u3ystsrKVkua6ZFi6hzc2llwcss5eiE2ZQBOYStMhM5fwS91ESIYtiqID7F5H4A9atl7jFckMmG90iTpofm_QVRbvBHBsYh3ExZH5_HIrotXFhXR1pSNewd4pUBjWmf9Mc5lc_ezgf9YIPH8euJ2jCVAX9lP0Vu6La_67EM0Tknjsw5yLIFa3z7guQIgXInWngL_IdrIJggQQFsjMBWJiVoxQ_Nxj20jN0Ji-3TkIyVnK56cDSkF9xHWyAzuIz4_trT4pGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac849176b.mp4?token=NOHRD1wtnVZkB4joMP9u05mvs6RmXpNIQLwyXjbbnMzCev2j3HsWR4Eujvs3qj5t1JK6kF29Kqghjc6u3ystsrKVkua6ZFi6hzc2llwcss5eiE2ZQBOYStMhM5fwS91ESIYtiqID7F5H4A9atl7jFckMmG90iTpofm_QVRbvBHBsYh3ExZH5_HIrotXFhXR1pSNewd4pUBjWmf9Mc5lc_ezgf9YIPH8euJ2jCVAX9lP0Vu6La_67EM0Tknjsw5yLIFa3z7guQIgXInWngL_IdrIJggQQFsjMBWJiVoxQ_Nxj20jN0Ji-3TkIyVnK56cDSkF9xHWyAzuIz4_trT4pGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرپرست وزارت نفت: تعمیرات اساسی در میدان گازی پارس جنوبی ناشی از خسارات جنگ تمام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/468165" target="_blank">📅 15:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b593f2b44c.mp4?token=ebunEcrdvuaTV5UxllNCqveD4cW8uby1nj_INKOUOU9VA0htND56HTkc5DAwVPUKX8i_21PZRGJXyLsxVmEr15CbTLRBKehJEAUzHTmvzNMWX65VDT4rWMIWPPbPRbaL5sm22WZFeSBF2hBpanEYwgYaukZUXlDZgBlofyQ8Wnmp_CQ6ffcLwjQafJuOxrgJ9PDnp-F-aGvAvU10Pcq6VOoxSOqn1TwsLTyInKfBsIwCWRtAv6NHiPRLhUuLLzwZ2gkXFG7bPbLQC_g7a3EMEdyVTVhRWMrzIZ6ma2k5D9W1honr_MFjGt8r89gDmjaXbpMemV5Zep5nZwTVDSzaYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b593f2b44c.mp4?token=ebunEcrdvuaTV5UxllNCqveD4cW8uby1nj_INKOUOU9VA0htND56HTkc5DAwVPUKX8i_21PZRGJXyLsxVmEr15CbTLRBKehJEAUzHTmvzNMWX65VDT4rWMIWPPbPRbaL5sm22WZFeSBF2hBpanEYwgYaukZUXlDZgBlofyQ8Wnmp_CQ6ffcLwjQafJuOxrgJ9PDnp-F-aGvAvU10Pcq6VOoxSOqn1TwsLTyInKfBsIwCWRtAv6NHiPRLhUuLLzwZ2gkXFG7bPbLQC_g7a3EMEdyVTVhRWMrzIZ6ma2k5D9W1honr_MFjGt8r89gDmjaXbpMemV5Zep5nZwTVDSzaYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: شرایط برای بارش در نیمهٔ غربی و جنوبی کشور مهیاست
@Farsna</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/468164" target="_blank">📅 15:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xej_j1pwAjpKCahOIXM_dFNYvkjbeU5Fkw-gTHGxcp04N_Z_CgDMASJZBmsT49me5gHrzZ2oXamCsgpGZ840XmcTNHPbjjYN_GWQKmxZc-q7KLj2McMKQpC_hWZNTymEUQn1hO9Apm24uHAOo0wppvrviaR0QL1shWQ7qMXgH7vIYhY3PBOR09iNFDWEdDu0Gf30DJO7YJedk4_QE-rRgjqeXT0sx2r1sV_FmAXwD2ct5OviXeEhO_vOn-JUkwBN_aSy1jqTLQ3Lz6zir6LNe8eMrmqFto-uK4zJY566J-f139ku2X6LQZ4wBVnW0V8tGBXhFD3_RixqU0M0_TDM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس من|
موافقت وزارت بهداشت با تعطیلی مراکز جامع سلامت تهران در روزهای پنجشنبه
🔹
درپی انتشار گزارش خبرگزاری فارس دربارهٔ اعتراض نیروهای بهداشت دانشگاه علوم پزشکی شهید بهشتی به تبعیض در تعطیلی پنجشنبه‌ها و فعالیت بدون دریافت حقوق، مدیرکل توسعه منابع وزارت بهداشت از ارائهٔ پیشنهاد تعطیلی مراکز جامع سلامت در روزهای پنجشنبه تا پایان سال خبر داد.
🔹
چند روز پیش نیز علیرضا رئیسی، معاون بهداشت وزیر بهداشت، در گفت‌وگو با فارس اعلام کرده بود که موضوع تعطیلی پنجشنبه‌های نیروهای بهداشت در دستورکار قرار گرفته و به‌زودی ابلاغ می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/468163" target="_blank">📅 15:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468161">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۳ انفجار درپی حمله پهپادی به پایتخت عربستان
🔹
منابع عربی از شنیده‌شدن صدای ۳ انفجار در شمال ریاض درپی حملات پهپادی یمن خبر دادند. ائتلاف سعودی هم حملهٔ پهپادی به این شهر را تأیید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/468161" target="_blank">📅 15:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468160">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64be7e8a46.mp4?token=k4UCplyme2Xg5nQU4LtGJs9iSAM7KJF-YOjbFHRtqpchZHZGSPNLOOk-Ak6xJ-jZb7-RPtI2K3Z8iTE3v1S_GgvNVQfMEaCYh6OCWltdS8BznwTtaDbVgIPZXQBY_NswLrBVsh_KCVrs4PzaQHRBtR5Lmbz45iDP889DWkE-XXydHZoT1XUPRloDqrirCAxJ5K7s7fvQZbaXOEYwkILyLjCaYbfZqp_JBAVX9nQ_PR3OFrYv5F5yj_8LePbkOAHGGkvEPtZi9p1zop06qD9HlZDK3Vl0lKBdFIxW0qrj_V2xMBNG3h32prWCwHBumL-P03fG4VLI5udKdOBvzyB6EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64be7e8a46.mp4?token=k4UCplyme2Xg5nQU4LtGJs9iSAM7KJF-YOjbFHRtqpchZHZGSPNLOOk-Ak6xJ-jZb7-RPtI2K3Z8iTE3v1S_GgvNVQfMEaCYh6OCWltdS8BznwTtaDbVgIPZXQBY_NswLrBVsh_KCVrs4PzaQHRBtR5Lmbz45iDP889DWkE-XXydHZoT1XUPRloDqrirCAxJ5K7s7fvQZbaXOEYwkILyLjCaYbfZqp_JBAVX9nQ_PR3OFrYv5F5yj_8LePbkOAHGGkvEPtZi9p1zop06qD9HlZDK3Vl0lKBdFIxW0qrj_V2xMBNG3h32prWCwHBumL-P03fG4VLI5udKdOBvzyB6EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز آمار: نتایج اولیهٔ سرشماری ۱۴۰۵ ابتدای اسفند منتشر خواهد شد
🔹
عملیات اینترنتی سرشماری ثبتی مبنا از ۲۵ مهر و مرحلهٔ دوم این عملیات از آبان آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/468160" target="_blank">📅 15:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468159">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHuUG3RVzRtWsNTZYDffKMRwCsT3fK73yCNR9Dv1IMp26jl5KBbz3peF3fysl038vo1vxDFagKdaBEkQOVo2XkUxHHYDTsq4Jb23GvMMcMkoaqIPSZ4bmyXxGhUAlVWNRAq5l3pQ0LJY2sNLdegKOfL-hsE1rqilgwr-Qo5-FEnbnrWQp9dyNT4TCeLpLmdh34ESmsVcQX-1bVUqibm6RZ2XovT17NRExuchLuKwjiAsUMeULca0mGO9IkJiR7IEke5bPZeW2iqVxi41Bdt8BjG9EWC3qiMW5z15C1YrmUncMywKj0d4ykz3bR-w4QnSA7HH9EB-XdCgHdDW2uJ7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور: اقتصاد ایران به قدرت معامله در کنار قدرت تولید نیاز دارد
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، در افتتاحیه نمایشگاه صنایع خلاق مانوین در اصفهان گفت: تولید محصول باکیفیت به‌تنهایی برای موفقیت اقتصادی کافی نیست.
🔹
شناخت بازار، قدرت مذاکره و کسب سهم بیشتر از ارزش معاملات نیز اهمیت دارد و صنایع خلاق ایران برای حضور مؤثر در بازارهای جهانی باید توان عرضه و معامله محصولات خود را تقویت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/468159" target="_blank">📅 15:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468158">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1902b1ff2.mp4?token=bXy9FnmcfoIXvTrhEUTrGyvM44_XHyFAMJYap-7FT8J7FUtSb8XJsD9E7sk5go8SgEqE370ojr9dNv8kcXH8hk_tWSVjMZ5G8fevPQ2MaZfonen4_GbOQdJAISUOndC5hhEq9jDuzLm1gWWNOBo_8tlUCfVuRJ_C4QpYNX6DBE4YyWc-7Cu22VvuEiXnjA037zfPZuVIJdULa7Nofs10ih-4OiIejDEn_GD3dSrp6CpiXyUyvmPKA0wL1D-yjBd8D2bHE72KsJo4vlrOYwPZMyJTxu-dOnkrTfdCfPdonHfQoxfEgf-qPRHRkOGnOpFam0ONSlffi5D1rKCEZvBc-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1902b1ff2.mp4?token=bXy9FnmcfoIXvTrhEUTrGyvM44_XHyFAMJYap-7FT8J7FUtSb8XJsD9E7sk5go8SgEqE370ojr9dNv8kcXH8hk_tWSVjMZ5G8fevPQ2MaZfonen4_GbOQdJAISUOndC5hhEq9jDuzLm1gWWNOBo_8tlUCfVuRJ_C4QpYNX6DBE4YyWc-7Cu22VvuEiXnjA037zfPZuVIJdULa7Nofs10ih-4OiIejDEn_GD3dSrp6CpiXyUyvmPKA0wL1D-yjBd8D2bHE72KsJo4vlrOYwPZMyJTxu-dOnkrTfdCfPdonHfQoxfEgf-qPRHRkOGnOpFam0ONSlffi5D1rKCEZvBc-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشبیه ترامپ به «سگ نازی‌آباد» توسط سخنگوی وزارت خارجه!
🔹
بقایی در واکنش به تغییر موضع ترامپ دربارهٔ زلنسکی و حمایت از برکناری او: این مصداق حرف کیسینجر، متفکر آمریکایی بود که گفت «دشمن آمریکا بودن خطرناک است، اما دوست آمریکا بودن مرگبار است».
🔹
مرحوم جعفر…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/468158" target="_blank">📅 15:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a3859fe5.mp4?token=kvXY4FVTEs5ZmRnYqbYjhCi0WVCTRErWy329SrNdBA2BFKTjV1FRcGjpRzarIq1Z6sfCFg4np1JfltYapvIyTcG07rZoOXAuaBBTXnXR-_VUCUo2Zk34DVzChIvhnfB9aVchU3p_xqAeyESm2DpeKH6UWwO1CX799ZO04CtWJTOItEk4uER7I61_jZjC2JdXSJ2KrCOquoDNElk70V70GHuZzq43MTtIIAHMV2pVxXwTvOgj0uJ79b89AsubP9c7tL-TGPcqz3LEW2H5LZ01dfY9SYtrkXKgLa0-bsmlyuzvCXO6azyLsQIJeKLJzkGrSAw-ciVUg3A8ShlLkFHdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a3859fe5.mp4?token=kvXY4FVTEs5ZmRnYqbYjhCi0WVCTRErWy329SrNdBA2BFKTjV1FRcGjpRzarIq1Z6sfCFg4np1JfltYapvIyTcG07rZoOXAuaBBTXnXR-_VUCUo2Zk34DVzChIvhnfB9aVchU3p_xqAeyESm2DpeKH6UWwO1CX799ZO04CtWJTOItEk4uER7I61_jZjC2JdXSJ2KrCOquoDNElk70V70GHuZzq43MTtIIAHMV2pVxXwTvOgj0uJ79b89AsubP9c7tL-TGPcqz3LEW2H5LZ01dfY9SYtrkXKgLa0-bsmlyuzvCXO6azyLsQIJeKLJzkGrSAw-ciVUg3A8ShlLkFHdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل سازمان انرژی تجدیدپذیر: برق سبز در زمستان ارزان نمی‌شود
🔹
در تلاش هستیم تا قیمت در بازار بورس سبز برای سرمایه‌گذاران جذابیت داشته باشد؛ البته از سال ۱۴۰۷ صنایع ملزم به تامین ۲۰ درصد برقی مصرفی خود از منابع تجدیدپذیر هستند.
@Farsna</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/468156" target="_blank">📅 15:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw7xbpQwwM9AFRTTXjAuK99_nj9qlc3lBQAqo-C-iuxaHwYqVX5s_YvZ2oKWHCT-6G4p0YI2iP_UmGPhv5W3B3xfEO_N-0Jn9IB1JOvWT6Ej8QtkuMmoQqszPwxlxtVRYHVN7hwtioLNjd2uv7XMl3cM9zcL_QnNYS_0hnQSUi45Ze_0u6HEJGd234hJ5F9zYt04q6YEROEGEhObQO0SQ6LGOZ1P_w5zAamG-Zasp97PHQrTZ3NoWPsPPDWYPsNCVGyszeN6IQZfnzU82hNxCo8HKlNk1t_S_rh_us0tXzrVxmgrJtobFJi1isdPL-31aKcG15SOjOVyGE5y92xrEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
«بانک شهر»، پشتیبان توسعه زیرساخت‌های شهری و تقویت سرمایه‌گذاری در آذربایجان غربی
👈
مدیرعامل بانک شهر و استاندار آذربایجان غربی طی مراسمی با امضای تفاهم‌نامه همکاری مشترک، بر توسعه تعاملات بانکی و اقتصادی با هدف حمایت از پروژه‌های عمرانی و زیرساخت‌های شهری، تقویت سرمایه‌گذاری و بهره‌گیری از ظرفیت‌های تولیدی استان تأکید کردند.
👈
به گزارش روابط عمومی بانک شهر، در این مراسم که با حضور شهردار ارومیه و جمعی از معاونان و مدیران ارشد بانک شهر برگزار شد، راهکارهای توسعه همکاری‌های مشترک در حوزه تأمین مالی پروژه‌های شهری، توسعه حمل‌ونقل عمومی، حمایت از واحدهای تولیدی و گسترش خدمات بانکی در استان آذربایجان غربی مورد بررسی قرار گرفت.
🔗
مشروح خبر را اینجا بخوانید</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/farsna/468155" target="_blank">📅 15:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmP66otHosC8S4Mb__IjE7WuDwr5WY6JOFO8j2fbslgpncx5wiFUq7WuVsA18jM8BYU8Gb46PLjEmU6ZsSOkSh7uwpHkpTU6SHVsS4f57RtJz9se8gWK70TubdwrGWuv08XScJCGfpxSythG7HC_mcZ1JSTEjtA3TYepTfe8qj8v_6Cxwv83CVbEL7PeZrVZpOe7wJ7TvTI5MSu_4zhPtS8d2f6Xh0qPrCCYmNOc8H2iqGFblkLU0YYOU7uVsDQOlexleAmiHbzuXpRmKyJlzpLslS9QPagtJ0Qqmh7JH89SNf-TuTo8nREEMBL5hCr-7yRKVgkrhD2DdceWQABv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/468154" target="_blank">📅 15:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/468153" target="_blank">📅 15:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5694dd35.mp4?token=K0tNEtF_yJE8A3eNqPPRedF6Ie-jjELSC2oSec32yCjscT-y__BxIM2rhgHGEDgccJJ2kMoztqyPgiPnHiHtZXvVkHDUsgw1eBE47gLi1c4Wgk4r6dCimDehc_jAz3Uz9WtKJMEE1KmEpzz4IoEYomdTq9L4x5ugHnqy2fxWla6-Hxcw0g4sz3Uw4cdkiSgUiGNYKzsK4hUk-RkzVNeOBUJIZEnyXWVUwc53g8tzQ9mTFAgKerT6ay9JqzyaTaXvdwFEK_0cmg2IJe31Mmw_sXQgmYEnq0eXGUmNY4WSYXYOVGpE6Fm1Z6X1XS7a_0zJHjJZpB-nIkxuPAF900KW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5694dd35.mp4?token=K0tNEtF_yJE8A3eNqPPRedF6Ie-jjELSC2oSec32yCjscT-y__BxIM2rhgHGEDgccJJ2kMoztqyPgiPnHiHtZXvVkHDUsgw1eBE47gLi1c4Wgk4r6dCimDehc_jAz3Uz9WtKJMEE1KmEpzz4IoEYomdTq9L4x5ugHnqy2fxWla6-Hxcw0g4sz3Uw4cdkiSgUiGNYKzsK4hUk-RkzVNeOBUJIZEnyXWVUwc53g8tzQ9mTFAgKerT6ay9JqzyaTaXvdwFEK_0cmg2IJe31Mmw_sXQgmYEnq0eXGUmNY4WSYXYOVGpE6Fm1Z6X1XS7a_0zJHjJZpB-nIkxuPAF900KW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران سلطنت‌طلبان یا ایران روبیو؛ آمریکا با کدام می‌جنگد؟
@Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/468152" target="_blank">📅 15:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468151">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5907c43e.mp4?token=ae6_jOLGO-gcB6PZtPyg0ik0glaHPht2gw6fBGDz3Zn-nfL4te2HZvAX53RFUwMTXb-xsbMlT34Z1wENCn0edCruQMwgUNgScYGg9VLeNleIH0kplubaA0T_yZwNcJFb71SzRgH8_V-6V-sJymvdbqCV6qkZOd2bfGBngK2E7SnYJwymGy_GEySdKnoZTAaQKt-H34hdSgqIWxuycZyciKv89LkYDQa6CIrez8L-CCNpjMOanvr2KNugFL_Y5i0AnejZtgbdHFb66idGENBS5FRKb5b5cyc08lugHeV_-yRiech8_NS7tkWoKeT8UiK3KgMJ36FUMq8dkUYGfcnroQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5907c43e.mp4?token=ae6_jOLGO-gcB6PZtPyg0ik0glaHPht2gw6fBGDz3Zn-nfL4te2HZvAX53RFUwMTXb-xsbMlT34Z1wENCn0edCruQMwgUNgScYGg9VLeNleIH0kplubaA0T_yZwNcJFb71SzRgH8_V-6V-sJymvdbqCV6qkZOd2bfGBngK2E7SnYJwymGy_GEySdKnoZTAaQKt-H34hdSgqIWxuycZyciKv89LkYDQa6CIrez8L-CCNpjMOanvr2KNugFL_Y5i0AnejZtgbdHFb66idGENBS5FRKb5b5cyc08lugHeV_-yRiech8_NS7tkWoKeT8UiK3KgMJ36FUMq8dkUYGfcnroQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی دانشگاه برای ایران برمی‌خیزد
🔸
روایتی از دانشجویان دانشگاه علامه طباطبائی برای کسانی که تا پای جان برای ایران ایستاده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/468151" target="_blank">📅 14:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468150">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHgPjND8OnLqgzejHkIjTNvPANBkz7qOcV9UmxkEviCzM6bO5S5njsi5GuY5_dFkCQ9rO7Ny6x6qydfU1bxtV3kaosd-s911pp7eZC3QAP2LdkxOUtodZYjtw95NY2VpDCwVK1gZwnRi39XXrCNncUQH4RJGdn42JXjOhk8sOE_3G3Fr9n6XZAnOADQUCMIBdQovehF2A8NhN0YHHYgfifJ7OG39UcotH5-Mh-OKap388kWZsKlSSiTwVvaPn8orKnFA7Viq_zUEQkczK2jQAbdQi70kQm5Ib8RqEJ6_5uIDipj8VHBYLLl-LWpp2yr8xDGolSbn7lFeMTQs_MGVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمایی امارات از تعلیق تمامی پروازهای خود از مبدأ و به مقصد فرودگاه‌های ریاض، دمام و جدهٔ عربستان خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/468150" target="_blank">📅 14:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468149">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108ca38a00.mp4?token=unabOAtDVrxsAG8yPuX2PH3Wxy8RXbvLwx76BQUcFW7D2f9h27acaB9OGykE9-c1fo-nESvIAgoeyZ9x1n31f35hywPLaNHN5gZY8bPMPnt_yyRKB-mDym-_K3UPogKIs4jF_tg-ZaSooJ8D4QGGk884Dvnkjo8wRQ9J4xWhMOt3uiZbhM_UQjkpMF7WnPzVuWybaPEDpWalMtV_c7QgZK6nedvJjljDN-HeOxAz7G7_UO300YEdC7tPTQwsTNm89Pc-bY8RK82i4A7XRQ8kXGzNiZAVWd2iC7qerRThPW1kpIholJd4XhIRN11M_kNKYUlU5L_RCulotlXkjGjcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108ca38a00.mp4?token=unabOAtDVrxsAG8yPuX2PH3Wxy8RXbvLwx76BQUcFW7D2f9h27acaB9OGykE9-c1fo-nESvIAgoeyZ9x1n31f35hywPLaNHN5gZY8bPMPnt_yyRKB-mDym-_K3UPogKIs4jF_tg-ZaSooJ8D4QGGk884Dvnkjo8wRQ9J4xWhMOt3uiZbhM_UQjkpMF7WnPzVuWybaPEDpWalMtV_c7QgZK6nedvJjljDN-HeOxAz7G7_UO300YEdC7tPTQwsTNm89Pc-bY8RK82i4A7XRQ8kXGzNiZAVWd2iC7qerRThPW1kpIholJd4XhIRN11M_kNKYUlU5L_RCulotlXkjGjcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر کشور به باکو رفت
🔹
اسکندر مومنی به دعوت رسمی همتای آذربایجانی، برای دیدار با مقامات این کشور عازم باکو شد.
🔹
دیدار و گفت‌وگو با ولایت عیوض‌اف وزیر کشور و برخی دیگر از مقامات جمهوری آذربایجان از برنامه‌های سفر مومنی به این کشور است. @Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/468149" target="_blank">📅 14:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468148">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c980577899.mp4?token=KK9uBU-4EK0Xce6AuEp6vZxAepSj13au6CFOyA5_yhYFN2WnsHoBilyWowya2URlazYMU0n7hbGgmMh1NUfm_9XglLVCSD1SEW6WbObM-J5YppcXtIXbESGnWYVVysZ74PI3OQZIBNu8YLmH-UJX85um-4tq5k4wg9oH8w1SZIDtPlwJuWJunJnJ6QrTLg1964SnXtkprlRbljVVsAN6c3jFpwhBKxF0tD2575tzQ_66M_A8KuTeyCr6U36Jpl83sp7BrT0L_nUedGATBFFIGypwc30VmIdPiNpcu52kFPcneMtPHhTEDjp4uHcnHfS28-8ETJ4VecRXN98GEzWt1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c980577899.mp4?token=KK9uBU-4EK0Xce6AuEp6vZxAepSj13au6CFOyA5_yhYFN2WnsHoBilyWowya2URlazYMU0n7hbGgmMh1NUfm_9XglLVCSD1SEW6WbObM-J5YppcXtIXbESGnWYVVysZ74PI3OQZIBNu8YLmH-UJX85um-4tq5k4wg9oH8w1SZIDtPlwJuWJunJnJ6QrTLg1964SnXtkprlRbljVVsAN6c3jFpwhBKxF0tD2575tzQ_66M_A8KuTeyCr6U36Jpl83sp7BrT0L_nUedGATBFFIGypwc30VmIdPiNpcu52kFPcneMtPHhTEDjp4uHcnHfS28-8ETJ4VecRXN98GEzWt1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رادیوداروی آکتینیوم در اختیار مراکز درمانی قرار گرفت
🔸
ایران درحال‌حاضر جزو ۵ کشور دارندهٔ این رادیودارو قرار دارد که برای درمان بسیاری از سرطان‌ها
استفاده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/468148" target="_blank">📅 14:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
صدور کیفرخواست محاربه برای ۲ عضو باند گانگسترها
🔹
دادستان تهران: کیفرخواست ۲ متهم از اعضای باند سرقت‌های سریالی مسلحانه از منازل تهران و برخی شهرستان‌ها، معروف به «باند گانگسترها»، صادر و برای رسیدگی فوری به شعبه ویژه دادگاه انقلاب ارسال شد.
🔹
این متهمان با ارتکاب سرقت‌های مسلحانه، علاوه بر آزار و واردکردن خسارت به قربانیان، موجب رعب و وحشت عمومی شده بودند.
🔹
پروندۀ ۴ عضو دیگر این باند در سال ۱۴۰۴ رسیدگی شده و حکم محاربۀ آن‌ها اجرا شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/468147" target="_blank">📅 14:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌ پایان درگیری مسلحانه در کورین زاهدان با هلاکت ۵ تروریست
🔹
یک منبع آگاه به فارس گفت: «درگیری مسلحانه نیروهای حافظ امنیت با عناصر گروهک‌های تروریستی که از صبح امروز در منطقۀ کورین زاهدان آغاز شده بود، با هلاکت ۵ نفر از تروریست‌ها پایان یافت.
🔹
در این درگیری،…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/468146" target="_blank">📅 14:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdgtJKMm42yms8iw1LSwhDZxSX8V1IDMsglJBHIrl6pNZN2PLVqzf2m2pz2lCqdsHyOrAIQTfKvp5K_p2OvC_Asyn-kfHULTCekAHxKkHSAQ9RMJXJebu95VPjGEbH6tlQn4QBuqEEhQwuTBv7Xymd0dnvjAdMR2ntf2BOFYZ54Re2P8BRGOTJBCXIfEfORewX6RT1V6NPyP5-vkTFmc7mOwlkOgRYNq9aPJ0kf9e_-MlqlTVVKDd8OUmOlSCof2SQxcKHWZ4YYUswPIYgl68sq68js04Y64kZ0AsWtOTZriTvJKFuxvYhR6E2zNUAWPMH2ibqO690B2vMM0lgWpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ik6VDlGteVlJmRDDm6xdyvFRph6BR4lY5H5QHwz-Y7AZTnlkr3Da1W207HsWJ9VVIKn8UlMM1ycAXybO0joCI2gGDFY5aRUS2INSkXwkFuaFH6gSJTBLQiX6mxvXc5yRfEJgCHhWL6j-ZX25D33yXLj4rhPq_hve6S_tAuhLTTATIt5S8dUyhPsCAr75zuCYpTo_9QnQqgv6xWl51KCBDLLASfCMR6w7NqBiKwF-c2g8Af0LeV_LQ4s4i_USAcXQsbXj2s8GAiNBtkfKYYZytwGTAU5zoWT3zJJYy3NClrJSmIkxR7hN5GT9uaBxle-BZPkY3h6ylqlkeQPrwP1Pow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5832d98254.mp4?token=pfw8WDeQRGeAmmjN3GppLM9vSuV_XpUigBZB-kYjhTya8nPfwFPIpuY7Tdsghi7yqdT5CZ2kRezsvu27J9bzMUhyhwOCUM1aGXoPvtMW0HmeE_HM3O7cbWXuFplu3Kua4qaqqV2EGc0CjTtQMamj7VOxcYDT9qOE5cvvGl_obQhKRwsbwKFFD6mCSfGfrygNbWf3DATKXR_6lENiaE1YM5FcbWBw3GFNDope-SwcEjJoqUdRwWd-p1ky_BS5zt58yPRpMGgj5PgXgFJ0udpYShN2OGWxS2uDZOkN9iKettaHMCiAqiqGJzms1uw-y2c4VJlE8u68qCLSL_XINuKSpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5832d98254.mp4?token=pfw8WDeQRGeAmmjN3GppLM9vSuV_XpUigBZB-kYjhTya8nPfwFPIpuY7Tdsghi7yqdT5CZ2kRezsvu27J9bzMUhyhwOCUM1aGXoPvtMW0HmeE_HM3O7cbWXuFplu3Kua4qaqqV2EGc0CjTtQMamj7VOxcYDT9qOE5cvvGl_obQhKRwsbwKFFD6mCSfGfrygNbWf3DATKXR_6lENiaE1YM5FcbWBw3GFNDope-SwcEjJoqUdRwWd-p1ky_BS5zt58yPRpMGgj5PgXgFJ0udpYShN2OGWxS2uDZOkN9iKettaHMCiAqiqGJzms1uw-y2c4VJlE8u68qCLSL_XINuKSpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک دختران دانش‌آموز باکویی دیده شد
🔹
کاربران شبکه‌های اجتماعی در واکنش به گزارش‌ها دربارهٔ جلوگیری از حضور دختران محجبه در کلاس‌های درس در جمهوری آذربایجان، سیاست‌های آموزشی این کشور را به باد انتقاد گرفتند و گفتند: آزادی و حقوق زنان مسلمان با این قانون زیر سؤال رفته است.
🔸
در پی وضع قانون ممنوعیت حجاب در مدارس جمهوری آذربایجان و به بهانهٔ لزوم پوشیدن لباس فرم‌های یکسان بدون حجاب، کلاس‌های درس این کشور به‌روی دانش‌آموزان و معلمان محجبه بسته شده و از ورود دختران محجبه به مدارس جلوگیری می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/468141" target="_blank">📅 14:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/903ae1c93a.mp4?token=sLc8JLll8G9gD0f7Gw1BkOGHELWjFMU1-Vjfwo_UldKu9hfNthvpcyTCYATHNiJ_UBzQ5ag_--fgtWX5WH9E1mFIq3cGnq7uq9tgteq0n5JG-pLMQzTObJkB_iJFFhDJ4bqjPBukd8ehPbUSNWH_AsFq0_4UG_9q1y7BNJsbUIQjivx5KT-0A8ypeYml3gSjpHQXn65aIdQx4CIZhD1wmrb8Gn_A7n303K_0uKxVmJPtVIPjVvfDFIAieJvpkt3UiWlN8w7u8NpSS-XZW7UX21iOvgU5f3yIKw2wsAWPDn9-VNcWTTFuNK5OkOrx98ZY4q_PJLPvrEhoFeag69QMGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/903ae1c93a.mp4?token=sLc8JLll8G9gD0f7Gw1BkOGHELWjFMU1-Vjfwo_UldKu9hfNthvpcyTCYATHNiJ_UBzQ5ag_--fgtWX5WH9E1mFIq3cGnq7uq9tgteq0n5JG-pLMQzTObJkB_iJFFhDJ4bqjPBukd8ehPbUSNWH_AsFq0_4UG_9q1y7BNJsbUIQjivx5KT-0A8ypeYml3gSjpHQXn65aIdQx4CIZhD1wmrb8Gn_A7n303K_0uKxVmJPtVIPjVvfDFIAieJvpkt3UiWlN8w7u8NpSS-XZW7UX21iOvgU5f3yIKw2wsAWPDn9-VNcWTTFuNK5OkOrx98ZY4q_PJLPvrEhoFeag69QMGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دادگاه رسیدگی به جنایات منافقین: دولت‌های اروپایی میزبان منافقین مکلف به استرداد متهمان به ایران هستند
🔹
بر پایه رویۀ قضایی بین‌المللی، کسانی که متهم به جرایم تروریستی و اقدامات خشونت‌بار هستند مشمول پناهندگی سیاسی نیستند. @Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/468140" target="_blank">📅 14:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmfKkxf9MbWP78eZiuvaBSjkBhzml_NjPQScLYNbaqEbxSfMEi6_XrrxtSC6xeYNpPz-mB4aqbjaXScSy-hVr-KrDn0OvghT4IFnA3mokynOI0yqt0XcDtRJxYsZxS6rIjo8ea719DHYg73sXJ1ZuRqf8xrDEN_6XD26HJ2sM-J3awhHTr8e-sXTrgTh34WVVfkylooRca0l8qon2fbQDcnPpNDWOKcU_gc0-FPkniCRq3knzloNFYrm-Fb-tlXmuiDXhBvc3c0FywWoyxf828SRMzpWqY76BUO5mNpSDwW-Y2tusrsjZ1ee0JwOwVWjqhaf-K1pT78DxhuJhFCo7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی فضای مجازی: شناسایی پایانه‌های استارلینک از اولویت‌های ماست
🔹
فناوری‌های مورد استفاده برای شناسایی و مقابله با استارلینک، به اختلال در جی‌پی‌اس محدود نمی‌شود و فناوری‌های دیگری نیز در این زمینه به کار گرفته شده است.
🔹
هدف از مقابله با استارلینک،…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/468139" target="_blank">📅 14:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4ea09b1f.mp4?token=PvTscY88-tYHIFOkE-p5sPBjeT3m3k8V1miHdQkG8bNQlJKMwAdOrKdgHRaUQ11PMp7VM2xBD1kx0nBZf1F4SUR97gDUtBbvcQclx_0gLEftRq5PKXmGV8RKXn522mkH6_cgAX8M-uxFtdCQcEooPsyUBrehAIWGuTisVn9eDjsUdqqGT9sOk86ARuEmf1UMxd983n9pJXRYoJXHDt6WzixTY_bLc-ah6fFO-1KkqiVDOqnuJ7F1ugHfiYLOhnXuiek2qY5NM6Pi3W--_vNHpFcmnV5Ji_l8d0ws5FEE2Hu2OPhcHsLQHf2utSv30Ow0wpt2ZIFY1YWSdZ-td85KYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4ea09b1f.mp4?token=PvTscY88-tYHIFOkE-p5sPBjeT3m3k8V1miHdQkG8bNQlJKMwAdOrKdgHRaUQ11PMp7VM2xBD1kx0nBZf1F4SUR97gDUtBbvcQclx_0gLEftRq5PKXmGV8RKXn522mkH6_cgAX8M-uxFtdCQcEooPsyUBrehAIWGuTisVn9eDjsUdqqGT9sOk86ARuEmf1UMxd983n9pJXRYoJXHDt6WzixTY_bLc-ah6fFO-1KkqiVDOqnuJ7F1ugHfiYLOhnXuiek2qY5NM6Pi3W--_vNHpFcmnV5Ji_l8d0ws5FEE2Hu2OPhcHsLQHf2utSv30Ow0wpt2ZIFY1YWSdZ-td85KYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ‌مجلس: معیشت مردم جزو کارهای فوری است
🔹
بدون تکیه بر مردم نمی‌توان کاری پیش برد. آثار مخرب تحریم‌ها باید آخر از همه به سفره مردم برسد.
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/468138" target="_blank">📅 14:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مهلت انتخاب‌رشته کنکور تا ۲۰ مهر تمدید شد
🔹
سازمان سنجش: مهلت ویرایش و انتخاب رشته برای آزمون سراسری، دانشجو‌معلم و پذیرش صرفاً بر اساس سوابق تحصیلی، تا پایان روز دوشنبه ۲۰ مهر تمدید شد.
🔹
این مهلت به هیچ وجه تمدید نخواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/468137" target="_blank">📅 14:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSTm6x33zwX19SRLrGXJVitSE39qef1GOUxJPSdnSisPhIqjrkn52YD2rWZ8vj1p_aD_p-BDzUuBr8LuA0103TbCzWsE7cfUANMQjU_LnVyxwsiDRuC74KRuTPkKMzcyU9POtDdSWibDyMAXOgugCNCEaET6tfsgewLuNZbgkVH5YVznInAJWenyZKsKafbA-v0J6ZbSi_-OfiqoTScp5BlJ7S3HB6ztVgFBk9rYDeAIB9jRjh1khM6VUGG_hNhy2R6TfRyAeCE6zN5GzHsTKe5sVAeqV8Mo_YJfSyVB9qMu1xtg7BrDiVIZBhCcG_iKPLcORGRXcvnp7eskulRnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی فضای مجازی: ۸۰ درصد ارتباطات استارلینک در حوادث دی مختل شد
🔹
آقامیری: از نظر فنی فناوری‌های متعددی برای مدیریت استارلینک وجود دارد و این‌طور نیست که یک فناوری به‌دلیل پیچیدگی، غیرقابل مدیریت باشد. در این زمینه چند سامانه برای مدیریت ارتباطات…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/468136" target="_blank">📅 13:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">درگیری حافظان امنیت با عناصر تروریست در سیستان‌وبلوچستان
🔹
ساعتی پیش در محدودهٔ کورین زاهدان درگیری حافظان امنیت با عناصر گروهک‌های تروریستی آغاز شده و اخبار اولیه از هلاکت چند تروریست در این عملیات حکایت دارد. @Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/468134" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b2546a2ed.mp4?token=b4A91iUu7vfOFkA9PRmOK2cQDQnrQrGJ6Bkr5kilbpR70NLX-2e2bGEMofCbKBujLFh-59OPhrQ9aavLgdZcFxCsUGGNuIcyF5KqtLQ5OAm6Rg1L1RkjBt0ypBuw46TcmVDC9jiNIn0ZnTW6dKb-urRE_odf3MjytSN8XUC62YdWRuqQsYn--dE39ekUaqsu6A5SUoVA7Ib2VOVc2cleQmPhY9oRXyR7TTQbh7q6yUj1r7StdqoOklNw7ppnSrhhLLZKN4tk43nekJP6RITBmE-HEMJlMK9KezP-stATa9hT1KZsI2PfW9J2Cr5Isb9DbwRsQ6Ivgjm5igBwOeBNoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b2546a2ed.mp4?token=b4A91iUu7vfOFkA9PRmOK2cQDQnrQrGJ6Bkr5kilbpR70NLX-2e2bGEMofCbKBujLFh-59OPhrQ9aavLgdZcFxCsUGGNuIcyF5KqtLQ5OAm6Rg1L1RkjBt0ypBuw46TcmVDC9jiNIn0ZnTW6dKb-urRE_odf3MjytSN8XUC62YdWRuqQsYn--dE39ekUaqsu6A5SUoVA7Ib2VOVc2cleQmPhY9oRXyR7TTQbh7q6yUj1r7StdqoOklNw7ppnSrhhLLZKN4tk43nekJP6RITBmE-HEMJlMK9KezP-stATa9hT1KZsI2PfW9J2Cr5Isb9DbwRsQ6Ivgjm5igBwOeBNoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازداشت ۲ عضو تیم قاچاق سلاح جنگی در غرب ایران
🔹
اداره‌کل اطلاعات کرمانشاه اعلام کرد ۲ عضو یک تیم قاچاق سلاح، شامل یک ایرانی و یک تبعه کشور همسایه، با همکاری مرزبانی فراجا هنگام ورود به کشور بازداشت شدند.
🔹
به‌گفتۀ وزارت اطلاعات، این افراد از اقلیم کردستان برای انجام عملیات‌های تروریستی سلاح قاچاق می‌کردند.
چه سلاح‌هایی کشف شد؟
🔹
۹۹ قبضه سلاح کمری
🔹
۱۰ قبضه کلاشینکف
🔹
۱۷۰۰ فشنگ کمری
🔹
۱۹۸ خشاب کمری
🔹
وزارت اطلاعات از مردم خواست موارد مشکوک را از طریق شماره ۱۱۳ یا درگاه‌های رسمی این وزارتخانه در پیام‌رسان‌ها گزارش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/468133" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdFXSYWA9iovFzAaozxj6bPNnaUAK39J4il3mIfknp7BnMmdlh-EP_ibHURHy0d-pPzufBCEUpZRIWjIxiB-Ne7vg5jNFAnjnWL7tD9M_82jp2NQSmSH86YSwJ9p14Rz-qJRoa6O4tgMoHNtgzgadKDpVd-mm8lhzo4JnGo-POoUWFTFJNfwVxY7Q8srsp_5zToIHWxAIA1cKDbRiuSmdg2yqTPbJ9PGBaqk2cL8aLhqfsCgsLJsl3ANTS4Kg9fWW8RD9efe-j2xvdOJ59zuIx3YXW5PWVbOONRibWpmIIxK881fkHL0XkoA0KEi8gQr5D3rl_6vUB1AZiROJmoBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با همتای مصری
🔹
وزیر خارجهٔ در تماس با بدر عبدالعاطی، وزیر خارجهٔ مصر، در خصوص آخرین تحولات منطقه از جمله تحولات یمن و تلاش‌های دیپلماتیک برای کاهش تنش‌ها در منطقه، گفت‌وگو و تبادل نظر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/468132" target="_blank">📅 13:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدای انفجار در اصفهان مربوط به امحای مهمات بود
🔹
استانداری اصفهان: تا ساعت ۱۳ امروز انفجار مهمات عمل‌نکرده در صفه، بهارستان و ابریشم انجام شد؛ صداهای شنیده‌شده در این مناطق مربوط به این عملیات بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/468131" target="_blank">📅 13:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqZcmaVhV1vnMKg2TDqwdzAeO9xyoiJBUdaoXlxhkb2u9VSGS5SnEAOz5Y8j6H6b5nlhYWo0I1U-w3NeV_-jlOQVESrKkF2szWvzDrzPaLhu-zOUdnwgjozJo9dPPdwEPZnXraTsUQZKcsakmd_4B5figDd6FGyZzipsigJDCLlqsut9HxGK4FspYglHlEvbtv9fIocLt9tA2VRkoenUge6GNiAgUWKofow6Dkm5BA97T6Isuqurx_eRLL7WDtb0so19HRCe4m2ZsLllxFQgXk8wm71ws-4jqVIbVf0gGLCr5-ruPqpUwynlqVryu10uMz6xLxf1vVwI33EhHmKq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بانوی گرمابخشِ دست رزمندگان جنگ تحمیلی و مدافع حرم درگذشت
🔹
فاطمه فلکیان معروف به «ننه‌عصمت» که به‌دلیل بافتن دستکش برای رزمندگان جنگ تحمیلی، مرزبانان و رزمندگان مدافع حرم مشهور بود، درگذشت.
🔹
دستکش‌های ننه عصمت در سال‌های گذشته به نمادی برای مقاومت و جهاد…</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/468130" target="_blank">📅 13:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzUV9A_vF8u41j4a7jqtrd88G-bSUHNQI4IZXEbIcIBN7JEluFCXiaVEJqNdsWd8YdQv8oCUmGO0SIEcFuqlAcyb1Pbj60RTXOnDZddfO4GFviqoeFZRd_xJyhVeKO6UeuvaCgpF8P3WBH6PdpSUu0wCdukBtsCmlnB1s0B7vaQ0UiQVPovWDlCA8dytg7xzSIVSFc4Yx6JFFDUDx1vOIL7tKsn-i2htU552SD0gLi1h9zsNPFQ2J_1KUZSxlVPwdjhWsdC-ICnXr8yIinYzNKByUfF0gW3D2yswG8aSsHcj5GNN1CRbCKbW3rJyB8mavhe-HlDmJ9rc_c6hhm9BXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
زلنسکی: قیمت نفت به‌‌خاطر بسته‌بودن تنگهٔ هرمز بالا می‌رود نه برای حملات ما به پالایشگاه‌های روسیه
🔹
رئیس‌جمهور اوکراین: همه درک می‌کنند که قیمت‌های دیزل ارتباطی با حملات ما به پالایشگاه‌های روسیه ندارد؛ همه می‌فهمند که قیمت‌ها به مسدود یا بازشدن تنگهٔ…</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/468129" target="_blank">📅 12:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468124">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoQnsUvbmMTWhOVrneFXs4DQ0LUvrcXtSjZGRVZUE1W6W6VHDNUuBk3JRWbsQlyso3bLfC6GnNl-N0HUjkEKtFrErIw9V_cW_zHOi0zZUFVJqbjX7vev9kO0jDzad90q1fzPzeKAxObIEcWw_btZakhWihkpIYDJHcIKVkd9kcwJyUKejuwdplk20_-cHNDVXV5MpX6zPoCHayNviGuQ-m1I5Dl6H7kAvgQktoU1w8jsTHN19wc8v89sZx9cQz_jATlO2ABA7rO9rZy2EPM4B5poDjlZFeSkaOyV3Hn4nsyAhYEeKwUU4PKI_pCZ24QKAJ6yJqfDtn3w5SEafF6YBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HB4cMq35GPk1oN06L1wswBe9x9_jy4DwkfwQycRxvPINyUwZ-uRHY1NmP428heiFrp197GnZ8NPkij3F4kdS0cc94PCGOhknrUfI1fR2Sfk_v4rOU17iboFLQt8uMOapA7xOH8FYqDHBTSP2x4lbVzUUobP64KPcNwYSl-RxIt-Rp3OldX18CdhFdHhExfGZHvpqgLitEK9XQH0zcBow5ZjB3d6eTeIBeWYZAcCzZf4-Jpp9wrA7kwq_Ov7nNJQsTMFUpDmTGDviqsPrDhD3UO6nrcAXT9x-PrPwnNCZPTKl_YWjbtdflB3IzJ-f5uLuKHmxr0Z9hz3HK9HiI7cvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-jCCdTyeBebUDDDUe_qBjMpAzyHwBsNghe1nlnScUZuLptPCqXnW0pkIqKptMeJFo-Yv7UctoOUA57OhjK5yunL6XpqkcL59ZpjeFzPtJYuEUd-XMok1vhCkz6PThKuf828VAwPDcTITLe1MEp23mFkXv7LnzZSL5EKvYUdaP6_cTB0igd_cBMzeu1QpWRI-Zrq_uUm5MODfDlNxq-xGrM1Ltn8gh_Sft9cy0iZkiJtDV48rVqSd0pNrtZ1WoC7I31N_ZvaLR2xvHcSmsPp7aOywfXmaPFutDqCj_1BrQI7wLKKySqBtd34P17bcjyGdofVr0qXFMPimDX8eiYyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Io_KPqGJaH-KesimUeOqZ3m1mK-WXRw6nbutrsnUkN9rWZGFU7eLJKZi2A91mBy18Ib1zV0f4ZZ5jxBdY-o_Teo3m9ReRaAB8zGgVVxv2yFe4gSVx92a3gI-ubrB8Zt1ZRksfj-wLgaEU9ZNRyTgsgz_MYwHDhhW8nEcjAUDth9pEUKoQE1wTSm4IglVd2k4Rswg45XLVfg0d9bm4iNsyhpB_aKXiTeAhnhYVBlxmsqfu_GFZLgBlfIbCIJW5IodxgVgRF2Y92iQhO1lt47phcHtlmsFuk9yzg7ZqoDhgYj9rcIrKJRR4c8_knIko4BVsY0F7URiMzzMtq1hIBIk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUmaR2Hg7udBljWUzERW-ZkRWBDdnOSSIvH73prTUzLd9nRchRpaW9pb75eCiLDvvx0tXdeYAUj2avHx8N9Iow2IA3jUD-kIKmQ8M8YHx8_mrFdvGbbTMoXb0Lw8dLyEqJl19MLgC1NRgBJsslIb6UX7_Unprd9yZvIq1MtZjPqVo_ywmQoxHGI9yd6NQGQU3QnEEQjkuip7mgIxo19qAnxXLCBgz8PtFID6ueFDqH5jrY1at2k_BAiqyAqXdKmh9OuOFyvCg7D-M2gu-X-8wQq7O3uKqOyvNPjbexMZHk_xfKfkZV5hHIIL-yC13AcflQ-zJRMZVGEQKBQtcSmgDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جریان زندگی در جنگل‌های بلوط چهارمحال‌وبختیاری
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/468124" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468123">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCQ5Mje9sRTtes9Ee64ZwOL7yGV3cOuJteMBXlWRoKk7FEOScEnF5JUwFo0N6NmXteHT2EB5wgfAAVolZcikHdkJDVmYwZA6qRQ9kWuR2alrX33qJkhTT0gYa3ufY5QykNN20mf8bHdKnLQM-BA4cRckgZWvegacPcWJsQ9vS-Dq6H3aTQ6l_RylFe-Ep_nYi3VCWYjRdQrT1FBtd7btT_sthvWW38TJyacaxhYU3Ha1OB9uQpvTw1eUo2FqPdE6Da3Qnjm9YICzfe0IOc9MNROPMMMQUgUonBqtfbiKy7yzNsFJZuBmodrvusRmC7lgBWLchb9qvK8HDGrdcRAJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۸.۵ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش بیش از ۲ درصدی به ۸ میلیون و ۵۱۳ هزار واحد رسید و رکورد تاریخی تازه‌ای را ثبت کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/468123" target="_blank">📅 12:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468122">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5BVWnChPEDCQlobkIeaZoGcs0qILL1dfaQw5LkB6_z7edPzNw9EbfUgVpbWCFFheznlozLZAg5YdufQhhHMr7Wp7yOX2Y8YV2-uXXTldUwvfnZQZwuHt6Jkc1xW-JCfit17jpjoVjJGQgsp0a-x_Ul7H7zeC7_CvhMq7wjuMksTrjOCd02AIaGvePCxtjjF46jzR4rocKLFgLMDegkNowcHahFdp9Q7qiFNLmEzep6Z3wGkTk7P_OnIWgK2hJo1RBgfVlTYz-b6p7yKtokjzJNS66CVo0e1fN05euu9VWEJ8k-kI3KEsVFCYkT2_dSMc55P_cLTJuz1DL8OZNEocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تغییر زمان برخی مسابقات لیگ برتر به‌دلیل حضور تیم‌های ایرانی در آسیا
🔹
با اعلام سازمان لیگ، برای کمک به نمایندگان کشورمان در رقابت های آسیایی، زمان برخی مسابقات لیگ برتر تغییر کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/468122" target="_blank">📅 12:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO_xmCaHbTHVtmSr03lxmAVz6V8t3I9G1hVYc4rmHy2c969R7OOXqR5M-ESTxHGeAfZ_KvEHwpodLGYO2EGLHW-fkt77j9Ecs6zmeATMTKz4Yxfrb2tLBxsG4DQmWc7sgtaBifCiI86xs9iBdRu1Yq3wBGNvc7TCs9vbtlAS7S8LwNjFUT_7rrtse86QxSpGj9LJDcNI0zUz-CpM73ha6sFGbvzzM2bFezW0zQbS6OCYb4_QOZX9iY3nVHG9n9e_V_Ga1_CQpx7RV1H1bSQVNTsj_Cgp7GthKVJK2KowBjiBuULF_fNp9ECkwVXe_gKJl0HnzWBeE7O9s23g8ilmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ خواستار تغییر قانون برای سومین دورهٔ ریاست‌جمهوری‌اش شد!
🔹
دونالد ترامپ با اشاره به ممنوعیت قانونی انتخاب‌شدن برای بیش از ۲ دوره ریاست‌جمهوری گفت که اگر قوانین آمریکا برای فراهم‌کردن امکان نامزدی او در دورهٔ سوم تغییر کند، از این تغییر استقبال خواهد…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/468121" target="_blank">📅 12:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468120">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlWHRnclzCH_H2EK9IItomtuF0hkuz_6vcJpLO_IiD8wDgG16aW93LijDX_5ayy2QlPMpR8_5MXXR0gAORPCINWRCDGeTB8j1Ya3y6COiWTij5PqJ6O0FM6e7OzcjUvyNG06ibPPTV6kmgcO0l01TQ4g1FHX35Jz89JX84YSDZi_6bbry5wflSLJ4ZSq7OTK7yawwT3SCi8RRzmJpeG_d39GEqeAcEGiJ0XxgaoHR5KotDyAfx9gJKkzt4JbR2d8NzWjEEuF4TSAtqGY98bbD_iZuqWsRrkjyOH-iAShOjVBQN_Y1Pc_BObcqE-iDYFEUiqD4Cwo8uTR1oWxqO8u7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی فضای مجازی: ۸۰ درصد ارتباطات استارلینک در حوادث دی مختل شد
🔹
آقامیری: از نظر فنی فناوری‌های متعددی برای مدیریت استارلینک وجود دارد و این‌طور نیست که یک فناوری به‌دلیل پیچیدگی، غیرقابل مدیریت باشد. در این زمینه چند سامانه برای مدیریت ارتباطات ماهواره‌ای در شرایط خاص طراحی شده که یکی از محورهای آن، شناسایی این ارتباطات است.
🔹
در حوادث دی‌ماه گذشته از یکی از این فناوری‌ها استفاده کردیم و ارتباطات موردنظر قطع شد. گزارش‌های خارجی هم در این زمینه منتشر شده؛ البته این اقدام در محدوده‌ای مشخص و براساس ارزیابی‌ها و تصمیم‌ها انجام شد. پس‌از این اقدام حدود ۸۰ درصد ارتباط استارلینک در شبکه عملاً قطع شد و حدود ۲۰ درصد باقی‌مانده هم کارایی قابل‌توجهی نداشت.
🔹
این فناوری‌ها می‌تواند زمینهٔ همکاری با کشورهای دیگر را هم فراهم کند. ما آمادگی داریم فناوری‌های مورد استفاده را با کشورهای همسو به‌اشتراک بگذاریم و در این زمینه تعاملات و هم‌افزایی‌هایی در سطح بین‌المللی در حال انجام است.
🔹
تجربه‌هایی مثل جنگ اوکراین و جنگ تحمیلی نشان می‌دهد که این فناوری می‌تواند علاوه بر کاربردهای ارتباطی، در خدمت اهداف نظامی هم قرار بگیرد. این فناوری می‌تواند برای فرماندهی و کنترل نیروها، مدیریت پهپادها و ایجاد شبکه‌های جاسوسی و جمع‌آوری اطلاعات مورد استفاده قرار بگیرد؛ پس نمی‌شود استارلینک را صرفاً یک ابزار ارتباطی غیرنظامی در نظر بگیریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/468120" target="_blank">📅 12:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبر فوت میرحسین موسوی صحت ندارد
🔹
از بامداد امروز شایعاتی دربارهٔ فوت میرحسین موسوی در برخی صفحات فضای مجازی منتشر شده؛ اما پیگیری‌های فارس نشان می‌دهد که این خبر صحت ندارد. حدود دو هفته قبل هم شایعهٔ مشابهی در برخی کانال‌های ایتا منتشر شد و پس‌از آن در فضای مجازی گسترش یافت.
🔹
موسوی ۸۵ ساله در ماه‌های گذشته به‌دلیل بیماری و کهولت سن تحت مراقبت و درمان پزشکان قرار گرفته و عبدالرضا صدیق، کارشناس حوزه سیاسی دراین‌باره می‌گوید: شایعات هفته‌های گذشته دربارهٔ فوت میرحسین موسوی با اغراض و اهداف سیاسی خاص صورت می‌گیرد.
🔸
انتخابات ریاست‌جمهوری سال ۱۳۸۸ با مشارکت بیش از ۸۵ درصد واجدان شرایط برگزار شد و پس از اعلام نتایج انتخابات، میرحسین موسوی ادعای تقلب را مطرح کرد؛ موضوعی که یک انتخابات بزرگ را با آغاز تحریم و مشکلات اقتصادی به‌کام مردم تلخ کرد. پس‌از حدود ۱۹ ماه فتنه‌انگیزی و تشویق ضدانقلاب، در بهمن ۱۳۸۹ برای موسوی محدودیت های قانونی تردد و ارتباطات مقرر شد.
🔹
برخی تحلیلگران حوزه بین‌الملل بر این باورند که اگر فتنهٔ ۸۸ رخ نمی‌داد و کشور با آرامش انتخابات را سپری می‌کرد، آمریکا مجبور بود یک ایران قوی و مستقل را پس‌از انتخابات ۴۰ میلیونی به‌رسمیت بشناسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/468119" target="_blank">📅 11:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468113">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6JAKDtbJQIklak8VNBHUgwvCpIrQy4CMxcEiJjGsgRI19EDnzqdQaqImYzsDfd6ZEDAs8TJ1VsKxqr6_R-eLYLIntrgHMiOetJpE5fFstS8sw1cnlISxcC7jaWdcyBdu8H47oyqYwQpmMQF2O3eeXa-iFNr8oSDO7EhbU-jgGJhRA8cge-5LuH3cnSJqZv6yEXk-ZGriGBIk4rbS0csHHwfem4dvU_P7QI1SSn9gcdIGHN-T13JjMd7g1hortvzQpcmjm1U8lH8Do8DsWuqVwtLqYHKxay2bfDj1BAIBbcoje7CTNjkjUcBA015-D5fGhoWBi4EJZuKPTFwAgZrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfUv_z8QzMNeMqDMBjn0GPwIiWFa4b5ggoJ7RzIKZJtECPCcyExGEiL1h0JbwsRGAAPXrGZLmpCtTDlGAf23ay8wYBt3yO3zYYBrqoEKYT55Oz7rbWvpwGLYDENfcNT9Sy0pNX3PRDg9gsAg_4_ChTRH47hQTTqK7uDw2cGsEafBuEwQ2McQpb2DhdHC387pCI-ceU8O-4wcDVvFoZg-hHtjQaWLeM49sVzTzdqVJ4gw0cH74vcqR6AH-Hyqp0lIxAAIjpm7vQkNDffIYnKHaEA7wV0Ju5lbtfHRpkNYHKIhJBO4g02c2utNwSmoOcNZp7hC7y857-zQQ78YjeKSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5IyfeUUUnVEbzydUSu9UkJgB1RQOKb7bBvLhiyqBDENH7iHUcQFu8zartzENkstf4XfEdoVZMMPl7hTaSUcd7QqWiVGtFBhiLO4oFa6Pg79uUHkkYQDi_UecddAhPNlvaRtOY-xR8dt0tHujd23lxaDtbOJHXcAJuwrZ37Nt41Dn824tKQInPlZvPlcDvNrAcqHHGR9vz3wnNH6D60Hx3SI-n9MOYw81tIZ79RFhHVPA7lKKv3yjfpEEbj8osjeS413L7dAQ1LhEw_QRwAQQviJbODk7jIZYRB9hRgz5p2JBFTR09VGkW-V9Uj53zNFrzIfp5Qd7HOHBiaG2buj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtQlGPKg53hpDuQ0Wr65RMuqVieUWWRvrLirZc4Ng_elsext31gLJH-0_tis_m8MU-qNkyoamldk5gFEyRkQ_AFzInbTd-PaIfoAe0i_emfb3v9SqrwJnyxv5nA2q96U1yd_urvl9Khiq0eiixlV0M2Z5BRZ43Bmj2dHz9GxhZ4kzd85gbxJZrVgawkdcLfHhYLEfC1uJSzwZID9r_BOf1yYqhnqRkgWej4g0InMbC5MHWFNOv_XQJw_NR-9-pPdkRQdWDWq5dLrKaPayfQqFYhThO5TYROCq2DjIFlTqUt9Q-jf1JcShD09Atwn6Vt9093QN8xRBAXZWHo-cmsgSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCHFne47m_XQwOzw4zzxvYW5PBhn-XDWJxy6w3DkbL20hLyBB5fGAlkqsicUOF7JFg57noGjS5i_xKyN7Mf0i6LSN0kcRfwKDDyFXQ5vGx-sHvt7VEjdmDMeSIh5rIia-UvGRL4cT1-hfD7JjOkWOC66Yv6_u714QzbWAbYdVMdIOT31-l3291fW7oZBMdTI2C4dfRPBVt7DG-fPfAhQzi44nHQQhv6aKlTUh1jM562n2qEvlURrAy_JxWTVOjstjs-gjZb6A_Vsh_DI-sl4UFjakgOKdtQPemWeJcvDHH-6ZVSSE-0OM8V4gcsjRU9hxfKLQ8EJ1hacDU3wwfkdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRG3pv6TAuMQOETY3v54KBYdoTq4cM3aS3_2CFoG3gtXNMFPSaIOS2itibHqWBB1Sa6NkVZspKsnitQVPuMuGVnKOD-6Ul02nxgIJ-0XUlPZw_9Finn2KS9sBeVBkc3qfxEi0GGsS5ueuCN8XPzczVaAdMrb3n4Ow343qoOTACsdCl2ZLUP1haDhcDZS3zFxYpCdexwd2vC4V9R90lvL1Ew3icrJ1yNjxfTEIk8GKoAsEI8bZvGxXoC8p87OSjffYRPACQAQnrYeAxyb9mRUxOkSPfmrD0i43hJr6kN8qFOsbNgZVea9BuFteqvF23exBgQxWp2PcFIPlwSd90LOLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نفوذ هکرها به شرکت تأمین‌کنندهٔ تجهیزات ارتش سعودی و انتشار ۲۰۰ هزار سند محرمانه
🔹
گروه هکری «اویس قرنی» که خود را بازوی تخصصی سازمان دفاع سایبری انصارالله معرفی کرده، از انجام یک عملیات نفوذ سایبری علیه شرکت «محمد هادي الرشيد وشركاه» با همکاری نهادهای امنیتی جبههٔ مقاومت خبر داده است.
🔹
این شرکت در حوزهٔ پشتیبانی و تأمین وسایل نقلیه مرتبط با وزارت دفاع و نیروی زمینی عربستان فعالیت دارد.
🔹
در این عملیات حجم قابل‌توجهی از اطلاعات شرکت استخراج و در اختیار نهادهای اطلاعاتی انصارالله قرار گرفته است. همچنین اعلام شده که ۲۰۰ هزار سند محرمانه در وبگاه گروه هکری منتشر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/468113" target="_blank">📅 11:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468112">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ea908237.mp4?token=NbZq39hKYX1UkUTc3yId-hTx-t9f1BGhDL6z5YE6mBpd0V4NLhT7YBa97Y6GSj-rVUCgsZiWwh-bJzDLlNhEp8HDIAzE4YmTxme_aLMPWvoFAQGp4l6PG9ZPkPtdD909EYKi60B8t4VvBRWStTxV8cJxJDpLlTpdVU1o-FSMtLH6BSCzJgz7f0C2NS7YDw0LgxyG6n99R62OEo6reUt2PLh7jjs5s8uLMcbH2_I8CLMSplV2mKWX6k-GZA3WAE9Qdb_0pveuIMl5EL1jbejW543PPhkXGrT62xxu5ggXoFeeV-oItetMp4m3H5pVbtoOWQQx116jxlQphgNe5MQ2Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ea908237.mp4?token=NbZq39hKYX1UkUTc3yId-hTx-t9f1BGhDL6z5YE6mBpd0V4NLhT7YBa97Y6GSj-rVUCgsZiWwh-bJzDLlNhEp8HDIAzE4YmTxme_aLMPWvoFAQGp4l6PG9ZPkPtdD909EYKi60B8t4VvBRWStTxV8cJxJDpLlTpdVU1o-FSMtLH6BSCzJgz7f0C2NS7YDw0LgxyG6n99R62OEo6reUt2PLh7jjs5s8uLMcbH2_I8CLMSplV2mKWX6k-GZA3WAE9Qdb_0pveuIMl5EL1jbejW543PPhkXGrT62xxu5ggXoFeeV-oItetMp4m3H5pVbtoOWQQx116jxlQphgNe5MQ2Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان امور مالیاتی: سهم بسیار بالایی از درآمد دولت را مالیات تشکیل می‌دهد
🔹
علاوه‌بر این دولت منابع منابع شهرداری‌ها را هم از طریق ارزش افزوده تامین می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/468112" target="_blank">📅 11:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468111">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8mVLno0zD9H-MFI8vqEUsKEsMJlZRvNUJ8yLn2aFxIhWjcsXAT-48XCcSyXVsIyclX_1hXGkHcnBcHqjn6Cg-PDfeN9sthr36ZOvhbJ97P0s7K_DUamER79YmpWk8RAXrc5DvH_wYeuCud-t0gFfPTS5ywl-C6ZfUH61q0AIvy_mgu_sn_UNWVtixw7mSPKm2Z9M_pJpjUNheCYDdSV0Bq6zK6-HWhjIcPmxDTj6XmEbtKe_CnRIGZU23VHq2OYjIPUFLN8w58TbL1qtXWjb5GJSpHRFHlT2eDbt8hDbUj4roUn4LxK7ENRSgLNolOiiLAagpC5KKVeb5g_NONxwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مهاجرانی: افزایش کالابرگ برای خانوار سه‌نفره‌ای است که زیر ۲۰ میلیون درآمد داشته و خودرو و منزل هم ندارد
🔹
سخنگوی دولت: در مرحلۀ اول سه گروه افراد کمیته امداد، بهزیستی و افراد مشابه، یعنی خانوار سه‌نفره‌ای که زیر ۲۰ میلیون تومان درآمد دارد و خودرو و همچنین…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/468111" target="_blank">📅 11:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468110">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f1e7b919.mp4?token=rH8lMmP2oV-LuFuCDwvkb2FZIMlpRfmf6Fr856VAZF5m9HlL-pnmH3M0HAR7oXzyMAbtsiPc-l-rDd-8uDy7ZNoBuOJDLF6HLxB99OCOYl4qC0XPYdGjiAuF08pVIIkIF7Qb6Pdq4mjkyEmxaMHSBsV4PP-ba9pWof91iMbOJfgy8GLnKE1daTP8Zppnv51W3XK9yOtPsIqc9RthezTHGMriCjinBLZOKTlKNZGnoWPWl544P5Rm-s6zEH1wZoySZ9vIfc06FVi_-x_mVY_PFwwSzUN7GJX-dI712GKl7gxskynUpu_Av31YVZS1VmgYRkyX8aUFpQyxeIKT0aFuSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f1e7b919.mp4?token=rH8lMmP2oV-LuFuCDwvkb2FZIMlpRfmf6Fr856VAZF5m9HlL-pnmH3M0HAR7oXzyMAbtsiPc-l-rDd-8uDy7ZNoBuOJDLF6HLxB99OCOYl4qC0XPYdGjiAuF08pVIIkIF7Qb6Pdq4mjkyEmxaMHSBsV4PP-ba9pWof91iMbOJfgy8GLnKE1daTP8Zppnv51W3XK9yOtPsIqc9RthezTHGMriCjinBLZOKTlKNZGnoWPWl544P5Rm-s6zEH1wZoySZ9vIfc06FVi_-x_mVY_PFwwSzUN7GJX-dI712GKl7gxskynUpu_Av31YVZS1VmgYRkyX8aUFpQyxeIKT0aFuSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات خوداظهاری برای افزایش مبلغ کالابرگ  @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/468110" target="_blank">📅 11:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468109">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b596a913.mp4?token=cotFhT7J_bOZz4h4nMcqGWx8BbnHCzgtOi52aN-mUoMbx9r6EdKZtK4dTCPPNG-EHWNCLl_noMiXVZdMgum6HEYrQ0I3_iP3kaC6gxpEv_wbzfegN73UL69wMNCmO8Uq2Pz2Cvi5bsJd0TrYRpicq1n-BXQa0T9GOhU-yDjZtFcUmJpUf5lQDZHgX_RQqqwX94DLvRNbvWaHHAjA-MW2DyPsSnMDmcbSP2Wc4NNkJ_cc3pNwT2TyDcBlzJx3R4XQSdRA7rmopbIhtqWQpWheCtpMVDDgpaj6fYsrLIc_cA-zhfz90PlqFAj94xbpe50P_uIDQacAnUe6li5ecklbmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b596a913.mp4?token=cotFhT7J_bOZz4h4nMcqGWx8BbnHCzgtOi52aN-mUoMbx9r6EdKZtK4dTCPPNG-EHWNCLl_noMiXVZdMgum6HEYrQ0I3_iP3kaC6gxpEv_wbzfegN73UL69wMNCmO8Uq2Pz2Cvi5bsJd0TrYRpicq1n-BXQa0T9GOhU-yDjZtFcUmJpUf5lQDZHgX_RQqqwX94DLvRNbvWaHHAjA-MW2DyPsSnMDmcbSP2Wc4NNkJ_cc3pNwT2TyDcBlzJx3R4XQSdRA7rmopbIhtqWQpWheCtpMVDDgpaj6fYsrLIc_cA-zhfz90PlqFAj94xbpe50P_uIDQacAnUe6li5ecklbmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: واردات انواع خودرو، از جمله ون‌ها و سایر خودروهای ویژۀ هتل‌داران یا ایرانیان خارج از کشور موقتاً به‌حالت تعلیق درآمده.  @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/468109" target="_blank">📅 11:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468108">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1d060515.mp4?token=QVVAeU6dSuJs5gc1aNa2wM7O_UAziRduIv7_ou77QCIO0vqBwqnoxnv1bRNbmMjF2P_jGJ2VYZ_6d2c9kkvStqtQj-Q4wDILvnRBbzuPc3yuaOl5F30dTMlQYyrVuC2YOfZzZ0hSZzu9BjUA6mW3UB9X0Ai-ecMFmuH_qrBOVaOv1Q-Ku5iffU8kbAEA6lvKnYbgNUAKKKPdlJH1vQDOdQlyAsdqorMf_aybmerZK2uLi7lYaqF_JHhEUY7LrTwDQXHdq1Pyh9ERzl0PbxgiMOG5FAGmpo0Oa7BXjWsxu3GnBt7cdpSUTEueE82eoDBCbuNs0VtW4GVDyksDzoZoyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1d060515.mp4?token=QVVAeU6dSuJs5gc1aNa2wM7O_UAziRduIv7_ou77QCIO0vqBwqnoxnv1bRNbmMjF2P_jGJ2VYZ_6d2c9kkvStqtQj-Q4wDILvnRBbzuPc3yuaOl5F30dTMlQYyrVuC2YOfZzZ0hSZzu9BjUA6mW3UB9X0Ai-ecMFmuH_qrBOVaOv1Q-Ku5iffU8kbAEA6lvKnYbgNUAKKKPdlJH1vQDOdQlyAsdqorMf_aybmerZK2uLi7lYaqF_JHhEUY7LrTwDQXHdq1Pyh9ERzl0PbxgiMOG5FAGmpo0Oa7BXjWsxu3GnBt7cdpSUTEueE82eoDBCbuNs0VtW4GVDyksDzoZoyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: منتظریم حدود ۳۰ درصد از اعضای مدیریتی را زنان تشکیل دهند
🔹
نگاه دولت این است که نیازی به دادن سهمیه برای استفاده از ظرفیت زنان نباشد، ولی طبیعتا چیزی که منتظرش هستیم این است که حدود ۳۰ درصد از اعضای مدیریتی را زنان تشکیل دهند. @Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/468108" target="_blank">📅 10:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a591024d0c.mp4?token=E8qaAvqweCwhlfytorgaUVfvQ9xbU5JBknQj72dPvcRWMCCBhH1pv1Vi9CRTThBoWRsKIsDTjuiEbAkrRXw0kXZxN6FBO_lIEZzKdLhf76uQBr9NT9eiYLkcs_Zmmhbk0ROxRBhft-jfs3FbBxY-fuTEdmYzT-nAyGuh7r1b_cFLPv_GOUdyxSvMlghTc6VGLEbLMkRBSc5CNNl-UphxEVCaz0ji7BIB--uVLej85AsIYmzea7-nREMZl00mFJcziNJh65fApIBm7A9kUzYWPzYRu8KB60cRQNsOE3XrQxIHzTzzLB88zYjoHHRzil2xglTduUhGp8VwhOJJLLz_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a591024d0c.mp4?token=E8qaAvqweCwhlfytorgaUVfvQ9xbU5JBknQj72dPvcRWMCCBhH1pv1Vi9CRTThBoWRsKIsDTjuiEbAkrRXw0kXZxN6FBO_lIEZzKdLhf76uQBr9NT9eiYLkcs_Zmmhbk0ROxRBhft-jfs3FbBxY-fuTEdmYzT-nAyGuh7r1b_cFLPv_GOUdyxSvMlghTc6VGLEbLMkRBSc5CNNl-UphxEVCaz0ji7BIB--uVLej85AsIYmzea7-nREMZl00mFJcziNJh65fApIBm7A9kUzYWPzYRu8KB60cRQNsOE3XrQxIHzTzzLB88zYjoHHRzil2xglTduUhGp8VwhOJJLLz_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: منتظریم حدود ۳۰ درصد از اعضای مدیریتی را زنان تشکیل دهند
🔹
نگاه دولت این است که نیازی به دادن سهمیه برای استفاده از ظرفیت زنان نباشد، ولی طبیعتا چیزی که منتظرش هستیم این است که حدود ۳۰ درصد از اعضای مدیریتی را زنان تشکیل دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/468107" target="_blank">📅 10:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">درگیری حافظان امنیت با عناصر تروریست در سیستان
‌وبلوچستان
🔹
ساعتی پیش در محدودهٔ کورین زاهدان درگیری حافظان امنیت با عناصر گروهک‌های تروریستی آغاز شده و اخبار اولیه از هلاکت چند تروریست در این عملیات حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/468106" target="_blank">📅 10:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468101">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdOXs5-4ixTxVD0a0SmkKV_XUYNzyge4KAubQ1WsoIX5joHph1SAfZ3vxgF9rU4SZ_TM_WBPMVunl1Zuj3SF3dZeSIBcaM5gJxYoUwwxaTfvJ06vaU1GdIx-gBBJyTyCETeOCIQD37r0rbW4RGDGdaOjBDGYD32ra1-7pbMSR5G7QUaJYWg8HLacP43UETaUZyUV44qzReUxMDSQFXHst_yitfDPLq-CnAt23GFf_Ji4C4fM2uQ0ubkWgJcHHD_xTrKJu2Zgaq_OQLMJ933LKOAL_a-7iLc9GOi8PLu8ghoYETXEWvgr2aooh3Esc6APsNcSxGLkUdqBIlgVwfLwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UY4Jb8qPFLwPSGTx99NTv2CoLJjV7G5iDECudLffRwt3QNAjnHMCJ-BHnefGU1__TmXQl7ESCDZcm0dbEdU8aOuOnKgONZPwLHvlT2aNwsSUchYkRqynHV44zMMR_keNsAA7cgoycDribzi3x4vYW7mOMN7xQIJOl0LKQkk58X1JnrJwBgMtb_U5PnwE-1d82jtOhcguK6vjjd8xFtRdqs4K8yHfQY74bMCHd4Q8IS4-wlJ6gPwQVRsE2d1l-07WGUHhdGyPuzD7-LTxkoVF8D_22YvlLLKFNjoPfOFjxer716DRRm-PbWgBWmG99vijN7yGh0zwNdBaze_724iIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3Dw6ZLhtmMWo3oWHRr4p0h7-ee_G41QC72oZtsijqr-gRu7nRoFWu-rso2YEgSGU_2gV52Q5E66Qy8CMve7rIrdc3AopYAYo9YGa6vJIGpmow960WmrCQfqUE0THirgublfYGBlUyul2d9RubQtl5r1KpksQNDPUOxMmjkxFuW1H4IwvViQd_lZm9ZSpcvqkQoF_s9jSuNd50tKdGO2jPcksMgfudHwTyLa3LoNgaPt-1yG1TcPYTVNht4ott2PSDD6Beey6u4s51G31kmzp_NtwNKd9I-oMFjbfAW4bf_Jyfjeu-zai9qhpX6zcBnp3Zn0IZ2ERJNSCxuKAvM0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2Ld1xzQxqL_IN08ELs1WSRjqFGJU89ZtutEMGyOtq25DT4ZhwlPcE6_nQ1pJohajGMuJk3wOc9A7sYoHITsLnAKRVTJrLJ7hLEDA34-kZpymF_d2ymGqQvlkEP1Q1AOF31U4qDOnCrgBkk4AAtWKRA202OTs16JmnR_PgXj0-h9lBtAqb1-gWPNRNh6z6PP2wi23eYugOEsKku59qnipPZyIdWB8AjcN1WlhIWxAp1Sm0QUdgcbBHl6jptNDUE6hA4EofntElX8kQr8immV3pzJLMSPDgmXOn4n2PjB5S7hOBoaYiKTgB1YKIRbisHFKKpLSmz5caOijthtsoErbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejyJ_MFoPIxTWdt9RWxVbwJ9BaIkLGNKk6O4Wf5RGi16Vh7MgaQdYXUzOesmYKH6XC9tIloyIM21VADTphwvNRVIc3oSeshJ0Du0pxA4jSCcDHTnYUN5QBPDawAoy0mDSD-QX-TwOF3WAM3LPN0orwx8xCD-JMs68H9XZ1z4wDA1wgKM_eHFlnrSWgHVgqQPCO-n9M58hF40zfIbjPs594ui0L5iv3lJ9ENZ0bMus_X1t_HGOauCEEluLhgA9Sfj-dKp0WO8YKsG3s_Y5vxPjFGhiVZfzWTbKDnqAiNj-JYdYOF_xgTFX4b7Mcw527ih-Myhv95nrF3VsWKW6W3ItA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخلستان‌های شادگان؛ شکوهی که تشنه است
🔹
شهرستان شادگان با بیش از ۵۷ هزار هکتار نخلستان یکی از قطب‌های کشاورزی خوزستان است؛ اما نخلستان‌های این منطقه با بحران جدی آب مواجه است.
🔹
طبق آمار ادارهٔ میراث فرهنگی شادگان، تعداد نخل‌ها در ۱۰ سال گذشته از ۴ میلیون به ۱.۵ میلیون نفر کاهش یافته که ناشی از خشکسالی و کمبود آب است.
عکس:
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/468101" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468100">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959e356000.mp4?token=f-rZ_j0rDL3sSEqlsZsXd9UhWjKwuQMUItibqNzOwlR3ESTkD2t65gtrpoNme2NzUIiKWAfwg8zFGQUtOKpT-yLp6m0bx18er5PHn-Fh4kmbtCHminHlHyXsArIuSm_psZ3GVaI4r1EeAUgGkkbqzlK0zrECVi0hX48gGLyrjxAqqAinC9FzE0TRNvVTV3GPBTmPpIjCOHpuNkj7Qag3cUyhS-ap8WB5x1aFMPbCh8_sByAxCiQ9SXnJ_hPNBCsYoQiASYBFLUdUK_cIm0vwB9d0t6rIu99pPuh5uT1gHpu_BXe7uTJJBTCtvY9_LC-GEv_y_QuJTlNZlhsQjQUy-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959e356000.mp4?token=f-rZ_j0rDL3sSEqlsZsXd9UhWjKwuQMUItibqNzOwlR3ESTkD2t65gtrpoNme2NzUIiKWAfwg8zFGQUtOKpT-yLp6m0bx18er5PHn-Fh4kmbtCHminHlHyXsArIuSm_psZ3GVaI4r1EeAUgGkkbqzlK0zrECVi0hX48gGLyrjxAqqAinC9FzE0TRNvVTV3GPBTmPpIjCOHpuNkj7Qag3cUyhS-ap8WB5x1aFMPbCh8_sByAxCiQ9SXnJ_hPNBCsYoQiASYBFLUdUK_cIm0vwB9d0t6rIu99pPuh5uT1gHpu_BXe7uTJJBTCtvY9_LC-GEv_y_QuJTlNZlhsQjQUy-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخواست عجیب بیرانوند از نظام‌وظیفه
🔹
علیرضا بیرانوند از سازمان نظام‌وظیفه خواسته تاریخ اعزامش به سربازی، اول آبان تعیین شود. این تصمیم می‌تواند به حضور بیرانوند در ادامۀ فصل با پیراهن تراکتور پایان دهد.
🔹
این درحالی است که طبق برخی قوانین، این احتمال وجود…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/468100" target="_blank">📅 10:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468099">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33f44b75d8.mp4?token=oUIipJjlGeg7RkHYMcqa-uLoP8pvvKMklilTw5zfhY150xovOyHwaR68D87f3S_I8zbGOQB531ZKI6yoYI99qD90mzv05b6gQMEbDM0tZODh0Cwp1LBkW9NibbcLvV6kj1t2VmS8IJmfw4SGp3K0P0nZyDlPg0q3l3rFcprKWqa2EpRWxGY1OLmecKeshGXvknAm4sdsoPrWQqKouuKv7lCYUYcSKidNwrZ6ERnOMnlbyoEVOhJw5xroMwLHtEW867ZWVUEYw7CbQv4I_u9saT2sud2wRIIKzK2XilTVy_BsxEmZcSasm6tq9Zu___QrT_AwaE9ttV2MzJY007mcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33f44b75d8.mp4?token=oUIipJjlGeg7RkHYMcqa-uLoP8pvvKMklilTw5zfhY150xovOyHwaR68D87f3S_I8zbGOQB531ZKI6yoYI99qD90mzv05b6gQMEbDM0tZODh0Cwp1LBkW9NibbcLvV6kj1t2VmS8IJmfw4SGp3K0P0nZyDlPg0q3l3rFcprKWqa2EpRWxGY1OLmecKeshGXvknAm4sdsoPrWQqKouuKv7lCYUYcSKidNwrZ6ERnOMnlbyoEVOhJw5xroMwLHtEW867ZWVUEYw7CbQv4I_u9saT2sud2wRIIKzK2XilTVy_BsxEmZcSasm6tq9Zu___QrT_AwaE9ttV2MzJY007mcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گزارش وجود بمب در هواپیمایی در تل‌آویو
🔹
کانال ۱۲ رژیم صهیونیستی: گزارشی مبنی بر وجود بمب در یک هواپیمای شرکت دلتا که در فرودگاه بن‌گوریون فرود آمد، منجر به تخلیهٔ سریع مسافران شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/468099" target="_blank">📅 09:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468098">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان سمنان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08396681e1.mp4?token=NDkR1rMc68o5ft_5JHS8jC6RSxc9aGn_6nZi2sI7WhF3xQCb47iEmN2dCAR-QvRZChrRmCI9E4AY1ocJ87V7KCKDtT-5UWOFJNr9ZKZdkpwcwVWIDb0uQvl2q6gx1y6XH-C6rTTvrZCBx-tot6MWOyW40ciqg_5gHbpXaVndasvjdDk84JWuuMk6RcoyKWSd6TEiI2SH4q2jtAwxt5vDVubLXWa31mFUhYdvObygkMk4TBBHU0kyRQnnmBhgdiQSCnyxmJxOUf_vhN9i9uoWxPQfVJggzvyc1lZrb1Fhix3KfMvJDIzY_RMMZogGHKQ4qIRSJ6WrzMSmr9u7FZRi8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08396681e1.mp4?token=NDkR1rMc68o5ft_5JHS8jC6RSxc9aGn_6nZi2sI7WhF3xQCb47iEmN2dCAR-QvRZChrRmCI9E4AY1ocJ87V7KCKDtT-5UWOFJNr9ZKZdkpwcwVWIDb0uQvl2q6gx1y6XH-C6rTTvrZCBx-tot6MWOyW40ciqg_5gHbpXaVndasvjdDk84JWuuMk6RcoyKWSd6TEiI2SH4q2jtAwxt5vDVubLXWa31mFUhYdvObygkMk4TBBHU0kyRQnnmBhgdiQSCnyxmJxOUf_vhN9i9uoWxPQfVJggzvyc1lZrb1Fhix3KfMvJDIzY_RMMZogGHKQ4qIRSJ6WrzMSmr9u7FZRi8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف ۳۰ تن گوشت فاسد از یک واحد تولید همبرگر در شاهرود
@SemnanFarsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/468098" target="_blank">📅 09:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468097">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95bae94013.mp4?token=QaWrjbOZiUihM8oqxjbZtyoHGR5tvAWcOgZ1OsUCGPkslQSnlGK0jyJ4xCSt8ATTwKIuJ6IWetYFG5jXSDSwhb-sEEdoKEjZXZnCcpLoz0TNzWR_oJMvW1dldzprsVP75GsQ50r8vd6L6iftgEIpvsqqO7AVHhHpPCPnDEpxaaH1b96ucx7K4hn-EJ8P80N-kRj5vh2l1m9iRI30d7I4ZWswcrohhRGnxXOXLgTKpKwEF9phhYNLh0OmdJCw1-qxDmJJwBTe1ccnQyFd_KE0TUYGj50kZF_mYZKPk_2EbnAdcojtD4CMOnnz_3CoeXUmVw7tEso4_kAZiZhqbK5zl4XPsBL6TXceFrJeczLsfSDqEnOLDt2PTBHX76SGp6JlPahT0D0O3u7sybMKQ-_HUzKGdEA6WzuUg-XpFIPf4BVs4KV7AB8wuFmvvaBEA3DNJSNaHLmYbn0mnO2bjGKDNO068j07Ww943AclejNO5OgLC5iRzBMRaJE6i7MaaSNxdb2yk5AyQdtt690Eg-ZnBn-ryYK31WZ8wizzhQtqvZzNlg6fdibQhMN8shzP6z2Ay3KmfE7ybb6tfzlTDuAl8qy_PJhNJ7Uswlj3_xc_kzjzfRbk0zMJa-BgbKCSRE16_pRzKMFo4Zas8iRJFiOKkZuVTP073MSIVjuCTbbC724" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95bae94013.mp4?token=QaWrjbOZiUihM8oqxjbZtyoHGR5tvAWcOgZ1OsUCGPkslQSnlGK0jyJ4xCSt8ATTwKIuJ6IWetYFG5jXSDSwhb-sEEdoKEjZXZnCcpLoz0TNzWR_oJMvW1dldzprsVP75GsQ50r8vd6L6iftgEIpvsqqO7AVHhHpPCPnDEpxaaH1b96ucx7K4hn-EJ8P80N-kRj5vh2l1m9iRI30d7I4ZWswcrohhRGnxXOXLgTKpKwEF9phhYNLh0OmdJCw1-qxDmJJwBTe1ccnQyFd_KE0TUYGj50kZF_mYZKPk_2EbnAdcojtD4CMOnnz_3CoeXUmVw7tEso4_kAZiZhqbK5zl4XPsBL6TXceFrJeczLsfSDqEnOLDt2PTBHX76SGp6JlPahT0D0O3u7sybMKQ-_HUzKGdEA6WzuUg-XpFIPf4BVs4KV7AB8wuFmvvaBEA3DNJSNaHLmYbn0mnO2bjGKDNO068j07Ww943AclejNO5OgLC5iRzBMRaJE6i7MaaSNxdb2yk5AyQdtt690Eg-ZnBn-ryYK31WZ8wizzhQtqvZzNlg6fdibQhMN8shzP6z2Ay3KmfE7ybb6tfzlTDuAl8qy_PJhNJ7Uswlj3_xc_kzjzfRbk0zMJa-BgbKCSRE16_pRzKMFo4Zas8iRJFiOKkZuVTP073MSIVjuCTbbC724" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میلیاردها دلار سلاح غربی، بی‌اثر در برابر مقاومت یمنی‌ها!
🔹
مرندی، استاد دانشگاه:  ایالات متحده است که از یک حکومت نژادپرست و آپارتایدی در فلسطین حمایت می‌کند. خود ترامپ می‌گوید: «غنائم به فاتح تعلق دارد» یعنی مردم ونزوئلا باید همه‌چیزشان را به ترامپ واگذار کنند، چون او پیروز شده است؟
🔹
آیا فکر می‌کنید مردم ایران اجازه می‌دهند او کشورشان را شکست دهد و غنائم آن را تصاحب کند؟ چنین اتفاقی نخواهد افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/468097" target="_blank">📅 09:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVu5IGOXejezWoWOGivPVTRWGAhdpdNap-rw_CI5OlKRt9MU93dyxMTir_BTQk0mkVOf9Hb737B-mUNeidDoEhgdCoavfWhxMwljk2cEqC-CMexkQ2e4E98HLq6xWZSBjn7L8_QMZaNrjd15t6DOHdFz5CKgRvQQR4z4wQCgfl4CLHDHKu8zBjiQuLo6cYQYGlJK2ycmftvGhUT3mnCdSvQQuC5X9Hl3mOiiHeyd0M7zaD9yTTSKW6Z0luG7hF8rYOMRX29OIKGkBTxfzwN8b4beEB_ytY5vCkk26V3V6fSXooozxOzOGc_OOkjNmDZSLGuzersaECWbVUuQbb6bUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۸.۵ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش بیش از ۲ درصدی به ۸ میلیون و ۵۱۳ هزار واحد رسید و رکورد تاریخی تازه‌ای را ثبت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/468096" target="_blank">📅 09:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468095">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab0427240.mp4?token=fC4KVJxr6M8B4idKI-kzujjkGoDJHJmFSCjAlhN9e4TyD_AenuKAe3Qvc7YBmQV3DCOwDj1EHNyKvoPA-NQlgx4Du5fkQs52IOwHs2Y8Wkzmy6zl48tEi02bv34UY6WhcOj77739wsc_1WArH0iVviKX7aSn7vTLQJAYaSIdsXkGdwsFCvX1DGjyBiUY4D0V5tPHQuCpk8ZZTRxRdQlLTrpdiJtrwfj9C7HmSLj9WOCyl-REQSlKWlQBKalRGx0QvafJPZzaTa0wh5nJmUAqDMeY9ilOxEbiWTEcDimq-YyyJNJiEVlkYlat-65TwCd154PJODRzHma8GFq20HMcOoeZ4M_5WRT550Qewtvow4vjTGJ0avCxjsfVugtXSu249LGy-EaoJNVpHIZp1IOwlpoTvCVVNcsPVJ_UcpaBcNg78HZGbV3IH7aZrNUoUsxx25-kIRu5VowxSSuKq6hpjL5bn1wKMRlbCcM1XDf81X-g983piK-pVRfrBhHloMhPBOKq_VTiEoDHB3wZtKNYffcAgkUmsLOBJMHeSW2FSdMrkbk6JZsJ-R1F_Ev1Svai78meHcgzyokYLg6bD-2zmag47vNvts808O5fg5Nt3iujYd3p_yIt1OjguYPF7bM7kZYgZUGxkVrSwXhZGXJOZKrvVIRgRveI-g1rKFPftGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab0427240.mp4?token=fC4KVJxr6M8B4idKI-kzujjkGoDJHJmFSCjAlhN9e4TyD_AenuKAe3Qvc7YBmQV3DCOwDj1EHNyKvoPA-NQlgx4Du5fkQs52IOwHs2Y8Wkzmy6zl48tEi02bv34UY6WhcOj77739wsc_1WArH0iVviKX7aSn7vTLQJAYaSIdsXkGdwsFCvX1DGjyBiUY4D0V5tPHQuCpk8ZZTRxRdQlLTrpdiJtrwfj9C7HmSLj9WOCyl-REQSlKWlQBKalRGx0QvafJPZzaTa0wh5nJmUAqDMeY9ilOxEbiWTEcDimq-YyyJNJiEVlkYlat-65TwCd154PJODRzHma8GFq20HMcOoeZ4M_5WRT550Qewtvow4vjTGJ0avCxjsfVugtXSu249LGy-EaoJNVpHIZp1IOwlpoTvCVVNcsPVJ_UcpaBcNg78HZGbV3IH7aZrNUoUsxx25-kIRu5VowxSSuKq6hpjL5bn1wKMRlbCcM1XDf81X-g983piK-pVRfrBhHloMhPBOKq_VTiEoDHB3wZtKNYffcAgkUmsLOBJMHeSW2FSdMrkbk6JZsJ-R1F_Ev1Svai78meHcgzyokYLg6bD-2zmag47vNvts808O5fg5Nt3iujYd3p_yIt1OjguYPF7bM7kZYgZUGxkVrSwXhZGXJOZKrvVIRgRveI-g1rKFPftGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دست کش‌ «ننه‌عصمت» در دستان کوچکترین سرباز حزب‌الله/ این دست‌کش‌‌ها به دست محمد فرزند شهید حمید اسداللهی رسید. fna.ir/TO6EH4 @Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/468095" target="_blank">📅 09:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468094">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO_x2hbjdaeTczVCGxJJShzV-QnBNDfBbzggQZJsJ0raW0FsU5U_cBQfDbHkeowNe_YXsQ7M5tBij1KpwI1aS_Rb9ek-SrRLuwCwV224cLwgWggLdwFrBml8gPG57mX7aPZ0E7ukJ_VtPMhaLinS54SDGVPhNuZL3QLcLIzymqfQl5aYzySXVAy_2DvGFiAqc_Dv6y9ql4_w-iVwbKPsmYQjn6V6rFnySMyKcIXAmiNxi1tUC8LaXsfDvyGrbISL6ILkkWjDfC_03PNGLYWw_JORP1bOIR1XvJZ3mHDQEzZJe4nTiaeSPmqnXwo9U5SmGgnKDuMk32Y6D3vEXEUcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم قصاص قاتل شهید جاسم حسینیان صادر شد
🔹
رئیس دادگستری هرمزگان: پس از گذشت حدود یک‌سال از وقوع حادثه قتل شهید ستوان‌سوم جاسم حسینیان مأمور پلیس راه شهرستان میناب، حکم عامل این جنایت در دادگاه کیفری صادر شد.
🔹
اتهام وارده به محکوم علیه، مباشرت در قتل عمدی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/468094" target="_blank">📅 08:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqxtst8zJiCd3VeZk1GTLP7Sx3CD5x52UQeIgtqHHJqAUT12LELdg1XEH-UDF65t_FbTvhG4h-w1QBtlNi_lgrzsYsf2K1mICXRqfaP2znY5QR6TdD8C2-19rbzBJotwSMpiZ-FHzaChnplbCufpkz1-KF1qd3c7qVl_kdBydaQn2Q6sjrTkasbrQwO2T-4sxtUn1r_PN3U1JinSazOyzowniPhlQ3OWpYVOlRTq9nU0OB0HeFM-kfrPqKFySHFXCXCGWOz5fh4aEVfbBZZ0FIzc8DCtgvSydKXZEqeLihg2cWA1fqCTq5WWY5Um2V4gUOmbbPnhazuL5HNUFTBghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی رشد ۳.۶ درصدی صندوق بین‌المللی پول برای اقتصاد ایران
🔹
جدیدترین گزارش «چشم‌انداز اقتصادی جهان» صندوق بین‌المللی پول، رشد اقتصادی ایران در سال ۲۰۲۷ را ۳.۶ درصد برآورد کرده است.
🔹
این درحالی‌ست که این نهاد بین‌المللی رشد اقتصادی ایران در سال ۲۰۲۶ را کمتر از سه‌ماه به پایان آن، منفی ۷.۶ اعلام کرده است.
🔸
این ارقام یعنی رشد اقتصادی کشور که در سال گذشته دوبار هدف حملهٔ ائتلاف آمریکایی اسرائیلی قرار گرفته و این جنگ تاکنون هم به‌صورت حملات پراکنده و هم به‌صورت محاصرهٔ اقتصادی ادامه دارد، تا چندماه دیگر ۱۱.۲ واحد درصد افزایش می‌یابد و از رکود خارج می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/468093" target="_blank">📅 07:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468092">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul0dsCBNmDcvkSMmqT_p9aaj3CG1TTr8wIZVjugkrP19nIA3ugDuCxOgE667EoiSpTD3PxHx1jInnoEvNaU3bnEi9BtRyI72-MmA0CEGbWhVqrqBjPBLaejYf-0et8fbpdJC7_2rORLA4RuZd9c4VofiYXuszXgz6n9Ssu-2qUzXVjfiiwCtdjbsGAGpWgIxtXfyKrMwsf6b_zMl1gg0MI4jeSOWWZoigzfypPWOp--LTrgXKj6hOMHfTBM7FIpcObM7_fp2zCouh-T7vUFNwdTu20Ncm8R9Tl7vFTniN2LDExLFLbkP3EA7CU7HjI7a5KwVe8ABRFEqoDoA-gM24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات ۵ میلیون تن فرآوردهٔ نفتی از بندر شهید رجایی
🔹
مدیرکل بنادر و دریانوردی هرمزگان: با وجود جنگ ظالمانه و تشدید محدودیت‌های اقتصادی در شش‌ماههٔ ابتدایی سال جاری، صادرات ۵ میلیون و ۱۴۰ هزار تن فرآوردهٔ نفتی از این بندر انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/468092" target="_blank">📅 07:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468081">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2L-n7RJuaQXpK5Pis8Mm1wZlHaeT2jCisqYoIP1ng2pAdrMGw1HB56mpIiNjMWoEsxknlsh9IMxKg_2qbVaJs9ZFylIHPfmqlnQ8qenTTmFsR1WfZa-QRTMC3KCm74tKy5I9IqCkbmwkCUik1YVAQmzTC14J4ojbdwJ2p_L2ti_iEDZIV6KRKcuuebZL30Sraty_qGmSQexTD4KR_-sWzsDf0p3dItTXUbugnRTZPwK3UH7TDgGKoa5tC8Zyi6_E6EKgS4T54fa9eF6U5LauV-3TsWK4vajTlN_DYri5x_ikDLkWQh2WTvWA1sAm5MEbJF-PgvFmTg0UOfaJwcfrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
انهدام پهپاد ارتش سعودی بر فراز یمن
🔹
ارتش یمن یک فروند پهپاد رژیم سعودی را بر فراز منطقه «بنی مطر» در جنوب غربی صنعاء سرنگون کرد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/468081" target="_blank">📅 06:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468080">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TktOqvIXD7oBauY7RfR8lmJKpyN6cJueEpsNNAsfBO-qXcxsq8zNsVRPCWL8eHwjJhUSIh-o8T7HhqCHoBKrqSqLF1MMG1-MQCYAlR_pnQ1Z-ScdVZyN6VMhj-4OtDgGk-3Ik3DVLT1n48XiIsbaKoP1v6ZqxBya2ung4PlurAouPxmjLhLGN0s5Q0H7TE6LDbSReSuolY0c0PvGcGPVprTRfcnuwlm1ViXDyAeNLMCeaXJs7S0Yv3IYZcsN6-NdBTg6AsISM8oqcfox8wLmQ7CnXi5m0gW_3858LIkG6mwPw82ovF47m80AXQ0OUb5xOGx7wbGuY_c4ugouq89UdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمایی قطر از تعلیق تمامی پروازهای خود از مبدأ و به مقصد فرودگاه‌های ریاض و دمام عربستان خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/468080" target="_blank">📅 06:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468079">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPjj7_pdO7NUlMQRTReN2xHGQ-cqJO91VsjMfc6pkvr-YqapnVf8yqHGIRJV6saqdGfaSGGvah0vKfqcB2nQxQU8wdmy7-I3VcyFeWoZoZH12xlxIAYx-gqGMdBy7R1mt8GWCmhPKCYxVCSnpFuTcQ0TiEgBdbmbfyRVMp6spEERhOCrIh5ZVPtEe5M0HeC8VQF9kkzWxFV32XJ6ijIPue0UDqf7rwJAV_JgEuXw0AaRH37mRV-QFYfv1LSGJGkA4sQcrgTItBHhednPACes3d_c4MjEHOBUvvmliujUevkB8TUPsjJ1n1J6qOiFe0ki2Beghzzidp13eqgUM60wDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل مهمدی نخستین فینالیست کشتی فرنگی ایران شد
🔹
مهمدی در مرحلهٔ نیمه‌نهایی وزن ۸۲ کیلوگرم رقابت‌های امیدهای جهان، با نتیجهٔ ۵ بر صفر حریف روسی را شکست داد و به‌عنوان نخستین نمایندهٔ تیم ملی کشتی فرنگی ایران راهی دیدار فینال شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/468079" target="_blank">📅 06:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468078">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjNqNZz7BatabPDe-kLqCsdnwH5BFj1PDEwxz3TKn-Ca_JRvozWTRyZWVej8bAlv0G_JOYTtX_6THoTGXKyjZhWw-WB4pPOfNm532kcCaxvN2gsSYpy4JNBs9uXWBiBuNsUJx-yRE24r43dOO-VH6K_EDRHfK2FjArVQCMlshr7ChcJ2xbNGWoWJ0O14O-EgDXxZWwCjx2njxVAW_vfAYRoqg0nslXpf4uTNIlO9pxomiUPD01-mcEc8YlOmNtk4IU-3CVxNk1d2neFaJ96F0yrEKUEgPNdjHLkNDRpaBmhAMGEGdl_lCxptnSuRH_x5vhpyBiWVvrEn2kJ7i--ZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مین‌های دریایی چگونه کار می‌کنند؟
🔹
مین‌های دریایی بسته به عمق منطقهٔ عملیاتی در سه ساختار مهارشده، کف‌خواب و جهنده مستقر می‌شوند. در نمونه‌های نوین، به‌جای انفجار تماسیِ ساده، فیوزهای اثری و غیرتماسی به‌کار می‌روند؛ جایی که حسگرها انحراف میدان مغناطیسی زمین و صدای پروانه‌های شناور را در کسری از ثانیه ثبت و محاسبه می‌کنند.
🔹
پردازنده‌های هوشمند مین شناورهای رزمی اصلی را از قایق‌های غیرنظامی یا طعمه‌های مین‌روبی تشخیص می‌دهند؛ سامانه‌ای مجهز به شمارشگر عبور که هدف‌قراردادن ناو اصلی در میانهٔ ستون را ممکن می‌سازد.
🔹
مکانیسم تخریب مین با ایجاد پدیدهٔ فیزیکی اثر حباب انفجاری رخ می‌دهد؛ انبساط و انقباض شدید حباب گاز در زیر آب، تکیه‌گاه میانی کشتی را خالی کرده و با پدیدهٔ شکست تیر اصلی کف، سازهٔ چند هزار تنی شناور را از وسط نصف می‌کند.
🖼
جزئیات نحوهٔ کارکرد مین‌های دریایی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/468078" target="_blank">📅 05:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468077">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0951251d29.mp4?token=cWmewJLH7BBZBHwCIPTbtYsRc_OIsAoJoroCUWoR0gQ0oByXokr1QT8wtW1ivih2-iv1wPh0ntIMP0ld6gQRmCMVzZUQ3-LPdcH3S7haIs1gR3ZcS0J33EZVnPVFDjh68P9sYnPg-Gr7iph_D69hjMFortqNfV2EUFENN5JckptlrPA37hyuJ40UFvZiEIJj5WWgIduDjoNZzt70VUPtKChJeMJ7oso_jnEMxvnql7nfEe1n-XWdWr_1qr_Hfr70Pf9iErcL-o3YGn_hV6Nx2my_ADJTavhvsEEOvAyiY4lPOc74DlE3SYuSKWQaTYmAd9N7jkiKTxWgEdF3hKkBJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0951251d29.mp4?token=cWmewJLH7BBZBHwCIPTbtYsRc_OIsAoJoroCUWoR0gQ0oByXokr1QT8wtW1ivih2-iv1wPh0ntIMP0ld6gQRmCMVzZUQ3-LPdcH3S7haIs1gR3ZcS0J33EZVnPVFDjh68P9sYnPg-Gr7iph_D69hjMFortqNfV2EUFENN5JckptlrPA37hyuJ40UFvZiEIJj5WWgIduDjoNZzt70VUPtKChJeMJ7oso_jnEMxvnql7nfEe1n-XWdWr_1qr_Hfr70Pf9iErcL-o3YGn_hV6Nx2my_ADJTavhvsEEOvAyiY4lPOc74DlE3SYuSKWQaTYmAd9N7jkiKTxWgEdF3hKkBJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام پهپاد ارتش سعودی بر فراز یمن
🔹
ارتش یمن یک فروند پهپاد رژیم سعودی را بر فراز منطقه «بنی مطر» در جنوب غربی صنعاء سرنگون کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/468077" target="_blank">📅 05:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468076">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM0VQqxtRsThvmzXnELgM23IAIL8N4iaXYSDbOpbr9SXVWwWEcREgfEFF4Qk2CqErkegz0juk2V47O2peIlbr8vCaElDOr5iIQsuKM6hIB8lLpqUAa0PR3MTJ3QW5KzOJQkBXFIZdNBqEKmgvSZlgj6GJ-XF5rwTQnEDT4Bx-T99QX8Ks-XPvNFK_5SDr_IgmH8mstO3gdApegUJiL0JcrTsuesgVXErDXdjcmFkzvh_S6BzQ4wsBjHIX-Rw3YeOeLRuksT0hqBy_22Ndqw0XyngJyJCx63nB0Lzpsvhi3o9AxvKUZlxENMNFROdzRISs_6oYNYRn4JZPtRSIsEVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط‌ونشان فیلیپین برای شبکه‌های اجتماعی
🔹
مجلس نمایندگان فیلیپین طرح ممنوعیت دسترسی کودکان زیر ۱۳ سال به شبکه‌های اجتماعی را تصویب کرد. این طرح برای تبدیل‌شدن به قانون باید با نسخهٔ مصوب مجلس سنا هماهنگ شود و به تأیید رئیس‌جمهور برسد.
🔹
نسخهٔ مصوب سنا سخت‌گیرانه‌تر است و ایجاد حساب‌کاربری در شبکه‌های اجتماعی را برای افراد زیر ۱۸ سال ممنوع می‌کند.
🔹
افزایش نگرانی‌ها دربارهٔ امنیت کودکان در فضای آنلاین و حوادث خشونت‌آمیز در مدارس، از عوامل تشدید این بحث در فیلیپین بوده است.
🔹
فیلیپین تنها کشوری نیست که به‌دنبال محدودکردن دسترسی افراد کم‌سن به شبکه‌های اجتماعی است. این محدودیت به موجی جهانی تبدیل شده که شروع‌کنندهٔ آن را می‌توان استرالیا دانست. پس از آن، کشورهایی مانند فرانسه، اندونزی و مالزی نیز محدودیت‌های مشابهی را در دستورکار قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/468076" target="_blank">📅 04:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468075">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">🎥
با گفتن اذکار دنبال دیدن نشانه نباش!
🎙
آیت‌الله فاطمی‌نیا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/468075" target="_blank">📅 03:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468074">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFp8XJfHJAXq28VsYYekZakOwrZQ4mtBtrqWwdzlx4VKy6fS1_iQ8ZhcZqR3_YgQsrWsx4FU5P7tiu7F8S-txdxl2Hholp-4prkkMmdy4FYxkMHyWdZJQR9gRlOx4wlCFqIeLWbxjEaGR-MQJgpAiwjZAU0V3GdjzzKMJlWWx_4CemGxy1mnehNyJ7nolht7FggQ8FQlYvdJAt1_5TwfRJIt44bs56AtAx4wI6xnWbhruJS5VPwkReqaM6RWSfXXvCtTipsIPPGwUkp-zS0medBNnoRZRIEXWIPoZ8IAwHslzgIcHduM4TyOg52yySzAdEG12ugayHwhkRrq4W6dEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرهٔ‌شمالی: موشک بالستیک تاکتیکی آزمایش کردیم
🔹
رسانه‌های کرهٔ‌شمالی اعلام کردند که این کشور یک فروند موشک بالستیک تاکتیکی را برای تأیید موفقیت در ارتقاء فنی یک عنصر مهم و اصلی، به‌صورت آزمایشی پرتاب کرده است.
🔹
در این بیانیه تاکید شده ارتقاء فنی این موشک، یک موفقیت بزرگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/468074" target="_blank">📅 03:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468073">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S212u9Q53NXUjoB9rHw03vwwctRUw8UI3tA9qKL0PFmsPXRVXe5ZoY9cWiEfzDYA6QRHMpZnTloAQrCY0dd68xmRSizJPV6CNcKsOrj2Ig1O5NDpl9Rq7Z1FLh8BuF6w7lU9uj7YQLJ3Ux33th954rNhLTMKQD30rsOx2J354xqQTNGo8o4DoX2eOOiz7jlnaTIrDt9JtVffPQjbGHDjsLcU49t_ktyeG8HrFtOCV9rdKvKakBticXeYVSnyEu1bOMsC3UB9Yc4DLqfre8dIg9FTYH02yBtpW8TBfcq9ZHTxgcxIrRj8vcsoECkw3hl5PujQH4uXV7NWaeb5H6iIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمایی قطر از تعلیق تمامی پروازهای خود از مبدأ و به مقصد فرودگاه‌های ریاض و دمام عربستان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/468073" target="_blank">📅 02:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468072">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwlFpm0dk5LlqWsYcx6F4DMZXduDC1_UCawLO81c2ct3-ymMnCfPjatt9p64Dz0q-JEaCrfjKpuf_4XVfJbDs1d5DITTpKYoz3jkwtfatbx-Kl7C4eXnZ0Q0R4-8B0CiWDN6EVyxA6vBnIeOztIfm6VPzMi8M6Dy1bvHqC_jWI6OJJxXnpi0yhZmdCpzdBBobyglZ1FWCnR7rG6KCqmxt10AtNdXp9zHjtzNNI_VTCJdNVDrdEmf9Dft869T9uukDW6BFSkwtOY7KMILq0m4eH7fx2_mMURZem8UyzKhWfFk9yko3k1OlqvWh1BhZAnpQpB9pN5SqDVrmzeW05VQHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: بعداً برای بازگشت به مذاکره با اوکراین تصمیم می‌گیریم
🔹
معاون وزیر امور خارجهٔ روسیه گفت مسکو همواره از مذاکره برای حل سیاسی و دیپلماتیک بحران اوکراین استقبال کرده و می‌کند.
🔹
وی با بیان اینکه اقدامات کی‌یف در جریان انتخابات پارلمان روسیه احتمال از سرگیری مذاکرات در این مرحله را ازبین برد، اما موضع روسیه تغییر نکرده و مسکو با درنظرگرفتن چگونگی تحولات اوضاع، در آینده دربارۀ بازگشت به گفت‌وگو بر سر اوکراین تصمیم خواهد گرفت.
🔹
به گزارش اسپوتنیک، شش عضو کمیسیون انتخابات روسیه در جریان انتخابات پارلمان، به‌دلیل حملات هوایی اوکراین کشته شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468072" target="_blank">📅 02:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468071">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حملات رژیم سعودی به مناطق مختلف یمن
🔹
رسانه‌های یمنی گزارش دادند که رژیم سعودی در حال هدف‌قراردادن استان‌های صنعا، عمران، الحدیده و الجوف است.
🔹
وزارت بهداشت یمن نیز اعلام کرد که تجاوزات رژیم سعودی و مزدوران آن از تاریخ ۳ سپتامبر تاکنون، ۳۸۵ شهید و زخمی برجای گذاشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468071" target="_blank">📅 02:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468070">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تلاش ناتو برای آرام‌کردن روسیه پیش از رزمایش اتمی در ایتالیا
🔹
پالتیکو: ناتو به دنبال اطمینان دادن به روسیه است مبنی بر اینکه رزمایش‌های نیروهای هسته‌ای در ایتالیا هیچ تهدیدی برای این کشور ایجاد نمی‌کند.
🔹
مدیر سیاست هسته‌ای ناتو ادعا می‌کند که هیچ دلیلی برای…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/468070" target="_blank">📅 01:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468069">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/468069" target="_blank">📅 01:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468068">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P14Q6jTLnJ3vD3lQk59vx2V4Q42TjDVLI0jq45gCKKM-XrRtIZ7mCgpxGqYQBUeyDU1Cd3WPInIKPbqz7qZTvdleZLcXSafG1vdTRNWmwT9wUht0O_L3A_TrbsJikddo8UN2c2uWGiU4lQJ-IrbcjhLT1W24DgdHvsD6mDiSixQkIgS-at0k9eHXYjrjIBSjm5YZI7SMIDrYP6hBVmlIwGG2dLAcS80ZUUIUh06ZGLquiWikCHZm1mAqLFspQmi-jGnobQ4526gLXEFmEwqnRJbB2xaBFzL-Vo8JmF_m8dwZKLNJ5q5gRN6RTh7MNUAwZmU4asMSix7yf973uwOydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ هکرها به یخچال ۱۵۰ فروشگاه فرانسوی
🔹
حملهٔ سایبری به سامانه‌های سرمایشی فروشگاه‌های زنجیره‌ای فرانسه، باعث افزایش دمای یخچال‌ها و فریزرها تا ۵۰ درجهٔ سانتی‌گراد، نابودی موادغذایی و وقوع آتش‌سوزی در برخی شعب شد.
🔹
حدود ۱۵۰ فروشگاه اینترمارشه هدف قرار گرفتند و موادغذایی آسیب‌دیده برای جلوگیری از خطرات بهداشتی دور ریخته شدند. کارفور نیز از آسیب‌دیدن ۸۰ فروشگاه خود خبر داد.
🔹
رویترز گزارش داده که مقام‌های فرانسوی یک آسیب‌پذیری در نرم‌افزار شرکت دانمارکی دانفوس شناسایی کرده‌اند. ارتباط این آسیب‌پذیری با تمام ابعاد حمله همچنان در دست بررسی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/468068" target="_blank">📅 01:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468067">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مجاهد خطاب به آشنا: خالقان «دههٔ عبرت» نمی‌توانند داور تاریخ باشند
🔹
مهدی مجاهد، معاون دفتر شهید رئیسی در روایتی از مذاکرات سال ۱۳۹۴ گفته بود ایستادگی سپاه پاسداران و دستگاه قضایی در پروندهٔ جیسون رضاییان، زمینهٔ طرح مطالبات ایران در مذاکرات تبادل را فراهم کرد.
🔹
به گفتهٔ وی، این مطالبات شامل آزادی شماری از ایرانیان تحت تعقیب آمریکا، رفع محدودیت‌های برخی دیگر و بازپس‌گیری مجموعاً ۱.۷ میلیارد دلار از اموال ایران بود.
🔹
مجاهد همچنین گفته بود که پس از موافقت رهبر شهید انقلاب با پیشنهاد مطرح‌شده، بر دریافت کامل مبلغ مورد مطالبهٔ ایران تأکید شد.
🔹
در واکنش به انتشار این روایت، حسام‌الدین آشنا، مشاور حسن روحانی در دولت‌های یازدهم و دوازدهم، در توییتی نوشت که این روایت تنها حدود «۱۰۵ درجه انحراف از شمال» دارد.
🔹
مجاهد نیز در پاسخ به این اظهارنظر نوشت: «قطب‌نمایی که کشور را به بیراهه برد و دههٔ عبرت را خلق کرد، نمی‌تواند داور تاریخ باشد.
🔹
انحراف، در عملکرد آن روزها بود نه در روایت امروز که بخواهد در مقابل طعنه، سر خم کند. ای کاش قطب‌نمایتان را عوض کنید.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/468067" target="_blank">📅 01:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468066">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ec01f669.mp4?token=YN8HngA7tpjRj0ka0jnvxr8A9i4LG3vL70ngTtclk6X8gSdOQLLfJ4uNNcd-yBS6DCF34z5XYKScYvKG2B3xPeKK7iztNXVBm5xSkTRL6QLKSUs8SDFA55-BcFyL6cXxMmbKIGmlUpng5l-Izl_pPfwKKBdvOj0IIqAHo660ZYpZ0HffzGSEpMmegQJXE0oq5cuLhgC7P3H9Km-QZ1M2c_ndOa5M36hFqu-nfo8aWwdyb4ZqyXuTfc_o6O8KW84lp2YroWA3DjgPA-Eij73paaLQMVavOKcPZ0qEFkZthdJXIYuPUSpRPbMurTmuobmJ7VO8LVDaQxDKmuMBFZYVKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ec01f669.mp4?token=YN8HngA7tpjRj0ka0jnvxr8A9i4LG3vL70ngTtclk6X8gSdOQLLfJ4uNNcd-yBS6DCF34z5XYKScYvKG2B3xPeKK7iztNXVBm5xSkTRL6QLKSUs8SDFA55-BcFyL6cXxMmbKIGmlUpng5l-Izl_pPfwKKBdvOj0IIqAHo660ZYpZ0HffzGSEpMmegQJXE0oq5cuLhgC7P3H9Km-QZ1M2c_ndOa5M36hFqu-nfo8aWwdyb4ZqyXuTfc_o6O8KW84lp2YroWA3DjgPA-Eij73paaLQMVavOKcPZ0qEFkZthdJXIYuPUSpRPbMurTmuobmJ7VO8LVDaQxDKmuMBFZYVKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: رابطه‌ام با کیم‌جونگ‌اون خوب است چون ۱۱۲ بمب اتم دارد
🔹
رئیس‌جمهور تروریست آمریکا: من ارتباط بسیار خوبی با کیم‌جونگ‌اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای دارد، خوب است که روابط خوبی با آن داشته باشی. اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/468066" target="_blank">📅 01:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468065">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBl_909zmMAjarnJd__Z3QYncmsDNOe4G_02O4QFc5D3zYrtnJdi0ArShP2kiEZ-pyVSfDlc7Xle0syvF3zTeBuyjAM3HvukqDCSckjVOAaCAeozYDT_YyyfGObXUYDGNsKIN3utbqijhz-FB7LReXPq_6ag6PkoegNzaW2I5Ubar9K8jrnluedlGK0Ejntbd9rA_5v0TqUoDrQ2rsKpCb0JUoVTAjZeVh8hfiuhfC3smVu9WNut4m1iTP-3C0QUkXDqL5X7Sf8W0dhzBvJIVv0erkm636VV3V1hzp_BWRFiR0wN2EeZyXBqQp0sKQVQJMFjmyGP08Lem2xfpWonYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرماندهٔ کل سپاه: هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگهٔ هرمز و خلیج‌فارس را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/468065" target="_blank">📅 00:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468064">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آمریکا دربارهٔ سفر هوایی به عربستان سعودی هشدار داد
🔹
ادارهٔ هوانوردی فدرال آمریکا و وزارت خارجهٔ این کشور با صدور هشدارهایی از شرکت‌های هواپیمایی و شهروندان آمریکایی خواستند هنگام سفر به عربستان و استفاده از فرودگاه‌های این کشور بسیار احتیاط کنند.
🔹
براساس…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/468064" target="_blank">📅 00:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e1e3a7b6.mp4?token=q3Rf5aWp-_s30Wf7X6Jxd_rhXJjXcBlQBxYVt9YKYIvly88V82gAssqtlkEc4OyfyyPJglc3DwmPP4s5hNmvZfb4xVWIP6hzX589ErVYduOVioL5oMQxmaLgXinmECx6exOt9HRgRIXmhuqV9A269ptXYrUzSng8akboWv1kVWD8xF-YJ0KBdrraXfqGUpKzagVJvkiU7NhEkrOWu5JJ74HcFTR11F4Ub0k6yNR9CxlNMcK4ixyUGM_1zExQAZGTktj00XQ2KG-8GhUOlYa1TUYC4GvG6HyJyI0yrJqib2CTBS9QkfufsSlNknm_D53U9-yOpr7Ymvt0_UpiZeE2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e1e3a7b6.mp4?token=q3Rf5aWp-_s30Wf7X6Jxd_rhXJjXcBlQBxYVt9YKYIvly88V82gAssqtlkEc4OyfyyPJglc3DwmPP4s5hNmvZfb4xVWIP6hzX589ErVYduOVioL5oMQxmaLgXinmECx6exOt9HRgRIXmhuqV9A269ptXYrUzSng8akboWv1kVWD8xF-YJ0KBdrraXfqGUpKzagVJvkiU7NhEkrOWu5JJ74HcFTR11F4Ub0k6yNR9CxlNMcK4ixyUGM_1zExQAZGTktj00XQ2KG-8GhUOlYa1TUYC4GvG6HyJyI0yrJqib2CTBS9QkfufsSlNknm_D53U9-yOpr7Ymvt0_UpiZeE2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الغرافه دومین قطری قربانی استقلال در آسیا
⚽️
الغرافه ۱ - ۲ استقلال @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/468063" target="_blank">📅 00:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468062">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
توقف فعالیت فرودگاه‌های ریاض و دمام عربستان
🔹
منابع عربی از شنیده‌شدن صدای انفجار در حومهٔ ریاض، دمام و خمیس مشیط عربستان سعودی خبر می‌دهند.
🔹
گفته می‌شود فعالیت فرودگاه‌های ریاض و دمام در پی حملات ارتش یمن متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468062" target="_blank">📅 00:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468061">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQhxIZylIdKU8g4N37GdPFwprEbJ0x5p8IreXKEF_BPuslQqvwb5W-w2_EbfGP_aao4LaeHR4hHow_dZckMTKu_-QKg916SMuO_AoU8tuvzj4SBtyh8EvHFjwt2jx3aQbbW_qP8Ai9JgDMwuFt-iOfQwqwOMVlbtwA2TZuH9D_ZR6UiAQKMd5PuGRrxTfg_WgFtVCTfI1eImE3-NPTKWpkiknfkeV2eJltDP9KjIkqkZVIFUtdDwv6RzeK5KJfOC3niaoYCBl25oGDc-1cdxFzr3uLtwees8e1qf5WhN42bDWSnnhU1wBnEX3ABRcWGabJO6y8Sf3t0bn6Y3Z_TJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت‌اندیشی نابجا
🔹
روزی شکارچی برای صید بیرون رفت و آهویی شکار کرد. لاشهٔ آهو را برداشت و راهی خانه شد. در میان راه به گراز برخورد که به او حمله کرد.
🔹
شکارچی تیری رها کرد و بر گیجگاه گراز نشاند؛ اما هنگام زدن تیر دوم، گراز در همان دم با زخمی مهلک شکارچی را از پا درآورد و هردو درجا جان سپردند.
🔹
گرگی گرسنه به آن دشت رسید و با دیدن اجساد شکارچی، آهو و گراز، غرق در شادی شد و با خود گفت: «روزیِ فراوانی نصیبم شده است، اما شرط عقل آن است که به آینده بیندیشم و زیاده‌خواهی نکنم؛ گوشت‌های تازه را پنهان و ذخیره می‌کنم تا روزگار درازی بی‌دغدغه باشم و امروز را تنها به جویدن چرم و زهِ کمان قناعت می‌ورزم.»
🔹
همین که گرگ دندان بر زهِ کشیدهٔ کمان گذاشت و آن را جوید، در این هنگام گوشهٔ خمیده و فشردهٔ چوبِ کمان با شدت پرت شد، بر گلو و گردن گرگ کوبیده شد و او را در دم هلاک کرد؛ طوری که هر ۴ موجود در یک‌جا قربانی مرگ شدند.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/468061" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468060">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZjdWvrvKdkEA4EhgmRbZQQML2Lznllg5n_tv1UNwjfXTWrjVB3Fmg90h20Qdm22HVngwkEXs_O_cXeaLJCvYiuin0E3KApB_Mb55KhETMBPCy9jtnEX_mIULTaKooXkHmJgrs7qEOr7F7guSKe_jRUfkmGxqkW3938dema0y9y7tlW3_gvkw7jlNm97ZSGA39ucsB1vW2-0UgS3zHd-K-Dd7t5YkgVdShib4d5Nu-4_7bFUPaqZXZhH_UUbaLJz2MFWw9MrpRxirAF5eB32chRTixeuy063s4ERVXcCOiADx-LYjxJvOR-gyKJvaSS5fac0qy-AQJN2NSWh6AKV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/468060" target="_blank">📅 00:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468059">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPo8vLWzDrKmghYLRQZz45X2l0PUDEvJBCLwAeTp-2wPxFNSR4o_E7UxrdosHsWzdm7dsFg6z8GMAUfIJruP9HJirbau4ku54Ctp2g8w02yHOCOp-KO_ffEgpHc9teQ1a5n7wRFTYYDQVjZQaTdXP90QHGrwZPdddNMtGooGr76HdVXdTyoMixDYTZkYHfQiAniqT04YP2lS2Xr2EEratNs58_SQdl5bEW4vVKWKswSNZW3D4905eHB7tH4Dg4wVaSS2ClTMhzR9J3F4nPUZkmB8a9-_fKHcwlL41JPdinrLL02SU4N8_yGFVhW-Rw-Wn42UquK3LGL_qulLRcvmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه آزاد خواستار پاسخ‌گویی عاملان حمله به مدرسۀ میناب شد
🔹
بیانیهٔ استادان و مدیران دانشگاه آزاد اسلامی به مناسبت رونمایی از یادمان شهدای دبستان شجره طیبه میناب و یادمان ۶۴ شهید دانشگاه آزاد اسلامی واحد تهران مرکزی در نقشه ایران عزیز منتشر شد.
🔹
در این بیانیه آمده: ما استادان و مدیران دانشگاه آزاد اسلامی واحد تهران مرکزی، بار دیگر حمله به دبستان شجره طیبه میناب و هرگونه تعرض به مدارس، دانشگاه‌ها و مراکز علمی را قاطعانه محکوم می‌کنیم و معتقدیم، هدف‌ دادن محیط‌های آموزشی نه نشانه اقتدار، بلکه نشانه ضعف، استیصال و ناکامی آمریکا و رژیم صهیونیستی در دستیابی به اهدافشان است.
🔗
متن کامل بیانیه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468059" target="_blank">📅 23:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468058">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1bd45021.mp4?token=dYq4hBddyVnA6ShW-rL4gLLbolsFw7L-dHVh2sIWz_rVvVPRNStPXly030C9Jmj2qTJdV2SP1Q6gxkyzovRkflIPv6YS9UxkxtBEAC190L4-H60iHrSF8b9WFxCSeT-D0dK2UTk8VHckjPtlKR-49MyOVDYf_sGhkkF23Q8YM53PWHAJwzyXffDvgwQsPCL8Oo26k5MwSDX4-j5aE-il5OrVBi3mwqo4QFDRmPcHc44RE_ADaKXC-F5Y13r-6fTeE2sVUeZJr54RuHK_rMAWIqb6Uh5AnNGVimmSrYPY7qc82B-uPYEIYXV-SCEikGLolrE4apnHFkR7cE_S5JpE5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1bd45021.mp4?token=dYq4hBddyVnA6ShW-rL4gLLbolsFw7L-dHVh2sIWz_rVvVPRNStPXly030C9Jmj2qTJdV2SP1Q6gxkyzovRkflIPv6YS9UxkxtBEAC190L4-H60iHrSF8b9WFxCSeT-D0dK2UTk8VHckjPtlKR-49MyOVDYf_sGhkkF23Q8YM53PWHAJwzyXffDvgwQsPCL8Oo26k5MwSDX4-j5aE-il5OrVBi3mwqo4QFDRmPcHc44RE_ADaKXC-F5Y13r-6fTeE2sVUeZJr54RuHK_rMAWIqb6Uh5AnNGVimmSrYPY7qc82B-uPYEIYXV-SCEikGLolrE4apnHFkR7cE_S5JpE5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس اقلیم کردستان عراق: جمهوری اسلامی با حمایتی که از مردم در این جنگ دریافت کرد وارد مرحلۀ متفاوتی شده است  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/468058" target="_blank">📅 23:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468057">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeTncS1jpjWCerbPB5yeG7YgWtkMD_n8hLWpBMn-upLlcnvd0w_UeV7dTkJhdOegSAodqM0BCx7IdNNIgRNwZ3AMeeJS23wP0ZxvaDxyg05Is6VlneOsQEDiL1BW6iH0_B02nsfh2DaZ-FfrVIJP7COzQdLWqVKmkmloYgx0lHbKqykX3McfdstumETLhRVxtmGDNO-RbFYyNUs7bfEc_wD25gQJCqUDR_w3qQx412-HV-59Dd2llWSX_N6Lli9Kg8-IJdCGB4bRvkvLMzSDa37v1Vcez85lrMlvYWnlEvpLH_eYVDCnxYkwqfZjUyjy4vToG22Yymd14eZ4FzuuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
این‌بار آشورمارتوف پیروزی را برای آبی‌ها سیو کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/468057" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468056">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda9d0682b.mp4?token=ZjuKmYyYVvpApWTel_e_6w3Y8w5g2BL997wsPaCWXrU2iMa-7u8xVsXEGN1YVINdXiHzL9cfduCl6Bu94E3-944_9uOC4pi9rId6W2Q1gjSGQBaGHgRFq3WqDdQ8Nas97T4YBzhysAWlqdlmMD60htCnQHWUtRgm316oeSxPluQZHn9M9ZmpRBtilqBKD_bqg7Kbimq5EhwI9jzcNQI6njCWUTOkrKr1ikJ3n_Elt_yoKW5VSMfWwa1KAiLQuhPKaMVKbM76FlZ6yfpTvONlYdqRrQrpEGP7CyZilSi3JJqQSre89YWev-wyzLLiCze2rd9cm6F7uYpvgaloVJ1mYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda9d0682b.mp4?token=ZjuKmYyYVvpApWTel_e_6w3Y8w5g2BL997wsPaCWXrU2iMa-7u8xVsXEGN1YVINdXiHzL9cfduCl6Bu94E3-944_9uOC4pi9rId6W2Q1gjSGQBaGHgRFq3WqDdQ8Nas97T4YBzhysAWlqdlmMD60htCnQHWUtRgm316oeSxPluQZHn9M9ZmpRBtilqBKD_bqg7Kbimq5EhwI9jzcNQI6njCWUTOkrKr1ikJ3n_Elt_yoKW5VSMfWwa1KAiLQuhPKaMVKbM76FlZ6yfpTvONlYdqRrQrpEGP7CyZilSi3JJqQSre89YWev-wyzLLiCze2rd9cm6F7uYpvgaloVJ1mYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرعباسی دروازۀ استقلال را نجات داد  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/468056" target="_blank">📅 23:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468055">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2073a26d26.mp4?token=YHvMvE5qkYrEg--q1ruWzByZ8UGIzl5amQ9QBVHlg2avXEfiwVgIdLjDhoiSrjmFdIjy77NQfFn-e1ikttBGPGT8tQqzpiRc70qB-mhx85cp09BRv3fC8Wu6QxljwPZ34REo0W2cnPZI7km2jWuAbmPBtSBLKde2laKL6r7BwdmRO9C4DIw09GNex54Sn4hujo4sTFwOSNQDKEXHkMPlsWEfmrk-eFS1dQ-ACF-HVKXFfWFvXDSttfRX_rO-4e1jE7x7N-JLz6t2PBiaLXh0DrlFKqZ6XMQ5M-PSwY2nJ8-9tw3LJmAN5wL7iYHs-bHvVd0JkA2M0Z7AO5BKnDMeBA7MgLcxJ9PdZbsipWk1V4IrGItETyD5i5jzOKV3fcZLjbAoJtm0fWiWsrK4QStEGDzO6MTtcmtXSckZICWjUXvPyPLTcXdNaGhrz-xV2bfdmU4qY17AKXQNTYEkf_EGMmuPB6sG-Pya5ocNoIdHblHtmNFGrAPniNYha8qqNhPeCZOQN3-22x_hGVDK3pIhBATAe3ko2O-vCeF6wqB6mERVCGea5XUAgnqo6hR9as041y2EQjhcDZFVD4el-F31gD07nHrWR0t1UyUNCzIlyXAhH_9M1Pbzb1jwOhachblScHOHj1SMazWYG4RkChj4O6xrRCvstD_POhrkbW97OhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2073a26d26.mp4?token=YHvMvE5qkYrEg--q1ruWzByZ8UGIzl5amQ9QBVHlg2avXEfiwVgIdLjDhoiSrjmFdIjy77NQfFn-e1ikttBGPGT8tQqzpiRc70qB-mhx85cp09BRv3fC8Wu6QxljwPZ34REo0W2cnPZI7km2jWuAbmPBtSBLKde2laKL6r7BwdmRO9C4DIw09GNex54Sn4hujo4sTFwOSNQDKEXHkMPlsWEfmrk-eFS1dQ-ACF-HVKXFfWFvXDSttfRX_rO-4e1jE7x7N-JLz6t2PBiaLXh0DrlFKqZ6XMQ5M-PSwY2nJ8-9tw3LJmAN5wL7iYHs-bHvVd0JkA2M0Z7AO5BKnDMeBA7MgLcxJ9PdZbsipWk1V4IrGItETyD5i5jzOKV3fcZLjbAoJtm0fWiWsrK4QStEGDzO6MTtcmtXSckZICWjUXvPyPLTcXdNaGhrz-xV2bfdmU4qY17AKXQNTYEkf_EGMmuPB6sG-Pya5ocNoIdHblHtmNFGrAPniNYha8qqNhPeCZOQN3-22x_hGVDK3pIhBATAe3ko2O-vCeF6wqB6mERVCGea5XUAgnqo6hR9as041y2EQjhcDZFVD4el-F31gD07nHrWR0t1UyUNCzIlyXAhH_9M1Pbzb1jwOhachblScHOHj1SMazWYG4RkChj4O6xrRCvstD_POhrkbW97OhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از عارفی که در قنوت نماز شب، شعر حافظ میخواند
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/468055" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468054">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_UEP8oMgBDN3bLw4p2f4FNcf7eRWLZ3bsYbjSyY_PTNfFgPMkkWOaXTYZe0SEfRhDY9hP5r0Mxk40cSKzjPp-QMS7o6uPbNdaILAnSs9N_sUSsR6xAEMM94lJ1MoH_s3E5x_O52M0Fh3UUN8WE1oi-Uet7UN4LMUHM1LBKrH5Cp3o8uH5ZQ8yi5a4ICZ1z7Hv-mpyVDXFOfBwzxvNnL5m-Xaic8hO_2rlEy8-QCF_DAuYoZgR2r0BKDcOUVT5zT5F10VE_owDiWkGFKIRMQO806Bqr4Elaty1tzBduKNq3NB0E4DyQ9pUTZKvr3T3VRjEmMIbctfqoyu6cpTCR_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصرار وزیر صهیونیست بر جلوگیری از بازگشت آوارگان فلسطینی به کرانه باختری
🔹
وزیر دارایی رژیم صهیونیستی با درخواست از نتانیاهو برای جلوگیری از بازگشت آوارگان فلسطینی، بر ادامه محرومیت ساکنان اردوگاه‌های شمال کرانه باختری از بازگشت به خانه‌هایشان پافشاری کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/468054" target="_blank">📅 23:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468053">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797670d791.mp4?token=m6u2SQUw07Vvq6T0FphhuPk-nHuy_vl6sh4jwPvAKWrS7c1Ac6IAii1yEa5T1rkODK_XMPO66xDFcKUdyyGFkHuCA9bodUib-mbmZxOfhCWmNdswtJvjehqLdFdDH0axmmqplUR--RsaKqeamPhO3SDoPtfdn6dmKewgzTY02KMfBGRdQ6BFDLBwxX1osFy2o9dprvCbd9-BlXvApGIp224kTjdV5v-UNWaNhcdsncxCneS4cNTwB8l7kaVA7qHJ5M6B0Uf4hAkgM0xlZe2aHIOwiMOmMaa0uI2aWqtWFVj817rUQ4bSBUmLQaWs89qVuEeh-ljdTPRFu062UkWPSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797670d791.mp4?token=m6u2SQUw07Vvq6T0FphhuPk-nHuy_vl6sh4jwPvAKWrS7c1Ac6IAii1yEa5T1rkODK_XMPO66xDFcKUdyyGFkHuCA9bodUib-mbmZxOfhCWmNdswtJvjehqLdFdDH0axmmqplUR--RsaKqeamPhO3SDoPtfdn6dmKewgzTY02KMfBGRdQ6BFDLBwxX1osFy2o9dprvCbd9-BlXvApGIp224kTjdV5v-UNWaNhcdsncxCneS4cNTwB8l7kaVA7qHJ5M6B0Uf4hAkgM0xlZe2aHIOwiMOmMaa0uI2aWqtWFVj817rUQ4bSBUmLQaWs89qVuEeh-ljdTPRFu062UkWPSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاسر آسانی پس‌از خطاهای متعدد بازیکنان الغرافه مصدوم و از زمین خارج شد  @Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/468053" target="_blank">📅 23:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468052">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO76tpuQxsURboq-vwhtOlvEh6wc4kUDek0wlBWrSQEMuC9XO3jEMxWi_fzVst9Fb-8E50_4NMGOB7rqAcX3Om0pd5eFx5-3UyyZ5WhpaB30hSaxC07B8sGQB050J90aMfuEBRtqPOuV2oqeEqnhH5YcyshjiQ0NoiEQ0KeoHY4SY0sbNnnTJA47UIppyZLt8LCnZI3tM8qyw2OyfZlgkX7xPNSmzXE5hfNre5srN98nrbsr_rrKhEfoYjts1TEh-1AriYlV4U7lVviJnWd6VruxyQ9H_O5KG9aw1139ADGrT6Cy1rfcIlN_8n9YM0K3ic8AeDYwAM12GC7Zm9c8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا حرف‌های زمان عصبانیت، حرف دل آدم‌هاست؟
🔹
خیلی از ما فکر می‌کنیم آدم‌ها در اوج عصبانیت، واقعی‌ترین حرف‌هایشان را می‌زنند. اما واقعیت این است که در بسیاری از دعواها، آدم‌ها بیشتر از اینکه احساس واقعی‌شان را بیان کنند، به خشم، ترس یا دلخوریِ خود واکنش نشان می‌دهند.
🔹
کلمات خشمگینانه در کشاکش یک تنش، اغلب ابزاری برای تخلیهٔ هیجان یا سپری دفاعی در برابر آسیب روانی هستند، نه انعکاس دقیق احساس قلبی فرد.
🔹
برای همین، هر جمله‌ای که در دعوا گفته می‌شود، لزوماً حقیقتِ احساساتِ طرف مقابل نیست. گاهی پشت یک سرزنش، نیاز به دیده شدن وجود دارد و گاهی پشت یک حمله، ترس از طرد شدن پنهان شده است.»
🔹
پذیرش هیجانی و مطلق کلمات پرتاب‌شده در مشاجره، رابطه عاطفی را به سمت فرسایش و سوتفاهم‌های پایدار می‌برد.
🔹
اگر هر حرفی را “حرفِ دل واقعی” بدانیم، ممکن است زخمی عمیق‌تر از خودِ دعوا به رابطه وارد کنیم.
🔹
مهارت کلیدی در حل تعارض‌های زناشویی، عبور از پوسته ناآرام کلمات و شنیدن نیازها و ترس‌های زیرین است؛ پیش از آنکه قضاوت‌های شتاب‌زده، فاصله‌ای جبران‌ناپذیر میان دل‌ها رقم بزند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/468052" target="_blank">📅 23:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468051">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp3G1zGAdGdZlmPBAuoqQn0_Wu-peOF9Bvs4rR9-lrIaA3Z7ceD5b8bJBmbt95KXu-oWzqJx9qZU4NbjuSwUVb07cAHTxqOlINSp5YVC2Lj4Ks_am88H_0yTuKZPDpDcMQi0A79Rz_vmUX-Box_9JpWJc7xhoLC2uPoTjO-NECakmzYTS3C4gJvOYbNaxZSF0moU9iKecDMUpiikawo_XHaKSVNcqLMBBVN_RxS079cyUTh8un61j-On6CAJmZhyNwlmSpgaw-hyBxNMBo_0QgWFkvcluw7_KHFuMoRO0jGlDHPgy2aliyuqUEwMPaiwLfeVo8GO92D7kVtRgGO8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای انتشار فیلم قدیمی کتک خوردن یک معلم چه بود؟
🔹
بازنشر فیلم قدیمی کتک خوردن یک معلم با انتساب نادرست به تبریز، درحالی خبرساز شده که بررسی‌ها نشان می‌دهد این ویدئو مربوط به بیش‌از ۱۰ سال پیش و یکی از روستاهای استان لرستان است.
🔹
پیشتر نیز این فیلم در سال ۱۴۰۰ در شبکه‌های اجتماعی منتشر و اعلام شد که متعلق به ۵ سال پیش است.
🔸
بعد از وقوع این ماجرا خانوادۀ دانش‌آموزان برای دلجویی به منزل این معلم می‌روند و این معلم نیز آنها را می‌بخشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/468051" target="_blank">📅 23:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468050">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsarrRI-bI-ftxRv6Nn0pTA_2E4WWlEqOOP6bkQAd3y-jT0ESRulgONwl8klvV9YDD2CdvvKP2hZTl_ryqQA4_h1OjPhGo8lTBm-SoWS56YIgbxqcwPj0V1O4h-RR2imeasolc7YgeAjLJr_docOJnuFKj6mnIfvV3s7L-qrU4J-gOmbT5Y6VWE9fDasLEefjAVKbgWC-_ioSPvAiSTLaHquSFjZiHkBtwgp4at7azwdlGAZdtlA_beM91NP86EPraTXNgelfOthCy_MvQXda49ZaF105VL7ywiKDUT9cVwK9Oa9pmc11nsELFGCOO8ExnVq3eLp50fBF1S0glv-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  جنایت مزدوران سعودی؛ شکنجۀ اسرای یمنی در تعز با سلاح گرسنگی
🔹
هیئت ملی حقوق بشر یمن: صدها زندانی و اسیر در زندان مرکزی شهر تعز، که تحت کنترل مزدوران وابسته به سعودی قرار دارد، چند روز است از دسترسی به غذا و آب محروم شده‌اند و با خطر مرگ ناشی از گرسنگی…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/468050" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468049">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4838d8be2b.mp4?token=B0TF1QfrG5N1Pmy0fC560MTLD6BjLzwpNN2i6TLiPFbvLmJWZF1Kvw9er8ihAMz8Sxn8A-lkK1xuOUDycmBpkqtt9JwHJkETztaLaF9EIc5lu5lMrXTB8dF0mpmb1req6GRR-8Dq3t0EmrtoIPpb2nVhmpO0mQ_qD00aJ04BVN49nLJQ2ARuVpOyXBL9ZfzIEschK1-N6MILufstNcxa87VjrkeYQ3DDX-OeeYB0nQyuH1_WyxNO6IeG0cGCmaL0w0mrTyXJ_gDoGg8SMbv7rhJk8f2vtBl-qlZKkGPSopnus-fUl2z-x5isTxdbFhgaKEFmX-0Z6KkDF2ZfWxAqxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4838d8be2b.mp4?token=B0TF1QfrG5N1Pmy0fC560MTLD6BjLzwpNN2i6TLiPFbvLmJWZF1Kvw9er8ihAMz8Sxn8A-lkK1xuOUDycmBpkqtt9JwHJkETztaLaF9EIc5lu5lMrXTB8dF0mpmb1req6GRR-8Dq3t0EmrtoIPpb2nVhmpO0mQ_qD00aJ04BVN49nLJQ2ARuVpOyXBL9ZfzIEschK1-N6MILufstNcxa87VjrkeYQ3DDX-OeeYB0nQyuH1_WyxNO6IeG0cGCmaL0w0mrTyXJ_gDoGg8SMbv7rhJk8f2vtBl-qlZKkGPSopnus-fUl2z-x5isTxdbFhgaKEFmX-0Z6KkDF2ZfWxAqxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم استقلال به الغرافه توسط گودرزی در دقیقۀ ۶۰
⚽️
الغرافه ۱ - ۲ استقلال @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/468049" target="_blank">📅 23:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e4f6c8db.mp4?token=W1xHr5rXIOooUvtKIFIBZcysPVb9aUYoVbJTd4SphZoL2OhEY3GxIzvhlH-tAx-cw5wUBk2U5_CZYNeE41g8-9V2EwCakAZfF6KmDWUPytscJ79Rjl3fSCxnLEg_L09_Ul0gkQnnWVAccwfmVjf5EVU4NKdPDrsJEiQzQQvHvkOITWUQttzOummYR3DE2xDJH7dC2XElfdxsNyhkWGVOTkiIfUeRyKmVTL_zUkgSEIYFTLVdGOSPF5XvLzjZKxR-rKJ0jwBCVrkWM3NwimYU95Vin4Xi6psxxnyWMYBABfNLnK72tcOklyw2eCGg__r1cWIHGXJN2PhnRzqTG0hIXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e4f6c8db.mp4?token=W1xHr5rXIOooUvtKIFIBZcysPVb9aUYoVbJTd4SphZoL2OhEY3GxIzvhlH-tAx-cw5wUBk2U5_CZYNeE41g8-9V2EwCakAZfF6KmDWUPytscJ79Rjl3fSCxnLEg_L09_Ul0gkQnnWVAccwfmVjf5EVU4NKdPDrsJEiQzQQvHvkOITWUQttzOummYR3DE2xDJH7dC2XElfdxsNyhkWGVOTkiIfUeRyKmVTL_zUkgSEIYFTLVdGOSPF5XvLzjZKxR-rKJ0jwBCVrkWM3NwimYU95Vin4Xi6psxxnyWMYBABfNLnK72tcOklyw2eCGg__r1cWIHGXJN2PhnRzqTG0hIXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل مساوی الغرافه به استقلال توسط ساسی در دقیقۀ ۴۸  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/468048" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDEqvQ2CIH5XQslE_EfdMkLxk762yPgK_zdNshtqpBGLUA0c7DHXhzwqY7BQmglT-gFMGrhOo5Gqnm2pydecQNUC3JZ4vf8oYJBJOUAvEd-t2Qdo8KHSvY9JDws3IZj8WA9hob6c7F4U369jdpXpMqiNfm79s5nLyGDjc2uPFtn6loJL7obq0mxA2YtsaitSgYsUhUnXGHNld7m1xAfcYDBD8oRkIVcqwTmChL5NTigJzIDJJtT0Yd6lw4LtJqaQwDvU_OxcZjXS5_H7QzIfVmbqsm1_nlDV6uCvoIGvZZFy5RlNbWbM4NHs3TaE_T11yv8LXr9N_0mclEc8ol8NdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAQbU5iGt-rN1msCKYoxWZoOFqzLLa9UQAru5dy1oOy2Bae3WypXVsUo3J9vphtSmEQnSqeAHsYzubKEnvKQ1mM8wyhapjvjhwUh-JJvKjJRYJFcaoi5qjBdmHqeYwB6HVF238nXL8fHqQdHpqfAmXI4fhC_8rZ-ZU3RrAallCJWRQkRL_dla-3GnGztDBMCvgR7E3xwWdEv5HUWqtHG2y9wEsItdAswR8R9jgjVKmM8Q6bfPexTAEU0vnYiMa0EhPG34kISYHwu2nOG91ryfXAA5dKtjVOwKk28pcQGSwsP8wpDlOloeOHiJcG_-m2qelPxx_2JotSV5bhsoOhDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IE1nQiV8W5ooo831C9wkX2GvKl6V2LJcBSZJ_0fV1vuMvzGGP-WhqMtnkeK8xQ3_v9tmuqXJGhmKoSB6rsmSP_CWyGeNRSWO6HSfC7skE3sskNdDCCAI6X7k1mKQlknR0n5zh_Qb9wFLiGJRqS_-chBZ1tRnfFPXmX5aegadqyhaWG0Lgf7kZAfFWlyDj19caGQ6Iz6GF43SGQsmKmrfMHphYuSkqApNgFyouARJZrfqbIa4JI6yKf2jS8JG6LnvBgT712Kw1PDhMYPJIHqW7CgJsSAIBYdFayZisnD_erlDm5aXzXL56ZPf_skfaHNGdU6PTBKq9VMo_lgfyO9DxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqLNlPWDLfnXOKhy66qhhPTiKYpRd43XhYWS_lVrX_pcAN8X5esR1ciP-1gvCSNRPJ8l_lke0PYJzWsRQqrsSrBxXk_Z1iE_5Dk9V9FI1Hts16MKtidHumbmEYoFDG7Kmm4HGKLoUbqNmWjyLRaIJf6YuE3AnIP7Q8Evy3njGfja2yFuwLZQPVACosrKM9YPlMHuagfhS1q9X9IQGCGDVX45OzsWckO6vK77wbg--Sd4YD1VmBuvZPifipxC0Za7C1EWX4_Aj_iCzFpx7Q1lpDjLobcctx-bKTUZRd-dqeP-b-01sqltVcTsjzfdNEWGVZbAUL3rwZ0KancPunUFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUVgmQBMJgr5fBovk26waG8yUkjKROnXJh637eyT80Y3y_jK-bG5lC-Xb_W1VP7-hNy7Q_Vtn5vOlP7hy4j1pA7h0Chpsa_64rgKGdAYX68wQdQ3Y1OvRdKy1m4n-_GVzGp6OQ5rSe2OdrU2vbvpHQc4aJZOWE7QMkwzUC58Vf-qXD4xZyHJmTTJXFdM3_3f91loStN94sySGGYMMd-LL_UbFgGIjEj3oobj0N4qmflTSdo93b1Tanm-pF834PLTS6hjFcdIIgtW4hJdgLuhMECWb0aa24hSOrvYTkIDNc1YW3_21V6AsZ0tou-MJO9drfBOlSyCoEVpq_zQuQa9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LU6mGVDitCZM4-MVUpSW_cipCEO71sirz3iINAprEI5d3YW7sfod5VasjVaMSfYG_ijnJZJHWPpGne2unB-_8h4qM3fVNJsHXKmlWymeqfYED_roK41SdCt_5XpUxjf8p23Z0lKho_Y-iKDakxFHMR_mxmVPap_DGQJMO9JVQJaXOZMRArcpoEo8tJyeDX1kkR57MdWkZLi2Q0afRiaIOjfgUje12Hqijx0slKHBzBXESyzh0_2q5eaheMMLXie9S-PhFbyOt4xR1f3lsCpAjYzZL8nCF4r8kApROBstXaHn11RLyAvJP9JA2P65unkIk6t5ogcQDMB9EtkfQmnLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btADuFgq4Mca5gtAA-I-Q9_H2MG-oTyvrqg1Nlyp59lGDUSgYDUCcTITPtc6Trx7DM6fhhO2pyvNkWHhPzfCH8IyUxfVQNvWzJe0LbSsF-kPEn0dE9wGtKio6NfCSI237BwAaj2uCvBDQDUs8-L0deXb1bBDFvkluEBuQPziTX2lBPdcomUksmo7BRVGD0A6Tic2B2HvV3R9hfCIkldl5TVmhPW15BvwLu6YSWgxHZQb2axNmPsidKiGxPDiwnZQ0md6e0b4abKWEKJI1ZKr-sO7qx_o67TFYNlYC8HH4N-tDCxMB7nL1Y8LucTyCBLmK6LPj_LMtQ_bhDU0ece9Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونمایی از یادمان شهدای مدرسه میناب در دانشگاه آزاد
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/468041" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe069ae48.mp4?token=dVmH4Th9WfuIExjpNXZuy9RTwN21V0fLdXQRSFuLZ3DCMDTw6w-WU6MlI36WSRnVjMRvjEPGHdqeXwZEp6InviEli-U_uKBj0UT8HnHfQ0pmqkpwBUY5dns0jc20LzAY2sW4TKwGPAXA5WJPx0dK62KRMqftPg6MLTnBstv8P3b1tbIWs4pYH5fUVWJmrAqzDC4AEp1nOaKXEECU4RJYxYsikLRjaF7hV1dDcA7ywmFg_ATrrfT9aQc-QbmR4rS-RF1m27ZyTOsaTQ8syuKLjM05-ibawVsjrhDJGGj5qYW7hunHmym-kkUJpLuNqBwi8T9usIGN0Q-yVAybk3uUow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe069ae48.mp4?token=dVmH4Th9WfuIExjpNXZuy9RTwN21V0fLdXQRSFuLZ3DCMDTw6w-WU6MlI36WSRnVjMRvjEPGHdqeXwZEp6InviEli-U_uKBj0UT8HnHfQ0pmqkpwBUY5dns0jc20LzAY2sW4TKwGPAXA5WJPx0dK62KRMqftPg6MLTnBstv8P3b1tbIWs4pYH5fUVWJmrAqzDC4AEp1nOaKXEECU4RJYxYsikLRjaF7hV1dDcA7ywmFg_ATrrfT9aQc-QbmR4rS-RF1m27ZyTOsaTQ8syuKLjM05-ibawVsjrhDJGGj5qYW7hunHmym-kkUJpLuNqBwi8T9usIGN0Q-yVAybk3uUow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به الغرافه توسط آسانی
⚽️
استقلال ایران ۱ - ۰ الغرافه قطر @Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/468040" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468039">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PesuimEXITbO_4jPw3oedpmNYXhCdYHfyYKcJISMGfRMIpOgWVTaAwdQCu2a1pvV2bxlRg3DLcu0Uv1h75t5D1fCDcshlllhi57KIwrJsoGyGY3H9Adguwg9oCcnMJh7evFwuyNLTPzAA1brQMGCWgavW78FAIfq0hAn9P8LXYWdc_dhTvaSWlEcWIBQCYD2hIkqW3if6xmHFAQqXxABbLH-Gb0yY7YshQCyare1hIIRcFkOlr3-HHQdTYEUHPop0DGNJo2nsc7_N-jmCpxr2dSULgEntt-1zpoCUbsOHHa-uKLIrBX36vx-htMmB3Yfw107CNvYOFhGl5PqXaX1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل آرامکو: تا تنگۀ هرمز باز نشود، فشار بر بازار نفت ادامه دارد
🔹
مدیرعامل آرامکو: تا زمانی که تنگۀ هرمز به‌طور کامل بازگشایی نشود و اعتماد به بازار بازنگردد، واقعیت این است که فشار در هر دو سوی بازار نفت تشدید خواهد شد. حتی پس از آن نیز، بازسازی ذخایر…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/468039" target="_blank">📅 23:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468038">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌  حملات موفق یمن به فرودگاه ریاض و پایگاه خمیس مشیط
🔹
سخنگوی نیروهای مسلح یمن: امشب فرودگاه ملک خالد در پایتخت سعودی و فرودگاه نظامی خمیس مشیط هدف اصابت دقیق موشک و پهپاد قرار گرفتند. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/468038" target="_blank">📅 22:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f56d24fd6.mp4?token=aXBa97zfz1d1bp_OTJ0AwQN-KzN0rT40EtmjY60Mqsdtglht4RD7Bck8DHtU8xElQ1jqvsiH02gkku3izj-npK3HL3V0-s5nk3mhF5ufqf20Y0B0TLnUebsa3iQdjrKSXUHdjqY_QJDZ7rHHefceEUjAkh_7jYjb-DSLg7B8scyQyDWYWMvWuG7j4MI7EFRyoLAmz3_5r2wGHn7zdhuXiZIoEyc4Ahq-qnUiMUuULpTh2GPHsPqj9wKLCAl_i1leAwVDXjT9XPkB6r8FjDdK_PPin5uXWktLfxHMgzRQppmnXScDuXTr9HrgzJVfu78SpL9G3516kBB3rktxKaaCVgOGuple3-q0bYJYyJJh8SXuVQun1oYOvBQFNdoqFoLn5-uiSVGNd_YnHk5e8uJBP4Kn0tbY-2YNoDwfAIVDvq0-wJX5PxwgC6z19eQyUa65NZPO7Z5PRFGmXKUcLnxU9OLZ2gEWs5DgA-TkON7c3_mqG2B4zlnjfJpvjqK5uhxv_HgVR-oIjZ4f8hz1XBeWRAAh8sgf8QrrqAJJFD6pwnmtHPjRz2atJs5hBuocug7ETjBaA_2Ah7GWaxKSW8zh9FqrtMin6cCyV4XkGdKCEorkuYlAF7iGEpqMRTlqVFNNAf-dKynBDxgKqA8BpyD-uomLFgjjmF6nwdtddkPVXcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f56d24fd6.mp4?token=aXBa97zfz1d1bp_OTJ0AwQN-KzN0rT40EtmjY60Mqsdtglht4RD7Bck8DHtU8xElQ1jqvsiH02gkku3izj-npK3HL3V0-s5nk3mhF5ufqf20Y0B0TLnUebsa3iQdjrKSXUHdjqY_QJDZ7rHHefceEUjAkh_7jYjb-DSLg7B8scyQyDWYWMvWuG7j4MI7EFRyoLAmz3_5r2wGHn7zdhuXiZIoEyc4Ahq-qnUiMUuULpTh2GPHsPqj9wKLCAl_i1leAwVDXjT9XPkB6r8FjDdK_PPin5uXWktLfxHMgzRQppmnXScDuXTr9HrgzJVfu78SpL9G3516kBB3rktxKaaCVgOGuple3-q0bYJYyJJh8SXuVQun1oYOvBQFNdoqFoLn5-uiSVGNd_YnHk5e8uJBP4Kn0tbY-2YNoDwfAIVDvq0-wJX5PxwgC6z19eQyUa65NZPO7Z5PRFGmXKUcLnxU9OLZ2gEWs5DgA-TkON7c3_mqG2B4zlnjfJpvjqK5uhxv_HgVR-oIjZ4f8hz1XBeWRAAh8sgf8QrrqAJJFD6pwnmtHPjRz2atJs5hBuocug7ETjBaA_2Ah7GWaxKSW8zh9FqrtMin6cCyV4XkGdKCEorkuYlAF7iGEpqMRTlqVFNNAf-dKynBDxgKqA8BpyD-uomLFgjjmF6nwdtddkPVXcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراغه در ۲۲۶شب ایستادگی؛ میدان همچنان در دست مردم
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/468037" target="_blank">📅 22:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/468036" target="_blank">📅 22:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468035">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPW9U7aC0NdxKG08SjKF2G9Ho5Fe7ScisdZtu-OJejgvLT47TESLEplQCGdVedRbvxUtNoCvzoyDU0WjNfBPATLX62AlHRYC8nlpyUvBhpMeOgME9mNPJfcie3fmvyJaSiJVq4I4edjnKt0f0F5Dlok-dtqhE-SYI-tAqGTZdU0vjsP1Mr9HoDRDDAqWdCL7codY0IwPZOyc8ZpKeu3jnp4PamYAbx1juUIkmhMEM5zD1wAdlJMT1akDLZwdHJ7U8kJTzRjxYLH7Yo1YkDC9Gl1kv5O5YGir9DOtvT-XMoGDt6GvqOI8CdHUlKZCUnB-hhPg4hB-LzuUGPbn1yivNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی انگلیس وقوع حادثه برای یک نفتکش دیگر در جنوب تنگۀ هرمز در ساعات گذشته را تایید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/468035" target="_blank">📅 22:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6ffedcee.mov?token=AHhHCpPTv6JBn-DKYfRNUKy-XOOPC2t6xzKsuB_4w_DLZHqyHA5xEJQuYsVNFbbH_SdznyuPG6xJ3Yf6R0hJ2uGdLEuULVWkcaA1DKW5kCih1Z-8T1qAEgQum_aHorgXFpGXj4LymLKkfqpl7VZb2Gr0FkCAHl7_AwRmikS8UGUEUw_-NQoRNcl77Y2-znJM8ACo1827WpqokdXgWbxZ7FZBsVyypUqpxVccEs_igaQYBlMJtiKUfZnYnj9CAY1x-C6iyD9Rm6uwD8ut-UAgTu_Un9ztSN_aOpEa5j6HFmNokHxrLpA-hIcE1htAYXxuKPYra-v4a3ud3-z1CfAAFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6ffedcee.mov?token=AHhHCpPTv6JBn-DKYfRNUKy-XOOPC2t6xzKsuB_4w_DLZHqyHA5xEJQuYsVNFbbH_SdznyuPG6xJ3Yf6R0hJ2uGdLEuULVWkcaA1DKW5kCih1Z-8T1qAEgQum_aHorgXFpGXj4LymLKkfqpl7VZb2Gr0FkCAHl7_AwRmikS8UGUEUw_-NQoRNcl77Y2-znJM8ACo1827WpqokdXgWbxZ7FZBsVyypUqpxVccEs_igaQYBlMJtiKUfZnYnj9CAY1x-C6iyD9Rm6uwD8ut-UAgTu_Un9ztSN_aOpEa5j6HFmNokHxrLpA-hIcE1htAYXxuKPYra-v4a3ud3-z1CfAAFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/468034" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
