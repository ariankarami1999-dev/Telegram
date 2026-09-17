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
<img src="https://cdn4.telesco.pe/file/CuxB3qD4xcgHGfh9il3yleb8r4qprPRdstAxFEKMFU6nUIdMaduQ_P0BOXdBsSUbhVjoxD7z28pMcZdibA4r8DkDVDqD_rLxBhk414aooVXjYx5n9ZyPtZnwI8pOwfn1qVmii215wahAXn3W23EExHrEFsxycs4E1fOyllr8u0K9zi-FhTULhZYXm2i9Z5ifN0gFVuPxPUeol_9gJYj9223brwghBx3Pis2a7nkOagIPAiNPlt4bTvB1S-4vG91zQnnSMucfiv6G8072OO7TrLQh7y_nop16VRj-ZzzYAx5hhexaU_5ICgclpHYKvJY1fT1FeVbENIxWd6dojW7GLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 949K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 03:18:30</div>
<hr>

<div class="tg-post" id="msg-147959">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=vNzdMidmyt51kdbpqFxTldgkVvJxPBeYi9gtnKpMLYLGfFQJ4y66rMkkP4zP5NyQVhPte3b7nFfSMZA65D5nbwXtQVVdHPUGf_u4s5bRyej4ma08WXBeBi4pqrQIoMdrJ-rzDa-tPOqgmKl0kgBkE9K_sEqlfbNl6QesoFf9sQeWqqGtNe32KN6tFgYbc6sBhTygiU6tWzdbKmwOUa7ro9OPqVMWJqT6nKVcnKAor5zSpzhutObtQQiv5j_ZndUZS9eWKEBwq8z0fznQY5K7_2Lrx2qtbdx3tx_MzXzfXs-b5PAJ4YOZ6EY_0mUJOmAYlsxbM1l7MQvAevFPYVFJ1y38mUV_bXNXT-l4q_76nTKhbmFWk8AYgKwMVmLkqLl6ZRI-2q4AX_j2zSx_fbssk7wNaELAceN687Cp8hQ20S24Z0KDCTEB17iIAs0n_f80WzwOVWvSAR1NUdQQFuc77RQ-gjrp9-yxmUtzoDJWTVSfxULNcKuhhRTu9pzhHkQ_0lu_I3Js-Z5VjohC_tkQJJI-yjOlb1YeP-V6nlwW73HJMCH8cA2ptHe2izDmB4lluHpy33Hux3vhD4iKN_OaveNR-VsBiIb3JX4BaDo7vuWOhXEFxGUfmb3RmV2CcsZ5zSLayXrCbT5mZlu1-wbAJQHcB5K8S8nbaaoV07g7jyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=vNzdMidmyt51kdbpqFxTldgkVvJxPBeYi9gtnKpMLYLGfFQJ4y66rMkkP4zP5NyQVhPte3b7nFfSMZA65D5nbwXtQVVdHPUGf_u4s5bRyej4ma08WXBeBi4pqrQIoMdrJ-rzDa-tPOqgmKl0kgBkE9K_sEqlfbNl6QesoFf9sQeWqqGtNe32KN6tFgYbc6sBhTygiU6tWzdbKmwOUa7ro9OPqVMWJqT6nKVcnKAor5zSpzhutObtQQiv5j_ZndUZS9eWKEBwq8z0fznQY5K7_2Lrx2qtbdx3tx_MzXzfXs-b5PAJ4YOZ6EY_0mUJOmAYlsxbM1l7MQvAevFPYVFJ1y38mUV_bXNXT-l4q_76nTKhbmFWk8AYgKwMVmLkqLl6ZRI-2q4AX_j2zSx_fbssk7wNaELAceN687Cp8hQ20S24Z0KDCTEB17iIAs0n_f80WzwOVWvSAR1NUdQQFuc77RQ-gjrp9-yxmUtzoDJWTVSfxULNcKuhhRTu9pzhHkQ_0lu_I3Js-Z5VjohC_tkQJJI-yjOlb1YeP-V6nlwW73HJMCH8cA2ptHe2izDmB4lluHpy33Hux3vhD4iKN_OaveNR-VsBiIb3JX4BaDo7vuWOhXEFxGUfmb3RmV2CcsZ5zSLayXrCbT5mZlu1-wbAJQHcB5K8S8nbaaoV07g7jyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب تو شب نشینی شهر بابلِ استان مازندران، وسط تجمعات شبانه‌شون دور هم جمع شده بودن و داشتن «
کلاغ‌پر
» بازی می‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/147959" target="_blank">📅 01:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147958">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYJuBgMirdy-Y5cZRTjs4hxgQNHCozmKNgOXqobGJVRivaO3Hdn4BuSn8eqvvE3GJVr3_GpliaSll4EJ3BZ0Bs_xCPlf__9kNwEqLQE1_jkwUCApe_dXGQCOs1F5WE0046KbT01-JLiTcDQGespEoXXdxcUo3jgMMnpvAK9Rc4AexkSLEu63UQh-7lSOsqWMwOCYYSrbdgxSEPi0NrbS5hBYYQ1_vesKJ-G1FdAEzDsejYlr-IrPDOKb4lzfmpCYbzp7sCil3WtE-HBadTcH8FontmWcpWWN5bH8YONs31CgvfTG2bf-9_ssWXg8H21Tlvc9N9N8Lbw_Jibcuve-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
ایران ایر که یک زمان بزرگترین ایرلاین آسیا بود اکنون فقط ۹فروند هواپیما دارد که اکثرا فرسوده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/147958" target="_blank">📅 01:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147957">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqXDDJHAKfJ3MDAgF1DE0vJJVAA2pD6MXb5SU76U2Pr2p19ko11r_9Vs8Ajxrxov4bBIsx12nz3r0M_YoQ4RSZt9euqtcTIK1v8dQzuIgkxlQ4JAev0zdCJZPj33riCsMxdYh4sDHVKR82lnBMy_f5S_BuCsmf-ViJy79Bl4wnwhtvWj9HBaiKuhA5BuLPMc2BPUTeYk37gLNOzYPTKZplkAalshCpc2ai06sSbmwMLUW0ICYfg2ppzc5GVrDaPF1I6E7noKoJw9tchZod6aXy_mn6odskn5q-mqRG99iy4cSUAadiqYIEda4OmeYIA856GjVod7F_hXxYs4XY-JmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران شدید جنوب لبنان توسط اسراییل
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/147957" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147955">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQZvLPFXcA3LKc0AaJyUscLNAd7j0l6UyLrnyDBTACQj4AfvKYgzixUlKeMxI_GyfbqStkY7WXtg2d2Q-cj2pi5aqLuszKONkvH3XXJbEQPPaRGr-M4ulWz86HJ3vZzXTic6mWNNFJ42GoHdlh_xj_-SQCnxVtFdIkGO7bSEQ9C72V7xkp1z3mwtD2H07DnlTrSGVYXxSTtGdbPjpH4LAuo0m0sjodWNYPXsq18Yco8vycEKOAsld_5ju81oe_a54LAWrEvUGUOp7v5Z07iXtBWjCoPKYEd0xxENN6yadoKOa3Vw1W5XJLESoGYwEkOee549PSnsc4xcLrD63Wkkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidmfQ7NdrUS8cGuMr9AWJiFo20zt5MOBLZ7TrV2L-qSsLLb2gFPSSy1D2-1oHU48CTKsAsZ1h-r44se8q8Ygee8Zcm5d4TRFVw88Pd4Ggn1fmYRa5ximu3PcFvZlo2Qep2QNj_XeAKPq2qKWaLBcA0f5lRjZsfGISnfenU4LB4rCKLijau1rpoUsyLFeQzIC46vJ0PoH4SJ-b_Q2Ha9ixokOimJYin7A2zgwAxKy8OkOWAmK148YD84DEzuo_bhG93if6YJQhQUDTbH8C72BNZL6Na2CBo9g2j8v78_3IOyQZeJtXFFExGUB-0LCOvEmxa6dtg_q_ONYsr9m09yqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گسترش سریع فعالیت‌های ساختمانی در سایت طالقان-۲ تهران
🔴
تصاویر ماهواره‌ای نشان می‌دهند که فعالیت‌های ساختمانی در تأسیسات «طالقان-۲» در تهران به‌سرعت در حال گسترش است.
🔴
طالقان-۲ از تأسیسات مرتبط با برنامه هسته‌ای ایران در چارچوب پروژه «آماد» معرفی شده و گفته می‌شود این مجموعه در اوایل دهه ۲۰۰۰ برای آزمایش مواد منفجره مورد استفاده قرار می‌گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/147955" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147954">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
قوه‌قضاییه: واسه ۱۵۹ آمریکایی اسرائیلی پرونده تشکیل دادیم دادگاهی شن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147954" target="_blank">📅 00:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147953">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
میدل ایست آی: ترامپ «وسلی هانت»، جمهوری‌ خواه ضد اسلام و حامی اسرائیل را به عنوان سفیر بعدی آمریکا در عربستان نامزد کرده
🔴
این انتخاب در لحظه‌ای حساس برای روابط آمریکا و کشورهای خلیج فارس صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/147953" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147952">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نتانیاهو: من نه مسیح هستم و نه پادشاه.
یک پادشاه نیازی به انتخاب شدن نداره؛ اما من باید انتخاب بشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/147952" target="_blank">📅 23:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147951">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: اگر به‌موقع برای حمله به ایران اقدام نکرده بودیم، امروز اینجا دور هم جمع نشده بودیم؛ چون ممکن بود اصلاً کشوری به نام اسرائیل وجود نداشته باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/147951" target="_blank">📅 23:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147950">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مکرون خواهان اتش بس فوری در لبنان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/147950" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147949">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه آمریکا به الجزیره: هیئت ایران طبق تعهدات کشور میزبان در مجمع عمومی سازمان ملل حضور خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/147949" target="_blank">📅 23:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147948">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصب عمان دریافت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/147948" target="_blank">📅 23:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147947">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M10dM4kaNLYgJwIqjVMxCPkWBXxECCTf9PP4MySIKTXFt-k7rLdEZWqJXZRtPl_eDVWATfZPeJqkNJhmitolRzfRWPOxTPLiVGgw3-HMQqAPQvSRbcT5-72sK12bsDZYXwKYa0kfgjGX9J3xyPE0RXP_Wy9i15UeXKWR6qcbDOHoPYbMmf41xknJlQgdDgCi9pmtuUlUjAkrrLbv-mPre6mRqHIq313gMCrI5EueTfEwYCqpPMiXpNCdHUUexWKWsT52GBoyCJQ48sVuv7_IWe5UE93yUqql4Nu6QV5n8kI5Mo_nCNrchXhXvvVMitQN8x07GRzBHb_Noj-_hftovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: نظم تک‌قطبی که در آن یک طرف با زور و اجبار امتیازگیری می‌کرد، به پایان رسیده است.
🔴
وتوی چین و روسیه سوءاستفاده سیاسی از شورای امنیت را رد کرد و حاکمیت قانون را مجدداً تثبیت نمود.
🔴
ما باید از چندجانبه‌گرایی دفاع کنیم؛ زیرا یک‌جانبه‌گرایی در خدمت منافع هیچ‌کس نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/147947" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147946">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دلار و طلا تا کجا بالا میره
⁉️
🚫
پاسخ عجیب هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/147946" target="_blank">📅 22:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147945">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خزانه‌داری آمریک«بیت‌بانک» (BitBank)، یک شرکت ایرانی فعال در حوزه دارایی‌های دیجیتال، را تحریم کرد
🔴
گویا صاحب بیت‌ بانک بابک زنجانی هستش
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147945" target="_blank">📅 22:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147944">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
آخرین جزئیات قتل‌عام خانوادگی به خاطر ارثیه از زبان خود قاتل
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/147944" target="_blank">📅 22:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtIgKbKhdjN5qDbNYfR_tLphlQL4NYkqAtAhO5avw8MdGY6hdLzJhXeGS6N3iQUlhbmemzgDZhaWfISwbXDxPGDG9qRRYsVGFljDi-tDku3xTPpwxcfqMkIOoRIljTpk-aBZv0e0pmYTQvAdXqxkQ7b0U-Wujkc1qrClfv7OTyTC8zIEz0yfeck9DMfQQ0InKODm_ZkOsA3ZmzAMzKUC8iYXrRrsk6lRlvBqDaYTB1v_3gEkMZH_NaC7dRg5305SUnLgFHa_fdHo4PtygI37dBqdFprFiyAGyWKdl3sZinxoJ6BLtzhNkB9-A_2HLmZsQc4fbYgA2xgrkoAX6ZvARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJmUFB_A255g8PH_dMP5FvlYcG-hx_J741M38Yir78LUxMIjhYT9BiKVw_9DLuXHPYihLLzvKRBIEswsEjU8tCMSv_oWMct2tb1hGSwqjHZDYZxoxqRTipT3KVEx0SukKthaFfK4Kvcaw5KaazvmBYL86-tlxkr5XSwo9NWkNHevcXbf4nVsxlq3aOGQVO0ikvHbJOAXCQNbtt4RTHI8-_xyt8TRdg4uJntAI7BylDFfVgc_ohNUne0Gyro1mKQ8GU36lTdTD7RF8lR8FqsS6dj64sDkT63zLCh4EWUQwkYaj7-Lj2ZpcE8Udvaxle-CcGBkR0AxZ4F_2O3jpqlHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCRuNmlRPjptkGTGbm_t3wqIlUBa7-gm3nrXTKZ9xBq-Y9zRYfB9tzwWkGWtelFPTxznw4QZZdMUsX4Ixa5WbMrdUsN75n_RAxd8488tc40xcXkxIDcwMNeV18UTn9QkGmITQMkMkxSU-LdJODSTY7UQ1pu94OHuHrv3OlZkVJfvFc_S4t_IZ10guTPWFRvqQeeRrjpgk0CRZpDt9gQIiTbXDilrSwl5UMrV8a3cBnqcbJgRWfBtIwRjnxMopXz0Db2iReuh_bdgmiKTeXM3vstxRoxlFmRpkHoTkTCn97KynWXmZKd86mGY5t1M8eUXcGqzdNF_TIMzdVRfV2KmLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از محل سقوط هواپیمای F-16 در شهرستان بلر، ایالت میشیگان، در شرق ایالات متحده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/147941" target="_blank">📅 22:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
آسوشیتدپرس: واشنگتن با صدور روادید برای مقامات ارشد ایرانی جهت شرکت در مجمع عمومی سازمان ملل موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/147940" target="_blank">📅 22:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9263a32ce5.mp4?token=U5fTvQ7o79cpmP5joeVaQQMJa_A4OIxVBWeV0g4dQNHs5PDBXAclmPx3JFKvnMdhEjfTv6Fx9sbWpW0zQE2f0I1g12jh64z_cBzQ1m6T3S0_aS0YsQvMpkaJFfzkUGWzIiPtI_Wb85afNueRqAoAzQQ5-GJg8EaRc2_b-lvxFx3sLFvOzCYOLSdTDXfVRXYfP9iTRy47H0epYw9m_luONkBAXRz9RTvAN6SIn2w7oWIGn7o84myhp2a8I225nRZnOvQAAG0GpRCfU-BXssDnLtxiOHn-TUvyy20vtB5bIh3JVBlXgi5zUUqQLL1Ookd7ybJ6zzkiY08tYbNTVbwmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9263a32ce5.mp4?token=U5fTvQ7o79cpmP5joeVaQQMJa_A4OIxVBWeV0g4dQNHs5PDBXAclmPx3JFKvnMdhEjfTv6Fx9sbWpW0zQE2f0I1g12jh64z_cBzQ1m6T3S0_aS0YsQvMpkaJFfzkUGWzIiPtI_Wb85afNueRqAoAzQQ5-GJg8EaRc2_b-lvxFx3sLFvOzCYOLSdTDXfVRXYfP9iTRy47H0epYw9m_luONkBAXRz9RTvAN6SIn2w7oWIGn7o84myhp2a8I225nRZnOvQAAG0GpRCfU-BXssDnLtxiOHn-TUvyy20vtB5bIh3JVBlXgi5zUUqQLL1Ookd7ybJ6zzkiY08tYbNTVbwmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عروسی یک زوج ایرانی ارمنی با حضور اسنوپ داگ خواننده معروف آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/147939" target="_blank">📅 22:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147938" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بر اساس گزارش شبکه خبری ای‌بی‌سی، سام آلتمن، مدیرعامل اوپن ‌اِی آی، و جنسن هوانگ، مدیرعامل انویدیا، قصد دارند هفته آینده در یک شام رسمی با اهمیت بالا در کاخ سفید در کنار شی جین‌پینگ، رئیس‌جمهور چین، حضور یابند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/147937" target="_blank">📅 21:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/147936" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده فروش احتمالی ۴۸ فروند جنگنده F-35 لایتنینگ ۲ به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را تأیید کرده است که نخستین خرید این هواپیمای پیشرفته توسط این پادشاهی محسوب می‌شود.
🔴
این بسته شامل ۴۸ فروند F-35، ۴۹ موتور پرات اند ویتنی، تجهیزات ارتباطات، قطعات یدکی و حمایت‌های اضافی است.
🔴
وزارت امور خارجه به صورت رسمی کنگره را از پیشنهاد این فروش مطلع کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147935" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: «صحبت‌های ترامپ درباره حمله به ایران، به اعتقاد من تلاشی برای زمینه‌سازی جهت مذاکره با ایران است؛ چرا که این موضع‌گیری‌ها بلافاصله پس از سفر عراقچی به پکن مطرح شد. همچنین تماس تلفنی میان وزرای خارجه چین و آمریکا نشان می‌دهد که چین در حال سنجش تمایل ایران و واشینگتن نسبت به هرگونه اقدام چین برای حل‌وفصل اختلافات میان آن‌هاست، و ایران نیز در جستجوی کسی است که تضمین‌های لازم را ارائه دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/147934" target="_blank">📅 21:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0vblWBb9mKSuCVsNJpNVLpOVSoghTc4Ws3twTTvGLFsC0fUL_3HcTP1M5gj6B4IhITh31xlu6XSs8ri1qPKSKoLg48Y52j7A-n3h7VHzm1CseLzQUN5lFp38TTS7uqo1_viJQAHLNPB9CFxJURYWtthqNdhCgdof0TcrVSfWww05yZr4OT3NaisoUHhEBhd3MKl8h2u1iBvWpNfnqAJl9EUGUD3Yj53vS-TiUoJQrM3KaKSBztVWboZ_jzUQPMI3UN-sV62rH06qa6vLmVRal78ucuhH2ie1ZVbK1VAvptmIxE7_FtMSqExmCng-M66WXLrtog6zcwXcDhYjztTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره لهستان: اخبار عالی! به لیدرهایی جسورانه از سوی دوست من، کارول ناوورکی، رئیس‌جمهور لهستان، پیشرفت‌های چشمگیری در جهت ایجاد پایگاه ارتش ایالات متحده در لهستان حاصل شده است.
🔴
اگر این اتفاق بیفتد، مکان آن به‌زودی اعلام خواهد شد. این یک گام تاریخی برای اتحاد بزرگ ایالات متحده/لهستان ما خواهد بود. از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/147933" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fh9I2fD2Y337GWuMzfBrWGxkR-JOfUwLufvOMsfqPsefa0dvcF7NhwpfbThz98_ziZhs9Lsv5MWqTWcraqouJSB2KCNzEhqFQLTJE_ffZFTfAVMXuh28pl0dwAxl1wNNzvNq7qY0v1b9daP7jA_z3GcGjRs4VwTZmp-rxG-xr7xfQMVAYq25dvq8kpNGh2Nox6kPKnmnxBuZo5vDSZ183hmNJuHvng7EBedlPoIJCKXx3mjtSYOyigvNfypDVZvNEL5bvLRrReQjo-MqeoChUxco1_LRA04OLktjDVDQUN9_EsJWqk6JLL-Wbdq3zu_oZoCfpTm4NewFoTjTahQF3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fh9I2fD2Y337GWuMzfBrWGxkR-JOfUwLufvOMsfqPsefa0dvcF7NhwpfbThz98_ziZhs9Lsv5MWqTWcraqouJSB2KCNzEhqFQLTJE_ffZFTfAVMXuh28pl0dwAxl1wNNzvNq7qY0v1b9daP7jA_z3GcGjRs4VwTZmp-rxG-xr7xfQMVAYq25dvq8kpNGh2Nox6kPKnmnxBuZo5vDSZ183hmNJuHvng7EBedlPoIJCKXx3mjtSYOyigvNfypDVZvNEL5bvLRrReQjo-MqeoChUxco1_LRA04OLktjDVDQUN9_EsJWqk6JLL-Wbdq3zu_oZoCfpTm4NewFoTjTahQF3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس: کالابرگ ۳۰۰هزار زیاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/147932" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147930">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMwUfgCjxlsS0SU329S-pPX61Mc198UxXbfmGeVp9DIFrb6J2EOGypbayhItf6XM81jV18ecewraAVduQSvCteYV5xlBSE5tGb_wjLkOHDKxrQiUfBNrlrxHcsvu8FF9LB3laP3-3yQJoznXUfFpkQasdS0m7KUwhIcg0Po_b2M52OZcMi7uCMBPoWbTQzY3Rj7BOLJNnbPyP3C3JfbYd6hiE07tFWe61s3c-xT-Ri7S9X41-YkolfY3XUH2YsJupVAetUgs-E2Ur347kucrjiQve6WSVQLTOlG-oaZbUnkpyyaxkSVA5sEfgjKNK10Uq6XX_pW-X3DIdlz0rNtQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef55f0b0ff.mp4?token=IaKdsoPjdkXgtfOLi1ZFLbht7bDexp7M7pnpmBv2yROe7xTqYUk0OvnkRdM-sDuy897Rm09iRKdA6rKDylfBuLdgLT7fJPN4oaNv2GQ8ltYoCDqvwGMqbkagGdKVNG6tS8s5t0OtBhHGCP0QpOywa2xCm7eN0mX7Ot8Wv2wzAIcaO243z61SK4WLRpdU1p_ndCwkM5Pt-nf6SW__ClxcPDVdiUFfyyLHZ1JOvgmIkzgucTh4QZbpoDNtfzm90RtlRknUex46VhOVvaYe4p3p0FDuVVtKIkLODqALEpYp4VUq3y64ylPNpabAvLYKluHoITGpcyRSsIOvpmL50tNugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef55f0b0ff.mp4?token=IaKdsoPjdkXgtfOLi1ZFLbht7bDexp7M7pnpmBv2yROe7xTqYUk0OvnkRdM-sDuy897Rm09iRKdA6rKDylfBuLdgLT7fJPN4oaNv2GQ8ltYoCDqvwGMqbkagGdKVNG6tS8s5t0OtBhHGCP0QpOywa2xCm7eN0mX7Ot8Wv2wzAIcaO243z61SK4WLRpdU1p_ndCwkM5Pt-nf6SW__ClxcPDVdiUFfyyLHZ1JOvgmIkzgucTh4QZbpoDNtfzm90RtlRknUex46VhOVvaYe4p3p0FDuVVtKIkLODqALEpYp4VUq3y64ylPNpabAvLYKluHoITGpcyRSsIOvpmL50tNugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/147930" target="_blank">📅 21:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147929">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/147929" target="_blank">📅 21:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147928">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
آکسیوس: ترامپ دستور داد سطح نیروهای فعلی در خاورمیانه تا پایان سال برای احتمال از سرگیری درگیری‌ها حفظ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/147928" target="_blank">📅 21:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147927">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزیر دفاع پاکستان، خواجه آصف:
حتی اگر هیچ توافق‌نامه‌ای وجود نداشته باشد، اگر عربستان حمله شود — به‌ویژه مکان‌های مقدس ما — ما به موجب یک توافق ابدی موظف به محافظت از آن‌ها هستیم.
🔴
خانه خدا و مدینه منوره — محافظت از آن‌ها وظیفه دینی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/147927" target="_blank">📅 20:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147926">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb984ea71a.mp4?token=d3ykdmfyLoZxrsybuGGB2rE1w-SGZRssnMIf8mJCTqJtp_05v3kExMbh2SUPxMy8A0TCBXJ2rLYYzl7phSxLK2feo2XvzKDLd23Vczy8SAZkl98QA8FBL-4fCrVmxJGnuVHRgYVaZx9HjiJh8bvBCLOVD89bRQQkA8Hmbl6yN6LYRC1eoVonA_h4a6VA_PQlHiiavXkc4WVf7WE4psGdEoeTJKmw_d8kPfEGmEYHP30KIUIoVl8AbravNIUSu8LSLEPZIQ2ijlVkfqNuzqe2sOe7Xu7UGac0gsSLXdufJ9o_8CF-HOazZ7mluT1h2UiHkN-zznAMLhZgifZDp2_EhBQsRAJKreovaRLJ2JpRuuoCjcr8tmySYGIg7eDa8lz1wNI4rvR5UmoZIOp6xNHXFmEG7HrNg8Hb83kDm05VSAj0Zey8mZazOtSaG14havz7qS_Nee25LsIa79GOhsOjo1iMbiC89yQmSNrki7cV3aJTiWyDDN3omcE4MgH0xNy_LhAx1mTnj6EKelkP8W45gL2jogLuWbbFH6tiOiujnNtXxqZZr3-bm3vgBillXH-vD2rTCN6qMlvt66RG3uTn25TfbNuDCniKWLm6vGx8OntRNHtyIIovkaHujJnSERUSHfeC5hjqbggXCK_80HakEKiWvGgbjFiPsLaZKK3GYF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb984ea71a.mp4?token=d3ykdmfyLoZxrsybuGGB2rE1w-SGZRssnMIf8mJCTqJtp_05v3kExMbh2SUPxMy8A0TCBXJ2rLYYzl7phSxLK2feo2XvzKDLd23Vczy8SAZkl98QA8FBL-4fCrVmxJGnuVHRgYVaZx9HjiJh8bvBCLOVD89bRQQkA8Hmbl6yN6LYRC1eoVonA_h4a6VA_PQlHiiavXkc4WVf7WE4psGdEoeTJKmw_d8kPfEGmEYHP30KIUIoVl8AbravNIUSu8LSLEPZIQ2ijlVkfqNuzqe2sOe7Xu7UGac0gsSLXdufJ9o_8CF-HOazZ7mluT1h2UiHkN-zznAMLhZgifZDp2_EhBQsRAJKreovaRLJ2JpRuuoCjcr8tmySYGIg7eDa8lz1wNI4rvR5UmoZIOp6xNHXFmEG7HrNg8Hb83kDm05VSAj0Zey8mZazOtSaG14havz7qS_Nee25LsIa79GOhsOjo1iMbiC89yQmSNrki7cV3aJTiWyDDN3omcE4MgH0xNy_LhAx1mTnj6EKelkP8W45gL2jogLuWbbFH6tiOiujnNtXxqZZr3-bm3vgBillXH-vD2rTCN6qMlvt66RG3uTn25TfbNuDCniKWLm6vGx8OntRNHtyIIovkaHujJnSERUSHfeC5hjqbggXCK_80HakEKiWvGgbjFiPsLaZKK3GYF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا:دشمنان ما در حال یادگیری از جنگ‌های ما و به چالش کشیدن برتری‌های ما هستند
🔴
دشمنان ما ممکن است از نظر جغرافیایی پراکنده و دور از هم باشند، اما به شکلی فزاینده با یکدیگر در ارتباط هستند.
🔴
آن‌ها فناوری، اطلاعات، تسلیحات و حمایت‌ های اقتصادی را با هم به اشتراک می‌گذارند.
🔴
آن‌ها میدان‌های نبرد گذشته و کنونی ما را مطالعه می‌کنند، به سرعت خود را با شرایط تطبیق می‌دهند و در پی یافتن راه‌های جدیدی برای به چالش کشیدن برتری‌های ما هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/147926" target="_blank">📅 20:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147925">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها در تماس مستقیم با ما هستن و همچنان خواهان دستیابی به توافقن
🔴
می‌خواهم از جلسه عمومی سازمان ملل (هفته بعد) استفاده کنم تا مستقیماً از متحدان منطقه‌ای درباره گام‌های بعدی جنگ بشنوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147925" target="_blank">📅 20:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147924">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/ ترامپ: به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🔴
هر اتفاقی ممکن است بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/147924" target="_blank">📅 20:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147923">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/ ترامپ: به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🔴
هر اتفاقی ممکن است بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/147923" target="_blank">📅 20:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147922">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / دونالد ترامپ: قرار است تصمیم مهمی در مورد ایران بگیرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/147922" target="_blank">📅 20:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147921">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed64f0a840.mp4?token=QnEMG5eG6ZvR0UZOArOTpoWC89q6KQJgYdwYjHUskW1y9o9eic-D8U__SB372bOxpbff-qtVkakHGaGTuAHITKRN-NDYzbCZeahPXpfvad4K5ftgAtBzwy1-v1P1YpbQTZk8oxJYGeG0gIMzOZPpJrOEJpVUSiNcoB-mpkT9WFgb0e_8bsCqmhM8BEL02doyStatJby-uj0g-aUa10H1wps_ZspvC4-jqRVv74d-HdCoDCT5GtlOMA9qEtfpkQH8Bfv1qW0GI3pttSqIOMriIsYo4N7j7HA0uwfdgXUIwI6mPuOcX_HZtdrdqyQWCxdkpuQ4-AElLEshq_INe3YQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed64f0a840.mp4?token=QnEMG5eG6ZvR0UZOArOTpoWC89q6KQJgYdwYjHUskW1y9o9eic-D8U__SB372bOxpbff-qtVkakHGaGTuAHITKRN-NDYzbCZeahPXpfvad4K5ftgAtBzwy1-v1P1YpbQTZk8oxJYGeG0gIMzOZPpJrOEJpVUSiNcoB-mpkT9WFgb0e_8bsCqmhM8BEL02doyStatJby-uj0g-aUa10H1wps_ZspvC4-jqRVv74d-HdCoDCT5GtlOMA9qEtfpkQH8Bfv1qW0GI3pttSqIOMriIsYo4N7j7HA0uwfdgXUIwI6mPuOcX_HZtdrdqyQWCxdkpuQ4-AElLEshq_INe3YQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نمایش بمب‌های سنگرشکن برای تهدید ایران در گزارش خبرنگار فاکس‌نیوز
🔴
خبرنگار فاکس نیوز: آنچه الان می‌بینید، یک بمب سنگرشکن GBU-31 ویکتور ۴ است. ما در یکی از انبارهای مهمات ناو هواپیمابر جورج واشنگتن هستیم و همان‌طور که می‌بینید، انواع مختلفی از تسلیحات در اینجا وجود دارد؛ از جمله موشک‌ها و بمب‌های گوناگون
🔴
در انتهای این بخش هم انواع دیگری از بمب‌ها را می‌بینید. این‌ها بمب‌های ۲٬۰۰۰ پوندی هستند. باز هم تأکید می‌کنم، تمام این تسلیحات در صورتی مورد استفاده قرار خواهند گرفت که رئیس‌جمهور دستور حملات بیشتری علیه حکومت ایران صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/147921" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147920">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9225e42d16.mp4?token=WIY5qzE10K2g7iPWyou9WnFwdhM5qyweRZAZBwxRvfqjXAHifZ4KLtFJSYsCo2hrYRm1s9CyDInKne2RWyCMmIif6zL8MCZdl2Nmx4jT0ophcvDdWckNOaFJDn7h6wXXRgc4p22P0AXs9m1edH7d66gKdImuvITCNJJ_oeOA9Xiw2HVnCHDF0kVcCJtaOJjgcIibZaXLUV5yPx8gkTyHBo5jQg-dPKKlQb2CWd87Ax6UUzGQDREOE7uQ1HRny89KTtEdR0gPVgbX2Ks-XPPnFeDm2tezD0sua95CHs7PD_9spIxiL-yn0l9WaR6YAHk6ywoTVOvNhI7TzRZL1Q51hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9225e42d16.mp4?token=WIY5qzE10K2g7iPWyou9WnFwdhM5qyweRZAZBwxRvfqjXAHifZ4KLtFJSYsCo2hrYRm1s9CyDInKne2RWyCMmIif6zL8MCZdl2Nmx4jT0ophcvDdWckNOaFJDn7h6wXXRgc4p22P0AXs9m1edH7d66gKdImuvITCNJJ_oeOA9Xiw2HVnCHDF0kVcCJtaOJjgcIibZaXLUV5yPx8gkTyHBo5jQg-dPKKlQb2CWd87Ax6UUzGQDREOE7uQ1HRny89KTtEdR0gPVgbX2Ks-XPPnFeDm2tezD0sua95CHs7PD_9spIxiL-yn0l9WaR6YAHk6ywoTVOvNhI7TzRZL1Q51hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف مانند «موقعیت‌های اضطراری» بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147920" target="_blank">📅 20:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147919">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16578a4b94.mp4?token=NvwuO87D8TS2_MqQXULfJFpdboEZtVAobK9cJqcggfZVA-EK5HVXZQT-MQIwKKOyAlVpFLf62H_7tBO-VyakYH6195sydauFQeqaVJMQ1chVScPOcJF1SR5waV3LqhmfeAajGjYFABH8aIxB9bmYEQnrz-PIQMQGWfGAmrkCGoCln2BPtRzjqvXjKptV9D1xKWpTNI5XrYs7LM4QF7vfYkgasR6KiYFw95ncrJDaJ4gxCYcTgiD_0SPDwDCW066zHms1h2JgB-QawxZoucCTLB2zEc6upeSk1gRpX7hN4yzeotjBLaNJfv2X0h52B3I1VDx7CKVw_Oufi5DsAa00lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16578a4b94.mp4?token=NvwuO87D8TS2_MqQXULfJFpdboEZtVAobK9cJqcggfZVA-EK5HVXZQT-MQIwKKOyAlVpFLf62H_7tBO-VyakYH6195sydauFQeqaVJMQ1chVScPOcJF1SR5waV3LqhmfeAajGjYFABH8aIxB9bmYEQnrz-PIQMQGWfGAmrkCGoCln2BPtRzjqvXjKptV9D1xKWpTNI5XrYs7LM4QF7vfYkgasR6KiYFw95ncrJDaJ4gxCYcTgiD_0SPDwDCW066zHms1h2JgB-QawxZoucCTLB2zEc6upeSk1gRpX7hN4yzeotjBLaNJfv2X0h52B3I1VDx7CKVw_Oufi5DsAa00lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من خیلی باهوشم
🔴
رئیس‌جمهور آمریکا گفت: من آدمی با سطح هوش بسیار بالایی هستم اما در نهایت من فروتن هم هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/147919" target="_blank">📅 19:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147918">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy4dhSIJ4xXk6iBthVoFsjGck4TmKZJ2gbXGiQfOZVN_1uABX-1ZAfptDpwosmXykpubEDupKx9CtXoT_AJe6-ubGYUEZdoU-zRue5YSLvO8H9USfu7xSTthsXqr37v1kkBMPamIUn8q5VJKq8xcpJmUktMRTnpubZc-w0YLOg873SR7BIak_Qia7pL-2sJGFjyO9SEI-0FQ5JoNk8KIkwWyVVqGbGeG9-70erCtrBa-vb4OcYW_a6Qn1jnnrLZ3clu7LkRTf_rLTM0GMmJVOdGfM4Mfbq8HupclFz1KrBp5wmqA9P863Cp_pNrapwO0LT2-TM13EYf7kMfh8H9xpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محبی، سخنگوی سپاه خطاب به آمریکا :
شما روایت هالیوودی می‌سازید اما ما لاشه جنگندتون رو با فرغون جابجا می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/147918" target="_blank">📅 19:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147917">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سفیر آلمان به وزارت امور خارجه احضار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/147917" target="_blank">📅 19:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147916">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPyjcWgtyQMdVW7SyUmpJ165aetIzYb6Y-E97bh6GxQksT5pa2-pAnDJtHEw1aFIoecRD7uI8jGJoM5HbaJhfM56yGNaspZ8RTei8btTxqHHfCKpMFs8G6jryptREnVPUow9RvNaJymQ3pdnUqNtrGYi8YTGiO_uyRotOLq0iRg54FA5i0Zk5Tr9at2IsBe40CkQcMZQNILCy_MMCiv3G8P5q2hzBSL4X5XgVpw5JhslrRVnCmzLKP_HBy6CSmvzzntjww7v3b2J_CJrfUasyMVyO3M2mYRN3XYuMCN9V36NtPH3AAU4RfUwYwIutg8u_ou57OFrH6RY2EGWgvPRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی بریتانیا اعلام کرد گزارشی درباره وقوع یک حادثه در فاصله ۷۵ مایل دریایی شرق عدن در یمن دریافت کرده است.
🔴
بر اساس این گزارش، یک قایق اقدام به تعقیب یک نفتکش کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/147916" target="_blank">📅 19:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147915">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c065e013.mp4?token=VdKmtRgGvDzq9NE-hUsd21exWToBfayd2FZ0gyhCuaydJHXLK9KXchI3g_wUTU7QtFkalH4b0YbEPAH07p6o7ysXxfWl8udokXH3M_c5I9JybJqKfFcpkmrv2GaUsJn6dLUirna04ORmLQbgf_L5ZkgdWXFxkuiN_DQPVfFg_aSaw1LnOpRLl_NZmuPt7MdPQeuY_WL3yv7tcSpA69eg5NbNPUf3gn4NjXRqRGXX4mlOLtX2XHLbew-KB0wDP9ZJw5j_S6bXqDKPq_KXYYRA3i8ptCyl7pfXsuiptHCu2O0eQhUe4LKCAzr6WGga1c_V3kCzOAXvXAfmKRhcVD_uboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c065e013.mp4?token=VdKmtRgGvDzq9NE-hUsd21exWToBfayd2FZ0gyhCuaydJHXLK9KXchI3g_wUTU7QtFkalH4b0YbEPAH07p6o7ysXxfWl8udokXH3M_c5I9JybJqKfFcpkmrv2GaUsJn6dLUirna04ORmLQbgf_L5ZkgdWXFxkuiN_DQPVfFg_aSaw1LnOpRLl_NZmuPt7MdPQeuY_WL3yv7tcSpA69eg5NbNPUf3gn4NjXRqRGXX4mlOLtX2XHLbew-KB0wDP9ZJw5j_S6bXqDKPq_KXYYRA3i8ptCyl7pfXsuiptHCu2O0eQhUe4LKCAzr6WGga1c_V3kCzOAXvXAfmKRhcVD_uboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده روسیه در شورای امنیت: عدم اجازه ورود رییس سازمان انرژی اتمی ایران و معاون اول رییس جمهور ایران به شورای حکام، نقض آشکار  قواعد بین المللی است
🔴
در سال 2025 تمامی قطعنامه های اسنپ‌بک ملغی شدند و دیگر امکان بازگشت به مکانیزم ماشه وجود ندارد.
🔴
از آمریکا و بقیه کشور های حاضر شورا می‌خواهیم دیگر تقابل با ایران را ادامه ندهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147915" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147914">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بیت کوین منفجر میشه
‼️
‼️
‼️
اگه توام نمیدونی بخری یا نه حتما ببین
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/147914" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147913">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igHlqLuvPXGhGVNVD42RUVSW76XHtf0CkDvkWYC5_Ed068ySzmrppDOuNu8paoDV6m1C00xAgWEOYS6XKt9oYwRP_C2W7VWAcHVjOc9FGO5N-iNiQ0I3d70pQEzaagaVk8uR3i5gku6e8xpypVSpwnI0pS5fPDLUKPPlow_1_UsU3MfaRoaT9akKK27FX0AG7FGmITaVkwNpwjfrDc-C6kLSxqR3AZPpPGrfMDOlySYGapdTRiUy-HIKWILrPb49qH2LTdyQWkxhfhsKGzQaTFZl3sL8Cn_qVBGuvdpdhEZGOekHmzRHBesG3xdmbcT0Aeq5RG-j1QHOU_udn8_gpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۹ جنگنده F-16 دیگر آمریکا دقایقی پیش از اروپا راهی خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/147913" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147912">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d68625bb.mp4?token=Eom5oYkkns7YyaPlWpiT_NvpxyNRtXosMvMtgBnBb5UgGN_Q5swjxc7pzZNwDw4LkDR4aPagHwsaceDEJaJRWkDBuTU71WXs0dXeXD4Y8aBY7suWuuH9AgBju3gKGsUJH63DUDtF0DQWXVaT0V56TUKeLIWMAFohZtwHcC7L1CbI-bjePCiJx0sdaLx7Zw1ol3eh4KZ_JDC4nZKOjHT4KPtNtVsS85GYiqvBekNT3OylC7Yva0MG4JWk_31eC6dzwToXDg_NtgQVOi6Q5siC0g116xhIDbG9O8wh4tv4Iby_vBj1lmpT2ol-sfnu2sMAOn2YV3NAYsO7OcairadWFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d68625bb.mp4?token=Eom5oYkkns7YyaPlWpiT_NvpxyNRtXosMvMtgBnBb5UgGN_Q5swjxc7pzZNwDw4LkDR4aPagHwsaceDEJaJRWkDBuTU71WXs0dXeXD4Y8aBY7suWuuH9AgBju3gKGsUJH63DUDtF0DQWXVaT0V56TUKeLIWMAFohZtwHcC7L1CbI-bjePCiJx0sdaLx7Zw1ol3eh4KZ_JDC4nZKOjHT4KPtNtVsS85GYiqvBekNT3OylC7Yva0MG4JWk_31eC6dzwToXDg_NtgQVOi6Q5siC0g116xhIDbG9O8wh4tv4Iby_vBj1lmpT2ol-sfnu2sMAOn2YV3NAYsO7OcairadWFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای جدید نشان می دهد انصارالله در حال تقویت مواضع زمینی و سنگربندی در کوه های اطراف تنگه باب المندب  برای دفاع در برابر ضدحمله احتمالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/147912" target="_blank">📅 19:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147911">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز پنجشنبه ۲۶ شهریور، اعلام کرد که ارتش آمریکا در راستای اجرای محاصره دریایی و تضمین رعایت قوانین، تاکنون در مجموع به ۱۰۴ کشتی که در تلاش برای نقض این محاصره بودند، دستور تغییر مسیر داده است.
🔴
سخنگوی سنتکام روز گذشته با تاکید بر اینکه خطوط کشتیرانی اصلی در تنگه هرمز پس از پایان عملیات مین‌روبی همچنان باز و امن هستند، این محاصره دریایی را «آهنین» و کاملا موثر توصیف کرد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147911" target="_blank">📅 19:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147910">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b6b9d143.mp4?token=MMmfBQjLdMF9OjVBAHK5hYioTVZlinijYMZXVCfGxykKLrDTIexP88Vqy-wwjuefzC0FJEMy25kP_Ad_b6yBcULxDa3Rq-YYXcddv5KJx0K0wvD-xTh1tdWWZJwz9wYg4wMqMbEpwX3iOsMfqa6sOMqTjTsDuFOYkpjtE224tSDjd3Lpl5nhjn7tzcRvOzlZZ9Epn15e_HIvz8fYhsdeRJFHH0Qpb3wy-Xp8UOk0H3V2bhmtFZ_khh-akMpr_TI9M5OV2bLX1Vr38aKRExx04t6Yax0_NQOaHaLwp3kRVAuH02bE_kWVUOoPoaYUntHMbeT0Eu7ZwCqHl01J7eBY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b6b9d143.mp4?token=MMmfBQjLdMF9OjVBAHK5hYioTVZlinijYMZXVCfGxykKLrDTIexP88Vqy-wwjuefzC0FJEMy25kP_Ad_b6yBcULxDa3Rq-YYXcddv5KJx0K0wvD-xTh1tdWWZJwz9wYg4wMqMbEpwX3iOsMfqa6sOMqTjTsDuFOYkpjtE224tSDjd3Lpl5nhjn7tzcRvOzlZZ9Epn15e_HIvz8fYhsdeRJFHH0Qpb3wy-Xp8UOk0H3V2bhmtFZ_khh-akMpr_TI9M5OV2bLX1Vr38aKRExx04t6Yax0_NQOaHaLwp3kRVAuH02bE_kWVUOoPoaYUntHMbeT0Eu7ZwCqHl01J7eBY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از وقوع بهمن عظیمی که گروهی از کوهنوردان را در ارتفاعات قفقاز مابین روسیه و گرجستان گرفتار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147910" target="_blank">📅 19:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147909">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoqZmIlcgALiEHr6eveMizyMXOPZnobZqsB8ZTekMt1yrnsf-dbL7rcm0i-Vo9Yan1hnWk4F-XbqVX5m-vS7tQXkoUvi39MKqFLnX15q4ALQj0D3Pn58Heaz2mvAY9q5vYkwBRt43BuWnBZO_4gvFwOZAhPTxJLvw4csTxwRjQjKvNy2Ch6kh161Gevhsz0NbjJ5_jznMF3rBcGLQKSdiD31YMA-KloLRtYwIKmaUMbSD013ia37FQfS-7n3tV9TS7gAW5J1j8jmXkIFIG_u0xylSQVe5vrjbIqL23a6AqUagLhzu_vtH7EyNQdXZ4wtmOg7uWbpGPjshrEvF-GkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیئت حقیقت یاب سازمان ملل:
آمریکا در حمله به میناب و لامرد مرتکب جنایت جنگی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147909" target="_blank">📅 19:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147908">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
هشداری فوری جامعه «باستان‌شناسی» خطاب به رییس‌جمهور: تخت جمشید را فوری نجات دهید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/147908" target="_blank">📅 19:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147907">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c82a08a4a.mp4?token=lYn2939tLmPqersVxi2Jx7KDdwQKftniEiuh18mdGvvv6NCGf-sMPDu6BK8I2MOf8TnyIEmOpoY7ACtuiBAT3pxvIvP_7_F7XFfgIPllev46EdzilKyaT1kXjGgiiT_wit8Fgh_vfkVJj_T5_NdB16S3hSOoMtl0zWRpYdqEIA9am-41dT8KPft9NVdo_ET6gJubq-NQg4e9a19ALNrDbJF5l55DBkWnuCUqiTLNbdbz2q4SPsteJYuSzQcm9FxoOmnXIIwYDDAS0NiRKjOYWB6CU9zIxryXhDnuGkcgYuLWL8PT5V0egIw7TXCLUErNYozOE2ugYhWO5QIyCx0ruolUCFRZicbaoUG7xoYub4hjPJAr28cQhXqgHrlySRy8XciU0cW7pmJQmHkmgIF2EfbkiKiomFTbq1IMfB8od5jaCuuoQnhp9O5SXaJuW1WdhAUyMnQ63xRBbwf6THfiUpSODOgNp9hMfIkt1H-eJeW-HurMQgJ4BFO4lGHBEcAFDnr17OcfUX_Lq1Vl-uryZuWxVjaDyjHaF_bBuCwAftW3WWogwk_SINghyZSRST5goPhi47vW1T0a8VE6uiL6NPFWSnm7UoI6FszD3fcngmqWsK5YEL8NBljpJ-B-4Qnwyj5b0aeIb6G_7_Ubc_p6mjP8Ldbx4xydKinn31NydIM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c82a08a4a.mp4?token=lYn2939tLmPqersVxi2Jx7KDdwQKftniEiuh18mdGvvv6NCGf-sMPDu6BK8I2MOf8TnyIEmOpoY7ACtuiBAT3pxvIvP_7_F7XFfgIPllev46EdzilKyaT1kXjGgiiT_wit8Fgh_vfkVJj_T5_NdB16S3hSOoMtl0zWRpYdqEIA9am-41dT8KPft9NVdo_ET6gJubq-NQg4e9a19ALNrDbJF5l55DBkWnuCUqiTLNbdbz2q4SPsteJYuSzQcm9FxoOmnXIIwYDDAS0NiRKjOYWB6CU9zIxryXhDnuGkcgYuLWL8PT5V0egIw7TXCLUErNYozOE2ugYhWO5QIyCx0ruolUCFRZicbaoUG7xoYub4hjPJAr28cQhXqgHrlySRy8XciU0cW7pmJQmHkmgIF2EfbkiKiomFTbq1IMfB8od5jaCuuoQnhp9O5SXaJuW1WdhAUyMnQ63xRBbwf6THfiUpSODOgNp9hMfIkt1H-eJeW-HurMQgJ4BFO4lGHBEcAFDnr17OcfUX_Lq1Vl-uryZuWxVjaDyjHaF_bBuCwAftW3WWogwk_SINghyZSRST5goPhi47vW1T0a8VE6uiL6NPFWSnm7UoI6FszD3fcngmqWsK5YEL8NBljpJ-B-4Qnwyj5b0aeIb6G_7_Ubc_p6mjP8Ldbx4xydKinn31NydIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حیف و میل گازوئیل توسط قاچاقچیان در منطقه مرزی سیستان و بلوچستان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/147907" target="_blank">📅 19:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147906">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53768ce3a2.mp4?token=R9Gc4e-Lfcf_zcGMhOZrDf_J0-2inKvFjnn1f6kv2vC4Eri5XBkpTLcizsCX7j3kgw2NVT81Vfe1p1Wo8Klv5dyf8hCWMPNdIrGwjau3CkCm2e5RJSL0ifsVDA2zjEnGlT1yv-bCqsP8Qx_2Up-A2udlaDIa0xUatM9UxfPdfNyK4opJSK7Bpg_CvRxZNgFOrRq6rCWHFMjMpcQPomXoXpzYwQZSfayWRv66ncu31i81xI8kEowXmSJbjLSIQ2UAD8JWFYgX6d6wsL082h8DXhET2-p-zpSK7mvo0NXUYLoZUa-LbDHz7J-AdkWvrVDZAbmaJEYGLHan7fbmBR3TpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53768ce3a2.mp4?token=R9Gc4e-Lfcf_zcGMhOZrDf_J0-2inKvFjnn1f6kv2vC4Eri5XBkpTLcizsCX7j3kgw2NVT81Vfe1p1Wo8Klv5dyf8hCWMPNdIrGwjau3CkCm2e5RJSL0ifsVDA2zjEnGlT1yv-bCqsP8Qx_2Up-A2udlaDIa0xUatM9UxfPdfNyK4opJSK7Bpg_CvRxZNgFOrRq6rCWHFMjMpcQPomXoXpzYwQZSfayWRv66ncu31i81xI8kEowXmSJbjLSIQ2UAD8JWFYgX6d6wsL082h8DXhET2-p-zpSK7mvo0NXUYLoZUa-LbDHz7J-AdkWvrVDZAbmaJEYGLHan7fbmBR3TpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه حوثی‌ها (انصارالله) یک پهپاد سعودی را در آسمان استان دمار در یمن سرنگون کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/147906" target="_blank">📅 18:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147905">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClgfSRNsCn84rfPGpzUb_mLHC3lwB9B-PrAHzNEk1rPtwnSciiEci23dzcMj4FMY2_DK0EQaHHRTZ70jCw3RRQfenrb6LdbbTqDiVKCnK_cjNpnMpulxSQQOkW_N_W-thd1e-Kdfo6da1obRhrFvaaTi290aSrFURJ0MZVRNNNNvizUhlFnZ2ANnYx6WUrIWEj5JtFl_HFP8Z8JJOrDirt29UMWUVh2JWVgmgnL40g3dJ7UsxLgZTG7C39f5IPJFVNaWR_cIRZn4V4CIvQv-OvWKpHBGFrJ3Nmy3U4Yu7eqmGNvk0PtRn5dAf88IqpkLzqiF5fRe6Sz4fy_FxufZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرف حق پسر رئیس جمهور:
ملت جانفدا شبیه یمن، یارانه نقدی‌شان قطع بشه و از برق سراسری استفاده نکنند و هزینه زندگی‌شان را نصف کنند و به سفر نروند و از هیچ خودروی استفاده نکنند
🔴
نمی شود از یک طرف به خاطر اقتصاد ناله می‌کنید و از طرف دیگه میگید بزن توی دهان فلانی و فلانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/147905" target="_blank">📅 18:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147904">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عراقچی: از ابتکارات رئیس‌جمهور چین استقبال می‌کنیم
🔴
این ابتکارات در مقایسه با دیدگاه‌های غربی، با درک درست‌تری ارائه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147904" target="_blank">📅 18:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147903">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
الجزیره: روسیه و چین با استفاده از حق وتو در شورای امنیت، پیش‌نویس قطعنامه پیشنهادی آمریکا برای تمدید مأموریت تیم کمیته تحریم‌های ایران را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/147903" target="_blank">📅 18:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147902">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در محدوده تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/147902" target="_blank">📅 18:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147901">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/147901" target="_blank">📅 18:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ذوالقدر: تا به زیر کشیدن ترامپ و نتانیاهو، تنگهٔ هرمز رو نخواهیم گشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147900" target="_blank">📅 18:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
الجزیره: روسیه و چین با استفاده از حق وتو در شورای امنیت، پیش‌نویس قطعنامه پیشنهادی آمریکا برای تمدید مأموریت تیم کمیته تحریم‌های ایران را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/147899" target="_blank">📅 18:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147898">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0940fba80b.mp4?token=YXDVvNqEM1hla7qIvS8vHQu84sKTB7_ue_9pdzWiMq9zz3t0Y6kesKPjJQU9mEi5gc1wHn8skUCXggOH716QXBEi43AGNH9pKsTH_z6D3m2jbmAo9hflSqy0sSn_k9dzSieK3ypkJBOuIRMZR3AsLuxZ4IEWtEXoYOHX7fn9oGC6p23bBm96BhovRN99aKXCXBCXApZ4p9KZ7-si8lr5OoBprxFmoKzRlUJNZ0zVawzgjFAxKkcJXhAqfmFG9N6f4KRZHnbhwoABb6z2y9YLAZcC-_cFzS423kH3UngJNsFp5mlduMs7RfDb0l_sb_UWktq6dsJn043Dr-JicIFteBelHShkqT2eHuJvOAJjbLCo0V0843o4L_XFu7_JAlzKvX6LL6V4S-GDL6p9R3kwzBB0RZSYA1g68PxAydW0Ak4vZcAd3VY4skrs0AyoJKoj20W_6c-8bbLvHhPw1Iv61a59_C1PoJhQ60mLjaGzcDyFC21ISW3wYaJoIgXOWRH-JlXmoyx7ZjuZ7sAdYstmqOUcvkksl7MJZ9dTOK0gvtMFb6FcN8XTX3NWOHiV-_5NMdJCtn10Q6TJFjPPrGk9Wh4FSmJbKl56AHco5ERta6h9bX2YK_fsEwVEVhi1zDq0KOV_7KrZ0UqmM3gJXZRVGNB31-wIHCeHQqEoVsNNamE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0940fba80b.mp4?token=YXDVvNqEM1hla7qIvS8vHQu84sKTB7_ue_9pdzWiMq9zz3t0Y6kesKPjJQU9mEi5gc1wHn8skUCXggOH716QXBEi43AGNH9pKsTH_z6D3m2jbmAo9hflSqy0sSn_k9dzSieK3ypkJBOuIRMZR3AsLuxZ4IEWtEXoYOHX7fn9oGC6p23bBm96BhovRN99aKXCXBCXApZ4p9KZ7-si8lr5OoBprxFmoKzRlUJNZ0zVawzgjFAxKkcJXhAqfmFG9N6f4KRZHnbhwoABb6z2y9YLAZcC-_cFzS423kH3UngJNsFp5mlduMs7RfDb0l_sb_UWktq6dsJn043Dr-JicIFteBelHShkqT2eHuJvOAJjbLCo0V0843o4L_XFu7_JAlzKvX6LL6V4S-GDL6p9R3kwzBB0RZSYA1g68PxAydW0Ak4vZcAd3VY4skrs0AyoJKoj20W_6c-8bbLvHhPw1Iv61a59_C1PoJhQ60mLjaGzcDyFC21ISW3wYaJoIgXOWRH-JlXmoyx7ZjuZ7sAdYstmqOUcvkksl7MJZ9dTOK0gvtMFb6FcN8XTX3NWOHiV-_5NMdJCtn10Q6TJFjPPrGk9Wh4FSmJbKl56AHco5ERta6h9bX2YK_fsEwVEVhi1zDq0KOV_7KrZ0UqmM3gJXZRVGNB31-wIHCeHQqEoVsNNamE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سه تن از نیروهای امنیتی سوریه در جریان عملیاتی که علیه منزل فردی مظنون به عضویت در گروه داعش در شهر الصمین، واقع در منطقه درعا در جنوب سوریه، انجام شد، کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/147898" target="_blank">📅 18:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147897">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3WTCAa8sNm1z8mZajqzvOm8702yU2uNOwBnvlsFq9aNTdUfFZFLOVwdSEMxfmSuDLQwsVB6zW_CBTUYbRfvBzJPMS98VFGooCBQ-lAJ2cV8p5xC2td3_k6gJLjb7LI37oYXBZmaEgBNjAu7Z2pLNCkHYeb5GKQYdUb5HKPHGjTVyqarC353vupB9ZdMgG5g3vrbQl_W5fepAvYHZQ-KISZO-J84A8BDaRFKD3FUSlGnGffQP5yqQkYTwVJSWBsWlVP-DyN1rOitM0aJq4ZaJNIecPMxMwqK-y2JqsfD7dfHK89OGn3JlD4Jm7_cwKWufpKCjwjcgoivJWikpC7n6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولایتمدار: روحانی و برجام ما را ذلیل کردند؛ خدا ذلیلشان کند! حالا با اقتدار مذاکره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/147897" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147896">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2SsEuk_Ba293ashT2RqIa6Ola2TvX5TXi_u8iFZWlOuC_aDdxAKEJlswB_OwruSGFh89N-VHdAcmQ2_cYKhlKjfFEsLIAeFRKmwISBuKDiE15ghWrBj3CVrxmjnr-aKlWcCWpF0YC9_Y-fQRma3BPJabVlgDoJ9zV3KKDSk7W7secGXsLEY4K7q_ZOioM25FlgAjQlDhoPUtRNco0VZZgyNg-PRgZpGXOc1OTKN4pstQ4BPRHDVr6Vjc8JAIRaiDf4fUxjAd2SIXd_fEEcCKaMqTtx1j4WrChoH8PVOwDySdJso69egtbAUbJyXDqtSQmECadpTjJRtOvPKQRT6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جذاب ترین رهبران جهان با حضور رئیس‌جمهور پزشکیان تو رتبه ۱۱ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147896" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147895">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmz0m1MIkDsnVMT83ES5kHE7bynbXUHkUzBa2jsv-F8YPXH9RXgkh9IjqejATM7ule1zQSw0FKZsIL7dhhg4S7k0f48CYLvo1V395D8sYrbSghHW2GuAnoJt9o8saVTMVC8x-mR5_4trLkE-4WcmB1LPpFe255cCQChom5A-GmDrYMHs9Aie-ePYYDEV781fM9j1lP72BDwrm-k_OLmQ10btp_RLLXMx_6-ryxi8gPZLvaAfIHCjePcnj1xn0FxGovIJP202uLQ3aytqzCX1KkVMFm8izLsX31WefXV1ewYC-iVpT9Dalz80dYKUfsHZvefGi0_gpXRjddQT5-ekjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۱۰۲ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147895" target="_blank">📅 17:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147894">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
گویا کارت‌های سوخت جایگاه‌ها به‌ تدریج جمع‌آوری خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/147894" target="_blank">📅 17:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147893">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع آگاه: ریاض از عمان درخواست کرده است که از انصارالله بخواهد یک آتش‌بس دو هفته‌ای برقرار کنند که طی آن، گفتگو برای بررسی راه‌حل ها صورت گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/147893" target="_blank">📅 16:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147892">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نتانیاهو:
تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است، تضعیف شده، نظام ایران را سرنگون خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/147892" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147891">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سپاه: پهپاد زدیم
🕺
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/147891" target="_blank">📅 16:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147890">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16117ba246.mp4?token=o9Yd0u40BYoObs0q4B5oAHTZ8s_r-jPuCe_nZHbec9YjhJVurX6bBYI3Or5oq0xjWEYIXaGg-Wr-iV1KSSi9tXZCJi5ztDWv7-Scci1TdkKKIDc0tKfn8nPs_M8CZmVzY_kHnJJ0DJ3bL2GMR6EN8iLSxLWAlX3LAfFyXzgZXq1a3wBFbDGoxBOFckpO8P2SlWCwpz2tbUcTOVotQSpQcaxI6O4xxdkDyojWW8xdqf8AhZFDEDlOW9rrv2qxVMfMWkIA636oOOYQZlZyyYCsjgV6XESxAvY47PkLdOYr1nIR5S4Ka9n2m-UFz5b-kbDpid-6iJrY3f5EhVYifuT3dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16117ba246.mp4?token=o9Yd0u40BYoObs0q4B5oAHTZ8s_r-jPuCe_nZHbec9YjhJVurX6bBYI3Or5oq0xjWEYIXaGg-Wr-iV1KSSi9tXZCJi5ztDWv7-Scci1TdkKKIDc0tKfn8nPs_M8CZmVzY_kHnJJ0DJ3bL2GMR6EN8iLSxLWAlX3LAfFyXzgZXq1a3wBFbDGoxBOFckpO8P2SlWCwpz2tbUcTOVotQSpQcaxI6O4xxdkDyojWW8xdqf8AhZFDEDlOW9rrv2qxVMfMWkIA636oOOYQZlZyyYCsjgV6XESxAvY47PkLdOYr1nIR5S4Ka9n2m-UFz5b-kbDpid-6iJrY3f5EhVYifuT3dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا: هیچ‌کس برای ما تعیین تکلیف نمی‌کند
🔴
مارک کارنی، نخست‌وزیر کانادا، با تأکید بر استقلال این کشور گفت: کانادایی‌ها متحد هستند؛ هیچ‌کس قرار نیست به ما بگوید به چه زبانی صحبت کنیم.
🔴
هیچ‌کس نمی‌تواند فرهنگ ما را تعیین کند یا به ما دیکته کند که در عرصه بین‌المللی با چه کشورهایی توافق و همکاری داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/147890" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147889">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3n7-p0E3gkLJvMCrQQTvWVhzEDuJ26fURwMZxXyBz7iijmpwfY6LUbdvMk-rKW6ZQLQc8vhlmsNTbWJpX9Y_YkfcHLjBu_iUavbKGs-l_eH75t3aEoi1e59fmH7c-tXY0P-B4YQb7DI6FfYFl0FcL2KnfyA5-MfPo4W6k-VrZpwy0oUPFRrb2U2SGtJ7gLIZdC0VHUtUgHMu94qYwFlGW4Cl91yLLOCZkYEubpkJLZl8Muks4oB2ivQqR_D64H1qYEsC8M2KnUwlgtPImmF84wV2ZyndESGtFilRHLjZ28gmK7SfQRptv4tKfmbQE4_NVIPCJD9Rr3fbO0xNou8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از به صدا درآمدن آژیر خطر و شلیک موشک‌های دفاعی، آتش‌سوزی بزرگی در یک شهرک نزدیک به مرز لبنان رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/147889" target="_blank">📅 16:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147888">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: شرکت پهپادسازی آمریکایی «پاوراس» خبر داده یادداشت‌ تفاهمی با ارتش پاکستان امضا کرده که شامل یک سفارش اولیه در حوزه پهپاد می‌شود
🔴
این شرکت قرار است با یک شرکت سهامی عام ادغام شود که تحت حمایت دو تن از پسران ترامپ قرار دارد
🔴
مدیرعامل «پاوراس» می‌گوید بخش دفاعی خصوصی پاکستان «در حال ظهور، اما هنوز نابالغ» است و این باعث می‌شود شرکت‌های آمریکایی سریع‌تر حرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/147888" target="_blank">📅 16:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147887">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9l5zkii45iHyQltlyyACE4FpKsSNjWm4-qJrJGBRffKWcmMZD5SBj3ItHUnpOHcXsmpXSRYfzf2vFv15zzL5ULMdCqCG9Nw2je5fLS8tyhbsk0MA3hes7uBOdVaAAk1lunv5RwCpr6vuPy4-JyFG9fwqRCRihWvgtNXiGT4u67WbY-lDomWS_wuG1NXMOaeWOP7Pv_EDRnizku2c0cV2iKug9wr15IwlKBOGTdbdBbeeWtj8s1LTlex-a6FgcSSm23MsKLSWOqBH1Ci_mm9FPWewKm3rQkIGAQ4XGqc_ABNsLTLKxQZ8rJe0rSrHR9hAmjEnaQVGaD2Ew3wMH-emQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت آیفون ۱۸ پرو تو کشورهای مختلف چقدر خواهد بود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147887" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147886">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMlHwiy4MGOq3Jba-mLqpQ9sK8X1-FBW5d8tsVGfj_2DyOOU3166YN44ziuADbuVRyA8lcAUvQDNrSkL9uEOAJf0miq1GedR28ujQ9E0dgs-JDkS9nC5Czu4nNFR_X_9bABMJXIniVharRrvvQfb0tS9BKbwBUhRULDTFtAF7JwBQ755NAUoAv23ohfr5ICaAg59eo0g93LWH9YP8ok5FnmZFogMt-50oujiC9Xc5OGlvqSknPWrtiqOLPXZvNLfremaecXWmj3EUmxHQfVythFH1AY-R6oT7uD6PbTkmuTKPo_XmWm7DnygURyZ4j77c02bjEvDBxUnXrH8DwvoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی قبل جسد پنج زن و مرد که گفته می‌شود قربانی یک قتل عام خانوادگی شده بودند، در بلوار سیمون بولیوار تهران کشف شد.
🔴
اجساد این افراد در گور دسته جمعی درون یک چاه عمیق دفن شده بود
🔴
عامل این جنایت دستگیر شده و پرونده برای رسیدگی قضایی در اختیار مراجع مربوط…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147886" target="_blank">📅 15:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147885">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/147885" target="_blank">📅 15:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147884">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/og3OhvfBzqpJT9_itnnkkK50l2YAb_oCHIc93CTDJsTcw2xrsHTzUdYix9wQQGR4Vqu-MJ_jKYZYkPwXE0ts0iUipl-VtiLv_tGiONctipnmVlA6a2g7y9GMAbzmqksnd-VY5kYuEe46rVu-jxZkIY-8OsWWY92ujQFp-oZ2Q8tr_WW-2aAVumFTaCd9UCjyVHJCSMdSyhXJuczJN-NrYuDUfIsR4wwIGwYLTl70WxwUrMEZjxGSbffx8JOmbOZKoFiUTW7hXjQUjP-eDUtyjia5Fnlgc2Z0Mj-JZVPlzk5X2oxYCxOFeVRk_-lvfKV-TMNuOqyjX1MEd9k9IeHtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت: 103 دلار
🔴
امروز نفت برنت 2 درصد کاهش قیمت داشته و به 103 دلار رسیده است.
🔴
قیمت نفت آمریکا هم به 100 دلار کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/147884" target="_blank">📅 15:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147883">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سپاه: رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش امریکا در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/147883" target="_blank">📅 15:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147882">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: جنگ با ایران و سایر گروه های شبه نظامی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/147882" target="_blank">📅 15:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147881">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96265f0275.mp4?token=PyFumLwgTl9VG0Zu_vctV5arch3mhTPRLFHFaDEp5KcoGDROAbh-csJB-ER-XvTZ8PtSdgQy13E2mJyiPgjB1gsraMn2EfHm5os4a4nhlmNavriR7PI4sSrNa5rFm-7D0iEMfkRZp2G1M6eGwLAqxMA8O5OXYeht2R9XilRS5kMyAEakQZnEeNcxpR7zYJ3OB5kCL95I25DqCSY0xJwFKQsW48hXnR7jqvjYmWTzxOHFudiTZwL200afo-tMYJfXL1KlghlwtdjQ__wsFRSY_SLP_NCdpu6GH-dgde_fd8NzKMVPaXM9pXVn-I8sTfWIb_BZ3XtICTtcCTJcWbIprA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96265f0275.mp4?token=PyFumLwgTl9VG0Zu_vctV5arch3mhTPRLFHFaDEp5KcoGDROAbh-csJB-ER-XvTZ8PtSdgQy13E2mJyiPgjB1gsraMn2EfHm5os4a4nhlmNavriR7PI4sSrNa5rFm-7D0iEMfkRZp2G1M6eGwLAqxMA8O5OXYeht2R9XilRS5kMyAEakQZnEeNcxpR7zYJ3OB5kCL95I25DqCSY0xJwFKQsW48hXnR7jqvjYmWTzxOHFudiTZwL200afo-tMYJfXL1KlghlwtdjQ__wsFRSY_SLP_NCdpu6GH-dgde_fd8NzKMVPaXM9pXVn-I8sTfWIb_BZ3XtICTtcCTJcWbIprA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ فقط تضعیف شده است
🔴
توانایی آن‌ها برای عملی کردن این هدف، اساساً به‌شدت آسیب دیده است. ما وظیفه خود را انجام داده‌ایم، اما هنوز کارهای بیشتری برای تکمیل باقی مانده و آن‌ها را تکمیل خواهیم کرد.
🔴
ما حماس را از بین خواهیم برد. همچنین ابتدا رژیم ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147881" target="_blank">📅 15:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147879">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLcHkJIeK19gDWR_xn6KrqG3k4vhYsQAn4E_n-UVONXbjuFZlC-skXfIO4XIRWjVtoqssAhOMxq2nEuWjXJVfea-gmgQ1p57FWQuLR-fMhOgB-_yDhJgFmZn-exFYcK_PFYkLxvpLRwKaoSh0cLhjge-mt5V9_1U-Wg9r9yxiHpzyeHB3DpDkjucvCuowRdQiowhG333qluzJNj9fe1NEj99xrkAW9v1pPyrXxX7jBSpKxn9H0_NzF5Nc601LhLOMpX7fjaSJSSZ-re-rtw1m7Mh21aBXvw3Nx0K6fqA2ITsJlxjvae8ygIRnTKmwpZfCh65EF01n2FNcu03KxtOOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krAmOBZVvJeShmRK-qM5T8Y0-0zV1BcUd-vA8aJ9avyqG7n-8bbKkDf8C3JW3dHz9eWNF5XGkmDjgv0SOSQPv7HyjW0HJNrvHjaWaOMx6GcZOUhUEI0dWIvGKFYFvCSh2aR-3ML4Fxg_tA4I4YznLAvg05hB4VZfxwphY8q8Bw8ZBIHZ8MJYFmVFqDt74a8UVT30qCX1MEtu0P1m4oxCEPLNgXbR6QYYAf0vG1d2n-QcJ9Mmx8agCXQ6yeCIM5umg1LM3i2MRsATkrn8ez0OKFQFZQDfsOkSkevP5FQsXZ7G6-8CwmfYEQV8jqIPi2sD5vC-IfDRmWrKozWPeXyw8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فعال شدن پدافند در شمال کرانه باختری
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/147879" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147878">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1vwFNTmHYA4S_xUPXKf3z-DqQV8Nri2c_bZSJ5Ek7krX_90hws22hdbzKoMit8uNImvtGWYC8IBQB8Nh7l71ogxDbIknwoThh74Z3FC6E9iRBmt_MHELoB7YVxRM8kb9cctRLifsWRLwiSCuFaPn8xcxVQPcLujfB_NDuULZ6-iUU_dujx_t_QaPUUiIFSY6sk9exp3FnYJd-biz6g2gIiK5g--g06elprH1vxPi6hPvW4Hf7PEd0_B172bW0hW-TDV17FmDW5U2jIQ2KAWctoRhiYC6OuPTZsRW9PFVEmVR6AUZVHzgx_qGnHaG6vf5KRFo8plXspEIsSsa-3tmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سعید آجورلو، عضو کمیته رسانه‌ای مذاکرات: آمریکا برای کاهش فشار از مذاکره مجدد می‌گوید. سخن ایران مشخص است؛ به هفت شرط مورد نظر تهران عمل کنند تا تفاهم عمان- ایران درباره تنگه اجرایی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/147878" target="_blank">📅 15:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147877">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmS9Uv--6GfBOlRjKkGKg5ysasKfUxuVWOYqUj1lqbD02lL2Up1JM_pQrFN5w0qj90_Vu3XTEz7hZ5Ufya4HxXv75T6jTrJAiJabsC1sNAb_IRQk7q4Muah2CI6NVQ1Irr3GfKZi46JYalGg1ekQ_iA9ETfZi2ieIOaVKBwAhppDvzEhVwhx_1byYAZ6ShmbYgkvVeL73ABd_88P6qNa72GzGMy8_SFJiKJdovpK8LI6o69xbFc1lD0fGIu4FZajShnYdU48g3LCWmw8dDM5deX8kVxZY10yYXVYziwAtE1aTnfjnBvR4RZwnzNNy8M16P587zU6Lr_2DGDe8LaDvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش ها از نفوذ پهپاد و فعالیت پدافند در شمال اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147877" target="_blank">📅 15:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147876">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
آناتولی:
عاصم منیر از ایران خواسته تا انصارالله یمن را متقاعد کند که به تأسیسات انرژی عربستان حمله نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147876" target="_blank">📅 15:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147875">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
تسنیم: ممکنه خاموشی‌ها توی زمستون ادامه داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/147875" target="_blank">📅 14:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147874">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دلار 227,000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/147874" target="_blank">📅 14:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147873">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euUcFw8vMb97nPUk1vvHcZH0iVmZtI7uSevPAVRlJlPy946NXLFWYFxsQL94Lrhgyw7-H0xjx2p_MZVIN1NxsXfUVp26gWgeNMKYfnXhxfT9iOJir9stp3Y8hw-V8KGfPwraBl3J--4x9dpRr_ANmEeHwmaR2ntb2Hnvt9DPsLL-4YEu_d8eVrYLW1yWt-wljECjo7dPf9kbQ69D4qirdrgHAaejzv7xBjr0iLboGdhKH5BxrL09DHq1f7AIJbLA8ncprY-HZRxT0NwdmDNNJi_FxcF5YsOsJMjX6jTeI4OKheH2A2wdOUoM-xki7h6v8abwmpQI4i9EaOxLUUIYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سوخت‌رسان سعودی از جده به سمت مرز یمن به پرواز در می‌آید تا پیش از بمباران یمن، به جنگنده‌های این کشور سوخت‌رسانی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/147873" target="_blank">📅 14:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147872">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S73vedxsSugR6unIcJk3F5gxwnIMIDvuSsruNfxF0HlG5LL0P41QCbniQkFU0Deq6kqwdUiqDIX38THejVw-Sh1-oNwl63e65dmY2NYFm7QdruuKtA74a9DS6VSDw87ea2CUcjEA3G8KATLtqFjqXWeDyNI9EMYqDnq574JhaE6zUyogo_PpOpphyCWvFnk4TBOg0cgRZHOO-RYmyIBRhfPUxYOwHf0XdTwoUy56hawOKrnrmieAV8TyGINovAhY5-5K48sEZW6s_fn0qZTW5jIH-CQzB9PuUjonqL6C6TSDtdiLzvvSZWuWa7NcQ9PMxgHVlb4dFlDz_x2BzTsgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز - توقیف تویوتا متخلف با راننده ۱۱ ساله در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/147872" target="_blank">📅 14:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147871">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کرملین: تصویب لایحه تحریم‌های شدید آمریکا، تلاش‌ها برای دستیابی به راه‌حل مسالمت‌آمیز برای درگیری‌های اوکراین را پیچیده خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/147871" target="_blank">📅 14:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147870">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: اگر‌ کانادا بخواهد به اروپا نزدیک شود و اروپا به او کمک کند، اروپا هم تحریم خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/147870" target="_blank">📅 13:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147869">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr_cs0y2zgiY-JHiILfLdNxC0Mo_9fA6KUv_gnQiRXr_BQsmPiVQIPRs_-Qe6Y0myY47dn_TmFVSolFqfYFiAQgcfim3vhBBSf_Cv09zj80cxfY5Z0WV5i2uGt8NPoXkIYai_xSRyxpkuk7vfyxY_UFJpYjVjgMwhXqKzBxzIVHFTA9hZrtbaG_pFLMXvVAYIgRb71nypu2YzsfdZXmA9ICVCSbV2__gewIkmQqfojkilCc-a-5_-tFO7AM_eGvdUULJfNHYTDZSlBevVUrEt5m5OxatG4n38iDgILdWC_QPaq06tTBei2PFkG9qdnvP2wYiZUjEAzNzJO0HncFd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۰ فروند جنگنده اف ۱۶ آمریکا به همراه تعدادی هواپیمای سوخت رسان، صبح امروز از پایگاه لاژیس در پرتغال به سمت خاورمیانه اعزام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/147869" target="_blank">📅 13:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147868">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ارتش روسیه ویدیویی از هدف قرار دادن 1 قطار اوکراینی در استان دنیپروپتروفسک و 3 قطار دیگر در بندر یوژنی استان اودسا توسط نسخه هدایت شونده پهپاد گران 4 منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/147868" target="_blank">📅 13:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147867">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رسانه The Nation: ترامپ علاقه خود را به جنگ با ایران از دست داده، اما جنگ همچنان به او علاقه‌مند است
🔴
اردوکشی او به ایران یک شکست تمام‌ عیار سیاستی بوده که اعتبار دیپلماتیک و نظامی آمریکا را تکه پاره کرده
🔴
جنگ برای ایالات متحده بسیار بدتر از آن چیزی پیش می‌رود که قابل تصور بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147867" target="_blank">📅 13:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147865">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
اتفاق وحشتناک برای طلا
‼️
‼️
👇
👇
👇
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/147865" target="_blank">📅 13:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147864">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
گاردین: عربستان سعودی از مصر، بریتانیا و پاکستان خواسته است به صورت فوری به جنگ با حوثی ها بپیوندند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/147864" target="_blank">📅 13:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147863">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
👈
صرافی کوینکس رسماً اعلام ورشکستگی کرد تا پنج روز دیگر زمان دارید دارایی های خود را از این صرافی خارج کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/147863" target="_blank">📅 13:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147862">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db56a3dd02.mp4?token=WCGSPwpT6IRIj2D7W2CCjtQCs-6BKDSE1fn-5SaDEsdm5h2srFaIIZcyzOPxcItzy81xQg6ZALeiBWV5oAkH2FJhuKVCCdKKQjfWMEz-V9IuE4U5Bb-qkjbnRz67cabxW6wL0FRqoQEigmntD33dOoVhWeiKYxBBjqM_iCKT0lP0fa_FJ1e-aJbHme5bRvgGoLBBsfXpnajpgNfK7qLtlE-ozl0DSuHsCAZXPQZK0p1_G79MuJJo6UA_A1onsut0B_7kcu2ZmBlfi_nbU1ojCZD-1HRKajYpTVCIwJDF9UYaoOy76ShoYseWppmhtZwobMAtHv3mr4a5VG1EWAZA2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db56a3dd02.mp4?token=WCGSPwpT6IRIj2D7W2CCjtQCs-6BKDSE1fn-5SaDEsdm5h2srFaIIZcyzOPxcItzy81xQg6ZALeiBWV5oAkH2FJhuKVCCdKKQjfWMEz-V9IuE4U5Bb-qkjbnRz67cabxW6wL0FRqoQEigmntD33dOoVhWeiKYxBBjqM_iCKT0lP0fa_FJ1e-aJbHme5bRvgGoLBBsfXpnajpgNfK7qLtlE-ozl0DSuHsCAZXPQZK0p1_G79MuJJo6UA_A1onsut0B_7kcu2ZmBlfi_nbU1ojCZD-1HRKajYpTVCIwJDF9UYaoOy76ShoYseWppmhtZwobMAtHv3mr4a5VG1EWAZA2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری شدید در جنوب سوریه و کشته شدن ۳ نیروی امنیتی
🔴
الاخباریه: درگیری‌ها بین نیروهای امنیتی سوریه و یک گروه مسلح در شهر «صنمین» در حومه شمالی استان درعا، بامداد امروز پنجشنبه آغاز شد و گزارش‌هایی از تلفات مخابره شده است.
🔴
شبکه خبری العربیه گزارش داد سه نفر از نیروهای امنیت داخلی سوریه در درگیری با افراد تحت تعقیب در صنمین، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/147862" target="_blank">📅 13:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147861">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ درباره اروپا: چرا باید بار مسئولیت این همه کشور در اروپا را به دوش بکشیم؟ ما بار مسئولیت کشورهای اروپایی را به دوش می‌کشیم
🔴
تنها کاری که باید انجام دهیم این است که بگوییم: می‌دانید؟ ما دیگر با شما تجارت نمی‌کنیم.
🔴
ما دیگر به هیچ چیز از آنها نیازی نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/147861" target="_blank">📅 12:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147860">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پولیتیکو: پیشنهاد اورزولا فون در لاین برای تبدیل کانادا به نخستین «عضو وابسته» اتحادیه اروپا، پایتخت‌های اروپایی را غافلگیر کرده است.
🔴
دیپلمات‌ها می‌گویند این ایده پیش از طرح، با کشورهای عضو مشورت نشده و هنوز تعریف مشخصی از جایگاه «عضو وابسته» وجود ندارد.
🔴
کانادا نیز با احتیاط به این پیشنهاد واکنش نشان داده و مقام‌های این کشور گفته‌اند تمرکز آنها بر تعمیق همکاری‌ها است، نه جایگاه پیشنهادی جدید.
🔴
مارک کارنی، نخست‌وزیر کانادا، قرار است امروز در پارلمان اروپا سخنرانی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/147860" target="_blank">📅 12:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147858">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پکن: چین تحت فشار آمریکا همکاری‌هایش با سایر کشورها را تغییر نمی‌دهد
🔴
وزارت خارجه چین اعلام کرد: همکاری‌های تجاری و اقتصادی پکن با سایر کشورها بر پایه برابری و منافع متقابل است و تحت تأثیر مداخله یا فشار طرف‌های ثالث قرار نمی‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/147858" target="_blank">📅 12:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147857">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره: شمار کشتی‌های عبوری از تنگه هرمز در روز گذشته به ۳ فروند کاهش یافت
🔴
داده‌های اولیه ردیابی شناورها که امروز پنجشنبه منتشر شد، نشان می‌دهد شمار کشتی‌های باری عبورکننده از تنگه هرمز در روز گذشته (چهارشنبه) به تنها ۳ فروند کاهش یافته است؛ رقمی که نسبت به ۱۲ فروند در روز پیش از آن و بسیار کمتر از میانگین ۱۰ روزه (حدود ۱۷ فروند) است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/147857" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147856">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445b3dec5a.mp4?token=L6A-0N6YXZFpMeQukPFg7t4bl-StGIguhDAHKhl_xRuDdaptHK46-ntCGlSbHKL5nnNerrUEDeaRQVStsIYfPRzYH9z8eyWszUZpwCKcS8VeqSFSF7GnSkAXhZk7TVFp-zvH8xVJtVuuGpO4ZgvYPyeIggmL-UDpIczfn3LK-W86xRIgg5EV5Y23y-G2zqTLNpXic_Q2LGvFFy8QMj6YkQLoBeLJHaErlPcoCuBcZbsX_wfd1nOAoU8m5bTMJ2UdcZzqBJr9oe0FVy3j9xsozTtGpNpzWZUedvJXVRMUMgh4j-XlSaGsdOaZJR_anZj12mK1tZ7yJ2RDuIbnutfhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445b3dec5a.mp4?token=L6A-0N6YXZFpMeQukPFg7t4bl-StGIguhDAHKhl_xRuDdaptHK46-ntCGlSbHKL5nnNerrUEDeaRQVStsIYfPRzYH9z8eyWszUZpwCKcS8VeqSFSF7GnSkAXhZk7TVFp-zvH8xVJtVuuGpO4ZgvYPyeIggmL-UDpIczfn3LK-W86xRIgg5EV5Y23y-G2zqTLNpXic_Q2LGvFFy8QMj6YkQLoBeLJHaErlPcoCuBcZbsX_wfd1nOAoU8m5bTMJ2UdcZzqBJr9oe0FVy3j9xsozTtGpNpzWZUedvJXVRMUMgh4j-XlSaGsdOaZJR_anZj12mK1tZ7yJ2RDuIbnutfhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرادویسی، تحلیلگر اینترنشنال :
بر اساس این 3 تا خبری که تو این هفته منتشر شده، بنظرم آمریکا داره خودشو برای یه حمله نظامی بزرگ به ایران آماده میکنه :
🔴
حرف ترامپ که گفت شاید قبل از انتخابات یا بعدش، کار رو با ایران تموم کنم.
🔴
صحبتای ونس که گفت شاید تو یک یا دو ماه آینده، درگیری با ایران وارد فاز جدید بشه.
🔴
جلسه بردکوپر، با فرماندهان نظامی اسرائیل و کشورهای مختلف.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/147856" target="_blank">📅 12:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147855">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به نظرتون کدوم بیشتر رشد میکنه؟</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/147855" target="_blank">📅 12:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147854">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پهپادهای اسرائیلی در ارتفاع بسیار پایین بر فراز منطقه بقاع شرقی و رشته‌کوه‌های شرقی لبنان در حال پرواز هستند.
🔴
پرواز پهپادها بر فراز روستاهای سرعین التحتا، سرعین الفوقا، نبی شیت، صفری، الخریبه، جنتا، یحفوُفا و الشعرا گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/147854" target="_blank">📅 12:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147853">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjmssKPnFhRrJfhTohR5zfi3tIEI-d7_V_ONm0S_3-YlaXI7qq_fYct7VaOqOQ5kbGInaKUxas2QrpmizPu6AEr0S5ao1ae45EXEd0Hpetg8Q_GTfRGq9XBVZNaB5Mc_W0cg8j6ggJyIW-SPfCeu_1UngE7hYb00Tstwtn5Ilgi4T8fyiDsfuzIuYEopWW92bnfPz1lhyhHKJnz207UvwZ-Y0zddIaWF0NflM0vRIvcNdudQW2KLFS60aDmYk4BUL3X5ESdjIBUYQ0mld09ZPcwiSPypDrRbAd2JA6foBz8iVYqfaiHtVLaYk-8y2tH-ebO3o_v5p7f7WSQukNH1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حملات هوایی عربستان سعودی به مواضع حوثی‌های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/147853" target="_blank">📅 11:57 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
