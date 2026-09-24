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
<img src="https://cdn4.telesco.pe/file/Q5yFJA0fRnTH-Y54-P2Dc00ivjnLrv7qktmKOANYfMwVCFpu5VkoiaHO7eDt6BXTWB6xOaFoV4A-veg0J3sU3yP0PlGB4PaKVayawmCxalVPGvNTJisykb6oBrWaag1bvWZHBIJpEPkvmOQH8wf8vqewcowDZIc6VqcgjSwINa_QutZgtTSA3nk4p9G30QY5w4k1O-8FLUpD1IpGFdD4bk77DY8P7q-rpH_xjfVaVLHIfL2YTX2d3bUuSaqPcsfzIbyjAEVZWV5t4Z_NvI7gIPJ9WEmjQ0CA1UKR6vBZXMUQUBAHyqWLNzHO3Nb4eiCVqHXby2P1fPLHTj6B6pGXCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 23:07:58</div>
<hr>

<div class="tg-post" id="msg-149243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c752dcf0.mp4?token=YfgK9ZP7w0jJLAz_05y9bXxBzfR-e5F7MEpVKZ1g1bH1y5C5RHFSKkOurXsqn4mGQGT1-gEl4t6XioIx9HlNkD_Zz9Mg9dwBNQDraYI9OiR9fpT-priY_-eQlGNm_FEBXThQPIftBkEjUR0ecquFiwr9F191gpwYmLu2LKwwRbCFW-L_ASNSSW-8M7stj8bWrGn8ITN23MYWwYDLmKDwNJq0Asp6N48vh-pyO-aYjqz2YPPZA4OXHgwGKuy0o-htSgOTdRbytr2XZaMHPjw7VddMi2hDwMLKtlhMEWQKcZsLQ7CrQS3NQU7h47IdMwbsOmu-P6ARHDLYOAWpgtXLWKjYeh4FG9q6YBbmPqMb1R0QxEaPoNZDBzNZH4fbJJKNrOfq8xy88AyIsajgZcajPUl6tMtFW6prr9HHv1yQ8pT6e0EnrDRy5E4zzkswCi6yj-4HIHyZnW5Fe6aiJWYgWSq8_cEriZoH03ItTut1mh7PCM3dnj6r9TG5tIl_nZwXgvNR-DJt6NfuASSeLTYAIidZEnNIzDQIkwyWm8nL2gnIXV3-inzXy4cIi34d4eUkbnuoCB41fjJA5BtZgabnWchb9OOrTq9NVc4CRz_n173r3FTLH8esakM9L-mmBo6EHBODaPsEwZfDGGkIHTnwde-367cMW0EM81K1f0uQSl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c752dcf0.mp4?token=YfgK9ZP7w0jJLAz_05y9bXxBzfR-e5F7MEpVKZ1g1bH1y5C5RHFSKkOurXsqn4mGQGT1-gEl4t6XioIx9HlNkD_Zz9Mg9dwBNQDraYI9OiR9fpT-priY_-eQlGNm_FEBXThQPIftBkEjUR0ecquFiwr9F191gpwYmLu2LKwwRbCFW-L_ASNSSW-8M7stj8bWrGn8ITN23MYWwYDLmKDwNJq0Asp6N48vh-pyO-aYjqz2YPPZA4OXHgwGKuy0o-htSgOTdRbytr2XZaMHPjw7VddMi2hDwMLKtlhMEWQKcZsLQ7CrQS3NQU7h47IdMwbsOmu-P6ARHDLYOAWpgtXLWKjYeh4FG9q6YBbmPqMb1R0QxEaPoNZDBzNZH4fbJJKNrOfq8xy88AyIsajgZcajPUl6tMtFW6prr9HHv1yQ8pT6e0EnrDRy5E4zzkswCi6yj-4HIHyZnW5Fe6aiJWYgWSq8_cEriZoH03ItTut1mh7PCM3dnj6r9TG5tIl_nZwXgvNR-DJt6NfuASSeLTYAIidZEnNIzDQIkwyWm8nL2gnIXV3-inzXy4cIi34d4eUkbnuoCB41fjJA5BtZgabnWchb9OOrTq9NVc4CRz_n173r3FTLH8esakM9L-mmBo6EHBODaPsEwZfDGGkIHTnwde-367cMW0EM81K1f0uQSl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فون در لاین از اتحادیه اروپا درباره کانادا: کانادا به دلیل جغرافیا نمی‌تواند عضو اتحادیه اروپا باشد. این تنها دلیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/alonews/149243" target="_blank">📅 23:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149242">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EXg6B6d43QPYjcvjMicqTZYHet36-wRmFj3xXknx2vgOQUEC490JnNh2uSHqpxoIVQOdLEgjcGG27wbyBz5NxlKYVP4RY78u0TnmH6mjhEem8Jb7y-nn07GzwfnqCwtKru-QEsRWOWDnir88Zx821pKHLFu-Z6_UmdzXRHJ1zlau5ozuDtLSZxy1gSGKUevp6IAed7hDUDIh6zm7ezaqLBiUihBBZSTZRxtmRT1qdrr8eFv0s8Mvo1jbLD28TFYFsRjXjL-TITJA7Zlvg7LBBYATcNVX5oYArDpCyyrifdIZgt8WpdfFkAfc_EsfMUyh4E0y9TwWWtjxuP5PZjySWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی عربستان ۵ حمله هوایی به
جزیره کمران
در استان الحدیده یمن انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/alonews/149242" target="_blank">📅 23:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قیمت واکسن آنفلوانزا اعلام شد
سخنگوی انجمن داروسازان ایران، قیمت واکسن آنفلوانزا برای مصرف کننده را دو میلیون و ۱۸۵ هزار تومان اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/149241" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8237eab5.mp4?token=MY-M3vDZrHfw1XY03jfWX-SLyQm4Z7hw6aH2pU8hbrBw4D5pGsnQU0kjgmOBOEk1QMqoKWF8z_Eg7v54xUQLKqiZQtom3fxGPK7XV54xfxXEEuSj_v-1LFEByVNcRtn38r33lDkRVEAOUQY_BO8p0E-Wvc1FL61S5E9GRMUi0Ar0y2z3jfeflW54LTlkgGP32vGG9hg4eVkOopTRnyDS6SJm7BotRRYg3VHeL9iqZIBA8OiIh8PFRRUTUD8ybkxbCOlSh8ZIe2iRcd2_QLLKma2pRrpe_bOrR4Che-IjwaPfu4jx35e3eIQrzZFeDjINu5lZq3cqtsYJJD2Tqd69Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8237eab5.mp4?token=MY-M3vDZrHfw1XY03jfWX-SLyQm4Z7hw6aH2pU8hbrBw4D5pGsnQU0kjgmOBOEk1QMqoKWF8z_Eg7v54xUQLKqiZQtom3fxGPK7XV54xfxXEEuSj_v-1LFEByVNcRtn38r33lDkRVEAOUQY_BO8p0E-Wvc1FL61S5E9GRMUi0Ar0y2z3jfeflW54LTlkgGP32vGG9hg4eVkOopTRnyDS6SJm7BotRRYg3VHeL9iqZIBA8OiIh8PFRRUTUD8ybkxbCOlSh8ZIe2iRcd2_QLLKma2pRrpe_bOrR4Che-IjwaPfu4jx35e3eIQrzZFeDjINu5lZq3cqtsYJJD2Tqd69Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه فاکس‌نیوز تیزر مصاحبه رئیس‌جمهور ایران را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/149240" target="_blank">📅 22:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149239">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1915ce4848.mp4?token=bA1yTjDhoRyvHJemILytLw9QbLilDo9PqJp2iBPDUnsGx74Y8iy7NvU1s-_tC8lmyEInUvsh-Ep5fap-Otjo6ujuYoVZ1lPlBkAejOyL6AKqiD42pgMCnaXMbgw7tuRdSnYL7aV7Ndayxuno8x946awHQb72dZeBlpFDPgjfvUWrf4iniXc_xAL-nar-K_bGOr7L0qYVTGSPhuXXiKse0Gsqk4jHUmYybXua2WbS_N1bmdjw9euRpN7goh5L2nrv4eqkrngTblnNX9vKjXnKFysvK-mjdpCXJhX4JP9JcwzUP-Il7q_Nhh4249RWwbOTpJFfQ2p-xK4AOYAyoe-goA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1915ce4848.mp4?token=bA1yTjDhoRyvHJemILytLw9QbLilDo9PqJp2iBPDUnsGx74Y8iy7NvU1s-_tC8lmyEInUvsh-Ep5fap-Otjo6ujuYoVZ1lPlBkAejOyL6AKqiD42pgMCnaXMbgw7tuRdSnYL7aV7Ndayxuno8x946awHQb72dZeBlpFDPgjfvUWrf4iniXc_xAL-nar-K_bGOr7L0qYVTGSPhuXXiKse0Gsqk4jHUmYybXua2WbS_N1bmdjw9euRpN7goh5L2nrv4eqkrngTblnNX9vKjXnKFysvK-mjdpCXJhX4JP9JcwzUP-Il7q_Nhh4249RWwbOTpJFfQ2p-xK4AOYAyoe-goA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کانال 15 عبری: احتمال دستیابی به توافقی بین ایالات متحده آمریکا و ایران "بسیار کم" است، اما غیرممکن نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/149239" target="_blank">📅 22:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149238">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
یک مقام دفاعی آمریکا : حدود ۶۰ کشتی تجاری روز چهارشنبه از تنگه هرمز عبور کردند؛ رقمی که به گفته او بالاترین حجم روزانه عبور نفت خام از اوایل ماه جولای بوده است.
🔴
به گفته این مقام، حدود ۴۰ کشتی از این ۶۰ کشتی برای دریافت حفاظت، عبور خود را با ارتش ایالات متحده هماهنگ کرده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/149238" target="_blank">📅 22:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مکرون خواهان برقرای آتش بس فوری در خاورمیانه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/149237" target="_blank">📅 22:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149236">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نتانیاهو: ارزش‌های ما، بشریت را برای هزاران سال الهام بخشیده‌اند... و تلاش ابدی ما برای صلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/149236" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149235">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مکرون: ما تجهیزات نظامی و سربازان را برای محافظت از کریدور دریایی در دریای سرخ اعزام خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/149235" target="_blank">📅 22:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149234">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنرانی نتانیاهو تموم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149234" target="_blank">📅 22:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149233">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa32aca47b.mp4?token=Rzfpbn-0ccG5GaLt9udOPSwcAfg1cj4MHr7QzgB9j-I-zh2jdGa00BCwqwM00fHOOjJQZiksYKaeDsK6drspxYmcWddyzTiIgQnMlg4_KXFo0609JYUO2ySMpm-Cua6sHpp90KFkancTnhPJGxgbO8Myo9qPVn43yC-Mqcmdb-7axuJNSiHlemxZrgc9A66Z1kMQPMNY97sRjDGTrrh5_cqI9FjHU464j2ElIRxH6CVHMYKuLcHzibOySt_q6dzlaUxsRtZ0VrA2bhS2BeH0mh-XRLInZ9hbQPq3UV_MrlFZsBrg805RtXWxdfMlotVxu8UuA5FF3oHdFY81iLi1JjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa32aca47b.mp4?token=Rzfpbn-0ccG5GaLt9udOPSwcAfg1cj4MHr7QzgB9j-I-zh2jdGa00BCwqwM00fHOOjJQZiksYKaeDsK6drspxYmcWddyzTiIgQnMlg4_KXFo0609JYUO2ySMpm-Cua6sHpp90KFkancTnhPJGxgbO8Myo9qPVn43yC-Mqcmdb-7axuJNSiHlemxZrgc9A66Z1kMQPMNY97sRjDGTrrh5_cqI9FjHU464j2ElIRxH6CVHMYKuLcHzibOySt_q6dzlaUxsRtZ0VrA2bhS2BeH0mh-XRLInZ9hbQPq3UV_MrlFZsBrg805RtXWxdfMlotVxu8UuA5FF3oHdFY81iLi1JjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره حملات ۷ اکتبر:
به‌طور نسبی، این معادل کشتار ۴۰,۰۰۰ آمریکایی بی‌گناه در کمتر از ۲۴ ساعت است.
🔴
این ۱۶ برابر ۱۱ سپتامبر است — ۱۶ تا ۱۱ سپتامبر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149233" target="_blank">📅 22:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149232">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aae11072a.mp4?token=m8R1YjO2qV5-5I5PnB0Rlgexu84dGllZ4ie_Y1iy5x8XSUO8-tN7kopR42QT-3S0eKlidxwp6K5Mmo_FdOI8E2i-GTJ5P6cHgiqPlfhnCEnvvXsNFllf1rviF2figEvne4CA8wKNPfOfkiL__k5ci8prwuIwTST-WmHH7p40nvzLqrorEgYeulrMsh92yLr6-8EYamHr_8XLQ4a3WO8xHEcc4VvK54odJsG_kdnQHXWq8z8ueuAvUOk5U1MtWBV0QgnH0tizH8TQ3JyZhjbrd2DM1o8HTPdSCggbDipwuZL4U3A0mK_V44DAO2VKIHQnAdC_cB9UvB2wrw9piAQ-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aae11072a.mp4?token=m8R1YjO2qV5-5I5PnB0Rlgexu84dGllZ4ie_Y1iy5x8XSUO8-tN7kopR42QT-3S0eKlidxwp6K5Mmo_FdOI8E2i-GTJ5P6cHgiqPlfhnCEnvvXsNFllf1rviF2figEvne4CA8wKNPfOfkiL__k5ci8prwuIwTST-WmHH7p40nvzLqrorEgYeulrMsh92yLr6-8EYamHr_8XLQ4a3WO8xHEcc4VvK54odJsG_kdnQHXWq8z8ueuAvUOk5U1MtWBV0QgnH0tizH8TQ3JyZhjbrd2DM1o8HTPdSCggbDipwuZL4U3A0mK_V44DAO2VKIHQnAdC_cB9UvB2wrw9piAQ-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو نخستین رهبر جهان است که از اصطلاح "هوش برتر/Superior intelligence" که پرزیدنت ترامپ ترجیح می‌دهد، برای اشاره به هوش مصنوعی استفاده کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/149232" target="_blank">📅 22:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149231">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نتانیاهو یک دستگاه آنتن استارلینک با خودش به سخنرانی آورد و به دبیر سالن داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149231" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149230">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نتانیاهو درباره جمهوری اسلامی: می خواهم خبر خوب را به شما بدهم. با وجود سکوت شما، با وجود ریاکاری شما، تنها مسئله زمان است که در ایران چیزی باورنکردنی رخ دهد.
🔴
قدرت مردم بر مردمی که در قدرت هستند غلبه خواهد کرد!
🔴
می‌خواهم کلمات مرا با دقت گوش دهید. یک روز، و شاید آن روز دور نباشد، مردم ایران آزاد خواهند شد.
🔴
حکومت قاتل آن‌ها با دروغ‌هایش، با فسادش، با بی‌رحمی‌اش سرنگون خواهد شد.
🔴
این حکومت شیطانی سقوط خواهد کرد و ما همه آن روز را جشن خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/149230" target="_blank">📅 22:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149229">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6iywtSSJxf2lVytfr-Vgcw2YS0ail_iYKPwF6gRFpu7PRN2tePqYJtsLfjTiawg1NSnoFHkSR2nIpjgj0QR6X-msE8DE62L2Dpg6t12u3FOogQ1dQ012BvImyyHNVDnqUpe1iMRBVm6ibQglaf6JMFfIknJDCs-HXVwexItZUJpnc5cK7PoH0F7jdDghahod_QAi1OH3cEfPB6WZFiyHGX2aMOZ9xW0nJw78BL4rJkgJ-HVobjd7noZ6rgvs2feWQWPaOaH74YnsV032VbTIqXDkfbKEjSWn9egL5HoCbv_mKbW_8NutnGoVBGw9tKXbaJcaKMb9rdz1IpuCmuZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده امارات پای سخنرانی نتانیاهو نشسته و سالن رو ترک نکرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149229" target="_blank">📅 22:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149228">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نتانیاهو: کتاب مقدسم میگه ما در نهایت پیروزیم؛ متشکرم از شما
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149228" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149227">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a98d071e9.mp4?token=MItf8umJp9_Jy3fDXV77k-QxS0FWEX80kgQK-W7SL71Eh6J1V0mbwmftrq4RvFYjqdSeHp3TVHAcnXqWskws5hTQCt2kD8pYY5b8FB2jFjaixVIHkK3ArusxA9ktiyKF3j4EBwz4Akq2e4wJb6iOKnaKgVLvknX8MHO4IAPwaQi1ZROV3F8t6a1SvY0S74yzPPDbpHpxBfWGLpO7M7Y11ME7nAx6husK-xDZxUUCHvhJFTFmc89mCIOjBiBRJsycJR-Hw4fDg7c5s9RwjB-dZf3P1yvRrmn9HOH--LbZZl2Ai7_ZCvg-lhCZhmuM7cpQsbXe1uC_JCJpJyC6otapLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a98d071e9.mp4?token=MItf8umJp9_Jy3fDXV77k-QxS0FWEX80kgQK-W7SL71Eh6J1V0mbwmftrq4RvFYjqdSeHp3TVHAcnXqWskws5hTQCt2kD8pYY5b8FB2jFjaixVIHkK3ArusxA9ktiyKF3j4EBwz4Akq2e4wJb6iOKnaKgVLvknX8MHO4IAPwaQi1ZROV3F8t6a1SvY0S74yzPPDbpHpxBfWGLpO7M7Y11ME7nAx6husK-xDZxUUCHvhJFTFmc89mCIOjBiBRJsycJR-Hw4fDg7c5s9RwjB-dZf3P1yvRrmn9HOH--LbZZl2Ai7_ZCvg-lhCZhmuM7cpQsbXe1uC_JCJpJyC6otapLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیئت ایرانی هنگام سخنرانی بنیامین نتانیاهو در مجمع عمومی سازمان ملل حضور ندارد.
🔴
در محل استقرار هیئت ایران، تصویری از قاسم سلیمانی همچنان قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/149227" target="_blank">📅 22:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149226">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aaac1b06f.mp4?token=SpJv8lDGH5-ACdUW7FScxuuONAbVw-B7KDutW1S6eTN1wdvziMtimsFjYB4Xncy7oB5UEavI4GvlN840OiMwLK3iIU55siK6r8IEJgbQbBbJZ2usPm16-gluG-KduN0mGQHybTRwAurn9uS88AIAcGYnU_H6e8nT2rCLRYfJfm6fn8M2cXyhhZ-ukmcQQmJElkqersknUtSnA5mKNsQapL_eb948gsqAy6kxe_IZTTXX-SK0SNu2eR6LZyah9c3dAtrCx_w3Ic6RKNvxln-uVw0Bdba0Va3LZzcTGflFbEXI8Qamcls2D5x1bwpXo_ullveLJZ2OdpSWRL3b4LngoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aaac1b06f.mp4?token=SpJv8lDGH5-ACdUW7FScxuuONAbVw-B7KDutW1S6eTN1wdvziMtimsFjYB4Xncy7oB5UEavI4GvlN840OiMwLK3iIU55siK6r8IEJgbQbBbJZ2usPm16-gluG-KduN0mGQHybTRwAurn9uS88AIAcGYnU_H6e8nT2rCLRYfJfm6fn8M2cXyhhZ-ukmcQQmJElkqersknUtSnA5mKNsQapL_eb948gsqAy6kxe_IZTTXX-SK0SNu2eR6LZyah9c3dAtrCx_w3Ic6RKNvxln-uVw0Bdba0Va3LZzcTGflFbEXI8Qamcls2D5x1bwpXo_ullveLJZ2OdpSWRL3b4LngoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«اسرائیل مرتکب نسل‌کشی نشده است.
🔴
اسرائیل از وقوع نسل‌کشی جلوگیری کرده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/149226" target="_blank">📅 22:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149225">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / سنای آمریکا با طرح قانونی محدود کردن اختیارات ترامپ در جنگ با ایران مخالفت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/149225" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149224">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
«باید صادقانه با شما صحبت کنم. همه ایستادگی نمی‌کنند.
🔴
ما این موضوع را دیدیم؛ زیرا برخلاف اسرائیل، برخی کشورها، و به‌ویژه در اروپای غربی، در موارد اخیر تصمیم گرفته‌اند ایستادگی نکنند.
🔴
رهبران این کشورها تصمیم گرفته‌اند در برابر گروه‌های یهودستیز تسلیم شوند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/149224" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149223">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=QvXQHBmJZo1bATUJaqy8Ua67szgwdlk2FEe51o5ofigHxvDGlfWNQyf8oIRtLj75cXA8JzcCpr_2EEnronki3VjI_6J7V9ljOsLJhSO1ZlrOE0WbEioOAAcaSEaFk6gib1O-0Ak1VxX314h76bvExGvAyfwzlPGrzxzK06x0GsZLfxyUghWkAl-LYevMkiqATXmIqarxqWC_kErg1w89BQcAfxiU5VYcqhIKGz_gffoaIFqadsKH5RINmcPWeFJzFqvqYWwjHPYn_2D7rIzxH8CcOMJ6DpLrmZwFhOspMsuBPAQaFTotORAKuWR0ARWNUnOqM53U4a17yNHyKeQLIi6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=QvXQHBmJZo1bATUJaqy8Ua67szgwdlk2FEe51o5ofigHxvDGlfWNQyf8oIRtLj75cXA8JzcCpr_2EEnronki3VjI_6J7V9ljOsLJhSO1ZlrOE0WbEioOAAcaSEaFk6gib1O-0Ak1VxX314h76bvExGvAyfwzlPGrzxzK06x0GsZLfxyUghWkAl-LYevMkiqATXmIqarxqWC_kErg1w89BQcAfxiU5VYcqhIKGz_gffoaIFqadsKH5RINmcPWeFJzFqvqYWwjHPYn_2D7rIzxH8CcOMJ6DpLrmZwFhOspMsuBPAQaFTotORAKuWR0ARWNUnOqM53U4a17yNHyKeQLIi6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«می‌خواهم چند سؤال از شما بپرسم:
🔴
کدام حکومتی که مرتکب نسل‌کشی می‌شود، برای جمعیت طرف مقابل یک میلیون واکسن فلج اطفال تأمین می‌کند؟
🔴
کدام حکومتی که مرتکب نسل‌کشی می‌شود، امکان ورود و توزیع ۲ میلیون تُن مواد غذایی در غزه را فراهم می‌کند؟ یعنی به ازای هر نفر، یک تُن غذا.
🔴
متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/149223" target="_blank">📅 22:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149222">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdac61ee8.mp4?token=Ano-WDIVWQKkwarVAW7z891xG2AOg0ZmxPELlzZUk0dXfUFbg7UDAAMymmYlVp5lLkSVaeqvQq_QMrUPBqOXlWu1rWTYs3oVnoAGgHMhFlwO3-_Gkwu5eH7Qx6TTpqHNx61iRKTJLSlqidqqUn7oiNo33ictS6si_3VnQOvbsvN2RgZ3RPF0Uux4jvVBRgqm4J5yCKC0o9kae4FPVkqjcKy_v-YB-WxlY6JUmh66qSPMZuHTlLMsJL-FadaAaJHnFFWiY4y_E7helfhQ9UR5A6Ol0a99JErCJMqQwylEtLf5g81Q9TU6SVAeP70cxw7Nj2w90VFB2IXFXS1rnbo4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdac61ee8.mp4?token=Ano-WDIVWQKkwarVAW7z891xG2AOg0ZmxPELlzZUk0dXfUFbg7UDAAMymmYlVp5lLkSVaeqvQq_QMrUPBqOXlWu1rWTYs3oVnoAGgHMhFlwO3-_Gkwu5eH7Qx6TTpqHNx61iRKTJLSlqidqqUn7oiNo33ictS6si_3VnQOvbsvN2RgZ3RPF0Uux4jvVBRgqm4J5yCKC0o9kae4FPVkqjcKy_v-YB-WxlY6JUmh66qSPMZuHTlLMsJL-FadaAaJHnFFWiY4y_E7helfhQ9UR5A6Ol0a99JErCJMqQwylEtLf5g81Q9TU6SVAeP70cxw7Nj2w90VFB2IXFXS1rnbo4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:
از معترض‌هایی که بیرون هستن و از اون نماینده‌های ریاکاری که همگی جلسه رو ترک کردن، یه سؤال دارم:
🔴
وقتی حاکمان مستبد ایران ده‌ها هزار غیرنظامیِ بی‌سلاح ایرانی رو کشتن و زخمی و ناقص کردن، شما کجا بودین؟
🔴
وقتی هزاران نفر از مردم خودشون رو کشتن و زخمی کردن، شما کجا بودین؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/149222" target="_blank">📅 22:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149221">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل
:
«رژیم ایران به‌ویژه زمانی نگران می‌شود که مردمش به چنین چیزی دسترسی داشته باشند.
🔴
این یک
دستگاه ارتباطی — استارلینک (Starlink)
— است که به مردم امکان می‌دهد به
حقیقت دسترسی پیدا کنند
و از
آزادی اندیشه و آزادی بیان
برخوردار باشند.
🔴
به همین دلیل، رژیم ایران
میلیاردها دلار برای سانسور اینترنت
هزینه می‌کند.
🔴
آقای رئیس‌جمهور، من این دستگاه را به شما می‌سپارم تا آن را به
هیئت ایرانی
بدهید.
🔴
تا اگر آنها روزی
به‌ناچار از حکومت جدا شدند
، بتوانند آزادانه
داستان خود را در شبکه‌های اجتماعی بیان کنند
.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/149221" target="_blank">📅 22:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149219">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«اسرائیل مرتکب نسل‌کشی نشده است.
🔴
اسرائیل از وقوع نسل‌کشی جلوگیری کرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/149219" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149218">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نتانیاهو : اکنون، جدیدترین کشوری که به یک ابرپخش‌کننده دروغ‌های یهودستیزانه تبدیل شده، ترکیه است: اردوغان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/149218" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149217">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«اسرائیل و آمریکا در کنار یکدیگر برای نجات تمدن اقدام کردند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/149217" target="_blank">📅 22:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149216">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43314fb77.mp4?token=nRYuG2xD3Z8BsXfu9pdfzcDtFqFCUX7aEFQyWVNOGSi6wQk9j-ks4AGSx97X7WfKtB8Se1HeWj3_Lfj7YWjP1Nxd9Z6wbmzWjIk25YK_jW91MT_J8o4kIVsdSGNfoAWhyEE7N97ylLzGuweuSobMkHPa36fOkRIMrd7ncFKE5d5W8JK5VVeipowEELRFYr6VWydtQggitt5A0vuBsTdQyg7jh-RAgoOcbh7wuDe5RVOUFXk2HW8KJ23FVLT5zTLHfZUIDaoYG5Tjo2yrZgKLymZDbz1MBL_4QqzMc3qaLF2q2YvuxU-Fk0MFJIHYEjORrwUnURP7AQeaTgYKDgWtsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43314fb77.mp4?token=nRYuG2xD3Z8BsXfu9pdfzcDtFqFCUX7aEFQyWVNOGSi6wQk9j-ks4AGSx97X7WfKtB8Se1HeWj3_Lfj7YWjP1Nxd9Z6wbmzWjIk25YK_jW91MT_J8o4kIVsdSGNfoAWhyEE7N97ylLzGuweuSobMkHPa36fOkRIMrd7ncFKE5d5W8JK5VVeipowEELRFYr6VWydtQggitt5A0vuBsTdQyg7jh-RAgoOcbh7wuDe5RVOUFXk2HW8KJ23FVLT5zTLHfZUIDaoYG5Tjo2yrZgKLymZDbz1MBL_4QqzMc3qaLF2q2YvuxU-Fk0MFJIHYEjORrwUnURP7AQeaTgYKDgWtsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«در این نبرد علیه
بربرها (اشاره به دشمنان اسرائیل)
، هیچ شریکی بزرگ‌تر از
رئیس‌جمهور ترامپ
نداشته‌ایم.
🔴
از او
تشکر می‌کنم
.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/149216" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149215">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE_QvffSamp131u4oX6lOjyhcMbr3X2zbZh3UMkMG9KiJmwkqroK5kWEOfEyTXAU-xejb9SmBFVVxJrTYkRmGzfOSlK2LUbzhZRMyG41AoSodfhOo6ui6m_DHgYxSMR2nQDP4PNVBZrvOChSEYsJTdCOusR4I4fc8PSup8F4WEMO2zLFuBbgqzd6UzLGpe34OtXO_E0epuks1tHRCVR1F85UckDGScPiJZSiqb0ExWrpExbkLqvwrJJj3TnfLWbOh6iLLLHItx8N18a22CCZM6YBCRetqdoRXg4F4pw-4i5Ty3p6lwxrlyfpb9B_qK4DriTvXkFav0hZ3bGMQdDI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: آیا این پیجرها را به خاطر دارید؟ حزب‌الله قطعاً آن‌ها را به یاد دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/149215" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149214">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«می‌خواهم از اوگاندا تشکر کنم که اخیراً تندیسی از برادرم، یوناتان نتانیاهو، در محلی که او جان باخت، برپا کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/149214" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آنها اسرائیلِ کوچک را به استعمارگری متهم می‌کنند. چه کسانی ما را متهم می‌کنند؟
🔴
در میان آنها، افرادی در بریتانیا و فرانسه هستند.
🔴
آخر برای خدا، خود آنها این اصطلاح را ابداع کردند؛ مستعمراتشان سراسر جهان را دربر گرفته بود.
🔴
استعمارگری؟ بس کنید دیگر!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/149213" target="_blank">📅 21:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149212">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «حالا می‌خواهید طعنه‌آمیزترین بخش ماجرا را بشنوید؟
🔴
اسرائیل همچنین از بسیاری از کشورهایی دفاع می‌کند که هیئت‌هایشان همین الان سالن را ترک کردند.
🔴
در واقع، می‌خواهم بدانید که بسیاری از رهبران این کشورها به‌صورت خصوصی از ما تشکر می‌کنند که تأسیسات هسته‌ای ایران را از بین بردیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/149212" target="_blank">📅 21:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149211">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نتانیاهو: تخریب تاسیسات هسته‌ای ایران بسیار سخت بود، اما برای من یکی از آسان‌ترین تصمیم‌هایی بود که گرفتم
🔴
من به آقای احمد الشرع سوریه ای می‌گویم که یهودیان از زمان موسی در بلندی‌های جولان بوده‌اند و اگر جرعت داری علیه جولان اقدام کن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149211" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149210">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
واکنش نتانیاهو به ترک سالن توسط هیئت های کشور ها: اگر هنوز بزدلانی هستند که اتاق را ترک نکرده‌اند، از آنها می‌خواهم همین حالا بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149210" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149209">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP4scwV9kA4gcFApPnP4K5zlTgtXnWfjARByKJaOE13r8ldIRNWN_9ylsrLb-WR6gQu9OkTHR42QVwLZ7UnDJ9777_W7Fhhfb3gUNKjmiRaF0bIp-Wt1qQfBku7Mu7jmiGcAVtOKnZ_8SwJ5qlx79VKOIX0EyWsPeVFdYBjabG3nIp-lI_YOkyyzj8beVf0OuUAipsyCQTDaS71o7kNikZp31PCPdjJqMm-wDTeKPt9augzJUqCqVCeLdjj9ipujUIHmfB0opC7Q_t9ka2KT2TlhJU7kmbE4LabV4fggqImOpWs8iMkaWn8yKOsKkgz37BFGZnX_98KQRBEGKiSBpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکنون رأی‌گیری سنای آمریکا در مورد قطعنامه اختیارات جنگی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149209" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149208">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پزشکیان، رئیس‌جمهور ایران، قرار است امروز ساعت ۶ عصر به وقت شرقی آمریکا در گفت‌وگویی با «برت بایر»، مجری شبکه فاکس نیوز، مصاحبه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149208" target="_blank">📅 21:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149207">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromver2 vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MezntaIeQ4rqHLX7HZmXjHczgugsp2RqaD1Fm9Zf-yQStj1UMz1zQcDkbLkCUmYiP2Zmiy27fVZTLg94bK78FDl2jHuwT5VWvuWjdDy0UhRXUx6C0h9YPIWZUcCgkWgRwEX2x1FoQPJSs8aCZP4S1HrO1-SZp-Q9sMheCTtqHGRM5wiXxhmGuB8ouQgn6At-wqoxz1AmYuUxSWaUVGZ-_62j6O-naZ9D9wB_25xD3sQbcg1XcV5Ylb3sjc-2ZhZpr0X0HCQgcXB4kDh-qPNj8nD6PK-UODUMceNx6xJz3Gl8S-OTUseBf9NyAevNlakhBbWLL1Vxk7FDAS9Qbsz96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
--------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
دارای IP ثابت
💥
سرعت بالا و اتصال پایدار
💬
تعرفه ها
🔸
سرویس ver2
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود ver2
▫️
تک کاربر — 180,000 تومان
▫️
دو کاربر — 230,000 تومان
🔸
سرویس ver2 ویژه
▫️
10 گیگ — 30,000 تومان
▫️
20 گیگ — 60,000 تومان
▫️
30 گیگ — 90,000 تومان
▫️
50 گیگ — 125,000 تومان
▫️
100 گیگ — 250,000 تومان
🔹
نامحدود ver2 ویژه
هفتگی:
▫️
تک کاربر — 129,000 تومان
▫️
دو کاربر — 149,000 تومان
▫️
سه کاربر — 169,000 تومان
ماهانه:
▫️
تک کاربر — 240,000 تومان
▫️
دو کاربر — 360,000 تومان
▫️
سه کاربر — 450,000 تومان
🔸
سرویس اختصاصی
▫
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 300,000 تومان
▫
100 گیگ — 600,000 تومان
▫
200 گیگ — 1,000,000 تومان
﻿</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149207" target="_blank">📅 21:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149206">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2774d824.mp4?token=vrMgTOLGNX1ohMgAN2Y_fuzvz5XsEUk1hEyQ9XqdkA-PAqpArgzQB-PBoZIt9BHH_TBwIOPy5pbdronRNJfDwlC2ADYI2sjYbNUFLS1owS28M8C0a0iC_IRSyU4jwGqQeFcWtFrGsK2dIQpm8Wq8TV70edVmSj8U-2aoqkYIPUHDaP2hXC2C6P7t-x3Jz1ri1t_Ac7kSGfzdsyYLUSL8Ali8Zf-Ppf53qFnJ-fKpzTcFo4nLPGLnQxXkyGQdBC4UBTFFnjdcFze24-P_gcYFSymuS1klEgtywjWgoP4fMfH6zGtCDvPGtRosyip_fBd1d0julviQ3rIn2gpRUpIbQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2774d824.mp4?token=vrMgTOLGNX1ohMgAN2Y_fuzvz5XsEUk1hEyQ9XqdkA-PAqpArgzQB-PBoZIt9BHH_TBwIOPy5pbdronRNJfDwlC2ADYI2sjYbNUFLS1owS28M8C0a0iC_IRSyU4jwGqQeFcWtFrGsK2dIQpm8Wq8TV70edVmSj8U-2aoqkYIPUHDaP2hXC2C6P7t-x3Jz1ri1t_Ac7kSGfzdsyYLUSL8Ali8Zf-Ppf53qFnJ-fKpzTcFo4nLPGLnQxXkyGQdBC4UBTFFnjdcFze24-P_gcYFSymuS1klEgtywjWgoP4fMfH6zGtCDvPGtRosyip_fBd1d0julviQ3rIn2gpRUpIbQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عباس عراقچی، در حاشیه مجمع عمومی سازمان ملل متحد با «اد میلیبند»، وزیر امور خارجه بریتانیا، دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/149206" target="_blank">📅 21:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149205">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOyNi4TeBY2jWTCblvM1f0bhy9v-VkpjPHg9rBWJkuinhx-Th4uxmUTwjrxz9tvBTqQYd5yYMXm2__gXupvHtyw0cHDcdXeIlyYNou1gZPivBIoOgjtgAqfeu5oxHPY0KvyvFvzLcCDlem8-GRqrn8wxsYDByXN3j2-ntX-iwdPhPddJwxe9bUFBlenmjoL0iPtYpZ4rX8F1hQkJ6uOqyV0A2phnLWiaJsUz3GARSc2j62FpNeLa7vaf2k83l8Jr-rA75qe0Nt6LZFVJcuEkXHwNDDOTBetsJCCNotYFF42COy0VYLjdFE-BEVcDzJo-iNiu9sG10dto47gII3pxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطعات کلیدی جنگنده F-35 که گم شده‌اند ممکن است در دست چین باشد
‏
🔴
سی بی اس نیوز: گزارش‌هایی وجود دارد که محموله‌ای از قطعات گم‌شده F-35 به دست چین افتاده است. این جزئیات در حالی آشکار می‌شود که ترامپ با شی جین پینگ، رهبر چین، دیدار می‌کند.
‏
🔴
بلومبرگ روز پنجشنبه به نقل از منابع گزارش داد که شرکت کشتیرانی غول‌پیکر UPS در اواخر ماه مه در حال ارسال یک سایبان کابین خلبان و درب محفظه مهمات از استرالیا به ایالات متحده بود که مسیر آن تغییر داده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149205" target="_blank">📅 21:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149204">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90322c0135.mp4?token=Y3noMXFnJ6_M7weoYbLjk90QRObAP6WqtXyTq1f_niI8r92PUQzxFUvqYmP8WmhvkH2JaOfK_amCkeG8TpgMHUCZFaJOlSx2u3n1STCoCdO8L4yHwT-0jyNJHhnF22yCHFfsu9OGz4YrgXegzilT53bblawl_f0okDT2SsolxeZUmg-a6tl67IxcjywSMZkUJzpF41qRORsAK0Z64IfvUt-YtfiKJpQNY2fxCPHssB6aXuzjn7CRFNaSRXwqVYfvaU_giedBMpf-yiAe9OBVw-kR7_6KcpLL0NkAdTov7feXlsNZdQ9zAy-e-vpuGd5T45asMC25UvNADO3dtmuLrD4hYVLUxEZ4gBeR_z4AVdGrAxZXq7Da3ILLezFW3wpqSJyTq8IV0fTixJ0sJWMF49Rybssq88S5F8bx2nUwLFRYtfOZHF3XjojOMhnUMB6nrNl0UqsKHYjiGxW_5OVch469R21_oacTbDzlQab3U8xldsJLYboQ5UCQ140aMewe72lfN5COJbM8g_cRHQv13BSCjI3azmlYMnaWozHiN99neg_n55y_k2MMOFx4Q0YHBz-v-q2l0LHfi9q5dBRgng5NnUC0CyBgeFS5Du7AQPXQlU_f2sfPH2JdfWm6Z01O7hXvZfvpgVFd9es_4gt0BVPkNUCmJKIM8OwWxjtLNl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90322c0135.mp4?token=Y3noMXFnJ6_M7weoYbLjk90QRObAP6WqtXyTq1f_niI8r92PUQzxFUvqYmP8WmhvkH2JaOfK_amCkeG8TpgMHUCZFaJOlSx2u3n1STCoCdO8L4yHwT-0jyNJHhnF22yCHFfsu9OGz4YrgXegzilT53bblawl_f0okDT2SsolxeZUmg-a6tl67IxcjywSMZkUJzpF41qRORsAK0Z64IfvUt-YtfiKJpQNY2fxCPHssB6aXuzjn7CRFNaSRXwqVYfvaU_giedBMpf-yiAe9OBVw-kR7_6KcpLL0NkAdTov7feXlsNZdQ9zAy-e-vpuGd5T45asMC25UvNADO3dtmuLrD4hYVLUxEZ4gBeR_z4AVdGrAxZXq7Da3ILLezFW3wpqSJyTq8IV0fTixJ0sJWMF49Rybssq88S5F8bx2nUwLFRYtfOZHF3XjojOMhnUMB6nrNl0UqsKHYjiGxW_5OVch469R21_oacTbDzlQab3U8xldsJLYboQ5UCQ140aMewe72lfN5COJbM8g_cRHQv13BSCjI3azmlYMnaWozHiN99neg_n55y_k2MMOFx4Q0YHBz-v-q2l0LHfi9q5dBRgng5NnUC0CyBgeFS5Du7AQPXQlU_f2sfPH2JdfWm6Z01O7hXvZfvpgVFd9es_4gt0BVPkNUCmJKIM8OwWxjtLNl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره شی جین‌پینگ:
«شی در زمینه سنگ‌ها متخصص است و عاشق گرانیت باکیفیت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149204" target="_blank">📅 21:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149203">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نواف سلام در دیدار با پزشکیان از ایران خواست سفیر جدیدی برای لبنان معرفی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149203" target="_blank">📅 21:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149202">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
به گفته منابع عربی، ایران دو موشک بالستیک را بر فراز حریم هوایی خود آزمایش کرد. هیچ برخورد مستقیمی رخ نداده است. این یک نمایش قدرت در بحبوحه تشدید تنش‌ها در خاورمیانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/149202" target="_blank">📅 21:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149201">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149201" target="_blank">📅 21:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149200">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
اسکات بسنت: محاصره دریایی و هوایی ایران ادامه دار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/149200" target="_blank">📅 21:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149199">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCS3iaoFQgemMlQECVpy7f_Y6r07LppSlJdgSCgG_DfIVwfxTW-LMazx76ktbWXpd-9GjsHL3IBacl1YSpYufsdzkleVOjtWrT5KTLaR_UXPDUNUcyPW3i5JfJT8_6vz2jJQw76Fnvi-WjNPhEm8uZhassKXBSHHK_JDpV8F6q-aWW1inpV40mFnNubKUyLZt6487oR8YlSnGL0EA-vHlVl421pOP6R0aaWkbYzWoXdHzTSei3nBQrdJBTubF0e5XKOd07NXvfiVUFMG7Zm-Ezg7r825AAkPil7w2G6B9cX6mx8FB0ja28xtIDKGZExAPfOXbU0OJDIiaoo_Gm5i4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی بعد باخت:
بازی خوبی بود امیدوارم روند بهتر بشه، این شب‌ها از مردمی که تو خیابونن میخوام تو عبادتشون ماروهم سهیم کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149199" target="_blank">📅 20:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149198">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
اد میلیبند، وزیر خارجه بریتانیا:
«یک سال پس از به‌رسمیت شناختن کشور فلسطین، ما همچنان به پایبندی به آنچه درست است ادامه خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149198" target="_blank">📅 20:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149197">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/شی جین‌پینگ خواستار بازگشت فوری ایران و آمریکا به تفاهم‌نامه «اسلام‌آباد» شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149197" target="_blank">📅 20:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149196">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
گزارش شلیک موشک به تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149196" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149195">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پرواز ایران‌ایرتور به دبی لغو شد
🔴
پرواز امروز ایران‌ایرتور از تهران به دبی کنسل شده. ظاهراً امارات اجازه ورود این پرواز رو نداده. هنوز علت رسمی اعلام نشده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149195" target="_blank">📅 20:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149194">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
۸۰ کشور با انتشار بیانیه‌ای مشترک در سازمان ملل خواستار بازگشایی فوری تنگه هرمز شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149194" target="_blank">📅 20:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149193">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رویترز: مذاکره‌کنندگان آمریکایی و ایرانی در نیویورک در حال بررسی مسیر مرحله‌ای برای پایان دادن به جنگ هستند
🔴
مسیری که شامل بازگشایی تنگه هرمز از سوی تهران و لغو تحریم‌های اقتصادی واشنگتن علیه ایران می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149193" target="_blank">📅 20:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149192">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrL858xQHFuDsaLYOJrCWp_Cm3zAhX1F8PfuKGtFl0sKADS8ShwaXwOhcDj0pFMtFN2zwXblGSKbC_UzuBWMc6qxPXa9Om1W5Hw93WDeCIKIBIQGwKz0hBjCl21xE_YU5pk7bcFpKvkzRvJpdnQswJD80JbtZPH67yi0xtGN43AP_e10whSFYUzFaiUoojEidUGGAtjdaLnmsQaEN1Acvio-2XydHcZAFnXKDbjOibjj74LbnhrrTpuFLqZldqVFT2olzcJNIsONeSUabONeh2bL1i1GW_6HixEcWAHohWeJIH1sjpcQ-wJtEJD5KUMGrM2vmFLfabLyP1rsNeO40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت به ۱۰۸ دلار برای هر بشکه افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149192" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149190">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pel5UulxKdqJh5g3Cp-JLrumZBskbhL0FLsS4gouDVUmyjm3lAiRhQC5QQbd9k7ltwcVPKVXESQM-gveAZomcBvw9lUI9-Nco5Aj2AvlkokyyhiFZpqPHZk4c2S2t_Ls9qhe9XWbORGOxzzRBOP2Lx8KBB1__izcRxWn1QE4Nv8HCbOZQ0_XmXJAIgKRbllJxF8We9Oyzz7dTPLkMdQz2wqULmxWQtkDXuvi4798oI7OtY_akvo1BEV-gvh34KiwJiqzCHWc_25DXuE0tAleRPEnFoeGRgiaXB22RWdxkskqWqCtlj-YaC_eH8tj2ha20V3lP7O2ilc_j5XsJ-JrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGE19Brmi5fyMSF1592iU8eg4wgc2mNlJvYbVJVjb6QR34dHw9iMgme8Sxwmjrb2bQVYTI1mXvZTGXHbu8w0ecnwXmeCjRQPMuf7A1ViNZkptrC2uWGO_8dvExb2FSeeX1rVGF7E6v-m1X1fPJ3W_my0rLVeB3yJcexLJfwqxCR4aZTcFG2vveZrqcJSdDL54fYbcP4e5hdNHA480ea_esmQ-D5SWkUGoYvV9HInsBXqQ5FCtmq-usUUPkIpI19tb1_kJbArUejuSw8fACfQcDvQpvy-bSyXfzGTY7RLNnSzgi5fwEFL-WN2n6BTRY-bWybZJeG9VdXZL4tjSed_aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه ایران در حاشیه مجمع عمومی سازمان ملل با فیصل بن فرحان، وزیر خارجه عربستان و ایمن صفدی، نخست‌وزیر اردن دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149190" target="_blank">📅 19:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149189">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voePzHg8B6ioROp0Yo6a5qlvYLCp-5lmyJNMDil1fMMaamneeoO8yMtMeHK2MzyvqLFgfozE3veavnzBnd-_V59ms0JzYH8tzd0IcQfdt6f7w4UHKa3o897iKAjQtReE2amgZGFoOCfXnXFoWEh7kgi7JHjultYF-GIvR9TH6H94xLmlLBNK0GgYd0hrbt5rzHWtZchPxz6iUKVMIybXao7jzq22dFEV95s4nSJfezvooX-IKi-saEenrftILlEpZOs6RdJ52E01LAWlcxnIBxJt4CSTzE9Kg43HsNh_V3EyDcPF3xJnrLHN1eFZh0jgk8v_CIUuHyTKtA6-zYZqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، و شی جین‌پینگ، رئیس‌جمهور چین، در دفتر بیضی کاخ سفید در حال گفت‌وگو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149189" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149188">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ac28e8cd.mp4?token=QkJXJeol3CWGpHUmOZjJ059JielAiuY4rZBz6Mtc4ha8ND7mQw7pxWP3tTMFHE-ZfCdkt8ImsNzxJ_g7DLEUBhkXD4et8gDZp6KMZAFUXG2H5Y4yTbwWfevQi61-D8OEZrbY-dQgvOpFaj-CrDyVIQkn5XcoPQrEWt5CPdQ2XwXQQiBcTFyQ__KmUU4ODL5EhJMZkB6bZsIh1bTs8JyGqnb6pKkvJ1fMz3T9dMclw0hpx1EeQMr4m52VBnZi6q8M463dpfYenzJB-z386-xEoKARfXObXOhiKOUi8ZHHRkmB-Z61Z5VmEapQGTwr5h9w_K-n0OfLMVdVwglLeOo1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ac28e8cd.mp4?token=QkJXJeol3CWGpHUmOZjJ059JielAiuY4rZBz6Mtc4ha8ND7mQw7pxWP3tTMFHE-ZfCdkt8ImsNzxJ_g7DLEUBhkXD4et8gDZp6KMZAFUXG2H5Y4yTbwWfevQi61-D8OEZrbY-dQgvOpFaj-CrDyVIQkn5XcoPQrEWt5CPdQ2XwXQQiBcTFyQ__KmUU4ODL5EhJMZkB6bZsIh1bTs8JyGqnb6pKkvJ1fMz3T9dMclw0hpx1EeQMr4m52VBnZi6q8M463dpfYenzJB-z386-xEoKARfXObXOhiKOUi8ZHHRkmB-Z61Z5VmEapQGTwr5h9w_K-n0OfLMVdVwglLeOo1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو، به مقر سازمان ملل متحد در نیویورک رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149188" target="_blank">📅 19:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149187">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
عراقچی خطاب به وزیر خارجه پاکستان:
نقض تفاهم اسلام‌آباد از سوی آمریکا سبب تشدید تنش در منطقه شد
🔴
پیمان‌شکنی مکرر واشنگتن، موجب خدشه به جایگاه نهاد میانجی‌گری است
🔴
تشریح آخرین وضعیت گفت‌و‌گوهای ایران و عمان درباره تنگه هرمز و تعاملات با ایالات متحده از طریق قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149187" target="_blank">📅 19:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149186">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deaf5a7be3.mp4?token=Q85FAgYzvXRAJejV6xzGaSrbfWA-KFngnjkAmpx8wZgZTtFkkiEVi80Os18v4u7SlV2JgiRZ4b8WbFddk7ZCib0feBPQn1j19lY7tPJrzgt1lNf9WoKkU-OMDBax6qVO0Kxe3wmtajJBvPjYCrpx8nRtLCDBXkUPQdebq4xHmEKeDCzVnaDJtI65-v8ae0JpXn6BSA4QXKy_g6PZDIyunoKNBwzsJA7xo7VU_QKeLVPM-zfQdZEf95z-D6zgosq63Gn-Oj6UzeOo1BafNWVBvnsn3NnNGBI8MS1P2GAkzk4utuswJMwak-qw-cO6oW49drJdItTNRHB4P-7J6Lq4yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deaf5a7be3.mp4?token=Q85FAgYzvXRAJejV6xzGaSrbfWA-KFngnjkAmpx8wZgZTtFkkiEVi80Os18v4u7SlV2JgiRZ4b8WbFddk7ZCib0feBPQn1j19lY7tPJrzgt1lNf9WoKkU-OMDBax6qVO0Kxe3wmtajJBvPjYCrpx8nRtLCDBXkUPQdebq4xHmEKeDCzVnaDJtI65-v8ae0JpXn6BSA4QXKy_g6PZDIyunoKNBwzsJA7xo7VU_QKeLVPM-zfQdZEf95z-D6zgosq63Gn-Oj6UzeOo1BafNWVBvnsn3NnNGBI8MS1P2GAkzk4utuswJMwak-qw-cO6oW49drJdItTNRHB4P-7J6Lq4yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار پزشکیان و نخست‌ وزیر لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149186" target="_blank">📅 19:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149185">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاهکار قلعه مرغی
‼️
ایران ۳ بر ۱ به ازبکستان بخت  @AloSport</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149185" target="_blank">📅 19:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149184">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqXqEO0WCeapr4vjUBTLBDbpE71Ry9wWoqYbCn4jL_n_ZJGIYeyLcY1SqSnwSRpWtPwUJ0wOno767OaMGl9yQppo9ySAziHwS6bJLVqhXFDn9txTP0OtaaALS_VNZuradnPi4SwK-G48wfVq67TPV0vjpXF_Xb6xte6y1KDNmGIHR24K-NKHFy36LLhUOfwtaqCRoefyBsU9FNEinupXRuwe12UiCrcovsnkmrdfmnj_0HPvQ7gnPuASMvJ3DfjZ1qMtc8JaXv23THvsotaRKFEgGAyJ__WBdw4qqfU7qzLUiFnZHvMwtBKBEWBJ9qkxdIh29r5Koj9Upv5A9XV0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: عربستان انتقال نفت خام از طریق خط لوله شرق-غرب به بندر ینبع را افزایش داده، اما صادرات نفتکش‌ها هنوز از سر گرفته نشده است
🔴
آرامکو در حال ذخیره‌سازی حجم کافی نفت در ینبع برای ازسرگیری صادرات است. بازگشت خط لوله به فعالیت کامل ممکن است ۶ هفته یا بیشتر زمان ببرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149184" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149183">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رشیدی‌کوچی، نماینده سابق مجلس: آقازاده‌ها از شرکت خارجی کالا را می‌خرند و می‌گویند فاکتور را بالاتر بزنید و هزینه‌اش را ملت ایران پرداخت می‌کند/ پدر آقازاده‌ها همه چیز را می‌دانند و خودشان را به ندانستن می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149183" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149182">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرگزاری رسمی امارات از تعلیق پروازهای شرکت‌های هواپیمایی ایران در امارات خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149182" target="_blank">📅 19:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149181">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=nT_om5bna0D6y6nM6H3SHzgd9L13tgHozsNC7bFiooSBVJEM0SfxEKuC9Juwf1SDQdEpQ7tZreHU_3uOm8SlcozhNqZYmv50aCcOkqS2f3HtyXOiCJDwc9pGPNCFgCwbb8u2d5DNkSIqhgJllVcAqUl-l7uuX_vcO81BO-_bUFMDBjVaY3WYtlRMDeRxfZ8t7ymFaKkBY4SPCyAKM4BJHR4rQH2CLhoTf26ZbbA_sB9VbIY2q7VwhFYxQOAMhXk2KNygQdtqtreBZfKNUNHC-_1Fpca6urv5iS8p5_rWU9t90aID4Oah3L5OJPC9K_7v5pCJKG3qS_mPjwjzWAhetCYNHKin4JjuvvhwAh5hEnKbxJhqPUc2EC5yhQvT-7UFhdUCDy99kLyEEhEgjffED_XQvczdmHwHqjkSa2JjvXQxtyeQwU71qlptboeKiQgm12SH2zGXrDkM69LNR_CN41ULm_7kKpjffwP67Pc06AOGEqeVhmB9vKA2HT0jWzAOsukBeOVdCjz9UuDF-8NmHtUolWNTdmH0F3J3fuQ-Ubx0_IF50FIAWFKyH4oS6Ik14SYKCDa1GFkFnA-FrmVX0nK5548FSfEt0DXco-ZpdlkQqhM4OSuL7gXl0RLIJXeiXRDdh1bhoPizFGYgsryRRgdptsQ7ewcs6yCeGIiKU7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=nT_om5bna0D6y6nM6H3SHzgd9L13tgHozsNC7bFiooSBVJEM0SfxEKuC9Juwf1SDQdEpQ7tZreHU_3uOm8SlcozhNqZYmv50aCcOkqS2f3HtyXOiCJDwc9pGPNCFgCwbb8u2d5DNkSIqhgJllVcAqUl-l7uuX_vcO81BO-_bUFMDBjVaY3WYtlRMDeRxfZ8t7ymFaKkBY4SPCyAKM4BJHR4rQH2CLhoTf26ZbbA_sB9VbIY2q7VwhFYxQOAMhXk2KNygQdtqtreBZfKNUNHC-_1Fpca6urv5iS8p5_rWU9t90aID4Oah3L5OJPC9K_7v5pCJKG3qS_mPjwjzWAhetCYNHKin4JjuvvhwAh5hEnKbxJhqPUc2EC5yhQvT-7UFhdUCDy99kLyEEhEgjffED_XQvczdmHwHqjkSa2JjvXQxtyeQwU71qlptboeKiQgm12SH2zGXrDkM69LNR_CN41ULm_7kKpjffwP67Pc06AOGEqeVhmB9vKA2HT0jWzAOsukBeOVdCjz9UuDF-8NmHtUolWNTdmH0F3J3fuQ-Ubx0_IF50FIAWFKyH4oS6Ik14SYKCDa1GFkFnA-FrmVX0nK5548FSfEt0DXco-ZpdlkQqhM4OSuL7gXl0RLIJXeiXRDdh1bhoPizFGYgsryRRgdptsQ7ewcs6yCeGIiKU7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند بمب‌افکن رادارگریز B-2 و چهار فروند جنگنده F-22 Raptor هم‌زمان با سفر شی جین‌پینگ، رئیس‌جمهور چین، بر فراز کاخ سفید به پرواز درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149181" target="_blank">📅 19:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149180">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
‏ سخنگوی دولت بریتانیا اعلام کرد: ما با همکاری فرانسه و کشورهای دیگر در حال تدوین طرحی برای مین‌روبی از تنگه هرمز هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149180" target="_blank">📅 19:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149178">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc9mdtbzNX8t1zWUFQUp2i9gEB-bX2uwdoBl-U4tsiyPm6tWLArslPHMB9tUIaUKPnP6HVKH6mv9gDjdW27WTJcKdhPfRLAyCMiyNyXM0rrjEVtdcsx0bZVBCoubPSxoCM0_5mi2nwA1hWxbi27GZQ9fWIZGnhhTqzCzCfGqNqJN0fnPJChhgjm-IKo29PM-WMzmKG_m1kJqZevcE4EZ1zFErgMwh-d4hBN3oIqyutME22F_TwTgMU1OhiD7Frh8ez5qFUlPePsnCu2CvX7twtam10jCB6eDli-kWzfyzSptjLAs5M71uLyaLptGBqU9YsuzifUxg_XaEgth3m8jyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به 107 دلار به ازای هر بشکه افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149178" target="_blank">📅 19:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149177">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان راهبردی و ترابری C-17 آمریکا به سمت خاورمیانه منتقل شده‌اند و چند فروند از این هواپیماها در اسرائیل فرود آمده‌اند.
🔴
این تحرکات در حالی انجام می‌شود که یک پل هوایی جدید آمریکا در منطقه در حال شکل‌گیری است و هم‌زمان گمانه‌زنی‌ها درباره…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149177" target="_blank">📅 19:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149176">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان راهبردی و ترابری C-17 آمریکا به سمت خاورمیانه منتقل شده‌اند و چند فروند از این هواپیماها در اسرائیل فرود آمده‌اند.
🔴
این تحرکات در حالی انجام می‌شود که یک پل هوایی جدید آمریکا در منطقه در حال شکل‌گیری است و هم‌زمان گمانه‌زنی‌ها درباره احتمال حمله گسترده آمریکا به ایران افزایش یافته است.
🔴
این تحولات پس از تهدید ترامپ در سازمان ملل درباره «نابودی کامل ایران» و در شرایطی رخ می‌دهد که ایران در بالاترین سطح آماده‌باش قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149176" target="_blank">📅 19:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149175">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uulrlvoI8IBbkw25OjhhdPLxW-kNR_Qtye79qOZk4QHuVCu1vHv9t3fIXW2J2cI3xYLmVqQcMrQvVawd-eZyRTOPKqzwV4uVRtlBwBXDvZGvQC_nRsGf5Ym3PsUOemQ7ex39YTC27cowhYC4eUCMWZxAUpAJA816mSHyl2azdnTBmfSpzm7xmCIKGd9v8mnD1eeOuPNOYEWvSU7038Es5lHxo9BUomVWp2RTnvQH5Xs3Gi_N2Ev3ND7vahgvl4PEVvdtqHi9PookeMxPGVVTAAudbzeDDmPuq9wxmNYIqlppoJAMk9ecxKoe2cOPNff33vCrgW--2zdhw44Pd2ksrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان، رئیس‌جمهور ایران، قرار است امروز ساعت ۶ عصر به وقت شرقی آمریکا در گفت‌وگویی با «برت بایر»، مجری شبکه فاکس نیوز، مصاحبه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149175" target="_blank">📅 19:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149174">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa9xzHChUQL37ftE7qcK0Eg19cbPgX1JNmuqWRuj8rE0_uI8496pBwkjpMc3dc8fpy90gLyD81L0YyT_HWjr1xFl9h01LEcNvMCLtuiypKMqnNbhysQc4rLe9XAjfb-C_BaNg_T_wlvJQEzTGmLjBxdApm6g_S9KqXH4l-V8Hbn3t2fdsJu3mKWE2_dDjbkjrfaMYt2jTKFWeg5z6_fRnqGhu_7XpzcArfab1qmI6by7LVY2sfdpI2w2kIaigky1q-RDX8WEYEsJbLTgs6-A1avGHtPa0XIYtQYA3t9-2nweCSGnRvg5W225rtN5d_bIhwWjKUpmZgBm-BXjsKHQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان در حاشیه هشتاد و یکمین مجمع عمومی سازمان ملل، با شهباز شریف، نخست وزیر پاکستان دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149174" target="_blank">📅 18:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149173">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7NAwi5YdOxnWK5LkyKhppc0r1z1V1uQnljfy_-M3Cm8WHgP6OTVjkrwEcEvdeF85rBBlGC0sJCsuDNH2qgW0moeozIwK77KQCdbrvtbAa7iZuQYrjihPIgAYwL2IALjb7VjY2pSY6iSwdKxFoE_kZM92XjU56INW77eZuS5aCh5NJM01unwud5-TzRLj8abzpf1PYU6KKvaeMQ2-kuIj1uic1o2-9iFehg973gHsyqeqHNLdBnyEK9WMxv0xtMxaQcjrpNOwrKKrT2tpO6NLbBV3t5pGyZ8Rlaw7GEdPQ97Ag7W32-KTEr6VNRoPkntdNxBoSplthcmi-U74BEDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعال‌سازی سامانه‌های پدافند هوایی در شهر صُحاب اردن، بدون اطلاع از دلایل این اقدام
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149173" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149172">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368d12a226.mp4?token=sNvud05c65krIj9_bvwt_upILLzU9PhYEUP5XBND4WfXF9xxK4VRsBOVH8WFOKQw_DzOWNGXuji8u5-FAnEOx75VA4ixVJcYuGD7Xcy6FhZ0tDosdR0YVqeBJvClBwYcg33rQzoko02lS_xY2xnzneMuuGYb5Lw8nOnY1sm2E3E8zDw-qrTTqTKpEpXNlA9I8JsUD4sJF5uIErzehlLrL0i79yx08qNrlbl-CUbzYvK7aJ6BAUQ5u9q7mzTJBzDHLUqalyQ9A_bwFX-0moaw0oc-8eUFdPaX3Sv5p3kPZRtT6lyFo9tzktJEN0dM4a2SCwhyEYtUeZm5Qk7Zhfk7IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368d12a226.mp4?token=sNvud05c65krIj9_bvwt_upILLzU9PhYEUP5XBND4WfXF9xxK4VRsBOVH8WFOKQw_DzOWNGXuji8u5-FAnEOx75VA4ixVJcYuGD7Xcy6FhZ0tDosdR0YVqeBJvClBwYcg33rQzoko02lS_xY2xnzneMuuGYb5Lw8nOnY1sm2E3E8zDw-qrTTqTKpEpXNlA9I8JsUD4sJF5uIErzehlLrL0i79yx08qNrlbl-CUbzYvK7aJ6BAUQ5u9q7mzTJBzDHLUqalyQ9A_bwFX-0moaw0oc-8eUFdPaX3Sv5p3kPZRtT6lyFo9tzktJEN0dM4a2SCwhyEYtUeZm5Qk7Zhfk7IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین پینگ: خوشحالم که دعوتی را برای ۱۰۰ هزار جوان آمریکایی اعلام کنم تا در پنج سال آینده برای تبادلات و تحصیل به چین سفر کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149172" target="_blank">📅 18:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149171">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال‌استریت ژورنال: نتانیاهو در حاشیه سفرش به نیویورک، به دنبال ترتیب‌دادن دیداری با ترامپ بود، اما این امر محقق نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149171" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ایران و اوکراین تفاهم کردند که تماس‌های خود را با هدف جلوگیری از هرگونه تشدید تنش در روابط ادامه دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149170" target="_blank">📅 18:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149169">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYiU6EtyHh6QIuO5H3rGl42KSaQ6E9gJaQOKK0QOtFutlxzTXF_EF9LJFtNPV0iF7Z7bQyXNeR-wA-SnY5uhHSDkiv9U7HkGB6dNtjSHxoSu7ljybI_Li1jF872SMrjuHkDNQOUz__DQHCeDAukTpB-3zopEbnlZWTT4Ev_zz9lLY-uQL7heRJxQEQtV00egZ-NbPAgOou7zeyRoT_tqfYIkABSHN0rTYuTHIh3bJ_3rnneaAI1qlju20eFBjFazyYr-Znnbpy1O3ZLCnAwLmwFD3QUbC95zZ-1o_awjFsJOjXDcAp3HbcwpCrQUdw4i3LQPrlP6DiySAFaL84IyRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشیال با انتشار تصویرش کنار شی، رئیس جمهور چین نوشت: فقط ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149169" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149168">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شبکه ۱۲ عبری گزارش داد که به دلیل ملاحظات و الزامات امنیتی، هواپیمای حامل بنیامین نتانیاهو در یکی از فرودگاه‌های نظامی و دورافتاده آمریکا به زمین نشست.
‏
🔴
این گزارش در حالی منتشر می‌شود که نتانیاهو برای شرکت در نشست‌ مجمع عمومی سازمان ملل در نیویورک به سر می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149168" target="_blank">📅 18:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149167">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ و همسرش، ملانیا، به همراه رئیس جمهور چین، شی جینپینگ، و همسرش، پنگ لیویوان، در مراسمی برای تماشای گروه "گارد افتخاری بدون دستورات کلامی" نیروی دریایی ایالات متحده حضور داشتند. این گروه، که از ۲۴ نفر تشکیل شده است، حرکات نمایشی دقیق با تفنگ و تشکیلات هماهنگ را بدون استفاده از دستورات کلامی اجرا می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149167" target="_blank">📅 18:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149165">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef0b8cbeab.mp4?token=RCWAriLvLBlfthPyPjAiW8lphLhyHCJ39UsfO4RVkhCh6OOdDsnit0Q1zF63MendvprPKz7iIbcNLjI-JSYIRHD6jxdhAUCKIvZMhL2-S2JFJKP2yavNY5P2yLsTEoJq56wUKiEqS4IZGHR7pL6N0AkY3vEF9PD3XX8fnOhgYqOp7PfKzHbtfNzbQOamww8pojebOs4GdHyBa2ieWkxIJWsJbvIoYvNydWiu36G8AqOLhmbUsThNVp27LBmMuMYg_lpKT2AyICWf76nSio5Z1f_au3RE1mjq1LA3txOBgo3T2TO-0yVNTDt0OK0AdiL9ZUR-VMWTC7tATxSdzE69HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef0b8cbeab.mp4?token=RCWAriLvLBlfthPyPjAiW8lphLhyHCJ39UsfO4RVkhCh6OOdDsnit0Q1zF63MendvprPKz7iIbcNLjI-JSYIRHD6jxdhAUCKIvZMhL2-S2JFJKP2yavNY5P2yLsTEoJq56wUKiEqS4IZGHR7pL6N0AkY3vEF9PD3XX8fnOhgYqOp7PfKzHbtfNzbQOamww8pojebOs4GdHyBa2ieWkxIJWsJbvIoYvNydWiu36G8AqOLhmbUsThNVp27LBmMuMYg_lpKT2AyICWf76nSio5Z1f_au3RE1mjq1LA3txOBgo3T2TO-0yVNTDt0OK0AdiL9ZUR-VMWTC7tATxSdzE69HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین‌پینگ:
خانم‌ها و آقایان، دوستان عزیز؛ تحقق آرمان بزرگ احیای ملت چین و عظمت دوباره آمریکا می‌توانند هم‌زمان و در کنار یکدیگر پیش بروند.
🔴
بیایید به انتظارات مردم پاسخ دهیم و مسئولیت تاریخی خود را بر عهده بگیریم.
بیایید دوستی میان ملت‌های چین و آمریکا را بیش از پیش گسترش دهیم و با همکاری یکدیگر، جهانی بهتر بسازیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149165" target="_blank">📅 18:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149164">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbca495c7.mp4?token=QQzjiz8COp0kDtECabkjGRC0Md5KXipUEyjZn4iR-Ud9Amhc5Yiy7EsTJTENNwHC2p_Gs8GMt6NOKrU7ToRThfM_Ozl3dTRXGcGcQsKJfmsJirFoMWfnH6uAem6zWqYPvNWQfO3T88N5YXqMlceCUD9KoqQovjv28WpBqp8Ixbr9kqrvSOc-s84a7K7WmG60LtYstOiAHU4DSDWq86Tvf8-DT2SHgWhgeMSdWijcfYEhXz8VuwhQwItxNUfgCHGb3HaylBT_L-r1brGbuKawn_q2gA-B39LcbhgTrymfPaM41AowR-8hvP5mAnVbsfJGXIuTTeIkt_4009eUFpBQ1YsfOyGyV57JNIEdjC0UIL_YSrFGzBv3uUvwKGChgGMaJr2nMcNjVrBGldVNMlBy_rt5GOwRu9qYOX0oAwCkJzly9SbYpyxHrfW_ofCV6i25ZpNmpAzc7HCUN4fS3Y8BcYzWvPFW9zYwT8HciDrTqdFdz1bgozFbl3jImxgsvmwW_JhQu5jcMSon-fwcULfYCMl9C1hxvs0hTVD9cGgXJhyqnoBuu6UsQ1bQY9EhFzBUt74xqQCdjbQ5Ft_zH-LzEPCVXBbqArH2KMnhq_Me7OhyNTjBkXLy-e93YDDLh0lp38PtD-pXNX5wKAFyfl4l2QgHNzP2K5kqjkvhavSHA0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbca495c7.mp4?token=QQzjiz8COp0kDtECabkjGRC0Md5KXipUEyjZn4iR-Ud9Amhc5Yiy7EsTJTENNwHC2p_Gs8GMt6NOKrU7ToRThfM_Ozl3dTRXGcGcQsKJfmsJirFoMWfnH6uAem6zWqYPvNWQfO3T88N5YXqMlceCUD9KoqQovjv28WpBqp8Ixbr9kqrvSOc-s84a7K7WmG60LtYstOiAHU4DSDWq86Tvf8-DT2SHgWhgeMSdWijcfYEhXz8VuwhQwItxNUfgCHGb3HaylBT_L-r1brGbuKawn_q2gA-B39LcbhgTrymfPaM41AowR-8hvP5mAnVbsfJGXIuTTeIkt_4009eUFpBQ1YsfOyGyV57JNIEdjC0UIL_YSrFGzBv3uUvwKGChgGMaJr2nMcNjVrBGldVNMlBy_rt5GOwRu9qYOX0oAwCkJzly9SbYpyxHrfW_ofCV6i25ZpNmpAzc7HCUN4fS3Y8BcYzWvPFW9zYwT8HciDrTqdFdz1bgozFbl3jImxgsvmwW_JhQu5jcMSon-fwcULfYCMl9C1hxvs0hTVD9cGgXJhyqnoBuu6UsQ1bQY9EhFzBUt74xqQCdjbQ5Ft_zH-LzEPCVXBbqArH2KMnhq_Me7OhyNTjBkXLy-e93YDDLh0lp38PtD-pXNX5wKAFyfl4l2QgHNzP2K5kqjkvhavSHA0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
🔴
خبرنگار :  ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
🔴
غریب آبادی : ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
🔴
خبرنگار : ولی با CNN رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید چرا با من مصاحبه نمیکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149164" target="_blank">📅 18:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149163">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017029214d.mp4?token=LM53qgtE4-4tFdm2y_8GzDqEE-dOIl82H-mqNQShU5-TqWYB4PHIPpuPNGBycJ-Ddlvp-o0e2hvUoE0CREdM8RiK6s0HfCljwvKdYWqY6gAmV9j2AKb9cLiQz2zfOVZTJQEabgE0lReDCYzf_0J7qbs9zA5noIIxv76eLNyFI5NTYa4QGyDByNohUfHltCyo8sF23u8_0Xw2tcl7pz5xWosxzdeVdc3affVSqeyksqBlQFAuFIWCYNcRAYXn8z7sMMOfPlVqdmxbFwf6cJAfLnt5C8PsJLmMebr1IiETWofiNwRLFNFzJ_wwzNKmFZP3sC-8NYaCrzlvrJ2rmZFfmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017029214d.mp4?token=LM53qgtE4-4tFdm2y_8GzDqEE-dOIl82H-mqNQShU5-TqWYB4PHIPpuPNGBycJ-Ddlvp-o0e2hvUoE0CREdM8RiK6s0HfCljwvKdYWqY6gAmV9j2AKb9cLiQz2zfOVZTJQEabgE0lReDCYzf_0J7qbs9zA5noIIxv76eLNyFI5NTYa4QGyDByNohUfHltCyo8sF23u8_0Xw2tcl7pz5xWosxzdeVdc3affVSqeyksqBlQFAuFIWCYNcRAYXn8z7sMMOfPlVqdmxbFwf6cJAfLnt5C8PsJLmMebr1IiETWofiNwRLFNFzJ_wwzNKmFZP3sC-8NYaCrzlvrJ2rmZFfmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جدیدا دخترا تو ایران با این تیپ میان بیرون
نظرتون؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/149163" target="_blank">📅 18:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149162">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">از نگاه مجله تی سی کندلر، محمدرضا گلزار 49 ساله، به عنوان جذاب‌ترین مرد ایران در سال 2026 شناخته شد.  همچنین گلزار جز 100 مرد جذاب جهان در 2026 شناخته شد!  [@AloTweet]</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149162" target="_blank">📅 18:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTcMyzllyZR0SwwweXX04uFcv4hSMkSzULM6CdpBXQscBJgUhUQdilBxtqlLD6FKXCH0hzMyiVE8nlbWl38ve5hdN21MWDiDBTRgbeuiM64_WydxsG4FJH5687ps7qPClFTivfaIrx8yk-uATqiodal0RRpOmlohTTWvtlcuB4XClJAEkGixwjyzX-mbFI57VvfY8M5nQ8BsGHTaMND6pG-mn445inbcooio8yPWi38sa4SrtEUUPD10TAsod_xCZHVj_3QL4wyfP5otTZ9aVTOpI0daw9qvUg6eneWbY5SAKLn89tj5hJqq-TZHUvmBIVKz-X_kl2UuWdtYZv5yFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوترابی: کاش آمریکا پزشکیان را همان‌جا نگه دارد و برنگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/149160" target="_blank">📅 17:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYceVQaFPM_8_oLrn9khfM1l13RboqU5EKaWyn_axufkWMbRQsSTDuELT0aog47ZUdGEnSQtK-EPiA9THqs3ycuf2hUhnJJbpzW03cGUOenbKsns42CX3WAd9iyuvYRtvq1p7QiJ-T3U724TLxjtl97VBKJ68rW2Ih9H93qp9kzM8a-fqn0icPoqHnbEM0CJTjkH2utHt4D8Uodp-0vnHIDUWhxq7FzXzEAefW3wemxAeeIjwhW4qd4dxKavXWweLPp1k2A7VNRJ9xlQBCxKLYgoLagML3foEsVw7JcLOsz1Mx81MDsN0qOEUttUCHfjuh69jJ1IyJouWLwI--E3dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرزوی موفقیت داریم برای تنها ایرانی دسته مثبت تاریخ مسترالمپیا بهروز تابانی عزیز
❤️
🔴
مسابقات از فردا شروع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/149159" target="_blank">📅 17:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نتانیاهو برای سخنرانی امشبش در سازمان ملل وارد آمریکا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149158" target="_blank">📅 17:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc96fad46b.mp4?token=NfT9iXzlKiuHXNgkHHEqhtsMJXKUTWfdv29GTxV3i76jcCH_svWowhKHgWNZ49RXsZM8GuBh3gG-PeF0YY6A5LSC6l74wbckPrP-ZM6RnRtWjV0BD9E_WoNZ5J4-VtpZDS0mxuWTqbaghHvyOvcYgUVNglorWGn8Q2Yeb4ECfN4EW_m35RBPSMSluq1VBY5r834pk3d1dyn8lOo9E0gi9gJc3fEEIKJO90dfThyjXvcT_oYc0Fp3iFnP9L1pBTaeA2cvB9Bgpxzd1w2ZkFolzpsCnRR-372I062ui_Jcm4_TxJBxXKO3G1Gzqb3JXpchFyolWoS1YR8L40oC8fyJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc96fad46b.mp4?token=NfT9iXzlKiuHXNgkHHEqhtsMJXKUTWfdv29GTxV3i76jcCH_svWowhKHgWNZ49RXsZM8GuBh3gG-PeF0YY6A5LSC6l74wbckPrP-ZM6RnRtWjV0BD9E_WoNZ5J4-VtpZDS0mxuWTqbaghHvyOvcYgUVNglorWGn8Q2Yeb4ECfN4EW_m35RBPSMSluq1VBY5r834pk3d1dyn8lOo9E0gi9gJc3fEEIKJO90dfThyjXvcT_oYc0Fp3iFnP9L1pBTaeA2cvB9Bgpxzd1w2ZkFolzpsCnRR-372I062ui_Jcm4_TxJBxXKO3G1Gzqb3JXpchFyolWoS1YR8L40oC8fyJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مدارس کشور موقع آغاز سال تحصیلی دانش آموزا رفتن بالا میکروفن دست گرفتن و دارن آهنگ تیرام میس میره علی گرامی رو میخونن:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/149157" target="_blank">📅 17:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
اگر واقعاً چیزی که می‌خواستند انرژی بود، می‌توانستند از راکتورهای کوچک مدولار استفاده کنند، که چیزی است بسیار مقرون به صرفه و قابل دستیابی برای بسیاری از کشورها.</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/149156" target="_blank">📅 17:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
به نظرتون وضعیت فعلی سر بحث اتمی که طی دو دهه حتی ۱مگاوات برق هم تولید نکرده و مدام تحریم به بار آورده و چند صد میلیارد دلار هم به اقتصاد ضربه زده، مقاومت عزتمنداته است یا حماقت؟  مقاومت
👍
حماقت
👎</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149155" target="_blank">📅 17:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
به نظرتون وضعیت فعلی سر بحث اتمی که طی دو دهه حتی ۱مگاوات برق هم تولید نکرده و مدام تحریم به بار آورده و چند صد میلیارد دلار هم به اقتصاد ضربه زده، مقاومت عزتمنداته است یا حماقت؟
مقاومت
👍
حماقت
👎</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/149154" target="_blank">📅 17:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
👈
وزارت نیرو:
پیش‌بینی‌های هواشناسی نشان می‌دهد پاییز امسال پر بارش و زمستان کم بارش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149153" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bksAqiKPMDWXTw2nXt0TM3iMBxX8piOV7yOkr-RorflRu6T5AwKQ88_6SEDi7uqtgK4WDoyZuF76sIH6Y8dHp_1eORarhmrdXmGeBSMbYLAjuW5vgrSFTnTiKVRM3y4uvvMpjfzjk7xtS52vOEUhkfQd916ZxarkTzDDHHWRe_s4xPAHKNZ1Vgc_h2UtWyDb8_L0IyePz0OcpU8iu8D0N6q-hk3GQ7B5FYqpf6w7r0V2zA0mxOu3pBinaaBn8B46-uN7nxznV-V3c1SQYc_cbja2leOxOIKck0RCvTb-gv6WqhWrFMAWep8KeEe9BA2JIMDFf7GFPgXcUTccG2EGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرلشکر وحیدی: از جنگ نمی‌ترسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/149152" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad942f49d.mp4?token=L_pWL0TfPXlW3MA6F8nMJPteR7NRaMueUoSCx8F-N6K1vxs-OQWOtZAddU2OJEaH2w5fWLtrvfNw5O5TmlTrak2B1FfAA_4oiy2pq9f_6Nka0_QeZkSTDBUWBGNpnvAXs5_skWVuSBew51fVbkhdwxyyp1d_C2zhP4hxNb-MumxKosWDG_iifeyn9atNO0dgGuRK2y2xPy6tz20HNA7HLst3POLMxFd1_UQqIlUa7Q9DYGvUZmlyvCrQAidogYk7bKB53wpUGE3qDnkifEB15yusWLpyOQCuFySw_CsNDPwEkcSKNh97N9kNGtF0gfmAPf9k-FIQeUgp745DoYnLeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad942f49d.mp4?token=L_pWL0TfPXlW3MA6F8nMJPteR7NRaMueUoSCx8F-N6K1vxs-OQWOtZAddU2OJEaH2w5fWLtrvfNw5O5TmlTrak2B1FfAA_4oiy2pq9f_6Nka0_QeZkSTDBUWBGNpnvAXs5_skWVuSBew51fVbkhdwxyyp1d_C2zhP4hxNb-MumxKosWDG_iifeyn9atNO0dgGuRK2y2xPy6tz20HNA7HLst3POLMxFd1_UQqIlUa7Q9DYGvUZmlyvCrQAidogYk7bKB53wpUGE3qDnkifEB15yusWLpyOQCuFySw_CsNDPwEkcSKNh97N9kNGtF0gfmAPf9k-FIQeUgp745DoYnLeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد از محاصره دریایی توسط ارتش آمریکا، از الان به بعد دیگه رسماً محاصره هوایی هم شروع شده:
+امروز پرواز هواپیمایی وارش قصد داشت از تهران، به دوشنبه پایتخت تاجیکستان بره که ترکمنستان و جمهوری آذربایجان اجازه ندادن این هواپیمای ایرانی وارد مرز هوایی‌شون بشه و نهایتا خلبان مجبور شد به فرودگاه امام برگرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/149151" target="_blank">📅 16:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsPFPJOKCSxXMuurBJlERBIXAIdiV937RjuWDXCKDYhlZpx-kt6MZeOwANIzjm4FeiLzFDGbbTn77npugWgAizx4wkJiAXqTUj77cQzYhkgkquCqsI1N_TEIe90FkOw6N-51z2QLdAeh-Ur15j5X-f30S2DyZvd4z8ScOvvEhIfArmo2lSuWwf_6txb0oN2dEtAou6u3T-4DZd-Cv2Ra62LygIqVQV-tHXJi4q-jhXQr6Wcvp6kGVPjG8rFbN-agVj0gJkNRB77fEHYHsds4LmzQIuwZq1nmd7VAR5xXmeqPBLPWLDDObXcJifzWP0YmqaSwJnpwA57D1AFei5WgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در سال ۲۰۱۲
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/149150" target="_blank">📅 16:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdbH12An-mfutm7cKRZHr6U6ShfJiIYzTyZoIxQJ8MxdpcDREWiGyFBorq_eB8m1UsP4GNvYHcDIrF85W7LISfJlEgJhe2wY1zQWaSr1u6Xi_1o_zvNmkAMxA8DyJLjUQyGlKceew7aEBYVuii12dqhKgbQHqZkNXod-_gcqLbk2Hv1QsvspVlnphSiWlTGzsia1m8InHwtByGXzalwW_CCtvkatslVl6Z2e-KKN46cAKsQoMxCOG_QwWR84BL7f4J4EOTOyaKEsCjJVcI1Z03Bhj9iY1qb2QVNHwJghWpCkX4vTOGU_tUjGBkqtYMi7keK1Ym9YDppTADqRnUrSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دیروز در فرودگاه با رئیس‌جمهور شی دیدار کردم و به‌نظر میرسه قوی، سرحال و آماده‌ست. بانوی اول شی هم، مثل همیشه، زیباست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149149" target="_blank">📅 16:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پولیتیکو: خبرنگار این رسانه با وجود دستور یک قاضی برای بازگرداندن دسترسی رسانه‌ای، از ورود به کاخ سفید منع شده و کارت خبرنگاری او ضبط شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149148" target="_blank">📅 16:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت نیرو: پیش‌بینی‌های هواشناسی نشان می‌دهد پاییز امسال پر بارش و زمستان کم بارش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149147" target="_blank">📅 16:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آمریکا به کشورای اسپانیا، فرانسه و ایتالیا هشدار داد که بزودی ممکنه روسیه بهشون حمله پهپادی و موشکی کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149146" target="_blank">📅 15:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae691e363.mp4?token=nTEt5w6-qNbPvjVYJCUnb2YHbyVcZYeDB4VSxQymA8Zgi_dO_0N_s4gY2ONmnECAEAMaF5NaAdUzWY7es_B2CfXAN_F2yx1qrH10J4i9qeWAI698pNU_Y2K0DtkQs8NBv0Y_rcwmuGXNHxvyJ1-K0XPxKltvyjG3A4oTmLbImc6fQcu7nPBNApdvuEUq4mPmgOIzY5q1Phg8kcXo-W4pXx1iUYOm-V51KuJC2XC7-JpJ2klH7IjAZ4MlIFLfYrKDhs-FgkW_gDpmIrG3Fri5qIfI1d-GyB4MSOQy7_sH0ItY1uttWv8gL9_wdf3B5QGIWkEmI_SvIIio-0JGICnP-KAwunkXLH4ew59ZSU3aOhf7xqZ4fVzSUtIbA1KPJ1MtuDdh5N-ZHQ88-0RUMP3T-ia0VifEGCxBGx2sNUFVjV8nX38aMSG0EljGXBFdKFaohO5smJ6EAJdA7bgPMF8Vs7DZ-i8ucJPh9_SlPiASoNHuiH9FxtVVIhZ1OXEAaVgDG5wo5lPgcELHW-_slokvZLGqEm2xcKQ5l2czfXZZFO6rhkDlgcxztSBqQPu8R1SmD2znsqptBcOOlvqDL-wWpHQ8oBwe2QN8H9j3M1FVplinV-Y3v6dzJM0DIa-uDsMo44DRWfNzNKCcu2HubFg4HszjbTLGRH60GDv7E2NcAfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae691e363.mp4?token=nTEt5w6-qNbPvjVYJCUnb2YHbyVcZYeDB4VSxQymA8Zgi_dO_0N_s4gY2ONmnECAEAMaF5NaAdUzWY7es_B2CfXAN_F2yx1qrH10J4i9qeWAI698pNU_Y2K0DtkQs8NBv0Y_rcwmuGXNHxvyJ1-K0XPxKltvyjG3A4oTmLbImc6fQcu7nPBNApdvuEUq4mPmgOIzY5q1Phg8kcXo-W4pXx1iUYOm-V51KuJC2XC7-JpJ2klH7IjAZ4MlIFLfYrKDhs-FgkW_gDpmIrG3Fri5qIfI1d-GyB4MSOQy7_sH0ItY1uttWv8gL9_wdf3B5QGIWkEmI_SvIIio-0JGICnP-KAwunkXLH4ew59ZSU3aOhf7xqZ4fVzSUtIbA1KPJ1MtuDdh5N-ZHQ88-0RUMP3T-ia0VifEGCxBGx2sNUFVjV8nX38aMSG0EljGXBFdKFaohO5smJ6EAJdA7bgPMF8Vs7DZ-i8ucJPh9_SlPiASoNHuiH9FxtVVIhZ1OXEAaVgDG5wo5lPgcELHW-_slokvZLGqEm2xcKQ5l2czfXZZFO6rhkDlgcxztSBqQPu8R1SmD2znsqptBcOOlvqDL-wWpHQ8oBwe2QN8H9j3M1FVplinV-Y3v6dzJM0DIa-uDsMo44DRWfNzNKCcu2HubFg4HszjbTLGRH60GDv7E2NcAfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کالاس، نماینده اتحادیه اروپا: دعوت آقای ترامپ از پوتین برای شرکت در اجلاس G20، شنیدن آن بسیار دشوار بود، زیرا با توجه به اینکه حتی چند روز پیش، تعدادی از افسران اطلاعاتی روسی به اتهام قتل شهروندان آمریکایی در خاک آمریکا دستگیر شده بودند.
🔴
بنابراین، سوال من این است که آیا این افسران اطلاعاتی به صورت مستقل عمل می‌کنند، یا دستوراتی از ولادیمیر پوتین دریافت می‌کنند؟ و من می‌توانم به شما بگویم که آنها دستوراتی از رئیس‌جمهور پوتین دریافت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149145" target="_blank">📅 15:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvNCk5gj-_NoFSjq04bpxVckQywWKc9JJlMlNpw2LFrknMr4N_0x3bnf7tAwHN3aBBKot5VLkQm7D_y5GqphHkoDfsFMu4nddD2fmNPfeLZRsjmHPHznyFJPnyqnS8AzUC3nxJnJ7v6NAZOu5zqHKppiDjU5Mb7Zpq4AQrZNgyxDAeqs0rIkYqbo45_5B2evzgIsgFWNuyarVLE9NCnX2jJ3TP0vWADxcvP-4-Ewi4xfxwa_vcEMS-8HfoYXp5oGzZBB2mfgPLjJP92n_M0e9bHNBbN7tWNgFWoptJOKUly8zvIRVgzYAen2wBr1utVzZLWfrYnBsvGBbO31d8bHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: امروز روز مهمی با رئیس‌جمهور چین، شی جین‌پینگ، داریم. ابرهوش (SI) یکی از موضوعات مهم گفت‌وگو خواهد بود، اما من می‌خواهم شرایط دقیقاً همان‌طور که هست باقی بماند. موضع چین هم همین است
🔴
چارچوب کنترلی ما وزارت دادگستری آمریکاست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149144" target="_blank">📅 15:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149142">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-hZSgDpsalz5ZZD8mQ6lMoqysqsA-YpEWOh1SilnIo-UdEcP7iie2yhGgEkn7Zoms7Uq09H_deuCwn0PS25TmOeIGCxDP10kCw1hO_3L1qg_jIbxQU88S5TFwmqm-S3qJ3P5aiAREN0d-YOLsDS6fBn4LgNrbURkuSq0dbE_UTpY5qEZZI5KO0tbKD1dlHu8q30FxM_9cBtuWr-KoyWlvlRVOxHGfqkST-uy4ZhYrtv33gm14dxgGId7_Ejy4fOS-y8aq4xolMYYQSO6gIHZbxMDBlf-bOxAmUw992Ta7ifYbRCuGcsWNtNQmKJVX8ZcY5o5d70UbVPi65VlpIhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای تانکر سوخت سعودی در حال پرواز از فرودگاه جدّه به سمت جنوب و در مسیر یمن مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149142" target="_blank">📅 15:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149141">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بلومبرگ: دونالد ترامپ، رئیس‌جمهور آمریکا، و همتای چینی‌اش بر سر تمدید توافق آتش‌بس تجاری تا ۱۰ ژانویه ۲۰۲۷ به توافق رسیدند. دو طرف همچنین با وجود اختلافات موجود درباره فلزات نادر، محدودیت‌های فناوری و موضوع تایوان، بر جلوگیری از تنش‌آفرینی تأکید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149141" target="_blank">📅 15:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149140">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مراد ویسی :
آخرین ارزیابی‌های منطقه نشون میده به احتمال زیاد حدود ۴۰ روز تا جنگ بزرگ و حمله آمریکا به ج.ا فاصله داریم.
تنها درصورت عقب نشینی ج.ا ممکنه شرایط تغییر بکنه!
🔴
دیدار سه‌شنبه ترامپ با سران ۱۲ کشور منطقه نشون میده اون برای جنگ پیش رو با کشورهای منطقه هماهنگ شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/149140" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149139">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سی‌ان‌ان: در نشست ترامپ با سران کشورهای عربی در نیویورک، قطر و عراق با هرگونه اقدام علیه ایران مخالفت کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149139" target="_blank">📅 15:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149138">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJy89jB8GqeS63hd7jcVp6-8AERXUsZh3m5WAyyw8cpP3ElpMgWF1I1Li17Oz5_-KWgIBxfgHSbxLz6-Uf2ozcnA6ShKx1gr4NvIOMv0nMw9v44GLrpuQAGQzkPUhzKMUPjhm7uWAXWDGpn5aejqPQLVFMTgaBI8GhWZvqAf1ml9vM5FCXXhvCMtPES4BiWjq3DTRsuE3aP9A11ZBjN89FhRNVBVm3sBiyTOG8HdJh7icJjPAb8ZbEnMpPCnIAwK0XBuMv0Znk4SeWNX73qvFEfixdp-67vcaZXsLvN8-AJ7J6OSC7fOZqKmftLnISgbC9Ut8i1xa-pJLRSECR3UVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنای ایالات متحده ممکن است از روز پنجشنبه به یک طرح رای دهد که بر اساس آن، رئیس جمهور ترامپ ملزم به پایان دادن به جنگ با ایران خواهد بود، مگر اینکه کنگره مجوز ادامه آن را صادر کند.
🔴
دموکرات‌ها تلاش می‌کنند تا قبل از انتخابات میان‌دوره‌ای ماه نوامبر، این رای‌گیری انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149138" target="_blank">📅 15:00 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
