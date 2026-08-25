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
<img src="https://cdn4.telesco.pe/file/MdqPU3XFyX9jjG284dRWlYyXGE9sszFMwzGfrpeGEXtW1eoGQFf-QlW7F5EMTivSaAjwozohsTgdaaNqMD8606iyouqbkjCwWzRLaCxTk1id6ZjSWBkWvhDetE2dd_lNlPRwKtT5KkxhxYCny0dMeEXfmufUUF3_t6Bttkbm8WPAlPtN0ChUpTTbAR72m5ttvC8tNTAZQH9_ayp7qtknbFFm7HOelLXM0XX1o3A3ofVS1AZhBsw9QommC9LiHmIkfOcDcrue_gRrKJYGnunrtY3Y9IF-QXbP2OphANsWRgQQFsU-IUgav6gw9bGyevQE7oKOXJ4su-owlKTWrU9_iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 617K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 18:41:38</div>
<hr>

<div class="tg-post" id="msg-28476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ5Rd0uQAV4rN5caG86jqR_dbj2vb9YR_3cY1BBQZN8BrPxrPJ9b8SCTXCUotBYg0a8osyN-dJ7KlEWXPP4uEuSw2SUuIqZAEx05RSom2VlE20X6uy5YNdgaa3e8DhxqzTOdPiGHDnz_tT-Xf7A645jRRAXTP_Gcnr9GYhmTmTRSQgp6oMUvoznqGp69ZjOFk1EsF31ZZqXhenDHIg5o4O5PBuo58PuR1KnMnsHf2NcAIMUGBgA-HdGohokjMnDnQpLyKIkoirgbguv_6_2UDBb9BoIbme3eVDRodbI6KVrXSPOdIm162PMc2pM-v_2oJoSUuKpU_jAjOXjIraiLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/28476" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
قیمت‌موادخوراکی‌درتنها 5 سال‌اخیر رو مقایسه میکنی آدم‌کرک‌وپرش‌میریزه. کسی ندونه فکر میکنه 50 سال‌گذشته و این‌قیمتا تغییرکرده. قیمت خودرو هم که بماند همین امروز روهرماشینی 50 رفت بالا.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/28475" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnk3B3JYyWlrfrG6V3nBHO5MZ7i0TNC0K817PpQ_VmB1nJI3MbYsJdr1ZZvT9zPfDMXiHrMHc8j_oYQSv17ln8ry2nr2RHTB56WLQF8g2vTRRR0OK2g7n8D0veFGwARWcqy1nWf1-nC8ln_SqgEuVa9yTEDPahxlWsh4W7dK1ICq9TVzkVDthDT8e6wV58W54tD6hV7gQWK3oLtNWNoqzX5wmf8-nLq_diGP5K7PzV89VIKRWp97Ivn_8cRJz8UIVB7tS0uW9BoXOuICzokGTdOFdOyoPiYau9gi7tBFa_YkhBCiZfd7kTqOHHvL-OKmlFY2fm_J8GYUd8FmnlH6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2017 در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/28474" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORzI6ODo7zsBOI1LWi_43hp29CQBbrN5V7f-Z3Ls1ehA_lc41sa8ZyhquACEFtnZvGOFJW9AjroBR0cNXsh3SBQ3LmVxa9OCv5tpNWd1tl-LaFGsyGesb90U8fYS36qKtZdCMrwSdp88WF3EbVt_QUEbOIFREP_rAKvWGsfM4t4lBNteyAB9qMvh-yjLH5B0G6OzOjQbhIfDHL6bSRGy3i2mnohSZ05Apa551hc_9UclEqdAWi0KA0hHaet2PRc3ZOYU_VEk8kmsVEcvegGVyZKbMDwfw9ed6N_5VYZPp8aDAXlbNWjDy9dDANGIyC_-CbysXSg32lL9hvCx3z0hVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/28473" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdo300fC2Ds3zh3P6s_a6KfT6X3pqInc-ULELC_eT3Sv2mXbpflgovez2K4SnVOPlqUcyOeEglbZaEOm_9rp7R-AwFYJvdMPNx0ELfF3UxIlz_ufuOPYkyEA6s81BEph3RDlXFbB3gK5o9IFMKLUmohcYC0wkNpIvqX3DYDX6VczAT7MiaE72twI3vuIMR9a2URqK-HWAVvx5XzKDE7qU6Qj8nNFF7C4147NMxwWGIAfsbded0__FBzmtcDDke7VZ7xRsHUjSRfmQqo_ZHcceLzvqQYheb3CXIWKWhH9x9kHfc4q9A7-j311T2j8vWlKBuGK3p3BR6SebWbqmofFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ترکیب‌احتمالی تیم‌اینترمیامی درفصل جاری درصورت پیوستن‌پل‌پوگبا و آنخل دیماریا به‌این تیم؛ دیویدبکهام‌مذاکرات‌خودرا بااین دوستاره‌فرانسوی و آرژانتینی‌آغازکرده تا درصورت توافق‌نهایی باهاشون قراردادی دو ساله تا سال 2028 امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/28472" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2YKDUUeYf2VdgUxExKUuFSOE9VelRJtUwhnp2u8fXpE2JQGvbBTAZRXBipqEzIlEWGT-6AMFpf0vyrc9lNPeWQs3XszP4KnloV83f3Uy7vPd4hux4Y_e5TyYkFpSHHnhG2pQ5HxDzjBSRzA3rmyCBK734OtiM-BHokKlppgXLcFlLFwY82Mbq1P10b5wsjK7lsRnvrWu1S9StRtGWaX24fNJ6uNQgF4dB_8lAD7gyEDKTKQPdBTlhKg8j2uDii2GBl8JN2NK42f4XsA9VclmGvDiwKro8dAAf2rGhtqf0rUCXzeM_ErnE_bclnrUauN0MDwbRX-VbRLwOObD0vmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام اتحادیه انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ناتینگهام فارست
🆚
لیدز یونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
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
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/28471" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRMWX9QZZs6fMBfdKWdIZLZ4U_tbP-iYqI4jcAvcGll9CWQC7tLjF4raHAYrThGrUbhiS_F0Gx2RIBbyy52nXHr4PA7IB_RGZNX8HaYGT9A5z5I1-mWzg9lzQ54yIiHMbXWObldY2-QXnFzMwwB4zl3ALRwRm4FKVI3AEjwtYtaFCSeWLYEQz7iuR5z97tRE0PVHb96uqvGs0JWZGeCsz_OCdqo7A5Mb-LZtNuGCsYG1KA6gcwOqMEYCfyXao3kKzBVw7NBQ-eixQKYE5AyBfSqEk2xKAvlR7bWFzOG-RPVeRwuxmUpMD3pIw52KL3kddhL_xjehoIRa3GBJbd-DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/28470" target="_blank">📅 16:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28468">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=dB-m3g_Qay3tbyPlgaD9XaAMLv0wYmkEZ7LwH_pNJX7BYf6jQx8fyvA1KihqZndm53iJsuYIzTLtSPnn5-bx0ZBiDAJJMFlJ-Nu8Zzf5Zdva_VXzJxtUTlrZ4mEL9INizJ2yAkKQ9w0Ap_EQxFvQkRj_EGB1mqzBi2e5-GtCBRZNEUt4RDE0QSJcNfL5lCwi8CO1ngNJRVpyWjqcBNb_XNFkxEFTYmEBX6CnVN2hLL6tRwg9TAfHq87KBLk6oLuMXdMlnZ7bLtpmOLaA1t5HDNkCSrX2i8EsmbQx8ZNi7krsWvSKqxMGwaHPTwkIhl62oeWg6NEo301Dc8ljPPp22Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=dB-m3g_Qay3tbyPlgaD9XaAMLv0wYmkEZ7LwH_pNJX7BYf6jQx8fyvA1KihqZndm53iJsuYIzTLtSPnn5-bx0ZBiDAJJMFlJ-Nu8Zzf5Zdva_VXzJxtUTlrZ4mEL9INizJ2yAkKQ9w0Ap_EQxFvQkRj_EGB1mqzBi2e5-GtCBRZNEUt4RDE0QSJcNfL5lCwi8CO1ngNJRVpyWjqcBNb_XNFkxEFTYmEBX6CnVN2hLL6tRwg9TAfHq87KBLk6oLuMXdMlnZ7bLtpmOLaA1t5HDNkCSrX2i8EsmbQx8ZNi7krsWvSKqxMGwaHPTwkIhl62oeWg6NEo301Dc8ljPPp22Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/28468" target="_blank">📅 16:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI50NP7sMVrF-bzrAsPk2D02kpd--gcw1In6IBoIMp_ybszL2ld93IU7lwTCHjSsTJQkVvG_kLcWYjz-opE-UGL3sLXgc86-9Yo-2n7PCOOec2x1hSjahZJ_bjRS_8jaPBWdspxBeIsKmlBGZ-Ixc0gRP7egvVcFHWg9fNWrOlgTNAmvQnuebkZyxgZ2qFlX5KZLP82b_YL2f83R55CS4BnPOCgSO4evbqgkYR4tlz8GkFu99x6OPGx6CwfW7w7437dzIagpchbGdp2JlBFKWBkiW-lPUL5KNJRR6c8Qm0k6VnAuEvOLJWcIGCjHTqtlmeOyFr6i9oSfTorWIoeNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قانون 90 به 10 در دربی بالاخره اجرا خواهد شد؟! بااعلام‌رسمی‌سخنگوی‌سازمان لیگ، طبق قانون باتوجه به میزبانی‌استقلال در دربی 107ام 90 درصد ظرفیت ورزشگاه در اختیار هواداران این باشگاهه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/28467" target="_blank">📅 16:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28466">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfAcRzbl2DVVJ6rQRhwOKC29dLqzQbWTM-CLxRLDCqekXS9AwuyrgjFIypJ0auLz0e1z3cmEaTVP12JGyB1E9c0G6r0mBzJnncZ4tVqDE7Bslygt6vYRVCduREZ9_8RhBcHOKhNbjl5Qnj4DU0ADEznEFl9zy_Dk3cMx9yyxHWb-yAFxNFDQ7CBxZTK2BCH0AhafZsnfyIYrcILbv5-Hoy-xZAYrXU3DvEUVk2EvQy5pBg7VyjxAuRl6XN4WXMETv2XLt8mQXMshbSec2pNc2EeCG5hnjsvPq9U83yIvkINjFcdR2OxC86RDkqnEHsy9Ubhemdk-6uXedld6KTI28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عارف‌غلامی مدافع‌میانی‌استقلال با قراردادی یه ساله به ارزش 8 میلیارد تومان به چادرملو پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/28466" target="_blank">📅 14:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28465">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PizQENhH452hQfkPXcZYvnWqNpzkC-bgG8xsSf58ghowP6vOREAdBLKc8QH2JLRK44X3NvHuuKVADvddmq49aGqx1ZO1tFkOHz--F4znyqFaO4owGiNAf0SVHgA9WvweeTvJ5Kle-7imZNJ2QnSFpOnkwPQuIlq3-ytavkzE2HLOO9eRX0yxC7Kr30oxayqjf0V0vZMklAQeeGM9mwTOtzPGeJSA46BkgsHUzpIh3d1sxhoa5MXmpMj-flgRshc-bOFgyOs7cOwUFinjU5zu7SD7H1reEH0HO-tMJL_vddqp8fp1JEFby00iw5CQFUaatGYQwT9O0YpmCgrrrkjoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/28465" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEbXo1d101R1PRAbOtdxioSzRoLKlJ41e6YV_QL6XUfKqLn-M3hJ10qLCjh4zsnBuell2Ud5poBlfsuQMB6ze5f64J8S0ocEyHF36zCYrWi4cdgqLJfQYcVdDYjKRKWDzM_V2HrJnGnT2zIXlA1RWRipy_bu4vl9mbsuMj3MtwWVNiaEg0qAveiYhAfR-F7g7_zxE8E72PFym69oldcYF61RrZSAbgdTEeRrzU0rWz5q_I_Nnkun72moiS0LEfh14HA2PEUPbssZ4YKrAnMadiVwNWGFtzrdz-hkHw96INfPnKuPxYk4cKIPl4FqtTbw9nrxUw4Q8_5xWqlmKJZw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/28464" target="_blank">📅 13:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsksxQHVakV_XVL0tSbEdXnpBuUrtiSYkQvE8zZkZ3I7CKxdqkjWrbI6Rp3Vf9H7iRHrajJsq8iGbNRjScEq1uhwl6Q8qn5pOtpOuHKJmXe64v5cHH-ZeVSSC8RTuG_N9r8F-D7OmOO36K4QJAFDng4u3TyQBcOOdyJKOTvvHYq400TZ8on7KoNBtYSToBZKybgy4w2IAS2l6gEoIK0qkV1TSNkTUOiBUp8QnnYrlCXUl9GErA39ED_T7TSbYCR_uSTDxdQLo7wuqh_gaZxUrjH9gFtoOKGCSyTxg_qWEEgHQoezIsemMd-KqtlFq9RzCDPl8fVebTTcv0M52Ka9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توورژن‌آمریکایی‌فصل‌جدید عشق ابدی یک دختر ایرانی رو دعوت کردن که همه پسرها عاشقش شدن؛ اینم رفت همشون رو به ترتیب بغل و بوس کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/28463" target="_blank">📅 13:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=PAdv1a6O92dQfcOpUF6NDm2qKD9BfV4cWzytaiRrN1SCdZR1CDaMMSe1DRbN_LxnfNvld4JX01CN_769WmYl-DZgOsJd4e3HkyVv5ZHGwtiklvjHnuuY6qXNuLJJTqr7o1VO0LIHil9pB-aZ3n3tViFXoGM2W_5WCf17BdQZikiJ5OBkp_7eqWVhpTx9m0k8QrUljeQwAea9atff7VAO5A2fS81js_-r-2zXPrWKziBNM6JR6GiLETMO6aLWxgly4blmEPJuIwQKrIMxjqBJIV5en_0lWU3pJhe8GoeEhPRWKP4AmVAD19g2XJ0RzDSI-t3OwHUMvjfVsliMYXnzsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=PAdv1a6O92dQfcOpUF6NDm2qKD9BfV4cWzytaiRrN1SCdZR1CDaMMSe1DRbN_LxnfNvld4JX01CN_769WmYl-DZgOsJd4e3HkyVv5ZHGwtiklvjHnuuY6qXNuLJJTqr7o1VO0LIHil9pB-aZ3n3tViFXoGM2W_5WCf17BdQZikiJ5OBkp_7eqWVhpTx9m0k8QrUljeQwAea9atff7VAO5A2fS81js_-r-2zXPrWKziBNM6JR6GiLETMO6aLWxgly4blmEPJuIwQKrIMxjqBJIV5en_0lWU3pJhe8GoeEhPRWKP4AmVAD19g2XJ0RzDSI-t3OwHUMvjfVsliMYXnzsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/28462" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28461">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNNEv6oJ97StG1uhRg7UnwTPgST9YQ1guS_g2I3AOh0oX11XzWc0hJsVTlDLyV7upx6QGhGOVsuDEUBjL2dAxn4NcCBlvVhh6p6Vp06lHYxjT1Vg6skSC_2oPy3n6KlzUcLza3B5vfpW0dc6x8PSA-OiotBJq_G9dkFBiDqFz5DOxc9EGFjl56TbdT0ri2RQF4z-WM_tBAvEjfdTgb8FZodqJVuTByaiDOj8QcGnunH_V83SLNO845wMeUFU3HLf2xAalwYP-1prztNBCHAf5ztG9pR-e0Y_GvI0GH68U_3_quq3H0bN86SjgHT6DpVpfaP6lAjvdcZhZAPtV1m0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/28461" target="_blank">📅 13:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoNBUZG_1oR_ww5O4xDx5P2mON7HppJPMZLUpUURlSjg-CJW01EhOfgw_W8P6cRNrz2dGsHWwpyruogB2virin0RLpPYsnqrDQiMvCKDMbtK2NMUtfE-yO_D1rntVDLdBWIKQjn2_-OfCZISxLfdY-c0tZnZw5oFEt721hDWsYNwTKnv2ejZ3uqdJbpCJwMbZ84MwAj955EzWOU8EKn_fIuGluBI8edgGTZzYiw69jfkYeabeB7TGtcKYJMr6zGQAPTR_x9kahig3qkZjpgKFyQVnBeIafhQzTvlWq9v1L3J4jwXcAeg6_fFiAwZVaDKG6L8AHJx5Ar7U9y1-lXE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDVNxOmais9WAwzUjdbhAYo0ehD5bavmTfBcngmvieIAQ_iCREWltKXvPxquIcDPhgS_fOd9deNmFq-hkT6LrKvh_--pKoXGzmjvdfjJXibMSefOsQaURnhNp2jDLrPD2hSX27ke-2a91Qxu6fylnDTw_8FEngiGZ4ICckqKC748usJF6OPPR6t3iAsoauWe99toHk04_CDXlEvOkXMT_X0W-j2EylzqTtg7r-dtEZ4My_OpHhEbgTGuQ2kvdwAKchi3dEEroenPspBl9b0ZNso-Wuc49UP_-swP3zKORubICEf04maZ_LnpFnubLR2CjqVxBWxHU97rnd53yG56eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
از مربیان آکادمی لاماسیا؛
که حسابی به بازیکنان این آکادمی رسیدگی میکنند تا ستاره هایی بزرگ به تیم بزرگسالان تحویل بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/28459" target="_blank">📅 12:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=uBp9iUEuXlDE-5dZXljoELBtvNmTDpTfHCSz8rhPpu8tbz7AQX_B8O9fsSo9hRRDFPZjHKqf1NjaHiKgpt7hYwC75LitAXEAoFbxaLRWbtQs19Y_3AKI1SxSXIbyfTJA3N0sZgelgUm7X3IggaUJcU190YO9YWuqT1bWVM0_Rl0VZrF7eYptSFo4oehETxnk9vbuell6uMQ6BCslPHWpNgnhp09_U6NpBXmqWkui_yurlZmXFNec2cWGT0AU-WXo1c-FHSKalnm9VLZVg1PgzSAHXVIzCklWw1mDq1Rz211GpojKjxrL3GW2cdtWNKNcUqTTnPUkRd6QKx45hxLSuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=uBp9iUEuXlDE-5dZXljoELBtvNmTDpTfHCSz8rhPpu8tbz7AQX_B8O9fsSo9hRRDFPZjHKqf1NjaHiKgpt7hYwC75LitAXEAoFbxaLRWbtQs19Y_3AKI1SxSXIbyfTJA3N0sZgelgUm7X3IggaUJcU190YO9YWuqT1bWVM0_Rl0VZrF7eYptSFo4oehETxnk9vbuell6uMQ6BCslPHWpNgnhp09_U6NpBXmqWkui_yurlZmXFNec2cWGT0AU-WXo1c-FHSKalnm9VLZVg1PgzSAHXVIzCklWw1mDq1Rz211GpojKjxrL3GW2cdtWNKNcUqTTnPUkRd6QKx45hxLSuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال:
باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28458" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWOWbbHB33OvQOjA5rdwI-ISUZXZQXdWnax1e4qubmMkl97PxPj7j3E-yCblDmdkJsi76X5m_VxeCdqxL2QHrLEklfk43V29p97_NxGIw2TuMBZet7aRHlGZ84QVAbo-RIsR_ILMxylMwZJJBMosxOTKRx2soZrZsAXQWv04xMswIAHQRQa1uiPT5OS2rsbzGfCQLrXCWyme55DY4qRFXQS4-7hM4jsCsz4vvk-Y7GNegpNPZVzvtmZlHLn7itaadwPePZ2czaoB6Dr-9cqiHGYyBwNdaqo5P1FD6sUJnyr-KYB9pHTVsxlk0OcDjx54E8-VgvAbb9-nSQOaUiqSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام خوزه فلیکس دیاز خبرنگار نزدیک به پرز؛
اوسکار ناسی مدافع میانی 21 ساله گرانادا با عقد قراردادی پنج ساله به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28457" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpomTTvueBhPm6U3XrKXYb2czQsD_NawdyJXTNJc9iBgBfh_39PzVWrySiqtNtRyEsb3QYrsW1Et-3gamTvnV28Jk1x11f_EN4GBjncP2ydhTST2pC50ThUj7ilNGBlTP1c2NHaHoyWe7XZT_zLejaUKXzlKzNtuoOKpCnPicFUYaceT6weShFxnbwXwFWtxdu1N-E0JGVmlh2eXSPTPPZcc4BCOcE10mXsPdIuy2j8xPBxMshxpcKTQEEKDo5BD9UIUJgZv4Wp36Ij6DenygvAiV4bmHMh2Gi0QjPsWDBuKpNOMGemtraCPIGweXUT8eS3dRtr1QZnUskl-WzqRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی‌از حرکات‌خفن‌و‌فوق‌العاده برای در آوردن سیکس پک‌های شکم درکناریک‌رژیم درست؛ تو‌ کانال دوم تمرینات‌بیشتری گذاشتیم اونجا هم جوین شید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28456" target="_blank">📅 11:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDXBIolXkROjA9yAK81s6qD_esp2vM42r4AV2NgGfgz2ww-9QC6OHzJvyot6YLXBx4Y2ff1IZegKkNKa6qbScjHN8XPROEnEZO0DLKcRtugfHXc6WZ7AgojtSaMe3BZsw9bN25yIMR-APhegG0OZHj3YgdWHfP1cN4ZXXF4MXC2ShqZXhzLo_5XRfpeN9vGjhiUXTL1bYO1GgqhhiCNB1_Ex4CPD5oAfPhGQTQ4Zkf-iMQ8xkKb_9L-fX5o4C-yPK5UgJJ0csQ766eAF6ySJbmWFHsXo7PNCG7la4FhVr8KgFRa0W0EKBV92y2ALnf3pZJPFtPUIMSOoluZqmEktSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمیدرضاگرشاسبی‌مدیرعامل تیم فولاد: باشگاه استقلال یوسف مزرعه رو میخواست و مذاکراتی هم بین دو باشگاه انجام‌شد اما کوتاهی باشگاه تهرانی در پرداخت رضایت‌نامه و تاکید آقای حمید مطهری برای ماندن مزرعه باعث شد که این انتقال انجام نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28455" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSSwp97oSVxYQfOWAyxstR8ZOMLp1oWEJdEJIz1Ntb9ubyTKl66wqfmGhQ031PZ5d0tFJ1_Y0blauNTikdVJ-8xQh5ePNo8gbqBmbX4dN3YiwFHTKC6LkwaPXobE94cjfkSSHT-3ILAsd88fgQxWsvkHwSfRBfwpmADD62uSmK6i_-dhI-tX5XaCZ6HQn8YE2m87xSzf5QGzG1Tl_olxp9hMUX1yolPS0n1Ai_G2pxLogF24_ABA35zflyY3esI-8SVFvkTrBIxb-3bU7uD_GWSpoS4piuhqDBBGsiSXCZla6PjwfWqQkXp56lxz-1tL7tX9xhDRWLomekv2HxqbRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28454" target="_blank">📅 11:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd6zkvxXo31WBVRpe4VJfhFrWbM_Q3xCP6y_Lmd3t6bmM6w0h07TfajGmkt5iSR75We0SCiQmDtqZ9lugRP2CAy3OjF1GfMXmyMc04Hy3F5o5mjHI7mgA3n50kY8aAauB12s7peQVlAFF9YbEp_Kzi7xyaHaBt04iE0gjMYuikppTNgZzMaELPLRrrVT2lhykrZeNh6z84G1UMZJ4FEZVALPuvgeiW4a4Wvo0TCKnddLT3tdP6LApdNo3mqCu4NRTidRMGJ2OTOWjR4GlmhRfNoFPytsIzUepjRCnV7X9Kl6KqiATn8O6H8SYBl9-d5JzDrXfjF-tE8wpYVyx2DsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛‌سران‌منچسترسیتی‌بیخیال انزو فرناندز ستاره آرژانتینی چلسی نشده‌اند و مقصد دارند به هر شکلی که شده او رو به خدمت بگیرند. انزو در بازی اخیر چلسی از سوی هواداران بشدت هو شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28453" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VofwhdwGw2r8OEWeeW9YmvgK-JcnlBV1qvPLfKsEXdJlvyEbXUT_CghHszMfgOK4sFsmuGzm6icmbtpL0ZkFAk8-90TT6e2Y1ujk7iKdRWDgGcGq93hr79wmN52vMZha9LWHLIegCWHM8cpCJUOG4juZXQkOdPH6D40sFAzbXIS0AC2MukjA5KtHkNKD5wclRH0onuM49VlSi0AeJCSCBNwSURr6H-ajiP-v6iaBDdjTJubke8gk75S1-QOPKDw8lxZ9_gHpOxIs6PE5SCk67vBRoZKlcPDebBHNI1U6M0L-tT18yhC7TbD-ccbY4aklAtBLAAD_8EITUrMMSNuqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی‌تارتار سرمربی‌پرسپولیس گفته ترکیب تیم‌من تشکیل‌شده از بازیکنان 22 23 ساله. براساس امار رسانه‌ها میانگین سنی تیم پرسپولیس در بازی امروز مقابل تراکتورِ نکونام 28.5 بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28452" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEHI71h6L6kjTa1XcJXvT1Rv0OQ2Auma5szL-ZE8Vkw74F-vqDJPUo8jxfTI2mPmKJ-OpTYsLSplB4RTl-G2f1K-3JSaaoujk7HdJUuT5hzCCXsFO6kpVH8m9QoGVABr9qrR2CcbYOxMSzsoOI4u13GCWMc7_bd3COH9033HSmsB-Za-YYhzpdlDl1AXNiU7ajCgR8add2oK52aQGjEfqNCy8DgrFxFrqmoY8nYbNWtB59_vlg9g9QpcO_4TDgbryW-FWcRcvL8I_79qsPmwZ4vFemBZUL187svYKbW3sq1kFaVn_jUMmDgl3Gk8wyK5N-gs5g0TqhMaYbuTuwxsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بدنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
؛
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28451" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Y09ffZwL_d7BL0nNbJ9Hs0wQmOWj-Myb5NtpucqJzHanxNCuBPu6Dxyl77RZwG5dowa6Htjlx-LWf2xiGb5Enfk-S97iZBURACYJSkGuV5u7XabFtH6tefq7tvDLMN8MpBvlvexKVeM3Yl-3w_mKO9Z4I9f5sM0aYg-4xWzeeEIMAFvES2DcpNr9APKf06bFFUt5Kw3BJItNMmNCSNZmauZ-Pc5AOp5PPCKWagqnD1dQtCUtrirnoCMYD6tZC4Byc-kpEsFu1nlcpafXQct9BSNyYHOKRTTC6GZB5_trR_ZqCKPtEt9lf_gPBpTnA1uL_uIHgq083RjUrbzRZ2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28450" target="_blank">📅 10:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28449">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=fQId0qJ3J9A1kmch8MkPspv1PKlwfFv1Vs97WoHRH4Mc7Zn_eo3jEMC0SzamRJulMCOMRLeHx9cZhVEdzB2B3aHC8kWrPO4z6SXQmh-ZQmO7kiK5BwL8w09bjSg3-8OHALvxpUfiq3OWw9h-0jdUji0no2M30lp4Gix0yzhQIxVNc-3QStHpyPEzYkYe4J4m1Kh4HGZgw-X1J9nESkOcoRbiZ24xkZmleQXvkIIM7x6J2-g5PfLglISW2Q0rcUcWsMibAcRhCpJhgfjnpGo8j12mxSjvZBrRsEfanIsbS5eQxQc1dobERB49dZ3Evw5Gx3hpZymlIliFhETfS6CaAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=fQId0qJ3J9A1kmch8MkPspv1PKlwfFv1Vs97WoHRH4Mc7Zn_eo3jEMC0SzamRJulMCOMRLeHx9cZhVEdzB2B3aHC8kWrPO4z6SXQmh-ZQmO7kiK5BwL8w09bjSg3-8OHALvxpUfiq3OWw9h-0jdUji0no2M30lp4Gix0yzhQIxVNc-3QStHpyPEzYkYe4J4m1Kh4HGZgw-X1J9nESkOcoRbiZ24xkZmleQXvkIIM7x6J2-g5PfLglISW2Q0rcUcWsMibAcRhCpJhgfjnpGo8j12mxSjvZBrRsEfanIsbS5eQxQc1dobERB49dZ3Evw5Gx3hpZymlIliFhETfS6CaAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
مجری‌شبکه پرشیانااسپورت:
جدا از شوخی سبک‌فوتبال استقلالِ سهراب‌بختیاری زاده یه شباهت هایی به‌سبک‌بازی منچسترسیتیِ پپ گواردیولا داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28449" target="_blank">📅 10:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28448">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCq_fe9vVhZC7DONZ8OQL30KQslaFZbe9DjR2PWFgIjIw5BdQkLRWX2y9_s8FKAsivkbDn_GNCFK5btynoX_y-oG24Fn2rmWsjZmg7KyL9Ub4SIRrr9pOMGoXBGqInxMVl0p4whx12vJwyX61YIPs9-pf4oc1GtarAtZzATRfoiHWuSQO_YnWcq_R2W1JJeWqtrXGArEwL5tE6FNtNJNqJ9mZLn95b5w6hpapmefcqpUudVi6IwCUVf1WV1AFAViA7W9FDdzcb5QBr9IaHXDo5xmzsMvpuEpI1e6UtxGG2IvcEpSQHrW8--BZzxwzXvL8p2BVJOptlNOyAiKqLe-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه سپاهان به‌نماینده محمد حسین صادقی وینگر جوان تیم پرسپولیس اعلام‌کرده درصورتی که بتواند رضایت‌نامه‌اش رو از باشگاه پرسمولیس دریافت کند حاضرند که قراردادی‌چهارساله با صادقی امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28448" target="_blank">📅 10:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBx22JSs2W8WBMOCEnifWfdOVQdVnfdHExf6F5Zz2-GWzx0TNUYQYP46d0KeLXJhF2eFjwH2m1W9qz2cjY1Df_dpFy8QdyLTOIi1yGT3ovjfIbkjZt_lH6ZbxKMloIK6AfRzFeEVQK3qhBSLoCuemLoO-CSbKzwophL5zKLpq3aalSBG-ZhU0pzYR_8PwITaH6EIbXpHp5fsVNJ07Fkuxvl33DXtOzEL4-Tcq0wrn5dA-RUpxjwsmTui_R_qxIdJ51TPiChrrIrmLENuU121WZnA59VMoHG6__78mfjF70Wy3IWIlFMOL4mt1Iap1ZzuzD4kZqPGb2FhABdlDkpzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uR_XJCqcsk1K3HaepMNF6C_X4YZM5sAzZ1MBe0QBp_Hc7aF1v3ZrzfsEQdBahbzZ4qR27Dl729K06OsyjORTJOqUcDJ9xElb77P4_98w5nz04xLneYYryeRJ41CCz9KiMNFgU3onZvRZgezxlhJL4O8lZAmyjivJ43FyC-s0clFx4a0yOBsw_rgnoHdzu6gtjMT-FwBXmH4sqTmsIOOSPP9p8LQANVGzjOF6XhMyv3pg11qGpmit9GgKUEapj_WQLC3Aj4ms4tD6GBbQYkG9Rwd3JCOMiv3Z-RDG9JYlL1_CNQHXkaGCUscayFe_ndrUtEG9Yini6qMToxFuxXAIiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
برنامه‌وزمان‌دقیق برگزاری دیدارهای تراکتور و استقلال در لیگ‌ نخبگان‌ آسیا؛ این پست رو یه جایی سیو کنید و برای دوستانتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28446" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrK0nfNHHqlBKFRqtKFpwdHUmUQ4g1aKpu-1XL7Lab9w4JzpkvoESHnglUV9wFwgW8u4FUlxhuInTSqB5SvvW_8je2buQZ40IMWQBk3H-BrQ-NC6UZCE7jbIKDtfdWq7HHKN7FouFls-Qaw6lOfM6oLQV-19bxnjaTS38mWa799188ynMXEtsja8iwg_0bVSyIrVtSWRXPEK-fVSQOm-l7cczLSkr111UkqE8bmvRR3jwz7ntJhpn_mAE5DtZWaKxdwh9NrnmIT4of8612ubTtSSKv2GZN7aDb5G6E2ENmRBWCAz-swDafDoObntuwk4o5hGdM6eHDupA21mcs6k1ngRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrK0nfNHHqlBKFRqtKFpwdHUmUQ4g1aKpu-1XL7Lab9w4JzpkvoESHnglUV9wFwgW8u4FUlxhuInTSqB5SvvW_8je2buQZ40IMWQBk3H-BrQ-NC6UZCE7jbIKDtfdWq7HHKN7FouFls-Qaw6lOfM6oLQV-19bxnjaTS38mWa799188ynMXEtsja8iwg_0bVSyIrVtSWRXPEK-fVSQOm-l7cczLSkr111UkqE8bmvRR3jwz7ntJhpn_mAE5DtZWaKxdwh9NrnmIT4of8612ubTtSSKv2GZN7aDb5G6E2ENmRBWCAz-swDafDoObntuwk4o5hGdM6eHDupA21mcs6k1ngRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موقعیت صدرصدی که دیروز شهرآبادی در دقیقه 90+6 برابر تیم‌تراکتور خراب کرد اوستون اورونوف فصل‌گذشته دقیقا اون موقعیت رو تبدبل به گل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28445" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0ewS3ANE1EkBq-hT1QyoxRuwpOO7SA6E2cjC6dduQ_hxDLtTS3PBrlFm_7uujTnMQf2diTtXyFSI1zWuD5Zuj-ayaA0c4yXDQWEvBBwhkpnNmcjOyttELbL_PQ735Ph9Q3sBhRoKHj-93RUw-bAgQNweWujDPYGEh-ggASNzhGGL53fio7hdCxuZUTiShrAzTaH3PvGPCVAXGP8tw69mHEWNPep9XKLH4Lp_FdcBofmGCvR04yh2lwv9p2WVaO5DPX2kprutmsm90zmufau8ig7vUDITG_6-BiwjNIVS1D_bj6ccQ18fm2IBBxh5rkUCG6hXijVKIIF7be3InFl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی:
کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28444" target="_blank">📅 09:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu60XcHnu7cyjqMUsi-gtK3cBOtBc6LiZGiVaGnGnpBpKRIBcUS2lZBHFqjKti-vYCHlgrv2lBRMY6FXB4DLpC0fK_XO0xUvjwWK7AbdKP4qOziszL1L6Wa1z-XuL2mHWZerXqsSGecNZQwLnf24fHsLIHojOTe0Ircwc7-Lwfl-tJ4itOTScxLV3DaEXv4793zTdKB6GRKjHzWLqmD-73UVC1266i_X2x9VijMCHkYdxxOuZwv0bXC_cKksuHTGdqMPcuuATClcH1rlch_0lQw16L6xb41DxFgG0N_X5QblaQ9kwPNG3F8ZSOHJBWMKRJRgtpPB8xcwJJk3vfnfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28443" target="_blank">📅 01:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28442">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28442" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28440">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sin_UIp4h178Tu6LtZftNQoTI728CQQDkkHNB-stJYaS7IZZA13POFzW0LNFMD50oZG6gEOFBxhDsMKe1inWxkrKWEPX7F5usp1CBUEW2_-BLmexx6rmiA12vDn5wJ03M38d-xZsbFcqxdPgEXCdD1GSy0BIKuI-cJrA8in5CBeY-iqeaUExDDdguwu-oosDNYzwCgLiVGLPayJNuTQzUuetS53g2VEuZOuiIMbxJOh_ZVkKyeem-yzfJDdGzES4oVq9RgHl6qSQ0ntSy_vvgwWgLoAO4CfYlaKsEtwfiKv-7bmoeLBu7roRKes8ARJPKd6JbPd-1MAQbz0KSXyQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
فرصت صدرنشینی یاران کریس رونالدو با جدال مقابل الاتفاق در هفته سوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28440" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28439">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2b0G9IUPSZZaMy2v4RelEy96DSE4E08_JlPQMnDA55ZTOQvHx3e9WKFG5lF4g8_mMbQCvyFv615hr7A75nuBuXRADywJaSIknl4JQrDJW_akbJcnLlacz4oaZoTXnrZaVAHsT5BRqnkx_NyJGHjy8IhlGWteQhBflMGr2AZjd9pCY5nkADTBBzGC7j5GgzesD-ji48sylyvp-SIy2UcbfNLV9oMdbQ0Ks18tSXvoTeGQbzfvunOwidhOC20WCvbRJ0YNON0TkJCBr6U9kwIuvkENAn_D3uDOVg5_f1RGbNmqHTsuj8QWSrULCjm-wXCg63ZO2Nl8xpvH_nxiWBqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
شکست پرسپولیس مقابل تراکتوروبرد ژابی‌دراولین‌تجربه‌مربیگری درپریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28439" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28438">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28438" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28436">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28436" target="_blank">📅 00:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28434">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8ECmMgLfhW4OwxDRLDjgrcXnTcvMVROJzVSABb-xjqTTRC_AeMXrz9Uvz6-iVq5_r8_espXrf4Ku_X64FDwFNU89mlFXIaltJlqphIelJl_EBfrv5Td1hWV0MVlzgYkFhEitCVyGWX0Ot5VFS0p9sTlWenAbg3GxijOimyw7Uh-ldp-vqSHSV_LaPt6-STbDGGPuSUlBCuClr75wlFIM09Y69dFno75sUi83enZBR8DJJIHYAmIfWpENtSotnSbv0U3eO-0vpzVaQRn62An51dFRottrxaQZ9TiQMT4Mvgi9LnnE9kKpoe31CzQ0qkClp9QZ-54Lu0NYWk9C_TiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTDekcDCMp0itmfwiaYweTitC50JNLF5-vtCAkyf6XQuG7S6FD_7DKg0zWn1bxuXXuG9kWP8r6SiEny6tZfq-9qXSilNGyLMaoFYLNL_rMEPq1NkgotaJ4u_5Qqp_Wl4EPGgygXXvMPWdGkJj8AZht5-RW3GhIoeN_oAkez2vgHTqgcR0HjfaY1aozUB6RxgjkqFQHNRopTX80EU5Tc-wCnQpa6BEvZ4wzeqM1tLuatPGs6EBR19_nExFCCG1OLdj1FzOohANs_lyyeffYQ6zMMduJdDd3VIGOOw6B0i4cmXVVJ0egKtaOyoZms_gPAZmdYshcXJfKUjNaam3uJnFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛
پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28434" target="_blank">📅 00:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6hVthQ817c9V5rc6JmFr1PnCbECe1PSZFgL4JHXCFe2lAY28f-hrCAQ5DGB_YpufW_wySKX7m9Nd-XGYPYSXOLj04uFu_iNOHPCQetNZQG-NMxQSDcC9rvTIMhG2YjbhArHLyucDl9_CZG3URv-JtlcfQbx9tJwKrnWVGCMSrOc9dULpSEpiwSJ7OfDVJvV477cbtbh5VroiXT9elMQpznZe3_aZ340Lh8kl3vjO0E_UJfnJ9lfGYEGOc2jmeMlwFpoSyaaxo5jCLEuKNmOZ-iuw91oyU9abElO95MuA76uS4RTt3w3IklSggg-W1awOA2oY9dLCFhKf_zMaU0JHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28433" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zc4QY_iWuQig7MCyRkY9vf7GlsPACX_YNJIV7E9R82LRfoG6OER0SFyGW3MqUGL_wNAgjmNgdLtioPo3b6nBZtnplVbsz1XoVC3OnRqJinRLVTRo5YM2pPdPiCZ6PgBeA6g2pF7gZMuK2d-XfBk2MfVlv-JJ0XVaNsiumDtfRBkQK8xXscKZO_5UDONfkU_8C_A4C14e04-ktAwV28j1vk10FFu2KCQLB_2GZZ87UcbfuQiMBGXa2MrOHjdlYFdOiCjp7guOQjNLBEQUqRd1d3X0k2jtprnPi9U-AKMsBIEJdbFkQf8VnzqLtiNpPdMLcNFv8ZEv7k2SBtsMq1Oigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مدیریت‌باشگاه‌پرسپولیس حمایت‌کامل خود را از مهدی‌تارتار سرمربی‌سرخ‌ها بعداز شگست مقابل تراکتور اعلام‌کرد؛ حدادی مدیرعامل تیم پرسپولیس اعلام کرد که کادرفنی تحت حمایت کامل اوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28432" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSI8lMeDBEDqjpeO4TrPf2ues9wCBuzRR1htZ0aY6uGjsJ6NV1JM5n3NQsFjxsevciNZdfgLQmtvbD8nI-7P6NKZin5djela5iSgvVYKuO0xghAeHwH7ol5quhpdH3xSs4Lws9m4yeRi0KIO4NAVqUKZKv1QVsXTu8LcdJPb0Fkyu3Q9QDgqcJgIk-jda8V5yUTN-_7zw22Rh89cNxM0F5sdIWOt9p2zVaiUokPCdktVz2HIRX4heAI9McqQiOUGZHvNix3gEjdrXT31EcFQVbnufQir1CxjyvU8akI16LpkcyvoC637NXgFTYWlMWFIY9Tj5i1DcfxEAW1nU5Ap6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28431" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28430">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28430" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28429">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pgu0-IgVUnNWRTPRvt4ip20TypY-g2W9YQMbzR6DcfEZoHyxR3h9N62WCAd-iRjP14V1y9Ilfo9lhuUmokh13Et6TarwQNMTwQh-G2Q-MSxDMDcnP1zI-8pQV8_UWUqisF6FzgCf7V1bXTqUfQgeuK43b__bt0dZs_RP8YURB4cbatGDvI9_YNhY2YOU5EX1jOlzV8CzwpkEKMA8tKVE2CUShHAM-qZioozmRT6d1_RrMYPyFp4Tj5Iu_TKLLUKzIcS4Ci3CCwo6DV1FUYbVXPfQIAKslIVFPHMxfSpu9ETlMspl_kOEhjMc9tJ14_SLw2YnJREazvVV4IPIy6JZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28429" target="_blank">📅 23:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28428">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1U99cXt9FycVmfAOyAVxLKocRjXQveUHS0HDLmu0JiHZpIqqKmmEeRR1IWSnk69L8Nvaj5jTVPkdg_MGvdYw5Gft3LgczzfZDRDQ4QRlMU9JG90R__JWjOYVeaPc5h26aiwKkt8LpklYI3iEg-ANfKKCr78Jf7UGnVLtXjNfq03tkcWAEvVh_IAiOAccoISYjAueKGsRw7f5_Fz8fgUUFvJYvkwvdCp4kc-Cwg_Fmpgvk4UnTRvhlIhV-oY8X6aaGakjWDdruZ9kJdFOVwgYjoaYB1zeWxa_0elC2MnLFByta-diHhFEy4_Eik7E5hriz9gBNVp-Tc3LhV4quS6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل مارتینلی ستاره‌برزیلی‌آرسنال که همسرش گفته بود رویایش‌پیوستن‌گابریل به رئال مادریده حالا درآستانه‌عقدقرارداد 3 ساله با رقمی نجومی با الهلال قرار گرفته است و موافقت خود را برای پیوستن به الهلال نیز اعلام کرده و تنها توافق بین دو باشگاه بر سر رقم فروش…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28428" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28427">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNu56jJdcTNbhWqlonalyeYwwqYJcRM50La9V_dKpgHnLuioVMIw5eW91iJx_Qlod5ggq0GWPBb_QxYxyvxQGw1utq9bQ3KUUeHGT29lIqFVtMFHEqcYCUSOPuOufrYEr6UO-jongczjXGXsyqhXLzIdUr8U4YGwGvrW0ODNa1NgC8eL5tcjIWWcb_tlL4vNdB1uVEtKliGdmx5u6Sr1HnhMInG3omscnyNPS3AxOYoVhTXtABfctZ8CzQ6OYbQDhZRx9ARqVHsbEwr1r9chgppiBFWLgLPjAOogHF3yweYHfOtvTdQ4XNIDgG0hsM7Cgo93yGUMpax03vvdBD4uyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28427" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1rP5hpPM5TFQmVpPSpR4sPACPp5yH8X6VDuYoGEQfBGjngb-3mM31QV2-LoXGacbeI0EnZ3Rzxt-oBlZTcIhAKE_KTgvtg5U54F7j5lk8tS4PXRubWywppfXAXku3J9zhIzLSVF7dNcxwtaWLLA-Gq6lN5iT2EmEtNwFfNCQY75vCJGSUtcLySoA5-DP4yw-fHowlQT6YJBpf3hbq5aKJytqJ5iL9fRjiFjkaZ6teQsJOkM8fAAUpiz-IDR77kwl2Tn-2qPwWYpOz9GMlLnzxOL5FBmgqBPS6WkKLFmliIV3aAcXyOlbDTjWtT4DndU_QjzMLsIrfnoVtWEnzGOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3FPs0SuAJjfNpfF7FmXSGxte31fs5a4iLhSGrmXRPbWkf2Z4Y0EmhA2IfarJIvJqjqKgt0-fhwCgFZC2AJ8qAJ03-iX71ZMQ3dawuHr6i-DltjivLIFLpjvNdyTcckytLoficwS1dCsnRcfEGU-wXbfAm5pnNBfQNd-3MefYImNaLksreEFHj0WxrMdKL1FXCSa4bVY19EUx2t76WThl0_P1Q9xhhgZ56Mzc4vJwLxkqSekniIL4nAlfh0umy2UNO_uSx3DZmX6uDOrAjneqniCtHHt4NHDg3CJe_3KZdap4aTYzDjUXx8xqTLrmywsLdZ7fwsh6yJz8p9R8CBcMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28425" target="_blank">📅 22:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiAg2r0rjkNCJJf1J1JDrHE4IbTaXjgOrNtd2rtLlsoE8b7h0j0MSdR7r3zM7klffmJRvSHhSF2y2xgQMWZJ9iH-Elgqx0cybZ6EvuwE7NCGxreDJIse4Ibaa8A0Ev6703s6jVKaRn7OI12WmQk4uKotjZZgBZrhnHqdbakFtANWCwYrbohMcqqkzXjETO__ojFe_RQ_qiRVLCULV1EApxnAuNICw8LBDPp4BCkx-mU1he1yB3nbXJLdjqvv_fRhHloe6Zk9X08EXOeHMwaylyZUHMbuBYLo3fPCP8KpYwnQzcTirhiPhapjLZkqfwaeFJMSRtDObJ7jXTUAVH7GqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندم خدمت سربازی در تیم نظامی وجود نداره. علی رضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28424" target="_blank">📅 22:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28423">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28423" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28422">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmI7kBaeBnyn5TGoNGpISAKga0ku9rdf8RE4zkytTdcdw_zAalKtSCxgDSQ5u8y_6pJ7hJPkuVRVPFoUKsN_ZUU4nc_McHyX8jxq32JOr_FjHNO0aoLmFSzRve_0qZt5B1opOWA-HDsqFvBi5JjkpQRo3oZC_T6hYNAnPtivxVWF1iVo5UlNeaJWJcb_i4XKEOsu8U2iIqj0RSPg9H2lau1LvoHMyrNXCDRkFZpyaXLbrvQ0z92Iqf5GFe-Uypl4HpwSfHJokq7ug94pNnaMoMVezR6t_QZ4wNH-U2DN5_IdiG1ZBXnTwrF7ZM7KFCZlrQFtAR9pjLrVaeiYps51MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28422" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28420">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28420" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28419">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28419" target="_blank">📅 21:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28418">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28418" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28417">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQjrsT_a0lE1I3sbSEPigjO7KH2wm8Gx49nWOuNZRpQ7oPZQOCq4M4MwTCYY2jxtRR56uhzzMpI34QIDq5hvmHEVrZ7vROMUqSUQ4yUGKvlIxUs2iv87WK5bnXnaqnf8zEH9y32rafwTK6bHAOVzALjBhRz42Ry7yP103iuBRXUhZwb9G4EcGnJ6JpPhr8ssMV3BMaeTCLnRnMn-kY9qI1FsCONsN82c6m04tKT-qfkztGjFcTyQSkLsII9dFShDih5HbWVsnN4cTBj3XHrYEjeny6kPOke6jhSTHZAQ15iF36FB-6YHUluCWHh_wIZR5wZcO28J9u1MBXDsqOwe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28417" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28416">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28416" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28415">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28415" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28414">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28414" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28413">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28413" target="_blank">📅 20:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP3S_qNxRD1eD20Clzr9FezfyUlfIXPjfEeokPSpk_El8Z3C0LE8bs-FqLD40e-rBTMs-Wz3IgRJVsOV4Z11i-KLIFxTcLEW7vgZp_ngcD-_ZEKw39VrEeo_314IG0zDHBNeHrxMifV2swwZRv2Uk7zACmT4Ciim7G09Me3Py2BuJvb4Ydn4rPlrjwztF8LalzW7dgh_FlBuTA1Jmxfk8Ok7oY-dwvQ9AAodNmslzSBi_YHSUZoYNK2-sQvzy4id00EEN46Jalxcn1-NQwbkY2YWlPaiXAiqgklaVFG9DUlTRizsselM57YviexD-nGoznsv2cXN5dOmHjhn8xbJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28412" target="_blank">📅 20:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28411">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28411" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28410">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28410" target="_blank">📅 20:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28409">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28409" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7_AzI-YrHLHNPKEw-3N6mqrWFKPf5iC787p9HtjI-8rrL8XWSGAIlu7XwStomvqtNMH3zXTGCNGzDoTKabqZmJh1h5P5KcZ1CJv6xVpx960W4EDxScsqFwzQF77KEnchPhtu4ifVSuKpgN9lBTi11liLqPtWbc0t4bpyzvDIIZccMzLNmh5wn5dgbs03HcNy1GhOBcY5sK53M20Npb_gkVJNNG9agKM0qrySUN4Qb9nQxiR3Tl3qyOX3uWZ0SkfzTN3z_8iqdB8W-QJTAO8F9F_NhqVaumClzwsxuqpSznP_9fMU7HHb8P5CKQi4wBiYLT6yvfpf_lQY2605SBq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی ۱۵ میلیون یورو؛ آکه ۸ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28408" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2y4vJdCHc-Yxusr2tFVqpmZEfJ7V5860GdAUnFWqflBEcOLhcavMqhdjjK3QsMpMlErYGG8DoH748qXf-eRzTperH8F3x7fdqYkmhcaH4T2Bz2KulYzodDlTUFx1UbG9gB-mmnl-Lek3XCxczs3iRAU8pUdTAYIVZg8NHV-RuIPtAVvWzUxAdwUkcGNkj2qNz7sVS98BwJs6x3WkicFypy6RRRp1haBmxUQjGiERQLfw2aVVrj3Ygtit395RubLIfviYW0K6o3Z8Wdtn4dx5Txw3NkUI1pL3MMf-Te3qQeGo_z2mivUccZWpP3AxC6ArLLaNtxIGtX5s6EuZvrLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔴
🔴
شماتیک‌ ترکیب دو تیم پرسپولیس و تراکتور برای دیدار حساس امروز؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28407" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtYRBrB5T6pf8zEL659FkIEaObNOLz0IkWUn-G5oUmD5q2lO5llF4ITid_GV3asnb3BQcyvnliDWuNNuVn9kiJSMtwSyjtTHcEF7g_U2EURrTtyAX9KXYulOEd5-LK-JxG59Ldwmq8L4O5XjtOFJvajxtEJ6BUiPkS4lLIWxixMwowa5UfYaw4fLRhVMpbtkBBHIix5rtZgCUIoAV329YSB2li1WwdS-O1RsbI6zGeJxNQ9f5oRSfvn5bL2X0YHuGKlOF-xUReRN3-A8Xcz-695EPYDefu5sd9FUaYbln3GdwR_IdzyF-YQldEADrtXRcSfnYk46bF8WG62EIY9ajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال طی روزهای آینده 70 میلیارد تومان به باشگاه ملوان انزلی پرداخت خواهد کرد و مدیریت این باشگاه هم رضایت نامه بهشتی رو برای آبی‌ها صادر خواهد کرد. تمام توافقات لازم بین طرفین انجام شده. بهشتی تا نیم فصد قرضی در باشگاه…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28406" target="_blank">📅 18:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7DMy1edn5B1_Tyu2WlC200nFNBhHRI2a1z9boatLktGmrjS-x_ScHw5ac0nfLHPJkK_FUlMrw_sjxrsab-y9kH9NQJRv1ajhEwFORQcYvSjqBQXyH8-lpyAsIgubOBn1bJW69T8BIASeWygqJaZyBw-S5zv1JlZagEIOpSY5Y7XKBmeZZ-SNn_xCACF7cpLUdWLXKYsKmX1_LXxqkDn_9grYVdpGgwMBUts5OrSvC7UXKsi9x9r2Lyxw1Tl-MqFa-IsLqEZONMAP2glGZCRUWca2q6Oi2hy3LyNJ0KCH6it0ZJ7_5lP197IeqJsDnM8BXMocFTQOqFH1ow4-EGjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیاناتوسط سازمان لیگ
🔵
بااعلام‌رسمی‌سخنگوی سازمان لیگ؛ یاسر آسانی یک قرارداد دوساله تو سازمان لیگ داره و الانم داره سال دومش روسپری‌میکنه و قرارداد جدیدی منعقد نشده بنابراین هیچ مشکلی در این باره وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28405" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28404">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOtD342LEC0N-lAiKfy99ugldUCKyrMI2_4CyiE0Ir6Ww65hlfN7XTVsZUi_YTBdx9tg9Tthrt1hZHIJQka7eEMzN0PP6iaqqdF7KrhbweTMXqBkHhisqsr2m5qTj5ZIeHUrluE34P4muGUnX4dNzjXI9LH3V8NF4HB1jl6gYYxpkEnxZ20HRxLxsH2Dz69_XtFeMNvNj2d-aXd3PvEUVWMXAczhZ0slO2b7jIjqbklzakKcbZEWc7hYjoVUv_QYae3LgnzMhKuZnfXozWkCkPC4HkgZSekx2aKTL22ajL1MiB0SVRu_iL-yCOnnrOwv6MwUum19NMD31ErVPIK3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آمارتارتارسرمربی‌پرسپولیس درتقابل‌هایش با تراکتور: 25 مسابقه، 13 شکست، 10 مساوی، 2 برد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28404" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP-wsz8qtszs4fSfmPZUl1-Rdl_2YuUz72D5ybzAOgDO6TUzmKt-3YZdiPp9KwKtno3cghDsWG5nPoiSP22IV4M1pFA4sJwAE7gu5uBRgPCqtZFXM435D9FuGgNzZSChtiOkHBJPEvwylB-LZ8RW7sZMvt8tNQsnXk9x067vsFO3Nb9FHzp4vZYP1ndJ57WWmqovyGgVPZVoCX2qzef-aADqdkJXXd_LbBFIYtROP_yk92wnPzeijh5cqLk6O0KxI38uciPAIC6q4hKfRD7uqjCIKAqT7S6GArvd10gUxr3sc-3MeKjf3Cnmb8qMnpHtRptaPEircBkNsBacu-zl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28403" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28400">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNcu81hfZU_ZgImh7-yVsE0_pJ_IzfUFuKISx_lIXCce5rKqm4t4FLiByZxwkT2NOGYIYeMvxU_ANa3cnE6tJvWQir9R8te7vpsYZZrlr7i_pgPRoG_yB5eGmcIKU-kzuR-VK7ADM3lo299vMq9-PAL75lJLgOTQvebiRxdOYJBW0JoL7Go1kvW0lncn0waEoTJ4xKDwI1YJN0jr5Xu1JBOB_0Hc-cDQ0L-zpHRUhH8bBcwt7YVhlnRSWYQSVLFEAJ62Aa9x9eZIs11AvA4ByRImcGixljN3vp1OXR2qzIsVYPfaboD8Z2izWk9kv2bObEvQyZKOAALklExlLqJavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bH9NT88PZMIWcWtzl1NZ2rh2flAdLxORlj7_ufZjlyiAeqbSERqtMs-WBZ9d5uVHEi-RhipsOnANaUBJzix6Q8_x0G2KEz6o-G9S94s8_ylsA2kpueJMO3oCyCfHvqbqYh2xlu6WXTuSok8gi4GbgVgOaLGP5SYm4Kq-Kec9f_fy-kZc6IdZ6LvR-GrevD3_YkE7iJN2nR8ha0_QZziKNbGCdXvRmtAhSBqawTOVHMvcbZYh6lVQKj7B7LZQ6gusIBZkUlDz1pFZ5wAgoJV4fU4CCXgadGg04rSsbRUBJcIz-CvEjSxzYkmHNANv8wSXQpIS3AEollh-mDVb0IJD1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب رسمی تراکتور برای دیدار حساس امشب مقابل پرسپولیسِ مهدی تارتار!
🔴
علیرضابیرانوند،شجاع‌خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28400" target="_blank">📅 17:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dof_vlxENRZuPE3I8-ZXZ5ko7LVGp-iF5V-IvvCitxeiBNoaK7bOdPv6vMEHzQ_dBPkI7u92SOHuO8qn92EGEnxxG3F_hziKSzScJ97_FOYYhxS5hweox0XEHnKMvp2nr-LPxhPBmy1CnWHriV_SSGeTWlElLLVKBnGNdF7uMVYY7MBTBbjv7c_nOHXmWTG0BZsfqDWyGXVYzj8rpB1uJFPjht2lTimZfWeNW4UAashGRPop5ulQ0HWiqcehR0CF0L_-pMrOtph_KhEy66nN0Fgu6a4s2ElslGRQnvOWVO9i4FOXZa3r1HbNwjuWic8vv4r-EeUpghlw4CnNNQXjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28399" target="_blank">📅 17:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28398">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqs7T9nnmq2dExHainy4cGlbNsKpahwxiShxftCxqcaq92nCzF2w3ktE25eXghg6f7nrgFIOw9TihLYY32EM_82dzDQUWCTo1frQ-T_QbqGZAG8T1KBePg2cVaF3pxOSsj200IcxQXCUVeq-PJdTU-yD406YJkEVgi-QnQ4W3DAIUQ_234QlNH1VXTH5Ya2V2eKA4INqTAQmzBMANC2Mt4XUMwPEtZ1ZgeSbm-XLUCwRL4YVlOJDgBJu7LmDumtvow13JgNu9ZRMrz-a0e6GKctgWaeOO3HUofmlAYLU0z1RfKzZGyKAuMvPau7Hj_Oa0Icz5V9-0SunsaXr6cB4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر؛ ترکیب‌رسمی تیم پرسپولیس برای دیدار حساس مقابل تراکتور؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28398" target="_blank">📅 17:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28397">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJiqDo2cB3o2RnVZjiQ1P12dcCDtkrrsrtZUq8YJPFqKpVuLg1SPR8i0y256L4af0zZRISCxqtLCJ34jsEMCXARYCmF1JcrrM-rEDFW2_LJ52wwhzbqnOwuUrOovoc2c3iNTC1b5Zg3xM0uHXSxYIn59GCAgut-f3aWz0ErKgHAweO0tKg3hLd6mjKhHrofBqW_TqIkKKhhFmVQUvpbl356xLG3wZjUw4u2779kYS3KRNiTwNsBUsAOHr0RhixQ_2_yKBWFMpwjHME7zaz6HzEbFiQJlm0F-Rkf10EHTH86aZw1oHFvmEGG48MMux9gjyqJpkRHZkVSBGU8ho3sSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب رسمی تراکتور برای دیدار حساس امشب مقابل پرسپولیسِ مهدی تارتار!
🔴
علیرضابیرانوند،شجاع‌خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28397" target="_blank">📅 17:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28396">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTm2600wOY8rWgE70ifZQL7C6Y4Qt3CfM70getlvCtJ59Mm6wi98_EkOv3IxckuU2ZClCKp6mztDw9Jd2-O0q1dDzEW2kYb5a8TQS9EFhEjU02Csg-bBpUVqopOxH288vlMLLl8wNITkq5UA5xeuOrCSSvaYxhXFGa-bI0sOgaMF-Mi9WjNWTRspEQskb0KP7jKWEklk3GwGvguFsuhr_9NF7Oim-Qe5rul473f2-MLyaIUxGA3LrRAxG7ixMBeZ_1vwt0Op2XKYRmnmbpf25yp_2BJBGcmif3mysNTJ-gxsiJhq7WR8QhVOWUPUcN6dLFEHknEtGDK4yrp-QS1NHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌هااز تبریز؛ تیم جوادنکونام فردا با این ترکیب بمصاف پرسپولیس مهدی تارتار خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28396" target="_blank">📅 17:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28395">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebi-EYwt4SigHBNY9Ex6bX33S48qD0wGtks9bE5DoBnjpDrIAGwZSk1rxjDoHOXwDXbi-esrMyE4Yc9dnxqeg9nxVXKib2wOt9EBbX1NRIhocv4z2pQADZqAJCudpAOb0MgFgRw4uYV4YI3RFh3gPs9kqpHD2qOsjfYRVkVcu27lu7rT0QrDgN3-7Mh9iVzLHvmY0bSiYBOafz11X4jhbwvNYRFfS6_8Z0zvP4SnVTux2qLZ8oSy8TUKc9UKe6Put6-_CmTRvJt5WX4ApHtreKGdsBOsH3_4wQTQdmmjJQIknZ0JgnGrmXA36fi9MKbdKCsohLOUTcBQBpFzVtaHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28395" target="_blank">📅 16:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28394">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiUuKyCyxK99AYRdm14JgmcGK00cmudhlUPxfXsEv0EDSVgPRf2VkAomrMiFM-GI6GEqf8kfHWvg0Ll9SsfOZZHGXh0VPIaLolpkpooGEazHKgUkGfm9FFBVY7b6JxULRUyPaxBlebIL_sAgfRMKN6NK75Fh8WhtECERmsoWSuOTpIzmI2Y9iG8tjStSHCCSi-oaYcD0KSIZ77aB_iyyItuiFwFKEwvXWNXSsm20geZ2bZK8poUYo8sxV2lbBrlaPsqpI6f03bIVBKjIAkZZbPsjL8PrwDchyHe-VMoKV8w-2icSJN2n2Y8FLC861nCjeNwF65I0WXduHbMycgXvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28394" target="_blank">📅 16:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8AjevGJlvsvRdl5niNZ5HaHoNcmHpna84zv36zTsrHjHawbJYqLmtTBjja-Ee0FHRBcVLWc0g6VtArnCIZYo7KY5HGxcAO3N-SZpLkN2b7CgvzHxzOXNHjs1wb2ba1iaGp-nJrluHw8Pqw2V8LbaBrzeWJ-XZJV1rc-WtjtTH_IyXobqTVtWqbEib3Ncl1tQCrHGgh8GMrBcEDsIT-vmj-DBVjiclEtFfio4Nc1K3Ve6Yn8D6RRABEHLJnE03AxLcE-scA4iAEp12XwGZ8L0nQ00Usr5AkM1x4sV_bpdkl8UKdfe4PlLah736Lx2XQV26hwv9PeNVhrztN7FX6hPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
به مناسبت دیدار حساس امشب؛ تمام تقابل‌های جوادنکونام باپرسپولیس درتمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28392" target="_blank">📅 16:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISnhCXQqnaolV7FK6JzHFgpci4JwJmWYJS1gaud7YkKnLDGqKU1oNjEztoPtxFCMP8AyuF8Ck3gEp22Qn3fU5uFVudhUn95aWCRPlv1LcB8HlG5yWsuwg6GgYXJQOZx6_aahB60mav-yrWPXVTj8jqdGVeVJ4DM1dfR-tqVo09dWvxnD2ZmyY9EWZWfzNqMK0Varor4UYhP1nh5jNLiMFg42LwxZn-OWjLuv6a3Wiyzhu98hkWeP0EY12kzcgJSMclFVkLvOGKUL_1ws221U4VEOA8X55k09M2HOrWVzcZB-G5ZeXab-oBZC7AM432dKyiriI3IwsP40tUVmTWkVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌تراکتور به همراه نساجی، فولاد و استقلال‌مجموعا ۱۲ بارمقابل پرسپولیس قرار گرفته و آمار دو برد، چهار تساوی و ۶ باخت را دارد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28391" target="_blank">📅 16:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6PVgpQycKFGV6g3w_OWp6jjm7hJFjwb8S8iytJygnPUU6Ub-Kt7WV2UlBhodOKySflEZQCRALLVTLA89GDyxMSxfFpxFYK05bJtn-6_8A--GNJ7rY049LLGlSrVdpCMmSvM2Qp82l8LCJvbmUhfmWG-uvJycWGHcCVefrYjsds55Y59Z1wIEfZ_-E8Gut6fuED2B0vfnBuwIETP8da7bz5K1Bq_Ec_6MRO7fOEaxUBkFC8wRWRctBdnXjD_uC7kO-izfHjqxr9X4sIwaVDFV-Dx8FQso7TeQuGyrV9xLVjqLrKlaraOtbsRPg7YEQ4Us7pXnTfh5xnmdRLoDqCklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|اسپورت: فلیک به شدت علاقمند به‌جذب سرهو گیراسی مهاجم29ساله تیم دورتمونده. سران بارسا قصد دارند که در ژانویه مذاکرات خود را با مدیران دورتموند آغاز کنند. گیراسی بند فسخ 50 میلیون یورویی در قراردادش گنجانده شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28390" target="_blank">📅 15:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfc5_rJMx1AisLmVaVBVlAR5LMNEok33ZZ8izDIn8ZU433Sda066m0d1hZXsI5jh9hmU9JjO6o6GtLfKKrXt6AoyD0p_V13sV4dO_BLSnhovCizOpMNMzwVQn4B8rry5ZqK2nzxJ_lhUQfnQ-XarAtsiPWNF9HzpbrJs0N5GE5nI8cxAE-w94683jjbYXaV3ALY9qyqtJAYmo_r7lV2BymaW1qHe-Ec8_bm5iRcQa8nqaMzLwF0eLUGNSnmztzVwYFJzrngkJ-ynKd6WG03qcfOhsI0OInUJmuI-PvFRkTsUYDr0-mk9yWuXnwufVGrUZh6Iw5qN1Mj7onNvz2YvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رستم‌آشورماتف مدافع29ساله‌استقلال که در بازی شب‌گذشته‌مقابل‌سپاهان دچار مصدومیت جزئی شد بااعلام‌پزشکان‌این‌باشگاه هیچ مشکلی برای دیدار روز جمعه با فولاد در خوزستان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28389" target="_blank">📅 15:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRscp30qL63R2Ht2UZViv9ut_bO-QYFOzenlAigXqjooHuaCJSd0ITjfE8cHN-xcHB9BUOZDO8MAGSkOLi5_lC1lxCZ3Pz6fw-CRsmahqcgB-R6AHHA8Iu4jg8QBCNCumAxIZ0XFeGDy91Ya3uE31Lc86sE2chEpGiQP2n3txnwFHxtGi0KZsxj-rWldELeThO548_T_7AC8JZXZvUfpfu2zSly40p9u6NHTmesjQN7ABw9diqWm6VYvR7e2HRX0AUADmuqDtWUdKLd25mjBcSdDuNlgfuT01qIidH91CRc5Gw8VXe31tOHgDwsm2I7xYut6t1329Gj-RHl9MQcpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایشون خبرنگار باشگاه الوصل هستند که از این به بعد در پایان هر بازی این تیم در لیگ با مهدی طارمی ستاره قناری‌ها مصاحبه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28388" target="_blank">📅 14:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTd6rLfvn1QNTHgY-zCCjg6ZppzLln78_mwk-a4rFwUs-YyWe0reYTfgAtZN40SAPMeeXoI-e4bbACkV9u8Gc3KJbI3_UPAk_kPw6E68lSZEOgb-XzGgrRkAPFFZboK_taY2hp7prNR_h_4bC3ZREUwBEZKVtoAgEDpX90lxG9IWJ5M9zI-zsRGA7n0E0qgRDa6ZQ59Vh-UwGtG0QGTdLFl_dkFksskoTGpfHvXTQhDHpEK-uk6hei6O_8-viQkrCXIWrYeyw7sX17Y4sraOAO1X-fnuple0Q7eP8w4Yho97UDEZTids4A94SaEeHT0tevm8Y2v6JwjDQRmLd0bzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خلاصه‌دیدار تماشایی امشب‌ استقلال
🆚
سپاهان در هفته سوم رقابت های لیگ برتر جام خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28387" target="_blank">📅 14:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4ca0f39b.mp4?token=qE1JHXnsrxZP8XuOydj1DjWbn_5JuWpNXgbeKzeHFFLpfvg4n9AkUwp5qh5q-xYczGRQoUG1fHi6vS6lNJJkPOr3Vms5A_OD0r7Vfng9fm6eHA94-YhtV16PP2INYXurzTWCjillBFJq-975NaMoJsa56sWAbYPvP8Ms-XZM13JI8CuYXRW5XS2POz9iO9gx4mo7WqWW9MSN9ux4K0xsrSIvqcm8bXKn2hAdaYqPFBzIOHoKlxKZGwHHlT7TyZ_NQMMgGbdvRUkiF22g0VAk-PZ9laW4rycUbH13uPS-SOA3PoVSuV12NtYmX--JvrkCGkGtJc0rKa_OumjfYbCStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4ca0f39b.mp4?token=qE1JHXnsrxZP8XuOydj1DjWbn_5JuWpNXgbeKzeHFFLpfvg4n9AkUwp5qh5q-xYczGRQoUG1fHi6vS6lNJJkPOr3Vms5A_OD0r7Vfng9fm6eHA94-YhtV16PP2INYXurzTWCjillBFJq-975NaMoJsa56sWAbYPvP8Ms-XZM13JI8CuYXRW5XS2POz9iO9gx4mo7WqWW9MSN9ux4K0xsrSIvqcm8bXKn2hAdaYqPFBzIOHoKlxKZGwHHlT7TyZ_NQMMgGbdvRUkiF22g0VAk-PZ9laW4rycUbH13uPS-SOA3PoVSuV12NtYmX--JvrkCGkGtJc0rKa_OumjfYbCStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال
«مرد سه‌هزار چهره»
به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28386" target="_blank">📅 14:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28384">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnPTnXJNgQW9iFsPRNbX7WZ9j2QMUWPH7dMO2PyWhg0U1ODJs0_owJ_hTsYX9RkV3nJR0J13o0wouBNYpVa9K3oqqBiuVXSo1HCjiSAjzXyrl25EeEKfFP-oDQN1wQeznZCGo68X9Vs8PxvJe1lhy8t8it4I0Otdq-FOqFlZynw-LaPIcbvxA-LUy95DywOYaXJn54dTC_0rjUAwz-bdHq2vZJ3sdibF8UaD_2B3O4RI0i-QScMQR7HlZfCRvmQjovZTOd1I4j0S5kVeOzzQeMQKLyw5UhHMaX4WIkZ-rKeDtPyyWmIDBhlhhNYVab_RbFsiMBju88e9dkD_s1kobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران:
دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28384" target="_blank">📅 13:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28383">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jzqtojtma4YJL0ZngCULzXaXrnvWg1VHXazXBe14QuzlT1X0ygOEDO32v-kr2B4PLWknU_BNTMQb8rCDftKG3S7i3ZyHIM9tzUO3aeBpvIQboovBbJF8GB7aG7sw58xH7QO0fKhsVfsJHf136Jr5vbEZmAg7ll-4qB0Y0X5MAjWm_H9cFcw7s0kSlvRCoixQByPL5EjbAHtSwM6Eo19r3RbfR04BCpdnpasQE7SsH5TzqKNPPI7ItK6-WNQBmn0yebH3Qha0owNCTbw2Mvi_P2Pq2G8VQRZtSrNBJd4ltuL0f6T9mzlNuCLG9hSvjemF8LL8CPKA5Qq5rQvHhb9YkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
عصبانیت شدید هواداران اتلتیکو مادرید از خولیان آلوارز؛ستاره‌آرژانتینی‌اتلتیکو دیشب بعد بازی باویارئال بدون‌توجه به هم‌تیمی‌هاش به رختکن رفت که هواداران اتلتیکو بشدت علیه او شعار دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28383" target="_blank">📅 13:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28381">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZfiPwlnjM5JFnECBX1o1qcRN8F2bMKyjdyDv7E36MrBd2nhDJapJJy7A6WIcGsJbc03o3YCUJb3R006X-Nq5ijiBTcMa4-4Pt4hXA88zyUq5B_QsIDKWQSTrSkH6kH_a2dTXfBp7NQUpu6w_-YxMHyoRX7dplpSD0bPiQTM7KFrg7TKfjvWK1vk2LhuMvrbRnkU-bhKsFvCT-Vd7o-Hu7yeW5cY7B11zUGeSLZ6rBsbcHH_H51wDcgpWkMVWDhovUj_e37_BvPWz2qwc0d22gkZaSN113CCymK6WFEk3cXVMePSD5BqGVXYphuwpEGSiwJjImvUaKRzklhEp1gA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emYipBbmXXAxDQPFp6BI_7dFKjewpb1zpxj41qtHtqav5GZQqw2wWTdOsEjFqva1TvSB93er63zKmMrY-fk64PWhdUWruYuh72zks6D-HO13mvVOlR6oeo59jRyL2P9sp0euT9DWgJEkrW2p6zdJPoF08Fdj-7l1OMgI65axkkmP2sQy_WleWUpjZkl3upKNHHsOUAcDbTNOE_zNA3Mg8mNDNVvi4HJxcswR0GDEOdTo5Z7iRkpqWPLNyvo-ImOEmUopYm6HYctjQgS_2utkc3jOyDwpQGsna9s8N7ipxpjMchK2xLnJg0jefy3SqePsndIKSrZzIii2gCj69FsMxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
رافینیا ستاره بارسلونا که از ناراحتی خولیان الوارز ستاره‌تیم‌ اتلتیکو خبر داشت دیشب بعد از گلزنی این خوشحالی مختص به آلوارز رو انجام داد و به نوعی از او حمایت کرد تا روحیه اش رو برای ادامه فصل بدست بیاره. آلوارز خیلی دوس داشت بره بارسا اما مدیران اتلتیکو…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28381" target="_blank">📅 13:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28380">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad50390910.mp4?token=ZWq-sBoSHWP5LGjJDmKdt6BvQHVw36gpwdWx5EKTjo-6_iDuTLxi0KfzXUzmlXucFXLAiQb5gunz03zGtJaRbS72ksnlA3AnGbBMc_CG4k94XXxDoPf3E-xdD9IbDUoCkKRTioSn5n5lCrLzgEoP2TJRJ8hnOP1zJv0RXLgLjA20AJudNAaajHQWeqg2KUHXRo3Z8WGnDvCd4VtmbWxOphjaMUKYByFIOpH6R6-cxWfg6gL5uUW7OT48wct9V-xYKBWBSF6IhPoSj3cfEV_GPVrVcfzbklTuChl3jrR9VPW7FIbCXf68mTf_5w9WZFJH0MfJvY3cecIuguG2zdd3RIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad50390910.mp4?token=ZWq-sBoSHWP5LGjJDmKdt6BvQHVw36gpwdWx5EKTjo-6_iDuTLxi0KfzXUzmlXucFXLAiQb5gunz03zGtJaRbS72ksnlA3AnGbBMc_CG4k94XXxDoPf3E-xdD9IbDUoCkKRTioSn5n5lCrLzgEoP2TJRJ8hnOP1zJv0RXLgLjA20AJudNAaajHQWeqg2KUHXRo3Z8WGnDvCd4VtmbWxOphjaMUKYByFIOpH6R6-cxWfg6gL5uUW7OT48wct9V-xYKBWBSF6IhPoSj3cfEV_GPVrVcfzbklTuChl3jrR9VPW7FIbCXf68mTf_5w9WZFJH0MfJvY3cecIuguG2zdd3RIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌ای درحاشیه دیدار شب گذشته استقلال و سپاهان که لحظه‌به‌لحظه داشت عجیب تر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28380" target="_blank">📅 12:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28379">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=F1QygALVWXvv1Cx9Q134O5m4kiwsdHxhnbn54G3xT2ju2gOwIgQNV3OOLBQqh3cMflmnPcmnESoybs6hb4xGxhHRlNg0V-eyF4l5WlcQMQIt7t9FQdFk07wK8TWgCuZq4BBmCnsLkY6beFuTBRtWpNnF86xPqo0wGFzAjrabPKSXJPa6tg4e5GXrH-E9pUb150ClQJbJpHW98mnHeQuzgY98ANBizNcmDV50LJ-CnG_gqM4ScRZCeeTT_b4FKdCcbuAtOfXKfWEP5pTs6CDD8-0U4cNa4Bzvh6aZkbsS0XHbdwJylncXVPgEhOvaDZSNzvLv2ttIKLD6HP_gzFTLloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=F1QygALVWXvv1Cx9Q134O5m4kiwsdHxhnbn54G3xT2ju2gOwIgQNV3OOLBQqh3cMflmnPcmnESoybs6hb4xGxhHRlNg0V-eyF4l5WlcQMQIt7t9FQdFk07wK8TWgCuZq4BBmCnsLkY6beFuTBRtWpNnF86xPqo0wGFzAjrabPKSXJPa6tg4e5GXrH-E9pUb150ClQJbJpHW98mnHeQuzgY98ANBizNcmDV50LJ-CnG_gqM4ScRZCeeTT_b4FKdCcbuAtOfXKfWEP5pTs6CDD8-0U4cNa4Bzvh6aZkbsS0XHbdwJylncXVPgEhOvaDZSNzvLv2ttIKLD6HP_gzFTLloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه بکش‌بکشی راه انداختن دیشب بین بازیکنان دو تیم آلومینیوم‌اراک
🆚
شمس‌آذر قزوین! اون یارو تدارکات‌چیه به قصد کشت زد تو سر بازیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28379" target="_blank">📅 12:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28378">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk_0dQyJZ_1cDetAsxqNBLZhtLfPJqsZRltsNBhQWMpY6tgXu3YQw5s8-sU1cFC8y4ZtsjnHl5U5Nq-Kmu_olwG-FTJLe7yKcvL4cjv907uoIkWDuKarde1xlPt7tiC2kb_0Xe1gVOGA0LSkLftvLh-ObtiGbz_cewqDKmeenvoSAYFCsTeLMuI-8zafYMNlpq1hoEh3hKVELRPDhP1-6Ahyfka4nImabR86dwy5afMc4-QGkJ4Aqdzj4sZDfIXWO_9oeB40rP18Nv3jHFf8nq99g36956LPyjSyhLONReShgiMNMgSR8slA6pdQBOXcveJaQuIBCVV14RsKemRfnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28378" target="_blank">📅 12:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28377">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a084028cd.mp4?token=Wqf_nzPxwQopUrK5I1NSmKTPqOeSclQpMQzpyP9eeLtm_YSQ5lOjIquA5dX98RT-6zuYEI5kO3FEExmaS-cWYc05bhqVAtE_mW8KUEAKeGx911iz6Lk9DGamKdmN-F4uLCPM2IfKH0AqAMfqDey7fpCmPRz-lfD0bx6_31R722qwUeezUVB2zgWD5gFkxWABVbWPPFNhr7M1qvt4KbyBV0QGJjZQ8l-3EEzI40HGZWGqlqqa4XFLzYXUX73ZghIzE4O2l7mMR9IpUpM-GVBUnTRFU0opJTEfW2NRWnv8ZbpoZ_5iU0ThSkTbhRNld7kWKhsSF5AJI41ETyl1w6pBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a084028cd.mp4?token=Wqf_nzPxwQopUrK5I1NSmKTPqOeSclQpMQzpyP9eeLtm_YSQ5lOjIquA5dX98RT-6zuYEI5kO3FEExmaS-cWYc05bhqVAtE_mW8KUEAKeGx911iz6Lk9DGamKdmN-F4uLCPM2IfKH0AqAMfqDey7fpCmPRz-lfD0bx6_31R722qwUeezUVB2zgWD5gFkxWABVbWPPFNhr7M1qvt4KbyBV0QGJjZQ8l-3EEzI40HGZWGqlqqa4XFLzYXUX73ZghIzE4O2l7mMR9IpUpM-GVBUnTRFU0opJTEfW2NRWnv8ZbpoZ_5iU0ThSkTbhRNld7kWKhsSF5AJI41ETyl1w6pBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدصلاح که‌سالی 17 میلیون‌یورو از ترابزون اسپور میگیره در اولین بازی‌اش برای این تیم چنگی به دل نزد و چند سوتی داد. بقول حسین حسینی از شانس بدش توپ هم باهاش همکاری نمیکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28377" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28376">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔵
🇳🇴
واکنش‌های جالب جک گریلیش، پپ گوردیولا و زلاتان ابراهیموویچ به‌مدل‌موی جدید ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28376" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28375">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRy-MTjj4ipUjT8EdDOyWn0tbpsEUBYgKifGXx0Mo2mv1StxH9n8MfVXgQAQg7DKrk3UlJfE91mk52tfirEr1xV1iogWhawRdjrml9ZIKJSGSg_IKW82bZQ2hBPF_VKzkffPX3zgroDB0xp3iIdY0Fq9-D-t4wRR-y0hRsHfDaFaa3Yae190QqBCDA3UqfrlfCkzVFz7omR6cdSUq8AzqL5VNrVSV3l9-lR8sVUMBIc8X01g-VUIFd1Hxo5zSVArnh57W9mFag9-oYPVLHAr6C9On2xgczojfc8_KirztnMAQofIO7Vhi3glHYeYxP4UKwrcFWAHVvhj_L7ZgHNnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
عصبانیت شدید هواداران اتلتیکو مادرید از خولیان آلوارز؛ستاره‌آرژانتینی‌اتلتیکو دیشب بعد بازی باویارئال بدون‌توجه به هم‌تیمی‌هاش به رختکن رفت که هواداران اتلتیکو بشدت علیه او شعار دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28375" target="_blank">📅 10:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28374">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnREGKCbfsCmesPsg89mZnWYKAVleGpFaYja6WeAVkl5bf06_QjOwyIzlC54rf1v9tZdRv9EY2brksvws8sHC_0oHMJmxECnJoVjOiKeQ44xteT0A_5E1itJ7twP2s0euIWXlvSCIC4_hnNOdFOHvzYx2e9niGEJwTQK8kCSE1lp6BcPJ6SUqR6voRq1tSpx8DKMQN9_jqZUejmOTIJzUB1z3vKto-bPyvVrznj4LrrpfNouhqAiJnSUUdytiuDpP-BpTqjyyjsX1fiMZHJultztumPtreC-u9JInHQwNnnciFCVY8kL0vblC_2ANIUVmxxDNlrziRp1qjls0kKFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28374" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28373">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-EivubOZ49AI_H1z52dPlW775xuzj_HZuwkw4Sy3g-_MM0Of3hUodSElVheTiUf6ImMPyZk9JlC588vYe0dAKYeo95xAdCx4TEXVfoHS0qPdSdkrP3eVv9SJaeeCmY-ruvoejKONwvK5GgaL7TwQ0O0cPsWWOK4GnNdN2AqkPKJ2ENm0MlVYCrdVPUboLTe_KyvzNHwCMc_glgy9AA3XhrXlBM0vFvQPPGQyRzveqowNK0fu3eeERpz8tt3V1bwtFn_69_AiBSDICyzSOwNCYS_R8KRmZt6DfVH2W1Lcrw8zclPY1ogXa2S7JEnMpvs4ON_Dk_zfmjZZc6rAGXquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10تقابل‌اخیرپرسپولیس
🆚
تراکتور در تمام رقابت‌ها: 6 بردپرسپولیس، 2 برد تراکتور، 2 مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28373" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28372">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400b87e841.mp4?token=R06pcsFOCZmFzFSBPmv-m02f40mgoL958mt7PTwAdYumIBj2Rwf_llWiwj6pnv-PGGpsIAfYpjjlRkxdqg2BPkaa6iEUfHBVZR2uwfxOK514JUUg3P8_JppULp4VxOqx_IaqZq6k5ESsxKHQWl5qe6t2Va1M5w1ISBQlXg8Qtfh7Jj1BrcGVS-0DhFY0eaEMkAhKI4kombr6E-fjWxPwufDI3wBLyem9XqCKW3NiW_P-i64rYvioWFWQFqwUBYYgWs1hvmogglp15Ec_7nTLYvAnWinWNUyI4P9Q11J2EE7fVqT-T4L3LOwN5aMysYPxeXJrSVU4hundZTNNf-ZgwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400b87e841.mp4?token=R06pcsFOCZmFzFSBPmv-m02f40mgoL958mt7PTwAdYumIBj2Rwf_llWiwj6pnv-PGGpsIAfYpjjlRkxdqg2BPkaa6iEUfHBVZR2uwfxOK514JUUg3P8_JppULp4VxOqx_IaqZq6k5ESsxKHQWl5qe6t2Va1M5w1ISBQlXg8Qtfh7Jj1BrcGVS-0DhFY0eaEMkAhKI4kombr6E-fjWxPwufDI3wBLyem9XqCKW3NiW_P-i64rYvioWFWQFqwUBYYgWs1hvmogglp15Ec_7nTLYvAnWinWNUyI4P9Q11J2EE7fVqT-T4L3LOwN5aMysYPxeXJrSVU4hundZTNNf-ZgwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو برای چند سال پیش نیست برای همین چندماه‌پیشه و خیلی‌زود به حرفای ابوطالب که گفته بود دلمون برای دلار 78 تومنی تنگ میشه رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28372" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28370">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7561a592bc.mp4?token=tXuQcb4oIUVLmTXHiXqDD35rqENJ_6pnsRPEjuxzMFgIrS5ed9pnTzEm9P-7srB7Ji-LXGlDGAXwSZcFWxC7w70V4nz31BXuLTH5DlZXk3_K_m_aL6lfVqkESpEJaT3Pu7GNEvVGPHI03-l5xr2c7YtmN0h9RhTYor7spZfcbNNiEM5urMRWM8p8KOMfIYQ6tVB-P6l34_tjil7aUZxqJ3fGt-TeUu2l7vE4rJMj8-dS0oSrLrF1hRMfH3rl3sX4shrd7FAsfaR8urI8rS6MRvEIS2Kd4fbscDnqKg0qJ_-HyeJfZMOEoJoNSZh_xm80GV4uNR4McxF9r06cqHTtDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7561a592bc.mp4?token=tXuQcb4oIUVLmTXHiXqDD35rqENJ_6pnsRPEjuxzMFgIrS5ed9pnTzEm9P-7srB7Ji-LXGlDGAXwSZcFWxC7w70V4nz31BXuLTH5DlZXk3_K_m_aL6lfVqkESpEJaT3Pu7GNEvVGPHI03-l5xr2c7YtmN0h9RhTYor7spZfcbNNiEM5urMRWM8p8KOMfIYQ6tVB-P6l34_tjil7aUZxqJ3fGt-TeUu2l7vE4rJMj8-dS0oSrLrF1hRMfH3rl3sX4shrd7FAsfaR8urI8rS6MRvEIS2Kd4fbscDnqKg0qJ_-HyeJfZMOEoJoNSZh_xm80GV4uNR4McxF9r06cqHTtDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
این واکنش و چهره عبوس رونالدو بعد دیدن رئیس فیفا در شبکه‌های اجتماعی داره وایرال میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28370" target="_blank">📅 09:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28369">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b7f7aa5f.mp4?token=jsEmHOiRlYya33kxePqSmmdLEoV7Za6KL0zRaV5mKqrVEdgiRkSb-Sf-JCa2JF4CTTHuzl04qwF27SzNqDzuX2q73e7BfUDtSle-7x6ffk36FVh-a7Kk15qP0QB_2BTM4TMrXMWqeci7HwPhtdDZ644psx7o0SxR8E7vOsg_2ECbdEuFqgUQmF8P19GXxqZz3oqMyRoLSEkscbEJ6SB8RhNEjf14vD4bKNU7ljMSNWQTJVzMBg3Bwb0T8kXw4Jnm9poP76hWRXESEkrnYIuFS6PiD7CPAWkzm_2p2RwTIjBRZFj1iQmicBOXJkzCGWSygLCFvv7lbbC2iv_LuIsFAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b7f7aa5f.mp4?token=jsEmHOiRlYya33kxePqSmmdLEoV7Za6KL0zRaV5mKqrVEdgiRkSb-Sf-JCa2JF4CTTHuzl04qwF27SzNqDzuX2q73e7BfUDtSle-7x6ffk36FVh-a7Kk15qP0QB_2BTM4TMrXMWqeci7HwPhtdDZ644psx7o0SxR8E7vOsg_2ECbdEuFqgUQmF8P19GXxqZz3oqMyRoLSEkscbEJ6SB8RhNEjf14vD4bKNU7ljMSNWQTJVzMBg3Bwb0T8kXw4Jnm9poP76hWRXESEkrnYIuFS6PiD7CPAWkzm_2p2RwTIjBRZFj1iQmicBOXJkzCGWSygLCFvv7lbbC2iv_LuIsFAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا ستاره بارسلونا که از ناراحتی خولیان الوارز ستاره‌تیم‌ اتلتیکو خبر داشت دیشب بعد از گلزنی این خوشحالی مختص به آلوارز رو انجام داد و به نوعی از او حمایت کرد تا روحیه اش رو برای ادامه فصل بدست بیاره. آلوارز خیلی دوس داشت بره بارسا اما مدیران اتلتیکو…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28369" target="_blank">📅 09:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28367">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82aeca8f4.mp4?token=UoPYQLVrTCVQYglh1ymugm4No6te8Ri-iEXi5oi5wQx5iUrE-BKV_GeAxwtkgXD6ounJcMpTSMKqilRXf_gHQs9JidT-WwRW2YMVm1lnaqPlNcoI-I_HvfTZdRsTIESCRogwTAgECbeMtKg-KNV9j8xqalcU5XyUMUw4CTd1bnX1-ROZzNO4p5ikuCh59-n3Rx3ZlJMyfueMUPDhm6HHEn022MDXZ05_nHsr6ZD0-fmTmhhgHaAXkSvl8w4eNiF7w1OtboZvma5DPhRFZoVN8T22A7yP1ALV1_fmW5o8bxLglUfiIutoyMEvtYjHu0F6G1TrpnHZGqC_eCT8RBGu4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82aeca8f4.mp4?token=UoPYQLVrTCVQYglh1ymugm4No6te8Ri-iEXi5oi5wQx5iUrE-BKV_GeAxwtkgXD6ounJcMpTSMKqilRXf_gHQs9JidT-WwRW2YMVm1lnaqPlNcoI-I_HvfTZdRsTIESCRogwTAgECbeMtKg-KNV9j8xqalcU5XyUMUw4CTd1bnX1-ROZzNO4p5ikuCh59-n3Rx3ZlJMyfueMUPDhm6HHEn022MDXZ05_nHsr6ZD0-fmTmhhgHaAXkSvl8w4eNiF7w1OtboZvma5DPhRFZoVN8T22A7yP1ALV1_fmW5o8bxLglUfiIutoyMEvtYjHu0F6G1TrpnHZGqC_eCT8RBGu4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
چهره درهم آلوارز در دیدار اتلتیکو
🆚
ویارئال؛ ای‌غم کمی تخفیف بده ما که مشتری هر روز توییم.
‼️
خیلی‌تلاش کرد دراین‌پنجره‌بره بارسلونا؛ هفته‌ای چهل بار مصاحبه‌میکرد و میگفت‌علاقه ای به موندن در اتلتیکو ندارم اما مدیران اتلتیکو بجای اینکه 150 میلیون یورو به جیب…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28367" target="_blank">📅 09:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28366">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292f9f2a3b.mp4?token=WdCM7SQJi99dbbrZkO34XBrP6k4vWsI490WoDmCA3OkBxZlAhd62CFne61CJbPy3u4DsdWRjhZ56MK4fQbaSytClDKtVAVsqyjmPG04VNbm86afox27gKqG4yB4E-4ua5s1NPdkszx5ZftvipC8hmFGq7FKoQZjAJlwhd-hF0vFB0tLw3HpVyzXb6gotkzFYrm8gNrT5jbgk2Jjo8lnEQNIzR467ksaJlySHGwQi8xsFYgNtXF04EsVoQBUHKWcwEKXpFiOq0uaQA6MW8dbiLoSkHiTTo-cBy_ZxilBS68h8B7GZP99k9crmTEry10o9thlWBRBxJFrKJd38iuI01rTatTCg5raic1fQcmGyyjjNe6WgXMLMtbNy4mCxr8TzV7bX90yBmLXemntHOfwnZcDufhCab5Z6aPKTj763DUDHawetO9kiNpUfCQg2cvGI-7n_hDAvbsy2Z8gZb0cgt85qIdJ72QIw30mDi2lcJxTdnkIAOcGdCwxsZSvRC6evM1R-pUjV3R6odLtVEetp6pwIhQ5slB7By34dJz0E5tbsTeE0hpna2toaeSG7Uv4oqcSqac7MM6vs6-p7CFrPcj4Dw6zfcMmIy5cnqWkkCTtHh7GKq59G_U9avz4nI-MfClsrfIa6kjTO8j3SoJ_CAzMDKBdQWIHCGpo3cxn7SkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292f9f2a3b.mp4?token=WdCM7SQJi99dbbrZkO34XBrP6k4vWsI490WoDmCA3OkBxZlAhd62CFne61CJbPy3u4DsdWRjhZ56MK4fQbaSytClDKtVAVsqyjmPG04VNbm86afox27gKqG4yB4E-4ua5s1NPdkszx5ZftvipC8hmFGq7FKoQZjAJlwhd-hF0vFB0tLw3HpVyzXb6gotkzFYrm8gNrT5jbgk2Jjo8lnEQNIzR467ksaJlySHGwQi8xsFYgNtXF04EsVoQBUHKWcwEKXpFiOq0uaQA6MW8dbiLoSkHiTTo-cBy_ZxilBS68h8B7GZP99k9crmTEry10o9thlWBRBxJFrKJd38iuI01rTatTCg5raic1fQcmGyyjjNe6WgXMLMtbNy4mCxr8TzV7bX90yBmLXemntHOfwnZcDufhCab5Z6aPKTj763DUDHawetO9kiNpUfCQg2cvGI-7n_hDAvbsy2Z8gZb0cgt85qIdJ72QIw30mDi2lcJxTdnkIAOcGdCwxsZSvRC6evM1R-pUjV3R6odLtVEetp6pwIhQ5slB7By34dJz0E5tbsTeE0hpna2toaeSG7Uv4oqcSqac7MM6vs6-p7CFrPcj4Dw6zfcMmIy5cnqWkkCTtHh7GKq59G_U9avz4nI-MfClsrfIa6kjTO8j3SoJ_CAzMDKBdQWIHCGpo3cxn7SkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شاگردان هانسی فلیک در هفته نخست لالیگا؛ آتش بازی راه انداختند و دردیداری خارج از خانه با پنج گل الچه رو درهم‌کوبیدند‌. فرمین لوپز دبل کرد‌. کریم ادیمی هم نیومده برای آبی اناری‌ها گلزنی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28366" target="_blank">📅 08:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28365">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c023812.mp4?token=ekhPp01gDkAud8z02mPOl0MrcfJ8MNjY4aYRNeQc_5IVuZC1DjWxWvROFrKdtZVD_NbVQNJmKImQUlIWhM3vyEnFS6QMF87qbPhKQdNLa9LboZ8QBbBAuf6nXLkgbXyGBW0NM4Uv44Qq0UQ71OsJzgVYOTbzTkwCoL1sFyf1CUUkVp8p0AzbozhjRVdRpZOjLovMmDeL0js5yc99Z0sxohivR8t0_Cd_pbqql5F9kay20iZ7TZWiQDpYSnTD-MuJ7qN9oY-peCgvMd8-ulG8XvgqnPaenhXmZ-BU6fLhGCdj1fmqdietWovjT4WSoNcK03HrVYi_WueSFsBHH9NZnguHjzcOyiJAWBSTrRFZ6YFq4xmYhiH6JxufWLc28m-6v6GPTkITIp5XfJtmPqD1Iaj7VUsnN01-5v_Qfp0Lj1DmloEtfLwJN15QmRJ4pZSq1n6oPFmA7OkqE-F2upIpDcJLD2KSTfM8YTGPQRtWrLeBS3ljZr7O3XhSowYiZte-ojRs9aieBpOKptS489xBaB5FyLXjIVsHyzjFfMjhd3WfUq1qxUBwQC5haGal91U9vrTebHS2XIaqAMJJ6zCCj7eitgMPGLcATkBzwMQT30g4ppAOqP7Sj1Io3bHNUUcVuGtA5YvEJpKKnQB03F50uCsLbi0Yf-SC6OpgKy5WV9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c023812.mp4?token=ekhPp01gDkAud8z02mPOl0MrcfJ8MNjY4aYRNeQc_5IVuZC1DjWxWvROFrKdtZVD_NbVQNJmKImQUlIWhM3vyEnFS6QMF87qbPhKQdNLa9LboZ8QBbBAuf6nXLkgbXyGBW0NM4Uv44Qq0UQ71OsJzgVYOTbzTkwCoL1sFyf1CUUkVp8p0AzbozhjRVdRpZOjLovMmDeL0js5yc99Z0sxohivR8t0_Cd_pbqql5F9kay20iZ7TZWiQDpYSnTD-MuJ7qN9oY-peCgvMd8-ulG8XvgqnPaenhXmZ-BU6fLhGCdj1fmqdietWovjT4WSoNcK03HrVYi_WueSFsBHH9NZnguHjzcOyiJAWBSTrRFZ6YFq4xmYhiH6JxufWLc28m-6v6GPTkITIp5XfJtmPqD1Iaj7VUsnN01-5v_Qfp0Lj1DmloEtfLwJN15QmRJ4pZSq1n6oPFmA7OkqE-F2upIpDcJLD2KSTfM8YTGPQRtWrLeBS3ljZr7O3XhSowYiZte-ojRs9aieBpOKptS489xBaB5FyLXjIVsHyzjFfMjhd3WfUq1qxUBwQC5haGal91U9vrTebHS2XIaqAMJJ6zCCj7eitgMPGLcATkBzwMQT30g4ppAOqP7Sj1Io3bHNUUcVuGtA5YvEJpKKnQB03F50uCsLbi0Yf-SC6OpgKy5WV9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
هایلایتی‌ازعملکرددرخشان‌یاسرآسانی ستاره آلبانیایی استقلال دربازی شب گذشته برابر سپاهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28365" target="_blank">📅 08:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28364">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsr0nOEIm_KjXyz3BWexYkyMQuqCHoNRIIv8lvW3GuYYxp7aueQb9E0wCNIkfj6tMRWcKYQ1H4IzNtLP95BCEZoZUEo4C3BESv4qEO_po6jU2xssMy8FsR-w4OWocii4fWtjDBKG-zXb8-sb6Fdhd8EvBArq_3Y9ImBgVse3veTB8YOLudDv7pHNvK9_ENukRId30ErCVtOpOJjx5_GLtgZYecvV8q_5p-5apU-ELNtcg3bcsv_4VNPZwbdmo0dLTpxXtIUrmDTe5ICKL5zJPGJx4iYX3ju_CtNb0uff-_bdXEYPC1IFgLEijRGezEByPPSIxeLPq3BTDcYPaD7Mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یاسرآسانی، اسماعیلی‌قلی‌زاده و حبیب فرعباسی به‌ترتیب با نمرات 8.5، 8.3 و 7.9 بهترین بازیکنان دیدار امشب استقلال
🆚
سپاهان انتخاب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28364" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28363">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKaGYsJLYb7nN0OJ4UeYD-I8RmDplwJXCbxRZ1uxw3vwobYU7aIjo1BK_LFSjJpEmm8ybJAeJwAHbRfKwLuAEGKGJkT5vGTpSRu1jfC0rhcVFT09nLEOyHOQ-9Hx-NTzk9oYCKwHwticHM5cHoGY-HHBL8pmU3iNvqrk_npFpc4U2WTd4UwBcmaB7G8F8fqCsBCC9d_uv9QIpQTp_o7fhDpcYeSaoXDwx-LwwDE32xMJ7wtslvwaPFONeUnoi_ybCKWaLRid77QPjzAM_FsUPwqqBVXqiFJjv9cKoIJ0ezEe_2O5qSzalJg4TnW8Eoas2hrwcdOtLMrDbaljwpYj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بخت در خونت رو بزنه همین میشه‌ها. مردی داشت با هال‌سیتی مذاکره میکرد بره این تیم که‌یهوسروکله رئال مادرید پیدا شد. تو اولین بازیش ازرو نیمکت اومده جور ناکامی امباپه و وینسیوس و یان دیومانده رو کشید و گل پیروزی تیمشو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28363" target="_blank">📅 01:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28362">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔵
🇪🇸
پاریسن ژرمن با درخشش و دبل فران تورس ستاره جدید خود مقابل رنی‌ها از شکست فرار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28362" target="_blank">📅 01:35 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
