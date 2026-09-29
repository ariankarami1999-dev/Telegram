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
<img src="https://cdn4.telesco.pe/file/SLyOXYz8PhF-QNk_TRYtiZG_BZ2nGkw8VONbh4nfjQMujAgVQEb1jL21805G-2nobqJTeP9dppXsgLFaUN6lW2CqFAnoXmKK2ncTleNYSZCh7Kr4MO4qihXoUuJqsBuAI-b_fphOyjiWEWaTUu15JpGNfEVfNmrJY1o0m-4-44HXIh7e-LRQdKdbZRQ-TQJrs5CWe6YGmVXnl8cXN12M_i1fEb5dJTuznwBUGs8AVYY71WRtLuCebgDNFmtRHikJp8tReDuq-meZRRoUSB28Jta1bFHmsV9TQQRX2qsqSNVivlxrDyuF21Yo1pogSBXnUcRtrRdXOYHFDU1wHkX1Tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.52K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-952">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVtvb0p6j9G2pbqv8zcVuY_U17_E-PI0qKWkUpO7xnVgN3B-1cfLGVAlFQdjiL-3bTjLr9k1V__vlSBlCl_OvpUcQPrMlyl_6DYFyG5Hl7_3M67x1QGBfFoEqKYXsTSPotvyXbjri1N4YZXovviyzxiN46NLFoLfCxyVlCatgHsOFb8YBvXZ9P00xRzmRkztSQ5WouJ6yTvXL9jvT482f3z90oPUucJ6mTClGUQvXijWGqx5PiyCzN5bKXy2SINahnCarIckUssx814P9N0DoyFjDCxbAq9jrls1C8_NrKSvFqdVOi467K0QR1EqeRQhxMNJmD5uU6z2KsdMlmwSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
GLM5.3 با رشد خیره کننده ای معرفی شد.   z.ai این مدل رو به zcode اضافه کرده و بنچمارک‌های جالبی هم به دست آورده با اینکه بر مبنای مدل قبلی کار شده و post-training شده    @danialtaherifar</div>
<div class="tg-footer">👁️ 476 · <a href="https://t.me/danialtaherifar/952" target="_blank">📅 17:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR7PjQl2_wM3rbgXxv-pLGlzQK4kns8o19_x8MkNNvrkxZ7jMP-6pSZzYol_aEaUknHEE8hAvgd6HXHsnoUk1Xk3valbbZoUPiJpglBrxtRrajWnvhz3fK1i5CORS2BE_OaSgZ-60kfNvdcwDPBD-XtkkEdiIixAQrcQ2yRqTDDWzJQ95sm4_73PFojfFTDVDMphyc1YselvGieKanfUPRKgeoxezyjjkjryK-B0h6L7Qh4YUeVFx9ZV8A0__gpgQtSnYn6F1J5_NEa6ozJq0a9aZYl8mKPSuzHLb_ZdEArN59P5OOfHdQttB9iZJ0nz7TLPxHpl7-R7DP6a-twePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
GLM5.3 با رشد خیره کننده ای معرفی شد.
z.ai
این مدل رو به zcode اضافه کرده و بنچمارک‌های جالبی هم به دست آورده با اینکه بر مبنای مدل قبلی کار شده و post-training شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 468 · <a href="https://t.me/danialtaherifar/951" target="_blank">📅 15:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ2Cfe_CJoPKQLrO-HcsoV_YvVAolnaOx27n-xpG-3Vy1OkcDzs_ZwFR1nvv74EQz7lpSBvYd_fPsD_xwvYZCK8ZU_yAxEv0nqqHoqcp0Fvd2YX4NYKE9uLSOBIMBfV_Tb-4wRwQrZle66EX0k4nePPnW6biDmy0Sl8pZwYDhmw2KzIM-yuEIEpbO16QBJJksCqbxTtBtXjo2DJNGHaFXZIWogLZ_Ukkt6OErRYzw4NVREhDqmEEmhKmNmaDX4yCEgZKV06_e18dEDPxVZMB9ycPXv4c0bt2q9NpB1_uUvxuWCNiULadupdbEZi1Ipano4rrxPlO5hMS9N0IYmdg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اضافه کردن پراپرتی های سوشال به سرچ کنسول اضافه شد به صورت سراسری
@danialtaherifar</div>
<div class="tg-footer">👁️ 650 · <a href="https://t.me/danialtaherifar/950" target="_blank">📅 23:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-948">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUwLMB-mQiadkNE6AtjqfRAK-CQLYeJg0MLplDhl-mBK6jhqEYY6ZBndaP1FNvSJ-PZo_gARA3Hyh9949zVC_20itXIZaB_XBiFunSDqxQAUbY-b_pu7jh87NiZOgJah4cRJWF-pybALXWGhMgWqWVeus0UqtGdG9PiglfZ27oBxDm7GKfjuOWq275vEY-nYg4Yp5hmImFKFI3KPoe5c9gf-c6SAj9hxsmUf0OoPRk_BscYTkRc6iaxg4Ily3S4czw3luUR1ga73rB5vtmYJiozDHUEBbgQP-QdNeIIRZkNmrZK0N1uPDD4Zp6y7sCzxJixe5litCdwc_La8tXfcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaIhwm7EZarXqoBV61QbtVeQl58Is5KFJl2pERMbUDrVdiDlZMIWAoQQMfno3AS9Xn-lXtGXIZpnGEcNfQHBnXiT5F1895Y11XouzDCSgRebIUcw9AYidsLpgdO11yD9ggZe3zedpdEo2E6FnaKF1luwfsVNFYIzLx-Cza0wSITMowgtXpL1365Y6P80jJ0ibOLjIL4n9KbXbinuXwuyUCOt5CJUvfC2s50hqyZP2e2apIEw_fS2FDqSgapqz-XyQnF2LXoYrKB2EXCoRDRcInegVE4A2NiwJQQ3YD_SK3O06OxWbwhTFfG3f0dR4-fCaAA0zhLj4JeGZF5Bj_xuAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😒
کلاد ایمیل میزنه به اون اکانتی که بن کرده که بیا fable5 استفاده کن.
دلخوش میشی که شاید ....
و بعد با تصویر دوم روبرو میشی :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 731 · <a href="https://t.me/danialtaherifar/948" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-947">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEfGkmc0SQg4GyTq5q2P_yO4jLtKM_QEnbCeVCR1iyOI1m6A0QORfBl9l6DNhAdmSUZpnrPUN1H3F7efM1tGNi-_SnmIJmYjizvPRuk2RNMgrIuZ9aAamxKQk4p6b63AdhzGB_F8O5VBeiARETRHC-m4JO7C_EH09LygQUW36zFgJfcsVPN0v_dXDK-wEFZeiqMJEL91JiaEiXTIUsGs6P8MIysmlvgnKh9OkN3ZKGhhLgFpwGWPJY0ZqEoA2tmBYtcOwFQ1G_9PCZjn_ZybQ05qxvsEu6Pz3rRR8F3lL2i3ArSwB1JF4RNYfQTPc0sbxC3OygdLXQ4J1kMPRTVx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌بابا هم اعلام کرد که مدل Qwen 3.8 با 2.4 تریلیون پارامتر و به صورت open weight به زودی منتشر میشه و در حد و اندازه های مدل های سطح بالا بعد از fable5 هست.
خواهیم دید
😁
#ai
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/947" target="_blank">📅 13:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-946">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این وسط با kimi3 هم آشنا بشید!    یک مدل هوش مصنوعی با 2.8 تریلیون پارامتر! و کانتکست ۱ میلیونی که عملکرد فوق العاده ای داشته و در سطحی نزدیک به Fable 5 , gpt5.6 ظاهر شده.   این اتفاق بسیار بزرگی هست برای مدل های چینی و ما تحریم شده‌ها از امکانات دنیای غرب.…</div>
<div class="tg-footer">👁️ 660 · <a href="https://t.me/danialtaherifar/946" target="_blank">📅 18:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-944">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBoCjRtyCSH0OshP4DN5DZOrtB-HKiEaGJN0D4CqTRVEbT7wkuOepm-uAOxeOu9EHsZ-hsW8mZ7S9rVik0EIl8UqeBFmg50Ou74-hwYY79uGcBeyupnq5MQK29x841xtK9HCa4ThBDmGZ6Q6fcTWTXedg114xwuYrClXQznMDPle2c1PULD-uV5i9Qz8f_n8dYFo7RyFxnm3NYnZirKzwS494_w4ZkyQSI6dkEtVvIVs3yFh5Lg5OAeQPM8v5ntlLWDx1z0meTVCipef_oO-gmmULBJJs3vfnOb0xK7ee0eH1vWm6CsF7QdEUFEXtRgsCM3J4_EErVWcMPXjEcJYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93f82da84.mp4?token=uHdOcgE0fUvU2R38thMK1p4rDxLLr2HtBgnEYvhXMHdKXb35wjyj4WUoa3p1RNBvSaflTk_LIbgzmxi_J9cgH3hki8l6orrpigUC0l-7ZPw1BGib7JsY4CZrk8067aKy0otKLb81nNYVqEFwZiFcnqJ__ovpBJsTWo2Sejk_ox0tB1OdkwA4tgwa4QPRZYiDMS3sXE_ETL2acFEQ8YFzvINJspdrVv5zy6IgcSobLWwbMnHdzSCxgJowa9jrIKJ3YaLWpiVL51qQBgUwemcjmvsspeEJadRNW_K_uYAwsK6AkABusQWrtYiGIc4QmWGGL6KAn8vopvuay6mMb8T4CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93f82da84.mp4?token=uHdOcgE0fUvU2R38thMK1p4rDxLLr2HtBgnEYvhXMHdKXb35wjyj4WUoa3p1RNBvSaflTk_LIbgzmxi_J9cgH3hki8l6orrpigUC0l-7ZPw1BGib7JsY4CZrk8067aKy0otKLb81nNYVqEFwZiFcnqJ__ovpBJsTWo2Sejk_ox0tB1OdkwA4tgwa4QPRZYiDMS3sXE_ETL2acFEQ8YFzvINJspdrVv5zy6IgcSobLWwbMnHdzSCxgJowa9jrIKJ3YaLWpiVL51qQBgUwemcjmvsspeEJadRNW_K_uYAwsK6AkABusQWrtYiGIc4QmWGGL6KAn8vopvuay6mMb8T4CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط با kimi3 هم آشنا بشید!
یک مدل هوش مصنوعی با 2.8 تریلیون پارامتر! و کانتکست ۱ میلیونی که عملکرد فوق العاده ای داشته و در سطحی نزدیک به Fable 5 , gpt5.6 ظاهر شده.
این اتفاق بسیار بزرگی هست برای مدل های چینی و ما تحریم شده‌ها از امکانات دنیای غرب.
من تجربه کار با GLM 5.2 رو بعد از بسته شدن اکانت آنتروپیک داشتم که اونم سطح بسیار خوبی داشت، اما قابل اتکا نبود برای تصمیم گیری ها، و الان امیدوارم فرصتش بشه که kimi 3 هم تجربه کنم (اگر خاورمیانه بذاره).
@danialtaherifar</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/944" target="_blank">📅 01:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-943">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avo7zIb98uF8iwtz92Bf0y857dL5FX-f1L2PuPvvWN7aKXS6MbaVqcRngnVZMmctwh17YEPs4XFajsmth2hZTGrCBP99kc5GueCR1fGx2UdX8uTSWuyupdHbDP9cme6Jo2L9kDEKu8hZ3q1xKCo8khCeoRi6-hbZEHB04gQJaXqvcgu7N6LnYPuHkKM7UqZPF1rdXJz9KyQov6ZATMKQwitgzBY9Qg4JWjMUvg7-FWkMvDeZMB8BDUiirBr_Ww_8rRjBHce2CC2X7sva8zK9K-Z-mntXWHkAnak-aSsOOiAwNN8Wk4qqbf2F9LRfU6LNclqzI1CYtcULf7s5QNnBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ظهر امروز اوضاع نت اصلا خوب نیست و رو به بدتر رفتن هم رفته
کارای مهمتون رو انجام بدین، احتمال هر شرایطی هست مجددا
@danialtaherifar</div>
<div class="tg-footer">👁️ 572 · <a href="https://t.me/danialtaherifar/943" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-942">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">باز بریم بک آپ سایت هارو بگیریم :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 636 · <a href="https://t.me/danialtaherifar/942" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-941">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📚
۷ ایده از Phil Chen درباره آینده کسب‌وکار در عصر هوش مصنوعی
چند روز پیش رشته‌توییتی از Phil Chen، از اعضای سابق OpenAI، DeepMind و Scale AI، خواندم که به نظرم یکی از ارزشمندترین مطالبی بود که اخیراً درباره آینده کار و کسب‌وکار منتشر شده است.
خلاصه مهم‌ترین ایده‌های آن:
۱.
هر کاری که خروجی آن قابل ارزیابی باشد، دیر یا زود خودکار می‌شود.
بنابراین ارزش انسان به سمت قضاوت، خلاقیت، تصمیم‌گیری در ابهام و اعتمادسازی حرکت می‌کند.
۲.
کمیاب‌ترین منابع آینده پول نیستند.
زمان، اعتبار و روابط واقعی، دارایی‌هایی هستند که به‌سادگی قابل کپی شدن نیستند.
۳.
مهم‌ترین مهارت، انتخاب مسئله درست است.
وقتی هوش مصنوعی می‌تواند بسیاری از مسائل را حل کند، مزیت رقابتی در انتخاب مسئله‌ای است که ارزش حل شدن دارد.
۴.
به‌جای ساخت راه‌حل‌های موقت، سیستم‌های مقیاس‌پذیر بسازید.
هوش مصنوعی سرعت ساخت را بالا برده؛ بنابراین مزیت پایدار از سیستم‌ها به دست می‌آید، نه از ترفندها.
۵.
تمایز واقعی در «آخرین ۱۰ درصد» ساخته می‌شود.
AI پیش‌نویس خوبی تولید می‌کند، اما کیفیت نهایی، سلیقه، جزئیات و استاندارد اجرا همان چیزی است که برند شما را می‌سازد.
۶.
هم فرصت بسازید، هم از فرصت استفاده کنید.
برندسازی، شبکه‌سازی و قرار گرفتن در محیط مناسب، کیفیت فرصت‌ها را افزایش می‌دهد؛ اما اجرای درست است که آن فرصت را به نتیجه تبدیل می‌کند.
۷.
هوش مصنوعی فقط یک ابزار نیست؛ یک طرز فکر است.
هدف صرفاً سریع‌تر کار کردن نیست؛ بلکه ساختن سیستم‌هایی است که بدون وابستگی کامل به شما نیز بتوانند رشد کنند.
جمع‌بندی:
به‌نظر من مهم‌ترین پیام این نوشته این است:
مزیت رقابتی آینده از «کار بیشتر» به دست نمی‌آید؛ از «
اهرم بهتر
» به دست می‌آید.
هوش مصنوعی دیگر یک ابزار جانبی نیست؛ بخشی از معماری هر کسب‌وکار مدرن است.
📖
منبع: رشته‌توییت Phil Chen در X
https://x.com/philhchen/status/2072793818945167475
@danialtaherifar</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/941" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEyTKG9TM_wtJdsl9KrN6SLFr33AU2xlRPVuHXBGWw-s-H8h0SOlhKCBl5DPFXzA6ZX2Im7X5S74IVicxTcEmQ-QgpwshX6Pg1KYXw52277dt8FuSnFClrPti9xwVErt763Zqk17l9ZS2VA6wM-h5j79N2MBId43h_v7Rk11JmPVZqqxaD9tt6226nUhLcVoW6Ev518qjVC8bkLX_JwerVUlJyOo26SRLfuQHplt96NIbDqdarG1UUzXFKvisLTlOqYQFerUtd2J7BwZIjspEIEgWGsg830pxMFdi821qYcBweVYJq34b9ENwCL2RSd3KNU5sfpF994C2YsHLVvOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=gZv79O4vkkvyEot8NGDuqbZ-eAhuK-WO7wuaSVPkB_pr1WvLXlEkKg0QxOOePejhCRw2-vCGlK42HHmFnlUdi6CROYaNOCi34GoMj84H5tmudFyikSrM4mW74NEquQTo4xnuOcJW8U-z9-xqvzf34mQRMqZg3jyXWPuWMMvOXyFVzm1zucIZMMD-4H4dKQ2mb1oEgHYGcyIqCDY2w4VsmnlACqmZZMEZbm4I0vS1anbrg11ZtmIGu7Brdlb7q7czomWWGKmqo-XFjQCdkdobDVGe-sKYp34t-RBYYCnRrRGDPmcUyls-qHq20iJ7MDa5eOBFIN31ZTLPYpzyc27cCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=gZv79O4vkkvyEot8NGDuqbZ-eAhuK-WO7wuaSVPkB_pr1WvLXlEkKg0QxOOePejhCRw2-vCGlK42HHmFnlUdi6CROYaNOCi34GoMj84H5tmudFyikSrM4mW74NEquQTo4xnuOcJW8U-z9-xqvzf34mQRMqZg3jyXWPuWMMvOXyFVzm1zucIZMMD-4H4dKQ2mb1oEgHYGcyIqCDY2w4VsmnlACqmZZMEZbm4I0vS1anbrg11ZtmIGu7Brdlb7q7czomWWGKmqo-XFjQCdkdobDVGe-sKYp34t-RBYYCnRrRGDPmcUyls-qHq20iJ7MDa5eOBFIN31ZTLPYpzyc27cCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIka3KzHJ8OAh4BP5VxJHkbV4On2LsVdzILbDYHnBOmkcKIB0Ncd99ltbt3UJVO3fiNHuSiYE-QFtwRF0jzzCIS1uKI_4dsQk778kl6YJdrSAgOwyejRbhuUIDkhXa_cJQQuOCqSS_K5UjxiWRaOn_2_U-BGjjDgIxn-Ph1x3cM3w_CyFMkqyGKPml2YIfHGiBf8WemA3YEi8KLJr6LG8jcCPUSZIwMI6cdkg149I72Q4pCbJXydPHeRS7LGmzd6yJMiM1RAPUucOEQMrwummAjWPm3f7UF3z8UdNzlygXcwcFso87KlamFq31JLcGGK9D9vs6_vdQohi0p0uvZbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 845 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVV67suHHwpdpB3Y0TBsB8cA3rid0BrBjM_s-Wh3mwuSkd5GJL9sHWk0MJOZ_BHTXogoaXbZWrBn1HT4xEyBLr2zkKExWzE1yvKnZeHi0HljO6bCoQ3SmslTSKTgb9t07P_mjBN06sdz9tNA03BULpckW6-Vs11ZVdh4OZ71mq9ekCZDUnRJhgBVzsbnkUjCbdHZZ6pVDl7T9104UeLk7LWDCDQuSld1DhmUr0FRA52hNhLUVeHozx81ZvAIDM_nzLmMfgoXNJMgZPe1GfYcTn-SIQzPHtvkVTV85H6RlqJL7RwUJz1fnB7mOCa6OoFCoaUmGEvdbTNiXrAVahN1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfIHq2Gi37RWlA-H2GnIRN7xi79UXpJ-X50VpFesi60AfB5yEPWGE4JbpynY7-dmpZgTG1FZUtV9TiQAVAwnX6J8Xl9EdhFVobUJjG6UcjYZ6tk6Ifdf1OxDni-fyAns3iXcnDx4QVMc8-yTQjfnXf4QiFm63qfggiesz6pO62OkBsmLb0mZn_nUP3_oVPujUL2XKS1hZVS2HGVj9NCV1pOdiaLA6rSq-6MuLVZxxUkm_Thd68G6eBEhQo575kpyBH8jiQ3PJRX01tyyXLOWO11ptg1OIU082ol7bnMGj6fmDFrrETzfAElHFcz5kBxSkkaqTYljzK7USKX1XwI13A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spFaey8U0yyziPubZb0LeFO6LDrClg8A2p-m6t6pFhov45Mh3lHqTgb0_q-_taF0Pt6tUfTux5pO0yqX1x5_QgaYNyky4qkmsq2V86Q01EDzu1F_7laNbiV2XlzXe0AvZfi_P_fztHeTXKBQZYSH6_vSMaYtKbqgGKANZ8-0zUWLc0BvbqeT2b5gmGHVjcxpQC58KrkZf9dLQjWppy-e7bVMGHCn5qKiG8IvqG5KAawap_DNDzUDo7LHSYgPOOzFARAFQ-2fkFHC0FMcZ8M1956yFT_tHRNY47WmCveWWQf1wEbFxvsM2fYzJQ4LH_1THywRrDEjv-PKgbIyo3q0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhvd8kOvK5qudSKb1LoBUEt4eWRXjlCokxDICBYTdp3EQ-XwjmF8QUWX11JvFeYq0z6yYZY2Rt71sp-td242s7fZTywLpBSuRYTwLW7yx444kQ4v_GV68Wz66cqe6y90He662kUet2N2eOcqiCGVKmV2FXRg4Rwtw7uJWPfIYFtWuEqpD2tySfvq-5a4Mo36fhgR4yd7224JYFs7VCTXcMTLHRYzjbWLBAGrjqo5J59fULvk_jbuxqwz39jW8_Ylpl8HxHcn8-VFE8rUv8EgirGQr-bvEOPxP2rxz6b4AlP-cwD-48rnou_2GKGOXBzXwzsQ07fNT1ZiKErqQwMjyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gub6VuV04JcDs6Hefpf-0gOQ-gyqxvizZxJZGHAKG35afB7qxCtSyixlAI1d9lClGQS_cxeT-K76wZBgzLRoPAUgAvD2l_bfHnc4CS1skqNdOyF0QJDcw25O2CN6dGl2kxMWCwNm29uxDBsnOn2e5sBlSa86Xwt_zFe2iKOasftD4vqWTz8XVXOWlMFLajdv_Qm0Jtrsr08VUX-2A7uJCbUMDmGi95wJcLklPfq3_GzTGJmllJXtL9if_NcuVlnvGOucMaRQDd4LSHSeezadEs4FxoE_AyYoVbqY_Mr_9LEa187N0SEVbL0TiKD_ZURxczhXd48dBcjXv22GMDlFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx4lt3ALU0afjFUzZgJ6oR7ZxA3UkyyaEaesE0Bc1f_phOCOBjj9p9EQsccR2JcLrpY-XQ_zEdTucP5GOvPfAVswKIsDns6KHT9OiEnRvq62AJBo4zrBxZwhrRA25mRICv5Uzhi9rQw_rZ3jxtdbCG6mmR7m5rAzoocto2jipAPbwPFC1dFcJabXv-R0RLMZhFl5_D8mgcs7YM2FuY7s9622J9WaV959jUIx1gBB4YhepXBz3WR62yKXvAlf_YHvEoPpZN-OhgAoP6R9vr_powXdkwpV2H2lL47ObqSjY1CBACxllgzsPG6hEWmZfJYQsAPHOX2iDnw1xzoh9YRYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQ90Y0eRR4V9034M8IdqW7KalhsjCS9cfG2f4LngQHHroVqjJYR6Ij-oNtQlXR0T7Pmf2dXuR7R8xstRgql9ugovtLJ1hrIYHDafQkU79cvi_ltLObjqSANR6KGzxnVsPq8UL_SacHbtydEscdLNU4fHuhdfzxwh_S40Qj6c7jzx6TsNei87YSv1MjN1xGhKBKd8BQdV4anw5DC7b6gjpjvLSg4cOnowIZ8Ttv8SbMQBtPR5NZ4FOHAwWFu_7YdqL74PloKiDcWgyibWeBdDjROxFTBBdHM00aqorsmqZHF4oE7PVeoZU3U9z1PTDuMdrQiAQmy2Wr5WCoSXjoUc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zl0XpiXfVlDOHw9yxtRvpcwxm_U37SnRid9a4bOAh2dGzHyiM1nbvGVlDmDLepD1p-9XLvvozh3vx--pOEDneZghp_xoklzz2HhVaIQbSyB0niYz515fOH_KeHa_Ph7Aj8rMUACbqmS1rybVkGf0wJNqjonLGFQBYxk849K33nGDvQqrgvnOTnG-5Ge-viAn1RaLrVxLd38llS2F5HCPs2nlfivPuJIERKjshKESDwV4eSOaAwEwmRryQiaShrduXqZzO797fmhPqsGgTTaTpiVfcr7Hdum5Wyi7mi8XxJf89-ClmhzukAUvBpfi5FdeOOV58yTSKshbJdDug6FIOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgfU_H7tU_CDJGSeeFE1N7TDaAELu8oYUQ-nBF7kfBnk28W29alizgi0RpAR3o6c3l4tJ4537C_rqwEpHMsjC1uk_Z7pMVa6iAc6XC0o1VtjG2w25AtkIBznrsQVk5gjZk2DscvYezUEHA0n2j7b3ecARu29VEa3Wjr3aNhRWuf56dcx4ZraBFcjNxWi79iSLwmG_DZBZKQdX62DgKXZi2TKJBeyKe9lOnH7pVxcYQJJ9oMfwVJdv6ODV4skEnyqVR0Ob-uEOBrPW8DtsqL0HXdg02P0dQ2AkPu1QpBI6fIW_SEd3fN38tC0pkbyUrSF5h8ewwofC1vhiZ4TLlJuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 710 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmhCMnyrksbO_RCdAmVT4gOfVwfRdJf5WD1DwNDAbb_OfRExU_PCl2oJ29MB5bWo0pYPRbpeA9847yyH3Cm_zm-YGj4LvvaO1PTfvEBf0XT1m3Xum4vKZ_DMhTHzneu_geYe488SwuDTBdnl9CGyCB2u_-iPtykAV4LtMP2i0L34y8bSnRPREwkayW3A9wN1SlN-mj7OfCFLFVhcIvfB6EdzrH7AxC_TRVTiebcb9oSdl_siZjQzeasc8UREejKpMtQONFJjhWcRfuuDiXiY4bf196SQ7vH05TktHot5nnuFCSZ7_2OxpQDR3_9kwc5Ga7JrhTPgvFJPU2eA4XQApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOaBC2eoHIR-HZUx2QTRxh3ej3Czg_HNv2SmvjWLXSRXNsG4yo5n6K-TsrtOnuPGmrOftdEaGnKpG4lS3M5gLbpSiJhRPUi-gh2VMNy-yx2zodiBd2f4uHqnHbv2uLPssWg3KTFRBFFz1k6_FETPFXIMSgml7KGO1arN7vh-VgsCBQB-CmRjzqdh2kKCmj399Z4H6aJZkZTpSWDkwi5cvG2XYp-W2XzfWZwXbD8osnILIkcYgPk5ehkAuKg21x-I2PzIQDEBR4anm-rYsIdl5T94reGUxEet4tEpneqckKlIXkU48gQqie23dOW6UVy0KS9Nf9Q1YD9NX6ZnGMAapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-4r7AWY6daWKJhMhbGHcpyqOaJDkGXM9zxHqLXELpFEfYBrsOP7vbVtJCO2Lps7Vp2fjoYva6tCRxaRn23D2HtY1XJjQHjEZC-o7D1fRRybxonJErToWoBDTUUY2up-oNqz7JLFGuDWXQafUH3Zn8szxboSluumxJoAFTVvflfRoCwzTlQLBJlybDMIM_GLNtky2xX3PVaAkS5Wl2-JgPaygC4DMYnHG6tKu4BUjam-ned6JUQfTM9VGsPBvESfbuz8PsTu9zI9Ci2DyoW46pFTrGg1pahilEVcl40RffVij7cjwd5Nk87vZpM5wFzz6g9uBYImB-fuF9ksriqNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_tBQqbc1vcK0FsusRPwEFTEPCkBwFgcK6GvPGvC0UzV1S3iNDnrxx6EfvQ-c9HuIUaWKfbm4COuRHHMFS4UP1Gw1VkhjkR0q_6Nh6Yho9_XLuLIrkP04m1EzdE7cIj5_A1gkGv84BrosWQ8NqyaxfNgx2N9AG-OrTVSqlDhCLfbQW9dc13NPLgE7QrX3qV2Em0or33XGpchvtdNphLX-A52vsbHyC5Nb8d9iTCne8Qky4EQnl9eAFMwXbGPQKQ8ZLttjrXOOfx-_6uXybelc573xMdZnMUnfHMNxhqAozT2BPtJTYLWiUXjOYKeOjW9lr9F0fGiMWYTiBnfFytsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnaZ5O6RWSOrNQTMeIiXmCS3Gxe5lLPB0K_8-vX-6S-Dra88kLkOBn41ry-Ony4V3CkIUA2IdFNBV9UG40ZWl2IkINQ3eYcYG8geaWKgHxCyeYkec7gWyG5SGnrTLiIXI7-aRHxHObUurXQ4TcNp5brgNgHLpNmSy9JMsBmu_5Ng7TD-q157GrZBmknf0WyuyQMfO37zU4ygotoMP3CDHM6HeLWnGNntYWzYm2mtB2_D7CdZ5vvxGDkan1xjSGxz23czT8Ic4SQdmvM6bHZoNp030gf-uJz4xXZOS6uBtpI5vFnKPmtiQWf3kbh9uEkM1gu38WhOAdCUTX-3EA3-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbtMu2D4L97Ai4Pm7vOetDfB4JkKWJTuYiRv9N6Ks27aVksJP9iW5XSgAWhfooADywj4u2QUzgq8nMABkKC5VOyNWPOhPRS9fClJer04atnLOdftTDIrgQy_epK_xBLaJK_U49Xn50kcQj08qmXBXJOCTdS0hcS3i2YmbHBWin8wdIgMfIy0uJe3ZdBGB9PODR4WGhiEJXnAkb1FN0c40alXVWiSrPvXzjNVttWFJLyW9PfNY1X8ZuvC6v5sc0bItRCVZnj-RWjxVn7vf5iXkgV5nTQoB7MJaIu9kImECWJCU1PiAcxoZVqoD8VCoyEs-Rx3OWatzY5_wrZVUBmA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnzUbk09EG0xdMmtL1caXKyq8jF1_JxF-lyMxiiBVGMAk6I4M1ypZHSgbXmGiOGhWVtCfvXa4LPGP2lcMTSy5fA4pWaRopevo7gm4VZcOHfCaA_oXSTa0laV8UPuf-9X0uS7DLtWx8fZkDIBaAwTOmlZQsHY37BJUOTwTdnHvxZdlsw6U2UIS80Cdhx7JdmZFnTe1_nSYyTpaUw-CWs6L8CXN1PloVAU6lTEPhzGJZI6brfnHkag4lcgWWoIlqtt24kKE3SXRZSU-YSUjgOl3ualKFjm5Vfg56dEt4cgTALEaCY793DrqhPgDIyJGdvNK9QYqACn0CTWAhAAHKpHxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgZUCmhykounUxbxCR5AAF5o8i6K8fmEdwxitkDhQq7wfJfCqrFcWjLvb0azhRjdByRXvCvGxWDjdhTR8FzMpMUGTZdCR_BggUtqrhEjxgQDa-Uz7-GVbqTC7-YEDHl5RsqfANQ_ZCzSZ1o9GbNnrOVUsG-eMJXqzhbagMZlRp3NOvtmdjidGaoaGx6hMBCiVrtNUfmAIEgNnPT3lWUf8X5l2iTRywlLefE19jhacGEw1yLmWCnfsHQbYPIckcNDaErQystHHrv45IfZ5AoPAipsEtum1BFwzhnPsh5Q74qMsKx9NJcD12fijcjX-ihfWAHYxgzvtdTmlFc5sDF-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=eoOEqyMbmmLpCGbU4kODNZa8Y081W6jhsqdpeIlljJmx1mLFreCsss_UTu6iKUKIoD_FymCA10lJIOBHXwm5HtLsnw-uCGQ5z12QL_5gAZmRew-X7i2jvUifxQ5OzoAdUhGfJvL-XI7HBuWXX3mvsQdgtqarB5DEA-dWYyuqn-SapFpt5ZBV0_KrbK5xJQ2LYwVe1JGW3iIrtKN8X-d-PumcDNdSkZYBAMZI9nhty1NNw7TrvlD5QwJOsYpxfSJ37EtQmWwzj3faj-4gSaEx6vYnb1ZddxpAggHO5xyoMr_nv1DepOfEIXvajcauDG9Go2vXGSp9rOD3lZdEN2MsuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=eoOEqyMbmmLpCGbU4kODNZa8Y081W6jhsqdpeIlljJmx1mLFreCsss_UTu6iKUKIoD_FymCA10lJIOBHXwm5HtLsnw-uCGQ5z12QL_5gAZmRew-X7i2jvUifxQ5OzoAdUhGfJvL-XI7HBuWXX3mvsQdgtqarB5DEA-dWYyuqn-SapFpt5ZBV0_KrbK5xJQ2LYwVe1JGW3iIrtKN8X-d-PumcDNdSkZYBAMZI9nhty1NNw7TrvlD5QwJOsYpxfSJ37EtQmWwzj3faj-4gSaEx6vYnb1ZddxpAggHO5xyoMr_nv1DepOfEIXvajcauDG9Go2vXGSp9rOD3lZdEN2MsuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miDak79R37mlu6kw5JZYb3gLRK-QebLkBDQuREEfJZoKO2WxQivYVOmcFQc6BGU6MA5zrldKWh58kcyb2NW2_cvIXSYKzEprrRG_PLhHca-7BRh2DbalNEjo9D85WWXkc3a8J-l7u4DJqhwQUvQE6Qh7egFrOd74l9BjHqvDmJ2WvqDJCSlz8NSAY5zLWUPX3KfCzBEdMEHmrUXYWuPxDt2rL37ejH8Eof93VEuTifWRAeYMsmCzZTJSWm4vut7CT1nEGnlIn4EYJMLWx5ct4ah90uGWAliHmg_Vyo7L_RAooTSx9Ej14dAPsYV4ZcExjGbTMSUNZG2Laq7q1sFOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erCpyjAsejUTw4bEvGdq5ndVQNJSFvSyr8N5YPf3sjIs5IgMfo-ahINb14AbwzZvEGEpVZ17cE_Jb68tgotSgIsaLV8uhh_nj_EsJr6c0sO9i6tIHxNfbcAxsiFU8PHb0Qav5QS9uXyAZ4Wh88Hg6x086xYCNHexNYEfhRtN0V8f7DHn2Moyh2cqiTZZ9D60t9lfEsRvxH9LFqOcw17TrtwJjzpIaAOTjTOfRnzlUkYvRICOshY6yY6Oc2pe0cSG4O80IpZ-9tb6rKPmA3f1b-15iKTyfVT25vJ2GUvqWZPbvVAP6a0gHCkOr3Q9YkXmTAGY3s2cSN4mAdf0Fzkf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 796 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4zRSQzUqX-FNKZ96yuicYgUkAvfXLs_YGtq3PsWQpXNlWtiZ4cYs5n1J5IerLilkF2wWoHEf4CAbt5kzyNqlwCm6u3_iO-wafd7vsEwzzpJofZ_R1odFR-VXvQzYKGxvYsgzWZM9FY2Px94ttCzB0Ert3rEWnjVjpszcE5UzqmtHjHuuiCC6fdnm2rb_yp5lusBtBK3d8B49HGuwpsypAGRpMvh43bZ2WMKxYsMOuveR7K01A0YT0Dn9zbEZS7Oov3e47gwkufrwtvoSLSzzK4hDoA8pJWg0cU2LZbJy5SCFQo3WlD58Y-qi4SN7nddJJ_EGU9VRebvajIjdZ7r6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FarVQsRnN46PU_mrw73JQyX6atV_5c2baDWXc5fVNkRjIyspEzlFLx_Z3zWG9UM483nJ9zv9RSKg7lpAQc2OGzzLnH-fw5wOEHVzZNHxbuHZyPSAOoctmWIkBw-Z1Hs35Gn1zIw0StiL7yEUdtJQWPrEsRZLJzG9Zq7z5Y0iya8K4qOcfEJwUMvKsNSe-iYnriUtJWkPsOYCZAxSC-rQkxJilfYJcjTiq6Uj856VznQed2wUtuVFJ5KOhSzXV6Wxi4zOc4kTc5qqhx_Azp9KKJ_x8j7GEc3ZF_OA1biVNEt6Dc5QTaZ7YFLLm-JFG9nrvMZw4pupeuU66JrFbX2Mxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTciTu9KPLs8dWsbPAR4GPnBz6obmZDvFmTKk06MLzy3yxH1Oyf0Sn1QhkK9f_Y07Wlpf3ol22cOlRCOYa5TfG5iGjDdvLrO07WzfmM27YQNBgOTot7rTaTsIBAc_TApUnjmnys9r3q7qCmyQpBkZ2_x5MNavt7D2pI-BdOMjv4F4XigRPWxK4CSN2sc-GEMsVqkz31RHai_52ghDC7U_sL6sL_PFVenbVrSiWm0JEVSqgolrDNEQ5X3b1yaFbwplapgd_O7UaE7h5JP3l5f0wsJ42CgOK0iD98g0oFnE4jKtQLchCnvnHgWHty87GPeYcL2eQocu2Y7tOafhyVoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/optS9obs_k56UHakf1rP8EltVbYYfhvt0ipg8CLxp3X9CjE26C1xT2FN8ANqAQUrmut9hrsC8OOoHq4yF0nIxim1N3bafPF7uiV79AoD0VLtRbG3t8TeEfiQ_uS9kaSN5QjhIdADrLwX6FbK1XvuXGwWX0pOHg3Vi0adeBp_w89M8FkLhe4m3Y687A0aGTx7w3xgBz4LjN-2K0KYeMfuoFmWRJu5qYTJD8EdYPkZ698236ehb066CxPmYjRpJOymezFwgY_g6H5KcsNG-KyBhPeQ5sPj16fJx4JhrSuNyTeZhdCQXnysVaS2aQ3K6A1eC5dWB28veelV0FdBB8z09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 759 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_e6P8Af_XLetj0GlUWqcEn20F9e8Wbu6h7vUfg--D7HLpbYSpblskwKbpszN1PMUnCgPX43fkFclDo3BJUZ2y-o4fE_7p7qdFhivNZNo0zgNM2a7l5-eF_C5eThA_RWW-gS7REsSt0gF0pACfZcOq8Toz95bQLujOM_ZEnKj8lb8cKkyMhhLXvflwV798UQALZ0LOJfhbnkVr1Zw2KbYCYkoeOBRJtwtA9G3VKSsTbxJaonm51KFrAkrfmosvD-5lug6cNhhA4QKz2T9mIr_JOH6sq-FHDn2qodk2xyd4Eun3dKw2DVQNluvH_ZiwAtW14XTbcvt2-aY9gb0erlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OChNfmaQ97gLqgE5ITG0H0eRcR5F9fAu2esXIFOu0ZbhxlXl0zWGKTmRRafafEZL8ks1a7-CzBjffXR7BTlRKw3gBtP5t1QOy8KufNcYszeABK4iUytywHzJhZjPKsiGtPdxDM_Wga0hU33W_39iLEG7cs9q8HxJcOW6_CN8TusXtzUSegwmUbrAUUn7k7bFNHJq4HTq58xI8V5kROr6DBR19oE0rb03s1gzbgpHyIiYpDGE5KJ-dz3omkq9Cqe8wvzdVJfcjDlbJRFuhAhese6oD4powO-P_rjm0X7v-4tCQR59riI2-0qGwlEeYp-pL58ex-3pmW2jTX3j2rVC8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le4tYpiafdnnpMeQYRemxPfQcmYkcpUs7UP4LqfjaLaQtIt9T3scaNjxki7m8swRWRNcmNN-d7uRxv2p-5fvlkh95hiP-PSt3q0sEPSg1e1VCUX-8NMMuQo1AQ3mZJgAXDlhaInMEWyV9_EqVYPeKw0EA0wXvQRQUgsIfRyqEPYGhwVYTo273MwDXiYr4ge6_JUBxiKWW295naE9MSvC8fcDcHpfSR9XVkWK1bRM9Hl9jscU78lgwmp2IaZyr3C8bHNcZ-4MtkV-cO4lgce5VKgJxmrUbR5TxiPEo7hLI2kbWm88H6IyRE3M7Cwjj7vcrLPInbmAi_ZWRUv6U0hfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 826 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 732 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKf4KDdVshMSXhmeAwILHD-cmUgiKWv5Duz2nf0LrTah3QjD0P9b7PT_iqV-8MEmofBDnk6cySLNakRz5Nux_XHBIECg8C-NLJSafK-sYdIbKMPNByNyfy6MwYUuayE7zTTPG31NXweWvGpUf-tyXfe5fz_40dIAfRnrVWYXJ_oLOR8tKbYHujMYpmZYSEdRRcC2VA8QVsvRdAnK2JDtEaR9SeF9f-mhf4vg_yTKQc4yozvz75FbSAXog6_2raRdSeESBx6W68Wj3faGGx2AlSWUq-ixuc-69-VgJhatiUedEFyIzJGPusgbcLHEHN1LHdeyB5KKlxJB726F9jN6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRqBfwjWVJMVQPr9EwB2zvkjpCvJL9HtMojNyk0G0z9Q1C7AGX9MOHHgGBhN5lecOpU5LHXuaTPY6VkTgW0_h6yX7w44erUULVnigSBPSnk3f77vI2WrEroGmBvde-eq6PAPqfNBRZ1w2WSBBtBfxRC4XL97fwUtskdjFmZLIkTzIGhFPOZdst4Ua7lVEOLvCPA3YkRC37GnKb5KJdr2sVrYnbN5USHJ4XaBEv3jUOhkYe1RYxSEgLORKHmXmF1qqUw1fUoDptQywq-6K02i305d_RJafaKRnpTw-5cxUBkw_yU8C2XvhYi38YpFladO9lTCElf9VLt7IUdfd7DUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 614 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5rD5lcl4JOwVhn11xAmkRp7o-3Vcl1tfTLG_BkBaQisxJ3n-pT7FApODF3j0oJhOwws7UDzxXJvZ9e8QZ0GAPF7rQwwlKVJ8hyXQUmoo7hKaqWNk1u8h01h-jC9uQ79e42r4FqHog19qlQ5YtcIiF4qIQ0ZRSxhsJQNMCt9zE0-PHLPD26Ye75kEuCZJd__-6Sv3TSl2BlI9rnMKZ67jD9mTrVNG2vmRoS991mFv3Tod1rNyYkSaFoRUEnW86e7N-MOFbVR8pZfShzQuGytnOkYmb39juC-Sd7ewtkNliyGkpxhyfC0eyDbhP9x7PfycFPxM8X6QqJYWUGvethYdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 651 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtDhcdQXpHHwMjqtbFG_q0DNDoKX_Ddu8o6tw04fXb5Or0SkETkBIqFe7li32Tge1FWiyHm8zwTiqBsjLmq2CqshZSoKhX9a91hoof0Wfa5Lyc0d9hSvHveITgOvK4HdMdVb9VYEBfCjfgik5o_QaxFnCO6AAt5WUlRwpRJMk6ouxHx_h5eMYMI4ycx6KGc8xoB2s6LWRrGdMY7cYv5pPmdTrGSwqCr_cOCU8yUp672nte_qSCGButCi51ck1mq8BG2Ve_5X1_hjB1HFNnN2EOqYAm-VIpWZDHI6qPc4Eo8toKDG3lAeDlvwzmPiNq8uTkLAMKOUhGhPo1GDri9HBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRS-Kev4dpm72EriueH5l8D0Npqyd0cl2HDNNVG2FooN_EgL60MuTrHdBcjRTipQwCcjl5SX68PaueiIymlh8megfe8cAbhpVMVrFWBVuKqVimG8Jagh1ZFFJrvBGxrMaHgtHLq9NLpJ6KjKPJ_zrLNFK_nLsSq3RxFRTKsM_YzOeGAaAxMcES16Ffu51Nl0K2qrAaxAU6YMDqzpwsoHNFkKmMaJZ88xH3Ms6DZ-6gvc8DE3CLF5L6RGNXtiBdFFm4oIiaVPK4Gk7hn-opuMBFrA5uqdFpWUXjKhF07lTpyX396P54HuvCcHF1UB-nu2jBCDgMrs57HFJAtgC9MyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQpFVM9FoIuaGYWCLTl4jaEXg4ziHquRghUlAC3UXcGoCyjP1lT9_UkOqKF3ZBcJBCRM6yB7o8JFW2hiLaWIU3zLoEnc5BLVf-lFgw_biPIch8NXuaFX1ZCcBG0fUa-eGm1rlfze196UZYeUzqi2ujSqBpAUGohzb-27iO1FSTJ8FESJge4gF3FOOXJM47MZCzpPmzB_4MzzoNHSPdxwWSd85x3SBGtSbRUZb5XmbFZlFLJ2WkSRax6IipKJcUDqib_M-8oGqzFgh7TdHWR27zWMLs7cCZm5GiMMcvVI--Uc_JNNHPciuqUWPD5uNq8fYZCupdAP-n8lbBnLgoYmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDuBH6KluhBlEZOK0bZfN8_gVpmCpZiQ8_9HmOI3sgtEP7i7A5vHXpXz9jY8W3J4azvP2F15wW5GU9aKWJjBwVXWc6RqlwRqqtwQqpIubdhOwj8KYud7IQ9JfOMmaUbfTYTwZ5vyWpb3lkLLO8REKF5kpWv1d-7tzTWeL7QU-8qjJuzwYb0C10u8BejNCoxgba2kX9X76cl2MaR0geEz_8ebO_bb6GFFNjFm17T6F5O8O8sSY31ssIH57jVlcZLjBDvEWKJnXl-JpE_tBtecgZz-YTqQ70pvuqq77ghXqgasakXb0W9Y5LBwyUlVzYxuoytunHbOOY5pfWjWX2Yi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U01MW8ElIFgUGIC2SDmwg4YHlo8K_07q0yCWq-9S_BQ7Kyux3tfpIQuTdcs8DqMNrvqjZEf6wqvRwfsXxJ0JMKmpbFEGirIACT6qDc7I5BO4blZiSCiIYqOQ-lGo_NvSQ52q5pviLHWwVVnr8DDAMJLga6Jf7s47coI4Wv9c5uN1OVkrsUCvYzlF24PrbmeyZK68NYe02NzOKaQfki5UE_yjHUT3Ct6M9XXZQln-HlI6LoS1C_1-o0o4Cz3GuvfCgnIQp9o0okPSw9Q93jS8o7seHa5uHQfEVG27uF38ZDmneTawrqyWiiknfeo-QzRzGsSV1_5gPc1xdjRPLv0XQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxcqERw7LA5ngPL8BtGQcTRihvsokeMkt5g_KWXSIop6VVVNWZoVa9bPSdWQFg1y7UtKXV3Bbe5TXnrxXXTAO9biozJGb1KpjxYcW7pLzTXwtVT5WLNUEGOkrEOrIwLczWQznjrEetiBOg4CNfYS2NztgdlaStarWA0enInw0z6wn0-bkQJRLgRQt2kfqHK5iCKZ8oSzZgba1H5av6tRPJYtEsFRy08fH2RnjF1-i-TLwMqh0LXlEaRP7_tdfxzlwJdaLY1htoZrf4yx6udUjY_OtuM5KX8xRK0kRnJ_bdtxBmSBU0PCbDNjGeo1RPYxM0a1dfNBXnwVQcJC8RvUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 588 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyUcTygAND0AwmNxjmqHIJmJCMhzJ9Vpb-a_sndIEi40RDgDCxJolrBTlnp2WVGrlhXViFq1LqsU3wd0aWBRZhJSerX86202na1KiroNxIlb_vwsafZmcpDKwW2p7_5kbdsy8ZTGf7ynuc6aoyiTtn1SMJU4rYI-L6Ed3IyXi-ovVK5V6kNjqZ72vurbsroBEewIN3zWfzt93QYd8730xzAbo96LY2bm5uHMryl2DoGiQD4LWiPgEKcPhlTFWZ6Zgxr3sBCLHEYpqkOywHfYYIJFCriyZLhFumQvv0LMZw7Q3wmN2I5r3Dz40waqyHNtt-iQQ7Xx2HC60tClsurylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJLISY2_fQq0i6VMsPNL4V76bYFI_sAwimAVoj3nKuI3U4OzrPijpxQeZB0wC5rsy-D1pWWFITB8D7gIpmjTnC9Ro_zd8_ZoFN9j1Zuu3tlTjsPdNiOdYpnYZ9EXwvKH6z7v4xWOkHFEi_KnpDMU3_h0ytYwpurbWxuAlxONGyPu8GfX0LtP-XIbzhmS-FvsTeTsZVjd4D37oTCchuRuiD9Gd24zz6HyNWTdUHrTARrqrlqK1IYH9oK6e1e94-Ecymd593sih0novdwXt6p51fd0z27012fUF7JSDUs2JMUN9FCOCeFTKCQN1mp7o5ZbSRPQLrC0VPclylP5e2lOHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6w_NDhyykg6cGMB8P_CWdwWfD-FdXHEUR7WclXjzCCNoY_NpCONxwRjMcncP_sGBZvSbSb9xD70dnyplNcq5pJ9LxFIiIoIyM9xTbEpwKNlc5ZmiZnaCMMpt1p4ayxvqN5h2RTh8pBVtFXkKFymfIoqk0OqrEhWuD26ZOrmi-fzuiuywCLsXdLV2PqIb-fK2XQnKbr0x9rm7OCB60qdKM9zg4SoURvhT0DJQOJ_ahWpLgUXVuGxaJqvLs40tyrmjPJGnE77w6jbXByZfvfx57VViGG5uj6l-uDaUfTyZCtlzzWUJF0Jokv40c6IyjpOJAk1prAeMR8375eI4KkBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 654 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJitE-2ibqcfGk7qxke76ZJWdRaW0CK2o2BEcJRFjufbdrf-PiufeYCEwJvNcoUEL-dqwo2jJlmD2gkqG5I9hDdiWp0dp1QIYFNoJzK6JLmxn70vCRUgTfh-YfbP8WawfMe6R6Wd_cInUZXwoVMAn0auvUJnuAa7jbYUYd4p6jRqjRjZVDLAccSWNUx_M_ZjL81Ogf1i8eM-mX9FkU3DVg9HbmDzQT9DgVsLGCL6Vg7R_XR0OhLfxOrDN12imM_nMt2YSixdf2WZ6WXpW73WOwRzHyhNXinhXjegnnBLGaOys0_djws_NdfHLTfnp_MkNmE__fAmhVn2ad5Pt4_qFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 723 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eljZtAmr0SeiyD_R6gIi0_f3Q9_4EhJrIt0FSqQAQCRho4lHeXGTFS8vj6vUk7aZfqrwz659HEj6z3axhKQvBsPHIcaUeVHoOKW5h_PsWGCjq05Ymd8WQ5NtjwKCEl_X7WKo8LHtfNTWIbQXxbvfHv8e9VznmqQT9cn9J1cEr39zr3QuTMUzzTjr-JceTllFpOz1aTjC-wJ8NMOA7eVWt2LHIu0DEYg-ZzV62yIakZXezOMeh74vh1-qyPig0xySn-xNnAhElQwiobuKj5hzKMl60NytRUjpv4N8qwA9fwt7K7_ebmYJOC7dEaMg94LZLlnZD35m5dnXgNqtexRtBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_hGmCHMKsTPUeLlOF57s_r6c2zpThs6QUo92MCug-vQm73yVtstojRAaadormm9Zxga7TmOB6OtK-gB1PAT1bhCVT23fOmVBbNYStwQF8NLsAGnpUZgfsnRFx50G9h7D8NzULVcjbbm97jz0RmkPK-nEvQj-3ZdbUei0XYUV8NgYHCS_qXb60TStYk-rNiZNBJTOFI3aL86MJmRhBwWdPNNQgH4vM-KguabZt8-tsS2y4D1d-BU47M22YeXykOMT7cisf0hHCXFzauEoK4Nudjaa01-LKl_6cy2D98Q7Br-9zpnJ8PbfYUMu2Q_y5J3Ohjfz9-p8Ci03b3QllgLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 650 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaq4gHs4Vm0oG64yM0ZHkH8raLK2QlEJz_R8lJqZGD1-DGYrrVQTkHqSHmee7kIzIKrfBmvyg2m2iUsp-pUO3jBtED30r5BbBhtcRX_-yRYVdkx4xK-Oaeh0q3Lm0kZRY1ozxq5c4ypH93LQZ_ZViXGy4ou0HA5kCPKGvzTFPL6SfRSmAVo6ECDRbJDsC62yp9ylmBHrw8MQx1jwvNbx00AHQ_c5IuvObtmoDQKnWFMDXPFu2JJM7D_SG9TG9xPwHi-zKLlF-cggatJyiLKYgU5Q43oSEoIfOZjl6-gMBR1lt1aEyCjZF2ynl86qygYS9XouVTGOj2_KGJ_DqeWs-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_JEBTUiIV10bsK68O_fQm4aNTDrcMZJuuuY8ikgeZeIkpCvmS497jpPvVVuCSX40uOF2Tx-a3dzGo_jz037NlAM2A0UL1DT_70xckCrYD199jIO_lBlVAdO0Dg1bdHUwBfmWYfWtocibYPRZdLXM-xcgmXEE2Lf8AWTGPiT_CCLY2lJ-vFxs0tjuxFkWBkywiFx1ve94azsKEQsmYRu5PQAB0emjqrsY9x_kVIJ32dLBGPB45fYNcChE3etV3H8DCgRMOe8RgRdt8mJVwcO-XIrqVX-eEduyA4OMQVLGj1lMfwuRac0PnwZmqHHB-9lOGhH8twfRTJBZ3qq2s5pnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juH_6YoU8KLgl8I_86bFLA6ET3W_Y71oa9Vcbn4puBsBbK1-w4HBKxqwcH8ZF5e-mzqeN_jKad5Yy6RrMQ-pWVQxhnwfr-7b4qIvXjgoHfbii_L7BW3U4nlqF1ofZd2HmnZ4s5TYAvimEGc0tcIJDns1WUF-UFx70siJogWpBl7PKTUBKGNu4Gbj9xuBK3EK95cAwdwF2bU8V3wSMRkMJ1rUFcnVkSIGj1ADZeIgK0UImua46dFiJjAip2vQeMx9G6dHDFLskDj8P6wUQW-lzIQZtNLxYchqXrQkY8UQN_2asHXyK9MXg4hBF6i1ny9XEqat3aKEJoUEEimh79vvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 555 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMBX_9CUBRjs-35GSFiDSUCaZG5oUp9oBZV8KEffi-C_6UTNqE9FjAz5TqMdoFkw067V75dGG1rIWQO7Y8X1zknwVF7jrLswG3KGs2PcWeu_NSNeH5zgpnf3RXNsZFlTgHLNC_C7V593u9p9BKwioPApEQhdGA67QK9LbalW939hRUIOiQZqk_PBk7Z4FWOGJT90vSahCi-QzAkJHubp9u4e_TI4LyJOaLbGHDBh8LwNnay6-NL7AHBdZt2U27unNge_CQcrGDmYkmtqe2v9lVUEyhlRdeVI_wEbTKF3uY7u2dIJWFZm5_TEAr3y7Q3W5HUEsH62JIhKP39g20DSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 554 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWPICOOc4w7wg08mmxxmnxA7x_iOr_jK7TienHgDO2MYqLlaeGrDW1xfDg5iiZu9zF25jEiup-uFGg8eT9MFdewKbSIu3Zfw0eLFkRrUQ7u1hIt9uKXHGEFxBb-Q2Xr44zSpKn4FV-Qm4wN2LdQkFc8suRPf4UUDbw1tWA_6Ogof3gAKmi5SyOzxgZkwpU6fbv7YEIYD0rcrJO3YLrYBqM608fPdb1v6iK-kjAen1An_J_uE3xTuoqeFewge0wqEa1nYgwA1lQvycLZtdEusr_PW9GMJrFiN08VWSIDX6JHRTTO8RkLJ3eywe40OqFXfGFq-n4jMhUxC58i5CKzvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 678 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIBeQwhlzCNn3JKmypeiXwvBidPse1ExiSgZ1EgFsiZd-lXXCPKlSd_V9BlcKYOHKcgHvSSA1yyWCle6Qs12UW1imSW_QaZlPz9Jd51nQ9SiSAJ5crl0IO5mUDAGwlBn2zALAU3aLIceB27cJGTrX8cHWj1S-PTZWoHeBNd2C3iW14a_vMMewltmn9s3Tf95fS-nYe9ZGnLgHMQ5vbU6pMTGYQVw-94WpRPUplFxVghoTvAlpqn_542QaRd_HCZbjR0jO_KpKUXZXPoVHPtpDHeLcIpqAcdSJakPWyJ6ZRwqN75qfOzXAJR3OtOD-8k-XOPvVYgHOQpsukM-aihoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6swY6usgoHL19y8JYBfUK0NMpRM4Y5532wQTxjomAsMpQCzQmQLt0q-r5AnSLw2LqKSw_g-Wur_Zgke3a3HnqVmzVG2YpI0QFsf1HRGHwAA36EMl956v9x6x7g1_fUanw9ci35z3A_GubdRmQbimYfNWf7ZKPf9EywJwI0Z6K-tGjTi7Urs11SXUNZAwbxg-CCedEugcPj6oK4sdccdXIsBHN7303XbnOO5bJjL0paWMr7RCOEUdWh-f68uZtVG_bfD8v5Vt_7LPU_ZRJ6GVOviZyURR3A4YxEDAD3hieqpci6qUuxBJt0HqVMUgvKgJgf_o2aQSnCu1dyfD7eoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPXYUmYRR1C7quLvr3JcAlGXwwLvlTqjboxRrE0GiQhVueryKysixyscyfNpTPnqQuz8DSPFilr6MEeUNlvOftPDycpHSS4R69YajhPHjW5Cx1SPNmpOXuJ4JjaYAXfCFVAsXC8pRvGJduIm7qa12E7MCNXDFplBJfR0U082U59_WkpQ8YorbruCbeKrtxSdbV9s2qfpOTO-OO8abT8olMfkEVed_bHMJtNc_7pCq8ahWZqSFj2TUucoEzACjNr8Aflr835vTPnl9dRxozsEH22p0eMXD0GKDuGStqxRds7yQPDMGot6amBQnZyfVebr9UZcWV8Ib_Q-3vNnkOCodQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUwGgqDfOjrcxhGsOVcSoNnVrV3KfUEso-e6exxq4nTxQovkbe_TmAdv6pIgluOMsJYcWUji05K5Dif82fCvCx9-AFKYfhC_6Eju5TBbQm7MLeLzbi9eCL8fa-3Hp69r_EttJ55zv8_Rps9i_HFWbVog0KPjFJTlv1oyXYDKnfGIgT_t5IKUjmF8h7Ks07DXSz9AXGWN5tkYbmh1u6b25CZmHxuLSm0pIEAxxwp5mCCrQNKM2fT9U4EAgdN-xcDcoGE60inQgcxy3qnVRpVtB1ngMwligEXUeuPq3T6hD6aOvQbSVhfGEbuJYBrCv9ZZaPA-AKxAsVpQ0slyfYAOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcOJwohJWk0puLtlhwlQD56JqvSEB_HJpCybZ-Abu80GHzNfal8goSqd2oykys2wkti6VflqjV9-tGiRo1TTyTO8-7-65NaBFZWJdSBj_7RBIeTFXc0TRLyMXM16vFRRUfW3Cz3buvt9VOwUzZ8US-P8Hg7sbQhHh2W01TL4cL7VGmj0rkWDKZT-Uboj7KkbBzZBXbcvZx7zvlkOhXto4NwOf1LinuKZ5JhmIwEeUzX3tfpIypZxJ77CME2SxTJNQYlzOkFiOrHib4ZAM9-ngUEZ25eevFscXwVGXO9lvCHlSRUfqb7Nb6mp0awdbKfceAJh6FAYZQO7QwVXxa2MIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMzMVLEXyzEK6lvRuwmP2NRviw24AlacePt6jim-xnE3Tzcl4WwTGuW5EoHdVKIUKH1gUu96KufdOqGkh0k-3LKcBnrYuIKD2pdbKGrvYrqI2IeoNyAHi9ZIRXTToliVi1jjjmHyeAIFPmpucWo2vdyO-DYUeczb-KpHORl8u5mZ8qSVV874ZA0sQFo7Yp2bqntPNLWybGEJpzp5pfMhEL43Gbrx0ETsbwn239eGEdkJHpbngRWsv4WIm78Tvj5OS0ZKbhYq1GRByT9rj0bPP0c80Uj8vzWZ_8VcYQ25kljE9tZaGmLpk2VnWBU_KGX8_9eQHIDVcVkyTurEGg7SAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 590 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JkRz9hinUZzCiUj2VpHqGx40eY3nLi1BIt0B_dwSEpcBbmwB1XqJEeIZB6wKap08k1pPL4u32MFPjVemcZuvTaXz-vQIErmEvnx-UBDnvyHqNtblcJIMZVq6w-0Hwu3PczibPXTQ49DcF1ceqi5GCMnMquepMqfxNquItTkw7AcKaCVnfCZ8pZEi-VS7T1FGHhpMza5Kz9-JfCt1wI7XKJUBZNQBhUuShoL1r_p3uEgxY073m3dU0uHqppIUQTFQ5Ogr3pmyHPtB3bktupquWQuRm2VXuktE4twn3kLcxblxOYz8hRgedDBwcxXwdo9bmM45--ENC5T15QPE2rcudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzKTPIxNhMwe879dtiNSssPwFLT_6nyuHh2Hmpu_AlfHskHh0OjiXEYMOZU7cVu1Rp1rJN1TfLh-z-8cWKJ3HGAqrkOSBNBwTdeFxcxfrGd8QljbmQX5zaJhA76FPSom-PM0i_RMa9kRy__6zLu3n-YGaGHXIwbejMfAppfFaTVDqC3fysb7Pb6LEVNoqi42FfD6jr7beyepogoCMBjC5q_VqXbEcghGeQRzpZpcUKpfebdHbAHQ_Zk1Vg5TibVVpq_Fy_HJf-nDbu4negNM4PdNm6ONmQEfY6RYIrmsNSvVjgA6YF8UxZKHtbVH-UojR6nGQUwoXhvWkB6_QcprrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kvn7U5vqA-SYagOOjrTgoLWwnwR3sQhSqcYTzBnDN2_N3UWHti5JgXoVBTS3gDiw3Re8fu10hy9AuqyywKFhUj7AA0Jv1QCvjiiKVpZergl9xJZfhSb28C9_t-J4bbeDRo6EYJ1S5VOWTVDvT37VRl3lti0_NOGtfUjwAMG6rTB4LJd-3k3ibd8EBvNrNpt7M7t5Rns7ATnrR0883MuvKjdRtklnMT9IkZXcLsGIoAdyz6GsvbrFvvc84Ita_A0Q1KW-AFT2lPOWlL_XBbmk6NvEBbtdftnn5mMde4TKXkSSbzCe7_9Hf1nBZ1FXYv3fRvxt0fDrbWYAkgb3PSs5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 722 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feUHWShcYzk7bwQbTrM9L4lxg7P2CJpjnl5i3Mz8EBGAwe2P2seIlFKi6JwHbjz1i2MmXq_PZKBEZs5ECnSU6lMBtvhX-Ff5otqC8mljlvnggGvBzT7XrdtJPZsBmYNxz4zM5WxhHsKKsTYr1AzvUkdBeAVwpmmZCwl0Cw4khVRhTimyWKHkdOY2uEoNkyG0pgaSnVc8vszJSuCWZJLWQWtsxOtwxfUtkfVo-n2obIaEIrQLL9b4m3k8HFWxbLN1VTlABTPsEBJkxxI6COMToF8ImdnubWPCESxM2NgdHnMC8xUSl2iJtPLxsC7ZKYx_VTNG8BXGs5b5LVOEDM6H_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECkqLjI-1GN2wHnVxgyPGAt3Su0UNce6VX81leY8JNBkKWUJl0WmwSeFNCdfKtuwQ1aVZ9b6CbN31gF12IibeFMIYAXYdzYsKhW5dTMh0X41S9UeySYiraEhRJTNDzbhXqajriGp0XdTSJr-OaGw0rFKVBomFoAg4PQyRkJvJgpNG0RbhehxradFZ4Yh1boziAq3uzjOyz1MrajlFO929-pIMDZugbRm3FgklLMRzv9kCHLt3XFllDd95OuMtbsLuP4ZyHd3reDQbpwhNuBD7BEtvIOn2rCRTqxYcs7yn6DWoi-dlZgViG5VZEEpQq94nf6YlA8E9dW0YcL-5uoiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXD0ltRwwWMrEYcKJBgAa8oxrwWejhLNtqn1Qt-PQhuedKrNk6oxS9goWCuvK1o0QxciZLJhfM_EygRDAYeJwIIEEGJpag02g1pCAA2vVmdnMweZsBGXciT05ShL9enpJ4dhZ3oi3-AaMocS9Ea1FnA7BgT2vTHika4uOfwEnuaOK8yed-Dn7xl7jLNJgj6ydjR25a5Wec4VMV2FbsrLgFu8IejRsj94d69OlnGelGumpX3B9cSC3V-FTTMUodK1ZzR39R2nQPVpvRCzku0AfprompAkvOYfdABEbpnEzHspg0dRiYv0ypSwRAr266hLrmPh1GJ8cvHDRSfy4CXuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cp_64ld6inmi88RxENy7RROHQBzaVI1DJrmpi6VNoTsLUToute3pjYT-xc4ayxzUNXk9MsUDhpBkffrt6Q5QHuNXpzwqdFGoYWjboyhbOw-tH9TDcltiX8Tpwwqx6uhxml2FuIDQDHFqbRBaJVgXBJefHBmyCjpXSl1aujILtAgjBXgYYIKTDgGPWi6_7Nyu9xr6K-77o1qRqcHOO3iE-TWgPmvBlu66JwEGht_2SphN9En1drG_eguszLq2piT0hx0M0e7aj2ISz6jpyvbTcTOx6aCA-MSdAccM3g7iUFb-RQFHAlFTZ2SQF7dOmKIw7CGYEd3QN4oXwrafjZZ_7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpWxo76X2CkGfNumV0A5ZFJKO-P6ROPHsg4A3_NIsL0gOyFatfAdLNkUoUyniTC-4yDOrUjdn8JQJyMsvJL_KHXgz45VAuByG-gKVvUl2N8MoYuqxanFFR4kYiKAjjP-pKVnSTGJtxifomVeMcL-ScNGPz3BonMzVdl3q-BrbDyMGnQOoQr_HDV6wzyBolShNwU1gLeSEu5zfY9eIBBxfeVcIXT0n4BsnQHBPEXKUQCbZBLR-rUzNy0oArHfSO9lWKpyKALeS-8WPuQ0gjPS6O4WrGj-x5D-qUw_kHCIBZ0NmniNn65nX8XTRz6ww1fxqszC_jpQheJRX-MhSCrFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 626 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVaEoixtTL1NHdZGVC7H0vT6ltk-ZDPeXVZERntZe6zPDBGMlf1Lia0fiqb0Kqfmprv9dSUsZ9wPt4A2-3tByy6woTt-xr4PJI3_KiPA3OUqPiMR6cpxL1wuzdDlsctWK2rS9t2nCqXdl4XIYFfOD_enWr-uGPUf1jRzbU4qkhuGH6LUTxmtX4W_24U5PBrWItsih7Bk0LSm6zLDnLCELSVZUnrhtDdeH4GFpnKluOuACfp-y_XC2kHkVjHcWQXLE9ihPhAQlL4U_JLzcxu2a5BANvXQlcwEqSjgm28fmAre3DxErrdd7DjVy0t5JsUWiUd2RGtfQrO4AdY8HzPhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji9ONR2FSxqlX1HqBiyE0PpSRO08cWWYtunzgX3p2m_wUsL7ncqqxmTfzXwm_aP4O69Ctg14B-cjXQc1nvvj_sqUD57u9fgsM0tLJ_GxL_NO_UkURXf2b-a6tWuFpsRRleiCSOIjUDhHE5BruY3Rv1aI2_hc4_37Ruszn4CLt7dbyzSpnYgCxhkeE3TgJUfsgtMwnlwLXgNztR2raBT8vcfqgG3iRMmUbcbirtjg_8zZvtW0Xx9N85q6eIQMy9iWfVkIGMd22oykDzZ13uOqEA9C9qb_1axwU6m05bbsfTvxF_iBZhJBajlOg0NKZju2Su623MdRu9hKj9as5qmdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW0P1KryFwCrV9AhYLv2r3iXqXvKzhklb2r3VxO1z7mSrI-DuU3ozShhxTnvok1iMe4skqDi8U3cfOIPar3wlMK21Qu9wmAMURmerrUnWJP_i2V9CQ48V4ajvgpAPbQ0hu72XmGhRBJLXOAhSGKTAn7ppbK_lWpLyBKj1I3WEtRoeazG2kmAf4HIAbZP-QRLBbONVz3uiAEK4HutWEpanT0AME77ZoIlOGi3oLNHqh_Vetgif52921JQaaFngDQYNSJ_Yiba7yOEU5ClczZeAJvWm6-riup_omzSXicIwu04xBOlexBqInuy4FFHesK_SnQgDGEbjob1kjsr3MFVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=LMT340dl2cFvCKYFHYnbgelbFcJvTdkrUJzdQt6Ie7GYN0xTLliAheFKElTwfW8AnFokXWsv0wmFEwb52TuSTEnv_dWW4exyaQ1gW3i1jEkortjPcLQBk4_CWJa_JctXexEtmZHaD94yzZijVut1JLVmafJj5gYA3xPWMHicaMdHRBtkH7UEazNVBk2KUkvCCSx4iXzdYKcjfQBb0bB5aCzHtLy1d5Xbdid_IxhyRk3eY1h8vWtNVnEsvpcWYHLtcn67I_KpujmDiNtnokQSS7pNpbmOMvqnfRPrQIiGO-hXgGTYZSaP8H9wn_p71QPFRTdm9_Yh5XOnFEiGQgxNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=LMT340dl2cFvCKYFHYnbgelbFcJvTdkrUJzdQt6Ie7GYN0xTLliAheFKElTwfW8AnFokXWsv0wmFEwb52TuSTEnv_dWW4exyaQ1gW3i1jEkortjPcLQBk4_CWJa_JctXexEtmZHaD94yzZijVut1JLVmafJj5gYA3xPWMHicaMdHRBtkH7UEazNVBk2KUkvCCSx4iXzdYKcjfQBb0bB5aCzHtLy1d5Xbdid_IxhyRk3eY1h8vWtNVnEsvpcWYHLtcn67I_KpujmDiNtnokQSS7pNpbmOMvqnfRPrQIiGO-hXgGTYZSaP8H9wn_p71QPFRTdm9_Yh5XOnFEiGQgxNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFYlXJHvEriBvrxuRnXK_Z6ord2CC6A5-1vozs5xIF8CapM-YIhE0PSZ-dPENEZ-jbRyGax5OxgDAgCI7dkl3azOqzAHokGexbWJZb6Ey1uxJBdAGXjxeSqnVxRFK1VoDRBD84cDgO6-GMLQ0XKXmRBbYposojEQop5QnZSZy6icrU-SygUd-SYK0vHH71bGNwBmsDivx7BGHpEhrLr3dXOvh81goYl2ncZI044PzMwdl-ZgdLxyl6c9ezw6_4oLSi2RDS-6A8RdfIq3L4Um5VXF-OB9Ec50GWD_Q_J8eCt2M1azvM0ltIdWe_x3hKA9VW8NLNo2uTTdkM6uENfglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
