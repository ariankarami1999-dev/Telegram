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
<img src="https://cdn5.telesco.pe/file/LJ5LzHDk-F89vV2ZrM8FrPBTz9I-WH3D28j78MFidbk1xrygZzcTtVO34i5TUqPWhaQY7s1joMUN2X3VEcwzp-aRCMLjhN9r20xsDX-Ilxe7XmxWUSmcXV5XMZXnus4AIBT_nswhmW9ZjijtXULLMzLXVL5sC4RzRGDxVI-aAkqPX8N8x9S3mxF-TuCVTPanZOuBOzQaX4EvFoRI3kHUl0U1iYmBRs0Czo74N2bTAGXsLUqS0q0FcSz_8TmzXQ-WMFqWt1dXEAKD_8Rc7yoOdaVLmvkHSIDrEyrDLs9RehCKnn7VkD1pLI6zMHRkajb83GF6_SeT1GhtnWvHssI9eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 558K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 08:44:01</div>
<hr>

<div class="tg-post" id="msg-100931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65552b958.mp4?token=L4xS1Hq7hNiAPfVCDjuiilabtzCktDKrGnbzccOoCiP2kDcefNy9DmS6UFn2VDcO9yz4JOQvOmBv7daYmQ7i42weMS17W8KU_b-rBsNzmWUAr3C8t6-vpSoQKhxc69ZW8KZaNSwfbakv3mblx7TEwh9GvpdOcTCWuSGZCqHfhYBFTuHZn7ZfUQjsivHZkxwBn97grVLAl6rIVP6p0H3mQn83Yb6guJbArQ85oN_Q-h4wiDH8Q7FLdicmfK4fetlMdr1N2f0PWK6T4RhdqifqWuCMQNgROUmqGyrtxTAa9mvM0hDd92vT3p3aoaNozPJy1B2G6DMGYamlxa5tUb3vJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65552b958.mp4?token=L4xS1Hq7hNiAPfVCDjuiilabtzCktDKrGnbzccOoCiP2kDcefNy9DmS6UFn2VDcO9yz4JOQvOmBv7daYmQ7i42weMS17W8KU_b-rBsNzmWUAr3C8t6-vpSoQKhxc69ZW8KZaNSwfbakv3mblx7TEwh9GvpdOcTCWuSGZCqHfhYBFTuHZn7ZfUQjsivHZkxwBn97grVLAl6rIVP6p0H3mQn83Yb6guJbArQ85oN_Q-h4wiDH8Q7FLdicmfK4fetlMdr1N2f0PWK6T4RhdqifqWuCMQNgROUmqGyrtxTAa9mvM0hDd92vT3p3aoaNozPJy1B2G6DMGYamlxa5tUb3vJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📈
🧠
صحبت‌های زیبای هادی عقیلی درباره جنبه‌های دیگر بازی لئو مسی؛ تعریف متفاوت فوتبال در دنیای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/Futball180TV/100931" target="_blank">📅 08:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZlHjM1Ut_RKEvjOLdoI3qwPNeupuhkHujqqyunTKNq0GAhpM_PK6_k5vSNgDaQD-ukGxzLsu2s6knFlPnbMq9GdvANv2_9fHrVXGT1LD3Cqs48GOYlVwgw0Z6wSPYD99c9610qu4xVydv1JCaKocRIkv8cUr7GRE5G9_1JY4a1RhKo5n6xN9vQ_geXZngorzu0h-66sFK3cjR5MKzlYTMAo2h1AaUf7Yd9lBP6NpqF6z7fGTMokY-zARZq3LUK5s1DPDQxEzslfRNBDNVr-AmhZvOY7EMsP4uR2kyyyAwCuDG4lhxhs0QdN6F8CTD28MQc4AWs2NuBwMMXqipp5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییییی
:
✅
⚽️
خاویر تباس رئیس لیگا، تأکید کرد که بارسلونا اکنون تونسته به قانون ۱/۱ برسه. این یعنی آزادی نقل و انتقالاتی بیشتر برای باشگاه بارسلونا در نقل و انتقالات
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/Futball180TV/100930" target="_blank">📅 08:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802a702ca.mp4?token=lk1Fd0I_hz9uRyhCLVP1dEj6bnX_s1oKBViclmUf2161yY-JoyWSGEVCpGRDmk2Zsc1zW_iQGtWFcgV8fUr7HJgv7gfhL0ytHtuEObu8No5jcMuP7EwDyINOLAdcxpTPYrfAQHrYvyzf5UFs5M7VUKIGaKkF0gGEoMiVUMJMcubzqXklU6aL6keyAANo8L9GCJXBNSHMBq12U11FKPg1fOZO5HWoPKl5vpN8GI_7MbpuMFj_fRPl1GpSFh1SOhhM2sSB5qkN1KCHyeEep9FXEo-Qrv9BBG8aDUkbnKzj0Y3FJtD1bi-rPtx5AtuPhlFrcKiHKEa8FxEmJm25YDXBkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802a702ca.mp4?token=lk1Fd0I_hz9uRyhCLVP1dEj6bnX_s1oKBViclmUf2161yY-JoyWSGEVCpGRDmk2Zsc1zW_iQGtWFcgV8fUr7HJgv7gfhL0ytHtuEObu8No5jcMuP7EwDyINOLAdcxpTPYrfAQHrYvyzf5UFs5M7VUKIGaKkF0gGEoMiVUMJMcubzqXklU6aL6keyAANo8L9GCJXBNSHMBq12U11FKPg1fOZO5HWoPKl5vpN8GI_7MbpuMFj_fRPl1GpSFh1SOhhM2sSB5qkN1KCHyeEep9FXEo-Qrv9BBG8aDUkbnKzj0Y3FJtD1bi-rPtx5AtuPhlFrcKiHKEa8FxEmJm25YDXBkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی پور ایز دت یو؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/100929" target="_blank">📅 07:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
#فوری ؛ زلزله‌ ۵ ریشتری شهر سالند-خوزستان را در عمق ۱۲ کیلومتری زمین لرزاند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/100928" target="_blank">📅 07:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
#فوری
؛ زلزله‌ ۵ ریشتری شهر سالند-خوزستان را در عمق ۱۲ کیلومتری زمین لرزاند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/100927" target="_blank">📅 07:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/472dab2e65.mp4?token=Hs1hYvK5mU42nI0mW8DnHQ4h7Pqk-6g8oHXbL6fkHV7OgTV2RIqcnebjZbOEdP_qsiWhZJfYcEs0As80rvll7NEF6XKmG4SHgRNxThH101FX_RmtrkVHg_SYwHRyGeZCaV4JuzdpIdw9k-wpH91G9lCXUkX80IUhjqepM2aNvndjohnfC_uJxcWj-yTWSqTLEq-OzOJGVoSWmtXzcGGzjcXCSQlIJs-wjHeeyiipiMcoGxeEnGbf0ehiYgfkMf4cbcVedZC-MhpBRH18sFTAxocWhuRb03ngOi_eLCoLY-_diambv_8eYBN9PxG4F-KUIrmQ_RujDOMq9gmOOLQGKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/472dab2e65.mp4?token=Hs1hYvK5mU42nI0mW8DnHQ4h7Pqk-6g8oHXbL6fkHV7OgTV2RIqcnebjZbOEdP_qsiWhZJfYcEs0As80rvll7NEF6XKmG4SHgRNxThH101FX_RmtrkVHg_SYwHRyGeZCaV4JuzdpIdw9k-wpH91G9lCXUkX80IUhjqepM2aNvndjohnfC_uJxcWj-yTWSqTLEq-OzOJGVoSWmtXzcGGzjcXCSQlIJs-wjHeeyiipiMcoGxeEnGbf0ehiYgfkMf4cbcVedZC-MhpBRH18sFTAxocWhuRb03ngOi_eLCoLY-_diambv_8eYBN9PxG4F-KUIrmQ_RujDOMq9gmOOLQGKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
گاهی بزرگ‌ترین ها آن‌هایی نیستند که بیشتر از همه دیده می‌شوند؛ بلکه آن‌هایی هستند که بی‌سروصدا همه‌چیز را برای تیم‌شان فدا می‌کنند.
🔺
انگولو کانته‌‌ی با تواضع با دوندگی بی‌پایان و لبخند همیشگی‌اش به یکی از دوست‌داشتنی‌ترین هافبک‌های تاریخ فوتبال تبدیل شد. او از بولون و کان تا لسترسیتی، چلسی و الاتحاد مسیر پرافتخاری را ساخت و با فرانسه قهرمان جام‌جهانی ۲۰۱۸ شد.
🔺
امشب، آخرین حضور کانته در جام‌جهانی به پایان رسید؛ نه آن‌طور که خودش و هوادارانش آرزو داشتند، اما با همان وقار و جنگندگی همیشگی.
🔺
خداحافظ، کانته؛ فوتبال هنوز هافبک‌های بزرگی خواهد دید، اما بازیکنی شبیه تو، به این زودی‌ها نه..
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100926" target="_blank">📅 05:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd61ad475.mp4?token=LCVUgtR0mFfBYuVtlJohUaVlGTp8jUh6LB63l7Q-W90CU110lM4jno65_A1I3TZdY9hpUcFO-0KXM6pi_sGAs6LeoIXz3TTIxBUa-8LSngzh0VPnpypMOfqioHAARiAiJEko60Im5K8QP8iTtaNZRgZuqFDL1y7f4rJu_dzXVwt7AjFPgzIc1Lkq8fdldbETrzwrmxmTRftNa8VTU-F6MZaR0xe3oEdUgdg3LuTxoWGrDsKTfBQ9UdF3eaNUOWPOkD7n7GOOV5cyqnYJafOFRK5Z3SDxdum9JpsPOVEW7FxI3_skd9TPaf-Tqi8Oh6iKq3wiFT21MIH4ldRn9M9S_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd61ad475.mp4?token=LCVUgtR0mFfBYuVtlJohUaVlGTp8jUh6LB63l7Q-W90CU110lM4jno65_A1I3TZdY9hpUcFO-0KXM6pi_sGAs6LeoIXz3TTIxBUa-8LSngzh0VPnpypMOfqioHAARiAiJEko60Im5K8QP8iTtaNZRgZuqFDL1y7f4rJu_dzXVwt7AjFPgzIc1Lkq8fdldbETrzwrmxmTRftNa8VTU-F6MZaR0xe3oEdUgdg3LuTxoWGrDsKTfBQ9UdF3eaNUOWPOkD7n7GOOV5cyqnYJafOFRK5Z3SDxdum9JpsPOVEW7FxI3_skd9TPaf-Tqi8Oh6iKq3wiFT21MIH4ldRn9M9S_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بین دو نیمه بازی فینال منتظر شکیرایی ولی با این شاهکار روبرو میشی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/100925" target="_blank">📅 05:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YB8JmMfNhcRVger-PDf-ZCg5RYop6TmBCo8dnHgbCL0cmMs6E9G5YwEf3oG2l5OgLlCl1fYhtKKWdomx85mfk25ojHn5ctfnwYovuCRJhdBu74F6bb4PYcGCLMUv6CSKAktEJyJim3iSG5DGL-f8p2Iv3VpmWogp2mqJ6f690En78PifZ6QGC2nb2yU8YJm470BK87o8m0wlaSVt9NB-gPWE06e_BQ3jFMhWcjiJ0WPEl-J8M3tt-bkH1GNzriDcYlQHalni-R_6PNETR9lQ9VX3HWVswW9PdoOKqoi-VMvv5vvEZygWeqmSZhhBot7Xx9H2y1EudADtqKtofIazbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrZpsxrBSSAeb3hoIbqOqnCa9cYJyV5nGjGt-7cgLY8DZHIbcFFt0KRcTUqbcuJl6LlRN2fMIyrE1pCBQNdQ-Z6oTP63N2G49Q9MhBjeVwWMlgjsk-BKkd69ucXvNqfIOfhxJ6MLCpbDFeasdtq0t0nsyHrDOop25oL75xuXztqbIEPEObomRiW71r6gA4n9_zKcDOaT8nEnSAS862pYyDUmD4Z7rZ-GGN0iuXQEoYThzlezYRhXg4dRmNznrn0MZK3tXQoZwOhJlkVIpF4s12kmAOri9CoYw83eXMFvuwXooTvIVdPFaCgY_XhRq_eEOkPAjzLrNSoJAIsVtbK-zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🇫🇷
اگر کیلیان امباپه در جام جهانی 2026 برنده جایزه بهترین گلزن مسابقات شود، به اولین بازیکنی در تاریخ تبدیل خواهد شد که توانسته در یک فصل به افتخارات زیر دست پیدا کند:
•
جایزه بهترین گلزن لیگ اسپانیا
•
جایزه بهترین گلزن لیگ قهرمانان اروپا
• جایزه بهترین گلزن جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100923" target="_blank">📅 04:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8Q_nBgi8rFR2bTMqpugMHGGPBKQ1jOhgxxyGVZEqDfbZFKmv1xTOO1cj9mgk35ydVV3MbJ1ei0dLQEOaGIh68D737oeNE4srOaEYiMfASJ2LpssyKe5oiHeq54bQgy4Xb7c5xsh9sDS5QdP2nqybCE6E7WqyDYhhQkHFl6yNE4ti0ujkD6veSyoffQ69-xkTo8uFzHoAknguH2ZhzYCIDjayHo_0cbPfCkOWrZYCgno1-Km47nuyB9RcgfSfsSfifi1fENQ9EBJDGlTtg1PLptqS9z3CjQTknc2h78aT7MW772tBIHQkMZhIaVONgzXhcd365QrAuxo6yqsiqu6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☝️
تیم منتخب جام‌جهانی 2026 از نگاه ESPN
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100922" target="_blank">📅 04:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AcWV2Nlkt2VZmyY4qH3nYv50DhTEbHqm7pTsOK6zWyItvoyomAK94SMODPYlF88qbMSEdcj-vunHBKZTRJZIzTy1yAkgpw6bT1oSFDx7dluCeSlrksQOMEoqu88sKptgBeYN8gYh4JtjFSDD_j86ag31r75fiSZozaZQHhkdPckyQzyj9-mcG6YQneXmZOBJ3Xh86xBLHXJab2rvtu-dSYoE1niqVKUYSpo2Gix3TbERY_M4F35mxs_VYNscBX05JFHP3-36iJT1rEvfOpfa_QWYLkJTbKz9JfU9FzKDDmnZB2btVI0tn-xgDjvYbyxMv65yg0k31MopjI5j04FAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khJRNVOjO4PcVa-JAbPoPCxZub_1ScQtLqcJe78W7jAUW2UbO6M0uBY6weUZNja6ofFR_9M3ZpUf6bIT8N-GoPiAY6m5fzCghQm2rGWwQUeCFOT-iyrPRebs0Ohit4wM4ijHYfgyFBeRkYMHRCT7CMr4umMdbr8sj8cP1dXQ4jKk4DMCkjWXGw7uuHEfRqtHNAPyVY3ee-GslgRe6TG4IAyesRTgtCsNPZ3Kxsq1T0YEBvi0UrW6rnjxDz6qH9usvW0KKWIk95qGbbGvySICJm9d_SI28afV7ddHP2MbieAfekqiknnx9sbwS_x5FDetktlvWEavHdpEL4JrDMaBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooPm39Up1xAZzt6uvabH8ycOpvzpDy3D9tmLZqCzrIYNrovJGTRKCGV_xpAFH72w3e4tR8znxteAjWuPauIThqF2z4hdXykWMiIqJoR-6Qhb6lJobCkGmWuEuBovzMnZCACLRaIr4S13wXhR6pcgibLIUsuarYd09fWppDmAoltaBIqZmDKt62VFyJ3APlMexVbTVArf3hY2wevC7_m0n7K-1yzqy9yel8sHJGQwluRldp0FjcaSwY_dM0ZgjhYoPcAGZCkE0KWjvSMO8nyWBHMspZngcl1bEUT5EC7BP3jsNaLpIO70mNQ3ot57c-pjNn9QR-JFt-0mLDA9JRzOYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بِلینگهام اولین بازیکنی در تاریخ تیم ملی انگلیس است که در یک دوره از جام جهانی، 7 گل به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/100919" target="_blank">📅 04:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUKF-Y8qVEoLa_MQvwq83oX-XvD908t2AXIntzdc9PjA6QmWVmn5prlmsh-1lumuseaqV7KGe3n27tWF3pwcAkLBSWrVJAZnUXRXQ9ELVka8TdfwRC3guxhvhPWNEBOjbzlxApafPQFHcGsRILgVnoDtZ9gwgBqRIoXVJJ9EsCSV_3YPRNfyxY04BY-KZBqwDvH0jAcaIavjbzKcWyeRqy0hrN3UqlUvVd87fK_cVHbIKn1I-Q-pAvCq5QKklURlB8ygWfdu08-Kf703gVRxupGJ-O1iPPHp4VFO2DnqLoVkuQKAPYFYpfbKApSWxPo1E1Kb4Qp44pBuf-KdzadZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🔥
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
🗓
یکشنبه ۲۸ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100918" target="_blank">📅 04:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m61oZQuVmjIEsGE0TT8ZGAthN1E79YXzQfH6mepbdmNLrO3R2UX0lkH0w39DJuayXVE7xHL5vsJAo08qJ0KVb5nJNpkDLSjzwqfwYyI7nYayKJvedHJCTjRLhjWMwkikp3VHMeHNqa5oTbnBopwgy2lKe70sgTPKZXJYwQpBS_yPKXQURIQHk4g0Yph4dKSN8PboFi7d9WGmqrGqDiMED81FNv_v0ewEeWz4jipoKJM39erQ-OyWguqyrdeNdGGHSoZiexox-fU-4us1eqT5bwWcSewzUMMKOR__7uTO_KsWbV91Kai-y1_GsY7lh8pm5atIx9f_7otk8LSGUhOfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بوکایو ساکا:
"در مورد پنالتی؟ جود توپ را گرفت، به من نگاه کرد و گفت: "برو و هتریک کن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/100917" target="_blank">📅 03:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TddMTS5H8V8ulutjL3QCHiYMyqABoBSFFjeyRCNSpuKcm-_KI-pwG-D71hNinflsLQP6H9pihCmHH_hw9DCk8is0g6xL1WLrVpaAsBjYPf88wkyOJrthed15ytrAf8EpS-o1reyCGUmLkJhev7dBUqJ-paHWad0wj5pwJeUM6E3Zd8DFlTDkV9lhHtQOYbKA31nFp6NJX5UmnAYXoDUzEXyavvx5WyVe7kIj-XQLeFwe6Hf65hg_Im2HCxuBEtAepTJGSCGD1oyc4osyOxT77Swn0kzZMHMv37NiHwfjbG0UTsEvL3UfajVqgzyWmaCe1ldNCtj1tKGNLQx_sf9SNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
‏
| هری کین فصل را با 73 گل به پایان رساند، اما نتوانست رکورد تاریخی لیونل مسی (82 گل) به عنوان بهترین گلزن رقابت‌های باشگاهی و ملی را بشکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100916" target="_blank">📅 03:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaFcVPdHg6w5KQ8OYlVxrXEhU0V7u68ti0x5pFu9xoAQz7uu2BHsx22e8GvNKcXra2Q1BPcmGHOxdXMzcShlvFs-mOeyLWvMBNIYU4CouosoS56aJTK2KeWMo053C8k5g1nwFHUwZRnwEOMFTgkI5kUGT6OpQHvrP39hDToIwAv5oIhx4Q9T-9aDjUtXQ74yXAEeuV_HsnncydawSXD2JzptGthkogUOE70aNQOP0gz0ftBNyjcVVd9PDsq2iGBITb4_hfSDkNrRpNnj4hjyVPfPPH2_-ExD637cFx8XDP3K1q7R3w4UDN2V39ZFpXjbb0_8P3I4UnGA9-zHgKgm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🏆
| مایکل اولیسه در جام جهانی 2026:
✅
او 7 پاس گل داد، که بیشترین تعداد پاس گل در یک دوره از جام جهانی در 60 سال گذشته است.
❌
با وجود زدن 20 شوت به سمت دروازه هیچ گلی نزد، که این بالاترین تعداد شوت بدون گل در یک دوره از جام جهانی از زمان لیونل مسی در سال 2010 است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100915" target="_blank">📅 03:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VC4gKC2uzSQKWZtzTB6qyS-k7j0PzloLsH0mv_-g_cTOezt3K8t9S5d-fN3XDSgwdOHyzHOZ6j8N5daxaY-FUN-FlNIP3dH_xnDJSDR32A-p1Z7sYyIVWFDIIqCZaVVsFA1X9Httca42D8-Ebs_dHquvkTITTY6ia0QVkkAtfbzq88E8g6Y2CxIK0W6mzWIoTym4a06NHyCYG-GRJ8Q9oK2y-Yp2I07qVKfhbJhYP33Gv18WOpkS1fdNUJcGskLwRZ7rH-J2KpefAMUfSdL-P9Wd6sRZWLMD-lAr6xVFb7WohuJfWimgKuVOimf6gYAr59w1ietFpEd1THv8xPgS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9tPMeWFWw4UvkkoRJt75iiwDDBbap0YZyD1m2RtnQSbhAHEs37uByk7-lkEzw_RQlbi6fZ6zQzXI4ndQPmys7a6d6MTqynK8lNa_i2JtcJjIkL7jqRzgKEiG6nqwFWFcgxH6M3tib7531GsTyEPwTDYTKSbvwlEo4_7n9ptvWb78l08icFy_P5o75aTuFwfP683Laja9GTeLGT3caPGKbcW-G1imW4uyz76_6mz6s7Jou3Ad_W2ht2DQejAYBCctAMPrWv3XxgYLNyWiJ3LfP3pSRXT4YpACU-usbIENgycow6WNn2GRGUSX5754RhM-QQQZ3hlIeoKowaTOEqlUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جوری که امباپه برای فرانسه صدشو گذاشت و نشد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100913" target="_blank">📅 03:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNLGI937ezD6HszvdPT1k6Q48Xm13hVwiRYCpfU-ckrg0b782PBwZeLfzuuJY-_wWoAEHoFFZds48TYyKX77wPE2tu-YT3qrpWOlWm2grevshQF4WQfjRKkclg6mDc2N01ywz_NMu-lC59V5UzpOR2K6PgBHCdtJcJ_fo_JTRtbPnB6ExR4j5HceKbLPXVFWUMKQl6VtW2TOG_mswCu7E4BENe6rKVrajVfRw2En1QbWWE5ypkGUPL9gGzqkQK4HSjekB_7xHoWRctBuC-cujxbY_pIQ_ND-0DscNJnSVhXD7NvWFun5ghUvLQL2NizGytJ1aZ5PIckslColYohb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
رئال مادرید رکورد جدیدی ثبت کرد و به بیشترین تعداد گل زده توسط بازیکنان یک باشگاه در یک دوره جام جهانی رسید.
⚪️
بازیکنان رئال مادرید در این جام جهانی ۲۲ گل به ثمر رسوندن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100912" target="_blank">📅 03:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_mKaDQu9v87dQZc7dwCwZiB2CENwRM432b9K6W7HLlU7EIBZFYpFxTDubH9zh8XmqhzdIPfB_OL2VGJpibE6l9sxzn5kPfQQC9EzUvMKak4xxJfTfrO_mCHItrocuKzrSjzrxAbEop7tK6xHQvxNPzx3GhqdemPy8HkWP458HZPyaL8kCTcHC8434WTie_GvSSRn86brIATavRfhUjwmVc7tBi_STp81yb1K4B_dKuOh2bvUhTfBQ83gsHKAMbO_dMIy6LIoJPMwr3C7q-2Fu3r3aNLPNhq7nx91ww-yfkXG_lztnEysSUI9itR3r9U17uT5NOmTVOoQ2FlnZNJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
گلزنان برتر جام جهانی بر اساس تیم‌های باشگاهی در طول تاریخ:
🇪🇸
‏رئال مادرید: 99 گل
🇩🇪
‏بایرن مونیخ: 87 گل
🇪🇸
‏بارسلونا: 83 گل
🇮🇹
‏اینتر میلان: 76 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100911" target="_blank">📅 02:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuZseBnaWEo5zqtcJt4UCLM-AuHNu9YbTzkpXRfp-6XuEnilTZTsfZroEM_7QK9YVRQm2aenG3ujXOwNd6X2ntW7bumZ5WjLcYe1z3zVcw8v3PvFHsVow64jOtHw9Uk_stGGPn0dhTOHzbkybw6V8Df0yAu6hYvW-LN6Ek5CFxHxVPsf4ZLQP6pnoVrWkJ1Dup7BaSU_RP_ufqz5V2tT_3rricZ6r-gyyq6XMpv7cf-UrCrtXakEk9fAZx0Z_DEJUu22JEE5gzr6ad7oSYXiKsu7_zvJC1_9LIhBkYxr8ngNA4XfiVkhUVGDdvfpBuVWCEOlWN76-KUOrLjJfdRDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋🏻
🏆
🥉
اینهم از پایان مراسم امشب رده‌بندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100910" target="_blank">📅 02:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100909">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veVhoLiHbBdk6PoWSNcsHIsncOLhSzHs2QAWAE-yuHgHMm4_izOPLB6Nbhi4pqu1FgprUtlW6hdp8UkoKgAiEzr2aumiaF_O77iLlCgibGu3u6TtMqAL8sGByxJweNfEQFLLznzSKEzgLohjny-eHFAczNdHMYuBisibukxbQahf65j6THNrtP6xwdGGfDeHn1xoEbKTzdzy7eJpwNloT4EHnSbnnFvLHjglXJgq1bUzq1zX3ChDa88t66zB4IelMqyXZ3Ka2Ccond0UMbdnAywmfA66PSYYypTSYetWi8tOlkAaRQ5u_Vo2D7jowDyosf_uvC5AfPKbPvebosnsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
👀
🏆
حالت‌هایی که لیونل مسی جایزه کفش‌طلایی جام‌جهانی را برنده خواهد شد  ‏• به ثمر رساندن 3 گل.  ‏• یا به ثمر رساندن 2 گل و دادن یک پاس گل.  ‏• یا به ثمر رساندن 2 گل و خروج از زمین قبل از دقیقه‏ 78 (امباپه 698 دقیقه بازی کرده است؛ مسی قبل از بازی فینال 620…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100909" target="_blank">📅 02:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLB2wlS_jYNRQl1Ez8KkTJB72_guKVNk4QFRJiz72aJSThGZNnfNv48whiZvODW_whntwjTv8bnhQXVn9v11NPc18nrHvRJPEvy8KmfRkDcJUS-PeY1j5pZnEt1_9fF_qi6P4z4yRusfHflNHZDzqokomJHg8aPAJq35C9_YdP7lhEU28NHu4Lc3Hxs0rFIMlxWNcnX_JdJr1j20mS_HVXfKSlhYQREDm6wsa0pCAWGYCxoaibhsRd0YOxYcQm3QXDbe26XMcMKwxNz6rLjSlf8l4zu6unEUEOyDAjfrDRrT6WIXSrd4ueCSPJ3IBTwrI_6m_lDCLj8HbHQzPNdwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
👀
🏆
حالت‌هایی که لیونل مسی جایزه کفش‌طلایی جام‌جهانی را برنده خواهد شد
‏• به ثمر رساندن 3 گل.
‏• یا به ثمر رساندن 2 گل و دادن یک پاس گل.
‏• یا به ثمر رساندن 2 گل و خروج از زمین قبل از دقیقه‏ 78 (امباپه 698 دقیقه بازی کرده است؛ مسی قبل از بازی فینال 620 دقیقه بازی کرده است)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100908" target="_blank">📅 02:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0yOeqtNfEfTYgr46hVExtGnyXImQxZOHZ00kANRUuGpjY-dujJ_xnJkTTI8o2ghGNejaV6x4QvL2GrMOKay9DuT-l5gNLF6QBLdd4VBcy2TUQ4NetQm--FL2mFFVD-yfqg1F1zvxuVNQOLczC4-eFQTFvan_rqw-zTyRSgxeoEhlyHvp-0EsLhAcGvVGJ2b6R_BIkbMleRlmXK2o0g21xcJ6UipOf5h0SpkFowhL_6aDjg5GuGbTGF-IK7sSIfTtkrf-fE_be7YVtlHLptVSeabGVHq75cv05nJW9aFYNNw-2kBImj0F2aHnOakM3z3ToUx2MJd5fff_BWPjXlo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇫🇷
پایان دوران مربیگری دیدیه دشان با تیم ملی فرانسه.
‏ـــــ 185 مسابقه
‏ـــــ 120 پیروزی
✅
‏ـــــ 35 تساوی
‏ـــــ 30 باخت
❌
‏• قهرمان جام جهانی 2018.
🏆
‏• نائب قهرمان جام جهانی 2022.
‏• قهرمان لیگ ملت‌های اروپا 2021.
🏆
‏• نائب قهرمان یورو 2016.
‏• مقام چهارم در جام جهانی 2026.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100907" target="_blank">📅 02:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j--uIdG6pumLjKZMBSwYPg6NBZYbq16ynM7NwBZgl4ozczuk3XVZVxP3Rv_5sqi1o1-SMRxgYMtHgKQpoqaCiAdo8IdoFfCplQHbTMxFBYst4RSjU4AsQfPRVcGc9Hg0P_yyA8iswIJSKSYG0Y1AuD_8rJrLPDn_AwWFLpPmjtfkYDTNHXofE6WlZm17obonWOY-PytLfe84M3Yx9IbnUA7VA4MIqjmUxiC3J-tyjCbEp9vojdXd2602G-yo5Iyr6_oU8LgiU_PpD1O1e9xoWo5EkCOZg22pCST6f_KtwOip6CoZvmqz4w6Ue_TkB7q_CCUNRpMSMZEfHIARp3Q7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم‌ملی بدلیل کسب‌مقام سوم جام‌جهانی رقم ۲۹ میلیون دلار پاداش دریافت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100906" target="_blank">📅 02:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100905">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXK92CfnShT4EKoPFJ2LgdRizuCtWLQIQM3Ad5S_dmpJX_HKQMM9VpCW8y0w9xI7Cek6DbC4MTcBtfy4rMMSEs5xI1KRJPbHb710brWvsZl04JNZoWSdb3bRRC1YYTPi-i4pZ74fXWLtvKdddvfyMNmEZZzV6-d1FMiTNEb_i-VJSjOivfDSRj4Lg16ayRc7GqjbszT8qNgTVEpxaI5Bp-_uUVIE_fVNXkf-9K0uaMfIrt8uYRTkA6n4mfAms2bobOkbWj3glxR4b3k1NY92isR9auaZwpXoum1Nn6iw_-RK4gUMMfPRR0oeVWUYMSEgNb6dVheTlQ5jb9_PRwLXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین گلزنان تاریخ جام‌جهانی؛ لیونل‌مسی فرداشب اگر گلزنی نکند، امباپه به تنهایی صدرنشین خواهد ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100905" target="_blank">📅 02:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100904">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUCSWjsa2exQUajymKDwL03kceh5kteoboegZk6yFUSu3fkupO-cvNybRgMMWghBcsec0xggcmeLnpDBGXxqtEQf-iSUvNOsyg3P_jj6J5R_aCg5z4TU6SrDpC5NgmuvMFAGF_qVrmucnY61SXjbBA1p-LNW4dvyW-o_Z-1TYWkuoGq7_kNpkHAdH45h8rB5HylUt3fl1rvxJryi-h7VDDnq0urbKwLSn6_Fno7bHa1SeN3Smk6xPVVaY4KwNYCgYgav9otfki0tpIFQD6iikE3vUTQvMawDcyKWpXoI9vTe4fmS0EAkrxGhSsxtpwNQ2byBas9AFqun3_5Fhi44sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بِلینگهام اولین بازیکنی در تاریخ تیم ملی انگلیس است که در یک دوره از جام جهانی، 7 گل به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100904" target="_blank">📅 02:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBhUGzx50yPyoBUk5aDT4RSiD2sBz26wB0qDX_C_jksRYaXUSLJmc9ftlyGZU4WuPIkyqwU-JuOoSXRRV16ib2zhqkpZvOx7_7IKeLWt9aicWcDnqMQ99hNsnXtiTPLyIIOgnwryLu5MhDl2Jhe963zPasPEIUZZt-zHF6yatSdRiPJYGiOiI3uRBFGZiJMiIHq_Er7EZgFufVYxh4tKixOQYLKBazWJBBnFvuuB2mgCIubIdOnMJ4JfusXOjYLf1wx4IF669P6MzG1nr20sy6Glo4kXn9GWlSlVb747GGbCXiQ3RmOBOGyihv1EuTR56PbZl0DWlHUS9qr56lEY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین مشارکت‌ مستقیم در گل‌ها در تاریخ جام جهانی:
🌟
• 33 مشارکت، لیونل مسی.
🇫🇷
• 28 مشارکت، کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100903" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbOUyGI1Mw5A01op5S3hMQfvirp44-0We5fQxcF0AF23dezc7Af56HAAyCMA4EJ7_iNpwE2L6ptmcpdg17wBKMFhcQ1uk4HPRKBcxsHwpXYc6WhlYOz_W3rdJ3n2bo3-tmmRD2_QXtxJ2FCzch5Yh1RMy_XhKOPfph45kwa-b3ZN6GBGMbvQO1PYKH7nrEdVBczab4EmFC5vClnl_XWX1l8pAgWuF6pe7zlF0uNDz7XAxJK-0CAPKgtX-8xa5kW8pADYfxzLalcU5O0ede9s7Hxh1xETQvIys4WVTb3o-vcb2_YdImdWUZIlRBcIEQiWabNc21dxJ7Iq-NR6MBmdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
✔️
ساکا بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100902" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqgnzicPdhk_4UKV4M_x7D3VDvBE4ng5IEYzJHqIy9SsdSZfppkfVaxPslTDZ8z9LjeIGqbAgwnk0xFujhPA-Py4SWfrklsnQMvLQF-oAqvFARFmKHU3kOmWbBIS41zVHF8Q0D31SJoXn3sBrU8LbkaoJ7x2FP3i4x7NHF0xMLikzVk2s9wSmFgc7DO0gi2eXsmztTohRQ3IeXGH4fX6GyGTFFzQR605Zgxj_r2B_tvXTBzSWtrg9hKdZ6Ic90bysXQoACr2yRRXnoQcZxENZ4jLeYgV1Y1PPPo8iy5rpXymsUT4b8xVpkTrAs5GSIv698TGp484JusNZsJTUQRWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100901" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگگلگللگلگل ششم انگلیس بلینگهام</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100900" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/95a47532f6.mp4?token=eimRodfJZePddh_emlif9oWYt3x63isNtnjuYaEhOoCzmUlzJOiql200gs_XVm016rE-1RjL72zjsvdrigNn04EIqR03qlZxfwhXKaVK6XhVD1FKm_HdPAshuQxLL9kkkG76V6vqreWvZF1Acl5GPsMhIj_1PA2j4nKYRtGTXaWsk-JP3OMo9LMdGAQ1SALNCuqBfh01xXJns8oVOF_iOHGvpuCaMR4ex3swskiR1t2oH-KxaGQ9RTCgtUVkDNYflOTrwNivHhiCJRd52FDo3O56-AhNfC20nY7pqQgni5P90d7C-g44WZQd2fs1k1M3EeM0zPbT1uCdIF9LdjdguAUgJRtd4nREwdzp8AlQMKwW1sDokupotGKrtRUnw-uolkHb725uOdivVsWEnpgWBYgZ7Usdeu4DfRUjSD7eirsrN045KSEj-0_sPEpnfHWGoK15rNXKkO-J8-L0R7f4wxZHGJ-jm-OO1nm7thv45A-GR-TlZrtSoF-33gjz0wZu6JWAgVTiKBfN-4HD_9R0BZ7ec7Z9r3lwp-o6o8d__lzMsUjJbfXPMmVjh3Kb4Mgld6yYIazhBgMHx5Qjvnfcvbo03PPP2N2Sr5q82Bchn3re6Co5mnuN8uqKZVh9rWSHef1NO2SnIHLv6Sx2M1aK22bi-YNA0nQpr5Qk4W4Oh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/95a47532f6.mp4?token=eimRodfJZePddh_emlif9oWYt3x63isNtnjuYaEhOoCzmUlzJOiql200gs_XVm016rE-1RjL72zjsvdrigNn04EIqR03qlZxfwhXKaVK6XhVD1FKm_HdPAshuQxLL9kkkG76V6vqreWvZF1Acl5GPsMhIj_1PA2j4nKYRtGTXaWsk-JP3OMo9LMdGAQ1SALNCuqBfh01xXJns8oVOF_iOHGvpuCaMR4ex3swskiR1t2oH-KxaGQ9RTCgtUVkDNYflOTrwNivHhiCJRd52FDo3O56-AhNfC20nY7pqQgni5P90d7C-g44WZQd2fs1k1M3EeM0zPbT1uCdIF9LdjdguAUgJRtd4nREwdzp8AlQMKwW1sDokupotGKrtRUnw-uolkHb725uOdivVsWEnpgWBYgZ7Usdeu4DfRUjSD7eirsrN045KSEj-0_sPEpnfHWGoK15rNXKkO-J8-L0R7f4wxZHGJ-jm-OO1nm7thv45A-GR-TlZrtSoF-33gjz0wZu6JWAgVTiKBfN-4HD_9R0BZ7ec7Z9r3lwp-o6o8d__lzMsUjJbfXPMmVjh3Kb4Mgld6yYIazhBgMHx5Qjvnfcvbo03PPP2N2Sr5q82Bchn3re6Co5mnuN8uqKZVh9rWSHef1NO2SnIHLv6Sx2M1aK22bi-YNA0nQpr5Qk4W4Oh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇫🇷
گل‌چهارم فرانسه به انگلیس توسط دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100899" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دمبله زددددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100898" target="_blank">📅 02:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگگلگللگ چهارم فرانسهههه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100897" target="_blank">📅 02:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">۷ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100896" target="_blank">📅 02:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b65d918250.mp4?token=omY7PsRMuT7IxQiwbEaLCMfhMRvlKXetiK2Ok2VTF4DlTyZRzPzZg3Pvuq6HXKO5SZhAdeQSvuqutBlm9EJd0TvXQomI5bmcWOcFtywofTcZxgb2ScaFA2_p74zd59_HiW17m5hSd1Iyx1BTW10ksX0vJRJ5xWj98Qijjo3bcicLzLk7rLxZqpeRctCwcwdpZksfCJGTgMvaIl_B6tllWwGRznHMvm4OyiLRlL-9m6cmD_yxMtqPzTysqNg111UgncCTMpMBMMewSn2UzjxiUyrDVEpXWR91UsHmFh1v_qnjKoFr5s0AILpfTjAN1g9FWcUCIkF-EqfjMTG6XN2XZ4TTbcRQLp_ir-UWkMZz6goyLD5xw3LOQjawnOwe9DHRX9zjP58zLilMgukAxyW_cM_AwPTqyIXO_uX1eGbtd1SNzqa5TIwyHYCjdIezhUZjsJTgMVcUy6CdbZiDr6J1ag489wGKgjd2fO8i3cJUAdbQfxUTnOnJvHMcPmc0ftgyV4hbs6gJf54MJuNMy5dfKQ54gNEGT3SlB2HGlHSd2pOR_B0GN9W93P1x-x9FbrhD_lRQAzgiurynggGl8xl5u74T-jsgDF1umeKI7_uMwUe7tRHc7VhOqu4Vtl5Wuq8Cm7iFbShCM8a7xJ7QJflWt48ftaxk4ES0G7eUWVlUo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b65d918250.mp4?token=omY7PsRMuT7IxQiwbEaLCMfhMRvlKXetiK2Ok2VTF4DlTyZRzPzZg3Pvuq6HXKO5SZhAdeQSvuqutBlm9EJd0TvXQomI5bmcWOcFtywofTcZxgb2ScaFA2_p74zd59_HiW17m5hSd1Iyx1BTW10ksX0vJRJ5xWj98Qijjo3bcicLzLk7rLxZqpeRctCwcwdpZksfCJGTgMvaIl_B6tllWwGRznHMvm4OyiLRlL-9m6cmD_yxMtqPzTysqNg111UgncCTMpMBMMewSn2UzjxiUyrDVEpXWR91UsHmFh1v_qnjKoFr5s0AILpfTjAN1g9FWcUCIkF-EqfjMTG6XN2XZ4TTbcRQLp_ir-UWkMZz6goyLD5xw3LOQjawnOwe9DHRX9zjP58zLilMgukAxyW_cM_AwPTqyIXO_uX1eGbtd1SNzqa5TIwyHYCjdIezhUZjsJTgMVcUy6CdbZiDr6J1ag489wGKgjd2fO8i3cJUAdbQfxUTnOnJvHMcPmc0ftgyV4hbs6gJf54MJuNMy5dfKQ54gNEGT3SlB2HGlHSd2pOR_B0GN9W93P1x-x9FbrhD_lRQAzgiurynggGl8xl5u74T-jsgDF1umeKI7_uMwUe7tRHc7VhOqu4Vtl5Wuq8Cm7iFbShCM8a7xJ7QJflWt48ftaxk4ES0G7eUWVlUo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌پنجم انگلیس به فرانسه توسط ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100895" target="_blank">📅 02:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هتریکککککککککککک
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100894" target="_blank">📅 02:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ساکاااااااااااا</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100893" target="_blank">📅 02:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100892" target="_blank">📅 02:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پنالتی برا انگليسسسسسس</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100891" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
حملات به مناطق جنوب ایران آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100890" target="_blank">📅 02:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انگلیس کووووون آوردددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100889" target="_blank">📅 02:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100888" target="_blank">📅 02:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بلینگهام ریدددددد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100887" target="_blank">📅 02:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100886">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اولیسه داشت میزدددددد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100886" target="_blank">📅 02:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100885">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100885" target="_blank">📅 02:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100884">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkQT78Wp--0en7NtRjbR5fbYAXKqGYIzfd7BdKlNrR-rYEQQlKFQmDyj5VfUn8ucd3JRVThwf8Rnb-mxJNfijQlIbDNxcZ-W8U5_0gLZWPswmmdea9QcARmZVGnzkAOMEU2j3dhkqi78Opamj9FPFjSxVSh12QiQtr9d5FHTaGbQrqeKUjIfExJSiC-gy3FUVKAfpwmQu6I010wr4soe0dxaOVY80ENi2FBOfGDjPyzVuK8PpswLtPr4gB9dbJrj9OtEnDg1FWLByKqKp6Ho6pRrhaKoaMlZ0lCR_OYrqg-EgeSqeAZ9ghYMz2h1Oo1VWbjLyHH07IHLpCfsAxoAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گل‌سوم فرانسه به انگلیس با دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100884" target="_blank">📅 02:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100883">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇫🇷
گل‌سوم فرانسه به انگلیس با دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100883" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🔥
🏆
📊
مایکل‌اولیسه با ثبت ششمین پاس‌گل خود در جام‌جهانی ۲۰۲۶، به رکورد پله در ثبت بیشترین تعداد پاس‌گل در یک دوره از جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100882" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پاس گل از‌ اولیسه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100881" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100880">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امباپهههه زددددد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/100880" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فرانسه سومییییییی
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100879" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100878" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjMbpavS_eWnG9-836oE6CVl6ly6o4WUGRRuDBqxjFh1LVzRNWn4vdusBpd7vWwL4O3yRGElqOKW4mZxdQ2gIAXhKxpbQuQdnDn8YUJ2AVZx_5thelqn9ubr05-SR-Zj9edq7HIsdxM-PrTwiDLxhBmJ3OYoH4zU928sh2FbH8UEdYTAhfPMfWZIB7-OSM5Z8dDUROE9A3lM_llqZfAzRINiCXXFYTp_qI7Out7_m2MxO8-B6n6m61h5Laq2RV668zhbHcMxNDUmSM-8zIJk8r7BNHGJ15BPQ2qFlI6XJwMaN6AGOkbGxZf6MKqsECKKlTeY2NcrPUuF1H9uqZIlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
📊
مایکل‌اولیسه با ثبت ششمین پاس‌گل خود در جام‌جهانی ۲۰۲۶، به رکورد پله در ثبت بیشترین تعداد پاس‌گل در یک دوره از جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100877" target="_blank">📅 01:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇫🇷
گل‌دوم فرانسه به انگلیس توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100876" target="_blank">📅 01:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فرانسه دومیییییییییی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100875" target="_blank">📅 01:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇫🇷
گل‌اول فرانسه به انگلیس توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/100874" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇫🇷
گل‌اول فرانسه به انگلیس توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100873" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امباپه یکی زد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100872" target="_blank">📅 01:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rgmd82U2BfMSR1iO-Qk9inQZWI1hgUQOWu2GE8YPOOnkr7GzPjB0U6r_f6IuQZH72lVbbj0Hr7sNZZS2zWee_XZxY4SluAtAjN5khw0_X1gP297aj4MvNe5zU7zofnNJ8l5-PBROgCE7CCZt2sqV0HItO8pTfbY6fm4XHbyAWSLjqLp158_yziCeUhTOXxvTmjW_AVQjv4b867qpTV6jHLwwP4hnwn8XoA-45HbXxrF95AKtpmNsq3-je3pMaxGpZyZqT3sJGYwfeCX0URkGBLLxmNPHUfh88GfzqiW_aLIB-73jnnpyK8UNwtPw_-Ft0dQQBgoZ6UJSAw-eRyKvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❤️
خنده‌های امباپه در کنار توخل حین ورود به رختکن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100871" target="_blank">📅 01:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT37SVqmuK5B6EWODcmqKwO2u3wlhUEZWfjcee4GQ4I6xXN4PU-PZ4ebC-6tvu1ASQsjnS3r_5qET36bNPE022hamLRDomsl6M363wBMc31G8A9B50yo4UtAga2vsNjMEb37ZnPSUwdn3G4dZE4tL5tW9XlB1OXUWzfu9ZDfyQ2TQq49vZtKiLdo9QnRmSOELTjt4yJjsqYTJGb5ZmOc05pfyQ-KNt8OhtKTtg-9a61grB3nD4GG1wM5rUIJceEvzeJiMeyG6WBNxrDjYW8fUN481YxW-GrBVY73iUArIEXTgxpL4vjVGQ338hXjpHfo3s9VQmkJnYwPPRAAXbw8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
اکسپوزیتو درحال تماشای کون دادن زیدش امباپه جلو انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100870" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj6ingFSArWtiTeWMs93gDHB_gBIxIZzpAk6qLiq93sJTjeUIv49ELif9Ar4bwhcE8ycs58lpMpKltFQOYF_LGrmKk_VlEcQfzilD5nAUgxALktR4FGpGQsyCybe1_BRTJpHvxT8XSMP25_ypj9isKymDzv3_fA3Mpi_Q2rlY9Nd1Cc_X179a4D9h4vrzlJyGAjvDH0Dv5DXT4W1iO1ETX_L6r_qeF6U0N3h-mVN45q0e1zHzQRAKEiRidh2gXttYoxJjU_PGbJSmwIpjbXLVXyO1KrlL-h5D3A4G8GZp4THZcJ011T8U1k7Wbr2sxM3HgfA5_9-hRXG3IdCaEOsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
فرانسه برای اولین بار در تاریخ خود، در نیمه اول یک مسابقه بزرگ [جام جهانی و یورو]، چهار گل دریافت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100869" target="_blank">📅 01:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
❌
نمرات بازیکنان فرانسه گویا همه چیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100868" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTcS6W6sR0SiFUfFcSbiaGYKNa8bGiA9a2TVyd99uWlqZzPMyGgwF-Hzxt5HIsKf-BsoaO853DPm9O_xa77AZ5tjnd_IN1VHxX7Va_R146Ir9GDQoaY4KIHZZYcoIwbnUdxWGc8Y3jy69QEDMp3Jdfuzfs6TtwipnPukZsfbTNqJ_dMtQeKoSaiycLQnBg0xNJfA5VHg6tBLO72LP-ml8YnQuQLvUU1XNoTGWk5W59Njii3WoFO0qhKOsVmIFUeMjd41gwFKrnPV-bC9a2NtXI0MXHsyVjyNKvkiuvXi_nOQHVk6zTxPfX1cbCHM3K3E43AfEym6PpMTCO8kmQIGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
نمرات بازیکنان فرانسه گویا همه چیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100867" target="_blank">📅 01:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100866">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
پایان نیمه‌اول؛ انگلیس
😀
-
😏
فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100866" target="_blank">📅 01:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🔥
گل‌چهارم انگلیس به فرانسه توسط ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100865" target="_blank">📅 01:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کسب مقام سومی رو به انگلیسی‌ها تبریک میگیم
❤️</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100864" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دبل ساکااااا</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100863" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ساکاااااا دبل کرد
😂
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100862" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انگلیس چهارمسیییی</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100861" target="_blank">📅 01:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgNvNvB7hyN2zHGsmrN96yooNCY3ydb4lOS0qPMw04rRfOrpDBTwPPE3_d63YisUhA8DPuVx9Gl-YHHm2vqjw4EYKwibtPdF1efsLg3A2LbnCcUDLU9MpgfTBOngL8jeSmBiOOgkBe26twnQEiDNGJObm8_ViNv16T0aGRqSWLPRdXMTNk9LsQep_dryfJlRFebFw_dakjHEakiDVqQRKkTyNJ0HDzw5kgRgyFJ3GKwxz8ZQ6-5a6PG3jPox4LiIhA3GDlK0Vk2RCiBsGh-Ge6_dwTmNqq1kCYxqcEDzEYseprp-V7ZBOfSmUlYAStHyolXstYZGHZd5xVxaKsA0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
اکسپوزیتو درحال تماشای کون دادن زیدش امباپه جلو انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100860" target="_blank">📅 01:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc1tAhXNk0Hu-KXIT88yA33fGKzEhEcdW8Dt8ivGsE3piNEFShCA7zDZ57TlcJGxSXoGNexFHdBBy28K9eRRw3bUbnCZeXkwYVp_uNaY1nOwlNQGt8ALq8y1of-oj9khvqlGYhKPrtaWZMYBdLcfSeXyCt8EI7LMPTrpmjhOm2-fLpFPWzhTIYPB_74gvCgHjaiKY9tC3ZCcppIbqjm2GlTPMlroXyb0VLYGdYRr38gqqp1lXx_zMSjjjaDL8zvpCQv2wIGLGPiFMF562Cc52WrlD5iqCNKwQRvAyngCgtkT0AQgEkwwH4BHd9qCgeclv3bp4iZ9dKlBL4Y585JqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😔
از فردا شغل جدید اهل دلا مشخص شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100859" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100858">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFUxbCMol7RZ6u5C6SAnrGw-2hGourKNdawWu60qVqVtXYIK68fLRDQoI_C9xQjTjoXE-USRr8AW5ywXk6ciOaRr-htUeY53qwZf7e7EaPL3qEPTQmdlkD2Ko2a-7iMvbqTEZHACdtv1Czk-eojr8P5HRZ_RYFM75qXtOQHdz4yGnrx6fQAxIbs1izY9-v6S9cL5kCugzVExGWlQyPoehvGo0DM-ATgmEzLTLxjIpm_hw5cHDaU11GWRjEuSHZSwtza-BUBKG4cKnGSWeWXacHl25VCMTh7e_3E3sQACmbnlty1EUAx8mmeWjmykXrj5Rr_GZsrybTkBG2UwWw9Jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاع فرانسه رو
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100858" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100857">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6441bdd49f.mp4?token=EUz8Dpd6769QFW_IuIn8SD_voOfACDckSyD69FtyNCKBZagkM5Zb4fyCsO8Xi2kAVmTNLrJHzzG-7Zha4ZH8GxX-n2p71GcbebVofvJfytVBNYl1-nipX4wVISAvG-bcpk5FbRQiAsq1jc3SEXxSIUZXk4Xp5iO8kZXM3Awg3ZAcTW6oEMbgZxneConFuYyzskjge0EKEmm65ri4pJGm7K3e3imvZzubARt49Ht7HIS9Ev3iSyW-r1zxByWIsGZHfws7SEn3QRCst3t6gIJvw9kESeBr1g4J6XC4DjDi9pDdqXaorpI98J2v7QpYCYTHJ2nJzIC6ls1b8ZgB0tVIKBOxUUb3ffnNn_2vIncTSOTOtFAszc2A0eDwMbDZK0ClJFvtwi2qXMJoQhEXb47UBEZB5k3CFfAmy1miHWMdvlHJJJRmLQx0CglQqNZExijz2yzb0JcaCnS-EU9j79XDYxXHQCmCwlaAfEkfvbqLeRg6-cH78AuIYzdnKOIqcGDPdZIRmTXl2A1oQgp4WqQQbSlIb3rYlx5XGo1OXtbOZTtFeQCPcRSVv_PA4gcKeXFyoWelQHq91tVHrYHDudQOIkWQEnDYxzstaVZg-IooHLZipaxcCyMBfpT9VwqJSV4Iz3lAXpiT5jc83NssWq-i8g2cdiEWx6b2u1_nJ_CE_os" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6441bdd49f.mp4?token=EUz8Dpd6769QFW_IuIn8SD_voOfACDckSyD69FtyNCKBZagkM5Zb4fyCsO8Xi2kAVmTNLrJHzzG-7Zha4ZH8GxX-n2p71GcbebVofvJfytVBNYl1-nipX4wVISAvG-bcpk5FbRQiAsq1jc3SEXxSIUZXk4Xp5iO8kZXM3Awg3ZAcTW6oEMbgZxneConFuYyzskjge0EKEmm65ri4pJGm7K3e3imvZzubARt49Ht7HIS9Ev3iSyW-r1zxByWIsGZHfws7SEn3QRCst3t6gIJvw9kESeBr1g4J6XC4DjDi9pDdqXaorpI98J2v7QpYCYTHJ2nJzIC6ls1b8ZgB0tVIKBOxUUb3ffnNn_2vIncTSOTOtFAszc2A0eDwMbDZK0ClJFvtwi2qXMJoQhEXb47UBEZB5k3CFfAmy1miHWMdvlHJJJRmLQx0CglQqNZExijz2yzb0JcaCnS-EU9j79XDYxXHQCmCwlaAfEkfvbqLeRg6-cH78AuIYzdnKOIqcGDPdZIRmTXl2A1oQgp4WqQQbSlIb3rYlx5XGo1OXtbOZTtFeQCPcRSVv_PA4gcKeXFyoWelQHq91tVHrYHDudQOIkWQEnDYxzstaVZg-IooHLZipaxcCyMBfpT9VwqJSV4Iz3lAXpiT5jc83NssWq-i8g2cdiEWx6b2u1_nJ_CE_os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم انگلیس به فرانسه توسط ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100857" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100856">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تایییددددد شدددددد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100856" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100855">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رفته وار بررسی میشه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100855" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100854">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چه تجاوزی رخ دادددددددد
😐
😐
😐
😐
🚨</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100854" target="_blank">📅 01:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100853">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ساکاااااااااا
🔥
🔥
🔥
🔥
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100853" target="_blank">📅 01:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100852">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انگلیسسسسسس ۳۳۳۳۳۳۳</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100852" target="_blank">📅 01:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100851">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گلگگلگلگگاگلگاگاگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100851" target="_blank">📅 01:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100850">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انگلیس سومی هم زد
😂</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100850" target="_blank">📅 01:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100849">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af6172247a.mp4?token=UviOqWPZQnc1iL3WNVO6DHFFovprP7Km5nUrKC-Lu2xTaEjOQiM3IWrsaasZ7C2pYWJguuRF6u9Q8Jjkz38--HC2ahjRYmlMH15Vk70KDjkoL0OpE62_2WiWO-B-_TOOGAEAVbiLJuDgNHBbj-bwDiGBmkqVJw6EhNeou5wmK68mvsod0hCKshOsjuIwmJRC-MvzlM3uBbfjBJUBlS8UsMBNU7edz_Z79cuzrmPTWmmTpvIl7XQ_zLkf_kdD0KGngEnS4hbtPJcqfPOcm9J8xjlQMHhEI2DgutcKlMhAq_n9g6ScXrzUh7Uw2buR_-0ak5VxpyNXa2IbNCUAmt70bw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af6172247a.mp4?token=UviOqWPZQnc1iL3WNVO6DHFFovprP7Km5nUrKC-Lu2xTaEjOQiM3IWrsaasZ7C2pYWJguuRF6u9Q8Jjkz38--HC2ahjRYmlMH15Vk70KDjkoL0OpE62_2WiWO-B-_TOOGAEAVbiLJuDgNHBbj-bwDiGBmkqVJw6EhNeou5wmK68mvsod0hCKshOsjuIwmJRC-MvzlM3uBbfjBJUBlS8UsMBNU7edz_Z79cuzrmPTWmmTpvIl7XQ_zLkf_kdD0KGngEnS4hbtPJcqfPOcm9J8xjlQMHhEI2DgutcKlMhAq_n9g6ScXrzUh7Uw2buR_-0ak5VxpyNXa2IbNCUAmt70bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
سوپرگل زیبای برنج از زاویه تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100849" target="_blank">📅 01:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100848">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUBj_KbSu8BXqXlaP05E2GAWzhRl-vJL1wR6dMPQKWiajqaeuO-WtRecYVu7c2L2cwqG_MAMUVVE37Hr8oZ5jXnLE3aKYFaOjUq9DOHNqWjryt5xPcIWxOe-24wbcN0pZmOhXEzmO847w0PvDHmjIObwiQSBx_sSItRBGH6UgfA9jZ8gli3sg1ujkseXIAnZWMFmpZ6YpKBqqJM4sT4dfBlSsSmcqbA7R9wgndMRWXI5NzI-PKiNU2GmmL2CQqSPdiNWwGSTeKoMmq1V5w13fw5AiRXY4sFZgKJ2S9OWxedy908nBoEKmyylRNJH567h4KAPCWyjFloTSpmrrS_ezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیس جدید بچه خوشگل برزیلی که براتون ریش گذاشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100848" target="_blank">📅 01:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100847">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBieueH-d4hjo0GvvXGEiAm3n0uV4wXTrmI8oezpjcUfYoG_2muZqNRjruzDziAXy_7eCQARJZms3wp4SDhtVJ1JmbqqWLR6yq-yrAeDCkRrO6JRJRft_IT7aMyxbd8d99WcseZrYCPPLkLrBOLGxRV462P8ET9mW1pjAwvPphyZUYnnPSnEIHLXYtemOGXC_P79DE3QgPB0O2VnKY6sge20hfYBAlzPET742J18KTBqpob18xRGGftLUPBy3FGYmGaCg8HusZhyJY5FDkanzmm4NUdTN3HpIvtNrPZ9PRLV3bJr838nxOVmKhTpnDUbxlV59W_nUrh3GXLSTQXHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس تا دقیقه 27، 2-0 از فرانسه جلو افتاده.
واکنش توماس توخل تو دقیقه 30:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100847" target="_blank">📅 00:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100846">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چه بدرقه‌ای داره میشه دیدیه دشام. در خور کارنامه ۱۴ ساله‌ش با فرانسه.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/100846" target="_blank">📅 00:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100845">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لاشیا زشته آروم تر حمله کنید اینا 50 درصد شانس قهرمانی داشتن مثلا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100845" target="_blank">📅 00:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100844">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOIhvkNFcy89gvbyjnWIFba1t0kIbpFSHaz82DK3KApkL1ONWnl7IF61l5Z0E8JEEAKVZ0WNCEkGX4ShCGzi31rTOhsZMb9RnvE7fEiS5fUAP_2EdqHJLtCJm03kFPwTnsK2rFZl-IRTZnlfiwVJYTchGumthvJp28l31aJr8943nUwvjnwc7YmPME4ylOqjwiB08d7J3hyOBnUA0q5rtoZwn7X7xxrm2Ulp5EA469XM86aaEei7ZfxG5wcgPjfWSp3TRzV8K6exAcdVDrvy9trRPhMCDW3PRNwhhfA1WLl18lj6DS1ft_9ErkHVPDsYCY1rfVSjeza1B__ysv0Dbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیکتاتور بعد گل دوم انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100844" target="_blank">📅 00:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100843">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌‌دوم انگلیس به فرانسه توسط کونسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100843" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100842">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
بعد یه مشت کسخل میگفتن آرژانتین از تیم ضعیف انگلیس برده
با ترکیب دومش داره کون فرانسه میذاره
😐
😐</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100842" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100841">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پاس گل از ساکااااااااا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100841" target="_blank">📅 00:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100840">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کونسااااااا زددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100840" target="_blank">📅 00:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100839">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انگلیسسسسسسسسی۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100839" target="_blank">📅 00:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100838">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100838" target="_blank">📅 00:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100837">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلاگلگاگلگاگاگاگاگگااگا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100837" target="_blank">📅 00:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100836">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انگلیسسسسسس داشت میزدددد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100836" target="_blank">📅 00:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100835">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100835" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100834">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfk28rWcEbAeC-l6yF-U4QvSzzOUZmixg6VK9AEbInrUb-ZTFz3Ozu0guVyng_re7xfC_YkUwHdCo-vxxURciLkT92JvJQQtNMBJXikehKqsXptptIO81ztdJ9o_0yJ0Mq9nh9bFK19EPipOxcpYPJGVfkPxRBIwjTVnrhrwQ4bNgRn23wdaAL8i_YXOgynhruH-PHYTWFOuaVltw6Bv60YaGLGdbef-AUreYInAG5ckd-cxouiGM8OnPCmAUCmtstsVk4UySW5Dxq2kKRD_2iclbvVHDOre3E6b1oP8ToH2fq_YEkD3NFZADc_ep9rDj346S__uHJShripy1K7BAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساکا زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100834" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100833">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ساکا زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100833" target="_blank">📅 00:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100832">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpLn3KaCGYtngupNAaYAOPKtiHCEznIwwouiNzEkoH_D6VqYD5M2AM9RofGKbGkm1D77gwfJPF9EVZVdESt6cR2beNEIqVngQgqyE3lIZHkzaN8e9e4Yu-yABfOGdloP0ss8jSGNZr0mGDDgvIpsaQkKI-Ah_X6yZfTJ1BsQB16BYG7oWrxAmm_ngrmSrvdabmuUHXJMhjyKiPhOYEcSWPsFheqYGANzLW4fNRPWry7dh06-5ZxL1ys0YpHY6OQJEC25irU6gHWAyHMxtU4EKAG5ZmWVUbh8XQxFHAzxM2-idRv7Y4G5lBQMioTO7u2YdpcMUWVKwpA_J64WCJOTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه:</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100832" target="_blank">📅 00:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100831">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امباپه احمقققققق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100831" target="_blank">📅 00:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100830">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpddfkPXpSWC9xiTJuGNFORDpTXp-DLxs-duSivfD1LHH31Mcs8pvbG5bauSXwlj1b2nslU55c7Sxzut2XGEz_Cwn_roawqHskIby_oGWRIkuboCBUoEwnoTYSXVTwMIwsx1I97_0-c17-Sj57shejE6mpt-AcH57Rl4P9lbB7reEG31uLWRoa04OXHf9XjysO-hd1Gpf4CxGC-OfhhZNzlzc8KKijnph-6m-Eb8aaIGGpUqUVoy38wk6_239zmvg6vyQC5JCjfLpLTYCkfRLu2TmKBvSP_7RQDZdgNiXRsxzEEhmBiOw3OI_A3vf7EYNDJJxRY5rlwxiXZ2tLnYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل برای آقای‌گلی تلاش کن کون پاره
😐
😐</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100830" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100828">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab49e0e6ef.mp4?token=HIeX5WM6WhRdgvZgYnwFdxMPM4UTFCNKkSWs1cUn1zJp_lzW6Yl5QZFgst1zbIymL4ZEeQjdwmjsx9DxDtbQlJgWecUTTgzrl8GbFoi5Kz_R5SwCQaiZKBaWiKo0t8BXRQaCdOSrv3Miti5kqImzpn0B4D6EASXCJ0_KO1VBhi117nk5LjFzE3S6nyCCH9iqD4e8b2UJLOaw5kA0WbJeJVXvfyAtNYsTCLFeeWc8wfiHUCe5OR6Y6gUXQCjTxR6JdnNISEd9rbg5jvUQV3XncIxdYpbCE54zW07EydlX9DXblv6jI5qU_Lve-Js15tfVykerL1VRny12LsDFcGMAyCOo594FJvPESAJ_CyiYGU5kaGXPEdbcSnPhCcXnBOB8MAd_j-W1j9DHJqFia9cQP60JkhcjQXZkxyDluibp6wh5wgOOrW1WpCYzJxf_-BQSP6aPDZiQY-hMpb2SpTwkgVWXfIF6ShuLxrF0dMkGGQQv2k4XWRS6H0RdWgw1JXour_h4giGkT0_4Lqw7ogSFcJyFnhC8EmpiEWFE3MQA8vtybDXmtyUCUVpqGags1XUygg_VY-SzeLNUHxG04WFD5R6dGHb49Jbm-x4SCdI8KD-ID77GIrXAiUzUSAhcnAt6trqIDZ19uLUW2P2E4Kdn7dwAhhJlOHIvwE_K4fqDLwU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab49e0e6ef.mp4?token=HIeX5WM6WhRdgvZgYnwFdxMPM4UTFCNKkSWs1cUn1zJp_lzW6Yl5QZFgst1zbIymL4ZEeQjdwmjsx9DxDtbQlJgWecUTTgzrl8GbFoi5Kz_R5SwCQaiZKBaWiKo0t8BXRQaCdOSrv3Miti5kqImzpn0B4D6EASXCJ0_KO1VBhi117nk5LjFzE3S6nyCCH9iqD4e8b2UJLOaw5kA0WbJeJVXvfyAtNYsTCLFeeWc8wfiHUCe5OR6Y6gUXQCjTxR6JdnNISEd9rbg5jvUQV3XncIxdYpbCE54zW07EydlX9DXblv6jI5qU_Lve-Js15tfVykerL1VRny12LsDFcGMAyCOo594FJvPESAJ_CyiYGU5kaGXPEdbcSnPhCcXnBOB8MAd_j-W1j9DHJqFia9cQP60JkhcjQXZkxyDluibp6wh5wgOOrW1WpCYzJxf_-BQSP6aPDZiQY-hMpb2SpTwkgVWXfIF6ShuLxrF0dMkGGQQv2k4XWRS6H0RdWgw1JXour_h4giGkT0_4Lqw7ogSFcJyFnhC8EmpiEWFE3MQA8vtybDXmtyUCUVpqGags1XUygg_VY-SzeLNUHxG04WFD5R6dGHb49Jbm-x4SCdI8KD-ID77GIrXAiUzUSAhcnAt6trqIDZ19uLUW2P2E4Kdn7dwAhhJlOHIvwE_K4fqDLwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل اول زیبای انگلیس مقابل فرانسه توسط رایس در دقیقه ۳ بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100828" target="_blank">📅 00:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سوپرگللللل زیباااااا
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100827" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
