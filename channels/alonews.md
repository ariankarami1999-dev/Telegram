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
<img src="https://cdn4.telesco.pe/file/kF-7X85kdkktmzHvQFspvR44Z0S0k0TotNH7CzwYqCxATVyV4Kwb6fOpXRsUBP_XW7CAtAGbhAiwSPsO3nGoI3_UsT1qPd7bVfY3YI8zaIX1oZWW-_jli1gWptMDMANW7mDWIkT6mxDuKM4PHX3hVXIQMhhNenrG5WBl0bH05-IuF85aHfHpjY2_0imotGtiafLzPoGFHNImvuPK78DkNyD799dTdZkw0Hx4_oSe0ZHdOtRmnQeViFPol6omDlZYwqsUkNslR1Wv7uOOkh46EgREbLEuorSvS0SiPxBdGqugvg9g8A-x09ZfgcmcJS_QKEP9MW7RBdYUMU5S7pap5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 982K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 13:59:38</div>
<hr>

<div class="tg-post" id="msg-140190">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUDtcYTIaIyT4hSYtxf1uAhdIWkJNqvDMf6TjAuJkn7kvoXhsQ9tmoLkmAtF25aY0LodrhBabOI5ucfh6lBrAEWMcoQ8EYFXckzDn54Vr1Zh2_vmoLe36j3eljQmC84qyCokWc195uWybyq1Av1snlGStdfeYUST6l_jXocYeUvW2iW7zjJOg--aQzSOcCoFTmSOXRKyw2YzLjJoYe_IZZRjcXTNH-mnmWT1IGEvPlcBo7-wwQFQXcv7rkJhriwUWcF6rt4Yvsiq6-1jR3q6Z2QTfgqxTyMB8WvNtcRgf9xXnQyVprtYWPJou5PHQJ9kHLa9DwzpaBGCj_KsKtHu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران عوارض ۷٪ را بر تمام کشتی‌های تجاری عبوری از تنگه هرمز اعلام کرده است
‏
🔴
این امر برای ایران ۳۸۵ میلیون دلار خالص روزانه یا بیش از ۱۰۰ میلیارد دلار خالص سالانه با حجم ترافیک پیش از جنگ ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/140190" target="_blank">📅 13:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140189">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0700f7505f.mp4?token=ps9dMUUUzfyfvVEnuIXdU8XIsgeVEBbkPKivXu952PnognNUUqxseD_Nziolkx0_4HHX3wDnvPw-Y2vkLbkY2LcxLG8b6RJMAgHqIYgiV49Fk1YMpSwOwYijL4JYc-JOSOKoGcW7n7QhHAbUqtMZQYJLesSXbaDsJcsCUxej1xj5Ky2w6G5mCHURuN0CKibjhg0SeExZriSvsiL2DhGbRb8tnxbs41PMysVccGS7i_k9jBA5bfkw8zkSO2r6Ee2kiODI0aKDxLKhJw5_Pz3ACoj0sftzJnAsIbSfacmKcHrcSN9b_cCZeF_9iglAyLWuX3rQ6yhT91GQITLqiZyGgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0700f7505f.mp4?token=ps9dMUUUzfyfvVEnuIXdU8XIsgeVEBbkPKivXu952PnognNUUqxseD_Nziolkx0_4HHX3wDnvPw-Y2vkLbkY2LcxLG8b6RJMAgHqIYgiV49Fk1YMpSwOwYijL4JYc-JOSOKoGcW7n7QhHAbUqtMZQYJLesSXbaDsJcsCUxej1xj5Ky2w6G5mCHURuN0CKibjhg0SeExZriSvsiL2DhGbRb8tnxbs41PMysVccGS7i_k9jBA5bfkw8zkSO2r6Ee2kiODI0aKDxLKhJw5_Pz3ACoj0sftzJnAsIbSfacmKcHrcSN9b_cCZeF_9iglAyLWuX3rQ6yhT91GQITLqiZyGgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا هنوز باور دارید که نوعی تغییر رژیم در ایران ممکن است؟
🔴
مایک پمپئو وزیر خارجه اسبق آمریکا: صد در صد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/140189" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140188">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
۸۱ سال پیش در چنین روزی ایالات متحده آمریکا با استفاده از سلاح اتمی به هیروشیما حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/140188" target="_blank">📅 13:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140187">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=i0FS6JYGk3Gf6wgHGknSkYa_2iYdE80zaWCPppG0HIAug0OYiwqT76EKeAPEZNGk8rCIzD3UV4dLhP2PGWaudUAzimAe-8bZk0nPOa_HToBsIvxf-dX0_JxYiC6-REsMY10lUpB37BFpUMwu7z1a3A6fNS4uM8TI_Cd6oPuUpBcPKUFXNve0MLjh8DUqityc0h228E94wpCGuoqyTZOJ9o7jRVprV20ouJQRSxObzEKMg9onAH5x4PKU1PoAb5UglSfcWuY3B4WRIrZtvLWJCPJRJ66k2GAmuGaEy2TTMLeGBjmbRv06C_bpP_gDbPT-_iF8YzY3bni0LOUrUeIRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=i0FS6JYGk3Gf6wgHGknSkYa_2iYdE80zaWCPppG0HIAug0OYiwqT76EKeAPEZNGk8rCIzD3UV4dLhP2PGWaudUAzimAe-8bZk0nPOa_HToBsIvxf-dX0_JxYiC6-REsMY10lUpB37BFpUMwu7z1a3A6fNS4uM8TI_Cd6oPuUpBcPKUFXNve0MLjh8DUqityc0h228E94wpCGuoqyTZOJ9o7jRVprV20ouJQRSxObzEKMg9onAH5x4PKU1PoAb5UglSfcWuY3B4WRIrZtvLWJCPJRJ66k2GAmuGaEy2TTMLeGBjmbRv06C_bpP_gDbPT-_iF8YzY3bni0LOUrUeIRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / انصارالله یمن 8 فروند موشک بالستیک به سمت اردوگاه های لشکر یکم عربستان پرتاب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/140187" target="_blank">📅 13:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140186">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=UwfKlT3yO_xcSmbT6MbPp2j_Lf4snrJ9xsvaiXt2MLwDvDbniebFiRqZS4NcuROXILdJgzldRbJQGlySvM8KMzYbqXnkKHq6jJOzEKVP7qs_O9uHoik2TlFpSmhSCRKwG43RR3iJvAMMc_nWabss1WOoqJIdTPjtwXqnKpKU90ZrQDO4zgc8-i_JmFpl5CAQ7cDb4cWMQEvMjXaa8vcZLANC-5HOBabZR032lEs6rB2VOwyNcav7lar4tvwTGZeeW6ZSBapSKrQrBwyW3lkUTGDq-wb3V5GDmMuYVzg62s0MjTQBGQCDYwaaYphnV1orpusRVuQsY5XmXDpBbZK4iACTVXBz_kooOEcVrlfovANnJB96le-mc0iUWIu6F7Yrad5K7tEOQ0hNvvpo0BeppgQBp1TkxWuT8yCOhwFGJ2bsTiBpTtREjWk34D0qRuaN2yLWsRcdia6OUKkBez6Pheh7-_e8ePeigeVyG7x1Ou7J2J5sBhQhxN8yMry-KOMpkdt7XWJoLZd_LokNEEgOrNSuejrqq1J3sssyZT2Jnb5Hxa_LsgN0eFzo5tPo9MCfD-H1C_o7XCpGA3AEsW9qules2crh_0lKKWZmZf6CeY9bAw2ptQwtlpCojV8QOcHQYsrOtYGWHCT4UCs6M4GmKGo5mj7QJ_Vc4oI0mz3X9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=UwfKlT3yO_xcSmbT6MbPp2j_Lf4snrJ9xsvaiXt2MLwDvDbniebFiRqZS4NcuROXILdJgzldRbJQGlySvM8KMzYbqXnkKHq6jJOzEKVP7qs_O9uHoik2TlFpSmhSCRKwG43RR3iJvAMMc_nWabss1WOoqJIdTPjtwXqnKpKU90ZrQDO4zgc8-i_JmFpl5CAQ7cDb4cWMQEvMjXaa8vcZLANC-5HOBabZR032lEs6rB2VOwyNcav7lar4tvwTGZeeW6ZSBapSKrQrBwyW3lkUTGDq-wb3V5GDmMuYVzg62s0MjTQBGQCDYwaaYphnV1orpusRVuQsY5XmXDpBbZK4iACTVXBz_kooOEcVrlfovANnJB96le-mc0iUWIu6F7Yrad5K7tEOQ0hNvvpo0BeppgQBp1TkxWuT8yCOhwFGJ2bsTiBpTtREjWk34D0qRuaN2yLWsRcdia6OUKkBez6Pheh7-_e8ePeigeVyG7x1Ou7J2J5sBhQhxN8yMry-KOMpkdt7XWJoLZd_LokNEEgOrNSuejrqq1J3sssyZT2Jnb5Hxa_LsgN0eFzo5tPo9MCfD-H1C_o7XCpGA3AEsW9qules2crh_0lKKWZmZf6CeY9bAw2ptQwtlpCojV8QOcHQYsrOtYGWHCT4UCs6M4GmKGo5mj7QJ_Vc4oI0mz3X9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه در حال آموزش نیروهای جدید از کره شمالی است احتمالاً به منظور آماده‌سازی برای عملیات  در اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140186" target="_blank">📅 13:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140185">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عملیات انهدام مهمات عمل نکرده در برخی از شهرستان‌های آذربایجان‌غربی اجرا می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/140185" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140184">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/INlf0bcjb3wprP61qq1-ylY3i5Mw8-itwR9Bav_14FGe9NeULpJn1PEChMOdU4G720eYA5fNssPV5e7XNk2ET_RaVCTUeuUrEok3gOI-4QpY3cuW3ZFtKSD3XKK-aQzM4f29KbN7bUJg0AIR-lpbmTs0r7A6bIsEKWmo4EqPXH0eFFtnHXKCMEwYiR6hAthOQaeYKtAalDz-UAY7-yGmHiTjxPcCesVU7RVYBS6gojkkwaAnXZK0UP1boVgZRoAfkEdBktotyEzs6QTdOzGtsEULE5XGNpcuVLYvcAeudeouHmXxRDbYDZ8Aqk3cuT2yw5Fd9khE1g3pTNaAbIa5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اسرائیل با سم‌پاشی هوایی، با استفاده از ماده گلایفوسیت بخش‌هایی از اراضی کشاورزی سوریه را هدف قرار داده است
‏
🔴
آزمایش خاک در حدود ۲۰ روستا، آلودگی و غیرقابل‌کشت شدن این اراضی را نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/140184" target="_blank">📅 13:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ccbf767f0.mp4?token=Fj_0P2dyWQCWGQFMXKqAe4SglWDFKKAcuxXGxDUKA0L6AkE5YrbiM59kcPHyXA1jPvI9_-4SSGlhRPdSsqxTidp2nLfgJ2-nE1J7urdLoLDXx_DZ62cFQsdySCmtiu-ZI7fazG_jf1PAOpb6gPnqk5qpHpO5Jg2WKC4idTandjGRr39kemAO-5efYIbHVi-hPEwFUH_edhEggwIJ1hFkdGEj69xIt1E3iu7V1_3DXCDTdvbGGQDpo75XmMfvXUI-NF_YPiQageB74VwVOW2_zo6pqVzWviXLWXvP4j77etfnQR4v1tiDCvvOkY0vT4g4x5-QtKKn1QiMKZJxdxmfSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ccbf767f0.mp4?token=Fj_0P2dyWQCWGQFMXKqAe4SglWDFKKAcuxXGxDUKA0L6AkE5YrbiM59kcPHyXA1jPvI9_-4SSGlhRPdSsqxTidp2nLfgJ2-nE1J7urdLoLDXx_DZ62cFQsdySCmtiu-ZI7fazG_jf1PAOpb6gPnqk5qpHpO5Jg2WKC4idTandjGRr39kemAO-5efYIbHVi-hPEwFUH_edhEggwIJ1hFkdGEj69xIt1E3iu7V1_3DXCDTdvbGGQDpo75XmMfvXUI-NF_YPiQageB74VwVOW2_zo6pqVzWviXLWXvP4j77etfnQR4v1tiDCvvOkY0vT4g4x5-QtKKn1QiMKZJxdxmfSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل تصویری دقیق از زیرساخت‌های حزب‌الله که در چند ماه گذشته هدف قرار گرفته‌اند، منتشر کرد. عملیات‌های انجام شده توسط فرماندهی شمالی ارتش اسرائیل، مراکز فرماندهی، پایگاه‌های عملیاتی، پرتابگرها، ایستگاه‌های مشاهده، زیرساخت‌های زیرزمینی و مقادیر زیادی سلاح حزب‌الله را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/140183" target="_blank">📅 13:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140182">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346341c053.mp4?token=klSTXUHyZcx9Jzbuh5lM4_qU1HLH6iCvD-3rbSHhEMxwivBDOoswRtu1SjXOaIq5r5Iqr9EAc_Tao6qXYtcWmcfYHezHdxOp0QbcVPL0jNCaudHluisGB6FnDFhV8Q6Ps83OHTPCNeVjFXcBBSTOVqgGKzuHSEndoipHV8r2sSp1yFUpylBhQB5XhZnotnS1I6ZJgUJLhn8fIhRthjuFUf4zInsSHUK9SQDvxUOVlO2deYGncMlEUngZOVNpa2NO3bSrneUYQP0xOS4GeGBc0cxTtYDS_58ulIkfBONV_vvLXBpv0-TpUAMK4dnOAHbqeGGmJSQbCUpoS0Vmi8gr7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346341c053.mp4?token=klSTXUHyZcx9Jzbuh5lM4_qU1HLH6iCvD-3rbSHhEMxwivBDOoswRtu1SjXOaIq5r5Iqr9EAc_Tao6qXYtcWmcfYHezHdxOp0QbcVPL0jNCaudHluisGB6FnDFhV8Q6Ps83OHTPCNeVjFXcBBSTOVqgGKzuHSEndoipHV8r2sSp1yFUpylBhQB5XhZnotnS1I6ZJgUJLhn8fIhRthjuFUf4zInsSHUK9SQDvxUOVlO2deYGncMlEUngZOVNpa2NO3bSrneUYQP0xOS4GeGBc0cxTtYDS_58ulIkfBONV_vvLXBpv0-TpUAMK4dnOAHbqeGGmJSQbCUpoS0Vmi8gr7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز صبح یک انفجار توسط ارتش اسرائیل شهر زواتر الشرقیه را در منطقه امنیتی جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/140182" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دور سوم مذاکرات بین لبنان و اسرائیل در شهر رم، ایتالیا، آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/140181" target="_blank">📅 12:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140180">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8b9829e0.mp4?token=fqAOz3sfd-dJLK6wSNMy2c-xUYjy_vyDQ_7kOKTU4nzkhLF_J_ie_IldqXd-MvHKeFT1dUrkwxLC-kGHH27g5zTXkirCasc3ymLIA2MbNF0xuhI80NlgZ3ETTL9KPUn7lCxsYGSEBuKzy65Su_rtQCXTGlXfk6yqrZbhuY1Fm9f0_MbEfaxw9mMF311Ad5fMhrUbPwwYlFeDE0ckzJeACvnuHokTFBWOYHrE57fPUjZNiXTRZGco-o1Oq-aYkSTq3oV5qy_M5frRiE1TvcEK4LHbbR9VQxpddST0W4lf_6k4016yQfP0RKJB9yCOQFzMESsI1NpqMtXkAVlUKRTZHl7K6HWKMd8GrUfgT2GGEIhXom-OjaOomNTFHQJMaS2g0qD-pA8YMGwTzj3MRXob5iI4KyCrWN5v8yM7hfhkXHQJW2Y3uWpJcI3A2pRjtlIUI6sBGGSVRIpxa4qyvT_W3ecA3zAZmZrvGb4zy-jQMYO3HZUTWeCilyQ994uJ8_atLq7BwhhIxTjorB1ZZJZDjxytsO2goRw7OYHftZ5mwr3cLIQQ_s0rl1BsQgpbC-cCd-26HI_jI08b9EsunyC0OGYNLU8axjkTNQrBaF9XDUg1C-Gy3Au94ciq8YgqSXRX-26odIOanz1vYIdeyZk1PSpdGWHeLoUy9IG8DrjJztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8b9829e0.mp4?token=fqAOz3sfd-dJLK6wSNMy2c-xUYjy_vyDQ_7kOKTU4nzkhLF_J_ie_IldqXd-MvHKeFT1dUrkwxLC-kGHH27g5zTXkirCasc3ymLIA2MbNF0xuhI80NlgZ3ETTL9KPUn7lCxsYGSEBuKzy65Su_rtQCXTGlXfk6yqrZbhuY1Fm9f0_MbEfaxw9mMF311Ad5fMhrUbPwwYlFeDE0ckzJeACvnuHokTFBWOYHrE57fPUjZNiXTRZGco-o1Oq-aYkSTq3oV5qy_M5frRiE1TvcEK4LHbbR9VQxpddST0W4lf_6k4016yQfP0RKJB9yCOQFzMESsI1NpqMtXkAVlUKRTZHl7K6HWKMd8GrUfgT2GGEIhXom-OjaOomNTFHQJMaS2g0qD-pA8YMGwTzj3MRXob5iI4KyCrWN5v8yM7hfhkXHQJW2Y3uWpJcI3A2pRjtlIUI6sBGGSVRIpxa4qyvT_W3ecA3zAZmZrvGb4zy-jQMYO3HZUTWeCilyQ994uJ8_atLq7BwhhIxTjorB1ZZJZDjxytsO2goRw7OYHftZ5mwr3cLIQQ_s0rl1BsQgpbC-cCd-26HI_jI08b9EsunyC0OGYNLU8axjkTNQrBaF9XDUg1C-Gy3Au94ciq8YgqSXRX-26odIOanz1vYIdeyZk1PSpdGWHeLoUy9IG8DrjJztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل توانیر: ۲۷ میلیارد تومان، پاداش گزارش ماینر پرداخت کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140180" target="_blank">📅 12:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140179">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
داده‌های حمل‌ و نقل دریایی: تردد از طریق تنگه‌های هرمز و باب‌المندب، نسبت به روز قبل به طور چشم‌گیری کاهش یافته
🔴
تنها دو کشتی از تنگه هرمز عبور کرده‌اند و یک کشتی از باب‌المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/140179" target="_blank">📅 12:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140178">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رسانه های آمریکایی: اسرائیل در آستانه انجام یک عملیات بی‌سابقه در لبنان پس از حادثه تلخ بود، اما آمریکا در لحظه آخر مانع شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140178" target="_blank">📅 12:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140177">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وال‌استریت ژورنال: امارات خواستار تشدید فشار نظامی آمریکا علیه ایران شد
🔴
روزنامه وال‌استریت ژورنال در گزارشی نوشت: مقام‌های اماراتی در گفت‌وگوهای خصوصی با دولت دونالد ترامپ، خواستار اقدام نظامی شدیدتر علیه ایران شده‌اند. بر اساس این گزارش، برخی مقام‌های اماراتی معتقد بودند فشار بیشتر آمریکا، از جمله کنترل تنگه هرمز و بررسی گزینه عملیات زمینی، می‌تواند تهران را به مصالحه وادار کند.
🔴
این گزارش همچنین از اختلاف دیدگاه میان کشورهای منطقه خبر داده و نوشته است در حالی که برخی کشورها از جمله عربستان، قطر و دیگر میانجی‌ها بر کاهش تنش و ادامه مسیر دیپلماسی تأکید داشته‌اند، امارات رویکرد سخت‌گیرانه‌تری در قبال ایران داشته است.
🔴
مقام‌های اماراتی یا دولت آمریکا درباره جزئیات این گزارش اظهارنظر رسمی گسترده‌ای ارائه نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140177" target="_blank">📅 12:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140176">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
یک منبع بلندپایه به العربیه: اعلام توافق برای بازگشایی دوباره تنگه هرمز ممکن است طی چند روز آینده انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/140176" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140175">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ-cDvALCp9sFkyU7DI7kzcJou3ytswGJMnJkMysyUHX8UMfrfqvhXpR5-k4pyD1Z7SiE39WoODh4qNwzhLGpKA6aj5AhjMjf7-7WSU4H-snWPYvixePQsRJQYbDltQ1JR9nLFmG1ZXT9hSzW0h3cIxEAaRZsh0oS4NnEIoA4fYMbxbf7dJ7XBcoTyNPcEyRL9m7HIH__n3xy4EpohM7JcR1u2zvwZifv1UtW4Tzhp7tTdsVX47emykUW9nFog8i7VILxdL7i2OpEulFjlcg86e-d4RrvK-_bYVMSxn9IPKNjj0X1TBHLsKMjC9GtpDU_hMEsUxqej6J_Y6b9lB0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز: عبدال‌السید، نامزد چپ‌گرای سنا امریکا ، بیش از ۱۱۵ هزار دلار از اعضای سازمانی دریافت کرده که ظاهراً با حماس مرتبط است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/140175" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140174">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سردار ابن‌الرضا: فناوری بومی ایران، برتر از هر سامانه وارداتی در منطقه است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/140174" target="_blank">📅 12:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140173">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
منبعی بلندپایه به خبرگزاری الحدث:
وزیر امور خارجه پاکستان از همتای ایرانی خود برای سفر به اسلام‌آباد دعوت کرده است.
🔴
سفر عراقچی به اسلام‌آباد برای روزهای آینده پیش‌بینی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140173" target="_blank">📅 12:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140172">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بر اساس گزارش واشنگتن پست، رئیس‌جمهور ترامپ در کمپ دیوید، پیت هگست، وزیر دفاع آمریکا، را به دلیل کمبود مهمات که گزینه‌های نظامی ایالات متحده در قبال ایران را تحت تأثیر قرار داده است، مورد بازخواست قرار داد. کمبود شدید موشک‌های رهگیر، ارتش آمریکا را وادار کرده است تاکتیک‌های خود را تغییر دهد و تهدیدهای ورودی را نادیده بگیرد، مگر اینکه ارزیابی شود مستقیماً به سمت یک هدف مشخص در حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140172" target="_blank">📅 12:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140171">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یک منبع بلندپایه به العربیه: اعلام توافق برای بازگشایی دوباره تنگه هرمز ممکن است طی چند روز آینده انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/140171" target="_blank">📅 12:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140170">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi-X1q0N4bUpl0XhVyknBfXEbpycr9-8udTBsssjWZnVGMjGjOonTc4XPm_KqdoKBSxngmEFrXcIdgqo6Xgu620izR20_xifKXh3VKaSWXF2Ga8PxgxSxy8OFzOq0I1E9xkvZYzUsTA3ORbJCBASIFtQnhPkDF5OC92XnWBRZ0LyetNouAczfKniKHjalAENKiHXOihSHw1WiuYvHN1JSLVDIlPlGuSONyK0OPIs0nUHwl4aikI-2jM3-7u4a73Q1iunySR72qYlFSWs3H5C6XPCHLkSvCzfJ6tu_74Rwsf9DaKRi8S6l0UQCyjtT_9BZvMwNs8QaSBE865tbQJKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن پالیسی: کاهش تنش میان عربستان و امارات می‌تواند به کشورهای خلیج فارس برای هماهنگی بیشتر در برابر تهدیدهای ایران کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140170" target="_blank">📅 12:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140169">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رویترز: ترامپ بار دیگر از روند گفت‌ وگوها با ایران تصویری مثبت ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/140169" target="_blank">📅 12:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140168">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دولت ژاپن : کره شمالی یه موشک بالستیک مشکوک رو شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140168" target="_blank">📅 12:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140167">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJsa1Y0LArFQZ4n7hiouxX3PROobOa-JSuoK96Vo-BLc1Qwby11meMAo-IPI4hAInXgz3csy8rPfgpoEnVexFIJ7129Gc3EMRuXsYX6Tjlfte9M54xo_f9g6GV-H7fIbEUQXO2QnB-eda5WwdRaTSpVoriPp1X_IGXtRkO9xX07ejANwD1bRV4YmvOjJ46XDojlgxwV1BzyiOsMYLE9eJzXCNuNG9m1Qosg2Qfy20_-WRnxEZ7lZ3NMYEU6wWD4qjjR9MkJVBkFNGPMyLQQT3cNbVnSkj9Ln0WihhC9Uo8QA4WHVKU6er8d8bhO9K3rjnYP447KI0cCtFU992CVAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت ژاپن : کره شمالی یه موشک بالستیک مشکوک رو شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140167" target="_blank">📅 12:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140166">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ارتش اسرائیل: ۱۵ شهروند اسرائیلی وارد خاک لبنان شدند؛ نتانیاهو فرستاده ویژه خود را راهی واشنگتن کرد
🔴
ارتش اسرائیل اعلام کرد حدود ۱۵ شهروند اسرائیلی روز گذشته به منطقه غجر رفته، به حصار مرزی آسیب زده و از مرز عبور کرده و وارد خاک لبنان شده‌اند. به گفته ارتش، نیروهای ارتش و پلیس مرزی وارد عمل شدند و این افراد را شناسایی و به اسرائیل بازگرداندند.
🔴
همچنین روزنامه هاآرتص به نقل از منابع آگاه گزارش داد که بنیامین نتانیاهو، ران درمر، وزیر امور راهبردی اسرائیل، را به واشنگتن اعزام کرده تا از شدت تنش‌ها با دولت آمریکا بر سر جنگ غزه بکاهد. این گزارش تاکنون از سوی دفتر نخست‌وزیر اسرائیل به‌طور رسمی تأیید یا تکذیب نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140166" target="_blank">📅 11:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140165">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سپاه: احتمال شنیده شدن صدای انفجار ناشی از عملیات فنی در پاکدشت تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140165" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140164">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIGJ05C15ya09ldeZNsCJmLrsp6mM187IdHtJU4Drl9eDbxXFsJ7-NkJuk-aIjV6iqNHNS0DvAtysEr0FTecUcv7QoZNYyZ0VMXaJLTFKQz__hRO8EfYhh8doUAuukCTtWvYrJHpZZndqYsD4BTq6u5_nlOJ1cmMXmOQCkeCwKNYfuUl-ySMVEOWQuQwM3N8POE4lJ_ZYsFlO35Q_o6W45OO2lnwdcEnatE7hB-egc_KyPoy_cfyR694qIOOvVD33AXtMgnaD81EbjoCRDLKPSAm4uTu_qcPCJQopqSF0Vi4D3tDLEi2AqG986QAd-j04MJVaAFzcxHNpXBOmSAdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک موشک از یمن به سمت کشتی‌های سعودی در دریای سرخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140164" target="_blank">📅 11:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140163">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4iGj1u4PvSQfa7lGTp1HHZbYYP7vP6RIJ2MDwqc7H4rFIVs72u7hGVmY-MOaJLBC8YnRZKQXg61zBsStzeu-fdPqE0THiMVMl1b-YZWguX6I-xBl5R_wkvVEyVO--XhUlD_RFcVN6GjXeGHaQftFnTlkNdUhrulN1-6VInR3bOqRMjJThAE20N2az5Uapexc0Wo-HXgrFG2n6lsqolevlnp1DTjgW1POnMQlOwbYU4gJFI2hOzBmkVrixv0x6muMxmOtJp56A3MovknaOhShzwnAghuJbE2JzAZ-Ti8Rpx7BU8XAtZTLSp13ygighpr1ByYWjox_G3KNlXJPw027A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان جهانی هواشناسی به‌تازگی اعلام کرده احتمال شکل‌گیری پدیدۀ النینو در تابستان ۲۰۲۶ حدود ۸۰ درصد است و این احتمال تا پاییز و زمستان به بیش از ۹۰ درصد می‌رسد.
🔴
براساس پیش‌بینی‌های موجود، تمام ماه‌های پاییز از بارش بالاتر از نرمال برخوردار خواهند بود، اما اوج این بارش‌ها در ماه اکتبر (۱۰ مهر تا ۱۰ آبان) متمرکز شده است.
🔴
در این بازۀ زمانی، انتظار می‌رود سامانه‌های بارشی متعددی وارد کشور شوند و بخش‌های وسیعی از ایران، به‌ویژه نیمه شمالی، غربی و مناطق زاگرس را تحت تأثیر قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140163" target="_blank">📅 11:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140162">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سوال : در مورد ایران، چه چیزی باعث می‌شه فکر کنید که این بار اوضاع متفاوتره؟
🔴
ترامپ‌ : نمی‌شه با قاطعیت گفت، شاید این بار اوضاع فرق داشته باشه، شاید هم نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140162" target="_blank">📅 11:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140161">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me2TngbZtBQKsh2_dGTZv0bLLrWX4ilaO9aTtqWes70yfzk5MH-hfVZvh8Kf1cZtKzMv9Lzm9fQow8Q53LGkjiHuscO4umG0VVVm1LpbH60pu1tdqD5kKYBQQwF2Vd9beI-Hp2GEnoxf98Ya49Q745Lth6gg1u2rbM0WmNwhXHlC6xhW-aHbXnH5l8o4OQg9Oe7xhKxIuNBq8g9a3hbW0nwoHDBgdnFMuki2V6PXaKx_N9tsDTbt4Y77VWD1m_y1mG6TYOTENXcOice7VfKZDLK5x4ZLrBfaD10owfigq1klzFnIUReXDHmyJUFZBuik9oDsPhkEdYxRRNMWK13_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حادثه امنیتی در نزدیکی سواحل عمان رخ داد.
🔴
یک نفتکش تو ۹ مایل دریایی جنوب‌شرق کومزار عمان، موقع عبور از تنگه، صدای دو انفجار شنیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140161" target="_blank">📅 11:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140160">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e77000cff5.mp4?token=ivHmDxWY-6gez23YXRR6YvIHBB_Cnp4EiKb07b6JEyGbhz3yIipXUoADd8DzJyVoG_KQpK3spnvyDWdZdalzNTJ75yLYZ65lIkLFmnI8W9jzCbtgZPjmaUSLCiyrPDmgBAQufJ_YLu8jWRYq4eyr-FVA3491nbfsPbMOVaGXbb8QmuGCI-cpfjzW1Gb0id-wDMXfpDIuvjL-XlBwUXOIw6pzrKsSD0SCYivWIXL0dfw718p5DFUGQzrjKewJD5XIt-rsji1p-znOuwC1Gzt6NM4BVt8_0yuuA85GNICkGgt6BENxdhuHEOx6IaRbrGkSrtIywx9qftZYLPWKn5UOGH9gYuihGsoM0yAuALa9f7qZ1iaLjJkL5DRfooPXJo8nJvHFnaDzFUgJQXBGyhzrttNJI10_1qn34wd4AsDvdFlw6mUgJkCrfBJke6PGmLcG5x3syl5lpbfiuKokd5cT6K7HIrPQimoPnmA4bxS_ZTjEvJ1Z6Vt2QBOMi9ssqcgwad_9PtTeAeoNDzmDyOP6n_PN1z2yczkx8zbEVwbnxtteUZdNYkCK2rIw95Bm4woQkgMwZoap2fZayFQgBdDtG1TWYrfVHAufEjqmOtTKqOf5WYwIPiH6cAK5XsM14Xb0jddKj95Nzh-HK8niFUzN-9HDgUCLdaZbeN5YHcLUPHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e77000cff5.mp4?token=ivHmDxWY-6gez23YXRR6YvIHBB_Cnp4EiKb07b6JEyGbhz3yIipXUoADd8DzJyVoG_KQpK3spnvyDWdZdalzNTJ75yLYZ65lIkLFmnI8W9jzCbtgZPjmaUSLCiyrPDmgBAQufJ_YLu8jWRYq4eyr-FVA3491nbfsPbMOVaGXbb8QmuGCI-cpfjzW1Gb0id-wDMXfpDIuvjL-XlBwUXOIw6pzrKsSD0SCYivWIXL0dfw718p5DFUGQzrjKewJD5XIt-rsji1p-znOuwC1Gzt6NM4BVt8_0yuuA85GNICkGgt6BENxdhuHEOx6IaRbrGkSrtIywx9qftZYLPWKn5UOGH9gYuihGsoM0yAuALa9f7qZ1iaLjJkL5DRfooPXJo8nJvHFnaDzFUgJQXBGyhzrttNJI10_1qn34wd4AsDvdFlw6mUgJkCrfBJke6PGmLcG5x3syl5lpbfiuKokd5cT6K7HIrPQimoPnmA4bxS_ZTjEvJ1Z6Vt2QBOMi9ssqcgwad_9PtTeAeoNDzmDyOP6n_PN1z2yczkx8zbEVwbnxtteUZdNYkCK2rIw95Bm4woQkgMwZoap2fZayFQgBdDtG1TWYrfVHAufEjqmOtTKqOf5WYwIPiH6cAK5XsM14Xb0jddKj95Nzh-HK8niFUzN-9HDgUCLdaZbeN5YHcLUPHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور قالیباف: اقلیت پر سر و صدا حیا کند! یک جا ترمز خود را بکشید و از نظر اکثریت و قوه عاقله نظام تمکین کنید
🔴
سیستم امنیتی به آنها خواهد گفت که مستندانشان در مورد کودتا را ارائه کنند
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140160" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140159">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سخنگوی ارتش: ارتش در آمادگی کامل قرار دارد و با نوسازی سامانه‌های آسیب‌دیده، ورود تجهیزات جدید و تکیه بر توان داخلی، بی‌وقفه مسیر افزایش آمادگی عملیاتی را دنبال می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140159" target="_blank">📅 11:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140158">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شرکت هواپیمایی "ویز ایر" اعلام کرد که به دلیل افزایش هزینه‌های سوخت هواپیماها، ناشی از جنگ در ایران، متحمل زیان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140158" target="_blank">📅 10:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140157">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWqbHG9uQxUFHFYFvIlD5zuFeVPJU8xCuWkyaDycjEJFHZ3NhS_xB2vx1rVHL_Y0M2hnah3O3LWIE91emeawaq_7c52CKVYv2EFNOuWvXtERmV9TwxgIzal987tHJ9wMCi__55GhDaR1n3hWSR37qvOEAOwNg403C_IZD4igj6G9u42x60yIxMmFPpE-_ZAkart6vZGLT_W03h_DLxiGm4vJo9OkEQ6N6GmXsCAj-QR4Y0RlLjUW_DUTFVzktp_qs-Y7cbDqvyKtVI56ow1V7gLqPPKO31RgEsMbMK3vy7yxVBvNFgm_gwqt44bkVrF_darC4nYKlrMPzPoPdO55zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر هوایی جدید از حجم ویرانی در روستای مجدل زون در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140157" target="_blank">📅 10:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140153">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان:
سلطنت عمان نقش مهمی در حل‌وفصل مسئله تنگه هرمز ایفا کرده است.
🔴
ما همچنان با سایر کشورها در مورد بحران خاورمیانه و وضعیت در هرمز در حال رایزنی هستیم.
🔴
تلاشهای دیپلماتیک ما برای دستیابی به راه‌حلی جامع و پایدار دربارهٔ تنگهٔ هرمز ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140153" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روسیه: ۲ کشتی حامل محموله‌های نظامی را در دریای سیاه هدف گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140152" target="_blank">📅 10:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سازمان وظیفه عمومی فراجا در اطلاعیه ای ضمن تکذیب شایعات فضای مجازی با عنوان "معافیت سربازان فراری" اعلام کرد: آن دسته از کارکنان وظیفه که به هردلیل خدمت سربازی خود را به اتمام نرسانده‌اند، می بایست وضعیت سربازی خود را از طریق یگان خدمتی تعیین تکلیف کنند و هیچ نوع معافیت جدیدی برای آنان در نظرگرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140151" target="_blank">📅 10:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رویترز: پس از آنکه حوثی‌ها اعلام کردند یک نفتکش سعودی را هدف قرار داده‌اند، تردد کشتی‌ها در آب‌های خلیج فارس کاهش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140150" target="_blank">📅 10:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaU5vg6nk7REpv6PuY2omHOnci_2qmgBgppSpgIqm1DpuH9FkilfoBFuZVuc-p48kVeljiYE0Gix6a1xlpqXZhV0EAQXyvuYrWADVbWy8OUPOZzK0bxFWWUV-Ddi-qSW8G_RWs0B7JkyGQ0X5MMlyWB67_E4yj0sCQdZrUzkk1ejsq1YWDKYbUR_ctdnZCRmHGOjYtlrY36bxpsDQAsV0LgmU89KSUnh8j-po8sprrwqMjjeeXC5gtQDn0e4NG3Aj2HznEyFgH4DTRUPj_zy6SVzdO0onp9dASVNi2zPerVmMIgqbIQTc63WpcvanReoVWNmbt_-PrxtkhnckJ3gCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشست چهارجانبه وزرای خارجه عربستان، پاکستان، مصر و ترکیه در امان برای بررسی تحولات منطقه‌ای و امنیت گذرگاه‌های آبی برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140149" target="_blank">📅 10:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ونس درباره ایران :  ایران هرگز به سلاح هسته‌ای دست نخواهد یافت و ایالات متحده نیز در موقعیت قدرتمندتری قرار خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140148" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43713c064d.mp4?token=qMQT5dqBgB3a1bEL8eFZp5TO6DjK5KK8-LruVZrfDBG6gbo1qnGyf4MkWq0mdmnQGdRusG4OsA9Y1yAsYpxpYbkgqFwBvTBxMFije83V8hqDtFAtPaoz1G43NEfnmKWrUbpn464--mZSG1L9DlLeyxJM3KJ0lYr0TLt-7FFkD4ty53JtVlNF-A55DBjzp_-WvNF_41s2xLszN5C36nd9CREUXjXi85NoaYZGy1UwE8x0GZPnC4enr2ZZvEB5IhYkdkD2V_r5ynqq4sJHvpmco7-v2qKVRu3mFSFGuB-_D4aNN4GadwNq8Y-cZo_RGChpMYNeolkqme_oYzgY9j-gz6KEybaRrfcsSFsqJB8tSLAdjDa2rxM9xFNQPMomTAQdZb3hmzWxOAZNabKl3NJXte-4Oy4ZPsyvzQkcc61dbQo3ZQzjEPWjNkPn2_MimmaD0HWLhb1zRsjjTbH7z6o9wNBten-e3RUu3KKV6DvRpZ0gpFdcvMlyPnYIkruZzh7Z95BpPrWbztYiUKr8QG-965zX6bIHLRP7u4q6yb8SjYyGku2iSwXFyPsWkt6HS9ACrBxrz1ZXBc02g7Polp_1nyslBkhT-7htvWYGelP-FvkKs8wWKTr8McDIO4shRHSaPfARMT7jGMJw9Ms2LrJSfV5duvUE2hcbCw9ZnYgKY5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43713c064d.mp4?token=qMQT5dqBgB3a1bEL8eFZp5TO6DjK5KK8-LruVZrfDBG6gbo1qnGyf4MkWq0mdmnQGdRusG4OsA9Y1yAsYpxpYbkgqFwBvTBxMFije83V8hqDtFAtPaoz1G43NEfnmKWrUbpn464--mZSG1L9DlLeyxJM3KJ0lYr0TLt-7FFkD4ty53JtVlNF-A55DBjzp_-WvNF_41s2xLszN5C36nd9CREUXjXi85NoaYZGy1UwE8x0GZPnC4enr2ZZvEB5IhYkdkD2V_r5ynqq4sJHvpmco7-v2qKVRu3mFSFGuB-_D4aNN4GadwNq8Y-cZo_RGChpMYNeolkqme_oYzgY9j-gz6KEybaRrfcsSFsqJB8tSLAdjDa2rxM9xFNQPMomTAQdZb3hmzWxOAZNabKl3NJXte-4Oy4ZPsyvzQkcc61dbQo3ZQzjEPWjNkPn2_MimmaD0HWLhb1zRsjjTbH7z6o9wNBten-e3RUu3KKV6DvRpZ0gpFdcvMlyPnYIkruZzh7Z95BpPrWbztYiUKr8QG-965zX6bIHLRP7u4q6yb8SjYyGku2iSwXFyPsWkt6HS9ACrBxrz1ZXBc02g7Polp_1nyslBkhT-7htvWYGelP-FvkKs8wWKTr8McDIO4shRHSaPfARMT7jGMJw9Ms2LrJSfV5duvUE2hcbCw9ZnYgKY5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل
:
نتانیاهو با من برخورد تقابلی نداشت. گفت‌وگویی صریح و در عین حال دوستانه داشتیم.
🔴
همان‌طور که بارها گفته‌ام، اسرائیل شریک بسیار خوبی برای ما و یکی از متحدان ایالات متحده است؛ درست مانند فرانسه، بریتانیا یا دیگر متحدان آمریکا. طبیعی است که گاهی میان متحدان اختلاف‌نظر وجود داشته باشد.
🔴
فکر می‌کنم رسانه‌های آمریکایی بیش از حد مجذوب این موضوع شده‌اند. واقعیت این است که وظیفه من، پیشبرد منافع هیچ کشوری جز ایالات متحده آمریکا نیست.بنابراین، هرجا منافع ما با اسرائیل همسو باشد، درباره نحوه تحقق اهداف مشترک گفت‌وگو می‌کنیم. هرجا هم دیدگاه من با نظر نخست‌وزیر اسرائیل متفاوت باشد، درباره آن صریح و بی‌پرده صحبت می‌کنیم.
🔴
من این دیدار را گفت‌وگویی دوستانه، اما مستقیم توصیف می‌کنم. احساس نکردم که با من برخورد تقابلی شده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140147" target="_blank">📅 09:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
هاآرتص: نتانیاهو زمین سوخته‌ای را به جا گذاشته و اسرائیل نیاز به التیام دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140146" target="_blank">📅 09:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
معاون رئیس‌جمهور آمریکا در مصاحبه با شبکۀ «فاکس‌نیوز» مدعی شد که از تمام ابزارها شامل نظامی، اقتصادی و دیپلماتیک برای رسیدن به راهکاری برای ایران استفاده می‌کنند.
🔴
ونس: ایرانی‌ها مذاکره‌کنندگان سرسختی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140145" target="_blank">📅 09:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxPc_SNC0IUxVXknU7Q88GpdYjeMwh0E0oGlfD7z2RzsKqxUqKIJ1Qrl_rjkKFaBVJ6BA8bjFejN9L1ZGLeAM_9eSayzuppfSK6B4W8IGgfs0XqxketZg2CPX-_oWcB2hSBxuYRRbGJ1ZZtrVdkHiPoo2xEEYV62mYedzOKNDRXrqKUPMEG7pc2vTt6HUnHQ1RryoD8bGrDQsFo-xkV3oLCviXtFyTkowrrjHtvDlIz480Z94XRcPYZiUvy2Od2lrCRHUOMdpCIHxrGy_mwFsWHL0suJ2Xoka77exf-aAtRTWPOYAksiJP_Wt6Po8Anv_e4A70AiGoszq0e1lMlACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
نفت آمریکا (WTI): ۷۴.۷۵ دلار
🔴
نفت برنت (معیار قیمت جهانی): ۷۹.۰۹ دلار
🔴
نفت امارات: ۷۷.۹۴ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140144" target="_blank">📅 09:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140143">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سپاه تهران اعلام کرد: صدای انفجار احتمالی در پاکدشت بین ساعات ۹ تا ۱۲ امروز، ناشی از انهدام مهمات عمل‌نکرده است و جای نگرانی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/140143" target="_blank">📅 09:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a86cac7b.mp4?token=HYFUS4gcYr_TMFiDiYlKGpJsNVfUS-ulMCGAomE6ymmpd7ORDmJahuZRYvGO2ox0ocef4mrvt9BSsjE5shcII7FQjmyppxrdYtCd0257242y6OrHqj5RZ9nnC34iua1DBijqOQ2WYj5qIXPks_J9HDd261ib6_UXCd9C69ujf9JEK7OEKMwJ6vXmlH68P2IE1AqCfPiEb0h4iFjUe1iI12jWDqvtR8QCYm4CcB5smJee4ookhAY8rKLPaq5Gu5gYcgRz_6RvI9Ctm1U0T4IIIpe7_z7X58H70R6CdrD_KtUcT9HQ38N2zjKgCdA4XEpaG5bc3gZzx1ABUuvs2Ei5wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a86cac7b.mp4?token=HYFUS4gcYr_TMFiDiYlKGpJsNVfUS-ulMCGAomE6ymmpd7ORDmJahuZRYvGO2ox0ocef4mrvt9BSsjE5shcII7FQjmyppxrdYtCd0257242y6OrHqj5RZ9nnC34iua1DBijqOQ2WYj5qIXPks_J9HDd261ib6_UXCd9C69ujf9JEK7OEKMwJ6vXmlH68P2IE1AqCfPiEb0h4iFjUe1iI12jWDqvtR8QCYm4CcB5smJee4ookhAY8rKLPaq5Gu5gYcgRz_6RvI9Ctm1U0T4IIIpe7_z7X58H70R6CdrD_KtUcT9HQ38N2zjKgCdA4XEpaG5bc3gZzx1ABUuvs2Ei5wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور آمریکا در مصاحبه با شبکۀ «فاکس‌نیوز» مدعی شد که از تمام ابزارها شامل نظامی، اقتصادی و دیپلماتیک برای رسیدن به راهکاری برای ایران استفاده می‌کنند.
🔴
ونس: ایرانی‌ها مذاکره‌کنندگان سرسختی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140142" target="_blank">📅 09:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
الجزیره: قیمت نفت در پی امیدها به توافق ایران و آمریکا در مورد تنگه هرمز، کاهش یافت
🔴
بهای معاملات آتی نفت خام برنت با ۳۷ سنت کاهش، به ۷۹ دلار و ۸ سنت در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140141" target="_blank">📅 09:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4caa2d703.mp4?token=nkCq-72MlzKv-XRq3O5rOTwk3SiWdOTfziU_RVGwI_3RGV1EaJD13SgIrHf8uY34kk8p7ChfbaV5PzZvV55oRy07_q71aDi4_6IJZQW6DG7ipo1BfR2ank-3i--jNOYazNd9VqJTxHlSOwCt4X1om0hdbAfTLNSUcdJwUFHH0hdFy8LFnCiNJouSAjuo-lLnS2CV-Jw-I5aIO4DOgUFTeflniFANuDbS6xTVsA9QpQL1lmS9pubSRv452C08pTKtw6BNsSpNe2qTlSYSXqba90HhsP2etTE1lVvTgHth6g_lKBPPANhUTW8sNHw0OBsooaJKuQ_QWXjNhkS84GK8LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4caa2d703.mp4?token=nkCq-72MlzKv-XRq3O5rOTwk3SiWdOTfziU_RVGwI_3RGV1EaJD13SgIrHf8uY34kk8p7ChfbaV5PzZvV55oRy07_q71aDi4_6IJZQW6DG7ipo1BfR2ank-3i--jNOYazNd9VqJTxHlSOwCt4X1om0hdbAfTLNSUcdJwUFHH0hdFy8LFnCiNJouSAjuo-lLnS2CV-Jw-I5aIO4DOgUFTeflniFANuDbS6xTVsA9QpQL1lmS9pubSRv452C08pTKtw6BNsSpNe2qTlSYSXqba90HhsP2etTE1lVvTgHth6g_lKBPPANhUTW8sNHw0OBsooaJKuQ_QWXjNhkS84GK8LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد اینکه اجازه نداد بچه روی استیج بیفته رو زمین: نخواستم مثل بایدن بشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140140" target="_blank">📅 09:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc78d3794b.mp4?token=Obz4V7hmBwHPB_BIcJw18-8LEmYE_s9KGud-nOlM3V6UWtnKIM6Rz9AQEntmNyix8NUW1vXZHd73P3H7GrGJufpZLMM7VagrfEpJZmOSU_ULw1ZRF1MdsWrA8NVZP3h3r49o8IH-p423uvSeOjcuNtbAHoO3nOpfpeUNzEEhpw5qaZQUxPU4r_TGnmYPGjYikfPRjvRIPGId8e6ZuQPxkJo95PU-TzS--x3Hr9M8RWvoVunTZ4JnndTaAQieWTnN1inhOSCow9jDeCkvA6zTUMtAP-fgQv9Peg_GvFBN3_vC7nBF7e2LeV9EjtdXxH15-A6LRP06eg8hkzYOPB06wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc78d3794b.mp4?token=Obz4V7hmBwHPB_BIcJw18-8LEmYE_s9KGud-nOlM3V6UWtnKIM6Rz9AQEntmNyix8NUW1vXZHd73P3H7GrGJufpZLMM7VagrfEpJZmOSU_ULw1ZRF1MdsWrA8NVZP3h3r49o8IH-p423uvSeOjcuNtbAHoO3nOpfpeUNzEEhpw5qaZQUxPU4r_TGnmYPGjYikfPRjvRIPGId8e6ZuQPxkJo95PU-TzS--x3Hr9M8RWvoVunTZ4JnndTaAQieWTnN1inhOSCow9jDeCkvA6zTUMtAP-fgQv9Peg_GvFBN3_vC7nBF7e2LeV9EjtdXxH15-A6LRP06eg8hkzYOPB06wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی عجیب در آمریکا: عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140139" target="_blank">📅 09:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سازمان UKMTO از وقوع حادثه برای یک نفتکش در ۹ مایلی جنوب شرق کمزار عمان خبر داد.
🔴
ناخدای نفتکش گزارش داده هنگام عبور از تنگه هرمز صدای دو انفجار شنیده شده، اما کشتی و خدمه در امنیت کامل هستند و هیچ آسیب زیست‌محیطی رخ نداده است. از شناورها خواسته شده با احتیاط عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/140138" target="_blank">📅 09:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga1hXNiloeOaqL4SV1BkPwcbSadM3IEKVdnPgsGf4VoVsUkPZuBG4NzagRclynIg1QMphC954Kym4L9J_vJhLtnbPVCIckXzH4u3qC5FwFOHXkZE8b_C4ad1g6858omN-lLBuWE3o0g3Tf2LmYKRuYUAyo_U44-mWs4pHS01bUOatpoBiXQ9sKSj6aXssGHfkenM-3r7ai7rw7y5laE3_lEtX-B1KYbwn4ROXbP38OApSzVz1NyAEmuL1HBlm7zt3kmAQVlfev8vz66qOH3zLsFpBjqaCjW_GQqqmq_i0NvG7QIiZLOXBgM0WIMStd8NEW2Gd9xGYZolLqZm94N2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: مهمات فراوانی داریم؛افشا گران خیانت کرده‌اند
🔴
در ایالات متحده، ذخایر عظیمی از "مهمات" وجود دارد، به ویژه از برخی از انواع آنها. علاوه بر این، حجم زیادی از این مهمات در داخل ایالات متحده تولید و در صورت نیاز، عرضه می‌شود.
🔴
شرکت‌های دفاعی در حال ساخت بزرگترین تعداد کارخانه و تولیدگاه در تاریخ کشور ما هستند. افرادی که این اظهارات خیانت‌آمیز را فاش کردند، تحت تعقیب هستند.
🔴
آن‌ها به مجازات‌های طولانی مدت در زندان محکوم خواهند شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/140137" target="_blank">📅 09:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc78d3794b.mp4?token=eAGSVZ4m2DGUDWLFO3JXTf5GDJudSdaq0N91Bzg-eEqKsbTRQdAlrV5nCkrKh6s2PwO6ylZ6twMb7nA7_-1Ut1kJTGbId_-elJxY4Gyx4ROJ5XcmEkmEO20UuueJAdQTA2ZdiW8miOT0hVUIFjP1w52EnprJDf0POT7gi8vRyLhayAC2lb6pEdKwvzkhUuTdn7wK6TuDXq-bB3bP-I22rmBS7HYrhjvgbtvI1lGDOnprEZHFcAFAKAqesM-CgoluTrBYHnRw8T-ybCWDyOBtNIWmBw7oo3a2t4h_6jPT54hi8NTb2FNh6OXimFNvjJ2mfbaW6-yVDptioONivodrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc78d3794b.mp4?token=eAGSVZ4m2DGUDWLFO3JXTf5GDJudSdaq0N91Bzg-eEqKsbTRQdAlrV5nCkrKh6s2PwO6ylZ6twMb7nA7_-1Ut1kJTGbId_-elJxY4Gyx4ROJ5XcmEkmEO20UuueJAdQTA2ZdiW8miOT0hVUIFjP1w52EnprJDf0POT7gi8vRyLhayAC2lb6pEdKwvzkhUuTdn7wK6TuDXq-bB3bP-I22rmBS7HYrhjvgbtvI1lGDOnprEZHFcAFAKAqesM-CgoluTrBYHnRw8T-ybCWDyOBtNIWmBw7oo3a2t4h_6jPT54hi8NTb2FNh6OXimFNvjJ2mfbaW6-yVDptioONivodrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی عجیب در آمریکا، همین الان عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/140136" target="_blank">📅 02:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140133">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw_Oy9X1IPnDBz-HqMahggaywA8eTubvt9P6wb_Z2r-DTTdZaSCR_ycIPlsts8iDepIZw-b3pjd0UwHnLZStmyq-IZ1zRSrmP5IoIQxPAUyPoTuBz-CpsGTVlBSDPk2tSND3-5pPp7rfPKug8-PVumw3hYkcixDgMQQOUUeDDbTWnDMRyEBsspH4PYRoLpzPs1_hYTiKUiAcUoG2emtcRlc7FV5KCkbBO7NuPBmceFqyRDyUxOkM4Ubyrynrdpc9cF5Z36LdY3wX3uEGDE_5k3ZADcQleb5ZGSjzhhy1PN1zdxeK1dyF52yhqRoKyp_P01--1SL3I8ooL7564pqtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ad3d54a7.mp4?token=YfO_ufmSzvWxTKiYzIc-XpswNxMMsXj-VCynI-h1Ayonuoz7e5O8JvFwp7BK_aQE6f3vP49Y3Uk_fYkd8q5gc-Gjl5OZ0Rrtzrh9tGEwebs2KyC3h6cA5uvjDBTuBtxKzA03vCLOXpXRE3hxrSteDglWaShFfFiiFDLm8H35hCK8VFd5hIRW1PfMcM4uClf_tYQzn5COd-TyEKqJXqJOfh1Q_WBypqQ8ljmRkVYFHpItl5JRnOn3hs3KA0ip9rUoaOLm5YJ96Y3xrn3GViV9fPeporitbeYaQ6qNLNx1h7jBRDXUc8ouU8OgGM7aStMzIjbpBw697Me1g_w07n8V8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ad3d54a7.mp4?token=YfO_ufmSzvWxTKiYzIc-XpswNxMMsXj-VCynI-h1Ayonuoz7e5O8JvFwp7BK_aQE6f3vP49Y3Uk_fYkd8q5gc-Gjl5OZ0Rrtzrh9tGEwebs2KyC3h6cA5uvjDBTuBtxKzA03vCLOXpXRE3hxrSteDglWaShFfFiiFDLm8H35hCK8VFd5hIRW1PfMcM4uClf_tYQzn5COd-TyEKqJXqJOfh1Q_WBypqQ8ljmRkVYFHpItl5JRnOn3hs3KA0ip9rUoaOLm5YJ96Y3xrn3GViV9fPeporitbeYaQ6qNLNx1h7jBRDXUc8ouU8OgGM7aStMzIjbpBw697Me1g_w07n8V8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/140133" target="_blank">📅 02:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140132">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: یک فرصت دیگر به ایران دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/140132" target="_blank">📅 02:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140131">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: ضمناً داریم همین کار را در جمهوری اسلامی دوست‌داشتنی ایران هم انجام می‌دهیم.
🔴
داریم انجامش می‌دهیم.
قرار نیست از آنجا گورمان را گم کنیم.
قرار نیست از آنجا گورمان را گم کنیم.
🔴
ترجیح می‌دهم توافق کنیم، چون نمی‌خواهم مردم را بکشم.
من نمی‌خواهم مردم را بکشم.
🔴
برای بزرگ‌ترین حمله در میان تمام حملات آماده شده بودیم. و طی چند ماه گذشته ضربات بسیار سختی به آن‌ها زده‌ایم.
🔴
ما کاملاً برای بزرگ‌ترین حمله از زمان جنگ جهانی دوم آماده بودیم.
و آن‌ها با من تماس گرفتند و گفتند:
«لطفاً این کار را نکنید. بیایید مذاکره کنیم.»
🔴
و بعد انکارش می‌کنند.
گفتند: «ما هرگز چنین چیزی نگفتیم.»
می‌دانید چیست؟
رسانه‌های جعلی می‌دانند که آن‌ها این حرف را زدند.
🔴
اما داریم مذاکره می‌کنیم. ببینیم چه می‌شود. اما آن‌ها برای ما احترام قائل‌اند.
برای ما احترام قائل‌اند.
🔴
۴۷ سال گذشته، اما در واقع ۵۰ سال بوده، چون سه سال است که می‌گویند ۴۷ سال. ۵۰ سال بوده است.
🔴
و هیچ رئیس‌جمهور دیگری کاری را که باید خیلی وقت پیش انجام می‌شد، انجام نداده است.
🔴
چون ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
نمی‌تواند داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/140131" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140130">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b2de1aaf.mp4?token=T6LOCEIgIqkWQOvdYcPSV5gO-G7dE5a1eFv0fUhqTD08kbyDPAORiCb7_QIGvgy0rdOEcyDikLMUeEaxfQ1bC0TExT1zIlkdZEPeQSJgEen6w8cbTH9sjvtHzX-52HTr7kGvscE6Byg-sN71iVTfuz2JCs1Cx4a793Ayjk9dNaC_HDi54SKgts_iq6k4KlIAHkg5_0MOWLj26OTqT50khPN5OVLbqj9P9QKEPyiJhx1NFFwwo8LL3eBoVdwayX4BaxpZFlzx_aOdKx-JO5sDanIUMeXO_hgKbmZQ2njl-urowR0zunwvKiBWJD0avnHVQkdv_Lf1tWMG_kZb5Ul5vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b2de1aaf.mp4?token=T6LOCEIgIqkWQOvdYcPSV5gO-G7dE5a1eFv0fUhqTD08kbyDPAORiCb7_QIGvgy0rdOEcyDikLMUeEaxfQ1bC0TExT1zIlkdZEPeQSJgEen6w8cbTH9sjvtHzX-52HTr7kGvscE6Byg-sN71iVTfuz2JCs1Cx4a793Ayjk9dNaC_HDi54SKgts_iq6k4KlIAHkg5_0MOWLj26OTqT50khPN5OVLbqj9P9QKEPyiJhx1NFFwwo8LL3eBoVdwayX4BaxpZFlzx_aOdKx-JO5sDanIUMeXO_hgKbmZQ2njl-urowR0zunwvKiBWJD0avnHVQkdv_Lf1tWMG_kZb5Ul5vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات توپخانه‌ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/140130" target="_blank">📅 01:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140129">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e7e04ce18.mp4?token=taf251xk8dz3-1QQgmRSnm71NvgT7_hNEuUcVtQG3LA5iBGYOLhrRpK1lOKbrlQFi0Sxgc-fidv1wxvYlQC38sLN5SNWUcsBUXH2j41P0HOuaa1tBN3Afy7v2VkG6nqjGt8jyjqrcwce12IfHajknBjAamBWoR48L1_a1BhpGbtR6haOCms6rhGNE5Z9AqExH_8_j_iuLjETBUByGiXJHK4vNUDjb9fBASB9JO4O2KFdh-C4wlahWyTG4FloCMRA0UvnfALUqPY5m2YyDzCa-VkslcJkJwwbwZSbKU-LbKuEP_ysas_DHKcb4HYgYTEBqRMK-RJN4jmUdmy1Rl3WtwYlPNKzon8JbUcmKGgI33obDSUVYsnd5iQjEOuabBYRvRYkgszpHE3BRBPXvafYIDDZ-EdKVL9yxchi4LBLHDJoQlU4rhIdQgoVwodLTY8zdZgPegigKHsVJ_XcGS0srDqmtJXDYOlNVuesRpObKz053gUwxulVn6mU-Rnh21JgajYaSqZZplu2pE_dypmYE8t_rmTYStSFTunKiInQFJ8_yX8-IvKZwKzW6ZQ1D_wAR6coaD07HoqD4hEi4o3NHmLhcoKQn9jqCi1I1maMlDKUzYzKm4EIi7YVTZgbqaupUnPKcNfftfGli2DEgncjQ2WEV-scWglWFy2mJ0ovDbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e7e04ce18.mp4?token=taf251xk8dz3-1QQgmRSnm71NvgT7_hNEuUcVtQG3LA5iBGYOLhrRpK1lOKbrlQFi0Sxgc-fidv1wxvYlQC38sLN5SNWUcsBUXH2j41P0HOuaa1tBN3Afy7v2VkG6nqjGt8jyjqrcwce12IfHajknBjAamBWoR48L1_a1BhpGbtR6haOCms6rhGNE5Z9AqExH_8_j_iuLjETBUByGiXJHK4vNUDjb9fBASB9JO4O2KFdh-C4wlahWyTG4FloCMRA0UvnfALUqPY5m2YyDzCa-VkslcJkJwwbwZSbKU-LbKuEP_ysas_DHKcb4HYgYTEBqRMK-RJN4jmUdmy1Rl3WtwYlPNKzon8JbUcmKGgI33obDSUVYsnd5iQjEOuabBYRvRYkgszpHE3BRBPXvafYIDDZ-EdKVL9yxchi4LBLHDJoQlU4rhIdQgoVwodLTY8zdZgPegigKHsVJ_XcGS0srDqmtJXDYOlNVuesRpObKz053gUwxulVn6mU-Rnh21JgajYaSqZZplu2pE_dypmYE8t_rmTYStSFTunKiInQFJ8_yX8-IvKZwKzW6ZQ1D_wAR6coaD07HoqD4hEi4o3NHmLhcoKQn9jqCi1I1maMlDKUzYzKm4EIi7YVTZgbqaupUnPKcNfftfGli2DEgncjQ2WEV-scWglWFy2mJ0ovDbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانت حکومتی به مداحی هم رسید
🔴
برادر حسین طاهری با این صدای مزخرف هم در کربلا میکروفون گرفت
🔴
سوال اینجاست آقای طاهری که دم از انقلاب و عدل و اسلام میزند چرا میکروفون رو همیشه به همچین صدای مزخرفی میدهد؟
#فساد_سلولی
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/140129" target="_blank">📅 01:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140128">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ما پشت هم پیروز میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/140128" target="_blank">📅 01:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140127">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: در حال آماده شدن برای انجام بزرگترین حمله از زمان جنگ جهانی دوم بودیم، اما ایرانی ها از من خواستند که مذاکرات را انجام دهم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/140127" target="_blank">📅 01:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140126">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49df8df3b5.mp4?token=Y5ywFjUNcNmRgfFkpmTyZo47f7bss1Dbk1gTymcxEIZTvB6H5LR0oB1SfDLMUiTwCOPev9KOWEg19hcG8OirVRnXF0bI0k-mU-bDq9Co8XajU4mIwsGwprD5Pz4z5-TVEKdGr5J2cSIjwK3jL1nP6RkUPscbyUp2Uk87ocWeVvLOTEh-QnmsmZcAToTxYdAUj8RLOBC5iD4qsSp6AjwpMDqCnM0OFzNoqegtd8TfmFzf1waskQQbytuMfiAuE2v9x94xJNiWC8U0oeLIViFtadfgu6tcKhlYnyK3BRJa4egDn17hpw-BqByKmgHuV0vUEPc3-tJk-pMlfI-fe4MLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49df8df3b5.mp4?token=Y5ywFjUNcNmRgfFkpmTyZo47f7bss1Dbk1gTymcxEIZTvB6H5LR0oB1SfDLMUiTwCOPev9KOWEg19hcG8OirVRnXF0bI0k-mU-bDq9Co8XajU4mIwsGwprD5Pz4z5-TVEKdGr5J2cSIjwK3jL1nP6RkUPscbyUp2Uk87ocWeVvLOTEh-QnmsmZcAToTxYdAUj8RLOBC5iD4qsSp6AjwpMDqCnM0OFzNoqegtd8TfmFzf1waskQQbytuMfiAuE2v9x94xJNiWC8U0oeLIViFtadfgu6tcKhlYnyK3BRJa4egDn17hpw-BqByKmgHuV0vUEPc3-tJk-pMlfI-fe4MLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران به ما احترام میگذارد. آنها به ما احترام میگذارند.
🔴
داریم صحبت میکنیم. ببینیم چه میشود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/140126" target="_blank">📅 01:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140125">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ:
ترجیح می‌دم با ایران به توافق برسم، چون نمی‌خوام آدم‌ها کشته بشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/140125" target="_blank">📅 01:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140124">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ، درباره عبدال السید :
- این آدم از یهودی‌ها متنفره. بعضیا می‌گن این حرف تنده، ولی نه؛ از یهودی‌ها و اسرائیل متنفره
- عبدال السید! باورش می‌شه؟ فقط برای من همچین چیزی پیش میاد
- عبدال السید ظاهرش محترمه، ولی آدم پر از نفرتیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/140124" target="_blank">📅 01:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140123">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae82204eb0.mp4?token=QF3GQ6h-qVfPgBWEWtaVlXXUyAJqv2A7KpV0KQXKd-437pvBaW_slCm1P95me1ymxFXFbdaBFzGPN24jGoX2gVuJGyfvUEu1mVbRGFWmWpsiNt_Bu9ECpDU_qk4FdTk41x1MaiOATLgOJI3z-aEBtUPzjCAX6MiHAa2N1w24JOwxPGXtoyf_pwiP83--wLf8kllGT1We0QTAHkhGtFu4bxyQCCICkeRFpvi0Zai13XeufT9HsA-e-DkAHK9JZPkhOTYI3Jz6gHOhnvOWjMuiwZkmn1xHtuy8dsfyWIzubz3g8cWL2IVnJpRana-TFsQZ1CuXy3C6u0QP3VpMkt34Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae82204eb0.mp4?token=QF3GQ6h-qVfPgBWEWtaVlXXUyAJqv2A7KpV0KQXKd-437pvBaW_slCm1P95me1ymxFXFbdaBFzGPN24jGoX2gVuJGyfvUEu1mVbRGFWmWpsiNt_Bu9ECpDU_qk4FdTk41x1MaiOATLgOJI3z-aEBtUPzjCAX6MiHAa2N1w24JOwxPGXtoyf_pwiP83--wLf8kllGT1We0QTAHkhGtFu4bxyQCCICkeRFpvi0Zai13XeufT9HsA-e-DkAHK9JZPkhOTYI3Jz6gHOhnvOWjMuiwZkmn1xHtuy8dsfyWIzubz3g8cWL2IVnJpRana-TFsQZ1CuXy3C6u0QP3VpMkt34Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات ترامپ درباره کانادا:
کانادا کشور بدی است. آن‌ها رفتارهای نامناسبی دارند.
🔴
من مردم کانادا را دوست دارم، اما رهبری آن‌ها رفتارهای نامناسبی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/140123" target="_blank">📅 01:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140122">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5853abad72.mp4?token=rJ73QhbI3w0buaA19WvsIqbx74hM9UG-nOrcZnNfn1WtcAdB_0rt3qc8HThUig_Qv5A0roty9t7Nzbxeut8-0R7lPakSV_QEVDp-4Mh9C61AtH63aSdKquxyHzBQcnSBREVs0UjKNgWL0eeqqsR3JKeDCJPv7eJtxod9Pmdqhpwo5JE-MrSaL2Qsr9nQHNMb8NF1jzLVkiXmbqkv79nGevRD-jXqp1nhPoilX2mqYfN6k9xyoi2MYuFNxOVOSautjzOFZ9UtHfFKG8khIcGr08TaoOpMwtZiGfMZ6B67tERg66yrbWAkTFD_4AKPky8gh2Ab-p55rOOFaiGEgtASrogMifuqJi2xnGfWp72rC4pkYmS0FpIFrkoGOtqniASTOh_OFXBAQ7v7-4HZAO4xIQPI-wRCGW417Hv0TfvbPMFIeKrA39f96mylwaMu67LvsoA1ek_JCP9NljCYhnT3W5TkHmTAraULAYE6nTZItHj9zFqjlCHvBg1Qy4Z-rQQ3vzpuqcNfkdfJnIKjJlc8NXGRO6YsY7Jn4s2JIxT4_9Ahdys8fmmiwEwgAR8WBNIeHI0rEvcd_gOPsLp91Y--gbNl5yqL3Po5yvB6uCCIPifdUZle6eptc1l10-NTOgN_KRprl_HYtgwMlxQAk8R01fFK8elgdOdekWf0pIqitY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5853abad72.mp4?token=rJ73QhbI3w0buaA19WvsIqbx74hM9UG-nOrcZnNfn1WtcAdB_0rt3qc8HThUig_Qv5A0roty9t7Nzbxeut8-0R7lPakSV_QEVDp-4Mh9C61AtH63aSdKquxyHzBQcnSBREVs0UjKNgWL0eeqqsR3JKeDCJPv7eJtxod9Pmdqhpwo5JE-MrSaL2Qsr9nQHNMb8NF1jzLVkiXmbqkv79nGevRD-jXqp1nhPoilX2mqYfN6k9xyoi2MYuFNxOVOSautjzOFZ9UtHfFKG8khIcGr08TaoOpMwtZiGfMZ6B67tERg66yrbWAkTFD_4AKPky8gh2Ab-p55rOOFaiGEgtASrogMifuqJi2xnGfWp72rC4pkYmS0FpIFrkoGOtqniASTOh_OFXBAQ7v7-4HZAO4xIQPI-wRCGW417Hv0TfvbPMFIeKrA39f96mylwaMu67LvsoA1ek_JCP9NljCYhnT3W5TkHmTAraULAYE6nTZItHj9zFqjlCHvBg1Qy4Z-rQQ3vzpuqcNfkdfJnIKjJlc8NXGRO6YsY7Jn4s2JIxT4_9Ahdys8fmmiwEwgAR8WBNIeHI0rEvcd_gOPsLp91Y--gbNl5yqL3Po5yvB6uCCIPifdUZle6eptc1l10-NTOgN_KRprl_HYtgwMlxQAk8R01fFK8elgdOdekWf0pIqitY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
دولت جو بایدن، فاسدترین دولت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/140122" target="_blank">📅 01:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140121">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4760e790ba.mp4?token=se0DvhgpFl-UMQPbQLCOMJtepiEJOloBriiX9l3ZVs2F2cohQU3QTliF43-CK7dVCU7VUKbMawnOl3d0zz3asv0ZATwROAzkQjXNprUAhH4D67MCWQrELqjNLH1ZVoUOtOeGcFHHWZr12HCzRVupXg7i6-rD1MMuJBJHf7KfrzuqgHiTvB0bqUfI8PTTX6oKA17hrzHRukeeeVH2c_X020L78hpXIEjMuc8ZcCT32r7P7q-kKa8dP1iUaq38ukvYRKNMxgl5iCDtkEdqx_BnNEgsE07dFbwOhThEjFBEop2viCCI6HXgbU7BoPNzLMhOA5KIAwe2qlw9oNER1tUUmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4760e790ba.mp4?token=se0DvhgpFl-UMQPbQLCOMJtepiEJOloBriiX9l3ZVs2F2cohQU3QTliF43-CK7dVCU7VUKbMawnOl3d0zz3asv0ZATwROAzkQjXNprUAhH4D67MCWQrELqjNLH1ZVoUOtOeGcFHHWZr12HCzRVupXg7i6-rD1MMuJBJHf7KfrzuqgHiTvB0bqUfI8PTTX6oKA17hrzHRukeeeVH2c_X020L78hpXIEjMuc8ZcCT32r7P7q-kKa8dP1iUaq38ukvYRKNMxgl5iCDtkEdqx_BnNEgsE07dFbwOhThEjFBEop2viCCI6HXgbU7BoPNzLMhOA5KIAwe2qlw9oNER1tUUmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من 28 بار پیروز شدم و یک بار شکست خوردم. آن شکست، مربوط به فردی بود که من فکر می‌کردم فرد خوبی است. او شانس چندانی نداشت، اما من گفتم: "با این حال، من این کار را انجام می‌دهم."
هیچ‌کس نمی‌دانست آن فرد کیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/140121" target="_blank">📅 01:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140119">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=K5CsNBAICfJ3yLwXlApNiuDULWoQq4K5kJllTebTzuSqg2RD5G7YJdE6aDJIAd7fQc6RnMkMN5bHogpjVaiDVG1p1KCpBTaHS_lpJ8aQ494MW3ZEeUgaZhtuHHlSZzSjh_apiMlysoCteVmBcnD2kjSEEclMl2uDx0gqf5rbAkk18VgDNOxpXJ0uAXsTEd0Ty5dkgrwNBqMYO2cf7merwOEeOfsPYyFmbwuv76Y0zjTo2IlLP0PM5DLmZ4km7deDFjjcwFAaN1yap3pU889GhtyokTxnLlXA8InBW1YSSLohNO84y1r3jicp4Gv3XNF6LosZQwEG-S6H9fGsQrdfGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=K5CsNBAICfJ3yLwXlApNiuDULWoQq4K5kJllTebTzuSqg2RD5G7YJdE6aDJIAd7fQc6RnMkMN5bHogpjVaiDVG1p1KCpBTaHS_lpJ8aQ494MW3ZEeUgaZhtuHHlSZzSjh_apiMlysoCteVmBcnD2kjSEEclMl2uDx0gqf5rbAkk18VgDNOxpXJ0uAXsTEd0Ty5dkgrwNBqMYO2cf7merwOEeOfsPYyFmbwuv76Y0zjTo2IlLP0PM5DLmZ4km7deDFjjcwFAaN1yap3pU889GhtyokTxnLlXA8InBW1YSSLohNO84y1r3jicp4Gv3XNF6LosZQwEG-S6H9fGsQrdfGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
باقر خرازی (برادرزن مسعود خامنه‌ای):
ما باید از جمهوری اسلامی گذر کنیم. علت اینکه این الدنگ (پزشکیان) رئیس‌جمهور کشور شده و بی‌حجابی کشور را گرفته این است که هنوز از جمهوری اسلامی به حکومت اسلامی گذر نکرده‌ایم.
خدا لعنت کند شورای نگهبان را که این "آشغال" را توی پاچه ملت کرد.
چهل سال است با آقامجتبی رفیقم؛ او بسیار تندتر از پدرش است؛ اما یار ندارد.
باید به نیت حضرت فاطمه از هر شهر ۵۳۰ نفر جمع کنیم و به تهران سرازیر شویم و کار دولت پزشکیان را تمام کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/140119" target="_blank">📅 00:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140118">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8544c437a.mp4?token=ZbAOLeHiqRDBUruADaMUeGy-jt1d2NcfjZpZsfH1SnjtVVo18-tTkFX6MhfHXHz90qDVFt-kL6tnk49ZL4Cq2uETqktHSujHPUJtsqqWzgH5HeiyAwaoP_FniN_Ll8VXzLt-K1aZPmkcMjaT44cIuB2sF0VGBnEeU0GiFdSPukMv6C-ylIaz0zlpbmShdk1fFQAVg-ZDQ1v4gPAiTwoCprpzhCYP3guBZRhVOm9R9i2NeWPs6JP9MnqoWs2SokoeRxBbpsA6fsCwEHCZPlcSXq8zNiv_yLmNT_lTjqK9IZY7djuL5GcXHkCEVO-NW0Rgh0xsVm6OHG-kdn57B2nOgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8544c437a.mp4?token=ZbAOLeHiqRDBUruADaMUeGy-jt1d2NcfjZpZsfH1SnjtVVo18-tTkFX6MhfHXHz90qDVFt-kL6tnk49ZL4Cq2uETqktHSujHPUJtsqqWzgH5HeiyAwaoP_FniN_Ll8VXzLt-K1aZPmkcMjaT44cIuB2sF0VGBnEeU0GiFdSPukMv6C-ylIaz0zlpbmShdk1fFQAVg-ZDQ1v4gPAiTwoCprpzhCYP3guBZRhVOm9R9i2NeWPs6JP9MnqoWs2SokoeRxBbpsA6fsCwEHCZPlcSXq8zNiv_yLmNT_lTjqK9IZY7djuL5GcXHkCEVO-NW0Rgh0xsVm6OHG-kdn57B2nOgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقاد تند یک معلم از شهبازی، مجری حال بهم زن صدا و سیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/140118" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140116">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DblQmkPGwOL8tfEZRzP_TPuaAITkXOTrYxRHeuKv09JtqxG62JVt1lPdhuFK2HDToPEXQqdYz62eDg_bQ3VEVll2kB1XVoYAqcgc_mnksOnqHb7qdUN2cyjvQsq9UacBphJWzsgmA6T7uQKQ7wV6APPeP83tTSYa1r0IlU2V6jOhwB7l5zzLNMy93czGIRrhAIIKZmNc4zPRFrq9OvWPqAHHE0uyQEdC0BhcaKlduWT9RWcgJwXA-F0zYVI6fUdeimFgQfewblX7CDtBwSAinXHoJU5ZaR_IoMmMQHYS79q1jQIXvAP_eiE_JtOvOKe-9vDJuRZfMbEd0L2jDbi9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8vZBa1I-uWznBrK74s7xXdVuPs8if-XEYiEocfkw-q4-p3W1msf2yNRI7IIXnrqhYedpAqI6ttO8Lgovnf__VD2-rMPG3wpI3228TwP9MrVSecLKWHdmoZIJ_cJkz99UUC2_BKHfzFEWlBDOvbxHyJQ3f7b7fzQDxIJLqa6g8PI5G-f-2-On7B-hcT80b4tss7EpSDbvfVNYuk6ZvmtnsBKmA1km9Iss6kavKc5rHDwzwsPEJpmQF6u-S4bB-8w0RqYt8798oQ3oO4Ys3IhGiUnhPZN_DNbxX1aK8NAmkidHCpNwyp5s3oc3_FWYs3gfaPtfbysJTGARqZ4ILVYuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی باری فله‌بر «مینوان پایونیر» که دو روز پیش مورد حمله ایران قرار گرفت، همچنان در محل پهلوگیری خود در حال سوختن دیده شد که نشان می‌دهد خدمه نجات، کشتی را در جای خود پهلو داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/140116" target="_blank">📅 00:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140115">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clXqRtpKW-eKieu6fmAG5cHSQRJvl_ty054m3bXqCbFyKQpN8i7dXXtoFqWH8vTot6pff654JF_d1vhRrIatua9aEXyFKWnZoFYOWrVdgql1UxvmBEdPa-PzOnHZyVlMBzgO085xZdERSS5RSAnCNfcHqp8TqiwvR2ELwhjQiS7qWETai4XTxaJrHdNiKTEMPLGmGRpSqyW_8txGpiXiHaoJ_iz0jgl_iE5STduttcHjna3rthuj8QVxMXtKdEjh9kIIFkf4owxqyy1lgjcZI0Mrqb6dddGjwUs6y6WpzP_LUBaE4f9rNyo__4EU7p5zAhynVt86dtqNrJJWa1zYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور فیلدمارشال حاج محسن: بر اساس برآوردهای اطلاعاتی گروه های تجزیه طلب در حال تدارک سناریویی خطرناک برای ورود به خاک ایران و اجرای عملیات تروریستی بودند؛ اما این طرح پیش از رسیدن به مرحله اجرا، در نتیجه عملیات پیشدستانه، چندلایه و هماهنگ نیروهای امنیتی و نظامی ایران خنثی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/140115" target="_blank">📅 00:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140114">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c7abd15f.mp4?token=V5lRzeMFFFaYJQu-cAltNbUAvsJe2HwDCeflqu6ixMU9c7VxcVc2po8-djSzn6octbsiZhTW82E_ATToFeUBie4fqXYeQDSKQsy69pZz2pa1gx9ltMC2S3Yvshlu1QmSQ4SBdFScI14g_F-eNy_C9GkhNAIQCdTTMKQpHVmSnmotsFyBWmAZmhKHb_ZLyfbX_mVzpqazrQtbIcCz87keFtCLeb7vF27ATSZsju9Ck8z5_sV5c4f9jz1rSOCl8CnfdTgEeeLlCMbNdfVMgQoNSCtRRBiMOczUy2x-GcNw6DIft7WM6YPZjKe9lDBdEC1vETBiGg5c2wBCkSp0qTWrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c7abd15f.mp4?token=V5lRzeMFFFaYJQu-cAltNbUAvsJe2HwDCeflqu6ixMU9c7VxcVc2po8-djSzn6octbsiZhTW82E_ATToFeUBie4fqXYeQDSKQsy69pZz2pa1gx9ltMC2S3Yvshlu1QmSQ4SBdFScI14g_F-eNy_C9GkhNAIQCdTTMKQpHVmSnmotsFyBWmAZmhKHb_ZLyfbX_mVzpqazrQtbIcCz87keFtCLeb7vF27ATSZsju9Ck8z5_sV5c4f9jz1rSOCl8CnfdTgEeeLlCMbNdfVMgQoNSCtRRBiMOczUy2x-GcNw6DIft7WM6YPZjKe9lDBdEC1vETBiGg5c2wBCkSp0qTWrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شروع عملیات گسترده موشکی روسیه علیه مواضع اوکراین
🔴
در این موج حملات بیش از ۴۰ موشک شلیک شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/140114" target="_blank">📅 00:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140113">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxRVs2tYiWiepIcvCPfHZ0Tl2CyJfaThyEYsFPFsUXdS2e-FrSS_MWG8LAW0gWsP2rDJsdc9sLMpLdxWplSq0cGmDgb5YcLNew-tS8JE2QLbrpAiS5m89AKbgPvlaTHuF4vd1Hl0C-b-aUYxwynW--Frrqk4KsRhepvHWNEksInL1l6iiX_zWzDnAtVVNVs2B_t2Ij0hEEcL0xYM0PfxR7pDo_KCtQSTdLCjA-6U1EbRMcu_whzGZxDQdFtcB5bxuLIL_LB7LlL_ftUgsPKfcEUUG9Dcy_uVFRJfXwS8HYbbFlcnd4UBWmUTgFi-VpP6CLFFccpP0GGPCqs6IFhR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، از طریق شبکه اجتماعی Truth Social
:
دیشب، در مورد تاییدات، من 28 بار درست و فقط 1 بار اشتباه پیش‌بینی کردم، و بسیاری از این پیش‌بینی‌ها غیرمعمول بودند، اما اگر اخبار جعلی را مطالعه می‌کردید، فکر می‌کردید که نتیجه کاملاً برعکس است، یعنی 1 بار درست و 28 بار اشتباه.
🔴
آن‌ها فقط در مورد یک مورد صحبت می‌کردند، و به همین دلیل است که به آن "اخبار جعلی" می‌گویند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/140113" target="_blank">📅 00:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140112">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taN7YPGj6qYwJ0_Rz99G7T0t0LAH99hPVL8LBce30qJHEWJNLWTFp0Kl-auYQHBRa3e5jYPtQhqLGtTIRz7HeBsYo-vMujniuxI7NIHVz2TFFUf86ACwkIzb0Kl1W90V3hu4xb86H6Fz4OldtOg4wCZfmffXpfmp8QPovsbJlf25DnTv3uE3jlzWKMLGwD2k-shPPHVLcsx4zEw_dByZ9pcIc90oXTD6ULu0zqz-rwc4yfozxODrQf4VGNMFhvgxV5RN8a9tH7Nchv6DA_y-e6g6fQ560IxSsrrMYJVcSd5-jSBZQ03ECATOaQqLEXljeo9jRDC26_d31T6UzSxIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر افسر اسرائیلی که کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/140112" target="_blank">📅 23:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140111">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVvEz3msVc3baZ9E6_hZ3hjPMqYQ8mujJfcUEz0g8Qcc9Jm7qr-8SsTBysgLh3w7YFGkbftiwlzbxhbk7WxOwr5owrmxKhx0pSbjh6MjEnWpsS9pBcBNMzci6emnoAVROh9mDMQJaV5pFPimY5x-902IBbzQ3vl5GIaWTi1f2heIKjChsvBSRjtM3mackO-w3FA_PVUEQhKs3qKliqW9SRCJd2YFYN39mwoP2vz1fT9LB0g_NvAQH2TSCexSfKYVPwPoglP3V9V5QNosYDjVN8NFktino-ffpVKRrs-FsAt-fAAsTl1fRpQ7iTRKehAT_oiLhubS9DHYNRQQf9vgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعلام کشته شدن یک افسر اسرائیلی با رتبه سرگرد امروز در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/140111" target="_blank">📅 23:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140110">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رویترز به نقل از منابع: ایران به کشورهای حاشیه خلیج فارس هشدار داده که هرگونه حمله جدید آمریکا با پاسخ متقابل علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه روبه‌رو خواهد شد
🔴
این هشدار در جریان مجموعه‌ای از تماس‌های دیپلماتیک سطح بالا منتقل شد
🔴
پیام عراقچی در تمام تماس‌ها یکسان بود: «ما برای پاسخ متقابل آماده‌ایم، اما یافتن یک راه‌حل دیپلماتیک بهترین راه برای ویرانی گسترده در منطقه است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/140110" target="_blank">📅 23:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140109">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
درپی تیراندازی مرگبار در ایالت کارولینای شمالی آمریکا چند نفر کشته و زخمی شدند
‏
🔴
رسانه‌های آمریکایی گزارش دادند این حادثه در منطقه «پِراسْپِکت هیل» رخ داد و دست‌کم ۳ نفر کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/140109" target="_blank">📅 23:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140108">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
العربیه: تشدید تنش‌های اسرائیل در جنوب لبنان روند مذاکرات را تهدید کرده و نشست‌های فنی به تعویق افتاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/140108" target="_blank">📅 23:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140107">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
یدیعوت آحارانوت: نتانیاهو امشب جلسه‌ای امنیتی برگزار خواهد کرد که به بررسی واکنش به تلفات اخیر ارتش اختصاص خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/140107" target="_blank">📅 23:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140106">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2ebd2079.mp4?token=fWK86QJBoCf2oMqWwff6pO_Zi9h2nL0e1kCEbQpM3mMH2gF0QFGfOKky33PhC1zw9XwPFblT8AIRa0kbkhgFdjATh3VPfp_7b5Brj0AWMUF2BD4fcc-ce5wqfvlBFFPGWlLDcjV7J9cWbqxNbnYcHVIVS8YymuD-UqfZ6W1cM87QxDRUMAOcEvdnRRJezUMVXm-z2E3UhgYQ-fR9eDzYoaoTNN66qt6MxVVzK2CYpSjtw_g5UrxUGNKWro2mb4yrpL1QH6CDPArgo66kOKQd-Q0HEJHoSIpXOAzXtaLkKrQQd_Q1f-pNRn6GEe5neIYN4y2o2xhZH_a3aAwo7NsHCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2ebd2079.mp4?token=fWK86QJBoCf2oMqWwff6pO_Zi9h2nL0e1kCEbQpM3mMH2gF0QFGfOKky33PhC1zw9XwPFblT8AIRa0kbkhgFdjATh3VPfp_7b5Brj0AWMUF2BD4fcc-ce5wqfvlBFFPGWlLDcjV7J9cWbqxNbnYcHVIVS8YymuD-UqfZ6W1cM87QxDRUMAOcEvdnRRJezUMVXm-z2E3UhgYQ-fR9eDzYoaoTNN66qt6MxVVzK2CYpSjtw_g5UrxUGNKWro2mb4yrpL1QH6CDPArgo66kOKQd-Q0HEJHoSIpXOAzXtaLkKrQQd_Q1f-pNRn6GEe5neIYN4y2o2xhZH_a3aAwo7NsHCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات توپخانه‌ای ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/140106" target="_blank">📅 23:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140105">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmefLDZxM85WX0SSj_ZyiuuoKakvuu8a3plC3-wmsDg8mXCSoT57GfcD-DBPdl9Dd2gmGlLH3g8y1XNZ6K4l_5UKRblth97pJtikFs6Q5H1ZWSq_xiLf333qCsQhWi20MrLNYp27piw9MYlh4u67GDwsY7OOgsvoQOiQEfPAeN_ZXMZzXG4Fx0lC-0eoXKVnEKnIuM9n2fCYvBZMQtFqSnBnih2cDbYtOwbRRvxHI4_TdyTpaHIcebfdzmbtsbcBobY8CtrqxLAT19xibk5SPxakDTscBUNnrfWImkebKiHd0pWFTkt4S4dh7Cf__L7f0Gll_xwJEt5m6tkeuANIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکسی که حساب کاربری وزارت خارجه ایران در بوسنی پست کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/140105" target="_blank">📅 23:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140102">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef0d6c980.mp4?token=XPQhEuXuq4rIYOsudNuXl3eDvY5hFZbzpMqNWVRobuuVHXXvvzD0O6vqLPGJn0LuQfoPFq89YrdOkFibhY8rYi_ycLucePQa--Gkf1GYWGqCFlTrPka0deiwKYdC0eVVbZhHZqYusYSkYq3D3YiWV7JUrMNe6mFNRlPMhXNLMfhPzqAQ41tYgVpQ4ZIq_o14dBmQWiOlGRHY_USfrGV-Xp08dU-_g1CqbLIU5VIaW6huHa39s22PR3BmxjF5qc0h57CsmXSyZKsdjW5vziKhkEtozs-zyawFpd7r628xEBgAQRDrBpxwhyAIIZmwKRIf0QbsQ972Od_JTy3lCSlTBXYaOGzktxd2j2Ofvzux7NlTe6upjhlvbjwecmZEW6DcWUbO5W3eYgx2XtM1CqrEJtXKGc-1KvKy9x04DRSz59rBxkeRMvVbTAwXIsSjpAdRgpJWT0TaADZFyltHUYtGM49C_89DYbiRq4Pv9oPMLPCLc3f9OXfDvwb28WiA1DedLUUzWAqbb3Vex1BSihbtgmFZx5T_-csJErMfv_QjHQNhZBdRVr58aPIUXydBsPiNmX0XhYUqFKwj0_BYtJYHVk_mjytxv1_3IVzG7AGnT25zRh3XyM9MkR6AatOglv_kDtPTIoN9ogg5e2W8iqIUWIuC2bm-owLoU1lkkx-GjkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef0d6c980.mp4?token=XPQhEuXuq4rIYOsudNuXl3eDvY5hFZbzpMqNWVRobuuVHXXvvzD0O6vqLPGJn0LuQfoPFq89YrdOkFibhY8rYi_ycLucePQa--Gkf1GYWGqCFlTrPka0deiwKYdC0eVVbZhHZqYusYSkYq3D3YiWV7JUrMNe6mFNRlPMhXNLMfhPzqAQ41tYgVpQ4ZIq_o14dBmQWiOlGRHY_USfrGV-Xp08dU-_g1CqbLIU5VIaW6huHa39s22PR3BmxjF5qc0h57CsmXSyZKsdjW5vziKhkEtozs-zyawFpd7r628xEBgAQRDrBpxwhyAIIZmwKRIf0QbsQ972Od_JTy3lCSlTBXYaOGzktxd2j2Ofvzux7NlTe6upjhlvbjwecmZEW6DcWUbO5W3eYgx2XtM1CqrEJtXKGc-1KvKy9x04DRSz59rBxkeRMvVbTAwXIsSjpAdRgpJWT0TaADZFyltHUYtGM49C_89DYbiRq4Pv9oPMLPCLc3f9OXfDvwb28WiA1DedLUUzWAqbb3Vex1BSihbtgmFZx5T_-csJErMfv_QjHQNhZBdRVr58aPIUXydBsPiNmX0XhYUqFKwj0_BYtJYHVk_mjytxv1_3IVzG7AGnT25zRh3XyM9MkR6AatOglv_kDtPTIoN9ogg5e2W8iqIUWIuC2bm-owLoU1lkkx-GjkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پالایشگاه نفت اوفا در منطقه باشکورتوستان روسیه، مورد حمله پهپادها قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/140102" target="_blank">📅 23:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140101">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزارت نفت، نهاد ریاست جمهوری را به پرداخت ۱۳۸.۰۰۰.۰۰۰.۰۰۰.۰۰۰ تومان خسارت محکوم کرد!
🔴
در‌ یکی از کم‌سابقه‌ترین‌ دعواهای حقوقی در دولت بر سر اجرای اصل ۴۴، شرکت سرمایه‌گذاری اهداف زیر مجموعه وزارت نفت، نهاد ریاست جمهوری را به پرداخت ۱۳۸ هزار و ۵۶۰ میلیارد تومان خسارت محکوم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/140101" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140100">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر انرژی ترکیه: ظرفیت مسیر نفتی جایگزین تنگه هرمز را به ۲.۵ میلیون بشکه در روز می‌رسانیم
🔴
وزیر انرژی ترکیه با اشاره به بحران عبور و مرور کشتی‌ها از تنگهٔ هرمز گفت تحولات ماه‌های اخیر نشان داده است که جهان به مسیرهای جایگزین برای انتقال نفت نیاز دارد و آنکارا در حال مذاکره با عراق برای توسعه مسیرهای جدید صادرات انرژی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/140100" target="_blank">📅 23:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140099">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXTBHRXPcVjBogCNcUBTNXHaOifDCzRLFQ68ztCwDR9xPJj_Uy0_IA-MPFiOH1hsQNm8LxvQqkxUhvc7e92vODuyg4MLXGgdmCNsTiVVlT_OT-WNgEpLR3-bezyUHPOKo0f71irH-oqNFigLknIFK7LW7C_iK7K5IWd3FvOxDQsqxQtMGLHxeg8oPnsG06F1yvmdCReUXA-BcpusLv4F47w4giZhfRVMoXClcmKlV0zeZjZJ0W0w5EDpckJpCEpW3v0-jnPzFBkAuu0j6HIwvBLaNGbriDRGmK7mWiXcYt-hJEVx5QbwqFU_dvJKFGrbWHoCQ2udM2fh8_UH4mxbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کمیته مالی کنست اسرائیل نقل و انتقالات بودجه ای را تصویب کرد که بودجه سال 2026 وزارت شهرک سازی و ماموریت های ملی را به رکورد 242 میلیون دلار رساند و سیاست دولت را برای گسترش شهرک سازی های اسرائیل در کرانه باختری اشغالی تقویت کرد.
🔴
دیوان عالی دادگستری اسرائیل در 5 اوت به طور موقت انتقالات مورد مناقشه را متوقف کرد تا در مورد اینکه آیا کمیته به طور قانونی در طول تعطیلات انتخابات تشکیل شده است یا خیر.
🔴
منبع: تایمز اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/140099" target="_blank">📅 22:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140098">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پزشکیان درباره دمای اتاق مصاحبه:
من زابل خدمت کردم، پنکه هم نداشتم، دیگه چی میگی؟ چندتا از کولرا خاموش کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/140098" target="_blank">📅 22:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140097">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایالات متحده شامگاه چهارشنبه اعلام کرد مارکو روبیو، وزیر امور خارجه آمریکا امروز با اد میلیبند، وزیر امور خارجه بریتانیا دیدار کرد.
🔴
وزرای امور خارجه ایالات متحده و بریتانیا درباره تعهد مشترکشان به حمل‌ونقل امن در تنگه هرمز و برنامه هسته‌ای ایران گفت‌وگو و رایزنی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/140097" target="_blank">📅 22:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140096">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پزشکیان: ۲۰ درصد صرفه جویی در انرژی معادل ۱ میلیون و ۸۰۰ هزار بشکه نفت است. کل صادرات ما ۱ میلیون و ۶۰۰ هزار بشکه است. اگر ۲۰ درصد صرفه جویی کنیم کل مشکلات ما حل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/140096" target="_blank">📅 22:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140095">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b349f9bd3.mp4?token=B9cDdf5JlTA6oDtBJ7aGzLtN9JBhrHFJMWTki4VocQuLHdx-jY6x3EWIg_vRk8CfltRpMv7tSLtcAaLq1-tsYcitCjbegJp-MQFAHNUIAIMvhuZExrYfhZ-pxIzoUSguooe719OF37fJ4EKM-IlIUIAfqEW3mIpNgbinY3qebczTW0BwdrLF70RiD0QmzEgb82V-wMVAddleCQpOJ_MoOoKsE2YbZ0kqLqhGFwzN_TVqXBrfCsDs8W0hfFdts3loCcetCdTmETaDVMff4C6pMmbz1D-qiWeQR0uKbL36QjaCv5HVXVcNWz-PyeXfKTtlXt8eApvVAmNnU9IS3Q-U1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b349f9bd3.mp4?token=B9cDdf5JlTA6oDtBJ7aGzLtN9JBhrHFJMWTki4VocQuLHdx-jY6x3EWIg_vRk8CfltRpMv7tSLtcAaLq1-tsYcitCjbegJp-MQFAHNUIAIMvhuZExrYfhZ-pxIzoUSguooe719OF37fJ4EKM-IlIUIAfqEW3mIpNgbinY3qebczTW0BwdrLF70RiD0QmzEgb82V-wMVAddleCQpOJ_MoOoKsE2YbZ0kqLqhGFwzN_TVqXBrfCsDs8W0hfFdts3loCcetCdTmETaDVMff4C6pMmbz1D-qiWeQR0uKbL36QjaCv5HVXVcNWz-PyeXfKTtlXt8eApvVAmNnU9IS3Q-U1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: هر چقدر که فکر می‌کنم، نمی‌توانم هیچ دلیل منطقی برای این پیدا کنم که چرا رهبر ما، فرماندهان ما و دانشمندان ما را کشتند.
🔴
بسیاری از فرماندهان و دانشمندانی که کشته شدند، حتی خانه‌ای هم نداشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/140095" target="_blank">📅 22:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140094">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رئیس‌جمهور مسعود پزشکیان: رهبر پیشین انقلاب توافق کردند که ایرانیان مقیم خارج در صورت بازگشت با هیچ مشکلی مواجه نشوند.
🔴
حتی اگر کسی مشکلی داشته باشد، باید به او گفته شود که بازگردد، نه اینکه هنگام ورود به اینجا دستگیر شود.
🔴
ایران خانه هر ایرانی محسوب می‌شود و برنامه این بود که مکانیزمی ایجاد شود تا هر ایرانی بتواند آزادانه به کشور سفر کند و از آن خارج شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/140094" target="_blank">📅 22:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140093">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پزشکیان: کسایی که ‌که کشته‌شدگان دی ماه پارسال را ۳۰-۴۰ هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/140093" target="_blank">📅 22:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140092">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن:
ما نفتکش سعودی «دیزی» را در خلیج عدن با موشک بالستیک زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/140092" target="_blank">📅 22:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140091">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd906c65a.mp4?token=Uf_aDxTO-6nr6Jo4tdXB7rsF3c2w_n0CYFv8wbr3jKxRIvSNuUjnGQDD-g0da5jmH1KPYN5IRoYdzBo6n4WDoD7qFLdH12CXEvQY3maoD8GnVLdEeTI3UpStmdDnenAapbl_pJ3GWz9nsZuoYYgV8riBE6dEmkpaiP2oMErLNo4PI5d3eqmcI1-DnSqROW42N8IXatVwXJdjN_YK1lp91D14jMrn8Rx9HwxhQEQ7XFIg6EAEiXmzUYBTNJGfrK-Mu8GmhQFYX0oAVz6KMh9qMuWoTx198aOKR1gKmB7vNRCpKFzHtaktYoiMG-E5hD5rwOpfjOD6zoja0jhS_hzwKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd906c65a.mp4?token=Uf_aDxTO-6nr6Jo4tdXB7rsF3c2w_n0CYFv8wbr3jKxRIvSNuUjnGQDD-g0da5jmH1KPYN5IRoYdzBo6n4WDoD7qFLdH12CXEvQY3maoD8GnVLdEeTI3UpStmdDnenAapbl_pJ3GWz9nsZuoYYgV8riBE6dEmkpaiP2oMErLNo4PI5d3eqmcI1-DnSqROW42N8IXatVwXJdjN_YK1lp91D14jMrn8Rx9HwxhQEQ7XFIg6EAEiXmzUYBTNJGfrK-Mu8GmhQFYX0oAVz6KMh9qMuWoTx198aOKR1gKmB7vNRCpKFzHtaktYoiMG-E5hD5rwOpfjOD6zoja0jhS_hzwKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پزشکیان: نقشه کشیده بودند ایران را ۴۸ ساعته مثل سوریه بگیرند
‏
🔴
شهادت بزرگان ما در جنگ رمضان دردناک بود؛ با همه سختی‌ها و مشکلات امروز از ایران به عنوان یک کشور قدرتمند و با عزت بالا نام برده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/140091" target="_blank">📅 22:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140089">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3ef09d2f1.mp4?token=E9oDeXLjlgyzmidgCh133W4ipgLf9ikTJvEkGWgU_719YtH5fK9E3Yn47uMAHrXTGkbesd3zdrM5m7ifYW8DVig1_MQ0MYDjlI-ldQaasPG6VL9BFMPLAiFXYv0f5BfLsniEL4BpwbrcHRVLqpcd9bNzICpWYaNZ-8-ELYjbnCPNa1pgXRIY8XK4at4UlF6JI3vjuRjeAhUifF9TJdH0i0OpAnUnKVn_1B2rORXSP-IspR_1QNTdpLx29vsp5uEZPOMpK5iT8CHnAszKDdQtkXE4FPkOwQvV-fCcs-iKjMTpjQ8TWzN6kTlnzfK3vrgFyVRpvdu10mZR6W2hY6kNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3ef09d2f1.mp4?token=E9oDeXLjlgyzmidgCh133W4ipgLf9ikTJvEkGWgU_719YtH5fK9E3Yn47uMAHrXTGkbesd3zdrM5m7ifYW8DVig1_MQ0MYDjlI-ldQaasPG6VL9BFMPLAiFXYv0f5BfLsniEL4BpwbrcHRVLqpcd9bNzICpWYaNZ-8-ELYjbnCPNa1pgXRIY8XK4at4UlF6JI3vjuRjeAhUifF9TJdH0i0OpAnUnKVn_1B2rORXSP-IspR_1QNTdpLx29vsp5uEZPOMpK5iT8CHnAszKDdQtkXE4FPkOwQvV-fCcs-iKjMTpjQ8TWzN6kTlnzfK3vrgFyVRpvdu10mZR6W2hY6kNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: امکان ارتباط با رهبری سخت است!
🔴
رهبر انقلاب در مورد تفاهم، نظر کارشناسی را پذیرفتند؛ ایشان گفته بودند که اگر سه‌چهارم رای بیاورد آن را می‌پذیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/140089" target="_blank">📅 22:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140088">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhY2oD2cfc5LqsKw4Flti1wDcr80VdnUww-3ngFcc2kmIDUmD9kPbFbzUuY1pXuI45xSsgGogiNEZC6ft9ReynwXFpoz_veb2FrJirMc_ZhSnPTgXr9cvoeAWcCYIDn_ZEqECIpxsbt_M0uzSMFnaE1t2K_ICLZ_6kg7b89hQMnMufqUGelsGKivMYpOe-PZGxI4N9Tv93pxGzL8xrrt4tZyq2sCIqdATdxWqZwc5yajp63I6UUuB0bAfZMbRWSRDIoNoHYBYFqMQV3JuUOpvwR73XHXMHgqwufleJeSTX7EgoHvvOpbF6233DBTPI4s02L6DVDZCgnvVYDyWsJzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: و اعتصموا بحبل الله جمیعا و لا تفرقوا و اذکروا نعمت الله علیکم اذ کنتم اعداء فالف بین قلوبکم فاصبحتم بنعمته اخوانا و کنتم علی شفا حفرة من النار فانقذکم منها کذلک یبین الله لکم آیاته لعلکم تهتدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/140088" target="_blank">📅 22:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140087">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پزشکیان: مردم همه کسانی هستند که در این مملکت زندگی می‌کنند، مستقل از عقیده، باور، دیدگاه، جنسیت و قومیت و حاکمیت وظیفه دارد بر اساس عدالت با مردم برخورد کند.
🔴
در این مدت تمام تلاش دشمن این بوده است که ما را از هم بپاشند و تفرقه ایجاد کنند و اگر تا حالا مانده‌ایم، همه مردم نجیب ایران را نگه داشته‌اند، نه فقط آنهایی که در خیابان بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/140087" target="_blank">📅 22:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140086">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4569f98205.mp4?token=vI4hTVHqkPUA3TaP11oKaYj3NOvK9I0xVR_yL5eV-4IgxEma7MVVcLpOUrPUwU_WCn1kr5VjMAa3USyzRRUfJEB4UZSwv4KSNBmp5-kLdV3pjJOk4dMp9w6tgAqPoqOVzQMhMZ0B6OnsYkS1IpraZAljOidJrVnk1HbtnRbjbO7-J2ZFinj3VLKoArRm6i9JsGQJSMwtby1ycAwsCixcX5_AOE0uP_z8vjIaaAyvH3gneCBQPNQ4f9lsy3zAIoN7TyDSMLWc_P0DzPH9If8mhOC2vOEnwpd4EhK50-GSsDVaJtYfrBGx73Pi0HMCY98Ykn90aaSvI1V4ZrEozOKf1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4569f98205.mp4?token=vI4hTVHqkPUA3TaP11oKaYj3NOvK9I0xVR_yL5eV-4IgxEma7MVVcLpOUrPUwU_WCn1kr5VjMAa3USyzRRUfJEB4UZSwv4KSNBmp5-kLdV3pjJOk4dMp9w6tgAqPoqOVzQMhMZ0B6OnsYkS1IpraZAljOidJrVnk1HbtnRbjbO7-J2ZFinj3VLKoArRm6i9JsGQJSMwtby1ycAwsCixcX5_AOE0uP_z8vjIaaAyvH3gneCBQPNQ4f9lsy3zAIoN7TyDSMLWc_P0DzPH9If8mhOC2vOEnwpd4EhK50-GSsDVaJtYfrBGx73Pi0HMCY98Ykn90aaSvI1V4ZrEozOKf1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلیپی پربازدید از محبوبیت فوق العاده بطل در رسانه‌های عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/140086" target="_blank">📅 22:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140082">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AH9h7F-YPrqPgeULMjEgW8AVwiyV3W4D5bFyJG51CwHAASaQeTiaf6Q4k32Opja4PVVljG5wAV8qk4oisT634TSovzmaVJ3zs_YrZoWP-LQFaDg056XSD_-tNvSD2ujp4-i03gmFMj8TtAwd-UEY6dvAppWWYKtUndDTSEeWBADc827bFaSWWaK88hpohXfo0eSDr-xlJN44no7Hk-qJnji5rCCzxap2YybUnOVsCw1No1FvSi9Fb7oHmq6Lar0_Hcn4zNutq6pyNUMOyFklAumGGKeiSRdFlD0PV8jymvCT-yLCTsqRg_97XHXkagGvwGyviXoGA6JmYCBMC-2m7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ije9is9ymZDB4T4EMeZAWlPjtE6WL6G_yyqMghia8E7ZthDz29E4HPek2wEjsPPmnRvCVVxScqG2Uw1MMQ2Dc1tMUo-DlduBCvQ54DDfFPyAWkbiCMK8J7BmN0XF0syiUSiO6jaxeBhakajYVczvKi2b0xMQv3d48-NJFalnKBolgsSJaDGraO3zS203jJ_DMEsBIHTpaJNvk_3pbfmp28EDeYDTgfmenuc_XSgFpUG6HxycPkJOsSbI7Vpio-6ngmwURXW5FvC46HdnIRZmrhAmpKwPM64V8Rc4bp8tiffdoqRUBipbJncPfUbjVtr3rnmTZL9i7RyFkXnyASEQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5M8w_U2n0HT06ilpTv6s9MwrRhNs3fmyiXaNT5ui6u_jiJMLbZ5F18uiCttLe3S4_Fe1pa1KqzKbPXipX1XRx8TrA69yuUxKw_FAdHh_panRjWa8Z1xmvMzvWakbbDSzsyMx6suuZjoK7PjrEy6A_9OK6xMuhkRpJZ7wqoofkVN2xivst-GQn52TlM6mxEK3nk7zuJldi7eXJUOTvVM0gvoynMGfpaVyQo7xZera_5HBwPUtpR0JkyK7Xtl3uMnYMCp8SEc7xp24gOddigV_nJE0BbcAgcpYEM_BHUVKgCfIm9pyMnFdC_HK2UoOjTwj6IjfLV-FRc_9raNGni8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_6Cmw4TAyFPrehoOiJXXkxVNrtol-yQ5QlJOqGt6oxKLN2DjmMO-X-FFwXkZcJvH_2nI3rBA52EFhH5kbeI7CklL57KpkWjcO2oXPAL7kGVJSe8BCXW1tfnaezvntUWt0ZZLjDegODNbG6uTSTzzdkLDgo8QrG7plRbAbNwOfXiKVuWGfAZKr91PH_YHOfFPJ_WxxHvhLi0S7IeiTkjRX0Q1ucw_fjNgUjUq5JPFkf6wR0ILhBZSXz6nDVhMYp8S7SyKm7Vb8YHMZ6S27GzCnWAyNP2zImPkuycTBd-sVSBavs91Mkd6hmL4a3DfSJd2aSEEH-izuJypMqBOICySQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از رزمایش تیپ ۲۵ تکاور، یکی از یگان‌های ویژه نیروی زمینی ارتش برای مقابله با لشکر ۱۰۱ و لشکر ۸۲ آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/140082" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140081">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d191963b9.mp4?token=W4IonGDYsHEkblmphRvlViXGnEWLgZEvXQk46WaEVeLdszEvfzhaiXwgDpEXsinhA5vR62a-7ePzws9FcySLV9LTXmt1YtHv1BcWlmgyW2e0ea0QrL-tX1ic5rqRvMKhDkaN0L-L4KjtVztfsMG1_RAcD4PfQ3qz_zDCsJT46H6isc8HJqx4ul-noT4EdZkXdhuAVQ-PKZN8O5q1iVJXXgQbYW-OmADPsGCJXS4nRvv4MFeqzBA_P5BPWLVegsvTf_CinJBps9viKfa5llt1t3pkWePPv4FqgQINMr9RofcwckfETSGtJGy6M8RyE_zsbOUHLBBmghWFMiDCnrQtj2_5Yt99Muf36oZr6kDPfWOiBfkYaFmbderV9hCCIpXu10FcfY3FfN0ym-zbESsWlVV7TgCGmdtDOzx_YCuj_cHJQ42NJ9Hcca_f9RR9r_nEbnhjacMGp4CaReVkvqtIZjcfGcQ99zQ4fxzxZloledYC0hRbvhh1jaMGrJhXFqi4PbGu_rqAiXNq82ipCZJivPZ9eaQdUV7mtCzxAerjBMn-bNRonorTdWLx_4-A65P1_MaRjEe3DBFrPZc04ilUTM0U3ww-T-Ol0sKCo5tPlyq85nxa3X7kfqzkZIykiqEl5RXrh5HOH_MYACuGVFl_wXBO96-bKl7VJVlz6VGH6pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d191963b9.mp4?token=W4IonGDYsHEkblmphRvlViXGnEWLgZEvXQk46WaEVeLdszEvfzhaiXwgDpEXsinhA5vR62a-7ePzws9FcySLV9LTXmt1YtHv1BcWlmgyW2e0ea0QrL-tX1ic5rqRvMKhDkaN0L-L4KjtVztfsMG1_RAcD4PfQ3qz_zDCsJT46H6isc8HJqx4ul-noT4EdZkXdhuAVQ-PKZN8O5q1iVJXXgQbYW-OmADPsGCJXS4nRvv4MFeqzBA_P5BPWLVegsvTf_CinJBps9viKfa5llt1t3pkWePPv4FqgQINMr9RofcwckfETSGtJGy6M8RyE_zsbOUHLBBmghWFMiDCnrQtj2_5Yt99Muf36oZr6kDPfWOiBfkYaFmbderV9hCCIpXu10FcfY3FfN0ym-zbESsWlVV7TgCGmdtDOzx_YCuj_cHJQ42NJ9Hcca_f9RR9r_nEbnhjacMGp4CaReVkvqtIZjcfGcQ99zQ4fxzxZloledYC0hRbvhh1jaMGrJhXFqi4PbGu_rqAiXNq82ipCZJivPZ9eaQdUV7mtCzxAerjBMn-bNRonorTdWLx_4-A65P1_MaRjEe3DBFrPZc04ilUTM0U3ww-T-Ol0sKCo5tPlyq85nxa3X7kfqzkZIykiqEl5RXrh5HOH_MYACuGVFl_wXBO96-bKl7VJVlz6VGH6pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه عربستان: اورشلیم، شهری که در قلب میلیون‌ها مسلمان، مسیحی و یهودی جایگاه ویژه‌ای دارد، باید شهری صلح و همزیستی باشد، نه میدانی برای درگیری یا تحمیل یک واقعیت تحمیل‌شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/140081" target="_blank">📅 22:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یک هواپیمای ویژه ارتش آمریکا وارد ریاض شد،
🔴
گزارش ها از ورود مقامات ارشد نظامی آمریکایی به صورت ناگهانی به عربستان سعودی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/140080" target="_blank">📅 21:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140079">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdSNtT35smuJeigBYrYH6rBBSq9EZEwnjCrWSG4_TbVkDnkebCmzzWKAeiuxAEu8eafk_NtblZhli-bPqHxp-rt3wECSKUOjpBwyRYBJVAh5ay9o1mWjTFQbzaRv4LlGMxaIy04IeOeXqODJfqUW0fifPp_bmOiwsZwy9YnF46YJuOJVRov3fpWwCP7tfCi7SxWv2kPoE0_OWlnaKva2KsTE9kn8bxvbA8yVuEpx7rRkqsNaBY7NCC7RgOmA6bmerwFcRDw4m3yiCC_PAINQRbNz9DG6S1GfuD4pYQAAh_WzX7jZo_VK2UXE6AxcewGtJLje7gOzZK4wBfICGWm_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست عجیب نوید محمد زاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/140079" target="_blank">📅 21:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140078">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
بنیامین نتانیاهو: سربازان نیروهای دفاعی اسرائیل شجاع‌ترین، بااخلاق‌ترین و در عین حال مورد تهمت‌ترین سربازان روی زمین هستند.
🔴
نباید اجازه داد اتهامات دروغین که از خارج از کشور می‌آیند، در جامعه خودمان گسترش یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/140078" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
