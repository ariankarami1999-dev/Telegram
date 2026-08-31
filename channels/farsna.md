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
<img src="https://cdn4.telesco.pe/file/DSDJzEdDq7NjvIDWDNOAuDsPTeZKzsa57xijsaO6jKbsnylZXUjhp0VrgEHlz3I515TRpb-qDBNb6-wfPrXOIpM1GE-vixDvuLDAqgLb-hXk0dwPX_vORQ2NY_1w7IJsbPzF7PiBJvdf5qeJ5Hl-wfIP1IyTZTJpELFi2JyZQ3yCcJZXfW5KjycseiySCUPr8Y-ze_Ar-UCk42_kh8ClffAYplhDJmZysUH7rOj13Gz5UAKomzwcjahH-Zf1zJEFBalkKYcwJ5nXARyR3mYQc2STdV99tm1xnmyAimEbtgNhEZainSRJM-iqEyyketx3uHUhgJ8q1xBot3xi4LENeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 06:01:38</div>
<hr>

<div class="tg-post" id="msg-459128">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6249a95134.mp4?token=j6OPQSul3B5ROv4bgIdNzJaT9C08sexRcQIW4gRd8FXhmhMukXt3HCLS51Q140ddyF5T8-hPHk9afue6tXwC9U9t-MAeRQ3w1SE7ydD0oBtAiKUP8O8fd70UeT-Ntv1x8Z-PNUC5sd8X9yOI--xVPUkH_ZWgoxSMrxUrG7QxjdN6QKWhq5ceynJvLoMAjgJvA25LDvTYw6IiplOZcqOtTa8a-BfHEdDDHVPuUzClCumNd7BUmOoax_RbknZNkDJCFLgNm94bv1Yaxd-bOOkSDgaOSicXn81HT09J-9ogBrrKtUD9LAPWQwJk1DrFLIXzNp6e9a3sWt5EfLNFApaZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6249a95134.mp4?token=j6OPQSul3B5ROv4bgIdNzJaT9C08sexRcQIW4gRd8FXhmhMukXt3HCLS51Q140ddyF5T8-hPHk9afue6tXwC9U9t-MAeRQ3w1SE7ydD0oBtAiKUP8O8fd70UeT-Ntv1x8Z-PNUC5sd8X9yOI--xVPUkH_ZWgoxSMrxUrG7QxjdN6QKWhq5ceynJvLoMAjgJvA25LDvTYw6IiplOZcqOtTa8a-BfHEdDDHVPuUzClCumNd7BUmOoax_RbknZNkDJCFLgNm94bv1Yaxd-bOOkSDgaOSicXn81HT09J-9ogBrrKtUD9LAPWQwJk1DrFLIXzNp6e9a3sWt5EfLNFApaZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عراقی از وقوع انفجار و برخاستن ستون‌های دود از پالایشگاه الدوره در جنوب بغداد، پایتخت عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 112 · <a href="https://t.me/farsna/459128" target="_blank">📅 06:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459127">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پزشکیان برای شرکت در اجلاس شانگهای فردا به قرقیزستان می‌رود
🔹
روابط عمومی دفتر رئیس‌جمهور از سفر رئیس‌جمهور به بیشکک پایتخت قرقیزستان برای حضور در اجلاس سازمان همکاری شانگهای خبر داد.
🔸
بیست و ششمین اجلاس سران کشورهای سازمان همکاری شانگهای نهم و دهم شهریور…</div>
<div class="tg-footer">👁️ 489 · <a href="https://t.me/farsna/459127" target="_blank">📅 06:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459126">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در جزیرۀ لارک
🔹
مردم محلی از شنیده‌شدن صدای انفجار در حوالی جزیره لارک خبر دادند.
🔹
هنوز محل دقیق و علت وقوع این انفجار مشخص نیست و پیگیری‌های خبرنگار فارس برای مشخص شدن جزئیات انفجار ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/459126" target="_blank">📅 05:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459120">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osyKq5XqFNZhmYOuQSKTvXEM2TV7NA68u-vG5-zff87wQrABWfarplRlZ_sRhfoAH5kfsNS_CSIU_F7TEyfl0XFZHCttAHzSdSEOGuZQPcVErrCrOwDlXRDaxEHKDFjbnEbgYuSpcozXGCvrojhwRYefASZ-9jSMB9ole0oYzDr5nYvm39am5DzBABdSVBcGhokJquk5UpXxRWQLD7qrN7wERIMQsPIqjHntDmrzjvxu4Xs5lkE2JdhtQIUAnq5-STZ-xgtRUIpxZ6chWg3RX96Rago-phwgSVhYkatQDGnBrdqeS-wXhqu1-06osXRFI4V24FrkmrMK7j2VWanA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOUdCvTHUv5EIrBTK5rNnaRvyMcpmuZR-FoGca86qpTjazhBS19P8P5xc-ISCC_2UJc7mNDTar01qyv2EXcETTw-Z5qCE8XYKdCjiK3JI-TLJY9WKP9Q9D0x47XsvKahQpFAAtnbWDr0S1-2hN3pt8UhoYmbtkrl3wqPfoNMJz9moq6_z2yXofBrMJ3akGIUggT1xjv_ma55tTjNwKQbzvgphzYoHgNApPQ-x6pQb5OMXdAIEIFeUJdduieDQjcF2f0mvvwJ8SwsufalwqFvU7WJMHtV6OxKmYk6lCGK28xlcKBRYzvZPxKl_zGFDLHgs57xPiGcUQR_pT0MlWzMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qENwqZtYs-rsHnUvAdp0tFuLKL3x7cFdO1oF85y8PmqdzucykgktVTKgcJdNrqK2S1lZj38jOvkyFchw1RZ5LBPhBx-zjch6-GRkCqngHN2Ydg8P9mILOysObYCkzq8jlXt_J4Vzsj2Zx9LpMXFifyV1ZkOh1DMspT-I7wysFUL2lynHHhPrTiKvaJo1aj1Eu2AJDwfHpPS_5dYj0Ct2E03b-3sh2FFPLiITdrnSzGX5SPobGylidvxwoHCd6H5_ZWuUwFLeb0Rje8tgx7lND3tbsA9THnQvzgAspiILYJ6JKu7m9mscd8NcefeD1XFQmk1Hy48uJbpv_GNdKYxi_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4tOUjnsWWbd3y0wSnRZX7dihHsin_iumAUHvEN-52amtRkOeQBZWlZQNy1ZXbfr4QFVih8poV0rkevWOI0NRaAIUSKfzNZwi1JklA3jB_EscmZA53s2_YWm0xv3k2wh1kJc1OfRxiS7s1AL8W5hG50AQVdOLtk177v69sCbIoIPZ47iYu2JwCIFA3J0qkqbmwa_7iJllxS5DsClu-Mh2XK_4-Q6L5TeXB-XiGhQ1ZScg07XSEELCPVMHT3swdAz_DIHxjwt-yf2_w8Xjdd5KXhgoa6ZRZ-vvKvy7zgXliL9Cl5jOaqlWAxQeDL8EhiGXaXSnApF1d_v6HLm3tI5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mSEDqvegEbEyvz4g_oFCaAaV3AUkCer-UVfTLDTY-E2eMlRDqUjJiderrTIIC8DVVSPNyUa8isZekpjyWMTHg6LZdcGzOgOphYkQPnBNfDk4kSGedg1FqyYOmD17SJydr4J28XttGq5pL3GDxWwEweYRh3QTO8ay8xzEI1MCSn6fLmJPis_892N6nRg_-wxIkw0qsA4lQPk8nYHWU9Gcz6jsK4eHWpnICUBdTuovK4NQ6S8A8zLd_iEHm8irMRC7D4XqJRpOVNRReTO-QXNRkvokpQTAk4h60JvDWyhVIk-ABxYlY8sdYSJmYXU3FPfzdh9RrpUSjqIVWWXD4viiHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BitLAI9pYYWOtjdaI3394LI4WwGuYrZFmAwjahAVXs7jTPYm4KM50JhuG9h2sF5lpLI7HCYVSfDUxltXvoa2_m1t-aDk4XBoGRMKFY1C9yxX30ueu2yx4s4hwrh3gqysSPCM0XiT6JbUPZFUB_CxfFRmwguWX6YaB4awPEukf3952hNrqPhHc_8DyAXjH1jkeegVZZ9I-FSbz92DqFMO4dlqNGUDj5hhU4AVaUzFaCwnYwjm8UHvNiXFrY9lPERkKA5Ta8k-QCbPYKN6WX9JSSHe_vPxdu3_Zm15zSj_okQzf0TwpCNvjP9o8ZJwcnVfvNyyfsiRlvOS-SQqy8XcPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن میلاد پیامبر مهربانی‌ها در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/459120" target="_blank">📅 03:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459119">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7489b53543.mp4?token=XmaUMU6jfZoJVzH5CkJNWOX4cpF8AU8JVsxuTMWGK0nsHQIR6H1AXDyOF6Wmcpj6dcGvrx-LbdV6q6sIrYqN3sSnJUgzyeo_fEbxeN7mPESjeMLMtAiAocEHq4_b2_WHv6tEv15M3HgnqPRsIkwReQcdn924X1xticlfeZHQEyG7M07RsW8Gwv3zIjSGpBooPhLS8ItWqI7rpfUIHDsPM2hDvjAzwIwlzjKj9-xd_rXXW_wXEIk40uQKrdc608N5nMDKIqWCXlq2ZPEvV0wUInkwpk656gr_1gZRzvbZH5N8OA2nQqZiUltOvzOk8GYcMQRpGXgynM-Z1CzRAOM4aUwolmY50IN_K2jjZPlDhJLqG-jR4u2hahuQmylTCaLT2_P7fHx6g-oFP4zmqT630mlX9v203KEhtG4hKggkoolbwIdeEMIsHNVutJf1FyDtro4BHZNSicMkUi5LrTGWKiYyZ9UuERUK925jPYidFxnvxRgGGHXoVJe4hGcmt4YkMJTm9urvaZYW8PPS3GY4IqERUrHH9bq-RM4Roc5J6rCJrwyMuyuXBMzvsxngz8BDsca3Dr1PHD9kZUa0CwLBQg0Vn-CRrtt6RutaoT1ir83F_WtcSXJKLpkHiXjX9PMC7qdseGbaXprfu3g9-grKG6x_IUicAB6n8_kS5zH4rfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7489b53543.mp4?token=XmaUMU6jfZoJVzH5CkJNWOX4cpF8AU8JVsxuTMWGK0nsHQIR6H1AXDyOF6Wmcpj6dcGvrx-LbdV6q6sIrYqN3sSnJUgzyeo_fEbxeN7mPESjeMLMtAiAocEHq4_b2_WHv6tEv15M3HgnqPRsIkwReQcdn924X1xticlfeZHQEyG7M07RsW8Gwv3zIjSGpBooPhLS8ItWqI7rpfUIHDsPM2hDvjAzwIwlzjKj9-xd_rXXW_wXEIk40uQKrdc608N5nMDKIqWCXlq2ZPEvV0wUInkwpk656gr_1gZRzvbZH5N8OA2nQqZiUltOvzOk8GYcMQRpGXgynM-Z1CzRAOM4aUwolmY50IN_K2jjZPlDhJLqG-jR4u2hahuQmylTCaLT2_P7fHx6g-oFP4zmqT630mlX9v203KEhtG4hKggkoolbwIdeEMIsHNVutJf1FyDtro4BHZNSicMkUi5LrTGWKiYyZ9UuERUK925jPYidFxnvxRgGGHXoVJe4hGcmt4YkMJTm9urvaZYW8PPS3GY4IqERUrHH9bq-RM4Roc5J6rCJrwyMuyuXBMzvsxngz8BDsca3Dr1PHD9kZUa0CwLBQg0Vn-CRrtt6RutaoT1ir83F_WtcSXJKLpkHiXjX9PMC7qdseGbaXprfu3g9-grKG6x_IUicAB6n8_kS5zH4rfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر لحظۀ شلیک پهپادها و موشک‌های بالستیک در عملیات تنبیه متجاوز با رمز یا محمدابن عبدالله(ص)
🔹
هدف این عملیات زیرساخت‌های فنی و تعمیراتی و محل استقرار جنگنده های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق در اردن بود.  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/459119" target="_blank">📅 03:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459118">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFzRx0xLHj8L6oINeNf5TseOcmkW81VD909qwB9QJEcto1TSuZHt9NrlueniSSlrH-PycJxu_kGIcjegiYQ8lNuv43Ui3SVrW7Z8Yubd7Vxpl5QzhQfhUfQIQqIbMdXtbSEeuyGgFdDpuoMtY8O9f8iaJfSkYiSvkztsLhsG0cJ4cw7bZkJZ-yBVqZV6GXWxvy-eg8M7h92ynN5VHN40CVK8aVWJIY-iFHd52bjBXQK1Bpk_RdtZ72en5v9hUiS00Ib62ah5OdTJmyHLSHSbIjtUdK5bPinDQMqLGTuqWSGsx4BktmssAixUQXOoZH8w0O_9lZQhfgtbmahMLk0kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردن همچنان تکذیب می‌کند
🔹
اردن همسو با سیاست کتمان و سانسور ارتش آمریکا، ادعا کرد که ۸ موشک ایرانی را در آسمان این کشور ره‌گیری کرده است.
🔹
ارتش اردن همچون اطلاعیه‌های دوره جنگ رمضان ادعا کرد که این موشک‌ها به اهداف خود اصابت نکرده‌اند.
🔸
چنین ادعاهایی در حالی است که اردن بارها حتی حضور نظامیان آمریکایی در خاک خود را نیز تکذیب و همواره هرگونه اصابت موشک‌های ایرانی را رد کرده است.
🔸
مقامات اردن حتی زمانی که واشنگتن به تلفات نظامیان خود در این کشور اعتراف کرد نیز مدعی عدم حضور نظامیان آمریکایی در خاک خود بود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/459118" target="_blank">📅 03:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhJ3ZTwsMPA_-OOBY4MZB7eAJ6qdp7gjJdX5ayBC8PPhBq7QNiF5OYaOjh9krmPDV5ntrX1IccxpTgTVFfIH4N7_dVyeDEIFJmIXP5KCI8Ewf7TuyHYa2Gsgk_5Sy78kq3SEaGmwqJgqHPZEEuflCTj-eETZIsBTTvUjJZTkTNQeR3LiYbEfjjsRgsc8FXRcKrLP9pi3WVoAHkGZAEALRphmBk0eIA6_Z3-lDPjNFNYlRPR5mEtcQ3BC6a43uYOE9AhT5xkqKiNu-bhTAZ4qOczdJBOITytwHqk55BYBy3gle0WT8lbYRL-1THo9lrVa6cvZRmVi0ppwLK0IMvUhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irOPp_W9r3Jy5yCnReFvTLHLSqTw-t7EolMijWZd1mFpER63GJU9JMgc110sft8rxyxY-dyXgLwWjXW-4Wep4da_nEbc7aQ_jqHA2uoVMZJKvz0C_-ZrNP-v0O23mUztpPVeO3QAUyccgAZh8E_-dS1SkHkg7AEI6JRKW7-t743V4E_72M_b0R5Q7wiz2-fjv5BLhC21jbHEHoG3WuxqdTXvMlwhUy2AK9xpJ2l7G-aldjOEY-miPsbLm-QDeoSxbav-L8vNJxqQdJXV3S6PpBYXIuX1Ad6kk7lKwGYZHSqCDijmN35NcoiE5uivj0cQZsWBQutV2RzBnCE-W1HJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzwkD5SQ1LtF4v27_18WFaigW24Y115hQUSQBKmvNDSNJ6wI67ef1GJrJNvllrT8CAy1VneX2V9Y3iyh5Y0JAylYADOnpsj_dI9WSA3YDqQQq44QydwjJrQRm514TLq-vldyVSippew1YiMlmtmOPROe33_H5O3H6AXS4uGc7i2vcYPSZEwjSzSKURc76HsuA2_5TE-YfTtr7QBfgP2-GMLaO6Pr0sNBUfPF1eclJUgNgLK4PGbu__QlBv8zt30RJgBcDS1GrktBkgBbBuplYeMdBUVNBBaZVjzRQl-ZeT8fGJlJFg02DBLrMru7XTp-vl4322huU4349f-D0A1AzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5l7l6CLxS7yHiSWTzNh9AJPsBV7HzQIjZR_16nglSJ2JKDXpgJ3FuqsfAkdhFUXyN61A7cLtiLy1DZ3u5RO93IMway1dhEmg1NN8vSCIWpTUSEb8WNDcF657EIQsoyvbFi20oHhidQ2TAfBGh0iN6oJBWSHP1UD8QsmskQreDVxalm1i30vJgZyK-VKKkjHIwuKIH0BWtxnYpbkmeIY01yGJCa2LVaKhnpemcLU8qdMCahusmW-Gblw-SJkuwktHwQc4r0PJ9JkMdQoQHjMVATf0uhYhv0pWsbkOE_qpPfRa_KSbJxt35Wbk77b_yTqjO5KbsdygkPr8puM4__k0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LE4edHtd7I-3ilYWjT1Jo5-Ug8bexGH2fRrstU0yKY2mzjl-VD3SazsxKQ7zMpPk5Aj3l7nYKxUjzYYfAV3RY-x_V9XWEmAj_7zJN-tHIZ0fKSKCBbZutbwGzII5QKhXtGiavJQWYyYUnE4FINN_UBgDKkywVwvtb-56LNGOwd-G0b5DVjlpOtKvewO3yBGarQQzVtk1Bgo1VIpxqEAF_xCso_eyZIkob25ed0F03vw0JTrGN7XSm2OHp6-tl3qklbl86tflYu3sDlibRmH1eXeyJDTm2Xp-6-muQkCFAQqzoLxSoBZYybAd4O-6iyDYVKMbkU7i_6ru_jZ0D_97FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۹ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/459113" target="_blank">📅 03:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459103">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwPd_pZixpv_k_VJa-1HI78yoFXNZgJgxgnO8sbIOHEeHD11eEvBoDkjgGTeCnS1VBuFYGqIUlwebjwg9Ftxv23dgjI6qgGUvHuz0cNeTzfXwtAjjmRWqYuLTASpCDOlgegzPaB2wyTgJlzV0tHICXbr4TRj1p-Ly7oFRCu-4MZxYOVeFLP4E5mQc6PDstL3Dz_tBlEdkIb_glUezrCaUDHizOV61B69_Da1oXnqw-zRT3FYE_hWQtsEuzuzXS6uleMC_oXDXyv4V0daqaQsu_VLemv4Z3oW8Lh3sVilhvX9XFR4PfnGglXCc8L7GkIlbzSH3_ZG7sdgt0bLQePcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J022L6JzqbiiRGd1Wo6RA-HGaOAezYNSXhMAOvq9eD5t-CibQCn5yrqde7E5sSzQxkA1JY3WGiC-dKc9u4YbTzG7EPTz_f2B9QuRxA1EEtD_8VsF7ZaAdgYqaK06ZEvFefPFIoBr-cNGcltcpvlw1UIdB_-RXtDrZJZYnM-bwnp3Pj-R49Mm8DtuQ2poo8vlOErHwsezVbXaRyjsxmsTSc1l0xi4lqD7FX2-UN-ib9KsPV-N0tngcxJbUzrL51GD1b3ci-I3kkNkuZI55__mzKcFVvBOyhw3d6IQbatWuXktsOH2Igwnq9Umf9b7q_l3GkCfYskH1i-ODU4IKeK1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqdS6KfqCM4G_V7MQWJU6QwrqHRDMXuWusGrYzeHIwhOuUuM0mujt_qfYrGFDfIqpuNmaSTcNUlc-jvmLIgnV9I7lXVaMg4f0BmhHwisMrT53OMyV2mUmvh-cUskcaRsbrVcrJvLFx3sfJlDiuD2ZzF5J4JbgfV-ExfKAx3MtlOdQBnT_8jcj4hY9x0sar0c0s4KB4a7DoJSMfRUsLl9BCYsr4PUcHu-fSby5Yu2YYk87-AcyHGdi8qn-O5QIv2Q-FwhpiuPamy0-Rlut-TlsKvFPFEKXKTU7aIg8dJdqn1v3TJsnZq1GVLVJqln3ZoJFjPfTGiaJqWMckSx3qcQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jFK4lwc2HVqrBpDvHXbW1Toewqe3YjZOvzwuI3jn8OuvZuuccPj5WmJ72ji4EbYQAphqugwjPSx7hlY6rKrTCOxNgGU8WjjtRSKQ26VV32dKrpvQS1bJ4kyfqpQ-FtTnh83n9gqmsNfUMcVcA66YdukCUoHX0aY1A4vc4DKP8XbZ67L2LkLqvZ0SSgozCslTEYGCzhJ1neeU4QuGuQxhg1GTUAnD-wLkrqJnLI97Ez_cACI_L5bzayRni4SdN9jDxx5_dnOi0rB_UNyINGQw1x1ua8h15C1rR1ArjAP7UepU_jABcVR3ZKTIhdMlnL85dh-iDX7RR-IWYfqXy7s8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNnL05S0ePnIUa1AZXiKU7QRf2X8UT91rwvt3h2sodKsxS6XPGHTLKRVb79Eny6Ifu3J7a1hThBLh4rz9h0eTKEPh1bTqQxotSJDgYr335uQOKOlfjYdBbUBQxgRZfB2LBo7YKIDj7u_FZJQzrnrK456srlKHZ45SRpLeDqFOkdxyEpULpkfeEI0-EFcm8vdXwaZTCL6fbGbky3vQwc3D1KRuMpfouQ7UPRM2TeiKg_ckj0ZcT_1X7NYC_9mQ5W5GbawCAqtMhwaanxZ_QGru-1HCgbdB2o4XzO9tnRj8_oPvhsfi6f8v7gpX3hkSLbbxlbpSXKE9qkjbTEk24laaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQ-WWZ8i4u9EzFSWOidbIRwwOCpZcOljw9Kd86XvIfjyiXcNcQA1pwEEdOVcsV7UB7vKOMFt9EO4e3tP_kCxcLWzJuRWa3Sp30fnyaU1LDUaSMtlPKOLrI9mJOXOrso6afUHpfxVFygP9BMQRjOBsL-hEnRG6OMx3XNuUgvawg7F0LlTACGXrIwHWwV53orPe6az2V7mXyF3IAMJ4RYa2eUz_Pleo-X2s1toG0_s4k2CQweyWhdedHUR7v49vuYA9yh3VopUp5l0XjSDfMERUjqq5FbMy-KLsWEIc57OZvIkx8wZ4JjITwzL1eUwEFNxveWTtQI0_zYtbtDWmWF94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOKAW6OeOCPU_2778RAKVbSa1UMPtL9-efT-pT1Ubp4dakAsD9O5DU8PNyUi45KDZzwaIDdZpQL9pRNHUWgcn_lQkakmzvOrRg4BCMJBxf8Z0HbDhxZbkR6pNIKaNJC_oA0bglQnArptnGYsuT53RSwGcT0QDy_0NizRwW20AgGkMZ1kxbKmh5k_NL40igL64SYPUvcjA2BK703eNL3KoDrGRKAGu_legE-RV5WGpmW4LYj7PEPyCOWZkKxEsYJvPYSqpbrE3R3kCWibQvajWwar3an22j8a1cj91tJzrJaLLq0KfGJC6yI8hR9ixuh3Mm-5U3XODDmints9-PJQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dsMacjHZTpROQEuEy-VT4vXHLtohAaIPz0lJj9jNqOvjUfDPFTFEzYVUR7refVEs3Zjnay-e9REpMEGN2MiJ8so-YfKFYmK8VCZgG2UQ6D1oUD77JzLv8Rt7E-PqQFBy4VlzCM6tXteV7eYXU6XM2vxpP4TRAc4A6lcGJyVVje-bDAUg017D0clFUoH_x7sJK64zZR8DZZEL99mZ4PHe33rKKpilnu126gjM7WaLbmU_ULnxmxdahOEhhwUjrb_6gFN_eiu_Fm4mmkN_U7ft5kn8ceS98fCukva2WUwMNuRiDpVtXNc4zi63ZTlH1OyfZgU3tI4sexG9EvGuJOYRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pN6pBdOO7pR8nOK99xhwgwXOmvXcws2UVhSeqwUkOnYbxlyQ41B0mMrCd7T8itxPSvf9V53r_HyU8JWzmocLj0x6r3xqEBNKmbZ9e4FZ_DN2CCU4yjRPMjZXGlOY5EbvA4tUZRhCna1OmnsQgoZ40Ta300V4J0yIJVvy1R7MgdAORxB-vwOtbSYrXKVPkI95oVuWM3LLJq7-4p5rn8jSRnzSVKogZbT7il5JpR_ejDotuxJLL1qVmj_6JcbXrjZ5mnw1l6mzGPwPx_Yw-kMXkS1IowBknPvOqL1G5L6SsSLPV7cbY14AuZy99wxiBXyIoyd9AQUpzeNlM_x6SpdohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7LpaUInGSiagftHzofCeB57T_OdB7eMr3Uhr2CshGlCMapApayG-0_b9zrPXBZTM5x8r-seCWPA1rOewZBw4E2W9xSxBelC5L4tT_pCGUDo8eBSGWsK2XZ1TKwgTA2Pv8zXcnShkttTBokS4nkJLXBxZSNm5bFD9Uid2MvuORBh7GFXGNn3_kpiJ5fwD_eT-sYISPq7o7YmeleAO5pRq7GemUJbSrdxooFUpSrjybcc4i6oc3ipn2aXhk6XGZIDc0pDES_gyG-IH2xhONi0K-PCit6jx9lzmu544tFth6FtZWjKvi3Qn_H8rxYwwh03H-ByJpFGBlp1Lzyqds7nLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/459103" target="_blank">📅 03:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459102">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a738e19ca1.mp4?token=Y4iJnOcr77m3YhGqiYRpDFAwiV2kqLP-90gT5Mc1NXwLSi3Z7vd8QZd-AG9whSHXW6aFFCt3hu5_lU9hG_z3Hpx9t8siltoAZa0FilIkAiyFji1Fnf-RHdDC3577pz1vQqBRUmUJ8mj-MiTNL6HWhZC0IId3_2nHDcgdI1j8sDLNNCTgwQENFcRf-1kIyPs3l_dKQIW4DQAWcEFsuuDMWtqZHHzW51qswnZ437c6TgJLH_igrnp2ErYiNnuTjmRpbArZcXyNY-RctV8UIPs-_IiVtaopozq5obkz_bdIS3wBmJpoRn1QJSywNF6CAtJ54NomdZrdEwOOmNyDP84ScVoJjV5gq-l_gaAqUA73pTT7a2PR_ZHYDIUtLrw-w4THoaL4Fn-8LgXCS4Aex4_Kq3wIglVNUKwUt4dcWS-8oh7Wqx2GETYzvCN1QzsARRCTcoGzMsaJUbWcSME7VC1me-50lVDySbPmsBhnao70Mt6bXAliqcRZ-VMFP8a2jydaIXVGxe9wh7KbFL9hTnhVJlX3YCwtFZcuEUzincKQAZmYbZiRrStBZP09y5OeLBjLRIRe3zgwoq6e5mn-IW9fPnhqpQYhhf6sZKC1vZa9vLQ6bcitZUjuoveIkqPZAYPXhOw3fLNfQ5cgLRE9T59P4de1I7xHcG6A8RBCVWQmMWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a738e19ca1.mp4?token=Y4iJnOcr77m3YhGqiYRpDFAwiV2kqLP-90gT5Mc1NXwLSi3Z7vd8QZd-AG9whSHXW6aFFCt3hu5_lU9hG_z3Hpx9t8siltoAZa0FilIkAiyFji1Fnf-RHdDC3577pz1vQqBRUmUJ8mj-MiTNL6HWhZC0IId3_2nHDcgdI1j8sDLNNCTgwQENFcRf-1kIyPs3l_dKQIW4DQAWcEFsuuDMWtqZHHzW51qswnZ437c6TgJLH_igrnp2ErYiNnuTjmRpbArZcXyNY-RctV8UIPs-_IiVtaopozq5obkz_bdIS3wBmJpoRn1QJSywNF6CAtJ54NomdZrdEwOOmNyDP84ScVoJjV5gq-l_gaAqUA73pTT7a2PR_ZHYDIUtLrw-w4THoaL4Fn-8LgXCS4Aex4_Kq3wIglVNUKwUt4dcWS-8oh7Wqx2GETYzvCN1QzsARRCTcoGzMsaJUbWcSME7VC1me-50lVDySbPmsBhnao70Mt6bXAliqcRZ-VMFP8a2jydaIXVGxe9wh7KbFL9hTnhVJlX3YCwtFZcuEUzincKQAZmYbZiRrStBZP09y5OeLBjLRIRe3zgwoq6e5mn-IW9fPnhqpQYhhf6sZKC1vZa9vLQ6bcitZUjuoveIkqPZAYPXhOw3fLNfQ5cgLRE9T59P4de1I7xHcG6A8RBCVWQmMWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: محل استقرار جنگنده‌های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق درهم کوبیده شد
🔹
روابط عمومی سپاه: مردم شریف و بپاخاسته ایران اسلامی، ۱۸۳ شب حضور حماسی بی وقفه و تاریخ ساز شما در میدان، دشمن را در بُهت و حیرت فرو برده، امیدبخش مستضعفان…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459102" target="_blank">📅 02:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459101">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
سپاه: تجاوز دشمن تروریست در جزیرۀ لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🔹
روابط عمومی سپاه: دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی،…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459101" target="_blank">📅 02:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459100">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مبدا حملات آمریکا به لارک کجا بود؟
🔹
داده‌های ناوبری هوایی تایید کرد حملۀ پهپادی آمریکا به لارک، از مبدأ اردن و با پشتیبانی پایگاه‌های این کشور انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/459100" target="_blank">📅 02:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459099">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
اخبار غیررسمی حاکی از انفجار در پایگاه العدید قطر است.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/459099" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459098">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcRCu2Il9qw5Cit65XKHwWpfq2jYohaQvlq6LMRdLyVNVL3Xx4RzK8tx9arw_JiP3cB3OfRRd8OVUQzdRF7vBqNoRO7TEKeb6XLE7BeHHegmqut-z9lXhaW1h5GRHlCsBt7GA0G8rsXlMyBHJ7LeswdVHD6SdWOqgZY4X1lw7_N0zAPTu0bcyJpRCLbkQ01LeN035HWe2AjOcdeD1VMuJrk5e5CpfwmFPvyhFakVuu2bxyGw9w8I0LOJM0B45ZYoJYl7yWA_REo4O4jgM9mCfBrFr-gXHpqKnTmoyQRRnYt7u7LNjCly7i5dm4nc-nHsY6_zQLOOe2-0H0lbi9kxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی بازار نفت حین حملات ایران و آمریکا
🔹
بازار نفت دقایقی پیش بازگشایی شد، و هر بشکه نفت برنت در مرز ۹۱ دلار قیمت خورد. هفتۀ گذشته بازار نفت برنت در نرخ ۸۸.۳ دلار بسته شده بود.
🔸
براساس ادعای پایگاه کوبیسی‌لتر، افزایش ۲ دلاری قیمت برنت فشارها بر آمریکا از مسیر اقتصاد و سیاست را افزایش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/459098" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459097">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
منابع عربی از انفجارهای متعدد در جنوب اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/459097" target="_blank">📅 01:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459096">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBgFuWYTsi-KNNWhstB-F-EfYqYu38g7tgxnGykGaQS1uMgu_Ju8dRM88_1BcUxjai5hsFU_BzJ8JFH56rawXpS8SzkYH3Qo5i3sNJw7isocjwp5ZfA9dErsXgl-OK_jp__Bm8DB5ESjyJz6CS7V31aQOHpO0CFvivLmFKwnm9pMYR1mcs3yVhWkPIfqNFDb_-ed1tR9RIWeQ3bX4uV9bWtHqTMe_TnTYZ5TK3sB20B6YXz6WNZfm7DyhF3TG0asEn0946EdwBzRXLL3RX9tY4MghrSknAz81_Hg_pvUvkjrE78W9o9qneIkHRgTmQNIlKklroxSvKpqbZKoOihSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار سوخت‌رسان‌های آمریکایی از ترس ایران
🔹
پس از اعلام ایران مبنی بر پاسخ به حملۀ آمریکا به لارک، سوخت‌رسان‌های پارک شده در پایگاه‌های آمریکایی کشورهای حاشیۀ خلیج‌فارس، در حال دورشدن رصد شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/459096" target="_blank">📅 01:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459095">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3381114e02.mp4?token=CxB30otGXbbPNalt3We0aaO6i1M2T2eBgfy9JCuOk33dmJ4BWshsHlYq7JRZtBihMCbCZptn3aZJfIK57XGIO1pJJrETWhQN9WLawbM6rJYoUPZ3ukqg3i4DtHm9GR4LppA-nAD-ksf10QakRdNMBlAuvJ7Dpf9KVheGRsv7ChLdKAXrOpTSVgL7V_SYv8CIAkn4ExTp8Io0weUjWi2pytOe_PMiscgOyaMpK2CVuOlomlrrWb4AEPPd_jJ24j-8XjPYaCKo_NsQJX4_ZhqS7YIEN2a7VMTx7_E2RCGv35ccrYzg902mb3wTjAPovANZXl4yFXcedr7kjwpsJ9nIsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3381114e02.mp4?token=CxB30otGXbbPNalt3We0aaO6i1M2T2eBgfy9JCuOk33dmJ4BWshsHlYq7JRZtBihMCbCZptn3aZJfIK57XGIO1pJJrETWhQN9WLawbM6rJYoUPZ3ukqg3i4DtHm9GR4LppA-nAD-ksf10QakRdNMBlAuvJ7Dpf9KVheGRsv7ChLdKAXrOpTSVgL7V_SYv8CIAkn4ExTp8Io0weUjWi2pytOe_PMiscgOyaMpK2CVuOlomlrrWb4AEPPd_jJ24j-8XjPYaCKo_NsQJX4_ZhqS7YIEN2a7VMTx7_E2RCGv35ccrYzg902mb3wTjAPovANZXl4yFXcedr7kjwpsJ9nIsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: حمله به لارک در ۲ نوبت نزدیک به‌هم صورت گرفته است
🔹
صداهایی نیز در سیریک شنیده شده که مربوط به دفاع ما از مسیر ایرانی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/459095" target="_blank">📅 01:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459093">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
منابع عربی از انفجارهای متعدد در جنوب اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/459093" target="_blank">📅 01:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459092">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تعطیلی فرودگاه مهرآباد تکذیب شد
🔹
سخنگوی سازمان هواپیمایی کشور با رد شایعات تعطیلی فرودگاه مهرآباد، از انجام پروازها طبق زمان‌بندی قبلی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/459092" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459089">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_ALOW8ElpDneANWIfSpmLiWuIFDphKya0cwzMt2YrxkzR_eKF2F1qDSWcEc_O8SynTi46N6viLvmTHpIf6XA0LxoELnGsyOLrEbRxYskUmj3s-zzf6skj4zGBUIP7gmjJ2tZ7CsbxXOoDzpBRo1y-hwwy4wPsqZxINRf3SddEaEBCZnY0SRTrA3N-w6M5YOSM55_5pMPNb1aF2sugNIle_E1g0BCx4cLUfYzwIONO4bxtzaWnU4CIN8qGrQjfevr8kKR868e77BTPU6Ht9Fu3TPYwbNeAzpz4O92fBNka-rD4FSBcLDycG2whLQVolmGAx6eMb2GWe_nbW8nuretQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwUcMIsMjnkx1Dx48hgw-KX5WtT3QJSQggF_dDO4iM9IzUvtMEQ_qjbuM1YMZwavjF8exhuHAy6Io1RhvNBMswpCxCRCWrM2G-7zGMG_PJamI2d5gzFsoo42aS3nuz2lfNQC6XnyI8UnHNRIAPUVl2yoUeKUvLWlJ4yFfS_lByFncpcswNE9jOgt47aH-3yJNPa5P3Q-sxs5af3X4z_f_3Cgmxn-qFM3ENOT6iZEBX_DuUb-ppCBZpO_eRERl7eGvLRpbdPxEDsWUdILHtWDcg0Xh8v3Lq48xh5KM8Udvw6wJqXnmwt5L5BbhsU8fDJ6XGqdY7pf3jGh0XwXjJzuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ocCQIAQkNHwkFgvtpf-dMVTtIEWuS2CDe2MWYm9qlNYD8e1DGzQti0MfKITocYzY_0SoADj3XW9uSGtYyw1DH2xQgEktxtzDwnakn5PK5N8x0-PFA9gmmSqyAYDegEx0YAAsZ5dxycoAPkgi-Rfd4IDu_l07nWcsrtqoQhFvru9WIVAKPjcdb_LRWZHtauQNERN6hRFH6S8lAMVirqXev5qlGB_zylDD6dZW_Ly-Kdqm4hwxUwpPDwNV4aYZzsdnM0mJTIzIlA6Sbvvh-_jpUltVTxThFbIsHI7c40pTaj1u5pWXBdD66UDToo2oG4cvmIqXgq72Ai6MBBQQhR2LBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یاد دانش‌آموزان شهید مینابی در بین‌الحرمین زنده شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/459089" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459088">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLoMmcoK1tHzvVTItKHtFoSS8s-AOZ-QPXi9c0xZCC14AB_aM4Qee6Esvy2Qs3InOCsq0s4fC_LoE__pi4vJVZA_lNnoc2h-Jz8gmYnptxzDUDPm6hquDS5M1KIljzLI27_Zocv0eqW4jjA5iA8gLp7z244BQto9-Fcy9Yyfo4WPAMalbLAPaJMLac0Yx5wML_uWJwq8L69Y0A9u-CP5MxXTlXMNDr6FjL2O23UB0pYXG0kqmxgn_aqFUAQmNm0oQctgbXXodzUq5KcomgjahYZGBEeZQjSBv7_VBqCgAFZZINmAK61jg2yd1fFJCel-qcwrGcWB38gRNL71hlzwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی: آزمودن مجدد ارادۀ ما، تنها هزینۀ شکست‌های خفت‌بارتان را سنگین‌تر می‌کند.
🔹
بی‌تردید هیچ جنایتی، در هیچ سطحی بی‌پاسخ نمی‌ماند؛ پاسخی ویرانگر، دردناک‌تر و عبرت‌آموز که سلسله شکست‌هایتان را کامل خواهد کرد.
🔹
با ترس و وحشت منتظر باشید!
@Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/459088" target="_blank">📅 00:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459087">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">استارت عجیب تیم امید برای طلای بازی‌های آسیایی با ۲ بازیکن
🔹
اردوی تیم ملی فوتبال امید ایران برای حضور در بازی‌های آسیایی ۲۰۲۶ آیچی–ناگویا، امشب در هتل المپیک آغاز شد. پیش از شروع اردو، با توجه به مخالفت برخی باشگاه‌ها و تداخل برنامه‌های لیگ برتر و لیگ نخبگان،…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/459087" target="_blank">📅 00:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459086">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VECng5FuqlUtOkCrCm76GajJvXduBOGc6h2hRyaAZI54SecQfXjcgUgMf6lRdJ-c8GeNHEZyCFlSvycc491a_3fSBM8kcZlM82c-owAWZIUOuamuFmWJyN1Fm9Ei949_HJyjdMClkFDaccSNTFt82FGfrOGWx7WF9tRbnQI_0aEUIntNg98S89TdOHEnXA2zUa_eicf_AEok3xtyY7oPjjDAgiVX8SFwoLV13oTstr9wEpLFcEs1rLsFDaQnsFMM-auXbukmskXg1Z7MVxytGHGcMHBnm_8iOf9EBnmajok1KvAHqPL96fvbRcxRVX8xnwpwQaPLmViZdhBwJ3a3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی سپاه: اقدام تجاوزکارانه دشمن تروریستی در جزیره لارک، با پاسخ و مجازات مواجه خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/459086" target="_blank">📅 00:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCTx46UgXI4Tg5u8tfAM9cigKcoiM-VI8Ua1eXvK773sVq-RMgRVLhzt3ZwoWGZzePLzBfT3vmBkgbX7-40iQjGGqyQAIWgyAdhoH6YM-9PymO7bWAEG4645j0PI9y1Ri4fqeS7Ss7dmWyT2ZJqRUNQ7gqAUy8cH1I895CdR1pDnbrsDoHS5grQM60qCbeYh9dXEvleg6VaAKTA_T4mkxR4u2T6476ZSkcs1EbQNYWN-5xKiNa4QA_jyqHKqe8j4Tp6qy3x2ewRouiFEU5t4VhAdkd5j5d1McrFIyfqhl8aGNcVO_kzSduQ8HqFwkOGXge49q-ncuvFNlaoy0o5C7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور رهبر شهید انقلاب بر مزار شهیدان رجایی و باهنر
@Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/459085" target="_blank">📅 23:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459084">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e7aa5b3d.mp4?token=XpK0w06qkT6vVK3GcUa7GnG7TQYWjOIQ_ORmYWQ4oapAJFYOvB1lL08yNvqrVH0eBiWNxTSDB3QaAdI0j7RBjoEQ4AmGt69oPKlgVL8EMZqIKNbPm_5xe9rOTGBDkYXkcAWbKirwV4qmvbmqmEmruCsgQSnj7Z67Y3V68GPJXdAsFzwEaC6CuJ49A_S_nV00EwjpGT46kmsOKMHjC5suoJBYOAU7n89VDcq3kAXooggC1cEsqh6amgo9DVT6D8ZaUGWwqf2yED-pwR3SUZNpDC0vALwf8jgYe91tyxlPAbxR-B_2Y4sETYkPxEjfWV3nLu3-N9eC-waWTFUAC9xKQTnXN8rNtuxREch0z3k8QzLnPPPrq-o5DDnELiED8aCaPdi3zgZ02fSPxp2xpOI_ZKsbDJ8bkLR2sc0pPYcSCOyPXkjK7P0T_YOknlbvEx0dymCYpvMwSTa_scE1cyViRs4jbxv3UvpiWKibzSHcS7DWPA0AFjE1-Nyv1042D29mGWVkPEHYFCbOPm2YzxLHFSRYeo4p7z0YT4GADAdb_4-Df2Z2pTPrW0V06JB-VYSleNkBhakPvhqBkLAnvNBjEOomP5U01dvMCtPrxLAonT7qi8EJHE8XcSfhbiDwtxjPVUmBnlk87dcakiqqUDrxAU4_Pvrrnblha67mOrq77Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e7aa5b3d.mp4?token=XpK0w06qkT6vVK3GcUa7GnG7TQYWjOIQ_ORmYWQ4oapAJFYOvB1lL08yNvqrVH0eBiWNxTSDB3QaAdI0j7RBjoEQ4AmGt69oPKlgVL8EMZqIKNbPm_5xe9rOTGBDkYXkcAWbKirwV4qmvbmqmEmruCsgQSnj7Z67Y3V68GPJXdAsFzwEaC6CuJ49A_S_nV00EwjpGT46kmsOKMHjC5suoJBYOAU7n89VDcq3kAXooggC1cEsqh6amgo9DVT6D8ZaUGWwqf2yED-pwR3SUZNpDC0vALwf8jgYe91tyxlPAbxR-B_2Y4sETYkPxEjfWV3nLu3-N9eC-waWTFUAC9xKQTnXN8rNtuxREch0z3k8QzLnPPPrq-o5DDnELiED8aCaPdi3zgZ02fSPxp2xpOI_ZKsbDJ8bkLR2sc0pPYcSCOyPXkjK7P0T_YOknlbvEx0dymCYpvMwSTa_scE1cyViRs4jbxv3UvpiWKibzSHcS7DWPA0AFjE1-Nyv1042D29mGWVkPEHYFCbOPm2YzxLHFSRYeo4p7z0YT4GADAdb_4-Df2Z2pTPrW0V06JB-VYSleNkBhakPvhqBkLAnvNBjEOomP5U01dvMCtPrxLAonT7qi8EJHE8XcSfhbiDwtxjPVUmBnlk87dcakiqqUDrxAU4_Pvrrnblha67mOrq77Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای کمپین تکراری علیه صداوسیما؛ مراقب دوقطبیِ تکراری باشیم
🔹
انتقاد اخیر رئیس‌جمهور از صداوسیما، اگرچه می‌توانست یک اظهارنظرِ معمولی باشد، اما تیم اطلاع‌رسانی دولت، با توزیع گسترده بخشهایی از آن، آن را به یک کمپینِ تبلیغاتی تبدیل کرد. گویی قرار است این‌بار هم همان الگویِ همیشگی تکرار شود؛ الگویی که در آن، هر ناکارآمدی به گردنِ «نگفتنِ رسانه» انداخته می‌شود.
🔹
رئیس‌جمهور مثل هر فرد دیگری حق دارد که از دستگاههای مختلف انتقاد کند؛ اما وقتی این انتقاد، توسط تیم رسانه‌ایِ دولت، به خوراکی برای دوقطبی‌سازی ِ «ما در برابرِ رسانه» تبدیل می‌شود، جای نگرانی دارد. تجربه نشان داده که این تکنیکِ فرسوده، نه تنها کمکی به حلِ مشکلات نمی‌کند، بلکه سرمایه‌ِ اجتماعیِ دولت را که مرهونِ وفاق و همراهیِ منتقدان است، به خطر می‌اندازد.
🔹
نکته تأمل‌برانگیز اینکه اعضایِ تیم اطلاع‌رسانه‌ای فعلی، تا دیروز خودشان در بیرون از دولت، تندترین نقدها را بر دولت وارد میکردند؛ از تمسخر تکیه کلامهای رئیس‌جمهور وقت تا کوچک‌نماییِ دستاوردها.
🔹
حالا اما انتظار دارند منتقدان، بدونِ هیچ نقدی، ویترینِ عملکردِ آنها باشد. این تناقض، اگرچه برایِ مردمِ امروز پنهان نیست، اما دولتِ وفاق نباید با این رفتار، اعتمادِ همراهانِ خود را از دست بدهد.
🔹
رسانه، آینه است؛ شکستنِ آن، تصویر را درست نمی‌کند. امروز که رسانه‌ها از جمله صداوسیما، با درک میزان توانایی دولت در شرایطِ جنگ و تحریم، بیشترین همراهی را با دولت دارند، جفاست که به‌جایِ قدرشناسی، با کمپین‌های ِتبلیغاتی، فضا را به سمتِ تقابل ببریم. دولتِ صداقت، به‌جایِ دوقطبی‌سازی، به نقدپذیری نیاز دارد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/459084" target="_blank">📅 23:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
سپاه: تجاوز دشمن تروریست در جزیرۀ لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🔹
روابط عمومی سپاه: دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی،…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/459083" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683a1d1a08.mp4?token=W4riXp_t0cwH6xZSx7ytYUzi552sML6z3ytEMKBY36LBi_Dd13uOBTVYGyZKbb3y9vBMfWm4VEQJ-7cSPzWVDg5BFeICmvqi79eEkrblterJg2oddcNesASw4d4CGcFaQ4LsR5pNwgdfvdgJ8kW3g3SF6ARJ6i3sYDzAQQoWcsEyAwULvKbXza3Mm5bTcXKXxDT5o0AcmpMm3geyn395PnZ0g-7xCtTgQ7KMbvvsLGpVMyGZbizE3yO6-DlLAtIxPcin_L8LDpG67NY3QHIazeKfHNX-hGKOKRo2wR7Kg3PdV0uN4Mxl6NgQ4wDhs0rFU317zp5tCfCLNCKHJnVWPEPHJK0F0PiXJxtTYawaBq_KuQZZkWWZldphdagTWFG8othAcfZ6yjwRESptOGjL1ARsGjJ8eOsYKiUEBQIj4dPXWmDomXF3Bzomhxp7A9LBS-NT338RIBnVxzNH3GjekBH1LHFkr8VlOZx-GVfCLnz2bCgLwt3WOpw02OM4_q8XpFzMJSDuwl9ACmKRzQkJGoRs5TY0KgmWxlBfMfx9F8YepxKXkp8t9pcYF4OGdX8BlHSxgGBzvXoj9KZgaudLYNq9T886q8Kwi2orK9iNBTMmGSn18qtKEBFSwuhvI_GmeKjvbSIxRBP4q9JKQzwCK_wEKKx2jvru7scpGt1FZH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683a1d1a08.mp4?token=W4riXp_t0cwH6xZSx7ytYUzi552sML6z3ytEMKBY36LBi_Dd13uOBTVYGyZKbb3y9vBMfWm4VEQJ-7cSPzWVDg5BFeICmvqi79eEkrblterJg2oddcNesASw4d4CGcFaQ4LsR5pNwgdfvdgJ8kW3g3SF6ARJ6i3sYDzAQQoWcsEyAwULvKbXza3Mm5bTcXKXxDT5o0AcmpMm3geyn395PnZ0g-7xCtTgQ7KMbvvsLGpVMyGZbizE3yO6-DlLAtIxPcin_L8LDpG67NY3QHIazeKfHNX-hGKOKRo2wR7Kg3PdV0uN4Mxl6NgQ4wDhs0rFU317zp5tCfCLNCKHJnVWPEPHJK0F0PiXJxtTYawaBq_KuQZZkWWZldphdagTWFG8othAcfZ6yjwRESptOGjL1ARsGjJ8eOsYKiUEBQIj4dPXWmDomXF3Bzomhxp7A9LBS-NT338RIBnVxzNH3GjekBH1LHFkr8VlOZx-GVfCLnz2bCgLwt3WOpw02OM4_q8XpFzMJSDuwl9ACmKRzQkJGoRs5TY0KgmWxlBfMfx9F8YepxKXkp8t9pcYF4OGdX8BlHSxgGBzvXoj9KZgaudLYNq9T886q8Kwi2orK9iNBTMmGSn18qtKEBFSwuhvI_GmeKjvbSIxRBP4q9JKQzwCK_wEKKx2jvru7scpGt1FZH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار همبستگی میدان و خیابان در مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/459082" target="_blank">📅 23:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxxlKuoc3Las0Bs7QAF8qHAjcIRNIsb95MJNQBEc0wS_VZMDdToGpPXQr1U_NoxKxGfl78xc2_RE3VeduwvwWifPBXcctIjZvGgWejsBYa77P1698-qexPXIKmtlyorPaal3HI-2QK8vyi2cfsccuydhbRsan0Pvrs2zABu0o_jnjSfR-Q1-Eedw5tJhtak4IGFeDyJvD5Qa59qhKz91R7en63kod08T4z5UwGHS16SVbrpwqXLX-5zqeRq33SvrkmzDrbVTlmtDHRBFYnR23lRQjJPg66c45jsfqM9xFNpc0_nuuTZBQ59f9pnPcVG6YOJWFTf9IKrhkEkc8l2_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده‌شدن صدای انفجار در جزیرۀ لارک
🔹
مردم محلی از شنیده‌شدن صدای انفجار در حوالی جزیره لارک خبر دادند.
🔹
هنوز محل دقیق و علت وقوع این انفجار مشخص نیست و پیگیری‌های خبرنگار فارس برای مشخص شدن جزئیات انفجار ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/459081" target="_blank">📅 23:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459080">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2933b57941.mp4?token=ol8h_K-f9E8LQIMuju4xBge5vn5GBik3SllQsT3FTA01U0licnppjs1VuIUddpj-HCLXsWobkrM0MnHrV928khAdTOmxjn7s0a5T3lLlMUymEzlqU09ArP14CgIeG2P3NPYkoFTdLUh516ghDaZJmh7PDOCNCSstuCYAccFdwolOTgMf-GaDeGFpL7cGnFL4HMFhBLu9W-wFw3aLf2XQSLGXbytjfccNdwGgKInlEbzuyPUvgmwpICMAu9EcU9AFHqGGfUQstZBmtzVl9LiK_rX1Smo-SCbOCEoiG_P1nPzKPEVDxi1QiNbTB63UkwGNeWcvPXH_qwIA6q2E32-UFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2933b57941.mp4?token=ol8h_K-f9E8LQIMuju4xBge5vn5GBik3SllQsT3FTA01U0licnppjs1VuIUddpj-HCLXsWobkrM0MnHrV928khAdTOmxjn7s0a5T3lLlMUymEzlqU09ArP14CgIeG2P3NPYkoFTdLUh516ghDaZJmh7PDOCNCSstuCYAccFdwolOTgMf-GaDeGFpL7cGnFL4HMFhBLu9W-wFw3aLf2XQSLGXbytjfccNdwGgKInlEbzuyPUvgmwpICMAu9EcU9AFHqGGfUQstZBmtzVl9LiK_rX1Smo-SCbOCEoiG_P1nPzKPEVDxi1QiNbTB63UkwGNeWcvPXH_qwIA6q2E32-UFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۸۳ بعثت مردم و حضور پرشور تهرانی‌ها در میدان ولی‌عصر(عج)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/459080" target="_blank">📅 23:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7627bc0740.mp4?token=mQ7CnSFq9zAKcBg6BJL4jpuZDjQTbpZKtwUnj1gPPhajXq7pZ-Of1gY1rp4MchnVcfzp8QWotM2SoKburDmfcXqNRTqT9PBBnyvVzHL_O3xwX9FWrUx1mElTmRK1UzWPecm2C1ziaZNj6WyKdcmjroukSlL_EXpws7xZzwxCZxf595Yp_0qEPT9NlRjsLft083qR5jPtAMLNs3Vc2dsq9YuCmmfeZPsNAjT6MQ1p2WEYk8afWsniypaHmEp_szuVZBc2eiH8KIZ1Ks_SnmEyhcq5yP9XzXZlvhGW1I4wybTW0W_94G6kcpxYgNlZlTQ6H1KiGZtHaCgUSR9q8yRAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7627bc0740.mp4?token=mQ7CnSFq9zAKcBg6BJL4jpuZDjQTbpZKtwUnj1gPPhajXq7pZ-Of1gY1rp4MchnVcfzp8QWotM2SoKburDmfcXqNRTqT9PBBnyvVzHL_O3xwX9FWrUx1mElTmRK1UzWPecm2C1ziaZNj6WyKdcmjroukSlL_EXpws7xZzwxCZxf595Yp_0qEPT9NlRjsLft083qR5jPtAMLNs3Vc2dsq9YuCmmfeZPsNAjT6MQ1p2WEYk8afWsniypaHmEp_szuVZBc2eiH8KIZ1Ks_SnmEyhcq5yP9XzXZlvhGW1I4wybTW0W_94G6kcpxYgNlZlTQ6H1KiGZtHaCgUSR9q8yRAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح بیش از ۴ هزار طرح در آخرین روز هفته دولت
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/459079" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395013da0d.mp4?token=IDGszFWXzdwHlKNKxIkuhITrKLJeBq4fB0U1YLOGOGb4gbWD65SwwMNL1ydCpcIL2Dqd1Tpx5QrPweawJKd5fLZN2zVgIkLufM3aEBj9GTW2LQmdfQyCV5T9gQX-vv9urSIhI0l4ulxm20_AV57uA3enrTWxrUhJ6Yhhh5-k8IWDkdq9FLvlWGzHX2ZA5HLPUFYvjjSJv8v9cAPCHlKTnwXG_S4e6n9Le6px9A8-DyxvE_xS6bN6oiqi3hjPAMXYhorDeGEBWbSfjzPHYc6qYSJclzTfn5vI8SWfCPVlrqlNVHhtmfQ5CkhReux1WI5iaWP-hy7VfVupe8EAHI1bRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395013da0d.mp4?token=IDGszFWXzdwHlKNKxIkuhITrKLJeBq4fB0U1YLOGOGb4gbWD65SwwMNL1ydCpcIL2Dqd1Tpx5QrPweawJKd5fLZN2zVgIkLufM3aEBj9GTW2LQmdfQyCV5T9gQX-vv9urSIhI0l4ulxm20_AV57uA3enrTWxrUhJ6Yhhh5-k8IWDkdq9FLvlWGzHX2ZA5HLPUFYvjjSJv8v9cAPCHlKTnwXG_S4e6n9Le6px9A8-DyxvE_xS6bN6oiqi3hjPAMXYhorDeGEBWbSfjzPHYc6qYSJclzTfn5vI8SWfCPVlrqlNVHhtmfQ5CkhReux1WI5iaWP-hy7VfVupe8EAHI1bRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: سعی می‌کنیم ۳۵۰ هزار مسکن دیگر بسازیم
🔹
قولی برای  ساخت ۸۵۰ هزار مسکن تا دو سال آینده نمی‌دهم. @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/459078" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d22ac977b.mp4?token=F5djz2YkGIwOWl_bOXrAvJEMZQizCSYL-1LG70CIauaJ20YFW6qr1wmWCK9ddwAzhRPhg9NE_V7bm1vCiu4KOxkmBOXhXV-1LWnGNVjPJA0lyY6ii5439f3ZIAy5N7BxpYXLrfeCQo5k1nNWsqho_9ys2dj5fKlnHEsKkalb82YWH-89H96T6sf0bIEWhTmpm2GE9EVd0NQPWAyDs42e1fkEE52mg1ahI1Ct4hSZG4iZJbLuXiSsjwddNg6X4EuOVM_OuxmT7zEuOWgqwrqf07_voyLrQGXQoowkm2w4e5sOYGid9JNDMnqug5g6ctwxFkXzXGbckUe62KeKGeU3HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d22ac977b.mp4?token=F5djz2YkGIwOWl_bOXrAvJEMZQizCSYL-1LG70CIauaJ20YFW6qr1wmWCK9ddwAzhRPhg9NE_V7bm1vCiu4KOxkmBOXhXV-1LWnGNVjPJA0lyY6ii5439f3ZIAy5N7BxpYXLrfeCQo5k1nNWsqho_9ys2dj5fKlnHEsKkalb82YWH-89H96T6sf0bIEWhTmpm2GE9EVd0NQPWAyDs42e1fkEE52mg1ahI1Ct4hSZG4iZJbLuXiSsjwddNg6X4EuOVM_OuxmT7zEuOWgqwrqf07_voyLrQGXQoowkm2w4e5sOYGid9JNDMnqug5g6ctwxFkXzXGbckUe62KeKGeU3HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌داری گنابادی‌ها در شب ۱۸۳ به عشق ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/459077" target="_blank">📅 23:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در جزیرۀ لارک
🔹
مردم محلی از شنیده‌شدن صدای انفجار در حوالی جزیره لارک خبر دادند.
🔹
هنوز محل دقیق و علت وقوع این انفجار مشخص نیست و پیگیری‌های خبرنگار فارس برای مشخص شدن جزئیات انفجار ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/459076" target="_blank">📅 23:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8344de3119.mp4?token=OPAZk8CScjp6c0P_3F-hCTE6PChMtN8Gwfun23JOX16zMiAAI04UQLPdzRllc1toCRvNg9A4SmPRq-MIO5Pze3Rm_wiMzeTwS7DKpHN4H__dc879rq6iDVm78osUbmaAgn-PlUxrjWul0jEpDNsMzTtHf-tqhKuyruYKn-JfnAqKDutYDWeD9adWERlAvZV-emsq19i9cYc2rk4EFeAv0XH5ye8MxNOGjOipLd2H-m8YozIfU-GWIB_1j0udPh1S6bWL48oSDLd6G6KZhHiNvZA9yuinN-WFfzjYfcI_mQBTd-8lvSCa2lvqXdBqnaDMyzfsA1FhLm7wPddFkPgncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8344de3119.mp4?token=OPAZk8CScjp6c0P_3F-hCTE6PChMtN8Gwfun23JOX16zMiAAI04UQLPdzRllc1toCRvNg9A4SmPRq-MIO5Pze3Rm_wiMzeTwS7DKpHN4H__dc879rq6iDVm78osUbmaAgn-PlUxrjWul0jEpDNsMzTtHf-tqhKuyruYKn-JfnAqKDutYDWeD9adWERlAvZV-emsq19i9cYc2rk4EFeAv0XH5ye8MxNOGjOipLd2H-m8YozIfU-GWIB_1j0udPh1S6bWL48oSDLd6G6KZhHiNvZA9yuinN-WFfzjYfcI_mQBTd-8lvSCa2lvqXdBqnaDMyzfsA1FhLm7wPddFkPgncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: سعی می‌کنیم ۳۵۰ هزار مسکن دیگر بسازیم
🔹
قولی برای  ساخت ۸۵۰ هزار مسکن تا دو سال آینده نمی‌دهم.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/459075" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a8b48ecf.mp4?token=SXnrvhGPC3ekMmB6tbCRsttAco8QjyrwYngXhYwtrkluoeJrPIKfd9PBolwkbKb0VtjDAW2d-moHtQvhXOoSqPEfn-BfWQ2M5dm9VGd2SiU6M-o6Gu195gtgko8F2uB2DqrV-DevrFM0C4Pccw8L0yRmwUzwhO95W49qbt_IuSSCtbkdlVwEOYEDvyP-OAg6y44MK88rOg9q53wBCyr2gp7BTxpS9XYzzTtcWGkwA6Hxom1ab7ZVSrb2tn3fsLQZH4IyfFqrGRy28MFIqRVKC-4_A82DlWbOOjeR_Jt2zAy3huwKsddBYeNvkWR0_dgo0I47-sSz-vXGoMRSevFHtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a8b48ecf.mp4?token=SXnrvhGPC3ekMmB6tbCRsttAco8QjyrwYngXhYwtrkluoeJrPIKfd9PBolwkbKb0VtjDAW2d-moHtQvhXOoSqPEfn-BfWQ2M5dm9VGd2SiU6M-o6Gu195gtgko8F2uB2DqrV-DevrFM0C4Pccw8L0yRmwUzwhO95W49qbt_IuSSCtbkdlVwEOYEDvyP-OAg6y44MK88rOg9q53wBCyr2gp7BTxpS9XYzzTtcWGkwA6Hxom1ab7ZVSrb2tn3fsLQZH4IyfFqrGRy28MFIqRVKC-4_A82DlWbOOjeR_Jt2zAy3huwKsddBYeNvkWR0_dgo0I47-sSz-vXGoMRSevFHtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت صمت: بلوک ۴۲ درصدی سهام سایپا تا آخر امسال به بخش خصوصی واگذار می شود
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/459074" target="_blank">📅 22:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25999cd90c.mp4?token=W-wenqM1RSPTfluAq8AbEIsDXi1Cq7qQpgunZTD3xCMKA_YHV9D4nnjIny8aORuA7Wb5WJdcx1pNkwa0LhfjvIkK9el13FEEBYEI4SiLgLuHAdtOiQbOkHn6jB1WIfhmBdERHcrcoDKrsjnAaOI9-02NypPjJHzc8yC6rCgSaPgHtdX6-2l_eejmRr5WSKIV2oFiEDgiwpXcAuwpCqHUrOV884IL6yW2CsfvkCVKwFhPWTVAPxgAlQ279faPYXReVCyLUQjwr14h2bFTvDeX2ouZXw0w4m7LtBwOMkAWQEDWdXonO8P0s5-5cxy9wI6mjYaRMKGz_7YZe3fkPl5GIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25999cd90c.mp4?token=W-wenqM1RSPTfluAq8AbEIsDXi1Cq7qQpgunZTD3xCMKA_YHV9D4nnjIny8aORuA7Wb5WJdcx1pNkwa0LhfjvIkK9el13FEEBYEI4SiLgLuHAdtOiQbOkHn6jB1WIfhmBdERHcrcoDKrsjnAaOI9-02NypPjJHzc8yC6rCgSaPgHtdX6-2l_eejmRr5WSKIV2oFiEDgiwpXcAuwpCqHUrOV884IL6yW2CsfvkCVKwFhPWTVAPxgAlQ279faPYXReVCyLUQjwr14h2bFTvDeX2ouZXw0w4m7LtBwOMkAWQEDWdXonO8P0s5-5cxy9wI6mjYaRMKGz_7YZe3fkPl5GIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین ایران ایران در میدان شهید سلیمانی رفسنجان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/459073" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKci4wPa3RJ9ppV1P7qdhtpaCc1Lpfa7QeIKpn_tb5VqZZgy6N1BeU5o7RTWjRWQkCVfdqai_wF2iiY4J7pPA4qCvz6du-C2Wh5eMQpEhQzDmOpKixw8s5bKOpQ_AL6sWa54oOUS_LVZfKI19aFiPOrlrVGBCRmM9FGZncS3ylerT0SGdTK4rQy7797oiWny_hYmLIudTwwp_26dqv6FuB4xlKTbIwNWlhCcb95D19m0utYH42B0k5w4h6-S2l7_hLlfriWBBr4QgDUn3DB5Ws5jm38gopp8fkYY5RLSvqddR792az1Kur9geDbaPqsjTZjyMXGOpeeXKN4t50Oeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaeCfI4AcQ3cY0qguOnra5Ab3iILxkU-6OzFvQQs7dGMXr_tylKV0IbwAdSsuKtNCgvIz6ePzMnWUx2o2BX2ErYNR-OzPMNbnXMOzkjH0dNxJrDHXKt0oUUaWHrVyGG9RIK-ZaR7Oe5NSd1JjVqBI5TFJQPTA4Em1cT2RCAOJWLmTVDae8-d9m6plJrrzQlCiygywVIf6bHX6QxORcL7rYTWpjzCC55a5vpjpPu00PlctaTBq510-oisOXr3pdnhw7Seea_0L4IVfpq9P2L1EmhYiRxj7loPZ5ravYMz-mYK_RVFb7lnmtxF9PIkl6y4Ponma_FBShpsVpcKmhUASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRV_52GAVX3GS6E_ExMKr1Tkiumu_Mb0shmfBH629jkpavis5pAfal8TNYGESIKaMqCGX1xXWAwUMQELqMqdZQEi5GEA92ZQKmF42kK4ACWt1XqbqyfT1MAEbFnieZHEyUE6HlXreyEm2xrJ9HeNT0HOA4gV2v7Diu_V0LwF5KP7tt5TaNGtrcxjPXrXsUsQiltZmzuSSldt3uZa5ga44hixZfJuaSTvCZAVq_jNwWVZHOC1pJu5pQE6KPZHlOuNFij5CaaooBV4EUVGG167EuAyIeZJfHsp6zplG49hJBYjA_wK5Qs_Ac5-yf0znfV3aTcCe3JOS4HCNCXk6BrIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfaT7opTeXsGv0UvuIn8zdaaFxfJGKOZJKsrrizbp-Vn4CxXek1aDh8KCO_B8fPtSMofiuidTQBSxfq239Vd8rExNl0HIddXq9tVECVNWe7eKgUQIgnrdleQZ5IkQt7cSzbYjpWYsZMN34nkj6F1KCuvOFJLyvkR3GBsidl-MsEZhS5kTESliVxw3bVkbnWy4xpjEUkpTgKAKceCez_dl2cg6ZHB7RzV_vq4YEwIszm7zxg7tPaWeKTCvuD7rZX5TMhqFO508zPfsanO1SY0k1v7Oah6PMbVEVvN5ev-PZCOx0VD-ZjD6tTn6K_Zku40XKLKsevcgIDlATnMuQQAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjQkm0Sy_1f1oljGDaK9ZTn7m5lFtykfWONQIA_vzIOQ5V-aWQzbi4l32UKZUACbFLEKHBpAOGWI2b1UivdvdKyG8dXXTe_jhO76hkvWpPaFD602rQA9vsWUMgQu1kX6JxQN3KKFw9AJxEfLk2Y6mkLpjUIxmqjsCOp2rwQUWVNK1PQqEjdD-ZV9GP8DxGf09RFhjU8JcBqEV1UzkXbqeZmQnHgkRE0Yp4t9et6elqn0nHRlZIONS9ENXeUGJdEoRQnPeI9dGrA8QnHJyRmTzZMaFjutqJh_M_txEEkvDVLaK4UxDu6zELol05RtdqhryeymRuQJz6NZ71AHNvp71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYSe8ZlzuvrRBlQBy0ZYQ45mFI-YAajOKdu3_KCn4JQKkFQpFBhnWOkhCjy-xsg74HSUIXQk36J4h-nvHSBqAvxGF1x6a2SM-0v7sJlPSGIWPLNa_0Zfv3AZUQtPKck4sxtZmMr2rd9X5C9r0d7Tcwt36etKY6anew8NNCnv2_u1iSW2Or61BGak258ElYwYIvpNG27Iej95XPWhnPUuz70nWQDNpE4f8W52uRpVJAUKM9ZdsAQBWmmvjEM5qJ3U1w3iw1nKeNljZWmNEmG-5-sy57T5YOCrfb2pDaEqDc9tKn93oxysxLoPi7yPwgH8pB80BkIC27FTOGg6TIJnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYFp2XC1IHid6ubVxFvmByTYzBPoMCr0zo4eH_bDFccUehv6v_WA1XjkYV3tY-h_rmuG6WPwy6kIyJm9KKI4cGIDWsH5D55nx2aRReyZNTdZy38Oq1UBsbOFixRrPRGAexymt6tDs_fmQrQ4WDfMibhOOkONvc5CL5h00Arm5WvwI7QbjOMb5QbqsforCWV4LYsyc0nIGh8I8G0-xlpnM4BiJYFMLCuGrY2ESBsj8JKlVqmLXofkUkLGFtPKe89D0Y0tg2SF1q5Uedp7StutPVeEltBEUkydiUKseJ_FdQnOF7DcCGv1JYIUpwCwkuqVn2n2kufTqltLHOa2tUHIXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن بزرگ «امت احمد(ص)» در تهران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/459066" target="_blank">📅 22:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4f22402b.mp4?token=iBFQngbnA5OEEN5GwiVwd69P6u_9jQenozRKpQKMs-RKIqCdyFlySO-Z3CfTx7F_KXRcrR8E4sm9zG9G3mDZBv7hkpCu4LobeCeZuoCNImeWBDMFL7e78U6rD5PB5W9ddxQ4vR_OHRQqSvu4-RrECxZ9aZa4XovhA1Kxm19Gps3CXXFVrqrMtZkWoLRDfTCYI7XURKKc0c_E-Ny0ACXwwdXi96tPh8SrIOOkns3hxKInntnefWHY0O7vDZu1au_Rj-pGBPFyHvfv8suF0tAEmGKxw3L8aVAMPgEjk4--w2IQkjgVPBvYUDFKW5oUYygipbl2KUTQNQl--SG6OdpwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4f22402b.mp4?token=iBFQngbnA5OEEN5GwiVwd69P6u_9jQenozRKpQKMs-RKIqCdyFlySO-Z3CfTx7F_KXRcrR8E4sm9zG9G3mDZBv7hkpCu4LobeCeZuoCNImeWBDMFL7e78U6rD5PB5W9ddxQ4vR_OHRQqSvu4-RrECxZ9aZa4XovhA1Kxm19Gps3CXXFVrqrMtZkWoLRDfTCYI7XURKKc0c_E-Ny0ACXwwdXi96tPh8SrIOOkns3hxKInntnefWHY0O7vDZu1au_Rj-pGBPFyHvfv8suF0tAEmGKxw3L8aVAMPgEjk4--w2IQkjgVPBvYUDFKW5oUYygipbl2KUTQNQl--SG6OdpwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم مقام حزب اعتماد ملی: نباید به خاطر اخم غرب از تنگۀ هرمز عقب‌نشینی کنیم
🔹
به این زودی فراموش نکنیم چه کسانی حامی اسنپ‌بک شدند؟ همین اروپایی‌ها. مگر این کشورها حقوق بشر را می‌شناسند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/459065" target="_blank">📅 22:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defe8accac.mp4?token=RptTB-ncphBDDkvH-bULKNFUQMunMWYtR9g-l99mt4Ity5wsvvwNqQYazreC7iTDh_gTaJTM1P_sDAD818UcoM-sP9WCKd6P9psnG6f0HL_qGVzZi-ZPQh-RPk9YGoTXM72hJRKNAN2CvEnh0QD-NB_yFPtBKw-oJcbkmj-kj7ZiIKsqsUFV4d9l7DWBJp70VMbZ7nnFXp3A2DaGy3dN4igQsuYBvTTSJzLkOf6Yif4Co5ovvHN1Zo3k2TK2PHkuUTJaiW0K4vsket4SRlD5RpAAzS7Y50jEtTB3_mXBrHRlSMvuTxxqnrwmNrCQ-CHuSCgsC-Qa0q98gAiCfBoYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defe8accac.mp4?token=RptTB-ncphBDDkvH-bULKNFUQMunMWYtR9g-l99mt4Ity5wsvvwNqQYazreC7iTDh_gTaJTM1P_sDAD818UcoM-sP9WCKd6P9psnG6f0HL_qGVzZi-ZPQh-RPk9YGoTXM72hJRKNAN2CvEnh0QD-NB_yFPtBKw-oJcbkmj-kj7ZiIKsqsUFV4d9l7DWBJp70VMbZ7nnFXp3A2DaGy3dN4igQsuYBvTTSJzLkOf6Yif4Co5ovvHN1Zo3k2TK2PHkuUTJaiW0K4vsket4SRlD5RpAAzS7Y50jEtTB3_mXBrHRlSMvuTxxqnrwmNrCQ-CHuSCgsC-Qa0q98gAiCfBoYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجوم، پهپاد کوچک یمنی‌ها که مزدوران سعودی را تحت رصد و ضربه قرار می‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/459064" target="_blank">📅 22:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45df4384b4.mp4?token=vawLB7bIRJFPvo7ckdZRvxx_g8UEcv0vRZmIvDHLDIG1Ffyb8mK-nY-h99xTAfIB2CcJk_7N5RN7prf9So9SIlHlqojAash3Cge0-KDoPdk3mHIeXaY6gZ-Tiw3KiTzNo75sv7cle7c3XFoVI8K-hPdjJHmZdIqc8NcD8BJz66kQAE8-GDltwCJZhIlwjI4B9P679kojIJtHh5gzjS7U6HxonMUss12DqLDuj8Y1Z2qkdHcmGGOVvNtylBPFVx0ruS80B2kQzJvLdq0e5XVEbwR4INSxZUiLf6_LnfvFJ8hZo1Jesv4mAtuDcO3Wgrfk2rXZr3QYdglEVKH7eFMX7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45df4384b4.mp4?token=vawLB7bIRJFPvo7ckdZRvxx_g8UEcv0vRZmIvDHLDIG1Ffyb8mK-nY-h99xTAfIB2CcJk_7N5RN7prf9So9SIlHlqojAash3Cge0-KDoPdk3mHIeXaY6gZ-Tiw3KiTzNo75sv7cle7c3XFoVI8K-hPdjJHmZdIqc8NcD8BJz66kQAE8-GDltwCJZhIlwjI4B9P679kojIJtHh5gzjS7U6HxonMUss12DqLDuj8Y1Z2qkdHcmGGOVvNtylBPFVx0ruS80B2kQzJvLdq0e5XVEbwR4INSxZUiLf6_LnfvFJ8hZo1Jesv4mAtuDcO3Wgrfk2rXZr3QYdglEVKH7eFMX7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی دخترانه دربارۀ پیامبر رحمت(ص)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/459063" target="_blank">📅 22:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎥
رئیس سازمان اداری و استخدامی: بساط واسطه‌ها در موضوع نیروهای شرکتی برچیده می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459062" target="_blank">📅 22:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459061">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
شبکه آب شرب روستای اسلام‌آباد علیا شهرستان صحنه استان کرمانشاه به دلیل مشکلات ناشی از فرسودگی و شکستگی خطوط انتقال آب در وضعیت بدی قرار دارد. چندین سال است مردم روستا با مشکلات شبکه آب مواجه‌اند و موضوع بارها از طریق دهیاری و شورای روستا پیگیری و گزارش شده، اما متأسفانه تاکنون نتیجه مطلوبی حاصل نشده است.
🔹
طرح تعویض خودروی فرسوده واقعا ظلم در حق قشر ضعیف هست. دولت اگر می‌خواهد کمک کند، ماشین فرسوده را تحویل بگیرد در عوض خودرو صفر با قیمت سال‌های قبل تحویل بدهد.
🔹
در صورت امکان در مورد معوقات فروردین و اردیبهشت ماه بازنشستگان تأمین اجتماعی که هنوز پرداخت نشده در کانال خبری خود مطلبی ارائه بفرمایید.
🔹
امسال خیلی از خانواده‌ها به‌خاطر افزایش زیاد شهریه مدارس پولی و احتمال غیرحضوری بودن کلاس‌ها، به سمت مدارس دولتی رفتند. از آن طرف تازه در مردادماه به مدارس دولتی گفتند کلاس‌هایتان را زیاد حذف کنید و ثبت‌نامی‌های جدید یا غیرمحدوده را نپذیرید. آن‌ها هم شروع کردند به بیرون کردن بچه‌هایی که خیالشان از ثبت‌نام راحت بود. حالا بچه‌های سرگردان و خانواده‌های بی‌پناه یا باید ۱۵۰ تا ۲۰۰ میلیون تومان پول بدهند (و این شهریه هر سال بیشتر می‌شود) یا بچه را به مدرسه نفرستند، چون هیچ‌جا ثبت‌نامش نکرده‌اند.
🔹
از تهران داریم می‌رویم زاهدان. در استان کرمان نه کارت‌های شخصی کار می‌کند و نه کارت جایگاه وجود دارد. چرا باید برای استان‌های جنوبی محدودیت قائل شوند در حالی که در استان‌های شمالی و تهران کارت‌های سوخت همه‌جا هست و مشکلی وجود ندارد؟ تو مسیر هم اصلاً کارت سوخت نیست. ما با مشکل بنزین مواجه شدیم و ماشین را همان‌جا با خانواده گذاشتیم و مجبور شدیم بنزین ۲ میلیون تومانی بزنیم. آمدیم زاهدان هم همین‌طور است؛ نه کارت‌های خودمان کار می‌کند و نه کارت جایگاه وجود دارد.
🔹
لطفا پیگیری کنید. بیمه تامین اجتماعی نیروهای قرارداد مدت معین و قرارداد مدت موقت مجتمع گاز پارس جنوبی قطع شده است و الان نزدیک یک ماه است که مشکلات ناشی از عدم بیمه بودن پیدا کرده‌اند خصوصا در زمینه پزشکی.
🔹
آب شرب روستای قلعه چنعان شهرستان کارون (استان خوزستان) در وضعیت خیلی بدی قرار دارد. لطفا پیگیری کنید.
🔹
ما از مال‌باختگان ۱۲ تعاونی مسکن در تبریز هستیم که در سال ۱۳۸۲ خریدار زمین‌های تعاونی شهید مدنی تبریز به تعداد ۱۵۰۰ نفر بودیم. متأسفانه با گذشت ۲۴ سال، علی‌رغم مراجعه به محاکم قضایی، استانداری و مسکن و شهرسازی، هنوز موفق به تحویل زمین‌های خود از تعاونی شهید مدنی تبریز نشده‌ایم. خواهشمند است صدای ما را به گوش مسئولین برسانید.
🔹
من یک شهروند اهل استان سیستان و بلوچستان هستم. متأسفانه هیچ جایگاهی به ما بنزین نمی‌دهد. به خدا کارت سوخت خودمان هم کفاف نمی‌دهد. هیچ مسئولی هم پیگیر نیست. جایگاه‌داران می‌گویند کارت پمپ بنزین داریم ولی نمی‌دهیم.
🔹
اینکه قرار است ماشین‌های زیر ۸۴ از تهران حذف شوند و سهمیه بنزین نگیرند یعنی چه؟ خیلی از مردم در این گرانی پول ندارند ماشین بخرند و با همان کار می‌کنند. مگر با ۴۰۰ میلیون وام می‌شود ماشین خرید؟ پولی نداریم بگذاریم روی آن ۴۰۰ میلیون که ماشین بخریم. لطفاً قانونش را با این وضعیت بد اقتصادی تصویب نکنید. از کجا بیاوریم قسط ۴۰۰ میلیون را بدهیم؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459061" target="_blank">📅 22:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459060">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVO-jgKRnb41-TkUAA44ttsKDx0YrI3E-CWWNVKFKmxYMYN1Ets5PxOeI2fbDOR8yi1ZoHBYuiqEnDRHj596b8ca3-1uJbork8p0GcE5q6QQG4nHo-6rqZdL6fJ5ClcV-YhABHg5dkwo8xIJ7MJoJ_OimoX44szdvy7nxzDG9tih1trKu7GE6MR9qDsaTJyTmjPMPMLiISs_rn723pq5aDIBnY838LdG3P1CD9Pfq2hKYKglRicCg9SOZTaVWeeSPhq-fyaqCTnE2MRumgOFJHGQK3TSOt6Sz7SdRwCh6jUsYExUvJBPD14bTMKih2nejHGlHlp7Uj2qna7i0qliZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرارگرفتن یک نفتکش در نزدیکی عمان
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش روز گذشته هنگام عبور از تنگۀ هرمز در فاصله ۱۲ مایلی بندر الخصب عمان مورد اصابت شیئی نامشخص قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/459060" target="_blank">📅 21:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459059">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویارویی کشتی‌های جنگی ترکیه و اسرائیل در دریای مدیترانه
🔹
شبکه کان اسرائیل به نقل از منابع آگاه گزارش داد که کشتی‌های جنگی ترکیه در دریای مدیترانه به کشتی‌های نیروی دریایی اسرائیل نزدیک شده و برای آنها مسیرهای دریایی تعیین کرده‌اند.
🔹
به دنبال این حادثه، نیروی دریایی اسرائیل سطح آمادگی خود را در دریای مدیترانه افزایش داده تا برای هر گونه تحول احتمالی آماده باشد.
🔸
جزئیات بیشتری دربارهٔ محل دقیق این رویارویی و زمان وقوع آن منتشر نشده است.
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/459059" target="_blank">📅 21:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459058">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fb79d721.mp4?token=ECsbDreZ03J4Hdn1pkm8DrBuvR301IuUeB9Umtp71NrV-IVBj7KwlHbiX7-tX1UkERM20XE5roAk3g3BSHuCoxDPCYqgKjMt9Z8_QNU2q4OA3krA-frYv3EDtbNf98bVoIpNhLZYTb2alJkvylM8WEXCIjMUFfihg4o8ZPdm231US46AkizgzNG7_wGydpsNUbjy765TaGfN5i8KpimUhSfi9ArYeiMSgXgYDKWCgCfd6OZX-LmQLtVgJ9CkSKcd16y2YnV4ZRFddAR0u03pLlREihKTA-qd_DLSHAwSrkSE-k7-pO9m5L3sDlmjUmiMsD_ZVxtcWCGZW9EwbuAAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fb79d721.mp4?token=ECsbDreZ03J4Hdn1pkm8DrBuvR301IuUeB9Umtp71NrV-IVBj7KwlHbiX7-tX1UkERM20XE5roAk3g3BSHuCoxDPCYqgKjMt9Z8_QNU2q4OA3krA-frYv3EDtbNf98bVoIpNhLZYTb2alJkvylM8WEXCIjMUFfihg4o8ZPdm231US46AkizgzNG7_wGydpsNUbjy765TaGfN5i8KpimUhSfi9ArYeiMSgXgYDKWCgCfd6OZX-LmQLtVgJ9CkSKcd16y2YnV4ZRFddAR0u03pLlREihKTA-qd_DLSHAwSrkSE-k7-pO9m5L3sDlmjUmiMsD_ZVxtcWCGZW9EwbuAAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان اداری و استخدامی: بساط واسطه‌ها در موضوع نیروهای شرکتی برچیده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/459058" target="_blank">📅 21:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boc97_-bjawSrn_ReB_vwhf1rSJ5H7w9Xzxfe6S1K1IIsa690PMDWA_F8RE5sX0Aavm14py1_Op29WnCGFEtIOkWlCAyM4HOEaOpCTxV0oHXslNzTRD37pwo2g51dfOGrELbiqYfSMrjIZ82CoqpFp0DfqkU00AKixxH8SZdheBmWhcDvHsyUtXFQg_LevkSaSo8AC_gbQBYY6ZP25Lh3FTeC2SFRyU9FhnpyHGy3m1Y0lYfo7IbCHEymO5n5vqd-G3RDjjwaAlW2K5_FWD_Iq4eNVMipwh5ngYFFccE_ZB5UlGJ1w897kk29yalNZTUnfAx2B6eAJc3bWSsRNtaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ فعالان رسانه‌ای در لبیک به رهنمودهای رهبر معظم انقلاب
🔹
فعالان رسانه و فضای مجازی کشور در لبیک به رهنمودهای رهبر معظم انقلاب اسلامی بیانیه‌ای منتشر کردند.
🔹
پیام امیدبخش رهبر معظم انقلاب اسلامی به مناسبت هفته دولت، برای ما اهالی رسانه فراتر از یک پیام تقویمی و در حقیقت نقشه‌راهی روشن در میانه جنگ ترکیبی و وجودی با دشمنان این مرزوبوم است.
🔹
ما فعالان عرصه اندیشه و رسانه، با گرامی‌داشت مجاهدت‌های خادمان ملت و یاد شهیدان والامقام دولت به‌ویژه شهیدان رجایی، باهنر و رئیسی این رهنمودها را جان‌مایه حرکت خود قرار داده.
🔹
هم‌پیمان می‌شویم که در این برهه خطیر با بازآرایی صفوف فکری، بازوی توانمند جهاد تبیین و تقویت‌کننده پایه‌های انسجام ملی باشیم.
🔗
ادامه متن بیانیه و اسامی امضا کنندگان را
اینجا
بخوانید.
@farsnart</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459057" target="_blank">📅 21:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459055">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0528b651c5.mp4?token=CwE9ezgb-DshB9zPdxoTjPb2nWfqSW2hfLvv9TXp_4AruDmfniwEZm7fqTuF0d7wn3s97SUnirruX3CnAS8glh_z2ifkwlPRFSDkSdxXV_Bmw0ziDPLxwtYS2VpO0rY3-IYXAWfUT-6XvM-15-8gEEHq0tepYtfx93z-erfZvpQwts1ksit8JiWBDlP6HrXHoeLfk0sTK6xo8WWozZaZb4U35xjMQMdA-Fhx0hBiehjIUmH2UNIdbHuGDqmjDIFLy0t1Sudt279flC42dSxXbzJFTwNzir8jgHy8jUQlozxm3x5fiQlqYdwvroktU9XsKvNHbj42mSVX47NPCmzUsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0528b651c5.mp4?token=CwE9ezgb-DshB9zPdxoTjPb2nWfqSW2hfLvv9TXp_4AruDmfniwEZm7fqTuF0d7wn3s97SUnirruX3CnAS8glh_z2ifkwlPRFSDkSdxXV_Bmw0ziDPLxwtYS2VpO0rY3-IYXAWfUT-6XvM-15-8gEEHq0tepYtfx93z-erfZvpQwts1ksit8JiWBDlP6HrXHoeLfk0sTK6xo8WWozZaZb4U35xjMQMdA-Fhx0hBiehjIUmH2UNIdbHuGDqmjDIFLy0t1Sudt279flC42dSxXbzJFTwNzir8jgHy8jUQlozxm3x5fiQlqYdwvroktU9XsKvNHbj42mSVX47NPCmzUsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۸۳ حضور مردم بسطام استان سمنان در میدان اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/459055" target="_blank">📅 21:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459054">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuySauF09PMFa_1e2WiSGk43AcrzVlgjVtENv4Rd-BE06ArC1VQDEjBdajuUvdiNzTCnllc4gveXtnFDX46Ex3nDQjDvILLxgbT_FzUhNDWWYxgz8e0jhBSD29uqKfXWfW-5f1usf6yio3VMyoRVGc9DFlYwTX58ffBX__LxajAM8qdCo4E7dZwlxB619FfPH3by6aMhiptsyudt7-5_2nL_iSRm0RfkrsN0Um-bCT_oFdNcVi8MVXLruSOFicmwopc_GpxxT_xzK6_HzeJXe8KngOdQfgNTS6nSR_2P-loy1XJcUMskczMMhIKWotmF3z2RI3GP19tFvgc3NPVKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوترابی‌فرد: فعالان سیاسی نقش جدی‌تری در حفظ انسجام ملی ایفا کنند
🔹
امام‌جمعه موقت تهران: رهبر معظم انقلاب طی چند ماه گذشته پیام‌های متعددی داشته‌اند که به نظر بنده فصل مشترک همه این پیام‌ها، تأکید و توصیه جدی بر ضرورت وحدت و انسجام بوده است.
🔹
احزاب و فعالان سیاسی وظیفه دارند در این حوزه نقش‌آفرینی جدی‌تری داشته باشند؛ نهادهای حوزوی و دانشگاهی نیز نقش محوری دارند و باید پیشگام وحدت و انسجام ملی و تحکیم رابطه دولت و ملت باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459054" target="_blank">📅 21:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459053">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRqjMVfoYom_TSR-SQXT1Ge1qLAro4Ohjh9sBrbj58mUI3f4z7Iws8hz3nxYNlpTBJUZWTFx888ww6C79xCr0HPjuEFEba2mURLw25bK-sYYCDgWHmDYIJXqdvDyFEAVh9fGAxVfW6iaio9nRQtZgSjoS2NHJNQb_7uSkCM8umhyd4JMyD_7uUGP3Nu9d_JAPaJ7v3HwCrvi7mnSzK9vOeeqecVKYDxeRVp_YMbL1-qEAOYVchVbdwVAhoQkpgNZP-hjmW5UrNCLxgzqIJH4y73fTaAVx5LT8C61-_LdS2DDCgm12JumFLn3Ca36r2SqcNKJBaf4y5Iwwx3DwOojTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سازمان اطلاعات سپاه: دشمنِ مستاصل از مقاومت ۲۰۰روزه ایرانیان، «فرسایش ثبات و تاب‌آوری ملی از مسیر جنگ روانی» را دنبال میکند.
🔹
پاسخ مردم ایران روشن و مبتنی بر اخلال در توان فرماندهی دشمن، ضربه به شبکه همکار تروریستها و مقابله با تخریبگران ثبات و وحدت است؛ اراده‌ای که دشمن پیش‌تر قدرت آن را دیده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/459053" target="_blank">📅 21:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459052">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27a0efc341.mp4?token=VZxZCYJNUC1NEsn2eUmQnvBzzp3kxUf-W-RKB-yYrTx4NcjNpHottIO11sWpPk4SxiQ8AwEkj7ezde5ZBIczlQpKYqJGogw_BFEIerNdeaZ2W9G9p_7a0QJPnAAMpfWenn-7a3K1TQ02P_YbnFSFvYFFfK98mKS5XguK2xH91EP0WIrfSsILDaYmbZimHxLm8sWQ3YcuQQWWW61TC_3RCnd8-kKbawqMb64cDjmrjwGqWSHtBgqHMvfLv8-MmJ6_BN_HoByzGlrR87HwBaSCz5BDF_zvyUVPW6ftKeKfCXsgGTO1v4ESTeSLczRD-CUM16aDVUsbCSVTRzDq6HCjN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27a0efc341.mp4?token=VZxZCYJNUC1NEsn2eUmQnvBzzp3kxUf-W-RKB-yYrTx4NcjNpHottIO11sWpPk4SxiQ8AwEkj7ezde5ZBIczlQpKYqJGogw_BFEIerNdeaZ2W9G9p_7a0QJPnAAMpfWenn-7a3K1TQ02P_YbnFSFvYFFfK98mKS5XguK2xH91EP0WIrfSsILDaYmbZimHxLm8sWQ3YcuQQWWW61TC_3RCnd8-kKbawqMb64cDjmrjwGqWSHtBgqHMvfLv8-MmJ6_BN_HoByzGlrR87HwBaSCz5BDF_zvyUVPW6ftKeKfCXsgGTO1v4ESTeSLczRD-CUM16aDVUsbCSVTRzDq6HCjN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی پشتِ تیراندازی؛ این بار در نیوجرسی آمریکا
🔹
در پی تیراندازی در یک گردهمایی در نیوجرسی ۱۰ نفر هدف گلوله قرار گرفته‌اند که ۲ نفر از آن‌ها کشته شده‌اند.
🔹
انگیزه مظنون‌ها از این تیراندازی تاکنون اعلام نشده است.
🔸
ساعاتی قبل هم در یک حادثه تیراندازی کور در نزدیکی «واشنگتن پارک» در شهر شیکاگو ایالت ایلینوی آمریکا، دست‌کم هشت نفر هدف گلوله قرار گرفتند و زخمی شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/459052" target="_blank">📅 20:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459051">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">توقیف ۲ میلیون لیتر گازوئیل قاچاق در آب‌های خلیج فارس
🔹
فرمانده مرزبانی فراجا: مرزبانان پایگاه دریابانی بندرعباس، بعد از اطلاع از انتقال سوخت قاچاق به یک کشتی خارجی، مانع انتقال ۲ میلیون لیتر گازوییل به این کشتی شدند.
🔹
۶ نفر از متهمان اصلی این شبکه قاچاق دستگیر و به مراجع قضایی تحویل داده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/459051" target="_blank">📅 20:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459044">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-VIY1_dZGXnHSsLnaIlwZFRGS2wi25mjkUx74JDdgvG_rOwsowXIqBCDeSpiLH5xnehDGrom_A00wHwCbvYizdsuuDVAMZ4rNJZRxq5rud3s6N8JvNIf6maOFjLrH3-ULCYWu9oiiwvyukDP8XrwEDP46tPvzvU7NEy6AD4P4iyx0JO5qQCkBAU9qww0qM2Ze-R98-IKVYaQWaagRdBRyokUS2-Yf2NUNju6JsyYaWmsB9qBnJdyo2bXOWTVTZnOPy6_fbG4phwIuv5B9YsqmNk7zsC9TVz81WY6o5ArYYTwdQ-s7Y7cfLtrGb0VB4j3Yo5-p0cMI0P8b-FJWpz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhkA3wfDV3Gu7Opnw4vYdNCmoAu5hcv66PV10ibZ63QTsln2HxSXpExLFswTFHsBjSvYlhC_UXpSSfAIPqxLzcKGvxX_pBxEY6X2FGFbud_ZWKerhgz5I5wG3o9s6jsTKqkTUdZA20v3KueMO5Ta_ptJC_cm7ZEf9H1GC5Q0VdF1-ELRTMZRjhEGCVlt6ppgPAgPOZTyCyqaR92H3viwpaGNzorRjB4dUhneC0RZYf20VUNOhYDfmKjxwBuu7CZJL-DGzRDYtwwzW3sc8lStbHENAroLasAjSzyY0UCYqMSLZc04aSkZfRsnc0I0NOzeHxqPTI5ib8pGn9Uk7SrMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhlUA-QHZJZa-EgjxawXANWPuI3E7Ru2TXQXB4ANJ8p4RXLccpEVBVxK9voRlmjn2oY-DObgorg49zMac82AQbgy-Is0SAzkvFQ8m3C8yPLpEgIC_V1cmEVP1y6pikcLNvDjGP7pKdeMrFm6EjB50U1G1uacJ16rnGA43HaZVX7jSDzTwf_rry9ZnYF5nL5tG2GRXfs0T4OKs1BpovjCU88H-kyWlf81w5j2o4pPvmTOhw_4eiZTIG1cOs4ryZE3U-yE1B-nPdLwWexookzKrihajTildqQ344VmsGa9y8V-5fyssNFXyHJWDfbjuElAOO5Ng_3L3X5WI4o3fYbtYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfuW4EDIthkqH_R5qtJa2BjSPiHiBqlmctfHzVwsbJp76oQ4YTGMKFS5KWlGlbppxrTovqqaO7bTRkJBXGCNH55KQCR6JxlI3Ram6S7aw5q_XxKEL4Jg5CjHdfZh2f9AREzyj7isM2zuIvoP_AFDN_DP5gnrL3u3wmdeknYXJZpwlAeun_Z6aiHk7BX01-ZnARnVpA0W4UI2zueasiQlU9zQulp-VciRv-KyL4P7fdoqffS-mC2m0KRCE3-W7wrW_VrFdesJvTbFbjbRz91kOCRIkg_W-Z1wIav9ihW3Hww2aiJa5jN08RUhvViw0RXVye8EeSmkKg2EMYj8KVMv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGx23ZC2xjwu7g2bFdlrx9QWDkEVL4Wod-dP6zM-lgaC2ucqsyKIPL3jfOgK6uWxtUcFEVuOZ2rMr0EnRhRdJLda-WhcWKOLczxdWOVOtTcoQ5pLAEMsQXUN-e1y-pyAvP-95kD_Z383wC5FONyp_qnJFsfyOzWItz0HZwumhbFQFJcPzhD3R8TcmZGp_MBfaNyE-bu48BWFxMPn8bUSb3FQF0q9prfOZyia3uEobv_54oxCen9zENWilg_9RSUdv34pFve5m7yGLfCRLv9z9ZkHuO6n6cusHpdQwNbWAslryqDiFjbj5KxSiHWgCpKLDrZY98uH0pDBAJXp648ziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YiGMJOo32Ibwgs1RzoMq2Ivn_R5wt3SWi1t5PPHEfJB8cf2ddCU0aaq3hVufjTVR-IZwHjZnVXX_cKP1dji03WNHqFED4KRqaxmUysntQlh3XqoIFBz_KItbS_4b8IWv_U-UvqW_m46kWlViXuewVy_cf_kEuo-us3jn7KHHzmTSO7oL6Bl4xB5zrJoJZqniGI1Ha7XOsxrOfpb7Q9jiukq6v49rAPKdO9Pycz8tvWU1tKyPJUeWSjhfcGK89xADECLbY61ha0ErsyzaZJNwu6usRV-vd1Z493Mb5rskr-myLh31URjyWoBqd_nkvhwGM4QdpbDShhH8eyQJlxMvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qep7qANuwV22l-H_M68CiZRw4JT6fSHWhgqXae12HvCjCfn0T2cLEf9mgpvZgiLHc5aiF_b9Em8QrVEikzffkWnvM0G-eBu3lMWEF7siKGamKuIxs5gyyDAsJ0lqu8liYsnzHiJYd9xYJKdqfgDo-hiAcxLyPNk3lrktd9d7SUrt2OvvcLKDqn13XMotLgMJUT2WE1a2qePUdtaJ5YN7nuEoLNdhnfzqBz0Mb7zTqZqAhCTxpzOTKgMOLO_8c3kkut-asapYM34-LGYdmtWILhdk3bc4NDh_5I88xMf-aIhDHTLXHx-7QPzbcF8IUjaCi6wScrkqzoWCtZKTIXohPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن امت احمد(ص) در کرمانشاه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459044" target="_blank">📅 20:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459043">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b2524a388.mp4?token=UH6TO3kNVTsKy9wDCDZa3_jOG4lOHdYxZ3Jbl_v9BXDO0gekDXylLm4DCqaLt3khf419K1Esl-MXeE38Z7KyVRGRys3DGR-BVFZz7zd44f1Y5iz4P5iRQGWKKjMYgmnwIj3GGkAph2KQnCyMfzFxsa9MFJoX4Uj6ahrXskOJX0zOF8bBS0WWlV_ykc0sEvJrhCrIbfEAKeBi9kB3oQq6M7hZASbwlk62QSAZbM8u90IYvG0na3-rw8JvO6wBjj7OumkNFLXt_EvJWH-Avi5TrSgNSY_nPkfMZFscMVWe7i6Ydl2MQsQHSCZqXujZobj4sQRs7NIwJcW6uN5O7EXa2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b2524a388.mp4?token=UH6TO3kNVTsKy9wDCDZa3_jOG4lOHdYxZ3Jbl_v9BXDO0gekDXylLm4DCqaLt3khf419K1Esl-MXeE38Z7KyVRGRys3DGR-BVFZz7zd44f1Y5iz4P5iRQGWKKjMYgmnwIj3GGkAph2KQnCyMfzFxsa9MFJoX4Uj6ahrXskOJX0zOF8bBS0WWlV_ykc0sEvJrhCrIbfEAKeBi9kB3oQq6M7hZASbwlk62QSAZbM8u90IYvG0na3-rw8JvO6wBjj7OumkNFLXt_EvJWH-Avi5TrSgNSY_nPkfMZFscMVWe7i6Ydl2MQsQHSCZqXujZobj4sQRs7NIwJcW6uN5O7EXa2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت پخش فرآورده‌های نفتی: دوگانه‌سوز سازی خودروها در دو سال اخیر  ۴۶ درصد افزایش یافته است
.
@Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/459043" target="_blank">📅 20:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459042">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bfa5919a.mp4?token=tc_8wZyOysQOM76PXuNq_IJjp24xt4TXNXw48c-z2QEbpOsFekFSyxcTtuM478EOOFB7ami2_g4D332n8jSulz1iQsEDrZm_ovY0HymiMT738j65jddK8V2sZ0FfqZbhC6onorfBL8TQdYUWQBc--ZLCrbUzSG2ZmtqUNnjWL6QxxRhn87-PCw13wfGs3sNRqoUqFvwTN8FYfaCogjSnmn3PTnnxQ5tCgBMb2L7l7ARq5E7qNYpfNIuqYAyee_EEv51fLP9xYOiIY46XsIrj20L0-xhJDw_dZaNHh614JaAbu1TwPnop5_to8cYZOqwmDYpZ7rmRJB7yn8eKjWaN5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bfa5919a.mp4?token=tc_8wZyOysQOM76PXuNq_IJjp24xt4TXNXw48c-z2QEbpOsFekFSyxcTtuM478EOOFB7ami2_g4D332n8jSulz1iQsEDrZm_ovY0HymiMT738j65jddK8V2sZ0FfqZbhC6onorfBL8TQdYUWQBc--ZLCrbUzSG2ZmtqUNnjWL6QxxRhn87-PCw13wfGs3sNRqoUqFvwTN8FYfaCogjSnmn3PTnnxQ5tCgBMb2L7l7ARq5E7qNYpfNIuqYAyee_EEv51fLP9xYOiIY46XsIrj20L0-xhJDw_dZaNHh614JaAbu1TwPnop5_to8cYZOqwmDYpZ7rmRJB7yn8eKjWaN5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون امور مجلس رئیس‌جمهور: کمترین میزان استیضاح و تغییرات کابینه در دو سال اول دولت را داشتیم  @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/459042" target="_blank">📅 20:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459041">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbXjhxWHOyluDxRc8OhyWakPwQkR-CcZcyUQmdalr1g8klL-0kCTpTo6Mkb7s7aeWVFIiUH5bizNF3ZTphfw07ob5xzqgwK2sz_izhvJHknUFcmfBbQmdX_ILvu2hv4cp0xtVN3ja7Yfe8l2fX5t3C3iAOh229NCZX1Ac4X_WPGj39Pq0T1M9DlHp0dcVQG9SofbNQS1N7PlpSgfvSVhZt2v3an8sKirWz79GwLCx1GYcjO_GLLSDbTKJ_xTO8NbxudYGD8JqAi3urbFu0bDH_bZk5F3uNKYZZ1aOaKUaK1yDOKL7k7tjjuGakX0uVq9JvjbsCdWNUACUfIWTKI_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنوانسیون خزر و زنگزور دو لبۀ قیچی علیه ایران
🔹
مدت‌هاست ترکیه و آذربایجان با چراغ سبز آمریکا، کریدور زنگزور و کریدور میانی را پیش می‌برند تا منافع ایران را از معادلات ترانزیت اوراسیا حذف کنند و با بازگشت کنوانسیون خزر به مجلس، میدان نبرد ژئوپلیتیک و تجاری امروز در دریای کاسپین است.
🔹
دولت چهاردهم در شرایطی پرونده رژیم حقوقی دریای خزر (کنوانسیون 2018 آکتائو) را به مجلس فرستاده که نقشه کریدوری منطقه دستخوش تحولاتی اساسی شده و رقابت هر روز شدت می‌گیرد.
🔹
پروژه‌هایی مانند کریدور میانی (ترانس‌خزر) و کریدور موسوم به زنگزور که با حمایت ترکیه و جمهوری آذربایجان و با چراغ سبز ایالات متحده  با عنوان کریدور TRIPP دنبال می‌شوند، در تلاش هستند شبکه‌ای از مسیرهای حمل‌ونقل را شکل دهند که از شمال و شمال‌غرب ایران عبور نمی‌کند و عملا ایران را دور می‌زنند.
🔹
نتیجه این تحولات، شکل‌گیری کریدورهایی است که ایران را از کریدورهای شرق-غرب حذف می‌کند. این مسئله فقط کاهش درآمدهای ترانزیتی نیست؛ بلکه تضعیف جایگاه ژئوپلیتیکی ایران به عنوان پل ارتباطی بین شرق و غرب است.
🔹
تصمیم‌گیری درباره کنوانسیون خزر، یک انتخاب صرفاً حقوقی نیست؛ بلکه یک تصمیم ژئوپلیتیک است که می‌تواند آینده ۱۰۰ساله ایران را در منطقه رقم بزند.
🔹
در چنین شرایطی، دریای کاسپین به کانون معادلات تبدیل شده است. سؤال اساسی این است که آیا صرف تعیین چارچوب حقوقی، بدون تضمین سهم ایران از اقتصاد و ترانزیت خزر، کافی است؟
🔗
پاسخ این سوال کلیدی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/459041" target="_blank">📅 20:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459040">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4949575f84.mp4?token=fMFpYgcDlyMILV1e-XGs5J8uZPXeKI_cX3uFQ3oXerl57RCEOleCsJNNWRTNQHgaHPrNpFRi25LgrjHORHrr8OPrH0O_maCIISUxm57Nsj6KsOF9zTk1DPN1Z8KnOzcKKKacHnctW3HvsFB0W7PslQQITp23PtL0vwGIEGVp_OJAkRiSIwsmEjGlH41GB2A0Omai0kREruSKN-l0Jp1Mod_aEqa0KbyEDBPa_HWxoLNFD8De_VbMMjdD-QfdL2K35A4VP-WW-FSC2jUlcnBB0_3sSoYVdaVXJt9K1AkibKbL0G8642ZhThDv5v4_mL8Chvez1b54eA0VTPRtFR8m3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4949575f84.mp4?token=fMFpYgcDlyMILV1e-XGs5J8uZPXeKI_cX3uFQ3oXerl57RCEOleCsJNNWRTNQHgaHPrNpFRi25LgrjHORHrr8OPrH0O_maCIISUxm57Nsj6KsOF9zTk1DPN1Z8KnOzcKKKacHnctW3HvsFB0W7PslQQITp23PtL0vwGIEGVp_OJAkRiSIwsmEjGlH41GB2A0Omai0kREruSKN-l0Jp1Mod_aEqa0KbyEDBPa_HWxoLNFD8De_VbMMjdD-QfdL2K35A4VP-WW-FSC2jUlcnBB0_3sSoYVdaVXJt9K1AkibKbL0G8642ZhThDv5v4_mL8Chvez1b54eA0VTPRtFR8m3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امکان ضربۀ مستقیم به اقتصاد آمریکا و لزوم دریافت غرامت از کشورهایی که مبدأ حمله به ایران بودند از زبان کارشناس مسائل منطقه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/459040" target="_blank">📅 20:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459039">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n511R92lz99A6f7W8kQ5_ABIZlbAQ0zvBI6d5eOyP-z-vp4FS7FiI_NNR7F8DIEVuORazTQPhDFQXfYWz8hQe9saa9SxRtNQqup4NW8PSevN-OdPaoXTWhquHln9UuHS88ZAUF3UTPDHD1Ptfn3uCpzv4YDKQ8YlZUMwSXg82u02wfzBM4FC7SdTp4jupS1YHGLPm08gX_WYUnqQP_ANn1bI0ovSBO6WyHFP9b8RRnjyxahmDdbGbLDHRbpHUcn3HrAzfLkdYuGRTmFiTwzUIshClD-N6wHpBSxDTdksoxRZ_v64fHXsl_eih_jGSdg_k5TQlOr18fi2huazVgslRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت دبیرکل سازمان بدر از بیانیۀ گروه‌های مقاومت عراق
🔹
هادی العامری: گروه‎های مقاومت به شرط تحقق حاکمیت کامل ملی به سازماندهی سلاح در دست دولت باور دارند.
🔸
کتائب سیدالشهداء عراق امروز در بیانیه‌ای شروط ۱۰ گانه‌ای برای انحصار سلاح در دست دولت این کشور اعلام…</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/459039" target="_blank">📅 20:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459034">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abCnoj8xgcirqXjaldW-eNILMOuxZ7Wbk7PZf8CbpcTRwE0S5lScXnoKWtpkrx_ZC1_tpPEzkMa5pQg6BC7MZkbU_YSejHYe-5S3R6mk2IXeVYx53X1PQnqZ-aclTH3FkuaDY-8LZWVqPKm2FygYWo-kFbcakFK7trTwr2BtfmtJ4PIR3fgKFfIjbq_F_UvufJJm0h6BQ_Ca6ENM2KGFXSxqK9RCUOFknQypgCIcymT6crYBWZoWsEUAgViDiqwIxaKCom7NKsgk_QfkovwH6dZ8LFQ-IMI6TAx5DTCdy-eJ1BUe4147q5tt3PK8JI9D7lFLPtJYFUwnsLy0wy8fLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzU0YoSwQc6CNGX1xjs0iJvj7UN6AUeRIzrIq9iC9E2NI3XSwf8X0HmHSbn70OettabWBoeZiV8XvMPAr6lEFYI_46JztPvx3yPA-zxZ-nnxLh01torfzOtYCaBembogdTjP7iNgZUEHBfHRFEYyHp731HKYc5cp_Dp9WL2QpT8Quaicx1I8irHjwnailgWl0UM1-uN8b_gHcshH72JYf8_l5qgy-HgH_bBGB_mh0jy0PwnM_BwvJNKeELYjBe7NxhcdSzCDHvace3FL15pqy-iIPEW0cXqgAPr-_rf1kz946YOjyjCCo_yw5Sm2SNiii5WxgwWJnMOhp7s5VPaQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIhnJ0BGsLY_jSfDQGK8K4VxXpy-U6GbMkeoWmWcpPT2Z32BfH_t3fn1IAtiNlCMseCiwDWEwzhDwJ9lzSLm4HfPVeQ7gO7_Ucj7Wk3UIn-JRwGgkyCuRrcz62vn7pngXVyXaGX91KJlLbkQZ3U6YzC7lCNTcd2wRrycaPjCdHUssjKbVo_Zcch2VF6PNWFtbRGMAUvkk9Nhi2DdJMUZsW4EYqg56x6JKP4YE6J9NnFdeB6BhrpeBWO2sA_UJc25fEk5apDLgcmyeY-zoU9mVg73szgV0ljpH5N7ZcGwbt5e_UrbyduSpraENPuFqI0QmxgQ8S5z3dpnONOhsBwt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kg8RR5A9U3_34P3X9Kf1JvtiRGJziVz0eDLJYWv8ehqhQwKe14LGI6L0vo_5GUKfEze87R5LAjXv2HoqZfSQPOItH0kE3Yj0ZdQan_aBsbfCM_vHczxlxN4dWYTQcLbw8vVap_PzZ4DFOEZ6SReudCRnA-aONP4Sj6QxqLYAaJGYfJdZr1rIFc1vaVKA4Gmz_K89bV7v-Do-tQvlAbFaQ7NDRNAKzXDv--qNj8cjb-MzJO_vgqIMsT4VX4y3AS4Ebc0vJo8AkXZEPshaJRPzuiiEaxeUmbpLQ5pg3fkb5yl_5r8Ph-07PgsJ78nt4CvtK7cRLhpiLEg06y6KvNM43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIlUDj0g5eEdbq0QO_eXCgXhP0oKECzIPdk51Ls1lp7oBZOydrLNN2aRNY5kxkpmLyn5tyS1eXHcS1qKkiSZ0ZobovZMIVsn9kAuA8awm6lZqGCxXGrHwOQ5zmEUnnoTYs8iQOhg2qkKlle03ub7QclK1BMNoqyumoUMznGLcE7mjvr6dt1XGBulELLPyhqBMWJjiV7gvzWWIZeSbZwMR5jTWBNh-GHeFMCx29Fmpq4PI7VVOpVF48sdxT93-hQnqpSVwJABsuKdGRGNplYmukpo6fFnvp3rIG_RfqeAaUACKIIze2Fxxjy11rZwgWoLeDxoZpn6IKgMkV75bghFFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن امت احمد(ص) در بندرعباس
عکس :
عماد یگانه دوست
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/459034" target="_blank">📅 20:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459033">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzYdhl2OCnUsy900F70SymzfAa2CrxEi5fYiNwUhdzTDwQh8DrM76f0DD_PqU9xn7JugfQnC84i8miH-57ytCSM1LZJvIs4pbVoKXIYLx7JHfCLX9tI6B6rgARGRaHQLHqoHLQHMKNNCoy_vZ98GqyX5YWc-Gm0Jr7zFWiqPqVdH61BfY7Ap6opvwB8Nigyqis3QLbyRPqQIs9t05-FteyFOhpySopGMNr1WDx4vi0rkK-3j0vbpeepZ74oAP3lqIxcuc3KQqP4TYA3tj2jW135uD3UM5tI3LQX4jeSeziPKnIvXAjUkJlCmYYHT8aKm6ejrhAkHT9nc-eRCiklq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرارگرفتن یک نفتکش در نزدیکی عمان
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش روز گذشته هنگام عبور از تنگۀ هرمز در فاصله ۱۲ مایلی بندر الخصب عمان مورد اصابت شیئی نامشخص قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/459033" target="_blank">📅 20:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459032">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc097c7ed4.mp4?token=IAAFjKeucG8d8KEKZSdkQQ0QPnH5hLqkkM3ZNlMc1ZZwD_LQL_Ghbci_G97yvPbS2E2Qrf_MPmcODjwEpPsHsM1F3BjxSMiyd-4IGjM9UCD2l6BX4GYxbdkC5B_NxM6zo8IW0EWUfrL2Qpma_YzuXS6c3lN_1DhvQl7sPEnt3uE6VhnHPuqOxuaBx1pB9V9lfxFqSi3YlGY4ur8-dpHyeH2acl_AYMLXnb9wSqvHzKaMs48CKzNEvfa8XQFE_p5nBLSJhCsKGJ6EpotYiT6eBaq89UAMJuI93_V1abG7FhUBPnre2-aOSUwhCyTBBJTF0ar1xZ79a1d6ft0R9SQ_Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc097c7ed4.mp4?token=IAAFjKeucG8d8KEKZSdkQQ0QPnH5hLqkkM3ZNlMc1ZZwD_LQL_Ghbci_G97yvPbS2E2Qrf_MPmcODjwEpPsHsM1F3BjxSMiyd-4IGjM9UCD2l6BX4GYxbdkC5B_NxM6zo8IW0EWUfrL2Qpma_YzuXS6c3lN_1DhvQl7sPEnt3uE6VhnHPuqOxuaBx1pB9V9lfxFqSi3YlGY4ur8-dpHyeH2acl_AYMLXnb9wSqvHzKaMs48CKzNEvfa8XQFE_p5nBLSJhCsKGJ6EpotYiT6eBaq89UAMJuI93_V1abG7FhUBPnre2-aOSUwhCyTBBJTF0ar1xZ79a1d6ft0R9SQ_Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون امور مجلس رئیس‌جمهور: کمترین میزان استیضاح و تغییرات کابینه در دو سال اول دولت را داشتیم
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/459032" target="_blank">📅 19:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459031">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d4388b5a.mp4?token=sKlNuUjAYRnHEuDwqvxk4qZ0jvBhxqdatU0G-hZkjUU4QO6pKQPfoANHy0RJFsPtSC3oXZobGz2mK9XM1UH3zx2qv5skudsZJgZyNn6ybxztkmqRQ2I3Kz59tO6wPCoVIenktvjbHGb_C5IfIO5B-l6sIBp9JlsLiZgEee_bGA7mBrjypGogmGu6CRnO9J9Nlh7FcbYR2jFKpijQSKNgWT_BHQdlpSXXBnhTTChlENun3A_7Kyv7qZNxk42xOMtWwvHjIZc-hjskdnWhEp4wRhA9fP7z8bJN6ImQ1Sltt5mfYb6oauWupEzqROAc-REa9Dom1cchD_A-6aDLXgaBUhohGbQITg9p7EaRAux6PCla5E-wwZlEVnnl8oFIJxotzztiKXcYL0MyS3l-qSxHMjfYQzo6qihrh0Bm82t0dS4I1MVDGhLmDhXVaDkjl3YtpjsOyTZHiTdNrjCj58f2bZvWHPnG3G2cAlHmpnNSeUs1dw9Ee3AgZ7LmoqsDEPKIBQYYExrFpkoSJ-rWsHk61v4gWP4Va4jbo9vjmv7lWVmxNT6KbVZ4yhHne_6sBebSQFVG7hcPqvzL5Y3cxshDxQVjI7UQLd2f02Tr9NtxL8XJwcLSgvRjl_LLe5Kfavw3JjoK5OuZVPov0f-AJrnS_J53HO4B9u44bckHqc6yJoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d4388b5a.mp4?token=sKlNuUjAYRnHEuDwqvxk4qZ0jvBhxqdatU0G-hZkjUU4QO6pKQPfoANHy0RJFsPtSC3oXZobGz2mK9XM1UH3zx2qv5skudsZJgZyNn6ybxztkmqRQ2I3Kz59tO6wPCoVIenktvjbHGb_C5IfIO5B-l6sIBp9JlsLiZgEee_bGA7mBrjypGogmGu6CRnO9J9Nlh7FcbYR2jFKpijQSKNgWT_BHQdlpSXXBnhTTChlENun3A_7Kyv7qZNxk42xOMtWwvHjIZc-hjskdnWhEp4wRhA9fP7z8bJN6ImQ1Sltt5mfYb6oauWupEzqROAc-REa9Dom1cchD_A-6aDLXgaBUhohGbQITg9p7EaRAux6PCla5E-wwZlEVnnl8oFIJxotzztiKXcYL0MyS3l-qSxHMjfYQzo6qihrh0Bm82t0dS4I1MVDGhLmDhXVaDkjl3YtpjsOyTZHiTdNrjCj58f2bZvWHPnG3G2cAlHmpnNSeUs1dw9Ee3AgZ7LmoqsDEPKIBQYYExrFpkoSJ-rWsHk61v4gWP4Va4jbo9vjmv7lWVmxNT6KbVZ4yhHne_6sBebSQFVG7hcPqvzL5Y3cxshDxQVjI7UQLd2f02Tr9NtxL8XJwcLSgvRjl_LLe5Kfavw3JjoK5OuZVPov0f-AJrnS_J53HO4B9u44bckHqc6yJoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حضور پرشور مردم در جشن امت احمد در تهران  @Farsns - Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/459031" target="_blank">📅 19:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459030">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
تصاویر جدیدی از عملیات پهپادی یمنی‌ها علیه مزدوران سعودی  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/459030" target="_blank">📅 19:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459029">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l66lvSja2zbHDxwpdr5mMIU33TNLlG4GtXmjeXf95yUFs9iLEJ8KwwZ08nSnu5gsGpWWAGHfcJmo_Xi5ISye3nzQMWj5UvHFO5EVLQ0iLraDeX8bgIYz5UlzlirOW_Ma-b0JwGol4zunWt-vcs-IJYAwq2vUchM1C8azDy-qmmWRUwTrWpIB--ElYhcXcxfLKXW9lfE1-SJe8XvVaH8oYwsQta28Cdo0p8ocJElQAAOUhkWmfSEP73yqlTeupkdx7ttUgmB1GXCh4HMLfXOqAxZ91eaxE4YL4IlQLeWsqn42E1RwxWddJL__T2JSf5Gie675Il55oqfJjYScHjL4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار ناشی از عملیات ارتش صهیونیستی در یحمر الشقیف در جنوب لبنان
🔹
منابع لبنانی همچنین از حملات توپخانه‌ای ارتش اشغالگر اسرائیل به شهرها و روستاهای المنصوری و صربین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/459029" target="_blank">📅 19:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459028">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2658b97b.mp4?token=EBflCjW5-IEXxeZTI7KgHB9EbLJX8k70a37ABTQxnGOYZ7QezAw6glgf6_FvNCVdbX_1-IMQorYj--Pi28bk6KAM1EQ7x4VlEGS_eK5QNGerX6SGcR35CAO_S3Fd49cF5_8ZgXU4fgAIVLGo18P0D290kCRM9Vk71jYOzunktmqm_wbPsofFBN2ALtCF6m4eXf2pbUxg2H-WAYKGQjQ6LbOggG5XyjKt6GHqvZf4wfT_VU8YQ-ktJIwMpXlD8rQSWvpRLhr0ClPfHJWBwwEih8K9WnYT8IrExBc_Y3SJyLuegM3HX1_A4FJw4OWuMy7cGPyzF-J1iTvzZQwxZeUCkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2658b97b.mp4?token=EBflCjW5-IEXxeZTI7KgHB9EbLJX8k70a37ABTQxnGOYZ7QezAw6glgf6_FvNCVdbX_1-IMQorYj--Pi28bk6KAM1EQ7x4VlEGS_eK5QNGerX6SGcR35CAO_S3Fd49cF5_8ZgXU4fgAIVLGo18P0D290kCRM9Vk71jYOzunktmqm_wbPsofFBN2ALtCF6m4eXf2pbUxg2H-WAYKGQjQ6LbOggG5XyjKt6GHqvZf4wfT_VU8YQ-ktJIwMpXlD8rQSWvpRLhr0ClPfHJWBwwEih8K9WnYT8IrExBc_Y3SJyLuegM3HX1_A4FJw4OWuMy7cGPyzF-J1iTvzZQwxZeUCkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان در مرز پرویزخان
🔹
وزش باد شدید در محدوده مرز پرویزخان بدون هیچ‌گونه خسارت جانی یا مالی به پایان رسید و روند فعالیت‌های پایانه مرزی طبق روال عادی ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/459028" target="_blank">📅 19:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459027">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p96Xe0J_dMH6FO277BCi0lKmjlTmgCqseTLuvbK5oXTQ0j6vofkZkHi7alMrNSEFhbdIWmaGEkqGx34u8S6SBwWeEEVF4gXo8nKnzaXQJHo6i-JOpJhxNRreQCxCsskulrVOGheTQh4psYyA6yLmqnx3SKCHoii25lCYtmCmY__h3yyWCFDIEwpt9y7X1wthEFbgRSMyJS1WUDMjHyN3qVmO1t_kiiJ3vImkvadh8wUCDFjKRlhpdEDNLqYo7yRwLYYvmHXcCPxDqzS4vwu-dWWacWg9KpCo-zxz8zXlHvgiFPxI8IgcDc7gZsstPrS-cGGzqtw6BvW2FXDiaoSl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر لبنان باز هم به حرف‌درمانی در برابر تجاوزات اسرائیل بسنده کرد
🔹
نواف سلام: مسئولیت ما این است که به تجاوزات و اشغال پایان دهیم، مردم جنوب را به روستاهایشان بازگردانیم و حاکمیت دولت را برقرار کنیم.
🔸
نواف سلام درحالی مدعی تلاش برای پایان جنگ در جنوب لبنان شده که ارتش اشغالگر طی مدت مذاکرات مستقیم با دولت لبنان همچنان در حال تخریب منازل مسکونی در مناطق اشغالی جنوب است و عملیات ترور و تجاوزات اشغالگران صهیونی طی پانزده ماه پس‌از آتش‌بس پیشین ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/459027" target="_blank">📅 19:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459026">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f0e714a8.mp4?token=rxWErPLD1D3OMnMQjEf9Il59gwwRRZJWmJfxTXyHUBmdCxtXiaBd6iseksU4EYSWK-iRKUCYtSFDRzLHF0ZG3BAgAMZ3q-bWyYrAg-TWRNM-PImiLWPZuQe1ckrToj1cm68h-bXGqo23IPwnGXl6_uAjuciz7zUDL44YYszUNfjym1DLx7OUowB4lhGqWSM_2xo6tBs_tz4Cv0j-h9NFcZ93tx0GTOBDhcdfZxfVAIYeV2qO1ydTjHx8GAsDU80lyo2xK4-hqhmewAXs-LlgtHXjW_G_UGWUaCOotBGPwHP6uUhQwZr4gK9P0eMzDTRfKxbDgcmD5EhECBzF9cqbQqsGWEd05hT-dIxdUBIzES_FBQ7oCUCfY4kqrj3HIjXNr45W3wUXOq5g8jpm-4lbDvhycspW7HZKWiFrUO7Al1TZuBcv_HVpTLD45n_3Is2fJ1Gj7VPCj7-gW7ho8GA6b7-2r6RA2svKiuLJVCcOEECoubenanFYH2pJbgAwOcc9UtvsAoZylibLeerO3U5UoT-ez8irfVP_6B0nW_3PEeYzkWMW_Q5-8y6s2XsT1H2kGK2Xn0U1xlJ2EHmIQX47TpQDt67yVYdjQxPYnoMIJZwULTY_ZOoWnlDAGCY-s6Zd3daHbVagZeXWtyF7zI5TY2-z-UkYmWKuZoai-N9wj10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f0e714a8.mp4?token=rxWErPLD1D3OMnMQjEf9Il59gwwRRZJWmJfxTXyHUBmdCxtXiaBd6iseksU4EYSWK-iRKUCYtSFDRzLHF0ZG3BAgAMZ3q-bWyYrAg-TWRNM-PImiLWPZuQe1ckrToj1cm68h-bXGqo23IPwnGXl6_uAjuciz7zUDL44YYszUNfjym1DLx7OUowB4lhGqWSM_2xo6tBs_tz4Cv0j-h9NFcZ93tx0GTOBDhcdfZxfVAIYeV2qO1ydTjHx8GAsDU80lyo2xK4-hqhmewAXs-LlgtHXjW_G_UGWUaCOotBGPwHP6uUhQwZr4gK9P0eMzDTRfKxbDgcmD5EhECBzF9cqbQqsGWEd05hT-dIxdUBIzES_FBQ7oCUCfY4kqrj3HIjXNr45W3wUXOq5g8jpm-4lbDvhycspW7HZKWiFrUO7Al1TZuBcv_HVpTLD45n_3Is2fJ1Gj7VPCj7-gW7ho8GA6b7-2r6RA2svKiuLJVCcOEECoubenanFYH2pJbgAwOcc9UtvsAoZylibLeerO3U5UoT-ez8irfVP_6B0nW_3PEeYzkWMW_Q5-8y6s2XsT1H2kGK2Xn0U1xlJ2EHmIQX47TpQDt67yVYdjQxPYnoMIJZwULTY_ZOoWnlDAGCY-s6Zd3daHbVagZeXWtyF7zI5TY2-z-UkYmWKuZoai-N9wj10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی صنعت آب کشور: میانگین بارندگی کشور به حد نرمال رسیده است
🔹
بااین‌وجود یک سوم کشور و به‌ویژه تهران دچار کم‌آبی است و به مدیریت مصرف آب نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/459026" target="_blank">📅 19:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459025">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07481a4b03.mp4?token=Dkggb_6GnoYb7rfhEk3ZopGuP0_Sycc0t9RATlRX7EWUCwS9CB-IbAPWp8WlPZjIMQ28VT2HuRYtsHy2nlis3EVuoiNHtIT1pfhAIMpax07BAoWwkEt0u-Pc2Pa6m2CDLIIUbCMy_jbPQO2hh-VYlxblAsDIWe6o6W7nSSj1RjsV8ENcyNje-wVCU2ZRQnh9uKRoZQ2D7BIBG1WAO0GZuKjxpw4_ZvLcajrCtv4By4KLQ8eIiVMMyci7XeWwGXnQeLXkL8as_sq8QFl566yZw4nKDXMXJ3DilaO94o_-PFXPzMHimzGQ2De1VTmnGFCI9MPv9fPOUrwBoET7cHyOAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07481a4b03.mp4?token=Dkggb_6GnoYb7rfhEk3ZopGuP0_Sycc0t9RATlRX7EWUCwS9CB-IbAPWp8WlPZjIMQ28VT2HuRYtsHy2nlis3EVuoiNHtIT1pfhAIMpax07BAoWwkEt0u-Pc2Pa6m2CDLIIUbCMy_jbPQO2hh-VYlxblAsDIWe6o6W7nSSj1RjsV8ENcyNje-wVCU2ZRQnh9uKRoZQ2D7BIBG1WAO0GZuKjxpw4_ZvLcajrCtv4By4KLQ8eIiVMMyci7XeWwGXnQeLXkL8as_sq8QFl566yZw4nKDXMXJ3DilaO94o_-PFXPzMHimzGQ2De1VTmnGFCI9MPv9fPOUrwBoET7cHyOAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن بزرگ امت احمد فردا در تهران برگزار می‌شود
🔹
این مراسم از ساعت ۱۶ تا ۲۰ و در مسیر میدان هفت‌تیر تا میدان ولی‌عصر(عج) برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/459025" target="_blank">📅 18:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459024">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-f6LIeyFQO68xTljPyiITXvcY-4XwQX9LBMpDH2c31waJb70lFoiLAx7oXpPe_LxTTUPHzJ1eP0D-GdeTz6Z4cBOU1vjDdWLD2c4HaF8AJDZaKyzuKdeZ7zl-QNoe6E1ItKQk01zudwpelGsKeHmh_IVFp7u2z40rPc5OLQyW-RpPIrS8vm6VldWdTe2LOITC_7GCpuScxK1Jo2pEKcdQdUiyNX_Ge9C3-oacMLbHM_l1DnOgmLaEjFh0JoUnj7LK1Cf8kUPOwuI6ydWkjFYbZfWmqEtv_zjAfAChXHbEfGariWQN-tur-kh_jH_WZC2wxP5kkbrIDCnYuiVErjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: نفت ونزوئلا ذخایر استراتژیک آمریکا را پر می‌کند
🔹
رئیس‌جمهور آمریکا از توافقی نفتی با ونزوئلا خبر داد که بر اساس این توافق، آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه از ذخایر اثبات‌شدهٔ نفت ونزوئلا را به دست می‌گیرد.
🔹
ترامپ اعلام کرده که از…</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/459024" target="_blank">📅 18:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459023">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTucY01AbbpSeZ0szCkFAxNd0QcVMagiNc3s24MLiVj8ZTs3wh9m1VlZ8BPxs7Xwy7EFz6Kkh4ZxJVT0a8ghJmsWGj0YohYhOZ1yqlS_a_yjfX3oCQwlcVpHA4wX6mYiytPVTI_hxu47aOxyHY0tPAahbUFPN9rin4gLTHkTJQbXpzoyONdMG8Qd3EF0Sm8wpez4Q5lQJKmryCiPgvrwrn9QUHKevCHgi9-rBxqyw6r2-ISjXLPkIxVH-9z8ApkZi61v1kO2o-VvVxgLDdpE1SrIYbHCoPf8Q5QfQYjGMjuZzcuM31S-f14BaEGvQqJ93sPlhbAkBy76GXwWHEmGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام صادق(ع) مظهرِ امیدِ ایجادِ حکومتِ علوی بود
🔹
رهبر شهید انقلاب: اوضاع و احوال مساعد و نیز زمینه‌هایی که کار امام باقر علیه‌السّلام فراهم آورده بود، موجب میشد که امام صادق علیه‌السّلام مظهر همان امید صادقی باشد که شیعه سالها انتظار آن را کشیده است.
🔹
گویا هموست که باید حکومت علوی و نظام توحیدی را بازسازی کند و رستاخیز دوباره‌ی اسلامی را برپا سازد.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/459023" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459022">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjvSGKozih8MJxSA_XHTL3VsBIDr9w0oqX27zsfNMZj3CpLbPtstWwGbtoL5lftJi_gH37pKUPj8pleXJVg9RJRfSLBoa6zqd1nqAGz56PdCGR9hvRj2QKEXbP-lkN2vKAe1nvu90KYaZf6CZ0DWBgVlBUjkB-U9Oy9joVupFBw_2C_y5QcnPfnp4qpoQGMeniBC-mYBC12MyUlv1h0t0K4EdN9c2Nqtrz_mk7Bl4KTyY4vkP8MxjURqYCqQu19_fwvZBuG72GqsnlKOuXhzGmWIZDUK_u9vfjTz1CcIz7QkWo-stVy3zvkTYgnEKWVFeOII_5QQqneAzsSnPQzm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلیلی: صرفاً بازگویی ضعف‌ها راهگشا نیست؛ باید ظرفیت‌ها را به میدان آورد
🔹
امروز در یک نقطه بزنگاهی تاریخی قرار داریم و ایران، به اذعان دشمنان، یکی از چهار قدرت مؤثر جهان است. این شرایط، فرصت تاریخی برای نقش‌آفرینی ایجاد کرده است.
🔹
رهبر معظم انقلاب بر «ابتکار مستمر» و «نوآوری» تأکید کرده‌اند. ضعف‌ها وجود دارند و باید آنها را شناخت، اما ضعف با ضعف برطرف نمی‌شود. باید نقاط قوت را شناسایی کرد، برای آنها برنامه داشت و با تکیه بر همین قوت‌ها، نقاط ضعف را برطرف کرد.
🔹
صرفاً بازگویی ضعف‌ها راهگشا نیست؛ آنچه حرکت ما را به جلو می‌برد، شناخت ظرفیت‌ها، کنشگری در تراز شرایط، نقش‌آفرینی فعال، ابتکار و نوآوری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/459022" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459021">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
خبرگزاری لبنان: یک گروه پیاده‌نظام رژیم صهیونیستی به سمت رودخانه زوطر غربی پیشروی و چند نقطه را منفجر کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/459021" target="_blank">📅 18:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459020">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auEJSO-gc4qsks9Uo1SACI9YBY0Zy60P7f5fqLdI0t1GKKDTg8SAeG_6P-4BhVcao5EgiOM-1ProV8go5CkyY2SqIed82zTaydH79HSxnBeReHBfofpRGGMIXPr5mckwPxfqLFtzx2VXg4KG9cI4yh5p_MZzYPR5uSDSo0HFiQ2dTgtEA5NrQvjYO71Z0LdZw2FerLhXTqvjELXC9oyZC5pgMY_KLrokoq79Mio9ME9Z6yH7YH-QzbVtvPXHcTSWdiL1hAvKLErEDG8m0FpSlBYqmykj-OzdevFLyOCfaTfErUDgpQ2Q4z0Wk5Tg-iaeXQuefuqYi4_v7jR6lMvS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بلوف ونزوئلایی زد
🔹
بزرگ‌ترین کسری عرضۀ نفت در تاریخ به‌واسطۀ بسته‌شدن تنگۀ هرمز رقم خورده، قیمت سوخت در آمریکا درحال رکوردشکنی است. نظرسنجی‌های آمریکایی هم از احتمال شکست جمهوری‌خواهان در انتخابات میان‌دوره‌ای خبر می‌دهند.
🔹
در این میان، ترامپ این‌بار…</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/459020" target="_blank">📅 18:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459019">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01c72e934.mp4?token=khkXmicspkJPgpG11MzCbMVxJTWwi19k_E90TbQpUxK2nyL-GdoiWJ9m9Y9P1Lioe4WS0F3OblIYFOeRVeVwJl2fY1xcTW-bbAh2oajy3NcLwnhSD8r6zyCbYmd9wn1MCKsP9QpMjcITDD90Qjf9WGoFYx6esr4GbYYFQ6xXW68chqWB3I911SPdI39LjxyMvhS6HI_n_QcGB3sUsHcUbG4B66NPo4Pa1pPxBFKSQsf6GMlPpv_kWM0xJ_BRBreyxf7WiTjLaOO-QpQV0uNVRYVcvfjHj5v1opqWXSeQu-Df1mskjID6l9Dxlz6UYmPX3e5dagFQRUfEGZGxjS1j0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01c72e934.mp4?token=khkXmicspkJPgpG11MzCbMVxJTWwi19k_E90TbQpUxK2nyL-GdoiWJ9m9Y9P1Lioe4WS0F3OblIYFOeRVeVwJl2fY1xcTW-bbAh2oajy3NcLwnhSD8r6zyCbYmd9wn1MCKsP9QpMjcITDD90Qjf9WGoFYx6esr4GbYYFQ6xXW68chqWB3I911SPdI39LjxyMvhS6HI_n_QcGB3sUsHcUbG4B66NPo4Pa1pPxBFKSQsf6GMlPpv_kWM0xJ_BRBreyxf7WiTjLaOO-QpQV0uNVRYVcvfjHj5v1opqWXSeQu-Df1mskjID6l9Dxlz6UYmPX3e5dagFQRUfEGZGxjS1j0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعویض گلدان‌های ضریح مطهر امام رضا(ع) در روز
میلاد رسول خاتم(ص) و امام صادق(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/459019" target="_blank">📅 18:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459018">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1267e25395.mp4?token=mrMErveUGs4ukhcFTnLL_Px6Z2924XIkLVqi6uYRBXJ3dA1t3Zu3kDrnxj6F-V4Ui-HIMOFNi2XBM1jo6HC205L4V_sKVqsnQqIebgjM4Bj8muVqNruq-mhFHYIwxSD1SWblNsRTRn1Fa1HaIZFRTFQe8MJVN7MqaPF1qGMhRjHNurfBWsrSN10OKwNfmuH6WfEBe-PqXpW0SS9AO_1B89YmH1iZXwVRW_54qwDoPxYzxTy4dNOFU5r5JcEi4urlCciHJBjlh7PfAJFH8UwRUFZngkI-tSYxf3nuybBRkdplOwIV2rYyVGYQnX-LsBpKPMJGA2oz_R3a50L50XWm1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1267e25395.mp4?token=mrMErveUGs4ukhcFTnLL_Px6Z2924XIkLVqi6uYRBXJ3dA1t3Zu3kDrnxj6F-V4Ui-HIMOFNi2XBM1jo6HC205L4V_sKVqsnQqIebgjM4Bj8muVqNruq-mhFHYIwxSD1SWblNsRTRn1Fa1HaIZFRTFQe8MJVN7MqaPF1qGMhRjHNurfBWsrSN10OKwNfmuH6WfEBe-PqXpW0SS9AO_1B89YmH1iZXwVRW_54qwDoPxYzxTy4dNOFU5r5JcEi4urlCciHJBjlh7PfAJFH8UwRUFZngkI-tSYxf3nuybBRkdplOwIV2rYyVGYQnX-LsBpKPMJGA2oz_R3a50L50XWm1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وبسایت آمریکایی: حجم نابودی پایگاه‌ آمریکا در بحرین باورنکردنی است
🔹
وب‌سایت آمریکایی «میلیتاری تایمز» در گزارشی به ابعاد خسارت واردشده به پایگاه پشتیبانی دریایی آمریکا در منامه بحرین پرداخت و نوشت که این حمله، یکی از مهم‌ترین مراکز نظامی واشنگتن در منطقه را به‌شدت تضعیف کرده است.
🔹
این وب‌سایت در یک گزارش تحلیلی درباره حملات روزهای نخست جنگ نوشت که هرچه اطلاعات بیشتری درباره حمله به پایگاه آمریکا در بحرین منتشر می‌شود، ابعاد واقعی خسارت واردشده به این مرکز نیز بیشتر آشکار می‌شود.
🔹
در این گزارش آمده است که گستردگی خسارت به این پایگاه احتمالا یکی از دلایلی است که مقامات آمریکایی را وادار کرد شدت آسیب را سانسور کنند.
🔹
بر اساس این گزارش، میزان خسارت واردشده به پایگاه بحرین نزدیک به ۴۰۰ میلیون دلار برآورد شده است. مقر ناوگان پنجم آمریکا، یک پادگان، چندین انبار، برج‌های ارتباطی و یک ایستگاه تأمین آب آشامیدنی از جمله بخش‌هایی هستند که در جریان حملات ایران به شدت آسیب دیده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/459018" target="_blank">📅 17:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbmMqqgKdl-mUNwQx4BXrBobKfrcNrCbZi__RgWIEMexLB6jFYy0S1fNDh8BbVCF-Ziuq32woI_hdynUEABmhhOmK1QVc-Rqcb9fjh0Jd2i-TExJD2BnxapsSUxu-f93oxqk6WI9h9xjU0A0To1sqbBnOtKJ_5DhNdMtu1RUm89H6l0RuPrRMfSaEpL_KMmHMG_JGeFpsHUozXG7kAHa2-r_zwqoJaihAkQlHnt5kJf58Uyc3TvG7-dDKFY_MlLQ2PRv4v10AkyHTpLSBKF8Ai-bSDaaKiNQoMm_k7hVHsviwEkK-gxY1dcy5QMBM3MrO-xFr4n9crdSi0bGmnJIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vq6-pXbqFHuqba0G1avIpuLIQyAWH4Oe0lVjmbSrFyey7NlBs_e-huFYUB91HVMcx5KVFU2MddF2tAeP70cQZ_HFZSW0kQ8366oVbZOrD-onX4YEhtibHUD--HuIFN6C-kN4sWJx8fCpQsJA6kEEZARXJByxUIHobL6Gx54rEIeJGcAbAihJwg0p-BmaN0lXV-IIKApdSE23sn0tJcE0Rpoc0Q5uGcInRdRfNDg-9gbiRqDEnafIeYPW74xwJ_sGY0bpp7ZVRCZdcUadmxOjKxmSSrA1layvIvpRLcZ_nPeFkm5RB9F7t0__-vS1AXk79CJ8qz8xIfvTK2yDbl_xQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_loN-hnfcNOZ228QmOtbATsZewXFmzKHfP262xWD-viMRu4xTTBP0qppNMreNl_bm_tWgeglLEU4893ACGofg7dZ5HQrCyAaABc2MN0LiaT2iL6kV_lpzVWiPJXWrYg8KOY6ppIaK-2wOuVhhlO0oABrZTlNZm-_hVTIbEZUeNNECkNeGJK3Aq6YGDPl7tnIYA3c0wIlltLZu10Y4KzOVXFLbadzKUaDiX0__0PU7Wp-bb05kQVq-GX2scj_ZuUT8DUpm4dQnGVqpap2zhBb1quBM6BGs-3ESChdfIYCQAOtZwS6FQ71VDnWStT1ShVMFvumFeoDsShqvO0kqt8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTi7CyRQKOLFmiaVI763Jv6K9oMy5ktsXvAzUAumD-2uyW0aUOcHAiTAyhkKuF5Y5I-Nk1fO4O_K-zI9AT7zCbK4OynYVOfERI9fkzawnHEvtVy27q7TtTdk8Dp8O7UvZ8e6e-X_zeOgQS4tYjwEwtytinz1S1cPSzwSU0jXHQrFOITm1C9BBLM5mcjaEHZbP-pqx49-IElLRqc24Fj3oy9zgd3ZKrH2yLas8MBQ6nb2vCbSjp-RooKkCceOjNCr_dYk98fSD3ZvAI9-8-d8qsikBDilydGEaqa61FQPpy27tAu06dJyISHE8w6YS-BfofCpeulzTDfD4Ou6BBQn-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور جمعی از میهمانان چهلمین کنفرانس وحدت اسلامی در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/459014" target="_blank">📅 17:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d136c2b860.mp4?token=R0EgIKlJPc4coTgSeHLZaA5ZIFS5xtd6h4XRHZNdxoOvVHAPdkPVsefhD3-M2RSYpHSxZfGGjIQrxi8lgIVK4Y-Z7d_QOhZqC9Ka14b__aIpWc5CMIK2bKtb5ehNqId6j_WAJbkmR88U0PA_dlim3XomhRkJAYufJu4NcxLrnoPqoYMohiZoxc_cGKc_x8ikazN-bfe9vBTBpH0unyhxA_szK3lkY6CLlz25Kgts_YW05nWTj2L0ii1ctVm0PAVrfsL7tshREpEF9lejn6Qr5yAAN0R_CUR8NZaGJYBRuIDNvvT2DfRtsSNDhjXXF4PAYcgKWbrUn3pjQxyem43CD0hMyQoapPo8hWEIAa1vfEWSa4nawEOFoA8qkgUGqLNXfCVOa61X9XQBK-9JS2lkNYLenJC7Uxyk6s7VxwAUvM8sgjP_kgNpOtbLjv9eqFwv-8nsD-2p5ScDPDyITH9o5uKull8ZovGNp_ydg1lUYQDu1SPKXxEOQboaeBpoUnUoY7FWT7fNTThylPS_ItqZuBMzWZus69I-VOZ_rX8eQ4raZ2-35nlpDUpvhPF9ApPFVXCfYyScGoYkH5_6leMrTeN1GuIczPNywxwidj2YjFmyHBEZJZi6F__gwNijVyLMlP67CIAsETF2Il3vUSwU7vRQUxlTNiCeHTttSABqVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d136c2b860.mp4?token=R0EgIKlJPc4coTgSeHLZaA5ZIFS5xtd6h4XRHZNdxoOvVHAPdkPVsefhD3-M2RSYpHSxZfGGjIQrxi8lgIVK4Y-Z7d_QOhZqC9Ka14b__aIpWc5CMIK2bKtb5ehNqId6j_WAJbkmR88U0PA_dlim3XomhRkJAYufJu4NcxLrnoPqoYMohiZoxc_cGKc_x8ikazN-bfe9vBTBpH0unyhxA_szK3lkY6CLlz25Kgts_YW05nWTj2L0ii1ctVm0PAVrfsL7tshREpEF9lejn6Qr5yAAN0R_CUR8NZaGJYBRuIDNvvT2DfRtsSNDhjXXF4PAYcgKWbrUn3pjQxyem43CD0hMyQoapPo8hWEIAa1vfEWSa4nawEOFoA8qkgUGqLNXfCVOa61X9XQBK-9JS2lkNYLenJC7Uxyk6s7VxwAUvM8sgjP_kgNpOtbLjv9eqFwv-8nsD-2p5ScDPDyITH9o5uKull8ZovGNp_ydg1lUYQDu1SPKXxEOQboaeBpoUnUoY7FWT7fNTThylPS_ItqZuBMzWZus69I-VOZ_rX8eQ4raZ2-35nlpDUpvhPF9ApPFVXCfYyScGoYkH5_6leMrTeN1GuIczPNywxwidj2YjFmyHBEZJZi6F__gwNijVyLMlP67CIAsETF2Il3vUSwU7vRQUxlTNiCeHTttSABqVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز عملیات احداث برج مراقبت و باند پروازی فرودگاه قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/459013" target="_blank">📅 17:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
یمن تصاویر حمله به مزدوران سعودی را منتشر کرد  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/459012" target="_blank">📅 17:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
رگبار باران قبل از پاییز به تبریز رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/459011" target="_blank">📅 17:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W33E_zqRfutswT6t_IVFOvr4gUzEcjUJXYU9_EQT3Z-d4gF1fDLJlyAYdDjFtYRcTU6zHIUN3zjQQynhaxZeiwjp7Vkme_nXQ69DXaURces54hndF7cW9fYCgbmrNihhFRUE-WRAzuBDs6YVvJOhc5YUyzJdQzhV-ucjJnWTnbRRsVcPsh1oraYz2x0DQ8iFd8CHY22zgyVAzg5gG5QW0xHbBrg3oHbyxEbhf99Tgzm_0Fm5GnaqDNA_f-nG-1U0y5TolINxY5RxIJhme6MFwsGI32EaOc9iqXog98X5igjeu13d3ZIHjaKDMK7CwRn70RKiVLKUIkVWBB07nxwAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان برای شرکت در اجلاس شانگهای فردا به قرقیزستان می‌رود
🔹
روابط عمومی دفتر رئیس‌جمهور از سفر رئیس‌جمهور به بیشکک پایتخت قرقیزستان برای حضور در اجلاس سازمان همکاری شانگهای خبر داد.
🔸
بیست و ششمین اجلاس سران کشورهای سازمان همکاری شانگهای نهم و دهم شهریور امسال در قرقیزستان، رئیس دوره‌ای این سازمان برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459010" target="_blank">📅 17:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459009">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">برگزاری مراسم یادبود اغتشاشگران دی‌‌ماه در مسابقۀ پرورش‌اندام
🔹
در حاشیۀ رقابت‌های پرورش اندام قهرمانی کشور در اصفهان و در سایۀ بی‌توجهی یا اقدام عمدی برگزارکنندگان، مراسمی در ارتباط با یکی از اغتشاشگران ۱۸ و ۱۹ دی‌ماه سال گذشته برگزار شد.
🔹
اغتشاشاتی که به‌عنوان…</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/459009" target="_blank">📅 16:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459008">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQAZ_yZuJmGMwp-JIg-Sx7KANEqxosyC3WAYmpc4bm8oxBRDJHTr1aueDQ3SwO00JErQEZWONN3JL0pYCg1BpJN9gCKC-x9lxCeKw8SYwbKYESxxqBJ0OgYt6RJHOQ26rX1MuYZENgXPym6UWlySW4PocydRJ9pLZ5iLWN-5J7e9Z0ZfqdqIH4qTs1k0X73OakYc2DSmw4vwxlS2sXR-dyUReeLO1I0ZDq4HoH_t0OSNOMusDz6aW-W50uxCGH4Gutc9FIYeAmCzDJvU2HFGBwY9oQ4EERIWsFusZJGXTsxAe6Vq0OB33X9wVruRYDLYuK7c-Az1B9Z3uTYiUzwVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار صریح ایران به صهیونیست‌ها درباره جنوب لبنان
🔹
پایگاه خبری «یونیوز» گزارش داد که ایران به رژیم صهیونیستی نسبت به گسترش عملیات نظامی در جنوب لبنان هشدار داده و به صراحت اعلام کرده که این امر موجب حملات موشکی وسیع ایران به فرودگاه‌ها و پادگان‌های این رژیم در شمال اراضی اشغالی خواهد شد.
🔹
بر این اساس، ایران در هشدارهای خود تصریح کرد که به واشنگتن اجازه نخواهد داد بند نخست یادداشت تفاهم درخصوص پایان جنگ در لبنان یعنی پایان اشغالگری و عقب‌نشینی صهیونیست‌ها را زیر پای بگذارد و این بند حتی در صورت نقض آن از سوی آمریکا، پابرجا خواهد ماند و ایران در مواضع خود در حمایت از مقاومت مردم لبنان ثابت قدم است و اسرائیل هیچ گزینه‌ای جز عقب‌نشینی پیش روی ندارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/459008" target="_blank">📅 16:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459007">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05793a0591.mp4?token=rp8vguqETW-GUSVIu6dn4rVtoT5YVAjFPgWXaurZxHys_NqIxgWqHvlVU1U1wnhi7v6-FzQoSbk1nzjpHsyrhyX2e62Z9cYHL2C64IN_TAhXald54SV7lVGnb0WLvJLTjZ2NXDtQDgHJY4kxfrPRHR5fCnBzdkvEot2DZEBJVPyL6rHz-Ln5xrbFf2QO6DHFvu7CL-xCGiA7bP993KjHpatlZmPFbVY99kWqGNGx4M4rKU8p6UuizDQqqmSUm3L-cZvGD1k1lRUMH51QcnuCG9TvD7wfNJjZaKAIOETIV0kjgyE_5lRpAOyYX1UkdxloNHzQrVGzBWLmd9v_WnCQmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05793a0591.mp4?token=rp8vguqETW-GUSVIu6dn4rVtoT5YVAjFPgWXaurZxHys_NqIxgWqHvlVU1U1wnhi7v6-FzQoSbk1nzjpHsyrhyX2e62Z9cYHL2C64IN_TAhXald54SV7lVGnb0WLvJLTjZ2NXDtQDgHJY4kxfrPRHR5fCnBzdkvEot2DZEBJVPyL6rHz-Ln5xrbFf2QO6DHFvu7CL-xCGiA7bP993KjHpatlZmPFbVY99kWqGNGx4M4rKU8p6UuizDQqqmSUm3L-cZvGD1k1lRUMH51QcnuCG9TvD7wfNJjZaKAIOETIV0kjgyE_5lRpAOyYX1UkdxloNHzQrVGzBWLmd9v_WnCQmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار همتی: اصلاح سیاست‌های ارزی از ۱۵ دی سال گذشته باعث افزایش ذخایر بانک مرکزی شد
🔹
اهمیت این تصمیم باتوجه به شرایط فعلی و فشار حداکثری بیشتر از گذشته مشخص می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/459007" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459006">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7_tDixFXGVwxrWrSZ36eGJJqDITS_BeYlMYDPP3tzyUKxrQyycYHXsrqewu1xS1co7ffEV2KkSyNT5E8mkohgzWriH4lT1sEkDwsKVmAkeRvyGeLa9Virym8yUokh-E8FmSjiWV7W88r8g291UehnsF2FHVT3WhnSTqkB4ldeQvFtHB4oAwd9M_V3M1-y-HKJeyMgd8a3t8Jvq9YFM4V-q1LD6Gx9Mh2hh0YisrEmhNaV4LpwugH3d8K1EqUia9r_zG1_CVkOr61CjAm4iWqQ0Lo0pqswg_U0XUwFHltQWSF2DxstC_u7PIYnBfyJYl5VwX1UeT5pQpPlpwfDzGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درپی معاملۀ مفت تنگه هرمز
🔹
تانکرترکرز گزارش داده که میانگین صادرات نفت خام از تنگۀ هرمز در ۷ روز گذشته ۳.۸ میلیون بشکه در روز بوده است.
🔹
این درحالی است که مقامات آمریکایی تلاش می‌کنند با ارائۀ گزارش‌هایی این رقم را بین ۹ تا ۱۰ میلیون بشکه نشان دهند.
🔹
طبق گزارش کوبیسی لتر، برنامۀ عملیات روانی ترامپ با محوریت بزرگ‌نمایی تردد نفت از تنگه هرمز، ۲ هدف «آرام‌کردن بازارهای جهانی» و همچنین «مهیاکردن زمینۀ معامله با ایران» بر سر بازکردن این مسیر راهبردی را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/459006" target="_blank">📅 16:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459005">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e17753a40.mp4?token=TGDHClZodaoB1oaLkteZuYUO1cfIzPSZHYtcArUnMYq1A-cVtjwcgzNUAzJLpccGNV7BopVZaPAKzHwn4QAV-kDT6mo8BHociqaJYOmeCDsCJ8nIYLGVIHvJS8IbBRhLb9xlawD8UNqs4o4QVZtB5p8r66FqIZKBlCGp7wBOGc1CQ0zytXpHjp4wOD_PawJ8c5OA9iZB6_28kwXLdgz0JSuPNXtDYb2WW_DPo7G41OZ7a3V8lly_TGqiZxWgKaqbJbDWXb5xEVRCwiSneAKTV3vSu53FflMP80xUnuqdh6RMff6s7AMc_K0BIda49_4_V2wT5emPPpqVLmkzILyd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e17753a40.mp4?token=TGDHClZodaoB1oaLkteZuYUO1cfIzPSZHYtcArUnMYq1A-cVtjwcgzNUAzJLpccGNV7BopVZaPAKzHwn4QAV-kDT6mo8BHociqaJYOmeCDsCJ8nIYLGVIHvJS8IbBRhLb9xlawD8UNqs4o4QVZtB5p8r66FqIZKBlCGp7wBOGc1CQ0zytXpHjp4wOD_PawJ8c5OA9iZB6_28kwXLdgz0JSuPNXtDYb2WW_DPo7G41OZ7a3V8lly_TGqiZxWgKaqbJbDWXb5xEVRCwiSneAKTV3vSu53FflMP80xUnuqdh6RMff6s7AMc_K0BIda49_4_V2wT5emPPpqVLmkzILyd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلسکوپ رومن ناسا به فضا پرتاب شد
🔹
تلسکوپ فضایی پیشرفته «نانسی رومن» ناسا، با موفقیت توسط موشک «فالکون هوی» اسپیس‌ایکس به فضا پرتاب شد.
🔹
ناسا پیش از این اعلام کرده بود که امیدوار است از این موشک برای مطالعه بیش از ۲ میلیارد کهکشان استفاده کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/459005" target="_blank">📅 15:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459004">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ_80P18ectUZySTc-RoidL8jIT6VSuHH8AHyVo0YLAmqHCtanE6jm3PY-oTzaE7Zb6Ku2dRH_u5RPeuW-rqRK92im5naePSDZlIA0OoN7wPgHq9Rg71p3X1g4iDKkhKKr9X_6wobd6zZUbe_RsPfM0VskAbg3OpuCmSe_anfhHPTPkRI432nQLlxgHh8p44LW_vbsgIvSko8yx6oMqdnxzuwvFrXNShPM12AisGsm8PjTwYtFdLGs3mb0DpVLtl06vExNNvQe99aRmTsHcx-TF9iU0MGmMe6EhSg2b_hn83fmfh29ozYIYi9V_kqYJAsMx7kgcVaOaisVgeAMBq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد قیمت بنزین در سرزمین‌های اشغالی شکست
🔹
وزارت انرژی رژیم صهیونیستی از افزایش قیمت بنزین در سرزمین‌های اشغالی از ابتدای ماه سپتامبر خبر داد.
🔹
براساس نرخ جدید قیمت هر لیتر بنزین به ۸.۲۵ شکل معادل ۲.۲۷ دلار خواهد رسید؛ این بالاترین قیمت بنزین در سرزمین‌های اشغالی در ۱۴ سال گذشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459004" target="_blank">📅 15:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459003">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d91d7afef.mp4?token=pSGRCgVZb1-F0UmKcLv_0rKi3DM7nDpKP3HG8vM2GaKrsNprl6QC3nurAizGrFeZjQ9VAOfOXX5K0KKsIPM40r6GCnHvJvVAhAdNw-RcA_FfGNr37dqC0Ljn_0UCK6gd_A7w7BduwVq6dpskedpo37sHS5c9S3Dz12PBn9TT7ApEc1-5d1mEUB_9B7iEA07YgVYsHxEhtqyvUq_xte8aFTPBA444I3t6lhQg4wK2m9EykmbbRaWByiRNi8aDuvcnUdbwGtW43_10X3egYfs8ENc9GaIdBnfahhQsFbItgkRs98KsQGkBcZ9Hwb3Epue9OSuSDrcAriz_VpMC1OhrPa3zp9k43LuZ6n0_WHdywOgGUhPPrG0u8iO0bHQJIY4TcfcTDXD7U1rJ8QKqLzggaLWhoPnUdfdQhovwDOsps1_0-90hSPABWk2rZ8akZkfJrTJMlUMO6puMqD89TZGtpPo3qSG1MxDSDkx8bnBtQMi6vlOmHCRyBLT1QdyWABaIzx80ghsLORzQovke_--KzGmyHyLSPodMlH18XKVjT0N0hr2mL2jlTfQ7vCk6UfHYNDPWmQ_QcjtzCSbRR1rEeDnkKUevx-a--4pD0dL5DWQN8QD0QsF2s5zYWsbn2upO8RpaNME_1Zkv4q5_1J7JG_OAzgvAqzSXanHFZF3u9E0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d91d7afef.mp4?token=pSGRCgVZb1-F0UmKcLv_0rKi3DM7nDpKP3HG8vM2GaKrsNprl6QC3nurAizGrFeZjQ9VAOfOXX5K0KKsIPM40r6GCnHvJvVAhAdNw-RcA_FfGNr37dqC0Ljn_0UCK6gd_A7w7BduwVq6dpskedpo37sHS5c9S3Dz12PBn9TT7ApEc1-5d1mEUB_9B7iEA07YgVYsHxEhtqyvUq_xte8aFTPBA444I3t6lhQg4wK2m9EykmbbRaWByiRNi8aDuvcnUdbwGtW43_10X3egYfs8ENc9GaIdBnfahhQsFbItgkRs98KsQGkBcZ9Hwb3Epue9OSuSDrcAriz_VpMC1OhrPa3zp9k43LuZ6n0_WHdywOgGUhPPrG0u8iO0bHQJIY4TcfcTDXD7U1rJ8QKqLzggaLWhoPnUdfdQhovwDOsps1_0-90hSPABWk2rZ8akZkfJrTJMlUMO6puMqD89TZGtpPo3qSG1MxDSDkx8bnBtQMi6vlOmHCRyBLT1QdyWABaIzx80ghsLORzQovke_--KzGmyHyLSPodMlH18XKVjT0N0hr2mL2jlTfQ7vCk6UfHYNDPWmQ_QcjtzCSbRR1rEeDnkKUevx-a--4pD0dL5DWQN8QD0QsF2s5zYWsbn2upO8RpaNME_1Zkv4q5_1J7JG_OAzgvAqzSXanHFZF3u9E0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاضری برای ایران بجنگی؟
مقایسه جالب «عشق به ایران» در بین سلطنت‌طلبان و مردم کشورهای منطقه
ساعت‌ها می‌توان درباره این ۳ دقیقه تامل و گفتگو کرد، پاسخ‌هایی که باید در تاریخ ایران ثبت شوند.
@Fars_plus</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459003" target="_blank">📅 14:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVuddbfvAfkAi6d3M1pXebdaLEjDYDiA3HQ6FlWTcW_3gorXzOHRN0dhbbJqwBCAyodBmanIMHnfp99EV8Du9V2Fvz4QZ6b02vmIHlJrzxXLDVFhFDKcEmLkgWEnRh_99tBXQzs4cwAOC1yIOuw0_FgoHlXf6vSaCyxI4wkNxFfXmdSrH37GcVOt6WrD6RI4_mE7SdHKHPGoJwYFqBEI_clwf2n2yNj11FC23ZRw4xk06rAF6qN8pUyWFDvfYgWt5WyWxn3lKNDcW8yUzA7-IYgH1O5ugyg9855uGjS_0tpOgVLDWZSS7SCWLuQVK2uNfzU52uTWNKmhh6kF3X2CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزرای خارجه و دفاع ترکیه، پاکستان و عربستان گردهم می‌آیند
🔹
مقامات ارشد ترکیه، عربستان سعودی و پاکستان قرار است دوشنبه در استانبول گرد هم بیایند تا نخستین نشست توافق دفاعی مکه را برگزار کنند.
🔹
یک منبع وزارت خارجه ترکیه با اعلام این خبر گفت وزیران خارجه و دفاع و همچنین رؤسای ستاد نیروهای مسلح ۳ کشور در این نشست حضور خواهند داشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459001" target="_blank">📅 14:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458999">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2ZOkahBN8cc22NVhCYHN4acbG2ZeC2kCKyaDJHgiAlp3mHdprMDpzAWr3N3Z_znt9VdIcm6TJsehOVxcD5JwE9No8pzSjdt_JGZgI6LYclr2ZCz-efPLbJKLQIcqn89lBx12mjX6kpY81fxILBnp3DV2DSwlBAHKfjHhqwgyoWL0lMdX5kuZBxPhdaLiKUqgSH3hZ0QwO1WA_HY8v4qVYgqgO6nmSn5jULcXCpkYVrYPc7e1pt7iJQykC8MC3IobrdvIMWfXEcUEOTXyQLNxrD4kXHa8F5R5Tu6Iwx7pFCl-s1BovrMMKSQCkwBklX_4F02bSFX97ZuakznajzCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RIx40xQb_BZRydkyCa1PRwC4MA4eH5SmNav2cZraB7noKChvpp7we4VQUnmKRwzvmv-gKl_G-ovmxj7Y9ip8q13zsYeI9I3rU9CQFIijk-i9dTwl5TzZbPI_mwr51mLzSgLimDYDmphSa4sZCiK5Rp2c9Lq8Ta8s2xvyvZEw1YaQAxK1NQGw9vWMKsoB416HM99qyuJcSSjFST6mAG1J6SxbGDemOP2dTR-JSX-53xO2mhH4CAO3rPLClu-TpWe5MujdDMxKz3muiNCL17S1R3AoDiV1yUjPpywFqtlMOzqnW5Lpxl5urTDC0CfGxWe4XlvbVguZFSkw98FkdqGloA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دست‌خط شهید لاریجانی پیرامون مقام شهادت
حدیث اول
🔹
پیامبر(ص): هیچ قطره‌ای در مقیاس حقیقت و در نزد خداوند، از قطرۀ خونی که در راه خدا ریخته شود، بهتر نیست.
حدیث دوم
🔹
رسول خدا(ص): بالادست بر هر نیکوکاری، نیکوکاری دیگر است، تا آنگه که در راه خدا شهید شود، همینکه در راه خدا شهید شد، دیگر بالا دست ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458999" target="_blank">📅 14:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458998">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7B1KEwKzV_M7Tk6hsc1WQa_G_KZvuy_PIbsOfY7s7lZ4vZVJ1ovb8TLH1-ClzX8SaHWrdx6nTFJxtyM8PXytL4RkqZ0ijbTvv59XzQLxHDHWEz8yk8627bWcdTTnmPuolC_rj2mzgAQzUNEmkTPCKtfdaISO4DIsW_sf741-2Mw9tKkIgnEKmdoBOJtHkdJPcjHozuH3NmGAITNu348kP4BwuYu7hSwIjHqPWWzUgsi8_TidNe20E8wW7abii5CymIJFk23lhSlqBZeEBrFYqSyFzxWN1eQsphCx-aBkvfw7EVN-wTx7eshYmjPJxdOTgbr5ArHftkjBdqg1Wnalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریادار ایرانی: نیروی دریایی ایران مقتدرانه از مردم دفاع می‌کند
🔹
فرماندۀ نیروی دریایی ارتش: امروز نیروی دریایی زنده، پویا و مقتدر ایستاده و کارکنان آن با همان روحیه‌ای که شهدا داشتند، مأموریت‌های خود را دنبال می‌کنند و از مردم دفاع می‌کند.
🔹
دشمن در شناخت روحیۀ ملت ایران و نیروهای مسلح جمهوری اسلامی ایران دچار اشتباه محاسباتی است.
🔹
پرچمی که شهدا به دست ما سپرده‌اند، باید با قدرت، عزت و سربلندی حفظ شود و به نسل‌های آینده انتقال یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458998" target="_blank">📅 14:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458997">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یمن: عربستان در ورود داروها کارشکنی می‌کند
🔹
وزارت خارجه یمن: رژیم سعودی طی ۱۲ سال گذشته، از طریق نهادهایی با مأموریت بشردوستانه، از پرونده انسانی به عنوان برگ فشار استفاده کرده است.
🔹
نهادی که سازمان بشردوستانه فعال در یمن نامیده می‌شود، در پاسخ به فشارهای سعودی‌ها از واردات داروها و در رأس آن‌ها داروهای بیهوشی خودداری می‌کنند.
🔹
صنعا در برابر هیچ فشاری سر خم نخواهد کرد و نبرد خود را تا بازپس‌گیری حقوق مشروعش ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458997" target="_blank">📅 14:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458995">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76a09f6a8.mp4?token=B-WBl1TeZEIGnrcsA2Dn8xvhi3HRKzJM3M5u3SPppTjrciIZUSOuNBKAluTphKjU47hSS0iXgOuyC88v0CETigVtAASZYYfq-wOeiL_gh8AJh2A7bZqk6c70SQGFhr4reHSPIIgTTDpKD-DjZCJcfnJFrvpvbq-JXlNH6SnXOfu6RkqeRS07Ymb74V8BGgO5DclOIUFjHWrMdxmT7vjl4qWY1Pa7J-bQwrokqaJTcFYLqWI2eY_Uzh31hlAQ0U4L57Uxgy7mtGvOU-lLn40nV8dKhWivWbYuHKFzvb6x7eTOA_OVZldLezFtl-H2RVr7ef6juEBIa1mJaoZ9oF0tWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76a09f6a8.mp4?token=B-WBl1TeZEIGnrcsA2Dn8xvhi3HRKzJM3M5u3SPppTjrciIZUSOuNBKAluTphKjU47hSS0iXgOuyC88v0CETigVtAASZYYfq-wOeiL_gh8AJh2A7bZqk6c70SQGFhr4reHSPIIgTTDpKD-DjZCJcfnJFrvpvbq-JXlNH6SnXOfu6RkqeRS07Ymb74V8BGgO5DclOIUFjHWrMdxmT7vjl4qWY1Pa7J-bQwrokqaJTcFYLqWI2eY_Uzh31hlAQ0U4L57Uxgy7mtGvOU-lLn40nV8dKhWivWbYuHKFzvb6x7eTOA_OVZldLezFtl-H2RVr7ef6juEBIa1mJaoZ9oF0tWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای پارس جنوبی چگونه پس‌از حمله مانع اختلال در شبکۀ گاز کشور شدند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/458995" target="_blank">📅 13:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458994">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ad1e6014.mp4?token=N9LTiEHJLT4-V_tMO4OuNtqLEweduEdhkkjGaB--gwdAl1eWQ7eChQMCwa6CljFRiQ71Wb9GVqCAqm8vKLXepLmgGUmR7s3mcvSJJzeO_RgsGck6V9gmF1kaBQaazlQ2j38vIAp4H9v0a3oOUJBxP-0tXYN4oXNhjnZRgdIq1F_o5Md3ifwBCFi1D60sxvI4PjxRVWSA2KqfvTEB7vcVQiYVoP9M3-QQzgMnPPkgAFuWJWN9oJEVXoRon-lbcFjxoNlfq_Bkyk5m2FYlEyyr7g9XKHXUeRv9QCgM4fGv-s-tLjnApFmKYcBMS_MZ5tyrntuIa0Ivov3J3JD19uW3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ad1e6014.mp4?token=N9LTiEHJLT4-V_tMO4OuNtqLEweduEdhkkjGaB--gwdAl1eWQ7eChQMCwa6CljFRiQ71Wb9GVqCAqm8vKLXepLmgGUmR7s3mcvSJJzeO_RgsGck6V9gmF1kaBQaazlQ2j38vIAp4H9v0a3oOUJBxP-0tXYN4oXNhjnZRgdIq1F_o5Md3ifwBCFi1D60sxvI4PjxRVWSA2KqfvTEB7vcVQiYVoP9M3-QQzgMnPPkgAFuWJWN9oJEVXoRon-lbcFjxoNlfq_Bkyk5m2FYlEyyr7g9XKHXUeRv9QCgM4fGv-s-tLjnApFmKYcBMS_MZ5tyrntuIa0Ivov3J3JD19uW3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه: ۲ روستای دیگر را در جنگ با اوکراین تصرف کردیم
🔹
وزارت دفاع روسیه با انتشار ویدیویی اعلام کرد «۲ روستا در منطقۀ دونتسک را از وجود نیروهای مسلح اوکراین پاکسازی کردیم».
🔸
وزارت دفاع روسیه وز گذشته نیز از تصرف ۳ روستای دیگر در جنگ با اوکراین خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/458994" target="_blank">📅 13:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458993">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D97W8vTD9JENSGxDLUJaUfZNQkjYO7GR4OsJVQDKMigcDU9Ct0MVuQxmpAQK5zc7SeoxYgQ3t_UC5ehil6lRUz1FS8KSjg9OZbmG-jds0Ut2_rw0hoqDmDb8qMdRkrj0toIwlAGlqrmBBNTX2bJHjfx_Y4_pCiY8DpBkSic1KnpQhSSd5ri54WvBloX-D0FiqLCgGAPG29V4DMWaqmXI52aU43Et8poRABf5-YvylySA4HzKOZ_HiwadmAAHyc-mAPHL_ASbqeB3ktDjckz2vjPnzlg9lyXqxjFnwcqXBV-R6JJbNDw5Rl5fwYv7ZrmqwigUcQHuKWox7gUxsbWaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ نوجوان اسرائیلی به اتهام جاسوسی برای ایران محاکمه شدند
🔹
دادستانی اسرائیل امروز علیه ۲ نوجوان ۱۴ و ۱۶ ساله از استان حیفا به اتهام انجام مأموریت‌های مختلف برای یک عامل مرتبط با ایران، کیفرخواست صادر کرد.
🔹
روزنامه یدیعوت آحارانوت مدعی شده این ۲ نوجوان در ازای دریافت پول فعالیت‌هایی ازجمله تصویربرداری از اماکن مختلف، نوشتن شعارهای گرافیتی و جذب نوجوانان دیگر برای انجام مأموریت‌های مشابه را انجام داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458993" target="_blank">📅 13:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458992">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAToLCjkMS2AYrCFGIjDSgf0-e4ZiK9H96ZKmjSv7BSIdZUO22evaE1hGw3mB7BGAI2lH9Bm7iYPOAJk20EHZWfhKuQkF-pmlzg06BoEZ3I7og-xtq11viDZMfSZsy9UNL3qEBUBUQpOFNEjuqj326rEQlc-p3DjuegVW4_bbcWbjsb-aGa7qxH9_ZHY8H6kNWjjCwfhhnsB5HXiUb1vUn0pxYA0YpSE8PgbhAH7mEkk4ixmf_PWBzHc8WAlGutaovjpCjj_mSKZaYr6hdHJBL8nFzDjK4w-bIhui-OFeYHCxmVlEND2BiuCJuMpij9Z2z_N5pRztXx-ySxk6H5Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز امور اتباع: جمعیت اتباع خارجی به زیر ۵ میلیون نفر رسید
🔹
در طول یک سال گذشته نزدیک به ۱.۸ میلیون نفر از اتباع غیرمجاز از کشور خارج شده‌اند.
🔹
جمعیت دانش‌آموزان اتباع خارجی هم از ۶۰۰ هزار نفر به ۳۲۰ هزار نفر رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/458992" target="_blank">📅 12:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458990">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار و فعالیت های کمیته امداد خراسان شمالی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c0a387ad6.mp4?token=rygKSAVzzkPgwAiqHhddLG4cWfCu3NDKyRta_fsqyvEQRU-LpT7BY2uAYnTCqTeM0CrbalDvUngoNpSKDiSG5TpRxajYuP65bmADWzi7RsY4BmwMBXiFSbEG8_sauRoaXozK237JX5pVog86LM2l3-eK9E-y5wOWemmtNpw5QooXu8rADNV_SKERog_k9L9aHhtlbxkAxwlD-X9Fv84ANd3-q2Pf-3p9ddTge1V3cOhrXoEFFJQBrbM6EiZzWo0DCJc-tXCSuowbG6yCZsu54ezju-RIs8FVMV07PLgdYaR1PtCpuekGDqC3g0oS3hR5k68AovteU9nh1I10qGBvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c0a387ad6.mp4?token=rygKSAVzzkPgwAiqHhddLG4cWfCu3NDKyRta_fsqyvEQRU-LpT7BY2uAYnTCqTeM0CrbalDvUngoNpSKDiSG5TpRxajYuP65bmADWzi7RsY4BmwMBXiFSbEG8_sauRoaXozK237JX5pVog86LM2l3-eK9E-y5wOWemmtNpw5QooXu8rADNV_SKERog_k9L9aHhtlbxkAxwlD-X9Fv84ANd3-q2Pf-3p9ddTge1V3cOhrXoEFFJQBrbM6EiZzWo0DCJc-tXCSuowbG6yCZsu54ezju-RIs8FVMV07PLgdYaR1PtCpuekGDqC3g0oS3hR5k68AovteU9nh1I10qGBvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
افتتاحیه کشوری در خراسان شمالی با حضور جناب آقای سید مرتضی بختیاری رئیس کمیته امداد امام خمینی(ره) کشور
@khnemdad</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/458990" target="_blank">📅 12:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458989">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/458989" target="_blank">📅 12:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458988">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3a5b28.mp4?token=QKSyKs7dqKCAHp156qPQFUPGM_vxFdsASmNlrozmeAABEluCb2LXAex0YA5936Md1KiLuKzB0NNz695vMvrK8Yh9SPYWprq_y7Wpx74vTRpFqfUwXYD4RhlaX4361XJjFTO-dFpqc-M_W5KoHZy7-TI4cDPogspTfUXRrRRAY4zEGCCZMEeYvq-LBto_wmQT9Gxbt7svhKEDmWPVJ4BT43Ww13gteYs4yrYPf9nYpNa0DZGEB6ozD-GfDxdSualXkft7SnZVgOCaLtbS-MZWGg7n4Hmw24iT6Wwv2YaJG5j0UpdH3hwGt4e_-gIFWKnxLNPeAlVdWRnR84nvdT-oWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3a5b28.mp4?token=QKSyKs7dqKCAHp156qPQFUPGM_vxFdsASmNlrozmeAABEluCb2LXAex0YA5936Md1KiLuKzB0NNz695vMvrK8Yh9SPYWprq_y7Wpx74vTRpFqfUwXYD4RhlaX4361XJjFTO-dFpqc-M_W5KoHZy7-TI4cDPogspTfUXRrRRAY4zEGCCZMEeYvq-LBto_wmQT9Gxbt7svhKEDmWPVJ4BT43Ww13gteYs4yrYPf9nYpNa0DZGEB6ozD-GfDxdSualXkft7SnZVgOCaLtbS-MZWGg7n4Hmw24iT6Wwv2YaJG5j0UpdH3hwGt4e_-gIFWKnxLNPeAlVdWRnR84nvdT-oWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلر تیم ملی آرژانتین به چلسی پیوست
⚽️
امیلیانو مارتینز، دروازه‌بان ۳۳ سالۀ تیم ملی آرژانتین و باشگاه استون‌ویلا که سابقۀ قهرمانی جام‌جهانی را هم در کارنامۀ خود دارد به چلسی پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/458988" target="_blank">📅 12:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458987">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amyg5t4fmPUqaVkqLwKVV5WqUd95KYSPgW_L5tf_nUPtrCh3GlQbI4vgLRzJRH9FmmGVB5JpWnxh3W5oBoTeK9MZULt4FWipgQgZ1yBvXy6hKBG3Xi_3aleTUNQmPpHaHgDoLBiMYhs6xJbpyMWnO0P_8dGVJFnVp0b4NubpFZC40_08VBvhg5_qc0qsuGseG0worZA50Wh5EBIWKIbsuv9f3sb2DjGaJtq4kpDt_peariRy97WlrEqG2DgMEZ-bjeXebXlCPBZJkYNrZd71-mx9iq5_D_5Aiaklbj5uZ8kWGRY0swWnh4NvPVCqouxMDBuM01SsqoZDHyCHrRr7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: مردم ژاپن دولت خود را دربارۀ مشارکت در جنایات آمریکا پاسخگو کنند
🔹
وزیر خارجه در واکنش به گزارش‌هایی دربارۀ اعزام جنگنده‌های اف۱۶ آمریکا از پایگاه میساوا در ژاپن به خاورمیانه برای حمله به ایران گفت: مردم ژاپن دولت خود را دربارۀ مشارکت در جنایات آمریکا پاسخگو کنند.
🔹
دولت ژاپن در قبال استفاده از امکانات مستقر در این کشور مسئولیت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/458987" target="_blank">📅 11:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458986">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438a8cbf8c.mp4?token=D0Mji4m51LuwsH83lf4M8a9XKhKEcQS7kjn1u3DfJ6iE2xm4LKMmWTe2WxC6hMfRIkyh7XJ3gsTP_5cu36dN9ES-f9crRMikHH4c9ld1ORikcPtLFGIVupG7jLE9l_uxaYcaMKp0dubRMW1VzyQMsXqAuzbinSV9hoG-CN79BIVNgkpXw9rrI41LBUUjqIw-QFiRpsw5krX9CJyIoXWG3G-cTg-KCzjOFDCPEEmqS1lw1YGQDT-IF0omdvhwOjgfw7pSbmpgYjrbG6ed45xCge9I2SuR_S8TRC_BZwYwrdzU74eGxrQycfrZEoS64c8uoavr_ZPW6TFLu15QeGYesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438a8cbf8c.mp4?token=D0Mji4m51LuwsH83lf4M8a9XKhKEcQS7kjn1u3DfJ6iE2xm4LKMmWTe2WxC6hMfRIkyh7XJ3gsTP_5cu36dN9ES-f9crRMikHH4c9ld1ORikcPtLFGIVupG7jLE9l_uxaYcaMKp0dubRMW1VzyQMsXqAuzbinSV9hoG-CN79BIVNgkpXw9rrI41LBUUjqIw-QFiRpsw5krX9CJyIoXWG3G-cTg-KCzjOFDCPEEmqS1lw1YGQDT-IF0omdvhwOjgfw7pSbmpgYjrbG6ed45xCge9I2SuR_S8TRC_BZwYwrdzU74eGxrQycfrZEoS64c8uoavr_ZPW6TFLu15QeGYesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بن‌گویر اسرای زن فلسطینی را تهدید کرد
🔹
در ویدیوی جدیدی که از بن‌گویر، وزیر امنیت داخلی رژیم صهیونیستی منتشر شده، او درحال تهدید کردن اسرای زن فلسطینی دیده می‌شود و با افتخار از اقدامات سرکوبگرانه که علیه اسرا سخن می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458986" target="_blank">📅 10:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458985">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e606af461.mp4?token=aFp44OpZzsp_qvuK4vt31zVN10fIjwnxTwroXW6OsrIgqVfWnChOZnbqOKxiEEfYlJleeasD5UC5MhkNh21SU7HVqAhUlvBRmhUyKL6YUw7e6aumBgXokOWgEV70QbFsHVbnlP5YH3rAJF4GMVb4LGYJZvQvncbTKmtZiqxzOVhK9-72SIU1-PlGmP5Lx0VSjDLZFHFKaA6wWG3m71XSwiyeuO-cLOgIfvY6AuFwIkbmcZRuhOXFLVLqRVKrjRIx5OjInts7tQpocX-RRzDC3-ycO64azyhkTYD0EUAAs0uKZkuhZej5cN8iG1t5rDwwPP5PVYUEswFTMggHl87O9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e606af461.mp4?token=aFp44OpZzsp_qvuK4vt31zVN10fIjwnxTwroXW6OsrIgqVfWnChOZnbqOKxiEEfYlJleeasD5UC5MhkNh21SU7HVqAhUlvBRmhUyKL6YUw7e6aumBgXokOWgEV70QbFsHVbnlP5YH3rAJF4GMVb4LGYJZvQvncbTKmtZiqxzOVhK9-72SIU1-PlGmP5Lx0VSjDLZFHFKaA6wWG3m71XSwiyeuO-cLOgIfvY6AuFwIkbmcZRuhOXFLVLqRVKrjRIx5OjInts7tQpocX-RRzDC3-ycO64azyhkTYD0EUAAs0uKZkuhZej5cN8iG1t5rDwwPP5PVYUEswFTMggHl87O9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک کشته و ۵ زخمی در حادثۀ تیراندازی در سوئیس
🔹
رسانه‌های سوئیسی صبح امروز از وقوع خشونت مسلحانه و تیراندازی در یک مهمانی در شهر آرائوی سوئیس خبر دادند.
🔹
پلیس این شهر شمالی سوئیس  گفته که در این تیراندازی یک نفر کشته و ۵ نفر دیگر زخمی شده‌اند و تحقیقات دربارۀ انگیزۀ این تیراندازی همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/458985" target="_blank">📅 10:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458984">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8d66fee.mp4?token=jxo9Xdc8FDbjJg4UOFsOjvTSnXYE29DgoG4t_9Gb_wtbgqddfV7p6bBTp1KzLwFfwFjzA7xHNm2RIu3Gfy8SmNBrAGhUVQaLP4SqhbPzLGvk70UubLpO0teWlCYs1A3HzWVayq36s9nJd-ppb5Crxv75MzOYBwuA0PVQz6q8XqIF4qtPZY5TJm6UpNPfIo5bWFgseGHKI4y-LwVCZQ6mhnXSs8HWd1lD_t79Zr65_O_hQ5iQDbOwBsFxL6h-gEkxeJ41GO7qskD0wH0JhGDdgvUjdyaRmoqUibDY1moU-9hQY5jgkscR3M82mSrqvQG7H8djOd7tLkRjwbgXWAAVXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8d66fee.mp4?token=jxo9Xdc8FDbjJg4UOFsOjvTSnXYE29DgoG4t_9Gb_wtbgqddfV7p6bBTp1KzLwFfwFjzA7xHNm2RIu3Gfy8SmNBrAGhUVQaLP4SqhbPzLGvk70UubLpO0teWlCYs1A3HzWVayq36s9nJd-ppb5Crxv75MzOYBwuA0PVQz6q8XqIF4qtPZY5TJm6UpNPfIo5bWFgseGHKI4y-LwVCZQ6mhnXSs8HWd1lD_t79Zr65_O_hQ5iQDbOwBsFxL6h-gEkxeJ41GO7qskD0wH0JhGDdgvUjdyaRmoqUibDY1moU-9hQY5jgkscR3M82mSrqvQG7H8djOd7tLkRjwbgXWAAVXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش شمار قربانیان سیلاب مرگبار در نپال
🔹
پلیس نپال از افزایش شمار قربانیان رانش زمین و سیلاب مرگبار در این کشور به ۶۱۶ کشته و ۲۳۰۰ مجروح خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458984" target="_blank">📅 10:24 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
