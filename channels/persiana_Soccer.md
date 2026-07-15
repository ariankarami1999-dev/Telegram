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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 469K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 19:43:38</div>
<hr>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoX4Jh0IkGo6VKuVOI3FHFMtPLR-gjH7MvU5o-Ts9ekHY0uDEH1GBWwP-ctxCxDUu8bJ2_MCSj2xqEe5lCLmgp9zw9dbNLBrYNn661sl-JzPzYgHN9Ufr-NxxB6jVTkaplvVOeLzOd2Q-T7OZnytri1g4zdIa6ptr7HAB1s8t-RayMlA4UlwOMvRoHWsWRkxZ-fqJVb6F0aTLrsRKstwyEZldRz0mINQTCxkdy9l_u__P17752-xazBGJsa94QHZaPXgGHM_sieAtyMbtIrBAFHxQUYtWkt7LGVI3CvP56aYp400HcA1tQCokzZIWe407u4j9MvRoKeq53Dvwyt78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-f8BESUnPFVEorN_FGGR_JzEtM9jIrVF75IQ8ewrlxnT5en8zo4Y_Xl0WSWxapDVNy_fNQ_kQdkUgPnk54fjygMCor9Q6ExDlC-sGuuLV84km7-EkVGDBdcokbCk-UES9Xe6oycdO3UHPVxNJ6yWGU53a0vEl3n7_S_3trsaBx7-HOVKmPkCtlB-aXsxrfymH6H2DAn9ODQ2srBl25topB0PHw4PjRNtdnYYWJpwdi3O3GJ-AtrYXSbf4nCBAJ9_U_J6jxC8_Cwgl3g1xljDFmiFAzKdcbwYcWXF9XDMAuiSy_Lj0wlDrJ9YdwOl-HLqpRz4IKy3OYLfLDagQ3c-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS5-wcs8Lib8dOEBIp4ggO4swlfMcWtMqQe8-pZA0xtTxFb-6-T7ykJQFoulY-_i9s9ARXy3xY728aNqfCAFDzOps8NQrs-3UvALDq9zaXCLL7K2hg6WdXZv_KSmPapDhWLJv7acXHEtYjsr73RNFEMyN7U1GsDe93MDzP7xdOYq5JmmV_Ph77Oit_a1gJ3xWJ4P1T4cb8GdHcqbNwvKIv7RoBIt4bRAD9LPl0dLQXyg2-DLUCCq42wajmILawZypvWvwJ4dEicIQwkPmA4ChhpnTKcC5g9fypDr7u-mJYKp6EwqLQFZdxKRUruJ4jCm62shr43jr8Vd54bTxCznSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsRkYQjdCm0RQsQjDb5vBBAYixARnoeQSfThGdseyDddwwWoyRPsd6bumQpRXb0aU4ZR-ldTClOI3qI8Ba68Ni_xU5oSayEpHfFhS2h6IvHYRvOllOL0sXJYC6fedhR8-OfFXhfzgwoFZ1PRiej65G8kkxJLIuqXYL6cfYT9VeaiA6PDKqPaz3A_CRlatA6DT_TqQ7i3JAfYP1iaK2f7mdoUNiEcG2xj6Fk7SVQLppXI1nM1960OD13S5OAAwZE4LlTPDMNQ_-EYR0ZdfZ2uScJ2mNmk-UjPzlttXzWmcZ5tl5wjcsmh6wBBRYP576nfqFqCH-kjud-3gEUe8N4G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isACpuYeNbFIh0kK1qIA9gvDWehlCkP-WZjE0XgRZEzDyDW4s_WtVjHgoAm9hq-a_5v347hIbnKSIjbkLsJhgCp20UTORSpWfMQU9b-N_rUeuKgTxvZY74SOrMStg2Z48OGlAO_pMH5taMLguN-Qb4ZaKqvPwarSoYaFTwxjvWY2I8v_xmK2IbJOJqrqBYfE2jxYU1KzPnJmCM44I5blTnjjIdAU507WTLdyGBxo-LxTvwl0ydcZQ2vNQmTyhxkw5WkABHf2HKgVlx480EzG74IaibfEXJgdSCK_2D8lBVAvLQx-ovO2kJYoKY4Blxok97kc6yvUOHd6vDjem7oo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urlZd5TZMgYSGIGTUmd_VCqwha8rxEf58HMVc0PXcMp0DlRLQMTCk2hB2E-sAoFVt9WdAn1-Io07Q-qyiQ23hW_gOWeCHWljft-Dn4ArVvt2rxYRqnLATHbZFYRjvFEh7LjmyiMwKO6_w2ZRT9k-yj7zOvOczoxsQ_15wgSKfIcjptI-bdZgYr0ZbfL4qWvaAHf8zDiLllmGqCsSR7tnmnp_xZyv6aLwxpNycEAh4LMxLxpaHFb8KLQGc4Pm-GmqofWG5_XMNAKWoF1RwVfaZnauwg7OkiCOa3WIrU60abYCjY59rF5RC4RyVnCs-cXDpXYTaXPAIDnGKt27r9wzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25773">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oyABkFSmYETdEcqo32rAhYzS0a4Fw8nFwFu0EB0BTNCsvoM0jnUJXmScg-dqRODgd9jjeGEXThTuiak3aop8cQJTUworeJgbBzmsStyVZbRg2gM3jnkDQEkZ0ma7fO8ylIgSqNxF6hAtmVF_AMbc_WCRa2pl8EGaXU4pFyhmqXfTYdCCYd3YdNfYKJ93hZybWPpHDozgFy4Mk_cB4k-abndzM2PBuJXDZVYfwJio_u1D_ZBZ8BbsEQqVkpFbu6sbgSD7q9f7_BVjnR6uQrYd7c2dUWtxTlpyn3b7759sImFaESG-C6eMtYse35uBPDc1vWdBiaqxMDY7Mk-5HE50SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود بسایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/25773" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPNvx9gVJO3LVXfox5jfRbkewAttMPRrwJiQ4igENm6psWdHGSiY62azOkP68F1BjEmV_mJ3YcjutVKRRI63-HmPQ5PUfarto5JoDpR94qmQ-l88wbufPo8qLN661lBM4C4ue1VsTXG9Soxqgz2bxUImlb9qhkT4C_jpcv78QEziBANMEC86Tv2V9Spq1Uc-MaGzUrgU_xTyt7109oXzqRpulPCG0pD5Nko2gPnzb-thadD4GcfNmGzxZw4f0uZTYetxFLSAAG-vmovsjbjyPNPx2Xjy1hRFDroc2rb6j6kWqFc_WEghuwcJAeKTbD2kaX9QB-qTB0_ewnFsLgEcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKBUpOAwpKVlD7Kh48djiBej53eeuXWe1u7NJk2wRpzM5bmu8jcvlpPvXAIIjRcEEQvnUaRz2se2eJgD26ir4JHnSGmmFf9Nyph8a-nPZgzzp2nUy_n_fqvCWyEXsDTw4hdktadctLA0ARXDgXtAU23CX98y8xLITYYuTq9otixhdqbhDnjmuhzfy0tgZtKFPPalsi3ix1576cCx3pn_w-BIpks_7c4NnSB9DyU2CPGC3_sfVIACAskhaS-tF5KEqE1ys44V_ASkePNPgkLJmNGGZzhmkWrKMeN2-AadYQY0W1pW3NNwKLq9DKl-YiGzonftTXmNTodmYYG0uDTqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHituhyojUGvGyemVKVHj1hfRzcbAC1PZpjivOJhOIlqaS33fKtsrSF4QIHrpMYQoAInvatTp7KkqiLJgzgh9F03pt_NqVcQz7xjury2D8RiIXQnALN9Q1vy8ZIg1WTZ-ha1masoizHOLbBVgL319gUA7ckEMhlJZlvwfI1SOQGXlVz1cDSRvqvIX5odSrCWZKmvJa4BfAHyh2kloHQ-hLQt12eAkCtOrh0XyMbs4BaYEwuqSLe4ybbKgvlr9bN0D4bejtpiJ-8j5MyiTGbmDy2N2ZkTuz7kNkrtGRrHKoMh0WgnhcOQSoa3JpBiR-I0kqmF_WYtIPf8gu2TQOKzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCsSlCGhBmocdWts3RmbQBCTZXzbYCfasq7o64kI1euJrhC0KSIbPFovI0vmPpN3mdCP8Zo2uITU6Qqibu9_3y1mqNKU6LQ_LA9YI6OKp4EZBGTRXKHwcEIA_CrIqSuz7Ytkh1iBnha63IUkiwXqJ9fOgVKCh73TZFDMjoMH8LDrpHC9QBHxCc6LnOOr6-BGcVCe0JONmv8Nf6FpH_iQcBYe_I3WdyfameUd2RChQcLcvovuIkHYxrN8Byl7ONHuV8PccStCI1JkyvRR0DWf0Uo-eTMvsFQIxwiT7aua7gSo-oO1HT1y8SO-LYqooEg4DnlHRjgOEForRDKnOU8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TArVDF089jWJpqXTMjCpL7y0EnCGqL6cs02Wk7LEDSNIr_quO-6eLzGTq4CvYFytQFsWfAt68ZHYadxynKFHT2uKu0LgViororyuyy2_O7uv1Rybv23nE11cxxJhI-fMsfBi2MkMoCeCPggb1fTfjx24QM9Vtne3auSZhiUN_2FpA0Igq7d68_EX8z_5K8xe2RvLmka2zOWod4J35ugly1vZl9e_oc_1QcTJ5PMB_3dZrMIPbqFuvZE-PYeep4tgI3UEsuCI_wGlz9VrzCE-P5PdnmVLAVgsDakdsuNoXqW1JCf5D92CgRR0NwTcZQuhBmya8kd823cD95Te2nXWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpX4iCHqNSUOxix6XXQNelmd0hoEKjsR6naRPHpDPzbsg9Rn1xyJSBGp55BlNl3rl2lCI48FQLIZU-AYf7w48jNzKxk6oz9Hsx6sf6oWHIV57S4YLUA4TOVXgXrW-osX4yGkEYXWIrl4FbR_gNQwcxNgPGPomya9a7Bm9viuZlHBntjrLKnAO2ROabyjJ5McCq3zd7Xds3J0-KibYqGQ9Kk6jCmU_fhc1E01FmBPUtnoz4IcQa3WfMyL20zFqIolsmv3beKUmkxanSlVvoUl9okURNm9Hu5SzQe9IDFE9sDoTblClysHzP4wPy0TnZH4nPjuY25-XjEQ3lPMBOVG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=LlIUEKYPXPKHZ7abKr5gOW79FwmxmQS62GyQ0VaKEJrJ72o-QYteqoe4DP0T3pnuWst1LbI8_XvIE4m-omm80S3jxfYKXYtXYwLO_EWm47tRNB_Z8c0K7BXXq0CDC36whOB6e0EGUXNm7rKD4lbck6WjjmM7upglcIQ4VWZI_qhRQh1hXxMEGHQhlkohPiKk98RXLy2iL7Bn6tm74960xfTdGrKO1GxrrnNSY66R9NF0cJuBecUOXV-Z_kE39P3KRQCBGKLT-3qBmSVHJmZl7f9w_lqQBtecpp9Mh1A3GlfYqIAa-I536DlvbMy1K1CJKMb9VPrNEK7dLbCSnn2vTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=LlIUEKYPXPKHZ7abKr5gOW79FwmxmQS62GyQ0VaKEJrJ72o-QYteqoe4DP0T3pnuWst1LbI8_XvIE4m-omm80S3jxfYKXYtXYwLO_EWm47tRNB_Z8c0K7BXXq0CDC36whOB6e0EGUXNm7rKD4lbck6WjjmM7upglcIQ4VWZI_qhRQh1hXxMEGHQhlkohPiKk98RXLy2iL7Bn6tm74960xfTdGrKO1GxrrnNSY66R9NF0cJuBecUOXV-Z_kE39P3KRQCBGKLT-3qBmSVHJmZl7f9w_lqQBtecpp9Mh1A3GlfYqIAa-I536DlvbMy1K1CJKMb9VPrNEK7dLbCSnn2vTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr-c7cKrdsUY7C3G3wLByU264hwpgUXB5uRiaPb_ADSK-13RVet6xZM7LgbYRAz5FWTFyQ5we6k7DjXjrus88uFeK0Z9AKnRNsG9tP_YUoMhvXHt44SU6LX27b23tGIYJDfE3YDHs45e6cakCsRltgNSenwZ-dbNXCjTijlwVxc9DA8fgr9u1W4J6BqJLdDHErIIfGGOmBoy0T2w3_nBKNBlI5-0oO5uGF77Ykmp2EHUFE_WiwZxsh-_1jOFVqNGe-vV5ALfLyowxNE6xfM76ovInvAPCocqVXlDyNb8ZLqYuILlbzjEdCYcagQ_J3Q07MKQiUwdeQ7LkDz_VWB8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSxiDmUU14fzexx7FJwsNap48J9S23ExhiDuC7JLephYrW827OLRalK6GHxVSp4REtiegJIaEDjgrfchVZWwhsrmTzEvZeMOl0nwXAVksJAwzrPON0N6rG5LxW3kGz3H_LQlVtdCPH3OeaIC5lsD8Ly6DFddpUirh0ChUYBtKgrTVgmRSHoy9bc0v-gqxPmustoZYsvGuS2BL8y_h5795z81jLSHh_laxsIb3CtJeZ-ENDCc4k7aQzeX-0wGbnedKd0iB881LHoUtejakRh9FIh-vYzOCTf0wBan18Rq5qSA6Tplr3L1wny7Zaiy0TX95i-wIQgPbsCE8G4ubQPwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZX430xGFZSQM1ClqUkJGiWafk8rF1Rh4msCIaApAmWIL8mPcd6YYcmwOX8j0Qjyu_6Oiv11Gf6BP0AosnV4c9U73Zze8HZY3IdEa95K2bwcWnzhItrB_uAiWNcb-fDhX19WpdrVBkF714_hfOUpsCKsVDKf8JUJWhKxeQpHCRsGFq1aCRqhRBrkFkEGY8IvnInvnpwQw2e8Uw7OHwwHd-_YI3XXTbgngR5qUSghHvsoF_EGhtokldio90qYdDqp-wGZ-FdJUtgvuM765vgAEnZLrI8NUHnobBQA00gkz5Crg8bagkuizcwP9PVqiGH91hUvT53m0_OLfCALqo-E9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=Hl6-juvjffctWNH7QyHCoEilvcEV4ej8OmSbVGcavZcgNSnRwf-wqqx7gS7F_aqdLdOGmyniLy9DkWDR2bACj3Z-EwUqB2tG3rBDRTzYj76rDMs2Mt9jAaLbODq3TN5APqqQIoIpQByETdtkiXDLzC7Q29VKPLYFf2qVQ7fSn-NdVAav3FJ3ix5h57zl_JBh_Tlbhl5b1bS-brzjAB7_M0AHKXCVSquzl6LcQjv0dCBmLKev37qIPoc5YE7ikrAXqiHuFzSfT4e2RXjfrVGEUXT6jNDHelvtbBB0QBOr_kebzrZGkoIPm4IM4gH1ZxEs1Kbo_RwzK2k9sdBp_H99mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=Hl6-juvjffctWNH7QyHCoEilvcEV4ej8OmSbVGcavZcgNSnRwf-wqqx7gS7F_aqdLdOGmyniLy9DkWDR2bACj3Z-EwUqB2tG3rBDRTzYj76rDMs2Mt9jAaLbODq3TN5APqqQIoIpQByETdtkiXDLzC7Q29VKPLYFf2qVQ7fSn-NdVAav3FJ3ix5h57zl_JBh_Tlbhl5b1bS-brzjAB7_M0AHKXCVSquzl6LcQjv0dCBmLKev37qIPoc5YE7ikrAXqiHuFzSfT4e2RXjfrVGEUXT6jNDHelvtbBB0QBOr_kebzrZGkoIPm4IM4gH1ZxEs1Kbo_RwzK2k9sdBp_H99mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHqCBlN9Ph6eH5GT-SSLesqecRC3UittkxMKQn_NN5XScE66zhfPzSm9wgknrVtA7uHVPspd-cnXfv-EeSRUQS3-lthjrjL47-QCivSQh_SUiloTQCWesU5Es3nCqOK41eA4pMBWv086MYCYMWm8zUP1o5qI4QEESrUETcUicEaGkKeP9q_IfjbjsZSoNoDawdt-_U6rqrJaBzGr6OH3Y8Vx3Ab4tMpK4UHYa6uTvI_5PuB6lEKz_p5jWoCFULoRGwTcxi7mG9sn0qkNyGoShp9a97YZSbk6b0NJDloToO0CNnHPGWUFM3RWC7YbseaghgBqBwjfZ1mVsrM0lDexOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOGMS-zZCvpBQu49hqVFchL9Uaww5gd-7lBmAINn1E1faM7XJDizyyEJ0EFcWFAez-SqKfiIhHQoAwvBuIU7KJV9M2sbsM2iC7CrLTxpWtMBw3STz5XwVu9bywOtfJ9WBfBtL6G_6U1YdrvnMNJdZsWTrdCIA3TIF_t4jH1b_yytwMcuIO0QaGcQ8Eu8HFbMN3lQcxnO4xF9TgOfDvN-TVX7nlYXmxbELHZSOcMn4rNxDcYRQnE_ZO6MqQd5aNIiZ71XgqAmCAX3uhLtH-CD0ZgrSo6fjw0qizwBc2L-gxfqY3KiJU14Cmj7fHEbUul6FlG430z4Yjqc7kmZ5qKWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec4JG9GNJ1s5-iXnjJfDioI0fANMJUPiaxEHDA-nmo2iUdFHhdOC6H7M64utl60olRcFu5Q6ggPfHtdvEriTwZ30cComM8Y1UVlTl4wfqj_SeuEwc0M2PsjsB_6BY2hg5-c4oxDxQdYDn8xe6hIfyjeJP6zddpottWhnhgecvfX0h3QzyIW2IIf85rCEmnhqARS74vPPoF4Sj8wCzSw_Det8z4lzjk8OUB4xIjH9oi9PEhkL0n3Q-z7OtVfIpgShbZwoNptMiUBc__08n2cPbcbLg_HxwyKiM70OdutQ3AvoW-_Bgl1f6vBH0l5zfev2lMIVrjiV0AzKQ3dhEzqakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKv05iRbg_w5qmDgUGZT-U9QsY1kIcHKl4V6bhbevT_rm0jOOOD-1IKAUt0khezXhVJMwBrRC-DAwBmvYnK8CDltc0Mee5uF3hMUgRe6jvvCFVKywIM6RYtdhHJVeMqNIfSsj5w0ILYnDTmT82QZH-2N80__8Ou3YCwtRCK0Tlxcx85CpIbrmgqFN61tykSd633LRtkLfLS0BgVg0mhLAASdn3uNhxGzoJgNx21lp9bU-Mg7BxZdNfjVTzth4EByGXLh2pPCtHq51WSmWkEScdyUxWQ-iNc5yw1eSA2jCucJgA1L3GiPEPxY2X94l6yhwOyuqvixkMmy6UpaBpwXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRP5ammiu8y8AcNi2fu15ogD9zUs8kT9t8DbieNsB7DphgoqkbL6jebcKhDn6CPEyV4zMraZk2Erg9LVygaMaOxcCYGrFDNkAtUiVV6oN7tb-hcabQIfsEBFQi7wLnhD11D_1gA0LwbvyvlVtZsY8fOZzXYPzUlcHmxQEV9L_rZXyP5tzd4RwCsglSEKl_vZAqcreUQQfNFDB1o7kqDpobefPj89vANRAP7hmr_EoXzzCCxLOb8awR9qwr0M6-9XWsOOkiUvqNjdqJmtsogOr-iLhF2ZDxxeNApBGqRlCG1y_xVyB9Pa30kYK3lSbJSixBS3YSFD_vMRp7V82T8fOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGWRl7JGFqhG07MHgWG-Oh-Zbm6R1qv07dVgmQyl7vEHG4sMrPCQxt-Rc-hMPH1AmbOyvLRFKqTkEztfevQvl23EHB1LnW9b68iER_mNV8ieDlOuyTs6ADnZl_UsBDAw-lO3be9k2yz6AuVoLDwcNBSHjtKuw-zOJeJPHewCB8mPGuk8QMK-PrClpa9xGyQe8o4FXXJkRHaUcn0CkrBatWX4ftoxzx3KfkL-kdVsE8R2WYdsOoiisoBOBfJPsaMXOZc5KR3fv6ZHw0TiyjOa2biR1PC1yYm2OqkLsvdIbWvawJMYEXV5810UrLA7BPVXSyQRe6kwFuoE3dp9f29BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwp-az-yU5-SQJe3gezLMywvBxvkqLEP-Zqcar38tP1tQiq5HDemCpC8YFearJw52Eku-4CbmRbU_aMa-vGoZeTMl8eXZ9gw6ivXB69Nwbv0Okik_hXUjRn8erFLcM641xWKX5NNdKBpgj1J9g2JwfLbctkRzPmWGYhYIjv7uQFmSgssXTJNuRJ7eq8Vf4n6ne10BCpekl61bAuP_P-aWKxcrD90l8tggVgq1uWQtOY2-F-Ub2I0GAZe2lOk64x0Afox9hdiDjzwCqBOTjcL7uMLRGPT9HghLZ0HS39T5dO2dPws8VTWEd-5MaqhhY8TGyrscPelH4W8Zgloll_l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap6J8Z8v22e68jgA8K_d2vFmKLN07YlB1w0VXSHUev8Aw2N3-ORX2j5_LcKSZmdeRs6WRCUKb-0Colq79JfmIsnqIUZlepDdZfJ5N0rryPxFYhfRXWgi1AM27giqMObJjOSUo1QrXnKtSOuSFYFbH3rZNBjwsm0lgxE_ZVaheI2BJ4e5LfjnpvM_4giBGITlljUWpJ79B-b5_RouC17xO2kqMrcpL8zcMVyiVQdKMdUFWejvzI8c7kNhVvwBrd3zPeL7Bod6KZXsfkttybr9Fe-Nc8qD5VuNrp9ighBhPgchnPj_kJXSTc7LZvJGRbUOjU0zQMfMDgFy6HVt5EoC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtWOdb-g1lc07xnC2M2hSLsZdBb2P5_9Gbg0qAdWpYKr2rksaYYCGl7H5tBDjASi2SDNLt2-8gNXbZKvX_6sw52DE7oMwn1-xJ3lP9hd0jSoET4KC8HCA_IE5-UwLy5ri9dQGplXH-iL8fYTYzyPy8EeTqtEBOWoGoCXJmsge3io-3Jw7T1PjaFbP0zpg7ahtZS7U6Uq4eXSfJPX2MEQGrL1SducwqRbcOEE7Iac7-o-95d_wQhdpbzz1JRDiUkHu0pPO7hWaCPpv7jbC0xoMatInuqKosMjrre3RN6OJIkgtRULgZt2nX0Cl21KNbAgj7SesakTwCpPx1iT08XkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB3qC-glbsoN8z-7G8g5SYBZ5DDYk8pO28AmSyIxZDI9i0rRmtoMdHIhWO0B-I8bn27jlKMo2frw6U41ZW6b8XL0Jz7v6GG-ACQIL0vNiq_l3slKzJA9EVo3x-US-YUzJByhzBsM3i-SKTAhWicuqnr-xsPY_3__PcpTtkcVWlauFH48FsicbYAtyz06iSNrGqm0yXt8tBx0C1O8rdiGOfFeEujyS-2jeOLmNsDvAyz6NbFLm7CPAA7SCEeV_yKuj5hOXCVMXGet2CmsCfpZ854RoGSu_3jKknArk2wRikwHo8ldPQ1ptheiYgBj92_-0zFEBNrzYttD7NYZWRsSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCinNNqw6Xl9mcnBDbGAzM52aUEgeud78nNvWZVTspjBpcoN5ZlaTfn0Bo3VZaiY88V4NsLyzhNyszYVYCjc-n5p8YZesXoRZL0kW3NjfYHklusI8S0KhCF77hzFDx838kXsarlIU0KMSLu4F0ECKXCnossS-qx7tZblYNNIXFpP3NXuiKw-3a8j2CIAso0V_XQWQTDm1qsKBaO3K9GXQjV1EDyiBHRPGRDnl-lWhAOq6ia0QVqx9agEb2V03896UhxdFq1ESbsIv4grBt1BKh92fkdQoTRuGo2DGVTaYkguG0DUWF-clwQMnWHpNdSS-k0Jbeiclxr3ZToMgAjJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9jf91FSqqEDKf0JlRmn03-OUum6axSXHjRvPJutVNjDvK1ZLxNp68a6jOVLGiNmCzUiaIhM7YZeGl-VUHGAH67R9ADrbW1gvX1hmaCAPr-Kd19UxerSWC5uGusrEowyYG84KSHxvug4_ipPpjpRHxlkUBaKAz9IiAHElO0kj2-R521Bzy7uE3dNzhTz1fZXlr4ryepYIzg6w_IQNNCulyI1dOPSMuN3czo6X8GtmlS6wpn1PPp_wrmRli0EGZb5uAtW5M6Czcxf5rHb8WPjzDXQRU6N6eqY48phkmJw8VDTR46ON_87Jjt71wpCPFdxOXjtDjGvo9lEeRGsZGLyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNtf-VoGrLGz_c-JzFXk9BuBDtnZiDHmJlKz3x9lqXCr84JA6hCk6gAJoEWa1m1zX1_NnIkqw0sCowV8s0PC-9huwfo6DH0h-lhSm8145QNke8csWpDv9cekpQh0zxGqWOMc2dnjfFCUTALIH-dmJF9_epJheiQYKrBy-NkIIBh3wXCAklbJVO8Ksfi4yA34TO6E_kn7D_8zKGJMgqlvRxEJ0Dhf8fVQ7ZMWd1mdWOyg00avZh1c29xM8L9IPLqtXGxq6XEl27QXOuugXca_z2fu-lCLlF8MBmkL1iKNzW_N0CSUSlBRdXf0QubixxgXqqp-t5PbNuMv_13a4Irm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=JDHhmoGCwlpAsAqgtzleIzcgojsJTilhz_pyI2HiqM4n7L3Z4BuJh5zVCKr89B3VOS4LmRJg4DwN0jPjaZrrDDitViYA4S1BoQ64Ja_FCybe32Qf9e66c7JiaRrQAKOH3RnG1FalngZCbKSyT4yChfUZtYj_3GQC3t2mJbAJeq2RCzSyQzTgLXhV3RBpDSW1ty7JuYAWAA6d3NFl0lzT8n6hJYH0pPs4tgyVvN9afVwYLFPMWdTXQeE6Zw0tO_-RAISnd8MsQsiqPvJztNthniqxD-VSxf6vI54BN7q0woiJlvSDh1o8OuP4xiKlI_xZ0LtGqcZORVqz7WMKha2-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=JDHhmoGCwlpAsAqgtzleIzcgojsJTilhz_pyI2HiqM4n7L3Z4BuJh5zVCKr89B3VOS4LmRJg4DwN0jPjaZrrDDitViYA4S1BoQ64Ja_FCybe32Qf9e66c7JiaRrQAKOH3RnG1FalngZCbKSyT4yChfUZtYj_3GQC3t2mJbAJeq2RCzSyQzTgLXhV3RBpDSW1ty7JuYAWAA6d3NFl0lzT8n6hJYH0pPs4tgyVvN9afVwYLFPMWdTXQeE6Zw0tO_-RAISnd8MsQsiqPvJztNthniqxD-VSxf6vI54BN7q0woiJlvSDh1o8OuP4xiKlI_xZ0LtGqcZORVqz7WMKha2-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrzsifyyTMwTduBo5AwDx66KkUeIxrj5TmntEJqdm4A5dGD5Yj2JewEoiMFdMGxNHeTMHqWU_vzxhdFNjzns1kwPvbSX7vGVvihgqVr2TO1wLlNdPH5b_i2Zfl92JQBOQi63JGSo9sT4fgemFSahP7_Z_m3RQySPKn__ubkYUUwXWACMt6UBFLS8m8xf8yf8rh87Oc0guhse6385fO40Xqxn9G_8ZtdQbXvHuQV6b9Wv0hLhu43erJl65VT0RrL-t44hKE8XxXUqKxNRaUHXV795p059PCl38EvS03C5Rb9yE82MNnwQ0UdGaqi9wHOhxh30eTVukeQnW41LVFzk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsQq1ns9KsKe-_dY9UjBI6luH5ZYYjEicz-vuXmbCmECTGs6wV1CQ2lWYHMCxABIUEXcwWOVQCMBN4YB1D9S-C16japXVzSfHRc7tSQmxdhca3dWcrS5TnA83K4cRntARCA-fUUjsDe-S7c7C0JT8BKbq4fXKWwq6KZPET_a68_nk0snoIfHhhFyLXbaS6WdONmiSzofYjUkx5JRjELnHyK3v5X-d0l3T4CFGi-pIhI6T0d85oWhLQUkvzDMP-A6ZCI-TVjGu8ZTbJcFmBkphdMt7UrY8vrGNPJi-PPDJ4kgMTKFbs1L5-4HdbmyMIIbSeY4hEqhixRvSnJ83uwBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=Gbg_qEhTJJdBamgQ_Ewrf63v_-BDWDkdeCf6DqfggwQTLOjyAhOkAcsp5cwJMxh4nBgKUJ2H-tq49iZTvSKxJ3TV4zQ7p5ny7_1fBdBLvZq3KrqWoqrYv8sCDbhxjEchKA7V6orfWo_V5bLIocspBAHlMoB8-2cPbAxMpMjqdQqUx30sJbi5VKk_MpHJcPQn1tUADptr_ceph0GdcdQH6_yNvKZ-BUns3Kr6SbGtuLBLKc5EBP4R9vkJhDam9UTFJWOoTc2lRN4X8xrX7OaH-LTIG3QA1y1eOEr_8BoL2nPYvscbbKj6Ka181ulTkTSjr5rMCklUI9EZr4W65Iu4HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=Gbg_qEhTJJdBamgQ_Ewrf63v_-BDWDkdeCf6DqfggwQTLOjyAhOkAcsp5cwJMxh4nBgKUJ2H-tq49iZTvSKxJ3TV4zQ7p5ny7_1fBdBLvZq3KrqWoqrYv8sCDbhxjEchKA7V6orfWo_V5bLIocspBAHlMoB8-2cPbAxMpMjqdQqUx30sJbi5VKk_MpHJcPQn1tUADptr_ceph0GdcdQH6_yNvKZ-BUns3Kr6SbGtuLBLKc5EBP4R9vkJhDam9UTFJWOoTc2lRN4X8xrX7OaH-LTIG3QA1y1eOEr_8BoL2nPYvscbbKj6Ka181ulTkTSjr5rMCklUI9EZr4W65Iu4HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kPzAIRW4G_I84HIovivH82wbVehjwaoMa1u4yQF_gmIvlLqbAAy3U7SPTuxzWsQ2RhDCVJv23VntdOTErRGuzZVhH8X7otDnNNChKYJI-HtbV6Q7yDT5WuJs8QRtmY-GptI5BY_ejomPpouWhams2kk5JP4F4IyBxjGzntYcFwALFJwsETy4Hbc6HR4TRvuyA4qo8xnXMcNWEXkpv2JQCaD4JXZKxge6s5zwr116BzrO0fpzoC3cdHghLYDDKe0vWZsy0RmT15SYttA5DyblG8Ll1-HkQDDnACr0bAbj5K5e7aiz-z6M8FMmvOaMHQCjQ-cS_cg3jW4xd8uVK82paA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=kbeOVKVSQb03ULE9RCV2lIiP3JhW4OkD42Et_blSHyZXvbNxgbFOTCKghYeRAViuEmtdkX8JA5RbwEqvXuyf2l9hXOigbqFIyfeQt_PLVxflaCz7x8BLxeRqzX_QUDIw7hoD6hR80di7Hy9BsqmzAelpjCQVY86L98u0Pr_SbZcTbomM2VzJr1pNdrQUs5nz78UjyN2XcIeAY4BesQdGeDnbm6Elj-MTFJnaBPqNPkq_IHPiRLN3MA8qNJMb87fjfBYCuZbsGgX2xNinmoRf5vehp4LeiLk6lHNlIzG-VVhT5GHuUDPxf4RVBJY5LYwEDGORJI4ErdSUKXz0QrF6EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=kbeOVKVSQb03ULE9RCV2lIiP3JhW4OkD42Et_blSHyZXvbNxgbFOTCKghYeRAViuEmtdkX8JA5RbwEqvXuyf2l9hXOigbqFIyfeQt_PLVxflaCz7x8BLxeRqzX_QUDIw7hoD6hR80di7Hy9BsqmzAelpjCQVY86L98u0Pr_SbZcTbomM2VzJr1pNdrQUs5nz78UjyN2XcIeAY4BesQdGeDnbm6Elj-MTFJnaBPqNPkq_IHPiRLN3MA8qNJMb87fjfBYCuZbsGgX2xNinmoRf5vehp4LeiLk6lHNlIzG-VVhT5GHuUDPxf4RVBJY5LYwEDGORJI4ErdSUKXz0QrF6EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv4bXximr_iidTDGeRay6oj6vfQvqZuNhbC3oYfbMh-3hrKzTkrdxw64NtWN_iL6D_dzQtPJDy-CGFbIJOp-p9JwYGRfqT07L_qVw6lr381UA1yTGfCmyfnYGVY-Wu6mBERhSrfSh77_1HvhkhslNblKLgxIn0WytjChTSFMariQHP5q6iiYOFA_t4krobYVmgKD_AJ7VTWHpieBke9DK1Udupcw5FY0bRVex6tTF2dCWJT93WhDqGOpDcVnd00wsOrzUW1xq0fXEd2DRUqBmFaDW-mAtOzsGFVRuThttd2-k6yU-tg987u-EPI0MRMsZHqPrIGSjIkZjcvJkhnutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXVcC7ATLWoTAAcgKlfUpW1F9kUvVKOe6pAnGoqlqEDGShRBbqA1rlkRrdv0KJFTeEd9EwOKtwRLt7IgJJmTWAywTLU7VjAWfNE7Iwwsgf9XelH4ZPA5GBbpzRtaQ73msNMbTKgGxVGCxOhPPF4C8ibhZenPlIST_Sgh6zd1wkrxsd89KjowXAzV_YlPxamDndq_rO_OvqvBD1E__tp5dYKww5kE0lFmYrkYVXsZEFQvpu5dAATIzRDPmZapWKif-kMp_MwW_dzrDQCJjb3ikFihIovV-xdTg4LZ6VouVMvwJlfvGQZ5Y1DAaNR4jnZQcsmoWVPDcxCEW1nB4E7XaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=AUqsIz107HuWr4_chdCrpYBxumdJCZjWtmZno-MVSpFrIL5XxQ-VUMhj6bl88e7s1OjtYjh50kbA7UgopSoVv61arXmP7yETkkfrnh7pH8SOA2aIkmkoTaNLQnkLfFP-3Hj-JMGGbOq0FQDrlNrLkcpjShGTGRHxBKNkYx4HK8TcqowFtgEHUe9JffGy_wIb1Ai_H0htPeExgoaJNCiOw32uTYnb8OvDoPCPvkIZzlfYOiwtpD5uVtvkQ-kgH9r-glAcxaIxQInHJrN8q-MyHxfVdDyDtBV7Tx2Jq-ZqdYxDNavbi26deBirLQ3UL32DNBgv4N61DGETgs_-rTwQwgPZ0AFWr-AQZBqj0aQxoo4RQNnv_upRzDspvTbKzakPyWrACmAfgEGou16o6CvD__Y9MXh_juxmvsSicWQsvePO5vzACNmjcPTPWBZY8nN1R68O_6XRFjob0pSuhH5j36dpkwscld5TEM8DCo3C0V5dmIhS-GGo-rFD3bPuADZIAHQo1pukJ4lUrN67UxlEjZxqtDcNQJMqxvylhfVT4IQSPyypczeNV4NeIcHzbQGuRpN3IgW0MqziQTFuPBG4UOvLUOuJIPKEltRkf1EKa_t8LhUGY92hSfezOB3YyxRCCCufLeDl3L2UGXFDRHweBm60I7GZZDU4G-dINHvkZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=AUqsIz107HuWr4_chdCrpYBxumdJCZjWtmZno-MVSpFrIL5XxQ-VUMhj6bl88e7s1OjtYjh50kbA7UgopSoVv61arXmP7yETkkfrnh7pH8SOA2aIkmkoTaNLQnkLfFP-3Hj-JMGGbOq0FQDrlNrLkcpjShGTGRHxBKNkYx4HK8TcqowFtgEHUe9JffGy_wIb1Ai_H0htPeExgoaJNCiOw32uTYnb8OvDoPCPvkIZzlfYOiwtpD5uVtvkQ-kgH9r-glAcxaIxQInHJrN8q-MyHxfVdDyDtBV7Tx2Jq-ZqdYxDNavbi26deBirLQ3UL32DNBgv4N61DGETgs_-rTwQwgPZ0AFWr-AQZBqj0aQxoo4RQNnv_upRzDspvTbKzakPyWrACmAfgEGou16o6CvD__Y9MXh_juxmvsSicWQsvePO5vzACNmjcPTPWBZY8nN1R68O_6XRFjob0pSuhH5j36dpkwscld5TEM8DCo3C0V5dmIhS-GGo-rFD3bPuADZIAHQo1pukJ4lUrN67UxlEjZxqtDcNQJMqxvylhfVT4IQSPyypczeNV4NeIcHzbQGuRpN3IgW0MqziQTFuPBG4UOvLUOuJIPKEltRkf1EKa_t8LhUGY92hSfezOB3YyxRCCCufLeDl3L2UGXFDRHweBm60I7GZZDU4G-dINHvkZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nagFu65hY5USn8Dbq1fin3WZtGkJr35moOZqj9VvyhZEbdP5rrZH8t6nG3tYYIJ6YIncnf0bb2PR9PtjhVPC9xU_P5HLadTcljuTM4Rhbbdsb_tjqBLNghidMx2tJRIuIFp46xC2ekJGHMzsI2HXY17LKFj2Xu9Mf3yYySEA51sUf4PMwMkHfwEDNakrhBvrqgKd4S3lx1s_Ez0r-Xh9PPmwZHxK23iiv0we8KgTQq82WB-tU5IMT4hWBc8KSVn0yQ9wplVpW22oqSJKpMHVPfE5lKCvuVLMYNNIHiUQDxLaxJCBMg5Aa6BFAoW_B3uh2M99bRbW3msFh5ojvVBM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAI6TAD5HwjESNZhNE9OrgbDtsVo1-FfpjFDZAG8FIOSgfIszhfaKx1saD6EJM6FHfeQ12vhjkkWBpVwe3z7RlxpHKCKBQa-VmzdMECfdCT-S3Y94Rjg80yXmPwa3j7xHXSYJGNP6lFDuh0DFUwV4g6-cePwMyGb_ejwxirn_F0UjdJhJc7-3hRkbn1J5eBL-1e30TomifZyZhErwVwsGcGm8FbkYDcXtSst12cosprYYCB0-BD6vg5hJgfeB_Bj1J_BBuhmHMCp_DjrJ6o9KinbTBzfU3F2bNhLRoBcXm1pwHseuV4bPfhTdDY0uPaopCZQiN8_qhFoVhk5UgkzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y126wzKdFutMF1O0XXqpYKmnATgHH0J7eJP6iDgvyVkR0Arky9a9SQMRKX9wxAvCtmZMGcVXMqljFRWrhulKJ9hLZtFwg-V0cfK5MrtzS0eUzoH30GtOh7w24lnytookWdFH8qQDGazhPO8uRuD0-3wMgGrBHS8IZ3OqpA-VdGzqzVSkq6TLFCR1Q_fzKcMXlZL7JzlvWt8vP9BiAWR3LHVJJQWP3jTmU2myUhvN4M8d9F-RkJj79l5QU52lL2ZebH6D__GW1VlHKPB001VqGwGOuaK33aTTaKW5vRfoZ9PELatuZTaA2oYsgK65D1GF9C_ZC5EIu-3Oe5mSzYfzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcIUDJ1xFPHY7_utCd-P1d_geYIVjhBuQ4x6HtogrRE8KN9EcErT-XGMczGulbxHNElOigRMX0Py7BJg0b1V732UzmOzyQrZLZOSLoSS7qTBPeLmF_pae1ZpoPo7IbS8UKWQLpUrv1JzPmJ0MWr4kgm69EgHXS0YmSC6MJnjcVCs4eKE29y7H_Ci4g95ci3bERkWOb1g4_82LHOntGwyeYCKo4hyVqi3RK830qzMY3Afc9qTZ4moHxv_Va17LyacUmpH5iX2AUJ73DHhUd5HjzS-1b1TbhWn-ZqTMX-Fo25bi4-GruwWWSFgC5q9YnrOIjpjc7lbHhVRvqZDgp4_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=Vf9k1sqW7OkZFSm04yoshws6YN-SvyDyM3NOv1DBlJqlf7sJ_c0Uz2inQ7Q5yIqX144c7o92Z_nGqtW2GYQcUr5bWKosfCVzEeGLR9Q3Gs-ToIKYMraC1yGZr8q5jJu_g1dvxD-dYLizYHd159NIwpt0Le08cJwK4enKPDVBxq2yZElmmumq9vRa_q19IOtVHM0ivStfkKq8cA8ZrcweO7uGHy0Fz0nIZEveN-stZRkc5vQehjG33XtprsQk0CrM8zGtO7Y2U--Ir5TD8YJlare9OOxz5Cqv3578Y1wLVtoe70WWdLCh6fDpWjAhKq3M2G9Zbjvd4sWEetZVbZxyrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=Vf9k1sqW7OkZFSm04yoshws6YN-SvyDyM3NOv1DBlJqlf7sJ_c0Uz2inQ7Q5yIqX144c7o92Z_nGqtW2GYQcUr5bWKosfCVzEeGLR9Q3Gs-ToIKYMraC1yGZr8q5jJu_g1dvxD-dYLizYHd159NIwpt0Le08cJwK4enKPDVBxq2yZElmmumq9vRa_q19IOtVHM0ivStfkKq8cA8ZrcweO7uGHy0Fz0nIZEveN-stZRkc5vQehjG33XtprsQk0CrM8zGtO7Y2U--Ir5TD8YJlare9OOxz5Cqv3578Y1wLVtoe70WWdLCh6fDpWjAhKq3M2G9Zbjvd4sWEetZVbZxyrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6MShhXRj3QdjIj6_ihfetb7ANHp68nTvJSH05Xt9z4avaoCCjXNrDmC_u4LUPimOnskHN9Zf6QgSUcLSo7TNJvHzBPlOhjNIsdRB4Rh8pBpGKbUC_5alNTCVETdcYoCd0Ber06cVFFH8DQuPeTbRU1IlSXDhLyQjpVO3ct23jTm43juurv5DfieWKXDL80508PnjCqoaSPHx32zUjA3PrPnNmSpuErWf9poXP-tgnt02DxKPkZAp-cFnAyl8S-7phH6zVgHj5DRDmu10bXWkIyLq66WuD_eEhijX4umMOtW4UbQjp8JbRFCa3_S8RSpIuL0_O5kWmayNZyiIPfJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvBf13qkYvjM3gmlv6rkw9N86PVRNzGvBC77kR4lHr4bu9eTV6SV-Y1rC74VNtrVykD-KSjUnpVkKQ6WF7f3IYmkRZaavPRLs3Q4W1auHZy63xS7iKh7WFwbg8VttHzwmtQOMTJL5XTAXOffonyrQwVlBhN7tMGHjmUQWhrO3iqfahqYZwLGn_TFeEIv7MQzDOIN_5aRMojrZWnjuCAnzTIljF2FlYRYFWVe5lirmzhbw99dkLpZN-jFc8Jjn-7M-hCmzMc05diYKYNDhuPBnWxo5SCEIQUqEa4E4r1nCAKNxe_qRyhKQzXMLiN8m3Lvktwwd5cDGhZ3EvTtcE7Kxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_G2raid4iqIeXHEvpIdjx6JnJvrcY6ZNJfE5Li4T_FLpidW_aIcIXu5Z6q3I6vwvEbHYazuB9tlMCexazbT_qpkydkWrWadc5pbAe_8ragxXSpDbOo4pOprmnvVXb-Xzq2veNY_TEzU5cWBsolQdWDlIQYrLTDgZNET8IgGOIrUDe-UvtnKW6bC63YF60bzd93qcBKjNgdGZ5I4_LFNKlbk6AjL_2tERC1wu2Lu1svAj-9WUjLdKAPdxHPUkpuqNLgH47rWLwLdDM6gFEuM5E7cdikAfzIRJh6aioLgHyMXEJ2RCdYB3su8q_JTdWB9v8bN0nqa5AuMiS_3Z2jOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kri7vuIid8OxrSbGJIKwE_1hbTxK5iC_pnHyClweWyBL2NYLiTvf8JB5R4eiXLylh_N-3gjb3u9eycnl3tojjaeYV6AuTE_LoB_wHRKFdWz2JnzoYh4OsmxuLqCOnSM_KqrXi1c-69xq6w1l98wFbolqp1UMeMkjiig4tSTALaqhVpVesPORdKCpxbr-QLTRvQxMUYEQBmim_3xMiaVRYWtHX0KEQxiJfikijlZcVQrXljnWJi40JjF4M5x-22nR95UpJu-ZjWYCxU7Wl7eD-2pv295aZFZeE7Dg62CdAfhRgP5uDLle45lkNAW6M47ER0JsqIs7_DMSJ-OBNoJZgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ML05r69nHjEHwYx6Hg88KsaNFudouhV-eOxRPmXxdEjIm14cWSTzMP8LkvSnhd4rex_4jiypUTWRMdCbGZthnUWnymXsmzS6tQWUx4FlblR-mEeleyf2UInS15zZXMA9gb135-r-KRr_7V8Rp_iHykhsMhvZpLlPYCF7xPHE2eRvHbU1HDjlCxO9naVzFtORl8ThMcu93DC9RpLCwqgxZqJN7-UPnnAqaGNIj9cLlCEfA--093AHK8yFuAtKklWBJC0bCPXTpxjYVhzvyUmrjvyw2Rkx71hHYddcpcxGS5FnylAT1XMJ_p3wBRkB69C77XlB7IV7nY3AilOdL7s0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSkhB5pbCZTaHD_66SzeRJ4I6Le-RaPmpa0evCQyHtANq27wwjCq4GjvqSEj8xrs4VcXe9qoGfmkJ0Jt0jp6na7nh_0orHSrJTwWA5nbgaWCV4cZB42a7w-mEH4aCtWmWLm84ChA3zWeVO8tLBuOqxXohsNIhH23cMKgmszuRFgBJxAubTSHl38B7n8nsn7bAqaQkeEIHV3T4cveYRYgrymPQHIvw0kTMhQsX6Baiq7UuDYy1C0uUVCkygiKQNM6v3ehorxvQbUxA9xl1d_pwW3w5OPF1LEMS8fRzz--3jWFmCgfL9AnaTU2JKz0g-S1y2HyIv_52nPMdh3IEPGeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFlayNCujQMDogFT1DjQYTIVsuE27rZ_4i8I_zmByWnsXCbrLbfCq6jOEigBCHczytp4bhueIDAHe1B8O86fEd_Sgg1CIV92bceAecx2RWJOcAvkcFYdFX8jVSQ7km64FcuQP1CQ5LFe5KDMQ0DXQme09bP4RuEB8t26x8DKh9_ScJ9GC3ctdHCFtFJQKFOiiGKjcK3MB2TC4ohOIXS2syhgFZ0qzqkLcMEoB4QFT3nxGlEWaHRTK6tYKlWr4zgsMmhK6tDurVMkhdDODCo_aZHQ6QUi9tTyet3Fq_mSgTs2SgcnkfRiDTv27H7_pU9eGi3gEgLi4kBLsH1628KJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P31-Vm6Q1E-J5l19Pd-cZJo2NZLZCyTjzr52gCydgr1WGaUeI0Wt4FFVcBQoe-pgXmpvONXLExQ3ov5lZeaALPm06hgqEzR9ZlIW6yeYT_8Q7ZupMKWkDDbNcw7jU2JXj3ME9KJ4Z8_o7o1NRRBrwW959t33ZlSEAvO-fZCQN4u3XiQxxB1MlIru-6HNL9cxek6wQwXHNTQr5TWhPdTQNlrGpBv7bur4X0foHrfYOvYOhBkS7VGeVuvc6irg3Py18SNIX2BwkmSwitxdjh4hTUs1n8SsE9sG9BwZpY9g1wbS2Cd_9m0h2MMErMUWq60nbO4tzisG3UXVkDkLR6FYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twh3cq2OS944qsYWhF7D57HluRu00qN9uIgjFsqtxpQ1BQNd7kzKNdjcTZS3QjRCGOCcVZECwy4xtX_RuLzUnATLApHuG9hZXxSy424dHSM9cgzImVZQ6t84huQ9fr4Kq9HXXOeYHoiBB2C9m6-NEU3TxD0bIuOUx-Vvrx07G3QPcALoLDhCwck0GX2quLPMlwLSgIVXaJPgWzIwJpvHh8Hj9CTfinCcRK8xQWS9PXXNYUKcTDO--e9sbbNfrD1DJYi1M-PDaYuyBo0MjtMMt-XsMDqx0pWX-Qarjktn41j9qymqVeqOKHvcZfIoQ_u2Rc5fMFdAjinrEQ_PcGlsyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ6MXd9693YaeWQdbSDmMJz-LPIZEQl-fqWSM6LsjMND8BC3Q-T1eDjdv-SA2LDTPGLgkvKat8UX6C_AOXULEWfciEJFHWPaSHRS1gT46z8MfETgK02oNE8ynoPo7l8-9fYxrWUebOFTngDgSK_1iQnDFIcvR_RpaTwL7NclizGKNlb-YMj0MgFjt6Q5dt2aw_MACEqxazKaQGZnAy3oLzqCf5gSAT_R8o2lJYSWL02Is-nFcZaIsO6UT3K6I1xsI6k7CEgrbx4HHMZKAvylmiNdVaxm2meNFGsdZBkHssT8o6WyaHdW3AaE1BRMLSi6n39EDisOAMP3vX4uoVdWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4_zHcjTwo34OM7sKFPzzhlK3eZM8bU4uyGw6aBnlB4jGGCpcrot1NSBAO6IxxCBnsXBIfo8QuFBoZ7PDvsCwBrIG9NID6MOl6QAjVH5qqmRaZ1x_4r2plOXvp5_4IXV_BEOa5qzCMrXqnO2xJ4RP04OF5Ev1aQHSTflAt9mf5j413Zb74qwIuDr_og8pXtrSJkPOkkssI_2yCvT_8d2HDAo3KA3S9_RSP_evWiZla2CEzS2vg3Ce6nH-_bahuDRjZ_aKp1fR-J4z4mNokfZLbqFyDw6Uji9rZ2WQtMIIEFaEqvp2WVRx29m8zBY7Ov7-1V6WpjFvPAVYr0IjRAzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veue7PiDmn1BSJn3cemRu1ilfQp4dAKlwSy_Dke0eNTz3V5XKiqN6W41iYKimuMsVOxFa4TA9PHZoZ84ug18u3VzSByD2r3o0bsBxu6AdPFTWVLSZ_wRHDbD39Mc8X2zvHNsU9zPcAm8TMBSqP9Bg6CyOj9mRj0Q8dg8UpjCEm1RnIL7AaQHkSm-R1CTgYdFVw5jFv1CNslJWBgzpRydDtWe7cp8l8sMCz9A_wF1Lh_2ARYlosanXtl2cmmqMXIh2L45mUkxsdTVC6c7ybWV1vm5bmD9n_yfxMJUVHJDY8NpXRzkq6fCx0z_WLL_vXnzkirJSr67BSDthw1fWdKEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG75Q_Z_MTWeIXDp8o6i_OjgVkw4PTjeK4xCKEkA5xEQLpojfGg5P2LmoaztvbBVexx8y-uXYcOSgguXrLBshF1wxR1O-BhfTyxQKmJepaHajxelnW9luJuy3Q9o0DghRVwbW8zgpHD9632WXnOsgWNYAsQxk8QUcMdB7Gh-zppI95nnkA_SnKH6Q8FeZnSDcxdeyQhB63MWcsNKxXHQSfy9wlCVQnaHSZb-kFl7kFlaq1A4qqR-sL9dPDzGYj3WZvkxzgH430iXFsmKMWJF3sELzJyaZrEb5fcwpOIc3LhdwXSU4ifAB1Jf1gyPGHRxR97Duu2HlEmCvfT_7Jr1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k08EQz_KvhSwTcUtjHyXonw9LRnk7Ez8sWBBJksrvfmojvmFvxhLezBaVk67tyfphAtRFzq_cYM8zHVQXyZioa3sjz6pTiLnLmyA2HWOej6Yb1LeHYE9xqhsFkY5PqqJpeHlKFK9YZeUoqETseHixyEDF4jYDAUSwNiyKjvJud5fFBn95_g88ro8IF4cme4bLZGZiwuzFAIcmhovyuthfIbB9p4HbsPEoI3eU7QRsg2w0jDJI77-bx52A4xyJN_V4p5fyoDH6RQDIQ4CuHls8evEV8jcseSri7JuQhSaEHU3tFEidQRgYbhkuLdy1Gk4LQooG6X_T-cx6NhOfUN4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZmYk4PAtgHsEvZ7pZA9vZznWLcByNG33LkZMHK2_rsP47B5xC1xtYO7MJjVdB-loHuGzKYCtcojl5PZOStyhMt7W6XQN1pRMffKWjvQJkSnvbqdjCR4owCg7JANJeslNAKvAjILg8wQFPallfSKu1LEXsTC6c43fga1lfcA0aa7WeuizzmQ6dTOFc0JG2mwOMg1bKm8FOR4-dpcmCdGKnDewuQGviB_Xy6rDhM2Jm_COJ7HTWz2TMeRsyCT5EEaIwotVA18Chos6QOpLRf1HzXLPK_GY4vqdkJl_RDVJM0kcErN_6v0VKpwyGtFy5BqjFA9moskmpr0Yekyqc01Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO3FQm6VsyMAtfDB5toawYl8nn-L3RJq5_DXVUR8jNNCUIfK4JKCeKaug832EGBOUNDOR4zHBFgkLFx_rBhw4ESbRX7biZEPkzzEXRHBFQEIU2_3tWXD800lgOmJDpgjQozzO1NOoLS0Ud3__Nf6rvw_2iLcls_mnF_IHFFV1YdgvPn9wymptRaMoqaNdXkAsNuzxx2sDH1iff50rtHOYtvslk-L3CASBfjcdUm3rViLy6VkzIoRhc7v3HJdYmwkw2tr7eSBn8ezOtj7pFi71M50UxQuYxxBs9cXeTYRGdeJesf9AebSnLKFIiMYBI_IEwHayTKbyiTuiHWPiSGm5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=oPAvqlZBcj1GjAw6ldLW-XcQpegXeigXOLi-aqRrzC4hpYCSwzW4BdcjUOvysuz7UBp8_BxDqynkO-fMXnd8-Z8ap_UO_mQpeCVwqvVWePoBscu6kePFp3nHvyatO-guX0y_kxlpUsSCVZz7LQVOgl1KiYY7bgOfurG4JWRmyJ0Q7Fs8CiK_oQgOUvQMEk6X5E40ro65NWoZVBvyDuxKiM3jW5ygYwOphQr44GI7gwZzyTW39DEcezPGhObfy2VapXI5QPe2l967t1rturz6Gv8iV01cuPVbHZEp-nQAlTmSIobB4nSoT7Oou5fVhZxzUoR72292U2sidtjGzcPWwIXVyyB_Jec7tHblaszf1-4O2_MkxbzM8vR1Cl67YXkbyXUqaHO-P5241Xi4pNZ-y2Ht4r6v57or9VnHzIR6ZjNE2ZSuxKgIsmR7Ke_g_bQrHn3S5CgnhaTMgXxMlAwbRKuNZ4NNtLWnNKxCUe0icxv_aZwZN-g8NEz-DsvwhoRjOzZftoKDhUCB6w1WWQS0wmNgCjLNS-GSLyd0hkH32JC9PRenq38V7d4AlmmVosxVeDm2hP-ILlIepFj5cRdNil6iHNtZP3z-2tFXYWldT51uvmRHrpdys0HvzDufLsWPHFQZxlBwRWo_ejGqofrMTbqcO_Xm40x84b3V5GPoFqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=oPAvqlZBcj1GjAw6ldLW-XcQpegXeigXOLi-aqRrzC4hpYCSwzW4BdcjUOvysuz7UBp8_BxDqynkO-fMXnd8-Z8ap_UO_mQpeCVwqvVWePoBscu6kePFp3nHvyatO-guX0y_kxlpUsSCVZz7LQVOgl1KiYY7bgOfurG4JWRmyJ0Q7Fs8CiK_oQgOUvQMEk6X5E40ro65NWoZVBvyDuxKiM3jW5ygYwOphQr44GI7gwZzyTW39DEcezPGhObfy2VapXI5QPe2l967t1rturz6Gv8iV01cuPVbHZEp-nQAlTmSIobB4nSoT7Oou5fVhZxzUoR72292U2sidtjGzcPWwIXVyyB_Jec7tHblaszf1-4O2_MkxbzM8vR1Cl67YXkbyXUqaHO-P5241Xi4pNZ-y2Ht4r6v57or9VnHzIR6ZjNE2ZSuxKgIsmR7Ke_g_bQrHn3S5CgnhaTMgXxMlAwbRKuNZ4NNtLWnNKxCUe0icxv_aZwZN-g8NEz-DsvwhoRjOzZftoKDhUCB6w1WWQS0wmNgCjLNS-GSLyd0hkH32JC9PRenq38V7d4AlmmVosxVeDm2hP-ILlIepFj5cRdNil6iHNtZP3z-2tFXYWldT51uvmRHrpdys0HvzDufLsWPHFQZxlBwRWo_ejGqofrMTbqcO_Xm40x84b3V5GPoFqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=hdZ2YTB7cj6U_02-PxyhJSHDIwp1h9MCPhM6dr9DxPnMq7_fm7ouODYS-DBjrWOgbUyhXERIM-MpVmZSaFZtpIyYPOcwGxgM3n_3KcCkkArQsjjaxqe_oWvCrGV9sUisP_CaXe4lR4RphNJBXq21NQWe_i_VbhpjddrTviwb4JgQ_03ITZzpIqOYAvFYp3N16tsEp-WsHfHbW6MYAFNO8WcuGMDJg0ncEz4ns7GWf7Q6JvvNwWq1GTF9CZs42rFnAr2Vjhbh-04JBF49_rojhRyPg2sMWuWHoiYdzynov5chBB1g17LoypwEpKsb4xfnOBWsUOXkROGW6kKqrwDgOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=hdZ2YTB7cj6U_02-PxyhJSHDIwp1h9MCPhM6dr9DxPnMq7_fm7ouODYS-DBjrWOgbUyhXERIM-MpVmZSaFZtpIyYPOcwGxgM3n_3KcCkkArQsjjaxqe_oWvCrGV9sUisP_CaXe4lR4RphNJBXq21NQWe_i_VbhpjddrTviwb4JgQ_03ITZzpIqOYAvFYp3N16tsEp-WsHfHbW6MYAFNO8WcuGMDJg0ncEz4ns7GWf7Q6JvvNwWq1GTF9CZs42rFnAr2Vjhbh-04JBF49_rojhRyPg2sMWuWHoiYdzynov5chBB1g17LoypwEpKsb4xfnOBWsUOXkROGW6kKqrwDgOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oms7uSBLXQE8sBmiU0BSIx37SmvcFOXpO5dclW1srjkOAaxk1RQLsSX6nQhS1UheacWnUZ-y1V8qpbMeEnt0VcR9sAQdUOcertGIwoo5zfMwXNUGcOdxTCpLiodlX9aQmufplOCy1d0RaA-Fw5TQ--iM4Z4tVzKf9MdBa5YuBb23jLojOAt0Jc2nqXgK-b0xBCCXBnR4CtaoeZvGndxjFYULMoa8RcbRxMZtTdTb6j5U59350G9GO680yNj2-zcW7QhYVcdunQvV2yPfmqu64rlpNfqi4yz--7EFH87xCWyb2KYX1FWkXecvGRJaXFz0vk5MhgTWraTw7arku4a-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3KWWUVOuHDMDbTGjXvtUjiHuEZL-L97YD0H2x6RWZSfArCc9Ww-hTHTWQM7JvSQfUCAX7zwvTHHZNe7ghnWmTjTbZ-INI_zteqov2n_W88hwdPI5YYaulgQ-Hgi_ucfN67C-MVagOHEb78nezDt0KRU0SoMOHnca1VFEdWSepaz7M2oswI6msI0O9xE2M-JwUj3zBhC9yu50aXaBVDzso5PLP1mjF0tTPBMoA0jF4GmpJGt6QIRWcZvTel9P6reuoPtWhmobiqop6iKK9tBRLyI-VP5NISJSPzQKLXTtZefzNRtn6772vJlyZNbrG3SomP2mpqAAb8duUcwqXNaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtlRKR0ESmqR9g1JYKVPmz9kDZmRFNOhXzhF-F57cFc9-y_FwBZoXafNhHivZ7fAgaNeYQg3_YSWlvcBtTuNp-RM7cb71cBs1B6jvpy0ABBcbxQOb92NrlF0bRaIuS7dGCUs3wqY4SEN9T7HPNSmc00BRxcDOXY7OcNlEHoNDRVWp5UQNnoL6SwPdz5FPDRAh2JmxJGHOZL_UwgG_uQG8o7L5tAUfJ8j6D3uYH6PUeR99l-DSeqOoEKZvXo6cJfwEwCh2S2fpTKccNtQ3-9uSPBJWWH16r3HSsrLWY5iPq23eDTzAww3CJjnX3enA6zaVqLX42GbVxThxHs26BkWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aoj03_B71J7Dtl1lQJikqRmSS3vr7_CtVrTamILkVff0kSw9rwtLGgafb3n8Dksy4bba1PuBH5huWFCONkOlitt4nOcpoc372h2xbaZS-DgPJuYK7SHHhjqsu_O6M4hGZiL3HWm5qpS66Mmc3kIPjqJKav6XwJcge_--NKDMiGPxxBcbP0V4I8LdPVycUOl0wBBfkW7FyVO81wJ-Syi3YZ076xpvU4eJ8sA4X4vSSkZWdNpF0FlB3H943s5eqI8_qf3S_nhSJePKxvOdhM3v6C2ax3Qq-YGMKaTvI7vCzEo0jOFaAttwTREe7T_5qRvmfKeI-g2djVK4iKVdrfHs1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThzolG82Ul45Yf1yXIprhocILwnpBAiG80n56QDb9J7jZERhgi7nTlRe_lQs4b_c_10xKrnKkcYivk9_GCeHR7gU15aRhj6Bg3oBV988B4iRppIKHyZ4-pXDYRpagHHwkzhIYa8-Cg7PuCevweUPnrd4XWpnOdXhyCyaLIPhdRLXwqjjEHqRVWpkKbrvjowXu8KuunJyOGGxpgXkSZrkG5stuWaM__ScZcOJ296ilVeQAM7ZNGEZfk6d-IUSU45J7AdjLmyUAVaL2l12IXNxLrvJbaDZlkIa9vhoILsA4ViMCs5RTcOHaIq7WnPA-q275ti6_er0Nyc1kdsWS1-ZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYdK6_DTruGRmby2RsOBfPpftfcn9AHZwOFNOLXbywg1eRYF7xuKdRBgaYY-MEuVzWO-KxT-7HYR5xO0aaAbIg5-4mX6Yr9tqN8D6REePu8TTezjmaX2RHYmoMXL3b9qN1ZyXpG2STRUbkqbPu-sJBOn-GQpQHD3bcVh8yxY7X2ei-F8UMRbydVlhEeh0jtHfYzZZFO3uoz25dhdSE4rL3i-leuBbXXYWaOgHHGaDvQcMOlmCT8S91hzRuBzGjuiEg4zZZhpU-xkNeS8hKRSe2iaYTl4FAVWtUc5PHc2TPpKLKm03T3B2Rw6fLJeFEBaPiFHUy6rkKeIPu8lChdtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN9-w0Z6GzAubK29hfoChzy5Osz3tjkvsVQFJXH_Iy_uSTm2zjAdjl2iTb35RFpKA3NE0do5t0_t5EMqA060eHQpgFMpSsi8fEFfLFAMadRPineFvteaoCd6b-FGD6DUzR_VaTiXYviP_LqB5a-utyxtAj2q740DQsOO0a4kMIGRYw8ykoeJKjBRlQjYwhGGADjrKUivgsaUIOUcISvQ5JVYbsoXIqfq2Zmmk83zza0g6Lp85B1VIAfq8pMVGMokCha83MOnw1QYUKvrEv2lEfJmJB5WNZQy8W-D8ZfmdMX1zB7l00DIRWWB0_VNwXsddXb8xCB4GomcnPooVkgiYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUBJduAwDYCmjVS3_tuVwZcxg0kbRl-I6oZrBfq7wVdinyMtXxRZLn4lGEAe0zaMo9m1DHauXipGfNGteqmS5cjwxdNF2nEoSbxVbylp2TBRmFroMekIsjDE3bWIyLp_zNVjWw10aGeq8lgEBvLH-XNO-cZLTKaY5YXdw__E4W-VqXyBm4XVkyUUWIa45ubpqLLGZ5LgwgNHYrTMtBT2VVHkiLXQq2c-yCXMRVviNooJdhlNhbyIW0Rz5zBCn3ZjFeSG1xlbbVb-4aGkP5gJuaqdO4UObgbKtZyjltJFkbiFWILPYrI8byu439I3ry5JviSguCkI2Yk8mXacKjfBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlMdwpdlQR-XU48-7vw3scVvuN6GGo5Hl3TQnJppD2uevhMnIreR7ADasgUug1X3uBK7JeyD9P2ejNE4qcfhT1o-zrSu8JXd2HzgDUPjGbdOKV_NqA0_wHjQTNY8RujvPsHgbG-3XS6e9ng2kbWY20x9wG0Z7qnI4RWNfbPynAObo7L8G9cDQWvy8OgfYt2tnI8jo7Lp8ql6wrW31DYzbcqgcOpxbILZQVK-fdCS78LgLZrDPd_tUmsX2U8x9LKUdgccSl-b9jibG9UiE2WwbRR15SJUFhkieiCiH7DIcjUVQ5y5VCi-lm_in7sgiGSRxkEqkZmQUWLUtB_zQXX3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odL539sX7afPgz6mRti60vF-2lj784fEg5rOIJFtpfgrolrda5x0eRIsdJBTDFicyh6vUJt5Oq6N-Y1LNnTx1p60McfY1uLtntvqSK_SZr8McrJr8fXYBFdbsD7ts7Mx5153b-lobrPuU_67bEl4yZRljIlRarNlF_dU0iZNNE7CBUbVccFkfju3xiCdcSuUlNKXUXh-JovXDe_qaZ40Tan2A_74eqY6PaZCuC0hNZnvynh4DSsNZtKO1YgnvotXGGkIooLmxN0AHe5xuq9UoUd9o3NdvTo8ZmctkT8uUShwwfJa-arxzRaBrpq5fIy3ptULaoIhczc7_vGU8mks8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=eVtY4UYu69wJfA8j_oEH7A2jJLUj0AhFCA2zRl8DNOsdYURZBWZhFI1CyB9Eqmpb0Qux_gNpDHGjbyKuiHx_C4DY5oNeFbQQR-nsovlT42vVWWlxXZ9rDVMNHb5djfFbV7bGkqMK4Ul51YZnQwwx-sRJLVDck0T0FK7a5Bty3Sf93IuB6CnZuUrwz7MkEgGTFe6YHj6B68cinNVdJLDcaytEnqAtxMzcYu7wxpYqHss8bJNsMIx-1McJaSlSpy0B-1CK5deqYChtmfmug2ezqD9a6tFXFqDXMr1aYah7o0XTmMtpfiw8yaC8Gy2aFqRoltytDXGdttEdkdTy3Muj4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=eVtY4UYu69wJfA8j_oEH7A2jJLUj0AhFCA2zRl8DNOsdYURZBWZhFI1CyB9Eqmpb0Qux_gNpDHGjbyKuiHx_C4DY5oNeFbQQR-nsovlT42vVWWlxXZ9rDVMNHb5djfFbV7bGkqMK4Ul51YZnQwwx-sRJLVDck0T0FK7a5Bty3Sf93IuB6CnZuUrwz7MkEgGTFe6YHj6B68cinNVdJLDcaytEnqAtxMzcYu7wxpYqHss8bJNsMIx-1McJaSlSpy0B-1CK5deqYChtmfmug2ezqD9a6tFXFqDXMr1aYah7o0XTmMtpfiw8yaC8Gy2aFqRoltytDXGdttEdkdTy3Muj4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iE2sjYuYfXgPyqE7CjKi0tUX3u0n0gHc-0Dz18a-j0gkvn0vzSfMrMzivgmA25Xp78rZYEdpWmnsRnRqBPqRjCLQqslb5xkkFeH79hZDThUGKw22iN8AqXBj8d28aXuSi-my3WplXDH3RCyFF42s31PUpKfzwT4Y7bYUBF8mWKZain-tXwJXwh6Z1IhIuy2wLcSt-nd8aVqZDHlQ5MHKWB6XX06KeM7trFD3_hh-uM5zifSKDzEHp74xnoiicp_UwucBiSKkZJExxhms8jqjh41gyM0_7cQaP-xBIPt2JhF4OC9gc41zlmISXt3319QjRdGuZZ8v7cv0uRqkkjSE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VX5m1RQaYZNZPfdHgF9L0itZ5LCAZMgp8ADxD7KiMhrv_p1Lq53ZwXZU0-VZlUUSIVplUWASEDLA_cl6nozDTC71nB4RTxKrZPcqohUKWlBSRr-aVMvfvcdSh5E3I8twynlu9x0hAT_-eTEk2qTP8ncMmqnWn3j20RdUKlzkHL2VC3nYQZXzZdoz_7QySxGscv3pOp2DUbFIH-w5PfqJMLSzdr6RNpY4bcCVyetnsuil0VwzHlIMB6wtXvBes-dg3ScJuE3Po6h9KZ0gDLpjmElSPN5MB-_0IoYG5828IcSS_LR8OHHVJyEyTVfAj0WNH4yI8Ui7GQNG6aIg5PInQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OomUKieeqr34KMW-I2pW_KsdVeNazlcC4OMoqoAm-CVFunWemW-e5R1NaFOc4Nzmv8AcNBhGAEgvv3dF4vn3vHamjJAiR06_IePxF7rPZQm0u9HvWs4C5EhGh2NLW5tDvjzdzDb4qYWRIaUzHZnFXpjBYZO7TyA9c01vT5mGZth2w8m6m1o_k2NnQ5FSwutUrlBXyApgwx8X_Tg1zDfWRy-cBqMjug49fYu3lL6bhEpkYe5OkOuN0vqkv8yHI4usiB83oYuTal4cHCLVf-FCQp1c1kA727wdKs4_8XvkdxsBmEZVd1lY1y1nGq-WSlyze_o0pmmuslYkg7j97Ovaig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWQMn9KIhr0pgrAvg2NKcNMmKK-CV6bA2xp6RT_xh1d6PvXJMUopd1brN2TB4rpsjC7ggraT6K-EvhtRWpJcg4_nBHIgNkP6YT3snr4aMbBXAIkueoNC1yur3DLoUP6vXVnIstzAa6NuxdNBSYEN5MRC8ClLoHbXUi5YihovWhd6936P0LQiDUVvFFb-_HVMXZdorskgZSnVGOSu0DXJfvXHNPdu7lTah6Hlwz1nDW6q3D4d2p1-RMPxQhKOrhgoahNnXwGcq5m0hYcRbeLceuEYFe4D29sQOt-AGvov4YQgPBkVZPYJEf_y5x3JNi-S2fLXCjn4mFK3gqj8IB_y4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk-2mO5K9ruy9Pj_4JJ64DSr-vqtT4gOyTfh8rL5-QqNFsPSCeXYabznUWhJJvVJROBi764K4Wn89_vtfwspTUQfp049toKotS5JCSX56-DswG0cWNV-c1BPHptU9xDKK7qDxtabxpUxRK0glHFDmSBvYTl-CIQwDrZ6Nh5wPEKWIA5qcqDJRGPcauFDabTxgPaEqKou4T716sYXiy8w7tYIIKzZ8wLX0BOPTdyE6gp0tyZMfWgTCbaGOR7sQjczn3yFjWRlcadaF15aPOQrsUcpZryV4k6D3pCjCxZkBYUdG96XNBvjZihmpeu5-h349bD5mFbjFq3ypaR7eZ9aLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulC2uV_LUg5DgkkEgBNu2igVgq_8Wur5ZADhet8mmrafbPCDoRt0wEhGO7sONQ-96-C_j-o_e_PrPMsnM-wpSNfjMfwXHmy8O75GK1kG2GWvXA9talXChSxWIUFSZCBwMx3yERxtoTQaM4ZgvBWa9J_vWiEH_U4HpTbxuff3MOBZmVlIMlrfWRbpGfeor72hlEINI-mOAN-Kjfz3nK4HU_flpdalrrKWG26LMdPiw-umEgEppnOPNRPmC-bAplXOcL2l45C8B3Ytotm2FdwSBow8qZa5qIiM1_EHJXaxpmmHBY6GSve_mJ7kalE0bAOXLP8Ms-SeMNXiKNFpdDzhKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNO5XKAr59yK_Fy-ads9Ao-rbwz111UrTjOuz1YuPMQmoM_BLWShHwwi98NDgPnlwSLM1UeAub0v1i-RezK8o7XjStMuYxmEvcqUpiBoOwhKzTxpIFYM2eUi37m_AC_5-gLUGhwHfQ2duaHlMe0n4KhMW2Q22G7ICYt-0X6UkbcGHBE4xnWybscuwYjh1CoaATWaGuVbEUebnHyCMXqjOrSVkbNCQFZs-YqZs5cS-rZ3lvHeSQutR6KC2Ga3bZ-nVX9C3zLDsjtmjVFRf1wq4L6MK_hkD8B9VILLrcIR-sxUJjv4YZtjV2_udSJ9blCNVTyC3qOtq8UUPFMSf6I_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juoEhdSY9YMHPWXqqmkA_ZPlkT9APE028UB_W97L1OgGz--9KsGy9gEFSDENRiX7FqhyH77pIwWKeYD72ts4z5LTcmsqq2peT_iXfJNWjgcFr7AP_vwkkcbwr1fUWh1qO6E83qf_S5eTSp3wCSwprcCD8FJABF7nfGzsrLE-4vDW5WEPcW5SO1a5i1mpGWnzq6aDynwcDFogEof0M7l_Y4BaZf6_mnezb1Jcka1CKzEkd3uNiFEZzwsr_BLDL8VjLQeR56UxgSlV22zFgsJlapVX-H4V__sgjlW6QhJ7VyHdi55qH5X-Tz1RcARqCIpFv-JituLxd6jdmeNCROW6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4WJEw3qHMo_QC5WC39dIcbBmYaCaRHAt-M_CxqSa0-Y4AoHqeQmyFYtouzz998jpfBAxQ7b1vPQF6BTtYuzfQOZdi-DDDenSpCfR0-DbWBjp8ljfNa70Gx7ENr8OOJpC9EPWgxjIqCa15MnNz2dtGsI_JOIQVPnh_BLYnB7oZs6S16VMxPeePORrRJLOSNvDdDMtt_vVS0tEmdfdnMKyfv5QL0ZiU3uOMPun8Nx4Z3NPPPg43xizqJ4W78SchVhYg9CL1bxLhRWjgWSTGy_dXTUNA-HdXmWtM_qThY3ozZ3AYeanHKq1GE6q9gyYzF1LZyT7HJt_od2gSuYQ4unHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-e1EAQ8xVJkoZXE0HPTIS2cTSZbAQxb9E7AiNoamcN50mhw9wBw09MUWbLZF3O7sXJ1H14s4fhpo07PNshbMSG3NNpnAFLwidtou3hH4rDBq3DwKUIJUBzK_xcADXleSXCr_SX41_YFUb_VYD9BYzx1dGTLyazQyBZa8RjC4V_Rp2kB5pkF3XEOO5mhhvcrdaZ6G2YYyPmqpK8O1TOtR04Jk0rI4aU7a55HVorpIVq7ABjiEWsvYAiHrRJKQas5ZxVqrHsbhV0Ywcf4yC9MTTYdmM7GY22Cc0dcBb2ZYBvsyvJW1MSKUZl_9hYB90x4I1xo0W_TS62RrnZ3BG2W0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmjzgFaqVIZe6MSrBvlAVJwa36XY0vSvW_8wNaLKuM3QBNDU4x7gtNbYEYKwSeeE7IF-tyd6hrWC1CROlH1Wp7HZDjOpIqnfj_Eseoo7imMO3qDpYwdet6ggOl5o-OXRifz0a_tV3ycP8anqAjPUZGjNpMgphfD3RWhN0gTIjMQUq8YWfmQl9gCTAUlmpfrps4C5IIcXkyne4MQx7sXgd4SRLUtl8PbsrSc0AWNM3Os5HeN6JggMMHlxVc384EQOQizoTSWOPcDZzmzzf5sy9p09TjW81dOgTt3pKMJryuvDdt4MbeLnlmeSWJKNGDMdsoshmszT1XKg1uR3UTqLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRNLwpfeTG43kmxzjGPQ61uAZrCRqha2ZpZx_kX5-C5r5dHeu9pXPjqnLOQoIu_AnBrQ5FtRX4WUOGXmHeFW6DVbvShstfIRMZ-LlKlK7CrEFdaxSeYJlJuJdp4Bok0RpA3Zdkx6qbKX50Uszad_ElEboVRmK1xv-Cz-Hl6yM2XsHWas8tLekXPV9IBXhqHUi3zfqKkQnhmeSJENXE1Oxb9ZSQx6R0Sm1nVgamvjy3tjHsOUMe58QiBW9k-XZ94FLB6Bduc96bPnuuNPYnwqI7Qk7D-lAuaals6R-UHAoqp0s6CCGOu_tiE7ff6OLPlrNrIxD4lj31QviWUU32CAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_ZT1nEZcF3E4LlLkHjzmMiDDreVHmWyjWa1FHgrUfkk61jmTJ4cusjN9qgC-XK-3oJybSHLWB_AphIhYIPpO9Xr5VDmecjFeA3cmasCjYw4BuU_xrqk2v-umE4HsOiAmabVXEVKf3847htISN8eXpjFa1GmIYA1vP7dG3vmlivNz6QhWWRSt-rk000jK4k05zXV_f5cUOJFjesXr3Uajg_lOjwJW66EH9kD0g8ONZI9Ec9l7NOjhwCpyvLi2z671ONWQ8Uht7ngx0TV1NrZNCALGujXdyHuva3wbPCT3OSRLS0px-nIDQ31xUiaLcBHtXMYLsTmO0ZmyxaJbuReFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2jTv2K0FUvBeBUCMCNMNNA6jjhdaYQKv-HNjBYGgZ0fAOEBfDHmq0vAXT7XyIc9PsOyL_wHVX4vot7AXY7BbMqQNSyElBNtrpSFOjRnr9MxpQQV-I6nmgOS_Diu5Vy_oMbZneszEOt0LNElytCv8NKlSNl-cn7IMjWHQstSSxKgF6lNOXh8MRjTNOjd8BXYEz3wGu2Bxytu1u1bL63gQHLUgmqVyZb3yKKO68Qxc8oD_vxUM0jWssac-Zgh2JatAWUmH-SbozUPyGx8xo6Zke7aTitczZxSaX-rzVxwMhWnexW7_0R1cH7aNw5NwVORShlnfdU-7eoBF7frCAQYkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwFfeWSwwo2AZsgZ21RvsoupjQWiS78bWtmplGEsUKDPZe8aKre1tebqNtRn9ScUUeU-0I0yJuxyBqep2Ag3nFBY983Sn9IMUmnZBq6vjPX3WtGaZ0BsLET4WIh7fzOOr7Cv7eZ9sgQFNJUCrIv9GAZYfMbbZpSrDkASx1kyfjPD802fwJjVnXd_YfbU3WzGGUjY_WFunDeY0UjLTsCmmrh3Ms-F4S5IFy_trzKswZ9kMM58UZQgg2sVarQT4DnWKn8eL8Xr3tAQCU5PjgG79Ut3LnaeZ20GKdpXhWGcHnxOGZ30I9OJZzs_FC8ulBcMg79vINrhTk_aY1L4GWiH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AngztgON1sWn8xkj4l1wWD0BwaQ_mMAeFYyBfeIWW3HUtQSG9HJoIQCSbenNvLXDoRmfuRn7wQjXzsL7MSHSk8Yz5u8Jz9VFTYmQm7XRDFOSbrAKoqslWk0pFpoozE6k7hReZLTyAvc6upsJonJhHlNte4JLIehBkJvzm-VSEN5Pj3XuwvRpz5Bm6BwpYVthQo_LR-VWIe-12Y4kPgcH4xn0P3wpNxMkAAqHwjEOdEEbI7VOTyoUriRzfdnyjHL3aD6VU_qr0gG0Eo1BdSpDHm996YguQ6qDLWj2FYjfZQ9IP614dGKf6v09vBI6oO_0AOmP1-ITmcXiiojvefMJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Al455Ivy3_cEU7eE04YqfTNcxhTZlFMOF71r6McVqwZ0kg9C5E2t0xMlHjE758AZE571ntWi8voQdsP4Bx1rTr2gGPpSLBNKkQD9hkpY73UWkKx5MB6ufouNxZj2mRKqvBSsBRbFEoh9pDQc6Vm473KMKfzRCySNxDArrP4Jxb7uxMFcjPa1Qy6R_LLDXbx5v1IW84Hh2rX62URD6KsDsBalOazczseo40h3OXyb_PeTpNDoRi1ZsQ-m7RKU2GuchBfQmLgEzL7y5PBrKSj4io5ce1hsv-D_t8ZAk2upkkaIfGD_5P6bSaSrQJ9PImxv1n3mzVts7Yhb35ClwRzOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTnGuL1avYaxkpZ2684BlEKTMEKSRo1xRCIUcfubjHaLpKcmyvlm-H-Hmk4YbI-lK-qPCy9cnrJ0TTKD9S9jVqXbNgO593mwQ9qTgsEfbkIb9RSq9AZHjgI0JFYHt75oa4BUqlecLbmXkRXtu5n5z3fe3_wKgVZJjmQC6ID-d7Q7QFcTe3lBZ5-TQrz_C_aTvWp5TXVar_xkVd1rTj5MjT7uD4QTlAMQAWUai_PzAIdFwXweVSBhNVes5uZ9BFHSDZ24oY795m5IfCr4l3Zg5iAw09u6Fnc40Fbqffeg5TBtoadT3bmkT5DnQfNOUubn3JhipeOYNErqzJS13e-OUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4kO2AcR2vdYk-vEPeBg7UP7zeYyQGpIzuBStquo63O7UuwsuF_k6qjWn4up5dL_FyUC4I6HpNVFX5QCZVF2AqeMEcm0Wse0e6le_Qi16eh0DiNq7t-j_Gfr2etJbUKPOW_28oa69CW_z7s99fmv0jWp5GVYeqoZEJEPse54cpFh3CTnQKp863KjZ6Q4chiyEi-kTIdqmNUhlglOX5ujvNeBPS6ZIULgDolMDjaJw3v0eRiH-XeYx8VSeXBeqb6e5ggXXkMaBcFeTvXhtZ2eJZryU7rp_Le5Z81Z0-NZFcL5LHKY8NPzCU0J3O3UnkSfe8y_2vQ-hVq2HRdTWdb9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMU7J6y5P_UZRbrAq6v29rZ85jNeYnapZpfru2SAJY3pnd8pSiBGrX1rpzZnxq8QSRppsrKqmqHrPpuZay-I937Lp3jevppfQ9DKlRTpCBp2rihmRtQbB9GjfKicnbI5B0VTA9SEm1no33-S-ekkBWbYdvqiPLkUYSiNd7CI8snk2O0YpC-T2hm-5qXdW-L-kGm-EmlkS6sknSPZbFf2yZELkLMVIksnZl2v7fYfVelB8fCbEpWO0prXbCWPIdzUDIB38EtQvv1qjm-zZPv06FPwIf7GqJI0IKviLUncwiB2m0pW0oj7Pi3g6ZBupPX39bEE5-0tBi_PuVSV64qmoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btJqqKi3mQXtPPiChJ83j1O0xFz10yGTXW07gCA2g2i8RgrziZs7OC4GjKsIsXTsL7XCPU3sjj-xXfFdJ14wYmI-W1iVoT8QflUbJF8W9XcuVQits9n9aZIIgewkD39I2J_h6nk5WHZmyC4thTBf42sfmepDsmXn__CPClzkAsNoScWrGoFPyXG4toi8QDNgQZz20ycuBelrN5gmFEHRIvhJywPSwyZ-MtR41jWSeXSnmt4D_dVR0AP1O9asWfWcApntoqrAmwoHaCjtsHrXOPSBLBixa5jdo_o3GquLUbHKMWmYxjuJO4BI4lvypLiUxnHd8z7gDg9iG7KUF6QRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKep6PATGPzr0q6SguY3YnV4s6I6Hd1FHDhLOv5Pg5GGNSlawKbPVrylu7FHUx-i4auIESgVW3D3McdA4p0x743UzHTf6erWKelsSk2Nd1ADdvLzidJBU1_Pqr94irLduIhxTyVLoHfzAmLR0LPwZNU5pmkEQ1FqMDFC7IyLTbI5OLpEA9_ztLe23wQmSoPC9UMeHggRvIXhC-RrxYJnid_gQyAXpAgcOGoJDLpVihVyABJ6YnOCCwb9FdB6ou947IoFES5-sUkutdz2mmQuWrBivXWbESl07xG_8gNcRi9CS2WjdrVfswGbASP9GafcyTFANE2FFmCLr5ri-poXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=tGE04SXbb708oAVJpiEHoFBOyy9OyI0SR9xOkSvNNlQBdZxM9YsPXl9St9XESv8vPwsmW4wqa0CVJsxazcC64z3M4LFEE1_CLpc-Mybjz9tFZF1eSp5dPxUpkpGf20wvAiNAZprJ_DhXic9BmkLAs2YlhcRiarj4dj7ugCHxFyt4091PWKQt_SKU5auj23h8syuodbffdI4IVGP9sKnbINnbc8xet43k6L2rH00xkMdmOuN_k1IL77eTs7NZ-d1rFvO3MhLcU_CwczSymiUWomEjl9M0mSNXHIOHJXqQMv2KM-ZuxQH1ZPWIyMnI52B7x5ZTsd1nH3M5oTPVsshenA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=tGE04SXbb708oAVJpiEHoFBOyy9OyI0SR9xOkSvNNlQBdZxM9YsPXl9St9XESv8vPwsmW4wqa0CVJsxazcC64z3M4LFEE1_CLpc-Mybjz9tFZF1eSp5dPxUpkpGf20wvAiNAZprJ_DhXic9BmkLAs2YlhcRiarj4dj7ugCHxFyt4091PWKQt_SKU5auj23h8syuodbffdI4IVGP9sKnbINnbc8xet43k6L2rH00xkMdmOuN_k1IL77eTs7NZ-d1rFvO3MhLcU_CwczSymiUWomEjl9M0mSNXHIOHJXqQMv2KM-ZuxQH1ZPWIyMnI52B7x5ZTsd1nH3M5oTPVsshenA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To-d225xaSBkqk9JwYeyVnw__1ExdSplnkIil77eX5fD5t-6jC8KDNJVQJEY6Xb9DFWxv6U-LYF9nQTUB5IyrozhXTF7FxgNZRh1YFte6_xHX6SYAB7WS4rbHnoc1ByDhLp4wS0sJPiv1bUJYri4yOWVt4V7WZOVqQmT8y3lE6UJnGgHgX8Tu5ePf5iTshLVBRray_YOTzgaj3dlgC2Vm8bZBQdGUlRoFSfQhYEzqXYCvO3dffjMe-BkfFrzlIbXjsyeO-2WYeBghNpidLSllfNtJqdoLqWInP6TmSyBv_QmAkOY_rNZwGH2b0b0x8bqpjtWHHY4UfFBxcgTeNxYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=INGoy8NiONh5FqyRWLzXGX0oUtcwua24htiX52X-iUbi6MDq6-K07BPJ-_E4ioYFxqSvnWi3rUHnxeJ3MjUsqkfPt6K_HpK4XIQvlgUmzk9hhXvNpSOmb_DnazSF9jgxnGBD0TX41F0HhRw8YJGc3bD5i7McxRazr1X4EbZiR-XXqRof5lZy76uH9EIY09LlbUB7yMBw-GJWRHyTMYI4axhXNh1ALkneyPbpOp6aQEFGloUiyEEEhHjU-YF6z5iS7x5OLa_rQa-rYFSZwCUqKuH1e4MLuVfpsnTCzx1OoFBvd2TKoB-D455pNFZhVLPtpJiMMAjL9B7jTwb1xrILfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=INGoy8NiONh5FqyRWLzXGX0oUtcwua24htiX52X-iUbi6MDq6-K07BPJ-_E4ioYFxqSvnWi3rUHnxeJ3MjUsqkfPt6K_HpK4XIQvlgUmzk9hhXvNpSOmb_DnazSF9jgxnGBD0TX41F0HhRw8YJGc3bD5i7McxRazr1X4EbZiR-XXqRof5lZy76uH9EIY09LlbUB7yMBw-GJWRHyTMYI4axhXNh1ALkneyPbpOp6aQEFGloUiyEEEhHjU-YF6z5iS7x5OLa_rQa-rYFSZwCUqKuH1e4MLuVfpsnTCzx1OoFBvd2TKoB-D455pNFZhVLPtpJiMMAjL9B7jTwb1xrILfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=OBcpe3NQDEhfdhLXblUklMs2qKogwRFbjvSfqZ1UkBevLlxPpoq7SesbPYTBOfVpqyDn4Iq9HO2VhOKssTRJQCaZDDWS1NGpG-RASmsKku-c5ZTQqQ7ph57nZMS4Q-RzO4NglXPdP3mjJrFDwvFIJuy4gHBOv6xYTA-Ind2JF3pDMsVN3e7CL9A5JUFXFRSGZU7tDH1pskDs_yP6ydOEe4cCcugL2cDuFmMNcD0X-WkAPQVFqlILk2lwy2DHJmfY3pnzR7bPicl0hqfe6iPEXvXLJVr9_iPOu6cQ5es3n0nmTYyfFIFjyp_vtlGGtpXec9cZW7i2VDd4e30RXKYTrCb2ZUurt1tOqKv7R1Uiui3kfxwQZ6i1b-sy6U0yJ5zGclijA4CiM1fZMoTfEq5Dr75zFDch8cZ5UMmFbXMaZs_j05-oWx2F2sZ8nR4ab5Uh2hr0EiNCqgddnI-wxxtH21h2qCwZJLwu7DURrWKw5dIfH9V36InVeqkpF3CAmTRSccLnxf7fA_hS43zwyeuHPnnxM_7FrK4HVya84R0pJorRm_ADMHui78KyqBEx69IRFpXHDTrpAgIHDzlcZi-fscQdeEwFFSMAVdd0a1NAFGHpdfBgLQzGx8-bxDPdjWMIHoOT7Md7-6LsvCgFfaPZaAATOJ6A1JRQcdMWZI0z0uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=OBcpe3NQDEhfdhLXblUklMs2qKogwRFbjvSfqZ1UkBevLlxPpoq7SesbPYTBOfVpqyDn4Iq9HO2VhOKssTRJQCaZDDWS1NGpG-RASmsKku-c5ZTQqQ7ph57nZMS4Q-RzO4NglXPdP3mjJrFDwvFIJuy4gHBOv6xYTA-Ind2JF3pDMsVN3e7CL9A5JUFXFRSGZU7tDH1pskDs_yP6ydOEe4cCcugL2cDuFmMNcD0X-WkAPQVFqlILk2lwy2DHJmfY3pnzR7bPicl0hqfe6iPEXvXLJVr9_iPOu6cQ5es3n0nmTYyfFIFjyp_vtlGGtpXec9cZW7i2VDd4e30RXKYTrCb2ZUurt1tOqKv7R1Uiui3kfxwQZ6i1b-sy6U0yJ5zGclijA4CiM1fZMoTfEq5Dr75zFDch8cZ5UMmFbXMaZs_j05-oWx2F2sZ8nR4ab5Uh2hr0EiNCqgddnI-wxxtH21h2qCwZJLwu7DURrWKw5dIfH9V36InVeqkpF3CAmTRSccLnxf7fA_hS43zwyeuHPnnxM_7FrK4HVya84R0pJorRm_ADMHui78KyqBEx69IRFpXHDTrpAgIHDzlcZi-fscQdeEwFFSMAVdd0a1NAFGHpdfBgLQzGx8-bxDPdjWMIHoOT7Md7-6LsvCgFfaPZaAATOJ6A1JRQcdMWZI0z0uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
