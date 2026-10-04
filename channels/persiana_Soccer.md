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
<img src="https://cdn4.telesco.pe/file/UI0X5Yxl5g0V2r4tyAeZv0dMGyOQImQoX8cYT7UR194V0O2ZiUVKg7ixroeFif8M-Fp_01rGSADsqra9IP2Tnt9B06hnozvhDvSxWJx43dUbOp2ZEjbaJ-NQNbpIEVxv_FKGvHJcOWP01P5SPRSLfhiil8BxnadcGruic_JI-gnPXu9XaGG5jhfBLnO8PSc0Zw4A1_LqrHXemIV7AthWqDZn13XWn83yMLW0eoUhRoqrsVU1E0rrL9MYu5HRK4ZIY6ITb9QwekOyi5AVQNkyXdheehflvXBhWn6y0F4B4sCDGV7HjpgKMnGACP2f20FQzZVaD-j-5EIqZe2E5SIm1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 455K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 23:46:47</div>
<hr>

<div class="tg-post" id="msg-30996">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Ficu-SbVIo0BdDL81yAm0gxd0BI6lq0dhl7QkM9TUv-bgPBOXIvo7e7MHEu2ORnmlIgfRiLHikfhk1Ja-MqeTL6Oi7s8eHL2kzsDEaXPGCESVE-Lpph89N8-rbYp7jg9nVBcnHXdYsr6f-iUmKhqrd7xE9ZQUd707E6Boc7X4wZYW3tlNWnO_7FeAXmg0jIYqhJgfOGIn4wHyDKQSVxY48LHb2x64Ho9hx2F9_GmVddQCUIVJvw1H80R6Kao77d76nexSsDtEJpr8pyljZgWwnyeXwb4J2qSbvvQCmqRJri6QDfjfiHUnVR1Xwz2ZAEkxWATCFGYpWwrcqy6q5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/persiana_Soccer/30996" target="_blank">📅 23:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30994">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9256e00306.mp4?token=KKT3520e7KEpcY7a4q61ykPlYlcSbQLsnDh0rs4AgMHojJMq7kWpiF-ZZm-d6Yl85O2T4TgXqK_7mQUANQuDJ6XJSckSOqscWUN8uziRRROgrImS6oR-pYb1kD6XNq-fvl_B_47V7X4KrYnBcP4Jql5xbPuvVqJbbM2KRA23o5I-RmACxb-PxiDCZb8y6UIw1d5-iRc1skHdrn5qi4djiswX8URQNsvPNpKlgrQhjpIPiIYA93gGTOcTuvf8xSuNb60WC7_myHmo0rcWQcTib17kyp2wgdPePuwRHngEap1b8uxWDrknJb0byfQ3Tn-Sm2CmhESR_ZWgoYTjRujpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9256e00306.mp4?token=KKT3520e7KEpcY7a4q61ykPlYlcSbQLsnDh0rs4AgMHojJMq7kWpiF-ZZm-d6Yl85O2T4TgXqK_7mQUANQuDJ6XJSckSOqscWUN8uziRRROgrImS6oR-pYb1kD6XNq-fvl_B_47V7X4KrYnBcP4Jql5xbPuvVqJbbM2KRA23o5I-RmACxb-PxiDCZb8y6UIw1d5-iRc1skHdrn5qi4djiswX8URQNsvPNpKlgrQhjpIPiIYA93gGTOcTuvf8xSuNb60WC7_myHmo0rcWQcTib17kyp2wgdPePuwRHngEap1b8uxWDrknJb0byfQ3Tn-Sm2CmhESR_ZWgoYTjRujpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شکیرا همسرسابق‌جرارد پیکه: برای‌اولین باره که این‌موضوع‌روبیان‌میکنم‌ وقتی‌از پیکه جدا شدم. یکی از هم تیمی‌های سابق او که اتفاقا رفیق صمیمی پیکه هم بود به من‌ گفت که بهت‌علاقمندم و در این سال‌ها علاقه‌ام روپنهان‌کردم و الان بسیار خوشحالم که جدا شدی. یه لحظه…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/30994" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30993">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCyumyKyKJulzB-nNs3NUxU4fXr0zzF21h7SuD35ryaqUiU6-YP7DOcy7oBFO5Jbhld-zSbwE55I1wxZTm4vHe0b4Pdk1uwqmDkdxohZ2w5nfg5ppsN41g3OXiD4a3Kp_GavMNiETttRtJFWypWiEH-SvehgtTmrGxOU-EUl0yESmRhoBWrU3WePLgOnFbakiYep0k3f36wJR5zrg1J6PXHswzFcQL3ycCurIlUP8nLsEYvHtrgQWG6kcnb8sCQhfYFg7HRwEvLdzpUb6NGsGbNHqlb9foCfX70b1uQVgEyvLlQkXeM-HUfqWV7onjwNXIgcjbsteROiKe22cAtHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/30993" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30992">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=RG1FxbTcMTEBKrF1QpFu7hzOHyw8UaXwssK0mh-htyJOiw1_8JL1ZCpK8XU1Bln7AkmqbzvylDWdPcPBZyqAI41aXkg9_cwU5koQV3qE-gKxC3QYFg8YijXfNZETFjO3lIMkq8WZPdh9Nu4D-IVjAdmRVonzY8y3reaQ9YvfUmyGFtdozRmC3n4luG09pJD1FUvsjSnJDj4By_nSbWGkmyJSgKWYlaaDikaLOBV7t5Zhbqb_lb9P-lV8emIbI_IlLAoLd7A_606u2NtiVcq2PemMPeilW0p64Q-lvVzQD8So1HgtbnNAYxgsLedRBgy5sk4wv7oPjIdMovsoJkklKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=RG1FxbTcMTEBKrF1QpFu7hzOHyw8UaXwssK0mh-htyJOiw1_8JL1ZCpK8XU1Bln7AkmqbzvylDWdPcPBZyqAI41aXkg9_cwU5koQV3qE-gKxC3QYFg8YijXfNZETFjO3lIMkq8WZPdh9Nu4D-IVjAdmRVonzY8y3reaQ9YvfUmyGFtdozRmC3n4luG09pJD1FUvsjSnJDj4By_nSbWGkmyJSgKWYlaaDikaLOBV7t5Zhbqb_lb9P-lV8emIbI_IlLAoLd7A_606u2NtiVcq2PemMPeilW0p64Q-lvVzQD8So1HgtbnNAYxgsLedRBgy5sk4wv7oPjIdMovsoJkklKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صحبت‌های پیمان حدادی مدیرعامل باشگاه پرسپولیس درباره شکایت از یاسر آسانی: مدارکی از ستاره‌آلبانیایی‌استقلال داریم که به کمیته انضباطی ندادیم و اون رو به دادگاه عالی ورزش داده ایم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/30992" target="_blank">📅 22:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30991">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3CrZrngqj1tywV4Y0D52IOCK5pTlhYEBVYqY6uUC32Bga_e22QPf0m1qbwypuz_3sQaHCU6UyxMGTRfHPyzvC2ws8qf4EeqR4hT-jbZuKeh5Z0g5xU3ddBjW4wUMi_FI7A9fuFItn1XZWRyoRS004ix5AoeyA8TduOR3vy5LGRyNUvn-6ocF_3PAHUWhRt6AKGdGh0oldL6QNWPernU1uj0vGn_6WePYFGelgZ4MqBPZ_uQk59hTpQ3FoVO4cJhZ2hS_-CR9nRDjJw3nO_a7VExWWXTtBUMLlZmMKzkHKOlg_Yl4f1_kN450dihfkH_Cz2G-q-OyStNjh7vHdEVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ادعای میگل پریرا خبرنگار پرتغالی: کریس رونالدو مصممه که هزارمین گل دوران بازی خود را با پیراهن تیم ملی پرتغال به ثمر برساند بنابراین احتمالا درسال2027 به میادین‌بازی‌های‌ملی بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/30991" target="_blank">📅 22:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30990">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iypxhvB64SQB9oqGwDS20zs7lpHQgIDnYH8Gpe-WB9E93Iip4CQNHVVjT0TDcgkBmIvYqNmFr_C2N7IkASSncAKnTH_6I2sU79N6Jo4JHMAvDsMN1x4E1WghtfGKcjS2cYrI_pB7QlyeOhVIQdsRKucZGI350SxSGuHn3VwVq7rImxFLd7GhLw4PtlCLYLcl5XUdnTDOCq6zTuCM3TyT6Nsnh_OAhd6RvzMSvv3huBMdv4qhisIagw5TzRA3-t3qyZFNNhLgnGrHw7bESP0KrF9oYJuU_iLyC_ladzRGbBRhgCzToFwW1Ptf-qv2fpLqb5UqZK5fevmYN-Nd-c5bjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمسابقه‌ امشب الکلاسیکو زنان؛ بانوان بارسلونا تاپایان نیمه اول چهار بر صفر از رئال جلو افتاده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/30990" target="_blank">📅 22:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30989">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOHcdqUQgFXziCvTp9LPvIMMjPSezF5gD9k_n0ATg1-xFQ0TksnJyiyEqrwlS22w_FYCSldWLsrGmYQ2FXc2007xrULUAksQxdyfQLl9KQQSDNQdMdKUj1qF_UqyS2QX3QAb1o0DCcfOu12zBuJjUC70CApoUWIHxvGEVGAa_BW1Ce7YxlcIZ5Y5kW_ZkM61VA6b_QF2wk7AM8hjJ2Avx9kyjG8F-28PrE6kPmkJnCcsWzpx_uYt0Rz1EFbi9SWBYm4nJB83htRXXOzT3SOOD76QnM5fDoAW5JBiniWNbPxQzXO89S2Hh4MD2Mr1qC48EmePUU34uBc4t3J-GSSrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/30989" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30987">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEIUAa9oMrYbVcqYiLQJnpJGptjweCb8lBZZvkcwauwGyZJ3s4QUXAgHGgiYC8vJFfl9POBrCWS7dlBjaTPLiswPCx8LmqbgNWaFDNrJP7Od_msNyDa94IQbcCCrQ8-my81zQNxUZYZPCp91Nh6_vVS30HzKIjx8gn3VJsCu4ckXf8ecB7KUu8QPhY0zR4HrGXiMlNdYg8sWb8TSxepbQ52eKazDfpizO5xBkrN-olIc16mbO64qe5893qvcDG6z8XAxvKjE9sYWbY2JlVVNt8tlpLoVVPWZiFwRKx52tm_02dilPd0alggEXlZxmSJDyx35wmP_ahu3Y0vgcYe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=s_s3d6X5kMTcW0Ji2hDYvcavtkn6pzXZr91y5uT5ZY3_LfyuvvEAfTrJjs_f03mcpqkpolDXTCNTWmo354P4GWM0uPtX198RpARL96K_AXEQqDMs0qYU1ZjoExKSOjGTJBMjL395yed0rZp5ysoEOeRQSiNZubb1jB18bJqIyXBZs_AbITvpjHrXUKQB9WItl9JbQeju30MHF4_BRN1om22dHiFq2Et-IklYnjSeJQMRa0SUnD7FRj2QCPjJ--tqTJJlJAJh9yoT7SYaTrEn_hMtq3dMp-uY8TXuK16p7hUrntAZBg_YfBQddG0xPC5kVZ5_EH7B0xmCcaY8MBFqeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=s_s3d6X5kMTcW0Ji2hDYvcavtkn6pzXZr91y5uT5ZY3_LfyuvvEAfTrJjs_f03mcpqkpolDXTCNTWmo354P4GWM0uPtX198RpARL96K_AXEQqDMs0qYU1ZjoExKSOjGTJBMjL395yed0rZp5ysoEOeRQSiNZubb1jB18bJqIyXBZs_AbITvpjHrXUKQB9WItl9JbQeju30MHF4_BRN1om22dHiFq2Et-IklYnjSeJQMRa0SUnD7FRj2QCPjJ--tqTJJlJAJh9yoT7SYaTrEn_hMtq3dMp-uY8TXuK16p7hUrntAZBg_YfBQddG0xPC5kVZ5_EH7B0xmCcaY8MBFqeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیوکامبک‌تاریخی‌پرسپولیسِ برانکو ایوانکوویچ درورزشگاه‌مملو از تماشاگر آزادی با گزار مزدک میرزایی؛ اون دوران الدحیل تو 51 بازی فقط یه‌باخت داشت که اونم جلو پرسپولیس برانکو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/30987" target="_blank">📅 22:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30986">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA-qOt-vfzmVhU3WfFM10r6oOD6pnOdbaRI9DUl9iUma3S131-oCJn2-3QXJMthC8PxnZVr_v7BAD-F_moyDB-d8my0VV6UZqL8VRx5fhs8BaWflUllGInhxX2V0mnQLMDgvSYxb6skBkEKrvdyAmrFH5qKYb4QAUR0hmm5lX0QKE8jdfrROAdCrlTvGAsb__wQB_SP4JPFniEuP9palzsBx_PqeuxZ5CipFMdSzSaqGz5bG3U9QO9KpCoFzY2h6eD1XoFMm00U1zHVQweIfvIFJ_rbVBXKsnGjoy1IZv2cgEqpdBpRxV6n8N3PwUbgVzEk6nU5KufvXsU68ejsDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خرید جدید تیم بانوان تراکتور برای فصل جدید هستند؛ نازنین دواتگر مدافع میانی که سرخابی های پایتخت نیز بدنبال جذب او بودند در نهایت با عقد قراردادی یک ساله به تیم بانوان تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/30986" target="_blank">📅 21:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30985">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=dj64RcMV3p5mxzCDDaMHQmbQRfdA-KSOjab-kwlESwQB0Do62hPw_8oQOTXurLHlniWEt3tcRuF6-HpmWjSMqwAzPjeXPS8SlUFIQq3NnugTxp6eZaDftMQtlidkXCUf4mi4nbWf0fe4jnhQQku7TrppO_mzggSvSoafL-yI7txoqTcVhhxLmSgriDLAjp4zLlQF6NmWTNkqA8_SSxmYr9uR_CVCmXBZitudV8gP10-LrMsujGDnvigIWjNSG9zwPl4lrXMCsagbOCaBrTXobTTfh9tRfAgLgBmCdTBjGOyc7QaCDt5Wd3a2ItpDs5y-Y7NDnGFF20tGt09jB0yIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=dj64RcMV3p5mxzCDDaMHQmbQRfdA-KSOjab-kwlESwQB0Do62hPw_8oQOTXurLHlniWEt3tcRuF6-HpmWjSMqwAzPjeXPS8SlUFIQq3NnugTxp6eZaDftMQtlidkXCUf4mi4nbWf0fe4jnhQQku7TrppO_mzggSvSoafL-yI7txoqTcVhhxLmSgriDLAjp4zLlQF6NmWTNkqA8_SSxmYr9uR_CVCmXBZitudV8gP10-LrMsujGDnvigIWjNSG9zwPl4lrXMCsagbOCaBrTXobTTfh9tRfAgLgBmCdTBjGOyc7QaCDt5Wd3a2ItpDs5y-Y7NDnGFF20tGt09jB0yIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/30985" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30984">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JXWBkCxmPAGCY8YVAuznJQPVcuNL6CT2UUA_7JKlvVBZeOiL5AYSaERxU5bhXbyw08EXpIR8AQOJf7q_nIY6ibyCUfHpJ3nLCyKFXWHj_y3t9iO2JuhK_yhWOSObdJrBpQYkGDCocQzo-cI2_EgWGnSKDKtw-DHVn4GqXlmbCQIR0MhDWilOEp3ICG7wTGPvvLYdEQmiT7XaYlvxE6k_XDQ1bSEGrQMP8R-UFD1d0VRefUirQJxJLj1HdVOMy9TlHvvJLN17fr0dMW0GILHQjujwjnUJps8ouXNeNSEPZFTQRqWRmuw-yySHvPeQ9wgoyaa_2GcfXv8yQdp-esrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد کریس رونالدو و لیونل مسی زیر نظر کارلو آنجلوتی و پپ گواردیولا در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/30984" target="_blank">📅 21:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30983">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdncHOBWIBghy2f8AyUNAasSdkGaGjQCuP-_XY1ENIhvtS2ElDSiVpvSQjBTL3v4S8ovgcaqqyp_ymnb7b4gHMh3S6puRbbDNeRDq4Hfxu93htrzss8qOSD7fraO-iEKZz3wKoyjr-nAbPcGgaPM-jdRJfjUW0t0_DfVLlTmMsQtFYarnYpvOt83TAs3yep-iE729GNs_ZomsV24b9CGDyMDCNMyqNkxSGng2WfdWoAy3OfjLQnGx3gfqj0-o7S9qfzCMTXnlrmAE3W-7C1B2u_cRYDR-zI0Z79d_TtzM_rbIJlgCnBoQlOD3mi5zrsPF51RRk9qENrkjhIPXwbbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی و زنش درتهران: متاسفیم برای فضای مجازی. مردم در واقعیت خیلی به ما لطف و محبت‌دارن و هرجامیریم یه ساعت باهامون عکس‌میگیرن. مردم‌ایران خوشحالن!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/30983" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30981">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=sgjkRF_9yP8Hg3tb8n5GR0UtTRjn5wcg5avNXv9tC2qIH21Khykd7jsKURJrWvLg-YbvYfQXMSYavDDYXuWCwTUJIIrK62PwVzwh3un68PWk5tZV8jEdzX83eoQhn24Ln-2GY4ifHnxOmlLpyl-J2E4pnV9KpSaDLMG3GKq2PJXcGMrGHo5ho2lFnjHYRdnqejw2bQE8vleH6dyfu137L-dSRmrCq3mNhEQu3REdtW_LeZtZP6_m1D65X3L9MKTGiteDUyzWdfEmMI6bOUDGWFbg9g059wKmErggBs59heXvsdjR4NhjX0aajPT198WXcx_XWfec4BbX0t38da45tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=sgjkRF_9yP8Hg3tb8n5GR0UtTRjn5wcg5avNXv9tC2qIH21Khykd7jsKURJrWvLg-YbvYfQXMSYavDDYXuWCwTUJIIrK62PwVzwh3un68PWk5tZV8jEdzX83eoQhn24Ln-2GY4ifHnxOmlLpyl-J2E4pnV9KpSaDLMG3GKq2PJXcGMrGHo5ho2lFnjHYRdnqejw2bQE8vleH6dyfu137L-dSRmrCq3mNhEQu3REdtW_LeZtZP6_m1D65X3L9MKTGiteDUyzWdfEmMI6bOUDGWFbg9g059wKmErggBs59heXvsdjR4NhjX0aajPT198WXcx_XWfec4BbX0t38da45tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توییت یکی از طرفدار رونالدو: تو امتحان امروز به سوال شماره7جواب ندادم تا به رونالدو و میراثش احترام بزارم؛ رافائل لیائو لعنت بهت تو چجوری دلت اومد اخه شماره کریستیانو رونالدو رو بر تن کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/30981" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30980">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUvZjPdou-NHY2M6mERuX7HKctX5PNSPQqCRbRutqTeG8Eaq0q0BtiWFDyJpMce9Oi7GVjCgRGRDoH3ZY5dz6UEzc86qNx4r_o4AXVyv_c2n1KMs3d4B8Olk_u36aahjJe8GOKbcInPoORJE_J8EJiB4VFcLaDTeatkFxgjEAJtuk-8Xn_p67bvCMPSEhBEVmyBj4r_HTClO_8_HWdARhDjnoOP0bjVFDHJIwwq749HwIKAMwkTQK5GA7Q9AHkkKCR7YY0aaRRLTLfuUVs4LWpN1oaAmWP6WANTZ2yxz9upGWhDTHt3TEyXASBTu2xQsVBfVbE7Tf4cVuj3gpVkggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/30980" target="_blank">📅 20:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30979">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVkXu_MDYaXN850sbnNZCW0ze8tb25A79STEQM8diplbZdKH9zaMACSzWJVWcZ9OqPEvK11b1y2O8pArsKStIsGOvJ-nwxdUaF0kUjZT7O8lBUOapkyvM_Rxf6Oh7_06rzU5vs815YeD2TLaB1vnkgdrVhSCkg5D-xvWTAbO0YivGmJgnHqcQ-zyFNqyxdyRoi9IMD-sGuyI-ZTRjsZ4-vyE2bU1drxfiZ5CEd6WUo-7FXsB3Xgcljwke4BycpjJxG2tVd75K1QNn1MUSx-BiR9MTzaN_HLIwM795Sk6basHEhPhjffPAnAWj7PI-TnKzN4B8z53qEqi4DdI1gxsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ مدیریت باشگاه پرسپولیس میخواد تا اوایل آبان ماه قرارداد سید پیام نیازمند دروازه‌بان 31 ساله خود را بمدت دوفصل تمدید کنه. همان طور در پست ریپلای شده خبر دادیم تمام توافقات‌لازم برای تمدیدقرارداد این بازیکن با باشگاه…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30979" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30978">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzIwGA_ULP_Vtrli3b4eYy2j-V2Bcw8AwAp7u27yDYzaVRDV9rfWZXH4_CuK4Iy1nqNLO3mkKJTI8zwQvL5zA5SE9c8X90HRpnmOxKbs5AK604OS7v1WHUPzBhN0z1M7XIdMK0fmvZtnwKb0OqTDgiKczUnaQAHnh8xS2nyDm_bj0iUVLfDB1XGQBuaYDDGugii7C-mqqSXczaN5tu4TcDLk-1pddVk4OMhX9GgJe5VuencFEEEmcIz8Kw1oic2S0ap4dF-HYD16Fme_OyBxu3jE-eK2Q8OvS3zPyvQXkXi0f94zYMu1gBJ2aaeauE4Sc-SItZgiM8KeeCKRkGyjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس با مدیربرنامه های سید پیام نیازمند برای تمدید قرارداد این‌بازیکن 31 ساله به مدت 2+1 سال به توافق‌کامل‌رسیده‌است و باشگاه قصد داره بزودی قرارداد دروازه بان ملی پوش خود را تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30978" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30977">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPwdEptZRWa9oGTgr8KyPMIB3xsZzJuGxiCASxfgTXwZ4sL1ITpvupCbtdqWjNuxfcbh3VeOH0kMtuDZN3gQXbs_rhaAZq30iOTW0kCTgR_x5vIR7cbZfokFx19NgHMxGljDQXwo6KSmk1rrbB1RbLKPU4maeUxUly-XmlymfBCD7uv1LZIj1S58Gp69dZ3zvbKkkk9OZpLRugrnH5ijT82IyQhYI1H6q8TPtnglKgWs8mMQDjaAOEduDwQEftWMF5Y4QU0rIKrk76uk2ibdMH3KGyE8Qjqua89BvHqTEUmAornNY-SWRFfvqOvbAlYezr-14Q-KlqX2ue2kylRpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30977" target="_blank">📅 19:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30976">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30976" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30975">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emlbymOifkxGGwZsFkAYHT8v4lOv7uJGL3WN--92jCgovc0in0uURwMeNGLVvhA87ECDx5rVsmuKyzgtFn2APeFIZPUkaLsLeXfE-NvUXy82QeGjOMtpg9aSESzlUVvxvMYL3ANrsPyiDzAywI1W0dn3S5Lh5Sp1gTKe48MZayzTNzW87fDfp5TTHMhh4rIpDYeeJzIr0w4_HcMuuv6zlaj4ISC1K4bT6fUdCaNRcLJIbev7oFuq70TdkzqnrahGgXMQ9kQQX9HPfiMdueaOxhYKehXRkamRUhboOKAtcVbxEbPgpcI1uaVbF7z-x0XsGunVP04AHZTcO9GnNass0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی بازی‌های آسیایی 2026 ناگویا؛ چین با اقتدار در این مسابقات اول شد. ایران هم ششم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30975" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30974">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoxELDH_VIk93iVeJ8evw4JRtCVOz-73cvbGDBPGOyp47TZ69G1DKFXoY-odzAdjagx33tXQSNWIoj-ZwfZ2A4DzFHJH3at5s08UQquH4ei2kByI8CjBzuBM0YParo-luHJezgh6r2Ck8Qb2GT1nl1pfNIrVCVwtDxT1wsSvGa5wgTPjLQEPCq5GwHV9mWNw0fFok5Vxq5QW8ZDuLd5zTsltEwalK_3IC1ndgPHJsD1FgDrXfw7tvA3zKCSG0OFH2M1PxGe08P-Q9orMQ7fQP42dwsjHnfXYjnmzJQFSFX5TXyUFm1eWzayD__TymzXv_0HtWQEfbc1kZW0UIlhYWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30974" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30973">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbLf_YLL6KOa6vl643QDunlRkmOq8VZ6vFyd-WXxVGCJIPdafNWl1Fzj1afJDYh1zCaLNvESRqzhPWhyaex8ZollA7Z9kJ-hbiQ6VI4WWRp2VgNxruSHTeVBEreGzJ5fxkPSoLHX4owZ7UneffMhKS52lX_y1Q0ubVyCiS5DfhQVgtv3FRG04Jxq23dxeIvCcsPu8ngaFQqCTDKhHJarUywhcGaTN0G2WHTQQ2ubkWxFerlYgyO1tf82ARelBAaOaAte0YJX4ZhIRMqUeRhYyrHQL4uLlU23c1SV-ZYs-DpqNaYCl93umwbc_BtLmPtB_-Ta90LN58O-MTi5xMhf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30973" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30972">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30972" target="_blank">📅 18:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30971">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5TZfAfYyPaJoH310A90FsWoSEdAxGXZ9ICuLEY_byDjHZ7fv3DIz3T7h9GD3px4fR_W6Xy4vNfWAXK6-mU4HUcrnquYZMIBPE-1TX9JyRikKAU9LYv9M4BEYBc03xO7C0dwU9lExQqtQecw7hiaZLLMCHc9Vfnd0nvX-JTkZG0anY39rK8kXdhot8_JG1uKNBpCqzwdzMb_ngGi6L7Zb3vhvATNAfvd_vWQpwiecLbqnw9LMjw9scciJBauWQ43xPz8ZOU0irxM2e6WPP5sRGeZxbsCLxDmsLWGcTqx3RNFh6ojNNjPLweCdqHq83bRzAnLsvAkMKmZnOfZC966xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از شکست شب گذشته دهوک در لیگ عراق؛ مدیریت این باشگاه عراقی تصمیم نهایی خود را برای قطع همکاری با یحیی‌گلمحمدی گرفته اند و نهایتا یک بازی دیگر به او فرصت خواهند داد. یحیی رو بزودی در لیگ برتر و یک باشگاه بزرگ خواهیم دید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30971" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30970">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCc8QQRLCrigZSVay1lXY4aCWUTsAIV29ereUaCkzSSQqJyW1_Pyjxdg61YWHd_6nievCUiUnCf81Q-BLknmZwBA5tuuZLypeIcTWKR8mTTdIfoe_fNquUNb3GzVvVssUyyjIeELA_ZGoqo9pgW4CP8HIpBJdB9dY3zP7jAS8o4kclAlug0HkO1uOX5G4ScYtgY07EfFUZdzVHh0gFvp1NBw4wjZjeZFI_DnEAchJth-hgIRg-mikjhDEWndUssnxlnewdl-MemIOfTynII4KGJNx9vPvgY9khMcmyyHElIElGe3yogNIZUHTBbL-MonbdgcVibSLq-weyL-fyHfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارتینلی ستاره الهلال در مراسمی که اخیرا برای پزشکان در عربستان گرفته شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30970" target="_blank">📅 17:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30969">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPS6S8I3Dsy4n88ywREL8q_KAjZbeUQsRQiQ-P6Cnvh-8c943OkMnBKM9aoJyrhIRom5Ux16oQKwEEcT93B8Y0SXvBKpnH8gWz47rfVtFxA2rLU2c7oQH2bT7tusKnmCeUOGBldaHTbRR8gwLA4o2CVil7z1ffnNBYoUmVZXgqlqoIzYQIXepxk88z61P5LUlCnoi6MdCf8LWlao2MuBRXqicWSJzXo77u-RwaRLKE_I7TDratC03-vkYI1ZG6KHdy16z2z9L5NsEuLBeBql3ESpOX_flF4UQO57PmQPe6PFO-6Bxg7bJXNm7OWAqSviSr0xjDBoO0l10mQFTXwLmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30969" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30968">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2-A3IqbP55_Dt6Mvqok_nGCf-1UWNA12qI3lVmQQLTioft8vhAVnsbLpttmj-1uyIpkWYts-HQABQl8RsDiguyF2dl-keRY2hV52Ih7emTAo45zZtKFEFJyIxHd6a2ji5XY-wdiierqTGdOQWxbDEXG6gMsTvdiIIbBsHQdBu2sPVS8g6EdP5zFFOS57NCQgIT9DlZ-uJzX3IGLon4xI9SOVz1-6pSw5Uwprppu5GcSdeO-lmgxTOtG71NzLq53v-Lm5GL--NJr_nDhfCd-bLMqhu4mPnuVVyHi81qMRGndzx2Hi53geL2vNNLzEwfv9x1yGW9COwO5fx3s3sxaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30968" target="_blank">📅 16:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30967">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEc3JTNEYD_gFuIYOHUSiykplnl4etDNxzrXG4f1rFZqLqFm0Ta8FuVgWFOS_mL6s7jEALuwl92YD7r05jgn0Kc-CsMToNvk3nvU_RKjyamlWpbLqH3-QyZitgKdG5PUSzowB5LbPB5K8eX_ZOB9XjQpgxiIiiVEW3udeExrKX3nTmMxLknHqviQnHi1YvU84t6rFtug_Ikhk-QfrSMh6sSYdfee0CTlRumZqCaqtm62XngCUgoCIF0lZFPKR8xw_lFjbvsQUtX7VQis4Fx3bQpcXc1pA3641uScbnGU-1z1YDFqrcbaBdCveGIUI5FIaeVEJwTT8ydYgMYLPP4XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فدراسیون‌پرتغال‌میخواد این هفته یک جلسه با کریس رونالدو و خورخه ژسوس برگزار کنه و مانع‌خدافظی کریس رونالدو از تیم‌ملی بشه. البته خیلی بعیده رونالدو در جلسه حضور پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30967" target="_blank">📅 16:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30966">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30966" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30965">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhvTiJloofmffmyFgzsRLrhSFia2QoOaSW3NLWeL2UvTaK57e56ic_VsKAxowcAOPsLrHNLxYbfw6QzoeLJie6xUjNu7weR6xnrJlBhYJPgP-TMTNBkX4cdqb9FYLXCNuAIHAmte5_GcT-P_ljglLkDOQqvB7cjOGBib3TWkV56yp0jvEYeFn0aVf0z9Xv08eFSBC6LIwrHw4qbFI0den7Brv_ooZbR2T6bLuGfeHlcLZzb4yLWGmn7lWqyQSOImJT_NoZLm_3s2OtGsl9F58LkGEIrdyezDRqsZu2yo9hFn2nPOieoxPRB50_l0miBvZcVZFWTrrAv8dBpMdxaTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسین نژاد در گفتگو با روزنامه همشهری: باشگاه استقلال رضایت نامه‌ام رو از باشگاه ماخاچ قلعه روسیه بگیرد در نیم فصل با این تیم میبندم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30965" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30963">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od1EpY_KrzUNeIa7fGvSWiPh3De0CkkR-WxW_Z-VFOP_FV89fCPZXZQQIAO0Q1QHLQ46pys-G1f_uZ__46MJNeoW4nfC_DPhITkaqbcxnCSsqnfDrmUyPYFTb5hTyuzR3TrlZOvN-CGudaAJ4F_rNBZp0R2ZnThcsQzSKug-R_IRxTBLMh5u2njkDXHMG9vmeAhJRHN_z22ZQ7XqZgI8ix7TI0BNB8HIbzY4u4UXnSWDRWYXZAxSFQB5IXu0OdYx0Y0EEK-PFldmZdhljGd6-D-RlL-VChlz_PlcqBcegz8XB2kxyU11AEvCc2NTU1mMN-2s53f4gRifzYUdqgikWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd2YYELGlxakoqYjLrqZ5RJzjCuFVNXvTLtlCldhm4sEGXSP7dthg9NLIDn2CrnJIZua3bdzP8fzzRwtLkdHv818aYWH9DaVXYrE1sjYrYZ-zJwRM1U_kagRk1J3G4clHCj4cCu1KAT2tuVcAyq6OlvhKfKVjhaHnl3t6ginOoB4jnhCy9smrNsDZxCPEQe41xBBroGd6G5dhckhwbNIpdcmtODl7NCXS-dcb3PVdP44i5ipTvV9Oqdr6avCF0CJVsBc5rHNh41UWFaYiPjgFW-AdmuIDWuFvQ8C_Nw2ItL2dLBC03kzsLBha1ywSQNUD0UyZ2YMNFouwWcKYHyF9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30963" target="_blank">📅 15:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30962">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kho35b9L7jHqF84M5ootJqI4zdC6wdeER9o7eISXJhDrxhPJLcjg3wNxSXIdrv6E0WtgZ4WLZYu0N1CxawBWt-ctwMj0rKrLXXhPbu2QoCX71gJIxLpLHFNo1dvqZ1ginu72OASBUyVbFCQKlfVJGIZJROM6mjYy88AA7vHHJm_FbNuT9PcIxG39KL71ej3NjnUqflab3JR59DTZBSV7w1c1y0Y_T0wtJb9tvMaobWChWz6lFUYwKM2CVmg_bXlIkpdVB5T5J94n05CdGJE4EjVor3YcDPtCIgj3NB9TuitXGZ2mvSlQo2QiyblclGA3jQK6IPdz9-KGrp-Bgj6tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30962" target="_blank">📅 14:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30961">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=BBEcq3IeMbT6DVC6pya2IGo9D9Q2iEDo-O7oMJgG5TFGF6Vmj3crgqa0n52gKtxiq9aya6Okh5vm8ZANk6cjSocOQIbtWz2UbxwZ8GFYZdm1zsRd9wDzgMpFoENEXE806_curosArdJqK6oVhzME13tIwVTjJDNaCeH9x5a0H_2EvL6wwHePEwRAaxgFhhY65qPmtZuBkmgI_uwJWVg6mvljsBgZfP-FZmfUkLF7gciVc9TO35ZRhEFs8H6lxTAEbbx4hKGEacynJuEB0hWewQW3CWPaAOHTf1N-KRyyTqYPP6PemcAOEZxSwIH1DQJpDgFQE6ZR43dbkPNJzn0fbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=BBEcq3IeMbT6DVC6pya2IGo9D9Q2iEDo-O7oMJgG5TFGF6Vmj3crgqa0n52gKtxiq9aya6Okh5vm8ZANk6cjSocOQIbtWz2UbxwZ8GFYZdm1zsRd9wDzgMpFoENEXE806_curosArdJqK6oVhzME13tIwVTjJDNaCeH9x5a0H_2EvL6wwHePEwRAaxgFhhY65qPmtZuBkmgI_uwJWVg6mvljsBgZfP-FZmfUkLF7gciVc9TO35ZRhEFs8H6lxTAEbbx4hKGEacynJuEB0hWewQW3CWPaAOHTf1N-KRyyTqYPP6PemcAOEZxSwIH1DQJpDgFQE6ZR43dbkPNJzn0fbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30961" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30960">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk2XE4QsVR1YhU5_2MJO2QtFcEHZSzJWvZIWvvdnwzzCIbg8rTyKRE6pHTZ0dv8mhlbaLWJIUNljzHs19Ml6ITmpluODY3g3s5-TmUzYVI5EX9nqkfDsXxdVpL9ViZ9ac_SzQjjnfDhedaTtuo1rPZqzrT8awbYthBXwQ5SHc9D-QbEvO1rqCFhsdEtOX6cAsgKjn8GjjlLVU5bbD9CzTQMMD8IQ-XmTjDmRRJuRd3iTI65OXosBJ5e0CScc74ufCyfZdxwZPJ_4x1vaTaixaVReJrYILNS4ZRtxM5h2-qG-POluE4gC72ljEbsdKGvQYLNj91KBqBp45pqOLfb4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با منتفی شدن بازی تدارکاتی سوم تیم‌ ملی ایران، هفته هشتم لیگ‌ بدون تغییر و طبق برنامه از پیش اعلام شده از شانزده مهرماه آغاز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30960" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30959">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H71YdjnxQ4Ng2CJEZE5vt6brg0BG8sCqamqhITYGs6sut1Bi8XTvCk_CAtUX8fEi_g7ZjOUPjddP1gTagsseMjG9JYThh0xqqJJfvQVJz4n0_CY6okKc20t4_qHiD6Tvjll8lh6pOdQKU6Ye1QHskBcrZe5w2odlTzTr0zUngCl1K-tp4PiqKPPJv2qg1SDDByOW1iial2p8F0M7WyuofkprbMJDAwKw8yHxXL0-fsaMeKhaDfMtn2VrgEB1wLJDDpN5sMobc2MzXb4d2Ghu4B_bCk38MO-aGmhuQji9zhiE4qIt6h9gkRqEMw4f_gNyKTMWH8CK4TXAZQjzLDhQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30959" target="_blank">📅 14:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30958">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqBMiG-y1H07Io1NOETYFo-bMRaX1bq7S9HwrTcBr95zqJb7sadi6X11S12vk6cAZxhtFlO6RhAjHj87_cnUcBySG7mBtGaijYQdTOcQvMPvyI202oVcKyLe_XeGPIGz9QN7h_yZL_qh-exl9ZKbLAJPRb6mx7X28TWQWOWdhPlegkDEB5T25c__upAvFK3V-TtQsWjvnLprKHYtQqIKjSTNtW4C5YXRVK0arOAM8NIL1Xu99Cw9aQlpyjGl7TINghdZoaWnSSizbyNMaxQahS6mhj5gapw-y20hjlXBS_Js9xiK6UAkFZmZsSuZgB_45Syafudi7Ty3bxQiYFPTdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30958" target="_blank">📅 12:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30957">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=CJJ9i15GL9-Vgfp5sCCeZIR7PmpJi7W2W5VKl8tfKg4UcqpCpGZsH5b3y3quio_MvqsKSVF26mnaZl36amDcj7s_o2fBZx-zGp7Lm5RA3m60fhFVL-BWFQOueX-VcgPn5QIO0tvym2Loo8pqNslauX-UGShqP6yhZ2qUozZD5OlFzJ90pwAS-HR3MswNOIuonfdCVYh232gyU8PQs_sXKdaHHVffQ1Bx9xrQFXHIwCLwnypzPwGlAbGGlidZQuzu0Q7Gdr1sPqfsmDkjGGUeX2PH3mA_tQQ3vGjR7SyvdeRCWLNN_Gena5LTlK_x7qFMaKr5KAbiV5KAHX16eJZYSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=CJJ9i15GL9-Vgfp5sCCeZIR7PmpJi7W2W5VKl8tfKg4UcqpCpGZsH5b3y3quio_MvqsKSVF26mnaZl36amDcj7s_o2fBZx-zGp7Lm5RA3m60fhFVL-BWFQOueX-VcgPn5QIO0tvym2Loo8pqNslauX-UGShqP6yhZ2qUozZD5OlFzJ90pwAS-HR3MswNOIuonfdCVYh232gyU8PQs_sXKdaHHVffQ1Bx9xrQFXHIwCLwnypzPwGlAbGGlidZQuzu0Q7Gdr1sPqfsmDkjGGUeX2PH3mA_tQQ3vGjR7SyvdeRCWLNN_Gena5LTlK_x7qFMaKr5KAbiV5KAHX16eJZYSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
زیباجوی عزیزمون با این وضعیت بازی مقابل تیم‌قدرتمندهندهفتگی‌حدود180 میلیارد تومن درآمد داره. انگار وینیسیوس واقعی رو کشتن تموم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30957" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30956">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzuy1udhuRpTfmQ3vxs3Wh8MqMOOc8hHDRjzDc6goQjp2xuJBQr4QbRuwhrXqW24687GEicGgsJDA1bIotK_UFdK5LMCE8V8ysUX0Uu4V8QbyGzbizmH7oSwdVstzCCr8UkMZZRNo3oCrm5aZH4bgUIjby_cqXu4oAyHthD6HdyIi0VroOgQt36XXm9aybgdl1c2Q749fvluMnEh26OCoKUUEiHn_10SzeroPp2Vkz94TXuCVeqW9y8yWpi77wi-VqebUW0GCPkjC5qkRnkqT5g2AHVOQgaNH58FQWY1KVhYY_VFRYe70GJflusWcKxSLakxGw5Fp8j6BOSi6wKcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ در صورت موافقت امیر قلعه‌نویی تیم‌ ملی روز سه‌شنبه ۱۴ مهرماه در استادیوم یادگار تبریز به‌‌ مصاف تیم ملی گینه بیسائو میره و بدین‌ ترتیب مسابقه تراکتور و استقلال لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30956" target="_blank">📅 11:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30955">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvlj2gN2k1-0uSllnnRkBevkB35fF1hg4wwlwWyLHkGJMamqNnXX5zjJUq1W8uCAEI4rMXy4FvcvXphbaxXgtSIS3mW0eS9zBRmSlvZiaB2olI0G2eKWqHGyrz0D6HuqYzMNpQQtbRSG_VN1DmYzMJycPFb8W06Xua6RGFL6wT9ZZavHeBf35oZ3KSgVw7_Dph7GTZWUvYCQN48xUT0zBZ6xF-Ujk2PIMUicGwX4AEiSOu5zaDHg_afi-huu0iUPJayJF-HcW4OskbzHvilRdZzDwRNSpb7krrKKsM-Jwy3q7OwO0k5-tIY8dArVLObLOKQrTAKbVGgDFr-oiZ15bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30955" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30954">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56284423e.mp4?token=q8-EFLZ5FAZK0qCWuRbtvFWpkPLS0eG7n0g-nBXQxhBsFMvicYJ_7hycapQjJyI7LlU_x4J9lVO3Xz760IBA8ozSKJLIw2WPccStIH08I_n3Av9uwIG2KwRIAf_ebBNyFDEPU48jn7wQJaRjW8g5u9AChZEvmVK_7USDiHqhvrRikTTY1CzqXr-zpzfTRoGVyiDu_2sZZaW--rSRXrSmQ-WEZrUZ8ACG2Y2puuft1BAJ9PLxTfVfbRwtwQcz7OgAfLGhhoF3FE2TuMmk3TZatOTV35PCZM0-zACvGbi2CbIHg6_Ye9xZCmSBhnoYiN-A-Z6tfuyZN_bBBlF3znVXujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56284423e.mp4?token=q8-EFLZ5FAZK0qCWuRbtvFWpkPLS0eG7n0g-nBXQxhBsFMvicYJ_7hycapQjJyI7LlU_x4J9lVO3Xz760IBA8ozSKJLIw2WPccStIH08I_n3Av9uwIG2KwRIAf_ebBNyFDEPU48jn7wQJaRjW8g5u9AChZEvmVK_7USDiHqhvrRikTTY1CzqXr-zpzfTRoGVyiDu_2sZZaW--rSRXrSmQ-WEZrUZ8ACG2Y2puuft1BAJ9PLxTfVfbRwtwQcz7OgAfLGhhoF3FE2TuMmk3TZatOTV35PCZM0-zACvGbi2CbIHg6_Ye9xZCmSBhnoYiN-A-Z6tfuyZN_bBBlF3znVXujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از سوپرگل پشم ریزون ستاره‌های فوتبال درمستطیل سبز؛ گل‌هایی زده شد که هم‌تیمی هاشون هم برگاشون ریخت. عالی بود واقعا. از دستش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30954" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30953">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0ebH4-8WRTHrBLQqcvuzqfqP9JW2bPO1-zsG8ABWQgGTfcSqUQedWiTJ4xK7FSNfr20Cv6vx8VL3KhzBt2r40Z2hVquGWpxrk_w3DFQFL9O7TujA6MGLYDknRR2Ya7PwEVGvIs1WS0X9NvZLMTBbBbL44KraN82lDVLKhjlSXNOIEL7SzOOAj4Is7Ux9m7bXoK2caGYmuHuXfcEhtyfg1QV3VKgduJIx9qrMtA7ttDJKpEcE1xcpdpkl6TlV8UmwyST3vR-kOJ-JzxP6TWAqHDiIBrj_kJ_eboh3WF_SdwytL6nK35uRexR2PoXMf3J_yHg9b87L4lPyVpAlUSCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اگه دیشب داخل کانال بت ما بودی می‌فهمیدی چرا همه  دارن درباره‌ش حرف میزنن
😂
🔥
😃
تحلیل‌های جدید  امشب
سیف تر و آنالیز شده تر از دیشبه
😃
♨️
آرون تیپ=
وین
⚽️
✅
💵
😍
فقط یه کلیک فاصله با وین داری؛ بیا خودت ببین
👇
😃
JOIN
JOIN JOIN JOIN
😃
JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30953" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30952">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=dLOgHLm9wpUa084kSpHaleRTcCyRmSCw7Baavs81N9CqNsbPclcP6Hch5SN1DryMULtnBeDsCmwjNI9j27XmkAxd6d5isSCpQlGOKo-2ynAsqbod2Dns8VQ8LBdwiHmmUPKC3qKj1nw4FaYb30VmDCh2AqUxrE8WJ0oIBAXpE0AtYqy-a9ausBpe9gZywC1hibBL0TAbM3Az-pCoF7H6HtE3rORIqQdq_NJNMTfpHCJMkQX6cLCsfwxDUXT0_n3re9VlszdaVA8KZRIlgQDqIujQ_M8HQlNu3s_lAM4AUYCZHLzi8Hl4vMs6BM3IaIkwBCvePbf6eqefTZp9KXK1XzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=dLOgHLm9wpUa084kSpHaleRTcCyRmSCw7Baavs81N9CqNsbPclcP6Hch5SN1DryMULtnBeDsCmwjNI9j27XmkAxd6d5isSCpQlGOKo-2ynAsqbod2Dns8VQ8LBdwiHmmUPKC3qKj1nw4FaYb30VmDCh2AqUxrE8WJ0oIBAXpE0AtYqy-a9ausBpe9gZywC1hibBL0TAbM3Az-pCoF7H6HtE3rORIqQdq_NJNMTfpHCJMkQX6cLCsfwxDUXT0_n3re9VlszdaVA8KZRIlgQDqIujQ_M8HQlNu3s_lAM4AUYCZHLzi8Hl4vMs6BM3IaIkwBCvePbf6eqefTZp9KXK1XzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30952" target="_blank">📅 10:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30951">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=YSyJwFi04IWn0hLxHriYlOpmOCYT3GChAlAr5k6ZNCGRoAZdxA3dUQtN7GQHQ22bwcb5L07PIcdfnZJuKEMsyQ8jH4EOYtEE8vbukmPwBB6DSqLNvLJtOH3neL3n4zvOdN-wnJlqatdQmbe4_KhLBHHLFfSdSy8bC80dn5CjCs_o_zw-MPmI_6E_MlbvhiaMC_cWnKJlVQ1ERkJU7KRciFomKElPs_pBdDlc1cpU_q_Qed2ND0Ly-0EKMdgXNzOtfsy2EDqrjwqne75eZQym1VS9MCyLXPka1gw8NyBrBj6bnB1zik1rAXXIJrgkOjW7c1joMbm-QqT2yDwg9FCpzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=YSyJwFi04IWn0hLxHriYlOpmOCYT3GChAlAr5k6ZNCGRoAZdxA3dUQtN7GQHQ22bwcb5L07PIcdfnZJuKEMsyQ8jH4EOYtEE8vbukmPwBB6DSqLNvLJtOH3neL3n4zvOdN-wnJlqatdQmbe4_KhLBHHLFfSdSy8bC80dn5CjCs_o_zw-MPmI_6E_MlbvhiaMC_cWnKJlVQ1ERkJU7KRciFomKElPs_pBdDlc1cpU_q_Qed2ND0Ly-0EKMdgXNzOtfsy2EDqrjwqne75eZQym1VS9MCyLXPka1gw8NyBrBj6bnB1zik1rAXXIJrgkOjW7c1joMbm-QqT2yDwg9FCpzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30951" target="_blank">📅 10:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30950">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=WtElvNLSq67tFwwSKOhsRuhbo5drrAvhBr6-9Jnz6PD7iySADFPss37rxJAN02BaN61iidVOs34orri9_Bp_YFUU36OEAznIUYqdX0VqjgXI7BAvNgJBsbKAmkmdhWP_w7foSrj9VFxhBr09vzAIjetDsUhkO6VfCD0J6SpGCsBqCQTe8MsADhgDs9yg-R_G_A8eGKEAqdv1-r9GeF5_6RqRjQOZJH_P2Jvynykfb1cqa4xxm4LAHTlbu3wkEry9QaJLm7qYPR9k-sWAJDJDAdDH55yIlYtHV5ZYUBKrlL4CPBWkyRIxxAq7SCZoiqGIGu3YUbwI-kjLfh2hGUV9CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=WtElvNLSq67tFwwSKOhsRuhbo5drrAvhBr6-9Jnz6PD7iySADFPss37rxJAN02BaN61iidVOs34orri9_Bp_YFUU36OEAznIUYqdX0VqjgXI7BAvNgJBsbKAmkmdhWP_w7foSrj9VFxhBr09vzAIjetDsUhkO6VfCD0J6SpGCsBqCQTe8MsADhgDs9yg-R_G_A8eGKEAqdv1-r9GeF5_6RqRjQOZJH_P2Jvynykfb1cqa4xxm4LAHTlbu3wkEry9QaJLm7qYPR9k-sWAJDJDAdDH55yIlYtHV5ZYUBKrlL4CPBWkyRIxxAq7SCZoiqGIGu3YUbwI-kjLfh2hGUV9CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون یارو مجری بیهوده یادتونه که چقدر راجب فیلم عروسی سعید کریمی بازیکن سابق ملوان گوه خوری میکرد؟! دم‌ از شرم و حیا میزد! حالا در نبرد دیروز تکواندو این الفاظ مثبت هیجده بکار برد!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30950" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30949">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtQfx4wJrgfuDku7LSROsPmXSvwGS2Ph2QJ10LvU07Cvk08T3uLBolYwCdnepsXUattEE8hFHNGDROWLZ0rcNDBe3gw1LhMLCeQv8ipeZfg39nNHMXocWk7OLD3304Whf5RLuUQ3IebaDycSqqUNZ1MKmV18A8_ZQDWzklczCXanbMSAdGAyhMzYR7VmeLspqgYlGB5XNkk7u0eSnPIE7mqmTbphRt23xrmU6V9cZbRXbvjH-iu2oMs_RBc1eFRX4L5UMf1X3njhIpxk6yDH2XRBNE-FgUIzZP9OihJFybtCWmR2tKTtmpn-UTHSls0iamaFdl_slT2kuIM8h2NAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای خبرنگار لیگ برتر: یه خانوم در کمیته اخلاق اعتراف کرده که با رابطه جنسی با چندین داور، برخی از نتایج فوتبال ایران رو تغییر داده!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30949" target="_blank">📅 09:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30948">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCRx87dLHvGPl0eJtCRAbg-dxkLR2VpQaza6EirVwLMkffKTaboI8PmV6k1Z74FdpQRi708884MWlo5ZYKzW-u-VLY0Sj3tyGZeqUWiAw0X7ic9l-N5yDb34ZOCpfFqEw425ioFi8TZU8ADJPUhAWmGm2QLCgjVaxsU0lN7p2shC0Xdel5No8ehnxMR6MJIRXdnk-TvnFnYReY_Lc6fo9qui63gbVmFsUobtZpg1APs04n0NA63Xph57XMsPbC1VxAlK9fUfwJnNdaG5PFuEHEqcs_-TfPIMzsQ3KDAaO3fl2aDFFvCnG0te320fPeeYRAqqBKWhopFXgDIz5gsjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30948" target="_blank">📅 09:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30947">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htf2yc7rl3f__1bHhjM4jp7KUyqXak5fRC4KvqYUzU-ePYDlYcXsFar_7JS_aojD7pkFfAhAs6NMweXefF9XlMjJcX8cHlD8gIlVQI4Q0CdTKgeIZnpQaJ9d45E6d8vX0u9-BmNGqpPb5vOlIWBGMIoUuX6HU346GkxaNTY-MrFgUlOlnx1bzFH-tkF76RkiBDjLD3VlB0IzAj6R_tN3nrrElW2LMK-xxZDW6C1pkh5oeiY315MOe2SshfNbepMPHXEwTGhv9IwdOtOmCNtF_ESPfiutlT1YAOTCXx8__OcLhgUJXSQ99SfO1GDG6XQZ5G375Yyjzkgl-wmar9BeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه روز پانزدهم "پایانی" مسابقه تنها نماینده باقیمانده ایران در بازی‌های آسیایی 2026 ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30947" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30945">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdbSH_Livv1YaKqLu8kHetb9Ohx67Dapm3lsLYUN8i7KSyN2u6N7sNe6GLLnyD0251sqfwsyz277sGyXuLm8E6RHt8l3uI1yvERLMooSlSnztrAak-vbFqM3FD60vzIxHHD8DutvBQCOiRTDQN-qoPkMOEpgwUtZJaEJWZqBMixUJ_nYPs9693rFRE5_OJqnnuZgdFqWeOPMrCb7fIZTxdqI4SAQHSEfr7XyOdw14-0TZe29wcYB26Gp8VfPQc4TaqJsvswdk5wWy9NWGX5BGRRDOo41gtXUU09_36L3HzQwHcjZtTHVxlf8aM_bifVcIdzmENck9uCzsGKqoR0Jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز
؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30945" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30944">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHaHkfxPrkBKXLq7Gvp5AbW0tLhQB3Dl6DU8SY24wfb5GMqYgmHQghcn6l6OJbjKggl0V2oa1kHVeuBOXyd3uqzJuGo17NCaAGrlG-ZfVn-ZWmisjAgJ4m1jS7WSD2kLYfWx-LxOgtQZX5tLKIn4FdD6SulmcCRQLsZbYjKfd5jGVmhdP_ZOaUNa6ZvUUAliJ6jVzKq4p4-pkZ1igMubNSJWmiLhX7WY1qjUo6dSddUi4rCVlQG2fknU9We773pR_tNmiscoy5og73HFEzNl32soTGro8c8kiBuYnFkRULeKoKkolmfl45Mv2I5ok8MTCrwu_FyYnHj9K_zMkdGtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
تحقیرکرواسی‌بدست یاران توخل و ادامه روند فوق‌العاده اسپانیا با دلافوئنته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30944" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30942">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=JWQ4PSOJPsSlA7n7zq6OsekmAGj4I3rZCKexAFLqhosVNabYdYWCUejjlLXAcYkbR3o4yGWc7evEYg5tW0He6SoPHy_HkWabitv1qwxKkuljaw2zqTeV7FRWs5v5uXkGuXmo-atTYue2RQLHcEXXtL31p4avsOTwBXVng8CQFO9D5tPNP_rcpkoX-oUf49Tk8OofoXKEMD0cll1sF7eiA7x5eqv1hQQY3yDq2cVZwg9ie-qUJCP8zbMvRO7raHEyoKvMFyD2gHKEJf-H28ZWzcx_6VCynnPNE0Me_BlEV8qG3sySqz8BHvnuQOQ3UpNbQjRZCyfspmbgZSv43A6pR31ff7vnbeMZ3GL3JqlRBah1xICdd0bz2yFc_MUOuwf7tRQlFLKIi23KhS3w-yxWV_vNVaIW5tvQDQfxWtMLj0yjuRSfJZF-I7eORrcIKdb08w20HfFwIV9h4a2c_92Hyf0XzBc9EoBvZqvON3PKy9xnVwNNTsytIGyXTNPzF8d9tNnRWMrYRIDH9qycGkIu4iXd3PZWSwKjN5QBkj39AykwODb1Vk5MQi5kmY0Ectfz24r_tQpdqezGnaQ6pY9d5grNlGIFPa_hxLihFnzkKecY7oXwK9Y5KlPCaN_Dx97c_d96uAl1EU0tScROdGEjDnHtwQdjamC9cB5XfKwgz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=JWQ4PSOJPsSlA7n7zq6OsekmAGj4I3rZCKexAFLqhosVNabYdYWCUejjlLXAcYkbR3o4yGWc7evEYg5tW0He6SoPHy_HkWabitv1qwxKkuljaw2zqTeV7FRWs5v5uXkGuXmo-atTYue2RQLHcEXXtL31p4avsOTwBXVng8CQFO9D5tPNP_rcpkoX-oUf49Tk8OofoXKEMD0cll1sF7eiA7x5eqv1hQQY3yDq2cVZwg9ie-qUJCP8zbMvRO7raHEyoKvMFyD2gHKEJf-H28ZWzcx_6VCynnPNE0Me_BlEV8qG3sySqz8BHvnuQOQ3UpNbQjRZCyfspmbgZSv43A6pR31ff7vnbeMZ3GL3JqlRBah1xICdd0bz2yFc_MUOuwf7tRQlFLKIi23KhS3w-yxWV_vNVaIW5tvQDQfxWtMLj0yjuRSfJZF-I7eORrcIKdb08w20HfFwIV9h4a2c_92Hyf0XzBc9EoBvZqvON3PKy9xnVwNNTsytIGyXTNPzF8d9tNnRWMrYRIDH9qycGkIu4iXd3PZWSwKjN5QBkj39AykwODb1Vk5MQi5kmY0Ectfz24r_tQpdqezGnaQ6pY9d5grNlGIFPa_hxLihFnzkKecY7oXwK9Y5KlPCaN_Dx97c_d96uAl1EU0tScROdGEjDnHtwQdjamC9cB5XfKwgz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30942" target="_blank">📅 00:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30941">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko1FL20jr0MLUIX3JEXd7cXfqVG8gmd13rEFReGe9lopcBwKkYhPdm46P1SfwActe6X_jRLxAhWYQL8k7CcrpSthEIPvKYOfHqj3E0uxwci9uvRMA-Ydlep7sYX7hHAYu768idj8fNT7djHhyEBfkMzRWu39FXQUE8yNEEL_n3gRmQW9wQEf5ckPJwM2XSiaK0734gExYuL2jMO8Nb8B83JnTPYztmOJgGiwSFaU9CDQQVEW6fv1WaqJcugWdnCilDf49OXiAlfrMtrIT_C6GmIm3XKColxZ00FDx3tGHcOJ_pD2ToLF4KV5QLHXcGkdo_GgljkXJoa3L8d62zh2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌‌سوم لیگ ملت‌های اروپا؛ لاروخا در شب درخشش‌لامین‌یامال و گلزنی‌رودری با نتیجه قاطعانه سه بر یک از سد تیم ملی جمهوری چک گذشت.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30941" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30940">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30940" target="_blank">📅 00:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30939">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov5rhXuDa0L-HkqK5f6-j8YB1koBcEBd4SayhPQkywZnV6Np338Tx5n4Ob81fQQp5gmZzz0Wo5PQt93_8WSg-d21Ogjxd6qBW1jO4ILUF7rKsRotxBN1qfwMpHrpjw5G_zdSk7L_SItMhAZD9_9IjiQrdniYfaK6p9ohHx9ARgZCW0XI1IyB-SW2m5eWJet5ONEz-1sKoU9umVcHUEPXIrKTt4G-fMB2Waynh4YX2JdPxua7DuvO3z8ShvT_W2kaiV3BuBy7uZ9yVhMIFwjpomssh0IIGZPp3MQnvJFmEK6lFQ58MBkv_5FCrHPeWnvWIGGIOJ-vYrb9oqZ8uPApjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30939" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjXvfr-8uRL_oGqQSUGifMvm2mktGry1P3h9viAqZEq1BkwrXtW-1UcmViJzj-8gqlx77DG7fRZdGG8Xnvxc6mD2GifUaJfEVRdlu0TyeSqf7yc_vz0b7RjSI4Hsxe20sgtcq8KjhXhZ1alg0D6Ja2jmFwcr6zH5o0XgUgoS0KFvOKHtN3Y1WfA5KZ1jabB1AhVTrBge77aKkn384sEueSK65IZTYHPl87PxqJntczeODOvQiriCaojonZ3X9VGCeEQvRbLO9aGq8u-czY2UgeEMimuI0w9Pi7z3PfpqXz9ZC7aSq3EEjSyVJGfEGeolZByb0B4f1-G9Pilg9Tdvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30938" target="_blank">📅 23:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNYWvu05CkPTcN6Xf1ZUTv3G7VKtEgKmyapMMEa_POHWVCEm4TwljnuRMDEU2WmohA5Mnyv8G6hilqfFqMGq5oo9rKpDQHXccUn8xaEdQGfgwWzCR6uaB8wvnUssxCEsfe_ctZ2n4HjTO09JsxpWlwOuRLhoo9aytHTUuv_lYbHpQ7XFzdL5Vz_go7tEsyXyDkmUiClcqPOFz7u8ZASZDger2AMpnUKSoT7haKuwphpIQsWgulveAtIMNX60J8KNtZyp5os7rvEhGuX7cTL3l32d85QMy1s7asWFvXWGm8MjwXqlsKt-HAlWL2j4VPMj6uwixVGg4XNw7SPNDp0Mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30937" target="_blank">📅 23:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_xrSkOnhioBuYtMqkGDk_zUP9s7N8eALJPMk45eAyc07OeCdXG2r67kl6w6uvf3vll8LF0gEXHKBwjdmUJDDll785n9ixLG1E2aN3D_xAL7Oc1aZ6FDisk1X49Nyz-AbV91VRMxWUuJw_edVi9P1TGOOtMP8AyZjpaM8uzHKkhhQGN6ltMgIEFkbq3kVeWCR3C8rM0-WvX0njJqZfv4QduiHvYzNNCqcyiBk29vHEpFbAYHVVkzCHUJDgsGZ225a3XjzwX7pX5MeB1kxdnpPyG06Vpox7Xp-tRk8be9UEVlQSoN5GYtaXlCZ2olULABbQWqNGS_foFjpSiI48HeIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30936" target="_blank">📅 23:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30934">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=AB3rtA9jx6Psa4sCtZE8WW4tX9iImWD1IIKCAFXUvZK_yyi_83kseAwxsRONPvMm_t-yBXvRYJXXQ39cJmZn6XwbaYs7dOfXhK9i-xrIsWcyNk7yZgYTNGuvxYY3o0hQ0tm-1blS_yvL32voeQGAU8hiUyefPoBPZJSRefhojvoW4DMTTKmby1pISlla4_Bsv4Ap8nhD3O2MCORyIFD6KNg3W82a3BUYOo2e1Uv6RABVF40hRECryHu58ntOMZ0ekOeDHWsMDWr4kf89S4wvMobp1MJFUrWqGTaaGv1bwPvWT_o-1bAK2X67N-hY2FCGLPAy-3PpYTdsm_obVUVASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=AB3rtA9jx6Psa4sCtZE8WW4tX9iImWD1IIKCAFXUvZK_yyi_83kseAwxsRONPvMm_t-yBXvRYJXXQ39cJmZn6XwbaYs7dOfXhK9i-xrIsWcyNk7yZgYTNGuvxYY3o0hQ0tm-1blS_yvL32voeQGAU8hiUyefPoBPZJSRefhojvoW4DMTTKmby1pISlla4_Bsv4Ap8nhD3O2MCORyIFD6KNg3W82a3BUYOo2e1Uv6RABVF40hRECryHu58ntOMZ0ekOeDHWsMDWr4kf89S4wvMobp1MJFUrWqGTaaGv1bwPvWT_o-1bAK2X67N-hY2FCGLPAy-3PpYTdsm_obVUVASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30934" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30933">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=lnrlG7M9coC9VeSVjeH1Bvi4z85jxomeys5JBMHkt-h4qTXwvvSFgzTmUhyhGy5owKXsOr9gFCSTPaP6yRcDMYVCgKnQxk0kzxNYgjZRTdKKYZB5MRDDqlZ89YmWQf_x-APxP74o8WiUY686F5VU56GUq9qzltIYNPi3R9Zqzad0T12FdgU8DnMDIrn5UVWsrOHKnuTB5_DGcDB2DKPbiFeeVwBMWFlYiP5W-EZoNVJp-Jvbbu6uYjciGgecoSRZvaWol4z-FSpa3dYVVaYGeNmfMxeVPTUvjrE-tkAyWUmKM2SlHUybqkU0xq37XozjRHoL2t8jlUGcHUCYVCF_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=lnrlG7M9coC9VeSVjeH1Bvi4z85jxomeys5JBMHkt-h4qTXwvvSFgzTmUhyhGy5owKXsOr9gFCSTPaP6yRcDMYVCgKnQxk0kzxNYgjZRTdKKYZB5MRDDqlZ89YmWQf_x-APxP74o8WiUY686F5VU56GUq9qzltIYNPi3R9Zqzad0T12FdgU8DnMDIrn5UVWsrOHKnuTB5_DGcDB2DKPbiFeeVwBMWFlYiP5W-EZoNVJp-Jvbbu6uYjciGgecoSRZvaWol4z-FSpa3dYVVaYGeNmfMxeVPTUvjrE-tkAyWUmKM2SlHUybqkU0xq37XozjRHoL2t8jlUGcHUCYVCF_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30933" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30932">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AH1qnY3iGDlQC2Iz2t832oQQ9ASW7hAI9RrS9o9Psx70c7RGkuY3Dlqx08zcwhuU60gOqKut4qlaCkBwYPOG89hpDfckCnpIp-GdNO66FKBaIMgP1PIzfuTPdt2Hv3S6CCLTjg1Yi7oBkd5mF_MBdupx_AEu6z_VgnHTteSWdcLzWeKrAnjEnnc1Ta4a8Iw88H3nbxGVJ_ZmD577kc-7m6XlZUwtU4E2FHW4OBY4lgnkNYQbgsRn8ouPcj_oDlaErqgaFuaLJJdT5068JUga9iUTbComwORhOwCa9rGTaFkCX6ovAfiTcP1d6ozdskSU-H7NvFqkJu0XWqgAGJoGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30932" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30931">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30931" target="_blank">📅 21:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30930">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j135yDJIhtaqmgYG-GnN9vQnQc5JPmEDOo0SL4OBsfIkNZ5uzVSsxarUS8lcGFsTqyn7vd2m_phTWkdhndSKO7lmnZ6LfY6aUL90SmLo1IesSU1MMpRdGafD4yME91QN_BS3gUWxfsj7gfVDen4BYYkCmdJ693xlWCqWvxpNTr8hVtUyVtHwuQAPB1JqPp700PBINS8-Ab7jSYfgBqsiW74ipf_XIkecGcTJP9PL3DtBZvfhsS73kjiYaYmXcp0ckOKStQ5VseKIp0f9AtANQuQHlUPJUhyZZAfSpeVlw5VQ1Qnnk43ZLVjq5Zn8n8gLvLw9W-iWd18HQIBaBEhv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبرگزاری‌تابناک:گلشیفته‌فراهانی‌بازیگر سابق به زودی برمیگرده ایران‌وکارای اداریش هم انجام شده.
‼️
درروزهای‌گذشته‌آهنگساز بیژن مرتضوی به ایران بازگشته بود و رسانه‌هامدعی‌شدن که شادمهر عقیلی و معین نیز بزودی به ایران باز خواهند گشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30930" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30928">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InvRVdori2Hc9jZraDgOBOeppoeAn0f54C7GGtF_nEcNo3TPBUgIgbb5-xM2tW3kfTFgPKtbRz6XN5fYGRV6fNjGLl_mLw-NTFMmkS3UsqmzGIov9TQzOKw5t41a4-GyZClrlIm6jObYC6Qgm8SXvtjum6vmIc8g6gGgB2zlHxcbDu9Dy6p7KUvCR2apZoU34CH5kX2xaZLw7TC5YTjVtmM7BJd8iH7aCL9ApWBmG5sTbBkXD0L2p059bmsBrx5onYecH5KTMMh2ZwoZDelCfvlPrSR-qOvj6RPQEcHWK9LysydgtNBwzlwz_4ShCgLo_mZrH68UT2Gx199AOnMbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHwASPS7POUMCf45Y52dn7trb2N8mWWovdYBp6YQLY4yFsLk6ONDjIRfLyLBqYJwjVKzRxpEeEH3cQA5y4VninHrP4EAWeS4rCBg3ReI5wdxUlxehduFdqlBmjVUm99I7x7Z1tIrdpBUF1HoRI9ymlEpKn9Fi1FdY9KvqlI3h5lWZvoCYvMceN8aXQYU9KclD5oMTPy34Wk8emxJ4IeGg4aryhAp2KDvQAqdLBllmAUR00efYg-49tfe2ps2R31iup6ft8dXLvpk7IGxdH_2v3vNs80OhNR0MBEVv-pcNOhV_T8RMCcGuqCC-9iH5zcLwRNVBSpN1hAmr-HZw3xNFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرنگار شبکه اسپورت اسپانیا و هانده ارچل بازیگر معروف ترکیه و فن شدید منچستریونایند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30928" target="_blank">📅 21:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30927">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=PLaTulMm9BCUSNLLom73pqL4teNlmki19Fyq7R8ngC5f5x9qAlgCcAiO9IL0SVochMv74mT-IUNwUHTGWJ4GwfB-UnCUHxme-bpLWc-GP440_KSyDSD-7bT9mk1Nr9Htm1phqy2F3SwHZcMDnQlHlX8bje8dlh6Wsyva302spZja-4FhM_5NjrzE2s4CuLqpSGq1NqqquteWLDiped787erZFkwedhIMzEm4biosKpgkXtScArcOmKR3UJZNs-NuUwGenISQFNWrt20MLYRymXiv861xUfqJvlUFdTznYGgSWNG5RAM9Lj_vWwNotG4vxFvKQfEhx7-oIe_GvaF_N4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=PLaTulMm9BCUSNLLom73pqL4teNlmki19Fyq7R8ngC5f5x9qAlgCcAiO9IL0SVochMv74mT-IUNwUHTGWJ4GwfB-UnCUHxme-bpLWc-GP440_KSyDSD-7bT9mk1Nr9Htm1phqy2F3SwHZcMDnQlHlX8bje8dlh6Wsyva302spZja-4FhM_5NjrzE2s4CuLqpSGq1NqqquteWLDiped787erZFkwedhIMzEm4biosKpgkXtScArcOmKR3UJZNs-NuUwGenISQFNWrt20MLYRymXiv861xUfqJvlUFdTznYGgSWNG5RAM9Lj_vWwNotG4vxFvKQfEhx7-oIe_GvaF_N4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30927" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30926">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=Z-QONyMorGOemQgFLioxxs_RCY2A7x0ifhZWn4QCx78PYz1FL2pGnrJZ6aAFyzDz97pBDs87iPcHtiJyxXmDZLkUtThi7IOHLl_nqPWzE1vct0-bzDTxwn03nOlkSvpeKR8u04JVz2P1NjrfFvpH3_Q-S6PhTXXz0hds67EWY64WQvOUexPrkFQbCcYxeTd2zsuyLTAT4SLX4RJXoUUVDWy9kcgnnE2yboaE1AO39JYkyVadD9Ke9zg_8wrPujZOFpMhmHgUVySoEx9xRUtYOqHBog7olJdkKWtDM_OwmtsU4UGDUXneMO18mwYHyBqcsaT6WyDj4ZpQyhfxpzx-LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=Z-QONyMorGOemQgFLioxxs_RCY2A7x0ifhZWn4QCx78PYz1FL2pGnrJZ6aAFyzDz97pBDs87iPcHtiJyxXmDZLkUtThi7IOHLl_nqPWzE1vct0-bzDTxwn03nOlkSvpeKR8u04JVz2P1NjrfFvpH3_Q-S6PhTXXz0hds67EWY64WQvOUexPrkFQbCcYxeTd2zsuyLTAT4SLX4RJXoUUVDWy9kcgnnE2yboaE1AO39JYkyVadD9Ke9zg_8wrPujZOFpMhmHgUVySoEx9xRUtYOqHBog7olJdkKWtDM_OwmtsU4UGDUXneMO18mwYHyBqcsaT6WyDj4ZpQyhfxpzx-LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حمایت جانانه و قاطعانه فیلیپه ملو ستاره سابق تیم‌ملی از رونالدو:
یه‌تفاوت خیلی فاحش بین رفتاربازیکنان با رونالدو و رفتار بازیکنای آرژانتینی با لیونل مسی وجود داره. من‌میبینم که وقتی بازیکنان حریف مقابل رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو پرتغال هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمی رسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ واقعا اصلاً راه نداره!"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30926" target="_blank">📅 20:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30925">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30925" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30924">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIhAeprLhlvTvanky6kNYufNRsz0fOMlEZMRgxxvyPbyuhZs3mlcjqR7SLVhUBk1oY9Wc1pQrcA2IvvA80Mn24m9cNCYhdc-_UuVnlJKG6yKNZHd70t2LriUdrWUQ9oen9tjaD_4XiFqGionz-eZZty3wU4qUJUBvSSkDjbZ6Mw5UJacRjQxGdFgPcT25ILQg6bNr0MhDSTTRUnUJbIi5DA08WLJ4C7a-UA8DBX_IUrmmmRllreMaEZYhLD3rx-MCWMZ_zjgLPpyjgEa6H6PohqgQY1v69if6Kd79gjW8FT2J7K1TCxXxANlWppAsFBJScEWf7RTEj9CBGHlCHyEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برندگان مدال طلا، نقره و برنز فوتبال بازی‌ های آسیایی در 20 سال‌اخیر؛ ناکامی مطلق امید ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30924" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2e3a0sCkNLdk-ThxD-mF3DInQEptEaVp2Mcnldikto6a2icTyf2_EHT5mypb40V3NgrRWITiQXatc0zi2StuJmCPj8hnnkMdTv1Iq96YqY4x7KM88G91dWQdOTU_wpdCbmJ4M964a0SdvxThR4ThWBUNCQ3lg0Zlif7VHx2lvgSLUdG7XVpZ4350d0ed4zmiak-LLqTGpE2lnwcutqcsDX0XyGi28KaX1E4DbMjN9mZ6U1GLlGDpCvEep_uJZHbCmFMYeSf-w8EJae2kyu8ULTW52-M4CP9cVz1dL6sZgAhZR2QjxDPR5RUjf8i0phNzz2Utv0XqgSZzJfwfKc7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30923" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2TpQIA1MyEuq3xBZ1liuwCdKpXaTxuLljqDvnsTyp1Z6qVBqbLdPJQJeJZhy_V9VjS7vWrmqT_6Ru2RdKA3CJZKRHA7PUFcfGmIM7yp3mqKymaQ9IT-NPiPjbDFhbomUAon0Giw2m9ouSTXZs99mdGxQJNvP7dfGgKFGgnJnR7y9EgiUTCTCR6zw5QiQ3UDBcJWj5xWt9K6vuy1blO_GKvG6zFwcvk5VBx1QCigQB6NyPrdIQuGxDiCzEFBNr64J2ZgOm0GcGS_Y2tX3YjJYp8lrLAdh9sjqUanyxKRM6yvWLeD3lH6nfmlC7bt5MXvivGyLFGOivmS7ez430wEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30922" target="_blank">📅 19:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30920">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jteb51UB4_XRsjtNqGH7Uy_vXEexe8LMD-DorZK_GkSQVk_JdM-kZG3aFJziU04CuxkDMy4Y4qrNs3lr3YtKuN4wZ9dFP8KUsjfynHEtAjwiILKFOWG_n1gcan6plKrFICjTvf0xKHQG2JaJLITVrcrV4AL2TPsHuzLnGdOTvsdMe6puoqx_ElcV_cYNmCt0rtzPo0SYrVOp-pNjzkQglvcPSYSEfXWYA14ObZrRQSkmybYcAvsWVS_6Z7z5OvSFF3XYxCSJhnkRI52UvovgxYbuupIUF2MV3LaxMLBOsutvEk-kofJfohFdr3kJs8GvEals8Bda9lOOKGc535Wofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGNo292ZFNg7UtII2WQjJ-qJ3dPcKSn8s-AjwDcC-Hf6So6BwDu8Cani5qXwkVrfG1sGYUMpimxFCi-03RH36ZCKVsp8zeKcRq49SQfR3yW3aIWufRGnY7TYHdetaTP4RX1unVMe-3tX_5vSSVIOu9NSEiySXDIBWOEidEncW6FfEJ5s3tfbXb4Pm490PB2Pwv4riG0-Lr-0niDshvDg71vKQRcVgL7-6emD30KTIe6J0ak4HATyWuW6moKJz3F6-2CxnFe_uGLcqePmiSp4R4Zlgrr-OP_EbslgYq_qb77zQ5-sEDvidI-u8OoqQfxYDp3UqBOjAOi2wA2eZvaw-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشک و فیزیوتراپیست تیم‌ملی‌بانوان‌ایران؛ روز فیزیوتراپی رو هم به‌همه‌فیزیوتراپ عزیز تبریک میگیم که‌مشکل‌بازیکنان‌روسریع‌برطرف میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30920" target="_blank">📅 18:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30919">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErYQfcSLSSq74yKMy2THStmwaX2I78ttjVtFBsU_3RtW9B3Bb03fppvautpzjGgZkgV4fUIZkxgB4jPyJtpw2LXhv2-Zeyl6H-c5waQUwwzh26LZBeOxx6MimLA-nkGsyDwfiJ4tnupG2HuWHfYXTSk860pC7O-N2824lzXpc-QkE11G6VlLGzs9eQ9CXzeI_adiybVteAM79uOux3qo_akuYLlfRurRoyU4e2XKLVeurBa22pW8xybtHVaw8o-8lK-YFRkPMQgZCY6vUAIYhnoFBwra9NHE3tCWuYQRCNoKm6-k_a6ZEAsEuq7OeyEnUotmR4FyCDT48vhPVSZjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
عملکرد خیره‌کننده و فوق العاده لیونل مسی در دو نیمه دوران حرفه‌ای خود در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30919" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30918">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMNjfhfU779zlDjG8jW9GvlEw8tlZOCDfn4jhmx3rQ7_IxsBQEwada77BJZmlt6dIjHmd41QLcKzh7SaA06Eo221CJEnNcenuo4CNp7lAnx5GJdY9hbTRqrFMZymERlBOIwerUYWdNogBKBNI1a-sRi_-OVKuikBVgdICxFqWfnxbD5iYWozoS8j7PPN-YQQXbmbZfJ8-a015FgkcSV_HL4NgueKPFLyKeJebWO_4B4qnT4PLd_LshkmNmOIKgdg6Dr27sXKC-Sms13rhzl8OoQeKGx8oo3MGSCiaWclJkahHlJtp-tt5FHyY2nRGGuubK8r7_edMRKF1qKM1q1hnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی کره جنوبی در فینال مسابقات فوتبال بازی‌های آسیایی ناگویا یک بر صفر ژاپن رو شکست دادند و قهرمان این‌دوره از رقابت‌ها شد. دولت کره بازیکنان رو بابت قهرمانی از خدمت معاف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30918" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30916">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlhvcViBdUeYkyuyu0ktBlLp2eD8m0SeN8WBBsxnIur5xxtBW7X7nH1Q1TF8Ooh5LeOT6JViXEFBO2H_bNkKM0cGJLa7sl3CO0KRtxp6sgEW1PM4hcwUIWTqdjVw8r7gjw0-_OzMd-azW02hcaoI8mewOVmIExeUp0ag22pCDwE-kF3Ou3FNcjBoJCYr8HSmrfM_WPNgGy_JpzztmXRAcvCj2shxsxJxEjVOIUSO5UMsnByTTo9Acm-jE7MavZggJovR7G38nz0fJsxJrwd2DpwS0jsW4oRRD9siv_l-DoN5FlnE2Y_l_QP2I_FrnTTiX6sWFgUh6fQm7dQ65UdqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فیفا باشگاه کایسری اسپور رو به دلیل فسخ قرارداد یکطرفه علی کریمی محکوم به پرداخت یک میلیون یورو به هافبک ایرانی سابق خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30916" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30915">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjlbUcrEmZIYQKLznRkoTThf_lQ6LDAvEmFpwCIEDeK2_1mYOVuyuB-wGZFZzgdlmxrFcg7ZgbgAvqHKEykCp9wjOJNaJS0Zpi8ZNeaqGxvaUjgR438bNLKIBrRCuMOLnb2fc_cnxR4l6TH-UMpBNuqI1ABL0qMExJkz3lvKq26j8JZVdBtIi3p8YssG-bgzDd2WA6D_qsivvuzk09tEixgIDA4MSUvQ3XgfkOMY86cKik2j6eXCkJtBm4j4F9lSMzMDoOii0GQlOjawYyIiAmlBs-ipinmAKMJXPB-IhnXkwJDXJaQDnLY5Ck_oDeqRKANcDShDYNuSKSrdkih3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رائول آسنسیو مدافع رئال مادرید بدلیل مصدومیت تمام مسابقات رئال مادرید در سال 2026 رو از دست داد و از ابتدای سال 2027 به تمرینات گروهی شاگردان ژوزه مورینیو باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30915" target="_blank">📅 18:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30914">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOkxcQJuspLR0S6qUnjMMwybuY9zsjUZoEQmmE1TQm1CwxuvI_d_tB48WlAEQihxeorv9xXfFmpigH3Jg0suiHDoW_CiEFLmZ7ZdXfCSm-4t5xOkClzbmuVeM7TqQbp0L47Tjva7h6YpZJzYOYOOmM3c35GIzRUXGQptw-t4VPAHnXrn9fAeG0uyjLkoKt0KEbwOB1th0YozNeMeDn5SAqFFwaQSLrsIffR7TjoeXfJDcEGbQ_GPe77yXTNVIZY2FgwOqMLYua5r1TRurq3Ipei-CO2OSTDaHYzRCxqT_UjAelvi8_8rNT_gltwi_dzfoUfhcSrgymQqIjEhQORm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دنیس اکرت مهاجم 28 ساله تیم ملی ایران از طریق مدیر برنامه‌ ایرانی خود علاقه‌اش رو برای عقدقرارداد با استقلال در نیم فصل اعلام کرده و درصورت تاییدیه سهراب بختیاری‌زاده احتمال آبی پوش شدن این مهاجم ایرانی الاصل بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30914" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30913">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSX2-ubfwKbME9pXA9RS2AB6jcsD70nt8YQjg5OM0kvulLG0K_uexIxmhc6L_p-6LndLaiNpzNMgtc-3puE8lJuRNbRzvnXnIzr4ptHW5Vu5_tkNT7H5yCf9iiq-BGIrYbqMnktFj9fYh8u6JiQNghv9-y2Aub2_F5iuhSfjNNnHkXFYVSz8LQPLownKuAEu7Zrkd27mxgzHBVn0wwLDUQQiw7nViKwyA0X7qeZiRPzKiqxye90HeUap1eHwYS71lTFqW8te9wH_kDeuehrj-xKH8wCFqtCnQhm3w5V6TFPqHrph89m_k2hPgyecDw0UYhDn3Ab6Z2g7Xq45Hg0OEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه فلش بزنیم به این صحبت‌های تلخ ابوطالب حسینی درخصوص قیمت دلار در آذر 1404 یعنی کمتر از یکسال پیش + دیس به امیر مهدی ژوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30913" target="_blank">📅 17:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30912">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWsjlXFwUnogqJV7I9NGH-9vD9GTXzZRNXeIg-5yzGqkMbiojckdSgh7yWL_JHNC_ZBgeD6hVHooavCT2z-ZFLvYPMDcuxp4DfS43E7jBPSSLL-WnEPdbvhSLvSJWX05998I9b5ZOvGJ7ItPRZR0q1ZxvGiUrz4W6fySdx_Cm7rSIo-vucr9Rp-6t0bC8-LCXinqTuL3x97ELJnWWiF4P3Q27W6CBkJDRc0ZyP9PY7H3mm6f1umid0Ekr5e1o17t2YD0_J2M4Ho0ekr_id815D7mPx7k5kwy0V-J1g8fmAyHdqombSVvZOgqMQ-6LTS1OnKedszPPVWWbAVi9YpoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هر ۳ جام‌جهانی‌که مسی فینالیست شده تو گل، پاس‌گل، دریبل، خلق‌موقعیت و پاس کلیدی نفر اول تیمش بوده.‌ توتاریخ فوتبال حتی یک بارش رو هم کسی نتونسته انجام بده چه برسه به سه بار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30912" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30911">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZa8wqkKwGUhcuoRO-F4I7FjkSAH7FdDTmsSp3jSQpFPbOlXxWTcZPhcbflcW38nGND2cNrcf5_PWb7k_ZPHez7av37sL2mPIPjrKGqIqPZJ256e2NSbO2aevbM04568FAibRKnibKGnpmsbKD4W4M93elU8bu66KDB8civlq5DTBAIBguRJQbTCTdo5vdBSOidZ_qQsfS6IkCFOqZi3s5ihIwTsx0_TJDeqTRrHK6KHApCSWcNb-S-6kJ5-PHEVYNojf9RUwp6tgNsQScvPL-JbSLRD68HjXYk9MP6qxaDg7CCu53ulEdfKDgrrw2eYlqjE0X3KR-ReL_ed_akveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انتقام قهرمانی آسیایی از ژاپن گرفته شد! تیم ملی والیبال ایران امروز بابرتری سه بر یک مقابل تیم ملی ژاپن قهرمان بازی‌های آسیا شد و نوزدهمین مدال طلای کاروان ایران روبدست آوردند. البته گفتی است ژاپن با تیم دوم خود به این مسابقات اومده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30911" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30910">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=nUuCJU9V7uohbenwcy0JiQ-FdpNswUIiMJPgrzLB07kOXOPOHMqKX7iD3uvwiz5qojISuNd3zSJwPw25vKGIAWN8MJP4kvrpb_XbuPc7ALa7EabIktTOJ5YVeDz_taQMiuXzP-nNfU75SWiBQZt2DEHvif64uQiyWf4nvV3ZrJOpTTPeXs2JGz5c16MT9AzPLOE4R88EdLn1u-xoDU3vQf55IXm2uALwWU4FsXx49uNJ3KcYj257GG2oUrDTy4xXwfshSaWHk_VzDmrPMhUSrmxL0ylqBBqSsyN6ZxxvA0N4pGpekrhCMY-OA1fVjhP3__OZebqXRsKOaKKuvRx9d1cs6j3e_hRg9sEFGhOeU12CoRhtSS5MJ2MfaHDbLmQx0c3nj8QD-twpZkzEqFgEUH7PU13JAHh0UmS8yp_QQRcosDTzoLQ4VklffJUHfTktRejsb8TV8O01YT473cdaCW1Z76bflAvi6xHmejna90BnJWzz2zi5NMKWLfPwcWAFpG04AbyB-Som_RI0ypJmrTCV9hPyizP03HWO3JdrFQMSRWaSpfqTdoBviEd4LbdV5PKhaEk94-jU3S8kHhpvb-zfE93d1bYO7HmvLpakOEGNKxF7gLPO-gC5XfD6iaCpzlVGrMoLUux6FMAUpmmwdI0mHsn3-cT5RO2Dwr_4pus" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=nUuCJU9V7uohbenwcy0JiQ-FdpNswUIiMJPgrzLB07kOXOPOHMqKX7iD3uvwiz5qojISuNd3zSJwPw25vKGIAWN8MJP4kvrpb_XbuPc7ALa7EabIktTOJ5YVeDz_taQMiuXzP-nNfU75SWiBQZt2DEHvif64uQiyWf4nvV3ZrJOpTTPeXs2JGz5c16MT9AzPLOE4R88EdLn1u-xoDU3vQf55IXm2uALwWU4FsXx49uNJ3KcYj257GG2oUrDTy4xXwfshSaWHk_VzDmrPMhUSrmxL0ylqBBqSsyN6ZxxvA0N4pGpekrhCMY-OA1fVjhP3__OZebqXRsKOaKKuvRx9d1cs6j3e_hRg9sEFGhOeU12CoRhtSS5MJ2MfaHDbLmQx0c3nj8QD-twpZkzEqFgEUH7PU13JAHh0UmS8yp_QQRcosDTzoLQ4VklffJUHfTktRejsb8TV8O01YT473cdaCW1Z76bflAvi6xHmejna90BnJWzz2zi5NMKWLfPwcWAFpG04AbyB-Som_RI0ypJmrTCV9hPyizP03HWO3JdrFQMSRWaSpfqTdoBviEd4LbdV5PKhaEk94-jU3S8kHhpvb-zfE93d1bYO7HmvLpakOEGNKxF7gLPO-gC5XfD6iaCpzlVGrMoLUux6FMAUpmmwdI0mHsn3-cT5RO2Dwr_4pus" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ امیر قلعه نویی به فدراسیون فوتبال تاکیدکرده که افشین‌قطبی بعنوان سرمربی تیم امید انتخاب بشه. درحالیکه جایگاه خودِقلعه‌نویی محکم نیست و ممکنه هر لحظه کودتا علیه او آغاز شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30910" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30909">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=qQRrAPkaYG6TsiDwgE5SVNsyByxYzciwoX34RCMdvpciFy9rx5BB0eiKkWav8dXtGlIOnkrju-j_GqVw2ORJaaDasVay5sGfX48MFIE7h5nw9ZcoJUPAsPAZjGeVE-05uDtEMCPulqOJ_sAogeueBAkCGFfQsXvsofcEb8cgsgGvAtwxaN_9sg2njcYR2fExYZba6cypSzjeuyPxfkOJpwWTVVpX7qi0FYNEHZ274NQ15jNfQ9OqpKd3V11a3_-ihEaAThR6W9-IR2FUkcasO-EzLQcG5DmQi1H3dPSvp7XHu1GfrGG4ofREZXi0MyTQZBf55YVrCeDG2qz3Y5g-Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=qQRrAPkaYG6TsiDwgE5SVNsyByxYzciwoX34RCMdvpciFy9rx5BB0eiKkWav8dXtGlIOnkrju-j_GqVw2ORJaaDasVay5sGfX48MFIE7h5nw9ZcoJUPAsPAZjGeVE-05uDtEMCPulqOJ_sAogeueBAkCGFfQsXvsofcEb8cgsgGvAtwxaN_9sg2njcYR2fExYZba6cypSzjeuyPxfkOJpwWTVVpX7qi0FYNEHZ274NQ15jNfQ9OqpKd3V11a3_-ihEaAThR6W9-IR2FUkcasO-EzLQcG5DmQi1H3dPSvp7XHu1GfrGG4ofREZXi0MyTQZBf55YVrCeDG2qz3Y5g-Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30909" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30908">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTyQzHx2kyQB-bxaR_N1bH6GzHp0YgzpjlOnFwB29_GJZaBNT_0TUMNAb0fvJY69LABTWP46xcEXBNfF6ckoscfkFslXOR0BX__4cdlkSS-IJyveM225GloGctbV_jEwkQ2elPZVSMv-qvu6GDRNYqSC9xGRlGqo3_hps8vLN7ihpZ-9KzxN0IBvfaUh63Knde-tc5Wso679MwiLyPrFzPeqlrjjRGiZhbvI_3BxPwc81TFLw87ogVZjVlvb828PnH-x7rpattejgRqP8HCDMfcqbV66SRNdCc_DwpR0p0I7BAx5uBd3xgMAbquHisUhDhu5lUI1jjY07xVeknIEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30908" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30907">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiH1D9XrdO2DevtRE3MQzVMGbhTMhQZdKmxxad8nKjoPgjZd-xEbJc5T15eA3nPRNi-s6BGuxib8_Gf8a0T22VNM3UvJtlDWAKUTAkQwgxogy8avaZtl12cumAPUNa9B3VJUSzF2TZCPbXOmihH94cNpujm1U5yivMos8ZPDQRg-msFWKitQWQa1HQJCo3hYh4tnIDxl0lU2kCUdVqbPw_fGyE3HAcd4s70KXIrfzpifvkckoRAzmmNCn2ajEWMu_XIhVNgEH00XzyuA0-6_7uCE8UA2m4btKjhGTXqsgrOm_V6jJArZlSlhSn4N29dSr7vC8LcvjCOoWJTlT-uVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30907" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30906">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSJg_-PGGWlICJn6vdUqxn5VgfZ3l2TPGpKU7AS0ln03LzBj2UNox3rBldbBG-NjPPFEA6dVauUZuY_GVkk1cjf1anWKN0Fs-CKz8iXga-Y7W9PiqY8lJ1JczzClLCFrt-77oAqb08DZOY8eOzFqYrm3naAUuqfAsiLPYDT5VjMkQdhyYiQYbvZPVIsUe4nM5LZ_blbjOLjaDyi3TdY6A3EeXQD_WKOOE8mtKfUfbBronO1u4ie4Rr4jH7NurccenFDao2WzXOLCVoUi2dU6iR_UK87C9gmZoxfJulZ-X5zyynj-2xUwZXwG0gvTnoay06aca9DidrK2qr2Sg6UNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ 10 گلزن برتر تاریخ مسابقات ملی؛ کریس‌رونالدو و لئومسی اول و دوم، علی‌آقا سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30906" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30905">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=I8jVdhsxcT9q2tufgXvw66QMUUDk4YbTTJ1QcC4TUns_rCUK5uFKNhLqSisW9K-els8WSU51xeU26rcD1dUc9T5T49Qm5Lg1skfzN004DbFAzODnRc_EzQgLrtH6eFU9AZDfWPyNI78rlx49AQ3Z6KyuZNXtQ_g6hv7O0bJxqwbsReKzEkky13a_8iFDzlkbUfbaQ50ePFFz2_b2i8zOTmb8dEbIw6jz5tCvv4G-bRiDT_yykJ1SJYy3cVeiwqmj-SlYy3iucJE1-Q3zMOgruFF_FmemKDnOH1788Rsa9rB1Y5mIigQVXLqwFuasRB-sOcZAnc8Kxddum9qa8wbUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=I8jVdhsxcT9q2tufgXvw66QMUUDk4YbTTJ1QcC4TUns_rCUK5uFKNhLqSisW9K-els8WSU51xeU26rcD1dUc9T5T49Qm5Lg1skfzN004DbFAzODnRc_EzQgLrtH6eFU9AZDfWPyNI78rlx49AQ3Z6KyuZNXtQ_g6hv7O0bJxqwbsReKzEkky13a_8iFDzlkbUfbaQ50ePFFz2_b2i8zOTmb8dEbIw6jz5tCvv4G-bRiDT_yykJ1SJYy3cVeiwqmj-SlYy3iucJE1-Q3zMOgruFF_FmemKDnOH1788Rsa9rB1Y5mIigQVXLqwFuasRB-sOcZAnc8Kxddum9qa8wbUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح بعد از پیروزی مهم آذر پیرا مقابل یوشیدا از ژاپن‌هادی‌عامل‌حواسش‌نبود میکروفونش بازه و گفت: ببین یوشیدا با همین خستگیش حسن یزدانی رو چیکار بکنه تو جهانی اگه بخوره بهش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30905" target="_blank">📅 14:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30903">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTj2I7MQg4eEVZORJdmoLXLSirHz09PF0DFYDxW_6Z2YgkCQYKDCNBw9R08G32Pqlt6S2mm6cHiRntgT5vFr0fTZcvj8a2DjU0aKB99No9ue9_c1de0IhdcjyG23cLVNqP8lt_AFrrX5AD8ClCBWXFwVio8GQ6ytKr6HuZz3roFXtB60Di2yCtD_u-P1OcBfzh3hnk4i8Bz8J4vae_JsrXbuIgVQxA35_e26Tb-pFzd70OFXRqmHMOiFmIxs1rF8PbJNSkYI5B77HtFvzz4_hhgkEGSKoU12wcfoTxE-nuiN5RCUsTyTzahOOUKoHbzn2LrdJdFIT6tnO8mV_S6S8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌‌های خارجی معتبر پنج گلزن تاریخ رقابت‌ های ملی رو اعلام کرده‌اند که علی آقا دایی اسطوره فوتبال ایران در رتبه‌سوم این لیست قرار داره و تنها کریس رونالدو و لئو مسی بالاتر از او قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30903" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30902">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjM3-qTZmLPvmzQHbh5bDOqsybc-crhILcPwD9lVhb1zyD-5qNoJG0Y5DZwAEjBxRKbxydNS9zr-mNb6Zxf92RsWXOTLUQuyJciqL5foHAtNPH1Kuquo-mIzov1QnsV8NLK6pVDLiBcXLw79UNNyVAGFzlUonSIHqRG0OVWKnAhi0uPq4ZGkdU4zCM_QXzVtYhD0eZXeaPdXWDkBy0ZouNSqOy9WebzO2ce-LNW8nDGQQrgaQscLjLD__ocb3qW-eccytcBshOYitQB094d7qDPgok76kO--yWZvyP1K3NWOHpFZtiOQdvSFkw-KtS7eD8Oqe9Ih2HDle56nJp2hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلای آرین پایان تکواندو ایران در ناگویا؛ سلیمی در فینال وزن 80+ کیلوگرم تکواندو بازی‌‌های آسیایی ناگویا طی‌دو راندمقابل‌مارات ماولونوف از ازبکستان به پیروزی رسید و مدال طلا را بر گردن آویخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30902" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30901">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCDjUOo_EKh-YUigpRkbMyMNK7VYzQsKeLBQQZpnQheyFd905VK2IZ6KqOG1LA-UuV-Lhx8UeViX-f79TnPTLBWgRO17khY0bku4YaKz_B5EeVWfz_NbNLuU35oTkuyUBHOYHXBTgMl5zr5MqYxdklhXxsarv_LQV6JeRzwHtAGHOp1k-8frrOTyOUGaxIgeOh_Rm0mmQ0xA-u00dpTuUajlhRU46ZUwYV69NQVAd1XU4eSQ05DtsiLsUcPy18iX3-ZyEJF4ZceYKOpAg0vU5xp4lp5fT8-mwQA7jCr6ICKOcM8xZ91JfLJ0n0lO5Rksvr0tOr1dqMtiJJX1rDyALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال سرمربیگری تیم ملی امید رو به افشین قطبی سرمربی سابق پرسپولیس و فولاد خوزستان پیشنهاد داده و درصورت موافقت قطبی ایشان بعدِ سال‌ها دوباره به ایران باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30901" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30900">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSOB0eb6A5mzqFmyb0MIfJ7XhlRBrha8_H5ZZbkqIa22NE7pC60RDPOCoTKHm3sAMqfXcxNtJjMHKBehuPu1QG_JWkvxJ50lKK4J4x4DP5UXfRC2qWkHlov7EfbNeQw46ycCQTDZdVrtHGsRQ9dA2GJHIuE0iT1fRPQwm_zmTvKYKeG4ca-N9iAzd6IEhMoNpWLxNTiYM6lgHlxdvj7FtDRGwyPSUYiK2U56T6zpRf_AiLSM6V_eJPABNj0C5ZDkEOuVRwymWOI-upyt27lCXotjFgUBNWRmb3DVFjUHPN2nEGhLW6OTP7j1QtYd-SOQIUJ3rEKHg6IM8tVcTIM2Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قیمت‌پلی‌استیشن‌پنج پرو تو دیجیکالا به 345 میلیون تومن ناقابل رسید. خرید یه کنسول بازی هم برای خیلی از جوانان ایرانی آرزو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30900" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30899">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0jH17J4AcyFYln7EUZvUv8qfKNxWNylMWxS6woyHx84zLsMZ2PusAsVGgs7JUctuzR3qtpTNEsXlzHcr2KenFlUi0iKhT8iQRGr3UlwxEOsrJ6IRs1YqgwZdj2Wjpz7KqJdjCxoUikhVfMjddG4K8vSHwIdHCsE6xghW7CrlpJOBLYyGz5dnRslw1QkSg3ClPxOs6ayHeP_Y-RHhKOn8oez14hlDPwE_nowDetsXB0cA5aT03SgfESG0GXuHAWcE7dG4JiMeHDB1Suw3fr5kT--2yqllYEC-PK2HjBCHZ32FJQi1O7xHkOI5h7g-Rwak2GJeKOSaM2YsD0hHo5QiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30899" target="_blank">📅 12:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30897">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
حسین ابرقویی نژاد بازیکن جدید پرسپولیس: باعث‌افتخارم‌است که هم در لیست کارتال بودم و هم هاشمیان. تلاش میکنم بهترین عماکردم را نشان دهد.
🔴
از بچگی پرسپولیسی بودم. مثل آرین سلیمی که همه اهدافش را نوشته بود سال 98 تمام آرزوهایم را نوشتم که آخرینش پوشیدن پیراهن…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30897" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBFS7JoXzzHo9-L4FN-XYH1hQm4ltJpEt_AmMApGcH4lSZBbSefcGTDArnsU98aCwl8Qk6-i3yC6LBs09rb2gsZ95kChAxwMATJTE68zmYuEMZdLjJKrf2KYA7Cuq_FIrp97twZGzjU8pJRqGvjEVxk7WNxu5FosWJGpZWxw4qMOyYiZ58n5R-nHCKBgClsBnIFvoMH9lSrlpdIeNSh4fGZHZvT64y78tc69dInLgASBFZgk0xONoOoeQ489WFJPWVUJADe5KQUQmeVwLoM1WqpoGRHRUIWf3cnsV2ED1GcZfk0deKTO8hSdPq8Pq6GpJPnieWTr9HbjiSdl5hDtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیرعامل باشگاه تراکتورتبریز عصرامروز با علی‌ کریمی برای‌پیوستن به این تیم جلسه خواهد داشت تا درصورت توافق نهایی هافبک سابق سپاهان و استقلال شاگرد نکونام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30896" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=olrpjVxFH38hhR_JDdOa97BJY4dnRQRzyAehUEJKqDYqmT-jtaMoDUq_tptU_we8sIsSkERD_qCzsfGSZc_vY1CugR1bWoLn-SKFXXZXbu1sOIFJFHG3OKZ2dSVwlpKO5q1TnPbdpJOuWy69KCCJVYvQWWfMW5LqSpD2obbl9VQUh_tB7ve_wo4lrc6FVUYASN_ZX36T072wZ-bmOZ3IGUQHbSUi50YS_5vFT5DHouWhN-371r2iy1UNcM2jx6yb-G3o_HzPeZzWH5buMmSMEWib4W0TNUf2bMkWJUX4WL-Bt-ijkW8bDcc0GmejuamXF1l0r3hZmekSj8u-LmEP3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=olrpjVxFH38hhR_JDdOa97BJY4dnRQRzyAehUEJKqDYqmT-jtaMoDUq_tptU_we8sIsSkERD_qCzsfGSZc_vY1CugR1bWoLn-SKFXXZXbu1sOIFJFHG3OKZ2dSVwlpKO5q1TnPbdpJOuWy69KCCJVYvQWWfMW5LqSpD2obbl9VQUh_tB7ve_wo4lrc6FVUYASN_ZX36T072wZ-bmOZ3IGUQHbSUi50YS_5vFT5DHouWhN-371r2iy1UNcM2jx6yb-G3o_HzPeZzWH5buMmSMEWib4W0TNUf2bMkWJUX4WL-Bt-ijkW8bDcc0GmejuamXF1l0r3hZmekSj8u-LmEP3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ درواکنش به‌خروج کریستیانو رونالدو از اردوی تیم‌ملی‌پرتغال از رفتار او انتقاد کرد و گفت: نباید میراثی را که ساخته‌ای با غرورت خراب کنی. اینکه بدون صحبت با هم‌تیمی‌هایت اردوی تیم ملی پرتغال را ترک کنی، بی‌احترامی بزرگ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30895" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA--HQsPDCMhtzAaGlUHTxUpITg3KRTOyAmRv2lMEPam-EgI1AXsxZWhDJjdoFeOqViwa_x3VElqgh3Kt_Gv5AA0Ju1qq5y6lIRqHtG89N0cUlQA-mR39c018sbmvtbcVu1ZqcoHT42fi9Ku8iT4CRZzkuT8qNoH6pFkmifX-J5gCu8XhIov1eHYIhDghVGSqP_e4m5LOkB7XaijbEhpITEQ-EWlIJMHDDlZMcD7A2wFFSokrkYUyzrJ6sIYnUyabLDdGj58OjW70XrrLSMwGN-ti09doIbXLFfgn575OLvogbOAFHFiEbNb_WPa6174gedlsd1ZF7CPSEZco3X5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30894" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upya4vuq1qSx4vl1Cv4DXa_qH5WDi7C7_VhEWI1130fWD2fbVhe7TOmH4hrsCLewyuJ-SAwOM5AKl_ZgdUdzwHWcpSR2NB27FMRh6jqt5NCyF-kLmXEAqgvbdjMRF5wlD3lTp9EzoEjPemYqyjCsetZkTaMHl2K1Hw0uRTnCs6RS_h8Ru3N62jspCNHDMC_OsIZeIutOJhYkHasZLrPzHCeSlLfNcGoVzIngOQsxFcKQ9jfJnFvCD9UNs5J_yYAZ_td0iBPSt_yOwXrdNC47uXipS7S4iNQO8KXF6poeIu3ThoPkHNQNWYrW9wBmvdsSbFcDCjGDElvTZ4M_ZnOX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه
آاس:
رئال مادرید توگزارش شکایت‌اش از بارسا به یوفاگفته بایدتمام جام هاشون از سال 2001 تا 2018 ازشون گرفته بشه. بارسا تواین‌مدت 9 لالیگا برده که تو همشون‌رئال دوم‌شده و اگه این پرونده به نتیجه برسه 9 قهرمانی لیگ به رئال اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30893" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30891">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfXDbKFDcDyCQ5ZTorZ-oqlpCuQF8LCLBlM-oiRQTe9fafC7RQ63bXYDp7buno2OS8_SA4uRrzpOOilZeBweadSKTOPIAnmwHWbJ2U2tbXWYO4pH_jP3jnlSgrGFFHAvAffZs9mXoUIldN24irOvaQOOTUJ69tEk9tw-bXnuCCfi6swm7c9qqBMNwH1SzdNSEaRPUdAFoGinLys2ykPsDe6nndSjGgOi2OXCYMGp86WcKtcQqgoF7SjL7rQkHSguGE_TBzwLiPuZ-Qr7nHNKShD3MWKAsgPxDtbjQcflo7ny9u1A9e_gAqYMz5i4LKC1zmQD6EMtNxdXALI6UvnFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 بازیکن‌ایرانیکه سابقه بیشترین تعداد بازی در تیم ملی ایران رو در کارنامه خود دارند؛ احسان حاج صفی شب گذشته در صدر این رکورد قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30891" target="_blank">📅 10:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30890">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzAIFjcNTBIca4y2WkAVwj-1sCBXDrlnpn6rmhjMT9bDqDxkCS5NAb_39sTxAGdF1rgidrhuuGPYjsQSnB0D00X_dABUW976A9eCDPpxtK3jKI2oP1cnVAU1NlpOl9a-W_poHJDwf2ZgY9C72W2puIaiOR6q2mYOD5kDGtp_Q7B_TQISk6kbq8vurvq34fDyYxlD0GuCa68YXuBvZFtStOZ5QCC1rxe_oCrhJsuvKH-Uw_1hVpzG9GbgwqbtvLqfT14ooGJyTge78clVkTO4ZYEnuPnVY00j44H8AQrMd4OifGohk8y2chKXSGic63Kl72ALSy5FLgNSKwy1sYy-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ترکیب‌منتخب‌فوق‌ستاره‌هایی که تا به امروز با هییچ باشگاهی قرارداد امضا نکرده‌ اند و در مارکت‌بازیکن آزادند. محرز یه مدت با باشگاه الوصل در حال انجام مذاکره بود اما به توافق مالی نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30890" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30889">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Ou64bKeX1kAAjN72OzbmM6pzT9-zwLpJKiE5qvcZ_mu-X2J8mkn3pMBcuNrdKtdQDwPYbmlLtEd4fXAJyWwU7dxI8GZ1yNZk6NY18AyKrJQaEsTynZXdhNuWgnx85LWaKH4nwDxfUV7sdGaPcaSh0H0tdq1HJViqNAdiQP3Dmn37I7z9U3VU02VHo2wSMGui760afI8_mc8ENuuYoi-Fe8mMvVhz3x84tepnV6nnricy-IjlQanL9-P9umMEJJUiOnZ1hqJ1AZX1-xrgy2NWYFUoGhRoYvHyBk5d8UIX4U5xuRp74Li7z9q5s_RxOUh6GZdnxvKu7GHhQZCx8Alw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان که‌چندروزپیش در اردوی تیم ملی جوانان گفته‌بود که من اونقدر حرفه‌ای تمرین کردم که هیچوقت مصدوم نشدم تو بازی با روسیه مصدوم شد و ممکن است که چند هفته‌ای دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30889" target="_blank">📅 09:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30888">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=nDjRbPYlduqBmwUexIagHeHS2i5m9xWOcSig4-LFLgPXPXcdjvhnpsVe0vBy1VM-g_80rcV3zgm8sqb6TkKbTj26_eEyzGsC9mfypU6CpZ6SgjCr3hv7t9-TosuiD58jxf4TsZlnoZGZMXWWXX2Y2KwWWb0Jc-SRs4NLj3ObbTbzKICrkuyK9NYvIGsk3rGnoRSbOHD6ymIBJPJCz2rX7M4s1_ifOxjH6GnnuBg03ojtS4RZT6Onp77lp7oLkIi3WY9pEp_S5QcDim6tsX2ZKAoB-SvKWnCK225GIyOUJsp5o0UzIBYa10riW5eLwEMrWzl8G3EQV2VADWj5C0bAfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=nDjRbPYlduqBmwUexIagHeHS2i5m9xWOcSig4-LFLgPXPXcdjvhnpsVe0vBy1VM-g_80rcV3zgm8sqb6TkKbTj26_eEyzGsC9mfypU6CpZ6SgjCr3hv7t9-TosuiD58jxf4TsZlnoZGZMXWWXX2Y2KwWWb0Jc-SRs4NLj3ObbTbzKICrkuyK9NYvIGsk3rGnoRSbOHD6ymIBJPJCz2rX7M4s1_ifOxjH6GnnuBg03ojtS4RZT6Onp77lp7oLkIi3WY9pEp_S5QcDim6tsX2ZKAoB-SvKWnCK225GIyOUJsp5o0UzIBYa10riW5eLwEMrWzl8G3EQV2VADWj5C0bAfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
صحبت‌های جالب عادل فردوسی پور درباره مدل ماشین اونای‌سیمون دروازه‌بان تیم‌ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30888" target="_blank">📅 09:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30887">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnWXpp95_cFIql_tZYr1wT7Qy_wZfMkk218uZtQZppJuPdPfs9jMU1su1syFN0Nb3JmA3UPV_T2ydvr-Ppg9MzD9AmSWQ5OvG5dP2XsI_MTF-K8iAz7anaX7-d3ax9hFg4knKgW-MJe9GFOQGUL7kakU2OhDTSoWL9L1f1z6AezJJpXQzqIdGunbliIKvk9ysh-KK-iAhOIZqIpJiVwJeULlLwM1hnmWZW2yYLFfPaO6vik7lLCmxoK4pQxu2m5u23iJiojMqOW_vEhFrEbg2Ck8fvHhi_bwbyPbQNWFTyhyI4UUaDR-8aHkzu-udvCjXuUyKVLzprwDY6A2lAVFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30887" target="_blank">📅 08:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30886">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHJ-5k4C7ORbVTpfGLTsqJlzF6mDfHbBHF_hlmVtW52Es2bhmGAbri3RBE8gvelqsWEpOigV3yihtkzq-uVo1B5stIAP2PwZ39XVnXj6-fUfKe3mKzcQnTCbCiizF7FwrVVYcABuPr7hXojLtyLmJy2NCYjhrPU9Go7v6awTJHq1-d1c0gEzwgZsiIAnCkN48UizsaR7le0S_kFbP12FmQ5Dk2fqskKrSA4N2d48K60benPVT4xii6-2LXHzNHeWR0dZXJtEcYweWU2OnidiMpF5-rSiX9RCicutp-nrFJ1g3qgu3zKAnKh96cRnfFYj2Ru-h7YKHvDugapqC8Ilpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🔴
معین توی کنسرت آخرش اجازه ورود پرچم شیر و خورشید رو نداده؛ وقتی تماشاگر شعار دادن وسطش آهنگ خونه، ترانه «بی‌بی گل» رو هم اجرا نکرده.
🔺
این اقدامات زمزمه برگشتنش به ایران رو جدی‌تر کرده و احتمالاً خواننده بعدی که باید تو ایران منتظرش باشیم معین.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/30886" target="_blank">📅 01:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇧🇪
🇧🇪
ویدیویی‌زیبااز دوسوپرگل استثنایی و محشر کوین دیبروینه 35 ساله در مسابقه امشب تیم بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30885" target="_blank">📅 01:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30883">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qle_0Gbks1tRcOwVMbcxd8TfRZ7XY9cFDQSPKjhgXgyHzUDi2P3t_AtYDbB2R9zrhxFTXhyyAVdpsJIN7UAZY1rFRko4-Xg8ID7GlZiNCKx_BCYc4HVU7wX-YySHQzLgwGUpoaLZlj1aY-BbvHm7FdpHHxIyCsaZHzgumkeBJt40r9UcU-hiaIxveBFfh4N2WKWsUI7Fw0gaV-Np82Ijd_DAvwfMWWINHyUUifcFFTQWbnHgZfviDDFvfi3ndqO5COG6oVJ0SQJBzUTws0BIoUQ60O8ylz-HYOX64TynG7T3Cir1w3OeP-8Kyc5BNPb-Qp4JpW4_7iRPGxeicZ1E3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30883" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
