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
<img src="https://cdn4.telesco.pe/file/Urx7n8UWhVMfZoJwOgc_v5teOhSn6CsOE07iV0gXBPUDTHYLWJX_ZUetCqltDU9VgrEBrtWu5SRfoGNVqGZfRnrZ5iBLLIcjPmYNPamFCu9XtnM2XgqokC1luBD-ya4atwGc9Hv1_QOFn-NB0lsRrzGVadVlErQmMwPPMGWNICHbkpfq_bgAz0p5_r6tBXfdz5qC6jvK-_Uiqve79MdiO7_LI3AESVvMqfqFYr-xUk5cx8YoPQRKd9N8ZLS3BzWIl2Y82kd1lsRzFnfZK5WW_0dS__mPLR5aRXdzaCqdOSamGfrt47UMjunl501yYriktjtC7rjqcxh9MtB7sISsrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 580K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-29257">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=kR9rZ_fgAHYgKHtEt_e2g1PYe6MxZV3Bg2yanTVouMzAs4xvNBgZAmSANUUut6FjfrsmY4DnjiJufH-u3Wmfse-ZtgN5FdOpBS7t9P2AHhLZN9HbwkO0QKQHvgVkYxf8WifVkbis5tyC1ylVNq4mrrt8ZcRiQDwUehs9U53UaelWk_xULg6jIUT8G1DmWYlt9ZeH0n0iwIOlEgPJ7TnSdem9-UiLya3SXjGq7MUjZ9St0dCqwMOrQfs8XQN4BOwJaC7h-x8lukEu8pzlP47qXJiDRGTj-LijP8HZSdood8Q2puQI5CBhvGkwHeqWPxzv63aLEkcDdkHLvQ12tAXHPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=kR9rZ_fgAHYgKHtEt_e2g1PYe6MxZV3Bg2yanTVouMzAs4xvNBgZAmSANUUut6FjfrsmY4DnjiJufH-u3Wmfse-ZtgN5FdOpBS7t9P2AHhLZN9HbwkO0QKQHvgVkYxf8WifVkbis5tyC1ylVNq4mrrt8ZcRiQDwUehs9U53UaelWk_xULg6jIUT8G1DmWYlt9ZeH0n0iwIOlEgPJ7TnSdem9-UiLya3SXjGq7MUjZ9St0dCqwMOrQfs8XQN4BOwJaC7h-x8lukEu8pzlP47qXJiDRGTj-LijP8HZSdood8Q2puQI5CBhvGkwHeqWPxzv63aLEkcDdkHLvQ12tAXHPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🟢
مسعود محبی مدافع میانی 22 ساله مدنظر استقلال درنیم‌فصل لیگ برتر باز هم با این ضربه سر استثنایی و محکم‌برای‌ خیبرگلزنی کرد. خیبر درپایان مسابقه رو3بر2 به پیکان ساکت الهامی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/persiana_Soccer/29257" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29256">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇪🇺
🇪🇸
🇮🇹
هایلایتی‌خاطره‌انگیز از بازی فوق العاده تماشایی و مهیج اینترمیلان و بارسلونا در استادیوم جوزپه مه آتزا دو فصل‌پیش درلیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/29256" target="_blank">📅 19:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29255">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3fc5egLOKfKri6qvz0dmlP41oM8eNaE3cW9rU3olDl3XSbUob8rh1Jfy4runRFHdqqowdqHEiAWvAUf5pSiRnZinTbll0bhdycmx5-2EX3q5ui9CpQB9Kwfk1E0nSkP26sFn20EQ8xpm3neai7Xu3DgFTqYacqbP6DMKI3JjvwxKVNIDmlikckDY_cLPRPuZcKlc-kw4x265F6ooH3CH2YZxTQZ_l9CThS1X0barv3UAXc5DM1l5hk6XGw-WDtpxFj_sH8ok_2FQyddWJiJcI2z34t4Z4yD6HYUCMVZaTcxaAy8MtDGgqgxnSWqjyB_2i0kqMENs06_GfWQMUJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
دلیتا گزارشگرمعروف‌شبکه DAZN ایتالیا که مدعیه امسال‌نیز اینترمیلان قهرمان اسکودتو میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/29255" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29254">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=vp-7cCvI704ETp933MbNIEVe9M5QfTfym8q0O5Bypk2QENtIvPuAgopma-R-rEAvMUX-6W3n-v_-g-oxUEpegWYlKyQ1y-tiUmZFxvUVmWR71oUljhe6n02pvq2m4jzT4zBb5Zr8wu2SUOvwVl_sQG82xkIdLa7kMMFlbzNNEuFSzc6ZCRLhdffqTZrOsEKS_MB4cdzuCxVcK6ORC5B-bCkIl-wejyJ-_JjZYALHBXWxtpTUc8nMK7rSvPmzPbQ2VDw94GzRn6WEeU5-hr3MRB1g8AZgT5QjKc4z-6M3g-PNcvQYQ5kUBTnyMhLrmZ0XnGqgAwnFSkrcycp1RKJFKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=vp-7cCvI704ETp933MbNIEVe9M5QfTfym8q0O5Bypk2QENtIvPuAgopma-R-rEAvMUX-6W3n-v_-g-oxUEpegWYlKyQ1y-tiUmZFxvUVmWR71oUljhe6n02pvq2m4jzT4zBb5Zr8wu2SUOvwVl_sQG82xkIdLa7kMMFlbzNNEuFSzc6ZCRLhdffqTZrOsEKS_MB4cdzuCxVcK6ORC5B-bCkIl-wejyJ-_JjZYALHBXWxtpTUc8nMK7rSvPmzPbQ2VDw94GzRn6WEeU5-hr3MRB1g8AZgT5QjKc4z-6M3g-PNcvQYQ5kUBTnyMhLrmZ0XnGqgAwnFSkrcycp1RKJFKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکردبرگ‌ریزون ادواردو کاماوینگا در فصل اول حضورش دررئال‌مادرید؛ سال‌گذشته و در بازی امسال عملکرد فاجعه‌ای داشته این ویدیو رو ببینید باورتون نمیشه کاماوینگا تو الکلاسیکو اینجوری بازی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/29254" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29253">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=Ana-AAM4-xw3KJcJLzxCHebmMD1BpDcuyV9nRtoqXi07lDpbx5GNm_jnR7FfJv1-bOwhSu3iTXypl-V_hAo-t72VOPkRiaP6Wwz8yIlz_ImwyN66WVZrdRfW-LFCUD5_HgtMxQd0oxj5HU87uSMcimyx7Na5Yum2I_co92JXe-RESc1NRIMAsbd7880aTmH1pT0dLEOuDhTkpcj83qFTrHOCD1ubG6z4EVEx7j5F9Ikp_f840GlmcQVqHO84C-TYl6uZEMQ4IIVcjpzs7JhrFfZQvqSBlDQUt5qRwzU0J0zeI-vS7SPB_p-tUvhKtZJoMd9CW8BTNKN2NQx8SflHqEZesSopHVQSPrPOorg1f45PoqVKXbfaeoQefDaUg9JoBDQhtQePf9us17madQP4U5mIe83LZo_5EzvzbcDvha9AQDnbvPkxH4YKgU2nF0sW1ouIbs3ncaBiQhp-_9qYeP9upiUPIT2zZrh9_IwtGFKOmZE_gCY_HEGRSOvqCg8r4RCmET5slrLdyrqJ6CaqsZCc_9QzRDkePewI7Aupcg0KAXFSlGaJ-qpp09_y6_GB6K4PiysqEdrTQ6ptiw4h3m0N0bs4m_Y_7V8Cq1uc11AD_7V4Eisp8RTlXMSxY7lTvTziuWXN--el8jgy5yLq6uDdV8WBDCNS2XJtApbgu3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=Ana-AAM4-xw3KJcJLzxCHebmMD1BpDcuyV9nRtoqXi07lDpbx5GNm_jnR7FfJv1-bOwhSu3iTXypl-V_hAo-t72VOPkRiaP6Wwz8yIlz_ImwyN66WVZrdRfW-LFCUD5_HgtMxQd0oxj5HU87uSMcimyx7Na5Yum2I_co92JXe-RESc1NRIMAsbd7880aTmH1pT0dLEOuDhTkpcj83qFTrHOCD1ubG6z4EVEx7j5F9Ikp_f840GlmcQVqHO84C-TYl6uZEMQ4IIVcjpzs7JhrFfZQvqSBlDQUt5qRwzU0J0zeI-vS7SPB_p-tUvhKtZJoMd9CW8BTNKN2NQx8SflHqEZesSopHVQSPrPOorg1f45PoqVKXbfaeoQefDaUg9JoBDQhtQePf9us17madQP4U5mIe83LZo_5EzvzbcDvha9AQDnbvPkxH4YKgU2nF0sW1ouIbs3ncaBiQhp-_9qYeP9upiUPIT2zZrh9_IwtGFKOmZE_gCY_HEGRSOvqCg8r4RCmET5slrLdyrqJ6CaqsZCc_9QzRDkePewI7Aupcg0KAXFSlGaJ-qpp09_y6_GB6K4PiysqEdrTQ6ptiw4h3m0N0bs4m_Y_7V8Cq1uc11AD_7V4Eisp8RTlXMSxY7lTvTziuWXN--el8jgy5yLq6uDdV8WBDCNS2XJtApbgu3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از آنالیزعملکردخط‌دفاعی تیم جواد نکونام که در این فصل با وجود گلر 33 ساله و دو مدافع میانی 33 و 37 ساله گلی دریافت نکرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/29253" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29252">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8S88B8frreMUYoU-qg0avxDkxITMjySPnisK8nIkG7WjYF4JsN4C_I4zomA7kfFJyZyZoQHJ3Ik8qO9n_ZKTtLmRNy-mv8TVAXKUM6xoD6rhGuIZy5ETm3qQ5Ei_pjv6adNlzjgmrMg8QiPtB81_qsBbmvZLjFVjYSIXZBfNKgOigPHpC2TRRJLzF9MlFTMLci7SXuxd2g-e_-Sf6nTaJckNoXs9MvSlv8HcD3ZZ8PvE_JbpcPi6CMg3nWgYnAiJeiGKR5BMJah2Fv0i7fXuB8pppUDOIwzwH-pSDrF8G_B4c_X0qfhX5D1pFbioFe-cSwalqc2FigbHjMHdXiUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
اودینزه
🆚
لاتزیو
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/29252" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29251">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seAPzSDlUg2TU8fRVZeVmCbqVjhqmjLRzqxO3DIrSIw62byCTZXOvq2QQrFF9-DunlwCMLfca8-U4HQl6qMEgqWmxRNXBHjlc4W0i39AilRbEkLediq7erG768Ua2ZHa6iksu091Ajiq8umr-DsqeBxc6IL-pqZkPsuhOnZjMGrLZ5eOstpfAf3F7L1F37l70qppLALrjypffBUsHT0yRHP9s1W2sjIu4NKk8Qit6m-t8fTish3F-UifRncK-iffobWAu-JLip81-vExn0VcnQN0FXK6kIq8e2FBEVGbwWInT7nJ1LVKSoRlYDR5o1AaPsbdHjqEaRxGhcBDsoC7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمدحسین‌صادقی وینگر21ساله پرسپولیس که در پنج‌هفته‌ابتدایی لیگ از لیست سرخپوشان خط خورده بود درتمرینات‌این‌تیم با انگیزه ظاهر شده و از کادر فنی سرخ‌ها خواسته که به او یک فرصت بدهند و در بازی پس فردا با ذوب‌آهن به او بازی بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/29251" target="_blank">📅 18:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29250">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2t-v0NaqIf3SKTyCPQtvqeuMoK9opEhPu3czwfLotdjk970GJ-M-EcL-RKk8dtrPnO_S2qkIwtaLT80coIC9V7GiEDlYUbBqRiy5pmdX7lG_GcEVGlHq2-wXsnE5as_CgzOTkiILvXDaRwjit7d0n7uyheShPjCAr0mx46B5B6SiKc_2IH2MI4mvFiXMMdvxnNWCp1lvPco_3tqk02XtC4QoQMgnQr1ULbKxP2giIjJih6VwI1L76etvbWH7ISiNvQjPWSyoLeejBIaMdYO7mbAEkgO0d_tyy_q6m8ryYTdOqk8iH7Scoalf1J3GUKGRsvT08H43_QcHzP3IfjRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/29250" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29249">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AouSs_yRPFP9cZOBHf1fc1wU2rnGX1FCLiqfl6OX3R8yq3VE2pHGDOSmh1Q5b15pRJXm-91ekXNofaaBJQ-OCVXGwJySJhv3iidFi7wXmsGGncjq-YBkHgnMLANsyoGm8obWB__5micht3FCztOuHlF5qynF440gcuG8ImKcVl939e3sFt3J5bs-AAQOEk6otqHu15UYAHuN1tmO6exu78EmfkiCeMhRap_ND9k4DMOdUysnbL8d9rpOev82LFVH9YyKu4acsqYi-Tynoh1qZ9FSTvz28QlI6D047B6jl-ot5i8AnP7vl4LDMipFQe42eGskUaIo6W4nPPdevscewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/29249" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29248">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuGkYHl8dJh_-oM3xOvIuvIvvjnb6NOfV24cbk7fBkOz_gRWYC4KQp3JEHnph3Bh2aGVtjtc8kP_i_owAzqKZFJJBoPk-ENaMPW_qLku8T3UZDCJsVUUj21BlWuXVsc3ON3IkYh6mCgbAl_9DhFjBMU-G8VpCKIvETjrzkH-xGbytFrdED0KAPB_bNblpQWpS6wYSamMNhjVfthcR-j1VQZbodP_Ruvkbtlam8rhvKvpSgYgVJVzzS9A8kCNOm7HdKiHQ_YQLTmI_BiLMrOr7_TBVaonZgoTgvn0sRv4TUVzRLnbIvidncHsu18mJzxRJIwt1Ia3m33doKPw0u-Zuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/29248" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29247">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=SAGRZhoYdm2jA3vDcHcXveRDEakPwl3hbylIbCrcknJ7z8LKEWEKqBImtz_1HH1mtSNvU653LZ9yZGgjTFjnDWVPjQZEB07iPrLMdN1XmJkyRBYtHoTUUjAf5gBHpKsGwfVNA6Wzu0pgCoaZ7x81Tj1OqSRP2qpydmq7kB4YTIqnhqIILC1v_X6IKNi8C9NoKrLWXAlqdTZSEmC9oQYsh2q3SPwdZlyq5adwFaM9QxqZKfXTh3Fgt29MLkgc2EbXrVkvI0YkMJlQRnedPiJ5NnEkxVVQAzAohE5xcqxmql2jadvsJdE4dMgnLOpHuHeWNiK0_JsbaDq-jAS-_W43SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=SAGRZhoYdm2jA3vDcHcXveRDEakPwl3hbylIbCrcknJ7z8LKEWEKqBImtz_1HH1mtSNvU653LZ9yZGgjTFjnDWVPjQZEB07iPrLMdN1XmJkyRBYtHoTUUjAf5gBHpKsGwfVNA6Wzu0pgCoaZ7x81Tj1OqSRP2qpydmq7kB4YTIqnhqIILC1v_X6IKNi8C9NoKrLWXAlqdTZSEmC9oQYsh2q3SPwdZlyq5adwFaM9QxqZKfXTh3Fgt29MLkgc2EbXrVkvI0YkMJlQRnedPiJ5NnEkxVVQAzAohE5xcqxmql2jadvsJdE4dMgnLOpHuHeWNiK0_JsbaDq-jAS-_W43SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پاسخ‌کوبنده مورینیو سرمربی رئال به سوال خبرنگاری که‌پرسیده‌بود درآستانه‌دیدار با اینترمیلان با کیوو سرمربی افعی‌ها تلفنی حرف زده ای یا نه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/29247" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29246">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFRGl1kwvy8kspW149UpwFGpJDEnerF6nT-eKgDrL2BgCwE8ltgKlEliOMCEZrA9uExDuxSpANVJia6APf7wDfizgwZEEdwZagqU9H6n__G30V3zchDJz3LyMib3XRozdms4ASHEAwiePBiaWJyKiX-RkF9KHqFbKZU1BCc-SN0LCY_sHnmz5uR5hLcyzPMxL_7sEBG-bvPWgv3GNiHFuZn1Ma28Jojk9E5yrgCmL9SRyoW0PfIKFcoZwEBclG8BKPccpZsKNhjSaIx_29r4teYgwYpXvXJCtqLyL2ZupFm4p-2hSOigf8l3oZEMLu2yQZA6F-XEM_NpCCJ-LMjrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/29246" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29245">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=InzmYvz36QuGfdJBm746z76hULChSd48b2DmEL532O6m0oybl_ZdG45cX4nEi2oX9WtvJW-J5EWLkVBKDL6w3d43lNk8wAkuu2DqDOE-877nxSgAQVZ6fQYGi5fBumpm-FSjQTXQxCh76Fv_mLsezQkfut8nuqwQNV9lvf8EBLbzIRWedbePnSfQ-8A-IVyty09yKqfNOO0UW8PfBAu_Q2r2FINlzP3D3nUCIDaKw7wpMIvVBcO6mktfWfSzFw7J_KpvDq6U-gvXYkqWwBGEmRgVQ6PInTQHY9ko83Ywaw7C5kVjBxd8Hp9SANrey5wGXiwZOvQyMkGBpsCm-eLy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=InzmYvz36QuGfdJBm746z76hULChSd48b2DmEL532O6m0oybl_ZdG45cX4nEi2oX9WtvJW-J5EWLkVBKDL6w3d43lNk8wAkuu2DqDOE-877nxSgAQVZ6fQYGi5fBumpm-FSjQTXQxCh76Fv_mLsezQkfut8nuqwQNV9lvf8EBLbzIRWedbePnSfQ-8A-IVyty09yKqfNOO0UW8PfBAu_Q2r2FINlzP3D3nUCIDaKw7wpMIvVBcO6mktfWfSzFw7J_KpvDq6U-gvXYkqWwBGEmRgVQ6PInTQHY9ko83Ywaw7C5kVjBxd8Hp9SANrey5wGXiwZOvQyMkGBpsCm-eLy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/29245" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29244">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqcSUNvtObRTnT1oxXVO4JUvlufU27l4bGoRWpdQ19wQ1Y04n_Un14F6Vuv8Zbj2LXI-4INDZABKbuEPt3V6IsL5TW5CVxLOOOURfOSATN-obkn00gGfq_ttnTPttBEdGDNYRGmti9ooOrd38YgoDHR2GG-P1Q-rQLlnsgts9NRncir8_OUNpD2ivIFGQkMTuEQiQs_NLRUruTwO4asIWSlsfm6WhXDvKiNv90VN9g766p1WG67vj6dABlldhdLb6-kUXXJCb52936fiQL0rQS-XKeKPWrNRPp4SrshkhL0V6mobdLeaatXV9UwA_MiFdDeE5hsTaSouxk8wCx3uTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد خیره کننده خط حمله بارسلونا در فصل جدید لالیگا؛ به‌ثمر رساندن 17 گل در چهار مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29244" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29243">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWp4kgeALQiXE0I9A6L3eua3kT1v_UJpeEOoBE1fzygCf3A_bmoUK1rcFXqWhgSTtCUzXKa4UPrFMg5r7Rfn64GHRemVdIOYklCFqR_NbY9TgeVNJpkwU6w4mhUuMvuZibP79k5BxfEDnG7LYeT0ySbezmhPs6T8aXwa4j64hMNA1uSxD_yumDV1G9qlMHXy3Y98gM7PxKUvxn7rHxZUQNe7thZvY8YhXMhBEYepN896L9e4IzMmQEMQrQJVitECMEyjbVgDa6CxAM33weu5ozfTUNzxzJ3eqN2b13PcCZMUMKv3kpyJ21g5ZRzEFPhP0WBSNSyvC03uPFiQ5rkp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29243" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29242">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMwLTk8le80D1mXLDHkW_LQw_CPVIRAM3ckmC4PdJ8Avaxx6fkBP2tCQ4gSGa_VJB_I-d1Z4dEYLBUmOTPb30EGDVkGURcVv2gGALbsgTXBthgLxYcrzkbbssgbWk3EbjiMbc9CrZIUw_TExMa7oBlcDJQNQzxeFk2SR8ZaScXIg23NHWMj5ndr_ciuinm5B8CsNnR0MbeDSmiFgQ7-k_7S4II-gc1fuCWLdSuPkJ0ezkhkzfIoha4eyMkCAYV4BAx9cD9DFviJpEK5p6aZiLWo2CS_XrsET2kk2OBGHMRgdTlkTd3gMw1NeFMbSHvBBwEscnf4EPNgQxui57SCyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29242" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=psCkIW7zgUn3FAfTi143eef1yijUnRHlvmcIMW6zuHOZGCyHJCP7UmXXyGpzvMxNEtYT3gFQiktc3n5nLuPBAZeG-vKurx1tpOFXLofdVmvTKJd5jsg-h7-Fwy8WesIwFAY6pSvnSNbGQbt-u-5dBWUBgMHDZ8ryNZfKNuUjU29ElHZjGqqTXYRJpcgqr-D5IJpffptFW_UnQ4wJhsAcsZ_rCD51ujfLV0gMvD7ldNE2Dk1erz-wGNUtIWeZIOquQOeXUAZY2qsj9gMAZvpVEzoQaKERFmlG254vEnCKYy6WgktlARVuqUDb4AfOFe_74c4KTnMZWCIzSHSn86p2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=psCkIW7zgUn3FAfTi143eef1yijUnRHlvmcIMW6zuHOZGCyHJCP7UmXXyGpzvMxNEtYT3gFQiktc3n5nLuPBAZeG-vKurx1tpOFXLofdVmvTKJd5jsg-h7-Fwy8WesIwFAY6pSvnSNbGQbt-u-5dBWUBgMHDZ8ryNZfKNuUjU29ElHZjGqqTXYRJpcgqr-D5IJpffptFW_UnQ4wJhsAcsZ_rCD51ujfLV0gMvD7ldNE2Dk1erz-wGNUtIWeZIOquQOeXUAZY2qsj9gMAZvpVEzoQaKERFmlG254vEnCKYy6WgktlARVuqUDb4AfOFe_74c4KTnMZWCIzSHSn86p2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/29241" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29239">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRXvq2X0l21yuyATjHYsgcS0c1-KdFU4Pg877WJWO0BwvQJI1fcIjBLjwdA1wE0bTyzbkNWnY18o1tySP5IYDkjrMiutENYetg181Edl1uXh8iKKV_VNi2U40-H5APJibup9LOD5Rih9EZnT5BpkTUVPYfk_Jzic5vhTOvkPGxdmG_Ged2NQS9EL1bUAFQhcaZkJY_g7rKHq22SprIWRsjnbfIzTXF6oEaTpK7IhluwEzGJf0cbaNn5vgrKsK5uKR45OcleNyMPMVSysCARFANWLENXuBQgp6RlHJ58lyQ-euHf77TVW63_1AfM8MhRpa3legPeXxPXY0jonpoNNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbZ9Vc0R2sDwoMZMTpbYrlR6jtDF9vwbQm8n6H2xepZf2kM68Ju-fnPm8twBR3CGrpF8bKs_Lspg9rvuhfFxJQoDn0cdvXhvLIPl9YCH5c92Goo8o6KjaiKVVZTG5hZyuNktVk1dCuwaHmZ3yUHXn6NdY21j4g51-bgXhDZMYh_qQ7wSUlpVQhx81L1PUi3PndjUMViBoAnx1B-_827cyyCn2GOCNN3wr1ggF98cLSG7ltouDyX6tc13yEGi7VIs8N89RQoHoikyOkjAIEDzXLLqfp5WrGwywikZ-yRWPcwIoIKaWNUTnAu5-8KYPiNBNECqBr5fL26d5MT-h3-FAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
هواداران سه باشگاه اینترمیلان، آث میلان و یوونتوس که مدعیان اصلی قهرمانی اسکودتوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29239" target="_blank">📅 14:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29238">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEpL_iXzGbSbghExOkKK80cQ279raCF_bVuqzE2tmUqF-HjDf05eZh727vYiZ6nNbidk8KmXGFderbDC8oBpMDfqDJzOFLbhbJG9bTfR_lLZ59sGh5GOcwRm1NTEuE8S0q-dK76FTapmKo1Pkl1aAEngi4F8_2EcM9X5nz0BnOWQ5xapcXM7LT7rEdBZMdTQiHFhmEIEsIiSot3qFx_7w-Iene45DVrmgxGmKcsgo2mWHh0mA1lJsKt4DKMxx93dPH5DwnUqc4ocktrOqrnn7eli8qaewuMFxy2Yn3lgpcHsSQJTH0tOguiFJ4IuT9b18GCwypjiEPqh9J1bNSBaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریهTYC اسپورت خبرگزاری معتبر آرژانتین: لیونل مسی و رونالدو به‌مسابقه خداحافظی کارلوس توز دعوت‌شدند و ممکنه باهم‌همتیمی بشن! فکر کنم این‌آرزوی تمام هوادارای فوتبال جهانه که یک بار هم شده دوتا گوت تاریخ فوتبال رو تو یه تیم ببینیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/29238" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29237">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdLFniOanN_ohIn8KrBplvH7VcEAB_TfkyzKc0QonAQUbQt4XENYRm4QjkkYuJFH7pScuNORR4A6PwqY1mv3bJMytOhs6HfvGSVEJ2gYcPBpgK3Qx1f3D4Mx-rIX_Gk2IWxDUYJlq9C3Fz_dKUu4StAgz2e83L41CEoDoeHyAg-V9wdesZ070Om-_g-Z2xzhoqkouEFxbsDse_lmvxFLdbWEOGg2DPyOWHsRPOunQo-hFThXPKqhOAa1lBQ2_-ode4OQThO96-pizhStFAtOZ_JI0j5i9_iPElTyTB62h2eItjapyvTSVR8JAzMh8GMzlLL9ynFwG8ooSQ0DyAoo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29237" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29236">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOZiKJnovxWfeqhV8WMUPUW3y6hvF4ov5_fpX-vBsoqkcJe1d95w9AbLTmJLCg5c3sLoByAIvBXzYW7z7RO6VGXk3_-Rc8DiPcmdmTVfri-cV4k1CdRLkwtbJkM1wRU-WEkTDrn6CqqpE5OfHZnT_ikbS6igwIwdlohmD4H1awm28HgFHpw7DiHpwBuZB5P9OZebB-3oywxH2fCHhdWCBzOFmfVrQsPXWNUQE7NmXojblxvYBaOOBubXV-nPn9ekJ8J8ZtDdzgpOcA87KVn3JTtw_RwTS3NxICdr45GxKOUVGP0ihLuRGi0kta0FH5qqhT2elZBG1ENrp6pk76NNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
بهترین‌ترکیب‌تاریخ‌لیگ‌جزیره از نگاه نشریه سان باحضور کریستیانو رونالدو فوق ستاره پرتغالی دنیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29236" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29235">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX1bmDak7KBbDC-pWi7072iOwHXYlDHRU3IwmhaWweC26s7c25cZgjva-rEIRw2puIRyi9Oa5jXVrD2a14wGkefq0h91HAsDbxquSZLIDq9j9O1y4SmMkbNIr1AJ0h6ON7tn0W08jDrR-1xnPZWbJzj0FNoxlYLUOQXRyQzyq_KTSadjMoI1gyooCsjyNhplzGRGnA652sLoKfncbVsC8IGnCSIAoXyTLxzYnvrNSvC-cbdJj24AZ48dw2ZQfeo24iAU1-P4hRYVWkVLYm4j6akCuZPb8OaN9dvx0ZCTPsX9oGgZTeDKi6sumQZ6bdw33PUGtjzDRSkqDGBd8TiytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌‌مهدوی‌مدافع‌‌راست‌20ساله‌آلومینیوم یکی‌از بازیکنانیه که قطعا در نیم فصل راهی یکی از سه تیم سپاهان، پرسپولیس، استقلال میشود. مهدوی چه در فصل گذشته چه این فصل عملکرد درخشانی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29235" target="_blank">📅 13:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29234">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg1TfS2_X37UlrwQoOyEXG5Lz6t0Mo2u-kIDPztvgxoyX3i2cs5Vf9svM-AFpCUPr0-iPjRNuNo5yzxtCTzH3c5oY2eA8SIanAauV35be0f8A-Snv5U_BUttMieecC5s2dC4DoD9Fm0Jwze-l6p5YzGtT6V2H10vTxpQf1VMIpQYiOOFw6XTL2sLV6oU3XBDbHYxpvIYVBzuM63yuLHArgmsyffTzEThhRlnX1ZPqnDeN80JStXMCSF1sXlU55U5U3bzV3lqIR5PZpxiV_ZkOUiV00MCiHZELfs5cQrs4DwbiRQ2eU2ZfSosN2mkKU_Ak42J_dNkylpwuUBtFX1jDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29234" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29233">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTKQAEesqIrI-QSv93cNyh-pFn8sLYbkhJ8T9c-HmjihNWCQK5tzT8gb5oKmBe5BQPu8bAL0H3u1K75RWvkFF_ynw6pv9IDxm3rgMkTBEjl_pOHKWEmLwXwEKBzOxuEGisXwyx7QdlrPeBWJ7OA1CPuGoKswn4hM-TrbgmxDCAFQEe42_VfyL36Q-1-3UMZqrA8rbbG6YDODzyYLGKVaoJSqvSxI9iZbOLFhwaW2uKM0PeMmLJGvSFozkiBpAvfoC0lcw4jcStsfF7ISnbtCqL4TVh7fSzfN4v6__SoFFzPyt9zpunCUf-gUfFXHO8LtuKbv4Gw8mUArIgjU52YRq0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTKQAEesqIrI-QSv93cNyh-pFn8sLYbkhJ8T9c-HmjihNWCQK5tzT8gb5oKmBe5BQPu8bAL0H3u1K75RWvkFF_ynw6pv9IDxm3rgMkTBEjl_pOHKWEmLwXwEKBzOxuEGisXwyx7QdlrPeBWJ7OA1CPuGoKswn4hM-TrbgmxDCAFQEe42_VfyL36Q-1-3UMZqrA8rbbG6YDODzyYLGKVaoJSqvSxI9iZbOLFhwaW2uKM0PeMmLJGvSFozkiBpAvfoC0lcw4jcStsfF7ISnbtCqL4TVh7fSzfN4v6__SoFFzPyt9zpunCUf-gUfFXHO8LtuKbv4Gw8mUArIgjU52YRq0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هایلایتی از عملکرد درخشان و خیره کننده لامین یامال گراقیمت‌ترین بازیکن حال‌حاضر فوتبال جهان در تیم ملی اسپانیا و باشگاه بارسلونا.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29233" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e15DdND2eGL7Lk_VkwazpS81x6dtWIFHwwTEwumyHMm_RAZAqf-Ah3lW5r0rIdqohZ0XL9QBTU2iizjCC1BuEpY1wm73vDnbcZynn3OmS1CphxdoiZ9EM9lZhe3cpWEsYTeh0q_oQhH2GF27V_LExiVr2l_nC3YKZ2kxnBZhR7JQAC_XJzskuz_UU4q02H7mM5BLi6XB-4C7ZKCoQOJXajwyCK1wUzhxP530v6355IJHnFToGmwggB5jO82VmTivmPWyUnWErUuFf83piMjZpNxzf_Ue_xhYjpCH6QQL1g29-tvD46tBx5YqZmyJCc-rcx1kY7U0NBEFDLTr6PwrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
پرسپولیس
🆚
ذوب آهن
🟢
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/29232" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29230">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3RTz5WxX5zol0P34WZ-pH2QtrUVyZfv0XQIT9HH1CUh9nrQjSdvl1oCS_KAE4pmy3lp_BnAh2c2gdFaYp9VF7pwV3goA9dzofKMS4ZmxqGl1VTzO0S_IsCZ0iOyVXNxvK_I7YwixvpQfXS6rxKhy8yqrCXUjWBeSd5o_SpRLgDVbVZ125QjGW-KCYz5qwE7Kjnl0KcjoL5wS2dzGn7WrAbitLELC4B9AQlyM3T1v-YzIJqx5PUMR3t6OGFk1f5Fx2DB5lIMqUB1HQDkNCk_OcWGf3Kto_eVhXlBuWxl9Ka_Dg93boXmlAZHKPpOwkn7BCgPfIrp4aoehUpXdimcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSxpTk3c-tXQ5GkeE4nswxIYNXrD8-wjzV0ny67pnUgyVINWsmaPJn-L8IpJEvdbcHxYPaupdLzRp7BKtIl8ouMJDVxN6zax6CqNy-WuaKVll_pqVTVi1rkARqgr-tdvh-bpehSS8OehEAZTmqemYcYkPi6zJbYa7yy1wliwZwRxwh4wV3I0AnpTsvje9gpAUXnowbDph7dNseZ9ikSIXK8MXULy6J626nSkDyGawViwz2H3iPA6LLcIPEXguv3Tz1755WMOvI7JF9y69QDQqVMuC_nGaI1trvz3NtmRNXzsmgTOEZjV3UTKxIby11MpqXd0ojAsAiPWFLvCh_5dzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
هایلایتی از عملکرد درخشان رودری ستاره جدید بارسا دربازی‌روزگذشته این تیم مقابل والنسیا؛ وسط زمین با حضور رودری و پدری بسته شده برای رقبا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29230" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29229">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LysngS0pVBxwzDapt0kkJNnpFtJqF7wk8KWpvTT4rzUvEut8FNRcMX78dY_8VbymclS1vWoGoFL7FtXyKV5hbYTqVvfUVnXzSR7kvMHPYpVwqznCdyGT1dTg3pTLvn8UNwTEhGt4WB4kBt_Wjr48dyhUCSbbnCRBX2ONXHqP5gOGO7ED759tirpeD8J7iUc5bCvSLGPkb45veMHgfj8Y41BUip1I_yibXLXdjsAu1xzwNKniuzOnuc3py4LwvT21l8wF0RnspeGy1NNpbBEvTAW3dkGJsnh_VRgARe8T4qvLSMqM8E51h6NlAXQVmhm37qPDxRuDIHkRuQTlifQ94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29229" target="_blank">📅 12:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29228">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN7HTglgwp1zqS0Mrb7VFbyEtF3n6jpEP5QN1MrJN7HaKYsO6aK4_xvBbyCeOchPy0mcj-AJeUO0ZCJATvRKumMlMnOwYGeUuo02tbExSdHJBxAXD87KLvXn1t1wb2s29OUqq9qNlaR2s9fKnX2o-ksNZ4OwpzTDmiHNHyL7Br4ieMFTuQAD42tuUkP4-KSItF095ENi09GiYOa_kbH7iNqDm_G-45qLR2-xVv46aINDhhnttfIZqI_CHlvUB5py1-Y7kP6rMns0DovB_Mruc1urFS1q7OINt5k8wEHVZmHZpTAZp4q8yUbqU3R-RoshqJAuGT2n5T-IcYB5p_t_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
آخرین برد ذوب‌آهن‌مقابل‌پرسپولیس به هفته ۲۸ لیگ ۱۹ برمی‌گردد و این تیم در ۱۹ بازی قبلی خود با سرخپوشان تنها ۲ بار پیروز شده. از آخرین پیروزی عبدالله ویسی برابر پرسپولیس هم ۱۱ سال می‌گذرد و این سرمربی با ۱۱شکست‌مقابل‌پرسپولیس در لیگ برتر از هیچ تیمی به این…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29228" target="_blank">📅 12:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29226">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29226" target="_blank">📅 11:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29225">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNkHjwA_RQY3_3vRdsgNIMwQ2SJywpwoSzbKwUFkyKpFiobA2y1Vy6plnKo7I2ASA-AmrSZ4i_wFVFW-9dB3GxHWiN7xYqD-1lkI4Hv3WhHUOy4q5g9qGB52vGyB3Ue34SIsRTCxb9Z_0l5cUbK-5CBFPySSsxwOQWfXwdpIQM6HLB2jIeEoGtbnycxRbrfJkLRGlP-_lOZBX5PFpxDIshsoxWiJIrQBtJA6xy3jnzM3DYgsjjvCgk_cg0AvQ_3H1kwZM_fwJnYGq8dItcIHNoocOeempvB7a9aIxGvDtCaCF_mthFaKEnG5YsSn4iWW1fEVI_C_Bu5yTxxuux51tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خب‌رسمی‌شد؛ ازساعت 12 فرداشب به بعد بنزین لیتری 10 هزار تومان به مردم فروخته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29225" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29224">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvAHNna7DDgzKI_xsan7UvYn9SJ6ywgjz4uV-16hKXtaoQHlGPH4k6NQz4NtIlpomgyIi1PqmZI1deN4q73mZA0D8FYFAAnQ-ISER_JB_iEcPPbZBRSwsGtGbbedul5nn5Eb9vD6KLuJVxgbXyvkXNAaaZ9UzBFpt1HyjXqgdcPv-xIX3FMbIv1zMxI-Wlgm3w-7Y6Pi0xPt84fOUGJqmI8eF7s5MSXgyr8FhkKQXVYiW6df3UWsGVaAKcftkuZkDLDLeobE2-o4KhmmUJ5ISk5errFX15MsN7wzcno0XRrNgbLSc9vbX2fDNRY_Ng3WaPgr2AaWuw2Ixyn_P2ZmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌بازیکنان‌حال‌حاضر فوتبال جهان بر اساس جدیدترین‌آپدیت سایت ترانسفر مارکت. لامین یامال و ارلینگ هالند همچنان با ارزشمندترینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29224" target="_blank">📅 11:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axyBqgkdrHKZj-DIH76jkrPoiHJxoLlhUTTO_nrJx2QikC59hfLQ6JnNlRTsL8iKWILUojHwQogy-Yx2JxxFIqcOQq2va8AsHM8QGuLLzE-57Gh3aMLeK507Dip5hgMHRpjEXYineXIqNaJ4JOKldRHdH1-uQR_6kThbFvCJ_3fK1qrVuSnadQCOF7Z8yeS41GwkUu2Q4O7CUagNLpz9ErRul4a9GEpQOOHgD0QTsXnb4grTMyyogMxwpn9zKHox5Bc60M_s77Ao9Myzmk6cONNb8OvP8JjWAM8snhBwrXVK3yaA401kxRcL5EqwIDgbQs3NlbpDeBtsXl5HkdXfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اردوی تیم‌ملی امید به دلیل کمبود بازیکن لغو شد و شهرآبادی، لطیفی‌فر و ایری سه بازیکن پرسپولیس، محبی بازیکن خیبر و صحرایی بازیکن گل گهر که تنها نفرات حاضر در اردو بودند به تیم‌های خود بازگشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29223" target="_blank">📅 10:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpa3xc_Csht9mJk8VBt4xQG7xJ88PwFHVGMGXRgbq3pOeUJXd74Sj1CeSjgUP5e7RNzgFC9w96erD1gGCrAD9bGvwMoBfLeGkODmlwqs3Q-9weufG6Yv8cfKgCxSYCQG3iPLqLU-BouhWYCBnTLV7nTmquaVN6Fr7gq1oYyEU3XNQBCa3J48S5wnTxe6EXXFSyonusHF4PCDEnlTAf-9CWQFg-5ozuT4lguq583BlnojCBZbfLk1ZwWZbCSSTfH2PVdS1Kv39zsHYNGUoM5cN5Eqf0gLa6kDvC1R8fYAHkxbcv6r9OG16wUTF-kL7m8XPFj5wFQpCbVY20EsMeqtFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29222" target="_blank">📅 10:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac1rlSb2LbTgLIMwQqJFUYp1_u11puGbA285tqegTFjCNJjFDH19_TpViZd_Fu-OvjtvVOlEsJr31l_wX2RSDNmU8brVv-pqGjNaqKgvacyczDwD8wElVle0EyDme5iBbRFamNkmA-JIJ9Yq2a5XI8KpJbkQVz2uGvdZ8NZrEeoqLXNDvwoe4U3GxEPNFn3SfvQdkFjViyVqY2AjI_gsGwmNNpxjdrOIRZVof60ZDsvBTaWgM2XQUnNEVu6wxgbrLlLf9spV5b93WzcCLlE5wuiCB6tUd2NjVVLzrIqLvbZi57tPTmGk8_DCNdWftmXcSCKvGtyza8s65xPTrhR8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29221" target="_blank">📅 00:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEbvW5Tg3RL08lI3JILcxY8fHMIlYEmGe8_WN_XG0_scekRyZiWcX2yru5r2ruuv5i2fUBzr85varHstG-pW5-qkd7ARhCWMdsm5_Ok8VM0Qwn0PvlIW74WT2uBMNFwAffs1BG7Uums21QNPYreN_Q_BVvdd0EO1ThZ63JnGwbLkR_VlsOnyyvhZs_8QSigVaeohLpZZqtlZ_RyH9Fd7B-yEXKZZNGHB3ui9_xoglxx1MZcWYE1jrZurVEGKE5l2Jn4pZhjpv5OeaFW1b4tdGH9xTBWZPDIByzYQFkivANOVhpEgZTyZBlP1XNks3HG_y7NkUIGH0wZarqtiZgieag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛مصاف‌شاگردان‌مهدی تارتار با گاندوها برای باقی‌ماندن در کورس صدرنشینی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29220" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smq8grX4mi45Bi0jeW-BLVXWfDNv-j5UzK1uOQZGFsZkif2rc6VpE1RlkogR7xQRMsA2dfqguVp3HJjLskem7QVnQdtwK19ImVWtRUzlVrCwL7jDF-HDmI6u33zYYWEJ_v_NS66UIRvFdtWPHlfDNQWoI5sr3CYPyLSmxvqSJTVLIFNkCH8ZS_Yy0JUkC8qqyoGOMa-uBaJSt7GnGvSgovkCFJkZaBVbpOozQL4lmM-77STSF4xY00LSflWelQHy-s8oLHJOIM2NjFywj6Qwg76-QAnmb6kJvAb9nk7ZpbXuEOoilaOx84QNIAu_NuFAVE_HACv-gJcQwml4tzVnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
توقف‌آبی‌ها درشب درخشان خلیفه و شکست‌ناپذیری‌ادامه‌دار آرسنال دردربی‌لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29219" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29218">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HacgfpdhovjiG6_RzO8UYHkaS9xzzhobo7MiiefW6ceZjXAej0GJ_E9kt1FOUbAzEDY0KzAdkazYn9keNdEh49Zh9cn5VePKI7wY2HHzqnRhckmTIeuBxmRZGszVZuPqLwLOrVZQRNu5EUicSO20c75vKL7dL-XfSYDi2leZ5JSAKm_hwYCDZMuplmpwgVQo5RiEcEjwpf1ghoe3y4xEH5T0blIjMCx88mwAlBc4nKvK97J-ffYGsKlQ0Id7LEAboYhEI174-_Z50u_MHhoFDsnwUVoOuM_eXSw0C1wGSDEXaCGZmXIG5pbXDk4uIG4Ko2aCovB2fGWZAokbT_2m7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
بعداز نمایش نچندان دلچسب در بازی اول؛ محمد صلاح ستاره‌مصری‌ترابزون‌اسپور شب گذشته دوگل‌خوشکل‌برای‌این تیم زد و سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29218" target="_blank">📅 00:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29217">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSRrrV8aY25PJ2VS6NqFFw7ioL1eTdliuYLAN9OPaXypxKw1jMwKXTrXcuo-Iatm8K9K6-LLkjibee43kQ4d7O9Bkg2XdbEbByLxvVzi9rrYcsx6XaEwQPFcRvrDXrlXGgrGl1rJGZlUHLy1c-GLPnkcqXlvnrMmUw80GDh_9M5bGAMqMNqVrZQZZwd7ORNVySWCnsrJuZXC0XjcUS_zWXFjR_kVGIVQHrBv5pm9roqLaYltDo95LoBL8A7kLuFBrDosLfxUmBcSTdpYSYp-NlBFX4mPycdEy9uqDmEELgccotVWkHsAaJ5Sy0O8DavmuF1gMbssgrmskwtg5O6zSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌‌سوم سری‌آ
؛ شاگردان آموریم در واپسین دقایق بازی گل‌مساوی رو از بیانکونری خوردند و سه امتیاز شیرین بازی رو با یک امتیاز عوض کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29217" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29216">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGlBVEpb-ll8KApmJ6B9oUqURvTXxCB60U1zDW3NouoLkW8E6rRglyUvpGX2cc9V9TI6fYuauwzXhKcDHb3a7PYWjQVz--2No2P1do0X9DIEBloCRpQKwMa7HqAKlkQ66s8dbSfDnS_UAYBGfRPk_INABoBULYcJL-ylqwZMwGV7Bcarci-nIjXOmiZqHQrUOTgpm2dxlsOKjQkHb_OFrOLpHL2DEzIcF1CLnsJ4PXfJ0cRFtcKVPzKaQjajTcIFKr6DwlLsTxg3qTL_i3_6U0kIfiXuftvkLgo2M8quUjowgyGz28Cl6JX4biXoKqOwhi81LUdAC8Po0u3TY0dhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات لالیگا برای بارسلونا به یه جلسه تمرینی شده! ۱۷ گلزده در ۴ بازی‌واقعیه پلی استیشن نیست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29216" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29215">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=o94oAkqCR0eQv8--4lqhPge2fBKu8x_Yfj6KJifEQ1wgA8t_hOTqnGgo8oTepV8CBVLjj5waXYdOCb9h6CxJfcoP_1aZGyapLZtNemj-b3KHYPuc0eKIxALOS6ArVyRrlw3jPAVbp8KvvXsyqgGIi_A7BF3iepWd3lp3qywnypV2nVE_mjybqS4SFVcMaqE5Ee222luXoV_gBjqyrmKFXP9TTrd3iyAG0Mw9lW9gqkJeslyg1ikvGGM3L2ljoBn0emPR9Rva2CqgEQumwhHaHXrjrmjQfN_QQ0RkXqQq5gPDOtoVJJmsbH84pv8PyZE5D7lLOU8VLllwBYAqcjwIfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=o94oAkqCR0eQv8--4lqhPge2fBKu8x_Yfj6KJifEQ1wgA8t_hOTqnGgo8oTepV8CBVLjj5waXYdOCb9h6CxJfcoP_1aZGyapLZtNemj-b3KHYPuc0eKIxALOS6ArVyRrlw3jPAVbp8KvvXsyqgGIi_A7BF3iepWd3lp3qywnypV2nVE_mjybqS4SFVcMaqE5Ee222luXoV_gBjqyrmKFXP9TTrd3iyAG0Mw9lW9gqkJeslyg1ikvGGM3L2ljoBn0emPR9Rva2CqgEQumwhHaHXrjrmjQfN_QQ0RkXqQq5gPDOtoVJJmsbH84pv8PyZE5D7lLOU8VLllwBYAqcjwIfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی آقا دایی هم عصبی کردین؛ واکنش اسطوره فوتبال ایران درباره درگیری خداداد و امید عالیشاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29215" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7zQitr3BUZgB4qClmsPx6rh6fh16CWap6-DroYaE2G1FkXMOAXV4GZyq4fOxBvo4aS0kg8mOOWLoyQR7407uhPItMnNaj6r6d_OGi14nDX1IDMy3fwJa_HICl247kCN32T85GNhUoDbrgHhkg3LaoJJ0k0w5QXgiEDTLoRMKTNIPrj8HtQHn43pviCUIzcVhj-71Y2ZJ4ZPnBlPNGmw8ZrXnBOu1vgLVpHWLp8ZYzPwBlBgvqbCbSZtpSt6PQU5yUogy8Zm6l3TgkBxYFsvw9MBT-PIJKOUGYCXA5hmAFHdN3oR6TSvGTx065THL6m3osYgJIjcgPWhzJJGnKIUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیروزقربانی‌سرمربی‌آلومینیوم: کاری به توافقات بین دو باشگاه ندارم و اجازه نمیدم خلیفه و گودرزی دوتا از بهترین‌های لیگ نیم‌فصل از تیم ما جدا بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29214" target="_blank">📅 23:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXbjuFFRsA9FAkNrwEDIRFHiFvX_snH5AJcNYtKmVQcGdRz4uGtGQRT8Dk_xcEbHP0cr7w8txk5du9QhLmejcXRUDwdHCjUtaVXZOQYzQDFV_CyBwiMxjIgUhqhQeAYw2hcWyk1SXzoU8wGjXGObvZsKRmSP5JsM4VURiJAzknzgSLcAFzklDQofPllX1DI4DYDe_zRVgzakQ-3mwZ5v6jGpeY8ro36K_SYlOoT__Nsn0MI55RKDVL8jjQe-5qK5ukpKA0ux97trB5OZdq6W5czlYTLEYO-aGF4fa6W_ouGNuaRAxxi3kbf6zz6wC5wv6p9CTb3cmXb3Nwdz3R8ojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29213" target="_blank">📅 23:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29212">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=jFSnoMCH0EgkskVbbBSQpb06jjRwhAS91mKd9TponRnI-eVIZGJ0-q1crBAeB27vACuBgvxuCDuj-8R1jnbDXKfASbVPz3QcqXYW5P-CmBUeGvqJz1F-bs2Sku_enTzfLi6LYvKui2iNGua-53PL7gF7gnL1hjCekdeZ-ra0OWouoON9HmEJh-v_Lbx05f4BF2FZaqG8Dm_YiGTzQFSmO8V3GEFDROctkYtOYbPD9WeZfq-3zxTg6pps07ySmWdgQtsTCKfqGxhupkYjwo1w0AjxBucvcB5Xpw29N9_RsR7iDk16ecz_lov3uR-H6ZNXpP5tv3YeL81TP14srUHDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=jFSnoMCH0EgkskVbbBSQpb06jjRwhAS91mKd9TponRnI-eVIZGJ0-q1crBAeB27vACuBgvxuCDuj-8R1jnbDXKfASbVPz3QcqXYW5P-CmBUeGvqJz1F-bs2Sku_enTzfLi6LYvKui2iNGua-53PL7gF7gnL1hjCekdeZ-ra0OWouoON9HmEJh-v_Lbx05f4BF2FZaqG8Dm_YiGTzQFSmO8V3GEFDROctkYtOYbPD9WeZfq-3zxTg6pps07ySmWdgQtsTCKfqGxhupkYjwo1w0AjxBucvcB5Xpw29N9_RsR7iDk16ecz_lov3uR-H6ZNXpP5tv3YeL81TP14srUHDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی‌لیگ‌برتر درپایان دیدارهای امروز؛ سپاهان با همون تک گل لیموچی سه امتیاز خانگی تقابل با آبی‌های خوزستانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29212" target="_blank">📅 22:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wxlo6Hnp-fKz7a0CEdhxWNj_hYHdlWP_DGzAT8_KKf0LRWb7VEbrEcbT1kFsrY3EqQtSD4wGfF4xstyqilXNwzyq5I0NFBR7eJZQL0_c91h5drKnOiuT8waBixygtKjoRy0fTuFCkbEPDVjjlSei-JBX_3a4__1_D9_WQXnyAxAw7cXxwxXuKo9ErHV1JDMmSdZkpTFkgx3vWW8TpcLAwiooZIikTfIhjNZgjQ665KKiZqo7QPzNM9UKlOMLcxt8tPk78h5jco3hLzOOXs89i0f9QIm_g7n2nSDdEzeAu_ITyPSbG2lifOjj6517kJ_HW0dfADWl-1AEBDV6-cFijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29211" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpvcum0XZ22ag7c3fYK7gC08_4nKxD-uQ8rDhWF6PSDCMxt9VyP4kTeFrsfR9ivPMgxxBv_5tN5XdZntC6E1kCqv6uNEW74uXxeR36rDyxebiJq11RfKorR_AOWRkaD0bTlBpa6jEUjrn8slnw_zZzbJDfkMdm7rdHhUPrs8SibkuhCbU1N5FPwr6rT7EuGkXH07xtPMX9VNYQ_vwV6sLf_udSfZA2oKS1syz_9TkpcYkqGoWs6Z_aFQmvJ8m6NWN0hqSnI5Y-1OxL3jUJgE9trab-y_HiT2eZ7IbRJzI1qFwIrdDCbblaG8tb8RAD6_mtAhBscggjjzf-T3zbuSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29209" target="_blank">📅 21:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=c57Pihw4MqapasMEKqE7Z_YGqw721IM7djYrYB_eyLVtmNQOUHlVS6QRHRuE-9Qsc4JISKg9A1huSrkoK-6yawCddT-Sw3_pEi1B--xDN3aHYO4tuUfd-Mh2wX3Xi-ChvbYqkY1WReTQIf9JF4xMM__JR3Vqh26BD3SHkpiTP6t5genFbR90bZUj5U5zjCDu45R5SRx2GNAaxYWUhVYr6ks5uWO6vkZRklFANrE05uPx2VSoK3Sc8mdOR7tb9EexUlFcxbeK16yQWnQtoxq0RMwSLR2bPv67KoMUY3jU9ErUPZhQvsvLzmaauDLbW9To2ZmlHSkpnDRm5elb6JPJxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=c57Pihw4MqapasMEKqE7Z_YGqw721IM7djYrYB_eyLVtmNQOUHlVS6QRHRuE-9Qsc4JISKg9A1huSrkoK-6yawCddT-Sw3_pEi1B--xDN3aHYO4tuUfd-Mh2wX3Xi-ChvbYqkY1WReTQIf9JF4xMM__JR3Vqh26BD3SHkpiTP6t5genFbR90bZUj5U5zjCDu45R5SRx2GNAaxYWUhVYr6ks5uWO6vkZRklFANrE05uPx2VSoK3Sc8mdOR7tb9EexUlFcxbeK16yQWnQtoxq0RMwSLR2bPv67KoMUY3jU9ErUPZhQvsvLzmaauDLbW9To2ZmlHSkpnDRm5elb6JPJxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29208" target="_blank">📅 21:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgirFlFFMTw3uS5SerRpTkOJa_17lkTOaMVQ2kCbXudBJCFJw9ubDTfqgjq2gfk8UvmXgJ_rPAZ4pE5txspLu7mzW0q0nW1znf9r8fVQnGIYmIxI44anJvgNgr_A7OofgSX5pLNGuhQmWY8zc1Ib6H3sl1mxrHfJmhbX_AdUn7sfqu7v-NzuqhKqCmADcQ_yGY6ztZ4_j5yFSzVh9y8EglztjKfi65JjHegvBB3B2Wwa0ZcJpAW-fuqdinTXlIFdF_8WaCPlOVmOVBBjlxVe7NVAHoU2aN9eU1n5S9z_ZdLAbEtka08S5zgp0cx-HdPfSL5ZYmyd5qB6ocKtruHUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29207" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c75PxeYaKU_IyUaq-FU17PQh2-7qGleqGPi3V-C4m390IbFk4jTd4Si70s3sRzM900ao4GHbSHDLamYGADGhruxO_1TfomrXdnPVIaYZ_tiUVUOICMrP72o_r5x0UxTUtS1MoDEVijSP5PMTYmrIz45P-m0MvUzFOAOvzibawDybh5mGjimoUv5Dy1SDwCTHCWURTzX3CgLcTgfKnPiGxdzhzCL22ZFjBjPSWmSHD_PiyFHhvydx0jS11h7TXPju6BerNRxUFWCl7HlDUDY_IaTAOxlANpn1YT5dLHNq_7AGqH5uHizvLocquZqh5bnCV4kz5_PRLquzPgUksRne4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید یاسر آسانی که نشون میده عزیز گانیف ستاره تیم‌ملی‌ازبکستان هم‌اکنون در تهران به سر میبره و به احتمال فراوان تا پایان این هفته تیم جدیدش رو انتخاب خواهد کرد. اگه استقلال پیش پرداختی رو بهش بده 2.5 ساله آبی‌پوش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29206" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezZNnF3WfrnEBEad9VyiIYtc0QQ7lwdqkMYbWv8BjvkB5S-OUp6irrmmrnbmNPXJGAd0Y5So59jGdr_wjTcKLrl0me0-0czgGcjPoKP6DmdMWz3i49ykq_7CmrRa6_crz9egMwTALcJh2JyDuMyrWtanuRze5ZOyaJcQTscEiQN1PqxL9roPuS8VkrhByKgsyv-kfqx4mJEc3b3TwJOcTIESzhJZIsqOXltg6K-KB-ov8gldpUWo1MhLSgjmx4hQW4gF2POwiONkboack8Q6c0at5PqYWc-0cr565uIBPV6FYoAvqWRuQQZCzfuPJlEUcrrVKJ_cM-yIoFegNjYTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ توقف شاگردان سهراب بختیاری‌زاده دراراک مقابل یاران پیروز قربانی در روز درخشان محمد خلیفه دروازه‌بان جوان ایرالکویی‌ها.
🟢
آلومینیوم اراک
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29205" target="_blank">📅 21:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxJAj1pJtBzL3acWr9jnBxKO-bEyzWeLod7tXiAUBgWboLF2pDx1NFCGWebbx7f_4wehJPKz_LDf3aTRyM7nUB-uuV0Jk8MtKghLMDwC2s8wUPzGJm0u-REd6LQ9ql20guWIKK867_7Yba9Te4XsEke_TOkSTS2bxhGBZ4Fkd2H5oWCG_AF-IUG0BtqsI26XeyktfivhJoETfZadvq64Kr-GhOXXkOYAW5Hjq4u3uJ-56PD3OoZgHskSqAfDRHavXTkV11yCynMDfe2BoEDh-UNIgFhvLswhFN-4eY-ZDvzw6ljJ4JkiyPe568lD2yaasb6a2UcXYiogdT6uYAhwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛ شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29204" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjOYOMvJFP1RKp3cHcBCclmMv2sS4G1wFXDK38HPAQMqjZ5r1ltgvO32_5kVweobeXf9659LCxJjYJfCoZSP9m4LHjBbpGFIt8kCTWtlgGQU0q0Ky-6AL4WHhRwsaP9KL3MpFyNVJ5wAHbwKM_PqL8Zr9FPJFfBMbAZ7twYe8NxxwoadNzP9aigx4T322rVLkWK2iP5yRWnl1W0amM3W5kwFjxjmFZXZOsrcs6PqfM2_AZySm7o11U7u_yZGJhmyVxcdmTdt-Tzz3agmUlKvT0KmJ4j12Jh-NYxYRaWxVD7PI6ykLmUK-J4bIeHGYyYEGIUchU28b3r4RLh43Rr29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دبل‌سیودیدنی محمدخلیفه دروازه‌بان استقلال که قرضی در الومینیوم بازی میکنه مقابل حملات آبی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29203" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29202">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUH8o-UKLfKtFhmjYRLT41Vs6UVsASWKU_zIZhm_rNiAFhesSIhHJBGfOUYb-hYzyt-cPDTr9dDZRBDodfSPwKbI_8si7Rk-pXKQcMO7j7h8-KKZIVD1jUfiUhA650GT1FSbyJMhRHTVNjana2R1ror4s32udE9EkW--5oMyZZvdyX8FXXP4rtjuqiyBxSa1h_ZsxtT-dWvHCDWYMNJx0dA_U-34qZSiEV8bd_JLx-F-dYJrugQj-ehkZjMReD1npG7RwAHl6Wm9z1V8tf9eIDuuMf3c1FRMrNaAZizZlYg4O4pX_plhtbPAp6vOgx5I1e40l00Akp0qaYsCxv1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29202" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29201">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPVTlNQJN5K610OhvZHHks1vCOVl5kRBXBwxHfaq7wxq4Pe3HGeDlIKBKNQeGdnu_sE2f94a04ER0ad07x4EK10TAZWaoNlOpEYcOsKkMSz_ymOtexL69humKX_HOv4iACERSNG3hN3fT3Df74ldUDl5FMQprzpteuzAeagEphcvfzuayLqSubFlPvTYn6-7-_XDPkvNaP_Xy6ui0xwBamQmDCu0Uhb4GlKPobGFmAve7BJFF28nAD4xYMMwVIdRh-Dii_NqNs7RqEv6U-p7ufi0IECGOpXedJLQmXJSXeXxdX_y1qw_pHfAqDbWEaStWw_IEO9DfSv2nLq_bsasMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
یوونتوس
🆚
میلان
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29200">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=KM_BTxtS6HTfElZdBQb0-Tt_DfBhio-9KNtGZCQYiQaGYhYiiQAb8aYfC8_6bh-2G1OTfV4GaRvOjPw7XtC5fFTeQ9zvOHRmKjJ6vQQRYkakErWURSljbLuOCldG_EjZRIwQhK1WJGmflxXFOoHOL5Cp-Wge4FarguS7hno8tTyjWZKoKlbfNaikh3Sgp_P8wvBsuQ0KpJpGboNk9NtimmSvTNO5iyjcPqCNNXzsCakN-lpdX_9TSG-IxDN4-PtXyEoRIK52JWtabcPssvtcqLBxNe21NsMZe1UvgqCmIzIHKl2_l4zHlm1AiIvuGqBvgS51xuwww8fNXjc3TVlacrVA1-_eJLVG9vojg2SQRPxAhGLdsPwIQD3X2YEpI2Vyjbs5zBP95p8G-2bouO8O0wIk9MdyKn1wv341Z_kFWkYi4dHy87Dkt6Z9vMIHZLAdET0Aa3wxE2-tEeJg9ssPzGBZ9CWMpr_SSnhEJY9iBO9h8uZuQlj2Jrri4FGaHCnddpscCQpoab4z-6fzYS92Qw4V9JramGbgw7fmL8SWqpvy11XDKniINSVQlnp3QA21AqeWaWJCzvmyUNqYJHvYdZ9Xnzi-QF5D3yZ3tJbTSYLNdhoGuE2nGz_m706rq9Ow2egEN6r093H_-uiPzC_K5-BuYJEVdJJSWsdCnfOgka4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=KM_BTxtS6HTfElZdBQb0-Tt_DfBhio-9KNtGZCQYiQaGYhYiiQAb8aYfC8_6bh-2G1OTfV4GaRvOjPw7XtC5fFTeQ9zvOHRmKjJ6vQQRYkakErWURSljbLuOCldG_EjZRIwQhK1WJGmflxXFOoHOL5Cp-Wge4FarguS7hno8tTyjWZKoKlbfNaikh3Sgp_P8wvBsuQ0KpJpGboNk9NtimmSvTNO5iyjcPqCNNXzsCakN-lpdX_9TSG-IxDN4-PtXyEoRIK52JWtabcPssvtcqLBxNe21NsMZe1UvgqCmIzIHKl2_l4zHlm1AiIvuGqBvgS51xuwww8fNXjc3TVlacrVA1-_eJLVG9vojg2SQRPxAhGLdsPwIQD3X2YEpI2Vyjbs5zBP95p8G-2bouO8O0wIk9MdyKn1wv341Z_kFWkYi4dHy87Dkt6Z9vMIHZLAdET0Aa3wxE2-tEeJg9ssPzGBZ9CWMpr_SSnhEJY9iBO9h8uZuQlj2Jrri4FGaHCnddpscCQpoab4z-6fzYS92Qw4V9JramGbgw7fmL8SWqpvy11XDKniINSVQlnp3QA21AqeWaWJCzvmyUNqYJHvYdZ9Xnzi-QF5D3yZ3tJbTSYLNdhoGuE2nGz_m706rq9Ow2egEN6r093H_-uiPzC_K5-BuYJEVdJJSWsdCnfOgka4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
درهفته چهارم لالیگا؛ شاگردان هانسی فلیک در در دیداری خارج‌از خانه آتش بازی به پا کردند و با نتیجه پرگل پنج بر صفر والنسیا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29200" target="_blank">📅 20:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29199">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e23364253.mp4?token=C5S2LMhdPmv6_2s7Q4nOzif_orGF59WEDywzS_khbJHKa3XKppjN8TCvn6l2ypAxDxTR9rqa0QspgOkSLUBFz8A4oqWvEG8JFMErDAaq82RW1UPY6xDCZe1NZDD_lCYgUxdcmxvL5ajsb3PP5DMsZ1kZEHNEqs3fKwJ5li3Af9jjCNIAYqEHCkFgi5I2UYEmb2lrwxe3YOMDB5KGtPS3Gu4uj5-icLSg9DaP5RTpwzZFEKEuGS1Yiv1Amxcr9ZiX-aeoJhBbRCwVycmEMWHUyVcjYko_mXqwYgWunkRm1iFilMVQ8XWlo_IJLviobnVLEBCvLQcwaBvdfguvlXo2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e23364253.mp4?token=C5S2LMhdPmv6_2s7Q4nOzif_orGF59WEDywzS_khbJHKa3XKppjN8TCvn6l2ypAxDxTR9rqa0QspgOkSLUBFz8A4oqWvEG8JFMErDAaq82RW1UPY6xDCZe1NZDD_lCYgUxdcmxvL5ajsb3PP5DMsZ1kZEHNEqs3fKwJ5li3Af9jjCNIAYqEHCkFgi5I2UYEmb2lrwxe3YOMDB5KGtPS3Gu4uj5-icLSg9DaP5RTpwzZFEKEuGS1Yiv1Amxcr9ZiX-aeoJhBbRCwVycmEMWHUyVcjYko_mXqwYgWunkRm1iFilMVQ8XWlo_IJLviobnVLEBCvLQcwaBvdfguvlXo2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ کسری فیکس شد؛ ترکیب سپاهان برای دیدار مقابل استقلال خوزستان؛ ساعت 19 از شبکه استانی اصفهان پخش زنده خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29199" target="_blank">📅 20:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29198">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da9tvMAfDBbUb_DhIgUd_VOK4RtYqTfJUxOVYIqhwB1nlXc3VHd8WHNI6eVkGbNlyKfYtgkitPge23t71Yzs04NDjmTdRJk-9JnrrkyLXHOL3-A67D3gvvwJdyp9hbvZ4teXaURS-8OdSiec5afpvbLIHxNBUnIC5JYjzIbaiD8pthVRAvr-q3v7E1CAho_XuPCCyX4-0eCkTqzgscDi5DKSUhO_L2wSHybpvOKimC6WUL6rhwCVaPMzg2rc8L8GtLsJeJ-UAhpqaoBKvBKcrDxQSRu5N-o00FhAsWXDNXbxpRP8oNSxwI9nqeynHxSxlGHVu3Z8SseakzGCx_kL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی پرشیانا از سیرجان؛
مدیریت باشگاه گل‌گهر به سید مهدی رحمتی اولتیماتوم نهایی خودراداده‌اند و درصورت شکست دربازی هفته آینده با شمس‌آذر از هدایت سیرجانی‌ها برکنار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29198" target="_blank">📅 20:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxp6jp-SRtDIbf4kS1t6vkQVL9HrL7oyzWUrSWjO60g0_lWOANYWMKmL8-Vm-GY1ii4mnkrkOTY3Kgd7lQ8w8ig3zgfbrNAm4Plr74K7FOZgvuzGPPbZAYlhOqLR-QcRv92ShKcg-CGsSUwjqU8mpOVJkxV3OfAFT_tG1Y476mfS7j5O4wH3JtXPa4x-IESKzTA6bBxiVDWuUR2PLMRol-L26SM8J-cRuE-yGmNxnWhieC3wkGSG6_xFL_WyO4amNcjWWXkhX24aRx8iNxfMsR5ZTdudiLJLeBXI5PdPGFA7NLwv0f7xH002_wJ_YSwN7NNCYrGHfsOvu5bkg6-TIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امروزمقابل والنسیا؛ ساعت 17:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29197" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=aAzpsTUWn_3wARR0jGbF8bpijtU3fhf5FA87dk-wjKf671ZHHnhDRA3GeXmOABjZJC16ZWjUz9WapBPUGNmuW6bRlbsT8-BFxkskNq161AyrFImdplAT9kKsEj1KaOADgRPOJkM6HUwhZiSjrqeLbik6HXehbBfBknaGNhS0-S2bPHlqxJKm2-Tc_0P8IB42ORNOclhqah8kHWT7KSN9djG4vOhAY3nPuHX3uXT9hFshpW1BVcVVGOCEq__x0sHMSwabIi0PR1AeNu5L6whFaCxko-yVl6M6fs5K6yndPLwl2YF_4WuYkCJ9GHGOkduZfry-Sb5wOuQs4hbyEuom5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=aAzpsTUWn_3wARR0jGbF8bpijtU3fhf5FA87dk-wjKf671ZHHnhDRA3GeXmOABjZJC16ZWjUz9WapBPUGNmuW6bRlbsT8-BFxkskNq161AyrFImdplAT9kKsEj1KaOADgRPOJkM6HUwhZiSjrqeLbik6HXehbBfBknaGNhS0-S2bPHlqxJKm2-Tc_0P8IB42ORNOclhqah8kHWT7KSN9djG4vOhAY3nPuHX3uXT9hFshpW1BVcVVGOCEq__x0sHMSwabIi0PR1AeNu5L6whFaCxko-yVl6M6fs5K6yndPLwl2YF_4WuYkCJ9GHGOkduZfry-Sb5wOuQs4hbyEuom5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت تیم آلومینیوم به پیروز قربانی سرمربی آلومینیوم اراک اعلام کرده دربازی فردا با استقلال از محمد خلیفه و بهرام‌گودرزی استفاده نکند که قربانی اعلام‌ کرده که محمد خلیفه و گودرزی از بهترین‌های این فصل تیمش بوده و نمیتونه اونارو کنار بزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29196" target="_blank">📅 19:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29195">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfwT8mG_3WBnyYdge6p2PDTEx69M2WhLWxb-vIouXvdv2umqv498q5rkAUwg0qCyWQ63Wxw2DG6K0fzRxzpuEfPMdpdCuqTekjuU-dfruDEQgf_YGSiqff-2-jhxqS-YQ8LHvQcQ5ZzZKXHsuQ0xNQsrWW-boSAlyfGQclxVxourFX6ki0NRD-eyPSYBQCD3N35CE3ZePLp-nHiLv3iY-1NvvQuW5HFoyEQ6-e6ObLrJA76ZzeNEsBm-71LsyuUyVlcPFtfzBBXcn4G69ooS9_UfpzpmtkkbgaV7fpoJ0irXvPN3wAd4IA8OrRpF51Md6M4WEHHZAmrIFdMX6JvL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29195" target="_blank">📅 19:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29194">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lmms6-xEAVEFedFzP2V7rf8i31nUGMaXVLCxdg7YXaiZTQonck1OYbmWPgWnZf5f-GTd46qQ76LNLsr5tbntVfcscsyNw-I6YqBmk2glSncCG3cVlDQmBhVVSts2DinaWwKgp1QnfTO_Ninh0wyonRJWx210qn7Uwa5QJT4yexh7OTdvhmFvKPQgBbuK47R1yk6BjN3nUkxKbK2B4QzawGc9ByU3zFlE1CBVLpAtrMV9jWpeCeK3_XHqKB3N9jxylbP9MCNjwz6sIwmstwJK-Ww9qJySthh3IP5IAZyWL0kQNAIdLk7NBRyndVUteLFHUQnAn7ENgO_SlCWBGAyVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛ ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29194" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29193">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🟣
درهفته‌سوم لیگ‌جزیره؛
شیاطین سرخ در حالی تا دقیقه 96 دو بر یک از اورتون جلو بودند روی یک غفلت گل مساوی رو خوردند بازی دو بر دو به پایان رسید. گل‌های دیدنی این مسابقه جذاب رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29193" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29192">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGEFpPQ_85APU0yVuSSzVYKXuEPNUMDsoHp4ES50s9QrWIuDxey5fs9mJRcDBNzyN11QOQJ5cOSb1-L1qrTGoGq5uSsKE9586AXNHcP9z2aewgAuiyn91jSB9lHBEyFakQ-TCYhrp7uP4xOIpoI2Sa4ZQqQU3wugcVeQiIDcnyX_joxFhZ8KzA_BCDpGJkTMvEJh62dyyA2xSQRofqsFdpUFiZEhuBD_EtIBe2QOyssFshVFDllaEQ38CdkklWvj-F_VBKd2tXfw7Yn6hehusYIXFFvBiHDLQWDzJynemjEYHrMrCzNPl1h-pqxnbjvPbLvKTMqnVu4zAAoxRYi8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29192" target="_blank">📅 18:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usPw8RA9r3tJUCr2bbN8ZYdovUgIkRfT5sKwq84ecxi-GpjZODOEODDfj-zx6DzKp30TeaGdnSWTIQIZL_A7svP7zLISLtEO0HxtpN6-SCqRtk4CY7FefhJEPKeg2FFsg6pSWScXCz4gmjJ5LOmMHyVd6o0Y39i3-KfjJC-hbyevyRBSwsRvaWrS2TPDww7Vaz4GrlxQfdJJZmtUf1G76cDP_yb1Tr0_unUzmoV3DaYrWhLL1_eXEkqvAEDbOKEsCoeADEqTivjLPy9-l2Fsyw7P5GDvAeN5yKNC3Bu5T6Lcjnhelc2bPTabHAOU1OkfioZZ0_Juv1mnM9PhSNGhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Na6QANU_JPx36lcAc_u5DnF2ue5YJnsJPiyvC0d_78mb4z2QijoHfduKfdqhYOVTbIZSYMonn_JWcx8fDV7D5jKOJPq9coWOv_FKnOmUlx5pXv-WgODdOH_qs072nxIH9-baRZqQljYNxUxU9dMVIjPJOy7HqLtsWMiBkonOMIAhIVN3Lmf9gC0DX0qfe60IXkEW9fbVjUhvSav6RDQy3dBCWSbyUGxqU7ZQi6v-D5ubVY0C2bOv6gk2f4oI8m5SQqq4hIU0lnB3nz8dNevxAUMM5hX0AlDK11JPunuRusHISgUJBZKVb5RUYFmgXfmZCIPxj-gLELMVXRl7BiM3TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛
شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29190" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJsD0vHr-PlFW3B-oWA9qpJBqRUcoXr3N8iFIAPiAG0tgvVxNskhLKPFI15BrKkGFD4AoNPS2AYItFV-J6mGe66xKiVTteFRQtH2DKgEWrR9Oic18wSEphxfc2O2VaNQv5mwMZ6C_NSlUiuijsZKys0Zpy09LbQUMUr_UbRbQwmRheKz-ziuHKlBG0tp9bsBZjoc90fE0TwsGhVYVY97337Oli0_J4tIkJ8NwpHGMCvMePJfPVQoX5OfCfhx4xHEjzAxI9zJSmFNYywaoc0_2OBeJP5I0NRLYINaTvgBa4BMovGpHRzskQibz1vsritbtw4IRUluGpGsF-ULNkI2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇦🇷
رئیس‌باشگاه‌اتحادعربستان:
سال2023 قبل از پیوستن لیونل‌مسی‌به اینترمیامی ما پیشنهادی دو ساله به‌ارزش 1.4 بیلیون دلار به‌اوپیشنهاد دادیم که اعلام‌کردبخاطر آرامش خانواده‌اش قصد داره ادامه فوتبالش رو در آمریکا پیش ببره و پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29189" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29187">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrQAKDslcJCsvDwT_uoEi4AZZfQrgOiELwZ5iIMaqlM6jzDpAyd3bhWq3IR5G1_lQQEfRoFbbcvuivqJb8-eZr7aAucDqWM0Akubli_FWsLni5HrKLf7p7IXq__tU_y5qWXyu1LfbA5SmtUXeV9p_BEdoXL6UADxgOHJ0TwcWh-tRLv3e7nxTl8Sfr7plyxLzDqcDPPSlvKGpORzQUMRe3jtLUMXI2zhsxSkap7y43zsnKuaUyAiejgrcJOK8z4F7w1vRMosSJRdwpTZ6l7CsXzndXHgwsn40Lv--nCKAf5djr13VUumlEzK_vZVcNwHc9i45Ji_1YPBwJNPbq4ZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29187" target="_blank">📅 17:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UARqhzAejVttv7wDLyNt6qWaNLtVIIMTEn1LmlcYh-Erum5teoY3AHlIMMCWfV7OXgl6h4eT9mtikI1aB5CxzOrXttJedo_IO0npBYbPTNhsUwYMKQ0FG5yZu4jUvQCJBG9xjA-N02T51tzvKDpJlxG8btuxM6jrgvXhqNW0CKIeEq21eDvHWqH5z2qyF6-U9p26Q0ZkQSIpjpBOg4JcCN-39LD_Y8cb-7Zi2PTeW1SIy8LzYxyKoR9RGyhyMxKt1-SAHOMQIcDWr8RBNl90i37khVTOqERmH2Ixq_yzfCaeW0gPX8983kKdPpbsccsjbbBStFmf44oivk9NB7wH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfPmhpP14QR84kO4q1FaOzfWN9rDwDt0G8aR2JoZGiI2OS6Toy1E2-hvMTPInhpRRDXr3YxAMN2VH_fzBBZQ5_UlHj4YOOJuA1QIazP0elixrOVvxoXz6NC2ah0NQ_ouFl_Trt3Za3l3f6NuNN8v5caErJxzpAgTF_MEu0mKzZv_lPb_BGyA0zWFYNCHiVw6SRRElbL4yRrQZ2Znbh8HuNiiET3zjlN794l7MEG2lXZdeUY6k-9ugZJZpY_AaOxeERkwNw8P1J2GN8Ks8sit3oBX7iDlJhOOG3aneeySFacSpgP1305eLCBrnMt6-TWtUiKKz_7iJtXn57cEboGcUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛
ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29185" target="_blank">📅 17:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMWsHSksEqimv2MRFuYtHuWQAr2VVnMjTvymX3YJwiSW9TX2lCxBeHPoN5IVmIy7k-brsE0F88gHWEquABg4EZJ2-VzpQ327GxT4-y0tFxVkgZxXwB2GE9DuJlQzehfm_gpRm1pbthKnrvxCVi3inhH2mwlQ3rhODtIzFhX-8P5CIhbZcLmh6EO2qZAHRtu9m1xZ4Qqv4uyrRVQgntrR96NKhEx54agHaqxZCBrrOK4UApVGEa68Vhl61xiKZ2yBX7Oz6l5YGcqbcYUQKVcNYC8GaHAbnIR4AgtfHROvDzP04XzeFztkvE-1yxvpsM6mG5920KDUjIBn7U0F84HTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته‌ولی توسال ۲۰۰۲ تیم پیکان یه اردوی ۱۰ روزه توی انگلیس برگزار می‌کنه و اونجا یه بازی با من‌ سیتی انجام میده. بازیم یک یک مساوی می‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29184" target="_blank">📅 17:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=C4GxEC8x8YP9iNSc-80bMB25Fv5BRMo73w1xDiSMTZJzU9E-_lJeSoNhW958DG6prG6t7J0X8EdniWt9znniJ6v7cvc-4dK5PsCde8pEgW_ZufG3tK6IUGBbAxwAiuF3LKl2yGo0gv3kFIlNxOoHgkDggBa3SzaZQm09LUuN5-e1Vhq7IqIquVhFmh3pnOaEJRbz7K17yxg9X7tu4cQ-PdJD8Crz3MUlSbmsKvCadPed8lFo1YU6NeNm-L3mukHRDoMvTQQGnDGQ_5NxJCm9d79p2HtNBGcMSFgRbHq3sSa2oV5dFBGN4eldH6kKg2knbXlCUjvn-x9am_q9EHDQJrLxLkK30U3tLZ7KCRnJ-g4TYhJTjHBeSKax6mEcFOip_eN5Js_lpVgr0ddkN_QFJE04G-V_WEDrh81GaSoRYsjDD_rjjoZhR5llG5vgwGHCMhakpzwu0aAlDmKkodNnc2F0SYUyipN32srpNktQNDO9478rfXyg3UdSAgCqi04G4U1HaJAyCtQ90oeEHtZg-wwrSsnmqCs3VeFx8c55dbpdkIyxkO_A2QdJBmY44PvzUpe2CKv41QJNfPJlcpNI2EugfBuIMDnVdo-DJ1479uFBLfHznBKQwaZ_dZEugteiEQSrXK0wtvo3NT2XxqujdgORGLqLKPFpmBgKS5jLta0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=C4GxEC8x8YP9iNSc-80bMB25Fv5BRMo73w1xDiSMTZJzU9E-_lJeSoNhW958DG6prG6t7J0X8EdniWt9znniJ6v7cvc-4dK5PsCde8pEgW_ZufG3tK6IUGBbAxwAiuF3LKl2yGo0gv3kFIlNxOoHgkDggBa3SzaZQm09LUuN5-e1Vhq7IqIquVhFmh3pnOaEJRbz7K17yxg9X7tu4cQ-PdJD8Crz3MUlSbmsKvCadPed8lFo1YU6NeNm-L3mukHRDoMvTQQGnDGQ_5NxJCm9d79p2HtNBGcMSFgRbHq3sSa2oV5dFBGN4eldH6kKg2knbXlCUjvn-x9am_q9EHDQJrLxLkK30U3tLZ7KCRnJ-g4TYhJTjHBeSKax6mEcFOip_eN5Js_lpVgr0ddkN_QFJE04G-V_WEDrh81GaSoRYsjDD_rjjoZhR5llG5vgwGHCMhakpzwu0aAlDmKkodNnc2F0SYUyipN32srpNktQNDO9478rfXyg3UdSAgCqi04G4U1HaJAyCtQ90oeEHtZg-wwrSsnmqCs3VeFx8c55dbpdkIyxkO_A2QdJBmY44PvzUpe2CKv41QJNfPJlcpNI2EugfBuIMDnVdo-DJ1479uFBLfHznBKQwaZ_dZEugteiEQSrXK0wtvo3NT2XxqujdgORGLqLKPFpmBgKS5jLta0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛
به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29183" target="_blank">📅 17:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=LYIPsjiabYPOPSv_mRUw6FLUiCeWc3u6BKrdduSiQjB5sj9P6hrddf0jerHhXWPmwYQ7mZVDFA7IsnFMWc88xNEVevTCS_4mYc78pDkPb1NP9v3QPNGs1BD5Er9NDnLFuQU4_OB2szPQXevUK77MlCPAeyXbtIJqx5W3kBp5VxPfXSqVvRHbqa5HLopyYva8rzu_gBMP5dWDKC8eUUVgJZoOaeKtWNFaSAwx6ehSqNB7xTPh996VvX2qlgSuKOjQjUo7v11vghGMjFk9Wi52t6rj-m5twvZEuSjGVXxDp8LxPKEeK3rFu8YIZ5sKIHZwhX6CbLF2nk_I67o9Eo9zOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=LYIPsjiabYPOPSv_mRUw6FLUiCeWc3u6BKrdduSiQjB5sj9P6hrddf0jerHhXWPmwYQ7mZVDFA7IsnFMWc88xNEVevTCS_4mYc78pDkPb1NP9v3QPNGs1BD5Er9NDnLFuQU4_OB2szPQXevUK77MlCPAeyXbtIJqx5W3kBp5VxPfXSqVvRHbqa5HLopyYva8rzu_gBMP5dWDKC8eUUVgJZoOaeKtWNFaSAwx6ehSqNB7xTPh996VvX2qlgSuKOjQjUo7v11vghGMjFk9Wi52t6rj-m5twvZEuSjGVXxDp8LxPKEeK3rFu8YIZ5sKIHZwhX6CbLF2nk_I67o9Eo9zOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عمرمفیدقطعات‌مهم خودرو؛ این پست رو ذخیره کنید و برای دوستانتون هم بفرستید بکارشون میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29182" target="_blank">📅 16:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVtmMNzV2lyTChImRCPzvm3-FGHVBgrT3seHITFSEfTufyl2UhwlwC7BCo7MkZqqfzK8VtUW-ObsCEnQ8O-z07omeQ80TOsMA2Y96lRZsoxMwh0CsdnhRq2fNdhBzqq3epQ7OIprTqE3JeRtE78YnX38gs3bWNqjfD7zLga6bncd_cmCOu8fM6mrw9x6Eo-LaJMV4uc1kbFlSlKjeU5QLaOYOMZUSTAbp81SKaXW0CNe70i0aAK2ZySkl-nRXvujmXkVPFxofJxW-seRPqUea7jfVXGjH_ImhoC7zhisT0Ov4xufQDx49VHvdwwQVlTnwICTXl8bNPEyKCB5cR3MMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29181" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtNLF7zxZz3HpUef5YWmE8zaOVBNXLM7_q29ypT2v31eLCBsgHUnIYcV7iN4W3Pjy6NQR4HPIh6dkaqknvMuvW1QYN1QhHZrsxy_fs71HuVsa5vELtGzTfWJE7W-YWqy8tIA4tCDKlNRrTvT5I7wJhmAs0zgJaLRmjfeeU224b_YFvj-fZgoi3ZsWwj8fsmfkg28YHI7XLYiJkRPezb6BkDyI9eWN5hVDd1JEGf_i9CvGcHbSxwz88WiePfv22lnaAMJoZLxBFwxw6jDGtuvnJ9vau5-69lN-L-5MfnnIbvbGlSrj5n0uGsqDARm7vlQJZyQDxRvwyMv3In-oC3Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29180" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFLzCYxmAO3GvuvOL94V4S2d4B6GkmIt7CWcC6OltnkAMI19uTPqXpIX18qaB3JnBonqd-FRrS4-qDjG4Tg2PKiN2MvwfSI8ta57UdXNgO5Cv5g9O4cHI79KAAwOI1hC1_CUm4fvwavMAS0oHfKIgAmm0ht5eQlM94nwkFSNJ6uvOG0ovgvnAIeCisABZeq8qpspN8BvOzyC1eR9h9y_0eQAYkXTJHVTRrewRwPeqH4NRBQr5vSZyzAT1W-KgUXj-3bT0R2_BgCx2e15-VnDo5cULSEXVDvZKF8Tm4NzHmZ2Uos9IIfbm-WYd7Jdx3oHAg4OwaDQWAAw8HzOrouAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29179" target="_blank">📅 16:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29178">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=AogDkmE6F7AmvEtWxpL7PeEfwlnBjRB8IlNiR1eyxM2164YQIi_PQ9Tng40EK9ikqN0yaxstPYP-8u8afuO5Ii6qC0bxxm-HoRp4QprAJ4c9lxWiOjMVuGAxBp8tX7IoLUmTASzTJwYkgUFZs2B8Un8l1HPRFbIr080PJIX7Vs9Nkv4hrTceKndxHMrg-LaZOvQ0FNkxtDw57yWC_sYzc6RjINygNDS2AqqU1U-NSWgWVLHbc7SQXLvXI6zhfiDuZNR36HBitwc6IeKINhp5LMCDIFDJddEYkkaMzYsBe2rlgHp4Jorj9iXqLRCxit19NVbkqEFIWJZUXKVka8vnVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=AogDkmE6F7AmvEtWxpL7PeEfwlnBjRB8IlNiR1eyxM2164YQIi_PQ9Tng40EK9ikqN0yaxstPYP-8u8afuO5Ii6qC0bxxm-HoRp4QprAJ4c9lxWiOjMVuGAxBp8tX7IoLUmTASzTJwYkgUFZs2B8Un8l1HPRFbIr080PJIX7Vs9Nkv4hrTceKndxHMrg-LaZOvQ0FNkxtDw57yWC_sYzc6RjINygNDS2AqqU1U-NSWgWVLHbc7SQXLvXI6zhfiDuZNR36HBitwc6IeKINhp5LMCDIFDJddEYkkaMzYsBe2rlgHp4Jorj9iXqLRCxit19NVbkqEFIWJZUXKVka8vnVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29178" target="_blank">📅 15:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29177">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=fgalLPIS1FBMh5y80ibkPUaU-e7K2fa7GPNMCbTYJzfuyM1HIij38N46rmLmqaNhbdujgkUo0uyW1i1MksV3JA-tdjs1sW6NgxF1cCav0uLPrzzu_MzKKttBldPmRRAGNz9dWGaco6zlb_2cnwPQrxtmUm5Xg7eCTxBEMYPEfO_MZY4zkvBQjAtXhnCDumXj_o2LMFDsQNLsFm7zdm-UTasGwMbI6TXPlMX1wdddWYW6ZtXxnOPhKt1FASkzNdpBfOrPqmQ72gUQrlwmMqraVG_umy6MUr3LhAVfbYGCPJGGqPD0xZd819PjHvoDoK4qSv6bb7PBjF8wy_4d0dIdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=fgalLPIS1FBMh5y80ibkPUaU-e7K2fa7GPNMCbTYJzfuyM1HIij38N46rmLmqaNhbdujgkUo0uyW1i1MksV3JA-tdjs1sW6NgxF1cCav0uLPrzzu_MzKKttBldPmRRAGNz9dWGaco6zlb_2cnwPQrxtmUm5Xg7eCTxBEMYPEfO_MZY4zkvBQjAtXhnCDumXj_o2LMFDsQNLsFm7zdm-UTasGwMbI6TXPlMX1wdddWYW6ZtXxnOPhKt1FASkzNdpBfOrPqmQ72gUQrlwmMqraVG_umy6MUr3LhAVfbYGCPJGGqPD0xZd819PjHvoDoK4qSv6bb7PBjF8wy_4d0dIdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزی‌روزگاری‌ادن‌هازارد فوق‌ستاره‌تیم‌ملی بلژیک و باشگاه چلسی درمستطیل‌سبز؛ کاش هیچوقت اون انتقال انجام نمیشد. هم رئالی‌ها پولشون رو به چوخ دادند هم ادن هازارد اون بازیکن سابق دیگه نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29177" target="_blank">📅 15:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29176">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpOE9gpyq_G7B4eAB-W_GYeK3_E1gFRJRw99AY2zuEos2jrT20WjI_ZbaMy_dkmDteN687Ql8YtaH6XvZ3FqbSF1rQsiVirgAMN2xkIOVyXmjodPIi0Zz0tVshPMQkeigUKwlFlWpK_x9yL2Z9jbtooclDD7KrdcGisbBVGCZ2Ic-g16vCm68RIOr2KXedrOXLvMD1IKG307V86JNGHwQp7BH96fZfSFKWZH80lgdy3FBB0K54w6kVhh2nZlQbQkCr3cwYHcJ72CbpCThWqK2Wp4HZvP36GpedKcGMpXJEa92PoxQXpvRJwd3FzM6H3WBY_05ysEyBIdcik9G-xGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛
ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29176" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29175">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=jIqkRbEulaM4lghnvryAH_PoK484VitfvaOkj0yPrryVLBvIPJ_m0Neuhu0ItZS-u-V0TzE8WS6nQVJXZp33AXPKic0bmzcIedfn9qm3jngXeMZBEpSk4TfRcFGJ6hkk3DcC5cEiBrwUNLVOzXLYot54opzAlCi0oaqdPjwkT1bV6fZtUx5XmNTIsqJKfCQ35y5w1iU_Wl-f0KNFC_pvUfuDM4td9VzGMclrAFjagWL2p05JdnlSAkz73OD773gCNRtavGI2arpkqCFcDMRIBV5PISDvZOTLHRAuv-t1NaYM0G2PYthIbA3zXI8zK0237MfERH32hjnij06dQ68lSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=jIqkRbEulaM4lghnvryAH_PoK484VitfvaOkj0yPrryVLBvIPJ_m0Neuhu0ItZS-u-V0TzE8WS6nQVJXZp33AXPKic0bmzcIedfn9qm3jngXeMZBEpSk4TfRcFGJ6hkk3DcC5cEiBrwUNLVOzXLYot54opzAlCi0oaqdPjwkT1bV6fZtUx5XmNTIsqJKfCQ35y5w1iU_Wl-f0KNFC_pvUfuDM4td9VzGMclrAFjagWL2p05JdnlSAkz73OD773gCNRtavGI2arpkqCFcDMRIBV5PISDvZOTLHRAuv-t1NaYM0G2PYthIbA3zXI8zK0237MfERH32hjnij06dQ68lSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
صحبت‌های‌جالب ارلینگ هالند درپایان دیدار روزگذشته‌مقابل‌کاونتری درباره کوتاه کردن موهاش‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29175" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29174">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFIdq-og2VtqbMWU6HrqYtjFD_-BLNFSrocQILcoYDaia2OWzUvK_bnXdwU45atM_5sOfcOlDclNkuReTt8xOJtabH6wb69gYpuJXWfbly273MS54wGUixcDM_5q9KAO92G7X8JaHlzRbiJO5rngDsAr_NFsHnFw1iOsCHWUy-momG1A5fNRUOYPk9I2Z7OlztScPj9gmskmXO4a1xtSxVFm-YeR6T0_MKnk5xTj8SXTJPWNdUP-qYMPvRUg5gxtLqrVbadVzDdiRc5l8A-dr6pgylN5rT_r92XkcOHvQrbhV4Yp-VoDXdKmwGrBjigoVhh9DXG7kQlDQXvqgSge4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🟢
آلومینیوم
🆚
استقلال
🔵
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29174" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29172">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=n1RqLCxAWOown8sZ2nbi8gD_nKY_nwPaAA4-c4moyQaGRiEcsdhgvVv8RISqlND5YV0vCDXoeYp-zvT1wgvVbBuqXpv6zWJhUSR8PRYYDNTII-VfamgJHZQq1xw3N071C7nnI68-awmH8z2b6T3_aujDbRyaAxcWNXKjFNmD9v_TlZ_m7FzDENZ2CS6suJjNrmErPP7X_nAQY2KYxSM8Q1s2yudIcG7EQAI9hjFpEydks5QDEk6_Cr9W9vo1F2ms5t2ie1FUcpwEAsFxyawk0oH8daG1Gx-YIY9cQSP-lIP_5pE--IRPOwm_RgK5jP7ubrr7nWdfeiTg40aE-XPY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=n1RqLCxAWOown8sZ2nbi8gD_nKY_nwPaAA4-c4moyQaGRiEcsdhgvVv8RISqlND5YV0vCDXoeYp-zvT1wgvVbBuqXpv6zWJhUSR8PRYYDNTII-VfamgJHZQq1xw3N071C7nnI68-awmH8z2b6T3_aujDbRyaAxcWNXKjFNmD9v_TlZ_m7FzDENZ2CS6suJjNrmErPP7X_nAQY2KYxSM8Q1s2yudIcG7EQAI9hjFpEydks5QDEk6_Cr9W9vo1F2ms5t2ie1FUcpwEAsFxyawk0oH8daG1Gx-YIY9cQSP-lIP_5pE--IRPOwm_RgK5jP7ubrr7nWdfeiTg40aE-XPY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
گل‌های‌دیدار جذاب و دیدنی امشب دو تیم اینتر میلان
🆚
ناپولی درهفته‌سوم سری‌آ؛ برد جنون آمیز افعی‌ها در جوزپه‌مه آتزا در دقیقه نود مسابقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29172" target="_blank">📅 14:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29171">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAqZYJAByivU10W6vjEmkKyfDau4JCH4hxEMYk_Y0uNNBukggg10Aw5xYGIFlsyine22mLWaGqbD_A46LWeGimihhd0fMtbfR9vkq3DIf9qvM_tD9DznDk5urL-3zNYvAubjZGFI0DlK6QfnfLprTMbGR9kM9rrkn1GbgssiCJLHK8MUHMl_pJB0D8jSidZ47EVXYxjRMQ-rM5CCcd8TQnukv65pljxlhoaulIFW8q1LN0o4GK7CjgJXX0PJngKeGU3rJ02sfftkHofAftCg3RK4QRHMkz30EdlBpqKHhZ7xPLFI0g1gxFLM54tlTG8YYZVY74hnCorNAcYLshHcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29171" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29170">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz8eFKh8yI1SXL32Yzd_r1-t3N-vxXL7XOgtRyL7-sDvGdP5JZq2nn8oddnxPEAU-tGc3TKrXIa3pIwgEefrCQYsoDbVBVneH-ewSItoXoYPPjmFt5ZDHtL7uOHO2OVbJDGFhjCGrfQA4BsubKId_Os6H7DWrOHC-bABehJb0v3TyIStY2FEkrALiokBPfFLJSldAKYHjC_zV7t2EonrzxamLcv-QpsUGZ66DJHlT47QAn5FYmoqduk0PpWTm8aHoX7FCEOtusJcHi6BK166XJKAk2oglhfs3UetM4Q-ZkN-7pDMkgGyDyn5IIzyFnhcWSyUibcqki3uwL-9SNKTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29170" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29169">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr1pyFp__YlV24D5nZYEv80Pl8yiKCqsEs3K_eZtovF3kZPI66bX7L6fp9mzRcE4T16x_WIgcaWrakdArKMxsOg2-N_qbBnR2v4j5ltvJKZviQKCgTfn6e2kg0YDWV54dy8BEkBI1HCxli0HJKmS0IXQULc5c5eQk2nyJjeRRVDDVZ4z1ZMUczkLZdfNaX3Hn3R7sKyvPjV906vnNyKAWo7Fr5MTJ-RvgLWSU7uwI0F6l8jId0rW24LWP5OvukMCEDC_oXNDQCBc9uIrMPO-alkBeft11Lu73VYKr1aep8LAqFMmvdEpRh2jFIk_lS0mxYF3NrKW1pIg9DGMdfRpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29169" target="_blank">📅 13:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29168">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr0p7mFjWrCsIja8JUu-2jqr7L-3JykPzX0VvAwTfOVaGiECIj2MdGqk5fcYIgngBRmug8Hr_cJ2KVBE3pRj4HQA4lOcyWCxr4IkHeLiqRuR5kUFJoex6lK6ucMECoSseuWN7B72JBHQdKKhg3ajwxQoczrghrQBvjAUPOUshWA7-xbyY4K50NJdyHcjFPyw18-wXOy6K5XOVKvCUEw5iDVoBVGXekgwGlx5slCXujDtQttOonWbfaJafO1dfsoXQzxxv-L5bNgyUSE_cCCiv7Ev1MJ1e7jcdrfv6B76Q5CvGwGhwG2j9dAAMSpiq3sv6BnKFCwncKiRtdhoilecjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29168" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_pskCWti9XEkqd3jwexFtV5L4TZIFy0mWdqhfaZPhvCEYcL4UqkKkL7UKeqIbomj0Ct-rRFbBEV5hpEKlu-qTDomLUK_JMi_4iLUJ68W_d6P8cjDPblhaWpu4n-HvlHWrnSpmcoYmjXx1aPm4Wr8gSmg-yK0KCd-7MHrqZwmf5TKIuaCw13Z2BQe9o4q6NIbBs0H0ckCkFMkSgx0-anvkzrJS3pW6FR_hKMDYo-tsZzHwMvoay2sv8jG7LR4hreJUiE8uKhHbowWxF5JVm5gNI4atFIgeeYKWt0cHfzgkzWDF4JbmMzIA_aeSwB-Wk6CdWyW6LBQA7AFXjgT8msWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29166" target="_blank">📅 12:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0u-InGYkhHVGwNydYbAMbi8Mxxs1RnjClIJjPMMMXCP-pO2vBnd733uzxmwb0jCRqnGUxKJS61FGR1bGgWdzRwifmMg3OlqudmMx700LAN0s_jurIyxBgCmJfmYq5IPovYSQ_KG6hlKSV4rD1qTXU_XNMo-gOt6uVlJKy5aqihd0wum-GtuxlybLNOPAECAipoQaXuHXIKwddFcDRMvvG0nVUcT7MAz0MQsCtBwsn5540pGKM0dYzNG6zYjRxqZHciHSfRwwuWUTtjHhp9tFq6uYhIFt14cZEFimKLmoy2BO1BFyPWugV7LVP2bxIOy5lU4Zo8Tf233CEcO-eHz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29165" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29163">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpDP6DWCf_PmQL-sxTcW1xujEWLFG2Bc5TLKPvRSB6S-3Pe6LcutZRM6ipBLv1ZASFVc-5PLaoqOnWtM2-srD64OEYRMwdqrF7b49J0JAwMKAlKlZrSgKPPbh7r7pL7J_GPgipm2lRlpHen-Vh7xVEhXz7PJb1I46agZFwpBDsmDxztcCYzeTSNjoxrVYFwDhZ_3o0S5vLS4vMB5B2jjNMfTDUoR6bS-OA82BD4UL3BiVmjceoIc0oZP01-UzbY8NLpxlmiDqRDZqeCQ0CZFNKrU6r6MOycbdhfWVrxM8augITnGRswyr_xKGfgjgaxTk9UxYc7kr8KKXeR5k1DGNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUbvOFwRcxAhuE7uVF6pyvd71iOvRBTmRobV3iZZIrveLT8-WJqC6xyRvVGDDQzPJlNic2frTXUAHysE-Pg5RUZqNltJeQPEtKh13o7rtF4_vGRRMR4D51qFIZiP7wCJBrV3eRfsfKPBCSz78-KpxYpX5NH8yHUJfFywj8Vd-6d8m8FHbFWUHPfJUAPNkHwbEPYl_wwHdS2qVkk_WhN7QvI8JukApr11SK_RdEZ57m_DJk4t3Pjr0B8sp5XUI8F6YxsFdQJq_4KiOpK6u07Gqobobi7dkW2bxl0PWs7igTm3Uwmsz8cd8EUDyNkBCnaElfJ2DhIcFZGM4FrQ4wZjgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
همسرگابریل‌مارتینلی‌سوژه‌عکاسای عربستانی در جریان بازی این هفته الهلال در لیگ برتر که از گابریل مارتینلی ستاره جدید خود رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29163" target="_blank">📅 11:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29162">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_AuKDMt1wJv2AzueFQuTCDVapfcpR8DsPf7rRX5kK3TbH96ZzJfKjeJrkSo9IBWIxOduevlutLhjQHoVws46Wpgha3dryYQgsPyNrJE6SXnGp0oH8xL7e3d9Nnm8k8JT-gduTlFdLJYIibxFJSbE1H8elNK-fUU2mCL-qv7aU1gf8AHdlDO9NFpvM_d4e3OXcI0B0WmWeSr13d2aqXnOVhLJNtaUoXJDCaTL43ZaRNiVJtmJaj_YoXREduwiSIrPxHiOCKKGpX1FOrysZO0JJU-v7GXQsWCO7dG0NbQ-kHNzXTxL74yjvLF0XhYBT-b7WAa-yuPbdRR04YUrmoBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت‌دردناک و تلخ ایوب الکعبی مهاجم 33 ساله المپیاکوس پس‌از برخورد با دروازه‌بان حریف در بازی شب گذشته تیمش در سوپرلیگ یونان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29162" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29161">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇪🇬
10 گل‌تماشایی و فوق‌العاده محمد صلاح ستاره مصری سابق لیورپول در دوران حضور در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29161" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29159">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29159" target="_blank">📅 10:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29158">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=KzapsaerAvHncyT-iTr19xPFXhE1P9U5RAQ1X2Cvf9pRemjlC9OKa7duJd9PEnx9ykMaMw0YCKNz-HdIn6hZaQAxAY1OLOwpDsqND9fFnTrT05o7M3xEcOsPaWmz6QIbagnLTIN6MgrobV2abq8AJOvZq-lT_UAm8sotljLow0Kl-mYfQMQmAhCZQ3nyBNCiQNi1dYOcA-35to1OkwVec_I5F3QZisSxFybflwBgu1SOStexKrdzjRpQktsCj84_MYtWiIm09-dTAfTI3RBNgyelLVmW_cRs2lZs6TJ-X-AfuKPio7iUIDVYt0h8H1b-8_-5QDxYEhjz1PFLfYnelk4pjsJ51dStxSlKTq6VyZ25wrUDPvw4b61v_tO6qILG15HRqHEzqQvxa4geaeAvRYtkyQRXw4x4jIC77YM5bBZwKVGg1kj6JE68Y5QEmwBbMVqBJclutGz1f97DKcYMTjw7BHl4fRHQbyKxJBTI40gtPioRVC0ishEc0KbejSs_28reRLoAnEyf5FXzZ3WvdAP1wz6vw-SJWzrug9JN9kztegsnWus8ZYe35M3CaBNj0q0z1VfxQ9frhhx8zAylANO_09MT1U9CdfCt7a18dejbkcubJB0VbWWHZ9XGn7GDOOUTOPgl_2CHWqLpbGroI8loOYMeqbf1a5hLT3Irvzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=KzapsaerAvHncyT-iTr19xPFXhE1P9U5RAQ1X2Cvf9pRemjlC9OKa7duJd9PEnx9ykMaMw0YCKNz-HdIn6hZaQAxAY1OLOwpDsqND9fFnTrT05o7M3xEcOsPaWmz6QIbagnLTIN6MgrobV2abq8AJOvZq-lT_UAm8sotljLow0Kl-mYfQMQmAhCZQ3nyBNCiQNi1dYOcA-35to1OkwVec_I5F3QZisSxFybflwBgu1SOStexKrdzjRpQktsCj84_MYtWiIm09-dTAfTI3RBNgyelLVmW_cRs2lZs6TJ-X-AfuKPio7iUIDVYt0h8H1b-8_-5QDxYEhjz1PFLfYnelk4pjsJ51dStxSlKTq6VyZ25wrUDPvw4b61v_tO6qILG15HRqHEzqQvxa4geaeAvRYtkyQRXw4x4jIC77YM5bBZwKVGg1kj6JE68Y5QEmwBbMVqBJclutGz1f97DKcYMTjw7BHl4fRHQbyKxJBTI40gtPioRVC0ishEc0KbejSs_28reRLoAnEyf5FXzZ3WvdAP1wz6vw-SJWzrug9JN9kztegsnWus8ZYe35M3CaBNj0q0z1VfxQ9frhhx8zAylANO_09MT1U9CdfCt7a18dejbkcubJB0VbWWHZ9XGn7GDOOUTOPgl_2CHWqLpbGroI8loOYMeqbf1a5hLT3Irvzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29158" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29157">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej_0nxnqsYBZXCTDGaqNlRHzT_P-qYD58XDiSERtZ5u9pSx1B_01nmqb5mbRETX6d6JW2fG23-18PSUhIdtKGuGmdI_A4aeASef_0Yd7w0-tSln2_Ei4h3DVFhL5rI0nFkNdwcKy25yMFM1st7KtA40yw-5LKLF5N62nCUdm5ch1NqXcmcjbdrl_QUGOzIe4rOxpaDMxz5xO4_CGxbglwnBF15fMKjEoTDOXSoEHg72c1lCKbf-o-d0rETRAhsU2TFFX9VFrsdfpsjhlsL9DO0_AwQr8h9Z1T9Z42mFOlcSOmcKswFhf0F-fBjaMp2mV3nTfROIs4qd0qUxaZUJ1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29157" target="_blank">📅 10:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29156">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ele8y1y48Ay60sRhQ2qxxk48YK08xp0dWbmtIZjCtQAE6cmMPBFWRtOM8f0_ugM16SdnbeRqPcKsQhcQK5_lG_iFv4jmWKuiGx_ZkoKUSYDhPSqWULJcHNiZlEUNzz9Ea3yCo7yA09DerUO8596He5yNXrKiGGKn1QaTaAypM842le91UnddqLNqHNv0zc7P5qOhzJqHKqfoLit8d4pUzlUiglHfU3LhvusoqXUkY5XEXo0S05lKwolg2Q_sEg8z5ZLDO5XGXDllUdtAjPwwoX5z6RwvQJBuVLmEXfcXJB2-6cQEfcnZlc_OUZsq3BNvEdUCahLrPnxm0iXQTFfW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29156" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29155">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29155" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29154">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc0OyFf3_MxhgXmxymh7Xpi7iIJKzM-2fezWkH6E9qw8uY-5h2EKbT5kfoNKYHyEwaYP21h55_fjFEvcPgAAHNuM7IRPd999ayTMQ2pyH-R4upGQxQ55eEl_KvSfw_VcSmZM2YtnMh_bracyfQBpcGNC6xpyWdgln-I3ZfICX1w8QhSN1xmce3L79NpxDNXScGLnKW-kpvlufNmIUviYqpYue5AEUUhQWuzt_zRmyLGCgLIuytPNBQosZI_jhNhcmTvkk0bJxrk8ECRe6Po6yM3fXXL4QaGJuIGso10nk-7xe8TC5SWk-SsErz7Vu3109hB84UubDObcnjFDDtYV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29154" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29153">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/29153" target="_blank">📅 02:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29152">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=E4VJbkLTPWkmAvbghXxupXvzHeACOJOdCcA2QEqO6BVXS1HaRccxc7ACxnNHcmt2x3XCbuOE4p_7JCgSEKtwqlZ11efzzqTxyBM5-YoVHiHiWdpBMBJjd1clMz4S9TJ8mJ1ZXgtB0woO6-Jc98-kgeO9-__hTH-fR2zjMlRSlb_8H4G1JIkRA2BLE4Tfdv9mbDDfxH6ENvKnfaDKwld1VIzRu9pZtgXZiFWebU1KcORQ_VZEteT3dZ2WFHyIEE6-zlsR2jQ16VqIVdlBajxN28CuD6iafDlRwafx5aGxdvLYYhjiZI4YcM2-xF7MOUtEsFK3AZcS0aY-aHl9i_n4sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=E4VJbkLTPWkmAvbghXxupXvzHeACOJOdCcA2QEqO6BVXS1HaRccxc7ACxnNHcmt2x3XCbuOE4p_7JCgSEKtwqlZ11efzzqTxyBM5-YoVHiHiWdpBMBJjd1clMz4S9TJ8mJ1ZXgtB0woO6-Jc98-kgeO9-__hTH-fR2zjMlRSlb_8H4G1JIkRA2BLE4Tfdv9mbDDfxH6ENvKnfaDKwld1VIzRu9pZtgXZiFWebU1KcORQ_VZEteT3dZ2WFHyIEE6-zlsR2jQ16VqIVdlBajxN28CuD6iafDlRwafx5aGxdvLYYhjiZI4YcM2-xF7MOUtEsFK3AZcS0aY-aHl9i_n4sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
رونالدو دربازی‌امشب تو اینصحنه داره تلاش میکنه ببینه رو برگه دست بازیکن الاتحاد چی نوشته شده اونم بالا میاره برگه رو میگه هیچی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29152" target="_blank">📅 01:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29151">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCvXLMZ_h9C9HzYYp-nWNIRLWext7LICGswmaDiEDLzf_hUodT5TpQE0RcwNun-bkxYwOJ9x1e-3eqGzXgRXjClVnBiYkmMPTLlRF4lCCeF3r73JuYbtyTCQttPf1Ih_Z4DvjxlWXWgAit4l67yhm31ttt2ZaokfLFskSpVuuZkC0gAOzxSUhqpTMsV-dijLfxq9MP_CU8IOhMNHfVWU58to3AP_t8TuvXOb9V6u2j7MI0v6jiKgZmDONPEzN10_9ipndG03e9_RIrqd0Y3pkq6WwegwF6YfrPyfGCIVHpq0fG6s5Ib_Aqj4Uj7f_zATXyUXAALKz8k1PDG6wmuf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29151" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29149">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7Tj6RNdZg4XSR5Bf4QP6rRPMfUkSh25p-W_6QS_YHUMA88KdPd17j-zHnX4EB7hpGFpz0JTceXFDsTlcMoLxKB4wzWWDTMULD9-RFjYqvHP4P0L-ONDP_ijzp3Gh8omk3B7uHpKAAp54SNIzuYeOrVzWIaB2ve_cPxd4oFPDlHSqM7UYR7Y3hhvsp_MJWYge_ebgWFVSP00JViTwkvUdTAKamjnaqoeTHk6SyIQ6VVR_a4wUBukaH71JuwZ5GePfRDB80UusOqmInetuzDvSoFb5UV25MHXa7qnaw3uklatNr4_A57Cz3eexXuNwNvpOj8dkgy2CshqLqVfMrlzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از جدال استقلال با ایرالکو تا دوئل شاگردان آرتتا و آلونسو در استادیوم امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29149" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29148">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reD9lFm2BV_DfvcCC1D7B0OW6VrkVvrjjq4vPOoFXo5CigKVMIOGVZl4HTzMMB4UvMA10oIdgqOCwzrWSH8gjkgqhdq8CTBQw8h16oe30JLtz977YKaccdQYp0Qx6sVLIKgv7Cly1Cfx05-l2uxLcrWX2s6pcdVcNDr3tJQYirMcmFKnQwlzkPMYrrT-sHz21TWTKHpSIqa3y1GSevRna-yTb9gzaygmcxH04dOcQ5WaiqUCUCO_iXTqau7EZgqDcdEmb6USMYbl09vwHnGuiMAtwhzBZHZnpWQSUdQo1uC0Hdd0G1veHWPmNHoWFr70djYa96iFElH5RRZ9uZVSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از شکست یاران ال‌چولو تا کامبک‌های تماشایی دورتموند و آ.اس. رم مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29148" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=Aex_vVPfnGQqkGhgDiNQ5-_hugEKnjp-K64Ul4JAi7mE1YhsCuMkiH_rB58wK9duAYkmzni1DBD-T9iiBTKuVKs-j9P6_xhuLE37FIPfnfel7NlFnorhiXYKxwkhGMRN1_1YPDIcSzUeNfX4KCHwyFjVm3SvaV5PhJtIp58gLyJ8MN6Z-i68QbHJtXq8ZiKl65NzKpMnC3a_pqeROsFAD8wI2L3wQABhG0yISJNpBuhtDmYd06e68ggwO7vfSsYvRFHaLOXtArHeSlf-c3oypuXR9XXKmg4A636P2_9uRjGlyy_ALPeC1SGBU1N0qNwOWhoj4cAWDjiseap_LdxLsXuUxRZWJF4D5aiFr0KMX8GBUZezDAXkqwtE78jNdRw3IECf29WTduTcQ_6d7iAO-SQnRR-j-ArMNMI77QWP0UAzzhMNIe8W6IwnFHMDymzxs9QzmLLl58ciaFNLiKbFXz8PQaHKVsBY3TGjUWT6ARHrpbMqL3JPcP0QIXg00m4z05hC6fiIuAkLT5fDYWcSnWL4AWiRiOXAtPLRCrIshgBW9wP63ADMd2VnQPFsEcZWdX6Ui4ywhyk8BDFm8qJmyK881nNJ0hiEPYHh_4RTBEg-LWLkXnP_gCvLKKmyoUacQuxbr99FXEneop4eQPIxUNw_qOY6X1Yazxo_9QIyWRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=Aex_vVPfnGQqkGhgDiNQ5-_hugEKnjp-K64Ul4JAi7mE1YhsCuMkiH_rB58wK9duAYkmzni1DBD-T9iiBTKuVKs-j9P6_xhuLE37FIPfnfel7NlFnorhiXYKxwkhGMRN1_1YPDIcSzUeNfX4KCHwyFjVm3SvaV5PhJtIp58gLyJ8MN6Z-i68QbHJtXq8ZiKl65NzKpMnC3a_pqeROsFAD8wI2L3wQABhG0yISJNpBuhtDmYd06e68ggwO7vfSsYvRFHaLOXtArHeSlf-c3oypuXR9XXKmg4A636P2_9uRjGlyy_ALPeC1SGBU1N0qNwOWhoj4cAWDjiseap_LdxLsXuUxRZWJF4D5aiFr0KMX8GBUZezDAXkqwtE78jNdRw3IECf29WTduTcQ_6d7iAO-SQnRR-j-ArMNMI77QWP0UAzzhMNIe8W6IwnFHMDymzxs9QzmLLl58ciaFNLiKbFXz8PQaHKVsBY3TGjUWT6ARHrpbMqL3JPcP0QIXg00m4z05hC6fiIuAkLT5fDYWcSnWL4AWiRiOXAtPLRCrIshgBW9wP63ADMd2VnQPFsEcZWdX6Ui4ywhyk8BDFm8qJmyK881nNJ0hiEPYHh_4RTBEg-LWLkXnP_gCvLKKmyoUacQuxbr99FXEneop4eQPIxUNw_qOY6X1Yazxo_9QIyWRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29146" target="_blank">📅 01:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/persiana_Soccer/29145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‼️
باشگاه گل‌گهر: خداداد عزیزی امروز الفاظ رکیکی رو برای امید عالیشاه بکاربرده و صداشم هست که او به این بازیکن ما فحش خار مادر و مثبت 18 داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29145" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
