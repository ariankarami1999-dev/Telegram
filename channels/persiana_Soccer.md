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
<img src="https://cdn4.telesco.pe/file/EUTkv9_pExAVTzFRvVPwypqc9r5yOzF8Ov72Gd-vinh0CNWdaFAw7Q-0enw-ZMGxeK1EaiMAbE3PdLs3At1u8MEpBOK74y_Cufu6f9f4kjsG6rA-QAq4SMbNocB447Kfyz7aDXoq9Ywn_h1gkb3KYJ1jh3DRke3r0a7tm74cyFU_jhgUS7Q41nKyeAbCBpQytQ5q38OPbMFZZY8VZ231LzbSKb9fQUPJpjgHBfASUIv8Hf34oixz2O6n0HjktzuVsZXgWknt5bhd0ptQfsTSxZ4jWAOdRHo-BMWtNwJUgYjxViiWuwQ9p1Eu4QSTTP8jlO7EmyJhx93vyCwtqndt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 14:29:53</div>
<hr>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx07aEeIkAoCI58EOHj85eZF7h8S8-yIj6rTUldIs0P8fjmI9bbieUryERUkZa5qwfwkLHM6UltnCBQ7cx6LgoUF-k1h1Ur5woSuXPWsOeRulNJpUZJwsjo5O1I-6SKMUj0ZM3wkNyezmOsAtGux3TUu6FM86b9HoNslBLRQKXdAYMKlkIAaEGF8jQfIB0E8ROgzfWeSUID_rW2I5rUOSfvDWzjww7FUYTuGWsOoNj1fK2-QJ50gg53qpMjk_o6tIkimLIWFBeEmHowO9S23d_5kQR3ITNe8rfnKbD4gwbS0_jdh7yAawly1x1izASmDdYyZVT-jO6-9UzrecgohVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJF86rxGN9cGjhwYZZ3VCABt0UjtLI03pq5FDAgMjDlBFaTFCLfbOoeQYNux4hZWOtZ0RV_FJ9TMri6EIEGToKrYpUck0146MPQy125s8QxhThr91BU6UmDrdn_vI-SxHLA9bKKo6KXjZjL8v02-1sHjKtCXjeKuYBHXR4IQYGsEM9SVXi2zwqIPapqp6y2oAISDBbEhwKU0Ep83jLaEufhB02gKWwLE4a_f-HZBHdBx1gs_agY0U8Rutw8lVbKQbyY_TCwxLSNgThW3lEt4EU0ET3v7entXyjzJI-c2qM5Nw4jBkofOoFZmdqmIv3_noAlNWKzQPr8JISIz0nVJRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhCjIDt9twmOcctLL8h_dAM6V2CSRtiKHkiyOqgogge_AUMu2hk7a40bRZjZ0kVovsZJSJwMcYBZKuXNslWuDKg6HCt-jPak7v7Fk2eKB4RcquPYvLMeHr1XfQT4ZVkipR0gfulb-gGu1gmHzTzHHyncXvOJhDqm06-UMZ9d547NWKKtu-gd9IXhTvY2Kg8l-pW0_XYAY4BoFwYaprSPiHS6dCx2k5fc9RI3e4qoELfArJvvadH3xIw-5Q5Sd3WRsmLVnsRRwOmKyH0OyXmM6VG0LrcMhlCsxVaHcouiNhP7yE9q7UH1v7loWnb6BOCZGO6ZcM5lMPes-GCoC-of6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=kzl2cq3O7eyRQtB-aSw_o2yWN4KRMkHmRKEPtXjL4kzyaoL4oTWOnWWmh5q6GoLPaZAwrTyWHMpKmHDI5SWgcgigdLgL6tW_dG1BHDvgNdfcVTOkZnoMDpTVHHlrQwkHoDt_PeQ4c0IjMuo6nvOabKEc5B94a-47UC4TiF4Ndp-L33NkucXONxCb_IHcpqkXQYY5LRykCP-RBw77RKTc_wwo7OZHshw5VuypQjIVgSKE7poyWMEMld80NIgH4M9IpEEOZcFhNzNmtDAHvQisuNxWIq8bO5H1jTDNwwf70FTdBcEueT3rVINTkL6u1HKxkqOjdM9GGt-nFVGQh5OWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=kzl2cq3O7eyRQtB-aSw_o2yWN4KRMkHmRKEPtXjL4kzyaoL4oTWOnWWmh5q6GoLPaZAwrTyWHMpKmHDI5SWgcgigdLgL6tW_dG1BHDvgNdfcVTOkZnoMDpTVHHlrQwkHoDt_PeQ4c0IjMuo6nvOabKEc5B94a-47UC4TiF4Ndp-L33NkucXONxCb_IHcpqkXQYY5LRykCP-RBw77RKTc_wwo7OZHshw5VuypQjIVgSKE7poyWMEMld80NIgH4M9IpEEOZcFhNzNmtDAHvQisuNxWIq8bO5H1jTDNwwf70FTdBcEueT3rVINTkL6u1HKxkqOjdM9GGt-nFVGQh5OWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3BJGSWqYoutgI9r8-Otc4BI9IMj6rddID-Blw1cb6rj2ygSQJoxII5wxw2byz9mEzlhBwt1JSq8VvgBujvZ4lGi6UA8uQ0PwCx2EukAnL1ZyqJb0qWSoyNeFp-Y37jq2657BZsIP1odv5HjcyLXad67jjAkOMKxmFjiWG3BoZtlUx82Q4UjhQ8kcLQJ_tXXRh04V9RG358aiW5nRu2I3sjHLgogBS6gFh9k5F5LgHFhrmssZZSY8TyeXMNakeQrwmfvl5XTnmmz8nRovMoTgsKDVoGQt-NsNeLuXe3A9osWkTDMPG0JlBKg-0s5up_EZlM44-gmIB4DuQ45YRbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juPhyuGkucOn07p6S4xROgtIRoHs3_r1DiSgP_UXtPteZTFmT1YVbAYHl5TKSR5HlzlTj5Mwt4OXPKvtoOVWqKPbJJb8lijDiQdhKS5CMx7katpI17GxljxKrpqmWQtuIwpgAHJpUUTjbV0nrfrSilm1zGgnJky2Cl2K9DlN13sWUGya-1jPxeA_H-kpXKy63CKmboauthgCOiiR9muAqIn3wWaYbffgkXytxi6BQkFEvYmlMrIYxd1kxaM3le4dL-uTZG4zI-9s3X8m6maEy6MyBFB2dHZEV6y5sFDPaX-jC-q18HLdCXINyZw-HLo5hvoYCMeLE0ZMYCwqLsL5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0JvGmOW-sssEO-QTodu3KnwnpQx8K23chxDhcXoWWQux1A5nnxgmlqe3puc1OBuoPC7pvIGMFqCFLKQGm_9HyPWuwxXYvbonf0HN6065S-FTubLHXFzkebNcCCbz3OmLNMwCtfsx_jH37HJpg-7iji3XWagpOXV3no7d8_di6vdc931KiiBZRgX40uRlyXIeJMozNgI-vS_-OoMTap7qiZZEbKAaBembKCOmPz6ytqczCsuszDFcB3BLKnW-bhjPqfqOQrGRW4GOnaKfIj4ZFuA7QpqgZzxvbJk91E9pn83Ml6MJCpfAgAYs0wJYRpyFLFteaTBZM7qh2vGlWnJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gICxKefYIbtW0pQYauMQ1TkOhnm1jAP_--iO8r19NzHk1KOtyoXLYAQpmrNVqf03Vp-22p7Kifpy1MHmaawU3oX-DwxQSXpz8waz1bSzCUCjB08whVvZ6lcKWZgist5s_poD5fyI80slDqNaeK4WA5lokjuYQvcWBLF49IMUfk2dwO2LedQpI0q9Fao2SMV7D8tWToeQbBhFqly1QDMBcFsgpJpdRQILLoB7iOgAtzDZw7GPF5Kr2kcwZcdgA6HMko7leC13q6kelXplY4ST-S5D9OJuACFKVrdBovKKYVR9E9oLkhC2ZUh-N282dvkGK9mZiZNCCMDSGO3CnnSvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Ys5tQWALWk1tYgkroqs86UvcNm4UeHN5y8Aq1fi8RVxkhPwFEtbRT-UcJTna9vRCV5QDk9bObJ20wIlTPj7nZu7mtU4kMam08mkNIDOkj1B3rMgj3r2X9KZYUN6GOkOGN4lWsDPaM13L5lDN3LLsFDtel-vPdvDwkPSusCn6mzechnUsl7vqd7i7YC9qTns9bjVZqfrPKHGF_B0TkdeXFf_eVFFCz7dWIjYh7rnqEjhOmTn5Y9yVvc3fo0EJOaIw706VRMHCHPrDRaGayb92HT8YIJsnSEGRs8Qx7tUHOcoTwwr5x0oiJMYS4rdHmc_xezFAg0cwnC_VzpfA7_T5OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Ys5tQWALWk1tYgkroqs86UvcNm4UeHN5y8Aq1fi8RVxkhPwFEtbRT-UcJTna9vRCV5QDk9bObJ20wIlTPj7nZu7mtU4kMam08mkNIDOkj1B3rMgj3r2X9KZYUN6GOkOGN4lWsDPaM13L5lDN3LLsFDtel-vPdvDwkPSusCn6mzechnUsl7vqd7i7YC9qTns9bjVZqfrPKHGF_B0TkdeXFf_eVFFCz7dWIjYh7rnqEjhOmTn5Y9yVvc3fo0EJOaIw706VRMHCHPrDRaGayb92HT8YIJsnSEGRs8Qx7tUHOcoTwwr5x0oiJMYS4rdHmc_xezFAg0cwnC_VzpfA7_T5OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6A-dc0G77Z3YzAIYcFVjhnqAby_RIG-RHw5oRwORuxGNqwPbj_ZMyCVXbcYoaOMZTPGpgi1sTWTjdmYwWhyro7SP3TI1RBby6KqqOftd0NphP6MUAKLwPlkZElREAM56XJ1RVOLZW2FVZYE5wZlgE8r3_tCjmgACR6UgRHm4VRGvkwswJ5j-FeZcdeqEzHJEFS11v-moxwk-V3C8sNLlt_66-1zOw8l1pippMqPaoUdN94CLP3blS37Rzuovk0n3f2pYcnsugHqfuGAIzIeJci_6MfLoUGidUMK3PA7hhhw6EK4S192ax2kePGbv3TEY2IVW7whJkhO3zf5gHYLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6ApQ-4gxhlfn2Xm6pNkFRserp3kqlAwUkRrpjiLsnsxziBvOhikZY_aaL06YpfXD257OfIze40TmFQEtqiDan3UgaQXs8oSi75DpxyPl1I03wfv3V8RRyXRg6Aj0WM-pMO36JPPdoBVaAyFo1mc_GZOY7_ivC8dq3zFeVV3cs0gXOjSWxtDBkBSRPZTs13IOd9rhgNum653GjPe9ERoIvJ4Ot_feXNHhOKL9bmm1QkaCGxs1NnL1h_K4GGPBfEnHV4Rz6ceKU7GNdpytXxQlN80bPAu2iroiZe2WUtlG8JUFjHBoLcZCOUGF5gciTfVTfEMab8_qvbS5_sAMA6bMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26735">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1XWnD_JUCsJR11IbYfvw0yNL_K7vb1-fE6uGaLHtrXPEmtzrBECwqxssgGA63TrV57J15pE46LTbO9x6Dy-4qxfFQ4CPqF68v8i8EBIk-z-EKy25J5ZofAcZlpn9kCx3Ji3TGsc2u5U5D6O8KPOx_fMhOae-sfhK5Ry-ii04RY-3U0y_6C7Ruj_4JxlM496oNiTM8MAm2euq1UKUbAcyda0Ljcn9f540SasFoI0_Qrm3NcQUfa1XVYOkKbrgfl-hJb549yiiuPvxsLKIsL00QhoqbiDWyjqlU7volWwqKxTkvIBs1owwlKbAyIOC0LIAGYfhfSLmaqawJDm6oS7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
🔥
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26735" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvsb9SFsyqoVEAv5sFhnqB2EiFEcDmkKJR-Vi47BY7LxyJwn0CMuHGgyGcK2Tds25M89LjWS78g84orFA7Xq9lKwjiNxKyBAGL2iwpjbMdZCrBp10JQY-rzcbD8Ie3d96Ds7joRpqQaLfYXqg3F6Hd_muGJxOel7tk1hoaQyWhHgzjDiumbyFUpdJjnQoYxC-r74t2xzzOZI5Jrv1lNvMFsat6Elqmg2HZ4JJtDH1omYVbjMt7L_PxEO2IcU4YVP5rIvMQsmG2rFVtEIRchKxWEtbJ7UpGJPI9NN_a9ldlsefdIV8ZvYogv9YjFTswrUrHlCo67bIqzY9AsJWM_Y1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=n4zK1_3GGQ8zT5nRJE3bWrptWEYWfkBWir-DY8Wr7G2i4jgr1uWEx72SNTVVNUAgb8SkqHX2GvynPTYvRKCoIHVohIGimmIPWAFDvJGgwblW-TaW9jHa96DBnrgj2I08usUpu_HN5IP2aP-INulRZWzn6aNJ86wCrpDnk_Myn3-TpSMxgEMacTm3plxVyEX-BtTIf45s0MyIhYrq7OSSj6UGbHNy3upIh0jCvFtUugbaQBfm1Ybjl25rHyhyg9HwunwnHs6Jzp9o5irJjxOT52qV9cOYQcvTyig5dOxU7kHeyoQkUjXYUfrJHicquW4MGYQygU4blmYEChT53xNuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=n4zK1_3GGQ8zT5nRJE3bWrptWEYWfkBWir-DY8Wr7G2i4jgr1uWEx72SNTVVNUAgb8SkqHX2GvynPTYvRKCoIHVohIGimmIPWAFDvJGgwblW-TaW9jHa96DBnrgj2I08usUpu_HN5IP2aP-INulRZWzn6aNJ86wCrpDnk_Myn3-TpSMxgEMacTm3plxVyEX-BtTIf45s0MyIhYrq7OSSj6UGbHNy3upIh0jCvFtUugbaQBfm1Ybjl25rHyhyg9HwunwnHs6Jzp9o5irJjxOT52qV9cOYQcvTyig5dOxU7kHeyoQkUjXYUfrJHicquW4MGYQygU4blmYEChT53xNuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=vSnZUH4QAhql6Rpm1oBgu6RpuiaHQJOHSZPV1p27yXhYGyIB95szzbdLs5x9Ce4vaoLvuuLXPSgbx5GJdqAlf4dV_ppoo2JtXuRbTOehJuubZlXRG0FjrHPtPKrfE3PsWCTUoUmt8qqjt3QV_gp1lypUma0YqxoWWMcjxJMzu8nAVuiTUY82OuhzaBkS5ac5F0XZthMwG8blbJdir2GRv2RwY2fRZUdaf8U3mOB7eBGGzTiUAdspIZaNHONrgHca0eKnPHHlDQ9hcVbH3SBLr8KxnImlSZurEeIYiVbbpZ1rL0OXCSwQQJA6nPHWFoCYUP7GEHhwBE7rdLJwu-CYJpMojKZE_WBPEls6xINATc94MXb9-xufweaQ1MBa8snt6jrCh-JO7FXalLY28XKT8rHYC4cYBxhyPppeXXo462MHJWqoGAZT0S3Sk5mdfNahsVLBgh_S9HgEUCLK7kYi2QrG0k2uIiDMrMwHL1GWNVR1rdghDXnMkCktL9Vovd6fROE6_T2wSkqqUWt-aewtoJG7Ep5W_EfHsM1P-kE21d0SzezhMEPwZSf6vEIDyzpzaEIwlDJ6KjWArTGZyID4BiH_X7_CY3Cr2Cx2xeIYdv8uqjPbc0axXmHXmlIkY1vsGXpAnkEHpLTvNqFPnERRHJ6JFBH53GNXbEt6tFJXT8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=vSnZUH4QAhql6Rpm1oBgu6RpuiaHQJOHSZPV1p27yXhYGyIB95szzbdLs5x9Ce4vaoLvuuLXPSgbx5GJdqAlf4dV_ppoo2JtXuRbTOehJuubZlXRG0FjrHPtPKrfE3PsWCTUoUmt8qqjt3QV_gp1lypUma0YqxoWWMcjxJMzu8nAVuiTUY82OuhzaBkS5ac5F0XZthMwG8blbJdir2GRv2RwY2fRZUdaf8U3mOB7eBGGzTiUAdspIZaNHONrgHca0eKnPHHlDQ9hcVbH3SBLr8KxnImlSZurEeIYiVbbpZ1rL0OXCSwQQJA6nPHWFoCYUP7GEHhwBE7rdLJwu-CYJpMojKZE_WBPEls6xINATc94MXb9-xufweaQ1MBa8snt6jrCh-JO7FXalLY28XKT8rHYC4cYBxhyPppeXXo462MHJWqoGAZT0S3Sk5mdfNahsVLBgh_S9HgEUCLK7kYi2QrG0k2uIiDMrMwHL1GWNVR1rdghDXnMkCktL9Vovd6fROE6_T2wSkqqUWt-aewtoJG7Ep5W_EfHsM1P-kE21d0SzezhMEPwZSf6vEIDyzpzaEIwlDJ6KjWArTGZyID4BiH_X7_CY3Cr2Cx2xeIYdv8uqjPbc0axXmHXmlIkY1vsGXpAnkEHpLTvNqFPnERRHJ6JFBH53GNXbEt6tFJXT8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNwXbx8estDLFDVx99kYmW8lG-O7qV3zl9rlQGtXeMp6UUcMOIRG7ZQAoGeNFL5xNP6O8r3KVwDe00CtCq9JW219b1HUQifhpoyX5-r8gzXH1HSFhCBIuEplYeu6FJed4o8zdXePVCbgWVaAzL2jOe00E2HwMsR_zA9hWgq0PHt_9UYpPp1W8t4Gpjm-c4EcZXHj9i32AJiORiwouDskGFi500uBjDamFePVI-sLI419EuoJsjylYUt1SRAw6eFPuG1wakwv80Zgj68G3b8UNaiEvlx3bISkYaNDoyYZQOqMgeM0uB00eL35wJZXNusBKVgTWoYQMH6Q0kPSMl7nZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQrHulZH3o8X7tUCmwwJ7sQdbeP5v3aCdTk8M6tBHLhpWhyDbX6CZ9tOHwGModhRIQp-Lh7tEgE8Yz7py9ZlPEKSt0ls4Gh3EDTdSIYJttalGDdfgSu04qrG9HrRHL3mCYbkxBNDwXlaRcencLH1INH3UZyEXnnp2_k1N1XpLACrjkBtm8lWOaqTycJ_d0BQ2w4nQskY8bli4nMsbLOg7U1IeS6WH2Rm0dv2X4CD4lVmOozltkDtAjzKoKfmIHkPTE7Ho6LPDyJC_0FzUsc4j-fvDqtCs9Wh6ZndW_iQklZswNG2aa7zBBWeAusKtl-WPUpvprotl0sWE6bwiIuS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nltfsJm75R01sMpxsYcHAtggqjXdTWC_JQGM5SVzpjNt5arAop6yMFzcyfIzzXSMf3Xfj_g-mk88EUSp3sNChgviv3XHc8oF-2NlfobYoAWWxSJ14isYQJIslxZG1E1PSj-bmbL1TWLpLHrX2_twPFO4k9SlR1nfPfoZoHp_5MXIgk0yfCFFh7biv3wUesQsQ-6hxPGhEuUz_YWMDRjv4wLO4Dco7ufY7hKSuNDN-5BNFHcXENYR_Lm-3EnU45NlfG8hyuFWYfZO3qXiBimyWs6sJdb78l7PY4sNwD76Ezq9yXzer4rST9QMmf0fw6OSfqu6madoFhmoAnSQjRuIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBd1Tg5FWnuYi_lPYMdbwPI8w_y9qH3aDl7LE7h1orQcCdlYgucNh0NEUtmlFQpk5iFob0eAZnHmS8gC8IksAjxGx1g3X0SwUBIRUg3lsf3iC2Z7ANh8OyfEPdw3spELZNJ5V0x6bg5o7MNRIei-Lk6NhCzzJpgqIKr3TTrLXSnRQhBE2iPzm6r-yIDkQwUAkPmtc5W_tE4BzRrjMPSbsa8qvQeYnCdVFK043w1L-ODM82jKK_yF4EAULQJ5M3YpWgHF7KYxT95yaqLRjB1f4qMTXcaSNibh2432zttgSBdwYkwSpwQMwqWFO4aiUQ9mtpq3t-MVLENn7wuw-fsRFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqubjHV_lnQmLdDOknF4DEc2j8o1HwRKU2fpjiFdGv3MByCRQX7ufX-hbxTWYl4yy9xwGtJRrKsun51-IkUmmG9_uXS59vM7kVeuvGDYAX_tCf_RAHLkOAogV2gKGtec59GnvaCWNImaMIytnjo3GLByUN3LUDyS4jFKVUPzF99KtMNB3kXb8l1pt7SxD0QFVuuwgm-xAf2jDZ29Fi3l_lnRvCW4A-7upMZCM1CVeQujuANOd6-pLNh74jg4hnO-6KcMCeX7Br-RIyTDUU_DdbQCCyuiEDnLsOT96g28Azi-OowH6a430Un3ZzDFGXSzbL3Sfo8_skb4dAsjoh_2EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1q5bmCKodlUCMLVn7k1I8omVSiO5vjtW31npy9tAug4BCLKY9yAZHF00L6Kk-7kz3Y3asCcA25VK2msixR_UcQEx0xrt9uxFZHI2EPb6SGFAYZqi_d_hzIooDrYQgRJ2hATFI81M8NEFyYUbzj96PUcv3MY8vNPBhmR51mAWbavXSIO_nd4lgoNsvDc9bF02xRzWwRK1ul8RfKyNfQJvq1O4dvIF79nASY_aGVMAY6N_PxNEcyKjYVsMRCL6hyZgTKX4aM17RNTjxbf7mOq-Szwz62RcNbsK7GeB7QA6mz-bdb6cxKQgLLSKM3yENYmNu7qK4H3h1mWuEoZ79wzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVLMa4ouQB3JN3ukpWdftk-cMpZun3Clxjanl6I424TyrJQOPAh1txw0zFxgKzLGSzDLU7NMY8TUFqxde1FPMZ5gVHNnuLm9YbHVuNPC0RPNk8g5c15w7l91u1ftomFSwL0i47QJN_-UxvMCyH6a3PjSRv5sgu5eCoJA6-2tAOBlqmnhwEdp7RmNs5ATHaQojQLOVIyhpsLCjO7BpFJhSkY0W_4AHR6dakR23zwJF7xTraG_hYv1VaC4PG_ka6PjWJTFP-PtctAMwvr_0UjGACRMUV48ow4K1tL5X_3VXzq6pj-vSsM434Z-fDNLuIoD44JcBrxRnHgx17saeeJ5kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=V_qR-yvw2FiaaorQNCKFG95ytvJ9vxM_8Q-itt-x7QFKWWNPEPEP4MYnNkGB1o1qHuvEsHDCUqMwu1DlBt1cO0fPUaXFnPl7zqMtc6aEV81qBG8YaFZdbgeAxmHjAaITyZfENIOgeb6dyax-6ebBuzrNjo3V7fXNpNDsGvbEP_23AU9dpkrIiSGb3QkfszL-8dxZZENXnzU7F2EhXES0aXoT1DZel4fBrkCsxp1lOz27eL4su8GQ1D4kHpS-Gex_UfXXLCtb8uxGZpp4nZSsCDZ_ieNo7H_LGQAoUPBFNii3zoHRFqaYxOyIg0HkWJ1PHxXVTc7CQBgI2xAT898GFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=V_qR-yvw2FiaaorQNCKFG95ytvJ9vxM_8Q-itt-x7QFKWWNPEPEP4MYnNkGB1o1qHuvEsHDCUqMwu1DlBt1cO0fPUaXFnPl7zqMtc6aEV81qBG8YaFZdbgeAxmHjAaITyZfENIOgeb6dyax-6ebBuzrNjo3V7fXNpNDsGvbEP_23AU9dpkrIiSGb3QkfszL-8dxZZENXnzU7F2EhXES0aXoT1DZel4fBrkCsxp1lOz27eL4su8GQ1D4kHpS-Gex_UfXXLCtb8uxGZpp4nZSsCDZ_ieNo7H_LGQAoUPBFNii3zoHRFqaYxOyIg0HkWJ1PHxXVTc7CQBgI2xAT898GFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0znQNsQLjeFO1Q1alw8Jrf4PuhGB6bIIA986p8AajsyPRFUxtxvt-5GMdK_tFUYWVlxfU_xrAu8RxtoKDCfx9EiW32fyliS5aH4ewXkbz9iE1bixo8ZvMpbn1RtmgOtt0XiTzR-ruXm2nvCkGhVJ6s-nLrtonVaDTfLN8fiE3ljXmFoBOyZ0182E-d6oHawOE1zFxxJJd-OHvd3ISgEMBGtCwj3LOn0YyVWqNBlnQo_QjsRng44Yv4E2I25yjEUjkow2U1D0tJ_0nvnlZ_BRYLzag_UgoOYnMfueiYvApuj6vNyVqy_GSDluz6E19b7ozV4mqK00HQn63AsaE_4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnCFn3eGVHEKVDe-YcoA1sU-bIr6Uoml_0j4FvJCUSwxvxRZ-5L56dE0-L9WLrmilZdFJk6M4Ms4IYcY2-r2uYX-5rt5-At_l01LURd0SNd7LCDGcFSrXiYf2HwJG8YpAoGFQqbTZgi2e5xhEY2uAON3_tRV3U0QiorV2Rg54Y3aWNChvPg4qXB4CnGLYEX5FLUJYVZ61g0cXzw78CR6Nmzx2N6s6-oD2Qv8W-niavCJiQ-Beb56RvE1ygG87oOavGaj3-pAL_nMLDhQYRCts6uJ9p0jeeJy1YxbwUIN4-zsBwsV770SeUaheiqV75Dm-0Dsok1jDJLJaqm548NOQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL7BiO_xX-d2R3jattYxLIyc7golPaz-2uG0PtblZ4B-6GNhvtQZV7PyUhsW3uWZ02aNaYLmR8nvFxG7_uHx2ONoQpNnhG02HCV0vmVM0hkVYo95HPHNylSfMlVbfvBRzX8vPUqDpijXncdp_Pz75xrc9LlTwUk5wlHhYFYylcQzZV4mNCJNjTtfuHRQOr1zucL3PUx-7bkouf-vfNYcLet8_iDQg2S9mJqxk0JM-bcFAvCb6FDWBnmrKJnNrG8OBL6I5UmPo3a_OpsCjUlLXI2oCkaUZ4yRgG1gAn7nHIxJ9eX-bgcTWuYGYmGtq1QJtM9f8Ft941iXkGwPEYBnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZgmeeLsFVekYgYsm6QC-peskfsZj-ut3Bpdv0omnvvDhCP5QXVNRD888udmZzsFc0COWInekgvdzYBp2GkRpFnC3lPnSWs6v7IwmiB1VxMWaZ9dOBqUrVim-VHuLlclAQGU_h11MzFchoWk43tB0fz2ybJ4GY_h3htmks6DaiPrE70hPF3wNqeRcuNpU7e9zAzMsRz-xlM4QwZwB8n5K96GC6v_-MfCxll0FEOPe4orNg92GVk3su5MNL85FI1CBhJvI7kGJ7e0nQE_u6I7dewOIXb4BBJ0TMsYlDQhBYMB7GtVxCYmWdVnrAUiughQWTp9yzWlOojw2NMnBAG17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=rULk6vTxM1Eh14whwkjhs_jZGwWQN9j-1iFUHdHjcGg763OE-awIulAhkbif7yH6r6258Ttq10ctK1kwYWbRqQ_DQQRvWNkxPSeXDxSJ69ZKU9UL1UP9DXdVEjqgMOBwXkeP0rgIM17EeX-UJ-vpr19xOpoUcDDBwXbPw-qRww-hfS_s_8NmravRwV2x2ieiHvL6HHj2ZBxiU05zY3KtXls7eczvvwdb45E9D3Hy-Ec-3UI0mcAvF9IXBT4s8DErK1-a-MCv-DdUHkdaVKiiic8yq30Ggra3054Btp0Xl5O0bArsTCVCXC4vpScUUuDBkKUkrS_CKkoQR1-Ra3O0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=rULk6vTxM1Eh14whwkjhs_jZGwWQN9j-1iFUHdHjcGg763OE-awIulAhkbif7yH6r6258Ttq10ctK1kwYWbRqQ_DQQRvWNkxPSeXDxSJ69ZKU9UL1UP9DXdVEjqgMOBwXkeP0rgIM17EeX-UJ-vpr19xOpoUcDDBwXbPw-qRww-hfS_s_8NmravRwV2x2ieiHvL6HHj2ZBxiU05zY3KtXls7eczvvwdb45E9D3Hy-Ec-3UI0mcAvF9IXBT4s8DErK1-a-MCv-DdUHkdaVKiiic8yq30Ggra3054Btp0Xl5O0bArsTCVCXC4vpScUUuDBkKUkrS_CKkoQR1-Ra3O0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxAoi2mvw2wPRnU_QNDE8ANBMfvN9SJ9xPmdx1ziPhi52bduyxjmcpKPl5tyKErLIkGsN0DTPL82gfEdnx-M-meOpw8GLcSIHLh8ZfJ6iLuvIyxZCoOd2Bo6CVDofoMMDIfO7DSe6OmRFNUJvG3j8Nvic4e4Sc5e6IBS0mwlKhPBdVRrb36TMuZ0f9xSv5ke5cDH3mPpmH1u4Cq8xpjSmEYGbPFPCl9BXFBiLAZsa1tedV4PVhKz3rb3pLNFxm5KwjkQ7gbWNJdh90EZ73_szr5wwLn1_QNcAXwycykYvjerjoUG4_hSMDFFn-1O6CCai2J3UDPekVR1XRxSlR6zFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdTCG85bka4LdeYeHICjw97oy7HOegUGte1sKR_b4tdJ7eUoSTCKG4RdY11pUaXFZddb0D64x6TNBEzX7veYEEZrprQUVjlRmb_-pebHqomZpAGZnpvYV5m5N6I6u00JBtjNrKlABgFfGOp61xmlWj-_FLDxQQJ3jbpJUIW0xc2U7eICyJZQqZ6J-H9IikRQ7mcjRh_CvCT65ytXONJW6pYz4kWV9TuCHqxIYOIJkt2CZN_us5yfOqL0X9kte8gGHpXP8aScuPdSuL6ld0L69euWCnA9aG3hrNthLVhFM9uF1Ij7CwJ4H8By2aYITcHn-ePfyehd0f3U4FbOFVLcpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUZCO7XubtmMg7IPe9xSelrrE3IxcDDWLrS1ipxChEmMpoLf66G5sJ3KZiglfQBJyS4JcvKjaD3o8kISqBAxiWT_SqLanGoX2Np66IzwXFOze6VA5YVO0PuZgdrjEyksO7xxyfiylMLwRXa8JqreMcorDY0V2NpmHT_VpU_Um4KEiE_Na557nF8vlk_-kTvejsGZiMhJBrYGpl2tYN0xuy2kUCjyvM6yQu31q5eExCJij3F5AhHasbIydJNDVasjZNQxcQnmrEGgoaKSK4p9Nik0qJZG-w3qkroCw13UFBvMyi1R_ete66j-kEHcnyPRIH_fbqAkYIaGt9h_dW3Wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=t4461CVoXqwk0G_cQPdUYmhN-4I5E34M5Ru9jE_lIY2BPrhMRAUGjBgdTB3W9ASjg0WOg0CAtKM1ilruev64REP-CvekSCljFTQx5uiJkWYuHMkRLHW7HRsyWe3yxrT90oCuKPhl7-ZAvqpdYAU9oz30-taDBgB4q4wMwtPqrFnH4GWpRtZV90o2vcKmOZmIwGNcVc4sfyXhDNcXzyfOPgvMcvSbHfdxUAsrjImTsxw7V1dij_ZBk-fFx7rd2VILlVJiY8tP_NuVFmOhN6fyiNLNkM985Z_1sTL9LS8hUwmA1K6k7HoB3ZfG9_4EFeczfLO-QYnMGT2TUFTEQ70MwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=t4461CVoXqwk0G_cQPdUYmhN-4I5E34M5Ru9jE_lIY2BPrhMRAUGjBgdTB3W9ASjg0WOg0CAtKM1ilruev64REP-CvekSCljFTQx5uiJkWYuHMkRLHW7HRsyWe3yxrT90oCuKPhl7-ZAvqpdYAU9oz30-taDBgB4q4wMwtPqrFnH4GWpRtZV90o2vcKmOZmIwGNcVc4sfyXhDNcXzyfOPgvMcvSbHfdxUAsrjImTsxw7V1dij_ZBk-fFx7rd2VILlVJiY8tP_NuVFmOhN6fyiNLNkM985Z_1sTL9LS8hUwmA1K6k7HoB3ZfG9_4EFeczfLO-QYnMGT2TUFTEQ70MwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=FRvW389KAlQYShby6ISB0Q_Qs5WpAmhVHyp8Zzw5rNcLr46Qo0bPw3OsriK0G8yXtf7xP8-hqkVks5NUH3MgoYVFhzXIjq5PH-ETsBKycQP5V3w9n0BXqKmX3Y4181X0bNXs1zQsq2RRdHxL84r9iYtgh-rTclsVI1yiozRiHcA3GuM6JfFCRh7Zce0wukab03hhxmDuKU065JEKXbgsn8UOhP8vNdlg6V7b5WIe1e9FX1Crm7RErnUAIxC_eyz7HvLFnryEguQuoIM36X7E9ixk8z3845buVX5UMFSPJ3st_bTiiZmpM3ADY8qrg-vTfq3mxn0LkvCIwvoRZIGMzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=FRvW389KAlQYShby6ISB0Q_Qs5WpAmhVHyp8Zzw5rNcLr46Qo0bPw3OsriK0G8yXtf7xP8-hqkVks5NUH3MgoYVFhzXIjq5PH-ETsBKycQP5V3w9n0BXqKmX3Y4181X0bNXs1zQsq2RRdHxL84r9iYtgh-rTclsVI1yiozRiHcA3GuM6JfFCRh7Zce0wukab03hhxmDuKU065JEKXbgsn8UOhP8vNdlg6V7b5WIe1e9FX1Crm7RErnUAIxC_eyz7HvLFnryEguQuoIM36X7E9ixk8z3845buVX5UMFSPJ3st_bTiiZmpM3ADY8qrg-vTfq3mxn0LkvCIwvoRZIGMzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urAxVPa9eyq7YgPrDsLCV-YPwpO0smG_Db1cvZaHdlOnqdh1ZlEs9CakKt6VvUkwLNtibxZdF4Pwp6RKjCtrhde5CxGjjqypNUAjib85oZi165DB1l0c6e-MUrfP-0ahUvVo5Cno8vDJfzOo78-uQjwCHuDYasj8esrkp-paJGbUcXOJukYFyQsmFZedIyYXuKvSTYQhkXNomJRA8kOAmIVOlppqj-BGX9wAzH_3kpS7aqkVbJQnTHL9Y8yXiGiuMaQZKJO8BeyzMXrveuTROEV3tfaTXGbqMhQnjNkqal3-sVLAUjmwSVBnEgRNLt9_WqE6NiQ25L7PqsHii7Yf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4zLoIh4zOh2tRTCCjC1tTLfBnUjtE1hiTFbY5Xf91pV4Kt0SSjXiedSrtWL2SCi2dWF51H4lSKTdmfSSl2vRnePUHYrWfEEuM3VLueuY-FhyKkMy6lE_2eBUjktMsbsYI3mNlGujrBMDXsiR7QD6WPixziuYZdeMHmK3t17P8OYaOK8KhmeU4bpqDDi_Yd8xE1EShX1tadzhL_HbSW1qvwrgWodu-ch0J0WtUleV7zMPWlpRjwub1vAw8As8t4eQ0txr14DxulEJ_cLJauX5NOaQUN_5OmZI2yBs3W3AbOxETlsgn5Hc6toyJIjI5oxxZ0F0sh2OUdeu_5tzbXCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=WB5dk5G-3GKgpetTjMnhQp624EbWRp-EnV65oSfwrtaZCqSdExO6KVQztConR99HidrlPxC1TMx6EBpB9vuBqJEM2GlmhOylq-rcnxSxWO2XmVRMzGbsWZ5MgM5sbwK5raUgH71tCWK3sL52M7_uLqTKCUz04fS3xdaCZAUA5lkiP98522K0V3byiNuoc0ZRx9oR1zqqGQ1nv7r8K47b-dSbThqKa1iaLBSZ9O7RGulBwjVz0F_U6h7uqBkNvSr3Ug2m14sgQ_OohewvidyJOkzQLk1goeQXzBj0vtxL10JKkAFjJ2uxKdHQpMnfvnfqWtI2foJUY3dHfaS5yGOhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=WB5dk5G-3GKgpetTjMnhQp624EbWRp-EnV65oSfwrtaZCqSdExO6KVQztConR99HidrlPxC1TMx6EBpB9vuBqJEM2GlmhOylq-rcnxSxWO2XmVRMzGbsWZ5MgM5sbwK5raUgH71tCWK3sL52M7_uLqTKCUz04fS3xdaCZAUA5lkiP98522K0V3byiNuoc0ZRx9oR1zqqGQ1nv7r8K47b-dSbThqKa1iaLBSZ9O7RGulBwjVz0F_U6h7uqBkNvSr3Ug2m14sgQ_OohewvidyJOkzQLk1goeQXzBj0vtxL10JKkAFjJ2uxKdHQpMnfvnfqWtI2foJUY3dHfaS5yGOhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxcgvAt1hII0xyoVMye22qvwJaJlMb4QMegwNg1rU08BDdmV6CjD2_C7uy9z5SjVCO6lsgtnVIXweqdmvx0Aq_MseXZwVbox7polIVTTGUxtX_Sgvz4zpL_r2xKpcnl5ONQ5SCwk7DNrk5SK-_Zf_YWBVOiQkgqQsezbF1yXRlLOWrnybmYlLRY1q7KnJjh3qGlldQzcSLUn17aZN33zHCShR4OjC5LOfE2g15ZR4Exm7XHr689fgKnIMW6etfpUZowJa-G8vVL6adDDx-qPOxdZYHjCozl5yNgjgg6EPybM1l9gnaIlr_1NRel3DCl25o0AmZ82zJaxRhntutlkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLlSxoK-z5YzJa-CYVgOx66jFYPRPdvK_YTmVZQMs3lgGhGg1EPV4Hiymeujb1uHOPr7rygSpLtigO3nbyApCG1bhlsJUzM6OjxdszMrRMpQJBUSB3NqAwvdJ1OhYkMQHKXQKSIKzBRp6yMA1ge-AKNxkKSlYq43M_h-VWi4BYL0fGy0fNHtyM7oaMg4lNGfhhPbXmEcdGGNiMOPy0G-aW83oFa8iCpk0KR1kLoD9iTH2AsAaV32EYSltWz_8dzZLAW9WrrtYJG69oxy5kTANwnC5jRabSnXs9ZsiYs10V-66nRCBqCuaRWFYP8Hnofd6lTJUkM85PKa7WtShdfNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZRa9EX1wn5Q1uKxeofp6LuXPdjqkbjYTF7PEyvcgX9hAunPe2YpEifDlPFWyNcKJfkIvyjer2yb0KcDDHVkOfkSGxVEZBIRfUa-p1AR5A45-lfnDJktkosQjYCunZ6Vp_nHZkWyEXDSm4gxwuPFVp1A9xUCgJOl40PeELbxXKLRLgzTE7ge0IH0mzRGRfUiZdXxyzbqCNof_8ywEZVo90uSE4i5AoemXrCELE3YldAKLdseN671Tass9Dk3w9RCU41kzWPZtWeyzV8P_wr1QPagHMtF73W4VXSO0d1a6mRnrqpWfsASEeQeCG5Aj1kNzaREPQ6oNIsIkgFZHl0efQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=GYnilr7qWIy1wAuHwr1cgokIPQbDWJNSb2ZoiG02ZujZFjefgBsqQr1CNEfsitGFGzvnCwZXlM4LZL_psmr4Q9iftIYnO6niG1e20aBvgTDGEg9kMP0QAcl1cb2j11y5ewQHzOFHo4-Rg-YAj8CfK5iqXEf8W6jVwNtSentJphbpnmP1AjQyFogpua5u3-5do7H6jnXbyQA7TmIqTYMyV5v9hU49XjNN6VHWW68OfUpmK2HTs2vkxAdCYV7bmffdyyqIZ6Zt1U_8CDkOhu3cVXe5-FHpCaXRRYAkxVsAU4WbBciNp8_ZjAtrgBuzjemST69f31Qqaklwmu28q0qsyoDV9RX8mYeYa0XFzRwrnZPiXFiPPzwj9IsRYypSOicXRYTeI6ubSabw5kUfAUfOuG_gxou_GbC-jkOGJsWUosn-FIaXiPXW-ENa8ZxFkLx4xIh5Sg88kEvFw8QenoUUeHeGU_wnyPsDbIRdLVZA-dbis5wO6xHe6OvuQQ0iaE1xjI4lWTp-7eAWOKQ0riH3jQ4Yzjhdr6hNzLpblo5LNlEjxiJZBA8bSrXTDpsxAXEMcu6B5PGmVhd1BX5L3vQmL8iZlh_WPsNnL4ys4ecAa5AdzSJkrcBa5qxwqY85kHTIu0Xyk9e-monCEemJc4AHt0fwwvrg9ohw8gaSK5fbg34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=GYnilr7qWIy1wAuHwr1cgokIPQbDWJNSb2ZoiG02ZujZFjefgBsqQr1CNEfsitGFGzvnCwZXlM4LZL_psmr4Q9iftIYnO6niG1e20aBvgTDGEg9kMP0QAcl1cb2j11y5ewQHzOFHo4-Rg-YAj8CfK5iqXEf8W6jVwNtSentJphbpnmP1AjQyFogpua5u3-5do7H6jnXbyQA7TmIqTYMyV5v9hU49XjNN6VHWW68OfUpmK2HTs2vkxAdCYV7bmffdyyqIZ6Zt1U_8CDkOhu3cVXe5-FHpCaXRRYAkxVsAU4WbBciNp8_ZjAtrgBuzjemST69f31Qqaklwmu28q0qsyoDV9RX8mYeYa0XFzRwrnZPiXFiPPzwj9IsRYypSOicXRYTeI6ubSabw5kUfAUfOuG_gxou_GbC-jkOGJsWUosn-FIaXiPXW-ENa8ZxFkLx4xIh5Sg88kEvFw8QenoUUeHeGU_wnyPsDbIRdLVZA-dbis5wO6xHe6OvuQQ0iaE1xjI4lWTp-7eAWOKQ0riH3jQ4Yzjhdr6hNzLpblo5LNlEjxiJZBA8bSrXTDpsxAXEMcu6B5PGmVhd1BX5L3vQmL8iZlh_WPsNnL4ys4ecAa5AdzSJkrcBa5qxwqY85kHTIu0Xyk9e-monCEemJc4AHt0fwwvrg9ohw8gaSK5fbg34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbBTltLAW9-j7w8sd2Y1B0IYCh5Q5WMazdCTBNQSr8a81YejSnvX28kiv0MqvCdsNZ_XSuHohWVwzkZnE3k2LndgYNIKz29XgxWPbxoBEAimSS8B1ztTRsqiNZcYFSa79MeIB5g7ge1zJeP0EggwV4Ql01jYmSAwSEv-fcEY4M888eBRbl_Y4iTCbc_STMz15GABTYeGyEvU4OlTeSeyzg-XdQh7QSfbRciLmIkFq-J2yyrQvtQupv20kN19McqklIVdZzHLPhcYlb6tOBBXlLYE2vgFVIsLmr7H_ycmYFQ8WSeRTO5kR3czep5MW_JL-9ZR1xG9Sr_4KGJgJNcNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlIvEtmPDLB0WaxT3H7a1bB7IcEsRkhjWKwemzKs2XqvfQVNzpUhhCLlIxcPruxsJUp-UK5AtS63zUQxMSh2Xc3pJ-1i-kk1tFwulf4TZ7Ju-_wPFZSr1Ub0uphq4fYgF5KLZeGKXjcaV4OvpAkN-b5UqyHCmDbloNFJcB70E4bQyoDf67E6mQhXfbSrLmEjtr10tLiH5KsihyTpwoEciKs8KE30fvsqGZhAGrs4nQhmhc3jxrWXvb5t8p6GOhgQF4BggVFcRsX9Fp9MTJFtpJ4h5-22KPdl-n01a_AbhgdTWX5I9fWWii8E2kUPius9kAsMoAj2y0CRqCP2SLm_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKE6A97viqMlXezC6JP1k0dtyfmQzA14YU-dUeW2J0VXm2HRyz1netFjNAFujTxluOOozgv5z_Zi6KRg_4C49G7A6vJniURdLBtyd8mZvFYvyHgMI_hy-NP9fg5r9VLgEP2S9_Tt3H-vk88O4066TYZSatWXV1SoGeKe1fBUiG3Bz67BRH2hDk2ek5okFNaPJ-jKUJQJS4xX3UDtYB4kQguev1JGarivIjVtLQj-NTc86dFXIczJbBLKMTC6EHgTm95whA-IRpO1q0sPHc8WsgSVus97xaoYti5OJyAOOtIsGD7xYoThJCVNQuYA1aXsexHKEcv6namO1uEjvst6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NM80lWiAGfzpVXfctgWBehID6e_rdRI9smsdsukKNjZDDcrWt_Y7axP3ozIhjtlk7dbwdIZktM5qsBHQiCWwZfoGhytrdNzPCsyOLgoruz2L0WI9dQmAHjQslxbF8M5UfbIHGrxXxSlrb_tToZruc6ueE476dwiGSS_0NOUX4D6IjOp7ri9FLtZ3MbBJ8j4f2jq7wmH2fZFBjfLAy-FU-yY9iPmSBXAMpWNf8PK6jrpUtD-u211JKg4Ux0jGOPYN-0ON-UR-1beWiCXjs_fX9IyxqwVpf-_GpMRiZqRkLwHFjUqh5VrSZEGUNlUE9NDAD8o6itQvERTRCvASFEtwWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1iSMOwZZo9Xr5jy6d39iV1GenmFckonB_7WSWF2r9VCAFD3HChoP-pHzSoAqFrFhEjYqd5V3nqLbIxmK_vLm0aRYk9S-gSQFERBg15RMILHhWdxAjvYDPnsfUkx-JVTPywbwItcdiOE36e3QSnEyEETIP_IiyK3Pp85n0PUpTgyAQVxyfzylbxqTivyJqrpShUMNbSqUYHPB3xLDsPlh9jcqMGDe3Xmk-rO5Z3q4Gu5RqqlOb61Wrk8GA51KHuL79u8TYQrjyLI7SaxoNzs71_f1wsDkUWXuQHNnh7e7qwtfORCSO9xZ4p8Z_igR8zDTi3Un8FMMoPc9VgGUwCGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSzwdRFR6FCpD45TydEmwy_xAcABWk8-fx4m0TW1SeATH23yZp0AEK9MfNH_klIKd8s_kSZOSD7GB_DAXjeVJbt_Ne6hIrzEzNEHqWYcCmA7YhqD1ERCmW-3ITDjmtIG6ARGKd2pVehKDsQuuT71z9NHN4Hlm_HxGdmmkb9flmICbOUTTJ_KN-jg00sgJTX1Lym4Tk-TbBOEKwxj_tfgo5xrf4q8c5ICgZuP1cm1LX33mhjtgkO0F8xEdxW3gmi9bERZHGin-5za7BIFbuoE3bHTgQhSgpDmlqY_YyxRei9Oej-j4wLKUrbAu8GtWwiHPUT6MMs_1nn7m3VyAkliAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M12L-Biq65bdINez0jruG5FuD3VPUfKghsvKaQIkLcFHdZadrFYQ2eX9K9npJ0KlQ1SxpHw7d72e-91Q68T8f_tP5-DLwsMjTYnCY_ZFpEbVVWR69KRrtayxyFRZwNtfD08OejuwtH74DYnYbY5rtaETH4OmjNdMHu4_6UPpiaYHqeBT_438C4RvPOdbzVyNYoQyuql7k4EIR4E3G35xf1SMvYq-pvoIVXlsdALulpGVltqoebtA-y02PvYVgWLj6KgA6kCU-BRNd7ivuHufzdOZP0ArTkqPGwLhOL8g0BSfUAII5Hls-ywzpb5EKIdu2OAfFt6bJfGVDKFyjEhlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=IPl5Qw74azKV_SYRN6KvhD94vHMDJTAxNKfOkFq-BWD-rENDUlAtLH261UrF70a-T9mQbwIjLfooNDYbgJQCe2-lHdWZayvE9IPYMOufafXKAkEVquCMMNP4oEDhlgsOWdCFcOpPMZHysDjY2gumtCNmCsd-sWjZmjXXXes_9DQEHNpbTtLrBZ2VwbSshC4LFZ2j6p_cDVLCNFy0xd5wbYpVMiL0JLMD6B8td8s2GXGgW5Cxy3DyOBRElxXxtqI8kfBBkf3RdQ2lyLYxKs04Sbj43NQzOFWh0MMZsXFgaIux27UoAKxmm9PXXhEFfsSVV98Rb4pWpvHHr4n0S6aGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=IPl5Qw74azKV_SYRN6KvhD94vHMDJTAxNKfOkFq-BWD-rENDUlAtLH261UrF70a-T9mQbwIjLfooNDYbgJQCe2-lHdWZayvE9IPYMOufafXKAkEVquCMMNP4oEDhlgsOWdCFcOpPMZHysDjY2gumtCNmCsd-sWjZmjXXXes_9DQEHNpbTtLrBZ2VwbSshC4LFZ2j6p_cDVLCNFy0xd5wbYpVMiL0JLMD6B8td8s2GXGgW5Cxy3DyOBRElxXxtqI8kfBBkf3RdQ2lyLYxKs04Sbj43NQzOFWh0MMZsXFgaIux27UoAKxmm9PXXhEFfsSVV98Rb4pWpvHHr4n0S6aGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqriooSijPmd9B0wpiHTLHZPF8D1UBXuM-8AYQ2wEMjy3ucqblZjO2gxTiwFoEB-k1FEWuxwuHxYgIDKswLb_qcqOqSamgo5qAddmRnVctmYDaXSbrjS4zJlq1QlSG7mwrFZQanx-eBVe7sv69gm3k3l2HGuk_IGsvPFn_kcvdSK7DhRnTt0jtANuxZDptUFgNyWOBI52_h7W84T79M3TzbjJwbUaN34BEB_D7EHLVFmQEgx4c2iuinTVMAsZ7Yx8mwnvGA-mOYWSQFQC24BlhyYp6sZJlJYnomRmQRGLKR2KgrDAD_0US_laThu-rzf6zjBcO9f4h3JpleBKdkXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-IqP5jgOUQ44JGvSSQOJ07r7eRrTmR7R0ZFCyN5rk8i8Y8P_M-FBwZxZ1Md5rmWw7OmcPtTKEKgpjhraAkYWgVy3cpZJLPfy9qKNx7LEc7WDQSCKeIo55s0QGC8Y0DvZJYqMgPwtjKY7l2tzObzF1dzZOfmZa34xDVwopev24me3dZYB6CMSTTv69iYUAPLZPuYwB0iMlCCS3Zdy7uflm9FGTy_gmfsPiEDAt5NwrjW8W0WvITfbS7uYZOifjltGXmsvL7kMzxH7HF73KKNysgL9B4N-Gq7Jey2VgPbsHt0qd1U2oO7eWV9DZJqsyRhYp7dTt25nHENsT9pjscjdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9Qy69vEatGWmQV6q0RQncIv-DSoH93xINEwoAjk4iUYzBdUijr5g9UHtjcEFhSYGrRI-PRj3933zipBVrKlQfL05uW-ZBL63a2-jXKxSSoc3EOC24lNdsregB0jiwTbIHpRh4VBSbo-SH0rfbUHPS3iz_G-hEc1LoPuMls3aztRUOeYn1UoktP5MxMacvVmx7PoZSkVklxEImptfp52Og2j7zmBg7l-AnBh-Actyily5LGycd5BqZSYuEMtoF2nKARwyrAzO3fRHqbn4lt4nYnnXPfFnvNigmqmm_ETEB0CiO85uZuJx1dHMtwTwrWK77G5HdgYVY4r-EIuHRFkcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=c2Bww7SMPMtWnjGH8b9Q38WixMiItpLEjohnfo1Zdxe6Wj9FaoF05sxHskdZcxqbivK1OSY5gDm66ICj_Ir5MLIO8TP9K08c73ySSHL4idv9BR4SxsQbfeLUMaRpX9Xt75phsM4QhlnirFUHstI3LDuM77q_92jx9Xz5I_0MnFICa7TdIjl1VYricerrTThyfhMIOmz3vF2K-Uz6zjgYVWEJN4I1Y3g0SWVj2boIFz2MhMur33qJ3P2bjdxEBgFEKEWxpS-MA6DaUIu8VTVBVdkb6XiJzak4twzPnJ-mhCeA0HPgJVIQbOlKgIE6jqvwGkMX_sa64YmkEVdn5QBT5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=c2Bww7SMPMtWnjGH8b9Q38WixMiItpLEjohnfo1Zdxe6Wj9FaoF05sxHskdZcxqbivK1OSY5gDm66ICj_Ir5MLIO8TP9K08c73ySSHL4idv9BR4SxsQbfeLUMaRpX9Xt75phsM4QhlnirFUHstI3LDuM77q_92jx9Xz5I_0MnFICa7TdIjl1VYricerrTThyfhMIOmz3vF2K-Uz6zjgYVWEJN4I1Y3g0SWVj2boIFz2MhMur33qJ3P2bjdxEBgFEKEWxpS-MA6DaUIu8VTVBVdkb6XiJzak4twzPnJ-mhCeA0HPgJVIQbOlKgIE6jqvwGkMX_sa64YmkEVdn5QBT5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUkee_ZL36aXlUopyqIzzxDFIFMFO29YV8GVTPzlMcNdIyncW5wltDfr3fTbapiRuooV1pPx2YoTz3eRCNS9ma3SQlcS-4zDKlG4-ODKuUA7xbfF-5ackb_ZeYPiwjUreXKz3GFQaT8ZKx6nZ93rWAZ0l0UkD3I6I-hM7-JdUo6Vcop6BOcQXpEvVg8DbaDFhPmqxz_ALgmLUnz9e__xTthDlmnrYljJmgxC7WaMut1UXIWectoNQJML8XH6TTz_VSMaCuFqUF-tAUmUKTpVIqfjYDZTWiXs6rWmiW_BefNEZeL3bp1W0z2q6j8CmuvFo_J7goJCi9BfzUyBZdOf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzZemyZQ81oL9AB-3EPU6L3lp1XCv3uTT2KNxaknz7RHwrHe4u8r6EJYeB5o-KsL9P7hKGKbbjrqQTaoy-zr4q0CqA0A-h-mo6rJF35NbiXULwZ6xbfvDxXPGPxLioZoAf2RQqC9_GmE2QAAOJijzLlfnPaLosqVx9NiqpB2xJtZirgsg2ANw_TNRY1V-O9IblZn9liwP_t64Pu0qcGA37jse47HQQ7C2SfKchJKotJHbhM9TRbc8trz0D66hTqV4UlADCj2BbIVW8A-V0Le6Nup7qPRtrlTZEm9VcafIi0-21CsHrdBaSxCXl-QiaKc1iltvBiXmQgkwgcmfpQ8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cckh7I2WVV__i22iPYkhoLB37QYxyQojdiS5TaErU6w_TXz-k0amTx2W-l5R0HHOxL_dIowXTJeQ6Ab4VUD0wieXA7QZmGLE0gDXPYvH_W7om2LFZov8cfnnxXIrxRZ6oyk7psWgheIE67zV6gXRFvP-FC3G9c3ghS3MII-mxpzBl5XF_mOvnZus3NvOmO1686hSgGWb3rEOG29D4vpCfEfFa70YoFFdD3_71OyRxzHrtmNemp_1TRtjQGllaK5Xx1YD-ZHx-iw8ddShGMT-1q4P8xRTBh5JRdF7qngnLHS2wn_Xhh3zxyCrN8RnwxN6UST_vbs8v35zZeVQurohpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQc1KcX91UBr5wEnXgPNJdpQVgg0I2f228gaeRTkAffcGeVsolzmROeR_j0J-haHTCzu2W7CP9Qz1SI15VIPbpPxVv73nuDYN1EGcAFtFSxBIePaWZbx8SfSIWmUCmvc_af9QT_6E9_mez9zWwbaODmpuBug1lQMLUuxkXcIf9tMrs4By0omYPCq_WsUMv0fdVzh6ESgwcO9X5eYCwRG1NmQAnm-xiM-KEYEFwUoohP6w_V9L7eNMXemC3VXDzev3FcCiqjvWPfOX-RuC3mkpYZSjLooe79dIQ_MfqRUj3JURguo6S0ElED1Fl5B55MrZA3e8zsRe8ZtocZHi9JdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8OM1RCRzIuJzug3hL-VcQ0hj6nBxIzUeIHNi4kcNvqJ20RntLe4i1bgBuhSRjU7LxYeD9biI6brdsfv1yNtvPIrBH_VY1CJOTKxVEteJ0cOEEWQKx9QNHYs7lqaj3__nNHVCqKVGNd7t7o1xJLVUKNmVLqxfxTHaP1r2DVFEOiJNLN3SXfxAW6Y8Dafj8ysuTwJgZIRO3W4F1VmYawbUf8Y82E03zw3po7_wKmQbUWHHlQjWbi8HO-qeTojY9cT-B4YDaudUDdAex8JpZG7tOepLNB22ojHmQRZmsf3y60eBECQGqaG7tpB3QOmRqh563wE8iq0ODtqXO5cnikJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBM0PtjYAWAUKMfFwnWqEZNzikTNLEmky26vrr1xlDO9VYNOeno4FglC8bhuuoHmglxgz1zEXpM6pWHLrpvehcnLVkKw0dqYI7VDQEd4mQN6ZUZgwSh_UwcnnTvy6MaQJ-FIpotqR1itzLg5WYJWNdx24EKsuXynuXq5YC64jFIU0REJAcR1w9K1g1t0PPckVi5f8imq_u0KSGimpguWSNvmgAzaLHBiJtrR5et3IQuiI1UC_e7IKzZ3wKbhdR2w7v4XvBjQVpvGRYGuVZEcpIESsCOHMi3fk_uCs2tc5paRbPE2eE6rmptpMdSiaJUxTqwFnde1SgVE_KW9v9yqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQDYW0GcOG5QrRSMurznEaDsO75C15-pv6AkzSzV8_48h6KDfA3L5Md4W0kdjdhGhP-YGfigwuepKvzCqr7Ir24UE6NvAVAC1dF44VUUC725afIe6ehyRAze5tILziYddqPoA_zkD9Tl73nvBkLkPKYvNW_QBCOP2GKZH-VGLKQpBnXIgDFnTClPn4qvn4wOONivx5gqrpt6K7AhovhoVaC8gAF4xRM5dG-R2lLqT2ZBMcx8edP6LOFLEWXIOYG5o3A_j5LbE7rlCSc8rXY9IlBBo2LFpxvcwZ5wm8y-nWxiNnxiIF5lc02pUp3_o50eqOvoGwIUlr7BLfH4zFz-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3qF_GES_xbo7x_WjSohazSGqRgppDktG4fpGa-xeD3UL902mUcivS4T4zRukAkbTOXQtoFMuDI5iTU8E61GXxc97L2ekPYRh5H4lEMLFTwXuCZ4RVnXatqQ0ZM3esS1NfHk2SOo_vJRc4O9Aa_kPXPCeQFRlmscKD6cA2_pEKKJLldtwfqsDrgb7RccmInwirTY2AnpwFdo3KaUchUjNSR5OQLeQ9GCFcDcOXBi8AJgSoEOcmjH-iTWXud-aa9qQERKxIugV3eBvrCskZLMn5ZDtR2NQ5BOFBnlrSBp1UsG9YawkIxdEE_4ccUDvkdgt9DGW1vNltL6RGPWzZb5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_P_wsSAQNrU1__KQoyw1CNDXvOOR7EXeGJVYp1c1vVUpi35oDdSPPzhgtrr9Cu7qO_4AS2ISnCOVEgRgsYaqnXmsYlj5WrWek3s_YWFWLsxe-jyv9vsferkZ3ZRbUB9khxBkMIkZ3WwgDTdbcANsMTtzMQFBzGqt3UUv8R7LN9B3JToGXed664uYYKNduqdp64ZsFRuMTS_w5-1mw8K2hCI3ANGwkeKkqVIrmfN6A4ZBYEmnXdKb0rePhoyi2TNaYeV5_hPj5lu9FE923drcke34VKrJxkxqVYUw78zrOIJP8FIp10FuwpSMQHpQrIgvfx6inE10jKAl5gKbNcKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Odhthkw3JgMBhwPTvN5I-ojNBzD3x7LSGPk6RnzudzEOT7DaOQ4PV8rQM5SS_fnDN3GCEEZdEo8vJLG71AhuGVWTlE1I-vLUUCPNuNZ9RV3HMZRjmUHSZU7n5SwZ27E_l0DJ3VkvH4QFaFuV5iQ6zO60P3_zQ6yQtYbhl3YLkUjPkXa5cBzuyxl-NvO4YToGkggNj6pPWNbgUaZfxyhwO0prTnM2uo0TodxRRyNLZ-g7k-1j8roe0s1p7Ccym7MWbrxJvRSApVaCOwx0X1HN09k-f68paNQ2EwGrT4mc2hSGszu3nUdJtOHa7EdsDPD1lDa_WKqcxNWdlr--Cnk9dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1Dwp3teiz7LIA4pj-_PoR_9qujXF68W4Jf8pfzczb2xG6VxI2k63ChK3syHAAYKpEBFUJfWnN709yG2d0b6UdyKlQWKTSWQabS9QWR2h2AZXlwHW8wRf71qRh2DX4Gv2FoizJ8Ybte_y9M9ExXqDNRahrPPGtSGkwV817pqAyvDOJMiQWJWK1HGr-VIihYYrclq2H2lwUxAR05NXxMIXIc4E73f5JDEatX-gbZ_zFI29o9w9VbB40Yko6P7WO2vUrWeh7TMZlQ-fZQ8YOhfZ2d1U6fyfY31wCETlKcJSCqqK7T9xq9OG3aIkWvbwphcKEfRI8m-qdbzliv_9JFjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwdH2zT5R8PSaM23KmktXE1_Y4PZuM94-Z82clAJPMS5SMidpr6pyG1puGaubEzrN3JHOnhTbr_aTAmRZz2GPjYUCN021jufpegUvBq4ckk2u29gaUfaetB7CaW91Km2hX1Tz5HGWOc26Rubdu6MV0WFqZpF94sauq5k6R1NDZZvyZt4k2hbGnV8EgQRbtKaWYOASzVGkSvavVN82mo6H0DTp81UYJwuSc2qqJNzhuHH85s4MvzALELb0NPX6B1cOS6QHHOe7tuz8x9lmqpqR6M9bsJVSeoU2iGSB1pvr2pz8M7st5ELIpS0ADMg6D6Xe-jQ_QlPJg5o740p19-kBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmm1HZrm5VsQ_uF8wlxKwIGu5_BqVuVDCWpwhpZciX_qxog8AJB4JX9RDNzqUKXQWjrvt6xfogX43THHdDcDl3SiHi7elxYPPNAh5oOtX2z_l_eHD2f84QQ8RIVQcRpHvZdqOHSqBQNpRYPEf_Og29ckYeqOPLlZVXwLXQp84GIHRL_mrFAU2ankXZCxbDhGWH65gx91b9F9nUyLaVo6Q57AXqU--Ns6wRBCYzYDdFRbjMZhv8-Tk_qxRurCJIZbenfH8XUhshcQqFMAlfBIvaEeympsCqCMzIAEjQwi_9DKWWDluKpWfe5SL788ihJ_I3NgtQ0EvQ5Vum0ARk3bIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxsWVZnDG3RInL1fN83uxR-b_3euHEGej_tuh_9s4E14WIZSiAgBqL2YniaOxNOUl2qsoxItA6Bf7n1ZC85fBi6C8sFEJP2siJwKeiR1ZXZl1snEd9bLBu9d-958r_v-FFM24FvcqScg5IL34eTg5UmM1QbEiugtPoAqL2hVHvBbD71feFmtUpWJsmmAOUPeT9NHF-T6OTtTnzBE5AoL5Vb_ErwtZyi463YCHBjON1HBlxkrGwKXOtTey7D1yQPTutp1sFUrraYkLJBvm2kafrf-7phv__RQeI2KPlPLOEh1KXIJU7oGAcYXv-igCroiKIC9d8AH5YsRaqeZZfiSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niHEJJ1xeuIlV6vC9ZMfrLG0b__Z89W5gVjIPLPz0atFOSNXENJwSVWWaeY6oB2TYFh1RVhAYhqDb5Y0FAzjVogWhzWHcmJD50RmoloU1SBpEba-PS4SZUjgeU8-M3B-FQh3u7u47Tz33MFoMV4Fel3OI6dis7kpciacY_rOnaKFffyiliGIW51fm8lL8TLewPlWY8Rf_UgHmoHVAR2HP6BXScbi9KkiGTAm1fwR_bmvrxtIFL05ITI7TUEd6aYpConRAaSfgRYB4DIqVsYf8coo3bUPnaHavRTJXByxn25x0xxKsqdonaEfeqczxbR-l6cwqK_JOecHVPZGgdOnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEBMnpNkKLQXnwGOA8svdr0pjCKhZwchE4kFrjRKahcD2KGlOEjN86anUFw9c-HJ6eI9UpqVFVMWUzm1joidrV-LLazVeojBQyCQbzzvH_fforekfKwNm94DGEJvdUGy-mBE12nNW4NWJ-_EhEac-otVymgaru9D7Vul7R2E4dpah_A3MnSFAD58wchIXRE9FtRG9o2Lg4dqQi42lLoIOK0e_SzNWN7DcIDKIIlmCDd39pjUXw4sudkPZHCZ1wE1c3Z9DPGbn9qNq2o-Kjhg3aDC2H0qBSfVE-fnrptb1T5i_60bkc84PIteNPWUDLeskyhgun2Hbf72m8E2mHNIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMstUibOvhWfNXvGlbbG3WZ8tmbQIAQhhM3KGfe9KOx8kJAp_jcTUPbc2JPQQH3lRJupKB_MznrFp6qU8GvgX9P2YnHXbHzjQAxcyrK6rsRoi42HEw7myyXykscFgAnsNIeHz4lwcNWTaIRPPMaQvVY-83vcC_S3yO5SzPj0wr8hHgumfzTG2Cke0NNBuGZiq-2701Gn5V-G_x9cDXPCBFjDPfWtIsbn_W5Hd_9NhBTB_ON9rKW7DsrC_MwSlGKSLELnt585KMXPzFE3S_lAylS0WnHLC9V_rg1-4HNPdZer-3ZSsV1ZfX5vOD2Wc47E32NsI2Mp8cD9jE575pZUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=UlAfYGxRKYRy9CRhmii1Q044c-2ggyNuI67jEmKynyuEN5lB22ir2S9wT1I5srHCQA9e8y95U0YWaVP3tzv-KzbhRAYLkFAWmVF6yESU8D6DWmQg6G9IOdMX3KCCpnunbLQThbamSGB3ujtz9Iya_fGO9lAOBwhilKf7kjYBSJw16FkdCYlJy51j9rM3Fhf4tUV3BIKv7s9hPS5UhxhKRMwpzZeurk7t3oE-0LuZ0poI1iTl22Z-XbVoxedZlmKtuk-MjenBMOswEQmsQekxu5dI4yU8kyNX29tsb3IJgV8--d9vUTum6g7esaNUj1ihL3gKzojdy5fR_ijEs6rp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=UlAfYGxRKYRy9CRhmii1Q044c-2ggyNuI67jEmKynyuEN5lB22ir2S9wT1I5srHCQA9e8y95U0YWaVP3tzv-KzbhRAYLkFAWmVF6yESU8D6DWmQg6G9IOdMX3KCCpnunbLQThbamSGB3ujtz9Iya_fGO9lAOBwhilKf7kjYBSJw16FkdCYlJy51j9rM3Fhf4tUV3BIKv7s9hPS5UhxhKRMwpzZeurk7t3oE-0LuZ0poI1iTl22Z-XbVoxedZlmKtuk-MjenBMOswEQmsQekxu5dI4yU8kyNX29tsb3IJgV8--d9vUTum6g7esaNUj1ihL3gKzojdy5fR_ijEs6rp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-m1uEcFbtp-61Uq-FkABDfA-CyZsyvBNd2kfDN1FMDlCTslW3R5Mk2vbneOEk3JcS0lbvDuaWMA9Bb5vD-CPJ6rUdNYPOrH7BfH4B86AQAoZFkGp5L5_n5fGqyU83GlmPRLNuls06iHcntwUtNroNkk6UR-JKs1ym6znrPSLMYaRPPDVBh6h3Gq9_m2A0hdBkQNGBMOo0Lx7GymHKr--LH34Jrj86nB-8XVR9tej-FoBWGZjYBwXYuLEYLyDVqSGaGcNThV7RCHQ1J0ZwCnfFR4eQlNvRE2V8EYXmaDXyo-wM8n5LJayVlhHq3fsWzAjbyXcZ4Zu4qL3cDvGQxLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZfdJ2b2OH8XlDlLW4gfNeR3wPC_xsiSh0nuJEY6N2eeJp3kshkqh6vsikH0Fr_2cpQpDL5YiqkaF8uvYoCo0QB9Gnob2p8boiZt_G-it-WA11E2auj2AV_iFdNNZMmPl1oYN44pxFwYbpT9-lxCMDpy3ykH00u3gjIDzVKWXRuyuX2Um68M4Z0AUSa7AuCklQfDe1xxU_Du0wiKqIdfZIp-jd8Knqxeb9GpgpmJtFCL2WN0KChWxxEenz7JR93GAX_3n3875fLd2c1uzzU5PwB5ojcwTFJwh0Hwp9L-9GydL25eOMvuJnqHPOwT4zW2TtUClXUb_BbWYSu67azIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs6ktV6LSEIsoHQ6mviVD4w5gi1wKFhaWWN_qEs1fck6NLnX-KWpegf9tyqod3wm3LGdb1dTlOsjrD8g4GftErMNHeqGaLuDW0QkB2dIrC2fGxWRaICK5_gJn7-z0jz9UJFzysM8T0GhKZpOVF3gHrGTFSlxrPp6FW3CoXLbzaNTVLkG6KEKCj8YBuREFIrqW1XCZg5BwDLFqxPkuYWhW_v2k1xr1OJjDCryImcCcsdhGdXceoPYKiEY3g1u5L3XTiVMNwEgfmtgHckP2m9HJ_TJGbezKVfd9UOENw5zTQyLQvp7hIsFyRkbNnaWKGK7Vl_lzN3UzuuadEWqR-BzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQtnNgWahsJ3Bsl0fGq7NNSYzIOhslbeyFs3JpctAtAKA7arM31jmImCHGlTjfJRTEB5N_xdxtq7Ref4Hjjlv-dKXgWfXk34O1ie1ZXScXAjGXoS3XJfNsIuS90OcPy9ERYeHsYwD4cr6x75x7vz-5C683E4-KumG-T1gPRJkkdwGRbkWZBMX6lTgIgfLc6TAjtz9vdvrA4YiRdrAC-tuo8KB5mCU9AbUL3hoOXP_DB8VCXFS_dAvLBMySoNIkz0YcfeHp8tP4pHZy4HZCgN9T6vJ7grbaKr8SbkOeSy9z1PApcCj-t3rVHnqZ2HqeialOwMOkwBx31yk-7uVoWgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp-N-foP0zRDZrcFa4ZB9Kc07dgC_Ljfb5SRRMMCCr68CUTbu4EMMVDaBZ3eVw9toAilJeBjGvqhS4nRc2BX8gbDZeljqIjI3BGpUV5QUSvliSzRaFN9HVMrSpb7o8_BgsgMsx1-Fjy8j4eqCVg6zUHsAqXUKmoRLjbtzAPNLEm69imcsu_mGEFuusaLP8Dg_hppmDrELyM3ztOLyK2VMMG2Av4GWVtDlZIbuv3uerQ50XFZAAVB2NFhnj-8xzQCTJ9vcKMo5NwAV2XoEqnEG4ffka807xS3nNAL-xlJpncCKB5GX7yXFVFbSOgeBRn0l3nG2Moll3tmmuXsnq8_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2vWf5OHRKEjotg_vgSJh71zJqEWvKHthJ2AnXYDmSK3RUeMbyPveMK_k_ZPO5EgiHCVXJyh4X9sRfwrdbATEhprWdLJU9pQ89NMHZEl7zlM3k3RFjYXGDrDlw5oVnysV_XS-MvY9hTU_4cnkGT8SrtA6MZYr_tDj-YPrAskaNMN3ZzLS7lNtro3GUl1kZojtRRVNKk6HZegTKOqHi09gLCOO-rLRk2W0lTZLcqLZE_xkcf3nVkEdnUifEXzn98__EIIp-Lr0R4uaS6_r-ZVuA8w3aP60X9_C6t-McpVo4wXtR2IiUxktLTT8JXZeRDvXR4lm8uLKI1aWHzT-96XYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT1JvbZ-DVCZ1E4ADw7I7ZphyIWNjWMNIlUjJ9bwbDOfCObs3aBbDTowOxzbC45iAfaZnde2-7vNAe9fKCn2wvWETzoktcJkqYe4Astf5aZgus5uaJ7saQYs4iKyP8yvMjTPwvKo5s0HemTe8XpD7sVlTb_3n7urW_Z5RJB8jAeUeKqp4NNwPhII8hswoKEVoN_AwzaDd_NurXl-7QAg-y11kx5SCCxulU8avoN8a-6IKbkggr57_U-k-paM2LURE0U92mbG7X5Oip5M0QhsXKA53_dpXGAcI-W5ma_kzxx71esGkkOxG71cCkFfJ0k8k28qijzAW8JgE-1LvLwrqGE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT1JvbZ-DVCZ1E4ADw7I7ZphyIWNjWMNIlUjJ9bwbDOfCObs3aBbDTowOxzbC45iAfaZnde2-7vNAe9fKCn2wvWETzoktcJkqYe4Astf5aZgus5uaJ7saQYs4iKyP8yvMjTPwvKo5s0HemTe8XpD7sVlTb_3n7urW_Z5RJB8jAeUeKqp4NNwPhII8hswoKEVoN_AwzaDd_NurXl-7QAg-y11kx5SCCxulU8avoN8a-6IKbkggr57_U-k-paM2LURE0U92mbG7X5Oip5M0QhsXKA53_dpXGAcI-W5ma_kzxx71esGkkOxG71cCkFfJ0k8k28qijzAW8JgE-1LvLwrqGE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg9jPiPwjvNERWNSf7T7fGWR-Ikmj4XCHqGesnT8EZjSkpsFm6grPRaMf8I2HBh3cwfdEnmSFs3TbGGdeKoJSieahkZ2SUefnzoRV7v0iE-RPqP_vjWMJe8tZW_G23SlibXX5gkPuv4r-_n13Bt2VADcYzXT7udlZ6-mBQdgg4XJNDh7qIerCkudwoEg_V1phYMVZef1462p7xemh5Y06_b5lw_QmTQUL2YaKMdXOT0DjZcLZ4ED3x50l1HRz4pNxG31fRvvKIjoadG_8cClMaYlotlrVXaWqDmARGUKsbFa97vTiyZrA9-_ksJ3m3gPrdveDJu6FrBEam9ranw9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grDJqBY4KCiIzbCU547cnaXtd2jTystYHj6bFDWnJMcB1501-PQJXzzemfjdmcdPKrwEhuBtrEiKglGocthgGTOYkPaXQI_y1kHIiqT-dER_KqPnOOTbCKRTD-xmJ8gw_6SQCx94p8q2bycfzi_l2Ty3uB4a2_EwLki5_kNkAOXZyO9gHToD_eGbXFh8BtWwZNGahF7M9JM72HaQZm-3mdDvjeWICzZ-ZiP45gkXuu7Krkq2a8TPK1XPDzy48XHPTayXMcc5TGrPhWqMvojQEIxQt8JzvCOOOBlEQbVUn7vnqi3zmbsdZh8YGNNgA1skQauPt_8onEVqiKmaeXSCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWTmCLhIjDysUy9-BTHpIYfFyZjmFa9snWKs_WkAFQeyuDT8_4uM6nSANZ2_gCnFbpLKu6mvxA17Kd0lNrUABNzDD008MQ7-7Tb8rriKE-HAFlKtr7KMSdfzrRhje0sEA5gYmeYzShUn2HWP58o3z3MHOziTJ5vNNfpnZpdC1tGW2ssXH_l8_H3iyoLtbsK7xoJ1cUYQePqKhiKYB9Ti9fMvYgJdnRd6Rb0bwizUbDQJsGZ42RKhY6-F0puHFj6P0wt3l6yBf48cVpRXA_ss7T_PMNBmiv5R_tH43tOAOlQw9_U7TBqyeOSQWSm9vPXctipQfOsVU9Fx-SC7-M5jGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=ZEKCBIMG4DzFskEAIssAJkMj97dwFM8135uRkI54KBHjtUyCqxGZOOjoDgop4tW8cGjgKUEXrPYHWpuYNdU6ODDc6tMPay4ACleJG4rvBrQCnSg-2toxK9xqlOB9rYJGzOKeLqTbGlbpD25QAIVPBZ_wHVHzSfs05NJFLAh4hsF7cSnMEGggWAPLl_doXE1qQN-R6zdyJxBRYdwibhEQP7paiP94iRfg2Vgf9LulVZTd5zveAIgo2vvc0lHtYgL0ZMxhMuZ9MULLf4m31oush0I8IyEB4w-Vdm-m01gfPU65tBJNabf_sWBuR9QojWjyv4KENaBSF2_T6TxOoriUEzDH6trhYYERKgeobFDElXq7En1s6yrGF_8ytHOy78cbDCAg7wj8IQbPoFpbZ_xX_cJV9hI5kuGphssAmCeaovkPNTKuLuYtlHMMrzu9vVbfkamKL8RpgImpUbjguNE6Z6ZNWPmTIHQDUrCQOmRCHhTPvQBvgN90z9Re_Zm9ADUqCxMbXdmfZzVQnse8PGShUTohv6bsxPzUiz9LuL0Bf4uzP0ve-V24jsuv1QdhaklTbru2f-7Zm3NufkRk9D1jXRjpf3DF3ZksYFjQsn5rVw0qE0TVa-JyvSZk-DG0jKXGDe5xgi5ehEM-C5jUZkwS04PHJ64Wk-rqTf-k6bcR0mY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=ZEKCBIMG4DzFskEAIssAJkMj97dwFM8135uRkI54KBHjtUyCqxGZOOjoDgop4tW8cGjgKUEXrPYHWpuYNdU6ODDc6tMPay4ACleJG4rvBrQCnSg-2toxK9xqlOB9rYJGzOKeLqTbGlbpD25QAIVPBZ_wHVHzSfs05NJFLAh4hsF7cSnMEGggWAPLl_doXE1qQN-R6zdyJxBRYdwibhEQP7paiP94iRfg2Vgf9LulVZTd5zveAIgo2vvc0lHtYgL0ZMxhMuZ9MULLf4m31oush0I8IyEB4w-Vdm-m01gfPU65tBJNabf_sWBuR9QojWjyv4KENaBSF2_T6TxOoriUEzDH6trhYYERKgeobFDElXq7En1s6yrGF_8ytHOy78cbDCAg7wj8IQbPoFpbZ_xX_cJV9hI5kuGphssAmCeaovkPNTKuLuYtlHMMrzu9vVbfkamKL8RpgImpUbjguNE6Z6ZNWPmTIHQDUrCQOmRCHhTPvQBvgN90z9Re_Zm9ADUqCxMbXdmfZzVQnse8PGShUTohv6bsxPzUiz9LuL0Bf4uzP0ve-V24jsuv1QdhaklTbru2f-7Zm3NufkRk9D1jXRjpf3DF3ZksYFjQsn5rVw0qE0TVa-JyvSZk-DG0jKXGDe5xgi5ehEM-C5jUZkwS04PHJ64Wk-rqTf-k6bcR0mY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ri8ySqNKhmz95GmMhCQiczPCP64gzp5VqPt3kY3kBZYufLx0Suk1OjskSAcer6ObWohngiIGg9lGUhEQdX3K_hQT7aNO30JLSaX9KBfF06MT1_FP6aCjK9N8xbmHsj6Brc8VJeGRz0UBcwsXgUHXwT8ng9EvATOW2U26tKqqeOUXKjTKTI9gKOUueFy0bGgNKFSUe0GZOtJ3zkBB201VfZ_hr4zdLzmLfx0Kz3phnEsBYVkr_cMgHemX49uOI1ZISZRzHhR7UQUbumiIHf8d4w2ywVDyzXgR8OzESEnB6JxsoLSRW23N7FQ_EO0CMAOBz6uBCXntfjdzJmeTTq3amg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbyos2LifCSbWCn7JrrWY0NRDhR2B7cQc9HOt_HAjhmGbleEB4ahmMm5jDkIvT5Qxe5EfJZouvSiMeC5NjTOOjk3qDsNh5J9C91p4Eefiir_5_dc6BjYl_5oF3lgRXLFu29XaIP1Gmf-3oO3j0wwOqCEM93dSa-iVbl2TydnKekboCZEb2mBuo_e0FrM1hes3VkAMvpAtNa8OjJgyHhT70OQkQiuqPANYBUHOxgFJWwITb6Akvfodtzs6CIhgMQefHau-0lh4Uhh-BKvedyvAqAGRYgskzqFyIzVBPlnuToxI89R_lOObz-rHHcfkT7gcSQM7SHxHt3QMkzq-ogWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=aTPDdD9ZwV1EAkGen3UIXucgJE3V5GFk0t6Vk8BTHFHcVGwN3A-kTZwgGubhCCUZa2KRXCwW9HfsZ6eIjQkr-KhRd6wns9ErWzbwQg-vn_JNclZSAMdHrYctjd9zSwMuk3mjYR_tMhlxzmMwse-gXWDwXsZisgt1sCpVxI2nA6EzkiEXV4uHsEJ0etA-39VztfNsrJDm2vSyTSWpz5y6BlBzafuNcwZCRwT2VHpqVRGRKuu130H-FvbNR5_guZ_OuqOjrE5VYTYQ235X7EYrEQ4u1oqLXkQ5ZLho9Jk7TWm-b0WHOWEXv24PfMoSo6-oGOrUOUWajafeJnmhf0KRi7W9S2NPbzXCHG7iiPNY-rAuFZorMg8UXES412FaMuQWtHJ6op60naaVIwuj_lJkLOGdbHn5U_pRt397IvKjNZb5hUmf8W79XUEkFTtPGkTfyRWOB_YYh53hWgpydu9s03OYLlQf9Mc4ucnVUqUTEyGTh_nGQZpCaIendgqTO9y6qiZkEGLEzxNNItWqVHHl7sXfoWXAVjXv6sCIn9m7EpOwpTPNx_MdUqKj2LRrrUNWamza0JH3mFIrsN5sM_mPHo_Yyrfpny6BUP1_lqN4RAgR1EvQ2YzH-xX_7wvDNkPZaWuKWa15iDfjzQIs5FfwmQZqWJ6u2ZWp17_kuApe--8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=aTPDdD9ZwV1EAkGen3UIXucgJE3V5GFk0t6Vk8BTHFHcVGwN3A-kTZwgGubhCCUZa2KRXCwW9HfsZ6eIjQkr-KhRd6wns9ErWzbwQg-vn_JNclZSAMdHrYctjd9zSwMuk3mjYR_tMhlxzmMwse-gXWDwXsZisgt1sCpVxI2nA6EzkiEXV4uHsEJ0etA-39VztfNsrJDm2vSyTSWpz5y6BlBzafuNcwZCRwT2VHpqVRGRKuu130H-FvbNR5_guZ_OuqOjrE5VYTYQ235X7EYrEQ4u1oqLXkQ5ZLho9Jk7TWm-b0WHOWEXv24PfMoSo6-oGOrUOUWajafeJnmhf0KRi7W9S2NPbzXCHG7iiPNY-rAuFZorMg8UXES412FaMuQWtHJ6op60naaVIwuj_lJkLOGdbHn5U_pRt397IvKjNZb5hUmf8W79XUEkFTtPGkTfyRWOB_YYh53hWgpydu9s03OYLlQf9Mc4ucnVUqUTEyGTh_nGQZpCaIendgqTO9y6qiZkEGLEzxNNItWqVHHl7sXfoWXAVjXv6sCIn9m7EpOwpTPNx_MdUqKj2LRrrUNWamza0JH3mFIrsN5sM_mPHo_Yyrfpny6BUP1_lqN4RAgR1EvQ2YzH-xX_7wvDNkPZaWuKWa15iDfjzQIs5FfwmQZqWJ6u2ZWp17_kuApe--8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu1SeI4Qp2WBGry9AIhDhJVhGlCxZapvM1bPUDMESsLwsEeAU-vD4ttLImC_tbfjXBoS48y6WxRh6uSdAo1LNZ_Q7DKsb98z2jEmun4FheoZUyNxP8Pt5QS4OSuYDZOE8XRXn9CJ_hr2mr5KfAEARdZXfi7duNorchqZgRUoPEvyWs58HI7eBNDKJpunyc7k8bLYle0rROU8LarU7l6nTNYT_0qZi0fQxCcZ-zyzErjnqr13sPnf2ktCVKvjvAAOnWH91jsb_U_W-6Hj83XHWF60Nb5DET6xoY6uUX5h0HSwLKgcIlyUztcJtA3XQN5b__TeRQJGZo70o9lgeYQmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeLr1vtO4eu_ufOGJBrSsnba-Nm1ZhwpG0a8JFvSQBVXjM13jrZl5M_5ccYrhQXA-fhxZEUuUpj9nvCT5AHe8-GiWekrjDmu9g19BGIIqxLVxnPFgzJdoHeKDLNweM90sIkTO-8cIgfgzjHkO_3xSUbTIZeAhk9rtmB1xayRjo3TAgmbUgb2KDu_92XSRBjx9a7HJCUrvD3z8wvJsjq3eMmkVduwHCZ-bzpE8V84aH6bKnvvuMZ9vxUCl9rZCYET2RNa47zRwZRXJ6IKataLV6PGuPfp_Yd8rOUZhcw2CoA5vFwXRbRELF3Ek_J46Kp0JWjKbjlzsudpdjl59hGleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3uPfyPsyJRQdVAL12XMH6Cs0w4LJqHl7nVuBkv285YqhOPkcNRVyjPUO_TAMFb6Be3QVqP6WkqZbDANfFZEIlLnXjZdLUNjTlvRBg7CFGtwzREczQCVx5YRlLOK5uDwwaZyOKaxraaV9O4b75cxP9WMVNghAsDzhvM7Bqhjl3vWA6a0hd5mhedgcyZQXslkElCy_thoEsdin__Y1zcWak-Cg8M2SAIsGGvyJ_pvNzbuSjC444JX_cy776nIsnWafbPGlbcCPdxEgRubpSLezz0Ky_bDDVbRsVi7PdH-n8_ab1Qlsr4b2nl_g2DCNROOGDye_wbP7J-uZkQF6Vy3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=mfxeO3TFW_UjdeHUTi1dgEVws4rQyiezyHZFf4Bc2iwrJlgpfV_Yb2qTCLvsTnJQVIAlUbvx9wPm-rUx3vniO4yFYOnM9ZG0eEVasKRUu90f0sTPxOB_QojzTCR10LqOwR8mliZCA0u2dSH-SS_W03y2V4cauBXISiS-Oro6_qrqLlFVUyYWLNdAaAqfijNCUvHnDUArbQss8jgG78sMXjLEzX6iLdAp01vbVwzYZW2qEeHrhYhWMCYJA3sZcAX4pc-OgLc2ci3e06oJdXwk1CDlVUWBYhIBG894YwHE6nNzwXyF2hZQSMNvOzr5YorGO45jpX5B6Ab0MvwIkcnN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=mfxeO3TFW_UjdeHUTi1dgEVws4rQyiezyHZFf4Bc2iwrJlgpfV_Yb2qTCLvsTnJQVIAlUbvx9wPm-rUx3vniO4yFYOnM9ZG0eEVasKRUu90f0sTPxOB_QojzTCR10LqOwR8mliZCA0u2dSH-SS_W03y2V4cauBXISiS-Oro6_qrqLlFVUyYWLNdAaAqfijNCUvHnDUArbQss8jgG78sMXjLEzX6iLdAp01vbVwzYZW2qEeHrhYhWMCYJA3sZcAX4pc-OgLc2ci3e06oJdXwk1CDlVUWBYhIBG894YwHE6nNzwXyF2hZQSMNvOzr5YorGO45jpX5B6Ab0MvwIkcnN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJxF7oFljLjthvpO3uonlD0DIZNt_Ji8xf0KY2tBgVCyJn0w3CGGrRj9EnWTalQLZBbuxOiSsrxU9TA0B8KSupBlUV_QAHUujJNgrQIDy6QRezKxD0Z4oPSBm3Ip7M38ZHulWOqaMSFiuw7iqXpWYtDRRo_sS02oVJZWjgT9BimLDsSe3E4UdmvfYNIdIx8RxBY5vxLKUr2OBZCyFNIObX5nPhMGrr_cYSWqrerDPfBJcnJm0hO0SzWUgHRh0XH_3o1SrJMBCXuH4YR9ZuvvaGvs7pKYfRY8GwXIk1Kzd3iSJ6DzXyXxm1VoIHjAgkUnkTRhEzqMmwjaWAgt9Vukzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n076m87nNPbrMMVYo5xVGmgp1NKJkkM_o4IhFZDWIJZVkeBcnyVxruDEU7RkEbkCPdnWoj7P8qb1cVgraS6swZtuRSO6lAYrbCKwAMl7WBX0VlkHEe6lZ1lVRzQGEJi2Z1ZjgP67aqXyjsOCVRLrX68QoGgD3e8juO_d3jojINk6kF62pQRv-zPaoFXl1hwPI70hK4tFv5SpqkK_Nd0F67Ztp_no0e_pWpE9NKeopi1eUVYyc60-gZtLST8LeP7BdPk_elCO0OxrlSD5Om_kh3VKs_CWPBHpdASucSyM40yuyT-aaj8pegqHPWmAg7hnOLg7yTEPEAxQ1gsWABN5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzFcv-NxXA7wsUZ-uxe63zWWpVwMVcio-2u4pkPaKhSKGnlQtXAiGiun57X5FPrUvKxJ0EyF8AIkcEg8-U89gXVUZVL54zlg-WhrYsNZmSHpP7gswRk8jXD7em_PQvGGTj2YWM2fSWofTk7GYMgTAUfJv0QWzObNBH-tigavjaAGr9VyV_y0x9rgdFwu35Awd0Tya8JOjD4bBZyD9hUJcjgjptc6qW_Qn_14VYMgr_qsDkRQ4VMMsiw_e2gAhe2-uhSssEIai4bnVYFTGt1-4QgSVegR0cGOWjFaG3KuVA-hta1qdbOgt3oqIrxKEOd7M-v-CE_H_YL3lj6S5qrATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=i0c77S62iiwnoo-PHld1ogj6x_GA0AJfLCiYWIYiSqWwTpC3-1FPmPmEZ-FC4YXRvL09kVYOyNnGRnjDAC-Nq6MJomr-bdEYzEM2oS1gH50AA-BquP9HFd67KkiivQq2cvUcDf-wsfihWC6WG1_JLETaPATeEoMYaQkxsJQE5FeN9_M4lcADGpWjf0VRJhXKqKFNPh0u9-YTTTr6VQ_dzCv1nL7uublH8AUZvFl2h-lLob37C01brVdnEP1Xtw8an1TLsan2qvz6DqrtEnLzXTFtwqVvqqggmQTqb5SavGsWukE9sH6sYgGiPNjf3iGeJOE9_ihVnz4TfIKke0bjeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=i0c77S62iiwnoo-PHld1ogj6x_GA0AJfLCiYWIYiSqWwTpC3-1FPmPmEZ-FC4YXRvL09kVYOyNnGRnjDAC-Nq6MJomr-bdEYzEM2oS1gH50AA-BquP9HFd67KkiivQq2cvUcDf-wsfihWC6WG1_JLETaPATeEoMYaQkxsJQE5FeN9_M4lcADGpWjf0VRJhXKqKFNPh0u9-YTTTr6VQ_dzCv1nL7uublH8AUZvFl2h-lLob37C01brVdnEP1Xtw8an1TLsan2qvz6DqrtEnLzXTFtwqVvqqggmQTqb5SavGsWukE9sH6sYgGiPNjf3iGeJOE9_ihVnz4TfIKke0bjeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czGxZ3raAzM-M094WAiZxiDf58ek2G-x3TMHBU9wbbQdAt6gGOGt-aVMI2ESC5lWFv67Eahx93Tz-KQNk9sHgaRz-VudpNKeEgBYg9Lk6EMOVK3wV6goeWnp8zeVxqm2o3OxpJhTeWTXLhsdMdp6CiS2JVNhyagZq8OlK6c4nc9Zx6my52YoVybg3pF50kMSlz-ZxxDOrCN_-HiD0XMnAUxoUQ6CzsJXP9-KyL7vF32iHLugLzQKoO7smxi_6VVY1t_G4KXLGi-HTVZ45BH5rDFQwq33gPOQxEIRzierCcGvosctTMoEK0C2-QY5XIVhLXs2OHSR5QjXgFn8M07org.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtLr3LtA_gUIiVg1CVWTMy0CwdESt-Y56xA79-ojDYxlnqAJh1AYRmHiaJsNjOHQjJRzRSoXOn2us5MjaTUsYQbXIuT6x_yzGD4eSukNj3fBp0qFScNCeXd7owoBmaigYCXX5pxlZV0GTwFh6EeKq-Ya4dhQTuRSHXhRaLcthTUmdS7zNdUflmZCSKHWyI_zTi_DHyoyCg4fNoAhNoNKd8EWFOhx6RBkwv4crFA022R-tyi0h5MB21XEDwqYkEqmu_brrqoDmHKdHQHm7ReaNUxojefxu618YT-08BV9FETQgsGi0_A_0lERfzKVHHv9kPk3m4_PPIuv-19KVjspYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NieqQkzXwwZ5LathN5d9vZFcaShg1oCOa4oGu-fZQ662OA6nB3j5XQAcpTPIOt8-pstdftZZS_0Fe93kBixkKX52tQ7H5j3Od3VXqTfzuyotL9-4b110FVVSdf9Zw5LCS7jcyJJsF3U0i19cAjjFDjP8a9fvuZSy_Qf2HV31BE9bESeauGC97KhNw3UJSgFGtW1ZNCYRFlc6DgY2ybt2IkM_hcKbzVAH-K2tNPnwy5IkMvGSQ4xwLmNZy2P49zrMPTXpoDs-havXHg3LlrqTb1VNx967h_j-iBm-jWpByonEfkDbM6is9O40g3EEk1tZAN5d0XLbq9qMlr8_U4tiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSaBIiwJO-QYmEVI1R0FdgxHe8aYPVx4FGIN-Ib6f8fhhif1jlOSLaM5XhcqQ3SKlGptxEmY8iUvJnrdwvmDYiR8XNNOv9r3r4xyakxTt-fZbneQn5QC2eghBxH11usXY5ySZlRf0yOy1hTL6KRijuQwwGn92B2dTDqGTxMpmGi8zMLVAkFoT6I3Gq6il3-Idphi1stzwMLy98XvZeutH7d_VkBIgCN5gekb1ejA4h-icoQ-VNvfIdt-GxH7ij8FnDlF3CAw2NGdKDjgFcBvZVzVzprAONw8oqPqDa0kAQJNN4lnDVjAf1AqHmt48fHh9ZH43d2Ga99L7Dhj50kdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-lzO_gDektH8eyXnZ_sTVz-AxOMYagWLvzgxRMOzZYus_qbDNePfQgEbksg4uIKSGrY9TzRICfSFzXO3zIlAnQ1zxIRouKLJqAEJY76L_Zmt_X1SNw-ihP3YX8qxfee21dK247WHOL1zsSEUc_OST1l-cB1gk3TTuJm471IfsbXswWpskuM3iTanf6bpnL1e-P3o5abghJZSpQ0NV0RollWVBvmaFwWh8G8E7FlUBjwhsxVVjzwSDJ8hUNjQDRCJjIuQabjouNtu06T_kVXNW4cSUXR-Hfad8SRjcDC-_YA4u77cM12XdGUaZDruegJle-iaVVBSzzlVMflWaOhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB_VtzrLn0NhH2fv3Xphd67YVDzQv5SPzs3zGWEBGGeyON2JBO9SUd2pscmcfRXua8AAxOI87b9wxpTvZjoFS-zsq5ypFIa_JRckcSH4WaK0sn_BL3Q8i2d8Se0_t3MBVUPcJoqFw9TnO7deX3aJpTVj66gg7J9YFnpYFACeG9fS1cEuzCMegNsb2svixFlPiShf4q37mJjH6C-hkLG9cLJ9OteatXZR83CQFgVGzfJjQm9MGGhLH0xMVFq27uVT3YXEBniMONR2ZwybnXfjXnstRAFV6RH2Hc7digKFjiGs9AnJp4Xk3dOIkUoXOxYrG0mYUsh5X08sixP3CQ_N8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk_vhRNy3a-WdMXoUo4rYA0FLxpz8I45ubVoUudpVCccO3YiT5pROwU4YN-nHmVQcJqSzvyckeYi5ROeO6Z4Gdka1d_QK6yQzavHTKi3m6I0av1wunFIqSTrKKF2P-bXHHNJGHBwXllnycwJxN-Y7nE2DU570CJrLq8uLJ5N3WQUDXmmk05VyTgZIQ1jCARwS3ZIBVgziFT2GsbRt1y6HmsvZ19cPXCKOZrpMwZbv5Eemf_cs_DOQc710dadmdzgV6SfxI0TNlwgfMo6ioIqzcSiIYZXsvYcOmPCNDIsYi-dxqmfFG27NvprzXnNJ82v90eUxEi3kSI5OWHdYQCQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY-ehDQBJng-lYfdq6y4IAIf5tNkNZvHbFBAmJrFClIFJHHkFfM-yfvzatl9vuWkrp8_ygrLJAkk2YgsmJsL4iPxQjkM9apATur1llqjePD_pzcx6izbNdF2DciV5rMR1cYYfS1ty2iPaIwov-orFrB-B3qwM9_fjrjKE5s1_N9RD13ax5KHJGfuAxjCoZZ2LBwJtAsK8uhfaiFDXLSNpHINa4oG7W-lrLoYcaxCrHOH51aDHiwSB0B4Qt1h9bhSJN2vpJvQ1lGcywAO-AJzaHmBvy28W-EwBoeCjrjNyrGJh0EOG3APqao_O4bIB0YhLbMMxpExyi2IRqHEpGguWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
