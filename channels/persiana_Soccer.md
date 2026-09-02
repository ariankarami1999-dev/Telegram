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
<img src="https://cdn4.telesco.pe/file/qfCx6nJAYKZruNdT-eLoGwGfPj3bJg64BJNDx4Gx9I0d5Iwhj9vCHY7YTZX187aQtcaRqthj8mwIgDUNDUyvYpKa9AEm8kp4OAO47J9ZJn3uaDMgxQ-Nxwyz64f_ueSRRA1EGaZYW82y2wPKI4jmA6XPfI-gB_HBeXjZnGftrglMYf9qeMLQsbbW3pIw3X4DDt4VaaA1TsOPoZ4JfCmtl4POZtWVnGN8w0kV7mqvhaxlyF5V01e6ycXV9V3iGvaCW3hO6OPMYxJExD5HsZEUOEo3ejt1hroIdNH6FJ2M5PB9fIQZ8MoRjSRtZD0jELFE9Ax9fbhpPf7q6rSFidr7mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgVVEDvj89V2-Nq9R1vDYyzSTxu4J960xlCEkqQ_a94mcog6tRAgVUzj1Cv3ZQGCFEMxCNYQ6OAUv5c_mArglqpJW3AdShQUwjOFcYCAiNd9sJF86if_9DqxHSKqJa0kxI3DSdtdM0nx7MpgKVdfw_LyRBeS4lnpyMfLjsvqI6cljg3GfcUC2iWpb2B2iZnsj92T5ZRapo1RHN_j_F8bs5sFzKZSn62WxhXS0EBTE03AQ7-YpvSCD0dUDZzcJf5TL0axAxnPYGyOlJadkOGGYTx_H94dKAqCc8_80Q_cY68RQgySJb3oUOe6-ROtOdehJy4YIRF-sFdnlyGkWOwZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNyAfhzhKKXGiv25xoS9uxjyLA3VA_LB2K5Dq4C5Ltdpo3w2LGTL-Scl9PHGHcUHEQaGPUghM2SVJ4JZV24S_fCSnDAmdCSI85VGgjJrnh1YNndjjKcOGuAKF2cEVAlQiGx4L5BvuiEuWvkEPPPg_XJflr4So8IkElvhISkKQf1GoZTdDntUSXXf0R_iUXEWQT_yx54-kdaPWxZ8w_v3gwryfBFRIqXzJAIO9sj_be9gbZi2LwV3bHEQzwlXOcpf58hCMKgKVihKwH8RHYvHWG7LvxgV3AnvKEP9YKeZC-KiyUaiTkmNj9-b3_t_peFktVfJu5G8esAPju0UcCgFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLL6ezR_TMnFYDOuA7JgwIJ4LORsIfczKnF8pPb5y7lt0n69B5oqq-VlKc3f-gyetJeFLXTprQ2bWs4ToViq0OY7jc6abjD9Xf61VHg8eqGjpf72gw4mtmr2onJRRO57ixFOaApukmi4IAg4p_yunhE-wQZVERVAZchO3vAhsYJRkERLNLkQ4vVLmR1-_Y2hIw-AUY8DQDQ-bIfwGzY9KMMco5t7frwa8rjJ38VOtpnGbiOHzlhz798AoSmnCFb8wAoXNRL9yY26kJsWme3eRtN4jVtokLyD9cLUD00Lyt8n0jBV4xx4xd-bVZZdzwKelfDredaV74njyVJUzH_ZtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN3T_XGVy8lDC07vUwGH5udcndh5fSkcMOW-ny0WuAA4qefiDTP3ybdMqcT6rzjxt0TG0_1jxAvdw3Me6Yclw-_xUKEeXRNHs2BY9gPc4xbfIMgCkT5V0SZNAkv6jT0n4HJremkKdoSS3eq1zA7t9y3GSZZZUKIiJbjVfjyklfRJdnWrKFHwO3DJISYg6XUw0UI-nI-4CfOHxRu8MWt-wlnFSW-1Hhzx7GWZIyFcUbsr3UHd16jQ-JPH7N-AdUQ0-S2QGwGMDBOuAr7w4DcZwjAvKBMv8yV_PZD2bDjJvnRJSU92YrTv2SE967sa1Klgjbjgbtb0pDsYfY5-ZHeoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNSE7KK_nWZrhj0FbanPe-fy72hnvtnAXjz-YvF0VNnANrr1neKlfdSMU-nyu1bbWK1cLKTpRUQiZxU6fJxpATttOJ4nZwT6GpLuYoYWKpnv0T-xgNZ-X_iTyb9k3hNtdDKjfUGf1rW9qaa_G48t1w8wK2LfQnjr2RfvQ5bk8PHpS62i1V_tI9k5KutwwyAQ2ruQJIsEZifHgWSf95AayWfgXQFrzG-RUZgs3VX2EAZJwGz9Y6l13eLAqk21VsdMqYKIY-iRaGLMpHQD0IaYghX30j_e-sM4D4A22ZzC3D4mXPq58jT2_jSqFqPRecxOTa5yepet-1MR2uJFpZJu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=aK5EBrCBjtmDe4hss02BffEYfosx6vTxizG-g_Q1xWtfgdEQ4HfufNvQQuLmBZuXlTNJhFvniv72fk493qK-MhJMJcIjjLjh94oyZOvxAZLN3aN3IEcJ-g9DOMKa6LVyybtc5Aec2tEK5ply411vUxM8ggTuwZiI_kRqsB8ULJ63BcinCgu7v4-J3Eprb8zvJvYruzC_NDhUnWjtudv1x9nscuwrY8l8EBok_4hq8uIeCzudtd6l-U747Q9JRacG2M70dNGBROfU7It62uIJt7EC3rk0PohvTrrPkYUYb22pw8T64WtloeojcBffIO9WGP1xcgdQv7MUMOKbc3tbIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=aK5EBrCBjtmDe4hss02BffEYfosx6vTxizG-g_Q1xWtfgdEQ4HfufNvQQuLmBZuXlTNJhFvniv72fk493qK-MhJMJcIjjLjh94oyZOvxAZLN3aN3IEcJ-g9DOMKa6LVyybtc5Aec2tEK5ply411vUxM8ggTuwZiI_kRqsB8ULJ63BcinCgu7v4-J3Eprb8zvJvYruzC_NDhUnWjtudv1x9nscuwrY8l8EBok_4hq8uIeCzudtd6l-U747Q9JRacG2M70dNGBROfU7It62uIJt7EC3rk0PohvTrrPkYUYb22pw8T64WtloeojcBffIO9WGP1xcgdQv7MUMOKbc3tbIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
به بهانه دیدار امروز استقلال
🆚
پرسپولیس یادی کنیم از این سکانس به یاد موندنی سریال نقطه چین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/28909" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4QLeTKEYj_RqCIXmohChz4-n355AhHAHuRW8jBpKILZntwunhwnZ_AECCzUdkdN67lMI7kYpvDsSbEWRbvE2CzWr9U5Js_81Lg-YY7DBl4sybhTXoS4NC2ME_xDLi7ViQIoLeiAB008pPrMmhYMvNut6RzfeLIjzTLtAwjVfzh5N5SyCjCSQ-y7baoe3-LNK0_dvDSzvloZ6gTxYlaNZ5eswkTsOYYNAiD59EHqSIVOk3lCbJwaj4t9H8iTxY8p-bJqPBVuPWOnHDtAa4__ei_V1SSWmYf0JKirxp4mvmLRGLQKMuFioXxkUZoMky5YamDA2EBJP780hzGFAn80vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/28908" target="_blank">📅 13:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28906">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDy43C1m3LtJWNK70VB_og7jmYACuM572Edp1EaHEoYducyoi4WGthQAH3TYBPTTj74IZ5Gd_QGqdqD-Ro532UHz_336s0h0hTPg3ov1iYyDQXnrMwmzTmF1tx10bEUxrS6Gu8S2s-9q2Az3fwf7aFz9W-FBBNyClEktKSMYGd5dWZ60grC03z7sCcFTDpqW-U6XC6GmmfUyAPzm643GQEiV1ZHVXv05Tj1rZGuUGdb7Smnfzr0ayhAI1awLfMwB3gdBc0rpbmxoB0f1Q7hleahNIPCUB5l3qe-Yp2f7Z0AxEhYxjMS-EiPvB7lLHf5WbCDgW5qC0Zv-2xIb7_Eh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_Iilv1hkrdJEPOm7rkiXtbl2jZuvfpWbX-0N3g1pdqX6yfE3VmYeIR7uWKsg5nHs3j5TN-DKLWM2oBCQKeMP4DrECY03TV8Qs9AFUsAq_DaaZHXsMP3sB31MNgMONoZKLq4MuTYP8yS6XwS-5LVbFKqrMJYbjdH4ge99dVO-AUsOLzuWjN6aYTI5l7vy78UtYt-4ekGJ9X52-0BxqFdRIG1HQzDyWZ-Wq25Nc6Zv86wl-JtXwqgcoINpzjh7J3vvKFjG4j1YXQQC5ZMqNIX4QhLYDd6VUsE13-BZMOl58A320FOmPbUeIfKMNEaoj08xKsUq_R62L95YYJtZXdLiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/28906" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28905">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jnr7Itq07aj0OHSMiPXU6fR2-8peLgEYdekmk2hvlNuLxAGoF5-FPmWehFuIuqtaT58AVsUY8EMd3HJBeVihm8OsQlqs5LqDIsshbmpSsSmJUXViKFDUMDqocQRpFUzNvUQGjazFkLTbVWnfKomJJK00INNnStZ3LwS9NfSmmfoLZ-wuF86te5vvKBky6f06lmIomryfC6aKfstpTSKvGmZhlwekc7mNYNrH5_ZcF8BrRPLGY90If2imkgVUuq9VojlBoYpmqCe3X5N_yN15q5xBY-tfyH9O1NFFn5LH7JECx3yVp_xGtjbgaxS9HDIBg0dUXUxFpz2NW5NCklVXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/28905" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUdcY7O0-E6h_Ip-d8Dh686uQaMu3hFJg4fPgDCZaWHrBh5AsRopbqPk0SJD-GidrLoV7LUAIX6yv3JWwwM8SECOQaIDRPsO8m370jcp0vG0I5lF7eGBvIL8u2wPbkYIHXuHjFawQ-nYf8imTI5ZsGxYPdXOrGBGM6SqOfHGHUDTanEFHIf2BLbxB6yDSScDeOMtQKCQ8KKPYSWiuUSfqnXgGgVLe2rVrZJI5it2Vf4FfRSWJH_O2pbcwUS5NIfRZy6B0D1_YvtO2VoRpKa4pz7AQl9xWZTsBjkJ3PPhlymchQ3ZF0ZSwL2_O_Mqhe2ALk6B-tK3_cWn911u59gNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
نتیجه دربی رو پیش بینی کن !
استقلال
🔵
—  پرسپولیس
🔴
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
🟨
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی در ربات بتگرام :
https://t.me/betegram_bot?start=p12_r4EF37DCE</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/28904" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28903">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVJn8rRtcrDYroXQD3niJAO4J5fjz5xKzuGMMVINLjpdVuyAZNNMbjwPN_3H15GJfWm_XEK2oXWY9YzsA05o433q3uf6XvavudjCrfLgZB0xRSjTjAosAeV-B4weei-z6AwRMFnd4zZG92ZN1k6w5KVAW82PMhbGzvlpBSWh5bLGMLj59kEZcwESzexqR6GDH3EVZnbaE8eAsyev71Xt7vElD-z-zyHFr73iL6yavgVnDLQxCdCKR_gJFFvWWdlyGUIhKwcYuvBXWUQhVo4uwhv9pdoRy0lQoLoEla5VK9XrIgBykFJO8YufcxVXxM_fssPya2pLrAzRMjtPWrdu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از ۶ روز پیش که همتی گفت ارز به اندازه کافی داریم و توبازارمیریزم. ۱۷ هزارتومن رفته روی دلار.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/28903" target="_blank">📅 13:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28902">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=nRdESWWqfE_zNBO2Kx96MbVVwxzqF6sU9HtwplqLp3DBJwSEi0biiw2oaA11cDsj07x9_M7AKoq3soMDlK1UsiCCaixzpMCdgW4_Fk1vcK1mCIy7pawT2x7nVVXi7TOBM18PTUvJfCVZDx1xHmpSKepGuFCxEEamqLzu4lK7ll5aETydheeN87CuDdvHdX04swdfXfTHuYhJf1oQK88CRH4bQAjAh0IiViVTFeLH1WYHRFCYfRtts7VkVDu-Be4ljzhE7ubG_Uybgj5BhAyQOhuxiVPF-7nIQJki3iG2E1AFTjqAyfsn2Hi7pVASFb3EDeUGEKVlZDQdPGhPCtMmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=nRdESWWqfE_zNBO2Kx96MbVVwxzqF6sU9HtwplqLp3DBJwSEi0biiw2oaA11cDsj07x9_M7AKoq3soMDlK1UsiCCaixzpMCdgW4_Fk1vcK1mCIy7pawT2x7nVVXi7TOBM18PTUvJfCVZDx1xHmpSKepGuFCxEEamqLzu4lK7ll5aETydheeN87CuDdvHdX04swdfXfTHuYhJf1oQK88CRH4bQAjAh0IiViVTFeLH1WYHRFCYfRtts7VkVDu-Be4ljzhE7ubG_Uybgj5BhAyQOhuxiVPF-7nIQJki3iG2E1AFTjqAyfsn2Hi7pVASFb3EDeUGEKVlZDQdPGhPCtMmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/28902" target="_blank">📅 12:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3B51QQVgiNV8lsBdm7tchB5C4AqjuInXKU5FfpxDEIKAysS2pktXzPa3Z2y4IuyyFt4xnkTY1BFpFXxDs7xTv7leHyr1uByISASEClxfgeBfjpKUzqzkCOrCfOnxBxahLsvnPil6TcpiQ3z3gbS9IhB9BuP5b90Gff9JU4qKil3f-XeMKxXKBOSY2P5o4zZKmopxgPMWmjNRXlHJJkr9oOkhMH4wM6xLsaewiInja6nPNHcVsPYDN2i17K0IUh5TQwQWI3-XbNHk6LiCj9MWDvvt_DPQHvU9DvbD7SRxBeHLsQ2E15Rm7BbH-cLOcCCzok_TaO6jGoRgS9jVUzO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/28901" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAdtol_o105m8629JyffgL67mxfPx3TcfB45TshkWpYiOlTyz9_fQzBTuI3jPw_vt-9Xwmz1gMqRlWVUS6khj2rtMm_CJHX_WMdZQnjHSRGLPERLiRfx6Vel3xOQ2p0_8gOeRd_i2rHzXMez8j_vpTLBeyS4fl4spWgvgxTWLx7DSCbXD9GYS1TYPCcP0W7hmIRNw5f-ssB5nuCA4JHqly4_GTcpt-6BGcqvyruhMjXqWomoZcU4QwXiduZnTuLoVVQYLWWwkq4bvZbNmKFU0PXGZSE4yNSQYa2EtczdznFrCiyIMhzTJV-Qp0Zv7tc8yX00XsmmLfjaae85qGfu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌گرانقیمت‌ترین‌بازیکنان‌لیگ عراق اعلام شد که شرزود تمیروف مهاجم ازبکی‌سابق پرسپولیس با دریافت سالانه 1.2 میلیون یورو به گرانقیمت ترین بازیکن حال حاضر لیگ برتر عراق تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/28900" target="_blank">📅 11:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28898">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH_pYZaEaGXG5N-2Bv3wFtZa7qhym0BEJtiYp7luXUabby7iL35NFg45kGYtCYb3JxLVbg0j8lAyL8oke52jj8mFIciKLd0h3v6L5H3YUI-AZdyrDe9dQRg6k9faSIxhbZ9yVakTCQdz_UqD1VJ42pqFroJTRW0zYz56YQm39Z8pSyd26OJLz3Fsew0dQhnyKtEXmFAeG4hiNSa2KiWBbSGTvUe7WokFVKafkoOvq8Gp2SjLKpI5qYm5IuqvGIqhAFx8bT1WFqnb8kt3dhCU-Fw5o3ZOUxihgacqXtLGVlG7ndXftps54WNWoiTw2Bk2sy5GaXMhz2hgquuGbpDtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=cgiIAGDDJBcrL9oHMlMTo6xeW8cvJccrgU155us02iPPQv3GpnyiA-W-u7b97q8jVWCsGmexdJ9EETcQ0pHkAkF1yJFnBZlHPcuYOHuMD5M_tiI01JfNgdwaHZeQWcp5LbIeobHVhcZSF8mYoZKWwhB4UdDXZWfLQJBR4mPaWsR7ePGVc6nyfGkOU0JMLyw3KH3herJKwlBFTU9jDV7zC5jMidiZ-0D7kWZTc9xY5ZguvmoVWhRY7oeKuYEg0C63hV_tci0Qhp7Vsux64JS3omj5_HDDkjSDAZtk-vYH2H-lN3HxFV1csVZP8Z85dp-muqgtq_KpG_uKvGgzeZMNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=cgiIAGDDJBcrL9oHMlMTo6xeW8cvJccrgU155us02iPPQv3GpnyiA-W-u7b97q8jVWCsGmexdJ9EETcQ0pHkAkF1yJFnBZlHPcuYOHuMD5M_tiI01JfNgdwaHZeQWcp5LbIeobHVhcZSF8mYoZKWwhB4UdDXZWfLQJBR4mPaWsR7ePGVc6nyfGkOU0JMLyw3KH3herJKwlBFTU9jDV7zC5jMidiZ-0D7kWZTc9xY5ZguvmoVWhRY7oeKuYEg0C63hV_tci0Qhp7Vsux64JS3omj5_HDDkjSDAZtk-vYH2H-lN3HxFV1csVZP8Z85dp-muqgtq_KpG_uKvGgzeZMNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نظرت راجب آلوارز چیه؟ لامین یامال: ما دیشب ثابت کردیم که نیازی به مهاجم نوک نداریم و همین ترکیب برای دست یافتن به UCL کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/28898" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28897">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfbWYz_xnPSKpb_Bhpgf-RxsvCVHP9izEMmLSluQmoAGnbeldoPw6qJmNq1Asy-MZ3GNv3qEjkkZ493SICBg_E81RTGcgacHnRpqTPJnyWwoT7QwTsrUvwrsAiJ8gcZmm5UzxWlbdBFB5asG-gIAF6pIJABNt1OOvc-1VbsHiHc_A9hmV-u_VhFYyVBdS-cPoS_tVl_OVcHXN4-0Zf1i6kyVtPiW5m5nt9DEMU1CHtEzDTwlWmDFPO9TBeLIirWf2sNSrrFTXqiChjVe6k3GU3v5IFb5twuDbm6U6_UgqqObDbBv1XzxffAhGluwpUim5AbNckqgm13NPzT4a1Tp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه‌باشگاه استقلال این هفته با عزیز گانیف ستاره خط میانی ازبکستان قرارداد امضا کنه بازگشت داکنز نازون به جمع آبی‌‌ها منتفی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/28897" target="_blank">📅 11:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwOwmXlnhs1oy5OE4X8EwRWaV6mRp9T-J_CzgCnmU2F0Ue2JOn9z1hyAG4WXfAJ1OnzF-a_Abv86-1a9vV7uCUqB6Wsji6ySE7_uot9dejgG7HHojx5-usIdZ-INfEVFXxttnFxt1tKTh6KRM03MlhwdLiho6G3m9yREQ_xQzKUyhN7Jf9EAuKiYbJNySIAsnoJItYURyHtl-bx7VJzhbpznG7FRFGOdZ_QBX6ALVpbNv5fXqf9_Ahe6ZLqZKYQO8wmb2joBKLOZLxXag59jGinUmohgoSzIQkxdjdTha7yvQte0CCK3OVd26aqiCFbYnlpX6l1HLzwX2rHhahLP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو شماتیک ترکیب احتمالی از استقلال و پرسپولیس که به احتمال فراوان فردا کادر فنی دو تیم با ترکیب‌ها به میدان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/28896" target="_blank">📅 11:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28894">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekUvmUmoXJje6BF0QPINMXO4b81rMFisCg742fEq-wtjun8d82orsoHe6xyIh07vnB6tuPT9iwIfmR4I2-clwOsqyUM99P2v7hOMWXX_cD3cooI1WfHciWpKB-R2vUio63Ck9PQ2ov4xoMKStt8kzdkfMWSibVKn-oeYqhn-aJvKFyjM-3ZTrptzaBlu3O7BfGP9ety8xNTMioEcDp2ABJjuNLbDnHxbeSsTKncBkngAOoUsC2mvBcVD7qnZbj-ap270jZoOsND6yCeHXeTswFTpqdBZL3_ttrqHJt2VzDHb8A4R_YTN01ZwS9mr03A9ys1Y_40yER7kB59hqzASoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtsCVx9moxWWHwrDVS3IG87eYHFvyH2cdEhbkwdl8PRd1WV57q6IwI2CH__sbQei96mAvgsXHGy5ss8-rgw6UflGnXUJbmS7meY8qeDlgeMzOTweaW7gwkhp3BKOXvTgj0VKLCfXjcHTxs95d3a_9UaV4JCZlGYVP9KXhUDxo5GzNvNFHiJXHunlO-U9GiRonl254htAiLVeKnhRFVVMXR-d0OALXbqE1_YLQbmhs7G2gGTn3pUg3QyB__6XcMhQL1JxrPGaD7nJ2SIwVYwi3uZDWOvDG9g_hcRv92bJWpv-PsRW3v1VOH1KibmXrky-knaNAHThFB99AdT4gPISZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1tUWmZN6WOQSPzHvHo93WmWZ7rXdAxpkyxESwa8fc5pgrukGhRyM1USBrRLkPNdOlsXVuXzdgqRnmkbtL3thO3ZN10OSgr9z_6Z45G7sJLgV5Trf6mH82vwrsaOlo3E0nYOXp1ciHIqjxHEmCoy029p710vMLDEHb1dXFcSB_E8TZAEQXaHCSwsCy_yUrFeKn3EJs0OOZmws-xJP5dQX1EqxgOlhTsxnK2rmhlba_BWy2xf4Vuxc5RVh71PpS9EVw8CIOvmc5pM_qpGE6NrtbR8I2s-nc-f1eWUMAxnxz9ujXr5-QiC8BpmIFH0m63Yuau-bHScD6dO9oPhu_2_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28891">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=U0yvJY2oVVN_FfT38MHbtH7U_ZwdbJuHC_aQe08Z_vuFJsWGuFRTbQ06JRYdTBkfP-abFE0g8of0paZIikHyIwalnF-IQbFWKFKUaHIUfbByJ-BbTShO8Xg_NaH-vIg1pNX44S3b5Kpnbm-m8y-C6QfDRGcsj0y_uSmo4j3tFIjbfxKLxJX5EfzX9KT36g97E6LGZF_hjrKkIVTeqlAfJO4FN1BBGxsPqCaYsEkDTdRvBuOS4BdHfEDgQ5Px5Oc1qW7cxxmtyilJzQLkXfmINafrFblYED2Q5GQHOZv7qP-2Eipcvm_P445pnYpYM4rOiI3gamwmHuo__33wbzcUvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=U0yvJY2oVVN_FfT38MHbtH7U_ZwdbJuHC_aQe08Z_vuFJsWGuFRTbQ06JRYdTBkfP-abFE0g8of0paZIikHyIwalnF-IQbFWKFKUaHIUfbByJ-BbTShO8Xg_NaH-vIg1pNX44S3b5Kpnbm-m8y-C6QfDRGcsj0y_uSmo4j3tFIjbfxKLxJX5EfzX9KT36g97E6LGZF_hjrKkIVTeqlAfJO4FN1BBGxsPqCaYsEkDTdRvBuOS4BdHfEDgQ5Px5Oc1qW7cxxmtyilJzQLkXfmINafrFblYED2Q5GQHOZv7qP-2Eipcvm_P445pnYpYM4rOiI3gamwmHuo__33wbzcUvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار!
شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXJtfX4NGMm2Lb6BpkScU_SK6mkBuq7iSrUDuJj_RMgsoJwGfRq_vaz6GZlo489EbgxoauO8knzGtviXnqDG0Umof1dRukYBX8dBVBb09MNwl1wZ5A69AKMatAvfE2BHVfK9uS2qbpq7wrGfpDEPmyVpHwQeoiU42v2IimSRd5QMyBK-FClTiwEGw4hQn23bArr-Kjz6rCgBB-BwzDW3PFwgMnnBmIabGl_zCz2WsZy813l7ZY_yLj-ocCo5nZK45fz2Czr6mbIqMga45K19F0IhjLOGZnSMExfCbRzXPvBlJdhUX-UGRgE1eXwB5A7tgWWoi8CIZkyH0nJSMOrUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28889">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT0hBqdIPZu31sSYqmGHWBDPXWIVa3pgWZrxyMcWeECCL3RZr2Kzze4m2eAOGZI7bpgrjfhNVLGiW9XjaTyIP2fmmnMkpvMPfqJ9SKqVCaFQR27OcFLtR6G3ongT6VNm1fZLx8OkZs8uNcp6XZvrbpPeb7Y4tJXlVOMYUE5CD-cy15oeMeRcAR-Oi862CeN4W-EW2VrLznC5tBRSTt5-zOKzohF0DvmJw4aDdjlqxJeag-oDBBKRCCwetbZIbEIWrBweIccuKWBe5NzSPcDt-37W_XTPQMpU096nVZagzjUbaZ0oIr3ijA3uu3gR0eCihHaspIzlIO3uIpNUoWFcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
ادامه روند بسته‌ ماندن دروازه تراکتور در این فصل و برد قاطع الهلالی‌ها در شب گلزنی تازه‌واردها؛ واتکینز نیومده گلزنی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28889" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28888">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4s9xt-Rf_SPR7UxgwclfmCnRmpRbQPc41vlkBrRkmB25mV9fZfVAsrh8N28UJPpQySV7qW_URoY-BBUsWgHJzfo0-rzZQgs610ncD3Ouz42WkgqAO-SIKgcTRmRyxnuzatQ1zS-4aqIvybb-cDxdUPczTTx6NsyKFQBmcrY540jFecHOy8Xgk7cY2cng9Z9z3LyIGjURaEKpD1F4CW6pSit09DSJWq-6PxwyTF-9fxw-0Kc8NCj6jszVb1RCPN8GNkufmGuXV446ZkxiOp_T0JKwK783eJGo5DK7Z4UlxznsZpORekUmPDgMvMEFYhm5hCDFS2iGMbB73s097aoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
بعداز دست‌دادن‌فصل توسط ترابی؛ شهریار مغانلو و امیرحسین حسین‌زاده دو ستاره پرشورها در حاشیه دیدار امروز با شمس آذر نیز مصدوم شدند و میزان دقیق دوری آن‌ها از میادین مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28888" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28887">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNgqjHlehuxTGtBn2OomIrwHaTpl5SX0bUxMGj5KIROSI0zILYrC49oZ8cI_WXrAvI5w_N9gIor9bY4W_nX6VTOj_NhbfmCuZ0lBijuY6tInqB3IVgCYXkA4Ap6yX_bZkeMbqQOW2n6Qm15en0PEyG-YERu96Llxrc2QW71H3Lfjp-QSeNQWLTJKwtRVvk-CO8I7ZZESW2ppZQTHTyWngK1q-hL4EZXXbyQWTrpUNGB0vRvf6LJr5fk5IEld7mStnIq8g6zKFTsNbHO1zzAOavnK50rnND5mEJFe8aXJAmUCxz4aEX6YVCEieZ2NAhHA_LMF0_WUe6flInw_QdvtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28887" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28886">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZXfMC8xo1l03N4d7XrEcckbM8H3b2BNHwiIZi56VWP_fbSb4EFMAEGaKfPfchzSwU0gCtc2Klvxky_N3Cx3w5u_ManTQJa2G1Yk7yZWTIbP76K5QOO5BX2HDooMp3XacKC_PbV7MnH-8-1mHEDUcYk57f6xpdYqOCFstx43Q7H6oqMeQumRc6VZ5gdWWHoXOp0o2q0Cytdy5dg7aNiODh-FHrEUQO_JXjRwdoqeA23UmGd7phjRHSAQtuDizJcUvT555wb2MdnEEf5lDU1H2thDx9yQkcGiQCTicQQ9uGacRnKZheWf1lu3U8AGxopYj7U-5xZg0M7dW9jqrboEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
لامین کامارا هافبک دفاعی 22 ساله موناکو با عقدقراردادی‌بلندمدت به‌چلسی پیوست. آبی‌های لندن برای این انتقال 65 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28886" target="_blank">📅 23:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28885">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URXQBuYN3pCBLkWlR2Laxf3A8UhH4KiGOI99RHGHzPe68iAvytTFYoDocGWY2dNoeXMYyvuDIjm70z_0FdiTiU6EHHkwTLQDfSdDcnZ7O1MMzAFxHZcaIe42kCLLlJLKx-bGBRttKJffQL7TpYhxDCgOqquRvihdYAYl_ec5C-Rx03Wka4kGb8SACmeafI0cDyU1mGfPVowvVR4iUxZrBwPkC3fwpgIDA6YWDwfX-GZcX0CvnripDxP2fVe6gqbSNEZCmppWSwP0iVs4WGq7iizY1dgcxJZCmwB-e5cFDsp3oHlVbp0YHSGoxNfB9IUhiWcDIAn5-U162pCkhZErWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره "9" های بارسلونا از فصل 2004 تا کنون؛ گابریل ژسوس صاحب جدید شماره 9 آبی اناری‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28885" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28884">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVxYxsm6_geS4DLu1zXQZM36ZRGOSXmL84D2GnTqwPtZifsAZlgcWYRNkDoEy1syB8ztTx2ShIb99fgqWXuvN35vlsh6uB9kC0WQYS4sD5UcQsBfjJGlPBEgcJ__pCE1Fxheq-0hk7JwjAksYGERUlqVHn7ForzbUMT928_Q9m0hUnuim_R8WFSiQFmD2bsYwNfqEtn3MSGHWEawmbSso6SFiCJ1qT4YCoMZVe3d6XcT-HOIaAv9QatRf1qX46EtDHCaOgroXkEF3wghziV_UoDZVlQQleol-ozx92IGaimDjsHXpe5ABG4M6-EhvaUCbMxPst7gyNc_ZR848MuhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28884" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28883">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrsLqwBxF7SanJ74t71By61vO-ztdouVTWyKgDD7cxt3XZ1OHlSOmgx2Y2pLfWTOXY4XBKZuyRMx71ER6eRmT2qNbpfBTjYh6Dv5NnUcRQxp-rBPBsfy7kJGi3eoVKoT6Zl3ylCwkZhFdznuVnFRX_QLBKcrIdRMVwtDJyEeV0snacJNdNd2pW9lXdNPpxLccuMCzr6muhtw4ifr4C8JNkFybt8BylFaV4XzRFIj0G0XaKBDa-OgiAjwHFxNRBjvFjbEVM7uk3CTpLfcxPvzN_Oela9je5mpfl0P0AhQKjzb7NWpzyIQNL2fMHDg22SgToFsJiSOPXDnbl13F9zKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28883" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28882">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1C8lrGBI6TYzONg72LO-zwhTqzHcfZIPkT08VLbSVzwgkMcQlXdJO6MidlbUscq1S6wU9-V3F5c0_ZGlLRBRHgpTq5sB5PSUhVwnoz2ncVLoegU7rw6Tu5Aq6TfKxIVI45CHMm5YAImbKQKjE2fJeR_2_BBt6GKummJes-rlsAKthskdfn9mP0O5LCutWcR9aB65nmyrHogld_2UY3y5vPUL1BoKuTGht1i6HnnBR68AxP6gxEJPTE6no6T2mmhxaKUeFgnffY2FAIArIMcLjFXHltm7PyixffpzhqOV6MQJO-4_BqnbDLSZ7ck2LRPoVhXxQreiPEuezUgliVxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
به‌مناسبت‌مسابقه فردا؛
10 گلزن برتر تاریخ دربی تهران؛ علی‌علیپور تنها بازیکنی از این لیست که همچنان شانس گلزنی مجدد در این دیدار را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28882" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28881">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITAQ4y1CuT20DcSaRnlUTemfL6tXbP-I-5Okzt3C0pIQi_AoHRcbtb8zAhIhz_CH1BNZw53gAARhcsOS1t7yXFcrA2v6TCVYyi_u4G1Qgk50GGXTG-BgQspX9Gkja5-R7wQ_gJuvoS9J4aqgbUdz3oN17DWYKM7x1eBGgiocluNI-NuIk5mUiNLbZW60_mCv4_DM-LRCdos40Ztek_PEvK0GtHbrSdup-q1FoN-BhGmLN5cFkm3tRSn6vUbZVMofwCOcExsJRN2AZHIF4kjIyDJk_j7rRdxKQ2oZlmJU9QrpObeENmxTBBMKgBkvVfCA4zSswARLXjiw1Nb109niBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28880">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=ruaAbLHAZYgynKY7nBT1TU9pBdTqezd5dri3_p73wCpgU22U3H4PW7DMgHlQskc3WorqhUFWymhKsEVpwfx7A347s2WNv3j4daevtrhHWmQHQ0q1N3fM0g9KTtuPhLohCSSKpQNBjIsPpHgNMJYpImHFHhZVHXJjjBQKIANH0e-IHeS3eSeTfw30mxdtgGKcSpYsxuFHexQEzAI7lm_3oiwx_1tPPwPvay_szTfvpfJMnq6oqzEHdU3uCY_nNzZ-kgQ_YeqyJTWMQBPISwzh8oKm9NpuY7WgLD48-jES1XFSE-aTtM5HO2FQAMo6dA8RF_c56hzBmn5Pry2Hf29PGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=ruaAbLHAZYgynKY7nBT1TU9pBdTqezd5dri3_p73wCpgU22U3H4PW7DMgHlQskc3WorqhUFWymhKsEVpwfx7A347s2WNv3j4daevtrhHWmQHQ0q1N3fM0g9KTtuPhLohCSSKpQNBjIsPpHgNMJYpImHFHhZVHXJjjBQKIANH0e-IHeS3eSeTfw30mxdtgGKcSpYsxuFHexQEzAI7lm_3oiwx_1tPPwPvay_szTfvpfJMnq6oqzEHdU3uCY_nNzZ-kgQ_YeqyJTWMQBPISwzh8oKm9NpuY7WgLD48-jES1XFSE-aTtM5HO2FQAMo6dA8RF_c56hzBmn5Pry2Hf29PGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
الان رونبینیدکه بازیکنانِ ایتالیایی عرضه‌ی صعود به جام جهانی هم ندارن، یه زمانی وقتی می‌خواستی مقابلِ این‌تیم‌بازی‌کنی تنهاتاکتیک و راهت دعا کردن و کمک خواستن‌ازخدابود! به معنای‌واقعی‌رقباشون برای سلامتی ورزش میکردند. این ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWAwp4VD7vHtFBiRcRz4ma2DAvTaRNU5li7MvXS_KQfFGiHnD_ZrWEPGA5AeYEq9NOSmN1sphmBz4YxZ2yT-muoZBuKmKG-bynzjzSCVtYU8xGBJl91Uuav4zA321v10bgncTozRzjHZ7CCNGpZ3X0FmRMCt0msovtOg_-MpuDDLz3SDe-SCzmF3-oB9dVcSfGubkV4pdbCs80yAZCPv1aK5jTzoRoLVbTou41J0axPq9940jNCGMx8zPclyijg2ZU56Av6_w8stJAUkmj9tjLEo9WlDfxi6eLoCYV5jgihgKpLMKZ9ny45ORt0nVi8bS-MPFtZ44Q_QWMpNJTsYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28878">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5pvp6B4IZ8_6AYS-XksGwKPuakspRGWKe1G9-x5BzWIfoy6W3Q5JfOb3vazuQ78D0EbnleUb8ew_9WntOHB-74pvdhn4tFg-qqGl9Ulo4-ixpgXuktZOa1YkonJKz199d4UmvPHzK_V4q5fz3D-mc6vT9hksa7Wg2FuRwd3lEEfdehkyUa7AyUFgQvswyOsPeXILqONTAETUv6rwBI7ixw1Z9VCTapzXHfQxUJYX99CnKN2wq6Oih2FR4c8a77NZHX720rwGpR_yzxmZMcnWLa7Z_j2yJyNkCx9AvImRTJcYg4nEEFBM-9_w1HdR01Th71f9ttk3UTTIjZhCpB-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر
؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28877">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=DhfNFiL7DOereb2J1XR9lAxhZrqC_oJVnEkEikqgG3apg0Mn_RGrUGjjQC4J8jPwGaYYszUrC1MWhHCODOjF6TR3LSzlv4VXtD9DrJSPpDiHN9Yk8z9DqHspZ52UeNdiHNMOwWX_FhjivjcWm04qul-gD3v4KZ6NAkuQ_T1x_jhoS64UUbk-TCo6Gd_DL7m6JO4QmQaq7kkX8KnuRCdUGxkGaZusqrsOdqQ_mhHz9Q2r4mN9IMvfQGfdLaRkeWKjHtcU7t3lFcYNMLTQdYWm_gunaos8oqZt-1tbVpSnzgwgRqenTl4nyAgllp1sA0u1C2EQMtM6CyoQhpjrhrdfdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=DhfNFiL7DOereb2J1XR9lAxhZrqC_oJVnEkEikqgG3apg0Mn_RGrUGjjQC4J8jPwGaYYszUrC1MWhHCODOjF6TR3LSzlv4VXtD9DrJSPpDiHN9Yk8z9DqHspZ52UeNdiHNMOwWX_FhjivjcWm04qul-gD3v4KZ6NAkuQ_T1x_jhoS64UUbk-TCo6Gd_DL7m6JO4QmQaq7kkX8KnuRCdUGxkGaZusqrsOdqQ_mhHz9Q2r4mN9IMvfQGfdLaRkeWKjHtcU7t3lFcYNMLTQdYWm_gunaos8oqZt-1tbVpSnzgwgRqenTl4nyAgllp1sA0u1C2EQMtM6CyoQhpjrhrdfdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نشریه‌‌بیلد: هکتور فورت برای پیوستن به‌‌‌بورسیا دورتموند به توافق رسیده بود اما مخااالفت پارتنر فورت برای زندگی در آلمان باعث شد که ستاره جوان بارساییا قید حضور در دورتموند رو بزنه و با قراردادی سه ساله به تیم رئال سوسیداد بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTmIZd4g-V4JrhhyF5kFKxV8sWEVe6xsmn4CkADL2BEog-bL2kGMV_jNz2JtpI85grJzf5FhhKJXkl6BbEUJ_HFeztBTDu4cYaOwGFNFKnbAFf6ZXXlYf5aZIXaFVBHzHAyhqgwkg7tDrdxtglUexKL5OaE5r7Yyr9zkx7Zy2u257cHhbUf-BBrGJKAUCAb7oOkcxAn2eEPI_rCMvHnosw7WemhazibVeFzkFG-aYqcl5xuPbaAMJvztrBhD0p9oPSfffSn2qPcdV1hdONNthAxw37n51D2AHU94BsNzG0ile_MHi4or7o4APxTEyS3hkZeXAdqd91l8_g9K0hUbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx9GQFL3ZgG7zd2CskQdykgJjGmb-_sAIdnQFy70vqrt7CGywHAKnzKZSFaEZSS5HWDAtRHT3M3jJZNnvsdrXQBJPX2zkhcewmVXG8LC-UmvxKqTHrmLOMNVbcRgu7mVYBlJ1of4SXvDsLb9H9Kb3ksLxNl5UxxKa5ofCsaP1JGaqEaAFx4GWFf4Dgz5D5yccj2_3AQChv-ag1ki6uWZw98i1mwn8xwF8ReKfa8vfl6kYxpqJ-MPsms9MvpPVScKkLuI4xewIQnc__toDjXykPbNzE6mI3ylnS6_mogWo1kYsGsGc54m6EjaProZJgMZLb-vbJnmiLWFdF6Wq8stFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNn_YzRhpHVFvQWDojWAsXA8BGJB3Nnxof8Ew_rz9UMpuXbZZkebd4-vp7v4nO9fUN-NPJ9JGk3iwk1VDgOyeE0OealxUQLLope-5p6yd0EpwUWYHUjrIBPionr-DPfSUUSaszj_oqfLOUs-U_3R5-XVcck6CrqC-oVs5L5FNDrmm861Pbi45jIim9-Wu1xKijekLhzx1oP3tQLmv3lppcBXFXIq5xzGkEwJqwdQEbGINQd44gRR2pvQ9Nk1dfFPsVaqrb-HPkQTG9hp54ANYXHeUKcRJBlZAA2mjFTdAB0wbOmVji6GlYvQAPcSoaYQqygc9CORKeNpMIPesNPpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2f5Zckp-YjIWV77EIonjaCiw09136VfIChFgGX7GCok-I4AUIsm5Gcnz7jCZAWUUvPAoojH8136-j8drL54cNrZu7wuizFbptRwp1xkxWMntG2Wo8g39Iy6Zi_lqr0oGP_GhCaqqnu-zG7uEdMbqfrCtkcrodWJ2hsP9eZ6tS4lzq3EMbQj9VS0o5fhXZjWe0rQjX3t4Le-myUmHQaC0eCC6o_4cck1EAUU6P73cCF0tLcuS4hTpJDW7ese7JgbOJ57l8twpUAyoN16edXXKngDv-mh0BSAP9BIa51QMn5FBC7rj7czlhHp0PqauztLSSy3IFvXOcrIBszDOBUGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7uXqCH-7y_jq_vNtedCB0ueXr952Cfp6Y8-AZKrRJgkcHY1W6_SF1ZtQE_LLbSLZb-uBLytrapC9u62TfYOjdYRNEyB2d2LTM3NUFmfYBomhjizuGfkyYUdmUS4CD1RXl-xp93iHIZBy5IxVZYry38rDS0vV-Sa6BqUcOoCY6E9JBgyCRWeZxRQ4soOacVlzq3lMVCJNFFsVVkUiPRo-aJLZBTvJkrKdlGTAR3WHUJ6LaSWdoPV1tnW1Iod9E6IAodCU0PRN-pfhCGMNp9wbyohWvvjGJXn--d-Y4NV3lShkycPxfUvMWk2MVCFP6szZ-5Ws_cK0xFW1_Pe2J8SIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAd4KGm1oDzdG2Qf7rp2QF1mtyASIdy-u1y1pCdFGp-cqzjL4aaK0BWyBb9FsvvO-JL0MrHxmYTvlj3_ePThhRJwZt0VaT0UCjltqf64TJzkKLHWSX-b-FWkY8C5L5AeBjOHbvqTqI3rtI3X_MY3ryOn1x9TVKZVmjkRFFQRs9at2vl9drWc_10fMDyUh51_BHhGrqCp_XiHiG_J-VBYnx-SfgCqkQ0dxtlVVFxAk5k5AtmJUVlFZdbZWGIC3bVXgVnF1YPPSiJ6CGMgntu7wBOVuQ_hRw7oYB_jvoNhNeEsBqFx6hVR6Iay89KIxmFrSX6MGidEBCOu9d7HjFA9Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7QXSe9LMLuNd0sjHcrfzj2UbGw4iyyhzWxtaMlkbVu9qMp_lQApBWt6Hiy-ZjaNemTapreL667CfX1RxO854D-GhHDZF1qqhosprbBlLVUxkAiJqZ8uhmKSRSnGQUMp8RPtIN7u6PVg3im6aDtrLvtraXmgzukre92R6wchHC53gHJveLRilRPQHMsNixS548v_mw-TpEo3_7YCeVGErF9LGHMH9IpMj_j_D9tTKbdEzq2VA3s1jjqD-UTMOgeGPQh-goJ2HyAalLJsZnylWnqmz7iY2O4i4pTu5nwiFXxEOmnpmr1-rz4Rcnuz4jPA4SRi9NyMQBfvs4-T079gfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyo4EftLlhILiUxl5AYj6ckF8BFTbNwyoAiGbpIRdsGnmDrJ0sSPMzarxaQGTvZe2zKDAYiwEuQoiFcAaYR69P7V3XFt9J3JESiPtKh8_PTbV-OTSlirgUnpq_8Yn-z4_EIjjk4ziGdG-4z0xrUvv4ZnK0X7UBg7H5F_ECK_jgRBqsho0KPcLfr46NJ-gmMyqy_cBpVzKCe1n1L1Se7_1GMakvkLBp8_2XxjrOR4dGbKc2I1eLBHI3OXToGfiYtYDLCNt3VhgvtbC-3W9YThIw0XGLOtzPRo3jx7XkNpiz9afJH73yXwQXhrlN3Ug3Ua7kTrH7FPuVRu2MQm1q9-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWbfj7bI4Ndsg3xD2dGIM2zCNHodauIRhHa8okHnB_QKJQk9lbALQShs-2etcAqvoiNC5YkHii46lhdFjuXtpLtdGfbNZhS73F9lqHm--izRd-sHlyTfWeSINHx-RvmoeRCFmCDtBIAb989blei5Yjf4DDjdRZOyXF7LAyaIU0mY-VPMgiGyOBhBxmbUjVHGzEfIupDSPGhCtDn97Qbqx6QFCnK1Ygw8-OxmGMztgE10Og3aX5lo3YM_FRPY2dpCFLEXw6b85-VLM78ouQWH4jn7OvLeOdIRyiChGnkgXH1iyCnESTSAiYLGBYPrIlI4fFUbJpLq7uoDji9kP1f63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMTjNJZL7prIdiZqH32oiuspAr6kRthJAvlMtG2-Jxjq2-9Mf7IWxnfxapz6FagtWGC9RA0RCJOu7pKsu46y9AdnByguOKbEi332Mee6mKbMHxY66FiNC5JH2IVJBZAUGqi07okSrF4n_PCtG7l0_eyJ1m9HpBj_KP1P_84SM2JlpYQD-XDrn04PKxm6cZiycxXljSc_OcejDRGx4cEuhxco04G4-hd1JTkzhqRfsgEPPilGv1oenCQtZfGJJW7NFJDsIaZklRlMa-SZbKpNg3NLVUu4LWAa3cw2j_dd_AZhqys_lKWA5B_N5e7lhI6akVykWpFTE8AluebCI3tZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWJ1SJsoq119ruc6aptk9y9WwXR3DQ0Wu-ssh8y0_neBI18_il8TRc4fE5PKR-_WLGapZznPT_QEdZ1Vy6qLDD04LnhtlhkQ38c_-CpUf3TEIuOwxk6KROaFVKvqmWDd_TLKmu-o-gxsZXSctVhh5OzEEtubE23qNnpqLqGLNEFmzC3DGKtSGahVnUEFbMeywGodlMSJIV2YPdtVKOjfaNh6OxHoBT6T9my-r1tY8Yt8TZ8DjU65_e4653Lfpum2Y7Llxd-UgmXP4IhSyriBy3FXwt4IMoHmZjkGsrhqhHtIYsQNLphLc01qS0shjIU1wFWirjFH4AtW73TseciSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=G5CFSnD7w-vK04iBVw-eH8XKtQ7rJhSjwQXX-X-axMU6hMkbJ0aUInWDsmYTcA07i2ciP6L0j3hZG9gzVCDlAjeS506IwrBU5eGDKCD__i0opDQK0T4Jfgx5ysMAZxxbHNGYFo7N15NtGUjW_LgV_A_raVB8wKhYwJauIKafZA9LQcg0FNAAlB3impw02-MFPK8-2LhAhLrDaJ7zjin0MIoSMZnUWKxKwvBzjqp4CdaSznlwF75nPe91117yggsGfsljpSqtMBCKn1MBvC14G0yymGWs9g-dk3CEMsR6zyoYxNCZiHTG8JrZCLH1J6qrLtBH8feRtA6gt-AXOFoBmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=G5CFSnD7w-vK04iBVw-eH8XKtQ7rJhSjwQXX-X-axMU6hMkbJ0aUInWDsmYTcA07i2ciP6L0j3hZG9gzVCDlAjeS506IwrBU5eGDKCD__i0opDQK0T4Jfgx5ysMAZxxbHNGYFo7N15NtGUjW_LgV_A_raVB8wKhYwJauIKafZA9LQcg0FNAAlB3impw02-MFPK8-2LhAhLrDaJ7zjin0MIoSMZnUWKxKwvBzjqp4CdaSznlwF75nPe91117yggsGfsljpSqtMBCKn1MBvC14G0yymGWs9g-dk3CEMsR6zyoYxNCZiHTG8JrZCLH1J6qrLtBH8feRtA6gt-AXOFoBmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN5R8OrChBtg7I1zmI6oJRosCfe33P6aoyBkgD07AbgPR7hoIwp8pZxtmR_olz1uj4mCEZBFLj9w4Wv_nHWtNptZrEUuOfkieV2ztAtNX3gC6WVFpxnCUp0GNE0_eWZoTDPHCOuD7FG27dvNnGlqbWgWapNU_zxvl1Gs_3MD10yznTotCTfX6oxsrWL8Tmxp8KirrCKx8r4_l8E3hKpvZrTq6XjZc4y0K4c5S6j0kN3wSNgT1_mB-k0AQ-OFbdFfJcPRjwcBwWmV5qADfsp0QyrXMsTzg_ABNwn1EpXdXHgf4NCFpbhTTbxmVNfvdllPx71Ky1hN07qZQECPy17VyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQHNgsC773DbtFBq0PGVb1dXtpwWLmYUCLFGzqIXzuL1j-_zq6YAwcHA3-S7pP0qooryPv7PjnHDJGMh40s1nCX6P9vZmAaMOb3cyBPr3Vkw-nV0AKapn08GoB6StccLLJA8uoUQFoyAYDMTmZDT7Flhw7tc3Ctplxy9ivfvN8KcDu2-4MPhb4Sy77N0iJqeCjL31aPSJI4FUQuIZZnookqgTShnQpfTz3TVHn3Ktm6rMh1Fyp1u2oJwHkyalMXKGVVbBJsDGkzALM_u1g49ibNguorVbRRXDLU6ylUTm_Qz0M_yzc9ondTTECCMZ5OEFKj7dRW3O9-jVrRhyo00PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLgmkn0-zyt3FaCzsanWSttK2ExzjUtPzO6FOdcaWFcrAmLh6MK9G3SjyBwTnpUQY6FTJnK42dyCFd26TRLs2fQgL7ygEK7mr7ferGChnbD80SbtXTa-5VH1DkfLyExh9IxYkxT04vsddIXWVDt7uGxX3TvE89dDhGdd6WTz0ih290WRq4IWX-iVUr2u5SbgAUx2w1FK6yLpL_4hwKO0W03ZS8_WplImsB6nEhHmgwsT84utcXOvMcg1Zy6jE1ZnaTXAprmOCserJSbQdsNOzsobbq4yQghXKoUTRnmMS1vsIHouH7AT0yYiUfBBpguMK0Q23CIBF2Cw7_Xkz2xgNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvTZJPax4b4guk2uxQqD9035aEyiNOiydr6Dh1tfz0DkcXeoQ-mGwh3pXFu_Zvj-0_ZlBNv4SVrf8hfiXnRb1E44t3BmGUUkWILr_wDd5xmwZ7xVfDr2hd1Y0cdSt0No8kIXAsRxkqLqS_ajtoaQwA9Oi2t-TsJikhhbo8X4WPwQeNw9HEJ773XMY88Oq4OGC6A96d2KVvFEzxpNYp2WMHiXKPFcGs4HghKS9VySjO8OzHM5BV2r-tqyF_YV98NUre5xXCuSDLN0kATCDtM0Nvmrbo80kTVwHue_7i80u9N9tWmGpVCH6gC11E2c25cipbxj21jE_DPLalY75gShew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW5jnW7jswZsQpbQS-e8rHWqHh3Tx1qw3z0CRSYLnUxl8hgN2493pez9ktMjDVUjw-uV-mf3muMzyAmLYilwAVPGLbXGP8otIgcwqzDTV3YImpjSTg477WndmaqI2GW21-fbq3ayMfJkVmd-w-v17KmqEA7YU4FqbSJkScOdOCYJvOg_cmGcPQfBM41WLtMldwUqiTIioTDku-k08uyFDnMRCcUGn8NyObeF_4Rp3ZDTvBE-qZ-UDEKVAWwv8QFKeXAC5aIejwLrUKdKsbEIiAxR727pLgiPwE14a3MuGhRJYyqQvAcJaM9UsIowhcnRi5d4sO0VBtsKVZ30E5Ao5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT4OAxXkjhRYduqEK15hw3NPw6dQMsT0ewVOFjOsSgYcnvXmcBCqXbdP2HDrVtvuUVYaiijkz53EEn8moJHrzV7XAsm6m-7RrJukw_s8YQ3S8_faoXGWOz_xmDgIoTSy6ErAnI2eL-WzvUm-Iz-9Flp1PEzxwmySTUNm3yGUZJSHVsJXR_bMRhUs_PyuvoaPLvlpSoTW44uHbRaXhsHTxeYPCVnBl0p9SGbgqtQY7AeOd27_Vi4Wd20rltcpDfm0JhRaYWD3-_LwDfc-pFMejUfO-_n3bzmBTsWTfRLMo6Mqs3kYDd-RwP69kgas-JSiZKPkZ1JbVKTyVoMelhGHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP69QO2_FYIMH1OZNahwJwuRBv_1f5wRFSRscuCy3bhxwO6cFHwq7uNVw8Vg-3GvZW6gkBZCuyKLEf8l_ZeqVWP4sc-fUcdWTD_hLsNapVdgefUmddanVhh2nSDDFrifHBk0D9c6a946n2Q01epmneBa_pneNd9oQov9bJzoFP5rNv-2CDsv62tsK3y1ma6YYZsX-FyceAnmHdjCuwL3t2QK-BeAWwVvoQowrWZDJ11me2_RAC2pm_mm9DIpJvdALCYrMB-cs6tQiIhDsESNv_tMphrlBZ-Q8QdT2npIx9FJH7rxUgdwvddkzqgfiw5xDjvfa5b-QbNUBPK-5Ldy0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=Cd2uvhZr68jAqxbPewGXUrDAt1N-aibAcgB3U7_mgRtJR72nSqzVrEgJrf9iACMpNK8TrqkYpOsFd6MybLAjqQVARpYvgO-ghJpR4Qcp-dXMB5DdT24Dr_a02Sth26zr4dNoPmObzvkuBFyJSoxbW5PLQnWiCPk5VEodMecwiT9qntxMc3JJMkplDY9-51QKk0Oj3D_b9vNKXZABTXZggWVBmcXqK9pdIUGfHotYSJC0EbPouCc19VnmXlvd78ztl5sTLgSgmxfzI54rsdEi8fBNItv6X04d4J84ufisCyz0tLBrOwCXV93K5j7_qw4IAhnfdrrMZBWhfrJee8zKDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=Cd2uvhZr68jAqxbPewGXUrDAt1N-aibAcgB3U7_mgRtJR72nSqzVrEgJrf9iACMpNK8TrqkYpOsFd6MybLAjqQVARpYvgO-ghJpR4Qcp-dXMB5DdT24Dr_a02Sth26zr4dNoPmObzvkuBFyJSoxbW5PLQnWiCPk5VEodMecwiT9qntxMc3JJMkplDY9-51QKk0Oj3D_b9vNKXZABTXZggWVBmcXqK9pdIUGfHotYSJC0EbPouCc19VnmXlvd78ztl5sTLgSgmxfzI54rsdEi8fBNItv6X04d4J84ufisCyz0tLBrOwCXV93K5j7_qw4IAhnfdrrMZBWhfrJee8zKDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnMZ0nJ4LMsyxAJELKWDLt0UofnNPbKowPQPeZK8jViWEP4G5cJSV6ahRpcoR9G0sXSuCt3031TiMq3MMHuKJ04icJ-_IF3pb8i1tNQZkIkLKHv5VIot1Pd0VVbVdGHPxNaQc5h7Jyd7H2WDzhHl581dhvjJFbTDIvJSvJfabU8P1dCeHbzRsO4TOms4SIQx3fx4E-03XUAUSIh_9PLEf6bn8w0NTXb2hi8PZhx94gXp-Sz89gPB1-mvh7GBfkHzIXGUnTWZV7Nuf9WH_7l4HEtgMDCmS_qsS416a5BxaXGW2O_fGHLB-X6gTONAd73GAL16OI3likwN0l0T1J2Yig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔵
🔴
درفاصله کمتر از 48 ساعت تا دیدار فرداشب استقلال
🆚
پرسپولیس؛نگاهی بیندازیم به زود هنگام ترین گل های تاریخ این تقابل بزرگ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTuWbaBc-kCHp7aE3cZkivip7fBKM-0e-o8h1RvnEBp0dG-RhXHWw3N4ersAeq8tO2C1rdIHI7uoSXjL3c9Q5LWQrh9FBMDtE1_ZaQCnbLcfnE0r0Bt0hKFcPY26XGx0k-XTcez88teqPwrdBbOchaJWbAmEIoozsoAgsX7w8l8dsIWVmkj6zj2OSNrmeIrCTxy8WvMk7HbplAeh9hd4QEwLEmTBYFnBWL3jsYG2CYgPT7z6ILYF72zdFNXAYto26uolgc5n6TSj-Hn4fgOGKXQnIz9ZtkD_71plWIwmNPFuoEDXS-h8nppRBc-EJlrNeUblVVT3cxIGLYcbjhz00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0aOi-SMv-AY2oNZLmSjrtmD76rlQZS74gk66UmgJU0J-9yPvW_5N1zTHKYgfjKUjNmv28W-jRTza0pvulN0OOFttgvHURy8QeYEYamQdrV4Hc3z4ORCm2xSrBkGqf18nRcji597ojPzB8x-mAUQQZeuU12dhO9Z4pPd7gss77kYtI_ZDeZP8cYIduOM_t4w4Qh7H7IkRksYF46qX0aBusKRBrXoFFtfaGl25_SsAM648IrA2yGTAi05YBVmA9TnLbRoaX38mCtNCw4Md1YQ4wczUAqDU0fo7LWC7JTHG1Ls86-nnpXKk7EdUzX1AoO7ErhhAV7XlWDqDu8bsHOyVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKlOW0u0omfCKBgU_3kvbytjW8OTKIO1li7d-kVyNM5tRO-qA2kpugjTMfIYMDoaOnyZ_xIAQYsVPG6JQsWtryVdpWUxR1bQ4HYjz4Z3oCzvLqabjK_SQiOnCfxkD80SEB0HVKAAe_c7pKgR1ktOnGLmKzwTJ129ajgRDS2F2fKCn0Es8cqQ_CvIPy78Cv-2TizILmEydEJqXVMnQhGOILVHXHaVu-Gxb5j6fK_q4kmIlWS65CnM4qsWTqU_RMKPJJeGQ9K6n8o_NW_CBRbCGuEQH9W0il4pmeee0EJ2yzueT1RNelDCtV73873m_aMo1t9mc_cYS61Pqs4dwOdLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnpzI2BtCwd0uYDinneScpa6KgfQridaNYkOYWsFXRbHBk1k6PFAE3laoVfNwg-D8TjM7vyzvQDnt1AO9vZLLwPiiUeI5JcIDcjmvuHPL5taMhh8HmoGDE181WBj_xNcr_GHDN0VOaGVM_st2QFryHLR4nFyIimZD3A549APdJnZqONnFSlIRgbTvGOHET6EHlznpXz4N5bG5ZeLRRXDgYpjqMGFT1d6aZDrLwV3rzApM6ESQRUyLg3dwN3-rlMzVK2f1zjxrbvblFbz2cmFTjyGPr56gC0y2wmEirEdTFMrjtT2Ib9rUo5pmBwGflpPwKWckdTM_pkz8caVM2RPWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqH5jplSoPKeWajcXsp0Grydrp5sod6NoCoGzlxXYMLPwWvD1mgQ5FiHLqmuwUtcnZKWSh_lueqorSIjQr4SiIknvpydxXAkPIog570KFe7a8Rf8En-qHlDD6-A_LWMzlbDaW8-VOUNl48Ht5vpRbbManzJsVu7lqmiXFb7s_uXKgLh-xcQYIewp0v7020K6I30Shnzv34tJvj0k4IUXvJfWqFdKqCB-UBei4iqQon6zP06qNTR3JcLCX1Hskbk_NTdSFs2IjAW81QZn5e8DbgEFDEOe5uRwVb7FSNdVjN_LYvKMLzPlmNHEYtUcyxlNTlKwKMbxHOU8pOnKnfW2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djxae7thbPw6BIS_N40bh3p34O81j2Hoe4KEu3z_ARsKCj_G81XTU7kna08HrPp_fQdBPwlc0Bt774xH6ZhpFHiZbM7OXiOjR9ncW7ayDGfU7fGtwRRxS-qFOUXWdTJS8mXF958FWCQAXGpOTEEHuEcFELe6zoBu1-JLySIE9koARx_bd6c983_Bf_XEVrkukArfj-TAYYVqJSERrTyArk-EoQZcXlVgGpI_fwybPgxSl-W8GnBAiy6LBbA7XATP97Ol7Zk1VlkLBuhkz-OokSOp8i9sAWeh0cbVRBL1d-9M8gKiH2W78nWG_wWNC-dHsh0GX19a2WZbeLo5r80zEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNmY_nGCCLCtcpk9HC4jrJsptB8wseqQH3cvUZ21JgpXsS3QjilhrQhVkhitpoU2LgmzMkZf0OCOJRkzHh1aIQRreG3HtiMY0aTCv4J5R27F04scXElGm9xqk1eZj1tYpe1yWsckbxUXF5_uGwVx4_qbX49IuCpp1s30TXzaIzvKlyJWwEm7JbAV0fo-qLJphz2pD7a149eqvd2ZjZQJdHDT0waNRJaaqtQbyCJhewa-Hb0pjhSE-QmacuKRDL_e3FLBjoKelwIjf5pjGfpFd42Z_OHwq29NWFi6VJiCYgEPCIim-s0keTTH1lOFOpIk0wS25XcvMS7duJezEBGguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8i6CdVcTB2tcB2Fx5OlrhXC8Lu1mQ2uurb5A4W-KAx9sYiLUhC5IVQKgfFpLomLh8cxUI0SI2mqmIzEGoIHOegd9O-XJkRQIs6S-e8JOg9fpLa0q2xE3fYcZ4oncJLFmPbChbu-kF49bGlHspJzAMx764XrLauEvep-ISjZ7_Q5LlaMhV-iC6p5v-RTKDKOKxhjAm1KFKPssBNxzfCN7WuhCzyzf-Xgu7RyuqeUJdC3Fknt8NqhftCkFlQB14t8W5B6AAS1D6NBaQRbmb7TgFPofmli73NE-VD9NkfiKuOdpPWLD-hhG-F-BEmHODp-tyLBuSp7oPKmOiR8uNtb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKUi4Iw2eH-YPrKIvPlL7yaZRN3_gpQAbPK4yphedpv0IG687bY78yhE3Md7cdNn5_zNvSIesVgf-cqhCH4jisHYqkxb8mvuBAu1QkwIZkqKC8rk_1eiiO3bd2gHVNi1B3k3eMjxb60aLmXnA8fLu1WNZEgOhNsBcRMfcKQ9cxjWPIMWFmDmYpKHrE8x4CoXM4dER_hPwy-fk0aQ8jgSz7PRYMl3lDpfNfCOd6BB0sda4PCOzMwTdYbT5_5FianSVyUFcaSxuBXKgVpQfPilefL9NX-bwDePRSVViDB3XM1A2H_zN9SQXqXwaBxyxfiP98s9rScSzC5SsE4jltvvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28842">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=u56f6c-EitR6OOvEk6UiJX3NLvW4Msha-W7QTmG0SUXvYOe-Ol1ea6m8u1v2TOYhVF9vpisPdhFphTZ5GN2Z6-B1ebOh-bhNDcW9HkTaQmWtELyecCX6dva5UJ9NcSUG8KU7kQKFgnY2EhUwAV8BQitdcCUzaBl6WMl2dIcI3qXbv1KlI2Gf71UaqxwpUk-TmdTgtTEzY0wtm8fxPFcm_j1WfU_J9NCJQmiBj4pTn-FALRoxVD1KlcN0yeBcwRxtDPKCbvWS0iGdSel3I7sAlZkRrhyLmxTY2qO9120QdqAnAK63BUkEsWRBK-WgnuXuES3HsDWTrqAlqNYoMkoM_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=u56f6c-EitR6OOvEk6UiJX3NLvW4Msha-W7QTmG0SUXvYOe-Ol1ea6m8u1v2TOYhVF9vpisPdhFphTZ5GN2Z6-B1ebOh-bhNDcW9HkTaQmWtELyecCX6dva5UJ9NcSUG8KU7kQKFgnY2EhUwAV8BQitdcCUzaBl6WMl2dIcI3qXbv1KlI2Gf71UaqxwpUk-TmdTgtTEzY0wtm8fxPFcm_j1WfU_J9NCJQmiBj4pTn-FALRoxVD1KlcN0yeBcwRxtDPKCbvWS0iGdSel3I7sAlZkRrhyLmxTY2qO9120QdqAnAK63BUkEsWRBK-WgnuXuES3HsDWTrqAlqNYoMkoM_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های جالب کریس رونالدو فوق ستاره پرتغالی باشگاه النصر درباره سختی‌هایی که کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28842" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28841">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW_GJLQiR6gluHi7jjUscJ1todULXsduH29Ly93PtbzaVZK7uXauE5PC5RoqT5lFIYhiCw2lZr9aQqK_QMRvBc2IFX5-6_MTY634ozNz_m62YaZXgbrxf0jWQPPEkHSPFxwEFaBOeUdN118S0Q8RY4jIX0Qbzxi7bp3dBhHOvMHPQ0m-LwA7RhmfXVCpE20LzUYbAyV-26zh_jgpUw654TAmmVCO8lWhibEYwFcivT5Anvo3lM1RsyXF5nM3Aa0C83r9NDzhXKqJWSun19W97WA0SttfogeOaqG5N-oOTc3bCo_DZHhjrEqCKOdav8ObwlnMpm_5J_Ml5anjZFCFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28841" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28839">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxQQ1hP8ZuQNjlhZgsZZMrSdg_4XCiDk8_mfRCLCRZfbJQ1BkdlWG2y5hCOIzsIJO-SZLkX23avH_d5qEZ9Q8noUkvaC5_PM0o4FCgM_15OHIEscidKbjIAMBVhhsVfzio_SaiGJs8KlX5mFedFUPPs8t9Qy_ZPum4tk2zUV_5w9nLnmR_MBT7PGSiGAk8RYeydGH3zgj43su4xs_vf7P401qGpdIDMOLffoD3QySLAe8G80lMJAYHvgeaCCfeH0a3DUzEWLfVBdLNMUw8dRmv87cD6MWxA2n8eXdvPq7ALkIpv3sksyzb5JFdYhBBxWXPazaRcB-R-Y-1mYJcKIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تکلیف نهایی داکنز نازون دیگر بازیکن خارجی استقلال نیز ظرف72ساعت‌آینده مشخص خواهد شد. یا به جمع آبی‌ها برمیگرده یااونم‌توافقی فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28839" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28838">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSxuW-syMhrpnIXuhhyaeaQDaZktLLhwnC-uin7ctGVXiCoV2vrw18Q5GvbbL_-P19jJiHnokfZ6S_6MbJPR2GWPfBuqRseT5G-Ob_78FO7aZFv6js2RPhv9p03L0K7mYM50oaJhTpV2qQK1tez7cIvtx70ftgelUVaGgo38hOgZxjxQPHqrtrZShKvKwXym5tubckSzNDN1Nz6y3l79h_VKhcKIpn6SKv-7nrSyX4LniCfmnZvCvHuUMEYOXJC3stb8QxK5J8AkP2d8ZCl_be7QSLciu97FVmSaKifBFfa9gigxE46-MiiNE5Mpm8dmQNGE9M2gguvYCw91vbhwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو خرید برگ ریزون و فوق العاده الهلال ظرف 48 ساعت‌گذشته؛ گابریل مارتینلی و اولی واتکینز دو ستاره آرسنال و آستون ویلا به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28838" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28837">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2cdsebg73gGw9T2jC8rhBVRdU935A6eOO-xuET4wZOoJZuUAX54ZpeM_H5tdRP8TTpdKSOtp2BdnVfPAgNpmV9dbbPDrJP5vGsijD5LdUbdMQrBAboxotfJynf7dxXuFeJJIf36Y4izLqs4J4fY0tCGZE_5HIXiL9XSTLWXP5QU-5VFmnDHlH2xzshadmC4ZllCG3RS-CppIKc1f4WTVsAEijenBENGLcWRTC1k1rx8WeY5gSvSS_Ymheuvr13ZnG7WB3Z61t3CCSpTEGcGtRyr6x6RV-7Xqs5AwT8iee9qBpTQfyiD0xjYwoqqPiH4myvEL8wp9Zam_br0Mm4s5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فاطیمه یوسفی فوق‌ستاره 21 ساله فوتبال بانوان ایران هستن که با عقد قراردادی به ملوان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28837" target="_blank">📅 10:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28836">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1lF4KtX_cQu67t918NOhyMHQWKabL3vO8GKhLELxwtkcmggOStE4O5G2cs7Bjfp-0LQX3oZenBFWxaQIBiBfFfWY6BU75MROYwbRleUN9CKVcFbx4WDQioT_-4TH8qNSte79scl_a99RE4ikNI_Rz25jTMrcOf4-rXj4KfZwvbMT8R_cGZFUO8U-mDRImy9wZFNAz7V93SsNUHWF3lNs-qGNuvVxRO2-O7_m3VrtTNvSNK-GN7DE2J4HvMKowv2oXQkDuu71obqSqoT61mt7rFrNMfIgdNyhSxe7T4vt3PQ3jbFdamcs8MZiriosmfwT2acly1fVBVNPICnGISUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌ساعت02:30 پنجره‌نقل‌وانتقالات تابستونی تموم لیگ‌های‌اروپایی بسته خواهد شد و از این به بعد باشگاه ها میتونن تنها بازیکنان آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28836" target="_blank">📅 10:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=KO3d_0ly_GHIlttbbcG5rHcU2V7bw1RKsnolcM_UYWAgSZ5OTbFCBM3K7z364IrVUWNNU1hD-ys81Wpcj_gOiscTRjzidPc9gAioiC36IXt6SsagvmS-h2PiUYz2TipPyO-QSfLwex7aJTHKuCN-sm4TyiTKQzrzqN1FCyzZZKDffP-IxH1jszlN1wQMJq0B-h9x7vui8PEeYMMvYmMZxZXco-9QgjWpGaVS5Hc5XQYZUpu3sNzLYP59Tnfjq_WZ9MvcqUuy5uxB0a1IUp5tT8WvLc0qlNrChXCqWV5eYmm4j4YRzY9Gk8vsr6UKdWKOCe2en2iZbX-1L2wojzdnqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=KO3d_0ly_GHIlttbbcG5rHcU2V7bw1RKsnolcM_UYWAgSZ5OTbFCBM3K7z364IrVUWNNU1hD-ys81Wpcj_gOiscTRjzidPc9gAioiC36IXt6SsagvmS-h2PiUYz2TipPyO-QSfLwex7aJTHKuCN-sm4TyiTKQzrzqN1FCyzZZKDffP-IxH1jszlN1wQMJq0B-h9x7vui8PEeYMMvYmMZxZXco-9QgjWpGaVS5Hc5XQYZUpu3sNzLYP59Tnfjq_WZ9MvcqUuy5uxB0a1IUp5tT8WvLc0qlNrChXCqWV5eYmm4j4YRzY9Gk8vsr6UKdWKOCe2en2iZbX-1L2wojzdnqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELUFovX_Fms9C5nBBrgAEfsQQ334A-YG3nFYVLp77Zhesj2XKbpuaqPrEb6sBVgm059haFMV8ZYDmutHM9G-SWMwKN2eFw4KY2R1HX_F6tp0RRrplvPMWREamnTqp4jOp6haVlae_CTwb20YjT3y8u3LCxCLREr6JWj5Ce7R-iZ-5xFKRUzhBtJY7PzRZv9g6DIX_5fywgDmxf9pkxwahb4rNsMWQIDzeyzcGaheDtcLkdhoiJq1u_0RO9J-La1T8k-ma67OjNfjxKAJZs6Ips7Gj1vD7QggiD9EvHJMg8KmkUkfuCSiMZt8fsyC45-nn3UjxkGF77tljlsP6R0Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2Oi2jPfXUvf1Cp5ge3UZTBJiYCDdQFmZ03-8zEjDKdTL_zCiP_7oatzVE9Nd0RSjuhl4CiuxezQKGmW1zD8kAXc-IufUgZg4vquVXEBCpZYKUsCy5mMepV0I6vXXrJtbLL7q61x_w5iuOUmlJsbYys5IzSp6a2Y6RuE9t382iXAN2iCG_q9_lRLJ29MyKx6voxEPc217bev_AvEXnd9tk2WfS0KO-uv0CfUD34KBRhMFFS621MkHVbqpJG_z4A7zv0cL5cLqsMR4Euut19Y3i2dXgfeRbLz1vpjGo58p3WVWQ6gzVNlF2W1Lm8hU0tnj7RwgAYl7PF2_Fstcs5Ihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28831">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=obVER64lPwDDsNsrEDu9SdWs4hI6-SK7hsF7cg3o-Ba-R-3UUkjwcy1HJsGKC1xYN2e0T0_fBKOgiMCmlgY3LtW0uG8KmwmYhguVlydipqc-8CtZ0Dj_6It8L21EAEnidDtTSOF8-0NLIkoR-34Rikf4vasS0v3eTyzbv55K4KxInDdWVxqoNWoeG6Z85_pDtRZWen7b2l2qBIhJssHOHlZ0P_zWF3NG58PvnAOxehbAc9Wz0X-odmEnpUOKCNItZPuiaxXxOowvkTNLlTYcYCme9graMJwBPZiQAyz5XCr7mm4EVUuSwG13-y4hw7wdmM_1NJsBUnul7EuPCefzTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=obVER64lPwDDsNsrEDu9SdWs4hI6-SK7hsF7cg3o-Ba-R-3UUkjwcy1HJsGKC1xYN2e0T0_fBKOgiMCmlgY3LtW0uG8KmwmYhguVlydipqc-8CtZ0Dj_6It8L21EAEnidDtTSOF8-0NLIkoR-34Rikf4vasS0v3eTyzbv55K4KxInDdWVxqoNWoeG6Z85_pDtRZWen7b2l2qBIhJssHOHlZ0P_zWF3NG58PvnAOxehbAc9Wz0X-odmEnpUOKCNItZPuiaxXxOowvkTNLlTYcYCme9graMJwBPZiQAyz5XCr7mm4EVUuSwG13-y4hw7wdmM_1NJsBUnul7EuPCefzTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28831" target="_blank">📅 01:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVlLcDf6m4BVfwfWYfC9zMLBDM8y95-kERJQqHL6skcurz4zDeMGIw1t_orw85_RWAqsDHRtDylX4n-0d8T6MQ-OcLx_4bShsSD8yexT81JZBdoT0Em7iV4u9Wvy4lm7J0HSMURXEx4eScavie_m0s13oTDCOKYP_OA1kehTzZrJKhNlAsHXuzh9uYrRKDw-qohXKoYc0dI6ZcdHBzLIE-tTQKfH4wc9UJIWOgccA0vif5pnsg9QTg-DxlOHTS9skIIlptHtKHZoAIpJ4BC5hYGrEE9ysHC-r94EMEL3auX8OR87Nz1TpUr5ovZ_tHaW7SACTbszfFcJTL58bgg1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAHLjv13776LkTe4nTZvkuyY7C43gFhZrJeVJmspBJ9xM--34Dht_S9FYsGBDAhop-SxuBYeR8aZ3g5tq93UYzf846jek0_LM-iQYv4uNMBOkNgRnMDTDmqHbVrh8aoq75qBq-96s3Kf1nT4ZrJy7XAtaMKln3PfdcnoEtWhdvICcyICqKn4hYEuGvkhnLZwbcr9JIK1jKCyzXyf0iFIupzaT0o5l9_Nr3jW9agpbTpVqWgd03dy68F5IoT0x-it_9CUDIF7LQlUnpA4_dLlr5cspmypQIhNElVDDJ_iKL1Ipe2xILlaDO6twbXJjHJcCKFBRrSnXGx4DQBewdPEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=HJXoJ35ciWQmXjbWT9eMpqb2f6r5dkxNHeEzK4q2pA_iPBAiCChnZsxCezupwErjSV3aJGr7KQiIMTEVt-ZK-94S-smwUjzvDpTqABDhfVML7FGHmfTABshH9fN2oeTbhfKB_jEooOOteLEIgVyeoG-RTYBHbEiHNhGxDdqQNS3MUaAYbddolvEs5vxtwivMKeZfr8vhwdgnirJS54wabtK-P-OpcBtXC8Sz847QwTMj998jXzNJNfRmVqPITfNRGBtpTtyxWQsonbJ4Js5t1ZXvx9DcWorHywVs4nAKgm3VCdN7-tV9U-jAFESo1zclP2IHEBCE0wa7rNCvgQOysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=HJXoJ35ciWQmXjbWT9eMpqb2f6r5dkxNHeEzK4q2pA_iPBAiCChnZsxCezupwErjSV3aJGr7KQiIMTEVt-ZK-94S-smwUjzvDpTqABDhfVML7FGHmfTABshH9fN2oeTbhfKB_jEooOOteLEIgVyeoG-RTYBHbEiHNhGxDdqQNS3MUaAYbddolvEs5vxtwivMKeZfr8vhwdgnirJS54wabtK-P-OpcBtXC8Sz847QwTMj998jXzNJNfRmVqPITfNRGBtpTtyxWQsonbJ4Js5t1ZXvx9DcWorHywVs4nAKgm3VCdN7-tV9U-jAFESo1zclP2IHEBCE0wa7rNCvgQOysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه سپاهان از باشگاه‌استقلال و هواداران این تیم‌بابت‌حرکت‌زشت و زننده عارف حاجی عیدی عذر خواهی کرد؛ این باشگاه همچنیین موافقت خود را با قهرمانی باشگاه استقلال در فصل گذشته رقابت های لیگ به فدراسیون فوتبال و سازمان لیگ اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7nMD0PAzqYFr4RAmOsxa8IE35VAcYDID7UElvBGGe91-cNFjmfXkfSK7unDnhH2uBJeD8QwJWx3lvJ6poiW3bLOE_FeQEHs86MOK7dWkMcPi3ho331NRpFGXXsI9beRL-2NOEOL-rxjC0Lzuay9Rtb_f2m4ZZmO-U2tb-cL1d2IZGzWb-bZzP9d8gTDyGjVbDkAcGbnki6B_X9nsjT1nTmen1L3V4TjDOLMM2bsCIuJ_z3D75O6mrM7Ou6ZwqjAIu8R5nwtQY_zrWSHOq3MTYrajz6dvVtdifZVLYuIv8izpsUPAz44D3S5kZAbxrV6O48pU1oQL3Z7B8ee_fITgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=dl89Z5B8zYROzLIra3ZrGlSfdiM_LLXE3Wsz3sdSkMdlb8Yh91c1H8bQxkdj7joVgeClO0mjzgum7MP440VXieADuX_OVHMNufTYjiRFgJWF4s4BRd_B0cpKTbUGk2_sZrjfKusz6NgRqZ-1lxNAoyBcVfC3eim851tlyAY_uGmO05tZ-sGXdgGUH7JdG6HVuuQ3xWZz5qtLPhCL7v3-aBhIvkcSBvEDmRA0hsLV7ON5vo9rIuIqCZOYCKFesYyjfvEttckYLHkMydRD-bru0_zAU69lvUEZqgzaqpV14AIIJ6uXk-uRfGkTQTkHsv3Wny9jrCrOfKjFMqQMMUNOKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=dl89Z5B8zYROzLIra3ZrGlSfdiM_LLXE3Wsz3sdSkMdlb8Yh91c1H8bQxkdj7joVgeClO0mjzgum7MP440VXieADuX_OVHMNufTYjiRFgJWF4s4BRd_B0cpKTbUGk2_sZrjfKusz6NgRqZ-1lxNAoyBcVfC3eim851tlyAY_uGmO05tZ-sGXdgGUH7JdG6HVuuQ3xWZz5qtLPhCL7v3-aBhIvkcSBvEDmRA0hsLV7ON5vo9rIuIqCZOYCKFesYyjfvEttckYLHkMydRD-bru0_zAU69lvUEZqgzaqpV14AIIJ6uXk-uRfGkTQTkHsv3Wny9jrCrOfKjFMqQMMUNOKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwdLyOQm3I52H3ONNN1beBttpMwWAQqkH8L8xl7UAR9PaM_JVv8iJHlGGR3W99rdLGgEYctZsnuivDUVwmFWtZl3Hw02S0pcCbv6cN1KqUH7kzjKO0-G-LPisc0EBukMt6AbL0MmEtWpI4jsvr3dkjdcx0rKqwzBekujY8mGuADhawdsbShhYVxx4QGOmUTodTgysb5UX58pTvi0jIDOcjcw2sHkikwsFnQlSnkN-gM0se8HpUV66DmNEsU1annvAKkr6U0qJbrFoOxxVIa_6fyYWsX0uIezDjc_u-b368bFeBQK2_TxkNUg1wZblASWyr_IQoTYjZS5hk_I5KJdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0cJz5rLu-CKrk6DqbjnsM6DAyTbrC7iwDyxNgIfgGQHw-tqB5BumhBg8KFentcoEqukhPi3VW34dD8ZuxIhaogIzQzk5sugrcQdSRXSLQJYVXrinbGsvuIsv_ayvsjvP6ujB4rG53YSVd3S__JXqRpdGT3lYuIHx3WRxZ6_A6ycrLDPbbVdhQaHgB-qIsfmyFDuhMzEjCR0uLj-fwNn2UpPqS6RX7QtoZ8xnGgbH01It3LKJu0NTnlsum9k3PlELhhhfp5VEXPQAWkst46hbr5M4-BLAAKzvPyZMnoIRWlOO6XdiyulYbRlQkRURZ38iva6e6DSqDfRb_m8yuNYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANwz3cNNXLUm6dEjhSLv7wA8KaVPxZ1NNncUxoaaN-0_8uopIgwPArpZg4VEirjESP2AOHowo3pXireaEpzw1q_pp6u9NQZrlBHCEsZhyUEKAmR0ZX4ToCqfY2wVCCUdAtBLahQMJkhFwsqdwUO8sAQA_baaD9fIyNsqlJqrh5v3L8f-NXR8RwVTpL5ruog47f8tuX4duaGKnXtuIp3wQT0_RXMiDbfcbCGVHk6rcmE70O9IWmIdXTsopYPb94ei_S-TbJNUumyNNNUf59BERcKfS4rtHsgHl49ucCYIkNyUE2B_1ul7rE-GDz0-GFtkKP7pwrKJNLvY3iQZHmEKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=uy4WUE-FgP7uC4aaP42nmyHZ66dre-m2a0kMFHSbtpWD_P8WbC0hf0KNgQKD5F4LXpepdtRbqJl9htYWJLkw49fCeZW7iHIs8gq-E5yr5qKz5Tnc-0KgqF1d6J4uqDjs9ZQ1fi0c3BYt29jo91b76r_FKx6q-NKlj3S4-kgmky7Kl1TbIGyXpY8snsjnsXX-Omm16cbrXBIpJUOZ_-MtUIBf9C3ivKDVKgLTa40W15vTEFBCp1kpCquT7Nc1GiDklLjixdECcngPVIgxI0GxhtanpCG0H71uMXwapVHB6BCkFWfH73HqET5yBB2XY2PwnvcIlAs_q5zNCPhPNiTR8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=uy4WUE-FgP7uC4aaP42nmyHZ66dre-m2a0kMFHSbtpWD_P8WbC0hf0KNgQKD5F4LXpepdtRbqJl9htYWJLkw49fCeZW7iHIs8gq-E5yr5qKz5Tnc-0KgqF1d6J4uqDjs9ZQ1fi0c3BYt29jo91b76r_FKx6q-NKlj3S4-kgmky7Kl1TbIGyXpY8snsjnsXX-Omm16cbrXBIpJUOZ_-MtUIBf9C3ivKDVKgLTa40W15vTEFBCp1kpCquT7Nc1GiDklLjixdECcngPVIgxI0GxhtanpCG0H71uMXwapVHB6BCkFWfH73HqET5yBB2XY2PwnvcIlAs_q5zNCPhPNiTR8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpZCvLsWvrOA78aonxjJOa8PoL0Z5NVX4d3YGRlQNHU3qE8gV426gVehgsdk3gwQhIqkfqpP91kjNAHq5EfQW3d7t7Z-WTn4PgYBp9GyywGkBkMFtKSK2MhZaWlIP7rhwIXGdJLj6S_0CINjo1d4kGItE59aIA0cL-zEW5vBWNg7DEyy_Z0Tp2PuTXUukslJOkkGhcIVCoCeeWiCXc96G-QKFg-xjKO5GorR2Bn4tDF6UAIkgUWixEd5iq7P6RqNkj-aGtrA4Cdqh6o_xrhFd8FqkxUaK_TVO-4UO3jpO2n0bfgr9tXgjYXEGpRFGyL_3veWH-WwemIpAE22DKLO0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjzLfdJpfVh7Cokv3NK7-NaNn0ehxVQydedhPGYPvlO6x2T6_Eftncz5YZZ8Skyl7NL_8AyOk0BrhRfxAnDsHF1144fATJ8nXpSlpglULVm1JdWi3jgSdz24WKuYeKZPuPxWSRJRXsojwwaA4pvFoSkBSUql9yQefN5FTHpivr9ukWBLxZ4c9Gqf37tQN-j85Jf-BAV7_G63lX-epuZjMY0j3yScpCQXhECERcwpnv3xWMoeIjOpJyWwNqdtjNOGME1RQdGEfROx4dIRkx5PMpGDA6ip4HJuuab3vG3IR3RVR7rmXnyd3QlHmrK5GCoaZE_EiBB9gCbSeaSjfm9feQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPEzjPFbl-ScjCq6HhY3FlD2z3G412na9dsq8fp-BB3NCttt-JXzbaxVw-AesOa1UPcHJ9TI8Qf-jopuUfJdjBcc_kkHSkNMkpeEEqBfuHGYRqezc_ta0jsZx3BICnfF9pDe__Y3aNkNOoKG_dSYWjI2PGi1jOkB2FRwi2oY5CVCOaVy7k7S4Qvts45Uln1sb4D9tD9YD6JNQQ-MO3078UjeoF5m8TimUIcQBB0pWk46oirTic9tkkEjwYhxM-GVB-_F2TC409y2cUnByvsCr-rdDXmQ3b9M_AK7dwAm4pUQH_zqvs0B7EIP_l50VUNyAWvxUKIF4Tq-sGkmt01lsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28816">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJLKgxZPl8MASywYi0cwhVWNm2aBzHj7ctfo-elkd3tEM9jdKyLVB1uwyqypWh6GMmEdFOrO9hcx3Tu8iByMlcRljdsUPNUWHh7XjRfNi1YRbDfxQTTJTVUHhKbUph3m3ZRfdKHK6GWEYbGdWVslyA5mvWQt2dBPeU3wB0Cn5GKATCXp95hiYg8TFGpf0qReaP-UG945xc-EkraeJ0WoH1iX8tB6LlKs-uiPyvuKBGSXxUkuSq4qVRLpjqHxMdzs1QoMqUU7VkUSxwOBW1GNcmiOwxd3tPnVMSz9r4DgGG4tLV2jGv7S-KclCMmC48aP0rBAVHtVwEEmHJkIyIFKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28816" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28815">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28815" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28814">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2H2dq4HAoEa3sUHNr4ZqkoHNBgPEFChHCYMkStvCRs1-SBvm6Tp_kRpk_YLVs1e_AlJUyhhRswwTumE8C-PKHgCqjUmnDDuNcaNWCXIX-5p6nyaP8Ig6JUoV21MaoSelffz7UgWF8HuJ6l3HwboIAW7ebNmNILVa9XUoA5JdehK5UvVhfyTUx_yuHkduRKVrnk0ED5OqGA3MGXgwI2_PnFoHDJ5CPOoXL8KjM5m9jYyzBrDNmPTQk0BoyttRc83l4zvPBUQUA00oM7fKFklxr_SeQ2vx3uB1kWVAvc8JnK-8g75Eq9qnwsptfdJyly38draAMaVyRWyl8dTRvN8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌اسامی داوران هفته پنجم لیگ برتر؛ موعود بنیادی فرد رسما داور شهرآورد 107 پایتخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28814" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28813">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbWK7gkxL8WNRhvWLYbWFfhb9byeogICYc7KwjScsZ1t7Q1_cH6sdpEc0GzyhXjYLRB9ixgq1buEfZdM_f0UT49Q7ydoAXAnk-DRE3eUo8ADcRP9Ly0p2ojMUq_Ww0NPXPmcPjEoJD_rjEdBNxXPb6OzNgScHNP-Y4eNwhBGWW_yyMw1r7igYaIUoLYHXqkGDhAqwnuVDRQxMGefTGbdv6jMvD7qU4m9oCz1GKQ5dPEBJfU4GpwWN0Ftot4bv4vZwvi2xMd1fOUqGdgK8rB75TeSqe_4tUHIFWiXkP7VADEdyb_7cGEX8plNtc8PFOeOVi6oWs6E8cM_EOpdR2gANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
جای‌داوروسط و داوراتاق VAR شهرآورد پایتخت عوض شد؛ موعود بنیای‌فر بعنوان داور وسط دیدار روز چهار شنبه استقلال
🆚
پرسپولیس انتخاب شده و سازمان لیگ فردا این خبر رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28813" target="_blank">📅 20:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD-vQWlDkz9rSHaJtNaLi4wYevSDeY39I99UYz5G3Pwci6SbpHqMY4RvEi_w6hj-Z5fZkKehTlGnTynhoN9kihREoHrtD11cbXvuvfJkJQqDjB7CEDYnk4PXQVGzJKP7mtmIwG_uHGDao8J0eYSFWZ7e3R14tSsjlRkVCgu3Qr0-mcoszPktY00dPQ7SBWOywLB4txDPr_toplBDVef-pyUTUpNx2lT4pKcPYKhnwaRAYMS5olmcRXf1HLYVFCFVUYfgRwt6aM1dhm2_4KoGPNizmaN7P6-Dxk3SnbhfAEpUn549sql1VqoWwA5gQGxr67oJRjG1_fW0qA-nCALz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjfaoxHd7pUQgcRQ0YHQyrT99vbFM-qUDWybnHPZyh2OAyLkS66RqWJeh-kav5OJFVo65S5fkdDuLD2k_y0VPBlkyNPM5865ff0hFDAhxGVDAg-xyex9Unki8AKPPJjVa06hJEtRXf_57xC5D0oRK_9lOW8t_XAQgAnqUJChBeLR6dF17H9qp2v2xzyiQVxsjwgMyzZd4tUtY09dAVeXKP9km-Y1JsCQ4Q-5Bh2BfXb-ji-AgDxY76BuTlhxa5uvcDZ0OwwvFCLbgn1SQuwkn_C24QvN80KUfXvkp2p3R9xR1bEKf2Vf9seGi0x-QU8qNREeaahClUaIAJdM4Cowqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVLKP0LyZ6zCRa439tzJ2EP4NLg-zA9H2LgpTTvp8cn8EMUUh8aVjJivP0UjoUWbSU9yJg_zFOlLVjR6LcVLnk683X9na8Bre_QpAQcgMjJz5J8LC82ENXXh9fyO_efgRNzJyLzNal0lrb47iP7s_EFul_J3V9ox14cffwJnnWlCwzKcf7JEqtLdGRKtKr4BmQ9g-eI_wmn6q2a4nwhKwyQpAIjEuDXxzQ90szWQOm--zp-AmRNa4HRX3omA0TC55fyO-EMVQmH-EYhFJOonBby8xeSDqyQYi4VGImys2Y7Ud2acC6dOHaQEjsGHHuAQnJdN3nY1VgvLzyVvO66ZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuCNsu5rjQhWeIu2C69J4FoQQFJB6DhYbr86va9aYHrTHO_czbZBgmQaY_hN4IiI0xW4-DabFgW-_e9vku6rvwXm2wvbpBnHHFLULl3hIbHJduUvoZFg7EdIZVTKDC_zWQcw_uj_XlF8zLHPt9Un2dyMubYv-R84TOrL9m4HCyFL-kdRWx9Y6n1dZDWWBPMH9a0-28IGdiO5knIOaVR5ilG47ubNhDaKCjkXDR_hJ2ReouxAwoplPiWCVnWbWCaJhHKI8Zc4NKJpCpQiTwdR4GqTvJkZoQFzvycYcxg2HiTgm-oo5C9LdWKi-IHLk4eqPuT_aS3LR9rq2askIL1OBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=vvf5g8Waxk5AZ52-49emjrMqBAGvDCk5v2qxmweIPloVK8VA4FK51EJk6bTxkVNDEOaq3Si3DemIMLMgKyWR3mL54MCevRlPiSkLm0_DSMap1jOpnDrxQaKdMnrf_cULwchDEXy8MA70PoIJzVPCCgr2zkN9joWSORYztnLuMg_lKY6vHrUDgf6oK-H7vOiTVkqTbQwa-dDO9SYpH00b772qQDspD9-Fqc3uTq-bQp2xPbLo6Hb2RQTRdQmQygjoP_v3l-Bcfi4ODOF2uAeoVv7RrvMGKbK8X7nxreTQ1Y9PXvWHScCnrbFlxs3m6RgKhyq7rupjIaJjRcQgQe1NPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=vvf5g8Waxk5AZ52-49emjrMqBAGvDCk5v2qxmweIPloVK8VA4FK51EJk6bTxkVNDEOaq3Si3DemIMLMgKyWR3mL54MCevRlPiSkLm0_DSMap1jOpnDrxQaKdMnrf_cULwchDEXy8MA70PoIJzVPCCgr2zkN9joWSORYztnLuMg_lKY6vHrUDgf6oK-H7vOiTVkqTbQwa-dDO9SYpH00b772qQDspD9-Fqc3uTq-bQp2xPbLo6Hb2RQTRdQmQygjoP_v3l-Bcfi4ODOF2uAeoVv7RrvMGKbK8X7nxreTQ1Y9PXvWHScCnrbFlxs3m6RgKhyq7rupjIaJjRcQgQe1NPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ht6lnHNZpMFDboX0J-FZTsCjuTWiy9fY_vPifRbnkEXYjoIkXKqME5jugIQY0tbniIHnllGmzLJmMRCqrJIFKieZugXOzbMSE1Rq85yWlhQ7VpNrNGyC_liNtJ1Xrwx7oQPoy9WMKWhNIBcS7YNhSP-fzM3dXOz1ghO7DezsLNBVvdLKGjaM-1VGOJkM8jBEPOmvKkMgfHnGJIyUWObUuJt5wJrVXsJPIe-AOWycAUGMe-03u6rAvJ7ZMZQzORkjyXS3HiRp4XqfCQpxyB9Kq8CBxDvp0QXW7E24LqWxIUBA3DMVYNZlqGeXfEyITXyIGtj_QWYH_BQbJgL2m8Eabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FI_dG3kUp27sH0d9VXgrGUyVCzQHHBTc5CnT_YMgTGzXlAunAsdhNzrHKhz1yILhYL1roXecw7IWkAi73E5tTHvKtnFQg-T7jDHG1JiYRQo-7fxgwTpyWeF1KD77_Af529jD-iu4AGOk0JHFwUYtVls8AxsmkGuoDA6AO4G-HbfD40gffHj_unl_BuiCxwdFPENf_PMhuSzcNAuhY88FZTHFR6i7L7arRpOdKFe3oom1ba4syXGTLHdQ9mcTl0dSDQYBMAAcX8qg_a0nhbgalxmzytKdEUOsVhjTfElK3b8hB-vOwx820g430u9pb3KeS90Jh3KqL7UrdOdNJohmvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWU48SZemCyuGZgWwx0JMJbBlf-_ioK21w8RNJeRNAAQ1C9mvIt5vxJBN0UzGPJRqg9m9QCZXMCqL6muOe52qqg8UenquKxndBV1ile3e4KNgIxE7s6mTRw8L6NeomF7cNyQm3A1tw9ZGs1DEfZ-4moSLB15L6UAuaUQHGz4bbd1QtsC0Pgniim7xlI13zNUhfew3vkyN5THdXpHbKzJUOnI957Wrcs5MwzRSvgL6pWdOCIZ4OFDHmMy7Il_oyVroeHUZBJcpS2JHJD50J5n6gHKM__DX8RXBwnizVXT2PSpgLxbDxa0cGkmC35tQxCh0eCl6ROzkf4db6wMDKVntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAbfRRPtTCQ-IfJnV3h3sQ3aLeHVgUar-pjCvA13Twz0jxHj_TeULBrBWbgiOyUTeOUvPrRxEn5cdxrJWMrEEsfg-gvUudu0fHE7gCOzlN-7O4OQPOFpH5J9k5xJEIdhb2d38moI3O1Sxi06vo5Lv2JHz_oNFRpiDDwGOvoluSMMTH7ESBAm1d-ZThEUSfl0O4dENSwRySPQB-sloS_VLmzgaNEVQ8NIj1Sv3fLqkuuHgC90Ptn0MdgrGgPaszPzH_4UB-2IdalWIyz6aGw6XD-K3yNPaf0UekF1rCBJ_PuG7hf8LO9LKQ0Zxdyi-fKamargfALFcp_5IVE54xJIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsXv5SG70Vugk1yj-rxMa07AbEFjZITCEIpk0ZHp6v7wlRfKjfwob4nzmlsdELk9AHAk9U7seDvdbJzAozmyKMJRhBuUdlywShbJHMScQT9WP2aoSQlmwZhus1Q3MCsUV05SE1vPFN3tqnpv-ihUFLseK7I2_HMjL8OTZCIbHRg-4hscy1YfTc5EkXNHqAKyMsco7j9y8WvEnIoKpr-ki7G0XcErQLuD2PnFXlmMqmJMRuLXsdqZ1r8YFxneFWqJ8NtKr8Af1gcP6Q8a_Y_xw3sViX59AnTWzWViu6uqYEQY3gZDil8_ScitJ1ZdwKvpMQV-EunbPrYVJQ9wQI8QeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsJ75SyCY4IjcB5hkTLdTs3BEUboSI_5L2Lrz42xfnKeu46gT4QUezkkN-aEweq3NqAq05mFgZ1KxdeMFHpViGjHVQw3PvbKkAO-JAMs_0GAjJ14As07jUTHeih6gtRWd_cfk1_CMBJtG113z8vA6WGYtAXAGTxu5AOIYK2rn4KQvT5JATC97vfjll8cQIJW01IbSdh6ITvHvF6iCIYHIU49xAGfs9l85OLse1D-9CGdLy0cLsFKZdZB5HVAGWfdjT37lrNJQTLL9UM3RvLTOBBEOYuIL2gx3qLKSJ0c3EDbxqJFIo6x7huh-aJOgrlaURvDfoL5IS3MbL5hBo2VJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRnNHnMm2gQx9txIlVhHBBEh9LC3b6bWvhMYTgTcI0leY7cIjkuMSFa7xeyfX3SAwC8hlIDMmzSKPFsj28CCbHC8tSb8aavQz-rkgx845G7V4XDypyJ_PfrJKL9sPGzOcMKTJAnveF0tXJBp5Ugmib_ZDPH4MQmbRxy5Lw7yTFclwGCxY20O7Vg9mAWstw_mJ6gaeTy8gJN0phE2B0K0GH7qqFKoCya9-WhPXGKniho2vwTwP95U4_35ITichOmfgE_s1f82RttD6JolOM2vyYtrfNMga7qecKrpwYxlQcuPH5T5WZ4unB5rY46v0M84QWH96koEQZPwOb2mgRB6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28799">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=pRZk4oq83eopYNUaQroZZgpQu4a5TuGuB-0ocX0bkUq-ZlgGtxxW9eKPIfiADtKIHwOZHlfe36fHvqxSGTwWMJRrMan0Dlk9SsztGP5rAbH8mPkBT_5BnDAzq4Sa3m6mEFSAILHB0NWgiWXnAZ9U0tOf675BDkU8p9fdXjL-yFabZVZX32UzjZ775EjzE3SRM82A7-LA1gqKSUgjQyVeqoQuuzpannYBIEcpMacm7Fd6kwanIsDOn0aDYSUwyNZoa1ImS4xz-H56cV_MvNa0WDcpp11_mX79xzdX9VFeI6cmwnnGHzBZwgA9bkux8ScdMxBC2WhOFGj4ONZSAqJQHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=pRZk4oq83eopYNUaQroZZgpQu4a5TuGuB-0ocX0bkUq-ZlgGtxxW9eKPIfiADtKIHwOZHlfe36fHvqxSGTwWMJRrMan0Dlk9SsztGP5rAbH8mPkBT_5BnDAzq4Sa3m6mEFSAILHB0NWgiWXnAZ9U0tOf675BDkU8p9fdXjL-yFabZVZX32UzjZ775EjzE3SRM82A7-LA1gqKSUgjQyVeqoQuuzpannYBIEcpMacm7Fd6kwanIsDOn0aDYSUwyNZoa1ImS4xz-H56cV_MvNa0WDcpp11_mX79xzdX9VFeI6cmwnnGHzBZwgA9bkux8ScdMxBC2WhOFGj4ONZSAqJQHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌جالب‌از استادیومی‌که.دولت تاجیکستان در عرض دو سال ساخته. اینجا هم ماشالله با وجود حدود سه سال هنوز ورزشگاه ازادی بازسازی نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=SyutZo7M-EXViyK_UFk6Pix8BjICapuY9xmqmg20_eko5MJuVF6UkY2yt2F5ir9pCsDwLuQxGnormvBhVIs5T404mp6aZe3LRlG7lq44IeY1l2YL5LQ7DHiNw_AFeJ2xBgaNUfphlb1w_YC9iU7FS_sUP-HnCd6sDBP1c2Gc9yOHUawf92E9i2ssoRoxFMDXam5fdFwwu6X3_6H6LZfbkNOTtUb7CGLgUQVlnN-bP6wlVo6vDnD8YaXjvFei_E791HZoO_3BU-Iizbc4S-XbfUHtPhYXh3mWuEeQJSpPDwEK9u-mmhJq2iWHXb90fxf0ciii3gTWXqncNBBQmBHavSbgXpnZ7l14Lih8qtG_A9D8JBwu_nFX37p8SXIbAcO9iAZzWzZIpI5GqeRuKZrRK7TJ65X8XL-j4rVeQ-5Jrts-6mhWuFtSuP1oNI-RJY91f6ZQrFcN6bLzLzRhj9pnJLOOqrJrC-M3DZffthl6bgBRLjYGUcRGnF_YWFAG9tNK54OhDSg-1hAfmFqEEHWx1oDGLUMUOjo67aM3FX3B7r3p8hjYcTCupFzJQgzYO5yfHYifyycECccS1qVDQIdt2KDJVxZH-eh_h6T1IDmJinVTGc0NEpfdKRyiySrGXaZXT-w8DLtehrgiaU61thAh9BVK2YWaCo6g-6HNXriVJRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=SyutZo7M-EXViyK_UFk6Pix8BjICapuY9xmqmg20_eko5MJuVF6UkY2yt2F5ir9pCsDwLuQxGnormvBhVIs5T404mp6aZe3LRlG7lq44IeY1l2YL5LQ7DHiNw_AFeJ2xBgaNUfphlb1w_YC9iU7FS_sUP-HnCd6sDBP1c2Gc9yOHUawf92E9i2ssoRoxFMDXam5fdFwwu6X3_6H6LZfbkNOTtUb7CGLgUQVlnN-bP6wlVo6vDnD8YaXjvFei_E791HZoO_3BU-Iizbc4S-XbfUHtPhYXh3mWuEeQJSpPDwEK9u-mmhJq2iWHXb90fxf0ciii3gTWXqncNBBQmBHavSbgXpnZ7l14Lih8qtG_A9D8JBwu_nFX37p8SXIbAcO9iAZzWzZIpI5GqeRuKZrRK7TJ65X8XL-j4rVeQ-5Jrts-6mhWuFtSuP1oNI-RJY91f6ZQrFcN6bLzLzRhj9pnJLOOqrJrC-M3DZffthl6bgBRLjYGUcRGnF_YWFAG9tNK54OhDSg-1hAfmFqEEHWx1oDGLUMUOjo67aM3FX3B7r3p8hjYcTCupFzJQgzYO5yfHYifyycECccS1qVDQIdt2KDJVxZH-eh_h6T1IDmJinVTGc0NEpfdKRyiySrGXaZXT-w8DLtehrgiaU61thAh9BVK2YWaCo6g-6HNXriVJRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
