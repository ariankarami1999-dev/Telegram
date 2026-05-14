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
<img src="https://cdn4.telesco.pe/file/ldU5m6jlgZaD6v06j4HiQZB9vCJJC85emLDx58iUQW3aGLrAVwVsGb6zJKSlmBRHiYO_3mILmkJYzPbmY__xDHIJmdKHeX_P9IgFHHlRls-z3Pj-bb1ZUEEBBvWERjptlVmiyU595yRKiACTqitboTCgCMq53rtSZL2GyZ8QjWt1OpfjQIlAwoHNOD1fRkQ2rbFXmJtfXbijds9AGbJp6njZuHH7sZNGJsm5ZqdFzVfzsToI_qcj_PvJl_5eD-UEFQ9ncDe9zfFUMM-GrNJNF4GddPSU2s2oHEso6KpIUu6rc1SS8iVO8pp0X8R9AtVaAS5cmuCAA492EmT29S8PPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 959K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 10:11:36</div>
<hr>

<div class="tg-post" id="msg-119852">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
عراقچی در نشست وزرای امور خارجه کشورهای عضو بریکس گفت که همان‌گونه که همگی شاهد بوده‌اید، کشور من طی کمتر از یک سال، دو بار هدف تجاوزی وحشیانه و غیرقانونی از سوی ایالات متحده و اسرائیل قرار گرفته است.
🔴
حقیقت آن است که ایران، همانند بسیاری از کشورهای مستقل، قربانی توسعه‌طلبی غیرقانونی و جنگ‌افروزی شده است. این‌ها پدیده‌هایی زشت هستند که هیچ جایگاهی در جهان امروز ندارند.
🔴
همان‌طور که بارها تأکید کرده‌ام، هیچ‌گونه راه‌حل نظامی برای هر موضوعی که به ایران مربوط باشد وجود ندارد. ما ایرانیان هرگز در برابر هیچ فشار یا تهدیدی سر خم نمی‌کنیم، اما به زبان احترام پاسخ متقابل می‌دهیم.
🔴
هرچند نیروهای مسلح قدرتمند ما آماده‌اند پاسخی کوبنده و ویرانگر به متجاوزان خارجی بدهند، اما مردم ما صلح‌طلب هستند و خواهان جنگ نیستند. در این وضعیت شرم‌آور، ما متجاوز نیستیم؛ بلکه طرفی هستیم که مورد ظلم و تجاوز قرار گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/alonews/119852" target="_blank">📅 09:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119851">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9f713d53.mp4?token=do3Qqtk23H6neH_B6AQhCQScC5YjIXOALDc8sC5XnucfOvludOL7r0zie8AaAhBlDVdwRHLdEXiAM6lCX8TgRBHkpEFYEjWe_zbxHlKZie2eFDpypyjeZSLYea-rfI3rnZhvl8yLSjh62hcq_qgb-rYM_7gM4K0_3XUs33QG3nIueNxYbPW5O9bKuu6EZdACr1-GuXqONNwK1I10QmyxaknwF0vhDxJnPk5dYsDzNxUvq2f5ZzAmqUTO9YlWWKXtt31I3ecWB1IhIkK_RJzMlg0_SGjGGi-g8Qz8aUX5AZq2YsKL56DJd6NT7hWQXdgQ3Dn9XXSlZAy83efgicntSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9f713d53.mp4?token=do3Qqtk23H6neH_B6AQhCQScC5YjIXOALDc8sC5XnucfOvludOL7r0zie8AaAhBlDVdwRHLdEXiAM6lCX8TgRBHkpEFYEjWe_zbxHlKZie2eFDpypyjeZSLYea-rfI3rnZhvl8yLSjh62hcq_qgb-rYM_7gM4K0_3XUs33QG3nIueNxYbPW5O9bKuu6EZdACr1-GuXqONNwK1I10QmyxaknwF0vhDxJnPk5dYsDzNxUvq2f5ZzAmqUTO9YlWWKXtt31I3ecWB1IhIkK_RJzMlg0_SGjGGi-g8Qz8aUX5AZq2YsKL56DJd6NT7hWQXdgQ3Dn9XXSlZAy83efgicntSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ناتو: من از ناتو حمایت کردم زیرا به ما اجازه داد تا پایگاه‌هایی در اروپا داشته باشیم که می‌توانیم در شرایط اضطراری، مانند اتفاقی در خاورمیانه، از آن‌ها استفاده کنیم.
وقتی شرکای ناتو اجازه استفاده از آن پایگاه‌ها را به ما نمی‌دهند، پس هدف این اتحادیه چیست؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/alonews/119851" target="_blank">📅 09:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119850">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62b70355a.mp4?token=tm7Mkh2PWKFK2d1WEiXFjKakYNyMlF-0SMr2ki0N70GlIsy9VjRm7et55tAktceDyRfSzDO6yHLcK9f7PB9J-oGVJ24xG5CFT0UWsCyODglCOmuylOO0EkMQhAuMiGHDkxqCmp6ncNH3W3vD9ouWJwkLlGzDz0Su1V-y4ZMIKZDNq7yjMojDPKu9PF0LFDGzdjFA0F2y7DvwrGpIsYrNh0hESci-ABTq1_lygFPv4tOfX2l0VSPNQl9Y850GtdVgQPSGdUEoygFE4b8mgQQKQ2FDk8WBwQFc-JLcf5kfFU5inUURHURZHgW6Zn2RqPeoV6iJvhiFxUYPzPZ8t9SIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62b70355a.mp4?token=tm7Mkh2PWKFK2d1WEiXFjKakYNyMlF-0SMr2ki0N70GlIsy9VjRm7et55tAktceDyRfSzDO6yHLcK9f7PB9J-oGVJ24xG5CFT0UWsCyODglCOmuylOO0EkMQhAuMiGHDkxqCmp6ncNH3W3vD9ouWJwkLlGzDz0Su1V-y4ZMIKZDNq7yjMojDPKu9PF0LFDGzdjFA0F2y7DvwrGpIsYrNh0hESci-ABTq1_lygFPv4tOfX2l0VSPNQl9Y850GtdVgQPSGdUEoygFE4b8mgQQKQ2FDk8WBwQFc-JLcf5kfFU5inUURHURZHgW6Zn2RqPeoV6iJvhiFxUYPzPZ8t9SIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ترامپ: او مایل است کاری را انجام دهد که دیگران درباره آن صحبت می‌کنند اما انجام نمی‌دهند.
🔴
وقتی می‌گویید: «خب، نمی‌توانیم آن کار را انجام دهیم»، او می‌پرسد: «چرا؟» او مایل است کارهای ناتمام را حل کند و آن‌ها را برای نفر بعدی، مرد یا زن، باقی نگذارد.
🔴
بخشی از آن بودن بسیار لذت‌بخش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/alonews/119850" target="_blank">📅 09:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119849">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddca6e481.mp4?token=axNxRFntfM1ZmmfWry84sKQrkaNXmHuTBSElwh1iqRw6DSc8IS7cKGKHD1BoI2qlrfeAtVQGdt_B2tEFee-jbWN92753BcYHMeeKne2W9i-fwHNdjBM99YAysiIdfKIW0Og3kswD7-DhgioiotPn9X-nbk0sljAZ_-OYLswPomp_3yZlanddfwNSHB_qFrCig_E9PCNRXNFWQAbkTxR9Uf52ec3M4N4pdZ_hm-FBl4vo7fvaeJWKB981s4_nWL7STAq7-naeRtbJKp1caUlSYVsI3FIjRZM-9X8gCH45JDVgz3eJJTF2Xi5-OF51jhcPFvb0xvGsV3wKqkHfVFgJjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddca6e481.mp4?token=axNxRFntfM1ZmmfWry84sKQrkaNXmHuTBSElwh1iqRw6DSc8IS7cKGKHD1BoI2qlrfeAtVQGdt_B2tEFee-jbWN92753BcYHMeeKne2W9i-fwHNdjBM99YAysiIdfKIW0Og3kswD7-DhgioiotPn9X-nbk0sljAZ_-OYLswPomp_3yZlanddfwNSHB_qFrCig_E9PCNRXNFWQAbkTxR9Uf52ec3M4N4pdZ_hm-FBl4vo7fvaeJWKB981s4_nWL7STAq7-naeRtbJKp1caUlSYVsI3FIjRZM-9X8gCH45JDVgz3eJJTF2Xi5-OF51jhcPFvb0xvGsV3wKqkHfVFgJjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو
،
درباره ایران : مردم در برقراری این ارتباط مشکل دارند، اما این ارتباط بسیار واقعی است.
🔴
آن‌ها قصد داشتند آن‌قدر پهپاد و موشک داشته باشند که هیچ‌کس نتواند به ایران حمله کند، زیرا نتیجه آن برای منطقه فاجعه‌بار خواهد بود.
🔴
به محض اینکه آن‌ها به این مصونیت رسیدند، به سمت دستیابی به سلاح هسته‌ای می‌شتافتند. دونالد ترامپ اجازه نخواهد داد که این اتفاق در دوران ریاست‌جمهوری او رخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/alonews/119849" target="_blank">📅 09:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119848">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
مارکو روبیو درباره کوبا: این کشوری است که مردم در آن به طور واقعی زباله‌ها را از خیابان‌ها می‌خورند.
🔴
کوبا نباید کشوری فقیر باشد.
🔴
کوبایی‌ها از کوبا می‌روند و به کشورهای دیگر می‌روند و موفق می‌شوند.
🔴
تنها جایی که کوبایی‌ها به نظر نمی‌رسد بتوانند شکوفا و موفق شوند، خود کوبا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/alonews/119848" target="_blank">📅 09:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119847">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0816ff7f7.mp4?token=nAO_T0-dGscvuDrm4Uvo8lvmpYEMVM1UUPD4FvAXDCDxgtMTE2c4_rqYXw281IcG7cczogdWNoqUiFdwFqv5JwS9B-CjHJIliEHjwrzWuVC4ua6swoXoymtj0o4iQaqgRg22zHgasKhIoXPtP_L88mgot5Lm4PkoxyJTtEmqDDQcUGJ1WXNAb0MEOTGGnOe5uWKX9rBkPkO3xzHfF7iU_dmVX7ieiNo1c30WrmHEgl6MBCMeGo50L5sRVI1HJELn1eoZPKXoNm6xfbcN4MvrmK5JGQMawn7vCp0ZSMnAmp3gddPaulYxYDlohUFhB-vwNmPfjQpSQsKKJP4zH0VYoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0816ff7f7.mp4?token=nAO_T0-dGscvuDrm4Uvo8lvmpYEMVM1UUPD4FvAXDCDxgtMTE2c4_rqYXw281IcG7cczogdWNoqUiFdwFqv5JwS9B-CjHJIliEHjwrzWuVC4ua6swoXoymtj0o4iQaqgRg22zHgasKhIoXPtP_L88mgot5Lm4PkoxyJTtEmqDDQcUGJ1WXNAb0MEOTGGnOe5uWKX9rBkPkO3xzHfF7iU_dmVX7ieiNo1c30WrmHEgl6MBCMeGo50L5sRVI1HJELn1eoZPKXoNm6xfbcN4MvrmK5JGQMawn7vCp0ZSMnAmp3gddPaulYxYDlohUFhB-vwNmPfjQpSQsKKJP4zH0VYoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به سوال خبرنگار درباره تایوان پاسخ نداد
🔴
خبرنگار از ترامپ می‌پرسد: مذاکرات چطور پیش رفت؟
🔴
ترامپ: عالی، چین زیباست.
🔴
خبرنگار: درباره تایوان صحبت کردی؟
🔴
ترامپ جواب نمی‌دهد.
🔴
خبرنگار تکرار می‌کند: درباره تایوان صحبت کردی؟
🔴
ترامپ جواب نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/alonews/119847" target="_blank">📅 09:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119846">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نخست‌وزیر ژاپن از عبور یک کشتی ژاپنی دیگر از تنگه هرمز خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/alonews/119846" target="_blank">📅 09:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119845">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کیفرخواست زیباکلام و مدیرمسئول خبرگزاری آنا صادر شد/ ممنوعیت زیباکلام از انجام هرگونه فعالیت رسانه‌ای به مدت سه ماه
🔴
هفته گذشته و در پی مصاحبه صادق زیبا کلام با خبرگزاری آنا (برنامه پل حافظ)، دادستانی تهران علیه نامبرده و رسانه منتشرکننده اظهارات وی اعلام جرم کرد.
🔴
پس از تشکیل پرونده قضایی برای نامبردگان، متهمان به مرجع قضایی مراجعه کردند و پس از اخذ دفاعیات، تفهیم اتهام شدند.
🔴
در نهایت با توجه به مستندات و تحقیقات صورت‌گرفته قرار جلب به دادرسی و کیفرخواست پرونده صادر شد.
🔴
همچنین قرار نظارت قضایی ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی به مدت سه‌ماه به صادق زیباکلام تفهیم و ابلاغ شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/alonews/119845" target="_blank">📅 09:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119844">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رویترز به نقل از شی جین پینگ: در جنگ تجاری هیچ برنده‌ای وجود ندارد؛ هر دو طرف به نتایج مثبتی دست یافته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/alonews/119844" target="_blank">📅 09:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119843">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ در پاسخ به سوالی درباره مذاکرات با شی جین‌پینگ گفت: «عالی است»
🔴
ترامپ در پاسخ به سوال خبرنگار هنگام بازدید از معبد بهشت در پایتخت چین گفت: «عالی است».
🔴
ترامپ گفت: «جای فوق‌العاده‌ای است. باورنکردنی است. چین زیباست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/alonews/119843" target="_blank">📅 09:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119842">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شی‌جین پینگ: تایوان مهم‌ترین مسئله در روابط چین و آمریکا است
🔴
رئیس‌جمهور چین، در جریان گفت‌وگو با دونالد ترامپ، تایوان را «مهم‌ترین مسئله در روابط چین و آمریکا» خواند
🔴
شی تأکید کرد که اگر این مسئله «به درستی» مدیریت شود، دو کشور می‌توانند از یک رابطه باثبات بهره‌مند شوند، اما در غیر این صورت، «دو کشور دچار تنش و حتی درگیری خواهند شد و کل روابط را در معرض خطر قرار خواهند داد»!
🔴
وی همچنین افزود که استقلال تایوان و صلح در تنگه تایوان «به اندازه آتش و آب ناسازگارند»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/alonews/119842" target="_blank">📅 09:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119841">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شی‌جین‌پینگ به ترامپ: تمام جهان در حال تماشای دیدار ما است.
🔴
آیا می‌توانیم، به نفع رفاه دو ملت‌مان و آینده بشریت، آینده‌ای روشن‌تر برای روابط دوجانبه‌مان بسازیم؟
🔴
در حال حاضر، تحولی که در یک قرن دیده نشده بود در سراسر جهان در حال تسریع است و وضعیت بین‌المللی سیال و پرتنش است.
🔴
جهان به یک چهارراه جدید رسیده است.
🔴
من همیشه معتقد بودم که دو کشور ما منافع مشترک بیشتری نسبت به تفاوت‌ها دارند.
🔴
موفقیت در یکی فرصتی برای دیگری است و یک رابطه دوجانبه پایدار برای جهان مفید است.
🔴
چین و ایالات متحده هر دو از همکاری سود می‌برند و از تقابل زیان می‌بینند. ما باید شریک باشیم، نه رقیب.
🔴
باید به یکدیگر کمک کنیم تا موفق شویم، با هم شکوفا شویم و راه درست برای کنار آمدن کشورهای بزرگ در عصر جدید را بیابیم.
﻿
🔴
ترامپ به شی جین پینگ: تو یک رهبر بزرگ هستی. من این را به همه می‌گویم که تو یک رهبر بزرگ هستی. گاهی اوقات مردم دوست ندارند من این را بگویم، اما من به هر حال می‌گویم چون حقیقت دارد.
🔴
من فقط حقیقت را می‌گویم
🔴
ترامپ به شی جین پینگ: افتخار است که با شما هستم. افتخار است که دوست شما باشم، و رابطه بین چین و ایالات متحده بهتر از همیشه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/alonews/119841" target="_blank">📅 09:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119840">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز: چین تمایلی برای کاهش حمایت از ایران در برابر آمریکا ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/alonews/119840" target="_blank">📅 08:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119839">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یک منبع امنیتی عراقی به شبکه العربیة: دو پهپاد حامل مواد منفجره، مقر یک حزب مخالف دولت ایران را در شمال اربیل هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/119839" target="_blank">📅 08:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119838">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a81f9fc6.mp4?token=m4BOga-seQqnqsXXRfN9C68yltYobMfQqJV2njxNGx7_9Wg2m-PrTWltcipcHix5YsSClcwnrL3mSFXdHmLT_g4OpcisjpypBnFuaG5SGaaKAvmrJ0j6nylO74NfebiRmFTa1CU-xCwGcICwSWLocGmHcgCcLRhmJ4mQifzMQTEjxrbUHMAgOkyUIwpeUry76w1oqwVuGGWDoG5vQcYl8LpVoj4B0_CRpV0NpkAWw7fe-f1xyBZG_cr6UdbbqxgaXAq_vtuIDJ216WGrLTdYx-AHEl8QrLsTqTcIneOVjV-patSh7lC-XY5QitLN86LXXexND4aamqbmTPGKz_K9uTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a81f9fc6.mp4?token=m4BOga-seQqnqsXXRfN9C68yltYobMfQqJV2njxNGx7_9Wg2m-PrTWltcipcHix5YsSClcwnrL3mSFXdHmLT_g4OpcisjpypBnFuaG5SGaaKAvmrJ0j6nylO74NfebiRmFTa1CU-xCwGcICwSWLocGmHcgCcLRhmJ4mQifzMQTEjxrbUHMAgOkyUIwpeUry76w1oqwVuGGWDoG5vQcYl8LpVoj4B0_CRpV0NpkAWw7fe-f1xyBZG_cr6UdbbqxgaXAq_vtuIDJ216WGrLTdYx-AHEl8QrLsTqTcIneOVjV-patSh7lC-XY5QitLN86LXXexND4aamqbmTPGKz_K9uTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار شی جی پینگ و دونالد ترامپ
🔴
دونالد ترامپ با ورود به محوطه تالار بزرگ خلق، با شی جینگ پینگ دیدار کرد و قرار است گفت‌و‌گوی دوجانبه انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/119838" target="_blank">📅 08:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119837">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f65176faa.mp4?token=UykVGo_gKhi0qKJV29a8Jo0-IF3BIWN7JR3BSQN5N24fE9lulZKILLLlP03VbNh_z-iErV7T_wq1nj2oiAtO1Vx8HrfUKsGzxr049V_nw2yUZluDEwzHOtVwAiXP7kq7L5cGe7B91Ldu11HUb0brrvRst-9j9-AYbEyZDcaSjlg-ReNawsbFtwC0W_NCS4ZE5mrTlVkCqx21D_nDeL2wMK7VDyeOH06IXCakzf8Lf9HYzcPk5hJ-eMZTPbfiGj3jF3piprpKkOWcDKST6Ftsv5hsLu6Llhdo8kx2jMgNEZcNob6LMeep4CVFqkABE-GB66gOEnpZHG9CnpqWtG8BWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f65176faa.mp4?token=UykVGo_gKhi0qKJV29a8Jo0-IF3BIWN7JR3BSQN5N24fE9lulZKILLLlP03VbNh_z-iErV7T_wq1nj2oiAtO1Vx8HrfUKsGzxr049V_nw2yUZluDEwzHOtVwAiXP7kq7L5cGe7B91Ldu11HUb0brrvRst-9j9-AYbEyZDcaSjlg-ReNawsbFtwC0W_NCS4ZE5mrTlVkCqx21D_nDeL2wMK7VDyeOH06IXCakzf8Lf9HYzcPk5hJ-eMZTPbfiGj3jF3piprpKkOWcDKST6Ftsv5hsLu6Llhdo8kx2jMgNEZcNob6LMeep4CVFqkABE-GB66gOEnpZHG9CnpqWtG8BWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جریمه سنگین دوربین‌های نظارتی چین برای مجری فاکس‌نیوز / برت بایر:
🔴
”به معنای واقعی کلمه همه جا دوربین وجود دارد.آنها همه چیز را می‌بینند... راننده ما به مدت ۲ دقیقه غیرقانونی پارک کرده و ۴۰ دلار جریمه شده است!"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/119837" target="_blank">📅 08:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119836">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laioWWpUIMghNHqfONyCrHYhL9gVblu1Yjx4Dn6TFAUTSc2EX0f4Y48mjw_U8T9jVzqScGRYZ-xoM0pnkxZ0CsJCo0if93K2CzrmBz0oaF1bQD7L_uXqAi_X8xfgGM6RfjUpwydBZ904BxAfR71VC49tiWT7fW3AoTUtIi3oIqECjQK9Li6j0sAVYs2okfKpt30bz9_HAAoI18fIqxzvuigQfSckkRbB84YCfM4LqH7CnqtBEagU2YmfjJRufLg-FpOH_D0lB-zAvX838rsmD-b5Ksxj_2h1sKsHqsGs8nNDAbszuJOlaxhCwEcB9n_t8Vi6nu3X-BgR4aSmg_q0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معین: مهدی تاج الکی میگه، من قرار نیست هیچ آهنگی واسه تیم فوتبال تو جام جهانی بخونم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/119836" target="_blank">📅 02:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119835">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGMOsdY1F7Xks2xzp7_pgRVZAJWK8KHqAE5We9dl_4kx9fVBhqBwpBDbqNaFYN8nCeLxVfvn_EI_8QEO68r97crHcMInsYvgVNNh8BwrXf5Zfz3YdKifPCG03q0le2EeEPj8oxliHYz5eXqZeaLijtMw0tyI1rAgJ-hFBYj7gCJpPbp9wHsr-uOk2BdBTbv5OLKeBTcO1PXiJxy247wSh-cwDKB0nbBq5PybKHErbyXd76y4zKyus4t9oGfhpx_0wzsp3T_wCjXRZEd7Kb9wCpiTK1w_z4IIIHh6qouxDZaf8fJ8aed4kyGa9si1Jj_okX79HUAp9X-Cr8niEKcR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش رویترز، ایالات متحده و چین توافق کردند که هیچ کشوری نباید اجازه داشته باشد عوارض حمل و نقل در تنگه هرمز را دریافت کند.
🔴
وزیر امور خارجه چین، وانگ یی، و وزیر امور خارجه ایالات متحده، مارکو روبیو، این موضوع را در تماس تلفنی آوریل مورد بحث قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/119835" target="_blank">📅 01:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119834">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ارتش اسرائیل: مدتی پیش حزب‌الله لبنان از جنوب این کشور با پهپاد و چندین موشک ضدتانک بهمون حمله کرد که هیچکس آسیبی ندید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/119834" target="_blank">📅 01:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119833">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef57f203e.mp4?token=FItVs7JvBW30N55mW_TPfatTHyMh4B32m6gVRUF05MBaEODG8SIux-lm2NujvZCw8KxobkXN_WZEunbxI0C0b2A9pZM2rgt1DYVuh0-m4dFUF7Mg0WjMEfyrXBWScQ33vPKGKNkw0YSuzZwiDSbaPxXVld3NJWJfGkwEXVlZuYX4Wemdsa8S_ixJgZUk_Q_bcSgZHd82OqQCSoQ2RbQfRLLYjyBwWWfnKCuNXrFGjZH-iIFUtbVfxXZpUsJNN5MCsxiA2Fc5ndsIt1w-lMMLoovgYYOYttkZSKzBrYQMwEwyVcrvcy2uasCRFe7hKppy9n4pQUCSpuhrvDz1yYuSHRAV3k03EYSBUVa1vQYXC86HeW5gXO5jooJOAYwJdKm-AnyQfltd45DDKDU1ReN0eKociWvOZzfcYHviFa7Al6XdY_g8vD_R-l35nE9Mj1QrcsmvKFvBPgAHwmlWxHLp6Yn7WZcD0yHjGCPwShtE630IVpfwp3u9QHCijsLOoEQyOpLteKw3bKB6khMX6u1yEFN7Sc9V_9xSflezEkEMDJz-8-df0SV11MgPQuRt30QlmFt5lmwc2PPi5R8HFI4MLCcBFpq9U_dOsh8sQQqhMvxFbBHfiUdSNVL2AGHbez5_cGBhY_HMkl8TsRfdKLJJmFjMiIMK0wAEgiwk2_xq-uY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef57f203e.mp4?token=FItVs7JvBW30N55mW_TPfatTHyMh4B32m6gVRUF05MBaEODG8SIux-lm2NujvZCw8KxobkXN_WZEunbxI0C0b2A9pZM2rgt1DYVuh0-m4dFUF7Mg0WjMEfyrXBWScQ33vPKGKNkw0YSuzZwiDSbaPxXVld3NJWJfGkwEXVlZuYX4Wemdsa8S_ixJgZUk_Q_bcSgZHd82OqQCSoQ2RbQfRLLYjyBwWWfnKCuNXrFGjZH-iIFUtbVfxXZpUsJNN5MCsxiA2Fc5ndsIt1w-lMMLoovgYYOYttkZSKzBrYQMwEwyVcrvcy2uasCRFe7hKppy9n4pQUCSpuhrvDz1yYuSHRAV3k03EYSBUVa1vQYXC86HeW5gXO5jooJOAYwJdKm-AnyQfltd45DDKDU1ReN0eKociWvOZzfcYHviFa7Al6XdY_g8vD_R-l35nE9Mj1QrcsmvKFvBPgAHwmlWxHLp6Yn7WZcD0yHjGCPwShtE630IVpfwp3u9QHCijsLOoEQyOpLteKw3bKB6khMX6u1yEFN7Sc9V_9xSflezEkEMDJz-8-df0SV11MgPQuRt30QlmFt5lmwc2PPi5R8HFI4MLCcBFpq9U_dOsh8sQQqhMvxFbBHfiUdSNVL2AGHbez5_cGBhY_HMkl8TsRfdKLJJmFjMiIMK0wAEgiwk2_xq-uY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاج: احتمالا معین موزیک رسمی تیم‌ملی رو بخونه!
@AloSport</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/119833" target="_blank">📅 01:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119832">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1rat1eX10Z2GoF87sQURJWEHKbmrGKGDGKH7cBoHfCSvjW8WlZmuXn7FKELaw7lxVCSm-1FxWkOoN5STv8Q6rMTRyRdZZiUtHhR8ywohG9SsDWwezDFg1dajW55UeAGg1K1M7U1EcL5fU70CUWRaJIbA4Uv3145Hr3bewrNnZTV6Zxpcry8wG1bzH-PeMg1Rdmc8Rl1RDpl3Jdnx9s-G8s1uoIQhi9ioh34743BL0tmOfzRjH1nsZbcvHQIhDKZHY6a84O5eBZMMnsp1zKNlLqMXmpyi6Tm14qbdHQEsBBTw5Sv9JpWbbtMgHVfDI_XZ6TusiNcQipYIUrSsmIJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا "نصرالله معین" قراره واسه تیم ملی فوتبال به مناسبت حضور تو جام جهانی 2026، آهنگ بخونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/119832" target="_blank">📅 01:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119831">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1278f5774c.mp4?token=AWnC8IpbSv-YUgUbcAFYQWiTCzXf-5FeNUmJWmL44lfFZnNIFN3_M8_FTS8wkTHo7q3L0fXX9zfHk3WCktgfWSHAJocsj-KLfU5qF-0ysZXTcaOQfIkqU0hAccA6AXC_a-7FWEkytbxWu3fcdIaMj2mH-lH0KsPOOkVQM4JW-zSBvhXLwOBFBLrj8eVK4Q4ZW9XsftK-qS2j_hhFNQT24f-4L1a_yoRnwBW8Trrf_87g_ANe-b7VCFjl9CimEfaJWt2P_YuCG6aICaszYxuqzHMpEOXn-LN6_uSXHQb81KaRCdAfsP4Wo_UbnkP53NkSGZhTQSgo3_lSBdIW8pAdKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1278f5774c.mp4?token=AWnC8IpbSv-YUgUbcAFYQWiTCzXf-5FeNUmJWmL44lfFZnNIFN3_M8_FTS8wkTHo7q3L0fXX9zfHk3WCktgfWSHAJocsj-KLfU5qF-0ysZXTcaOQfIkqU0hAccA6AXC_a-7FWEkytbxWu3fcdIaMj2mH-lH0KsPOOkVQM4JW-zSBvhXLwOBFBLrj8eVK4Q4ZW9XsftK-qS2j_hhFNQT24f-4L1a_yoRnwBW8Trrf_87g_ANe-b7VCFjl9CimEfaJWt2P_YuCG6aICaszYxuqzHMpEOXn-LN6_uSXHQb81KaRCdAfsP4Wo_UbnkP53NkSGZhTQSgo3_lSBdIW8pAdKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو : کشتی‌های چین توی خلیج فارس گیر افتادن  یه کشتی باری چینی هم آخر هفته آسیب دیده
- مطمئنم ایران عمداً این کار رو نکرده، ولی به هر حال اتفاق افتاده،واسه همین این کشتی‌های چینی اونجا گیر کردن
- این وضعیت خیلی بی‌ثبات‌کننده‌ست،حتی بیشتر از هر جای دیگه دنیا می‌تونه آسیا رو به هم بریزه، چون انرژی‌شون خیلی به این تنگه‌ها وابسته‌ست
- این به نفع خود چینه که این مسئله رو حل کنه
- ما امیدواریم بتونیم قانع‌شون کنیم نقش فعال‌تری بازی کنن تا ایران رو وادار کنن از کاری که الان تو خلیج فارس داره انجام می‌ده عقب‌نشینی کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/119831" target="_blank">📅 01:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119830">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کانال N12: ترامپ داره به صدور دستور برای از سرگیری درگیری با ایران فکر می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/119830" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119829">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhSMLHvFxSthf1fPIcvsuC7_ZS5MyAssQxki_rX9HVXBvfJYqR_8w34LlWTQmd0A3XGcz2_R3G9XfJgul3xrr-GKPoHWcpfYVwgNfaOE2uqjvnVkZ9wF1eX0589CaIwOqXAJ2VkxE9OgZA_9MVUz8iVXYY6YJp8eWcr0wcH4VDjsVtvjFSEbs1RodWjQyaEhJmt5rL9wtWnvXid16faZOkMSsCFISApyBtmKafQSSE0f46-qpfy3oc_yO_bWOP-WSNDfoQI8f8x91fFv151D0uvkMP3GNA318ARYAHQbuYal7SmHPle__9QRKRhAtdletskqagUk5lFhuYodSxjhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/119829" target="_blank">📅 00:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مدیرعامل شهر فرودگاهی امام : روزانه بین ۳۵ تا ۴۰ پرواز از فرودگاه انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/119828" target="_blank">📅 00:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
خوش‌چشم: ترامپ رفته چین التماس کنه تا میانجی بشه که ایران جنگ رو تموم کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/119827" target="_blank">📅 00:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20b6d8ff5.mp4?token=ODEv7Qt42ViDa6mvHHQZjzyqC5ugPbiBX36w30VqSyEnmi8I21-qsNJGGG7cU27Xc2f-2blwweaMxikqxA0_7V2x_des85q4dHEi1vPobsgQuHayPlX7mn52mfVE_c52u9Kr2TlfeyY9blxYjtCtC7qdWA_aNFZSsK-axBI6V1MbanzS2HGIjCDI_ETxuGcbmkJNIG9YCPTWIFAvecYqSTi1MYTdHCqQiGN_O2a0b0p6YVa3am-ZPWsFMoCU8JGmvwJ7HXHl3UlN5uIVNBkJicu3Sb4d7MJqC_3wbIjDOII3KLyjAjzsfiX9v_IZ52K-0Z_3QTL_BMNK7BEel2YtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20b6d8ff5.mp4?token=ODEv7Qt42ViDa6mvHHQZjzyqC5ugPbiBX36w30VqSyEnmi8I21-qsNJGGG7cU27Xc2f-2blwweaMxikqxA0_7V2x_des85q4dHEi1vPobsgQuHayPlX7mn52mfVE_c52u9Kr2TlfeyY9blxYjtCtC7qdWA_aNFZSsK-axBI6V1MbanzS2HGIjCDI_ETxuGcbmkJNIG9YCPTWIFAvecYqSTi1MYTdHCqQiGN_O2a0b0p6YVa3am-ZPWsFMoCU8JGmvwJ7HXHl3UlN5uIVNBkJicu3Sb4d7MJqC_3wbIjDOII3KLyjAjzsfiX9v_IZ52K-0Z_3QTL_BMNK7BEel2YtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمرینه بمب‌افکنِ " B-52 " و فرود به پایگاه فِرفورد بریتانیا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/119826" target="_blank">📅 00:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOrtpSx4S971AszgyOQKsute6mPnTb0hWYVPNZ9K1PGQUqg7l6AqnrB6rgnpdS4HPvqd-V11j2e9oY9bbIYCv4TYNsyxPWVFFPUE39JOu6GIs-Y74hKnRCgdfbaY0QHsQB3_WQgcrqgt6-XXNlMSqo_JjyvYi52NWVmmh4VvFOpzNV6mfdetqporNvoN4xic9XL0AB4_JBXzB47a4wCggTTE3H_JZgcobdP5VY-srL6dM2xCyo39jpsayug38YpL0wd5xWeFzDARkI2eJQkI04Vsi2GwmC83ij0Bl5swmwEcYJe-L0EcosdpfMNis02sKGWKlBNmVBD-Ii6UMV1q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: در تاریخ ۲۸ خرداد، شبکه اجتماعی مای دات به‌صورت فراگیر برای عموم بازگشایی و طی مراسمی در برج میلاد رونمایی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/119825" target="_blank">📅 00:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
روزنامه South China Morning Post: شرکت تصاویر ماهواره‌ای چینی MizarVision که با تحلیل‌های خود از استقرارهای نظامی آمریکا در جنگ آمریکا و اسرائیل علیه ایران به شهرت رسید، افزوده شدن خود به فهرست تحریم‌های آمریکا را به عنوان نشان افتخاری در کمپین استخدامی خود به کار می‌برد.
🔴
این استارت‌آپ اطلاعاتی با منابع باز (OSINT) که با نام رسمی Meentropy Technology Hangzhou Co Ltd شناخته می‌شود، در تحلیل داده‌های ماهواره‌های تجاری تخصص دارد و در ماه‌های اخیر چندین بار تحرکات نظامی آمریکا را رصد کرده است.
🔴
این شرکت روز جمعه به فهرست تحریم وزارت خزانه‌داری آمریکا اضافه شد که در  پی انتشار «تصاویر با منبع باز که جزئیات فعالیت نظامی آمریکا را در جریان عملیات خشم حماسی (Epic Fury) نشان می‌داد»، صورت گرفته است
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/119824" target="_blank">📅 00:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcxDA20UDG_J8alNVkSrS2RwxK9Q9u1pNjCSsESxJRvVxLQQSGKADwfjx8PaUGxJ5BiB3_BtBKHgMkworAgz3j7f8aSOtN97MGgvkIA8tHVERsJWdu1Bu4_sBCpTtuwoAjTp-NYvNjafn7d-qfoTTneiS-v3MC0ONGUZhZ3LY7BqlFWWoynQULq8qo56P0tHC6_hPVu8oowRcE7gqZeF3tQPug-2xOaXfV8GUIrqoO3UeqHCB-6U67grfniozoi-SuJm3QuEY-12wXJRkI_77FaQl_ZJ8YRaIX58IuCSowXSE_CZEO6MUxdVnWQnX9KVGH8WOu6e96If7dVuIB-GWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPVoQMh_e85-Dl9UtHYdInxa4ya9xf3ZG9FRsHk9yIar1R8_cFa_vSC6oAVLV_up05YPZ4JTOoQ08EKz-o64uAHSLVFcp2L2TYTpyyIRT96Kvu9JNMF0ozzvXITZl54PYOk5iTF4YoZlCgo1h_Iqs-OtjoD7t6fLSlIVCWCWO6eaPkdD4L6m-Xai9uz965FLD_mAjDgwC11Iwa4SRGG5PuWRrCAcpZQkVYmmYfmqFf22DVNNiTTXpHmrEsz7PLXOqbb75cKGlYAiYiMErpv_YHBFiXDKMNxI36UosU-4gK9_B0ZDbsbWJaJEZ-V0KQFSXmDJOjLHYLMI6w9lHrgPYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هزینه نجومی رجیستری گوشی آیفون ۱۷ و گلکسی سامسونگ!
🔴
رجیستری پایین ترین گیگ آیفون ۱۷ پرومکس: ۶۰۰ دلار!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/119822" target="_blank">📅 00:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
امارات : خبرهایی که درباره سفر نتانیاهو به امارات پخش شده، صحت نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/119821" target="_blank">📅 00:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff5j2zs7YNFC9ednVUaGBLSUhiCuw3fgaQCuNnYvfjYfqKPNX_BE39ZIU89facKaK7XWO2BkP982OZ5UeRA8hU0U30EclCjdit4PJgYdxMMXRh6kCbjmePDYRi4DTq85xasWVo-qklKggnRpf8tR7vqTG58HW33Oqa_Lwcrc0CN39s9rKccXaDImGEnfsYHyW3ov3IrhWh6wVKbI6xkyTq8zu9ykgedDyQ111A0r6Ay6Zz4_Cle1JGmdi9pe0n5NhNEzBGeG4qjIIARDHCt__QskoQOqYmW0hv3dmbBXZnJxmXim_iin9WfapPFrx8Wvvk92KgX4zMqGobERbhFPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: نتانیاهو اکنون به‌صورت علنی آنچه را که نهادهای امنیتی ایران مدت‌ها قبل به رهبری ما منتقل کرده بودند، افشا کرده است.
🔴
دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است؛ و همکاری و همدستی با اسرائیل در این مسیر، غیرقابل بخشش است.
🔴
کسانی که در همدستی با اسرائیل برای ایجاد تفرقه نقش دارند، باید پاسخگو باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/119820" target="_blank">📅 23:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وال‌استریت ژورنال: در حالی‌که نگرانی‌هایی درباره کاهش ذخیره مهمات ایالات متحده وجود دارد، پنتاگون در حال تلاش برای خرید ۱۰٬۰۰۰ موشک کروز کم‌هزینه در طول سه سال است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/119819" target="_blank">📅 23:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119818">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خارجه ایالات متحده: امروز، وزارت خارجه به‌طور عمومی پیشنهاد سخاوتمندانه ایالات متحده برای ارائه ۱۰۰ میلیون دلار کمک بشردوستانه مستقیم اضافی به مردم کوبا را که با هماهنگی کلیسای کاتولیک و سایر سازمان‌های بشردوستانه مستقل و قابل اعتماد توزیع خواهد شد، مجدداً اعلام می‌کند.
🔴
تصمیم با رژیم کوبا است که پیشنهاد کمک ما را بپذیرد یا از کمک‌های حیاتی نجات‌بخش زندگی خودداری کند و در نهایت در برابر مردم کوبا به دلیل ایستادگی در برابر کمک‌های حیاتی پاسخگو باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/119818" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119817">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf0426b5.mp4?token=hah0CVcHDm_EunieI60T19_G43Qot7ZhY7m8hRLwLJivfFFXV0iFxjWr9ikKYeENi6EouKxCUSnUKm31GU_a7khjQka2OWHYSI5gfI1XHqQXQIYkf-m6u0H8Hckx8ABy5SbRV5EXta_wL-LDIigR2ahvHYvgq4lq44FFPKcgPd_ArrEpaSVyGHVjlDuPFwJHt4wVB_GtnKkVS-_buSt6r1yZu5OczxCMd7IfQNlDTg-9_m9EuyNU4nAz42a9N8s5CHjH2E6mFMJQ6TEbnRJvLXdGHtQdMeYm8oPjRoI2YF2GSwPkkZ96H5PCLH-gXCjG1mtsJnh2MtSZv-ZXyI6vmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf0426b5.mp4?token=hah0CVcHDm_EunieI60T19_G43Qot7ZhY7m8hRLwLJivfFFXV0iFxjWr9ikKYeENi6EouKxCUSnUKm31GU_a7khjQka2OWHYSI5gfI1XHqQXQIYkf-m6u0H8Hckx8ABy5SbRV5EXta_wL-LDIigR2ahvHYvgq4lq44FFPKcgPd_ArrEpaSVyGHVjlDuPFwJHt4wVB_GtnKkVS-_buSt6r1yZu5OczxCMd7IfQNlDTg-9_m9EuyNU4nAz42a9N8s5CHjH2E6mFMJQ6TEbnRJvLXdGHtQdMeYm8oPjRoI2YF2GSwPkkZ96H5PCLH-gXCjG1mtsJnh2MtSZv-ZXyI6vmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوین وارش با رأی ۵۴ به ۴۵ سنا ایالات متحده به عنوان رئیس فدرال رزرو تأیید شد.
🔴
جان فترمن تنها دموکراتی بود که از این تأیید حمایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/119817" target="_blank">📅 23:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر امور خارجه سوریه: دمشق خواهان دستیابی به توافقی امنیتی با اسرائیل است که بر پایه احترام متقابل به حاکمیت دو طرف و حفظ ثبات منطقه شکل بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/119816" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119815">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرنگار سی‌بی‌اس مدعی شد: پیشرفت‌هایی در مذاکرات با ایران دیده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/119815" target="_blank">📅 23:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119814">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: امارات و اسرائیل به دنبال علنی‌تر کردن روابط خود هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/119814" target="_blank">📅 23:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119813">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
منابع عراقی از شنیده‌شدن صدای چندین انفجار در اربیل عراق خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/119813" target="_blank">📅 23:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119812">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شبکه العربی: حزب لیکود درخواست انحلال کنست (پارلمان) اسرائیل و برگزاری انتخابات زودهنگام را ارائه داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/119812" target="_blank">📅 23:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119811">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کیر استارمر ، نخست‌وزیر انگلیس در نخستین جلسه مجلس عوام پس از بازگشایی پارلمان، بار دیگر ورود شتاب‌زده به جنگ علیه ایران را خلاف منافع کشورش دانست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/119811" target="_blank">📅 22:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm-TflWD9Tf4fJ4xe4nyyTw__rzfmQyU8ETjRCQFPYPlSm0UfcsvrHVlzGUzsAIKhop99q3ZbljuKNboDHvW3Qh0SZ3_hdZI1HjvpR-1OK24pzgszOGzhdHvSf4UQv9YA15szJL6q3iSsFDe1PtaQdng7yP6XubVM-NlihuYSWfp9xpRTtXsT86uOMgYi5eq0GcRjglLYvuguXxiAPlyvR2w-Su67cm1t_OYelRK4IMsx3gjrrUCSJ51ac1EPoB9tzwTTGRpVZYyRcYpejr1j2WPaJdPRhrlit55ray_ZUNUbHfNSKCiR5bMP5yVEgfHDmtA9j2h36U0vLlK9UQBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین رئیس‌جمهور ترامپ را با حضور معاون رئیس‌جمهور رده‌بالا اما عمدتاً تشریفاتی، هان ژنگ، در پکن به گرمی پذیرایی کرد؛ انتخابی که طبق گزارش نیویورک تایمز، نشان‌دهنده مبادله نمادگرایی به جای ماهیت توسط پکن است.
🔴
ترامپ سه‌شنبه شب با استقبال یک ارکستر نظامی، گارد افتخاری و صدها جوان در حال پرچم‌زنی وارد شد — نمایشی که برای تحت تأثیر قرار دادن رئیس‌جمهوری که به جایگاه حساس است طراحی شده، در حالی که چین زمان می‌خرد تا از بازگشت به تشدید اقتصادی اجتناب کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/119810" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کاخ سفید در نظر دارد که رئیس‌جمهور ترامپ به مناسبت ۲۵۰امین سالگرد آمریکا، ۲۵۰ عفو صادر کند، احتمالاً در ۱۴ ژوئن یا ۴ ژوئیه، طبق گزارش WSJ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/119809" target="_blank">📅 22:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
جنیفر جیکوبز خبرنگار سی‌بی‌اس:
جی‌دی ونس معاون رئیس‌جمهور امریکا به من گفت که امروز صبح با جرد کوشنر و استیو ویتکاف درباره ایران گفتگو کرده، همچنین با مقامات عرب.
🔴
او مدعی شد که پیشرفت‌ در حال حصول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/119808" target="_blank">📅 22:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119807">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر خارجه کوبا: حمله آمریکا منجر به حمام خون خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/119807" target="_blank">📅 22:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119806">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سوپراپلیکیشن ایتا اعلام کرد امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/119806" target="_blank">📅 22:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119805">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ادعای ونس، معاون رئیس‌جمهور آمریکا: ما درگیر یک فرایند دیپلماتیک فعال برای اطمینان از نداشتن سلاح هسته‌ای توسط ایران هستیم
🔴
رئیس‌جمهور گزینه‌های متعددی دیپلماتیک و نظامی پیش رو دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/119805" target="_blank">📅 22:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119804">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرنگار: آیا شما با موضع ترامپ موافقید که وضعیت مالی آمریکایی‌ها نباید در فرآیند تصمیم‌گیری درباره [ایران] مد نظر قرار گیرد؟
🔴
جی‌دی ونس: خب، فکر نمی‌کنم رئیس‌جمهور چنین چیزی گفته باشد. به نظرم این تحریف سخنان رئیس‌جمهور است.
🔴
اما ببینید، من با رئیس‌جمهور موافقم که ایران نباید سلاح هسته‌ای داشته باشد.
🔴
هدف اساسی این است که رئیس‌جمهور می‌خواهد جهان را ایمن کند، اما به طور خاص، مردم آمریکا را از داشتن سلاح هسته‌ای توسط ایران ایمن نگه دارد.
🔴
ما به وضعیت اقتصادی مردم آمریکا اهمیت می‌دهیم. ما همچنین چالش‌های متعدد دیگری هم داریم. طبیعتاً رئیس‌جمهور باید به طور همزمان با همه این چالش‌ها مواجه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/119804" target="_blank">📅 22:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119803">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ادعای نیویورک تایمز: شرکت‌‌های چینی به دنبال فروش سلاح به ایران هستند و قصد دارند آنها را از طریق کشورهای دیگر ارسال کنند تا منبع خود را پنهان کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/119803" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119802">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از یک منبع نظامی گزارش داد: حزب‌الله از ابتدای جنگ ۴۵۰ پهپاد پرتاب کرده است که شامل ۱۲۰ پهپادی است که با استفاده از فیبر نوری عمل می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/119802" target="_blank">📅 22:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119801">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مقام ارشد ضدتروریسم کاخ سفید: ترامپ نامه‌ای خطاب به معاون خود، «جی‌دی ونس» نوشته که در کشوی میزش در کاخ سفید نگه داشته می‌شود تا در صورت مرگ یا ترور احتمالی وی، مورد استفاده قرار گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/119801" target="_blank">📅 21:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119800">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrBLBezZf3os7AcE6Kntp2XJAzp4VOQ3uP7ng6rrz7Km6-vzROP4cbdEy0iIzsT7aD3kdde-pxlKo2y3j_AxCZDSyu5pjamgUlBeg-x-WZKSA6NXUQ_Yo9sEWhY0YylOVyshXyiR4XqwIxxHhslkUzK5EnAs7xkq_Mj5JRAErrhVsidJH8zBsFonxaXmZTQisjpxXF2tWPKHHw1h_s9PgYWAjvZEAhCuXd-ZBurp9nfN6kOKvCbH0n4XA0_Pe11cT7zTouKNRbEE5c4ddNj2dbte5PypiHGoLGkEIYPwMMzFFARZKOL5xge270fbm0dmqox6bQRWoUnvVcMupdGdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">املت قسطی هم اومد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/119800" target="_blank">📅 21:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119799">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4KInpR4B30rRJizVD2G2nJomGtfZgeBVcGEa-DkjgOBYVP0UGaoLO3Khu7F6Q5TKXFT0Xf-7SbQAjq4YSxKU2yY_3a4l7BiWgQb5NBR0i5znGRhIGqTOqJTZF80Gev3ukjAgj0a6dFyGUJttw_SW075Hr-Md4p1rtLXnOcLiiDmw95dYg2WaI8XFvaO8StiETvX4lIj4sUz3vHqdci1Oc8gG3z5m7lGo3WS7v3zSpxTNbQF7qNuYAAU67n2E-dP1gMz0lazy-SMxrgCzWy8dp5Zlj3lat5YFoBCo07YukEoamlbRcN6ZBKWlSjBC7yW_uwArQy9UnCieV0vadjBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پیراهن تیم ملی برای جام جهانی 2026 رونمایی شد که دقیقا شبیه پیراهن 2014!
@AloSport</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/119799" target="_blank">📅 21:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119798">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزیر گردشگری: گردشگری پساجنگ جهش پیدا خواهد کرد چون مردم دنیا علاقه‌مندند ایران جدید پس از جنگ و واقعیت‌های آن را از نزدیک ببینند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/119798" target="_blank">📅 21:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
المانیتور: عربستان در زمان جنگ مخفیانه به ایران حمله کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/119797" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119796">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
به گزارش ان‌بی‌سی و به نقل از داده‌های ناوبری، چندین کشتی باری و نفتکش مرتبط با چین در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/119796" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119795">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d734fbc3e.mp4?token=MoqpWdz_YGNtYWiSWirqIbiiwOX6trBdJpsi3fVs0gy0i5RobI_t0MnQWLmVvgZl42y0TR9APMnggIKv3ds-MY0t17WDkChK7o_FBVDDg_2uXZSOBCpFtfi0G1tfgpzYlNfe3BCocGyHXQBCvlYOPSpUoPQmKinQrVe6arHHH4YpxZ0qdwNxQExG5w4mdKXxKHrITP6sInFmPuOyteIB9s-bKiiBc9d_gPGzdwtO7rvlkbDpg1oinQZYi3IgHD7xYJFHo6y2PwuzXZh_qXOXbjzNdP1Ko-tH7E3as6Pp06infgA7_E7io5oEVjkODO5UsGQNdd5_znEvZL6LZRGRrFLVNSTQdtlhOGv_qUBZceCkWKzCHPgx9LjBqQmBVnw9RaBzni-NkiomEt18IY8wGoOzJWnfQpnenE0X84yXTVWphCr2RFmbOll7pvD08YXtPM4CYC1yXMsM5a47UuMhy6ORPALEs_xBzrWnfT8CVffuM7718nn5V0nB_KoWio_x_zBsYiSHRi9d0NWYOH7NzJufKYapqpipIKsF1s-p2YoH2LyZoIRiBdRZ7dWSCsqCB9uxEasE9a6ja6LBaf-2c_AO8oQRtcr1lnTZ9vklQ8l5ct17BehjxcHWctwGiVwAMgBGLsanvoSrZBaUeC4W4q7_wT0xXatPtVTKbD_J1DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d734fbc3e.mp4?token=MoqpWdz_YGNtYWiSWirqIbiiwOX6trBdJpsi3fVs0gy0i5RobI_t0MnQWLmVvgZl42y0TR9APMnggIKv3ds-MY0t17WDkChK7o_FBVDDg_2uXZSOBCpFtfi0G1tfgpzYlNfe3BCocGyHXQBCvlYOPSpUoPQmKinQrVe6arHHH4YpxZ0qdwNxQExG5w4mdKXxKHrITP6sInFmPuOyteIB9s-bKiiBc9d_gPGzdwtO7rvlkbDpg1oinQZYi3IgHD7xYJFHo6y2PwuzXZh_qXOXbjzNdP1Ko-tH7E3as6Pp06infgA7_E7io5oEVjkODO5UsGQNdd5_znEvZL6LZRGRrFLVNSTQdtlhOGv_qUBZceCkWKzCHPgx9LjBqQmBVnw9RaBzni-NkiomEt18IY8wGoOzJWnfQpnenE0X84yXTVWphCr2RFmbOll7pvD08YXtPM4CYC1yXMsM5a47UuMhy6ORPALEs_xBzrWnfT8CVffuM7718nn5V0nB_KoWio_x_zBsYiSHRi9d0NWYOH7NzJufKYapqpipIKsF1s-p2YoH2LyZoIRiBdRZ7dWSCsqCB9uxEasE9a6ja6LBaf-2c_AO8oQRtcr1lnTZ9vklQ8l5ct17BehjxcHWctwGiVwAMgBGLsanvoSrZBaUeC4W4q7_wT0xXatPtVTKbD_J1DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دیسکوهای ایرانی دبی چه میگذرد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/119795" target="_blank">📅 21:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119794">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/119794" target="_blank">📅 21:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119793">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/119793" target="_blank">📅 21:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119792">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/alonews/119792" target="_blank">📅 21:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119791">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزیر خارجه عربستان: امنیت تنگه هرمز اساس ثبات اقتصاد جهانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/119791" target="_blank">📅 21:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ادعای رویترز : منابع متعددی که از جزئیات ماجرا آگاه هستند، اعلام کردند که در جریان جنگ با ایران، جنگنده‌های عربستان سعودی اهدافی مرتبط با شبه‌نظامیان تحت حمایت تهران را در عراق بمباران کردند. بعلاوه، حملات تلافی‌جویانه‌ای نیز از کویت به داخل خاک عراق انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/119790" target="_blank">📅 21:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119787">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXa94xXAogV5bc0sBsQhVnStzr0VY408QqjpO7KKX1WBFXBH6f0-LwSOmQtAcsQ18noT-vnWS4oVAnUO1tZI3Hkm-ywi5gpPVSDOVeydNvUlZbDK4yhogOwz5wnKyIkM_STBef7dqQ9rDIF3H9H6l51j75Q5B7TrxEDoU4UOwzozVii5-iwvbCZuft10LEiLssjXLWrxBZEgqlBBTVB46utvDQaUF6cS4LCEIG5U0nFZFKnVL11MDeTb47Jd8LXygcn0JrqPJlFNGM1m0wxBqN3dX6yUN6xZf7VRSHEOsSERwLqHX8JfD6Iz5v6YegxYWGk72wYYpobnc3E7qBsy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP-gegI3qVXBOR8vvJdG2dxmY3Nb8wu4cHYuXEcKZm8JWXCV0Fo0LhiG0CpPRijQ2D-RpayL-80d8OPLoheFZp7Wu9bsxyFzdnGrcXnWsld2wCbD3B3ZQVL4HdlhkPm9ionaK4bO0LZ4pYlP3lmi2qT-Tu1CebX0xcqNSoyD-bQR5U6c_taxHO7p3K-SZy1RZSQa6JIPMOAmFHaKYPEY-PJcsyHWxIGmY_iTZXiDMshFgPAH60HtElribefxFvzWPg5dsR5vD3Nt82STdc8MN_u0T7EpyyZlH-JABfldDS5jw2JtacDl5E3IqYI62T6f6sOk8odjPvSik2C7RRy_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxFpsuQmMpPrR7imQMQqAJTRkh0sYcvroju-JSEXRS6_di84_j1UWHqJt2R6_s3-AhbuoJLuZuB1xjKMhSVcBT6VLq-1YXRHhTKMGAFNiS1oIenSlDKbo27hYoJq4dBvPR4PZ-d1FlqSWD6ibJe7OJlC5AJBayu6PO2CNq1Sni2r6MtIuSwwty_SKHdXEe44mWG3Zp6_dpqRnd27KOZjAavsGsNtTtWRytXyUbVW3oNbAoFpYZtN_RUNH2gCe0lkpaeg64LEi7Lcwnvdj0DTnOBOVK8NpB-AHlwYjsEww_9gbdERthYGzJsDsJv7ZvmpdoxV7ULDfUwwJ8vrp-y2Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سرباز اوکراینی با دوش پرتاب FN-16 چینی مشاهده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/119787" target="_blank">📅 20:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119786">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هفتمین رأی‌گیری در سنا برای پایان جنگ علیه ایران شکست خورد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/119786" target="_blank">📅 20:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119785">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دفتر نخست‌وزیری اسرائیل: در میانهٔ جنگ اخیر، بنیامین نتانیاهو سفری مخفیانه به امارات متحدهٔ عربی داشته و با شیخ محمد بن زاید، رئیس‌ امارات، دیدار کرده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/119785" target="_blank">📅 20:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119784">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
هفتمین رأی‌گیری در سنا برای پایان جنگ علیه ایران شکست خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/119784" target="_blank">📅 20:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119783">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
عراقچی : کویت به‌صورت غیرقانونی به یه قایق ایرانی حمله کرده و ۴ تا از شهرامون رو تو خلیج فارس بازداشت کرده
🔴
ما آزادی فوری‌شون رو می‌خوایم و حق پاسخ‌گویی هم برای خودمون محفوظ می‌دونیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/119783" target="_blank">📅 20:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119782">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اکونومیست: طولانی شدن بحران ایران می‌تواند آسیب جبران‌ناپذیری به کشورهای حاشیه خلیج‌ [فارس] وارد کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/119782" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119781">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ارتش آمریکا به دلیل عوامل متعددی از جمله جنگ با ایران با کسری بودجه غیرمنتظره‌ای مواجه است، به طوری که ذخایر مهمات از سال ۲۰۲۲ به دلیل حمایت از اوکراین کاهش یافته و اکنون با درگیری ایران بیشتر تحت فشار قرار گرفته است، طبق گفته یک مقام آمریکایی که با الجزیره صحبت کرده است.
🔴
این مقام تأکید کرد که این کسری بر آمادگی رزمی تأثیر نخواهد گذاشت اما هشدار داد که در صورت عدم تصویب بودجه دفاعی ۱.۵ تریلیون دلاری، ممکن است تصمیمات سختی لازم باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/119781" target="_blank">📅 20:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119780">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بلومبرگ: عربستان به اوپک اعلام کرد که تولید نفت خام این کشور در ماه آوریل ۶۵۱ هزار بشکه در روز  کاهش یافته و به پایین‌ترین سطح از سال ۱۹۹۰ در جریان جنگ خلیج فارس رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/119780" target="_blank">📅 19:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119779">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
با اعلام قوه قضاییه جمهوری اسلامی، احسان افرشته به اتهام «همکاری با اسرائیل»، بامداد چهارشنبه اعدام شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/119779" target="_blank">📅 19:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119778">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا، می‌گوید ایران "به طرز ترسناکی نزدیک" به اورانیوم با درجه تسلیحاتی است — که در حال حاضر تا ۶۰٪ غنی‌سازی شده است، در حالی که برای ساخت سلاح هسته‌ای به ۹۰٪ نیاز است.
🔴
او می‌گوید ایران ممکن است چند هفته تا رسیدن به این آستانه فاصله داشته باشد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/119778" target="_blank">📅 19:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119777">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53f547919.mp4?token=TylopYiPm2iX7vjz3BkcU-GZJ9g4qrbI3iUchlCwibqvFa9bXLufKTRG6hSLfXUgZAhFD1PsjvbOHlZrZVIPVDvFPOmkwjYfLuKSpAdRBu1-U_unxCghY4louN0lJ3SBjNZJ-wNQZB4QYR-YkGdFO0_gkdR1A07Gp-jZ1qGG5x9rh8iPsmQPNlLzXNzNyuU15_LaVivwvSNKlJ9-yeEG860gz3iXDFLrvtHUdhlslFZmjkQ4K69f3jD1Vs1CfpG3v5ZD7xpWt6nFGh92J8Zn7hpWIWrE8L0A2yrbQRhPXoV8pTtpWew87j1J1TXi_J5-HReqRqPV7BdrfTpP2zYosg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53f547919.mp4?token=TylopYiPm2iX7vjz3BkcU-GZJ9g4qrbI3iUchlCwibqvFa9bXLufKTRG6hSLfXUgZAhFD1PsjvbOHlZrZVIPVDvFPOmkwjYfLuKSpAdRBu1-U_unxCghY4louN0lJ3SBjNZJ-wNQZB4QYR-YkGdFO0_gkdR1A07Gp-jZ1qGG5x9rh8iPsmQPNlLzXNzNyuU15_LaVivwvSNKlJ9-yeEG860gz3iXDFLrvtHUdhlslFZmjkQ4K69f3jD1Vs1CfpG3v5ZD7xpWt6nFGh92J8Zn7hpWIWrE8L0A2yrbQRhPXoV8pTtpWew87j1J1TXi_J5-HReqRqPV7BdrfTpP2zYosg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید نتانیاهو نخست وزیر اسرائیل داخل ایکس : ما پیروز خواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/119777" target="_blank">📅 19:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119776">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر نیرو: تابستان خاموشی نخواهیم داشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119776" target="_blank">📅 19:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119775">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
دولت فرانسه از بیم شیوع ویروس هانتا ۱۷۰۰ نفر را در یکی کشتی در ساحل شهر بوردو قرنطینه کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/119775" target="_blank">📅 19:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119774">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBfosa3S3fguSqOVxK6DiuljBWhKjm5ifvncVTwW29HIKKlwG1mfq_Gp7OWajA81_sZGf9QB-GK4eGyZEmJs_E8ODfzZLShPIhzooXz9J0gWaOQoGYkWR8PIny4GiCuMFy4PLFF5B_McrBsq4TmnMmA7kDtvJlZgySm3nXWUpuN3euetouNKjLVVAHbhgdYyjMVfaGzdnPZTJb90wJjSwq14deMwslrrnvXH29peKDpDEta55ekNAvlth6-nq4yU8dxqBGz20h87Oddc1Z-6XhvNX8IuuxpWFKkGlnqTrI0AHeZQUQ6WuKpdtBCLw95-1LYCBjJZxyKG0sfpaTypiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی وارد هند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/119774" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119773">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
تحلیل سی‌تی بانک: انتظار نمی‌رود دیدار ترامپ با شی جین پینگ بن‌بست موجود میان آمریکا و ایران را بشکند
🔴
بنابر تحلیل سی‌تی بانک، انتظار نمی‌رود دیدار دونالد ترامپ، رئیس‌جمهور آمریکا، با شی جین پینگ، رهبر چین، بن‌بست موجود میان آمریکا و ایران را بشکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/119773" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119772">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای امور خارجه ایران و جمهوری آذربایجان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/119772" target="_blank">📅 19:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119771">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e876ccef94.mp4?token=u8mdq2_sYSYrEJ_g0OtLReyJ87M--FWWaXkFjf07695rrCB2zekDg8ClLWPZOCpE5lIvMRVFy1C60AxlfQwjL2RUP3E559jalvGoWezywkR2Kvfn82fyHFVBzCPmZXoLnFufY9FGtFI9NKkTOezQOBd3v3y-P0DPLNLlHUK1VprReRXnYReBpnQv3sEF4JrnJBDZClasvtoGE8U5UFeXA7Ew4UQQC-WbQ_ATRckUc97s0k1i6u0ne1BToBLB8brbkw2kCa-oALFQMKCNvyWdtkzJob7vVjz_WvsuNNP0b_vhgzaXCAS9bdzXOB_4gLbOb_aTTVIKd5FR6NukY29bcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e876ccef94.mp4?token=u8mdq2_sYSYrEJ_g0OtLReyJ87M--FWWaXkFjf07695rrCB2zekDg8ClLWPZOCpE5lIvMRVFy1C60AxlfQwjL2RUP3E559jalvGoWezywkR2Kvfn82fyHFVBzCPmZXoLnFufY9FGtFI9NKkTOezQOBd3v3y-P0DPLNLlHUK1VprReRXnYReBpnQv3sEF4JrnJBDZClasvtoGE8U5UFeXA7Ew4UQQC-WbQ_ATRckUc97s0k1i6u0ne1BToBLB8brbkw2kCa-oALFQMKCNvyWdtkzJob7vVjz_WvsuNNP0b_vhgzaXCAS9bdzXOB_4gLbOb_aTTVIKd5FR6NukY29bcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل ماکرون: کل اقتصاد جهانی به وضوح تحت تأثیر بسته شدن تنگه هرمز قرار گرفته است، اما قاره آفریقا به‌ویژه تحت تأثیر است.
🔴
چندین کشور قیمت سوخت خود را بیش از ۳۰٪ افزایش داده‌اند، همراه با افزایش‌های عظیم در کودهای شیمیایی و خطرات قطع در ماه‌های آینده که امنیت غذایی را به خطر می‌اندازد.
🔴
در مواجهه با این وضعیت، باید از اقتصاد آفریقا بیش از پیش حمایت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/119771" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119770">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZyHpG1l8_ImIS5K7LD5RpyKmiCmIC5q9G20HeJchWKqp5jUjv0cKPwygIUiNlpr-8al8GxA2OWgSx2IflxXERzR08JYRv8BhBYrytvK8hDrqFdLdWTqUNiWSxnq4NstjT-T4Q7c1PNQDl6YnJXhALVga8EMN3bDmFgnLQI9pC-qVaEbyhTTeUbjODRHnx9g6pJOJIIaGAqsfELTL5lnIyIM8fJDUzFO8sFD2FW06QdaM8NjKHmFabvdAfugvo8S4PDIMjDMKm5b73EKt0Pk1mfsH1Uz-EgIHc7AtuH0SGOZ5XO1A_NTbTtZc1N5kEQOnVOPGQiY3Ed7gTdyHGv-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119770" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119769">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5dae8e894.mp4?token=Uqob9Cmieqas9FMCB1nDbPNH0JoUuD7_0NIGgIAdosjtcnp0AG4p4Nw-YO-4bcV9GtQ-GRe2ID0CQmpu-Lskw8ZoQmnfPl4Mo-E07v_74UMYaJtloJKQuIVw8jyj8BKdOm82UaBCxk0Joh50j64Bh6qeRasDx98O6ktwIvQ78BwLD_zqfbU1syFwgnSca_zMkOq8YFuzYAtBtoESGZMWVauvJjhRfpBD4H-d9niu6tgIO72q55dzy8KPPi1F7bz8RJ3nm0djVhOme1v9IYVwqRK1njZjHmOq-2kmBFH8i-J2fImodQQLogRO9uXkh05YQqcN_k_Ya2oW88YDew1lqQVv8FocQPp0etwxg6NoBcWfIm97L-oKCJg_eaaSEmzaKfUfwKRP59uAn6VMftkUtuXBSoP054VQRrFtm1xwxiYstHmbz8e2_MwMI2csT3uD4IGd6hMw295f1X60w4PwkL5QttecSux7YKyvby7C2291DplMOK4iBU2nhzZEkUNlgkMOEFNrzF1tYYIQwCQy4O0iwqRy9jn59pE-tIFMvVwHuK5lJqJQAvOml_9vUdh4vTHbXy7tLAK0ZKx_5cR48YfH47lxF8L1OeFYIwK9z6vlV15HYhkymOaNnfwcM3SnVY2yPTnGT58lPr_to3ywl8rry_QpTe_dLhTR5oJ7Hf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5dae8e894.mp4?token=Uqob9Cmieqas9FMCB1nDbPNH0JoUuD7_0NIGgIAdosjtcnp0AG4p4Nw-YO-4bcV9GtQ-GRe2ID0CQmpu-Lskw8ZoQmnfPl4Mo-E07v_74UMYaJtloJKQuIVw8jyj8BKdOm82UaBCxk0Joh50j64Bh6qeRasDx98O6ktwIvQ78BwLD_zqfbU1syFwgnSca_zMkOq8YFuzYAtBtoESGZMWVauvJjhRfpBD4H-d9niu6tgIO72q55dzy8KPPi1F7bz8RJ3nm0djVhOme1v9IYVwqRK1njZjHmOq-2kmBFH8i-J2fImodQQLogRO9uXkh05YQqcN_k_Ya2oW88YDew1lqQVv8FocQPp0etwxg6NoBcWfIm97L-oKCJg_eaaSEmzaKfUfwKRP59uAn6VMftkUtuXBSoP054VQRrFtm1xwxiYstHmbz8e2_MwMI2csT3uD4IGd6hMw295f1X60w4PwkL5QttecSux7YKyvby7C2291DplMOK4iBU2nhzZEkUNlgkMOEFNrzF1tYYIQwCQy4O0iwqRy9jn59pE-tIFMvVwHuK5lJqJQAvOml_9vUdh4vTHbXy7tLAK0ZKx_5cR48YfH47lxF8L1OeFYIwK9z6vlV15HYhkymOaNnfwcM3SnVY2yPTnGT58lPr_to3ywl8rry_QpTe_dLhTR5oJ7Hf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: چهار هفته پیش، فرماندهی مرکزی شروع به اجرای محاصره علیه کشتی‌هایی که وارد و خارج از بنادر ایران می‌شوند کرد.
🔴
تا امروز، نیروهای آمریکایی ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، اجازه عبور ۱۵ کشتی حامل کمک‌های بشردوستانه را داده‌اند و ۴ کشتی را برای اطمینان از رعایت قوانین غیرفعال کرده‌اند.
🔴
اوایل این هفته، نیروهای فرماندهی مرکزی اطمینان حاصل کردند که ۲ کشتی تجاری پس از ارتباط رادیویی و شلیک هشدار با سلاح‌های سبک، برای رعایت محاصره بازگشتند، که به وضوح نشان می‌دهد اجرای قوانین توسط ایالات متحده همچنان به طور کامل ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119769" target="_blank">📅 19:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رئیس ستاد کل نیروهای دفاعی اسرائیل، ایال زامیر: نیروهای دفاعی اسرائیل با عزم راسخ در همه جبهه‌ها فعالیت می‌کنند. عملیات هنوز به پایان نرسیده است.
🔴
نیروهای دفاعی اسرائیل آماده‌اند در صورت نیاز مبارزه را از سر بگیرند و در حالت آمادگی دائمی هم در دفاع و هم در حمله باقی می‌مانند — از یهودیه و سامره (کرانه باختری) تا تهران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/119768" target="_blank">📅 18:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119767">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رسانه ترکیه‌ای: حضور کشورهای خلیج‌فارس در نشست ناتو علیه ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119767" target="_blank">📅 18:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پاتریک وینتور دبیر دیپلماتیک گاردین:
معاون وزیر امور خارجه فعال و مبتکر نروژ به طرز غافلگیر کننده‌ای وارد تهران شده است. او اخیراً به عمان و پاکستان نیز سفر کرده، بنابراین به نظر می‌رسد نروژ در حال آزمودن نقش خود به عنوان یک میانجی اروپایی است.
🔴
همزمان، برخی جمهوری‌خواهان آمریکا نظر منفی نسبت به تلاش‌های میانجی‌گرانه پاکستان دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119766" target="_blank">📅 18:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نفت آمریکا به ۱۰۴ دلار افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119765" target="_blank">📅 18:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119763">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzliwLh79nRr6gsoH5_4SDkT1HYPVUK401OeE782rXJgnUsdBG2I_IkFrl_Kp-6EH4S11zTZQNUNp-cF7KmvNFFKnIiaoVwQKXiYpv_8ar3QLhqB6vuelWYtg2VInn5QNrzB73_4_jFeTDLYgL7NiCNCy4UFmogT4lJishIJ1JX1mfE-PJBoCKLLJSTDdQKlwGDvVs5iPMApv459fjjpt3p9KljGhccbsbffku7GuoL4QGkWfsMKeu1fuxqBJbRwtWvnbcj2tcc_NJ54US8-VU4PDmsZftdIar5oJseeNEYIoM4YtJYvy2KBRfy7tDxdAiMUt5bKnWVGowhyxDEgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d2cac2d.mp4?token=iWe37kQvV5_VBaeJsLmaUbbGK0_4TrDE-zYZfTAmZcsu4hCimtUel-39dojjNBF2e197U1bcVA-CavxgybwbNHTj-ZaVvnkwmb7YQZlMOGTZrpn4tvhkc77bRdWC5S-lHMEP_HaAjb9sBHPx8_0UWnpFJx8sXAeD2thNRUqkE4eQA6ZV09GuwSkkB7iA21TpvnlT9hNhv1xnkvXx1abkh2rj6LMIB1c6KJmb8pukP7SoXk7EdJZWTAQrvAmAZQm6OUSv0fKNRFuVeNG4I7DaqavJvvoNvDAp7_8y6v3UExjVbkyxVcQp53k8U3bgNEFZOHWzthcFHddafTHDAVbnOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d2cac2d.mp4?token=iWe37kQvV5_VBaeJsLmaUbbGK0_4TrDE-zYZfTAmZcsu4hCimtUel-39dojjNBF2e197U1bcVA-CavxgybwbNHTj-ZaVvnkwmb7YQZlMOGTZrpn4tvhkc77bRdWC5S-lHMEP_HaAjb9sBHPx8_0UWnpFJx8sXAeD2thNRUqkE4eQA6ZV09GuwSkkB7iA21TpvnlT9hNhv1xnkvXx1abkh2rj6LMIB1c6KJmb8pukP7SoXk7EdJZWTAQrvAmAZQm6OUSv0fKNRFuVeNG4I7DaqavJvvoNvDAp7_8y6v3UExjVbkyxVcQp53k8U3bgNEFZOHWzthcFHddafTHDAVbnOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل چند لحظه پیش منطقه نبطیه الفوقا در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119763" target="_blank">📅 18:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119762">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نیکلاس کریستوف، ستون‌نویس نیویورک‌تایمز: جنگ ایران یک شکست استراتژیک بوده است که از برخی جهات، ایران را تضعیف نکرده، بلکه آن را قدرتمندتر کرده است.
🔴
هنوز هیچ راه حل ساده‌ای برای از سرگیری جریان نفت، گاز و کود شیمیایی وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119762" target="_blank">📅 18:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119761">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ادعای پولیتیکو، به نقل از یک مقام ارشد دولت ترامپ: انتظار می رود ترامپ در جریان دیدار با همتای چینی خود، او را در مورد ایران تحت فشار قرار دهد
🔴
چین پیش از این ایران را برای رسیدن به توافق تحت فشار قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119761" target="_blank">📅 18:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119760">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq90i89QVxBL261NkHWriINe4uxSMKK4mmwVtB6b8J1LqjTmh-gJNZidCEJ-Ast34WkifP4TcLwsnx-JnKIsyXrM7DgNo0SXD9dcXLmeRrPDv_6xCJwjbS36LkmtctZ0anIafYYlOQrXdoqcZ7xQDAz-6ig44QnobMdcv8svZoqFeNKFiFKmySFnYlvWlGbrxPf_u6yY5DbehhDZ-B3eLg-rFEGT8Z_1zIpC6xR3yLZY87nt5xrINPjZwsPb5OtIrRoPrQcJ_2qVqaVv7tyIuONsOfuBzPa5yJCBqfDiiQ_bg9kphxWbROEPG1Mc_5TsGlFvDXJNgodaHVbeZhFHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا اینترنت پرو محدودیت حجم روزانه برای استفاده در سایتهای خارجی هم داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/119760" target="_blank">📅 18:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119759">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
اطرافیان همسر مکرون با تکذیب ارتباط گلشیفته فراهانی و رئیس جمهور فرانسه گفتند: بانوی اول، هرگز در تلفن همسرش تجسس نمی‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119759" target="_blank">📅 18:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119758">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696b22878e.mp4?token=InNs-gi-aMhynDl8CIeP2wbihrt5IQdamqZs8Q_xUASNS0o501mn90-E6cdjypD-MYHyKKHP1ntfGPu3Ysgq23zVyYWdARNlCqSo6bJlkS6RCIefjAgMlMYeb1SgFK2k7CAuRr3-gCE4VE4d5XZ5WiECB_xC7Gyb7GMbxL3o0TK9I2kZyM9GrKO79_utfp-S1O7XJptEh31lNmn7nFX_pCKpH18AmbQc5I7paN41zae0SjkNGnJYjzo4y1gNlgekCZ7aqNKu2-EoJ77B7wdBK-eKoU2_RmS5OxhVfUnz_57liNL7DGCYdNYicWASixfZvWZMnJ29BQ17lBuvxie_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696b22878e.mp4?token=InNs-gi-aMhynDl8CIeP2wbihrt5IQdamqZs8Q_xUASNS0o501mn90-E6cdjypD-MYHyKKHP1ntfGPu3Ysgq23zVyYWdARNlCqSo6bJlkS6RCIefjAgMlMYeb1SgFK2k7CAuRr3-gCE4VE4d5XZ5WiECB_xC7Gyb7GMbxL3o0TK9I2kZyM9GrKO79_utfp-S1O7XJptEh31lNmn7nFX_pCKpH18AmbQc5I7paN41zae0SjkNGnJYjzo4y1gNlgekCZ7aqNKu2-EoJ77B7wdBK-eKoU2_RmS5OxhVfUnz_57liNL7DGCYdNYicWASixfZvWZMnJ29BQ17lBuvxie_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور روسیه، پوتین :
🔴
سیستم‌های متحرک نظامی که موشک‌های بالستیک غیرهسته‌ای دارن...
🔴
توی جریان یه عملیات ویژه نظامی به شکل مؤثری استفاده شدن و موفق بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119758" target="_blank">📅 18:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119757">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5371c1430.mp4?token=Bt2JnrQgKf6EndsueXndHJE1iueNQG03XysConIJNKPg3ge4clQ0e5tUHfhJxBPLrj5XG9RPvyY9Jbd1c4ku_dQjbcUmmm_lCv98qUwZuX-vJMukaPSnl7TBcRkadQAJP2v2adiE_1QFT1R10brW0ATfH0EJQAo0hv0QfeeYF268x1Xk6gJ6FOdXOHcj5JCSbbi0dOPWG7KHPbrD9aeRd5nXosU0u8v_xKmM5JagTo7M6bm2NXNrEIYtcEMx0Vd_QssNLu7bGShYq4yvnNimkqYcy5ID2-iOPLtwLOq9fEvlm1oQhzMz7sOLLq2UCd7JdgKWd0_jD69CIn_8LSWnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5371c1430.mp4?token=Bt2JnrQgKf6EndsueXndHJE1iueNQG03XysConIJNKPg3ge4clQ0e5tUHfhJxBPLrj5XG9RPvyY9Jbd1c4ku_dQjbcUmmm_lCv98qUwZuX-vJMukaPSnl7TBcRkadQAJP2v2adiE_1QFT1R10brW0ATfH0EJQAo0hv0QfeeYF268x1Xk6gJ6FOdXOHcj5JCSbbi0dOPWG7KHPbrD9aeRd5nXosU0u8v_xKmM5JagTo7M6bm2NXNrEIYtcEMx0Vd_QssNLu7bGShYq4yvnNimkqYcy5ID2-iOPLtwLOq9fEvlm1oQhzMz7sOLLq2UCd7JdgKWd0_jD69CIn_8LSWnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله ویدیویی منتشر کرده که یه پهپاد FPV تو نزدیکی خربت‌المناره، سربازِ اسرائیلی رو هدف قرار داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119757" target="_blank">📅 18:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119756">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آمریکا خواستار پایان برنامه هسته‌ای ایران
🔴
وزیر انرژی آمریکا مدعی شد: پایان دادن به برنامه هسته‌ای ایران که دهه‌ها ادامه داشته، تلاشی پیچیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119756" target="_blank">📅 18:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119755">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f911d75b16.mp4?token=WlRJnCwSzHPWc8NqF2YKv5laZvvq5BXYRJNSHaYgNY7R7-RJMw1Ekq7xEAOnh-WJ-K94b6u3VNCDdhL-kVniEoQ6utb_vXddyonPzumxIDyXEDhFQWmFlPgnrTWtRuJSRUGJhdhPmNY45B_QebNxMbHj5BKkBEhAodYW2D1I06wfTfsPqQVsZMtLcUG93gJB1DftkfNqJDyKtv7-3QiAnCiEq-Oq6k4yEWTOft1Tsqd1wXJGdgF8tW9VwriBIknV9MjaTlxPy4sjuFSoA_QHzoH4iWmAkaS48p_Xc3h8CzERJgoKLkZgyuUN6kS-6vZlJ9yEb3LetzAOh0u6wOD5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f911d75b16.mp4?token=WlRJnCwSzHPWc8NqF2YKv5laZvvq5BXYRJNSHaYgNY7R7-RJMw1Ekq7xEAOnh-WJ-K94b6u3VNCDdhL-kVniEoQ6utb_vXddyonPzumxIDyXEDhFQWmFlPgnrTWtRuJSRUGJhdhPmNY45B_QebNxMbHj5BKkBEhAodYW2D1I06wfTfsPqQVsZMtLcUG93gJB1DftkfNqJDyKtv7-3QiAnCiEq-Oq6k4yEWTOft1Tsqd1wXJGdgF8tW9VwriBIknV9MjaTlxPy4sjuFSoA_QHzoH4iWmAkaS48p_Xc3h8CzERJgoKLkZgyuUN6kS-6vZlJ9yEb3LetzAOh0u6wOD5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز چینی محکم سر جاش وایساده، همزمان هواپیمای ریاست‌جمهوری، ترامپ Air Force One از چند قدمیش رد میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119755" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119754">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09bfe31db3.mp4?token=cffWY32kORs3ycZezvTzSD2T2tQ2SWbe4jPObMPae1okCKx0S0HeYvHLKZ7HznF3cIeP3KGKK6uC_nl34WxVGvtolJzqI3ud1Ognpaew3ZAENyVGWYJHDXkNN1h-76mGz4H7-7d91i4ODBstC-ZPGeCCjWEOcvHhKu7xf6QgV4C1vj9nItNqU5G9H7eW6wV7T5pnaZ2r2KsAKcSFm4NmkBy-wTPMTuCgStLk_en02nAhGbvSYEpE7klNXkulYjDxHrbIHNaWjvYne5hOOmd-gmLYl02_2TrN0WBvGAGjBAWjSN9u-hgMRDnshHXYKcMkGDAoT8ntwoxqCD9d4AVNvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09bfe31db3.mp4?token=cffWY32kORs3ycZezvTzSD2T2tQ2SWbe4jPObMPae1okCKx0S0HeYvHLKZ7HznF3cIeP3KGKK6uC_nl34WxVGvtolJzqI3ud1Ognpaew3ZAENyVGWYJHDXkNN1h-76mGz4H7-7d91i4ODBstC-ZPGeCCjWEOcvHhKu7xf6QgV4C1vj9nItNqU5G9H7eW6wV7T5pnaZ2r2KsAKcSFm4NmkBy-wTPMTuCgStLk_en02nAhGbvSYEpE7klNXkulYjDxHrbIHNaWjvYne5hOOmd-gmLYl02_2TrN0WBvGAGjBAWjSN9u-hgMRDnshHXYKcMkGDAoT8ntwoxqCD9d4AVNvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: امیدواریم ترامپ در چین موضوع پایان‌دادن به جنگ اوکراین را مطرح کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119754" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjfCZd2yjQ71uLQkd8KYK-Y6FCdU_L7FenqE1Y0GS-MJbfVYEdZhUyzUhfANWlExb7dgCNXwssVVslki-djjCl3vRW55hgTinDOQrPt94CjoihHCQCfCINJy2Q7cZ8WE-7WkIwScrYM0AdBYpg2p8rJjpjaxuBZkvTeHzOzEeSOphh3E39HrqJAtIFyY1had0xGa1N5Vo-1mTFk_utJGn4h8AYSSgJhlNuGVrfZjGL-XTni0o9wA95kmSGQPqI8vau3c8JLBewBJqzU8VY-FymvY675J7VxlUddWUG6Wg4JQF0KSgiJuel-HpAzKdLU6LjWZBtsXjP-Q8rX3mKw8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استارت‌آپ چینی تصویربرداری ماهواره‌ای، میزارویژن، به دلیل ردیابی و انتشار تصاویر متن‌باز بمب‌افکن‌های آمریکایی در جریان حملات آمریکا و اسرائیل به ایران، توسط وزارت خزانه‌داری ایالات متحده تحریم شد.
🔴
میزارویژن سپس اطلاعیه تحریم‌های وزارت خزانه‌داری را به عنوان یک آگهی استخدام منتشر کرد و اساساً از آن به عنوان یک امتیاز شغلی استفاده کرد.
🔴
در آن آگهی نوشته شده بود: «به ما خوش آمدید.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/119753" target="_blank">📅 17:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119750">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDPVuDsPqbdcbIGD0KG-TfEA20zemN_CFJdLccfGnTDuM1wq1VAjZwssvJsYhx2C5izZBcYe4NMTWnZF8gcCKXB-0bXoyGUiES3Un8BwFVrOqhc0a1fpwife7DaGbDnPc_hIH2oKN4HozR3POzvY8QfUhgk-KpYDOJlhVWHJIFR4irkXPIejXQ4d_8fqnOc0nosLEYGnjfyx6ziJCbwdMsgo13do7EiU8JjBF9aZR8axOwJRfYNwFDw7K-FpkwWtqpVgUQ3ZuSXKYd59A5aB7fgfbMMYf9-fXbCQ3LAy-e4hB9C4Q-6cQ-BYOjAo6L6Gq0Vfzdtnf5P0C92P3EJHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZqT7VyBhwTjbmbb9nKTONuw1QjLE3L-K7uiAmjZQ2MDtzbN-aawqYY2f21OCs3jxbQOEKOzSToT9CbPyIP6-vfvzCIsoAIAGCMOC0_VzJyiTLTh6HfWpaaPlvRwFe1BELFlyPUgfbloBMm2ivyftqIpqxwn2ech2ObDrpnsKRWXEbiJupBV_xrcigmp5V-CWkToMqGErKTkEVbQHCpdSjEHtlMe7_n3q4Z011WnvR7_wg6rZK50oQ6krT70DHqsx3I_92AchMNEPpmV7IU9euJOz0d5f1BX33MpVAcrRyqk6B9zm1HeX9ghwOj8pv0PAc9GYp5S59WOOad8SMNOMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af69a990d.mp4?token=gjvHi3j9JR6WkWjYUi118utodwCRQnf_5gGYxED-lVh_lvM06MSOFTPy4xZVZSKfp2NI0bSVEiQKTiUT1CGWrkwtVwA88QU52MnhwpeLJvvd9Vv3ukY9y1HcEe3HpjigzBbzynC_qBUEgFSsS_F6OcwoG9hYZrC7HpiOR6FwvCZv2wqJYbTE-KYfI5F9OM2dkOvSAwTgnyOo3uml_rN0xBZsmXS0eI9b57kSxc4Ic0Lmd0XzqhjSyMgqIXlulJBGMxvQyUtKet5BJajyUrhLURMttL8U8C1qcWruv6b_ua833F7fWaFsjVXukHC2iT0iDSynYvHLI-MzPxzcbbWwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af69a990d.mp4?token=gjvHi3j9JR6WkWjYUi118utodwCRQnf_5gGYxED-lVh_lvM06MSOFTPy4xZVZSKfp2NI0bSVEiQKTiUT1CGWrkwtVwA88QU52MnhwpeLJvvd9Vv3ukY9y1HcEe3HpjigzBbzynC_qBUEgFSsS_F6OcwoG9hYZrC7HpiOR6FwvCZv2wqJYbTE-KYfI5F9OM2dkOvSAwTgnyOo3uml_rN0xBZsmXS0eI9b57kSxc4Ic0Lmd0XzqhjSyMgqIXlulJBGMxvQyUtKet5BJajyUrhLURMttL8U8C1qcWruv6b_ua833F7fWaFsjVXukHC2iT0iDSynYvHLI-MzPxzcbbWwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کتاب جدید یک خبرنگار مجله پاریس مچ ادعا می‌کند که رئیس‌جمهور فرانسه، مکرون، یک رابطه «عشق افلاطونی» چند ماهه با بازیگر فرانسوی-ایرانی گلشیفته فراهانی داشته است که در آن پیام‌هایی از جمله «از نظر من تو خیلی زیبا هستی» رد و بدل شده است.
🔴
حادثه باند فرودگاه ویتنام در مه ۲۰۲۵ که در آن به نظر می‌رسید بریژیت همسر مکرون به او سیلی زده است، در واقع یک دعوای زوجین بود پس از اینکه او پیام‌ مکرون به گلشیفته را وسط پرواز در تلفن او دید.
🔴
کمپ بریژیت این موضوع را رد می‌کند.
🔴
فراهانی در مورد این ادعای خاص اظهار نظری نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/119750" target="_blank">📅 17:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119749">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suHyejSsrESdRrzv0T7ljBph1sU1BI6BQKk-lLD_TL_jrIIUapIYRpza7-luKelZkscvc0leqI_cNFE4_DjnmCrwjcr61Flo6ud4VAwZKHIQxG33Sd56b7UgInfUU0sUIgfKy5qZxo0cfvvWX2hgO38J_8XlT1wdfEHLPrE1XLDKIeoLlDjJ0CwuIYx_xLagLw60aqzAJslyvBxiT3FaDneg1XpTKWqhHKpK9dZqtcx6G-q-cFufGxKLmAR8oizHrwiv1n4xgOAD7PonzicdlGJTYDCj7YytAzPX8Ei64c_-6YqLXm2DGqBpVStjYSyMJTbo8MLcz8c1o2JEcefTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بروجردی،عضو کمیسیون امنیت ملی:
دستاورد تنگه هرمز را از دست نمی‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/119749" target="_blank">📅 17:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119748">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3813de281a.mp4?token=RpXUKh-f2BLeMW_dzy5Ik0W_Z5MencDNU2YEMTlvt-QfoARXBS2IbvieujRGOSRHGLga3T25c7wvfTNl5RJNfC56XmkkaxaMdC8Pygn67e-qLdURwXSW0Sr7tWM0t3X3AvPaxoxTxkZIBERt1gUwZc82ZmgRXn8QEZHTBTorgNv-OQCYQRzFnFqSw-w3eiKePtXFVChYmtc4HbadYR9rUnhLR4MxWRi6hNXT6-J9rsPBfX5LiuIInP4FIKFjcYsMqUgpcbdWX0t5onGRcAMBsL3ICTQd9RT6OzTlM9Re0sr0DfRu6kxNiaiyGstKDCT0zMuaHjGXK9_LmSoEl9rxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3813de281a.mp4?token=RpXUKh-f2BLeMW_dzy5Ik0W_Z5MencDNU2YEMTlvt-QfoARXBS2IbvieujRGOSRHGLga3T25c7wvfTNl5RJNfC56XmkkaxaMdC8Pygn67e-qLdURwXSW0Sr7tWM0t3X3AvPaxoxTxkZIBERt1gUwZc82ZmgRXn8QEZHTBTorgNv-OQCYQRzFnFqSw-w3eiKePtXFVChYmtc4HbadYR9rUnhLR4MxWRi6hNXT6-J9rsPBfX5LiuIInP4FIKFjcYsMqUgpcbdWX0t5onGRcAMBsL3ICTQd9RT6OzTlM9Re0sr0DfRu6kxNiaiyGstKDCT0zMuaHjGXK9_LmSoEl9rxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من خطاب به بابام که میگه ۱۰شب خونه باش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119748" target="_blank">📅 17:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119747">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل:
جنگ با ایران پایان نیافته است،برای از سرگیری جنگ در هوشیاری کامل قرار داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119747" target="_blank">📅 17:12 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
