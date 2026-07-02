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
<img src="https://cdn4.telesco.pe/file/F1dfKESAjAemtbSeg455lqDthi_uu8Sv7zOHVzes2MYBco25llZ6V52_JhjEBXRbxIH-ExbRFAYpNg_RzzYorGzVPPW5fqdXNgz_WrIcUKUEKDqfKF1Jx2PTGnsmt7cmis3qD71IFCaqI3JTjKgatYhu3rrWsjXFV0QFpUwNnnlqOfTS3OpeukYbaHpRgGJ4qx6M8gC5BDbu74k7i1FfNVc97SyiaXn8xz6K1llL3eiNbGZ08yVa3V2v7IvvRrc5UQgaWATUjlfWadVydeXIvhnVn4T5P28iNlUS0c0oOtS9VFyIszuDKdbTzE8YOthZa-I1AjQ9OY0a99_fzlEUbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 359K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 05:59:55</div>
<hr>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-_YS1f924PRXZJMro_kvNM9NpVdoJpgux0C5Z7PzxR0Ri9jKM2KFTjEsj-Ga-gPVlIzqCW3DB2lpT1e_AoBuOjui2xz6cfPJNxMsFBGZcqwo608DDkpXYgJcoEO7R3zljoqoW_LlOohw6imzm6TNKJGxLYNlWgmLvKQyoWSdwTjmQdh41MYbWEEof2BX79PLfrzZ21kAIJiA2cvXJiJDSWgQL1ZcXqXcKlN2VqNZl4wTT1eOLxfrzZtEB-gh4bzccnSCbwmBB8XJnuEUdGGRdyFzd2qz_7jCp5Vn6JOrZVsdLc2gQFztjDMxITEwH2dW8EldywsOgNtqZyNUzsx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIokwPS7kSuo16nvDGQjCT8HwY7-vuHGJPnnMe5awpEqLrQjZKZ1pR4gU3AlCQmXJ6e8qH4J1wi4m0Fd2mz4iMdmXr5AIRxoBY_hrGNozCr8JZZRmkMOS5Qs-HscDJ18BuoZO5biNT9Qs0CAFwqhZkyQr101qX6m9945blee6xSzHXkzw1YQmLBT5n1Q3TDg5q6Z499NJAr1b1GX-_HBQMZemFCHEoh05YMUa21cdcXKqTBFvBuHw-QVR2ikkw7-8NqmCVkOPH2NOEJ2ZgYgtMIuSfmSbJQcpltrJni96YD4_AlUGfhBij0UaZUWhqYHCYsv8xPnDRPNL_fkBTeQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9G5DZyrdAlP_F7Qt4sNiZqHS0O0V4PfN-Rnb6mF9vfvfaiZMmeVew4CETXb2k8_fNP_x58RBNse5-01RqiuYAnM8hiHIXLjr45wcqXWRDfJf051ff8cIkfTy614Vyf4eoMpHTSM_HB6CjHghz5VTbfeQb6m8R9aM-6NbqPD32L-ajiC8rI199_nHKcLxZOb0_EbvC4q3ZXVXc1zwaJ4za_nZqbbjS-xxCatRRwRmv-vXE_riDngg5abjhlxebzPXqXKpYh8HBS4RQwsbt9WJXv3wohiP0cehVMtugRZ5BraWzfH3gZT37Y_jGXzSPmr0MVlWalof2oHPjKGfgIrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAupG5wP883gbffodbhRc-GQ0FH0mSn3xPxNLDvPWdPsg9K1R8cZq88dgcDPtowwUQeNy69j5d00RPW6XQZivELgOpl-2-tzPdkAP1RRj8W6BBYOBpyKnoPVWZHcMyjjSxQgr7hOyWiU1p-bOwuwWF2y32jO5iak375EDogaDCzbwFNiJ7LTQMQPYPBAPtG5tN8s1QNn7XOkTA7J_oOmnvwBJF3kTXKIGiK3EBlLspxGoOkrbteIc5rXchGIIfjjrUuidAtPbIkBzu4DFQMJ322a9q321I4cIlPyZfpFTadCLaEuIRR7IGanz58sogTkcdTRkeyibUC2NSzKLVyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24792">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXFVjwGllAuGsrL3myMggUX3ZmcurWFNU-7yfEMnX5ihxY10Ns0xobHzclhWBHY-71huCcyz9yVnqyKTS3lJsE2Tu0LPskq7FLgtnwZwFJ2GoLZX_1NC9ESAa9FF5q6s6ua-AKmrtuX_oA6c0IwIcI6vRj5CRxgu9d8TiMdZcVcNPDZIe7h7swYSAyP21qhIbrj2X--J1IS4i-oKICNf222Exb4FH16Ha9BBaTZiTVZlMZXfUYg4Mt07VjLQleyck18mBPwi7nVgtMvOYiXWFRmFJ5LemJhfZEeaIx-7PmV1KfhOHkAOr0kvgha2R10riUYzOPH6ODiGBPfQWPh14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
باهر1میلیون‌
🅰️
🅰️
🅰️
هزارشارژ اضافی بگیر
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a10
@betinjabet</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/24792" target="_blank">📅 02:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf_vswQvMJfRyR2Lqtfoqhtx1vD1JXju9dtXoIF0l4XZTRp9efh-7-3yqjo3f9XFQpe8luLrPoF7l1-9_MdwN3KL2978FfQwFD_pwbnejfl6KmxyzNxDNZGwGTFYamaTfkjxflPIlML6mikr45gBcIMdqxsE_s4bIBCi2AWzLVRPE6sV6TpRW0OeRj89RBf9nIZq7J2El5n-CFchrubhVibCkJd_B3tcp8lyEVC3jJMtWMPguBF81_UlPQpSbUb2LeodhN4lxvqpLrrRXBIK_GqEKwjbkWRMwpNhmjIHDyh0DU3PA_xn_CF6dxa8VtD6BhXoqClu05Rf6ICh-6Xwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQbv9sAN2GxVTbqNtjx2zgbGo-sKGGvgVRByH5pHR6jNHtDHnHIagraAIKmAauas7fWRstL83weFDEWuzN6yvCY7A1lFLpGE6DHKtn3_qL8R5MIUgSZ6rLOFdKmKB8-fuCZ66Mqe0ry_dO-9CoypJU7Vv2cJJ8fMdtrD4eeG8V5Q_qF24LpXnXJgrfLGCTYm4wd046MByK9TH3LtuRGKlTH2fSz8cALm4ScXrCL3EcaJkESevBJcILdPkgAUIsY1hTSlZoBUruCfnWCOVPeMajg2_RZbgZCKUXCJ4e7wlbskfpUbfWQKwgQArD25_k-btcH5IgQJeZGUSaf7Hs9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7ul91UFSyINwoTYKKR5X1u9p-HsjLjVA8k6bJVaj7tq8cF6wH7d3J7YCGCIeGOMxU_0hCEzwh0qPwKoIlpTg9vxZeGm0zR94P4KfkCqKQpLDKoYiCa9U67Z2XBNqu16FP3sf9l_sZrCZw7P7lxNagOxcTxOiZEWHSs8AhX4xgR9gkCBDNl3Nm9V_uqbVRlmY3oheLxg9fbJTZpCBBnZ5HjSjehI67plV0J2yZfssf4lsk447cG24Oy9feWTsObvAhLsrVIH0Gtc4B2fI4JYxF2Z8IF7hny2x5GZu_WZNiHGUAFFp9RdLJAXnmuV_FLsTHSWS2f5CPQY0WYxLExuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy8PnP7gG0nDb6HTT_pfu3WR-x2yOnuByrJzqUEdZznCPPz4mqLipQt1CE2rA04QvZ73u85TkCts5nrMxdV6LnAXj9fhjBcUL01hGcOnX1vNuVR6dj-pozWZ7CXXaSkORxBI2UlaUoqHyzOdIIrOpChWUsQW2cgktQS2HfYlvScyyVRDpgfLrlcY82l05WKk_h6AyXULOEJpWXDCRwNR-_rapAlneoIc1X-Sc5zgBHnx8KcEN5yb-sbO1gF7VLKFfIbJUT55DUykV4OXgfgjlmptpAx_2KLLYE6yKCAZ0F8vMrPcTzYv47XTLDR-wZtA6TolSiXSWvoHikfKjorqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzOkaN0WD0ZfIuvuFJOxJsdN4H1k-TSFgDN6Ihgizf2ICD3PgigN828hIM7gH6NT6TG38l7Bw5nhn7fN-8R5jhTjgWof2_WWF1oyd6BXL3LeYIQg4QYNncuaDBIFrHAPB8ib7IXsUgedSvts-_2pFmk-Uq0UKzGkurVrZ7AJwp01L2RRLuZqESMGwsMJjLCaH-_Kg0QvKYi3jCWEAPXuQ_Ixd-kUujZCOnE4Ap5wiHGLlDdkozDz4R_RloJSQ7fN5BuEVhvx9rvTSsTDpkWC9g9mwoV-CDVFr3lXdS0zoMs_dSumbf5ouqhxzzszXjU0jhT8n6RXFbkjmUhl9K6FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZtyOPW_ilcHukP67Z41eXiQOOAk08ShFvkZ0dg_C2nAuH-b6dahn7bC27BscBxc7SYylIBapL0_NVqX6aKJa6gQ-AmiOVbgsPiBdpM4jjE2UtCXCZmkznx2PgV7j8ipVKwQDmIRWtTRnxiDTxsJnWEK09Tf61ijmk5SLXT6AXu-EeDflPCm2GG_Navv6ag8k63NY6fG07nU7iJqrKJKjcVry4oi0W9BWYURV0sCEzv0POdCiiOdmzaBXdRh8aYzAILF6U-gc0xOt5VJZ-x4HYMBV8CzawJaXyu1CEw9r9Qo8a7XyK2L_gQ2AFDnFUXkYq8_ELdAzgYC0uN2jM3Yl0Vxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZtyOPW_ilcHukP67Z41eXiQOOAk08ShFvkZ0dg_C2nAuH-b6dahn7bC27BscBxc7SYylIBapL0_NVqX6aKJa6gQ-AmiOVbgsPiBdpM4jjE2UtCXCZmkznx2PgV7j8ipVKwQDmIRWtTRnxiDTxsJnWEK09Tf61ijmk5SLXT6AXu-EeDflPCm2GG_Navv6ag8k63NY6fG07nU7iJqrKJKjcVry4oi0W9BWYURV0sCEzv0POdCiiOdmzaBXdRh8aYzAILF6U-gc0xOt5VJZ-x4HYMBV8CzawJaXyu1CEw9r9Qo8a7XyK2L_gQ2AFDnFUXkYq8_ELdAzgYC0uN2jM3Yl0Vxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD21yl0lRgSEUGoc7j5XX644JB10mTdlV73V9tOHQtyWas-Qz5EZ3wCuKlgfZocs0OUjLVUd6eUx-1rtiPt7SulCDrGyLMaB-s8XjH0kz2YfKHSEn9qPk1RG7NLFK5YiiTS31Upoxo8th9UcrN8tXZacE-C4cCXyDKdDgPqwbNGGiO6RzD7dlUYSDLb2JLhE6GGbAg0V0I-5icxM8-1prrhGhVipeRiP37VnDSZXESWId9HbehjE9AyGgERyY_l6EUFUe2KJyFgzyoBHgFSmvW50IF30jrDcsO7zKvia9q49VVvpiVZFiVJav96Dyx54n5VYKmyeZAnkfZA8ouO85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsuwdhKTk6awCxIv-2uOhh59lYfTSRd8ZMOk1zxAAThXcN7yavTzHr8lujP33PriakNycoReYg4FtaxRC9_nHJPqnhuDgAHiIkk4qJu40LWIRBqyCgNkgZUYS2i7sGd4on9RiMGHreYBnSL1xGoyhU98xm9z_X7UAa5sxWah2jYYhaBk8nYqyWilzjlXOo1w-Xq3b4nzlJlr3j0kp0s3jeTK9F6ZhrL21kC3RILjLCufQBwAx0P_U3PBK2U-pkKlppzGpnsVAxsfoSVeMk42L5UrQNv4eeLdBssD_djYyuK1Lkpe0qSM96fzETX3VppdykT46XwvmUiLm8mDnALnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=QsRv-H6mO4toL-ghXl9wTCvL_RyMAo14Dx7u8ywM0QV_f42hdE4tWkLX8GSgr6kDZPuIu-igepc8D0G2yIYNv0Mo9EdhqaXX7bN8nXBt1ZZ9zOYY51K92b_0Wp-_AfZmYsAHa05lJgz70DxovaneDZMV_oAGRtx-_AtliwMlXEiC9str59--qpxdDXngkXMWaa3-2qAmoqHM8iQCfZEuTpeefEB7iCCIguqMsFe-FfP8veFmqGxqBSslfbTDU70CVBfGIfnkhldWoxBpONDlHOWKFK47iwNVSo04165HWYi7uvcIQhDNiZZxdjuW8fFSC9xnydKh6x6S-3jehXBMLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=QsRv-H6mO4toL-ghXl9wTCvL_RyMAo14Dx7u8ywM0QV_f42hdE4tWkLX8GSgr6kDZPuIu-igepc8D0G2yIYNv0Mo9EdhqaXX7bN8nXBt1ZZ9zOYY51K92b_0Wp-_AfZmYsAHa05lJgz70DxovaneDZMV_oAGRtx-_AtliwMlXEiC9str59--qpxdDXngkXMWaa3-2qAmoqHM8iQCfZEuTpeefEB7iCCIguqMsFe-FfP8veFmqGxqBSslfbTDU70CVBfGIfnkhldWoxBpONDlHOWKFK47iwNVSo04165HWYi7uvcIQhDNiZZxdjuW8fFSC9xnydKh6x6S-3jehXBMLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQQA4p1MBoimqsJRiz5fMRWp8rXm83bLyX__c3AtD5C0sy-OoYyVPhxCydO3dQNsGaMDJBFmfmtpKUbgOKTmdqA7i9KH_Z6GTk6_rXuBFoicOXCLSEUbHwOK2HiiOsG252feYB91_y_b2vILIxdJ4wGAQOqyejWGAjJ2vqsG5VJvOqLnPFTvEUXRl4PDHaaXSb8PeljuqN8YVEg8ROVx9XylyqlYv6IADSRRCMIANNE3Jexw95Q58C7QtnWxrDufKZhw8ihmJaaoDvnH9M4_uND542V8qgVDlHD43aJNv-X2HO_5bBQOk6m34QIL5KqPMQMSJBYeZKXey3cDQsjTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq0OF0aqoF0u3Y26MXkMPc69awtM8o_I-eeVvKCxVzImwLgvLDh_v7hOmWyxAo1TQA3SMlwZjuZGIPmxlrWlgUiLGeyFKyDczSVDbgkr-ZKI7kRdqs8L4fc0FAzYTniUwnBDwB0SRzRyIEtugUn4VlvK5Au61cOdba2P6MIUzvjog3aimhEtPx0CyT3_gC2Glu2x3PpUNp5N3g0OuI9em50j6MPgwUuZocPI3ycXUEOzDNlOkx1yRB50l639xiEG_oYCRf6YgB56vA7Nciflk5ruwIJVyYgSaovLQm5h_5RQxTZ7FS8K3NDR9GGc6wr-JaPwve2_vLO-PZhYM-FRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzljHlNgf5e0XuD1bRDMiQ002qG9R4N1l2BqFv35ZBMtD72yE6hsFlZQkcsvxTXFYN3FWPOQX6D0-XdsdhIsPcI39tqBye3b-R1H-XvFQZmf7D0-qfL-KQCsMwAZ9KcxG2njFrpYg5GGroHiVKnu0McrDIvYwb6Auyu1YnL7iWY0hOXI2-5W4K-Y6ClAC4Cw7IhjE1KjyeS8-AeDlQgKVc1kKLMhjbS1QZX6HWJl9s2W96MWNrqc0ymR5MX9G7uv4uXReeY4KlfXpsjPcWup_waBv_KG52D-jW4_zS-MKid9LjpC9HtBaOICzSdHa3_dbSz0byij6RZhW2e5jLeONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
پيش بيني رايگان ورزشي در لينك زير
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=brhhSj0MjkvtSQS5rjBtM9Pt9joyDZ5CDmGHcCr5Jm-IUQHoez7IrR8H6ejIRU4ImvZgseZiwp-opa8pBuyTy3DzJlM7M9hR1WyIItcTTPEg9NFaNirpK-64CLgw9HPlCcwqbZpkUZDjqAGE8UiXRHnvibMQFuITIrCa8CkNzoLa3sA45Ak4jGtRTg4RAOb857N_puCSxYonHHXqdd8oxmKJGzAb0FAaC1E7Ujs6V_eJaOOEVeVrDE9CPmXuwthM0k6i-yZFpfr5ZVSBD2Byd8A59SwhPWN-G2-6zQJbfxY-GAAqycWFll0gdylIzrPQhb2UG5u2x31oYh17dBJJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=brhhSj0MjkvtSQS5rjBtM9Pt9joyDZ5CDmGHcCr5Jm-IUQHoez7IrR8H6ejIRU4ImvZgseZiwp-opa8pBuyTy3DzJlM7M9hR1WyIItcTTPEg9NFaNirpK-64CLgw9HPlCcwqbZpkUZDjqAGE8UiXRHnvibMQFuITIrCa8CkNzoLa3sA45Ak4jGtRTg4RAOb857N_puCSxYonHHXqdd8oxmKJGzAb0FAaC1E7Ujs6V_eJaOOEVeVrDE9CPmXuwthM0k6i-yZFpfr5ZVSBD2Byd8A59SwhPWN-G2-6zQJbfxY-GAAqycWFll0gdylIzrPQhb2UG5u2x31oYh17dBJJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiRQCB6HVDTk1GYm7AnULUAGeDIOpdLGC008F5EpKwZaSyGQ8hqgZgqbTslYfK--c19Ymv2mBom0TTJ9KkBjKECUbrttpTprM0dEG9TdG7J3IgW-2lzCWFFIO6_FF2YMEAuX2MLS03S84fZD-7jJ6yul1YaxDz1LP664SQpTxxBVdKYQPR57Fz8OKs5w8j4AwvkGsNjjsTenzGBeuTTL264_gMT8TRWS5AN9C6KXCfneBDyGHCD66Wwt6kO01P7q456fJYmwF2zzGF9BpbbOrKrbe3Yr7JbgYKyY2ph10PZPg46Oho0i1oQk1psWZuSGVtx5QdGYWB-9n9BMbjA1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=QnA7WQFCBbO7CuUAbWyztcukbPhyQJRvwgm5MSHd2hTJD8tswCMr-leeKcJPQ8vY1DMf1abZ5-7aaeFKNk6Cy4ZXLvMNB2qZV5Gt1q8_U4WDsAGH4zWj0EGmRcMnyua2Gg7shD_FU3r6dvL5R0uqDTY9oP7oaPqb_m4ymixPxfCqxJlf-1KwxMyLAEcLN78qZyw1Dv534NvHd1eZ8f93jM6z-r-bEHZJsqbKUj6SPzVbbkytZ3pLh82rjFRwqHtIP7DSUJco2kM4tcSeB2jlVT6h0G5TspmjLXl9fb_pLwm0A69AhrJn4JcAYdedohyAF32IvxcekyBkLgqyij8vFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=QnA7WQFCBbO7CuUAbWyztcukbPhyQJRvwgm5MSHd2hTJD8tswCMr-leeKcJPQ8vY1DMf1abZ5-7aaeFKNk6Cy4ZXLvMNB2qZV5Gt1q8_U4WDsAGH4zWj0EGmRcMnyua2Gg7shD_FU3r6dvL5R0uqDTY9oP7oaPqb_m4ymixPxfCqxJlf-1KwxMyLAEcLN78qZyw1Dv534NvHd1eZ8f93jM6z-r-bEHZJsqbKUj6SPzVbbkytZ3pLh82rjFRwqHtIP7DSUJco2kM4tcSeB2jlVT6h0G5TspmjLXl9fb_pLwm0A69AhrJn4JcAYdedohyAF32IvxcekyBkLgqyij8vFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdKkiOeWpcFAkScvjbROlAoALKZgSp-HZxGw9AlDZwUX8nGJQqCbmysz2atnVpjzMCZX3uhQrzDnV4pikDnGSz8iyrCCj9jSkDywaPTWUIw70x8M9QjctkRaXzfrBPvgFnmlbViqkpJnllUQjFpfOZlgarCVI5jLg0gyMMXFYHZ_FZPYQM9Ge6phrwEzQCmmAqalKXR8FWbmTJN6-0wtLbnZlrw6tPritJ5GaXsQCqB9x8B-Kn3Ywv0M5ia-ZxN5T64Np-S9zMmeOQ_8aV9fhQXuXSts-MwUfJCYtK-Gpnt99t0TqkUMv1hZxrZCcXI4wdRJzXwcB72VTysf_yi_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT3cBFGggEsSzzLq5qArCVIEBfpKRdc94q2tIyQ97vgeNHy5ePo7zvkGDWPuNoVQifV0enH6vnS1gDA_s6t-bZqaDbAZVKi7uFP6a95WA02L0ezgerl9tCnaaEPNUF7WF2IVE5Nj--IWIT9b-jbLqh8uy3tRwU0Fo_rl0K-hRufRoO4CSqAac3VdxjLcgHU4t23hzd1UEduIou9qevqml8UsBZpi_JyldMOPi99pow5ieOV7alGAoUr94cuFBSeWmITxhk8uO5aGhpbrFopohXDnUblaRoK3SP4t0GjCYXot57xAudItJpK9iCeaM41gtQrZ1iJl_oQNOW6NkEsHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=pSXRmNbnbTEZj2Hnl_XSODfyV-KaKrr-3dbVXGM6W6AQdNbxid_2xsRlBqbjlSpTsKgKqgw1QfGwLxyEcJtmv--6CyRX40aA4VNAWyxvxi9QAh_4alRQueD0as0olxTF1aRTo4x6H_XQIrVde2f7MJ9CLv_oNv52USQBsEnD3WMECFB6E5EEYNQ_GK1yBXom1ZPSWINmp10EbKzb0spd_RrF_LKlq7zHnciW0ZYRj3Fg4dVYD8QPQ4zwv_3ex9PxF4dhu6IvoRVB7M3g1Sm4JUGceWvJO_Jrb2SldBqKfIclabHlfwsd8vdfgsTtIAaLBPu7UdqZntE2-SpaD0xr7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=pSXRmNbnbTEZj2Hnl_XSODfyV-KaKrr-3dbVXGM6W6AQdNbxid_2xsRlBqbjlSpTsKgKqgw1QfGwLxyEcJtmv--6CyRX40aA4VNAWyxvxi9QAh_4alRQueD0as0olxTF1aRTo4x6H_XQIrVde2f7MJ9CLv_oNv52USQBsEnD3WMECFB6E5EEYNQ_GK1yBXom1ZPSWINmp10EbKzb0spd_RrF_LKlq7zHnciW0ZYRj3Fg4dVYD8QPQ4zwv_3ex9PxF4dhu6IvoRVB7M3g1Sm4JUGceWvJO_Jrb2SldBqKfIclabHlfwsd8vdfgsTtIAaLBPu7UdqZntE2-SpaD0xr7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goV0QbORaP532yl3gM8JxB1lv0wpizHpYmjv4yrdHZ16xl33u6I_ov1bUyWcd03KFmwh1KryxD4pGQvEZpfCkzuu0pPchKgpTMP0mywKdLDGOc3uoNKq1g5yEcCXXC56ZK1GNUGDsgprvnlqx87Rld7AYPzQE27JdWG9QIuN5aLISUvju5DVEVyUWLTskXGucgWJagDOdPel6VvRizz6ctukbwO3weRTKpqCODEa_oG0-dlaA2SOd5h25I6W2md11jBKoOd-Fyty85wXPk84QJmccjFdy8ReJ1LgW5PBB1KLiBX1ux1Cn9wm_8kyanAi0oqXBzlCKRZkCua_Bu0SXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
پشماممممممممممم
❌
❌
❌
مکزیکیا بعد از صعود کلا کارای عجیبی کردن که یه بخشیش قابل پخش تو چنل نیست تو رباتمون گذاشتیم:
دختره رو، بدنتش رو در میاره نشون میده به همه.
🔞
مشاهده کامل فیلم
دیدن فیلم
/start
https://t.me/nod_ppbot?start=d3c61e4fde78</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24770" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=FARFdHS2XecO_JQH0yAEbWhEthViwaegPML17kmmdyCBkKw1x4N882EtPDVyLhFfZLnTd5z1MwQ0Y-Fs2k6NZ4lEfdzi4D6XD9WMA63BgfRD2KXfx2I-Z4u5_6iQOXOmlCv13Q3MxHDfbKBnDJFUd_aYE3xcmxc7khuuyhm4wV6QGsIGd-jaVq-31BRk7EI9kShHrfps7_hbm8SxtpKA4fwEG5KHcDgXIo2kSF5PyHrHXC2egpeTzoOFg-__dNPOaHKl6XQZuZlr9NKWIA2sfpTQL19rfSavhlHN2V3JeqGiOkAp6L7YQqkZKbpg2Sfs5gU91wYg-qHiDw5L9G-i-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=FARFdHS2XecO_JQH0yAEbWhEthViwaegPML17kmmdyCBkKw1x4N882EtPDVyLhFfZLnTd5z1MwQ0Y-Fs2k6NZ4lEfdzi4D6XD9WMA63BgfRD2KXfx2I-Z4u5_6iQOXOmlCv13Q3MxHDfbKBnDJFUd_aYE3xcmxc7khuuyhm4wV6QGsIGd-jaVq-31BRk7EI9kShHrfps7_hbm8SxtpKA4fwEG5KHcDgXIo2kSF5PyHrHXC2egpeTzoOFg-__dNPOaHKl6XQZuZlr9NKWIA2sfpTQL19rfSavhlHN2V3JeqGiOkAp6L7YQqkZKbpg2Sfs5gU91wYg-qHiDw5L9G-i-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL7mkKiJ63VSCJLA81Lv_cjpWEi-PrsW1S1sQ6PxESbBZa-rp16nVzMcKmGobFkhgfYBaWfMi6GAJ6Bcjwdj24PKb9aD8tqY-NuNEwdeezuqEAbdnD_5EPDV_ArLOCVBFZgJzS-AaHETNh6rzfl0Pddt3wo1orbGk2PQ_DsBwDISw0k_fRyxPiDhwt3lfJFHgWmysZQ94PK6mQU8VBGE7Ro5Hidi16AiDFiFrLTiARf2-542a6FB_9NIGIVGPqD8dARqq9HGqviUrBXGwuEf2l3E9Ldk50PXyVQUfpB5K70ZlTpUDV7CFP2DThfrlK6QjnCSS9UpI9cOk5QP8GkLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5bZTFXHWSF69-MVXf1W2YKXSnwGcSQ64BwnYEUFZjzo7r75hxyVJ8szFX3qgQnVhTeShA-Q4lZo0AYJC8iMspc6F8vBFH-LTfAS6xXvqsd9E2eML7MmoGScezYNi7vtgzFo3duNC8fBCXjjgitYjChh1KCn7t_5a_N9bRhrkRBto4jnRzZZXzRes2lYmyIltneSzWJjGhjYHCSTEdb5-Wd0Oc20AoK8n7l2jgsoRwjmzMxC5acIw5MFMp6e5oq-cgSfuXiLaT25guQZemTu0TQTs9gPkssj4Wx-3_jZfwyMlUqy3cz2AHTMMF7WYX0RlPULTEanS3cPix0NX9h-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym-vGF2MuCwfzzF9p_Zf5oLfzlX_Y7mRnz6See-e6STBhNUhS3gcSgQlMsMluQ0Tg63sD5TuAcp06OLVJawNQO-3Iaf8Nrkt7IMAlEhdiYjXL3lSXmjzajL2cftkqyvyDv640CTi_gsj1S6pEU28Z8CjSnfwWSanar5oYTkHg0EevWokRijG2Vrq4JFHxtOP6LRV0FAzlVgS1X005Gi3DVic1okXNPGj6iq99HEXBCDu62m1_Gj4V-lg90GYnLR1vvYFj7kN6U5zO--8l4lgTEFdtyIKoNf_5GSGio6BCbID2zJXuaON_KDpBnj3XDMHioxCqK2dRiA4od3VlHhjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=Mx3O-pa_iOmkVTa_2Bz8a_8wjel5skE4zSl5Azj-MNafpeJ4X6HwgpeH_y63v0YHABVp36orTVeF6H0BgKsczlR2ZzKZ8w1AH0CrvWwNQPftGzSoM6ggV39eAgqMbuHjql7WF0l3vfDUkScOKH28oEGQEOKYD0QsIlLnfMNqPmycEmS-nP9xiW7RdZqFuyAlBHXaQDrjIHZPSr7EqTQf_akjPrnOU90mDcXfZL8_RGuP3LVldkBS_OxKWk3nOcBZBJOzVNnnPaopI4dd3B1fP9EcjLQtR2imE03SE6kjZ0mV_n1tt4K9ZA7gwepBuBhZYdtEWlC-zjzYi1pLz20FjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=Mx3O-pa_iOmkVTa_2Bz8a_8wjel5skE4zSl5Azj-MNafpeJ4X6HwgpeH_y63v0YHABVp36orTVeF6H0BgKsczlR2ZzKZ8w1AH0CrvWwNQPftGzSoM6ggV39eAgqMbuHjql7WF0l3vfDUkScOKH28oEGQEOKYD0QsIlLnfMNqPmycEmS-nP9xiW7RdZqFuyAlBHXaQDrjIHZPSr7EqTQf_akjPrnOU90mDcXfZL8_RGuP3LVldkBS_OxKWk3nOcBZBJOzVNnnPaopI4dd3B1fP9EcjLQtR2imE03SE6kjZ0mV_n1tt4K9ZA7gwepBuBhZYdtEWlC-zjzYi1pLz20FjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVrXXsBZu0Xll6bVqdMfgpgoqZnnv7WzxHygGx1V-zjNmjIBcr7H75qbWz6Y3SagKzyCABG1qxT96hGUyDWEqDsfEfuVLZbqPxhKKkB0CpX6mzHWKjKuuUUa09jCN7KmE4l4hQWruGBwNrubQeohoaXRrICpoS-JAIjPhQzOSTfUFOJIRWH-iakcPb12IEftHxbKlfEprNK5mnO-zTNl9sr-j1oIANCwF348tq5cW_Hm3CCQ4Pasp7n92jCGqJFRQUMfTmv8Em5Br6ODzADpUskPDatmCornXf_rZH8zsZ7fM17yr9_A5ofyaDtNHjZUDs0AIPQ7VVCUtT8X_U8yAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=IMD4Ppv0mCDZbvgIVCRn5GYKFsaFrLEEg4cHajuesZqPlFZmDordB-FazCtLfBphAbU5kSPXFXbB6JdvezbeD61p89ih_lxByfc6_KpP4BXOhBvTYN3aDNdBnaCYAqLkP5aLpB7NFO2vtGsV1O-c3W8wPY-shcI3prqFMah6TfsrBiYV8OK1yrWHT73w8_LcpLcikinjQvICzZTXGa84cQl2PZj3MYo7J9rwfBV8otvM5TRhR2lB9P55YgwWEkjG8PQ7SPEzozSsduVS-6LH059p-_1BJmqaqs6hLCvT-rVcZ0y0fdyOKP2SQw4WalTFy5dQVvEayRgDmapeXzYSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=IMD4Ppv0mCDZbvgIVCRn5GYKFsaFrLEEg4cHajuesZqPlFZmDordB-FazCtLfBphAbU5kSPXFXbB6JdvezbeD61p89ih_lxByfc6_KpP4BXOhBvTYN3aDNdBnaCYAqLkP5aLpB7NFO2vtGsV1O-c3W8wPY-shcI3prqFMah6TfsrBiYV8OK1yrWHT73w8_LcpLcikinjQvICzZTXGa84cQl2PZj3MYo7J9rwfBV8otvM5TRhR2lB9P55YgwWEkjG8PQ7SPEzozSsduVS-6LH059p-_1BJmqaqs6hLCvT-rVcZ0y0fdyOKP2SQw4WalTFy5dQVvEayRgDmapeXzYSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqlMQCHvGTh5wLxe8Tf8CFAT3Ahg06T2zSBGHRD0rFvIjuCEO228dsedjZstVlPZjKPQ4UDElS_--KlpbslWqqF66-Q6-cPYYCdQVrih9zcCEFlgC4tAR2xOow7cIm-pPX6yUOFauYGj6N9SmBhUMSYhvvlVNRYZfwmpJduJjVRiH_71xxS6KRW7CaJg_QpRsjMzyPdzQPjhYC7A2eRo064j3dXj1JCKhdECNGBfqtbNtR7LtnENOJrNnOPz0E5Ss9IdZVkHwBFUonuiM2Q7mUCV7PQkb7z8AKFcjC05StgpbLEevRd_Xf_7ucUwov-tprB0KZZgC5ASozNa7ilq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=mVVXLm4-nKQgdgkoDY9c7m_JbErh1wZ5NS8xR2yqMKBCkjtx2ylZ0gstVCunc3goT4C0T6pjz_V9FcseLLvd1YxihOqxZc-rjYUlSvb7FYz2InEc5lYyKsNYxDxCj5DgvLSyj91rwAoSGBEBHxMizK-wWYP-6STuCh3dXfqh0lN5CwMXX_fyKnIHjJckBWLBfPtCWEv1JJ-x9IB3QEQDynnWs5uB49DYOlSQdTXtQ2SmYgDqlrLyrVzaYWpKtT7JdcWSqwM_NEjZsRSvQyEQrHFpHuBCRNR7sKvC5qXYX99PDB8ZAH56HGS1ePbx-4o69Zjn0Mmc1nZOO3Nlk1u4_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=mVVXLm4-nKQgdgkoDY9c7m_JbErh1wZ5NS8xR2yqMKBCkjtx2ylZ0gstVCunc3goT4C0T6pjz_V9FcseLLvd1YxihOqxZc-rjYUlSvb7FYz2InEc5lYyKsNYxDxCj5DgvLSyj91rwAoSGBEBHxMizK-wWYP-6STuCh3dXfqh0lN5CwMXX_fyKnIHjJckBWLBfPtCWEv1JJ-x9IB3QEQDynnWs5uB49DYOlSQdTXtQ2SmYgDqlrLyrVzaYWpKtT7JdcWSqwM_NEjZsRSvQyEQrHFpHuBCRNR7sKvC5qXYX99PDB8ZAH56HGS1ePbx-4o69Zjn0Mmc1nZOO3Nlk1u4_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8EEYrPQBpwAOQa5vtow9SJognrEWyk01c-HE92-EwX65TW30aiNJgt1_nQ4BavG7RfgRCLXbTcdibe2IEmo3KoV5sN1Q8jBVOyo1Z7WAwRVY-p2u4Eo6EJXusSLuAE8GNCFcjQ4SG9CgWehIfoKol-fsm2g7bvfDVgug0fNX-fHU53Qj2CywmpQrTeXFo3bQQ78zZ74dmd7T-cY27VF7uRy76NBC7pwFoRceRTYFWgZZZ0e0nnksd-Q4P2DfAdb-jgVBvABmTTKdUu7Br2CW6mujxFKFRjEssttOckj2IN7BXHey1RQ_kvamG0rOOx5WBz3Qlr6ALBZwb-mw-JOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9nmSjulavPBOxsnbEFdyBLRgujrU_HHWzvm7I_fhPZ1Mn5SW-rbiJSBjmMy1xCets3eMpH9DbvWqfHpyv8bLM1FQ2_h4BCw2j_IYfZ4a_XLIxulBjhb9fCa3uqD7SdV6-U3SAI-R3OXkFjBMXGxkexLnOP7asTjG3kJwzSFaXz08rT7SDITJot4opQL-gc7wlSSN4Nyt9ZtYGJQEoe20w46uFT0PtXTXZiFS86-Y051I9DPG1O4xpA9qJGkC05wtf1-p3y6Psro2iPFBWBV0j1oGdVACtgAZNlgU7e6Jyhn_9vJiyKupGmbSuxoCC3vHUydvwRnAiwrkEXp507syQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
مسابقات جام جهانی 2026
🏆
🔥
⏰
شروع ساعت   20:30
🔥
20% شرط هدیه ویژه شارژ ارزهای دیجیتال
💳
امکان شارژ با درگاه پرداخت
🎲
آپشن های متنوع با ضرایب بالا
🎁
10 درصد فری بت به ازای هر بار شارژ
⭐️
برداشت زیر 15 دقیقه دلاری
🔥
همراه با درگاه‌
#ریالی
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
10
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24759" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sxhh2N_z0siBDjKtEO0VzWyZYYXT6xtcR7uX977JD7OHkL8JrggtR9kurvTeMKvKDYBFeIu-kzfY4sibWCutLl-iwdg9Cxn94qzS_lc5s7gUn1klgGUCW8Pec3pzdPKboPxHffHWqKmvrA-K9e9-8uXf369N6Slyo3ebN50yTQkhjtu9d2itCAj6p3BctKtHF-IM_2kiK_kjjG181zD37CJLOXSmGMPFfEkzhT8xM5ZNVGDygr5LEvy6aTPMiEjuOQ-VUt7NDrBZjTOOFifUJ1aAYzQaTiMJLtf4M4Xp66NJtSw02FPPLEz7_rKypRCO7yUO0VTK-NM96alrxbU3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5L20TwjVN4Kg-WsEnjGXvp7AK45ZTP1HRIX_SSLF6MAH45BbPjDsYSjsLVlNtnPgU3zAHnprYJtfjsGfBdfWFxZVaE-df0H9ClOfSUw2tCLkfHvamR5xBcOgYv9rXSSwSLaU3e1Zwmnxti0ewKTAd1LZxwrPqh8vj2UXuOyCoORa2HvfwMl7J6FHZrEqG3fJX2hzwTeKDawFGgr-PZ_-f6F229s-KbCrhug3yrvvNyuJDMiW5OjjkTniICeL7kSvEz3wUV6o7p_ZN0lqPmsAr6CAHs75beWRKKztKVRe6mYFHW0jEQhcafVK_i_PHWGAfz89RKOdrab4N_h7DA0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkTiw9gGANDHHg-HQJq__aCJ-bKJTUrvWBXDLJ-1fNnzpiETHU7cF2AeQBYNUUiqj_IrJj9qUslvpS15A80D_PBOmCPHcawKlWeU_erbIgfTf1yGclrb1wD5enNwS_2SSjm1g7FZh7MO8PdWfHeyxcovQlT6FxdfgUOQOWc3fTPq6NYv-wOHRfeBaSg4fKahPwmzfNXDY5oDY6zhCyVKlf_DT_adcQTPDcpGZUojyQ3cllI9QwWhHITfV6Q42USpALXjAbDe77uKz1ReMsfMVQ85Q_7WwU1137W5GPFCZRhF9FKLB-H_LdUUqtwicr0c7C2vXJfT8SWWQsuD_BxYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnIulZlYteY_YVD2uUrRVRbO5YKzlLN_IjJrRx361uQh7FmWV8MGXXVdGZ8VtQ81PAARh3AqT09B556UhYgwH3eUHGsEqrziyPX_LCu3REDTDh7ewSvaJRC0sLc28GychdbwJt7RmUL7-CRyVQj7Ux1-p_ElO6BEW2p64D2fPzEdhRIqJObe3Z1rzZ0bRYq8MlYC0iV8WGI_rFLb_RftQJEJtxhWtLpDTj5k6TvPYD3q_Dc3j_5Lhifok9Xzo-RPBdiEkD1N8ICk-mEL2Jboix5obCGmmnoRz6St8Bxt6rQ4-28REI_1OB9BGeX4Xyx9YPaXSFKZWUhk-tP8PkyvaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=ARbYu3QW1QrO3uS728E9Z0J7l2AAJqL3CcZ5EXW2C-jx3hxPys6CdTA3RlOznae9l7pXSpzorkIcsE-NK1yFNl66PzeMy15sK2sOgLyQTyaI9SnC4DmNuUoSoCylJE56IS5NHQNmc6nm4ZIYG4LPcQqwbtEyEBXonkY0yh7M5GJjhmmfsOj_OBqM9Dw-J1bVMf1BFETe-HD61GUkMOiXQ0z34repmpKJShMtJjzCn1saCTGXPYTsmiU2uXxsAnoN3-GCsAv0UChVwZRuHH9-D_EcadigpybY78KfKLCsbgHbycbZNjprqa6k5ZBovUxvYuR9cvFSobSd6-rrjV_87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=ARbYu3QW1QrO3uS728E9Z0J7l2AAJqL3CcZ5EXW2C-jx3hxPys6CdTA3RlOznae9l7pXSpzorkIcsE-NK1yFNl66PzeMy15sK2sOgLyQTyaI9SnC4DmNuUoSoCylJE56IS5NHQNmc6nm4ZIYG4LPcQqwbtEyEBXonkY0yh7M5GJjhmmfsOj_OBqM9Dw-J1bVMf1BFETe-HD61GUkMOiXQ0z34repmpKJShMtJjzCn1saCTGXPYTsmiU2uXxsAnoN3-GCsAv0UChVwZRuHH9-D_EcadigpybY78KfKLCsbgHbycbZNjprqa6k5ZBovUxvYuR9cvFSobSd6-rrjV_87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL8eHWujS-B52OhZseqCr72UH96fUofB_Nm9PC2_bL1nUqN6Du8_ICHpUL0jPEfSLOc4qeIFshUF3wPqD4N4xvkOOsyX10DO9ZWFXQLZ_RUiFq2Da4xXzWH3sn3EeDdK9MHQtTe2ZlcTAoPg4jrRfBhY2cYKZgrlGOY7ZTaXsXoDVvYa_kkbaAwvxLKIhnXDniz7d9kQzEwVYCOiZkJXgqf-L6Uvo5HMA4qIxbdQiwcvzCbAYtNrEXF_IZSHkY31-z946rfQrzOBIoYgnjBSO1K_S4Md1hna2L02E0IdvwOXEP3DuyhPI4vEFQoctFNv7X7SvUcctZuxlPs-q4ZXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=AueRDBDJQFawVkjdsJTH6wu9rbXoBlDH_K5yUtZlf2sLKduCGCLWNm3xV5NXg-pvfCWGeqSPn20UfRsREtfY6jaX3gYpD8gRi3GLt6rB6QC1kdD4CZkkYd7-vK_Mh-APWDjxU1Xd5svrIFuf5LTFsha4qC5WuqqP7JxVI3c59TccIGCbTn6RyQEpANmOLbSej_TvVyGlk1K7G8PerCNTHWu_hlwpyKtDhJRrU9FE8Rvd2LrUHZddAI_nb3HAoEdbkuROG4PphpEp3J1NJchIVPUxJoxIj0KW0tKHXtnQsi5CwnbbSrBgH9-vsgvpPaOKe_4v8bY0Zkcf1WvvzvYevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=AueRDBDJQFawVkjdsJTH6wu9rbXoBlDH_K5yUtZlf2sLKduCGCLWNm3xV5NXg-pvfCWGeqSPn20UfRsREtfY6jaX3gYpD8gRi3GLt6rB6QC1kdD4CZkkYd7-vK_Mh-APWDjxU1Xd5svrIFuf5LTFsha4qC5WuqqP7JxVI3c59TccIGCbTn6RyQEpANmOLbSej_TvVyGlk1K7G8PerCNTHWu_hlwpyKtDhJRrU9FE8Rvd2LrUHZddAI_nb3HAoEdbkuROG4PphpEp3J1NJchIVPUxJoxIj0KW0tKHXtnQsi5CwnbbSrBgH9-vsgvpPaOKe_4v8bY0Zkcf1WvvzvYevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=tNn2bcrbIddy1TXzk9hPuw5GtbtlFgzLp3nSaQPGhe3dHDNQfNfZum60UQWV148PT2aDYM0p7cGAIhU9r8kqJUwT_tR1bY1aEv7NfSYmXKobhNxg6C4z8uUefpjtOAX2ROSs0YRciARX5UKMNpAJCjuzfw-wD7_SHQHzplbo9Kqh-cCUFqqdXUbHh_ZOsWgHeWoEUeyojHuOy6REACvicuv8RliNBoh9G7kFn7hMVjPdi2Nrp93nQW2tJjTwifySZUnus_nrvlPCabUI31tHNka2goFLnve-WFKA5ORwfU9nJRXQPdgUu9XG_vR0EZIVovZxNULFO3sI9dr3DyYznA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=tNn2bcrbIddy1TXzk9hPuw5GtbtlFgzLp3nSaQPGhe3dHDNQfNfZum60UQWV148PT2aDYM0p7cGAIhU9r8kqJUwT_tR1bY1aEv7NfSYmXKobhNxg6C4z8uUefpjtOAX2ROSs0YRciARX5UKMNpAJCjuzfw-wD7_SHQHzplbo9Kqh-cCUFqqdXUbHh_ZOsWgHeWoEUeyojHuOy6REACvicuv8RliNBoh9G7kFn7hMVjPdi2Nrp93nQW2tJjTwifySZUnus_nrvlPCabUI31tHNka2goFLnve-WFKA5ORwfU9nJRXQPdgUu9XG_vR0EZIVovZxNULFO3sI9dr3DyYznA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQMrvU7JxTRNQJ5BHnJ7hnQE9bJYKuWaVH7Fk_4Ij0YK6n13017Lx6AENjReGmVnTigocy0S33CXE5Aum4YDPMRytpgDqgu5g4ryKQ0KA785P9THE_EXU4Uu2mnkMTdwWzB3ietR0RB74Ss3trPVE2Ce49BxDo9hyB0beP1oZtU2ggLcnNn97HdQqjavwk1mvW2yGDNeWK_1LZsDEjWmTZlg4EBOpLMpKBrk8Sragvc81aRbnFdxWS-L8GkKD418pUcEepzTCFvwpY5Trxa8sYrugY2B3jh0G8fSvpWtkTzkAHtWuCKe1LUKSXoiEd3kuVFKV0Zi9tqh9XKfR5KVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqm8jHqnIKPPNFPOG-g3OTMwzim-nMivtmUXSO2CrBRu0ct3vm1WuSwSj0Sqh5ioRPJoq5QA99UnoYzX0tolPCZja78NtLEfuXD_PsE9yBzLCt-UwP7MU5nQp8jmU5p9TIgX0cVBNezImqgXb_8XB4rB9-4vfBT7B27WRFHseW8Ol4ytdtKotFelmy8Chzh1kPKaSdhzf8ckwGrtfkvOw_iua7mI6OmpaP_OcvcURxanvM92PWBMuxaBKY2f5SNhr3qwh4da6rw8gEtz3JhvpJruMlb0fXzI7HaO-oZchydstgT6v25XU8pv7XHC9FaVa5cRf7NkFXyesVTke-zoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQZbJVLjve3DSjejs-ckybLfjnTzrHUlenbZjVSSHgx5tWHQeI2O6Y6qh7kU0bbJsZOdA1odGB2qUmJYkbzZhwScaP6WZX0GGvFa6fJhSOlLTKh65vf9Jn4HBEYKy9wFpMhmDzzRmEaKMKdiienX8s-bNzSmLSdzb-yXsQuTrN2CwUmMB3fCv8PmFMLkvzdqR9KP_dKEIVgrzn9YTZmiG18AgV5-xC9BkeA5-u0A1V7lrioLm9y17P7G8UvLnEZtSzvv4r7gSPQUIfEI-tSyJAyMmuXAx6U2M6oMm7iYE5Q0ss6ARwiBZyQjqAfiQ4wdrwY-T0yjd4kgUBY8eRU7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuiZdRAK_dvJSx0ajyGD-ccHjYMmO287A3J8QyMQ1cd5v8dDo2SuoaA7AMfIffJhy4R8ohb2NheBjFtYnVnBdMp-iek4gf9HNVwT1nKpZ3p9QSSxKt3rET4GEtdE03-MB-kKFVFcku2K9ItOw09O9cwRpIOEHle1kklU8Qays5kY3fIyJHWWzS6qlJV2sqERBw2wWqkC3XsVRHxN32ud6hq4AeLYJ1HHS1hu4MPwMpzzGG-73u6g8IjZmYRap714BQxZeZEjQOZ4DJzY_bAy7jWgUTTN59xrH2PAQhljmM_OEtOa2z_tpZbdSkQdVYsL5Km2Dwg7IIbXNOp8cYKwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=uIZ7Bje_GhkEoExHjM0k9vLw5GzHalAyLvF05n3XapDxpgyNMJ96YAbs98byjOhW3uHlV7hVeok4IDfDMs3c_zs98wvmz-G6D51HVwuVed1g2pajjqXCyah4JrLUAihzn9-unwENIMEc0fUnURpZfCaoIjmcZ62zgas1W-5vcW9PnJL9DK3XD-XSm0nH6mHEbIdVyXyH8XB07Ou60MIInqOjtwG-O1NhBIUDP5WBlyTIxuRnK33AFcIEhEQms8RUJAqxYpRzgbs2DgEI9ZloIENWwf49RRv40vrzGnrZ-NPXXeAtDmb-563uk7xpVhEQPEdxyjYgRMCCPBcxrCdFIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=uIZ7Bje_GhkEoExHjM0k9vLw5GzHalAyLvF05n3XapDxpgyNMJ96YAbs98byjOhW3uHlV7hVeok4IDfDMs3c_zs98wvmz-G6D51HVwuVed1g2pajjqXCyah4JrLUAihzn9-unwENIMEc0fUnURpZfCaoIjmcZ62zgas1W-5vcW9PnJL9DK3XD-XSm0nH6mHEbIdVyXyH8XB07Ou60MIInqOjtwG-O1NhBIUDP5WBlyTIxuRnK33AFcIEhEQms8RUJAqxYpRzgbs2DgEI9ZloIENWwf49RRv40vrzGnrZ-NPXXeAtDmb-563uk7xpVhEQPEdxyjYgRMCCPBcxrCdFIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVlqbnwbjMycsbnNGaWrzf-QDR37dcQxKbsZNktktzUFzgzFpDiFHCq1mZi9VosPPZTjBBi6qrvSdxDoarvc0BOy_-HgMgaP9tH3eDIRUC58I878JpzbAgG-uEt9RAsA1Fh6LFzpHaoKiPZQHytfsEfFw8-ZHzPq-rYmyibc365ap_5_Af36Dfr2GZh_ibhigY6wd4DKLkh7YJf72FGk9wbGrlNQ8qG3NoiveOVMc7e2xGKeS-w8_a-n_pz81rvVT_YqrBjei_EvIW_5wQvwAtdIWjG42FaYT2vzbCyyCZXZfmypial9V6HARPbt3CygIBB95w4J6ak6tLTH10Jz2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ouac6fZX4YCK7dU3BtxTHfIbBPpAiM0peUlzp2b6yAMqpt3sKAoSLy7te3JD8auGy13Gc0xlPssuQ9bbtmqtSEQs-mWQOfQpSQKRtB3jEf_AykVbW5mUWvT_RfsltCv7NyK-NAKwDavbvMIt6mveSWFxN_6GWq1Lc99NQBVDs33Q4zCoQXUFVXZKm6dm8FkTkGD9Y3DmTV9ydjdNlLQXXu1_LcgX_nfoejWf9i1BIaaDRfbYwV8xfX1pdNVw_F21-_2gHrXSGvHG8I2RmsPQkbm9-K9BZ1uN_XC_mj40hMcvnYI4O7z7AysJTfZKFEz3hZVgmREZuR5XgRZbF0fCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=PfljOawW8qfr2egyv15fx-XZqfn1zMXJhWQqslMGF81wiQ3R0y8CUjFy_ghwBVovNdDq0PaffCnYh8iJprx8OdOf9YgbPddHxXge0NMAfgOMB6nNI1BEk3UCpesP6-kQrYLWEFqnpAUN83de_pA6_ohSGcEjLNZR2gDJs3h3jKtmtS7MqRKJREbpQNF_-L5OZPCGfhV5X9FVRfxNFQ4Ia-iX1VbRoS3oG5zBuuIi__dbgn49kze4tpEWfR7jzjxsAQEfJef2CHkBbTbsiEWpYH-5tqauoebAk4J67wx5rjR6HDfikTBgnxDe3Ih67XKw_ISmAcKTCfAs4Qgwk5yUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=PfljOawW8qfr2egyv15fx-XZqfn1zMXJhWQqslMGF81wiQ3R0y8CUjFy_ghwBVovNdDq0PaffCnYh8iJprx8OdOf9YgbPddHxXge0NMAfgOMB6nNI1BEk3UCpesP6-kQrYLWEFqnpAUN83de_pA6_ohSGcEjLNZR2gDJs3h3jKtmtS7MqRKJREbpQNF_-L5OZPCGfhV5X9FVRfxNFQ4Ia-iX1VbRoS3oG5zBuuIi__dbgn49kze4tpEWfR7jzjxsAQEfJef2CHkBbTbsiEWpYH-5tqauoebAk4J67wx5rjR6HDfikTBgnxDe3Ih67XKw_ISmAcKTCfAs4Qgwk5yUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP3jItg7QGPj9akDF8mU_e43cMPD6bMBqHva8jqWVI5EpInSJW37DRTEBhNy4_wVk8HodqKRR6FODKLz0hKTJ97BR0f90V5GDK59bPS-0VV16DdBtv3_O8Mip3PVmEk5T3F-ueJMVl5weYHU3y8pi4_XZqGKPlDR-WkwD9otbVZ_Ic4Dy2pgcv6on8g7KCS0Sy9Sf_feojLZPHYnr60AeODNf8_BJVT2lHZzBEeiQIFcn0i77pRP0_gE9vbgyxxB9akwqvnsSmYCaIx6d7m7eONpLlu4DUj__a15YZ9bcCKlzQ0OIQht8jwH_WjPIorW9o1-trXhBRRo6Ftfja7tMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YskBmee_JtgMIcQPpRtgqFf1PA2e5qU58ObO3iL3wEq82vfC18gYyLz4quq9shZ8tKUMJvwpuRcuaiTy87SQllXoWTTqn4prxbKZHmU4jjkUJPAq4rmYKa7c65jWraZTKCiyNsgJaHNwEjsdR4kCOgoS8tykw7yWT-zcTdhkT6n3Z4UQnZ0XyjGYp9UYku1flJyfu_ItIOcpoAa7WRz54rNtvMwy2TfqZh38uoa4UIls0xP14M61L5yOq5SFKC5Uog3fNgkR-CJttiK_rQnj-j5JDqWyGh0gqBj6WeABo3H5Dt4CpL7MHbmTfxFBVgMxjvD7bxhLLTN8r90F1NKZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUBMFPu7tqTxAVVa6fKeYpsa7y3kSUhOLA8J4rILjekiJExG74mjsirFma3y2NWq4Fzzb9Fnm-KkNi3uvuXyk-oAo9dgXbfiTLIZoN5vi7pt5zkNJSFwEtfKFpN7gHMaOfYvvMe7ord1lmO0KrdoLlzAtWIrEAR6yDr8nbBq6pWGjZy70zm--XlfSqe7wWVEhxaWHz1UWe_2JaRS8cM3J4HIbI4_Rq27wlQHQS05PqrCbKPgyly4Yt4gTaUMUn4bfDVITDvTHQxIIqS3LFIbYGEr88lgqN2ilUN7Br294zPQcuc5hRovhrcwarlno9qNhZgbNrRxwQxnb42Vp5pqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kem2X49F-rhWbtR_fj48Qn9sGRlSXO5gJeyHBvepam9TlIAFfg_-AqjT6ApADBV4V6GGrcOwGtHd1_DijRe0uS_oTQdJQA9fHl5OZeKUlWeEkoLbXWYBfRorMXZ56jbNV0HD_ywGeynduNsL2ui8kOC3wdj_i80kcoFOA7cgXRb3Pxfxw1cry2GHKHofG5Nl9a2JwtEo4DvbxnEelKfwae8u1ngMv7kg5Xki33OsuxUjBVEi7oUthTWHkT84xHFWzmeCuBByfivzoGMVp9Im0MZUwZ9q3vHxoOPFhe2Pg1kwcGbhj_fT1g7O6FLvdOX0_v_o9edh91GnUuIpK6sVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=Q1LyrERV0QjtkkFQddD0uxov-vUUzuyF7HJU5-t-C546RhX6adotFG1REY5c-O4uk2oGGxENF3ruPYhlIeRnUN1J2LIdyjP2jEONKh0lEzmJhmAQZ43RAF7LqeIik1SoeOl6HUNCO0O2V0OCv1cWV7sGPQT2HequX9S7OC7Tp2ZV--43f8cPiEjnsFvPwMNnrhS4-Rk5n_Sfmcn3dYuRNeZ-EzaX9r47sFBYTL26OgV-oKUj_eaekWSBE3maPCfzEKxElwcKVDK_USZrZcV-dcXVMx-3bucvneh_3GRPloqUU_Axlw54A2tbK8ge-6vFZAQqfXQ46fJG98aV2sslxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=Q1LyrERV0QjtkkFQddD0uxov-vUUzuyF7HJU5-t-C546RhX6adotFG1REY5c-O4uk2oGGxENF3ruPYhlIeRnUN1J2LIdyjP2jEONKh0lEzmJhmAQZ43RAF7LqeIik1SoeOl6HUNCO0O2V0OCv1cWV7sGPQT2HequX9S7OC7Tp2ZV--43f8cPiEjnsFvPwMNnrhS4-Rk5n_Sfmcn3dYuRNeZ-EzaX9r47sFBYTL26OgV-oKUj_eaekWSBE3maPCfzEKxElwcKVDK_USZrZcV-dcXVMx-3bucvneh_3GRPloqUU_Axlw54A2tbK8ge-6vFZAQqfXQ46fJG98aV2sslxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=cGFEvrb-ZpYHGhCP5-P6_ShW9CEt6nhs4ujn428qw51oWPNFMYuEOyt1O_bloRCK35g8xkgSD85_S9To8pHrQJt7byKBJsTJ0fndE3xWAQVQ5dE8qPfbh8gHbiX2cpp1PhpVboIAox_5z5TgeLggRgjyXwY4F838MwC5DAdOmJutVw9N_8E9WJw3bXRvXEMj6tHT2ezIXHtQfu4U7lv86GXb_XpEgbW-WnyMzq6_EAxnQ9YV06j3134a2EC56O27OVHDOfQoxVMxRybO1r6nFQIx3R6KTQEtfBlG4-N7J6qU2rtNTYMgPHKaCiwr-LgaIgJce3QSmLM7jkwS4Q9CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=cGFEvrb-ZpYHGhCP5-P6_ShW9CEt6nhs4ujn428qw51oWPNFMYuEOyt1O_bloRCK35g8xkgSD85_S9To8pHrQJt7byKBJsTJ0fndE3xWAQVQ5dE8qPfbh8gHbiX2cpp1PhpVboIAox_5z5TgeLggRgjyXwY4F838MwC5DAdOmJutVw9N_8E9WJw3bXRvXEMj6tHT2ezIXHtQfu4U7lv86GXb_XpEgbW-WnyMzq6_EAxnQ9YV06j3134a2EC56O27OVHDOfQoxVMxRybO1r6nFQIx3R6KTQEtfBlG4-N7J6qU2rtNTYMgPHKaCiwr-LgaIgJce3QSmLM7jkwS4Q9CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn5DxihmLlAnMAzYKU-nbWQJ_DYAcihvkwqyiWdfe-Zg5gQ1eCRWc2ekSwasKw-Tl6rT09249eRDTLLPwsc5p9zjuEAXfj3LC9Glwyek5zM6aL4AHiV2UGwrROLd6ZIBeJZf0UPZNH1_z_omqYDhGoZ6mGi3TpVD3k3qWEJvHrej9W3FWQKdcRGI9yQ9IoBGWTsqG6MCwes6gDDd-8NRl4c3paKtPLQADL0TYxek2TevMOUB71f-TnYMzpbfFdjhTrG_1tYYDwL7_cEHnQD0VpcRoq5qichD7mIJpVxc9J3Gs0A445XS6bNRUIzcqVDGLMywWPgU2PND07Uuy9dYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r10
@betinjabet</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULEYuzgvorkIrvefLpKGG2_V1zqGDl9NAbBHlDpwl80XKcHrQjGbJCNZu-sqZ3KdhyIoI43ce0wui2dp52xSpCEAvzW95H4McrJln9kivDO4EIC4joEF9Qo20Z-q9D2x8mRNViYee_bb8sixncluLEABDzNiHaoQuQZY-wJOksgdQUQ8w01U2Cb-Md-7VbzZbE1X5SSiuKZ3X6OBNi1K3Ag-bmD0biHWVW3heJs2XkluHV3CWaRj1z6RkFQuOVf8PaqOsPkElzBeqJ99zrNqa_BYWt1M85arbVnx3OECP4lWPmWh9XSjWHdlW53z5zTUSyZcNGZrYeDF-pml8ekebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=pdk37d9HQDV77cX8bDM1_v27NM9_Zwh0hNh-xNCjIlwSbjrPWx2poGRnn0fz4KQMEvVuiRgxRTI9z_24LmQrb4KREwSPQEMNgIors5Uw_zPKhHbwJR7Bje38K30KvQXL_RVpTipnR1TPAibD-fgC0_b9rqk-5LLI1rvp6ag3_khBJ2xw7aQtVk0-9OdTWIrNSo1Sko8J52COdibHADwULnneVJGjo5ru6URvsy3BxW38tAsPsN0PutG_bYPFw7KlhxpoRRp77Y6qYv0NN4gUJhHir_Yp8CqWDyQZ_5fC2ZHtLKBzNpjEmWhUgu_f7enY6OdKWOTUb1NxSN_thVB2Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=pdk37d9HQDV77cX8bDM1_v27NM9_Zwh0hNh-xNCjIlwSbjrPWx2poGRnn0fz4KQMEvVuiRgxRTI9z_24LmQrb4KREwSPQEMNgIors5Uw_zPKhHbwJR7Bje38K30KvQXL_RVpTipnR1TPAibD-fgC0_b9rqk-5LLI1rvp6ag3_khBJ2xw7aQtVk0-9OdTWIrNSo1Sko8J52COdibHADwULnneVJGjo5ru6URvsy3BxW38tAsPsN0PutG_bYPFw7KlhxpoRRp77Y6qYv0NN4gUJhHir_Yp8CqWDyQZ_5fC2ZHtLKBzNpjEmWhUgu_f7enY6OdKWOTUb1NxSN_thVB2Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=G-4tTUpcWM-uk-QR_DYynfkrr4GbY57DSAKaZE_YhOtYs76asEU_HMlrJdYJdmODHLL3IVv4xvot9RGd2nWktZWqJBdLIG3XHmz3y1uOTov1I_5HWvDSmU5VH6UiuTPXiLCFmmRhM69WByhSPF1mPH12rXv1sl_8lTXdTl2X4EzMfKDKs24Mr4MapfUdTohgYWxxfkJqP3vn0eGttBua_-9IAx5G44b4220us77yE8owppOLFMtCfqFwARRGXYd19ST54SzkiObSlS-eQg3XHMqC5r11ED0z5twOs1BeVk6IlK0M-tVy4GjLrwypqgZKLTsmtzZQTm1XW49UTJLgaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=G-4tTUpcWM-uk-QR_DYynfkrr4GbY57DSAKaZE_YhOtYs76asEU_HMlrJdYJdmODHLL3IVv4xvot9RGd2nWktZWqJBdLIG3XHmz3y1uOTov1I_5HWvDSmU5VH6UiuTPXiLCFmmRhM69WByhSPF1mPH12rXv1sl_8lTXdTl2X4EzMfKDKs24Mr4MapfUdTohgYWxxfkJqP3vn0eGttBua_-9IAx5G44b4220us77yE8owppOLFMtCfqFwARRGXYd19ST54SzkiObSlS-eQg3XHMqC5r11ED0z5twOs1BeVk6IlK0M-tVy4GjLrwypqgZKLTsmtzZQTm1XW49UTJLgaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEQ9e0NvD5iWsczU1UsCiE2xtiXlnw1XpbXorK0EP7l9HXuXjqBu9PDhgB1dWjIT9hWBYOOHcHUtxdrHDRZChpcZlJNGqKGz_qf4PMMJcDU-bpqRceFJDNwXe5LugHXoid8glQQKVZfk-rZr0ON-1iMV7FwpudX1UvBFWypclnTkkOxldCNepLsD9PDSksQ1pUwUc_OhKNjwfF4DbR35uMsL0sL2zt88K6htXmgpfrxBlI-JVOs1fnIIGEBgvMaEWK2bCPWTP3acorKDBaVOGoHuo_qfnd23hbvRawfdePVGsVyri1qT23GrSdkW2uscWrIgFbOUNEvu5_WEG8sRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg1nCao_c0kj2bhqU1Mv_r6eX3DBi5hBZ8csN5FD_oBpwQo72evUI4Fb4Io5es8tJ6crzdvy94BzwnVR_fPxxyTgR8qZMaG856ssJACDnYxBU8FLJJGMQ4olXa8v5Bbj_h3OCeSvDjwvvhp3E4_cTfoCwZnzCWMGpn_OgagJNxGoQGRssbj1wr_j6XSyJ5C7fbwn0Xn0YTGB3QuAo0w4sKEpwjZhZ7cnmuuyZ0Ln6_gJWSx7M35XuLkeAVgWYOltswzrx-m3s1ANiDwFTrgwqyaUkfWKxEEIW4OtiBl6eIn3L8RAA077zxE4-N2eJexaZyvGwpbIz3deZnCYpMvWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM7qazc_Qz_koDQdLFTstrxbfb3N3xkGqVaJcifaLQiWMHtaCzAtcpXRKT0OC7DEG0Ia7jH6J3cPxQmTSEAlGqTg9tTn_i-5F7o4VbuI6BtXTjENNcpZHhibCDpvYTyK2tA7w429s7aNq0C6Jvp-k4nmBv3uBb5C-3PaPYRXcyOKFtlY3WR0rxr3pXMx5cORyqU9yCaKjqz6U4XGY1wlSiE6EJI1q4JLxW5ajRvgFuTljgSLb4z9et8W6irjAtVIiSOdUv8D4Un0hCGbN68Z1SnXj6X8aWk6y5bK2l-FuKpkp2JCl37YhX92QgsnVYTxJuXiZi8C4zzVeUc1rDVHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-f_dBei3knZHuCP4QnXrCoA6KTLIzJ6CASCN2CZ_VW66duEL5fLu7g_bWhGEpthqMn05Vd4FX_AZrmheEi41GBbeAzzftjDopwQeQGjnjpYN2XDjzsvLDQzmnUBJ9ryZfrH_3LWPODUV62mY6SZ1RoikCHw0-DBRK_bmSQoXOXdn6oOVzr7kIJ9HQKuslQh_jtDbIfYInLFAA7sdbizfvfxLsEyf0-TBgMDQFdlH8G1okfa5PUi8TNCTji_oCsId10R7CHFj7dfLuUIcKXHRlFG-ukEc10zy7rL5fvekgeSHaGFsCdZTMMkjn-ic30W3syKIDopN8ssksSDif_iQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Md9SZ2O68iZb9Gs3KjuRdWO0IHhJcha03qL9x4fG1ehX6KISz9K0y-9UeZL2EYyz65oTuOPeChQNnhQNaTd2gLXYOoqYVSck5xcz-5L0PdDQyVpJa9SgSMvhuPJtHGsfr7GLmGuvx61b4wIxr0RUZ1-aMz7-Vc_E89AzULkn2Ws0rYKapaUd8HIUoJ1cayQKDEabfSUOd_LoNAn2fMzQ8zm2MiQi9LzeXDp4zJYvgfvTVXPlLcgUsv0nzjB0Hw0Z5aYC07OSN0O3C5Hco-EwIc_1Y596K86TLDFylAkx71EEs0EHm6McWIpkO9YKphEfJyreg5qeH3LEPAb0jKuXMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Md9SZ2O68iZb9Gs3KjuRdWO0IHhJcha03qL9x4fG1ehX6KISz9K0y-9UeZL2EYyz65oTuOPeChQNnhQNaTd2gLXYOoqYVSck5xcz-5L0PdDQyVpJa9SgSMvhuPJtHGsfr7GLmGuvx61b4wIxr0RUZ1-aMz7-Vc_E89AzULkn2Ws0rYKapaUd8HIUoJ1cayQKDEabfSUOd_LoNAn2fMzQ8zm2MiQi9LzeXDp4zJYvgfvTVXPlLcgUsv0nzjB0Hw0Z5aYC07OSN0O3C5Hco-EwIc_1Y596K86TLDFylAkx71EEs0EHm6McWIpkO9YKphEfJyreg5qeH3LEPAb0jKuXMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbC7CPGvFWWeL8eZVzDbtLOhqL0KBA6lTDxaibz0JK88nbtxFtQZJ1iCB8AnUaqUh9HX3niXZimkO-aFj2UKwVnBrhrl66bKsFfyCaMfuUT1JENjNq0A2p_H6_qDVcyIWhWpS3thRCy5c1hyO7WprJp5zTXL_g66LF444UadUgBpLRmyRJjiIMgP5CmjfWH5iz-9Vpc79FiqOPwEy472Adp1vuqz2XmzI0coZscwxFRPrbkgkalTMN0RIrhUwySi2D4ELzGP4Yhx4OHoZVjUXPQaWNrsHzmpJQjE9ooQvK_GyLbcAxX4QuT_Y5XrhX5rtQSisFz_MxQmB6IIozrtzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=XNeA9LL0N2CoU6ZNSvDd40AgrN8DLzAGXvzP-qSMX4aYvoZIEnQUwjqESlWI8OfzcmITG3OvKuCyFhVdK3B6qpbzCLrE5ZW5yf4-pdTh8aZat2SFZN20NWJhioLqbwymJvt1sEDke22ZE7WDkaKbvottnmhYDUlNkEszSeaxUEJ-WmiyE0eL9y0Bb96Qk-cO_Ye-M6kAAhZc-qSDg_Ieb33znWBLwmyyptdeNBkuBcTWrODWiZjVVJulmGRHF8Ts5VlFDYAf21yFAknZFIl3wJZ_NN5YfgStezFAnDXVs3hGrhz5z4dybXyl0oSODB1GYuIaaCO1ziwt78KF4TCFew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=XNeA9LL0N2CoU6ZNSvDd40AgrN8DLzAGXvzP-qSMX4aYvoZIEnQUwjqESlWI8OfzcmITG3OvKuCyFhVdK3B6qpbzCLrE5ZW5yf4-pdTh8aZat2SFZN20NWJhioLqbwymJvt1sEDke22ZE7WDkaKbvottnmhYDUlNkEszSeaxUEJ-WmiyE0eL9y0Bb96Qk-cO_Ye-M6kAAhZc-qSDg_Ieb33znWBLwmyyptdeNBkuBcTWrODWiZjVVJulmGRHF8Ts5VlFDYAf21yFAknZFIl3wJZ_NN5YfgStezFAnDXVs3hGrhz5z4dybXyl0oSODB1GYuIaaCO1ziwt78KF4TCFew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbZfx-hDUmn6aAvuwRED_aXVSXIKVWkjxomA0z10yIlLyM9I5Hi4Qc7Mw8gYIvjY8AoUxxvSibt-TkywBTJHCVX-7CDmhNHaKllDO73FAwSXKxId9-x_atEbaXZxVg40tkK01UGqWSwhmB2oxUTXHgM7SZil9o6HnWdxUX7OB0tA8Xi9ujmEE2A4kc72-T-Av7NZWirURPnxlLsMfkp8nV69YdpY5ckacIyldcYodkr-YwJzFYJexyPo3wDTE7IOaagLaR525dq8fD9LbC2k-TbGilTrFEtNQwk-coc5PT6vftqLge6RmfTZtzZed5J6sVHW7fEnu3Ood_cX1lE2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4eHsv6k6FB-gzgjW9cfuJeiiA3MVbLsUGE6ewPT40hh0pF5ZUtIb8qCdFKelBFNaTYTYUzDlQYO88qOlGY8QHAS31JJUxCJG6bByPXLShliaN7udLfN7KRtYo_TqBhBsStyWaySdE6EqyAvo0A9yvcIfp7XA-GyPFw-pEGc6gPqdyJaLynfst7bcVqTgZa7AnAHyJwPfc1HBnlSfm46m8x-uWGHVHgsGp22n7WW2BEj-zMeD5U8sryPTuRbbo6gRBcc5kA7s2kZTBTBZLukbCnvZHMHJ7mFkn4V9jw-dHXPPcQRFzR-5XPEaUYTtoH7Fc5qTvcQgijjPrNcrljtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ojd1HPo7aW3TESq2_SlH2dWA7CfPlpSYSiRKovN1h878WeIz_RGzrtlfGIKiehlGp_XSxuZUNgR3K3apNu6BvegWFW_LyVRN-k4e79LfgLmHEHUGuPakkYSngdiGOnD27vSOysZXEBdszan9q49i66eXLneOzVvDQQ6vQ1Pe5oiyynJeKO8myiAQkfU3euqx98idM9LGqMJ0NwdSFTf3FP60tPpUuNFmjYNfucK8k7oia65tUHLbAA67LhyWUlJ-akuooofN4dtifvLIFep9mt8A2Djm9ZCGd-jeo4988ocNPdUIn3DaFAFQk6-bx6cJ6z8IZYkn8cV4dVhjImcPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uarzITIuFLFJ1XW3nA317H9nLx60SXS2PuDf2FYHl9Cwcs3BtJjqO1_nWt6T-2yyzRHoPYfIJW97t-x7papQcOJKV1qzc2nMy0ekzB2Q8RoSokiWULv_v4jLL3rWERA61ed-mZtB5JoqtbjVR-9TFmvvAFq6InfyNYU9SfyJM0l0yVNwJUqEGSaVDutzfUJiB66Zib2861f4stC7i3NpQHhJQ7YhborycQNCsL_tua5a73Wgh13VHpTZRgSCgMyblyAC3rX8J-Zz3r9Q6wyyoLkxMITOmLsEmckFHWyod-uigwSZ9YCiky9B4yxZw3IrhXFjFCPrTNF3CxMJ4LcC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS5ea3_eayeHBLQI6fmlrhVZNNCg0Jg7NrXJFnHyskwBzls6qkw4RV3dXY2KL93bTFGTl5KWS_6vqN-gK8OLVirsFjMCGPSLNAIs8PB6Ofc9QvJQR-tgqHxBnkLwzrx4I-HRV4xxi-e5O4l5xqfpfAdtj3u8ZQfRSXpoMr0awMK_PfG78niFLQ2Vs5ZbspCaFrW2nQ2kYJeT61QCHiKRE6katLtLu6Kewyk6QURX3tZ-3remAymtWUWuYyR6NvO1uaemIm2ZzsWw6jQdifuA-_5T-qPXXbCY8UiaxDDRIbXNCZ1orC4DHzB98OEvSvQhN52-1NvBd4d0KmawfZGNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9QvL2MfhWzAwJO6q93VRF15rz0C5SMJ0MW1MlXRnvStn2xqobU3cc1PSKJ5h4CygfriK2GsgHHHRyAcxzLQ3gBGZZangDTWzXP7O-1EQOyZeiXaaheWbHOcuSXlpddplw3o23j-jRLhQF_-tZN1pSZT-uX4yI3jAtRh2Z0Enonsn-2czONUeKpWConaHILC-x1UIDLzJJ_KknOYp4SFsiZjKjIE3y-XoW4roNyvUG9JO0Ey8Hh1zF-_J5XCTTqQ0oRf9rwZ9vuxv0lx9xQL9V9M8wGOQrZEHBRENpMTlkDHe1Ie8z_4sSuLh-3-4BBbsZVF_b7YnPhvCz4pj1X1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlchNBpa72w-LGUoi447VNyJ8UFmZjrQ8_JCxuCDEjh9xc4g7DWlV6zvdIDpEFpPvBbA-SrGIBdfiaNdvc9hXVIa8f-XI5xVS2JzZ9__uixQgatHSZfldWTaax7Dic0YmltVFSmadTWd3LKiAMnOzgIVZjuDwpAyhbWtJT_fK1We3I3WLg4Fv8lt_EYKd7pup8445W7MfNiahNt-fpT5sfuTKbzcUSW1FExNKN-EhyYbs_bfdhb5c4J2uDMqMhAdofnR7QSmEcCas6qhP2IxEsNtwxCdGavqvuJUbiQWlEqf2KRzXXRMhRduK0-DTq5ey2IczMsoQC6pFXCm1lJ-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygt3YpjWpKnMH28KN0aaEMMvB6KLpqqU0eA9FVsz31IOgEEGTnoUM1AsmY8d7pd3wgFXsF492Vw9U5PUfyikFJh0a2kA84S_FhBOMrX_UNI-uu08FqirHUC7kmN4u_5tjahWodjON-DyYLRzjfpTLGKeQv-dLWdbxeCqFkA5Hc_GSo1n-W0kp08SRKgZ9Zm0wxDqjbpnoEGnaeHOtOC9cRM6wBiBt_SnGJMEO1EGDSwWtiFRT7IBuByYkdT1qV_c5w1PQDloxl3sAWkKqmCamT_DGpbV2EwBKmiE9A2bYn51_wLNEvW8qZVZXo2PCyL-4M2DP017TTm2I7PWZfO9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5Bfr_uc9nJ8jAktlYX1g_c5hdUXjTgvo8i8m6uyW9cZ1N_KMgbhXk9KjkXpEvlh1LZ6LWHp3a2JKHzvk_vi-n4dgUKyRTZNe3SbttGRHTeq6HfHloXMd7hhAdxyffFrS-EVpUzQ9DRm_PuhLctn67EQo1aD8HaQU007UlwA0-mrTpfSfsjcRNpOi0nJH6PZC-Fz3gNGZqaSPXKw48qIQoDONu3wbo3mb8fU7witkuK_7t_IkV0lH3GWV3mhb587YAUtcJnQFBvN7xGUHYFiRqqA0Dug46iXZQt41mDu6HxmndYFgpSGGuaRJ6Yy15VVbGUUuEKAS47w1_MYxGYXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5_MzIaRxKgMAe7WvlpnAjs0gqGHGDK-WlakK7DzmYLgeaeUCvfXOQaLbGUj_nm-evWd3ynSoQ9HMv7kJv9CgJNDt_yEBLH_7puq5cq3pqhySRXClBKuJ_7APkmjOwY6puz1XkP0FbdILN7XOe0Iz84dl4TQdLzlZE0_S9TAYqnZqpNPypxNeAivGDWGRx8nN4T9pUdHZrFzvi_sDjNKZFP9NSPg480LNOjOQE4ASObFWHbLq-Y1h_52IShmRvH-bt6NW4Zxko-yv5JwieGScBXFrKQcAHHkufRsQxX_qaA7ES7lZWaVFtFfApOWyP3gujXAuN3hxGm0kBZP_dLhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxG14vmAmQYZz8xxo17UM5AXAXh3NkvxkkAYmfy8bN8HiIn5ym_KNswh1X2mumH6ycPVvHB3ZQlHmTYBWrpCJWj-D5gvTaDasgHO7IWQYUG0WEZUDKmfnn3TYKQ6_cZN1LBdXB4ArYAJd_AlPlsLOKqStR_By4EhGeizof_ZM2TmoSl163zEJJuckYNmYtrBVSCcdxXGosE7bQMXeLn3xKu_3dAadsfx7Mp2fcvj2LkuDEiJHBwpU8OCfCQAya_363jtx2wyZXaya-xTAcwqFIaSWyaTf2BcsIesvt-vTgYLXG0ggvIp-CJdwqXKPq7kDw84fFUlHc8xpyzcuwrT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t93xHXx5YPUESKDpePIKbOgJ-Ep-hixYu3Q9MrVxdua4V0o7wJRDo794GATSGvmM_gWGYT2pbREGeqf8QoP80vIaxmqYF9M7iJ-nkxjNE2r_9exWOCTAYBIk6ULJA0EjLGSnwNzaUvby6DD8NTk2DKoyIjXsWMXN9I7JCk4e632RZYS7cQA5zTXfaMoAEGaI-GQBMDAjQk7dpXZY70WsU5zmkzStrqkHLJpNcIQQAedY_y3jl8aVI0HFX3pbSK7cW0w8sB-muwew4Rgj1uSi2kc522u_pc7k29ttiPhRAM1TnHI7lAvtU7QyfUi3tvnPgW3U7h3GZkVoOnhrNVt6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijNGkn23ocFeCtAqSrfpulcTB7lpwpCN2QVtuybdrSJL8E75MinJjnPTIMfwp2JzEF8E8X6N01Ei3ukykIcUlzWlxyPnB35UYHEUhpFhOmwOLVXajAW9Q_ieNvcY3hGskUUjloxGXLOmjcsMMKwQvAlqqeeYkXNQ5trQ3XEoB4UBnFhgTXIf0Z3yqLk_IFNPBS12eqXZDuVwbzJqxcnsePYTTmT8NJS4BlzbMky29kCM9tANXfd4MoEbrAlxpZvObsayHkzMM6fRL0pq3M6Gpl-lhHxhAvTE98Kt_tGSKi3OiB-FJKBfkZucCcV3Ai5vm6liS2ul5BATE3S-FyOmlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akwTnRrNL2Iv-b6qPNH3blcwDR0EKkW-NfqEln2bCz7F2RV6FzShm82qN-hU2qobj5XUNhnc_rVJ-ZJ8bK__vXoqaNiGWY6ErmRhlyJ2DywWY45YgBb1lnBhblDFQlr1DG2XALkoaYmNzIEcSXJYDfkhdj2EoUoFLHIfPsFXTkRXa6dJitOG0NNEI34S8xSfPpeLYOnu_8WFvHudEZpghvsEsG_4lw076qRd4NluFPijBk9RnuK-iJR2vaPYUGixEyg2QZI53rjS81cjlx48lgoCvtl44xtri5Ca71SaO8-52VDA6kMIFKN8Cu83cY46GD3oV_jW6ReR4ixG5ePi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7r1KJ6Acpf0Utete4CvYN0nXhSjwX95M5ekAXz4HKWoroxB6PtiyghKONnYSNeA2ZIrv10dkGcRdj7plWaXdc_CoYLYl7dFmUK5SjSGON9kQUmSFnNcq9U-inm9s-_a9NkVjfkgJCjLcsQERQDjtacCE3yaNL4jYbp3OtuCi4GcpuAzIA8d1pOExYmS66qqT2Ymx7rwSLBzsP1t2GDSZriN-LYwZfHBimaQg8SWRDWQOt3OW0rXv5NoAYm2CkKwTnXyoEyTr2ShjICoe5LIVXLbaVOSjIZcBWlDzFU6PLV_9D-TBPsx29C84ngN0MLRjMBhGwaf159u6L1OmVJq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAXL8mEfD-s_3QvjVnoj3UojD7bn7QDBcAZN4aLJ952RAbeYgwlofpULe3cLXhKwNhfyPgG86MSJQ5HjF5lb8O5tevE3oEStuv7OzyiFj2XytokLD5btfDwjva3H-Vv-IqYEWe6wmnfhIVioMIJSm53TTyE939C8MUfVq8ispSSogf6yZbG1CMqJqEMzbihgV1X_jjUUyvA12ZVhfGLeXbEIH8Virck77YnjNa1moxWpgrgRng3Zl8gmXBtbrkSiD0LyLKhov_ELR2tbCCHRCYKIasrBiV8iDp7uVUffdFLAJU1cdxNCArNmvnlrvSWUKpcSs9ACW2VLatzvup7aJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScL0ktHteUdnWU7ehZkROPRl-u8ostk4pVVuiJx68Zl-b6cu_QnxHShtc_l7omgsunq2FDX6NMPUpTP_YjhtVqjoR8BFPbdZtxqXjJB1SYJwAt3Xie25iTj1PDP-HaxiHst2JDhqbySNSVafWW2id1O6sovobafgZDeED2rVR1rkquDwy0QBtgx3eZFRq5ogw0vZ1dd_S3rQnBhsURi8AuifD3ERvPQA4jlMZXXzTDnYGyo6X7MoD7cv4p5bnqkrHAE71n4mr3I4JGPCM7yU1PHNLNjk-WUIRrzXhp5bjo7Qt-eSbTXDOaEfmL-h2PIQhJUJgBL4k9H0q7xvUN3BZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3ld0P7ToEpgvJjp9JMHgyz_5mDgEbDR8dZqyRKiT3Vqm5CS6Rp2FcZvL9AcFToFQNlN9dkDfgx1doI5jSCbk_Sa1qq0r2p6SPv_GIPrVjcFlk85INDy4iF1dgrIPaII6NnmNU0X9AJC84wpeIOxvoN6z7gdngdvbcARK7OsWKNeFZ_ZZOtO3_M_jO7PwY298UkOQsl0BGCy9PG70zQX3KLPv2PFSQAb1o2Q1CFXAyHTOE3flS1qjBaJwjglKbkUV9TsODNC6VAVSv6WnBSC16fu8yAEZpyWp2dOlvkaAs_z4hxSSXo7B6zS41L-KadAAMhbO9eIyeAizSa1aOkF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=K4i3bRwv8ZvJxgFbQpfr8vgPJwc9COd6BPySmZykSm76uRrgpy8KKu_yzec7hYhse4W4dkvOCDJxLeDu49PlkWXInUdbAVwrvQ8FSjjgvMwRUrLx1W-o2_7pZGCyJeDio6zlWsqgviXFZQNZukdQML2R33R5vCGD7pLS8EArArWYvEYiedUniRNeuz0fjxEsg1d5hMDTN8IiG0FazkINyJwLFPYlXrxobeSdKSMwSi5h9ovCAf4jElR3DiQlccrbUEG0tw9-kKAp1JT84scvAYnGoQnDqAX4ATdwbG8RrtyD9ophPxCvecgBBae0VLLIXusE1WTzbhiQuRFBFcqcwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=K4i3bRwv8ZvJxgFbQpfr8vgPJwc9COd6BPySmZykSm76uRrgpy8KKu_yzec7hYhse4W4dkvOCDJxLeDu49PlkWXInUdbAVwrvQ8FSjjgvMwRUrLx1W-o2_7pZGCyJeDio6zlWsqgviXFZQNZukdQML2R33R5vCGD7pLS8EArArWYvEYiedUniRNeuz0fjxEsg1d5hMDTN8IiG0FazkINyJwLFPYlXrxobeSdKSMwSi5h9ovCAf4jElR3DiQlccrbUEG0tw9-kKAp1JT84scvAYnGoQnDqAX4ATdwbG8RrtyD9ophPxCvecgBBae0VLLIXusE1WTzbhiQuRFBFcqcwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIXwuPKqdloK29piAZfJJIzkJXU0zsI_UYJ_SLSZi3nmAKkY1JJpxH4KWKV2Iu4TkYtCUVBDMaFLnZGEvOmdXXx2cozG5xUzrqy7MsIr9Dq2GtBru4moo8tvr2i6crbRGoPecvnANM1nrVaz7Qdtgpk37kyyOrg1mk8sfo6gAiJ4Jvu3lgJ_KfxIc6c83OCz3739QQzEt4-L7lrsXFuHVpj7PGCMl6gTfCkazFc40qiI7qFomgCHu4F2itFNYj1Tp96_975wTcMBUZacbDlYeYK_s1MRFdkTA7XNRYhGaMa_f-sAQ4pbM7kCQXqlPbcsU3EtFiFSQ9tgAhDl-0tkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=eBYCDt7co-r1FnK9uGC4Rcw1ho2OHXYmiDx0NIo1IK7zl31XOdGiDBxwWntjco62sVNJ9G8-DmA28ke3faQhOUwoDtGqZo2-xbLQhQ6vC-mmzjNZZh8Rs7ma5GKU5DSEHlbV2uD5ru3SNxREI2t5-OcxX9sDKO1dYskSwNCVi9dveJFUDtNBAS4T_uaIhjg4V2_AVp53urAfBtU52oZd-rP8LxiuFoBe2MfnR9vHbV6VXwV3JqCndr7GgIsyAUKne3_gcbflb-2PBddGv_x8U0qHy4_Qd9n0lbjs0Vafc7GMZtqHkxRJUbGAQdvnNfFY8Qf27eCS_LHhSFl998-ZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=eBYCDt7co-r1FnK9uGC4Rcw1ho2OHXYmiDx0NIo1IK7zl31XOdGiDBxwWntjco62sVNJ9G8-DmA28ke3faQhOUwoDtGqZo2-xbLQhQ6vC-mmzjNZZh8Rs7ma5GKU5DSEHlbV2uD5ru3SNxREI2t5-OcxX9sDKO1dYskSwNCVi9dveJFUDtNBAS4T_uaIhjg4V2_AVp53urAfBtU52oZd-rP8LxiuFoBe2MfnR9vHbV6VXwV3JqCndr7GgIsyAUKne3_gcbflb-2PBddGv_x8U0qHy4_Qd9n0lbjs0Vafc7GMZtqHkxRJUbGAQdvnNfFY8Qf27eCS_LHhSFl998-ZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=ZJejssR6lFugtCubRMBDkem-9FkmglsBIMBPPVG7hXmYeOiPx8h_glIBUAsrsTTfojE2bfxVPmeS0KCgkuLMx-djGfr8VNGfcrIOOkekjDm_sTT3hNnqIVe75Enxt2c0r8sN_8QFVbEgo8KpcutJa0eBzIVl6ElkdLB2eezE00Kdq18VKtDy9V3ml439qiG6qORUV0_6kvlKMAlpqK9A0JhPrfDk6hHOcBdtdJgJ8sSAMMAZgIM5bdaNfS5AjiLcSDwhuMu9K_omjVm0oavPu2rhmUFS1L1CcPOjFUGFvACpygr7omsQEfaOc0exKIQ9d1Zz4reF97P1PMrGOBEbag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=ZJejssR6lFugtCubRMBDkem-9FkmglsBIMBPPVG7hXmYeOiPx8h_glIBUAsrsTTfojE2bfxVPmeS0KCgkuLMx-djGfr8VNGfcrIOOkekjDm_sTT3hNnqIVe75Enxt2c0r8sN_8QFVbEgo8KpcutJa0eBzIVl6ElkdLB2eezE00Kdq18VKtDy9V3ml439qiG6qORUV0_6kvlKMAlpqK9A0JhPrfDk6hHOcBdtdJgJ8sSAMMAZgIM5bdaNfS5AjiLcSDwhuMu9K_omjVm0oavPu2rhmUFS1L1CcPOjFUGFvACpygr7omsQEfaOc0exKIQ9d1Zz4reF97P1PMrGOBEbag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf0jUp_r5e19SzDa0D2_3Xn_nHQa83g-Czyj30rMC9cYNFoDJIcyENQuWfmMCp_AQCIc0fHaWP9WN-h8W7dp86Tl41McPd_PmR4cEu3WG0UCV5B4g3UPfwXY6nHjB2laegUrxz2xoSeFA8FXvo04CgFqwreUoHJ4riBKDD14L2AnISKjQMXcVMHeMP7GBrONuucJRC80mcxAwRagkOnzuZCiddCPNPLJ_ne0C6mWEb_jrqX5W3zXMhsNcwzmRo2nrHt2plkMwFMFBtYqBYmd6XR7OyaZ1SP-AsJOY3WTlCNibNg-YSzhpY80nJA4g1Hy6kgMKpr3mavHpRYaBZ-Maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGwm99_KeQeNlzTB9wEKkcEEkp2K4Rdx8MTydkiL1A3bofRVQaJIOFV1HQcPcSHGRDxNIAn2Cfso4LJ0urtajCFkFwFlEtQDBu4Gt8V-_gho07Jgp56m4ma0eEuM3tcHiFfE3eIUs4IwMng7L2AyjkaUPN6BxF1zD-w0TxcF6yFmJuFrvPEa0qluN0gxnog-IzJYf8VXqz8HUCIw-U5cUDQ-imeLjIet_CSuKuBigI6x_ICA3Pb4mcxaSkYGHSbKwWG4cSSsFdF7WwcEdbzePPiD4_FJFCqBM7rH9dyg3KRs60VdgiRRO6pKgGohccFcf3MZvsVjjcq959HMJJk7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjq98M7Yt-y9GEIqXTigFFHZ2byll8mQzW0VJ3CRLW0WpWiLR4GlNEVLLUvfJJ0U3TXEA0K8cBG3c0x3Ho4lAQI3eu7lf9hs9ElOTYCSBV_dCsuqePVySjUeXmjxbZMBaoKsDGIEz5N4g677mMgpu8abeNnA34WyeKy70my3xU0YemO3CCfT0V-yW-7NDf7UPE98dNw5gBricWaOHaSI7rx_esC45UrnCUNA13KOzqD1z92efjpPuAtrGuVFKUyg-j7UenPOnQSs__v-cLNgWd4V_2tVNjJciS-KqQN5KwbUqutDRmbm0X_bwaLDPQCOTd1kzb1ur5by_apimGCqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmi1H8MJ0u0c0_xZN3aBCXrAVqE1hBgWwET65Lw9ztp0AAMDQCJ2J2OQQGzeTf6VfAZdjQy9wfgeQ89iaXz-a1S6242WfY6itI-p46Nw34xa8553XMjBd3Q_Qp4-l4tWe9OWcbG19k-n-qgRU9UkKOPl3KYqfnRFnhs7qNytErp1vr3qSrG1UCsnChO6NOCHIkxNwRzWpfozmF8GNWNEhcbtCA9ZMJsk1GdGlGXD4hbkvWSAZKmmj3kYJeRsxmo7ecwBLBrgQjU4zdSXlPKjQPayeJdn9sPmvtcd-GreJxBwy-6CO7Zi7i-anYmv-jztiwCb6o2YTJSMevEV3zapbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqEkxbGYW7pVNmsSY2fkGL2oIX-o5RAi-YiyZ1PN9VKzdTWkhu_XFswZIHTaBXNKkjHAZKTuqtAYbZ7RHgEZuYCMR1gA7E9cNWC6NyH4lhz93LRXhHiyIVJ3x4Fv06dx1YP2NFmt1N818hJdUmQH8zhpRjD6YXXQyEB1jIxgemLvICkwv4PVe_6B-_Hdbu3blUIpWzC_L2SZhM1t17HrZ4iLd-40orqf3_-5tbb4glA6k2zVoZQ_alNSpnfIddLMuZSbsS3UdKypLsjuLAoqt5sShovJf91CgdrMTlmO_wAU1Kw9_HrjJdFDDPLBuCYLdML70LsLVlHdbsA9s6T40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=u3vNcg-9jOzH36dMOZbnoicBOeZjrPjNKJ_bW25IocqsDa_fj0H98EFq4eZNsoaLObLxn-dyg3pHrunos5_2pqNElK_KrUgUndDW_yj1j3JnTw7rXSbjjAoJvfk_cRXJu_mbm9Z29xp5flRs6Jtbd0E5WXfknA8Uv0sf-oQmNDFbMNzi3viffmiOeyudPgaX-7PBHDFrzjgH1ZYergZpyfC5Fo-XYRDyEc62ZlQL2yWMdu0Auzq0RC0OjEnPWz1w8iA_9jsuoJ2Cf3I18IofkKBD4yoPgMalhvjdcCqS_AD9ZpsS9QMQX_ZXs0jTLNQQ3zEEKsaAHoOo9XFZKn0qyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=u3vNcg-9jOzH36dMOZbnoicBOeZjrPjNKJ_bW25IocqsDa_fj0H98EFq4eZNsoaLObLxn-dyg3pHrunos5_2pqNElK_KrUgUndDW_yj1j3JnTw7rXSbjjAoJvfk_cRXJu_mbm9Z29xp5flRs6Jtbd0E5WXfknA8Uv0sf-oQmNDFbMNzi3viffmiOeyudPgaX-7PBHDFrzjgH1ZYergZpyfC5Fo-XYRDyEc62ZlQL2yWMdu0Auzq0RC0OjEnPWz1w8iA_9jsuoJ2Cf3I18IofkKBD4yoPgMalhvjdcCqS_AD9ZpsS9QMQX_ZXs0jTLNQQ3zEEKsaAHoOo9XFZKn0qyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
