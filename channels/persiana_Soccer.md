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
<img src="https://cdn4.telesco.pe/file/hgncm8MDeYMuTtg13gus1jZ9Veg4vkeDdTH_VIxn8TWlFWBUMGIS46F2_SJj1sctRJgFkYH_2EY1Qm1QxcMDwu6Apgmpgb04tE20aRKk7DYLlCOFfDY1ti2NfRr2zlnEmmXsD9o4wDo6uQD0M1-V3JKbTeGotrQgO6aJoLQBVrkNFHStaXafH5Hrlgntt_Vl8zcOInsjiRY_TNLmCAYjjxikynbsFt0HWET7VjRwmsk6ZrSkswZdBt6vGq9Dl8oopsMwQfliCVUC8sFEwQM7nf48psOpe58y3AsL_mQPzfZEUkO4ZKlp4DMJjyrLqPKPzBRZOjId0eJLebwp2sjvXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 619K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 06:54:04</div>
<hr>

<div class="tg-post" id="msg-28443">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu60XcHnu7cyjqMUsi-gtK3cBOtBc6LiZGiVaGnGnpBpKRIBcUS2lZBHFqjKti-vYCHlgrv2lBRMY6FXB4DLpC0fK_XO0xUvjwWK7AbdKP4qOziszL1L6Wa1z-XuL2mHWZerXqsSGecNZQwLnf24fHsLIHojOTe0Ircwc7-Lwfl-tJ4itOTScxLV3DaEXv4793zTdKB6GRKjHzWLqmD-73UVC1266i_X2x9VijMCHkYdxxOuZwv0bXC_cKksuHTGdqMPcuuATClcH1rlch_0lQw16L6xb41DxFgG0N_X5QblaQ9kwPNG3F8ZSOHJBWMKRJRgtpPB8xcwJJk3vfnfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/28443" target="_blank">📅 01:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28442">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=Ldel7drWStYvk1gW2WH-uiMHvaU9JMM5Lx9V5RPymhu3jAWRjkxra1uSemBbjz-VjDQJA9ZCRnsE7FceClqRafFlee667sGnNoZYXU3OVtOWPmQw5xoIhkxIb0zZew6POp0OrEdCDzXxxDvB3mKvRz9qTlB5c7q21RywFNEHRnq5LNivbf5WJL1uNfY8tuMeP_F5t7S1iBkn1bGLoJjvej4J3AdV3mJ0F7ntG4YSD8BZlg1uiBDjf2ogWalqP9W8jftowJ7drlz8WATZszDBPuDemp0ghmNGSCKDcoTA4Q0hkM_lkADvU1FbHXH9Kc-oKl2bxHUfjpenl7erSSBRV3Oyc-XputNeVwe1u2h0rZzufzBUGsVAi5vuJunME7yTGFLMM7Wp_iX7-LbYLbRvR6MwlodYxkvq5NB32CyMyh1JxrEy0rlreRZFRaR1x3iedX1cTIkE5pGEVK4dWxLSJz1VlvFm2iepVvBKIlZ30Dbvict8J7Cfk5pPXvlG4EnylKD2b1q_C5EfaujSM-iHbZ53aXh6xbZqIzXX2vG7ZuIzKpOHKIgVAngERQLed0DptPYoehwIF7DUVB6tCoMC1FkDxsn8njrufMyvPiqvxSxmGHBSzT1Rc2RoJV0Q9UPq2rP_Jh2YOb2Cpvc_QrnOGbqR1lfL9kvE4si6ZDk_6Ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=Ldel7drWStYvk1gW2WH-uiMHvaU9JMM5Lx9V5RPymhu3jAWRjkxra1uSemBbjz-VjDQJA9ZCRnsE7FceClqRafFlee667sGnNoZYXU3OVtOWPmQw5xoIhkxIb0zZew6POp0OrEdCDzXxxDvB3mKvRz9qTlB5c7q21RywFNEHRnq5LNivbf5WJL1uNfY8tuMeP_F5t7S1iBkn1bGLoJjvej4J3AdV3mJ0F7ntG4YSD8BZlg1uiBDjf2ogWalqP9W8jftowJ7drlz8WATZszDBPuDemp0ghmNGSCKDcoTA4Q0hkM_lkADvU1FbHXH9Kc-oKl2bxHUfjpenl7erSSBRV3Oyc-XputNeVwe1u2h0rZzufzBUGsVAi5vuJunME7yTGFLMM7Wp_iX7-LbYLbRvR6MwlodYxkvq5NB32CyMyh1JxrEy0rlreRZFRaR1x3iedX1cTIkE5pGEVK4dWxLSJz1VlvFm2iepVvBKIlZ30Dbvict8J7Cfk5pPXvlG4EnylKD2b1q_C5EfaujSM-iHbZ53aXh6xbZqIzXX2vG7ZuIzKpOHKIgVAngERQLed0DptPYoehwIF7DUVB6tCoMC1FkDxsn8njrufMyvPiqvxSxmGHBSzT1Rc2RoJV0Q9UPq2rP_Jh2YOb2Cpvc_QrnOGbqR1lfL9kvE4si6ZDk_6Ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛ پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/28442" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28440">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sin_UIp4h178Tu6LtZftNQoTI728CQQDkkHNB-stJYaS7IZZA13POFzW0LNFMD50oZG6gEOFBxhDsMKe1inWxkrKWEPX7F5usp1CBUEW2_-BLmexx6rmiA12vDn5wJ03M38d-xZsbFcqxdPgEXCdD1GSy0BIKuI-cJrA8in5CBeY-iqeaUExDDdguwu-oosDNYzwCgLiVGLPayJNuTQzUuetS53g2VEuZOuiIMbxJOh_ZVkKyeem-yzfJDdGzES4oVq9RgHl6qSQ0ntSy_vvgwWgLoAO4CfYlaKsEtwfiKv-7bmoeLBu7roRKes8ARJPKd6JbPd-1MAQbz0KSXyQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
فرصت صدرنشینی یاران کریس رونالدو با جدال مقابل الاتفاق در هفته سوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/28440" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28439">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2b0G9IUPSZZaMy2v4RelEy96DSE4E08_JlPQMnDA55ZTOQvHx3e9WKFG5lF4g8_mMbQCvyFv615hr7A75nuBuXRADywJaSIknl4JQrDJW_akbJcnLlacz4oaZoTXnrZaVAHsT5BRqnkx_NyJGHjy8IhlGWteQhBflMGr2AZjd9pCY5nkADTBBzGC7j5GgzesD-ji48sylyvp-SIy2UcbfNLV9oMdbQ0Ks18tSXvoTeGQbzfvunOwidhOC20WCvbRJ0YNON0TkJCBr6U9kwIuvkENAn_D3uDOVg5_f1RGbNmqHTsuj8QWSrULCjm-wXCg63ZO2Nl8xpvH_nxiWBqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
شکست پرسپولیس مقابل تراکتوروبرد ژابی‌دراولین‌تجربه‌مربیگری درپریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/28439" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28438">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljDUr3YKgaaWN6kUKoJjXM-CsMJ8Le1vAq3XMkmmLwKo2a5UhzKWJOVv7vh6hqmE-BBy09jaL_IHXblg_q0PZcZNZs8eBsSS983Eh4yGNQR1v5oDINbNF2_fZ2SLQv22X9TrO_7fTGubYOxVlY1WLWrV610nLBvMkKLiPCm4pmRyo-gZUdW6eJHalCQaz0QjhXteFmBI-PZ8xjIy9sscU10IoRHK83r11WU-iRrjmIlpeVt4QJtyH7vjr5Gs12bkZ2NZ4W_n0aKo0CXppCPJtYZmcwRAFJJq9pMORjzJmPNKmCuAbh-TlQ1SuprclL0sJaS_AvrmOcOczuC34uUBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://telegram.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/28438" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28436">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=iT6gNXJfBHo4opVYeda1caiYccUX2D4amIpupj6wgauhjCELPFpDv_IMzKygV_iDUE_DtmKw5l40PUEA33TQMI-lCgzeduPz3DddPLFn_ZC8KNjB3BJeVVyneSor0nfoseUyhacgP_e92hEpJ4c3Sn-uhMykuR8_zNzihHxzExqxzMxbromeIgd0aEczgV6u_PCImjR091Q8hQNI4lRQOO1fD650KLate7YRaMhYLzjulqAwEO2d1Rdxf94H2pkR9yKXu_k_PYK3XvnqCk9S5q75xOQdXuCHhrBpNML-EqFCsYsCXtcGu5uBL1Dy-aXM-u8ii7NSr50-cF_AOfVlDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=iT6gNXJfBHo4opVYeda1caiYccUX2D4amIpupj6wgauhjCELPFpDv_IMzKygV_iDUE_DtmKw5l40PUEA33TQMI-lCgzeduPz3DddPLFn_ZC8KNjB3BJeVVyneSor0nfoseUyhacgP_e92hEpJ4c3Sn-uhMykuR8_zNzihHxzExqxzMxbromeIgd0aEczgV6u_PCImjR091Q8hQNI4lRQOO1fD650KLate7YRaMhYLzjulqAwEO2d1Rdxf94H2pkR9yKXu_k_PYK3XvnqCk9S5q75xOQdXuCHhrBpNML-EqFCsYsCXtcGu5uBL1Dy-aXM-u8ii7NSr50-cF_AOfVlDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
رامین رضاییان در اولین بازی‌اش برای فولاد به این شکل پاس گل داد و فولاد به گل دوم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/28436" target="_blank">📅 00:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28434">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8ECmMgLfhW4OwxDRLDjgrcXnTcvMVROJzVSABb-xjqTTRC_AeMXrz9Uvz6-iVq5_r8_espXrf4Ku_X64FDwFNU89mlFXIaltJlqphIelJl_EBfrv5Td1hWV0MVlzgYkFhEitCVyGWX0Ot5VFS0p9sTlWenAbg3GxijOimyw7Uh-ldp-vqSHSV_LaPt6-STbDGGPuSUlBCuClr75wlFIM09Y69dFno75sUi83enZBR8DJJIHYAmIfWpENtSotnSbv0U3eO-0vpzVaQRn62An51dFRottrxaQZ9TiQMT4Mvgi9LnnE9kKpoe31CzQ0qkClp9QZ-54Lu0NYWk9C_TiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTDekcDCMp0itmfwiaYweTitC50JNLF5-vtCAkyf6XQuG7S6FD_7DKg0zWn1bxuXXuG9kWP8r6SiEny6tZfq-9qXSilNGyLMaoFYLNL_rMEPq1NkgotaJ4u_5Qqp_Wl4EPGgygXXvMPWdGkJj8AZht5-RW3GhIoeN_oAkez2vgHTqgcR0HjfaY1aozUB6RxgjkqFQHNRopTX80EU5Tc-wCnQpa6BEvZ4wzeqM1tLuatPGs6EBR19_nExFCCG1OLdj1FzOohANs_lyyeffYQ6zMMduJdDd3VIGOOw6B0i4cmXVVJ0egKtaOyoZms_gPAZmdYshcXJfKUjNaam3uJnFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛
پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/28434" target="_blank">📅 00:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28433">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6hVthQ817c9V5rc6JmFr1PnCbECe1PSZFgL4JHXCFe2lAY28f-hrCAQ5DGB_YpufW_wySKX7m9Nd-XGYPYSXOLj04uFu_iNOHPCQetNZQG-NMxQSDcC9rvTIMhG2YjbhArHLyucDl9_CZG3URv-JtlcfQbx9tJwKrnWVGCMSrOc9dULpSEpiwSJ7OfDVJvV477cbtbh5VroiXT9elMQpznZe3_aZ340Lh8kl3vjO0E_UJfnJ9lfGYEGOc2jmeMlwFpoSyaaxo5jCLEuKNmOZ-iuw91oyU9abElO95MuA76uS4RTt3w3IklSggg-W1awOA2oY9dLCFhKf_zMaU0JHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/28433" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28432">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zc4QY_iWuQig7MCyRkY9vf7GlsPACX_YNJIV7E9R82LRfoG6OER0SFyGW3MqUGL_wNAgjmNgdLtioPo3b6nBZtnplVbsz1XoVC3OnRqJinRLVTRo5YM2pPdPiCZ6PgBeA6g2pF7gZMuK2d-XfBk2MfVlv-JJ0XVaNsiumDtfRBkQK8xXscKZO_5UDONfkU_8C_A4C14e04-ktAwV28j1vk10FFu2KCQLB_2GZZ87UcbfuQiMBGXa2MrOHjdlYFdOiCjp7guOQjNLBEQUqRd1d3X0k2jtprnPi9U-AKMsBIEJdbFkQf8VnzqLtiNpPdMLcNFv8ZEv7k2SBtsMq1Oigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مدیریت‌باشگاه‌پرسپولیس حمایت‌کامل خود را از مهدی‌تارتار سرمربی‌سرخ‌ها بعداز شگست مقابل تراکتور اعلام‌کرد؛ حدادی مدیرعامل تیم پرسپولیس اعلام کرد که کادرفنی تحت حمایت کامل اوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/28432" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28431">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSI8lMeDBEDqjpeO4TrPf2ues9wCBuzRR1htZ0aY6uGjsJ6NV1JM5n3NQsFjxsevciNZdfgLQmtvbD8nI-7P6NKZin5djela5iSgvVYKuO0xghAeHwH7ol5quhpdH3xSs4Lws9m4yeRi0KIO4NAVqUKZKv1QVsXTu8LcdJPb0Fkyu3Q9QDgqcJgIk-jda8V5yUTN-_7zw22Rh89cNxM0F5sdIWOt9p2zVaiUokPCdktVz2HIRX4heAI9McqQiOUGZHvNix3gEjdrXT31EcFQVbnufQir1CxjyvU8akI16LpkcyvoC637NXgFTYWlMWFIY9Tj5i1DcfxEAW1nU5Ap6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/28431" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28430">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206c65214b.mp4?token=QcChY4G_lqNcfg9gGIPlEBM_ckscdUzEyrTY4VtmTI4f6SqC2koeehO2m4Fod-lYNAl_THxfLhVqj3X2d_214nDVlaaLpVRwGqCVOTR3qET6umXThGDg8NXYm2XIEBZr8o7EthqZyJ7uirPv7aSgPMXoEyt5pFBs9rd50Uh5wq9OxkFqSj_EEQ9r95RF7IAq4-3SfsUzcb7a395F7GOwkM7gAyWNKfdwxXof3knYj5er56V5A0BXRNneWrlbzQ68QcJW4oSJOYU7GFoCaxQHTwDuZQ0LxfbkZaswZE-pFuWHAW27GEvOSOJx7hMW8LC4Ng7_WgLsCt8aR9lvbirj43Yhp9AduVh6pMBDOJWijJIxfsNhlY8qDOJfrpPRWs3jrSBRYd1Jb0amN2vFWwhtUk1b_8Nvqda1XWmTh9Gc8cqGMZvHec3umlcet4QsK_Km24g94R_acKJf0hDoZ8M4co14Z_lsmUjOHxi6yTrAo5URU9zCED7f_AHK-adW-mAjPqVVfnnZoBL04RBtecQAm_6UpNAAB0SR8kui3WkhMb8DOB5Yh1-ULDQTED_LvlYbCq7SkiNfyEhoh19CXZv6yIy38iQ3j8s54FtuSCTeJ9ilbabeIXUbaMAkFWs0XsLrVJhMCSnkyYl2JzVtW1q2vfgcQjfURQnPx78B6yxnoYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206c65214b.mp4?token=QcChY4G_lqNcfg9gGIPlEBM_ckscdUzEyrTY4VtmTI4f6SqC2koeehO2m4Fod-lYNAl_THxfLhVqj3X2d_214nDVlaaLpVRwGqCVOTR3qET6umXThGDg8NXYm2XIEBZr8o7EthqZyJ7uirPv7aSgPMXoEyt5pFBs9rd50Uh5wq9OxkFqSj_EEQ9r95RF7IAq4-3SfsUzcb7a395F7GOwkM7gAyWNKfdwxXof3knYj5er56V5A0BXRNneWrlbzQ68QcJW4oSJOYU7GFoCaxQHTwDuZQ0LxfbkZaswZE-pFuWHAW27GEvOSOJx7hMW8LC4Ng7_WgLsCt8aR9lvbirj43Yhp9AduVh6pMBDOJWijJIxfsNhlY8qDOJfrpPRWs3jrSBRYd1Jb0amN2vFWwhtUk1b_8Nvqda1XWmTh9Gc8cqGMZvHec3umlcet4QsK_Km24g94R_acKJf0hDoZ8M4co14Z_lsmUjOHxi6yTrAo5URU9zCED7f_AHK-adW-mAjPqVVfnnZoBL04RBtecQAm_6UpNAAB0SR8kui3WkhMb8DOB5Yh1-ULDQTED_LvlYbCq7SkiNfyEhoh19CXZv6yIy38iQ3j8s54FtuSCTeJ9ilbabeIXUbaMAkFWs0XsLrVJhMCSnkyYl2JzVtW1q2vfgcQjfURQnPx78B6yxnoYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ سردار زاهدی معاون‌نظام وظیفه عمومی: علیرضا بیرانوند ازمهرماه سال 1405 سرباز خواهد بود، و باید ازیک‌مهرماه‌به خدمت سربازی بره؛ زیرا مهلت معافیت تحصیلی این بازیکن هم آخراشهه و بزودی به پایان میرسه./ حالا اگه یهو زدند معافیت تحصیلی بیرانوند دو ساله…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/28430" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28429">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pgu0-IgVUnNWRTPRvt4ip20TypY-g2W9YQMbzR6DcfEZoHyxR3h9N62WCAd-iRjP14V1y9Ilfo9lhuUmokh13Et6TarwQNMTwQh-G2Q-MSxDMDcnP1zI-8pQV8_UWUqisF6FzgCf7V1bXTqUfQgeuK43b__bt0dZs_RP8YURB4cbatGDvI9_YNhY2YOU5EX1jOlzV8CzwpkEKMA8tKVE2CUShHAM-qZioozmRT6d1_RrMYPyFp4Tj5Iu_TKLLUKzIcS4Ci3CCwo6DV1FUYbVXPfQIAKslIVFPHMxfSpu9ETlMspl_kOEhjMc9tJ14_SLw2YnJREazvVV4IPIy6JZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/28429" target="_blank">📅 23:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28428">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1U99cXt9FycVmfAOyAVxLKocRjXQveUHS0HDLmu0JiHZpIqqKmmEeRR1IWSnk69L8Nvaj5jTVPkdg_MGvdYw5Gft3LgczzfZDRDQ4QRlMU9JG90R__JWjOYVeaPc5h26aiwKkt8LpklYI3iEg-ANfKKCr78Jf7UGnVLtXjNfq03tkcWAEvVh_IAiOAccoISYjAueKGsRw7f5_Fz8fgUUFvJYvkwvdCp4kc-Cwg_Fmpgvk4UnTRvhlIhV-oY8X6aaGakjWDdruZ9kJdFOVwgYjoaYB1zeWxa_0elC2MnLFByta-diHhFEy4_Eik7E5hriz9gBNVp-Tc3LhV4quS6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل مارتینلی ستاره‌برزیلی‌آرسنال که همسرش گفته بود رویایش‌پیوستن‌گابریل به رئال مادریده حالا درآستانه‌عقدقرارداد 3 ساله با رقمی نجومی با الهلال قرار گرفته است و موافقت خود را برای پیوستن به الهلال نیز اعلام کرده و تنها توافق بین دو باشگاه بر سر رقم فروش…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/28428" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28427">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNu56jJdcTNbhWqlonalyeYwwqYJcRM50La9V_dKpgHnLuioVMIw5eW91iJx_Qlod5ggq0GWPBb_QxYxyvxQGw1utq9bQ3KUUeHGT29lIqFVtMFHEqcYCUSOPuOufrYEr6UO-jongczjXGXsyqhXLzIdUr8U4YGwGvrW0ODNa1NgC8eL5tcjIWWcb_tlL4vNdB1uVEtKliGdmx5u6Sr1HnhMInG3omscnyNPS3AxOYoVhTXtABfctZ8CzQ6OYbQDhZRx9ARqVHsbEwr1r9chgppiBFWLgLPjAOogHF3yweYHfOtvTdQ4XNIDgG0hsM7Cgo93yGUMpax03vvdBD4uyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28427" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1rP5hpPM5TFQmVpPSpR4sPACPp5yH8X6VDuYoGEQfBGjngb-3mM31QV2-LoXGacbeI0EnZ3Rzxt-oBlZTcIhAKE_KTgvtg5U54F7j5lk8tS4PXRubWywppfXAXku3J9zhIzLSVF7dNcxwtaWLLA-Gq6lN5iT2EmEtNwFfNCQY75vCJGSUtcLySoA5-DP4yw-fHowlQT6YJBpf3hbq5aKJytqJ5iL9fRjiFjkaZ6teQsJOkM8fAAUpiz-IDR77kwl2Tn-2qPwWYpOz9GMlLnzxOL5FBmgqBPS6WkKLFmliIV3aAcXyOlbDTjWtT4DndU_QjzMLsIrfnoVtWEnzGOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3FPs0SuAJjfNpfF7FmXSGxte31fs5a4iLhSGrmXRPbWkf2Z4Y0EmhA2IfarJIvJqjqKgt0-fhwCgFZC2AJ8qAJ03-iX71ZMQ3dawuHr6i-DltjivLIFLpjvNdyTcckytLoficwS1dCsnRcfEGU-wXbfAm5pnNBfQNd-3MefYImNaLksreEFHj0WxrMdKL1FXCSa4bVY19EUx2t76WThl0_P1Q9xhhgZ56Mzc4vJwLxkqSekniIL4nAlfh0umy2UNO_uSx3DZmX6uDOrAjneqniCtHHt4NHDg3CJe_3KZdap4aTYzDjUXx8xqTLrmywsLdZ7fwsh6yJz8p9R8CBcMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/28425" target="_blank">📅 22:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28424">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiAg2r0rjkNCJJf1J1JDrHE4IbTaXjgOrNtd2rtLlsoE8b7h0j0MSdR7r3zM7klffmJRvSHhSF2y2xgQMWZJ9iH-Elgqx0cybZ6EvuwE7NCGxreDJIse4Ibaa8A0Ev6703s6jVKaRn7OI12WmQk4uKotjZZgBZrhnHqdbakFtANWCwYrbohMcqqkzXjETO__ojFe_RQ_qiRVLCULV1EApxnAuNICw8LBDPp4BCkx-mU1he1yB3nbXJLdjqvv_fRhHloe6Zk9X08EXOeHMwaylyZUHMbuBYLo3fPCP8KpYwnQzcTirhiPhapjLZkqfwaeFJMSRtDObJ7jXTUAVH7GqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندم خدمت سربازی در تیم نظامی وجود نداره. علی رضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28424" target="_blank">📅 22:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laMyYxTCfVfTMHgrbhOr8cXuKSdchrkrvziQ5QOhYtKYcZBDYHsQ_U9UX04um359f-rLzGE1htEB4KcJOl14ea_1TG_g_OEJQeGC2589tiINye5wYO2A46a2YMxp0JYwfUcjL6kvvOrMJIJqzpV6sHb68txb4PIdC-RR_KfRc4GYeIQ0WcDsLOi8nS1NAMnLhBe434fIoPn5EJrEHvdEFHoksRz3yOkRFO9vnLgnrp3snZAHIwKUQrtqDP714UB0rcSc4-1BhlIJJKL_QoVkBrTlOqPz99Q67eFsqh1PabmEhzEzaxyxgwgWzc-nkdXFZ-9PgOM9hSLSTa1CB2Dzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28423" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmI7kBaeBnyn5TGoNGpISAKga0ku9rdf8RE4zkytTdcdw_zAalKtSCxgDSQ5u8y_6pJ7hJPkuVRVPFoUKsN_ZUU4nc_McHyX8jxq32JOr_FjHNO0aoLmFSzRve_0qZt5B1opOWA-HDsqFvBi5JjkpQRo3oZC_T6hYNAnPtivxVWF1iVo5UlNeaJWJcb_i4XKEOsu8U2iIqj0RSPg9H2lau1LvoHMyrNXCDRkFZpyaXLbrvQ0z92Iqf5GFe-Uypl4HpwSfHJokq7ug94pNnaMoMVezR6t_QZ4wNH-U2DN5_IdiG1ZBXnTwrF7ZM7KFCZlrQFtAR9pjLrVaeiYps51MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28422" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28421">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns0FVT_o7S8CXVryWHS1GR9bhFWASctANWTTHo6hA8ASQLgL6ABkBknXDxQMwLp8HZ2irbK5U4WOnPJGlr6n6t8jjc-OOGiGbDqDDQbiXC34lBGSJFEsri5OzslLZ5knrYi29ErP8cFH07dxIvgbeQcBo8MQPPoIxgF-J9ik99hyimjBGwb9bUe9JXvCHM6skbLFfC0IPLWh-ybJmcea4nAnqYy3HFXyyLifVgx3Zrp2-nLd7EZgGWQHmHP2JqjKwsRN4Mlfw3lm5rLSpvuarULihgbxTO2hIVTBzwr1yoEdr33EgkB4dPEG89qx55NgQWtAy5VsqgozBHAlddgQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28421" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28420">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9248dbd6b.mp4?token=nAYB6b0Tp1mYN4kpFlUej6Ll3SditCcdmHr9m6wNbwH2YBQOki5vmK0CYp49KAS5SM_px-oplXegkvbf6NvFHEuKeRH-71ezRjjKo24iaF1DM7jF3D8cB_ALgMskTLqbLze7onCz31d-eq6j3gqGHT3LpoRe6zHO4h0ClxKqylKrOUGniDl7n1NywORkqpqHyKEbYegCozeQhtSjlqFA1ZLtUOOUQPidBHcB0K2hWUBGJKrSsPpiwdyeeGy0riG2Vva09ZDG70kZN2N6IBNcUcitXB7jo79cOlgRnCnVyBnjtWnnLAuMzAEMMmGvAvqgD_DHEnkQ19aEuah4oFePFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9248dbd6b.mp4?token=nAYB6b0Tp1mYN4kpFlUej6Ll3SditCcdmHr9m6wNbwH2YBQOki5vmK0CYp49KAS5SM_px-oplXegkvbf6NvFHEuKeRH-71ezRjjKo24iaF1DM7jF3D8cB_ALgMskTLqbLze7onCz31d-eq6j3gqGHT3LpoRe6zHO4h0ClxKqylKrOUGniDl7n1NywORkqpqHyKEbYegCozeQhtSjlqFA1ZLtUOOUQPidBHcB0K2hWUBGJKrSsPpiwdyeeGy0riG2Vva09ZDG70kZN2N6IBNcUcitXB7jo79cOlgRnCnVyBnjtWnnLAuMzAEMMmGvAvqgD_DHEnkQ19aEuah4oFePFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🟢
گل‌های‌دیدارامشب‌خیبر خرم‌آباد - مس؛ بازی یک یک شد؛ مسعود محبی بایک‌ضربه سر دیدنی برای خیبر گلزنی کرد و نیک نفس هم با شوت دیدنی اش روی حرکت انفرادی‌اش گل مساوی رو به خیبر زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28420" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28419">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb30f0066.mp4?token=bGA0ejIlQs_P-jCYkOwinGcfzBMdr7eqIkRmJzSybV6ks1CQEW-Y7qEXK9hvr1Kp3OHBTNAj1D0w5po-LCepXp8qVL64ecrlODz0ZP-ninwu-KliVx2HAJ0WpdQLX-tX6gIdhvoknpeBCK-DOmDN4OPE3UiB3Gl_M3HxQsm9QLZNM994hl9y0xXFLVmubKUit53BLim9xPRh1RrUB3ajPiedNQgjoG1wrYl3bCctZK1rgSsqOVtZFzSFRcH3FnSFTB5oRcTNyz1jcwLzd9lxdDmtlYsdpazD5UESMSGx7ox4-874IckeHq5Wvi2Ge3c7k0tzOxF0gEoVx39Ktz0wzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb30f0066.mp4?token=bGA0ejIlQs_P-jCYkOwinGcfzBMdr7eqIkRmJzSybV6ks1CQEW-Y7qEXK9hvr1Kp3OHBTNAj1D0w5po-LCepXp8qVL64ecrlODz0ZP-ninwu-KliVx2HAJ0WpdQLX-tX6gIdhvoknpeBCK-DOmDN4OPE3UiB3Gl_M3HxQsm9QLZNM994hl9y0xXFLVmubKUit53BLim9xPRh1RrUB3ajPiedNQgjoG1wrYl3bCctZK1rgSsqOVtZFzSFRcH3FnSFTB5oRcTNyz1jcwLzd9lxdDmtlYsdpazD5UESMSGx7ox4-874IckeHq5Wvi2Ge3c7k0tzOxF0gEoVx39Ktz0wzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهدی گودرزی ستاره جدید گل‌گهر: مذاکراتی با باشگاه استقلال داشتم اما به دلیل بسته بودن پنجره باشگاه استقلال نمیتونستم با این تیم قرارداد ببندم. آقا سید همیشه به من لطف دارند بله با من تماس گرفتند و درخواست کردن که به گل گهر بروم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28419" target="_blank">📅 21:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28418">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=dfFtyRoB1B-dtyeNZl5PTZKurjWWIzZNh-sOz0HZugdYGMvgzqC9yj0RzNx21FaZFjdzZhiwjcJDqBCeGAL9qyZ6HVinNJoCNCLChJHpJzQ7e-rJnCCUIABa-e2vFGIfQJ5aNFTbOO8IFgf0RyNlRhrn3z7ynIrcYsfK2DDoNbsxZemiKHUKDH2klL5fVMD_0YRZRcZm59aCbt8PahXUJ_OsRKUJ3BmrUo0qynwanmqrLfz7XjiBLtuJ3r5Sko0BbJhS6bqoaOy4Ci4b4HtorVElJ9EL7DM61mybsHtbXYSQa2SNc28p15Nbq7QaT8p8tphsUc-szsFNaccbZisDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=dfFtyRoB1B-dtyeNZl5PTZKurjWWIzZNh-sOz0HZugdYGMvgzqC9yj0RzNx21FaZFjdzZhiwjcJDqBCeGAL9qyZ6HVinNJoCNCLChJHpJzQ7e-rJnCCUIABa-e2vFGIfQJ5aNFTbOO8IFgf0RyNlRhrn3z7ynIrcYsfK2DDoNbsxZemiKHUKDH2klL5fVMD_0YRZRcZm59aCbt8PahXUJ_OsRKUJ3BmrUo0qynwanmqrLfz7XjiBLtuJ3r5Sko0BbJhS6bqoaOy4Ci4b4HtorVElJ9EL7DM61mybsHtbXYSQa2SNc28p15Nbq7QaT8p8tphsUc-szsFNaccbZisDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسینی فر مدافع ذوب آهن در بازی امشب مقابل مس شهر بابک به این شکل تماشایی دروازه خودی رو باز کرد؛ جدول آنلاین هم پست ریپلای شده ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28418" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28417">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQjrsT_a0lE1I3sbSEPigjO7KH2wm8Gx49nWOuNZRpQ7oPZQOCq4M4MwTCYY2jxtRR56uhzzMpI34QIDq5hvmHEVrZ7vROMUqSUQ4yUGKvlIxUs2iv87WK5bnXnaqnf8zEH9y32rafwTK6bHAOVzALjBhRz42Ry7yP103iuBRXUhZwb9G4EcGnJ6JpPhr8ssMV3BMaeTCLnRnMn-kY9qI1FsCONsN82c6m04tKT-qfkztGjFcTyQSkLsII9dFShDih5HbWVsnN4cTBj3XHrYEjeny6kPOke6jhSTHZAQ15iF36FB-6YHUluCWHh_wIZR5wZcO28J9u1MBXDsqOwe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28417" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28416">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87affc8d0d.mp4?token=rUqlxPGPSEXS0T7Jp_nXHQ0hAPHv5-Ju-MZ0N4VVkzfb2jCIj4VnxpokfwRmUb-KXWADp_VpCWRoevYzWtO93PgZYDwLGB9wqZJqU3mjwMlKKxNleCR94Dge45fROzmtxqMMk8idmBr6QGFvC4A9ort56kL3QhhuUuU8zQ54YQ2bsQXDm5Hv-HFYqqYl57YuXkIFm8wUSF_aO7sW8bJ6llPeF1xZ583HeKAJSjy_Z8aqJTiNKDzKoSNWZd8N0zMoMQB2dafaIpLJvZiIA_QY93UCEawhpSfJjFf23lTL01oQhlgetC0DPJqenpBrbIgWDl2gp3GLAFe6OE3mv7sE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87affc8d0d.mp4?token=rUqlxPGPSEXS0T7Jp_nXHQ0hAPHv5-Ju-MZ0N4VVkzfb2jCIj4VnxpokfwRmUb-KXWADp_VpCWRoevYzWtO93PgZYDwLGB9wqZJqU3mjwMlKKxNleCR94Dge45fROzmtxqMMk8idmBr6QGFvC4A9ort56kL3QhhuUuU8zQ54YQ2bsQXDm5Hv-HFYqqYl57YuXkIFm8wUSF_aO7sW8bJ6llPeF1xZ583HeKAJSjy_Z8aqJTiNKDzKoSNWZd8N0zMoMQB2dafaIpLJvZiIA_QY93UCEawhpSfJjFf23lTL01oQhlgetC0DPJqenpBrbIgWDl2gp3GLAFe6OE3mv7sE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول آنلاین رقابت‌های لیگ برتر بعد از پیروزی تراکتور مقابل پرسپولیس در هفته سوم لیگ برتر.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28416" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28415">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ZWNjP-6pTDfzHRC9sCThJdfM7rM3TwOA_9vYMoNIxtPHoDvEqcTfzoSWH8UQ8TME7IoLySvfcbNitc-MSgtvxgBCo_YW0unMb9gV4kHbZrfRdYCUTGOVmWZ-Eu_DoK8-mVCpuvTSdhVTyjylXkM4mZOdSLBYpodvzTCPa6SrltGefcIIgDAUPdV-3_Q-7i1tVhSx3LirgYe0uUqLce3SN9IgPzNbugf2s2RAfaPBJwnD0IxPZm4i9-hm2DIZPX1N-f4byYiD9HAilROSB_68kgvJh8hI6AO1rJVbdSOVPt7M5d7-0Kf54HGN33xlboWfMkCT5Db39LRgPrmFJWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28415" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28414">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGGDWjThShntWqNvzRzM7tUtu0woQGP3a40iLpOnmBLtT4igVz1JQO3AL9QGrThvvjaItNpRk2cg_FVG7wIpbqSc_dcojgyorm0GdQMlZeBJaTe1HYdfv5q3DCpwmKKQkqzoZ_uuA8qjqhyhWWz8iu9oesAAukMFeEPank_CbsJMdEmWFxiJ_ZuHCbFox64cw-LZSgO7tcBd7-PK6A6zoyl9LjAbt_tS-DcyVApSlbpgOM3a0fI5TQrJVKLWV4DGKertUjeIhJhMsHWtoEKdBnnPTtgOuOjUIZwZ9mMAgC8dYMzPMLdGjZMth5lwZaAN1cKsz3x4R6lde0i5QDeJ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28414" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28413">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxT6ci6YAdG6YF1Ztm7rZMNlESIOIcpawJ4_U1KgGHWvIZWAqgoCDlL42Q6odGN1IsTcATPuQeluN5HpBuh9DepJcpG3hRtpE-h2XFj5-EwNoS_3yrPYTJh_AYwjL1StYHxoOPWuhwqFZjFAuyD73GgD83JinaRUrTSyqiVBijLf8w_xbYBjat847i4YVM9saQla7jRFaoRhLcRTZv1U18aTjYewKPId3C-EmXecI-D1yX1UntgXe0d0hm7UVgcOhPPaYaqAGV5YYHcaxqVxu8Pvuu7GkaPWwmZScI0v3Cx9pNdutuXQH0nGacNDbovdaa-mN4DVtxDC6x5VozRnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28413" target="_blank">📅 20:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28412">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP3S_qNxRD1eD20Clzr9FezfyUlfIXPjfEeokPSpk_El8Z3C0LE8bs-FqLD40e-rBTMs-Wz3IgRJVsOV4Z11i-KLIFxTcLEW7vgZp_ngcD-_ZEKw39VrEeo_314IG0zDHBNeHrxMifV2swwZRv2Uk7zACmT4Ciim7G09Me3Py2BuJvb4Ydn4rPlrjwztF8LalzW7dgh_FlBuTA1Jmxfk8Ok7oY-dwvQ9AAodNmslzSBi_YHSUZoYNK2-sQvzy4id00EEN46Jalxcn1-NQwbkY2YWlPaiXAiqgklaVFG9DUlTRizsselM57YviexD-nGoznsv2cXN5dOmHjhn8xbJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28412" target="_blank">📅 20:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28411">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8596f7941.mp4?token=lzjxfvPLY7Y3pSadaZqnhTkBUzEo5W60EPJe2auMrckfZw9xSGHU9A7Re213sWX4WHC5e6XkVzx-YJFY8F0upcEOkx01Ta9wrywt2YQlWZ1j7b7P8l5egri0LqHpc74ibDqSwrsa2sXkQvvoY1f6RFTWKwsnJNKFSSINCSJgR50cNJsZOWAbtjT7sORmZxapPpmq4CQG-0dRZPxskffCrnWvVAVjJ-hcYLn4hjxsja0dQpyuCtHBltaOLoN1yFbnZle985YWC9Sky_8R63cyEbHThD3q_aeiQMo87xfq546mPShSDlmb_0ZEiEhCMU4wh-LdgFBQxbWkZ_X5ORwpBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8596f7941.mp4?token=lzjxfvPLY7Y3pSadaZqnhTkBUzEo5W60EPJe2auMrckfZw9xSGHU9A7Re213sWX4WHC5e6XkVzx-YJFY8F0upcEOkx01Ta9wrywt2YQlWZ1j7b7P8l5egri0LqHpc74ibDqSwrsa2sXkQvvoY1f6RFTWKwsnJNKFSSINCSJgR50cNJsZOWAbtjT7sORmZxapPpmq4CQG-0dRZPxskffCrnWvVAVjJ-hcYLn4hjxsja0dQpyuCtHBltaOLoN1yFbnZle985YWC9Sky_8R63cyEbHThD3q_aeiQMo87xfq546mPShSDlmb_0ZEiEhCMU4wh-LdgFBQxbWkZ_X5ORwpBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28411" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28410">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130f6f7f0d.mp4?token=e0OX3o2UOXfGyrxk-Juq54oMfYASTbPGsworRSoQHkChn2S-JVLhNrFj6bqCoAlpMZoNSr--8KTDmd3gZIIQa2-m7MxqPwKqWlPM4zdiPw-jyciScAoZA_Z8mn_usXpudyBcN_v2ByqB-qiX9JUHEmrTTVsSe33JOM6ZaLNch_2YlSjJgfXJTVBgn9Czjunja9ggRgOhBootKR6Qrlr88zoq3HJ_TSZhoiXCNsYFZQ4tYPnQBDiKjsG6NvcPB33HDYi-Xdge3mRAqr0_FB4x2QtutAxw7OuS3GqVezFoEljrtJrxdy8cXGi873KcAJ-Wjz8y5SqYJ8R6IniDZw7KcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130f6f7f0d.mp4?token=e0OX3o2UOXfGyrxk-Juq54oMfYASTbPGsworRSoQHkChn2S-JVLhNrFj6bqCoAlpMZoNSr--8KTDmd3gZIIQa2-m7MxqPwKqWlPM4zdiPw-jyciScAoZA_Z8mn_usXpudyBcN_v2ByqB-qiX9JUHEmrTTVsSe33JOM6ZaLNch_2YlSjJgfXJTVBgn9Czjunja9ggRgOhBootKR6Qrlr88zoq3HJ_TSZhoiXCNsYFZQ4tYPnQBDiKjsG6NvcPB33HDYi-Xdge3mRAqr0_FB4x2QtutAxw7OuS3GqVezFoEljrtJrxdy8cXGi873KcAJ-Wjz8y5SqYJ8R6IniDZw7KcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این صحبت های جواد خیابانی روی انتن زنده صداوسیما که سال گذشته به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28410" target="_blank">📅 20:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28409">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bd5f94c2.mp4?token=Y2QdxJPs08qHgAd4YYOcbLKehkd7e9rBkk6jBwc5RS6hrHZFOKlG4JYbefGfGviJ3cHFE35S-OtXlKJz656DWi7vtF205lYEmgBx8otHLMmNAuB0LPSffpMBHZn1mHl-cpgWcDdyAFWmrJZM8FB9fxzSzEHAkWH48o4xvVa0Fagicujs4yV9mVHRdNU95iOMB412-QgqbsztHdOQk0C95r6S9qnfHdSPGDuRWFrvLULGYUSV46uulpeJeVfaN0vdvufucbMM60B6dbXauqjPxXc5p1tpdf4m8laxtQexD6kf0BN0P2YxmNQCE_M7UNYGwCG2x4DZiwDcI5wEYlA_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bd5f94c2.mp4?token=Y2QdxJPs08qHgAd4YYOcbLKehkd7e9rBkk6jBwc5RS6hrHZFOKlG4JYbefGfGviJ3cHFE35S-OtXlKJz656DWi7vtF205lYEmgBx8otHLMmNAuB0LPSffpMBHZn1mHl-cpgWcDdyAFWmrJZM8FB9fxzSzEHAkWH48o4xvVa0Fagicujs4yV9mVHRdNU95iOMB412-QgqbsztHdOQk0C95r6S9qnfHdSPGDuRWFrvLULGYUSV46uulpeJeVfaN0vdvufucbMM60B6dbXauqjPxXc5p1tpdf4m8laxtQexD6kf0BN0P2YxmNQCE_M7UNYGwCG2x4DZiwDcI5wEYlA_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28409" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28408">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7_AzI-YrHLHNPKEw-3N6mqrWFKPf5iC787p9HtjI-8rrL8XWSGAIlu7XwStomvqtNMH3zXTGCNGzDoTKabqZmJh1h5P5KcZ1CJv6xVpx960W4EDxScsqFwzQF77KEnchPhtu4ifVSuKpgN9lBTi11liLqPtWbc0t4bpyzvDIIZccMzLNmh5wn5dgbs03HcNy1GhOBcY5sK53M20Npb_gkVJNNG9agKM0qrySUN4Qb9nQxiR3Tl3qyOX3uWZ0SkfzTN3z_8iqdB8W-QJTAO8F9F_NhqVaumClzwsxuqpSznP_9fMU7HHb8P5CKQi4wBiYLT6yvfpf_lQY2605SBq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی ۱۵ میلیون یورو؛ آکه ۸ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28408" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28407">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2y4vJdCHc-Yxusr2tFVqpmZEfJ7V5860GdAUnFWqflBEcOLhcavMqhdjjK3QsMpMlErYGG8DoH748qXf-eRzTperH8F3x7fdqYkmhcaH4T2Bz2KulYzodDlTUFx1UbG9gB-mmnl-Lek3XCxczs3iRAU8pUdTAYIVZg8NHV-RuIPtAVvWzUxAdwUkcGNkj2qNz7sVS98BwJs6x3WkicFypy6RRRp1haBmxUQjGiERQLfw2aVVrj3Ygtit395RubLIfviYW0K6o3Z8Wdtn4dx5Txw3NkUI1pL3MMf-Te3qQeGo_z2mivUccZWpP3AxC6ArLLaNtxIGtX5s6EuZvrLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔴
🔴
شماتیک‌ ترکیب دو تیم پرسپولیس و تراکتور برای دیدار حساس امروز؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28407" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28406">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKqazKyWpGW99q1_V9NbdXInJt7p85AYOqGs7ERCv__RHU17a0pREEuT9rfXHAXh7FqfN44-metPNnEF1UFQMeR8lS9O926UFaBeHS8rorZudsgiKccHHYgFtM5a3JI8zdHklaF5jGPYhJWbLAlyR2VFI56xY_Yem0jcJ9eOArbijyxa9os0_EnM-0vVKNK8Rv2En9A08sfEvgWrJV6Vr7O-ZtNth86t0I25Z14eva0VldTN2dKZ8itkHsv8Z52LZq1tj7OnoMANQRYb0vFvdteW0Mzo_qMHl9pEXT3Xvwd7nzzI4-Ormxcr6NlX7ltFyI-2E5jZdUZeqPZVVmLq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال طی روزهای آینده 70 میلیارد تومان به باشگاه ملوان انزلی پرداخت خواهد کرد و مدیریت این باشگاه هم رضایت نامه بهشتی رو برای آبی‌ها صادر خواهد کرد. تمام توافقات لازم بین طرفین انجام شده. بهشتی تا نیم فصد قرضی در باشگاه…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28406" target="_blank">📅 18:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28405">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NERw0dZqq4LxiE1bg5TuDRxn2MwFT-XODh3EBKnYZj7yfdXLnuYZ553cPg_Qlt5GPGGhHQDceYcadmEjn_OiunFK9SUPWtDPOy2KYccTwy5HlW_h-R-_VTv7LUdAI_7zKI_BhpagRjhqCVzUUDgkNlCKjwJHV1PfxSroL-MmQs5KxICYru5gW20xAW5FpCQak-ErS4oB2eMqUEkLXmcRKGNGbTfrgG7XWklfoNpr3hLx74n17x0TlejMmRMvStCEHwLtdnzEbc9QguyrnbV9kIPfULmdkbapnGqCcPZa4PaLq6_ndG4IYcvk99tvunk60Gg9J95blWYLzmY48iJaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیاناتوسط سازمان لیگ
🔵
بااعلام‌رسمی‌سخنگوی سازمان لیگ؛ یاسر آسانی یک قرارداد دوساله تو سازمان لیگ داره و الانم داره سال دومش روسپری‌میکنه و قرارداد جدیدی منعقد نشده بنابراین هیچ مشکلی در این باره وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28405" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28404">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNILLhO27Scw_ielWBxz7t7iSqqXrnoP0obc2u48mNR-DZL0QxWdt_pCrEqfy1AOxhhoCxHxb6f2CN3Ie1Wj1xAdZD_HkFfG8y_X5s0QamOM08a-h2aXEZSFc2VkzC27zyqthSHBNdqox-Uz73gjECkEiSk7eucMpDaqVSseT4KneMHUFziSfOs2YPvWrduQcKsiOdoQBcqqoivKEGAGWkT_5Lnmy8QjQIlF6nX1v047qAjpMXXNs5rZE0BbPHTIfaL24zn9rILw1bU5NLhB481MQv93J_0wARVVZCGwo0cFJdYDSbUyj9KdNEo4W5MgOwkUkyiINUYSfQavMHoQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آمارتارتارسرمربی‌پرسپولیس درتقابل‌هایش با تراکتور: 25 مسابقه، 13 شکست، 10 مساوی، 2 برد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28404" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28403">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-01NUtLWuPHqB0ejRxbLrtrRNwCQS2wUfL4Wm_OMBc38WwH91E_O6Mmsn4ehue5dVAnqvtbShbyD74dCmxorWPizXm9YXmgkMa-nA6phNR3BkeuSn1hh995-wogkkrToeN7zXWFdUqLk1PGAtFmljzoGOuIPMORGoDr4Lcl9R80CZvHJ1HKoOvx_QMtJnOZaUeaTrRysM4FDxVpPjQ5dI88Rg_6RjyD-J4uQqTzzlF-RRvN5YqoFCSrOE4b5IqTYzMlNnGrylvHxFATRUx3wq5FI2c9hhrNEXF-MF0IXIn8-JkyfbVzyTX81WXHQ13rPSKVQB4uge6aDdk5pl677Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28403" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28402">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRv5Ruy2p6l4pDGO08ZDMEzmseKh2wSLOgRQjHnC13y82QcSdse9ubFkgbsjU03eNkrWpJ7jFn93uC13Vkc58Ni__iyKs4Gj1gvL1YIhEDrFSH5VeNsN1augVSfa8-A7P4Nr-Fy-j9xCRTppbQ6RHcf6uNRRnKLESqz5h39uYcR8AiZZAN6_KtcgCroG6ramiNn32rHsa-a6wy_27TcsXLWlD9nzY1SMNGEIjm4lgsqG-QLb2C3bLpc-VAyPoqZB3Kf3zsuZFW2GZp_Q2FVUz79p-9_EZmtbbU-MxPZCX6bMwBDepaKzTW8bY5ZfsRdjJYQfk81yPGNHyTsNoLhC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۲۰۰ میلیون وام بگیر فوری!
🔥
‼️
با اسنپ‌پی می‌تونی بدون نیاز به ضامن و فقط با یه برگ چک صیادی تا ۲۰۰ میلیون تومن وام بگیری و تو اقساط بلند مدت تا ۲۴ ماه پرداخت کنی
😎
تا ۶ شهریور ۲۰٪ هم تخفیف اشتراک داری
🤩
پس همین حالا از لینک زیر وامت رو بگیر:
👇🏻
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28402" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqQEdChxvW8xEgBW3AfVjUyRIivqEGIQcEuPHnbwk-coQ_xkY1nprFJ2PWkCycK0am3RmPBDjKlBb6I0oWbJ2fAhF7hr1yHFecGnxW9fgCEsWaT9Ak8yBHkyydCub501TCDytWHpsN8NZyJBYEG3suTNlAOwHAEoeWbc6wT3BLBDlXzUdwChOiPsShGzThOPEaJnX4NFx4u_wnRLM5znEMBh_eY9TN0RnIMx406O1cf5t7gRlFH_zxUk4DPfcw7X35qpPpqpRAXyI86mBn2nh-X6hD3l2O6J5wb1CNqCdHALTfRcbO315os1Rw5ApfpbpgDSOWCGax7AgRzW4hlVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLe8KsMwOkDZlFx0S3E34ZAytL0UPXarfIMfFbYyFha01cSImqLpkzxPUIfhjIlSePWeF6TsBnE7MOz1get8hAXGaczkUIn7BkGBiBCOPKULFzRDx3DCzPMGHJzQp5a99SSbaEyLFyPZqUBE5qkx9WGr1oe4p_WnPMmXujpVUN9G4e1tHpvCam1DX4WlY0oSkg9ITEyS1PGuhoUM9PGhj9gxDgdN9Zz5ujZauCtIG7RzIbZ7VmRxWJMTw0BVBm4zYkDVQsSvRQpB6wCjeoqVJ5yuJenk37RSywp7QxPQ-EQoLGZyq-CNud7lmX46NIqe8-hyaKRqbXMh-y7zFbiBoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب رسمی تراکتور برای دیدار حساس امشب مقابل پرسپولیسِ مهدی تارتار!
🔴
علیرضابیرانوند،شجاع‌خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28400" target="_blank">📅 17:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s39ORoxwWykrbnzmJwW0Z363DYfjXfAh-_uihlkYyepUKSw_-uCBOrIFcVT9eRO2qUe-cn8PpdlKI0cYB2Gf4pF9CZC7e7iZdbsj9ViScITge7UVmIUZZENpmKc5RqWtzHDejd9cf6EWIu9GFV_NHVD7oaKyzCveWuIYna5mL8fkPfVIYuEYrPi1SVZq_GaNU5A8bxIRJYFEjpl7eg8I4rGps6g6_Hys-VEhny9sLR4Jii5Jvh_Qj3zD88Hn0c3biRJAXYWrCLk8AxV4clYhFVfBtZCK54OAfb5f3TqnYOv5Ai2oaHVVmB-BFTctRWtBAUNLUgIUVLZ-92vCFNR42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28399" target="_blank">📅 17:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfu0sstxDHIzZkHyj-EzktyXLB-KmnyFuc4KhJNKafR93ZVLNisGwg4Ybsf9-xT0u1Z5Y52zol7V0Gjyn1Plqahu8mJKXElhu-IZI_fdH0aslVr97DPEyfFDrBuOxNdZKOmbw28BoKemYHAx6hOTZr1g3a_t1cszVIotXuFNF3tiQDLL-9SS1GLnX-xCvt3Qt0qKfwBGlIMfhsrKj-4X05glCCADUjWn5TKAqeW5smQ7jhNLF8lDL53X5AD-HE0znsiq1X360WpylKCb-grJ9KanlhED4G-5KpKlSaf4KcVmlVj5TGL6rZ2HEsTCssFIhxHqitOQnl3bh_beP5k62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر؛ ترکیب‌رسمی تیم پرسپولیس برای دیدار حساس مقابل تراکتور؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28398" target="_blank">📅 17:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp-kQt_-W9qJlPjoAL0gY0LPWs_n9iyYGNP3AxRp45BRUbLNuoWl1M_ZXESzAzecEFZwgByhZ5BybpcwTSSfJtHggHC4_PENN8irl2lFQ1xvh1pulm0izGoJF6go0SLLIa7ytdzVEAK8KTbktyzMASkV03bSoHqHK3_A_hu8v62gOF7DO4fQKsgVqAd10gFVx9p_cmrJl-meNNL0_Q6L2yBxocLNKk2RMrLRgRbTvIMwJ_QKBhk-tdY6Hhn08-qE45koSbjiThhA5yVaIPOLB4fIXORp-YHzM5kLtvikLfEi0whvFE4c_AXCSrxYwl1z_vimsXQVnjxK14lXjTM2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب رسمی تراکتور برای دیدار حساس امشب مقابل پرسپولیسِ مهدی تارتار!
🔴
علیرضابیرانوند،شجاع‌خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28397" target="_blank">📅 17:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBt9fHqkPnWVKqfAkh1e7ksV3eSGX5X3FszemTIelLcJFHF34QSWjLv6ySvo0zbyDAA7fgfE5yYximfvye1uFizhzijY7PJYyHVBw59goPrHDePWPo8v1P4R8DVILtpcwInNSiJfPHmIEVR5LMZZSXKzsMhzUReeGLMD5bjIzQgeULEsn3PrZX__LBR63bO4nyJRvqLQA5d5rgnUh5sN8xJP0_C1hGBt24re4LcVJi0-Md99wCRBZ4XJKPfz2L08r835XZqIzlMWykKyonCb63DKliVg_nZii5lPovGkzPEqp3jvKEsKylhhii0FfcxestCg4Y7tTjl8m_VHxmVtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌هااز تبریز؛ تیم جوادنکونام فردا با این ترکیب بمصاف پرسپولیس مهدی تارتار خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28396" target="_blank">📅 17:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlNFLaLAt2itIFO97lofbOBUqxUK0m5ENdAbCzWk99wEEOc4soIm9dtudb2aq-S9GIXzsF2wQ84R6f2esCS0Gn5Su1_4TIvfAfx8mXJ_e6gYKn6sSm28IAMCVB6QVmtiRLQOsEfaWtleGSz5hK4bFhTHkIzQGGJmMDsMFwZ4PIymQDX8Q37gyo9NDgmUleB2ASJJJHRKpsbeCP85O-Q87Bxqcso2ByZqMqyOFrhSI-eh2KX_fTCaw6CvJgnwNTm8S0stEAbAemeTznYwq5Susop3IIc0OiE2wooq5hE6SGIkwxzoa4DmN8Aw6tzhBeDMzTqDqdNppIT-fplPyxwwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28395" target="_blank">📅 16:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG5AaAv39ylkAQ7871F-Mlh0Ix-Ud5XAOg1gNKGt1TlhUwfAtr5x6rSJI4jgeqz1ksbRUJgA8qP3h704npRzfYATXTFL1FIU2kwkcMrNIi-idjqKhD72IYECLiFwStmV3Nnn9JSG2V5cbIy3fHGKMek1TmhX3KYJTAHrVOiWL7XMLN6gBC5tCrjVRuqcje4lCIkWzN__rkipJNuUHxX4N-EbaWCUqhX1xXh0FYFOLRvSvY_0hsZyg0penaoRBzm8Q0uSVdd19thdthBzvedREmlmMaGQyKIagagZX74hTKLKO5pjm7M3N0Hr2rnVJBQob5wlehcQxGrNlXQUAIylYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28394" target="_blank">📅 16:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28392">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIOzZrhw5DlF6FhCY0ytenzQ5ogBIjt8v31sdA-nSReipWaWBNeIi5zh6rmiqgY0Abm0REIf2rhGfx-SqZQQ1a1kI213KMiyBFjIqal3aY7_FOIp2Xc1ucyj9HMynZucZ2QmiSiBJBAWuuqFB71WxorR5pwn1Hs6ucGUo9NkIDwzTjmOrgFr1OFldGzOTU7_vRdyMXafuyRl8r8bSWb0s2DvMlCTvvetcFO9-45_qzcDCvzDnDUp512IMHr8papgbWAF6boFT7YvGCpEZIZ4bFpgzX36gTfZe5V7gHcb8-G-9dUiGiBrlA1IsLxD7KgqspP7fB8_BzYICyIJa9GASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
به مناسبت دیدار حساس امشب؛ تمام تقابل‌های جوادنکونام باپرسپولیس درتمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28392" target="_blank">📅 16:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28391">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJvuwoLDm8zl_BCJudBEQCD3LdI-PuMUBjh32i1r4SU__MMTdtLE-GV00O_AL2rI4V-vLpW8-fCs2IUXUMla_W5Wm3dYxS4c3BMylcEgp-zWwbOH1MBD8bGxeHsa9CNyynixn6q_GtaMAB6ETQsaFLLKtd8h-U_fyYweBF4y5phZ3d399Eolh141Zb7-othq_x9gu0N4wsodS0ASHqWwfk5akjJR1fy3Fkwtbxpdx_0r393mnj-4FjedrkeEUSIx7j7wefnt7hYpdtTwqrK6VIj9LTroIO5cAom60nckp5vYsf_7aeheb9BacT8iX0YVKmwMFLFmG4VTR-F-lNviXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌تراکتور به همراه نساجی، فولاد و استقلال‌مجموعا ۱۲ بارمقابل پرسپولیس قرار گرفته و آمار دو برد، چهار تساوی و ۶ باخت را دارد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28391" target="_blank">📅 16:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j084czcqDT7oi-Xc07SpT_oQ206CBY-A4VgC_dED2UtDT-zHH1bSV97P7bpKt5AfX3A3CgeRrBYxDPCwDclU02KT-uA8o-fbcVWufCiYhzgehEFNl5Zj5b3SEOZwrByL4Dohr8aS3sbLAGxX7yYIbHZxAiZ-UnVNAzJKQle1V-7f8aSR5a-SgUteRRZz9-QV_W6b_3mIBifcdh76ACkvom7MZeanumWvRypyMKzPWlVaZ7YGhOEi8DDoeySCwe4rAuw8-fV9BWC8GvG-Ki9evkvBRYmXDkvzNtuH-Xn5X_HOfNDDz-Huw_eOuaiG1cRaYUulcfGB8BDKPbl0jjX5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|اسپورت: فلیک به شدت علاقمند به‌جذب سرهو گیراسی مهاجم29ساله تیم دورتمونده. سران بارسا قصد دارند که در ژانویه مذاکرات خود را با مدیران دورتموند آغاز کنند. گیراسی بند فسخ 50 میلیون یورویی در قراردادش گنجانده شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28390" target="_blank">📅 15:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPbSR8pRMXgG8AaQ7NPzM7olcQ6OQq7reiE4VkDujU9vk029Hgy61PBe0WveRnwzRa0Jw-vASiNYF4J-uFZPITUbV_afapc53ubl5nxZSPHK5Y50WB55Bn0L0iOnOOSkpT9FIjDZ58yh3D6b6mcznCRwkG_rkCH7-lpEBwLosqioZD1izv1aDhZWqhkDB760Ybr1EDF2I7I4v2YoQYyBTar9Ixna1jc9n6c8HnBdiBRy4zWUG_jQENwki6ZExss02n2CRWobbwwOfRqnPygNeeoo7lBxTA6OmmKex23RfPR0pifaoLAWg06G13wqB2oIE2RdSmvPomGHuHo2w06iRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رستم‌آشورماتف مدافع29ساله‌استقلال که در بازی شب‌گذشته‌مقابل‌سپاهان دچار مصدومیت جزئی شد بااعلام‌پزشکان‌این‌باشگاه هیچ مشکلی برای دیدار روز جمعه با فولاد در خوزستان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28389" target="_blank">📅 15:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjRT6cmuTbip7yZSMs2KR9nNjBNaRQ7AUeOAdDsFdNlTbZpeiML8rJGX3N-5OkuL_evNQI3Dmms3dqeHsgVD2zHMJ3l0UVY54apRJJWbv98MBXBtU-XZwyQYfv5CGimBJKCLAQIo7jbJH2uqskrJapCBP9Oca3kuiSZJHp3Z23DtHHjJGbbjw6nZQ_lwo6fwHBFXmHAG-ARGjx5vxxjbZ5vvnDMNi8uVZJuDdm6VtmaERP9PpL8PBw5dyQS3w1bZQUpB4bfWXToxX21ifOkaIiM3LGu21-yXXwuPZNffDVEonUVnu3OChrLazGOAGud6QKA4152GNkSICzJPs1m4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایشون خبرنگار باشگاه الوصل هستند که از این به بعد در پایان هر بازی این تیم در لیگ با مهدی طارمی ستاره قناری‌ها مصاحبه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28388" target="_blank">📅 14:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuuqSS8V4hsf5LlocNnkrsywf9-USKpHIj_w6nUZU3gS5xX-1hkjRoy3JWpqCU5TjB1ahY-6IcfccABIgHociAoB9CoMFYcafVyl7xEnIUm1XirGqDY2LRgu3npA9-pFv40syxWdTVWoqPtQQF3s21QS4Cns0LnCsytv7VkOzJYxu2NxCaKnaCw0RW-u94Yuy30CSfZvVBtqQ9h2tn7vwd4uE7jhsCazidqUwQWzRW-UM-AfHTB9hjTK35UvEzMkL7oQJtqd3iqY4eX1injRn_oR46pTHRrP4VVObBUaRRfEVo9xd_h9WbUVQYk0QEo-tP7KhbC1e_zmY2nx2qdfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خلاصه‌دیدار تماشایی امشب‌ استقلال
🆚
سپاهان در هفته سوم رقابت های لیگ برتر جام خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28387" target="_blank">📅 14:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4ca0f39b.mp4?token=JpOOk9LsZjUl_-DyTTBYybqKGAGX7c68TI17vsmv5wgIPqBJMgPOAY88MbQkqpduHi8h8VtW3kDQgP9h3TL8tOKyF0xi0--ykDO6_VA0gqFODYyLsudfFlfRg7-e2-sO4vicX0arb4OYEJm_OzXvygrMhhEWi0rDoTtSRDSkWQ4rGH5OW_mclthl7_q4THl8Hbs3wzvn4YFvcyiBzbJCUijxSoTMRwZW9UCQtjmZutjzYrbOjhN4jcWy6toPH64VvhRoZYWuv3bKrqdg3CAv3j6dqZ0YhvL2GKZpgpQK7GobaV38KdNsIXdhk5xOSrVkDQhAW7C90-A9Do9Vm3YPYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4ca0f39b.mp4?token=JpOOk9LsZjUl_-DyTTBYybqKGAGX7c68TI17vsmv5wgIPqBJMgPOAY88MbQkqpduHi8h8VtW3kDQgP9h3TL8tOKyF0xi0--ykDO6_VA0gqFODYyLsudfFlfRg7-e2-sO4vicX0arb4OYEJm_OzXvygrMhhEWi0rDoTtSRDSkWQ4rGH5OW_mclthl7_q4THl8Hbs3wzvn4YFvcyiBzbJCUijxSoTMRwZW9UCQtjmZutjzYrbOjhN4jcWy6toPH64VvhRoZYWuv3bKrqdg3CAv3j6dqZ0YhvL2GKZpgpQK7GobaV38KdNsIXdhk5xOSrVkDQhAW7C90-A9Do9Vm3YPYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال
«مرد سه‌هزار چهره»
به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28386" target="_blank">📅 14:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaS3dIpuJ7eEncJ0SOcJCN7LNsQwkKLqUMy5nOKFpNy1U4Qc5VGeWIs60oUZ2vxH-FIQBbr_ddG8DHkfJf4B6U2RpEk7omHHfw0Dbsy0rvQn3kPfSA2pL5BHb5Oq_MaEOxaI1S5YqpcxlfjhQ0dbM2mjgi-YxsPQUlLxWTONPHlID2mVCF7L1EGbwFJLVzhsyndn_Yh55KNnEbpFZSGimvh4AM86HBmUcU8HMR30RgjvwJOFWjNLdUlEE3Hvn1mLLtPNoAZQatQwDwfkyOXoidHRW6sQDCzOIJZj7tftNF7jkhkNnu5gM4FDAji-2Ei_chBoxRRNffLERvJV_N3Tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته سوم لیگ برتر ایران
🔴
تراکتور
🆚
پرسپولیس
🔴
⏰
ساعت ۱۸:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28385" target="_blank">📅 14:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQBbcEiHDQCHt9xcc2aIo9OK3O2Ocxuwu8RZvQxA1bvvy96_yniVtqps1x3jkO6G3cBOkR8TGOClKAHjZ6WPFvtxo3XfFwvsKn324tGIdYYxQL4a7qnuFxcAuMRvcoxF2INhh6x7bX7qOhprU5OCRSmsxbNZ5vCKJy0s-lf7Q1aiFKPMGCZ5N7TuQBey6mlZdUz_L26VCcDgrmiVwI4b_VUP8x635tG4fMqxoloxYe3Sdq8IBQ225PK8vXJf_lYF07mo3bXsCJIVL4RTXromQw6emyFRoM_mtUzrDDliMMcGQ7IGmPycFGKU3JzPEKgPOEN_q-51oS60-ne09aeZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران:
دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28384" target="_blank">📅 13:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGgXQhtvrhccuFKesIeMjhAcibj_gBH5j1wBqtZK4krJ8Wc90PNiMZdNRJbRR1ipq5gGYd-8fhxJjVSauEVPVKROM9x8jnT6J1bD5nqMPd1oPOtG6unLjl8JUO1UUhOW2c33UlMKANR2vpB0Iua8MjwcVa3EB9CSsL1cBe6MPS87JK5V5lMWj3KBMOIr9gNw6suD6khgD7CzyirbpYU1770Bo1QZWx8_T9eNNr_X5MDCRQFb1VvxYk2PPIlvKMFCJPsR3vSba4fzv3pIR0Q86HIGdLqoqSKpGEVpDlJfLhb5EyUAk2gJwTWb3u1YdKRzWjMZcUSOi2vMBovAAnNUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
عصبانیت شدید هواداران اتلتیکو مادرید از خولیان آلوارز؛ستاره‌آرژانتینی‌اتلتیکو دیشب بعد بازی باویارئال بدون‌توجه به هم‌تیمی‌هاش به رختکن رفت که هواداران اتلتیکو بشدت علیه او شعار دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28383" target="_blank">📅 13:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28381">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC25Laqcpg88daltE3B82RXRTm41fcWp10QgWb2xMfMh2UHkVHMRzf9YffwhXZW6L7gimpBinmsle0G-cFKvqzuS6szizxOQep8QYKVa7OBfOn4puF7rvXKRL0NFcKrNZrcjpDLddyBa5GDfYpaKXi5KgXK45s-AaCmiKUl6VO0-Ny231OcZ9K1GsXqz8IyLETMQlDq4MpVZuYv02NE2PziMR2Ir43GPvCa3dJIcaYfSZmt6nQ8gYnxUxDf-S_hOaVy3SKzVtkyE_AXLkp4Ul3P2Lm8oU4J7FfyIh6yQs9BfFORqgHAj-5u9p3Q0KPFV84rlyIEjA9D7rlHWzTDP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxbEwevLWyn_uXG_fTjupy2TQAQEz9ZB_Oe1-64Bht-wohFISOxkPfD2VvYRN5aMVsj_c_iFhG1ZilHbHapiTPtqx4Mj2RVDZBa7m26lrCh-0-jLnOFv5KjZmgYYrEptPUVTXqiNWNqpkV8ApNzARnYGOZFYlBfE6FdKZk339qphOgNU1jNjKdB3Ff_JpTjee4fzg5zHQGQTXip4607RbLkn_0g7_LUPV9HXhfhxvdyV6m4NWZ0Ns_vrRz958J0kx_2c7Cs41-E48og61WcZC4ytrTGRatvr0RQkK0G7zdvRQ9GhDQULx_7uKIddmCSNgpNUR0rijdgLoK7IrvFJIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
رافینیا ستاره بارسلونا که از ناراحتی خولیان الوارز ستاره‌تیم‌ اتلتیکو خبر داشت دیشب بعد از گلزنی این خوشحالی مختص به آلوارز رو انجام داد و به نوعی از او حمایت کرد تا روحیه اش رو برای ادامه فصل بدست بیاره. آلوارز خیلی دوس داشت بره بارسا اما مدیران اتلتیکو…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28381" target="_blank">📅 13:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28380">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad50390910.mp4?token=Bt-grxW2uZmKTt__sK7VQ-bhNmiZbBqXqhWuotQyTh3WdQwTegPZaXCGidl6tGfQPI1QdlC2y_g-mu6Jr6q4XZ71Ngyxo_wHZXn9n9qvHlUtLch834O9B79F0nnHNpxmqgW54gVrm7SSkRNAQVt0B2TVOAW-FoSb5uObJnX1kvNc9vGxt8u1EL-XnFJiyFRs3Z6yulsp1Oks9BH-EFdyYhleBWpWcQkdhlfeX1NkUFO7NxProM9_6oS9M-dKELWWt9t-YRCA7nHDukmVFyoad4A-TrXnAHXYKJ4eaEQe1LlCfNUNQRYbN-b7jtVlg9PICaR-0yBURxndN4UVSA-r6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad50390910.mp4?token=Bt-grxW2uZmKTt__sK7VQ-bhNmiZbBqXqhWuotQyTh3WdQwTegPZaXCGidl6tGfQPI1QdlC2y_g-mu6Jr6q4XZ71Ngyxo_wHZXn9n9qvHlUtLch834O9B79F0nnHNpxmqgW54gVrm7SSkRNAQVt0B2TVOAW-FoSb5uObJnX1kvNc9vGxt8u1EL-XnFJiyFRs3Z6yulsp1Oks9BH-EFdyYhleBWpWcQkdhlfeX1NkUFO7NxProM9_6oS9M-dKELWWt9t-YRCA7nHDukmVFyoad4A-TrXnAHXYKJ4eaEQe1LlCfNUNQRYbN-b7jtVlg9PICaR-0yBURxndN4UVSA-r6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌ای درحاشیه دیدار شب گذشته استقلال و سپاهان که لحظه‌به‌لحظه داشت عجیب تر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28380" target="_blank">📅 12:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28379">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=PMMyoD7mhHjLdqF3NzXBFa3uZ7LI50r6Khs3CEe2YFmBmzYy4IBZX5EJ8nQyv-DtUjM34oIMv41gvrD5UDQpO3-ZPBX-gZm-_nq8Bxu0_YrLXqe-vBQz7YEsU4tKeSwUJ_ySoofFgdQqFw_yY4FMS4NKtn2Up0QDPK5MH1oe_f2-VX6EksiQ4WlqgaSG7Kp8TZQJK4F4JrE6oSoGoS7pXzWeZhrtlduDEX9h6xLcvaL65SIPMXstG9iYulKKkoZJPMkHimbcu2Wm6X_140zyB7w2mdO4fEYZWPZXoFCoGEMv_eh6-jCPQUmVbw3EMLvOib6TccD4TI3vA2n5lBvkKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=PMMyoD7mhHjLdqF3NzXBFa3uZ7LI50r6Khs3CEe2YFmBmzYy4IBZX5EJ8nQyv-DtUjM34oIMv41gvrD5UDQpO3-ZPBX-gZm-_nq8Bxu0_YrLXqe-vBQz7YEsU4tKeSwUJ_ySoofFgdQqFw_yY4FMS4NKtn2Up0QDPK5MH1oe_f2-VX6EksiQ4WlqgaSG7Kp8TZQJK4F4JrE6oSoGoS7pXzWeZhrtlduDEX9h6xLcvaL65SIPMXstG9iYulKKkoZJPMkHimbcu2Wm6X_140zyB7w2mdO4fEYZWPZXoFCoGEMv_eh6-jCPQUmVbw3EMLvOib6TccD4TI3vA2n5lBvkKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه بکش‌بکشی راه انداختن دیشب بین بازیکنان دو تیم آلومینیوم‌اراک
🆚
شمس‌آذر قزوین! اون یارو تدارکات‌چیه به قصد کشت زد تو سر بازیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28379" target="_blank">📅 12:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28378">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMq34RklWsXOdOzivHJOZUYbTUU-m1ZAWf_fC8FsSFZGmzImcJPKRl0CIECZz1wBA4Fx5MmqaPvQVa_5DzTT6X_b7FqriZiVp_8aOXwyF4UmdFZ_fZm7fJOcYUGlE5-nBJnmkcswJqYbPz2r8_EF0gDlLnqk2AxYGfQgRopkOLx6YQQqvnSz1Nsm6ejOQZl_FptoHe40Zpml2hdW7x5d96I0Mipv5jR8_gsDKC0EQdEyramm07ueYFlrS9W7T8LwFKjgkdMb3Chx3wN2bBJ3I5AcOmbvTtts1_ecJcIXPccpFgPLebgYgmGmQYQ6KXYnFdzDbQklr05C9XBwuJqKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28378" target="_blank">📅 12:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28377">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a084028cd.mp4?token=teH_JsSIMGizLPgqNEiEjRRko42Y5Skf9kFG5ftVcSsQ4vVCte-DgLVOTg8PxTcn_K1_mpUb4SOdRvFAC6vh1FFzvqcFAS11n_OSQ4S2UVgbSfpiApS61d1XF7W2AnJ1Ktgg6ROfRfBo0qu-pX7-F50xW1cthO3E2KhofQOkwTai8Hw5epDKNrFVZjzOlTniOwh-9htUq2Jmz0xZaGS-KQCuHQoT39rtlCKfyCMncHYuuSUzsisjvJK5neiDRtSl5VURpzzcJIX0Od5dtOIUxi0-enOQufv-I4brGn_zcswhdaOy6BFMev6PLplkYdC7M7SqIZYkItfY09g5NaKGyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a084028cd.mp4?token=teH_JsSIMGizLPgqNEiEjRRko42Y5Skf9kFG5ftVcSsQ4vVCte-DgLVOTg8PxTcn_K1_mpUb4SOdRvFAC6vh1FFzvqcFAS11n_OSQ4S2UVgbSfpiApS61d1XF7W2AnJ1Ktgg6ROfRfBo0qu-pX7-F50xW1cthO3E2KhofQOkwTai8Hw5epDKNrFVZjzOlTniOwh-9htUq2Jmz0xZaGS-KQCuHQoT39rtlCKfyCMncHYuuSUzsisjvJK5neiDRtSl5VURpzzcJIX0Od5dtOIUxi0-enOQufv-I4brGn_zcswhdaOy6BFMev6PLplkYdC7M7SqIZYkItfY09g5NaKGyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدصلاح که‌سالی 17 میلیون‌یورو از ترابزون اسپور میگیره در اولین بازی‌اش برای این تیم چنگی به دل نزد و چند سوتی داد. بقول حسین حسینی از شانس بدش توپ هم باهاش همکاری نمیکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28377" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28376">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔵
🇳🇴
واکنش‌های جالب جک گریلیش، پپ گوردیولا و زلاتان ابراهیموویچ به‌مدل‌موی جدید ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28376" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28375">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta9fyESqt0hzlvVzgDJXJItdTux8kSsVLaJ47U3Ab6v1kcKstglOwjZhDeTynuBfrc0Q9j-JGR9I2teDP_6cp8OjZSsaGJ9vTgOJHaW7dW2HX9ZW3Hqj73j8tM6TKKn2XQyNAYGS-cnxxe_NahgwpAYFlZ5N4PA9m-dH8bnLfxRCTwd0Pc4lq39KxwGWQq3dbEhYtfHFN5hWg5IcJYONxHXOJ9HSe3aCyAw9BnZkFamA8L-C2OedDZJBrU9-f9OCs2xpj71Aq7EXsvV51EOFOB2e0aL3clrdbuKNi6JEjrzTfTbLNKWCw9ydXRXRpeNAsRJGp5KU6d0kQyuljClNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
عصبانیت شدید هواداران اتلتیکو مادرید از خولیان آلوارز؛ستاره‌آرژانتینی‌اتلتیکو دیشب بعد بازی باویارئال بدون‌توجه به هم‌تیمی‌هاش به رختکن رفت که هواداران اتلتیکو بشدت علیه او شعار دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28375" target="_blank">📅 10:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28374">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ4-ybVGd0NP1sUGX08DhmaHUlSzBvJ2cBLW6iyWUTwSTQ629aLFMIDUtvkTvfEKN-a4mwQiIMue98YS6z7sI_tE9JZ7zeibHw0c-P6HoK0J6g1OQLv5KQR8dAD1N_RL-BkGNhIfOf68747VgOlvCN8tvVOMETB4WH9KcnaAuFmSMTydL8lohb8x7pAGjzjYtm9UDWhbeHwVKFslZUPsQR42qT7nnMVu6ZE4xbktk4lP6Kkfx8a-YKG7g9EyxFdnEmVF4HXe8Xif2ccAVVLYi_yhgyLQ551H-m86CivXoDaaIKyDQdb2vDk0ChT8JoS6cjqADcv2mGXG5bN3wVAb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28374" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28373">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml0Zyqi1wztS82eCGczHwdUnifECPXpXm-aqw0QUyeez6N08CLZjZDxVibdbUVy5ZuaDplms5O9o_EsrhEbQSTS64daSNJ5KGw6grH4nw_4Sn-mkPmOPbxj-KIysSWaApkCj2_Aj1FoXiAg75E_J5oRndv9qW9FhKfT5l7QggC0HZD9E8VlcAIT8kfNAUq-Zo8gUDbR0EWE8vcWtqEUZNWSD7-gBZyEn9QBXsO3WpTYUlsjmH_pumETsqKzQGNdXZ4RPKrEU7J9XqFQIjQYK5G5f55DGMjZjnTZCRXIs3RZ5TktVKTXjxYzOZiQ17ScRFXG-duv1qaDNwD5qfMaNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10تقابل‌اخیرپرسپولیس
🆚
تراکتور در تمام رقابت‌ها: 6 بردپرسپولیس، 2 برد تراکتور، 2 مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28373" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28372">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400b87e841.mp4?token=m1viMBBHFLkrUC-nx_9MyVQU2G1_RRAAt3lKWplumWPzvnAc2CYLcNXDmI_-TxcA9-JenSM-YYlYI5UQbKIVI4i_j42f8LrqfotcHxR7PRO6A_DxdWIimW9Z9hs2Lh6eaS4RhP0XTPJ8vdWmJz6S3LbuIR-z9xLI-BkDJLdX2w0JIv9Q5ok2mNUa1EodqjMrlNG9Kp_NFI6f2i811AKaP2c5a-BhfEVs6rh31OHJ10yRBicSb1QziFnsttCiT8OUoYEENAIVJR3kmN3RZ4QgLyXelS6ahrCTEw9c3al6mbww_pErr4W_ziF5ybLo-9I9uREQrkJKPquURRgqBIxtmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400b87e841.mp4?token=m1viMBBHFLkrUC-nx_9MyVQU2G1_RRAAt3lKWplumWPzvnAc2CYLcNXDmI_-TxcA9-JenSM-YYlYI5UQbKIVI4i_j42f8LrqfotcHxR7PRO6A_DxdWIimW9Z9hs2Lh6eaS4RhP0XTPJ8vdWmJz6S3LbuIR-z9xLI-BkDJLdX2w0JIv9Q5ok2mNUa1EodqjMrlNG9Kp_NFI6f2i811AKaP2c5a-BhfEVs6rh31OHJ10yRBicSb1QziFnsttCiT8OUoYEENAIVJR3kmN3RZ4QgLyXelS6ahrCTEw9c3al6mbww_pErr4W_ziF5ybLo-9I9uREQrkJKPquURRgqBIxtmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو برای چند سال پیش نیست برای همین چندماه‌پیشه و خیلی‌زود به حرفای ابوطالب که گفته بود دلمون برای دلار 78 تومنی تنگ میشه رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28372" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7561a592bc.mp4?token=h2MUfsTs4CAZlgDMMkz56JK5zGmWFyjRVcdu2tJGy0bZDRuBG7Wql9NMLtxcgoLz8x1IQDMJ7uW6Pl2PJBrltq7JAT8xQpFA2Y69IJ3c2kmU0z6j7-wWBEEFWKw9S_1b2IwsUplRJLU3hXke1pahg7J31cuJzM2hIGcnlUZ_nfP5FJ_C08DTaFtJKVoSXC3N6Q0uRgLCYUkVZgpn1RqLPKiXz-jQFo9gvl5bgaxFsxPex25da17cUBS5RiyGLtM0MFgKwczjWEObVRY5q5HuQxVmlLikH200D7d73WWl4H4OiOd0mUi_UTUH-Vc9nA17UUssS7rtEI80UWK5eAsoNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7561a592bc.mp4?token=h2MUfsTs4CAZlgDMMkz56JK5zGmWFyjRVcdu2tJGy0bZDRuBG7Wql9NMLtxcgoLz8x1IQDMJ7uW6Pl2PJBrltq7JAT8xQpFA2Y69IJ3c2kmU0z6j7-wWBEEFWKw9S_1b2IwsUplRJLU3hXke1pahg7J31cuJzM2hIGcnlUZ_nfP5FJ_C08DTaFtJKVoSXC3N6Q0uRgLCYUkVZgpn1RqLPKiXz-jQFo9gvl5bgaxFsxPex25da17cUBS5RiyGLtM0MFgKwczjWEObVRY5q5HuQxVmlLikH200D7d73WWl4H4OiOd0mUi_UTUH-Vc9nA17UUssS7rtEI80UWK5eAsoNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
این واکنش و چهره عبوس رونالدو بعد دیدن رئیس فیفا در شبکه‌های اجتماعی داره وایرال میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28370" target="_blank">📅 09:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28369">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b7f7aa5f.mp4?token=heb5e3128rpMEoh9S_JJhwUbJHMNSAxvtaNwdZztI-qI93nVwA6qDrDbfbBbh-wiqEYVB4pSsDrMLLQbsKZ6-J1joSlemWZZ1Sf5_U44U8aoSEL8NHx8eL_pbqBpqOjXdxN13h51pNFWgPOqbbr760oCkaFhkKQJ3_TaIpDnS49b82Zo3L5-i0JIrkCl88X7gHHolcxgzMSxoC07Pu6exnfMYWEowhfWFScW97lHkToSVPRn9VUPj674K1nCe2TVPQ1EpRV01X4DIJr3sl-hIRGbYhpbCOcSaBDJfsQXgvrNq-G9-xft9FRO2CakEKCNpLNDqYMA2Kw8wYXlCd5lXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b7f7aa5f.mp4?token=heb5e3128rpMEoh9S_JJhwUbJHMNSAxvtaNwdZztI-qI93nVwA6qDrDbfbBbh-wiqEYVB4pSsDrMLLQbsKZ6-J1joSlemWZZ1Sf5_U44U8aoSEL8NHx8eL_pbqBpqOjXdxN13h51pNFWgPOqbbr760oCkaFhkKQJ3_TaIpDnS49b82Zo3L5-i0JIrkCl88X7gHHolcxgzMSxoC07Pu6exnfMYWEowhfWFScW97lHkToSVPRn9VUPj674K1nCe2TVPQ1EpRV01X4DIJr3sl-hIRGbYhpbCOcSaBDJfsQXgvrNq-G9-xft9FRO2CakEKCNpLNDqYMA2Kw8wYXlCd5lXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا ستاره بارسلونا که از ناراحتی خولیان الوارز ستاره‌تیم‌ اتلتیکو خبر داشت دیشب بعد از گلزنی این خوشحالی مختص به آلوارز رو انجام داد و به نوعی از او حمایت کرد تا روحیه اش رو برای ادامه فصل بدست بیاره. آلوارز خیلی دوس داشت بره بارسا اما مدیران اتلتیکو…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28369" target="_blank">📅 09:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28367">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82aeca8f4.mp4?token=XgockX_2cd4-psybdM81NMCjNb_Mh5LZ5TfJfNqF79T_W4np9lgFuQPbims4GXSaeFKsdYICa5n6aAacXYAV9V_xotb8-bY-fBIwwSsCLCXvvTOtfZTlb4QeRLyBIl7vrEbJv52iYDrQM5q3cntyyfBGcpwJt0yhp3TrG4YM0HYCfxVQha3u3nMdwmFT_bOnE7wseE_T80hMx-IlQWA7O0RCuQIPIj1XCJTHjJCHgNFwUF1qWDj87bgCmorJ1godRnTrEj42l4HHY5CeQpbonnyp8R9QD5pPB-5o4blLyKX0DQbvuKCL_oim0CIJEXqX2WhFk_ZTtpIKLF02RGJlAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82aeca8f4.mp4?token=XgockX_2cd4-psybdM81NMCjNb_Mh5LZ5TfJfNqF79T_W4np9lgFuQPbims4GXSaeFKsdYICa5n6aAacXYAV9V_xotb8-bY-fBIwwSsCLCXvvTOtfZTlb4QeRLyBIl7vrEbJv52iYDrQM5q3cntyyfBGcpwJt0yhp3TrG4YM0HYCfxVQha3u3nMdwmFT_bOnE7wseE_T80hMx-IlQWA7O0RCuQIPIj1XCJTHjJCHgNFwUF1qWDj87bgCmorJ1godRnTrEj42l4HHY5CeQpbonnyp8R9QD5pPB-5o4blLyKX0DQbvuKCL_oim0CIJEXqX2WhFk_ZTtpIKLF02RGJlAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
چهره درهم آلوارز در دیدار اتلتیکو
🆚
ویارئال؛ ای‌غم کمی تخفیف بده ما که مشتری هر روز توییم.
‼️
خیلی‌تلاش کرد دراین‌پنجره‌بره بارسلونا؛ هفته‌ای چهل بار مصاحبه‌میکرد و میگفت‌علاقه ای به موندن در اتلتیکو ندارم اما مدیران اتلتیکو بجای اینکه 150 میلیون یورو به جیب…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28367" target="_blank">📅 09:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28366">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292f9f2a3b.mp4?token=ApmDWB70IbdLWJviJXr57YFqumJrp9FnUNHnIQYAJWQcgGrVVLVJkJ457DefREvCZGh_L0ee7riMEK6ZlT-t4nq5BraD6tYOWgsOEblFplG9k8QZQZ_TAxj9WXr5V8eqJwUwoh61HAQAM3FKO4eVryDigY_w_BhkPZtbiaW4FxpQvBMN-XjEjn06h-HINgasGd3zXL-0SSFOihcNUGmHfF81JCZI1TZtvpX3UdtxY289ve7vDlc4bwi1iS-KbtVG3u6fPWGvW61LvdLbpI6P2e-X3DAcKS8bxwdaAlXHO7k1_Z-UFaogus17Q8KVNHXuRRRtbu_27MzmfeBMwXqQp3c743Cj9y-2-7DpS51BpKWYHZIor8n3Tccwz6T3ow0h-GJFiypBXuJSy_yrloDtV9gQl01g-8p--BwekJ4VoDHr1Mn4s87Y5cttDjkrSL0qux07VdVVDsFPkq2gY4pMJ3eMlQR-C-rYRT4CwCCy237UewS2oQMbZ9x6U6HjYNe-D5b6OpbTy73HkIlmh6__I3ttJeRpNv2XqGOVYPe9TLPgrfIvR98OpHHlJOWCnqM_QOkl9MzJDROSxG9_7vlrXk1_xg5PUWqmXl8hrJmB46HBrPsntzr61wS-NDAbfk4Oydjkl-BpO3Uo8Bm86GC13-xuYtsbnNDMjZAIoFrpWBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292f9f2a3b.mp4?token=ApmDWB70IbdLWJviJXr57YFqumJrp9FnUNHnIQYAJWQcgGrVVLVJkJ457DefREvCZGh_L0ee7riMEK6ZlT-t4nq5BraD6tYOWgsOEblFplG9k8QZQZ_TAxj9WXr5V8eqJwUwoh61HAQAM3FKO4eVryDigY_w_BhkPZtbiaW4FxpQvBMN-XjEjn06h-HINgasGd3zXL-0SSFOihcNUGmHfF81JCZI1TZtvpX3UdtxY289ve7vDlc4bwi1iS-KbtVG3u6fPWGvW61LvdLbpI6P2e-X3DAcKS8bxwdaAlXHO7k1_Z-UFaogus17Q8KVNHXuRRRtbu_27MzmfeBMwXqQp3c743Cj9y-2-7DpS51BpKWYHZIor8n3Tccwz6T3ow0h-GJFiypBXuJSy_yrloDtV9gQl01g-8p--BwekJ4VoDHr1Mn4s87Y5cttDjkrSL0qux07VdVVDsFPkq2gY4pMJ3eMlQR-C-rYRT4CwCCy237UewS2oQMbZ9x6U6HjYNe-D5b6OpbTy73HkIlmh6__I3ttJeRpNv2XqGOVYPe9TLPgrfIvR98OpHHlJOWCnqM_QOkl9MzJDROSxG9_7vlrXk1_xg5PUWqmXl8hrJmB46HBrPsntzr61wS-NDAbfk4Oydjkl-BpO3Uo8Bm86GC13-xuYtsbnNDMjZAIoFrpWBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شاگردان هانسی فلیک در هفته نخست لالیگا؛ آتش بازی راه انداختند و دردیداری خارج از خانه با پنج گل الچه رو درهم‌کوبیدند‌. فرمین لوپز دبل کرد‌. کریم ادیمی هم نیومده برای آبی اناری‌ها گلزنی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28366" target="_blank">📅 08:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28365">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c023812.mp4?token=hLxzeBoRrLyTwU0mt35FNYumQyjJM4XISbtyQtCt3dw1zmGsSh2GmvNX-EjXc_zRLf_hEL6c0yetBA3uT9p3dhUX9CX0owD-fwenmmNfcQ1-b2YjAjkHV4i9cupH_BLlWTcNKBksTXb7j7JWrdSxHKtgxKgOEicJCVQZIE8idNAsBZ2gwCxhRal-MuWdFsusI4PBXlzWja64Ytbbaxl_D3OVLUjnCeS_DmNouAomVMOXmzKU2S9XH0uoczZQN7NdjNdzqxflnmx5WJsf5GIdFH5OIshOwYHklF4o16_dEIO2012FCHuBlu5behSpa38yY4CS__uTQAKTpQLxA99Ytpd-PctgOuonL_zTIy-VgtYv5C8Uf1v_ZRzwnravR0D7QHWuoXY0Ay_JpjqBf4YbR2PCPH1VJvx7mgZFNYP831mXcmSCKnDjMMQSPlGpySNBZPmulOtXi0Xj1B-PFiVZlXInVZOVKWRtdPniJBJIR3HLFE2CZDZ76aXieBzGX65egIfLUun0ey4eNmK9uGkc9Nc0bKWovFCsoYVVFb49KWwIzZ8r5fcRKKHY7xOvOtcJ8I2zf4kECShxfswcFsDVt9FD_MySFVCNqe7LsfG4h9tVKwLMbaZGEfOFQQSZGoCBBF4nr-vCwcva3m5Y3Z15O2MOHo2xgmqacjNWWWg6qEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c023812.mp4?token=hLxzeBoRrLyTwU0mt35FNYumQyjJM4XISbtyQtCt3dw1zmGsSh2GmvNX-EjXc_zRLf_hEL6c0yetBA3uT9p3dhUX9CX0owD-fwenmmNfcQ1-b2YjAjkHV4i9cupH_BLlWTcNKBksTXb7j7JWrdSxHKtgxKgOEicJCVQZIE8idNAsBZ2gwCxhRal-MuWdFsusI4PBXlzWja64Ytbbaxl_D3OVLUjnCeS_DmNouAomVMOXmzKU2S9XH0uoczZQN7NdjNdzqxflnmx5WJsf5GIdFH5OIshOwYHklF4o16_dEIO2012FCHuBlu5behSpa38yY4CS__uTQAKTpQLxA99Ytpd-PctgOuonL_zTIy-VgtYv5C8Uf1v_ZRzwnravR0D7QHWuoXY0Ay_JpjqBf4YbR2PCPH1VJvx7mgZFNYP831mXcmSCKnDjMMQSPlGpySNBZPmulOtXi0Xj1B-PFiVZlXInVZOVKWRtdPniJBJIR3HLFE2CZDZ76aXieBzGX65egIfLUun0ey4eNmK9uGkc9Nc0bKWovFCsoYVVFb49KWwIzZ8r5fcRKKHY7xOvOtcJ8I2zf4kECShxfswcFsDVt9FD_MySFVCNqe7LsfG4h9tVKwLMbaZGEfOFQQSZGoCBBF4nr-vCwcva3m5Y3Z15O2MOHo2xgmqacjNWWWg6qEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
هایلایتی‌ازعملکرددرخشان‌یاسرآسانی ستاره آلبانیایی استقلال دربازی شب گذشته برابر سپاهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28365" target="_blank">📅 08:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28364">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsr0nOEIm_KjXyz3BWexYkyMQuqCHoNRIIv8lvW3GuYYxp7aueQb9E0wCNIkfj6tMRWcKYQ1H4IzNtLP95BCEZoZUEo4C3BESv4qEO_po6jU2xssMy8FsR-w4OWocii4fWtjDBKG-zXb8-sb6Fdhd8EvBArq_3Y9ImBgVse3veTB8YOLudDv7pHNvK9_ENukRId30ErCVtOpOJjx5_GLtgZYecvV8q_5p-5apU-ELNtcg3bcsv_4VNPZwbdmo0dLTpxXtIUrmDTe5ICKL5zJPGJx4iYX3ju_CtNb0uff-_bdXEYPC1IFgLEijRGezEByPPSIxeLPq3BTDcYPaD7Mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یاسرآسانی، اسماعیلی‌قلی‌زاده و حبیب فرعباسی به‌ترتیب با نمرات 8.5، 8.3 و 7.9 بهترین بازیکنان دیدار امشب استقلال
🆚
سپاهان انتخاب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28364" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28363">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKaGYsJLYb7nN0OJ4UeYD-I8RmDplwJXCbxRZ1uxw3vwobYU7aIjo1BK_LFSjJpEmm8ybJAeJwAHbRfKwLuAEGKGJkT5vGTpSRu1jfC0rhcVFT09nLEOyHOQ-9Hx-NTzk9oYCKwHwticHM5cHoGY-HHBL8pmU3iNvqrk_npFpc4U2WTd4UwBcmaB7G8F8fqCsBCC9d_uv9QIpQTp_o7fhDpcYeSaoXDwx-LwwDE32xMJ7wtslvwaPFONeUnoi_ybCKWaLRid77QPjzAM_FsUPwqqBVXqiFJjv9cKoIJ0ezEe_2O5qSzalJg4TnW8Eoas2hrwcdOtLMrDbaljwpYj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بخت در خونت رو بزنه همین میشه‌ها. مردی داشت با هال‌سیتی مذاکره میکرد بره این تیم که‌یهوسروکله رئال مادرید پیدا شد. تو اولین بازیش ازرو نیمکت اومده جور ناکامی امباپه و وینسیوس و یان دیومانده رو کشید و گل پیروزی تیمشو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28363" target="_blank">📅 01:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28362">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔵
🇪🇸
پاریسن ژرمن با درخشش و دبل فران تورس ستاره جدید خود مقابل رنی‌ها از شکست فرار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28362" target="_blank">📅 01:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28361">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1704880194.mp4?token=lZoBFnwsJLZzDNQf8j39njM93iVZo23kGf3vfYasx3JZCWlxQiEeBrKbvZWmO7lsSiMajBEffF4C2V-9i77qkAoucRsPMG56UX4i6giUJnFU_zWix9r4wg6dZS76PY8vaigB8JezNFxS8WWa96gifAn_3o4zOlKKX2xFwcwxfFUXOcNTqlgE5iweXTjWHTPuxooQmmPtljlbYlJrTipZoEwWDq7dz2qsnNrNGPYWpJHR__Q0-V-N2qTmaKRXImjoc1C3Q-GHfCIm2YtHbJz4V3gZuIxXVH9wcydXeEOrAPXd_V9NA1UM5yQvAdOzsNkHTY0Fh9LrGBjjqBpqNQDfkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1704880194.mp4?token=lZoBFnwsJLZzDNQf8j39njM93iVZo23kGf3vfYasx3JZCWlxQiEeBrKbvZWmO7lsSiMajBEffF4C2V-9i77qkAoucRsPMG56UX4i6giUJnFU_zWix9r4wg6dZS76PY8vaigB8JezNFxS8WWa96gifAn_3o4zOlKKX2xFwcwxfFUXOcNTqlgE5iweXTjWHTPuxooQmmPtljlbYlJrTipZoEwWDq7dz2qsnNrNGPYWpJHR__Q0-V-N2qTmaKRXImjoc1C3Q-GHfCIm2YtHbJz4V3gZuIxXVH9wcydXeEOrAPXd_V9NA1UM5yQvAdOzsNkHTY0Fh9LrGBjjqBpqNQDfkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لالیگا|برد سخت و نفس گیر شاگردان مورینیو در ایستگاه نخست با گلزنی کارلوس اسپی.
🟠
اسپانیول
1️⃣
-
2️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28361" target="_blank">📅 01:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28360">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NejyteXTskeuaOYuIGLm_H9xzNNiRjcPxaVMrGlVyGSFbrElyYlEfrCYL37_pnriGUO3Arwo4TIhTbxjcsB0DV2zCjGPXIlandgxsmQZnGHX_qvU486xl6BZ-jV5tNfAbCEz892qJDGDKIcfWngHslJgP639oJ3B7pMUp8l-rQLCVuka5wxgMJGVQIM663ShPSmlsDffOYKDVSuOGRFmmzFlTJOWuGYCJqK5W_QbKQtyKinValvB_pVt5f-_nI3Og7DzDCgF5bitEiI-eOYMStGSYvaDDwu20sqOUKrNwKBfOetFMzBg-fQEuWOQ-sLZ5LQpv0UiWY3prVqcA27HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
جدال سرخ‌ها با شاگردان نکونام و رونمایی‌ازچلسی‌تحت هدایت ژابی آلونسو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28360" target="_blank">📅 01:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28359">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OW8V_auMa2VOeorHAF448GHO-wv2lJeDgHctIzmpp352a0VhL8Wd-4J9RDepfY1vJmx1_SRLhO8RvbuHbAjR8WH7165I4DBTa1r_vMi4pjm7TO1CJX0pfDT6ySRfSsJjHy1KBXlPnfIHqyZetoU-TZr7FOGoYDDSCpscs6mqkzT7TIkmTpDS9Bui-TtqsxkFjcNd2-pMIaTEB-SyGZtbyuz7nUcE8up0R1nB4Q7L0lUmMcGRMpZQv5sMDA85G_vHk8UA6EyKcOiPgaNJ_lKorxhYzmGGvkkKcxk62vqCwKWkQUyFmwZVLYNhmKEj1LK_3BQvRSq8KnOMkVkrRYvP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌ دیروز؛
سومین برد و کلین‌شیت پیاپی استقلالی‌ها در لیگ، برتری دشوار سیتیزن‌ها با درخشش‌چرکی و جشنواره گل کاتالان‌ها در گام اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28359" target="_blank">📅 01:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28357">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amg7FjgndssE1F1OE0TyWRCebiIZ8zrWU0OiDmbr80Ubloj-a9VlefxIcwJEkMFo7dBovzrT7ESpOz4lhiDsT8vXhoOvJHcn1j4ZxA0IlnMP2LexwLrvemsvug2ECWhbQKX4806ylA8SsoNFWuBVjd8vfFZ3znNlK5j0OhoZ2R3R12YVvKtpwFFuvxvJoAoUChFnfJcFTXHC71iaVvGZHuTpVuW7nm9lJNomcvQLlgsgP1fECC_u-ndqqEhNp-24aNPC60jNH7RVGymZX7XU6HxIqQ12OQfPibLnCozsyPC5qEh6QufXPX6nfFxsKZG5ZGDfRjeGXf70ReHfYh918w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار امشب با الچه؛ ساعت 23:00 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28357" target="_blank">📅 01:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28356">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da75343e43.mp4?token=je3duwKnePb1XXDaJa97LTBAE2KEJ7oCw-z1yW2WgYQBcDbL3vbMDXOBXKiygCd5y3pH9NThJY1lJqCRFErQrmmd2BhagDFwO2JR4HwFtDqlukoXr51wDOGSEmWk_VnyKHTJlFWbrERpt4YFBPK55FoBrMm6aSdKeNZEqXI2inTauoazR4CogX-i0jwaMbK3gyZvsiaMsPJXGTior-DQblbGTVdpAkS9_VilORZXdvRCELjUgxw_gMhaNejgYKgR_x8EWTdLBUVk4S-L6EmZl5EZX6LySZ9ZB3IhraHyYeA1sKSTjopOBoMmnOh_u81sH43U-rAcNt7-qZdCsCx8-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da75343e43.mp4?token=je3duwKnePb1XXDaJa97LTBAE2KEJ7oCw-z1yW2WgYQBcDbL3vbMDXOBXKiygCd5y3pH9NThJY1lJqCRFErQrmmd2BhagDFwO2JR4HwFtDqlukoXr51wDOGSEmWk_VnyKHTJlFWbrERpt4YFBPK55FoBrMm6aSdKeNZEqXI2inTauoazR4CogX-i0jwaMbK3gyZvsiaMsPJXGTior-DQblbGTVdpAkS9_VilORZXdvRCELjUgxw_gMhaNejgYKgR_x8EWTdLBUVk4S-L6EmZl5EZX6LySZ9ZB3IhraHyYeA1sKSTjopOBoMmnOh_u81sH43U-rAcNt7-qZdCsCx8-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28356" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28355">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfDfqNdLsd9fuWYX0ehezra6fAaCI89EUZcbD66kzaCfMMhY8I6UJnNK4qGhfTWXYU2qMJaKcPZI2dre2_SRbSbigtDpl9D7A-zYYbmGEcFz4EYsEOXNsKyBbWEu5_ofRBD0yXew_JwDlfDjZ0jmVjAJFlhCUHaDXjC1fWU-GXGK0Y8BhHPsU_RoWqUVrEAw1RHYnmiyA9oxS2KnEVrv2zM5Z7q_rUNaRYrFPMUNJc3K9UejC0DMvCuTcTUQM5CA3iNRtPhqH-GSWrOfxKu97vpDfrzXqeMZ1lSkEbZ9WHP8FvHesmUAaTKdsxozFG7crZfSRkO9UXhHfmvO5bsBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28355" target="_blank">📅 00:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28354">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jat53CbScbK19mvFNz-c6SMJHP8DiwCOswmEBq8ZqOR5VJBZLoYrgGirZEghEWxsLOdrAuwx8HQ01Qdv1TtiVfEdSGtEV0dIJGvIFEj9sBEyoRI5Ekm0ulxO1fGDvXCeYRBao1fY9ejPvgouJKrwuDB2DI9tj-tzVGqoaBpElh3bZEIKOanHBuzTB4tyXDAXaGR_Ja5FiMLkJbofMyn9uCPvmz1YrPTUIP61ZDi-yjVJSi0amWTQWyA_ts-nBmeZynmtHsjAcjR64nQm_dpVVf0rVtatBUZQ5R-ZRsvFkQgY2KondoIK6vntM_WS_fAUo1NW7gfuHOZaJR-0hRh8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
پاریسن ژرمن با درخشش و دبل فران تورس ستاره جدید خود مقابل رنی‌ها از شکست فرار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28354" target="_blank">📅 00:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28353">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6gI-Lc4zx7sc3x-MQPq_z45jAUeTmMcSfSp3cCGD-hkN58YNDMcDQTEUq0qH05xGpaepNz8Pnj9HwfDWE4QigJMkPummlBfU3b8_cTqBYu8QW6NdKiDSYNOoNdqcRJUghKMQkfoTnBjjJkNOnYxSYHD1TGjx8PO5i31pcoqh9o8G8CwjuJrIMYUgyVthvBU807GsKHppaOnDjxRWE4bhmXJCnPoR3HzrBmKkU3pex0ah_KiUpZz5dznR5SHaIPtsZnQ1PtJFLxgXPfx-K2gaUgLjbLLccGNs2hRoKjO8vkLFrNEJGXSV-avGEQrkIKclA7Nr3KB4oEfIXkzYScYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفاصله‌چندساعت‌تابازی‌تراکتور و پرسپولیس؛ هواداران تیم تراکتور مقابل‌هتل بازیکنان پرسپولیس تجمع کرده اند و شعارهایی سر داده اند تا به نوعی شاگردان مهدی تارتار نتونن به راحتی بخوابند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28353" target="_blank">📅 00:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28352">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e759f195.mp4?token=nHMfS1SOnUJi_aburxZSwoKMkLIcnhMgIbZv7FHtHeBUnDUeP69IN1ftsGBH4UvWdaQ6Ex6uByEsB03Qb6eQaz5IzYPN9k8cF3CeHNcK--yk9CdeAh4sMWxFVDDbhn8_di_cwA5lQF6Z6UaGztrTXOi7ykOE2uli_UMthddoQEINdK8o4Gs90Wo3x5I5nlL_J5mKawPaEwOsJ-IRg_xE2BVs52WxGkOVjDQZP8L-fLLiqPnJwec5TPtRspzPrv1kF_8Ceo0BHZjOqjxS_1S8BA_zcKEUabVfZCDd2i096e4_FHeeeN2-M_gJ9UR302dXp25z5hl4IikjwWAoeVYb6nsoZ1o4xCBTwKm3wWxgIv94R7Fdvt7OvmMb0XFA4TWSDGkj_1OTFyiVVcQP9O2XqiwGz935-gKRzWwvnzjPm-PAxMxC3uT2gjI_NQPGSkAVBlRaEC7jCd1AU6W_YRG7Ojh4AodBVNKS4g4bLql9eQ7zdiW28XgHKDPO7A0_3ZMJb9vVD9FfsZYjEBfLWhiycuCIq4BMOd-uVi8jYD_iFitUgxOdfR5XUcTuqk0fjwZozDxzKQY-7NkTxIjGDqllnkn89DdiZO7yLAauFM5X2RYPwZcQIEPEz9TtpbrudWy3XBeuZqIgU2XJoYH-x9_JFyMTVR0Ya7thwqKUb6RkSaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e759f195.mp4?token=nHMfS1SOnUJi_aburxZSwoKMkLIcnhMgIbZv7FHtHeBUnDUeP69IN1ftsGBH4UvWdaQ6Ex6uByEsB03Qb6eQaz5IzYPN9k8cF3CeHNcK--yk9CdeAh4sMWxFVDDbhn8_di_cwA5lQF6Z6UaGztrTXOi7ykOE2uli_UMthddoQEINdK8o4Gs90Wo3x5I5nlL_J5mKawPaEwOsJ-IRg_xE2BVs52WxGkOVjDQZP8L-fLLiqPnJwec5TPtRspzPrv1kF_8Ceo0BHZjOqjxS_1S8BA_zcKEUabVfZCDd2i096e4_FHeeeN2-M_gJ9UR302dXp25z5hl4IikjwWAoeVYb6nsoZ1o4xCBTwKm3wWxgIv94R7Fdvt7OvmMb0XFA4TWSDGkj_1OTFyiVVcQP9O2XqiwGz935-gKRzWwvnzjPm-PAxMxC3uT2gjI_NQPGSkAVBlRaEC7jCd1AU6W_YRG7Ojh4AodBVNKS4g4bLql9eQ7zdiW28XgHKDPO7A0_3ZMJb9vVD9FfsZYjEBfLWhiycuCIq4BMOd-uVi8jYD_iFitUgxOdfR5XUcTuqk0fjwZozDxzKQY-7NkTxIjGDqllnkn89DdiZO7yLAauFM5X2RYPwZcQIEPEz9TtpbrudWy3XBeuZqIgU2XJoYH-x9_JFyMTVR0Ya7thwqKUb6RkSaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه دیدارهای فردا ادامه هفته‌سوم لیگ که در حساس ترین دیدار تراکتور باپرسپولیس بازی میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28352" target="_blank">📅 23:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28351">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHQFz-cP4742ltYj8-HjMbVhI96Sq51FxdnA_bxcH4y21ToGt481Syf1X4fBiBlnoZPbD91jFX9cnspLCe-570MGyccJHl0neTnVjclwZNs9PYf3dLxgCX5byjcNdBsRzNLf1NCLowxhhD6xNliJvH5sGdlqsJIRY4CQ9zJ-UtHbZ6NlaNisHP9_NzsgdG_XgsjwOUsAJcMe_ZyhE7QopOqpKCee3EKvFWAQGFUPBjAVImLtlkU0k7tcyU8hnhKmoEOV8NaxxywhLLBiTszg9NItt8AvvLx8Mti-KRtNeqX1D6q0iW5NRyvZaSBWuX9MTicWkxCeD3gkPDSdf3Io_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه کامل دیدارهای هفته چهارم لیگ برتر که قراره روزهای جمعه و شنبه پیش رو برگزار بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28351" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28350">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8101aef2d7.mp4?token=Ko9cVxQD5j5DXSU3piuQySbvgqtOZZjkqLX_aBwZ9SukY5Fa4ZOVn2e-NswNi3V4Hzp4GFi0Hk0Dn8sYvpxpJOIWUoW3JiHOsLlpGFXck0N1b3_sYFiJ2Z1V3PiPEv3YJcEFr5egmxpLMU45jgzMlrCB5-zSdl8p-BpjY_8OP8lxEG95frFih8W5zcTAJUvj3tCn7b9OITY6Pwl5oFMKRyM0F27ACYU0RZgG3ShTW88qKOMPxo__SuKsrRud01Fedasc_dfpnXnDQvAhYHPQFY_af588Rr6D1iIfqzOCsx81Hs0A69V6GOBO8Z17RmDH0k9SpVfwSv0RxOiLDlh8kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8101aef2d7.mp4?token=Ko9cVxQD5j5DXSU3piuQySbvgqtOZZjkqLX_aBwZ9SukY5Fa4ZOVn2e-NswNi3V4Hzp4GFi0Hk0Dn8sYvpxpJOIWUoW3JiHOsLlpGFXck0N1b3_sYFiJ2Z1V3PiPEv3YJcEFr5egmxpLMU45jgzMlrCB5-zSdl8p-BpjY_8OP8lxEG95frFih8W5zcTAJUvj3tCn7b9OITY6Pwl5oFMKRyM0F27ACYU0RZgG3ShTW88qKOMPxo__SuKsrRud01Fedasc_dfpnXnDQvAhYHPQFY_af588Rr6D1iIfqzOCsx81Hs0A69V6GOBO8Z17RmDH0k9SpVfwSv0RxOiLDlh8kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
بانوان‌هوادار استقلال در ورزشگاه شهر قدس در بازی امشب آبی‌ها مقابل سپاهان در هفته سوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28350" target="_blank">📅 23:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEPpjJRyo4Aq6kbMWpPaIQklFDZjtXNnDCKKewKJj5rPvy699bIBlASJ201-7hoHniy1m5zyY-zlNixT4E47UETyNx1brTjO5QdcrOflkFeLmoiWspXPQH3m0vRWQ6bAblg-ec-TsFDYh12ndeiDP4UdgYW7_zYPOaYp2A5f1EJprziqv0_QQ-4wCWeLx-uidh96Fyp1LJeYycMLshicPj4xnarSqPTn-0ygQ8iBk68axa26IS7ADQJNNCQGixvTgiHVCLwBhpuev505jlGiMxqAxASWQsU_95vQgf89M9cX2AxqA8TyFXGDEKe2qQxMgE69lvxOgHCekPV8-OPrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCImDF_aagO1qEEewMLmVMU_KB5vWicFT4VlQP1Vc0IE-7sBIMhO2wM8OHL_K8kcJ04p05H4NJyiRYdQNB9cfNA2kMv7pZm0ZPRu7wFUIGbhIUQSD1gcw6kZO8fHmEZSZCLjslF4YugM_139MNjmmAeWG5cNnbMiRSRiWT4-6qDTUKCz9FOQac0STovGUzRaFXc3d3iG1xosgcEuL0BAwuB33ANtqbLWAopX9PByExC3UBh6wm1tVwvjxa6tYSWSAe8G5195inopPOjbkPVz0r3oZIDZ2icbUDiSBH0aqJ8Po_O3arCE_-qGOUgEL8RwXkEza_O2jrZ3JtNDmMCurQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
بااعلام ایجنت مهدی طارمی؛ باشگاه الوصل برای‌خرید مهدی طارمی تنها 400 هزار دلار به باشگاه المپیاکوس پرداخت‌کرده درحالیکه این باشگاه یونانی برای جذب طارمی 2 میلیون یورو هزینه کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/28348" target="_blank">📅 22:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpqfKoroY2fvMwWgbdMp5KWqjdjzoqlFssQ_pz-fwDihQ3m4LB0KRLVzqUd65hfPvHqn3peyTl_1XjJEmvpmWfAwE3s6osUgD7uCN2c5T14l7PevZc4qq3LnMIhoz0CDSgw-WKkXcpcMUGjnXfZbLw5tYpc8pc4D1IE_cV0o-yH8SNsTu8kES-1-d-tVCrQtsGeD5oKR-Nf2XFetSVL4J7-CFzvdHFhZffVsUWWmFR5yfe3es9RJ8mOgvneHCiQuadOch3hu-07SolPOp_EpNUtYEP_cfsrwvyxnP4ABW7sZEvqBeTTnjL0TWEuMQ6_2yXUNgVYOOuWz_fp5WjuVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/28347" target="_blank">📅 22:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRLO4Vs9-VBknC5p0sYE5g3r0gLkZBEQYL36MxZfiD0chOc-yW23-Lu4BF_rdUP1V35ZqrBrU8MIecZ7UIkI93Pon240zZFaPrIeX-L6fFeMo4OGBDOgitxRbsnxQWwVYd8y-lo4HLUOZe_3CNlnsNQHBgdFeiwJLtNbSR8i6GqwEOEAaobQAZqag0mGxLlrCHQJ5nFA8ss6N9pGM8wMsNvxzfNiMaouF6z1gFmDExYrtdI1gtBmuwBYpeI5oDwNdfjrdKmAyvJa2X8WP5medXsgkc1VA17BM1dsbdN2R9zuLt0t-j9BhRpfRZZDGuf2Rh88y3gEMhpK9t09rqHh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بدون کلین‌شیت بدون پیروزی؛ حسینی به‌دنبال اولین برد مقابل‌استقلال؛ سیدحسین حسینی تاکنون ۲ بار با لباس ملوان و یک‌بار به همراه سپاهان مقابل تیم استقلال قرار گرفته و حاصل آن یک تساوی و ۲ شکست برای او بوده. او در این ۳ بازی گل خورده و اصلا نتوانسته مقابل تیم…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/28346" target="_blank">📅 22:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgLQtQe9HJsAayv8n1aSw0_qh7tGQFN7baLui9_J5AcNOZQm3GrLz0lrguPG9wQ0cBVx2PVAg-TEGm2n6UXqqI29MFQTMVFyVhx0toQpa8X3N9nQ-8G9Gb3luB-qOxsY4ABQbxoQvNVWAqMwZ7RyntwgOuFf7aP-nPM3LwEB10FHaG9jBbnC99w7mstrTjTOR70ZWqAx4biUohoBTc5jUjCNPSHpuELmkg7m2W0sv64zwXtmuTWsazTCeedWB8M0aikOyLRlcQwKcPm8Qp7yFovW-FrhD33quuEk1Pq4j1yCsDCdYrrf7Uu8r9ADXjX34fMU2QX5cuW4C8omxcJGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umyyn9U9FKRI41Z5fnYObg3OeEDj-3m9H43zSl78PJm6ZWNXa-zfcfMhy4_VA0BNb_JaPq9eqNXTxod77ZTXR_aTth-GeNiuPvqMAnnF_KjzQJfgYRip9q1Fthv-hDwvXYvAkFw4fOKlSZiBN0NtcbYCRCybbIF7haYvjqMF68DEfk_3tfqmbpcOgjhjCWT3UkIiDvhUxVawHOAQ4a7f97G6RFfQZRyIkj0HyIQ5JS1izf9YnwrEn1PIYtLIO1gVKOD3cuWRK36tAQt4KClNsCoQMBAjo6MbFbhZF0OWdP6X7QImYgljApUKTr6njWixe9o5rXiF8MehWemhRKP3xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جواد کاظمیان:
اگه ازم بپرسن بهشت چه شکلیه، میگم این شکلی: با جام قهرمانی و توپ طلا، کنار سرخانمم مونیکا بلوچی عزیز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28344" target="_blank">📅 22:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkxQzL5sgDzQlu7quzMm5uzojNw8UdUX-KoKm0EIC5CklB8RoH6tZijJKtpw0iooA9XyEbzmsltebSDqrD2xFCLscs7GrktTlNlM9gPSQTRWW0PlB_qswxu1BXW4jwS3_zVbJ_JwU44Hdvosduhs17uud6YhyVs4i_Ov11FYKXXcFJYn6f224uSF7btnVICapnCLblYacC9MCqyJWl_TyIbYJb6ex0h-keto9EVU9zDPKU8cb-FVjCb0AwMlOfoPSFxeD5Y_unD9wH-8ayIG1Pefn20q1HwbqJ-UEH-58dnSm38syk9Jw-tnSrZdCTDwgl3N4k52-XdBTrGJcMP-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28343" target="_blank">📅 21:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZbNlqqwWlNIQGf__dvloAlnWO6qEnE5Y9wP8eDaYKh0jxt2Jr02Jmge7u-E3rxgKnhg3YOz43Tobb9Znm82WzaQMa9_W4SqA-JIhC8tH9rkfUGmaD8ANCJK856NErs2p99FOMzSCUEsyDP5eP-MOMkbzG1CyrXeWL0u1C3eBIwDsgP201RKNJDB3Ki6SiaOMos37Ht2Suqqasz0HST8Wu83ERz0rgA8IiKlIFZJU6TyFM2ZzrKg4i5OLH4TzSZxuDpoRxJ0keYambRjS2dWUrXKZxEFJQ_5MeogtZUczr-8yGgPL9VEkGQYPyH6UBVardt5RvWEpZnbo9kV96vcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
به مناسبت بازی امشب بارسا مقابل الچه در هفته اول لالیگا؛ نگاهی‌بندازیم به اسکواد نهایی تیم هانسی فلیک درفصل‌جدید رقابت‌ها باجذب رودری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28342" target="_blank">📅 21:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
خلاصه‌دیدار تماشایی امشب‌ استقلال
🆚
سپاهان در هفته سوم رقابت های لیگ برتر جام خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28341" target="_blank">📅 21:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8gth8WnXJFoBm8bJHnvl547JAmZCf1-Fzu9wEa5MsddEOzCFlmU3QHKgb3BdiJW8Byhk70VYS6940a_5yLCcAWK4AwfvlYE1cPxq3OPfyA9bu25073ZRbvGRdhp7YqzSLQ2SubLZs-czhMxxPpy8Lg267BsN9JCW7NxI-tmLV7epjEop7XD-58_B5P5SdiVuoIKdgBMeTSXjCcX512wMs_PE9P3yY0MMBxyJHrxrPx9Y0xBi7_sSTWJwsBNMf9kfqHm5ab8vRrt_o-zu0uDpXCc-6o8bt4bLfFKAW8YXebEh5TGa1Ag9QktBneDDSIFh5ckC7I5rbKBEUMYIHqjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم ملی امید برای مسابقات آسیایی ناگویا اعلام شد که امیرحسین حسین زاده ستاره تراکتور تنها بازیکن بزرگسال این لیست است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28340" target="_blank">📅 21:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP6LlggwX1YUd1IuBy8SKkUVYduDGOo7tSNv3luQd9WEc8caTqHee-XWuHHQ01NLj5Jx0ToOG9crmzAJu3HOAteg_E9O2nmX22Uojaw-52e9c_LVo3HD4--4RkYPt2Suv-b151P2ZUeTOgWo28Nz-szB3l8J4IDQzIVT6fEzUct0JSBbWvUGBX2TbTQS-UiTiWX6G2ftTA-sQaRAfsVtzAy6n-ncazlNKl7_Dx7-NWs2h-uxGJ4HFMh2M8ZtY_0ZNcMl2QUylMNg_G77tzbPdEFtzQvyucTcJu35w9D0jUn9kGceOiEbmzW2LctHOSNpqsjK8I1dH2ywFwpU6WdQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی ارزشمند و حیاتی آبی ها در تقابل با طلایی پوشان زاینده رود با طعم کلین شیت؛ محرم نویدکیا باز هم به استقلال باخت.
🔵
استقلال
2️⃣
-
0️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28339" target="_blank">📅 21:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkprdPQhBp5CfOa_igOB23j8c1hDHHWdSQppboqoaUQ3P6hPBRnD1O_mx0JQv2_QDlveKsr6Qc40Ueus-LxfYwzBMV2QK_aeOWgVygeFVlFhbH9mnlLLxcm0XQvqVFrc1JaMeDR3LlzRQkO732gZTaqGa1BDYjv6xezmB5x7LaEwawCdjwTbFz-ius9PactVZp0eio6LSMsk19RnqnTGcWWparJDcUOR5oZBjf0MpDgBhuNqJ7r9Kj6LgWIhw0fY7BHl1BPVJVZ-SUkIhhigsFCUUFzKP9_D5yOOQwFUaZx4gCAuK_cfFNc_0S1UjabbaliafCTdVqR9QB78Gus_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی ارزشمند و حیاتی آبی ها در تقابل با طلایی پوشان زاینده رود با طعم کلین شیت؛ محرم نویدکیا باز هم به استقلال باخت.
🔵
استقلال
2️⃣
-
0️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28338" target="_blank">📅 21:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZo6rhiKSq-IhGB8PcG1ey8DqVKTKZ36yUKM6s-wy6qIEWtenFNUv69EdgBno87ty9wAXQWrXtNo_qe1t2NCOxDcLIp-koQz2UP2Y4glBKSXm1hPV-S4-c3sG9XLq-X9erA6W54L9NltaD0Na-mUim-pCv1RIZJ5qja4S0RMJUlNGMq3CjF4ZXioCg111wjvhviMjMD48u7Vg9eaDBCPt6sx_eo228Mj1UrFEWWzviXfXcjA2iC3xiOq5NvlHTxRipaLBkpNs6GE6GKih9PyiH2uazY-Rn-yMcfD-xeFUmKGTW9XKWxy6SZo4zXziAO-xkdyr8FQgP5hdZpz8Jo23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28337" target="_blank">📅 21:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28335">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXUSSxSIEltR3G0fseSqsYL5_akKc8jNdVPlsr5xI2vTH40mp5gSCBIoN6GyZ2m4ObnourhKqfSAwnA72TODr_7r_y_swo9dmKGXCuwiQaX1FvsiI1KY85WW5XrzHkdmz2rluN2TMxS9az5uGuqeVA21j_WaZFb_f24gpAWAD8X2Ys-luRkJRfNGn0G8IdUuX-AOuuqxJzQ98XtDLV2JZK1jzGSB8fvCJ7z831bpHhK0nEAvhOOtdfI-MdctBYi8FSvrEh_QUDfKC9sFTFkb1INoEs9hi1UrciR19FaAJ14RZjkG-EnAta4RcnkhsHaNNnfcY3FjNAlGiRYDVeACwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXQIywC1ZKv2o0xt-yLpAW4KNakaHjtW1Cp8ellieFWbImMa3-3t_qeBDQoaL7iglIcME-u4uBUI761D8rUxQHCV5b8A8S6bD-l77ImAM6XBhek07LXhD7UO6hdRtOopJvuLrfcYHeFUhspeutD7PGwn4ewYQkIqZAcxRUnCD_MBBEK5iUQgpbEiITyS2fLmMIt902OYZl4Q15AtPkfM4qMW21_0hybd19DvrEvya3krQsVUsxK8zXiTUCjOdSqIURX96DuZufF5bGSkq3nMkIK2xQkIhDC22LzGmOfzu0IBQmr3vm9dqRvmMbfTorFmUyAERyklYTEignjSFkIDnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدار مهم امشب
؛ فرار سیمئونه از شکست در گام اول لالیگا با گلزنی پسرش و تساوی پرگل و دیدنی لک‌لک‌ها و کلاغ‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28335" target="_blank">📅 21:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d47b1892e.mp4?token=CdgJVMYn5mU469YdGxYIzP7DPdO9wOTDNnXwjMpX0Xo7nr-iyU3wpLOOojtq8MXXj1tI_Hppk85vdgMVI_xyLXXlpWZQbYkkH85rUS3RcUo8fbM1mdEHbvp4rX5B0AsFBMRK1_V26Kjk8k-YXlYIAMyo3t3cDFsFj7EkwElkzmzHqUgeltr1Pa3_CnLjOeuH3IrEW7ELwLPXPvfIA8iVSZ_Gf4Ed6iamGLi8s-rejXn7U24dpjByuBZjyaqPMlCLQg28pzAXp9LjhFHEJNcRB0joxR7E8pb0_BxDBZOs0tN8cJQrDFnKbDI3kwzW8dtjVuTCbNinWN4GuIFNveD24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d47b1892e.mp4?token=CdgJVMYn5mU469YdGxYIzP7DPdO9wOTDNnXwjMpX0Xo7nr-iyU3wpLOOojtq8MXXj1tI_Hppk85vdgMVI_xyLXXlpWZQbYkkH85rUS3RcUo8fbM1mdEHbvp4rX5B0AsFBMRK1_V26Kjk8k-YXlYIAMyo3t3cDFsFj7EkwElkzmzHqUgeltr1Pa3_CnLjOeuH3IrEW7ELwLPXPvfIA8iVSZ_Gf4Ed6iamGLi8s-rejXn7U24dpjByuBZjyaqPMlCLQg28pzAXp9LjhFHEJNcRB0joxR7E8pb0_BxDBZOs0tN8cJQrDFnKbDI3kwzW8dtjVuTCbNinWN4GuIFNveD24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/28334" target="_blank">📅 20:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu_DPm29bdkO3qjpY00iTGMDGGhZStXm3876ZI17NJGt0Bx9df6yCig5_ZKcam6wkNwEwGgS1-xlFwKmaC_e09NThvSASfnVRteMZZLodhf2foaNThTUVkg9cwWuCHUbpnu4DCsfHvUo22e4176DTt2VUphgfMlYLHH7icnVmjxc2mJxJ6QT7mL0qtoEWHNUQBB2BqxWRVpCMR6Z4KyZ9C2gCTZUzvpV8QwMS7PxzLmYDIXBouun30ADWKLx1mEPmjmY9m4U9b2qjWxQcrJQZLcJ-gKGsjlZNZj692NPE-XslfOkjDBKVH3CJjVzTS63xxB-gzI3_yVvdRkXeVLXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
دروازه تیم محرم خیلی زود باز شد؛ گل اول استقلال‌به‌سپاهان توسط یاسر آسانی در دقیقه چهار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28333" target="_blank">📅 20:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS2lyQeIcXSkJ5FziRMH7jSrNviy34pAzP_jHeGQbN3j52ZxIH8OTvQAxlVvkcl23Ez-R_35Mn4tKUMwdNt7dRGJ_4yc27NlmkGebvD2ZuvPCWC5VxZyFfAzMQ7rJ7gvXJ5vmsJWaZh1nN_cbrdvNQmVLwkL6FFcvEiu0mCWhMVRLUkmpbvlm6HyjUXvGxsM_BOykIT6iIJFmBF_f6pIJhWvUYPSK5uL6TAHv66nr83YdKA4SxtQ2-ifZnNxD9817YPfjCbWFAPxYot87TcjzNO9R7XfMURENnh1021AxfWdRlAIi_h-gEnZMgruXqkr4wz9QBc06EjOAY6ETt8Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28332" target="_blank">📅 20:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3797b4f0c.mp4?token=Ti6eJdWNn6AcCrFIqA1ZqvRaWXOI8LL3A9jG-MJrxa9I1FJZN2AwEZeYuzguC6aeLFyxVQAWlE1othd_yKx83I5yzd7MvdQwQ1XButIk1nFYtCBiQRUtSHj-zgCojLZSFNI1wQ4VoNiXvd6QddJkdXRWi1XT8utztqphpd2fdVi82Et73M5XZZBjduOj2c5p7SDHMSqgVnioH8LXQR1dV01acwy1PN6VYM8WAHsAtLoA7PMmCY9q55LGxp6gNUYLWr7TxSpjqkEjBU46XbO0O7JCcgvatO6Z7sIweQ2n-sMMS4mpwb969LVl9DAHj93nP04aR9EANAqqw7G1Pp8mmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3797b4f0c.mp4?token=Ti6eJdWNn6AcCrFIqA1ZqvRaWXOI8LL3A9jG-MJrxa9I1FJZN2AwEZeYuzguC6aeLFyxVQAWlE1othd_yKx83I5yzd7MvdQwQ1XButIk1nFYtCBiQRUtSHj-zgCojLZSFNI1wQ4VoNiXvd6QddJkdXRWi1XT8utztqphpd2fdVi82Et73M5XZZBjduOj2c5p7SDHMSqgVnioH8LXQR1dV01acwy1PN6VYM8WAHsAtLoA7PMmCY9q55LGxp6gNUYLWr7TxSpjqkEjBU46XbO0O7JCcgvatO6Z7sIweQ2n-sMMS4mpwb969LVl9DAHj93nP04aR9EANAqqw7G1Pp8mmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28331" target="_blank">📅 20:11 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
