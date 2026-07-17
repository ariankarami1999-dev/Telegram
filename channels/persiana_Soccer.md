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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 19:23:01</div>
<hr>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6wuXWgcOg7Wd_fgB_lWzO1i9GZs_pRfAgLD1Nf5oObsLcvKpghRNiDzbohbz1kKhRxSe-x3936fOo_o66F38vLAvoL6gRTYi7XBbZvqMX3Wo2bouGKiZxZaiVuvgHSLfqAdKFtyw91EuQsrWH-PeZYrZod09IQJw-kiRBP3Uc9QwsAv2zw-ECnx16TXhMD2u6RF83UvF1o2u_FlS_jZ7rrUb6cJzBd3FXihB67DPEm8ZUUZLCA3izCMJLnneUsdAaVk4B1Dd8ji3rnfd2H2py2aYs959lgsOzO9xWWyhBY-IMCvD-5VICDGXzd_jyWOn4pgcMI82m0jH43HOWtHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 305 · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5_KiiqH3LDUvuB6H2rcrakvbMMXzOp8vUbvteXh13K-tsoCTgEsHdgHKs5hYJwz5GW3LYxk3737Lmhm64fHM1ZrwCCyrV0AWByeZcrPcLXhyhBtd3siuX2zFJQj4OkmYMLPYjYtXSBpM9f6jutf9mNEvbswccf5E5Rb9m1WhB6bewTUt4dzZG8rrjMORHLZCbKUFSK1A0-LbU6keWR90NX9m3v1ts4lqQ-zcQH4yEfi-IoVHmMfnFv9m0Y_OjfmSdc8JpRDGR6V7HhYxGoA_ziF42yrn4hfyzW1ecYv3ipb8bSznnMbU7qkUuXrMbrUlb8JRdMTsMxbIjhb2RV1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afb7_k6CXkNJeNl07Ulo6wIh5orl64yQ6Akakp9C9EVY2hwDdNDqjArQKvLdL0UCVcgTln7viitUmiJIyR9iJEnScCxcIG13qSkQv4vXYxYKVGAW36617_GGq3DsRHFL1Mc02Ir54TvRXtTHVnji-6lThYpRKZPukEo_Fal72AjO2YNROITuoGA49Al2OICOKVduf5ksYx7WHCHVQDOWBjauFkCiVfXGzC5VCmrdRGyQh7elco_rS4taUXdf8t9pm8BAGV7AEFyOxU0OpzpuE4yXkheK7nA9SVY2I-iPEfaQiY5FibC_5tV09BC8A-ZpSGtikMwZubUl5t__V_DSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYxwz40VJAKZW-Vru1CjCsxNgwkJHxRycpCtyagqzewhbrIICMLSc77XauC5x2leRrxyZcMmXWRTI6HL7EDb7iTGGKae1-BhZn_JvSYKBA1F_mfj2OZAQkIeeoLNResqTWv4vI5o-wDmMmFgLLVoN-3wpkL8r7iHw61Nzk4_scXkFLPuxP1H0u3Ie269IbhQpeRmV33BAsyOrAVaynSiTabzjy06-WpQnRIo2dXo9zEffeFeg12zKeQAHTltaxz6YH_2uR_jUimbkGqzTaHNfzcGctOi9MFE2WDzQEXUNHdnyOI7-hGysR5O5LhNJNj6yjNBlYkc_cRop3BDZIWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biS5Ywz7qhof6LqoCA3uBVcbZLLNEgnra7vF9UBGG_WVZ98a_FAnLz9PvjRAFpuz97j_UXk-qPja4a4Wxa33BWtFibvvwu42vbpHngN-sg5Jop_T3h-fN7YizaXMqFgwFO5adugI6ttW-AnTtnYg0etOQ0L_wEW3Da0KN1QKgOlOJUfCc5zBviAlxHhIiSC4FKy8VXf_FQSYXX5fg7m1xsUz6kf5YXXDemdmU5_nKrsUXJ0lEZzy_Ayuz0ylqNv69lhnaowKmXQHd6-bsDVmPHKm88g9QJtc8j_gsitdQ-c42BcqkFYdrs_H3i4p11KYxmxMS3vl5fWligHMBtxs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrmhroM3OltksV-N2HXG5Fyu4eEuExEL8qeQ0yEAMbJe0JApxN0yR7A3xizeGZINe5Mt5WhYz8sh_vAhIFaL15pOEPpABsYcUU5jHtYIfRglsO9XYIQAksJSVPLQNdoVixQwxpvQGJVNQsQEs-4khNj4KaKL5rCnbqPLZVbz--qno9n5Z8WQfqEcB1JW8Q6oyPPjmxVCETeIqVdIYEGgHier-8aNeTQqPCo3kNTFZXBNkPzL-U6LRzVi9hNpdaIHGk_VU7DS4buKEeB5t_oZ5sna7hUSlYVkUqxREYtTUvdTLnq9UaQbOutMXDPgxq5hxeF8rQtda0oLRa30oxSkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-asvDoFw8RCEyjgFhXkjFi5aFE-ExDlhUy9Dklcel14FTVCEwd0S89t_kqhRwcAZJDjnhpXIxx1QIYG-BWl2dtjiGywFbPjffnSk1VQkwdqlNxtsM6MB66u7LH-S7r0MqB40TD7rI2iqZcO25cUQOQtBosYH9934as90JZo-JzFVNL5rCKRQhTuil5Jg0yEplEfwNgo_n-dpxybawvL2xxE0J1gFpB3qhzI6DuF_cVFmGDEEb9SiRfkL_8eET0Vnd1wGXKNbugX2wWXxJXD88-nVV1mYuPUSL-9LjR05OJjCMFPDMvja4NhiksBKOyk9U67bYDZmOmcODIaynr7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSfPM6yUx9x37hkNJckB3gvbihuzY2hX0SfmNgLePtCBzDVs30BjwiwtqPgr7uTeo3QydQ_jBfZbHvdicnBeG53EQChFgScu-VjZvdi2XsZVLpK7fV0Jy8hFbNNJuj9EHvNHnbF9QTn74Ol3V0LtqZ4EiGPO9N77oAaAhnTrjerVM_cOLzYQNcnBqthq5x9ADtNDqvDk46nHR8Pz7Ghcy2zJTOib_Qqp8GyFyQi12ZApxJw8ba9-Sgk9Xs2IwUXkjdwhSo7Glk1UIVRXxOtld0UUxcAaeX3PX-qo-NrEfHZqlvgQnclQegwtigWIy1AktGL06fu5Qk2DOQkzOD7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unr3z-bRva4d-mGyAS2zneFhedZ3ovXfsxFD2hU_aSlf_suonjPpVKjIVzB1AsylicMsQ7QxEf0-njUl_Ii4Umw3hko7dzzRGV8v6hvwLLJ3bFB4f8lPNeemLQVm8twIoodGU0ntdfhOAtcNOwGGjpXcemhGFLbbBeTD8swdqD_jZiGu8MfjE5J6zTS21JWT2PeRj6_9T5tqZGHPJarhHRRnMJ0fmMvZO5lP5STq9mod2-tzOxp_u4Ryje7VFSh6Q6kFLfv1cysKdUvsXOXkDRYwVE-6kMYzIPbpjm-ZOOCk04hC5_fusGZ0FkQPkBA6VCm9ra8dWH-zV7qibKiMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRwktfwSrdyAjQKbe52zd-JoCOfLvEDh4XgTZc8FYt7_pXkNsA7RaraxkiWoZHedkWMdtnbZLpP1RsVJKC9cWylyqzKp8oCpui56Ac-PQZrd-gsqiDQJQ4basDN3YI6ZGFPiRgJ3s4HKjAZXpu5JdpBm6I8oU0vVQOQQXh5xcF57iCN90qN9D3dKxQCaYdSLWeFb-9S3f0KaTpiX-PH9i4cfu9VJr99xROewrSczA7WZn3SeViqShvYXqpxn5ugYY9vaWwTThPhLcBz-zpCQJCejtuQWypQFF9sXvwW9p2Zm2lG2KbCDb7Ew06InUxleS6FjFzYj6mtHkmrENTYWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuB7Lo870jOcZb50bu1Vo58KumfxWoSD-Yh7kjXx9wQIf6Ga2QV837EKTcL_AnXTUF0idw8CEdc8KUrjtvamdlWhcEPRoZRnGUQo42BKb9tvDStEI2iCBat0tIIoXqg-tu-ORDW4jOdXZOBNUE440HlaVJNocESV4MynO8hTyEimPx4BFgt4bqf4zgLO9LsZgnfhboAA4_0d53fKamZc59NWumCT_HD0hMuXXp0-bPmSS2jTPW9EKOXbd-zrzGIOKBdt7wylimFiuMWyYr0t75VNdTa2V2GjRMBcL5UhwMDrxL-xc4Js5DdCXFRlZULO1ERVLmc2wpriASb8c3_whQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epQydzNd9EDjoDb2RPdC8iHTJ7qhWlUAFyf1n7YK6-1GJYmZiQ4KD2SmSfWjPzS86Ky28bf2TXGOke4Yj7Y4TQybUBiZiYg-66VSy46lwe8r5NeehC1aJACiW5Ma66Qyrnq_Nn_WwjJjmVPwwNAuDWsP8i9QSngNcvHDcr2K5fNo4vzxVk2ZAZoEkjKO4pizW1BGk1wifzYVUrK4jBpFlDmpRhOOzJfliRMxkhw3XbjOBFYHGnaldL3pTi21HfpJHkGbKCuShSuh6IsUH2Sea3VGPGV1GRGtrBA-MftOiP5vPNHUBYr5ioMx32cx96IAjcu2_wIC9Y3uM64qDKkUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polHdQ935e_pGQv67DLjP14UAZLTUGvokZKJcjn_fNLIziDmoAZg1sDPxKSIxfO2Mc8tSCWIFPDl7PJJTHa_5izIpNd7II_-iR5lqRLiwL7rD8lvnlhF3cAIbkQAHIn84c3iu36qsqZTKbKhgGOKPbHCqzBePngrsg5gxfqmYvaBELDWPV7uauJfmZCUHkDJhITPQP00fIByJrf1x9jk2N-qspE_HSG7SPd5mhBAZC0dOVB-ZDyKZ3uXNElgjT6xNjBxUnvdy1yl4BALOPiTielEn4qyhjAuV9ezpIeGVvHP1gNf6clOGCHTOkUko_qeCO5f755ok5LId3DoJiZdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHaH7sOlZTbg7UGZ68QquuZ2zkymAw6AKGIGIJrT0px1lNU8U77IY17s4_o4LwgaLQpoV4BLtsNS_piiosA0S-UA0X7VD2Ldu61Lz3Soedmm8u3vzhrcMSww41x1o3GQqBFs2vmsM-_RyLmYZmx_bHfcdohyVFmOpa5jIfuuLyTfAX05DBmqhbw7actU6xMvedo0GQewbxqhlmTT7YG-AqXkMzFf9m-GGwDgJ1o6O6luWeXX5Z2M9cKmsX8QNckhlYT2gAspiGN86N7m1p_QCJWwtJvK8w3IuyxdnAOfXgxEhXrKh8hGxbnnSUTkLb5Cl9rnQJ6M-gz8ThAJgVbNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPIX-1M9xIfafJz5sO_zlFDNv2vQ7yOQMozrmPvjEFdGgj2b2wiFypFqmvDbtrT8aOxP3av9TQ6fa2zXY-k6TIOemG7d1ZgPg0wf_8aIP8Om0phXg4aL8CE-TPpvfaP4unQPhL0rTuHjqiYwbWNV_qopfaG5icDx6pYpv-IkfaLBslrC8zlNoV39OtmwraVMShVunAkZ1L_jmVUm5zSEgpCAO_j1mGuKYjN7EPm9Bif5xT5aHrkOeT8c0652aLRRGK0s8agN57TXucsD968wA3ub_f0vbJjmsD4l9HLivk71ZnZIVUq-YQveOGxA_mV8zz204Esn-92Fq6-89CWWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upDnlYB4OBx8ZN9o61NRkZWERhP9jiRrJkw4w5JHtSgHw_U2fFcUg77l4uKk5KYQuWUs3yXJPQzrpQV49E2VuuDF-HWJW5t-em9JcK2RYBe6SC8-itdrQE1XLRmsRC1olYb0q8XHeciVlec11d7JXFyOtjoyrzzgaCHDlZy3OotOOKSJfX8ghEyx_2hsL8NY4jzpDiuZKivg6o3MzpwG3acodZIPSXl96H06FJfEAOhwmf8oX_gLE45e-CpR93ZUWrT5sRmkHHqOpPsZigkeCxlPUdvVEGCRDdm6ln0Lq9PLNMXXohM1IIlFeNDcKLIk_vsqEL0eJV9wevAg0m7pBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25912" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw1lYSKp2RjdE2tuqCUvScnORufTGtDgnplVF0Kp8SiX6iVh4wctEqwVWCbD7H9Rc9OoOwhOgfSJEzBCvRCZNVtPBDB9Wdns7ceOZFCryR1oPbJ8yXu-RG3ddzjBS-6jtOdvXrD3d0vS_2iZrhekfiQJVLbiq0C_PmiJydg9LRJPOsleVFQxxSZqVlJdqAPp4QXrY5N-bETG4Afc47rlqZLz2nSpcuvVxQ04fRbMQCh0JLQtmAIW_SSEMR6hIHloDR5j9gk0MM4XXC81hgR4x61SRrJrh6ywJXr2TSn4uMXVYCbz5sLNfM0oew6nhsK7GHSnREYcjVt8BrgYzKnMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=Bd__d2MVVkpwOSlcOzvRy5fd15HPgmAGu9gNyLNqZipl6PWD0rRpu8cHM40ykEHgEbNCXmMZTIGLV5VFrliiVzlZs0_ivp2erX1FHId5uue_31ZOdnRbS1rVFiGqgUxupJCxFFAqHZetp3_1czxF73J37UUhYy_ZiXqoOu5nl1hcqyTu4N2E73KtTJiCecKenoQ9SMWBhTmww017zPzWj4Tz_Jixeaez3eVo33X8UQ4FEJ9ugcOH0sojf2ynnAzJ_qsQ7siE9WIvvANZ6pKwr_MdWo2Ver55rO50NPWldtyv0u9KSQaPXCBQ70i6CGa0xtGILuKQJNrBRsmRpTanhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=Bd__d2MVVkpwOSlcOzvRy5fd15HPgmAGu9gNyLNqZipl6PWD0rRpu8cHM40ykEHgEbNCXmMZTIGLV5VFrliiVzlZs0_ivp2erX1FHId5uue_31ZOdnRbS1rVFiGqgUxupJCxFFAqHZetp3_1czxF73J37UUhYy_ZiXqoOu5nl1hcqyTu4N2E73KtTJiCecKenoQ9SMWBhTmww017zPzWj4Tz_Jixeaez3eVo33X8UQ4FEJ9ugcOH0sojf2ynnAzJ_qsQ7siE9WIvvANZ6pKwr_MdWo2Ver55rO50NPWldtyv0u9KSQaPXCBQ70i6CGa0xtGILuKQJNrBRsmRpTanhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=GW6jiFY76L7fzaQeX1xMJxQ-AHq7efHqYCtAYWwEaQqoFsjTENe4rNIKXdODhLQNK2PUByl75ZCJmPfPI6GnRG9kgKIPldcsmbHL2wqB0V8p3xvOPslG-Rvy6eZxmQysZTPekXVqjudoAA9rJ69-5uGdJaqBzbu-bv7QtY4_UeNrxpQ_VueS9ga3P3mIRvXlLrlWezaJcb1XXblOvrwdFhJDqE-BBp_G9JpF6kHKb1HYlswLzhB6FrQGmQVcbq8sl9R85DpiW3NP5Cspe12ujnDaeUPsNPdC-S0TzEx7u9ecb0_fI9vmnr1NPRCwhPpw5dSn4azXfdK539dH_JoDTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=GW6jiFY76L7fzaQeX1xMJxQ-AHq7efHqYCtAYWwEaQqoFsjTENe4rNIKXdODhLQNK2PUByl75ZCJmPfPI6GnRG9kgKIPldcsmbHL2wqB0V8p3xvOPslG-Rvy6eZxmQysZTPekXVqjudoAA9rJ69-5uGdJaqBzbu-bv7QtY4_UeNrxpQ_VueS9ga3P3mIRvXlLrlWezaJcb1XXblOvrwdFhJDqE-BBp_G9JpF6kHKb1HYlswLzhB6FrQGmQVcbq8sl9R85DpiW3NP5Cspe12ujnDaeUPsNPdC-S0TzEx7u9ecb0_fI9vmnr1NPRCwhPpw5dSn4azXfdK539dH_JoDTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=CxRWhanH58pirA8aft8Wg4ajhhUqutFID-2m9JatJgG-Uo-VmgdOx6xNKlU8BAqPd77rkqY-S3AQSU8OExFF-sl7RukLBzt_PakWJhR0h_Ftxssx86MkE0S-HPeFFg-FsOmhJ9em-zyBTcEu0_Y_B9lnwCh5h8f02jcwFsd2fMu4ZNuJUoceugSQn1pjZbHIc2M7EkX3QPoh8OcDQT4hOUJoUt33IdVcztwhLUCrGIITMllDM_sGEqUBaHcSewE8HVKfsKENPHBZpfKt4WIZRq1SfM7-GWVakkGc3250wOFzflwquxEJbDP6gbYZQqaQvOqymZG7jGSiuFlTceGDC3ZhDGbxpljofKxWMiOlkK62G5hUdRw9m2w98Qxb4AXBjLKhommNAjaCABFm82Ot92rQb09zOASy-eqj8UPHi7QHX2AM7_IXixT55PhmOLDx4dzyl7kIbxQ9eep4iXJXUbWzDpOgDb0Nn7KTO_WNDm1OR00OaKNDYyw1Ev-nzQ0idJKiVQ8udnFfGtY6rK1WmiTeGm-rpjTTAu_4RE-HicdWP5scv54XztEyULFjWvNgUxPhF4UktBlP_b5xROyRvnalcOaqC5xLxyK2BmfHbpu6EsusdatmO8OC6oWgVmfq3elqPhdWV9hqiLwhhZr8UmDWH3Sd0vbtXvZdOzoKIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=CxRWhanH58pirA8aft8Wg4ajhhUqutFID-2m9JatJgG-Uo-VmgdOx6xNKlU8BAqPd77rkqY-S3AQSU8OExFF-sl7RukLBzt_PakWJhR0h_Ftxssx86MkE0S-HPeFFg-FsOmhJ9em-zyBTcEu0_Y_B9lnwCh5h8f02jcwFsd2fMu4ZNuJUoceugSQn1pjZbHIc2M7EkX3QPoh8OcDQT4hOUJoUt33IdVcztwhLUCrGIITMllDM_sGEqUBaHcSewE8HVKfsKENPHBZpfKt4WIZRq1SfM7-GWVakkGc3250wOFzflwquxEJbDP6gbYZQqaQvOqymZG7jGSiuFlTceGDC3ZhDGbxpljofKxWMiOlkK62G5hUdRw9m2w98Qxb4AXBjLKhommNAjaCABFm82Ot92rQb09zOASy-eqj8UPHi7QHX2AM7_IXixT55PhmOLDx4dzyl7kIbxQ9eep4iXJXUbWzDpOgDb0Nn7KTO_WNDm1OR00OaKNDYyw1Ev-nzQ0idJKiVQ8udnFfGtY6rK1WmiTeGm-rpjTTAu_4RE-HicdWP5scv54XztEyULFjWvNgUxPhF4UktBlP_b5xROyRvnalcOaqC5xLxyK2BmfHbpu6EsusdatmO8OC6oWgVmfq3elqPhdWV9hqiLwhhZr8UmDWH3Sd0vbtXvZdOzoKIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkgPSviz6LJVxcTK-BOkVGRzTfsPQSmk-f8u7jjjTe-CRyqPWqmjGrlTbkCzBTD6M7Q0X-qqXO7CIbBwXGBcqm0REchD6tBeiU5dpzDceiSdRGNldHcNJsqOZsEglxP3BYyfCrSqEMxBUWJKIJf4g6XgxvWeoW7dZHRMeaUSxktrLpHZNnkxHKcGKeTMztVbBOUtIV5I4tYkav9e43EAqhXhKLV9dZ1P2qgQq_SjWlaYGEWKB9yMelozoXgwYRT1XbRcAGha7K1vdcIDZb7O0CU3ENybr-tZRt2OeSYa80jKUANuVlQcmPPa0bZ66upvkxSn5YQciGmOVFQK-LZDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=hyEiY8b1eNhwdftE3mQOuxdyNRHjG11IKhrtf6vL7pdVRUeFQTk9KyCEAO0-uZ4T8QaWIdTgdLQftZ-qbYrnNp3GjtQ9a8nqqDo6RBU1iQMtK7UIgr26A8ptpLgBVMV5maDEqI-0HTKL7r8phoN9ojKzvQ-hjkhnNPqMb_PBUQLz-ZMZvBh6a5PEmEhjHbqf52Ht2MlX1_QeYSqWJ7y1Kb_PgxyZ1XA8v63RHgSQcjT7OIktWkVtq3MOeKa1Y_qMxA1B17TKv1rysTEBrD1CrlqkX2Zk4wJS2m61cuOGXiKbCMTdhQVq-kWxo2YsWxeXH8VdVwiGoa6RI3A2CnmTfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=hyEiY8b1eNhwdftE3mQOuxdyNRHjG11IKhrtf6vL7pdVRUeFQTk9KyCEAO0-uZ4T8QaWIdTgdLQftZ-qbYrnNp3GjtQ9a8nqqDo6RBU1iQMtK7UIgr26A8ptpLgBVMV5maDEqI-0HTKL7r8phoN9ojKzvQ-hjkhnNPqMb_PBUQLz-ZMZvBh6a5PEmEhjHbqf52Ht2MlX1_QeYSqWJ7y1Kb_PgxyZ1XA8v63RHgSQcjT7OIktWkVtq3MOeKa1Y_qMxA1B17TKv1rysTEBrD1CrlqkX2Zk4wJS2m61cuOGXiKbCMTdhQVq-kWxo2YsWxeXH8VdVwiGoa6RI3A2CnmTfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=UP0rdBzPbDPQhOSjHVjJ1QMPhjdKC8EIKJGjjtmCwoxF6IAARuhq-GkL4Z9lJ6aQ0ViEiQVzlo9zgGGpmVG01SLQaRbUoDXczF5Ql_poorS8ytTk1ZkEPZR5hNIKEpqRYpS1VPJT63U39T-ilmFMvEAN0CtSAxZjXPXxkRv9zZnQbSuDVYCa-DaRj9RFJ1zidofLvXMrPMXyGomsTH7t8B5CoPrcJRU1Nec1YsoqUm9NZYjWh8XDKwFeX4U_ir1FzO-6FTx_94sPaBaKAZdwKpPt4MKcBgXJxccKF64VNvs3d-9kvKjIWsZt24Csr69SQ33LAI8aUZ83_9be9i7GRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=UP0rdBzPbDPQhOSjHVjJ1QMPhjdKC8EIKJGjjtmCwoxF6IAARuhq-GkL4Z9lJ6aQ0ViEiQVzlo9zgGGpmVG01SLQaRbUoDXczF5Ql_poorS8ytTk1ZkEPZR5hNIKEpqRYpS1VPJT63U39T-ilmFMvEAN0CtSAxZjXPXxkRv9zZnQbSuDVYCa-DaRj9RFJ1zidofLvXMrPMXyGomsTH7t8B5CoPrcJRU1Nec1YsoqUm9NZYjWh8XDKwFeX4U_ir1FzO-6FTx_94sPaBaKAZdwKpPt4MKcBgXJxccKF64VNvs3d-9kvKjIWsZt24Csr69SQ33LAI8aUZ83_9be9i7GRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eg3HclGECPrjGrCdkOyaQ9TUAXpGZEMA9MJ7jlDqujVxoyjs9UpD7jJsPjosDc23isb_8XtvvrRcPjxGJIMyUgFk3Jwe2MJaYncKUE4dkQQe00e5YKYYAMwMoNxuBN2bYnr6tYjWovBkaDWRuhacJLrIAmwzr21RLDdJKmr_oZnLvj_oSOGaJgHOK2rHUBr8f8_JtD0_iYK7eBSaniydAlG--NGI0iSiBfZ4HPJ_7O2vmdtIYr4MXvpgeBiN9BySLRvI8f1IyzDe1lIsObJg1NS03BGbbjaJ2-lqSBTTIz-cW7ambYw8RfIRxgN9_qls--WaXCpqHdLUH-K9GwJ0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3K1-DsymfioKtEHTpzLrgn_iRE6jsjAs137sMkwVIUIqW-PHIdGnWKiU3BMbUCQ-HIVi3LTxySxcjuoXZ1K9UMRO_8bRhrdJtHZtK7FifrkO4yqGM9jCrf3d6JDSB8o4kx9dSstA9ykKkOmaPZOhcBvGPkSsxBgFSK97xy-vcrseA6w7AOcqgwr59V38UoUrDAjTdfmF-EF9Mp7uDchC4_DKKreqkZllMfhd2QTNb95dZN8U6KNuO36rBOpbSHSbO4Sa9CIh5dujW6fXwOh4WYf85_R9_o-udWXwxxoAGSeh5yvHM4akVjUVKgCO1piarYDKO5OTBCTohuTfa_wRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSeEqlcNpXx3vKa9-Gqtsnmq7JdEYgPfoapPDgil2EouImBXypxgZAGiGG5SkRf6okLzgmf1V68hpzcX3qPRIK7tnNfhs041MujpYXBdoOi_FDhgBC7BOxVekCoqMLDWrN-tssNFvl5ChowGAKKePXvqK0RLNdwlerffNWR3uKjcj1isvroIaaHErPvagb75dWpfmRhnaXWnGlPVLaam-rIf23T7GkOmN96FPgwBJZqTQM0Gp2HcypGUB9IJz31dwByRajcSW125E98qXsGLD-cEoTLHI8bnylMoXfcmO4VZ9EJdjsvvW_vKxZPECzTGtskEl79Y_2156vj61IFhaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7GNEnPiM_z-8pOyQwJer6rwZNwKbEjHivIgcOnCXC6czmvQI6tEhYB0BgCP1ZyqJbJ7k5qWY2XFsBxqRPO6y1IbyveqFmRs_JchN__n1VVx1bIB--bo1VrXYNIhzKW43jXn3qCJBQ8TpiWSFxR5uU0LXJWPUgNDcd3eZahN8HA8MIBS2wYWqu2lOv57dR01oSXeJO3GnOAD_KnplyG-CtgR7BWOXHRW0p0g6p5JzcQwWiYJra0VyeEoMuxcM1rjgKw__XdPwT8PQXxb-aiXxK7sX7oopuuXQJysNoNg8hT94zz4dL7n3qXfvvwrwXiSMFnfgtJ1Nhhf4d5uX5VeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKbKBgUX5-9tCmJ2knzkeQa7ZuFgfL2SwW5VV6uDzvece4Oco0tJUsEV4TuOyFF2sMnrcHIq7n6Kx3wWLlDWyOA5alDlTMRFnDPR6dYz9MKnXAJmQtNQuAgCVvGpQxLl6Ka554BMzmbOHTTNutfwBfePpGPLgNivPBawgXr3PjBjMEjUhsxqBgcDP76AsNtkQYdNYst67CuOVD7T9uGT_g4_jknPhRUDiKpqw4dwR_kFCcIX34r_mk2Y8XRvE7HGJ3oIpatyXhuwmxZYtspCht7LMqB8E-whFYil80i4C9-dbfgJhXHRud2Td9kA2ktxgMmVFXDYHtAkJuCHTCEdDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcbcLCvptECpW5q43P5wQtXX0jidVF6Xi2C_dr7PLGWqQBMpnqJ7VpbiVzLN_HLxl8W_6JdYFSs3ria0kD6WpfP7IeuvnU45rX8F0UmaD-An1WH6n0hADXpiLVOsbtwvAJJFoNfp-ljCq8xGRydBtaGxrCYXdIRlgDqxXdf5SgZNjqcpuZP47Y76hLpgrofLctfRob-cQJjcYBesxGH6CeM6-CeJ2mRy0YrGmU55J6KRfIJTskms2dsRlWXpCA5Si_6KRnOwYpqL_AsDCA4n77vZ-uDWAbuVCpurvdVnCB9LhosjOindpnkhrlijs-h2SWlaU8fNNc3ZgBrBzWbmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=qUUGq-MahKxq4Lo_4fBxFW46lb_DG2GVy9Mdvz5yrUpWaf2CoCsPaKsw7fOCVmOO2d0LE4xQNFTLfqz094vc36woDYtiRVwffSOFaA1AEGB2X3c6WIo4UgjD-QBfP1gBJ8tfffJvkrhzsWdqkVPlJObiAoffc4gqUN8BFeNM-vcUKO5_x0z1NzMhmtU54ekraeJ5biaHFVNiJviGt6iVO1zccv1RvA6DxMtAMpe-MQ4GhFyyZi9XcVLYhGYAHxMheW2rbq_lrD-zkuRJP7gqZ6-h_pUd8lhfUm6xWvP6HodRZYRzegxX15fjtC9L56fWtz8GBoUNL89CcjocvncqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=qUUGq-MahKxq4Lo_4fBxFW46lb_DG2GVy9Mdvz5yrUpWaf2CoCsPaKsw7fOCVmOO2d0LE4xQNFTLfqz094vc36woDYtiRVwffSOFaA1AEGB2X3c6WIo4UgjD-QBfP1gBJ8tfffJvkrhzsWdqkVPlJObiAoffc4gqUN8BFeNM-vcUKO5_x0z1NzMhmtU54ekraeJ5biaHFVNiJviGt6iVO1zccv1RvA6DxMtAMpe-MQ4GhFyyZi9XcVLYhGYAHxMheW2rbq_lrD-zkuRJP7gqZ6-h_pUd8lhfUm6xWvP6HodRZYRzegxX15fjtC9L56fWtz8GBoUNL89CcjocvncqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5HBMk5_ETOIwE5TLeXh0e70SwAPAWm9_0bURFS200o2SctAYK4mKke-dj22tfO49cYYxuY9O_O0v80mPv70D1TP9IoL7vXDP3x7CTVfb6-iS5tcurIfSleWON2gkgkq3iruQnYLGFJi40zu4dEMzJPO-USY1UmBZGk9bbQWBYHahUwfz3F2oq_yT17t5bz2c_qNr6VGBaC4-a3l8glgWtxsgQSmRvydUvPwDbBZHEROdVQ7xegGoBisjeZXMkBtbj7FXTwFYq90sMT33usKGIeyIQeIbJbDc-wWJ0witzb2cv2cdhu8wUV2RZwXJBPIVsFD2R7az_10TCvkP4cecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugVOSWOMRlGqNk5Um5AZxSq89080FsAv5AcKK3BJ4wobMoTEhlCJS7wFkPb_QW60pwuB3dEYiDGN7BRJOFdk5yiY3-K3Xm8LfFD_nNGD566oh5HL3OCb5AhsQTfYA5XYMsjGOfG-Mxfmy682-gd14NoJnhFPKeLROj5jWlcPG0-lec4Lyzjb6vdUNmYoRvCuZarAO6-nzQYwhvlo1V8uFT7-60uLtE1ALqeIsZ-RneHAMW5EilI_v61lBlY20C8Q9avTKm6Fa1m8Tn1kScngFUbhzkFv2sxxVCWAnnqrh3j3ysJOXmRMrmjDQOo-hgnGEN9AeO5aMHAWRzL56Zo5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfalRz2xOlDH0VVLZ9qXxbv3ngph9G61imfCywKDuTbtevhW6EsEA6Vr9Uu9Yf6fQuNJmr_8nPPBV-nG2tKbPE-piXIC0kwRAXyPXBaJD_HldY3tyFBG5A3cmMkqxGEybdAuPD_I9inGwbPDF3nRiXjfEBEFq0Q-k__2zZ2T7vtarN5fPMx_IRve7LEPUTu5uOcMKXuCieewY0pYEoTmdbT4u6O8h7V_eJ3_37jOHqLYmcD918_1kLUkcMA4sD37I_CSX4jFS0dNaskNCJNxGt4jabzts-h4ez_LG3htt-PZ-AGsPIk5w-7tzWCV6zafH5xyklhwiI0Lb4SpkjnoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LveWeCvsGBpqSbMxqFuLfbQdoiOlUoHGeX6SabQmpllcQx4myiWWrAvBLfCm0nj_vIjfRE7OOsRChoYeFBan_V1eJEykz0AOMLf_gX2yjTdZBszXjv8W-_h58VQLjfIBKBOgMh3IfUh3T7IxmHYOcSCgvxtSFW4m2lv4L25xOpDkVPMk3wazwU2BlbE2T_Fr7SGaY5cqFRWZIJK_JChsZ-qVYieyB9myC1l2TFBMqbcXTbvB0pJ2rlgJgt73JHIJs2Ys9LV4qs_r0M9OJlRvkLKy2LzXAUZ6xlfl0rC2Y4EwRztLZ0FUXG0369-lEtTYPxS5EfPoUven6DqDjGQiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxunYPqGAvMYnOie3Fd2-kB46ueoDRXGON3cbX9sWQxGlMmL2qV2IoEpem-mVahKl6POlVjfWpb7jRfNic6rsv6r7CialAUJhfdzqihA3VegtP1Bp3wBY163OqbiTTklk98jajLaWBoFKYby8wr8OmTA3vG2ErWMwgZ7veuQoa0n_D4kPBesafwZsOQqqk24QOfmmJrgr9nYoCOniM7uJ1xseE-AK8H7yAOOvJUWVXpVc2Moptcuj8yFt0ZqQiS1ABaE9fNetT2PdEWS_ysPxpcKs6Gaj6FOvllzLPeQR478oBh0VqwwdI1H64dHYh9iXI6W7XEiW3Mx42SpGo0HMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=np3uQKPqdA1Ou6Kh5NJATjx6iCqE_tz8HW6kbQEnJCCio_Ja9RsNzd9JdRGM7EKlsPW_DrwNFMIZFHzddB3zt3KaA_0bdPdNqP1O5-bMHp9HAeSKst-vv8kiyzDrCu7PmckXU8-BBuRRNPKVo_SwMjjHO3jCZo8952DCS4adXgTZc3sG-kWME_5qMzdk3wA6Ial8DtIBP5-Bf_vTZW2fjYUUUe2n567XWD8vksdiU_CUFJSskahGIwyhWv-6hT9bYXJdhYO5TXhiklzcfNx48XScTwWgaJWQhsPMwv9QY4cS3LgPpevO9a5StN4RMpodH7Yzt6tQRNtf1bll9MV2IybphWqlkY7eVIUmYhRhhlac3kbCP0M2Qn8JEpIVU0c32a6hQ6b_4mAwT7orv79O3qG8jqSoCh5L1PRH4wrUowsF15OyuoVQCtq2Tov4ciTfjOO-Jaavhh2Hx5MT1IjLNKL5FuoskcKew2RyV34-Qp6tfGNMSbLFqMyOdImNLl6K5UO8k6-Pc0n3Y9gcIsx50SHhXv5HVYAVEq8QUV8cnwLcsV2XrVsHs55D5cRySmc-RH5JeWNkN6SP7ROc5RhUpVtvf8SwcmFVmEX4gwD20ttliEqvlOedVC3ynukxnZLd0ZhIBOYKk_pRGoF8JyqCisqbSoxeKAWwOt3gap84k_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=np3uQKPqdA1Ou6Kh5NJATjx6iCqE_tz8HW6kbQEnJCCio_Ja9RsNzd9JdRGM7EKlsPW_DrwNFMIZFHzddB3zt3KaA_0bdPdNqP1O5-bMHp9HAeSKst-vv8kiyzDrCu7PmckXU8-BBuRRNPKVo_SwMjjHO3jCZo8952DCS4adXgTZc3sG-kWME_5qMzdk3wA6Ial8DtIBP5-Bf_vTZW2fjYUUUe2n567XWD8vksdiU_CUFJSskahGIwyhWv-6hT9bYXJdhYO5TXhiklzcfNx48XScTwWgaJWQhsPMwv9QY4cS3LgPpevO9a5StN4RMpodH7Yzt6tQRNtf1bll9MV2IybphWqlkY7eVIUmYhRhhlac3kbCP0M2Qn8JEpIVU0c32a6hQ6b_4mAwT7orv79O3qG8jqSoCh5L1PRH4wrUowsF15OyuoVQCtq2Tov4ciTfjOO-Jaavhh2Hx5MT1IjLNKL5FuoskcKew2RyV34-Qp6tfGNMSbLFqMyOdImNLl6K5UO8k6-Pc0n3Y9gcIsx50SHhXv5HVYAVEq8QUV8cnwLcsV2XrVsHs55D5cRySmc-RH5JeWNkN6SP7ROc5RhUpVtvf8SwcmFVmEX4gwD20ttliEqvlOedVC3ynukxnZLd0ZhIBOYKk_pRGoF8JyqCisqbSoxeKAWwOt3gap84k_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO_4dwkPHjL_2UWfbOEaqFFg1fUYIQikyNvvVl6FBEn5NHKH61Mo41dO3n61qYt5CootCvtCAYb6VpGOSmTAAhY3vqaen_B0jdYT_ZOvRLvI5QmVythxwo7eGUOY_BrvfF0uW9Q1MR5jqN5Sf2thnaMTLDquTynb2NnZOebeEoupqk17aMatFk4JE51ccJMhI7mHZxUxOZaaQHffvAvCm539GK0V41blgU4-4VByvOIvQ_e_1yslDrtWMMcxbFmSRP1Mrp-WUH_OLdIHlrAkTISMDIKHevQDiJmOJD4NFDO39h3y49GesdjE4mvP_fo3UIlbl7MOs-ND_jEy56oCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjrkbJeri3m03sISbuKmNhsQV8ZbRfilknjVAVRX21LFcfqC1may7QQBx_m3UqLaWECYDh1o1W1jWT6zLfJ8bZqbUsdZjFmVoTVM7aQjgBQ24VnxOq40tDMhiSZgyG_CLU2ygjDV1-M596XOMl4CNd21UGhEThyI1dsuNSRWnH5OJZ7t5U2yT07PJUtARva4YA0F7QJh5dibnZB-q5hXxBqaE31srSQrQVo3g45dgQdcfhg6ZpTilXoFCfuI4SoSSVl60MEEVbJrrlIUBtrv_imMMvfUYwmtN7Pw1-rpx17tzbP52J4ff3xAFFJ6xiDT5P_XKaQJ83WThTSO8FeF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=swuBs5-sLEO0Hgj3Sz_prClE8rc665NdcCTJPO0w_Rs7GPqMw_aZkkI10GSb1onYKHXnqurtp3IqiS2QQBbOMhn-B1Y_DtmvWSRsl5XfcjhMYi6rQ2Usm3zZWVFbOjnYy1X4__nSWBpZESN78dnpvxICCFf7WgDWHkB6DgAmWWMamQuufUJF5BEPDSxQQ3FmBvdIRWtFVcX1oE4WFyxNgcRF7kt56ggK0uW01D7GfMz4uiy3jp_XW5NmZhRqxegCi5mxbZjgU-y5YIZptw116q1s7hWjpMk0cNpihvxBDFfCkWKTthJhLOCFBuitNRPAlLJNSWAo560femyaMb4lBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=swuBs5-sLEO0Hgj3Sz_prClE8rc665NdcCTJPO0w_Rs7GPqMw_aZkkI10GSb1onYKHXnqurtp3IqiS2QQBbOMhn-B1Y_DtmvWSRsl5XfcjhMYi6rQ2Usm3zZWVFbOjnYy1X4__nSWBpZESN78dnpvxICCFf7WgDWHkB6DgAmWWMamQuufUJF5BEPDSxQQ3FmBvdIRWtFVcX1oE4WFyxNgcRF7kt56ggK0uW01D7GfMz4uiy3jp_XW5NmZhRqxegCi5mxbZjgU-y5YIZptw116q1s7hWjpMk0cNpihvxBDFfCkWKTthJhLOCFBuitNRPAlLJNSWAo560femyaMb4lBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQJpTQiyTP_xRI6wMjA81Oot8WnoJLpCBnAAS6IdL45AZUvQQEzndVLWIPzA8AqgHrE4_JQW-mPd5sme_jwYnrEN_rcaM4nX9c0gDreMV5w__W-unIZhmgNHzBHMlRVkSeLXf7qP9a30TkWPOz5mtCPmg91WLypGo4tRGVOL3ghOEnEzR5uHNFxpgzHrDTAjy_g8SpE391XMsRgGFibRVXx1na_2ft5vh-F2kIQM8ipHQD_k9fivAvNPoh95uRNNtUj8bc46Ne6bL4g9MmUIN_vefA8Vj0RYkNHTr-TopL46ccnWtkA6LxyFU3jvWYFd1Fhyo8cOLwq3hWSZNym3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=JdJHVcNk5z-TtmNVUgwFWdS5z0lfrvKjHT_vY4Sod3y-j4xetTEavwW9TbVfqO3dE4WPwnj_eMP4P7nub8zPlKVZ9ZYYjtmFHZ7JD9ogmcNlXVW8g_lY6iQXw72SHANYTpYOeUuZFzqHdW4xqdbGkwT3BpQ0OZH-G39A-umfHzHPo5aQwSiE3wtXeBd0VV9-VyVomYOGYDE0_4EviNxNMkfRl9FePlOkH1Qp4y4QyC7kmfgMiJGcQCpfZOi6q96TIZWmPhPjgNiymhn4Y4M4WcAoexoFrwVTCNl1qPf7M0c_mqNpxW0yeNtsQsK4lmFmpRKuyD7GgmVtj5GpoKW59IoIlzDdUMHpBHMqCCeWyBaYhhpq3Qsvt8pyzGbmbI2RBR0cTpFHe_UNYkBWfJOyH29XDatuGlQ9iuDi6mMjtPqEYH7O3vPIrcqaf-agIinQx_5ndNWckL3UaoZMkf-lGc9CDNfyJJSeBeoVwdKtBd25o3EH9B12Ud03lPebD4x6is4xdgnXl0Btg2KdRChSW_aVYoocizyf9LQxTTtEZ3hH0Fv4fghmoAB4diG2dwHqaudJyAdDePiBU1bheqelJUOu1_1enIjuT764I5QGi1mzWzBXV7FgAk2ugPOsd06579RIjzDyAIOOhgWL4RLgIxiTRTmNhGrZm-X04_5E_yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=JdJHVcNk5z-TtmNVUgwFWdS5z0lfrvKjHT_vY4Sod3y-j4xetTEavwW9TbVfqO3dE4WPwnj_eMP4P7nub8zPlKVZ9ZYYjtmFHZ7JD9ogmcNlXVW8g_lY6iQXw72SHANYTpYOeUuZFzqHdW4xqdbGkwT3BpQ0OZH-G39A-umfHzHPo5aQwSiE3wtXeBd0VV9-VyVomYOGYDE0_4EviNxNMkfRl9FePlOkH1Qp4y4QyC7kmfgMiJGcQCpfZOi6q96TIZWmPhPjgNiymhn4Y4M4WcAoexoFrwVTCNl1qPf7M0c_mqNpxW0yeNtsQsK4lmFmpRKuyD7GgmVtj5GpoKW59IoIlzDdUMHpBHMqCCeWyBaYhhpq3Qsvt8pyzGbmbI2RBR0cTpFHe_UNYkBWfJOyH29XDatuGlQ9iuDi6mMjtPqEYH7O3vPIrcqaf-agIinQx_5ndNWckL3UaoZMkf-lGc9CDNfyJJSeBeoVwdKtBd25o3EH9B12Ud03lPebD4x6is4xdgnXl0Btg2KdRChSW_aVYoocizyf9LQxTTtEZ3hH0Fv4fghmoAB4diG2dwHqaudJyAdDePiBU1bheqelJUOu1_1enIjuT764I5QGi1mzWzBXV7FgAk2ugPOsd06579RIjzDyAIOOhgWL4RLgIxiTRTmNhGrZm-X04_5E_yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa_VzXenlx9BT_DIbRlaEsjsX1m0bD__udzrAST7Di3sMSqOOlZMAV72CFTHD0YfB3lJ9OV9XzEcu2z0jkWDsf-Uo_WJnuSKZZcSHSLZ7VhJBOO0kOxQWzuCKjpnwItTHoFvapmuP_8suc7WgXyfOo2a1sRDksEq8iaBY4_Iftp_ulDoi__u78-Z7UcG9LwjNJeIa-nvRwZjM_boLw4iWmXtC3z-jjitsDBCaZMBMASZUk6abzZkG0qA1_sPRyQid0jAGIRslG-SXgIGv39MYP4z5O_v-YG9JEOZdgF9SeWJTncJ_QuJHx_yiYeKPctSzjA0fx655j1yuBLuIcIlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYSxi8nrL6r4qof9b7gRwxBsH_rq6WAYrj7T8E95dVCr_RhEClm1_9PNFUy4-tF8oqQOqKoSPiQcbOLLzTswCRY6hFFbcUfZrCcHWONIC_-7kkxlR5Mt_-pglNjvbL4lLRuOqWxl0A2INwxyr28-FhZtIYduOvMXLqklTDA4wXRLC4UZaPkly8Uv72X87yeKQQuJwvyD0EXsFwSQijmc7CGpL1FoBhqqDm4keMBpCmQ7B459te0e2XXp6OTgGColM92nU1rPNG7zayG_zRL6l_KWoQMq8OERaJ3E_nq-2-q2dXgT9-fptbeuxIHRcAR51uKaJqCGjd1Cb2XUWv721A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF7Dw1Ij96XCCgFhFjL68nbV3jq3XYWI12YM9tqUzaVMNmkFjMxJDN8BfnzJ7XyXj1jXr3W7w7Qgroi-3-R7rrk7EkN_FmXxxsAAtwegm6f6qUGFORtPha7YGzuinko2C_lnIo5jGYsEK2H-HLAS1DBQ-UfwPndh8Bmxw7xOpcqUmWp0A2LBYwqqUdUFGe8oyIi7RubLcG-S2Au6CkQd21LT02d5pvUmp7U780MqXb3ej8xdUtVzqahYkO7y0RoqI_uadV9GMQL4-1qGLjyWfNJ28_sjsHIKICcDjKxrS3WswGFOM4jqO-C-D_8aZUfM7T62XEV-pLDtC-Rya-Wx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=plu_c3tcGVGqehK7fK_XBwhqWLHQ-cJaJAsD8-dS4qXd_muw_IU6MKoPcKDOw7Gjx6AuX0136lWZIxrtSQeHZrQ8mpNFrLSW4Q0JTyOxjt8S-McVD2ve9ldxDE5aPlhetSyUD6QL07ql_iFbmo0DFnIAgCGIriIt72e_rBvUEHytOMteA2VKI7CqqImYMe9KBhwni0_g8LqJGG3o2pBQ-EYZPRoLOit8iSNj-0thvNf0Q_IAaHSuOvAz6p7vBA0XIpi6mNQbN-5pUN5zgVHqHkz6fsfLKleXycetbDCM4R7O5WWy6wlkU4ySaBGYhXAQq5sk_j8ubZ8yGF4Pnryi9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=plu_c3tcGVGqehK7fK_XBwhqWLHQ-cJaJAsD8-dS4qXd_muw_IU6MKoPcKDOw7Gjx6AuX0136lWZIxrtSQeHZrQ8mpNFrLSW4Q0JTyOxjt8S-McVD2ve9ldxDE5aPlhetSyUD6QL07ql_iFbmo0DFnIAgCGIriIt72e_rBvUEHytOMteA2VKI7CqqImYMe9KBhwni0_g8LqJGG3o2pBQ-EYZPRoLOit8iSNj-0thvNf0Q_IAaHSuOvAz6p7vBA0XIpi6mNQbN-5pUN5zgVHqHkz6fsfLKleXycetbDCM4R7O5WWy6wlkU4ySaBGYhXAQq5sk_j8ubZ8yGF4Pnryi9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlCA0NNctBzI2LNffTiu00Azuw3oYp_HuBywW94jJCvPvFfN_dYs5TRNYuCC86r94sQcnJ0bGfHUOCiP_ChYBM4PXuv0rW6Dtl8K0rYAt5wloEov3L0q4tuVGfTZBcBVxHxLxTkJKPyWLTpbRnyGlX_MoOHfdi6DZthATATCiCjNAW9U-IptvUa8bsg2SdSVjlgnkdCuUQfYmVedbYSkqKlnJclu-cMmwF2H0oDArNVwWmNcvZpoNfuxAMn5FkL8mwyOLzTzmkk3ueW9PqJ6jBCgkgvAFX0RJupT5dsHPCJj1wfrXA3GhugN71gDeduQlTU9qOoPji5m47SiGPi6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXBKDqrGJepolFd9Gqo4eP2PIoDHzqraYcrfmtuC_TTfHLwAFUOwH2ovdvY3to-o_aFBXtYPsPtFlJSqUzM7jWb76g788Co2SvwVDFy2M6G4O15N3VbKObhyZpft9C9WSgGr9rxnOcmQBv2RgUAvEn3vy_wMS7khDmbX2GVuAFVnhlxV4Kbdrh3IGsjft5APb8QGZrI1DWygoFil6yn7w3Lyn6qr7YJ7pLWSYoMcVuux_KHWn6zbyGMu8nH9_0NzIXMui-rubBA8lpQQO-OOeZzqeC3SsqjwEOwek5gmw9xmO72cQhptyvHeGzOFKkqsaCXc_NVMSjJMSi7-32YviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu7SLYY-AuK9NFUWplYTMqmsAaeL2dM9PqIXJKX-p1XG46Wc67UNXX9gHWV3zr6v5hmDBeWSFlR1syw22eFpMzUqFG61tl3A6FejlC5JFEoVMWKODf9SYnJEx0i6l4jVf7HDsD23ooOw7PgrcWj5q-2PuYJU9s6JGK1Ec_UkJvZYlEm3VJ3ncPUKYPVIDgawy23bZ2WGIOIQYaEoY6kS172tSKUG2BKbtvq729mN2jc6WQCWArdYgTQVAhoR37cWj9zfu45WmnhZhkKMH4JwqO3JjeLhcp9jZemQzjsY0gK3FHim4muAl9iwam9IMMSxKKVMVh_EpaMue0lu6pMVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25878">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVqpIg0_rz_QZg1TooQcoYa1rOgJShXVnoxohezVpoDR-Dl8FIUXUMvVfc7h8cluIylFzhoFHCJnpfz6ELwnfktF2SQSKnp_DHUw_18EaOakTaiGuc5TSk3rMuqsG6bJ4oCYyfyfE9skxPxM0YlCQPcBisGNvohmWdlIYlGN6tSt9dgnvNGpe6YAjZ3r2VFEew1Tn19IO-bEMK8GqQKrSvh18IM659b0DWmWG17BIejUuYbYExRwxoDADcZxpmAErzGsL7b-csFORWHBliubpad3ACHootT9iFI3TCM8DYVxVswJ2SVrR31Nk1PXWVOYUBLab2plWrXIgFrcPso3HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25878" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=SSpcdDIOIMyncHMErWLU6ndfSg_5XUtJ_2m-W8pifcoMobr2nHZpgLVsC2aSvnnlQ5bgZr3z0oDHyhiQTQDI8pj76FCegPWUapF6rq9SYGCgyX7CTzMqadve1p7XjQ-3BnP70urVHOMdIW9xwU-BL1Uv-MAq9gKYuSSFJPU-_K-INLuVTmI7yoYuhavU-D6kmGUMN-jHWJG0z6DHCrO-ECo0t-bsOypxgFOQP_O4YeVA4dxXGv0BXKjXkCJZqRsBhTu3O-NpvY9u_EelGZGbvFFxviL6E-GyCYnA_VGyh-YpRB_xMFUzMyzY6AvvtnohMlwZt32U95bjmXRs6TAmjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=SSpcdDIOIMyncHMErWLU6ndfSg_5XUtJ_2m-W8pifcoMobr2nHZpgLVsC2aSvnnlQ5bgZr3z0oDHyhiQTQDI8pj76FCegPWUapF6rq9SYGCgyX7CTzMqadve1p7XjQ-3BnP70urVHOMdIW9xwU-BL1Uv-MAq9gKYuSSFJPU-_K-INLuVTmI7yoYuhavU-D6kmGUMN-jHWJG0z6DHCrO-ECo0t-bsOypxgFOQP_O4YeVA4dxXGv0BXKjXkCJZqRsBhTu3O-NpvY9u_EelGZGbvFFxviL6E-GyCYnA_VGyh-YpRB_xMFUzMyzY6AvvtnohMlwZt32U95bjmXRs6TAmjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwRMrzlYK9GdKz3ptWAqRqQNTozRPXg1rlZYmlNjGhlSrzAO9oOkALwek749GL3Aege1GrMw_fcORe79Bar6-D9amVIkWOAnPIGb3O7B6sl-wqS1mu1UaSiXZGmiEPW1uu9_hnrJv2ImsDdaeqj_kx8For1Ina_o-Cjtm4ARY8mlRmYDYvvMdVxKwlgrBM1fEW1wc4CAIDLJRFFqjmZG5UqselZZSQPUvzkAq7K0rb3fxpCTSNwg4--wM-IvMj09BmsTu1z6Q_enaFqfQtsQq-fop1srQkX31JtLV49LWSDAwPN9OGVwErCHbXG47yt0ljsEWPXJU_0dqqcNRHt_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRGlMo_5vnMEtAztpYJZeEdDV5vBK5RHAQfHzpKqgj-_SdtEPEt-LUa27t4-YNqaaZBB8Oh-pbR_Jy8byxC1jsSgHGrxTD2l0s4wUmyk2iXqT_dMtIWwN00up3s_F8JevjFuL1fPM4NdhhHevcvHBPAinVOa04kGK9IKD9Wdmwfu3_Xo138KkeSICAaMPkbefWWYwgYd36Dlnvys6MOhhGxkB-a_8tBSaWE1MJjK2m2qCt7tfdLCzqoaFCCHMeSq-BLjAkoiBbihQ-Tr8xY0FiQx-I_GpjSCHKI2l-uR9Cr81DMxBr4C85kWufCHbjjSqxjqhI5cclHI3ad01b_CEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCMLVxL7xC3VLHYpTg1FTBpBbvc04ceup6dmECWRJi7XsgI5VKNBJ-5V6cgIrwx2Z8IXy1WCoCPORP--QOKa8X_fblqWRlQCz8fhGSqyDnd2vT6PKry-cIiuNvxZ6GceQFLYYLTNNK-6gcIJJlIJ7qdsL_B2RiraUhO54Szgx4Ge--WN-k5XgyAkw190sk5Aresr4bsbBGb8a6_G0MQaiuN-mGJ0PpbQuH-4Mw308wkaihHWvyCX1n9K7Na63ZYWWO2vA6ldoJLXGcCUMrEFHChYsfoo3ybc7uJJpiIoeUm8yy66BO2eZYZu_Etj8pY-PkFYr5qKQLFJUR-BO3u2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4-_C004KrW-0VO-Oipkz6mjJWOcGmuT57EskpvwKguczic7T2A8FWtqX-ax347d0dxOGiGl7ZxW1DUoqshd6ow_1jyVa8CNM1eTz_P1Z0-iiscR-XkJIcpis-U9aZpQpHlItfah_iErqGMBwjPqxfUzkgyrL3UM5r-T70BWstToe8X8zGP0VKgLcysTbaSqswbZWrCECXcya36UupmZqUn-S-uSJcv8zIMtNlnxbDMaPSNcJJ5MzvM3sOUFX31i8Ahl8O0zWs9x1OsfjLGCLTOkfuzGndnh1lKH-rtDkua7kaGt6DBLS_ZCmVJg6e1K5K6UgKNCQsd-nHeCpd5cyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKaLyYXO2R4j51TmwODpRFxUyFxODozbiqez4VpZiPDLCqvcs9u25XcFB6qGTAsU2o_fGcdtcJtoIPCXFRG4qLpT3we1fcQHs9WujfT-UJY43xFBgUPT3GQx7n6VnLnoYX3VNQG3YTC_X2qQ12QhKs_u0zW4_nmKLpyfDuM_Hid5EDFYtJQHa0rnu5n6u_qegAMeK929lUf3M1x3fLj1eXXMRHnfY3ZHznOXPy-KkzrEXs16uUA1DOxmncNt7MB0EHnoyqwAGG6V0yy2bKt_RgXvbJHZWFatGaq4uCkq1Hki2MDLj1HX2toWMOojujqlRM_P7gxUUcdS-yQ5RVQS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBauQzxFL-WfEOYb_sf7LqfiKOt90iA8BSXKO8dgV6VZ3xNar9bqeLPg5S5bd-zmXCmlFjR5GEwemX8hhRH8qc02pkXnhhWCiimtMDznbNHBoBmNOiXYpbjRgroM_u1USQhDyN-JMt8xbZxLuS1KbbXwJlQiVzjGvvhSdJjUhJgwWcwDK-66PZTBe0-XclFkKXe0ydfQBzxauslq3w6IafaFzxypL-NGFlZA35SUr7rekrLegAPi_vtCWzYT27mw_zaGG1AVm4QZSm4gDANkVMAdVeNj5sYhGUzlsJOXe3LzMGimMDCwlx1Gv2dwUsEPXYnQzB-ySULug6htsXG2Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD4Ue5E7zB6xdxqOOnQbWGvmOcUJnH3bCRM9mMlWoj5g-JNj2ssETruhzxZ_3Nge9LJf7-Csnd3OOJ73LV97jeH7tKZKArmWpUuBpE6NLOzSsK_xdu4WEoxGnUWHPfDM-IEQrRBnUR137TT2qTxa4-MA08qyIzfya7EKgGdTRa_eMyil8LLxI3Jn7gw3YNQ9_n05n9WxiSYDKC0BlPgQ0le1MSdMCdtuODjSGkQj4OUlQ2tWxs3rg13WBZWSmlUofbAxD37GZdbRxxwurSVmH8bzkag5559aCLDdy70MBNInvsz2p-xcMKHhNpHLj7S5uojjCSnIOdBFDfUj1J8M_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=AoE9HAXW0nJLGoieWM19r6Sbm-IwEVSy109lxZlixRJggkELmr8d7QJfkj7OdemQSXzOZnCiFCq8ubVxRpfNdCpfD3GpRLJMA729AcY1dzoT5cBpsynkk4YSvjMtsnT_35toO-RbYLPiEdm1JF2Aw4prk20OEHPXuxTP8zIZORGT3FjjoFaQLWR2KF7VCgL49jY9mcloHNEEUSz-B7g98wawh9Gql9UgZ6h03gLyeimLnea8hTA5Jgtm0EDPIXcaasYbXobWlIib8Nc8_X9x0fCpdSfHWMTG67Zdc92IvwvFi_tQdii51o_tGcjG3X0-HVYsY-b8_XYtCgChhcgHIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=AoE9HAXW0nJLGoieWM19r6Sbm-IwEVSy109lxZlixRJggkELmr8d7QJfkj7OdemQSXzOZnCiFCq8ubVxRpfNdCpfD3GpRLJMA729AcY1dzoT5cBpsynkk4YSvjMtsnT_35toO-RbYLPiEdm1JF2Aw4prk20OEHPXuxTP8zIZORGT3FjjoFaQLWR2KF7VCgL49jY9mcloHNEEUSz-B7g98wawh9Gql9UgZ6h03gLyeimLnea8hTA5Jgtm0EDPIXcaasYbXobWlIib8Nc8_X9x0fCpdSfHWMTG67Zdc92IvwvFi_tQdii51o_tGcjG3X0-HVYsY-b8_XYtCgChhcgHIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk8xrn6-MBDhsKOckN-MIfAC51_YcI2vhZFcD5rE2DfjivOtnE0IL4-wL6NUnPZjcoNMCPJTCTkGrqgxf4_n3_-zkKqALm4dWGGe12OIo8LlK-xK2R-0Hzl3NDiJ7NW3GAId8fHHw3WeZXSSZ5QiOnP7lwKK56JwZnUiFbYkkrAu2I8_UBuS2EHrscInQH5etc1jipQ2JYdM8gTNSo1oJBcHR5SlCKaTieoBjB34IW5AFJh2mFvGfqUvKylEdlmUfaDAbpZCkPxLR95mceSAyxj82LkQb96Mfo3Yz-VA0PpR9OBuIOVfaMH-5m5OHp2SSiTm4sXCgUFFM29oLy5AMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of0w4jiwZDvN51R28yWWCreruT3iAz1pu8aJgjDWYmmW__YLZlXD5BJJztw4-G4HPeY7bJG_FG1Ix0m5COBkny70mqwhrhwjFDk-dXckOgtGQAcE8M3MyUdBd4YeKGgW57z7PwEL07_cd9QjAqIIQsL3WurqqVaTCqOazL69sHUyL04-dQG02vcseG5tyMg1s-GcKsXBe5HFhKxiRdByOisZg-Ig-J10ikinIvnY30ztxeA6crwA5LgflxBgqqGGAEJJP4s1VkIHXk5IVuDBDlJe9Cw9-lOEzqJwGfp5pTVnRB3f6zGcreyua2bWlDkXX4Kf8h6r7Ky9nogOf0As-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFncszu812wgJcRCKou7JxZazmznnAWQK5Vm3AyIJJplWJOrNFQJwoQseAc-cHCUxUk1TNQENjK0FdL47ey93CzDqrHdkOobkkmL0OIUYVks9M02R2Ap8fFezByJjU3OQK-sU4RWBwnx2bW8kaDqMm11H8aMLbC2Nf1-xOpg03wUX4EVNAD5doAivcu7A2zcP2Z8uPaT-TqSzCkgfbkeowO0JsuZIiOlDG-6c7tfVklaeGOt-dF96kV3iFiGtx_QQxPFJCyPud5XU81sNza_df55b_qKnotq0nPMxZMkWtpqYciu5sLuRCGo7mvj7JGrqzuu4UlMRfXNvjtM0JWZyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=QSQCz7I-qrkBcJdU2jGhwBhKsnnBQrdm98UC_Z6LjWhMTA8nstYQ9cK5fVFS0zk3VH-FuU3nsqHJUEqFvJ6NeYmCxlESRaCk9WaIcXEvGVEOtd0fhz9wbTruGHcQBVGjpIEA21VYuYD57d55x7NZRwyLazBb9BrCknWX8nEYRSkjsVbxVxmYOluj6UIlFCZSGw_48tepbjbR7xyd3ghCxnHNiNykQ6Jio1upeD1smyUUixMZHMtdARntVxmemquZLtt1xLOLRdALOFjAn335YEiKSR4Wwfz8QQ3dY9BCq-D4hgSie8_J5h699cKP_XoVAnMs-pHqRAyb8Snijpb-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=QSQCz7I-qrkBcJdU2jGhwBhKsnnBQrdm98UC_Z6LjWhMTA8nstYQ9cK5fVFS0zk3VH-FuU3nsqHJUEqFvJ6NeYmCxlESRaCk9WaIcXEvGVEOtd0fhz9wbTruGHcQBVGjpIEA21VYuYD57d55x7NZRwyLazBb9BrCknWX8nEYRSkjsVbxVxmYOluj6UIlFCZSGw_48tepbjbR7xyd3ghCxnHNiNykQ6Jio1upeD1smyUUixMZHMtdARntVxmemquZLtt1xLOLRdALOFjAn335YEiKSR4Wwfz8QQ3dY9BCq-D4hgSie8_J5h699cKP_XoVAnMs-pHqRAyb8Snijpb-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5a8qTSOWMB5obxCC-PDK6ZN13cXTzedEQnUPEJaL5nBvZScznXasHoxxXiGYyeflYuDMJ4ogUen-kW7xgpozqBUxtNfBHHC_IVjFLLORPygOB6O0lgDr5MVRP1VWb4uo_lhC4E0Kyv0RXv27iFM1HsB7_LeT7u1OEddtvtNcKbHKTsUr9RWJzzYir6YCqEuOWWbySKbRpF84mnJlRwSi7ViEQvd20AUWD8R7u7tVBgTM_TyRJxzkL26v2KjS6RirRCe7vVmk5kN9D8rOtxZwsUnxw_AQbiqqErLCD4OXX6fU0nL9xB-ubnrFPkzIwNKxM7QYDCwE66Od-Vr-ZNcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loT1iFczLcIw39Zodrn-GknErt_pVghiDywAecpImi3tH_lsR0e-QGbJiYKiBRtG57sk6M3eH9xTvLgnCVOYOyCtIf219onFPGhzlEd_-yf3SqxOge3AQg1O_cEmaAHsYa3V6bSa_K9qFZk9a1zQVXig_gWq3RlDx-JLf4tKindl7o4iG8dX0ctM5tqpBHcNHyI31uej0XWbkpTuN89IsuAMtkLYbLkYKOrQSHJTQ5v5zgy4QXZ08-CDGd8Z2L-2ZgUPFhUMgzG0L6E2UvTvncTGfLbJmKU0N_wQiM_ugqrdgt8V2JrLVQMUp1jqz5gNjY-rjSYrn9bV_fZWoTrHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXs7pTJ2UsnFMCcNYNCAmc8OinnmbSB-Wj5WZ_SlWICF_tT5kKNugFqw9vld-u_tZ4PWgkp3zOmaPs7Z8OJHYJ_rZLuwEubg0I2WopT0wW8hmw2zwuRpeMPlpneexsaYDSlBgIzZCtIWJH6bmzeBZRkb54vWN_hDZlOEKK7_C6ib2FE5an4i1CaKJOovQ9CKsPj7KWEGuNgXtJCTc4LiHa6i7xfIK01xxQLzTUIXN9FdhmRt3Vtp6Qdo4zcE6oIKLuNNJ5r0GDYmr15Vm7lieSSRTINhHzQqdtdLGGF-En8BNsWnh_ctliN1KCnhtPDTjkGl1pnV17NxD9Qxyhh3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tenJbhokxBg43QZ3m1E2AUIXf44qeOa2O1-JOMCn65RGNzPEpZ-9SKH7cwR4hcsPqldtj8QK8f3qEUCyBTi-c2U8tSn83zzibPNLRp3h0vpV3HL08BArd1cNeNp3BacZNgIPsG3AGzarpFYKXZz8hyPXs0zsgj9HJCtA12ion79ianaavAKTP-2Ryfs3oFWoE9lB4Py2AE28HsBclf0MA9e-SeTuhJKZFWyRS5bWQVSXB5linnVMp4LCl4-3ydyW8J0Acap9pEtaCjE_ThWf8FC1trIBJY8vzoKEJnNPRb-jeXXmV2JN7RAYSQHA4TlHww65wV7vfPIe9LIaXXtIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5x-7nEOngGfS4sBr_T9S0MQRTnuT_tndPHQXgmC4AUsaVzyxGMxFCvg2hn-Re-dLf8JXZ0f08nwNmDxGu4hWimeM9UpAQa9zy_cfAnBLGuVSu4h273atBZ0MHN3Sr4NlGmeT83ghz9HnkiCz-sFIhCa6w23y3ChJ1tkQruW8hC92rK8ZFOYwD2gXmsAj_62ocAU4S-GI0Rx7qlrpm25gI2VFvAPo74oVzd1Tugf4LVuRaWOAhDuvB6lKD22gGb31iHqLnJdGRBUsTuOSiD92av1CXL1mpxwcdvb2YaQpYMBpYLdqa0taaYEluzCKtd48NF63iZQsi2LBorthmpeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h957D0NSVXdoppgrAl2-mYNIOOVgL8dv4ZKTXEtxpugGu5kSFHN6AkTIB_9FLh1ID4Zv2Ufl9Fh5P5eZX3Y88leQNMcijtFB7SDn2iD_d2ZayckBg7z0HcvdOe03GQdZAChHozK8Xaptozwre7kJ8xQ9Z_qMkeLuwSmvyMDov0y2pwOguTqcx-DCD_Xt6AYrtG4WZIrcRNupQR-gdhfQayr5OWNqzVwaaulbb07NfY57drXsc-HORvkubNskt3t4BvFti-3Ckl_o5PlfPDw5FDCnd2PShRqMM8iTo6Cqry5hvmefj7L8EZuRhMnH_tA_37zQ_X0VZdDrZkk7EoTXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLgzQd_SCBmtFMAUN80uzqLKNzvAtyiS0UyKsZqSGRxy6lBaLY73NJB4VvHVJvqUIutPX7rkBcOi6GTWXXOq7nHzdUBN5UoBvpNU58HSgA_rfDuUEj8hG3qkGqBpD0Wnl1Q2xtXWmaDtP4Tj3AucC0PJLjMsJFzyZlob617VcZ2OPeDxp4q1P_Vu_v15ZO5UWCFz-R99T-nxPchdLaAeOS2h8voyGLdoZMkRjJ4pVx24otlNCqORTSsIN-190q67JnSqd7fy_mn8xyGMsZh0Fiw-ryVn90-oHPJ7ub2tNwIZ152AMoYggQOUYirfaqNYE29x6iigpkl_aiEW_XT1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDvlC09IRIRf4yc0EK90wg3Ox9Ja-v826K6obYDeLC1gg0qt7RluppH7KncHy8PbhjPbDd3TgZiWyFuJgSaYK3uj_xFamGDw_x-yTmBgRSEc4COfqlNVlUIax5Qq1hyRhpdKMKHDdi7oKFy-2mi6zkRVlz9uvTbumkVP5ORF2Byh9V7AN5yiFUhGN-dKNdIIYox92OvUEjaZivORUg6GejrwtaKqPzqJFIQkncBNjn2iwDTlOOqdWfHW4NWjftTV8-zUYvkAjMjqO7QkqaJovX4PsdavNOKiR4jHVshtutcXPfb1ziopGGskXRLZrd21U2uzn60XUkc2oTAvsz5X_YU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDvlC09IRIRf4yc0EK90wg3Ox9Ja-v826K6obYDeLC1gg0qt7RluppH7KncHy8PbhjPbDd3TgZiWyFuJgSaYK3uj_xFamGDw_x-yTmBgRSEc4COfqlNVlUIax5Qq1hyRhpdKMKHDdi7oKFy-2mi6zkRVlz9uvTbumkVP5ORF2Byh9V7AN5yiFUhGN-dKNdIIYox92OvUEjaZivORUg6GejrwtaKqPzqJFIQkncBNjn2iwDTlOOqdWfHW4NWjftTV8-zUYvkAjMjqO7QkqaJovX4PsdavNOKiR4jHVshtutcXPfb1ziopGGskXRLZrd21U2uzn60XUkc2oTAvsz5X_YU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3OzyueZFvLGeIZjCDWCGRfizkVYRF0CW6nABNZcTNALdmAqTd-a4eh3RngQ_26Gv3m9Eh1lTKKlN2b5bQ2fm2O1zmW9CPMzCuzatCktR0RM3EA6FuqYJvbrqcy6NoZLJ1feL-NmYhmePApC9lcWC_fPN4w4Aa-pubBJLQmoVImHqFdONZQqkEU7sY_w9LjWAu1wh45LtJW-6q_taD1mc4KM8u8ZiKHnUSqvJ-Hr9PHWWbaSrY6KsHsojZjCEwgRBgjKsOR2D84-PgHCrY9q0ttwMvCUYFCAYIIr6_DYaqcLsHYEVbjbYF7KVnV5XVPxp8Y3UsT9mEQwikY_GYm1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js3oUjGlAmSK-v8MDapwVk7E5UjMaF4__VxtAw2M7pUqbokwx_4NqSVxraOt1Sjme6u3In8vrM4wDdk5FaMs10BfoiiHnHUKVnhfPgoW-OS8YDGw6hF9ROsKJKab61RpXXNlnDtoFH-pBNqP25mB3BnsMRROkAmUNOhjwONte62_j3xvqFdwF0jByHy04YyobL8lt7Bz3HHQQbMnlLatWvL4hrcttfGA_kZtGHSVEtcAlrH5mFoz-p7yunRJ8JAFVQ01MZ2A9POVY_w8thwQn6Ah8VTHCoYNs5DJmNEWFKb7GgUL5lnO4u891QkINdlSVGFz_8xhJfZfMIFp9Tm9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QETGw5XIHQLWoCQtaGER7eMuNCFR7Yh557gxcuaTlUB8ssVOv51zf4UPS4cyZNjmVrbmhZNQ5zO1lkR9kPp8uS6R-b0xS53OK5VQhGTI1vg7BH6NgcZj26gB1AnRjia26ujuScqwruxZiSnVS_yUZkD4q_WettV-K7fAo9FcwHhFgfKvL1CP1x9cN4CeyVKEaoeErUmVtl2EnJ3MzL6Pad9nB3VRvAzLcEx9M8gzB0jv7S2VN7nBm3Y7xiSFlGWnnRpJMYx7KUxUA8AgDv8VYIfSdnqOBkCiU2MKeRqquGOt0XuSzKeEQp0AUptWWxumf5ZKemvMglt2OAIidKpcVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqVaFzkj7vNy-uv7NdBD9UQqsoV_z37s5lsAJn2T5IqBHzi58xXrNu6VtILKjaS70cLclBW5okKbaEJomfghkYhWVdoRtEZsQryGVuOnXddxJJuE7yJtSafkl6uqAY9rsYGyUlUuWIRSL_t-TAS-97-kzGtqhcV889ugX_k0Okjm9Q1BRavoX4pX-2KgOBTyLDNWCVsB_oOKAELNo59Vw1aHnvq7a6jBRy2jTlpcETKowhanVqZAYHNqKsDEGqsAGVFsVJdCZvYb0ZAcTNN8MJjlSnhMeP-4kFQE43P-lHCUx32r9WwNURep8N8FoA9lejHQ6srxst4ltQjKB2Fs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyBPaVgUaL8XmiVAe2BWRpY-EP3yH9cKux4coP6P9F6bpiUlpHwq6RpPgQW0WVm7M0svaz-lqHHpZLdDW4OmY2bnStC-eSuBLBjTTdMVeiPczyIZ8YhOlTRqff2d-AZoTfX8uK1-ASC41kNbLdxk5cP4BBkH2Pcoxw0t5gHAEsETi-7apmx9ugPnjKQHQ4jrHs_tMstZF5v2HMRQwFy-0hs7gpvngs-9HJ6pS0kj6Uh8KdQKIGSUDczV9sg1P9ZJhcyNR1W8MS7M_V5qoOmo8o5jaTzcvjRlPdtaBdnRWeA2C6xYl4y0nAmZuN_lI0-OmGQzjtD5jQ4nUC9cZ8_sxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAGbhl-Dox89uECpgJJR7T5f2tm1btiMdnhdtJDMHGfrUymOuVyf6couYVdf7IyNcTt-Fp_r9ER4y2oWVc-LmFNS1cF9sHiuDgAqq4BBj7WieomfNb5fjL3cnvtv0FIkIeJ3B2qtPuxL9g82WeXtkQin8N-VhCrnyrUqHr0iP0y1lgyvTJw1-KAEt2v3MyY1Y3a8-9P0Qhf2MBZJiT-1qmqEgSnXg9xOA33cea4_HaZbXbm9B-l8aFRfECW0NU-ki8kP0b5pIYdtek9GC7M5yqSbPgKARtIhIYhzedLwc-31GT0UovGRggJxHrnKrJyv2jFCm4fXjdDGWODV0vJzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNY0cmdnANwP7obbhlDlUkLe0TnZZk4nptXggsOz5GkbdVOxj8iQ-Bv2RkuzQMQLCozGl8E8EyxwmxfaHDUvDSptWgmZEaBw-lLUqhGO43lfmr8x6PHXw7mpk7Hg_Z4hnYs2-JXlhcuSNtYsBw-Iscci8uuHR9V03TUTo6aU27UP41JtH5ffAkjHqpZYSyrE8IWhVwbsvHLEOfh71EnPj-6CpneL58Qk7fxWbie2hIw9KTRGnUnRCRK1BZ5r96gJdvd0m92r4lDkuzB7JZKpHuhO-imROk3pConSoyX9M7lw3OdeAJvKLn3Qe9ldIBrIYfGYkv3cv-wBc83SVcM2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpojcnSliBklUQ8N2UI3zr_XBVMK-bmbwxnie4zQU4DPR2SIFRlVY0oi7mAWUA6l6qmAlCIgqgWLTYCltsiIPyYzhoE_h-FdCXfmglayHSk2tpG_un1v6jMWFLNRwdO5xhFbH4W9Huqn_0EYyg3qt62qQ8dkTaWPF3cunhw3Euj-onnD4MAfj5b-6ZXtRqp6x7WsvdkAnftOAzLZfmzsRfL51DeP1rB_39BS7cVd7PF9OnAP6tOMSza0Em5tv_dq6496yA4Rvi0Agd7w4lnqn8bBmYStpJSFH3fCrt0pc1ajUHikMtY0dGE06oSYRJY1CQePZaWjWBDkH3l_Nq2J3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=DhqwtV-SloCMANoyd-Wv54C7aPBI1AIeG-_Kd7IG4_b0Q6XJJ5QizLPcYwqtsi18SnZEmgnZ9plY5gPFNTQfHZImqq5IFuEaaJsBuyBaXINuDKDrP3fOzsJ3rgN6h-mb9qRdUNW7q7yyUa6EincLalJbkzbhwIMI9ADwjh9oIN5QPSuuVNTnr4F0vw7_Oza5l5M19MNOL2haJXKom8OHSh5iMqf5mwMUn1Bxcto8hWj_27k5Z5343idlhlnWjgvfXMYlC3RKIYhuGL1505k4ZHhv6-J2_HUvEO-_4x7B-o0SpReq-mSF58W6tXZsHBqGcajmSe58XJgLW3wcUNhS7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=DhqwtV-SloCMANoyd-Wv54C7aPBI1AIeG-_Kd7IG4_b0Q6XJJ5QizLPcYwqtsi18SnZEmgnZ9plY5gPFNTQfHZImqq5IFuEaaJsBuyBaXINuDKDrP3fOzsJ3rgN6h-mb9qRdUNW7q7yyUa6EincLalJbkzbhwIMI9ADwjh9oIN5QPSuuVNTnr4F0vw7_Oza5l5M19MNOL2haJXKom8OHSh5iMqf5mwMUn1Bxcto8hWj_27k5Z5343idlhlnWjgvfXMYlC3RKIYhuGL1505k4ZHhv6-J2_HUvEO-_4x7B-o0SpReq-mSF58W6tXZsHBqGcajmSe58XJgLW3wcUNhS7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjjGYyI9oxY1-rujm0OHl6frKsNozayI7hkkLD87_l3K0OqR-9n17h75sDx4AZWTnVjLoU-c-xCsjfY3Yv5dWaHsmwyGN739q1Ly_vlF5jYP-eeLgvX0H4Z75k_laBjvMUxO4hpWO43QDsPi3uyj9ca6n0H4WB9LgtCV3Lz_R72x44AJJ7acdkOLNkSQ3xuctv9kc39PGz_NGOblz36s0yI5_IoLweDWDKwKl3Rr2Uv1g639ud9gfPwOn4zQf_KxrYWXQhCwzGaxgoqMds_ETER-NFZ9PQxzeHEygyvoA0xLpCmBBb8gR3lVwysfjX5TdxxRW70R65B_yXd_gwW_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=KolC83l0c2zOf4I1_SqEEcR7nx4B72NVDTY-FaijY91mBRPnkHmuNPCtLHn5qwSA1YO9IxdXs3UsE8tMV-w44uubFEXD-F70ruEWimU2AW6hSOzMXxwWQw6eVYP6jZhP-XCZQFeNq4O-cMS_sclLNJQ1HfMqrJWrsFildvxKKxespnGAdNNesWLPFvIX42alZCybZvcADom6XWlT-aZTi9CZv6mxD8s-WASmOwdOBCDfncRctCaCFbM9tEC9ZBrfExDPdRqu30xjq3sqj7aDCwmOONWlamFA2JNdpmzQHjP_PFfnuNnxe_GwDw9VhyrD_xGd2VDLnPuVga-6IIkuN5l8HMc0260uY0g7f9QL15T5kKN8bwnPTFXD8xNRhaIh0Ptmvwgqi4SJW2WH3xLjEzYj-VG5Mq12AW2uhX-_KCprycr0dcWFvtwhAClIqkrBwOcC-8JGv0mhmb4Loz7EEg0nj2NYxUXrVLmEaOVLHi_O5IlkRYSyK2aA5ro_MZ7Fx5fraD1EZAz5GbWeBRf9gSagBk8m3sur-IcqWG8dLMvGtplawpiaTOo6e6g2-L_Q5znnLvwGuZJQFxhxLHCuEGPaFUgMnpJi9lRH-3MBOt-INqZ8CwE-QtdWlt2vWdpYk2xg1p56bUSXQPIlCBcn5cr1KJ_cc4r-YUnOAH4CyeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=KolC83l0c2zOf4I1_SqEEcR7nx4B72NVDTY-FaijY91mBRPnkHmuNPCtLHn5qwSA1YO9IxdXs3UsE8tMV-w44uubFEXD-F70ruEWimU2AW6hSOzMXxwWQw6eVYP6jZhP-XCZQFeNq4O-cMS_sclLNJQ1HfMqrJWrsFildvxKKxespnGAdNNesWLPFvIX42alZCybZvcADom6XWlT-aZTi9CZv6mxD8s-WASmOwdOBCDfncRctCaCFbM9tEC9ZBrfExDPdRqu30xjq3sqj7aDCwmOONWlamFA2JNdpmzQHjP_PFfnuNnxe_GwDw9VhyrD_xGd2VDLnPuVga-6IIkuN5l8HMc0260uY0g7f9QL15T5kKN8bwnPTFXD8xNRhaIh0Ptmvwgqi4SJW2WH3xLjEzYj-VG5Mq12AW2uhX-_KCprycr0dcWFvtwhAClIqkrBwOcC-8JGv0mhmb4Loz7EEg0nj2NYxUXrVLmEaOVLHi_O5IlkRYSyK2aA5ro_MZ7Fx5fraD1EZAz5GbWeBRf9gSagBk8m3sur-IcqWG8dLMvGtplawpiaTOo6e6g2-L_Q5znnLvwGuZJQFxhxLHCuEGPaFUgMnpJi9lRH-3MBOt-INqZ8CwE-QtdWlt2vWdpYk2xg1p56bUSXQPIlCBcn5cr1KJ_cc4r-YUnOAH4CyeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2GKlrZuy-D4PwNZzxn1Y_aqQpwnRqhlw7JmyIzE8NHtg7KFAtl7JyFEZQ8bg8lK9az-qtsdhK4CzFB5sb99TicvbRBiqhkpWi8ZxIazRZTNUfGuGCpoyOvlpDLO5DrttNl-IKbepU0mWL5xtYscOUi-GVbOixDvRV4v20ziP-f32wRw9takq0FSApjZjg3KHEyxyfKyllyFGg5_t96z7CxYOc8RQoAK1GmH_afFb-aXUC9SGdSblnRaN5nN_4WIdEEE-mCUMTHimg-G9z1mPVtIvbgpLFVzY-pBtsTYqMjqztY0uNMf7y3X9O2QheyU_CVJPKX2_mcQsZM10FRKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kp9gc2LkFH-ViRBA5iZOxRdsBAEar9ZQeW98qIu66uP08QQJ5LsJLPPmkLoXOcS_5S29IXz6r06S81m6BFZ45pFMNDhxbA9Tq56-IgguRj_4d_RUo6mfLD4N5yxNP7cEC1XqZk68oOrwu9vJMn4bEPDdg2GpaGqdS0d_paFtTskasPiUFh_JEjMh6BaW6qrQFYbaHeg1pKOpzovByASiUx6Uvf-Bt22nCbzU2jU5ZIk_G_ZJHEvw54PIen8NaXrd5qf147aEiBtQIaFZ6U4-1ASM3WG7LZ5tLltV2SwnQIqOltuGBKwyFErXPH9cGRhE76OZDdLh-ANyMp8Z7sltng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOIFGKcvD8NxXAmiNu2BB6W8B1vsf3dEdrtWMk2a4-_0B2Zmw0JAEs9DKffPKECugEYG_xr1tkkVsNJpi-fN6rpr8NB68zwLniQJGenxTHrYDiZYMvFjd1E0jA2Nt_vz0TCVDpkYe4ZB7689alkAzfgS539yDTq5fcZ93cYQR08-3nSwzuyNT3BSssevZ8EZQWv79O4ddBKx9B4MylD9Dhtj_ZY58i12pe8-5eAZuziU51c7nWqzICbKblS15Prc1ddQ9NklMjmFG2iGcpxZk-uZ0SAXfklwmVZz7B0jWVoewuZnY2_UgQpZdqa78Wpkze4nR-BwxLOJmlIZ09slVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=TlmXPkFZHRqWEfwX96NGvfWZNXme9PxR2rrHY8soDczm72dgqiTfuUp80fAFrvO3Fk8-AwEbUcj0n_1P_-eBhR6AYlWN5fPX9z6fVqVbbSH2Mzt9o-yhr2l0WKmIiM0hOA289ihixjTcrClW0_IWLAZAPKzbN0Dp9Acfg0WjqkcfNA35y8QJZc4s5vZduo8jZU_PKbizCqyar3NhHmIUCCwez8M-SvbXntG3CFgcNwz0azxpsUREcUKv-WDqd4AJFE-iNdkjjDfrhg5aH-MX2GwhN86UX4ivH1LeOkA0gku2_EBWUat_4jOv9DrMrrxr7qI80Hn8IZhk0nsT2sLBoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=TlmXPkFZHRqWEfwX96NGvfWZNXme9PxR2rrHY8soDczm72dgqiTfuUp80fAFrvO3Fk8-AwEbUcj0n_1P_-eBhR6AYlWN5fPX9z6fVqVbbSH2Mzt9o-yhr2l0WKmIiM0hOA289ihixjTcrClW0_IWLAZAPKzbN0Dp9Acfg0WjqkcfNA35y8QJZc4s5vZduo8jZU_PKbizCqyar3NhHmIUCCwez8M-SvbXntG3CFgcNwz0azxpsUREcUKv-WDqd4AJFE-iNdkjjDfrhg5aH-MX2GwhN86UX4ivH1LeOkA0gku2_EBWUat_4jOv9DrMrrxr7qI80Hn8IZhk0nsT2sLBoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOZNqlF7Z5bEnL_8qp2pM5wwZNNLEO71YegHe_LBoIzsYsAO0xy5RLtRD3wXm0waigU5HzhMxYG3Ut8jyJ5kJUG5cWLg75lB1Z14O0OiRSDQOvAcSGnvHvq0TQrGLvUQbotRhpNVR3K-jMOAsj92chIeNbKHnx1N8iiVZOtGx-1KsBn2S49_f2w0i1gzFeWieOdQv4M-eNywdfFFioIEdi8t7pxpMuayeqRt0RIomRI40V9X6ByNTSKUOc-OmnkzTvhZMm5HRdYApJBPfp9YHW8yI9j7BD7Y6yGvevVYyUe6sUpLnFJrsV8HO4mhJqB-R8HcOBAiRF_4HmGjsR-ACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=dLj6iKy7XlOtAPy3kkBxs5fP9_xd6McmMerEwHeY2a-QcFjNlO_cuRIFa717hktRcofYW4v1qoqQ-caN9JfheEPm6oGKrzTICN_cBvHpvDklIVyTb1LD18jPzZVcgOVfW6JnbTgNx1NBghhGcjHJcyy2cWMLN4BwS5fRl-i63efEUyWzzilm61AjkT6_aQ1ElTOz112fEtSu2PSzFpSp5vi4yz1XLxXuTnZHhSj_-WdnqamKykTawUH-GSPL-oeeWHbwmOqNpu13vRKQHf5XI1JwJFyQ2h7bRuWbDh7CUATtfMCw_42u_Cl9_tquADQjVwGGZhL-vgZeKuZoBZSk7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=dLj6iKy7XlOtAPy3kkBxs5fP9_xd6McmMerEwHeY2a-QcFjNlO_cuRIFa717hktRcofYW4v1qoqQ-caN9JfheEPm6oGKrzTICN_cBvHpvDklIVyTb1LD18jPzZVcgOVfW6JnbTgNx1NBghhGcjHJcyy2cWMLN4BwS5fRl-i63efEUyWzzilm61AjkT6_aQ1ElTOz112fEtSu2PSzFpSp5vi4yz1XLxXuTnZHhSj_-WdnqamKykTawUH-GSPL-oeeWHbwmOqNpu13vRKQHf5XI1JwJFyQ2h7bRuWbDh7CUATtfMCw_42u_Cl9_tquADQjVwGGZhL-vgZeKuZoBZSk7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZTOyoUsRj8atKMCfE-r79TPvygUx7T8kbCPr4--bt8ywsiftQKfGD5e679FMEzw7dxqFg_SoogqAdF2kq6WfVKO6ceQg6i7r7s7KVVVW_BTW-w3kaSnL0IFcANu7InLsuX9W9RK1RRAoVVyI0A6nlw1b0GmjeBkh61AnhawDLdw2KH4QsPrY0jD9E765yWXIoKF7jlUlWH9jnLkaEpRHuaQmZgDYPfHhrKSS0sJdsE3TkdHeCgO5LFtHSB1zq40sl29IPjxtaelBcA70tBsfrDAxiFify__75i_pEDfDqPoiqddZoKLapjEV7jtVqZtAeqJ5v9dLK-36q99xOZheQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=X8rQwVfAotOxGX4u_aSHyAxSmNDu7ZGTOUAnkaoEOvnsRCvEhNxgviT_7Dm7URHCAhKJSzd9npruiLXDYwFre_ARSjadlVQjenUQHbTg5_87Jx7EF8C2ToYuv7ECjEdkfRZEtMaqbSilPBrDllh_P8NQ6Sh6u3UvUkiT3owshryX5TI0wir34Ubjti3ou9Co3oa6WSgmyGqwi35jAOhINOZn-_pebsj6n2wj_yscdKsk7kRoF5HrPpKk6qmfOYv_jKVigp32YJvrRBzyLfoxh5uoGQBT1hHKahijw3rFOBxjs8tBLYrydoX52k_GuL45Nsf7BM2FsWJwdlFEARdK-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=X8rQwVfAotOxGX4u_aSHyAxSmNDu7ZGTOUAnkaoEOvnsRCvEhNxgviT_7Dm7URHCAhKJSzd9npruiLXDYwFre_ARSjadlVQjenUQHbTg5_87Jx7EF8C2ToYuv7ECjEdkfRZEtMaqbSilPBrDllh_P8NQ6Sh6u3UvUkiT3owshryX5TI0wir34Ubjti3ou9Co3oa6WSgmyGqwi35jAOhINOZn-_pebsj6n2wj_yscdKsk7kRoF5HrPpKk6qmfOYv_jKVigp32YJvrRBzyLfoxh5uoGQBT1hHKahijw3rFOBxjs8tBLYrydoX52k_GuL45Nsf7BM2FsWJwdlFEARdK-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=tYsn1uRfcRHp4CPoP2SygOvET-gTLZmYSWy7lW7d2NpHqNKPdebTm-X7VDgMJfd18gjdAytNrf-bn934CJs5YqYQXrTfZIF-6_kJmi7g-Fsr1BOODKUN4BwcI6VjX7jvQ3ngm7xeTyeQOeYhd8aY9hionFT6ChykQif8r3Q3u_FMIVAWHe73OVI3La7N4G3TboJgElaY8_vYze4Q9oZkZknNvGT4v0okFs0PJQYSOWGD3SKb-fTQxnkXKE7N1sVFxSh3J2BiR93hwfz9_h2b42EzdrAyo5ufGLw474GpXxiZPI0qj9AdUIs2i3mqHoq-a8TCBOwAWVTWgl7nUGRyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=tYsn1uRfcRHp4CPoP2SygOvET-gTLZmYSWy7lW7d2NpHqNKPdebTm-X7VDgMJfd18gjdAytNrf-bn934CJs5YqYQXrTfZIF-6_kJmi7g-Fsr1BOODKUN4BwcI6VjX7jvQ3ngm7xeTyeQOeYhd8aY9hionFT6ChykQif8r3Q3u_FMIVAWHe73OVI3La7N4G3TboJgElaY8_vYze4Q9oZkZknNvGT4v0okFs0PJQYSOWGD3SKb-fTQxnkXKE7N1sVFxSh3J2BiR93hwfz9_h2b42EzdrAyo5ufGLw474GpXxiZPI0qj9AdUIs2i3mqHoq-a8TCBOwAWVTWgl7nUGRyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8MDSIUXLK4y6NXyFlIvVMkWjBmOsSoDX5aIou4Y6kqbwvRXRz-1nGuBE4NMlJrV0wMv8O1cpl0IF4S9GfDn6PW7knLD-5mpl7xtHvjuT3rT1bo_qp-1pqnSLGxmK0MB9aUyz1FJ2oxi-hhY9mIZXWAN1lXJG8ge1Drt6aD05sdFRmL92JQ_XQHXNBJvMbVJlHgtKAocYuY66Z8O5OPcZQsRCZCJy5TuijEBRSawLZ01vWD0tr5_4e5-GI9OIPbosKC6LHc-SJ19oGaxjV0sRYf_TNcsYkHlfji6mLZY8gtXRyrsofCH-VMHfF78zSfZonFSQ-iA_NilBT8ZP8MNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
