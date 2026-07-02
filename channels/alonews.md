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
<img src="https://cdn4.telesco.pe/file/YI0GtSt8hTVbTAqnttD0ozQm4pszOccuYQS7N5l55qH5Px_ViJ04Kn5PvRar7_yLyWxoWPM-Mm2pcaZ-dJXiicUEct6eh0D8_jzHi2NJzBs7Ss9QATfHfdbXStRwaC5XPLaOmvToElmZMI3WHPyXGxWmJtxAjiKp3XVawBmRVcRFCUbboR3akn0YKTpFH1j1VqUqUSewsPwLACHUi23iRMI-04tuxwwQdzzW3QWOzPzQyAMoSuNyyq6ufeeB8rdWFqvS2-g-U-UIJgUEyv3uZBCJQ5dqS8428KLi6UsuP5sM0rl0aAB-GFxoUmLLOoj7qsy3LyS8wWDje21pTCWDrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 02:04:33</div>
<hr>

<div class="tg-post" id="msg-131533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Di4o5Yp1GJin7u1zKlg3boR6EG34qJ8KCyY-g5L-YTrzVIFTgMF0A5nLfGtfDgFOBgRKRuF_rXx9jKuynL3D6xmiIM8N21tENkbM7MumXXdXikN2LjgeFgX3Zn17AhEetFf2YHXazd4DhVsIIvKiV1h8M4SyqZFIC5ovMw0nalV4iirr0AMcWi-MKjZTej7sz0qIZcSy_yOMl09HZiSaMgVRBx_jLF4rlMjqkjM-_eoCNcjWA4__iH0Kha9yKzlWKe5AifETIyhIdV3QAsmMXRTqOdnVwB-QoD_KABLNerDahRkoYSGqEJKePdXB9ZRr4MhfRUahrqhv05ebuq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/131533" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131532">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3df6d8da.mp4?token=iMLVQjAlbdvWsQH9uCW9E7c3NUj3FkLx02JpASOM3CDXB4lKTjuhZxYSs1Ba5RAy3dkCBRz7_oanBJFCtzSmJzmdgOg_zouvBrKaa5I_H74gYRgsEGSkspm29bLI2K5RBXLF0wo32C5m7LInEB1TKqq-TdIGux_p0xV4iv8Wmrb3PXeWWd4lDiC_7L2NQwBeknibG9i9K-2i051aGVy8tHVqiFrr6YSxJI00wzfH2iWSVuDt86lnCdc1mrVQxqY9XnE9_BTV2sqOkohFk-mn6wRZl1n7F_u-UHFjArbBTxWlBsA_BN6UtMMW09dDfYd7bJAeTOxmyd9yWpgpXmJWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3df6d8da.mp4?token=iMLVQjAlbdvWsQH9uCW9E7c3NUj3FkLx02JpASOM3CDXB4lKTjuhZxYSs1Ba5RAy3dkCBRz7_oanBJFCtzSmJzmdgOg_zouvBrKaa5I_H74gYRgsEGSkspm29bLI2K5RBXLF0wo32C5m7LInEB1TKqq-TdIGux_p0xV4iv8Wmrb3PXeWWd4lDiC_7L2NQwBeknibG9i9K-2i051aGVy8tHVqiFrr6YSxJI00wzfH2iWSVuDt86lnCdc1mrVQxqY9XnE9_BTV2sqOkohFk-mn6wRZl1n7F_u-UHFjArbBTxWlBsA_BN6UtMMW09dDfYd7bJAeTOxmyd9yWpgpXmJWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور:
نمی‌فهمم چطور یک فرد یهودی می‌تواند به یک دموکرات رای دهد.
من بهترین رئیس‌جمهوری بوده‌ام که در تاریخ اسرائیل وجود داشته و آن‌ها هم این را می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/131532" target="_blank">📅 01:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131531">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac200869f.mp4?token=p9CqZzHTYn434WoDJ989Vnl_kNValWgyv3v0JjgCOFB10DUG-gRjsf0aGXDDMSFaWIRd6CNiGwth8GreUbiZA59EI9GeSTZDKVBDE0vQ-z08a3yfr2-FbBRWz2zxPBwBat2vZ4IinvzGDCHUzYyFeMyla6OnYJiDVoa1HLQiZMWJ3pLqTI0FXZbI_iJf-IpiHAjG7eKIfXaqm5mkbdObESHv32649nQn6nb0FecqH9UccKfm3migkb0qmwEVsNu2Fd155UZOae1n5QePRvkJpSLYQMpj6igx6wtSr8eFXXS6JQL3orH8ZY6tef91aKGK2XAI5nWs7kxA_bMg-x9D2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac200869f.mp4?token=p9CqZzHTYn434WoDJ989Vnl_kNValWgyv3v0JjgCOFB10DUG-gRjsf0aGXDDMSFaWIRd6CNiGwth8GreUbiZA59EI9GeSTZDKVBDE0vQ-z08a3yfr2-FbBRWz2zxPBwBat2vZ4IinvzGDCHUzYyFeMyla6OnYJiDVoa1HLQiZMWJ3pLqTI0FXZbI_iJf-IpiHAjG7eKIfXaqm5mkbdObESHv32649nQn6nb0FecqH9UccKfm3migkb0qmwEVsNu2Fd155UZOae1n5QePRvkJpSLYQMpj6igx6wtSr8eFXXS6JQL3orH8ZY6tef91aKGK2XAI5nWs7kxA_bMg-x9D2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان که تو تهران با بیت المال داره اینهمه هزینه چند صد میلیون دلاری میشه برای یه خاکسپاری، بهتره این کلیپ هم ببینیم
🔴
ان‌شاالله که همه مردم راضی باشن با حقشون داره اینجوری ریخت و پاش میشه و دینی به گردن مِیت نباشه
#بیت_المال
#تبلیغ
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131531" target="_blank">📅 01:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131530">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937314ac6d.mp4?token=TGYiYkrdMaCajwSGx8AEEShhHbRQamxKCZOyMU9xmNTeFGbpZPPwkapHv_emSxyUE1TkpdFP4x5jrRt2EIWa9Bs2YuijD-mgCw_tzJ0lUTVmurI3YZqJOuMAWH2pha8-Q1QHq7aSkbaAgSvKIlSTLNFVgvcibaBlrVpbOSkhA6HXDZixhzhtuxYdqNqyeWZRomQ1spzB6SYHOZFQm44JStFhzBTo4RCv_nJvd3Jfq6WGMKyc_HbHM9FIlnecuH7buU8t5NpAmWfvSrQLfsIXgUSP84hKWthQTdbyoohxvp_CPJImv9ERxVEXG_jNDBHeEylG2R4QsbUyupWdQYyCHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937314ac6d.mp4?token=TGYiYkrdMaCajwSGx8AEEShhHbRQamxKCZOyMU9xmNTeFGbpZPPwkapHv_emSxyUE1TkpdFP4x5jrRt2EIWa9Bs2YuijD-mgCw_tzJ0lUTVmurI3YZqJOuMAWH2pha8-Q1QHq7aSkbaAgSvKIlSTLNFVgvcibaBlrVpbOSkhA6HXDZixhzhtuxYdqNqyeWZRomQ1spzB6SYHOZFQm44JStFhzBTo4RCv_nJvd3Jfq6WGMKyc_HbHM9FIlnecuH7buU8t5NpAmWfvSrQLfsIXgUSP84hKWthQTdbyoohxvp_CPJImv9ERxVEXG_jNDBHeEylG2R4QsbUyupWdQYyCHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تورمشون ۳۰۰ درصده هیچ پولی هم درنمیارن برای همین یه بخشی از پولشون رو می‌گیریم
🔴
اگه به جایی که مدنظر ماست برسیم، تأمین غذاشون فقط توسط کشاورزهای آمریکایی انجام می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131530" target="_blank">📅 01:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی: رهبران فعلی ایران منطقی‌تر هستند و ما با آنها کنار می‌آییم و این تغییر رژیم است
🔴
من به دنبال تغییر رژیم در ایران نیستم، بلکه به دنبال جلوگیری از داشتن سلاح هسته ای هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/131529" target="_blank">📅 01:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfe688da3.mp4?token=Gfcsspd52r9rc5ZpUtVdvC8U_zFysMU7aXRYXPNQuF2rajw0dCEG0Ej743oM54gbbONANatKplRX9Xr5sVlUUnkdcyvTJLmdEu0jfuxbP7QADPn2jcpqyzFPjRgeWlAOux4bFUxbUdB_zVCgcEPdkU_s31TonEjrQMRave5ayf-KwP4IfFz3MKb50mUwznkX3iJnzhyC9G7SY9BuFd_IjRABQ32MZQqZFw9K3ZrQofNHF4ddZqhx7RrD2OTM3rHTOO9-nW_qYh9zvmYZ7KFSng8DGPGw0ZiP2L8Ys8F6VkVhPK3e8J2zQdXM5h4IYpPGcUBK7pEpCiK8HJsmkfAz5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfe688da3.mp4?token=Gfcsspd52r9rc5ZpUtVdvC8U_zFysMU7aXRYXPNQuF2rajw0dCEG0Ej743oM54gbbONANatKplRX9Xr5sVlUUnkdcyvTJLmdEu0jfuxbP7QADPn2jcpqyzFPjRgeWlAOux4bFUxbUdB_zVCgcEPdkU_s31TonEjrQMRave5ayf-KwP4IfFz3MKb50mUwznkX3iJnzhyC9G7SY9BuFd_IjRABQ32MZQqZFw9K3ZrQofNHF4ddZqhx7RrD2OTM3rHTOO9-nW_qYh9zvmYZ7KFSng8DGPGw0ZiP2L8Ys8F6VkVhPK3e8J2zQdXM5h4IYpPGcUBK7pEpCiK8HJsmkfAz5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
🔴
ما شب گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/131528" target="_blank">📅 01:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673b985d42.mp4?token=kM0VqkrEAM-AaeKeOdxASA47wBqpUjNPFC62k-KkbxJGkOeEDLu50-VTRqXR6PeHlhNw0t9RueDUAkTcKdwd7_9H1TELWmPy06PVoKzOvGNUvv4naGLbMxGkAXzheCyZ9J9dcAf-Xz3DtGimxrNONmFWm2MQ16IgWYh1SNh7mfh8Tu9Dp1Gs_HGNmu3EWOpiC1Vc3AIR2jJLuDctR8UzpPIbtJgP47SbdnKMK0Z0bCIJ7JWeFRmXabsiwv4anEgYN9xDS5aPeNMd1GDEI4IHyjitY9iESaN1_KNZKsc1MeFnmSUb373NXSnmbRGBwfgTAPZS_Kx3JfUR5_xBMG9NeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673b985d42.mp4?token=kM0VqkrEAM-AaeKeOdxASA47wBqpUjNPFC62k-KkbxJGkOeEDLu50-VTRqXR6PeHlhNw0t9RueDUAkTcKdwd7_9H1TELWmPy06PVoKzOvGNUvv4naGLbMxGkAXzheCyZ9J9dcAf-Xz3DtGimxrNONmFWm2MQ16IgWYh1SNh7mfh8Tu9Dp1Gs_HGNmu3EWOpiC1Vc3AIR2jJLuDctR8UzpPIbtJgP47SbdnKMK0Z0bCIJ7JWeFRmXabsiwv4anEgYN9xDS5aPeNMd1GDEI4IHyjitY9iESaN1_KNZKsc1MeFnmSUb373NXSnmbRGBwfgTAPZS_Kx3JfUR5_xBMG9NeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/131527" target="_blank">📅 01:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131526">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی گفت:
ایران در طول 47 سال گذشته، با بهره‌برداری از ضعف روسای جمهور سابق، زورگویی و ظلم در خاورمیانه و علیه ما انجام داده است.
🔴
اوباما 1.7 میلیارد دلار به ایران به صورت نقدی تحویل داد تا از آن برای توسعه سلاح‌ها و موشک‌هایش استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/131526" target="_blank">📅 01:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131525">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی گفت:
رویارویی با ایران به خودی خود یک جنگ نیست، بلکه یک عملیات برای خلع سلاح هسته‌ای است.
🔴
به هیچ وجه نباید اجازه داد که ایران سلاح هسته‌ای داشته باشد و من از حدود 4 ماه پیش، تلاش‌های خودم را برای خلع سلاح این کشور آغاز کرده‌ام.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/131525" target="_blank">📅 01:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131524">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌ان: ایران تقریباً با هر آنچه می‌خواستیم موافقت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/131524" target="_blank">📅 01:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131523">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQOQnTDm2tovS_mS_h_8ZU7qcSmcrVD1PrGMTIDMBXbKUYZj2AkCn1gz8ktGRTft9uRgArcsUm-pQhtnxTl4sY5R8BPfV7WmEE6sZoqXZKSjv_Xo2sXpXJfO0MPWRjXmyd7I1WCIx2wskiTZAF26p2zPp3sF1BYdtPrPqkwHxLCP3ePHsS0w3uEYIGf07Th4DwL8oaU0jnvODg9Tn8nKX_MDKosBbQE2z2nc5AxfEBuHEVm-5al6Xi2mFDdjirNg4Q81C46cxXm1IpN-h5mfyEKYQh1otEjUZ0_2XUmLFyaX-1KITGmo4AtAkVioL79Gnyws6tF7riDwG9IA7GR9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی، شهردار تهران: ۲۵ میلیارد دلار پول نقد دست مردمه و میتونه در اداره کشور استفاده بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/131523" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131522">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131522" target="_blank">📅 00:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131521">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بچه‌ها
الو اسپورت
و
الو توئیت
هم دنبال کنید
@AloSport
🔵
@AloTweet
🔵</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/131521" target="_blank">📅 00:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131520">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f6f491fa.mp4?token=I9KczZkC0MehxEWgGLre0al56PysCWcu-4QfX3MOeDMfnYMN6jFFHUr4gZ9L9cSx9-DEF360p_LNL-q1-QitcLWr8hfTQ1kOVnfAAfl9whjT1BRIIm5578qbcvaZWSKgbhE2oj2uTR7me90QuYuHd0jVahdZWkvImAIZBwSb7rZoy8ohYiNgdNgw7FmNJbG_tGSr9dFydQmUebhjm2aU2srGesgmStx8ewiuCpQwlepWZiaUqCCzVosVRmDlxAz7T-5aMI9txrY_lVLQ1aLDfc3tsrCeASiUOv3bnbsuXkWkrviwOP1LUn-m3I-qSpBjMtEjFAn6P_yxFxkVKvjAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f6f491fa.mp4?token=I9KczZkC0MehxEWgGLre0al56PysCWcu-4QfX3MOeDMfnYMN6jFFHUr4gZ9L9cSx9-DEF360p_LNL-q1-QitcLWr8hfTQ1kOVnfAAfl9whjT1BRIIm5578qbcvaZWSKgbhE2oj2uTR7me90QuYuHd0jVahdZWkvImAIZBwSb7rZoy8ohYiNgdNgw7FmNJbG_tGSr9dFydQmUebhjm2aU2srGesgmStx8ewiuCpQwlepWZiaUqCCzVosVRmDlxAz7T-5aMI9txrY_lVLQ1aLDfc3tsrCeASiUOv3bnbsuXkWkrviwOP1LUn-m3I-qSpBjMtEjFAn6P_yxFxkVKvjAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه 14 اسرائیل ادعا کرده که قراره به زودی یه گزارش کامل از صحبت‌های دونفر از جاسوس‌های موساد تو سپاه پاسداران منتشر کنه که این فعلا تیزرشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/131520" target="_blank">📅 00:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
هشدار سطح نارنجی گردوغبار در تهران از پنجشنبه تا جمعه (۱۱ و ۱۲ تیر)؛ کیفیت هوا کاهش می‌یابد. سازمان محیط‌زیست به گروه‌های حساس (کودکان، سالمندان، بیماران) توصیه کرد از تردد غیرضروری خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131519" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
هلند ۴۸۰ قربانی جان باخته دیگر به دلیل گرمای شدید ۳۵.۴۰ درجه ثبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131518" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131517">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoc526SM-D9xMZKO2rVbR4y1k3fXkmvn021TB3vuMSjc1o4pHL4TRsahYxhENCydHDoFO7pZcWrYg4940g5x1Ae-6asb1LS-5ZjcsYLn4eAIfQKygWt8aWAqgO-LXsc1ns4I__hM8LdNuie7wV4ozeN9bu5RErOuu9mTZiX4WjoP_cg4fTgF7vorRqIjqGq3W4gdVe3wPxFD3oNHXp-b9AHbUHKWEdyt7jmupBvdKGVLAuWGdHFdWBa8_Waft47TZiZSrS2o3-QomLSYg2CR4rJKQ0ufdHS3YQthcpOnhIQzFlI6aRAybx6LII_Y3CMjHNRrW4T7xvsW6MJ-mYuq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ:  ۵۸ میلیون بشکه نفت و میعانات ایران روی آب انباشته شده و ۹۰٪ این محموله‌ها مشتری یا مقصد نهایی ندارند.
🔴
با وجود تعلیق ۶۰ روزه تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خریدها محدود مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131517" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131516">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خلاصه هرکی بیت المال و حق مردم رو حیف و میل کنه در دنیا و آخرت ذره‌ای آسودگی نداشته باشه
👍</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/131516" target="_blank">📅 23:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131515">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یادمه تو کرمانشاه که زلزله اومد مردم برا گرفتن یه چادر و یه بطری آب پدرشون دراومد و آخرم‌نگرفتن
الان برای یه تشییع جنازه(تبلیغ) صدها هزار چادر و .... به خط شده</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/131515" target="_blank">📅 23:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131514">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چه پولایی داره خرج میشه برای یه خاکسپاری</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/131514" target="_blank">📅 23:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131513">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/131513" target="_blank">📅 23:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131512">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLCUriPtOqhufKS81HMT9YmN16x6EZJb300qrju7rlOkWxUmD17W3Ujmkndda9q0xl4rx1Q3oLjXTxrOkTvW_4ypeJkLeoVTkXDFsLCu3PnMvvHDYkVL9TO3LBEdvvSBCCt8DnTRRv3wuAS2VxVlpJgHb7mEqpUG2xoWkBSaUw3usukjvrSPbAAPINxjKEXaTlvEts1nFfhn_l6BaTA6cilk5Rfv128fiIDZrOX4z2WzWzGcPhBm7Zj0Wc42obfYPhTKW-NOAzkWi32EZEqeDZ3YkOwAKqOYT1EWn_EC4DeVfm132cvV79tVnUS5CKbD5Ne_mAXjMUAKSsPa9epplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده تو تجمعات شبانه : وای برما؛
تو تاریخ اولین ملتی هستیم که خون پیشوای خودمون رو به گندم و ذرت فروختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131512" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131511">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
العربیه: فرانسه، ایتالیا و آمریکا ائتلاف نظامی‌جدید در جنوب لبنان تشکیل می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131511" target="_blank">📅 22:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131510">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سفارت اتریش در تهران فعالیت خود را از سر گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131510" target="_blank">📅 22:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131509" target="_blank">📅 22:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131508">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: مذاکرات با ایران ادامه دارد؛ ویتکاف و کوشنر جلسات سازنده‌ای در قطر برگزار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131508" target="_blank">📅 22:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131507">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l87EQHL5vgIc3KIevkr2Ltj2JDBkadi1VsVx999lDrWYYsJOq1XUaXUCq8_eXp7f3WLU2g94h0z50TJXtMSd7-4oauS-LloR4ZUXtsgKZxLCvBDKDPoR76c6d2rAt2RqNrqxXmJfnD7Gy538h7lzN9DYRpjpL-Ur7pGZs29yS0pfGNtaxzfzDkESG2Y_6PcqBj_EdCWS0RBZ7bMx48MLm9fSI-VplePNF3o9YIIhjYpT4gfKHz6-pIUOO1hG0T_xG20wDpseUE0gRUpZ_fIPvqSewyo-5tTgpaVaRU4JGuN5isFg6li4x0k6GxV0VQJudBAMPMBlK1j0znL-v8VGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی در واکنش به جلسه فرماندهان منطقه با فرمانده سنتکام: فرماندهی مرکزی ایالات متحده (سنتکام) امنیت را به منطقه ما آورده است یا ناامنی را؟ پاسخ کاملاً واضح است.
🔴
همچنین، نیروهای مسلح قدرتمند ما ثابت کرده‌اند که حتی خود بیگانگان نیز نمی‌توانند از خود محافظت کنند.
🔴
صلح در منطقه ما تنها زمانی می‌تواند پایدار باشد که جامع و فراگیر باشد و هیچ دخالت خارجی در آن وجود نداشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131507" target="_blank">📅 22:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131506">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه، فیدان: اسرائیل در حال حاضر به دنبال یک دشمن جدید است.
🔴
تا زمانی که اسرائیل - یا هر بازیگر دیگری - به گونه‌ای عمل کند که با منافع ملی و منطقه‌ای ما در تضاد باشد، هیچ دلیلی برای ترسیدن از کسی، تردید کردن یا عقب‌نشینی نداریم.
🔴
ما مشکلی با رویارویی نداریم. اگر به آنجا برسیم، برای ما مسئله‌ای نیست.
🔴
اسرائیل فقط مشکل من نیست؛ مشکل جهان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131506" target="_blank">📅 22:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131505">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزارت خارجه فرانسه به «العربیه»: با بریتانیا و شرکای منطقه‌‌ای‌مان برای بازگشایی تنگه هرمز تلاش می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/131505" target="_blank">📅 22:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131504">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صدراعظم آلمان: ایران فورا باید با اروپا وارد مذاکره بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131504" target="_blank">📅 22:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131503">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHCWUXQX7IYvfFCwNb6d4IZ0kMpo99MRxntVX_EboPyH5c1SiB9e5pQFzrEB-r5V1K79Z4AhVAkb1zjdC8uKpT6LcSxJ-EPa0Bv0UbxIjsvKqxu5tlA1090GqPQdnizCx2cU_KLWXAevWUikY5IxPz4iypVZbL9ur2_pm9wIiZsGayqq7PKTeHWkYYojniGtQJg_4pP7mMLnS4kOt72YAQdHK426BigTLfH9MnGPDqthhFXXiAOcBWgXHxSVnWh8eGZgAe21a-DnRLYT6N-EyuEpYX86liH-ytLAKyCib4aF-xqw3ifcmAccTnsqdKUyWaW7XPUCLDXXjFFwv-6NxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم پناه: آماده شهادتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131503" target="_blank">📅 22:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر خارجه ترکیه، فیدان: هم رئیس‌جمهور اردوغان و هم رئیس‌جمهور ترامپ تعهد قوی برای لغو تحریم‌های کاتسا دارند.
🔴
در سپتامبر گذشته، این دو رهبر به‌طور عمومی مواضع خود را در این مورد بیان کردند و ما به عنوان وزرا دستور داریم که این مسئله را حل و فصل کنیم.
🔴
من معتقدم که لغو ممنوعیت فروش F-35 به ترکیه پس از لغو تحریم‌های CAATSA رخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131502" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131501">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
به نوشته فایننشال‌تایمز، کشورهای اروپایی که اجازه استفاده از پایگاه‌های آمریکایی در کشورشان را برای حمله به ایران ندادند، ممکن است در همکاری‌های نظامی آینده میان آمریکا و اروپا با محدودیت‌هایی مواجه شوند.
🔴
فرستادهٔ دونالد ترامپ در ناتو گفت آن دسته از کشورهای اروپایی که بودجه نظامی بیشتری داشته باشند، امتیازات بیشتری از آمریکا دریافت خواهند کرد و آن‌هایی که دسترسی نظامی آمریکا به پایگاه‌هایشان را مسدود کرده‌اند، باید منتظر مذاکرات دشوار باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131501" target="_blank">📅 22:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131500">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
روسیه: اجرای کامل تفاهم‌های حاصل شده میان ایران و آمریکا، ضروری است
🔴
در پایان هفته گذشته شاهد تبادل حملات شدیدی بودیم که می‌توانست تلاش‌های دیپلماتیک در حال انجام را تهدید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131500" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131499">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل: در بحبوحه مذاکرات دیپلماتیک، ایالات متحده همراه با اسرائیل دوبار به دیپلماسی خیانت کردند و در نقض آشکار منشور سازمان ملل متحد و قوانین بین‌المللی، دو جنگ تجاوزکارانه را علیه ایران به راه انداختند.
🔴
این تجاوزات تهدیدی جدی علیه صلح و امنیت بین‌المللی به شمار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131499" target="_blank">📅 21:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131498">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpslLVzT2SUhu3PCUz1rv1eG2gdYnfZOPy2aQUKtFFom-aRojfBasA2YUJoeX255gSK5SWgPmmOUo9xwH0iNlA1szaIztWIiZwO5hQ9v6QTE8jEjIhIuZxh79i31VEu6--BjM8A1cAiCscEsewD6HfkuU86m4wjrXX3VFozn-0M_bFNCOxvSgB60rxkG0pJVDXUq0h6gzBfuom_6xlNHEs305wZ5sHUttyDC9i-offD-zDkOXOqLcdlqbbrunf0lptsynpAjpZ4dZ657jQpiNgeSxXPBa7JEsVB-YNKFoB29bkLsMa1j0kMtWNWLzhiQi6anMUpofla9YTc_9ipSTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روسیه توهین به پیامبر و قرآن را ممنوع کرد.
🔴
این قانون با دستور پوتین تصویب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131498" target="_blank">📅 21:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131497">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hspQKAYOFFBJn8eNzkhgtN4Qx5B20P4aIt05Zp3-abU1m-xz6xEiJQAhbfXTtzU7tew6wZ7zZ0Cjr3l7SNMl3Y2K_yPDYZfy9-_0E6TRKo_hG39H4XR-Vu87D_vaQlLSCtrokMZQ66akRbpoVQyTNrWZYDiwzB_lMmr8U9Ow1pBKNQ6Ef6zCU-7oW6N0RquuIiFK4U6dKN2AgZqx9AWceNCY-Q0kk6CT8Dv0-A-bDh_vW-t4s2qkx5iJvotut6YMZ1ADgu-_Z8WabDG9Zm-fcTvmvXUw5HWhndDO3FJGfI9GytdcdduAJhjnm6ySYqA5DtxImCYtBXlZ1GwkaJquag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه حزب دموکرات کردستان با انتشار تصویری به نقل از مصطفی هجری سرکرده این حزب اعلام کرد: در شرایط مساعد تا ارومیه پیشروی خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131497" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131496">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeLSweZj5R7r55eMLJvG8ZCa7zQ2K_5ba4UnC0w2OQEwtZxr5gHVbIOZMeDm7gsYoUz2iABVDSUP245yjCxerBYh6qt7sbOfgioj2kkUyDs475SakrVfvojUzJ4F2WZWmZBZ3BOBbcUF4y9y_r-paOrWdaIa6O_foZvK9oWi34RzFVOVsOwXQxd5O-sKKVivTSzso6DTfK2rgaE9Q0ETMQsP4741m6wYX4gUFHEuzYVsA671Q5VXhYiQhh0txWHaiAirniXTTa9XnaTqQT0RM5qHE79TAZz6Dp-vul-WN1ribBaMFdahbfax1o1lS9E7k7wrWkf1Hc8u2gqALPgP-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
بیرون بروید و در انتخابات میانه‌دوره جمهوری‌خواه رای دهید، زیرا اگر کمونیست‌ها وارد شوند، دیگر هرگز ماهیگیری نخواهید کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/131496" target="_blank">📅 21:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131495">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e3603b94.mp4?token=cryPGCEu44xWUDZSlKtriCI7YH7pZR3N5fc66G2TVr38PYGp74W3VVBOgNKHHx_emUyat8miYndPkfbvg-JEo2aBfuy8K1tOb4FushBr6mrUW5ZMBKtOxUIQ1u1UVJRB_9S1-MXscZxlBVMe8vIHgS_fQrFvRU9l3ewg4QLXzx7MJonIqNsguCZTC1Y1n2aGEHRcugsPfNO1oydUn8mBeke7UkSxQXt6DeGDV7ff6mcHQ6F9U9Wu3-wv-V56tTMSNbVj5n6L2t3FSALGJ4ae6Zz5Sdg8BIwS6tk7IXNoukKaBN68FPSz_rc1aMApbLn2c_88tvaoMsBGMq9BXn2iqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e3603b94.mp4?token=cryPGCEu44xWUDZSlKtriCI7YH7pZR3N5fc66G2TVr38PYGp74W3VVBOgNKHHx_emUyat8miYndPkfbvg-JEo2aBfuy8K1tOb4FushBr6mrUW5ZMBKtOxUIQ1u1UVJRB_9S1-MXscZxlBVMe8vIHgS_fQrFvRU9l3ewg4QLXzx7MJonIqNsguCZTC1Y1n2aGEHRcugsPfNO1oydUn8mBeke7UkSxQXt6DeGDV7ff6mcHQ6F9U9Wu3-wv-V56tTMSNbVj5n6L2t3FSALGJ4ae6Zz5Sdg8BIwS6tk7IXNoukKaBN68FPSz_rc1aMApbLn2c_88tvaoMsBGMq9BXn2iqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که موسسه کپلر از تردد در تنگه هرمز در ۲۹ و ۳۰ ژوئن تهیه کرده است. همان‌گونه که می‌بینید تردد در هر دو مسیر ایرانی و عمانی همچنان ادامه دارد.
🔴
این نکته هم قابل ذکر است که ترددهای ثبت شده توسط کپلر شامل ترددهای با AIS روشن می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131495" target="_blank">📅 21:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131494">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/وزیر دفاع اسرائیل: ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131494" target="_blank">📅 21:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131493">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در بندر امام
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131493" target="_blank">📅 21:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
زلنسکی: اگر شرکای ما آنچه را که وعده داده بودند، به موقع تحویل می‌دادند، امروز می‌توانستیم خانه‌ها و جان‌ها را نجات دهیم. این یک مشکل بزرگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131492" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا: مهلت ۶۰ روزه برای مذاکرات بر سر توافق نهایی میان ایران و ایالات متحده باید به دلیل تبادل آتش از ابتدا محاسبه شود.
🔴
احتمالا جزئیات مربوط به جدول زمانی مذاکرات به‌زودی منتشر خواهد شد و کنگره آمریکا نیز تحولات را از نزدیک دنبال می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131491" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131490">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb66XIFy4-eW_3iQzfuv5FZg6cgA8pRmStZju5oENmDVS5f4DneVLvQ6dy6EcaQq9lA0iUUvsA8u5syvIMHfIwAI3iObH_dbaiT2iZGA1XJdnWIM43iBk2Es9pcK6Mi62Spq1Sh1XfcHUzTthXVTh-K24XQzYIPDUVWt8yZ1XDEG61esG-6Dgvh0EsKGrEOYBZDJXxupQej8E2KLXmdK1cVVRpSD696uUxJUTg_MDw3TLTaJfBJ26fnexAw7IcbZmwNrQcbqXX1M-dK-Jqrg62WPZKPsHgXt0fpb8Sq4Fkd95RtBchZ3fY8NFAgBgIrdKblgCdUcYlJrjTe7tK8zhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری:قالیباف مجلس رو باز کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/131490" target="_blank">📅 20:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یه بشقاب پرنده داخل فلایت رادار تو آسمون آمریکا ظاهر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131489" target="_blank">📅 20:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قائم پناه، معاون پزشکیان: قرار باشه هرچی رهبر بگه رو اجرا کنیم که باید در تمام نهادها رو ببندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131488" target="_blank">📅 20:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131487">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erwQI0_Ai4OJicst3gk1m5WbfJzzKK-jA0AI802jUJvHS4U4wgCANYpT5Q-Z3ocM5D63Yg0xP4rquFEAMITlleqicxsRugwQuOXK1_wVHHDux0aY1z8kBtwx85gfWPBP8rrDXehhMwa6WyheBi_zKuJyTz1wKJjBHsssJ-hAAX5Yp8bJD2s_ZhXVJ6MQXxYo_8UCrkn4B3WoKi_CNPJBFiZX2dLOdj6JCxgV2Dp5u22qC9vQTD4Gk4uIYGahqdb1tSY78zfiXTEoonnCvWyJ4LdwbdeVJsrL7IybOl_PTfmU4H3vHPa7-fQm0afgw5w_1WPD-wEno8P9yw6PbAvPdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه بشقاب پرنده داخل فلایت رادار تو آسمون آمریکا ظاهر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131487" target="_blank">📅 20:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU84HPNthcxxsZ0J124CJZLvihV01y2RwIGeMChYuNQ667ui5BV3LXEQzsEGAQ2f-xAKnfl8W5RUjMehBIhGjatWgRv1iMjJ051F4zCg_txT8oATneCO78SkNGBysQBfNtTHt8MT4RUEeIuf2g3Ve8PkddgwMIGCtPZIwf-kQxs4izrXwTpk4Fe9tckVbFdtnNhzFMRlCw3JAY4J546rnoQ6mc7KsQZ4LBUdrz71DWOtJPnnh76chrcRa2UB68KWXMeBO8I9NemNzY8jgx2egW7KmdN_Fq7SRK1SAZcx8neg5ZNgUshXk6OMIIt5gkXKnFGsx1YPo0JIBdvUCiQIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار بزرگی در اطراف منطقهٔ کونین الطیری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131485" target="_blank">📅 20:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317cc5baf7.mp4?token=rcCf3FmQwFCM6vEl4Goketr5ACOILr9Fh6a8q2ZsiGu4W-7hRbjnRYIXcXC_m_uouaf_m8TpqkrduVrgvO0YBGHeMsAKt_5241RrNBywSR_jmuIJBPCy4GhcGsgQzUiVDr14YYm6Cm0aSySdJ5yPWWxf_nsHuy_NhSO705VQg6eoNHS2y5-fo2XLWt4An7JyylX-6gbZjn0G-fxacL9rBAXu778O2B4jAzvib3WLjySD_KrMT07TZMeOe0YU7betiG_A4vfDTk1Jf8j_loFMcxaQgEe-Bj64mmq3i4fWoqhYcGv0sIcIiMhMW4HHt_7tQhDNdX-ffHCjRFGwkxbAf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317cc5baf7.mp4?token=rcCf3FmQwFCM6vEl4Goketr5ACOILr9Fh6a8q2ZsiGu4W-7hRbjnRYIXcXC_m_uouaf_m8TpqkrduVrgvO0YBGHeMsAKt_5241RrNBywSR_jmuIJBPCy4GhcGsgQzUiVDr14YYm6Cm0aSySdJ5yPWWxf_nsHuy_NhSO705VQg6eoNHS2y5-fo2XLWt4An7JyylX-6gbZjn0G-fxacL9rBAXu778O2B4jAzvib3WLjySD_KrMT07TZMeOe0YU7betiG_A4vfDTk1Jf8j_loFMcxaQgEe-Bj64mmq3i4fWoqhYcGv0sIcIiMhMW4HHt_7tQhDNdX-ffHCjRFGwkxbAf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیم های جستجو و نجات کاستاریکا مجبور شدند صبح امروز جستجوی ساختمان در پلایا گرانده را پس از نگرانی از اینکه سازه در معرض خطر ریزش قریب الوقوع است، رها کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131484" target="_blank">📅 20:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پزشکیان: نمی‌توانم ببینم مردم مشکل دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131483" target="_blank">📅 20:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پزشکیان: دغدغه ما مردم و نیروهای مسلح هستند.
🔴
من هر کمکی لازم باشد به نیروهای مسلح می کنم.
🔴
جنگ بود، ماه رمضان بود، عید بود آیا کسی  احساس  کمبود [کالا] در کشور داشت؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131482" target="_blank">📅 20:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پزشکیان :  در مورد مذاکره رهبری فرمودند اگر سه چهارم [شورایعالی امنیت ملی]  رای دادند مذاکره کنند.
🔴
از ۱۳ نفر، ۱۲ نفر رای دادند.
🔴
نه تنها رای دادند بلکه دفاع کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131481" target="_blank">📅 20:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=bQfH2neAwxT6G2tDcZLcYaUzFlbZZoJN9cGfJZUdc0SKNwSXD5FX_pLl5gpfYRpSDdOOfB_ogtAqKD2bvDcIP5qpCLxbSzVBcgyCgZfl7FD7Iq_jNq00eJ8kkbdKHt-Nk4t8huyDR-6VjqUwXxcHa5PcuZeffKXwKPXg9h9KlwjbYaaUm1Ji9r9ulV2LG0-x-zmuqY_oQ82u_WGjLh1YnR-pSce48p_PtIJesRPRmNsluAgqBjBjJhDu4ZVWmZ5IdbCFGMU8lC8zSZ8l8DoHWcYjqoFGNITPefAeb5K3-SmPT_xuCmt10dlJLKQoJ36bUmQEFmdLtsG1sK2Ft7LdRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=bQfH2neAwxT6G2tDcZLcYaUzFlbZZoJN9cGfJZUdc0SKNwSXD5FX_pLl5gpfYRpSDdOOfB_ogtAqKD2bvDcIP5qpCLxbSzVBcgyCgZfl7FD7Iq_jNq00eJ8kkbdKHt-Nk4t8huyDR-6VjqUwXxcHa5PcuZeffKXwKPXg9h9KlwjbYaaUm1Ji9r9ulV2LG0-x-zmuqY_oQ82u_WGjLh1YnR-pSce48p_PtIJesRPRmNsluAgqBjBjJhDu4ZVWmZ5IdbCFGMU8lC8zSZ8l8DoHWcYjqoFGNITPefAeb5K3-SmPT_xuCmt10dlJLKQoJ36bUmQEFmdLtsG1sK2Ft7LdRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور
پزشکیان
:
من به عنوان مسوول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
🔴
من نمی توانم دروغ بگویم
🔴
این نیست که ما مقابل دشمن کوتاه خواهیم آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131480" target="_blank">📅 20:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نماینده پاناما: از ایران می‌خواهیم به قانون بین‌المللی پایبند شده و تهدیدات خود را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131479" target="_blank">📅 20:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یک عضو ارشد حزب الله لبنان گفت که مقامات لبنانی باید از سازش و خدمت به پروژه صهیونیستی در لبنان دست بردارند و فرصت ایجاد شده توسط ایران در مذاکره با آمریکا را غنیمت بدانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131478" target="_blank">📅 20:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26179bf871.mp4?token=MP38KI6YiRNYFEVbs5ELrsHqKbCdj6eSU9jVdRLIceCTXlHAYABKEdRN_sNpgGG1sAEKYW__2YWbqvw4xIJVH0E7xWdqTliLpa_aEDBp2oItWcoDIP5lv4s6Wthrwp5S541gy8Gay96-hwIK7I7krPGc79oJu2mTJAYJY4u8VKkM2ynk4U7lUPjKgXRcAnZ3QwMBo7HCOZQNpbCwTkCljJoX2oF2lUTpxtSnEpqdKGzpP49Uh-QHkEBwVe8oe-2q0rJfrpR8c5rtYP4aialXec3nhhiPsBROnYnADi3yJ5uC5dh3qUCIHLQD73Smk_UHIy6SwWA0uqWxUpDuq0wEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26179bf871.mp4?token=MP38KI6YiRNYFEVbs5ELrsHqKbCdj6eSU9jVdRLIceCTXlHAYABKEdRN_sNpgGG1sAEKYW__2YWbqvw4xIJVH0E7xWdqTliLpa_aEDBp2oItWcoDIP5lv4s6Wthrwp5S541gy8Gay96-hwIK7I7krPGc79oJu2mTJAYJY4u8VKkM2ynk4U7lUPjKgXRcAnZ3QwMBo7HCOZQNpbCwTkCljJoX2oF2lUTpxtSnEpqdKGzpP49Uh-QHkEBwVe8oe-2q0rJfrpR8c5rtYP4aialXec3nhhiPsBROnYnADi3yJ5uC5dh3qUCIHLQD73Smk_UHIy6SwWA0uqWxUpDuq0wEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم فرانسوی‌ها برای تهیه پنکه و دستگاه‌های تهویه
🔴
مردم فرانسه به دلیل گرمای شدید برای خرید پنکه و دستگاه‌های تهویه مطبوع به فروشگاه‌ها هجوم بردند. فروشگاه لیدل پاریس به میدان نبردی بر سر پنکه و دستگاه‌های تهویه مطبوع تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131477" target="_blank">📅 20:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وال استریت ژورنال:  ایالات متحده به ایران پیشنهاد کرده است که در ازای باز شدن کامل تنگه هرمز، بدون دریافت حق بیمه، وجوه مسدود شده را آزاد کند. در حال حاضر، ایران به این پیشنهاد پاسخ منفی داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131476" target="_blank">📅 20:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K59yhr8M7kuRnDl-XkUG1H_oy3Eb3y_lElDTRJAfptkhZtX0HQZmxAFAjZNupXgufJ7rMUc5a6u040GL2GeN1Glmlmy2tR3iXdZorcfVO2VHOidcRaIqlNZcHEZQUuTJDCw4Vei-HquCtiCnrMoEzrO0NMH21wi_rRHWDaOjJNefoRLET75vcNbTvEp99Oa-BiO1ilIIfKIR5jufSOON4ievkTLU_-Q68uVmsvJoEiUC4yHNL_HpiTVcAZ6y2675uZNChP-srMvvOowsl0kraESYiZW-vS1CLtIU3k7tbvsWwImwwzGEeVrmcKiIY2Y4t9hlnYXOWFKq6pawi25PTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روز گذشته ۳۸ کشتی از تنگه هرمز عبور کردند که از این تعداد دست‌کم ۷ کشتی در مسیر ایران و ۱۶ کشتی در مسیر عمان ثبت شده‌اند
🔴
۷ کشتی که از مسیر ایران عبور کردند ۶ تا ایرانی و یکی عراقی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131475" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5HHen-qKyxNfq29FRVGY3fmCQI90UrIXakAvtXeh-4ofqvTsLGXp1_RNXBrVfHDA1HI_aQbyL6AuXTxDiFvzGnsDwUOMVNqvQj0bbx3D6ii-iFhl7YDLWz1LGhwVnhQ2lXddjv_HfjWsccjM3RWTwolt67sShJi9XNRfqgZ5M3mSnJ2W2kh7TlN1kSneGKjoJo3IxHqXga0doL0j9Fj9FB75oM9fFO1dOndP7HCtRUSDNjZW3YfdU42SQJTfl5MZ8m3b4QUB5fqQOvZ8c1PfZ6dXI7HiEHWTc66UZxBGX1-PpDYOObzbxJ5H7yspyNCuLHiyQLkRZqZ7h-VgXVj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس:  ویتکاف و کوشنر تلاش کرده‌اند تا به ایرانی‌ها بفهمانند که درخواست آنها برای عوارض می‌تواند توافق ایالات متحده و ایران را که در نهایت برای ایران بسیار سودآورتر خواهد بود، از بین ببرد.
🔴
یک مقام آمریکایی گفت: «پیام ایالات متحده به ایران این بود که «بزرگتر فکر کن».
🔴
این مقام ادعا کرد مبالغی که ایران می‌تواند از توسعه و فروش آزاد نفت و سایر منابع - در صورت لغو تمام تحریم‌ها توسط ایالات متحده تحت یک توافق - به دست آورد، «برای آنها ۱۰۰ برابر ارزشمندتر از استفاده از یک تاکتیک گانگستری برای تلاش برای دریافت عوارض خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131474" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نماینده پاکستان در شورای امنیت: نمایندگان آمریکا و ایران، بر سر برگزاری دیدارهایی در آینده نزدیک توافق کردند
🔴
بر روی تداوم گفت‌وگوها میان تهران و واشنگتن، کار می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131473" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
یک منبع به العربیه: آمریکا تأکید کرده است که هرگونه تشدید در هرمز پیامدهای مستقیمی خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131472" target="_blank">📅 19:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzDAHSnK48pK0HQXjBG1afVgCYh6n0f6xVIRyezfNwvk0bX0eIVb7Ocqgi9nxXLPVcp3IiNrObn5hDitarQG8Q-Z75MVsw6XlfkRRfvBbzFs7hUo6-vm3v4qfDyGY6zQ7KStJGc-ZZeFNL1HWSUTadBagCrkgNQhEwGBiyhPEuY6NIaw9pa6jAtrWPmXdWeX5d6vysKkdMWetPKkYHrCgGWE_egVsgQ_SESsP9aKi_Wfu15m-oP2zkwBXxE-MISRO-ncCE8Lrl7EafKN9_riu4FyMW1A_aAHsDb8VjY-7qqwWdoCNY2XKl8MmpgC4yK_Y9KSG8-i5aE45I0uGfcNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت نبویان بعد از اینکه ..... کشیده شد
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131470" target="_blank">📅 19:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131467">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ولی نصر، مشاور سابق اوباما: پیام‌های متناقض و راهبرد‌های سرگردان ترامپ، باعث بی‌اعتمادی‌ای شده که ایران را به حرکت محتاطانه‌تر وا می‌دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131467" target="_blank">📅 19:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131466">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سازمان هواپیمایی: پروازهای داخلی و خارجی شنبه و یکشنبه برقرار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131466" target="_blank">📅 19:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131465">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
خبرگزاری بلومبرگ گزارش داد که چندین کشور اروپایی با تغییر رویکرد خود، موافقت کرده‌اند که کشتی‌های تجاری آن‌ها برای تردد از تنگه هرمز، عوارض تعیین‌شده را به ایران و عمان پرداخت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131465" target="_blank">📅 19:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IW4EqYThRv_-mcJPwkbABHCBQXom_W7FgJz-MiGEqUWGABNBTFy05Z-V5YfeWLp-7dVTEzNzya1ItsP8uzvNLoI9pf66GF4_3ZwOX8fnRx0MkOy1J_uBvvHxvfhaVj3fgbdwFLlzRag9ss_KivAu-bjhOOx9Thl0TV5hGri6lVxdUjFQX5QGWn-MESOz_TgcOdDXA4bAOE3hvdDghPObseMX0KRq4DdLwzuQ0gN-ZwjjVdDsI5K9FnvmKchka2vqX-QsMp4fNG5IVBpJmtGxq4ooT1lJDckeLhewdMdKXjrz76yDDAB9eP19EW57xcOLCVtAY7pmm9RIg8r7sf53CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5ee2x5BgNWWQwMB2NlZegP1YV07iWDKlX7V5DH8KwT4NmQj30Xkx5LDWbXHervZIuDcQTAnItMbgUA6UKOYN2sGC6FHG9F1BjdSS3au3YYSlgik6tF9JxRkUYxrq7H2wdouzFv0s0qBZwuHwuqUuujvmV2tAmL3CF_YnaM1wwXOrNPN5NaC1T8bkpRF4ZwS1d-M30xZMaP1lG5o7bmjx0tSN_BBACCwJ0Bo5bEmeYHMt8q-aWfeTtIT3C509F9IkTMREf7eCdejOxWyf2_gSGbPfXupLySDCY1DHymF-fBi_GEnh0qhRlTkpEftvfqMJNTNeoRcqcu_-Y-QQp8Y7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت بهداشت سوریه می‌گوید که تعداد کشته‌های ناشی از انفجار در کافه در مرکز دمشق به ۶ نفر رسیده است و ۲۲ نفر دیگر زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131463" target="_blank">📅 18:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: ناتو برای آمریکا بی‌سود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131462" target="_blank">📅 18:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین زلنسکی گفت که احتمالاً در حاشیه اجلاس ناتو هفته آینده در آنکارا، ترکیه با  ترامپ دیدار خواهد کرد و افزود که در حال حاضر آماده‌سازی‌های این دیدار در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131461" target="_blank">📅 18:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
خبرگزاری بلومبرگ گزارش داد که چندین کشور اروپایی با تغییر رویکرد خود، موافقت کرده‌اند که کشتی‌های تجاری آن‌ها برای تردد از تنگه هرمز، عوارض تعیین‌شده را به ایران و عمان پرداخت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131460" target="_blank">📅 18:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb04c879e.mp4?token=Wuw2n2u46G66eXSXLQ6sVfbTwLA6iqfg5k3_gwJL-KJKVNZcR213XWfMG4Mp0zjd83KNkkdmpKFZ3RAxEqaAIIw9KSTotVQL-C-jp6PO_gx7qTKkih9SJW9Z6DwLmZp9zI0W8ECcC-975OkhtiIfYIBwIbpiUnGVkAD--jIvIlozExWc3Zb4VxK865tij2DW4ZwrCAxMH1EwTeoOc6Mkd5ZDE0IptgIrgs00qhXvpNLc2_wr450TVjoUEaY8e5dJsX_EpB2t94a_RuJSNxbBFGKgKDG9X_g1pZpaEymztM_mMOqC0lcq5429Gq6My9doHC2CBwqpMhbg62E0gDq_hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb04c879e.mp4?token=Wuw2n2u46G66eXSXLQ6sVfbTwLA6iqfg5k3_gwJL-KJKVNZcR213XWfMG4Mp0zjd83KNkkdmpKFZ3RAxEqaAIIw9KSTotVQL-C-jp6PO_gx7qTKkih9SJW9Z6DwLmZp9zI0W8ECcC-975OkhtiIfYIBwIbpiUnGVkAD--jIvIlozExWc3Zb4VxK865tij2DW4ZwrCAxMH1EwTeoOc6Mkd5ZDE0IptgIrgs00qhXvpNLc2_wr450TVjoUEaY8e5dJsX_EpB2t94a_RuJSNxbBFGKgKDG9X_g1pZpaEymztM_mMOqC0lcq5429Gq6My9doHC2CBwqpMhbg62E0gDq_hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: ما آماده‌ایم، ما آماده دیدار هستیم. پوتین از دیدار با من به صورت فیزیکی می‌ترسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131459" target="_blank">📅 18:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بقائی: برگزاری نشست امنیتی با کشورهای منطقه، تلاش برای سرپوش‌گذاشتن بر سیاست‌های مخرب آمریکا علیه صلح و امنیت منطقه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131458" target="_blank">📅 18:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f535828338.mp4?token=H5X3g_thnWnHeYpn9YkYoSEBAqbns9TTeXidYbUhzwDxfvevZUQ6dnlZVJnFFPQ-7zXHpMb_vHMZG2DVfp4KuDZBaucqdnUqnGmitRK8vkOs_7tV55oqpAg2GBm6j08MZsdDH6cB6SGjvOIhkN1fAYubSPDK87CtOlGqjYA5NIiU1ve75p-V0FBKuE56Ky8NbWVuRi2E2vdPmcXuMCTXvesa1ZJ1BZztKcw_rm9l2IBxJUFGyFDadBWMt0yXVijPHgmfSexfK4Uwh4uJHlGdRuJvG3O4tIrrvVoQLCe7ZRSeUMl7ve6TDjROrvxVSTqRSqJANBUGzcvIL9A6tbjEzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f535828338.mp4?token=H5X3g_thnWnHeYpn9YkYoSEBAqbns9TTeXidYbUhzwDxfvevZUQ6dnlZVJnFFPQ-7zXHpMb_vHMZG2DVfp4KuDZBaucqdnUqnGmitRK8vkOs_7tV55oqpAg2GBm6j08MZsdDH6cB6SGjvOIhkN1fAYubSPDK87CtOlGqjYA5NIiU1ve75p-V0FBKuE56Ky8NbWVuRi2E2vdPmcXuMCTXvesa1ZJ1BZztKcw_rm9l2IBxJUFGyFDadBWMt0yXVijPHgmfSexfK4Uwh4uJHlGdRuJvG3O4tIrrvVoQLCe7ZRSeUMl7ve6TDjROrvxVSTqRSqJANBUGzcvIL9A6tbjEzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای مسلح سودان ویدیویی منتشر کردند که در آن پهپاد تهاجمی بایراکتر آکینچی ساخت ترکیه، یک پهپاد تهاجمی FH-95 متعلق به نیروهای پشتیبانی سریع که از امارات متحده عربی حمایت می‌شود را در شهر تندالتی در ایالت نیل سفید سرنگون کرده است.
🔴
رهگیری با استفاده از یک مهمات گشت‌زن هوایی به هوایی از نوع ارین انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131457" target="_blank">📅 18:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131456">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان: هزینه جنگ برای لبنان سنگین است، از این رو مذاکره جایگزین بود و باید پیش از قضاوت، منتظر نتایج آن ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131456" target="_blank">📅 18:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131454">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=DZH2kvc25r7hF6n74zqvnDG1xw3dEbGPi9_eJxpkrmz3lv67aOUiEtz5EUMgPhbC39QyD5BVqKc_PVPGMATBjOGvl5dykBZzMpxJNYGIkLKadxMHYPGNmyhC-OVnQveJSAMj3R4rtaRN64WbE0ioTHRk93ZwHkucN6zzH7wgy0PXVYQPlENB5Z-5WiwXm4SowJguWEVA4dB2X0Rypa7_akAKEUUnnGHx7kGSXlfm_jQAgR2-5H3Szxl-a6Bh1zbfKPepgN8tTd7R-qefz-uYwHbkC5uUpLyNV-Hna0VpSa4jNtPHxtZxYJQQd-NCtHWFCd0KXtD8bMFAWj9AOXZIGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=DZH2kvc25r7hF6n74zqvnDG1xw3dEbGPi9_eJxpkrmz3lv67aOUiEtz5EUMgPhbC39QyD5BVqKc_PVPGMATBjOGvl5dykBZzMpxJNYGIkLKadxMHYPGNmyhC-OVnQveJSAMj3R4rtaRN64WbE0ioTHRk93ZwHkucN6zzH7wgy0PXVYQPlENB5Z-5WiwXm4SowJguWEVA4dB2X0Rypa7_akAKEUUnnGHx7kGSXlfm_jQAgR2-5H3Szxl-a6Bh1zbfKPepgN8tTd7R-qefz-uYwHbkC5uUpLyNV-Hna0VpSa4jNtPHxtZxYJQQd-NCtHWFCd0KXtD8bMFAWj9AOXZIGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد روسی امروز زودتر به سالن شنا و تناسب اندام در زاپوریژژیا، جنوب شرقی اوکراین، حمله کرد.
🔴
چند نفر در داخل شنا می‌کردند که پهپاد به سقف برخورد کرد، اگرچه گزارشی از تلفات منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131454" target="_blank">📅 18:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131453">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
بلومبرگ: قیمت نفت خام برنت به زیر ۷۱ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131453" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131452">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aqa1rBPHk9izG5SMrissy4ZcppN9_jpA1G0OLAX6jsA7gI95Tke592qDk-XiWbUx7LjL28r3Oi_Odv_aTWapbN9vdQxfZw6mDVG0E_qZs0VpMYemEAUQJcKSMvwrAMoZqhWHWodGF9FSvojE4xmjKPKY4wYy0QbaAVu0KMKKHpWmRo_Gn-vm2hQWxElApP-zAZW6ApAl_vl2hZ7GLijc0vNYJDICYK_g8zr5DXX3rgbT3Fwo3wnjRzgsiSsI-C7KC8XaK4yQZYgOh5m0UFtVwDYzTIn5DPtTYOESLbkF-o5jsXEcn3oYhdBvIZvOS0OeuOPsElob-UHZC4uGOCAgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم پناه، معاون پزشکیان: قرار باشه هرچی رهبر بگه رو اجرا کنیم که باید در تمام نهادها رو ببندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131452" target="_blank">📅 17:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131451">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_2nvHTonx-6dIYpr7rbAYIkHe7_aPbADDP6A-ZXKauzzaHRgNScGgBpxjOsaZdykTkQHvl155Vm_zs4BTLdlY_RFRTo8GH2OB7KYu60XGJMdLxhGjk-XGVi90svefEs54UdBoB3WcwsUfG4TZ-rHYEq9XEqqIT_LQY0aCO6UwUX_HLwN11AdYYKd7ovdZJJTMjE0J4eCvRHTwaZzjWN5KFkloSYqunp1xjb5dVdvqRg_q8kuyqnKtHmp9wAmZzP7gzg7_dT_T3L7tPzTmTnZvuWsQMN3R5obXhqSBELj2dPu3qSiNajDesFlRiJ13erCfCQDQ78n3XjyuNSZ26HxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهردار نیویورک، زهران ممدانی، از هر کسب‌وکار و هر نیویورکی درخواست کرده است که با تنظیم ترموستات‌های خود روی ۷۸ درجه فارنهایت (۲۶ درجه سانتی‌گراد) و خودداری از استفاده از وسایل بزرگ تا اوایل صبح یا اواخر شب در موج گرما، در حفظ پایداری شبکه انرژی نقش خود را ایفا کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131451" target="_blank">📅 17:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131450">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سید عباس عراقچی، وزیر امور خارجه ایران و امیرخان متقی، وزیر امور خارجه حکومت سرپرست افغانستان امروز دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131450" target="_blank">📅 17:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131449">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkvjRhhG04Q86D1Y_zk7tend07h7ojHnZTBE_xKMTURRvgKhWJrjw3s2o_KZPe-laTXfoRf5UNZJ9FSIUaqM2dZhh9i8vO2PknRP353XgnKLAdtSjmEgO3t8dqP8GwIX8BW6A97cBSE28-kWwJASc2qGOgGIlV_P8t4Ro90pCYgZ2455aMB-ZM1v4YB5GwhOZhyo4_cfYlDfbW8_0S0MhfFMuMgds4NA9hE3K5-EmHxgRaR_hQE25SKOgsC5hBIdkwdLhGxQLZCqIzFk9isrQK6o5wreV2Pk1e1su9GEkzNclqvYPYRcp7wALzyiN284QQ4rAxEi-tM5MqQ0wqugGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس از تذکر مقام عالی به نبویان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131449" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131448">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روسیه برای واردات بنزین دریایی به هند روی آورده و ۵۰,۰۰۰ تن متریک از قزاقستان تأمین کرده است، زیرا حملات مداوم پهپادی یک سوم ظرفیت پالایشگاهی روسیه را فلج کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131448" target="_blank">📅 17:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131446">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=CuzC9lGD7OvqkELYU9mJva4q7aDLPs4djIqb8FdEETaClY0OyCLS7JDhMp0NOl2FEonJk-1IPGR6Dh8zSPEpO3eMUcOleYCcT0Ivt6XerHFnqiVmz7vvZjvYeI2HSdSp0pMu-tcVS95m8VvEGTH8doyor60QcRDk0qSGXBwiDFWY9JSu-nZlWJ-vHwsORv14FFXApxu98-k_sSCMhUCOM_z9akGuy50VxhOtXrMBNpOC1Ccs-2QS5_JhSOZxru3Q565oBRVwY8c15BmGtT4PJkIxsTBuoWd_fcqYRyaX6CDd1mQyiQs5xHYtwCk2RB2G_0K8RF62WqBBNzesrKhIHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=CuzC9lGD7OvqkELYU9mJva4q7aDLPs4djIqb8FdEETaClY0OyCLS7JDhMp0NOl2FEonJk-1IPGR6Dh8zSPEpO3eMUcOleYCcT0Ivt6XerHFnqiVmz7vvZjvYeI2HSdSp0pMu-tcVS95m8VvEGTH8doyor60QcRDk0qSGXBwiDFWY9JSu-nZlWJ-vHwsORv14FFXApxu98-k_sSCMhUCOM_z9akGuy50VxhOtXrMBNpOC1Ccs-2QS5_JhSOZxru3Q565oBRVwY8c15BmGtT4PJkIxsTBuoWd_fcqYRyaX6CDd1mQyiQs5xHYtwCk2RB2G_0K8RF62WqBBNzesrKhIHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس شبکه افق، به قالیباف: این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131446" target="_blank">📅 17:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131445">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
طبق گزارش ها برخی از مقامات ارشد سیاسی و نمایندگان پارلمان عراق از کشور به صورت پنهانی فرار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131445" target="_blank">📅 16:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131444">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47920d202.mp4?token=Tr5E8nwXYqf2ZcopoG-aX3GNPWp1LqaJCwVSXqMEiLkNVhgzJkUihOCwT9X35XZOhvmiBh2JaogjjzPkqaCLakGto2ODGT0jemBRC5yan4R_Pr5tbKxx3_LVNgX2NWozsxavod9Zhie4n9V822UHw9aXsv8qk-hiNU5ezyhK9xpmG7dJNga2DHgsWKJFSMhpMiDqAVPbHB4gpr-U2YHaJ5-6lj4z-mkTqCu53ZLPycBIfPB0gxsiDXzLkeK4vEt9QeSSrGcuYDBdJe3WUV2mzvCh57Df6OD2C738WBAYsks4h1NLYd6S_jr_RR61YAgoVM7T2JWk9CEgo2w1042weg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47920d202.mp4?token=Tr5E8nwXYqf2ZcopoG-aX3GNPWp1LqaJCwVSXqMEiLkNVhgzJkUihOCwT9X35XZOhvmiBh2JaogjjzPkqaCLakGto2ODGT0jemBRC5yan4R_Pr5tbKxx3_LVNgX2NWozsxavod9Zhie4n9V822UHw9aXsv8qk-hiNU5ezyhK9xpmG7dJNga2DHgsWKJFSMhpMiDqAVPbHB4gpr-U2YHaJ5-6lj4z-mkTqCu53ZLPycBIfPB0gxsiDXzLkeK4vEt9QeSSrGcuYDBdJe3WUV2mzvCh57Df6OD2C738WBAYsks4h1NLYd6S_jr_RR61YAgoVM7T2JWk9CEgo2w1042weg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یک مداح به مذاکره‌کنندگان: رهبرتونو زدن هنوز خاکش نکردن، چیکار دارید می‌کنید؟ چرا راستشو نمیگید که سر هسته‌ای هم مذاکره کردید/ ۱۰۰ میلیارد دلار بدهی دارن بعد ۶ میلیارد سویا و ذرت می‌خوان بگیرن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/131444" target="_blank">📅 16:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe0d83ee9.mp4?token=lP-qAqSHcNOpq94AVZZJ4_mZkhw6Xit8K5c8Gea3XfrGOCp-I4QSJq5qoMF_YZE0vGK-HnkleN-8clVzzhYn6NymutFSu00y1RXihh8bljcjM4TkpGtrpQ5EhWVlBzeDS5XXe6JUrblpihPeQx1tJq67xJWwc9vx1w--0_wbMBCd1cLid-p_GbAnw7w4lowQQMKkQYGTQEuplFm4OHgANexphc_LJbAhPy9Az4OhlK2ZNlCNsoCLfOu5tqI1gSdcz5JYULmaCLSvhC5PEsMOEL1T4iU3-txYchiB0WyC96j5kqPBYuC-3IH4_Itebrwl2hgbMvr5cgTwDZ89EHbyHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe0d83ee9.mp4?token=lP-qAqSHcNOpq94AVZZJ4_mZkhw6Xit8K5c8Gea3XfrGOCp-I4QSJq5qoMF_YZE0vGK-HnkleN-8clVzzhYn6NymutFSu00y1RXihh8bljcjM4TkpGtrpQ5EhWVlBzeDS5XXe6JUrblpihPeQx1tJq67xJWwc9vx1w--0_wbMBCd1cLid-p_GbAnw7w4lowQQMKkQYGTQEuplFm4OHgANexphc_LJbAhPy9Az4OhlK2ZNlCNsoCLfOu5tqI1gSdcz5JYULmaCLSvhC5PEsMOEL1T4iU3-txYchiB0WyC96j5kqPBYuC-3IH4_Itebrwl2hgbMvr5cgTwDZ89EHbyHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه وایرال شده از یک تریاکی:
+نظرت راجب مذاکرات چیه؟
- ما با کسی که پدرمون رو کشته حرفی نداریم و باید تا نابودی اسرائیل بجنگیم
+اینجوری ممکنه زیر ساخت هامون رو بزنن
- بزنن ما هم زیر ساخت هاشونو میزنیم
+اینجوری ممکنه وارد بحران برق و آب بشیم
-مهم نیست برای ما ، ما کف خیابون اماده شهادتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131443" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131442">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
آموزش‌وپرورش:
امتحانات نهایی به‌هیچ‌وجه به تعویق نمی‌افتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131442" target="_blank">📅 16:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131441">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHk-keGrjliKZ86q5PdzyYG2lV4ZjRkYqswiC9lyXoGbWpTzd73a9699mO0OjYFc_RcC5KhMoUg9M3srmyg9RtWWWCrQBoS5h95njxsfW8vqMz3GFd-7yL_mvf7YH7qrbbhoK1yYpHGdX8CcenmPIINSim3XUI8wum134iXAR2hFbGJNCxb--vJPdeLKMtfqFPKcYHPGeKlSt7XKPGFxw4nTjNwd0YWsEtPQqhGbo8zgPUBqn5_eqFwzGt1rsh_ciXuX27A8bjxwbXSu2jamP39Y4edtDEJbMVAEpvrkWeqwa-poUXRcxcrxRJLWm0rRadPvMV55fusqePezjFkQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه سیدعلی خامنه‌ای توسط ارتش اسرائیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131441" target="_blank">📅 15:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131440">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfZOnM2_zNc6mFh4kDRbjW7Tlz6vpjOxVM0pt01e2-qZu34rRfA-6ILDNgqoyYD0Vu5U669VcRyZpaodOGjK-deDDwO1cwZf3_97rLMxz1DCNtgQPAcL4RkNqrrZctqrQUhkzsfUj9awLoyegB4wOLRqhFf_tMeVZl3oeSuJ3knXXHHtTkKTeGy4cJFEAMjsxcYSSJElsEZYXck6Q57LWsb1qZwNtcDxwvKedw913yxVBkPl2uE6CiCdZpr9RYDhNWF6G48v7L5jfGG1ayi9xfcYuZNegfurdXTIrhLSNYUF4mf-0GZVCpgBFHJY5GJRIgEHfUget3XUYnzXZLQoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فواد ایزدی:
مشاورین قالیباف کصخول هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/131440" target="_blank">📅 15:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131439">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmIv8HuaxmQuHKu5B62gNp795n4bV4-8E4gEhkTmlsiYa_xTrGjBJRz93GkYixHZSVkOH-goB7kn47nZrmJS_G2CA7Ie56glLf7iShHRIzD8DWA3-Agllhg-XJVK42J-RI_Mdo9doWxNHO1fuwX3h2bYiCVpKO1Cx9OwP97mW0I850p63A5JXRDK29Ed4EJvMSFUWCLCAC8Z3Q9u04mclP8s-XDRahs6sSPKTLSF2hh2oDnCmaluXHdRvXNxPC38S2jY2L86CNAG3MXlBIInDKAzinLXVX-lwOipdEQMIb8g6wZSpPGjMsDXgzeJ63uU5Kzs5ByoUyronyhMMsztHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
ایالات متحده تاکنون بیش از هر کشور دیگری برای محافظت از ناتو هزینه کرده است، بدون اینکه هیچ سودی از این کار ببرد:
🔴
ایالات متحده ۹۹۹ میلیارد دلار، بریتانیا ۹۰.۵ میلیارد دلار، فرانسه ۶۶.۵ میلیارد دلار، ایتالیا ۴۸.۸ میلیارد دلار، لهستان ۴۴.۳ میلیارد دلار.
🔴
دیگر کشورها، از جمله آلمان، بسیار کمتر از این هستند. (۲۰۱۴-۲۰۲۵) مسخره است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131439" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131438">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noNeHlVVZPPmcDU6PgYNdmW7jM2alrvJJOg_VUIDocU-J4r4XuRNnmYfreMjncx8qUaEc5KC_9E4YHtla3Md8brbuiOA-JpjQeIRrGNlUolPuYuHzhv77gGvoCrVXJ1kCIa-tC5fwJjfmofFVYY3LhQC6fOoYK1L8hzEBkaOc22wQRm_fEKJB6VpCQAmx7EMo7O-0TC1a2KWlzbsHt7TLP4Qu9WB4IM0P6qrNZQ5_Wa0ppWzRlGY0h4xnfxkc5cCeahi41oDyJdZiSDqH8ToBdwMaAqlW050sQvTSXOMtuVZeX2YxEUTLAqVJfp77BJMJA2gyXMo5-MhXCsIQNXewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131438" target="_blank">📅 15:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131437">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
زلنسکی از آمریکا مجوز تولید موشک پاتریوت خواست
🔴
در پی حملۀ شبانه سنگین روسیه به کی‌یف و مناطق اطراف آن، رئیس‌جمهور اوکراین از آمریکا خواست به اوکراین برای تولید موشک‌های سامانه پدافند هوایی پاتریوت مجوز دهد.
🔴
روسیه و اوکراین دیشب هم به حملات دوربرد علیه اهدافی که فاصله زیادی از خطوط مقدم جنگ دارند، ادامه دادند که تلفاتی در هر دو کشور داشت.
🔴
ستاد کل نیروهای مسلح اوکراین اعلام کرد که در حملات شبانه روسیه ۱۳ نفر کشته شدند. در مقابل، مقام‌های روسیه از کشته شدن چهار نفر در حملات پهپادی اوکراین خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131437" target="_blank">📅 15:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131436">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d606e626.mp4?token=ps_Xore-vwgKqhhzN2TmOeHxlYvb7Mv5FRj2Pi51WoOheG8-nIa60npRsmxRfCCUKy2mVOq6N_hR58762EZBkaan3ddvwhizW7a5x2cPqr3O_vKfSGRe0rlhSTI3e98dhcCa8vDHktHTCeCYXAyrKl0AUHJDkVpFxrOMZVk2geajl79aTflDpWuAe29BhaPYM9ROBNnseWNpZh6h_aavc4ulZWrcuQmDR_lJC-SFDgbfP42JRntn2CWoPlLza5NPI_9rPZxc8WOXn9y5_w2GDgQK28aarfiifumR4Lm-_H1iUgYhGBAAHoy6dSo5eZoKfCmDTTvCIqWqrb0opCO_IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d606e626.mp4?token=ps_Xore-vwgKqhhzN2TmOeHxlYvb7Mv5FRj2Pi51WoOheG8-nIa60npRsmxRfCCUKy2mVOq6N_hR58762EZBkaan3ddvwhizW7a5x2cPqr3O_vKfSGRe0rlhSTI3e98dhcCa8vDHktHTCeCYXAyrKl0AUHJDkVpFxrOMZVk2geajl79aTflDpWuAe29BhaPYM9ROBNnseWNpZh6h_aavc4ulZWrcuQmDR_lJC-SFDgbfP42JRntn2CWoPlLza5NPI_9rPZxc8WOXn9y5_w2GDgQK28aarfiifumR4Lm-_H1iUgYhGBAAHoy6dSo5eZoKfCmDTTvCIqWqrb0opCO_IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بزودی در تهران، مشهد و قم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131436" target="_blank">📅 15:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131435">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4392bc1c10.mp4?token=oPJYPvPeEjxth7bp3kHqQgiIglEXMOMVV0n1bFxG17-QJ1stxf75z0XeRi9RrByIRem9jDzyh61W2JK6XXkE4cFarqcmCKWJsVyswpkP_dXGO9NbBmMvv58LxhidNyfrXPZo-uJig-Pyav4gLvEKKdzXdXOFrLbKOPscFZybme7DAuZjvRLS89EumDjEP1GY1WSaXwSM_7WWdy4PnO0DJDb9ZaH9L54BCIm-wYmKl3vyObkw-lXEya_KjvbXdjan3NcuECxSZWm8UIkSlk9WHqG7buN_lp3sfsWWPWebxZUkItAbCntdnzjoRL3hx_tNYsHDGgvZn4W5fOB1Ko6gR5sFt1Ibhf-xZd6dUIv-o-4FUswOzetsVn0bQ0o2UgUx4ukPy9sSpc7QjyKHnSTYHh75PZLe0R1Y5ol4DoxPsjLXPh9umyZQq68rPvX7U37A82oM_e24iG0md9b8SNLi2D6cGXMwbbnZCD-jInqNtUsyrlZ9BfSQblUbdCemv_YmbWpLmBYoAoatAliNdWdlLQN5Ii0HFrTf6VBFx3pJlzFtztsA2JrfDU9_E5yXlObDdxBrVkTm_SCGXwFToB95A0F417nkaCn_Mw5d444QcxAag5u3mAmDYAhq7P095jlI42FyKLb7C0nj36lYwfbxneii-jZAE_9GnwC7KkyQO48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4392bc1c10.mp4?token=oPJYPvPeEjxth7bp3kHqQgiIglEXMOMVV0n1bFxG17-QJ1stxf75z0XeRi9RrByIRem9jDzyh61W2JK6XXkE4cFarqcmCKWJsVyswpkP_dXGO9NbBmMvv58LxhidNyfrXPZo-uJig-Pyav4gLvEKKdzXdXOFrLbKOPscFZybme7DAuZjvRLS89EumDjEP1GY1WSaXwSM_7WWdy4PnO0DJDb9ZaH9L54BCIm-wYmKl3vyObkw-lXEya_KjvbXdjan3NcuECxSZWm8UIkSlk9WHqG7buN_lp3sfsWWPWebxZUkItAbCntdnzjoRL3hx_tNYsHDGgvZn4W5fOB1Ko6gR5sFt1Ibhf-xZd6dUIv-o-4FUswOzetsVn0bQ0o2UgUx4ukPy9sSpc7QjyKHnSTYHh75PZLe0R1Y5ol4DoxPsjLXPh9umyZQq68rPvX7U37A82oM_e24iG0md9b8SNLi2D6cGXMwbbnZCD-jInqNtUsyrlZ9BfSQblUbdCemv_YmbWpLmBYoAoatAliNdWdlLQN5Ii0HFrTf6VBFx3pJlzFtztsA2JrfDU9_E5yXlObDdxBrVkTm_SCGXwFToB95A0F417nkaCn_Mw5d444QcxAag5u3mAmDYAhq7P095jlI42FyKLb7C0nj36lYwfbxneii-jZAE_9GnwC7KkyQO48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اگر ایالات متحده آمریکا دولت لبنان را تحت فشار قرار دهد تا دخالت سوریه در خلع سلاح حزب‌الله را بپذیرد، آیا شما با آن موافقت می‌کنید؟
🔴
نواف سلام، نخست‌وزیر لبنان: نه، نه، نه او و نه من به این سؤال پاسخ نخواهیم داد. من معتقدم که رئیس‌جمهور احمد الشراع قبلاً به این سؤال و بیشتر از آن پاسخ داده است.
🔴
از طرف وزیر اسعد الشیبانی، چیزی برای افزودن به آنچه رئیس‌جمهور احمد الشراع گفته است وجود ندارد و من هم چیزی برای افزودن ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131435" target="_blank">📅 15:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131434">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پاکستان: دیشب طالبان بهمون حمله پهپادی کرد ولی همه رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131434" target="_blank">📅 15:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131433">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcwiCJQ3XmW6ozv3CH7OyDLgWmQf29ewHJcyONqmwyGc1bTYY9xAy3rHLVjvN6ILlaWFhnn45FUL0N5DNjcwwYKM1c0W3UA9fQRuFsOUJVx69229Q3r8nl0itVS1nPr6WI0pTU3K5tc8ydxbogGJgXtVKEN0taOR5_EhxjGkdXmzWw-5rUW4bvypDVrRkJcGNdjFAq4GTsO5ojHAJT-A-nG-AQlckUXPqPS3Fh8CpZ1W8UbuBI7o3CXNtarR0VZ5aRtzUefjxQEgaRkwkKksAfqIS8Ce4eN1Yq94EH-DFmyiktO9xqKD1EKuJGzi9ex37bHB8vxhrf1Xm8o4Bw-asA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان درخواست ترامپ برای وفاداری بی‌قید و شرط به ناتو را رد کرده است، و وزیر دفاع بوریس پیستوريوس در مصاحبه‌ای با اشپیگل تأکید کرده است که این اتحاد بر اساس اجماع ساخته شده است نه اطاعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131433" target="_blank">📅 15:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131432">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سفارت روسیه در سوئد اعلام کرد که دوباره با پهپادهایی که یکی از آنها حامل یک بمب ساختگی بود، مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131432" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131431">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK5uPFnCCjN44KDChj8GNRMDgHJVUHuRlVMjpqSCXQj1RYPZ9hC4lESNNyiUcpryjmpaazKFlEIuEKaIZWad8wPkFmXxqpT-hMkvA3gToHmpq5jyuChH138wa-Ehbp4DHc9N1bdxtYCpe-OHBr5rX5e3r4xAinyN8AOYLBnM5_CmVPzkYsID36hmdc0qHgJN5iTnAlPX2h5zjhBr9Lr2YylgDu3Z4oi1PfEPUBlAs_dtmpyZRjptslAauMN898cryjSgQWVIqnulZlz544g3St5EUVbXoniICoh0vji4r0AmYV3q6pS-_1L2S7wMajnjFmvKFCrhDM7iNm0B-DJ8UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشته های گرمایی در اروپا از 2129 نفر گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/131431" target="_blank">📅 15:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131430">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نیویورک‌تایمز: جنگ ایران چگونه به دلخوری شدید ترامپ و بن سلمان منجر شد؟
🔴
ترامپ هر چه کرد، ولیعهد سعودی نظرش را تغییر نداد
🔴
از لحظه‌ای که ایران تنگه را بست، کل روانشناسی اعراب خلیج‌ فارس تغییر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131430" target="_blank">📅 14:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131429">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYDH80GT2jaj0kLpRz3BqGY3ckmMx-HkDYiuPv8uVHC_yvD3ubt01Ho7fK8_sk0cnQ-kIzi-JeYWnYJ9Et1w2u8FUWvGd1hKNoZ2mEC5Jgr6oNL5VKeMJVE7eA3-W8W6uy4ORNEwj_FAO3-nxnZmEC1XUvzhbXwU7a1BwNiPEO_pBy7AZwmeZ-JTW7J-mqj6H66rQfXY-a9iv5S7w3K1wX8JwQle40t3ZzdR4DjyCM3A_H53OuzaOYdICWpFDLhGUvRlWlzBXXhUb2ivGD3gO9DHPFypu6MuxBtwKHcv0RWKAKcvHI2IwTqLFrUr4ljAebnsnCZ9wkoaf1LLDGmcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد لبنان، عامر بیسات، می‌گوید خسارات ناشی از جنگ از سال ۲۰۲۴ ممکن است بیش از ۱۶ میلیارد دلار باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131429" target="_blank">📅 14:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131428">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQH7YCkMLR1KZlUOn0wXFCSFozrnl80oZ7tG-YC4OmefDVszZ655rSu5Q8pbEJC-Lse2O4XT5DAIp-z3WR6cG182EXKqAIuAre9HRlG5UbyLPT9oltD65tyVJHBRTUVTtyo-WTOEKJDnuUJJIbz9RCZ6bJrewMcP5gQnI47Gf_wT6WAzI4eyMjFBfMk8cZaPOvoSZ0MYr4AiGKOL7Ojd1GCeTA8BNTZIk7juS9YFN87jgxR8ae16aGf9FX_Rz2sALKdDNT0lSw7x1dvgrZA2cvB2JYKTxLxBfZ-IO1JX1uu0_93AncDTjry23XNPNbRyIvAofabX50AdER79tLnHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش شده است که نیروهای روسیه یک هلیکوپتر تهاجمی Ka-52 را از دست داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131428" target="_blank">📅 14:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131427">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الحدث مدعی شد: دور بعدی مذاکرات هفته آینده با حضور عراقچی و قالیباف در  در بورگن اشتوک براگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131427" target="_blank">📅 14:39 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
