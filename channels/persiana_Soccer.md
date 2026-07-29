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
<img src="https://cdn4.telesco.pe/file/Z3Ch8Y_mxb-anIyJIR8PBMgI8u5-UGKPWkvQCO4lOV6FJjib6ZQRPAHMIcHj3V_iBPdm8-IpO5Iy_wl1WKkOt-qEjJNWPAtX-J1Yu-yz4WsfBDUK7iebyBfDN3KFs1jW8_7mOXGuAM-2Amx_K-aQO2NrZ8B8q5-Dfdjg7QGNsCOvvWF-NltI8nzsTCcUVATD9QYsCPVNlYoX1dtYkXejt75ldGGjW5Bnt-Z62iqvTQhz6ddS8Yc6OBN6NRgUeUe0J5Q_S8kCXKH-qXDOfpqvpHwuwDxKpJfZHfelfVUPxYXB2kibrO62yLtSdFHJmlVpM-aLou-uEkfevvKaeLT1CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 18:55:34</div>
<hr>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3lB2h8HXbW-gyZvzMR4nJhvaAI8g5kS1alWnvB0pDrgZrqTsA4wvBM_wbI8Cf_vlbtRmL_zgLfhq5eYJbxpSMOFzJkFJvuvsOcYvMxnTl0yP-DzD2ZETzIB_QDo9OCV_UCkfjTDo3VdJlzaCU417mFmoadZ47qTwLPTBRyItx4HcekWJWsVQLskL6WgGaIJ_1C2s_D2SYwmUHkDPfmKTh4wOxAZzsVO2rJLzBVbUkI0nD8yAl_JAF-VtYapq4q0koOaz5cdmewm6G4gje1azzTxHZN8lGFLLqrUzzYAtb1Q0dk9pTw2eVXjtvDbVO177E4_uhfQ-7vcHp0-a5wjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqpiTTot7-N2bcDHdN5ttwKoDvm4KTzNmDKYjQeF0iW2ZsMOjHkhC5ZzrY72bfeXByC88eLhiUdj_zt_DQhgEige8R-XUGA_FUhZ_GSnO_xKSWdXnWt2_Qwx_GuFSI2wBZpwaW09_YbldtLJahT6GbyPQmU69HrYiVBqeAppzzWYvWvQJILSH9mUn24ZJhFoup38ORIdTWhnLLzIfKiA9RwATk7Y7DT_aTC21K2Lx0738aopqh5JR5Kx0DyVYc-XaHap-04NCaZ6hiEX34RP8KYFnUcHdSgt2CNR0fvPNKRK43_az54nOI40PCrOUko2QxWld1GhJeMDOMN_E5-EZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivmS-FwcCJlK4nqwkDJPQoxMhNsgIAxWfvWI2k5lOXVtXdxKYRkTLumpSH7rCKRC6tCX1hdasGVn0igtjjvjy6RBG4WtuVxD67Hoa-0PLeyYd6-qqE2bSlVzjIM1PQHTI213Z42E78uZB33Edu9V7eIyHT7O7RbTlqaB3KFx_vGp3tFO_BBeN3aLCiS7hN_CbSAq1o-ySH-bE-OoGDRo9LoJM8MlK-dUgqFQtv9t-alFRWOqe8LFd5kUpZJidsvHF8LVv06hGQ4hY8_CcdtCoUnM9xSZa7wqwjw5fhA4TuZNI-bldZuZ2D93utOzSeOyr4dWsJP4uThOwNLNngBfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzfLErNOGS93aEHwdLuh8L37TZF89CGc9X2vczmvaynGlioOhbM9M7LANcFaBnf3Mu_N2MNJzEsFa2GgsChda2-QQdWlQY6rucFc6xzt4nfdzrhe2jW2ocRg89qhxz8Jwz3Z2ij-cV3tjF10t2QqPLFqEmJ2oOxth784asJNHfPaydCPXVx35r4k7_HV8p_LpVxwUYvOgagfuVuWBrtMvk0GEl5tFGMU7Yphh6qe49j5ZByEb6JwW00TMcVNQVHmoHFsd58T6YV-5xdD0iVdbGjI-Em_4v4gmVbh6q3qID-u89KHrQQCw61J76RZ9xRyy5IVomCm5y_uIkHr2H_I5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnb6Gxx3JVum60zVFvTjqiq70crjRrpEsq3Zv6NRn3FB9fi-I7f7Yw3jO_aup56umclhWVzPXXLqRTkoi0TIM0EawQ5131dMMDXfSVNrUwuh7Eq9awIrVamygVPhERnMxcD2l0xgS2loSYmmVTrP7iDPVSX5uCvz1yHn13i5LKRLhbEYZcfuScgZwBzhtQBe_taeL72ItGICfHk754KeDPctyGSfthKFnEQatAJUx6Hp4IPNo52lxSg05pxSkiRT5oH9chLhq0jS0kKRjmhfgqXajnvt1kRsfNpqEMyGixxVwuHYCvTUc5vjr72vzjlx1Pc765hSWqO33rLckVoHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcTZxAP5Xh4wyHQjos2URJARMyfYvyKkIOROyxrSQX1OB5zQwGBsV_wguccngDpXeSKMtigf28a5olXwWRv_eX_dIjK_jvSM-xpDf63sWDfCLojiIUyUoXoc44SdYegq44_wQsT26tkEG_Cu0smLdlYKoakg23i3hqZRWNbmCl55Z6wabDtNeUYbPkZYKUDxlUu57Cto7gaaK6_SlVjnvmEiG44V-_8pphfgQez7XPUxeYnSMn-D1qyoZW9A77XfKg5zhhWbd9iTkwR2ZYaN4p2YIYBkuk17YgNfFZA-SX4U8Irr8QVZmFBwZQbuzKBvgmutI2AkutLzTwKdaHrqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26758">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnxBCZXOK1pnY2omkBJW5vH2ZeidUjsAhHLV8LBrgon3kLWvFhHzpXHdWYqxeKHX6KqJSUAPvOS7uXCNadoo6lO2Nwng6kG_9ui_68aeBLzLB6bw2-z4f1cL0ekkhxL7pwTOlidNsi1OhaDBAilsiNqigxpI7qBLAbNOqnM5bBJRt_9Obb7Kq5VqCImxz_cyO0va19Dd8-XzLunR9IE0cyPn-VInO6bYan1aQ9tMVGMcQ5RQRfq6yYR7UziUHZlWJiZQd4lo7OZWLMZ-7ttnJ9syTf1j9od5JNWySh-BW-56d3l4sMOl9l8A2jESSAb6FudZkDJmreaz0VAByOG-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/26758" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOSmWYz-tLMVaZRiZIPHoVKdzOMPaYpWjhqm0HTbFABpTpT2dPpHieHeWId1blBq8lMUl35x4w0vJ7FvONi0K0ISzyyFN6XmpgouJ03poFpCjfbww_474ocyyNL3LVT9R4xaZxBWwyXMmoKY57MlgxB634TJ_o4rtPJnSQvq90VqM2T7jm7Ba63pgLCgjh_byreEd7CTO9P_MHSy5RBTX0nCqgDUPoYsZTw_5s_ojyQ80imj9Hx20Z3Q_eV-dEQKJvxKi3WB4B9hMS_zqEEuwOAb4ey5Y4M2zWsl2NM0ssmR3BEIAkr07D93B5i3w5ITatp1P8j71u-NlY8HSuzi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7YMMUfzTu2g5fvskE50DGJKUsnIOBmwpsTXxS0nmcPD7NR1wnTrZOFa5CQPp148I8Q4C-ruV6Dx9DsDso2z5btPmFoDq7rr3v_89AGgmOdHd5tMu55EBtHdNA2GBHBfhR36Da0ePwBzfo4u0NyT9eA8GZ32jgHo63rhYfWI_VsT10LprbEqtxbSZ0Dv0GmFpFueducmcixouerxJfMqdMXlsZNXtrJnyB7yZ_bOaBe5iTB5lIEmS6CcpEnBtDj3ryaJHxKAnbI1WebnYI8_yCpDfuNj-rfVLpl0ZMiYj3mESOszs-YTS6C5U6TbuqHZziwzm3jEpixopOnu9neuZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3WjxLUR8ANyWMrTsGW5sqhcwsbcCJ1veo3yYbk3zCyxcr3FxDOAaZvab1-jmqvW1CQW4iqHZQIbxY68u17pCZw5iSHOusdEmYISOG3qBkfNWDit0tomdkogszFN3bN-GvodSZ3uNZtVJ9K1JDMVBXRayIuvLMzszBQqyZL_N4MbrYo0_0p3iI6sdGMEJ-kbTJKUQG2F8Uo_AIE6hBOVnQo58v3lg11PR1ws45OuQ0_VR54EpnryV_vCQnF4N1tYw1trQNe8kx0JxeG4IrCZfKq3UmchZB9Eiu5wLREGBRC-8e80jv3_tcuRZPq8p1gBOED_N8fxOc7PYHUycst0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BneAuHU406W6H8LXHJ2fEXrO39dP-7yqVcCvr9NUiuSQ4rXIqyh8fpYAiB2YF6f-ndj8KITWKjG-_9tlbl8g2BLn8m-jI5La9YqKAYQwVZ3m2HBMvh_v-gEEO0pjoct30NWusRb69SkyeWLBvKgUMShrTwRfgMAyl373JS7KGcfGHKYoB8rYMxyuXDVA5KHUZjg0L34Rc0Mbnb1b5reGwxWYpKxgd64b6CIxU_nu5yKNbpI_8eHtN_CFhqdM8TM-ZhTCjH5m6osbpiijawifC05xhYlw_2slbhFoK3dXmPK2PUiG46UiqCZYNyFdXULmGgTbCEO42xJZe0vDM-Z07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Ho4vjv9vB3TjASE8vHv9YHgIXZ0F1yYCnb-mB-zGdW_pFPhfzeV9xrsEXa7X_Fo1nAeog_ErVFTIhr3tVk09J8L9_7yEekUFoWv1fWiKj8_4lNj3kIG-CpUl1U_o3UX8ai84iQqivOQMV1LRwxFTXvfqcRSgX1ePdvxTOdYQqlZWg8RWSrNGOXPTK3ketYIDjRa0j9TE23kjgRBZ1TdMwpw3cUCiQcNJEd1iXqut3vvaxOdqfG_ZywOgZHK8ewbk9Yb-LT5RIkKGXtbJxsOEfgQTkDrQIHfw_CpJjacfrSWEYMyjLNhe3tXNdNTRilhCA4OztcxFxZvvPmaxo6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aknC9ltuYi57cb0QG8CX0uhpd6aP_UTdz5baGB7YK2a7ahVgU2uQaPH0GzS0hxJ0U9zbefq12iu4tzgh1uDa8UfVm33c-Q17LodR4ayuBDkiDrytmeUbmGcdnPuk6__pnKdUQ2JiQ2wmZWHHCC0FnYcm9e_vp8a2SC83iK5lAleXYicUm7XbM-O2tqy4xJTQjFHZg8BVV3RqyqSv3Yac0z5pCbijr-voN75nqxgqPCusRwJwKt70S0x2GuUrnSN8xA6chACFqD4rZ2bHM84Or4hl874fSrN7LzTQXOoJNo8iw96R1k8xxNChBRC7OuxOtXaHTyT86BUg4XP5DpTGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx07aEeIkAoCI58EOHj85eZF7h8S8-yIj6rTUldIs0P8fjmI9bbieUryERUkZa5qwfwkLHM6UltnCBQ7cx6LgoUF-k1h1Ur5woSuXPWsOeRulNJpUZJwsjo5O1I-6SKMUj0ZM3wkNyezmOsAtGux3TUu6FM86b9HoNslBLRQKXdAYMKlkIAaEGF8jQfIB0E8ROgzfWeSUID_rW2I5rUOSfvDWzjww7FUYTuGWsOoNj1fK2-QJ50gg53qpMjk_o6tIkimLIWFBeEmHowO9S23d_5kQR3ITNe8rfnKbD4gwbS0_jdh7yAawly1x1izASmDdYyZVT-jO6-9UzrecgohVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJF86rxGN9cGjhwYZZ3VCABt0UjtLI03pq5FDAgMjDlBFaTFCLfbOoeQYNux4hZWOtZ0RV_FJ9TMri6EIEGToKrYpUck0146MPQy125s8QxhThr91BU6UmDrdn_vI-SxHLA9bKKo6KXjZjL8v02-1sHjKtCXjeKuYBHXR4IQYGsEM9SVXi2zwqIPapqp6y2oAISDBbEhwKU0Ep83jLaEufhB02gKWwLE4a_f-HZBHdBx1gs_agY0U8Rutw8lVbKQbyY_TCwxLSNgThW3lEt4EU0ET3v7entXyjzJI-c2qM5Nw4jBkofOoFZmdqmIv3_noAlNWKzQPr8JISIz0nVJRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhCjIDt9twmOcctLL8h_dAM6V2CSRtiKHkiyOqgogge_AUMu2hk7a40bRZjZ0kVovsZJSJwMcYBZKuXNslWuDKg6HCt-jPak7v7Fk2eKB4RcquPYvLMeHr1XfQT4ZVkipR0gfulb-gGu1gmHzTzHHyncXvOJhDqm06-UMZ9d547NWKKtu-gd9IXhTvY2Kg8l-pW0_XYAY4BoFwYaprSPiHS6dCx2k5fc9RI3e4qoELfArJvvadH3xIw-5Q5Sd3WRsmLVnsRRwOmKyH0OyXmM6VG0LrcMhlCsxVaHcouiNhP7yE9q7UH1v7loWnb6BOCZGO6ZcM5lMPes-GCoC-of6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3BJGSWqYoutgI9r8-Otc4BI9IMj6rddID-Blw1cb6rj2ygSQJoxII5wxw2byz9mEzlhBwt1JSq8VvgBujvZ4lGi6UA8uQ0PwCx2EukAnL1ZyqJb0qWSoyNeFp-Y37jq2657BZsIP1odv5HjcyLXad67jjAkOMKxmFjiWG3BoZtlUx82Q4UjhQ8kcLQJ_tXXRh04V9RG358aiW5nRu2I3sjHLgogBS6gFh9k5F5LgHFhrmssZZSY8TyeXMNakeQrwmfvl5XTnmmz8nRovMoTgsKDVoGQt-NsNeLuXe3A9osWkTDMPG0JlBKg-0s5up_EZlM44-gmIB4DuQ45YRbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juPhyuGkucOn07p6S4xROgtIRoHs3_r1DiSgP_UXtPteZTFmT1YVbAYHl5TKSR5HlzlTj5Mwt4OXPKvtoOVWqKPbJJb8lijDiQdhKS5CMx7katpI17GxljxKrpqmWQtuIwpgAHJpUUTjbV0nrfrSilm1zGgnJky2Cl2K9DlN13sWUGya-1jPxeA_H-kpXKy63CKmboauthgCOiiR9muAqIn3wWaYbffgkXytxi6BQkFEvYmlMrIYxd1kxaM3le4dL-uTZG4zI-9s3X8m6maEy6MyBFB2dHZEV6y5sFDPaX-jC-q18HLdCXINyZw-HLo5hvoYCMeLE0ZMYCwqLsL5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0JvGmOW-sssEO-QTodu3KnwnpQx8K23chxDhcXoWWQux1A5nnxgmlqe3puc1OBuoPC7pvIGMFqCFLKQGm_9HyPWuwxXYvbonf0HN6065S-FTubLHXFzkebNcCCbz3OmLNMwCtfsx_jH37HJpg-7iji3XWagpOXV3no7d8_di6vdc931KiiBZRgX40uRlyXIeJMozNgI-vS_-OoMTap7qiZZEbKAaBembKCOmPz6ytqczCsuszDFcB3BLKnW-bhjPqfqOQrGRW4GOnaKfIj4ZFuA7QpqgZzxvbJk91E9pn83Ml6MJCpfAgAYs0wJYRpyFLFteaTBZM7qh2vGlWnJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gICxKefYIbtW0pQYauMQ1TkOhnm1jAP_--iO8r19NzHk1KOtyoXLYAQpmrNVqf03Vp-22p7Kifpy1MHmaawU3oX-DwxQSXpz8waz1bSzCUCjB08whVvZ6lcKWZgist5s_poD5fyI80slDqNaeK4WA5lokjuYQvcWBLF49IMUfk2dwO2LedQpI0q9Fao2SMV7D8tWToeQbBhFqly1QDMBcFsgpJpdRQILLoB7iOgAtzDZw7GPF5Kr2kcwZcdgA6HMko7leC13q6kelXplY4ST-S5D9OJuACFKVrdBovKKYVR9E9oLkhC2ZUh-N282dvkGK9mZiZNCCMDSGO3CnnSvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Ys5tQWALWk1tYgkroqs86UvcNm4UeHN5y8Aq1fi8RVxkhPwFEtbRT-UcJTna9vRCV5QDk9bObJ20wIlTPj7nZu7mtU4kMam08mkNIDOkj1B3rMgj3r2X9KZYUN6GOkOGN4lWsDPaM13L5lDN3LLsFDtel-vPdvDwkPSusCn6mzechnUsl7vqd7i7YC9qTns9bjVZqfrPKHGF_B0TkdeXFf_eVFFCz7dWIjYh7rnqEjhOmTn5Y9yVvc3fo0EJOaIw706VRMHCHPrDRaGayb92HT8YIJsnSEGRs8Qx7tUHOcoTwwr5x0oiJMYS4rdHmc_xezFAg0cwnC_VzpfA7_T5OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Ys5tQWALWk1tYgkroqs86UvcNm4UeHN5y8Aq1fi8RVxkhPwFEtbRT-UcJTna9vRCV5QDk9bObJ20wIlTPj7nZu7mtU4kMam08mkNIDOkj1B3rMgj3r2X9KZYUN6GOkOGN4lWsDPaM13L5lDN3LLsFDtel-vPdvDwkPSusCn6mzechnUsl7vqd7i7YC9qTns9bjVZqfrPKHGF_B0TkdeXFf_eVFFCz7dWIjYh7rnqEjhOmTn5Y9yVvc3fo0EJOaIw706VRMHCHPrDRaGayb92HT8YIJsnSEGRs8Qx7tUHOcoTwwr5x0oiJMYS4rdHmc_xezFAg0cwnC_VzpfA7_T5OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6A-dc0G77Z3YzAIYcFVjhnqAby_RIG-RHw5oRwORuxGNqwPbj_ZMyCVXbcYoaOMZTPGpgi1sTWTjdmYwWhyro7SP3TI1RBby6KqqOftd0NphP6MUAKLwPlkZElREAM56XJ1RVOLZW2FVZYE5wZlgE8r3_tCjmgACR6UgRHm4VRGvkwswJ5j-FeZcdeqEzHJEFS11v-moxwk-V3C8sNLlt_66-1zOw8l1pippMqPaoUdN94CLP3blS37Rzuovk0n3f2pYcnsugHqfuGAIzIeJci_6MfLoUGidUMK3PA7hhhw6EK4S192ax2kePGbv3TEY2IVW7whJkhO3zf5gHYLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6ApQ-4gxhlfn2Xm6pNkFRserp3kqlAwUkRrpjiLsnsxziBvOhikZY_aaL06YpfXD257OfIze40TmFQEtqiDan3UgaQXs8oSi75DpxyPl1I03wfv3V8RRyXRg6Aj0WM-pMO36JPPdoBVaAyFo1mc_GZOY7_ivC8dq3zFeVV3cs0gXOjSWxtDBkBSRPZTs13IOd9rhgNum653GjPe9ERoIvJ4Ot_feXNHhOKL9bmm1QkaCGxs1NnL1h_K4GGPBfEnHV4Rz6ceKU7GNdpytXxQlN80bPAu2iroiZe2WUtlG8JUFjHBoLcZCOUGF5gciTfVTfEMab8_qvbS5_sAMA6bMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrgNRlRss1mIAtMgmEVPwG4ANe1aVHdOVWCvTqhp9fsKKMS6YAIBTt4laKvjpZeWKednQGFzvKsX7uf9JWhbY09vB_7tr0Pm0eny0J5HUfWwZnNzobrCBWTHO8m3kuoThBR2s0QGqiAs9kPw6iXdqwYTqPybkeBo9itQt1qT_WKY3sAFrLD6wgE6OXNpudCyyQJxSkc7qcvCeOw1ZH7P05skmskgyFHFW6c466rtEmRuWiEYXA-omx6yRoTgy2x-NWqWorr8-ifq3m0Sm9g2-GfAEiaYpBTMKOPlh3zbcfA54nCqvgjMqmxa-e8BRldOesDfvt8DdLvBYg-KM60MPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26735" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oshNibq_rBML009NgHjFa1_9TeABco3rUOJy_doIm2aXx0qj37puZSbLq4z8Z7UGq5N3noQcegCdUt3OC5tH-oQWmtlwvIesNwpyJcn2UGjSmlexi2A5TNwJlxEtsQ9V9GMt6YGwehtxIbBx1TVKy4PBcalyvWdemOQ54iUSuxaASIMeQXrGk8ZTvO9N_zvyyPjW2-2nFso1hK0Eoj-lt6O5iTas2RmVjj4_hAhEhs5KeTh3HXZ4W9ZvxXW0Rf3pPSTAemVdyIRGlBSlOlwZMHKEgzJIE5cQXsKdqRcHdECY3noleiS9jCWxsEiN_Tse58PiuU-Ymz9RiY_X5lF6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=ipAIEFn7B3UGiY14UibzVauvkqqkwV_7i6qB7BEdepDx4ntqCK8MTsaJjDdh0G7W4g-zpd3wVEMYvuSxo61xwSU7BLnQYV9yb5VyltitmBz0oGV4ZlNhwbixCxAw1QM89NmxbQmsgaosvfKZ2GSbZx8S_ooKmpJ11Rip1iJQCyWUe93YLT5H-Q91V6_O15EjTloDw-Fk_Yu3xjo1C0T3eoPZmiMeElFN7yVyAmo6WKxP4YcaTiekkC5P_pV5KI-csAsK6Az6nukH6fezkCxgghYLpf5SRtlGlFaTMea9oE3ByXE-loeQzeh2gugLWRCX9IoVUD5fS4sZ6sHci-kajw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=ipAIEFn7B3UGiY14UibzVauvkqqkwV_7i6qB7BEdepDx4ntqCK8MTsaJjDdh0G7W4g-zpd3wVEMYvuSxo61xwSU7BLnQYV9yb5VyltitmBz0oGV4ZlNhwbixCxAw1QM89NmxbQmsgaosvfKZ2GSbZx8S_ooKmpJ11Rip1iJQCyWUe93YLT5H-Q91V6_O15EjTloDw-Fk_Yu3xjo1C0T3eoPZmiMeElFN7yVyAmo6WKxP4YcaTiekkC5P_pV5KI-csAsK6Az6nukH6fezkCxgghYLpf5SRtlGlFaTMea9oE3ByXE-loeQzeh2gugLWRCX9IoVUD5fS4sZ6sHci-kajw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=DroMWrAvOMgwqVPiexvEHl3-FafxtXBVCynaIki8nWmiK3Y4xJPrxYJ21CmyGbE3b5MPxYzud32YM6kvKMQdxCzyDTK0FcRuUwP8t2kFlwRswcB0hBp3S0EEYphjL_dtDCUZQ9giTjXfuIc9YKfm30X40BRXJihfdXMz3IZgZaSy6s2GJUeKDAlkCMPkkf1a2JYQrcNorloCE4ahjL9ljJDs1vMOd7m70Ouh7Rds_wlBKvIwr6MTIj6JBebM6dTLVxpSHsr3obd0hb0Z8aer8NWkZJcsE-5HHl3Jtz0w22g-33uN3Kp0ExTq1h_SXcRdwMgPpiFVF4BRjYUcmqIMhgbduXXe3zF9RJOmMoYf4Kyb_fLwKO3imukodMdUEzRMoBQoi29TZd-lDhU8BHJ6EpUv8vJW8yaiDe5ro_dU4Hjq2S7Ai6gRL3sqZ4OISi-Hv90RxhIDpc44poFWWZsKdho9Y-kodolVLMUnEGUwXHa4u0DhLB634PhOCBg-D3hw6ojZ-h6kS17IeJHVqPtPxnYEcluqNmqdklU7cYl0boUb80MybeNc6nXff1Kae_AVgOilh9YhKby6MbVkk6y14PK308Sfrfb1YgIwaQWblalrZk45kFSTBfzrfGqgvBggSUBSN-RN_Ji96kLNDkGPIy8JEU9bpYtRuJAZ3eiyYdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=DroMWrAvOMgwqVPiexvEHl3-FafxtXBVCynaIki8nWmiK3Y4xJPrxYJ21CmyGbE3b5MPxYzud32YM6kvKMQdxCzyDTK0FcRuUwP8t2kFlwRswcB0hBp3S0EEYphjL_dtDCUZQ9giTjXfuIc9YKfm30X40BRXJihfdXMz3IZgZaSy6s2GJUeKDAlkCMPkkf1a2JYQrcNorloCE4ahjL9ljJDs1vMOd7m70Ouh7Rds_wlBKvIwr6MTIj6JBebM6dTLVxpSHsr3obd0hb0Z8aer8NWkZJcsE-5HHl3Jtz0w22g-33uN3Kp0ExTq1h_SXcRdwMgPpiFVF4BRjYUcmqIMhgbduXXe3zF9RJOmMoYf4Kyb_fLwKO3imukodMdUEzRMoBQoi29TZd-lDhU8BHJ6EpUv8vJW8yaiDe5ro_dU4Hjq2S7Ai6gRL3sqZ4OISi-Hv90RxhIDpc44poFWWZsKdho9Y-kodolVLMUnEGUwXHa4u0DhLB634PhOCBg-D3hw6ojZ-h6kS17IeJHVqPtPxnYEcluqNmqdklU7cYl0boUb80MybeNc6nXff1Kae_AVgOilh9YhKby6MbVkk6y14PK308Sfrfb1YgIwaQWblalrZk45kFSTBfzrfGqgvBggSUBSN-RN_Ji96kLNDkGPIy8JEU9bpYtRuJAZ3eiyYdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1VCF0D89oZH9Z0rOs9aNXj0uSx9RBcWj6E0GiHdkJFyedFSrf3qEOOjT98ft75G9BuAhu0odyobfXKV-Ro17Q7Kh4VeK2hFqh6sh9ZHzSaLxog-PfeKEjkrHZjWTt0PYmRsiNc-sH4wscX-xIC0Ply3YevVEdjckyVXCD8Vq5E0Y2kF0CF3wfaFyeKxVJNjWXS5FNfwsV-U7Br8VVwxcTj5DBMzT6aAkTDuGH8HNWcuhtpOF_GDvgkkZOIQHPIGkz1KcTWOh4Wfj4ttiozt5tc5Zm7Hi_eTi1Io5NON1ckhBlXM7gnO31_Lu9FldBW68NZxIwrMTGEkl6dueMk3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1otSme51lcsgaACWbTmAMOaEDKeoFP41U-H2gyWINr9Rfjoc47EldmB4zcb1f_nJHnRkLW0ecAXr1ixioOFcIzGWlaOst5n7p_DcfMGCrZ63r_TC5Oy4he6Uo3803LQsHZyl4JS5PnAN_LG3PERPScQZXGibUqxqUDE6LEA-r8HX_UhhGizrpnXxrhYLyUDV-CGQy513752r8JWUqUL8Bmalq97SS-fvMUnRVCzubMDGP_hxw5sa_sdCAvF-dMiLps9kOBKKDF1MjbhanUO770kGazITKWoSRPRPHPnxn1aoHLlyrfkATPhU4RQnVUpN3miwvqJ8s3I5iwKVV5RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCvOQDbEDfcx9QLHUbOSjzGhMkJtRVjkxAVztNGivD11aFn46aNkF9U8gvIcFGFKjoHHGqV55DhBWVriAEXeBrmhU_fdAAp2hIdM5qScoZRlqByLmKAvHknFzXpeF9Xhf0W3rfRWBWMgSJfTccqUr2La97s95-hxWccmMhQkoI_V6aMl7qnghlVBffb-ohWDzyEjK2iXghQkWuKG7guIfWs11Dawjx7Dv9ktFcigF9AkY0bZuKIIXJCXq3ibUs667-lBxyB-CBOkgBREGsdUv6Nd05Tr7h4IflCBoWadyHUcw_x6hOxVNJSH0u2La2ep6uucO1KD1rsB2yROwBK7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTfCLBXV-dh04TF5xO4Sn8SYrGcuC03qEoU_AAX6emM9L48bDmWiz5yWiuTjwyoeQq74OMqvZpVevFkZriMKm3netgikghXCwPVCCzf8FxvAKqTBsHncKpMQdmtHS4LUPnGygz6rTkbei4j01m_s_3mmRrRT0Gs77cWXNAcCQBeCBnLtxhSXkPaHMCTGP8MMSP-ybCoC4EOXln_aoRHcNDYJRfl8RaVGdSzIMIptd5HJwO59yDrFYAsirByLMOAp8-MgMSADSFajk3KR3DTs_rFBcA1QHPdLfgQCYbAicCB7yWOEUJeOqnd2tcDPTOfXkmUZ36hNyRYX4GqukZ_GGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvO00pcNgDO-_A_tRL-w-t2af914k88-xdCCUC-oKP-KOHGS-QaoIav2WZxOlc2Lg0HFBqsghbpvkvHFjVLNOx1vjdl7F0At9U17u_6YhuZuIyFl0lQBaYa0gD_E7auPYBFVZ16zD4zaY9okMEL3OD1LetsGaAYNVj5jmqPGsNSKtZOIK4LZXepY3V10JQXXKTMDTQnSngII-zZLnKFmg1HtCh27IQ4MfOFIVhSY_VkigO4JEvoJwecBpTJAYbMsZ7l_SKog1ekjFOK_FxdYs5_zp7kMacUNJzAXt19TP1pBjigtjqzwh8owoLHczmwvDpTHvD1XsCKaq4Vk7m1MTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQEUAjP4xXOzjk-fFMnPSxZnMbW2CyQ9EtYWBv-yapeofXIoh47Uk11QdshuT8Q7NnORtIL2OMT8Cl1ojZaPZB_mgXInn1NYDv4aKPyfgIwi1g1oHv9rr_ry8b2-ZfvkB-k0lgRur5B8nnR6Hau9QR0Ar_o61cyzUfWfgQTROHMjom7Es0sZQqZB3EP3CfIgSM-tOxmGPylUEedT7Y2gvYUQQ6upJb69lFBe7HDYv4Rdm6nTyJg0n4oB96dxdoUiCM426dYtS9lPturSldCleMCgkYtiFW3OhbMeYeYs9Iu1OCnHZZdTZ5s_CtW1zi2Nx127E1V1s2U4joKAHmUalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjOSUHO3MRA4cTn_4Ma4pAfkPFwsa2_FwVp1idcK-vBAP26tMowJcgUVwgb4hv0MVjS5KXoQQNzFWM2Qn5PzpffxYrJNPwNBrT-WA5fMPVesd5Z-sLosC4WAr5NlbS-X9hUIYr491Jy8ReWporUWe52_o1ZRZb0DZu_uWGARtVcsVwfWRW-WwLiJzXlGoCLc9GL-kJdUMNGklnwcP4Ilevek-x2JiDBVOZCdu3FFf4hfWlDDNH3Ibd1KPEW-V1JKVBV4FfTKrz32V5ooJN30OmOOilT7oYY-WIfheeDSZ2s-U1ka7zGYKnK5tLOnYgEHm0JZd1ktVyqY9TPZI5gBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=upnT-ijgh4cJP_ab6YJ8PDABOXteRHHy13Fc_zLXY2ZL99g5ht1lN9PtytIiP-URdvBtoSEMtAd3dExptDkJuFvq4AFiMnvMcr8XtN1VAdhJJ5fU6FbYIhSIOtegvMNuyqQgWtwxub2qJCdYRtMtsfquNMa8aJkAPJWg9Gz25mNMt-8YDIrk0kpXMPyAUWoGBiHJ0r0i-a-vV_Fo7O6v3Ab5W3B-XyK1DtAwfCZw0wjD2ndXofOR3bPCXF2wg2wed9YPiYuT0OvamjYUuGhiSspv2yl_Ks15LqKE7KDaUr6h_cAIxW9pZL7ICy5Nsw6xps-9MjADHgDmOkkLmx_JpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=upnT-ijgh4cJP_ab6YJ8PDABOXteRHHy13Fc_zLXY2ZL99g5ht1lN9PtytIiP-URdvBtoSEMtAd3dExptDkJuFvq4AFiMnvMcr8XtN1VAdhJJ5fU6FbYIhSIOtegvMNuyqQgWtwxub2qJCdYRtMtsfquNMa8aJkAPJWg9Gz25mNMt-8YDIrk0kpXMPyAUWoGBiHJ0r0i-a-vV_Fo7O6v3Ab5W3B-XyK1DtAwfCZw0wjD2ndXofOR3bPCXF2wg2wed9YPiYuT0OvamjYUuGhiSspv2yl_Ks15LqKE7KDaUr6h_cAIxW9pZL7ICy5Nsw6xps-9MjADHgDmOkkLmx_JpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9FWvwtUVAtMxYEqONN97EzDYjIZCxASjwDTTK9BMiuaCntuhJM2rOpRL0TjdWrmjxZRFLt9iNtY9DAdYaXvG33bhLdxN0anwOZD10VHY9vKaBVFV6qaTxGqVcq0xVVUSMZUbH2DfrrM5cG8ZOrRVLQ_Jmod1qtcyZg3NQU86HK_0zJ4Pfuz200jK0Vay1HqRtJbITd9GVplb5zbweOcCTsJ2StbtZ-TyunveVAAg7K0hkvYkw6SzhuXJiOVOafBpLrKmP9HRNr_jFTD9legHOWIfBvUFnY9HKnPRk12x2d2DGjJbjh_Ft9S70TOfhWQFyURYyYylKcLX1ZQuc3-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXjiJeTBzH34JNgzN1ogDjmvkUO94c9HNsOCy68PhP7Ia13bD5-Y1ptfEsgz5OtBK9w7wMTCS55QzrK6lTYWgaRQ-vYsHsaeRw1h4CGs7868gjcbDXhMJYy-FR2ikvLdHxjklpFL49HUZ8fn80wkpTJDMqZCyPOY52ZFLvZYzoLck7kOGJXj0gkTo3yl8otQw2hP_B_zG7E5s1bCkIo0S3itzegtDG6gHz5n5vfXb6ladqnOxLreHydg_oFd1mu189s_U4WJ_YJb0mADCcvP2h9ydAcOpuKpq2zNEzFsoWDniNDyfKK7GeyP9WrcvmGfZZggiZ7kpcchf22lxNbD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF_7xTmOOwCHDEZvPw2fB6FPOMly2Q2prYwCWj_2KOCUpJ40OuifdjkMfrknYyoMTh0vRjgtxW67kPlSWRE39s-MIWdRve_y1aC2xoFBkcyPXkfS-R1RTzkscnO1Wn9iVp0AiuF8FYAn9W51k-zeZ01lYofZzihMvsYozuslIs-uPXZUVaTeoAzVYoOyHwxr3oH1zv6kPk9SiBB7TxbRx9gtwE9Et8YQLp252QNZ3ZpT6wy_GZOBbfS0TjQxVJiFAcRckANEQorqiKMZusvM5o16lsaUjCGeMp-xSMt0oGteDBSpM4WXUmDAT3Z1XOAjzZ4GlzzfWO5vODd8mFnHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9VTVwS46Bt0yEfQB08ecwdEchrvS4swyAA-5N0MUNFEZYTmJ7man7Csz8R7OHEyUufmTPv6a6ZEKMiwpPsFzfhp8lTSISuDAEUHlC9_-E7j8IMqpx6FWshdBxExTGWK98f4Qj_8y2I-0_pz-8y7WgO__qrn8pMdY_IXe654P49BRlwUhoPcoH6kvp0_eeCrU-HdnE6lfuukyxn_OsKgIGDU89UzEqIaSq-8V2e2-o3y_KAa9I-s45CTmdn-i3r0gmiszoIasAm-ZyksoYAByQD2zpuGKXFpncIwk-6s-5BU1d53WW-_I-2Is77vfrzuHEdZ-3l4ZTP6xMgB0wYFWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=aqBgdC60Cj-mVcEbbpd1xagno9kCGm5EuT4dStzaAWXss8Ze8i2rvyT4irbKMA5S1lO0x7B4kOjcM7QfjtiMJOzqQqVaKg6XW8qPjcJWNrtqieG6IBTBibvneKmwEt9_SW0d4AhOpoejb928GQvMLkowrBsV601POd9_aNxFxPP21yR4rFR-9qjfiLPcMZ2vIqbfVJ8Elpa3M_fwQd5BCxcvIhQHxwhiP8eYL_bfTZOfEI47K6LvVVmk_WZapaXqH6mUDSFfyYAsERXcyWvamJ_phMd-0Xw7j1rokvOMdhV74FbWfApkEX3Tg1y0KPpV01s_yYAJXMlX2F-tjsf5Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=aqBgdC60Cj-mVcEbbpd1xagno9kCGm5EuT4dStzaAWXss8Ze8i2rvyT4irbKMA5S1lO0x7B4kOjcM7QfjtiMJOzqQqVaKg6XW8qPjcJWNrtqieG6IBTBibvneKmwEt9_SW0d4AhOpoejb928GQvMLkowrBsV601POd9_aNxFxPP21yR4rFR-9qjfiLPcMZ2vIqbfVJ8Elpa3M_fwQd5BCxcvIhQHxwhiP8eYL_bfTZOfEI47K6LvVVmk_WZapaXqH6mUDSFfyYAsERXcyWvamJ_phMd-0Xw7j1rokvOMdhV74FbWfApkEX3Tg1y0KPpV01s_yYAJXMlX2F-tjsf5Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-0sxz-tTiJx1mrdgdMYqCzieU979tVTrjBr5qmbltAQtV3BIIJFNoPNbVb-U5Au0Axd_TYhlAUILyykOsiRCvm2iwsLTcLGeE3Eev7CKA5ZOWmdeF8iATT6yqY4-Bi4vC2QEN-mGnLhIgWAXHr2njEL4UGfIvFmp6cGRlQVxFEV5vaXMuVKDGWe-SGP13Fda3VigiJMtGXl1B9GoALQZ2HFe1_CXNcU5V6auKc9wLHviYrD0Vw-nhpmW59UzXvDeEQB8eHC0ovb2wsmU6D6knx5Ruj8YlsfJIX6Tk9VH2uA9IuuhzhtCyWq_7BRrZaYfk2Fk3SNh7tLw9oqb9-KwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8DupcJgAPq0XKkpQL0jNs5MEIJGzvLzogboMfFntZH-U-dEfn-aFhja6P23SQsHH7VsUa9Q3BTELEoJ-WXP1QFkx5t9C1OlLAO4Kwi-WE9v2kVyG6a14H4LF_bixeZqtItA5-4I_4QTCS-z9Q2hpV_pWwneDgrp27w0Gh0GEuC1O8fXTWSzMApPIrWPdcXhrjLYW_w_kvcsHRDcqa9vjyGYLpGLcoN3OW4B3YTIA_lPF99pr3kZ-P1mh12V54a5m7FYZZY8cF0uvtahP9dzA6mrS1X_JM1O8YBGWI0SJP_yn_m-17TKHtDjav8RtPTbkIE5_n_ou5uos_olDOov-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciLFnCRcgr7_3vMRcW57fWeni-S0c4-JD0VwJYfK7JfgifyBo9UzB8LV7BGm5dzpxghfNutxMC9cbiDXuw-ioUN5CKbU0J5XZpMdFY2YChZkDLAU7lWc6xaEywTmBgPiI_4iNX2xcnBBFIYk-MzBlU65xVY-jr5nlw4DB3J5xNrLqFYyUUZaDNvOFBo0Byusl4CqwUCX-eT8s3LT3xnpvZYcn2JmoF766j96lxYegsTzpjlqdJu1UpNvTxevK6Lov0rkmDiFNSCMxklGCFPUCoU9Gy7HGgwSieE4L9wweh3L9g4B2bsmRyL_cVqInerFvtWAtDOz_ZmqKU3I_OlgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=gFOnIkTdX3UV-NMQK2NUcdWC1YFJmjTXu7B8OwI7tGgogsLePvWH8pzz8QesWT_nZfxonPUXIbdDKiPlvpia0F4TfQ_HXwwfqUrTk0pINpd_3qgRbNi21bdx8unJkb4i8wVFf8scfKCypCoEBVWZL3ZImsbXHRn2xxhh2olmAeOE2ZruQF9iGhVCza2CJZXxWjSOP7i9kPX-_SUbSS4BnBYIgpJeljNgtjtdDaoW0LHwkDwERQipNuhL_uiiBoZMCERwXSgq2rJ__Tm0xmFVOWKXfP_kNtD7FPtsTJm1B6h_mN6KEtdRsgbqk0XaerISZLLRuYr6ia0dSwqjr5GxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=gFOnIkTdX3UV-NMQK2NUcdWC1YFJmjTXu7B8OwI7tGgogsLePvWH8pzz8QesWT_nZfxonPUXIbdDKiPlvpia0F4TfQ_HXwwfqUrTk0pINpd_3qgRbNi21bdx8unJkb4i8wVFf8scfKCypCoEBVWZL3ZImsbXHRn2xxhh2olmAeOE2ZruQF9iGhVCza2CJZXxWjSOP7i9kPX-_SUbSS4BnBYIgpJeljNgtjtdDaoW0LHwkDwERQipNuhL_uiiBoZMCERwXSgq2rJ__Tm0xmFVOWKXfP_kNtD7FPtsTJm1B6h_mN6KEtdRsgbqk0XaerISZLLRuYr6ia0dSwqjr5GxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=bRP2QZMja7ebwtV7GVFmorO-3DomdG4zFtBKqSWTajCX9N80tqrKYzf65aA-i9Yw7p9KILKwQRq1LtxpBKhynjR1vB-bdAJ6TNSrR4ynUzO905VygXsJi-k09-wlJl5acsAi7AH1daZ2qjxeVCIXfYxiSjJrVvS-bwxBqTJ3BWYmyK7X5a1wFLo-95bzdSyhGqUHP-b-L2640k6GUrq0Z-U8lwa36g7SGgXT9A4yaCIsutyEkh0chspivU-TuP5gXOLviUkRaGatHc1IWqKII3CqGxU_vNBN1U1WqAuYdnHkSrV0VLfSrzbOjE0Xvy0N1WrzOwNKohEA8k5GF9HsmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=bRP2QZMja7ebwtV7GVFmorO-3DomdG4zFtBKqSWTajCX9N80tqrKYzf65aA-i9Yw7p9KILKwQRq1LtxpBKhynjR1vB-bdAJ6TNSrR4ynUzO905VygXsJi-k09-wlJl5acsAi7AH1daZ2qjxeVCIXfYxiSjJrVvS-bwxBqTJ3BWYmyK7X5a1wFLo-95bzdSyhGqUHP-b-L2640k6GUrq0Z-U8lwa36g7SGgXT9A4yaCIsutyEkh0chspivU-TuP5gXOLviUkRaGatHc1IWqKII3CqGxU_vNBN1U1WqAuYdnHkSrV0VLfSrzbOjE0Xvy0N1WrzOwNKohEA8k5GF9HsmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF-cgWHY4zf6T1paCQPmQQKcHw_n49yFtMK8pSP9YC_FLcFdX1A5Dy2UGOg94rsA-C7Bio_IqT56Zbef51-I0PhpsqQwdhiTCxkKWdbDki7q0Eiy0C-LgweCnOI2BRFC-Ms5ZbcTbwhUvp8Wr62ogYZ1MQtAXg3Yfz28-bHxks2G1CrKi6RrdfgS0gj0Sqjb_T9HAZ7wbTuOAluwi5DV-gfhB4tzI5ZYgnUW7pewkRXqQe7aG1LihIDG7419Bg8_L8DzSLYPLX3iZaXwO4AaUXUg5he1ijzuZMeRqnCPFvyEuwb6PJDWmpKFWtX39C5r5Clq_mmhIO3B6Pgj8lxyWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSMz8orjY9RPu6ELxqMmuFyd2DF7S1BIyxZ7mvfgUnkCM0fO5qVtqZp6Z1aR4sUWv7c-1zEBlFvbPhm6sQEtq3u1HBFhbk7yV9kp0QnHNUUYfWIjAVRoJ4QPKMcbkhTRU4lPdldEiw32muu5Gm3H7rH84NIgea5oLz0Rjm0Uh_5W0K6mfALsrmSWNSpk2CWXLaIeJvaY9Or7pAZ-rmL_6piJTzOTps-RNawHQczzbNunyeOAEFStAquRpOzcApy_chPbWh97inT9IsQoJN7l4D4pLVt2PeSobvPaIV0gjmpA8lly59ut3LtFi4sS7LTEA4UI2HKopPedNzTE-MA3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=A0F2GopP2GsD1guV7LAMV0d0Y01p6ev7a9oRFwbqGbAPy7VGZXxxE60DFkw5xxGjTt8qEU5vhm9PJBSS8zDF_QNUnuEhna6cKUw9DtsKEYVjrJSVW7p0XFvmPxHCcF5EVxhaShjSQlz4pLYKY2TeE7CgoY1E8HcTTG5C0fkhjlbw2UtQUzuallvAts3eEwnJWBfkoTmec0YN3-pUo1OaOh7v_c3aoz_uaz1L9gvQGAQmgTbM1iyzaufgO0W8ImIYLoTBrwKx9h5YbaogEv-osnNQfprZNIzCc3eZ27ntbTPkV0bibQ3UtyirOAeaAstTC7n1IMpohsrQhshl5SOekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=A0F2GopP2GsD1guV7LAMV0d0Y01p6ev7a9oRFwbqGbAPy7VGZXxxE60DFkw5xxGjTt8qEU5vhm9PJBSS8zDF_QNUnuEhna6cKUw9DtsKEYVjrJSVW7p0XFvmPxHCcF5EVxhaShjSQlz4pLYKY2TeE7CgoY1E8HcTTG5C0fkhjlbw2UtQUzuallvAts3eEwnJWBfkoTmec0YN3-pUo1OaOh7v_c3aoz_uaz1L9gvQGAQmgTbM1iyzaufgO0W8ImIYLoTBrwKx9h5YbaogEv-osnNQfprZNIzCc3eZ27ntbTPkV0bibQ3UtyirOAeaAstTC7n1IMpohsrQhshl5SOekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-nzUiTO8aKxLLip8Wcs4yXtmgKA0tVSJRM6GsVLHbJFURq8XpYGw8Q-k8cX18Y5VtOkyjRx9jo_7e3_H5pzsFSjHD2UEFI5hDxtqGvQJVwnmRAGyd5zTj8RRkBibt7Q32mhytjBs5-W7G8fB4hBSw0DSgT7jb3JPkiDb9si8jd-Cd386HNj74OUAetWlQkiIxRdtb15PMJ99cNWO-AIBBNNgObMUY1lF5GIAVJFOCL4ThiTdygPDSDdnWWb4ofaoNnRVQuQNGBN6VkRDH83d0B4ZkO09kG36y7OzKrynohzVq00mPKpwm1ZRhFOoXp12q9rrT3EFMM-5HAJDLbZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYbaHM_kNJQQg-Ubu51tbca-oHWXiMznElwTrMzdZ1tG69GgG6aYRCg9S6mm0_5WkhDfOKDvpocVWP70k2X18VAIrfoYkIwDLryIct7WgHToVQVfUt5mJTUT0jANiaK1V_aV9TKWS-ETUpfwo1AcESRXqXQvWhWm43wfRnHWnRaJX01nJO3MgDiV_Q0y2VCtrDSPFVQCQwdjRBUIky3dkqKbJi7-6rxk2gtIiARmvgS95sgSr2bkxLbhWwbCg7XAf6cx5taeGjuTAL50Veb_9IcVcK1RuUYutiD_Rx9F1_D2jIHG3Rx0aLuL6OgzSirD-jn6PDW7AhjG24lwR5grbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5PfIAaVMSp-kivPO7NJnArInor2ywST7tecEfVZZ26at3W25kSq_NzaNRD31F8ZlRffLpn5GFGB07w9JBVrOHv1zi-O9cNTezq6eIP_5tyqVORZjbAuQ_OiKG4iXK_9PY8JUe6969-99-HyHSevL9Tm46zwwGbHHPonUx0hMdoGF7M1nK4vs5tXx9eAE1kIZM6fV-oY-kaMGHTQSzDX34DGKgP1_pgzE6t0UVL9QU43oPh9ieg5EA8Z-KQkXdEcN2nwzNdDFnmsaGMwLeeBUZshzNATkBXJTH1DlJHxUHNKe8npEMDknCkMB1LaEVi67ozNwiXDh_f3NY_dokI6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=GYnilr7qWIy1wAuHwr1cgokIPQbDWJNSb2ZoiG02ZujZFjefgBsqQr1CNEfsitGFGzvnCwZXlM4LZL_psmr4Q9iftIYnO6niG1e20aBvgTDGEg9kMP0QAcl1cb2j11y5ewQHzOFHo4-Rg-YAj8CfK5iqXEf8W6jVwNtSentJphbpnmP1AjQyFogpua5u3-5do7H6jnXbyQA7TmIqTYMyV5v9hU49XjNN6VHWW68OfUpmK2HTs2vkxAdCYV7bmffdyyqIZ6Zt1U_8CDkOhu3cVXe5-FHpCaXRRYAkxVsAU4WbBciNp8_ZjAtrgBuzjemST69f31Qqaklwmu28q0qsyiYX5Vihzg54jyEh8Nrt2u9UoBuyGj3d9IGJJVuZrVtl3hcqzBxSBGd4g-nsID6FVuyQpe90NUgdxECDllO6fKqph1pdSHRVrIaZXowopas8HDd4kyGsjnrZ_uH9mNV516K21-8hRHsN-XfZUz2a8ciFOWub9E4tT3vjROjOmezufPXTgDqZCPqM3xYllnH-9yVZiPLFznqJxESM10ksIwvm-KU1hLyKuQD3Y9zOQHkX2iES8Pg5tM1j946ukBW3DhhbjQBK9MkkLFaEXXH6MnIOoFwKkNydN6efkzunTOvGbYH-YErjuw7U_-G0C15vT4eYBYgvK1A82e4kM5GmJgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=GYnilr7qWIy1wAuHwr1cgokIPQbDWJNSb2ZoiG02ZujZFjefgBsqQr1CNEfsitGFGzvnCwZXlM4LZL_psmr4Q9iftIYnO6niG1e20aBvgTDGEg9kMP0QAcl1cb2j11y5ewQHzOFHo4-Rg-YAj8CfK5iqXEf8W6jVwNtSentJphbpnmP1AjQyFogpua5u3-5do7H6jnXbyQA7TmIqTYMyV5v9hU49XjNN6VHWW68OfUpmK2HTs2vkxAdCYV7bmffdyyqIZ6Zt1U_8CDkOhu3cVXe5-FHpCaXRRYAkxVsAU4WbBciNp8_ZjAtrgBuzjemST69f31Qqaklwmu28q0qsyiYX5Vihzg54jyEh8Nrt2u9UoBuyGj3d9IGJJVuZrVtl3hcqzBxSBGd4g-nsID6FVuyQpe90NUgdxECDllO6fKqph1pdSHRVrIaZXowopas8HDd4kyGsjnrZ_uH9mNV516K21-8hRHsN-XfZUz2a8ciFOWub9E4tT3vjROjOmezufPXTgDqZCPqM3xYllnH-9yVZiPLFznqJxESM10ksIwvm-KU1hLyKuQD3Y9zOQHkX2iES8Pg5tM1j946ukBW3DhhbjQBK9MkkLFaEXXH6MnIOoFwKkNydN6efkzunTOvGbYH-YErjuw7U_-G0C15vT4eYBYgvK1A82e4kM5GmJgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWiUbRfhzVcvXnSjUWApPZSWrPavESe19GEhsn1IlxRjQwZ3y5B0qLAEpRP7U95DuXeLKiR5-i-zhJBkQES0OORaoY-UkwelUkLh1e6WyoLGx6ySTEcnNerbouA89TIF_Wpdobp5NGHqsK6Xl-vWNegft3bJsE0DE7pBMi1fQ6y2ixtB0URCBAdrJy4j8smPqmhW4seBmEOofmkIVovzACuO2fkXltnSjeGXvlo31COe9m2SzDQajoQp1NLmygFP_W-2LMrG_qwl8Uurd_dAaGZ8JOCXz4oMMeNDbHiPe1KH0eauUK34fZBlNu9nCN6kTvUX-1GPs496OkjS6AAZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejVJeGjd5qhOmiNAsT0JT0fphGCRJFJKMzutreGgCwHVJWrur_hyRvY7nZe40uqjiIxh0ZENKSQwhBYnPcLgCGIGRzcoqBZgmAPvs8yJ_T1ZV-nmNpS45LoRCasLQ51tge5Q4jNt1rYcfcC_2jdu-X23v46cHfruildjYWbJAzOcy2r_O-u-B0NU-Zes3jcQ7e3477NieIYpP6NxSVIWxsXH_QJYffgeWABp-D4oEYrRRY8wVTawkPslWJF86MxNaS2_UQzkFYajwuqHGzhQcAntDub5zE2c0tf9NwY97_QiqxrhSPt7hmoZpg4JdkeH9CGKcAzh12L_ig4AdRZ4Qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUg4WtPbhi1UPA7Ok77qGnGNOT9oy0n8Pl3igb3VJk6S5p9Rj0BFIC8hCZIJraAxQ-KtS-GA8i8yENkE-2wZAlK6WueJ-mJNsIhn3DhNPX-o9Ys6TRG_62eJc8S4PUFxhTvMmCZZVfM9HxfCjhPGFrdMH4ruRmtPYS_Jmvs3phVbctBb_8h5OFE3ylZ2SAsRmwytuMNxF9gT7RzmV2emGUuCG9hGmGFqkAueZJ_Th3q7cZ8YB3kgPU2N7F4vymDH_Stdr6pYSX6OQYzl20IbH_nLNLRlXPfpKD0tgtWJSHwSk9mSj5s5DLb_1xDyHATOoO66Ut_aR6i7oL5aMttmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGvrdmqBKtYPUNlgZ-z92D2qhdoOFGggVz-FBc4O66-WnAB6uUeFAWQoZVOa8zN-B05FoXp26xNU8fAPPgt0hRaTl7hNa-HYdNZlbsGUslYWkxwHuT2Sb0Ivk7meSe9rGH7I1ChPaArh_OWbQNBg9xeOwxQtc6MrrxD2LikBaeiYCMdi-9VqvBRNgV2Wqy1A92dCnbef3R_hc_MiLS9HpVcz8M5NCsPsicLJ_w2tyDCLTNy41ofo17T_A4gbd_zlqLO4a2-V5KOgKLIUkdmlR4gYyML2QxjYosCBNbR6iXF-FSsDNdvwb0Vo1a7yU7F-CPRZRGoaOihfWda2GA-kJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqEBLSWFTCeOv-eYcWALbxCPh_3hL3t2-_muA1bHN7fqRykcw7U5y4Kkqug79B04Mh-bwo75FrGDEScis-RC_MqRh-7X4DBl8ugAUH9O3P_xIyBN4nqljZqYnr6uLrVgREOwzJv2sYE7vnjPNrYj50-5LEz0OClZvX53g5J30nkhe3qazsSjX4w9p0e_38OjXWmC8NyAOaebbau2InbrPIzqldI_DMnIQuk52WlKx538KC1bCHXbMPs4k1rLcm3IqOVfc2AS7O_axYLn9W1_O4ErayhbRUDYJFW-JZkz8XyF9Aiu3D4xdlEasngBQulSXvCfrZ4udn-jujHC9bef4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cisFzFi1PRLusVvSKFq3RL2kX5Irbbayecrp8Q7pvj4i498lmjZEuHxesd97iruE1tAuYUkymlgKqL8NwlTamjhDt5bu1NEpN4DoRvnGqjg2jiodZH6Sx04ADEcqCutB28K6r3X3UK5KZ_WvO47Ef3Q0bks9ggJOHNp4u8VGv9Fi0wykbKllFduVUJwGlPMC6SwOgfNPmKVjTPNXxGZER8N12RPLAO0Uy9w-PYQUL294nUI_ux_QGW0Q_nPHnpRY29A7Ef9yEZ1i2QVQrB9zfT4M0YA3XbJT_nX49xhVcepIw0FEtfzavdxo3X8By-YRza045qNEL1YF2CYs8-xexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV2O83rVImddzlqIj_mSNt2Y1g1KK9pxQ3jCOHt3BtUO_-yMj427hxdaw1i_hg4JLd5MUEkgRoy25Eej-2dB_f8P7VEmsYp_G2a89oCyyOl8qNxtidrD1m1B9xSvg8GsL0kBV8RGCY4mui_SyVGzgToy2CrK6so0iF2UwGFYds-5xWcDWgU-Mx4KDy_KeVdWQRnGb0otQHsoEq_QrR6YWAI6r_k5iCBOUr4bpYVLyyavReLwmuNHxo6nGS78LQcKk-TqUzoV327bMlAvaF69es2evLcZtKLaOjz7iUNSNVJEI-vSEBllYA13wvL7DyrB7rYOJ9MRFYv5ZoE4yEe6Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=DiBw4d56q-So_dV-ZWRyMSZtVxJV1OTaS0Qqmd6mLDCetTXM8jBYTiXlpNuNFE1BIh0uVmzMtvmivCtUV9lF8NEXJIs_RsJO6zoRDdO0Z4-Ab1Vyc3sQGhV3hJ-sWPA6Hq71TGw7BvqLxpQsJNnXIAfigBww1gIbQ8zvnGU_qo6fb01cMa_E7wTpIRRiMJFLQZB3KFL_6rLKvYXfqLtNCo7-Twc1stFLntNfSQ_uJANlAlBEO_cfG2qGHQbfFOfnuHmuQkgHMsbg_sY_oOfiZK5KCSpfYkGn6_6KSjuwAZIuOig__jUERCoKqHBh5iwkGeoPNzHnlOzTQIozNCn1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=DiBw4d56q-So_dV-ZWRyMSZtVxJV1OTaS0Qqmd6mLDCetTXM8jBYTiXlpNuNFE1BIh0uVmzMtvmivCtUV9lF8NEXJIs_RsJO6zoRDdO0Z4-Ab1Vyc3sQGhV3hJ-sWPA6Hq71TGw7BvqLxpQsJNnXIAfigBww1gIbQ8zvnGU_qo6fb01cMa_E7wTpIRRiMJFLQZB3KFL_6rLKvYXfqLtNCo7-Twc1stFLntNfSQ_uJANlAlBEO_cfG2qGHQbfFOfnuHmuQkgHMsbg_sY_oOfiZK5KCSpfYkGn6_6KSjuwAZIuOig__jUERCoKqHBh5iwkGeoPNzHnlOzTQIozNCn1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBX0koIJOHRD2b4VXErPzD90vOHX8WEWIYAlh6Vi-OkXTR14CryJZob6o49FG2McWYv4wzBydtqFdCwFg9W6BksYXq74dMWRjw1YnuU9mS0E2WwdJ3YEiL69wv8RbRC6wZNICEK3ZD3c7JcgHfK_U9YXsysg9pPYujZMaKAsg1OgHDH-m8TyrYkDSKdNHvQoXUIDqXdcGLFRXyfadJYowySuWWJGs1UjtzuU5Dt5xfywEp_xzFWEXBgZVmB70uBkNYPnmZJDNnQvz7_9TzBmwGuiNAu0mDGMPKGu7J9Gtr6t0LP9R0OJU-a9p5QFOvWRNHrDThJh0Da99CnPe2Qzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjRuomKzRTE6Wv_V_VnHAD2o1HGcBVt9hN25nZYBtDjIpsrMFctf7nWuwAaFHmQkSbtPRJBSmJy_Svmg1u8F6wGXoxzsAbJc4xb5cCwWlxLkG2kQ3mr3sr2CBuPCpAJHZbMcyJWiOSJUG2-oNSE_jhQURE2RXwciIowg3_iPtszQYLemnHc27Rp07REEbm-E90NglQPLZd0lEf02gb6Ai2vMojbqWcw-aEqlbqyU_HSkrPPxxBtrnzU2JjoGjejLolf-1rdjIn3rCdOX4f0SZ0rRdI2XHqq0R3YJovSGBn874jgsOsf_FyG73fQYurhh_Vb3BCs77rXOK3eH-SCzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYfckxn3BHjqC1pX27mVGhqwovF1AZEAifwKEKsRiiPvc4mhgUTkH-Mf0vosfOKJzZO5ThAGCvP1KTgFjmiehjvG4pq4cq2GS5F2EJpACNtpTQ3xHZBcxxChW1RmNFoSj1v-Sb46l6PvyagYD0QHBBVkj_s_F6Djh9O7iAtL2rSBEqLq-vqK0dlE7XVNWCZUrRzi8Oz58dprp9uGsAp9bs1PnBho5RYb-UkWh-nFZmiuMxWv-1fwNzEyIniGh6sq-hPaYEUBHM0x2lOrKe-fS3cBiltmLAQK8Ona025WZ-oLKbBtdKTskkJ2T-lxucvtyjJLzbGhO6EejD50UdKroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=NV_5CvpC8qcBNvGRArrxTTGGfOdlG5pswcMCKw3OHD_3pu7sF9j2Scv8mId9zPqLnTmqeoZbZw6GtSIi5NmR5g7iNcZHuWXn2PHKT1rYzRcVzIpjL2L36p0JIdwufpoPCVcpZLufE9sdEWx255Npgc46U_Zu6WnEqolT-_Uh3HIDvmVlXW7EY45casf0OZGxgswmP7gN7BOPU050sSGPTayQLnimFpZM1BfgTAurRdQDRJTTYTOBpLRosJaIEaJxs1dOgguJiIz7OzPXYOQ8EMaMYgjn45cwR6NA9f6MZIv9MIkvk9rrs0jZq9CGcIycouXO_m03Jv-x4fxK1bVjCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=NV_5CvpC8qcBNvGRArrxTTGGfOdlG5pswcMCKw3OHD_3pu7sF9j2Scv8mId9zPqLnTmqeoZbZw6GtSIi5NmR5g7iNcZHuWXn2PHKT1rYzRcVzIpjL2L36p0JIdwufpoPCVcpZLufE9sdEWx255Npgc46U_Zu6WnEqolT-_Uh3HIDvmVlXW7EY45casf0OZGxgswmP7gN7BOPU050sSGPTayQLnimFpZM1BfgTAurRdQDRJTTYTOBpLRosJaIEaJxs1dOgguJiIz7OzPXYOQ8EMaMYgjn45cwR6NA9f6MZIv9MIkvk9rrs0jZq9CGcIycouXO_m03Jv-x4fxK1bVjCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXp72vUu0jRJa4wliVU8Yk2471-44qUeitcTdv_aARCpjxyqnPR4UsXLcUbFGLfjoCSXTJ8LVzz5zHRYAxTPQ22Er7SzupRkgcpVUj2WQNqxrWpYbSA6lHLNFmUTSw2aD9ZxVeLmgJ8qn5vLaEsHoVNXZtC2YkpuG79CxdSmiQyyzKtP5ZLuEU3a1xPHcaV-mLPbFa4kQTmy6kH9Z61ykTbKoIEds7RbHuf2aBfKm556UM2fcDWqVy27ofnDBy8Stw-fBFIqWvv_6PPOjOui-WTf1oiCUQRygyKTE6aUsp6sLANixaobwYYM4BM6CKCnTLdTJIR-idGJqXEggrCQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8-8Dm5xNkmIZKoYs3vxNGdq0kH5ZbDLr8-M5SiaJyy3IfbIjYoEzDMLqPyiw7j7-HbDtiD51zGsnF1BIIewoZWXNDw24oXpI9E8581GnU4zcMnyujdruwr0RrAxvaooJFQVE05l_ZOVdILdsum885-1uc__vC2KwIKY_u9yqNadXjLz7Jh0o_VSt5SiSmdTWwdSRdIN5W_6_EGEZXIN2dC1fPU47ZzZwrub06c3-RbFPYDhYtm1ntthBJ2M4AaG_O3GKKpymHDLfqB76ko6Ut13McVl94JQIaFe3BEGHvfDVAbLQneFLLgVEMcH6JqdtVoOeNvhpEQYLgyfcDiJfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM5wHNE2dSLZOO1uenqEhfZfyQPt2wKn-L9RhbHtuGXErk_lWyg0FyO4smiOldM5rodPtgLy9ClVM1Rz9PGR2QzcolFLcE_7WBc39VRR6_yEkppVDpD20DJceRlZNb5Y1iwrw9alhx-mxsPc3GkT3K-JzSzBBwA1VjIkpoHXn7JdAaLKqGRH5sA3djGtqhm-9NuBAn37yALedmCp4zC9lG8tUMTMwRbswks4SW5cYdjYsaXfrQbd1HsgK9Cr-edQivbxuDU8jKObqjOFEZ7okS_OkxNshmnSYKLnUVQj8ANUqKvq8v82y-pP9gI_oE-rNMDdxu5oPrmHQcSg9HzC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEPoWgWeyE1n-PXkOXEmVExqqdngv2gRH10UUIRutm7pXcWc1nXU5xnnbn5oF5t5YGcx021zmnBsJ4oDE3Wo-aB0ksBHjoP4YVdK5kZ7Kot5d1JkEXhCtL2KaC0jLq9O_b_eORboxKGH-Pe_54VPL0z_uzgWH9DkMrDCPP4RvwwoJXvxqyZ8ARwBfmA_ct_PqhlERbMDDSNZ8qEVl4n82eSJrDxYpVmVqGURw1bhbWoJPUb9LVXZNTuQoOXbpuFl6G4CNBE8n-B5wiTNXhJoCtWhBTsbypR_Ulm2XxqFtkEXOEYImzu9OP_JtbdmQ9dWdzjb2rIU8pMNpVWwjneEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQGTAgqkzrKnXvYQ_0wzkRp8Zmhp5M5xrtMLlnkKdqsiJCFpnOohjZmzEBhJfFuhXHLnqFmrmP3md3iOcJhmWefnLv4_NM0O2pYRPEuZh7aaS3g5n4XEVF3KYtmH0CYSCj_jdGcFU7bN5I-_1d7o3VwUXdXg1MLtL0_4vzJExW5x0cqMM93myJYxO_0lGqRRU0PZNEobywYuGkteIFZty7oGdIecLbhPh6HZ2gyrKTvQXP95rcSwJ9l0JIKn_nJfcDwHb_FN2lXyP3kaLoGf301MPWSiBAn4DgHwrlNNnjBWLnUR_ggySWD91nXqBaeqdxyGPWbB3_q6qJfFqTjMKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTQ0odWCzUch1WMpnKqa-ZBSeMc6iu7l48YlkRCUEhs7fCtY8xyGdCtyouMNX6TsTvDkvgb4wqxKTkiu50V_Qwl03L6dIkTAmz-WfNy1cmpXVP8prbVz_GCAnGCskPxmmf9o_0KFi4fHuGLg_tPxl4POl9hNoyyueXHbUxKY3CWec5fN_RoLmnh0rhhW6_uejy64kZtdpnXu8LVTk5IC5kofq4a98lSWnqYrXCi2o4oTgVvUFx0fd4iWxU87seGpuA-6LjXgfBeYqqnlLI92RTSvPLH8tBB6AcfA3kHkybdUw32xG0oYY3pq3_-Dp9AFuptlBEgIKXVHDiubC-uWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CShr7WJx1UxrLjxtVqYXwNeGZyczfa5N1Vx1bbizK6MBOuLNDz-yu_godAXF_lKvTCs_nH0NzbKh-Vbe_iIRjw53v7hK7mOR47d8EP4jOG9yKk4a894sciMzsxTTLD5KXs4XZ_-CUgwQxTr-nazWBhp_rNTZ5jesOooqEm04yPvnRq3IG10gYzIxyD2AIheWALlVtdFLLzRfUsBUopcOA76hOB7-luoi8aR3xnf-oafrprEQtflRXwoBGbq8WRT2EmN7Mjq37IYb-bgnM0bVbaFcbAbSPg7WCrL8VIO3YykMgsh6M9sZMsSIW-Y4JU04dy0g2JYlbcya4tjv8poHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us1Hd4U20wSicgumj_4OfA8YsS3j5g2DHQ6Bgmk0HwrLETB-IL58F3kQdGfGbvwDj_d03v6jdYemtf-qzw1kLW33MGtZkIEWCcGic3ONe4ykTB9Tb0-SUeL5KLFHpnvqrDL1f2OXzXzvWw6f0BNgeD7Ne-0QJ1xzJe9qh7IZy04u1Tc3WVjBDBxodMfERQ6K5y4kQKtVP6YrDqmRRi7maTlHVA-BsNSB5F9wBfr1GjIctX7ZcdfJ7qa7MEqRuBXsNjv86NGQdGXOO-rhh8H2tboujdfMnbirp5uKbQUYzbkllhRPUFgrNgo-w4GKs7XECCT_rM_fUFTO-S_-naTTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmQ_du5nCBY4Z60MpCcH_WtB0-UK7OibTZvXK-KETbAPY2PE3KsPgFlw6zXsucAacFiLIe8JeAcN7MDrQFBfx8pmk6lDlKRH_zHxnZS_Uas5fD5zuoC92SLIOe9OfwYH-jrlIqh2wl3kDJtLQ3-gy9Um_FRsOr3zszJEHAEOskOMTeC1dgHNfrvX-SESnnLWiU6vkw9F__g8KWG7pIZBaVG8-M8lxYevf5QYcQM7WgDnFekDP6VK0KXGSjdqKd7Reqnhr_1WZECIQGHn4tB7h2gH5-gDIqZyqtvZvLXopp6DI28sPfmBgrv6KzeSCSjUvYs86lZFfvS4jaX8ycL5vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2wzyl6EuObuKkkFkT2STmapmVbQYd6kHdwkcpyhWcLrTiWz8exKSJOwp4xc1ZzifJb6z_sT8NLbpNHuczQIU-mttMN4OGkc2niOaXKzdB7stv-34plIrVYba5C_KTm-rljbdWDVo6elbQEwUDa7nUlwuiKdnOdwtfOttxa4Re_YwIgggZiR7wVC88Wm_ATeR_V58PG6YUy9uTsM9qhkUwPK1PJJNXbRQPLUETyGkG63mGGV0HGzGr-8fG9qz8x2e0WDY57VV7060TsALiKCwdmwyquk-1tTUwDwSob1TyRzOG7gfuCKeR9lQOnwtWEuoTBV6cN5mwrZMhm9HJldww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmQWpCdMZ2GDnpXZcf3Z60ebcYmrgGyG80Fe7-NeUQh7bpS3H-mWbJx0h2nhoWYT2E6gPEAebjb8m5vpTEyt-MQdVSbGAoy80DVXMeYDjJET_XOnIOPf1Z3q05lHyAFvceOuErzfjwwQhPRDtRDZOr7UN0YXvVOj4r5EnLIwa3pAbcwrqgtaLFrnpwQ2cpDpX4ltdMSUAnaQNYRvaWqJNAOXfR53qiZxnCVbldjxHRBy0Wah46ePPl3_-bGkXWPg8UrSUgHO1ez7u4jsy_-v3AYr3IkOisqoB53qXHtqNTYSgc05nkhn5gRfm0qhX3fzKVzYJNinoCyhPML-wPR7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llMnEt8hP-sviyuY9l8OmR0XShYfLro1bhgxGALE8MP0TfRt47mg58lk-LK5tp0xbeGm9ixtBG87SZWhSXAniqDVBgYE9UtS-P3Z8wZd4xlCB2OjPTNhGYrLBQ-yfdHMM_FmxM1B_z8vCl4c08UBaXNmR6Qy9Qa5Mw1uYZa5z9KE1MujwNIMOf_3e_v-QKWOkmJ41ZVVyIpiGa5QaCYp-GPKhDihJBzKbVkVF1GLI4nBd8XoRRzPW1r6ctNvSKzUC9Xl93HFErBD94aKQ_hh_6azv8Ny3yzBNCbuKk_JmFSTxu0TfnsIUf8ZQtsIdD6fUIyCbRPUhUzrgsSorGwxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZ1L2uhCDeAqXcYSVHLfdST_OL2n-rhb4r3tUVYUXGo0FbehPSYWFrVaiXS49P33-BZKg8uXbvqk3GPnhJsDD9KgV66LzcyiQasQ0V0K_jgMRQRl2Xw-pkLw7f8X8qnnWgxZveOFFAoMbxtb6gPkfKDpMYMKkk3dww7Os7U3TbwCsbuSCIDCQ0atvUPGOUh-yp3h3vjPDYbmI-fvwNIbE5UEACTMhI6jUNPRS2jz-nKozEzKmOl1c8wQsZwPdfK_4c5aaWU8ZXT4fqc1R5wBJhxGBybkW1MPJfSCQw3cK27jyeaWmh45VAGoxDQzjw3Nlij03xJZS7PSoii3nEqiRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQoG7m4DS1vIOErbC_nQ0T1q7u_kb9JpoOOr-OGX4PeprF8yWQgN10Spf4oYa2O1uKsE6Sj91YJ14PTAgXY9TlHfPdEEU51rI8rXxDO5aOCJe5MKbIKnD69Ul3qlky0c29UdF5sUOKh3-TanBbEs7mf9UIEmnVtgnzIt1-b83UX_zdJ4YX_nqFVXslI4biRfiWKVhmNiAbib0R3VUnQ5XXf5JMNqOfJ9goterv1iUIr86rryLWtTezJK2ajYTxWr6z0n4rt7PNqMJpV6JfsCVy4F3pQ-Fys3SOeD9TvVxdYqNDN9k0RQPMIt-eoig0mln2UwNkPOwcEfU8SA4a5hRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrfedJY7bm3d6EsJnhLexgiyDZlnMJZSCRbHQ_80ftiKDiXVMgqVdlbuheucVVQGOlpe67XQxNC1eDznu2V7O2CNoxbcJtaXQ2rAAIsVEsD6PZsWKsadNpMWAiu--pcFRUVtUMnqtr2vuqMtrfKX_HDrnSMFaN59Dpc6DAAVTTQxH67BJX_AaVasOKhiUJTZ3Mb4M6ZjBcClxtOFNHrZd0txNJISN6dNEJ7IQe7B_rs1IPlVDBh8T5FJPyIXTI7fGcTBRJKwi0fTciWDgMY6ByW-NTb18JUie33bC3W5wmRwrVnPsbkwVpbVUtUWZ3N7GKTcMkz1V6Y9I8uks1KgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYAPIucNZsw7lL6biD-1y0FoN0OZCyf-89M1LJjGM9xr2OanTPbrFaDdnJLVsAAP4zJ7hLVjGHRVISBjmqfygc9MA7XuLKE1lg4QfwajcnTJWuctAqRCWOZctrsBRU6aQvmqafpDPHGQOHSCJw0eX4bakoTgtU-u22GuJh9lQH-IGdYb5GRzRBirmeAJV0kUbaPfDDY7kpHeo3dljiNxmeC8APFP_pvfXXSRiKEf70dh-JgjJmrS4AOZrlhblu6OI9XTSXVR9qGB2V0MzoKIYzNFOE4dCAlP7jc5rFS_E3E4mEdFMq7InRhb-bViXxZVRaBJpLvf07pVWQLVDAy43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEUjzIZxMv23AGKHWmqvjuHu2iYi3aDfR845rPFfdrbMjBUBEtuE1Zi6Bg39v0KlEXIOr2zMfnA1hQhT4V-CipjsBFLD5mF1iqL2idxpGCFP8YoMSx0csm-zJkAAd4NPA5FNBZvriPCMNy502GEgy5LIkzoNfQr3n7vmLVszMaE2Q24uv7TMTm0qq0vBFh7aIPnfXqsriq6LIldeaOnvNr922csFhfQdkkdI5lCC66toDBUWxRWybns9-85EJP-24JKgO_TCpj0ySPuzBM26IhYYbwWqKI7WtA4_Sthnmu_89FMRP8W5bifKcHIJYFWFORtNzsO7rpPuMldYgFcQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=Ds3ykMPSm6uZbAiDpL4Xjog3H37uqBggkwUJJO--R5TYVYQHoSNVqseRzcIGECbK3BggiDXTxTxjE1G32udDq3h195i8sF83lCXccaxHulojMHuUo7jsmYmaadazOGfXEs9RtggULaz2BJH_ymvRM9YZVFcByvhjpErfj4mmuCkwwzZf_KadbYMI2CnjHHzUkAvNoVTJeVIO-c8WgpTVXi5l4MoCeoZquM-tPH-2SirK1-ybd3VoTIBqCPAbHXD2-m-e1Ty5ucwlrUbYYA6_0zqD4LerF0R2SW36HcBDdK1ktejp3CMzzbk2Tmf8sdVzWJ8czp1swFnZ66BSU037Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=Ds3ykMPSm6uZbAiDpL4Xjog3H37uqBggkwUJJO--R5TYVYQHoSNVqseRzcIGECbK3BggiDXTxTxjE1G32udDq3h195i8sF83lCXccaxHulojMHuUo7jsmYmaadazOGfXEs9RtggULaz2BJH_ymvRM9YZVFcByvhjpErfj4mmuCkwwzZf_KadbYMI2CnjHHzUkAvNoVTJeVIO-c8WgpTVXi5l4MoCeoZquM-tPH-2SirK1-ybd3VoTIBqCPAbHXD2-m-e1Ty5ucwlrUbYYA6_0zqD4LerF0R2SW36HcBDdK1ktejp3CMzzbk2Tmf8sdVzWJ8czp1swFnZ66BSU037Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsgyu-OT0HTcQ7TUJh1nSXJ5xlj4dYZBuDEhG33Vldomi9OjUJIQVDF1-Vl2cavz1IJqi2CHwd05Ed9fjDxFIosnFdL2l4a4vjLF5HeQi9qDVXlPeHvLvL9dryl4w4U7FtvYpFtWiV2snSUpnAd2EXIt1XUv54tdTP3L1ZxZJdymsr0OWy1mBS-YV_jLpej5DZ6jNixou2k8FduqeqkGSHCFpLxzpL7DWYi-WMUxsNqONSZXPvtQIWE716p9C_4BDpzTy53Aqw2_t5PKfUPjIpqfHYxWmTBkFPvIDqpX9belBL8_q1i5whnKWCxGdvqiFUuozqzf4FG52Icd52reHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgBXaGWtbLDufcxP2UsymWW_zWdM586v38zYRMvECXcuI6oXT6kuThb_RBoaN1diis-oBcCOTjNgKu-MmUiYm0ZbZN8_9rhAn7LGH3cKZICPd8ZbTmCXZOFmgw6Lw_rH6RAPrXt7ZX7DQT8iWPYV4x141kxKa0SBC_9EsKsp7WKZNMMNkOqYs20_LIVIsES8hZrwGkxHTbQF75tRjg0hgvdL5a9LQKlxALQFQQV3yDrcZ0LTXXIwuiVkjxVSsMHqV3gnu4LQG1SUakAYJheBo4Uwg8RJDQKAnTOV7l_zh416mhfflK0aDnaNseXUzt1jlt6dktUl5kBYqjytVqdmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzPEcZK5IJhmUvbYVTDAdg3sbgHrHtFMWlf2hiWRuEAv9kWzo2H9Th7OWIwRVtJyl5aTQOUUuC2WSbwt-ZxWG9SuJqeE8f5NiZHshdeMNtzlMmhEOuHNACDxs3eqokauXyXVBcT6dcYDSah7R4HUx85aV1UdPqb-4UOeHEhfGMUIe6-SiSfUzFLkbi5ESEoH-zRboR3RrIxPmlhJtFGxPmDwUOsajHigJLuI4KskVIwPpZp5OHjoyqncQjdJ7ALkyoQ_oCstCvFHKtM3jNqfxGJgG-exvQFdnXREYLbamvm8fo0ha5Xd9Hv4efPLq7uBCzFomaklcN9kqKw7Fj9J5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTn-lDMxhtrDinXtTvZTzheU79jY1xV64WR7qRZxTmBKb_aomgPH-N1Bu_EYGXXOPhU1xGWfdMTLL8RL5Rq5Ehz-dk9iD5_UDfb8dV7D5twuaH3zX1K76AiGbqQoZDwVhM7MZrS2od9XhQpLfLf0XQY_8tq03w0LbEen7IKnwpDbKLAz3xqyTuPdNV9Knm7TDtMsgposTVwACUKNpfyxWgBlHo_QQdzfRLWD0ZVuv_AfoMqx7YTmQqD9IWwvTh5nspsVb2erTwEOj9fmcVH80yDmqf--mzTVO6P1kfhzefNaJI2nnrLBMEdiYR8rbX-E3DKJqYrPpT79KzdmM8yazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIfcEXAZ8x3r55Z6QkX178GJTh15ooADCONGIzV2121kHvRpa-j3hHuE1ykW3c0AM2y0thGs74jVdWXItagU3tzCkgGy5mrNMaREOMYh08JfkVQyV2t4wiwmLZarLfJ915K_Sovifh2VbxnCyhHs2cJ5d167STaD-xxVbe_kwoPZEnp6VSXsdl_5QN87cRzYOSeKdxPlwL5Y_W3Q0hotWoUYWp4O2uYAE2IawiuT8dT8yB7Kf7LmwiAxTZWePc0hP22cW5td1WG3Fjvd_EXxCHJ-C8PWIjxOkLk7rKAIUJCVkR3SCMUPcgyNbpw-M4IPZHFCGLzLRsxKjhBRzdk2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikDbz4ik1D0HCfuanmEtAV78w1q1OxpY-hvSFN3MpWCtDUqzRRDC9q_-NIMBT7-D2aOPcS_bBu2cmRLmQaX_11fHejNA779IP6onUehTsiEq-xDWnJvgsyFGvDm6lxI6c8t360BJSB21zQQ-5njoQ84v-TkCDuRg5a_XIahYVYsAIdDJLdZB7d_G2svBmBDu-WUfdJZE2cZz8jcHq6C7ChWjFmv8pRa1diskDWSmhtewUO-i4dMxT0HPhsvqniAlsZmhuhw97zurISzQdp0HAhVjTO73Y-TqiXsP_CIwGME-rk_OlelPrA49L0TEOP4azb8ru7MDPvmphkzhoe6uhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT46iYaaH6y6w5BtQM6PfDXBCOcOpKThNMdEbs9P8ep5kIH4sSJ-zW2yM0VK0jKILH_h8gsri87CUyY41Y4P5f1GcRbGMxcUKP0grCA3XqZtxGULFr-vwbn5mTYbw1IuAaqdprSpBTEObNOQxvA2TuopRspu7aoU943VIri-z_9MomgTofsOTrJeSIqXIfCIzH6kfn9KhjYsmcoIjc4k4OkmLEIZP8eev0_R7DSc6E49CUhbKMkfy6AepdkMzHQtm__Mhow9OJQiUspiNpMT9nXmMrKr8Kz86_eCkLEfyVh7Oi3AaKikugL9rbAykgICN2o2cbpztkla0UfAAr9Ur2ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT46iYaaH6y6w5BtQM6PfDXBCOcOpKThNMdEbs9P8ep5kIH4sSJ-zW2yM0VK0jKILH_h8gsri87CUyY41Y4P5f1GcRbGMxcUKP0grCA3XqZtxGULFr-vwbn5mTYbw1IuAaqdprSpBTEObNOQxvA2TuopRspu7aoU943VIri-z_9MomgTofsOTrJeSIqXIfCIzH6kfn9KhjYsmcoIjc4k4OkmLEIZP8eev0_R7DSc6E49CUhbKMkfy6AepdkMzHQtm__Mhow9OJQiUspiNpMT9nXmMrKr8Kz86_eCkLEfyVh7Oi3AaKikugL9rbAykgICN2o2cbpztkla0UfAAr9Ur2ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwYY4JY7MUUiV5UgpxX4gJEuIpspdSCoR6rrKxbKXLf1PzANle897R4qBNy1MjwGMPVS_4P7ehBG-uCOxeYw02ab-2DFLQdH7NBn21z3ZsFYL3FkNrAMOMEP8p6q8oCCFdQ5CbitkT9GxYeYw6gBCIsHwYu8-VnJvLlwnXe4XggWJOQ-zHPcgUbnclFfQvBjPTFkZF3ZEwjNmEoX-C2nPzT6aiq3GgdtfgtzQ_ybiluTFNm5eoqQUZiNIp5YjedNEKk3qbd6vhEcei8LLvet8QOd7o9wgK-GM9o0dxBBGR5ctF6nDwMW1_3fB427REtuDsFm_zfDnXIlUsnO-Zwt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4rk0WX9Zh11zND2cE3bTR89nJbAIzIkkAuvjySrvJ9oAakA0pjg4NjryOMAOs4MJOw2BSyElneHUvO-Eos-zmyB4F-WergI0WB9p2tNI44NMCLnPkZFXyOwbDcssXvE-3K2H-FnwdELfnCDWk9Pdw_qKwkDXx15fTxUBuFWuU2JU_ZPeFdbZBkRxgLIIo2IElj4qa9k4_odoget-FzOpb3lOKgKQmSoCe_ZH3Bv6SMtQ3mP1F924ufD78S_EauPXEejOa8WZylZ26WsXUfsN2LdUgLytvImtz1cLrSY-B5WWbnne8P3EWR4v3ZR_W5HDwuFqMx9UCev5o5BKS69WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdADC9vBdzL-gJK1mBy61Uh_qfP1tY6fRm_AB_Sq05q13FsyOVvmv_4FSkd8mTIbk65SY2i1ay91-I6PkLI3Xc85FYKcJaGOixI_7rOgBZKycj-lCrd5QB7b6X3BN_BCovNzuxa86q0ZWXUNJqfPy_h0HwhkwkCmIZUFsw6Z0UKsJUlGD8LjVIK_I0UAdGYa31NmX1k2fEV04XNqB9T-55MMeefZOVqn0d8V7LQgz6payzBmYIQQp3fiJ25VPyuGWGupCz2mhWsOtSpYke0v0olzt9RwxxsT0vFlL8WWBNfLf8ynJdYXM9Aoyvszd2gTc3lYGQVmh6MzuZqeqMp-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=OgaW79I8oSagJEon6fwXhncHPHbWnAjIaNnLs2eKZnHPHFwSW4lzBisxjktqMGF_nQb8GgjtZb6pDgdmVHY4uMFa06-oF8DPgrlkxvBRweBvPgJw6tZnyhL6JO88ab-ViSKVugyYTqQvMBX51cMXkHT5WvNRj-jJZHLWt-jkHUYxspsd2nIjlFtnmODowq-6CD5Ek_ZFPX_glBw97xRfDBk9iSrt8qSx6IbUa5Fe-8w8lU97MuEGgYA4MGlFsOYFUr_uTE0G5_ApfQmI-noqjJnaJ8fXUsWKOzM53HWXgqo_mGLj0xY6BHU9hqH0clWsj79-VON4rnk6gVi5LJkLdCw5R-enYK8hlIGdChSOmA9jKnrB8YmbcQ-Xx3JWF21YtzpUSXC06yxKD4TSl2k3wD_Gc4_YTO4rTVXdUKbM1sOdbHLvROBWk60xBmXql0WYgadzO7sCYR1okyFD4fqoJwpU--aAe7QSkhfbloJgjqSsvxf63YthxXMpVY5RqpqlkBP0p9Bi45hD1JbWV9LaGz07awIBFHbv4Qk_u-sq26qouzqFmEMWSDHmTICegYSwedINtGv5DSlt8roZIHc7gJprN2UOiUiIi_-n-ueZ6PKp-6pKU9EJJjZAI8uoy8qhUQGulOHo74c_vIWPcHoLPIiRJiPGUQkVvBfrCVl1vRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=OgaW79I8oSagJEon6fwXhncHPHbWnAjIaNnLs2eKZnHPHFwSW4lzBisxjktqMGF_nQb8GgjtZb6pDgdmVHY4uMFa06-oF8DPgrlkxvBRweBvPgJw6tZnyhL6JO88ab-ViSKVugyYTqQvMBX51cMXkHT5WvNRj-jJZHLWt-jkHUYxspsd2nIjlFtnmODowq-6CD5Ek_ZFPX_glBw97xRfDBk9iSrt8qSx6IbUa5Fe-8w8lU97MuEGgYA4MGlFsOYFUr_uTE0G5_ApfQmI-noqjJnaJ8fXUsWKOzM53HWXgqo_mGLj0xY6BHU9hqH0clWsj79-VON4rnk6gVi5LJkLdCw5R-enYK8hlIGdChSOmA9jKnrB8YmbcQ-Xx3JWF21YtzpUSXC06yxKD4TSl2k3wD_Gc4_YTO4rTVXdUKbM1sOdbHLvROBWk60xBmXql0WYgadzO7sCYR1okyFD4fqoJwpU--aAe7QSkhfbloJgjqSsvxf63YthxXMpVY5RqpqlkBP0p9Bi45hD1JbWV9LaGz07awIBFHbv4Qk_u-sq26qouzqFmEMWSDHmTICegYSwedINtGv5DSlt8roZIHc7gJprN2UOiUiIi_-n-ueZ6PKp-6pKU9EJJjZAI8uoy8qhUQGulOHo74c_vIWPcHoLPIiRJiPGUQkVvBfrCVl1vRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9ZBTQxUk33T0AGH2orLSh8VXnfJbT41nZDJuCgfvkTtK2W6Aw3yXxflkJfDxbtP4ImVq_JmFdbncpuggjXDT3aefads5Lvtp_0YiQd32Xt12ARQkrPtmyigT_N-ts46XPIdNZ4ufHxsmJeG61WJ2xY7OCIHodcAIAiWl9bciJ3AFGB9dGUiDJkKXkp7TepMlkbsuwgQhV1_97ROJ_yHqgQnGStM0tgMErsCfJ_ySPcz4akr1scauU4jF6KZpacgfFnDyuoE1zQszxvWtc6sfWQA_p0Bz8Lr720RzvNodS4820E6XpAicXHtIhiYiWnuZtlYZtc0MLfEIo9I9e0gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxFh8slfVSjWAyKmVXcl_klXT-2-A7vnK4fwWsOQKWvyYWUfX3mA45pVI6vb4eHIanUHktH4upx_l1tE0FYEZUOsup_QOCpENXW7yeGdpgcZKtS-2-ekRrWkH8VnsjQfExuSOmbUlTvleZs9-4zEvD3A_3AaRSeoryANHQRpBaJVC4UuWqoNfblmyDF9BnhoNS-aWj9HJfbD0EUZcLj0rTzuYwqCGS6pH5NgBOLARcWKBPt58iaxZDw-K8f4-t6cSl1VaEYew05IY9YD50xtv0QZkmDPDKs-RJ3eJRLJVkTXckfkBt45ENZENKGy21Lv52jWnHK9lRbQjJX_Z4Cnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=k06-ESsm8Ggvl76NIRgYiLrmDcEsbwtIQtEojpngM1mC3EQ0NDyCGvmBel7w-GCQOKY51-j27Ap_OqcZABDn7oU72kaz-tZLCCl7Bhykw0ZC0APxdIjCcxNMOEd9X_aV7-jYs9nzD45mhl0dYK0IPltxnndnKdMyAhk2s9m9XuBHR0prCoabXK4sr_to-0GV0mhc39HoKD5usNLGoSZZroI8vwbm7jON1376BbxuBou3tVo1XRUaj1pAojJk3OeIGcjCRROVCOAKqszmnPfUeMLdc8sEs9JkzJ3KTZ4W_n7UlrYz4Ea60JMQgzqwN3QIbdhS0vcYJ8GklXK4flvg2RINWiHUVK2NdfT4XQxC-PmbSxYCaAMWZF04VwunzKBtCAb_RHedBbJrUhAY9wNMtz6hTb3N-3gl6K6Vqvqog9zpcyA3DysY953bDr3DSogHemMg94cHhHCjRmi24PKi0GUgpGAhlFXbKNR8uRvFlAxBZCKmgyLXYv4d-UDP5jTfO9UGVVYFhNlh5XQlQSJ1sDDc6X5YvzprETbEXHoWBpo_W6YAfkftxPhPIENtMu6hgCpKIDM1le-uWJ13ybjI6WOi-BB70oNV6hfg2K7_ZGz1PmCqpttJDSUwUmyXioT8A-iTprLnDv5IRJoDdJ-r997EcX8nYX7nlX_QAtZ_DfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=k06-ESsm8Ggvl76NIRgYiLrmDcEsbwtIQtEojpngM1mC3EQ0NDyCGvmBel7w-GCQOKY51-j27Ap_OqcZABDn7oU72kaz-tZLCCl7Bhykw0ZC0APxdIjCcxNMOEd9X_aV7-jYs9nzD45mhl0dYK0IPltxnndnKdMyAhk2s9m9XuBHR0prCoabXK4sr_to-0GV0mhc39HoKD5usNLGoSZZroI8vwbm7jON1376BbxuBou3tVo1XRUaj1pAojJk3OeIGcjCRROVCOAKqszmnPfUeMLdc8sEs9JkzJ3KTZ4W_n7UlrYz4Ea60JMQgzqwN3QIbdhS0vcYJ8GklXK4flvg2RINWiHUVK2NdfT4XQxC-PmbSxYCaAMWZF04VwunzKBtCAb_RHedBbJrUhAY9wNMtz6hTb3N-3gl6K6Vqvqog9zpcyA3DysY953bDr3DSogHemMg94cHhHCjRmi24PKi0GUgpGAhlFXbKNR8uRvFlAxBZCKmgyLXYv4d-UDP5jTfO9UGVVYFhNlh5XQlQSJ1sDDc6X5YvzprETbEXHoWBpo_W6YAfkftxPhPIENtMu6hgCpKIDM1le-uWJ13ybjI6WOi-BB70oNV6hfg2K7_ZGz1PmCqpttJDSUwUmyXioT8A-iTprLnDv5IRJoDdJ-r997EcX8nYX7nlX_QAtZ_DfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
