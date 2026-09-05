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
<img src="https://cdn5.telesco.pe/file/QcDJAgCY8Hj73dMOAKhWYEG4ikGZHtW7sI6SI-zwEbnYlLk3-8p-8RK-SEWM5bU4ZjAJfMiWaQmVB6EMHiGwFgL3w6_KjIalXkXvxE0q66tdAWvO4cjZw7cdAUu-y4wcPvtUYcLBiJKfxcmAquJmaYzRzGoxZkgeGr67P-V3lbckc5HmYmsTQt6YB6mJMPj6OXnumkpFfwOfpYOEJRyvbxZf80cU7AeQa6VRvu_LQjrzpVhDRiZNYYjmmctHAeUUxzZA7hEgMD_vXEjsTwopjgjmq9OV8KLv45Pb3X0ptc3w8RrifMNRe1CtE2RG-748uZMdZVdz7OcpydqtjOYLYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 426K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 19:57:32</div>
<hr>

<div class="tg-post" id="msg-105622">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgECjQm_s5crvmw2WJwTITd4cuCv0DzKrXRxihGYbr81zI8Nu5P6V-hrwlzF9cHHA0c7lKAYeey94zBWkpBX6OAMDWyeSeTTZ9TymArD6deCB_7Xj-5VXjPNZQE2YhwBK_CflOfS-D5xtaZgWPTw3yt0ce2xrA_G8NMWNIiIyWBJzmSrNNm50rAMh6eelq5gPNa6dVKaKMcuAfdG4ZMSD7IbZzGFCgnTlb6-qmYQNw1d-2_ce2RUsIRy_f7t-llo59bJzVa3HeKH4smqe6jGEaHeR7eCiUvxVTofmUnNxnJCJTH02tZWxchB71hM9iVGRv1yowPcvjYm-DrH8GxOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پایان بازی؛
🇪🇸
بیلبائو
😆
-
😏
اتلتیکو مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/105622" target="_blank">📅 19:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105621">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKZfJVbEcBtnjtDoWQhlbPv0Gn1KjDXkt1zFZ8aHBixia9fmf1VZYfVHAD4iH0f1DxWTM7Yjbk0DBXBvlSVq0qtIRTRWwPQeAQHTl1kYhqztRi9i1BfCyxT9wJmskz6HDbw8LoED4RDUKDVPwhkeyoLLeBg4h9AVv4EsiOp21MpBkGAb8lqqDX3dUiW9fkAmIQUsCiJakJ_9XKfROcWenU3-ifrnbYUtlwbvPz9VubK8FcpD3XrYJouO3aTiIH5soMTksnAZfkfgxhPk_nM37aRvO9KRoZRDcZBxAWCS5xXa5Bd8u60_2HC15yS2pbLxqa0D9dW97L-9vksgHZADnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/105621" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105620">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/105620" target="_blank">📅 19:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105619">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اعتراضات شدید خداداد عزیزی به داور بازی؛ واقعا بعضی وقتا کسخل میشه الکی کارت میگیره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/105619" target="_blank">📅 19:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105618">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🟥
خبر کوتاه بود و تکراری؛ خداداد عزیزی در بازی امشب تراکتور هم کارت قرمز گرفت و اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/105618" target="_blank">📅 19:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105617">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQsM-d_Q5P0cd0ihPl_Xl-JuEoO8Do-8irmOwnaVLGyl91kMbjfWOFvD8B4fyrDN3wd3upOO7PngEaJTfzPBDayJPJ4dwhwfuLV2iVWdKtqX3Ejw0fh8T_thoWhA8HpZDuyorSw0Q4YR-5E0TPRO0FaLbXP0N_o9QnoaoJ2CtO5tTvlYV4HRiAiImdNL36PeLTv1vtN1AtwM5xekhOXsNNHuAR4dMh8HB-RMS8NBFcydgnTrTvwwNk6cvhNhlWd8xe2ZP9mNqMaq1DPcc2wJV8BB8AWBUGli3s8Bch6RXeJUr9jznHMeFVXl5NgmHNzj7mx1he-HrL4__KW-P7hicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تاتنهام برای سومین هفته متوالی در لیگ برتر، بدون پیروزی و بدون گل باقی ماند!
😵‍💫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 3-0 مقابل برنتفورد.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 2-0 مقابل نیوکاسل.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تساوی 0-0 مقابل ناتینگهام.
💸
باشگاه بیش از 300 میلیون پوند هزینه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/105617" target="_blank">📅 19:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105616">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
‼️
🇮🇷
🎙
صالح‌حردانی: مشکل خاصی میان من و آقا سهراب وجود نداره و‌ بزودی شرایط به روال قبل برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/105616" target="_blank">📅 19:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105615">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/105615" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhvY6r3v6B-OcfC3h3YfJvFSiK8yet22CYBABCpG5jwbysBf8XZ6oGglCrmypRihQY6PjJN3MRmJT1n_FmoPB0bHw6_TlXlGDKZIb9hP8XEHT04hEP903hj14-qfHNQ18ozEF8_P3HRJRnl7TcX3A7ssaJJTYaTExSWy5pcsEIaKjzPIpys_Tc7JW6piJ74h6S7_7RpN8X_51iTEVv3X6MS981XG3BGW8tzL_HMQ8Lkh4dXFSO495XSTEpL9bGPhsihVPnzTmC4P0SMb7rBc2H1uthaGSRXmaXRUnr_4KnBxPIy-drHVw18466bH0AKuT-CtKfLXwlp57Z2u4TjgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/105614" target="_blank">📅 19:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=FxENXGmuD50N_ogIT5ZbqhSMIr83Y7ii6dt-rD1OlWFUr3e6bOxELE2vD0X34K6rAJJUelE2WBF_PJ2hgtSGpFCJiWLnJUj5lwdIt0rUByeix3FLxMUY2BUcF_BhuaKSuTyJkeECyOJ_fuh-A9MuuX1-T8swl35A1wQtBMp3l86xFRU-kC4InvHWV07C_ywkHsGP6O-ZfXQ2k0e6GbRaqRhYCA5yqFZqV-J7F0Lk3OpsInzRUzHbxghm3YslWPw-vR34k96PVTKaEITWFm9gDtMmbe8kbeZDoAdaXpsBkhnP9EEwycPXF44dPDk-D0elg-2HnO9UPMjV2M1MW-05Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=FxENXGmuD50N_ogIT5ZbqhSMIr83Y7ii6dt-rD1OlWFUr3e6bOxELE2vD0X34K6rAJJUelE2WBF_PJ2hgtSGpFCJiWLnJUj5lwdIt0rUByeix3FLxMUY2BUcF_BhuaKSuTyJkeECyOJ_fuh-A9MuuX1-T8swl35A1wQtBMp3l86xFRU-kC4InvHWV07C_ywkHsGP6O-ZfXQ2k0e6GbRaqRhYCA5yqFZqV-J7F0Lk3OpsInzRUzHbxghm3YslWPw-vR34k96PVTKaEITWFm9gDtMmbe8kbeZDoAdaXpsBkhnP9EEwycPXF44dPDk-D0elg-2HnO9UPMjV2M1MW-05Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
عصبانیت فوق‌العاده شدید مهدی‌رحمتی از داوری بازی تیمش مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/105613" target="_blank">📅 19:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im0APaUhlFgjwTWL9l7UjhZ8CfYrHTBEhFZZa1gJF1FuegPz0M_rI9sPnujvl0BiAXery7hFMO-9Q3jVYrktn798bKOo_rfw3NhENK-44_njXgBriKs37Snz_O4SLQD3aWTwc707UpPrudbfNZhVu4rR4nw7hZs3Rcv1rrMvC1kDI2IZuhedFNwiVDymgkbJySCOb_ozcJ5hcCrnfraJbVt5WAvVo6CqA8rqYA1PbneIuK9I3bbKfSvIISCb99g6F0JwSe6MElvMLFivTar7U59UWO_AT9j_J9QKhlWxGtO7oIpQMYhI4n1vF6ZVXksH_q5qR6TgnUjcY5iQ5UZicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌مونیخ مقابل شالکه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/105612" target="_blank">📅 19:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=Y2PoLTojF5T6yx-ec33f-yyis_MU6PK4pD8vmbDwFJVgQoObqlVXgF_ueaSdhuOWVEANsSOwkZQcG4bvjPP6v1NrIuY80HswEtieOeHt713bXVQ07Uwf8GxbwNFuwMdWrMF5GwNwM4PAZVhvG1nozKwjL1l3gVPr9ZtO_zuzU46f0SBG0vGoX2aIOTLKskAuB_miIBFcRCHwLmTSfFgEMhikDp_xii1RuSIlpiMqikQmTlfMbyAf5Eh5ek7ktu3MF2-LJ5aW97_xKxzP2LWNTvqWsH-SXVmlWzGXa41qnchDGxFvwW6o3jr2S0rppPIPQORmu8KKyHdx5S6bbVMk07mUlQOlkicSYYZ1fiQXuxfMxB8X7YBYYMG0WENOEnomkMd7rw4aEI5WHJ2t4W7pfo6kqzgXy0KS4uQGIG5d0iPDnBoOKxTowm3PSd0v4DRyQAFWk3S9JS9wZNTWm2nQDWeoGXwDzgjg1u8NA2_HjRDOroXIL_e_9JxApmEanOLXLCxNaPrNBYrPkh869nXQOKIZIOnM4BzC3FtozHEThiKQFIbdVl32eKBKs1cW-gqoHzugpHJi3EgnhLDg3jcDYx1w2FDndo3rb3KEayaGkVYnkkjxqrDfC7h06n15mvtj-12lVmY089i0W0tNqTd2jqMuo1KJGZpkItxC5qDm1rI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=Y2PoLTojF5T6yx-ec33f-yyis_MU6PK4pD8vmbDwFJVgQoObqlVXgF_ueaSdhuOWVEANsSOwkZQcG4bvjPP6v1NrIuY80HswEtieOeHt713bXVQ07Uwf8GxbwNFuwMdWrMF5GwNwM4PAZVhvG1nozKwjL1l3gVPr9ZtO_zuzU46f0SBG0vGoX2aIOTLKskAuB_miIBFcRCHwLmTSfFgEMhikDp_xii1RuSIlpiMqikQmTlfMbyAf5Eh5ek7ktu3MF2-LJ5aW97_xKxzP2LWNTvqWsH-SXVmlWzGXa41qnchDGxFvwW6o3jr2S0rppPIPQORmu8KKyHdx5S6bbVMk07mUlQOlkicSYYZ1fiQXuxfMxB8X7YBYYMG0WENOEnomkMd7rw4aEI5WHJ2t4W7pfo6kqzgXy0KS4uQGIG5d0iPDnBoOKxTowm3PSd0v4DRyQAFWk3S9JS9wZNTWm2nQDWeoGXwDzgjg1u8NA2_HjRDOroXIL_e_9JxApmEanOLXLCxNaPrNBYrPkh869nXQOKIZIOnM4BzC3FtozHEThiKQFIbdVl32eKBKs1cW-gqoHzugpHJi3EgnhLDg3jcDYx1w2FDndo3rb3KEayaGkVYnkkjxqrDfC7h06n15mvtj-12lVmY089i0W0tNqTd2jqMuo1KJGZpkItxC5qDm1rI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بیلبائو به اتلتیکومادرید توسط ناوارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/105611" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=UQuD5rQedljy2-qJj_imBZPCQhY96T31Pjc_KK7_IB9XnTwvvR73M3aZhfwRuS-fGzGFej5Hyq1BYyd_QZ1DuqIPP6yV3zjjLWA9S_CtSH0I85MUTqInw3fPjX_AME08ZKdUYxyyzOFdMDXTaEKiZEXGHUJ4VggQ7TTeDxe8-ANLMDjNbMakgTiYNlNiZUenHlXIM9wvbfY-9lwu1XI0jIt-N2R1297lnIrEudG8L-t0zxkpFHdon9S8TG4csoU5mQXB2FV593WQT2ctpPV3Is6WDvauN6-K-Dt2dIduM2YXhau9D5i0k2FuNKXBtJFwXCnqRfthvRHFZ-ewP3D7szVljGH_wNgWonv09z9ZIpeLbXPIihYZHF-Ku5adWmWvdIb4ykfKk6bBvjn5OJQnuN4T_3lKsC980CehuR_Bx9oDjBxS6I395bvmIjuLzEKrvwb3lvaF3ohbHhn6h_DExERV2F7XKqXh4yOSrls5L0lBvRrLmOpJiLxczH8Ivfd5OHZwE3fdI1cWPsKTHml8oDME3hu-N2xBhq7PnHxfl1zNysvwHlPqRPD0WI0J6JysbcmuZv5BIJFnQafhzNqpNms7vLatzqTBgPVOY9hVVcjMsPA7slLxkQKmUX4Wkd6KX8aIbz3yoAn6egVNH7KdwMSmoLJCltdR3JfvtcNRBbk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=UQuD5rQedljy2-qJj_imBZPCQhY96T31Pjc_KK7_IB9XnTwvvR73M3aZhfwRuS-fGzGFej5Hyq1BYyd_QZ1DuqIPP6yV3zjjLWA9S_CtSH0I85MUTqInw3fPjX_AME08ZKdUYxyyzOFdMDXTaEKiZEXGHUJ4VggQ7TTeDxe8-ANLMDjNbMakgTiYNlNiZUenHlXIM9wvbfY-9lwu1XI0jIt-N2R1297lnIrEudG8L-t0zxkpFHdon9S8TG4csoU5mQXB2FV593WQT2ctpPV3Is6WDvauN6-K-Dt2dIduM2YXhau9D5i0k2FuNKXBtJFwXCnqRfthvRHFZ-ewP3D7szVljGH_wNgWonv09z9ZIpeLbXPIihYZHF-Ku5adWmWvdIb4ykfKk6bBvjn5OJQnuN4T_3lKsC980CehuR_Bx9oDjBxS6I395bvmIjuLzEKrvwb3lvaF3ohbHhn6h_DExERV2F7XKqXh4yOSrls5L0lBvRrLmOpJiLxczH8Ivfd5OHZwE3fdI1cWPsKTHml8oDME3hu-N2xBhq7PnHxfl1zNysvwHlPqRPD0WI0J6JysbcmuZv5BIJFnQafhzNqpNms7vLatzqTBgPVOY9hVVcjMsPA7slLxkQKmUX4Wkd6KX8aIbz3yoAn6egVNH7KdwMSmoLJCltdR3JfvtcNRBbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بیلبائو به اتلتیکومادرید توسط ویلیامز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/105610" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/105609" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=XxD3yu5H4ieLGPJECP2rZPAASvMovCAFnIrogF-UvInoLQumKEo9VEQwNfVNOJ1uXgSH-i7nmZWaMGn1BMlz-0ug-1Egbv2PKDRP83RDYTR1bAllQO-Dpl125q5GaH8fjqVrSsuhAxpkQenrkP5vJux9rB9JgLY1ehAP7u2vjfgyEGoKQJWC3wHT_R97X9c99qZtEptFuBnjNFWFVJ6c6Z1z6hMJbRSW4tr8vHPvkOGlRwQqNoJeocAYYZx9Jw0u7IOP2bSJbJImGIpchPJB6Orb8vNUo8H6oOM5e2FybK_drkVuPpj2diJ4GjGsMs8GA6tEbbR0MUtgJ0w6riQleg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=XxD3yu5H4ieLGPJECP2rZPAASvMovCAFnIrogF-UvInoLQumKEo9VEQwNfVNOJ1uXgSH-i7nmZWaMGn1BMlz-0ug-1Egbv2PKDRP83RDYTR1bAllQO-Dpl125q5GaH8fjqVrSsuhAxpkQenrkP5vJux9rB9JgLY1ehAP7u2vjfgyEGoKQJWC3wHT_R97X9c99qZtEptFuBnjNFWFVJ6c6Z1z6hMJbRSW4tr8vHPvkOGlRwQqNoJeocAYYZx9Jw0u7IOP2bSJbJImGIpchPJB6Orb8vNUo8H6oOM5e2FybK_drkVuPpj2diJ4GjGsMs8GA6tEbbR0MUtgJ0w6riQleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده
روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/105608" target="_blank">📅 19:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تراکتور زدددددددد</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/105607" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/105606" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/Futball180TV/105605" target="_blank">📅 18:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=e7WTuTvqN2UkWm1ThPIlwZ0Xlm7dDQZlWwoYnatFC5vajrQ0JeZ0QmgZZneqz9XSrt9iE9DdaKrkChioQewJte8lsm08o5T3jT1f2-xh0T9v2BUqRMbXu8-teXbRzz-Yg8DZVyiLF6WZUOv_t27xIwNPZfMnUZi-bUj_Ie0-zw8jgonbu3myG8-yiwD2x1GatATQhZ3G78PJipIacxUYEU8JaZQz-c7xEhjZqBbH-9HnjhibaV8HoPIyvcwa7t8UVoRe7F8oLrS6NsxGpl7bSZ_vW22WjPCIvxcTIkS4oXRevj7J_k-P33MgxPVEvSHPTbqmlW893rEp0qYaEp5vtEFC1K_oSik-LYZKUWZUJ2rOKEJrh1JIHdKhJtSUlHQWeCYBcgvlFz6_wO9iFX1mLHP9hZM1qfgWoYNFNUUJDkbrcv2uHUpkxebk6qrKTjFH62yEBF2NAyCnnf_XuBrT44SRCyRjk-A-k6mQ02wQfN1pJfIB0ykiW6GLuxYPa4KT9KjM5WTH8vZL_i6NCVURjqE0nt82yJqk0G8HNXeRfNk9X4QZ-Up0y_L7N4FfXB0aGFv2VeMJc8kKWOsGf2yARihWqt6YRSY4vc_l47IzDcF0sbBcl6bHHB2ptKhtifRQ5tmID33pzNAg_AdueXF4ZYjVF4uoL77Q0jhJzE04kBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=e7WTuTvqN2UkWm1ThPIlwZ0Xlm7dDQZlWwoYnatFC5vajrQ0JeZ0QmgZZneqz9XSrt9iE9DdaKrkChioQewJte8lsm08o5T3jT1f2-xh0T9v2BUqRMbXu8-teXbRzz-Yg8DZVyiLF6WZUOv_t27xIwNPZfMnUZi-bUj_Ie0-zw8jgonbu3myG8-yiwD2x1GatATQhZ3G78PJipIacxUYEU8JaZQz-c7xEhjZqBbH-9HnjhibaV8HoPIyvcwa7t8UVoRe7F8oLrS6NsxGpl7bSZ_vW22WjPCIvxcTIkS4oXRevj7J_k-P33MgxPVEvSHPTbqmlW893rEp0qYaEp5vtEFC1K_oSik-LYZKUWZUJ2rOKEJrh1JIHdKhJtSUlHQWeCYBcgvlFz6_wO9iFX1mLHP9hZM1qfgWoYNFNUUJDkbrcv2uHUpkxebk6qrKTjFH62yEBF2NAyCnnf_XuBrT44SRCyRjk-A-k6mQ02wQfN1pJfIB0ykiW6GLuxYPa4KT9KjM5WTH8vZL_i6NCVURjqE0nt82yJqk0G8HNXeRfNk9X4QZ-Up0y_L7N4FfXB0aGFv2VeMJc8kKWOsGf2yARihWqt6YRSY4vc_l47IzDcF0sbBcl6bHHB2ptKhtifRQ5tmID33pzNAg_AdueXF4ZYjVF4uoL77Q0jhJzE04kBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
تمجید لوکا مودریچ از کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/Futball180TV/105604" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/105603" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reVHXGgZqr1xM72b7hiZSedSU69VLG9m0rrrxJA6V0E13Oc2rpg9Hz7gmxVBbYSdVk91-GUwa6EAxSG3pFB84rqpKEEERaFxrLC6ok2Ri2n4PwgINq89x9hiGIdx8WK1K2TrA4Z1h1sVOoMqhKpdcJoSxyC7deGJzGOyh5S6uwKg7dsEvIoWfhWHmYHWliCZc7Y8fl_5P4b3k3W9_cTHHeSC-vUsHcgRDPc8WnQyPFl5BT5iK1RZKhFren11dRGvWf9JfV-ioJ-k7fVsT836Hb3gDda1eq6f-OtZotY2bl_hS-N7TRcg0Tm1-nb6QrmDz01AoSyGInhbvz0FBiPkVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/105602" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=fSWFgge7FtXCUs8go_i9TS8LK1UjC-yE6Fcdqt3nEbg7ogZivO7MwijkMiV_6wnDMieVsivsNwjATR8bF_-TxftXX4dzxU4leK8vheU493wPThKi3n_Eay7xK0VdFQtLFbMDgIQ5IUQPbvCyOBUbYOxGjogaMIQnQjGG5wLhI7Xxf3QHoJ4Zd_Tm9cgSt0eIx2UgGXgQUKd4HDaQG0AQvcwqrYUeIffQlviSgH_LSOGMF-yM7I7p95MqxfWXa-z5m2p-SpLnGVJsNGqWvnhDq52VKsVrff0I9_lA5CkWRGwQYQHfQl4rc6NCvafeKogSbI_PX6x5sP58IP1QVeEhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=fSWFgge7FtXCUs8go_i9TS8LK1UjC-yE6Fcdqt3nEbg7ogZivO7MwijkMiV_6wnDMieVsivsNwjATR8bF_-TxftXX4dzxU4leK8vheU493wPThKi3n_Eay7xK0VdFQtLFbMDgIQ5IUQPbvCyOBUbYOxGjogaMIQnQjGG5wLhI7Xxf3QHoJ4Zd_Tm9cgSt0eIx2UgGXgQUKd4HDaQG0AQvcwqrYUeIffQlviSgH_LSOGMF-yM7I7p95MqxfWXa-z5m2p-SpLnGVJsNGqWvnhDq52VKsVrff0I9_lA5CkWRGwQYQHfQl4rc6NCvafeKogSbI_PX6x5sP58IP1QVeEhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
فحاشی هواداران تراکتور به امید عالیشاه در بازی مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/Futball180TV/105601" target="_blank">📅 18:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKC_1eXeDRiK5DYCI1dJ-_hqXhUbIuauByZpdfRBhi8t0GGMic2vF5kHoe8qcJFGmYep2YxKYJ3DWRXtMmTSnFX5m2oVU2Wc7OrCUDxU5a7cx8hPTIkq3uoVxJsYNe2-k7a0-oPHMFUqrf8Zl_plIYczn2kIGG924M3Nfp8yR5UoBMFJpT34u1UWwEHZz6vBMYzgh7ne0CAILbJgGlfawvvGSHb9sTX1WtzKvOZ5EPRDVz_pjFfJaTG2fZsrJ3vfJWgjNunp9kPgC1itS7ndovEZSl_mKVBzFAwET5v2R41EohpTwKEYMiH0q0yZ6ReHPwW_25tznuWF7otzV3JHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🤯
🔵
هالند مقابل تمام تیم‌هایی که در لیگ انگلیس با آن‌ها بازی کرده، گلزنی کرده است، به جز یک تیم، یعنی ساندرلند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/105600" target="_blank">📅 18:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRBijhBxhXgZbmyPiGEI0jEX_Sdsmfn3uwpyN1nu6Hd-XBQkQRdfmIYXwZIjR3eUhRsp3XQwdfeHo_VvztetDhibvoHhRHxxlxNV-1S7QN51Agp0KcvlzNNPkLingS6TKpnbZSUcskSqPjP8GI4oZqDhCvgF0sg4wrsTCI5pK1_wqiJF35VAqmEX4cut6QK_iB36d4oDdba0DJAmSKuT86yVr41f6guO4c1uZtaA689TU2ifjXpC0UJyFwU9aqUEKfPcSUgllmZbMjimLISqdOSKhBcyPptt_Xi1sXbGegdJ5pIcBJBwdq7WDtjukEWmsgWDZzJHDLmWhienlaFcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اصلی اینتر مقابل ناپولی؛ ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/105599" target="_blank">📅 18:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpNpMMVTBmP_t46Wymfv4LDf2LIupGNt0xD6uBjG0DY3B9bZvYyi7kqTYsPl8PY-PmudV0z_a4vFZquHt9oQbhd-nHGtsYJ_y9pTLjtLAQzqg64qfbG2bEmc3h5dVMBXCps8nNWeCuB5Sr-VIfWDAVFSvjXEUVnDLbXYfn81V7Lu2X0JgoYAJj7AC8Q4RQhzr9SrADrtmnT5Y4s3fhWXdPigyh0arTvRfuTHPTRSpbtOgWJLemlufhyzUpld_ZjIGQ21a_Y2XxlPs4i5odlCM-bSWu7WsZgSr4LAM20Rr1TDnvlN6Q5xlz64XLwhFnFpMJiPpnUJ9_EkhFiOyGCahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خولیان آلوارز امروز هم نیمکت‌نشین اتلتیکو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/105598" target="_blank">📅 18:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105597">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=c2oJtHqT01n3IbEGeUQz7ghgxmhCvgTjL1vBCNLXylmOs7_jBBAlETI10AwWY766Pu2fXSakIvaveiOnJuARnqw5SCKkhPQZrkAwsLEVfv98zhiyhULUaT--dOl_90AMT-HxtmZHuuDlaBLn06lxBhBj7yTIqroTwgJrRx-uYsDzkRsGclO7ak8QQIe_DeBPmnH9QUAq9o5JXFCYwbnscihmeV2pebvSwqCHwftl3mBAohNsY3-q0T9d9JxCiN0oUzD6kgFg1ZfsELFVN3twKtfRL6aCBYTDVWa_Gp6YPQSYORgHuCl3vh_PAFjeu0AW_jZeyDzbjlsFT_iRQncPsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=c2oJtHqT01n3IbEGeUQz7ghgxmhCvgTjL1vBCNLXylmOs7_jBBAlETI10AwWY766Pu2fXSakIvaveiOnJuARnqw5SCKkhPQZrkAwsLEVfv98zhiyhULUaT--dOl_90AMT-HxtmZHuuDlaBLn06lxBhBj7yTIqroTwgJrRx-uYsDzkRsGclO7ak8QQIe_DeBPmnH9QUAq9o5JXFCYwbnscihmeV2pebvSwqCHwftl3mBAohNsY3-q0T9d9JxCiN0oUzD6kgFg1ZfsELFVN3twKtfRL6aCBYTDVWa_Gp6YPQSYORgHuCl3vh_PAFjeu0AW_jZeyDzbjlsFT_iRQncPsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/Futball180TV/105597" target="_blank">📅 18:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
🎙
🇮🇷
حمله رسول‌خطیبی به هواداران شیرازی: لابد پارسال فجرسپاسی قهرمان شده و من بی‌خبرم‌. یا من فوتبال نمی‌فهمم یا این چند نفر هوادار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105596" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇺🇸
سنتکام این ویدیو رو‌ منتشر کرد و گفت امروز سه نفتکش ایرانی رو با موشک‌‌ هدف قرار دادیم
نفتکش "دانی" را در نزدیکی جزیره خارک و نفتکش "استارک 1" را در نزدیکی جاسک به طور دائم از کار انداخت و نفتکش "کایلو" را در خلیج عمان به طور کامل نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105595" target="_blank">📅 17:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇨🇳
🏀
ژانگ زییو، ستاره‌ی 19 ساله و قدبلند (2.23 متر) از چین
🥶
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/105594" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105593" target="_blank">📅 17:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105592">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixv-GINYk7AgClNeAnf2rZCJ4BB6uXqf4wkPFNQkiqH4J-DJ6iBYS-BD2cbeZEBC7OQV_wiNvql6U6mImW-bOrCxqc51T76a6aHbiABn_an-Smg4wFSEwFi80vcqevM52h-K6x_c01G5CtOkQ7ou1tnYMQOhdKiTJXOoROZMZk048TSAZYp1bOjnVSx-1oH3zHDB4PeuzCRFJuqcWT2tLPIL3oA-qhPaVHjTMDJNkNmky5guNccJwlY-dVdKc9cmmS3lZeI-qK4zvgz37e5dY8XPpSJvBEH7KvmCWRKOHGpSeCIThywy5i6fFSi9fcfAElqBiqcEVD-G11gi02AGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
لیگ برتر ایران؛ ترکیب تراکتور مقابل گل‌گهر
تراکتور- گل‌گهر (١٨:١۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105592" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105591">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=HidpGq7GtQArNxzFeYzE0h88tTw1Cqw2JiS6PAso7yqhHCcUs6hz_v608YIVEpRUCBIegQLpL6B673kig2YkP3_Z0TKP1CV-jHLlwrEvydsEKISCcRqIXzo-ZgwybNkffaIfFrEJwqgQr_bHjmDYaEhP3i78q-FqVPnXJcZkGM1_tB_oYvDlZOlinTiHBLpWBH4c-nt1fa-XC-nb24fAQdDoqY9--igXQEpq6Vp4Yq_dSSEMOs0Rqu7QmFSKhg0ysU-XRlYUcSioaPaw2I_w0FxJYC9OLqsvERfJ5hE1XtFcyzcB654pWoeJmBAURo2gi60tuR7NBlABAFdP8q9cIjDHJpVgrHEVuSBHE8tG0sQfyX9G14GurfDb79e7uBz3BH4deXHm6XgO_ajbYCVC3gh6Xa6K6-uRHIUGBTPftT5S7gl7UYuMpovOBlKwrJ6bWqR73BJr1YCCuEhTRqyYAPzVe1oFoyMg-rKPhrw0jAt7sTELk-0jFbbx4ikpfsHS5332W1spSANJkCzEWxqwiHf8_or8zOb77-Gg169ke-xAKFO-OOKcSsv-IiX75AZ0ZFmH3AHXQZ41Jk0nX1bB2WMIbnjPdNdaj2-yW5MRn4a0GwoXFzIH2sCaDLIgqaF0hDt9MSn2HJecOKogbFdCnTSi81nRNpZcxyyMV0nW_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=HidpGq7GtQArNxzFeYzE0h88tTw1Cqw2JiS6PAso7yqhHCcUs6hz_v608YIVEpRUCBIegQLpL6B673kig2YkP3_Z0TKP1CV-jHLlwrEvydsEKISCcRqIXzo-ZgwybNkffaIfFrEJwqgQr_bHjmDYaEhP3i78q-FqVPnXJcZkGM1_tB_oYvDlZOlinTiHBLpWBH4c-nt1fa-XC-nb24fAQdDoqY9--igXQEpq6Vp4Yq_dSSEMOs0Rqu7QmFSKhg0ysU-XRlYUcSioaPaw2I_w0FxJYC9OLqsvERfJ5hE1XtFcyzcB654pWoeJmBAURo2gi60tuR7NBlABAFdP8q9cIjDHJpVgrHEVuSBHE8tG0sQfyX9G14GurfDb79e7uBz3BH4deXHm6XgO_ajbYCVC3gh6Xa6K6-uRHIUGBTPftT5S7gl7UYuMpovOBlKwrJ6bWqR73BJr1YCCuEhTRqyYAPzVe1oFoyMg-rKPhrw0jAt7sTELk-0jFbbx4ikpfsHS5332W1spSANJkCzEWxqwiHf8_or8zOb77-Gg169ke-xAKFO-OOKcSsv-IiX75AZ0ZFmH3AHXQZ41Jk0nX1bB2WMIbnjPdNdaj2-yW5MRn4a0GwoXFzIH2sCaDLIgqaF0hDt9MSn2HJecOKogbFdCnTSi81nRNpZcxyyMV0nW_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
لحظاتی از مسابقه طناب‌کشی تیم ایران در بازی‌های جهانی عشایری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105591" target="_blank">📅 16:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105590">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fca94904.mp4?token=KNORPgSzYphI-BAk7rX7vQ-Y1sLHO90S7NYUkL986WEpIjfYHD79rvSb6XEnS5g1Z2VxERDASB_5eS8Js1fiqh26xnV_n5Yyj0BvKQlZdm3ur0LQOjy2Bwv55gmERLk8co7C7jg6pkuN8yQ23Iqh8J9DrANxBTFPuXvJ95t9zbQ092u4-xzFjF2W0gAEyF9IuoTAsYf_RJGowHuKd2RSrv7GGBOz_Dgo23kH2mOWPYqCemrFTrvB-hnxvAhQFsfLdv9p5xgJeSoz4am8wptkCS8_0libwOWPx6I--ZSMK4HjG5a3HANLKoCqYxN8XrJlYgZqxkUBreiO1QxhJo0fGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fca94904.mp4?token=KNORPgSzYphI-BAk7rX7vQ-Y1sLHO90S7NYUkL986WEpIjfYHD79rvSb6XEnS5g1Z2VxERDASB_5eS8Js1fiqh26xnV_n5Yyj0BvKQlZdm3ur0LQOjy2Bwv55gmERLk8co7C7jg6pkuN8yQ23Iqh8J9DrANxBTFPuXvJ95t9zbQ092u4-xzFjF2W0gAEyF9IuoTAsYf_RJGowHuKd2RSrv7GGBOz_Dgo23kH2mOWPYqCemrFTrvB-hnxvAhQFsfLdv9p5xgJeSoz4am8wptkCS8_0libwOWPx6I--ZSMK4HjG5a3HANLKoCqYxN8XrJlYgZqxkUBreiO1QxhJo0fGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
هوادارای بارسا جلو کمپ تمرینی این تیم منتظر حضور رافینیا بودن. حالا رافینیایی که جلوشون دراومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105590" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105589">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAOYJACzVXaPEDfm6cUJkG0nAZNvKKMsVf6u5UVJGJk8quZnxhH_GRDoS2NtWVoNclTAr6ER44Sihbqt3V96CPfmqJ5Qd79y_Csy1U_tJ63isEY8OkLs9h4yHuP8UImbSbix1PMbNj_7X7Q_qx4XW0CEbe6vaqvKqL4mawX79s4QeBet0_DSrOoWgdgQ1NN5tf7nRUA7umEIVktoniEnJ9t7YO0HHysbsinY9qYxcjWrL9oDSBjrFDdm7QTxQQQRirLqZA34A_jgcel0-POCJ5s2K2pFgvp1Om9UBAt-b8Hb_oA_1vIJ3t_yAmYF9f0_Pb-Uts2-4fXYGJGijF25nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس برنده شدن باهاته!
🎁
تا ۲۰ شهریور
با خرید هر بیمه‌ای از اسنپ‌بیمه در
قرعه‌کشی موتور یاماها، آیفون 17 و PS5
شرکت می‌کنی
🤩
چرا با اسنپ‌بیمه بیمه بگیرم؟
✅
با پرداخت قسطی هم می‌تونی تخفیف بگیری
✅
برای هر سوال یا مشکلی، پشتیبانی ۲۴ساعته داری
✅
و در قرعه‌کشی
موتور یاماها، iphone 17 و PS5
شرکت می‌کنی
این فرصت رو از دست نده؛ چون با اسنپ‌بیمه شانس باهاته
💙
وارد لینک زیر شو و جایزه ببر:
👇
👇
👇
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105589" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105588">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
‼️
🎙
مُچ گیری عادل فردوسی‌پور از محمود فکری: کُل دنیا دیدند دارم به صورتم گِل می‌مالم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105588" target="_blank">📅 16:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105587">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29285b8410.mp4?token=t2fJAd4e5G8LjCe0NkTXiX5e96dxMTi4SS32ZfIITQ6Ao6GfYHINVT5lMpfYHzJW4ro3uOYXKEl-8bK2JqGRfcyDpxcXXjJ6Hc1g_joAcoM5laeoFh7P4o8Hax0pvyZ9NCF-bgMkOpjpPxlj31lR9wEq0dQPQX7eknO98r_mGq25r9D0RrVPMakxMrvGxwEmTE1mZVMMhKo0Bxt04GQsWcPHv10xyjIXGkPfK-i4ntMpOx219q33Qk2YmZjDgyLBwv_el6xv_-7Q0hi8CqNOK6y_w1kywp02DcS1kBrqynd7kh49WAv3XR3p3F-YSSnTkjoZh2n3JNWwZ_Pfewh8gSLtlzgRF-TaBf3ouH5MiHO7Tf7a8lQRv3cVztMpU9qGIjcaYtwYsBbj3U6WqPDNsFbgrih3dwcn2P0g3zlA81jGZ720YaXoAMZ8ayx4SbASo0G6bU_gwoGxR2-C1CLmjwD29UlbSmTI1bCQVETWHmaiRy_fyTAq0i5aERkjo65HNf3C0I2s5n6bXw95EpFOQPJIQBum3rN8MMi2YARczUreBy6WL1gab8OBSU_ODyXwmvc5j68tI0LDIru_urR5eqGmz6acLLHj073PTJteM_5ELts_Lk0idiH9T5Zn6JQpoR5rdsOj1W3iiG_axgjkPwifSg2mRqx6xba_4jEGdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29285b8410.mp4?token=t2fJAd4e5G8LjCe0NkTXiX5e96dxMTi4SS32ZfIITQ6Ao6GfYHINVT5lMpfYHzJW4ro3uOYXKEl-8bK2JqGRfcyDpxcXXjJ6Hc1g_joAcoM5laeoFh7P4o8Hax0pvyZ9NCF-bgMkOpjpPxlj31lR9wEq0dQPQX7eknO98r_mGq25r9D0RrVPMakxMrvGxwEmTE1mZVMMhKo0Bxt04GQsWcPHv10xyjIXGkPfK-i4ntMpOx219q33Qk2YmZjDgyLBwv_el6xv_-7Q0hi8CqNOK6y_w1kywp02DcS1kBrqynd7kh49WAv3XR3p3F-YSSnTkjoZh2n3JNWwZ_Pfewh8gSLtlzgRF-TaBf3ouH5MiHO7Tf7a8lQRv3cVztMpU9qGIjcaYtwYsBbj3U6WqPDNsFbgrih3dwcn2P0g3zlA81jGZ720YaXoAMZ8ayx4SbASo0G6bU_gwoGxR2-C1CLmjwD29UlbSmTI1bCQVETWHmaiRy_fyTAq0i5aERkjo65HNf3C0I2s5n6bXw95EpFOQPJIQBum3rN8MMi2YARczUreBy6WL1gab8OBSU_ODyXwmvc5j68tI0LDIru_urR5eqGmz6acLLHj073PTJteM_5ELts_Lk0idiH9T5Zn6JQpoR5rdsOj1W3iiG_axgjkPwifSg2mRqx6xba_4jEGdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطرات شنیدنی ستاره سابق آبی‌ها از دربی شش هیچ؛ قراب: همایون بهزادی زبیاترین گلهای تاریخ را به تاج زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105587" target="_blank">📅 15:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105586">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=QFPTCUM7DDVKAwVB9y_Ipg4C6pdLbslHcRxlbDrt3QgeJCb24sKReUAzNWcQy-1ExiNblFXnoiUjdJXW5jUsDuo4obcLz68g8-XzsbEiN1b8w_k3F2IFx39otR2EdyKvVXv1hGPfkW0xnJjWu8cw7jTYdNlnteZPoGOa-nqVjxQbBW1Ju8qRc37jt5Vgj2wthZBC5jK4LsT_wEm5RLeUpwaSJVVYPAY65TJyrNwg1_69UC9vxBQkMmqbLOLD79YSU9PosWF1H6XBzCm56JWWhUnx5NeH_KzNfK7w-dzvxUP765N_1z6vmws2FeeODZ7HPqXg9IvavcI5CIP6AfNiRDv4YXN48O3ESf_IqgIlGPiwGEiGp84bUJUmz9FJ6XXqxmzHgosBR3lnk-vyT2zxb3IP0fHtB3jG86vvhfx5snmSrFsib9KbWk-jtHe35Z-8oyDgqETi-L4CPVK4vLVuBI4uQbFW7zRAvOnBvkXfjA07Mkbz0ZBDP6jMSpVcr5mp5y4ovAs5Iaae2o9fsJZo6X23Yvu-J4EudZ435pmSnNfM90wroBqZQnT8yx8If75qn9HcD8L3PcaRgWH35Dk7jmcbs90sKhAk7S7INX8XbDbOmuRXPhMD3gqo9Bmcwvsgx2P4zEYAN0qBgH61vptm2yffVcmqVzDcNdacLMa-Woo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=QFPTCUM7DDVKAwVB9y_Ipg4C6pdLbslHcRxlbDrt3QgeJCb24sKReUAzNWcQy-1ExiNblFXnoiUjdJXW5jUsDuo4obcLz68g8-XzsbEiN1b8w_k3F2IFx39otR2EdyKvVXv1hGPfkW0xnJjWu8cw7jTYdNlnteZPoGOa-nqVjxQbBW1Ju8qRc37jt5Vgj2wthZBC5jK4LsT_wEm5RLeUpwaSJVVYPAY65TJyrNwg1_69UC9vxBQkMmqbLOLD79YSU9PosWF1H6XBzCm56JWWhUnx5NeH_KzNfK7w-dzvxUP765N_1z6vmws2FeeODZ7HPqXg9IvavcI5CIP6AfNiRDv4YXN48O3ESf_IqgIlGPiwGEiGp84bUJUmz9FJ6XXqxmzHgosBR3lnk-vyT2zxb3IP0fHtB3jG86vvhfx5snmSrFsib9KbWk-jtHe35Z-8oyDgqETi-L4CPVK4vLVuBI4uQbFW7zRAvOnBvkXfjA07Mkbz0ZBDP6jMSpVcr5mp5y4ovAs5Iaae2o9fsJZo6X23Yvu-J4EudZ435pmSnNfM90wroBqZQnT8yx8If75qn9HcD8L3PcaRgWH35Dk7jmcbs90sKhAk7S7INX8XbDbOmuRXPhMD3gqo9Bmcwvsgx2P4zEYAN0qBgH61vptm2yffVcmqVzDcNdacLMa-Woo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پریمیرلیگ هنوز شروع نشده، جنجال‌های داوریش شروع شده!
⁣
🎙
📹
مایک دین، داور بازنشسته پریمیرلیگ، توی مصاحبه با پادکست جیمی واردی اعتراف کرده که زمان داوریش بعضی وقت‌ها برای خودش چالش می‌ذاشته؛ مثلاً ببینه چقدر می‌تونه بدون سوت زدن بازی رو ادامه بده یا چقدر می‌تونه توی دایره وسط زمین بمونه و ازش خارج نشه!⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105586" target="_blank">📅 15:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105585">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rFRSmgIquJ7Sd0W9eaL2SD3mnMzAiswkXvxtROQFe4REmSBmOkQUBnGgjTdwLs3_gJOuVtePXYaANs3wbs06sxbsB-keAV4dYFKBGnAiZEBl0tn2Kbt7y4Gg4_v6As0SZx347sF50HVrn2lDIore5ZDJKW3yAyK4jc2ZjXN2lLeJ7voveMGyRDgHJj1uucfv4BeOOJuy1hTR1LVD3sVOKMjwjNmzRln4CMpMC0zl6lWT9qS4S56EQcrgWDSIH6MG79GVTknrZhh7OR5XkE8i97hlMVi6NHsr0cs4LjwUpju2SAJrEHwCA18Y2kZPoRJx8k8MDhRNAeLnEQ-403NDTr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rFRSmgIquJ7Sd0W9eaL2SD3mnMzAiswkXvxtROQFe4REmSBmOkQUBnGgjTdwLs3_gJOuVtePXYaANs3wbs06sxbsB-keAV4dYFKBGnAiZEBl0tn2Kbt7y4Gg4_v6As0SZx347sF50HVrn2lDIore5ZDJKW3yAyK4jc2ZjXN2lLeJ7voveMGyRDgHJj1uucfv4BeOOJuy1hTR1LVD3sVOKMjwjNmzRln4CMpMC0zl6lWT9qS4S56EQcrgWDSIH6MG79GVTknrZhh7OR5XkE8i97hlMVi6NHsr0cs4LjwUpju2SAJrEHwCA18Y2kZPoRJx8k8MDhRNAeLnEQ-403NDTr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
🇮🇷
🇮🇷
لب‌خوانی صحبت‌ها در صحنه جنجالی داربی؛ کنعانی‌زادگان درخواست احترام گذاشتن داشت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105585" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105584">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBXr5MzcQ-rMSLaBRWOoLqgDCFJ2023n4sR6QHxYFr0EglPxK382JWOSAXv-5qxHJiI2qLIndV0T-vWaJRoVLSZn0_elzEJc2AScW7jBCNxQqQQTugTNNBscapSXiDzXLI6XN8zxWTmloejzTP208CVeoL5c19Vp-sKheIJRSVWPLSMI7pexXL7Nlp6niJhZ39HfNEmpLsX_NNFWW1prOjZRI7GPM-sHRdMpA8o0WcQlGT1KgIe8Iuwf9r_f87idGFcJMOuTc6nLYuvxoavohdyXzRP99OSEQZKesQ7OujVuo67EtPguleKGhNf3--4dSf_mVOesi2HkVnCSqPbatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇮🇷
💸
هلدینگ‌خلیج‌فارس مالک باشگاه استقلال اعلام کرد که در ۱۲ ماهه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به کسب سود خالص بیش 187 هزار میلیارد تومانی شده است که در مقایسه با مدت مشابه سال گذشته حدود پنجاه درصد افزایش داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105584" target="_blank">📅 14:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=tcj4eQClqwMhleEz-JHKbq2Sbm8juaigR2a8IaM4er8RmsyIwvP3ii_MVYcy5a98PPkCsV8zTwKwJM7jn86uHKih0cPMgd0LeuvUt5Utsi498DaoOvnv8BAiYEOxRespLK0faRtu2gc3mL1OLpZwpogKZ4ALmPPoMhVwJPjACy2aULNML1k4WdmAxbCItZTVsUEUAEArJzkmXVUCww-4aGrjtzmC4RI7GiimsfapCCizltr-lZdbaGLkefKRPyV68X1kLvOf1aLFy6OlBIgU9omIm3qWlLXeDZ0VvtM7fuhdSZUYYfTO4OJDos29KVMSS6MIvlMUKsMmA1Lpp_hEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=tcj4eQClqwMhleEz-JHKbq2Sbm8juaigR2a8IaM4er8RmsyIwvP3ii_MVYcy5a98PPkCsV8zTwKwJM7jn86uHKih0cPMgd0LeuvUt5Utsi498DaoOvnv8BAiYEOxRespLK0faRtu2gc3mL1OLpZwpogKZ4ALmPPoMhVwJPjACy2aULNML1k4WdmAxbCItZTVsUEUAEArJzkmXVUCww-4aGrjtzmC4RI7GiimsfapCCizltr-lZdbaGLkefKRPyV68X1kLvOf1aLFy6OlBIgU9omIm3qWlLXeDZ0VvtM7fuhdSZUYYfTO4OJDos29KVMSS6MIvlMUKsMmA1Lpp_hEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
آیا پنالتی امباپه باید تکرار میشد؟⁣
📹
تحلیل صحنه پنالتی توسط روزنامه مارکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105583" target="_blank">📅 14:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PN2LSFoSPtSoGSEfkJLqjiYrHMTPUtzFphcUgFPL-zlEehMSRRanJdOyS84eQ_l5_aIdj95YjG1we07WjB2KNcnrSn_tzzcKikpp4YcrLs-cBcDjQxwJ2L2KlTiZJuB2MQ0J7cwbyBLEHaNf9i7k-c0gYGXKetHRHyyRmbmMNE3tsX-RS6c7H94Pu3S8cZpTgk4jX8BrocsbMiVd5rZWFPzUGwoVqduJVOwIRKLXU1HXz00GthckqwWbadWPYb0MzXPJih4vu91ElmfhB-qYa8CrhSgi0AEq4GIQ6qjLwA8FqGGLMTZrs5EEXW6mrG3m5nBuzEDmJdAUi5H-fTgIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PN2LSFoSPtSoGSEfkJLqjiYrHMTPUtzFphcUgFPL-zlEehMSRRanJdOyS84eQ_l5_aIdj95YjG1we07WjB2KNcnrSn_tzzcKikpp4YcrLs-cBcDjQxwJ2L2KlTiZJuB2MQ0J7cwbyBLEHaNf9i7k-c0gYGXKetHRHyyRmbmMNE3tsX-RS6c7H94Pu3S8cZpTgk4jX8BrocsbMiVd5rZWFPzUGwoVqduJVOwIRKLXU1HXz00GthckqwWbadWPYb0MzXPJih4vu91ElmfhB-qYa8CrhSgi0AEq4GIQ6qjLwA8FqGGLMTZrs5EEXW6mrG3m5nBuzEDmJdAUi5H-fTgIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
وضعیت دیشب فوتبالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105582" target="_blank">📅 13:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0lp9RZHNx7iigFUHeo-jv6jj_nRfh_GQHINCesrrAcJiJKMWXnQcUX9lLGqZlIKXWGyQ-1h12NgssAANW4BUNSd-Cu7bmxwYhB_WHxV9N81MU9UaUVUqB_LJ5Pyck1q8dqnRFYFkDnSjsw-HdXhyCd1UOm63lFR50HIAByGnrB4UFoxUf0A_fboGX7vvOIwOp1XbUqP8MpKtOAu5mSsJnzAYaByOv17t8J-uEcUR_38aypVCAhEIrc5BggpNp8WiQFYvUj3bmp2iP9jLOoxQcOf41MJSzMCAzrPGtPtLiktIjPjGrtjxKDJOnJOs14OK9Y27OSnty2V4WEIvcryeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
20 تیم برتر جهان، رتبه‌بندی شده بر اساس ارزش‌های بازار، طبق داده‌های سایت ترانسفرمارکت
💸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105581" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105580">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105580" target="_blank">📅 13:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105579" target="_blank">📅 12:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105578">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
‼️
🇮🇷
سهراب بختیاری‌زاده درخواست برخی از پیشکسوتان و بازیکنان استقلال برای بخشیدن صالح‌حردانی را رد کرد و نام این بازیکن را برای بازی فردا مقابل آلومینیوم اراک خط زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105578" target="_blank">📅 12:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105577">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105577" target="_blank">📅 12:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105576">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇪🇸
لامین‌یامال در آخرین تمرین بارسا پیش از بازی با والنسیا بدلایل نامشخص غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105576" target="_blank">📅 11:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105575">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzGAwe8e5Wj81rEIEBpig6-oBzW90Y2JGiR22z7oDbkDINKI4dZm12_BOSK-3eeQsreTA4hCNo6o2D6icZ3vTEM8m6RwkyML-qbKJNgOhgObzKLGtAFim4ijkNHDXHnr32OF7fcK-R8v6hagDM8okbF9gc3gfWkZ3r7Oy1F8I2wCW6mGc7BMPuNZf030VeQMDg10jXqJL6UCiYRdi9MLDAPnUXrnGPZhX1d_eOpF5HgCcDcUKmkVhqi0gddHY96eJJnqtbLPtw-1mIPROjYatdnIpQFda-ne-JJd3jSrC3zdiXRdb7nnhO3Mbxe2dxnxzJvWwYnhSgkbqffKsWM2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج رئال‌مادرید در ورزشگاه بتیس از سال ۲۰۲۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105575" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105574">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
زوج فوق‌العاده پشم‌ریزون ازه و اولیسه در تیم کریستال‌پالاس دو سال پیش رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105574" target="_blank">📅 11:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105573">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105573" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105572">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv95tEwzBbN7QUBZXQQ87VW7IFRhACc5SumPmGfmwL75Qm6iIhTgCXFU4ReVUrLWZ9Z-Otj4h4XwEjKM3gzDgAU1NcYqTr7Je_Yyac7dDd38CfEXwXGcIFWg2Vlntj2A0_TenrQRjit5UhMHRu22vSTH_s19jyYfNOZacckOa5G4mKQUtogQTeT1I_35czPi-Xb-cdPtX7_ntnQE4-Kd1JPk81HnC8rSQcDWWjPuRoiIUdbbjkkrBV5WNVvvQwgH3ZVJRbrnCqcGkcn9foYP0VB6IsfIdDZgtmH9LMwNzoKXd8JzwqY6GxUxZpdHbnJcwlaz5zIhB95NBqiJT7X2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105572" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=i-NVTaJ36HxGioJzToEn4TpGI2OGjT5RijLJC5_3RL6sc7XppcGI1TGTiH59NRfmLyPtrQk4R2dEDiWAEwQMS1yJg-EZ839xEMpKofJfP1hM-re9TLZrHEFLfKDhhx-pJ1iRac9TrrO9OsLCvBqA2X-hRQhxnJjoVOVYLeJVRJUUOq5GLhOw_Qo04JVm0dAuC8zT-5y-6AzYxmioiNPs1RN67DmGVKEWhd5vGaigSc74oh7vPbiPfsI1lizrajnEqt95ZOlqfJVJEwOEW4IhWH_CX0MRkh02orBAovqq94FcAtWo0KrZ7QSdhVQAMUHE3-LsKeopvAr3jXJHehh3nZdHT1XRw0vgFQJTVLShfVGF5C4r8S_u8Gvvu1rL_1bjtyyEkDWdCjPoUlCgM6-8ccFxUdM7o3J9VZCscS7y6JZ0Jxynec_u3D6wO5PSu4vM70qJXuliwUDmWd4c1UEaNyGdGyQhRIzMiVIZQ-T0PdSboSninubykkkiRoILrw1KSm3PAeIHNo0vkQRfKK8Q141virnObaFQZIRJwddOI-DYqcJtBbh52Sdqzh5muiarMVbWuSIzeIEK0nmXMTu-P1YVZmPrs0wxY5QnPENhVt6O0OvMK2Xybk8woKKeMTaylwgukjKwoDQF2sBcTbRQdpBHTSMdwb9zikSO13PewxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=i-NVTaJ36HxGioJzToEn4TpGI2OGjT5RijLJC5_3RL6sc7XppcGI1TGTiH59NRfmLyPtrQk4R2dEDiWAEwQMS1yJg-EZ839xEMpKofJfP1hM-re9TLZrHEFLfKDhhx-pJ1iRac9TrrO9OsLCvBqA2X-hRQhxnJjoVOVYLeJVRJUUOq5GLhOw_Qo04JVm0dAuC8zT-5y-6AzYxmioiNPs1RN67DmGVKEWhd5vGaigSc74oh7vPbiPfsI1lizrajnEqt95ZOlqfJVJEwOEW4IhWH_CX0MRkh02orBAovqq94FcAtWo0KrZ7QSdhVQAMUHE3-LsKeopvAr3jXJHehh3nZdHT1XRw0vgFQJTVLShfVGF5C4r8S_u8Gvvu1rL_1bjtyyEkDWdCjPoUlCgM6-8ccFxUdM7o3J9VZCscS7y6JZ0Jxynec_u3D6wO5PSu4vM70qJXuliwUDmWd4c1UEaNyGdGyQhRIzMiVIZQ-T0PdSboSninubykkkiRoILrw1KSm3PAeIHNo0vkQRfKK8Q141virnObaFQZIRJwddOI-DYqcJtBbh52Sdqzh5muiarMVbWuSIzeIEK0nmXMTu-P1YVZmPrs0wxY5QnPENhVt6O0OvMK2Xybk8woKKeMTaylwgukjKwoDQF2sBcTbRQdpBHTSMdwb9zikSO13PewxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
واکنش مورینیو‌‌ و نیمکت‌نشینان رئال‌مادرید به پنالتی که امباپه از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105571" target="_blank">📅 11:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105570">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
✅
🇮🇷
صالح‌حردانی که دیشب یک استوری در حمایت از سهراب بختیاری‌زاده گذاشته بود، استوری خود را حذف کرده! با این حال سرپرست آبی‌ها به حردانی اطمینان داده که تنها با یک عذرخواهی ساده می‌تواند به تمرینات تیمش برگردد که تا این لحظه این اتفاقی از سوی حردانی رخ نداده…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105570" target="_blank">📅 10:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105569">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=tbS3PPvlrH2hgzF4va9PJM_ALAKHCH5Doi8lMO6N-I3UM22mosPT4BcW0qlXYfV1GQi5YoH0EK6-knsdpAbsuWa_-IIRPXUKC9RwQxHcfFlqJhMQ8Q1VX6R9TvmFAcWy_x_HDB_1Cm7jAJ9W4cWsQsRb1dG37v-6DYrnq6z8wVHUloHV_lTmUaKe4VoFABEKrznoh0saa-llSJDqcsoEMs0NNZTszMZSz72vCiBEBpiZr84Ih2bTG2vWvMYO3L7Rm9Cu7hQpee3wqXcehFnIM66s57oUB-0fhFNJc1nluqBS-G2wHgcyTN4rZQKWmM2NxtbO3xrayCa9cg5X0Z8R6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=tbS3PPvlrH2hgzF4va9PJM_ALAKHCH5Doi8lMO6N-I3UM22mosPT4BcW0qlXYfV1GQi5YoH0EK6-knsdpAbsuWa_-IIRPXUKC9RwQxHcfFlqJhMQ8Q1VX6R9TvmFAcWy_x_HDB_1Cm7jAJ9W4cWsQsRb1dG37v-6DYrnq6z8wVHUloHV_lTmUaKe4VoFABEKrznoh0saa-llSJDqcsoEMs0NNZTszMZSz72vCiBEBpiZr84Ih2bTG2vWvMYO3L7Rm9Cu7hQpee3wqXcehFnIM66s57oUB-0fhFNJc1nluqBS-G2wHgcyTN4rZQKWmM2NxtbO3xrayCa9cg5X0Z8R6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
اولین شکست فصل رئال در خانه بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105569" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105568">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQXZLKOozhID2sbLhADObvbb9RbgrZD2abGubfLPichqQUVvE6jWCKiuTzbIMkEC0EaTxXujMHA5m4NugSEZc8VKFEyF1nwnpLkJNqg0KAnx82Ne_nAUOn5YP-i7daV0InKvbyKlZLO0n-ON7a_H9T4mzrQI3gVtWdSpj2uQOLgnfHGnrNI8nhyKFu564btBDI-kL4YXsXXRf593EntdK_Qqv4ykyg-6QZRzGTMGTQkWL08iSctJKZlokB6A55jYWZ03Na7xKUhvU0PXYckUe_MsiXi1kcYK1z8vihqNcgmiR6ql6-v1_hbfX_HkefRDf0M8B-9nHRMC8vhU5tHYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇫🇷
لوئیز انریکه درباره نتایج ضعیف تیمش: اگر دوست‌داشتید میتونیم روی قهرمان این‌فصل فرانسه شرط‌ ببندیم هرچند که من شرطی که خواهم بست رو لو نمیدم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105568" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105567">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=ugT_ZdSKX7PJVJFQqK1WAkXN5AqSFYiNi4PapeCesbVonwxmdjiZuKZ_qOD22tXF45RE50xFY5Yy0E6v9mKjUd6Umym1UmgfkECABg-DlGESrlyGylTqjckDWyZo-BiGQUHg-tFQRnVnLdBNQQHjTOBoiYMoqqvhZui4K6ZXvf2maJxMjCDBH-0-Tu8mAOTmgxhqn1P2_wajqhTgh2YMpPrUkllGgIgSNz3u9fHseYYLeOeL_S2PYaw4KhHkj7QpPxNCb8Aygc_vfDyNemi0LpFwiU5CwhpBcturTUoH0bxMQv3PifVyHOdbw8WzDELuFwXX4yXyPLibvaU6PwlfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=ugT_ZdSKX7PJVJFQqK1WAkXN5AqSFYiNi4PapeCesbVonwxmdjiZuKZ_qOD22tXF45RE50xFY5Yy0E6v9mKjUd6Umym1UmgfkECABg-DlGESrlyGylTqjckDWyZo-BiGQUHg-tFQRnVnLdBNQQHjTOBoiYMoqqvhZui4K6ZXvf2maJxMjCDBH-0-Tu8mAOTmgxhqn1P2_wajqhTgh2YMpPrUkllGgIgSNz3u9fHseYYLeOeL_S2PYaw4KhHkj7QpPxNCb8Aygc_vfDyNemi0LpFwiU5CwhpBcturTUoH0bxMQv3PifVyHOdbw8WzDELuFwXX4yXyPLibvaU6PwlfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
به‌نظر شما دلیل فحاشی به شجاع خلیل‌زاده در ورزشگاه عادل فردوسی‌پور است یا رفتارهای او در داخل زمین؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105567" target="_blank">📅 10:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105566">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=hZfWXNNeaeofXIO_tZROIi13-iObo-tXe_Hdb1Ej1pPZCsP6zZqCZUjD26S94vI6YAZVRNRh79S0j7WWV5nrUX3vtXAlAB5wzb-iKQADDe_IzREAxI3gboe73WxLH2tQPIaVZBXV4m1nt-5J7L0PChsnNucvfEoRIbEnRKdDRCZwpsLeNfGPPXVbiaLHh9w9blmYsUa4RphE_2D7kPBibcZg3DYTI6NgF1owdEcKTwjHuZXmH2qMtczMEaSI2wz8Idxl1BB_VTmsufHG8h_bZTrBuX38WL-KpmgfCBqV4sS4yhJGM1JUqL74BLuGVJ5X177dxXeYyRT92O1KitYHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=hZfWXNNeaeofXIO_tZROIi13-iObo-tXe_Hdb1Ej1pPZCsP6zZqCZUjD26S94vI6YAZVRNRh79S0j7WWV5nrUX3vtXAlAB5wzb-iKQADDe_IzREAxI3gboe73WxLH2tQPIaVZBXV4m1nt-5J7L0PChsnNucvfEoRIbEnRKdDRCZwpsLeNfGPPXVbiaLHh9w9blmYsUa4RphE_2D7kPBibcZg3DYTI6NgF1owdEcKTwjHuZXmH2qMtczMEaSI2wz8Idxl1BB_VTmsufHG8h_bZTrBuX38WL-KpmgfCBqV4sS4yhJGM1JUqL74BLuGVJ5X177dxXeYyRT92O1KitYHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‌مخ زنی به سبک مهران مدیری در سریال جدید مرد سه‌هزار چهره: فقط اونجاش که میگه برای من منگنه بشید
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105566" target="_blank">📅 09:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105565">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=VFA_YqFD0A4C84sjJfyFZ801jz149q4d177FABrEgbNTJG4ctKkANLReKlhmn3DwWyMI_CYb84_IklqDFmF229-ApPbwE2cB9r524JJhSI2Bro1QbYddegHTm83fsULu7BqjqQngXatWcKf0itP_qUqsdCi7jm3io_BSzIsnIEIkwq0UAibjaEAjPNBOT5-_DQKHb9kpgA2Cu8GFkQvVN4NKlbByIXWHit1qRVo1ScsiTpEKLcUBSLukemOx37bPj7y8jKEKRbFLETmUzQdeYV-eWty8ZKwu4Apwwn22RSiHy804giY3gGvECpv1UA9nsKTi8sobwHsG2ri0ZflfXJDwFH0Ck7uvER5XbEZz-WziTLQN7pd2lIGEt_9ZMTmlf3h1Inodv70X-0S1AezX0lT35so4D0TKZxp6jUrxu3Nn4AxmP_0vEDkOIr9sXhJ5ZW3cOjJVFPDw0uWnpEW7CEbMjqnV9IrpE6gZsxwE3OKVsm0hR2ScWQ4U1mzTnovppiltiehTd9LX7sjEHINssQDMzlDhLFvqrik6S4aGPa_Pt0nGTfPM6ARKtcyAEcRiUCPzsRTN_r8pjixpjP2n4y3tPNJRwdnTk4YajRTVoIzrdqSd84XGBnWX-fviAlGoNpPqmzxXopcEoJERVxM7y-ypA-mzto3_0Ze57WPrw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=VFA_YqFD0A4C84sjJfyFZ801jz149q4d177FABrEgbNTJG4ctKkANLReKlhmn3DwWyMI_CYb84_IklqDFmF229-ApPbwE2cB9r524JJhSI2Bro1QbYddegHTm83fsULu7BqjqQngXatWcKf0itP_qUqsdCi7jm3io_BSzIsnIEIkwq0UAibjaEAjPNBOT5-_DQKHb9kpgA2Cu8GFkQvVN4NKlbByIXWHit1qRVo1ScsiTpEKLcUBSLukemOx37bPj7y8jKEKRbFLETmUzQdeYV-eWty8ZKwu4Apwwn22RSiHy804giY3gGvECpv1UA9nsKTi8sobwHsG2ri0ZflfXJDwFH0Ck7uvER5XbEZz-WziTLQN7pd2lIGEt_9ZMTmlf3h1Inodv70X-0S1AezX0lT35so4D0TKZxp6jUrxu3Nn4AxmP_0vEDkOIr9sXhJ5ZW3cOjJVFPDw0uWnpEW7CEbMjqnV9IrpE6gZsxwE3OKVsm0hR2ScWQ4U1mzTnovppiltiehTd9LX7sjEHINssQDMzlDhLFvqrik6S4aGPa_Pt0nGTfPM6ARKtcyAEcRiUCPzsRTN_r8pjixpjP2n4y3tPNJRwdnTk4YajRTVoIzrdqSd84XGBnWX-fviAlGoNpPqmzxXopcEoJERVxM7y-ypA-mzto3_0Ze57WPrw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
باشگاه نوریچ سیتی هر سال نشست خبری ویژه‌ای با عنوان "نشست خبری با قناری‌های نوجوان" برای هوادارای نوجوانش برگزار می‌کنه تا بتونن مستقیماً سؤالاتشون رو از سرمربی تیم بپرسن. امسال هم این برنامه برگزار شد و البته با یه اتفاق ویژه همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105565" target="_blank">📅 09:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105564">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=RKF0LYhCK0KT65inccAs7QoRN5T96JQnkyh5CLFy6vKo2GMGBVqub4NLON4WH3N6xL3iq1XEFM9ehnEek2RWGnsV0D8XHnOHW4ENU8StJry60AGF3C-gZHVurcRO1NhkmhNk8YLI6uyqfd-A2w_JXwd60ih9SjG8V9sQLWBMbDMWC6C19edxkGmWKvJq21Nac4vlQz4AzIF4qfyQNRN1344px0-qAUI4K1fJzdjFAHMcQ5_8elMTEj_ZPGy7w9VhefqzGlkwyPdT6Z-5jT8h_eCCLA6tqCPAcT0yHRfbapl3-xaroEoKtUR_hEK9pSv7rXLAC-olmcWM5dGLL0hRuwgS1H9bntGFMNalkZLOhkRE7EETbEFQLCv88VnxuhrRJnfiFTVwsoKMfCV0D0UZ_AG86-zQTcaTJI62Yb6naRWpCbMrD_ltqRqVMxHYYbKFcHpLLBdkr6ZmEVqU7elGWmBPzcuu1VF-yP1yA6sD5hV6JTvw63iIl0IX5KSuRZCbZiavTqFCbcgqGLDDminy0DJAMYn8fNCVlVYQ2F-6T4HrZCqNK7Gc2fj071uGQpn045TjdxfuQ8xzhddjONVBjNHhH1YKy17VmSM9sqKcpXBE5mYB7HbyBR9u5nZkkVdF6BH6GnpHAvEniS1kUR2WDd_spL-Z6G_APjLYJWHzBkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=RKF0LYhCK0KT65inccAs7QoRN5T96JQnkyh5CLFy6vKo2GMGBVqub4NLON4WH3N6xL3iq1XEFM9ehnEek2RWGnsV0D8XHnOHW4ENU8StJry60AGF3C-gZHVurcRO1NhkmhNk8YLI6uyqfd-A2w_JXwd60ih9SjG8V9sQLWBMbDMWC6C19edxkGmWKvJq21Nac4vlQz4AzIF4qfyQNRN1344px0-qAUI4K1fJzdjFAHMcQ5_8elMTEj_ZPGy7w9VhefqzGlkwyPdT6Z-5jT8h_eCCLA6tqCPAcT0yHRfbapl3-xaroEoKtUR_hEK9pSv7rXLAC-olmcWM5dGLL0hRuwgS1H9bntGFMNalkZLOhkRE7EETbEFQLCv88VnxuhrRJnfiFTVwsoKMfCV0D0UZ_AG86-zQTcaTJI62Yb6naRWpCbMrD_ltqRqVMxHYYbKFcHpLLBdkr6ZmEVqU7elGWmBPzcuu1VF-yP1yA6sD5hV6JTvw63iIl0IX5KSuRZCbZiavTqFCbcgqGLDDminy0DJAMYn8fNCVlVYQ2F-6T4HrZCqNK7Gc2fj071uGQpn045TjdxfuQ8xzhddjONVBjNHhH1YKy17VmSM9sqKcpXBE5mYB7HbyBR9u5nZkkVdF6BH6GnpHAvEniS1kUR2WDd_spL-Z6G_APjLYJWHzBkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: مردم فکر می‌کردند این آخرین جام‌جهانی ما باشد. میخواهیم در جام‌جهانی بعدی هم باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105564" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105563">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=vln6TfZvTaksWoYWTyIhW0EaNWuTEhnw-tv2EHgHOuwbd-iKh1UnAydXIBMhJwiDl8GYm9zcoV4eaf0c1IgSJ8A8kF6lyZr0K9UEX69ifFr8jOiNr5RRCwJbOQy4wxUifjVwsNNoAvCHFaL2l0mwRPbnbwsrPaHuRUt0NXUDEx-3XFz7kfNX3xv8Ll0pt04aW1iNX2Vgmp4ryAqSCfe__PBblKMjoMTxkdn-LNsHy2Wk5Fa8u-KVPdO78HIlbCAS9xoCYXSARucF0UID7SwLjTSnKHIy-2QUHQYxrz3KouxZ6vnWqoLZJX1v3UmLkjZWxKwgt3bdHu4fyENoze0OFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=vln6TfZvTaksWoYWTyIhW0EaNWuTEhnw-tv2EHgHOuwbd-iKh1UnAydXIBMhJwiDl8GYm9zcoV4eaf0c1IgSJ8A8kF6lyZr0K9UEX69ifFr8jOiNr5RRCwJbOQy4wxUifjVwsNNoAvCHFaL2l0mwRPbnbwsrPaHuRUt0NXUDEx-3XFz7kfNX3xv8Ll0pt04aW1iNX2Vgmp4ryAqSCfe__PBblKMjoMTxkdn-LNsHy2Wk5Fa8u-KVPdO78HIlbCAS9xoCYXSARucF0UID7SwLjTSnKHIy-2QUHQYxrz3KouxZ6vnWqoLZJX1v3UmLkjZWxKwgt3bdHu4fyENoze0OFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🔥
جورجینا همسر CR7 با لباسی از برند گوچی در هشتاد و سومین دوره جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105563" target="_blank">📅 08:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105562">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105562" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105561">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arPsWaQFAga2UTCEpEAiNTqui6ZYx5ahqMFVZyk2hOaiIo1am-pStIlV9BtAL73ELuw4lIIFV1djTztFgsByTtrZ0_IyKc6tR9wGOvx9nZQhwWukG6kwFTBO8QTJShmTEGtfA1VrHIVZjxMLn2M9rcKXjJxPmFaReIHQBxrf6Av1iSAjPT95xI5AqmrxJmapJegI8v26kEn9ZalAQ1WKs4QUqiF6G2udZp7SSoXSz5Y-SDnaGYpxgHrJ4a2TUkP26gqO06Qa2ao_cbaicP3HM8QEM7O-tSMicQiG4CNEh78o41LHJV2GPBD3krmZAcLZpH8l7JbdVm9NBP9FdgQoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105561" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105560">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105560" target="_blank">📅 01:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105559">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=LO_pl8cRi3t82Cr4Moo4s_qKEAo3USAumzdBRmh3EWNySUI-TBvXOr1HglZeeupCwx3kyPw25tyx_S7DH_3FHogMzE-9nAiCI5ns2XzmMNVNBSfYPdo1cEG2Y5rvJnWZFG9aWRNblNRRZJ6BqKvapOAec5Mcdi3_KEcQdAf3i2ns6dWSc_zxhLO7dDRsg9c6brwV4iNDhItOtUUvXELNTpwkyCn2PZ6QgQXJ03wDXtgLdj84W9lW7giwlmyrGRdiVruAHzfLltN2cMKO4CWbiH9zngcdM_D6hdbz5eVpgcHjdqivg5If78k5GiK5eyyrjD4Y0-TqoS7nVK1q2lMA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=LO_pl8cRi3t82Cr4Moo4s_qKEAo3USAumzdBRmh3EWNySUI-TBvXOr1HglZeeupCwx3kyPw25tyx_S7DH_3FHogMzE-9nAiCI5ns2XzmMNVNBSfYPdo1cEG2Y5rvJnWZFG9aWRNblNRRZJ6BqKvapOAec5Mcdi3_KEcQdAf3i2ns6dWSc_zxhLO7dDRsg9c6brwV4iNDhItOtUUvXELNTpwkyCn2PZ6QgQXJ03wDXtgLdj84W9lW7giwlmyrGRdiVruAHzfLltN2cMKO4CWbiH9zngcdM_D6hdbz5eVpgcHjdqivg5If78k5GiK5eyyrjD4Y0-TqoS7nVK1q2lMA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رفتار سرد مورینیو و وینیسیوس بعد بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105559" target="_blank">📅 01:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105558">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzxQhtc0e1lh1cM9V4zsh87w8iDkVsmmP9mzOZiCWW3quBP3UVH3jgJgEYGakZhxj0YeEXVU5nWig_X-iJv-ssDY3Ta2t-5K0UWcXEKg1UulSY6FeBnTi1VsJP_nMaDzXMVMSQ_KB-dRe8aeJktd9Vzeqc6-uHRJz5Q_bcUVvjIOayWcMOqEDDN_IsqQMwsYy0ZMmadPMpUTvrCO0_Zf0RWMv-27-niInWPpTl4qSDaK4V50aokXZNUUp_-dTau1lKcLdcryGC-_u3Ab5a7330xUni_uByIf9kLeHzvGeo5ZdnuErmP5U5hovckAlwNbzx4gJ0DhbJLEBfGA0BN-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
#فکت
؛ در آخرین‌فصلی که رئال‌مادرید مورینیو مقابل بتیس در خارج از خانه باخت، آخر فصل بارسلونا با کسب ۱۰۰ امتیاز قهرمان لالیگا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105558" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105557">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCoHS_NAPrs85WPX8s-9zuq9SUi35QLy0sU_RIkGkxlfNOIDL9TiXuuEUI1Q6tBBXBFLJF01xdYhSl6Ue41MMAP0_8Xu25SsS4tyafxy8mmyjG9hKGn_ReRQHKNAXJ1airV10fAyW9TfcpSM9at2kM50SAO-68hfWXtVeOl3ob4OiZelxadfBaXUAMbmCBIsJUnU79bvJvRNGbroASt0sZI1PtMxnIhWNpwcV5D9ujKXkbNoZVcnlR_m2WylWTYeiWLi0XnBNJaM4PAk0PThd0cziAaVF0LR3_9lxhWURpiFYY3AVbqnkkkxRt0NARbzEYGzbXG3tSR2DbJuZUPk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105557" target="_blank">📅 01:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105556">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gErTMT85kvjJ8amq-irq7JKL_5HDJlR8_uBTYbBVAJ6QCIyq9ahiuVfH3HYSHM0dKFMKfny_nX1TfSdUN7OFezX_5LrUlgoAcMO1_AID6azxeoJeCbrCf2KB2DNbP6DR1NHPkXW_YCQ_JPS_kG-mMWlsL9VWSuh8gWBjAyHhgvMiPIHBjPfwzlhe7DycuteFh2tLE5CtfYX8z0vWb07WSnQxq5AuAa0KXIXD5f_1nZNN4Qm15LW6ZQsAOC_YvM6WLZsFzlKklUVaMqC-EWrC6xZdbmxyxwW5-wgvAn70RlkN9mjtB7xys4LJyXVCLafmKgZB8ChaWk2PMZDmqszbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وسط ریدمان رئال‌مادرید گویا باید از اونور یه فکری به حال پاری‌سن‌ژرمن فلک زده بشه. سه تا بازی کردن دوتاشو مساوی گرفتن امشبم باختن! گویا اثرات جذب فران تورس داره خودش نشون میده
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105556" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105555">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGshZrztG804TwRxyNyvmhSLMBPyZAi45dDrd__Eq7qLmCaxZ1LmzeFA0KIF7WWWL0bkdom-s9fUp4p4288x9FB9RfRA4ifp96F8GPHs_HtnUVuWkcHEnoKPJ-O5ujrI7TAUzOw3Jnt5dravKBq8X7Dszy-WbRXOSRjTPyL-DW1cpmhS0WnuC4d7EpAcCdQD-Ya4NQZ2ii7MtsmmQ2RSlOPMW53QT22NiAXowxsLzPud9MEiOswE-Zma_7AOisIk_KgcIufxjVyNGwNcOtKxmoIBuY4TggoyQU5S1WXKf8lkK0wUR0cSKPY6AmL4hwKNF3ggjn9vZ6dA__QLFwKvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105555" target="_blank">📅 01:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105554">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🧕
البته گویا این صحنه هم آفساید شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105554" target="_blank">📅 00:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105553">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy_mBGZ9TdgisoeR1PW8hOwRXiocoDtF_BLm5mdZAdK2yU56MxWM4btlSQPk89-_sLlT3huWehU79yQOnfgUtFXoQU4YwlmaaKJIw5EWzBXRfLbR8MK3MWV3FSIZALVgXNE6klLc3WaNFXKZe68yf4hDqWd7MZFkFYkKlAGh-ka1KjzUTK7Q3Yqc6w7aocfOgVtI3rhwxTOmHMLLYmJAlvOpBU6WnrGUym0MN9TqaPIEdXiJ4L3VMQWRnQ25eQrjFD7SqgfS_-d_zjGS5t9FRJ8cKssWRQtSnNORuGr0wmLSbeJYROCcFTngLs3I-s0Br4C5w7HeH9FH7urBcGllSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🇪🇸
رئال مادرید در پنج فصل متوالی در لیگ، نتوانسته مقابل بتیس به پیروزی برسد [سه تساوی و دو باخت].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105553" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAt-IQt-BA4vEdJ8lZpqMS2xqmgPNv2JgoQciF70oyKysUWOEtg66QfcUHWEJQzBUjviGQ3MoQi7-Lhc6Z_BINke-WhzYvIkGt3GYLNggHMAKmOIf-k5OuSbFMvAfARHi-bucOPzcnOmAaa3vZYYfcYWR___VWCcgfKioELMrLySRpsiasM1Cfjh7QHt-3bZACRu42xAuIE1uZ0-WAhSIzxmdv-FvneVbsp5YWorUo0Fjpw8pZZ0LMCOtrf3usaFdQILoyZ7Uqcc99hqcSiOCyMxf54iBCVo11mjZYlrWLaX6dHWcxxOJKJJqsxo6f5-DG2GzQt9fDde1Z2gbCB_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105552" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105551">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inJLBPQ4ZovOy7VlghsuwspUpVH29OtDI4T5oQmSdcKXgGMEF69MR-jXESWg__FTbALVCGQLA_fwdlg9xWGBACQ0DWYzKbHobHa6JsdaEKSmnCGk65ElvGoUOU4MUAwKP4vji26YpTKHrn9KgxFiTTFBa9kF_fktXT-Jaav3KdQszXo2TdbVbKcbhJpivMJvGTxw0HgR-5KJV6MqcU1M-womHkX_t7U7jCaD3ZemcJVPRA4AvmeUtMA9We3mHiD5NXBmEpcEDLj_6cFJiMOk9w6TS4J2K82W1f8iPu-S2mFzCMYKBXgcx5KE78JTfviXO8q1jZ6n1Ec67_tUHLYjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105551" target="_blank">📅 00:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105550">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105550" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105549">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE6jfLixIJt-yaneNJOWSXNSiZgDjKiOTCkrN80xcavxW7RjBjdRR8wEVz7YWLatU9DC-nldIFcbMx7ovJzENK153dzNq9ihWgjPsdOFkZC5yJwNshgGnbDwPVXvbegT46DJljEjmWga1vJ_-_fV0IkkRPEmTQxzDDLiaEKoHLP1eN-EEVOCh5s09gVTSa0v3OPkzmkN-EjDuvzmjHC5li5B7FNPjzFP-tNZsdaQCN_Z_m9Llf8hvAy0bUf2FjIGls1spB4DBChlgm8gvEhFWeRpJq7VK9fHUpy8e0s3qpxgi0MxLuR44lyJYwYG2K1gp671RMVUGzwkmKLcskTc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105549" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105548">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رئال‌مادرید بدشانسسسسسسس
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105548" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105547">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وای خداااااااا چه شبی شده
😂
😂
😂
😭
🔥</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105547" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105546">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
امباپه ریددددددددد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105546" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105545">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بدلیل خطا روی وینیسیوس
😐
😐
😐
😳
😳
😳</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105545" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105544">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">برای رئال
😐
😐
😐
😐
😂
😂
😐
😂
😐
😂
😐
😂
😐</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105544" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105543">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پنالتییییییی</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105543" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105542">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdLO3vCOdaziBpW4vewMDszp6fY6IPCD8QKJv609ts-a36DWo8v4sDqFJlltCsSSkHfV1UOhqrq1avntYrsDdV3tqfp5A_iGZNCiF5U91bpFDCR8g1ToiboKL0rXuROvKKPVmxnXc-xoS3E_VU1Yvu0bAcTkJ8hvde-OhM2p0s0X9LNkrF7_9HFG9mlzTszthzyFVtMZrEkbMQ9fbjKjUW8EiYp_jlfY6XDB-vjNYV6Pfb5RNTq3dTJxLWXfUX3eVQGFdAUMvo9KriP5pOZ8gT7Oe1hYo74HAiGYwtfZ5sKVB1lTBBn51CEGKJHQnd2mxxv2UwYIc4i0wOQrZ3LVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آفساید ببینید و برینید
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105542" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105541">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105541" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVZWMbcDEvmiF8TmkVhwIgPyfSCA3SrvxEWgp_wyP6rnBdMf-uXWaB1a3lV3UQULY91f8wClxg9PKdvK7gLIuCK8OFoDij7Jq9L68sLm6PWOR1rqTOpnk1vm6YrCbkrmWNgQ_TrCI89ukepbGp-HZvb55yKljx0bwp5rtlt4joYa92BzXc6_GmdYwoXxCodjvKd_UMTvvGcR3MxRs7rSNV4YP8ptjofMUuiZ87fULVo0CbQk6lXisxQelyH3HMUxozLEhe_epWlbSORXKbLnoG3wtTOctnEZBMrbzRDWXRInMbzuo0VoxxCpGVnj0hm2F18WVw6RBl6vS9oRmM8MVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید اسپییییییییی گرفته شددددد ریدم حاجی چه صحنه‌ای
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105540" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105539">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🧕
آفسایییییید رئالللللل گرفته شددددددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105539" target="_blank">📅 00:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105538">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🧕
آفسایییییید رئالللللل گرفته شددددددد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105538" target="_blank">📅 00:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105537">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اوه صحنه رفته وار</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105537" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105536">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسپی نگو سوپر بگوووو
😐
😐
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105536" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105535">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رئال کامبک میزنههههههه ببینیم یا نهههههههه</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105535" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105534">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چه گلییییییی زدددددددد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105534" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105533">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پشماممممممممممممم</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105533" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105532">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سووووووپرگل اسپییبییبببببب</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105532" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105531">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگلگلگگلگلگلگگلگاگا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105531" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105530">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رئال تیرررررر زددددد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105530" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105529">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105529" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105528">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسپی برای رئال‌مادرید اومد که گل بزنه
😐
😐
😐</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105528" target="_blank">📅 00:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رئااااااال ریددددددددددددد
😂
😂
😂</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105527" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بتییییییس زددددددددددددد</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105526" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلگگلگلگلگلگلگگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105525" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105523">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62db78c19.mp4?token=n2zN-6_V7xITAowFc90Hq5WlaEIiGkdzO6p379Y5Ztl83azNZNdvCVPAc6DZvXHUaXfshwlIMRvP3Zr1Faa9fFLRc1XlncquJjXDGfoR6aiVkjoc6uky-JzbPwuiF_uB6yFwIpX5QvO-ja0f_atZwJKl0DBywqrULXgxwjQULkkJomkq6Bh79QlzUKBDYChDTS4ZLwtZizU4fmuDrtLODOlyCqbqXDBsAaSAmiLEh2mlBR7Cix6GtzBYcUuPhTc9KdIY4DNhwvwURlGezfMfidR3vB3Xb6GM4mJbLRI4ad-IlqklA5jdTte5Oj181Ez2xfE5TztyLSY65daCo_01hnkZkvLHBBUqoQ-P2b6nnwns59FS-BV_3VxRZyzf0BE9Bb403nKwpSKzDjtLorSJioAuS2rjH692aZE6UzwS0o4VA12LCjdZ3XLnPayLBU89waOyPWxjJu1So8ctZ3CEAgks4NzUVZq-G1f8aB9oT_n3WSVD3-IO9pumVzvNhrhLsgZX2MUCJFV-bTVhVEsR1_I3kmt_MSICrFq2XNvlZkBBT-C_8pZFbnq4_ZwXijmqI1sbLLE78u1MBCmH3P2dZc6p8X-KzXQ_MoQIhz0M7gtIj-oWs1fM500BuN32vLPST_VeWE49A-AstEh8rxhuGoHBKJzFSOoUjvq2H2mgtKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62db78c19.mp4?token=n2zN-6_V7xITAowFc90Hq5WlaEIiGkdzO6p379Y5Ztl83azNZNdvCVPAc6DZvXHUaXfshwlIMRvP3Zr1Faa9fFLRc1XlncquJjXDGfoR6aiVkjoc6uky-JzbPwuiF_uB6yFwIpX5QvO-ja0f_atZwJKl0DBywqrULXgxwjQULkkJomkq6Bh79QlzUKBDYChDTS4ZLwtZizU4fmuDrtLODOlyCqbqXDBsAaSAmiLEh2mlBR7Cix6GtzBYcUuPhTc9KdIY4DNhwvwURlGezfMfidR3vB3Xb6GM4mJbLRI4ad-IlqklA5jdTte5Oj181Ez2xfE5TztyLSY65daCo_01hnkZkvLHBBUqoQ-P2b6nnwns59FS-BV_3VxRZyzf0BE9Bb403nKwpSKzDjtLorSJioAuS2rjH692aZE6UzwS0o4VA12LCjdZ3XLnPayLBU89waOyPWxjJu1So8ctZ3CEAgks4NzUVZq-G1f8aB9oT_n3WSVD3-IO9pumVzvNhrhLsgZX2MUCJFV-bTVhVEsR1_I3kmt_MSICrFq2XNvlZkBBT-C_8pZFbnq4_ZwXijmqI1sbLLE78u1MBCmH3P2dZc6p8X-KzXQ_MoQIhz0M7gtIj-oWs1fM500BuN32vLPST_VeWE49A-AstEh8rxhuGoHBKJzFSOoUjvq2H2mgtKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
مهدی توتونچی: کاش به جای علیپور، کنعانی به مانیکور می رفت!
🎙
وحید فاضلی مربی پرسپولیس: ناخن های کنعانی را مثبت می‌بینم یعنی او تمرکزش کاملا روی دربی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105523" target="_blank">📅 00:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105522">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=Cmi0_ITYaFUgI9EJzy9B41GWqy7iRvu4OjMGVCyLCgm3_dPRzWQqUi9Aly6Xgf92yaavWSxu8LRMo_iUmltS-S3PEKpFG6TZ9pHFt_Nrual3u5m75JBOaMWhQtNTXULVoMly-SYgkH6e8n5hyVi2ne1SC2-q3cwvx2GnbmaCk83BJGcZT4_MRr9-FbJNtPSTHQUfJxM_5Z1CZ0fIy_jmEM6opWw6M8nWDFITOdvsxEi3laTvsL5_1di7B7k9G3aoIzy2F79T2_d_2xWFaFZZS5UPFEwaGX77nnP5Yl-qraBlaSDysYaiIDz5RkLwgwQgrf6id5TY8R4eBSvf9lrlWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=Cmi0_ITYaFUgI9EJzy9B41GWqy7iRvu4OjMGVCyLCgm3_dPRzWQqUi9Aly6Xgf92yaavWSxu8LRMo_iUmltS-S3PEKpFG6TZ9pHFt_Nrual3u5m75JBOaMWhQtNTXULVoMly-SYgkH6e8n5hyVi2ne1SC2-q3cwvx2GnbmaCk83BJGcZT4_MRr9-FbJNtPSTHQUfJxM_5Z1CZ0fIy_jmEM6opWw6M8nWDFITOdvsxEi3laTvsL5_1di7B7k9G3aoIzy2F79T2_d_2xWFaFZZS5UPFEwaGX77nnP5Yl-qraBlaSDysYaiIDz5RkLwgwQgrf6id5TY8R4eBSvf9lrlWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📰
🚨
📊
آنالیز دربی پایتخت توسط محمد تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105522" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
