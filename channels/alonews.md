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
<img src="https://cdn4.telesco.pe/file/DGuTU-AmW67wLSqyIDJBbm3N1Yt4345HJCPahSokEtGFL2nxz_nFxcuQXC-snOYwJGdCjrU_2dX7F7EJQn2RrftnuCmwwQcY6MwdD2d5mekoj-XLSw2oUVVxpteKCXj5HPLVI2inDzVXggJ0RFHHTS5jEaZkimS5TUxizHP1AQ6Pvza9kXKvJSN601ICXyzY6JsJ2I_GYDRbRxm2cqARdVcKb4W61OmWgBfWavYEb6RZ7J8adOIjw--tY6MAyBW3fuKS_9LokFTky5YjEQ2sg6poWWpaHrjql-ctA1DARqhB_kmloUNF1pYWTtDky2rErLtEZh-zqB0qT5ptF0b3dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 23:41:22</div>
<hr>

<div class="tg-post" id="msg-136809">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c650eb82b9.mp4?token=Jnjfl0p6FSjP55G9PICtzN7I6FEDRUJyxhEPWVsLC2q51Neko1miogXCjJ3VJQaFQyLXrV63XWDH6U0LzXDL2L_H4x3koFdKY7KxckgV9KPbwC994-BxZr2NhglzQMwO4npMaHfBMJK-W0EhPC17Nd_Rp_nhSdxfFFKPIAOVQrQh-D3MwvqGD3i_gKKEhCraJBP_0GPfQuPJq8kir8iDVJ4BYMqBn5YUlOyOggq5RZqHD4r1ip-Tivw7N0-5bSMjaE0uJG-vHneh2P_yTilzUbKRU_gBU-NcqSsCObFPdrygo0z8t52LAVQTIxpxSb_rgazIOHVAOmVxTnC2aoXSXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c650eb82b9.mp4?token=Jnjfl0p6FSjP55G9PICtzN7I6FEDRUJyxhEPWVsLC2q51Neko1miogXCjJ3VJQaFQyLXrV63XWDH6U0LzXDL2L_H4x3koFdKY7KxckgV9KPbwC994-BxZr2NhglzQMwO4npMaHfBMJK-W0EhPC17Nd_Rp_nhSdxfFFKPIAOVQrQh-D3MwvqGD3i_gKKEhCraJBP_0GPfQuPJq8kir8iDVJ4BYMqBn5YUlOyOggq5RZqHD4r1ip-Tivw7N0-5bSMjaE0uJG-vHneh2P_yTilzUbKRU_gBU-NcqSsCObFPdrygo0z8t52LAVQTIxpxSb_rgazIOHVAOmVxTnC2aoXSXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران و تنگه هرمز گفت:
ما به تنگه‌ها نیازی نداریم. ما به هیچ‌چیز از این نوع نیاز نداریم.
🔴
اما این کار را انجام می‌دهیم، چون مجبوریم انجامش دهیم؛ چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/alonews/136809" target="_blank">📅 23:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c74afdfe5.mp4?token=VJuw-jV2gEUejTH3xxPPmE1PPUycqkG35yJd7B_a4maEQ1phL117g0Y0QEtEZuXZ1rBl0JLbPpLafgIPTFNgGJpxrYy9sVZL5cS1KNdgGEDUa-PsqnAazSCl4rS6nAIhSZT82h0Vf2r59_2tMqYxa3A_yzjButLCyYJDem8RIx3LxEW8VUS-X_lOi8IxwjSUbfldXJz2M7Oygup3rGcBs-6-Z4QBmQZqt1kI2O4FGSBOdByMFOkCX1nEJO1oiAN931vqiZDdilkJAzKMOo0zmUSCzPjnUZErL2Prgjnlef-M-1Qb43xmtq4SddRDaSlUDe1GRFvQSQ2J5myZJm8B8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c74afdfe5.mp4?token=VJuw-jV2gEUejTH3xxPPmE1PPUycqkG35yJd7B_a4maEQ1phL117g0Y0QEtEZuXZ1rBl0JLbPpLafgIPTFNgGJpxrYy9sVZL5cS1KNdgGEDUa-PsqnAazSCl4rS6nAIhSZT82h0Vf2r59_2tMqYxa3A_yzjButLCyYJDem8RIx3LxEW8VUS-X_lOi8IxwjSUbfldXJz2M7Oygup3rGcBs-6-Z4QBmQZqt1kI2O4FGSBOdByMFOkCX1nEJO1oiAN931vqiZDdilkJAzKMOo0zmUSCzPjnUZErL2Prgjnlef-M-1Qb43xmtq4SddRDaSlUDe1GRFvQSQ2J5myZJm8B8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور: ما یک مرکز نظامی فوق‌العاده در کاخ سفید در حال ساخت هستیم.
🔴
این یک سالن رقص است، اما همچنین یک مرکز نظامی بزرگ نیز هست. یک پایگاه پهپاد در بالا و چیزهای فوق‌العاده‌ای در زیر آن
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/136808" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1Y4NAqrJx7KAzaBalIwqInhv7xwz9THsHNbMqsLsEK7eFTTpldAnUqEhZlzoexRHrMc8_n9-YOJRNHA2gF6LsvK_YTuC1QNc9sMQGP1GmJ98niihyOygxzqL5YJP03NTXVlLNR-0IZ33tvR4fpc2EP2pVKXtkuNJHWTkEDvBD7iRiBCh_czDaA4GK6X-_RfuRuK_b4aikmMT9AQEcTD92c3Onm1BZk-r0-KqOj52Y2o7T0F66cT7W23FAXyxL7jxMH2LdzUuknRePFaRtFXVEsIdBitFdbWVclMULa8eyCxU7OLHMlhfY8gfk1grlVj3tNGPcXezzQthz-PojfdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ایران تنگه هرمز را کنترل نمی‌کند. این مسیر آبی بین‌المللی علیرغم تهدیدها و حملات سپاه پاسداران باز است. کشتی‌های تجاری همچنان با پشتیبانی نظامی ایالات متحده از تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/136807" target="_blank">📅 23:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136806">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سفرای پاکستان، عربستان و چین در. ایران در محل سفارت اسلام‌آباد در تهران دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/136806" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136805">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd1d57aa35.mp4?token=dRGbkp4QmzxGCN0qpV18fJISZVOHuu-SFHkIdgv47lyTybhaly-SFGhfoNl2UYkVnCiij6J8xgJJRGF3DiCkqqsK5tEP5z8wHnxKGpBPKjAGvegCckptUefHCE562B17mNrm05w4SAJOo3w0b_kvDIp54gDvYhJOSLeeIIkgfMX9By3KZ3sWRn0b1U3iG56jpYMNRFo1ZM467yKCbsdAWroN12FiwAcdVXOpNYj14ZA0nN1zO-tp74zGKOKO9ppg6N255ecR-eAdABwJTCbWYWxWdUG4Z6QN9esbGc6UbwYaHhmLd6BXBwo_4YHT57twkXfcpsFh6dRYBLGp_TAODCDq7aJMK4WpFMF6UfeHnj-BWo3rk8yGowUs9SyR23PbpHcSwfPqoM8GjCLcjFjZbVB4yREQvdxTGUuLtGZ5N5go3S9tgvnZOFVax0jg-4Ff-RM7O2sRaxZ8zuB8J-oSRsKDBr5NPP0KY6-IQmAV1dDasAHPftKo6pdPcgFVAvgKVYfh2Byuz229luSZ6YvHsrpPHAoSCdQsJkLY0JJcPMs0oced3M5yOF1PW0Rhak3vfKUVDD1t6mcJs5KYeKBNOtp532llzWmnr0UjHrX5Nt6KJ2LFktnoeIocSB4RZBGEN4dGXeViO67R_BpRKlZUTScqja0iRXgk4nbehTpaF28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd1d57aa35.mp4?token=dRGbkp4QmzxGCN0qpV18fJISZVOHuu-SFHkIdgv47lyTybhaly-SFGhfoNl2UYkVnCiij6J8xgJJRGF3DiCkqqsK5tEP5z8wHnxKGpBPKjAGvegCckptUefHCE562B17mNrm05w4SAJOo3w0b_kvDIp54gDvYhJOSLeeIIkgfMX9By3KZ3sWRn0b1U3iG56jpYMNRFo1ZM467yKCbsdAWroN12FiwAcdVXOpNYj14ZA0nN1zO-tp74zGKOKO9ppg6N255ecR-eAdABwJTCbWYWxWdUG4Z6QN9esbGc6UbwYaHhmLd6BXBwo_4YHT57twkXfcpsFh6dRYBLGp_TAODCDq7aJMK4WpFMF6UfeHnj-BWo3rk8yGowUs9SyR23PbpHcSwfPqoM8GjCLcjFjZbVB4yREQvdxTGUuLtGZ5N5go3S9tgvnZOFVax0jg-4Ff-RM7O2sRaxZ8zuB8J-oSRsKDBr5NPP0KY6-IQmAV1dDasAHPftKo6pdPcgFVAvgKVYfh2Byuz229luSZ6YvHsrpPHAoSCdQsJkLY0JJcPMs0oced3M5yOF1PW0Rhak3vfKUVDD1t6mcJs5KYeKBNOtp532llzWmnr0UjHrX5Nt6KJ2LFktnoeIocSB4RZBGEN4dGXeViO67R_BpRKlZUTScqja0iRXgk4nbehTpaF28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ایران:
من این را یک درگیری کوچک می‌دانم. ما یک درگیری کوچک با جمهوری اسلامی ایران داریم.
🔴
آنها به شدت تحت فشار قرار گرفته‌اند و می‌خواهند به توافقی برسند، اما من می‌گویم که آنها هنوز برای توافق آماده نیستند.
🔴
آنها هنوز برای توافق آماده نیستند. آنها به زودی آماده خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/136805" target="_blank">📅 23:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136803">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a974815af.mp4?token=jCzkSW0-OJgeBXTk1sUPbPwhmQMOB0UsJA6XQqe2KtrvKYKAJ7pcbKVcW-mbY3mlTv0u2vy15utfY0Et5v77QloHNtrnheGjO_kl0QOKF73aIz0p0NPbRjeB7ob-MB_NLk2k2BW6F3C2GLMVhedxgoEgXXjTJyHokLRPbZX_amKYXAPNPNU-RZCbwLlfycDna-7EUXGMT8earkgdoRi5cJy5_5zulGLfvb1a-MEHICVUhwGD3poBB2rIZ7k8-BsVizwcWQ3TkammopchRMVu27fQgnxvhIZTzHvUL4oOtY-fTt7vtp82Kt4PEk7yt2yfYQa9tQlTgSVMPuh8goxEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a974815af.mp4?token=jCzkSW0-OJgeBXTk1sUPbPwhmQMOB0UsJA6XQqe2KtrvKYKAJ7pcbKVcW-mbY3mlTv0u2vy15utfY0Et5v77QloHNtrnheGjO_kl0QOKF73aIz0p0NPbRjeB7ob-MB_NLk2k2BW6F3C2GLMVhedxgoEgXXjTJyHokLRPbZX_amKYXAPNPNU-RZCbwLlfycDna-7EUXGMT8earkgdoRi5cJy5_5zulGLfvb1a-MEHICVUhwGD3poBB2rIZ7k8-BsVizwcWQ3TkammopchRMVu27fQgnxvhIZTzHvUL4oOtY-fTt7vtp82Kt4PEk7yt2yfYQa9tQlTgSVMPuh8goxEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در سخنرانی خود در جورجیا گفت: همه‌جا موضوع تراجنسیتی‌ها مطرح شده بود.
🔴
مردانی که در مسابقات ورزشی زنان شرکت می‌کردند، همه‌جا را به‌هم ریخته بودند.
🔴
تمام دنیا به ما می‌خندید.
ما در سراسر جهان به یک مایه تمسخر تبدیل شده بودیم، اما دیگر این‌طور نیست؛ دیگر به ما نمی‌خندند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136803" target="_blank">📅 23:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714c9598a5.mp4?token=HP7HZ8Rydb2hm5kBuuMVJls_vM004sNal_Unfr2KyquI0BtltLqn_L6rxTUiSBp-T86A0udUH3lITzJaNR4HYdKWZ00i4HVrSu8gE4s35K9uqq2dotEsuTQY-lXeWs6CHxvtn5pKAsSn47CXp6V0EZ6S9swT9D_ra_81qw_vgOIUbHDy0S7hgsvxr5NgED3iBF6tueBBEvG8PBvQewQKxZPEX5XBNL-Sc9WuWE_lkWvLXsvCuYaW3knfOhjJBnzuysByihurKCY7YatJ7zgoHaIqMEM9NExDbV5cCgfqidqUQSxVdc-Is0Wkm_dxb7MD0HLI3N4x4qRqTS1UOGPLgzuQjOr8TULxMyvoOwshB7JCNzcz2nKoCxYrGng3NYKGcCTKi-nRhoFIUe9TTWeBK_2luyQGDOozY4bY1afTJXABFgOY7jCu4QzHMf4C_BFGBhHW9JIiJX8tEOFFY7r4rV2p95PA92RkzjGg8mNt7iLLt4O5mBIhN7OHA9k9AvYv0mjCjyi1xHRxdbKZUCVoO30BKFpYZA1zHd6WB5wOuoC6l-MtH92e2Gsl8cr2_zHh89aj72gYN27AE5c10j36F3e5slC__fzOIxstK4Lqw0NKg7YOSTjZN6VMy0nNESZP2qPQfEDgmIbhTADzwsKCVi1NUv2X78qkiWd49vqSngU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714c9598a5.mp4?token=HP7HZ8Rydb2hm5kBuuMVJls_vM004sNal_Unfr2KyquI0BtltLqn_L6rxTUiSBp-T86A0udUH3lITzJaNR4HYdKWZ00i4HVrSu8gE4s35K9uqq2dotEsuTQY-lXeWs6CHxvtn5pKAsSn47CXp6V0EZ6S9swT9D_ra_81qw_vgOIUbHDy0S7hgsvxr5NgED3iBF6tueBBEvG8PBvQewQKxZPEX5XBNL-Sc9WuWE_lkWvLXsvCuYaW3knfOhjJBnzuysByihurKCY7YatJ7zgoHaIqMEM9NExDbV5cCgfqidqUQSxVdc-Is0Wkm_dxb7MD0HLI3N4x4qRqTS1UOGPLgzuQjOr8TULxMyvoOwshB7JCNzcz2nKoCxYrGng3NYKGcCTKi-nRhoFIUe9TTWeBK_2luyQGDOozY4bY1afTJXABFgOY7jCu4QzHMf4C_BFGBhHW9JIiJX8tEOFFY7r4rV2p95PA92RkzjGg8mNt7iLLt4O5mBIhN7OHA9k9AvYv0mjCjyi1xHRxdbKZUCVoO30BKFpYZA1zHd6WB5wOuoC6l-MtH92e2Gsl8cr2_zHh89aj72gYN27AE5c10j36F3e5slC__fzOIxstK4Lqw0NKg7YOSTjZN6VMy0nNESZP2qPQfEDgmIbhTADzwsKCVi1NUv2X78qkiWd49vqSngU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در ایالت جورجیا با شوخی گفت:
من اینجا هستم تا نامزدی خودم را اعلام کنم...
🔴
شوخی کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/136801" target="_blank">📅 23:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630fb8e1e5.mp4?token=GZimQBDuJyy91RV6B6msei2SJ66N8ywOE2IKGWWNv7TpgWSWr8_NvZYWmHrbryfn0wyMO7IwTl2tM_st08SWelVlKZqUmuOArTbR4BjfqYBvBQq9oXRJy32xxFBwUvMPbOJnJ0mFje31dcW3khYJTPR6Oln46r8sgmdkSP_Q0i_tsd_h7BoxQkrchXTw4lc3H6_WUhQIhPe1RySTi8PBexMB_FjU36JcvTbBBMitQoa8g6005BvDZBK-XJhuCcF1wYaA1Ztd33UWMh03BoGnscp2z9T8mihH3AvUUnzUJtrnVuc5ShhwTxnJTrOUlMc5GcTzzx9bZnT0tYAL_3KRgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630fb8e1e5.mp4?token=GZimQBDuJyy91RV6B6msei2SJ66N8ywOE2IKGWWNv7TpgWSWr8_NvZYWmHrbryfn0wyMO7IwTl2tM_st08SWelVlKZqUmuOArTbR4BjfqYBvBQq9oXRJy32xxFBwUvMPbOJnJ0mFje31dcW3khYJTPR6Oln46r8sgmdkSP_Q0i_tsd_h7BoxQkrchXTw4lc3H6_WUhQIhPe1RySTi8PBexMB_FjU36JcvTbBBMitQoa8g6005BvDZBK-XJhuCcF1wYaA1Ztd33UWMh03BoGnscp2z9T8mihH3AvUUnzUJtrnVuc5ShhwTxnJTrOUlMc5GcTzzx9bZnT0tYAL_3KRgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درمورد قاچاق مواد مخدر:
به نظر من، افرادی که تلاش می‌کنند مواد مخدر را از طریق دریا وارد کنند، شجاع‌ترین افراد تاریخ هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/136800" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ:
ما به تنگه هرمز نیاز نداریم و اگر هم اکنون آنجا هستیم چون مجبوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/136799" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXQzb_fiLbihPfCr6V6hHcIZDVrlTo7Tp5MaP1XZHsbgdqiR4qxrGDzR4WWduoHIN8HcKoh6kLZ76uilJcqQPa0sIWq5J3t0Xm-NnGjD14MnNEPVVGC6LFG7bJ7nFlu19CqUCgHMVpm4uB1SNaNy1N2xnAW9YaHJSjMpq5-YCjnPnixeTYFt7Ux8luj9RnhMH1zVNpXega8KmfdS6gTZeQvwmDbyo8p56ql3XIf7aAkMnZO8LB62SQWax8UsDIMeLUFSURpDyaDBVAIwjMO2SFMGFC2uzZSBuS5_R6Vb8tCd4cGZF69XI1jwzNObj5PQyh8GC1ET5BNzWX4Vi2K8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفعه قبلی روباه پیر(بریتانیا) ۱۵ ساعت قبل جنگ این هشدارو داد:
🔴
۲۷ فوریه ساعت ۱۸ هشدار
🔴
۲۸ فوریه ساعت ۹ جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136798" target="_blank">📅 23:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyNMLHLhlZeQbBZUApaDCXyUbVRZfmjx_KSZBEetMC28Q-hzslET7-qhzcaQF7GhycQ6NVXfilGbClaYGUe1jo5xK8V--0jB_-0bW23SMkZxpsR11S7D5Tq_vtQhtc4xfkIOLB0yrmSvXGIiARRhE3gzw2cU4Qr9NppEosy_B7Mw4Lluoqy7wLSma9zxS4rocv7U9ATrYZTe5FE4ezmUfpexRp1z51_RNWfAw_EEypLrVQTMtkPGkosb1I1dVns0xHR3LAB5tSnoC1h9mlXLl9jTEewxN3yh3rgwPLlUADAM4peiU3V3R_ZSPk2nHVroYbcLOj_oOaWQmHkDAW8dkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیر نویس عجیب صداوسیما:
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/136797" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💢
فوووووری/برای اولین بار در 2ماه گذشته 4 هواپیمای آواکس درحال پرواز بر فراز خاورمیانه هستند
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136796" target="_blank">📅 23:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136795" target="_blank">📅 23:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
روزنامه قدس وابسته به سپاه :
وقتشه که این گیم نت ها و این مراکز رو جمع کنید و همشون رو بکنید پایگاه آموزشی برای جانفدایان کشور تا در صورت حمله ی زمینی دشمن آماده باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/136794" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136793" target="_blank">📅 22:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136792">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
پرواز جنگنده بر فراز کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136792" target="_blank">📅 22:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136791">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b372ec2c.mp4?token=GWxjtqFs-qmtvAdGWH1TlCr5vyEYKwYjzbLlFRsJRNGWDUgYjpT4qhsoJNzDljX1pQh3v3IpF3N0rsKM4sNa54Mv7QAXegrMFhFhA9DNtOLU1lMxQr0Pe2dE047ki8sTmI6_7HOD-Mk4UHtEppeLkud7_o1NvZHXm-CA4Uj2Z-Wbt1VahDFZ1WINWQnv3_WqZ5NUzRPDwH4KBpjY7PRLmd72PxBS5y29Mh2bUp8_jmsgv7tINgtShV5N8NYcdpuHhbUKBibxBrVTB1WcV2KT481NGYBQV5oZAN63Uf0FMbhd9Ka7B_0ThCsuWCZoybynWyu6RRWU3WWpfocFgvIyU2BFiqOZK9Qj-T8W2aoHllqPTYnLMXEAVRo5FhIhx9pJgezQ8TS1QX1lbL1YUqM5gWReuK-dlEpgzDibd6tdsTBI4zDYFOAVcrZRoeAovKO6mpxHaobvxZeAw7jMW4_DjOzldZVxkDwWDCB27nYgZ-zBwTW0GwLMjWlmBGnhRwHFityQypb9vFCdC560g41G7_2w_BC2GCZkF_7_ySslFgVA6QMnxtJY8FxkcppUsosBR44OdRFqROv-iXPYiIVkSubcJbrxRXrjMb38YBnO7nmqArlytIcePuVG_WcDEhzw_ja9fE2M4VN8kVyn-l_z4jxlDNueHUQv-LpRqdzBUrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b372ec2c.mp4?token=GWxjtqFs-qmtvAdGWH1TlCr5vyEYKwYjzbLlFRsJRNGWDUgYjpT4qhsoJNzDljX1pQh3v3IpF3N0rsKM4sNa54Mv7QAXegrMFhFhA9DNtOLU1lMxQr0Pe2dE047ki8sTmI6_7HOD-Mk4UHtEppeLkud7_o1NvZHXm-CA4Uj2Z-Wbt1VahDFZ1WINWQnv3_WqZ5NUzRPDwH4KBpjY7PRLmd72PxBS5y29Mh2bUp8_jmsgv7tINgtShV5N8NYcdpuHhbUKBibxBrVTB1WcV2KT481NGYBQV5oZAN63Uf0FMbhd9Ka7B_0ThCsuWCZoybynWyu6RRWU3WWpfocFgvIyU2BFiqOZK9Qj-T8W2aoHllqPTYnLMXEAVRo5FhIhx9pJgezQ8TS1QX1lbL1YUqM5gWReuK-dlEpgzDibd6tdsTBI4zDYFOAVcrZRoeAovKO6mpxHaobvxZeAw7jMW4_DjOzldZVxkDwWDCB27nYgZ-zBwTW0GwLMjWlmBGnhRwHFityQypb9vFCdC560g41G7_2w_BC2GCZkF_7_ySslFgVA6QMnxtJY8FxkcppUsosBR44OdRFqROv-iXPYiIVkSubcJbrxRXrjMb38YBnO7nmqArlytIcePuVG_WcDEhzw_ja9fE2M4VN8kVyn-l_z4jxlDNueHUQv-LpRqdzBUrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عشوه‌های عجیب المیرا شریفی مقدم در پخش زنده تلوزیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136791" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136790">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گویا اینترنت بزودی قطع میشه
‼️
🔴
دادگستری تهران: داشتن و استفاده از استارلینک جرم سنگینی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136790" target="_blank">📅 22:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136789">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
یک آخوند: علت قهرمانی اسپانیا، عدم کاشت ناخن، نزدن لاک و عفت زنان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136789" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136788">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947be4f21a.mp4?token=Eg_RDL_CCdO8rJLu3dAYNve9nrobyQLnVvXnh0eJEkKaT7-iA4W4IUJCRyaaTzQ4Quocf1tkHhRGLPOyxsY1l5W6p8bDZo0Yomku2gn71CNymBBKx100l_yEHoCg0JcTF-DZHtTqG0Qrrf3mN3puhAia2F6Kd4gttYqRaD-3TuyIM32OkOzCwAwpmrPmqoUPN65Fy_jzjTXIhlHrNU4RGiSEzQ339UuztB9bOzEFrL-Oyenh4iH_eFPoBcRrbk1oVCJ0pP8_POWiEZefvVppXWCYrOi6DsmzyZhDyFVxd4xYihmnspezV7ARC3fHxQgRZbNs89sFsXkQyqw48wrD-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947be4f21a.mp4?token=Eg_RDL_CCdO8rJLu3dAYNve9nrobyQLnVvXnh0eJEkKaT7-iA4W4IUJCRyaaTzQ4Quocf1tkHhRGLPOyxsY1l5W6p8bDZo0Yomku2gn71CNymBBKx100l_yEHoCg0JcTF-DZHtTqG0Qrrf3mN3puhAia2F6Kd4gttYqRaD-3TuyIM32OkOzCwAwpmrPmqoUPN65Fy_jzjTXIhlHrNU4RGiSEzQ339UuztB9bOzEFrL-Oyenh4iH_eFPoBcRrbk1oVCJ0pP8_POWiEZefvVppXWCYrOi6DsmzyZhDyFVxd4xYihmnspezV7ARC3fHxQgRZbNs89sFsXkQyqw48wrD-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چرا تو تجمعات شبانه کسی با دخترای بی حجاب کار نداشت اما تو کافه‌ها گیر میدید؟
🔴
چمران: هه هه هه
😊
😈
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136788" target="_blank">📅 22:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136787">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بریتانیا: از شهروندان بریتانیایی که در حال حاضر در خاورمیانه حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136787" target="_blank">📅 22:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136786">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بریتانیا: از شهروندان بریتانیایی که در حال حاضر در خاورمیانه حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136786" target="_blank">📅 22:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136785">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136785" target="_blank">📅 22:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuQe8RfSBNUfUa65SUL7ZSd8JW__Ca3h8JsY6vGvCCccCSPzCChtIiMtPmQbyHEu51Cv-79dlRz6sdTV8I40mZiBPxjAOF7RMsaRMvTzo0pezDcWHs9Hqpted4j4TjJ_kIUJOmhhcsw6WYJ8ZRRPA2jLC73KQRpaJJIeBpxiOY56JZZTBH-c3ueaHB0WlKegwmaH7HpVBNlYB1Ywvrb9UvTK3xfNUuP1Hhx5cYUmr3gg7kZDy_EwWBakLGspL4KolMvREBU6xVlpLWIkAllgaWZx-82Bp9KgMmcHIuTnWhnmf2twglVhjQ0t11TgvmHND1wPIr03Sux-_3r_5zN4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما تعرض شود خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/136784" target="_blank">📅 21:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759f0f62bd.mp4?token=oWFLG4p0lQXOIqO8n5TOLds4Vzla0DEJDP_-OsDBRbu5RooCfNnijG-JvEgO-6ZEO0gbxXzRm06Lp3CM-gKlYKKfHXYrAd_-L6YbAZUGQj0NsXQXjEsa7gdGjUxZEqhTurvq7RMq6Aie2dnogvk96wWb9Hvz3DWrX_Yx4hDvOaDFKw0GNm877SsWa-2dxousvjRD6pYDpdGzEs0oEZbQ3n0_mYEQnXUwIXxsdLWU5L9jpi3qzojt7z5o89l5TdKVadWeEdf0s58tyqs_QeB6NZJtg5HWvEOSCuavJvDodG-5kno9isSh99o85xENuhxsp4nCcnonPB49ht4sjwNWuByPfEUuYgSgWfZRiOGqR4yoBzO2ojP-1-el1ICFAVaDj9M18eTv0JpQRS_jA3GUUQ-XwAvNY8pVDRniLe31kODIRy64dyKljlX2ZwLd6XECbyuFNN_aPHPIwPH4b8GfFlVzudTMBzZFjw6FIJV4bVdHplDOto-T7X2mNOkPslxpzFXdzR6Kznq2mLPDffyiskibqf4QEhRTw-rWY7-7qcMMm5jczIkrk3uY8tRMSB95VVXB38Mw5BDM1RF_TVQgwGdRdXCe7CyHOpPcMZoYkIvgEFxBofAZng_vfrPDntoA6-JPjXVaN1JDdhiHUzObAjIqDBoUJ1d0I4QtzvuW-Yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759f0f62bd.mp4?token=oWFLG4p0lQXOIqO8n5TOLds4Vzla0DEJDP_-OsDBRbu5RooCfNnijG-JvEgO-6ZEO0gbxXzRm06Lp3CM-gKlYKKfHXYrAd_-L6YbAZUGQj0NsXQXjEsa7gdGjUxZEqhTurvq7RMq6Aie2dnogvk96wWb9Hvz3DWrX_Yx4hDvOaDFKw0GNm877SsWa-2dxousvjRD6pYDpdGzEs0oEZbQ3n0_mYEQnXUwIXxsdLWU5L9jpi3qzojt7z5o89l5TdKVadWeEdf0s58tyqs_QeB6NZJtg5HWvEOSCuavJvDodG-5kno9isSh99o85xENuhxsp4nCcnonPB49ht4sjwNWuByPfEUuYgSgWfZRiOGqR4yoBzO2ojP-1-el1ICFAVaDj9M18eTv0JpQRS_jA3GUUQ-XwAvNY8pVDRniLe31kODIRy64dyKljlX2ZwLd6XECbyuFNN_aPHPIwPH4b8GfFlVzudTMBzZFjw6FIJV4bVdHplDOto-T7X2mNOkPslxpzFXdzR6Kznq2mLPDffyiskibqf4QEhRTw-rWY7-7qcMMm5jczIkrk3uY8tRMSB95VVXB38Mw5BDM1RF_TVQgwGdRdXCe7CyHOpPcMZoYkIvgEFxBofAZng_vfrPDntoA6-JPjXVaN1JDdhiHUzObAjIqDBoUJ1d0I4QtzvuW-Yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند
:
علت قهرمانی اسپانیا
،
عدم کاشت ناخن، نزدن لاک و عفت زنان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/136783" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
گزارش کانال ۱۲ اسرائیل، مقامات ارشد اسرائیلی نگران هستند که ایالات متحده ممکن است به عربستان سعودی اجازه دهد تا در چارچوب یک توافق هسته‌ای مدنی پیشنهادی، اورانیوم را غنی‌سازی کند.
🔴
یک مقام ارشد اسرائیلی این پیشنهاد را "تهدیدی برای امنیت اسرائیل" و "خط قرمز آشکار" توصیف کرد، در حالی که مقامات امنیتی هشدار دادند که این اقدام می‌تواند باعث یک مسابقه تسلیحاتی هسته‌ای در منطقه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136782" target="_blank">📅 21:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سفارت انگلیس در ایران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136781" target="_blank">📅 21:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136780" target="_blank">📅 21:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136779">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نیروی دریایی سپاه: اخطار می‌دهیم که از مسیرهای جایگزین تنگه هرمز استفاده نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136779" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
در آیین دریافت استوارنامه سفیر جدید پاکستان؛ پزشکیان: تلاش‌های مسئولان پاکستان برای تقویت صلح، امنیت و ثبات منطقه‌ای شایسته تقدیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136778" target="_blank">📅 21:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136777">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فعالیت جنگنده های ارتش بر فراز کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136777" target="_blank">📅 21:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136776">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
منابع عبری از شلیک موشک های ایران به سمت اردن خبر میدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136776" target="_blank">📅 21:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136775">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار مجدد در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136775" target="_blank">📅 21:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136774">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6gMZW2YEYsHNLVlvEzbdXHEZl0e7Ezk_lwq2n3A9LrcrUcgtFv1zug446cjdnrxYtdwWvoKQf8tg5NHUpMh90fmQSuGUX5QuH9CJB5xGEtf02oIVAP466BzUIOqQ5Nrq5TL9oayF8YzXiKvz1NhbTkbzCJkG-oTloK_8Y6c3K4rG2UKrh74xmIkqRhCwwdPM3r5Nf9G2rhELcq8m29auoNI6XTrQFv9l3CJzNYsnQF71OGHBxKa6afVMdyJAbgRs2NAQtq9PQyEX_fJNUZNcju8ohqI1zHOTo7Jno__6-wffK8SKWlMN1NpNUIKEptqEPWLoANst_x7Q6j0upv4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور آمریکایی: ترامپ به‌هیچ‌وجه در دستیابی به توافق هسته‌ای با ایران جدی نیست
🔴
کریس مورفی: توافق هسته‌ای ترامپ با عربستان برای غنی‌سازی اورانیوم در این کشور موجب به‌راه‌افتادن یک رقابت هسته‌ای در منطقه خواهد شد و انگیزهٔ ایران را برای محدودکردن برنامهٔ هسته‌ای‌اش بیش‌ازپیش کاهش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136774" target="_blank">📅 21:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136773">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFogKSwRUBcdVw9EMPzTxm3TezN4rJHOMYgg8Q-KyEcFMlF8-l9cmBqdTTA4cqEhowClY0dfGg-ndhyu0L0U046wziTvbGXYc-tieLkmwyUciZW9Jgclsosozi_NSSQJuW6ir0HaXU360BubasN19QMRyMmhb419HsrIdalEP5MHJkK1mgiM4J4CDzku0UHizBMV_W6kTLJl_lzV67Q80nY1DyPB1q_KLPDrvfITkCk2lB1JByYR0mpbWPctpAFiIZqi4sg1Xq7f9eAdgL95Y2cKmtOf-4R2fE6NAfDZ1_nZsbKInir07G4EAXQSuzS_873LBR2LYZzvXUZQwA75bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته دو منبع مطلع به آکسیوس، رومن گوفمن، رئیس جدید سازمان جاسوسی موساد اسرائیل، دو هفته پیش برای گفت‌وگو درباره جنگ در ایران و برنامه هسته‌ای ایران به واشنگتن سفر کرد.
🔴
منابع گفتند گوفمن با جان رتکلیف، رئیس سیا، و همچنین مقام‌های کاخ سفید دیدار کرد.
🔴
در حلقه نزدیکان ترامپ، رتکلیف یکی از صداهای تردیدآمیزتر درباره یادداشت تفاهم با ایران بود.
🔴
او پیش از امضای این یادداشت تفاهم هشدار داده بود که ایران بندهای این توافق، از جمله مفاد مربوط به تنگه، را متفاوت از آمریکا تفسیر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136773" target="_blank">📅 21:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136772">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روزنامه قدس وابسته به سپاه:
وقتشه که این گیم نت ها و این مراکز رو جمع کنید و همشون رو بکنید پایگاه آموزشی برای جانفدایان کشور تا در صورت حمله ی زمینی دشمن آماده باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136772" target="_blank">📅 21:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136771">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💔
مادر جاویدنام
#عرفان_رضایی
قلب هر انسان باوجدانی رو به درد میاره.
🤔
حرام زاده های حکومتی که دم از وطن و دین میزنن، قاتلین هم وطنان ما بودن و هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136771" target="_blank">📅 21:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136770">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سفارت ایران در اسپانیا خطاب به آمریکا:
تا می‌توانید تابوت آماده کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136770" target="_blank">📅 21:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136769">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گزارش اختلالات شدید در سیستم GPS در سراسر خاورمیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136769" target="_blank">📅 21:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136768">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q478gblWV6TTLQYZo1DkiyZNl3wCj2oxMJUbNe9rwZ3AYble1cS1T8FRsP0gcemQ9QOSJjBNgTq3ObKqCZNdaXaKELqTyqZ9aa8qabhLepC2TmpZ5-9Q3JwkI5GhjYjsv4_nyiWuU8ZNp2L-N54djmOFN6EWpI6vIvZ0HsPg1KTqHqM0PlWGU6ZjU4uuz4yY_dEOlL-Iv4_sN5V6_xAme8GHjAS8X-znLz0yOoBPvorVDUJT-oZfmkFzvcUsEpdhcenGkTxO9rqb0H7pAtDA0fHBOf9_Nc0bqVxJXOMbxqZEGf-N2MN9VTJQZhm11hnCkH2_coyPhVu3MxT-HmL69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: دوست داشتم برم بندرعباس باشم اما پروتکل‌های امنیتی نمیزاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136768" target="_blank">📅 21:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136767">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گزارش شلیک موشک بالستیک از اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136767" target="_blank">📅 21:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136766">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
هم اکنون حمله به اربیل عراق و فعالیت پدافند هوایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136766" target="_blank">📅 21:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136765">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136765" target="_blank">📅 21:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136764">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2AYcwXTL9sCDcPQrxi6UL3-mpTwzsUic2HaTvH0isWZDjl-T3Les_hQYyACldSkAaq5Aqr2fASFPkErR9KidKn8CIo06b8fJvIkXR2pvCmM4bPbdXUAubwZoxrpjbH-FDnKtzdYlsmsFNatrM7egFFByxoMVeK2Gpnjl6UAeAHosbop5jAe7N-xxY4NnnDmmvVwg6mAjQ5HnKCQIoRHfgDrWorzLmyV07iQb4goCtKti4KQ7bAMhvhpVB-xxtTKOGQxSUZktprJSHNi5EJAwjsEUXaNEDhSs3upy-IrgWWsBh8f-kDjJsULsCOhq4bO6qGFCfQRR850qExshMDCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: معادله این جنگ کاملاً مشخص است: یا همه، یا هیچ!
🔴
در منطقه‌ای که ما نفت نمی‌فروشیم، هیچ‌کس نفت نخواهد فروخت.
🔴
اگر امنیت ما تضمین نشود، هیچ زیرساختی امن نخواهد بود، و امنیت تنگه هرمز در غیاب نیروهای آمریکایی تضمین می‌شود.
🔴
ما بارها گفته‌ایم که وضعیت تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136764" target="_blank">📅 21:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136763">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سفیر چین: پکن مایل است نقش سازنده‌ای در بازگرداندن هر چه سریع‌تر صلح و آرامش به خاورمیانه ایفا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136763" target="_blank">📅 21:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136762">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CigfR1Qif4-qxdeqdKgSYiOCXqvWEhm9fJ0zdEYnVTMRdIZHpH9eNqor6ocO1sXJO0LJaE4OTUHP84hZVVlLDZT_Fa6wrF9C5frjX5m1ADAi54fL8WO00WjUlsJl54EQDkIvIIR6w3ny4EK67VaRaTm_o9__S3jxa4yUcqauasmIhqNNIUTSBiYZkqnkCAkCP9J7t-aCxGX3qz_V-ctVo-MkePjEA7XJx2KYZg2ytiQ23GKsyS5aZsIdIW8NSVV2rXOwUUNjrx6u67YdXivRzQuudwK52_wRdiUK7f8LSWtry8l0IS2Q5_db9jYXqZuojjb2fEuZI7X95__TpddylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136762" target="_blank">📅 20:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136761">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
به گزارش واشنگتن پست، دولت ترامپ در حال بررسی امکان انجام حملات نظامی در مالی علیه گروه JNIM است که با القاعده ارتباط دارد.
🔴
این پیشنهاد باعث اختلاف نظر بین مقامات ارشد دولت شده است. گفته می‌شود سباستین گورکا، مدیر ارشد شورای امنیت ملی در امور مبارزه با تروریسم، یکی از قوی‌ترین حامیان این اقدام نظامی است، در حالی که برخی دیگر همچنان مخالف آن هستند.
🔴
یک مقام ارشد دولت آمریکا، نقش روسیه در این منطقه را مورد انتقاد قرار داد و گفت که مسکو «به عنوان یک شریک امنیتی موثر برای مالی شناخته نشده است» و ابراز امیدواری کرد که کشورهای آفریقایی دیگر «به عملکرد ضعیف روسیه در مبارزه با تروریسم توجه کنند».
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136761" target="_blank">📅 20:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136760">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پزشکیان: سفر نخست‌وزیر عراق می‌تواند نقطه عطفی در توسعه روابط راهبردی دو کشور باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136760" target="_blank">📅 20:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136759">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc7VxFd_nlTHe8Sa4j9uA0vBZyT2Mu7Hh9rJxxBEfjVw8ifGgl-TkHnNxHW50FtB79QON1TrrEW8ME4_1332Q7qvulaRp3JAkMG4NpUvfeeEzhX4g47LNgYWqMsCBVOIUQ4_YRDWcwW-qsfWQX6Bgu4c6nOwBdQbmIcUCr5J6EHTTysgq2T59m4qpcj2gRNf9-WlkwM1YIhDKYvTB5Xu6A7GIvgBfYXRx8M51zJ57KSFtt0k1PtjL4DbiFji_EhQBVwvxpmYU8U6ee8GlKU_TpwTQGRoMB7wFuw8sTPhmRwF4wwfVInfCEf9W4MoCI7scKeMA4Xv9dmmiR2xmxWHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیباترین پیامی که تا حالا تو الونیوز داشتیم
❤️
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136759" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136758">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8ff091ba.mp4?token=mPyk_qLQVwUn7DTw_7zAfnmxc9upslg29YcxpHsaFtpGPyX9CRI-Z3PLU1aspusLcv4YI8-HjF9SbvMgNyyfNZ4Wc7AvC71xvRmPM7wIGkhwHeW24jB5XUfH5GxxNQ90clxEKylqQJcX9P9kQ_1ECJFRYCaoPDyl-cECJk_omrmhJt06e4WfkiRZ-TsgGjj6ZFyARmw49t5s9n8tcQNyHKifeqnIAWUcceddlNzju9Q7GMm6CC1WnmuA7hrnxslKDSxz7wBzHbnhZWS3o9WgkJSh_q8bYYzASA8SFipraopCgiWFOym7LaPAY6K6wE8WuTcgxzCiNe5yeHRMrxm6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8ff091ba.mp4?token=mPyk_qLQVwUn7DTw_7zAfnmxc9upslg29YcxpHsaFtpGPyX9CRI-Z3PLU1aspusLcv4YI8-HjF9SbvMgNyyfNZ4Wc7AvC71xvRmPM7wIGkhwHeW24jB5XUfH5GxxNQ90clxEKylqQJcX9P9kQ_1ECJFRYCaoPDyl-cECJk_omrmhJt06e4WfkiRZ-TsgGjj6ZFyARmw49t5s9n8tcQNyHKifeqnIAWUcceddlNzju9Q7GMm6CC1WnmuA7hrnxslKDSxz7wBzHbnhZWS3o9WgkJSh_q8bYYzASA8SFipraopCgiWFOym7LaPAY6K6wE8WuTcgxzCiNe5yeHRMrxm6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسیر جایگزین پل کهورستان که در حمله آمریکا مورد هدف قرار گرفته بود؛ نه تنها فعال است بلکه آسفالت هم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136758" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136757">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس: ایران با نقض اصول قوانین بین‌المللی، به حملات خود علیه کشورهای عضو شورا و سایر کشورها ادامه می‌دهد.
🔴
ما اظهارات خصمانه شبه‌نظامیان حوثی علیه عربستان سعودی و تهدید آن‌ها به بستن تنگه باب‌المندب را محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136757" target="_blank">📅 20:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136756">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0HkOezMYrdhMs9uQ3fvjqcOgJMrF6_EourbCJJriYXtuNhQrmLywi4wQu4uYRl12Wy5zMI53HTxd0NbKpWJekEsyiqB-GjQJ4Qk2AWeW4BhYgZiwHjsWHhoTCWb9hOFfHm_RR8wee88d9deYvdlwV6XEVYAFLfaxZz9ZsTyZZiZjsGjPmjazufN8YB7_ulpa7Dy3iBbgZGUxO99mY-NdCLTllYAhJJyIFS0i_70dmy5BVEfqV9td-3JdkAZIImqTldLoZrrcfEewx3qeZRkBOcmSe7huEk_KtoTXEawwcArYVxj0EoDZrz6n1xqAUecYMx-PRdsmavkVzxiiMdZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136756" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136755">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
محاکمه نیکلاس مادورو، رئیس‌جمهور ربوده شده ونزوئلا در دادگاه آمریکا آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136755" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136754">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
میخائیل اولیانوف، نماینده روسیه در سازمان‌های بین‌المللی واقع در وین:
بیچاره بریتانیا! رهبر جدید بریتانیا از ابتدا کار خود را با اشتباه آغاز کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136754" target="_blank">📅 20:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136753">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی مسیر ۹ کشتی تجاری را تغییر داده و عملکرد یک کشتی دیگر را مختل کرده‌اند، از زمانی که محاصره بنادر ایران را از سر گرفته‌اند.
🔴
افزایش یک کشتی در تعداد کشتی‌هایی که مسیرشان تغییر داده شده، نسبت به گزارش دیروز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136753" target="_blank">📅 20:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136752">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwd_Amx_nzvg8wXMV7nEeffAWK1jjhfrYIdG8NzbFK4fzEUMNIxOutAYB0kMfpIoNZ7SeW9f44xBDMjUj8knEa1ixdSgeOKkM7Uojc1eAGqcpgEQHocAhWbAKPlZd8EEhl99M5HC_MlKRgYFr79xq2xbwmECWqwgTsjrahwE-weodQFlVmCCr1wnNRF-2NK60nojCYw4cp5XDSyf3909GZwUAkK9A2O7GrLPE7xrqeXnN8C3e8ZIwLSxsjvg9N1_julbrRN7vePB4lzYWe9-Sn_3OtQ7ZrE5SWoZlktf3kJdscApCFya5BqP9-CB3GE5tI_yekbaqxdSOUQI_NrEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محاکمه نیکلاس مادورو، رئیس‌جمهور ربوده شده ونزوئلا در دادگاه آمریکا آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136752" target="_blank">📅 20:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136751">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS8jQXUIvMb9DoM7JYRu6kqMCvf8Fxy7LHFnwraGeZQfb4Z1QeGzSZw8niAedMqxinj4TZ5doPcq3IozHrPKVGZQ_m19xW520-fNsjCv0P6ikgF7eU8I2Irwad-wIQmBgvDtywWZWs79w6EWnqJpSsyXHFVShpfKLtZV3j8v5sQMgIg9RnRUUoR9mvS3Uy7eu3DOjlg0MMro3auWpJBEAxvT2IXhlCA3m4bLtWG1QGvbV1_HuNxwMRkWJ8rlwQ9BdOMPfB2FhQgJ8GRS58L5NnP__HVUwP5i9eDAoOzlgzyype2rM0Bmp5DvqKE2vO8ea6_pMjWO9Fs3Xvr67VMZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گسیل موج جدید هواپیما های آمریکایی به سمت منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136751" target="_blank">📅 20:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136750">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ، با حضور پیتر هیگ‌ست، وزیر جنگ، و سایر مقامات ارشد، در پایگاه هوایی دوور، به انتقال با شکوه جسد چهار سرباز آمریکایی که در درگیری‌های ایران جان خود را از دست دادند، ادای احترام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136750" target="_blank">📅 20:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136749">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اکونومیست: جنگ علیه ایران ممکن است ریاست‌جمهوری ترامپ را ببلعد
🔴
او امروز می‌توانست در موقعیت بسیار بهتری باشد، اگر توصیه‌های سیاست خارجی اوباما را دنبال کرده بود که می‌گفت «کار احمقانه نکن»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136749" target="_blank">📅 20:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136748">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhtSOZDJRvCZyI5XRZlUMI1BmrYKy3CUvB0gPl78qmNfq4xUTUzXfk3MnRCJGFca7F_w9la_UtD9qU_EZYb34FN5aVJFKNL9W3ZwyTEfeNu5SWoeMw2gKE7VZAkWnHICr-v7N_nxtW10FqTmr5ayZ661pIlWQAxcBztv_FRlrmqKm1fuQVlzfRuDVKGvrTq_7ENxCM0dRxmna3cQACADCl0lss0w81Lw5R3QSTrRNJR_PHSPKRRMQIlKBU5HOB_zSb9xXTSio5W9ycoCaufYDGGxAf3w3v7Hdi-5Xjw1VSUI_I-segPCTZxPBOGxekNiVXp8KCXJCCiFf-PFE4APPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفتالی بنت ، نخست وزیر پیشین اسرائیل: توافق هسته‌ای احتمالی آمریکا و عربستان، شکست راهبردی برای اسرائیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136748" target="_blank">📅 20:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136747">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اساس مکالمات شنودشده روی فرکانس VHF، نیروهای مسلح یمن به یک شناور سعودی در دریای سرخ هشدار دادند:
🔴
«برادران، مسیر خود را تغییر دهید، در غیر این صورت با مرگ روبه‌رو خواهید شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136747" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136746">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">💢
فوووووری/کان: این هفته حملات به تهران میرسد
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136746" target="_blank">📅 20:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136745">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
هم اکنون ارتش آمریکا در حال انجام عملیات تخلیه تمام هواپیماهای سوخت رسان و ترابری خود در قطر می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136745" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136743">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU_9xMgt_BpNDH49OfvJnLQ0VAeDwGEDZaqtGfPVhIThQLjcnuN4Rt3_229ZJY-mxdK_LzpTQ94ZsxcWoejOwigo5xkRlbFiTBolc7XCgxS5v5R1giJC950AU2TNIig4wOxwaJPyFfRuvypHMb7m9Ywb3gkptkHUiHEOOTLyTEgXYQ7bARzwxQdomgB9R_OpTBWJHvsDYS4ajwQCCyDBZCFeOTTGQ79uJJR9GhvWSxqqCcx8qhGhst5eTkyTNOxsjo2MsTjOOayH_C9eAtkRp7K1b6KhmCEonPLzazbsHKKWVP5qGPqVd6B4FtxhvhpJwOeaD9ZTYb0rn1-BtPKclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af19d389f.mp4?token=ABFr21H6UvkSzd-a7pAVRnipxld6aamIs0TAhMiVs2D0OnAPJSKAxMrUeswex_devhhewR0QYMnfUQncofcozLOcLy1tkClFMmgOOQVA8ytQCA0a89-o2qZYxYUwSa-fgzIthc_09MV25k8MrpDxLC_s2_ZV591yNAhtj7kx2P7FJ-Fs8VOkJeOzAtgJUABo2dBEapAtauHqcz_3VC05OagEae3yYbrA-WyGLPHps0C27pOIslRgSJ9Q_JnP7I1z59HKTshnwb2ZRFaUMgOQKVdZJKVdSTgUynBcstLTOsFhCNcKWHHy8pXqjTCCA0OsH0iM-kMfOBg6NBEJjfx-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af19d389f.mp4?token=ABFr21H6UvkSzd-a7pAVRnipxld6aamIs0TAhMiVs2D0OnAPJSKAxMrUeswex_devhhewR0QYMnfUQncofcozLOcLy1tkClFMmgOOQVA8ytQCA0a89-o2qZYxYUwSa-fgzIthc_09MV25k8MrpDxLC_s2_ZV591yNAhtj7kx2P7FJ-Fs8VOkJeOzAtgJUABo2dBEapAtauHqcz_3VC05OagEae3yYbrA-WyGLPHps0C27pOIslRgSJ9Q_JnP7I1z59HKTshnwb2ZRFaUMgOQKVdZJKVdSTgUynBcstLTOsFhCNcKWHHy8pXqjTCCA0OsH0iM-kMfOBg6NBEJjfx-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی اخیر مرکز فرماندهی مرکزی (سنت‌کام) به نظر می‌رسد حمله‌ای آمریکایی را نشان می‌دهد که به پوسته‌های خالی بمب‌های هوایی یا مواد ضایعاتی مشابه در بخش نظامی فرودگاه بوشهر در ایران برخورد کرده است.
🔴
تصاویر ماهواره‌ای نشان می‌دهد که این اشیاء سال‌هاست در همان مکان باقی مانده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136743" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136742">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
یونان در آستانه تصویب خرید ۳.۴۲ میلیارد دلاری سامانه‌های پدافند هوایی اسرائیل
🔴
شورای عالی امنیت ملی یونان اعلام کرد آماده تصویب این قرارداد برای ایجاد شبکه پدافند چندلایه «سپر آشیل» است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136742" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136741">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d166f5f8b9.mp4?token=c4TNv01rKfR6qslnZJieqYmyKEXMesA83O4UPGlDER21r8JpQazWSNWfSaeGo2749Z2mAfwZXa_Y7lH7i0ckK3ghCC29L1KJZ_XLYCLtd_q8QltCJhw-NjHs1rndtbvwd7no8_SwUtQ6blK8K14xl-Lz09FotNLvFJSry47sG4V5kValdJh50lYZPi3eIMU7h6UWha3GW6zagBfRg9ljFQcOKSi9bQfDfiW_tYEWjBx9BXAe8vr2vpoi3izrDUQHayz3knjd45tPNY9Eo8JaTsCMZ1J9QgPAPyy9v2bz63zjmmJr3L6oxHCqsYaCbhNjnJeEzDDmp4LZY0Xddyl46w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d166f5f8b9.mp4?token=c4TNv01rKfR6qslnZJieqYmyKEXMesA83O4UPGlDER21r8JpQazWSNWfSaeGo2749Z2mAfwZXa_Y7lH7i0ckK3ghCC29L1KJZ_XLYCLtd_q8QltCJhw-NjHs1rndtbvwd7no8_SwUtQ6blK8K14xl-Lz09FotNLvFJSry47sG4V5kValdJh50lYZPi3eIMU7h6UWha3GW6zagBfRg9ljFQcOKSi9bQfDfiW_tYEWjBx9BXAe8vr2vpoi3izrDUQHayz3knjd45tPNY9Eo8JaTsCMZ1J9QgPAPyy9v2bz63zjmmJr3L6oxHCqsYaCbhNjnJeEzDDmp4LZY0Xddyl46w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عصبانیت شدید نماینده کنگره از مایک والتز به خاطر اطلاعات ناقص او درباره جنگ ایران
🔴
لیو، نماینده کنگره: تو حتی نمی‌دانی چند سرباز آمریکایی در این جنگ ایران زخمی شده‌اند! شرم بر تو! تو سفیر آمریکا هستی و حتی نمی‌دانی چند سرباز آمریکایی زخمی شده‌اند! تو باید خجالت بکشی! تو باید استعفا بدی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136741" target="_blank">📅 19:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136740">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رسانه فایننشال‌تایمز مدعی شده است که خیریه گیتس علی‌رغم هشدارهای کارکنان این بنیاد، بیش از سه سال به تلاش خود برای همکاری با اپستین با هدف جمع‌آوری کمک‌های مالی برای حوزه سلامت جهانی ادامه داده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136740" target="_blank">📅 19:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136739">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650663bf5e.mp4?token=svgmpdK6WFPVB1ny3nYOHLNN6iyqPssuK5QAcf-bSqQqqMfA44pNDuWk7oUqBL57wQPDPwU1x6-Osf5C4g6xHFYTaBEt0RSuL-9-apbFXvV8_ti8IL5-Lw4dZgAZqWAsJo6QJ2cnZog9Ud0rePfTNHuFT0IL-resmUWQvqZ7_D8J-EcCKzzYsW0-QAE3TvZJawdQYchFYcc4GFv8zjMYOwIm0eAJ1nPN1s4xDCB7vNatm20fZxxZmG6GBvCdCkEnMLeoVEUebtKooDKN623f0r_3-XQZC2_jjJNSTZLx-gXEvsdsCTKK2F5Wp4GJ2LM8f69wKkbYX7ZQWyRzo9NZVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650663bf5e.mp4?token=svgmpdK6WFPVB1ny3nYOHLNN6iyqPssuK5QAcf-bSqQqqMfA44pNDuWk7oUqBL57wQPDPwU1x6-Osf5C4g6xHFYTaBEt0RSuL-9-apbFXvV8_ti8IL5-Lw4dZgAZqWAsJo6QJ2cnZog9Ud0rePfTNHuFT0IL-resmUWQvqZ7_D8J-EcCKzzYsW0-QAE3TvZJawdQYchFYcc4GFv8zjMYOwIm0eAJ1nPN1s4xDCB7vNatm20fZxxZmG6GBvCdCkEnMLeoVEUebtKooDKN623f0r_3-XQZC2_jjJNSTZLx-gXEvsdsCTKK2F5Wp4GJ2LM8f69wKkbYX7ZQWyRzo9NZVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک افسر پلیس هندی در جریان حمله به یک ایستگاه پلیس در منطقه کشمیر تحت کنترل هند، کشته شد.
🔴
هیچ گروهی مسئولیت این حمله را بر عهده نگرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136739" target="_blank">📅 19:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136738">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136738" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136737">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
پهپادهای اوکراینی در تاریخ‌های 21 و 22 جولای، 13 نقطه از زیرساخت‌های انرژی را در کریمه و سایر مناطق تحت کنترل روسیه مورد حمله قرار دادند.
🔴
این اهداف شامل چندین ایستگاه برق 110 کیلوولت در شهرهای آلوشتا، یالتا، آلوپکا، لوچیسته، پونیزیوکا، زیمینه و گاسپرا، و همچنین ایستگاه‌های برق در بردیانسک و بیلماک در منطقه زاپوریژیا و اولگینه در منطقه خرسون بودند.
🔴
نیروهای سامانه‌های بدون سرنشین اوکراین اعلام کردند که از تاریخ 1 تا 22 جولای، در مجموع 117 هدف مرتبط با انرژی در مناطق تحت کنترل روسیه مورد حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136737" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136736">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
روزنامه عبری زبان «یدیعوت آحارانوت» به نقل از منابعی گزارش داد دور بعدی مذاکرات بین لبنان و اسراییل طی ماه میلادی آینده و در سطح سفرای دو طرف برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136736" target="_blank">📅 19:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136735">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
لحظاتی پیش سفارت آمریکا در اسرائیل یک هشدار امنیتی برای شهروندان آمریکایی در اسرائیل به دلیل تنش قریب الوقوع در منطقه صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136735" target="_blank">📅 19:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136734">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رویترز: چهار نفتکش روز چهارشنبه پس از تهدیدات انصارلله یمن مسیر خود را در دریای سرخ تغییر دادند
🔴
کشتی‌های مرتبط با اسرائیل، ایالات متحده و عربستان در معرض ریسک بالاتری برای حمله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136734" target="_blank">📅 19:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136733">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35436f215c.mp4?token=r7Cdi2eyY16DA8P9dkwLPEmB4J_DE_ExzLFdupi-TxF6iohXZpz5e0SnuppQe6YV2D3oCAgqpbCdS5E-qcYVLFGrecqKw0Kj_NctLcjegRDSRKVnrIGGG2gkBWIOeesujFfHfhC5cbxnknHwHF0uLLkEOIMsaeSie14vZ9vsip8AnF_UYTXqw5WuQpFZTX58igv5g7YIH7am7sxkkUvrF0Z97wNwk3h0LjqPaYxpoqQrgwnG9_mdvYXYRCxfu3pEYqgQ8A67thinzYA0o1VOQPttljvyMrc-KUnaoChWv-YRDhunCQdG6PldPgPot1rxUAJ_sJqVN5vtOkB_DszqWCTfQZZeBAkNjZJUuWW6l7opKaPsHdI4sSa1vh2-WQGE5rGnhHkEI5k34Y1kjztURCY6cQCCQv9PadmZ7wStO4DD9VgWSsxNErZCi_dIEYMy8mrkvJ_yb__Q038AWPVPoKKEiPItbYhI0G7YJoWb3gA_LNBK-aGepYOUalK1A8ei3n4f7mnP06jYLJQsb2IjgxzepTWFYaVhRvnQyFJefbomQMUF7Ey-GTzt7rLFaAoLz8abn7F5TQBItnUrRnTo8YYlKxeVnhlK9xxb9ajm7oGVFhNb3ZadkwdogID5YSJewtUKQdI3V9UTz9PqHCgTGiZvj9ZAvW3DJW4uvBLkXqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35436f215c.mp4?token=r7Cdi2eyY16DA8P9dkwLPEmB4J_DE_ExzLFdupi-TxF6iohXZpz5e0SnuppQe6YV2D3oCAgqpbCdS5E-qcYVLFGrecqKw0Kj_NctLcjegRDSRKVnrIGGG2gkBWIOeesujFfHfhC5cbxnknHwHF0uLLkEOIMsaeSie14vZ9vsip8AnF_UYTXqw5WuQpFZTX58igv5g7YIH7am7sxkkUvrF0Z97wNwk3h0LjqPaYxpoqQrgwnG9_mdvYXYRCxfu3pEYqgQ8A67thinzYA0o1VOQPttljvyMrc-KUnaoChWv-YRDhunCQdG6PldPgPot1rxUAJ_sJqVN5vtOkB_DszqWCTfQZZeBAkNjZJUuWW6l7opKaPsHdI4sSa1vh2-WQGE5rGnhHkEI5k34Y1kjztURCY6cQCCQv9PadmZ7wStO4DD9VgWSsxNErZCi_dIEYMy8mrkvJ_yb__Q038AWPVPoKKEiPItbYhI0G7YJoWb3gA_LNBK-aGepYOUalK1A8ei3n4f7mnP06jYLJQsb2IjgxzepTWFYaVhRvnQyFJefbomQMUF7Ey-GTzt7rLFaAoLz8abn7F5TQBItnUrRnTo8YYlKxeVnhlK9xxb9ajm7oGVFhNb3ZadkwdogID5YSJewtUKQdI3V9UTz9PqHCgTGiZvj9ZAvW3DJW4uvBLkXqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: تهدید نابودی را عقب راندیم و به دستاوردهای عظیمی رسیدیم.
🔴
به یاری خدا، جاودانگی اسرائیل را تضمین خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136733" target="_blank">📅 19:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136732">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اسرائیل هیوم به نقل از رسانه‌های آمریکایی مدعی شد احتمالا «بنیامین نتانیاهو» در هفته آتی با سفر به آمریکا با دونالد ترامپ دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136732" target="_blank">📅 19:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136731">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
منابع خبری از تداوم نقض آتش بس از سوی اسرائیل و حملات توپخانه ای و هوایی به جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136731" target="_blank">📅 19:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136730">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزیر خارجه عربستان: ثبات پایدار از طریق قدرت نظامی قابل‌ دستیابی نیست. ثبات از طریق راه‌حل‌های دیپلماتیک پایدار که به ریشه‌های بحران‌ها می‌پردازه، حاصل میشه. به‌جای تن دادن به تنش‌زدایی موقت، باید راه‌حل‌های سیاسی دائمی یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136730" target="_blank">📅 19:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136729">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136729" target="_blank">📅 19:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136728">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نخست‌وزیر عراق علی الزیدی:
ما اجازه نمی‌دهیم عراق به یک دولت شکست‌خورده تبدیل شود و دولت ما متعهد به مبارزه با فساد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136728" target="_blank">📅 19:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136727">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر خارجه روسیه : ارسال سلاح به ایران را رد میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136727" target="_blank">📅 19:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136726">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ca8e4ec9c.mp4?token=E-X7Xwk75H6_L2lDCYIcT2PYRjwxpO8kbNsigfeLs5AdKPrkDuFnHABBKCE8GbnKRmOaIjqPxF0a9T3t6BkE0ivD9q50ZrP-Xml7t5yvmLY4npDhUovXiBysKBhw51AC4aj0DZbsgw8jFNcS0VhxvAif20eI2-ownJRGWYUCDEYCc9rMCDVLyrMLoTwqibYFw7pnxZpUxrS5PkCZA0b4KqN05SzZYvoq7JpTEgQN1EqX64C4s77T41sOzFi0smH1EqJKpZpqO9vT8SA5XgaJyl6ASPLOBkMGzCfoUmn1ly9DNbKe88OEAh2KIhKUuyC-6G0VXgozJaS8ogHGQdnbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ca8e4ec9c.mp4?token=E-X7Xwk75H6_L2lDCYIcT2PYRjwxpO8kbNsigfeLs5AdKPrkDuFnHABBKCE8GbnKRmOaIjqPxF0a9T3t6BkE0ivD9q50ZrP-Xml7t5yvmLY4npDhUovXiBysKBhw51AC4aj0DZbsgw8jFNcS0VhxvAif20eI2-ownJRGWYUCDEYCc9rMCDVLyrMLoTwqibYFw7pnxZpUxrS5PkCZA0b4KqN05SzZYvoq7JpTEgQN1EqX64C4s77T41sOzFi0smH1EqJKpZpqO9vT8SA5XgaJyl6ASPLOBkMGzCfoUmn1ly9DNbKe88OEAh2KIhKUuyC-6G0VXgozJaS8ogHGQdnbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت خطاب به کارگر لنج:
من به دستور رئیس‌جمهور به جنوب کشور سفر کردم و اومدم به همه کسایی که دارن تلاش میکنند خدا قوت بگم و ارادتمندم.
🔴
کارگر لنج: باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136726" target="_blank">📅 19:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136725">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lObhwrrvR9ypxmMIZdi6mAvgpWtzr58lmveYtQRr95-Yv6W86ctY97Yq0IpdQahs1R44BRFPSaZwPPZzIb4iLrSFZ_l9UdeS45cNnYFMp7iQ31_piY723V6FN1lEV4GoWtiInEKRhzfZPo0NNtIo1rJzY7diqW3oYYTGAjFZ08h7edjPCexRKe_bz1iu3_2SCwTKBW9fjvIMAWBbQOYjrEGod0tx_djLHx9tWQmG9h0r35Be054jb52Z6MnayMJZ0DoLd3vveZlPk8FoFxthxnyWwAm5-kqQXqOtz_8JsYd62T_WuzQ96ZLg4qo_ZMjxbYMLeZgGkxz0xHJ1iKEGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت گاز طبیعی اروپا همچنان در حال افزایش است و به بالاترین سطح خود از آغاز جنگ رسیده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136725" target="_blank">📅 19:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136724">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ در واکنش به حرفای ممدانی درباره بازداشت نتانیاهو : آمریکا به هیچ عنوان و به هیچ صورت ممکن نتانیاهو را بازداشت نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/136724" target="_blank">📅 19:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136723">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
منوچهر متکی، نماینده تهران:
قرار بود قطر ۱۲ میلیارد دلار از ۲۴ میلیارد دلار منابع ایران را آزاد کند و حتی اعلام کرد ۶ میلیارد دلار خود را بعداً پس می‌گیرد، اما آمریکا وارد شد و گفت یک سنت هم نباید پرداخت شود؛ تا امروز هم این پول پرداخت نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/136723" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136722">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رویترز: شرکت هواپیمایی کی‌ال‌ام هلند اعلام کرد تعلیق پروازهای به دبی در امارات و ریاض و دمام در عربستان را تا ۶ سپتامبر تمدید خواهد کرد.
🔴
این اقدام به دلیل وضعیت بحرانی در غرب آسیا اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136722" target="_blank">📅 19:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136721">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
اختلال در متا (اینستاگرام، فیس‌بوک، واتس‌اپ)
🔴
درحال حاضر اختلالی از سمت شبکه‌های اجتماعی اینستاگرام، فیس‌بوک و واتس‌اپ وجود دارد.
🔴
این مشکل به صورت سراسری است و کاربران ایرانی هم شامل این اختلال هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136721" target="_blank">📅 19:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136720">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پوتین: می‌خواهم بار دیگر تأکید کنم. مشکلاتی که در بازار سوخت ایجاد می‌شود، بدون تردید موقتی است و بر پویایی عمومی اقتصاد روسیه تأثیر نخواهد گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136720" target="_blank">📅 19:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136719">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سی‌جی‌تی‌ان: تصاویر ماهواره‌ای نشان می‌دهند که هیچ هواپیمای آمریکایی در پایگاه هوایی العدید در قطر حضور ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136719" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136718">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBt77Y9a79N9f-fioVwERLm-CwnqAWMHCu6aAaVuDVWst6NGA40O64MtJbmT3m75E88Vv_gmpHB1t9IkhO97NTJT761ZoBMLnzDItB_oaImDBtFxKvIBfxyYcd0NYrxzlU26mjb9Dg6RNRBJiTLjeuko20Tu5ZDABzrhfTrqujZ3BT65gTi6gTDiLYvHxJ7jEyGaj-TjTfbSw2OhmEg-bbcaRREzpWdX02gJT6Hok7jgB3D-s_sAEItvbmqrQI_EWbjS59O0I4s45t2WlxCTXdf0K2rAqnSEsh_d44KaccdERzjDgGDNsRBPN1yrghuBJ7Lc4QAUTAP_oUz28PSuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دستور پزشکیان برای رسیدگی به موضوع فیلتر شدن سایت عادل فردوسی پور
🔴
در جلسه امروز هیئت دولت، وزیر ارتباطات و فناوری اطلاعات گزارشی از حادثه اخیر مربوط به دو سایت «عادل فردوسی‌پور» و اقدامات انجام‌شده ارائه کرد و چندصدایی در حوزه فضای مجازی را همچنان از مشکلات اساسی کشور برشمرد. پزشکیان رئیس‌جمهور در این خصوص دستور پیگیری جدی موضوع و جلوگیری از بروز مسایل بدون هماهنگی را صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136718" target="_blank">📅 18:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136717">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2801c386a4.mp4?token=D53BC1AyEsEktOyDT9jGRS1M_fUbCNHXTLaF56rUO9otcLEsnhN1uVaCZci3-j1nHWhW_cVSAd2JQAON9dNTkLVPp1SvU5oM6Va1oZ_XwFoih9SOX9xQZqUrhEz8P4dr1HFgAgg8639JRQyxAz1U4gtJb1jgTfr--otF65kKM0oFNcfVnapukPwC9y5lHhR3sRcVIrW1ZctaT-NktvH3z4e5oMh01TVr0hXprC-viMFaL1_WnHqyZSId6cqoQ0WG9Zx_fyN-LafyB8J7dWXiHhZ65_HubIEj4qZv9K1zSLp8HvUtXipDQOsFwhJnywu6rQIveFkAVS-Ti7bAOmzMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2801c386a4.mp4?token=D53BC1AyEsEktOyDT9jGRS1M_fUbCNHXTLaF56rUO9otcLEsnhN1uVaCZci3-j1nHWhW_cVSAd2JQAON9dNTkLVPp1SvU5oM6Va1oZ_XwFoih9SOX9xQZqUrhEz8P4dr1HFgAgg8639JRQyxAz1U4gtJb1jgTfr--otF65kKM0oFNcfVnapukPwC9y5lHhR3sRcVIrW1ZctaT-NktvH3z4e5oMh01TVr0hXprC-viMFaL1_WnHqyZSId6cqoQ0WG9Zx_fyN-LafyB8J7dWXiHhZ65_HubIEj4qZv9K1zSLp8HvUtXipDQOsFwhJnywu6rQIveFkAVS-Ti7bAOmzMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: بخش‌های کلیدی اقتصاد روسیه علیرغم تلاش‌های خارجی برای بی‌ثبات کردن وضعیت در بخش انرژی و سایر حوزه‌ها، باثبات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/136717" target="_blank">📅 18:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136716">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
اکسیوس: شرط اصلی ترامپ برای برقراری آتش‌بس این است که ایران حملات علیه کشتی‌ها را متوقف کند و تنگه هرمز را دوباره برای کشتیرانی باز کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/136716" target="_blank">📅 18:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136715">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2371f68421.mp4?token=mvzj26OqhNxdOQRgcYAdNZK_8BOoTiD7abeusSACRGCUAZfcKcrJ-Tz95zOU9qxx9a-146R5T8H2_ptuowKPZ0moxKH5Mq23JmlqIOFv1QYEm2qSDoAkvUysCMTz3TBzebGV9ucG8FamguS0GBbC2yeCfGd_cs5b-dp3O-gjySxoYdYtjTqxxN65WjJkc4eVxWcUq5-EAhd__WsXkneDNswEJAwQU6SOiyfRPPsH4UMw_YPyV2BD8d4QYsiRo5_hnPMozu2_i_1HQGgR0jWeypZNR-9A8gsoVGJjA7BF5weGOLd19LisxszMH8Cg_MmNGGSZ8w5njZvaNmHKQJFtkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2371f68421.mp4?token=mvzj26OqhNxdOQRgcYAdNZK_8BOoTiD7abeusSACRGCUAZfcKcrJ-Tz95zOU9qxx9a-146R5T8H2_ptuowKPZ0moxKH5Mq23JmlqIOFv1QYEm2qSDoAkvUysCMTz3TBzebGV9ucG8FamguS0GBbC2yeCfGd_cs5b-dp3O-gjySxoYdYtjTqxxN65WjJkc4eVxWcUq5-EAhd__WsXkneDNswEJAwQU6SOiyfRPPsH4UMw_YPyV2BD8d4QYsiRo5_hnPMozu2_i_1HQGgR0jWeypZNR-9A8gsoVGJjA7BF5weGOLd19LisxszMH8Cg_MmNGGSZ8w5njZvaNmHKQJFtkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که نشان می‌دهد بعد از شلیک موشک از ایران، سربازان آمریکایی پنج دقیقه وقت دارند در محفظه های که برای آنها طراحی شده است پناه بگیرند، این محفظه های به دور از هم طراحی شده تا تعداد تلفات به حداقل برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136715" target="_blank">📅 18:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136714">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
هشدار سفارت آمریکا در اردن؛ بیرون از خانه ناامن است
🔴
شهروندان آمریکا باید دستورالعمل‌ها از جمله آژیرها و دیگر هشدارها را دنبال کنند.
🔴
آن‌ها باید به وبگاه‌های مرکز ملی امنیت و مدیریت بحران برای راهنمایی‌های ایمنی عمومی، از جمله توضیحات آژیرهای اضطراری در اردن مراجعه کنند.
🔴
از شرکت در تجمعات بزرگ اجتناب ورزند. از تمام مناطقی که پلیس در آن‌ها حضوردارد، دوری کنند.رسانه‌های محلی را دنبال کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136714" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136713">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / آکسیوس: ترامپ در آستانه اتخاذ تصمیمی سرنوشت‌ساز قرار گرفته: پذیرش آتش‌بس جدید با ایران یا آغاز یک عملیات نظامی گسترده و مشترک با اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/136713" target="_blank">📅 18:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136712">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
شرکت اسلان ترکیه قرارداد جدیدی با وزارت دفاع بوسنی و هرزگوین برای تأمین سامانه‌های ضدپهپاد امضا کرد.
🔴
این سفر همچنین شامل دیدارهایی با مقامات ارشد دولتی برای بررسی گسترش همکاری‌های صنعتی و دفاعی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136712" target="_blank">📅 18:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136710">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44376769e1.mp4?token=pkCC4fcWaPo2q7lb55UavUmfX95Qq5xHeVOUSWDu4laEE7HTUNky1s7KtXKF2H9pQBEopI6YS_pG8VfsUcqgLd67Ma2tNLXfw26YEOSDg0P7W6xKRalRwUo7p_SXuxEuPQPY7qoAmulbz3OVuzC7QiFcpAHZFDCzjIBkMGIJAJUrkVfjNLpJNwVoFRTnGip1YMsX3RsOs1dHOiMp_U4HzzxaqISFQEVP0iVsmMWZw-rfekheZUt2WubWq2JD8ZvkOK3BvPxPuiBRjtgIw7rjb2GW_b4PQqwJrLaBUmSz5Dj2igTpYTKm8VdW3Y8p9FExJtWca1ntFbcqQVFBKBQOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44376769e1.mp4?token=pkCC4fcWaPo2q7lb55UavUmfX95Qq5xHeVOUSWDu4laEE7HTUNky1s7KtXKF2H9pQBEopI6YS_pG8VfsUcqgLd67Ma2tNLXfw26YEOSDg0P7W6xKRalRwUo7p_SXuxEuPQPY7qoAmulbz3OVuzC7QiFcpAHZFDCzjIBkMGIJAJUrkVfjNLpJNwVoFRTnGip1YMsX3RsOs1dHOiMp_U4HzzxaqISFQEVP0iVsmMWZw-rfekheZUt2WubWq2JD8ZvkOK3BvPxPuiBRjtgIw7rjb2GW_b4PQqwJrLaBUmSz5Dj2igTpYTKm8VdW3Y8p9FExJtWca1ntFbcqQVFBKBQOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که هواپیماهای نظامی آمریکایی در حال ترک پایگاه هوایی فیصل در اردن هستند. این اتفاق پس از حمله امروز ایران رخ داد که در آن حداقل یک انبار هواپیما آسیب دید.
🔴
چندین فروند هواپیمای ترابری C-130، به همراه چندین جنگنده و هلیکوپتر، دیگر در این پایگاه حضور ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/136710" target="_blank">📅 18:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136709">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9eYpkgfA6Ypl4rrjwwwG158st-OBR9orcU0B0S9p1sFKJ3uWwj9habP8LbHDEP53d7YuS-GH_gHG2cWhZOjNED0kURb0vadnN7ZuU7TqN63iYizQlUFFeXeXONMp_ToY5CnJ3Nzl-_MbaePQsAcA8UOPhPw6Ozi-vCdoPFf0NfRZh8uB8TagAij_7Y-NLZuVkY3x2_A5Bghc27SYVNprqZ48zFgYeFlxJD5MtECHkdhpgFJheg4oXsnzYTsoziLGzUL8X8HRCQKSqt851brrV5GcBU7XOd7Iyg1ox7-d1I_cf9hhOAvpIMysAGZSDDsPQ9k2L4q0L1caI6NqNc2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای MV-۲۲B Osprey متعلق به نیروی دریایی آمریکا در فرودگاه مسا در ایالت آریزونا دچار آتش سوزی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/136709" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136708">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرنگار: آیا ایالات متحده تلاش می‌کند تا سوریه را به درگیری با حزب‌الله بکشاند؟
🔴
روبیو: ما به سوریه توصیه کرده‌ایم که بر چالش‌های داخلی خود تمرکز کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136708" target="_blank">📅 18:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136707">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نیویورک‌تایمز: اگر انصارالله یمن از تردد کشتی‌های عربستانی از طریق دریای سرخ جلوگیری کند، حدود ۴ درصد از عرضه نفت جهان از بازار حذف می‌شود
🔴
خط لوله سومد در مصر و کانال سوئز نیز به عنوان مسیرهای جایگزین، محدودیت‌های قابل توجهی دارند؛ زیرا نفتکش‌های بسیار بزرگ قادر به عبور از کانال سوئز نیستند، ظرفیت سومد کافی نیست و در صورت استفاده از مسیر مدیترانه، زمان رسیدن محموله‌ها حدود چهار هفته افزایش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136707" target="_blank">📅 18:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136706">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApLLLgwyGqH7QgKHufuDyY3jPh5WAl5oALaMvMJldLOdHoTSpchMrTswUuACsdrwNXC_oXfXkqDLG6kK5WHyxb5-NAv5eyMPbVGCxRY2LqfxzKsL80oQxOcW41uH3n4FSguqNytBxBrOoQet33ZkAeS9OZYldkIjj3OEF-t7DNGb8AvgsCSdLW0jIWewpblm6Fdx9p0Czyl8wWui2uzcbivxmwirPlAj-G80Vt1ZRrg7Z0f9z26ZxnA4oB1cUM4ZS-4A8AShpKV9WxlFmbQSVnK_-qSsYJ_jAsXslIRAvC3idk3jXpkLOuHmgcgIHS5BMxiaBcWgKnT9YFWNTg3KTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمیخای چیکلی، وزیر امور مهاجران اسرائیل: ما باید برای جنگ با ترکیه آماده شویم.
🔴
احتمال تماس مستقیم با ارتش ترکیه در دریا وجود دارد. این یک سناریوی غیرممکن نیست؛ این اتفاق می‌تواند فردا صبح به وقوع بپیوندد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136706" target="_blank">📅 18:09 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
