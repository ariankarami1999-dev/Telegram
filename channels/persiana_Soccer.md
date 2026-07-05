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
<img src="https://cdn4.telesco.pe/file/WBzt2zUGlmcITvCdpAhzq3bbONodZEvLiZioWT2xcJ_ftTkxDoiMmeSEPr1iLurQyq_kRuoIG37squRxOUfB2BB4zKcVYX5VQWDjO4UixvsN6ZvJAVOia0fDVx6rWCBkifsF3L1kTVKX2GIis7oviniXTDtzy8WolvHF_yyR9m1KENEHmi3EqXyCtDNLnXH-87ZgERrdrdhaVwzYkSQysNYFtF0xDDsedcXh4kYfL-PCMBIZyerMbDcaeprbOpYDVs4X74CGAsDxz3nYQnDHBaxZYo42MJbGZNleXUVhUx8dax7VYNULG22ips6zc7tPVbaCqMjTMafkDZTMfnevyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 396K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 20:27:24</div>
<hr>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=HQMfzxYTQ2XPwvBbbzS804laVzynC2GKxHYbYZkDDduLfFo92cejAhy4nw3o0d6upGkvYkElxuRaYbl47NQndd9K0-gULSyVpy_2lacvNvBifAZ7SyBjZ_0zo1GHUe6SF2s3TnRUMR1pli7-c0qCmdEI2-rqY5zS2s5YVLcsvpMhXIOdiq6fuam-2LUEQMsppFDhF6jZ8wdM1mQEaRiZhp8ND1oKF3hUvtJHQ5f5yMN3meFm4fdRjD_3wlhEWzIiBAe0XjLwuOyuj3msjXGF1JaLHhMkRVrVQ8L7NKHQB8bGYx3hspF73EDuI6DN48F3Qe4UfFB_012olkbjsz_P2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=HQMfzxYTQ2XPwvBbbzS804laVzynC2GKxHYbYZkDDduLfFo92cejAhy4nw3o0d6upGkvYkElxuRaYbl47NQndd9K0-gULSyVpy_2lacvNvBifAZ7SyBjZ_0zo1GHUe6SF2s3TnRUMR1pli7-c0qCmdEI2-rqY5zS2s5YVLcsvpMhXIOdiq6fuam-2LUEQMsppFDhF6jZ8wdM1mQEaRiZhp8ND1oKF3hUvtJHQ5f5yMN3meFm4fdRjD_3wlhEWzIiBAe0XjLwuOyuj3msjXGF1JaLHhMkRVrVQ8L7NKHQB8bGYx3hspF73EDuI6DN48F3Qe4UfFB_012olkbjsz_P2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3BCl6ykH5YGCgxMEh_4K0TRd171MUdj0E5Nl3CivPrkb2CcZMCdV7dG-Jn1ekSj4ciFQn1xA1ZIVyNlv0aiDwXWIW71ByK7H0L6z5RTluj7uQ3ygmcBqg2vrvFs3T7y6jMXLY4pJv50N_fas2PSRrj1mqa9TM7xVimNNoSFB2piEuhfFaTEWGog5SRxZhWxEezfFrIc-l0CvWtIktU9QBC7p_tR43OitQMoRYXWOhLF_Og7UIul-6hbKLz9lf7saq4bIDnfx_BzItMh0L3s3Rs0xttLV2_759qZKHEW9n2IJOtRsPevTiJOppKnZks4tNRSKRtnRP36bHUjDLuqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWZn5cqNnz4PNhBh86r-u_sDa5cLG_dfbXVpnifSq--3M9SdgUh8nUGdXeursNUFt3JNVq-D1HkupZSIV4-Z0zAYuu2A1i2uxRpWJDUDW0Qi34Jc7iMN007uF-PK1v5WU6GBnG_x4s0CQTinWdfdxUe23NfxE-8fqmUNy5ofI0MQOmq3KTZ4uHZykDweKFCO9tIJXfLeqgSWiOGYaxzK55I4igj764hta7HJ43Qt6XerCwYf3iIC8V2yjK0YbKxFMGzNhx_6EAD2FeuLkVqAjnE3oNyFZNaBOM4QT3YY2EG1vQobZWz5IDGinkx2UiEHXDeMGwgtul1evWfqytJp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4aktiPfGYEJqqqF2zt0OWgDZiblXQ74KbFESfuNmw9oCMbEV8fYssf9cq7ABpQ5ykvFSqfHThuNeUru4xpa1WQUxYGsqm95gmuvRJR5p0FroDmrhWtatHTjVJePehiBcEhydvo2Uif3Lq3mp7RhGEDc9MMokeQIaKadNIo6MvPYHIlBks3ZH1R_KHlHiK5lKd8Ul0uimPuDga3YTZI-4e6gQcmkNFIs32_vdLPBXrQ0SctEWbYilGlV2DpYv53dnEP39Yc20ufD-6VGhyXkgFKG--bzQFCbJXPQ9fgplr3NuW4MRK3OUGjORH6Ye2LzjKBLoTYUTpKxn3wSibFkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0V-iDXcbPe5_sifhEYA2zmQIg14ir4cdxjhdsadIilaWaq0JhomwLeGeVuRG4vH1KU6stPkXfg7lZNhg376obs6SHl8kWmYmW8W_PoXmkhDD5HXzFB8hVLTSCYBkK8cv9mBrovc3RJodLG7fsfreh5iUH-NaW5SyyXP4Sxx-x7Ml1GWNuEfwWakN6tq30sQs6pHlbggfSv0tB15xgzFNQb0PPnO8yLzTHhqd53H-eSN5a2CMYG1SEv9Wc9Y-TUxtjfJCOhyb6b3Zww4gRAXRzkLrKIqd9XS8G8V9KZv72hN3zlq_nAooFqO-KEOb9trPHvnImgZKbxYz-hRvAaesQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇳🇴
🗓️
۱۴ تیر
⏰
۲۳:۳۰
برزیل
🆚
نروژ
📌
صعود برزیل یا شگفتی نروژ؟
⚽
🔥
پرافتخارترین تیم تاریخ جام جهانی برای ادامه مسیر قهرمانی به میدان می‌آید، اما نروژِ آماده رویای حذف یکی از بزرگ‌ترین مدعیان را در سر دارد.
👀
⚡️
برزیل صعود می‌کند یا نروژ تاریخ‌سازی خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/25017" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7yzuM_Vq_11Gi2HwTup0obqume3FrTnnRo2oZNFk3o4oaI88-xF6xGAiNafQFsr43wsbQlaZubkyz1buQ22q1E3ycbJMzP58WVvE-kNmB1osKiZbKqN7Rmh06DKQSLYSozvBqGbg4MLNdR7eDztQa1WIpjq1nmhzWftDRzLnI1iCvzayMZMxykQhgzx7mcqbtwcdsRoVvsyEqBBzevgo1twpN5YNyZf6iY8TyoOocsVGIOWsJhQN7EQUOAoccX9YzIFGRNJCdLePsHX8xc6Jkc439YJon_uO_O7lwJ08w6e3gOs6_79r6kco5FJVFdEEkEAdd4nr03Dq1AgHky-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRizUKVIekKdzQ5XNQdGnahA2_5udmQ4AT8JPuzHWKtUQl4FcDQw_4DnKfutsXiwwyCBWCrftOYcpVlTSw0q9m0DhZEN4ZCwjbKBBky2WAzjUF_NT6kSuERWwIseyJTZReTTKntgiesZLjBR812uKm3V49_wenCzlWszyGewPixGVsQtkoOhySCwkv1OV8tZ32R4aDW15SWNJ-FMG9qjvZByQq1saLw8HaW2mRn9mGYvPNzLh8BnUD1qhPUeg2f9ZmCJ9sXsz0pWHojjpufI0BKIKOdoR2oQlgKAdL50wrr-MDwljfmf88-GKZuOPrnCJNY97ZELFyS6ImvGP3Qstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUzfQZVh9DeHt4Zqq41m21n9XKP4o27yXG2jqw6H5li6UNkkWODjxUg-qEGM4gFxKKoHHhEER5N_XrtnpiKtlaZkM_1HNyZcEIJ8HyQd5VlnUwq7XGGjO44XoTB2F_-6BxPoDgKrFc4tuAtHD0D955D7BeMV5lWL38P3a_ZRGJj-buD99eYLYEXbcsZqZOUt7Yw6QpZ2AgTMHJ391bQdPBefaC78te0cX_13SCP7sXW1C0y1-Q-93pPeCceFUiEgx2aMJks6ivSHTvzu8Qtxs4rIVJc8RVdMO78-kSRAYzKpoBKikjl0_or4s00PxEVC0g_UHQjGICR09wKN1P0D-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQEaVbdm8aShl7X1P06dXha9WUZ1p_pDhFu5HZwVMWmvgPJim4jT2CqMVrpM5svmLacD7v3FthiotDs2sYjhVeYAzJHelBRNTyDdCs4tB9DzuD4iOYOj5HwfxS3tUSNzAyGJREwsaoQdgsin-AzS_5Ay3MopQ4chXTqLtOxf9A75zToaoaOCpjsqWZIalNOQq33G1-7dstPalBa8swS8G62fFma_t2MGESxqDzQp9NGnv4GeF2x23fgF38M4mJKp2xtCR4Efvnhy3s99KovjapCcDUj61R-FI-c0tu6WHvKL2l_FZ1EVdD0D0wMyTAEgT0WsoK1aTgqQDERVE3agkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZezubLZX1YI8vZR1YoCpCdrG0S6XCF85YnQUpM7dGvyFdbBZRwjViR5f6JIDaYN-jqqy64cMY-KBGYLl76nOC4olzxW2YvS-Q5XaYzvrG1aopqdgnMdt4T6vaCQ4nrmqF-ytFTWdGclde7uyKY6ODIvtLf2S0I2Go7KTow5BaENfV8SzizTupyNMmK9iC-9lk4tj9_voL-T_RTYiX2txxp1fPryD77NzOBBdLcvQnsV0mBXA0whSXHsf66nsMgWHDqf9_SVjwVSvCHyWgi3ebjuPolWXNqZtrvBVSNRJgR-9fWDB_xvvj7eYBkp5_jkKq6paLS6IxwOKuGt5qfz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_EqWEh_JmLDbzE64tkTOXEKXnUnkrw0xD6dPvOXxLtQ5OiYnMiEuwAGoN9_09G5ASyXZx5PCuPXLZJdoFImvwYnY7WA1WVi1nib0WAujBXmKpwRRtxasdAcSj-v4gt1SNmjHzDF57bFgW5UZzr9VwoiIvYnbC0ivxog53MRjwV2WRAeSI5qaD2MTcUUSijn3iQL87-sX-3jcYISQXagVMMv3Fphjsm8vYV5_dX2DTSAvOD25ErYwbmROdIBwTVm8rsPlXT-JZAqX93QaXT5dZZUcTkTC0DFcw5AzGOz-HtKwxW7onFOCEY6izxFDT_-GwDq60WPqHVl7OAvwZBFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=kujPf6jTiDH7rz2ddLxAWzj9QnP_PYW5WvaMZspq23VQw8ps5eUqhA2huZ9qD_bzzPc48GUALZ3X0ZAFp08yoZEYNhggXl4JMcP4IYUUcTxsxRmbkcxe3WhBF3GW5OlUjwWo8ET19AdEmVSXfhxoyrQQr9qxHCb1Zc6xvCxlexFi6ZwM5gK6sTMdOTcaINfmTsMt-kNa0FWyBxUvjxtL1wS_WNmbOVFXP7_hZKq0vjiJ4VngmLsE8-Ul_mJa9U1NqIhEwXPGotJiYs739KcsTLGsOr0BIvHGD1VU_thoft2twPhlxY71AW36fzMK_1ryvqJLK5RHeeWueNrTdrDppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=kujPf6jTiDH7rz2ddLxAWzj9QnP_PYW5WvaMZspq23VQw8ps5eUqhA2huZ9qD_bzzPc48GUALZ3X0ZAFp08yoZEYNhggXl4JMcP4IYUUcTxsxRmbkcxe3WhBF3GW5OlUjwWo8ET19AdEmVSXfhxoyrQQr9qxHCb1Zc6xvCxlexFi6ZwM5gK6sTMdOTcaINfmTsMt-kNa0FWyBxUvjxtL1wS_WNmbOVFXP7_hZKq0vjiJ4VngmLsE8-Ul_mJa9U1NqIhEwXPGotJiYs739KcsTLGsOr0BIvHGD1VU_thoft2twPhlxY71AW36fzMK_1ryvqJLK5RHeeWueNrTdrDppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8JtSqga4xT20xMPv3iCFAoXnTN8tW_8gbfr3T6udbWssmHMUws4z2GlFZs6fCEuKYuwrYEC3LESZW1bWdxF7mAGxi8_CJeuazpwQNCaJ1TMtxI3r05tcNvhHH9prEdB8YzzSc2insFM-5AV-XeAs-4_rcmaqx_ugrqwOJg0VUdFydog5hZCdkKzmYHEz6e3Bkuhvi7ae89ZMeD_ty23z-ljmuN-RM-cpmuxf6x8Gawnb8wqMpi_p6A6VcO1b59xGCzL5qJJ-jD5a1sPyxg0csJrzbLzoZgiM6ET-FLzOVlpLBXrOIJ-iz65GI22ybZI8BoaG8pSqYnlAl7zIh6V5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=kGFdw6fDmZXAcGCHqbAY6zPs_NcyziwwsxYX0YOD8DRTgPB0Ze-SNPucfGL4QTV1j_JKOSGOXuj4PxUvS1pjn9sKm5fUEf3NfZqW4fu29IrWqwkPFEptW_VzWRk19ORr2r_4LyRaHdI22AXqscVlnWJSDlo7Yjpg08jNdjaLKsyCF8YLaSFrFk7fEVgZECYIGEZ_ImL41kc8P2yRt7MO5kj-qaU11n1xN4fpx_YmAQ13CZ4RiLwDPB_30qZrAD8VZ9BNVTvqht6_QcBqz-wSWcfPKrJRFjsCcnokzbesWPXEf1JOjX91jJ2FMz90EDFEAaS0wHmqKGvG_-DQM8zOxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=kGFdw6fDmZXAcGCHqbAY6zPs_NcyziwwsxYX0YOD8DRTgPB0Ze-SNPucfGL4QTV1j_JKOSGOXuj4PxUvS1pjn9sKm5fUEf3NfZqW4fu29IrWqwkPFEptW_VzWRk19ORr2r_4LyRaHdI22AXqscVlnWJSDlo7Yjpg08jNdjaLKsyCF8YLaSFrFk7fEVgZECYIGEZ_ImL41kc8P2yRt7MO5kj-qaU11n1xN4fpx_YmAQ13CZ4RiLwDPB_30qZrAD8VZ9BNVTvqht6_QcBqz-wSWcfPKrJRFjsCcnokzbesWPXEf1JOjX91jJ2FMz90EDFEAaS0wHmqKGvG_-DQM8zOxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KswPZoadMJUOI7vjpvSJ7s-pklcV2ckr6CiHbYWkUJbyu3rhrzT15T03NjM_f_whAjBq7HARHSC2GPqcH3d9L1c5ULo0sxRc2lu0ZAWUnEHAjpoVK9uGBG96V11qt40ndWTtQYh-7KA0XSvexYrUANUgszlB-nvpdHBU5b797yAmnD44G6mQFmtRd2hwhDJRDcOuiF-uOh5MwzDZAHCr0wKGQ1CJpUSHR-Uu-248z2BjSvp-yqwvPyC1KB-yHc5fBKrSx7vmwoiwQSMAj7COFN42ZdWw2qriwknpNtrKkqvmFKQdsCpMNY_j0ehJ2-U27T5B5xxa28HvFbDSsStYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8CBiNpCKfiRwcFWsbl1npo1sqLMSIArPSm7VO0XCv-4CDPfx6AKXJqiljVDLjlVTIlhc819yWLsqSj6hclR3RuN8J85T9RzQg2VUXtOR15NrlwrJsFRmmJ6H5te-BKPfH7b3pAYKn8pp8c_RhoV8-bCFo-I4UgFw8obeO14DOczcm-EIL1vENm_Iy-RGc-0rulsViora2gRLbLDiPwAKLgxcYL9vyLlw1eUYAuf4Dy0tTTlGq9LJx3v6fLQbiK4bxXwrNyve-PQyAlIBZFG8W-E4uVVzNe8p0IJ5b53frCQSl-ySyUeAz8t3bnFXmdqCIJ4QSc1SEfEHVT01L-jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=MTNLyuLn5z79axGpwTySNPoOczCnsHPddoxDFsJFl4jqP606OTtnwQZjJNmvEQRM53MHrW6189lMUgjdexwLl3tn1PBENZMHaX8mjDGik9q0Bxeoy81VaGw687mw0VvIJ0Mkyq4BWVBzy20Edgz1HBMUqorsVf4QD64Mde2942U1iA0K1bIQsIIL_UHYeSH7ur6SAwasnSZ98sEkGugE7nL7ECBXtRoPlFizpk2Dp_YC5aJP3d5Wc5lhvQsK67ZjgLxZVLwzIOq0FHdjo0ymzVU26oXpbxqMMgNQwEMtJSdjVOSxCherBHrOu3x92nT5lLuUa_77bQGmG6y_1pSwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=MTNLyuLn5z79axGpwTySNPoOczCnsHPddoxDFsJFl4jqP606OTtnwQZjJNmvEQRM53MHrW6189lMUgjdexwLl3tn1PBENZMHaX8mjDGik9q0Bxeoy81VaGw687mw0VvIJ0Mkyq4BWVBzy20Edgz1HBMUqorsVf4QD64Mde2942U1iA0K1bIQsIIL_UHYeSH7ur6SAwasnSZ98sEkGugE7nL7ECBXtRoPlFizpk2Dp_YC5aJP3d5Wc5lhvQsK67ZjgLxZVLwzIOq0FHdjo0ymzVU26oXpbxqMMgNQwEMtJSdjVOSxCherBHrOu3x92nT5lLuUa_77bQGmG6y_1pSwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Ne1b6qeSd8FZ4XbVimCDZDV_JuvDrsoq8P36OOiby84apJcLQLzcfxQkzqTKBOqsl6gGEOxbvO2Y-jWTxquDOLF3hu_DJBb123XnP9ynCMOsRzRqWId_uDoj18uXlzL1iBqDVEVDFl4kte51cLUrFw8N5B7RfGnkKOiyJaM8Iwx7xSSKrDVfx-TqC7qnQiTMxIM4Fm5lzZGUXOuc7sRY6NydH3UI7EYU317tnSsnXmZXpQ5h45gGSdPjD-q87FVjEqApHpz5FoAPgUucF1vxcT81rX30objscuJcHSKdkIZ-sFBbI5ZjTcn88yWzdx6aYzRvteLNGP8IAK3i0ckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUgXgPSSLAdj9Qthp75kLfe406gd8zm8lUD0qFCLDq9NzDbihVbancAqlGceKV1QbjAWCSPLm-pWSCB982AWcj4ZtvJ5fKv2cFbj5JITXQY8hLAJIvT-tCH-sfq_iqYktgUZ_lAWkihGwzGpjwFxCDIxNxVPzpFus089sota3Vn9_tMiLNcEdZ4nMkOcKpHfxMjT9TatH5uIXKS4Sjkr1UasdfSHOAAPnnLlBLl9InmCeyQGEEWDO10K92aky9vn59Se-QsTNqe50BI13BikV1W4rtKCjeatSEnR0a1BlEMvBOvJGvrEb3rnAAS8UIzmb8myT2_R4SFDv52O5vqoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfSCZucNivh8XtU3oNP7ZtcgVm4LNBwIzBfgFTSyRIYoiYVoT3orOVTm0YLieSpW7CvcMS2rxEuNszuUFsEXH9B2_s7yoHclhPGtoT9ACLb-2o52qvwmp4oxgRUeH2LlZaVgMquQS-pvDlcjekOwHKnCzGmTHWf3emgONq0wgtBbD1Y8M3FkyeaqNYoZFDKq398ULsPiwUQHpAHX83Iw1PpWcfJp4JBYCiaZ89b1Z_LomInJnJytysvOE9T-wQ5AHFl8IVNBVDxGZhJF9jVgKDac_x1wWBBsbGqOCG-qrPEPgJ2K9Vsah-q4bxNhdGFe0Dt9MLILIYTyEE_ENMzBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrfBVJFM1OWcumRFVkccCILv3UviL1-KgiXGBzdukLM0uyjkUXiiMk8nf7bwe_vidwCPYku47JqT-OyGkARENbd1lkJvKnduEcTAoLa9aDIUQ4CF_chSCdYkcNxSs4cfy7AfjKgEY971Dgiq7CZ2aae8Y1FalFVjdXBiAzh8zp01GL4BO_tBLiDjPpNT5E7ue1KFhF1NzXaBsgk593UIqe1uAop64yZg_SBuSVKG47FmreampD1VbDlgG995no_n0xuURHMDz7VERKkKuQXCpa2in4A9RMzHlEbKYT1DKbeeggGxLU-X4-gXsIknKLJip-kz5X-j9zGXm7Rmpl_Gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsssX5qLjuVizx9YsZcjYQEtPMU-axmk7XBofX3ergAeEei0M_Mx2uVPjwUXkyLbevNjq70GyVYqakFsnTFICnvlzDa8GbZVkKMRhf-UPWQeDpQ31ABdE84B61g0swb_5dSQjtsLWx7woYve4xN4kcveNx8a4_F2RsEaVzLShUUhXXP_qso1xOs0tYRsV42aH7u-dbXuKS-imenNtJxTMxd_Nru8XyiqyHYCxUnFeaCQB7xth2ZKcSdv8fE7recNic2NoqEde4OU-gGQboIYeVmyrnuYnVgmV8zQGW2Lqqo0yR7hIy3lSnZm7mOz_EnZcmzs1wENqXFfeyB2tl9TgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkmzarUcy37GRuW-IryboSepL9zD-1MPJHcHl0cP7FYhiRRVey8Y-5VON5_pIZAU3NYETt_2gchJNLT0wpNCvvlG8RvJzFbgohCMaJnLJCEfs8CZTpiZk5Q8lSrH3PftBcZvDWCuALqtY2JacqR3EhpjZrRgOWr5obqNJTssPR2tJUGfHubMU3zKrM_E_IVpyZxbIjJIQNUGR5b4mzouTpbA_YzRFc2usbpKf2mi72rVRcKgUdAIz8fPahgjOQz6lxacRj6mJObrWL_Xifye5a8rkN8KZJPna_UnDjgx8HxEWLZQ_gRuljAoF4bmEYCUIqEbfcl98X52tPLJrkItew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS5k0IlrS_P1Tvrb7a_x8eyoAWKnoMbHBKcnu9CxTUafTOMhhm45LXH_7Fo1AiYE6dtg38lLyVM4M22WGzyc57nVliOQddpEVbqU9jMIv8u-GqL_DOltJFGt8JUMzGWJmXphOsBj1Jn1yioxwgX5kkrOl3Jh9HlGYLV0WkPKzQC4g53i0qCzcf7VRM8WXSBl2qNvMobTCgJAIyIp87LedEd-Hj4V5DsYNN6_loFWIVTkjVabojGk4OoRDLhxNYVb8pJSrOsZ8SVw-tf2LzTZiJyJHYP7lmhU0czwoLGpygIiinMnpkYqXP1QU4PFzGKtcF_gkKs-hliZq-h8OCJyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-ebxrj-W_JazLpoueCxwAony-_RPTIqCCXH2f0kvA2VLMmvK3BNU84ndKJ8XY0RWa36Hozk0jyFXtWNHe8UeJAMo0iyjXL_Ue577Fs61ilHmBlwIHN8xHbt7W-MxfIZrgMYbf47I8v7We_hWVpc5HudI8froNL7gb2c7nZvARdtBFa_Hcc5PwfVeh_FQGWrbkTEyDAkME4-ymANd8Qj9kFiSgiFZ9idIgbhWp_KMJ9l71Vm9zwlFtZbvwOFw1HMdW8BvwX7OeTTiQNYATegIPUhEzAS1IgjI_4WVHfAII9JSh5jJ9FmxYx_RC8Z0lcHR2ophGaaYWefIp1fSE48AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWTa4pK7g26Pk4KEnAX1vv4eb8CtM_MGVOYyf6e5xWc3RRH17Qzxebp1PgV-ZDUDaqAijY5hId4h0nSkYVXh5ygsHOp8BkqmkAiVIYFUe-1GOsJc_sjyC3eAK2c-pUoLvITrkSOM1DKm8B_swWQHi9vn7fXjE1Xin83kWb1IbuTQ2ESuof4ifKgnPDnc4tjhEdKOhhQBfLkbqAH0P1t-5zcP0zNfuXEkQ25973-6uiEYmIkewrXWd4pjn-a02hoXWdvx1pHH4psLKzOmDaM5KKg0JOfUFdWgBJtxarOjCpXauYF72Num9__9enaFQ2eYv1_TBOllVbVgOoTv5PytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pboEtNtmdQ4dEgkdkSKREXestPB5RFwpRKgygzfe3v_S_rqVvAv9Ph5CG-rebqqX-hUyFOxihM6A8_qlsNcWwvRYroNpjFhQygxHLiBSi_XKSd-D_H54Ji-x82x1k_ws9gPkMfFZGU7KjslV8TI6Yk4v0ttoicJH4F8UtYfKZhCX9ONd8Co9s9BIBMtw4rmFBTmvoNX8utacstyxIw92cr8hG7Zc2NJ_fbSOGixBQhrgxWelG3vuDdhpOSGL5kbM1TbyfPHXramak0T-6FNRA2ijK53KpMoOrsJ6Je1rYviIZ9shpmuuBkUZAGxkyKUAn5LPhIHoDDwdHxy47vK28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxdOSjnZzBuAYWqP5C1ZgidK_xVWwc68wgts-7zBfaUi1QpKWm9qTZ9I1my0lTo2Lvf1MMtKDLfvlaW_mgMCbAGOxPXJ6bGfrxpSRQmnFu4eIBtuk4otCS-Ci9VkUnpYTgnM8PdlAISGk8PGQ6bD7RQpu4xqfztDprrtWn9srk4cmBa7GPSKa8gwK87PCy0yU4nvn3YJA3bFScjiweRDV_xvOAW2w7EesRX49qrMGPFv46gVTYpZK1L0BGYDlc7V8jdGE5F8QmC-43WL_eoEKZWrshwrRuNGyd6OVj6c-akalLOTFds1eKvbsVneYZHaziP17-gfXuG2JdGmX1EVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEnTNAzMVpp_7k2aTTcQFk7oeiu1f9ygvctyBUqyJ6PnYIqjH8WSDNpu3QGHOY0Yuvu2E5MS__D7ZmKIzyE0c_mvqAJ9264Xxl_0LAjU-IFOpwLEc_lIOZzLb5ejBzru84OUMCOW9UZmYWDLoCLIleuaWIad7F8YyyT5ipKLllCnjum5TxrNHfCnR3WOsgioQrFbWVzBpGD3xMKAEoXNK7_YNNLVZss_i5UYPELOywmKuAJvWeMiIgMQ1itp9CCxz3il8jRxdWLEVKGSKIH-0929O893X5tFWE9rdILxPV3AiEyihLn_1k6RjlnbMx00Sks5WVkO4Ixof7Znp72LCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVAa5BXRTBYjlsT9RKn43o5zQaZJ4N8Pnk4noVOoLBhUgL_HN7gs8GjSPDG5-uyXyltqb2J2NuWvhdPMRsJFtxEiiFUA7zhZy4aVB7GQKv3-JA6ncigxNW52k0_iSoNyy6V_3Z2f3uItpqvUiiaHatzAVaoaygwAQXO4pXOHE-wwsW3Tt2UQQ6ato-2raxjo1a3FRKvZ61YuTlZdWJVt9KNoid02263mJDSKT8sNAg5kk6ZKTED4uBK_guUIRDo8G_n7KuCF5oJp79WOCV4d52gGlKeCXxbQxm4DFF8fwPVHywpJy5WpcYtPkJYtK65m-ZlgYQTpwwiqsWx25rSQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scH8ShAdeCD9RiC5lzvoDSHawCU5g55Swj7lC94vRh-uiiXcLKsom6gztmlRkB0O_0LksrWfu-QnTJnmj6AZht8Q5Ctdfy_tdjKVIIRAf0ob-m2oMh478FEdSVul4RSZ4pzpuN1d7HS1D9FcQxXgF6jXk-ZkbVr4bLOB8furlBNq-77lPQPdiechIcoFlzMQtTKEeZidJTfuWtPqEbNNC6T5N3nhNTvxz8EzJluMpCpyCK-c4aNzu-8HKv06m5jlWHTHjJj8rMvTkxYb5vK5heYICHH_JtD9XJVxrqgx1aopmcfIpIX3H078pQ7_erS2hy8boBZLfeqgo3wQ-dj0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll9EkuL7IdocoWceTlaodEcn9fK6wHuH88evM051Tiuyj-PzlmEODelRs5ZqG9rQJKT_zqUre9lfWPSjMPJ7Kr2FxTT1jz_q15-zBQS34SroEBXemslozZP6X8kJirpm4tEHKCUBHRRj5RZwIwvb0WfKUgkHfaSe2ALurcp4NKdjSgnZcyJgUr_S--byCZPtfLNzK0gyWPCtchOmQi8EqWX5mjzwyMkrisArzFWNOHneg6dZToCJJQLMoxiFbENCXU7V5QZNzXB9rn4TXXeoD7Elh-SBBoXtUbOdA-heC7MtEhWBP09-k48uHsO_sahm89Ud3l6x2jlFz62VBpOxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXhm6rqbVOMki8trwzCMxJ0g9RXbn5fteE_dod8aFlfGWc_z8CiQLusoTTiOKn77Tw8EhICTwjjRQjJOHltPkfqU7-gp0PpenYN_zSo4JQWkx4sux8dqrfGHQISWO_3JW2vca9T9_ytpMOEiTtFlsrM4LHyPKhgBF4pjQRQ-9pgeNy4-mqT9Jq_MATOtlGXgJL3evvfhZ09Tks0hZu1Kodz5vNCWDx68Z0FCnSjxKnYH56qJ6Dwr5XAB_cvu6D8yaw0A73DsRu72eDQU296Xoe8w-oCglJMOtUrDLpZbksYnx2fZemSw5hfgERq-A-3kbEJgTmMiQInfrWunU-1vNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Pp1Z33V7uo_TxAEWETGNG8jluLvVNMvQgZ-XXiqa79PONKJRP7bbOL6eHIc8JQdH8Kqe4buLdAX4K0EpqgmqPvp8Dq3uhHXbY3G2yOTm80AgluMKCZM5FWzQzclobFcr_lPlwrxwI9HZ6141bEU1WlEaCrXzwgxz-4KrXAwmxpFjBq9fDta3OU79bTyeY1bqYLIYJWXJM0lryHvevymniwEuLHbwxPsI53gU007lxOM-LZMNz2F0VcHWc1df5IluP6kLh-naG7NRAHXiF70_wB4GYEoZkWSQZIhXWdoIaYmpIOQw3Kb5wnXXPJrg-aGmmuxC3fNxIGgmwPNGwKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcR_MFCiFCQh1m-jFR8XqTfFkcbzlXVTXYBGDH_WoJDyc-0J3LaAmyvHzG-3BGKM2OvRnUGQrprwcxBMfv8-63YEMxuWv4oVWZ8oVDiEBehsjcF5_9xaAPBgCuwKtevBhKM3YU-1HKg9HbKxsbyotmQ92u256O26hK19m5aplcuGqkqk4v2vtjuBCzeNPRRZ8MiQ6jFF2UV5KO_GLEJ3TnYcw5RsETmMefdelGRjoRpELAUFNZto3uAPvhDmAC-L6cRY451YZdjuXSoFHdHX4rfZ1JCLjeZY6DcgvJFPXQw62hpmVSGp_rFJMKtQrqzITnijdd2aYMF0LDYeyfAuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edUEARLR7BC2eSBZVcfEIvxmO0anx_gfo1yyO2CwbMDokkFVMheygb31bLxBCmI98sk-AShozVvwNq8XxjFA_kscThSVdOJSJ_5cydHr_ZuhNUXOVtucbZ7leMO9pggr3VBUkd7e2fhGboD0iDkeRfsRDPZEO2UTIK4-sW5iwkVtqLiQ38uncsxFWRIYUAazQ14GXV7FsJhM0HGplzN8by-hjgF7QJ2UTi11o_D-Opsv7bUlwwoWuQ6Xfd_6w49ECH744c0XyCcV-Hutv-yOZ6kbf52WPlFJicEXrrx4UrOAV7PHJJMrfo54tGQYeKXIRpIU0UsT7V5EBYp1peMTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIbfXvFJgpYY12qXE6WE5kRB2xjTYC6DiluQQjjSS1X5BwU1k5FvfDtvH0_CMKklwITuasZaqJ675jUZaU1SVNwxO9sOw3LJlrVKNb2aVrWtI6s0hs2AQj9zf97_IFzh1YEBCkDMaSPkGdVLnLTx-m2M7UrECNHcULEUwraR7NHYg-b0GPD-WmUsL-SvFZCkiHURutqU5_siRZisNSR0mezLLOU9nQlk1c48I1gr0CbpxrDXJ5pnv9uPvpLFnuzjCfqaoEMWc2Z-xymtZ4jd4lS6KdO3WF5sdDqXsMYfBh0PDrmK8DSTKTlqmCnHGR3OopShGGYsNJwgP2lgEjkobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf2TiU32ON4O31nFULaSM71_4qUlgR36sG6Q-IFpwIdrvDcIwjs3ds_PEaMQgxhzeOCfFEj4mKaSTP66MfAQOuIg6nvYl_gkrZBBuSS24HbBtJ4Y2mPtTm_lRugRbFQC_KYnytVi-g3k7-DHeW1qTfARrNiYgN380A_RmzBHpfke7B6P2txV3g7NJABMEAdYVJbMyCOd-p5pKOmuOLPcAuuBC2Br2ngLuT0Y-tXXHJeyRnaGpvOOXonE2i0qlp_-pg0ArTr29WaP32Ik4MVT2XSCjyrNJnvYU5BvUmCSJDieZyMxTuQGm0IPbx5Tb307-o76zrddTLq--DPXz7pH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=Zy12JN20RExeBrl4G7pixa2x6ciuCcORIGACUSug_m9Ce9_fLI_XgwY4iuMJceKPu-iWVXMitKIJQdX-ZsGwawGm89Mi9wrCyRs0IzKk_J4MkW9IEa2PzM53bRriPHiqYiBHjzbkXnx37f1C0XtBjhSgm9uJKoBZ54sESpmjiBIS-QMY1YzycTKCjXyEUumdpO6u5hWogrej0ScLVd7lgMWY4XH8zW01q1gPJ44rGYPsdfo8ILYAzE2I6Vd_IXqZZELuJ11gvSo2htXoJwXalE22LBwGVD7A34-jHshqjFKXRXSLae6B498PBOCtwrtyCYgB4-gevibDENM8AqlWdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=Zy12JN20RExeBrl4G7pixa2x6ciuCcORIGACUSug_m9Ce9_fLI_XgwY4iuMJceKPu-iWVXMitKIJQdX-ZsGwawGm89Mi9wrCyRs0IzKk_J4MkW9IEa2PzM53bRriPHiqYiBHjzbkXnx37f1C0XtBjhSgm9uJKoBZ54sESpmjiBIS-QMY1YzycTKCjXyEUumdpO6u5hWogrej0ScLVd7lgMWY4XH8zW01q1gPJ44rGYPsdfo8ILYAzE2I6Vd_IXqZZELuJ11gvSo2htXoJwXalE22LBwGVD7A34-jHshqjFKXRXSLae6B498PBOCtwrtyCYgB4-gevibDENM8AqlWdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk4GIb-Ou4pq1lqmb3ZCi4Qk3bC2R34q9-v7hgimuQDg7GWLBahUUDHcUKh8FKBiZWO3U59_6t5IfHKu0iElI89yMqL3XhQr9yHcYlKkkT9d9LPqeAUxplXR_RE5Ixn-WNGyxFXjWvDE441CUjHg-bFGQMFICAymCchu02bAASVYCDjBaZHDP2bxdD31ZzEybQsw9vePI6WHQ5xm2PHl3bqXgpMCd1dcaiZUvmUkqDe1PQmYNTd-wzi5QEkCkECY5FnSw7X7xLaVf2Uo6ovVMdmo0J7lpXxr-Fd7CZgPaSSjGsZyDGnu7IsJ7Xl6Fo-dFvgOOLaP_Vgvp4Me0uF8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=uA1U9JxMyra-PqwAy-0RnFJb94JPZKsxCIchG7Q5jzSP9SJPkiCHTw8NjafyZqp2yvKZrKZVEn2D6VgDuVcw9HnDalHzMTbmsXGlEwVR9sHut7m94iedzXc3f0kjeVarO_7uQdi7QUh0_QEDyCWximJNIBHM806VE6YOBOgQarGP66GJhsBTpXiA3vnEomEF3hiP2b4I8RWW-mVEMkKGbgDlZBKjZME1XFGXwEPXL1xF-62aJti3sCyDM86x9vhPcO4Cdbuk_ru7AnYmBPnIoBqa9DkgesiklT73LSyxMF7aDp_SLimRaX0B3dD0ejiGf32bbPkZC9wKeHFBi8hidg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=uA1U9JxMyra-PqwAy-0RnFJb94JPZKsxCIchG7Q5jzSP9SJPkiCHTw8NjafyZqp2yvKZrKZVEn2D6VgDuVcw9HnDalHzMTbmsXGlEwVR9sHut7m94iedzXc3f0kjeVarO_7uQdi7QUh0_QEDyCWximJNIBHM806VE6YOBOgQarGP66GJhsBTpXiA3vnEomEF3hiP2b4I8RWW-mVEMkKGbgDlZBKjZME1XFGXwEPXL1xF-62aJti3sCyDM86x9vhPcO4Cdbuk_ru7AnYmBPnIoBqa9DkgesiklT73LSyxMF7aDp_SLimRaX0B3dD0ejiGf32bbPkZC9wKeHFBi8hidg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGjnCWR3rfnUG_JiCQ-aidiGanFru9_G1KEKn-TtHr8BpCiApyMiKOB7o70Wqf_w8K5eYcItI7LlwspSdl2Nb-DLuobTgGkKW4AH3jSgU-o8pWZAS8Az1lJtzT9C4LbP_8_g6DDQ90U8ou8csG3aemnFjwP-XoBOejP_FayV87LAzBMQ_OoNa677xGuBJNc-ydx1BO9GtVEEFz5zUGHtFlXjPVG_IZNIhAdx9jMjoI7Qx4aGqCnEmGSUwuI0K_bazmhqcS9Mwfz4TJy6XlmOkv5MMLOZPrmSQd87xAGTWwDkpyIAcYJL_7Heu2pPy0dOhYRaZwkKMImT9x-hyLYSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=OA1M68WH1XSLJJqu1GRH-0N_swwos95lzWfMX1dr4ixqogAb4gwI8ufVlkofwXzXB5UuPyyhcKH31WR1YZxO6ULAyA2bnwP0suRjQbwiGC5VRnKMW5Cvr3eIfEolUAR_E6Z_IEexo93-hK17pp2Mu6l1sp3FvciNjqy8mrKx4stV5A2dhgoEg7DvLgmXgpFcuE0vRjrB3wghnjJXX__NgY8vc0d-K7pZPJ7TKhRwWea_eFysL0VY74J6o6KGQV0gdU6Kvm0OhZEDg_xzmbHqJ9OOzWf8bKs-K082D-JU1xhiFHXIFychREPYpbHUxoWiZghbdbd0wjriZ4NyyGi3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=OA1M68WH1XSLJJqu1GRH-0N_swwos95lzWfMX1dr4ixqogAb4gwI8ufVlkofwXzXB5UuPyyhcKH31WR1YZxO6ULAyA2bnwP0suRjQbwiGC5VRnKMW5Cvr3eIfEolUAR_E6Z_IEexo93-hK17pp2Mu6l1sp3FvciNjqy8mrKx4stV5A2dhgoEg7DvLgmXgpFcuE0vRjrB3wghnjJXX__NgY8vc0d-K7pZPJ7TKhRwWea_eFysL0VY74J6o6KGQV0gdU6Kvm0OhZEDg_xzmbHqJ9OOzWf8bKs-K082D-JU1xhiFHXIFychREPYpbHUxoWiZghbdbd0wjriZ4NyyGi3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0TlX8cXMo3ohx7qepbnrEFfL8fbrNhr6jTZNSW75bJNxbL-eZPHEsOjqtl3bqbez9_HNbrMGhXsywNcNizHjkaf1ctEXrY3-TzI6144fytYacy6uSOin4P5w6IXLJCabL3D26-e0YHeTqM18nIE3hbMzabHriqgy5Dzw_GgV32Z-Ab932hPE02MFXWixnUaU_t2T6yBJR24J7-Vvb2Ny7RwR3jTs9depe72OB9SLDTN-cT_eQERoIWufKUDnKkff9ACeUMtixTSzl7ZouDvykiQ7YRD-SOijcblggZYL_2VJxn-u-xGJyXiy-P6j9NYNqiIwGenQHDakqW___EmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHZc7EcSIWLjvNuLXIV00JE47b25_ueQdzn9AJLHO05XjmoFbjqwE2FnkFEopmVRPzwbLvMe2sIp6fCZ8lZDw6eUFDXot7GEAKGZsGm8njdqku8ahtIUcaySHd7cxweFft8yucm1So-RA7glD_WP_COE2MRpOksadvQOujC2PkEDeoLdyib9JuHiTelRrQEXmeX3jJbyGpS7f44hYT2fp41THUGZn585BPdo4Y2IsCkgBydy0FIz_j13Gt9AS-eRiNcCUsOhbv3PnhpGqfZ83Zv70wGjuDhJoeRC61Z2l9tLA3k4SLzm2PjS-dMVmVaMERaQWMsP3VGHzHgzN0JJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrcSZJ1FA6lUk9QQpYtOR9O160qVEzzmxZ8nDxS6-WrJ27b1MluDvIxD8YeeBwJHGR1S0fqPhCgnpmcpHrvldLteBrdiBGq08lJ0dLUfGH055WcX_9Q4V4izic19taq1lZGeTHl2-VfzOX-7GydTQyNMEiTQAbFB0E9xd9AnXlyMQV-oz2BpqU48LMY0duWru3t5YfnrY07dQ0i8k-MRvf4wg_jOR7qY3g1-AuBFRPWegIaTb4czTpAYxMs_tsS8Zm7on8tYmMP5MEx2KFrOIHFx819sOylwl2Sv44iTm7P5rrbvssCYTPaW--QRomkgTR-wU3R7uukbdIGiw5E74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJn1coegbb7kMP1JIYkWi_V3esUVH6olavh8ovboIFZ-MSfwgJF3hE4TooDaUZd_qvFYrQpk6aaFdCIT7IisHJ4V3t5vdB6VMYAI3_SlAdasJ_Tzt7T0mJcfIcQB8sm2vFRty0TkBmE2x_zIDqBT11T-GpN6g6qlygA3Sb89pxrJbM2t4rkXP6okNh1FQXtFSuq5j486B6SOVQXPVIPtQS3PpSseGMeRFO3bluibF82YT9NqhDe-FDEC_TwenheNfjfRpOdiVevSrIhJ9PVylfHE7rjsMJ_U1uahLzhu9i_868H29VU-lk0ryiBPV-sqYkUOF65Q719u7BvC_VKlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmXH6mDeHCg3SgWYdOk1382ozQBfhSzMirV4MILhHXIgsQGFSQS9MPj5oPmsd-Ee3Puqpz2oYUZX6eo1a4T4P9CnYkFVBIxsyQ5U_9mOjFdPvud4ctsIOXg0d7PPv6QtG0aRbfLJMWZmuJwwBSF6bG7VOCfWjH9PWePCp15SqoAYjCxgq5h8LrAuU_8oMyQvuwB7SfvE4z7Z1yz77ksOKQYOrcTsCmemkpLMBYkXiRrJFQiijUIFP_303PnWtPPwMqVC92o0maTA_3ZpqHxK5BybvdENO0rbxMqe7Em9Rb_K0E9MwMiPJNVeHl9HDqacg1cZYp_o5L8PbYvYXgxZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU8tu9SIauhvpnXQ0yhtRf2RqVQ4zxfn3MaL35appbki3PcyqZ9rUjqCnl23CI0Ygbb29fsnmS2SZVjDC66ZgmYVUsRPhoR8vpQ2ctxJ5nvH_4ctegRI3_bRdNCIrjJoZyIHH7vUlXTO9V8_IPEucvw8no54PIGQG-BgKt6jLt8oHUtzUQQoXblY2vuUYUe93CCoEYWxSh6j-N5xxT1hr6jnoT0eHiV1WEPpqyHpPjGTcZcUqBfah9y-qQ8wHpm_Yjx5X1rIX5NetLJTD9dulx3Lx2dvoZxHAgQ-caDgzBU9PCUL_jv18EP9eovVrHWkk5LyCG3h6v0cUigaA2q2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNClYKS6hSf8T7U6UTwHSqt4QF8VLeQ2yqQywjrj63EkgsevaRtcXBZsLGdpXvmjzsmkpAwSCR5nv16gjcPPXNIwOjk7z24pzogIsvFnU9lEaycE2PuTR3Ich9c6_8c-B5E_q9kaYYcZwWSremcxmzIUj2YV_7T8-HBtbZiH0rPchG_e98jySbUcC7Rl2jlx0uBqs1npKD9THlW4exMFdEl4a0Od-2qPDquaa1Ite04faA52eNgIR21l7uL-hxAvYpdhfCGWLQxzRhK6cEFV37-WD1Ed86PmDdyafZvmaWbKfK1dbz7K7cpMznBeVlbeHfmEM6HoL5hW5w0s1CrJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db2Fz2qfxpGtFlucqe0j-12C-gWf1F0VVWUvtxafBKOsxjUYIZH5t8lpxrVHmU3g0bR2i1OTNdbW9mEsIjBW955j6TZlpLkA_O_uwOKVPFSHU8FUuqbnGB0FeWXhY4am99qrn63DPNi6GlOmN2gI30s0EOSz0lqNkmuW6y6NktWjZjNZp4rJRlxeyrXB-SvsOw7oPm892fxgJjdXVYCdzsEld6RKTWMf7PwKUc8yK6p2ATgFmJuPbsFGguQzeOowXtE0ANKd76JmXqsLsishCn5vXYhSAwtKVTy-K25AlljCz_l22lWTKsW0OHhw5_vH1HQQqrl2AMqRSDkRLZi56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwpfG4_M2OD-MMtEAlkkriT9e4PZ1931xHtn1Jkd9wZEMo36nA0xgg6nr7hTQ8QAJ_r1ujtELp1iSohgXSvk366tAKnk1X3_oexIqrZR7WpvITHERi6--V6JGxc71NnyNI19Gy1Q3N5JtQkeE5fQvQv7dzR9A9nY07kFXyiFVFzTwtbWz4DnalrZ-9oqU6jqzgVFD6cS49hwEHGsMr8g2M-mw3hQvU6qtEUvM5hatp1386Wg5p80be4gxODyHHhoJw37KbPNAvSBhYHAYphFmQ6QP5mh-U1v49C7Elo9IbBHreYGYbCckdwk7Thsh_h2iNfxjzvkCGrin5CtnkQu6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-UH0zsoe3DF50az8iBqvmaDd0WBKYb2-nUGET1vpynbcKC9aoPRrlGATP9h6hEHYS2bnotR41NOrs41pUFHGzNUi27gVa4ylQPhKmTcpNQLikAsLUllxh2MrvXZcePsr66VgC19OFqy7u0zNnyhSBzkLbCJe-MQiWPd7-mqTUbxWneJ6Q4HXLwEzaiv6T9ettBU-keFfSe_effCdPb0MlvyTCUkNaqfCThMNG37WPXEx-_2H7bc9RhPgoF78R8X2JjkrSlTLBvZbzp5cmIHUPT-tuin_D-5T7UbIGAocvIP3sK3yUJElawps0T2rPqQvi85McgOWgD81yyLcT2RFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvYYjYcPYg0IpARo4L_U5IX48jHILBJYBxGd_hGbx-Az3VVKacWAI3cAH5SRFllowbYv-j_qV4dSdoQWBtlE9IJyxFGROqB3wl69E_QooGYauRXDg3F-LNIwUNMeHYXAre_TRhiujfxFLIwvzHWlwJY_pzKu2GSeiTSMVQNCdMVSs3dTBoZoMdfL3l2nBVf_HjmNvexB9EEOXtUdP1SS4LU4NnEPjiF5IbRMszSH4DZXpQz7tk3NBEVhx_7ljN7s_faVH9cvpyfTkLmxRXRLv7-AeawNfI5wYy1oMm5UgVkgY2dNhwBaNDAIYY3LdNGTvXBQ8Rn-uD3ouC7ZH05DcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7eQVBJh7oaZ3q8pYip0bQ7GnRwW7PQs6WHUXcSoHXHaUABDM-_wLPZTdKq0oaAKZKzDKkkwgYrSriEnfVU6UGWCUkGXi0ua3pps4hpaZ4CPp_3ZIDVJ9zu5e_ScVkmRT-aWz9UMipejx7wwMZvKhzhvZJtBPEaJsuQEzZhwAAEP7URdmxUhhjIahlaGRbuqqN9hxH0BcNP3sCV2ZYtEPhyu_N6qW11J6iNSt4mcjD5pJUyYJZDrl9MZ0hHrPyUNp1aLk_DfDfq6rQNdfVPF98FiRBAqNquImaBkJM0yjar36hdKaRCd7ggpRY8D65g1XblOHiegAl4YAKn1JQlraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raWLQmzbKiiKA-93OARsWLOTSOhwhnoxGe_PYOVJInsF95Bc_gaBOaGUtueYYXUFEWjo-8a6XLquMZhAPulSV3ER-AQKm1IIpuiqPryaOamyDteF5LQSV62vssX0BABw6akg-53ddWiUa2VMnzmzC6-3sjgjOLcfHHs1bv27ceOvG4qtit5wzy_e3z06NxxUwy618mGUUdZnMIUvCjsc08MgVwyDBqvAEut8iFCtJB1371CY_jLz1SpvAEiq8rHKWVjWYctHvcP32YSlaC2Wep0Hh8emGPuAQiFin_Wubr_hR2-KGUyjEbmNT5sWOnn2EM6SNCtUWZvnHg-JDyaMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSAVwQQA956LjiNOkYQttUk384mkOrSkrtAzB7PlN2qm2eh5Mj1n2BmM65_lyZ5lgl-It-q_9e5GTAGQEBEolP8KfLpmTS5tBBej4Vpv8Wq0M9KYO64m9zqe3xQBonoH9rA8ayTy1S06B-z1eEm_NKwnrDvIt-bN89nSMjJQx2auM_YeylHTvTN0tgU_7aUfDklADPdK7Xxkui8x5Nry4Zat2tULOMcHMq0q_Lv_0xXaiQ60xLa0MyumSJQ1YhFyKtERhoA4yjWLeKwplGfMJJSCVEJdtXKXI_S7AanRdkivBc8iRqPYVe1WiKUWB047D8MN2HHjfWYotzWyFqtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlPmQ5yUXK6yQzo7Ssy7KA9fWyrzY8Lqw1Wytbebqtg82WtSI24OE-7gZ7Qcp1eDwUOPsfKcqwUdqSgZPnA_OA-a7asfmZbvwl-HMWwpL5DM_dPKigt-DeCG-4wo6JElJoqRCt6a_eh9jtFY-Dnlju-3_bkHmPvcettCs7U9DsrxlJXUK8y6VcDb6eI_T1Zn5srfYMMPLXrsgr8nvWp6QA9nUTpRsnNvD8Qwxoit7vEtyLuiqwdVUIqyuoKeITaGZSLa2JEyDJRaRPv9qIophy-14iYMo6z2mdsnEhSrawtHWnEJaxjlpnx_1vuktFKpTxAAN_MjwWqlqPXM3cW3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc5uqymc72eC8KvBNVGWRF5HxGFnLqtEtBz5DMMqZpjT_QHVJG1RQ_6qibeKnvcW3A3Y1QpMRdad93D3-q6oW5KPQgax3fmJUrk36N03tdQnxrw6Nh0ZWU4tRqu8Oj7bbgqL7Cktxeg-Shf94CBZvQr8PlClgAWttttqQOzXMLvC0-mFN90KAQI9NzgUUzsbJSOXknX_gp6Vd5NNplR6XEhxK8PwZ41dQDaRmAwiyJrnDJu_Rk7ZEvNgLN4EUZ-CO-ojeZekoNGBoPjrxViLFGb-bus2RKJAvA6gtBCuImzPbAJxgpE3jHEgIYOYhWVLOxsfWI-EUjeaqO8vzFh9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQeR3Rv11XBq15ePQ42KSE4fy_IGn-LIqYihf3QuBb31RFfhbJsw3cy0Mm1f2j3ZdsVzQIryo239HGkvuo4J8pA4YXxQ-LZ7uIJURNiYkPbZKtSskZG7LXo-JL-9gaai7qeV_F4LyPo7jmGusKXSJAUSokFd7aod6zeiyxU50-Feg6HKt_VL7NV6bpFN7sdYiBEMfP85c5R5ae4FEzXQ2I5oHmabA9SpscT4azYgvWBSJvHstjDwlR62L6GCOa2Pz9xzXITkRJAa99wlAk65DQkqX60hojI3itbb50cwtIAACj6ESe9mDYZL-aZGXmehypZn7_wnZo7jy6QYCAMt-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYaGzRRYGq7574wP1b1fuNxTMdiV5QnAqDjIJcBp4IHiOpQU7BS1sz8VOiBFFnwhcfys_STWYiYJ_w3X2PA32BTeC8wutwi0v5AZUAXurJOqdQ4lthqsty7lVlQGqvCGVbH3svwuCU1LNW3Uc_EgeH4242KsniG_h4aWk3id-tRotvXRlo_bfUqZVw2b5H07sLv5KfO-pHyQAHqmGBH47ciad07A4TcI1xLr5GMU3l-L1XfbZt7_uJ5dbNver2PJlCKrsOkWR_PayAY2ENwviNrcuN-Xv0ZW_7h2WlJyvyjTZTpe0M0-_CpQ5IUpUyiB_tpStSvKY222mOmkjHu47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdMFVFKw53IQx8NAZx9M84yLnd9VfjWpUZZcskQEj4R1kPM1AruUx5KonUh7z_aqldSJRPZHTmvP2qOt7QYXp7WkRXtNdVdQW96brRdKT0QPGBEiaEsenE-zy7naEV7BNYn7TaYVaDpsuwQHa1c3IJAp73Kbgr4Roh9oGZ9t6Ep88LtwXEtNQQLNQ4PzecPVxtGr4aSnnlVa53S5VGKFH8UI7dQCDvUtMi11X4fdZ6z-wFV736PVTLPEKUlF_XLGMWW2yvQQ292D-tOZyCtM7gxZPWH0bhf5OxJX657k18jw844i4EOF98mm-HtrdBksrjmKo0yenMIYYL-68Ii1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukD8O4AWSgdjgQhsALl6bSy2CY_cCFksry4C7noR18c_Y58BoPSB5HG1oGG_KsQZVnVNFh-ucxRtPIKbmpiid6j7Ml_H1FQGhupgI95kQYKfon6UDU7LdyRDdcxThY-4Uu645zosmvIqnXw6tCXkyKBbKLB0rAdLP8-hbA41puef4PFn64QBLFkW1Q5wYa6a0JpKOWc8ono0bqX1LVP5rsylVvmYyStPw7NU3O_6ymomJRQwEXAztn6GG8Kke_PuH6oX_kc5oi2RZTBCaWsWtLs0bcvk-JDd9uUJQ6pM_4VwofBK4U9LtgXYXMFtkik6t5ntHVGdM879TNoScqduRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaJR13qa2XGk-qUvTU0u4BbuagiLCzWBE5qsIqZkZIODMsIFN2UwD-nkoY1KYRZvjRjaUfw0J6Jx7_sVTfXtxjrlxfeW1D1ss6kaPn4sB3pEa_6L37E4lGNBxsKfyrx_A_09TeER6tjFxPSc84aN0gJ2qSEj7gZm7J7Y8rwt1UwwBOlBFkIka2gfHS3jR52_SQX-Yt6bErvqWNh5RKv_I7hA6gsnGkgOqgGXXcUH8cZ18x2QYZR0Q4MP89WPHT5phC1lxWVD8zHlJ1BOkbhTvYxzgWJfpDmQZ0VtB7DpBM8u9FnZS5xPmaVJ8mye7Z_xrfmzXMrf_oLkIRanfHsKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piW1UgoF4YP92wfvl8s-hMkKgVzax0i5uYlCrXbEXYR8XhH1jYobS3GB0d7cCBvrQo9IAjXefPmn7Cbt3cYe9-7Na4KIUJqN8qgqSwAenOk2p2iTZMXNlt6p6ENG3WJjmq6rXeVmZ8QdqsS-u66HBA2i4Ym5PMnO96yWx7rROY_X29xY-yO-l8uAGJb2Zy0ovIrkFXQPr_SmnKaBePKMZ1fNGzaHhnK3FhhDgGP5uTUTyvLkru8h-gZv5FKYXktTtdiqwEDIk4q5_tm6DIUPi5-zVFTiSD5jS2czkCgBwRzaHq29AcyZrjP5Jg549ikVreE6OhF2tY2yI83uO7uXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb8TP8_yhVZP_e-7R-tHgqJ3Lg_UK29QqQhC78TS1uyT0ujD56RffvOP9iUYxKzQNqbeiYVuWxUQkbSAmW1ZtJNadk-Ff_CCN9JSLlsD5t8Vnt2bdNWhQw38wCcFgGWrISlzRwql5Y_LozjeGpft9nau6YwE6whBzpO8FqJ9yulkL3Qn8AQAIuTiVapRZZyb2d5gfJ1GQ08muO2j6KQFMgR4pXaNkkvq-HGS3SC06SLNUYR5NPnHKcaTU-NAoujlydc7ZNnW3eHtk9B7glfCJ_pygmhscWKJCh2tHGty-bY2QtAfavE8yi-sllh939a-espR5CvSdmoeFGK2gvyDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgL1NCA2kIrs6WSvKrPM6EvMyS-kRKqhCF7WY6-Tan3HB5rlQXDoPV_vtBPIt4BZrkL09dgeL-wky_zb5NpWnIQjV_nGjk2amQhXMRBhFGiCHSX1kL-xUhoBNtxbLjPOkhrQ70vlMULjd0JTrlPtBaOxASqtw771XJuwIe2mEh5RHYK-k_t1GCyGmOdY1bhLMMVUOfiwsUeISY9UhXy3LsYPGhF8JMQBhiXOINImd5SiFbBBQTciQE_ssm1aQdwUsKELr9zUbsTL7DbPAjSjyr1GDlJC00RvFP4qt3UrPbxWVbi8Q1UaFAm95ZXG0F4hk_YsTHrYuL1jvv65zWNArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ux9UNLdce-C7Iapwe_vKnuDpsbU5LfssZuZgDiYKHZ0Ywop_2eYca08IceBJGPjBu3h2quGPJEWeassf_KX-ljR0KhdN-DJR7XtUa80YuDcHe_FJeP8NiWmfwNf9dPyQ4ACeVmwaKfhUL3Vlk4YT6oKuzvQGN6ygoltoMyzxEMq_jbj_xwhkCMGjY1KHhvMCEcdhPjToRBwRLQqflhOOHkSvquszz7ZDU3fI3SG5Ras-MEzrg1-NanN3MSz0ccgTDwwWMwW47awUWYBWpFqyOlFt5GPpUeyR3IJbxuGzPIBVwN5AF6sIRs7vsVUMKczk1IaijHl3-9zCKVjTYljYEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6jCQSLC48E3RLcKimOmi9zJuUodSxcjLJu4KvPge-DnM7DvomjEeMDHB4aIyezMLVM0Ex_1WVBBcD0vleb8X8HVnf-mYlreSUS_nhYNOpT1w_20jph_s52ytmD7LA2O1Otj7tDWcS6MFO7Fyb5T1xYSyS3vbMZcFGshoyQ2ezRPlaXct79jcUuvOyoB4Zzfd_UzhaX3F_oqELr_zlHRUZJJ_7REJYIoWCiC8WPokYXWMVlA-g2D0p3DzbBIkRne8CtBxKfbpbd7RKPIKa46fP5sYV-n3uwOkWvC_toamkykI-X8Lgg5_ayZPZHQN4XoYXM_jPx5-V_tGtijWw0sHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLlPLh-KZnPkmnp6mhr_72z8z4k6SHG_g7KXy5ctHxJfRRKkrLvCyS3zsjX8Pq3ue869lguCdQWHkQrS58ZrRU9hLfFaSQhC4iJw0YRxHA1di8WBVhQCVfvEqzo-7qlJ91jj-viKqRxugRgwJPuFhGD20CaFO1d8JMxnuhlR3GbHANy2g336oOXbp29bUN3g1YhOlwR-T0RiRE7P2S3PtccJkzpilOfjSyGPuMgOLOGEyKR130tFd03x6_LzhFYoI4AGYHFKlcLe0DhZjFePLTRGtpka7cd-yl4kqBq2M95Jgy_YX26AEH5N7d6ihvV1EwkD4C29rn5MG_OjgO_XhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9O9IErpNd9w3mlZw_a_5t8DLFfkYK4r0__uI97XJkoc68mskW9VzXXl0eSO7Jamt5sJhth7cfzqqu85M2DsnCzqdp7JY_2FIA-PVgN6-uu3ZkAKGCQsH9lMl0NI9JR8dLJ_OduP_TTxCyMHbvLs1fOTku8MJfADyqyhzL8u9z-t654YCT-WkTEV3ayeVafKPBJ_Ks9kfc8Xbsoe09p--rdaQ648BzR6r6sbjCxi32nJ91ld9iwPHL8Rjiq1CK9_yGnFTy5I4OrcW8QSZHyl4WAAlrdOM_zJ9isys7f9XnPKAb4j8VV7GJ9zvso7HFBsEPC21snced3WRkZme4Gk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5zXbFN3bjf86Gckx3VRInXF6lbgHCD7WvZTg3ZQRimnq50SSu58Lb27q4841r6JVzJZVxnjdeoPzdHu8l3T2jz-6H4yJ6DaWp9FmL_65lJHWNIIHAXJw5PVYVy_lcykIDiVS7jmTS0bda4NARZj3eN0NzAqW_59bVRBPHnMJlkJMj64vdXhiSS7muOr1Cvbvjf6AzS29ElEdNSjONYYdet7af9lyCnrPnmxe_OFBwanb2pxRwDyRN7_RkPHTxt_zl-t0ahMgwK-cQyNmtUN5gi02D9Pv1tWXfJY1dyOMsoIGC8mZEe2GgCxVl3rbHf7_qA1uW7wf94NGNPqzMN2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi_bFn09lsvCcglGO8E4vXe_0VqynNbo_u6BqeKLtgCGQN2UCNqqRzf1R3zPK46AhG8kCg6sgCC40mx_914DKKqnViE7bNvRBd8XBatuSD3RZ2ffc6GInEJ6tDubP4MDyW-tatO5fGLhMfTe2SeLiUbRkjgrcuPBj0qj-JNNbcAZ_JR7YwWhNzppbOnwRnBtpR3TgswqkBBdJrza44OlwG_9G-QX23-5pSiNXEV-xoRDXnHWPzy6ldpKedRygCmUUq6SHCh28gP2qIMJG9THmZnCi5qvgcxLbaq0XrWVa6vYmnhCv4r4OngyNlrRav3CnkoFOG7a05jb6UtrjATF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCPSSHtitWuZ8Qad0FhGr9K1Zt16d1tfJhsYXuczTfO7eQIZht5ZUTAF8Ng3GIGR3UtwfAPWDe6zxqR6TYtGhdI7tbOtS4JoncDyLqK64YtvfIfkAA6MTGCm2KjR2Y0vO0JiWfiWARETIX5NkAwg_TX0gTUjTgNW9F4ozXaewojW44ZX-s2BA1L-bvfSyaWg9xmsBlWhdQNSyRMMRVEZX0mxmeH2BFnMEv0gEbYer3xj4vTzXEYB_XH_TEKyVY0sij4MoEtd61eooILY7Q2ZTiInbA67ylHGKeIZwIrWtBpuH9-lj6aVYtN9tEliOc59zEi1Cp9Q6TvTN6NRzzsrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EKMR2bvLW9-1Nft1p1GLS2o-6LBuJpOLJ_lO4J88X4L6DzjyfodXP5RloiGSd8XZsr_i9vukZQJxtVu_PiEHGlOdJo09Q3wm0wCrpfH81aM1Wil5M9dqJQrPuwxcjxU6oNDUsnyN7fDYLIggFy6xpidWBmWZoZSiDSdclF21beKwVGB-YWDfahF0sO7ee49Tf2ourwD2VuiTQtbKrMLxrsSwuGgazp2UZsPC12E8ykee-RdR3LGSeWMaoQlkvQle7D4mFAxfNduXCPGfUNZxm4Z2QFnuBOCPi1aMyGvom3Df7qoQvtzNvLm_rRGS-72jiw6f7XUPQgIZ6khcx-I9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UbZG6_wMiOMSWjSmEDJSDaifKfPWCwzk0DFU5pJZrtQQwFM2kPMNHxBr-C5xnryzLeC9Y5asZ4UNDHJ03lg1E8cINR4qBmkmNxE2Cfw-PuosGrvyGJBMsnGQF9lcfdYvQ8si4y8o41j7oxi5KA6uQXWxfShKUCzLv80EuiNxQL8w_z7GuhyCiOnC4PL9HP5UR56cvIhOm87FI9ozxsK8gr7_EU5eIvVjiK8mCClWxza_vSs5vBcXfz8sNFRsFOGaXMvh71G7ogg-qhRz6dWMC0kFsWH9HYQ-44AMEzV1eYQKH-oQ5UB0_JJ5TGXnE6UqRDUVsGLgu6mxVxtRzOuY6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=g2R5AA8WH4ZQ5WNU-Q6o4GGEAtYP1OH7oxDtnU74Q_OPd7Kb38GgoDVqwWilnUHekLtHDPXFPavZ33znxyzVfN5KIeRfGyOxOlFGZ8cFb6FzCo6FGffMfFexBegU98HvM0dbJn-ZmK4YGdiv_k84thpVVKRgGF9sg9x-Ycb2kjKvRwwIi_ghOhVhtUBUoPCzOI2wTPFBTnZSGK-m5Z-hSoJa4EeEBmPElJuL2V-V1xWdIQqxHg4CfEKSXgt7vWthb7pvNJLp8NHAv1MJTtZBHi_hbj_5IfLWslHbmqek25qzU-DVSzSrNANQfJqGU3wXf92kr8uNe_qIGBky0Cwqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=g2R5AA8WH4ZQ5WNU-Q6o4GGEAtYP1OH7oxDtnU74Q_OPd7Kb38GgoDVqwWilnUHekLtHDPXFPavZ33znxyzVfN5KIeRfGyOxOlFGZ8cFb6FzCo6FGffMfFexBegU98HvM0dbJn-ZmK4YGdiv_k84thpVVKRgGF9sg9x-Ycb2kjKvRwwIi_ghOhVhtUBUoPCzOI2wTPFBTnZSGK-m5Z-hSoJa4EeEBmPElJuL2V-V1xWdIQqxHg4CfEKSXgt7vWthb7pvNJLp8NHAv1MJTtZBHi_hbj_5IfLWslHbmqek25qzU-DVSzSrNANQfJqGU3wXf92kr8uNe_qIGBky0Cwqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOVeRvF7itot3TPZc8W2P4GViVjcj8UC4Oacx9GirbWKpcyCuV4Uw5AxYvRcNHFV07sK-7KYLrfbI3vU3T0J6-iDSMBgP84RAEnwOuCz274nAHBi1iAqhbJSJDmbeAan571eLuYktUJf5ylRu97tMaXFfqAsNFXdpvzeI_WPGPJS6QfT0RQgIOFPvruAv-VrQqOcj63hTfLjUtHFoX5TmOC2jP6sZNzGtTvZcxzaAJMmXexG0fA_y-Y79h_nfHteaENMyyJCC1mUDofyLcBvXISBza65DgI6aF78-JEe8s1PcOs_slgxfrC5uQ-pnUs0_PXeIf0D5Gs5u9H5PgUzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayfqd8I981hY7fpfe3pK6NjnW3-_9VBsQ_lfxNiVHkQGd_iSPnFWXS_VqP_Jo0NMBvqO018sk-hYhL9Jr6Kcn4ZFHFEpgcincFHs9jNGjHKwy755ixBlDiUi0u0gJBqWkRsLq__7rr29fqE5FCrKBW4eErE_-ofog8CrGgADKdNyzuEkLiiTQpZPlwWcUCcn1unIslRxyYu5iFSunJF5AJW2KXzMwq5ZoY15rup6VN5Hlhm1v4VnBHVI5SO20qDopgl345MyC6ZiJyK3d94Sr3wb66HKmtYmRWK0bsgWu4O6UAFC0YLybIGziD-kGMCDk3E4pP8lBGUL0sbcBlqtug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4gjRPv36UOFSmQdLQ-osmPvO50_RXt58dyygJQUXqRaLozCEsImXDd62_qRqfE1JqPII4o8kq0YfQSqyGW9uC97z9Eicp3V464xt18A3--djPeoIylo3XBMBZzpLtyWwYEzujueoynvTjyWdIHmlqamaZZzBWpuaSLm_g_mj3rbAwBSc4JCH9LSF1oq0WJhFKDbWqQED0DdB3uk9S7gyvZnyGtIDAA09hrlAMxsbRlaL7Z5GtTeCyPGqymI4zZQXo8okWWldJniAgtO0xWhO3l4b_QPC7wdp1zPuKwTqY3-Zj4usI2ZmYIVLDiEN0j3MAXGwwoj2rmMFPZ8a_vQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awkrMTxa_2y8pylq_nssOzS9zH6xDqCW-DbKvBeQWijnTxEwaKGPLwNv2BopHBuljnjmWDuTXvRK5-wbcw9vykhxwyDRXR6gUGMFmpLaKE4LIXdbqfHFQ_KpP1Ms_BKs3IG-dOEuF0-I3aTdss_7R-MIvfhXXF8A4I7wlQR1c24K04ZBiEBGJq1D_wF4yojx2cuVWMbVCWd9vYp4bO6ELpB7IPQK9h1xxfqBU-McoicF0vQdZD2h6hLZZKUiKCyKILWBGn2x0ng_Er9cu5KO7zPYBHDe3P2WfImLZinoIBXMatYF1b0F1uIXFI_9lco8qQmCfbKtI1mikVh65mFgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cngTGeT-NZj-Y9ad1waAWT1WQd_LRd8mbWRnMtnowCaBgATdN0tpLwzXW9ng0InWWDfwp3ASrnIkQj2Lb1nyHDIhU2Zqvk4zUwZHBKWZzFt7QlaaQskUugQnYCycfW0_xvW_x_yORqOSdAWHlKXOPxTVoTbnXU5dT9xodaDz0u2JJh1mVbCWbeh6bWFihcMyMtE7NPJcT9UYUznK8K1Hnzl_TRPQMmVfjyHrY0pXlTH-uBVpNti6PAAr6IW_qvOTC7O0oH26Ipkpm7ICei5upKplFQESjjGTw0q8ZW2Y97cuMaqDYC1Lqa1ZngrTGCqFeoljPvIb_5MO6HD2kvG59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=XlAqzy9_Lcgp0sNf8VI9Dv27NsSj1H-M-YwRRRPp1fSjyEZeuz95rhX2yH0e9fzZAg4eG5ey5G6g8YJMdzSnxI6MNjWMMZSaJ5TwUQvrH3uy0JTdzKrReifNAK1HMkNfCvHZObd6VCfAASD_cGhOgYqvPbCP1MBkxRxRyX0uDqdx4RwHcA1pMlAUqqCEFkIYWyisd8_LLVKU93PLidJEvOwIPWG13QxsNkDxvtt26rJ-YgGI7AGQIq02Lm8bwOYyDw_HwXB7akxrZa3jDxhQ_rkSzyZbYJMIk3GKW0KUrZ-nWIENT6q6Avyo28X2wfE6LrltB62BCmmbzKZ1wzUnFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=XlAqzy9_Lcgp0sNf8VI9Dv27NsSj1H-M-YwRRRPp1fSjyEZeuz95rhX2yH0e9fzZAg4eG5ey5G6g8YJMdzSnxI6MNjWMMZSaJ5TwUQvrH3uy0JTdzKrReifNAK1HMkNfCvHZObd6VCfAASD_cGhOgYqvPbCP1MBkxRxRyX0uDqdx4RwHcA1pMlAUqqCEFkIYWyisd8_LLVKU93PLidJEvOwIPWG13QxsNkDxvtt26rJ-YgGI7AGQIq02Lm8bwOYyDw_HwXB7akxrZa3jDxhQ_rkSzyZbYJMIk3GKW0KUrZ-nWIENT6q6Avyo28X2wfE6LrltB62BCmmbzKZ1wzUnFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=PMYd3c7dh-ZWN7F_8qbizUls6iSys2uuyXVK-z1c5HOoX502CEaLZjRCzJZc_VVwBZfJ20bd8UaYH7a7l06Sdler3IYOZ5_aGA5-ExSQr9leOLmdK5B8zXgaqJb8qEYQE031aBFS5aBN-mcGWOARO_QcF9Jm8vztDmxs1knxDYtUbF84wniBkhV8kgTHSVUcOHTJKSU6tbiplZDhXAY0PJt6q-kw5hgAiJKzsrqo0bOWVRN8s4iSSZddIF5uVGbvRGpB8SB8ZlY91Z8i-JHGYZ88tSqbvWABdHCzQDy7FBgp3votvhY8-o72DDC7nfsgIiK5PQEpRkSDr_HsoYW73A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=PMYd3c7dh-ZWN7F_8qbizUls6iSys2uuyXVK-z1c5HOoX502CEaLZjRCzJZc_VVwBZfJ20bd8UaYH7a7l06Sdler3IYOZ5_aGA5-ExSQr9leOLmdK5B8zXgaqJb8qEYQE031aBFS5aBN-mcGWOARO_QcF9Jm8vztDmxs1knxDYtUbF84wniBkhV8kgTHSVUcOHTJKSU6tbiplZDhXAY0PJt6q-kw5hgAiJKzsrqo0bOWVRN8s4iSSZddIF5uVGbvRGpB8SB8ZlY91Z8i-JHGYZ88tSqbvWABdHCzQDy7FBgp3votvhY8-o72DDC7nfsgIiK5PQEpRkSDr_HsoYW73A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgsjR1U5nrr35MC-imdClet_d7JyvQYQfePFQ4T7LUuTCPRdC1mVI1OkGux9KSX3-4JVwwvChO-fELZcN9juwtlIzeYXrmUCRgeoce1Bfo4XXUUZcbCezhynpWY37F0zOlwHsK1DnIcgNezplxzwgHkHb0YcnhPFgTHiPUp0X9USKmpSgzV_ZTQq8q8KLlkdIWE23aY6xKyxFse_8uHyzZAnl9QQ1TTkjwbOHEhMfctx_fHmcb-KHn6jEKqxnZThocXh1M-q2H-iv8Ovdzvi-2DZj3eLksc_W5qwaSZfsYzU_1bp1GwpdP15YaRby3RREbi4mfAPSbfQZqM7oo2DeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sen9Dc6KrSRx4EaUSJMLpUB8aH_w24babNl6TlDxkaioMacCn1yGp8OS_uHp4kOMLXrUeSolTtpgm2p4gcm7zA-zSsJK_Rfil4RS_E9TjlI7IEYpzYHtP36roGfz3B7KWeYe_FGE7RZJ6byd4WQiLtoWTP-Vf-r4V55lRXVe4cOjkG1Y6YCc6PdaIp3EOqMdQfNd6AdZ4meytbpxqz3fJ8nsWl3QyHagBpRWPdo1bCEcEtr8o6iB7QbVMbmid8WMnYCtRxr9Qme1m1_wdzvi8Z3ZGuvntAyL0avYF1ArVBUWozNgIFf9-xXdCnihRVaQDCsGrp7N4GI0KD5Lh8PAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on4pW15FI1MU5mZn000JMWVw3aOkWPVnGFjqwrDfar6k0sjtqNIQTo3KJM_0HpA1GHd-80l1IRnSS52aysWUSEHvWt0ShyxXiVWO0fqE0jrdraFRMPjEZkLc-edRRI4vNTtD65tvlWdaWvd0wQ5mm1kt7x5OTAmZWGyTe97nfIEf9x33nA86NTl7mInmZWonoRWtW3nvuD2L2LTmt8Wmim3DB6xltsVispYrJW2yOGJmSQYshVO04EzEPt_jS5KrRs6bEnfe6xcxXEsjVR2TICAMhRBUqTSC2cfiMzoRSpFcyu_9JZ5RT8Dg27bNulX8nRb7s48SSJJe851TXYgvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNzf_ZS72e0BBv0KY5LzrPKP8HcrEmhGFQFBuiK2qZ2_tC58P6VFMMxK0m0rlfBkb2TRgpNsyXQDgop-k0x2aFYV_U117f12gAxiolyYG6joi69jH5jhS1WRet6yX6TzFuaKp7QDKIQcN2aPDgfItZ_fGf6rZcANlA5sg81Ss-yzerRgItVS_GxgNCFBtUGqhxxKL5qkCLTIYabX-cZyJUGaG1KBGJGyjB2VRp4ihfb0HRqvf5J8rXZ5xYuujjvPUIUJa7IcoHyfK-sH3-T9SzPWAfQ_i6kLKKlzucItAS2KsJwetlBvnrtsgDXhtgHwzTOU1ByTarGXwYoeWJTDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR2KIxKGJv48MYJskmHTw9E8mIR6urWjkvGYTWkeZoZv7o08XwsutRrSlmPNnMJcoF1SB8vMvkFB7daZ8tjUu1W03jFlGc8sB75T-vAg8aEWoNzmt4zjJ8TSAbSLYWZ0Mz7Iu5YZ52sN4y11cvFB88AY-wohKDHp_G2-EUP_r_F-PifOxO5owySYHuRQoLu6lRRILjON5FrY8r-YnIueOYmhrajFofiR3-bz_nMqsKxHlJF-XqO0U4yIMzQ09H7C1Bchva1agkKFcH_POiagG-8GvXS2vC11PB0S3ZE_-iTmZzmyeKgLzMF9HrxOHunlv0cQhfULkoY-kbBoo275_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sye26Dv_GTENj2ki0Gi2WcdYbwAeuYfcHz7t3PMa6XvDPouXl5NaKlphWugN-uwYsOIo3aM0Q8e5ycbtshsYqc1hwEGUB0raVWK7Zyre1BygULz1MMDSEA967nW_gwpfuMdyKd0FbTqWUotKSNpdJXE_rUKgH04JQzJs7X32KgFaS3Qp01n4oHB3LpTeYy8F3iZYeg_2Wxdh2aI3EuGf1gQxRnUInDV9fn-BkYxSHoHSP9vqI-AbtMxHF2Ias3SozYyoZeXCrWBMRxse_F-A1OY-cPDOdLNa3WgoLPk9ZHVirWS4SO_JDU6nl3c2lE2sGxAYleKKzo_bNLjir-RpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK5nfWM1WRANHu8nrz__TastG1B-IbiruPwDMJvsfTtGjQknN0de7xw50VvJtyasls7Wgen5IpIQR8tic2ZCR4yCo4SiKRVIqCm8uSf7nhs8ABOrRs1sM0Fx6bs4w3TONrcxnt6vkz-q4gpoC9CMVAztWBARjlZ-0XgiqUQ352_EsneJxqTupI61bN2Uy2cdDosS8w0xxMN2aQLlWLWKRwWrv_KvWFQ9Ehq2rezoq48wL9dpFSQ8s3V4e9a84TlQYYCVr220JYn1fJE66Sx-XPcvqKjLO_8ABtfNmS1jD5BDQcYeX-nkUunw8iohrD02nIURKJdyhFW6tLe8HqXvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=PJPRr7BjE1FSr-69w5EaJK55r5lXzs0FnLJoW5vr_pKWXmhpluEkNaTr9VrUoBls0RGCGfqMWL6pAZlC_WVAocA2Sq9jiSRaPOST3z7n0xFXbu0ekuSsZQCGXu8E9PBYPijIrQNMLHFjEbpTCnkcq_YEDXnUWOXFtRWNJPSDa7F0qa11Xpfh2JcCkrU_m2-_poyb6dW3En42cCoAneCG3iO23IIFiR4etFfZJU3DAOxAkzjZSah9axD3gzLbTQ2AmknQfllXMXrZUvwZyhbbby836-yLDj48GJCq6H8dtjJlZV_CLx5UaB9w5KEjWfqb3A62wbnWk6SuCPYAEmj-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=PJPRr7BjE1FSr-69w5EaJK55r5lXzs0FnLJoW5vr_pKWXmhpluEkNaTr9VrUoBls0RGCGfqMWL6pAZlC_WVAocA2Sq9jiSRaPOST3z7n0xFXbu0ekuSsZQCGXu8E9PBYPijIrQNMLHFjEbpTCnkcq_YEDXnUWOXFtRWNJPSDa7F0qa11Xpfh2JcCkrU_m2-_poyb6dW3En42cCoAneCG3iO23IIFiR4etFfZJU3DAOxAkzjZSah9axD3gzLbTQ2AmknQfllXMXrZUvwZyhbbby836-yLDj48GJCq6H8dtjJlZV_CLx5UaB9w5KEjWfqb3A62wbnWk6SuCPYAEmj-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDsE9YNJeEw37ke4tSnDWvuDYBexO2a_rOlMWNu642fxfxQw0hOghZmcBDveI23r5Di4Ey7lGudXkgkJag8-4MX4UrFKQW9dBNQeDqv7sLDYj1VemnbOiKXiMuSu8q2xBzxBD3Uckd06whAY8Azyu0O67Y9ts5WJ6UxldOtB1UwTkRb1MfCtFn6G3bex__rciL74qKhBg9pSl37Pa5WMbBs4UQewLGFF4wKfI81kdSFa2KGvZGhj_t97MuWkV2AhbJJBkyYSraPWRq2qGcGvY2ad8rDQSzdlVVPQpx5SxaNEv8Vk1jXn_1QG-Vx1eG7Pxn4gemW2iHfD-r7zjWfSBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB7ry0KNRTuvMWloEeoRHKPZPy7FZK77PDTjhqexCWmV0GifZyRR-71DOe5p0nXG9nEzvd3IctYq5GIBuvvqOXMM3rZD5I-kvmylTiY3-AcPyHLd4uQWpCOlj0dHeA79IQdViAjwPOx6bOIVnxFT1Uihs8GyjCASNUHt-dInyzELjNurnRRGOmpFqbdeWZwuGKflF4u3wzdhYlFgjHcp3mReGDOi5pnuBLO5GGPOVtT8saMT31-jPkw8zSCNPuPbe8i6MqAaKem7piswpzQl0tFKXbN1g5uINw--mO6tcvms9It4Tcz845Dzd-Zy65YwefowTaW0-OIZKIDk0UTbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=EK9Wr9yktP1b4r_vsh5-wtJrLaM4HffNmjhaoxvGzay9eQ16ZtA7-WPHDGcF3peG0ApkXCEJ6I333RSpgSLM8xESuv_FPPwzKp5ZTWmktPbUni1lURM3v0oyZgV7XfMo6xmKr30OhvYVLU__3MOVksSrineAhi6_uYKGgqIHcAIqgfxlijWoPLxKfDX0Csmc_HsNb8Z5VPn68yWhphorJXRdiVWiSh7iYkUcQByUnP-9qaRo96FwZuCd-AS7Aa_P6MHOGtXLuDEuGDaoVpjVYmXJkUYT9cZjsUC-G_t1vau4QWlcmCZMMJPtyflI6sCb1n1eh6wBYYRd8Jqejbs0Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=EK9Wr9yktP1b4r_vsh5-wtJrLaM4HffNmjhaoxvGzay9eQ16ZtA7-WPHDGcF3peG0ApkXCEJ6I333RSpgSLM8xESuv_FPPwzKp5ZTWmktPbUni1lURM3v0oyZgV7XfMo6xmKr30OhvYVLU__3MOVksSrineAhi6_uYKGgqIHcAIqgfxlijWoPLxKfDX0Csmc_HsNb8Z5VPn68yWhphorJXRdiVWiSh7iYkUcQByUnP-9qaRo96FwZuCd-AS7Aa_P6MHOGtXLuDEuGDaoVpjVYmXJkUYT9cZjsUC-G_t1vau4QWlcmCZMMJPtyflI6sCb1n1eh6wBYYRd8Jqejbs0Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=AgDnco-ilj_mX247rZFhfGQEYJ0n5prGxLxzEmRzpdsVsXnc5K8Qh6GNALDGE4BiG8C8jDeFOEqEJ07Bat3Mk9zJu0ERd661rKwlztDoyWSZYnlhFPzKwbm-mq0nTe4s1xg6m-pUhimmxIEVhexctk3vzcW1j9qyIUxkaDJ6lzTwj4Ed6bHbKUgTXM8bO2Y-fWk1nS5MMeiAIyatB-BqIynxBWEdwpYvaE6GKiKJRZ0rh7iqkQ4FSy6s_XSIlUXlbwQ4yOsklAokwruqQVjibyLcVLhL_R-BxZ653Sn1A9mBQ0CUp7zEjJKhh709cdcHH2osgAUhj9SPSc5Y2c-FRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=AgDnco-ilj_mX247rZFhfGQEYJ0n5prGxLxzEmRzpdsVsXnc5K8Qh6GNALDGE4BiG8C8jDeFOEqEJ07Bat3Mk9zJu0ERd661rKwlztDoyWSZYnlhFPzKwbm-mq0nTe4s1xg6m-pUhimmxIEVhexctk3vzcW1j9qyIUxkaDJ6lzTwj4Ed6bHbKUgTXM8bO2Y-fWk1nS5MMeiAIyatB-BqIynxBWEdwpYvaE6GKiKJRZ0rh7iqkQ4FSy6s_XSIlUXlbwQ4yOsklAokwruqQVjibyLcVLhL_R-BxZ653Sn1A9mBQ0CUp7zEjJKhh709cdcHH2osgAUhj9SPSc5Y2c-FRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVP1OFgMKOKDO_f3aa-W7rg67zniPBZdc0W3tdZv_oTu4uSrfUc2YHzgcdPt2lr67uxSPYbJtMpjDGJUEOOI-ODUUqB-6Wic5Vx7LDJzWH9tbG2n4V6GZwE3AUZG5zbageLEAUzJ-sW67jmjAyzFZ60s6Md7gciM2SnPskqv4OJLtMETBHRm1gss4dVfxYkHaAWJRkWPx--FSE90jAor3Trav1HiyZCwdgYGU-bnJRHtQsyqOY0FxqYwQKoN5ErU2NEfsDY3c3ys3pKtXPVYgSBYqm1Kp69AsIyYJsxucogcCPclOUQHL2Xn_On999Cm9AVljhvt1iBxzdlzaX3YkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThR5TWGH8HubxJLksuMVeEVU-5w8RJm_hxUUCwEuz-o9almkD6RXzdy2aXYotb9W-hPV2TxLGsEYp_mjquU-QeCcNdyi3WQFN2-pdJ62-qKF-LQm7yZ4iNp4H1PUodtitUDncKf0u-xCO3HFnGpbEdhRJMxOPBuOycEHXykF-dD1Of4wksn3Lsw56XD5ErmRPbauxHIDGYyTtp_xy3nLkBTl3rvDzrqfLUXk2up5odN4Rlh_DWEggkjmgqPvAjOjWGyZKvB9mVPYnuFzacLWTwvUPKpDzvJZQOtJqTPHlcMX-v98TruTj4GURzmTwr4xVkXGePz-1U3-MFoMGIcaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti38ZOi1EMy1RdoYWVoHa4YtTEZYzIvbZMu1eqo3hxRxsuVZt5X185hXP2cn62eCEozIveEBcgDco9iWMJ79E21td4-ejPBTXpM13rdrT2o2DSoRMdv80b9NgjjhOb9mMAtCzjjvmHyxZvF6rwbnsxmISNI05V298aulJzm-OUNJD3sKEBZsCb3NBZv91zNF8fz1jo3Nxs3wS-MBRpA7HKDKHQahJKmCkw7EvlAPoMCRk99uY53U10UDJgOVy4l2p9MpeYEycVBlVKkP4cSX85--TcsYBmfLqgZU7B_BpY2rXXK7dPgVGUxO1JccQLp4XDsfDQqDugrXmHdWLqkKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
