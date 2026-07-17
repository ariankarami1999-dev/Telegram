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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afb7_k6CXkNJeNl07Ulo6wIh5orl64yQ6Akakp9C9EVY2hwDdNDqjArQKvLdL0UCVcgTln7viitUmiJIyR9iJEnScCxcIG13qSkQv4vXYxYKVGAW36617_GGq3DsRHFL1Mc02Ir54TvRXtTHVnji-6lThYpRKZPukEo_Fal72AjO2YNROITuoGA49Al2OICOKVduf5ksYx7WHCHVQDOWBjauFkCiVfXGzC5VCmrdRGyQh7elco_rS4taUXdf8t9pm8BAGV7AEFyOxU0OpzpuE4yXkheK7nA9SVY2I-iPEfaQiY5FibC_5tV09BC8A-ZpSGtikMwZubUl5t__V_DSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYxwz40VJAKZW-Vru1CjCsxNgwkJHxRycpCtyagqzewhbrIICMLSc77XauC5x2leRrxyZcMmXWRTI6HL7EDb7iTGGKae1-BhZn_JvSYKBA1F_mfj2OZAQkIeeoLNResqTWv4vI5o-wDmMmFgLLVoN-3wpkL8r7iHw61Nzk4_scXkFLPuxP1H0u3Ie269IbhQpeRmV33BAsyOrAVaynSiTabzjy06-WpQnRIo2dXo9zEffeFeg12zKeQAHTltaxz6YH_2uR_jUimbkGqzTaHNfzcGctOi9MFE2WDzQEXUNHdnyOI7-hGysR5O5LhNJNj6yjNBlYkc_cRop3BDZIWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biS5Ywz7qhof6LqoCA3uBVcbZLLNEgnra7vF9UBGG_WVZ98a_FAnLz9PvjRAFpuz97j_UXk-qPja4a4Wxa33BWtFibvvwu42vbpHngN-sg5Jop_T3h-fN7YizaXMqFgwFO5adugI6ttW-AnTtnYg0etOQ0L_wEW3Da0KN1QKgOlOJUfCc5zBviAlxHhIiSC4FKy8VXf_FQSYXX5fg7m1xsUz6kf5YXXDemdmU5_nKrsUXJ0lEZzy_Ayuz0ylqNv69lhnaowKmXQHd6-bsDVmPHKm88g9QJtc8j_gsitdQ-c42BcqkFYdrs_H3i4p11KYxmxMS3vl5fWligHMBtxs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-asvDoFw8RCEyjgFhXkjFi5aFE-ExDlhUy9Dklcel14FTVCEwd0S89t_kqhRwcAZJDjnhpXIxx1QIYG-BWl2dtjiGywFbPjffnSk1VQkwdqlNxtsM6MB66u7LH-S7r0MqB40TD7rI2iqZcO25cUQOQtBosYH9934as90JZo-JzFVNL5rCKRQhTuil5Jg0yEplEfwNgo_n-dpxybawvL2xxE0J1gFpB3qhzI6DuF_cVFmGDEEb9SiRfkL_8eET0Vnd1wGXKNbugX2wWXxJXD88-nVV1mYuPUSL-9LjR05OJjCMFPDMvja4NhiksBKOyk9U67bYDZmOmcODIaynr7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSfPM6yUx9x37hkNJckB3gvbihuzY2hX0SfmNgLePtCBzDVs30BjwiwtqPgr7uTeo3QydQ_jBfZbHvdicnBeG53EQChFgScu-VjZvdi2XsZVLpK7fV0Jy8hFbNNJuj9EHvNHnbF9QTn74Ol3V0LtqZ4EiGPO9N77oAaAhnTrjerVM_cOLzYQNcnBqthq5x9ADtNDqvDk46nHR8Pz7Ghcy2zJTOib_Qqp8GyFyQi12ZApxJw8ba9-Sgk9Xs2IwUXkjdwhSo7Glk1UIVRXxOtld0UUxcAaeX3PX-qo-NrEfHZqlvgQnclQegwtigWIy1AktGL06fu5Qk2DOQkzOD7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRwktfwSrdyAjQKbe52zd-JoCOfLvEDh4XgTZc8FYt7_pXkNsA7RaraxkiWoZHedkWMdtnbZLpP1RsVJKC9cWylyqzKp8oCpui56Ac-PQZrd-gsqiDQJQ4basDN3YI6ZGFPiRgJ3s4HKjAZXpu5JdpBm6I8oU0vVQOQQXh5xcF57iCN90qN9D3dKxQCaYdSLWeFb-9S3f0KaTpiX-PH9i4cfu9VJr99xROewrSczA7WZn3SeViqShvYXqpxn5ugYY9vaWwTThPhLcBz-zpCQJCejtuQWypQFF9sXvwW9p2Zm2lG2KbCDb7Ew06InUxleS6FjFzYj6mtHkmrENTYWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuB7Lo870jOcZb50bu1Vo58KumfxWoSD-Yh7kjXx9wQIf6Ga2QV837EKTcL_AnXTUF0idw8CEdc8KUrjtvamdlWhcEPRoZRnGUQo42BKb9tvDStEI2iCBat0tIIoXqg-tu-ORDW4jOdXZOBNUE440HlaVJNocESV4MynO8hTyEimPx4BFgt4bqf4zgLO9LsZgnfhboAA4_0d53fKamZc59NWumCT_HD0hMuXXp0-bPmSS2jTPW9EKOXbd-zrzGIOKBdt7wylimFiuMWyYr0t75VNdTa2V2GjRMBcL5UhwMDrxL-xc4Js5DdCXFRlZULO1ERVLmc2wpriASb8c3_whQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epQydzNd9EDjoDb2RPdC8iHTJ7qhWlUAFyf1n7YK6-1GJYmZiQ4KD2SmSfWjPzS86Ky28bf2TXGOke4Yj7Y4TQybUBiZiYg-66VSy46lwe8r5NeehC1aJACiW5Ma66Qyrnq_Nn_WwjJjmVPwwNAuDWsP8i9QSngNcvHDcr2K5fNo4vzxVk2ZAZoEkjKO4pizW1BGk1wifzYVUrK4jBpFlDmpRhOOzJfliRMxkhw3XbjOBFYHGnaldL3pTi21HfpJHkGbKCuShSuh6IsUH2Sea3VGPGV1GRGtrBA-MftOiP5vPNHUBYr5ioMx32cx96IAjcu2_wIC9Y3uM64qDKkUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polHdQ935e_pGQv67DLjP14UAZLTUGvokZKJcjn_fNLIziDmoAZg1sDPxKSIxfO2Mc8tSCWIFPDl7PJJTHa_5izIpNd7II_-iR5lqRLiwL7rD8lvnlhF3cAIbkQAHIn84c3iu36qsqZTKbKhgGOKPbHCqzBePngrsg5gxfqmYvaBELDWPV7uauJfmZCUHkDJhITPQP00fIByJrf1x9jk2N-qspE_HSG7SPd5mhBAZC0dOVB-ZDyKZ3uXNElgjT6xNjBxUnvdy1yl4BALOPiTielEn4qyhjAuV9ezpIeGVvHP1gNf6clOGCHTOkUko_qeCO5f755ok5LId3DoJiZdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHaH7sOlZTbg7UGZ68QquuZ2zkymAw6AKGIGIJrT0px1lNU8U77IY17s4_o4LwgaLQpoV4BLtsNS_piiosA0S-UA0X7VD2Ldu61Lz3Soedmm8u3vzhrcMSww41x1o3GQqBFs2vmsM-_RyLmYZmx_bHfcdohyVFmOpa5jIfuuLyTfAX05DBmqhbw7actU6xMvedo0GQewbxqhlmTT7YG-AqXkMzFf9m-GGwDgJ1o6O6luWeXX5Z2M9cKmsX8QNckhlYT2gAspiGN86N7m1p_QCJWwtJvK8w3IuyxdnAOfXgxEhXrKh8hGxbnnSUTkLb5Cl9rnQJ6M-gz8ThAJgVbNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPIX-1M9xIfafJz5sO_zlFDNv2vQ7yOQMozrmPvjEFdGgj2b2wiFypFqmvDbtrT8aOxP3av9TQ6fa2zXY-k6TIOemG7d1ZgPg0wf_8aIP8Om0phXg4aL8CE-TPpvfaP4unQPhL0rTuHjqiYwbWNV_qopfaG5icDx6pYpv-IkfaLBslrC8zlNoV39OtmwraVMShVunAkZ1L_jmVUm5zSEgpCAO_j1mGuKYjN7EPm9Bif5xT5aHrkOeT8c0652aLRRGK0s8agN57TXucsD968wA3ub_f0vbJjmsD4l9HLivk71ZnZIVUq-YQveOGxA_mV8zz204Esn-92Fq6-89CWWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdrE0UvB8-mK_hulGrVM43ExbV-pjc4i3JQNnCrDHe5MESaHofxO3KOnkuzmWvmOD7B5kgjlMfSsFJ5D4Om9-257eBAtoB7YufHUy4Z8bxWddCTxq0ld2mArdTgQLVa6vxmXOu9cTSCtHrnfdd2tzdEy0YT0uTXBbl_6W_zjTqy8WNaKkKaG4ACx8ndNdabjPS0SmKmevd4mUVuuGxXi7QL3GyaeSzE6cO2Hh3Hog0ofSS_AiVf6GTIarBVEOyt___D4IA363blhjn4LdEzY9u9quxITJG3RswV03ThDuosYs0r7mj5zpfQet0XJlR71Cph2GTKeSPLDTvcPNBSUlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25912" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELTBhe8-OG8AHt_D-HGyqt4JIQngKLPLYTuIzTLTr_9L_ntIRZdxhR6SX99BDygLpS5a6-EDtoDcH7nFiQ8-BwsFwYKVCtIKvsu1G5tfHJh9XVYMrwxIJwQWPwsMdz_oXkp0HgNkZ9QHdAg6gNcxI9Nxz1KFfVJNya_8N9Ouso24TcCx0zppZfA-SKWvzeGL8oTbMuvViPN0gQAdwqk-qs_2VteiBdLwnI3h8th6LmCqous9fYy-_jiqIYkqruwxQDz1sEQRU6uv8nR0N2S9X555A3C1F2aBoIci71pWo2wMQz7wyPVw9vdvkXLoCOFJC5TtETAkkb-2GjhDFiYD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=UAEgnX65NuTA0szyygHazWJzSDiakpyAurI-r_D5c2FdB5JrY3A2FiD5y6SlOeByILVQKvSos5_Llj6LjBaIxvQQaM3hWZKRRC9Q5BYz2obz9usao3JTrBTWHQNjSXRXVONVKdVoiZW3ZoFAhnZHowaIXy42jQKTvL2jice4ggI6EgylY6ub-RawOYU05YoxcmZydVbaeNooBqx5vmKJWuE2Y8xfsSKjVd2WGMCdsrWVRj0UtEHLKxZHDrv2lBY7HGNxUK3liPpLvldeuexoYUtTJOlZ8U36BJwflm0utBy6xbc4wmFuq3mg2P511hTE6nwTG8DDPQIQ_oaPpAEzEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=UAEgnX65NuTA0szyygHazWJzSDiakpyAurI-r_D5c2FdB5JrY3A2FiD5y6SlOeByILVQKvSos5_Llj6LjBaIxvQQaM3hWZKRRC9Q5BYz2obz9usao3JTrBTWHQNjSXRXVONVKdVoiZW3ZoFAhnZHowaIXy42jQKTvL2jice4ggI6EgylY6ub-RawOYU05YoxcmZydVbaeNooBqx5vmKJWuE2Y8xfsSKjVd2WGMCdsrWVRj0UtEHLKxZHDrv2lBY7HGNxUK3liPpLvldeuexoYUtTJOlZ8U36BJwflm0utBy6xbc4wmFuq3mg2P511hTE6nwTG8DDPQIQ_oaPpAEzEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=uWdROcuNUSVec6PibQmoTaEodV6qe_iEBPjYZYb1H8vM-dJTs5734NNsqW1f6IY9yaDWBMfWzJFed7-dG3faccXZHfvBf8o5Nujt6o35T3sZY7zzKXaWK5WVPI8_diovSYVrLfwZUpTE8aSp-jQOch5nm75RQ1YoVy9AHp5jSTFr4Ir8JltmHIt-okdsKZEAnC6Z35TfdKlkASVJNZk1Qmm7aZTSSXHhWSm75OpXB4pPd-p1yzlZskL4OM1rKtXf2W5lj8liYtRm5S-jtjXhk1nh9Ebewe-HkpF0EBdJPXs034RcmW19UFHj9GSbozbwBa3FchK1NlLHMeS4z5xW6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=uWdROcuNUSVec6PibQmoTaEodV6qe_iEBPjYZYb1H8vM-dJTs5734NNsqW1f6IY9yaDWBMfWzJFed7-dG3faccXZHfvBf8o5Nujt6o35T3sZY7zzKXaWK5WVPI8_diovSYVrLfwZUpTE8aSp-jQOch5nm75RQ1YoVy9AHp5jSTFr4Ir8JltmHIt-okdsKZEAnC6Z35TfdKlkASVJNZk1Qmm7aZTSSXHhWSm75OpXB4pPd-p1yzlZskL4OM1rKtXf2W5lj8liYtRm5S-jtjXhk1nh9Ebewe-HkpF0EBdJPXs034RcmW19UFHj9GSbozbwBa3FchK1NlLHMeS4z5xW6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=M1iGUFC935RneRa1nQwclyo8eQkVbI3Xtc-PdXpm8ZL8LbGJ2mrlSY3xWewlMqRGiIhI7B29rXZV8RuGvN2KPmiWKlJPRjLyHvyw6lLfdZese89Ee8uP5zvjFlcQXrV4eDolAVhzOqOh_NC5esl5CmOW739mAMySzHCXKqAdSicQ1wGovgWbpkuLH_tClqq1ggsEpABdVdmbFqWbz45elCotBmj2lR8cvdHCUqaCK981vKMUVXvryJlY-97k9CBeX8YG3Q6koESMG1w688xXuvlNDe4CjfklQ2GtK7BadbdgUiQdht0__qSYcvKFySLlHKEKlHIGdoHY6pLh4mDuDoADqfxeyZnLmK-gT5VQ1kFRvTxAmFQzZQY6blkueAczYKFvsl5KmBKhlKt4KvtJwF9zcSsMd6Gl7sXhNdfqcsekJO74XF91C4FhBW2AdW2QHVia-ew-29Quami5d0160eTqUHrpvVHnyf3d1qULVM2BCYd86kh9FXf8sDpZLhKleR8RomHnFDezChNfHjbCV0pncBke5gIy40d-HllvkJvYvAgaqFVVxkOPs2TriyTHCrivY4kG3A8sP1aB7R6sCxRTA6HeobEtxJcKMBg0O_8Uy9wqABX8o8WmqfRetU9KouSJTKh-FI8lTYSkD46lT-Pn-JHvhI76nlfdoAsS87s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=M1iGUFC935RneRa1nQwclyo8eQkVbI3Xtc-PdXpm8ZL8LbGJ2mrlSY3xWewlMqRGiIhI7B29rXZV8RuGvN2KPmiWKlJPRjLyHvyw6lLfdZese89Ee8uP5zvjFlcQXrV4eDolAVhzOqOh_NC5esl5CmOW739mAMySzHCXKqAdSicQ1wGovgWbpkuLH_tClqq1ggsEpABdVdmbFqWbz45elCotBmj2lR8cvdHCUqaCK981vKMUVXvryJlY-97k9CBeX8YG3Q6koESMG1w688xXuvlNDe4CjfklQ2GtK7BadbdgUiQdht0__qSYcvKFySLlHKEKlHIGdoHY6pLh4mDuDoADqfxeyZnLmK-gT5VQ1kFRvTxAmFQzZQY6blkueAczYKFvsl5KmBKhlKt4KvtJwF9zcSsMd6Gl7sXhNdfqcsekJO74XF91C4FhBW2AdW2QHVia-ew-29Quami5d0160eTqUHrpvVHnyf3d1qULVM2BCYd86kh9FXf8sDpZLhKleR8RomHnFDezChNfHjbCV0pncBke5gIy40d-HllvkJvYvAgaqFVVxkOPs2TriyTHCrivY4kG3A8sP1aB7R6sCxRTA6HeobEtxJcKMBg0O_8Uy9wqABX8o8WmqfRetU9KouSJTKh-FI8lTYSkD46lT-Pn-JHvhI76nlfdoAsS87s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZIJtl4wcKfzjLjd_h2i0TCrjLOZa1SDWRpTwiB4Mj8DxXjEbATAFLWpL18zQXYEAS8ox92UGAnQI0qpx1oJb-w_DWXLE0HO4lDRTS90tpCr871bDeA1n6qsnKYS5mDnGUk0Vei3hDv_PTHE17u-jccWY1hCwtgmp75vWkSo18hp5TbOLdy5_Olu7XHf_sjv6IdY_eio5-T2LdSv_evVHBV3yrcSVl8Ic8ldc2zAXecQaay0reL4XNUKIeC7TIyuszH2RS5woEc4BOeeqTb4HcaJg1qYg0svqWA9jKKKv76YKcq3IjYGFRaNiKLoOKa8xGEWK-nYwaSoeezBynkEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=XhGIpmXvLHzHMVCvwP8al_419CLGjOJzu4qZtPhHoJaSnmnh-XL4yLPI_wRWM8KLKFVtmemvxg8cMId7WryBkcx-P7Y6odPa5xZLuCobtaSSxANG-VHIgvryq-Ou75sPI5FFI2Dy6R5SoAJiVWDew-4u35fEs4A3WEYFYscHxXN55E8BSQGvbk5k3_3Oquh2H2R0Iz7tIIHWrmNXiDSns2KnhANn_AEM267SCmvNmF0w0o37iIm9KI7VkuPul5HTx7QXVbGm2DywbHfVoQWYQCKHXXussFfOhpexuzGhBh6DH8JSz5U3MM761geOkhgreoVcKaSoju38NMo9rUqokw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=XhGIpmXvLHzHMVCvwP8al_419CLGjOJzu4qZtPhHoJaSnmnh-XL4yLPI_wRWM8KLKFVtmemvxg8cMId7WryBkcx-P7Y6odPa5xZLuCobtaSSxANG-VHIgvryq-Ou75sPI5FFI2Dy6R5SoAJiVWDew-4u35fEs4A3WEYFYscHxXN55E8BSQGvbk5k3_3Oquh2H2R0Iz7tIIHWrmNXiDSns2KnhANn_AEM267SCmvNmF0w0o37iIm9KI7VkuPul5HTx7QXVbGm2DywbHfVoQWYQCKHXXussFfOhpexuzGhBh6DH8JSz5U3MM761geOkhgreoVcKaSoju38NMo9rUqokw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=QO-9YGRmsNyA_a_McEBUwjwy3lOLlSdketrHBAdsAJ804CEfuz4rbU0Mobwq2_anT88PTPnsC1-_KT4-9cf2pSjqR23DDbweCQ24_xZQ6CmwsfVXlgouLNaWT75DrGDHKQeXtyZE-zo1qkAlaj5i9ED2d9zRv-A9ica8fykeq9vDQMZJcGZTGy9OjZBwLjWvZf_SyW5bDa4dJIEg4k_kjyK2iFHfadWMHuPv6p6xfR--M4I7fD0_DpsivkuGVjCiGIE-9dyX0xwgYU_tb65ivJK4jDi7_9LlVk--ZAivCodEDJjp9sG1WLFL_c5tpWvLCNB40Nt3KxNhU-gklv9q6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=QO-9YGRmsNyA_a_McEBUwjwy3lOLlSdketrHBAdsAJ804CEfuz4rbU0Mobwq2_anT88PTPnsC1-_KT4-9cf2pSjqR23DDbweCQ24_xZQ6CmwsfVXlgouLNaWT75DrGDHKQeXtyZE-zo1qkAlaj5i9ED2d9zRv-A9ica8fykeq9vDQMZJcGZTGy9OjZBwLjWvZf_SyW5bDa4dJIEg4k_kjyK2iFHfadWMHuPv6p6xfR--M4I7fD0_DpsivkuGVjCiGIE-9dyX0xwgYU_tb65ivJK4jDi7_9LlVk--ZAivCodEDJjp9sG1WLFL_c5tpWvLCNB40Nt3KxNhU-gklv9q6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlZXFfot4W_P0acVSpzI34PxsSu3oVIjBO17zeqWBmxQ0aFRv1XMdwpDKoAY0XviHERDJGZNjWWom1APXVPWa80godS7yLDsgeKBwtaECc-p992Z6OzOvbZVR9aSCqQmdZxIPxgO8pgFiIv9f5qLBASetOCZP_2g-iXtCbKBTJvFAOW0Rt6Ps4BiryHzcKchbMGqpJcRv7-_IhyjgAoY3Vj8AYSQjRnLe8c7bF0fZvlj-n7JwHJbWXrDfjxGrOVAL2dYPGTr1EceGcMfVmTWbwlIOXLB9IlQo-kCikKsheYcRs5Hv8_X6JNHV6OSI6l0C-7LXggwZE6x0luwdAunCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0DIx3QKGCrNU1G7H9BtsIX6RTIq6sM8Rw0m5lp4OqYdqW7WGC-O9qyMyfL54yvLU3qi_pzlD9ziFoajda5uYtVsLUuwA4GNbMVIfxmmB8fQxnX8F4mGR-ZqhMA675eL8o3EmBPbYXFB6ExJYdD1XKvPkLgC5LXyvXpbkhPth_f7NF76r12VaDR_Rfe-xeFeuHoXjdvbXfZL-FAkrGf4wlQm9eB8ywXTAjA0RMGtqDQEoAEaL7zB1w7HEiNdZpY5sDh9XqH9inf3LMqKS8g_XY-DV2MMRKSi-PM8wZpcyfglDSEcUnASn8JjlVOsK-iaRWi98QCVC3NXxUItCaBB_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeRUSO6GqmnH5zxMTYDFTpe7gEJlJZdya4DbCNSI9c2DTExq7j3i24w_J-PFqd3CK5BNLaOA4AzpFwZX7K8I7JAMPHpEj_HN02NCKODU7skpkv92aJwSkgw7jivmGFKMf8-pdEsO6hVl0K12ZRu5BPmJGHZOkwDBm1rK-hlWtCjOh5bpr4GNqj5m6gFxR9l5QetnURJAwxHRKEqpmLbDZ01IJRMPFsRfm1n7T0gxdl96xQKGBMaDYmk195C4m3vSfVjHmWeDXcuJCWIF8-jQzPwFGpRkur-5SiiholcFU-x-YiXRIGhasQL7KDPM_2WZDDVIsFUSv0xEEjXBRojxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgm5Cb8AkVlXu76hv62ffOfzPPkOc2kXOXAoLmmWCDEOVyCfJcIFUVSz42xZEMokgq0HlVrP6ZNAxQc67VOyzStWqJFeA4FvkRuM8jNSQkFDFBB9fLh9fxx9NhWXg22Fvst3F8z5xx4c-aLQP33IGzgjd6kWlfUjDCy8Sk8i3w-CTujI3EXPVZqJWxivyZbdqkxgazvjFu8YT8IehFRjWU1UYfcNU5nX1L834PUkDj1h7KWg6p05kvG2yz7qAeFbJVhNg5DPhNIGDFBxMBAyXNcFO-k9x0GdonaKQnr6MqTYRBp2NMG2AQJtaV5w9LAbNN8xVn2nFATmLkhlON4ViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJS3r-2zIRXpNyTxJwQMD1v-4uXoU6pYsE49oVhLUd3GcZpxj1E0PsT0hii8ee0b4dvx9RBDIgVWMEuFlnqBWo32XwvhvAuHTIeuXbIH-hQK-rD-Onsswuuz68UK5wQDuRP_pPctMKZ0YojLbOcChrJLjxWSNIUr0iZokcSwPom6wNN3AhNe1heGZC-Gm9dAvt3p_18FXokwzwGpwHlN_ZxyY6OmZKzs92a5A7KTd2bYzpl24zr114lsuJuia1UbY6NmwHBZhu9HKqVFcaQa0c-fqxEnAgXCKDs0laiGJsxmjOcTTCcUyrYGcDtX4rkxWOaXvo2E1mm16ijwpaveug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mik3fz6wMTCUiv4WoboKofJGJQ0w-yEXu6aJAyX2rpn6JNNR1ZsSjlEq5DKC22vHYEjbnYDed-ec1T3V7QCFARjr7HAjgce7pmkWjJPMmF_3i5I1Afrr2K3wRGBrOooUzv2-cOpUwqgKU7DdSLqgiiC9rRMHhCgvWVD4L39fphxCnZP2wOYf_Li4AG9GPGVnfdTOXnIAPoRhBeB5ha6z5PqnBA_5qkus0Ax3-hVuhF_ZBOyHrTyXX7G0xjs217lekWABrTNX_JX7zYMCHlmVEM6l-zFZS7-dnz-_SaTlBMOYfNu-DhGioyKP4gH3gvqvaShbcd-w1sPn7bocP_8L_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=ni6cAGqO7nwfmV6c4BnHMhFGetS6lSEdyzhkfYyLmi5eDFVOimg5OvQnjUfH2xUWO5f-xLG3tgw3O8Nc6rrJ73Bcc3Qn7gnqgi44cxF6KvVIH6DnXQ8To50quYPv3IG13CdoHY-D90zwTHWhCW5MJuCIGM67ZiTQynx7t2w23JCUFObrwXg2DKkt4pG9FKxsO8fokcDq0fvLdnQ6Dy1CDHqvs-zkhsLHrgHjZRAtbwQv64Z7ObNOEtOn7aWNjAfYbEWTNezOATuxPyN3Kduc1E4DZxMVuWEj_vPLRlb0QjBoUguwJ9jfR4La7zFEQdgB1rLwsqzYhI3uESNE_IjIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=ni6cAGqO7nwfmV6c4BnHMhFGetS6lSEdyzhkfYyLmi5eDFVOimg5OvQnjUfH2xUWO5f-xLG3tgw3O8Nc6rrJ73Bcc3Qn7gnqgi44cxF6KvVIH6DnXQ8To50quYPv3IG13CdoHY-D90zwTHWhCW5MJuCIGM67ZiTQynx7t2w23JCUFObrwXg2DKkt4pG9FKxsO8fokcDq0fvLdnQ6Dy1CDHqvs-zkhsLHrgHjZRAtbwQv64Z7ObNOEtOn7aWNjAfYbEWTNezOATuxPyN3Kduc1E4DZxMVuWEj_vPLRlb0QjBoUguwJ9jfR4La7zFEQdgB1rLwsqzYhI3uESNE_IjIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLsmnxNcahwH-ix2UZez0DxIpmloECbLSoCtf9xPhvffbrqAYLUblHPmebESkcZD52hKjh8TrI9SM8Ggc_MCuxXcyMa3gbT7MCL09cpqXT1YVCuv9Aoahf4RI-p_fbqx3HLCHOXQ5xQeJfthAYMJBAQssZ8jBBdvmIFOpqeCZu-cbfZ1BccDbJBsYHqkc34o47syIhy_aHaOrXt4o3_gWHYrmejmPhVh-GNTLwAxO9oE47dtdbYDKZ9rs_YX3l0EddENdSumOLBXOQFEIFXV3YKcBaISKqlDrlFVBPoFsrWTHDv_isowUQsW93NIxkCKfDBNScC4d-5irgyt663r9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3k-971QsarjB1nHvrhAmoLCGmGE9scGQE6gZHd_g1O2GV0noCs3rsvHVoRx9ADG5r1JIRp14n748BlRZk7DgMLDUc1A9iTZSGX2c3KLYDdGGWekturYLmQ7a0mAOb60qcwsj7_YDfbOrBm_Sfl5lsdjOBqknrJq4AUR6NVhk88i-4GmlgvLuNyfv_CTjwRbIyqQEXiiImdZV3UD4HwZpA_FanQS3O3P8Xn2KshECWJlVPPQQm66Jqab_lKVaS2fOYWh2MZ5XYO5rgfxPSfFjE6sElBzQBQDEJuLUr_jnoEZmIT089R9I4IHKRqT0lO4V-qcgE-WRVvWP5a9GIifVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqq1EhAI8ZhFsJoHmTUGg4mURndl-Lu4l2yt5X6pHLoHoe1LZfbgcsn3QJRHxIdHmUOXAh09DPgin3ibeYXY2p8mUjfuXOY0UI50-kmWxohu1QbQ0Q58i3J5C8VIHIAoCsurM5mwmS8H-xTlrQlBVuI20nP77GDTD5xzF41A3YzCWZRNU37fFtF0IEl8fZPLmVSrX4ggKQAtuZQrwyU_NrHrc_EtYmsaTZKGfMue9-3PrMnIzJbb8A68yNs0dehihFsHG66ttfU9JOCgUpPSCZhINcNFpWIlgrrZlK482o_KzCg1w5PPyVnVn7_oYcTEzRleT8rafb6IkP2gqzHRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efFBUYYItJQ1mJQUgICNOgTgkZ56F9rVUBjfy5NyFgkGUI-gzQ2YF4R5t-c_-b1UN3ZC0VL0qWtA7pq_JfajqFo183NSJbsuDnMnVdvhjMl8YQjTAxVTAZxcRtJ9GAbhmX61fxPmOAr2OU9cRCiiJytmbMtMr_YQx1K6dLGwzwEY3TzCtWiQf_M-kUK-ZN_hTWktDp7PUzZlWvSOvmuqwDX589LDeCi8WoHoxsxQSLJ4CymNhMLZbYQOdzTXVsnSU9kXIvuw0MRPlvraReB-sFX4mUeT_vCh7DXnoXSeXMLoJ-OJ2utBI-2GFfUQPi4cuTrlSOA6DT9NowCnIV8JxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXEq8NUOZ07LzTvp9gbDRlhZsTKdNy8hmW3iXfnn_lVg-i-B1HbkYrvUARakYpA1QizW4wBQyeyllYd3sR2g0H07_R17_nrqFN45BC1y59q9RXIxdcQ_ie5XyZ3Mp_O8K6UqBsaak2tvLoGl1l0iUAbm--PlMPlDyRee_XVseCKURExNz8WLdRLjYAeNGOG_FQvPb_QsRlngLGn7xf4Kl90bnfmTr9xamFoGr2qQuMsW--Vo6RdDkMkSQY9Uph9ZZ27DzxXT0suNKMTxBBteredtGIKOsLuZoCknJXnIg_d4WQVVd09Iuj3SW2jeKf_tXW8vIDyDEL1qslLrCOoY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95DcV9WcwaqzkGL5S1neHXYYI8ingB94P1mmN-4hL_CREJiUWzeqz0iij1uTr2bSTTvcJzuh1seqtdNgaqu1oPMgJKnPLNJc1rTpPO0arzPFJwqziYXsnf72w4B1386x6E46eQOhkI-t4EpDyzdHK6tHaDm3hmoIv4gF8z7O4Sve9KRaI5luSSiZPkvqD6tEHVDsvZcWiF0uO7nHzKvDPAzvmn85gO5sqIRZH6sKmXkD5zDf6PXhlnHbW8leYL2JlU71harKVVghzwegQrmd9VRyELXyzMftOWHQe1GZuF3hLcLhKjQxp3d-gxT9QfRjgbutKK8wle2wm08MKklQdN2vkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95DcV9WcwaqzkGL5S1neHXYYI8ingB94P1mmN-4hL_CREJiUWzeqz0iij1uTr2bSTTvcJzuh1seqtdNgaqu1oPMgJKnPLNJc1rTpPO0arzPFJwqziYXsnf72w4B1386x6E46eQOhkI-t4EpDyzdHK6tHaDm3hmoIv4gF8z7O4Sve9KRaI5luSSiZPkvqD6tEHVDsvZcWiF0uO7nHzKvDPAzvmn85gO5sqIRZH6sKmXkD5zDf6PXhlnHbW8leYL2JlU71harKVVghzwegQrmd9VRyELXyzMftOWHQe1GZuF3hLcLhKjQxp3d-gxT9QfRjgbutKK8wle2wm08MKklQdN2vkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpod1uHmK3NfkHvHlRAQyPcmqW95th_c9UDUlLKgnWX5QiXWM-p8JUmAFXVamjjN9oB0PkKyY6TnuBb5YPJTi7-JX7RgOedj99Sv8Md7g016zxGuzA7ncdrM59omjdLqG5wW4VMpzujRX7UITNHL5Hd-4Z65dgTQoQY67atRuZ_iTjjhkhzST5RMq0iX51AHkDRXw57NVlDQXYhR4P2TXXwW1M8CQwCAwVHl92vpGzdUWZgQl_ZWbr-alVKXw6MovoJQWrt45H1iy0fo7MQeegbiAqeh5rUcGSyegxCD8_lIa6CGMxeIUquvQszhsxMeyRPNP3xCCeobRI0YwfeXSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgqXSjo6W-FKlf-W8bX2FEvKY__T9c22snpc9dclgpLAWT678l3mzI4lcCgFfD_v7MScHOzN6GUFoEEnhAWe3s9sruklbQpX6wgPBqHH0fNKrAjcfRTG9pFclf-jxmAFjC6HFTLHpYALzMoxJzlU1nJwg6QGS7zJfWxlNz4ewEPE-0RYIrTTi0pbR5Iv8yXVBwX-U21aSm8IkF3xpncEIjAagKG0w8w7GOKnNphnpZ-Yk7RradYpfbpfpUPBv9N9UI0iKbP6cuVbAfEMMgLttNcC3TsHvePb_PqpRlJ3AJjQamXteoGecOPgcmOzbA4B4W4zsk1ZrhDa-iPseXbK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ocya5Cpzs-JM8rijZKeOKhZiz-UPZ-kSSq2IwFxs2quUWLMZ18pXOiGMlSjjybaiDTgrDeYGhdKmiHXQVgFlMNYP7RjpRsoSW3jyi0reJ28RmqLXeJz9Zrdtj1QhnVwrh2leiHeUIc4PNQBDi9zLxBnsAhjPA0-MjeOzpkTFIJTi0I8qczZEfNpT4uFC0v4WTDEJkH2YOP5J0NvhSeWyrxCwBt3IwmniOPg5QX_O_o_9tmbajagh1RpSjV5AdADyWIh4yU9VypqiQMA-nqU--c9LrJy_EFFIn8Cji--ee9aKK6Rwh9r0ZgoXWZ2QfFYqbZvFchRJlbBaC9kHKb4jaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ocya5Cpzs-JM8rijZKeOKhZiz-UPZ-kSSq2IwFxs2quUWLMZ18pXOiGMlSjjybaiDTgrDeYGhdKmiHXQVgFlMNYP7RjpRsoSW3jyi0reJ28RmqLXeJz9Zrdtj1QhnVwrh2leiHeUIc4PNQBDi9zLxBnsAhjPA0-MjeOzpkTFIJTi0I8qczZEfNpT4uFC0v4WTDEJkH2YOP5J0NvhSeWyrxCwBt3IwmniOPg5QX_O_o_9tmbajagh1RpSjV5AdADyWIh4yU9VypqiQMA-nqU--c9LrJy_EFFIn8Cji--ee9aKK6Rwh9r0ZgoXWZ2QfFYqbZvFchRJlbBaC9kHKb4jaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H45V5tirHLbQMzRnV8NIVVvtDm-N0Em6FYnIq3BF0Qvdagnq9TBSQdr1iiSZSQQT2iXl3FcINQogz3muOqIMx4SV-lRLnR_cN_xXisiTNmYAwfWLEHMlLRdnKh2o20HiiwlnOAjsDfTmwbPFw18lUHfTa_V8zbrkjYmh3oSsMOb1aBT4hWogfVYhZV8ZYbN-ZgukXwOF0rPVlv1Wp_aiaoZ1cI9PAvuJcWrqy6fg8_vEDrn4lGIwv9cQi6hlrfATiZWXnxvAOLZHe37-Y-rb4jgZSjy23Za2l_CyajjJoqrktKTsa7JXQlHdmotynfXiSzOLQmU9fHBjjy7np9zu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=DD0HtkZw2Yc9FXEYsHEN2qw1ivAa-CuJtOdzEYr3K1C5BRp7ogmnpCTghi_C5BUEHSeYHfDA1bDgQmPJIikMnKNtWHjMhkMrXuu1V1rCXc6pm4DXQ71JShWg_xPglfsR3w-m7OMtN9WeYTaye9TVUCZm8YRu5G4oDeGLQWEHUk5fesaLRfGznjWOYeH5-IzhdcHqLHlsHbePq9hQ7_7OzxHrJAQnfA7LeKtrxqncv5ON4zaX-s8k1iv1NjIhqApLuR69uIw6yWIsBth7dd6CUBtaZ6wRMDV_h1uEnZuk3eoota0IhRVShqfi1YFZEL3u3iPS_qLNEnFA4vlpjdO5pitfOM2He5UG4XdAzD6HN0pTHBw0P9zMgeIxq9juD_wISTbVCFn_1dv1nqWRXILklkNFHPCFZJ2MXqJ3Qne_SWjny30syE8so-NdAxKwffN0ylMSBnXDP6WiLhHeEzHwfJcIJZcKEVI9FwDdRDemkki7hudUATi7pbGi8cua9l4snrYsYz2evwu6arBUCmEIQ2h0WrxODUPy2-frQgxky_1GfUDJrR5kP1jnQhrypji62dHTVvR6b6-hBTcqPrcb9Y8X9vfrIOYSM2o5D7ei1CUbx7_mObrRsX789d2XwvMayr65nDTYhAcYsBgIDfI_qw2VklMu_6xFPeOMFIZs-N4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=DD0HtkZw2Yc9FXEYsHEN2qw1ivAa-CuJtOdzEYr3K1C5BRp7ogmnpCTghi_C5BUEHSeYHfDA1bDgQmPJIikMnKNtWHjMhkMrXuu1V1rCXc6pm4DXQ71JShWg_xPglfsR3w-m7OMtN9WeYTaye9TVUCZm8YRu5G4oDeGLQWEHUk5fesaLRfGznjWOYeH5-IzhdcHqLHlsHbePq9hQ7_7OzxHrJAQnfA7LeKtrxqncv5ON4zaX-s8k1iv1NjIhqApLuR69uIw6yWIsBth7dd6CUBtaZ6wRMDV_h1uEnZuk3eoota0IhRVShqfi1YFZEL3u3iPS_qLNEnFA4vlpjdO5pitfOM2He5UG4XdAzD6HN0pTHBw0P9zMgeIxq9juD_wISTbVCFn_1dv1nqWRXILklkNFHPCFZJ2MXqJ3Qne_SWjny30syE8so-NdAxKwffN0ylMSBnXDP6WiLhHeEzHwfJcIJZcKEVI9FwDdRDemkki7hudUATi7pbGi8cua9l4snrYsYz2evwu6arBUCmEIQ2h0WrxODUPy2-frQgxky_1GfUDJrR5kP1jnQhrypji62dHTVvR6b6-hBTcqPrcb9Y8X9vfrIOYSM2o5D7ei1CUbx7_mObrRsX789d2XwvMayr65nDTYhAcYsBgIDfI_qw2VklMu_6xFPeOMFIZs-N4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbozHum30LfYlXswBTWXjW75JgEDK4svLFfVngJxNOoATRMluzRdJzGR8Hua_s8ZJN3L0ZhvmcG3WBTWACGneUiGpW6dJwG6rdrTWbKh23KfCvZOQ53cSCOtxgfaB7Vx9QooF_bOsCcTlEZEwAX-9IpChDVGdI80zGNJLX_Pj75oY6zQhKHzDV3p3HsBSeJkKeBfOQ-NMu2YyIRJfFAg2277rHD6KORL4wlCdynZFkmcudYXnmobDZTz3ke7lJxpDHJ5b1rRIVUVvV4KAgz64YhlfIHC2c9O3ZukDUd1eVSW-cj42UkVIEsgO2DPlR6ioEHIog3JlaY-CJ4rLN0qUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-MDYkNz41FYTuOVZFqYBOcE3zc8wgW4yqFHOkg74WkHJl7iWpOpo05iJ7O0RMvQ9xcRYui7d1Ej9xb6sZgICfcQcNwT94T-jjC6sFVqmy-CUy5fNL_F6DjFw4ftl7mRBk9Rej_kmPAbickfMB_t8DOC8TuqWqrpbOoqgxHkOY75ajDSSf_ILnUMieJa_5lccLQYuyi1beVVrRsplBON34FaX0IrRXRw8Kj-nHl5A5X7cXFr9rkLKVYSOMOBcEJam_KEeFhroxkU0tjjzcwHvZELr-HJg-_KE_cxHdAvkxhBMu1CaL0GLrAYAXMAKZJMjsh9WQRz6HT-zUlK6jtN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUeERLRDAYY9VLw7t8fFhqOpYcnBMBiCRiPHwHLHtgZHWu97NrYzzUaGNI7j7KYnlAFktvNfA7187SZg9PLS7Xde2jwNZ68WeDZJNAIRH0NVKzqv6A6cGjnOtULG2DAHrYIML_iepWn_RxED0fqjZ7IoOcH3xFqcijV5kdIe1R32B0cqht393T0aba6SBBfsTqjfDvQewyrzSXk6Q2deWn3k1sG9QnPNxKOjxg-gTUld4sRyvZZFzwd00kT0S9yIQa7kFCYYEOWl2OfzayYnt7HlSiS4usBsq78nr9WIdWXhgUDxsaMLQ6uvI7iUch-VD4myFxVPQMkeHMLVCEvS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=pdp9qk_go46ZMxDPuP9boekO78kaeZ7VtWHz8THWoS4dqexEA-jGNNWR7f-kwocD5ycJnTz-vrC2Ey_VO_nOVBgB4e4UKDwjksJiuZmJbPNtQe7xX0TvKciv2gRDeev12dOv7AUcGQd8TIol-qWC1nYZ3BOYJjoSayiKw4QtL6mr32dGZjgIoYHQQoeyfFMzZUP03qg_fT8IT0Q6Wgsg4mQYeOjU9uJJC7FaHxdS2YdTwkkFPXMA8FY-LP1Ruc5FV40wBqh_-wavgwA-GFT-5sHQA_SINHSsj0UYQGbO8R1Fji2Os1bI9vlgSXJOYzevZK5DMsBL-MgF8nmQTJu0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=pdp9qk_go46ZMxDPuP9boekO78kaeZ7VtWHz8THWoS4dqexEA-jGNNWR7f-kwocD5ycJnTz-vrC2Ey_VO_nOVBgB4e4UKDwjksJiuZmJbPNtQe7xX0TvKciv2gRDeev12dOv7AUcGQd8TIol-qWC1nYZ3BOYJjoSayiKw4QtL6mr32dGZjgIoYHQQoeyfFMzZUP03qg_fT8IT0Q6Wgsg4mQYeOjU9uJJC7FaHxdS2YdTwkkFPXMA8FY-LP1Ruc5FV40wBqh_-wavgwA-GFT-5sHQA_SINHSsj0UYQGbO8R1Fji2Os1bI9vlgSXJOYzevZK5DMsBL-MgF8nmQTJu0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEhHZ-U_zOOK_Mk68SNI4JkrsWijtSbpM4qax7WOzxaM2TElmL4DWDdDRDwnH_8Vg2B30ld5WnI-iAEJx6NXspnxHInMPEFxi9aLICcPjUW1Yxrn_NmRU80FWDsCQlltvJt5258yg6PMdMJEx_dlOGmjplHSMg3md0lItCqf8pMjK4MA3igfnoeb17kKRpB_NCohZHor9OunBo2lrbogFTPYi5g19SnxGOWsnSIdl1hxhitpV9o8dz65vmiZ0Gg4kd1t--TnMi67Z6i57QwXm5WnrMxUJHRvZ85fJRJESOsrm203_SPh4Vo0N4lxJUctkMTsuEXwL54e1Hqo9oER6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifxMUo7oE8c9pCRkpYelFyLIdVVrojMWOAMVa0NvfRUXd_ASJbQHx8ZFb13tIjBpFNaeZXRKsLweRCo6AuR1a1jc0vGmNguTkTZBDpM1OFeN2LMXh3u2cUJall78emwK-NMZLvvJVh8S77WCWn4JB-VviujyC523kmt3t5IqibpePMMv_rrP9TqHT-H7R0hygutuc4iNX0qbYrFm90W7XzTuSUw5FM0cbmNqMUmFTqM0Pq36dV_AqIaDnPhz4ZtdWmqAjPmscJcVTlcIEVs1uf5ODQGZ4MEtb-_vssmpztGlhayJ6xcmiY60YEilCY4XqLOD2YCrHBqc0UdSbIKw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsjluP3jBlxUIfrYSVuGn0KM9mKAtMcUJrNtlxF-1gwiJshXDmqAJwCNn_57T0teJCGntvYllEBmX1zfl93K8SKLFzFMH4_Q_6-e3nh58NlGduWsDzcf_fxM68xWXLTdbXT-KoBCKMNrQp9tn0YQxv_UR62mpWTJcLLbTGJmVLd3fIYPqT923aPEANhWBLWKc-ojSe4hAUw6R_W0NPDPawh0i2jwQFvpHRbcC2cxIcEiZS_aqo0Jxfoj1k--3hLQqdD1cdxSAG5tTXx-BtH1ih4WFDHzYEp8nsN16CitMRQyDJbA-BjWQNUo8qyILoylDhX4tZ-XZrCgJtH2ClOdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtLYBy9yBaFmX49kvHqX6cInduT6I83t9hKAe0JVE5ie9_q96E_OQgDi6X3TzlIwosN-V_svwUQDFECGV6BMRF5WYj3Mzy4wN9gzrMm8KSc8Tpu55eXF3MJlIYxPoLX037_INMWbKoEMqQSvsWwjjpw_8vC86R8YdS38oiImO1l2kIaiw9dp4Wqn4SlzZAPy2HLXScaFGyf_MvFRtKPDRXZa3iqYAwDXQNFrFgXWlUF9NlW-MKlNNpThaNTO-fljui2qp0AMRnBbF1poa_cA4JaB8anIVsTKrbwW_4Lppq1BveJXyZBoW0LZYkjUA0BQ5I1PIzvnhWiJaEjUsFTyLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25878" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=Ks3s4Yn48QNzcSu9cpiQP7ZWuLMa1l6YnOVimvONq2cp_YtBBKcDc7RlQSWXROQgzWMWFK5KMIGPubTbfR3HnNDNpNsNqhDWmK_TKY1VsMCknXM-1vxzUaRVY2VgurVh310q_itMRrghXqN5f1lctYP1CnwM-7GsdYxcbEl92Fk_ECCphGfZx4hzN46YKjGvJr5Mh4ChL2gr4JWsiFUb0rcI_k53vLX0MlMI6eAUlNH_FGW0l0ZytK1SA62t6g9d1ZeLRLDcMwRdVBVeeCTlAqyIQPO3Ii2NsrI2I0dweHv7pzc7ahhb4gv0YAbkHpKtbSwsa9ZMpHuOxOjG17huuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=Ks3s4Yn48QNzcSu9cpiQP7ZWuLMa1l6YnOVimvONq2cp_YtBBKcDc7RlQSWXROQgzWMWFK5KMIGPubTbfR3HnNDNpNsNqhDWmK_TKY1VsMCknXM-1vxzUaRVY2VgurVh310q_itMRrghXqN5f1lctYP1CnwM-7GsdYxcbEl92Fk_ECCphGfZx4hzN46YKjGvJr5Mh4ChL2gr4JWsiFUb0rcI_k53vLX0MlMI6eAUlNH_FGW0l0ZytK1SA62t6g9d1ZeLRLDcMwRdVBVeeCTlAqyIQPO3Ii2NsrI2I0dweHv7pzc7ahhb4gv0YAbkHpKtbSwsa9ZMpHuOxOjG17huuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNIfHMyeYVUYMijorXaSGDtiQOxpn3jBdYl6JSFMuB8Ep6jMWdJGq7xAEMiDOYN2KXxCxBYVmh-ZqbmfwAD-aM8eCuE902T5KJY2Q9E61dOKvd4oi08moAYMBu3HvtFI7EEKdbdfP3-uRjR8ao4b9k4t01ZVFKjk9u-rR4P8L4q8RKV2sBSU0PgAKdiItqtXwSKbJBQnVK0bao4lY0SfQRdvGJVLrn_mfBrpi8c2W3pAoH6bkgHAGatNVcJv8ZI_EFWpqH7jH7eBWbAV8-YwpIGH2EoZZl3W6xxXVHQXNeN4K8gy40na35cuuo7dgZBydryS6MfD-WaWXkn_x2EiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr9kPetky_nRme8pF9AmwUs339auGdPhGZ64wrD_W1FheFragiy0kEvSdAWK4Er_JuMZQhIiK3vyANwwiRmqaOXkxKXXZ0Uw55oZxpGaO7m67iZNXqxBrEitKAM8QkhxZFTjH8MBueQexZweIhLABNj-GgkO3Oqa1gMH_WzFRPs3D5wzKDT-G1rhvjIfKmGh3EREq-1_Ji3EJqkujTNF_Vv-Z8327vd-p-UISH3b5PYv3Nu-YTQU5uOFwoq_mVzXm2Kt8xjPqZwYDQp4sh5uz7bA21qvR6Ja2p4JFjgFkl7qInNdfNGi-4O2W7Uzbmg25BF57PBk_VWxiPfyfc6nbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmXARHj4zXUftupzyoaEHcZjjA757Q22J1WQ_bvNNFvTJKJpU_K_5ZB4_GbqvnyliNK_pHGy5jx1eCbdkri3BiiY_jHgZ9Ty6eD-eADoZxflGgtO27lgE91DZYyZmpd645HA-zRskF3r2qHrwTaLVyI1odex_8s1XjYwLpHqXmBPZE0Enb-CWZk-HW_ZsWMy_XZ659c0jjgqsSKZYZl8xeKgKU1wZnjQDJ550bvjinoYrU3XTLzeDJ4xVIzgTJFCg6n76Cyv_-DV8wNbxWMxLH4ctU3Q8B8B7qct3SyefcGVSfH2HL-bc0fruiO8A3oGfgCPf38UcN3Gk-ohdsnlTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVI2lIl0EG1rPrSMdidOq3dVuogGGeDs5GSbEj4l6_aHQxyTvr4jMTNAFueSgLfOzzoCNtlouFPcI9382Xa8W7Z3E82FkT6HYMLZ1p3Ku-btriu0oQIWezXkfQYi42ydecMqqIa8mL8mZloxRfNqlfSzDMRoMoCA1G1WdOazCXKcvUqYGuZ9axyE8AolOTZwFugn9opeKtjOwszuI1KLTqOyZdsFzH3GtYkplgx3_RikJOsdGMOu80dMdP25Ki_X-KZKIah9MmqstKfYZwD9jnEgMoyHbze3UgnxPZoVe5wB6HITMhHa0iOHx61po9suimCsYhEVvGorsICAwKUjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrLm_FnODUk6M2DYbbwHg-bMrCnKYC_3AoB7WpO636FgAiYuo3nmrw9CHkgF5WSQfRDB09mqa8rvpk-H1NgFVrnk9pUoHyxzN3KEUuaVdyM2RvtyoR90s5obcrhriGgjhicW8QDnPxisvNcMZlibz0Yh1UFCjQkQbKMTUk1RewF6xpMpoBk5unI4TohSMhglzEYsr2P8mchgfN-ycveXpnwrU0BqlJy1e0KZcq6UWABHkt0JI7uDldoKQt4T075RNu3UtwNP4ijX5Jq_958BMsmPsZ1MuZ9pgNuTB6GrxEVRHVQ-H6a-XntB86-VqgfUZsXhiMyrwNLLBLY5tT2zOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtB1_jzhZ3aaue4nWO1UCvW0mQjJ6m7DFkpEgvC5qN7okV8oUHW77gAt6tPDnuOfqOLWVmGOjzXMnxJHTulX3OtxKn_lGZr9-KTOJaMDfcXmPFcCLQ0SAXYPG8WpJjDUfekigGToGLgTz1G8MCnf3bT4D36O30bto0AHWvJobf22XawxNv_S_I5Y3hwThtlc0TvGfptLGNZ9Z7ZxqZABoPkfEgRPfkhwPIRC4YYZ6f5XSj31ek-8tHhZagMp8iv9ilNXh6UrN-DYi7RF3N-MCy--ByOiTfjuanhUvG7inREUHU0M9WDc1aRjNqFwiN3ooMCiAByIWGlUto4xy9OnRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue6TMVIXGA4cv-TZQL16qdO32T8sZ8sFGF1nOtZWP2MiOzP4ZQIfCbbss1Ok5KYuD7gAGnBezHcyoHVTpsPn_3L6rQdN1V58QglffGiyqnWED0i5Njo9kaVoEcP1ydAVvBmAq8JZMp8L98830uP-dj8LBPrK5ivlIxdYsRfdOXgWNd7jF6zfMhSXUfWC61o17qt7ArlADSyNyHjyc2MKxLl1f22IdXy9WOY8VXohRl4yJj9xAzJYUMT0lvHfcHTPR_1J21u-cxIoiwK4TL0gZBLGOHV3vxvb4oi3c0Waxs3DBSL0APZGlg44Lpb60AuKO5OZ03YNmxlxYfIsoK-DXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=eVpsgk6JJN3KxNMPG712BRndK3__G35jse_kD7XCYry9KcbRSdKh2nboaxtir-2_8qyCZwbhEsLvAhPFCIfZIuxDhfcsDLifhhmwSKxQBFXooIvCowqUtONpvmDo3Gxtb1hqHVtkKltlbEAuk8PmwP2sl9Du5ZUEqt8cqV31cTziYgL8c6llYQqP4JRvN66S-cJs_kHAuph_s0FSdpyCXLg9MF8PdbOxMYLgb8EFqBzQu56hC48t5DXpaOA15aaDdKRGojdtzxEFkPMguc-vcVz-Rhk8hUqsGUuOMYYh-IkhzXFVcTYat1gqTdbDN72nN1IlKyx5CbPXNeHenAs6fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=eVpsgk6JJN3KxNMPG712BRndK3__G35jse_kD7XCYry9KcbRSdKh2nboaxtir-2_8qyCZwbhEsLvAhPFCIfZIuxDhfcsDLifhhmwSKxQBFXooIvCowqUtONpvmDo3Gxtb1hqHVtkKltlbEAuk8PmwP2sl9Du5ZUEqt8cqV31cTziYgL8c6llYQqP4JRvN66S-cJs_kHAuph_s0FSdpyCXLg9MF8PdbOxMYLgb8EFqBzQu56hC48t5DXpaOA15aaDdKRGojdtzxEFkPMguc-vcVz-Rhk8hUqsGUuOMYYh-IkhzXFVcTYat1gqTdbDN72nN1IlKyx5CbPXNeHenAs6fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVZ_rCwqEUgadyvtSJqiDn-0ahh1kDHp8SkbPcqPmKKv3NpYqr-kr7ysvyBrauYxIy2komrMhr7XkWDGtHu7oMfz2hH2_eI5Sfb5Al74FEADzCudojWjMg6CkFsLSFfYNCtOalG0mXNP5oIn-cKFhUJftXemxC3YEYxPQGNOHF8FYf49RXqyiA4qwnsOvUDePwNqHSt5QfXQDnh8-g_XbThNINdFYfMaW8MUIEHHWWRiGwSHqSegSqR-IFE1GPm0AVs2h8uuFrkIdU4n6LPFeJ4XTD8Lv1H-5xOF9uEi6zrY3O-lD36lqVCEK_g2f91TvdYgb4D81kgiM2lE9v5B7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kycgq0v7jhkpxGpxHTrxL8RA1jp7df9dBOd72YOmvDoQkgzaGXkEhwlEaqu1PSnuVGMw8pYvAE1ItngKTgdcMWUl_7llEQed6IgRKt7X2StFW4YJE5K-67h9ALvKlOhf-gqjmls_kXjHKu72I1SnbeKNxxFngsf_taW82I51P9Qdh4a3AgIIU1qhDxY-uDZccubVYd1MMkiLwrXjq9Vj-_qrNCViZyNH5bmwhIkeJrzTosAWiXTI38FlgolniMt7CGOR-NQSF99s9DZPnSWYBdfT8-hkuB4yvg0-tp-fwhWROktm9teDM2swDyFARZb8Nc599M-iSNRN3mlW3jKdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChfF1qOt0vIJH0K-dNSGXbA-r7zqfZC-iF3hitviXu7D1hOki_54Cd5u4NItQiu-540R7rpUAMqxE4FpF7yQVzYLuJ_TiNPzi6u7xZscmM5GPrbioT52PigsGTvX3maeWCtvSmhBeoM4-gdDNmSBDDZKuHCQObZ6TA-eg7m9RzwPhQg5wRQkw6tolelFrPPsJL9zxt6dhumgq2EMA_WIDa3jT67VeCPbDe-jwpn96rX1WGIJBOH-QmYx9VazM1Ph8edfWOv1iqcCdFkKMdYQVMD54Lj3gZZ6Ga54Pvv0w1Dqt88lDd7pwvPh9g-wPOmAB0mTtDSORVMcTyahNxrKZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=WLj7byKGyOTVZnAoDLGGqo-bvNAaLXICo0sAx5ERXkWdmjJofqyK87gJ-cwrL1moPKi4Rq5LMjpX3ltM7nNFX8JYQYbXtWRpi4UWyGWBWN64OyBlhBx4cTqk4EgRrSr1pYNeo4bGrt-L95p3QbmHD2dBCH678FLVZzJfyLVQF440mmL1scOTz3ZnUyDTrdK5B0MTScqAD7oWlWYfYqv8Do0MtXK4ADWMLF_rDzbeDxxLP5V3qFIOdNUZ_K0KmkI0gQ7TjNlkPEyec6PJqAAW0Y1GPif6_KsYf1jtP-dQwKdsoMjpe_qPM_-RrU63HgUTRt6TCQ4uSSvb73Oe89SLBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=WLj7byKGyOTVZnAoDLGGqo-bvNAaLXICo0sAx5ERXkWdmjJofqyK87gJ-cwrL1moPKi4Rq5LMjpX3ltM7nNFX8JYQYbXtWRpi4UWyGWBWN64OyBlhBx4cTqk4EgRrSr1pYNeo4bGrt-L95p3QbmHD2dBCH678FLVZzJfyLVQF440mmL1scOTz3ZnUyDTrdK5B0MTScqAD7oWlWYfYqv8Do0MtXK4ADWMLF_rDzbeDxxLP5V3qFIOdNUZ_K0KmkI0gQ7TjNlkPEyec6PJqAAW0Y1GPif6_KsYf1jtP-dQwKdsoMjpe_qPM_-RrU63HgUTRt6TCQ4uSSvb73Oe89SLBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPXfJFqHY8C8A0fXiTwiTdyLqYXyw50i2Ohl6qnZOjOUtIn49oGqWNGDuSMTWJ3RIoUUGP-UZGIYSSlM4mNTL8gRl31hiTq3UQ8WIN18ehK9gamIkQpR4Smug7-0T2V99moHGcyIeSc226htt7_Tj6uAOFqFcA17hNCnBaQNlMssvDkQCq4PZH-wqafi0XVU7CK6mMblhCqVu5xmuDQwEjq9-TuIpzFg3OxuJWj9fNJ-pXLx7eniQFGLxBCtYTPpRTuHOLVdNV2sn6ZAKR4QjSOyK2f4lHuU5JwxucRN2GtT5QaCqLDr0LCrQX5_mRC59aEmJiFSL562PBl_HSlEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6c-2uLj4rEB-jE0g4WSeoi7qvFBKDbkPwxlT3TJTbanBpirSK0Fzx5L4OCpSwV_K-BKLFnWz7gXrdIFVHzOh5uA0rjAK3Jli-Ithbu_i_6l7kAaIOdRt-ibnV44IHG5dPEtd7b_8SQhZK9QF1vy4XEkrIgzLGZDpaus-qNHLL94RZI9f0-_t3NzXI7WjqlpvUzmthr3EkAi1cHDMElq8sk_4etSf7Xrbpqa-Msy_9TFvoBpUsy3Cy1M8b2sF9EMxaTjiBtLHWKT3ep2F0dD1QpmcPovpkeE9_zDKIHsEQWxluQVELv5D6IU4-4J9KLH7wGLebJn_nvU8SSGd9-Ewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_WWZ0hcqM1NXdPAHaSIj-Pu47W-QeCHwZVgZ75Qr1x0ln29v028PpW-gC2RU7Ozet6w5QKJ5W_D4awzLHAioj2wSqEddmfQhLJuPtWRnaFRI_oVF8VH84y0N7zJEWw-pWb-LNej2D1-lyJzGXZDdLj5uARo4RUS625YDvQrYtg0orSr32FWdXEhPi9vqb030zJdeZjRZbIIYTKby2a_NNoEL47dn3CO6xEaVpDq3PdHxWH-X4sZhWLgrrkm4AsMloJ0-uT1LVUc926I-B7IWalbFlO3sFR3Ojn5TuePTMNF-p2z2Q4L5xOD1tTXWQi6lNVB8olydz4PYJBwskdFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlMC6RqZTlF19F4EARCPCyLzP0qjQZxmghDojfZJbH10GI3BEiO40Ds_pCDDB8JiU_YO597sRtEN0fTldFRCqhd6pNOye60gdB_wxue_n4IJVgOZmiWxYgNhgGmrGPP2a93BfOQNTycHkzlWUJeBlY88sfrG__kmnHj9qTHY4I8MFelkjWXwNlBw5_gIZZRHab1Oqw0Ui_IyTtNDNzx8Ve_5AEDQt0u8IBg6hdBnbBL_tMW6Zw4mXYycL6djlndb23poWd6KVeOg44_Dyrln_Fwt_-Q0FNwiUWlxFW7lqXZV41lKpb5NZAbCF2aAeC3jegtkhT_fgsjz_zwLAPIsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVI7tCGq8prFUl4fjRLSjYgOpT7tp3h96z-_Eb9qigK_AZj_JA5UdcbaAfne5gMxNVYZzMyjPzi7vtDGFk5nDg3MpZIoFGg41fNAGeh7Uv3cGxoDHp3mz3JoHHxrt_C5_pfeIWg8WSxOpLHFcDLb1Ux73gEBLELeQTI361LF5ybAcxYhXW78sIHGtVJMyyQz2Webx_YL47GoFpUHfBPxVLulUK22EX9OBiwnDmNS2aIC17JjlnOxTusXgf61NmMGuEDZ16Si52kBkb8n1G9Cg003PCHtHtWT0kxb2UOyR5TNGgapce0o_XxuimoWkUT3TKTPUq9dAHHidKPU9Obemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZBlrptH_tZlKvtoqVoZyhce_Gx3ciPOHbaLf2H0Kdeiup2Wq9OJiiotbyinnYL79dY3eGxbkqdAbxSeM5V7arCl4hDKTjAtD3Kvm1L1yt8SQNLUmIw4HHBhpC71rDxMTPcca-IZ-1pSPBMob6I5j9DAuEZ5hxrbcEBXxXPIsOu7T8Rc2cu-nf-ZeJQoqZVmhAFti2hihNqQc9V1cBRDTLdGeYHhBOy9-nIOMfjzU5URW0U1BuXhRXQHLhK0Ad56AxAb2lscSN0pM1wovlQCLLIZbbL45TjPNX04aqQnuzChdDbvfJllCtB0nmQvGPMbflPvYiSx2ht6IH1zHP0XaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBZQmT47BA8QXl-7DC_8DvzIo_OSQJD5MXnPYIqAtpILgyt0JLbZOhsozmsuV1Fo1e5aTRbSxfuMLHt4HP4id1Lf_w6DPnvvLL-mcho0eJrxz-7m_G2twsjZl4MG5zaoliW-9iMhJI_TMYo44g0u1D1EG0gDO4IiYbvtl8U9ei6cCEnolHT6YcvLJBFfEohnZsmOs7s6JezKge-MUfnM94x1uthSyRKewzXuSkLbmU_z3oEoL5qDN5Z5864D9Wh3_4sDEEUXJ6152A5f9uE_hR5lChxDCXuS8a5fbYOL-O0ndBYU29szE_J05WYovIeFjKsWhmVaYg6QU_dHaNiN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxEeHHKRvoMKxFB1CDoZbJCbB1uXWyY8y8VvnrbSHwf_S_hzZy_r9w49CDR1_l779F8lUB4neFGddc8WSAgWdwr88CaiZib5LjfiiN4UuMb52ehbC0hl-XTlllhm8w1kEQXhSe2HWK06iALwTaFHVfC6GxmB7gsGbITVVw4uz2oWWy90z_3FOA1BQv_hy3rzeeX-i64Q8cMSKmSapoG0F2N5F4gyccTc5dIX08lHloOOMPM_eyo0_716_uRYJwLzl4rDs81ZuNfOtamOwp8CKOZT2SRzpewYDsmVF7WT1O3lKWWT_4hsZiXxdqUCcITY6VJ2mQ0F4GUFzosVfH8Ziw00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxEeHHKRvoMKxFB1CDoZbJCbB1uXWyY8y8VvnrbSHwf_S_hzZy_r9w49CDR1_l779F8lUB4neFGddc8WSAgWdwr88CaiZib5LjfiiN4UuMb52ehbC0hl-XTlllhm8w1kEQXhSe2HWK06iALwTaFHVfC6GxmB7gsGbITVVw4uz2oWWy90z_3FOA1BQv_hy3rzeeX-i64Q8cMSKmSapoG0F2N5F4gyccTc5dIX08lHloOOMPM_eyo0_716_uRYJwLzl4rDs81ZuNfOtamOwp8CKOZT2SRzpewYDsmVF7WT1O3lKWWT_4hsZiXxdqUCcITY6VJ2mQ0F4GUFzosVfH8Ziw00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWkXjswH0qRf7InBgLNaioVUYTBhMoC79XWz2loPp7FFS7BNgWH_FIjKedsnw_tEdIXHImkW910cSlan2hevmJIcFu9FXwh_vdzwFbwAAAf21ytfmuSUBdn5nqQeltVwNA9QGZYmHskzQm_5pvL4tywr1vbwYgRUHPapgbGk4n4sSvWlYQ1rjVJG_4U69tByPfeg7CJAuHTUEmSrJwVA6mXjRDu0Ox2DK-9IbDnYjEhxWUt5Inx3y8OLjMwwe_7RNLmZIF4bP1-9i0aid89N87LTiOoiCsNNsXLMRpQjeXhxrGD2HvgEt8-pxz05aQ8ZygHLuZbF4xBbIS0M40dUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX4Yztuo6NmeIX6I0a3we3TH5KwFMNs8WGPomD-IEoFnrqMtrcx96LKktNqgsCHSMbVGFH5jfRpEGi1yQNQEqKfoqtYi5DvlGzOLX47s2PssL_54OgYT2dSN9PZcbFPMAZB3sOXVu3swDKU4DqPFqxAwbBmzwb9C0nIkXB8XIYJV0b0Z4OYmlum6fqsYnC2XjBOO60hFTqp2gkmAp30gYv_vMvNovkQsn_s-q1XePQtPo1owswhh8MvdHy5n3P17hqQS4vq_E58pqCVLq8S2_4IL7ocmnU02Lm9WbPO4UQP1w7XG6dyOezna0wLSBFPWD2kZinF0P1X-NfdSpPl-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUm2IAv1t5IFWEV_loplmqloHzuR5rtBHZgRujWe4IV7ylFymI2wlp-vD-IYL0uDFdsuGONWMnTwScTqlthp8avhsHpaQO4ZzBh0cOOEI6_RWdUd8ldNFLsUrt6X_1yipMiQ6C36zqwBmQPX3rEiIyFsZXTSJW5Ork8aWVARWgiCHrX_DDNPe9--L4tEu2nP9XGJ9Fpb3jfGbzAfB0mSMcR_sFZ1ZFfT6ik6KbCi5OLIatB6TERXLrLVLVRwr4yazeeeYNQym_GsKMttTVuOhi7WEz4J9aKIRb9K50m288F8cmWkKAHUZwqwaweUtXs88Hb_8Slhsey-arzdmGEalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOFn0nZ3weBD6gVMjTIMHtlr_BeIDS9nP7sx8t86gk9z1bfavDI5iFbsSyuJgoVlu40bFMnYj9fc8InwnVbcjpICnWLvj6Qr6TLxx73ELVuc3ajMsgqsmWN6nn0fjyPlfZiiwt50firhiZM2q3jXYU_imG1TgxcHn6Vr9iAKpDZmv8LRCKI9BCHGytPpVIzPXlDmq27ntLHOlMee3-6mQ5nOnfqSdUn2krS2nqyHLpCiuc3FYuRqzx49NIk1MAnl2UsGBF5y571_XeJSpfSJnUlfdSx9ZYogASpuz4X4vGvb8O8WoqpxHKuIXrffjDklqTywdVKjrCGOJGqVWbz2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpsPxEogXJnRAi21i2u6_LiABbtNLo6u2cIkk3XaPWxtITf4_JhJWkivoJTYaiRtyg3c4iABjrGQ2zeiyhwNnT9Jgw4_r93vIZ3eaIVYW2yjfaDjEX2d_7l8RCElGVcUcno-GQmjc7RCGti7WnT5oZitEFffyahGuZmJ9wIts47l5-6tG6nfRhTqb1XJp6_b1kvlwUPvFE1xZEJkoqABXhQw_kVjcaK5zUGXcaL36n09NYa-unVedDqxSI8ndF6oRMhPHw5qHXnRbvYD0JZvwAesmAG5f7YwxXWBd6j87xwJFo0MiW0xLT3nAkUBWW2h7Bclj3ojr_M4q0uImgSlYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHxfGa9A0hiDYmdgwqW0CBQ1qng1jYjX0HtxS33v7T_2Phn-5YelfzJnVc1C1cJQpOnPQC23AXwF-AwAGQGBILAyeydRQYVakieeqJLctWxNJ4HlzHBY0rGCYh6Nhzix4rgLrHR9YSPb4BjIfxzFTNSc-A3drtA2hTON5_1A9jwTMxG2q91Mjm16dC2VZ-hojNfq9u7969UHo02Fxa7e4XG5BLM-qgdJtmdxz4Uaj5Xhip0d5mn6ysIeQat-hzD6y-oit58-fGr3zvmnWOtA_tbS8KP3n_mOf6eFY_2kutErIHUiYAS4nRzKK7-h-QrC0fcgc1k8-Q_bQK-MRk4Jlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcJ2zTD6LZJO09fpwcdSywHw9MTJ4qeQM76UQUXux-KBHt7Ky8eaxNbQf4fXQIhUw_Yas58-VEl3VYPt5tae_XWPnoqSTIyW6DBgJp0oI2TDRQB9gQq9leLJLPHyeCjRKiWsFa-UJAtPDy4QstGg5FLGBO-Du3Q_jShB1rGBZp0RWI_SswJ8cfDHIPhEXaUIjXUDI7ouSEtOdEJbiGn3WieO8ts9tmAF5ZUf8KS0DXZsRv9e7_ERX-DMUX558_qPitI-XcQ3wslWah_7SuZFr7DArG_xwvb9eQNItBUQzMmtJVwklN0a-StdLVMiH3p2_pZjWDgcGT8SN23wdQ2zHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K844Tseoel71AeUGJ9dW_jUN80xkJ_5mDeR_-bj11CBx8qtIZSzZr-rEJG9zl3uRFkiVORpz1e0GMVZTDm_LIWdDZKGYjvl-a_QHEhjts-GRcZyjb6vN6nT4ooPPZP90PRVmUit6PcyEZFJtPqENtsjAChUMkVdBu8zPSW7IXFrqsZOEHWy9wHu86VLUBQ3Hf6DQPixST65s_F_veV9k3FxMkePK3XuWbEEzMOxvnC3epdimtrPa8C3ar4fx1Z1RZHNSju8-CbFbfkdgHfEAOjRZk5VUdVLg5_ozWRxnG8-STS1HagqTzyyaPNT2hdc9PASXR1l1Ce9i-pRpSNhV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=JtwRLyB5xok_wdthgm8Z66Xdh2yYjhGzJEQrLRQ-w3WAGUkasfBiuJgWa_fJZJQitjhCP06V02gE7ix5EnXSEZ50Nygk1lrkMZxn2Uoml7nuW9xag1i_jAN2ArNMB8gsCpQAS-lMeqfNbEYjYaClN99l74a-TLGphpc7YykLL3tTdUVnoDMKdJBDELRcHZfRB13jnMl-CJneZjuyn-qXAxEig-prd1_uygeBM0n92XDKg6btcBATMNf2khirkEjySEzGMoNL-warb47vkwKELSV47raY1SRfuMmW5zvDJ4fHWleISQegV7mXVJWMIvoBh8HCAoqzzfEQOgzF_Zgf1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=JtwRLyB5xok_wdthgm8Z66Xdh2yYjhGzJEQrLRQ-w3WAGUkasfBiuJgWa_fJZJQitjhCP06V02gE7ix5EnXSEZ50Nygk1lrkMZxn2Uoml7nuW9xag1i_jAN2ArNMB8gsCpQAS-lMeqfNbEYjYaClN99l74a-TLGphpc7YykLL3tTdUVnoDMKdJBDELRcHZfRB13jnMl-CJneZjuyn-qXAxEig-prd1_uygeBM0n92XDKg6btcBATMNf2khirkEjySEzGMoNL-warb47vkwKELSV47raY1SRfuMmW5zvDJ4fHWleISQegV7mXVJWMIvoBh8HCAoqzzfEQOgzF_Zgf1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVDq2dV_7NdBw0ShXkhcK74bEjKQrCegbnPWcmhNEGiJfWNUz9orbRzPbG94m8vmEJEN0_AxaCd4MPgtbz3MIpFxjrGuB7VZfDNWm7RdpvfMK5bAAXvyTiYQgKZyZtW6in1xjEiqyGAFluyYQXDPE5FSudRMGSYzXTvb93_y9gISTRetQrKVUjolgQArIxmICZkA_h341JoT0aFOLQpT6PZzgxnegtTkisNqtDU6DDUefysE4Gdr3TG4x1buEAi2by4cFT-pLrfC_ZPQM9teYyBHQnMBl0YIEqfx-EQq9F5pcSBdqjEbZV8sgpF-6v1Z3CuOQtClaoVfpOrWqhNB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=jQ3b6SD4XlqbOL0XX99MuLDJj-fW2ssggPE93cRbuT6tr94P82xt3M5mF6me2BnzDmjjqdLSgJn8jwZptr_3_6ycObHL0kFSCcxgzIGyCqSD4s2sV9KhAIi86SXXI47s7rhFKSTZ18hHGAkyx9gH8NkkukHy5gddQ8M8lMV3fTQkEpvBzVt2piaA48sIp8UnuTEmqva_nMm7pHuH9M8SO2gH45RY-8l3C3eLcrbUeeaY1NyBkTvExWQOFsYLm64EhMdIbEYcigi6kfZ2dr1ggjFZ-2MTJdfFaC1i4inBy4qsoQV1H0qY6v4tNn6ouzUOOZxRoZBpgaE8vJFMFTPdmFMSF0STNLo3LbW0Rt2suC1V7OjOnWjbK7fZS1vzaqJpT32biuAjMJHqLunTCnH_WwYQpmM4L4nygFayA1IUKTJukyw97Tv5z1wXZjdcthsXlLLHJfukGLbcoUksxvTvqgdMxE_whV5Bqwi-WskXZ3B4oL-v-FudEQN2cyyzkxjXKFqXnKu6HaDr5XWnwPRNUlTPZfv6zHrv9oRFXViGL0997Muf81LKtGc5CC0w_zpXYvJYEsZ3n7bwb2umntqAc2wAO5V7SDD-ofqjNKZOqK-Qz2D4eg01gdjEefhWmmgXm6Hf-HyrTQ3Z2ITDCMRgq_71mYWeqNEAbIl0GeZfHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=jQ3b6SD4XlqbOL0XX99MuLDJj-fW2ssggPE93cRbuT6tr94P82xt3M5mF6me2BnzDmjjqdLSgJn8jwZptr_3_6ycObHL0kFSCcxgzIGyCqSD4s2sV9KhAIi86SXXI47s7rhFKSTZ18hHGAkyx9gH8NkkukHy5gddQ8M8lMV3fTQkEpvBzVt2piaA48sIp8UnuTEmqva_nMm7pHuH9M8SO2gH45RY-8l3C3eLcrbUeeaY1NyBkTvExWQOFsYLm64EhMdIbEYcigi6kfZ2dr1ggjFZ-2MTJdfFaC1i4inBy4qsoQV1H0qY6v4tNn6ouzUOOZxRoZBpgaE8vJFMFTPdmFMSF0STNLo3LbW0Rt2suC1V7OjOnWjbK7fZS1vzaqJpT32biuAjMJHqLunTCnH_WwYQpmM4L4nygFayA1IUKTJukyw97Tv5z1wXZjdcthsXlLLHJfukGLbcoUksxvTvqgdMxE_whV5Bqwi-WskXZ3B4oL-v-FudEQN2cyyzkxjXKFqXnKu6HaDr5XWnwPRNUlTPZfv6zHrv9oRFXViGL0997Muf81LKtGc5CC0w_zpXYvJYEsZ3n7bwb2umntqAc2wAO5V7SDD-ofqjNKZOqK-Qz2D4eg01gdjEefhWmmgXm6Hf-HyrTQ3Z2ITDCMRgq_71mYWeqNEAbIl0GeZfHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5_NgZ16kBj8HUkqE-ghRKsY5XfYkHx5k0LU3R5bf7D6xcCm4Gu8JStMlfNgIraRUkMXnJS22v8UzKV1TqD-_aygR_VeMgzHRQGJANHyIUJJeru8Ktof2M8kX1ERt_99X9a_h9Wt-_CB0jWOoe7D0b2aOfiP1DSeYDtCFdkiKo5d9rM9fY2kvBef-LX2fYlLJDSTih8IjCyWxGay4_jUZ2Hvb_-Qhd0SWjacnzB-QKPu2tMi3Y9SwQDyNH96V747NiSAl4G01HOynOu-zB0GG_YJiOFIy9boXWCIoE-h902673GiW8WpgikAnxZqieNDhBjEeQnbjRaTrwv4oUc0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzZyfhR8BEe6vMnyYsCVyjmNxeDVsAM1s05ljub3Db3H2BkyF-CcMsset1qb3InezTVmeNx012UuAjWb33cURwx4fdKpdfgbEgI9Oii_CUHj4HGVZ17qW14Uc4UQHGGtnqL7LnWbN7e4mNGT8Sj0jDXxN78x0xiiOfGcCWQAwjs35W7zPEG2iSRietp76OMJdyITuI-7fedUMAg7bgK9bbZOlBSxHHVHRS4MhiPhvHI9UyVrCKPJ5FjT7daOlWhuWb5uj-ntbiNVesv0Jn9krm6TzNByc2TtxEpOOZJvB0tm-t3kiWbQWPwSinNUsOxQUpZu2tXvEfOV3-z_5sAhfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkzIwFzVkW90di2GJ6XipKtKApERJcsH85r2xqFKK7kf5uMtp8Bd40F7bvl_2V-ALuj6Gdow-ylRAEPWxfWilddLSz5DZeW0fRO-NeshDi_64zxC47k3G92ARfkpWERcZBZ9n4ptLmHfwWH170JGLeLVJQ6q1R9sfXnWjFecTPbAn1OyjTyfqmB_H0n8MpRu52O-hQvz_W2a91KS-KmqlnkXYXYefaSVnCqGvx5MHzEAIpm65qSXmgdTyUGuKkkGMZfY2yG5gsVn4wTPRzoz8g_DU3GDDHbYDkEz-yWNgjfzspEahXJdZlIXCK3omd4FKvtOup8yLacxBCWOnJygSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=OXlvFfOEkF3b8Dkt5m0EkDy-qHneuEiwCBti2XrBQ2rTWP_ib4NSYIPKYG1Mzm19tGO4AmutgXo9IniiY0C-cEM7Hm9vuZ-yNwPDBiBYpsvAupTak7hE48nRj7_Ya_FblpVj0alJgRMJ9Sip4-D2wJGxh34oTLRGSdqjEjTr_2QGwUiAqz_Jlte5GnRZstIodiMWvuA43wDx3jP_kA9kkZBHJYs7gDrPZuFm0RLGOvmYnJhEikyWYKIhF1Qhx3sit1fPsbDYF1RIZNTdFg7QLtMUarTa8CIWYlt2a-qEEMwEWJO0Hwi-8NMQ8DsGmKSV5R8rxSU6ti7VCMp7iBRVUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=OXlvFfOEkF3b8Dkt5m0EkDy-qHneuEiwCBti2XrBQ2rTWP_ib4NSYIPKYG1Mzm19tGO4AmutgXo9IniiY0C-cEM7Hm9vuZ-yNwPDBiBYpsvAupTak7hE48nRj7_Ya_FblpVj0alJgRMJ9Sip4-D2wJGxh34oTLRGSdqjEjTr_2QGwUiAqz_Jlte5GnRZstIodiMWvuA43wDx3jP_kA9kkZBHJYs7gDrPZuFm0RLGOvmYnJhEikyWYKIhF1Qhx3sit1fPsbDYF1RIZNTdFg7QLtMUarTa8CIWYlt2a-qEEMwEWJO0Hwi-8NMQ8DsGmKSV5R8rxSU6ti7VCMp7iBRVUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LURi4xmb-aRG7wLlZ_ZSmsg7YGSrNZ15wB--cdGnciQ33X_IFxlMB9izDDiMaRaW1xIlhg0XyspMrBjGOHUIfGLSeZV8Ozyuc0_oQi_NyEmJmxdQyQOgQp0W1WRTz2nrrcJeDFl9mdpii98fn3Byht5SyE6YTf6kFcgyetwhMRpq97MUidPjGcWIwxagdmYLhpuygrxQl8DN96j6MOjZHdrA1iID_-0_SiiHM-BRW9eS-vL6zRg3gUuNbRZ-cEIXD9J7QTStIGeS2wxbs0GxrFRavdYnBv983vw6WI5b5cJ8USLaMHZSzoHdhMiajcjPXW79EwRyTL1HiPQKL8ohGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=S8sfOqpyTkmzC2BlO7_9w0eo0pLzanBoNztVSDt-hEgKDudrKIAhnHprba-dasr_-eDbpgEBwM6fZC_lTScLUHueTby34jLmxJ8B0MgdkAvmypin9XFLyCgZh9e3w_ujcI3XgcP2F5_5sia8kvApWk-9vKx_Hv0MytocMcPxFI55PRpS9FjXso1KMc5MjjFodDCqaq7x_IISZNDHiBWJf-977iI2XithhS-kE9jb29EKKJnGv-eVR8wbW8xi2NOCTYj_BNG8xD-mB92AUlS1-h88rzx6bgnEU4ktMEOP7kjnqc42K_0buwceSPDIBM-t_UswlZUIr54XrffUgXiT5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=S8sfOqpyTkmzC2BlO7_9w0eo0pLzanBoNztVSDt-hEgKDudrKIAhnHprba-dasr_-eDbpgEBwM6fZC_lTScLUHueTby34jLmxJ8B0MgdkAvmypin9XFLyCgZh9e3w_ujcI3XgcP2F5_5sia8kvApWk-9vKx_Hv0MytocMcPxFI55PRpS9FjXso1KMc5MjjFodDCqaq7x_IISZNDHiBWJf-977iI2XithhS-kE9jb29EKKJnGv-eVR8wbW8xi2NOCTYj_BNG8xD-mB92AUlS1-h88rzx6bgnEU4ktMEOP7kjnqc42K_0buwceSPDIBM-t_UswlZUIr54XrffUgXiT5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ0CTmCEOZS9GO_tsKlod5tvDpHfD_q3YSVKn9uMf3WLdX5nZ9C_Rwv9cqxX96BC7__1FPRHwjEYJstxxM-1iNcLQT6lQQ3mNazlsMi4IVSp0a6Yu5BMwQIrgEIyY3SvN-xedHQ3ql0XWRJesoXPgC5UPPQ-402AayUGkBrAPUWH2Ts3u1FdVfSxuUbw6Vj90zobkW-bqEgElgMEiEvDNNpju-xqjonujfh1-Kg0BfuSizpzLLllrcmvwEyYYNjtyA8EcO6mf82xtuUUSFihTn2a8VeB5eIfMPxBFzOcbgdaHPObWFi98pJFgl8EIJnr36qsg8fnrx2ya_3cDuIjWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=Hb0-qHLxdUD3nahga2ZG86bpF_3Jvm-7MocfSBV-F6fgKtAS3P6MAhWXKpjOYmnnguJnNPbWy5XggMMcMElfegY7C789HihmRXZGN6EawfXpOUgrK_oinjNtdMwJ-7lXSSrd33fgxuUXzgfnqOyIF7j_5jtpCG2wQ3XoTsfz4Z3vVclv4x7aH8siyiIcYr6i9njNtDb3VIOm_-vLE2lVMHbN7LmJtzUCkG22-Ao0N_6ObtF5ogeLzvKXNESrO5jG6UAqEKJ6IswlP0Ww65EegzIZpFEDLhQbkO_IffNOOeRAJHhSBUCxwPURNGgae7jrMxvMvoqJWuhV04KeKSCUaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=Hb0-qHLxdUD3nahga2ZG86bpF_3Jvm-7MocfSBV-F6fgKtAS3P6MAhWXKpjOYmnnguJnNPbWy5XggMMcMElfegY7C789HihmRXZGN6EawfXpOUgrK_oinjNtdMwJ-7lXSSrd33fgxuUXzgfnqOyIF7j_5jtpCG2wQ3XoTsfz4Z3vVclv4x7aH8siyiIcYr6i9njNtDb3VIOm_-vLE2lVMHbN7LmJtzUCkG22-Ao0N_6ObtF5ogeLzvKXNESrO5jG6UAqEKJ6IswlP0Ww65EegzIZpFEDLhQbkO_IffNOOeRAJHhSBUCxwPURNGgae7jrMxvMvoqJWuhV04KeKSCUaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=ob9COjiKJmyBvmw2YMre0Y0k5mIk1UQDVwrQd6fIB8m8CHridefZXQ7Qhbo_qI9epgU-1hsafWXuQYNh44bflTNdvMWbCf5p6A3JYYZkm4dH27JEZ63KKtgfQBhfnfRHEYt3Vw4riXFAzR3Wwc9bxGbpvGgo33VvphSFFYjMqWFDDvNrSE3xWO_C9PDQIt7q_Gokf-iiMJWYCbydCkVF3aY3gkS8MbrLfPN8nUYi72OgzjvQbPexCjRlHSv0uHTVQH0qTB0lKADCNiGe4_mD2NBvNrvez5QuKWnDzYaFt-MDvZ58t5GAZyGhG8cOtN1z4cD7Jm1XkwgDBwxX9KaWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=ob9COjiKJmyBvmw2YMre0Y0k5mIk1UQDVwrQd6fIB8m8CHridefZXQ7Qhbo_qI9epgU-1hsafWXuQYNh44bflTNdvMWbCf5p6A3JYYZkm4dH27JEZ63KKtgfQBhfnfRHEYt3Vw4riXFAzR3Wwc9bxGbpvGgo33VvphSFFYjMqWFDDvNrSE3xWO_C9PDQIt7q_Gokf-iiMJWYCbydCkVF3aY3gkS8MbrLfPN8nUYi72OgzjvQbPexCjRlHSv0uHTVQH0qTB0lKADCNiGe4_mD2NBvNrvez5QuKWnDzYaFt-MDvZ58t5GAZyGhG8cOtN1z4cD7Jm1XkwgDBwxX9KaWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzHDO0yaZdIbxAc8APSDgMBDjrMXWaF-90lVVhSJz2To_z-DyjvgUMwibE5gNQIRlIGPaYwUbr0HDjqAbpZX7inxgBY692YUhabCJLwoZm3A1GDwYUKw-2196J6AnYYfb6aA625U62d234BW_mCTXZMHCw32sO2hMn-mbIGdF29idTSZcFsOg8-V4h-KpKRr28w8rqi0uJTHSt393zkPUBrdWIKJej0W8A9z_p46gWcvh7JYtXpiBhaY6oeft2VmrRnqd8RxoPSgD92y1Xxu5IptvPdVUgsukgYrohNoz4rXLMQbEiZhPeeKCyBTnOdmYGdmsawNnLU4PMr9rfpCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/job1-_IZzjYIVbU2suESeFj5XoGFkiCVPwIantaGmOPxwxAGZdM1WKX7Ify0P6-aXySu7kptN6kyJVcsy1tpespRQDIFcMXam8MJMyjMLxezRnhn74E7YqZ8pi9VRuGUUy59Cx3JesaVxHJY1YY6eL9CPPe48jColVMt7q092NNVqnqjpL6f5P6KFiHQmkLlWmbiPJFi3bMFu_NhaNQYjhSTc4_MXaf5us41p3CwT7BD0StFi91g1PzYM4N7J5Kj1jmQAOjqsLEc6gV3OUnDpR6bWmlqrS14aHCXjn_7ee7G4ugvWkEZuiZ9a9iyIzQJ-0WvbWNzNIGTUR9uyeFgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kG1RWVaz4zRWdncF1BNLFcl3DiTKXHzZmbWBv7wRcPnB8FFt4d00VL_f6aN10OkXywjfldpy9rvcW4evM_ZxFKQHcOjtZxl6PMHLFWX0YXVfweA9i38yM-GzIsSZg0RyWueFThLVIT2gJosEmeI_J8OrfE_MS7lMdvlVwzOhwDvBWlg9DOr8LJ_Jtbz48HESzNNrku4eN9lg58X1guQYtsKpmdKSZyZCFPY75D-Ia4cUsXju0iyTWTgve6XyoUGekc_OLcQoeuSIjLMDEYids3kyeuDLPl-DfHiy1fRtM22Cxl4e0-E7XoMiaCjp_Jn4OOHr3ImQbCzVB6c7hP5ocQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfJWZDZ7pJVrxL35aldJz8kSz0_g1P7tAUC6_CJv-OKZvnxMblMiSfAN9N0BWnACXXUpw-SRnmT3TjeVvBLEyz86orrrO3-8g-wD1aE5z-_uXfkfrtv_HqE8kyjTBa4IlWwDcF670OSHPAxJuzykSL_S8fCrpWXcyZjiZlutkQgh1FgK2BdVF3Y4_cr9_EMknOVG2-7beogjTqiQNVdBBgx68l_Z8mOdPrCjJ1eAbw6St2uj8LBcBBJjkYv2g3FOoJ7Kgq2nD4WnRJGJALiF2m1gWWQBZgclIR_RX1AzV14w4oQ1YP8JfL-BTiMa-TcTN51DcRufY69oH3viOOp5ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
