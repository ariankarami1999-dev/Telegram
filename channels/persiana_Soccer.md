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
<img src="https://cdn4.telesco.pe/file/VO2cJssef4P2YPvaPMVzTiAtFQHSriiDGMxFTmSqxnAysmVrTFqLS82a1pREDNLYYqTTU0wwixHQuNdNsj-GqwgIZ5OOSKr4W72I2bDqs_xPQqrt0NwrWBmEQ7wjYiPK6v7GfWjI0cnMPAWJrpdIrPRaMiyLrG3_z-AYfsUdjGszLGAx-esScgEeJYeL_CctM7nCKAlp6aqwFEENC2ufXofmfq32_0I7U66sMjxWWlWD9Jc2BVyX8CtR-JwGISGgQ-t70eDF1eezQ7851htifW2A3FegzVlsjoi4LhYQdPhxXMZcgI0l4Kuk84V7nE4HdvjPe9pAEpv_3BAKnLkLkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 512K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 23:29:19</div>
<hr>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFMVF7wnsC8SoOJct_qLDYECpVXTcwyDXCUwWeqyWQfmYPNxuZ8r5aXiZVnonBvTGJPbbxVcnGlfEuPHF3dEVt97vQE-DOb0BOVBoGcflpjSdyhNauGgtwMILmyDW-yZYprfAOi6ySyXWWYGLguvQIOF_tsr9kdejmftzleePf0jEFEcHNLRP79oAJEo_3xmUccGXdOfLqieHGQ4wmy_bcVPciBbAtHIDcFpkzP2teQ3Xtks3xeYoOS_DBYrATZ9dfi6fPnstslRTXE8-H-A9ZqXEtNQtD_VjanTcV6Q8ryxB7QFbiUntOa4o7AhBqV80o7PuINFFhAVhG85KWWWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZOWNuNt3nc78RZ1rQyC0plUZVwDtr6IHvuggIeTfYI2BZ5QU8EYjKyrabCkxOnz54KKNr_jQaqL0efKxm6L0uaiu8BaRzVq2rhETMU17Dpj4s0eB3J_VH0LQdrfIooGMb3eTdnQVNy3sreffAFLK5r_XAeIzGtQDL8Jhn7EG0WzaQXvqbmFMzm7c0lJM0dkhy4VU8sdZZaSBWrhIHwicKxIxF9mxhNz9W_U5q7I5x6HqDtubHF83ZOu6eRjKJ8uJtIIO2udbbJJux3GEdNgaG0HdZpdEM2uX1p9HmYOI4ZCA7mtMqrB9xdo-FUfv9Jy7w3K7UFf-CSm3d3wU4loLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=ZlAbhPWYBm-J1Zmw2oYpq6egbdGJxdR9cCEPZCNN3Qe_oZtiuHFBlZn2KgGLqsi8gf4Qros18gSP120krKMZ6q-weqfXvzL23k_0X4dpWZT6-lgfgOzr3C3odqqG9gdDFSPMAY9JJ95DP25_yAQA-JmkGMFjJPpvuX1lg0IwiNVepyyv4r9IKn5n12cGsBSXbntYPL8fvcuppoTmyzu0hHtCA_qYxJPwAedPi9UE4Q6kaHA8kDCdd-eroPNKVDXDu2hKT2xl5R6FMb1Rurxmo-auxxrjigpAOox_jHtz8bmi9UyNMghAk4oRSn7UrJDjISfyQP1f_z5OIoVUk8CFOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=ZlAbhPWYBm-J1Zmw2oYpq6egbdGJxdR9cCEPZCNN3Qe_oZtiuHFBlZn2KgGLqsi8gf4Qros18gSP120krKMZ6q-weqfXvzL23k_0X4dpWZT6-lgfgOzr3C3odqqG9gdDFSPMAY9JJ95DP25_yAQA-JmkGMFjJPpvuX1lg0IwiNVepyyv4r9IKn5n12cGsBSXbntYPL8fvcuppoTmyzu0hHtCA_qYxJPwAedPi9UE4Q6kaHA8kDCdd-eroPNKVDXDu2hKT2xl5R6FMb1Rurxmo-auxxrjigpAOox_jHtz8bmi9UyNMghAk4oRSn7UrJDjISfyQP1f_z5OIoVUk8CFOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6-bfOVJBBPcfzCFSXCuPO1Dz0lm6QQX-5_tQtYX_m5JRy5zTEb7cEmCXqPkZJNR-Z7asS0nUskqx8usN8VqF-W5e_AS3m70MAl7UqZO8CB97OZnTbnnRIyPpeUsUxp8Obm18Ts8n1haii3zsN3RepuQKcQpjY1mJYRMWq96UhmNGrNk1r0DWqPyZWf7Gu-GcdOsYnLB-5bDYTf8kaclqLrxx6dwQxtM3zcGfCgDvkBdmM8bRQdukcDqMeq0L9ScGWS052I73M9uRzMn3YgD3SoP1kWtqEEt9-7tfcQX32rtWbyuR6MHCkdrOYlZHk0pOfWSAlJjh_-wlO6ZRiL7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP7nv4Tueogqdx1A82Z7HK1-jpnjfmL2jIF9WXrcTbKINEavFSf-B8SGdeK5Is9cG4pqhYOygUWvxnOiYxddQDil4MWhTp4aBTG0nf4e8yS8hMCkn5DbE2Nf38O5Qn6PXQK2bLcms27vBdiqKNZ7smJDrvRSBPyj6vApvQDg3A3MhKFR0yK4HQtNMwO2gjMZ_3bhYB7_7raTq8y1azhVCu-ZkYRICoUOONOgrhYO2iTwZsCR7NylO1Wk5Tdlq8nFPM981DEDX2OM9uDzlawoK98fTZLzaWt48XVaaoGT2ich7TW4drpOiOPsgLeYefMgi5x2ZnGN0YX5PrdjyrFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25944">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT4GR775Lf9IvKuBnYXUVrd0kmwe1Wg3P9SH6QgH0ftxiWxBwgivzygaRanQ4kXnDdQgOpbzbpGO1T9KjEhBEmphn1KFSW24jRrelpcsFMRtyrDDw1IeR8e7yYFO71CnHw5Nd_hfjn-wnVvQOq_odFTRrLDgwHB64UpSKzEIkjSxzQ6aqwFSswKyj-t4dkWIQfldfedmUOuyxJuuOAowxqnih-zG88hzIdnq18IZc6alFl837bghChZ-VWinvZO9Sld827yZmjd7PSqyPo_faTsgpIKyMFHaSLvCzisYvcGSRiGQcGIhwdlLwFyrFG-xamFACa6BzIDsXqNgeuEZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/25944" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=iUKciMgzHsiocmcDNUu7gxg_BhBhHaXwihbYRWsHlZrrkC8363Eac6CA-Xoo-LttLSjWnGAMAeYbnYXS3YjWSsloMsZyLqanE92a6zEsv1z8S2GNDp8aC5iqt5Tm3USy-0HeUgw9VOdR7dsPUV_9XDxqeflN3a1SPDzxAXcUiqsrtzUsBAc8OaEFIeIPBFP19UAVc-kHFKIRXilVAFGit9VtlkemagBxJ2veJyIpjEL-1WWe9-jA13jXdZdDy7_LqxnjkEPaQ-br-7o22kdTSUAR63bFca3Ht3if6eKOguUMLHFJOZ4X4ntxbqfLwK9-irlFkWSNuOZbHof_sNmqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=iUKciMgzHsiocmcDNUu7gxg_BhBhHaXwihbYRWsHlZrrkC8363Eac6CA-Xoo-LttLSjWnGAMAeYbnYXS3YjWSsloMsZyLqanE92a6zEsv1z8S2GNDp8aC5iqt5Tm3USy-0HeUgw9VOdR7dsPUV_9XDxqeflN3a1SPDzxAXcUiqsrtzUsBAc8OaEFIeIPBFP19UAVc-kHFKIRXilVAFGit9VtlkemagBxJ2veJyIpjEL-1WWe9-jA13jXdZdDy7_LqxnjkEPaQ-br-7o22kdTSUAR63bFca3Ht3if6eKOguUMLHFJOZ4X4ntxbqfLwK9-irlFkWSNuOZbHof_sNmqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alGRWVYmul9sl1JYPSbTelcIFebyte3XqVP1yRg1LiYzahXATGMfunxtXQkorDLPVcR0Cg-KAmFZLSle8MSLV0JP9ee41qLzIevhlxxPzL-8ngvgzhXdmyE4OTA9GNYGgofb0syarORTp8hj3dQDhqHmhXk707f0OcfeEcbBy98Bs01IW56WosPUMbD2dYJitWcDNf93dIRVU8f46wGLXhGKqCTMXF5ptirf7ZhnmkyM-6OwWdWdELN8Rqo9Xki98IEnyHOEI3o4pz0p_pJVsonPsnLDw-HNLcX4_L3dga5KURnCMO1H80C1G5bzzhtapwSHS3DWJSqLEWKavlCQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOYOQoqh91OzBBEa5WEYFpWDA1JnklQai7fwysym28koUT9KzOXQIHcKZqoN_DGepMleNKW09Zv0_n2VqMph9cZFad7lOhOgXmsVyVrirAj_3gIW6WOi-j4x_lwS2sewDNGs641wC723JHmdERMWvc228h4X861tHypRtNGDQG9xWi10LIY0UMREfG5sN-CbtFQE2GJTECrGkdKzGD9GGc0pUTT4m3ar9j_119NRXCKz6PnHmbS4iuhpMLSqqLcYRnOQhBEEGllIzJKpnfVmXDXJhfBG-N2CpYUPv3scqg_hW_aU7h_YLqXwTILO7R7med_pMP0oOKYasfXnOgWGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBpnh50pdv0AA-2BCq_JG8__Mw-y_nulShVksAf6QV3bm8yIkXyJw_GwCrqDr5pgcvdSlctGctM90WDBZexo6o15aWYFPrTgf6YXTC-CFOJ2kf9-IETONoWJMEvBGhSJReGJOjKdVwShTOg_CSAkA9Ld7RIDRspPyNsgCQ1fnsTP31oFfO10jRnUqBkAcN1A5ApGEPzlqg6jutQTl82zb3SOXNvb8yH4drX17QUTTmNahz5NVMVPG18OPxHFEQPuNEa9zXULOedUJgQ9NY3M_6nuTLrKu-wY6Di0_LRfYiEbAKzF9Kt652T8wN9XONhy0FBBbk0QvWvbvhRYv94i9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVUG73lh0NCDK-Jp9gpKbfUyvxYIe-8q-ds7Dro5IVLp0JbzLwu-QNGFj72WQxz6wvAdYMSoBm6Le0ZJrGrUXEbboefe4uV8AcMvDZKr3XZ4vYqG2Nz8Dixlbv-xvue6_saHhN3717g-XqUqvbVKn4KJ2JnAvUitVvYOPzrQqGySQeZKORJizLxObDBT1LZOAH5CCYppmRp6mBJ5tjP6UNJ1OMk8e1NlT3IylXwTmnbU-Lq0voxvhGRRVhfJSyrcGLEbKAp9knEZ5_yXUQcqTJgARjyFwo8IrWYLJPZFZ2YSk4Bkjn3zxl5hWdr8GlsWc1fCPfl__TAB6__d_intaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huiAZ_Nki3KeEY0ZZaxFuIe5z8BZl_WQaKSc81qrohmbvmjAkcV3Swxh84glBLLPEqyOwJXG9T4dytka33c9eaRFWyer66lYxuKTDqnj4lL5krrmXhxAGuKzKg-lOmAJPZbcvNZGZzeG54tqhTTSFR-zkzJiJEnk9_YpF5u4tYTo3I3y88wM36jtkE3WvZjNTq2tvkAUs0zQaOzbbEfc4N7elX3lRCZ6t43JB5cQZA-vnMgUR9-N_j5o86CUHBHGxBvsiV3hI2TthGtcdi5rH1OqUPh0YxYFQwqjAPQG7pp4BsMINGzNseNlRfEKQS8xzDAZ5EneT5TJSSVcfhN3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6wuXWgcOg7Wd_fgB_lWzO1i9GZs_pRfAgLD1Nf5oObsLcvKpghRNiDzbohbz1kKhRxSe-x3936fOo_o66F38vLAvoL6gRTYi7XBbZvqMX3Wo2bouGKiZxZaiVuvgHSLfqAdKFtyw91EuQsrWH-PeZYrZod09IQJw-kiRBP3Uc9QwsAv2zw-ECnx16TXhMD2u6RF83UvF1o2u_FlS_jZ7rrUb6cJzBd3FXihB67DPEm8ZUUZLCA3izCMJLnneUsdAaVk4B1Dd8ji3rnfd2H2py2aYs959lgsOzO9xWWyhBY-IMCvD-5VICDGXzd_jyWOn4pgcMI82m0jH43HOWtHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5_KiiqH3LDUvuB6H2rcrakvbMMXzOp8vUbvteXh13K-tsoCTgEsHdgHKs5hYJwz5GW3LYxk3737Lmhm64fHM1ZrwCCyrV0AWByeZcrPcLXhyhBtd3siuX2zFJQj4OkmYMLPYjYtXSBpM9f6jutf9mNEvbswccf5E5Rb9m1WhB6bewTUt4dzZG8rrjMORHLZCbKUFSK1A0-LbU6keWR90NX9m3v1ts4lqQ-zcQH4yEfi-IoVHmMfnFv9m0Y_OjfmSdc8JpRDGR6V7HhYxGoA_ziF42yrn4hfyzW1ecYv3ipb8bSznnMbU7qkUuXrMbrUlb8JRdMTsMxbIjhb2RV1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afb7_k6CXkNJeNl07Ulo6wIh5orl64yQ6Akakp9C9EVY2hwDdNDqjArQKvLdL0UCVcgTln7viitUmiJIyR9iJEnScCxcIG13qSkQv4vXYxYKVGAW36617_GGq3DsRHFL1Mc02Ir54TvRXtTHVnji-6lThYpRKZPukEo_Fal72AjO2YNROITuoGA49Al2OICOKVduf5ksYx7WHCHVQDOWBjauFkCiVfXGzC5VCmrdRGyQh7elco_rS4taUXdf8t9pm8BAGV7AEFyOxU0OpzpuE4yXkheK7nA9SVY2I-iPEfaQiY5FibC_5tV09BC8A-ZpSGtikMwZubUl5t__V_DSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYxwz40VJAKZW-Vru1CjCsxNgwkJHxRycpCtyagqzewhbrIICMLSc77XauC5x2leRrxyZcMmXWRTI6HL7EDb7iTGGKae1-BhZn_JvSYKBA1F_mfj2OZAQkIeeoLNResqTWv4vI5o-wDmMmFgLLVoN-3wpkL8r7iHw61Nzk4_scXkFLPuxP1H0u3Ie269IbhQpeRmV33BAsyOrAVaynSiTabzjy06-WpQnRIo2dXo9zEffeFeg12zKeQAHTltaxz6YH_2uR_jUimbkGqzTaHNfzcGctOi9MFE2WDzQEXUNHdnyOI7-hGysR5O5LhNJNj6yjNBlYkc_cRop3BDZIWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biS5Ywz7qhof6LqoCA3uBVcbZLLNEgnra7vF9UBGG_WVZ98a_FAnLz9PvjRAFpuz97j_UXk-qPja4a4Wxa33BWtFibvvwu42vbpHngN-sg5Jop_T3h-fN7YizaXMqFgwFO5adugI6ttW-AnTtnYg0etOQ0L_wEW3Da0KN1QKgOlOJUfCc5zBviAlxHhIiSC4FKy8VXf_FQSYXX5fg7m1xsUz6kf5YXXDemdmU5_nKrsUXJ0lEZzy_Ayuz0ylqNv69lhnaowKmXQHd6-bsDVmPHKm88g9QJtc8j_gsitdQ-c42BcqkFYdrs_H3i4p11KYxmxMS3vl5fWligHMBtxs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrmhroM3OltksV-N2HXG5Fyu4eEuExEL8qeQ0yEAMbJe0JApxN0yR7A3xizeGZINe5Mt5WhYz8sh_vAhIFaL15pOEPpABsYcUU5jHtYIfRglsO9XYIQAksJSVPLQNdoVixQwxpvQGJVNQsQEs-4khNj4KaKL5rCnbqPLZVbz--qno9n5Z8WQfqEcB1JW8Q6oyPPjmxVCETeIqVdIYEGgHier-8aNeTQqPCo3kNTFZXBNkPzL-U6LRzVi9hNpdaIHGk_VU7DS4buKEeB5t_oZ5sna7hUSlYVkUqxREYtTUvdTLnq9UaQbOutMXDPgxq5hxeF8rQtda0oLRa30oxSkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-asvDoFw8RCEyjgFhXkjFi5aFE-ExDlhUy9Dklcel14FTVCEwd0S89t_kqhRwcAZJDjnhpXIxx1QIYG-BWl2dtjiGywFbPjffnSk1VQkwdqlNxtsM6MB66u7LH-S7r0MqB40TD7rI2iqZcO25cUQOQtBosYH9934as90JZo-JzFVNL5rCKRQhTuil5Jg0yEplEfwNgo_n-dpxybawvL2xxE0J1gFpB3qhzI6DuF_cVFmGDEEb9SiRfkL_8eET0Vnd1wGXKNbugX2wWXxJXD88-nVV1mYuPUSL-9LjR05OJjCMFPDMvja4NhiksBKOyk9U67bYDZmOmcODIaynr7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSfPM6yUx9x37hkNJckB3gvbihuzY2hX0SfmNgLePtCBzDVs30BjwiwtqPgr7uTeo3QydQ_jBfZbHvdicnBeG53EQChFgScu-VjZvdi2XsZVLpK7fV0Jy8hFbNNJuj9EHvNHnbF9QTn74Ol3V0LtqZ4EiGPO9N77oAaAhnTrjerVM_cOLzYQNcnBqthq5x9ADtNDqvDk46nHR8Pz7Ghcy2zJTOib_Qqp8GyFyQi12ZApxJw8ba9-Sgk9Xs2IwUXkjdwhSo7Glk1UIVRXxOtld0UUxcAaeX3PX-qo-NrEfHZqlvgQnclQegwtigWIy1AktGL06fu5Qk2DOQkzOD7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unr3z-bRva4d-mGyAS2zneFhedZ3ovXfsxFD2hU_aSlf_suonjPpVKjIVzB1AsylicMsQ7QxEf0-njUl_Ii4Umw3hko7dzzRGV8v6hvwLLJ3bFB4f8lPNeemLQVm8twIoodGU0ntdfhOAtcNOwGGjpXcemhGFLbbBeTD8swdqD_jZiGu8MfjE5J6zTS21JWT2PeRj6_9T5tqZGHPJarhHRRnMJ0fmMvZO5lP5STq9mod2-tzOxp_u4Ryje7VFSh6Q6kFLfv1cysKdUvsXOXkDRYwVE-6kMYzIPbpjm-ZOOCk04hC5_fusGZ0FkQPkBA6VCm9ra8dWH-zV7qibKiMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=H6h35Tsrnkd1kfTHGEBjYyssC_mt3Y0-MnrvTCnEPF4m_V2H3VNbWdpbxAqTtlR0izJ9CTXT3eB65gzjqdna_C8HC_1SwqcBRrggWBZq50ivfvmHabnzsnjDL569qGBVE6AR1Rk0XVK5MtV1bCiiYnGwoFb481dYRBH6Pp7fbX-QirptEA62Vvh-H2OJ_o_LwH73NvBtGBl5Ac-nRARpLv4FUpa-M_aaNNnefucM7Kz7pbd0FU6mLxmUo9ipq5v2glI5z0BDwAdKzOSr_4z49-VRi4NxH1dITRtRmv-NKuloQdVyNsnTMS-oXRB3DjdNOWloo8rMtV8KQsAKuVGhJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=H6h35Tsrnkd1kfTHGEBjYyssC_mt3Y0-MnrvTCnEPF4m_V2H3VNbWdpbxAqTtlR0izJ9CTXT3eB65gzjqdna_C8HC_1SwqcBRrggWBZq50ivfvmHabnzsnjDL569qGBVE6AR1Rk0XVK5MtV1bCiiYnGwoFb481dYRBH6Pp7fbX-QirptEA62Vvh-H2OJ_o_LwH73NvBtGBl5Ac-nRARpLv4FUpa-M_aaNNnefucM7Kz7pbd0FU6mLxmUo9ipq5v2glI5z0BDwAdKzOSr_4z49-VRi4NxH1dITRtRmv-NKuloQdVyNsnTMS-oXRB3DjdNOWloo8rMtV8KQsAKuVGhJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRwktfwSrdyAjQKbe52zd-JoCOfLvEDh4XgTZc8FYt7_pXkNsA7RaraxkiWoZHedkWMdtnbZLpP1RsVJKC9cWylyqzKp8oCpui56Ac-PQZrd-gsqiDQJQ4basDN3YI6ZGFPiRgJ3s4HKjAZXpu5JdpBm6I8oU0vVQOQQXh5xcF57iCN90qN9D3dKxQCaYdSLWeFb-9S3f0KaTpiX-PH9i4cfu9VJr99xROewrSczA7WZn3SeViqShvYXqpxn5ugYY9vaWwTThPhLcBz-zpCQJCejtuQWypQFF9sXvwW9p2Zm2lG2KbCDb7Ew06InUxleS6FjFzYj6mtHkmrENTYWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=ILS9XgTF5nimT49i7Dn7z_8DAgRS_HzpzhhAW4FU6qhCKULRFfAclk7-FYfe2RLt64YPnugZdxUvPpgD3kqdhEYaqyw78cLg_-YUCHvtW87FwJz5aVKHLdGxhx-3LsZXB7EBHpSFhQeL3EvC-bZCrRKago1__mOLDYEf4yLoMnqytwSoyi9NnR8gps3EEIAL9pdtx9_SG_vSS4QcQiEHDTnWBlfCqJNiiKf2bysiJALLjPqGLuYyjvygr_caqclXk2g6lzCg0SqmaNGhEU4aUA6a0oWtYlaY8X3OXuHqQCWcFxHD-05mM0T8kZAy5kc7O0PDroHERuHzC8rb0YlbLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=ILS9XgTF5nimT49i7Dn7z_8DAgRS_HzpzhhAW4FU6qhCKULRFfAclk7-FYfe2RLt64YPnugZdxUvPpgD3kqdhEYaqyw78cLg_-YUCHvtW87FwJz5aVKHLdGxhx-3LsZXB7EBHpSFhQeL3EvC-bZCrRKago1__mOLDYEf4yLoMnqytwSoyi9NnR8gps3EEIAL9pdtx9_SG_vSS4QcQiEHDTnWBlfCqJNiiKf2bysiJALLjPqGLuYyjvygr_caqclXk2g6lzCg0SqmaNGhEU4aUA6a0oWtYlaY8X3OXuHqQCWcFxHD-05mM0T8kZAy5kc7O0PDroHERuHzC8rb0YlbLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuB7Lo870jOcZb50bu1Vo58KumfxWoSD-Yh7kjXx9wQIf6Ga2QV837EKTcL_AnXTUF0idw8CEdc8KUrjtvamdlWhcEPRoZRnGUQo42BKb9tvDStEI2iCBat0tIIoXqg-tu-ORDW4jOdXZOBNUE440HlaVJNocESV4MynO8hTyEimPx4BFgt4bqf4zgLO9LsZgnfhboAA4_0d53fKamZc59NWumCT_HD0hMuXXp0-bPmSS2jTPW9EKOXbd-zrzGIOKBdt7wylimFiuMWyYr0t75VNdTa2V2GjRMBcL5UhwMDrxL-xc4Js5DdCXFRlZULO1ERVLmc2wpriASb8c3_whQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epQydzNd9EDjoDb2RPdC8iHTJ7qhWlUAFyf1n7YK6-1GJYmZiQ4KD2SmSfWjPzS86Ky28bf2TXGOke4Yj7Y4TQybUBiZiYg-66VSy46lwe8r5NeehC1aJACiW5Ma66Qyrnq_Nn_WwjJjmVPwwNAuDWsP8i9QSngNcvHDcr2K5fNo4vzxVk2ZAZoEkjKO4pizW1BGk1wifzYVUrK4jBpFlDmpRhOOzJfliRMxkhw3XbjOBFYHGnaldL3pTi21HfpJHkGbKCuShSuh6IsUH2Sea3VGPGV1GRGtrBA-MftOiP5vPNHUBYr5ioMx32cx96IAjcu2_wIC9Y3uM64qDKkUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polHdQ935e_pGQv67DLjP14UAZLTUGvokZKJcjn_fNLIziDmoAZg1sDPxKSIxfO2Mc8tSCWIFPDl7PJJTHa_5izIpNd7II_-iR5lqRLiwL7rD8lvnlhF3cAIbkQAHIn84c3iu36qsqZTKbKhgGOKPbHCqzBePngrsg5gxfqmYvaBELDWPV7uauJfmZCUHkDJhITPQP00fIByJrf1x9jk2N-qspE_HSG7SPd5mhBAZC0dOVB-ZDyKZ3uXNElgjT6xNjBxUnvdy1yl4BALOPiTielEn4qyhjAuV9ezpIeGVvHP1gNf6clOGCHTOkUko_qeCO5f755ok5LId3DoJiZdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFRKBwOwshsqZDrk9u_mPjIXEc2bzj01wDwWBFCUM7a2T5GCT-btt3H61TXC1LhGi0YEE2qo8sRyupio4NN1MOVM6O5LXv566f06t-FkMgiFbAexMalibwIrA3DjoGRizbtRScxN6jC50ACJk6hVlo4JRK1ESTd53tCRJD_yGnQYSf16UQz_YOwT4vRifVm_FNkuG4BOHfYt5s3SYr8YqSUJMcjkdMNlD2qAx0PLNOMUbund2cTO3-CXSUJNv07a753-gnBRjPASz6BWvFEWmqDgigplH-FnM-LnYp2OmsdKcDAd-O3peoH6f7e7XbflC6LIaMs9LEoP8K9IQuUw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl0_I2nLlDENC4-Er6BiHP59BU-46gByp78P3hUDa2gDk6qo2_O-_i2hxaLPLGgfQWjaoTOYIjrsfAEtqavy8LnkJLe8J68VqP693Sf7Nd_GBZ80G96fbGyFprlGrQG13CIjbWz9KuQftyempBHZ_Q_720XTkm0reaeUv78AdMXwexhl2CVxeWU2Qk_ODl4rf0JBobOkCsFjEtp1PhgNKNEsa3qecKw_BaEOKKRL0FFTwu8Nd8xX6u4fRmr57ekxFhS_rNt3ib8PFznP44dy0A8yw7Cb1dMvhZzn_I7zL6rU_v2snwfmBMdxeQ3kfo7X-sp03s8PYZdBRW7nfMZQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=UGzhoGjAQU324oenVao2vlKw0MeZDYW0Bp-nt64QrGrV3z70G9zpomKrRPAhaFGep-UvDLLB8gtFFMTP4zta5EqCNfo-ZBUgGiTZFFgo_qM0vZjEl6uiEIy488zETPkp6_1-a2hrgC6Ixi2PmMyxUmHD3zDMiVF_p55rvExyTKpQwUuTCKlnbIzy5i3iZ4XD2cPOdogy3mbd8cDq-rBvVT_7Bf31kGvwbfRsxIYW4kuKUB6V3XxRHcipNCqIiaMeh7NuL3unJjCdp4jaWYBDYPjMEXg6pY8tBDQNrBSy_A-GRTtjG_aA6ReYdts7dSnPN8Zoj5Hft0Pgfiw63XQ5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=UGzhoGjAQU324oenVao2vlKw0MeZDYW0Bp-nt64QrGrV3z70G9zpomKrRPAhaFGep-UvDLLB8gtFFMTP4zta5EqCNfo-ZBUgGiTZFFgo_qM0vZjEl6uiEIy488zETPkp6_1-a2hrgC6Ixi2PmMyxUmHD3zDMiVF_p55rvExyTKpQwUuTCKlnbIzy5i3iZ4XD2cPOdogy3mbd8cDq-rBvVT_7Bf31kGvwbfRsxIYW4kuKUB6V3XxRHcipNCqIiaMeh7NuL3unJjCdp4jaWYBDYPjMEXg6pY8tBDQNrBSy_A-GRTtjG_aA6ReYdts7dSnPN8Zoj5Hft0Pgfiw63XQ5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=YdrMBDm6GRGG6QtA5GxPKcwdPdK7vSxwEExcj-HD6u8IBiyYdaeg3K_Wn-Q9dJBsXUvuni8clZu7UYGjVGCo1eAF4G-cLE2K769ppTK9waNneZ-w4Nh7qV20rzXIyhtd0YxQpzCxEqaBtouIfQxVWmxW7ISH29FZyalTXtikLLkjopdqzBEg8anrTrvM1b6LlDSlhtuDYCEFZ9l9m8mKoS41BY4-elx1Sslgv4nNJMkAvB0NgrsPtVNLwpGG7hIDmVgV_gq_gJKj3_kQvPe2LK24FJGSC6lQznenT0eZNPydt9TKYxVjPeAusFjCuoi6wk8USPZmjg1MnzvHyjd7wa5DYdycVwUX0m4MNBTGwU-pF4pT0cSl6HEDy0vGFbkJ0q9EHyHjdVk2Jr4w5lXD921ht4KNXUdhSpgQlUW2Wp_VA-QDH2MqECvQj3AiAytpti7t1njx4T7VKD6DFLj1mQYWRsrRN_TTF04vVNbUCzbf17OU1BXn6E92hWZAC-u3nYkeWkF4RYFW9WKUzu8h5Vrwt7A6bftlKEWV2KH0PxJqJMXKXtf8uDNeGvY-CQhNnpyGt8GPrDg7u0YWgYIm-H9Fh1bfWV3DxDANX0_04aMSOavXUElQfRMCcNEbQJlNhbrwcjcNcHMD8YGem83JNg9yj_q2tNOP82Mn8HkujKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=YdrMBDm6GRGG6QtA5GxPKcwdPdK7vSxwEExcj-HD6u8IBiyYdaeg3K_Wn-Q9dJBsXUvuni8clZu7UYGjVGCo1eAF4G-cLE2K769ppTK9waNneZ-w4Nh7qV20rzXIyhtd0YxQpzCxEqaBtouIfQxVWmxW7ISH29FZyalTXtikLLkjopdqzBEg8anrTrvM1b6LlDSlhtuDYCEFZ9l9m8mKoS41BY4-elx1Sslgv4nNJMkAvB0NgrsPtVNLwpGG7hIDmVgV_gq_gJKj3_kQvPe2LK24FJGSC6lQznenT0eZNPydt9TKYxVjPeAusFjCuoi6wk8USPZmjg1MnzvHyjd7wa5DYdycVwUX0m4MNBTGwU-pF4pT0cSl6HEDy0vGFbkJ0q9EHyHjdVk2Jr4w5lXD921ht4KNXUdhSpgQlUW2Wp_VA-QDH2MqECvQj3AiAytpti7t1njx4T7VKD6DFLj1mQYWRsrRN_TTF04vVNbUCzbf17OU1BXn6E92hWZAC-u3nYkeWkF4RYFW9WKUzu8h5Vrwt7A6bftlKEWV2KH0PxJqJMXKXtf8uDNeGvY-CQhNnpyGt8GPrDg7u0YWgYIm-H9Fh1bfWV3DxDANX0_04aMSOavXUElQfRMCcNEbQJlNhbrwcjcNcHMD8YGem83JNg9yj_q2tNOP82Mn8HkujKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upDnlYB4OBx8ZN9o61NRkZWERhP9jiRrJkw4w5JHtSgHw_U2fFcUg77l4uKk5KYQuWUs3yXJPQzrpQV49E2VuuDF-HWJW5t-em9JcK2RYBe6SC8-itdrQE1XLRmsRC1olYb0q8XHeciVlec11d7JXFyOtjoyrzzgaCHDlZy3OotOOKSJfX8ghEyx_2hsL8NY4jzpDiuZKivg6o3MzpwG3acodZIPSXl96H06FJfEAOhwmf8oX_gLE45e-CpR93ZUWrT5sRmkHHqOpPsZigkeCxlPUdvVEGCRDdm6ln0Lq9PLNMXXohM1IIlFeNDcKLIk_vsqEL0eJV9wevAg0m7pBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr26
📩
@winro_io</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25912" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbTUu_sT1e00s5O4lxvNBwGDLyHMhe61OydhpHPioOG4uTpBGA8SBlYzh1679rWj9hEAiLa8imWWTIuKu9SVFamAuR5jYtfymUup811O0E3kWAXsUESDU0L65P5229R33LguxNCO8_1UMB0zZ6ABqbbcBVV1ukoXrE1FiMrQbPakO24oWrnrPnwW51HR1CIGOhIzCT_IoPVdNk-O2RpLhBvLENYSs8zIUYCm99qfyMZZ9HsZ_mE9Ab06n1iRFp18yQ_oItyT3Qx5fxJ80P6VNrlt80xFYKh47Vd18Cu7EyVRkkPqWkKABre1KbTIG9sklyHqTFjxjHmHo2fQf8LjzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=EhjOcIKAJhGeJjJojjHiochXBTmf6UXXJiZZfY_kJ95lsfhxsIowFoNsWca5fQuclQ2TUlhhUi13vF9vafGXdg1SbpIuPn51lOlb9umZZrakkAtOfM_pwuPujvzgxkFAurupk_FyQ-s11J-DofvYiQufgbTfLxqFHpIEo0Tz4KJ1iqy61fkwarTcwZAtGd10ZDZv1Qg4Y4AO05G6weA3JojorNKQtz56cqc3sp9WcKo9cNLgsNIH_4NgEnzNFiTcIO8iiaqVFdDMithEekrzCx1HHzQfirFRR9jgTvt3Dc5rjM-TZ_7Y9-ECoijQsYbsAokwBWlnmf2WiMmFPH2nyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=EhjOcIKAJhGeJjJojjHiochXBTmf6UXXJiZZfY_kJ95lsfhxsIowFoNsWca5fQuclQ2TUlhhUi13vF9vafGXdg1SbpIuPn51lOlb9umZZrakkAtOfM_pwuPujvzgxkFAurupk_FyQ-s11J-DofvYiQufgbTfLxqFHpIEo0Tz4KJ1iqy61fkwarTcwZAtGd10ZDZv1Qg4Y4AO05G6weA3JojorNKQtz56cqc3sp9WcKo9cNLgsNIH_4NgEnzNFiTcIO8iiaqVFdDMithEekrzCx1HHzQfirFRR9jgTvt3Dc5rjM-TZ_7Y9-ECoijQsYbsAokwBWlnmf2WiMmFPH2nyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=FgBZG9KF42V-e4AFU5NreITI8TAj_o1eGVpsK9WSa3mAGQiN1xaVH0X7QjiQMJL3CcgJXaEaVtWyHuFKGuCSkP5G982P9kHZfsFflkSz9hL-98e7mYGYT_Hv2ClElo2H3kuIkxsf70KnmwoK6N4cZ_X87drX7sc9iMkLKbUeAgC0riEvwoc891JSvNS1NOXo23-7DQ9fiidtc26cgr-5Mc-9NT714yM07nmOFyo1NgPvUMZ_5xjJUwdmW7TDFeLxhH8t_uCiTi4XsnDQ4omgsblDKdIuZG7OGHg5tPDg1P5LgkTML_k4CAzTk1Ca-ZmEVuHEILA9x9b2r5mMP_D4gTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=FgBZG9KF42V-e4AFU5NreITI8TAj_o1eGVpsK9WSa3mAGQiN1xaVH0X7QjiQMJL3CcgJXaEaVtWyHuFKGuCSkP5G982P9kHZfsFflkSz9hL-98e7mYGYT_Hv2ClElo2H3kuIkxsf70KnmwoK6N4cZ_X87drX7sc9iMkLKbUeAgC0riEvwoc891JSvNS1NOXo23-7DQ9fiidtc26cgr-5Mc-9NT714yM07nmOFyo1NgPvUMZ_5xjJUwdmW7TDFeLxhH8t_uCiTi4XsnDQ4omgsblDKdIuZG7OGHg5tPDg1P5LgkTML_k4CAzTk1Ca-ZmEVuHEILA9x9b2r5mMP_D4gTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=Ao72jl1H31DJq8eUt1DFbz3tJpP7UHKSflBNLs4-1LD4STXlbxUVSmTR51nwdoZVZMDw_QKqKj5-6ts_3Sbs9qkCQeN3ec2w9qYPozAKeoIv6ifkrEw2ywNry8lOfFkyYC5X1o-q60CnZCHSsV9el6VeKKDhTPgceTya4VmbnL5O9TwVDB50F5t1gZYI_IKGApL_mEnaB1-legJsvOw4WB8dUamCmsWOcn0zgPd6j9zK-fozvBmbYoX5SN1KxqKSqrikHfhByRLJDUTKlE7-BG48vqsi65KgfZj-zPROq4bpuSSRB0gAtxoPyF-NsvkXJZ1XQiItbWGIF115yKIMa1vxAPFCmgvA8iFfMCI2hLV-bZ60tDn4CfD5AED166cCUmp0ZhN9QwVC-a-APTFYNTA5LNP-gXt2ZJdrCdc_9r5Qc3fQ2GuvvDHf-LiyvHluLfmQEfr4HD3YuZJQnrH9kR9099vorCcSAPy2219LuUhwlx2DEzWVezXZVdm413ZnPix6O6A5-235yFgNnHCh5GF2WcjpLpsiWHqvqTPP8I1YgFCu64mp1GSft2EY3mq1Y_ZzZfmk5Xz_4DjKp-nxLKwHQycJ9U-_pQP2s1lQNofiZfyc8lRcqts49B539Nu8h8pt2VSSwxP0hJo2OFkKdf5E5Wk0T09hZN2SzJrtWBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=Ao72jl1H31DJq8eUt1DFbz3tJpP7UHKSflBNLs4-1LD4STXlbxUVSmTR51nwdoZVZMDw_QKqKj5-6ts_3Sbs9qkCQeN3ec2w9qYPozAKeoIv6ifkrEw2ywNry8lOfFkyYC5X1o-q60CnZCHSsV9el6VeKKDhTPgceTya4VmbnL5O9TwVDB50F5t1gZYI_IKGApL_mEnaB1-legJsvOw4WB8dUamCmsWOcn0zgPd6j9zK-fozvBmbYoX5SN1KxqKSqrikHfhByRLJDUTKlE7-BG48vqsi65KgfZj-zPROq4bpuSSRB0gAtxoPyF-NsvkXJZ1XQiItbWGIF115yKIMa1vxAPFCmgvA8iFfMCI2hLV-bZ60tDn4CfD5AED166cCUmp0ZhN9QwVC-a-APTFYNTA5LNP-gXt2ZJdrCdc_9r5Qc3fQ2GuvvDHf-LiyvHluLfmQEfr4HD3YuZJQnrH9kR9099vorCcSAPy2219LuUhwlx2DEzWVezXZVdm413ZnPix6O6A5-235yFgNnHCh5GF2WcjpLpsiWHqvqTPP8I1YgFCu64mp1GSft2EY3mq1Y_ZzZfmk5Xz_4DjKp-nxLKwHQycJ9U-_pQP2s1lQNofiZfyc8lRcqts49B539Nu8h8pt2VSSwxP0hJo2OFkKdf5E5Wk0T09hZN2SzJrtWBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkgPSviz6LJVxcTK-BOkVGRzTfsPQSmk-f8u7jjjTe-CRyqPWqmjGrlTbkCzBTD6M7Q0X-qqXO7CIbBwXGBcqm0REchD6tBeiU5dpzDceiSdRGNldHcNJsqOZsEglxP3BYyfCrSqEMxBUWJKIJf4g6XgxvWeoW7dZHRMeaUSxktrLpHZNnkxHKcGKeTMztVbBOUtIV5I4tYkav9e43EAqhXhKLV9dZ1P2qgQq_SjWlaYGEWKB9yMelozoXgwYRT1XbRcAGha7K1vdcIDZb7O0CU3ENybr-tZRt2OeSYa80jKUANuVlQcmPPa0bZ66upvkxSn5YQciGmOVFQK-LZDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=ZYLwFkR1jm0BhHrBUpR5BBO-OPqekvCfkhBumrj48mQFii7IDkS79CIbqwbX7dJDSRsG6l4s6LVQL1trHKZfVQttpbYNCM0c56aDz-icD0V09bZsZTs5j9TEi3hTfSZw6RJqH-_BuD-o1SePFDuPw2fEYyF6loYl-D1mOi4hoWam0XpZq-a5kP3yz0d9fXHpurR7RL1C_PjCIW2fia2_bONexvayuq4D0SagYqKUaN_7bPvDAKLQxpt0O0REhI58Q2ur_iDr4bVlJ_9S_yXJYiDetqlRFsMGxyLgDfyC3auGx9iyzPkrSchThozb0kWVmWHoM8wSXdechFY8tVqZ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=ZYLwFkR1jm0BhHrBUpR5BBO-OPqekvCfkhBumrj48mQFii7IDkS79CIbqwbX7dJDSRsG6l4s6LVQL1trHKZfVQttpbYNCM0c56aDz-icD0V09bZsZTs5j9TEi3hTfSZw6RJqH-_BuD-o1SePFDuPw2fEYyF6loYl-D1mOi4hoWam0XpZq-a5kP3yz0d9fXHpurR7RL1C_PjCIW2fia2_bONexvayuq4D0SagYqKUaN_7bPvDAKLQxpt0O0REhI58Q2ur_iDr4bVlJ_9S_yXJYiDetqlRFsMGxyLgDfyC3auGx9iyzPkrSchThozb0kWVmWHoM8wSXdechFY8tVqZ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=S0npubsQrbafJre1f5X11AjUC9qi4-lSkGwiHG3RgzeksJ0ljtx-5Ii1HtZJbPG996e7jsLTkd20qf-wWDMEvLgL7GfosMlml3Av94xOiDGZbiEMRT3PBnBo01dYmTVOUQxk3qTb2GN3Br26vDF2iJ3Ogc4pwoQQJR6olPxy03Ks62Rgjt31TRDQTeAOzdZ9kpikkln-rGQrD0-5zCVj9hBeuWmYw0Ds8VAPQZNSZh5AnCk2jjfqByIokhSv4fvUWQGgQSrqa4-y_waqbVo1XBioTaNRpPPDwTiJSUK4CbpMJd5w6-1nP4WTOmb76wVJA57M2toe5C1MRoDvKGBtvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=S0npubsQrbafJre1f5X11AjUC9qi4-lSkGwiHG3RgzeksJ0ljtx-5Ii1HtZJbPG996e7jsLTkd20qf-wWDMEvLgL7GfosMlml3Av94xOiDGZbiEMRT3PBnBo01dYmTVOUQxk3qTb2GN3Br26vDF2iJ3Ogc4pwoQQJR6olPxy03Ks62Rgjt31TRDQTeAOzdZ9kpikkln-rGQrD0-5zCVj9hBeuWmYw0Ds8VAPQZNSZh5AnCk2jjfqByIokhSv4fvUWQGgQSrqa4-y_waqbVo1XBioTaNRpPPDwTiJSUK4CbpMJd5w6-1nP4WTOmb76wVJA57M2toe5C1MRoDvKGBtvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLFu7GeOZvUkzOjFSYFuwDrFQQforQU_gZKqxlpon8HpXWSnzaMb9KqMMzPAST-SkNIqm9RlDdnhjDL4_vw1h60Ge_tnrlzP13R2f_joqw6os1M2JP87CRUaM5fXJJRG77EOjp_KyGrlZ6JSwLhXSWEN5nGyaht7ZR1cLFiJ1lmBKk4ARos3BMGsq5tSmp0N_gnFm__rAzuDBlZMTqLy_o2CFypBUqJNADXMdUak_sZaXYlYnDiSrXYbE22rPhaN-T07F_eEnf6ndpbrvo2ZQAtVLMbcG8h6Os82P0B5zktvz1PmZfrbRsLniokTXPWxf2SXYCiSK7NSkAsggL2eEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8tgkymiF1Sv8O2gqpOPGbaaw87IEfi_9Zlh0Z0GbPzW4ni3Nphw2zDAKHJd1fri7QfL9d0z-1Z9cdxC-U2AElPqo6vWYV7GRRtqxX3uRKcJwoMU2L1f29fTmTQe2pEaKjVfDXvjOo5UkwUabbK52sBQl4JxEo4yR1kpC5ksdlPgjaN81dzZ0L66qygbYyrr6gRiq_DDyWj1-H-AvyrYoZNtblWMRKIRTd3f67lK1az91BA9nzq7_FKGWdaYgb4KMfBa1t81obk4oz8q0ro915GxWFqTB2B-NC_jHt0zC5s2d1u9oyQ5yl4S3nFOUjCZJN9olp86d4aI1ApfQ6oYzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLySgEV4hb6GRXvgycsbckpooYxe28CNaOX7a2v6ihmXo4SYQ097oOyIbGfA6NDCaQSqCX0Hzf7SeTM3xv8KZrF7qyKbhdWy3Cqdzf7CgXEysFWiJqWScvpogbTRFGDS4svHv2awJH-tUVC9P7JmvkCWMqRk-KMBna6AEDH2wtiZnL6b9vTwYT7xEX4Y74y90x3cgzsDAXYl2cCUvlAiVQxXqBEWfmhKP-ymjOuWd4govfDTcf5M2afJou86LLjcidAipYeJVsGqVPSBaA7YHBpCPBAyiSZUOZxOGCUnG-ahaINzUGrJMc29rzkYdFIc7KP1zA_DipaLtEY95ryEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5ENi1DFs4meeXrWYlTn44NpWvrZ9LQj72pM29eRPvNxU1zZeKL-4rG2QL21DdByfU7jDInU9BwpAyu0MPgsJ2A1uQvKZbcwvobF4jV45_nemz89rhNFaJu5F5xSqv8NgRhdCVX1mi136uZi6gOISk8gqFBdFgIfHyuuR9YhaXzJOSF2_oyxMLRlYBxPcdiEflIHVvHnZ9jQo93EK6hBLny2nLZQaGKJQv_8_nCop68qYooQ__wKjGFTqhZdGlUB93FsS2cIRMLW4CZs70Ay4cz404RUSKORG77n70F9dC2oiEr381SE-9igVNPEY8AUdTKfJ_YoucrxXJ7xsP7Vaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvZNRcgDEUSUSDGYSgPnm-CKj96pYXf6cNklzXtKNS4EXtjcPlgdw9_fSmEhDLM7Djv7s2ajYDa0cnVwxfJCrz7D7-eYaEjBobvAzqyd65YNHptzgy3G_ohoH3ESjFhuI44ayC2bsZfMflGI88oN7qdTxX9VYUoNcoetYPwrRPsTZJ3XPXweiQGlGS4Bw_Oxh08MgdF3dIy5JtO267-_XfsufeyIAPiH1t3mzCqCI2CkYGpV8zm7yd8wmuic48vct8n8tkf3P2dWE89mPNE20LY3sj17_5hqUk6ougmzhaYF-EsmCpFThmaj-JnVCdLw5tcmVGjg5diRXu9wgdl_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTZUtT3p2WzU2lA_3reTiW9-ZQ-DkOhkgABrMGFbdZWicjQV-pySd2rC3trFr8f2KKFeuXMEtxS2f_3kZXUIK3xx5lO5PDfZQoRVuvTPrzphbet2W5brl7TCOW4nWk2L4Jinv6CKF1VhMA8sqTdZy3TAr5axwc5Bp9qvhXnv7Vy1Vl1c4RF-xdCrD3ek_uDBvBl_EDhky9oAjpVWSwpnvXim2VK87lStZfZFXHjmRRmc1D_DmFhmSxei7ZZsPneL1nW_KCO8RUEuGwqh_td764z6SSd_xt4irG5WhSHQPzFP706Y9MBW1FUGMwCak7TYOu6-5Nle6l-SjHx_XkxBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=qUUGq-MahKxq4Lo_4fBxFW46lb_DG2GVy9Mdvz5yrUpWaf2CoCsPaKsw7fOCVmOO2d0LE4xQNFTLfqz094vc36woDYtiRVwffSOFaA1AEGB2X3c6WIo4UgjD-QBfP1gBJ8tfffJvkrhzsWdqkVPlJObiAoffc4gqUN8BFeNM-vcUKO5_x0z1NzMhmtU54ekraeJ5biaHFVNiJviGt6iVO1zccv1RvA6DxMtAMpe-MQ4GhFyyZi9XcVLYhGYAHxMheW2rbq_lrD-zkuRJP7gqZ6-h_pUd8lhfUm6xWvP6HodRZYRzegxX15fjtC9L56fWtz8GBoUNL89CcjocvncqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=qUUGq-MahKxq4Lo_4fBxFW46lb_DG2GVy9Mdvz5yrUpWaf2CoCsPaKsw7fOCVmOO2d0LE4xQNFTLfqz094vc36woDYtiRVwffSOFaA1AEGB2X3c6WIo4UgjD-QBfP1gBJ8tfffJvkrhzsWdqkVPlJObiAoffc4gqUN8BFeNM-vcUKO5_x0z1NzMhmtU54ekraeJ5biaHFVNiJviGt6iVO1zccv1RvA6DxMtAMpe-MQ4GhFyyZi9XcVLYhGYAHxMheW2rbq_lrD-zkuRJP7gqZ6-h_pUd8lhfUm6xWvP6HodRZYRzegxX15fjtC9L56fWtz8GBoUNL89CcjocvncqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5HBMk5_ETOIwE5TLeXh0e70SwAPAWm9_0bURFS200o2SctAYK4mKke-dj22tfO49cYYxuY9O_O0v80mPv70D1TP9IoL7vXDP3x7CTVfb6-iS5tcurIfSleWON2gkgkq3iruQnYLGFJi40zu4dEMzJPO-USY1UmBZGk9bbQWBYHahUwfz3F2oq_yT17t5bz2c_qNr6VGBaC4-a3l8glgWtxsgQSmRvydUvPwDbBZHEROdVQ7xegGoBisjeZXMkBtbj7FXTwFYq90sMT33usKGIeyIQeIbJbDc-wWJ0witzb2cv2cdhu8wUV2RZwXJBPIVsFD2R7az_10TCvkP4cecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSV8yQGNhkUf2gw7648OnjU_5B_7U84__QZEjqdXwdgZfE0x55xk3haktH25_364o8Fpt6BCmR3DzUOHWnyzkn0_zxuBbe4ZnmEVIWn2NfHVKUUoA1xf0Ur6EzS7_dggzujEZUI51BOu76LPMShv913aVBZ8s74MEpwyLHjBufqB4xyaoF_-hA3nClTSKBDPC8NwhXrvdX6TAIEYI1euMsw8c5jmHsXMRk60bjjFu6diZxlRXymeMO8KkDk3qScz3Z9cvuJmg624WuSPRWft5R2YUp-rTZKjv_eKUNZEm1UJSDF5kJy4btmifiDE1g2QwmuUuVRA1syIHg1v36WPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5viHQChuIy3o39hDghV7Z98rDZSuesyXNBJKFcUkvfjdUMDfWyt6ZiCA4J8uV9BpvZEotMBB3MTMGdE9tV9Fq2JRpxlLajjZFMoYx6k9ewmt-vUfYaV4ou1qWo5XAcYd12DB8NYklYNMObco4eu3Kn4cFYCKCeTOnRF6LcHcRB20yZvUAGQwotH96i6-CON5TEgkRinNps-oAYw7lmcBqQ-YxmRKAPSa39m2dNPHi7r2e7EhVJLkl7Qv7Z1LLfUV9dLw3wYQ1cVrzDkYKb2riVZy3h46t_YhO9mL4OKfCouAyGaVkO87OVDG2lKVggaoYg_ghgnnDG9_TTCVNFzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmycDAI8r4H21vFXSu2fCcpYM5MjrEnhZCq5DoezTSZ_cr7lnp-yji6WWdF3Li-5F-ZCzTgivhMKz-WMDvX02xGuadL6TDwqV_45etqCTYctE4OrlIw43RfOjs3rsi0J1vJ6_SwGdzO4AEuPVxOfsoz4q2acqz0A_I_doGcJl-XrbOsy84m6PPgba117bF9UgMPZEaKiSPM6bBMbJ7tDS_eWWHKrL2K2K8tiLzORg6144rq4DV2S3vYYfivU8KpICk_06icNPbnQhWtqQmph-D3gTxN59J6Yb-L0a_fr7OM_Nsismc9YGAaSH_4pLj2AJXQRdyIIc592JpwiywxTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEJ5m47dgKRu5S0g6CwQFydNBsWrPqJiElh0XQa9RC2xn7cyn7t7oxDWqMNc-c2TlaJKCr5ko4dLn27BokMFcnM1UBRhtofHQwUSUvBUb8v1vGHlwOSfrs4vYmSrBxCdaZ_RUW8tjujVTPIdsgH6NzMg9Vw-qLFvY4cWSW0P3i8I7KAYSQzZhaRbZ2oYOssZImwvyKzIG8uB7a51PFR7g-4nIVmwnvHLcMeLG-tmhF4w6SEbjkWK_DreUKYHKWzMKzx3kfH3tYFvxRq0Hih_70x4lJwOcKqzUvkpgo5aku5p4Vz-vlt34qffLcWiPfosIVTIs1HCubbW_E1fBpVhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95DcQY9os7J_U4giwTTwrwwNE9kPqKaoLMfsF4QWnQNe2B_i25P6iL_MIJaDt4eb89ptMfRvXKUOoZw8sBoDH1jrZPfm6OHYEKIFMoa716eehrlKNWuq4u3NPnRfaGZFkXG8JGKVSDjnYj-Zh84rsXg0on_FZ0JHT2NRamakOdnYi_daT88ikOZeFZf9il12NUt8U_nh8sUnHtiCgBOUPAgG6piWRy1aJGS2ETDGdd9tv2JcbDc0Pranqs8DKa__SQBt1rH-gopZz-DFsXh4mKbN1bGFGLYMFdV-MHNa6QubLGP4JTOw61Avt52xlNs5JCHrnRMfefc4MEtlmOXXXi8eF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95DcQY9os7J_U4giwTTwrwwNE9kPqKaoLMfsF4QWnQNe2B_i25P6iL_MIJaDt4eb89ptMfRvXKUOoZw8sBoDH1jrZPfm6OHYEKIFMoa716eehrlKNWuq4u3NPnRfaGZFkXG8JGKVSDjnYj-Zh84rsXg0on_FZ0JHT2NRamakOdnYi_daT88ikOZeFZf9il12NUt8U_nh8sUnHtiCgBOUPAgG6piWRy1aJGS2ETDGdd9tv2JcbDc0Pranqs8DKa__SQBt1rH-gopZz-DFsXh4mKbN1bGFGLYMFdV-MHNa6QubLGP4JTOw61Avt52xlNs5JCHrnRMfefc4MEtlmOXXXi8eF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZRrMdRahWx2EtBI5ygM4amHFrQlZUAADKlfzi63v8_wCeqF6La5E2p3Cc338pGWRPVN9FgSPhZRdbAfhhQKCr70j4yGqkY2UtGSkFm_Jev4P8-ViQvjP-Elp96NnwJVviR2SwdcSATi4qo6whePnDR74hEDAXNxdB0t4QrJoTthEGI_JyuwuXDu98gWwmhSAhAacSusxVA0JXaJCGD9AsFmCgTVNnKYAoNXuYDGmxkdi-bkpcnpZhWnfoS_pjeMSi1xDK-C14j5BIw65jJhbc-7hiPiHVVkrNLe_kN5S-pv-nYfhWAmxonFDPZ2neql7ippQTQRefWo8MzRzkpuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcHan9fs41OqAv01x-qQacwKt8xuEKKMt4-cXaHnx8qTrpnb61lxt42aqHyJkWzLwhki82XG00RgMl0ZSL0kuFFCAAo5hul4wT65_UjrgfBCpMUMG0aNSoZJtDMh0VJBYMTWX3HwpxVXo2ge1jXGrXgg8DHxZRWP1kstRHiEfQ1k0za1FuEoyZ7Up0pTf3nr8dIT2A1L91pdSPayBvI0fdds5W0j5rHzhXYIrRFVCONRbBvtsDojoJBHqBEnpB73Q-c_X4iN4NVJCO0xH8qjBVGWCCxWtSoALDHc6uOHrVjOsdR9tVqdfntx-fIizVlqAb5SpRU-ByY3-VAEFMoNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=TBMNASIunZkE3yYfFqA_JNmHF19TKFsbnR2klS0dtP12tcPJiAxpHVgRn9qa9i-Ib0ujX8Oky-V-tPpzvOG4XEg-c7NBSKd6pophswDofEuueho1m3mEabZQ5G7eFD0GFNL5ndh0-liRAwEEsnm6uOhv4Wyk5y5j9n5WWUKMjbB0D5U5ZOygdqSjnNmRPpcOAy1ZJ1fMDKDarX9mZXU2At_4NMlCB7YvYX8Mo5xUz07q3sRJiCXo3YKU8f6Mhk6eEJ4xsvxYuJmvHTFI2hUDx_1ARmPfqcDE1muCvnHy0S351nu6IsNgdFuCK3NjnXy_QTT_QabnRMDhAymw6GqpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=TBMNASIunZkE3yYfFqA_JNmHF19TKFsbnR2klS0dtP12tcPJiAxpHVgRn9qa9i-Ib0ujX8Oky-V-tPpzvOG4XEg-c7NBSKd6pophswDofEuueho1m3mEabZQ5G7eFD0GFNL5ndh0-liRAwEEsnm6uOhv4Wyk5y5j9n5WWUKMjbB0D5U5ZOygdqSjnNmRPpcOAy1ZJ1fMDKDarX9mZXU2At_4NMlCB7YvYX8Mo5xUz07q3sRJiCXo3YKU8f6Mhk6eEJ4xsvxYuJmvHTFI2hUDx_1ARmPfqcDE1muCvnHy0S351nu6IsNgdFuCK3NjnXy_QTT_QabnRMDhAymw6GqpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVoVp885P9flI5E4X1PN3aq0TtEIwzGMqxKErIy9XGNNqQovX39IEW8vAz4OLqFVfX0h8j3Z5JZz5-2Fl9TBYcHdAH1zi2NmLbfieQsxaNzEQkDLWUg3GWpuLrL6ZMLaM5gFvfyz2VHviBIfwxT4VZ-5thD-qxk7SVkbi1EvXlLc0tmWjM56DwPALs3mcOFAhkk3X8Po6FZH6QdLO-2DGa8HgdLbPjccgKNVv7myXNl38mSzZxEN18Q-9no18L60HfxExUCUSnaAcBph7dkrslK7rrC-L7aqDu_JnKdbi2CZxGfVqdpkocGXNm_SLRG678CZYpFEEBdMtsyNgiqIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=bia2atyhiNjpBIoVvB2xrHr1V8WsQhAx5rjVHc-GCWabrJ2y6Yp4g7A4fuAvrDaaVJoK02W2vIGf2zze4zEezzE985xGEUMx3YcVolsxHtJAQG2IHVCnGsCH8HjfaquZRCTiIn2JjnVwBotq_2JEUxuzyhtd1mPk0IYf_ieBOwpCNHmBfvhuin2iiWVktQ7gdpO8rcsohyQvn1mNq0UbfOjWgqy_dk10_xncuT1QIWecGWRwN0MkQi-EpMUg0ye8yKGYyjWxOatJYq9TXpbvIzJDl-bJr5tcn8NyxGS86pwdTesoXnU10CRdn4Scy37c61Ow7AWHOisWazZ_VT4fyxurNki45PzuChgRdh2mj-PKTmZ31QzJNw551ZxrqCdsoRZNXuOzFtQiRvzsQfJM2WBfbUcvWnSgX8-GyX0iCR9z0mds1xnD3f0jqNajCffs2mHsJknSYAWCYl7-vu3ssJ-B0MkW8Ds6WYeZgdq_on4_IiqRX7LK4FOMrtuy2grcs78Wkq4r4-qoe9fPhwdHYtUhjERPtqHlu4PqYF1ird68IpAzx0FMadSiiAjax65PRYzoSRHU4qt-ONpa06d9h1BPsslBNnyGA5krpOrDcZo2aLl3g5iERbrkpzCki7z25a7WOt4w-xKWweh42lZJfcKvc2lyJWZ7RkaoEUZfXG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=bia2atyhiNjpBIoVvB2xrHr1V8WsQhAx5rjVHc-GCWabrJ2y6Yp4g7A4fuAvrDaaVJoK02W2vIGf2zze4zEezzE985xGEUMx3YcVolsxHtJAQG2IHVCnGsCH8HjfaquZRCTiIn2JjnVwBotq_2JEUxuzyhtd1mPk0IYf_ieBOwpCNHmBfvhuin2iiWVktQ7gdpO8rcsohyQvn1mNq0UbfOjWgqy_dk10_xncuT1QIWecGWRwN0MkQi-EpMUg0ye8yKGYyjWxOatJYq9TXpbvIzJDl-bJr5tcn8NyxGS86pwdTesoXnU10CRdn4Scy37c61Ow7AWHOisWazZ_VT4fyxurNki45PzuChgRdh2mj-PKTmZ31QzJNw551ZxrqCdsoRZNXuOzFtQiRvzsQfJM2WBfbUcvWnSgX8-GyX0iCR9z0mds1xnD3f0jqNajCffs2mHsJknSYAWCYl7-vu3ssJ-B0MkW8Ds6WYeZgdq_on4_IiqRX7LK4FOMrtuy2grcs78Wkq4r4-qoe9fPhwdHYtUhjERPtqHlu4PqYF1ird68IpAzx0FMadSiiAjax65PRYzoSRHU4qt-ONpa06d9h1BPsslBNnyGA5krpOrDcZo2aLl3g5iERbrkpzCki7z25a7WOt4w-xKWweh42lZJfcKvc2lyJWZ7RkaoEUZfXG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrNuKzSReHq-5RZpJJ5PH4K6P5WUd9FACz_mn6ff5uPaJjWY720hrFXHM1vJSSmfHeLdIj_14d2HKo3DIgRm8GYQB9HEn_pw5OaA2qogiTwkPPSHTAKBVXAv4mjqTzVcE8ptCw37WffyTrdlf2uyqcCSQDpvicyOYJb9aUEZiErVivGBDiWPKmWNh40-sKFLoKs0YLWmE9ajzuSxKwJiBMFSdKMnXhKLR8o3MQIZ6o84XEsjtbz7z59jzc8FZeW6ftGxowDPhrXsTdmDWX_PylD16cawiay1LTKXQskt8EoTkKK8JsHXuNaWTvVl0Fub75zpdsUtSw5x5qPb10sS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJpLZXT26G2x2ClLYb90-EkhZCXKpZA4tarv6gUtku-TpeujlfwNoFTWuVs2Zz4Zc3mtoRFZGyTscHhh9tCSLOa3RwStfDVOaePCNyuT3Hxji8A1gcNmgxAVPBTcp70fttOGLA6ueURoXk2IOcgtE2nVMuxDuZ8RXf7or7IpzDj3W3a9ZbFpNzjG1LN0cl32o6ISXHyNj7VXB7bXAblT6LFdUuaGd8Mo3itr1niSvAqGaIF3vv761WO2k_eqkcDX_cK4OU78gA8R4u8YHp56PyrpUpS4AT9okqKmFgkO-vfUKJaQXardXy_qVSClGRQJ6lBlkakFNVNOYLcdGeZghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os2RRe3uEkBFHDtO0rdnKBx0mLvAdtdxGh52PoFsuukbXA1BYDdpnY2dvzGuCVExDhOFjvSv8S5VDQt1egizjS4xgNfi_z-23MkmzJJS6xElpfNMdSPl43sccEhSCh8pFa8qVZJwo7CrRwgvBDh74J7lMtuqNHKIqGcd0JS_pEFsRo2OEqCOOXC8d83LPjqcLJDSZlCy_MehezoH1KhKmQHErGsGlG0QVncgIdrIkay-Pu-eOXyjN9tEOS1OmEPqgLK6lxYezF-j8NPIWTXXvcp5LOxehUFxJk7JszXjKQe4nJ02JoAQVff7mGJlbb7YSozCSSYBzb4QBmZsQyyaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=W3cgsDeeHpxtETeZAvKrTPEHOm9Gr3I7UMxZAlCZEuBXOwOB6XLvnzo9B_SFd-twHviovLIVmxmZP4P1OA7rCPfmBYT9EoSz0uAJJIXhuS__JjTvisQrDCxI9xNwTMDzB3QSc4rmLbL0CmBqCX8QtqS8THkYsam_4x00pRxbk-k_zVRCtBUP-gv8GVNEJvBgLMKRXkxaR5AyXL-SEvHOHVSpZYhuUfTenyBrCuBTZfQW7n_dsWiW7oK9YhFITGLu9L0l_VT_NbtA6HqJw3vvA3uiSby8YnwxPbf8cIWuaePg8qPRoNi3nqyNg0I0NvPo1PMUpYEbNiyXxgGVuoKHmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=W3cgsDeeHpxtETeZAvKrTPEHOm9Gr3I7UMxZAlCZEuBXOwOB6XLvnzo9B_SFd-twHviovLIVmxmZP4P1OA7rCPfmBYT9EoSz0uAJJIXhuS__JjTvisQrDCxI9xNwTMDzB3QSc4rmLbL0CmBqCX8QtqS8THkYsam_4x00pRxbk-k_zVRCtBUP-gv8GVNEJvBgLMKRXkxaR5AyXL-SEvHOHVSpZYhuUfTenyBrCuBTZfQW7n_dsWiW7oK9YhFITGLu9L0l_VT_NbtA6HqJw3vvA3uiSby8YnwxPbf8cIWuaePg8qPRoNi3nqyNg0I0NvPo1PMUpYEbNiyXxgGVuoKHmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaUrgyRHhvjiEWtuXaICAPLaAPqBYZiT0zml2rlg0M1PcrUGq9WE5ujZyP5icwrJOmj3KYB0zvvICexW9qxhJExJxcMxTnwcDMdt2WhdCiyEcYmqdblp_yblCDpXeZhnkNIhl-VX07ddRJtt_QN4Cjo67l84egUdN6Z9VnTX2pC8ztGxbVF_7HgvQzQAVJ_5lvlzSzM34V1pqHE3wWhK12ZjgnOLttzl4leSFnaf1TB4q-pv4dTLzwKC_BuBXwkDjRBQNKJk4A2FZJtwJ8yK8BuExxzm0K-OZtpLBihgkgA20_GbFdLM97nhqXYLKERH_KIQwWxhML67oDu0SHX4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2Er9AnOkghxJP_QU3VINzKlOr0MUgaQhceGKyvu3D2Nllb3x9KqLAEr95l_x1iuucgOdpYRVAjvvJwcakhNF7ecOWC0tKBF3_qHFFI7IlKWMTYzHdnbgLXyWdKQIvo5TAdNQoC2wobDkPauyDOXNGXI0djHCkZPy3Im9EpwBQqOkl0sSxODtaTkJhnGUa8kMxSUg8Fo9w4-GsAK3mIBbsBbS1G7Hn6jMI_avGnY3XBvkE_kPayKLnBhnAahVJh_xmEK0QoS0_1I3mru1uAiTwAmcoZTbL6qOc6QZMxnpzYkwyYXavva5ELXrzxroDMaaw7G4QH5Tx5lgNVq-zjApw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6gM7moGIKLQ6ULAMTjxfDaQUd58gVOZYob7BMX0sciGhBLMn9BJ04GF72rMYRzXsU5wPyKI51OAZZ55QVrfm9zycN5B2qRI91Uuo-2NIHfWCfhoJDuiG_3PPwSijCzpZfu7Lk3eHxkQLizMKDBOC7TQQtnRSbAQt81deA2eGR9QzUncRlZUH7BZIqJ4Rqh1oRLBP9V2AS_xdtHEGjEhufJzcFs6kObTKMsk9OK5Jk2LmxkLmDCc5mntunjMDZFaJjvUFe7QWNFw1bBXQk9-BJ26zqHRyKU4AcoMygpn3AFxsP1_-iskBIbG1ZEgsY7UOH1vm97jM9QblmZkJ5oYhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=GtGWvMCGhNsbko5p0NS70foTxoUdv3uT8UHQxKH8pVxD-_i8olAO9_-MJAqxSgBbfNDkMUMQ_D9D_ptR7aSa3nrkrq_HwNe3TgEqHa8ChZ0R0ciLCpo-0C-PLYnu4SD-JX8cMmY26vIEExYBFie9h-A-PfYlZ4RLRbxPaGB9CwkuezascvhY1tkx_coW1V_-j8le4sZsMBn5EZG1EGqcgc-2ULZAFXYPqmDNEjo64Mghuo7-kSp-Gnv7OctDlvJHbL8np6NIWskesDRegOK_w0dCXGFu_zdIpxhOv-v2ozgixkLNdIxB4NpjSMhNM2RsACJs3f4nIZzlW73y8zNcHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=GtGWvMCGhNsbko5p0NS70foTxoUdv3uT8UHQxKH8pVxD-_i8olAO9_-MJAqxSgBbfNDkMUMQ_D9D_ptR7aSa3nrkrq_HwNe3TgEqHa8ChZ0R0ciLCpo-0C-PLYnu4SD-JX8cMmY26vIEExYBFie9h-A-PfYlZ4RLRbxPaGB9CwkuezascvhY1tkx_coW1V_-j8le4sZsMBn5EZG1EGqcgc-2ULZAFXYPqmDNEjo64Mghuo7-kSp-Gnv7OctDlvJHbL8np6NIWskesDRegOK_w0dCXGFu_zdIpxhOv-v2ozgixkLNdIxB4NpjSMhNM2RsACJs3f4nIZzlW73y8zNcHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtd1pSwaMHimcepP6FKpbdkAwCCOTqaXftKum92no37kJAqdUEH4szWDjhVAYoOwv-aXEHTjt6fw-bY5Bd04NVm_R65-9qm1IET_GcoEdXqacV-R8EKZdpJmSbUt8gWU2TJvo0nFr59d2co0H3ShtALNlkdKh6EWdyG98TSjPjmFbOYFNGGGiKEw5UkkQg3fWhLdO4QuIH9Ps93evQottn4YesWT487Af6DTxLhEapJKHll1OyzZtYPZZmF-e2gpkJz0BW84bggQ4cwNcMo2BgARsH0hGcczqhy8TbK0aFsbFG8VLvdbyjFjxmQGS6aIy8gre50jbkrncOVFXFKmRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2xmOLjgOh87MTz5ap0OGaEJ6qMBrAMaHbgIRmUcj7o0p9Ta3OuO4jc3UL8OOeD5BDFWMeUgF97fnxjfagffXXWpw3dZKHai7bwRQjCG4mr7depjfmvSD0yYI0eyRHe_OHUZ6nl2wi_i0PWDFDtK7lkvOxJXCkRu2pYO39pzSAMTAxdVlAOLCzyXULVWKxk8eqIiQkr2BWZDAmpZLg2aeuboaN6fVPg27SpYl7tUCY4LHxHWu4ScIsoL8mrgY0E5o3dxYS1jzh2cGlvfE7vlnCgeEdMiPiBVVd0wLrspIN_0wxYKM0o-vsHNLnM9Qzq_vj1YJXcyHoOdfo5mUUwUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3-GXt6R_6lBgu-_Iqp2zC7RY64o5jQgIilGbIfJ43vf9foDeDx5P7R3uwZx0QdRd5OluzQfA8ePCPBMT6oSjgKiwef-IUCbyYlPcOU8MLDO2uS7Y3OqerTamJSt9Pxe5XaQMQ_EsNMklK185Coy5G-ZN739BI4fDIBf9zkiElCRHpS8DSJDdFljQMyoaH_hJGBHqT0FXuRnS-s5mOUnFwf37Nga_u16OLPl2hikSLVTpVs1N3SYp0fElF3x3ew1H5UGrVB6XnydIsMW5ifrG-cJZ6MhICOcjaM_nKh2C8kuEYGmsRunPYU9S-8VaiVD9bxlj7lKFx-sLyHHdoSr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-tqCYx2spLwaFrBEwslM7kMmHOf_LETEv6RgGHI2t0ATN4GjeqkJcnkaOa0YTgtnWNiae7vHqb5IWvbGhSa_VNRABbiMTRHnuLBiSMeeH4Hyg514lUOSVwVwPTqqw4oI7kXalewos29q3rglDLKhB6Q1ejOkL3Cmr8URhDZbYhekHtuYvNBP_ro_za9MWI9wUcK14BTjCrXK_Noo9U6TnRRwR--ezeC_IEJV5WU4LAzZDQcBZshbnq0O-i68ZMAdwsK8RU8k2ZjS2bNDWrdcGjS48LiQ7qC4hzErffWgt1PsUFPm-AJjTfjIEuax4s1NMv3kDCRA3_d2r8v8ox5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRA0Q2N3xLWGdvpJefoZDxZjMZD_H-gpHppFIFzkmI1UqvonUjVU9YtR4EGhkllvoJYFBdMKO2SwI6TfzkoA9ozS-t_MPUYD1d4Mv0hfWZMRuwD8v1990UcY3ust2GlAxCU-KzI0p1ZGWka9qlsX7uSGu-v2xatn1wcPBM_W95P8wi-7PYNzRryoL-yHcmZJ3solsrrL3bJWyDSr14uYk-FxHiPviDg8ozuNEcGlfSLsXqwsa-gzwAxP7BvFlsL7_TGuM4txK9YbCFohaciCbcQeZjBJGNhWiiCXo47tm1JnwuOLGCepAXRQnBV79gg3V5uAgs59hUJI-bLeCctzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PN7leVbnxyk8JPOm2EJcZLpOFY7ivUzQDx72SoQkSbcUyso4fwNdKak3BnHcsYDWop2CYqRhGTo_jQtKDr6EDBYFTrR0J6xJxX2u4vqjimdgJuvSFe3Ph8I2jTngo7cSUpj51CDnfIWoVMP_2igl7CB-IChWOHyA7pQWdvk3LjkFOsytZaqHUKGH6veJMVGYcN9LPjoTQgIARts_iB3Llt62d_pWG-viMbVFL7WSoFeI4eQcueciDX7V_7TVym1aDkXI0uQvJgsPu67TCr9CRfpeOOgGkKsZn1CsZWTg5irqMnoYiv6xNJmybXKefKj2k_op6FbnLiXyfmDnXBXpig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9tZsEYNpNb1ICfvtd-rluF8emYJE0uMKYlN2yr12lGI0zYyyKhv8JC2-y61YJC5QiEFKvY6HnoVKf1X1s4vPGdsZNdQlPpO2JuyOEkt6jTB1WbkWYsXHOZvsPmunto14ZNa8dadY1tdCub0x4TnWUxSsQcD66kC4mTUv08r4V_D1LOZZHXEg1hJrKaqvPzYF7gWPbwth1s3G6xfIWMOy4TGWyh_pNaZc4b_f0yeecSiAp0HCzvoLnlrEBTrBzUPf9YrAoqf323WPxXBxl8EnPiJeg8oxus8iszAwzKcZnbxp1xiTbO4gjYz5nQgwlD-lK2XKWJKuJQkxyQK005C-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=qETf4fQZwu72UE-FBKIGfL1dGRnr9fUkA42l_mO85ErQl0AN8vFzQQWmk3BeSoJEfwUQgmsiMWS3lsEvcoEDjoiRitZVskXhcyRlJy4WXNxIQmXlhQtL8N907MwzYZ9JkabwkY1DmVzPHcbIAgv8oBxEJQvLexNobnEiolHoOfQ6vxJVjaWmApOhpr36wq7aGsoYLQnjWp6OyDO9jDI1OT_X-3RkZiXhHpx4qaTn3kx9fD_hocHmIMCKmyVUeIchGxshhlSePTBUefxrn8kD2FAQU-mbvZxRXTMarFqDae564SnkxtVYFzRFulR4fe2iv1WShn4giLb0o3WiU127BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=qETf4fQZwu72UE-FBKIGfL1dGRnr9fUkA42l_mO85ErQl0AN8vFzQQWmk3BeSoJEfwUQgmsiMWS3lsEvcoEDjoiRitZVskXhcyRlJy4WXNxIQmXlhQtL8N907MwzYZ9JkabwkY1DmVzPHcbIAgv8oBxEJQvLexNobnEiolHoOfQ6vxJVjaWmApOhpr36wq7aGsoYLQnjWp6OyDO9jDI1OT_X-3RkZiXhHpx4qaTn3kx9fD_hocHmIMCKmyVUeIchGxshhlSePTBUefxrn8kD2FAQU-mbvZxRXTMarFqDae564SnkxtVYFzRFulR4fe2iv1WShn4giLb0o3WiU127BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkaXUsSYJuOdWfrXeIYXEXAbE-Mf0_MRlqgMc6z-GxJJwwLLMfbOdlciXQWH-BDH6pDftUpH-7_G44SFIcjyfmAYW7mHdqEdED-y-X_adN5_oL39abqKgxxd1qhiwOhGWCckOiB1NuleIIaSx786RQ0H0_wzi-jN8KAvUFSr7igvYoz2Fwumx6bQI5kkPsdqO350syuK-Ng5IXt4wAgG3JLGmrZgvGrXK4uHAH2ytCKpoxh2R6UjtvjtkiTGmYikMqVgscqc51D38gmYirBW8YigXOOYogfEiZxvIKZ6bDqCRUQmt_LAcF1bqHIXoT18nIY2xXPK1yFkcIyXOUFbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB4MAIVLUpGgiHMhzCMzvGCD-9SqeNuRBsT3iWPfi-UAIfpwcxwNgRkG8MpCnFJbAvUfg-jXvmkddgmxejnWzMraMh8Orm2gO6La1CCzScV-GerkMxMLfbAD-EdXtm-hapf1QiwBzxdBLA2nzOvmI88Rkp-U9J7TByKOwiNOl1q3L56FIxvnRmuEY6NgvM1HmLVlrwJIQbabro9DLO8YnmI8PGamKl5FeZMtuz2Zylk7YJt1f1ixPqsBKDt9W_Kc0JdvbIdD_LwABiVcDHZK7-ADfY2zVaLpYYqodO9RD5J3JGw9YT5r3Naq-753OM7UK2j9CaHHmid_YKzbFNM4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv1UQh1-jp8dJIe4GSBVGXaReHQAhLLXQmNvj6CIwTaKxmw_4xT0jPEq_P7rTRX9UFy9XpwwQDGqncaGCwk-gPEqPgTbqNgBmYaf_wa0tFRvOc_07HjGKz6o6X_1uii0j2peC6Vc1pePUoS2J3OgGzUThco0YZ4_LArBqjThJBdbR5-QIt2jeqXL9pVUHvH26gMRsl0tAds3ZKEh36JkCQsFvrUQnTjJ2UxzEwX1Fw0oIWaY38uVYSsvkSPGvCKmoXMKqjZF4x2ChU0J6P_cIPW6ixTMnIw6wqsFjWYRMTOhV5XgLIOJBkHtlyog2DS3YdUkBe0bCI8MFv3oYNsiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=Emcnvlq7SCBHM8N3Ys7a2rCv_lTv86cGqLPjZtPUZqyPXzZoBqAHwWJu6qJmnFMwOrjjhOGFj2BwNRSNl7MQjvgxBJx7NY28Cql1ZLEnlX595Haep9dBGzH0_IJRw51cvwZ2icrCiGIsraCpClxFnONZ2xz9eaHf7LdlwGrEJV4DL8d3Mp_DfbtMKEMHWfUP_pp_Erux9Zjw1lzGv6CROR6oCieW7n-hOVylcseT1MOomjfCIDaJF8HI-vziIw5B-8DADttm387_BACGwrimpqx8goD_NdFOo45JJGxsA8E3u0xJ0RduShX4f_5GUygSUoQDppbw5pFc9_BAkI7cew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=Emcnvlq7SCBHM8N3Ys7a2rCv_lTv86cGqLPjZtPUZqyPXzZoBqAHwWJu6qJmnFMwOrjjhOGFj2BwNRSNl7MQjvgxBJx7NY28Cql1ZLEnlX595Haep9dBGzH0_IJRw51cvwZ2icrCiGIsraCpClxFnONZ2xz9eaHf7LdlwGrEJV4DL8d3Mp_DfbtMKEMHWfUP_pp_Erux9Zjw1lzGv6CROR6oCieW7n-hOVylcseT1MOomjfCIDaJF8HI-vziIw5B-8DADttm387_BACGwrimpqx8goD_NdFOo45JJGxsA8E3u0xJ0RduShX4f_5GUygSUoQDppbw5pFc9_BAkI7cew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avlm0bMCOj54KSmV3Rq80HTVi6o58BUrvkDmuGlQwi7ZVNqgO7tkALRsJa2AsizTddWKZZAEZebu2Wh8JDqNcTi43V3_SrS1XzRQHspaPK8m0TZEYsOgsiuz1etO9Zhq-7xmPhS2fvNFzHoUmjKJtdgDsHhUqwqE5LOvRtFO3WEdg_WCMriQeRG7ei0i_J8UoONRBCxyRdEMRbpyN7CNxaGCJH7sGHMEtf8LZpHY0nRRNeOOZ0AAbeCR-SAbZ8zM0PoItPf5wN2SNKF57CxUz0R_47qWwSGie3mPdPKWVPxNzAVFUC4g_v1YEZ0GA9lg3mL9USg2lAUfm9sxKDnJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwusIdLUOQCebB518X0xtjGfkmpUZlW8i8KGYL7trpRsEBjRBtpZZyfbN6egpPtmf7DjFfSZsaCpNTEzWPRLIHlJ2HcFboTS1P62t8Sz9ZgSYO0KD_pRtQCRSDNEK6K7lLXE7qkg9OP3VdsgXnNKfq5LDXQByCpFlb1Lhjuyj-M5sek3P-yswg3a5AxyKiyfwrxjpk3sPfhZM-oIjhR5z6IhOHe7n-I8iGP42fVOXCvzMzDOmTVnOui9lGocUKWV_kkIIERwMpVD8NUj2amp8ZlXWeqM8XJwykcaS0D3yYrYe8xBjurC9iNATiUKRCt6UA0zrhW1FaVUF3HX-AVepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyBySkPKr2CMwFWXPLR2WyemA09VtThx7WUDzO20veIOvTcBXiMRf8Gpp8bIW_OEOiS1H2pFGpc9j-L6jiPxyBBpbnxWcx0RiZ1GAJylFM2MOXyNFiqLoRCk0gIOcXwlcoJUxAoZHogr4A9qNND19aF6p7tp48r2mKKSKPTiGcTKJLcqTvXUXrF2zXr_SNrL_qwvePiW3Vq-VVInnTpNNg5QhiVwrTppcmfqS0Q8kf6DIiKEbClZPiZgMQ9wFCeSSuW8h_QGMG1Ahjj0qj40jgl5yAJjowZr5S44nSmNgyMBlPCqL4sP_z3kTqrRGLMkkbRbBEPspyqR_nlkCFbX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr88dPzTu1SXrG_Q5c21ooo8B1UePp11NQ4Hf7qJVR6DyTwjCk984kD587eBih69Z9We42cHs3vuj1CZgDjgBbE0HdjdYEdoZDkoGduSoRSeh7q7q76b-JWihBrNDwH4tKsdeBM1J9xmMfgJHVjW2kFT6NWFH6qfGi6LIoaCkLuA6eBJf6P3ozj4Er9M8i9hqnw9pUsZRPsvHlgv7H3JQbDnsfowTz2tO6kHCp4s4yVI3-OFWoabJQzYoXDLbYrsFkXctl_f7a9b0yzL5KDkOndw-wUuzlLG7MtK0oykF-KkdWGq77sLWc41cOEqWOJF27syxSUNpKbzEFJpb4hDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-mTz8XB8ySJjgvRC8Jpd7VBLMP-8iu3dW6a71ZM9LI9s3tzywbz4WwlLbQWS_VC70pvPnZbtdfATPCk02TBhAbbamLcdSRn2efymKT7VMtisOb0D-jSNy0M5PYAySF5Gxj9iHDeNVjTNfawBwU_IDoSVwI-VCyHnJwXYpcWwGE4SfBqef5_gvdW7OcdVyok5EKhszwW0RIhPv5HOwc1B89mA3sitAZAJQjHUzTV5joeqcwikltwOMNwIu1-9BFTqE4kKG8Ooay48FtyhmqujTlbsPX5SBWAhlB2KkzACBH7HoyFdxXyHrZ0cHBN7juehW6MgtoekqPv93dZg-zbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY9TCsfS6tWi7jyJIqVrQasExwK65aSoiZQX9WW1duLalMN7tzmhq0_oE4H_HmZwSq9HO9z1EqynSdAoCCscMdaKs6SGCNt7pY33PDGOK6Tc9COm6f1kiDYzPuDtaySv_hPlwHEwHPx60AkCLGYORU9MY7wXCXiWIOxBAWEyQocYkslMFFuTEk2KsxJ8PMNZX-pGPH0wG3WKBFXyJBwdXuvdDBIs_UBWHiFrGgrhS3OYV80JwtS2Mdm6zM0Jn74147_LlHOpa3MAivEP942Xu9NGXFRm-iLtnGqfsUKmRH_xojC_78uddrJ5VUXlOBkzOhuW_Wv5EVMgOP0uAywwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4cZurFGNMA27oLkW2bP0az9g1IzMksOlG49enU5Omw8zDXhL4PQmXNsbvDEOMRTpPAhWiHmPCnxSm7DkSLfpvHWsG6deR6gpmSdhSazaFQriZvnn9XzF9Xk1PtBRwFnd4XRlQFHxhwvVpngmrguCNzHHp2M2HD1jYPOI1aVOqWvBIirarx7LD5WvUSS7qDwnMF9XLM-LgDYSCH_yCE5NOLdJdDVlSgeG36gkzbbZo84A1564d806IoAZAyeNI1unIlbPFRV2i_1pbHhKQKG-yVYikBbyADzdEEJr9oa2oKC-01UsNiTF38oahpdT1BjQYGqk_OhNVy-Kqfr31iz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxKpcqgCxD6UZiMcM0glDSi4-_7UGmhVpy-9HGV2Sy6JcrO8hoNS9BmaZ6bT0RfY-4jXQ3aBnHc28f-W5-ZfdKWTfU-nckPMjfcJQDrL5eDfY-aOEBvle5Fgy5Che3_zTAiRxjDgLn2ORrZnSXuNKkCUvNNUM-E1-GLJnUBEBqOojzXUfd4PfatAlntB0Fxoa_OvKu1lzNtfSwCK20o8egZTHThZgXdhljrqEKPgXzYVFUNMx1SwHt3hj-fMBgMk_daM6HoKorSrzYptZIV_xGXHP3Cq6cxI-uTJl_CHJcYOSSZ9CHveM8wZmQNgNVc9elg1xEX9Yny6EY-wHhUd2RrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxKpcqgCxD6UZiMcM0glDSi4-_7UGmhVpy-9HGV2Sy6JcrO8hoNS9BmaZ6bT0RfY-4jXQ3aBnHc28f-W5-ZfdKWTfU-nckPMjfcJQDrL5eDfY-aOEBvle5Fgy5Che3_zTAiRxjDgLn2ORrZnSXuNKkCUvNNUM-E1-GLJnUBEBqOojzXUfd4PfatAlntB0Fxoa_OvKu1lzNtfSwCK20o8egZTHThZgXdhljrqEKPgXzYVFUNMx1SwHt3hj-fMBgMk_daM6HoKorSrzYptZIV_xGXHP3Cq6cxI-uTJl_CHJcYOSSZ9CHveM8wZmQNgNVc9elg1xEX9Yny6EY-wHhUd2RrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-tUR1LMyUPUqKQLy9MpGv0F_1JxH5xwdwQ0eMK6nFsYahVw7KVGE29629gwWKLrVxAfo3Tvu_xmyizojloE9VoC4JozbctyihN5BLYFA1tFy91D2IpUHtAbkYgQw4pgW6zDEMNuGEzUiQ2ltzheZ_eOt2Ybqs7hJj_FMAWzUIkufbaEMPax0qNdvPwACUwO-mbp33AqPs_xtcodEWWzga-lnOGebank8KxBt6jB13DmabUkNQR3JXjYTCpJUq95yVotCK_eb9ip0Xlj2DhVHUMNfhkBtPKnprJL68mYuNj6CsahtXyzTTxCCWaXC-m09fm7T9H7SNgQX8mPAVNdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JG9Il85rCulMRazsZzU9X9N68J0G2IelkfrXMsxZ4Rc-Bg6Yf4evOKlUds-J4nb-NBOcvq_lsxnwRcFG-EQwQNMmxO2-UwicMmkTO4b_c17cBf_cNPFptbwahKwzw0H4XxMvzn1mkxsPJAVva7ihnPYMjjXWOmuw_PuXfOTL3KGI7vgqgctwqULO-7VIrjvDOIQEVdNUyqYAPuc6MORpVhgYLCm1tCo-ArsFEfwQTHn6UwlZy4emNVjaV_pHgM5zOQAHAlnu948h0uZbXgtk0XBcgPUNQKRCiSob5LXw5REJ3bMQpcLRFIt3hs4gd78klK845BbhhHW9GCcF7OEhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgLdkmXBuDnCMo0F7HOWf59lRiEC6gns-Krw61d-jktRTW1wK537uVp8rH8l7O4NAl_abehyMxIJVQZ5CCB2rDfg2tLXk9dm7GOIFeE3dRc2ir4PxCzWedhgUfygHaH8x_tEh_4ZgR_zDHjTGcBKahvjaIe6hJis5xVTma2H4-AhRXHWS5LKdPHoSA_ICDDG6ifJMfB72xb-jntxqN0oiB7imU4BJJmaxJDGCwoVPrTCLpUb4vBGuKcvfB_lWdvV-t4DrVTxWrpl4pVSRzG-nrx_iLqBiVc6lKcQ3oWdFaseNldklBtpBHfnfOaMmUz_eqWTT0wi1Rfi8BOJWtoQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXv0Y1paewt03Sajl12u4U0VnKs6WGWrLcNEVTODyGRwWnQTR2HCN0ynC-XEEyR3l04SyTiPdcjXQWbfnhelpVMjMDj6zTqJZOw12B56kLyaW7zggykgSfKmrvhCqiA_iDjTb2WeqQliDeqwR96he56pyateXPRMyF2kbqHnH3LfkKJ-oT8GcwtrnicNLKGeZ2KBvQ69Qam78mb1kSuJQnFswSj_Jm48_h8IEbvc6IRSzt4am81Uv5IwA0zXkP3m_NtHJWdW9qBrWIflpNmh4jrfQ4auB_uG3A95VaHO2qE03WqoflpxBZVtASnL2E9GUoZEYyeb82CCnoAeZVQhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtjdui8q6b0hIE8neavZhEt3uS-ICSYRVTAi5k-AhPXW46OOjcAtYvnjvjdrCyjWH_932SzvQ6yaUMbf7277lNqXoRaQayxk9CFgEYW-zyTplmJIbVCMlAcYzU_PAJkntd6fIyzg2DbbSY1t_1p4uJxpdxvRbbpvxyhWTZHD6ngd1h9JYxyagpB-OStOcNfFB9J_vkn3WKqM6Qj8V-flhSF_opbIUobqjOWfLpMAXnaXziWtU_qzUDTLESB2a9rigd-8K3JLItT-60mSPnvBD2Pvq3CXj-L8VJz7hcJTkRxyJz4uHjFcdxFVfmDyqoKtcBl0Awg4lGc6EzBGNX0d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLQmh_DRZUo4t5B-Anel3kmW-03Jr3abxO4YhkKTWgL5afFRpbqEsQoPRiIXPWF79GYdCKJz17SxqODs9J-Aq5O3gg7oiNwhB70rAtXX8JjknvjTxJPRWY1XPIh-iF27HKGO_4ud8tmwIe9sJOmGISdih4IF_sjAZ3FloB2BU9KgyDcKGjiF4uhmyf9-5ZKrWh1bbIVjXFYOxPoOxAjUh-otTk-a3lKyoqjZBZlk3fMc2ghgmLqnkgMtRzgkrcbLKMScPiGQjSmPZrxSmj_WQYMadfYfCUO5A-kRJ8AMM4Btob0f48tMPgdjdOYb2KyAYfh_KTWf5_DBufu7GFadDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXCy_jMatp9LiGkxB5kVP38esMab_0xA9MrRJmjpESxKyvZuNlBeX6r44-GmQD2gnTXOeVEhktR57LOj7jSwZRAcWTIKK0NAUhm2xEa41-Y36zYw8ZokBoyz_qqx8zxQ6CnmFtJKXxn5aoYkT0OFc6Af9LByL9DD-VBBhWNaqUyu_cpMz63wMuyP_B4CL2Z6HkakmydYSmu3alJRqo5dVkWqNesViWEj7r17i7PrMm6xjR3nLCTm8MH39-FyVWXf0dAhv7ACHkmKMpJGnyjZD0GlXT44J9PF2180UHj60uRv2l3j30PTRNBoGYTpm2vMGDsHgnLC9V44-QvYHL9JdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0AN-H2Ov3QMgGCEd_aQCGxdaxVLYzOv5PAOlDE5deHBSFIHAaoTZzWn2M90OFPExZOfrwP5BwJrCavDnz5--vlCIV4uY4CDxycVLdGGewfUD4x1PbkgX3WP71PAoOoGX0F558C9PdEad56APg2cC58iC0zI_oGy9S00b3wHrZpsgAqEOe1dqnSVi43wiLZUD7BLUKBO5Rmqf7-cgoZ67xSDdSp7PkljmTXrCseRShIZFldDU4wGyTPa24uPIwv4jPCHg7kve54B3YPORmqguUHcIBY2zT9o_y36ZpSflKlCluIV_PReWkHY2eCu2jUKFfd18nfgxjpVdx1BMbFDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
