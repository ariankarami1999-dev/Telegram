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
<img src="https://cdn5.telesco.pe/file/EnJBuxfszWoaL-HsYuzSU6FxouckcfnR32clTw_UVdRzcM484bijDWNd2ZDEaZp2RJDQQhVWs5ZfgXOyLQVMzoTUc37SJNRE5iaqIxaqny37-6HSCL8ff_McrZedigrzlwErL1nTS72WFuP1rA1oKn3cmDYQt_5WKQo1819cxEMCyF-enUOxtiK7bglya_EgJKub8oKsfcaKaZOMv5vebAHrUcEX-6HWLoFA-8qQuLYm2yxJmStgT62An13BSy2KurbqFBveMQtdepEqHvuPJGuyFHVliG4O3pmJI5BoYz0AFvVJtyUYPcvf-54wckA-tExxpjOt-XAGCDlR4I7Q1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 717K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-95195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpOQ9ck_4UwzxGiJwwoaqHJLe5ItGmigx9yXdLV45fuAT0dv7qEcHRC0AR0yPU4NulGDlHe_WB2jZuq-3h1y9pmg03hcYiLW_g-Bs2GN4KdjjFjArXFApRMJtdpTAAh7DpmTJS0ltLf57sUCPkt8CURmjX1u9l1Q2bs4AIq5fjTYzu8Fbm2qHHALRMvjhHG4Bp6ilSYrLEoAvpMaZV9gJMd3HNluqqxj-J07HL1B00R-HTWOe5bYrYew3vciih5x6ARCjmMBU13eZIkttFQ3hsbOU1fBM_m6BMZR4WE0nuVZrhv2rj4nflxEo_PQiFYyzjvpxpJp-5-rkSl8R1Tu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار کلی لیونل مسی در برابر تیم های اروپایی در جام جهانی :
17 بازی
7 گل
6 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/95195" target="_blank">📅 16:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJf-gq9j169G5Y8ykqhgG1ipJCDCoyvRyGqgu38Qp62hjRSCjOcSDDBpJNpPSxXoQ876gEuVer4D5kx5epY2ucvedSoNr0A6I9J54uH65IuzIH1YbEdODbLuE13fZFT6FLjOQ5Q9HhzgcLd0QIoI4N8f3w-IW3UMTa4eJj1CkltYqmIlzu5q6ds9t5HRCBqT-0Or9Vxhlqk93rN1bvaO1Lh0BhrtTTFX0fKeMHZN7KiwSFVrOuQLk7bdqDl-lGFzC7LJzRo-Cg--6tAKri67u5XOdnHA5fQXlz9ACXrYnSaU5KZQimLwG8fOop0a1wvV6hBD6G4M0zJlDMdFR3gPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی:
درخشش مسی توی این سن؟ من وقتی ۳۸ سالم بود، چهار سال بود فوتبال رو کنار گذاشته بودم و ۱۲۰ کیلو وزن داشتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/95194" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7f6b7006.mp4?token=pceT8iJMA6rMjp1vafaN3nFeYYKtzpI_gB9OTzHSbtdqlQCsFp7c6g2SFzs2eq9FqOyGIRStKqbVyexJBKydoDsHeVXBlLrWJkS9sZqOd6Ou4iQ3-excb1F_U2rOYQKBlulw5ttlKTp4YCVbaYqCnfrjoWKbmezG79vDUjtfYcwrrxhdleB95NSg5hy_4uEG7NlgJ11hXA2wyJw9fMf-kPMmm45MV9I5HPb-qLGRiVP9CZNhY6NmsyTAsSvbalSuvx5noHuICLpxc6bFiG7AWtKgQCO7_ZXOyFnrn2chF8MbgTutclNbW7WpwGDdiiCnr5K5oGLBvtGvYrRqgLGlcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7f6b7006.mp4?token=pceT8iJMA6rMjp1vafaN3nFeYYKtzpI_gB9OTzHSbtdqlQCsFp7c6g2SFzs2eq9FqOyGIRStKqbVyexJBKydoDsHeVXBlLrWJkS9sZqOd6Ou4iQ3-excb1F_U2rOYQKBlulw5ttlKTp4YCVbaYqCnfrjoWKbmezG79vDUjtfYcwrrxhdleB95NSg5hy_4uEG7NlgJ11hXA2wyJw9fMf-kPMmm45MV9I5HPb-qLGRiVP9CZNhY6NmsyTAsSvbalSuvx5noHuICLpxc6bFiG7AWtKgQCO7_ZXOyFnrn2chF8MbgTutclNbW7WpwGDdiiCnr5K5oGLBvtGvYrRqgLGlcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇸🇦
هوادار عربستانی بعد ریدمان دیشب کشورش اینجوری یه تلویزیون رو پودر کرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/95193" target="_blank">📅 16:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95192">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🤣
اینو یارو رو دیگه حتی خدا هم شفا نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/95192" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95191">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7kzNsnqp8eskd1T4dz_1zcebCdp0Omb2Z_WpOIe5L-l73YZd1QDH5zYXOAVn18AHMrauHbPOguzFYO6vRJ69HChzZq_Rqk3QrMgsesWryjPXVyVS2EMro6BNiBLbYVaHAwhm4XKE2DjjmIOmOJWgkZNoGu1xkZ7dc5vDoOyq_JyoiAbYbQZxVa-pmKGq08nMQ02j0BR78YE5yjWvtkYd-YHSePsBhM-Rrl3gcef2lch3FlX8BMMkMWsCLcVrjLC9V_2VtxA7Yj9I9l1rkLOtdq3HRw9SfN59Tw6JGSDDubvMvBCJw2egN8Fg9vHqNC4BKVllUAvMtSYLrHfx_5rBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
افسانه لیونل مسی امروز فرصت دارد تا دو رکورد را بشکند
🥶
🐐
💥
پاس گل دهد تا بیشترین پاس گل را در تاریخ جام جهانی داشته باشد
💥
گل بزند تا بیشترین گل زده را در تاریخ جام جهانی داشته باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/95191" target="_blank">📅 15:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95190">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8m-KxB0DR9DtOcwe0zWyqqTGgM4qDNX50ib2VdYU39SOzIr9c7ZqCHdWuUgyhxfvKEKP_WeofBM0mwe-DTl4BmlIKmgro2LZY5io3QDc4gwAi4747TX1yxfH38mfzYLWAO01fLhlSYxEhxUE7LpvoO8Yw9p1KZMzn9g75ByjoRxrSSzvQpTXaMrjIE8KcwrH18dX-mtru3Trl3NsInCNLJERGvnXMOGzhPbKzXrBJ65WyS5BeBb6CVIqXI_vqCLtyNKM_tnP_sDuHxPGJ-jFk-xoH4AQyGPkndJQGeQAVpIclYxCahtZ5y7d30uYUOWEKbD_44G4PVCxsay3vBKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت کروس برای رونالدو : کاش من اون صخره بودم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/95190" target="_blank">📅 15:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95189">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsMitjFZrKqcLD8kkgBcdANguWLLu6ySFC8qKSZTf9HWWP9EUbn3kVOCAwEAOCxST87pgUq6gdtGBItWJVb_64UVilWK5GRdm0LP3WpfUvq2V6n0N4nYFRmVPWwE28-yvhA9SeTF1fW5R7Tm_RtJFKg_qEKUYMUmwkQLJqNThinVB9AFZfCspNIx9RPPEIeumcvaoEVSLq8XTnOz6Uk3u9Ve5VwmqQVt100oZ52JtE2WSu_OYQahQUwasKlFF4uLzopRL-Pl7wfsSG8hCVYr7rRnxfNCduavsKx9nC7HQZiuUBZoFWcH79CmgUVf_5HsqxyeapUqIKyBT1-I002jLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
تیبو کورتوا، کنعانی‌زادگان رو فالو کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/95189" target="_blank">📅 15:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95188">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDvvnCpj5EH7adEk09nDzOR9CnaZSIRKNIELymKNTioGvVtLU5pWwF9uCu6pm6xqdiufu_rIJaklCKgZLavQBW0AllzPaRpDRoZADW8u6WYmA9AjLI6cMXKshh6IiphCPZGibpQNUTG-EWjuW0k1a7Mvv-d9EV_jG5UVo_DJBOzfHckR1JljNQ9J4VoqcxLMsPlOT9QstFHwnmI1Ql1erV2ll5FtQ8J31jbBEPLeI33xoKUgRlU0M1yh-lVnxVjwy1XJefVp9irx6HzfJ_P3W9vrEtnOnnXJ9HDVT-wWBMz-eMf_58ukdrJpXfPZNV8byeN3KGuhMSC1RGX7u_Z_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇪🇸
زید دنی‌اولمو در بازی دیشب اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/95188" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95187">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77bb57281.mp4?token=fIEGSeuFU2XmPYEyQfbysBlQWcrspHAijjxOuz7pk56leYMZF-LVIOvxwcCiovuAQ25dQTZNBrYsEIznIEaZetPJtOkGSgooNk42tgIjL6JMTH-2NFqhvKJkatVQpkUsQCmdoo5h-KuQJTuFh30I7r4pJLvj937raTFBE2UQu3Y3rG5s9NbpxLf_UE_ZmxId5zSnJ_3ZMAY5mr_9b0rw0_yqLyooON_57QB7II3lP_hh22DUnItD6KnYHpMRgGHHe6qpSZhoX9EGVAAaviwVsL9_nzUk6H0t2iqSNIHg0tUK22VNnW1KL-pGeGap1XrBQRFa9G-Pq664w42vR9d4XSRaVp36zQVd88cmjCnFMv6AxtBl4A3_NRDigeHTlPhEJ4cQ6yx88Ld1LOZZopjpdqNIe21PO-60-_2avhGwybFXerdbkDjTDWog00NpOdKJ5EU85yD-jJw1UnbhgR4gDxjhQM4a4daLct3kQhCPcl2F8OkU13fFf0YiowwD5cwEvh1o4bhHufeIy8nDy_mZA1ndqFa_lOccUe2VLhfa89bLMVcZJQM7pgXILj3v4OYsBjuyj4jLf2dUig3S9jSeuWxlQQ71ODkeD7kAjDLcxBidFjJTEGSfIm8GS1xnOgiTD6YpEW0WfZd9HBvJbiKEHlcTY8T4zs1Ubl13fAGVCyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77bb57281.mp4?token=fIEGSeuFU2XmPYEyQfbysBlQWcrspHAijjxOuz7pk56leYMZF-LVIOvxwcCiovuAQ25dQTZNBrYsEIznIEaZetPJtOkGSgooNk42tgIjL6JMTH-2NFqhvKJkatVQpkUsQCmdoo5h-KuQJTuFh30I7r4pJLvj937raTFBE2UQu3Y3rG5s9NbpxLf_UE_ZmxId5zSnJ_3ZMAY5mr_9b0rw0_yqLyooON_57QB7II3lP_hh22DUnItD6KnYHpMRgGHHe6qpSZhoX9EGVAAaviwVsL9_nzUk6H0t2iqSNIHg0tUK22VNnW1KL-pGeGap1XrBQRFa9G-Pq664w42vR9d4XSRaVp36zQVd88cmjCnFMv6AxtBl4A3_NRDigeHTlPhEJ4cQ6yx88Ld1LOZZopjpdqNIe21PO-60-_2avhGwybFXerdbkDjTDWog00NpOdKJ5EU85yD-jJw1UnbhgR4gDxjhQM4a4daLct3kQhCPcl2F8OkU13fFf0YiowwD5cwEvh1o4bhHufeIy8nDy_mZA1ndqFa_lOccUe2VLhfa89bLMVcZJQM7pgXILj3v4OYsBjuyj4jLf2dUig3S9jSeuWxlQQ71ODkeD7kAjDLcxBidFjJTEGSfIm8GS1xnOgiTD6YpEW0WfZd9HBvJbiKEHlcTY8T4zs1Ubl13fAGVCyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
England is back
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/95187" target="_blank">📅 15:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95186">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce785e516d.mp4?token=E3akmp_EVISHGvemBS8qtlDfdI_590j8R7hEvuY_rSkS_OGEaQKebWtLMP11AAf3fIa6g0NQT_8uQ1SlssWFBPEE1Njjn5DwlxliZGq038nnxnLO7eNaUvTCtBiSiwOoHDW5j1nrVIuG4leHbsojaB4ncCo_n-QGUR4jhvn28KmTAFXGqqiHtntpEHuiy8r8-Vu6wonNANADGm7mfo9R8bEOeThR9Z3G9TaJIWfzffsoPHyq9sHhQEvRMQs0-FrzaSbfcWg8dTGv0JjvdOyX9vGSYRgoUmj6P1O2QDe5IsLXbKEdoZolQFy-fon-Uo86oUPnJj4U3ZGcUn9dIKp1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce785e516d.mp4?token=E3akmp_EVISHGvemBS8qtlDfdI_590j8R7hEvuY_rSkS_OGEaQKebWtLMP11AAf3fIa6g0NQT_8uQ1SlssWFBPEE1Njjn5DwlxliZGq038nnxnLO7eNaUvTCtBiSiwOoHDW5j1nrVIuG4leHbsojaB4ncCo_n-QGUR4jhvn28KmTAFXGqqiHtntpEHuiy8r8-Vu6wonNANADGm7mfo9R8bEOeThR9Z3G9TaJIWfzffsoPHyq9sHhQEvRMQs0-FrzaSbfcWg8dTGv0JjvdOyX9vGSYRgoUmj6P1O2QDe5IsLXbKEdoZolQFy-fon-Uo86oUPnJj4U3ZGcUn9dIKp1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار درخشان شجاع خلیل‌زاده در مقابل بلژیک در ۳۷ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95186" target="_blank">📅 15:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95184">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQ5_b8IZ3B4DjCqPNPq-OMVmfOPcNKGfqUiuAg2rMx94k5_Ixs8V2GcWxsg6RMoT91qoXGsUD-5AACEG9lQ6TED27RdvDC3wByaUe_wXMROW2m2R5wqXvCxQ2geKLWl_soZSfelNuXOusuIiLszfjS01oRkDWWHQk1K1djxwDLAyitEO8L6LL24CMNPk3sTgfOI1fV_NAYCaPdcbU4OSUTqGRUMHGfabDe2rU86NjN3j5dOpsm-Cg7NEpa1tXatabox66bibxhEIvQmaXCah65RxkzT6rRAWJjM-_-1br6-5vGPK_AxYgi4v92v-Uj9qLi1tK3R2mMgeMWG6sWSC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
#دانستنی‌های_کسشر
: کیف رامین رضاییان قبل بازی دیشب از برند Christian Louboutin بوده که ۱۱۲۰۰ درهم قیمت داره که به پول ایران نزدیک به ۵۰۰ میلیون تومن میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/95184" target="_blank">📅 15:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95183">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTm1wmVT8nis8EqJQJQE4sWZ-miwkyFCu210nGUA9yt7DtIvWbYGGQh-wPIqit33rkB6KExB9GbYSsg-JBSAuO9N-RmeT70lDejJpPilJ-wwUukdS06ZIKb75BpUeP5FM8RZur8HHzNNTSaBAphWqMt1PtucdE5a_NOJutM5lEpsMvJ2u_0meM2Ucbdow3rIK6PPne-LE-UCL29g8Iy-iJ9yv_g5BoZvFDkH7Q5wLUjen8etDelEMeILUtxUMGfIndOk7sIEU3NrPjig9DI9eL1Ot5B8a9wavcGThjYhSvjDoiLcUiz-awm1zJK0zszK7UG4IWX-6DakLBPX8rclSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه مسی‌ و رونالدو در شروع جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/95183" target="_blank">📅 15:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95182">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22bcd95a4.mp4?token=NGd0sgat7rYwCBsePxonI7hOqNfjDILUw7ZrjkjdeF8EvTR3h44F7JlnYd_V3cSYq8Hxf81obPAQW0USl2offJ6zYjdpFaI0r0adZmh3EVe69nsdDV8AGtVOTsVKBTqdhm0v2j6p-gm0juOffK3hywuSAvIo-QOHQNyzrwJIRFzsnZgHIBxwx6J5hjkbAqSP9RrvQLEhQFxitKkVnNMihnXiPLib0KBSdGQYAw4YxYgbqjNxGW7rPMaDBaiCKY9W11GePobYMDNo7j3IvBatv3qZLqY2VgR6UgNohUh8eIxVlfEuoCCWg2so9J3BAgtz-HLOkbvZZU7KAtfyq9yOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22bcd95a4.mp4?token=NGd0sgat7rYwCBsePxonI7hOqNfjDILUw7ZrjkjdeF8EvTR3h44F7JlnYd_V3cSYq8Hxf81obPAQW0USl2offJ6zYjdpFaI0r0adZmh3EVe69nsdDV8AGtVOTsVKBTqdhm0v2j6p-gm0juOffK3hywuSAvIo-QOHQNyzrwJIRFzsnZgHIBxwx6J5hjkbAqSP9RrvQLEhQFxitKkVnNMihnXiPLib0KBSdGQYAw4YxYgbqjNxGW7rPMaDBaiCKY9W11GePobYMDNo7j3IvBatv3qZLqY2VgR6UgNohUh8eIxVlfEuoCCWg2so9J3BAgtz-HLOkbvZZU7KAtfyq9yOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇨🇭
سوئیس رو در جام‌جهانی دریابید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/95182" target="_blank">📅 15:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95181">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6Rnzflq7ktFqbDjb4Nzd7IfXltpt1k-sgV4YFHqQ8VYhhHuxr4G7G1YjliRGnuN8haX9lts_5cQ-6z4fD48qrTsvLa0L4Ar61b0L74CGOZyke781EkBw43RIPN20sUFnK9HUmNnfCEUG2clvhCS8IMgoOhVbWqWi7MinQN0RIRtOn3_66IjOMIVMySClz9XqNxzIdwFzunTbfdg4oAUiQUrIZeQzVlStB6FCIiEAEpu5RSbjC8isZRtmmUPHIm4yDGI3Bl_QEmWfDczWcYNKSc4QAcKJHh_oxzXNoGC78xa6X5TgWOrU_ho2khPLgMpNJM8dHE8R_b3yh3TkeTHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایناکی‌پنیا گلر بارسلونا با قراردادی به مدت سه فصل راهی پاناتینایکوس یونان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/95181" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95180">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU0agXfSfNrrcMQ8c4Cja5OpbTbNGyw_3y0Nmd64d2h0J8lvqhiLuwof-OXfh3tJjVfSHi9JYfGrOgtXh_gDhggPXMGRMp1x9RFnm50obGp1X2d_QOZcdUnAqzUykie0m-oU_AIhkvH1TxNJIHr0WGVy44PAB6K4wyricT3m16FAiUjrTK_cSs1vh19hGQ4or-8wCU7Vmo33XYPuJgIlSj2bzL_R5PVCWO7kWmVlKwdrCLg2QPg7tGN_j7gta3pCWAqBFQgsMSXdPszwmYIVee2Exb8pUUiPlFkIoT60R0g06mB87JFiCcSbTuqrSxuAqZoBv9VXa0jxrd3LHQYgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇩🇪
❌
اشلوتلبرگ ستاره خط دفاعی آلمان بدلیل مصدومیت از ناحیه رباط جانبی به مدت سه ماه غایب است و در ادامه جام‌جهانی حضور نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95180" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95179">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzNDqiZe31qo_GT38kIBlrO7_00Mk8JbNkLDbO-r3XsSG-O6bZ2N6MIzrNDlxv5rvkzBMUSGEvg_330t3ezyqqVly6VZZLSmEJ_o0jsboKRkbgSZxlRC0cMA_Pfe78U6_CbYMsBUI-u6m-LQy3ud2H5tuhQw2pFc-HnPflbLyXdMV0WyD38Q4vIIL_nwyobrOPf5Yp8IMZBsbEmh75psClpbcbTy9qTlVvTehNCZRoyoteQyHJ10yy6jloL-njEzz4IpBIXn-F1gDffXxSGmeK6GtITTqwjLwu5XJdmj7rQu96G54QwmBrYBJGiqa9mRFNWgF9ERyp3aPrefLFscsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
لحظاتی قبل جی‌دی ونس در کنفرانس خبری خود اعلام کرد که ایران موافقت کرده است که بازرسان آژانس بین‌المللی انرژی اتمی را به کشور بازگرداند. او همچنین گفت بازرسان هسته‌ای احتمالاً این هفته کار خود را آغاز خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95179" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95178">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIg7lsdxlfcYgmlTc023FdwXt5EBFDTgsl91Cv7VpCmRKqpbyyHucnDaH58O0fCJVMQLXbFMwqghL-hNVeaKzwUIhttgoJuLeTQpec5Fiqi8ZhKGZf28JTlkWBaagDC4IpLTD7j0M-hcgZUgmCsbTF5nTI3TIFK2hThMi_8cmMxlUHj67RXC8tFasLC4IqHbxsaOZMfcpfCTUUEIFVpG35GXoZnvr4MOQm25XrsPlgc19zf-fzFmpdSkc-DH1GzGKzHKGZjZzRX9M2KwtUbwQKDbqvvOLPKC9QXTxa48sVwuzE5d5HAtY2B--RfJL3K1zfk4V7K2uiGwVLsq4eSEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود بر اسلوت کبیر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95178" target="_blank">📅 14:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95177">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh_ZKJ4fPAR1QaftwRYWqAd7UAWHQ2xtA_uFGtQ2pTCoEtbxnEZ3WoctUTkc0nlX2BHh8JqJW4YwuudOVx6kVXbU0fml7CRqenO-UNSI3FI6NyS9MhUVC4F4cpvhDuP6_d3FrFJZXGMWibeDg8Q5CaQA7yy7pit6pCpTMZcrszjFeBIkRW8AMgsFSrdUSRDSwtZs1SXZ_crthojZmhcJlSHZdBlscD8lbPZNZVHUTa_epr6sDeNpYHUShjoXJ7kmw4_86W10yQfJ1vbEEFADiXHEqEyvRRQ4AEzZUvKu221VREcXc0916BGWZrI3Y_WxlY6swCGPLFEOWatKG6Dtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرناندو پولو: خریدهای رئال مادرید در این تابستان:
• برناردو سیلوا
• کوناته
• دومفریس
• کوکوریا
همه آن‌ها خودشان را به بارسلونا پیشنهاد داده بودند. باشگاه بارسلونا آن‌ها را رد کرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95177" target="_blank">📅 14:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95176">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13fdaf80ae.mp4?token=JhV-AZSmEVUF5RusolVmlhCgQEcZuJPuUk-FD6P_tzS5JQ-Rh1sM7FgLX6dalDO_rCF5woU1VsKUdkQsPmJWx3GRB8vUvqvy2SHdcY5JFnCvRqYb6MPMFhR9bo7YfwIN6-lzk3ZD0h_WUJMRXqgZFOfID97erTuARy6Gdj6eJH7TQijhdlP2gNIEplygxAuj88Bqi7i93STp1Vo1HRY0Jtjco9o2SEb4ikKRm9AbS--7hVyutPPCIOGtLvxYE5Xhf89ITamSU5aSv_Ms1iMMw5G7o5QOQAo_tDAgQiJuCEpuOfQj2io2R1bLNKeTakwYQ0zMM8bTEu4yT23f9rl_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13fdaf80ae.mp4?token=JhV-AZSmEVUF5RusolVmlhCgQEcZuJPuUk-FD6P_tzS5JQ-Rh1sM7FgLX6dalDO_rCF5woU1VsKUdkQsPmJWx3GRB8vUvqvy2SHdcY5JFnCvRqYb6MPMFhR9bo7YfwIN6-lzk3ZD0h_WUJMRXqgZFOfID97erTuARy6Gdj6eJH7TQijhdlP2gNIEplygxAuj88Bqi7i93STp1Vo1HRY0Jtjco9o2SEb4ikKRm9AbS--7hVyutPPCIOGtLvxYE5Xhf89ITamSU5aSv_Ms1iMMw5G7o5QOQAo_tDAgQiJuCEpuOfQj2io2R1bLNKeTakwYQ0zMM8bTEu4yT23f9rl_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
انتخاب تعدادی از مردم بین پول و صعود ایران به مراحل پایانی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/95176" target="_blank">📅 14:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95175">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLhNTCxm9326leyqn7XqNt5NdYLYYROCUsLP3u5_8s3GhKTwO-0BsmqjsfNuj4c8SC0hr_qYgvTZAFxgw0nVld0aOLiVyCVqJwfI4iKdqUtmql_9KCqEQPhp5M5I7aZRhV6dBfpPkAUkYD0RIVqd3IHsujxapfEalGfwMX4W7TfhB1dSz-ued022O_pU9zojmn4xutDI322EbrI3-PNb1CmBh1kck-xr-yQKkxKqRYzDPGOhj_-oyifUm8wV2zpKuvfgTa1z9DqM3-0cpWfXQ5ij9d0tMIAVp6PjwqR7YDE0dhuFA52cYNA3NaOPzpzFHTQUYU7lm15K8jtRtlpGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
📊
لیونل‌مسی امروز آخرین بازی خود را در سن ۳۸ سالگی انجام خواهد داد..
❤️
🚨
🚨
آمار افسانه تاریخ فوتبال در سن ۳۸ سالگی:
‏- ۴۹ بازی.
🏟️
‏- ۴۸ گل.
⚽️
‏- ۳۰ پاس گل.
🔴
‏- ۷۸ اثرگذاری مستقیم.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95175" target="_blank">📅 14:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95174">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e16e4dfd.mp4?token=D3a1SKbY6CFYx8tC02GZECsROZLPjMB20IjEQtJfocWgisJ3IZ8F6CTm98FooAsFgMsaAyWkhXbADycVs3jll31uNZb4_cAQ-TkKqzIffmBQ5n4eA8TZ77d2unPT3KDW23ujI7x0QZSQldt-qEjUmOdjEJr7DTfP1beJV33Wq4FlWqwS9f3LXVxq16ONS3VRVb7BD79UabOlxhJLLiepJEEGjMIlcwZMyS1CmgLMsHW3rIw39ipSdRc_wgrHkQPyCMjbawRvUsLgwqeUVMfv6P_3y7QUXHSuqQjS9Zt10wMD9b2hmvI7_t7i5OPN6OimOM8sI4XwO8zHbwyT_5nF9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e16e4dfd.mp4?token=D3a1SKbY6CFYx8tC02GZECsROZLPjMB20IjEQtJfocWgisJ3IZ8F6CTm98FooAsFgMsaAyWkhXbADycVs3jll31uNZb4_cAQ-TkKqzIffmBQ5n4eA8TZ77d2unPT3KDW23ujI7x0QZSQldt-qEjUmOdjEJr7DTfP1beJV33Wq4FlWqwS9f3LXVxq16ONS3VRVb7BD79UabOlxhJLLiepJEEGjMIlcwZMyS1CmgLMsHW3rIw39ipSdRc_wgrHkQPyCMjbawRvUsLgwqeUVMfv6P_3y7QUXHSuqQjS9Zt10wMD9b2hmvI7_t7i5OPN6OimOM8sI4XwO8zHbwyT_5nF9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😬
👀
واکنش دکی به گل ایران که نمیدونست آفساید شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95174" target="_blank">📅 14:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95173">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc9b9ff0e.mp4?token=cskflG7yXFP41nfUu8X7TlFR-SXPLTuRifapCKrF4MIxcs3VJ7A--awAc1iAwGYlYoPfmwOy0RtCdtyWhihS9EfZDfWoKCGDIH9TNhBxQwXMqzj007QQ_grtXPuDq16PlJMZeY0JZmGjPMzbo31zGX3NZl8QVmt-iIwDzsHsuD-jgZV5TKh8QqgHpJrFZsF-gMwAhlNA6KhI4pmJitFZGsUeRI81NXHdZG73KbC0pq9lGMGJSnFLEIYKDu11esf7ROdJk3YWINbXlyQsZ5wKWOSfR7jWWningcZM3iqPjCEWY6KQTTz2VxbPTOPmiI0EXwDefF44aOnKecLO3Ltzsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc9b9ff0e.mp4?token=cskflG7yXFP41nfUu8X7TlFR-SXPLTuRifapCKrF4MIxcs3VJ7A--awAc1iAwGYlYoPfmwOy0RtCdtyWhihS9EfZDfWoKCGDIH9TNhBxQwXMqzj007QQ_grtXPuDq16PlJMZeY0JZmGjPMzbo31zGX3NZl8QVmt-iIwDzsHsuD-jgZV5TKh8QqgHpJrFZsF-gMwAhlNA6KhI4pmJitFZGsUeRI81NXHdZG73KbC0pq9lGMGJSnFLEIYKDu11esf7ROdJk3YWINbXlyQsZ5wKWOSfR7jWWningcZM3iqPjCEWY6KQTTz2VxbPTOPmiI0EXwDefF44aOnKecLO3Ltzsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
علت تفاوت بیرانوند در بازی بلژیک و نیوزیلند:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/95173" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95171" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/95170" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9JtOge28jFxL65ijOPBvD1NDFF9xaagooCut-_i7bKy7OCYYDU3SR-V2uWeNf5YxMRFZlUX_HG2e-tGhnLO3VhJMHUjk1eYvikMyjuVFFys5iGhq01H9o56BtgKeNAOLiywOL1II2IfKw6u-4kYUHxbM3d2GWtyyDVeCekL-17k8GJ_FqBQhfLGJQeFidwzBGcHmK4FHckSasM4_Mlr63dH9TOgc4U_4wm6Q9hvkK3E_PQTo-JWt3ru40WuJSTiwKnTQ-ojX7_q2MriTDnSfE2MZRwQDlwb8I83F3PrrMsci6HMvvIBS1Z2IZPP8XfpCfvOQUbxlC5USFGprf3vmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇯🇵
پیشرفت چشمگیر فوتبال ژاپن در دهه‌اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95169" target="_blank">📅 14:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzS7Ze1nn_3aEXK_-JH9L7HHrC5STCbP1vavJ1QuSFvRNipCdA8u5jkc5fEEo3FVoQPKQ0x7Xmd7wKn5LAyj7jMQGQmq43HX-4_cHFeW2asPTIm7fm02hOm12u8DVhGItoU-S88m2q_hVE2PKDlZOyEkic_70jk523d5gEZ8OxNeIsRISui3UjOj4HEdH7V3zXF_z1hFI40rV9ZufPJQUFJmlcv---_p_6f9yenbPo9f_-Rpgik_qDYo6wT1tuQQsrlV3LlmbkZR7c6E1oQCejWvL44UFhKwBGUUs55M5_cbr6kGahRFEivWanpZxlRqTbzbWKXlAAiuzixD9JtX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔺
اسپورت:
بارسلونا گزینه جذب کین رو به عنوان جایگزین در صورت شکست معامله آلوارز بررسی کرد اما کین تو بایرن خوشحاله و نمیخواد جدا بشه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95168" target="_blank">📅 14:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0a1fb2cc.mp4?token=VjWAGFATy5BTPqiE31VTUGrbn7NHeUsFEo76tOQrQ6cLgZVMx29qT2Aaw7ggVDOsWmf9xQ_Yr-aMmIIbZEvQscSgJDmtAEM0Gzx0a5If3et7-K6_0Lrs22qagkT2Eso38ClMijsVHVZco_3J9BRmEMBvSANUqXYWld4GGDfHT3sh0m-SiFJ7NVoQYdHAYGCoHfC9TfiEVhGaLOWZaspbIfW0297QYrk5NNKbLgmY4Vyf13gp7eqekclRJmVILV2j1FNc35fZM5sSoqfi9cyKreAomr0t5aoyCnJh1qspCJnmtOmU-o9uuVKkYNgN4d36YH5jz0BXCgZT4qo_hpLNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0a1fb2cc.mp4?token=VjWAGFATy5BTPqiE31VTUGrbn7NHeUsFEo76tOQrQ6cLgZVMx29qT2Aaw7ggVDOsWmf9xQ_Yr-aMmIIbZEvQscSgJDmtAEM0Gzx0a5If3et7-K6_0Lrs22qagkT2Eso38ClMijsVHVZco_3J9BRmEMBvSANUqXYWld4GGDfHT3sh0m-SiFJ7NVoQYdHAYGCoHfC9TfiEVhGaLOWZaspbIfW0297QYrk5NNKbLgmY4Vyf13gp7eqekclRJmVILV2j1FNc35fZM5sSoqfi9cyKreAomr0t5aoyCnJh1qspCJnmtOmU-o9uuVKkYNgN4d36YH5jz0BXCgZT4qo_hpLNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
درخواست سیگار برگ هوادار مارادونا از خلعتبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95167" target="_blank">📅 14:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b2bd55cf.mp4?token=HlfQdU7yBArqxa86dzUujLJlZS__D89TkASSAAK3l24wilx1TB8PdMVbVYS4Eul5IRl9OYt7KjVKGbqG8QL5ezIDnE_kiPl3tHiWta6Xwl7B_x8THuMolrFiu4mILc1swi9CO1H4y4TgjyWPZgXVIbSUU-jLXVyY_riQURNaNRq-kB4QWHVJrLUFz_xzV9D5wEh5fC1Pth23nflxr3FB-yoBScta12KpfmL8nuJcOANsiqVZr13FSlYW9R3uZvN9h1B9bmbgZ-A4Q8mcUSA9zZtkfkmWJ2bOt5HyUG0_pR0BdLyux9H4f0qOIi7UekPFxTLk6kqL378V15rh4wl_Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b2bd55cf.mp4?token=HlfQdU7yBArqxa86dzUujLJlZS__D89TkASSAAK3l24wilx1TB8PdMVbVYS4Eul5IRl9OYt7KjVKGbqG8QL5ezIDnE_kiPl3tHiWta6Xwl7B_x8THuMolrFiu4mILc1swi9CO1H4y4TgjyWPZgXVIbSUU-jLXVyY_riQURNaNRq-kB4QWHVJrLUFz_xzV9D5wEh5fC1Pth23nflxr3FB-yoBScta12KpfmL8nuJcOANsiqVZr13FSlYW9R3uZvN9h1B9bmbgZ-A4Q8mcUSA9zZtkfkmWJ2bOt5HyUG0_pR0BdLyux9H4f0qOIi7UekPFxTLk6kqL378V15rh4wl_Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتخاب سختتتت بین تماشای فوتبال و ..؟
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95166" target="_blank">📅 13:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd7adc8564.mp4?token=Ah-9GsM-nk4VuWTI1l_qLEi5IjFpdA4LiNP5oiUG3FoJxOnCRuqrobTt5SlC0qD3PF83mmt4UeQ-SbCHdQ15Zhh97B-9Xp2sAeOB9xs34jqlYtuA4CJyjDL4pyn6RenuKzesBcytBzrLjo9MN-T9p3oRa6Z1_09SmVLC0W-wEO6_AIRXR_a0S1dUb1KdFsEODLfHoDZSbpYyUFWzlLjS7yc2h2O3KQMapJfXvXx9sABG_fzE1d9Bo-HmeG5FTMNwjbudEdKrmcrWwEXIHBdKwmHNo0NlVUvRLXTV5--1XibwsO0aX5czvuXztcIRN51AML28yndJS4kE9hzcWFPXrDqqsEXngopx5OB9qX0VYEN_9CUzE4K6BWBZTKFJeo3bD3gm3u4gWWF4FsIBfqmpvWqRHvjInE5QlIRv1Yfiwdc9qftlMHN7QqtZMKw7AUxOQMvV1XaoyP5XIBtGt1jy1ghDpHogZt-Osg5X_JHPm2FUAjD_R8ztZBp2nSQ7mjy3IV1HtoOn6t8lCv27-vmsoqZJC4BPbZlNDR8zmCx5BG2ZQKPpSaFIqmCnMLRBJ_wFOeIWWYJpyX8Cr-kaJx24YOAxZW4BWN0DoVtIwFOy9RxlElB9SfWLZECKy0tiLN0RGlP8NmNtPxLfSYOjrlZaV3kAjbkzOn8UeAipG8j7XdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd7adc8564.mp4?token=Ah-9GsM-nk4VuWTI1l_qLEi5IjFpdA4LiNP5oiUG3FoJxOnCRuqrobTt5SlC0qD3PF83mmt4UeQ-SbCHdQ15Zhh97B-9Xp2sAeOB9xs34jqlYtuA4CJyjDL4pyn6RenuKzesBcytBzrLjo9MN-T9p3oRa6Z1_09SmVLC0W-wEO6_AIRXR_a0S1dUb1KdFsEODLfHoDZSbpYyUFWzlLjS7yc2h2O3KQMapJfXvXx9sABG_fzE1d9Bo-HmeG5FTMNwjbudEdKrmcrWwEXIHBdKwmHNo0NlVUvRLXTV5--1XibwsO0aX5czvuXztcIRN51AML28yndJS4kE9hzcWFPXrDqqsEXngopx5OB9qX0VYEN_9CUzE4K6BWBZTKFJeo3bD3gm3u4gWWF4FsIBfqmpvWqRHvjInE5QlIRv1Yfiwdc9qftlMHN7QqtZMKw7AUxOQMvV1XaoyP5XIBtGt1jy1ghDpHogZt-Osg5X_JHPm2FUAjD_R8ztZBp2nSQ7mjy3IV1HtoOn6t8lCv27-vmsoqZJC4BPbZlNDR8zmCx5BG2ZQKPpSaFIqmCnMLRBJ_wFOeIWWYJpyX8Cr-kaJx24YOAxZW4BWN0DoVtIwFOy9RxlElB9SfWLZECKy0tiLN0RGlP8NmNtPxLfSYOjrlZaV3kAjbkzOn8UeAipG8j7XdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
مروری بر تاریخچه آدامس‌خروس‌نشان به عنوان اولین‌ اسپانسر ایران در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95165" target="_blank">📅 13:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c27b7293.mp4?token=a-JbVFfjIRcabHlfXL5VGFPqkUDLR0wlOb4PNkzQaBA73jO06EJ3TM0J87xSlrq3JKlB0RJZsafVaLrCWpgKP1f8WOzb6ygald8UzhCNPmksUrNWIILxWOzMzttfBmctL8R15XOH5P82h6kNQm4fZJDF7MgSVmkV5sRr6bfVv2F1bnx6_WXangsUkqsiVBKaDGdrOkpcL7Nx4fk5ghNMH1PTv77NEpAHgt_xbouBOXy4EG21tcb7j9FzEt9wTwrIo-04CJzQ1KSdcks3fHmVxMJ2cvvGpKmJYMSCl4axG4ZvWIKvBM01cqC3bi9-kmPFYfX6fbR4-1_FusczjH_GXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c27b7293.mp4?token=a-JbVFfjIRcabHlfXL5VGFPqkUDLR0wlOb4PNkzQaBA73jO06EJ3TM0J87xSlrq3JKlB0RJZsafVaLrCWpgKP1f8WOzb6ygald8UzhCNPmksUrNWIILxWOzMzttfBmctL8R15XOH5P82h6kNQm4fZJDF7MgSVmkV5sRr6bfVv2F1bnx6_WXangsUkqsiVBKaDGdrOkpcL7Nx4fk5ghNMH1PTv77NEpAHgt_xbouBOXy4EG21tcb7j9FzEt9wTwrIo-04CJzQ1KSdcks3fHmVxMJ2cvvGpKmJYMSCl4axG4ZvWIKvBM01cqC3bi9-kmPFYfX6fbR4-1_FusczjH_GXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشاورز بوشهری که با «قبر مارادونا» در حیاط خانه‌اش خبرساز شد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95164" target="_blank">📅 13:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077ba9b0fe.mp4?token=UTQDOjK4FG-ioUx7q1FIDV6rhgwffc1kKjmJ2XiYuHv7M9wEN32SUOIsFs0t0N7LeEKJWfj6iCHwOATPPwj8a57eKGxUPC8oIq9lUW_KKQjvgnWm7iM3d-Df8op-flSAkIl26usnzZdep3ViSRbmp8iEMW853QKSBE-RgW0TAegaj82WAW1XE-a0t-IBkbEaVMHCuVd__gHjNhLaZXRil8tULcT_i9QDRInbXOqaH6iiE2g9vtM0yHH7wJldGIgo2xnp75njqTRIvoGcrCw-529Kjo_fIf5Nbwnb5h0hlLX4MN0QxKKyU3zYYShyVNl3axuVT_MrU8CX4odMIzeVCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077ba9b0fe.mp4?token=UTQDOjK4FG-ioUx7q1FIDV6rhgwffc1kKjmJ2XiYuHv7M9wEN32SUOIsFs0t0N7LeEKJWfj6iCHwOATPPwj8a57eKGxUPC8oIq9lUW_KKQjvgnWm7iM3d-Df8op-flSAkIl26usnzZdep3ViSRbmp8iEMW853QKSBE-RgW0TAegaj82WAW1XE-a0t-IBkbEaVMHCuVd__gHjNhLaZXRil8tULcT_i9QDRInbXOqaH6iiE2g9vtM0yHH7wJldGIgo2xnp75njqTRIvoGcrCw-529Kjo_fIf5Nbwnb5h0hlLX4MN0QxKKyU3zYYShyVNl3axuVT_MrU8CX4odMIzeVCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارا قبل گل داشتن شعار بیشرف بیشرف میدادن، موقع گل خوشحالی کردن، وقتی آفساید شد، بازم خوشحالی کردن! ایرانی جماعت همینقدر بلاتکلیفه و مشخص نیست با خودش چند چنده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/95163" target="_blank">📅 12:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d2cfcb46.mp4?token=A6XXZPmQN8JGS5AxiX18hrVCg2D_bDItoBkBKclx48PJz18ZRF3PiCBuHBDdDghjvTXXYr2ZwWMKTtPYdeIWax6Omy1Z6EEg3pJ7D0jn3rYgb0i5mp4sG22LvQhYzAusvH-NF_2oUgZAhl4bCHLx3BH-hXUtI2mZir4uLnbgmcJA-MYpX8-cVx7Pe1aMmM-OQX_HxlMHXFUuNRi3WLO3QnszS0Feo352JAt6iC1A6fh0ijiwbOp84zaiHk9UJSAO80mIBSm5KKTZdWVIgHf3XI8V23VHT5n-rgC28z1fl7LhvqcImOR-dXabmr4Yjj_y0GBzF3e3Isb3Fc3QfqJDGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d2cfcb46.mp4?token=A6XXZPmQN8JGS5AxiX18hrVCg2D_bDItoBkBKclx48PJz18ZRF3PiCBuHBDdDghjvTXXYr2ZwWMKTtPYdeIWax6Omy1Z6EEg3pJ7D0jn3rYgb0i5mp4sG22LvQhYzAusvH-NF_2oUgZAhl4bCHLx3BH-hXUtI2mZir4uLnbgmcJA-MYpX8-cVx7Pe1aMmM-OQX_HxlMHXFUuNRi3WLO3QnszS0Feo352JAt6iC1A6fh0ijiwbOp84zaiHk9UJSAO80mIBSm5KKTZdWVIgHf3XI8V23VHT5n-rgC28z1fl7LhvqcImOR-dXabmr4Yjj_y0GBzF3e3Isb3Fc3QfqJDGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
هوادار ایرانی در بازی دیشب با بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/95162" target="_blank">📅 12:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca35f6f9c9.mp4?token=b4i_CY4Tc7ToglMyIB6O4bR1jNFZF228FMAxNH8DQDldhXb6GUnv5UDWcjeh7CdekKhg238XdG-RA4hL7kbN96Ym8_9BJmSqpB-tRvlDuVYv0P3sua51z3NNd8PAa_uOCif4P_QgPZOy5K5kiOc_Qo8NAE0DAWI8s55HzoJwskBelulE-4e-PYwvYf1OBBX5GlM97Vc57pp_jqOFc0VttsTiOYynzdL0CttGv7flVdKMo_w8ENngeWxArwQET1jOqJNdH3OKsHYzEQBxr-bnM4me9aXI12N_8U5_2veYvikVceTeJbQmzp-TzXFD8LMnuCB0DkfNnNJt7cCVCGr1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca35f6f9c9.mp4?token=b4i_CY4Tc7ToglMyIB6O4bR1jNFZF228FMAxNH8DQDldhXb6GUnv5UDWcjeh7CdekKhg238XdG-RA4hL7kbN96Ym8_9BJmSqpB-tRvlDuVYv0P3sua51z3NNd8PAa_uOCif4P_QgPZOy5K5kiOc_Qo8NAE0DAWI8s55HzoJwskBelulE-4e-PYwvYf1OBBX5GlM97Vc57pp_jqOFc0VttsTiOYynzdL0CttGv7flVdKMo_w8ENngeWxArwQET1jOqJNdH3OKsHYzEQBxr-bnM4me9aXI12N_8U5_2veYvikVceTeJbQmzp-TzXFD8LMnuCB0DkfNnNJt7cCVCGr1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حتی اگه مسی هم باشیِ، دلیل نمیشه که به تراپی و مشاوره با روانشناس نیاز نداشته باشی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/95161" target="_blank">📅 12:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0820af51af.mp4?token=DqdW3t94Gt5tdSKuYv_FyRUOUkFTi2duvxsSiq_TjiHhUgaa5-JTOnDq4mAdQ6SXsROL3xVXAKBdYnFNO1IZsFpQmib7WKW-n82FNwHu1PyhUaqjOACOPILY2DiI0Ld-766PVzdm4uzVpQ3qnep5b4VpMph8H6AV3yobO22rcHx0pHScysU6-PNfP1hA8w8mrh-O4Urbk-C3B9MLlXUpOrIKxJlXZ3hs-PxmiY3M6Ij5V01fLILz0m78Q-HHAaH86Q0KM1lFihJiTvp2JxU2-I6xLI29-gQTmXjuSnN4skuP_di6w4FOu8uTtBIPWg9UPv9v1C87ustvmnndhJkrRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0820af51af.mp4?token=DqdW3t94Gt5tdSKuYv_FyRUOUkFTi2duvxsSiq_TjiHhUgaa5-JTOnDq4mAdQ6SXsROL3xVXAKBdYnFNO1IZsFpQmib7WKW-n82FNwHu1PyhUaqjOACOPILY2DiI0Ld-766PVzdm4uzVpQ3qnep5b4VpMph8H6AV3yobO22rcHx0pHScysU6-PNfP1hA8w8mrh-O4Urbk-C3B9MLlXUpOrIKxJlXZ3hs-PxmiY3M6Ij5V01fLILz0m78Q-HHAaH86Q0KM1lFihJiTvp2JxU2-I6xLI29-gQTmXjuSnN4skuP_di6w4FOu8uTtBIPWg9UPv9v1C87ustvmnndhJkrRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
آرژانتینی‌ها آماده دومین‌بازی امشب تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/95160" target="_blank">📅 12:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJdgEJ60kVGQzR3JG2-UvdxphlbL_Jwd3S3naBK-MMKV7VGOWD0DIR7oUAX-Zbw0ndJJflK7PM-s-oXxH0GYG0V7r1WBzAzkCCbTdZVxXEnO3V0N6NsyMNy1Arkwt4GiHD4MLHnZfjh7MXb-HOXsHMy7l9bg83EGrk83XOxoxbYSoyJrVyjrfgWexVGtH9hb1gcCwnqy2i9nrMPDlxogoWKRyazofoO7fwnS_DMZFzCnVeP2NOmHSIoZGssmlavPpAk9DEijvAJ7ou1WPhVEBKIvfhpfIq9yNgltPhsa1boQHDGIQqFzrkWmmHzaH0X848vm_gnJBBrcdNV82-mt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرناندو بولو |
جولیان آلوارز خودش را برای برداشتن قدم نهایی آماده می‌کند و در حال بررسی بهترین زمان برای اعلام رسمی علاقه‌اش به انتقال به بارسلونا است. داخل باشگاه انتظار دارند آلوارز به‌زودی با یک مصاحبه یا اظهارنظر، سکوتش را بشکند و همه را غافلگیر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95159" target="_blank">📅 11:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">▶️
👀
وضعیت یکی‌از کافه‌های شاندیز دیشب سر صحنه گل مردود طارمی به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/95158" target="_blank">📅 11:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAu8jIGAoMeoS9qWD7oF1DULYF2dFgs4ZeEWuskJI8anurJ_GUinUSWf_pLC7q-dTg1wNNwejYOIcS_23YBZUgC6olDBfwCoUNxn_xO0RRAJnLM9bOHqpxqFmB76SKVqLGqtqf7PluXuUwNyiY7ojJsvBxVy0waL5_hJojS7XaD0gwoRXlE34ObHXyK2D7KuEF1_Ho7UNr1vwc7agYJjFRhp_OvIQQRWh1QFgHcFrSxoAeo_RzoJ0rve5cKFVrr91DorymMnQ6LOZfrF-hfwcRKhhqdaWRA4h75jfLDt_2K1EZ1DOT50y-6_BFmUVwi7hhMoyQy5VWZPe4zg439ezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
مسابقه فرانسه
🇫🇷
عراق
🇮🇶
بیش از هر زمان دیگری به دلیل شرایط جوی سخت پیش‌بینی شده تهدید می‌شود!!!!!
⛈️
انتظار می‌رود از ساعت ۲:۰۰ بعدازظهر تا ۷:۰۰ عصر رعد و برق ببارد، در حالی که مسابقه ساعت ۵:۰۰ عصر به وقت محلی آغاز می‌شود.
و امروز در منطقه فیلادلفیا ایالات متحده انتظار می‌رود:
▪️
رعد و برق شدید
▪️
بادهای مخرب
▪️
رعد و برق و صاعقه شدید
▪️
احتمال وقوع گردباد محلی محدود
▪️
باران شدید که ممکن است باعث سیلاب ناگهانی شود
⚠️
طبق قوانین: در صورت مشاهده هرگونه صاعقه در فاصله ۱۳ کیلومتری از ورزشگاه، بازی حداقل به مدت ۳۰ دقیقه متوقف خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/95157" target="_blank">📅 11:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95156">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda9868a88.mp4?token=tgwXcmwfuKOjmPvpJ9U2Wy7ayM2XX3JFHgr3hed57v8WRr6Mo-u_90x9UQ0VW86d3fUBsjkW7My0Ztz5A-1h5bL9aiFPQJCGOxp0Sc2TVaj82jXTIP1AE7reisrRtpd4JEq2zEbAelyxjWOD_QRq3gSGNrItdTx1pT79hqkmUXg_oU7kyHtmxbKejhxsTZhcyxepfRIKAFv0MPcSMRxAXtppwjiOLF-ebCqXP3qiT4LG6AyiLOQD8Iy0ms_d03STJnnSKUOHZiYCBSvGLYFpDBUs0BkkaVnZUZSi89p9KQp6beJZ2-fYeg80k4_oLI-XVlJevt0z3cXQpD-edQ2Rbl1DnvtRcaStaRGA9I_LFxZOL2q49B6Fw874LZO590_KRYmNtPsTqmc2vUNelw7VwVNt7GczP7aCMMOhxTYlirBeHcwplkUlZ0iTzMt4ah-vblzaG5Fb6G1_3Pc_0XI50863CgADH5oIZXSTbYwAX0MqehfnvdwlJg3qcq8ZNYUqQPDbq0NkfZPWvMVnQds7uuMfc-H79D6IpwGi0VyHDq7fuxIH7R6igb3oB58CKhOV7Bo7g0yWmgrW_5IUny796iBThQIZhp4DQSodSAC6Fg3VxWsca55b8257VjpZl0dP12gyY22ykqCJychH9vuI23JcfkpJYFlu1rCBHfrQJ6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda9868a88.mp4?token=tgwXcmwfuKOjmPvpJ9U2Wy7ayM2XX3JFHgr3hed57v8WRr6Mo-u_90x9UQ0VW86d3fUBsjkW7My0Ztz5A-1h5bL9aiFPQJCGOxp0Sc2TVaj82jXTIP1AE7reisrRtpd4JEq2zEbAelyxjWOD_QRq3gSGNrItdTx1pT79hqkmUXg_oU7kyHtmxbKejhxsTZhcyxepfRIKAFv0MPcSMRxAXtppwjiOLF-ebCqXP3qiT4LG6AyiLOQD8Iy0ms_d03STJnnSKUOHZiYCBSvGLYFpDBUs0BkkaVnZUZSi89p9KQp6beJZ2-fYeg80k4_oLI-XVlJevt0z3cXQpD-edQ2Rbl1DnvtRcaStaRGA9I_LFxZOL2q49B6Fw874LZO590_KRYmNtPsTqmc2vUNelw7VwVNt7GczP7aCMMOhxTYlirBeHcwplkUlZ0iTzMt4ah-vblzaG5Fb6G1_3Pc_0XI50863CgADH5oIZXSTbYwAX0MqehfnvdwlJg3qcq8ZNYUqQPDbq0NkfZPWvMVnQds7uuMfc-H79D6IpwGi0VyHDq7fuxIH7R6igb3oB58CKhOV7Bo7g0yWmgrW_5IUny796iBThQIZhp4DQSodSAC6Fg3VxWsca55b8257VjpZl0dP12gyY22ykqCJychH9vuI23JcfkpJYFlu1rCBHfrQJ6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
ادای احترام به رشید مظاهری در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/95156" target="_blank">📅 11:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95155">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFtNUBRmcPmY2yRuB3jkbf4hvo6aQziwiD430OjAW7os_4by4EoXH65LntqRzBGRB6nAqJ6ngg8FZgQb142xbv-ZptKLD7tJWey3oiFYAqaQbVhZoyidDlU5vThs0uWUoB4OL4281HB0V6M_pGAcpTl-HbM2sxxEnW8D8z9fMKwA8BJNO-vM-WwOsY1ZeTFuzEb2pLC7bXOMLzcN-iuNAtvjz5-4iS_8maIOrLVx-slgUqpKbxtJ8BzkAbsGMDxyVdQ8aTXOck5i3PY8bel5WY8_ZvvyPo516FbVqCncykgCUR_bJzhN--PGrmVm-pgg2Bl8MxsBLqxWZZScfCG9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولو شیرا:
تاتنهام در حال آماده سازی پیشنهادی 100 میلیون یورویی برای ساندرو تونالی است
منچسترسیتی، آرسنال و منچستریونایتد نیز برای جذب هافبک ایتالیایی در رقابت هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/95155" target="_blank">📅 10:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f33346775.mp4?token=Ohg5cBCYFS1Qh7NcCxMmod9nmhNqfOZHm8J785xRqyZGLXVHJwHQ65SUc7_kmOGrdpETlhCHkh9lQPxzE0wt4CXRk_eZJftyi__rzOYRPHfK-59O0h64TOyULSbJ2dO8JgiQ9g3QWiNc5biQNKEm8yQ0_H3aSYDTE0cD8wE7ljKLImQCUN9sMr2J9c8zukASb9JKadHjimfokdA9e9OdMUmFryhSPhn7lg1fMo57LKxT9L1-9o_fL_3lLPgKPlWUS1Ghhuq1FAAtssBiX7n1LDXylDcPekf66LS8cacgFZ2ueJj-foyipYJT2QXJBu-22cmT-fn913a75zuvd-dsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f33346775.mp4?token=Ohg5cBCYFS1Qh7NcCxMmod9nmhNqfOZHm8J785xRqyZGLXVHJwHQ65SUc7_kmOGrdpETlhCHkh9lQPxzE0wt4CXRk_eZJftyi__rzOYRPHfK-59O0h64TOyULSbJ2dO8JgiQ9g3QWiNc5biQNKEm8yQ0_H3aSYDTE0cD8wE7ljKLImQCUN9sMr2J9c8zukASb9JKadHjimfokdA9e9OdMUmFryhSPhn7lg1fMo57LKxT9L1-9o_fL_3lLPgKPlWUS1Ghhuq1FAAtssBiX7n1LDXylDcPekf66LS8cacgFZ2ueJj-foyipYJT2QXJBu-22cmT-fn913a75zuvd-dsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
امباپه:
«از وقتی فوتبال رو شروع کردم، هر دوره بهمون می‌گفتن باید از یه روشی کپی‌برداری کنیم؛ یه زمان بازی مالکانه بارسلونا، یه زمان خط حمله سه نفره رئال مادرید، یه دوره هم شدت و قدرت بازی بایرن مونیخ، و حالا هم ازمون می‌خوان مثل پرس شدید پاریس سن ژرمن بازی کنیم، پس تیمی که میبره، همیشه الگوی واسه کل دنیای فوتبال میشه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/95154" target="_blank">📅 10:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8977a43dd2.mp4?token=FNJq0nIBbp4c5oKlK_b2pBA1rjyFh-T5DGoaTlUsaqYJch-3r6qVyxxctl2QLd5cZrajhF9zYZ0myLwyWtdfFJXzgBmxmSOxjA1W62RtykjP4B3gTvEV56knuiP9g20KUwtBOWjFOyt8lIq0lsrtqGw4VobHIGPs3wdpsWFwoDoq9xT3DLhgKy_YyfwEBvcSMO2-5-mBPJvIeWYHdJrtnGH5M2Bhg7rGUpHDvikuux-e3NAjE1RxglBbcXfcVu09WPToKiS3l3jDOAUGFWc8kCgY5rkHjS1TTlqrzagWtEih4Jj29vS3AGYiVnBEmPd4KyDORbO5tcuvPD8xp6M0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8977a43dd2.mp4?token=FNJq0nIBbp4c5oKlK_b2pBA1rjyFh-T5DGoaTlUsaqYJch-3r6qVyxxctl2QLd5cZrajhF9zYZ0myLwyWtdfFJXzgBmxmSOxjA1W62RtykjP4B3gTvEV56knuiP9g20KUwtBOWjFOyt8lIq0lsrtqGw4VobHIGPs3wdpsWFwoDoq9xT3DLhgKy_YyfwEBvcSMO2-5-mBPJvIeWYHdJrtnGH5M2Bhg7rGUpHDvikuux-e3NAjE1RxglBbcXfcVu09WPToKiS3l3jDOAUGFWc8kCgY5rkHjS1TTlqrzagWtEih4Jj29vS3AGYiVnBEmPd4KyDORbO5tcuvPD8xp6M0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
شوخی‌های جنسی دو مجری خانوم با نیمار در ویژه برنامه جام‌جهانی یکی از پلتفرم‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/95153" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f153f9102b.mp4?token=g4Wf5ne0hDe9c5Fm-bJyCHG6UxiLARsLqvBYv64B95KBqlMy8za8ujd-Y5KTeF9zzgEh63vFHFCaVlCl4cS7j3jswOoCXrMiGdYaujwMsjN7NV8N2tujshwrS5HncRwWAMs7ngOcfYBfQ0YaOvsUb6PLQZmrwYBgc1NgncTUeudJHK9W_GDXPZqW1oGBQpaf087emJsskXeFotqRU-iJTIuHfAha7_V53-CrRWb2Jbd3_J10Dx4XHccUC4AeoaHkCe2x7sGsGzkTnBGyUYj-YBzU7U1Ap4X0qqyq4C7GvIPuKqUYMZ7Q5yq86nzlzMJBbuoMI0z1lZAFbsvQaIk2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f153f9102b.mp4?token=g4Wf5ne0hDe9c5Fm-bJyCHG6UxiLARsLqvBYv64B95KBqlMy8za8ujd-Y5KTeF9zzgEh63vFHFCaVlCl4cS7j3jswOoCXrMiGdYaujwMsjN7NV8N2tujshwrS5HncRwWAMs7ngOcfYBfQ0YaOvsUb6PLQZmrwYBgc1NgncTUeudJHK9W_GDXPZqW1oGBQpaf087emJsskXeFotqRU-iJTIuHfAha7_V53-CrRWb2Jbd3_J10Dx4XHccUC4AeoaHkCe2x7sGsGzkTnBGyUYj-YBzU7U1Ap4X0qqyq4C7GvIPuKqUYMZ7Q5yq86nzlzMJBbuoMI0z1lZAFbsvQaIk2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇲🇽
مکزیکی‌ها دیگه خیلی تو جام‌جهانی راحت شدن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/95152" target="_blank">📅 10:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226f9c8160.mp4?token=mvojblzs_5wvlAL7y2t5EZlamd_0nROdxexY8Brk6gD8Lat6MMtuKXIdGQOlpbDfE6s-UaZ83rAT8AdunPzybsT_nqXfhQhz-5FY-iw91TpM74XkLmM5qnxTEf0y1d2KsXc24QJiY5Jepep6q8Lp5BXnMZofU4NAcYlmIdbRXPh0cIsDaY2khXxyrtPGaNUv6FUizzUzFMqCJV-7E-qolaMpjEB2yT9-lnGlTSDeM2RyUWD16wfwPcMNkrvkL8UbZ6MdS4exuUNom_tS_njYVnk93Mm8zyWKMwQw-O1mTRZUySOHM_8p0CGZ14rMpugrMsXpzayRucsk-zf1X6moDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226f9c8160.mp4?token=mvojblzs_5wvlAL7y2t5EZlamd_0nROdxexY8Brk6gD8Lat6MMtuKXIdGQOlpbDfE6s-UaZ83rAT8AdunPzybsT_nqXfhQhz-5FY-iw91TpM74XkLmM5qnxTEf0y1d2KsXc24QJiY5Jepep6q8Lp5BXnMZofU4NAcYlmIdbRXPh0cIsDaY2khXxyrtPGaNUv6FUizzUzFMqCJV-7E-qolaMpjEB2yT9-lnGlTSDeM2RyUWD16wfwPcMNkrvkL8UbZ6MdS4exuUNom_tS_njYVnk93Mm8zyWKMwQw-O1mTRZUySOHM_8p0CGZ14rMpugrMsXpzayRucsk-zf1X6moDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
🏆
هوادار ژاپنی بعد گلبارون تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/95151" target="_blank">📅 09:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95150">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpNuZMaiNJO-Lt_ym3YyGaQ6ot4VolpCBygZtF8tgPbWYBCv0fQq5ZCZcHF1-tDVTofcLZtbdoW2VZvrKdnA7p5BghUrTRZK0jvBRQVrY4dgfqegQm5NSNv60t_JbMp-dhVyITWomoYYAgcmO7Wspz5fxyK8qes9DcZZr6oWV4Zjb_PEhpOdQOVNGQl5xM4H-ofx1e7x7jmFQWgl7aDNv5kpcBqpeNagWEZhd0xdBzi85u1U2WEeg1EtZ4380a3vKdMUIXTbjE-YkzN3_IFgkMJbbNrAaDSZm8Vap_wlzOtNfGeSL9umnXg45Iwcp0ZNzcXBp8Rt_Yg91PIOneyt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
پیمان‌معادی دیشب در استادیوم لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/Futball180TV/95150" target="_blank">📅 09:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqtNT5CB90Mstxl0P9JF5Uf68H296Zt_0cRk3aBAOIXBy_xag2EXTzFLxP3BwmaqpUkqJyUZEv0hl7RROQD6PYEk-emSvJNTLcEI6i54ZnkAUBalEyBSD-q1vv4MPf1UyJY_9_63YiA8WY4WQFYWwEw4dVHEagz5hH06QEwtcBRLB5OUedGk9ooKxzANw8LPjBg8JZL_BLLZXaAXOU_OrFkj6PPVD_Hjh0H_tgC_O4xi1FqueImpRvTwkur-RhTjiuzU2wWEyStKjHNUb-BODnJxUqWU93AMvmgXR8W7i1TWqYRd1ZHBfsu7sjyKzEBhAswX4RmWdVTBfUCBRc8EZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👻
به امید صعود تیم مردمی سوئد
🔥
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/95148" target="_blank">📅 09:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3243a4ebbc.mp4?token=J3GiaS-Vqp3vH-veZMik16ldpaImVI60xaMBJJ4LHGMpYboDlK4slU8K0mZKQ_svBejLCHlPpwQUuMgKaoWxhZcpd8gj7hIQeIVMZblUwmIN1Pp_QaoKZp3RndjrfeLRjw2p7m55D5qiBHgv8YZbL8U4CYpJIu2A26Ex21f22AlxtvycVyaoi1J-duPNZHwoo_fvu0zhWx_FvAEXuzfmn45QTh9TPUBM05-IntDQTIQ7rl1IxRpom8uC_67C-iBoAzkXUh9vjjGKHRzKJYz10xZYJu3DHhxDBZCBEO04V4oVgmqWO4Lke18xjgy-eN1YG2TdrszFtyOZ_5EKEUmVpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3243a4ebbc.mp4?token=J3GiaS-Vqp3vH-veZMik16ldpaImVI60xaMBJJ4LHGMpYboDlK4slU8K0mZKQ_svBejLCHlPpwQUuMgKaoWxhZcpd8gj7hIQeIVMZblUwmIN1Pp_QaoKZp3RndjrfeLRjw2p7m55D5qiBHgv8YZbL8U4CYpJIu2A26Ex21f22AlxtvycVyaoi1J-duPNZHwoo_fvu0zhWx_FvAEXuzfmn45QTh9TPUBM05-IntDQTIQ7rl1IxRpom8uC_67C-iBoAzkXUh9vjjGKHRzKJYz10xZYJu3DHhxDBZCBEO04V4oVgmqWO4Lke18xjgy-eN1YG2TdrszFtyOZ_5EKEUmVpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
واکنش صادقانه یه هوادار به بازی دیشب:
❌
❌
❌
❌
❌
صدا کمممم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/Futball180TV/95147" target="_blank">📅 08:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU0IUhZz_dgOhPhB0rTERInTkxMQYrA-SLVxSUwOTIchvSAhG72HImVwyZwHIT6dM5C6Fh0dbxq-PYDG9QZpNGIApqdcJzZiN9Vspkk69gIHWjIIBQ38SRflmtzDdANZMTgDQTvMPmOstFtnDnia2jO8d3vpeK7rWpjms1NGjm-mQQc7REMudPKcTUwAvgVVXTDXtaT1-IIoA-34Qq0qIe6avrDGNWIhMzClAqGMUweZ8HttAdPFD4ftclhwtnCBcHNjMLfZxBVDu7YXnGJE8EC2RwplHhKqIf0o3BnZiYaMbzbSy53N5DtwxjKv4PE_qFfnScEfjiBk9w5IOzNK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇳🇿
🏆
🇪🇬
اسطوره‌صلاح بهترین بازیکن دیدار مصر و نیوزیلند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/Futball180TV/95146" target="_blank">📅 06:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95144">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSK3-_9nXgdV13ewn5q7tCRbtzdzUJTALpFJEVr-bk_rE27JvoPqYWqMVJZxnkLQjTx3DVvFbP4wlUUABYRqxYm6SXnJUBdPembn8gfskqDxizBOWnHEzkDfelsiJgYh2VPjzy3Zb9G2Zks7z55iAI5_8m9DSAVJ6BZrx_HD7W28W8QVKlRYgtYdUhxzVOM-505TgNhKqhQYbU4oP-dbA7ElL1dPk8f9a1BrnAOmSi3IQWue0qu4yqmfNiff32cinVYqY_BLB__iStb1wqGTXQk7pB4BLKrIRPV4-QY8uZUy1iQGPbkaLeJvbpI1HvZ7i9nW6pETcPsRv4qB2WQ_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه G جام‌جهانی با صدرنشینی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/95144" target="_blank">📅 06:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95143">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03ce4f787.mp4?token=JU--7rPWHytOFEfzzDKHxfun3aota707-Q9o8G8RfRzTZmJdXAd8PIiAgK5PTegE3xLXGfvhm1uzojVwfJhVE7FqcbB4Z74qy8gbNxBKktsALA_ni1Ewqsrr-w2g7HgrmNzdeUheHwvw74zcPSdQrvl3YKqvXNca9f-MnhOUfb3TEAFnTSL-1h706UNQjhIJ2YIxFXVzz3-r2UseRYN-odE9KzPjHfXa8Ml07GNhRsqQVUWS4NUowMPWfFtmKRihr6erfyJVU5nHGcfLOuXOTk94i5wWx7dTY0E2JWZ-SyvoZ_fFnluJu6VtcDJ2Qt1LZbXeEq52oqo7Kv80b7L9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03ce4f787.mp4?token=JU--7rPWHytOFEfzzDKHxfun3aota707-Q9o8G8RfRzTZmJdXAd8PIiAgK5PTegE3xLXGfvhm1uzojVwfJhVE7FqcbB4Z74qy8gbNxBKktsALA_ni1Ewqsrr-w2g7HgrmNzdeUheHwvw74zcPSdQrvl3YKqvXNca9f-MnhOUfb3TEAFnTSL-1h706UNQjhIJ2YIxFXVzz3-r2UseRYN-odE9KzPjHfXa8Ml07GNhRsqQVUWS4NUowMPWfFtmKRihr6erfyJVU5nHGcfLOuXOTk94i5wWx7dTY0E2JWZ-SyvoZ_fFnluJu6VtcDJ2Qt1LZbXeEq52oqo7Kv80b7L9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
👀
گل دوم و کامبک مصر مقابل نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/95143" target="_blank">📅 06:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95142">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b497a60b9.mp4?token=MEjJ7B9eWMtH6bCpVapMeIjKOJ44SPH1M5I-65vnV648gWIS-Vi-w-qLafzPZD0LTUg1eEvRGgEVdEnd_5lT3SwrDEMu8x1AE4_pJZzxjVPjH59pY8FxiNpJE25tE5dSXweAd6xb6pTppiGcOM67ZWwAyCzH0Bk4SVngh6aCiaeaNOQh9OezfV6P1CIwZtiOO-ovuhAf7moIUEJL46GBCKoUnULRRV2QrmphFC5d7sGZK4tCXbDEPXvDWl3No8g3H5FTJ3v8g8wb9O3g9aSNkEfU_rdEa3yDdSrAcZg935wMR2sTsbYHH9slF9ipchI3wDUM9MiAUeEwGDDOA4D5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b497a60b9.mp4?token=MEjJ7B9eWMtH6bCpVapMeIjKOJ44SPH1M5I-65vnV648gWIS-Vi-w-qLafzPZD0LTUg1eEvRGgEVdEnd_5lT3SwrDEMu8x1AE4_pJZzxjVPjH59pY8FxiNpJE25tE5dSXweAd6xb6pTppiGcOM67ZWwAyCzH0Bk4SVngh6aCiaeaNOQh9OezfV6P1CIwZtiOO-ovuhAf7moIUEJL46GBCKoUnULRRV2QrmphFC5d7sGZK4tCXbDEPXvDWl3No8g3H5FTJ3v8g8wb9O3g9aSNkEfU_rdEa3yDdSrAcZg935wMR2sTsbYHH9slF9ipchI3wDUM9MiAUeEwGDDOA4D5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇬
گل اول مصر به نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/95142" target="_blank">📅 06:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95141">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/95141" target="_blank">📅 05:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95140">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH-UwkCuaWcBvtihFSN2vN_-MQ-v7ksXRrZbk9RLObnxPd7qMhoktlGfxOQcxR5YVHnYu30WB11iHnHvesHcaiOozXS6HOcwTIBz-kmYtzCa54yx66Idos97T84Wgc66xCKSfFT_m5g72CbUFYneuGHMp1-xrVvs2rKFBBqS3y0RaLnD-yJoB4cQXmhRw-0xTrC-e0YEebeVbIxXcI7A2Q3QeT9OZC4vY5yxiB8EPwZZO3GZwMmbhxeYyWNvWFafM5Fj-Q79Vk24m88wIGjnPbSZyFw5iZXZXdpx7RLLS2FKZGk1razQzugBpCdOs5su7hsqxfBvm1m3dUz54bapwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
#فکت
؛
تعداد فالوورای تیم پین دفاع تیم ملی نیوزیلند از جمعیت کشور نیوزیلند که حدود 5.3 میلیون نفره بیشتر شده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/95140" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95138">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhADNPIBCvIyJRckuMZqlacqGlunrUP9duNSLcrlxive7liZHmqJgF68m942iWtTE2tm-VPeIpFsVQKpZeKopgpMLA-KV7Njc8CYcOHalyRmRoZ8ySVSUyQcWJ5lARGpbhGf5CukjQk9WDnlWgKEiOy850c55Iui6iXXoMr4NsbgyEXWkrj8dj7aYkoC9it82qU1kPTORRTqXqt_wncWqbprNQPpL9JCpL5OT74qHLpF3jQlqXoeR0RuULtG8zRNrjAQY12qzN_x8lu25VwUfkad6fGsii3rdsUXhFKr_xp-1abU9jkHSKvc-Jme4BFw1Bzx0tP_K4r6ErcuIOnd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو محتوای خوابامم همچین چیزیو نمیتونم تصور کنم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/95138" target="_blank">📅 04:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95137">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac61dfc9d.mp4?token=mkRQvnANrh_hqrWP3PdK4hSkpDx5ezdum2WT32vEWbD1Kj44vSM8IfEa95tX0xAq2_Dg1jKlEeQu4UoGmgT2maBTyEGXYC-DpPjyzlHbWqWM7FsNCOoxaxTro2OAzxCyai7rLUCMq0BsWR6Ua2Lrz5CSwUY4ozS8EIiHqDJTr2Kv8uIw4b6jYrr5fBRv4gihhCymiXOK6RduTIqDlfgnQXOAAHV3qmD2323qX9VNpjIjQKjT4yoUDpMaKx8XKEjd9ZhmnM8bY4-qeKEq6TNbw32NfFWf_DU56P10fSeNqhvYBh1gCm1HVrhZSV6R18F70CX05wR_770n_Fql3p7zWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac61dfc9d.mp4?token=mkRQvnANrh_hqrWP3PdK4hSkpDx5ezdum2WT32vEWbD1Kj44vSM8IfEa95tX0xAq2_Dg1jKlEeQu4UoGmgT2maBTyEGXYC-DpPjyzlHbWqWM7FsNCOoxaxTro2OAzxCyai7rLUCMq0BsWR6Ua2Lrz5CSwUY4ozS8EIiHqDJTr2Kv8uIw4b6jYrr5fBRv4gihhCymiXOK6RduTIqDlfgnQXOAAHV3qmD2323qX9VNpjIjQKjT4yoUDpMaKx8XKEjd9ZhmnM8bY4-qeKEq6TNbw32NfFWf_DU56P10fSeNqhvYBh1gCm1HVrhZSV6R18F70CX05wR_770n_Fql3p7zWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
گل اول نیوزیلند به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/95137" target="_blank">📅 04:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95136">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پشمام نیوزیلند زد
😐
😐</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/95136" target="_blank">📅 04:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95135">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/Futball180TV/95135" target="_blank">📅 04:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95134">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بریم برا شروع بازی مصر - نیوزیلند</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/95134" target="_blank">📅 04:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95133">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffe5f74c8.mp4?token=EWfavBedVhQjM7DPaSfHTE8pLWByTDtI3trr5tN6C4oRxImcny29_9UV-UYQ4tl6Uu5sWa5ev5dGxKm-UTwI8QasyrsHx4OIshQupwh0ralbndKlHjftv_sqKFIE1zt72eQJ4O-lNvCwtWOQ_e13ylo_eahcBVsguDyzy3HQDcVD3cy5lH2LvajTFEtgLIqTf5d6cqUact27fogXb7ncxsy-s0ZiOHpPpvn6cOTnCbV8hdJOXP2hPe_R73VMUi0M2nLuz09YwjCOq7sjFVVc0Vu1Rv1GH_e3XwP6dAYGRQHuXqsijx9U2pvyWR8m0oYEoUc5p1OnnoS_X-ka02Vxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffe5f74c8.mp4?token=EWfavBedVhQjM7DPaSfHTE8pLWByTDtI3trr5tN6C4oRxImcny29_9UV-UYQ4tl6Uu5sWa5ev5dGxKm-UTwI8QasyrsHx4OIshQupwh0ralbndKlHjftv_sqKFIE1zt72eQJ4O-lNvCwtWOQ_e13ylo_eahcBVsguDyzy3HQDcVD3cy5lH2LvajTFEtgLIqTf5d6cqUact27fogXb7ncxsy-s0ZiOHpPpvn6cOTnCbV8hdJOXP2hPe_R73VMUi0M2nLuz09YwjCOq7sjFVVc0Vu1Rv1GH_e3XwP6dAYGRQHuXqsijx9U2pvyWR8m0oYEoUc5p1OnnoS_X-ka02Vxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
واکنش کنعانی به گل آفساید طارمی: اینقدرت تو آفساید بود
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/95133" target="_blank">📅 04:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95132">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWFLHLY06BcfWh27dXosvBAPEeDnbF1Gu2Gcy77ZR8E-jW-G9sPEBAy4SZ459Uh9Ro67TbQVEZRdMDhZMSGPwafIngQZC9f8XFpSzOiWylHjPKluR5bb3hyMTLI20WQ5NuX6et9UjsVdrPpq94c8l4Z_c0iqF4hKQOBEduDoEpHj9VFEUyvb0BlXU_g7zss5dTqfKFqzjYDXcLiamocdCAlkF6WORHkDO_MEGUj_PHvY549qWOymZ0Nu5EFBShGTy9yWyzrDOeUGkIHk335lGoKWWTHtB1RIsKuoon9t_wPhwT8lEUNh57ThONZdcENr8qRpx4HlxsvTqUYCsEc2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
‏ بیشترین مشارکت در گلزنی در جام جهانی ۲۰۲۶ تاکنون:
🇩🇪
دنیز اونداو — ۵ مشارکت.
🇸🇪
الکساندر ایساک — ۴ مشارکت.
🇦🇷
لیونل مسی — ۳ مشارکت.
🇨🇦
جاناتان دیوید — ۳ مشارکت.
😀
وینیسیوس جونیور — ۳ مشارکت.
🇳🇱
خاکپو — ۳ مشارکت.
🇳🇱
سامرفیل — ۳ مشارکت.
🇯🇵
اویدا — ۳ مشارکت.
🇪🇸
اویارزابال — ۳ مشارکت.
🇺🇾
آرائوخو — ۳ مشارکت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/95132" target="_blank">📅 03:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95131">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vaupam8xHpDQdcbXB4bQQNRyT-M0PerGlreL-ktVLwNKGo2A7LhAayG526F4w7MPnsxv6I2MsCJRwawa5LjjBXmDvkCU4AbMdTiFE6dNmXiVkBlhH0s-A9zfCxjkJPg2gHXicJMvBCs2ZTtXavHkFSDQtR5UYopuM2yEtkqcmF3AZiGB_QrJF-rEckXeQQ0Gdl4UlBZ31W2_Fzehr0bKC9wytJXacea2841w3R3Wm6x7yuTYCeVT333p80ekOD6b7zmQaPJeTe0MjYkfZNQ4VyYw91FOlkdt2nCnIVrKpVLmwMJlWDfKCtd1DP-sH_zaTvHyryhQO3DDmHOq6VWauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وضعیت جدول رده‌بندی گروه H جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/95131" target="_blank">📅 03:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95130">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krrEdqVguL0dU-k74-mCWaQ-MEsZEsrIOZX8O1iZnK9ZsYgfwn_zRIecK0G8VsLAKrzMhhvRCqVniHSCfNzAaS2oJLzE5WPQz84ZTvNjXhPzByx75lFihNTF0hD6Nny06JorGDLAvSPzzCZKriu94nGrdZQRlF6qWNSSAxCiy0Aem2RcWraQMvCRdi4gKWhjXD6Uu2_hHW_7JMxoEVPGIu6D8WqCjsDHW9mZ1V65BqVOztGg2OR4ds2R3PhFru3Cn3IrVxg0rJavPtQxg5OAybclRm0_x2NZrbOIL1R0LlU4CnyJeGcwO1Wmeev6FQViHysV4cW0Xi8c9tbe0Evlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شگفتی ساز جام همچنان قربانی میگیرد
🇺🇾
اروگوئه 2 -
🇨🇻
کیپ ورد 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/95130" target="_blank">📅 03:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95129">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNxZ6E6I5GfHCUE9WECUfrcI4RAiaOVixT3oWSOjLjuoWGDNzYKgySiw6y4q0D3Fhhr2jp50Pk86rJuOAd3qGuIjxI1eyHLJ8kyjxvqXP3XFONEw67HtiRtoIA4YagERtqZ7TdklbTVsFN9LuJtXvnd209Xm0LV25uhmbVOHRQj00VBvuJ4fx5Aqqjac8kUDNeR1m5cuHWaZqrEWNY6zbrB5AFGnXc_y1kzxtm-9qk3iQ2UvQvhemT4lzPeGiZ24lgDVOAtbPUmBe3jlDSaDJaoxrpHa5Ln-DzRdVOOr3uFNgKaFel_-TZ4gkxbGwTpE3xDKGTQ00XU5WpufVJYjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
ترکیب مصر مقابل نیوزلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/95129" target="_blank">📅 03:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95127">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAs-jvWSWWMdKjxO0SUeTg7RcarUsjNTigO5_xcz7LVcwnJ9eu-jkCcLGHiQYTsh076HHy0cdQ6MSDRfFXDb4CV6yQG22bLrWOEA_uZGo2db_EmwgLUUp6xHhU0MVZbEgbM9gPi_Ps6UjgStz9OAUPk6t0z0IQYe7hI99xPttkLsmGUCX_mTmrv9HI39mH7y56AeyXeN6hH7CwoLVaGl32ke_qCg9vL_5bz6jX92PTcuDv3kYBduZz1TfpSpoIQGcOEuvXv0dHx2hPh0GcI7Ke55EJ0WXo7g2IShn7RMkHmFGnEMHrlIaBZeZu7SVGAm7dlFPa_HPtbcXstroIRBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lkb8_Lfkj31JYFKH1viVdPibtVyOQ_mT4SYRdQ25DYuhkOGDe7P1s3u11vB5iEL5ZZMtBT7qHzm0E96ctzHYAVuOHDznAL14ogB-nT1eS3B-NZjVkwamvPzShp3LwR5EEYycQwVADs6A-32S5KuyogVm0BLMR6ZlK2KEpsSni4bSCPAuUg55x_k346ORSJtQts9t2SPbEImZYiPQ8E1ZfKskek5KjhZ8ENd18s66xPGmuEKpf4s9IafatEdQcFD2SJ2eGUB2exNiIKZLPeeB0EOaD6PM2jqgmxm68eL4NLmky2s_Pv5WniwUwVSWwxQFiARcnc1HwHzP6jyg3QXmdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازیکن اروگوئه اینجوری داشت به بازیکن کیپ ورد کمک می‌کرد که دید دارن ضد حمله میزنن ول کرد رفت
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/95127" target="_blank">📅 03:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95126">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چیو نزد اروگوئه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95126" target="_blank">📅 03:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95125">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اروگوئه سومی زد ولی مردود شد</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/95125" target="_blank">📅 03:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95124">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46dacb2641.mp4?token=KS0Kf0rppTYxA5nzoytuN9cECEJ3JzVEDpmdCV6gQ06aLv-5_rNBhcpiROpxFLL5XtjFp416d6cXTP50U_Mx-uA1CUjkkqoQEHZ-gfg1PbpMBS8KA-HSWprJ5o7MgyWmsMFQL-AVLUu8FVzOvgJCF2qCtPWkTs8NEGrJwza5OCfmE0uqZcyip1WgQXwsuAfN2u6R5Cy83Yo9QqF7J9UpImUT0M3bNp8SykyRGjhDkAsM3OAEE-osls8JebbYYwzQKv9T3z0rx0J4KH7EbKWimyr9vaqSsA2U7BcPYGqh_67IP1oKJGN-S8krN1QWG-60kACnpAWwrZv3q7lp9kj431N6QVY7pUpPqlu2vSkg5oTkHrcEMIaCVPjcHFv92btNSQfioWXRkKSwexY_qFquFtc3mEqKkbygPo7qKQysqbTMKS5ANZeO3YF00qkPe7mvPa2P-ZpLCYFHrks_F1IcTm8f4m9kJVBvO78Vg0ncyoiEuzsBw0ZscBa4JHvTDjwZHPyLgbAeQHCHr3SauumJh_t2GOKNcBIU-5hNla77y2_UvRaLvjjjVgQOG7Ym9xw98XsEsu1iSlJEQu6APaJu2-pSDYsjlx3ba9-oAeYwLyL-44RWLahXZC40VmAfqxjeYLyeKVAt9fCyy5YjnciEtwTB1xuctM3gTUw2ObGzHBY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46dacb2641.mp4?token=KS0Kf0rppTYxA5nzoytuN9cECEJ3JzVEDpmdCV6gQ06aLv-5_rNBhcpiROpxFLL5XtjFp416d6cXTP50U_Mx-uA1CUjkkqoQEHZ-gfg1PbpMBS8KA-HSWprJ5o7MgyWmsMFQL-AVLUu8FVzOvgJCF2qCtPWkTs8NEGrJwza5OCfmE0uqZcyip1WgQXwsuAfN2u6R5Cy83Yo9QqF7J9UpImUT0M3bNp8SykyRGjhDkAsM3OAEE-osls8JebbYYwzQKv9T3z0rx0J4KH7EbKWimyr9vaqSsA2U7BcPYGqh_67IP1oKJGN-S8krN1QWG-60kACnpAWwrZv3q7lp9kj431N6QVY7pUpPqlu2vSkg5oTkHrcEMIaCVPjcHFv92btNSQfioWXRkKSwexY_qFquFtc3mEqKkbygPo7qKQysqbTMKS5ANZeO3YF00qkPe7mvPa2P-ZpLCYFHrks_F1IcTm8f4m9kJVBvO78Vg0ncyoiEuzsBw0ZscBa4JHvTDjwZHPyLgbAeQHCHr3SauumJh_t2GOKNcBIU-5hNla77y2_UvRaLvjjjVgQOG7Ym9xw98XsEsu1iSlJEQu6APaJu2-pSDYsjlx3ba9-oAeYwLyL-44RWLahXZC40VmAfqxjeYLyeKVAt9fCyy5YjnciEtwTB1xuctM3gTUw2ObGzHBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم کیپ ورد به اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/95124" target="_blank">📅 02:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95122">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کیپ ورد زد
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/95122" target="_blank">📅 02:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95121">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلللللللللل</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/95121" target="_blank">📅 02:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95120">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tINvTC7G_k3ge3e-Ajr493Y48_U1PgmflPCIndWu1FWyOSKBrQYkbJkuovoYSGkBmnZ5T5xMJ4KZI0IFPjfmZKdsKGPyx5HuL8pVCtStuqtTVG2Wtx904NAbuscOxsOyMVkHSY0_shRh6UP2DaHtzIY47vIv4DYaGri1UaEQzeiVrwr2_uzsKjQwE5d-nC8DIAOqpG_fLFVP7P4yUU4Cd5NNeQM6XhmiOli_yFLFy2tr2Uoj2sweUwgyY5N76WSNwCMvzGj62QfYyDDi_dxTSBE0dDdUkWzOyOEWk4gqhY9wJL_PtImdvrw4qNLzgJz_pUVYb2XNbL3FlIzpd9FEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گلر کصخل کیپ‌ورد 1.3 میلیون فالوور میخواد تا به تعداد فالوورای نویر که 20 ساله داره کون خودشو تو فوتبال پاره میکنه برسه
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/95120" target="_blank">📅 02:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95119">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX0WyKC6adA93Zr4SQAiWG9_nYURCe169VjfcfhZnz_l_Z6j4isjAP9SiouQQTA6rr9A860f_REXQZu1fuJAoq2MQiWA9OjqH6NrlH1w6uXOPzj3Jsc-Uxj_DpU2DC-UCV3vv9EobEJlcCp4cw4X1UV8Wy9LzVIGeXP_GnTSce7wVCGules3wuT8soXTW3fd7YBCIyyGuiJjjFTwJrl8Q7eKq5xhDx96K-9M9cJGXY9cAiXufrm2SoitX3I_DSrfCbwIK1rvb_yZkLIMXtZrrinJu1u_LYyc4Q1PqT77HHFwNULsGuJRQrr0kL6Lpb-PmODLAtsQmhI2kckTQo5j8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
ترکیب مصر مقابل نیوزلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/95119" target="_blank">📅 02:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95118">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CznCW7NajIAjm1NftW72aWyaGfFZzgYmYvbLGBnOOhh6m_0ms13PO2Rb7gYAYQA6fcH5iJTB_642_taTEuljMTyldhugEpisveiMufVUU4-s0XiPRV4UBOC2H31QpsFEofNxRA6dZnswwZSEXRvMy_7xwTTKf-ZU2axy-kBdAPMUHkyTGQSE8FKlov8zaq_cA_noUHBcvt9D-UFofUczsU7iSMi8W2j8DtuT6gcf7ZjbFhasIEsdPXnG7zDnd7oZZD1M--XaHadYVQkyH10f2--jbE8Spu3NHFz1M9jj8BQQ7Wi-j3NInJ1is7zoKxsHM-A9qMO4Hg3kFHQus-rCvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار اروگوئه چه سمیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/95118" target="_blank">📅 02:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95117">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیمه دوم بازی شروع شد</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/95117" target="_blank">📅 02:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95116">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqWLw0ZbW62wb7Z2eMlwI3OIqq2DsojDGizSPlRqiUSXHeD2PqpiHgMZ81m70AxMqptPCtXC_c76HmVGanvCrcSmVowPxh_TBDbipd7oUUbNrsO7Zg_irj-YMoMmkZ0YPAeD-Sp4ssYH07o26RimZY7k6mUzcdRyKAvmCNXAK_vtUAVvQk3rI7EhdfjI-_Vdw29ZKjA2mV4hBKi_KkN-fXbTgHlm_g8IGI4o0B5QYdQgXOM8nqdZuDZTHcUgQkb4JDq6QiD_KwQrwfEji4ElhJPT_cfqnUNJ52qdtR_OUsoHa1fJbwU6X1KGhE2ykNLW_-SlMMsjzJgu_x2VixEEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید جورجینا خانوم کریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/95116" target="_blank">📅 02:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95115">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پایان نیمه اول
🇺🇾
اروگوئه 2 -
🇨🇻
کیپ ورد 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/95115" target="_blank">📅 02:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95114">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508a2a45bd.mp4?token=JF1FGrybcEJd8LgOMYklC4NyG1OijBLAq8bTazV_fAy4gExlyz5VnL70ZVHnKuR9K_cZAdgnfAZnNrfJwhLoqwJ7LC9rObHYsYYix4l-LoPeoiIgHwYJ-2BgP92TUmiu9mcCnpMikIgdILHob3XGAlN2X6cP8D58OQyVSXMWeHB5U8a05Uo85WpQEyjKEPc3ombdU8Q92AviZOcNkuhJ6r534MWdUAEcm7lEcOE0AWcY6WezTMnQXE7OhBT4PngzjMdmP8aUxsJtehZjE4MdOa-zv8lFejfLeUxfUKq1AbFj6j5_vZ7xbiSJmGuVbju9Fcvo1xkVOWvSot_Wpz5H8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508a2a45bd.mp4?token=JF1FGrybcEJd8LgOMYklC4NyG1OijBLAq8bTazV_fAy4gExlyz5VnL70ZVHnKuR9K_cZAdgnfAZnNrfJwhLoqwJ7LC9rObHYsYYix4l-LoPeoiIgHwYJ-2BgP92TUmiu9mcCnpMikIgdILHob3XGAlN2X6cP8D58OQyVSXMWeHB5U8a05Uo85WpQEyjKEPc3ombdU8Q92AviZOcNkuhJ6r534MWdUAEcm7lEcOE0AWcY6WezTMnQXE7OhBT4PngzjMdmP8aUxsJtehZjE4MdOa-zv8lFejfLeUxfUKq1AbFj6j5_vZ7xbiSJmGuVbju9Fcvo1xkVOWvSot_Wpz5H8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇾
گل دوم اروگوئه به کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/95114" target="_blank">📅 02:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95113">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اروگوئه دومی هم زد</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/95113" target="_blank">📅 02:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95112">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/95112" target="_blank">📅 02:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95111">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cdc8088ef7.mp4?token=aeXDD9q6z_Bv-Umlvv2dG4WGsURV1xP5-vfyHNlMk2ps1wquOLrb3dA9gflZY7UDdWU_-pWtWort2ClODCkt426oFuMwnfY80fuHFLkJHnfwJ4gNgefMsD6nQ2xeWzPMmuK13qBvUD3_m9nPlp7Y5SyZjtbO7prAPG4P5kzF5nT0zkZ-0G7fRq3vA1uONkls2UY8TYz-rggZH_8etVpG3b-vt5hQZBtxP3JCT5JanK_7QT3WNQv4LwLCQRmPNJwEPdDmDrNbK0DCnsfQ8_qya6jJjMko79hpT83VsxyWmEfcz70BqQz4SE6QLDctnUNjYteIyxje8vBkiMqKX85e1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cdc8088ef7.mp4?token=aeXDD9q6z_Bv-Umlvv2dG4WGsURV1xP5-vfyHNlMk2ps1wquOLrb3dA9gflZY7UDdWU_-pWtWort2ClODCkt426oFuMwnfY80fuHFLkJHnfwJ4gNgefMsD6nQ2xeWzPMmuK13qBvUD3_m9nPlp7Y5SyZjtbO7prAPG4P5kzF5nT0zkZ-0G7fRq3vA1uONkls2UY8TYz-rggZH_8etVpG3b-vt5hQZBtxP3JCT5JanK_7QT3WNQv4LwLCQRmPNJwEPdDmDrNbK0DCnsfQ8_qya6jJjMko79hpT83VsxyWmEfcz70BqQz4SE6QLDctnUNjYteIyxje8vBkiMqKX85e1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇾
گل اول اروگوئه به کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/95111" target="_blank">📅 02:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95110">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اروگوئه گل مساوی رو زد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/95110" target="_blank">📅 02:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95109">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
قلعه‌نویی: معادلات گروه را بهم زده ایم و به دنبال صعود به عنوان صدرنشین هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/95109" target="_blank">📅 02:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95108">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiIVjtdQK7DJ8zJwiT_KOyOo0BS0Hp9ZCa08qj2XFL-GuKVRn0HPppx2zrUKs5hiC-lR_cyPO_3qFM4Hd7SqLZZdTJfrFHqUjgFfBmqnWx2PZ3ze9g658YGpj_ALUgAL5UB4wgnc2HUZorLCvcg4ELI3dbieNAzvLqoZKyfNuPgexauP8V8ZdJmNyrkQa80lHQguSwuK4fyPJZGpjQm_3wnWeHaisb99x1ILVClJufUoizMj_nZGmRAe7tbb7olmhKDHhgwQpGDT-r9rEfJOd_5PMyxip42aLr_zVJYWUDmPYC-mR9pEGsc2aqfk6v-UnwBzelICMdkPamClpYUIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کنسیسائو : وقتی صحبت از توانایی گلزنی میشه هیچ کس بهتر از رونالدو نیست ، هیچ اجبار یا ضرورتی نداریم که همیشه توپ رو به کریستیانو پاس بدیم، من توپ رو به هر کسی که تو موقعیت بهتری باشه پاس میدم، رونالدو هم اینجاست تا مثل هر بازیکن دیگه ای به تیم ملی کمک کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/95108" target="_blank">📅 02:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95105">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca2c51a18c.mp4?token=WYoQi1PutrP9T7ucsMb3wdmWf8plhMrJhzuOIfTgFNytjlzyvJsGTihTsqD4zSXsmUs4OpBZbNcl82G31In-jH_Z4wFnW4gEnUl0WaKC08DSxJ8IN-22nJPlv9N_I_Wh4TMG8kX7pb5IGreAKTnB-UrL2m2AMbgcgbfv-Nf7oLk5WrASRyifVLzn7fQJiR8J6rG3ahFjYtlnqacyP1L-Lq_sPpyIEiRTKWzYpGXzSr6_dE0E3xCCN_XIdEJ6cJCz-0DmtVcknH8b-1sXLziFk112Jro0rzgLEDkLiLzs3zZFtdu6SgvPd_5r5q_uH8Bs9VC0U8uGhvuhVgvnZVRyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca2c51a18c.mp4?token=WYoQi1PutrP9T7ucsMb3wdmWf8plhMrJhzuOIfTgFNytjlzyvJsGTihTsqD4zSXsmUs4OpBZbNcl82G31In-jH_Z4wFnW4gEnUl0WaKC08DSxJ8IN-22nJPlv9N_I_Wh4TMG8kX7pb5IGreAKTnB-UrL2m2AMbgcgbfv-Nf7oLk5WrASRyifVLzn7fQJiR8J6rG3ahFjYtlnqacyP1L-Lq_sPpyIEiRTKWzYpGXzSr6_dE0E3xCCN_XIdEJ6cJCz-0DmtVcknH8b-1sXLziFk112Jro0rzgLEDkLiLzs3zZFtdu6SgvPd_5r5q_uH8Bs9VC0U8uGhvuhVgvnZVRyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کیپ ورد به اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/95105" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95104">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چه سوپرگلی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/95104" target="_blank">📅 01:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95103">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کیپ ورد زدددد</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/95103" target="_blank">📅 01:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/95101" target="_blank">📅 01:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNs7tEpbZTc8qdLa_oKsc1-ARksXCqRXHKYZyptPplOBjL3_qC3YPuMJiZaCteWMfvgeFoh0lapFp8J_-O2HIyjw6-IGEY3fO1mRs0FaS9vIt1BSzNFos2mbizYv9IYrQZlnrHpvRZCxbjRi9Mv7x2c8hT6IRGT_P22Bfzbiqs_KIIALobS1eE56VIBx-NNAa0jsSX244afMmQdIB7bm0YOqAA8VFJ3cGd3RzEM2uUSf8yk6g3kfgoeGFTlm14WXgVZ5GipRxhnJR7jRdzvoSRReBz-mjfObZ-PNWb_IhwsSC6tL4cXJRhs4lHT7InoEr6o70Vsb6uy0A7VxHg41ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوارز تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/95100" target="_blank">📅 01:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4516eab25c.mp4?token=AvRASHz6DAo1L71GXBKTEyHkhpx5rwZ9Ilxtzc402A0moYnqjUluJCJIg_G-3H6PUTxLM34XBeSiQCpFjpbiJs9sxvKaHNU41n1MsMVUn2HO7BydB7uJ1detMBny_1172EuKo9afCqOrpw7GDdkLK1QkGNOSSUpDIk9MKnx5hkXzksRTddvvUdTwtX45D8Mq6cIJJKyr5xKQL0WXxIXKiuwx85gcnC4y1n6Kf7IG-cepiUfIzs8AYZ2w4SKwXzvKOii6OR4ZkDuiqEQCcNMUIotedRSZS5YofVqd2zTzIXfNyqGHEmuZk8kb0ilp-_-x5Rs2fY-FO2UGFo1LL08xKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4516eab25c.mp4?token=AvRASHz6DAo1L71GXBKTEyHkhpx5rwZ9Ilxtzc402A0moYnqjUluJCJIg_G-3H6PUTxLM34XBeSiQCpFjpbiJs9sxvKaHNU41n1MsMVUn2HO7BydB7uJ1detMBny_1172EuKo9afCqOrpw7GDdkLK1QkGNOSSUpDIk9MKnx5hkXzksRTddvvUdTwtX45D8Mq6cIJJKyr5xKQL0WXxIXKiuwx85gcnC4y1n6Kf7IG-cepiUfIzs8AYZ2w4SKwXzvKOii6OR4ZkDuiqEQCcNMUIotedRSZS5YofVqd2zTzIXfNyqGHEmuZk8kb0ilp-_-x5Rs2fY-FO2UGFo1LL08xKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
💥
دلیل موفقیت امشب تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/Futball180TV/95099" target="_blank">📅 01:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKb5AyY6HoWEgtePSAMFoDFMD7KzwbkOpXO0eMVvgunoRaZCw8pF_zEJyVxEuz_gupGw73bxJg4qR5fNCxs-FLNEYpzwOlHaDo9-yibA6jMfwgH0eMrVh_qtgpWW75yALkUnx7VDd31-dYUF_I2g8DOTrc6D8QtOWm64f4WFbb2JI_59lHpMtbrzv0xeJcRXNFNdyfm2cPveYmzGqL6Y9OrdJotraabZEHEw7RGNf4qMFNcfEdjZVe2ocPg6IqvrMqNQ7oVBZgkbsTKH1Ycryq4nVGqnDLQb4QkbTr58iqh05ariNDGjsBdSPhG7JH0QTI9Zh5U3y1w7zYOf1jPv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
با تساوی مقابل منتخب ایران، بلژیک در رنکینگ فیفا به رده دهم سقوط کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/95098" target="_blank">📅 01:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95097">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0036204705.mp4?token=NB-T1FSm2YpmHMGXdR92dmeYqDGr9vTN_BaUYxJ-tZwLmwUEMTkjSOgvBOcB5ZjX3wFRa2u5OrfonQtJM-M47qEOcUTFn-4lIdtEFVLNyQ0_h7UeGpS29H46ZycWXMg_pRVIV-NMxYhKaA-r2Dd8jpcKhEqzm2w7R4krPXVaobFwhDTJMOOFd7k5TyU2xbm8I2qQwtIBpQGOeH4e65B5AQOovFW-cDHBHylDuvtD6LUqpZKgjONoOG9qzppG8lK7TQjh3Fy_XIoilAzJBrv0ToEoW75SbEmdPVuIVqQpjpFJ3qmGZzBASKGijgH1qtFPlFUfO2la9lPFDwfc8x6I8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0036204705.mp4?token=NB-T1FSm2YpmHMGXdR92dmeYqDGr9vTN_BaUYxJ-tZwLmwUEMTkjSOgvBOcB5ZjX3wFRa2u5OrfonQtJM-M47qEOcUTFn-4lIdtEFVLNyQ0_h7UeGpS29H46ZycWXMg_pRVIV-NMxYhKaA-r2Dd8jpcKhEqzm2w7R4krPXVaobFwhDTJMOOFd7k5TyU2xbm8I2qQwtIBpQGOeH4e65B5AQOovFW-cDHBHylDuvtD6LUqpZKgjONoOG9qzppG8lK7TQjh3Fy_XIoilAzJBrv0ToEoW75SbEmdPVuIVqQpjpFJ3qmGZzBASKGijgH1qtFPlFUfO2la9lPFDwfc8x6I8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ریدممممم حرکات دست قلعه‌نوییوووو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/95097" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95096">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHEyBlV_6a_7n88DEClVTwsIGUXsEG_3JURqxYtSafekGvRxIZ7fCEpkCkF1e4hueL4MzBggZsHK20dGZFFt3wEA8hIrY9yzQzDM0x5NEeSY21B3_hlCe5LXjmPvC0pUHWAJlpQ2sjel-E45fioajIMbV66ruSHmPqvxDoR5ajkkZBLoMBs7KC4qssdn3YSl0IHotICfJ3nCzQcSshewMFltkcd2XTB09oerbkM6C3PY6OqgbgGsCrgjt7ykIVje1nsNoU5lfRF5RFY7G2KLdD9ijAQIu254z2b_3mpuHWNzOyRndsjvIvDgTbsObMVO6Fg25nlAZ7rETD4Sq2jQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
آمار پشم ریزون؛
دروازبان‌هایی که تو تاریخ جام جهانی نمره کامل 10 رو گرفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/95096" target="_blank">📅 01:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c180e5c8f.mp4?token=q5n_-J1CvcWt2Lzi9cYdko1nT6JX-K91ykSvtD0Fc6jEHWnlyj0HPc_6mZW5rQefwIUqUfkopDaL6RslqvJoabYpcg2NuAzEcRKN20IOVAY6KqIs92Jb0tBO6WIk31Jm6_gW2v_Fjw89fqIGaW11lOASfAUFLK6g3kcDR_MDjwGcscEZifdxJi7-9WNvysB0BtrMATHi21-3akp3Qn8J_RK7RzkqHW3Gb2trNpWc5jd_0BddPDU6Dh0dnWL81JB2bm-Cquwmqo3goT7iY6ylxBXOTPqm9Pwq3O4jgjqLZT4fhqiO8xVbGvdUUPAWEe462GJHMCEWREU99BKo8cw17jEmbaz_oo-2j6X6zYcMYAJRqqvMQd2i1863pEh2Bh5AgSM5knJw9nyQ3iG3JWRypCqRPbudkbhv7wR2mv28irNzDSsTPHkE5zQMzYB78XnuMzPuolQTXtQvItETf50V_5rJIihEBohipnm1XYxM9NBM0fTQRZZs0QFHTvtDTFkOfjp6jU-ZZUkbIgmtdsAh8X3th0RQ4O4DQyA77qglDYeQ1Kkfq_zv1y9-m_qd0WBR4N15NNR3NVc0TuZk1Nr8LkPB4SbGkVMjYVX_xVSbuY08gBJx5faxBQHLQY4SvGTEJ4VS5Cig5iIoKsP5DwKju2Um0eOKrwwTYuYjBKFMt-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c180e5c8f.mp4?token=q5n_-J1CvcWt2Lzi9cYdko1nT6JX-K91ykSvtD0Fc6jEHWnlyj0HPc_6mZW5rQefwIUqUfkopDaL6RslqvJoabYpcg2NuAzEcRKN20IOVAY6KqIs92Jb0tBO6WIk31Jm6_gW2v_Fjw89fqIGaW11lOASfAUFLK6g3kcDR_MDjwGcscEZifdxJi7-9WNvysB0BtrMATHi21-3akp3Qn8J_RK7RzkqHW3Gb2trNpWc5jd_0BddPDU6Dh0dnWL81JB2bm-Cquwmqo3goT7iY6ylxBXOTPqm9Pwq3O4jgjqLZT4fhqiO8xVbGvdUUPAWEe462GJHMCEWREU99BKo8cw17jEmbaz_oo-2j6X6zYcMYAJRqqvMQd2i1863pEh2Bh5AgSM5knJw9nyQ3iG3JWRypCqRPbudkbhv7wR2mv28irNzDSsTPHkE5zQMzYB78XnuMzPuolQTXtQvItETf50V_5rJIihEBohipnm1XYxM9NBM0fTQRZZs0QFHTvtDTFkOfjp6jU-ZZUkbIgmtdsAh8X3th0RQ4O4DQyA77qglDYeQ1Kkfq_zv1y9-m_qd0WBR4N15NNR3NVc0TuZk1Nr8LkPB4SbGkVMjYVX_xVSbuY08gBJx5faxBQHLQY4SvGTEJ4VS5Cig5iIoKsP5DwKju2Um0eOKrwwTYuYjBKFMt-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
👀
سیو خایه‌افکن بیرانوند از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/95095" target="_blank">📅 01:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccbcf146d.mp4?token=gKkAPC_0ZeDwqobDb_DqZ3P8XtTAKlIAatZKVk3VukDB6FkWNFd37-MUX3PrgrefWKYHDOwbIIGkJpHNyXViU06ho93S8I0-WO9SLmY-I2fhKcYtaQbdZLpESTivtBA0F6XHvvM3uxpS739hkQHgsWWFnXI94ZCNO3YquNPT3QMx4Mi6HCdlf2PU74ac_DR8XCu1cW_-vV5eShbESMqgcXT9rlORRgwLxuCOzvbtZ4k5Wf5ddxbyrhIQIlaTtdsi_DZHODJtoRFF_oseSGI0ByNMD57sr2EDXQh9aifeI-XQXM1W9tOwydLxI8Agw_JxHZtMbm3iSu-1WNEWlHsG9gLPZMeJvvw6l_5WFJtvBHhVSRkEJ6yMxJZtNiS0QyFlTe-Wrb5lQYido6tK-czPQUYAAkFbxrQzR5kypwIwaZa9J8i8O9ZqMnHLzwlScCAlB9oFxWsenYeE8AmbZYFz8sI44YSwuMk8b5z6N7mSQvJvyFXbXzylp4LHn2jW0Be0yUXLiO1bxDPM-9SPtBrObT583e9NNvA719zYrTxEdPjM5Ip39lIt8ERz0W0T_rULvDk4somWLOS1m8ie2JHzGVeP0oJ7u18XgIs9ets2DIMbv3UVCAayTGK_zJiuVGae9BoOQU_RD2xRcTplWKYWD8aheDQPQf7E3FKffw-ktUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccbcf146d.mp4?token=gKkAPC_0ZeDwqobDb_DqZ3P8XtTAKlIAatZKVk3VukDB6FkWNFd37-MUX3PrgrefWKYHDOwbIIGkJpHNyXViU06ho93S8I0-WO9SLmY-I2fhKcYtaQbdZLpESTivtBA0F6XHvvM3uxpS739hkQHgsWWFnXI94ZCNO3YquNPT3QMx4Mi6HCdlf2PU74ac_DR8XCu1cW_-vV5eShbESMqgcXT9rlORRgwLxuCOzvbtZ4k5Wf5ddxbyrhIQIlaTtdsi_DZHODJtoRFF_oseSGI0ByNMD57sr2EDXQh9aifeI-XQXM1W9tOwydLxI8Agw_JxHZtMbm3iSu-1WNEWlHsG9gLPZMeJvvw6l_5WFJtvBHhVSRkEJ6yMxJZtNiS0QyFlTe-Wrb5lQYido6tK-czPQUYAAkFbxrQzR5kypwIwaZa9J8i8O9ZqMnHLzwlScCAlB9oFxWsenYeE8AmbZYFz8sI44YSwuMk8b5z6N7mSQvJvyFXbXzylp4LHn2jW0Be0yUXLiO1bxDPM-9SPtBrObT583e9NNvA719zYrTxEdPjM5Ip39lIt8ERz0W0T_rULvDk4somWLOS1m8ie2JHzGVeP0oJ7u18XgIs9ets2DIMbv3UVCAayTGK_zJiuVGae9BoOQU_RD2xRcTplWKYWD8aheDQPQf7E3FKffw-ktUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امید نورافکن: بازی با بلژیک، بازی تاریخی برای ما بود/از لحاظ بدنی در مقابل مصر، تیم آماده تر به زمین خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/Futball180TV/95094" target="_blank">📅 01:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d8e1f59.mp4?token=RSaSPLjemU8IqDboWTvSzKlWqyclPW4HzsgOU4H-vvmiuhYY2yMXia8_Lz1B7zEzVCKArV24YUPYQ0WyfABRRGc1ResOxb8I2hfk_E0BhELh59I_w-9IdouDTV3OlMsNiW5b6dI4NYLO7ioS1gyk9EwgwDYhMFGlr18_PKv_bD0ET48EaoDZB1LChUDaCA8bCOkucP8pLSxYkn0Vd7e-snvgGO00uPFOCAG7_sr3xXiHcXJtB2203C453ViWPAox2xktRBkYwfFJJ530IJ21LpEztAVWiNTyTpe318aXfAlaKfQSeJ_sQ4C7aGQbY85x2NOvUDbHYY0jG1PczLy_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d8e1f59.mp4?token=RSaSPLjemU8IqDboWTvSzKlWqyclPW4HzsgOU4H-vvmiuhYY2yMXia8_Lz1B7zEzVCKArV24YUPYQ0WyfABRRGc1ResOxb8I2hfk_E0BhELh59I_w-9IdouDTV3OlMsNiW5b6dI4NYLO7ioS1gyk9EwgwDYhMFGlr18_PKv_bD0ET48EaoDZB1LChUDaCA8bCOkucP8pLSxYkn0Vd7e-snvgGO00uPFOCAG7_sr3xXiHcXJtB2203C453ViWPAox2xktRBkYwfFJJ530IJ21LpEztAVWiNTyTpe318aXfAlaKfQSeJ_sQ4C7aGQbY85x2NOvUDbHYY0jG1PczLy_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استراتژی امشب قلعه‌نویی که عالی بود
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/95093" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95092">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/95092" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95091">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e-0Znt-uKD3N5anrP8uZ6wNeHQBynD7-kXzJpqqoJGEHNN-GT4FxkNUMiZUq3k0AVZfhgDGctCyWX1Y7_3xNIioKpCq-nMtXkAgCmI_sZUntFzwHZP3iBdo9-_20utjWAye8an8EnuugJhoBfFJbT7S5EcAYR7L4WdOXXeMsUBIqFaYZ-yX4zkfmH1sI68gK1dDcdZGeVb916i-OADvcgeTke-Dk5uD47fI-QZpK3pYbeY5nRBedv9I-UmTEd1zWvI8YH2HPyAPiWsagESDGfLg28KniOBCbssCd1z85iQCv9nSMgrivRdv2yYkVpWYQae-v04Fz3bmGtLZNztFUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/95091" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95090">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از رومانو   بیرانوند به رئال مادرید  here we goooooooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/95090" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95089">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qmVC6OsEBBycj_d5Rkuh9xefp1OQV8URyln8nU_ZpV9G3FldIBV3O9dUDITUvLfxpJfCvQtiXP6pRzSA9FvJQk0VfWDv3sApbRMOpTKO44VSvx8Or81xxQ2Ga-krDk4XgsZo460RBx9M0OX_IvbixSeVBKtMONzmRS1h9AAXbEsFXv-xOBOnrIXvo_HXoCugKFhb05negwuz61PGtusZinPwKTmm0J5VNkG184ML6ScB4Lj-phdPkgI9EMXBmzfQ9x7g-Mo07NExqnDJIFM3ILRhjiAfFcIYCghvbSPt2kcTmy4lnwh37Suobh4JtuXCenoDqqeMtN7y9mq-DYneVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از رومانو
بیرانوند به رئال مادرید
here we goooooooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/Futball180TV/95089" target="_blank">📅 00:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95088">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j12gPmg8aQ0BoMPeS2WkqKOmWaRSOpOWInLl4VDJPinyB-iS-6MnaIUT1KJHKl2l09z16iOrZwkNslprqySC1Q-sfOlSSscx-Fe0tZHCGnvnykST_aieFw5R419njx7bJnT2uQ_8lrHljBuKnbq16e3eu2IzsRtCleWSK5phsjoOnkif8pa8Mahrb1nLBy5jJqsja1VJU-Ce8yRayi26feuQvzd0W_e_wkh9pR4uqwVGOr6noj2ieZKSbNlbVMD3vitGokAEG6OJZUVin-yASYZw_PVpNIvk0nursDSw3KnhDiWWTbZNwYLvR1_seaNWQFOkyKoVzCcm_dHEcz6-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیرانوند و جایزه‌اش بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/95088" target="_blank">📅 00:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95087">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a4d65e8d.mp4?token=cJfFthhN5aFaxJinOu0KTptI0Y3eL47xLfZWGPOiXX4SE9ZH-sOJMtLVTAEeJL4HQS2J06PbFzlZP1ZD1NUCRKBz6Q1O6jREt6JMhLTq8HWx5W7AD7DJ4ZbqweZuCkh08PCGBPqYrtro8_NYBjnCaG3kCsICdNDV1zXfpt-PNPE149eoi22whHyX_AZaJLt58jYya2KY55ari3_CNUc-eU_ipYZivQw9Un0doyJYxVdtXIBpooHbj0ByfDonGlefbdPuaI9osTmIpylrYnHhGpKPXPPR_xNMxXfWKIK3XLlbt3FbYGY5oefh12ivmh5Ibim4hSe62eUZz1seagAO6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a4d65e8d.mp4?token=cJfFthhN5aFaxJinOu0KTptI0Y3eL47xLfZWGPOiXX4SE9ZH-sOJMtLVTAEeJL4HQS2J06PbFzlZP1ZD1NUCRKBz6Q1O6jREt6JMhLTq8HWx5W7AD7DJ4ZbqweZuCkh08PCGBPqYrtro8_NYBjnCaG3kCsICdNDV1zXfpt-PNPE149eoi22whHyX_AZaJLt58jYya2KY55ari3_CNUc-eU_ipYZivQw9Un0doyJYxVdtXIBpooHbj0ByfDonGlefbdPuaI9osTmIpylrYnHhGpKPXPPR_xNMxXfWKIK3XLlbt3FbYGY5oefh12ivmh5Ibim4hSe62eUZz1seagAO6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
💥
واکنش فیروز کریمی به سیو بیرانوند: خدایی خیلی تنگ بود
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/95087" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95086">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pEA8cGDtvtthYrXSnHZFQ_zV4COJzQX89kzB2jA9pR-hi0H2R9pZFUtLRW6G9RuFA4b5_Zs9HXWZRx2P6wnhA4WAadzzIoRa-Rx1gjw5KsnMAkyN7qAEMHqEPEX9eQemnrcchdGD-8DZenWJ3Z2fKUCO3zM0EGTzuEWT_U9b8Q5L056Y2ORytlSOzkwlW2Igg3SXhUn4hug7jz71Q2Bkp5zI-CFCnZUWnxNWpzDcOpdbyfGwgAXDED_pagC7EIOtklyRHcFak3cgpQj7ujuSoenYBOfPlpkCXzZt6FiSkDed1IJhibV4gK_t3KK9yHwtbV0MFcNz_BXh0IkG4ErNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🇮🇷
زلاتان ابراهیموویچ: در نیمه اول خواب‌آلود بودم و در نیمه دوم چرت زدم، بدترین بازی‌ای که چشمم دیده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/95086" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
