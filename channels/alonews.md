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
<img src="https://cdn4.telesco.pe/file/oTF_naOUns1QMXRzE2BIOHta7yf28o7ulF5EO_D-BOdrex52rFOqMkHqEdohTTJBj82UcrfMsq6khu0qPlXUHkebJWLX0GZf8k1zIfmdjXFsJTvRt5-wU_d4ZNn2V5mBiTaQEY4hL9ZfdSqQCL3VBgfgCggL1_tIVoy5hZ5X5ZxOIg99AYGWHWF6K91fGSgjbLXoXxEysZarV4mYY1xbHiqbefNRSW6vG7h3vu_eaQidqoYZHkEhT6vJCgOV0N13Uy7TKU1wHba_5NXRQEllpjJ6DjRPtMOivGY5XzOL5ADjob4U5a__tZ7aoUlNqx5wvdp5LF-FrLcpi6Vz_Wjg8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 01:20:26</div>
<hr>

<div class="tg-post" id="msg-144482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KThovjbt_bVAemKSjSlDt8nwYiD3K-s4DNrLBgapeDm1_iqu4Ptf_I1nT6XqDk5J_MwyttdMGZ_3CJJVvCBbr3r6PPTXt5uG1cuob-Wlt82NvVKAdXarZ1DBN6ReSPnZN1J3nbpqqBLPz9jmAGvU_PT7IaAsx3k_CgCpLEt6ug34ikl8_xJwJIE8MxqDosUgU1ps-B5Kxt3ZAXnd9yXcZtgSp2VaVtDVH_l8vOJo1h9-Rj1hOff-i-XJaZfByJp29cvfR4PWUEutxEeb5E8CGOtHpP7kawiDisojVKdqJrUwrhfvq6ISCdW5ujifTaw4uvviZPM0nNl2Au1eP9YWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مالی، خبرنگار:
چند روز پیش تو یکی از بیمارستانای اهواز یه بیمار تو ICU به طرز مشکوکی فوت میکنه، خانواده بیمار از طریق پزشکی قانونی علت مرگ ناگهانی رو پیگیری میکنن که با بررسی های پزشکی قانونی معلوم میشه چند نفر از رزیدنت ها و کادر بیمارستان خودشون مریض رو کشتن، تا تخت بیمارستان رو برای ی نفر دیگه که پول بیشتری داده بود خالی کنن، الان اون کارکنان بازداشت شدن و وزیر بهداشت کمیته حقیقت یاب فرستاده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/144482" target="_blank">📅 01:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfNA8MekEBA3vMZNUaIDtLUURzZdUzRjvsvcIPsTfpHekbUfvgF1oyknzV2CR9NVst9rLgZ-G6AEvCng8E0ag7hyCOQItcZE52eEv1He0cSTZih55TKcpA-O55PNUuiR0PS3Z4gq8FWl1db88P4UzFIdvcQMowtpWoG3mVGzxKm2Nf1B0lqZWNMblsdHvMrOLDP9GLYHepuwDdUBGeZ-Xxja9AOFNFwC6mgdy-aFhmlyExeFJsNIgCsR1zzSD1LRe3U7wXStocCmL75BWe5oBWdcGkATSRYgRuE-IyBF6xSsZ0EnMcBgiihp6HewcP-a8MvvJvsa_hgFmNNKsMqX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5d94A8uivDZSBo8FY3LwIErNM0OcqsCxBwILoFL1xGT5KlCZ6NepQhQ3YPXKVNIuo4tL6Pfwmyo4jE3mrkw3Oy4vxpQp8aGuMZceLDVI6nvhhOu9BxGR0z12qU4kLdngmyPScmAaSFlYTa1ki3f3vm4GSmWBh5ey7TBhMf0gWJTFWauLwDnUaDgpYuL54uTGX0ZKU6qEvE-5_DtfpfPY7E1RG7s-r4ZJQkmGxuZtcZz0yV9C_vpDFMaoaD9fVXkpohscE65DVCxE9LDOpewzM4WFk5GURqdlanhyG-7X5zbwBMUizlMvExOFV2jBJCIHPwTLYcJdoqFsckRjKC4Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مجتبی ملکی، رئیس فدراسیون بدنسازی: مسعود ذات پرور یه اغتشاشگر بود و نباید ورزشکارها اونو تشویق یا عکسشو تو باشگاه بزارن!
🔴
جوابتون به این شخص کچل چاق چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/144480" target="_blank">📅 00:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بانک مرکزی امارات متحده عربی، بازرسی فوری از شعب بانک مصر در این کشور را اعلام کرد، این اقدام پس از آن صورت می‌گیرد که ایالات متحده تحریم‌های مرتبط با ایران را علیه فعالیت‌های این بانک در امارات متحده عربی اعمال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/144479" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر علوم: خیلی از اساتیدِ اخراجی را که از کشور خارج شدند، نتوانستیم بازگردانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/144478" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
موسسه گلدمن ساکس: روزانه 15میلیون نفت از تنگه هرمز خارج میشود و فقط نفت ایران صادر نمیشود
🔴
ایران با دست خود، خودش را محاصره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/144477" target="_blank">📅 23:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddaa4078e.mp4?token=VA6CY99RDTfwNvA76COynA7Qzea-nL6whfRLSFA20C_YWsxl2JZ4xqyiIZ5APi1CHFUUCc8YZVv2_lDy4ekq3d3-LiTWpwkZIue9RsBwcJMyM5vQ6HHFyUwFGgW-A16yenz3D_Wu464zLwR1T4tb9g3MSg6Q-uTWKb_YG4qgLFZybN5xSp2zFuwopQDKTsGHcLuDafHMq2MsDBO4iw8Po9hTgK62Yu-u_dFGobu1UJBeQitgpWa-nIQk7GssHGUtJLJPLhyHOI80zv0CxNGpH_q8Keh-TGhDsSENGX8-rEElQfsETKzBL2y-KMomkyyvcQmaqROQN7CqXM0Nq9V8enqL6_tWj0VFAuLUnh_Ru-qqFsu1-TDq0XUTDA56mPGn-l7qVos0-MtHkrOEmxyofdGTIa0dYpWLrFJWcO2o02sN2Ui2SSr5fWnMtkF0ScgVpkpJ_5RT-1GCUtFWZdZzds7fyH62NJ_Yy3HUBhg8dBkzOjt8zDcqxblcHw9PUvJM8rZ09vuT4IazuH3Q84hGF3HOJOyRfpIWKdsA8ctER9e8206Hn3xdwKBbbeXGO2ALXETPSMnv68kEUHqi-JOV--e7I5LfFd7WRmmPnV4zPaOKvE5X9DAaqrX1Hk0vPxT6VR3BGuvcQGzsNkqS9iFspdULRm0Xcwr-PvEAn2NzhDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddaa4078e.mp4?token=VA6CY99RDTfwNvA76COynA7Qzea-nL6whfRLSFA20C_YWsxl2JZ4xqyiIZ5APi1CHFUUCc8YZVv2_lDy4ekq3d3-LiTWpwkZIue9RsBwcJMyM5vQ6HHFyUwFGgW-A16yenz3D_Wu464zLwR1T4tb9g3MSg6Q-uTWKb_YG4qgLFZybN5xSp2zFuwopQDKTsGHcLuDafHMq2MsDBO4iw8Po9hTgK62Yu-u_dFGobu1UJBeQitgpWa-nIQk7GssHGUtJLJPLhyHOI80zv0CxNGpH_q8Keh-TGhDsSENGX8-rEElQfsETKzBL2y-KMomkyyvcQmaqROQN7CqXM0Nq9V8enqL6_tWj0VFAuLUnh_Ru-qqFsu1-TDq0XUTDA56mPGn-l7qVos0-MtHkrOEmxyofdGTIa0dYpWLrFJWcO2o02sN2Ui2SSr5fWnMtkF0ScgVpkpJ_5RT-1GCUtFWZdZzds7fyH62NJ_Yy3HUBhg8dBkzOjt8zDcqxblcHw9PUvJM8rZ09vuT4IazuH3Q84hGF3HOJOyRfpIWKdsA8ctER9e8206Hn3xdwKBbbeXGO2ALXETPSMnv68kEUHqi-JOV--e7I5LfFd7WRmmPnV4zPaOKvE5X9DAaqrX1Hk0vPxT6VR3BGuvcQGzsNkqS9iFspdULRm0Xcwr-PvEAn2NzhDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدر عبدالاتی، وزیر امور خارجه مصر:
ما شاهد بحران‌هایی در تمام جهات هستیم و در شرایط بسیار دشواری قرار داریم، به ویژه در مصر.
🔴
به طور خلاصه، ما در یک منطقه بسیار ناپایدار زندگی می‌کنیم و این وضعیت غیرقابل پیش‌بینی است، به خصوص پس از جنگ با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/144476" target="_blank">📅 23:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006470b470.mp4?token=sdXTdAyp_o7VyLxrmSMhgCvA5nfJRAtKsKuCcQRf6XZsc_SMwlGQxWINgQ0hOSs88yD-SEKJ4XvQuiKlDKoKoA5dCS2r31MqN5mOHAZFPsT_sooDpzVoamXxE2SaNFW5pz5cKMIO3ty3-CqIzzRwdWO7gBQ7uG_kHNLUkIypdIDBbei3tDfkpXXyIL83s3gt0MBM92h_yXHYQ-18a1UjAxR6dzf1VXk2TK5kTGrdqWeqKR3WK-O1GaUbIiUvGtnipX50n3cSmb_hBSF93n2hUPC7LH6wOe-1E2GrdSyMoc-vT6l0pUZ6kKuN5CSkczeiNOHEv8AYG_XTZDq50_aD-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006470b470.mp4?token=sdXTdAyp_o7VyLxrmSMhgCvA5nfJRAtKsKuCcQRf6XZsc_SMwlGQxWINgQ0hOSs88yD-SEKJ4XvQuiKlDKoKoA5dCS2r31MqN5mOHAZFPsT_sooDpzVoamXxE2SaNFW5pz5cKMIO3ty3-CqIzzRwdWO7gBQ7uG_kHNLUkIypdIDBbei3tDfkpXXyIL83s3gt0MBM92h_yXHYQ-18a1UjAxR6dzf1VXk2TK5kTGrdqWeqKR3WK-O1GaUbIiUvGtnipX50n3cSmb_hBSF93n2hUPC7LH6wOe-1E2GrdSyMoc-vT6l0pUZ6kKuN5CSkczeiNOHEv8AYG_XTZDq50_aD-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی تجمعات شبانه در میدون ابن‌سینا خانی‌آباد، یه سامانه پدافندی رو گذاشتن وسط میدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/144475" target="_blank">📅 23:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
حوثی ها، مواضع عربستان در استان الضالع را با موشک و پهپاد هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/144474" target="_blank">📅 23:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP_PRVMN2TGNR-RUpAJP9EM2SKxC2HubGAsPVFQFB0mJIxjGwm67nDmQKBOPf5lttAKA5-1LvAYKPhQnps_DDRHfghq4-0EvSUbSsxnxWjJmEYKy5d_m2NAG0SC2ov6tVqb-7B3zmwBvzww-B9RSWjI4Mkv_VmxEBgx-WcmXlMXKCbytupB1I8JF9wt3DXOYae5b1P1Dh6MC9MqxXjsUPtGoR5md9hKk_Dvi7Ag51mRN4uRcvPGck3tnDo8w_AwzOmQVSXe1J34BkDTUxW7VPIm5OXg0egZzX4Jp2iqiwtxlXqGLypkFxN0SyR5hxbG-9FEGk6dwmjegYO_U4PBPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در یک کارگاه در بزرگراه آزادگان؛ یک کارگر جان باخت
🔴
در این حادثه یک کارگر 21 ساله جان خود را از دست داد و یک مرد 30 ساله نیز مصدوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/144473" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بلومبرگ: ترامپ باور دارد که قدرت غلبه خواهد کرد و با سرسختی او انتظار نمی‌رود جنگ پیش از انتخابات میان‌دوره‌ای در آبان پایان یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/144472" target="_blank">📅 23:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khIZ2Yhe-0hQmOiUNRzzrDMv2NlrOYS7AmCCe5CdKOTpbipDobCDK9Lh-mm6YCiPqvuUvWrXusIVGB8EYrONNHSG5CY-XIGsayF0hKgk1cAwAHPUPbkD6Q4Dzda-YN3UBMTMkOkkK7etqeSIbFerQdNFLz1FWLfThId8b9YeB3YiXiMyNHDoJPwZ9p2B33Prqmg40pjoZwB9y7c63vUYqhDyQOkloFjwp4MUOOngXEUL2la16HaIizVfJ5wYPkHm1KSisaxzMbsBwieb9uitE1WKBn1Z8ERzBUk55dx5bBNf0bV8SKnP0kmfFRRCVhO4shVDt5SGTO5Bx9RfFU13iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتیوپی خود را با امارات متحده عربی و گروه  RSF همسو کرده است
🔴
غرب اتیوپی در حال تبدیل شدن به یک قطب لجستیکی برای امارات متحده عربی است، زیرا آدیس آبابا به طور فزاینده‌ای خود را با گروه RSF در یک قمار خطرناک بر سر پویایی‌های در حال تغییر قدرت منطقه‌ای همسو می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/144471" target="_blank">📅 23:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اطلاعات نظامی اوکراین اعلام کرد که پوتین به برنامه‌ریزان نظامی روسیه دستور داده است طرح‌هایی برای حمله زمینی به سمت کی‌یف آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/144470" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a636fbbb.mp4?token=izRUbO4EHM2sQGBtDOqh-NTtKa1ASWldRKLGm1hr-sdMLxivhpq6QgBiuThaX8dPsjODiLl36ZErNTaBmDXZUS-hfxkTdM8ob1Zn9WB3SWT4q5V0-__2IQEcYwdYqh06k1Cl7njDPauIrQDAVRPXtwVt6z4mNfegDeade6QMnyFaTJ_f5f8IO_ciucFNOGATaX8orj6ddil0jRbk2POIlS-Nk-9NGr0F8e6_gLn6iIlZmdGZJGHa2fuh9LPjMB2tAcJ4XQ3LegNEjFkSHY49J-LXhQaLYNm47Uz82ioS4fz9huKoF5mgd5KWkuYeiho89g_A0_-bSNzCOdL2HKHs3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a636fbbb.mp4?token=izRUbO4EHM2sQGBtDOqh-NTtKa1ASWldRKLGm1hr-sdMLxivhpq6QgBiuThaX8dPsjODiLl36ZErNTaBmDXZUS-hfxkTdM8ob1Zn9WB3SWT4q5V0-__2IQEcYwdYqh06k1Cl7njDPauIrQDAVRPXtwVt6z4mNfegDeade6QMnyFaTJ_f5f8IO_ciucFNOGATaX8orj6ddil0jRbk2POIlS-Nk-9NGr0F8e6_gLn6iIlZmdGZJGHa2fuh9LPjMB2tAcJ4XQ3LegNEjFkSHY49J-LXhQaLYNm47Uz82ioS4fz9huKoF5mgd5KWkuYeiho89g_A0_-bSNzCOdL2HKHs3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده مجلس: ادعای عدم فروش نفت، یک دروغ بزرگ است/ در بدترین شرایط روزانه ۳۵۰ تا ۴۰۰ هزار بشکه نفت فروختیم!
🔴
محسن زنگنه، عضو کمیسیون اقتصادی مجلس گفت: تحقق درآمدهای نفتی نسبت به سال قبل ۲۸ واحد درصد افزایش داشته است/دلیل این حرف ها در وسط یک جنگ شناختی و ترکیبی چند لایه چيست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/144469" target="_blank">📅 22:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
غریب‌آبادی: هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند
🔴
تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.
🔴
نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای آمریکایی‌ها در مورد عبور کشتی‌ها از تنگه درست نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/144468" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
مارک لوین : قطر یک رژیم سلطنتی و اسلام‌گرای شیطانی و نامشروع است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/144467" target="_blank">📅 22:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر امورخارجه: تلاش قطر و پاکستان این بود که بررسی کنند آیا امکان بازگشت به اجرای تعهدات تفاهم اسلام‌آباد وجود دارد یا خیر.
🔴
ایران آمادگی خود را از طریق تفاهم با عمان درباره تنگه هرمز مشخص کرده، اما اجرای تعهدات بر عهده آمریکا است.
🔴
آمریکا تعهدات خود را متوقف کرده و برای بازگشت به مسیر، باید اقدامات لازم را انجام دهد؛ پس از آن مسیر مشخص خواهد بود.
🔴
ایران آماده حرکت در مسیر تقویت وحدت و همکاری با کشورهای اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/144466" target="_blank">📅 22:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=XwhEnbwJP_v-IWYYyuXM5i7cHEE33m5E_UMTg_NV-7jnobwtJVdUxIrPoskRHDf-5-ux1rnA6GLeoTobm8PU9Y7XYscudfWVVCBIT_4e2wUqnYpnJYQhhW48DoDNVIWoJSJEE8hsu8Etl0RmwgF_T0ys4nA6fThE46yC9izQl5p7dzTuSAVL4P7gUnpcLgzlzmIYlk-OziDEHg2eBsbov1LBlUeJEQ-3ua5u788dAvjZNe0qPI7q0_mQOR26qq8Vd9KR8gnD9SHZkO6h9jBmbtescdeEiaGEGwskMtdwjDsR9Dpf-ER89lVCotsjDeY1OUg6ozNg9UpBgvpxF6Fppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=XwhEnbwJP_v-IWYYyuXM5i7cHEE33m5E_UMTg_NV-7jnobwtJVdUxIrPoskRHDf-5-ux1rnA6GLeoTobm8PU9Y7XYscudfWVVCBIT_4e2wUqnYpnJYQhhW48DoDNVIWoJSJEE8hsu8Etl0RmwgF_T0ys4nA6fThE46yC9izQl5p7dzTuSAVL4P7gUnpcLgzlzmIYlk-OziDEHg2eBsbov1LBlUeJEQ-3ua5u788dAvjZNe0qPI7q0_mQOR26qq8Vd9KR8gnD9SHZkO6h9jBmbtescdeEiaGEGwskMtdwjDsR9Dpf-ER89lVCotsjDeY1OUg6ozNg9UpBgvpxF6Fppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
مسئولین شهر مراغه سر چاه: با یاد رهبر شهید پروژه رو افتتاح میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/144465" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قیمت دلار به ۲۰۶,۰۱۰ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144464" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyZqDjXqxi59vykkkgyftZB5AU9HPV3x1NVTOsc20eaeoAzFtLCqHtuxt_MhIDuobMb8Nfsewh4VDOLTQ1AFovUj64xeJ6bg1eTIOH9rSd1KDL7bFfSQ7DI69LX5cJDQHxVggQN-3peDHnF2IEoSnnUYjQmii7xdjAKOeGx8ufip48T6Z9pyHsM9Seg7AEmYfPWM8Vb4jSO41WCUvKpC2_IUb7ARYxo3xKRgvYfKQoBKaEKAw9AxulLhYqpYWswqbA4PAFZ3NnMv-GIomow6GPr_3cfxx2RR5AbjQZRr8Uy4p5vtYx56jXnwdaVXvO0WVyXgE4WkKo-d778seNl89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آنتونیو گوترش، دبیر کل سازمان ملل:
آزمایش‌های هسته‌ای اعتماد را از بین می‌برند، به رقابت تسلیحاتی هسته‌ای دامن می‌زنند و خیانت به جوامعی هستند که همچنان با پیامدهای آزمایش‌های هسته‌ای گذشته زندگی می‌کنند.
🔴
از همه کشورهای دارای سلاح هسته‌ای می‌خواهم تا به تعلیق‌های موجود در زمینه آزمایش‌های هسته‌ای پایبند بمانند و «معاهده منع آزمایش‌های هسته‌ای را لازم‌الاجرا کنند.»
🔴
بیایید بار دیگر بر تعهد خود برای پایان دادن به آزمایش‌های هسته‌ای تأکید کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144463" target="_blank">📅 22:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07f1cca6d.mp4?token=gKTZwwJuCpvtj9aMqKMTNhtjMy5J6SIIE1qrbccCzg-d_qxy0XWcgp6hP6RJC6da1Nw6Kc8wGOadA_iFOvehSpjuk1QE2uecpnpCCrpw-ffbZzOtMt1EaUDz5wpx80FbWxdBx5E2pAZsPlhr929BddXGHLVKDW9Z1aDucvj9fLKPwFt4hPOMU4GxSU0MOOYTzP6LlYShtPnItMowHrNpKr54meouCt7djus47KyijNIAABYSsFWiisFQYfuaxsN-zf_OzC3vqq1SWZGbit7FmeGBoBxEw2Z5UdmFj2WeiWpxZJCJs7Vb5cV3YKuWMYWBSHBaOR4Jqe2LfRs_HgLrkK3C99F8F-Yp4_KkkWwlkC3SMdWWHUNUdCjhUGFE6jFnRh1wMCASF142-7YOcQWP-83VGx29J03wf_FewCsqgvaKwbyT2hpFlmKdkMXJLfI9xAa2modMvzrfFG99KwlWydqRnNKh540qtDmnZefxPPHlet1yTzncSR_-ScMrbI1evnMJpb0tMHxdbGwtUi9zyKd5JQsC3YEK_bYJWXEYpRkG-FH3627qgzf2M5RtPiUZYO0F3hB9FbDmJJTxJ0UnCJAV61qfUK_ZBYNbSLPsxHInOCn-FEs0tI9WEGMmVL96LNUoWO-RgWTgNv25bWYsQHLKpnj3J7TofYBA0MddjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07f1cca6d.mp4?token=gKTZwwJuCpvtj9aMqKMTNhtjMy5J6SIIE1qrbccCzg-d_qxy0XWcgp6hP6RJC6da1Nw6Kc8wGOadA_iFOvehSpjuk1QE2uecpnpCCrpw-ffbZzOtMt1EaUDz5wpx80FbWxdBx5E2pAZsPlhr929BddXGHLVKDW9Z1aDucvj9fLKPwFt4hPOMU4GxSU0MOOYTzP6LlYShtPnItMowHrNpKr54meouCt7djus47KyijNIAABYSsFWiisFQYfuaxsN-zf_OzC3vqq1SWZGbit7FmeGBoBxEw2Z5UdmFj2WeiWpxZJCJs7Vb5cV3YKuWMYWBSHBaOR4Jqe2LfRs_HgLrkK3C99F8F-Yp4_KkkWwlkC3SMdWWHUNUdCjhUGFE6jFnRh1wMCASF142-7YOcQWP-83VGx29J03wf_FewCsqgvaKwbyT2hpFlmKdkMXJLfI9xAa2modMvzrfFG99KwlWydqRnNKh540qtDmnZefxPPHlet1yTzncSR_-ScMrbI1evnMJpb0tMHxdbGwtUi9zyKd5JQsC3YEK_bYJWXEYpRkG-FH3627qgzf2M5RtPiUZYO0F3hB9FbDmJJTxJ0UnCJAV61qfUK_ZBYNbSLPsxHInOCn-FEs0tI9WEGMmVL96LNUoWO-RgWTgNv25bWYsQHLKpnj3J7TofYBA0MddjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشوری به شدت منزوی شدیم
‼️
🔴
حتما ببینید
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144462" target="_blank">📅 22:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144461" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c661cdb96.mp4?token=KrPsPigFtZdotyDAdEjMJ7_k5aTQ4Q6et64G-IVovFNmB6Vy0vvGyYBrYTPiiWoGTQglNL3LydIGdEcQMn7OWp_RyJejfnftRw62qHhpKBWDH4gwA6LNrwP3SidFtU0YdEHHykApB2jGnYi42cL4Mx6x3RvvM-oAnvpLCEh5RQsmFlVhPeFScUzvFF-Mut6IWgWEyB4ENyrF-ZkYOtzl1Xi2uZlVIxaGdyzl5P_n355RLT1Dy-_DWvKGKiYvmzMwlxa0jBWErsXT3SV0cyqXs0l85fU-IhR5sHCUoN0xL-l_BmsP5lkbsWZEMe12TVWD0CvOvt4rlm3dsF1esX0GLIq3RMVzltXpXW8KYjMPbfd6ZaYEybR2Xjiwtu-9qIK9ZgIySxs5FUB7XQwtkyM9zqT3VK5ttlCsLk2IRkiM6sl_6fb1bx9rx4oiACIdjo2iv6___BPRVA09W5RfPL-hxBtqBnWynd3_ZhpTwkkQROyNEiiVGY4PpteL2oHzEHIa8a6ZvniyRt_KtDn-NDZK-QX79r_ePwcWjQu5pbTLWtNggZl5US-rI6uVMjbsIvq55rJX7sbygfLriuByWP3j22WGEom3xRWOblSr-nN55AjjdYYbPTf4totxyY5dWq-URooVwhmyMCOQeMqeFG4A1Q8iVOeUqnu_IEo_1TS6Btc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c661cdb96.mp4?token=KrPsPigFtZdotyDAdEjMJ7_k5aTQ4Q6et64G-IVovFNmB6Vy0vvGyYBrYTPiiWoGTQglNL3LydIGdEcQMn7OWp_RyJejfnftRw62qHhpKBWDH4gwA6LNrwP3SidFtU0YdEHHykApB2jGnYi42cL4Mx6x3RvvM-oAnvpLCEh5RQsmFlVhPeFScUzvFF-Mut6IWgWEyB4ENyrF-ZkYOtzl1Xi2uZlVIxaGdyzl5P_n355RLT1Dy-_DWvKGKiYvmzMwlxa0jBWErsXT3SV0cyqXs0l85fU-IhR5sHCUoN0xL-l_BmsP5lkbsWZEMe12TVWD0CvOvt4rlm3dsF1esX0GLIq3RMVzltXpXW8KYjMPbfd6ZaYEybR2Xjiwtu-9qIK9ZgIySxs5FUB7XQwtkyM9zqT3VK5ttlCsLk2IRkiM6sl_6fb1bx9rx4oiACIdjo2iv6___BPRVA09W5RfPL-hxBtqBnWynd3_ZhpTwkkQROyNEiiVGY4PpteL2oHzEHIa8a6ZvniyRt_KtDn-NDZK-QX79r_ePwcWjQu5pbTLWtNggZl5US-rI6uVMjbsIvq55rJX7sbygfLriuByWP3j22WGEom3xRWOblSr-nN55AjjdYYbPTf4totxyY5dWq-URooVwhmyMCOQeMqeFG4A1Q8iVOeUqnu_IEo_1TS6Btc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر کشور: ناترازی انرژی برای ما نگران‌کننده و ذخیره ۸ نیروگاه صفر بود اما انرژی‌های جایگزین وارد کار شدند
‏
🔴
امروز ۶۵۳۹ پروژه شهرداری‌ها با اعتبار ۱۱۰ همت و ۱۲۳۷۱ پروژه دهیاری‌ها با اعتبار ۱۸ و نیم همت افتتاح می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144460" target="_blank">📅 22:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دو مقام اسرائیلی به باراک راوید گفتند طرح بستن تنگه هرمز از سوی سردار علیرضا تنگسیری، فرمانده وقت نیروی دریایی سپاه پاسداران مطرح شده است
🔴
به گفته مقام‌های اسرائیلی و آمریکایی، در ۷۲ ساعت نخست جنگ، ایران اعلام کرد تنگه هرمز را می‌بندد و سردار تنگسیری نیز دستور استقرار مین‌های دریایی در مسیر اصلی کشتیرانی بین‌المللی تنگه هرمز را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144459" target="_blank">📅 22:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca9c5cc09.mp4?token=uqpD7RyLjXu61-ruellw5MFzYQIHg_KHLFf-SwVm03ixS0_2dJavC9Zk8KlqtHYepDmeagPiaXRtEzyn8v1s4AfX8Da98Q3iVe98yaVdpUrf4uCXOULE7KnC9FKxz5Cxf4UWPZoPJP-JUuyYU0bCl1sIpsD4HQNu9Dy-Tuynx-WLZ76dhjxHljTSHiFcGYc4EOSjaDSoHFnjG21IZ0FoV4QsTQDRKx7CA5Y3vi1EMnJckg1SSqRJuwZolWXMhzb6HJxFryLmXOl2yAz6PgZymsM7_s5iSDwAEjjHnbLmHUYl1ZaNqhCPJYwmUXeVFGiFMeE0VqsWB_yi7HmQ_RyFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca9c5cc09.mp4?token=uqpD7RyLjXu61-ruellw5MFzYQIHg_KHLFf-SwVm03ixS0_2dJavC9Zk8KlqtHYepDmeagPiaXRtEzyn8v1s4AfX8Da98Q3iVe98yaVdpUrf4uCXOULE7KnC9FKxz5Cxf4UWPZoPJP-JUuyYU0bCl1sIpsD4HQNu9Dy-Tuynx-WLZ76dhjxHljTSHiFcGYc4EOSjaDSoHFnjG21IZ0FoV4QsTQDRKx7CA5Y3vi1EMnJckg1SSqRJuwZolWXMhzb6HJxFryLmXOl2yAz6PgZymsM7_s5iSDwAEjjHnbLmHUYl1ZaNqhCPJYwmUXeVFGiFMeE0VqsWB_yi7HmQ_RyFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهرک منصوریه در جنوب لبنان چند لحظه پیش توسط نیروی هوایی اسرائیل مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144458" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4ce022e9.mp4?token=e_I4X5WysMOVXS389TsaaQ8KUIpsdQ3rROYxqlsxTGvtW4hIS_Fo94R8mrwZbRaL0hdc8CfX39g2yc1vjXZAAic2sSxVqj1iwKW1yIfOLf2ZUO5hHhWPq5PIwbbzuWDtWcxy3Pm7T19O6_2Q8srVR74PX-TtusupExZmdIrzLBT_u5AFDsq0OEpfy29oRZiUVJkaWR2WiGr5UD5L9WXrfoT_AgBelFF6WmcwM7pESMXeU09J1MP5CeWCDrmBxXTlUCnJzL91q_wu583F7yJ8TXfzOb5jiVCTx6M3ANv1kzZEGfAVGNmH7MuETCJTrcpUEO1L2CgyiCe2ycl5wtVNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4ce022e9.mp4?token=e_I4X5WysMOVXS389TsaaQ8KUIpsdQ3rROYxqlsxTGvtW4hIS_Fo94R8mrwZbRaL0hdc8CfX39g2yc1vjXZAAic2sSxVqj1iwKW1yIfOLf2ZUO5hHhWPq5PIwbbzuWDtWcxy3Pm7T19O6_2Q8srVR74PX-TtusupExZmdIrzLBT_u5AFDsq0OEpfy29oRZiUVJkaWR2WiGr5UD5L9WXrfoT_AgBelFF6WmcwM7pESMXeU09J1MP5CeWCDrmBxXTlUCnJzL91q_wu583F7yJ8TXfzOb5jiVCTx6M3ANv1kzZEGfAVGNmH7MuETCJTrcpUEO1L2CgyiCe2ycl5wtVNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیوانه‌وار، انفجارهای ثانویه مهیبی را در یک انبار مهمات در مایلا، در منطقه بوچا در استان کیف، پس از حمله پهپادی روسیه در شب گذشته نشان می‌دهد.
🔴
در نتیجه انفجارهای ثانویه، ۳۷ نفر کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144457" target="_blank">📅 21:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c151b7af.mp4?token=lf5ZSAVNRIKue8tFQ_7H-ijNq3gJXB6-glajy7r07adMruYgk3WgGwirraI5KQ2xl77_noVXo6Rk1LvLTsZyKNvrcbregtpbdBa9tAnDFD31hx-ZALXNNIXzCum-SI8eqeelyMzIjZJ-c2QfY1VeUGFO14bq4gRWV-I9DBJCvTqoplEI8O1nOLPrmYTmI4SCXZweJl9RWaIU6IUAtTbwA3GtrGfBC_HTHaOJzP_evFIlhgpRWBFamQvs9SyH1ewCht56Z8phsTQCEJEesiWA3WPAd45vwFeC4hNVjDUPsjjMyasOuPxMvEpopGiG7KBLvnmrSmKzE9okfgLR5iCm3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c151b7af.mp4?token=lf5ZSAVNRIKue8tFQ_7H-ijNq3gJXB6-glajy7r07adMruYgk3WgGwirraI5KQ2xl77_noVXo6Rk1LvLTsZyKNvrcbregtpbdBa9tAnDFD31hx-ZALXNNIXzCum-SI8eqeelyMzIjZJ-c2QfY1VeUGFO14bq4gRWV-I9DBJCvTqoplEI8O1nOLPrmYTmI4SCXZweJl9RWaIU6IUAtTbwA3GtrGfBC_HTHaOJzP_evFIlhgpRWBFamQvs9SyH1ewCht56Z8phsTQCEJEesiWA3WPAd45vwFeC4hNVjDUPsjjMyasOuPxMvEpopGiG7KBLvnmrSmKzE9okfgLR5iCm3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات عجیب رئیس ستاد امر به معروف: زباله‌گردی در معیارهای جهانی نشانه پیشرفت یک کشوره؛ کشور فقیر اصلا زباله نداره که کسی بره زباله بگرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144456" target="_blank">📅 21:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
عراقچی: ملت ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144455" target="_blank">📅 21:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f57eb5399.mp4?token=DxrNtiXVAGFihzUqh8JC4jqHXnHIGgSRVPVmJ3ft9ycN7_hH6ZSwH1hix1N8HJe2qjlo4OGIFCn6wS-oB8I-NB4gGDCQWSSeUMqNP8BLFrFDBDmXEkM-1wabbXttqbOghJ8OE-Kv9oI3eXFGsrxFERiS0yY5U4w0t49KtudAhkCGfQ4mml4UQPEK8aGWT3otjqXThGGBHUYSmKLKuceLGHCWS5jObf7v9Dd3Ij0YPzwOJY5RZDlZCqMmETcTicbiAsLTuGNujULG-STdXu2oCHxKl9KyiLgEm1AEpyR3gfuhecr4ViiPqMLaID-X34NS1jURqH-Qwld_itQmnB6r8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f57eb5399.mp4?token=DxrNtiXVAGFihzUqh8JC4jqHXnHIGgSRVPVmJ3ft9ycN7_hH6ZSwH1hix1N8HJe2qjlo4OGIFCn6wS-oB8I-NB4gGDCQWSSeUMqNP8BLFrFDBDmXEkM-1wabbXttqbOghJ8OE-Kv9oI3eXFGsrxFERiS0yY5U4w0t49KtudAhkCGfQ4mml4UQPEK8aGWT3otjqXThGGBHUYSmKLKuceLGHCWS5jObf7v9Dd3Ij0YPzwOJY5RZDlZCqMmETcTicbiAsLTuGNujULG-STdXu2oCHxKl9KyiLgEm1AEpyR3gfuhecr4ViiPqMLaID-X34NS1jURqH-Qwld_itQmnB6r8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داگ فورد، وزیر انتاریو کانادا، در واکنش به فرمان اجرایی رئیس‌جمهور ترامپ برای تغییر نام دریاچه به «دریاچه آمریکا»، یک تابلوی بزرگ با عنوان «دریاچه انتاریو» را در طول خط ساحلی رونمایی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144454" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9Lw2UGm297TwcQAkAIcCuJjVMiZFA9dHF51vwoXC92ikDok0txpDZBlNkmPuyZQZ0mbskWGEDseoewXzy52yfT4LVjL8iSQaT1thz91jTpsECwJ8AkYPOCu16E7EaUVDU1UL9pdYUbGGc3BgflJENMQBndpX5QTB2jFcE_O4kQ7fsSWqPT2cx3v7V1Rk5hI25yjUwOEVnCrQA5llr4xq_TjqCTNm4rV5quV_3YstpK85vywSaEuA-EMD5K7780VmPVnMH5TiN71HGKGLszfydkBqNX3xHC8UEmbpT-b-uEViMBL3iLBw3EMx0-G17wuWuy8VETd_Cf-RDRXk8QbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: من اعمال خشونت‌آمیز جنایتکارانه‌ای را که در روستاهای قصره و جلود توسط مشتی آشوبگر انجام شده است، به شدت محکوم می‌کنم
🔴
این آشوبگران قانون را نقض می‌کنند، بی‌عدالتی بزرگی را نسبت به جامعه یهودی قانون‌مدار ایجاد می‌کنند، در انجام ماموریت‌های ارتش اسرائیل دخالت می‌کنند و به جایگاه اسرائیل در جهان آسیب می‌رسانند.
🔴
نیروهای امنیتی به سرعت وارد عمل شدند، سه وسیله نقلیه را توقیف کردند و در مدت کوتاهی به این حادثه پایان دادند.
🔴
ارتش اسرائیل، سرویس امنیت داخلی اسرائیل و پلیس در حال انجام تحقیقات جدی در محل هستند و من انتظار دارم که مقامات انتظامی آشوبگران را در اسرع وقت دستگیر و به دست عدالت بسپارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144453" target="_blank">📅 21:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b35ada18.mp4?token=C3qK4bcZB5-bMQDmIW1p3WCAU4wSJ5CHY8a0MirHaYSwyBpfjISGI4__5sW-AkeOt-66E7uUbcT17SxWwbEbwiUtWhvBkrIVuk52eZPtHYGYIjNlbxyNdDcBGLELu5wGcSGKoMqnBUMTDHe19ni19yQ61U01vJS_gc4LfZISw8JUtLUibvPzL8EkagaJYm_PElSjxmpyAdhozLWw18WQIMmHeow5Q_EXvNcPz0AeWnZwl9vxxz_1B0FigxDQKol641j30q58rmNpAVZ5o_8XXCxaV3AR_KoGcxhMHZ6ih4mQJPQ8RvB44lUtd26w7QJuITp8mHouyVmcVuDfWZT3uQngKGp_GKgpxckAUnm7qiYqVnQ2sK31ctHViSjo5MnA_UH4imx-zqJRdFzYVabJLvBof20n6vSH5Xe7L2IWtHzpSpy-XR3ilRaXAIqFBcLpAGZP5XnVM3sxk52zoasc2rNjY8IYUxMxIM87vt3VLT1P8U7enhn5xjZuNkJ2cingQp8NYmqe_qBNcvbNS2PUjqp8xBbs7LkwZ8ce11ckHwlNr650mXia2W-3-uxKABjJkicLJvgcq3unFTgTxD_YTMZPY8_MW9ydgJ2kywR_3_RZL-B1PBqQyWTUUqYOZ69cXPUoPbIA8VpG6aYX6nP2vAhdI5YzIH_EbI-dag8AJMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b35ada18.mp4?token=C3qK4bcZB5-bMQDmIW1p3WCAU4wSJ5CHY8a0MirHaYSwyBpfjISGI4__5sW-AkeOt-66E7uUbcT17SxWwbEbwiUtWhvBkrIVuk52eZPtHYGYIjNlbxyNdDcBGLELu5wGcSGKoMqnBUMTDHe19ni19yQ61U01vJS_gc4LfZISw8JUtLUibvPzL8EkagaJYm_PElSjxmpyAdhozLWw18WQIMmHeow5Q_EXvNcPz0AeWnZwl9vxxz_1B0FigxDQKol641j30q58rmNpAVZ5o_8XXCxaV3AR_KoGcxhMHZ6ih4mQJPQ8RvB44lUtd26w7QJuITp8mHouyVmcVuDfWZT3uQngKGp_GKgpxckAUnm7qiYqVnQ2sK31ctHViSjo5MnA_UH4imx-zqJRdFzYVabJLvBof20n6vSH5Xe7L2IWtHzpSpy-XR3ilRaXAIqFBcLpAGZP5XnVM3sxk52zoasc2rNjY8IYUxMxIM87vt3VLT1P8U7enhn5xjZuNkJ2cingQp8NYmqe_qBNcvbNS2PUjqp8xBbs7LkwZ8ce11ckHwlNr650mXia2W-3-uxKABjJkicLJvgcq3unFTgTxD_YTMZPY8_MW9ydgJ2kywR_3_RZL-B1PBqQyWTUUqYOZ69cXPUoPbIA8VpG6aYX6nP2vAhdI5YzIH_EbI-dag8AJMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر جدید منتشر شده از اسکله رجایی در بندرعباس، بزرگ‌ترین بندر تجاری ایران، حاکی از توقف پهلوگیری کشتی‌های تجاری در این بندر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144452" target="_blank">📅 21:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4BVhWizfvztRB6BzXItgU3m5ly2qdsUVenmARf7plq4jtoiuMSMoZREDLj7vIgT38qYlWg561MU_gsHerVmdF0a7x-Kx12z-gk2_VNW-uIqhQjgxECsOjdH25mUDW6EKPs1MMPvy_XUiG1giabmT_T_EH9kJMSeWL-IO36CWvgzUPtzhfuI7QNjzQNK4GWcdAzvAEBlIl97okRk8AN4c59f1VvKPKBuIRFhojSTjlFCboxvcuHfS8TkNLgVAdXsIj2fNKCLL70AWBSkunNBJqJbz2a1gHrmt4SUu-HK-u1E8sXKUgs5HIxwGpHWgO8HNxjDlrH0yy8WlaMUbSxhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد زیردریایی اتمی آمریکا با کوه زیر آب؛ کانتیکت ۵ سال از رده خارج شد
🔴
زیردریایی یواس‌اس کانتیکت (USS Connecticut) از کلاس سی‌وولف نیروی دریایی ایالات متحده، در حادثه‌ای کم‌سابقه در جنوب دریای چین با یک کوه زیر آب که روی نقشه ثبت نشده بود، برخورد کرد.
🔴
این زیردریایی اتمی که یکی از سه فروند گران‌قیمت‌ترین و پیشرفته‌ترین زیردریایی‌های تهاجمی جهان محسوب می‌شود، پس از این تصادف برای یک دوره تعمیرات طولانی‌مدت به مدت حدود ۵ سال از خدمت خارج شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144451" target="_blank">📅 21:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144450">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
از الان به بعد مدارس روسیه آموزش نظامی اجباری را گسترش می‌دهند و به بچه های ۱۳ ساله در مورد مسلسل، نارنجک و سلاح‌های ضد تانک آموزش می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144450" target="_blank">📅 21:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144449">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گروسی: نیروگاه هسته‌ای زاپوریژیا ۱۰ روز دیگر وارد خاموشی کامل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144449" target="_blank">📅 21:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144448">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxUA8Pnd6U-czYfl1-wuGKa8g3v3VbC7aGtWl63c5B82LudtBxtQh25zS2yOpz86PV2rerVEL_A_8TgN2yId_7JGz5BXJ_zImMdEjLCfGGTD-fPuRcY_eViYYhSPpnI63FlKiHY4PorantxXVEHvj7OMnhqB5FUFShsr2SHeXdQZ1yqlaR0v2Gl1Jl2nfHn4kvY-uNqPSHuSxrUs3M35ggNLKSCR5ZjHLs2TTr58GqI4FGsS2CQq-XRQjjyE-jY79qSDogbC7hOxTTHMLjvTqz2YBSQf2MkdAPnF2SZarWVlRdnAmV40YGYpjIAhT9Rm_Xe3JTTthoHSUl_Oh2Queg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق جدیدترین تحقیقات تو سال ۲۰۲۶ بهترین کشورها برای زندگی زن ها و دختران از نظر رفاه، امنیت و آرامش روانی و اجتماعی : ۱-دانمارک ۲-ایسلند ۳- نروژ هستن
🔴
و بدترین کشورها : ۱-افغانستان  ۲-یمن ۳-آفریقا
🔴
ایران تو رتبه ۱۲۱ این نظرسنجی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144448" target="_blank">📅 21:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144447">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52c1cd1de9.mp4?token=lx7Pax85HIOKf0HtsT99TZsc8I9wQOSAIMkALm8NQT4DCSixA5IYS8lG9nIh74idnNehP5p1_O4Zd5rH2GzK7YdF1CxYF9Xo4WX54cgF87Art0SIMfTsQQyPfJDbAFSJ0U2qCgmg3m2_7sPE_jFJyFj1K9275JNu391X6dnE2qaFBq2bLclA8cJp5bXGP6l5g9yTNoWsHCEBUQ2Z5rgARLMUHIkGXFFuDzAhrJKfyx8rBZqNVMv8sGBv97qB1RLp_LLIXPPcCtli2ScrBybkZaot3oeKmETgvXq-QsgLlLfIda54XNoUIFqEjpvSJXBmSvGedJwzeVPGWHNI1SLFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52c1cd1de9.mp4?token=lx7Pax85HIOKf0HtsT99TZsc8I9wQOSAIMkALm8NQT4DCSixA5IYS8lG9nIh74idnNehP5p1_O4Zd5rH2GzK7YdF1CxYF9Xo4WX54cgF87Art0SIMfTsQQyPfJDbAFSJ0U2qCgmg3m2_7sPE_jFJyFj1K9275JNu391X6dnE2qaFBq2bLclA8cJp5bXGP6l5g9yTNoWsHCEBUQ2Z5rgARLMUHIkGXFFuDzAhrJKfyx8rBZqNVMv8sGBv97qB1RLp_LLIXPPcCtli2ScrBybkZaot3oeKmETgvXq-QsgLlLfIda54XNoUIFqEjpvSJXBmSvGedJwzeVPGWHNI1SLFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) می‌گوید حملات دیروز در شمال غزه دو نفر از مظنونان به عضویت در حماس را کشت، از جمله هانی عبدالهائى فخری مظلوم که به گفته آن‌ها فرمانده یک گروه در نیروی نخبه «نخبه» حماس است، و حسن زیدان حسن دییری، تیرانداز.
🔴
نیروی نظامی اسرائیل اعلام کردند که هر دو نفر همچنین در تأمین و قاچاق سلاح برای حماس نقش داشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144447" target="_blank">📅 20:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144446">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سیل‌های ویرانگر در نزدیکی مرز چین و نپال دست‌کم ۶۸۲ کشته بر جای گذاشته‌اند؛ از این میان ۷ نفر در سمت چین و ۶۷۵ نفر در نپال جان خود را از دست داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144446" target="_blank">📅 20:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144445">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMN5BW3BuSdWpc03GcgDlqtE0zLu98XchwmTacLSVG9GfqCMkTP2HnQFPshE4Y-Wt_5U8w-MO3EPr--oTLbljhDPzmvW3NQ56zELOcU1Ao9qAbDwQz2z3XAsSHP-4UyCLWibb32VjhKFLB0rB8IkEvXiCUIjGPZl-mY-ZSDs1AIDT1tvtEutIB-nRvSl8Q_SqPs4cu8W7nQNPALPxegrYLz8-ZNFFtPQ9B3n-QVa4N3IAnvbkAJ8sB20ubatVwRZL11pIbBrxyB0K5hVYpQWT3HFEAR1b9FM4IavExSHZvqRSiQLP5BulWiIwTcwi1IUXJL8ewvZcfUTQdtqbZrJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز شنبه هفتم شهریورماه تصاویری از تفنگداران دریایی آمریکا در حال سوخت‌رسانی به یک هواگرد «ام‌وی-۲۲ آسپری» در یک پایگاه هوایی در خاورمیانه منتشر کرد.
🔴
«ام‌وی-۲۲ آسپری» یک هواگرد نظامی با قابلیت برخاست و فرود عمودی است که برای جابه‌جایی سریع نیروها استفاده می‌شود. سوخت‌رسانی به این هواگرد در پایگاه‌های عملیاتی می‌تواند برد و مدت فعالیت واحدهای هوانوردی تفنگداران دریایی آمریکا را افزایش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144445" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144444">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9021f8047e.mp4?token=UaX81YT9YEWYvHphJuvXU27JyDLCfj_e5TA2GeqN3_ml15tAH7-V6DjSRQI9zfxE1-MeLrKY2l2OBCdSgy32fYBeK3NTBfD6u3DJRrAlXJ0Mt-G5yV4jkJNJmgqbQdVpbs8_do12WkLxmJxNU3N5G0hAsh71kOHhgaQbkgmFQifX5-SKTQt3ORxuBYUTpD5bbqvLBOCGvTmZfKccZMjJxKNQxvin1ZVdTitV9XRrOfJvprVCmgOHrJhHacc5LHaTQkhUTZIDdBk0cUJr-tDQb7joTK0Q0S592mopQRah8YTUm_5v_0o0pq_pIUNIwr0qRvTRliuaNIW3QWtXJPghEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9021f8047e.mp4?token=UaX81YT9YEWYvHphJuvXU27JyDLCfj_e5TA2GeqN3_ml15tAH7-V6DjSRQI9zfxE1-MeLrKY2l2OBCdSgy32fYBeK3NTBfD6u3DJRrAlXJ0Mt-G5yV4jkJNJmgqbQdVpbs8_do12WkLxmJxNU3N5G0hAsh71kOHhgaQbkgmFQifX5-SKTQt3ORxuBYUTpD5bbqvLBOCGvTmZfKccZMjJxKNQxvin1ZVdTitV9XRrOfJvprVCmgOHrJhHacc5LHaTQkhUTZIDdBk0cUJr-tDQb7joTK0Q0S592mopQRah8YTUm_5v_0o0pq_pIUNIwr0qRvTRliuaNIW3QWtXJPghEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صادق الحسینی، اقتصاددان، مدعی شد: کیفیت بنزین به حدی پایین آمده است که موتور خودروها تا ۳ یا ۴ ماه آینده خراب می‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144444" target="_blank">📅 20:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دولینگو (معروفترین برنامه آموزش زبان جهان) اعلام کرد آزمون‌های این برنامه از ۱ سپتامبر (۱۰ شهریور) برای ایرانیا متوقف خواهد شد و دیگه از ایرانیا آزمون نمیگیره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144443" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144442">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47148daf34.mp4?token=J5f0kOkrCKUnGPoWt1BEj3eOObfidO-Gt3_h1tUtWK5ncwIK2cGuTyydJkNHwCjWgE50msHUj3vWM6YLBQZrvE84bPN8DsnuRATdUMa2DarFLVFglwN8ZVUBlFCp5Nj2J2WaqJGny73jCwLA8G5jI5aIRiDEsj41lF_KAX-UA3fBhYOcecj7TwAwzwZWfFo5O74Hc20u85unDWxpAcHzSFtMyGdjSSYdLjYbBKIv3Dxt1yrFZGc7J3OqknSkxLqo1XfKft8UA_OSdscjSa-ObTQOPTJhGtjeEI5HkvRXuVpsDLE_KJn_uqCmTGD8Q-nUovqLHG0gjyrlRRg6nns-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47148daf34.mp4?token=J5f0kOkrCKUnGPoWt1BEj3eOObfidO-Gt3_h1tUtWK5ncwIK2cGuTyydJkNHwCjWgE50msHUj3vWM6YLBQZrvE84bPN8DsnuRATdUMa2DarFLVFglwN8ZVUBlFCp5Nj2J2WaqJGny73jCwLA8G5jI5aIRiDEsj41lF_KAX-UA3fBhYOcecj7TwAwzwZWfFo5O74Hc20u85unDWxpAcHzSFtMyGdjSSYdLjYbBKIv3Dxt1yrFZGc7J3OqknSkxLqo1XfKft8UA_OSdscjSa-ObTQOPTJhGtjeEI5HkvRXuVpsDLE_KJn_uqCmTGD8Q-nUovqLHG0gjyrlRRg6nns-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک بمب‌افکن روسیه در پایگاه هوایی انگلس هدف قرار گرفت
🔴
یک بمب‌افکن راهبردی روسیه از نوع
تو-۹۵ ام‌اس
در پایگاه هوایی انگلس-۲ در منطقه ساراتوف هدف قرار گرفت.
🔴
این پایگاه یکی از مراکز اصلی روسیه برای شلیک موشک‌های کروز به سمت اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144442" target="_blank">📅 20:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144441">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: هیچ چیز به اندازه احتمال ادامه حمل و نقل دریایی هدایت‌شده توسط آمریکا از طریق تنگه هرمز، به اهرم فشار ایران آسیب نمی‌رساند. اگر این امر ادامه یابد، اوضاع را تغییر خواهد داد. اگر چنین شود، اوضاع بسیار بد خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144441" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144440">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اردوغان: مشکل ایران و آمریکا راه حل نظامی نداره و باید فورا برگردن به میز مذاکره
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144440" target="_blank">📅 20:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144439">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144439" target="_blank">📅 20:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=VaDpAP7uEMi3tKAvCV7fWOnQAVoSFII0sBWq-8qMIPVG_gBN3IYRwKwxkpxpLXWKE5-_QvZLyV4RmjxvEHNs-D6qS9VkX0oGg6m8UiC_TpLtLVWACoePkFyO70MW2ixy0RARfD1d3U2sIy4BKyzx1JS-ut1-6_6xr0_1JZcf3-OZQ9BV_RNlR6fbwb3EUHvLN2bwa_MTmvuMxohAU9-mf5mr2A95hbgvSqk-3z23GrIlsUXTGTrdFwdRltkhqFlIhhHrLLeanZHt85JErmEOMRK9qmjBaES2SCMKOPMqdi5tolr24_axWVziPrhReLn0_4CQyqG-Mj5coukGhhBBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=VaDpAP7uEMi3tKAvCV7fWOnQAVoSFII0sBWq-8qMIPVG_gBN3IYRwKwxkpxpLXWKE5-_QvZLyV4RmjxvEHNs-D6qS9VkX0oGg6m8UiC_TpLtLVWACoePkFyO70MW2ixy0RARfD1d3U2sIy4BKyzx1JS-ut1-6_6xr0_1JZcf3-OZQ9BV_RNlR6fbwb3EUHvLN2bwa_MTmvuMxohAU9-mf5mr2A95hbgvSqk-3z23GrIlsUXTGTrdFwdRltkhqFlIhhHrLLeanZHt85JErmEOMRK9qmjBaES2SCMKOPMqdi5tolr24_axWVziPrhReLn0_4CQyqG-Mj5coukGhhBBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظات اولیه حمله به انبارهای نفت تهران در جنگ ۴۰ روزه
🔴
‌️انتشار برای نخستین بار
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/144438" target="_blank">📅 20:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گفت‌وگوی وزیران خارجه قطر و ترکیه درباره کاهش تنش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/144437" target="_blank">📅 19:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu2gyGX2Ql7v6Pkn5mNH0NN-fa79gvyh74U8VLTSbfr5RQs0U9Tph4QxG552sQmq-Ag7aEfQi4NNxcCvjEzWfv7YdrB6gRlKG2Fadibdozp4qZXAoo-BBj8lcLoV-KciUQfhSagi2K4JQLo5chSTPUebkvzsq9Nm4MjsdKDrwULYZ22P-JS11T6g_rJ2Jas2pVsuUdmIG2GdmKuurnhq3cwA7j0vuXCzVBCQP4MokKdV7mb8K8XolsfDhrjtRyuqZCglU1p-0maagxl0_002RxvSz6fkJ_RRMPnwOgUeVr2pUw7HJs-U_rwSzUR3w8EKQKv7UJhhEfHGK5tgPqv7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات توپخانه‌ای اسرائیل به جنوب نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144436" target="_blank">📅 19:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY0BBd1wUwlEnLmKb8J1KewcNDqYqHzsmNN4PT3Qd5HQn5xyw2kMNeRJayIygiYxis07M-hcKUxw___GZsDiPOiK7iXs46z34EFX3aaPnnKcJArVuvMTGfyL8pUMyUk_w7pmcbdUsrw8k3QIReqNGrD4Q3wT9kAgoj9BbmWPOdB5JU_WcxCuGIybWc9ovD_u4lgqEEk1xuHJLCXw9r00j_fzb6QN6_jqNQLRHj6J7rVw7UR1QclHKtEAAnIGMW70EbnN-5pmrJN8o098i7SEN3XFtcI7muq55rHlKM_j7TQrHhlhfsY3D6c0u_XckFr9w6cyR8V0YpWamTickVYy0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف خطاب به اسکات بسنت: دروغگو، دروغگو، شلوارت در حال سوختن است.
🔴
در واقعیتِ ۱۳۰ میلیاردی، به دستیار خود بگو گزارش مودیز را که هزینه‌های جنگ بیش از ۱۳۰ میلیارد دلار را نشان می‌دهد، بیرون بیاورد و از دیگری بپرس که جین استریت چقدر در یک دوره معاملات آتی برای شما با فروش کوتاه نفت بیش از ۱۳۰ میلیون دلار ضرر کرده است.
🔴
دروغگو، دروغگو، بازدهی‌ها در حال سوختن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144435" target="_blank">📅 19:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الاخبار: ارتش لبنان قصد رویارویی با حزب‌الله را ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/144434" target="_blank">📅 19:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59c74d913.mp4?token=hXwvnZkZQDTcHmU8xkGymAnZRvPOcNxGKc1Abn21AUlC66lorY-ARgkFL2kSn5HjCVUrde6LbVLefHNFZNAM1DbXOfy8QuYaX2jK0eC0V1dMkGcw_1KQwwgr7zfBAC0owqyB2uyTumTRBOdJR9vX_OVnGHWO9aawM_Iqiy_APsXGqp5YFijGA-NNwpQScQlhbQZaeGgi1TNB6AJ1d3TAeG8usf3dOLk_VLXg3Jr00w5jJvLgwhSVsRn61ItcpnNKEm-enmcphZu9Ql8DkyQLPEvG3FRMjBeqPJxcZa8-phr88EzTWNhLj_5RWw2PcrEMRWZiTtMIQ-GG7f0Qpbszcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59c74d913.mp4?token=hXwvnZkZQDTcHmU8xkGymAnZRvPOcNxGKc1Abn21AUlC66lorY-ARgkFL2kSn5HjCVUrde6LbVLefHNFZNAM1DbXOfy8QuYaX2jK0eC0V1dMkGcw_1KQwwgr7zfBAC0owqyB2uyTumTRBOdJR9vX_OVnGHWO9aawM_Iqiy_APsXGqp5YFijGA-NNwpQScQlhbQZaeGgi1TNB6AJ1d3TAeG8usf3dOLk_VLXg3Jr00w5jJvLgwhSVsRn61ItcpnNKEm-enmcphZu9Ql8DkyQLPEvG3FRMjBeqPJxcZa8-phr88EzTWNhLj_5RWw2PcrEMRWZiTtMIQ-GG7f0Qpbszcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر بهداشت ایالات متحده، آر.اف.کی جونیور: سربازان ما برای اولین بار در تاریخ، غذای باکیفیت دریافت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/144433" target="_blank">📅 19:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7t3KmcujNmaZt87_Z-tH93rztKU5TJ1Ab32CTv2F88cGeONMVKLG7fyqjiogmxlnjDgJI8PuXsWX0rtlTrXCY6-96fLzJ93Yp4iwBDUiHM0Qc2K9RmYiBxVetevPOvPxvLzSLeZ6_b8-yZGms_zGRtbaCOdDdavoyOOzVIuXxN6o5u9DDBntjvbHP6Futc986quqbCOKESt0l8tAyhuF1D2mEsv2lRiASVq85SprPc8Rv6C9nF4ar0ZKHTysPl-TjwGAAzTta9Ra76EFv297wMbKdlHs8eIeL58zN0zy8Gz8fihtGN_sTtAcatATWCBBV9m-k_6wMjewNL3m8VQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوشی نوکیا ساده که همیشه نماد ارزون ترین گوشی تو ایران بود به ۸ میلیون تومن رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144432" target="_blank">📅 19:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9238eeb8.mp4?token=axFkhfArKXdE_4QeflN1F69YsyFupJUi0mYo15Rpfw5GCDqcFo25zp79PJd8MWB2TlXZVdPrtk5QNQBnNLx09yEDiif_wo9r4_VmgQQxIUhZzHE8Vq5BoUHz1FGihZtYXGoPrqwX-6uwXQwLsvHu6Oa0hOhtcRXnPl5y5zWnKKYmGPHjKhi6ae656W1hX1-t7xqkeTPizePe0tvjHOmDCg3Vg_r_iQ1VuPu3fEgBF86cghQnU3mMSIL5cLAK2pHnI214o73GOEcpga7i3turzdFK6BgoNdQaesv-CyajOrlf05ApCTsyGWPCmeh_7kdQnXdFzYxs8m7VYQs1KftSGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9238eeb8.mp4?token=axFkhfArKXdE_4QeflN1F69YsyFupJUi0mYo15Rpfw5GCDqcFo25zp79PJd8MWB2TlXZVdPrtk5QNQBnNLx09yEDiif_wo9r4_VmgQQxIUhZzHE8Vq5BoUHz1FGihZtYXGoPrqwX-6uwXQwLsvHu6Oa0hOhtcRXnPl5y5zWnKKYmGPHjKhi6ae656W1hX1-t7xqkeTPizePe0tvjHOmDCg3Vg_r_iQ1VuPu3fEgBF86cghQnU3mMSIL5cLAK2pHnI214o73GOEcpga7i3turzdFK6BgoNdQaesv-CyajOrlf05ApCTsyGWPCmeh_7kdQnXdFzYxs8m7VYQs1KftSGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در تروث سوشال درباره دریاچه مشترک با کانادا: دریاچه آمریکا، محافظت‌شده توسط اردک‌های دونالد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144431" target="_blank">📅 19:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d8cf7ba8.mp4?token=hdPJpd625GC-90R-eF1tlbQChCXjO8sii_v8_H08bardOONdt_QNZLKKdd7YShn2wHqxcbYDp7Cct0Shlmy_OlOZMbhj4qmjN5R3z9DAPTADtz3EvpOHaqdrab9E-I4XeftWQexkLbDt3Rk8AUDxIRsOwT5tEdhf93G_a7hWhzreSrKRtKcqsGt7zfC34jRy0MNxnRP5_rWJB4uWwtVDm4Bv_KjeFZ7Qfi-fSqKPSrj5mTD0mFt4qOskhXiN7q6OJ-UUDye3W6gjan-JvlmvEKBceCs25rGJpFcS7NwXsd7PYcQ8NLYMm-4_C402I4CPuf-cJ0s3_qLNtqVJ-26SBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d8cf7ba8.mp4?token=hdPJpd625GC-90R-eF1tlbQChCXjO8sii_v8_H08bardOONdt_QNZLKKdd7YShn2wHqxcbYDp7Cct0Shlmy_OlOZMbhj4qmjN5R3z9DAPTADtz3EvpOHaqdrab9E-I4XeftWQexkLbDt3Rk8AUDxIRsOwT5tEdhf93G_a7hWhzreSrKRtKcqsGt7zfC34jRy0MNxnRP5_rWJB4uWwtVDm4Bv_KjeFZ7Qfi-fSqKPSrj5mTD0mFt4qOskhXiN7q6OJ-UUDye3W6gjan-JvlmvEKBceCs25rGJpFcS7NwXsd7PYcQ8NLYMm-4_C402I4CPuf-cJ0s3_qLNtqVJ-26SBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه چترکوت در استان مادھیا پرادش در هند نشان می‌دهد که آب‌های سیلاب تا ارتفاع نزدیک به یک ساختمان یک طبقه بالا آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/144430" target="_blank">📅 19:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
استیون میلر، مشاور کاخ سفید: تنگه هرمز برای ایالات متحده باز و برای ایران بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/144429" target="_blank">📅 19:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ea5004bf.mp4?token=jZ03K8hcWFN0_3Pa6otM_vrO14XnyNupdoEGv11uSWRaf2HyxoqMm82Ojr4jg6sSN_hGpJoz2N1hLjxFtJ8stKTltTXKukeu5LtmAb7Ifx_n9dIR4cbZr_wEUhgIkX2PW_Phh9wCF9Gf1TAtsUmZJLk5OMbshT40wd3wzZIbwgSnLr_LkWAJqw9JYHkIJwBDPQP_G7PFKW4hwgWR3pm-rQLjhBpXuuaEj7Zr34ixgw__QF5ZjY2iubTsVO7uvbPxzKn3DGTEaGSEeH_RtUqnFWaLlCX2d0pE63yZAUUrlcARX0wLnH7-R0YIUjQtdVsk1Xly2nmSi_QEHWyL9CQ88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ea5004bf.mp4?token=jZ03K8hcWFN0_3Pa6otM_vrO14XnyNupdoEGv11uSWRaf2HyxoqMm82Ojr4jg6sSN_hGpJoz2N1hLjxFtJ8stKTltTXKukeu5LtmAb7Ifx_n9dIR4cbZr_wEUhgIkX2PW_Phh9wCF9Gf1TAtsUmZJLk5OMbshT40wd3wzZIbwgSnLr_LkWAJqw9JYHkIJwBDPQP_G7PFKW4hwgWR3pm-rQLjhBpXuuaEj7Zr34ixgw__QF5ZjY2iubTsVO7uvbPxzKn3DGTEaGSEeH_RtUqnFWaLlCX2d0pE63yZAUUrlcARX0wLnH7-R0YIUjQtdVsk1Xly2nmSi_QEHWyL9CQ88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصویری جدید از ورود وحشتناک سیل در نپال
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/144428" target="_blank">📅 18:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
الجزیره: قیمت بنزین ترامپ را تحت فشار قرار داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144427" target="_blank">📅 18:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144426">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اقلیم کردستان عراق: شرکت‌های نفتی پس از اختلالات ناشی از حملات پهپادی، فعالیت و تولید را از سر گرفته‌اند
🔴
قائم‌مقام وزیر منابع طبیعی اقلیم کردستان عراق روز شنبه به رسانه‌های محلی گفت تولید نفت در این اقلیم از سر گرفته شده و اکنون بین ۲۲۰ هزار تا ۲۳۰ هزار بشکه در روز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144426" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144425">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کرملین: در حال حاضر هیچ زمینه‌ای برای بهبود روابط بین روسیه و اتحادیه اروپا وجود ندارد.
🔴
اروپایی‌ها به طور کامل منابع نظامی خود را علیه فدراسیون روسیه بسیج کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144425" target="_blank">📅 18:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144422">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqHAZGIuKShZbFpkarzj6EYec6qH-a--oMYBTZW0vKNJB-B1I2ZakxLp2aCE_jEoduKBvPrgmgK2m-oEFvztsNfvisDc5DIJvSNkqyhtiuxJ2ik5SnD2n-c4qEYaBw7qgDbal7Drgze5fjDK9AEFJwCJ3M1tDRYxBb0MvkD7pM9f0GwvpoaELeL7prgazeX2Veg7YsynszPtoZ4hrGfRHaZkXz6z7FucRpMbar5Lzl0rb_uFsZou82QYO_1aIQOGgUt_BzmtIX-Mkc1x0qLBKxMqV7dJJd4hoi-tFuKwV76I67GczwXGtSD-ZC61tv1dhWrWIGreN9m6CPdkM81YUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGn1BIpsU9WcsWrFbLZyLCZZYum95S19YAPG06zkl5grSS7vNPvBB0593qbxby7s4NesUP-Hp7pqpTKgSwEyNdrmVp3sEC4-4VW34RYpTjLMxImSr1sejt2AIbrokeuC2CB_Q7yrUAoBKbFkXS57Op2SmC3A1yloZTsv0it7y8cfFKBtt4BafVsZG-BDjLSegvQZu6AkYH11DWbEEzfxIRzDuCsZ6W7rYYV2WxEu5_Br4p0mA64MnY8Sihs0SE3kgWUgaZZkPxKFM_9KtXG3Fd9ocDj33z_YOK8-P-s1jAuG_GX31ZDSSoS57mWYZu65k2ZWYlF1Dt85WFYT-yBjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g31TNxkllOAleHnHeGeBWLmZ8Y9Y5FOk4FF6z05Dh6fGOsValmAhbHZ1D73Mu6G_pakD0eAWT0xm9fwDL9fUk5pPuqdllW5cRD80Hixl01u868DDAqL3A-XONsGZJBEgl-Ojk7PbHFylFdfqZQbAhInhwpR3Wpv6qGVJZW-_H5SnOUNxuhAmH5H17kjPqO9HR5MhfRxKLkibInvI0UU4k-UwDtUvW2hRx3b7db7J2S0yipN6lQxd_PFi2dljBRcYwykkkwDleLXEZlJYuAvSw5ZizE-Zrh0bNnetT65AKwoD98F5HPgXbTgoNMtQU4naaSfJnX2WjpEgZJkD7YoTxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون جت های اسرائیلی در حال بمباران جنوب لبنان می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/144422" target="_blank">📅 18:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144421">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
۳۷ نفر در حمله روسیه به کی‌یف کشته شدند؛ اوکراین نیز به کریمه حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144421" target="_blank">📅 18:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144420">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ، به سی‌ان‌ان و ام‌اس‌ان‌بی‌سی حمله می‌کند و هر دو شبکه را «مارپیچ مرگ» می‌نامد و می‌گوید «واقعاً، هیچ‌کس به هیچ‌کدام از این دو شبکه نگاه نمی‌کند».
🔴
ترامپ از تحلیلگر نظرسنجی سی‌ان‌ان، هری انتن، تعریف کرد و گفت که او نباید اخراج شود، پس از ارائه نظرسنجی‌هایی که نشان می‌داد ترامپ «شش برابر محبوب‌تر» از آبراهام لینکلن، جورج واشینگتن یا هر رئیس‌جمهور دیگری است.
🔴
ترامپ گفت که سی‌ان‌ان می‌تواند از طریق «رهبری و مجریان جدید» احیا شود، در حالی که استدلال کرد که ام‌اس‌ان‌بی‌سی نمی‌تواند به همین شکل نجات یابد، زیرا «یک برند بزرگ هرگز واقعاً نابود نمی‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144420" target="_blank">📅 18:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فارس: ترامپ رو تحت فشار گذاشتیم و درحال پیروزی مجدد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/144419" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144418">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06639a95d.mp4?token=S_1vrnHJKjFIHiZ2UPKA6w2_EMbB8JQPpQnCfkg4fgRDaqFsfHOgKzk2iRolYeUse9AGTynktZ4xloVnRtVqg166xX53T-FxnVyf1V0y_HJpItB8KNddT9vcOmkZCstV3sZqzt6vJgRl166UvPWHlTo6G8WzfjRY7CqwvtfHxENCzVyHCWbdaMMf1I9VoY99-YKUKW0MEgYwH2R_i5iVqIxFptptUbKogoXVJrIF_hEgQSedanJXDHhNyOz97wi7OiWDZbYpsTsj89q8QcCa32zQsUdaO-ygIW_EBzyMy_mGMs9tiTuQZDKoTBRTGgZ1-t9csarqKgtC6pwtwY5nzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06639a95d.mp4?token=S_1vrnHJKjFIHiZ2UPKA6w2_EMbB8JQPpQnCfkg4fgRDaqFsfHOgKzk2iRolYeUse9AGTynktZ4xloVnRtVqg166xX53T-FxnVyf1V0y_HJpItB8KNddT9vcOmkZCstV3sZqzt6vJgRl166UvPWHlTo6G8WzfjRY7CqwvtfHxENCzVyHCWbdaMMf1I9VoY99-YKUKW0MEgYwH2R_i5iVqIxFptptUbKogoXVJrIF_hEgQSedanJXDHhNyOz97wi7OiWDZbYpsTsj89q8QcCa32zQsUdaO-ygIW_EBzyMy_mGMs9tiTuQZDKoTBRTGgZ1-t9csarqKgtC6pwtwY5nzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون وقوع سیلاب شدید در شهرستان راز خراسان شمالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/144418" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144415">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/al9AUkibZN1uNZODE_kmHyX8SIjMZ6J2TDGdbHG744dp-KqvzoXF3BerYZncpvjtDXCKJcpd76THxBojfLetrvJWHDIKUEnqGt4SuVduuwm5iMydob-if2tM8R2lktUhUOUjCBm3kpTpsSn-EsiVkf9Upg-x-uJ3sT5woV9-iQYrCxLxvoGkO5BzruXi6fIQAi6SmGJmaBpl0wgo9liF4-DIzxI0S4au0IoPPYU4QG-VSBU59sCcHuR0ntvbdY1iPA0r36f09siI3ZRh1-zu_NTh0qmA8Rr_WnC2y-jj6GpXSEml83qpLOoxZv4B6HlsDKp0MQ_pHi-7TRilOVBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0zxoyA1GnYTmfqDkN1pLrC0DVO41CGnkRcRorNzSVHT3MyAVs0H3Q7Mk39WgZNHFKin78DElyaAiyCrd47za6nSBkt0egbWLdr-Or_nGfeC_z_9Jk_m7xuyZIpyqSW5Sj-c1xrWHTI1J0r5EEB7zpnrzB92GD1kq8TTG88MSkHMpOw2kGdTrScdwDZQfTEzR1bGs8RHR6JQ932h4xhz4YIVpbIAgYexIUwmc0Sug650nr0MD7-GRSOGxUGio-rRDxglPdPKjS1zsV5JRjJHo-2hQqRcanazlITkds3rESLTA46c-jcNTN_Byo-7c1ZGFOl1nMUuwKUTVYsZddtgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWiARiHB_Y8w5pAiIm5kUYwTzDK7tjI7OfULTH-9ST4FxM8GVk5hTsB-DYooPOQ_f6cLuy6Z09oQ_8x74enIXNphGqQoafor6-ULGxhLGUvRTqCjDc5CxxOrUSFDH5J5wA_2VG3aCfYVquNuU3sr3eWlGvk_M1ctD3ZYazVNf6c5JR8-CCbkh5NF2w6_0BR7G1Acziqk8ho6JiDVwY2vD1nCPmrwnzFLg7AQcqdV2EjXEQVSMJYKmcUcSqQaIvCPZfNflLoZHtnr_KpCcPDM9316Uab6NB4rnWHFDnGnjH_fIVKD1AIInXD3dRMUuSuFwdKmYZ1nb55vG29MGty3vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر از حملات هوایی اسرائیل که علی الطاهر را در جنوب لبنان هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144415" target="_blank">📅 17:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144414">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏
👈
هم اکنون قیمت دلار به ۲۰۷ هزارتومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/144414" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144413">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK8mbCnV5efNwGuoPhw50-iWsM57k2MS3mh3QRfYRHSheBHyNa-bApM60s95i47otOM6OC9wd0sNGlFsxnJnd2F6lxsPOyfMG0RlEfX2Km7w99s5TKgqEt7qihxFm_FBAKpNcM724ZV4_zGXMwQnGtxfk5rGIlZm30P3ZVL6nStFd_7qNCkGrfDW4le9j7iJ7vih7KrBGHhA8D35_UWfXJb-7_mGPjXrXVHZa6oOR7bET1xI6MKW2fsousegFFcquKGVf64dq-zVuYbd-SWZK8vyrJtKaUEA7dy0lywZdEUhTgP3D6wwYi3uyy1VsQk5SEajVsmbDDqIc7USMKU7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ترامپ، مقاله‌ای از روزنامه نیویورک پست با عنوان "ترامپ در جنگ با ایران پیروز می‌شود - بر سر راه خود بمانید" را دوباره منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/144413" target="_blank">📅 17:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144412">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9n-RgGA2vRhC-riyTDpZHjYmUGmeBm4wKiUVRPI6Yon4z7RE4mUOKCqNj2STFhDeOZpq9TQgjL7hHlX_sGJB17yEsIxlFlDz0PAdNGQ9qnQu-d4-MB0TS_mhka7Hiu8GOgIYyVV95z182BKCHlMdWOo1uWWUsZHBeLeNMN8QbjcQFzZmHVcV1XpFM2ywAaPuux4hCm6mE_PQM6x4DeTBronct_dg7j76uZpW-00LHUnMeTi7Qb30DyDWyaKw50cZEgnuOM49bMl9WDM6JF41mJ77Eu6aC8cjMv3fwQDCvc0vIZjrhl9ubEJFWMQdnfzRL5kqbm62OSN1mCSAVdi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: هیچ چیز به اندازه احتمال ادامه حمل و نقل دریایی هدایت‌شده توسط آمریکا از طریق تنگه هرمز، به اهرم فشار ایران آسیب نمی‌رساند.
🔴
اگر این امر ادامه یابد، اوضاع را تغییر خواهد داد. اگر چنین شود، اوضاع بسیار بد خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/144412" target="_blank">📅 17:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144411">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead0270f87.mp4?token=Ys-FeRhm6VHjCQ7h9F5PJ5gnpIt45o83SqpTa-lHfbnb0GLg5RNlsJV4Qj6ivVutIHNS6NkS4ngDkowbW6ThO_msIY42sUcNKaC1cg0QnMvrBa8F0Rcnf4nyJKDJ3X9n4TPcwTuo5IQeU4nd7p5QM2AekFY7BRCQ2ev0FWouAV7LJzcDd7mtgZkTe19SnqlXTB-t2KSkP5a17qif1KAk3T8F59El4cu58XRkMO-WJtaJn8Fd0WGuvkMd_PRnpDn_FJxKRlqEg6ftH_Wj7JQxD7bY71SBZn8nAezUYM8eQxSIBSwadYqXXFgRsr2VRHdbNZIaOMTNkrB7vPk9C5MB3WLrntLMhxF-05vCvLcDM-5yLp2_XLxlrtCpWMM0yCjyGnXRg6pAG8-p0BcrNcOtua6DXulL4E7uL7THMLChwIXW2fs5IqkGSRDOOqM92VqwXVTMS5xXhkh9kMkVKLFFD01xJ634ev8uhNndt04JXcnjCCm-keEiMEdCEtYFycYsP48oHdwp9n_LviPjd2InWmDSODzNWZybJcOU8LFc5yCfCd0LjRBR_pj8lOxqAJ88UHl7cI7XxiDZTVEHbjM1jbbeU7e5U7Wzm8dR0h8O1Ly_8BRq-ei32ZOM51WNbLtnz9m8RDad9bgbaVWJrhafyHZbOZOFFqk5bKKXnmiLnXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead0270f87.mp4?token=Ys-FeRhm6VHjCQ7h9F5PJ5gnpIt45o83SqpTa-lHfbnb0GLg5RNlsJV4Qj6ivVutIHNS6NkS4ngDkowbW6ThO_msIY42sUcNKaC1cg0QnMvrBa8F0Rcnf4nyJKDJ3X9n4TPcwTuo5IQeU4nd7p5QM2AekFY7BRCQ2ev0FWouAV7LJzcDd7mtgZkTe19SnqlXTB-t2KSkP5a17qif1KAk3T8F59El4cu58XRkMO-WJtaJn8Fd0WGuvkMd_PRnpDn_FJxKRlqEg6ftH_Wj7JQxD7bY71SBZn8nAezUYM8eQxSIBSwadYqXXFgRsr2VRHdbNZIaOMTNkrB7vPk9C5MB3WLrntLMhxF-05vCvLcDM-5yLp2_XLxlrtCpWMM0yCjyGnXRg6pAG8-p0BcrNcOtua6DXulL4E7uL7THMLChwIXW2fs5IqkGSRDOOqM92VqwXVTMS5xXhkh9kMkVKLFFD01xJ634ev8uhNndt04JXcnjCCm-keEiMEdCEtYFycYsP48oHdwp9n_LviPjd2InWmDSODzNWZybJcOU8LFc5yCfCd0LjRBR_pj8lOxqAJ88UHl7cI7XxiDZTVEHbjM1jbbeU7e5U7Wzm8dR0h8O1Ly_8BRq-ei32ZOM51WNbLtnz9m8RDad9bgbaVWJrhafyHZbOZOFFqk5bKKXnmiLnXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
آذر منصوری: پزشکیان گفته نه تنها استعفا نمی‌دهم بلکه برای انتخابات ریاست‌جمهوری بعدی هم هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/144411" target="_blank">📅 17:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144410">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brLjXQCDU7PNJzz79kFHxe6JvfE1shZFqGmSEHKfAZCovWSwUShaqsU4wfUEoGg8Rje77BiPOTT5MxX6c2lhdrKiPsjWMnzN1dJ5FlcyBE1RPAGL8THIS48UGv_taI6nSESUieKqVEb318zTeIrjRGFIATR6oXRiCrUHUdMFaPtegO-9Xg4pecbeeV414V7waIq0mvD_uLga3yfFMrp31bFKzxwOaa0cuDPEeNJMJG8KPuvmrA9zXXTPwwaSD5qAYwkoKGmUzAtj6zH6FgcsFTQBCKd8VTnBBLfGoio0wYFCg-t5hYe2ZlFOnneo-KL_Iau1dDTJQD7TkviY-_2ADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری آناتولی: استفاده گسترده از تسلیحات پیشرفته در جنگ علیه ایران، ذخایر نظامی آمریکا را به‌شدت کاهش داده است
🔴
امروز توان واشنگتن برای بازدارندگی در برابر تهدیدهای چین و روسیه محدود شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/144410" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144409">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5cf7bf87.mp4?token=th0r3PjCDGWq_RR5d3JOkTHhW03RU8cLXrz6LeN0DMj898DGZC9C5pjlejk_PD7liREbRm1wf1h4Q48DDE3NzKP8X2DPZk7KqS7xnS7ow5CcL9IYt3ex5FPkrQ2ST_cQ47f8pckwyA6T7KqNgr9q6exzwQq2KXUuDbN2zVysLRzAcx7Xq5nkqiKZOfxzlRtGNPW9Gvqr4MK8yxiwxWqDZ0_0QclEwQ_ie0lbCb9lWc5ZxED18e1TbPLAjIj_WSF_qO6w2a7x5imNA3Pbh7coJ7UFa-fVlbj_MyvuALy8sVKNjIPb7XKXQiSCOA5Pf74wA3IcTIe65lN40QSQ2VC1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5cf7bf87.mp4?token=th0r3PjCDGWq_RR5d3JOkTHhW03RU8cLXrz6LeN0DMj898DGZC9C5pjlejk_PD7liREbRm1wf1h4Q48DDE3NzKP8X2DPZk7KqS7xnS7ow5CcL9IYt3ex5FPkrQ2ST_cQ47f8pckwyA6T7KqNgr9q6exzwQq2KXUuDbN2zVysLRzAcx7Xq5nkqiKZOfxzlRtGNPW9Gvqr4MK8yxiwxWqDZ0_0QclEwQ_ie0lbCb9lWc5ZxED18e1TbPLAjIj_WSF_qO6w2a7x5imNA3Pbh7coJ7UFa-fVlbj_MyvuALy8sVKNjIPb7XKXQiSCOA5Pf74wA3IcTIe65lN40QSQ2VC1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای معاون سیاسی سپاه: امروز در دنیا قضاوت و تصویر ایران قوی و مقتدر مطرح است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144409" target="_blank">📅 16:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144408">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نبویان نماینده۲درصدی مجلس:
اقا مجتبی در صحت و سلامت کامل درحال جلو بردن امور کشوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/144408" target="_blank">📅 16:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144407">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akQ00APMjacJbtcPkT4SvDIGE_swQCSAh4TavjravgXvjpFGCmmnARkIE5bbLvSAjhch2ons-8NJQDrMEhZxX1WKLRue3FL_A-6ezeYlHwwVr1hn0R5uO6WFgP9KFHFhdCqEcro0mCQuFnWVCJn-UutkdcBcPSU1IIyAWhTvjSCNMrjd4xg_sf38GFEL9E0AREbnLG1WutvBzpxWfoX25wZFZ-1s6o08HHn09KwEylDyzPRv0vDursz6IIKG1v69q-m8fqjJRAJYLLqGb51-4Dqin59JXrBGxJ66krmu1t6mhRCcT9_DWV86tZ8kdB44sKCDeQG4vli_66QH3LvSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه ساعاتی پیش تو
فهرج کرمان
، یه پسر ۱۰ ساله از سر شوخی اسلحه‌ی شکاری پدرش رو میگیره و به سمت خواهرش شلیک میکنه؛ که متاسفانه تیر مستقیما به
سر
خواهر ۱۸ سالش برخورد میکنه و در جا فوت میشه.
پلیس‌ها هم بعد چند ساعت اومدن پسره رو بردن، اما پسره به حدی تو شوک فرو رفته که بعد از چند ساعت از این حادثه هنوز نتونسته یک کلمه حرف بزنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144407" target="_blank">📅 16:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=M-ofeMxjm9hPbSfj-UGpdk-LwL81dNgyyKA635CNbRecmPMsYPeLnogoftgB5hVS_3GGNp3hnlPGo4TwA0MJ2v595WRH55A76Z15ds43OK4BJk3FoSU2-3N9oRebGjF6OTvRzgAbbxiuIu7SbvJfw5freWbe3lqtmSvLQitNllc6g9EvCjp1QmxJCCrLeVbo6pK0noDa3W9toCiSBzdP0IwOoH_2r8ldPtvVOGGcKOcFm4C1iMW2_yWt0BfGv6PEiEesb33FVz2FrtcLdape2kFDcslljk1oyiAaLTFb-BoDvH7u66CKMvr9JYae2MIreyF7wAvnGWfdOy-oN9e5Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=M-ofeMxjm9hPbSfj-UGpdk-LwL81dNgyyKA635CNbRecmPMsYPeLnogoftgB5hVS_3GGNp3hnlPGo4TwA0MJ2v595WRH55A76Z15ds43OK4BJk3FoSU2-3N9oRebGjF6OTvRzgAbbxiuIu7SbvJfw5freWbe3lqtmSvLQitNllc6g9EvCjp1QmxJCCrLeVbo6pK0noDa3W9toCiSBzdP0IwOoH_2r8ldPtvVOGGcKOcFm4C1iMW2_yWt0BfGv6PEiEesb33FVz2FrtcLdape2kFDcslljk1oyiAaLTFb-BoDvH7u66CKMvr9JYae2MIreyF7wAvnGWfdOy-oN9e5Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روزه توی باشگاه انقلاب تهران مسابقات و ایونت تنیس برگزار میشه که حسابی سر و صدا کرده:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144403" target="_blank">📅 16:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دلار منفجر شد
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144402" target="_blank">📅 16:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144398">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOvr3WJ2ObITEkuHc0LYoqOSTTRdhtiVvPvg0pXoA_MH99lyikrqCSGWBHWD4XOxbpIl_7I96hXISh6lWu3WGFnpvTP1ROcDfjdEIagEN7Uh8_yxNtxlKO6qKlPaYEwcwh-A8eUnRkuqJ2t97tyZW2MQuq500YaO3pwR0Vd2GdPeyu1_q3N6_e6hta2XhjqcoK47r30r-dWnS9BZnKrx869zXXdroCnVyEbaMZrMR4_jRo7PeZbuNtW7hw5mvVYhdTXlaxXm5_NuZN4gYJfq7TqiLLEEFSfxy2fdK4Gv-19dwJXZ-zBvQP0zmfoLLGey9S2M-4tb4DeufuxXGPd5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNOqyDiwydTwalYY81Y5tZoKrPKstwAGoZ9yd8mijaTNZVNjCqzH2SlvF1SKplHxZy64nwQEzjS0pH5MnbIHXeKpoMpyFOB12kTQJN2aFeFsIFKltxRk8ldk0Z8hdOE_NvG7PfbOrDvn8wMwwalFfnwL_WEh4sksnXcfdzO9XC2sGxp8zsmpKQHRfD2kpKf7esoEfO6Azp-NdTdqQDclAcE_VbT8Cpm2NQRpRKy18sNY8z3Pqkvp8S14KyYkByHfIaIldN_Ls-2GGeZwy8FNJq6SwxmbDz0tFLKxp9PVTLfObDoTsliyVqvkbiOVhpdwpZc0_nHRZxPeWCe-EPBMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZSvQZrz4OwykPFXvhRWC2smF3lsjNX5jABYTlmqwEtTXPOu9tQ_OukAwePjbSk6tK31eFjz3vMTa0JzYVvHwBrqOXUzyrlNxfzRKoaYPPuMyv_s4mY8pZzGR7nwg3eYNdCpF0NPFam4Yg3OFHzoBwd3mgz2erLaurTTe7RNLSChw9qWCjZna2o_cveR87WfEFhEoPEtoXWAxvuKRC3ZGY_yGNIPGJchXWNw8jGBNfcn_eQ8kGn78NAKtSvV5P9uZ7ODZbLK83XBTuuLGYdpe_3KYmiLiiPuGL1ddGfUE2EeZOoi5lLg4KfkMwdafpc-eYpLnoteof4dWROXFk2kBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQW2XCth3JxjD0fBADivz25grv_85yp5qRJYg_zUshsBIWxpj_9EDMP7sDoRBL_EaK5mK8NH0SUuuo-UebtVV6gJOoX8ocxEhkrb5C1nfxaCI1AuHqE8KLQixJOrSewpCGqn_NZjwIoq6DuPtne9TVA-LI_680dhEubBm_j4fCDVYfgVG4DsWiW-fYHXJU8vVrXQu9gUhwAnPlsdVD15KdtHfIQBCLGhaauKURm3_88JEWGM3OdJSNmA5DCRi_1gEkLKLFk8diP--YcDRdlr2-jPREOdplQgSPtog9bdumSctYcgRfFgSaA6Y7R4G6gbM3-GDo-rOYTEtVPUR5eENQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تجمع مالباختگان بورس برهان سهند شهرستان نقده درمقابل دادگستری کل استان آذربایجان غربی که بیش از۵سال هست منتظرماندن وهنوز به حق وحقوق خود نرسیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144398" target="_blank">📅 15:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144397">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p97OB23XQYAfB23ENwdiZkfW3iDtLfikACb2Tj_e31nlpKYsVdf0Nm44h_IjoDKyTu7lfub9FPVwuK2gA99i26XS_Gv6kCBk37k0XWjCRUXKx6kxGjhcDczC8Od1Yi4dB8i4hVN2BURylkaHwUhOyIMvKv0f9t3KOpw35be_QbWPMoEn3RwoA9ep3-pa1G32weypgEECUT55FyIC8Ix73gkuImJGSBYkmNSK9OhLoRX7HrSzTdTUZ2QR-HL8BEf1E2U7KoFMjGosBo1fzOudrVH3T_KqRJoDalAD0NfFvAGq5mdDebvo_K2n2InkPQUOE_7g4BbfCzG2aQy8JIB8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرف حق یوسف پزشکیان: ما باید هر کاری که برای تامین منافع مون لازمه انجام بدیم اگر منافع ما در غنی سازی است، دنبال کنیم. اگر نیست متوقف کنیم. اگر منافع ما در داشتن توان موشکی و پهپادی است دنبال کنیم اگر نیست دست برداریم
🔴
حیات و ممات ما به غنی سازی وابسته نیست اما به توان نظامی ما وابسته است. این دو قابل قیاس نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144397" target="_blank">📅 15:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144396">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گویا قصیر خواننده لس آنجلسی که اخیرا به ایران اومده بود و از جمهوری اسلامی طرفداری کرده بود درخواست خروج از کشور و بازگشت رو داده ولی جمهوری اسلامی مخالفت کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144396" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144395">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پزشکیان: از جنگ خوش‌مان نمی‌آید اما با قدرت مقابل تجاوز می‌ایستیم و دفاع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144395" target="_blank">📅 15:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144394">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پزشکیان: اگر تفاهم‌نامه‌ را که مورد تأیید همه دلسوزان است، به اجرا برسانیم، می‌توانیم بر مشکلات غلبه کنیم
🔴
با اجرای این تفاهم‌نامه، دشمنان قادر نخواهند بود منطقه را با آشوب مواجه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/144394" target="_blank">📅 15:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144393">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrG9RbkQ6Y8npkYVC-XDZEGlKgnGWYQnUMLsbemgMIkzSwSajF2807aSq8apQWqp58_gS4iTwVLEHNvmDXi9zadVorYDOA7lLQYVGzvDlutQCLP9GINPfpgKnxwxQMqc4eWVLvufmqUyccWDe6X39OJ_4QIPX7FH9ZlFfQLD22g7BrLpd9f1q4_aDAMj6tVvMbY7k9IEVUOu55pNwBrAPaYjKIlAY80z1PZc35-OYs872bPJFrJO4vDWrMC4qpm5kCsXpzsVg8m1XshoiIspnG_F24ZQEW5_y0e1QVgiXtQTULFzkj_Qlo3Z3sos_L9_R0dx5JxYcavzwWDx2xoYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا، گزارش NBC درباره بررسی نامزدی او در انتخابات ریاست‌جمهوری ۲۰۲۸ را رد کرد و آن را «۱۰۰٪ کذب» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144393" target="_blank">📅 15:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144392">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3063be136.mp4?token=erXib3S2tjH-OyZMtz58Tns4vytkMh21AyS03tC8Ms_fY8lNr4RiQfs5yJIZEhOTW1-TMbBDBbZBUOPLsjxBBqSYNxDdNjwYMdObBNPLPO8P3JfPmXMv8biQ_nKcU5wVq7Z_c0VLfGaa3kGZ78DV5cvL1HzjdboVu2Lx5kV-VT_iVRU3RqRzDiP1_weVtjQV3Jm0bbZ2s4_xbRS6IHgZy1E5nLsmWho7VADhBEdI8eYctxr4IbEp0TgQ5mNtv9yErBqtNjnxzRJbT_lrZQvGiekjsdWjwCuV5eOq5J5nRMx_6KOzv6y42QaSaN7okGFfuETnRH4gHoVjEdhPVAaPioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3063be136.mp4?token=erXib3S2tjH-OyZMtz58Tns4vytkMh21AyS03tC8Ms_fY8lNr4RiQfs5yJIZEhOTW1-TMbBDBbZBUOPLsjxBBqSYNxDdNjwYMdObBNPLPO8P3JfPmXMv8biQ_nKcU5wVq7Z_c0VLfGaa3kGZ78DV5cvL1HzjdboVu2Lx5kV-VT_iVRU3RqRzDiP1_weVtjQV3Jm0bbZ2s4_xbRS6IHgZy1E5nLsmWho7VADhBEdI8eYctxr4IbEp0TgQ5mNtv9yErBqtNjnxzRJbT_lrZQvGiekjsdWjwCuV5eOq5J5nRMx_6KOzv6y42QaSaN7okGFfuETnRH4gHoVjEdhPVAaPioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی آمریکا تصاویر بیشتری از این عملیات منتشر کرده است که ورود تفنگداران دریایی آمریکا به یک ایستگاه سوخت‌رسانی شناور را نشان می‌دهد؛ شناوری که گفته می‌شود توسط باند جنایتکار اکوادوری «لوس چونروس» در آب‌های بین‌المللی اقیانوس آرام شرقی مورد استفاده قرار می‌گرفت.
🔴
تفنگداران دریایی عضو یگان اعزامی تفنگداران دریایی ۲۴، با یک قایق بادی تندرو نیروی دریایی آمریکا و با پشتیبانی هوایی بالگرد UH-1Y Venom وارد شناور شدند، سرنشینان آن را خارج کرده و سپس شناور را منهدم کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/144392" target="_blank">📅 15:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144391">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0ueyMNtucOYIbxslpb2JckaRpYxZ8HvjgY_ziFfOg9b2Hamd9WCVSdcmQzS0YcEA1K_H-ATSfiDRSv9CmkjRVUbFcCDd4J5RbPz4_09A3AlhSsjgK9xC9xonJ0oVvUfS1qCisIxh3WZEn-v9ZQauvWEyrIgUhM1oIVqrReu2HChP9lpqKATRoZCmO8VTQyLRLQucMBtxc62qrc59pjm9S8jjsRVgyYJ0gRs6Dulpl1AJ4JtxNTiDWQmYWLzhuRCMZCvzQPlohDVjeSgZZcVDwxTfor27UCisL1uK0hxHkEPDpqYlypTCZtAgWvypkvbRw1_neoBntfkZJIjIG0WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیست جدید قیمت‌های موبایل در ایران؛ پایین‌رده‌ترین گوشی سامسونگ، A07 نزدیک به ۵۰ میلیون تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/144391" target="_blank">📅 15:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144390">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbVTs-rWXF_wa7jlazmDDdhRhSvK3nWrT4t2-SV-8aCVGC9dgF7ukomtRuAtPMx87bX8Wc6i_J7FsYi4YP6nfFsUqP2U3bscEjq77mdDzCRxPLRK1zh8j0jtBzc7JbIPNQ6lZlSBIifcO-tL27IYkUbKFVmErc3aFfY3DP5Sk1_7egjcs1OnjmTHlDyK4Yg3sFKjrYe41L9gFuegqfdlG9lamib67nr4809YhkJSh1BUGeURsd8GJlSaAjFfsfkQeAu17ytsrdCzzaAgkfq_U-TDtencq5ojN73qn6SZzmUUd2SkmPWZ9XNvIDM9YZAw61NR8RSBFQk-DjslzoBCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: بر اساس اطلاعات و ارزیابی‌های اطلاعاتی ما، تلاش‌های گسترده‌ای برای دستکاری و جهت‌دهی به بازارهای انرژی در جریان است. برخی عناصر دولت آمریکا با استفاده از رسانه‌های ساده‌لوح و زودباور، درصدد تأثیرگذاری بر قیمت‌ها برای کسب منافع شخصی و در عین حال، گرفتار نگه داشتن رئیس‌جمهور آمریکا در جنگی هستند که در آن شکست خورده است.
🔴
بازیگران همسو با اسرائیل نیز با ارائه ارزیابی‌های خوش‌بینانه و غیرواقع‌بینانه، به دنبال ترویج و تشویق ادامه جنگ هستند.
🔴
مصرف‌کنندگان آمریکایی هزینه واقعی این وضعیت را می‌پردازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/144390" target="_blank">📅 15:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144389">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511f12e405.mp4?token=kbhbCCJ1iiluWVigsVJQ9TlBWv5WEDHkxh1lAQJISBxu-2AJVRP2yXGFES5m8vnBtGFD2Y1V9FdSiDinaG72AQ51RqV__3Uk4iPVB-8JwRKiN_3lacbhsr4b_o6aMmgHNwPU3ql9oX9OQgV1PMco3YsCp8tKaxrcysqIeS1MSe2u4vkDg95UvIAczo1603CAOw3EVDL3QzDQeNwAZzO_3HsentRUSM99b9UFcaZ3-s2NTqYfd4my99-IkXvPql8wYjctKExpmr8ZDMQ2zUQi8RlB0AiW2dZDN-aXuJaLOBx7--nkUgPvVI8uAwUuxEG_fIFCF9W2HlZ80G0SC4_5bowl3IYFOl3tjVb8ud6poBqWawttEfm5eTG2ye4B17R6aza9dgJ9UCA5ACiGJ1MIB9q8Avx-q7yFhEtMscSToGzsdD5JjydbOzh0Na12CG9KhICTjDHuNlpKQJ9zB124WIEfIlfwirIIUAw-OLWBLGHYU2KhmU9uKYnNPTZOyYyaB6oleogWYQxH0oeI1SplDv-eK5MT6iMC9FFzxs7uXAgqbjXeIpzq3H2Yby-B1Dm-BCs2N6bm95J2zoCjk-Mj8CV0n8LfTF0o4mBDTuRuypAKFEeRp44QLmD3ftez9kwApSPT3dANCsIs5IctG9l9C5b7ugevYJV2_0CgeN-J2iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511f12e405.mp4?token=kbhbCCJ1iiluWVigsVJQ9TlBWv5WEDHkxh1lAQJISBxu-2AJVRP2yXGFES5m8vnBtGFD2Y1V9FdSiDinaG72AQ51RqV__3Uk4iPVB-8JwRKiN_3lacbhsr4b_o6aMmgHNwPU3ql9oX9OQgV1PMco3YsCp8tKaxrcysqIeS1MSe2u4vkDg95UvIAczo1603CAOw3EVDL3QzDQeNwAZzO_3HsentRUSM99b9UFcaZ3-s2NTqYfd4my99-IkXvPql8wYjctKExpmr8ZDMQ2zUQi8RlB0AiW2dZDN-aXuJaLOBx7--nkUgPvVI8uAwUuxEG_fIFCF9W2HlZ80G0SC4_5bowl3IYFOl3tjVb8ud6poBqWawttEfm5eTG2ye4B17R6aza9dgJ9UCA5ACiGJ1MIB9q8Avx-q7yFhEtMscSToGzsdD5JjydbOzh0Na12CG9KhICTjDHuNlpKQJ9zB124WIEfIlfwirIIUAw-OLWBLGHYU2KhmU9uKYnNPTZOyYyaB6oleogWYQxH0oeI1SplDv-eK5MT6iMC9FFzxs7uXAgqbjXeIpzq3H2Yby-B1Dm-BCs2N6bm95J2zoCjk-Mj8CV0n8LfTF0o4mBDTuRuypAKFEeRp44QLmD3ftez9kwApSPT3dANCsIs5IctG9l9C5b7ugevYJV2_0CgeN-J2iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی بزرگ در منطقه کی‌یف؛ تیم‌های امدادی در حال خاموش کردن عواقب حمله روسیه هستند، — رسانه‌های اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144389" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144388">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیرکار: تو جنگ اقتصادی هم مثل جنگ نظامی میخوایم پیروز بشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/144388" target="_blank">📅 14:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144387">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پزشکیان: اگر لازم شد برق دولت را قطع کنید؛ برق صنایع نباید قطع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/144387" target="_blank">📅 14:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144386">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq8nzwLraFF8Dved-N0diOUENsLyiUvfhkb-xux3tHP6j4Gp_sjSNnJtL5eOcnFZIlxTufJLT7Fq_DIKYF9_LnM1uYL5FjpERjISc5BJaNB99Yx9uBNHYWTyrHJOfhmENpgKbzbojr_xiaYORGe_97TrR7JaBzubkyn1bJFdpUKgaOc75achKHlP4ZnOxyv3c_qnwm1cnFiK9qVHhecXosQfobbTpqm1HOaf-LWRXieaVeZLt-tqZgDdOgdu3feWPq8IUN2VAi3dqVDzTcfd0XS9DYsMrAEewEhQaM0R8ViGzjVf5LZpIjZxnM1_cXv2L-DqjlTR72AnNq6oNR0VRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شورای شهر اوتاوا روند بررسی تغییر نام خیابانی را آغاز کرده که حدود ۲۵ سال است به نام دونالد ترامپ نام‌گذاری شده است.
🔴
به گفته برخی اعضای شورا، با تشدید اختلافات تجاری میان کانادا و آمریکا و اظهارات تند ترامپ علیه کانادا، ادامه استفاده از نام او برای یک خیابان در پایتخت این کشور «مایه شرمساری» است و باید تغییر کند.
🔴
این پیشنهاد هنوز نهایی نشده و پس از طی مراحل قانونی، درباره تغییر نام خیابان تصمیم‌گیری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144386" target="_blank">📅 14:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca27e916.mp4?token=WPpF1CtEqEa2Ks_Ne0loKnCtzoXL0ptPg7G_svMsEq2nlx5PeFjv_RPzUnSl2bWu-TZWT8jw08X8Cpa3gDkjug6vHk1Q8Sx6r4x6G_hjA4hu93E6StaNSFkyg9P9eR0u6az1rr3wSKQ0m4f5tICV_bFTZQb_thhm_ItddJdjT1Cj5hxwQUKpp-_354cxb18CEJhyfhxMwDMpS97V0_qyB1Xz61IeT6e8BJ2tgn9YoPU_OzzWwSnDxglhwQkbzrhdMFdiKilv6CL_CjAH0-HhD0j4BThbXXu4Awl3HNByUIwDWqNpESSTdlc9pT0rMoo8u_yNgkxoIOejc2UkQrSNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca27e916.mp4?token=WPpF1CtEqEa2Ks_Ne0loKnCtzoXL0ptPg7G_svMsEq2nlx5PeFjv_RPzUnSl2bWu-TZWT8jw08X8Cpa3gDkjug6vHk1Q8Sx6r4x6G_hjA4hu93E6StaNSFkyg9P9eR0u6az1rr3wSKQ0m4f5tICV_bFTZQb_thhm_ItddJdjT1Cj5hxwQUKpp-_354cxb18CEJhyfhxMwDMpS97V0_qyB1Xz61IeT6e8BJ2tgn9YoPU_OzzWwSnDxglhwQkbzrhdMFdiKilv6CL_CjAH0-HhD0j4BThbXXu4Awl3HNByUIwDWqNpESSTdlc9pT0rMoo8u_yNgkxoIOejc2UkQrSNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما: تو رو به خدا، به ۱۲۴ هزار پیغمبر، به همه اهل بیت باور کنیم ما در جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/144385" target="_blank">📅 14:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سیلاب و رانش زمین در شیلی، پرو و بولیوی
🔴
سیلاب‌های ویرانگر، بارش برف و رانش زمین بخش‌هایی از منطقه آند در شیلی، پرو و بولیوی را تحت تأثیر قرار داده و خسارات گسترده‌ای برجای گذاشته است.
🔴
رئیس‌جمهور پرو در پی تشدید این شرایط، وضعیت فوق‌العاده اعلام کرده است.
🔴
کارشناسان هشدار داده‌اند که در صورت ادامه بحران، تا ۱.۲ میلیون نفر ممکن است تحت تأثیر این حوادث قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/144384" target="_blank">📅 14:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1e6c44c2.mp4?token=sXQ2N2iKlD_THdP3n9LDdMQjROzlv7ITCJdfs3J4QVRZxt2cnnKGFVZJDuxw9ExEBU6liMgod-TmP7XjMKuhQsC2SpoaaimUk-uH4xaa91VgCR6ceL1fPsBXRy6j68UfhK4mHzs4an-FY4zkbcHXuE9vsY-6eQWQzCEMd7zjDm82hC6xnaCTiLcrv627XhJt2T0f_MilY1211ZUIsJJpzYxm2bWLVaelyecRq3v9JqAN6gS9rXN_9IWcM_qQPbLo-4IVBRe_yx6kO9K2indD06Q6l5QDh7ivF2gBcsNwgLgXOb4MmUmbWV7on1Hupk-rsDBQxScofBpDB66ZjKZ94oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1e6c44c2.mp4?token=sXQ2N2iKlD_THdP3n9LDdMQjROzlv7ITCJdfs3J4QVRZxt2cnnKGFVZJDuxw9ExEBU6liMgod-TmP7XjMKuhQsC2SpoaaimUk-uH4xaa91VgCR6ceL1fPsBXRy6j68UfhK4mHzs4an-FY4zkbcHXuE9vsY-6eQWQzCEMd7zjDm82hC6xnaCTiLcrv627XhJt2T0f_MilY1211ZUIsJJpzYxm2bWLVaelyecRq3v9JqAN6gS9rXN_9IWcM_qQPbLo-4IVBRe_yx6kO9K2indD06Q6l5QDh7ivF2gBcsNwgLgXOb4MmUmbWV7on1Hupk-rsDBQxScofBpDB66ZjKZ94oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری ازدرگیری محیط‌بانان با شکارچیان مسلح در تنگ‌صیاد چهارمحال‌وبختیاری
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/144383" target="_blank">📅 14:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMwLlKIgHarfVg5NHvcX2ulEiQS98awAXcsBIZT4CGzwZCne45bFFpbSKaLneWoxd2GzvKoLaUzEXEkTB-hrX_1FkfAOepiB5nsgJiCULg48A3MaSdH7VuD_imLPVf7dxJw7me75AWhsM2bMmbKIAsfnWQa-tCgrsTUXxibacEtepIPwfAtzTKc0dNsW8wIafTIgn_PEkRXKrutfErln71yHS1wIAngDpUYLe0UN4QAswbaiwyI_nkVmNik1EaOIZ-bec0qwo9SiAqoGTIYMVnCefm6qlccfggZ_aRCAUUpcICjMkjRFht_Ymt3tXzvIEf_YmkSzMcE53Kg1YrXE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این مرد ایتالیایی بعد از اینکه مادرش فوت میکنه چیزی به کسی نمیگه و اونو توی خونه مومیایی میکنه و بعد خودشو به شکل مادرش در میاره تا مستمری سالیانه ۶۰ هزار دلاری مادرش رو بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144382" target="_blank">📅 14:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5KwNe_nFEg6_gGf_ifHOhjU2OMPjwEmldsLchwXBRkWDrPubAmowxlm8b7kLI2y54Ir7we1hE2uQmIU87Ecv7U9VRDqHC5tgehIs7HsFSevirdQ3aaLB_3PTRwkJUdV0s16I27c3DtqzXx-tSCjKMjqLjCo6L4d3gNHuo-OkBXiaWN2VSB1YVsZYuAndOjd7Q5BPYlvpD5tB2vx6oZUedpz89_dOW3MszJd-5A-D7ecZ0qEGbUix_nFhocIon0wnjmAHXvU25DdWW1vaJ9yRJb7EIhEH9YJi_zbWST7lFVh_8g93WkcfZrzV_8pGyWaMYyxiERJYeyHJ0a4ifuUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع برکنارشده اوکراین به تیم دفاعی ایتالیا پیوست
‏
🔴
میخائیلو فدوروف وزیر دفاع پیشین اوکراین پیشنهاد وزیر دفاع ایتالیا برای همکاری به عنوان مشاور در زمینه نوآوری‌های دفاعی را پذیرفت؛ سمتی که قرار است در کنار فعالیت اصلی او برای راه‌اندازی صندوق سرمایه‌گذاری دفاعی در اوکراین دنبال شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144381" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
العربیه: گروه‌های عراقی در ساعات آینده قصد هدف قرار دادن عربستان سعودی را دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144380" target="_blank">📅 13:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_aur90-31DhknWDB-rnsOnubYK37rAZqlQeg-wy-HA6u9jDD5l9sBbBeiQHn4GuI1Oyg16kHjcl-hETKtbZ-CfugLGkFFS1_aNx1lQofRu2IsfcKvzzfX80eXtgQ0qq8cMgBpO40zTIQNlzeQItsRAiO2xS7Yd7Fvz4SuLOMb0SEQkJ0FgCQm-oK8v0wTRV7nALFCB4i7uBKKgpC4ZuiiG80iU1BAKLrZDTJK4be6QDNdkaXEKCYy3OgbbhM2d5IvHvE3dRWFunr36QkZBgP0r86gbzUX9yS_SHZBMYnwH64dA0RgNse8MHM24J5wa0jaewtngUqqF_RZC7Mg5bKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه رسمی توافق عظیم نفتی ونزوئلا و آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/144379" target="_blank">📅 13:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756a7c2134.mp4?token=OoUZaa9JJaB0v8HTFfcdgvvBHU4VNfnIxmM0ImXpemohlkNvACNSgUDs1ToCq8xcMmgrvMEThpeWYYQLCrjmOKeA6qCRctjYhwuCb8yj5fhy0icoXqU7mzViboZWI1nnHpJgEMxIFiMqyVKjC_apksN7_PIjWK00CWDO87Hsb5zVs8fIoKmLkFnf2rHhB77e2JMQUWkQpKW6qbJzFpvpe4Qwixw9zI6zSxmrh1htK0C_2WxG19k-D2C0Is5XNrG2BLXK60RXenqBwVVAE7KeFDSIOSN9UcK-QV7AAYX0lirleeqZgQz-EJGosctNev99n2BOTkglV_Q9KcRuwMAvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756a7c2134.mp4?token=OoUZaa9JJaB0v8HTFfcdgvvBHU4VNfnIxmM0ImXpemohlkNvACNSgUDs1ToCq8xcMmgrvMEThpeWYYQLCrjmOKeA6qCRctjYhwuCb8yj5fhy0icoXqU7mzViboZWI1nnHpJgEMxIFiMqyVKjC_apksN7_PIjWK00CWDO87Hsb5zVs8fIoKmLkFnf2rHhB77e2JMQUWkQpKW6qbJzFpvpe4Qwixw9zI6zSxmrh1htK0C_2WxG19k-D2C0Is5XNrG2BLXK60RXenqBwVVAE7KeFDSIOSN9UcK-QV7AAYX0lirleeqZgQz-EJGosctNev99n2BOTkglV_Q9KcRuwMAvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر مسعود پزشکیان: برای کسانی که می‌گویند تحریم‌ها هیچ تاثیری ندارند، واقعاً نمی‌دانم چه بگویم.
🔴
منظورم این است که عقل سلیم یک چیز خوب است. این تمام چیزی است که می‌خواهم بگویم.
🔴
عقل سلیم واقعاً یک چیز خوب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144378" target="_blank">📅 13:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq0ex33TLXfn_XhWWQl0i3BD6-U0Wbsm9yjS6Gxgk8NUGsqs5YLxWVPEKzCTUVv1AoZg_RZ53Ws67jRr-bkUhREY6SWClFCK4hu1zGmXKkIYM1kj711ShNSWWLI-xzcvZRzSZOU-fc3k_aX-5YZbmrE8irq71qOPqtFLZvc0kMC34aH7kaOmRldzGfHg47c4VrwlOBkCEuCg2Acmg1dHsf19aFO1_7GaWXUggCJo4A1slFyeOt4RXQBmu9EQjNpid4UMu1Co7_8gALB66_O_miWxFt4vtMefa-7RspB8MMgly7j-joG-7ShBv6S87Z-239sQdczeNWHQspQFNt_f8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: شنیدن خبر درگذشت پادشاه هارالد نروژ بسیار غم‌انگیز است. او مردی قوی، با افتخار و بسیار مورد احترام بود. او به کشورش عشق می‌ورزید و واقعاً مورد عشق و احترام مردمش بود.
🔴
قلب ما با خانواده سلطنتی و تمام مردم نروژ در این دوران سخت است.
🔴
این یک فقدان بزرگ است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144377" target="_blank">📅 13:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
العربیه: گروه‌های عراقی در ساعات آینده قصد هدف قرار دادن عربستان سعودی را دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144376" target="_blank">📅 13:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNIU7KJg5pJ9MvG43zKZTn8-E_C2Y6zM0_xm0HfqMxRf6_QImx9J3iS3-5t7cu60we4rYIuKZX6FotUbri__Ob4xe3mOs_K9FJiCk-T4jVqlzI4nru0vtvghl0-ACfVMsGwgq8lafXGbTE5WTWk_IioNnGklmch-utA0OdzQioFFTrIT0gWuPYED7_xGcFpfRJXkyIa5Tk26wnLHzcVcJraS2GWh7LlTAKOg9Ndzfn3ySt8mLzq79bmCL-odyKAwAAyjlOnrmZY1fvD4t-nOx21lhDqRaPLc34Jw3TUlZy65eGyaBjezSZaKNpRuKdmTat8wCmsKXFzF1n3t_287Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت دلار از ۲۰۵ هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144375" target="_blank">📅 13:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np99qTr9ePkRNkhwdg04ktCYA1HUWu7JxO02vqA3mKr5ldxRww5A98WGv2RauQzEJzC8izzdnjaogCK2uQmicrN9N5Xb1vF3MiPRN2ITKVShWMU8jCI--UNQtKX__RjuGi8THmbXiZj-rEO4vwt3IO7yUvZRMNPrOg9mO_j-dTN46Pp2lexlZopOdl42JElYVD1J3qZlGwvgL-RzwRayqPr23mpNlQuJOwOz44DsUT3rUNvYdmw63OV-iqWR23Dn-MLtQ9DENQLr-Gr1cNFMZn7U9WN0N5236W2_fg_f5DaD2NuE-Tn3Q0lbMdvD4Bh3GkMTkAc1zLevSycQmuq6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: میانگین عبور کشتی‌ها از تنگه هرمز، از ۱۰۰ فروند قبل از جنگ به ۷ فروند در روز رسیده/ ۵۹ درصد ذخایر استراتژیک آمریکا خالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144374" target="_blank">📅 12:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دادستان تهران: پرونده نتانیاهو و ترامپ رفت دادگاه تا رای صادر شه ایشالله
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144373" target="_blank">📅 12:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144372">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۸ ریشتر حوالی قصرشیرین در استان کرمانشاه را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144372" target="_blank">📅 12:45 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
