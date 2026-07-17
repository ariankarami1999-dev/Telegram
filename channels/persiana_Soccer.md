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
<img src="https://cdn4.telesco.pe/file/mhddfIF3UZKE9MMdSea_W9XeWiN2X-PfYZhxvkIO5zXSVO0j1dOYskuhDb0HvGT6H_pXNGgNHXup8ueXqzWKJQ1eHL2Krx4VP6bjyjXIsMIuRw9fAjnwGYgQGcRLX81TlsJ75MS84c87V_-_rDfhcC0KLfLg-QSlotV7z8El8LuyXhnxM7QI9_XLHs155cLAD-dwZlKby8bV6DxTAm_cTuuGekOe4f1qbk88rejd-vwh6p4Tv7yZ8_YzbxUrGZ1WY2Wps145AhpkBs2xUr_CQcVQl4g3VCtMMrjMBJ9quHNIzkwzgpF4QjDQBq27NJpqpaYnzBkCCGh0Fxy8MBgrvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 512K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 15:32:33</div>
<hr>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afb7_k6CXkNJeNl07Ulo6wIh5orl64yQ6Akakp9C9EVY2hwDdNDqjArQKvLdL0UCVcgTln7viitUmiJIyR9iJEnScCxcIG13qSkQv4vXYxYKVGAW36617_GGq3DsRHFL1Mc02Ir54TvRXtTHVnji-6lThYpRKZPukEo_Fal72AjO2YNROITuoGA49Al2OICOKVduf5ksYx7WHCHVQDOWBjauFkCiVfXGzC5VCmrdRGyQh7elco_rS4taUXdf8t9pm8BAGV7AEFyOxU0OpzpuE4yXkheK7nA9SVY2I-iPEfaQiY5FibC_5tV09BC8A-ZpSGtikMwZubUl5t__V_DSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYxwz40VJAKZW-Vru1CjCsxNgwkJHxRycpCtyagqzewhbrIICMLSc77XauC5x2leRrxyZcMmXWRTI6HL7EDb7iTGGKae1-BhZn_JvSYKBA1F_mfj2OZAQkIeeoLNResqTWv4vI5o-wDmMmFgLLVoN-3wpkL8r7iHw61Nzk4_scXkFLPuxP1H0u3Ie269IbhQpeRmV33BAsyOrAVaynSiTabzjy06-WpQnRIo2dXo9zEffeFeg12zKeQAHTltaxz6YH_2uR_jUimbkGqzTaHNfzcGctOi9MFE2WDzQEXUNHdnyOI7-hGysR5O5LhNJNj6yjNBlYkc_cRop3BDZIWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biS5Ywz7qhof6LqoCA3uBVcbZLLNEgnra7vF9UBGG_WVZ98a_FAnLz9PvjRAFpuz97j_UXk-qPja4a4Wxa33BWtFibvvwu42vbpHngN-sg5Jop_T3h-fN7YizaXMqFgwFO5adugI6ttW-AnTtnYg0etOQ0L_wEW3Da0KN1QKgOlOJUfCc5zBviAlxHhIiSC4FKy8VXf_FQSYXX5fg7m1xsUz6kf5YXXDemdmU5_nKrsUXJ0lEZzy_Ayuz0ylqNv69lhnaowKmXQHd6-bsDVmPHKm88g9QJtc8j_gsitdQ-c42BcqkFYdrs_H3i4p11KYxmxMS3vl5fWligHMBtxs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrmhroM3OltksV-N2HXG5Fyu4eEuExEL8qeQ0yEAMbJe0JApxN0yR7A3xizeGZINe5Mt5WhYz8sh_vAhIFaL15pOEPpABsYcUU5jHtYIfRglsO9XYIQAksJSVPLQNdoVixQwxpvQGJVNQsQEs-4khNj4KaKL5rCnbqPLZVbz--qno9n5Z8WQfqEcB1JW8Q6oyPPjmxVCETeIqVdIYEGgHier-8aNeTQqPCo3kNTFZXBNkPzL-U6LRzVi9hNpdaIHGk_VU7DS4buKEeB5t_oZ5sna7hUSlYVkUqxREYtTUvdTLnq9UaQbOutMXDPgxq5hxeF8rQtda0oLRa30oxSkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-asvDoFw8RCEyjgFhXkjFi5aFE-ExDlhUy9Dklcel14FTVCEwd0S89t_kqhRwcAZJDjnhpXIxx1QIYG-BWl2dtjiGywFbPjffnSk1VQkwdqlNxtsM6MB66u7LH-S7r0MqB40TD7rI2iqZcO25cUQOQtBosYH9934as90JZo-JzFVNL5rCKRQhTuil5Jg0yEplEfwNgo_n-dpxybawvL2xxE0J1gFpB3qhzI6DuF_cVFmGDEEb9SiRfkL_8eET0Vnd1wGXKNbugX2wWXxJXD88-nVV1mYuPUSL-9LjR05OJjCMFPDMvja4NhiksBKOyk9U67bYDZmOmcODIaynr7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSfPM6yUx9x37hkNJckB3gvbihuzY2hX0SfmNgLePtCBzDVs30BjwiwtqPgr7uTeo3QydQ_jBfZbHvdicnBeG53EQChFgScu-VjZvdi2XsZVLpK7fV0Jy8hFbNNJuj9EHvNHnbF9QTn74Ol3V0LtqZ4EiGPO9N77oAaAhnTrjerVM_cOLzYQNcnBqthq5x9ADtNDqvDk46nHR8Pz7Ghcy2zJTOib_Qqp8GyFyQi12ZApxJw8ba9-Sgk9Xs2IwUXkjdwhSo7Glk1UIVRXxOtld0UUxcAaeX3PX-qo-NrEfHZqlvgQnclQegwtigWIy1AktGL06fu5Qk2DOQkzOD7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unr3z-bRva4d-mGyAS2zneFhedZ3ovXfsxFD2hU_aSlf_suonjPpVKjIVzB1AsylicMsQ7QxEf0-njUl_Ii4Umw3hko7dzzRGV8v6hvwLLJ3bFB4f8lPNeemLQVm8twIoodGU0ntdfhOAtcNOwGGjpXcemhGFLbbBeTD8swdqD_jZiGu8MfjE5J6zTS21JWT2PeRj6_9T5tqZGHPJarhHRRnMJ0fmMvZO5lP5STq9mod2-tzOxp_u4Ryje7VFSh6Q6kFLfv1cysKdUvsXOXkDRYwVE-6kMYzIPbpjm-ZOOCk04hC5_fusGZ0FkQPkBA6VCm9ra8dWH-zV7qibKiMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=H6h35Tsrnkd1kfTHGEBjYyssC_mt3Y0-MnrvTCnEPF4m_V2H3VNbWdpbxAqTtlR0izJ9CTXT3eB65gzjqdna_C8HC_1SwqcBRrggWBZq50ivfvmHabnzsnjDL569qGBVE6AR1Rk0XVK5MtV1bCiiYnGwoFb481dYRBH6Pp7fbX-QirptEA62Vvh-H2OJ_o_LwH73NvBtGBl5Ac-nRARpLv4FUpa-M_aaNNnefucM7Kz7pbd0FU6mLxmUo9ipq5v2glI5z0BDwAdKzOSr_4z49-VRi4NxH1dITRtRmv-NKuloQdVyNsnTMS-oXRB3DjdNOWloo8rMtV8KQsAKuVGhJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=H6h35Tsrnkd1kfTHGEBjYyssC_mt3Y0-MnrvTCnEPF4m_V2H3VNbWdpbxAqTtlR0izJ9CTXT3eB65gzjqdna_C8HC_1SwqcBRrggWBZq50ivfvmHabnzsnjDL569qGBVE6AR1Rk0XVK5MtV1bCiiYnGwoFb481dYRBH6Pp7fbX-QirptEA62Vvh-H2OJ_o_LwH73NvBtGBl5Ac-nRARpLv4FUpa-M_aaNNnefucM7Kz7pbd0FU6mLxmUo9ipq5v2glI5z0BDwAdKzOSr_4z49-VRi4NxH1dITRtRmv-NKuloQdVyNsnTMS-oXRB3DjdNOWloo8rMtV8KQsAKuVGhJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRwktfwSrdyAjQKbe52zd-JoCOfLvEDh4XgTZc8FYt7_pXkNsA7RaraxkiWoZHedkWMdtnbZLpP1RsVJKC9cWylyqzKp8oCpui56Ac-PQZrd-gsqiDQJQ4basDN3YI6ZGFPiRgJ3s4HKjAZXpu5JdpBm6I8oU0vVQOQQXh5xcF57iCN90qN9D3dKxQCaYdSLWeFb-9S3f0KaTpiX-PH9i4cfu9VJr99xROewrSczA7WZn3SeViqShvYXqpxn5ugYY9vaWwTThPhLcBz-zpCQJCejtuQWypQFF9sXvwW9p2Zm2lG2KbCDb7Ew06InUxleS6FjFzYj6mtHkmrENTYWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=ILS9XgTF5nimT49i7Dn7z_8DAgRS_HzpzhhAW4FU6qhCKULRFfAclk7-FYfe2RLt64YPnugZdxUvPpgD3kqdhEYaqyw78cLg_-YUCHvtW87FwJz5aVKHLdGxhx-3LsZXB7EBHpSFhQeL3EvC-bZCrRKago1__mOLDYEf4yLoMnqytwSoyi9NnR8gps3EEIAL9pdtx9_SG_vSS4QcQiEHDTnWBlfCqJNiiKf2bysiJALLjPqGLuYyjvygr_caqclXk2g6lzCg0SqmaNGhEU4aUA6a0oWtYlaY8X3OXuHqQCWcFxHD-05mM0T8kZAy5kc7O0PDroHERuHzC8rb0YlbLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=ILS9XgTF5nimT49i7Dn7z_8DAgRS_HzpzhhAW4FU6qhCKULRFfAclk7-FYfe2RLt64YPnugZdxUvPpgD3kqdhEYaqyw78cLg_-YUCHvtW87FwJz5aVKHLdGxhx-3LsZXB7EBHpSFhQeL3EvC-bZCrRKago1__mOLDYEf4yLoMnqytwSoyi9NnR8gps3EEIAL9pdtx9_SG_vSS4QcQiEHDTnWBlfCqJNiiKf2bysiJALLjPqGLuYyjvygr_caqclXk2g6lzCg0SqmaNGhEU4aUA6a0oWtYlaY8X3OXuHqQCWcFxHD-05mM0T8kZAy5kc7O0PDroHERuHzC8rb0YlbLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuB7Lo870jOcZb50bu1Vo58KumfxWoSD-Yh7kjXx9wQIf6Ga2QV837EKTcL_AnXTUF0idw8CEdc8KUrjtvamdlWhcEPRoZRnGUQo42BKb9tvDStEI2iCBat0tIIoXqg-tu-ORDW4jOdXZOBNUE440HlaVJNocESV4MynO8hTyEimPx4BFgt4bqf4zgLO9LsZgnfhboAA4_0d53fKamZc59NWumCT_HD0hMuXXp0-bPmSS2jTPW9EKOXbd-zrzGIOKBdt7wylimFiuMWyYr0t75VNdTa2V2GjRMBcL5UhwMDrxL-xc4Js5DdCXFRlZULO1ERVLmc2wpriASb8c3_whQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epQydzNd9EDjoDb2RPdC8iHTJ7qhWlUAFyf1n7YK6-1GJYmZiQ4KD2SmSfWjPzS86Ky28bf2TXGOke4Yj7Y4TQybUBiZiYg-66VSy46lwe8r5NeehC1aJACiW5Ma66Qyrnq_Nn_WwjJjmVPwwNAuDWsP8i9QSngNcvHDcr2K5fNo4vzxVk2ZAZoEkjKO4pizW1BGk1wifzYVUrK4jBpFlDmpRhOOzJfliRMxkhw3XbjOBFYHGnaldL3pTi21HfpJHkGbKCuShSuh6IsUH2Sea3VGPGV1GRGtrBA-MftOiP5vPNHUBYr5ioMx32cx96IAjcu2_wIC9Y3uM64qDKkUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polHdQ935e_pGQv67DLjP14UAZLTUGvokZKJcjn_fNLIziDmoAZg1sDPxKSIxfO2Mc8tSCWIFPDl7PJJTHa_5izIpNd7II_-iR5lqRLiwL7rD8lvnlhF3cAIbkQAHIn84c3iu36qsqZTKbKhgGOKPbHCqzBePngrsg5gxfqmYvaBELDWPV7uauJfmZCUHkDJhITPQP00fIByJrf1x9jk2N-qspE_HSG7SPd5mhBAZC0dOVB-ZDyKZ3uXNElgjT6xNjBxUnvdy1yl4BALOPiTielEn4qyhjAuV9ezpIeGVvHP1gNf6clOGCHTOkUko_qeCO5f755ok5LId3DoJiZdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHaH7sOlZTbg7UGZ68QquuZ2zkymAw6AKGIGIJrT0px1lNU8U77IY17s4_o4LwgaLQpoV4BLtsNS_piiosA0S-UA0X7VD2Ldu61Lz3Soedmm8u3vzhrcMSww41x1o3GQqBFs2vmsM-_RyLmYZmx_bHfcdohyVFmOpa5jIfuuLyTfAX05DBmqhbw7actU6xMvedo0GQewbxqhlmTT7YG-AqXkMzFf9m-GGwDgJ1o6O6luWeXX5Z2M9cKmsX8QNckhlYT2gAspiGN86N7m1p_QCJWwtJvK8w3IuyxdnAOfXgxEhXrKh8hGxbnnSUTkLb5Cl9rnQJ6M-gz8ThAJgVbNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPIX-1M9xIfafJz5sO_zlFDNv2vQ7yOQMozrmPvjEFdGgj2b2wiFypFqmvDbtrT8aOxP3av9TQ6fa2zXY-k6TIOemG7d1ZgPg0wf_8aIP8Om0phXg4aL8CE-TPpvfaP4unQPhL0rTuHjqiYwbWNV_qopfaG5icDx6pYpv-IkfaLBslrC8zlNoV39OtmwraVMShVunAkZ1L_jmVUm5zSEgpCAO_j1mGuKYjN7EPm9Bif5xT5aHrkOeT8c0652aLRRGK0s8agN57TXucsD968wA3ub_f0vbJjmsD4l9HLivk71ZnZIVUq-YQveOGxA_mV8zz204Esn-92Fq6-89CWWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=i9SYRDD5NySkn1-vIsrrNllPeSZEeT7WvNglD3ssESkxFlAzdJPBYRe7qQ8sQPMxpxVsoJX4ODCzxT-bJTeR8rgpZlku5I6HzLeXBYoxzVGv4MYkYRtNWisSus78iEX6d_L_1Lo83-JHo50dT4PbOMP2z0t2N3ddfIZ56ifeeDmq2vBqOg8ZqOvm0nKeTfyzX0nLZcwPVWEfuSudIYuDv1cEKXMnNgBu3550tO7a9vCGMO_TJPxheDy5jmKE8QjA4la_lM_ge9f9S-aRRnwVQtBQgpkXYu8rrXA7gA0VRriik46KtnT1vDK_uJBh3uWOspyuZjZlaKoXSYZj5bEiWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=i9SYRDD5NySkn1-vIsrrNllPeSZEeT7WvNglD3ssESkxFlAzdJPBYRe7qQ8sQPMxpxVsoJX4ODCzxT-bJTeR8rgpZlku5I6HzLeXBYoxzVGv4MYkYRtNWisSus78iEX6d_L_1Lo83-JHo50dT4PbOMP2z0t2N3ddfIZ56ifeeDmq2vBqOg8ZqOvm0nKeTfyzX0nLZcwPVWEfuSudIYuDv1cEKXMnNgBu3550tO7a9vCGMO_TJPxheDy5jmKE8QjA4la_lM_ge9f9S-aRRnwVQtBQgpkXYu8rrXA7gA0VRriik46KtnT1vDK_uJBh3uWOspyuZjZlaKoXSYZj5bEiWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=rPyP6vVenDLlfbkzbKkQytSsZTVhv98nzxOyctHGzySEMGbquIFCXNSq-I_h3efZa_aLrDQwU8KG0r-WpbC1rDEPgCzeeksxLJMTbNJHpWIVMIV4kaQHPkdebAWoPossyNma6tcerINeSz_KoSblv1NSJ-7v5V1Tk_8HkH4PkPER7xGKCzNZ-0nwXUo-E4KrLMy13tLCCLu1O29PPsAxbGzkE6AEmLesbUcrU1Z294ZWunCJSpJfb84RpPi3b8FhbAiyWgIDzGtkfuCroQ9LPbY1k6x-dtaLFCVQGiZd6WLXuG6vs1Mr3DiiW33Y61_OSxB_4bY9F-OG2pgbn7S2L3BXblxB-SCzGYwTY6WLgzVWTE8aat0mAb-MTjhFRjR2xiUZygFr7Gb_5snHNaeX098CPWmH9kVQ6I4iBOGWMxjde3zHAk2pho1QOnipUljaBJpCxJLuv7GJl50GZucQOd6aAhgJkazAaRqQmWrkdy7RfX9LsKr0EzPQfNDBhgP5tNGLHIUb5346txXeDG8pCpzDtrvE3xQsigY03alTkYhhzDvI1IAfzQpH-frjYI800VZGD6uRPulZdVQuvLvF7g1Och0G39rxnRnUG9ikrzd0A7FBiT4YIEzjyjpK1yWzz60XB1aPmCI9OyKmu9zzVPnq-SBMp2A5KfTDXQYjcWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=rPyP6vVenDLlfbkzbKkQytSsZTVhv98nzxOyctHGzySEMGbquIFCXNSq-I_h3efZa_aLrDQwU8KG0r-WpbC1rDEPgCzeeksxLJMTbNJHpWIVMIV4kaQHPkdebAWoPossyNma6tcerINeSz_KoSblv1NSJ-7v5V1Tk_8HkH4PkPER7xGKCzNZ-0nwXUo-E4KrLMy13tLCCLu1O29PPsAxbGzkE6AEmLesbUcrU1Z294ZWunCJSpJfb84RpPi3b8FhbAiyWgIDzGtkfuCroQ9LPbY1k6x-dtaLFCVQGiZd6WLXuG6vs1Mr3DiiW33Y61_OSxB_4bY9F-OG2pgbn7S2L3BXblxB-SCzGYwTY6WLgzVWTE8aat0mAb-MTjhFRjR2xiUZygFr7Gb_5snHNaeX098CPWmH9kVQ6I4iBOGWMxjde3zHAk2pho1QOnipUljaBJpCxJLuv7GJl50GZucQOd6aAhgJkazAaRqQmWrkdy7RfX9LsKr0EzPQfNDBhgP5tNGLHIUb5346txXeDG8pCpzDtrvE3xQsigY03alTkYhhzDvI1IAfzQpH-frjYI800VZGD6uRPulZdVQuvLvF7g1Och0G39rxnRnUG9ikrzd0A7FBiT4YIEzjyjpK1yWzz60XB1aPmCI9OyKmu9zzVPnq-SBMp2A5KfTDXQYjcWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY2MKYIAXiuARXdtk7km3z6Q0zFKNOCOyRC62mnSzXsJMzcbLnHmmiuA5v163Xcen_nq4R1SGDLGYnsc2y4mCzFv_J5lYwT4YkpUgOjpsjq-6QPRdKnOGz3z6hwL0If72gT5r2GvNVSRP6szYVu3HVS9IamTitJ_GIbjW_Khft4MVFT0KJlSpcWENeOOfeq2o_Ja8NAcFf5uhuHUezOSGdOyAZKHwbhQ2IY3j1EXcyrNcE3iMnm2wlRLC3F8JCy-4OHt_lDx7t2h45Wa8joHfpALzw32M-rgYJbep2NS59YMoZN5j9_Qz4mUvEPhv4kutVbmzrOURLPYlnT4fJttkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr26
📩
@winro_io</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25912" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ficCt0PD-5C9tJRZTes-CL3upWOzzniZonKoLLX77SrgQ7CrSqmq19MeTEsvf3F1sJruMlQmlUDYi2I6loKP_eP8f2J2M7NPWFUKeJ1ZMq6T9TT3SySWqQHEgnmwxq0TsEUVVN_w4Y87WjP4YMG7Blp2SxXY7fHTc78HsMXq8UJOU3EEfrYhcdmFlxTRVlPabVU1lKYkyABCPo1YxFpoLYTi25AIclj7TasEE2bg5QUjc25cDjoTGcYExyPr8a2j0pg4StF24cvsnNRubp6mrFJyAvRkpP5O3-1j35_TAki5M8sTmqYq1hFHPLfHRAZSQFsLSWWW5xuV5TQOpVY3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=RemqubOsOavW61tQqKP766Q4Tg16LksJPAKfY1lg54517rpaNJbLchr5H2uF-_PMzUb9nu_c_UASogcT3dPYK02C3cBfGShSWHMMikT82UzawvNJQVNjy3SrdKRdHcnN_OTXxGhirDs3QTWAI-_hs8JwYMWVrNviA-DjoFpUxmpLMMaiqWJRkVonEchnf3UwiHXgbSDV6F9y2MsZbkU6qsJ2gRrN9SNgLcv3ssaxsoKC7-sOtfjXHIOmf3EmzfWzxVhuISZ9Og0vhMflmJoSs-lITo0XiVn8Z2_3C-el5t6a-pR_QFFFONZk4RK9jZWQbfwGAyT5q9E55E6nxqGVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=RemqubOsOavW61tQqKP766Q4Tg16LksJPAKfY1lg54517rpaNJbLchr5H2uF-_PMzUb9nu_c_UASogcT3dPYK02C3cBfGShSWHMMikT82UzawvNJQVNjy3SrdKRdHcnN_OTXxGhirDs3QTWAI-_hs8JwYMWVrNviA-DjoFpUxmpLMMaiqWJRkVonEchnf3UwiHXgbSDV6F9y2MsZbkU6qsJ2gRrN9SNgLcv3ssaxsoKC7-sOtfjXHIOmf3EmzfWzxVhuISZ9Og0vhMflmJoSs-lITo0XiVn8Z2_3C-el5t6a-pR_QFFFONZk4RK9jZWQbfwGAyT5q9E55E6nxqGVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=e7BA2dlp6XHHlVR3Pu3vmjjQwuBD_xhrG_s6395RdnuHIRCBK0qVqA3M-My27NehISwCbMW5pgqa6Z84pODvISlr0qYuvRecgJbpg6Eadz7laC6ETTso5643BAqg06dHtF20M4TDyO536rYGR8uyEo3fLVpC6AwodV9Gn44Gb3lvvF2WihJIjEXi3Gg5r8XtN0jiqiT_my_yV23F5PBkVseoCpG6cD_y_4T8MZdugj8-eIM-Oo8c8rHhvw11h21xXPuLzX2ekIyg5nI0IcWkvH6y-_GQyPVL4ndSFEVh-d02WH0exBDt9SfiOfLvRMkyQ-uCtSncnaxDU2pwDG3BUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=e7BA2dlp6XHHlVR3Pu3vmjjQwuBD_xhrG_s6395RdnuHIRCBK0qVqA3M-My27NehISwCbMW5pgqa6Z84pODvISlr0qYuvRecgJbpg6Eadz7laC6ETTso5643BAqg06dHtF20M4TDyO536rYGR8uyEo3fLVpC6AwodV9Gn44Gb3lvvF2WihJIjEXi3Gg5r8XtN0jiqiT_my_yV23F5PBkVseoCpG6cD_y_4T8MZdugj8-eIM-Oo8c8rHhvw11h21xXPuLzX2ekIyg5nI0IcWkvH6y-_GQyPVL4ndSFEVh-d02WH0exBDt9SfiOfLvRMkyQ-uCtSncnaxDU2pwDG3BUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=BTKegEayNS-sY-VlkgllDL0j6oqa4BlHxaH_bgMkOwMHkSvyTXL37ucBFwOsveG9x_d5870Jj8vp7f9mLcy-3VbEK1M9eFqZhFtFm6jVwyMQ9szBC5ucUzpn-To0H1JuMOY-7obsSH6f9okh3NA3R2gq6oZa3fun4PL5TC0YM4eCrcf6h1kjilmJucvp9zo3Fl5tXfLuXMaY45IfraUPtFOVGNIR-axOLYdFeCwV-lXPNapzcSaMQJPhjqExD6hSQNkUoqv8fO-kJXF6QaO2oicEgBeW21eHRxxZqJyjQ-lF3HiFjnJklP-OLwfunaNsH_2gv2rMEXnyf-uTdtVKSL5-dEEkBqsa03stfr6lsr5qSAIE232I95-kfR51utB0s4-TNG3V2iSy9iPCPwzZZSBmri3f-W6TArJekP4y3ne6Mj4cyly55UT6kIbjzJWPUnMBfpeZMoXQznN-pAn1N-IQqghQkzgNGdJt9J5IFx79Kxz05hGM7BVCGFGeb1kPK9EwI6XJveLsBGbgfVy16SAbBOd5g_g-5wUYUZSmSG-43r4MvfrpEIHKWbRq0j1v8T9mgCrUJ1GZUSE5WhOZJxvMWdcRtbbxlQsimwOJ62ReON0jHr-t0AOQIJXVCY7TJHdDe3HxyXhDdrlFg9KjbV8AKdZbpZN_MjykGZknRNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=BTKegEayNS-sY-VlkgllDL0j6oqa4BlHxaH_bgMkOwMHkSvyTXL37ucBFwOsveG9x_d5870Jj8vp7f9mLcy-3VbEK1M9eFqZhFtFm6jVwyMQ9szBC5ucUzpn-To0H1JuMOY-7obsSH6f9okh3NA3R2gq6oZa3fun4PL5TC0YM4eCrcf6h1kjilmJucvp9zo3Fl5tXfLuXMaY45IfraUPtFOVGNIR-axOLYdFeCwV-lXPNapzcSaMQJPhjqExD6hSQNkUoqv8fO-kJXF6QaO2oicEgBeW21eHRxxZqJyjQ-lF3HiFjnJklP-OLwfunaNsH_2gv2rMEXnyf-uTdtVKSL5-dEEkBqsa03stfr6lsr5qSAIE232I95-kfR51utB0s4-TNG3V2iSy9iPCPwzZZSBmri3f-W6TArJekP4y3ne6Mj4cyly55UT6kIbjzJWPUnMBfpeZMoXQznN-pAn1N-IQqghQkzgNGdJt9J5IFx79Kxz05hGM7BVCGFGeb1kPK9EwI6XJveLsBGbgfVy16SAbBOd5g_g-5wUYUZSmSG-43r4MvfrpEIHKWbRq0j1v8T9mgCrUJ1GZUSE5WhOZJxvMWdcRtbbxlQsimwOJ62ReON0jHr-t0AOQIJXVCY7TJHdDe3HxyXhDdrlFg9KjbV8AKdZbpZN_MjykGZknRNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNaPvHacwpkONmEjfN2bRCaVKumIQEdf9e1u83_jpMATT_27AwNhN4xfRrfesUecteKDdSHczIwZv1U3aoKtR_IwG87eotZqVvuVva0yhvCON7mCwK94GwCoOTF3r6eUnG2o51rBvLZDwwftp7AagcMWIcU6mJSOMK92w8J8CwILnZ2vSYqpXwzP_I_hIaWsDxEtjeWvKPhGZASEYQ8qP1NKkNv4BBCqyHf3sStlqDVlFuSAhtNaeJqHy91wqUyMpOjlGhNiWBiD81aOL9TWZOwunFtZ1zvYncAVvrizWtW72j9tuc-iVCPUJM735CXZ2sSbFKRknGXBeCPXfjY-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=lbZGUJ1IE9vrXjDzZ4N-cvmW1YMYNG3jDf0GjoEXv9MI6DNhXcHePSTYt9TDnAJDGelM8rAQFWdK2691YBoSY2Cyz58RO2jnOFH0sR8wPsH9w25konzl-D6nrZRpPqoFuwaMrBxZdl2c018Y6pHtA9H30joHV-VzRiQejSI6m2DclFyve6Z1a3-60LpuD4OqY_kEcdZ3jVFJivYNy049a3TcKW_V9EzEATTK3JP5QIGNjSCv1tV1uUCgkbdY1056ObdfBGGr2exj3AAlFOjk3dlSOvZ-pvcHFEJq8oLCOw3_MGO1Vr1CdPZ2KHGAKpR_sToEw6Ak004y8_JKlYeKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=lbZGUJ1IE9vrXjDzZ4N-cvmW1YMYNG3jDf0GjoEXv9MI6DNhXcHePSTYt9TDnAJDGelM8rAQFWdK2691YBoSY2Cyz58RO2jnOFH0sR8wPsH9w25konzl-D6nrZRpPqoFuwaMrBxZdl2c018Y6pHtA9H30joHV-VzRiQejSI6m2DclFyve6Z1a3-60LpuD4OqY_kEcdZ3jVFJivYNy049a3TcKW_V9EzEATTK3JP5QIGNjSCv1tV1uUCgkbdY1056ObdfBGGr2exj3AAlFOjk3dlSOvZ-pvcHFEJq8oLCOw3_MGO1Vr1CdPZ2KHGAKpR_sToEw6Ak004y8_JKlYeKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=KTZhLVcTAPthEMobUczpJo_QlTnYDs3DgYZkmmZhnCW6r_hoGus_mJ_eNxOVaai8IOJjQoiPi0XKwoslY-eJAu1K-J4Jd0fS77DzeUgcO-ttauFRGDa4eB61IntgpZUr6lV8FarZEsQca8Xjjsspznzx26zgzN0K3GHQE8-MhE-d5XAeeANB51q9-I3dLJF5FAb8W1GgJrvRj30nLolNqT2olt7vKMHS11uS3XIOeFm498Y7J5kxzKQMDA0s1333EzXPVTwYaxs4nszkprLhwWW8afH8fFaoefdFbFaBw6kPBzoKMz1PK_ZNy7l8cH-Stv4uIH7sMDYu3FZ7H8niXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=KTZhLVcTAPthEMobUczpJo_QlTnYDs3DgYZkmmZhnCW6r_hoGus_mJ_eNxOVaai8IOJjQoiPi0XKwoslY-eJAu1K-J4Jd0fS77DzeUgcO-ttauFRGDa4eB61IntgpZUr6lV8FarZEsQca8Xjjsspznzx26zgzN0K3GHQE8-MhE-d5XAeeANB51q9-I3dLJF5FAb8W1GgJrvRj30nLolNqT2olt7vKMHS11uS3XIOeFm498Y7J5kxzKQMDA0s1333EzXPVTwYaxs4nszkprLhwWW8afH8fFaoefdFbFaBw6kPBzoKMz1PK_ZNy7l8cH-Stv4uIH7sMDYu3FZ7H8niXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPyQIbhUlMw3va5KLg9T68ftGr3921_SruzpP03dz7S1HACfYA2rAiEbh3LV_0shLs0MCb1GSif61-6KMsfUBFrivuv5OZiJAvTekNwSNE8W_GichLX69lViaViUrUKPmvAAXPhbqmeCSSe3qtxEw1h5uNC9bzRk9V49v4DYQD5_HvR1_yAsVLDeqdC4c3b5LqtGgDCCwja4dwKqAdVUyXI0l8HMu6PPAhc7k-KCh7OPpfC-fjhQdsC4GtHWH3TBq9iEAQyVVqcnmK5uIzs5MIVFWh-P_yc0QKpxwTNnFys0uRfpifGC48u6MsolrMjU5WG4HpseL1NrzBReezzwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3_RNVqRgLPGZzdF3adMM_9mBb3EMhKQq99700pW8Ac0G_wibCsoIaDLbMt0OcTCB6APF8CA9f_buyUQ4yr97XatakhQNUFvuTyIEoxh6N431vs-BLBti_LOeGc_zdkqEHgo0bVJSlzlEuLyVT05suvvpAP3ToPCKYb2DDA-_jorBekxKaHpL9xKrHT6f9j6txRSTd3pcZ6kKVVdt9q7kI47wj9aURYu9CpPlonSmto0sl58Jibdsi9dV5O826PMtd_3fqak2b88I6-vWSSjEVFAau0-Myo_3pfYsSLTkL7OpwbUw3RLkQJkGcwHR8219NQnDuJ1OLwEoASniLhIXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCNqxZPG_0Uc8foZxABW9jHZDKdE2nvxaaxGKdpmu2OngD60yua-2fNik_Y0jcDikc2_gfBL28ZxCUqzOtrfh-X1QINeJ0C60rc9Inph4ErbFpvfZxsGYv2P1Axlxl2eU0i918DCNlrIzFo7Sj21ns8asAtumVPwc1Enc3DN3gDNbfMs74bg6cMHPCdk6fuKaA4oti6u35wzT4Tzx3sv-t7IK9FFIh3UUDVIXDXpE61HS-9LBiAr7k_LAuyEW9cvyoSwGsvUuWJM8JqNcw5pdnp_lNe0OY3Zcaw7j_s7xAXamPCYngPg5mx0bgSDABeRDNPZnRt0UZVqc7W61R9x3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1Z6oWxCPqa26FJ7zd_6zGsGlRjIDoP8KeG3EqimPjhPfPR39a103BhbsMtkI84F0i9JfbZbL4WVW5DBlG98aRWKCexOW_hDCuDVs2ERTz53tGFqyHWtzMHwH3oyn6BJEnKvo0iWfFonNJBGDBD8D475znIPZt2mrleG4-vUexnZg265xk0_fNelhjWxJHAci0bcGBDr_SSSPRJJO0AjR5Ri3mc88aTXYWTj_Jw6w4IUpj2Azn7jCEsZC-qRX-Kq9giSRP58noMEEQlCwaJBznUH0EqvaGMXMY9kWv2LFq6SBWY5OHtsmXKD-QEOpDPwyIjZ36yZPTc_B0IrNR0F-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En15T6WFDAADPb09wlyLOPy3hluChgq4efIv8E9oi0JKe2g_HQ-u5tx4L5Mn_fMRm2-j3fXrZyQHlmBW1Jqo9iljk0C7883fvhl2rgSucW-tjLLvZ1gmBAhj2ggHRjXKU8mYvxhiV8kdRZrEJHz-9N70N_9mq3ML8JifOmmEkcnxaQlld4fhha6GQQfF1eOfjanOfqj4jVWayxSmBh-uopd9Ys5p4pc8ORGVql_cH-lk5eonjN4RgQHAHkzLhewFnZM21kedr60xEVbRvIbTGxgGGT4fHwzy_b2xDMmXd4Kw1yZlyKftK7Y2h9DQ1yh3H9hq28PLn1fKGBnWJ-KbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TULa37vp4qsL7vTbj15a2hrop8b-4lMX6mLivjo0wCB31gqAbmIAnbkMaQjJIlgO6RK0Gfa1qGAgTkT6SPCnwHdVbm2ggyhLHOnfrRZvfTPo68cy2GQLGU8Awv8DarQIUbcsNuDprxLLTBwBoQAvzcR-REi1kFIpxzycwq7vdVS2am_rmCKf4ZpeSkJnc01ehDr81OHb8swkJ_T_TLujbYC6dLpbapL9326hymtfvKf5ZiS957a_LZZ2Ao4q2wk-RIHTn26qXYcxrrboPfvisPjsJLayvmUQCuSMopY0Ku8hC5por1X3iy_N7msVi6TM5fbJ4qeRqJpI7HGZybGU9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=CgYQUhIICDLHn8-VR7274BwlynJWwVsTefj7H05YI_G8E3F5McMwhcasjO_EZ7TkCbYFhfHxKJXr1bI0OQOIuuKpYaAlL0D0XpjUNdjgGg6kwylTq0kTZYHFNYurMnKg1LI5XiJ5v-X8dzVO73hEiJO5ZSUJ50MCDKRi7XzT8lSpYHApaILqCfD3w-dCulhAy4iYhaxm4D0eNScnamgoFD3VB19AirxMIw34sA0Yi2iVnjn40KyXkN3bzutATM1-oF-ThkRFSMnGX-6EFYIXvHMjJGo03WeQnocC-EL8jpg1uYNddoSG5e9nWASBllVvT3UpccF1TT3AouIwahOqSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=CgYQUhIICDLHn8-VR7274BwlynJWwVsTefj7H05YI_G8E3F5McMwhcasjO_EZ7TkCbYFhfHxKJXr1bI0OQOIuuKpYaAlL0D0XpjUNdjgGg6kwylTq0kTZYHFNYurMnKg1LI5XiJ5v-X8dzVO73hEiJO5ZSUJ50MCDKRi7XzT8lSpYHApaILqCfD3w-dCulhAy4iYhaxm4D0eNScnamgoFD3VB19AirxMIw34sA0Yi2iVnjn40KyXkN3bzutATM1-oF-ThkRFSMnGX-6EFYIXvHMjJGo03WeQnocC-EL8jpg1uYNddoSG5e9nWASBllVvT3UpccF1TT3AouIwahOqSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbZTEJOvAve_DeK6MdngYPDoDLCjXNc7a8I6Q5VeXilDKw9jFf7_vvxeeJmDHxGUY-QrRC90btukKsoSMdkp2hYxJiZK_vMgPH99McyBJt8h5Ck-oDHq3xFoWpKuFbksfSZSvSQ0m7IpalAQ6D9QZAPwIs5icZdzrvYp2awmAywz_r8B1G4xm2Czc6Egh0w5QdhhAivDJ2kmzL4dGbMfZTbvCNVV01vD6IxCSTQkBx2Uoat6Duu4GOt2t6P3fL-A1N7-V5MjHgmvSKvkStnluR0ow12-eEM9NkVfvqhgAcSShIqxKEtJnx2hCaCeG4-58u1iykGJZKfTDT-pXYFMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAQd_ESjnt1p9FIv1zkWHX-TB8K9os_vTr-KwD_C2-Aa7Bex6LntjKUO9YC2c2HkC4ZIxEgDiCnC9vm8JsDk1b00JBLye3lC5JLkOb34TNUuNx1QfzzdqjCfq4KUPK54tOeBjpxSUQOUJhbpgMuzBfcxdHA7RCpRY7EZXtgr4iyzKaTo816ctPHzm1Nq7PUCRIK2EkPRVYTbz0jBmspnesBl1sU9GYyFWkbXmbqUXe1RBpUu7EF_JJvreSWRLYFRGRODPutcKmkY5clYxG-u0ErrMqWaRDKqGSIfhGN8WaPvqusou7cB5VQYcVbtPUx5KP0QEBqDFFWxwRr-N5n1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-JQPybbvYNRB8yX6MUEbDK9q3p1I1z9k-Suav1DerDtapY00NqEFadKy2Tm7e_2XwIcuLjDSEFVglMzu3TuxxibJNa7EfX4zmaOViJ27_tBALy4nH2RImgh4ada1X7eJHYirHplKT3kg7vWT1fJZrRqXF4hvG2BCzdiZ0m5EnkOskXpoocB3es1JsG6-5_X3TN9O0jfYnamQcV4JqDckihwUZG6jVJfqMG3d9t_dVexh9JkJlXO8jWJhyQQJnWJESclIH4ohZgmzrq9n8qjrNJTMWgExdM7xXRubJTwYvg9oGTTOY6EvnKm8JW0y31uyL0UznVDCf-_ptP4EzAu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anm8LmrokRKhiTGpiTAGvyKplRmfhL9SHipoHT6_0hmfXTfEVdwjdcHCDvotxpb06rfyNETVndDXRcZq52D44bnhY3O-eX_qT4goae90YiORGgUMuSZ2a2qD1V8kZ-u16-43-wOIpj7SJ8ST3ikzwPGs0YYyauUbOhMm2vD3XxYSUHYEXskHbV-Sh7MmRxNXQpI3d-eeQdzQtpJTCYLC3ksGTP-4PQVKi5OOcUxiNf6Op-iITs5UhtLTeHNEGxSz-PtqRRtIPht2rp12vPFYbQOVVLkQMxriBDS9SRxwOQfzdudxjmm1MBjMljK3X3cgouuV7fUdMQZDQJM53cZAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgJx4pTwn0hZEPrkjLrFgw8EAq_0puVgnZVknh4LU-Su00gtKd7rj0kXdMqbmJH0w7RWQ_mFz_Fbx5PXAoMs1o9TJNRBt3w45EKhtAwA7hJCQCUmkf_FNREqfpEWnj65CfdK9xLRqqbp2HfqoH89gYjh8I3jYLFHNa6wMaOtHzSOq30DqV_UHRUWk2lTObdLC9vzUyzo-Llmc2Qy0QV2ittrp4IEt3b5WyfCb6fVI0UXsCjID2NTClreBkrJlaMh_PakYst7hXhC_2yaj29pls-qfdD6rJ765GE7-yuQJXdnQwbuVqDKdl-LRiCBvAHTA9VSRElxSkma-OZ5_EV_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsG0AewqmIU-uWPIdhv9tvnFMBWAqv0UFT3lTT5oAHU0xOqqD3iAEzVJC4o0fvzPyhi95qY2MEl-ROZRBiSBLjJbYxl53bBG-p4-iY4ykUq7qK3sEED3WSGpYG5rs_d5EYDBi38cHrGz6RN3NjteBeklnddJ6AuuvM-zq8z2A-Kgl2cx8Q8UH0fR52yl0WIGOGyz6GIxjV3TW3ANHUP9dHUFjUr8NIFmSYb3cywznRY1rVcx5WsOqJwxYsrksIw6jR6nMhnZdw72Fsc3lSyCM9C6T-W_Gei3azz30R97Qnv9WeExgSrOkXJjAMT_2wcJLj5tzgfjRaLFYJB9D5AHeYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsG0AewqmIU-uWPIdhv9tvnFMBWAqv0UFT3lTT5oAHU0xOqqD3iAEzVJC4o0fvzPyhi95qY2MEl-ROZRBiSBLjJbYxl53bBG-p4-iY4ykUq7qK3sEED3WSGpYG5rs_d5EYDBi38cHrGz6RN3NjteBeklnddJ6AuuvM-zq8z2A-Kgl2cx8Q8UH0fR52yl0WIGOGyz6GIxjV3TW3ANHUP9dHUFjUr8NIFmSYb3cywznRY1rVcx5WsOqJwxYsrksIw6jR6nMhnZdw72Fsc3lSyCM9C6T-W_Gei3azz30R97Qnv9WeExgSrOkXJjAMT_2wcJLj5tzgfjRaLFYJB9D5AHeYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUWqcfVnmGl5TwIu7bvbOWDEffMC5uc6wrCcNoOYd9Ou-tYBF5GIN8txhs0okxtCScqEK9v3qzRuzZsJgeyjj7_Wq9O2AYx1AIvERaoACCMrW9sTy8sHF-7PkI2SfkuFPhdPeeNmJ45bmEEPRIRtcvyR3Kj0ArgYP-k5xaTYt7bECc9GvfpbhG2gJLHYdgBZbZO3qj8fBsM7_TqmKFR5roCV0bneVBnAkoLOepyBx1Q16bLiRXpcxAJCsGTvTyXeAkGV3da1THSFlCKmnW8B9Vyfi4SVzJgSul6JIeCbMOW2qVGVGvIO5kLwUfH-Si_2IKrMnO23gmDSJcZS97VEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF52F6v7MPjLFZEnIFHIyQaYZ47YYdbelVpev4SLClFx-0oMFvnIheMP5F7_ORqmmsu5NbjEyCh6fx-1HKTq7_kuq5_4iMnSJ-LJUnhMmYLHKNDaZ9-VI2F22aeynrM8PTQ8WAm9uYoF2Ais1m3FQvoGfZpA_Aequ0DLTAV6ODQ-_98jceX35uTuRD5JJRW0UscxlbzF49OrbMkfHglF1xtIG6rVBaNtOWCmf3aVe_Qmr1lrMJJXEXHIgddJ1Wu1emZCtepgWj8L6AAZSce3CLADHxgisWFXYjxcBFrlWzuvc_BDpiVAMZc3foe3RISC7xmyQuQGePGaahPDJySIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ct038Oi5BZT4Wpt9cjnypK8tR41JfONxCtRDY2SQhhUl1Hp4uiaGhfnfv9z_CfHypONlhE0-uJV3vgBO5NCqax3I55n37zfVC8qSGlR7QuPqmME0Hp2tDEYm2IwlrTY87X3Gj-fi_FuEv5kGyM53nb7WvTB1A-O0B6WJTvKiIGVMFlpNqUtkrT2Z4Y_W8jo8AUtVvMFPXjiQ8NrLNLN9-RDCvEgzFpObw7OzGMyTAsPoJ7Wph9V8aT1Lg3b5UiFQN2FF8yPbB7AY4UL6f8l97nzs076NQu9Z_ytQGgYGC2j5mVM5BL9sRY_A1YFtADC9mSrPQJH_QLNHqyTVjRgRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ct038Oi5BZT4Wpt9cjnypK8tR41JfONxCtRDY2SQhhUl1Hp4uiaGhfnfv9z_CfHypONlhE0-uJV3vgBO5NCqax3I55n37zfVC8qSGlR7QuPqmME0Hp2tDEYm2IwlrTY87X3Gj-fi_FuEv5kGyM53nb7WvTB1A-O0B6WJTvKiIGVMFlpNqUtkrT2Z4Y_W8jo8AUtVvMFPXjiQ8NrLNLN9-RDCvEgzFpObw7OzGMyTAsPoJ7Wph9V8aT1Lg3b5UiFQN2FF8yPbB7AY4UL6f8l97nzs076NQu9Z_ytQGgYGC2j5mVM5BL9sRY_A1YFtADC9mSrPQJH_QLNHqyTVjRgRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKWegOwoJ4CXCU_tbjfYoXdjRwIJXC-t5SeEDfXthHvkHDfNgJcbZKVGiPRMLXXs7IEbLdfombzBhC0b4Chig34bpzSlC0sqiuGzr__BFr6r7V0nly_g24-YmX3La_If5qU_zafwIKIqTkW7DC7iv6GFBu5U7hyfr06b7ZsyAO2V1J81gVMGt3uQtVQnhrg91WLjlPa242_kZ2MnK7257bnsQBupTWsUAtCdfj_7CJjOocItVWtApeaOusX52FVKNtPUlUy3Yda-hM1EY7XSVy4Xp8RCITJgmAJfXgG9qrmZp-o-WjFtngu0OyHAb0MP0tl4ALF8mVhphnjwd-Vtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=FPGAPvelPLOLOjmx7X0_e2Sb-C6cVzyjEicxdfjK5dtsvvs_9TapT301HCYs9PtWJDGagHOUr6A_Kdmx16ws2SW6aqZIiQytMEin3Gn4gj_f4MuPP4pHwkZ6DM9FmJ-jHQouwUnb2c5E5vCGvbIzCd58M14DTGzBmxIi9bCZ_MNrO19fqhU1G2qA37sdt7hom4vgYIPHWIOb9nSm0EJ9-iqRYw41C7XnEgoxRwj1lS0Y2rJ59AtgsTAO1g7_ouUsrKOD_nkjaRdwA-Mu5M-gAKS6z5yWGI5il2mVkkjM8ffxyR8qlZAYRquszIIgPzCqnt1zgyIsNdKo1CLVahcjOAHOcdSbjKa8PcCbEpXtb25qrTsEBa9u29mWB5WFOWcLqcTIjpMJtrRSZvC1A1EEHutA7rD01i1x1aVdXcenA-owz4sDfJXy43FVGfntEV_QXvJvZi_Qq0JYv05xBFe4b66lST2pTkmQQkmqHOqwLhas8jKFpqueMGWQ5h3R9I5CKxnPXest-BXugJHaMXatXB8eHGfEsfR77iwIOOswbkAbYSzPL_WNXFsL1oH6TbkLxkFMfyRIZ1H0irHayCcPTG9qt7QEbhiTnF_OcaUIC86___IjssNjD89SJvfwo1ETe7n9HupMGAhWJ9QckoVkm2NzP3wCQiNT8J0zHj4uyEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=FPGAPvelPLOLOjmx7X0_e2Sb-C6cVzyjEicxdfjK5dtsvvs_9TapT301HCYs9PtWJDGagHOUr6A_Kdmx16ws2SW6aqZIiQytMEin3Gn4gj_f4MuPP4pHwkZ6DM9FmJ-jHQouwUnb2c5E5vCGvbIzCd58M14DTGzBmxIi9bCZ_MNrO19fqhU1G2qA37sdt7hom4vgYIPHWIOb9nSm0EJ9-iqRYw41C7XnEgoxRwj1lS0Y2rJ59AtgsTAO1g7_ouUsrKOD_nkjaRdwA-Mu5M-gAKS6z5yWGI5il2mVkkjM8ffxyR8qlZAYRquszIIgPzCqnt1zgyIsNdKo1CLVahcjOAHOcdSbjKa8PcCbEpXtb25qrTsEBa9u29mWB5WFOWcLqcTIjpMJtrRSZvC1A1EEHutA7rD01i1x1aVdXcenA-owz4sDfJXy43FVGfntEV_QXvJvZi_Qq0JYv05xBFe4b66lST2pTkmQQkmqHOqwLhas8jKFpqueMGWQ5h3R9I5CKxnPXest-BXugJHaMXatXB8eHGfEsfR77iwIOOswbkAbYSzPL_WNXFsL1oH6TbkLxkFMfyRIZ1H0irHayCcPTG9qt7QEbhiTnF_OcaUIC86___IjssNjD89SJvfwo1ETe7n9HupMGAhWJ9QckoVkm2NzP3wCQiNT8J0zHj4uyEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daIYd6iNbGi0WJ11Q3soSSzY2Yh_qIQJ1mNHDnRqqoCg31jxaQdd7nwg1TZNHjKXZjjDZfqs7sgTzbMFK7Ww6tJSnoY82bX8b8S8dNiKFLb3iyEyUsBxDwa3iOQ3QEjAUY9xPpglywI5eEKHpLBX52UTFAcUmLmftNmI7oF6aKnmDZU5aEYh-H3yIHBs4NcwxZnHtH2vn7gu8FLRwEasZoN0-g37xBJeGYzdO5xZ2L5d3UlCM8bY5fT4SlekAxTwRSDLII1QCx7Z8uu6qu9tz1-CfPWbC8KR9nMXibfJTxNMt7MLV6p7pO1ZFtSuApsyI1hEKBe20FgOzEr7WVlMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYS4YsnItQBUpZzUrBQrnCESh5wqScZGLOgNU2cxi4Fe9Tz_l0l8Ig0OkjyTwQ6Rf8C3HouGMwF0D6VkMysZaXTjOrVkaGtHEhwJVbSErXdtMbJE47KbM4UnDEeGDeU10OwGQ-d6Ol5a4RcWvl_lQfeyd-oAQd8pZcYSA3bo_xl2FjbnvvxdmJWrmbOUaYeL_1oR6hXFmPToAFCXi2QWFFeHG_WgSWQErR6WJwT79CfDB40kFFabM4CKTth3YIsDfn55nTLqNuuSfBXKr9KsWB3WM0kuoYNn_GvgdR63-oTI82EPSvgyDEzQ1PXU3jzVFWVNCw6zIWZDH0IPMej2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5kQ282d-ZpNbY0GfF0Vnm3mb9LLJSL5XVo9i8C5dODyqxUwpFAat_KRh1-iFwp2qwQ6zBzk691nqYMKWxRDriUlAuHYtsqGAyVkPn501Poh1oHulKpn-gDNPeyzjEd3CG9ckoURzJh6oShNNiDle70fU9nagYDTVRz4mAo8xzRpIPykn-ATfD9JDLBj9CZ5V1FxELNrBYl463C04FaLQbredHbmlWoaCpqCxO9-SJVYzfkS1K-cca8jgrkHOEgyPxZcJ1yLPzOca0ilwcazciDsEMwyJamO51Psoh8wXOVPqJ_CIt2H3k2EUdTLndHS4QZujgpgiVZarJjwcbKjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=r18Ozdy_H1BeqHMAkiTvzfLX6fJ24bKQ_MFH_VDaubLr_ZE09p3UOA-DEeM3zNIO_5TzE4fUzHgUCn1EFIcYXKY0myEJ46B6TUKSY55yMD0eRsGyoMyzR0l1MCL0wgc4rxmRiNLuVL4tMyQIkqpoGMRHRAwP5NL3ZttR7pgxoKYRyWheo1FJDWPpnV2vylPJC_wD3p6Fa57wOsiNFCQk0Jfr_R1gLBu34VyRuB9WwlvxUFhfkWoJWSXdoZn0Qs7FBzfV8Fbe3yqHZZf22MZdRTu3UrqwCdwizZt-mAkw29-uV3MTwKKYnntpM-R_6ODS5dGmcJ_qu63eCYT_9ifW3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=r18Ozdy_H1BeqHMAkiTvzfLX6fJ24bKQ_MFH_VDaubLr_ZE09p3UOA-DEeM3zNIO_5TzE4fUzHgUCn1EFIcYXKY0myEJ46B6TUKSY55yMD0eRsGyoMyzR0l1MCL0wgc4rxmRiNLuVL4tMyQIkqpoGMRHRAwP5NL3ZttR7pgxoKYRyWheo1FJDWPpnV2vylPJC_wD3p6Fa57wOsiNFCQk0Jfr_R1gLBu34VyRuB9WwlvxUFhfkWoJWSXdoZn0Qs7FBzfV8Fbe3yqHZZf22MZdRTu3UrqwCdwizZt-mAkw29-uV3MTwKKYnntpM-R_6ODS5dGmcJ_qu63eCYT_9ifW3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_k9KXlAyXJuu9Su_NEsqQLXupcNsZ6wv_a4UZdkDuPN9ZCz3fcCOFznAVmzaRBiZ0qTqAclYwEq1tNK1vDl8jBPfNllXlRxk5nKw39XR41RsnXhQFQM5_4cWz3OkbmS9hxiQzLDKkREw5sjhSYdlUnWFh7AB9lB-5D3tWjm7tToboLDAlJeIpGZziVk2NF0vCuDk_Min2nD5r-f51tTVJjaf5TzAa23SwdnQGE28bZ__1GlSPobxNhKnYOz9t2G-YgwGxA33c83CwLec75vYzdE9B3F7lFIX6OfsGo0YEI6AI-4skvH5vIVXYAya4tSu4dcIFxm1zWdD2AJY1SFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLYhDMGxrHgeU4t1cwDnC3YfYpODB80oT0RpHTDhe9QyryGO2DtbMbWzFFh6Duuy7hcrExDrOz8j0csT8TjWKs7MkOomkJ14ml0UK05nvoryFP6rO9ZhaP1ljOPc_rVzPA13vdDwrkSJCfJaMeSoJa_8aMcTgiK6xnaHrVPL9BXf0SQlrqaAGkyyRXA-_U7jUcJomeXbi435X1DSYKAORxvH4eoXjA0a4qhMrU37GIa0CYZIP4PDIqAl0Nz0j_WvtWMEF4IatWwIk6-GuMubFjyXSFPSYQrIZ0DOAlCFwojhYECp__TtLF9jOJ2Unp2-h204twyka6xnxOKAGnW4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpY7CXnV-aowFs535UWS3QqUK6FcTqNg1DogwsNA6GOu633D-3GtJ6yFn3y-LscoWAO7PRBB9lDht_laP9WxmiqOiGBR5bQg7XXZEMgUaDLylRBxVe2mNBmxiLbsU9bItIy6SXkGdJ6MlumFe0cM2x-UGV9S3SYl4K1zJXfjk0-wwqpWRoOMH1jGJfNAS4QzcpPH-okrS3PjYxP-JdS5ek9P5-xb9tcM91YJxTMdCO82wmFhAah5_zjzCx6tv5zb5boGbZq1LX_OeOOHvvE2pkLC5bpVxnxBb6qUuDO7ewZ0TKD6oO6SAHQ1T6zG1ehmWC-VpuA_akDB8mNLRrCcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKWd8zRlF231hLgnusTJHBHmUXI7rZK12BTzjbFDW7SRk89_PgNOqUu2LRdjQUWmyqQHZ57D5xwdJxGpxPkrpct-Q0FtrrKTVSP9BxpWb88-3_kcNEGK4QZCydzeooeXO3_MI_0fIMA2pzRXHidQd3f4UKkq-rGlalxAghzLZJXBgWgN1iIGnzWk5GwquOl4bXbcynMFAo3ntph7cMnzMp9At-oESvG8gtDAQQIns_vIaSK5i7_iKp0-WDO9Pc8QxkU2v7E2_mvl6McE1vrvJPerAjyDGuLlNeyjYy6mmSMWJ6Q14f3ai2UC1sGeJffyA8DfxKAs1a6d2xMM_qqzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25878" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=TH8uTWIGkk2eVggucS0Qg5KQiIpUh2iKQFkSwo3rjvQLVE62naDl3rPcZ9_fIe3hy36fonJ4pIw4Q5W1nws5uKxza_GnPMIjSVpMyY2jOMloXJvXKZcezUj3nMCd5Eio8Rb1qoFXd733TDOGe70Hm_i_UVhO6F-_5loCWm_JOa1buADytMpAvDkAX9sW7pv5ZeAGzFNB1iPDMUjnWotvXQIGiwb4r6hRz9TBaLvQ3vhUHrkG7dQsCodMAWqQ9NYH8oMHyOUK0MkkQ7aCEx26L0BjB2IL2WYN7AlTV8aWZfh8Io5CMaDoX_wueZ45OVkS8Dpz2viwC6M2VhsRsshRhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=TH8uTWIGkk2eVggucS0Qg5KQiIpUh2iKQFkSwo3rjvQLVE62naDl3rPcZ9_fIe3hy36fonJ4pIw4Q5W1nws5uKxza_GnPMIjSVpMyY2jOMloXJvXKZcezUj3nMCd5Eio8Rb1qoFXd733TDOGe70Hm_i_UVhO6F-_5loCWm_JOa1buADytMpAvDkAX9sW7pv5ZeAGzFNB1iPDMUjnWotvXQIGiwb4r6hRz9TBaLvQ3vhUHrkG7dQsCodMAWqQ9NYH8oMHyOUK0MkkQ7aCEx26L0BjB2IL2WYN7AlTV8aWZfh8Io5CMaDoX_wueZ45OVkS8Dpz2viwC6M2VhsRsshRhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anGcEWYunUj8xcdYPRBmr_uff7o6bylgdUuaEwei9xMlKHsUo6dqC6qC1mpmdG0JbpDnMSGNK6xI_QdFdVUEatkpkFDGT8b4oroCoYAVT038GW1ai5U04vh8V22rAok1qjED3YzbkSQrxXNE27Ygogngfiqtg4B7tfnNpgKsDyN8pa5UGf4N605S94H1nFfmB7tEBwoR0GkEurXZUYuH8rjRy3Dv8Hl4m8o_25UiFwtwhAne-z1gcgesU4_FihcRMkZ4RSd3y6hlbPcwtpALAmidc3Bb6v1lHPFzF4-UTkRsU2t1_CZDWBej3ia-WnthPVtMt3DZQs02WItq7LSShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0emm8ymCtw8cnf8XuO7_Mg-mmuCKQbKutnMr6m48J0VDCeUM5_AZoTqBqlrfchJQUvqTRMAYLVagZt_2iTUNskTQxzSYuHumuwTftMmhwyM2M9u0kokOBAWY_2CA-vKixWSv3KgWM9sgdYLi3bLQwWYHW_qBbl3bY7GytcPkG6zLZEa2is-0SxRpDN6Lzjn3jA_3_4avBPWjZtB9p-crahSUehVwZn5MVa7An6aBqbwcLYg_k5WzHTV-OEf_cxQmXoWxhFj0u8mn7Ximi8cQ6_-xHxevDj7LHVBKpVfvJBiIqe0-ctAdMGr2RgiZwJyBa5rckel5AzV4T3ZsgFT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUy9u4Jyz4VidF2P-X4L-6ZuCMFP5zzYp_9XXtXEbCmIc7VxkQyH3B166qmA7o7HVTdBA4V69k1F6h770RqdZa0zapeUeKwYyBIs45_nfXmHPE1x71vchF-SGni_knAwJWQG89gvS4vsHUHQxdXVM5EvPdbduGFGGFME7FYuLdQqk3PSv6L9GH8XRIDdGAHt42J-cMJkgt5SvVbxYQC8JsdZSoP_0bQCKEvQvqoW34UUkeGsDUbgJxZeQSV3Lx7D7wkU-1Vm9hpnLTbj-Jy6X3vmbilwq4zJtk0zhANNTdrc7mImYqMK_m5-bfZE0hnF0zPivsb2c7euogSkq0PU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDkeuu5ZHwUDzDo1PG3yvjDg_HgoiRRga_0q-4XD8P7UWQHmPX_hKaNLhhgm0RCfwigyEWkStq8zUEzPeT74oBW335hsGEMNCGnmGf3a8yBqttgTQ2l5kkc182hCX81eTvhRbimrRXXSbyzVVUGM15TXxdAOQvCBJhEMUnsXMSErK-6IyyjtclQH4bZu6yr8SVBliM1Y7NTEIWGUnncXdXXtIUNURTqSih__1000xkzNIAZKoIE2d-iOdUggavxbGA8-WcKakIPImf1-mYCeV-oWfjcOByJ_3lYnO9xuijTJqpuUbAiIyVKGEbCcXw7t5oHESJzkUExOXwkMrn_liA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPOC-PvUUkc2XMgfSb3nYr_fG59da14KPeMJYm0gjqIHm8V7X91u0zI1obfvLYby0CNAHhA_Yj4bDiGwatSQnYQd6K-nP-8y-h_Ogzxwc30xmlK9DNzHabrzyxKBdWKvC48Yw97VWfDBrJnn1pRECPuqwAUvfnz8pIjSgOUMRoFHA_AL00DvXRb7f9jfKr0JP1e3H_ALQqsZzW1GQPfktkHhZrkfM7nUGDFSNzCnbTjcUT3gpqpPx22TpHiMnoFzp3fDRIkcbUYvv6zfJCNBQ6NivWNDxFcFDc9nvTzhiClzdjuB2q0E9G_r0EbfQx-ROso4VY9ZT5AKtgiyNAo7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R9dpYryx_XpcHjcg0T7I6duo1aZ0__GttsLaHFptkxNwUAD08m6dkp19jZZsXg91hfPUx66UFSSiXKHcKaT8kMdYukNprEYbCro8rwKRhpG2pb0cjZX76HD6ektneBA9bFjKX3nSEhCgn-8vuKBpg7qYaOWogW4HwuRRYpqIaOp6BUUQp9p6k8ceZZ9Bo3it-kzI_KqcocuEnafAOxXllO_ZULcNGTOrLyasWUdbkCaL4vUN_SqfvMWC8ax__cbE5G330bbVEfGVVdU4CiXhUdLUtFb7DZw-SqUj5TvJHc3Bq7PAn4bkyiZbHtL_XPzWEA2L26TFyd2Rf5_RQqPwSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoR0eGdvxKVCFXZe47fFSM_9G-Lt9691nek1y1_tPiZ2rDlTpSKW0oPeAS2Y2Z7Zo3ZZmsL_jCDdh0BVT87cXccQRav9DIZtbT7jmypdSfwvH6KW6atlTNOVo2c8BB9KtlU8uuiRP4_8YKuCCkCH0D9W3fPdGJDGVBvjVa8jiUwHgLzpTA2J26o8dpl_-Y2KY5cCIU9rFQB2q9CvoGey8_lhmIpdmQnWUdR6FNKYqIKm19ttd-Kyc50MeJU0dQ3j3m6IHUelfttZ_LK0Z812pHnXqQ2AX22PMCWjHZaBxW8chZnMr7vvZf9hPdzEYnPlvabet8uQ7zov_Xgn9Bek8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=e3SDz7p1mSZcjXUluYwoB3C5G49XrVG-12RshZh3cJIrCEJHITL-D6DyS5-Q0mT_5ehC2x-n9liCX_RfGwj4wA5RLanfc3LpGV-btgUbl11kUJYB0DrppyTliBw0sUAP9hbs7uvvcfFwfKTitaUdghPrCeAn0A-foENlSPPbi-Y-lMphsBtBVq1T1JgncpRF_3o2rslOnSTrjVE0Vr-1Ccfsh8ge9_-SopAp1N2VYuSxVxugVmULHB_EupYFk6bSsZe7LxtGJe5tXSj_24zID2frFYXskYD4SY-pS7qcFCsXquwxPd0Ii0gApAOVvhQIUuu0hEh4sAJuCJeqRdwBRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=e3SDz7p1mSZcjXUluYwoB3C5G49XrVG-12RshZh3cJIrCEJHITL-D6DyS5-Q0mT_5ehC2x-n9liCX_RfGwj4wA5RLanfc3LpGV-btgUbl11kUJYB0DrppyTliBw0sUAP9hbs7uvvcfFwfKTitaUdghPrCeAn0A-foENlSPPbi-Y-lMphsBtBVq1T1JgncpRF_3o2rslOnSTrjVE0Vr-1Ccfsh8ge9_-SopAp1N2VYuSxVxugVmULHB_EupYFk6bSsZe7LxtGJe5tXSj_24zID2frFYXskYD4SY-pS7qcFCsXquwxPd0Ii0gApAOVvhQIUuu0hEh4sAJuCJeqRdwBRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q63w9isvDhd45g4xBDkmtBq60IQB1EfjEP9yz0NT30MCdwAIUNMRyfmtbnMXzATiU8JMcmwXsllL9G0uV8_hdG69Xg2yxQhRzj8kUsttBllS7tlWr8WdJUeUHZ4-R7XmLcKi5nZWLBeEjlj_ESFsadM6bgSTqOFGW4xRxZqKiPQ8mPUnQo9upLSUWT59AnEaPxEXEVFK96YFGrpbH-KvQhC4ORDJxvg31GV4YYnakYqM6APgQnt9oQmjOZ7PU09VaaxfKjBeIqeFbeVLF6RQb_7862VQ9W01eVV4H7I9GSEiOiJntUXWzi17uHS9_ZmkUWopN--MhmeyDUcFjXAmoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqVVrJusIDfP7Bykd9tvpmYOXzip1Me3s3CdI_UspoOhvOMZeWaySi3S-mMnGIcsF0t8KPBfW09vn2FzL-sqPoOO5FeNhZsoSmaZmzwKb8Sb9ARlJmQ8nn7UhVkYcKl2IBFgYJ6anfWrNSP1YJQA7jMK1JJrU02LzsAVqGyKMajFod9m4OAAj3yEgHhHI33br1nPNSo3fI8vfQxnGCo5MS1nLpvB61kYKXLHdTCgq74_27t6m8EqS8ePeap8pFgzM2fMwNtOSdvxTDeXAFWmcmG1EEfwHqKUzxH_0TA-d22jJ6ZG3QxgY034BVXsIDBSKV9G4LmVhTTcVtkE0SNIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zesle2SJPqhk2y5-v6gYx3U-0aasg-8fY9Xr4US---i47PNTZhnhpRGCY-sandDSbN_P9cm3H51NIYfemRjvQLQjXrKztvdRoq3VQXt4441etjgd8_IXKWJKc2xobqw3osB-25HZvDieuIDhUrxQHZgZu7X_Q5KKP-BqA2Z2VFiNAXl5j6Hxq6XiwAJjvCcQvFWTOWMys7hiKo-amEN7A2TEqQqECeITLeO3bnygQcr3kX5xxhrPKBnvGSlTAXBVw3OqLp5_peptXOhKZxSqseBaIW1Vj4m7nVh4yPzUT9GddpwTWBkHWSBAijdpj1RYuBFvAmBdo0Xc23c7VMDxBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=F0u-Pe0UMF6K_vjlxrU7a-wBnSCAe9xe09B34fCc9alchFjkXD0m6f-SXFKXpBSHAITFZcx2Lrcrbx8jTZjoKlS64KE5BpQl4AN1-_T2rfJIX9siU4B1lOilrwOafTTlIcZ91F2aLaqGfs6GB_2kkKEVdB7ABObo41eOI_-xkjJ0uL-S7ugWR9T1IQjdfx7gQBJsh2onEau9jLwCy4NtPXwtjQOrFr5dD5xNvYnPlJFrnBn3YLbuMhNIKV5JmIU7tiDORmjk_RUJO_HX6FgoSwT4ZGPvHCjC4Jv08aH2h9DWMPTryJkK_Z2nLBXs2DjKdsgm_bdsntc_UqDk04TQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=F0u-Pe0UMF6K_vjlxrU7a-wBnSCAe9xe09B34fCc9alchFjkXD0m6f-SXFKXpBSHAITFZcx2Lrcrbx8jTZjoKlS64KE5BpQl4AN1-_T2rfJIX9siU4B1lOilrwOafTTlIcZ91F2aLaqGfs6GB_2kkKEVdB7ABObo41eOI_-xkjJ0uL-S7ugWR9T1IQjdfx7gQBJsh2onEau9jLwCy4NtPXwtjQOrFr5dD5xNvYnPlJFrnBn3YLbuMhNIKV5JmIU7tiDORmjk_RUJO_HX6FgoSwT4ZGPvHCjC4Jv08aH2h9DWMPTryJkK_Z2nLBXs2DjKdsgm_bdsntc_UqDk04TQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzOd4gLKzADsg2KlT_9FNbgHuAQyFBJeYK1Hq_UnTGLG5SEW6y2lX8RtEN0mH79psp5leg_rDS_9gn0B36oYVc3aXuT9oggkzziwoJ2prFGAmN1o4-__q79Wp8ScUDJNy6eB8PmXbjJ8wsw5nkBbbhfqAL8Sztx-eh97CUGPnTjKtJ6I0YCGVbn4gcSn59ZxVoMg6qjKivnDlMVQJaOWTs3SpkHGmsKsPT9IpsAl4Ir8NsdQ2Bsj46uBYP6LjM8__TBmi59s2gFEwFmTdQxFohbDyJY3vFWSj-IVuU6Nh9ZF2UYVv3acn4fVeSbsG2vMlIcJgS0yty1bEyha574OcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_BQD-p19HWV4X8gKx-qMoAkGJtHjHJxSI1iFwOqA10DhChiT1rDYTvQS7E8zV6pf-q9z8XxhbGTIxcbgtt6WcgQuDlY38BqhtcpeeUbgSra6v-bhHBRAMc6Y1Lg3I3lYw-naEoFceXiliztOzxyOexvVH8Iy8J7LHEk3p3RDkoOIxRoLHFO1RXlHQ-jvLTml65uKQ3f47Rdbc7t9xXw8dOWwSrCd-RyfJqVKEEM7SUl32V8oqIuFvIRrS7He2ZStK8b3kaSJuZxsGMhggtGhUR3tXEtlS_C-99iBKn96rnyFQA1Jq_cAnjrYvgZm2PQ6MRJRaj4jEw157S7jRARdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5BOC0WIvELqJfwaPDNwXVjGZv4jO4RFV6Af0w8GQCJUXznHPuJwdrhkv4TBqWuniQoTkA186MItshHRxLKwJ-dedCredS-pDxFPP4-KEZPCawOE6_60lA8pV2-_1RHrsiYFVMtwg2oWFzPnRQQr-7EkELh_kLb-dKy3wT4yItLseORsC24kUpcyaYUzYuv3qbN75ktuCPTv8yH8G_E-OmRhTDr8ZRA7EAMcLL22d1NxIJ6gCdH7x4cxIdfu2i1yoF4eWKZEDcRC91E0CnMJkHL1uMS0Ko1qPmnJxSpnPflsWgMnEI9gVzYh2qxNvt9H-R1hheVN_J3adSIX64g70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUChGC3WSr9S-D3lrHLL6bVtAptbKYuuj05V1ISQg2lKempjJulenWBOvAK9sFMD5jlB0jwvhPWYd4R2mscM_9EHrO79weDUjaX2p1c89H-QdtWznaNSTHhytBsKXMvWvlqQWAy1Ci4YyQK0AsNH4X7PSHpCXv9EDhhF7dF3jFnPCdJY1qqyue0aQSwexoIhDjT0VYUgRWYhq7OPo3QgOGivorsKrc6xx6NYGxnEri-HVM7tVstEs-eCV8HuZTyxo8A81r5TP1Ul1B7I5uI-nm1x67K1pbQcXnoSj8kkoFBDZ-uuNhRaAYoBpjHv2ORA4diiaiAooorYSm9T8u-R_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk1DBPQU7FLw93y8wFO1paSRx6-8LiCu5R-15bkCVElpQWqBP_Vbbzkq8SH9nbBQl7oQ8lZVcJkZ8rcrO3gsUhiRlL0R_dBuPqeUGXIhXz4Jli2SYA0r-zFH8Z2FgZ47Y_sc4rRuTVruOGWo-yIjam0JyHtbJudOEu2i0rLYXqE9oR-kyMMjSaxEwgNJbmdBa04ZtZZ7lE5_hQkzVM-FQpRvWoz5M9X8dMkmpBnrN0h8VTq5l2p1OUTVCyXtYaEp_HB0KPe4Pb6fmfo-o5rRlw9BbA5yKVKia1KAJvd6opFzAnolYSCrscZ8ef1QdHuFCIGgIJRCXAEXqAmYXDPdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_kpkNJU8VMXCx7TT31kJyXmXIQI1SYILqj8JJ0ysgzB58Dbnlp-JVDD_JLQe2gMYqF4XcJGLQucERWP4ujgm1XnzQ5-vJteA-R_DLpg-XbqReiroGjudC8Kavr2GWEvZofCQ03vsAXqBSe3HpTiY0AVjN9orUwqGpXzj6E7K9urkubbjG9L_SQi1AkOuELobN83MJ-Mco48dwUaf4W-Y8544jd5F3euXJhIbXu2c0AXPVOET7iwkaTH9Kyfytl6WGjjXLy_I3QX9jFBSy41mUajQAy5l1DbIrAb0WyQSOi21r47f4Mq-FK4ki-3SOuUGNxvCPyoSXzhzzcsHbBDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWH6_FAucFHfKV74jgkZL8jWGilyj9MVQRchBCmf1XJYe1GUptPVno7MNREj3ve8QSGj7OQ3U7wsEAjH4Xr9W8FUPYGedsYCj2ZGRs_nzglcANuqDkoBRX6NUMsWB0udmTWg2puVwnhH0t62KAQHYjpwKurO4JMAshc2aS5p3Yhsp8G-44kzid81Mkp_qmVugV6tGwjGPXCAuQeZMuiI70C0zYJt_jSasNtC0FRmsTvW8Tp7-EYOqE7mCxvw3Inz3hvKPW50qpD8u3SkajqXmHkDgJLshLthFCsSzMdAbkN30hXJ_rJFjGTBGLUb4UD_lyoJrsoxo-FY2IkajiQS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDqTKMezcVKXZTafclIY23Kk1zuXMEKLlqbwFfPkh1KtUE3k6FFqJHVpseRF-4ZT-1D62Z3gxurDyqzgHHXh4zxaEJWI3IU1WwBINP6ALTXixDVGwQxuCkwIoabMNni8XuBgjmIWl2R4EX_tpvWhwIimto0miba31CeiYG4X4-DYErf1Oh5ArSiBdRzpHYx98lBp7P8RPN48p273ny1zAZcfXLXh2x5oucim58qDRRdiWacyExCqAfT0X3Ro4DVYeGLdEVZ6C2xGN_KMZbQKeZXOjRwMLADUXJsttsEoEvg76uts7jeTgKTG7KDkqmzgahKMo1CppvZ6-MQS0CDxfwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDqTKMezcVKXZTafclIY23Kk1zuXMEKLlqbwFfPkh1KtUE3k6FFqJHVpseRF-4ZT-1D62Z3gxurDyqzgHHXh4zxaEJWI3IU1WwBINP6ALTXixDVGwQxuCkwIoabMNni8XuBgjmIWl2R4EX_tpvWhwIimto0miba31CeiYG4X4-DYErf1Oh5ArSiBdRzpHYx98lBp7P8RPN48p273ny1zAZcfXLXh2x5oucim58qDRRdiWacyExCqAfT0X3Ro4DVYeGLdEVZ6C2xGN_KMZbQKeZXOjRwMLADUXJsttsEoEvg76uts7jeTgKTG7KDkqmzgahKMo1CppvZ6-MQS0CDxfwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvjEx0gCHjktRf0bZGr6ObON2qmkehkxJKAjZe9tMK9FWg5nJ4YxPS5kmXM-shEpR8h7sU_zgM702zrbFarxCW4Q5VF8OeDaRjXxl3bSZ7fsPBAh8LgNcUCu964jFzjJE3zLbDayl9Oh_4Pb20mKjC6rlQ9Qa0uXD2BFFK7slQKON7SbiqWcJawzKljc7gKr_QMfOH8WQT9KzFw78rbdzEa9efIraPHAsA18s81ER9zmMyA9Fj19jDxgGfLGOeVy26MRA2dGir0KAABg0zbCH_ekUShiWydP9Y5mJo77_JFTa8SPnAgTMq1QV4TlRdlBavHiNhat_vP8W_ioWTjGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0r1kXJXmp9CzYho8vgca9Q2p-CR_YroUiID684zTU14Pf3L_2l_FkN8WLwFbEZaNyI0JQu9g43EQJb9pbq8kvjh_sf6z6qK0CEaM4Dy_uNBZs8igpMcI2ngrQmnflUZBJrsXWPHsWBK7DaT4RYSPNhBBnNBOgC5uZY0LrNhhuoIZjJf3W9oeNVgYT5ilmT_H7lrnw-XA6NV0HskGKRP0dv7ke1877rBqMMGKavrkwgvL7arQfHspQp2Kw5mLx681THO0_McxRbEaQN8a53x0k7XSSLho4LBinNywARDKdr4goZKKX1XU_Ti2SL8pAtLT1I7aO-bhrVc2TUPgTJcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afafvCxvUspyN_qkUmmu9f-CkuykQ62SNO-Rm-ebxMu95-JFWVZHLleh8WwQNne2FnXwko6_JjmAQUnWpDtoaQ3wk-CpPxrNhZ3spjuqQ_Zwlr9hxwVfPA5dVx6GrsshQId1pRlpDZePXuMXBNw3vMi6cseCypXIuF0gN6Qa-D4ZCC4DJvCE4cK0KiWEb4yVq6xUfEo-MlcUvYNW0_rVHkKTmY1aZVvlk-05BFESMjiTCsQo2NxSryCkCwGjqALyakJw4AVuvQq1aIQZG67Hw_kCNlfih3EvcOWfkHRrkfjA3IXPAdGKhwjeBT9XXVwsOsDd3hikQuNUoAg81WMO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec3Aa1fVlKov1SwwFi7Qww9eXJECGaUp7fHreEAI10yb1Q0j8NUEpy-hEJrSSh00bcX4I9U9nspPqA8-NbVXK2fcbX57vjsifPnKpSqKdG-OuVHHoj9FtzfnLZMmitMhZOV8zFBNlfVC1iWZHPOsaPliRV3ad2TRJw6BDaCeH8TqFCViaj1DoD1ZFw185n89G6Ly_5--JTq575DtSkOsuFSwcjpxq5pnfyJ7TIpONb4hQ_ycQGRyAjKDuYXCIoDGP6B6_7qDPPlRTOo1d_UhoMy9EelkoCN5CsXe9heeP70Hdc1eqKwkN3fIHMUw6PXyY9ViEDpKRaFq0XnMCH50ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0usjYkCf_eU7vwyNKY3rMZoKAsrTfTuEkq5uj3a_rV86ymnQZyJOXhOk4ZN3n7998QE5hb9HXcMGsg_a3hYJY37Rbd830l0Ey4BlfpX9MSX1I62R4ZQ6g9Fqx9TuUPoSLIFIYhmzoeZIXTWynVWcTu9RxD9ajnPM2n2pPrMLie5WpmupkXXZTmc3MYEqJQST-UAZOubc9eoE1yuMfuKVHmIPclXkh5ny2-ot76keBblc_UWS9-vwhEyS56ZrUf2l2K782bwewTLfYQi39DwFp-jfY1XOTUA4SuAdyizU5zmMVT5piExM6ulzjxcY9JtvTdWTv9k2BNm5ViUsIwp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpTnHi2L9hbVatpJ7XqkH15FbKTFScID9mF43kuvNUpYggR59zcnN_5GyQu3JiqKG8MxtWM1o_Ot5sOUWyvFxfbTe5m18kn_ydPQJ6ogt2HA3yYGW25MWVxWkqvoTuSRRwoIrRMlaQk2GkKNItIO4Ufs3CAdHzI1SQLcKojrqzXHCHpiwq6rY1MrM3TZuatb7prE-HuX9-sx0OkUs9GfPKbGeQKjwdoV1TI-qwzCcl1_7DCiE6sjs6hBs0RVlrkBoeJlHYtZPFVhqzIkGYRtjXXU83tkVrHiENMR7oIghy4s2oLkPpKbAYcrSB0j5HJzoCC264oLYDO7VdvIvLU7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJkJO8eILME-Cogdp8IopUMRArXbX0sfrsAOC00-u6dnACw3ULpwKHUtB_WU6fGF4uY9_u7MruD15sfUWuVsI36Zfl-d_RQSWZvXmB3lT47KyJPRYFW06mXPfX-2Zddcq7JCbyuZDTwAtC4aNtdU3KSd_m3s6CNfr8YBPDnfdMzT1OLAxemXXeOgJbWiYcx0fPY0jdIPjpow8z78vrtIatExOknFcbP-DVo7Na7p5UlR_ojLCH5K3wpLyVuyC51CNHi29sckaDJ4KBiGJIknXMsgv1BIaygg-ef3-5dXJc6ZHZkuRuNNAEgB2vouygLL5b6g-PxBSH2UNa4nqnkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7T5wRVvIc9fPKTbpPAT5aZZytqQOn9yRPn7ml9IhTagMpoBHkaTgQZp3MyG2joSUs3er05P5tm0pAuOecW19qYtnrqYO5ccwyx2D27YkFEBjdJ4tIxaCC7J1e0IpIKJLLMpfaCCKbArWU1DuhaFPnDtSqyFViTGm6w2pyYe8WWy7b5GgNONA8Ix47xa65x1vnw8BB78wNUPONAgD4bnxgflzNzpGzUrQFSklxbyOA6BPLj2pdcOrvuXl6qU9Hjdj7dkQEal9jqVZVU3dORAiDR37l5v1XqqsmhK1aMJ5dkU7w0cOCnCHNzOYQfT24gE2C1njWsqffAVi33aezsR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=rBPS3Of0qPcLoHkgIfXlPPD3lGNrzHzSEvLpv7HKAy7BUtOPs-rDDxltlnk6MJkuOtxSAmnnixLTL7wu27U5Lxknraw4Ku69pNbc8wdgtvWr-DDh3SYtvISgs7QjGLtNKMF823cH2z1pcb6LoPxayLk3u3NEMk_Sig5i8a9aeIFWKyOaruZrAfebms8tandal0VeudHJSZjk79JuNPxYoddqXHR4bFyPFVMrynM2XDOjhdLfTLVs5f-gBSu95UCrV0aAml_Bb1PO5WZv7uAeCKwtHEMNFlog_T69J0Zhen49RrG3b8BPz9H18E2b-LNsHRiPLOHbvJ_eSwERlMKJuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=rBPS3Of0qPcLoHkgIfXlPPD3lGNrzHzSEvLpv7HKAy7BUtOPs-rDDxltlnk6MJkuOtxSAmnnixLTL7wu27U5Lxknraw4Ku69pNbc8wdgtvWr-DDh3SYtvISgs7QjGLtNKMF823cH2z1pcb6LoPxayLk3u3NEMk_Sig5i8a9aeIFWKyOaruZrAfebms8tandal0VeudHJSZjk79JuNPxYoddqXHR4bFyPFVMrynM2XDOjhdLfTLVs5f-gBSu95UCrV0aAml_Bb1PO5WZv7uAeCKwtHEMNFlog_T69J0Zhen49RrG3b8BPz9H18E2b-LNsHRiPLOHbvJ_eSwERlMKJuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-QT5LTXtwz4doU2PYzWtfBYJSS55Z0nECsUCI7BSLatJ7TLbZjRU2H_3w02HXBqv3VL4iMpVaAsttr3WCO7z7BQwn90EGhXV1t6p5vkDWkC772NSJaSrrwDzgfIwJflp_SNuadfXjfmk68B6YX1c82Mko5JLbLF-lMyXU7jEcO8DNVHiO3vcqqQpwkIcBkD-utB0EX1ERhKkJGVXFc_LfQOskdrphFF_9htcsXCh6HUonO5CbKS4Dqqzbsc5lvDC4Se_r-_sMSLgR5dMtT6AMmnUURTA7OqqLbZEeK7pSiz4EFy0GDav4RcymYRLnZ-438FjDrkzOa9buKv7Rhu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=hf_qvYZ7_6YKZk4Z9rovZSi3JyMEwtYuWkZhoxoRXzyKx6L4Ej43WjlzFaUbCTtIPF0JpqeWmY09jz7XK9fDuWfN3RcowJPqUA_RMZsLTwo5l779PeDPwvVATlI9nqvATfYkWcr5Ras0NF4hF-ueSGduVNyJE9ShwWPr8HOmDe6IGzB6YwbBJwmhsuEcz7EqU7b0gVddb5j7kyhRYleg8bFOheuM0a6XtTfh4G8FTqF32oFlgSXZGcHBkCfxxeQ8Db6e4NTTZIZ8ilDqy-l4dJ2t1FayRvNPAxAqx6W5WB9gbBzL7ysx-mZEdQXAYwslM5xJ5_Jo9eRLZTtrOwYeIGHAkSL2GXw5wzSXmUsgH8BUeHiRKrriGHEZW9BF6Fo0g0yEOy4fcY_ykUBXtMzUfBkUBkcWeyCLWcms_26oUXzgKe4lrU-uvPIehEQhYozZ3-IDKegLgOKfdlmeNfbJk8xwl0hx_pG6UVF89OS66uRH20WGmK9qULIzLgJEBHMPwVdthxjxfAmBOJZxGEITMJZHsYefBzbZQxPVwnam-Jisi_1W7X1gI6dGTLEX0xSw8fFNkEOLbdJYwnSl70J1aoDZJ0hDjDmoFWkE1IoRM0Egj98kulyxAWBLspNWEmoKERwjjxIF7bM-y5a9PU6vz2_3-LlOE8fdbee1Js9ScMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=hf_qvYZ7_6YKZk4Z9rovZSi3JyMEwtYuWkZhoxoRXzyKx6L4Ej43WjlzFaUbCTtIPF0JpqeWmY09jz7XK9fDuWfN3RcowJPqUA_RMZsLTwo5l779PeDPwvVATlI9nqvATfYkWcr5Ras0NF4hF-ueSGduVNyJE9ShwWPr8HOmDe6IGzB6YwbBJwmhsuEcz7EqU7b0gVddb5j7kyhRYleg8bFOheuM0a6XtTfh4G8FTqF32oFlgSXZGcHBkCfxxeQ8Db6e4NTTZIZ8ilDqy-l4dJ2t1FayRvNPAxAqx6W5WB9gbBzL7ysx-mZEdQXAYwslM5xJ5_Jo9eRLZTtrOwYeIGHAkSL2GXw5wzSXmUsgH8BUeHiRKrriGHEZW9BF6Fo0g0yEOy4fcY_ykUBXtMzUfBkUBkcWeyCLWcms_26oUXzgKe4lrU-uvPIehEQhYozZ3-IDKegLgOKfdlmeNfbJk8xwl0hx_pG6UVF89OS66uRH20WGmK9qULIzLgJEBHMPwVdthxjxfAmBOJZxGEITMJZHsYefBzbZQxPVwnam-Jisi_1W7X1gI6dGTLEX0xSw8fFNkEOLbdJYwnSl70J1aoDZJ0hDjDmoFWkE1IoRM0Egj98kulyxAWBLspNWEmoKERwjjxIF7bM-y5a9PU6vz2_3-LlOE8fdbee1Js9ScMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTJlSZJBxwFuACLk0q3aOyM8UXYkYLEqRQ6LXVo7MGFQvuRph9o33O1oKN3LWQ-ik3VoFK8hNhO6PuRoV4CXEeAJYBd88uYbGCjR-WOkETmMNW9sIAAMqMoYJr2n9SampAnDm4xSdTWcVjcDk_9qV3pbEYgSRqYOJYpznNOvLFS0fjwcXDA3grpkh9ypDO_f1f3SlgShxPGuKlrGGBPQcgcB8JDmGFej-ybYEW_VKmGZRd3_mSVJwoVTfuHKXqgZCP_507yTYQjSz0-lhMwICL0_Y2BRVHuOdCdJhVYBNb8UCUDw1cBWODu94RnbHqAW6iTr4FbcGpodTqnOcsIpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQOppdDZbzhGTZYPtXFqgTVivhahIS2l14qNw7ZYslmFdIIh8Cy7Qu645kOND0bgBU2GZBexsNEHVF_vfSDgEsapBIhU7U4E4btF2g4Pa9FkJro3aZb5K0It20j4Wxr9ZHdEma5HheRpqJjZitvnlRA1hbFE-6FLZ_uhPpYXk5KokdcU7OcniP5GQzCuPHvTODmcv6CmWteHAieV4NDzFq2lU-TQQ0GWDbmzYb1r6HYXETnHLvvU1IjgrwQUdUjReJ0hASVbzvMwb1hrL-TzTSkcbFRS8OHbKFcxeZv0KTSf9dweS7nthVzOgK1uD1gvHMo7JZLbPiYa9-3n1X94qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkyxklkItNtqZoV3nwN8YoSnOQijfJXHIKCqWFoOiXwV85mnCAs5QBc0LKDXlI4g96lO_aon54GsC-bprMI1VNDK7xZ_MTRCSLM-refwFPktdsL-loSgmpk7dy6g-bL1gVDTM7FSBQeWjCP3fJ6Vb4Zv_MDzZ3sUQNWqrRO5UQeDs57QlsG8mIn1IG19U-vKAcAGrlAvk7hDjNzgiD_NkX8DeuL7Jwtmai19yuxQRIHONA-sQsV27_WToi4wygZUWW44N2vrJhTLJpo_NekmJeb21-Kmpt_Dr-9wlLfXzAIvJNnZdYJQa3jgU-HlGxiS6NCM4g09vcFzpanbMAhn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=Z5XCOSU9GFfNl7tSeEoAu3i_R9o_YhNGsj9XfilW4tlYDnLcwdb6uhXU_v7YDrcehxU6yr4W6ZBv1yKo40flxJTFrM8tSsvk8jVHBY9wU-RCizs_LiFwAE7bNHXa9ilZ7cSf9yV4KTd1TAUQKBvujidPmZ9fFZ-HRNS2fVO-n_xKC-hoF3c446aA2EmbcBmaLlBSyOeqaYMcREXc6R4B_-0wK9x4yrVN6lifgki5l6dw5ePgRZ-cXoe7pqYarM9jqNKtsEZFFJFdj_cqMFZ4BFfvTzHGThZL1IW2B6pLOFXyPl4n00q474Jr4nHNBDYI9taV8vWOY4D2PNGASesfMIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=Z5XCOSU9GFfNl7tSeEoAu3i_R9o_YhNGsj9XfilW4tlYDnLcwdb6uhXU_v7YDrcehxU6yr4W6ZBv1yKo40flxJTFrM8tSsvk8jVHBY9wU-RCizs_LiFwAE7bNHXa9ilZ7cSf9yV4KTd1TAUQKBvujidPmZ9fFZ-HRNS2fVO-n_xKC-hoF3c446aA2EmbcBmaLlBSyOeqaYMcREXc6R4B_-0wK9x4yrVN6lifgki5l6dw5ePgRZ-cXoe7pqYarM9jqNKtsEZFFJFdj_cqMFZ4BFfvTzHGThZL1IW2B6pLOFXyPl4n00q474Jr4nHNBDYI9taV8vWOY4D2PNGASesfMIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXGiEqIqgXUdORaUL_xCJk_7B5L_e476Jk9lWi2kfCc9cVZ78bIW2y8EpqZsB8ALqIoSggqtvrJ1IN--30UoP_dM4XGkF5gOOXbmX_dS3LZZBFQMxn5Go_kxUkjV4XKNHoCtpYWyEGjxJAZkjh4O3J2MBFl1C-eJcsltF_aQjzGYvDqCwECxBtRNZdOLVSnay4nRd9Hg69XWVM7rbi_n2lT0aG-SzSKFDDa9HBnhixx5pODLQbP5TC7bziwKBq_zvFfhdKYHt2VXWO6nfCtPYObiOcD9g91CvlMvwwk7V0t_ytlE43d5UfBFoCqx7kxMBsk0dyU2QubXOrJCg-JPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=i0ij1ampDmhEdDGDwd5GCjPT4NImd6ZhR9OiKMUhGBfT6zggaa_faQNe1hdC8HSw1y5em94b2JpA3T3vs042DSDTGs1qyMPrrgoR8HVrbU4v87NpSIzJjKW0ZDuUrK8pBPby-fMNbAdCibdrfFeUPLTXWlG6JCQ_8JtHANPgY-0-WV6Pb-_98o7BQWsEGnw59bzBl4yNIxY7gvSn2sqFDSS_ldgBzgS86TVqdFaVD_AfJ03YZ8Zv3vR8OcJnr0kg6Wtto9ReQ4GMXOl_fvN8UfurCRjtonY_mw8Iog1yN0duNgxf6fcg9VmAZnC-AJrjqpudrqcODvcs9gB594PjqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=i0ij1ampDmhEdDGDwd5GCjPT4NImd6ZhR9OiKMUhGBfT6zggaa_faQNe1hdC8HSw1y5em94b2JpA3T3vs042DSDTGs1qyMPrrgoR8HVrbU4v87NpSIzJjKW0ZDuUrK8pBPby-fMNbAdCibdrfFeUPLTXWlG6JCQ_8JtHANPgY-0-WV6Pb-_98o7BQWsEGnw59bzBl4yNIxY7gvSn2sqFDSS_ldgBzgS86TVqdFaVD_AfJ03YZ8Zv3vR8OcJnr0kg6Wtto9ReQ4GMXOl_fvN8UfurCRjtonY_mw8Iog1yN0duNgxf6fcg9VmAZnC-AJrjqpudrqcODvcs9gB594PjqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eys4azAwK2Fi7BkIEKU-2NoQz5oiVKdQh5F1BVa5UFr1VUI0MlsneDtTDKMcdxNOq8GNz8mwjvzHbxHa-QBy7QHB6eHYXC0eL2vw34DVetECiUtmPtMWtUxCvCia_bqIEcQJQgmVZBbzuxqNQHeOe5YBktapDL40fqiex7aUSySbjc6-F52zF6_edYKmwU5KpCODV9ZAd74lpSkBrYpe5LoHq2wXTk1dDTPEzyhuygjsajO1rNB-Axx0LmhkeiSxbYjvkzpi6HNvmUAvUzcMDOcCEiF3oKY0L2aIdGiqmi57_GIoFiu-MWynMvfOtr4xg7uwd3z_7YxKrYlE6CNMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=BhMpEWB8TI7paS2L9sS44MAXvDFwxTULEDy08HDDMUIbzgecXFiZCWN-g7rP71zQy3HzIgUVisJ5cz_tZ-AoAWcp668OSaRqRg2NltdSsIUECcLHdcDH3uU0Y8o2yK4v_y6z5nGNY-ZcZPgLFHeWXiuza_EYk3qlQLF_BM13wUD-bHUlUOx2jfF3XelQJQR_qAzY22NWzyidVNAu4q3ifTS5HqXFJ5F5TWBhYvdHvCAoSRFjUOIFN5oT0x7m4p5eNe0riWydONfQpREn9tO9CbuAaxanjyAHBdLZ0bxpZrGBW7S9Hfvn4Bz7qBK7kKjOGDXQFDMYVP6OntGQab7uwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=BhMpEWB8TI7paS2L9sS44MAXvDFwxTULEDy08HDDMUIbzgecXFiZCWN-g7rP71zQy3HzIgUVisJ5cz_tZ-AoAWcp668OSaRqRg2NltdSsIUECcLHdcDH3uU0Y8o2yK4v_y6z5nGNY-ZcZPgLFHeWXiuza_EYk3qlQLF_BM13wUD-bHUlUOx2jfF3XelQJQR_qAzY22NWzyidVNAu4q3ifTS5HqXFJ5F5TWBhYvdHvCAoSRFjUOIFN5oT0x7m4p5eNe0riWydONfQpREn9tO9CbuAaxanjyAHBdLZ0bxpZrGBW7S9Hfvn4Bz7qBK7kKjOGDXQFDMYVP6OntGQab7uwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=iYxDZbJMi6hi6ewDzN_58XFJvgHzCncF4792Z85vahI4ruaNYHVWZLEu5uIokMmHUO_UMK4QeUeowvxpKWvFN5Ym4mhSunS9GwZJqpVr7sCZDyfSsJ-k7on9LU_pJ8ixGEdlwaN04y_4jEM0jNTB77DDN38a7SGKCsDDBxwUtjC0arDUXo06dOOUKzSDi52VTB_WU2d4afFsq9Vs-wc_CbQ2gkhyXDIGD7LiqLx-jATcVt8UDBIwcEBsVwrVkMtcuPqEQ8eQmZFJ3CXZ_nFuU-uBVKNybELMqafU_pSDdeVIkm01Cvu1mbF1jrGOT2fud3SZi6Rh_uF-Kfkl0Dsjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=iYxDZbJMi6hi6ewDzN_58XFJvgHzCncF4792Z85vahI4ruaNYHVWZLEu5uIokMmHUO_UMK4QeUeowvxpKWvFN5Ym4mhSunS9GwZJqpVr7sCZDyfSsJ-k7on9LU_pJ8ixGEdlwaN04y_4jEM0jNTB77DDN38a7SGKCsDDBxwUtjC0arDUXo06dOOUKzSDi52VTB_WU2d4afFsq9Vs-wc_CbQ2gkhyXDIGD7LiqLx-jATcVt8UDBIwcEBsVwrVkMtcuPqEQ8eQmZFJ3CXZ_nFuU-uBVKNybELMqafU_pSDdeVIkm01Cvu1mbF1jrGOT2fud3SZi6Rh_uF-Kfkl0Dsjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jovXnYm35Ycz-F9qJZHriJidBVGp_x7_YvvBN5YNHQEL9V9apATtfffZh-aZd7q6Q87Okbh_R5R5-KsZGYRe9ADhrHn8INybJSp6LrdJtnUNNHwcPm0_NKN2OSC4qrDvo4oantizfSdtrs1HKsyGasptqyhjO7m3iq6WDuuaEBTfcu1sc7OJaU0FCiYbP7D4VXlAUU6ZQIzzJF1a-xIFh4I2PEsf6slAxaYeA2mwywr5o8SSzh-EBjt6PdxeV3iWKSg4fHjzJJqzeC9FH5X_UhBXi6j5dtadc5Z5tLWVXv7pUu0kM12ouyspk65r0NPdpDmPUBjY7g0ZwwzQjRTLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KG_2X1_uRzM58CgbQGoxsE81a3dq-DNKf5okdUvtm3iiAuMpIuHmyGFbbtT0df7briotNlKGlkhOVgGtFyHBsCcDcYNkiR1y2RpQ986DQLO7CtOx38Mggw4HeOhQjS50v8Nv1K4s1mol5v4DMOdaMof9S1zy5jx7qh-5dv6joKxvayFzBZmexVbI_AzFzUh7Srfzrg_qc07Ucl4GW6A5Rqsb_f_WkJlHHyhDfMYxSvSe7_y_EuDGQBPTVU3xUpGDqrQ4HvnX8z8WxvKEc17XUaDoI0m_fdbtkh_l03CVxdseiTYdX5zvn9YSuEDJ2UxooGk26SowNR51v_bxTR_Y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWwNKjWppJVTenji4GtVuCiydZ6NOZsAH5vWXWepKePSz_ocWpmUAiRVbSOh-2FijC3Ul9ssDWn3AqmAdjtMLUWg_leYrdRfJXzbHkbeJO3bEXx1WzsPCJcQ-Kvo3MRX9CCr8iyPppYeVMqJqIb7IbQFoIYd3re7P1ebJoBapRnFNv-W98qfjpoY2LASrBKwBSx949JoVa4zbLlIMqcBRkGhr8r_iYlPzwM2OuLG334yWj1II4qRSLLWyBR4icMOrBpf_lULfJJmu2eu6uBRsNt_6PxS9IYj_yIiVME6tPUH0kNr359NO9AeRw9Hyg8n0Z9f4MX0mPCQQb806j-0fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq2CRu96iHrcLoI6mJwTbFlv3JeH6xFT5PB6jVWJB7uTCDGdDIyHqL5TXGFlVozKKfczanRlp62Fpd7scAksymXii3xdCkFXhp_CHPZdtCkYalPmGYU1Si_FdwqVIE5bzmAaaXR6Xlz9d6VjO4QFIXqmhc_MS0a6d81R1smPhVUzOwmzT3aP_VgunsR4of6jC-T_SfI5v339r6q9adA2VoNFjb_O5sujrj9BVRGiKKtck5e_FzFvbIObmMWq3EUj2O55mXTrHb3ntDV0X7o15o5SDON3VfhQfQUeE-qlDrbKRjmCeH-A5V6kTW2oReTNFHEeLdSHHon-bUCKly79xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
