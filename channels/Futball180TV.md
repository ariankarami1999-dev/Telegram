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
<img src="https://cdn5.telesco.pe/file/Rxp8Jq9QvP9p3SkvCpTHyogW1RcAwetaXZ9QozbjxXtqt2WklehWBWAZD0pXzBgQf38ftqx7Nf8zir0TntWrpp2iFvHyDW7NXhhVvNA0HBB1WJrdkMzSmJ9dDwAPaXDqOq6FSwcGnZxbjYo_wQD_H9099OR10x0oj5eR-Z-mol5l5qeALhCjH7mXw9ItxijRKKPM8pyCYESskuhdSAWglqCn2STWpxJUj4e5A-fBuJAbkSJsScdnUpMDlsDq-HKskEl0cXazeXG_H467uKlISMRKXfRuOWvVUBwcNFoz8IVSFYxwjLqBnVGSJfLNOvpb-vY-P66mry8nZe6Gszneaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 405K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-107022">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/Futball180TV/107022" target="_blank">📅 20:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0JcNqL3JyxoBpwlbyMpawDxC80Y0-rl-VVqbbpqGEFkmnF09tRCYdpWgjEuCqDOgqPnceKUrAm-ro3-cVha3jHOBHjmTrYiulh-t7Z1p3C9l80WqusDnzmRW8G8QQAzis-BeD_7Qt1rJpcUuoXsTD9GZMhpJsGDnWHm85AaelN8-4bL_Z3CQiWjQ-TfUOiaemtQ2UHBR65jBsR4LxRbVVfwWubq4O3YpQ2S4WFrQCTxxSk6kAK-UBvXA4tdC00dxWVve5dMdMNkoTgrkSaV8Yfvi7Q35-Vu_taICaTTvE92ACegiurReyz-SN_4VFA_PmT5K1bP1jd5M6U95_WO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
مقایسه آمار نیمار و رافینیا در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/Futball180TV/107021" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107020">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=O45DNC4cTf3HxyTxydjtpXOdsjr8YRzm1juGjlUH8uUqtaD9bXuxgbh1g9V30qjfZrqbHUh8WVZ1om1Ze4s-AvxT4k2NHh1vc9OPJ60eQrnbAmF3ItVLi2iaQgixCdwIeQk5FbNS-nUgkIRVMx8vQwDI_fzNqSu1b4tnsSUc8zGb1kAUf3aGSOqY3bLMFDvMGmoOY7hjJIPyotgxgfOmdWQnClnYYGRlkSnfuuCe46C3yRBAyX4sBujmj158yvWFslKRJccfHiL12WSUm2wudJDkwH0ovb-wZjRylnaJIkYhZMXWqliMQSlxh30igI--errkKbbYaznp2gIlwLc14Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=O45DNC4cTf3HxyTxydjtpXOdsjr8YRzm1juGjlUH8uUqtaD9bXuxgbh1g9V30qjfZrqbHUh8WVZ1om1Ze4s-AvxT4k2NHh1vc9OPJ60eQrnbAmF3ItVLi2iaQgixCdwIeQk5FbNS-nUgkIRVMx8vQwDI_fzNqSu1b4tnsSUc8zGb1kAUf3aGSOqY3bLMFDvMGmoOY7hjJIPyotgxgfOmdWQnClnYYGRlkSnfuuCe46C3yRBAyX4sBujmj158yvWFslKRJccfHiL12WSUm2wudJDkwH0ovb-wZjRylnaJIkYhZMXWqliMQSlxh30igI--errkKbbYaznp2gIlwLc14Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
واکنش اتلتیکو مادرید به عکس‌های پرینت شده مورینیو در کنفرانس خبری
: «همین حالا به آزار و اذیت داوران پایان دهید!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/107020" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107019">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=h6zM61MPML26WvrC2lWEsDwny3X1sh6G8VJOw51MKov18SH9KonbFtXWD3R3uLHTmINXTHmE84_Pag8r_DT12LA4LPwOdnWs4Tlv6ioX-_N2DHfPx3LXKwEwwynqYGKP45kgVqP9xbeCz29e5nk2EHSCP1jFxB5YRcFIv3kCFSmNhq7EorYFPsDVCXYAEflpYqT2iIgzulnQF-XqtcwTn028aQgltMOhiSkjJ6iVGuYNK9HQHjwzQqBHoYfsrXzQkefLMJuq2kxIWETBsyHqlMLhAuGq3RBjs3-ggNGPyNp6BEea4rFxyR87nV2ZPf0gowbWsm2cRJ_HYSZmTE9Gbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=h6zM61MPML26WvrC2lWEsDwny3X1sh6G8VJOw51MKov18SH9KonbFtXWD3R3uLHTmINXTHmE84_Pag8r_DT12LA4LPwOdnWs4Tlv6ioX-_N2DHfPx3LXKwEwwynqYGKP45kgVqP9xbeCz29e5nk2EHSCP1jFxB5YRcFIv3kCFSmNhq7EorYFPsDVCXYAEflpYqT2iIgzulnQF-XqtcwTn028aQgltMOhiSkjJ6iVGuYNK9HQHjwzQqBHoYfsrXzQkefLMJuq2kxIWETBsyHqlMLhAuGq3RBjs3-ggNGPyNp6BEea4rFxyR87nV2ZPf0gowbWsm2cRJ_HYSZmTE9Gbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رختکن تیم‌فوتبال رئال‌مادرید بعد از شکست دیشب جلو اتلتیکو!
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/Futball180TV/107019" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107018">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=S_40_nspWMeE1smUbxPf7oFElhnrsGvK_0VEFn_h6wnrLbkWLBjBRHdR3Itm7g9OQjsn-jP81ZOIDGAL1b4Uhf3PQbCiDSma4qzOkv_m7nslXr0HDUM2YUSorDI0zwzeH_YyTMJh6yFAcFvkASmq1GcO3piKdk-cVTD3KFazCBfiMSQt3LwaUL3bOchyMx3EDg1DqX0BKfEj2O_gBlmRw-RHHgoSgLjMop2wFhEMZ5VYCqo8a6l_x6H2JtfRS853k9Kpq6X0DyCIIRH3xhm-fKSjrErLfLzLY8oCvlDXof0VTVoBbhdlBZPDZc9V0mGAMvmFFki__h27JV-9hUu_RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=S_40_nspWMeE1smUbxPf7oFElhnrsGvK_0VEFn_h6wnrLbkWLBjBRHdR3Itm7g9OQjsn-jP81ZOIDGAL1b4Uhf3PQbCiDSma4qzOkv_m7nslXr0HDUM2YUSorDI0zwzeH_YyTMJh6yFAcFvkASmq1GcO3piKdk-cVTD3KFazCBfiMSQt3LwaUL3bOchyMx3EDg1DqX0BKfEj2O_gBlmRw-RHHgoSgLjMop2wFhEMZ5VYCqo8a6l_x6H2JtfRS853k9Kpq6X0DyCIIRH3xhm-fKSjrErLfLzLY8oCvlDXof0VTVoBbhdlBZPDZc9V0mGAMvmFFki__h27JV-9hUu_RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «ک…، خفه‌شو» دهنشو بست و این شاهکار رو خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/Futball180TV/107018" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107017">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=V8gxZRj7Rwy3d52TTYeg6-dDd2G7kU6JKlkptp-A3Y6jGNRRdU8eGOzO-CvNOPPKwBBc1knS1jAC9C9iiAVpmjIGtpYqTU5vd5gD3TmJNkwjpXkQpcoWO9Rbv4S9cXcsWzlRF3B1PINse673EJELBEfvAhNiq-Ehxs2wV0yt4Mqtu_2V5ZlI-K232TI9PrvIGMVIrfaIMn5PesneGUloFdkwASNsRz5_uffYBUpnigZY6YSn16JkQBv2iY0a8dCKs-jvo7XAeaWQlkRt0Gjpk0gk0gY6C2IUDNqAnKA__p0NmCGKDrP1I9HUv8JhANz9iz9znpLqtxmo6-TQfaBcMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=V8gxZRj7Rwy3d52TTYeg6-dDd2G7kU6JKlkptp-A3Y6jGNRRdU8eGOzO-CvNOPPKwBBc1knS1jAC9C9iiAVpmjIGtpYqTU5vd5gD3TmJNkwjpXkQpcoWO9Rbv4S9cXcsWzlRF3B1PINse673EJELBEfvAhNiq-Ehxs2wV0yt4Mqtu_2V5ZlI-K232TI9PrvIGMVIrfaIMn5PesneGUloFdkwASNsRz5_uffYBUpnigZY6YSn16JkQBv2iY0a8dCKs-jvo7XAeaWQlkRt0Gjpk0gk0gY6C2IUDNqAnKA__p0NmCGKDrP1I9HUv8JhANz9iz9znpLqtxmo6-TQfaBcMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت هاشم‌بیک‌زاده از استخدام مربی خصوصی رونالدو برای رساندن مدافع تیم‌ملی به جام‌جهانی ۲۰۱۴ برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/107017" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=YuWjvaYbIwaNlqFQySwG1TG2S5Um1zYfw5W1Y2Z3pssrb0pHizkkQbmpBMy0pRs23i-nB3FMNrR7Q7MuRwSubkqQktYWJH86XzPvSY-gDqBRRCW7wYXy8iXgqJZ_PUNXxB3z4RjsEv03q0Crazb7Z1IJOUbPNjZr52cxrilWq1vMriobJ-uoXb4wi8djxBXDJEM5LwMcPzvC3757eFEKnM_PFxgYWF-N7VppdfJkdP8s9bu0F70rjJ1IoWokHOboFD37pagPgV857Mxm8yW0v3O3a_IrwHMDoWR6Oa_xvrnxwadGpHydM36s6QjTLyAn_MBcrbqaETqx1xfCR--UhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=YuWjvaYbIwaNlqFQySwG1TG2S5Um1zYfw5W1Y2Z3pssrb0pHizkkQbmpBMy0pRs23i-nB3FMNrR7Q7MuRwSubkqQktYWJH86XzPvSY-gDqBRRCW7wYXy8iXgqJZ_PUNXxB3z4RjsEv03q0Crazb7Z1IJOUbPNjZr52cxrilWq1vMriobJ-uoXb4wi8djxBXDJEM5LwMcPzvC3757eFEKnM_PFxgYWF-N7VppdfJkdP8s9bu0F70rjJ1IoWokHOboFD37pagPgV857Mxm8yW0v3O3a_IrwHMDoWR6Oa_xvrnxwadGpHydM36s6QjTLyAn_MBcrbqaETqx1xfCR--UhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین قیاسی: مهران مدیری برای حضور در برنامه من اصلا هیچ پول نگرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107016" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107015" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzumOeOGnsqUXvWQsNg3V7rKUCpkj2NipPSfOvMsQnPoPZTJezI-uKUM2PmMcrMtZCJFrhmH7y-zFaF7nu2e4OxijYrU5C_JnMx_xzItuCPuQsv47PF41waVrkIVWK0HazEuNsi9KSQhL6WfD0-tgQhCIfZEpQ9_7jBZZYM2E_s4uBgQPPpoNNeyHtJP617qxRzFlwKVJqRTPnxk89mHCg7KQPYmBwZcM-dUJ7K6RCuNRcyLNfJ-dBZRfI6b0nFyVr4RpggV8JHZG6fBM6Ux52504BBHt_teMXGVGB_PLtsrsmr38_HqKD9iaae1ZYlhhNiABviR46yiY-A92zvhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107014" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=UKiEIaG9xMgNX5whfylBV6NMleeJx9Gr1lcWBymVTW-j4BYIIGBe0tFzbebxTB-uz3-GBG_igmIczJaRIyi9Nwwtlq65ShXE70FAkl72QHi5FhxbxTLOWKUV68LX883rmN6f4QI3RLpF0AP_A3bwCSAAQNEbsZAtUizZQVab1Cj2zR4erEJRLz0hcQtP3_Racc7o3-2dmh2Ng9xdzXlQKXII-tivOBHFZwD4QGfohVt15yxXR6pAuOYbXiVzc4oRRupPZir35HXJf7xFIwXZH-TOSy4HQ4jLXauN-_-19V5WrAM7inGhuc9qfWbP8RLpp_WWwG75MlBz3VQ5ox37_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=UKiEIaG9xMgNX5whfylBV6NMleeJx9Gr1lcWBymVTW-j4BYIIGBe0tFzbebxTB-uz3-GBG_igmIczJaRIyi9Nwwtlq65ShXE70FAkl72QHi5FhxbxTLOWKUV68LX883rmN6f4QI3RLpF0AP_A3bwCSAAQNEbsZAtUizZQVab1Cj2zR4erEJRLz0hcQtP3_Racc7o3-2dmh2Ng9xdzXlQKXII-tivOBHFZwD4QGfohVt15yxXR6pAuOYbXiVzc4oRRupPZir35HXJf7xFIwXZH-TOSy4HQ4jLXauN-_-19V5WrAM7inGhuc9qfWbP8RLpp_WWwG75MlBz3VQ5ox37_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
بهترین گل‌ دوران فرشید اسماعیلی کدام است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107013" target="_blank">📅 17:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfpnvsRhOzefhvmqckA9tJLjg5hj4BCJLXhagx08gaNJZiEICf2E0Q6eHmWhIUA0LjJnkoQj0wjZ_OTfC4edYYsdHC1-NZI_gPwb8C-Di5AtZBc48QCo0LqJMH7Uv4WkodwFqYiGl-5OYNKvQhnR39Bb4GMaVsFK7LYKPfi-bLMXC4B7icL5DW7UbKdjoL-dE9XW4zTnLanBTnHTVuQwZBt1ZyNyYHLIQw-fCXS88cYkbQYnvENvQagPDWvOZcoyCpWAZd5cZf6ZUEH1MtdS304eBL3L7DuN7_g9qp8HGqEjadfIvRNmlMcsN7Bx3-gzOpywt5E31dwsjDwtW3i_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سه سرمربی آخر منچسترسیتی همشون پنج بازی اولشون تو PL رو بردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107012" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107011">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=KrON_hufmzRlY-s_Z-yO50QgMKHa49yDr5OxX5lyadpDQuJav_1OBB-uRjvoKmHoO3bMbnnS8ZTPgDqeyB1d5Sr07TzYfrjC1WCfYSCi139bYdmOLysCwN6VGxdrfPVwsTnF9wIN260-rHRv_xm_Ewr4jGOfecyEbppC6mQkAhXhZt9X4XP4RSyhPjNrHe68-Ve0mRRdFDovi8NH5fzdgbvu5d6RyW4a4DYzwvgeYKE95hVhMezsCR3yo_I2anqSp4ll_0GB22mPCSachyDKAp6mdvIPGXukz7busx6Ta2_Ck4-l_qUTaH1zeh7SScjVRQys7MTg2e-KS7qdWvnb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=KrON_hufmzRlY-s_Z-yO50QgMKHa49yDr5OxX5lyadpDQuJav_1OBB-uRjvoKmHoO3bMbnnS8ZTPgDqeyB1d5Sr07TzYfrjC1WCfYSCi139bYdmOLysCwN6VGxdrfPVwsTnF9wIN260-rHRv_xm_Ewr4jGOfecyEbppC6mQkAhXhZt9X4XP4RSyhPjNrHe68-Ve0mRRdFDovi8NH5fzdgbvu5d6RyW4a4DYzwvgeYKE95hVhMezsCR3yo_I2anqSp4ll_0GB22mPCSachyDKAp6mdvIPGXukz7busx6Ta2_Ck4-l_qUTaH1zeh7SScjVRQys7MTg2e-KS7qdWvnb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند شروع جذاب و یک خداحافظی تلخ. این فیفا دی رو از دست ندین.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107011" target="_blank">📅 16:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107010">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⭕️
⭕️
⭕️
🇺🇸
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد و از پرواز به تمامی مقاصد بین‌المللی منع خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107010" target="_blank">📅 16:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107009">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTLwL6DGFMxgbDkKTvIJ8DW6mQk9yBpqXGqJnSLe8LJEsrctmTolgtGpkrT4GUafVrivj3gcte5ePWebcM7hSJ45MF3v7UPTAjD3J3PRbDcIrStEW_yzS0LEHLmcs7YEjE2i36l2NUadAWBpcOZQkKkBC9cPQzqpu_e9qQzQdbq8oTL8jfJ9qZs0NmIrvkLYzp8YU-vvRZFnyMiBGj1_sEzQfGVjl3tTZXblhylN3c8A5C2IH-kzAMSySMtfo7YujDFq2Kt_8-hkQotVaW_eLYuQVb-UKfztpUwCoaYWBbA01TB-pxScqWQXXfBRC2O-FcSWf8J8VJZsQR3JBVPa2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
آمار درخشان اللهیار صیادمنش در لخ‌پوزنان لهستان که نتیجه آن عدم دعوت به تیم‌ملی بود:
🔴
۱۵ بازی؛ ۷ گل؛ ۲ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107009" target="_blank">📅 16:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107008">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d7084572.mp4?token=OreVuD1S8lehy7FzfsQj1pf2wHr8YHS_V9OGcHhBhYsz0iQ5RVbI1OL8_RWR17DUSFjCZ_qLHkFrcWrwBO0mSPptQVY81V3VTZVN8t9k8FWzOl4QP_X20l9aCaxjMVKTd268qxa0h3NdqoUhHu9qsYDDR5Kj-Jz5xC2KYjsUOxafHEX8Lnp4IFMYUls__z_Uj3tJe3X9VTZD47ZdvcJ4Ju6mNWTKuWeE2dVghwYkIlFAyQ0p18XOoHU0Q6KYI-r5OwmC9fXjRii-xOv56m9IKAVyOoJAfZUHgLPQOzjeGkxyNAvPaejxadzJ29oR3JeUfOvbM7p48Uh5PkN3jb0ung" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d7084572.mp4?token=OreVuD1S8lehy7FzfsQj1pf2wHr8YHS_V9OGcHhBhYsz0iQ5RVbI1OL8_RWR17DUSFjCZ_qLHkFrcWrwBO0mSPptQVY81V3VTZVN8t9k8FWzOl4QP_X20l9aCaxjMVKTd268qxa0h3NdqoUhHu9qsYDDR5Kj-Jz5xC2KYjsUOxafHEX8Lnp4IFMYUls__z_Uj3tJe3X9VTZD47ZdvcJ4Ju6mNWTKuWeE2dVghwYkIlFAyQ0p18XOoHU0Q6KYI-r5OwmC9fXjRii-xOv56m9IKAVyOoJAfZUHgLPQOzjeGkxyNAvPaejxadzJ29oR3JeUfOvbM7p48Uh5PkN3jb0ung" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری یاشار سلطانی خبرنگار: روح‌الله رضوی کشمیری، مجری جنجالی شبکه خبر ۱۷ میلیارد نفت از ایران فروخته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107008" target="_blank">📅 16:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107007">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBo25NXVEm1ybXZF6cYwtJCl8Rp0S0f6LyEHHm2WRnDTKfxZpRA-O0cpWa_3hZtBAuEUP_s5fWFQti5ryIXKCwrKV58_lt6iomf44PGGHnqUzwL8534sJISZyyGG8Srl9fNcB9917EikUfxcO0PEKNjxXdOSX-9qQ1wUY4GD5idhDSkPvcBcZdIttizf5njZGxp5Yrv86-2i8b2qOUXAdq_7EEgMZJLF0uuXPf96wc9Jl3jVhSW6R_0Uw9GaxKmk-NHeHYLCIYbTF-2xCTnJfpaOPueCCkQTtfy3Vkm08j3sJGBuBOhUs0r7psBGJkr3v2UMqQSPYAJKfh5KW_0zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
دیدار دو اسطوره محبوب و مردمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107007" target="_blank">📅 16:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107006">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=jwZNttxMLv73dRJBUeaKrG_z9eik14TqgW_Xmvr3gPa55DcL-nmUcA7EGSU0481qliM2MMjDiy8YksbQ9HTXsXcbJ4jk25aSfupGJ4mNT2X1mZKBiiQxqQX_VZEMLMxhXbH6XO4_3KBxaEWjm7C66Mt0mosXARpETvFIaAWQ7UNxINPF1xbb27n7Ck6t785u_ntJjtsr1f-u2ejf6bOLRs3EerPQX_MLbuIyHLX1aGg_3OVDlFFi8K7VivTf0oF_Y8hLVBgll_AYs8J-touiHYHXRAiS4nBHA02rfR5JsYtV8nCTpMcUiurDUxudmV7u2EtN57c1WlzVDxbmBR7OZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=jwZNttxMLv73dRJBUeaKrG_z9eik14TqgW_Xmvr3gPa55DcL-nmUcA7EGSU0481qliM2MMjDiy8YksbQ9HTXsXcbJ4jk25aSfupGJ4mNT2X1mZKBiiQxqQX_VZEMLMxhXbH6XO4_3KBxaEWjm7C66Mt0mosXARpETvFIaAWQ7UNxINPF1xbb27n7Ck6t785u_ntJjtsr1f-u2ejf6bOLRs3EerPQX_MLbuIyHLX1aGg_3OVDlFFi8K7VivTf0oF_Y8hLVBgll_AYs8J-touiHYHXRAiS4nBHA02rfR5JsYtV8nCTpMcUiurDUxudmV7u2EtN57c1WlzVDxbmBR7OZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مانوئل نویر در بازی بایرن جلو یونیون که انگار خودش رو دروازه‌بان نمیدونه
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107006" target="_blank">📅 15:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107005">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4379faf506.mp4?token=hLtdsdY2bQBMrOC5XSejD0mS33_M_zZjjnG_rIM-2FeMa9earK_R70x63qQiJY03sSs-IEb-6f_zYTbf2mOuWGTdBMemu7P6yEhvP-NxhU-_ffLPSmbhXX49qymNcTGPFgxSg96_21zgJ48EnHpoNJ_CtfCMtbu5j7jMjV3dij7X50X7wk8U11R98ww-CWMQqZQaiQw6B7HNPXmzz1naNMDi4APwSZiF-7ynC9QRYk3VbTji1SCWhlCO25W79pLzCGhELBbYEaR7-fMCivCYfx1skr2Fw02iQhVHMZ8NaXX40M_rTsXvV3NrSj0TtmWo5k9sepHmcAx9gCYQu6nZ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4379faf506.mp4?token=hLtdsdY2bQBMrOC5XSejD0mS33_M_zZjjnG_rIM-2FeMa9earK_R70x63qQiJY03sSs-IEb-6f_zYTbf2mOuWGTdBMemu7P6yEhvP-NxhU-_ffLPSmbhXX49qymNcTGPFgxSg96_21zgJ48EnHpoNJ_CtfCMtbu5j7jMjV3dij7X50X7wk8U11R98ww-CWMQqZQaiQw6B7HNPXmzz1naNMDi4APwSZiF-7ynC9QRYk3VbTji1SCWhlCO25W79pLzCGhELBbYEaR7-fMCivCYfx1skr2Fw02iQhVHMZ8NaXX40M_rTsXvV3NrSj0TtmWo5k9sepHmcAx9gCYQu6nZ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تمسخر امید عالیشاه توسط مجری صداوسیما پس از فحاشی زشت خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107005" target="_blank">📅 15:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107004">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxbgHsiuAOqCBjUkWec-nMkxIhSRAxH_R_fn6AHWirJD-fPAPsLeld__Ja4ti3-2eoYiE7j56JcoFShcY3HfWwk__ed0a7yxmxKpFHGwxKDoyuyrcaPE8IFrvL1rjI6h912VBbaVsjUst_p8olsUrvGFzQLMvk2qotdJjGcwEhSbv4E7TAGNeTEzoCQ0R62X3HhTu1Pst0OPVu5fHsYqoSf5EnhJHzbwW39C1wVoReZwVA-JLkkNmdwu0y575FKijvWpDrS3fZKJsFFQDryJQdYSSmLiPbF01wv_8kBie84XEfkFnE_7SoqGZIV9I-jgsrrYsFxZdXlFulwxq0TqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107004" target="_blank">📅 14:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107003">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBJ8fP96VsY-JupBNKMAEiDfFZ_B477T6B84z6k1x0vqirSCpAvynT5PMXixPGSjCjBigChpJtN1JmKuWmcBsqpNgF7bymwA57P35U10Q1ce6nvhJ3dwAc-rFmFMmwx6OlMf8wZz2FMyIekNxCx432pcrvACeu2vxWxVVlfnskUArGjYW3aAE4hEyaNGInxx9usaoQQpk2F3za6RULnv58a2acpYNHL0fSUip84SkNxkfOISTygT3M3pyJ9iwWz40TIa1iTqTfULGB_Bxd2zRXNcRjDHHL9mxPd4CV_kSFYoP7jpqJjQlGD0HLZd71Cr4aL5dQanzb2lLGQ_OMM7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد تیم‌ملی اسپانیا با دلافوئنته تا سال ۲۰۳۲ میلادی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107003" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107002">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=Iw0LMjvC3jA4RJN6xd37YEcjW5fEO9qUlODOeOT2uh0-xeRF4PtRlhTnfXTP0s3mBGPRbgvX2mkchcFvksViKJ58BZ3mqhUnXGqyos7PblCm5FQrIo7aSMBkh4RcQVL21CkwN7QT6KNniMIAfYZsvvrOKnnNLqGHC9gWKQlxzT2OrCqcyFoj7Xq7oG73BBFmpD_3w2jcHKoRyN_fAcOhDtyFpMk_WNuP22BaT6w6jAD_AfYFG4b6v_6_ZuqbuHJgbWc6U6T3pg66cYNoqMRgyclAL7rXROG1MXDcqGz5PIwpz8Dg4gfXPjByr24nQrSztDaAYDkHqwbKc5xR3TISKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=Iw0LMjvC3jA4RJN6xd37YEcjW5fEO9qUlODOeOT2uh0-xeRF4PtRlhTnfXTP0s3mBGPRbgvX2mkchcFvksViKJ58BZ3mqhUnXGqyos7PblCm5FQrIo7aSMBkh4RcQVL21CkwN7QT6KNniMIAfYZsvvrOKnnNLqGHC9gWKQlxzT2OrCqcyFoj7Xq7oG73BBFmpD_3w2jcHKoRyN_fAcOhDtyFpMk_WNuP22BaT6w6jAD_AfYFG4b6v_6_ZuqbuHJgbWc6U6T3pg66cYNoqMRgyclAL7rXROG1MXDcqGz5PIwpz8Dg4gfXPjByr24nQrSztDaAYDkHqwbKc5xR3TISKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
🇪🇸
بازیکنان رئال‌مادرید و زیدی‌هاشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107002" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107001">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH1oGu_fQOVg9jEyg3G5JCgJA076OxqakPr6Ogm504Au5QisNegppNzG23kNbTinAyf2bRgT98-sr1nbG7FvOs8LZVFISdPKgY_DlZ5yCRsLwI34RTTLpRIa5iIiVaZFp3nlje7ruKKddE19zgFx9EQz8Fbt7XG6ws30tKyO99sk6YCIH70Qg6U-SxvmDA5lUTmNGJBDmQ5hZd3zwYWybREIF7dnHbJnmuYc5yVlNYmbRSnYInlJAUF3pAAmOIuZZUYZ5Zhm6L73z_d-b6_339tzcTrAZFya5cOE5ejmhi4zQhxutRGo653NADICcC86gC_q1kk7gnoSRStWhyOaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل رافینیا، مسی و کریستیانو پس از گذشت ۷ هفته نخست لیگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107001" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7xn5MIsg5xrIPljYykE1Buxx0THJORm7V092mqEsSZRxiB5Jy1SMz3ltlNbmSWnpVuGitvpqg-eayacJ7WAHhGwB7Ds3dXtfdvV1x2UvOdM3exU7yTBGA0GhkYyXtWmjS_r51BgRKhBL0lHDcSpaSpbiZ-i1-09GeDcHPuqJsW7yInC1gL-6ECWOhfBdu6dgp57IH1fqTIM_ED0uHjaN88WER6-2ia0ef6sT6RswIHdPd3UzcMTJQyonIpRAQIL6gW-YIgFUTQ0kSmYtABUfMkuJfCG33YG8aqnapuE5LuBRX8-fZxx6_ml2q1uTsg2qI8XkSWwcENaREFDfLB7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107000" target="_blank">📅 13:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=mrTBX2PJOegaBx4-Ssql8Ul4usmfyMcr79iww_6KWzDVkHFej0DG5ewyQbPDmAASUkxjCPEsyiV7JfhhQHrMwOjlhzMJg7bZoZKuYtFRYBvoKjBvwXbWrYARgmJ6-YxzcjERGqw49EYpoYNAVK6N5sZbkfsAu7V-Zt3U-7bSKQ4rbuzteYq9feilDFiAnpSFJmu1WSuR229vLe-L4gtMMV7dsUEBkzDfMiDl5n8QrxXvFEKxGtqHRacP5eQA_3NSePfGbmyrXauku_8GnX1Of9-jQil132C2Ih0WIeu5DK_2v95DIHDjg6uef3V9SsnhB4LIVl_FNwwjCmQBXHZqdIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=mrTBX2PJOegaBx4-Ssql8Ul4usmfyMcr79iww_6KWzDVkHFej0DG5ewyQbPDmAASUkxjCPEsyiV7JfhhQHrMwOjlhzMJg7bZoZKuYtFRYBvoKjBvwXbWrYARgmJ6-YxzcjERGqw49EYpoYNAVK6N5sZbkfsAu7V-Zt3U-7bSKQ4rbuzteYq9feilDFiAnpSFJmu1WSuR229vLe-L4gtMMV7dsUEBkzDfMiDl5n8QrxXvFEKxGtqHRacP5eQA_3NSePfGbmyrXauku_8GnX1Of9-jQil132C2Ih0WIeu5DK_2v95DIHDjg6uef3V9SsnhB4LIVl_FNwwjCmQBXHZqdIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
اولین گزارش سعید زلفی در پلتفرم اینترنتی پس از جدایی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106999" target="_blank">📅 13:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXaqbuidWjrBmfcRe7DKwsTgJCrfLeYeY44XWQJKjYqh5SYZAPJbuuA5JYal6plTbNJ-kaPCeBTetVpAXeopCIv6BYz58KwT0jLJB3UCw1B5ZnPFoEbmof7sCT1d-ccjBGxrDn4GjjB5JDAjSCi3OxJI-mNz7WUoDnAKP50ogzoyQ0rZkL7qBagXoOwUxaw448iKs01oQCHUxvD2lT6sEhsKB9d_To8fpVkDz64E8ywcyU6vTmiLk1qtKYF2hEPg11_nnrY4b_6uB2CxHRFxG_tuIJgj063RfItS67hm7TWpPU7gUERcbPLwacZHC2SRbCC3NK2OnIjb3SfraO1-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔴
اینو حتماً تو اینستاگرامتون فعال کنید!
برید:
Settings → Data usage and media quality → Data Saver
با فعال کردنش، اینستاگرام مصرف اینترنت کمتری برای لود عکس و ویدیو داره یه تنظیم کوچیکه، ولی اگه زیاد اینستا می‌رید، تو مصرف حجمتون حسابی اثر می‌ذاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106998" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-QO6j4Rzp0HvTi6MDZ9T_Sva_tQaeA88wbmOJeLrf4TzfTSeCfpH-dZlCTEmwJ3xUQdMHOqpm0B48zbeL64QphJOmcrOFMsM5u50mbibuMEdQd7G85_mQjF0RG4XIVngF3xHUGt7hwWb5hA6j343bcXHGKGFqoEoQTFVNk_EP9SGlAp6Q7lsB6ZPaehSgrmxJKtDIPA6tG7PcFc3o8bWu8B-dK0c6ld4FRbvg6Sc9KUVwcsS7ZkC4iMuXUO0GFO9aw7RQ1hpeaogeYOqTAEoxzkXjuXBo0-rdTsIxVLdGqTjIlIMm4fGoR2Ui6Wz1Iw-lcttf8oEGEuFZ9OWrdaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🙂
استاد گودرزی
: متاسفانه پارسال نزاشتن پیاده تا آرامگاه کوروش بزرگ برم؛ اما امسال دیگه میرم
هموطن راه در جهان یکیست و آن راه راستیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106997" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106996">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=BNj3i2d6mbkhAztd2nsbtYJO4qP4bK6LGTeHWPnTuB_hLAI0djw6AZpheySWGPIXFGlV7AJ67U2MLcYILIxCdrZZeaS0J--bT-RY2PpBqZ3Pp9ccREDi4zWvgAZgInUny1Job9VuCCH6DbiW6zAI3ReFOr3egW3cMdt2eDZqesUOxt3kxEfO_4KCJNYN319iQmwxLHtOFOMSytQlyIs32gKlMYANehYkTgKB6lhlwqLR1DqwXHy2rdMXfvfsuhn_bKV-vcNZTzDvhUy4Kj2zlnX8tR2QwJv4w681xFmC3FVndv_8pI8lhymcCK3JNLAVluoRprw3h4VR2Sn64_F9qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=BNj3i2d6mbkhAztd2nsbtYJO4qP4bK6LGTeHWPnTuB_hLAI0djw6AZpheySWGPIXFGlV7AJ67U2MLcYILIxCdrZZeaS0J--bT-RY2PpBqZ3Pp9ccREDi4zWvgAZgInUny1Job9VuCCH6DbiW6zAI3ReFOr3egW3cMdt2eDZqesUOxt3kxEfO_4KCJNYN319iQmwxLHtOFOMSytQlyIs32gKlMYANehYkTgKB6lhlwqLR1DqwXHy2rdMXfvfsuhn_bKV-vcNZTzDvhUy4Kj2zlnX8tR2QwJv4w681xFmC3FVndv_8pI8lhymcCK3JNLAVluoRprw3h4VR2Sn64_F9qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
لامین‌یامال از مدعیان اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106996" target="_blank">📅 12:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106995">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmq5H4My4Fg5S0cJi--DeCiRQxVTDZL71GuHlYB2TQYjX2GQzcE5bzogUDeRQizfg7L-BYc71nAueBHM3GWbbX5NYJ8ZU4Y2HWbt4ohz7dWJZPIsV2qH3uwhCP466l1LrzXS5ofytmznD5XK09GamWN_f4js8YJjeFmavZbArjiPyjBafwswam0I6ibtt72-xE9pPCnTVlzAbmCdlwFoHNoL9AlXHbmqjVScXXjYlVuk2iV6Wn8EG96FDaL-ursugdC3GJ2qtJTi_e-UXgyzKWszivRaWRIvALfGySGu9DRYNo0__yJetNrEiccwkAlbP7VKA6Ic9Bopxfgaqy3cDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106995" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THGD2oQjSw0uSgRcmEwLJ02C_2dfGUY0PJ971mz0UTadobtdX9CBNZBRztTa-dJM7PH__ThZUSJvpY_ePBSMnXC6PTJbzlu9wI1lDr3iPNvV9V3ito70vGht_3xVi-1pI3Pbkb9ULJJN4UMjiGfWp8Xq-GG06nHwzPhOlzWB2nMvALrmCo1NgB4GXFC_yn-LA3B2WnQMt-skYS0svwROBfajxiHKNi04DdTJ1aaxRpoTOAyUjGN0Vqkuz-NkWF35JVXxyQEyVPNOpfYybS2qDVjw4WrowcybCCgE_gNyklR0gxZev7M2tak8ex8PrneQqk_aG2Uayp3UH9fzHJpx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🔥
بهترین بازیکن فعلی فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106994" target="_blank">📅 12:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=CGR4ISDnI5Y2k7w00CgLK7viZ34PL2PHcn6nzF8jaU3bm9UP_lkP1ZD-1RSRJtKFM7EOduXde2OwNw4IQm2hzMQn2i1vNK6nR0R1IIni0rLkYSAHh3jPssaKpOj2bxuX5ZR8dxz_hNkUzgo2lfZE40WVVebOuZKxpYkC8dCNV1XG5WUPHU21PrFnDx8sqIvmRVqE8vJRtju74tNjYFEDOjs4rbTjU6r92xqMBvHemS21Z6lKUONGS2voJEhEZMdt2cIzVjtZSjCIIW5WgGUM7BY-PSFo-hVYAbR3l-F0n0U47d5E5l-moTozDUj2xAz-qCXhnhhsoDDS6ykhJXeNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=CGR4ISDnI5Y2k7w00CgLK7viZ34PL2PHcn6nzF8jaU3bm9UP_lkP1ZD-1RSRJtKFM7EOduXde2OwNw4IQm2hzMQn2i1vNK6nR0R1IIni0rLkYSAHh3jPssaKpOj2bxuX5ZR8dxz_hNkUzgo2lfZE40WVVebOuZKxpYkC8dCNV1XG5WUPHU21PrFnDx8sqIvmRVqE8vJRtju74tNjYFEDOjs4rbTjU6r92xqMBvHemS21Z6lKUONGS2voJEhEZMdt2cIzVjtZSjCIIW5WgGUM7BY-PSFo-hVYAbR3l-F0n0U47d5E5l-moTozDUj2xAz-qCXhnhhsoDDS6ykhJXeNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند ویدیو معروفش که با هوش مصنوعی درست شده بود را بازسازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106993" target="_blank">📅 11:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106992">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETmKAlVE74prLjXPC9W84fPtaIcaXv1_ForWWJj8meFA2lN8eFnkI3pNJZsrKRlmSr14CpSftMPUjTjQXyh40dQy_4v6Anz6aOU5nvS9dnxBQTVwJPJ8vwWzcgT5EC_35IxGL3qeEZRkifE8Cw84t3aeAepzNglwTgs5MNiaXJTCOFuQ_DG-diWtSkaLcj7jZ46G_kj6AFywx9qFTZpCFpZnSPq3VfQU-PALkxJ5rc-9-m1AOP0sz5_BMu0mXOriSowz5ol-aym9gYaj_mnfNapDDG-4pSGA-8m0lnyd0kVOSLbM-9gsdZv8lMBc7gW8Duc3o3bJBYF65ifGH1HDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
‼️
اعلام رأی کمیته استیناف:‌ اعتراض تراکتور رد و محرومیت 4 ماهه خداداد عزیزی تأیید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106992" target="_blank">📅 11:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106991">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=qn4FiJTO7lgqflGrFzHGydsumFRkMo11o5N3o3TbgE12L2TE-YKM_haNEJoHoA0qr9Yv6CJ-8-8QlGkLmk6YYMqua3qJepoW2nlA6roySzBuHVeqbvjdBdXFXSfkgSB5GQ4-ZrO1PvW6p3HoWP_IYXxgQToGfg27EiyqvVKZLzOr3N0dZjZRUkTS_tDL7cttxeMpMw5w9JTUVXUrkVCcoI4zKnimFRxvNXWUmk83RtHoqrhUIpxdQFEeLvSeDCFV_HwUybOSFQL3P1pEwnV8_bSwWYY5XOD8BuEq2G9du4wijhK8xdjRefr9B5T4Z-sdBJk_VhEOIDum34CQfzYHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=qn4FiJTO7lgqflGrFzHGydsumFRkMo11o5N3o3TbgE12L2TE-YKM_haNEJoHoA0qr9Yv6CJ-8-8QlGkLmk6YYMqua3qJepoW2nlA6roySzBuHVeqbvjdBdXFXSfkgSB5GQ4-ZrO1PvW6p3HoWP_IYXxgQToGfg27EiyqvVKZLzOr3N0dZjZRUkTS_tDL7cttxeMpMw5w9JTUVXUrkVCcoI4zKnimFRxvNXWUmk83RtHoqrhUIpxdQFEeLvSeDCFV_HwUybOSFQL3P1pEwnV8_bSwWYY5XOD8BuEq2G9du4wijhK8xdjRefr9B5T4Z-sdBJk_VhEOIDum34CQfzYHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
🇪🇸
ویدیو سال ۲۰۲۳ بارسلونا وقتی که یامال ۱۵ سالش بود و شماره ۱۰ بارسلونا به آنسو فاتی رسید و براش جشن گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106991" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106990">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106990" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106990" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106989">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTCM-t2YLytlPFuXaAwgWi8V5wFgCfIj_sktEpf0MW-i9yFDrv3qPfuv3CSCoGQuGZh_xI2IkPrzRwE4VAOSaQWMezdu_AFCkR8ofk6gMKuP3yc8bjMLpdC99WJyG1rE2vJRUwGDYGnotyvwME5qCqu8S7RNj9QGz5W0pp45D07qG-xCNaKFaDQrfp87KoyYxjopJrVQsD2obb3zVoB54-D0ReC4wg8VAG0w1ZQHv0J3saJZ_ud6f4QznNmCJbX2CSqJa29LTHQgOgdIXq8-y-HxvwetS9P3NllG7SmP5Wg2nPYbO5KuJQjXSbUFhUwzo4YeCphuyg8R1oNYHaBmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106989" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=MWkMjr0j9TsXtoQtBkNfWYnIlFKkjPipWzS-IyQz4JEdJqZjG30rS7qt1KoFMHy0LHiBRBslf5Xb2p80ZB5Nx6yLlSB7MPcourp7oAl1BtHvEr_deVBQdKMJTtBZqaDg1bCvqv3zTma2JPU_l6OGkIojQWDA5_Ub2CT3niFfXcx0Gr9mYJKKHxSeUuc5DScbEoyYe07GPNTYPZZMhFZ5hnRE6HEidK4z50ysfPnsJ1tLj1V8E16JDHAwo4p2q-fYJzogvIzE3GnDDdYKmYVBGkNVsXT0YB0jCUf_nLKsRJr7d1ZVedgjJ0NPi1c772yPWX-rirsw8tZMIoveg5fqhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=MWkMjr0j9TsXtoQtBkNfWYnIlFKkjPipWzS-IyQz4JEdJqZjG30rS7qt1KoFMHy0LHiBRBslf5Xb2p80ZB5Nx6yLlSB7MPcourp7oAl1BtHvEr_deVBQdKMJTtBZqaDg1bCvqv3zTma2JPU_l6OGkIojQWDA5_Ub2CT3niFfXcx0Gr9mYJKKHxSeUuc5DScbEoyYe07GPNTYPZZMhFZ5hnRE6HEidK4z50ysfPnsJ1tLj1V8E16JDHAwo4p2q-fYJzogvIzE3GnDDdYKmYVBGkNVsXT0YB0jCUf_nLKsRJr7d1ZVedgjJ0NPi1c772yPWX-rirsw8tZMIoveg5fqhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدای کم‌گوش بدید
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106988" target="_blank">📅 11:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106987">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=UTI-wqX-x2XtVgiELbUv6cjrynVla_CVZA3PPZ7bN-ebYTJns63uZNztn7pLQ7TenDbvQk5Xwsz0pjmwLUfdkAUcw9Yw7ZuIw3K52fBcQxLqKhFfL8dZC51gedSkkhXD4EDknOiOpac4MXNB4yUGW68OgML8yk1R5eUVdNLeZy-YQo_fVxwDPEHWqabhSY-oWNifyYWgkz7paPsytXUIZHXpL6zp1Yp9uzfLWLCEHDzoN7bDLtiU0y-YV7Xo_FQwCHVIwkAptM59l5U1jmrsR07NjVoZGwd9hyrel6Dyom0sVhBQklA01TJrx2qbSJC5LfgYDX6d-b0S1nVpXMnjXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=UTI-wqX-x2XtVgiELbUv6cjrynVla_CVZA3PPZ7bN-ebYTJns63uZNztn7pLQ7TenDbvQk5Xwsz0pjmwLUfdkAUcw9Yw7ZuIw3K52fBcQxLqKhFfL8dZC51gedSkkhXD4EDknOiOpac4MXNB4yUGW68OgML8yk1R5eUVdNLeZy-YQo_fVxwDPEHWqabhSY-oWNifyYWgkz7paPsytXUIZHXpL6zp1Yp9uzfLWLCEHDzoN7bDLtiU0y-YV7Xo_FQwCHVIwkAptM59l5U1jmrsR07NjVoZGwd9hyrel6Dyom0sVhBQklA01TJrx2qbSJC5LfgYDX6d-b0S1nVpXMnjXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
تعداد‌گل‌های این فصل رافینیا در مقایسه با چند تیم مطرح اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106987" target="_blank">📅 10:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106986">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxMx0wJkst91TrYqx7v5UQ7DTzwZnbLEgrO0uUNOQe52MdOiQMtCK1WP6uCAp6yEaDDB_d_Ft-hFCPYVcpnsTnopzBJ4kwu88b8JHgECWTGhuXTgH1AtdLkl2QMCkCSAR_HOT3cr7ArcnUgXqSo1V71OS30F27A4FIKPdPusEHT6yxYJwlZ9V-eyOIYlIWPOJB232w6kmZQk-JNzpcC8djGw_do08twpMMjUf3qYapcQXfeh4BqpMTX-jsN41i5Xw-Sfz-lPTjnfArX8n4TqS-Xt8zp4pmd5E7rHmHI3mOXp903PUmKrAiV2ebla6PTNMRSZfkDDMQjBk-PDjzorFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
احمد ایراندوست از بازگشت شادمهر عقیلی به ایران در آبان امسال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106986" target="_blank">📅 10:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106985">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=o7ojyut6bm4Ur0GDCnc9bcpgskqmLhta3Eym10ybzkUj6SVSGK7ToBgOB7KF7tGE-PAn6yMBEGfv5EWcKIuwV7sZSgNtrAZ5aYelqlW9_DZRbTBovdKXUwwOPsOnKTsX4rIVB-n8CQSfEAnd6q-lOEDlWT0dPOm74GhFqvQ_EIcOQyw6CGJIEOFvc8HsQLdxy8tg7klz1PgwSKtZ00WpBlHBm8H-eMi33jVDWEsaw37dZEb194jwh-8O8JqzTILR_fL84WcHqMBM39OWUlYOhWfNFvAUb1o9ZBwjyGN_SBvjAj-WqflreteswO7xgd0faA9Hju1zS1_uRNcbsgwRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=o7ojyut6bm4Ur0GDCnc9bcpgskqmLhta3Eym10ybzkUj6SVSGK7ToBgOB7KF7tGE-PAn6yMBEGfv5EWcKIuwV7sZSgNtrAZ5aYelqlW9_DZRbTBovdKXUwwOPsOnKTsX4rIVB-n8CQSfEAnd6q-lOEDlWT0dPOm74GhFqvQ_EIcOQyw6CGJIEOFvc8HsQLdxy8tg7klz1PgwSKtZ00WpBlHBm8H-eMi33jVDWEsaw37dZEb194jwh-8O8JqzTILR_fL84WcHqMBM39OWUlYOhWfNFvAUb1o9ZBwjyGN_SBvjAj-WqflreteswO7xgd0faA9Hju1zS1_uRNcbsgwRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟣
گل‌تماشایی لیونل‌مسی از روی ضربه کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106985" target="_blank">📅 10:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106984">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=ClK-W-Br7Epn5d9xacxnlZY1kvii9FQwWjzp06L-r2LYHboxG2x9W5shdS0-BolLgIdfP70uGm2bhlc6fc6Ah0DyFu2A-8naTDxabznFKoaGrZeC50hw7OC-UekTn4xCOOZHTgOWF1XHLoDj4VjA1g37F_REIR0rrhbdqMUeoGLVNT_2BX43QK3b42fasYToS-IHPR38zg7z2X60jcP6aoCJSaGwyjNnscj5E-ZInOS8Crd0q4FyqIadRFUh7O5jEDfjrPne_F8PTWu-59vdJfobYCZFbEQhVes70TCKGeN8UK2b31qauKgXwqmRmDIkF8cLI5iJ-wLsK3CfatJtYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=ClK-W-Br7Epn5d9xacxnlZY1kvii9FQwWjzp06L-r2LYHboxG2x9W5shdS0-BolLgIdfP70uGm2bhlc6fc6Ah0DyFu2A-8naTDxabznFKoaGrZeC50hw7OC-UekTn4xCOOZHTgOWF1XHLoDj4VjA1g37F_REIR0rrhbdqMUeoGLVNT_2BX43QK3b42fasYToS-IHPR38zg7z2X60jcP6aoCJSaGwyjNnscj5E-ZInOS8Crd0q4FyqIadRFUh7O5jEDfjrPne_F8PTWu-59vdJfobYCZFbEQhVes70TCKGeN8UK2b31qauKgXwqmRmDIkF8cLI5iJ-wLsK3CfatJtYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لوئیس گارسیا پلازا، سرمربی سویا، پس از شکست ۳–۱ مقابل بارسلونا:⁣
اونا خیلی، خیلی، خیلی، خیلی خوبن. همین که تونستیم باهاشون رقابت کنیم، کار بزرگی کردیم؛ چون بقیه تیما رو جارو کرده بودن.⁣
توی فوتبال یه‌سری اتفاقات هست که نمی‌تونم درکشون کنم؛ اینکه رافینیا جزو نامزدهای توپ طلا نیست هم یکی از همون اتفاقاته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106984" target="_blank">📅 09:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=E9yxrpTaZdtCu2aVkHMCI-X5CSyWjdJ4KrayZd5OktDYrvpA-jFFkliaMwMHviaYsFY1NhajmWEVkSIDPxPyGgJjhBlmaWBsBQ4drF82T06wjlH9-iHoB1RuNzyr0rHo6C9tc1R5PslvFTAGXjm8YfXtHq7V6x3Xmw4H6XkgnQW6d_cqydlLE2sRn6s2MvtDWOb71VHceLkLq1b1WWBy1kKwNTWcQF-dAhJMhL7Ko3R3ovgQiVsxCJsPo8740aNYJskzDNwlQKTql3Jqf51OlQnb58pP_O2o6MDkwTHhkOUY8gxa0b_bpkmGd_xuSDg_pZPltUqwSWHnWjEbT2iIgDW3Af5NNtp2GQXVi5PzuANbECNZbsCtC3r9M_aPdb0I5lBozOLlqBy3hn344Ns9a2S-p01Y8R6fFiFEKVEuh9Qg3BhedLlLzc0md52zvFdyhCImjzBuOCRsozYdOZW4SkKATvF5-zjIXGZm8MqPdbEA0knBIbCmmxbKlrEHbCZVpqoJHnhbvcxRTRzn-DRetla9Ey3OQtoo59bew_qZnOgrAcCuVItHJHnX_KMUJq2LF2UGaVNw_bj34Bnu_C5Ig0X7aT2XFk9IlfLfAZ9IJkRQJx_sNFuc8EoZdvLbN6K1cBiasqW_4_emZCUoBhmiiOidhBeg0N-f8OE1e5vRYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=E9yxrpTaZdtCu2aVkHMCI-X5CSyWjdJ4KrayZd5OktDYrvpA-jFFkliaMwMHviaYsFY1NhajmWEVkSIDPxPyGgJjhBlmaWBsBQ4drF82T06wjlH9-iHoB1RuNzyr0rHo6C9tc1R5PslvFTAGXjm8YfXtHq7V6x3Xmw4H6XkgnQW6d_cqydlLE2sRn6s2MvtDWOb71VHceLkLq1b1WWBy1kKwNTWcQF-dAhJMhL7Ko3R3ovgQiVsxCJsPo8740aNYJskzDNwlQKTql3Jqf51OlQnb58pP_O2o6MDkwTHhkOUY8gxa0b_bpkmGd_xuSDg_pZPltUqwSWHnWjEbT2iIgDW3Af5NNtp2GQXVi5PzuANbECNZbsCtC3r9M_aPdb0I5lBozOLlqBy3hn344Ns9a2S-p01Y8R6fFiFEKVEuh9Qg3BhedLlLzc0md52zvFdyhCImjzBuOCRsozYdOZW4SkKATvF5-zjIXGZm8MqPdbEA0knBIbCmmxbKlrEHbCZVpqoJHnhbvcxRTRzn-DRetla9Ey3OQtoo59bew_qZnOgrAcCuVItHJHnX_KMUJq2LF2UGaVNw_bj34Bnu_C5Ig0X7aT2XFk9IlfLfAZ9IJkRQJx_sNFuc8EoZdvLbN6K1cBiasqW_4_emZCUoBhmiiOidhBeg0N-f8OE1e5vRYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
سوپرگل فوق‌العاده در لیگ‌کشور مکزیک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106983" target="_blank">📅 09:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106982">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=jXQ_OrQlYtGGJAkoB9STqYdY7eOQUqAwTrABV3KbJ8aVWJOrP_Hu6OzDhWJccwrNr1YPO3xyNiDY98Mn08BWP-jdzkVglILiUT5gdn3G_C2jxiU_dNSlh1YRlhZq-F_g8Nf6tvB6PiUxSo4gNDGNM9oFWwPGzlgo3f5zfovt0cmjVqb-p1ryBUIC5VjDYPgG64fBJhU4xp_G6veanZ2-g0ZEvZHk5SY7LVj4nn6qhO5cfHYsylPJuluCJmzfA9oqs6ZJoVWZEt_rahc4TykJvOXEhloDb2sY9T_No9N42VPGFvBxWOtl0Pa5aiffFq74MnlqrZcIDHfXZxvXc9_RKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=jXQ_OrQlYtGGJAkoB9STqYdY7eOQUqAwTrABV3KbJ8aVWJOrP_Hu6OzDhWJccwrNr1YPO3xyNiDY98Mn08BWP-jdzkVglILiUT5gdn3G_C2jxiU_dNSlh1YRlhZq-F_g8Nf6tvB6PiUxSo4gNDGNM9oFWwPGzlgo3f5zfovt0cmjVqb-p1ryBUIC5VjDYPgG64fBJhU4xp_G6veanZ2-g0ZEvZHk5SY7LVj4nn6qhO5cfHYsylPJuluCJmzfA9oqs6ZJoVWZEt_rahc4TykJvOXEhloDb2sY9T_No9N42VPGFvBxWOtl0Pa5aiffFq74MnlqrZcIDHfXZxvXc9_RKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله بارسا و رئال به شش امتیاز رسید.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106982" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106981" target="_blank">📅 01:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106980">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/106980" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4uMo4tb-2L-ALE9eU0EylZ2xDkvKWt6vZ5LH7cj22weoOsdtwZW9QfA35Qxah9ivOmHdBsCw0DQtwuUgWsSO6UZs7vSvMW6zdgQmycViF7AJhVi_c393cXQ9BfeSo6yDyZ9PWfnlreZs67agTVcSrXNeufGa-TRK2JbCGAohx6JACpyRQW-GsopfCjCNAp8SshnheDALn1Enmnap2tdiYp5KjSFdZ-AptXdvjLpXzwnEmBG3Z3UEoYWQ_G3bSw7dnFbk2XbdsGXBqCqVmQOuivGl856bySnVZU5WbS-ItgJQ3uMqLajhZ9_uJYqhNB-pL6qC-Q47UeFZpPQ_Kqs5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
سیمئونه درباره بارسلونا:
🔻
انگار اونا دارن یه ورزش دیگه‌ای رو بازی می‌کنن، نه همونی که ما بازی می‌کنیم. مهاجم شماره ۹ نداشتن، ولی یهو رافینیا از راه رسید و ۱۲ گل زد. یامال هم اگه اشتباه نکنم ۷ گل زده.
🔻
توی زمین خودت بهت فشار میارن، زمان رو ازت می‌گیرن و از ریسک کردن و گل خوردن هم نمی‌ترسن. حتی انگار گل خوردن باعث میشه بهتر بازی کنن. اونا الان بهترین تیم هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106979" target="_blank">📅 00:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIgtIRJXDCx6qbq553ToDfhCwdIQmI3amIvZuicm3yJNekfytM7yiFwyMjxC-pODayaJOU0koL_buv1_SXLxeLLqGVGTfFxTtKH_2LKlGrqjEXtzCvvdWAilmhDNmUKCT8rF14LTcpA0lxeDfAfhTNeVPXVXv83p30LfaVpoMXocimGOQn7QB82n0kPQ8xfMZbR3b_gSkKCEaciPuwcSBWGuDri9WHRzFKxXT5oSnrbsMPEp4puUlSq32_77BI8H74VI-1IvL2BcWoCbH_7TZxjFOk_gLBQe0EKvuCDnJTIIarfakqbUU9Ucin5mgCTY0rKTH_GOKbrHUieepUQkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⭕️
شبیری‌زنجانی از مراجع تقلید شیعیان دقایقی پیش در بستر بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106978" target="_blank">📅 00:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106977">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGaAxhkUyzvaoyb9M42flK71rGtLrZPFuAQlgj5oB6OosnM300-qQDL0Eq8lNwTzveiZfvGNuMPAgCy6AKZb2HHcSnnihWa2hqjDPlBD3PKFsDi_OcQtsYnqOFTVwBUDouDFThRv37bW66X0EBLvrcwvXaJwW1kzVU9kyP-X81LzS0hW9dLH0c2MH4Vlz26wQQAj98ab8K5udmMSQeHWMdgKDObctNlwRq3TzaPJI3cAVvf-bAnPbP8PEMDZlLbxt9LPCmK5qFJJa9vd4KBZlGwzzaYvgfJSXxUHJ6c8yava4Mf9agHoJfp9IEa-qbU7EWSE5ojBf3zRPd7FeJrYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106977" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106976">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU4VmTJ_wAsP2uOHpLiZZ-_BvGYK2xqGWWMZv9HvNYPLL_Qz_xyopZjq0U3aRWw3G3KBi2T6HZxzT7auOpXJfjvRKnHRLiWij1QZaXGVXnhPTcEizcXZE6WWjG8yEcsCNYktP48I1J6fdOx97nNTeVMIi7n10bWelUu6qQKIulFEmMTUSadYWDd8vZ-n4UAqLLxJV3mFHUlETNlqj3Ak5NPHjxRis29-1MZ4uZT8hnKzN0hN-MMsQ-eT8QUOHx_7gL7r3tzTD52elSW1c5fGeG2XmtkKcdsK8ktVXRMIvEGQzcIm55Ohx-Z60cZXblIAVpY87QSkRwTwqMhtH80t4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بارسلونا در فصل ۲۰۲۶/۲۷ تا اینجا :
⚽️
۸ بازی: ۸ برد، ۰ مساوی، ۰ باخت
⚽️
۳۶ گل زده
🥅
۸ گل خورده
🇧🇷
رافینیا: ۱۷ (
⚽️
۱۴ گل،
🅰️
۳ پاس گل)
🇪🇸
لامین: ۱۴ (
⚽️
۸ گل،
🅰️
۶ پاس گل)
🇪🇸
فرمین: ۶ (
⚽️
۴ گل،
🅰️
۲ پاس گل)
🇩🇪
آدیمی: ۵ (
⚽️
۳ گل،
🅰️
۲ پاس گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گوردون: ۴ (
⚽️
۰ گل،
🅰️
۴ پاس گل)
🇪🇸
پدری: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اسپارت: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اولمو: ۳ (
⚽️
۰ گل،
🅰️
۳ پاس گل)
🇧🇷
ژسوس: ۲ (
⚽️
۲ گل،
🅰️
۰ پاس گل)
🇵🇹
کانسلو: ۲ (
⚽️
۱ گل،
🅰️
۱ پاس گل)
🇪🇸
برنال: ۲ (
⚽️
۰ گل،
🅰️
۲ پاس گل)
🇩🇰
کریستنسن: ۱ (
⚽️
۰ گل،
🅰️
۱ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106976" target="_blank">📅 00:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106975">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=JBg485njtooxIL0sUtSHQ0-PAQ4zOSr_P8hXWSFAT9sU8XH2BrJeb48YMrVNWu6I8_GaT_Y_Z6TRPklZIwy2FmiTuJJ6SNYeNBW7_Rnx3N12HHSsTj16Eg3Zo5l9FDrx5xzYrvo9r2Ecuoo7cq423q3hZIfP8v3zBzfzl_H4AIle_ClCEG0Z_IauxRYNh6l7Cb0WxswXdntbi5l7ohKFx5NYIK1xL4MCQCqEYrISR68r9q2CPGniYTenLTitXRuQLlgS1wp4QrKasDcsuIf-GDXasoPrwBHVGhoxgk5yRjb1fr9YH18bQhQz-mrjkOA0biHJXg7Hn0X-QDYARCcicw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=JBg485njtooxIL0sUtSHQ0-PAQ4zOSr_P8hXWSFAT9sU8XH2BrJeb48YMrVNWu6I8_GaT_Y_Z6TRPklZIwy2FmiTuJJ6SNYeNBW7_Rnx3N12HHSsTj16Eg3Zo5l9FDrx5xzYrvo9r2Ecuoo7cq423q3hZIfP8v3zBzfzl_H4AIle_ClCEG0Z_IauxRYNh6l7Cb0WxswXdntbi5l7ohKFx5NYIK1xL4MCQCqEYrISR68r9q2CPGniYTenLTitXRuQLlgS1wp4QrKasDcsuIf-GDXasoPrwBHVGhoxgk5yRjb1fr9YH18bQhQz-mrjkOA0biHJXg7Hn0X-QDYARCcicw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم پاری‌سن‌ژرمن به مارسی توسط مارکینیوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106975" target="_blank">📅 23:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106974">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=qJhzQMKAiRifGu5arQSJ90Lru57sTO3TmWmd-j0bt2XCVEuUygWc1EuvocjG8rMG1R5uUfD1jluvU007mVd6m0QqSX7ErOwcjMXewgNIL5ARtU7ZvefZhkMTBePVLInd7IRN_bEbRzDNJFREY7ZCyWDDCjv-tLQuiSYVWLWrT1yjjVj5xsMBsb1pjTqXF3Sn-VVy4VH6tjvLwxO8sP3OClSxKejfLj8pBFUd-gwBIKwwzRUBli0Vmm0LAiZbnUOo7pvx28mTA4lISkLgboaa5vaHLvYxXwHN_rfjHSxDPoz3AhMETNlUJR16WT_0ViiEeFG75HM73ewYIwAcA7edUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=qJhzQMKAiRifGu5arQSJ90Lru57sTO3TmWmd-j0bt2XCVEuUygWc1EuvocjG8rMG1R5uUfD1jluvU007mVd6m0QqSX7ErOwcjMXewgNIL5ARtU7ZvefZhkMTBePVLInd7IRN_bEbRzDNJFREY7ZCyWDDCjv-tLQuiSYVWLWrT1yjjVj5xsMBsb1pjTqXF3Sn-VVy4VH6tjvLwxO8sP3OClSxKejfLj8pBFUd-gwBIKwwzRUBli0Vmm0LAiZbnUOo7pvx28mTA4lISkLgboaa5vaHLvYxXwHN_rfjHSxDPoz3AhMETNlUJR16WT_0ViiEeFG75HM73ewYIwAcA7edUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی مارسی به پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106974" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106973">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=sc344ZoyHjbEZ-fc-jXo4ibufY0aqv-bCffXgLGleOR5N3Bv4PoBYvIQYVgRWiYT_xnrpaz6QDr80Z59InaCg9ggsAMFyiPjhJw28_9tTu1UFFAhtFmdK1JzLpV3OrtzYjsQlrf9TKHv4P_6ENIqnVkQ6Fd7B5DmQ79w5hw_OJW6ah7H82xn7RwKq669FnFbx0lGJSVD-XA9EGzAEJQXw0kYtDUdTR9RdkTm1iCe04hXfiGEi96EvgN80gp3YBOWezqSpO9qGpMPCXaoTla44Wnw3o_Bvq_fKAS0fsgtVd525S2MuBHS2HDVzdAyncJIL5Wm31X5MaN_z7kIEVbOYBGIbK-pYs_apxXqh3MAjcJ_JR_Ov9tkpGBE-VaWljiPGd7symQHOfYWrLu65imS6ljZpbwLWXpshV_bM-DT39gv-4iyDxdgHyTMQTkGQ1wgHVwBX1fQvDq6XhFXsobBqsvKHAIOzvwM-Wg9u1vlVHMvsNyKFKRWeuyfkYCB8lyIdfwQB4lwmvmvha-Zxvvg5grJTHP9wMwg_OR6tGoCGnOn2lA82nObU8VrCkhtwS3zT8wyr65tGCfjRK1zA9tViIaMcB4QsRcls9z6Okuo1bxBTFqpjJ9iDCFGVVZd5j9MsZlhn5x8b42vzvOTqlV_o4Ku2CEYEyo6c72qbHouUeU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=sc344ZoyHjbEZ-fc-jXo4ibufY0aqv-bCffXgLGleOR5N3Bv4PoBYvIQYVgRWiYT_xnrpaz6QDr80Z59InaCg9ggsAMFyiPjhJw28_9tTu1UFFAhtFmdK1JzLpV3OrtzYjsQlrf9TKHv4P_6ENIqnVkQ6Fd7B5DmQ79w5hw_OJW6ah7H82xn7RwKq669FnFbx0lGJSVD-XA9EGzAEJQXw0kYtDUdTR9RdkTm1iCe04hXfiGEi96EvgN80gp3YBOWezqSpO9qGpMPCXaoTla44Wnw3o_Bvq_fKAS0fsgtVd525S2MuBHS2HDVzdAyncJIL5Wm31X5MaN_z7kIEVbOYBGIbK-pYs_apxXqh3MAjcJ_JR_Ov9tkpGBE-VaWljiPGd7symQHOfYWrLu65imS6ljZpbwLWXpshV_bM-DT39gv-4iyDxdgHyTMQTkGQ1wgHVwBX1fQvDq6XhFXsobBqsvKHAIOzvwM-Wg9u1vlVHMvsNyKFKRWeuyfkYCB8lyIdfwQB4lwmvmvha-Zxvvg5grJTHP9wMwg_OR6tGoCGnOn2lA82nObU8VrCkhtwS3zT8wyr65tGCfjRK1zA9tViIaMcB4QsRcls9z6Okuo1bxBTFqpjJ9iDCFGVVZd5j9MsZlhn5x8b42vzvOTqlV_o4Ku2CEYEyo6c72qbHouUeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول پاری‌سن‌ژرمن به مارسی توسط فران تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106973" target="_blank">📅 23:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106972">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2832d49487.mp4?token=PcnHibd3XFEeEyDdi2oy5EXdjG5qofsuNpw5smzMDMouK99i67zh6WMcHMzY24cGUfacEhFmodidNkaCYNjrTg2xa9HV0i_WBFTE-ooen_5PFliC-q3clEa8DDhE8OwKFToTx7aaHX9XMYlvBNKhikeLVdMeQB7dmYFMWf2mhGfmpdJkH1pjUivdmGVcIBtF_Ex1_vfmcJK9KwOZR4waYAIrzkiueJ8xQKmcQaURklJjMQubWlq2Frmpk6bdKaW5Mp3oa0C_BSGGsJIxjI39el8LIQf3_0Ge_lhLHhO_dq3o-G3qD9v-QqktTWHGcEBkKBewZ3-kJ9DCMmvs1-I38g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2832d49487.mp4?token=PcnHibd3XFEeEyDdi2oy5EXdjG5qofsuNpw5smzMDMouK99i67zh6WMcHMzY24cGUfacEhFmodidNkaCYNjrTg2xa9HV0i_WBFTE-ooen_5PFliC-q3clEa8DDhE8OwKFToTx7aaHX9XMYlvBNKhikeLVdMeQB7dmYFMWf2mhGfmpdJkH1pjUivdmGVcIBtF_Ex1_vfmcJK9KwOZR4waYAIrzkiueJ8xQKmcQaURklJjMQubWlq2Frmpk6bdKaW5Mp3oa0C_BSGGsJIxjI39el8LIQf3_0Ge_lhLHhO_dq3o-G3qD9v-QqktTWHGcEBkKBewZ3-kJ9DCMmvs1-I38g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم لخ پوزنان به رادومیاک توسط اللهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106972" target="_blank">📅 23:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106971">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_n43A2F4YCAr5zasJF_udd1q6ldT-4bxr98vHd9UgLb--f-beIlf6bJqw5NQIo8d8h2oSw-KX4OVgwKR-GpVH65i5g6UtdJ_l7mg943fNZlTwHFUE2s9qEP_4yB0_mFoSnUYuwExO9pAMM9-4X67A5KQXqVvKfqErnkoibnq9KHfYLZw3UDAaq2QlQ4Ih_6nftgVLIWuNzhafH2uV9V8ENCi5IiycUv8QEYRuZ1HBVoy2sm5T-IHyApgVEr23MJuCnS2xqDyk2xKTG34eAH-oru4A1Z5V_wdHJxbcKN6CvR1GLEHWxN9eDf6GUhzBRT8de27UFizekGs80vJDhxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ترکیب پاری‌سن‌ژرمن مقابل مارسی؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106971" target="_blank">📅 21:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106970">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=Dm606hUBBXRW4sMw-qY8-q3oFGCuO87qNDvhU7HVPAKBmCG12Ve2zKr4XWys7CnLD2gANgxVR-QALIF192dC_Y3zBsdIqliYtBwq_t7TL5zMPaP51vlRUj0mW1PTDu2d0ZSwmtHFnrKsA1Nm-mNzlmIyrrRxOFNBSGRVufY41MKXuBm8BuKnavwVHas3A1cY1IoiWqHjb-pUam3yfG4GmGNklqBHc9YyG4M25L3clKZLS24MWJaQhjjyaWv6rgajhX8EW6v10poeX1UHu5hGvtPdo1yCXb7Eulx4Qel-HtMzL6r9C2dc7kR1YTr92PPZLrAiwKLU44KhLZ-Htxmz3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=Dm606hUBBXRW4sMw-qY8-q3oFGCuO87qNDvhU7HVPAKBmCG12Ve2zKr4XWys7CnLD2gANgxVR-QALIF192dC_Y3zBsdIqliYtBwq_t7TL5zMPaP51vlRUj0mW1PTDu2d0ZSwmtHFnrKsA1Nm-mNzlmIyrrRxOFNBSGRVufY41MKXuBm8BuKnavwVHas3A1cY1IoiWqHjb-pUam3yfG4GmGNklqBHc9YyG4M25L3clKZLS24MWJaQhjjyaWv6rgajhX8EW6v10poeX1UHu5hGvtPdo1yCXb7Eulx4Qel-HtMzL6r9C2dc7kR1YTr92PPZLrAiwKLU44KhLZ-Htxmz3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106970" target="_blank">📅 21:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106969">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHBDf43LbIt9ds6WWXXqfZciNHpVzBw4VeJegnvvl0ndyqgGUAYQj6WUTY43UlbKXYXkeJLeRQHDO05Jn-maVQYhVOjLErdPnq6AKg57L2W7CSUsOLeX5q4qWOUqIJyiv1gE_bgUsENu3nm7ew17jXBHFLqXN7NnfbEr3ILPYeA03wTMCduq0SkY3GYd2XQrZWQXgkPpajp8hBPlIxTiwS6NkkhoqwBVIisU1z93Fzh200FgihbNj-S-r7NFi4fcxoDMfPwJhl-LpveP0Qnb1Ax3XcJNE0sL6eqbVsd0SyskqdiRrYrJ6Zi7T8t1DBnjKj0kFTwlRVCCZGb5zQaThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مورینیو در ۱۶ فوریه ۲۰۲۶ که مربی بنفیکا بود:
تو یادداشت داور نوشته شده بود که شوامنی، کارراس و هویسن نباید کارت زرد بگیرن، چون بازی برگشت رو از دست می‌دادن! من خودم سرمربی رئال مادرید بودم، واسه همین خوب می‌دونم اونجا اوضاع چطوری پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106969" target="_blank">📅 21:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106968">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGFusLkhENWmvZIh-DwjxhHwtr4NZXCvF6K940lNG8wies9d7hNXMwhpRmPMR8n-Xdmp38Yr8Cj4ecEGPGZPVLdasY2X467TSUDSRWknkC8vsm-kBrLp08gv2I7CzRwlTfcc5F5fVKt6cCFkPsyVS-pY6_RmslPhR6YqenSAlKdS8rhzYuqf3dQJGZTATF_yMkuQoocD-BFnGHEL0Xp0mPstMCogXIJwKlQ65FUpWejQN0PDXmXdFP36LKiywLVk8zCQm209noCaGdROSN8lL8-ctryyR12xxtJv2auCp6wr0AdOie42m3Ihn_aKXzwpIXf5WeLTjfwvx3sBWNgoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج درخشان منچستریونایتد در پریمیرلیگ؛ عجب کسشری شدن بعد فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106968" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106967">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=q14jsc9aKiR-MegT7cwWD80omvUDxfb4TCQ5xAgmqxj1CNvJqvgF9HBkB3gIwEiLYGV_EkRz41eugz5d_dGyXVOzgueO_lDBHudkKvMZZvy_z8hml1NuGsRLJxmK2RH_5w1GJTTWfGpNi4TKsTCGiv-BtRQjt0Tjy6G0uGscVj3N6JeIaGwY-E3lBPuxxdQz6FgZ2rFoKVxIM99ydGrQkKRSs2QkEZ24GBjsYPVyjBU57LGkL5kvG30uBRgpsMCtcD3Gefla-MIoOQVFyd8W-Ngvi6dhsaEskdif8H-LjlEpvv0xDvaeMVYsuTqEJyVCfDBiG9B1L1tZa7pTMMCyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=q14jsc9aKiR-MegT7cwWD80omvUDxfb4TCQ5xAgmqxj1CNvJqvgF9HBkB3gIwEiLYGV_EkRz41eugz5d_dGyXVOzgueO_lDBHudkKvMZZvy_z8hml1NuGsRLJxmK2RH_5w1GJTTWfGpNi4TKsTCGiv-BtRQjt0Tjy6G0uGscVj3N6JeIaGwY-E3lBPuxxdQz6FgZ2rFoKVxIM99ydGrQkKRSs2QkEZ24GBjsYPVyjBU57LGkL5kvG30uBRgpsMCtcD3Gefla-MIoOQVFyd8W-Ngvi6dhsaEskdif8H-LjlEpvv0xDvaeMVYsuTqEJyVCfDBiG9B1L1tZa7pTMMCyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول منچستریونایتد به فولام توسط متئوس کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106967" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106966">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnxZmjsWh5grQa3guiOq-YgGob2ElBntWSNeEnqzId2VUoi2YPY_tKwcjZcVbssgH6oE9bWAvAbeCKvi5Edtpyw1VP5ncJsTajdD4iNW1UeJzvBQ5UV_EelEheStEfFj-ndJRX1hXS0JJTK04tMOaIk0Dvchff8lG-QH6vlMM77Dtx1y5mjnM_F_ReffISpvysgBLmhs90wdrtv3aOlyxipydHdFmkfaUMfrcM7vVY0B40yKJOUMKVONXqLDIrRM_EcTnkP3nhi1SKsMoOI99V7sRDw6muaVCSPkkz5Pler3fpF7fLZhXcyZWeAHV_5NFc8juWOYubgYThFI76cadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
رئال مادرید Tv:
🔹
وقتی پای رئال مادرید وسط میاد، برخوردها کاملاً متفاوته.
🔹
لالیگا و فدراسیون فوتبال اسپانیا اجازه نمی‌دن رئال مادرید رقابت کنه... اون‌ها یه نقشه و برنامه از قبل طراحی‌شده دارن.
🔹
دیدن همه این جریان‌ها حالت تهوع به آدم میده... اصلاً براتون مهم نیست که کثافت و مزخرفات تمام لالیگای خاویر تباس رو برداشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106966" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106965">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da8be998.mp4?token=gVlbyf-_w7G0OQ0iaWhT4aNLadN66l793sjYrNzftmrTmgrUHo__O-y9HH-pVJEZgjqgYwzt82CN6lOi7rO-9Wg5_ESZ9sQwE7Irj9yS0CK9MiJZAd2vIibjuWwMfi8X5ZVgWpu-5xXkWkPoETMW7_uQz6dqNa0A5Ojm8gOFPh57iws6oZNsKWoAN50dWiam8mHDz_NB7I7B4WN-9sVK-fxTkOxIfGailBqvqGg919iT_q372cvFdoSJL3Z0OC9wzMI4w4ZcIVuTeOgwREThgMwfVHmJ_bc5ngQ1OCuSJo-5fEI9ikqbdug-UUj02fiQKGmEsCeMS3gp1mazWrkJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da8be998.mp4?token=gVlbyf-_w7G0OQ0iaWhT4aNLadN66l793sjYrNzftmrTmgrUHo__O-y9HH-pVJEZgjqgYwzt82CN6lOi7rO-9Wg5_ESZ9sQwE7Irj9yS0CK9MiJZAd2vIibjuWwMfi8X5ZVgWpu-5xXkWkPoETMW7_uQz6dqNa0A5Ojm8gOFPh57iws6oZNsKWoAN50dWiam8mHDz_NB7I7B4WN-9sVK-fxTkOxIfGailBqvqGg919iT_q372cvFdoSJL3Z0OC9wzMI4w4ZcIVuTeOgwREThgMwfVHmJ_bc5ngQ1OCuSJo-5fEI9ikqbdug-UUj02fiQKGmEsCeMS3gp1mazWrkJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
حالا که بحث جنگ دوباره داغ شده؛
اگه تو آسمون یه جنگنده دیدید، سعی نکنید بهش شلیک کنید یا سمتش سنگ پرت کنید، فقط این فن استاد رو بزنید تا خود به خود به آشیانه‌ش برگرده :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106965" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106964">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=qALIGmHI4WQhPpQqxmpTLk3JS_sHUE68NVyry5bhKgKPHVQd_pvX7HYsqsaI33bqAI5zSRtLkXTzD7YD3jJkEbbQdQYadErrxw1EGDJg8nyD7Li_KqTSYDdo6FhZW0GC4B8AZWU4fiAq8_T5qU7fnGd1mJvA54Puu2If1bdBvRVCpUVV9Pn2VRTOHMgw2iYIsMEnBCRt1U74rl0RuCuZ53U2f2MZc_O2I37F7kkVqsXhjjT6zwoVILa3eBqEq3xCgeH5zAEgdQE6yIz2LBANTYP9kcZZlRBc-f6qaXkMnuonNolQ7YZSYOagGw9wstY8A2RFGo7e2713Ns3J_4MDbi0xGQ8I6046DxDZE95eb8XGGluD1NcHcNnZgzJT3XsGF26lwtiR1kLHWgwuGhztmYgcLUst7MKMolGAZrEetyBaZ9RxKJO0_TgAAnpQdR9hLYqYItFyEtpj64IaWa9iAYdeF3vHUcKiKJmG4QXvAmc8RTooOyUwRO9rqDy7B17M73k7yTFTcs-G-mHNJ54PuvOwXyzpcMsejK49fGhm-CwNLCcC3LCPXyWugret2IhHflTkpSTeh9SpfGhviGZmGNJgv4VLD3KUpgQpZC-KQA1asl52kTbczCzyDPtBuimlVAcyvYXHU0MY1RXN64JsEr6T1VuH9adNV9Mtsht9BuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=qALIGmHI4WQhPpQqxmpTLk3JS_sHUE68NVyry5bhKgKPHVQd_pvX7HYsqsaI33bqAI5zSRtLkXTzD7YD3jJkEbbQdQYadErrxw1EGDJg8nyD7Li_KqTSYDdo6FhZW0GC4B8AZWU4fiAq8_T5qU7fnGd1mJvA54Puu2If1bdBvRVCpUVV9Pn2VRTOHMgw2iYIsMEnBCRt1U74rl0RuCuZ53U2f2MZc_O2I37F7kkVqsXhjjT6zwoVILa3eBqEq3xCgeH5zAEgdQE6yIz2LBANTYP9kcZZlRBc-f6qaXkMnuonNolQ7YZSYOagGw9wstY8A2RFGo7e2713Ns3J_4MDbi0xGQ8I6046DxDZE95eb8XGGluD1NcHcNnZgzJT3XsGF26lwtiR1kLHWgwuGhztmYgcLUst7MKMolGAZrEetyBaZ9RxKJO0_TgAAnpQdR9hLYqYItFyEtpj64IaWa9iAYdeF3vHUcKiKJmG4QXvAmc8RTooOyUwRO9rqDy7B17M73k7yTFTcs-G-mHNJ54PuvOwXyzpcMsejK49fGhm-CwNLCcC3LCPXyWugret2IhHflTkpSTeh9SpfGhviGZmGNJgv4VLD3KUpgQpZC-KQA1asl52kTbczCzyDPtBuimlVAcyvYXHU0MY1RXN64JsEr6T1VuH9adNV9Mtsht9BuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به منچستریونایتد با گل‌بخودی لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106964" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106963">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjbwOi3FzMyPrlMdJIXWPi3ZouNAz6z2niGE9rxoo8HuNG9BlsaYa02h2Za69asylZ5nDIcBZ7oifqsFMOmA1oV0VgUKOA3X9LLNoyFzHPJwnGK-EGT3eyEwxnOxhUS1CjoDlJ2dxhd1HJ8Htzqr8tSdJG4i2f4bVRCivs1rW5kBkUOZxtejmXw4NfiIA0I3QzsBQAiR5AYODmuIq4EXFFo6zvizm3WE3jQCeSob1vKJYhM38i-lLVRBj1ewE5tEQVm1kibuI6Le6k3KxGLCLMT9U5V42ou0UH0HsJXKcpgcSqJlHF-qR05lpCicNX5QGkprKE6rhIO15JfrcN7fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو
: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106963" target="_blank">📅 20:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106962">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7YrNf1lIzJj_kAX8mcUjqVQIeUVABOd5vn0TNamEBzXi_Q6gcvNUffOeeTQT4v5pPDs4i8zYwTBDZQDdSYkkGPnp-m5TIMedFHml5tDFxBIX5dOvGfwWWARBLwFjc91P0DAhnaPzHqMXRLEbtq07nTEw_3-IKStux7xY8ZishQw7ksYByAayeZ06aH-YXnItIP1ZpkuIIdtStAe016p4CI9bxIhO26K9odyoH1HApEve2K9d4-O6-Lt5nhvfcJgmzjn70WuBLZ60jUOtSn3HztIyoQALzUW1AD3PKHwtEn02cu9tfPdo436cSnam4kTajKoYGHpLv-RGjlHiV-c_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رسمی رئال مادرید:
اورتیز آریاس داور بازی، رفیقِ لامین یاماله…
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106962" target="_blank">📅 19:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106961">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Fyu2gTR4V7-uR7UB5SOuCqlEWcd0PcsKEO4JHMD6ZLAOiekj49ktfZFH0ZQ-6sc4txLubQ4Z976AkMYjHQZ4eJzFSpgSqXux9-_y27EEjtUaR_YrZOaJKxKSXdgwXEbWqkmOsQ18GZXmGK46MPokxafQQCns56u4alKsYrw8NwbTgfHHPz2-5I4r6ShAg-BdTOZXAenhOJgjxj1Rm-ckcwuUbbIoPO7PCDuoC3CCa0-64bTuqzdzOmU0fdmsYnGFgZ-2Lm6q0NnSpolmAhqPlCgIpU-w1tEsu-VCzk9UM04KxQIoBMKThIWJdtSKZVEweNyE0FEzhIDylLLxyp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106961" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106960">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZc8orNFYdTDk6IAmQCqc-auxim3J05Dghw5uTnx35BZMhxlre0ctgF3BHJMqcGa0XomLJiD8oJ5-O-IBvVt7gnye7NbKHqu-v0fGvhWVDlFIMpS9FrDgUAQffMmOiTAWzZXiLNBUwIpA_-saTY5ssY77WIpH4TyPRL3Xt2YqxyA_UxJmB5D0Wy5O8jWaFKmcIN79y3SDmguL5XFzWfKIXgZl-dJn3GP8WYge7AwIfuS9AnUIxDBLDV4c6vZYD0AmSX6TI7BmbAqafWYO5OBbEwbI0UEfYU4w4VuwXyAx12tA6GA5KqYsNzqjhzeQ9ph5Gtk-mYnwojfj1jr3E4Q8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106960" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106959">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY5YF4kKoUUvfZz0qV55x9bjcvxseXRETs-YKS16AwQUmCNjhxKvtaNt7aAx1LoHW_UCZoszPuWWRDgcuHDRPIg6KpS1Kq7QgDd2ACSAAp8E0Q3V9_zEXf9Y1UaVEE-E3F0xcAdS2GFiy2OpuwBLcjPQNK9kehffB6og0fWJvaQy42ARKIDXxEmoURZlW7AUA47-Q-mMDou5tYhM86OvFZ4tJ3mkYFpkhHutxEHdEFd4nKUIMhDcaN9JYFZQNQqrJgsQvKKDE56SCZ5hTLgyxObqb28XyrwxQjuGt8S_rEz7jQpd1tPbFgDINEXQfPfsLoN4TmqyXCDNXSbUf3hUHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106959" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106958">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106958" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106957">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دقیقه ۸۹</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106957" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106956">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رودیگررررررر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106956" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106955">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رئال یکی زددددد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106955" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106954">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106954" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106953">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یا حضرت عبااااااس چه توپی گرفت کورتوااااا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106953" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106952">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اتلتیکو دومییییییییی زددددد
🚨
🚨
🚨
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106952" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106951">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106951" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=UzQ-gNEjf4GWCuuYxwzX0Kddb2GzqUZt3ogAFtgt--a071GGjR0bcFZBLnLISS7QWcAfCi27a4kPlzcD35MdjCK5h21myTPskG5ycs8WsX7Xrapc63CcwrFD9kqFA6hiEZPUq53FaGiPZCfrsknooCwL4n1YfZuLDchwJzJE0DYVltCBBy4FjpFzf4h7j8fghQopWUy0QDSyiYR8PnTPs7t3QzK8xVp1iHhDVourx8bn9Hh4je6iXgGUtMaeUtE4Ys3BGDhmghTQdbBfcOJpSx8di4rGaxO3pnzc4poBnn82Ha2AWanBikSJSxVrWN54Y3tZsmKk2mGnDS3kUkLk3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=UzQ-gNEjf4GWCuuYxwzX0Kddb2GzqUZt3ogAFtgt--a071GGjR0bcFZBLnLISS7QWcAfCi27a4kPlzcD35MdjCK5h21myTPskG5ycs8WsX7Xrapc63CcwrFD9kqFA6hiEZPUq53FaGiPZCfrsknooCwL4n1YfZuLDchwJzJE0DYVltCBBy4FjpFzf4h7j8fghQopWUy0QDSyiYR8PnTPs7t3QzK8xVp1iHhDVourx8bn9Hh4je6iXgGUtMaeUtE4Ys3BGDhmghTQdbBfcOJpSx8di4rGaxO3pnzc4poBnn82Ha2AWanBikSJSxVrWN54Y3tZsmKk2mGnDS3kUkLk3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول اتلتیکومادرید توسط گریمالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106950" target="_blank">📅 19:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتلتیکومادرید زدددددددددد
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106949" target="_blank">📅 19:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلگلگگلگلگلگلگگاگلگاگاگاگگاگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106948" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106947">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دین هویسن اخراججججججج شدددددد
🚨
🚨
🚨
🚨
🟥
🟥
🟥
🟥
🟥
🟥
🟥</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106947" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پنالتی برای اتلتیکومادرید
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106946" target="_blank">📅 18:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106945">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رئال‌مادرید: وقتی داور طرفدار بارسلونا باشد، چنین اشتباهات خنده داری کاملا عمدی بوده و پرونده نگریرا رو بیش از قبل بزرگنمایی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106945" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106944">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106944" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106943">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EapX6cWJnnO3IK3Uvz9RYdN1lV9Yk7U9-Q3MVlswJl77uf2vRbZ7BoCVv3Vr1j5ui4GApHeJ8lXX6YGs92nqBNVgrDR26VNBleocFNSPeSu19ZXaPTzrw4GMIfLPrv0SdQVyP92yb8gKc1H3PQc7S8LqxQTZuAyWKxBKH4cCqejCr9XvLbNJKKhPZj3MSO6t1rOiNBagtNz1fxgMltBob5tNHoOobhcD6EmnNcYzdWCVr182xI9cq5pvE5rdk3aKq9lOxw3CSz02OEYkoQAus39jDKiad_JshDaixRviGY2wMtJnMGgE-4hW0CAqfBA2L-6jQw3XbnFbj_cOBidLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106943" target="_blank">📅 18:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UougB52o5FFZD0VrXAswSd6rBs13FTD1ASfCRg00VGEYUeIbJZ04j7DNmkamIhtBK3Qc1BmlcntmxfJdZh9jpGMK1D5dOk2F72ZkV66cGqKi3D1NKgQ6RxTmyBLwG5A3yhLiyYRdu6yPaIeqAuZZAG1mUiWye_RGXrAnNp05b9-DtOvM96_Qnz803hQZOfZXnxpg2HBeuKu5GUpiSl6R7b-m9ofLMS4FMuOXq2wluIh31L-qaQ_lQPsW6OIwTK9gpqpXkwIR5p3qGYiWM2A0SQUi4sHrICAJ4PmGlqugKglsku2BAn9eZJHLjSjlr4nkV0ILDQOoTQ98Cf4NffXeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با گلزنی به ساندرلند؛ ارلینگ هالند اکنون مقابل تمام تیم‌های پریمیرلیگ که تا به حال با آن‌ها رو به رو شده، گلزنی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106942" target="_blank">📅 18:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106941" target="_blank">📅 18:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106940">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M473L7kTv1iH3NKIuspHjIwB0wTv_80vEXF3b__dJXHf23vzMMrO8-kYRUXH7K6QwpP4FZo8_IE3S89sgX8w10pjTdhY9g7WPhHCkfxHCQV6j_YTzpnW7Dq-NOLhTtRhrnktU0iVGyy9gh4yq-TOPPFj1n1y5jsiAmwBwmpGxpvvGEADtjv06L94NC2gcHLI2UOWROibpcDlZGumxOG93ZDaizg3X4rRBKK0Na2Rw0-OK0d25-BPiqVwDmYjb4JSQnga93zveDIlQ0FEPpPNq9-VBAR5Ci37iFGkKdTJayu4oerTVLG1UGFeNfVX9IWvEf8XJikqrmEOv-6uESpm3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106940" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106939">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتلتیکومادرید دقایقی هست رئالو لوله کرده
😐</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106939" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106938">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqrE8q4MECEojldj_JkoTPhNezAHzD0XdfxDoI_Nr0LFI7N3Lg7cBfmzoDee59Affw6l574OkC2L2oo2M_rO7_TMvAoOh1lt_xOkMBLTVZi_Eg68XFI60DwhTVSrZDlN1rwLBGIDyPq1a5E3zbZuDXb1tgy__li3G1VGUrch9Vsj-uVe4GBIGzlELUa8E3ExuoLoVp36vu95iVpRaVAA5Cu0gY9PBViWUfFwDfD_ZXbG5IiPBIppxlWnzEe-uFv_Ngg4w21I4WlSfO6QMmsLauYr8CU3Fi5LYr5mzJo_Km_FldQp1PaQSAarJE6muho52B1ddsZV6UNIg76smU09iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106938" target="_blank">📅 17:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=XUne57XJwDa8oXRzkAF7wsuKuE-5ELZQt05wRDcKK-2JQGATumVYyHViZpypKMOHTmr43wviKy6cK2WMxyW4DnAXsDqjvradAn2-7f_Wn2xDlCTCjcvqwnNJZW-L3KhqwPNL6-cZEIjqjg6B6Ka6Eknk4A-GA5l2AxTnms7MDz9xK5iOLyRhPOFwKzzucx36pe6cp4lKVfRM2-aVS8jEp7ZFKnLu_uRZxUr6B1XN5JPCiq-dHVTp8trkgIhnOPUTjlm9fzhFxg7GsrvUCY9Um0hh-kU9dcwI-iDCUCRk329cOwwnyY_SqRRL3AuhD5MB6eoCznORUIqusvuOp8drWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=XUne57XJwDa8oXRzkAF7wsuKuE-5ELZQt05wRDcKK-2JQGATumVYyHViZpypKMOHTmr43wviKy6cK2WMxyW4DnAXsDqjvradAn2-7f_Wn2xDlCTCjcvqwnNJZW-L3KhqwPNL6-cZEIjqjg6B6Ka6Eknk4A-GA5l2AxTnms7MDz9xK5iOLyRhPOFwKzzucx36pe6cp4lKVfRM2-aVS8jEp7ZFKnLu_uRZxUr6B1XN5JPCiq-dHVTp8trkgIhnOPUTjlm9fzhFxg7GsrvUCY9Um0hh-kU9dcwI-iDCUCRk329cOwwnyY_SqRRL3AuhD5MB6eoCznORUIqusvuOp8drWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🏆
پیک‌زدن هری‌کین به سلامتی توپ‌طلا احتمالی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106937" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106936" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3wtttDg_BR694P1qjcn_Qc43bulSL3IxAEdKIUkT64q5d1Iel8ezayBkf2KEx8oQq_SAtuy_57d1lYcSyHQSi8sUAnze3FIJCj5At72ElJH4m9TijWzgl_OqtvzAlmEz3HhvrCAB-LGzdUZsUnlRR1rWqtfeBjaAagaUHcuoceOgidsPVNtn-OoOuPo1iZ6FLYUN0z6dgmqjyvBMPpwhAy7CmjS1ugvZnnhMW4zmHnHS9vPL-hxiSDUZkhsY6DX1m9KYt8j38UNWYl8FbinIP6d2p4bTt8aORbQvrUHe43XiGfFUs1uT6CMHo8F_py406UXZskJpIgWJ2Ede4vyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106935" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برررررریم سراغ دربی حساس مادریددددد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106934" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNVKBFiMqhhSkWsl19-76M0sB40vsJ8obIDWZY76AMPO_nOl_gH38y3w571AsThYkuw8VJmwM7amylXJrZQpx8Tw26mz70sjcMi260qthG9geUxu2xsG-EXk4_XAO1maFFQMxXOSfeX1EG8TM4oIT2JBe-2T6l1pcgk7uy70bGEW27QN1UDdJ4n8ayPTCSfSjzUinguCz5NKdNCYKVIvf2FXMc36yP5Ue79fogGZXVg1At-l8byQ-1hpps9tiBQCzb9F9H1SmgrJ6JquaTMCt_d3r2yImG84jVDHOMM6sp88zlr2xb0ta6KfD9xrbopPiq6yB87X-kVdvZ6CRXCtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMI_dq8Ab2fHBOmBri5R9c165eDGlRcJicy5dZcW3RVwe1Zz928q54Agl39oOiJ_uAcwGpJrEmVoGCkfP7WfI8ynf5TaAeh4UlkxyTGDhVk6SfTVS5MefNOO_mOO2r8CcZZCaFWvJsTcYjdhIW75jS9HVLvqIt1MvZvb-GLTQRUTKqu0RPgnBRGSzaQVsee2MEdrypgUOZSkz_UQ3vKrZYvKeEwAuVmtjdNvSZO12wMPgY-CurDoY9uDbgh7d0Z8mS-0j06BTrWgwexFEOkYRiV3pRAXx4SslBEWzwHaNGrYBz1UemZ7ImmB5ihXpS6LBGPuCi4YuA4nhSaGKJpJsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب دو تیم رئال مادرید و اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106932" target="_blank">📅 16:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106931">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=Yhof31U_8GSf0Ba1-01oj4fYvO_oiH3EKbPe8z0aFCZasw12LDrObZpDBDzBe8WGaZ1KUtUVkK6rPub1v5AJoOjkLFM2Sf1auI0ISrve2ZntlD-CwwA8VaT-tzqJx1wrjvV54R6UZozSxTecj4vPmU8J0PVidKnjYKhe7Lgcz7T3SoQJl2RlYycWx8WQVl7QsueXLvtqaCh-Vr-s6YKiCcX0gAHCGFWXTv9_hRxP_ZdpkT0XEgWj8rJ-LlN9iW9di4Q8kqRS5Xoy0FCRyPioYakWa204MBDkzk-a6QnnOblEo05QK1zOWtH5DKsatEo7rZ-T6BCco4iOsOs50fZ2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=Yhof31U_8GSf0Ba1-01oj4fYvO_oiH3EKbPe8z0aFCZasw12LDrObZpDBDzBe8WGaZ1KUtUVkK6rPub1v5AJoOjkLFM2Sf1auI0ISrve2ZntlD-CwwA8VaT-tzqJx1wrjvV54R6UZozSxTecj4vPmU8J0PVidKnjYKhe7Lgcz7T3SoQJl2RlYycWx8WQVl7QsueXLvtqaCh-Vr-s6YKiCcX0gAHCGFWXTv9_hRxP_ZdpkT0XEgWj8rJ-LlN9iW9di4Q8kqRS5Xoy0FCRyPioYakWa204MBDkzk-a6QnnOblEo05QK1zOWtH5DKsatEo7rZ-T6BCco4iOsOs50fZ2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
دوباره از ایتالیا صدای گرگ میاد.
🔥
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106931" target="_blank">📅 16:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106930">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=PK0Mv6iCf7JzTEj12yrW6Pw3JH8ccQCe68IOxQcbwO1T8fjio9NdRMDtDLdNbXnWZnOZklCUWN7TUvyNpVMcoco4ebevv0SeRYrznzQ8bKl6YtNbmgcAwNupZHqaR5MSR5m3E5ssSE2wt16kYGKMC3CNF7VlbZQbDuhh-xZ3K-EuZbayfVP1C_EOhU8flxF4lfQYwy-48-VShZnHSdB1h21AGI79eDPOLES8fGl54W3lgZj6bpgtHeqYiqHYRzevRt-3XgFYNES42YPVJ3Ck71OiJaJyi5KlcTnGOqKbcR5LFFyrREhSwM_JeVIId_qUo3Z9NgzDPmMrEsLoKYy4lIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=PK0Mv6iCf7JzTEj12yrW6Pw3JH8ccQCe68IOxQcbwO1T8fjio9NdRMDtDLdNbXnWZnOZklCUWN7TUvyNpVMcoco4ebevv0SeRYrznzQ8bKl6YtNbmgcAwNupZHqaR5MSR5m3E5ssSE2wt16kYGKMC3CNF7VlbZQbDuhh-xZ3K-EuZbayfVP1C_EOhU8flxF4lfQYwy-48-VShZnHSdB1h21AGI79eDPOLES8fGl54W3lgZj6bpgtHeqYiqHYRzevRt-3XgFYNES42YPVJ3Ck71OiJaJyi5KlcTnGOqKbcR5LFFyrREhSwM_JeVIId_qUo3Z9NgzDPmMrEsLoKYy4lIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
بغض ایراندوست از طلسمی که شکست
پدر و خواهران مریم ایراندوست در ورزشگاه، برای اولین‌بار؛ خانواده‌ای که بالاخره برای یک بازی زنان دور هم جمع شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106930" target="_blank">📅 15:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=ZnySS6EnIPgIz8qqBFI3pykzumesVcpFErfU8S8bY9GbnwcfAcMUQJdJdQ2mo1OOmYYuYKQ-EN_ReKgZFLaxWQl_XchHE8kP_5UQceWa16FJEmMmGrMbRufGUhOLIqzTioK_hPNlbjVms8Mumiqma-mSLFwddll75EZU71dT8NsxZEUaBMCaDjp0k_AW031Ze7bNQ_H0Z4lR75n4hLQ5ZgN2BBregT8bueqdklb2ZMEi5w7fMqD4ED9-VMjAWd-L6EpTKDdSuGwZAkd8cBEH7t6dn--BZzMGFAQyd19Dd9CSSZ1jQHYP29gjIFHzk6n64SVZQZTIr6ojU1eHC1ETZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=ZnySS6EnIPgIz8qqBFI3pykzumesVcpFErfU8S8bY9GbnwcfAcMUQJdJdQ2mo1OOmYYuYKQ-EN_ReKgZFLaxWQl_XchHE8kP_5UQceWa16FJEmMmGrMbRufGUhOLIqzTioK_hPNlbjVms8Mumiqma-mSLFwddll75EZU71dT8NsxZEUaBMCaDjp0k_AW031Ze7bNQ_H0Z4lR75n4hLQ5ZgN2BBregT8bueqdklb2ZMEi5w7fMqD4ED9-VMjAWd-L6EpTKDdSuGwZAkd8cBEH7t6dn--BZzMGFAQyd19Dd9CSSZ1jQHYP29gjIFHzk6n64SVZQZTIr6ojU1eHC1ETZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
🇮🇷
فرشید اسماعیلی: یک‌زمانی در زمان رویانیان در آستانه حضور در پرسپولیس بودم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106929" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krrwaLelIxf_JFSD7odC-fN6O6kVinMXGEku9TN54CIyUtpPU6YGkOem2xKn0N6RgnBmTWfExh7V6-0GUGlj8rY5CoGYnc2u_rwTDJy2-s3sCW4p03xRyx0_TIDVbEhoW7gZsCKBH4NDO_xbHL8wBw6v9I0sKChLI0YJL8sWzhPunj12X9NmqFY2Ucv5vRQVBE9pybjeUdpWKsFzwmEh3_C3C84cVv8o5gMP5TW_SLYIDwwTZVXwiuyONu1E173fxOrzpKCCujj8ZCpCJgMMDP4ydtbwA9N7bAQizkVasfxetYQPsxg39o7MEh4i8xvN6HmQ-oUAMKF6HuU0tQ0PYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشون زید دیومانده هستن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106928" target="_blank">📅 13:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=Sme9-8lZug1k2r3Is02HHSnorYfH-8SA85j0AW6bmk3z9ma49qRZtE8eA1RCgx3ChD1Zv0LvdanZOoG8mxCUI4MzoCyS0o-JMHU_YMSMrzgyyYPM89OWM-Yo_uOwRIpKUFBta3HFb7ju1fdBORXtXctXOq6etd6jAd1t_63fijbR6uljywlPvqEBW3z6TpcnIC3wz_69ORtl40YVsI7Ndd_nEj_iqqgVI8xtUfQhEBZA3cMmVRO2TgiZY_Gth-rD_Pit-0Xoei3YztLTXWAPBI2mAdP418nwISm2QVlTcMQ-un81bKUVN0dKbdEptTSE5jhGT-YuvlaojUsedXHp-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=Sme9-8lZug1k2r3Is02HHSnorYfH-8SA85j0AW6bmk3z9ma49qRZtE8eA1RCgx3ChD1Zv0LvdanZOoG8mxCUI4MzoCyS0o-JMHU_YMSMrzgyyYPM89OWM-Yo_uOwRIpKUFBta3HFb7ju1fdBORXtXctXOq6etd6jAd1t_63fijbR6uljywlPvqEBW3z6TpcnIC3wz_69ORtl40YVsI7Ndd_nEj_iqqgVI8xtUfQhEBZA3cMmVRO2TgiZY_Gth-rD_Pit-0Xoei3YztLTXWAPBI2mAdP418nwISm2QVlTcMQ-un81bKUVN0dKbdEptTSE5jhGT-YuvlaojUsedXHp-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رختکن چلسی بعد باخت جلو برنتفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106927" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=qJatPjVuKgMg2pHtp0nJ_IJAoeUSejcbRGlJT-DXBLOMy-hv45lL1N9imIv4XPL_Nsu6HQv9bp2drI46VSWij-qRqveUX4ZAa0F8IEi8IN4sGZIQWdDbVgo_-lyurLcEpsBT24ASfROLf1haT5LCNMi81UY08JPtuNjG3Xi-MZj1j4dQRCZ9YjXiHDwctH0LSUYXJnULa3Mf8-ZvFZYLsBJBkZL68Q2yKXxNVT_Ly_IYCdC-zEGHF19tozKooqVdQ1-cYGPvOH0-eSQOodX7lp0Rr3ZQuDxgu11OngfX5fsHaHGiyVpKY_UPEvwKwzzDeZVquhQwifI_At75QWDN849z2QmguynT0J_zSbCytBu-jsSoCWB62p93DdiIt4o4MpVSWA977QWB8YeIKPiLkhsxrlajb4CVu7ou1LGpn06SGRXu_QA7SsuTmoTgLWGX_Lp3OMHANSVTmtzu9yZtf1GDfQBEOdsLXHaK9L3KyJAsaXpH2UIoA-gwTDEFZwWHh8kR0gG5e7fimNl275ZPmhr5UCsoT0pC7WlgVJZ2OIw9buU-c4i3vpgXLAcUe7_1hrxj02Vki9cdYmhq_jm4p-QR1ECAby1BhruoiedQKk2BNzJQ5QRGYPfaCUGT84LXKdNAPMZ_Igy4vP7Den5uxd5s1FrZnRN8UYKVtD20ZK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=qJatPjVuKgMg2pHtp0nJ_IJAoeUSejcbRGlJT-DXBLOMy-hv45lL1N9imIv4XPL_Nsu6HQv9bp2drI46VSWij-qRqveUX4ZAa0F8IEi8IN4sGZIQWdDbVgo_-lyurLcEpsBT24ASfROLf1haT5LCNMi81UY08JPtuNjG3Xi-MZj1j4dQRCZ9YjXiHDwctH0LSUYXJnULa3Mf8-ZvFZYLsBJBkZL68Q2yKXxNVT_Ly_IYCdC-zEGHF19tozKooqVdQ1-cYGPvOH0-eSQOodX7lp0Rr3ZQuDxgu11OngfX5fsHaHGiyVpKY_UPEvwKwzzDeZVquhQwifI_At75QWDN849z2QmguynT0J_zSbCytBu-jsSoCWB62p93DdiIt4o4MpVSWA977QWB8YeIKPiLkhsxrlajb4CVu7ou1LGpn06SGRXu_QA7SsuTmoTgLWGX_Lp3OMHANSVTmtzu9yZtf1GDfQBEOdsLXHaK9L3KyJAsaXpH2UIoA-gwTDEFZwWHh8kR0gG5e7fimNl275ZPmhr5UCsoT0pC7WlgVJZ2OIw9buU-c4i3vpgXLAcUe7_1hrxj02Vki9cdYmhq_jm4p-QR1ECAby1BhruoiedQKk2BNzJQ5QRGYPfaCUGT84LXKdNAPMZ_Igy4vP7Den5uxd5s1FrZnRN8UYKVtD20ZK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اقدام عجیب و جنجالی سیگار کشیدن مجید واشقانی با اردشیر رستمی در برنامه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106926" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMXfP40NqtzY19aC8sdwu9MJSnurnf2LM64SVRV4eP4zGZMGvHVJHqdIX0bcR6nqhtR46b8HwYS9IK0thC1mHzzf3MRoLgvIIRcND2DxHp2aoGqpoj9zhVGW5Xut2bWx-qVTe6K7HsTPsOUqoMlVm0-Zq7xFNuFX7Fk7wOhpETsCU98WeRuT8nlvnOTktEQR_VOGWLo7Xtxvojuec64lOOh6_bOIoo_b5Z8cw6Xb70vE5nmQIuT9fbN4Qac6u4_ne-4sZD_5IGQ0DELx_RWw_CUaJUZex9lpPImNvAWZ81PjTRQmkG-EkGVDHyvPHZReVNTZ51x0RykOXczcDZws0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106925" target="_blank">📅 10:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106924">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز متفاوت و جذاب از تاتنهام که برخلاف نتایجش، فوتبال نسبتا خوبی ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106924" target="_blank">📅 09:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106923">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=iMjSDtWEnjCmNkCC3-bl9JSGe_jhXMWCTV7JAQzk66bn0qyuLlj8cVAwJRp2xt08BxxjaTOiUcjtAnGaYFPdA1koi0WUS3FKd4Drt43X-UYbFmEmdSaGX4KIP6kR4ZCv7qmXGpPLziVRuND09ATsMdlwHZ2Si8Hz89sGByv2xit7nmPipW_YPJmkIMpgHMZuUjYsOXPpImPo2kiXp6-vcf7cO-DZHiHuyODsg-gAsFxVrxH5qJ1I9gLLQj3zZQrmnMnlmzUZSXTypvyqFeCsKUtdpn6jYpj5hBhO2Zq-K7VXMElOHKq-Zm_nrj-87-A4cTU93t6QCLUG5UNpPJW2VIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=iMjSDtWEnjCmNkCC3-bl9JSGe_jhXMWCTV7JAQzk66bn0qyuLlj8cVAwJRp2xt08BxxjaTOiUcjtAnGaYFPdA1koi0WUS3FKd4Drt43X-UYbFmEmdSaGX4KIP6kR4ZCv7qmXGpPLziVRuND09ATsMdlwHZ2Si8Hz89sGByv2xit7nmPipW_YPJmkIMpgHMZuUjYsOXPpImPo2kiXp6-vcf7cO-DZHiHuyODsg-gAsFxVrxH5qJ1I9gLLQj3zZQrmnMnlmzUZSXTypvyqFeCsKUtdpn6jYpj5hBhO2Zq-K7VXMElOHKq-Zm_nrj-87-A4cTU93t6QCLUG5UNpPJW2VIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😢
جوآنا ویتژیک ورزشکار ایتالیایی در مسابقات چین یهو وسط کار اسهال میشه و بی‌اختیار ازش خارج میشه اما با این وجود مسابقه رو ادامه میده و قهرمان میشه. در نهایت از مردم عذرخواهی کرده و گفته امتیازاتی که گرفته رو ازش صرف نظر میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106923" target="_blank">📅 09:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571388041d.mp4?token=qAWVwa0uIJc5ZLqYcflXcmUPXbXqUKdlWya-2MblOGuEfemXZI1dLXcDi8k_tazNlgUPsKt_GIPSexY6X9u-ACXM8ebuvURoufV3naNl1LCLTL_B8XtZhiQaR_A2g39Ug0niSlRewLnVYfz7XgIuMnmqYRL2dMsKdAaObV77eICexKpUbNXPPH923v4o1UfNsz01XnHlLy7MQRwQsZjzJu-3AFVj9xjWLT_lFl6MVmfH40DpSrWcX1Bm1mOosaEg49pWYVPAcfjuk-rI-VvdsZPyXbsKfFVHmAPAYQ9gvoQ7Uh6SjFn59Wy20rcsJ93UNJRqFRr2y9lZZBdhixe6lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571388041d.mp4?token=qAWVwa0uIJc5ZLqYcflXcmUPXbXqUKdlWya-2MblOGuEfemXZI1dLXcDi8k_tazNlgUPsKt_GIPSexY6X9u-ACXM8ebuvURoufV3naNl1LCLTL_B8XtZhiQaR_A2g39Ug0niSlRewLnVYfz7XgIuMnmqYRL2dMsKdAaObV77eICexKpUbNXPPH923v4o1UfNsz01XnHlLy7MQRwQsZjzJu-3AFVj9xjWLT_lFl6MVmfH40DpSrWcX1Bm1mOosaEg49pWYVPAcfjuk-rI-VvdsZPyXbsKfFVHmAPAYQ9gvoQ7Uh6SjFn59Wy20rcsJ93UNJRqFRr2y9lZZBdhixe6lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
کار جدید حمید سحری از برد امشب بارسا: واقعا کی میخواد جلوی این بارسا رو بگیره؟
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106920" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
