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
<img src="https://cdn5.telesco.pe/file/u27T9V7IaRsiPBUvXS96LN-zjhow6FxtK0YToFOB7ecvSRivQpKuilZMyYH3kmczdXmIaoXm3DeLPho1L7LOMhimYGAIAOyuAQADQvA4yTdN14pipRYbXLPwiuqIsFcglK3nI6nGKsUFbqpRoYrXS9SwireRiXO_6Rh5NNyugSq95E3oSmr0HDZ6xTdLzQRi-ypcvPP8967hn-nNoaO-SonX5AAerUV48TfkfT-xEygyK0LN5-yRtRrXNwM4SByULmb91k3NxTQ4n_hjOaFk54sDMecpXa_yvjtlnuhRiBnK2BH4_JyIaNg2wNH-WufhhajrG6DxHxc2kMoILBHgWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 412K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-106586">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8940fb69d5.mp4?token=nmuZprnU1UjvRibC1exrsBBkZKiV-4RvT7_b3nFf1dMPCHrO408kCT90OyZFfTTSVWi9-0zqJvOTM2DOeMF5Os6tspvjzF_pW61immwiV3nzt7m5ewBKiTq7YGFF32REoZvgEJOQBT8I8KBY9OFjS-e3EhZuq6D5rmqg0kOSF3aHQPFeIqTbT3zShH8PL4q8AO-JbCmZJykMmaEjmm7HiGMdY2Vr5hH2NY_rJmb0imyJQu8XDoG5iJpQrurfnsC8JDiVjNA90ncYJh06WQuKCFYt4Ttv-5c4Hx8QjGC98X4IDXDkml9LIjVfnBGdabuX9UWnrBLfVsVw1e4TZutV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8940fb69d5.mp4?token=nmuZprnU1UjvRibC1exrsBBkZKiV-4RvT7_b3nFf1dMPCHrO408kCT90OyZFfTTSVWi9-0zqJvOTM2DOeMF5Os6tspvjzF_pW61immwiV3nzt7m5ewBKiTq7YGFF32REoZvgEJOQBT8I8KBY9OFjS-e3EhZuq6D5rmqg0kOSF3aHQPFeIqTbT3zShH8PL4q8AO-JbCmZJykMmaEjmm7HiGMdY2Vr5hH2NY_rJmb0imyJQu8XDoG5iJpQrurfnsC8JDiVjNA90ncYJh06WQuKCFYt4Ttv-5c4Hx8QjGC98X4IDXDkml9LIjVfnBGdabuX9UWnrBLfVsVw1e4TZutV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇪🇸
پست‌سمی الچه در آستانه بازی با رئال‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/Futball180TV/106586" target="_blank">📅 19:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106585">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
🇮🇷
🔵
گل‌گهر در شروع سطح دوم آسیا مقابل الجزیره امارات به تساوی بدون‌گل دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/106585" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106584">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6whzucQaq_Ndfbuy0T5wFXdQG827CaWEQ10qU77WkX4UeJ8DMy8Swgn7vQP5MTsqNRxhWKcTmqRull22bLdfedK-a0_H0no3AR54ibdTsMwk7s4Vt2j5g-Dq-ceughiv_UnuitiZqSl0SkdVIZ_0eUimOA0GKqYQ9JQ7E0YYKjfXmhWCRAPrrzohJM89L2Ljk-urtyPq6NOKwTkL-mbbFOB_rf-GYiyMKENmYFH9udsXxLgNO_vuwgppXFVrnhU91h4It-7ush03wAKX9FgI-Jasl_fpwGRpFzZFTnQl2jGv-nbB1oz19lRgCenAieM0vbvhFvkE0RPhhZFJ6WlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
لامینه یامال دومین بازیکنی در قرن بیست و یکم است که در 5 هفته اول لالیگا، 3 بار هت‌تریک اثرگذاری در لالیگا کرده است. تنها کسی که پیش از او این رکورد را ثبت کرده بود، لیونل مسی در فصل 2012/13 بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/106584" target="_blank">📅 19:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106583">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e25f47d65.mp4?token=WYICAq0nhSPP9dBBP1HmIt_u6SfDwlHxuJ8mt6-KA8QFO6HoiWuSAk6NO-WhzyK9zRspM-NynFd8Zd5DFEgqqfAPkOkOf6sO8kX8jkSZ2CsJYVOxa-qY7HpqTByMPivJ1SuRAP2bUibI-yXiJQ-w3muUtPaLdrEuyd_xyFzDMB3t0SyN96E4C4Air2cwTaseVj1w2RSZ0Vplcn2Of8f8BfXSVGiT5ndwo1i7xadEuJ_X4O9z0BJYNJTV4NCJ_f0zhboWDDJVbM5YrTFlHxU2_y62jezusM7-zAlR0CzXGeijGyuChtu-qq-7KoiVkBfF1Jh3vty1u98g1gu7hVDmiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e25f47d65.mp4?token=WYICAq0nhSPP9dBBP1HmIt_u6SfDwlHxuJ8mt6-KA8QFO6HoiWuSAk6NO-WhzyK9zRspM-NynFd8Zd5DFEgqqfAPkOkOf6sO8kX8jkSZ2CsJYVOxa-qY7HpqTByMPivJ1SuRAP2bUibI-yXiJQ-w3muUtPaLdrEuyd_xyFzDMB3t0SyN96E4C4Air2cwTaseVj1w2RSZ0Vplcn2Of8f8BfXSVGiT5ndwo1i7xadEuJ_X4O9z0BJYNJTV4NCJ_f0zhboWDDJVbM5YrTFlHxU2_y62jezusM7-zAlR0CzXGeijGyuChtu-qq-7KoiVkBfF1Jh3vty1u98g1gu7hVDmiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
امیر نوری بازیگر سینما: والا منم جای نتانیاهو بودم به ایران حمله میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/106583" target="_blank">📅 18:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106582">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cfdd069b.mp4?token=Okrn2lclBCLnNBQidkB-GVp-6CALJxbcTYcCm-TJP7fgwgTYEt4A5_Lm2uWNoOkOB0F-gcDMrmHkcMJOTsuNxfg_z67FYJ294OSY2KqLaYrScykC-Eqt1KYqmoGZKnqupZJJhKW5swTThljqOTE8SFZu6Wp6uLz1nsXme-KDU-Et2Dmkud5BJWKyhG9ZanQjMO27BQHrsA7dwcM-f3xVJ9tf4GE63CWpzFs-ZVTriNOvIG7uRb45iP41TrSOF8nu0cF-cj5FMgw2U2wev1oReM3vhhAqF61vIHA0nOAn0Pyx5AaWpIoeQsgKjDe6N4BYceXvXiXPJpW2DQSSLvsM7pb5HiU8sqqSWjMy7Bu2Dwq0vxqnknTjmJaEsUCyWpp8EGYlUlCsW6lGnjo4CrAWkiV29keMd2WOoQarCk-hI_oHxf24ir-zlJ1h5h8m1h3hQ8dunisuptDCpyqjH2tc8PIZMPNUKAofik0pATTEOmQQaOsZjbabVltY1xr3SvMcp5qxiLqymLP2acNeqw2rAOenZbnzxeKqWA6dwBSRlHklrkQ_wrpTBoXZ1DlIwLz2gSC--NdwRtWsrL16CSd4DBnqbalq7vSDRNw1ctTHzxgef3vwqFlu-tOBkkqu1374WrCCEXHEoxvK677j-hmaVaBGQqmDud3wUDOeBbSEmuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cfdd069b.mp4?token=Okrn2lclBCLnNBQidkB-GVp-6CALJxbcTYcCm-TJP7fgwgTYEt4A5_Lm2uWNoOkOB0F-gcDMrmHkcMJOTsuNxfg_z67FYJ294OSY2KqLaYrScykC-Eqt1KYqmoGZKnqupZJJhKW5swTThljqOTE8SFZu6Wp6uLz1nsXme-KDU-Et2Dmkud5BJWKyhG9ZanQjMO27BQHrsA7dwcM-f3xVJ9tf4GE63CWpzFs-ZVTriNOvIG7uRb45iP41TrSOF8nu0cF-cj5FMgw2U2wev1oReM3vhhAqF61vIHA0nOAn0Pyx5AaWpIoeQsgKjDe6N4BYceXvXiXPJpW2DQSSLvsM7pb5HiU8sqqSWjMy7Bu2Dwq0vxqnknTjmJaEsUCyWpp8EGYlUlCsW6lGnjo4CrAWkiV29keMd2WOoQarCk-hI_oHxf24ir-zlJ1h5h8m1h3hQ8dunisuptDCpyqjH2tc8PIZMPNUKAofik0pATTEOmQQaOsZjbabVltY1xr3SvMcp5qxiLqymLP2acNeqw2rAOenZbnzxeKqWA6dwBSRlHklrkQ_wrpTBoXZ1DlIwLz2gSC--NdwRtWsrL16CSd4DBnqbalq7vSDRNw1ctTHzxgef3vwqFlu-tOBkkqu1374WrCCEXHEoxvK677j-hmaVaBGQqmDud3wUDOeBbSEmuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی مجتبی پوربخش درباره جاویدنام سحرخدایاری ملقب به دختر آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/106582" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106581">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106581" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/106581" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106580">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5s3gSrBzxcmBBwa1xrfkMz0W7cwkFRg93C42a6v894tg8V5Q4ilumjnVALREfOSdPPNaQu18MhIG9nirKlRFALPrGNDpvQDz5b1trbReMKH8gxzsQsuQ4JI9pE0QIpJsYxrvcbWWM_U6KUU0NDE2uTCOkPSDLyZfF4ZvcnVJZgkVFk51f8YskX9Qf_fQMMuncOTSI5mQODea5aOOUiJjO1zJ5felEu9948Cox5aIr0w2SFBMNc4gPQWVkQVQ9pb1MCgdB_0Dd2vJKo6ndK2EHIHS6wiaNCNmisQi6sPU7Kr8eqhihcUXGyNU6ooaDvp4OndKKlNmqeNUnwAvv1h5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/Futball180TV/106580" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106579">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0ea3f6da.mp4?token=kN_nZGYfUI9n4hwx0-Q8cws6MrTr3XjWpsvc4gL955fRyVNRwzgG10AVRK27mMWH26fXeKcOu7CxzfVT-2QG7aqcRgDNDfHkp2uwX6pVZf_ULwf5uWu-LHsuNjjCFgHUvN0LDq6xFQShvmlcr09Ss80bDJnl11hHCdEjmjmXLlIGBJypG9k0du6CR1bRvP3Bxe9x34CyK6uF82QCrZ8Zc3aRHyJyHnkvv8h5StlvQKMOYA60KAhM7hn2nPoP-GhGA2ATIy4a_oJgnLoe3Jpd6suS5a__ZJXsBA_Bwpq6vwhwqmEW5sK-IxOiRAA1QqOEyNundoZwbVw88kxa14EKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0ea3f6da.mp4?token=kN_nZGYfUI9n4hwx0-Q8cws6MrTr3XjWpsvc4gL955fRyVNRwzgG10AVRK27mMWH26fXeKcOu7CxzfVT-2QG7aqcRgDNDfHkp2uwX6pVZf_ULwf5uWu-LHsuNjjCFgHUvN0LDq6xFQShvmlcr09Ss80bDJnl11hHCdEjmjmXLlIGBJypG9k0du6CR1bRvP3Bxe9x34CyK6uF82QCrZ8Zc3aRHyJyHnkvv8h5StlvQKMOYA60KAhM7hn2nPoP-GhGA2ATIy4a_oJgnLoe3Jpd6suS5a__ZJXsBA_Bwpq6vwhwqmEW5sK-IxOiRAA1QqOEyNundoZwbVw88kxa14EKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت ریسینگ حریف بعدی بارسلونا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/106579" target="_blank">📅 18:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106573">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMqG9A8eCT2wWvnCLf2SRtDcmS-jDM-eBL7j936lpsXSKAnNHg0FUYwsoLeEvwI-GKHV37Z-DHZdXcHJ-og76OAPHwLdyG5Satd4SEeK5uy2RbDky5n0CA4hS4pavBbwyBTHqbc6ziURoiyaIOU89ACdLj0pmKkD9y1_F-o_IKvmFlVIEd7szfcE7U2Vdl6aIhqBh6W3tmNx6v6phtnVEKJZYMf-WwF_gk9Vjn36k33qKKQ6_nv6QHaOZOUNyq8QuyJy3FSHSsWDB1oLyvcFENr3ofmGQ6zr5aO8PM5YaJcV5HLf1e6qLNt9Xn78_lRg31PiyevQWHG4zMipYgubjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5yUmu7eS8AuAciz3bGIuc-KIymBAfIKrxkqzQAoeBABJymZaOP-WJVcsjtLcMxUHEOtm9GpqZoeUBUkmvZr_6Ufll2pQ6m3Sixke0DmJ0-gZoyD9kixwVWeAr6of01XTrK8ucCRae2B3qOWYJZkFJh-KsqiWDw0tX5CJ2QeArAPh_pYRAHE4cnO_N6WTadD_MiKvzzagIyOJcUfzoObsNRLPkiYpfr1FeLqbQtiyFlMuSV-ScNGTUZCrkJvgbqcDHnJnnnj_25UmmkXstTkR-eMHAV4jPuJ3Ic7xzaFf4Dzb35-57RpY8dKMziZTJHxtYlWn9lXYNe7ODJx4oQ2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCHtGBbfoz6JKaPfENzx83JqG8eqDo_ChuSiTNNOOk1i24q4QaKhVLuArjnaDZzgsn990tg_my8g6vNPDA0GR4kBrwTizEhu2TThUELaABtv9siSSgjE3nRUroB8wI1i7uB5EVmtQgziAtt4PVVLgRaaioemgPhAId4gNo36WAYxQ1MRIIKgfq_j_cZcs9BurWK1SQxyuUHMEHiZLRR3_kRRD93aqAlfifNz7wwOj9sph1XwGJ-IOwbm-FIXrzah5pDNz3qiGbe1WTAzppaWP3H7Z6BKXDRY8bI42MQC2J6euejCLFPj8fN0gxruQaZPzlFr2n462fWlbmJrNVgb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIdbnPl32HeIOtRYTA2eIzt283gmA2CYWXz1CGnL3cVc2NlGPA-dzqyDObkonSVpizhsBqLfnJ9qlOI-Xvq8a9FmrgdT-_xuJb30o1nSRDctr9ulOjBMvmDC02RrEXkO-jkaY78FtaAPyT7m4fs_RFchSxv6VVQAawVNI40s7hftol510DzcpzetJVkzUmLNVsrhzeHVhnv4WZ4qRh4GKRx6m5z3oEtVQMhVyodr7i9tBQu12a78xS_e84PINDZyF78mC55FlJWGfEgGmVgJnPS-9V2Js6qm6kxFegZjuWyHEK8ZLeuYan79MdAdJP1R8w0hNQ8FMfrpEI2DcjMWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xut5J1qeRY5GOWiXclolt6t9ueit-Aj2osA4I9M3QJ0k1a9O3hWmdXOjPuSH1UhDtl3p9Bhg1eKbVA9Ea0-TmeyVt_FcQQi9ZQIl7BJDfTFSw0rrATJnCyP7lN0Wmk7XKfbjUDvtqV-VR6z0WZ7inabpoGEHXv_6fozhckCSy8lJOwMl_7XP166_-15OOknurrrw9GGBCaGMgFTo-hKseUHnP-MjcgoRymKexgPAR6pYidwGx-t_jgBStRZvEsAvnvnE53p0KQ5d5H5_IeLJ_zA-igF_0K0rHEM3AHrgc-K_rYraHUqmh19EeoybpjsEedpw9M3dOAlNo2Sdyr7jCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsvpX_QEyMPDlLor4QJ4wabIPaaswl2pG-PNt2PUa6Y4_9teWf8A-OMJPYaln35WPgu-RhNwRy4Ns_QGx_ktVvOkJjiHdNvZh7mf4rWM1Q9Gs9gTudtmQmgNRXPhyHsilLMUF7eUwYm1dmYM7coGemhBLp1CSaz6V0q-ugB_LwRQtmUPtEi3Qqu-cLXH6yvrl02SzA9nuSej3I2QpYGXckwKpsOYYyCKcw1cTNBLDD15GDXH-82VL8w8phFUMyPFpL1QLrZRXVk4cOTGEgO7aEbAVFKTT00NOKbiFlfN31d2wUm1aYFs3dRzyfv50enQq7sDvgGggG22VkztfzTQcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
سیدنی‌سوئینی یه تبلیغ فوق‌کسشر گذاشته که داره چندین ورزش رو به صورت تقریبا برهنه تبلیغ میکنه. همین باعث شده از سوی عده‌زیادی از بانوان مورد حمله قرار بگیره و به نوعی به اعتقاد اونا باعث ترویج برهنگی و نشون دادن غیرواقعی ورزش کردن بانوان شده
حالا تصاویر سیدنی رو ببینید
😳
😳
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106573" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy5c6IL4y62QNJ8kOcerHoxb803lZEkOLYrHHsR4N8Cf-4yh0yUKdh-8FGUxmjvC5aSdnlJPOOnk3YpTz-S_6R9temo6Yxi50J25XcIcW99g1C6T9mkOl25q2KLCz6YFDZ4CQ-NAGrDIFcB4nvHuGXxhb_7KEen0f8jn0G9q8MdZOXEk9uf3yqis8q69OxAjz0WBdGcjI5VUFnKB3g4GVhZ0Alp0nHaQeX3BJtWp79kBWGHlxv4sAr0RZruiK47gsXGrvaGACtXI3cj2BuRXtEcYxGxL-TCex2uv8rBaoxko1hej9w-wkJC-YQCG3EAHzo-H8KtMnwXQds9JNwP7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
جلد امروز نشریه لکیپ‌فرانسه که بنظر باید برنده توپ‌طلا رو از بین همین ۵ نفر بدونیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/106572" target="_blank">📅 17:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4542b716f1.mp4?token=UEVHvGCtiB_1Y26D2NfQENcljZ3a1oIafpFTJ7bGKA_7ro-4fJLSYa5QZTeO_fXz5-jefqYLaiz8zbVzcwv-O7VUUWmcOmwUnzIdmhPlU9q0pd9ebOWLJZ2AN_sk7BUbqX7fDJ3eAO260zHdL_2e68pGPVQpMNvJ2z8AM08TvtSiuMWqga6Vx5MylFsW1YSYgx4l3NjB3cS4Ax_ZooNqCrnxJIWzfzBbj3YjDhSeD0jU6YNpdXtvudcNYfn5LFcZdYyIRkbrEXwRghQCzX5t5pNs1BhXbBWYr5eJq4Un34KB1nGkYPqwUKIwDW886panFLxWSRRj6_F0UPJsJAkxiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4542b716f1.mp4?token=UEVHvGCtiB_1Y26D2NfQENcljZ3a1oIafpFTJ7bGKA_7ro-4fJLSYa5QZTeO_fXz5-jefqYLaiz8zbVzcwv-O7VUUWmcOmwUnzIdmhPlU9q0pd9ebOWLJZ2AN_sk7BUbqX7fDJ3eAO260zHdL_2e68pGPVQpMNvJ2z8AM08TvtSiuMWqga6Vx5MylFsW1YSYgx4l3NjB3cS4Ax_ZooNqCrnxJIWzfzBbj3YjDhSeD0jU6YNpdXtvudcNYfn5LFcZdYyIRkbrEXwRghQCzX5t5pNs1BhXbBWYr5eJq4Un34KB1nGkYPqwUKIwDW886panFLxWSRRj6_F0UPJsJAkxiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
چطوری سرشونه های گرد و پهن بسازیم؟
به توصیه های استاد هانی رامبد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106571" target="_blank">📅 16:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO36-mx-xZuoWoIcsr3Xf-1FqKztIm-hoCS-6QZFVWTNSJKXOYHNjzi7xFSZoiJ34-tg1RT6hyukuin-kCZQwU7uD5dEW5zV6asFesupTk-2wZkc0zz6zPaFNp49KkFhFXsx6Z0zlvkXuPc2icYfujKM6NRsbFpes0AsFEkhraNhM8cUuGWMsvg_tEZeeyFhNTTyx0RhKbKJXUb1liridO4QeqqbwIUcwfzZOljwBCz95Q-4HFe6CAgGDrXkZmqtlacN7GBKhOwSSt68R_f7fNs6-fxnUBSVFb4ikJYrZtVuuu0CrNxcheFc4CawPwjAUgsKbBgYlmTisVWLtblZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عملکرد فوق‌العاده‌ پشم‌ریزون هری‌کین در بایرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106570" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aef2c9a7f.mp4?token=QisQBO1tAkB8PfeMP2_gK0xAgRs00_o4YF9oSp9G874gd-1UtdnTqYsHNOJyJaqhGQ0w5GJh2FTh_ELWHbJ2N-IGiEsWxRgHkmX_burQY3Y-uVipiWtmIbabDsBP_6fz7LzJuwRpGEf64k9uhxV4GU5M3CkueqGbe81H37BUUB-kHFsDjdvD0WhNsrQ1TMZPWp5YLPxE1xFTqnOHyTyw_3QlWWV_uTPJ3zTSP1ixi3kj1ZintTbvlStQSNk01-Wa0M4_-9Vb_yEfKVuHqflMCULhuPWwZurQLvpLTCuzcTlZH6MA7rbLRmFlk2phL5DzVuCP1oaVT9gyds2mkvOfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aef2c9a7f.mp4?token=QisQBO1tAkB8PfeMP2_gK0xAgRs00_o4YF9oSp9G874gd-1UtdnTqYsHNOJyJaqhGQ0w5GJh2FTh_ELWHbJ2N-IGiEsWxRgHkmX_burQY3Y-uVipiWtmIbabDsBP_6fz7LzJuwRpGEf64k9uhxV4GU5M3CkueqGbe81H37BUUB-kHFsDjdvD0WhNsrQ1TMZPWp5YLPxE1xFTqnOHyTyw_3QlWWV_uTPJ3zTSP1ixi3kj1ZintTbvlStQSNk01-Wa0M4_-9Vb_yEfKVuHqflMCULhuPWwZurQLvpLTCuzcTlZH6MA7rbLRmFlk2phL5DzVuCP1oaVT9gyds2mkvOfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
فاطمه‌مهاجرانی سخنگوی دولت در پاسخ به سوال یک‌خبرنگار درباره چرایی تبریک‌نگفتن برد دیشب استقلال: ما فقط بابت بازی‌های تیم‌ملی تبریک میگیم و توجهی به سایر مسابقات نداریم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106569" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec515fb788.mp4?token=LioFSCRauiysqYvcyTyVd5raOH0CZySXM0VALhRFZEbIUL1Hq4k9U1B_aRa5dEJzPg_5UswCazcw1r8MCTSOKsjM9UEBvunkOTIwR4HZ5OwGp8JndHebnYmI3FcqeNCJ78ogiwFpbGy_HSKqK-eyrMtE_njZqO7KsssE7hVy-I1n0qiew24PoW32L9AM0wUjZ6YFmjz5Heh_CDrfOuYiE09QT8vpymKmbshM45gCBfPSO9tDRuK4dPVUBIcXhiIX7YzBdGc1E5sF5SPYPZWva3JBlKUDttj0aYaJxzTbGYdr1F155kFvAz5Cmp1vC1chYH3lxK4ukNbx7YP8qJOQhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec515fb788.mp4?token=LioFSCRauiysqYvcyTyVd5raOH0CZySXM0VALhRFZEbIUL1Hq4k9U1B_aRa5dEJzPg_5UswCazcw1r8MCTSOKsjM9UEBvunkOTIwR4HZ5OwGp8JndHebnYmI3FcqeNCJ78ogiwFpbGy_HSKqK-eyrMtE_njZqO7KsssE7hVy-I1n0qiew24PoW32L9AM0wUjZ6YFmjz5Heh_CDrfOuYiE09QT8vpymKmbshM45gCBfPSO9tDRuK4dPVUBIcXhiIX7YzBdGc1E5sF5SPYPZWva3JBlKUDttj0aYaJxzTbGYdr1F155kFvAz5Cmp1vC1chYH3lxK4ukNbx7YP8qJOQhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حمله تند مصطفی هاشمی‌طبا رئیس اسبق فدراسیون فوتبال به علیرضا فغانی عزیز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106568" target="_blank">📅 15:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d6b37a2c.mp4?token=bO6-Es7wbmqINC8srGpTmG-wK5uDmdQlLKQPXQMpBpbBssicHiR_f5SRij2NvWlZDhXZX_ECZF_WXqWejS4TFGxz7bjnNLftJLpcrU-bMD3zAqReVlJl7h8cnj5iGPRKtfZEeONlbcry6BpJqZ0DRv5YV5K4HmvgYXdh8nqli45_81FfSHHl3AlLRTCc11zYBjwh_KaCkoWyjSZ-E5_kcTAmv2NRrmQ1OZpKNqpqvlHlUi5nmruvRSpKUjQy-Jw96YB2CPzv0wK3Sm4jl9K3DsmuMA0Xz9Rp4ORK-1Cn6UkIw36nClxJgqifGHHZa9kewKJ4UXtxhXtfyh9c-KEpyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d6b37a2c.mp4?token=bO6-Es7wbmqINC8srGpTmG-wK5uDmdQlLKQPXQMpBpbBssicHiR_f5SRij2NvWlZDhXZX_ECZF_WXqWejS4TFGxz7bjnNLftJLpcrU-bMD3zAqReVlJl7h8cnj5iGPRKtfZEeONlbcry6BpJqZ0DRv5YV5K4HmvgYXdh8nqli45_81FfSHHl3AlLRTCc11zYBjwh_KaCkoWyjSZ-E5_kcTAmv2NRrmQ1OZpKNqpqvlHlUi5nmruvRSpKUjQy-Jw96YB2CPzv0wK3Sm4jl9K3DsmuMA0Xz9Rp4ORK-1Cn6UkIw36nClxJgqifGHHZa9kewKJ4UXtxhXtfyh9c-KEpyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کل کل خبرنگاران استقلالی و پرسپولیسی در نشست خبری امروز سخنگوی دولت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106567" target="_blank">📅 14:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdGcMHYoGfPNCB8R_36ShF94sg7zivmrT4pL0iLj6SCRAakqMHeCgg98CRr6C1ovdL-IBLwShNgg9r214_ZR1Azs9Vz6en-NchGSE2i7SA-cgd-6OP1E_Rng1jK4bcn2AduPQHtVORISGPe2_k7ss9Um0ToGrdgt7LpEBY0GS9IbxN4Yn0t8UQaOGz8JqxzV0RM_tmL1Qkmh77VJk0wDscXN9zb0AqUUmANJPkAAp8S7wVzUDw7klntvlDU32fTtQWMypG0ZjCuVkEF0uogvPy4UsP3VYZaSeIVfJMzUzSnhEtMkYtjbZR5xilS_5OoMbVr6L3EThflK7hyQDGDq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
هانسی‌فلیک: مطمئن‌باشید تا سه سال دیگر حتما حداقل یک‌بار قهرمان اروپا خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106566" target="_blank">📅 14:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaKmMNiMmNJDQg-lzBjUnwz5H03k2SId5LPegueRHpXM5tacc0qbvL0xier2x81sqNrOwuc9bK0-7JBfYTQK4OABq_indNK9rgqQkr9vWzFLVGNY_SSTS7XHo7re5bzGgnqgX-9jYpQg8RQWQMvUwwzz0heiDWnMszwOvgTOXVKgCbNaIA26XV3yno_DRmzd-m4jq-XGkuasFbHUIi-pQO_PpUkBjQjyIiEomqqCo9gjCeyjqPcfxrXXkuHr7xo9RlBQubM9DzhJHV5PZVIjs6od91ADeD886OlciPuFesRoajubxIEv1EqMowR6blM0D8kWBqqXUz7jG9dsOX--yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهار نظر عجیب و معرکه از پیمان حدادی مدیرعامل پرسپولیس: چرا استقلال سه بازیکن تیم خود را به اردوی امید نفرستاد که امشب دو نفر از آنها گلزنی کنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106565" target="_blank">📅 14:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py4SojlfAfQfV-Mc5R2AppQIiYDC_cdv8YnnLsjOiVb3I9h60WO3tCuMz9O7A4hqS2Jfqg8awD9AcGw0zNGHsyYPDoRIlxBlVxgjR_jACGgF-qDCjpuzeRRUCjaSMR4oCfQ9O3C7J6EPYtB-QSZ-c7iEP6NwXqvT68AB0Ldq9s0qzu4xf6D3UzcuQpq5ThcVXaeETK7hasNpsagpcp0hsw41fIBKICPy1PkQEwwJYxWTHHCdBYP_8v4uKeluFD6l_ns2szYi6lgyRlx4u80TU9i2tPqi8OiLvDS6OBXB7awHiVbd82yNeoAhx7QxH_bJRqTp-Mi8SYnRR6f02P6rKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تا ساعاتی دیگر میزبان فینال لیگ قهرمانان اروپا در سال ۲۰۲۹ اعلام خواهد شد. نیوکمپ گزینه اصلی میزبانی از این فیناله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106564" target="_blank">📅 14:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1f3faef6.mp4?token=oguduUb27TBSaK7t5-ljZFn2FnG4fBjmS9bv8Gi8q2OSGy0KBhXKeIzAGVBqrtmi01otlTlYZRNjEnx4mpxRptnx3cB9NqqS5VPSE8ORvQrGEPRlodPabLL0x3rBpPHRoyUkIfK1IoK1mZW1Uq3w_Ar21V-_bHRFMLd6_MUEAaCmfNhK_TcPIFp-zueqCCyDtQYTUdJvVaeKZhM5K47zBX7zyxf-fF8dZwizJUIrRwzW1cTbxKMC1bF61_YiRlBKcVRqSL15-4R8yfHxztgQ3pgh7maGVC5MiGuMfXsycVRYDTFHWsDFv57f5idHjSTxo55FtrbJHlhItdVdI9RHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1f3faef6.mp4?token=oguduUb27TBSaK7t5-ljZFn2FnG4fBjmS9bv8Gi8q2OSGy0KBhXKeIzAGVBqrtmi01otlTlYZRNjEnx4mpxRptnx3cB9NqqS5VPSE8ORvQrGEPRlodPabLL0x3rBpPHRoyUkIfK1IoK1mZW1Uq3w_Ar21V-_bHRFMLd6_MUEAaCmfNhK_TcPIFp-zueqCCyDtQYTUdJvVaeKZhM5K47zBX7zyxf-fF8dZwizJUIrRwzW1cTbxKMC1bF61_YiRlBKcVRqSL15-4R8yfHxztgQ3pgh7maGVC5MiGuMfXsycVRYDTFHWsDFv57f5idHjSTxo55FtrbJHlhItdVdI9RHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حمله تند و‌ عجیب یک آخوند در صداوسیما به صحبت‌های لاله‌مرزبان در حمایت از مردم مظلوم ایران در جشنواره ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106563" target="_blank">📅 14:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589bf63655.mp4?token=bf96zCcLWUT-r3tsWz5eEGqZTSKFcoGHlQfOztJC1HnBUmfQcjQq69tKbTAOaIv5xX1RnhPAEJjfFtJWynQYkPOHdtwLOqQCVzuVgmjnjvzFM9NUO3AHANrqqwMcwi1e91KdBsNJawY4jtm1VScXjiKHWwr03Qair3ixllqY4t-Jl-pk4u_Y71atOx6zayPlG1Ps_1PDHqz1wQbXkwoYSEcllQ6iEGX4zIOgIcnxsgR3g00mPv_F6acJkEu5ho4KOT0Y1m_uWaohrW3UQ6AGbocxhM8BZyZGOjYb7aMiUVXFy3Xhn2lojrD79H3u5AQF8GP9PL5qzeYqzr1vxaudPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589bf63655.mp4?token=bf96zCcLWUT-r3tsWz5eEGqZTSKFcoGHlQfOztJC1HnBUmfQcjQq69tKbTAOaIv5xX1RnhPAEJjfFtJWynQYkPOHdtwLOqQCVzuVgmjnjvzFM9NUO3AHANrqqwMcwi1e91KdBsNJawY4jtm1VScXjiKHWwr03Qair3ixllqY4t-Jl-pk4u_Y71atOx6zayPlG1Ps_1PDHqz1wQbXkwoYSEcllQ6iEGX4zIOgIcnxsgR3g00mPv_F6acJkEu5ho4KOT0Y1m_uWaohrW3UQ6AGbocxhM8BZyZGOjYb7aMiUVXFy3Xhn2lojrD79H3u5AQF8GP9PL5qzeYqzr1vxaudPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🎙
رضا شاهرودی بازیکن سابق پرسپولیس: نعیمه نظام‌دوست گفت هروقت احمدرضا اومد پیشت، بهم زنگ بزنید تا بیام چون خیلی دوسش دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106562" target="_blank">📅 13:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a994c05864.mp4?token=VEfIWbwSq7iiwgdfxA1vG1ZvkXGu6LYEt6_Q7Uqfh_JNYRGWlDFLlz1ok_Ylqt8VNxnHRr70-qOpU5X7b_YXsSM9HVwYUEXanEblL-f_TIZq8icOLZ8E923yzI_vBU0E5v2Evw2ShgvGBqZpdQueQFESNVSx8eyEkMcRbfn3WVS9foEIuqy5LsbvylfyvHPLepdivyStwroBV9IoYU6xOB4BLErK6STnWr5MUrB58zSta0CSU2o-jkbGaT-kjBefwAmPKmpFDsaUpYhnMd6N-5JpiEW1_ZkJbBr15a8e1jGuTHww-vgszKuYrI4aRzzrh4B82fDdolRvwc8yJsV7Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a994c05864.mp4?token=VEfIWbwSq7iiwgdfxA1vG1ZvkXGu6LYEt6_Q7Uqfh_JNYRGWlDFLlz1ok_Ylqt8VNxnHRr70-qOpU5X7b_YXsSM9HVwYUEXanEblL-f_TIZq8icOLZ8E923yzI_vBU0E5v2Evw2ShgvGBqZpdQueQFESNVSx8eyEkMcRbfn3WVS9foEIuqy5LsbvylfyvHPLepdivyStwroBV9IoYU6xOB4BLErK6STnWr5MUrB58zSta0CSU2o-jkbGaT-kjBefwAmPKmpFDsaUpYhnMd6N-5JpiEW1_ZkJbBr15a8e1jGuTHww-vgszKuYrI4aRzzrh4B82fDdolRvwc8yJsV7Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇶🇦
توصیه جالب صالح حردانی به نیمکت استقلال بعد از درگیری با بازیکنان السد برای سنگین کردن جو علیه حریف قطری: همه بریزید داخل زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106561" target="_blank">📅 13:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe5inIDUH4ofwJSMZzGbTqsT2DFZjJZSgWQILLPkbY7FKyN0fTRuZ6xyrCxkJgddhYp73d-ZPItul2xqtTdgAw6dsJHiQ1vkrsR16dlxvWPxf25gD23ddxoiIFdAowSBl6NyFzTQOkJX66r0TYQsDSkIDLGy23uPFSNGmYbs5maHdXLz5IxLbQpSe293zf2niADrBgqUItrUvbyxeEDWlzq8dAiwKYgrBscoSAHjluBa-lBYXnlRbtWaYrSfPMyJRvAc_ECUOCjT7VAw-t4adVDWkMgurXAuKOv8qYGYcwa2pEPXmScmHF61souTrPTBUeSaTmEmOcnrUWNWDZL_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
آنتونی گوردون:
من با این باور اومدم بارسلونا که می‌تونیم تمام بازی‌ها رو ببریم، ولی خودمم فکر نمی‌کردم قرار باشه همه بازی‌ها رو با ۵ گل ببریم. ​الان واقعاً هیچ‌کس نمی‌تونه جلوی گل زدن ما رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106560" target="_blank">📅 12:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKK9rM40etGjIc6rEzheY5gFFn4wOZodRalIM_bxgJ1KUdqphetTWMuwjr_9Sgt1phXb5fbiKBs_XCptuYctjgMzB3wRJOmjKjrVUhXYm5HPVJbnIFUUeoqHIN194x7CFvsiMeRUxDYE7DLKzuTAlEY0xrpi8nHcvTVcbGdMFt-xPOTDMaVbijPgrHCDzkwnpR3j6FA_7bTmOTXbPs88ssMjGD-u6ECx9qTki7Zyc2HJvl79efguzjbz5rPDJn8VDaExoDBpvHvgvr2XVJgFYRzF0HGq-9NOiF8SGiQ0X03SLNKvysN4ds3drlH-CNShIlAZ5eErBTuSqyFr3k37UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
برنامه‌مرحله گروهی گل‌گهر در لیگ‌قهرمانان آسیا ۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106559" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106558" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106558" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhC-_JCzCX7lQT8wKDxEE7i4uf1zxTXcBk51vUCNRxTh-6fq6FmReV5FihbaXTLBepauR2JfTQj1JGZl4joyGMOjlHh-AB2S8X8vx4N-ZXKJPgHYHrhQ91gXr57K0d54TEVsoAK6POmX8QdAxGtzJLSl_1yTtydKi9hYZtSgwSqM7um1n1kn7VEYPdIu1UepL3PqI4tFINYOUKYACZSx3T-bdKvcMXfd89Dgve3T-UilZifemZ7WqedMDd29RB0WaR6Wi7CACA96OC40Adm3-JES5aAmHbMOCCa5RTiPPJQeoYHjuBJodSUMzWJc4N6T14Nca8agIbfBLJ76bpQWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106557" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851e159f48.mp4?token=S5t00ue30oOqbbG4FqA9enQALW40OQoOiLZNrEY_ToQhF-aqpaiQ-qTtbiIYusxFaA3pButrQnqh7oU32_ZHToz1kGlbYghLyKyn2lzcP0Zv3cSHXcdABb9Jry5pKwh-0zrHGEiu8J0sfBb45EOnxVzLwW4BDQsJerU49cSvVgGCOJOxYyZ-jk-5HHV0zkrYWcLf39J6Sm4FzYrI3qvPmeEeZHGJMTIlSdZu8XXpl75WqINs5vFPz-sDbpT75fS5rymUUepMntW-HdPmJAWVVnoQLkkiWHhw-Pw3aJA8IDoovM6ki3EcTytH3sJ-qRfRsoqBe2QRU9VoJ0n8E3-yRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851e159f48.mp4?token=S5t00ue30oOqbbG4FqA9enQALW40OQoOiLZNrEY_ToQhF-aqpaiQ-qTtbiIYusxFaA3pButrQnqh7oU32_ZHToz1kGlbYghLyKyn2lzcP0Zv3cSHXcdABb9Jry5pKwh-0zrHGEiu8J0sfBb45EOnxVzLwW4BDQsJerU49cSvVgGCOJOxYyZ-jk-5HHV0zkrYWcLf39J6Sm4FzYrI3qvPmeEeZHGJMTIlSdZu8XXpl75WqINs5vFPz-sDbpT75fS5rymUUepMntW-HdPmJAWVVnoQLkkiWHhw-Pw3aJA8IDoovM6ki3EcTytH3sJ-qRfRsoqBe2QRU9VoJ0n8E3-yRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حواشی فوق‌العاده زشت لیگ‌نوجوانان گیلان و کتک‌زدن داور مسابقه مقابل چشم دخترش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106556" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
‼️
🇮🇷
ادعای رسانه‌های عراقی: استانداری بصره تمامی هزینه‌های مربوط به میزبانی استقلال در بازی دیشب مقابل السد را پرداخت کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106555" target="_blank">📅 12:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1348b5a435.mp4?token=kDQz0b1jVZ4a85pVT4HguQmhdH_M1E9MGByp-h68iO4Uz2GL5KEnvmxAuCcftE6-SgkZVsrNNTeaLJOff8BsQj4LeSDeUqesmdM0Yc11_9kNMC1jIVPlFxrutWnP1cfx_pf1epf6ohQtGl89MKolC5dOArQNDphY80pz6rS2rr_TaaHetitJWPvI1VrP9rMEZFp6CeEbemQXgB9JLUSlV56Anra89C50KggyVGuytd_yreS_OfbLC-rhlvIVG_yEER4hgwyA2n3RY3l-Zt9AjEH81gsFpsL0QdE9VqFLyGMN8SmD8zQiZsnPXqrK3ThKLVanx2meij9M-T-odHa-jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1348b5a435.mp4?token=kDQz0b1jVZ4a85pVT4HguQmhdH_M1E9MGByp-h68iO4Uz2GL5KEnvmxAuCcftE6-SgkZVsrNNTeaLJOff8BsQj4LeSDeUqesmdM0Yc11_9kNMC1jIVPlFxrutWnP1cfx_pf1epf6ohQtGl89MKolC5dOArQNDphY80pz6rS2rr_TaaHetitJWPvI1VrP9rMEZFp6CeEbemQXgB9JLUSlV56Anra89C50KggyVGuytd_yreS_OfbLC-rhlvIVG_yEER4hgwyA2n3RY3l-Zt9AjEH81gsFpsL0QdE9VqFLyGMN8SmD8zQiZsnPXqrK3ThKLVanx2meij9M-T-odHa-jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیرقلعه‌نویی سرمربی فداکار تیم‌ملی تا پایان جام ملت‌های آسیا ماهانه ۱۵ میلیارد دستمزد می‌گیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106554" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106553">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVDT5X4KDn3GYFTFquZFPGzWVC7voiastGlgjrLHtj-r_vbeRDfVttrVg2NII5EI_QT3ry-98jAndPISqPCoZXU7BS0e58XtXdjZzYpgoMkaLEaEl4iYZeSMmO8IGQPm-BnnlTdbBDrgorq3yfnxSbZw9fr8x-w-xjz3rEGP2AhDV8EGxiDfCjDAnWAtPbFkih2o_wV77sxik0eoe4KgKp59Dp-_PTf9l2bHPHcv-FrA_jhqehNvcvWt6lca-dCiXyBOOQqzS7tFVBccGODYmMqGlWWsu6WkLgxhgSHse8ZFNjck6Um-UvinZW2S5ePucfECL64xpZmk9dS_REm7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
‼️
مقایسه آمار چهار مدعی اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106553" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106552">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d711d850a.mp4?token=KZPAjU39U5lrW1HqTsrNOS-93UHx57myrKSlh3MGD4OI3gNuS6XacEv7Jfoam-7J4-aHhr4XLrDSqDlOxaWy9XeaDo9uRk3CrMNQl-BZsXjYvag49vUgh2URIUhNVjG87T-U59WjAQ2lAqAlYxrJUDvmO14GtcooFdE3feQKg_JN3jdrgQ9ufQims19MZtjlsTXvGlYO6wr1GSE0ojqn_mHKo-N293WFG0NiZ5WcISZWA4kvhpVfNktOe4PtG5yaQo3r0N6XC1Lfso3u3mzMrzQSSSuRrdzJ0m-XzP_VzqP_EP-59Ena-tsHs32BQFWmP3CZiHyCWbcWHFErCd6I8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d711d850a.mp4?token=KZPAjU39U5lrW1HqTsrNOS-93UHx57myrKSlh3MGD4OI3gNuS6XacEv7Jfoam-7J4-aHhr4XLrDSqDlOxaWy9XeaDo9uRk3CrMNQl-BZsXjYvag49vUgh2URIUhNVjG87T-U59WjAQ2lAqAlYxrJUDvmO14GtcooFdE3feQKg_JN3jdrgQ9ufQims19MZtjlsTXvGlYO6wr1GSE0ojqn_mHKo-N293WFG0NiZ5WcISZWA4kvhpVfNktOe4PtG5yaQo3r0N6XC1Lfso3u3mzMrzQSSSuRrdzJ0m-XzP_VzqP_EP-59Ena-tsHs32BQFWmP3CZiHyCWbcWHFErCd6I8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سکانس جنجالی مرد سه‌هزارچهره در کنایه به فساد بی اندازه مسئولین مملکت جمهوری اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106552" target="_blank">📅 11:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106551">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46287e0aa8.mp4?token=CZ1nlAJUnKLoiohYy9NE-9aCMPo7IpEI73fqYp6FAPFypXlBE6S8dH75ksFpD-Jr3JFTU-14IXanNGEP2MtDWzXIfM2yawZq-3EcXFzNZmAKgdIBHqmi9ZmF1_dINgzSf7sZQPBQIGcoyTp5EY1CuGSAAZa8heZHdcbyrq7mAaaZrVTlxfvvmKfCJCJI5AVpkjfGtMljR29OQfw9PVslWXYGnMYA2p4OoDILIH88t-QZgpN46fyg2PlDQHZC3njAJSBx2LXroGzLl5czw4_rJZFKwjVQFgwSYKjfHnpVgTysQ08CTgxjYzpvhzBQzLZWUqdQYtKxhILz97IwNgsEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46287e0aa8.mp4?token=CZ1nlAJUnKLoiohYy9NE-9aCMPo7IpEI73fqYp6FAPFypXlBE6S8dH75ksFpD-Jr3JFTU-14IXanNGEP2MtDWzXIfM2yawZq-3EcXFzNZmAKgdIBHqmi9ZmF1_dINgzSf7sZQPBQIGcoyTp5EY1CuGSAAZa8heZHdcbyrq7mAaaZrVTlxfvvmKfCJCJI5AVpkjfGtMljR29OQfw9PVslWXYGnMYA2p4OoDILIH88t-QZgpN46fyg2PlDQHZC3njAJSBx2LXroGzLl5czw4_rJZFKwjVQFgwSYKjfHnpVgTysQ08CTgxjYzpvhzBQzLZWUqdQYtKxhILz97IwNgsEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
تعریف و تمجید میثاقی از امیرمحمد رزاقی‌نیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106551" target="_blank">📅 10:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106550">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c06af095.mp4?token=GUtGImjkVVpBXf7PdOYW3fn-5YUFXjNPuXFGwlNVrUgyfabh1926YTR0dF5U8xio1SDCyiGuBYruz2e0yxs-RMbs_WvVrPl6uM6902q_UKJFDdlKnXoy7Ipsxi6pnrcCs7ImKQDa-bf40OLcochXR6MeUUjBB5drkPwXeuGeyKufJqqFvmO1djwmtt-XnrOPTYtTsNTyUoKWP6itn72HvHSClFwQgYtPonPR8SEuDMF-sS_vO0EteD5KzCDSButMOZ6QlHItfZg3RUxOsf-oEMSHG2OdvDRtpNCsb9c2LnS7Q4Xp0zjFo4iiU-d_BSURyq_qy8C778aMxdWn_CFIYWqCk86T1neKkYZ0--bBYiUedEJiDhmOHQHmWd5xVL2m3xTdMkhQ1vswkvILN3Pzlwj1k3IU0xaUmOlsWhV29Lll-hBLKqNRjl8oTYQPFLxDospK9Ta6uVD_H4_zQ6dmaG5ZnNu34Cyu1-IGmydzOnaywn5bLIrt1DEenF2_m1mr7g9Bp6Uoof-bznYKzOGeDvB0pgQ_jOuxQypLkYbk_rksMw-fI3-zKit0R10mbGr2Jc_bb42gYPTfgTLO8SzWH5Ci-l0GiYbGmv6auVFrLS1O2hLy4CaZrrjLha_enjlriKl8cygFSCTawoq2TWDmm5Z1uV64uBGeIIqJ7urpbt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c06af095.mp4?token=GUtGImjkVVpBXf7PdOYW3fn-5YUFXjNPuXFGwlNVrUgyfabh1926YTR0dF5U8xio1SDCyiGuBYruz2e0yxs-RMbs_WvVrPl6uM6902q_UKJFDdlKnXoy7Ipsxi6pnrcCs7ImKQDa-bf40OLcochXR6MeUUjBB5drkPwXeuGeyKufJqqFvmO1djwmtt-XnrOPTYtTsNTyUoKWP6itn72HvHSClFwQgYtPonPR8SEuDMF-sS_vO0EteD5KzCDSButMOZ6QlHItfZg3RUxOsf-oEMSHG2OdvDRtpNCsb9c2LnS7Q4Xp0zjFo4iiU-d_BSURyq_qy8C778aMxdWn_CFIYWqCk86T1neKkYZ0--bBYiUedEJiDhmOHQHmWd5xVL2m3xTdMkhQ1vswkvILN3Pzlwj1k3IU0xaUmOlsWhV29Lll-hBLKqNRjl8oTYQPFLxDospK9Ta6uVD_H4_zQ6dmaG5ZnNu34Cyu1-IGmydzOnaywn5bLIrt1DEenF2_m1mr7g9Bp6Uoof-bznYKzOGeDvB0pgQ_jOuxQypLkYbk_rksMw-fI3-zKit0R10mbGr2Jc_bb42gYPTfgTLO8SzWH5Ci-l0GiYbGmv6auVFrLS1O2hLy4CaZrrjLha_enjlriKl8cygFSCTawoq2TWDmm5Z1uV64uBGeIIqJ7urpbt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وضعیت سربازی بیرو: واکسن اعزام به خدمت را زده اما درخواست تعویق پزشکی یک‌ماهه داده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106550" target="_blank">📅 10:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106549">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9668387e.mp4?token=iK16T_7ngfuQbrVZNQ8S4msrpjqAXyYCBqchxjFzy7GV8nGSRH0oMOE9SH1TYhtzDsc00Ku7di7v6UOllpleb_Tu5rUDzYMK-4EtPiLf4SkcA_I1hTzfI2xV3QBiblQJYpyOnma8k6rSyylAoWI9fOcNNzR8z1nKDaioINeWq2ItLtXvll14Ze2kg1cfB-mEKXwjLtGt4wLdwx2MyP7gHI4YqJD_MVGKERN6SmEDDFOaFSVsyCjME_yqhJzVRFUir_-4syuqE2HXJGLX0hcQoCJKbv1EBd2iV_v8wgd_7Xg_Mji0OS7i08wRwCImRsjszNYx-65Bu7DukjkKRM5-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9668387e.mp4?token=iK16T_7ngfuQbrVZNQ8S4msrpjqAXyYCBqchxjFzy7GV8nGSRH0oMOE9SH1TYhtzDsc00Ku7di7v6UOllpleb_Tu5rUDzYMK-4EtPiLf4SkcA_I1hTzfI2xV3QBiblQJYpyOnma8k6rSyylAoWI9fOcNNzR8z1nKDaioINeWq2ItLtXvll14Ze2kg1cfB-mEKXwjLtGt4wLdwx2MyP7gHI4YqJD_MVGKERN6SmEDDFOaFSVsyCjME_yqhJzVRFUir_-4syuqE2HXJGLX0hcQoCJKbv1EBd2iV_v8wgd_7Xg_Mji0OS7i08wRwCImRsjszNYx-65Bu7DukjkKRM5-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
آیسان‌اسلامی: هانی‌رامبد بخاطر مسائل ایدئولوژیکی از هادی‌چوپان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106549" target="_blank">📅 09:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqHkKhZtSndrU-aiU8SSow2esqinr0OOI1o-KcAshnl-vOeZeu3jOZDizP70qZhb8Uo6qVSN5m1jbLDELVPpN9F8_JB0vTLKuZiSbYOJ3auGHAd6okuM0iu6Hz7BBmsSzuyL8YEo932dBUprjs1PQBz0EoQrTNNb1CIggL8BNfQSGW-N_5TjghgSxi3l38WPvUXhgoKxNJF4TALseasqECbPrpmHQX2EKb_CuZE0DkXQkcq9Gk1BTxuXQqNrHnPe5e5x12y6DFY9F5twZFxR6xBqGMO60iTXjPeLD9Pw1UvS_weu2J_4ZNsQkfSr8HXV-qGDtjn85i4DfP08EiRD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🟣
عملکرد فوق‌العاده یاسر‌آسانی در تاریخ مسابقات لیگ‌نخبگان آسیا که تنها ۳ گل تا بهترین گلزن تاریخ آسیا فاصله داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106548" target="_blank">📅 09:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106547">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKedEFxFYCUjgHIHY92eBSOWGBnqwNiHJJoqWuG0TR3HVdULfwt1JuH2JOF3sFhVWKs1bV7Dk70t9KJgUd8KeNIlqlNXxK9UPpHpie4ytgRI434JTLHcd1nGIzfemiiDSwjAoQgY9zNOsL8z64pQlO9rpDLX-xy48y06r3soR97WDcqoqUMM0kPtkT8wJPbsoJwV6oeWK6Q5Orwok9gN6Xp7aCyW8A_pQRVbWw6uZ72nkz8b0fhwLxDCs_8hP78ZKLFQ1hw4NwvJ4sCG8NfqVjfVpXtb9JFaRWPYGH990b1Mplt6KKnGK42wnUYBTXGiX6N2k-tRQdRyMmykP_aACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
‼️
مارکا|باشگاه‌بارسلونا قصد داره یک‌کمپین تبلیغاتی فوق‌العاده سنگین در حمایت از لامین‌یامال برای کسب عنوان توپ‌طلا آغاز کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106547" target="_blank">📅 09:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106546">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6843e64d1e.mp4?token=p1M7NRLLCyXub0bJpiEnDtU9kNKN5MHYhc-MAy6t79ov6HHNbR-31JZcx1qsRvjNYIp5dj5xXtJOLlkYvUWI3NpGtQRCGHPvARLsZeb2v6KGYbiWHACBOn-X0QUvfUJDvqmCn3Z7iGqeiuk7cdXO-Yr8YAzp01QNHnz3IFcz9kl-rnRNWscLeb5n8o1hf4k2x3zfcEHriqb5JohYmDl3tPlE3Djjo7L7YSj7hrGS2uokKzKMDtInSkhe_YrGNIbenTjTevCh7kXJWditlWMuJt0pgy9cqCP5-ZLmTjACelnefAtGYzJtN6JkU32JO0MitU33vhuKYvlKRBOP-quiOSuXmqN5EpX1-tha0XFS92NZQiBmNeH2nBSyqN3P7mLIG6tc6r8B-e63raMhYkuAbsOPULB_s0bDr9BoTDz5nozPQImd89ZqScFascIJB7QXBynLwUqD8jnI1ZmCK5TMCp4wggzeNRYQXXyioy0rDhRMQvT3iTE3AGEMPVOnPWEYbBL_zjkM5o1TL-FmiZrroqOrhdRVOHF4CR0RYNdjLIywwlxu6f4nSwURz1u4922kulcxDoRGCrtibAXM_wrXrFXsci5hb99Qv_kD_1G3zIWzSmNSxOCsntNCLMN4bEBoQfsM0mubPaL9ypluEMUwsu84lCQKMH7HofgiiXR6S4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6843e64d1e.mp4?token=p1M7NRLLCyXub0bJpiEnDtU9kNKN5MHYhc-MAy6t79ov6HHNbR-31JZcx1qsRvjNYIp5dj5xXtJOLlkYvUWI3NpGtQRCGHPvARLsZeb2v6KGYbiWHACBOn-X0QUvfUJDvqmCn3Z7iGqeiuk7cdXO-Yr8YAzp01QNHnz3IFcz9kl-rnRNWscLeb5n8o1hf4k2x3zfcEHriqb5JohYmDl3tPlE3Djjo7L7YSj7hrGS2uokKzKMDtInSkhe_YrGNIbenTjTevCh7kXJWditlWMuJt0pgy9cqCP5-ZLmTjACelnefAtGYzJtN6JkU32JO0MitU33vhuKYvlKRBOP-quiOSuXmqN5EpX1-tha0XFS92NZQiBmNeH2nBSyqN3P7mLIG6tc6r8B-e63raMhYkuAbsOPULB_s0bDr9BoTDz5nozPQImd89ZqScFascIJB7QXBynLwUqD8jnI1ZmCK5TMCp4wggzeNRYQXXyioy0rDhRMQvT3iTE3AGEMPVOnPWEYbBL_zjkM5o1TL-FmiZrroqOrhdRVOHF4CR0RYNdjLIywwlxu6f4nSwURz1u4922kulcxDoRGCrtibAXM_wrXrFXsci5hb99Qv_kD_1G3zIWzSmNSxOCsntNCLMN4bEBoQfsM0mubPaL9ypluEMUwsu84lCQKMH7HofgiiXR6S4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
بانوی استقلالی ساعاتی پیش: به فرودگاه آمدم تا جلوی آقا سهراب زانو بزنم و پای او را ببوسم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106546" target="_blank">📅 08:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106545">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHCLwZYsxcpxa4rL41-f8llkI2_nAgCF6XGKztAWLmx5gD6pXuxQTtcCz6gMpicflgq2z2kaPiQH66Ds1uLevwdScynZRkhbsWkkZ8ChL8z6rzlYyoWNaBSvVpON0ARldNi2TvKzmoYKYWkIuXaKEjvTPzSu8w2i3z8S0MhveJI4DhFZzIRATtfqgO2n8ddYJjOq70e2Frl-cgCfmEAFRtDUqztvmrx4ffmswvaqmB5EBpolaJAeQO0U3VKTa0_F3hBo_XODXvRyywLcKd357dGprjlMGGfBVqGPMG6eD4fzMbw6kp8-SnabMFV1QrXFihFVgLuwN_YZLyUYGOK2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تا ساعاتی دیگر میزبان فینال لیگ قهرمانان اروپا در سال ۲۰۲۹ اعلام خواهد شد. نیوکمپ گزینه اصلی میزبانی از این فیناله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/106545" target="_blank">📅 08:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106541">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HptjNHfoQIIUDc7ciqnrab6rNb-CTNSZlyVZ4e3FMiPf-JqiuP9a3MEJ2avqv8cWPcSMI4lMMGSjg8dpPl90ejRK9i0LA_fxgEmeO1EV3RGDqXUzYfZwPkk_usDTsnjHqpkCkEOXZSZh9snzP1dkmYBmeenyQ7HzJA-Fi0EZ2ZmYIRu7NzuSF7URIjfpC772tWk1r3Nj8VVMy1gKFY-_73NDfiAVkmfrnvKgDUZ5W8NUujhltJQvWucarcT1g9xhXKqKrTAHRA2Zix3nepOIIAAl6ZcAXoA_CEqdqIGdrELuSpg04a91lT7CACO_tUARrGvlQqE5H1lyVoQSTJP0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
تمجید لوچسکو سرمربی السد از استقلال
:
🔺
مقابل تیمی قدرتمند و باسابقه قهرمانی در آسیا بازی کردیم که از حضور نفرات هرچند محدودش به نحو احسن استفاده کرد و مطمئنا رقیب آسانی برای سایر تیم‌ها حاضر در جام نخواهند بود. متاسفانه بازی ضعیفی ارائه دادیم و چیزی بیشتر از این برای گفتن ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/106541" target="_blank">📅 01:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b135c8df42.mp4?token=VC8qMBhNbQmLZtHidmWeXsn7M4n_eL5v932D5mKnkZ_KUVQIdcKrlMkmTEnjAoAZ91w_inCWOdmYp98-41tl8vT72mb6xJqo9xi_aJqxY1qcR2THTEnyNGhReVKlo3ndDahx5f7fFHwfLYIzvK2Z5z4lgODN5L5kWRlPRA_yB1Kvtnvj930zfLS81JCIYVejfCq61UNKjYgNJzoQEu4Kn3hjxwOCxmaD3nRNUDiwTxml2wA5BTvkpA5rcBwoSO8cETe9Obw01sMvAgQjtSWc7B9Aav2vkCLcxXn19TjZy9WvOQkYMupZeGkPcEMSYRLJ8RMU3-ISWNsq4mJ8CvEi_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b135c8df42.mp4?token=VC8qMBhNbQmLZtHidmWeXsn7M4n_eL5v932D5mKnkZ_KUVQIdcKrlMkmTEnjAoAZ91w_inCWOdmYp98-41tl8vT72mb6xJqo9xi_aJqxY1qcR2THTEnyNGhReVKlo3ndDahx5f7fFHwfLYIzvK2Z5z4lgODN5L5kWRlPRA_yB1Kvtnvj930zfLS81JCIYVejfCq61UNKjYgNJzoQEu4Kn3hjxwOCxmaD3nRNUDiwTxml2wA5BTvkpA5rcBwoSO8cETe9Obw01sMvAgQjtSWc7B9Aav2vkCLcxXn19TjZy9WvOQkYMupZeGkPcEMSYRLJ8RMU3-ISWNsq4mJ8CvEi_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇶🇦
روحیه‌دادن لوچسکو سرمربی السد به بازیکنان تیمش پس از شکست مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/106540" target="_blank">📅 01:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlTt2tyBqymOcxG2LHdt6MNpuYTIpNjaP0dmpsE6h6qn46oaH80-MB7VJnv5ggVrwcBIpHQLO0txHLxfKL9pL8smhWEO4VA03HO97Pf0-QM184ZYHxfTF1DhmyegRh-JsDElMfIgVoFrvcwP8E0sxVjzyFQihljo0HcN9dTToqpEEp1q-9Gjw-s36xOQQC4p7Ger6oGhzcmwiKwYCICAb-90ODrSBksBAosGweD7FNi2vUHwKGJQEG4KnEUkRQ9YqFshTWZRDqOe4Cqgqs1vBEsJtUZvgZCkxCJFbNdVy6uT2BuRaC3Cvi8RnG2wx8Ip-D0IhDs8Lsa1h1NIAqjWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
پست جدید یاسر‌آسانی ستاره استقلال: این فقط شروع کار است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/106539" target="_blank">📅 00:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1214641e23.mp4?token=ZmjwpLGCDutk4uom1E0-zshFAljD3knt0sKBFunfyI5HKxdTFsRSQpUbcetLaW8b8l4Hgvg1l0tAm5iMde5eYZ1FyulNke4eNvPSMl510ompT2gy11X8A8dBcI-RbVRJVOqYvf7Uu51CjEnoDM5HU5s0L0T0K0GCXoXQgAtzvl9G_JmTz-9ePmEY8QtDCnthJV7TaUcW1sHE0rhuB9wWi639KDEYFYgNt2vMsu86V55jTqRG5SsVm7Z1Zb3Cm0DIx6NTXAyk4T88mqJqNcSkeX2La9NOR45U9t6jQHvlWcfa05x9qYv_ir7x16LPzBs5AcENwI2N6qtyLqWduSxWuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1214641e23.mp4?token=ZmjwpLGCDutk4uom1E0-zshFAljD3knt0sKBFunfyI5HKxdTFsRSQpUbcetLaW8b8l4Hgvg1l0tAm5iMde5eYZ1FyulNke4eNvPSMl510ompT2gy11X8A8dBcI-RbVRJVOqYvf7Uu51CjEnoDM5HU5s0L0T0K0GCXoXQgAtzvl9G_JmTz-9ePmEY8QtDCnthJV7TaUcW1sHE0rhuB9wWi639KDEYFYgNt2vMsu86V55jTqRG5SsVm7Z1Zb3Cm0DIx6NTXAyk4T88mqJqNcSkeX2La9NOR45U9t6jQHvlWcfa05x9qYv_ir7x16LPzBs5AcENwI2N6qtyLqWduSxWuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇶🇦
میثاقی: بازی مقابل آسانی آسان نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/106538" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArvtPaXvLCPN_RBjEi_gdxQ6rlTLlXSA_3AQzjGmQYIarj1ariR_NwInmr_MRMs2l8UXXsayJCILPcwwSO4uMiZkyoqNDRH1cjxyQ4_yJgXOoYlMHraYE1QxwdpUCJxONwG5zG8DSLV93TRZuzjN3Jsrc7J25WCBfU_o2vOf-dujnsk1EY1pc_4iUaErWD9tpEoHcOZZkA1LKQhE1r2keFVwruD-JNSnF-OVFwYUvnJ2eLmGr1t4MvNcHBVZbjKWf5SR3kuZpBcVUIPxmtg8NmZsj4PQpPu57wacMDjudOdI4Pq699vXXMlzQaMTeuPUTyjPRrh_VFeAvaxM_hJuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
کنایه عثمان‌دمبله به امباپه: برای بردن توپ‌طلا نیاز به جنجال ندارم. تلاشم را در زمین میکنم و امیدوارم بهترین اتفاق برایم رقم بخورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/106537" target="_blank">📅 00:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
🎙
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری
:
🔺
ضمن خسته نباشید به تیم السد که از بهترین تیم‌های آسیاست، به بازیکنان تبریک و خسته نباشید می‌گویم. بازیکنان استقلال امروز فوق‌العاده‌ بودند. به هواداران پرشور استقلال تبریک می‌گویم. امیدوارم این روند را ادامه دهیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/106536" target="_blank">📅 00:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDwRBgH9lBhspGgJrM_1ndHaoquoc1Hp5Uvvlah2mLTS1W8nL3LyOy6Z6JXW6XFLdWcqdVKW61c5xpUiNUlNXPOnWMnhXzbFyUxgIUGeFXqP30pq9bDjvA0G9jA8IxYx6LgLEBcNkb8UQ78E2ZWZAdvXvs3BkHW7q73WjCd_5ihg0OrZh_mIWpKrYVKbZlDz5Mw-EY0P6ORo0AbxPm6SwaTl0JS7ySbfhUq1mD19DSnehAHdP8-BTUkXkSxUeUFp6fSoFVkRo6ny0G29nZzh7Oz9NZ6C6UvpHoQ8DsUDh3hKkwmfi2nHXQDv-Ap8h3yUeT5kcso4zNx3ciqwjntVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر بالا خوشحالی اکرم عفیف بعد از گلزنی مقابل استقلال در لیگ نخبگان 2024
تصویر پایین بعد از دریافت سه گل از استقلال در لیگ نخبگان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/106535" target="_blank">📅 00:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd294b65c6.mp4?token=F1EAivt35yC59SPODjtouIVEqGxGxD3NvW5iO-v3JnAgZV1nAjF3TpmqFtMO2Gvcf0ll0AFMew2iuUPTfQZ-0OsL53-J__QkJ4SLqBxs3H0GHzRvZ5I2uC011aiWcdy72I_d-wv-5XJiTKYRnrlj94fmybAtCuwzYciyiJPjaHScf7-rJsDUr8xIZiXcLtIYK4Ssfal8m5IQKgCGZC0Ptkk3rWzFH_eSkYY0FyoRq_oGc0O3ny-6o1Dio36gDSMCCcEzvt3jzi5B2nzVSAzRJ0h_u9n6zHJ5am9AMVRYFYJzFqZh5gakrjM-MYTwFf9rXPwu2eLOI7jAaBmiH7sp6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd294b65c6.mp4?token=F1EAivt35yC59SPODjtouIVEqGxGxD3NvW5iO-v3JnAgZV1nAjF3TpmqFtMO2Gvcf0ll0AFMew2iuUPTfQZ-0OsL53-J__QkJ4SLqBxs3H0GHzRvZ5I2uC011aiWcdy72I_d-wv-5XJiTKYRnrlj94fmybAtCuwzYciyiJPjaHScf7-rJsDUr8xIZiXcLtIYK4Ssfal8m5IQKgCGZC0Ptkk3rWzFH_eSkYY0FyoRq_oGc0O3ny-6o1Dio36gDSMCCcEzvt3jzi5B2nzVSAzRJ0h_u9n6zHJ5am9AMVRYFYJzFqZh5gakrjM-MYTwFf9rXPwu2eLOI7jAaBmiH7sp6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
جو فوق‌العاده رختکن استقلال در بصره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/106534" target="_blank">📅 00:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8nIqswHgVdmvuWiYATg-h_0mHEMRbfO9ZoT1KItfUx3GUci_Ud_b2999pxwBqcA8tsq5WjmJ4QHKLYo9EtbgxQ6kietzltmohmkUPDj1ddN7TLlIQVR85-syDLD2lGIzdFQSwVyw1sHUcYka9c6F5sB-SA9lGqvuy5cWQl2jpeqrCkw9b16pP46nHNNIbhLZQGbk_ybnFty6FnHKC3dfZvgZNciS3h6WPdu2Hwvx_fAZru9Pi7vwpqt9rt9iV2WWryA7lvZ0H0mkvkSzr4EEFcuL2KAHIPTKKZYWEgyeLJB5YgYzhe13gQHnpH6FXFgoAIqNfkxBWA_ZvN9M62N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنایه‌آمیز با چاشنی کری‌خوانی میلاد میداووی مربی استقلال برای پرسپولیسی‌ها
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/106533" target="_blank">📅 00:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_FAo5r5Yvccddoquu9c748m2eYhi0W1jbiey2E6sT0tZzJsYv1YUClcplOqvk5YhDDHhB0qBTeoisQmzQrOy8Emwk_g23Wg8J_kow3qGIiv3kksc__DNDPE_zyPB3zReRtRuZZiJD5QBj2me4sXbf0dxOw6ypaVvhVrDOuH8pAHs5Y0BVpcyZnbyVpOm19gwT8OB76Zq0dUnONmUWGhK4kdIx2g0gnQ6STZEnVe9WKCaarYGd__qjWTmu4rlbLUFb5bBY69pyY9DPOVlX_TCalAcv14k8WYkM4OirrKBVdTdzg20AHl2BngXSTg2lanImawWAVAQgkbzIbUJzYIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇶🇦
السد قطر که در تمامی مسابقات این‌فصل خود حداقل سه گل زده بود، مقابل استقلال موفق به ثبت‌‌گلزنی نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/106532" target="_blank">📅 00:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXlLlykCYiuiTctftmoKn9kVpDTPqn8dGhzDeBSB02X78wTYWv95skWp9qTZircstKN88-biXlkBYAJAh67TPyOmWsC-XLsVZLgYisOOHTztagreWX88ddXDf8xzm5oCCSl-Xbwwaog8fy3MEm-rwk65M5N-l_ZRjjtINmcs2iK-X-btTXG2eY_JekC-WER1Pc6yMH6914YJ4NOCxGwP3ni50C0XycsmEEVNOYVGoXRlcvRpKdMWS4FquWphlJIi8XYYvMNmswpri38UR4PU2R5xOMPJR66y5SaX3zirajPjUc6AMEuXLUCx06X8Iyd5aVdS1VeT62bzpvHnwpNMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توییت فوق‌العاده سنگین باشگاه استقلال به پرسپولیس با کنایه به تورنمنت غیرقانونی سه‌جانبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/106531" target="_blank">📅 00:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106530">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKdsABUcuULEOK94u9Dkl2KL1WbR6GtiFeuTpEFMSmd282HMh9IQv1KWyWUzl3kBPS344DjAeUDY932HvDSzM3vEd8uUxMfO_Upf9qEd59S0knnYPzD9NXECqHRtxOZan8cjJALQ6JvnSjK1NaGyNnskfn6EAJft5OtgAKIjRVUWurDbZ_WHATsCph6RF89g0sWnPNeePApj2mzj658pSMj0oinferErd_X-Hy9YQF224IsSrIjuBN8rMJqmdbeOnO82Ye_ENZ_ha9E4a6zgZhmen56KBw7LSefczJ-FM2CGdJZUZCzRYs2hXDbjX66DIf3ZmXkUnN72YH_nwFGqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✔️
صدرنشینی قاطعانه استقلال در پایان روز اول از هفته‌اول لیگ‌نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/106530" target="_blank">📅 00:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/u05Q0R8gX_wfD1xyF2xzWZDGtQ-C2Nbtd2WRQvrV1ctsrXzc6ieSoMtIBtagxKtEuJGSiuzdTc1EMUVZLzcxecjH-mIOHRg2VYWPS3Dwo-Fd-gvvb1PXMexRgU4SIc1BCgLetJMVqmIWr_sSt17D3ze-05yEDPEwGpGjL6oskJvEmwxGtvaN5hXcFslIM2cJlTU_d_ZHSXBysKpGDXa_Ia0ItppaZlU3HJNJmBIOXJ4esx4WrKfTo0nMsrOO7SQErp93HrkEFzUMTDhYBnBChwF1So3p88ev-jaev9o8KqH28l-oeKW4aAXPJjMJVIrGZha-wOBQQNbGL0Z9T7VHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
توییت کنایه‌آمیز باشگاه استقلال بعد از برد قاطعانه و پرگل مقابل السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/106529" target="_blank">📅 23:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGFVakFJa_jUbeHr-DTbLmSeOTUGfZw7Uiw-rbz5crcCLRxRzYwjhBbra8nCU2I0Xdt-7COMPua6RbinQZQZmQhUqfXqvifxEmYML_0nw8HYD4DECotSX1stpEPyJGyH85I_csJjsW4MnyJrjLGwAXZtG5ntpbyTK5QBTs7rvLPO06h6qY_KG4YgxkK6kmyPPUUs1U26BAEGRiW3rurAxXSS-JOshL1SUq8lZ6WkEXu4Msoy19SqeSj6n2M4ddyNT5gZMI6udut4-7gW_Lpk7TOVgdYypEYVL4A7tVbsq4Lydj0QChbaVm3EIlPKdhU8RfnQWldmp5Ba0RmtsJUBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
باشگاه‌السد قطر پس از اعلام غیرقانونی بودن یاسر‌آسانی از سوی هواداران پرسپولیس درحال تکمیل و بررسی مدارک برای شکایت از ستاره استقلال خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/106528" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106527">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqfgf8UvjjG2z4Uu1XGv6MW9XkkWQ3JUHLHjnbLLdd4_wgwmQFSKhuZaA7A4W1BWtdDc5rRNLkYiJpgM19TgN3-naydoR3uUliw-KsmYG6GLe4sN_fSmpyG6pmnn8yVkj6MSNMU-SxOKW9lsNWgxCECVS0gQG_vxr75p2IUYNQrtpxtYmuxHlGr_yEjuKI-RLohtKHhW1_gT-z0q7rkVrgrtv59KIieBF5T_dN-Mc4AU8Iqk0Q3ULyrh58pJssRc0Y4agRYY6SflxWWzNjq0ubbgc548zyz0PaSnCngji-5r0LiXS9QV8RDNG7fK3MXY_vixBsxfaVg6vgB_bGsnMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
هفته‌اول لیگ‌نخبگان آسیا|غلبه تاکتیک‌های سهراب به ریال‌های فراوان قطری؛ استقلال قهرمان ایران در نخستین گام مقابل قهرمان قطر پیروز شد
🇮🇷
استقلال ایران
😆
-
😏
السد قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/106527" target="_blank">📅 23:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106526">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
✔️
▶️
خلاصه بازی جذاب و تماشایی و دیدنی استقلال ایران و السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/106526" target="_blank">📅 23:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8H_PV7Lm5-6kMxaHbUkLqDO1ljW0b_JIMwxC6tgZ2OvMbkNsHpxjCIsN1CHXjsAE7dNoPvPgqcnyxt1_p2H0oPE1mrn63fZ0eatXykLfFhhLaJPqhZAzEJtNy1wdXKeWm3POIlBirFy2S0JRk6CdjsJWS5TCsB7t4XoK9kvvmc0C9BJ1vnzOcFwPsCp56R2zfDO1EhPPT28qqpvAzPyyEycgUTfFUgRbkEhTOUnPz5HxWuGXgF-8JVdRXwHuBMi4B7fdb7f2izW2dJUmndiHMkihcDmco1kRjoS8fJZnr0FcQsbbV-UugIf1JXdG062fhypu0wVjtbJQzEBM-rUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهار نظر عجیب و معرکه از پیمان حدادی مدیرعامل پرسپولیس: چرا استقلال سه بازیکن تیم خود را به اردوی امید نفرستاد که امشب دو نفر از آنها گلزنی کنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/106525" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106524">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهار نظر عجیب و معرکه از پیمان حدادی مدیرعامل پرسپولیس: چرا استقلال سه بازیکن تیم خود را به اردوی امید نفرستاد که امشب دو نفر از آنها گلزنی کنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/106524" target="_blank">📅 23:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKJm7YKP6Q7r2gsNW5LnGSDgKqov2CiGS3C2n0QJYoT1a99Chuq3i8nqSEVIH6F5urvjcNoE7o4RPrHnejunFz2AcChL9o6CM8LHK3YQQhZ0Ax1DJhm2AyWJEmJpbks1vSRudHYeMQuyUgKOUZxx--n00q0IkVnefrf7nPzjlTwcvEDzxibtQNqf1bEW5HpQjv_k-wLloAZYxBRaYyKvirt0Rm_XmQ8qDnEZ95DbgYXb1DHdmcJJKSCsLL3F02MEMwCQWQ7V8BNDvRQnUQ66DgCzHjrnDUaQaYpuAWye1fJ7NwrIFpywahLzlyxEYXpGU1JIcAHjxFivoBhT3ABE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
هفته‌اول لیگ‌نخبگان آسیا|غلبه تاکتیک‌های سهراب به ریال‌های فراوان قطری؛ استقلال قهرمان ایران در نخستین گام مقابل قهرمان قطر پیروز شد
🇮🇷
استقلال ایران
😆
-
😏
السد قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/106523" target="_blank">📅 23:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766e5c50db.mp4?token=EFAklK5c2cehbCuiTYGJWwBiXimitLXcgHOr6_MuH3L3sAKp9D2cHuTCbaP7VphOHldSs7sZczgkSvvkifJ0o1bo-PFYx6NaM-4dueSfpHFD-atI5jr90kck_RLM7k_NAR0ABqz1efhT3fJQJm8f4zePP3VMbnrQfbd7rv6zhmRRPZpMAqic-JAfLWeAVY63UQve0f289lt8zOh8Eqp3WqmOD6nM_DJRKnlOieZ1bwH6s4fJ3e7nNmUuw6G5GE2JjbIwaQEiXlz8SDge_eKTXh0GmyZDkVdmv97j1YBuVUYq233F9BTVzpOhRsu7VST3tIr1Hh_lQ3eBczT1Tm9nZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766e5c50db.mp4?token=EFAklK5c2cehbCuiTYGJWwBiXimitLXcgHOr6_MuH3L3sAKp9D2cHuTCbaP7VphOHldSs7sZczgkSvvkifJ0o1bo-PFYx6NaM-4dueSfpHFD-atI5jr90kck_RLM7k_NAR0ABqz1efhT3fJQJm8f4zePP3VMbnrQfbd7rv6zhmRRPZpMAqic-JAfLWeAVY63UQve0f289lt8zOh8Eqp3WqmOD6nM_DJRKnlOieZ1bwH6s4fJ3e7nNmUuw6G5GE2JjbIwaQEiXlz8SDge_eKTXh0GmyZDkVdmv97j1YBuVUYq233F9BTVzpOhRsu7VST3tIr1Hh_lQ3eBczT1Tm9nZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
پیمان حدادی دقایقی‌پیش: قطعا از یاسر‌آسانی به فیفا و CAS شکایت خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/106522" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106520">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/106520" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسماعیل قلی‌زادههههههههههه
😳
😳
😳
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/106519" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چیکار کرد امشب استقلال
😂
😂
🔥
😳
😳
😳</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/106518" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106517">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پشماممممم از سهراب بختیاری‌زاده
😐
😳</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/106517" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">استقلال زددددددددددد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/106516" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">االلللللههههههه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/106515" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلگلگلگگلگلگلگگلگلگاگل</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/106514" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106513">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/106513" target="_blank">📅 23:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106512">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/106512" target="_blank">📅 23:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">السد از کوووووون آوردددددد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/106511" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106510">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/106510" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106509">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فیرمینو دروازه خالی نزددددد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/106509" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106508">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استقلال از باسنننونن آوردددددد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/106508" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106507">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/106507" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106506">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چه توپی گلرشون گرفت
😐
😐
😐
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/106506" target="_blank">📅 23:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106505">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">السدددد کوووووون آورد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106505" target="_blank">📅 23:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106504">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلگلگگلگالگ نشددددددد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106504" target="_blank">📅 23:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106503">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ماشاریپوف بجای رزاقی‌نیا وارد زمین شد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106503" target="_blank">📅 23:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106502">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حسن‌الهیدوس ۳۶ ساله هنوز برا السد بازی میکنه
😳</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106502" target="_blank">📅 23:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106501">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حردانی امشب بهترین بازیکن استقلال بوده</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/106501" target="_blank">📅 23:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106500">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۱۵ دقیقه تا پایان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106500" target="_blank">📅 23:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106499">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آب درنگ
😆</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/106499" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106498">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صداوسیما حداقل با یه دقیقه تاخیر بازیو نشون ملت میده</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/106498" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106497">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">استقلال کوووووون آورد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/106497" target="_blank">📅 23:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106496">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حردانی میگه اگه دعوا شد کادرفنی بریزه وسط زمین
😂
😐</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/106496" target="_blank">📅 23:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106495">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
گل السد هندددد شددددد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/106495" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106494">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صحنه داره بررسی میشه</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106494" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106493">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">السد زدددددد</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106493" target="_blank">📅 23:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلگگلگلل</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106492" target="_blank">📅 23:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d2b781d1.mp4?token=cagtvFQsU4wA34lLT6UXFmaIGhzJfKMiEfZLBN4B4UxGMycOQWrPSipxpmFH6aQ6SOM0xcm0X6SbS3N2p8hstO8QqR0XyMu9dceQbR-EqiDaYBdyGHHcChSvQIUAwUR1IZU_5FzTNa75uSzyQNF73gkrhxhZ0S2xc40DB3qywHQdqaMEbCZeIwXdhsGzE-sqy-2k0cccCcxI74SfeC1oXHooCxfm_Z_TrWu3aVHpM0olHxz5vy-CLdZPZcg5_IEOHzXgnxIBL9ViTTPoDLIfbYYrdGwAchbaFOkRAJc2JQ7EhcWfmijrvsAZonYGWb54bZTniJASEbS6AEuNDMoCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d2b781d1.mp4?token=cagtvFQsU4wA34lLT6UXFmaIGhzJfKMiEfZLBN4B4UxGMycOQWrPSipxpmFH6aQ6SOM0xcm0X6SbS3N2p8hstO8QqR0XyMu9dceQbR-EqiDaYBdyGHHcChSvQIUAwUR1IZU_5FzTNa75uSzyQNF73gkrhxhZ0S2xc40DB3qywHQdqaMEbCZeIwXdhsGzE-sqy-2k0cccCcxI74SfeC1oXHooCxfm_Z_TrWu3aVHpM0olHxz5vy-CLdZPZcg5_IEOHzXgnxIBL9ViTTPoDLIfbYYrdGwAchbaFOkRAJc2JQ7EhcWfmijrvsAZonYGWb54bZTniJASEbS6AEuNDMoCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔥
گل دوم استقلال به السد توسط سحرخیزان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106491" target="_blank">📅 22:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سوپرپاس گل یاسر‌آسانی
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106490" target="_blank">📅 22:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سعید سحرخیزان
😂
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106489" target="_blank">📅 22:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دومییییییییییییی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106488" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">استقلاللللللللللللل ایرااااااللن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106487" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اااااللللللله الکبررررررررر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106486" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگلگلگگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106485" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106484">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swJoS6xe5CKXNWJQVNv5CQBOviU1XwopunMpOXNuGQkXfs_Cj3dwFFliJmDSggf-PNU-CI4u9-ppArcUHhyQakoQlHu6bWB47IRebh0OuMRz2oZhhV_KtaF-qM0LIdnBWcLOksDmKGzYA40t0iByEdVskqeLQ0ck9gwoKDaWPAktl7LKFdgayqf8G2Nc_3KkKJ2WWg_fhHgWuTejDZnMPf2KUtljuKyWjlaTyW4l16hq3KFe_Bi2mRmO81w7Y82bMi0ohriBMuZ6m4SvCtSRSmhN4qWg7426zJwNRbExZ9blR_y_Cwh0WGpnOOsEZxUPErAlPdkfTezWBTVm1UKOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
آمار نیمه‌اول بازی استقلال و السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106484" target="_blank">📅 22:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106483">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323962117f.mp4?token=eWxDrK0VJHmfXa45sJ4sBCnzG-vpMXS9ni-vsC9vrrGe9LAPQcH2tNsczBfePdgEz8woCPd2ub6-31FLBu7wOWVhrSYfXz37zgqDlwNLIaOwXSb5xr9qjL9jeQxQwEN2zlNkJkgM1Fclr2I7Mp_fEJscoYld9NvAWaK7HmqGNUGXaOL2LLBGuJ84lWHw9hjQZalk0aAjvaQl8_TeMl3YaDczKpuemR1IvwVgXbBK03X65SX-nAl8SUQgAzXfUYDDj2WUO_19rolXI4Iz6-YL-lJ5JwyrQcsH3fgnZozgcg4TcNfoSGP4FLPID3B1cFVVYWr9-3KMhYo2pUPiwDQ6qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323962117f.mp4?token=eWxDrK0VJHmfXa45sJ4sBCnzG-vpMXS9ni-vsC9vrrGe9LAPQcH2tNsczBfePdgEz8woCPd2ub6-31FLBu7wOWVhrSYfXz37zgqDlwNLIaOwXSb5xr9qjL9jeQxQwEN2zlNkJkgM1Fclr2I7Mp_fEJscoYld9NvAWaK7HmqGNUGXaOL2LLBGuJ84lWHw9hjQZalk0aAjvaQl8_TeMl3YaDczKpuemR1IvwVgXbBK03X65SX-nAl8SUQgAzXfUYDDj2WUO_19rolXI4Iz6-YL-lJ5JwyrQcsH3fgnZozgcg4TcNfoSGP4FLPID3B1cFVVYWr9-3KMhYo2pUPiwDQ6qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
درگیری بهروز سلطانی و وحید قلیچ دو پیشکسوت پرسپولیس بر سر علی‌پروین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106483" target="_blank">📅 22:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106480">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76510c3fac.mp4?token=ugHYWThqpgLDcKI6rCwpr1HaMsGCOpDvjXbomRpZu-ghdshUb1daCSI0xUZ984iPmlmCaOHszlSnpEOZ78MYVBw-bCpXu16r7s5dyOtsx2HJJqwU2KDwzUKO1S6sm5L621G7VGsJ6Azq8-r83BbUAIhV8w2yPB_w2l07IfhNoWietm98RPmkSOUD0LD_ANt7vId7aBBZ4hStm-D2BM15lmtn8Kb_wXPW3_16e2fovdwITfBPdwLTXdqV8FTBzNmIbEThovRHMCxD1O5ZaY6Xawdm4EMcut6_E3ii7XiNitgjfQGm7ca_VzqM5-RqNyxlYvSTpRfaxkM6KBL66J3hFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76510c3fac.mp4?token=ugHYWThqpgLDcKI6rCwpr1HaMsGCOpDvjXbomRpZu-ghdshUb1daCSI0xUZ984iPmlmCaOHszlSnpEOZ78MYVBw-bCpXu16r7s5dyOtsx2HJJqwU2KDwzUKO1S6sm5L621G7VGsJ6Azq8-r83BbUAIhV8w2yPB_w2l07IfhNoWietm98RPmkSOUD0LD_ANt7vId7aBBZ4hStm-D2BM15lmtn8Kb_wXPW3_16e2fovdwITfBPdwLTXdqV8FTBzNmIbEThovRHMCxD1O5ZaY6Xawdm4EMcut6_E3ii7XiNitgjfQGm7ca_VzqM5-RqNyxlYvSTpRfaxkM6KBL66J3hFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوت رزاقی‌نیا با واکنش دیدنی گلر السد تبدیل به گل نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106480" target="_blank">📅 22:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106479">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">استقلال چه ضد حمله‌هایی میزنه
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106479" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106478">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106478" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106477">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">استقلال بدشانسسسسسسس</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106477" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106476">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106476" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
