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
<img src="https://cdn4.telesco.pe/file/YPO5RjznOiyMGhISp0pVl4Edv01brtpJVfeHftxgiTe0kT8kFfxtsRmWLznrpyDLdSZwTbngc9HpnMzzPOpjt73f5rO_jhVrmrSQf4L9ZsUTnKLdV4PERYJdhfKaHJofvo7FKOyx4x-NdEpGZdV7sDUI0RToU3KQjgt4OnKSEZTxmDKes5Mu5uG8YP6KNk3K_M56_MBpw7A-e1CD4-6wQqQtArhCUC3fKPPp1r0RnYsg599nsTgE-zsxbFxJiNWlK8t3eFrfBX8mD9ROsTjby5gfK69Fdl5d4J_qvUk-H1E9snK8Ub2Ig3HZUHNDBIw5evxehtashM9vMR5kALTx9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-127132">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کویت: رفتار ایران نشان داده سازمان یافته حمله می‌کند و ما مجبوریم پاسخ ایران را بدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/127132" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس درباره نتانیاهو: نتانیاهو کشوری را اداره می‌کند که آشکارا شریک بسیار نزدیکی برای ایالات متحده بوده است.
🔴
اما حتی زمانی که شریک نزدیک بوده‌ایم، گاهی منافع ما کاملاً همسو بوده و گاهی منافع ما ناسازگار بوده است.
🔴
نتانیاهو به شدت منافع کشورش را مطرح می‌کند. گاهی این به معنای هم‌راستایی ماست و گاهی به معنای عدم هم‌راستایی است.
🔴
آنها در بسیاری از جنبه‌ها شریک خوبی بوده‌اند، اما ما همچنین باید بر آنچه به نفع آمریکا است تمرکز کنیم. و جایی که این منافع متفاوت است، متأسفانه برای اسرائیلی‌ها، ما باید طرف مردم آمریکا را انتخاب کنیم، که همیشه این کار را انجام می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/127131" target="_blank">📅 15:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
یک منبع دیپلماتیک عالی‌رتبه به الحدث:
ایران پاسخ خود را دربارهٔ پیامی که وزیر کشور پاکستان تحویل داده بود، ارائه کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/127130" target="_blank">📅 15:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be3c800123.mp4?token=f8XK-urS6MfhQxQsTEh7kjwQLpJu_j44pOc84DO80rYxL0eslp9KfrWxdWHeN_S0kguk3tloGue8Ukj3jufOxRUMawBslcAENFuQE1Kp5TQ0w9uMXlqHb91NwaNS32gMERM2i_ErjAq1JZEJBWHFR5xbWj_O-NZQmnZm-bV9A4ay5LmzLI0MSBOSam4knXkg7ZzvMEvX4XmYsOwa6qAjuyOLhc56scT3MntGUP1Mwdj8mcoOrmBL0ZAorVTV_iL1vfy11Q6nhk-DL-ohk86jvWQIgmOdW47h6qIKDQzmA25tmRr7Yd7MYTTQEk-rHDXqBES6FAuTApRySVx0v6MECoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be3c800123.mp4?token=f8XK-urS6MfhQxQsTEh7kjwQLpJu_j44pOc84DO80rYxL0eslp9KfrWxdWHeN_S0kguk3tloGue8Ukj3jufOxRUMawBslcAENFuQE1Kp5TQ0w9uMXlqHb91NwaNS32gMERM2i_ErjAq1JZEJBWHFR5xbWj_O-NZQmnZm-bV9A4ay5LmzLI0MSBOSam4knXkg7ZzvMEvX4XmYsOwa6qAjuyOLhc56scT3MntGUP1Mwdj8mcoOrmBL0ZAorVTV_iL1vfy11Q6nhk-DL-ohk86jvWQIgmOdW47h6qIKDQzmA25tmRr7Yd7MYTTQEk-rHDXqBES6FAuTApRySVx0v6MECoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام:
نیروهای آمریکایی یک نفتکش را در خلیج عمان در ساعت ۱۱:۲۰ شب به وقت شرقی در ۱۰ ژوئن غیرفعال کردند، پس از آنکه این کشتی با تلاش برای حمل نفت ایران، تحریم علیه ایران را نقض کرد و این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی غیرفعال شده است.
🔴
فرماندهی مرکزی ایالات متحده (centcom) علیه نفتکش m/t jalveer که پرچم گینه بیسائو را داشت و تلاش می‌کرد نفت را از ایران از طریق خلیج عمان حمل کند، اقدام کرد.
🔴
یک هواپیمای آمریکایی دو موشک هلفایر به اتاق موتور کشتی شلیک کرد پس از آنکه خدمه بارها از اطاعت دستورات نیروهای آمریکایی خودداری کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/127129" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0R1AT6hZLOup7IuQKDuXUs9et6oy3uPZVNuOLK91AoGtpeoBDbqtv38KF6oUR6F301LPP6jkFtTlZ5COQWMIsHyO0J_z1Lwv0NS1SCNERZJznVSssIKHs_sUKdqS2VnfTeGGCf__09ZZs_MyMowCXakwsuGcBoo_zDJoABxz2152HaUJThSo1I2rxtCK9KBOIpWWvlXsFCEvgYk4drRf4l7ZkUzw-EdEbGIt67QeU6IRs_f7E9V2zNaKkPSbMoRNnljNrlZ_jD3EqVQME6Xou18U1-m_rve5S5ylkn2b7y291QzdJzivCljf1eK5GlBzARsHETSewdqqw56CUE48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/127128" target="_blank">📅 15:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رئیس جمهور لبنان: با وجود فشارها از مذاکرات عقب‌نشینی نخواهیم کرد و تا رسیدن به آنچه به نفع ملت ماست، به این مسیر ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/127127" target="_blank">📅 15:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcP2H0pneYDY6WavzgTWlK8WxN9ryUc2IWvn8EihcISlWXH6p-C4sZchfIG-Ri3pdQC9QoThXyVb2QcUpjOHaIrS57y6lqHYTeY8wW6XPubId1LmjNSYOdTetXWklkmh2z-lqWJzOtyHyjpFjotV5Cji_iSmS2w_eYFIvlryr6SH_3RTKZC-tFm8edTLPGWIVuFoBo1GpF2TWjLITKExbk9iu3WNN8HAQzs4Yi9p63bhQ74mRm574poB6WLE80nQ1Mx1K5wA9FT9fAiuOgUj8LQnJ5wxhUXMNjYoF3FIYEgrQ6n5lZc3B5Jhm25qU-8adgl_9pwJTyPd_xsOxfPfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۲.۰۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/127126" target="_blank">📅 14:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرنگار صداوسیما: لحظاتی پیش صدای انفجار در محدوده سیریک و از سمت دریا شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/127125" target="_blank">📅 14:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpgr6DFJvrn1_9zY8lWiBU5YowkLPmTvxAZv2GPuOiWmLqImFcampRGjYZKTsnF0AIa1DSMZ9tJWzvFfOCwWJ7_vxmrx0gg_cYsDwwKQcCaRQRXKj2FoTBwDS-xaiRDGmFjaJNc4RGP-Dow0vBYwrqpJ3iPCVqgLOQuy5KZXOOZGhdXBfhwDgubc3KrimEldR4AQ8Wu3ef7H-3MnPXgDjTAIpLxh1o7a1Oi6O7eCC26zsSgUoTwYT3hqRlgs6_E0QedwRDaxLrisU-ya001M7XOI74VE4ztGkwvFBJ1VzuQFtoqRwFtwKECQr4zbXRN5Nn67HETH8fkCIrRC1pdYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع بریتانیا، جان هیلی، استعفا داد و اعلام کرد که نخست‌وزیر کیر استارمر و وزارت خزانه‌داری منابع لازم برای دفاع را در برابر تهدیدهای فزاینده تأمین نکرده‌اند.
🔴
او در نامه استعفای خود گفته است که «طرح سرمایه‌گذاری دفاعی» پیشنهادی «به‌طور قابل توجهی ناکافی است» و هشدار داده که این موضوع می‌تواند آمادگی نیروهای مسلح بریتانیا را کاهش داده و این کشور را «کمتر امن» کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/127124" target="_blank">📅 14:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خبرنگار الجزیره: یک پهپاد اسرائیلی یک موتورسیکلت را در شهر حبوش در منطقه نبطیه در جنوب لبنان هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/127123" target="_blank">📅 14:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گفت‌وگوی وزیر خارجه ایران و مسئول سیاست خارجی اتحادیه اروپا درباره حملات اخیر آمریکا
🔴
عراقچی: این اقدامات آتش‌بس را بی‌اثر کرده
🔴
مسئولیت پیامد‌های خطرناک آن نیز بر عهده واشنگتن است
🔴
انفعال جهانی، موجب افزایش ناامنی جهانی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/127122" target="_blank">📅 14:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا: اروپا باید در صورت تمایل ایران به مذاکره، تحریم‌ها را کاهش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/127121" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9650d1637f.mp4?token=XRdMclMZnUf6NL2vcj4cupqSZXrR-ra1qBoa2e5paQsyJOYlw6Zs70cEv-7EzfSowFU3wpHptHrucicOs2bh8OUtvCYy3c3oJ_7XjIsx268oJ_68AMfk4wzmzt8H3hAI_RSCKAn3DyPsbaM6MSrh_J096F8WDmb-7H15Y0r05xOrxiSg6Cx-mq8SuOlYMKwXd7-dLOtagbDpYTtFqHyOZOIOAhnBOVEXrnSh3tdFp_uNS1nDzolGhQi9ntpYtiJhIGVUMNVd7wUez7pdlpJ0yVOCTFTKSdq6aQ2VT49o0XMzsItEuoY42ufKOAfMrJIS-Q9F6ngiqMzDFuKIIYV_K0nplzW_EdCOVcNkMa-OZLNSBDryOT3tsXf0xREuCW9meOmmskPQ-FVqjWlf6uCNNqTtaPzYGDFF5JAlBLTquYN7c7BntF77lYG65Q8x2wuXpOTmTt09kPwxGMVnDJVHUkgqC9v1n2tM4fgPOOmZ7b7eWf4GRM8-gek5PmDa95pdJ-UfNK4TBgh4B2g9onjQnhfk1ew2Nk9gDrM49REUto6ZXEfQYr4GN_fPESFn4GrSoVcg4DJmLY6NHhPCOifs-BonK2xSCOUw6E47_zGBJsrkWiald20ijTdFs0QIVO_pZ9LTWN3s1VNooCPPex_dIA6qzr40ldfc_WB7OUM9Nnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9650d1637f.mp4?token=XRdMclMZnUf6NL2vcj4cupqSZXrR-ra1qBoa2e5paQsyJOYlw6Zs70cEv-7EzfSowFU3wpHptHrucicOs2bh8OUtvCYy3c3oJ_7XjIsx268oJ_68AMfk4wzmzt8H3hAI_RSCKAn3DyPsbaM6MSrh_J096F8WDmb-7H15Y0r05xOrxiSg6Cx-mq8SuOlYMKwXd7-dLOtagbDpYTtFqHyOZOIOAhnBOVEXrnSh3tdFp_uNS1nDzolGhQi9ntpYtiJhIGVUMNVd7wUez7pdlpJ0yVOCTFTKSdq6aQ2VT49o0XMzsItEuoY42ufKOAfMrJIS-Q9F6ngiqMzDFuKIIYV_K0nplzW_EdCOVcNkMa-OZLNSBDryOT3tsXf0xREuCW9meOmmskPQ-FVqjWlf6uCNNqTtaPzYGDFF5JAlBLTquYN7c7BntF77lYG65Q8x2wuXpOTmTt09kPwxGMVnDJVHUkgqC9v1n2tM4fgPOOmZ7b7eWf4GRM8-gek5PmDa95pdJ-UfNK4TBgh4B2g9onjQnhfk1ew2Nk9gDrM49REUto6ZXEfQYr4GN_fPESFn4GrSoVcg4DJmLY6NHhPCOifs-BonK2xSCOUw6E47_zGBJsrkWiald20ijTdFs0QIVO_pZ9LTWN3s1VNooCPPex_dIA6qzr40ldfc_WB7OUM9Nnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : ما تو همه جبهه‌ها پیشرفت قابل‌توجهی می‌بینیم
🔴
هر هفته صدها نفر از نیروهای مسلح دشمن رو از بین می‌بریم
🔴
همچنان چالش‌های دیگه‌ای هم پیش رو داریم
🔴
یه چالش ویژه هم موضوع ربوده‌شده‌ها (گروگان‌ها)هست که روی اون کار می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/127120" target="_blank">📅 14:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127119">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=BATnC8PB5BT9kcGrRkIZC2oyaUIDEwil-8i0uE0LOjhfq_Gc28xyHpqRFCvKfdH0E7SoXOWHg7rhXxmMgpXIH_g_jU1elEXuU5pgtviAFFbgcDOPte94DAZ9DAIkgGiJf0TuJ3CSekfCtKzdEoWIwMuTOV1vLMD-b5buI2fClZtG6U7lJ4Cu-Ie0aJ8vGnO4yk3EBMQE6t4URJ6Fkra7aFY_0I4bR6maERx4auim2fBShCwhvxADdrdPwb9WD-fY1M_XvqRT20pean7zh-sverjMbXZQLDK1OuGdR0AqHBcaBcck2_aWXZBVrNDYCwuO-orYMplJioS-ULtE32lYLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=BATnC8PB5BT9kcGrRkIZC2oyaUIDEwil-8i0uE0LOjhfq_Gc28xyHpqRFCvKfdH0E7SoXOWHg7rhXxmMgpXIH_g_jU1elEXuU5pgtviAFFbgcDOPte94DAZ9DAIkgGiJf0TuJ3CSekfCtKzdEoWIwMuTOV1vLMD-b5buI2fClZtG6U7lJ4Cu-Ie0aJ8vGnO4yk3EBMQE6t4URJ6Fkra7aFY_0I4bR6maERx4auim2fBShCwhvxADdrdPwb9WD-fY1M_XvqRT20pean7zh-sverjMbXZQLDK1OuGdR0AqHBcaBcck2_aWXZBVrNDYCwuO-orYMplJioS-ULtE32lYLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حملات امروز اسرائیل به لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/127119" target="_blank">📅 14:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TA1UA1joihq2lfmk7mAHj2orwD64YZNLFyEnQ8_trFkqt6VsapDSO5Q878ozS-r7c5n79BNQyiha9SjSTCtFy4T2VELu3JVwHE7EvhQLc0kYlYrzEF-NZR_ay5rePutHg47Ou20e1YFsXIfHViTKsLu0Lf3Iw4yiON235oUkTYBf-kFlULgc67ZwUokhFVk-xOaVB7ZmZ57aq3LB-Y_neDGggcNfjjLTq3Rm_I8Efq6V_MOhzbdHQOzKGstFHuQjX0TG75UPo1naL11-W6p4Cy9qgSx8LcxlWwPyskxnL8u08NOddaIJGOdeWyj1f86x7UFIu02UdDeCch4J6XmgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد ، مارشال محسن رضایی: رئیس‌جمهور بی‌ثبات آمریکا تصور می‌کند که بمب‌ها می‌توانند او را از باتلاقی که خودش ایجاد کرده نجات دهند. اما موشک‌های ایرانی او را حتی عمیق‌تر در آن فرو خواهند برد.
🔴
واشنگتن باید بین پذیرش شروط ایران و از دست دادن آخرین ذره اعتبار خود در جهان یکی را انتخاب کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127118" target="_blank">📅 14:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
صدراعظم آلمان فریدریش مرز:
ایران باید برنامه هسته‌ای خود را به طور قابل راستی‌آزمایی و دائمی متوقف کند.
🔴
امنیت اسرائیل و کل منطقه باید تضمین شود؛ در غیر این صورت، صلحی در منطقه نخواهد بود.
🔴
امروز، ما در حال کمک به شکل‌دهی نظم نوین جهانی هستیم که در آن اروپا جایگاه قدرتمندی پیدا می‌کند، تا اروپا بتواند به عنوان نیرویی برای آزادی و شکوفایی، برای صلح و دموکراسی در جهان باقی بماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127117" target="_blank">📅 14:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت خارجه کویت: حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/127116" target="_blank">📅 14:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تسنیم: ادعای رسیدن به متن نهایی برای تفاهم بین ایران و آمریکا خبرسازی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/127115" target="_blank">📅 14:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رئیس سازمان اورژانس کشور: ۵ نفر در حملات بامداد امروز مصدوم شدند که ۳ نفر در تهران و ۲ نفر در هرمزگان بودند.
🔴
همه مصدومان پس از درمان مرخص شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/127114" target="_blank">📅 13:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت خارجه هند: ۳ کشتی هندی هدف حملاتی قرار گرفته‌اند که توسط نیروی دریایی ایالات متحده انجام شده است.
🔴
۱۳ کشتی با پرچم هند در تنگه هرمز گرفتار شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127113" target="_blank">📅 13:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه: ایران و آمریکا باید حملات را متوقف کنند و برای پایان دادن به مذاکرات به میز مذاکره بازگردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/127112" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127111">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTytdOSaQjibMuCo0qS8A5S0bMXtS3G-a0k0oNfgeTFLIIS7I0_oMhTfTqWqzOsdRr5STEBZMDyMaVr0QRoK6xhGTVc4aV1L23US1nNRlYC1ssldGfjD8rA9RYODcoSgK8jfFQzEsW1fE-85JnXq70ZeeMZqJkjbVZdrFJHrD09NZef4Tpk-yDRB3kMUqqe-iQrgr57z2aorqtJreM0V79y1VLAKChs6QWECiDhtLWALiyfn0l62OwDpmKwyvDoOLyHhc74JxnXwC3IbuY71LuOomzgO3uam2YwQphXCv2EDO6xL-RkITyQc2mjPuQ3Q4WeW0yEa0yh7CtL9OKmVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: هیئت قطری امروز صبح پس از برگزاری مذاکرات شبانه با مقامات ایرانی که با هماهنگی ایالات متحده انجام شد، تهران را ترک کرد، در حالی که حملات آمریکا به ایران در همان بازه زمانی مذاکرات شبانه صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/127111" target="_blank">📅 13:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127110">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd611e5ea.mp4?token=vDsHZzmobBLc6l3ROEBsqzKjzD4ekXHcpdkuIlPuXV0I10hrNJm56wWMgAlTX7Q0STbE7QweGqvWUlEqbJFbBnR5NdwTc8p5xOfglmoJgwLtS6Z9DJ9tu0Npw1eR7azf4l5TUzA_tkcqj2wx4yYotfVudRZy1kxIEy_BUC1etUWlaK1Fs52Y5izyZu-X7ob5QfnwZUI-uyIpaGksl1sq4sgqG6dYQRDLrPp8dKSb0Q1p6jw_JgQwVIAZjuyb0MtEAGnyesn0sSJsZt9qWl4R0SwYsStcrEx0EeQ-roi5a-5bS8VOG1uMStWqCKy1uWVV0IgscjZ1D7auxGZD_ELktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd611e5ea.mp4?token=vDsHZzmobBLc6l3ROEBsqzKjzD4ekXHcpdkuIlPuXV0I10hrNJm56wWMgAlTX7Q0STbE7QweGqvWUlEqbJFbBnR5NdwTc8p5xOfglmoJgwLtS6Z9DJ9tu0Npw1eR7azf4l5TUzA_tkcqj2wx4yYotfVudRZy1kxIEy_BUC1etUWlaK1Fs52Y5izyZu-X7ob5QfnwZUI-uyIpaGksl1sq4sgqG6dYQRDLrPp8dKSb0Q1p6jw_JgQwVIAZjuyb0MtEAGnyesn0sSJsZt9qWl4R0SwYsStcrEx0EeQ-roi5a-5bS8VOG1uMStWqCKy1uWVV0IgscjZ1D7auxGZD_ELktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط بالگرد ارتش پاکستان با دست‌کم ۲۲ کشته
🔴
ارتش پاکستان اعلام کرد: یک بالگرد MI-17 ارتش دیروز به دلیل نقص فنی در کشمیر تحت کنترل پاکستان سقوط کرد و تمام سرنشینان آن کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127110" target="_blank">📅 13:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127109">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کرملین: از واشنگتن و تهران می‌خواهیم خویشتنداری را رعایت کنند و به مذاکرات ادامه دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/127109" target="_blank">📅 13:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127108">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سه دریانورد هندی پس از حمله آمریکا به کشتی M/T Settebello مرتبط با ایران در خلیج عمان در روز چهارشنبه، جان خود را از دست داده‌اند، گزارش CNN.
🔴
دهلی نو نماینده موقت آمریکا را برای اعتراض احضار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127108" target="_blank">📅 13:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127107">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d7ae260d.mp4?token=pBoouTEHQtEnZhiz98cVsJPd15_yvhZ-piNHDJ_7vWJ0G7ReIz6k7f-6DVWcWWBaua_PDHV2CNQ2OTJHG5crF8xKH4DfiFsmO2VJMs0k8ocGfdDtZmWjPLvxaYNlKGhueAFb1DAL3D25qColujU4eM3EEyZ51R-oHsPxVJE0KK2Tawxh9uCcF4HLzexBYTwzSZ6fCsrJMaBkjN3omqOTFx4KDEwsucJ6DCPt2Zc3Ly0ThTndSzZdbnQtSiS0RFv5v_55UMwF4_v5gDkyGzEhfya6R9pTWD18kchTbcGzMZNfKb_essnjq5d6o-H0gnDA2r7ONQ3SUeytRutnsgfB5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d7ae260d.mp4?token=pBoouTEHQtEnZhiz98cVsJPd15_yvhZ-piNHDJ_7vWJ0G7ReIz6k7f-6DVWcWWBaua_PDHV2CNQ2OTJHG5crF8xKH4DfiFsmO2VJMs0k8ocGfdDtZmWjPLvxaYNlKGhueAFb1DAL3D25qColujU4eM3EEyZ51R-oHsPxVJE0KK2Tawxh9uCcF4HLzexBYTwzSZ6fCsrJMaBkjN3omqOTFx4KDEwsucJ6DCPt2Zc3Ly0ThTndSzZdbnQtSiS0RFv5v_55UMwF4_v5gDkyGzEhfya6R9pTWD18kchTbcGzMZNfKb_essnjq5d6o-H0gnDA2r7ONQ3SUeytRutnsgfB5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تهدید تلویحی ایران به حمله اتمی / کیث کلوگ، مشاور سابق ترامپ: «داشتن یک جنگ طولانی مدت، روش جنگی آمریکایی نیست. ما باید به روشی که در جنگ جهانی دوم و جنگ جهانی اول انجام دادیم برگردیم و کار را تمام کنیم، آنها را نابود کنیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/127107" target="_blank">📅 13:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127106">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
انفجارها در خارج محدوده شهری دزفول کنترل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/127106" target="_blank">📅 13:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127105">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzKH2XDbCUEdWJ4GGMDMboaC9_Kvm_sYNlqop6o_li6ApwskNCvSfS-SfXgXGhvlMldkcrkqoV_v6AyHF_VIJq1H0OZmI66jHQsy3DuOTbdKC4eC5awosEVDB0SouV5EDsnZZly-D7vS4oiPEY_KrF9z3h5Fyg0fEgwlt2fofcdhQha-EwoIxJm8G_dljYtD-4Qg9TZe8O8xFXmZRO6yecwEmZ4-_USj820ngcyUjcQ-Lqsqa9yZ7ankihobFYzc878Ca3OqpWGuBdRlMXnCdCSxws9mDcRDJOxs4Q2_y3t2VHgHgkvv5bzNI-QYPQ3axD_lNaQUupwl7S_PE0l0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس: تنگه‌هرمز تا اطلاع ثانوی بسته خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127105" target="_blank">📅 12:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127104">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه پاکستان: کانال‌های ارتباطی دیپلماتیک بین آمریکا و ایران از طریق پاکستان باز بوده و همچنان باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/127104" target="_blank">📅 12:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127103">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f715d743a.mp4?token=F5v8I4lZEo706UJ02G0r__L4Jwc_whczUMyovEL-2dHOrX02VG5R9E4o0QNCGl9gi3GgS9uGuUo_wUctfAFD8jbVOXCyrPGsY7fUdOfwgyR7nCTutx74PnrK87HfWFDU9qpyJA8DraU5MdQuyAsQDI-U4sJNbUDG1rNxF9Eo7WQITAK-6EKcKaniQP2wcshkeDU3xWy6dO5GEqd7C7qpnnOTlQjes1yQjfWvUxD5xHKR5X0f0Har2JJ9VbrZYR6HwJ-MUoxo6GaACGJeS6A-_9wygtyDcUQCNC2_GDdc-XZ33GPzFphGpMa93RNxKDd0coKVmlDnoH6jv8RSB0KnTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f715d743a.mp4?token=F5v8I4lZEo706UJ02G0r__L4Jwc_whczUMyovEL-2dHOrX02VG5R9E4o0QNCGl9gi3GgS9uGuUo_wUctfAFD8jbVOXCyrPGsY7fUdOfwgyR7nCTutx74PnrK87HfWFDU9qpyJA8DraU5MdQuyAsQDI-U4sJNbUDG1rNxF9Eo7WQITAK-6EKcKaniQP2wcshkeDU3xWy6dO5GEqd7C7qpnnOTlQjes1yQjfWvUxD5xHKR5X0f0Har2JJ9VbrZYR6HwJ-MUoxo6GaACGJeS6A-_9wygtyDcUQCNC2_GDdc-XZ33GPzFphGpMa93RNxKDd0coKVmlDnoH6jv8RSB0KnTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله ایران به اردن، صبح امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127103" target="_blank">📅 12:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127102">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رویترز به نقل از منابع: تلاش‌ها برای دستیابی به یک توافق اولیه بین ایران و آمریکا شدت گرفته است، با وجود حملاتی که دو طرف انجام داده‌اند. این تلاش‌ها شامل بحث بر سر مکانیزمی برای آزادسازی دارایی‌های بلوکه‌شده ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127102" target="_blank">📅 12:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127101">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / ادعای رسانه بریتانیایی امواج:
پیش‌نویس توافق نهایی تهیه شده است.
🔴
متن آماده است. دیشب نهایی شد
🔴
اگر تا امروز به صورت نهایی تایید شود، به صورت رسمی اعلام می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/127101" target="_blank">📅 12:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127100">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شب گذشته ارتش ایالات متحده با ۴۹ موشک تاماهاوک به اهدافی در ایران حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127100" target="_blank">📅 12:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127099">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
منابع ایرانی به رویترز: ایران و ایالات متحده هنوز در حال مذاکره درباره یک توافق اولیه هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127099" target="_blank">📅 12:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127098">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بررسی داده‌های سامانه‌های پایش اینترنت از جمله رادار کلودفلر، نت بلاکس و رادار ابرآروان، نشان می‌دهد که اینترنت ایران در حال حاضر در وضعیت پایدار قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127098" target="_blank">📅 12:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXBMw1swsH6gLEWW08dg_ThPV0q-txZjZBand-60wkqvkRbkVeDe2Z5OaMP3o3apAmJ_loc8p8ahAEjyuBg6gIF66sGBRbdriJeMWMBDAF0VHTwtKG7ZiUd6TGDNA7G7WGi7qkKczdIcFj3UYAOoV7UHQa7l1kaan2Q00W6BBGdVnhnIiC5X_KDgqYUZT9bMxEXPmfn31e_eWmt33VmGexIgTU_SoYy80hHGBjD316aB3Uylk5fvIRw2S3qM5lYOyImHx7HwoyZ2-NWnXaJfb0bSd7ImcvFLVvE9anbu3IZPeXZSqxJRPkhMx42l_i5QIM3Y6uJtB61nPzwNNfBCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندوقت پیش یه زنه بعداز این‌که ۱۰ روز از ازدواجشون می‌گذره، شوهرش رو گول میزنه با دوست‌پسرش پا میشه میره شمال؛ وقتی برمیگرده شوهرش میفهمه و زنه با کلی التماس شوهرشو قانع میکنه که دیگه تکرار نمیشه
🔴
چند روز بعد شوهرش حین تماس تصویری زنش با دوس‌پسرش میرسه خونه و مچشونو میگیره.
🔴
این سری با دوست‌پسر زنش (امیر) یه قرار میذاره و وقتی میرن سرقرار، یه چاقو به امیر فرو میکنه و میکشتش و بعد خودش رو تحویل پلیس میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127097" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رویترز: مذاکره‌کنندگان قطری پس از مذاکرات با مقامات ایرانی که تا ساعات اولیه صبح پنج‌شنبه ادامه داشت، روز پنج‌شنبه تهران را ترک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127096" target="_blank">📅 12:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزارت امور خارجه کویت: ما تأکید می‌کنیم که  کویت حق خود را برای اتخاذ اقدامات لازم برای حفظ امنیت و دفاع از خاک و تأسیسات خود محفوظ می‌دارد.
🔴
حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127095" target="_blank">📅 12:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127094">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مخبر: اگر دشمنان شروط ایران را بپذیرند جنگی در کار نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127094" target="_blank">📅 12:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127093">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
الجزیره: حملات هوایی اسرائیل شهرهای سریفا، برج قلاویه و طولین در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127093" target="_blank">📅 12:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127092">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وال استریت ژورنال: کاهش شدید واردات نفت خام چین در طول جنگ ایران، در پایین نگه داشتن قیمت نفت و حفظ رونق اقتصاد جهانی نقش مهمی داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127092" target="_blank">📅 12:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127091">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYWX2KC1NlRSnaC_zo--CNtf_hqqAAGc1D5wNYg5MjCAvFdKjC2Fknnfkp4IfzAOgK_5F1LXpMPnf01Zss0rCihd3Ajpl0KnZPTv5lNSxzcM13eiD2pEufbF3-dtrFHT-bpMK0CPjwRWfQdQIiD3l27QqYViYs1gUGcwzdF3OzVrAP07zNREpXCMRMj74pNDvu9o_DkYo__oSqNqSWtAsdhr2Jy3dIoe9L8TPd-ceN3cG248WpXyOHHxR9X0ebHmZXceITLAVQUYaD6oUO1YRakXuetScBSNyw2UVGrDGWoKgGmL5i3EkoJNwaXbyUNQ-jqJPnOd6L55o5MNfVIYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: با هضم تشدید تنش‌ها در حملات آمریکا و ایران توسط معامله‌گران، قیمت نفت افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127091" target="_blank">📅 12:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127090">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554c9942ea.mp4?token=mdFB1DiWe8aSM8f6PhC0GwvVKApRGaId64ZYgI03H-RCn9DFvdssiQtWUE-FSLft25wUfcvpd0anzlmhxSSbIhjqX-vrI-qeUBQMuNgiWpDHEysp8Ichoiz_-0qhhnhzCKkYQP06PQTeIsMaDWRijLEI3Ureb-6Ylbv9ofDBIzTyCpjfhOxd6yei4BF4azvIXw4aW9GC936kxwcezKz8tEqX2QQzyRjNwqmF-v5GCizPy3j3VAv30nZti380ILDkjtLTG-MzcnNBr0QYhUFNYxDFTXl8Gf8YaQ57WAQFfZiqjMdKOeuOPLxm1lpc9h-X_Ep56nAWVDyPCykyThXrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554c9942ea.mp4?token=mdFB1DiWe8aSM8f6PhC0GwvVKApRGaId64ZYgI03H-RCn9DFvdssiQtWUE-FSLft25wUfcvpd0anzlmhxSSbIhjqX-vrI-qeUBQMuNgiWpDHEysp8Ichoiz_-0qhhnhzCKkYQP06PQTeIsMaDWRijLEI3Ureb-6Ylbv9ofDBIzTyCpjfhOxd6yei4BF4azvIXw4aW9GC936kxwcezKz8tEqX2QQzyRjNwqmF-v5GCizPy3j3VAv30nZti380ILDkjtLTG-MzcnNBr0QYhUFNYxDFTXl8Gf8YaQ57WAQFfZiqjMdKOeuOPLxm1lpc9h-X_Ep56nAWVDyPCykyThXrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد خیابانی: سردار تو تیم نیستی ولی هستی، بعضیا وقتی نیستن، نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستن
!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/127090" target="_blank">📅 12:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127089">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت خارجه چین درباره حمله آمریکا به ایران: باید امنیت کشورهای منطقه محترم شمرده شده و حفظ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/127089" target="_blank">📅 12:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127088">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
خبرگزاری مهر: یک حملهٔ آمریکایی به یک کشتی باربری 150 تنی ایران، در خلیج عمان در اوایل امروز انجام شد، این کشتی حامل کالاهای ضروری را از خصب، عمان، به ایران حمل می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/127088" target="_blank">📅 11:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127087">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سپاه پنج پایگاه نظامی در اردن، کویت و بحرین را هدف قرار داده است
🔴
پایگاه هوایی موفق السلط (اردن)
🔴
پایگاه هوایی احمد الجابر (کویت)
🔴
پایگاه هوایی علی السالم (کویت)
🔴
مقر ناوگان پنجم آمریکا (بحرین)
🔴
پایگاه هوایی شیخ عیسی (بحرین)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/127087" target="_blank">📅 11:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127086">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/191eaaade8.mp4?token=pqr-igWC6k6U_j4jXWQBlkXOjw7NMojAddl4rn76i_B3qCvRi36b71SsQq1imuMOPJiykHm0_6sMLY3YpmCWpcBwG9NuAItl5liKYc1D6bHGdiQz5TZiTGyCs6l_DkeArkYCNGa7kbhfSq_qFc8fgXfZso9uo4LpIbdjbYM4oI6k28DgTAmqHgG4sZuzv3fHvcJjw93YHR_qlq7vS1xfpDfrFp5gl_Lsi2FvpnAaPxL4g0fV5GncptFhguc2G6uWGb27Gpb3MYtX4gsf4lfCzyo8IlYpcbaX0K161pDVmUQJuiyjrvhg4YJxH8lSKDnbGj3FjkFn4JrSrTAl96sz4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/191eaaade8.mp4?token=pqr-igWC6k6U_j4jXWQBlkXOjw7NMojAddl4rn76i_B3qCvRi36b71SsQq1imuMOPJiykHm0_6sMLY3YpmCWpcBwG9NuAItl5liKYc1D6bHGdiQz5TZiTGyCs6l_DkeArkYCNGa7kbhfSq_qFc8fgXfZso9uo4LpIbdjbYM4oI6k28DgTAmqHgG4sZuzv3fHvcJjw93YHR_qlq7vS1xfpDfrFp5gl_Lsi2FvpnAaPxL4g0fV5GncptFhguc2G6uWGb27Gpb3MYtX4gsf4lfCzyo8IlYpcbaX0K161pDVmUQJuiyjrvhg4YJxH8lSKDnbGj3FjkFn4JrSrTAl96sz4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه وکیل: دارک ترین پرونده ای که داشتم؟
۱۰۰ تا زن متاهل با یه پسر ۲۴ ساله خیلی زیبا رابطه داشتن که شاید بچشون به اون پسر بره و خوشگل بشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/127086" target="_blank">📅 11:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127085">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پاکستان درباره درگیری‌ها میان ایران و آمریکا: میانجی‌گری ما برای دستیابی به صلح پایدار ادامه خواهد یافت
🔴
عمیقاً نسبت به رویداد‌های اخیر که حاکی از شکنندگی آتش‌بس موقت است، نگران هستیم
🔴
چرخه خصومت‌ها را نمی‌توان رد کرد
🔴
از همه طرف‌ها می‌خواهیم که به تعاملات دیپلماتیک ادامه داده و به صلح فرصت بیشتری بدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/127085" target="_blank">📅 11:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127083">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/127083" target="_blank">📅 11:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127082">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9Jw78mB-fOHBrcDFxkC8MQuENxjyxheKzf2izbCXjRQSyo0ivhMu9M325k3NWe5kncNlHTaAtNrGakO4ECXt069Bkwefo_Mwsihnuj-OOTmsFrLF9JLJ-X_fAz0_H4Cs7ul96GJVAyZ2p44n6v3XCifXxG4FRaMvqi5ICbAREYaZpfj5xMcbVUlPNjOeg6DBTpkuWanOLpdxnmimAUlxqAdOJiQhJC56v84M-qM3CGho1Td9jrYp39QT-z6ABbLkIZJQBXGEw_YklDUhXFcWfG2U30n6lHZCgECjTowMCePR4oVBz-qMCFowbMSBSQW04J_SEGXFIxXUavBeDpYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت خارجه در خصوص نقض آتش‌بس توسط آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/127082" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127081">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع دیپلماتیک: مذاکرات ایران و آمریکا همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127081" target="_blank">📅 11:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127080">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8736eceb33.mp4?token=DkMNeOc9RsA40frXdbSv5UTdx8nrN43su8TQJYSekoYXg57afrwDs-8P-lCqLKhauM2DOa-GVo0pFTc7iZljPPNbnkNf8jIC8XBXPSj6vRE1eG5e4VE60cO2xVFZSQBAI4AQX-uhHjsjAIy4uikxrMC1BxAZCbKLOlB04mA9bwOwhbWUKvDwhdPCQwLLSdQB2yJysBqWK3iACd-p5YOy-JQboI_OkbNd8Nsc-I7dFWw1OxfIuvFP40B0EzYsKTHFGFHWgxQ2YanxTAf5gsHCTha_u43BJmZTy-K3ndRj2q2m1ekRew0oIlCxTx5RR5c0cn_15-8J71CT3URO_OIrVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8736eceb33.mp4?token=DkMNeOc9RsA40frXdbSv5UTdx8nrN43su8TQJYSekoYXg57afrwDs-8P-lCqLKhauM2DOa-GVo0pFTc7iZljPPNbnkNf8jIC8XBXPSj6vRE1eG5e4VE60cO2xVFZSQBAI4AQX-uhHjsjAIy4uikxrMC1BxAZCbKLOlB04mA9bwOwhbWUKvDwhdPCQwLLSdQB2yJysBqWK3iACd-p5YOy-JQboI_OkbNd8Nsc-I7dFWw1OxfIuvFP40B0EzYsKTHFGFHWgxQ2YanxTAf5gsHCTha_u43BJmZTy-K3ndRj2q2m1ekRew0oIlCxTx5RR5c0cn_15-8J71CT3URO_OIrVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از آتش سوزی نفتکش هندی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127080" target="_blank">📅 11:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127079">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: ما حملات مجدد ایران به اردن، بحرین و کویت را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/127079" target="_blank">📅 11:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127078">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srWboyylrtGdwIUwy6BUB415e3gXdF0mQhMfdCOHJ6nfuKP5fc3sSKpyp0Ax6X2_aDgkP33qzeelHE_43O1652N3G3b3wJMQzzEDRHiOJuUdEdgGzEsdJivfaZ-nsirG0GJIvtZp6OsLr79c31oEHkNRfsCJmsWob5shZUl0ClsvLBO07qZS1IMypPzZQ7dJ6902USMvcOl6Y8yI0fAlNM9XZPtkbSVuDLDDUnkuR4AdoJjb92GzFVcZDk0R6_qXLVb9TYevOcVITBlZ84CLdHNkp6u0LHdGDRJ3BLm1z6J6Ta5zbTZ0ojSX_G4M095FtibIgvtYOH3BB4cbeLZ7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاهکار جدید رستوران های تهران:
پنیر+ گوجه+ خیار+ گردو= یک میلیون تومان وجه رایج مملکت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/127078" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127077">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">😳
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
@NetAazaad1Bot @NetAazaad1Bot اینجا از اون خبرا نیست
😎
⚡️
💎
نامحدود واقعی، بدون استرس تموم شدن حجم
✅
مخصوص این روزایی که اینترنت پایدار از نون شب واجب‌تره
❤️
🚀
فقط امشب با خیال راحت وصل شو و…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/127077" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127076">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kawq3CkLsLefB9L5vkZygEqTEaaufxbE1SyQs1gr50df2rV4daViugJGNkeviUATe7cXA9n2RtHjaquritnGkcTQWOZ8xZM7bLt7yrRLVA2TgiPh1aFLq5OKonwEyyjCcUWmbaen_IcjuILPuiYrO5i8WfQlFP33b5XBMfzoOW0GMAc1TfUK4uLQpsswEu83CEBfowAGcfiHBhhBymWnn3sOsYiVFvXBGXRtictuykQAgpCsUUNHP7mw7PCDW-TQTnszVHy9bSeqKCo5DwwHbObDtB-K8CtEhJWN2LiylOoyQ_Y9NCrqOGCfgZvOcfm-gyy4_b8owz5tSecO0HfJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
@NetAazaad1Bot
@NetAazaad1Bot
اینجا از اون خبرا نیست
😎
⚡️
💎
نامحدود واقعی، بدون استرس تموم شدن حجم
✅
مخصوص این روزایی که اینترنت پایدار از نون شب واجب‌تره
❤️
🚀
فقط امشب با خیال راحت وصل شو و لذت ببر
⌛
ظرفیت هم محدوده، جا نمونی.
✅
@NetAazaad1Bot
@NetAazaad1Bot</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/127076" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127074">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/To1H6WMURTLZfgHuIiH4zwwDAOWsQqPA7DcjlFIMcqot4U96ywiEYRH9c3aIGO9pexVsdg0hGGglRwoR-G13sPF65A62GDNliN5nQy8inhsZu4aveAInkKm0-WleSKEopWimqb8zcDgrP5IlBvJ50pGB8PlCE6B2-TWJDKvNblTZ42YTCC0yU6YpOMr_Iy1dCqfrHq_FDhaIfTBcwiHeU-zUEJc8zVo29N1kC5OOV84h_57ZbWqnPbxMsVald6lMqsgdvoU4kpp959LeNV7kI6t9xj8g8I6kgD--7wWe1-2OEw7uUPT3Je9hu6p3PcYa6mzjVQQwPG8HxujOQLoQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkb9qLQyw7poBVuO10GgHPiUfgOy1Gyj0RdU-1WCWco45KnclA6AEy-pq6hv7b2xx1RPsQc6jAwRIDQjnsxgKJ1744Vw12PQx0YKRYcmGyz748zpAbb5MLL93xo8ljf7RH-BuqZr47YKc3_Ymz0C29Ityr080HVWG4ZFE8PBP403eA911gVoAO05-Xs9ijjBIOiZ9MU4Hg7lSCqqDbOxqMXQJ042lcvhBK40QW0hZCH5na2gHErVGN3QS7BWqadN3Q6GS4lxGc_4q5tD5LUHb8hhWNFWYlduDNqYP5YtyPl7018sa_zzwH1BU8dow_NfsPtLcNkChrOYwfmbWyK55A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون اومده آبجوی ۴۸ کشور حاضر در جام جهانی رو خریداری کرده و کلکسیون تشکیل داده.
به عنوان نماد ایران ایستک رو خریده.
یکی نیست بهش بگه اون آبجو نیست داداش.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127074" target="_blank">📅 11:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127073">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رسایی:
این اینترنت بی،صاحاب رو یکی قطع کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127073" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127072">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAt70oue04QqaVBrIx4Ca6o_yR4RqfTs4I1QmO_-mYrUuxVrYnOZJiH94jGNE5htg_Meqa8xtE7ZivbsQStTrx2DBqIs8L8quefiIsEWYPwjBLptFyDK25F8HTV62_IS8HQ3j31WvYI4muLDPifhlvYHRVsa1CwH0nC-phdfq6tkRb_V_V3ld54DDYXldEvDyVVfdh-GARFbCcEDhgW_sRDu_OxU82wYHbJRftsrtsjaRJESGCgu2ArLSX1w8ggUczIgvITpwMLtImQWQ98l9ry3ZLuzVbzP7KPnEEwOWgnnaH46DLJksfJG2R0DEY9NtICHeNc68iLVuL-p67K1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: مطالبه مردم حمله پیش دستانه هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127072" target="_blank">📅 11:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127071">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LojARnAdO3Zrec9Od8-cBWhP2qkKXCkxVGqowB16M86Ho2zHN8Z7zlaOpS-Lrfv9jClazBnEY_v2DuzipAh2rv7jpKKXJxvWFdkqnef4z5tl2xgal4-Y-NxLzB3AHQG9azxOFeMdZ8Hzz9ALNlvUvrcQymGO5jbagINZ-_l96_ed8TCdTCsrkNTwNZGg9IYtP8C_oyFxy6ERdSUstDr-VIoh-SKL5zczoa_ne_9r2UmXySLmROFv3EmVwbfngHSmxK3-l_VX-GD7pR53F2LAfTTRfDfv7Scol6djj6UNeYFolKk33HSF7LT8oZS04foX-aV7qU5kff0_y2i7wWF2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: فورا از ان‌پی‌تی خارج بشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127071" target="_blank">📅 11:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127070">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
۳ مصدوم در حوادث مرتبط با حملات آمریکا در تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127070" target="_blank">📅 10:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127069">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ارتش اردن : سامانه‌های پدافند هوایی کشور 20 موشک شلیک‌شده از ایران به سمت منطقه الأزرق را رهگیری کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127069" target="_blank">📅 10:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پزشکیان: دهک‌بندی خانوارها باید اصلاح شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/127068" target="_blank">📅 10:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127067">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رسانه‌های عبری: اسرائیل امروز به لبنان حملات بیشتری خواهد کرد اما از حمله به ضاحیه بیروت خودداری می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127067" target="_blank">📅 10:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127062">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kA6ksxFpJE3vrdQtfHZCR2kpkMwfcjPsCdu9K34azUuHJOY6bUI2bsQJ1ELMz9U_wAgeSj7NLvHB08bu0LLNlnFQR9If4cxRYztM_LRklA1-q541_fgAjiWjGs6mYW-B6GqT5KzK4kowysQNjqn-5KOrvFs2pH-zwKYhRHqfdDMZz4wlHfrm8Bqjbrv8v_jpFIMbPG050thgy4kJY5G92TkPJEstoTEmGtyJ4ocK0_B-gIZUdOw07PKgJ7_GjUFFa6VI2mzIOtKsbwaYVq5aJfHV43U-YlZvy2LVTGBA2qzZTW_AwrNkPCOEfbjKietSwMaBnkIUcMVlqq-nsTf4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rWee5PU2l-tICfUiS6R8PI33wV_ZkQJUQLmUK17kWRltGN6k572WhmPxrpc7FAnRVqSwnhmFg0aPCSZGxbR0a8B-sHRrTbNQ_t3l7d-OB7-OQcrdyQ7SFwu2EkweCV-hBJGGfOsEqTopI9BJpO5aPpsYoiSXIhhSNOJje_lv_C6xYBbIMjypV1juGSYd2zKsgP6rBgxP1Uhg8XBKdi9UFnCtziyv_dXVrfaH9triWAbEUrbukPR7-7U_sXKW32qPXuW4sWTsyJ9A53HeVzbQmlGpelPy8Bbvuooq17JDh12Q4rH2TDmPhTqVBEbGOtpjvakuVdPBR5vL1W5b2kXM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mHCfP5Yem457xrEry_YPvsHghYzR16FgtVVjswtNK_uBCUsAS3t79noTlO8eD4TTtROR6YGUu3PRNfT8SJJO117Lttb8S_kZadxUxkqcl6fniHKGdEDu2EflEsZt76t8ci31m7Wt8NKtu2S8RrjYoYxRwqQnppY2L1PwkpVTYQLsDda7nNtfkR0epPVK0rrFwOxWeBNSJSSrkubw0Yk67LkSkouNpKhhDr4ISxXcVtyuF1D_rb7tFMvuKQwwBwsNLDMySxPkQHBqi-hIgQtqtFEgVhq6SOK2arELXc58ENHVtR9PzY7PLBFGx1wifDRyLOJlM6lWbmwL6NV0PbcmQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خسارت وارده به مناطقی از شهر منامه پایتخت بحرین بر اثر اصابت موشک فیل شده پدافند پاتریوت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127062" target="_blank">📅 10:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127061">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BX319zTGJF0N-EyU9IAr4YQbRvgFM2ZFVuPwXmwxocU06fEMxgZLvLvFKBLt1xRKn1b8T4AuLEGbPxADn2BiwpeLq0JAQZtx5DNTZu7hjCs4sEphctJDCAxV5tObk0ybR3KAu3iecOu69lFbG03ygfpeROOu0g5YUk72NNXIcnDqhGnPWsIdOmb3Yk_mUf3t5UbtZe0v0DH4ja8QRCRTcOfKmu4u077zGxwItb9cSB2pGvYhH0Bu28qLfSEYtcbn4yJ-D65C8EVzZEeYYieoKz_5zAetGMR-ebgXZo9zEpiR4gtHk7rN_7Ab-j2rNk-P0bRDX5rkyk18s5dx01-3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یوکی‌ام‌تی‌او گزارشی از یک حادثه در ۲۱ مایل دریایی شمال شرقی صحار، عمان دریافت کرده است. مقامات محلی گزارش داده‌اند که یک نفتکش در موتورخانه دچار آتش‌سوزی شده است. هیچ تأثیر زیست‌محیطی گزارش نشده است.
🔴
مقامات همچنان در حال تحقیق هستند.
🔴
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هرگونه فعالیت مشکوک را به یوکی‌ام‌تی‌او گزارش دهند.» - یوکی‌ام‌تی‌او.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127061" target="_blank">📅 10:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127060">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رسانه‌های عبری: اسرائیل امروز به لبنان حملات بیشتری خواهد کرد اما از حمله به ضاحیه بیروت خودداری می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127060" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127059">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta2JU0tKTRXHP8nZEZc7wW9sWDOy8BgAxLwJZ94spi_dwahAg0AzGGfF-6mGIm9BNcipnXbhzvD6_gkPajdbjAn_T1NQK_HnlT36gfbNvVMQoBtGBuRqtajoTJ3v8MYBpYDgGRfE-tB_IPj0ZcTmdB3aTtGJO92NFmkuHHcgFGYyW0vUMDJuTK7paggNWZsNYv4tNFGmSYcmBHYI-um5JhZfLcfj0UHXDNV0xkFp4w4yrtWGiSQwC7QGdCCYb6ENCQse3hr7txGyWqreWCNVdxQ-h9RA7h9Qg3wJaWpBKuN1FwL9fK1fJoSiVzXimFSZeIGjOHJCBxjsc9wDP8UZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: تولیدکنندگان بیشتری برای رساندن انرژی به بازارها در حالی که تنش‌ها در خاورمیانه ادامه دارد، به تاکتیک‌های مخفیانه روی می‌آورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127059" target="_blank">📅 10:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127058">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴ ریشتر  حوالی نورآباد در استان فارس را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127058" target="_blank">📅 10:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127057">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8GNFhykcv1-LKVsg4WBsY3h4NyUuaWUdEc92QfsQdzEJqna3hD2ilDkOjE6SH3TQ1QdpNJn15MlR7wmahy-8epILs8C_8HG5ZrRSjn5F2VRr_i09UDs_ltFlLp0__H8vuSHjPsHUlWrcVvnFS8k8MqcbKNzBaksBOWsdkoXOeQk7rgcPXvudurZNuDewfV2kfI3GT5jqP7xk2BzsdTRrp8BTQTnaflD41Y7HCEZqsbEJugwlhFi9xKuYfgJE6tTU7kCgGuhdGTF5ljLsVHKb3_vnRHeJO_HT0uJTVh52aOj8_1M3n2ELxfs9KQ-MP7cr1DeWkP67gZxTxWQO8ySIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اینترنت رو قطع کنید تا دشمن سواستفاده نکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/127057" target="_blank">📅 10:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127056">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fabf4cc4f.mp4?token=l5HseysWIkrohuxwryrHsh9TTZII3tMRxjcJe6A9wEpXyUPR2e5MQIvtcrPq171EYq81r1uTkjDGikmzcCBjPk0-06c5f0rmU-EG1mvuu_lZNSjr9p0kww5EzovCtCUcKTWIuivIVcxJgkbigJcobH6y0LBNXPFcEUh5ibF0KJHOj_UNjSX2FYJces7UcW9I_AtB-0CLTQiofXP2NLEeAwtWoz3ny-Mju21AeZX1lNxNluKt_0I7lMzxmbglikXGVXHtvZtnlS-830iBHx0kgk4Fbv6XTbzT76qRXS60kDtzi2rfNqnooekFFYNer_as9WRzC_W34fWtLXqyhW13ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fabf4cc4f.mp4?token=l5HseysWIkrohuxwryrHsh9TTZII3tMRxjcJe6A9wEpXyUPR2e5MQIvtcrPq171EYq81r1uTkjDGikmzcCBjPk0-06c5f0rmU-EG1mvuu_lZNSjr9p0kww5EzovCtCUcKTWIuivIVcxJgkbigJcobH6y0LBNXPFcEUh5ibF0KJHOj_UNjSX2FYJces7UcW9I_AtB-0CLTQiofXP2NLEeAwtWoz3ny-Mju21AeZX1lNxNluKt_0I7lMzxmbglikXGVXHtvZtnlS-830iBHx0kgk4Fbv6XTbzT76qRXS60kDtzi2rfNqnooekFFYNer_as9WRzC_W34fWtLXqyhW13ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از انسداد کامل تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127056" target="_blank">📅 10:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127055">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ceee7bed.mp4?token=oHsL0lPOkbi_jCsb6W_-eXF7397Ad222OdFLTf4duk-Pqw5CHfMUdNqHnq2-ozZDCEObjjm64F2uZtX5xlK5SS9IFUhZDrmuq3hqWRS_ejJsrbAzNJS04iEoxWksXitiHH-eYKoSpL4wOB9LHPaV7fOfdC893NITWuV1jYz4jKmeAG2T3kdhn-KjHer95PYNPjqkC0_hFtbknQZHOT7mbCCv7ACyete9qgmhLj45oqIhCYdP7R98-nll4Wo2C_I5jtC_CZZgCmET6nTDIoQlLN0HbmHOBMadPHFq_nwwvDY1mrpC1uV_VxyeEjChA-GA7JllHTSNfA6yHp8i6_fgRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ceee7bed.mp4?token=oHsL0lPOkbi_jCsb6W_-eXF7397Ad222OdFLTf4duk-Pqw5CHfMUdNqHnq2-ozZDCEObjjm64F2uZtX5xlK5SS9IFUhZDrmuq3hqWRS_ejJsrbAzNJS04iEoxWksXitiHH-eYKoSpL4wOB9LHPaV7fOfdC893NITWuV1jYz4jKmeAG2T3kdhn-KjHer95PYNPjqkC0_hFtbknQZHOT7mbCCv7ACyete9qgmhLj45oqIhCYdP7R98-nll4Wo2C_I5jtC_CZZgCmET6nTDIoQlLN0HbmHOBMadPHFq_nwwvDY1mrpC1uV_VxyeEjChA-GA7JllHTSNfA6yHp8i6_fgRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز یه شاهد هم تو کویت دیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127055" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127054">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کویت حریم هوایی خود را بازگشایی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127054" target="_blank">📅 10:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127053">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نیویورک تایمز: حمله آمریکا به مخازن آب هرمزگان می‌تواند مصداق جنایت جنگی باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/127053" target="_blank">📅 10:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127052">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر دریانوردی هند: سه ملوان هندی دیروز در حمله ارتش آمریکا به یک نفتکش نزدیک تنگه هرمز کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127052" target="_blank">📅 10:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127051">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سفارت آمریکا در اردن و عراق امروز از اتباع خود خواست تا در اماکن امن پناه بگیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/127051" target="_blank">📅 09:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127050">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اسرائیل هیوم: شرکت هواپیمایی ایر کانادا تعلیق پروازهای خود به تل‌آویو را تا ۲۴ اکتبر تمدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/127050" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127049">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-_s-75RzawUErdmoJODUzHfrwWGQ2elXFxidyZp6iCTLdWzpa9rnmL8HQ-ORycNA4oQj_MLM42q2B4ggIWkTtVYO9IQnHzC0bknFqCToYlk-MWoqjqzOM-EnqULZvzhZe5WCAxqIIjvDz6GvLkqdydTpgyNeZEPYr5E0tlY7c2kgbh76lrT6ycDiy2xKDHg2DzEGFZ7rz3-Nqnwn6YEo2If29wvQdKm3dX4D2K2XXQ5WmUMtj9zb7Y94Np08i8hq9jNCLvwA65JK4tzSAwuEcdFddBv0E1bMhL0In53lxLJdV4lp4ZFdcf5GRtV_S0Fh4outsFu8u9C7HljqD66hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل تخریب خانه‌ها در روستای غندوریه را آغاز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/127049" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127048">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سی‌ان‌ان: میانجی‌گران قطری همچنان در ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/127048" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127047">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هم اکنون حملات حرب الله به شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/127047" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127046">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZksRryjrrDoA6LSbrn06mENDcJWT8L9lG36B1klSJSUzDNuaHD9aHUhNvCzZ9rG688Hs59CNvyao16E7_JCfM1i_nZiMwtFddkZRzS7NB1NjQT1kQQT2QqZBYTYUJ-4qxpXIXUbBhG4UZmSc2a7RxMuBMlC5yhsq_TtOCgrCHyi3oAXRuf8z-IykDvmQkjHfQ3QcfxB4E3pdLHXn7eksVdn49fReCPFQoACqy-IMMbzD6MGYd-DJM0UaI_8q6d5oNmQP9DR1GLLGLxgC2IGramlfuxXrmnq-3HpEosWfQYOKvDuCcwMpSb7tBcTwJukWA9mplNLZR5sPkKo7qYwQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/127046" target="_blank">📅 09:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFeUjPdT2BmspYSeZTrSP2u7vykikhrgtWk473P_CJHgZDWRSeW4rkGcm2wX1Dsg5dsk7oTDCzb1CpYFkS60k1oyrQ-LD3WxU4Z4mRUh14PPXjfXpTgS4fTSAoJKdu3XxLS8DC7sfZoNdrnYvUgsizVVHH7wQZufnCeCVzZbYOM5MuHXj0VVVboXst2b5DyHePPWg7xk6NcqPgxaXzvNsRi7YtpZQSf5RUOsM1CcKTfsAu7OkiL9Sy3gPez-HehApfUv0g2PdMxXsd2whOdQG2HzCt7u50EqEuKrtPTXo9OXus07iq-0ZhQo6pji5cVLn8I2vDEqY0XiFIdRAJM5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMhFViEfldfYprkJF_YU7LYYeiOriEp9fRy6_aIZCpvZfsxnqspl8vUcPkmQSZm6_5vqhOl-vMXxkNJQ0cltk97e-SJEbxWlY6EPjNfocX39sxxcmocEQPeG5xKJ2qyL16Ot_iGxDpKEPnza_klyOLGpNcyb-RTve0URgsePuI79btlPHpmmvcs9Pwxhn7QvZg1jfU9EWhsdhFnV3b_wMNn4Wfup8nGGoF4z-YQ0zxzqTJFivQYkJWdmpyHTTtLfrAyea9L08Zsjm5jngCnyCNt3BvZ9mMhSEGbyRYvXe_S7oYlOxc-Ac4isomzx0A6hKQ88iKgoX9ovH52dulCY3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تی‌آر‌تی: آمریکا در جنگ با ایران ۴ میلیارد دلار تجهیزات هوایی از دست داد؛ یک فروند اف‌۳۵، چهار فروند اف‌۱۵، دو فروند اواکس، ۱۰ فروند از انواع هلیکوپترهای نظامی و ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/127044" target="_blank">📅 09:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B4ev8ctQs_Ab6fhzIKesCwJ4Yj7tKfwdzGj8dq3cOF5OZD6576PSBQ7kEoCyJgQ-wfzEhFqJY54t8t-NiBNNGnBShFXCHfVUl9xPgH2s8RDgapbcwbdI6iFVz8U5blfEsQDChbg0DB4t7dAq6myb9XYAqjvAAQ1Cc1RkxVtVbQ5PQ9o5J8bPPUlszlqwK1xtFYDziVPLjrGg_z9ls7var5EA26L5O04ac6RJaw6BGZolLAmsH3ZaFuc02xsvWWPZegB8DJBU2FPvG8B4X0V0sIM5JqU4bwfyip4iICXF6qU5bHECZTdoyUjylafsC9ZFa9_ZhmyFXxEZ4YdtqoPdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس جمهور آمریکا:
«اگر ایران توافقی که ما می‌خواهیم را امضا نکند،فردا(امشب) نیز اهداف نظامی آنها را بمباران می‌کنیم»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/127043" target="_blank">📅 09:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در محدوده شرق اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/127042" target="_blank">📅 09:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127041">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNxRkOmHt9G1zG3ebpTGQrcgaiEhQEoRYU8DOMt5lM9FXiL5QsnAB_aWbIk5wexVBzaG89tajLXYx94Og3HgTwHxSN0yynyYRf9p94p__QJba1D5E7_XV_SntxP745XfwFMaQwW1IXvZ6gj0BAson680ZyugwzoeT_oIwJn5fQtbMOKC3HeDAVYdQKFKUbB8OACfk2mmHR-fMOk6Q7HRWtLlGzk8WNoTSRHEZN4aCuyljo_U3leKVYxlC98KEnaKOtd02EvT2iMzfgqamUIjNfz5jviaSkMD8INRHX_JzN_Ihpp7uYiXcV6S4X0Wzj4xKckaxlXfaBUTfNSrccLvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های ناسا از احتمال آتش‌سوزی در نزدیکی پایگاه هوایی عیسی در بحرین پس از حمله موشکی ایران حکایت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/127041" target="_blank">📅 09:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127040">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
صدور حکم دوومیدانی‌کاران ایرانی در پرونده اتهام تجاوز به دختر کره‌ای:
🔴
حبس ۴ ساله دو نفر از ورزشکاران؛ دو نفر دیگر نیز تبرئه شدند و می‌توانند به کشور بازگردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/127040" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127039">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گوترش، دبیرکل سازمان ملل متحد، گفته است که آتش‌بس در خاورمیانه «بیشتر شبیه به یک آتشِ کمتر است تا یک آتش‌بس واقعی.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/127039" target="_blank">📅 08:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127038">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758c0424e9.mp4?token=hKTs0I5lYTHGwBmrUP6PMAK5t2A1j6qcQV3Y5kaOOze8b9VCUoSgf6-PMIEiyqvxorT1kEt3a-VHo9zBzi4dGyZxMlAUpwmHufeRkQSqeaNedW-KJoggqWb-B7dNLnZ7M_3CKdTa-p3Ovrabr_aPFtWpqE3xO_uSvPIM0I5B7pmzpVVCXnKXKNwNd8y152TRQ4AyRfM8M5_s2XGe26r8Lf01oI1K2HvGFUGSSkKXzlV47cdyGyHIgJOCdAFOnpACZcVp96phv27vvWJGfv-eYvggUuzx6YmWEaUFR09kdL7atTonzcE94jrtojpxLPyU4pQ6qsb477ldpfq5dTdAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758c0424e9.mp4?token=hKTs0I5lYTHGwBmrUP6PMAK5t2A1j6qcQV3Y5kaOOze8b9VCUoSgf6-PMIEiyqvxorT1kEt3a-VHo9zBzi4dGyZxMlAUpwmHufeRkQSqeaNedW-KJoggqWb-B7dNLnZ7M_3CKdTa-p3Ovrabr_aPFtWpqE3xO_uSvPIM0I5B7pmzpVVCXnKXKNwNd8y152TRQ4AyRfM8M5_s2XGe26r8Lf01oI1K2HvGFUGSSkKXzlV47cdyGyHIgJOCdAFOnpACZcVp96phv27vvWJGfv-eYvggUuzx6YmWEaUFR09kdL7atTonzcE94jrtojpxLPyU4pQ6qsb477ldpfq5dTdAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات موشکی سپاه به پایگاه‌های «الازرق» و «موفق السلطی» به عنوان محل استقرار نظامیان آمریکا در اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/127038" target="_blank">📅 08:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وال استریت ژورنال: فشار نظامی آمریکا تا زمانی که ایران شرایط مورد نظر ترامپ را نپذیرد، افزایش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/127037" target="_blank">📅 08:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4542baba.mp4?token=NFZDMMp_fQriceZ1yK8O--udKeAgx_n23TnE6p4w8urvQpfyxsU1kCRYkZU_O-oWXveR1C1LvqLu-5WPluXmQGMGqT_6yX9Ao-FsRlY70KRlfFtZSxVr0V6MQ0mR1Z4WGRu85p9FeMOCubKQw_AQ2dOT2A_KFb9b-sag6Vmx2ZI4rFuiolW1iAS5JpGG_LZDzmKfCJbj-ySYEd94qCL7bbh2GDt7d5dNlfB8Zuf3UqszrZJ81vHRix0gRsgwkrdF2-t4r68a1XLZEH2ZHYmDDW-4bw4clmKi1wJjJNfWwKFcFCFguokFt2QF1IqXhIS3pIRgL04zU6XN1_t7DUG0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4542baba.mp4?token=NFZDMMp_fQriceZ1yK8O--udKeAgx_n23TnE6p4w8urvQpfyxsU1kCRYkZU_O-oWXveR1C1LvqLu-5WPluXmQGMGqT_6yX9Ao-FsRlY70KRlfFtZSxVr0V6MQ0mR1Z4WGRu85p9FeMOCubKQw_AQ2dOT2A_KFb9b-sag6Vmx2ZI4rFuiolW1iAS5JpGG_LZDzmKfCJbj-ySYEd94qCL7bbh2GDt7d5dNlfB8Zuf3UqszrZJ81vHRix0gRsgwkrdF2-t4r68a1XLZEH2ZHYmDDW-4bw4clmKi1wJjJNfWwKFcFCFguokFt2QF1IqXhIS3pIRgL04zU6XN1_t7DUG0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش انفجار در نزدیکی سفارت آمریکا در بغداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/127036" target="_blank">📅 08:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127035">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6UY2AuTKOOANocFVXy8a8tviW-WkGHfCZzmermkFpsUeZk53HFxO2rUyb8hud81EqHQ45moOH5W5Yk6tAcyr04LM8VpmrMUYUonA6HQmmSqqO9Yn8t5Zia4Kzgig2MkjVF5jThAchju1VxaroeEtCpobE_Wq3fMuAG0Bra15z0Z89ij2E1LnNnkNx2VhFsLdOzN3Omz7bVld0iHdurUq2KFFFeDXeJyFjaLZH2xSuPPFJOzvvC1WcMWRGyrAed1jRojI7rWEpZ1fzMXYmFzSNcqsOgot34ZXdv4Ire-EAwwkXuxVkcCvjM0ofkZfZz2UOHnurdevJjKE30LwisP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه هواپیمای سوخت‌رسان آمریکایی برفراز آسمان عربستان در حال فعالیت هستند، احتمالا برای پشتیبانی از گشت هوایی جنگنده‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/127035" target="_blank">📅 08:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127034">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGWX1eAwZvEajoeA77Q_cGoDDpXpd4hRxpSzAZRJ1fLGWlaII9K0pwwN87c8NZ6GiemCam09eZn-klWSIXLnt2X7B0YnyXt6-pkxvcD3isA0ipWyl5h6sTH1SEWCt7jisogOCy2CUQxPj8EGrcc_kl0ARMVGKkpchcQ-G5jr58ROumFNQkRaYKEZdU5fHLTPmkZEfuYpZtZi8FNitnVk5gr5Gzp2Ziyv_12wU00A6urzt_zgYTdKvs0qxyCNrPsA_PKaCU3QOjV_LQi1Ikv_zwwFSJcz71ByYZd4yGDPqPf5dsjr28hIcwqD4yNap_EhPug67KuPQUNI0B1CQLVVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ سخنگوی دولت به تهدیدات ترامپ: تهدید زیرساخت‌ها، تهدید زندگی مردم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/127034" target="_blank">📅 08:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127033">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0e7a0127.mp4?token=K1LbMWJlRtGeFWE9eL7TPfOz5mwVNz8OLOyjBuL6532QHK2rgO4AfC-OJriZJSSyyWiAj7aqysMFXkgLtetJcpE0udyFOR2QB_oezrxENcOhUfA3t5SCXSYejo1IWNdbed8NIvJ0jHmjLwi9TDmXJuIZ6KxUReSdp2TuEkb58wsO4uromqVytmaZue2H9dJXRKARWXjWP--Do7O7lewtQyj7KzAGczXXlZjo_I4YBYMcGaDrX5jeUKgQJpgcyp202SVEAJAwRFCqiF_5NwZfk8S8JShDL-oFEiTLn5KnUdGCIWO17Ycz66BOzCq03IMET1OJ_UeA67x2RSNdEpKGIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0e7a0127.mp4?token=K1LbMWJlRtGeFWE9eL7TPfOz5mwVNz8OLOyjBuL6532QHK2rgO4AfC-OJriZJSSyyWiAj7aqysMFXkgLtetJcpE0udyFOR2QB_oezrxENcOhUfA3t5SCXSYejo1IWNdbed8NIvJ0jHmjLwi9TDmXJuIZ6KxUReSdp2TuEkb58wsO4uromqVytmaZue2H9dJXRKARWXjWP--Do7O7lewtQyj7KzAGczXXlZjo_I4YBYMcGaDrX5jeUKgQJpgcyp202SVEAJAwRFCqiF_5NwZfk8S8JShDL-oFEiTLn5KnUdGCIWO17Ycz66BOzCq03IMET1OJ_UeA67x2RSNdEpKGIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک موشک از ناو جنگی مایکل مورفی ارتش آمریکا به سمت اهدافی در ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/127033" target="_blank">📅 08:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127032">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4500df2fbe.mp4?token=KCEGvzT5O_iJ5zjNsoRce1yovNV2hwNjgXThxJ33q8MkSC8XHFVVtfexohMz0EUIDVHaS8B8BzUqO8f-PXUhOB7INVeH5_2g488XE0Ke_rEYy4KcVbyfNbcuy8k4FafCABY3ef3mwja0y4oReglR1CqDp084s1tgyIo5y3Rtt3srNxFFKzQS7VQ5pkpdt9PvL2YdWTg8tD1de_zlq0nRIxrThSCpY0DFbtc1nckW6gioq3O-bNGxfxDimi05uLWzpcffyPTHZ9KmpWqfViOE98BlDr0RHVmfSYGMu7FzIp8DoC_oparhCtVGJybxeKAMsmtxv8sAAtVlnicMK2qkPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4500df2fbe.mp4?token=KCEGvzT5O_iJ5zjNsoRce1yovNV2hwNjgXThxJ33q8MkSC8XHFVVtfexohMz0EUIDVHaS8B8BzUqO8f-PXUhOB7INVeH5_2g488XE0Ke_rEYy4KcVbyfNbcuy8k4FafCABY3ef3mwja0y4oReglR1CqDp084s1tgyIo5y3Rtt3srNxFFKzQS7VQ5pkpdt9PvL2YdWTg8tD1de_zlq0nRIxrThSCpY0DFbtc1nckW6gioq3O-bNGxfxDimi05uLWzpcffyPTHZ9KmpWqfViOE98BlDr0RHVmfSYGMu7FzIp8DoC_oparhCtVGJybxeKAMsmtxv8sAAtVlnicMK2qkPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلوله‌باران توپخانه اسرائیل دیشب در نزدیکی بیمارستان دولتی در نبطیه، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/127032" target="_blank">📅 08:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127031">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده(سنتکام) : ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی شده است که تنگه هرمز بسته شده است.
🔴
حقیقت: کشتی‌های تجاری امشب همچنان در حال تردد به داخل و خارج از تنگه هرمز هستند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/127031" target="_blank">📅 03:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127030">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlO5A2aOYLQlRLaV8MdYe4Wq5VU1DhA7_S2UaUfS_aChSygRnWARrE7KHMAsw1VAlBOUztR1IjT0cSAyDVcqXZvBRVH46xxqAlA5rPVmGjB1zdZQWPRUgiHkDc5HJIu5LJxgwrFXDqm5Pnbb4JW1HhXoaxkHTI9aY7cxFkJoJ8BrIiaNtO7LVToJdFTrBBy2CpiAHy703PLeS5UUcSyz6EkAvbplAizY464qnXwuwxi0E1IybdDxuJGudnKNnWunKzBK0lkaDKShZmBnZxNN2YBAe6OU6Q0lU_8VmsftXHIeu-b-iOwpURJ9GgT59pQHfNVtmCT4VTWmIEKRJ-lk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده(سنتکام) :
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی شده است که تنگه هرمز بسته شده است.
🔴
حقیقت: کشتی‌های تجاری امشب همچنان در حال تردد به داخل و خارج از تنگه هرمز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/127030" target="_blank">📅 03:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127029">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
صداوسیما: ترامپ بازم دروغ گفت و عقب نشینی کرد و ما پیروز شدیم، الله اکبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/127029" target="_blank">📅 03:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127028">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ در گفتگو با فاکس نیوز:
آتش‌بس با ایران، نقض‌شده‌ترین و ناقض‌ترین آتش‌بس در تاریخ جهان بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/127028" target="_blank">📅 03:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127027">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:
نیروهای آمریکایی ۴۹ موشک تاماهاوک شلیک کردند که به اهدافی در عمق خاک ایران اصابت کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/127027" target="_blank">📅 02:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127026">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: اگر ایران توافقنامه رو امضا نکنه، فرداشب به بمباران آنها برمیگردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/127026" target="_blank">📅 02:57 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
