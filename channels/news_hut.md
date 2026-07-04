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
<img src="https://cdn4.telesco.pe/file/oQEi69z3ULo_fds4nRrRbpvuByIXQ9rDRbpu3m2Oe4BKb5g_7rPCjDN6aaql_y2uuOcF_8dJvI-HxezUzicOda-sPsU-C8Il3XbwWDyQ5GszK99uWSSYg_TKr_N5exytDJ85NwISRTNqAqcRIz2CWRcR_GFNSDAfmezR3JP3CHVWUHRtXWyUl5z3uKxFSQ4-LuDcHk0ZG-MfmV5ghglWRyxbFCXgrBrIIiWUCKMZcUkniYYn8-_JyM7qncouf-qj9WVfdi0vhA3blkGu16wgpfXleqi9gNUIm4gycOGL3HCX2N6FtplN0aEtu6HTPxRRDwLOpKWDJy_tip8tycqoaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 207K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 00:56:25</div>
<hr>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSCRo-pWVyW-vF2zHNSD-pZ5LLY0SfPRkPGIdDoHzd_XLHAWCzcrD56iTxEXrmS6qLucDs5mAv6-1mljJFI-0lc_9dO3ieZKwcYdLjjFqcgyLgbTAR_VymOfBH17tvTLwuGCfAvapbqLwYOhtzwVoBRNg7SfjFQqTMPlX0UFZvF3FHMymBrrQgpQA1JSRO4vSj2clGL2tcol0gabywKlphZV8bLZkxOrvm1f8mUMeEPmTPU93lIrH70pf8V06rFCKT8okPSSDipoH3aenCANn1PmpISV3lVLAQvJKuV7lh5D9-UY69RCaC70MC90qt2PhaQChJrjyyzoaUZQlcn_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=bZvjCMaFjaIVPgv2yw-AfE25sDwRLuB3Qi89heHHV-mQqw4VmFg5PUAoMfbHgsPmON4qldfniZ20bIwCbD-MpNX2nY3KGvx67-UulUB2ZrpF-W62A0OVFr9fCbuL2aTpFHoHl-M6I-okjzb9HEs-hrQ70H2jgLX6nPkPbVqWTEy4zSGXBZ0OcBFp-p6GMuUeiaWawz1fBkV3Kkv0-dUJjYay_itlBalYWTQzeNx7bXchbYM_tvWLh4x6-VQUbXxH5FdZN-Be0Qf9eUFbtk_ASkKrvK943nFesd0MsI8_AQ6XObkSbl55ay0I9F4AZgaKUpL2wtp-ktLpbsrgWhqixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=bZvjCMaFjaIVPgv2yw-AfE25sDwRLuB3Qi89heHHV-mQqw4VmFg5PUAoMfbHgsPmON4qldfniZ20bIwCbD-MpNX2nY3KGvx67-UulUB2ZrpF-W62A0OVFr9fCbuL2aTpFHoHl-M6I-okjzb9HEs-hrQ70H2jgLX6nPkPbVqWTEy4zSGXBZ0OcBFp-p6GMuUeiaWawz1fBkV3Kkv0-dUJjYay_itlBalYWTQzeNx7bXchbYM_tvWLh4x6-VQUbXxH5FdZN-Be0Qf9eUFbtk_ASkKrvK943nFesd0MsI8_AQ6XObkSbl55ay0I9F4AZgaKUpL2wtp-ktLpbsrgWhqixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRdZ3C2LMcZykC5HWaHNP7aDcCXkyaWK0lcPz24UDW_xuhTRbwwIs6J9XzfQGYvfA328Vnpg1Iv6ZlICWYH9jiMaMhc6MeBP_vzjulLcl9RLTQLkToHEW8BvOM5fWlRZb-akWNn9U7t9FQr7nupK09XchGHrKtUFprJPKB8dj4cuGaO5RvEd07I6hFWJ2FP2Ost35lbUBTzdz1nVzOv6KQ1Ru-BQTk_UKIHQGnjr855yg2Jm1Zj1lk-tP1_qKWnpcCvwfqW0kXCo3FvHCVcuyBNwk8wjuXKCy0lTS43W0Du1u5MEd5a2AZznZkWoIYqj43_boJZmRTQ3f1ktErBNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=OVciMYBgRxDV4ZRMbgPJjUaLS-NewrrXbHjoKl34U_qk7dZjLOSRwQnVpHy_3Pqwk2E8V3tQdvteGtTXIF3qXDPlEKh9sEhjWPhlfGtP1hoyZopiYimW4SQX6nOr9md_mMW8nmPibYny0DZ6qq1hE0jySg7RYW8VSVYpDNUAhv29f_8CPfPfFHiqPQ-mIIMjc3lKfzbMiafsw5Gxq0ugCa5sYK0AGFWXGgxP85NKEQbbw3sX4e6BTzF6eTa1LkzL7C6A1yUFArABgNg6ecqet8pw0hMACGX75NLScjR8Kv9AmZrZepeuleUxuyHbVT7qxTe0CPWs9Wuoa0PzjumgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=OVciMYBgRxDV4ZRMbgPJjUaLS-NewrrXbHjoKl34U_qk7dZjLOSRwQnVpHy_3Pqwk2E8V3tQdvteGtTXIF3qXDPlEKh9sEhjWPhlfGtP1hoyZopiYimW4SQX6nOr9md_mMW8nmPibYny0DZ6qq1hE0jySg7RYW8VSVYpDNUAhv29f_8CPfPfFHiqPQ-mIIMjc3lKfzbMiafsw5Gxq0ugCa5sYK0AGFWXGgxP85NKEQbbw3sX4e6BTzF6eTa1LkzL7C6A1yUFArABgNg6ecqet8pw0hMACGX75NLScjR8Kv9AmZrZepeuleUxuyHbVT7qxTe0CPWs9Wuoa0PzjumgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUgp3gUXf-7xI5PTHhARzhLiTKZX5FNvRh4SKM8mLsW_6g4cTgFhdu15KX9cDaj7j0Rx8_aTgbZ6Lbych-TMBOmCwusy8jtx4MZnm8JOEho1ysUh6ntewxR7XRi1n-ZZW8QPGxpCIHI7qMUUV1UGJFpEWM_WQYm462GLNcFZid4ww9xNBwEmjF3gdnOQaQ6222w32sQvl2AUpaYac6lbdOw-vd-SzxL8sgTnCBfcecMVZvwa8QNHEmUGnPA0qX11g4kM2vNnHLVyYZIIptys4vLSZ4oKotYogsiK8pBv6UWe8WXwCkiMwPXzrPfjM_RLhjF4rKTfhTNcoRh2RQ4Syw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=NH_m0iuoBroQiYX9G1HJ1tC24zwK7U11M4wb0J6-6hLSD1ODEH2OAdC2_dCvbiT9wZn0byB7hY8WRCpjzvZ3cIdQeazV-Se7wGE0Z-F3hlz3i5TU6h64UYIc-SAh1bERfrPBWIaPTX08ueibW6LRaax8-cM1UUb3idrNQ2akuwTeJ2cB_QxAKVWoI-OF70x82lDcUjRw2UeXo9Upcv2RBg6VyQirQAtSnq7XRJ1a6zo3FU7Pm_5tzZlg-DXcGd1t4EzXNtMWSB6AGSO41Fc7Krq5ukOLenUtIuYL67dl7sRPm8mfZrTdFqIY1pImDvJfzpmBJr6PPdIXVWNFJftEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=NH_m0iuoBroQiYX9G1HJ1tC24zwK7U11M4wb0J6-6hLSD1ODEH2OAdC2_dCvbiT9wZn0byB7hY8WRCpjzvZ3cIdQeazV-Se7wGE0Z-F3hlz3i5TU6h64UYIc-SAh1bERfrPBWIaPTX08ueibW6LRaax8-cM1UUb3idrNQ2akuwTeJ2cB_QxAKVWoI-OF70x82lDcUjRw2UeXo9Upcv2RBg6VyQirQAtSnq7XRJ1a6zo3FU7Pm_5tzZlg-DXcGd1t4EzXNtMWSB6AGSO41Fc7Krq5ukOLenUtIuYL67dl7sRPm8mfZrTdFqIY1pImDvJfzpmBJr6PPdIXVWNFJftEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=WQFf7RYG1UZEj-LlfxKA7qahWXULju7ed34A4pF8Nh7Bzj7ouOdtLS0BpfK7bQJ7t5w_Q38YDPzy6UFKaGbuR--peyE-BNvMLVRm-FUH64byqox-8ZM3M1Mb8A3xz9VWaNozJNdwE7C-KOUgefYHK6zpw0oBNSXNEkoPMJbulIBAaOtre_uejOAwNjkPM-_eseRh4UchJQxc79cieFAjV8d57w_lcQ29NJsGnD66m9uB-spumn3a8-iY1DRJ-9IY023SGczR2q9ytFym7umobl-ACrcaGlM6uMd613Qm1IK5ZrsHtQ3XWTt3Gfa2pQezJtzRtqvU9QAa7UCFiKz1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=WQFf7RYG1UZEj-LlfxKA7qahWXULju7ed34A4pF8Nh7Bzj7ouOdtLS0BpfK7bQJ7t5w_Q38YDPzy6UFKaGbuR--peyE-BNvMLVRm-FUH64byqox-8ZM3M1Mb8A3xz9VWaNozJNdwE7C-KOUgefYHK6zpw0oBNSXNEkoPMJbulIBAaOtre_uejOAwNjkPM-_eseRh4UchJQxc79cieFAjV8d57w_lcQ29NJsGnD66m9uB-spumn3a8-iY1DRJ-9IY023SGczR2q9ytFym7umobl-ACrcaGlM6uMd613Qm1IK5ZrsHtQ3XWTt3Gfa2pQezJtzRtqvU9QAa7UCFiKz1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDWy4pzi4Ip5XV7vgElrgnwJbFAvfcRovbKXFsMQfktjsbJuyxWNIM0YGwif7vrTGD8XeZ0Lgs1XNBVnzhWoPCqYNe4bhEkCMaSXBCG2egIIuV9Qdu-zzyQtI34Dj0uB7ysJNMUh2WG9F3GqGuKBpUeN4zkhnzeEah0001WFsCCEmhzRB3o4Bl2f4IJP53cIUfdbDWplPPLBh7lFI5Hx78kG_ZmL74E4sYJLgdPkNUlSdj9b9ipL6bP-tqdxQsXmFkIbNThqJMk9qX0B1u0y6OQ6_E7vjFvPgp4ZgeaL5xCinMANTVihO4gWYID1uGY40Pvox5mpHlKyaeHiWZa2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm6tcfojvOdGL_83bYjDUh7y0BWt3V52alrsqGSuAkPjNP9PRg55kdIqlJerYybGLl5NlTwljMKzF4EOQqdVPImA_MkBeLJf_XuegOHnA_VUrfn5wHFCqkGpv9_RwY7QflTfGJNQemMhqwMVdcFcilBOfa_m-P3fQ2pQtD9ipD-YU0y5UHpjthTMXGjPNRel19UHSU10RLHiJC9hAXAy1azkF4j3Lp5dUFsi8t46n9iSzKcpqrUQBAI5ctWP1JZTxipjpLKyIn1qdR2e4Lwf4dAD_bDfZHoHdoUwZJ7rg5FZ3FfVdxlSzjUbiC9KKHhneqdI-1eCR0YiHlwKLDsAkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-x9-aOaeoV_adeiI6vJbRO5RJJ23JGEbe2axdaJK8uqYooCOtcZfu_YI3nTjT_HCpf8cOn7xYGzfZjLrAiERUYERtJZnhFZgabzbnZm0NWPtIfFiqI9BAWmOaonuOfrc4_p6IpnCrEEGsnlQ2oetS7oRLdEFOPWOltgIlLS8y5u8ZmfTUtqaPo4O5hOZlpf43VeqspUjE8OwLIoUDlM5qy50px87s86x5Gdpbj161rxrXKk-Re0Q76Mq7OMu1h2xno3M4QWo7p-3EQKQhvz_YVC70MlI14_8fI5Jb9-_Iz6Vnr0-b7VvBcZtaBvrx-b7yz5zcgH5oZvO2e3j1B-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=GxHoaPVxkwVCFTpbW6WbZY_jyyEebY4SZX7F4ea_CjjFKuk0FRy0Of6noOy8ms9w0KTXOSzzHFV4k9vzcY5I1AFrD3nF_A5mQN9Brnxna5665Tt3ZX4AYuo-b5unTBxyeCLNvFiduFgGSVYDMkM9z5ahwF3s5KEa0AXQa3fzQeZ8p3w9Mx81ikerernX4BS83i4RsEtKyj4TPEcuyTgo12AOIa05uwhrb2nDblebB-ucFTW9-trUhyUhpEMwmGwDfDCsZA5NiHQl1fQh5jLr-cwCJQKHEHxHTY9B3JAhlWoR_wQ_dGXHv9Fu7kzTtG3qwoOKj100Df1PXhmkO50CiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=GxHoaPVxkwVCFTpbW6WbZY_jyyEebY4SZX7F4ea_CjjFKuk0FRy0Of6noOy8ms9w0KTXOSzzHFV4k9vzcY5I1AFrD3nF_A5mQN9Brnxna5665Tt3ZX4AYuo-b5unTBxyeCLNvFiduFgGSVYDMkM9z5ahwF3s5KEa0AXQa3fzQeZ8p3w9Mx81ikerernX4BS83i4RsEtKyj4TPEcuyTgo12AOIa05uwhrb2nDblebB-ucFTW9-trUhyUhpEMwmGwDfDCsZA5NiHQl1fQh5jLr-cwCJQKHEHxHTY9B3JAhlWoR_wQ_dGXHv9Fu7kzTtG3qwoOKj100Df1PXhmkO50CiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=vBNJseh73LA_AoupbqKPBCW44o65Xge_mxcIuLOH_ZtWpnsx3zE7MusDdNnKmAISHRyqtYeKgeaWnuvy5DbFaBTw0KSd1tanYZihjlK-DfkT0TfMaLdYKBR411fzV0Qlf7KKM5yNi8Frf-GeeC_p2LNYBFl7vEsLojQcDaZNO7lCn5NGLb6SbEhJBK2bsZLEH6CEn-gROCOyTUEwKJhQycp3jVrPoR0PsjLTFuqXDzAEpoD1txA8HTWHbcOnG_z08r90gVVxW-GLB1RTr-PRxbutaa1Mg2tiJMHPIXIjt_nRzR5GoMxd1TJb6VfGUm89Mda_US8dJHt70rUNUxmgwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=vBNJseh73LA_AoupbqKPBCW44o65Xge_mxcIuLOH_ZtWpnsx3zE7MusDdNnKmAISHRyqtYeKgeaWnuvy5DbFaBTw0KSd1tanYZihjlK-DfkT0TfMaLdYKBR411fzV0Qlf7KKM5yNi8Frf-GeeC_p2LNYBFl7vEsLojQcDaZNO7lCn5NGLb6SbEhJBK2bsZLEH6CEn-gROCOyTUEwKJhQycp3jVrPoR0PsjLTFuqXDzAEpoD1txA8HTWHbcOnG_z08r90gVVxW-GLB1RTr-PRxbutaa1Mg2tiJMHPIXIjt_nRzR5GoMxd1TJb6VfGUm89Mda_US8dJHt70rUNUxmgwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGyidfyl8IRbkqaAq1M9__Vaze3zlalljbwjKSwbppvPFGqddS6JjaZ1TY_wT7PNKBgb-Q4e7w2K66b1oXFfSLgQbrr6QfS43jg2zI4VQ9HCAxg8DgfHJF2o_Up9o145RpH1ma2lTF1OJs4GvBz7X_yLQf6PgoCiAHk1LEoHeK6zKfyJf67VLRZqDsYgWECdydR24lV3LZP2gUpU7ICU5h0fdl4xxGNUKAcZHLfSsxVdMRG5PILfWKDS0lSINB1sJp5mxiR8LuCClVDpp2IyEHwv15ssQO5srQ9BPvUPfloUicDo5_jWQDd6h2xmJVts5HMw1JbAaiCcUb7gE4GKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBe-n5-XJ7eEpm0cKUvwMvRDINe0BD0DiaVO7qXAVtU5JQPnjMF55kSoTeCVG9B40ZK4LngQK48YBQWpnLEsAUKkGYuyHye48OSgGANvIw9lgpROv11qeyhRGsPgTJLyOxcHl2sTkiPvFYEN3-cUoOrnoCq5TGnirMcRL5R0Aj-gy_w6HZpP3YHQGCJrNduyUIJja5tERIkAQMOZEXEm19z92boLeb01KtYkkMn7FU9lwfLD0vylaWHc0Ej6Y9OvQk9d8-4XXlu5rSZd2VYiMzPcdau-3CkPRVpNSz3rKESct80om2jiL3JoHznzBH6CXrRlkynmMyHkL5rFGoCUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtatJ_urYgV3jA8hrmHntL4B3BGxS4j3kxrrRZP2pcikItiOkE7JHvsLJUhoSq7miSz7FB-_4lmxJPz7GwTajk8sICAm0LX8NW0yqXD2vN0H0O22LwHolNw8xT8wb8lDyw1DVOmhgp5cXD-mTXYWGKC1F5gmDR9y7AQAK6KoUv_LV8sy5-2YJmvXlpouQJmWQXV9xxhIpFpVutdSo9C8W7hJ6ZBJtQ35lcp6tHDwttMqsPo6IN8F9MjeeXBumo6JEopmStVMPHGZmhXeKqyl7YSr57x7w-oeEPIEJ2AKKbVpfREM7LH17c38A0KtBu0JE8_NTGqWPHe9CRMJXU8iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=FmBhrhVutt1Qzz-dVQKGQLZ6wz-3lLvUIenIpYPvNCmsuvhn5glaMzKmyC3o7qxmmLn6pGBOWWo1dGcbCs3-H1YhCP0djhEr1q3RDoPiV-LYZtD4W98CpJDAzuagXIDjqTpMQkEzFfvPLTLL7s7o9XOMhLoR2bJSlR9T8uAmy4jvxizcG4XJy0X4u5Kwv9Prb8UG69Vn3L8ArHZY3c_zmNdU2-vsrhhwo-clixiB7cKxOdoKYqlBBYDt85g6NZZX5PFL882sqGiVXl1eP353-MhlUJMzKH5OT4WYjhrK2xs9bhC1c-BmlFEInPjr0a72sA0ORyzZcqet0fEUP2hjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=FmBhrhVutt1Qzz-dVQKGQLZ6wz-3lLvUIenIpYPvNCmsuvhn5glaMzKmyC3o7qxmmLn6pGBOWWo1dGcbCs3-H1YhCP0djhEr1q3RDoPiV-LYZtD4W98CpJDAzuagXIDjqTpMQkEzFfvPLTLL7s7o9XOMhLoR2bJSlR9T8uAmy4jvxizcG4XJy0X4u5Kwv9Prb8UG69Vn3L8ArHZY3c_zmNdU2-vsrhhwo-clixiB7cKxOdoKYqlBBYDt85g6NZZX5PFL882sqGiVXl1eP353-MhlUJMzKH5OT4WYjhrK2xs9bhC1c-BmlFEInPjr0a72sA0ORyzZcqet0fEUP2hjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MgiucSsvFFl0NOL7cy7_Qe4XJETURcKemrVYsPiqs8GvHGkGe7lriQrXgue2iU2Cvkm0N_IMpIy2Og2IR8q99aLGT7hrXcVy4BNw9xlVhhDXBZJYCt8RcSSzLbH1iJezs71Y5bYOQxhX_FKdIIvKOPwbq-xljUPP2OGGPOp5iLSRMpkGwbgiymZy9A_0TUHCmMhPuw8o66aMWAL7_ZdQRnU4ZZEkiUpmD3WLspkt0SEYCBUUmYSB-EhMO7tSkGRReQRuUmmdEr0zUFJgZtLdgCtAIk8JPglxlgGCNgl-WaBE2lfHdPufNLvJN1dyU9sE_ZUK-xccR768s61U3PoHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MgiucSsvFFl0NOL7cy7_Qe4XJETURcKemrVYsPiqs8GvHGkGe7lriQrXgue2iU2Cvkm0N_IMpIy2Og2IR8q99aLGT7hrXcVy4BNw9xlVhhDXBZJYCt8RcSSzLbH1iJezs71Y5bYOQxhX_FKdIIvKOPwbq-xljUPP2OGGPOp5iLSRMpkGwbgiymZy9A_0TUHCmMhPuw8o66aMWAL7_ZdQRnU4ZZEkiUpmD3WLspkt0SEYCBUUmYSB-EhMO7tSkGRReQRuUmmdEr0zUFJgZtLdgCtAIk8JPglxlgGCNgl-WaBE2lfHdPufNLvJN1dyU9sE_ZUK-xccR768s61U3PoHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch4uks0s2zIVQQxXW699xzRqEv254JCxDX8v1oXz6EeHET-fdEUTVkQEF9MDnvBZVIZ2S5FkSv54CSz5wSXel_7u8X2FA3JAIasdfUfWUKXCiRqL5l1f5ZIVYklj1zmAz5PSgYNIN5O46175NnQOKZ_XchNnG5fZEuxD6ximpI3N6Qlm0fzuM_buZqSqwU82LPgPZtc0Zwur3T2OpuYpbqrTTDd9AMe5qBXsMLyGfw2b8LQBgwZuIoKAJvdIUZ5EhVfz860B5BMqbHrAmyCgrhmCxtnbbQtwcmRodEIv-8Wa8G91kDV29lvXTh-vHw7fKqIRlCbpDrcAagCUX9autA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=DKdx1Kk-8tCe3sltOUxdjvqroc7IuyUHzHrv1wca5t_CO6MvuDxBv5n31Y0i2IVhViqfzadY5rTJ9jdwfKX7vM6GBQSJsMjvvrBgIJRPYnM0KPqicF41xG_9hatXMk-sjpOCaPgHIkxW334kwcgO-xLgE_KWg6eyjGAF1DgRdtUHTt1-jkMdEFHsCN95SQWA0dktzjGPAJDwBzGFipVouwpPJEz-yvObbs0RnG5bcd1hKAa78khL2xmZClx8OWG930SMJvXouZ6RAWPLei563a21lZHSQsw6fxfEFcFKHd2wpoQBUtUNpsBMgD2WmdihQhoP_oEGgfglhbHMsLEzUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=DKdx1Kk-8tCe3sltOUxdjvqroc7IuyUHzHrv1wca5t_CO6MvuDxBv5n31Y0i2IVhViqfzadY5rTJ9jdwfKX7vM6GBQSJsMjvvrBgIJRPYnM0KPqicF41xG_9hatXMk-sjpOCaPgHIkxW334kwcgO-xLgE_KWg6eyjGAF1DgRdtUHTt1-jkMdEFHsCN95SQWA0dktzjGPAJDwBzGFipVouwpPJEz-yvObbs0RnG5bcd1hKAa78khL2xmZClx8OWG930SMJvXouZ6RAWPLei563a21lZHSQsw6fxfEFcFKHd2wpoQBUtUNpsBMgD2WmdihQhoP_oEGgfglhbHMsLEzUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=eNbU0bmKhwGOeFgohphNQ2jhChYwG-ThTzp01DG4beNhnZo57o-vd3JpEF-H_qJzKakDMOG5MgTfqqXb2XrqM1D55QKUmsHspJRQu3lPsVt7-OifM2PCpxw2LEp0rDREy8gu0I1gNORzY8tjjdxapSgu2d-y2oVfJextlGhQKp2JZUur1rW2qec-rOPLyCIJTK3G2QGitvg4pLiNWCnh4auhOXe3qCznikMYq0GxKXfoQwmFGRyIsbiy0-BCueuOl8fbVb80Y0nYP_ipQi3hbvnUtHZmB1HLzFrq4s9yH5Og9Nj5sTsITMCUkj3v0cKqsXcT9OsQ7d0d-x39wXi__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=eNbU0bmKhwGOeFgohphNQ2jhChYwG-ThTzp01DG4beNhnZo57o-vd3JpEF-H_qJzKakDMOG5MgTfqqXb2XrqM1D55QKUmsHspJRQu3lPsVt7-OifM2PCpxw2LEp0rDREy8gu0I1gNORzY8tjjdxapSgu2d-y2oVfJextlGhQKp2JZUur1rW2qec-rOPLyCIJTK3G2QGitvg4pLiNWCnh4auhOXe3qCznikMYq0GxKXfoQwmFGRyIsbiy0-BCueuOl8fbVb80Y0nYP_ipQi3hbvnUtHZmB1HLzFrq4s9yH5Og9Nj5sTsITMCUkj3v0cKqsXcT9OsQ7d0d-x39wXi__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCkDzREyosoi0fGqhz7utjoRS8RIdE83ihRb1YvzxVuwJcx_5TIu3nWtyvM40p-Nw6lo15hgfQBYSy_71ldcsSBvMroexnDfg0noQWGIMUhtdf2tcgt8aW595JDy60gnsWyqxhgHpS1uWKefhhItoOwH0tntWfvMtsFZQD5I1j-AHsgt6fUajIVBR3ebJwSD2rrT-7QuAqCQS46ErG87lFfMyBKzPgRN0-1regKieMq7xCI0mzEzBYT_W4dQU88Djcq6fBq0oUFsk_GC-1SXIInFBB42eMC3P2GxvROEqfLZjU2giLRVFZp17wwMJnSGsjQogyI3yo5JL0l_pmVMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n27F_8eormeJaYJmudWmmRnbDNcQFCIifOZlgRPpy28fzBX0C0KfJ-PSE47ztdeAbpXJDWcJ2NELwJdYm827dbmUNxLldQJqyol9J_tHRVDB3MVO_tNVQBURx5P6Z7GPie8wMrWBSkJ1hwBrQC1s2M0pp-ICN9EUo-NsKXiSkQOs0bWgtEzSUTGJpt3zv4b5PnqLF4VWKi51i7fddxtYng6rLvxXh9EBX00egqfkyoVwj7KbUOMhWFGT2rEnEPHHzYZlVqllI4A6YfPvsaYGBAB4fBVOXTS6sXEcvN2UgYOjfoDvjvdTh7kclvR7L1LPW2oxWZL6PLX8IQ_RskGgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fu6qCNF5E-DO-Jfv36kYbb-To_nNulCJc_Vyof4y_7msOJTjcijMA3B7XnTyXLHlg6-FFQO3MGWXFZ9EHXYI1PjBh2OUPzvbsm-erBysOraqKgKk_KHACsJzJWNdo_AV7uw-omgwdXPdoNhCdE7-P2eSXEFlUtDxqsV_vLRNg_jXmTaQQp3djh0xAK1BXA4ZG8I9Fxi7G5FWTo4KTpywUaB5JMwFs9zqr0ZF_u1rJZmE7eR2OkuTIQ8JzPM2x0wjmLPCopJtzH361ow-bpgUZ0bgK1suIdAkHhGxfrp3rAjrFtnVdPnkqEqEFoLr8oePen8xgaxgYsrUejabS82mqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyIGoPC9gJveeBTm7AXnrlF7IDbTvdyIZYv8ZrsVUb58HURMiMAX8uBBhN2ZSpAj2hGUXNn9lOP6rRNwddfBqLIut4Cx5NQLUeaH7EfkFDaOqNg1uESeyQf8I4vHH1yP4TO5-URFKqe5JzwgYZVaEV0diCpYW7rIK-RAzQP3A6TJlBahyUOdS6D0h04pJ8Gxdbz0-aDdc-7-3r-aN9-IP_JdCiHYUR6xieKTZT7liqOXXc5Zzj0ivRvV_gu-zuwicAXc4x6kcqb7ePMiNVyfgXAx9CXTLu42ciLzijM9BGPFXkkMvKDZkVnnE-u4SXdfFWyDcIjfKDa4g8EAOsMSDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=KmocJ68soMHmyMbeucOr2yuq3_M-9NVD7rxD6ttJNnVnRebqgtMrs9__tot9eaiZEoVbVRoZFKO17E7JzrNHIh83FzT5jVXk4t0MR4ZBYf5o85raoxkBVLI-zdn55krG97YsYVR30XtI2ummUK6-9e_cJQZ0hRllsdtquPhXN5LB6caCq3x9-NOs7UpjRvwZgkZR_WDnoili-77eI5ezxYAi3cpdO9QyOk8mzFV-iXfPSflwcByCT0YZN99aaiaB_Ba1ILAxYiOG5MrPKa_5T5ahTjzcRHwwDqrFPPO-i6vbdpAWmd2vfd092w6Gbem6QVumPQyyPzjHDQQSlW_QIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=KmocJ68soMHmyMbeucOr2yuq3_M-9NVD7rxD6ttJNnVnRebqgtMrs9__tot9eaiZEoVbVRoZFKO17E7JzrNHIh83FzT5jVXk4t0MR4ZBYf5o85raoxkBVLI-zdn55krG97YsYVR30XtI2ummUK6-9e_cJQZ0hRllsdtquPhXN5LB6caCq3x9-NOs7UpjRvwZgkZR_WDnoili-77eI5ezxYAi3cpdO9QyOk8mzFV-iXfPSflwcByCT0YZN99aaiaB_Ba1ILAxYiOG5MrPKa_5T5ahTjzcRHwwDqrFPPO-i6vbdpAWmd2vfd092w6Gbem6QVumPQyyPzjHDQQSlW_QIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahJzFfwkXm3Z4zawoyPRoOXOf14k_NrbMi2V9Y4jV-lEihETmjZeGvQUmrgb-bC7fkrrZ0efDSr16OgKWMcfaL6JH1Hzb7Q5H9_1mstDnZP_Nu7eiRC0IJ5hCRpZdm2bqw6XQn0PXE5OEyB_sM72MiEgKcCRKcJ7U5z4-yvmFZioL_4r8IHyO1J1vu-EoTzZDN6h63xcZuCy_t0vUTPE3mfpdB7jh-9MUStr9rE_XoitSR2isFhiK49i8B8RRXpD2i39U-sVz1V2dfM-wAW9A8ZaR4IdmnnEPFfo4szSor929IFsgmKPxvCcuKTXk0arXt78QoqZ2GCFHJINl_-4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr3S2Re5hQn33wtE5l51iSPs5w52ao1f85UHnWmHHff_S5RGAF4Nw170C19q2kJW17xXTCv8R5Fao9QinMDro8FnBrbrCogye1HTRjW2yWQFg5Lbloxsvk5JDV0Hb-6iR9Nqaix_JzEwgEmBo8x8gAAC-XGgRTN4oC-zcMSpVXPidHkyWoZq3O82mskM9vyPGWhcrYpbDq9YKLhs2x0Ej9IMQcHXY8ZOmn24UnoBYdew8pxUJcCuYs7C9LLRPLH-hfFLEKThA3qeZ2T6yxyXRjzp2WNKoSV2jq34lfNygKy4PXY9thadecKicw1IDlBsQwZHg7O1o8FQ1TJFjlhjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgOOkPpsEa6kRI9qpp3OKzpVZq9ODShHiO-fPGRKTGwbtVWorhFrKZo8DF8yR96Z1teWxLQlk_kfCVTVFM5nSFSDS8SO-9vSmcGu_raemJH5aSsAvViIuXupGvBhWUaGjGZ5BYEIAA19hPuImtm_mCMDZoSKvoHhM11o1BM1SSlaaKLC9lcUPjy_aoQ6-jSnt17_DE5rp-osm64iTtqUGC0_laJpQ77vKTyGl5KAYatGEgUUaWLtC65MWPvn7tSG1Z5dk5NDJmgN8bMypVNQ33S5Ol8L_YP5WEsjCZaG8teztok3Ckl2JQBSJ_fsAJknvkewpdKgNV1277xERHdelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=oaiCSbA06pajYmh1vLG_c5vSBYsJERnU2pr9SEoXV3jyag7wqQKzhmwEI5WRfAtc1s9scqMz4k31wjoJLHNUHbPz2-6YM89fUZuJgg2LVv47SrC9P-9y7ZNvJYJPXp9tZkx56NdawSKVfMc1dg1iT3F0CQq5LxgNpnxMk91UcBDkiOEdcBRPbhaFauwHQTsFSEZfBMLKjXCaA9XmjX2Qi6DoUquqR7HGUkfhjaNyv4nDjMKu3uBRqqSrDu3Zzwb3SddUdpaYq6BVvFIiT6H9UcWHda9SC0XaihZJxqq1wL7usOhxEHaWdFDOB6NE9Xpk3_bzIcYh0yC0fU8zX7FI4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=oaiCSbA06pajYmh1vLG_c5vSBYsJERnU2pr9SEoXV3jyag7wqQKzhmwEI5WRfAtc1s9scqMz4k31wjoJLHNUHbPz2-6YM89fUZuJgg2LVv47SrC9P-9y7ZNvJYJPXp9tZkx56NdawSKVfMc1dg1iT3F0CQq5LxgNpnxMk91UcBDkiOEdcBRPbhaFauwHQTsFSEZfBMLKjXCaA9XmjX2Qi6DoUquqR7HGUkfhjaNyv4nDjMKu3uBRqqSrDu3Zzwb3SddUdpaYq6BVvFIiT6H9UcWHda9SC0XaihZJxqq1wL7usOhxEHaWdFDOB6NE9Xpk3_bzIcYh0yC0fU8zX7FI4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4h6H28bNLslSvVb8-XoWUvjISn7Bfn7ymA1Kbup810oJC_O5yY8Rlki9VAnQfk-J1drkFs8fYaHQShxpP2GEfMGmJzK5NmjoBHvMH5eYLiaFpLmgBT8RotzPiTKOaCZpPniYHa0QtdoFmDscNKLjLSPupI7We9hMkq9iW3X5nEfLU1PGj4L1xXNM3NTdCAoe68TQB0FmV5TfjbcM_9ObR-kx_Ih8o5tn3MqzM-zYQHY0439MEXxwnQbOmkP03NQzKhDHcgzr1BZYa46JVHxXxnf4N4PBmb2vTJ-cAEZA6R31YZB9JCbB9x_KPDB0xf4BLjEgiZf9XSkdaHEQzRikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=jfsdaHI_GohBMiKYwBuZgmrc4dJpEiKTUrxCKBrC9z7ATUaPnEycVfPh4a9Um7KWknkx8GiPX51Y7TXYrNPc7Tmvvkun-BalCgFkQXrYhM6nH-X3YTt2CUCt76AAiS-3_twZiX5wcBAlDbRvyqgPybCxLNZX6jk3mlXIB9cNac_tutMo9nRPoFW-QeIqBzgIpEaWxa2pCfA4yiBfsPHK7tNt5WJKT_wEPdNNDZbdTEhuwfjYn1SnGy5yz-Q_feZBgHV2-dp4s619cxO764utcxoLPa47Lp4m6-B5wKpwxjImHMaVmEK3VE0Amg64QNAVqt1bUIFMhrJGDxLw-Iyz2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=jfsdaHI_GohBMiKYwBuZgmrc4dJpEiKTUrxCKBrC9z7ATUaPnEycVfPh4a9Um7KWknkx8GiPX51Y7TXYrNPc7Tmvvkun-BalCgFkQXrYhM6nH-X3YTt2CUCt76AAiS-3_twZiX5wcBAlDbRvyqgPybCxLNZX6jk3mlXIB9cNac_tutMo9nRPoFW-QeIqBzgIpEaWxa2pCfA4yiBfsPHK7tNt5WJKT_wEPdNNDZbdTEhuwfjYn1SnGy5yz-Q_feZBgHV2-dp4s619cxO764utcxoLPa47Lp4m6-B5wKpwxjImHMaVmEK3VE0Amg64QNAVqt1bUIFMhrJGDxLw-Iyz2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=QbKab77rVJgCy7-nvK6GthAi7KipW5jCR8Xz1uU7kZw9mUjk_R9f2AZIrgCSoGx7BJfwk_P6oZCRr2-d9ry3NdFcNBaWilQ4m1TAYV8mPiS11DP5v3tSS8uWsFLP-bBdjDAPms7Zf9HBIhAEFXOk8vuFoZQCuft7TPzY8kvcRwcHDK5ck9RT-viCTgzuva40DIoODGN_1oAhwncustfNiTE6XrkxjpY-tOHPySEbJSDlT9tciihmwG4_FQSN5PK2yG_4FUnuYI-5_Cg-K-ACq1z9vwYNUyOw_iVoLHspQZQ_uzG27WweKhfHyeeyccwXJLaMk9OJf5k__QWaRD2B-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=QbKab77rVJgCy7-nvK6GthAi7KipW5jCR8Xz1uU7kZw9mUjk_R9f2AZIrgCSoGx7BJfwk_P6oZCRr2-d9ry3NdFcNBaWilQ4m1TAYV8mPiS11DP5v3tSS8uWsFLP-bBdjDAPms7Zf9HBIhAEFXOk8vuFoZQCuft7TPzY8kvcRwcHDK5ck9RT-viCTgzuva40DIoODGN_1oAhwncustfNiTE6XrkxjpY-tOHPySEbJSDlT9tciihmwG4_FQSN5PK2yG_4FUnuYI-5_Cg-K-ACq1z9vwYNUyOw_iVoLHspQZQ_uzG27WweKhfHyeeyccwXJLaMk9OJf5k__QWaRD2B-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=S5YJmKl8dyuBQoBzGaHbil0tEg_PGWa5PJSf5vdSPB7i0vQSX78qgIKRg-4JVw5ZLqtH4ObngaR6opTggMcONMeiF63qir4xZOHOlBLO18koPIcxwZqETABGtcIIDkjRGlVKyJZcC8h2EUCCsKrZPp8zAh8-mWiGHM78arhGmH2ZIfDlhq-dl6p_3fi1NFSGZuGJbxLKmz8ftNofr83sLMZhVJsccJsNs26dEFWfrR5RgqsASG-QjCFsHj1nOv2bgsqZXC6qB6FW1H5KLCi0NWB5Bg1c8pvuhnBm2pBFC8qQS9ktwCY0xX-gfrUY4S68GoiWGSpk-SqWKpWheiQi9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=S5YJmKl8dyuBQoBzGaHbil0tEg_PGWa5PJSf5vdSPB7i0vQSX78qgIKRg-4JVw5ZLqtH4ObngaR6opTggMcONMeiF63qir4xZOHOlBLO18koPIcxwZqETABGtcIIDkjRGlVKyJZcC8h2EUCCsKrZPp8zAh8-mWiGHM78arhGmH2ZIfDlhq-dl6p_3fi1NFSGZuGJbxLKmz8ftNofr83sLMZhVJsccJsNs26dEFWfrR5RgqsASG-QjCFsHj1nOv2bgsqZXC6qB6FW1H5KLCi0NWB5Bg1c8pvuhnBm2pBFC8qQS9ktwCY0xX-gfrUY4S68GoiWGSpk-SqWKpWheiQi9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=A6zGyVwLGZqc6iyqWEVqts7qURVoox5diVMObMNJdnzOlWItRyfMiFG0b_rmAqK95VS3cuxebZYnX93oRDAxG1qLKO9al5He48OxfdX4grt2EHz7Nrs6DnfvLOjUM7qn6fIyAARWdzVYe4tNxknkYMFWc48up11CYM0kJ3K94t0ZlsXJ26qe52FgZd4fSHScj_4tuM3no-jnap4vGY15vxq9T8i5bLvzmVoKFbJYRwZFmkcHbxaQMJ14587EDmX3TXyYxnhV6SzRvRrZl_b7ptmGWNXns0EbWXr-qdAq9uUWfuKIWt9hF3biBdhDBjj54CODC5USM-3QUclOadmZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=A6zGyVwLGZqc6iyqWEVqts7qURVoox5diVMObMNJdnzOlWItRyfMiFG0b_rmAqK95VS3cuxebZYnX93oRDAxG1qLKO9al5He48OxfdX4grt2EHz7Nrs6DnfvLOjUM7qn6fIyAARWdzVYe4tNxknkYMFWc48up11CYM0kJ3K94t0ZlsXJ26qe52FgZd4fSHScj_4tuM3no-jnap4vGY15vxq9T8i5bLvzmVoKFbJYRwZFmkcHbxaQMJ14587EDmX3TXyYxnhV6SzRvRrZl_b7ptmGWNXns0EbWXr-qdAq9uUWfuKIWt9hF3biBdhDBjj54CODC5USM-3QUclOadmZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sD9YVzmY-1R6S9sv_2Zsv_nNhzipIsKvdjlecpWKHelhS5QKRx5RSq8xcm7UA9CGa3NI5O3ZAbkdSzLsbqX37daJmIBJL_sNbb6dptGFWEatQjyN5KWhJ6bta1tWGXh1w1pOg_zK5sjOHuDNlWUjtL8ANsNpXXvSyMDAlwRqcQH3Ybt-brAm7YowYCBlCntlgRsu6KHN_S-h2VICA1MJ_4q4SWE3SUt1l8q1wl3vRTlfmdnwVxYVTXGY7w1FjmxzDgKe7lL2lwEFwrhQJdBt8R6uABJpRAhD-35_xW_Xjka9VIX8Nz_kR4cBYwlEumq2JwkpPh4Vy7pgPwWPNl2RjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sD9YVzmY-1R6S9sv_2Zsv_nNhzipIsKvdjlecpWKHelhS5QKRx5RSq8xcm7UA9CGa3NI5O3ZAbkdSzLsbqX37daJmIBJL_sNbb6dptGFWEatQjyN5KWhJ6bta1tWGXh1w1pOg_zK5sjOHuDNlWUjtL8ANsNpXXvSyMDAlwRqcQH3Ybt-brAm7YowYCBlCntlgRsu6KHN_S-h2VICA1MJ_4q4SWE3SUt1l8q1wl3vRTlfmdnwVxYVTXGY7w1FjmxzDgKe7lL2lwEFwrhQJdBt8R6uABJpRAhD-35_xW_Xjka9VIX8Nz_kR4cBYwlEumq2JwkpPh4Vy7pgPwWPNl2RjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=uLjkvoYLV4GOInJKn04wkIW38iv9OG7aqNugdqi2vJgvxHP0L8t5oir8Z5QzfEyRZ7MojFwQqdHRX3TNbi3NB2atp-7UGfwKY5cpnKdhScbC4Y32uDxfUBrQCsh_xrbPrMawC_U9KXfUJhElfrzSa49SFumGYrrpv6vzdPJnkX72mZ56loJjFjqig966yIZJguR6KWGanATt15suvisVm3NADb81PJuOfSvM_VgRSc2yv6Q7HVC2qm1aDNSzZVnm9Hb9Oxi4-bnnk_Jr7lVPQWBFahhXaQ2-JomJsQOG_b8sWhlQKeM0n0wfCHvsMjbcXcynfJbMr8LNjm6GOPJWTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=uLjkvoYLV4GOInJKn04wkIW38iv9OG7aqNugdqi2vJgvxHP0L8t5oir8Z5QzfEyRZ7MojFwQqdHRX3TNbi3NB2atp-7UGfwKY5cpnKdhScbC4Y32uDxfUBrQCsh_xrbPrMawC_U9KXfUJhElfrzSa49SFumGYrrpv6vzdPJnkX72mZ56loJjFjqig966yIZJguR6KWGanATt15suvisVm3NADb81PJuOfSvM_VgRSc2yv6Q7HVC2qm1aDNSzZVnm9Hb9Oxi4-bnnk_Jr7lVPQWBFahhXaQ2-JomJsQOG_b8sWhlQKeM0n0wfCHvsMjbcXcynfJbMr8LNjm6GOPJWTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=pqWE6dF_Kx0SnFvuo4YPSn9BMnJwwTYF4vr-Id_mmZEiaGNYJFYSgeAldYuq-IqX_O0pyig2E6hHr9YCraoR06ZDnIQN4PgDHg6UXAiPXsVIx6tWZN3n0Xrw1mHuB031z221u47l9MK3vsdi7y22OVpQDNe5W-gvVr3wVzwa6X5Va1Fmfq9nh7iuYwQG7FeT0qr6N3PuOoHdAy3j6QzicPnknj1hUuOJ4OWgG1gS5MldcEaYDewB07NbyT53Wj8b3UB9Tj8cI6PWtVDqa-JbRFGRWDdXyxVF61o9xCQBru2mvVj7ar5_VDyUmLW-fXxSQpfKXiIvkTY5kuktR-3upQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=pqWE6dF_Kx0SnFvuo4YPSn9BMnJwwTYF4vr-Id_mmZEiaGNYJFYSgeAldYuq-IqX_O0pyig2E6hHr9YCraoR06ZDnIQN4PgDHg6UXAiPXsVIx6tWZN3n0Xrw1mHuB031z221u47l9MK3vsdi7y22OVpQDNe5W-gvVr3wVzwa6X5Va1Fmfq9nh7iuYwQG7FeT0qr6N3PuOoHdAy3j6QzicPnknj1hUuOJ4OWgG1gS5MldcEaYDewB07NbyT53Wj8b3UB9Tj8cI6PWtVDqa-JbRFGRWDdXyxVF61o9xCQBru2mvVj7ar5_VDyUmLW-fXxSQpfKXiIvkTY5kuktR-3upQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YhZiNDeJvPnO1cyhwlSahomXTlz5toPWNaVGbwOMDHxELt--wE-JWtGwec_vYPCAPvtzgnthx4uxU5HHY5i-GoWPhxfHtuRFH_BjAATe68RAfpZFcOXHEqc6HQnssy_rsGW4WW-kwk0hEpvFx95qTxeVGo4XelqtS0G_rSeUcbWqKW3h5ba092W9JEsxFPtP7UNOOUJYwueQvYZyIQw8hXU7DvZAt5e0AaZe97JhftIc3rv-ND7YDZLs861ReLmxprkmoBNdGRhsfUHcX3ZNmKVjzCT_YEwehwO3iyrq0QJyrCSy_SDKMXjdfGzHQpNjkkQxmM9ckMDlSUbhFjuDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BSnuQ-bNcOEAhtwkFGQTn2enrOpNAxa_w9k4OcN9uVrwleH1ZWrJOOv5aZgxCqw9QdhjrsfHwgRyAqfQr55VfPgBdIK1VIDyHsuJNvgaEH-2_s4jqWWYed0uDuYaFcE47mPtsXxEGauKXE4WRniAS3EZ047ukdhtiuG_bKKDJR-TCv0UHBYNRYaHTKIcNhtULL4DnADnQrh_0aPAEQ6loOAn6CdWoarXCzJqx246nBYcXWKGWvQxnaxcvb6_W-9Y4PUIgRy8ajWxj8vm96A2V9tkEUTZQGuN3gbIjgtGOH-EL5b6URyX2buen9DRT0QkrL0CYQO3GkWJYu72MrHjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=hEZEXNHV-gYEjHv-0NUvBk9eQW9jZSzz59guAjxjF6jgOJComZksKS3T5fc84bjEdrkIETjsoMWA20UgmdV0e1Cs3ciwfj2-bc67VIDBBmKyV7Y9oZZJYYym_hKRqvEBhwte87y8y8zIHC1OSBmjms_0dzgowbb--QKLOZYlVwVH9QwWYXJ1E7e_2djhiuFhNi39z0GKx5SbxahDFtkCiqHEds_jdDRyOeZ2JNIU-pZpAqBUln53_aDaGdAoQL8G7SwxnUTM9li6LobbUZzaleqrI3lKEuxgnhXnbtGdaBAdk39vNKmI4vJdFF8bgDF0KqcOiNNfT5DP7S4lD4RKERUoUl8Sf0ixVgG-cz7HkFB75X4GcIl-v5OmIolcVBCsNKethdbglN_T6XSSFn1EnBgRCWPnK_u1lsMyeJjRdlxRQahzDQa4Hn9-mX6gg7o2b_ajplWNHxXczRlfxAvfWOZD1lsv6bJfz750S5kkBR9UrzZvg3588l18uY-Wvqwn6HHn_OTq6BTiiwS7Uvoxv9ulWjLOz05r99Kc71DUO5EBtdS9dA4SLd2qVhBKcxkz8giidWd3PYbrb9S_M1U9DHJ9Qjaw6JQF6SjVqi_WR-W8TbY0Z50XzNlDA8DSq_LE2ZNa9kVKXnzkAB1VLC5wiz028d488EJwI_5wO4Rrsyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=hEZEXNHV-gYEjHv-0NUvBk9eQW9jZSzz59guAjxjF6jgOJComZksKS3T5fc84bjEdrkIETjsoMWA20UgmdV0e1Cs3ciwfj2-bc67VIDBBmKyV7Y9oZZJYYym_hKRqvEBhwte87y8y8zIHC1OSBmjms_0dzgowbb--QKLOZYlVwVH9QwWYXJ1E7e_2djhiuFhNi39z0GKx5SbxahDFtkCiqHEds_jdDRyOeZ2JNIU-pZpAqBUln53_aDaGdAoQL8G7SwxnUTM9li6LobbUZzaleqrI3lKEuxgnhXnbtGdaBAdk39vNKmI4vJdFF8bgDF0KqcOiNNfT5DP7S4lD4RKERUoUl8Sf0ixVgG-cz7HkFB75X4GcIl-v5OmIolcVBCsNKethdbglN_T6XSSFn1EnBgRCWPnK_u1lsMyeJjRdlxRQahzDQa4Hn9-mX6gg7o2b_ajplWNHxXczRlfxAvfWOZD1lsv6bJfz750S5kkBR9UrzZvg3588l18uY-Wvqwn6HHn_OTq6BTiiwS7Uvoxv9ulWjLOz05r99Kc71DUO5EBtdS9dA4SLd2qVhBKcxkz8giidWd3PYbrb9S_M1U9DHJ9Qjaw6JQF6SjVqi_WR-W8TbY0Z50XzNlDA8DSq_LE2ZNa9kVKXnzkAB1VLC5wiz028d488EJwI_5wO4Rrsyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=Onu61s_PnWUhl3ZNqbTcoOJmWgQ9jJlNmRLTJ0VZhApU01GE7MWyjLPGpmf3bRvk4EZprNFR0zjSRIw5bxDNItQ0cxVo4TSNGdYs-HGWw-gf8GO3Rs83AETKN8LDWx0JnWm-vOpMrh1vA3x2hr1ZaYRrgOqZTHvcrfsWwPSUCpxSS2wzk94kshWERptb27OZCVwYM2lZsAstEifLs1-r8Z2dX4SgR4X7tjvik-T-JyYTxpzrzKjNX5iqjeKIStwVOlF8I2dFYBS3MBk7GJqZl85fY7T06VU-c4Whncg2s-cvU0O-srfkQ4nfQAC0IgqehGwEr_C5bUJ_-ArnKny0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=Onu61s_PnWUhl3ZNqbTcoOJmWgQ9jJlNmRLTJ0VZhApU01GE7MWyjLPGpmf3bRvk4EZprNFR0zjSRIw5bxDNItQ0cxVo4TSNGdYs-HGWw-gf8GO3Rs83AETKN8LDWx0JnWm-vOpMrh1vA3x2hr1ZaYRrgOqZTHvcrfsWwPSUCpxSS2wzk94kshWERptb27OZCVwYM2lZsAstEifLs1-r8Z2dX4SgR4X7tjvik-T-JyYTxpzrzKjNX5iqjeKIStwVOlF8I2dFYBS3MBk7GJqZl85fY7T06VU-c4Whncg2s-cvU0O-srfkQ4nfQAC0IgqehGwEr_C5bUJ_-ArnKny0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=F_8_1p_pkJ_aCVCSpxyzcL-yiNTyevuhW3fwDQSkwPwQpkvrwlI4Rt_Wsf9KA7YUwapQrNkUQgMWtlrehIE8SVwswBBAa4r1MEIyxzXVnzYRPOVZh4EisNKEVLBuzAJ-sv2LqFTx7of4IUy4H3lz2nackPZpVdBHqWqzvM8VC5kr7FwHcOLM7OMerFOBIx0AgP-kpj-YVVsRPhOIk3r1wZ48S-rSK0-Irq7lGNlUiRfEMBvf2ShtFj0at_riAItpoLlYgsba1kBCmgmKUPXJVDR6RP9-xbsfGL3XX6TnZ0VIHNKkD2ZffN3T7tSMrXebyfuqvM6Vc32CLbyLmEy8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=F_8_1p_pkJ_aCVCSpxyzcL-yiNTyevuhW3fwDQSkwPwQpkvrwlI4Rt_Wsf9KA7YUwapQrNkUQgMWtlrehIE8SVwswBBAa4r1MEIyxzXVnzYRPOVZh4EisNKEVLBuzAJ-sv2LqFTx7of4IUy4H3lz2nackPZpVdBHqWqzvM8VC5kr7FwHcOLM7OMerFOBIx0AgP-kpj-YVVsRPhOIk3r1wZ48S-rSK0-Irq7lGNlUiRfEMBvf2ShtFj0at_riAItpoLlYgsba1kBCmgmKUPXJVDR6RP9-xbsfGL3XX6TnZ0VIHNKkD2ZffN3T7tSMrXebyfuqvM6Vc32CLbyLmEy8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=uF4l6_Oxl8gYa_q63VZb7VSCUrnBsevTJJqGgQTmrloM3uelng7gZ9fAC8MO6bln48Crkf83hB5gbmxsFHafkPtZtxLv14Pxv0LfxHy8cPh9lU77X3ShJ3va2yORDt0XM4NfFvENNSq_SQBo2MgOVDTBM-kkynqbUOr88n0mXksvML5FJrDj0823NhtVhI8AWZRn-KMTvI84ILceSxPTzp-wfpYkqWx8LY4lQcF9ErimDsHorn3ElMRynVHORqqzaqo_KPkVhwkPjkJF6gogpAHIu_Iqg_nXiuQSO6HkfJhfMc4axGyydRp-T1-vkq_76runCAZjUc8VwxyN__ZJUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=uF4l6_Oxl8gYa_q63VZb7VSCUrnBsevTJJqGgQTmrloM3uelng7gZ9fAC8MO6bln48Crkf83hB5gbmxsFHafkPtZtxLv14Pxv0LfxHy8cPh9lU77X3ShJ3va2yORDt0XM4NfFvENNSq_SQBo2MgOVDTBM-kkynqbUOr88n0mXksvML5FJrDj0823NhtVhI8AWZRn-KMTvI84ILceSxPTzp-wfpYkqWx8LY4lQcF9ErimDsHorn3ElMRynVHORqqzaqo_KPkVhwkPjkJF6gogpAHIu_Iqg_nXiuQSO6HkfJhfMc4axGyydRp-T1-vkq_76runCAZjUc8VwxyN__ZJUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=o2omqDkjs8pWpIwlAFUjBjQAP_PulX3-gUdr-PKnL0IPFA9AgZwJe9I-XTzgSyZ6FAZu3fkNVqh5L8R0m6-Pb9MTEaApt_76f2Y0NukoYkhFapzUciqRxFRIQrepdt7Q4PJsUzZMsNGR5BgUEuLR0CzCfb_9yA1Fmvs6qzrVHzhTKacUasMUQuaAxTeb0HIItT7xWnY0yaM8Zo2e5QRSXHqh1ZdgNltSQDfqkZYSiALRXhi2kbtVFEn0DYVHoGlSUqCIMlsy1iVfMzFFJYyMU9O33veqjfrYw8YxQzQupuJWiASOq8FAKbVNg1pIeMYYxo0-OZxbW_-GSxnsMtUZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=o2omqDkjs8pWpIwlAFUjBjQAP_PulX3-gUdr-PKnL0IPFA9AgZwJe9I-XTzgSyZ6FAZu3fkNVqh5L8R0m6-Pb9MTEaApt_76f2Y0NukoYkhFapzUciqRxFRIQrepdt7Q4PJsUzZMsNGR5BgUEuLR0CzCfb_9yA1Fmvs6qzrVHzhTKacUasMUQuaAxTeb0HIItT7xWnY0yaM8Zo2e5QRSXHqh1ZdgNltSQDfqkZYSiALRXhi2kbtVFEn0DYVHoGlSUqCIMlsy1iVfMzFFJYyMU9O33veqjfrYw8YxQzQupuJWiASOq8FAKbVNg1pIeMYYxo0-OZxbW_-GSxnsMtUZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq17ypOwpT7Z6xxL1B-KrF4CNs8tiRip5fVoiak0ff_h8DX2AAI040rxxsT9L_Jdi9BEJbd_luBPMuC4q_S5Qpc5PjaX34tsJg0jNijozfDgSBh4SmbTbrpb-LmAGu8FvfLoEx_aGO7VF-RNx3M8u3FKbEY05V9Nf3fG1HQwfAeGGb7YOy7bZqYzACqAU3n0uIF5r0pTTn9IQPz2C0SUGjvqhMfNuBgxU8Uq_HdNvms_St15oJYIGDB4l07m_cpQ4YhUslQWBYWenOJ-IEt-eWOF1vDZhH9PKivhvDTghGgYtCOcbdt5iiXqZuFsEEQB_CPUGMPRdJU3uiI1-h3q5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Leod_xWAWUPrPf-MyWXncured-q1dqNUDWsYPlGa-PpcMKdo4MkV-V6xYQBQDNae8m0CqHzIJxtgPFkUg731v77cGMYXhQiJGagqxAG-nUATT4w-gP2ygKHfJbwmWimj2sa9K42TjpqWqw1R_uqoEKZ-gPqBpuho00nEgRkSzggriOzpG0IxI9btc-7ELGbz5tHazzFnlaVa5aVDq7sPCKk3vXPeRoWRTX-O74GnXMLZRF1CUIwZrcPn0YoKgL6OkYkF00mJDNjBqQowqJ_7uClZy42l22NCaOpgyiNihG7Fzz92Tlun7C5xZ4DOEnihSPR3kLSw5rlGu5WsQUB9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3TnpcZqZVy2xItmjPi5FbX7sEv5oCWhNpc7yIJDAubW6ih7mB241RDSL_wuvmpY9lxYrdnCwJwi8GmSb1kln2KiXmmrIW5drCCRW7D3oxlhV3hrrKHuwXJk-4A2k3FyCvrRl309enDEgfqHBwXMWx494LoGW7s01NxmBH-YdQCas7rWnF6SIl9uS0Siq_Ntdcw9ZtlRTa52Nll8Ey8lI591QhbA6dBpjJb_xUe7eHfD28VjohfPxuVCH6SnP1J2B4YO2jsPfrWT3o-OrFfcZBeMmM2iYchbZfrQgADwO1GWJ5kgHwapirdmn_kRZfYO1j4F_Xv0NOC4iDnxWJj4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkfXaN-omwnZ0EoVOGPZscC1tK5OJV3oClYpkINeKyPsYtpaaCj9_ixnvsw9pgFa7BxqUoi5I9MIq_PIaubP5cItV7fiX3-squQl4kPV026XPNeTcDsOvLBv5MGbpFNquoTA1j_ItKOwC-gOB0Rc0a9Jz-vJW5Ml6fVo6-7HnBaQdtSMAl253GdltkUIICc7fD4HfLBokmzHbLqG35I_wtIZAMW_77JW1v1dPn_HbnkUImBkAY_D_9RO_fpGeYdbnU19AvWYiq9e1LIhD5dUe1mdnlXWXZKAN-xr2uWK4MMB4L3prySNaRH2ym-iDS4NsbpTI6be6EIEQc2qHMWdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF5_Y9DTKqmRZry1mamu5aa5h0lczav-F5n_VxF_42_0SDcWFBkNi9q1OTLuoo6_tnt_j_8OtDunN0O43PTFiPPmECwz0Gp7CIRID1FHa6bymPoYu3kEVRVF5G3PC0Fb1I6hc5H0G-9KOgo0XJURmn4yrbvb5yp0Hhw1JfzQ1N71H82iqxY9rcdU8THsSNgu_VdHXq8NkBDAkPDmHVeW1DBDE3xXIDBXcKNoToUSQMN163o1kLI1fYhxgRxmZ486aor5KjgLLTXrTIj1dQflzzV23dvddnHz0nsfey2TrBiyFwe3_dm2WhZT2CCFQFdYa_M6s4MHBnRYub5Inj4tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq-okK_LucSLVERj99STA4ohSQiA9tbwxZpF9G5u0BstSEeRdKNSmpSILPsEDannPQRQQoqTmbvpkj6ijzG7ob5dO8hN6NtB7ckpTLuOeEy3OoDwMbyrCWOoxDMIrgxZX1P4riikAjrVKk3NOmvo_5CrpanGJg3yQ6OXPAthWFXaALlry4gPFTTWaoJCu1596tM0uHO1qPF0zWrTC-ShJhum1ejlHbnwtVe2HGQmurl9yGPcINB5hn5g0J6vqwj8kaQOwQgBbQ06U7y2WJ2EAMQRxq0sxNaH3nq0lUBdtTa-KzFDgtMnYMCdKsS7YSAOG68GLcg8eNZpAFDi3-VF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=uStGlw8yQ8eVOZqN03BgoJRWK7vmzVH_bvcd1RQki-zpFUTMPYs__knaA-wiQKDKMc2jckttDlIhLu5XRJ9vDFoiPunIWoue9qBN8SUc0OyY3iS_tqK-AB2k_cCdbSnhp04LcKVhLTI4J_ZsinCC3DwZyl6oq5B4wYCsUsS8zQP4EyTPAdRGGaj9ZutJdB9lkQEgofATw1LP-OWS8PwRq3pRNi6ZkTZXLtByJcKvi_VVZN4YdMcppZFV5sdb2YLOxb81BAPpJb2nLahck2L_6_qm3mZmtUNPb4E6DtMyeInmiECrwVPMU3s8b1tR8mJOP1rMGj3rwH_5AsNb2kCFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=uStGlw8yQ8eVOZqN03BgoJRWK7vmzVH_bvcd1RQki-zpFUTMPYs__knaA-wiQKDKMc2jckttDlIhLu5XRJ9vDFoiPunIWoue9qBN8SUc0OyY3iS_tqK-AB2k_cCdbSnhp04LcKVhLTI4J_ZsinCC3DwZyl6oq5B4wYCsUsS8zQP4EyTPAdRGGaj9ZutJdB9lkQEgofATw1LP-OWS8PwRq3pRNi6ZkTZXLtByJcKvi_VVZN4YdMcppZFV5sdb2YLOxb81BAPpJb2nLahck2L_6_qm3mZmtUNPb4E6DtMyeInmiECrwVPMU3s8b1tR8mJOP1rMGj3rwH_5AsNb2kCFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vT81jSuynk-NI6coU9K1AIbyTWCZi68iOIOcCioRSPC4dA4Vab9FgGINq7tRnJPQRwEl-6JrC3kLAzOLY-FYUuZLjGTmKKgxw_gUIK7G-kpoWbDUCgF-lwfTI0WIzIfu0Yx1LaxqTw2299VpT-mWkFWs7xQ1YD-RHVfvJS--JN9VO4FQ2niMggPz1Wo8QZ92XOOo_7L0GlEGUwBfwEMebomeub_KSOwsj8mttgO7TxjaaPAJbsegK7YrGKUJJKqF7D4P7WGCNceQn6P6OxliM1B_1fmbBNwRVts7jOKn2vDepyIz8OtPZWPnAA91PHGpgdRIHebSUqSUsZbceI7FEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=i1mJ6ZYuqWP2qqaDcI6LUE4b8MMvjGEcfmKktUp4lPkl2WNAQ1bOie0cpr5wKeiKEOQFJPuDIxRAUm8TGMTbxU2snNzodiZWV0aYihJNH8vyNKCYCd_hWkpiK5HlASzGpqNf3ejaDTKgT2RlGpVAGQJbWDPGQ6_IPbRSr_0SNcGB3FS__BU8tXLEWJsrzpgdrrq49mrAOc3QXNXV2GL83h8hF8q3wH57cIioYZCGXevyQ7tkqF7ziPlYxbGnnQXntl9hm_3ECOlB7ZQtMFXDzHxGW3P8pmaRz-AlZ6clifdqtjvk5qxm20Xa80dDFpmLov_sKPGSM7NSshAzfl3r8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=i1mJ6ZYuqWP2qqaDcI6LUE4b8MMvjGEcfmKktUp4lPkl2WNAQ1bOie0cpr5wKeiKEOQFJPuDIxRAUm8TGMTbxU2snNzodiZWV0aYihJNH8vyNKCYCd_hWkpiK5HlASzGpqNf3ejaDTKgT2RlGpVAGQJbWDPGQ6_IPbRSr_0SNcGB3FS__BU8tXLEWJsrzpgdrrq49mrAOc3QXNXV2GL83h8hF8q3wH57cIioYZCGXevyQ7tkqF7ziPlYxbGnnQXntl9hm_3ECOlB7ZQtMFXDzHxGW3P8pmaRz-AlZ6clifdqtjvk5qxm20Xa80dDFpmLov_sKPGSM7NSshAzfl3r8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=OXlkl9Jby0yQMTcpHh9ZtSM1xv8FrUHUykrektMGQMmqB9EHCIKvfQNiJ-R7lDxAWbGmw6_Av3w_P3h0h1o9_mJ5tk3hrvNKOIJTxRmRyEJ4-owSTe_yoV_K_dpFQlN1i3pfQpVzeJ_HJQ8KWg7Jrr5UnfxdW2zT5nf-TEjfaiKwVnejmZZwiFH-0tukgSeHB9FNp2ZCbQhOK6p4GuTgg3EktsViR1nqisMb5umesOvgMuL_FCDFxSqgavAp65877zGyNg6a-n0i8FICVlGngM2H62A9PyWbmJU4Kd5He8srx1Nwl_6lIKwv_E9YB742r8CVjfGnNlcQR3mjWlPd1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=OXlkl9Jby0yQMTcpHh9ZtSM1xv8FrUHUykrektMGQMmqB9EHCIKvfQNiJ-R7lDxAWbGmw6_Av3w_P3h0h1o9_mJ5tk3hrvNKOIJTxRmRyEJ4-owSTe_yoV_K_dpFQlN1i3pfQpVzeJ_HJQ8KWg7Jrr5UnfxdW2zT5nf-TEjfaiKwVnejmZZwiFH-0tukgSeHB9FNp2ZCbQhOK6p4GuTgg3EktsViR1nqisMb5umesOvgMuL_FCDFxSqgavAp65877zGyNg6a-n0i8FICVlGngM2H62A9PyWbmJU4Kd5He8srx1Nwl_6lIKwv_E9YB742r8CVjfGnNlcQR3mjWlPd1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=lEunBPU0q00YDXuhtiOcRhoZ9pWURkT0__MHxu1P73pB0UVcAsN5CMu0p5eypwz782rmuIKZQPtoKy29Xkdbw-yJmd12BfEBi3H0X2UJ43GQZdYByHDHcJr5eqDRgPlm1mblmn5l89F-TOLpjyaJAi865zlqFNUTpwqO40f19nt9XHJI9AOeYUBfxWaviITq_1LsCW9k1MOK1K-EdXwczdi_9I7YvqW2wzWcLPf4jx6n3JsrTYsvhu336YgLUVv4tmUCalIYiICDrM-c5fMRfGRdws9WEQWEcdDtWjKDHU9tFPKZlzSMYaL_wm4RPaPm6bZMGKDtK5yM_2yGcyx8Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=lEunBPU0q00YDXuhtiOcRhoZ9pWURkT0__MHxu1P73pB0UVcAsN5CMu0p5eypwz782rmuIKZQPtoKy29Xkdbw-yJmd12BfEBi3H0X2UJ43GQZdYByHDHcJr5eqDRgPlm1mblmn5l89F-TOLpjyaJAi865zlqFNUTpwqO40f19nt9XHJI9AOeYUBfxWaviITq_1LsCW9k1MOK1K-EdXwczdi_9I7YvqW2wzWcLPf4jx6n3JsrTYsvhu336YgLUVv4tmUCalIYiICDrM-c5fMRfGRdws9WEQWEcdDtWjKDHU9tFPKZlzSMYaL_wm4RPaPm6bZMGKDtK5yM_2yGcyx8Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZomeV-ksFLROHIKlu-f7KGfQbLuF6A5QTbxYxX3vlkHsxo5JgODHdCMEV8C7FCSYYdlR7Q64Rf4l7ZwROX8ayn3kqnTJZv4j2OAAmdQQJxuJpUFAdfG_RA5bTDLd5YPNKGuYJmTzxMaletkI20_wHwD-YpGCBU6PR-Jamnic7QCAnTBNadfGBcTq5HjSD5_9qmLFIIzsa-dtMujxtjtz6_pOYzCi-_b2kbBBQ2GBvF3sSbKIcF1tdp4RR6etpeyL96Jq1Wlox7z27ORmilDfAg3lwos_nOajVNgEc88l9vMi-Rl_f6ljkQch97suxLOgGPVETvLWLY5apCiIRy-5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=lVKDQe9dVXUB_0MYK5QWrAmsYmS6cQ5QMw5GHkm5eHzU6sJY41XFCH1WXUhCu-we7KW1qF5JCgkGx2j55KUdOGVF0jbNl4e6Wf2khli2TEfmUpPFswN9h3H0o41ZtQfnMe_n8s7DzFs3AOF-dA_UT732-lDwUO6sogLlXOrvy6WmkVcMlZUjOYnx5SEdSO8tE-woZb9nkB1VE-HfrCeEMvNYQjmhNAceHNSxQtZ2jptr39W0S10qf8Uuf-UOJg5Onc7OQnOAqZp7MLoyOBspo_JC_-mlb9Pa2j_VV2jvXTJFTpx0wjasGU-v1H3vzTq9-uJx0pbfaNrulaZy35U7qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=lVKDQe9dVXUB_0MYK5QWrAmsYmS6cQ5QMw5GHkm5eHzU6sJY41XFCH1WXUhCu-we7KW1qF5JCgkGx2j55KUdOGVF0jbNl4e6Wf2khli2TEfmUpPFswN9h3H0o41ZtQfnMe_n8s7DzFs3AOF-dA_UT732-lDwUO6sogLlXOrvy6WmkVcMlZUjOYnx5SEdSO8tE-woZb9nkB1VE-HfrCeEMvNYQjmhNAceHNSxQtZ2jptr39W0S10qf8Uuf-UOJg5Onc7OQnOAqZp7MLoyOBspo_JC_-mlb9Pa2j_VV2jvXTJFTpx0wjasGU-v1H3vzTq9-uJx0pbfaNrulaZy35U7qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=s5CJxZ3Kqo0kn4ybvzDL4J76b1DXqDFoX1BfCiOTZKfrYDjpSF3iGCbPzcFPD3D5e4WSlEUYtDF7-w7EB3WnOOPTsgbF_LcZ3u9AKdHp6SSNmnNQ7UmxX6dlipKoOU6MXgbusE8rdubjU1tfIojMEhWfen23HsZpgzqKgDkln84lJ0Kqzj_RhTckNEIssWhFy8Uu-ZF7UFTZ_C55yagWSeIKTC1CK7qXC-Q8R16M0e9hLJp6COeVL-cbwrDeEnaSIOsrqptMNgMtdhnVaYM8NPxb7H-zwGAXh7pxUebt-QbJNhDwyScNOBz3Ey_mmyi00dsQy8kmmEfL0nGGa3wgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=s5CJxZ3Kqo0kn4ybvzDL4J76b1DXqDFoX1BfCiOTZKfrYDjpSF3iGCbPzcFPD3D5e4WSlEUYtDF7-w7EB3WnOOPTsgbF_LcZ3u9AKdHp6SSNmnNQ7UmxX6dlipKoOU6MXgbusE8rdubjU1tfIojMEhWfen23HsZpgzqKgDkln84lJ0Kqzj_RhTckNEIssWhFy8Uu-ZF7UFTZ_C55yagWSeIKTC1CK7qXC-Q8R16M0e9hLJp6COeVL-cbwrDeEnaSIOsrqptMNgMtdhnVaYM8NPxb7H-zwGAXh7pxUebt-QbJNhDwyScNOBz3Ey_mmyi00dsQy8kmmEfL0nGGa3wgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=VtusyIlPVnrJbcgET6yxQ9c8_jYlko8ExIm59qBI8WANrhhkTj9hlR7xS_-52Ecri1PfHfC4FnDEHyNIHzcfQa-9BdqRSuQLRThmfg4UA-WASSeU-ZrrUhJXcv-ZDYI_7YoLAAv8_EZ0gjhZMEe7iPcZ1CEjPHThZUNQYAWAwK3WpkN_RkXOyGMGq79r2XVoMglgAKDC_dFYmiwDUqHvHgaqXRA8GvgqL7SSRKH8fvJMK7LU50Qk7pFJ3EeuiA8qTzqbzJVhGRtQw--yekkuoyUU8Sh8ubOGk_04NixSm88j5az0BCsiQGQQEpFGdlKXZZAQZhLQdHtD0M3GkmZDWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=VtusyIlPVnrJbcgET6yxQ9c8_jYlko8ExIm59qBI8WANrhhkTj9hlR7xS_-52Ecri1PfHfC4FnDEHyNIHzcfQa-9BdqRSuQLRThmfg4UA-WASSeU-ZrrUhJXcv-ZDYI_7YoLAAv8_EZ0gjhZMEe7iPcZ1CEjPHThZUNQYAWAwK3WpkN_RkXOyGMGq79r2XVoMglgAKDC_dFYmiwDUqHvHgaqXRA8GvgqL7SSRKH8fvJMK7LU50Qk7pFJ3EeuiA8qTzqbzJVhGRtQw--yekkuoyUU8Sh8ubOGk_04NixSm88j5az0BCsiQGQQEpFGdlKXZZAQZhLQdHtD0M3GkmZDWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smd1HkQ4Zs7p3LDDfD2RnB7uLVSTvV21rcR8YyTCWNRnnztAh46NNN6-rgfEeld02oAcKddIKY_ouRHVmDhT0HjwZajDMXsFCiThmGrrqflBzwhRyG1sViK-SW60XFgbiCpjc-P4H9H5UwpIneyrN7AjtO4gVLhpL6YvH4zY5GOpIkPWmQ27PDSeaEMTrMcKbPavwExxb2GXKSznMi_glIAEKYvv3Ldp0regeq8S4pnxTaa_CgN9NFebltyDL-f_SgM_weUM3BEsL6b3yIVej6VxLHJQe47vcdSMjjEeFx0ULWq4Z-4tKM-npMSTpRECsBIsWsweS30RyIGZF8l3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBY_CeYQpGUn5kTmXAWrQWf6HeOpS1OMAOofWWXDyOMvKp2QIvNvrMJyWm7TlcFjPhtUNv7f7w98kVOWhLq42nVkzDK1CWsBUc2qKcD13COe7qJxh9u4uVSVyx3zZojHGRXl03IoacTMDMwxMWUvJz4E19rRLdhV10g0atHaS8z3dO5C6jd0bNy7Jr9jD0-MO6Ila5O0Hdh_2Wj-Cp0lx8v3Lxj1nJiTwwhHO-8GxQ3_X9QMuRpbGQLm_jw5wflfRWxQt6e02vSAIv0u939QdmQtZ5jZomrgVGeSSLc1rsuF68wf1PnIZbyH0yVEPrbh4Z-cZpGm5fcE7QrzKL2gbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=iIMjZmywAqb0fEuNqjL4tsVtbW_3AmoJJE-SflyjbivPaC6R8LVUPhmZAF6MesVUVnnnQQhdI5BmS5Rp8YII78GFV7TFwme_SeMqdPxuirqPYm-Ebq96BpP6RQFUDYk6ARKw3vaZ7IngTW5b0y4ip-eewaYebYkC3Hb2c8dDveU57UZ8dQ2LLOPzHoqtH3rstAQ3vqGO6sYjxb3XLH1wricaDykQsLJ30vriy4jjDECxTB-9FQydUzpgqTxM6deJDfJWCWDBPMp7qz4mYS61e6XUST-24Be26sAut_gvPzyR9_Pfx9WM3ceE0tyYg3lEKj_OHEGw9fyZJWqqc-DJ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=iIMjZmywAqb0fEuNqjL4tsVtbW_3AmoJJE-SflyjbivPaC6R8LVUPhmZAF6MesVUVnnnQQhdI5BmS5Rp8YII78GFV7TFwme_SeMqdPxuirqPYm-Ebq96BpP6RQFUDYk6ARKw3vaZ7IngTW5b0y4ip-eewaYebYkC3Hb2c8dDveU57UZ8dQ2LLOPzHoqtH3rstAQ3vqGO6sYjxb3XLH1wricaDykQsLJ30vriy4jjDECxTB-9FQydUzpgqTxM6deJDfJWCWDBPMp7qz4mYS61e6XUST-24Be26sAut_gvPzyR9_Pfx9WM3ceE0tyYg3lEKj_OHEGw9fyZJWqqc-DJ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q0mrpcuDQ7FIMafEIOJwdfeS2rlXgXsPd02yiZcDk9JFjmd392u3Mg_ct6tm2WO4_L1IwXAzsb2BGj533j8NqwouEP7ZOrcs3m4egN1HaymdoRsqLVMvMyZcua83NsmODa74-9XXmnXSzJ5TPMVZN9Z1ld5zcMSVuzztf_iRpWe5xrgKoqTqfcXgHvGIP-h0pihrqztHkqSVGbJKrJD0_TJ6e3EX1EY4T0xglj28Pn6-Kp1szLEGPdGlxs2ZZzZMWqLyB4u6vKpHSPsJBJTOIXsZWV5PS99OwM75AlEplTXKtO9qNRbwiIs8qWrQU-7OdHU3rikTbZo16gIXQg8umA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=ozDu76Vz6fleatEXz5bUngNMA7UYvtzMapB3lwrN_uOu0IHCJASF6fgqr8JKg5lx2zg8TjP7AoAejlAnJY5LjBK8mOqS4dacjijxFrKMetUhOkMpCmOt1GkEyfPchmAyDZEjK4-gcbjcqQ3FipYCLInAnTjqntU6qVTGU5y1sAlnAHxTeKqRsdT9W3QLj9kryhRzZV7ztEjtN3Mk4Wvib3wK2ypzEfqJ53UzpR1S53QJ3gT_qkZ7UK4_4HDq843R4q3_b-Twjbn-S4Cbpp1kuZJwi8jZDDvJwU6vu8CHTdahcFwQP08rs14fF6p-iTYM3_vw8ksWa_yyOdKc1Pktmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=ozDu76Vz6fleatEXz5bUngNMA7UYvtzMapB3lwrN_uOu0IHCJASF6fgqr8JKg5lx2zg8TjP7AoAejlAnJY5LjBK8mOqS4dacjijxFrKMetUhOkMpCmOt1GkEyfPchmAyDZEjK4-gcbjcqQ3FipYCLInAnTjqntU6qVTGU5y1sAlnAHxTeKqRsdT9W3QLj9kryhRzZV7ztEjtN3Mk4Wvib3wK2ypzEfqJ53UzpR1S53QJ3gT_qkZ7UK4_4HDq843R4q3_b-Twjbn-S4Cbpp1kuZJwi8jZDDvJwU6vu8CHTdahcFwQP08rs14fF6p-iTYM3_vw8ksWa_yyOdKc1Pktmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1AqyfX6UU9kauB37lfqJhxaCFuK_D9ip7jtLPYCnXWmwEAQHSi4xQQy3jfntQ8UQVT7gDC1sRnDmJeJ7rnLBm8FjCjKNfyE9lB9_pelXrnYd6dxAX4W_RTLSJcAdnvDmOiNpRBCrE36G3L-8zZzYaEFWCQ7l5F9x3QYP5ZIatkYp7ZIe4M2luh9M3f6fmWskdSFc4bAF1Ewt0EnlsLbIPKKZKwRdBuAwfdufH-ReheAKYsgpuu0_HQiPF4v3Cy18aJ9N9lVn-dgBu7iGSOtmCVBBnmJ1cQmkO92ja01fQ95ZVnEpLFQh9XNPd4yLFNDEgo1DXJ-mf5mtaUyDXSAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=aemyBzmHvChmp1sbf4fIclb5ydEoZC3etR_6MQB_BOdZf7RJ7r14cl9-oAOsOU2b7n1kg5Zt_uUrXSq27noxOe1QLs3Wt3cRYgw8AKmP_RyDgX42lV_zBjn7PjiOjJXX_M265yTYQtg6g2LH8vAZTfL8g_VmUJL_pDGhU6GEvaHZLSUcU-a-_ZiL71Ac7Zx4XJG9p8FxcAvOSxY8NlEo3Su21TgDEoo2rPSsuSe4OKbww4FIwAGOhLyIcSEdjHRrTKxnmXBC5Ety1TKFFlAVx3ZXsXqzmdOWZOq7yb0oFJM0a9Z-wO3iKpQpK4qxZzWlNpqghvMaYTyJ5leUzR6yYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=aemyBzmHvChmp1sbf4fIclb5ydEoZC3etR_6MQB_BOdZf7RJ7r14cl9-oAOsOU2b7n1kg5Zt_uUrXSq27noxOe1QLs3Wt3cRYgw8AKmP_RyDgX42lV_zBjn7PjiOjJXX_M265yTYQtg6g2LH8vAZTfL8g_VmUJL_pDGhU6GEvaHZLSUcU-a-_ZiL71Ac7Zx4XJG9p8FxcAvOSxY8NlEo3Su21TgDEoo2rPSsuSe4OKbww4FIwAGOhLyIcSEdjHRrTKxnmXBC5Ety1TKFFlAVx3ZXsXqzmdOWZOq7yb0oFJM0a9Z-wO3iKpQpK4qxZzWlNpqghvMaYTyJ5leUzR6yYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=KH4Q_jNZRLD5Xq8QrVcyVj-JegyX89DtYJd1ikizxymeg-npmVzgAu9j6Y3IFh4tB7AAB0ocIFOFjV_DZrLTvoz71yskqiNA6hlx2R9vmRY_B54FAJF1RPa11WiE1QBgRl5VIORDkVjM5Mao_FKllrgRlt7fsF5tszGxWlw66Xl7uJDgtvIeDYBCADllJu3w2jhrNBRQNnSNUw7xEHx6tTLe6MinrGybdSrdLdiuikhp6h_uevyJvscF8wJDurhvpASQtPPe8WsJkaRXxqQGuTGqo3HOGxXaNRvCw5M8tuJxqxm2RDj-b2BaI3woN5FK6-pa1BpGzVgc_71Rev8FSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=KH4Q_jNZRLD5Xq8QrVcyVj-JegyX89DtYJd1ikizxymeg-npmVzgAu9j6Y3IFh4tB7AAB0ocIFOFjV_DZrLTvoz71yskqiNA6hlx2R9vmRY_B54FAJF1RPa11WiE1QBgRl5VIORDkVjM5Mao_FKllrgRlt7fsF5tszGxWlw66Xl7uJDgtvIeDYBCADllJu3w2jhrNBRQNnSNUw7xEHx6tTLe6MinrGybdSrdLdiuikhp6h_uevyJvscF8wJDurhvpASQtPPe8WsJkaRXxqQGuTGqo3HOGxXaNRvCw5M8tuJxqxm2RDj-b2BaI3woN5FK6-pa1BpGzVgc_71Rev8FSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBJOZtt7_foaDmKnQrllGs2f7t0Dd-qLB3wg0hvYzxjiFyuQS-H10mcRja4EC5f9ZFWHnPAcA7CB9MvB7KWuYHvPZp1vYsY3PtLdNtrOCFcevCBeo4tCtWUCnpby_grDJoUNQV7wb0zM6i9137iQYDrxxh5P_Pxa8bmh936nd7ErFubzzrkRniMuAQz87iPsH30FRiI73z3OoKJ7tEiFihcw7MYvEY_GFJX9Fq2nYbDt63QP1gn5109kgUT7u5-91BuFKaU3vhuVBfUxupPYSXJZY3k1J2gb87_7DPOD2c7aJQzfIWEbT2FAZh9vhk9__feiC0gmTKJhYuKKK62bjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paUzEIGt1db5YmYu-62q7MqdvzVtHPGJYC8qSWaA7u4F7BoZ7CXa0WQewKnV1pPYC2ohXafNzhWan8G0HZISaVzUd4ioSga7xonWMJsVAgFIox0MfkuqLOEeVWjS72NJYYUqmISKnG9ogkrP3MCdIeQxRawr4k175nX199l6L0r9qNzydy-Z78Ll-Pwsw84RXdSgLUYfTrOIFbh6kJgRfATvMW8XTsLK6dSzkUt7VnEui5HuR89NGRA4I_k9Svp7klqRfF4qkg2-QfoiDz2ozRIREM6GrMjQ-dFOalIMCoBFjaPDkFbhfNoubSVJ5PAcO8_AO5fqo1tsPNmQmRyQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAxfHj2USwssLIUg4bFBGBEEY0eIjTeIB1EwSK085X5SGrJAGIKs1EaFLzdtl9XPefkCDrmHFWuH4C3fiaAG9A0k82fU9oqlSLIa3GBFJMlTSssWiLrOjk-IDHQ3nQR_GdLmopjnsrGZ3N6IMzZU282yK9edc1gNJChVc__IlJ-bpfk4hPS6jd2Yxtn7Kmmw_AGppUmWU39Z1wP2tVyJfkrPAXcFWIc45N1G60RuQQCa2OD0mZnjZ9TxXENkxtNejhH6akSAE_3e2U6Bm78rRdb_h2SGiqkrzNkhwG1p7zFdaF78vq0UFnUM0xOxXyimCgZwP_q1SZpqFblARWzURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=qiyR4XVnJjbeIlYPaCHHFWtXSo1t5DbvhIE8uQwW4KhKNEg-lae3K5ZA2tW7CE669bBQJ6it9p3b5lwV8Ltj2IP_Zu9FFupU0Jh26sK5q_ax-r36glB4E9KYZ8pfCaa1NW1MAoOPkjpEYxUfodV74LOptMGs3xgcrxfwVbkIymCd7NiskKBmpAG3d1e2av7l2sibo0XTF-MUUxKGnWqmI4y0eJBhUWTkpvSUdBDNrB0_PkAjpJr7mnfhP-C8WzZIrdGO94xLAtoSVBZ0WxGVWVk7fJVqfzlY36cve1nzy15Fb_pgNUxt75UEPY9iLyMThL1ZHN9M_lMJ9pPPRwO4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=qiyR4XVnJjbeIlYPaCHHFWtXSo1t5DbvhIE8uQwW4KhKNEg-lae3K5ZA2tW7CE669bBQJ6it9p3b5lwV8Ltj2IP_Zu9FFupU0Jh26sK5q_ax-r36glB4E9KYZ8pfCaa1NW1MAoOPkjpEYxUfodV74LOptMGs3xgcrxfwVbkIymCd7NiskKBmpAG3d1e2av7l2sibo0XTF-MUUxKGnWqmI4y0eJBhUWTkpvSUdBDNrB0_PkAjpJr7mnfhP-C8WzZIrdGO94xLAtoSVBZ0WxGVWVk7fJVqfzlY36cve1nzy15Fb_pgNUxt75UEPY9iLyMThL1ZHN9M_lMJ9pPPRwO4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=YlwB_X0OeAnPKsaeEocPyV-KpuVubMLu23ALg4gLaPG5VPDKfxY12fIJz0rNW6DuBytXXtlrESQDO9oZ91D2btWhe_GLve9Pj0S0zZfPwvoJtGXDd5geuyko_Ng2ZyexRsJCto-T1-jNK4MlEJAsvfNwgEGONSuuKNUOEu_E9ZS7Q7sUPfuspWloaGH7DcazaqE4d6UNRK9m-_-kvdjZHdUDPpYxs4CTYb9yic3VgUizeR0T7deR2X3kUcNAQidargDVpa7Du-DWhzOcBi7DEB_8bi9gbAWbk4KDc1vZ2J9K1Zu8_DH0gALthN8CdRV-eWCy1DwNdGpykFEWwpHH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=YlwB_X0OeAnPKsaeEocPyV-KpuVubMLu23ALg4gLaPG5VPDKfxY12fIJz0rNW6DuBytXXtlrESQDO9oZ91D2btWhe_GLve9Pj0S0zZfPwvoJtGXDd5geuyko_Ng2ZyexRsJCto-T1-jNK4MlEJAsvfNwgEGONSuuKNUOEu_E9ZS7Q7sUPfuspWloaGH7DcazaqE4d6UNRK9m-_-kvdjZHdUDPpYxs4CTYb9yic3VgUizeR0T7deR2X3kUcNAQidargDVpa7Du-DWhzOcBi7DEB_8bi9gbAWbk4KDc1vZ2J9K1Zu8_DH0gALthN8CdRV-eWCy1DwNdGpykFEWwpHH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auaJ3VmpNZZK-Rh5n3x55oX7KOQdHgPhu1s5uFMBEQE9SO8_dqiZfmsW_dy3GHHYTtLzR9tpd0Yf4E2lPUtjnyEoKn8bbshV9XvE7RbIGmJd15uO_rDakjUwU12wRku0rZzsev2sgVUvDpGkHqpyu4mRSVcfccRMKhEkU1BMkGt4YFNNN7osXpzuLwlocuoKn8x6xgmQj5xEPdkCwoJdfx0C1QW0GBDKTYsAYdLFtzyA9MiXsXxSCNyzRentdptW63uZhRdRoCfPm3S03JUQVv_hmFm_d_Rc94aOW6Axb0HdlH9W-7aLAufWSESJn_esuTWExtwEopvVglp-j5WTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=aMVSF08zOek89nK5F0gwR8wuOaKwtyTjKlt9yAP0i5Zpv-2NEgvIEKad6MkoXKZXgBWZIgWnUDfNN2_ix_VzWlq6rK3bzPPnzdKm06bRqUxKGQeJJzZ4kJkr6yvDJI69PVHRC4Yq8VpAX4iNRoKCSBVpoRflEQUbFo7bfmxTK-QfPIGFrQ3a3WNTmxyXTP9Zef9VGR6MTP4CBH6vL1jE4Vp0yPjQ9btHNFgaF7Wx2mCyUkX9yUVsP4bH_Ye4dzVjt8V8KC5rbWSHI1J_klLdbrhmm4QmmoQSA3oecIEL0mBBkFhS0o7is3EW6ze-242Ujq4TfbLcG3BC9Vc6yf1XxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=aMVSF08zOek89nK5F0gwR8wuOaKwtyTjKlt9yAP0i5Zpv-2NEgvIEKad6MkoXKZXgBWZIgWnUDfNN2_ix_VzWlq6rK3bzPPnzdKm06bRqUxKGQeJJzZ4kJkr6yvDJI69PVHRC4Yq8VpAX4iNRoKCSBVpoRflEQUbFo7bfmxTK-QfPIGFrQ3a3WNTmxyXTP9Zef9VGR6MTP4CBH6vL1jE4Vp0yPjQ9btHNFgaF7Wx2mCyUkX9yUVsP4bH_Ye4dzVjt8V8KC5rbWSHI1J_klLdbrhmm4QmmoQSA3oecIEL0mBBkFhS0o7is3EW6ze-242Ujq4TfbLcG3BC9Vc6yf1XxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewjVqqrttiaPGYrSlmDnKtG1AlPmaYGMk7xxwABJ8VfWnlqoz4-RXwSqJL9v0C-jDvO4_0IIF7WyJ7fHRO_En7oHyAsLkPu61ojZKXHOOXBP5SBRHp4Fu59mKd8Pv8_-0G2DwgLwRVoBh-vfXTnrgdkS3X6lfw4IWgfv20utWUJcqOTrdkSBi03jPm71qZT45G4zAr1ywnbxcDOTgFnAF6NFiohrnevPXQ-DeA18CbDtQNprCX-KWzqAcR3yl7b6QMpwAvSw1V2DhWZIcC1EZeIu5l2uOsFwKIyn4l5gHFObWpCO38EHmwaQZvwxB2dndCF9T2_ffUq29WEuiEq-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=epxx4mpa2ipCLizp3CtTyPbLoA6cqcoWr7lIcTpD5-IVU4qk_KBv_FQaTt9myqSis0TPAmHL3XnX6qDHBVsjO8bVQKcIr4YGhPO_SJjRRdoXzhyUBYflAemzjFwKK4udmn-prJYOnovjpvh8ilnP3gyG1VH70UVXn3ckKsekqzjlghy_u8a2093uK8K8IKETmByh7uIuG141XTRyebXZ85BhRQ3-sB2QqiC9jPec3YWlva40b385MFoNSc8IBnFsPyXHvjtttHFeboO7yHeLwydaHm7f_YFr-h2im5wLSw_RvE2YxnQpQ6LBrng8nqWnnCTr4P6dssqkRu67jbebmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=epxx4mpa2ipCLizp3CtTyPbLoA6cqcoWr7lIcTpD5-IVU4qk_KBv_FQaTt9myqSis0TPAmHL3XnX6qDHBVsjO8bVQKcIr4YGhPO_SJjRRdoXzhyUBYflAemzjFwKK4udmn-prJYOnovjpvh8ilnP3gyG1VH70UVXn3ckKsekqzjlghy_u8a2093uK8K8IKETmByh7uIuG141XTRyebXZ85BhRQ3-sB2QqiC9jPec3YWlva40b385MFoNSc8IBnFsPyXHvjtttHFeboO7yHeLwydaHm7f_YFr-h2im5wLSw_RvE2YxnQpQ6LBrng8nqWnnCTr4P6dssqkRu67jbebmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glOtsCUkqgFPlqJrMk89C5Ar-DRgIkecQ26zJg5ElmO2RBXF5nj4xonx8n0fYuFqfOR-AReIA9dkZcdPTqH859NNrQMgVXhqPeUx7gb4WeR1GZarvyQPQ51J_VYBKVKuX5KZ83vMAzTkPTLbZanY6ePV4dgVZQpHK10keTraEmrXqqM6HMye3HodAaehWqzqwubMNEIhRML-lblfY79sH-E7k5_7Rbfys2BwsjCw-e2lypWHTIdrFF-M10heoXa_TNR4TM8QSRjHMPslEZpuH7FZwhXs5fEpamV2hbaTxZ8vwztbFnHABVq6KCkUaa2fTcO7Xv2-FTnzrGet9xyh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=U8TQXnfgynsnT3D1Ge5D1sw7NbRmpXvD2-VASlHOsfn94Z0FAd9-oZowB3mj3jS-woep9Ar4CNAlHpyz4nlkIFvtWXh9zUsLHVcsF1C5MjV-ea4wIFOCKH2T-E5tGW2fliNn6pqkRdhb4SlD4zv5RiuhC_bDzooXBu6rpzVi1uHERftckNbrgYUggc-VefZIN0c905bMZIVa8fNN2tIa1T9Fu-gfflG5OekV7gMKAe5DHhpDNkyGI9WxslVOy9kMTxdOceloohrjbUUHShaRSjhCUjKnnCgZKkoCLCu-eQb-YV4R5BbSVeuM9xZlcMH6JQNyNVJezSAF0up42oBk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=U8TQXnfgynsnT3D1Ge5D1sw7NbRmpXvD2-VASlHOsfn94Z0FAd9-oZowB3mj3jS-woep9Ar4CNAlHpyz4nlkIFvtWXh9zUsLHVcsF1C5MjV-ea4wIFOCKH2T-E5tGW2fliNn6pqkRdhb4SlD4zv5RiuhC_bDzooXBu6rpzVi1uHERftckNbrgYUggc-VefZIN0c905bMZIVa8fNN2tIa1T9Fu-gfflG5OekV7gMKAe5DHhpDNkyGI9WxslVOy9kMTxdOceloohrjbUUHShaRSjhCUjKnnCgZKkoCLCu-eQb-YV4R5BbSVeuM9xZlcMH6JQNyNVJezSAF0up42oBk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Rmy85UhcNe61NPKhKyWYGZvDxSurZ9SamZ3JG6RhUzVQYN0ws3GSHXEXB6J9Kxzw1uLvBbZytibANr5ShTTrLlj4EU2chXJ5fRj9bNhjTnxEa-ivq1DYmXxJ1Ztfs9ijvMuJGbTAecHtWVszqGkM6Y-Jc8_YZeFpiXC-lePFPltIyunSx918ujIbCGmyfRKpPbgjBJ6G_tSsD7bubCkKgaBU3dZm63KDye6xtdh1tj4-NB_9VraJQnQeTtHD5StSkjmxRynvZ151PVIKjtdURQwdnM_uOExxfBanKbYIVU59vIBz1XR7zerba_ryXplDmiddc8FQf_9riLx2i_XVMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Rmy85UhcNe61NPKhKyWYGZvDxSurZ9SamZ3JG6RhUzVQYN0ws3GSHXEXB6J9Kxzw1uLvBbZytibANr5ShTTrLlj4EU2chXJ5fRj9bNhjTnxEa-ivq1DYmXxJ1Ztfs9ijvMuJGbTAecHtWVszqGkM6Y-Jc8_YZeFpiXC-lePFPltIyunSx918ujIbCGmyfRKpPbgjBJ6G_tSsD7bubCkKgaBU3dZm63KDye6xtdh1tj4-NB_9VraJQnQeTtHD5StSkjmxRynvZ151PVIKjtdURQwdnM_uOExxfBanKbYIVU59vIBz1XR7zerba_ryXplDmiddc8FQf_9riLx2i_XVMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=fL2JG8qpUMrA53Uyago_f65Am_O0KDNMVlcd_12iBxjOyoySdKG4Ty_t816twapv5b-1fXyRN0pQDBA2TK18oKM6EzEhfI0dwIARpshow4b7mdjmOYbDXU_IPUSl-zo5-LBm0WCW_Gv69uJ07WT7MeghLkmuCNP-aJWJ8aJU1Zx3NRzICoYXwfcEDvBUyDNquUMRdXxN_Phn92bPFeRtTzpYhYZtVCAZwUHzbjQ666JIpMNd5E95BXDb2BdfZzdOYtgdYI26Kw_JyMqvYZp5rnf-05e1i2BdRRS-Ij7_eaXIKCteqvOr4QCZadm126wJfLCtXMCyu-KtVxhkwCqg7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=fL2JG8qpUMrA53Uyago_f65Am_O0KDNMVlcd_12iBxjOyoySdKG4Ty_t816twapv5b-1fXyRN0pQDBA2TK18oKM6EzEhfI0dwIARpshow4b7mdjmOYbDXU_IPUSl-zo5-LBm0WCW_Gv69uJ07WT7MeghLkmuCNP-aJWJ8aJU1Zx3NRzICoYXwfcEDvBUyDNquUMRdXxN_Phn92bPFeRtTzpYhYZtVCAZwUHzbjQ666JIpMNd5E95BXDb2BdfZzdOYtgdYI26Kw_JyMqvYZp5rnf-05e1i2BdRRS-Ij7_eaXIKCteqvOr4QCZadm126wJfLCtXMCyu-KtVxhkwCqg7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnVCd5u4FVORFbHNXUftBYp0EdKV1LGaxLLZJkmoga2S6WwUVd8oWF0Gq1uTuxTlFJ7_HkxhWujY08UZAfG1lBQlDYxvCz793ipyncusqhckI6Nrj8eqAElpO0wEWkxYHZHIdjXd_eXpMWTckh4rBgFrHzoqp4Ys3O3Zg7-30lVT2A58wI9vs1cGodYifmMgMORYzD7AtNdEuMg7JE8IOaQ-Tt0ocdMt8A-Tw5l7UJENx8Nr0LF0tPOUYwePeVeP6XLQ_-gWFAeSzPGNL7zz17uZCdi8HJwPpR-q5T1tpTWmmODCLjLfR8yBLlbsp3C8PBLPFt4XUDSp3zysgVR9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukFplb83FqqcQusHQxFoyzA2yBv_IFiqA5CsXVcLAux6hUmwGrcR129iBdUnmKSc8DPAb7TTxAHtyyS3aQPv2lV3hUEL6JwIKDmhgrIGNHKvBKE856IFfTHZi5W3PBsuxP1XovKmyQHbT8hHWg2oanClsALdeZIkoNOCfpPwzUGQb5-T8X3uPHl40xNbkx_og-dZlPBnEmBDQLaq3M3VAwkSS1kA__w0U__34L1VaLTN1StLqzHjoaC9N4zn4P3Ka2MZKA8bkX04uAq5k4-OEXBqdMu2QuxEED7Jd498E6-abBgQIroafnpTuOB5P6ril9-Ye1oZBd9SZsirEe101w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l12X0o27wuhWvPYCqEm10gpo71V2Sn8vfr6RZsfyxIRN0U9_s84XkHCBDgePAKzDlH-V_NR0dS-1iy3TBhtcVAi5csjsPM2Dr_cGgbult0GhRadqlg_uZ_DX8UXr_3JrudROiLOiOx8WankM7HlSaSyXHwsnkZeYR1NtkZrFoT7EZGFI-Eam7nUx7AmTvYYVZVRmY2eQOcXFNblDXTrsJ2jGsmozPa2fMfBCBOLAMY06iD5uVUbacr597Yn4be-9sZLVDdlAbUPNIJ1oiGLwNTjfSXbVpjKCtP3_H_5TpexbAsK4Mp-xAeT5HMUP0PWb2dPjfJGt6NzBj1QZM8jRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Ze2NDwvhG2zlqLcC7-K_lgYA__FSgIQ7rewUKv62Br8TBn4TiGhUiUEq0UqzCVD-keoYBYCqh2UApx37mvjTwu-p8IjGzCyq0ofmn3S2BIqcQ-B0SSrOLzuc9-Dm8FBro5qk28sFPG7hpceBJoWMVBJjtvpUldP7EUmeA9RRHIPhMayGWPdfcIwzHwJIVWFvIcGaGB0pHt1ouzYGrkrP-gxFflma7QTFT_WR9PxKD-vaTNncOYvZ-kPVkQjUM8tlv1SCTWAGzY8zuNSbvdMMYenexhzR9xlnn1qmwrd2DLSSSQx8rzNkNBpxbHORIRAerd-wrbHwdq9XsjxWgIuZOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Ze2NDwvhG2zlqLcC7-K_lgYA__FSgIQ7rewUKv62Br8TBn4TiGhUiUEq0UqzCVD-keoYBYCqh2UApx37mvjTwu-p8IjGzCyq0ofmn3S2BIqcQ-B0SSrOLzuc9-Dm8FBro5qk28sFPG7hpceBJoWMVBJjtvpUldP7EUmeA9RRHIPhMayGWPdfcIwzHwJIVWFvIcGaGB0pHt1ouzYGrkrP-gxFflma7QTFT_WR9PxKD-vaTNncOYvZ-kPVkQjUM8tlv1SCTWAGzY8zuNSbvdMMYenexhzR9xlnn1qmwrd2DLSSSQx8rzNkNBpxbHORIRAerd-wrbHwdq9XsjxWgIuZOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3bwmQDJNawvn0zt3-H7xzaMbZkDMJ27UaWJiVMHmtyOjvhFRd30xVbC_qq8S-cN55LMd8gba9xflQKKO5uH9Bd9dNvXTMs5m8QiaUOemZGfPBYChn84fh5C-MGkqynGY-YsJJ2-uBXK-aGygTJKX-NFZg2J3mJda8Zl98SZvSXdZWG-5kmDqnWdvXLIi7I0guyaoydDYvF1cjGTF_ThTwQ9NXC-NjKLFgE4sdZkYmPbOaJ4qCNflPe6JHL4ndvQqQkBSagvDg-MWym9AgP1bo1lJmv5kYLQE_0gwe2m0ck2mm6TCI5d0aXZFbqMqhCJjHO5Jbz5jWguBO2jbLPyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=gtNMXuTv6TEI_Jcy2_9VPV3FlJb5kv1FwidjQ13SLnIt4auyYISJ0vRuZ9IyfQe3Ya8gc1cRSSnPNAN8H6GM099k-esz-3jw7IIJcoSF0ctzMogwyyVDVAu3_MSNlMH39zQ9cEGcmK2w-5Mxpu7cx3-kpLX2MzjLcfOoz0-kfHRQAotnGZHsGcLsSa4qFRUfgxOwOaQe9sxsBPenv2eStnKRQFG5xu4oD74qtCpuy6leYYtQ1NFKBZrPEZEr85M5VP3V4VA6fFflSiJ3WaRgHhqrn_S9He04YMK7nIgudsH5VtOkj4rpLy4nWRR-r5wt_0i7mL-TBx9ztqvk8CtozA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=gtNMXuTv6TEI_Jcy2_9VPV3FlJb5kv1FwidjQ13SLnIt4auyYISJ0vRuZ9IyfQe3Ya8gc1cRSSnPNAN8H6GM099k-esz-3jw7IIJcoSF0ctzMogwyyVDVAu3_MSNlMH39zQ9cEGcmK2w-5Mxpu7cx3-kpLX2MzjLcfOoz0-kfHRQAotnGZHsGcLsSa4qFRUfgxOwOaQe9sxsBPenv2eStnKRQFG5xu4oD74qtCpuy6leYYtQ1NFKBZrPEZEr85M5VP3V4VA6fFflSiJ3WaRgHhqrn_S9He04YMK7nIgudsH5VtOkj4rpLy4nWRR-r5wt_0i7mL-TBx9ztqvk8CtozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6xI6pbMX61P-mDclCyZQaQwnnM9KHMfeokwXXHh2yfzA-TWF7Fzkafa0bsH6BTvIx0I0B4uPxlgEOfAO6l44Mb3k6ZdBbjRhCJH1czNPv5RkEdEY9r5jdicTb6AcQa2P5ZOKCBSfL1jRd-ZIujo6Sra1iMz6RhWy3op6ZIs_nABLPdo7pL3dftSHbi6CneKIb-mpwO6Xna8n6d8yueH8w6-M9dB_t1ntU6K0nUy4xQe0OfRpzmb3iyddcZE-_rpCWah4Q5gLgothY2Xjxm9B11LAsnSR6qLaRY_I3uzbCLHvbZAt5Z6JrvC4pQSZZyB7EsuiQHMdp2yNlm01uRyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=YfkyP28sfZ5OkS6V2VHukyR440lXv9lsXYlSuogh-qxhQ9j3P_eafWB59ZIhuwHGwVH6SWLkRFVWEwpEKo2jw-u2vhbNHbAHxLDaBHgB_VTCH8NTck3q5y_pFpozAol6HdjTGDp6r0M6LRcmQRqNQvaXiBYUVQIKWkCUe4BbjBk9gpNVm_Ecp39MT_SsKANz_nR0AjyNhHwJ4jNPi1FU25ry19oh3j435k48kLmc1CaE2RM6h34hapKIwywCdJcrO7GM2LhSir7dQhMBzi88hYkVhiQ0TmD8M3ISUs-MNS9rTAcH2xmI9DkqMXMpxBrY_n8vKbWUZZJgwEwzfQgA5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=YfkyP28sfZ5OkS6V2VHukyR440lXv9lsXYlSuogh-qxhQ9j3P_eafWB59ZIhuwHGwVH6SWLkRFVWEwpEKo2jw-u2vhbNHbAHxLDaBHgB_VTCH8NTck3q5y_pFpozAol6HdjTGDp6r0M6LRcmQRqNQvaXiBYUVQIKWkCUe4BbjBk9gpNVm_Ecp39MT_SsKANz_nR0AjyNhHwJ4jNPi1FU25ry19oh3j435k48kLmc1CaE2RM6h34hapKIwywCdJcrO7GM2LhSir7dQhMBzi88hYkVhiQ0TmD8M3ISUs-MNS9rTAcH2xmI9DkqMXMpxBrY_n8vKbWUZZJgwEwzfQgA5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9QoepBp27H42bB5BTJSXZ-XFF7FvYk3-fJjSrMTsgw4f9rMNga0C3CeaSCZgyJaYOUZWQfEtsNWqMoDGzigPSWcVExyfLuE-Ao6O8dlANhysr2xkUjGdEe32Hl13IazbNsYuFAfw-jKWTXvjGieBCB7JiF7tkiIYnSHM5abMUK2Y0hSihXMMrZe2BbgZb4jrGVRncMbJNUQlYSztvjXs7JBBxyXDUeKKQJZ_CTg2iKmfGoLrymSfL_MfvOGiqVkX8CFaul3u-jbN22Q2j6uEbk652Ei22nR_8UqW1OD9qLyZhBp884BR2Qm-Y-d4rMBrB-_6VIT3-x_PtX3jRA1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhguoC_iWXCQ_l9fmkoFumk_x-jBToMikz_yrjwpx9nnQ4AG8KcLqotQJA9TGSJdn9vWhyHPQTyTnFY6UC0fjHfRpb0f3Um3zkVvGC9NfBi4RyKqX8OK8jDIOfmqslJpSLOlFaHFH69Nk4p54laz8hNoi2K0_SoelviPKov0ixa8KHJc5GyvNjKYbDKPKF_kiQQ-JUQ1nztqJ0cM7sLGUbp92SSHlbQafxVfd7ZgpuO7UEjXuou1aYCoeLKqh_pJ4OJa-Wxo-NvxUixkG3olsvErtBGlbWcopnljpBRuHoY20WxbFYwk2XDzQUU5VEt-Lc9dFKkmJnheWPmOIUwtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6N1rO1aQZT6GoSya-PWUUo--4IyIWISMpv6KsVLs66xbDSjJMUm-QjD9smrYFUvZBUzYtk0K5uUi_kckYXTb8nONrhamoYxY0UcRC3Db_G5XYQkoIAbRDImmAJXltBZ6HCfeF27rC0v33DEuUIOaUvr5HNXHQDlnw5NMQtvJEHFP2l7xiIPC6AmU8eiG56iPDIHrXgzAJnQZnFANYbyGJ_WB-SWTEudOOsCeT0coWgs9aNCW6JXOQJTcFGAUTttR-MBD8XqhnP2Q41TtmxprGbSfAMVkIiOYCVuTxkG3roR6YvyWRx1T9YsEIIDtmA6KCo1aCkYkR2i91V-fVdJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
