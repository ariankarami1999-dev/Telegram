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
<img src="https://cdn4.telesco.pe/file/C6txvn9JkJnSBQm7zw2oyDdriv7RnqhI4NJJF7OctIE5w0hLwzjNSnM4-vGp-g2_cn-K5YX2cG-pSb_3H6g6BUx0jjtAM904zGX_V9b2zljUqEnkvbriRP8lPd3-oHja_iGeS_FUX51j1UYSbTLUjV5_lIvIs08DfcAej4btwslyj6QiJv8JYnIZmc-WPAN2quJ78aFwo2dLFof2cM9aLE8A0EPIxnPNAJGHzLAqk9cM5NIJgqO3GJM340h86q1f4jc_L0vzJ9-6Z5WRj3krroZ8wBYOaeB5k7qYZPmfaVva224aGUNbkbNcIFF26ZMVQ5S59wG7NouV33HGZGzxAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-447467">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9555d366.mp4?token=d7ygj6B04hijt7t5wiOMvfW1X5KK_g4PpOHfiw_UDFkFMX7ew3McTtR7wTQQW4kAEt2PL9YAB7t1YGlUHO5Y6hP9JDnCvhspGNNwIW2Aw7ewS8iOPjklXbugxjOrfDbZGyOwEXA6dzSiHx6VzhCsvOaX8lzB2mnGzejaCZy9sjHRofcO46m0J0rHXupzK1SEBxQEEZMFCuegWAhATN7HaFOPXArHQcB4qBxHYzt1ywV2caHvfShCXpj0V_biD3vI8T1HzZow7h1licmQWnS54yXzG5GEVbL2tz-Zju34-wxaZz9aNXg046y4TIjSGwl9-_yo6U1EXxlbk2BHP-RtBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9555d366.mp4?token=d7ygj6B04hijt7t5wiOMvfW1X5KK_g4PpOHfiw_UDFkFMX7ew3McTtR7wTQQW4kAEt2PL9YAB7t1YGlUHO5Y6hP9JDnCvhspGNNwIW2Aw7ewS8iOPjklXbugxjOrfDbZGyOwEXA6dzSiHx6VzhCsvOaX8lzB2mnGzejaCZy9sjHRofcO46m0J0rHXupzK1SEBxQEEZMFCuegWAhATN7HaFOPXArHQcB4qBxHYzt1ywV2caHvfShCXpj0V_biD3vI8T1HzZow7h1licmQWnS54yXzG5GEVbL2tz-Zju34-wxaZz9aNXg046y4TIjSGwl9-_yo6U1EXxlbk2BHP-RtBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر شهید زهرا محمدی‌گلپایگانی نوۀ ۱۴ ماهۀ رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/447467" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447466">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV0uug3FSGH_Yy3kZqKKu0qnfQe8iJjLemHixPHP-NUbeV3eKMCZ5ExNXzxJh20shIYjmdElDhYHA80y5h4ywOBi1S5n4PuwVd5XLCS3BGWq_ap1JqLn4_HA-8wib9nPRs6fEZaKoTfbOlMpQAG27J10TfGZ8b9zEcLIoO6bPKvK4nhaNoudGeb1cQOLxQ3mQzht-JYo5inUN3b-7-utWdoBfQ0FIofe0tbVZtLZVzbJgd_kvS5BTtQ3qDauA6FrCjT6Sa3x1uNSKtxh0ntG3kD8bkSfenrN1d8YANIgcWo-RmHrboVdvI-4n4OiQUzepU78WYSCK5SM1thlIBY_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور مخبر در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/447466" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447465">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f531ef0c9d.mp4?token=eQFc-TXF1DS8pnps86G1455WMIIynUv_O2K2mpmm5JbOgd-9S0y3Hf71qYKPt4Fx2OpPn6l0B3DkFTuP4-EQ7cvKp8uCws4TVLyD-n4ArVD64LIkMYkzM5xDzuW3uhuqLCNuaANusAs8SDUNfWZfa_amx2wrxKs5g7Y-gK-NQH-7rjnjJDR3Mcazu0uD7kT7SSa2I36zETrkI7EBpczMXcsF1a_UiMb7HACaJwb0fbyXLelfPsJxRyCU8dHCdtUpjO3MJoeK0kN4zVfYBA4kNRM7ukd1trBu0HJkt8EiL2OgVr7pHvxVKJ3JHfhWBH7UZ1u_9SG4FIlQ0ReG2ZJPmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f531ef0c9d.mp4?token=eQFc-TXF1DS8pnps86G1455WMIIynUv_O2K2mpmm5JbOgd-9S0y3Hf71qYKPt4Fx2OpPn6l0B3DkFTuP4-EQ7cvKp8uCws4TVLyD-n4ArVD64LIkMYkzM5xDzuW3uhuqLCNuaANusAs8SDUNfWZfa_amx2wrxKs5g7Y-gK-NQH-7rjnjJDR3Mcazu0uD7kT7SSa2I36zETrkI7EBpczMXcsF1a_UiMb7HACaJwb0fbyXLelfPsJxRyCU8dHCdtUpjO3MJoeK0kN4zVfYBA4kNRM7ukd1trBu0HJkt8EiL2OgVr7pHvxVKJ3JHfhWBH7UZ1u_9SG4FIlQ0ReG2ZJPmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعیت انبوه عاشقان رهبر شهید در میدان انقلاب تهران
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/447465" target="_blank">📅 11:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447464">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c51590d4.mp4?token=fVZQ-Wlc5BDSkRMW7WE2o3kKxYFIvz5phkk0V_EQS-UkLcIjmvUCvlARF1916aBOJeGUv-JZUtyZ-JQtEnWSmUAH_pxqouvqmQ77-TQlsC-C6Bnxq7emwpCRqttuLjjztouqQLr84DKE59CSK7rEO_zXIHjZSnVT-2RCQt10jVGJrvb7UxoLm2ig9o2HLKzwWISU8FTrvySLK0b3WITCDcGPXeQFbA2B_VV6Zu-xgKrI3BC5W_Yfbz4uoSf9uBnUH4ASvxSHzY6LrImEi0qQgTNgExFtr2NQFRfEAhUpw7YZf2CLXzo4TlGBz_ddwHkoAxeQCaLtoR5Fs5kMMm46xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c51590d4.mp4?token=fVZQ-Wlc5BDSkRMW7WE2o3kKxYFIvz5phkk0V_EQS-UkLcIjmvUCvlARF1916aBOJeGUv-JZUtyZ-JQtEnWSmUAH_pxqouvqmQ77-TQlsC-C6Bnxq7emwpCRqttuLjjztouqQLr84DKE59CSK7rEO_zXIHjZSnVT-2RCQt10jVGJrvb7UxoLm2ig9o2HLKzwWISU8FTrvySLK0b3WITCDcGPXeQFbA2B_VV6Zu-xgKrI3BC5W_Yfbz4uoSf9uBnUH4ASvxSHzY6LrImEi0qQgTNgExFtr2NQFRfEAhUpw7YZf2CLXzo4TlGBz_ddwHkoAxeQCaLtoR5Fs5kMMm46xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور آیت‌الله جنتی در مراسم تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/447464" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447463">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8044130594.mp4?token=YmRceDteYs44BYH44FC9ouFs3rwZ4jKBZhRu0IZnol41E6wV4gqLKnlNysN4vlutz_Fhmeejl230dDT_C7Qztd-q-n-CF4Y9nuITtUeNLcvNqeD2E2eeTg17RhcNbskVd8449S8tiq9M0tUHzg4OLGz6Af4ImrUBefaOQtGgTyIgoo7WcP0hUwWmdD52jRrOW9RuGdw2oEoTCOgNRSjVaS-kNdEkqyuccNLSVsm3_0rfH8LzNO-bU4Exa3vFyq5wkTu3IcbxHHN7guREliJDNqng3oY_i8YBwF4dpgxXMXdaLcGMrSx3tCRiWzB5SnR0rEl8J9sfKdL7a1WYU7yaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8044130594.mp4?token=YmRceDteYs44BYH44FC9ouFs3rwZ4jKBZhRu0IZnol41E6wV4gqLKnlNysN4vlutz_Fhmeejl230dDT_C7Qztd-q-n-CF4Y9nuITtUeNLcvNqeD2E2eeTg17RhcNbskVd8449S8tiq9M0tUHzg4OLGz6Af4ImrUBefaOQtGgTyIgoo7WcP0hUwWmdD52jRrOW9RuGdw2oEoTCOgNRSjVaS-kNdEkqyuccNLSVsm3_0rfH8LzNO-bU4Exa3vFyq5wkTu3IcbxHHN7guREliJDNqng3oY_i8YBwF4dpgxXMXdaLcGMrSx3tCRiWzB5SnR0rEl8J9sfKdL7a1WYU7yaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد لبیک و انتقام‌جویی مردم در وداع تاریخی با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/447463" target="_blank">📅 11:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447462">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8P1w_5UZ9_HsYDu4I1nSe9lUu4R8UUWkdsdr8Rgf5AkqEGT2L9ceij0NLmYBla8XKdusnR5SskDveESNCcwn47V2r_ARUqP9Y5fJXuGQNzx1SeVcmtEg7Pqqm5jgaRi3KTOznUJpDqjUtP6LJWee32uZB4XKHALiIoLYkpMot6z3TOiSyIxIrGVF3Odj6t4GzMXtYMrT6G40NfkLVxI6xZ-CqYWnR0ER6-x3dxvdkvYwev_VXuKru8rnBR7z9R2D5-j7Gm88B-VTAba8kRRMdUeF6PEcLPxa-SeqHNYq7EYGNq9KjUh_YFMj7XpD82owEo-9UmiIuCIg2_6viH1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور رئیس سازمان انرژی اتمی در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/447462" target="_blank">📅 11:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447461">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEhz7mo5igjcLTNHce5JdpWhIC70i4f_v12-dZszrbAK5RKQaBo1qnGUH2Ezs7kb4HEQxnWAO4veH7GIuTWRBzfRW9SnD8cpO1r_GAF_YYLiui1Q0hHturFuDzEIlOMqYqwR-rPQmKFqYmjn9oDWz3wFaMu2lF5TfG_uDnFPuxGkE1XlF40DNISmP4S8MEFwNyda88UBpGY45riC3JRSgSmrtPKVLGashHxFceMTO2eE32zEXZn61m6EO5DRPSTLWVKkkvGReF0YKfECTcNenawxEjXLrfHa9WfhD6Ay_tFOogX9-T4Zgjslk-ocGhu9rcGepnOtThWT528RLw6u8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شکوه حضور مردم از نگاه دوربین
🔸
اینجا خیابان آزادی تهران است.
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/447461" target="_blank">📅 11:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4ccb9859.mp4?token=Ur7LZXYXcqjZJp63sgJCQMaThO6N4TBZb8KFna0i-VfIU13NNqfQ9KNMdT5xXnerFCG1qQYVrawNJ_jHi6p_42KeGJabETVJHC72H0k3bxQM6zsUf9H_kh-E91mBYC55OxyjpFy7jxtgQqPWnkhJ5rdbI4OcoapbpaX88D-5jLmr42DtBm-fK7j9VCafM-2qLTIsQ7orZIwMJddahNdfy0V4ZgXE9ltbBKX-zDc6Goa8S75-ON2vuyIqoIMk3boTSt-oNYGK40s5s-vNXqkhU7Oop6AuqybewbTocRHmg_XiauhgirHSFGWAxHoTeAO1x4Co2r_gLjuZesf-IE1Ouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4ccb9859.mp4?token=Ur7LZXYXcqjZJp63sgJCQMaThO6N4TBZb8KFna0i-VfIU13NNqfQ9KNMdT5xXnerFCG1qQYVrawNJ_jHi6p_42KeGJabETVJHC72H0k3bxQM6zsUf9H_kh-E91mBYC55OxyjpFy7jxtgQqPWnkhJ5rdbI4OcoapbpaX88D-5jLmr42DtBm-fK7j9VCafM-2qLTIsQ7orZIwMJddahNdfy0V4ZgXE9ltbBKX-zDc6Goa8S75-ON2vuyIqoIMk3boTSt-oNYGK40s5s-vNXqkhU7Oop6AuqybewbTocRHmg_XiauhgirHSFGWAxHoTeAO1x4Co2r_gLjuZesf-IE1Ouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلباران پیکر مطهر امام مجاهد شهید در خیابان آزادی تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/447460" target="_blank">📅 11:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srSL2FPEkV0DUpya8LxeGGRo_yTzFeDmjGG62I7dyLsFbdE-rUTs0qFBtd8VH9vbqluCdtMqola4xhF-w04f_G9H26yTl4wZXLGb_RQ7clY0z3ANvSnFROdG4IXmhY1ybGDRzUD0yhjhwE_0aOR7Nh4yC1h4NylSxvvCCU6OzyOuacUTUdwR3NJ64u5-IIo6NLSkmtwpwg5kxV3Fbx-yAVZfPvopPO8iDxhclvoyXFJjx4LVPvTnk7_FFSoOyloLpJR0D0nAEEn26oHvbNgO22xUxHyUxhepdA45GFJRf68RUUFJAOYzQRwyD_4_NhI33QQ1LEeEBPQFDBFgvnLQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تدبیر جالب ستاد برگزاری برای جلوگیری از بروز حادثه در مجاورت کامیون حامل پیکر
🔹
انتظامات با استفاده از طناب و زنجیره انسانی، مانع ورود مردم به جلوی کامیون می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/447459" target="_blank">📅 11:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447458">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e634dea5c8.mp4?token=nwMvFtbt4ZV5VcR3XCoQRdvaCLyyjBzNu_Q6MIH--3N9qLHJssDXnKHzceKv17aFGU4JrMfCzvat_PmNZC8TNy30D2kyoNnImYBG8CJCfGUyA1Nf6sOLzxvggkYMn_lUMMJYNeu-TR6YxsXVOFwupOTut0cIbRwx4ZjOkR7TPXkERKap4P12raBofsA6Xa-sKN-yGidwb9zSjRPwISM4IoGlUzjWzzneFFVoNUio7wlcf6WlgLwYlJAWza7_rpssMC-kH9x-MUclueNKSP6devyxMQVfa9Q4s91GF-TkSGbEAJwQfo7bgfnvhKOjQC_WE68EoHenAyJplz2BjZyWzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e634dea5c8.mp4?token=nwMvFtbt4ZV5VcR3XCoQRdvaCLyyjBzNu_Q6MIH--3N9qLHJssDXnKHzceKv17aFGU4JrMfCzvat_PmNZC8TNy30D2kyoNnImYBG8CJCfGUyA1Nf6sOLzxvggkYMn_lUMMJYNeu-TR6YxsXVOFwupOTut0cIbRwx4ZjOkR7TPXkERKap4P12raBofsA6Xa-sKN-yGidwb9zSjRPwISM4IoGlUzjWzzneFFVoNUio7wlcf6WlgLwYlJAWza7_rpssMC-kH9x-MUclueNKSP6devyxMQVfa9Q4s91GF-TkSGbEAJwQfo7bgfnvhKOjQC_WE68EoHenAyJplz2BjZyWzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید آوینی اگر امروز بین ما بود...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/447458" target="_blank">📅 11:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447457">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u089UYvAZX_XOLEnq0Eg9rIpwXKrtIDDe6tfUb_D-_JV6ZvqRFj_fZbh39fnqTSeq8NBGTKT3ySYLAxlXp46H8LKMsjJ_4KXjLjJrEnUcXDKv7vkPdljf8w0NGex_lKDp6dLozsfMSPK5d--60mo3kiDUsdl8EAc-NZhfThLOfALtK3G17fPrhuR8vUJgfr0ZIyOrrHhWZ5CQ9rf71RBUycUiUR8KPb1RII80OMhNKoQ3MFC0EpP1AJqsQhctny3adXYe3wxxC-s2nvcLkf4qceM0HtrsK4F2unZRfPnQ65GtedDVxvXE8Nu9rPL1hbmXLrdMSZ00oKw85ibx8qSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: رهبری شهید به همگان آموخت که بزرگ‌ترین سرمایه ایران، مردم و وحدت آنان است.
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/447457" target="_blank">📅 10:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447456">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a0deb299.mp4?token=mIfJSkE5wc45de2LVCWVSWsndGm7vjF2ThAm35LwAJV8JwkssGSEafAKVcH7M6FQ2A4x-gKpN5WSOGKw98w7f1lUmrTlnszD3lucy4pztx-NipySU3qxbR2LnXMoJvUdRczmyeULr4dDiEeiDxexaTx5Ybg0w2Ojlcbayb4lVqPyqRShDh8HnWjKl03qhlpcma4A8uZGXCsjq6ZgFRVh7TDMkmV1W0XOavMq-rEAAOU9oACVg1Jf1D10JVbsqGM9OStlBZVH9_kvI2AYHnyeSOPNkxifdVCffGk2FbJTIeRKyvg8ia_-HmrhY0PjL62YmCwKi1Auw7BGsZXQcLgg2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a0deb299.mp4?token=mIfJSkE5wc45de2LVCWVSWsndGm7vjF2ThAm35LwAJV8JwkssGSEafAKVcH7M6FQ2A4x-gKpN5WSOGKw98w7f1lUmrTlnszD3lucy4pztx-NipySU3qxbR2LnXMoJvUdRczmyeULr4dDiEeiDxexaTx5Ybg0w2Ojlcbayb4lVqPyqRShDh8HnWjKl03qhlpcma4A8uZGXCsjq6ZgFRVh7TDMkmV1W0XOavMq-rEAAOU9oACVg1Jf1D10JVbsqGM9OStlBZVH9_kvI2AYHnyeSOPNkxifdVCffGk2FbJTIeRKyvg8ia_-HmrhY0PjL62YmCwKi1Auw7BGsZXQcLgg2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ میلیون سفر با مترو در کمتر از ۲ ساعت
🔹
همزمان با آغاز مراسم تشییع رهبر شهید انقلاب، در کمتر از ۲ ساعت، یک میلیون و ۹۷۲ هزار و ۳۲۸ سفر با متروی تهران انجام شد.
🔸
به‌دلیل ازدحام جمعیت، ایستگاه‌های میدان انقلاب اسلامی، تئاتر شهر، دروازه دولت، فردوسی، امام حسین(ع)، توحید و شادمان موقتاً تعطیل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/447456" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRO2f_0qLCbZ7NBdDbEa6Ib5Z17ROFd9yd2SDMU5aoUnzVeJJRvjq5Mv6HJOIYTCJBGi7KMlhbUU-ndKmdVVMzFXH28MreojNigj_iI8WMH-RYMJsSufA_z3sG00fzcAFdqtQApBl8TEq_drK8UgT8mYYdNwz0PypPbGmbMj8Vvr7rJjRXynBIdNXHpT1uhyncKF7W4sSQZtvoimmzp0uKAIpfePaihidWgXC4oxRhzsT3BLEU0y9lHDf_3TZj8_-yMbdzSH5zu723ogiMmrAakFRxDRqOhZnQJmlFEeVZ7Hk1jABnqEgeAXd_-eR094UM635jHNFjE67e7WlJ4Agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMwXczyXnMka_dK-P2p9Qih_F8hKdTK1e43f20pk3ja2uf6vWZFGTJVsRMoDzYTAd8QHoXhjBSTPONC_EVTEzQrdKNHF6NWg4UFuVoFExO-w3N1U_Jbr-i8ZeQmfGVL9m-b-8JH6vx9XpSGGzzzSs4H_nE3eR14B9QjiNOXaAhmxNB02nFC6k9ROFkv-SD3Pp1QslPZA5RU8xflW1bzvgWQQ-9naT5ni5VSNU0naKNnXijcya69ocp9xl30F07BSweoaglv11L1UqcWYwDenvOgrvOXAIUwiTnMSlVSGFvsrlygbAzpXON3s9KGJbJJftsq1s3Rt7AV58haTvocdxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جمعیت پرشور مردم در بدرقهٔ رهبر مجاهد ایران در خیابان آزادی
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/447454" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447453">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEDeSSPI-6mGEoOVPX9PCZmZOPwdrGPaa4fDnyE3LuEh3VSewFdQUT7OZtTK-eJD0I6lXPOf1D_MEpNk28ES9t72JnMRlnwzvB6h1XrkGml5tRKYAEVcNVKo5Wk9LuoQL4PCMl_cJruzPqdrChtw1eUwiAm9QDWrhLo-mW2zdpa7_qh5H7sdIIlhwmYE0dhyLhQISfksoxRvE1Svc71Y5rynGYZkQAoiDzjvvbCJtB6zp61UAx4UAr066IfyJM8p4hc7k3uzLgm6KF4KOBxLE3BoZS8PU9pViCkZPv-9LQlYXBMus1nYBtnTma1FDjqt-VYKOXmCn2LaLzB_l12qnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور جهانگیری در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/447453" target="_blank">📅 10:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447452">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRavWUQqj8jKhVeTSeyvM4aMO6rftVX4IO4qiyczXMQDFuzPxOqXGshpln5oSfd5Zg2f1KD7coxn4Qq-JL-F30LkAmm8JEFIM8k0sWGYqqid1tznqXqTYfEChV1QdAvi-cR_W53KzUFTODCSRXsP3g8G7Hmw-JV3atANG7mo8rIdzv8f8XMk1BixTyly5S5BTVXMGqYEBjHMxC6RTpOO7WjyNfgWep3_QUJJyF6a4yjtUh0LdY1on0LxOe45WVULByrmfBg6uaRLVioHRrA5ySUqQl1lSQVyBgRY2XSqSRg-ovq4k8p34dXXXBMpsLHBi-nZoBOEVgy9hjJO0Wbxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برپایی ۲۰ مرکز خدمت‌رسانی همراه اول در مسیر بدرقه رهبر شهید انقلاب
🔹
همراه اول همزمان با آیین بدرقه رهبر شهید انقلاب، با ۲۰ مرکز سیار در مسیر مراسم، آماده ارائه خدمات ارتباطی و رفاهی به عزاداران است.
🔹
این مراکز با هدف تسهیل دسترسی شهروندان به خدمات ارتباطی، در نقاط مختلف مسیر مراسم شامل مسیرهای شمالی و جنوبی میدان آزادی، تقاطع آذربایجان، خیابان شادمان، خیابان خوش، میدان توحید، میدان انقلاب، چهارراه ولیعصر، خیابان حافظ، میدان فردوسی، پیچ شمیران و میدان امام حسین(ع) مستقر شده‌اند.
🔹
این ۲۰ مرکز با پشتیبانی ۱۰ مرکز دیگر، خدماتی نظیر اطلاع‌رسانی، مدیریت سیم‌کارت، راه‌اندازی سرویس‌ها، شارژ، پاسخگویی و رفع مشکلات ارتباطی مشترکان را ارائه می‌دهند.
http://mci.ir/-NJ1Z7C
@mcinews</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/447452" target="_blank">📅 10:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447451">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx9EWW0xrz5oZ3ZoQDRsE4LlBvHrIWalLcmEoz6-NYXB49VhwU9elVdw5Hs0D2RUr-JCus5-lUoE4dQqkiT4Udog9biOrWLGZBkXsXrn_VHVS1VO-T-XoeXEC3pEL4jTlk8OR4Em4zKJgvMneNxteSHndfhXdWSFYlQr0C8fCXcVACm7rkzbg3nnUQyaI1lRertkP0u4A-hbUr3tvNaTBmSRAtNv_1aLnPDMfpECoyKooWlyOl2qD-VmpW6Uwg95CNWYILjGC7E-R-ZyuYvDjiaSMUxdI8YjQRBj3N62VU82x4B0P0ZyboZQ3GjLmZTUw8G4WJ-y8NA-jCx2u2CPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/447451" target="_blank">📅 10:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447450">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/447450" target="_blank">📅 10:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447449">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544f106e.mp4?token=hExuS86_oftydPT9FfW_7hY36WaLY7Vp57Yo-i983oUGFq8bo4E5psj8rm8AjCVNbjAiHLITH73DtugecqzM7f5bclzjNZ0mfJml5K9_tb7srAblxczbxGwn3nIAhUIexF-5wWuAV0rMj2kBOtqdcxPUpGDqNMvP_3bq6v21cNQmmOIJp9_Vjm3JWraLgV_ZYYtgsOuNMtgsjhxfTejB5lGfX8rnCKqZ1ieMy1MPLfHiHNu5GBPDsBuJ5xNfIcjaPWFqVs3LGR_cvGEf66WZvwd22Nc6MdrcUzWjqg_i01HrbiKuyXmh48q5x9_yl-9gq4oiP0zUVK4HF8ZasgYRnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544f106e.mp4?token=hExuS86_oftydPT9FfW_7hY36WaLY7Vp57Yo-i983oUGFq8bo4E5psj8rm8AjCVNbjAiHLITH73DtugecqzM7f5bclzjNZ0mfJml5K9_tb7srAblxczbxGwn3nIAhUIexF-5wWuAV0rMj2kBOtqdcxPUpGDqNMvP_3bq6v21cNQmmOIJp9_Vjm3JWraLgV_ZYYtgsOuNMtgsjhxfTejB5lGfX8rnCKqZ1ieMy1MPLfHiHNu5GBPDsBuJ5xNfIcjaPWFqVs3LGR_cvGEf66WZvwd22Nc6MdrcUzWjqg_i01HrbiKuyXmh48q5x9_yl-9gq4oiP0zUVK4HF8ZasgYRnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در میدان آزادی، منتظر آخرین دیدار با آقای شهید ایران
@Farspolitics</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/447449" target="_blank">📅 10:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447448">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW-TdWJB4fulpI0DX6W79TMqQFCyznjUWXmRcREY6e_88KKm9OtFBUW0tKPD6bKR2IBGrOZl11cCL-AUCzoGw6ST94bYLe8ZiX4AifU6L6Gx4GWWpEJoWzuHkbsOOUK2dvF-Nh5wVJSP2ucbS_qbQANNANTmBfvDpaiZ9qoAHjKjefrB8mR6uKIXnGLADRmV2Oi7nPU4jlU09wUAIqLzcBzW8_GAhwPgYHouRxDDAWWzmameqIEAiM6dsxZrn7WmQdjmAzq4eFUWgmPEPUzjaOSvlQdePyCsQRKnvgXMI9eyz_jpFWujm1o9V44XxSnc8DXzUNK4klXewEmG_gQGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تشییع امروز آغاز حرکت یک امت داغدار است
🔹
دست‌نوشتهٔ مردم در بدرقهٔ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/447448" target="_blank">📅 10:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447447">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCCpbGf__RjhbLrRYYgKIiLLkNCo0nIT4SZLMG-5dE7tnuE_U5IPiY5YPIjA1w6HKkLE6XlQ299OxdmmBH59p7avdKUDEZJZE9-7nKXr-X9zGOiBJ1W4xyh5iDrxBrCZ7S7zZ6eYgYFc8eZeiZBAuP9ZrE2jOEtDDoHAH9VXrEdajxw1dim14N6k2c7uHk8YAca8r6ldn4djuKb-iVgbv20Y0dwaT_AXH8xQzHeCaM1TFFqaIQW1Wh-AEGlho3bWxhJh6-aP_yfRKjB64coFp612XE7YzAbZ5cpMb9ok8V9lDrC3qhukZEgkNI9Sq5wGMbRtHh0clzr1Xnq-y2MUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور احمدی‌نژاد در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/447447" target="_blank">📅 10:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447446">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caMSeZPIe7tl4-WY3KSZ8Knia1742a-Ffnt8F6vhU5ZCTIKKYoP_h3wSIt1Hdnc-1PteNTJKJ6_ek6gE7gWIUZH2cNUAfrvDayS1vYC8deppRnHWtK37nv7GC802BLILG9CZQlzLlkA87pDzyoPkdL-LX_OyAnayNIAeOq7KquvHFiCGpWg4dQQO8u33p0Q3LzEmx-61oPlqlmyMLvaYe7PzX-2Yc_zRLawv9-7_2UXbmuDW5hz2CjQODFdDFCAQqrI_CdkUDuBXECBBFe_1GB-jSgJq3ZkmnTE1gAxNaJGNAEwi6VbWQ4gQzHeQCyESJwRDldakVhjNJZxuIPHr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف ‏خودروی حامل پیکر مطهر رهبر شهید انقلاب در میدان آزادی
🔹
سخنگوی ستاد تشییع رهبر شهید انقلاب: ‏خودروی حامل پیکر مطهر رهبر شهید انقلاب، به‌دلیل ابراز محبت و ارادت گستردهٔ دلدادگان و عاشقان امام‌ مجاهد شهیدمان در میدان آزادی متوقف شده است.
🔹
مردم عزیز عزادار میتوانند از مسیرهای اعلام‌شده خود را به کاروان شهدا در میدان آزادی برسانند.
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/447446" target="_blank">📅 10:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447444">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a768e4b8.mp4?token=hM5sG6bMN2LGOXa5z10md49jbB19NQexusSXMcjA1vhUEUwNH_4Bn4382RlsqVeiwyVLLTXnBOCCUqsHq2UdXQZ_Wpem5fAAKAL6iGF-zipuGTBvlJ_KiaTKf3Zo7Roo781908FSR0aeX8yy__lYzrhxmrn8qQU9ZSm0Tt4lMvg6Rr2CLAEsrt_hNCct41IwUy9VoInMEjIb93I4vBBgU7clZhhy-Tv3q9gVAVjREcdP-NTGZ3F58svMP-B_9e1WbrOr823-briC4iYU3xq5G4ThfHdr6_QqbD5fwvSVkyPCf4pFEVQLIoOjqtjWJ9AfRgJdTohjsJdpmUEeZgd-44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a768e4b8.mp4?token=hM5sG6bMN2LGOXa5z10md49jbB19NQexusSXMcjA1vhUEUwNH_4Bn4382RlsqVeiwyVLLTXnBOCCUqsHq2UdXQZ_Wpem5fAAKAL6iGF-zipuGTBvlJ_KiaTKf3Zo7Roo781908FSR0aeX8yy__lYzrhxmrn8qQU9ZSm0Tt4lMvg6Rr2CLAEsrt_hNCct41IwUy9VoInMEjIb93I4vBBgU7clZhhy-Tv3q9gVAVjREcdP-NTGZ3F58svMP-B_9e1WbrOr823-briC4iYU3xq5G4ThfHdr6_QqbD5fwvSVkyPCf4pFEVQLIoOjqtjWJ9AfRgJdTohjsJdpmUEeZgd-44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسهٔ حضور زائران در بدرقهٔ قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/447444" target="_blank">📅 10:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447443">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0171cd7cfa.mp4?token=F7RidnSeMGL__-uwrxqLCDL0e4hJQbC9e3l-i5IWEum3Y-Cevsp2tvOLdTBpKe4bP7hnCNumFXhRXKkq5g6t-xgk2HqfLg8QXnEyMZ-YICyy-6MGnhzVs1aRGK3OyUhayOylsTJiLZTkAs9wHiQvn696LFnRHZzxKQ6CoZ9NBwGeeIGPdrDxs_jcIWTUs_NvvAjiMNyNV37g8MKSw7SWiiyIGC0Jl0rM9uw-HTF64GRJrTgkp-yWnYiwCE0aI9rRtS2txDapdszt2yEluLop_ow13cppsADSUZtGXqwuxiYtIHNlhro6TCzduk0XavHzo_ZwWR27w5Rhjmq4o_djpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0171cd7cfa.mp4?token=F7RidnSeMGL__-uwrxqLCDL0e4hJQbC9e3l-i5IWEum3Y-Cevsp2tvOLdTBpKe4bP7hnCNumFXhRXKkq5g6t-xgk2HqfLg8QXnEyMZ-YICyy-6MGnhzVs1aRGK3OyUhayOylsTJiLZTkAs9wHiQvn696LFnRHZzxKQ6CoZ9NBwGeeIGPdrDxs_jcIWTUs_NvvAjiMNyNV37g8MKSw7SWiiyIGC0Jl0rM9uw-HTF64GRJrTgkp-yWnYiwCE0aI9rRtS2txDapdszt2yEluLop_ow13cppsADSUZtGXqwuxiYtIHNlhro6TCzduk0XavHzo_ZwWR27w5Rhjmq4o_djpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت از میدان امام حسین در حال حرکت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/447443" target="_blank">📅 10:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447436">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O52iqktQtAOHMLOoW2jJVHHAOa2pnOJYs5-_vxhqEG2liGiZN8jM9ESdNbjRdum-mSo6f6aRKz30_-JTsN2QQE42zI6jvpxGSdiA_JkqJ6CX8uVHpWS0bDoaGkD0bktwlSKM-gh7Gh8_wqBnR95T6Mm0G5GIad98ELvU5cu87AqHOL2CVEbLAwLzWWAUs4eRjmd61qNt-pYAeyRqQoFSvNje_SeYSye4k3nvG2bSA2dI7Yvla-pL37rVfBXnVjtOPW9G-zEQUv9I0BhrOzORfvCDlwlam7RCqSWIK4gWC7k5EJmp9Qn8SV0feBvzsbTpnKnHCFFQeqfL2NXRmWd-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aebaj0fE20YW-62dd8B_-nzWE6ITqTjRQXg-dYQDoCtMoN-EAbbJJ55L0JFKjoWmMomKjXLEDD_nQw9qJuT26YddKr50xUsLS0yJxvvEeVdr5VCqQIXpA-WKlYKqrLL6vRJHKha2ndoxFxSXpkPyO1SMFXzoIvIWdZGYR06VghfAA8Ukxe83x9v_k4bXDecY2MxjgaSXp6zxko9p5A2ih551vO2OiXbVNrHzQk3-EtCl-7nEuTecAvFPpg0jXZVThCXa40XlAJ724Kv16FPqCFAJN9ovnkcvr5Ix0USAgjA5lqUJYxD6J6lOoExenvvI3GDnnRxFUO9jrjcgRYr2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTOd7svqIHlWsBRoalPT_VTJOn6MiKiIhsRY5umNX1t1ED_rIDhSr9vudKdX8A4ISKO2ufosbp1AJWA8LubLSpXYcG6yprsZKZVCei828NhROpG-7l8HcgaXEos-QFGQzHYd8MZubQJdBoeJ-XLjNO1ExoJnZojQz3LtJA0NCJbbeeaxt9y_fBwroLrHGvgTnhBAGmw3sKfzQPv2rEB2dqDDAmWn0q7xyjJXzRmwzhfzNIwJHe8OQQSBct-O0aDT2bjbwhCa1HqXCVC2FRdmXGDPzXY-CFLyXNiUiElzdqgds_moQNhD2H54Xk6ksjTIm2fs7Va98hvxnA5V4Kwk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SP4mxxKjkx_swky5D6njLyFAc4X65-atQJ-yg2NL7b8iMCgPVzvHK1_URv8L_LB3fvZD4rgEcLrorrMyRCkP1pnRQrRMgpiqS68g5CmeUxKnuTG-fI0l2qWDBVWqQYzP9Z0rMHXobNT7FCRcLOGM6XI5JtB0DX6WzrszHpPFcU248Pe7Ia8fW-1-WaOD-QctgytSfnnYvI4GO_sn-vCFJMrPajAEm-fB5j0grYemf2nq-t_Vfj28DwtKfCFS8esmZIF7VwkdqNjQ4nMfGcqYQv3aMmgLpgtV9TE9nghhyb-7PifYygL0jIkChSTQnHaeCTgNHaZkzo94RnKGRE8B2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlqx8ysGlxNHrZsePBQOPLkETdsHXU4mvoeCYperrtKgR6JUYUUASvhU_aPRRAO1Si5WyxU4w6lxkMQGRDKtsXg4MjbihelM-ktuUQ6f0yNSWt8hWQdM5QUrEyGW10M2SYdrDKnU8y0le8rqu4JOmA53azJn38rttXyqXsmtBM4072S1UtG-NxPmVuFkkWjnmcoISYcot0musrpuEX8C6ykZGCU93oZFCsdvVBpkdFc28jr-p24fMVs8CFMlFPF0IruwAT_m8ZVQpCjnIuv6Kf6b2CbgJ7R1bk2BF15IpC_ZBsl4_au8JAWnhO7SHfgFoTJhv9Qs4SnW_97LuDuPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmaZmSelW7z4zuwkfBvRLmkLxzpwaJeHDQbloQ75nuVUKYoaXYMjoDUquZUF4Mk2edEwpKoBcwQviElzijn49cGwaFaASZHwMNFKraJ48zDbeRIG2iy3aEHueQff62NtorCmreRn5B8zy2gCrQYP-Zzcz1FfuMi7u3YluhlffjhC9DsxkOhvi2iw162irBbhkOo7nvD6hkSLTDUXXgGAMMAgfPuK_2lHQqDYc7wCnAv2mBBltDraDXwM-FXmcOdpHRVH7GKrfeyIGv0EjfJmsRUkRauyzhKo3UXW-HmRD01ocCdDws-6nBMwnIPRg1aITWRe5EshhO3iarWyqxvXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mabCx6ADLdBYmIELySonCRbXZA9m5dFH9NbnBi7vGlKR6sEZBkgC08vnivBeoCB2igNV6Tn2pOgrsrm-fZetoWc4ruG8cD-cV4IvW2tBEiotEAffLXJ-UrZzvW82BopKevLtr8XLYdDMEVJ4sRP28iRzzBJxhnFZiKq9Nv8ezKY_im9k2fvpfBry03KQP7Nn_PT9fyhjne5s4RcECwNR8ZxBVwx7jQ-XFBxPbtUKo6PJT3VpCyj8oj5KUhGE_N8ikvAnODTyvPCPN4q9y6k43_txE2VR7SgK44w_mDR0J-OWOSF7SL_4QfXaYuNO3xMt2j8bHvsp_T8GkpKoWkN0vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هم‌اکنون؛ تصاویر هوایی از حضور جمعیت عظیم مردم تهران در تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/447436" target="_blank">📅 10:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447435">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8004c00f8.mp4?token=lRjVAHMuBfO0t8fXj44ZHbGWLj7C4VllBMY8AGHGloa5rrL2ReGkXtoQR4tDdoAu7D3b4cUtL7I_IO2KiIvBf2DGZweIDPspHWDk-N6igKdhHXf4FABcg4pT0XRxJLZb8HfHvX9O660uvNMqmW9wiRAxg9iH14VMe6WqOWwZ_1h-sjD3Hzjr_0VIT4Ds3JalUvUKUXp4N0KRH3S2JIprlkG6waHhaNfbdKienHgmBstXw12fNVr26hrrzWSwQkqz3IyJ8jPjbju_HFcni2PSjRhAqN1bC_Xngq64Ss-1V1dttIHAkjFxLWjvD6vOcwnRmZVBfP8BRAeWPVDc7Z3cig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8004c00f8.mp4?token=lRjVAHMuBfO0t8fXj44ZHbGWLj7C4VllBMY8AGHGloa5rrL2ReGkXtoQR4tDdoAu7D3b4cUtL7I_IO2KiIvBf2DGZweIDPspHWDk-N6igKdhHXf4FABcg4pT0XRxJLZb8HfHvX9O660uvNMqmW9wiRAxg9iH14VMe6WqOWwZ_1h-sjD3Hzjr_0VIT4Ds3JalUvUKUXp4N0KRH3S2JIprlkG6waHhaNfbdKienHgmBstXw12fNVr26hrrzWSwQkqz3IyJ8jPjbju_HFcni2PSjRhAqN1bC_Xngq64Ss-1V1dttIHAkjFxLWjvD6vOcwnRmZVBfP8BRAeWPVDc7Z3cig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش جمعیت در تقاطع بزرگراه یادگار امام و خیابان آزادی
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/447435" target="_blank">📅 10:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447434">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9910a7d906.mp4?token=NtgbMRYnQ7FyphQ4CYRIH_e7pGWgiFc4fk6PYBEDroOeYDiysj9pLvqZGiJEtWcXP_07TfmyDdmYrCHe7Lr9j-XwbQseC1xJD999vXNlH6CwHxjlKbfuKdmMm3pcVXzMwLRnlzx2LXYNhprSttWCCpPxaVT0iilNwNF3UuXGEgF1jP_U8Bjf0reXVtId4WgPAYtiTJfhkdxJJp9l1DB08j5qG7oSoNrpA5JH5EIp9gYFgwZceWaiw0JpNzJK_4m10qgQtKiP_mjCVdZDUIaMhTYBOhHu265OwqQAk8qUoaCWi1ftpokmtD_RfnL2rYgciZRUXw6AFPJePQBWyCPi_Ylqy_ArE_1LxXcAi6SRM9AfvUA4yWrYNLd428vgb6Tmt2NYdN_yPiTzeRMl3fafI2sTx38uT2heNL_WIs7stTTJUaZP97Qplu18IlBuj42hjyGLXnUnWpaKzY9NkaIwtZGhAtSejoehZOLfsltjnR68xqbBkD_zEZ8CHveYF24RMGahWAGAztqb6WKUeH6moUsWXnzxCc2y4nAQ1g76MmvV4x6uVBT6LKVVUqnxofAls_fwz8_HIhI6Qtf-PUo9olNRwnwshEFfPrDIflEAFHeC4AUWfrFbildpwm378owZI6CxeA992HgxKYJ61BtxaPn2J65Q4N6rZCkPEEONJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9910a7d906.mp4?token=NtgbMRYnQ7FyphQ4CYRIH_e7pGWgiFc4fk6PYBEDroOeYDiysj9pLvqZGiJEtWcXP_07TfmyDdmYrCHe7Lr9j-XwbQseC1xJD999vXNlH6CwHxjlKbfuKdmMm3pcVXzMwLRnlzx2LXYNhprSttWCCpPxaVT0iilNwNF3UuXGEgF1jP_U8Bjf0reXVtId4WgPAYtiTJfhkdxJJp9l1DB08j5qG7oSoNrpA5JH5EIp9gYFgwZceWaiw0JpNzJK_4m10qgQtKiP_mjCVdZDUIaMhTYBOhHu265OwqQAk8qUoaCWi1ftpokmtD_RfnL2rYgciZRUXw6AFPJePQBWyCPi_Ylqy_ArE_1LxXcAi6SRM9AfvUA4yWrYNLd428vgb6Tmt2NYdN_yPiTzeRMl3fafI2sTx38uT2heNL_WIs7stTTJUaZP97Qplu18IlBuj42hjyGLXnUnWpaKzY9NkaIwtZGhAtSejoehZOLfsltjnR68xqbBkD_zEZ8CHveYF24RMGahWAGAztqb6WKUeH6moUsWXnzxCc2y4nAQ1g76MmvV4x6uVBT6LKVVUqnxofAls_fwz8_HIhI6Qtf-PUo9olNRwnwshEFfPrDIflEAFHeC4AUWfrFbildpwm378owZI6CxeA992HgxKYJ61BtxaPn2J65Q4N6rZCkPEEONJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی رهبر شهید؛ مهم‌ترین مطالبهٔ مردم در روز وداع
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/447434" target="_blank">📅 10:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447433">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
پل کالج تابه‌حال چنین جمعیتی ندیده بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/447433" target="_blank">📅 10:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447431">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4bd5f908.mp4?token=lGIU65J3qQM7E4ENCrT5XA_zMUQ89vXGect_l4EvaQHfCGDBWwjXacU7CqXJN9BirNfnnhSTegJVDo40CGsauNNZLPnhVcjp8jhgKGsTYxipSchLmxucAi-p9e5UOVisYoN7Ps98O10pJ4AOOE_maHwz-RKGpKdmVpa7_LnGx6Z9g-dfb8UVyCx3OvNDlR5AuRAT4AigB0IWhDqGwKucYXZxJP_lVItjt5PoW6ixMPvWlz2xIRm46sTzXfdRe6jKVhdQqNJdpXu4UHMmwMsd5cLSd5DxBaIakPGGYWQWDFgRA7el_8qOX-yflFP6u5gha4ZaKwlnQqJRpMl5ib90NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4bd5f908.mp4?token=lGIU65J3qQM7E4ENCrT5XA_zMUQ89vXGect_l4EvaQHfCGDBWwjXacU7CqXJN9BirNfnnhSTegJVDo40CGsauNNZLPnhVcjp8jhgKGsTYxipSchLmxucAi-p9e5UOVisYoN7Ps98O10pJ4AOOE_maHwz-RKGpKdmVpa7_LnGx6Z9g-dfb8UVyCx3OvNDlR5AuRAT4AigB0IWhDqGwKucYXZxJP_lVItjt5PoW6ixMPvWlz2xIRm46sTzXfdRe6jKVhdQqNJdpXu4UHMmwMsd5cLSd5DxBaIakPGGYWQWDFgRA7el_8qOX-yflFP6u5gha4ZaKwlnQqJRpMl5ib90NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در تشییع آقای شهید ایران به شیطان بزرگ سنگ زدند و عکسش را پاره کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/447431" target="_blank">📅 10:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447430">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGmJ9NMocxU87oVTG5d-B-ffwpzvAubt2DXPIO3a-QPYzipBPrdSpHDGXDTPrsATEIFUBTEJhIL7NkKEmWF0l9g05iwaOwreOszW1WlnMXA0OsDEoVPAiHO-rWniJ8ZdSz8gnRuwC2X7yXgLaAw-Ml2TgOAlBbug2YNSUh6SDh66fCBINVthI5NnScJPnAGeeSBfSOgeJZE7bBTBS57c8bWUNhe4yyWUR6u0PH5J1ndptlslG2E-kZz8-7DsxsQJc4A8UoGfFFZ696yVITy66LREv78w8jCgHE4byVGb42ncTgPtKagNX7T22uhPW8Ve72sk9RYCAzcKHJZG1z69_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور رئیس قوه‌قضائیه در تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/447430" target="_blank">📅 09:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447423">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgXN_1oxTxoGqIFhrW0m9CaC2IwiHPTmIB4WEldJGE_RScIGsEm6jaWjekqggMYRIDS-cx0KeoC22GxKJBy7hBG0DbPiZX9KU_Je7V-dFXpZGR6KfmlC12TYQE-g_Ao5RXEv6FYHcxSU_LdNLVwfwkaTfwtLsVRXmHgcaj34m__0xzKWcZwEw9hGHK5HBKfsFSldMUi771EJW8VWnGdH_ieW1wXj1A7N6axloCH16f_w81ZC5iwknvTUq_S5s3SnJI-CerUCTVtiUsg6H5VEfhlGaJY_jsrY6ivywme1OTqcr3zbpw5AjxExuw5Yaz-kyDvsB5uADkfxAaHIVUGHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzcLn8B3_Jf9ismmDBo5A3h5Dz7ErTs-HDAaEWHNCYy6ndz5VeyCDPn5Y7cbdECAEyABs8Sqw2doUWAsaJQdpqJ5n9ikelVkoAQitMAIofRiaIrE2kDsgYEMzKueoqtddUUva8L75jefWFllLOEeD_SOqJMcSDHrPGzae-Aak7phPDM6WCij9D6u6uHfT5sMqhOs_aFrjMm-uSbssewxDPWNc0ZCbIGiCAAZa4mm0ETS6KwysnXNycR4NDRpe5KRQVJrLTzAqqKKlgm409G9yabrWU2mk-MqYlPC2Y-Ju_kOlVWoOFa63VP25-ayTloT6Du_kwhj3g2TvAFASbaxNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbpRBlwzA8ov7UV6wx1zs02TB_4U64k69iRCrUFHlWt4XwByamK16_k7M5_OTC63URFKw5WUYiDDQv8Jg8J1iQdHj-EOX1wZkpTlkekjkWi4tvi1bifmrz8elerHiVnuuw66SKOA38Cvqju6sTmv7FDAmfRcJi4bpZASPbEaCttpcfVzmd1iufdeSlYnwjUR_4EEIav1jPR2vQdUU58Ry8MPrC9dBMJ4j-v1zZEqWu0yBJA4uilFRUBdd6pZZk9mf5MNHgTikn1BoblIueM_qOVAl9tRCbmvzierhlpFRfDsPEYZ-qd_Uc0E30d9A1NHWVE-sJrRUl4qjP2_Qfi4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1a_geiZ4Gm2ubQ6uQGjmRhfyVhr3ZJpnKY54Lq67lb6BLjX3OKmqBx6clrRK3jIwYAgVN30a9Geo4r0DB-snaNHJcJaGI4pCTmUg6HEd8qJ0ILoTDtYU7JvOEiOmGPpa0P0OBd0JGHAOQVXf-sDTmhaSS61r-cokR8ZX0B1aXet3tw0qnsf0I7sIEg_zi4UBCmGnOlnfFjZXjalEnlcNycjWzTVAoNGbR1BjbmDyPZFU106MCJUpO76FZ7bo4wFwHkxGKjzo3c-Yad-G_lXuoxtNZoBUc6eE-aXpVoqcVGStt1Vx5Y-F6fTROxFj-07HztXmRBOVej_wxydJ0tTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iM4C1HAA0FoFnjv-ewAhh_RR3JHPCJmIqa9-JC4Arw93YARLJ2tiM9mB5eVnhV3rYoQrmrY5wNJvZTmDaeAfyoEogD7PiNsOudZSFZH-Iikoo57cSA81qo1ZLImvo3FlhXEdahCthH0wfboYw3UiyQQChOp-Dd9iOmRZHPUfSEGhTf4H8PFDPXib-vR9n5_z43T6whwNqqzixqQ6wKqjbsTNC_TPwvB0TDcs4tW1qfj-bgFAv1RytaADlqx2temOkYqKvVDyeMQydpthQ7QOaf_-kIB7j4d6vsTSM3RkS3MZJEf0T8Bq564t5FnTVN5aOP_JTSdhSBFIeUh1xssPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gknY75nG8u0F4jc30GDKFF26BYy_Owz0tE3gm0tMGkPl3ULrtQgfGrwl44hJP1pqJlglJb9wJyES-zcRucPvBOAi3cE1LEdAGDjOqOmcxbqsn99_Cu1z8RqAfZ6KC2-jqOb7CPd_fgkwhgdOtECLoaBZI16B_5Dt2cCuDOyk4bPrCeyemPJT1n5CJDoNFUSBBKYapqGkTNhD7c7a5GK9L5kda7jpX7bioNTYALj4lANVU0mSdWU5P7IAXLBYibTl14gR22O3wbyVfVw2MzPXjhQn2BrFYLiLAghUv1z8OoV9uTVYfUwEbhKI2Y5KI9BeLLWvOgblMt0SFht5tIk0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXaGE0vQ4J4iB0eOE5uKYiwjwlQLGbAwG0YmjZePJ9OUpjRb11nI3SdUN3vRPCH1kqWPa98zogFzu5-w-UneRseZq_tFR2MlvNq9gRKOEr66y5ee0eeN9AyD2fVAGjysh1DlsP4OCcVu2eEdOd-2hulWkm-MYhI8zC_LSjsvpibTurKEAIeZbDSGuO07RKq9UReN2BE6in7Wn47Z6Nb8vRdCXUbqiEDWbeZ0IcY7hmtiOzOjs-COSI-Y9Phc2OU_bwk9kihk5JqBH-B7lHJ3iGqWduD3k1AsBATTrcnwApTbzC3ijMpFqcteYHB5wOPWn6f-lYsQMLCS2eakBdS-Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میدان فردوسی سرریز از جمعیت شد
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/447423" target="_blank">📅 09:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447415">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a28b7dd526.mp4?token=Zwb_qslcJPKt1F_YsL7IuTnPLLpj2pJGxiXjJ1PyBPGOA3faiQt-zCGY3rG7zN6IFs3uCRX9FIp5pCfbkF7Mz-3KujeF6QYTfR8MZ8VvK_DVNzxtd-Va2TS28xPQZRwPa3Lz787120Urc1Ezzi2rQt0LWZ-KFkKFWtZl_tSze8ZbnKACOmS9AZL6rDNoe0Y7Wo35B1KX7NQjjURpL6BiHJokbatAI51q4iKDdLL4nEvC8PoZslIQnOzwuY7V2zlEpm4NKfEUJhXkt7zBsvdoeifSKAxFws3knCr5qy0QsunueRdKPKOVqLC1FRkH08RYdHS3kj9djDtPU0UiQmtJ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a28b7dd526.mp4?token=Zwb_qslcJPKt1F_YsL7IuTnPLLpj2pJGxiXjJ1PyBPGOA3faiQt-zCGY3rG7zN6IFs3uCRX9FIp5pCfbkF7Mz-3KujeF6QYTfR8MZ8VvK_DVNzxtd-Va2TS28xPQZRwPa3Lz787120Urc1Ezzi2rQt0LWZ-KFkKFWtZl_tSze8ZbnKACOmS9AZL6rDNoe0Y7Wo35B1KX7NQjjURpL6BiHJokbatAI51q4iKDdLL4nEvC8PoZslIQnOzwuY7V2zlEpm4NKfEUJhXkt7zBsvdoeifSKAxFws3knCr5qy0QsunueRdKPKOVqLC1FRkH08RYdHS3kj9djDtPU0UiQmtJ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از بدرقهٔ تاریخی قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/447415" target="_blank">📅 09:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447414">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d24e9588.mp4?token=WrZsXnRQVyxweyuRr4w6eHfUK7sZw1GHhYBCnt4AOLOmbmYdBMHJ0TLsyR2MgaGVvJP_yJVhsM1Lql8SSw6-4syrwW4KPua_tsQw7F37S_4-VtKREA4uXoCmiWt3H66ZcRq8BcOxEcxYACwh0__HEcmBPLz5lF4JBLX6gwGW3StDqWiPtzKAXvk55uHYm-9dwvZUwKhzM0R__snN3_6z45Z1IyOs1LV9PEfuyF2uEOEN_GUAlddWEQ1qtost1dYgWMV6E5UFozrAqw_9reZHRkaEXHRIibPnEJ7FvWy_galETWjE9f-R41g0mj2caP3F8tgrjOnZJDO8nqE4EBWSpTe-C-UdOHt8jshxZhv7dgKS19rqAdASOXU6MinvbntF8_fc-HbpGWelo_x-iTsNUIGMhkC9KLN8tGapNBw4oQwJvP8pkwc_rOBBJ9c6GRRxfXVBUQ756Ib0DuNioBXKPO__lT0uNX8ZNBQv1tcU4HSBreSxveAy5ElupjyBXyT1rMueFLK64ZNGa9kNZXet87jNjW1lCf9n5nMYX5Zs-MBM20qE1G6KWdMZ8OQxZo-WZtTPoSZOzvV6m2HRJiv62GnqSPMkvvnnggt2xA0_8B90NHBJi4UIbtc1pf57FdyPKAh-rnXv2q105qj9nzXWA0s2_5a-XiASXroSkORfM0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d24e9588.mp4?token=WrZsXnRQVyxweyuRr4w6eHfUK7sZw1GHhYBCnt4AOLOmbmYdBMHJ0TLsyR2MgaGVvJP_yJVhsM1Lql8SSw6-4syrwW4KPua_tsQw7F37S_4-VtKREA4uXoCmiWt3H66ZcRq8BcOxEcxYACwh0__HEcmBPLz5lF4JBLX6gwGW3StDqWiPtzKAXvk55uHYm-9dwvZUwKhzM0R__snN3_6z45Z1IyOs1LV9PEfuyF2uEOEN_GUAlddWEQ1qtost1dYgWMV6E5UFozrAqw_9reZHRkaEXHRIibPnEJ7FvWy_galETWjE9f-R41g0mj2caP3F8tgrjOnZJDO8nqE4EBWSpTe-C-UdOHt8jshxZhv7dgKS19rqAdASOXU6MinvbntF8_fc-HbpGWelo_x-iTsNUIGMhkC9KLN8tGapNBw4oQwJvP8pkwc_rOBBJ9c6GRRxfXVBUQ756Ib0DuNioBXKPO__lT0uNX8ZNBQv1tcU4HSBreSxveAy5ElupjyBXyT1rMueFLK64ZNGa9kNZXet87jNjW1lCf9n5nMYX5Zs-MBM20qE1G6KWdMZ8OQxZo-WZtTPoSZOzvV6m2HRJiv62GnqSPMkvvnnggt2xA0_8B90NHBJi4UIbtc1pf57FdyPKAh-rnXv2q105qj9nzXWA0s2_5a-XiASXroSkORfM0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش ملت ایران در سوگ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/447414" target="_blank">📅 09:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62d2a87c.mp4?token=W6zbEGPfXFKw6s4DpnBH_g1YtaPbBRpgdGoaiiwFYxvtU5r0EVaiWPdZowAiFLxcPe4JIiNYkU1h3N5_3AjOxNtptISKcb9V7FMwVTYNctYxZeaRFvFQZweSh70aDw5bSgfH0WzwazXqmJMwOrAgHbiScTph4ykJYXlLSdybC_BwJWncRydYaZAMsb4yfxMm6ynFOJeBi8Pt5DFRJM86eRPL4lCq0_1dtBVUekhZi3JAhcSZJJxZ2QcBF3eundPzMs4JjY2wKn5qYhM8_ePfXkFvj9-VlJTe6LSFizH70CmAmyaGPemcfisYVE5PXS-x2Tu9hODOtRthg8iPtKl21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62d2a87c.mp4?token=W6zbEGPfXFKw6s4DpnBH_g1YtaPbBRpgdGoaiiwFYxvtU5r0EVaiWPdZowAiFLxcPe4JIiNYkU1h3N5_3AjOxNtptISKcb9V7FMwVTYNctYxZeaRFvFQZweSh70aDw5bSgfH0WzwazXqmJMwOrAgHbiScTph4ykJYXlLSdybC_BwJWncRydYaZAMsb4yfxMm6ynFOJeBi8Pt5DFRJM86eRPL4lCq0_1dtBVUekhZi3JAhcSZJJxZ2QcBF3eundPzMs4JjY2wKn5qYhM8_ePfXkFvj9-VlJTe6LSFizH70CmAmyaGPemcfisYVE5PXS-x2Tu9hODOtRthg8iPtKl21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم در تشییع پیکر مطهر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/447412" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5fbb61c8.mov?token=IUuTA-SSlhXKaCVCjg3DWrcHsxOLSqOIJBDczfwkcQKqllQWXXi1-B4bVO1gsTc0dzJ1fVl4ZADXcafoIFaKVnSR1lElXcUSfY3qjKFSolS101JFit6elzBASygCmBd3PCvceZnkuHHMMeI3DZ1wQrZe_EqepKuk-tqdgsTPUz6xNN4oJqXF-IjOJiGjkZzXyc2k5TXiJBDYADPPYQcpRBnmZ9nVQANKKgtP234CIJoHpNUnOwExVC31gP5iOo734VR5J5_6685EzngrfFHNtfuefzKnOcj0ICu52acXEibbJofnytcNR3yRGU_Fnk4Uy-s-qGrrms7yoY06zMWVXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5fbb61c8.mov?token=IUuTA-SSlhXKaCVCjg3DWrcHsxOLSqOIJBDczfwkcQKqllQWXXi1-B4bVO1gsTc0dzJ1fVl4ZADXcafoIFaKVnSR1lElXcUSfY3qjKFSolS101JFit6elzBASygCmBd3PCvceZnkuHHMMeI3DZ1wQrZe_EqepKuk-tqdgsTPUz6xNN4oJqXF-IjOJiGjkZzXyc2k5TXiJBDYADPPYQcpRBnmZ9nVQANKKgtP234CIJoHpNUnOwExVC31gP5iOo734VR5J5_6685EzngrfFHNtfuefzKnOcj0ICu52acXEibbJofnytcNR3yRGU_Fnk4Uy-s-qGrrms7yoY06zMWVXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبوه جمعیت اطراف خودروی پیکر رهبر شهید انقلاب را فرا گرفته
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/447411" target="_blank">📅 09:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447406">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMILBi9KZYR0IqYMfYr2KUNdJVrKwRNHd3jXOCNdhhv05g3mbswvNxEH2R9zkwsBtn3OCIVJGZlXongXe2rVexBa1c1NWVZRxU_mjDe0YdBouWxP3aEbbejR4zMmStNhRJR06KfkAvUdcNEy2_MsQHcZ245ICRtWVugTHR8oeujppNgcSpcxRU7dnHXE-XNjzwkvllC3_UR42JRb9-c_PaQWXx54KMO6kHNsOhGzoJud4jeAyPoPAzFBnoRurD4nP0ZQHZUytIdbhrPc2envdqDpskWJDoPdukH1b44vippI-CMVT7_Het6ECcU2N3IQDl4aw_okvQVZWQAkLE1HAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOEpH50tw58E_n4nqsfd8iPlthMeoOFsCAwQ98785djczPa5rByzxRk8c3e0iOEYXmlMCzJ3xzEoTazqmi7xrxhmoQxZ9x1GKv5pLurwLel7byp_vnRq5sZsiWqwc1Nfx4UGwcPpYIP-dBxyt1Dz2Qhg6vt93_zoS_QqrNY0DauTaYHTuyiwnQ2Eg501WMtA_pCzR8xsNHCPW29SgIfESMNkuHbtz6oHaVs02xgVTa-otap3EZ7l7VXzhHWdIDiRWS5t29tDkeNXKt4WmQwgO9woYIISdPE5aTzKTDejtjhIIlQoiAJAwUoOPeVK4C8YfEYCHQTEJRdrZlbAC5NQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brLJBiwvjLL8hVWoB4jXEMJyjcXQ2rFcEkK003ZUkQt2uLgxDy58yOeSQU0oLIduqYAQYIEud_Wfqws--PeFr6q0SP0ld0bYwbTlVHy_MlJ-k-rKH1-FOuoGpeQj-14IvIea0MgLabSNRaUthZDQOC4qq1u4kDFI5XysX0tqI96IS3K9iUju0DYXWQ3j9tRsPSRJq3H9vuzKaTknsGLIwXK-EIyRab-zL5f8HqlB8Odv8viEqWrcYURUnGe6zRyY6y0rTNULAS3yo58Skm1cLDQ-eg9F41ivdRAB-bexo23ba959dfKLG0_JxHO7pbVqTttWvSCSmdP-8YfL_5nY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCQhFxU53wxhQsSJRZKTUUEIgFhWeYMnxPsqE_vi2sZoMZxB_fXWgGdyGMuaU4TCDkjU6d51KQb5PF3oeTXJhpi2zEPZPhyib9H3C3MCv-6EIlQxff2w8vTOlOuICVS7LrKQRzhSZjyLYKMj91QGZUf092p6SUv3-9K92XPX2-mX2vqQA5VQ2-RSrOICXVoB53KFlHe2KpFCY7_i5ucC9yl5TxDbkEHzo2efzfZ13C7xOdsKrD1rojO03rBN1h6ZilB6gJGvNW7MsZ4lVFWGCC6rIc1fnmcP7dBvbQjB5FO2bcaZJ51x75xFvE7a8kZ5u7Z5C5DZkDvt-wuNcZXQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDMwl9oVVTfCNCoCi1Gme1ll2TVV2RdAuaD05ccOyUGAFotbD5jiho6QP9QIFplM8o-gaRdWGQewrMuhf1abiSBY_NgBd1vf-hZQYRKROFN2R_pUWKpncTm-IzQ6gwMI2_upJ-f3_0ztWixRy9a1k3IS3UV9ZweCQJmgsRRCUkzLBuoK6fAjRO3KXB5GyYuITnBoT7UxMNrJwjQIoLU63FAgE7red8clgEccoNVC1JlfW1-v_tScmol4AUFGpRqoLhQj8h0z-i9AZGEooejTQH4oYbz16_hWrZfiUjMZGFeuPUV5vBa27aKsKsHYuPnDTjdbotFghavrExN19Prsvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
موج عظیم زائران در خیابان انقلاب اسلامی
عکس: محمدمهدی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/447406" target="_blank">📅 09:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447405">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7qr498qUzNf0dURqvcZzsy0wUa1EOQX8z5WnbCFg7CBPAtwaJi1cPXrmJzTHwiHZRBMrCf5O6T-K9_HEBMyRG_2MQ5hz-lRJ6jbK2obuvqMmUcdILT5_XZO-CKPYTtOCpnNCLigk_7UiLahnD6LEqJoLnyuyqVgtgHLOs3lJoH0hgRIub36Asp_5pQ_udP5BHn0WbcilOMJWBlHxk7HtUkRD0I9FRbGFU1CsOfXOSktcJlQB4ELY07FHhy9XlOnWv3Gp-ws5lxpBRHclPnFeIB8QljoNW-R2xBdB9BgsW2AP5ePuI73gBNtPRDUWUR1vnaGmb4A6u7Lgl77RLfXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بنر انتقام‌خواهی مردم در مسیر تشییع رهبر انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/447405" target="_blank">📅 09:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447404">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771ea7f1d.mp4?token=g-JWbzx2UFsK5cExRfJZODOiSU1TBwybq81sksJLVv0zipcKSdNOXeuOGed7ef0WMo7ictlEpZlMvr8BGteajOLNSumA4u4gdp6Bfac4pCwauAxhgcdZYNegv_NBy5Q0uAv8zdJQg7DhMZoqL4fAYcfHluPZ84ImsrJjFlN36E8oXd8ya49hS-_nkIW_fNyKHxKB_ejqUUtxWN2DnTkc9MpGnm1RWc79yP5DgWXAse5KkQsl19DbPqADai5mBw7b4KUcaJCh6bvmSWVFSj0PBcUrt1iY7Sm7XE8tOK9FNkQ0t3hUeQNJoKwvQIeG9W9PMxVN91NfgynImkvzz1nUeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771ea7f1d.mp4?token=g-JWbzx2UFsK5cExRfJZODOiSU1TBwybq81sksJLVv0zipcKSdNOXeuOGed7ef0WMo7ictlEpZlMvr8BGteajOLNSumA4u4gdp6Bfac4pCwauAxhgcdZYNegv_NBy5Q0uAv8zdJQg7DhMZoqL4fAYcfHluPZ84ImsrJjFlN36E8oXd8ya49hS-_nkIW_fNyKHxKB_ejqUUtxWN2DnTkc9MpGnm1RWc79yP5DgWXAse5KkQsl19DbPqADai5mBw7b4KUcaJCh6bvmSWVFSj0PBcUrt1iY7Sm7XE8tOK9FNkQ0t3hUeQNJoKwvQIeG9W9PMxVN91NfgynImkvzz1nUeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار لبیک یا حسین مردم عزادار در کنار خودروی حامل پیکر مطهر رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/447404" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447403">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5226f64d40.mp4?token=hrlspckIjYMmQi1hJbBu0nTQGp-kZOjlSc7p6BvLW-Km0xmSNYMggYugEaexPg4zC2Qk3yWD5esVMqSvNhrceQEXRaV9BqTvcoED2R1DxlBPsPvowr1WJ0iikwZrE4cDI-yOvDrRy66vYaZOoa5jab-Rj1J3vj8nkJGzS02bilXtPjpssv98lr9vQBgt6tgJzIQ5Uh2i4IY9HmG4Dx-mXFAqelVETWudSIukfkv-Zvw8jCwN6E_byKsr6aEvcJwSc7KOM1V2V2nNVLlJYAFEqVjuEFSSUImRPxg6KpdGK0alrXeDStBNtreOCkizSF-Xs8iiuoznhBHU7XTpUiUejA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5226f64d40.mp4?token=hrlspckIjYMmQi1hJbBu0nTQGp-kZOjlSc7p6BvLW-Km0xmSNYMggYugEaexPg4zC2Qk3yWD5esVMqSvNhrceQEXRaV9BqTvcoED2R1DxlBPsPvowr1WJ0iikwZrE4cDI-yOvDrRy66vYaZOoa5jab-Rj1J3vj8nkJGzS02bilXtPjpssv98lr9vQBgt6tgJzIQ5Uh2i4IY9HmG4Dx-mXFAqelVETWudSIukfkv-Zvw8jCwN6E_byKsr6aEvcJwSc7KOM1V2V2nNVLlJYAFEqVjuEFSSUImRPxg6KpdGK0alrXeDStBNtreOCkizSF-Xs8iiuoznhBHU7XTpUiUejA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حضور زائران در بدرقهٔ رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/447403" target="_blank">📅 09:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447402">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e9bd3f29.mp4?token=nGU-4RJVz_cVZsKgcWAk43ldxu6LXV7h-8vikQQaKdrfnDXbTqy_xUz5yX2zQW3it5SAIdRAfMpMCXYxKiwBWGGFxtHfs-bMFUxRBXqeLNf1nCP955cE3Q1mhVcviK4IHja56gqytOVXJFo9O3_BVY0faJo52R6FS2ZEzjT2GxlhbGKjZMiGwik0vvxOXBH8NpHKvX0Mq32ew1ziMW43x5t4-pNd6TK3D2sTSMBl2gHeAgw-XJuGtwZIPf9oR2EqTlVTrcZTpd4elp59oMsYFC2dAVe4hkP5YGHkDuqAblM95wyQ1HIs_jak3DZpFPeDdoa9s7pfBsfWsIyArUTP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e9bd3f29.mp4?token=nGU-4RJVz_cVZsKgcWAk43ldxu6LXV7h-8vikQQaKdrfnDXbTqy_xUz5yX2zQW3it5SAIdRAfMpMCXYxKiwBWGGFxtHfs-bMFUxRBXqeLNf1nCP955cE3Q1mhVcviK4IHja56gqytOVXJFo9O3_BVY0faJo52R6FS2ZEzjT2GxlhbGKjZMiGwik0vvxOXBH8NpHKvX0Mq32ew1ziMW43x5t4-pNd6TK3D2sTSMBl2gHeAgw-XJuGtwZIPf9oR2EqTlVTrcZTpd4elp59oMsYFC2dAVe4hkP5YGHkDuqAblM95wyQ1HIs_jak3DZpFPeDdoa9s7pfBsfWsIyArUTP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: خودروی حامل پیکر شهدا دارد حرکت می‌کند
🔹
پیکرهای شهدا را بعد از میدان انقلاب به‌سمت میدان آزادی می‌آوریم.
🔹
مردم با آرامش خودشان را به‌سمت میدان آزادی نزدیک کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/447402" target="_blank">📅 09:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447401">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9a627324.mp4?token=QWqbYQNxztyzcOQrHww7SaGRTc5fvQURyF4hCxC5rO7dGj1pmROTMSRal09JQq1dRfzTaOuR88Q4H49IYPEDuroR_p8oXoz31RxpHPkcjQxh9G0qgDE10gVv7TAxwF7ykXGOqu5Z8NL0idAMr7MF_arOVetQXdiSB9WdgUUHDD-tJG4Wo9KfUN3FUICsYGnYhuXbdsIzej1ueeddhUWo_bQhLOXjMTLspSmgMiC_-qPkEE-Sa9wbS06mZpEX2v2WvabTjaE6gzDAoeeENiGv6SsdHINrv1NJ_K9YAVbuyl4mZCyDzB1969_wC4dXfocN5Qxq5LxV6M2-vk4LUJx8cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9a627324.mp4?token=QWqbYQNxztyzcOQrHww7SaGRTc5fvQURyF4hCxC5rO7dGj1pmROTMSRal09JQq1dRfzTaOuR88Q4H49IYPEDuroR_p8oXoz31RxpHPkcjQxh9G0qgDE10gVv7TAxwF7ykXGOqu5Z8NL0idAMr7MF_arOVetQXdiSB9WdgUUHDD-tJG4Wo9KfUN3FUICsYGnYhuXbdsIzej1ueeddhUWo_bQhLOXjMTLspSmgMiC_-qPkEE-Sa9wbS06mZpEX2v2WvabTjaE6gzDAoeeENiGv6SsdHINrv1NJ_K9YAVbuyl4mZCyDzB1969_wC4dXfocN5Qxq5LxV6M2-vk4LUJx8cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیل عظیم عاشقان در محدودهٔ پل روشندلان
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/447401" target="_blank">📅 08:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447400">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d52JGhHhUqNmHaGEqV6w0jR-K3nz309wKN353U8vzwkwZ6kjhUMdAMzvVKMqNP-eZDCbahZDONs4qbuG5VIXpT2iaoMMB1Vq-F12fjcPXjCVmAPinR51rDuH2ipi-XlQ_fBG2YrxjZ-wFivANcg16MqDdQspk4PhrFY5y8AsaH0K3etUL1OpHilnuZU1gY-vb5OMybTmIg_NfKbpz0Ch0BIqZQwd7CKP9uLnYHy0PmqPVDpemK1QmOCMwdT33GQOqdmKGi4fxiNHA_UHNZMonSVjKEFoMM_FAOc52ACiw0ei6uTfGbpDy9W6qGp2wR9ppDOcrH5PnZ9Wk0WQxdCUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
شعار لبیک یا حسین مردم عزادار در کنار خودروی حامل پیکر مطهر رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/447400" target="_blank">📅 08:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447399">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c66ee92f3.mp4?token=Wm_RWE-HecdxMwmw3TndVCVMLRYt8uyplagmt-Q81K0teyRaLbhXmf-af4rdUNC5vJDoxVU_K4NoNy6R7IKtWgujFmaqTIRtc3nsYJuIHv059zWpQGUdlZePaq5Bgq0LUtL5-e0LaNLOmn_SSB4h3JooQLAh4LKcdes9xnQKFfN2YU2gau8KKUnwyCmquK4uCaswGO_BZfBXeNiFXuFBdIXs4P031aygGblKDGZQMrIIlGOJEJX3q5DjjgHn7-Lpi3K1jQ_-YY3_kB3qGVQKW7JXjOIBWkeXzHIGJrVziCR2ziok9oqz3D2hK4nQWuvncWSvPkg_fjDEK-hy5wi-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c66ee92f3.mp4?token=Wm_RWE-HecdxMwmw3TndVCVMLRYt8uyplagmt-Q81K0teyRaLbhXmf-af4rdUNC5vJDoxVU_K4NoNy6R7IKtWgujFmaqTIRtc3nsYJuIHv059zWpQGUdlZePaq5Bgq0LUtL5-e0LaNLOmn_SSB4h3JooQLAh4LKcdes9xnQKFfN2YU2gau8KKUnwyCmquK4uCaswGO_BZfBXeNiFXuFBdIXs4P031aygGblKDGZQMrIIlGOJEJX3q5DjjgHn7-Lpi3K1jQ_-YY3_kB3qGVQKW7JXjOIBWkeXzHIGJrVziCR2ziok9oqz3D2hK4nQWuvncWSvPkg_fjDEK-hy5wi-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود خودروی حامل پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان به مسیر تشییع تهران در میان خیل جمعیت مردم عزادار.   @Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/447399" target="_blank">📅 08:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447398">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUyN62aLNLZBCBAaDRkF9g5vdIH3kGWKtsZg0dBKhHrbCxgTkqn8gnAtp6ekY5HEneH8S3_9Q8zMt0osg-7FjE6vvyPzTdoqvZJjjJlwG6qMkiJngrv93XzkD8Vp3MCJhBxw-87kra-3jYJHFPSdjyriObIM82EYz_RBe4u15Vsli_LWjAp52-aGYlcY6HEWU7dcajXBg5h2Wj4LuZ3OHWaFSwTtdTl5rGoG1FkxU9tc3_fPJXFTKo36qj3sSUIbBnFHmcBXWhZwi1rGcD0ac8c8S4nyAOqjTy82RFzoK0Hj1hPjwJeunWyM5bKbBsn8efePqt7-ox0NjTg1lt2i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دریای خروشان عشق و وفاداری در وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/447398" target="_blank">📅 08:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447397">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7t0h5ZN8H3VGOW07rd2u6JxoBSmQJS2juv-AGp4NkS3j08uI9Xq109ML-8kVYKyVDnZmVkwp9DP_o0P9127539lqK1kHBiMIMJ5SN3Qm8MipoyToA9mxpUUk32mEOJ1_QEVNVpygZXu0HDDVmR5az_dia5pQnsN1vpleK1w3DeywU6yz8Rrpla9DIO6MQDZ47G2yG58HloQLyeo_XdxeumJpOKjEpYvPEXTGCezllbHogzzEezzpBaeLelUqLW_K36e5uxzUmlAok-RAV-lv6QxUbXYVHmSVTaKfb8N2R8oKmfLdEylGcO8wXgEtSUdVxGPglYmXMee7y-KlkstTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل سازمان خدمات شهری: با راه‌اندازی سامانه‌های مه‌پاش در مسیر، دمای هوای مسیر تشییع بین ۵ تا ۱۰ درجه کاهش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/447397" target="_blank">📅 08:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447396">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aee71456c.mp4?token=PLCw5rgu6kr8-K6VWpNyLiLxttnSn1SqbMHzQqbBJXhQE4tAyxa7onbRncLhroIjAFGex8vNhYDKR-SjcqCpJcpJOovuyTQDCzR43FDXVmx_C7XxNlFrebyLn-bGjJlCstY716PZlsRLU6Exihi3XVv8LFZGXUZcYQvTmOuJKoi-0MvwUvDOrNSmPzL96Pkr_hqnTo77o4ezg9MliIdFXpVJapltjBeMgyZeD0NkOQyhkCG6LnA2NCvtDZ8DdnKm9UqOvrIWKRAJEehXNTsZfhcZ_g_mWrKngofMr51kGQtKQnWyzIyyuEyeV6jgJd8brnIUFmTFrnLSU2ncrverQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aee71456c.mp4?token=PLCw5rgu6kr8-K6VWpNyLiLxttnSn1SqbMHzQqbBJXhQE4tAyxa7onbRncLhroIjAFGex8vNhYDKR-SjcqCpJcpJOovuyTQDCzR43FDXVmx_C7XxNlFrebyLn-bGjJlCstY716PZlsRLU6Exihi3XVv8LFZGXUZcYQvTmOuJKoi-0MvwUvDOrNSmPzL96Pkr_hqnTo77o4ezg9MliIdFXpVJapltjBeMgyZeD0NkOQyhkCG6LnA2NCvtDZ8DdnKm9UqOvrIWKRAJEehXNTsZfhcZ_g_mWrKngofMr51kGQtKQnWyzIyyuEyeV6jgJd8brnIUFmTFrnLSU2ncrverQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود خودروی حامل پیکر رهبر شهید انقلاب به مسیر تشییع  @Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/447396" target="_blank">📅 08:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447395">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAxM7c8bn4Cf17oA2IThRWdZyaFeyIXyFx_m8WrPsjPVTtRGfr770MC7CtXxvozBDCSM3WJzFHGleESmTIjzjxbmDvLlS4UPH44D_lSvieyetnaDxw0fcmFHxQiHqvrlcAMSOtau5oMcfWLozay1JJXupaoglzz3Rcizw8JW4uz6BiqrllK3y8Cyjyrg1W9GbL49EA-CJrlLI538QD0PtKOLXxaMy6j6ACkwNe5bH1nJAYjrl5j6W2LGg8o90xSms1rc-LhWczqsQ8i1BWpo4sclRnZ7Tqs2kO-ljxCPF6aRMj_jhK0EWZj1RRsROKu6Kv4nUOgKmG4KJHRuAhehrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ورود خودروی حامل پیکر رهبر شهید انقلاب به مسیر تشییع  @Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/447395" target="_blank">📅 08:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447394">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b4d69146.mp4?token=YUsEDYuUyxe-0qO45yR5gMZ_0Z-Sakwdcl5uJMax6BLVoUz0oGF7YT1Tj3u6wLXobRA5_hSszfrV9-A8Q11u0pLbXSFaBSDkuwHwJbNZpTtGrU4RdbRTuQZidvtdCBT9wDNa6jcokJWYFaAaisdx85YpPdW4k4vYV-8LuQdXOfX2j--Z-jR4IDK4_dqKZ8-tlWYIMMVBV7x9yEizzNxBZPgKYA_YhwPkbXABH0vvfBSQA3G7HIgJpdE1K1_slMf5hqO0u0FM5JNxzTdlANrq0M4lCpZUgVviK9bRcNIOHIHIzbeTkSynrqrfHBFMFkyfbFjL5aDEOaYJAJH647guaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b4d69146.mp4?token=YUsEDYuUyxe-0qO45yR5gMZ_0Z-Sakwdcl5uJMax6BLVoUz0oGF7YT1Tj3u6wLXobRA5_hSszfrV9-A8Q11u0pLbXSFaBSDkuwHwJbNZpTtGrU4RdbRTuQZidvtdCBT9wDNa6jcokJWYFaAaisdx85YpPdW4k4vYV-8LuQdXOfX2j--Z-jR4IDK4_dqKZ8-tlWYIMMVBV7x9yEizzNxBZPgKYA_YhwPkbXABH0vvfBSQA3G7HIgJpdE1K1_slMf5hqO0u0FM5JNxzTdlANrq0M4lCpZUgVviK9bRcNIOHIHIzbeTkSynrqrfHBFMFkyfbFjL5aDEOaYJAJH647guaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: خودروی حامل پیکر شهدا دارد حرکت می‌کند
🔹
پیکرهای شهدا را بعد از میدان انقلاب به‌سمت میدان آزادی می‌آوریم.
🔹
مردم با آرامش خودشان را به‌سمت میدان آزادی نزدیک کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/447394" target="_blank">📅 08:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447389">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNwlI4TkecQTKgVtPhtrI6vOxsgKMyDEsPBKB2pDE3Da8PL5wAVWNGtrA93-wUYLDIT6Zq4Q4bd9x8lQ9TUaSAYcLncnUNKWur-aJPo0JRT3zPyMLJ-XFJYIUHFoCtUj6c20ooiHRa-bob1XDNSjULvLIMRr4uF1GMZrey0XNYdHgboEwVPmsCaDGB-ryrZzVBB_0zFFVT_3-k1IGoZ9IsEe7AER87hS4FZ6Jdc-4vl-REkGOY49m2CecZ5puR_hkWfraSHanj5DgwDXXd_q2JfUvPemwAJaFNQ4McrNKECX2KMqBfDu0xpV9UdGLkvIkC-3vcuPvDso3Gl-aJSPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHj1J33llgzJ6gB6D2tn1rj7Mq3iptTICbqfGG5fX4T9JFCCQoPUfgkRWUAq_Ha2-z0ZeKSBHJvHSGPc8PXQckC2M-SH68XEQwwCs_xkj_KR3VhgxNoTbhY3SQo1_wdlnHMkpHiVeUxyldATAfjYC9Z-UrItYOMA8D3eqe3MRhC47BJ1wfdk4CQ7r6ajdVWKPrXaEyRqqElugkLqnYhW4fBZfl6YHw34VmRsodIoHujdCgIbNgUuShGD2Hu2OasfGJp4USdqquLCZtP6HOdnTvkMayxXiSCnV1YSbLpTVjKgEZcQztXNvo7P3hfZE_KUTZU40ao6ezSXVSjbyzhQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0oBkUXAJ89SYAbg4r1jm95IH8vlximOI8PokyygJdKveVUpKN-WYBzNDK7UEepz0m1NcjRq6OlJoiuxFJprtpZtGinQ-B7Kx0lS1MFUnTTe53JU_7uIYuMH7hIYtIJbJ-KmtwyO_smYANn_6TNFDAC-VBeRe-7t7Mpn5326XB9fkUotkoNCF5-ZjMNrMRpe9bQz1hkzRGoeGl_gPeDHQxtUUtU7UpjzZ47yKyCz2tGDs40Zp_hQmUwf8zLX5zb-nJ3w5Gk90qhkRfh5lDiFXdLZWCzA805b2aA6vrPyM-T-MJm1UdrswCkTCwQGOfNProRy7-4up8MoliY6OsYfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRjBw3Pf0DtxLLoFxeLLQUCNqP13LahsBUbjm_VTbWNhQqJqXfFmfIP96IS8iOXwkG_4tbY6XBZmO3bsXNFyOHRjTbG6QiPbt7_dXx2R6tgzas6U6ju3sgcrT3yNaIO9zxQng9_eEgZ8SH6QWn3xyQlWsFNbY91_JMMHvvz2Kp4YZacfRnfZ1rOYhQdXz_SoMnVmV6KHXPjZxa2SpECQRUjL_Mcxg689f_2gqrnelxlZLuI2UrARRU4YzY7v3sn71vd8_pCfhiNvusWfMflPWlBEMS95YF1lzQCcYrEfQWQ-XlAMvK75CFtr-uwiEnyVoad3mt-DRXqlCWni72bYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFUF0MYyf9SVwYSYmL36dZIzHBShuN6O1ldUJcLLvW_6FutrdLe6vH27MyuBuXckvZSkjFKLqxGGgurc-Rm3-47S4XRukhB3igm0x1rNMlKFnGc3NbF9xg7o05dx10YcyxohzyfF2M0tWmGsrqovH1uOs7zqPhlavxnEj-odl_CPWvxC3Mqi4a4XZ3s3BEkoEtVdv47ZWzklD4dYtf0ioHjXEwvnGHZdX6IzCtrDvn6sHj8HPX2NBAgbyxfKXPVBw0GK0E1PBLiGTnHUOBO4bx4Eq_e7nAVGCddcNqcK3nMyKcEYhrKe8UxctlyPkW3qaeDgp6NuUVeFcdk40PCEVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌های ماندگار از مراسم تشییع
عکس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/447389" target="_blank">📅 08:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447388">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c3703ace.mp4?token=eKdMV_eGUoyF38At8yKeDBKDes-AhAJioKRXxXKdlI9KhAIpDmK2ZGBpDYe5IV_9Wuh8JCsx8ZCXnzObWP43C9W5YVIcp0E4FoaZmQ5zus8FlEGkI9v2Ea_09zr8Uuc4yaL6cCfF9yw_6_NLRxdgAtpYc8Dy8HjLmcJgsmsGzFEI2Vg4EJZDBeXUi7PwypXlGUmyB5dgeakGgH322nlEYNkNOuo9HEfnfdqDWMolE4UPx4snJ4MpDG70vN6y1DMiaP1JvR-KCej5uSLQfZY242O1saBtEUbqrH8HNJv-au34ZSLJsy5noh2jTwAnZdX-PelffjRj-oDGITAD2GGl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c3703ace.mp4?token=eKdMV_eGUoyF38At8yKeDBKDes-AhAJioKRXxXKdlI9KhAIpDmK2ZGBpDYe5IV_9Wuh8JCsx8ZCXnzObWP43C9W5YVIcp0E4FoaZmQ5zus8FlEGkI9v2Ea_09zr8Uuc4yaL6cCfF9yw_6_NLRxdgAtpYc8Dy8HjLmcJgsmsGzFEI2Vg4EJZDBeXUi7PwypXlGUmyB5dgeakGgH322nlEYNkNOuo9HEfnfdqDWMolE4UPx4snJ4MpDG70vN6y1DMiaP1JvR-KCej5uSLQfZY242O1saBtEUbqrH8HNJv-au34ZSLJsy5noh2jTwAnZdX-PelffjRj-oDGITAD2GGl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: خودروی حامل پیکر شهدا دارد حرکت می‌کند
🔹
پیکرهای شهدا را بعد از میدان انقلاب به‌سمت میدان آزادی می‌آوریم.
🔹
مردم با آرامش خودشان را به‌سمت میدان آزادی نزدیک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/447388" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447387">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54092b1eb.mp4?token=SjqAETq6Mlns3dkmbuikdT9U-tyh31WG-LstgNtmrea59-YBXLYLdbRu45kK4zS1fiP8CkIsFOIbPG_Yg2NZOYKrdpvg4kxQWX9sZel8sQ3izFU4E5ZpwApkfPnBqs3iH8XjKpPChEMh6qzgXgO-Yu8tQ1bld3QJzRdzVC9A93pbYdASOZGpciQCe77vpmqGxYtLifpJdlUuM5IAp0ArhkbAPym7Qv8xFW2dr6FpXQGvBVAEMbvdh9Y4EzS2c0zBN9tsccOitR68bKqITUP72fHsSKt_4EfTE448ope2suJvrtz0NfjUOSweB3Lc3HIIBZnTQc5Vku_zGLAOCPuCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54092b1eb.mp4?token=SjqAETq6Mlns3dkmbuikdT9U-tyh31WG-LstgNtmrea59-YBXLYLdbRu45kK4zS1fiP8CkIsFOIbPG_Yg2NZOYKrdpvg4kxQWX9sZel8sQ3izFU4E5ZpwApkfPnBqs3iH8XjKpPChEMh6qzgXgO-Yu8tQ1bld3QJzRdzVC9A93pbYdASOZGpciQCe77vpmqGxYtLifpJdlUuM5IAp0ArhkbAPym7Qv8xFW2dr6FpXQGvBVAEMbvdh9Y4EzS2c0zBN9tsccOitR68bKqITUP72fHsSKt_4EfTE448ope2suJvrtz0NfjUOSweB3Lc3HIIBZnTQc5Vku_zGLAOCPuCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار زائران بندرلنگه در چهارراه ولیعصر: انتقام انتقام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/447387" target="_blank">📅 08:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447386">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5ceb14b0.mp4?token=nQp6N5HvmHK3tpAywVuSVybDfjgXUaWdkyMisxs6dsVPSwVeK-CEs1ijwfY5dXPfKIud58050GoL94ky1EqqCImGLUmOGghtn8JuimoBs4U4z1gvgYpSPdU8Zsq_vUMkJaLvtlMUiLmTcDoxc16kn3WnYPXKeNMO4wBIQEW7KlPK6JK4G2WZ7r_5ww7hqy81-jOgsvYX_-tcHdAXm2Gkiw_Xto4aIsrXcYLqK3tCGYrkUTf7uLppjam0PXj0-5sKpEeYzaJoPny0RuFLaUskMKJxVgzCyXc7Xs3C-54yX7he50p034y6uBl4FWv50RMKIpA5cPo2njLX_xft1tsvbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5ceb14b0.mp4?token=nQp6N5HvmHK3tpAywVuSVybDfjgXUaWdkyMisxs6dsVPSwVeK-CEs1ijwfY5dXPfKIud58050GoL94ky1EqqCImGLUmOGghtn8JuimoBs4U4z1gvgYpSPdU8Zsq_vUMkJaLvtlMUiLmTcDoxc16kn3WnYPXKeNMO4wBIQEW7KlPK6JK4G2WZ7r_5ww7hqy81-jOgsvYX_-tcHdAXm2Gkiw_Xto4aIsrXcYLqK3tCGYrkUTf7uLppjam0PXj0-5sKpEeYzaJoPny0RuFLaUskMKJxVgzCyXc7Xs3C-54yX7he50p034y6uBl4FWv50RMKIpA5cPo2njLX_xft1tsvbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم در متروی حرم امام خمینی
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/447386" target="_blank">📅 08:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447385">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4a133b596.mp4?token=W95K77zy7Y_3d-96wvUre5GS89ROw8CI7mLIHUCCkYDrSpmGo4agW5-IxLkdRkxo-2qWpPan3oHX9H6krryBkkBysH_c40Wlu2SR8QsHJuYfVaLjMXkPOsBSmqn7tSL34U8cBRpWBg7WPcYMmPkyfuqBJ6BUEuPfImgjJJF5kgpx0k1mYsrt5HGfA3M99STPZRKl1OdS6UTA0UE3LbM3fKmUxrP_H6_nwtnM7JZlTaLLaDSUGBg7kvJqgDm4sIOn_8gLmrDpdj_Kqg_DavSukfA1ThywhIx0PLmusP80pzgMO4xZS6Tv68UdlObY_v6k_WY8piBl8m0OqAvT0xp3NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4a133b596.mp4?token=W95K77zy7Y_3d-96wvUre5GS89ROw8CI7mLIHUCCkYDrSpmGo4agW5-IxLkdRkxo-2qWpPan3oHX9H6krryBkkBysH_c40Wlu2SR8QsHJuYfVaLjMXkPOsBSmqn7tSL34U8cBRpWBg7WPcYMmPkyfuqBJ6BUEuPfImgjJJF5kgpx0k1mYsrt5HGfA3M99STPZRKl1OdS6UTA0UE3LbM3fKmUxrP_H6_nwtnM7JZlTaLLaDSUGBg7kvJqgDm4sIOn_8gLmrDpdj_Kqg_DavSukfA1ThywhIx0PLmusP80pzgMO4xZS6Tv68UdlObY_v6k_WY8piBl8m0OqAvT0xp3NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌نوایی مداحی «باید برخاست» در پل روشندلان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/447385" target="_blank">📅 08:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447384">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4271d31f.mp4?token=uykr_wwkWQv5RoEMPiopetfKyGg7Wg91Z2zbOzRVAleRL3B-fwmVOmsnx3mbAfkLxlnMUAP0pn9Fm8aBi9XhnZ6YdhIMIpmjhUm-q_mDRhoK-Mdgv6dDMwWFmwEADpB2MiEwLYUe07cWIlWKkXrbEWkKftBTed8K51XfsLY2BId1CA2m1D7jhW-HbNbP9bSvRGMeqpbl1brGMVMFCZFlMnLnxBAda9oQezXFabs8p6Yf6PtxsoAldB7XdDcMHuPZlzbTpFrCMz0CyDQ2cXtXQ__3kk0CZN6-tI5Fk6qAghY98EAL_F8eCYx2vvPgoCzuLK3TjSZ7h6e5SZFcUopRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4271d31f.mp4?token=uykr_wwkWQv5RoEMPiopetfKyGg7Wg91Z2zbOzRVAleRL3B-fwmVOmsnx3mbAfkLxlnMUAP0pn9Fm8aBi9XhnZ6YdhIMIpmjhUm-q_mDRhoK-Mdgv6dDMwWFmwEADpB2MiEwLYUe07cWIlWKkXrbEWkKftBTed8K51XfsLY2BId1CA2m1D7jhW-HbNbP9bSvRGMeqpbl1brGMVMFCZFlMnLnxBAda9oQezXFabs8p6Yf6PtxsoAldB7XdDcMHuPZlzbTpFrCMz0CyDQ2cXtXQ__3kk0CZN6-tI5Fk6qAghY98EAL_F8eCYx2vvPgoCzuLK3TjSZ7h6e5SZFcUopRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری لرهای غیور در مراسم تشییع پیکر مطهر رهبر شهید انقلاب در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/447384" target="_blank">📅 08:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447377">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRU3iRtRp8tffFQfOK0twlV5JuxocBS5GUGQOrAWEqCKzA-NF6PhkrEvUnQ1HCMMtidjWdbCNHzSrMGUrcHpfME9JDWw5t_QLPPmWrGq2AI7AqoD7WgzJfjwYvZACUGFyF5L7k5xxuBr3QGErvOsOUQHxuKKdIyek_Av2q3B447z4fXMD79g5hTx5frl3mexXqxpYtcEtFG7hUGKS4kmVDjrsNnzuxdJvPlXRV-agskJCRBBQu-4wvWJcXAUNq0kREi3i3pwYy3U0zrJTnd2ZzoLEe8gS95fnRXSDPf_8dRnh4ta2Jo3ksqszylVwx7hvtv6f_iFpCaTBVWhv7Srpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLPbrR6nQNMXxcWOdQRKrgEcuS1_qTwARKS8cqrYn1xQKPdqgpEEgTTjPMeTtpsZRFmP7DZftNKh425gIjnSOQ1F_FDXkQNzUmZL4mSQuFNQhk1uld7yCNPSwDEMFsPLH6XEpsHTGRLq5QhPAVB9C_UnNCo2qPdsPLqVC36MqwTLMSjYWzeuiTj6NtgiFy_i4Ip56Z-_tkrieYfZI_ghFedYKYswS6C_5ubrRTDx5Gm2oCIckRwNypa91_o29EGSDuBQUZuICdjhH9gR2bIjh5QmWyan4ikZv1LDyjDsc78yeyRRjdhUcP_gOkwPVtSLe2lIt81doLxb7n-mLCZrIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFM-gCvwl73QqzSRXOJCHBbALmXdl1wlbe7zti2w7Je2Bo8zwwkLRf0s7V3i9yYVw73-LXalGvID392WYfUXHzRw9PwYzyhZ2BU94TUoa0bEtHWPFc954pkl9zxU4HM7xnCpeQtJZ38E7VKgM1-XbHxFFA10viWVJQwuuhLiCjjxjTnywl1UsC_6x4Aj8n6oXOSQP3CqrF065FXcpVAlAtyBy2NwMyw026GnB5aMPfjaHAmaA07G7aWjyDVkSEtlsXJnOJUxa5Vc7rXE4OVRpiNDlzA5LQufbsGr1TT_Gbq4kJPMkqzGCLUCHnc4hHUkK2VOC_-72N6vFbNYcTuzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXhIRwkAMh_v1ApNTF9wxf7_lAG5gIS2KJoB1r3w-AvkQ-5SzrztY7LfbrXQAMVuFDSWb1dxF4tKak4C9H8wo1HZiT6ijsP2_pVz4wSyDXcGVrDwP-hjekqpMXlfw1S3x8ku8HZQCcAjZNP09nJkhN_NSgxlPt2IO5buJXXdAh9nLVr4XVMRN5_x6ovT9rp5D3e3v4Z4PomcWk4RCq9yN9c-vY1dcKhpP2FlxkXn4e4I8nLn4EE6P4_yh6HgX20JNZXbxS2RE7t2oMSoYSB3o74B0Kr0IsiB_-j990TNJzExpbf5N71ISzAFJiipt86Auy8ijRnsybw39SGtcAKsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7ilENCtYF6YRTN3WKYEK1tbMit5-BF23rCt51WWpnJqs72YrZEovYHRgSLZ2--Uh5kKhfd4-AJOK6POJfWMEHKMwCsNKQoNrSOdF_yhuW7oscmWF1BX4P3OtHcsnsXYkT542lPL_PzwWZeXZx08rS4PgVMM7XIfSKIIy_B1aDpWt2-y-1zgu620bputdsio5SatSipzJihbQ3Wt07gKBt_i02t3QviXLt5_ubNTJdBj0IEEfRzxeeVPXrHFB-Ot3xjdnMM7pw-k1dpnTDpakwFT-1lRUBQ80e6_37Dm6e7Oyoap9RHDnvppi12TTdhNOFMfiH2lgjKD9b4QdNueHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwY70O2KDIf-LrsCa6mY4xzaWPiDkiGTRj_8VLNJfema9O1o5HF5luMgR0DcLWqGXW3yisBUDZ_dzUqNKUS_-rBZVdpqVBAVM8EikxuAW840P29r1_5ecTZPMCetXDH_uddmGBgpWESNQI0DxMOlgTCOd8WuosnBsZwIKVMr07nbGydAq98j9j4oVR-NbH6vLpniuvboA47neja8c6RdZ7-gbvsp7qp_xZ5TYi8bFwO-dwnoMwA9Ley1fjNhJZbm9YYp-piyKyeh89eXOW45rikkvt491cJ1fN4wcMNSRoVOxK3yZ78HI7hi-ILulUJIsBstQRGcsn2Imy_3x7PPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_liqidfkqX967qAMllH3lcfzqVK-MX-Jny4cdCQMvUgcYzf4XVF7pbG58-f8TbGPYqxD93kMAXaj2OUQAuJFJW28EqMZEO-bIoHVizMc00In0OoaFZKNsjGNDOZTAuFSNWTEgRMpviZZNSzB7bul2Do9yd7AXYnqDWhpH3O6PRu1yHkm-nfRTX0E8ahbNRHbtJWiQmc8Frso4Arualy-_4gXdtpIc6VSa9cQybjw-lruAbaqrWg_k6p3JZqPfGFPvuYXEl8Er8J7kLMdr5nfCcxMn2B4L1quXwYmruwmzV-DerIzKGKG3UNU_y2oWcN9zzeHdn9DPDt1ECPeerPHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یالثارات الخامنه‌ای
◾️
مراسم بدرقه و تشییع رهبر شهید انقلاب
عکس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/447377" target="_blank">📅 07:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBORoI2dh0wjTZXXkWmAAj6iMqNSFnpr1eFgNM3u3oj7nB8FW7xJpNoLF-4faC1VJHCwflRZtVqnUDCAj4-O9pQIxnk6zGOA0ss0ZmEJvGlIg-xt5Q8rbQchiHSYunio3yA8G4erVq9brcTukBuG3MYxnqiUbmbbIgnuEDbqxuI0uqsq8c_ARtis9csY_5GthgvzqnmVxr6lIyN-0jRsW0umiCavd-OFuqX-gJs7zixbnYSY794BRlnF_PQKrWztAuagT-qldK1F3dh5QOdnVCwbTeOqLU5tP-M5_0Ud-Yzt9PRhm0Ib2oiOX1bc8-9uKrQ606w5noVnhpN45xskJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر مراسم تشییع رهبر شهید انقلاب کجاست
🔹
براساس اعلام شورای هماهنگی تبلیغات اسلامی، مسیر مراسم تشییع از خیابان دماوند، میدان امام حسین(ع)، خیابان انقلاب اسلامی، میدان انقلاب اسلامی، خیابان آزادی، میدان آزادی و بزرگراه لشکری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/447376" target="_blank">📅 07:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb7cb794e8.mp4?token=UUnnr7etS_wwfNJfF9bMnU8NQNzjFksPqDwcQFLZz67PR5hPuA9p8geZCPuyq-xMBPGtTxYQgF8XVkF3u7l-f8fduDumpYnXrhxk0FB4HungecHlXd81lEQhkQnz3dMuqzIhkYA8YLr5eZkSQ83eS0XwKXgYBzK3JbEXIbz5r-M7L2D1jeQjy2aSPDzkDfZgdI50kmEYNkfeStbdes22t8x-4uDBLD78QgHIgf1vx7x1M375XqSmjBQat7avWW9-QN9hFzFo_mkLnsSraCzLB9xdLo-mpJbV4PAIYPP_eU8S6uuA04VDu0HJAz_CTaE6Lr8YVSHvUguR4CleTPOKaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb7cb794e8.mp4?token=UUnnr7etS_wwfNJfF9bMnU8NQNzjFksPqDwcQFLZz67PR5hPuA9p8geZCPuyq-xMBPGtTxYQgF8XVkF3u7l-f8fduDumpYnXrhxk0FB4HungecHlXd81lEQhkQnz3dMuqzIhkYA8YLr5eZkSQ83eS0XwKXgYBzK3JbEXIbz5r-M7L2D1jeQjy2aSPDzkDfZgdI50kmEYNkfeStbdes22t8x-4uDBLD78QgHIgf1vx7x1M375XqSmjBQat7avWW9-QN9hFzFo_mkLnsSraCzLB9xdLo-mpJbV4PAIYPP_eU8S6uuA04VDu0HJAz_CTaE6Lr8YVSHvUguR4CleTPOKaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویری از خودروی حامل پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/447375" target="_blank">📅 07:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab06fedf8.mp4?token=A6yDNOOFDCqGxVQXFEKreHh_h1hILUrHLQxFLMlsSCml_-vNcqJTfKs8r-sdoikVrZE45PrOBbvallfk_dWiRR25ufoCGMqnub8ImkLSMu-iglOhYuC067HzvK9CnJaQgomX_01lM8_UeH7OF6wK_FGgpt0erfn-lyr1cComtrpJbL2MTcOwPp3UEZkOXf2gDPuBwM3nm8mP38L0u1zgIdCoTN7soBvFWAc7DxGSxf3aLKow4BIDWS3pI4I8Df5dGLTDp5FjLuptnP-ZLqjhaE6TeFha4QumoRT5Elsa2k3SyM_OXDxGxtocxj0M3a94gT1i34VSJnGrADiRkQaRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab06fedf8.mp4?token=A6yDNOOFDCqGxVQXFEKreHh_h1hILUrHLQxFLMlsSCml_-vNcqJTfKs8r-sdoikVrZE45PrOBbvallfk_dWiRR25ufoCGMqnub8ImkLSMu-iglOhYuC067HzvK9CnJaQgomX_01lM8_UeH7OF6wK_FGgpt0erfn-lyr1cComtrpJbL2MTcOwPp3UEZkOXf2gDPuBwM3nm8mP38L0u1zgIdCoTN7soBvFWAc7DxGSxf3aLKow4BIDWS3pI4I8Df5dGLTDp5FjLuptnP-ZLqjhaE6TeFha4QumoRT5Elsa2k3SyM_OXDxGxtocxj0M3a94gT1i34VSJnGrADiRkQaRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از حضور مردم در میدان انقلاب تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/447374" target="_blank">📅 07:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447373">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db158f810f.mp4?token=Y5Fx3t-KQEnDZy8Wexjv9kA69Nwg6SCcDmAbDZlUAuH2j6XtExzJrSG4Xa3sFgpNWIcjXiXu1tm9RU1T_bIZVvO13jb8gvxRmWsiNxFeH1K0zsX5LMNp9ZZCIWZbXpYW9pTMNb6SHATLm6nYzGNhFH48E6IucEy_f4egQLz3e4NWxLjvjq0P0F3k3HUKMUmk5rnA7JBEkxo7tzLwr-FnIujZEmfHjCZxFM9fttmwAqQ5uHV37ePSWlHPKT51qwSwlCphx-v0a22YW_-bp_pfa39pU8vQNzq8A_NgGQTfwrJ8EXiToMo_7Xmdh8D5TGj0zV_G7R-El471JpO3clX5bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db158f810f.mp4?token=Y5Fx3t-KQEnDZy8Wexjv9kA69Nwg6SCcDmAbDZlUAuH2j6XtExzJrSG4Xa3sFgpNWIcjXiXu1tm9RU1T_bIZVvO13jb8gvxRmWsiNxFeH1K0zsX5LMNp9ZZCIWZbXpYW9pTMNb6SHATLm6nYzGNhFH48E6IucEy_f4egQLz3e4NWxLjvjq0P0F3k3HUKMUmk5rnA7JBEkxo7tzLwr-FnIujZEmfHjCZxFM9fttmwAqQ5uHV37ePSWlHPKT51qwSwlCphx-v0a22YW_-bp_pfa39pU8vQNzq8A_NgGQTfwrJ8EXiToMo_7Xmdh8D5TGj0zV_G7R-El471JpO3clX5bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سینه‌زنی عزاداران در مراسم تشییع پیکر مطهر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/447373" target="_blank">📅 07:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447372">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e16be4d02.mp4?token=EN_44pXJkccFw55xp7u0yJ6zFYXF9mgl3H_rQzw6L-EojVGcCAi4V3mwXTmTAEHuIe-W97-scUkyU4Y4E7Th2E65cMfJEMn0d9oK2jWGHvSfGraZuUf3QHrzJipQbawqy78k_PCgltl_PmM2NdBewwRhlTHxdsdcMHHfF3wtdaaF-xhcdc7LYBis6H-crprXCgz3qEMxxSN3VbzJAl8__AGOwtNdXdTDCR-SM2-xl6-OLsUNN17UWkVxlvmzJRt7Lf_2plvIhUN7Z8HNKuD9CONDVlaXBzGL1Fr1xzqwotE7aYC3OnZoU_UrQLfbVzw_VScp9pf8kt4P5nmTs1i71w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e16be4d02.mp4?token=EN_44pXJkccFw55xp7u0yJ6zFYXF9mgl3H_rQzw6L-EojVGcCAi4V3mwXTmTAEHuIe-W97-scUkyU4Y4E7Th2E65cMfJEMn0d9oK2jWGHvSfGraZuUf3QHrzJipQbawqy78k_PCgltl_PmM2NdBewwRhlTHxdsdcMHHfF3wtdaaF-xhcdc7LYBis6H-crprXCgz3qEMxxSN3VbzJAl8__AGOwtNdXdTDCR-SM2-xl6-OLsUNN17UWkVxlvmzJRt7Lf_2plvIhUN7Z8HNKuD9CONDVlaXBzGL1Fr1xzqwotE7aYC3OnZoU_UrQLfbVzw_VScp9pf8kt4P5nmTs1i71w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخستین تصویر از آماده‌سازی خودروی حامل پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/447372" target="_blank">📅 07:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447371">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9738eaa6fa.mp4?token=Q1-r2deu4e5skrnIAJ4uwrAKJ7U50F_TcOxNLrMbYmCkXutz6maII1ag3AxIqOVTzDwa5RZUfJerVpfQqxYZhqMBFBfJiNOtCiESE6H_T4LAAvf3-8xwlsBksUZfXa5CsY3ma788PoMnP_7b05oEzXQljt7NZLdr7cbmZEM0-ckST6-wJtVs8TO87ZZZQCWhK39pVhspzQbpEY3ro_3SXowLMmsqLUUlxlfU4rFpjE9koCWVy7zySelc8T24scpCzPUdd6Ab_ZxA-A5bGhhbL3lAaSbnLtXuJ184B_lWNi-y1UeJZZT9rk45NJYW5iKAq0wSX9sPxUytc9mt2iXljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9738eaa6fa.mp4?token=Q1-r2deu4e5skrnIAJ4uwrAKJ7U50F_TcOxNLrMbYmCkXutz6maII1ag3AxIqOVTzDwa5RZUfJerVpfQqxYZhqMBFBfJiNOtCiESE6H_T4LAAvf3-8xwlsBksUZfXa5CsY3ma788PoMnP_7b05oEzXQljt7NZLdr7cbmZEM0-ckST6-wJtVs8TO87ZZZQCWhK39pVhspzQbpEY3ro_3SXowLMmsqLUUlxlfU4rFpjE9koCWVy7zySelc8T24scpCzPUdd6Ab_ZxA-A5bGhhbL3lAaSbnLtXuJ184B_lWNi-y1UeJZZT9rk45NJYW5iKAq0wSX9sPxUytc9mt2iXljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: مسیر تشییع تغییر نکرده؛ مسیر همچنان از شرق به غرب است
🔹
ما تلاش می‌کنیم از نزدیک‌ترین نقطه مثلا در میدان انقلاب پیکرهای شهدا را در مسیر مردم قرار دهیم. @Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/447371" target="_blank">📅 07:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9582cdf2f3.mp4?token=WDfVQgMOsewEuZ2RaHqOgaCuk0-rlSyBTWPeuakWG-dzM1gMrirF03Gspc0FBL__-c0Kbqi9mf2jfdXWQxUNBV2O3BkvJY2xfSp6XE94VtDXOf5bwTyx9iohTysbgENhX4LWJq8LlrdJ8Q5VJG4rJd6BPuSRhCDT1uWgem9JlUvwL_Uq9YZRSPHVaECcQN9xfYU7Zi4aTKx4kjVsArIJC0dDlhhnnWC8dPfVMSIe2Z4UskknjjxPDrpAYEdTPBtoWrxEzQeB83LjGlQN-e4evSH1eyUB73E70mUQi9jKf72RgQjkTXAV_h4wATXbevXYCw9HBZunDSI06XcsLp0ldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9582cdf2f3.mp4?token=WDfVQgMOsewEuZ2RaHqOgaCuk0-rlSyBTWPeuakWG-dzM1gMrirF03Gspc0FBL__-c0Kbqi9mf2jfdXWQxUNBV2O3BkvJY2xfSp6XE94VtDXOf5bwTyx9iohTysbgENhX4LWJq8LlrdJ8Q5VJG4rJd6BPuSRhCDT1uWgem9JlUvwL_Uq9YZRSPHVaECcQN9xfYU7Zi4aTKx4kjVsArIJC0dDlhhnnWC8dPfVMSIe2Z4UskknjjxPDrpAYEdTPBtoWrxEzQeB83LjGlQN-e4evSH1eyUB73E70mUQi9jKf72RgQjkTXAV_h4wATXbevXYCw9HBZunDSI06XcsLp0ldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقاجان، اگر در دفاع از شما کم گذاشتم، حلالم کنید
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/447370" target="_blank">📅 07:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e11f66b5f.mp4?token=Tn_m2dUlS3Ywq5g5efy7vsJgHs3NXDumw2wKce9nmbzcZume9Q3YvLK5ED2tLutcZt-OVir9w7v9SoxbYgPhkrSEPJN3WCpJ578tulXOQn7xBGzc4V-5fca8cs0BO6917KlWt6Bvo4Jdyihz1PZIjTyku9SV3FQIlFtAIQ9vJyxukUUUri2eQj6VFGcSLG6ddRaI9UKH38MNgYAMlAcvt3BlLYkQihWl5xraLOkj93dRmQbPnoeRKKmxV75pj3Zcdb_BNk2Z3ikOHK7UqgBP0N75-o77_xTA4cD8cvd3GPdkLWjO5pU3b-urigYuF973-sKFMX3J7bWIc6NTnwAEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e11f66b5f.mp4?token=Tn_m2dUlS3Ywq5g5efy7vsJgHs3NXDumw2wKce9nmbzcZume9Q3YvLK5ED2tLutcZt-OVir9w7v9SoxbYgPhkrSEPJN3WCpJ578tulXOQn7xBGzc4V-5fca8cs0BO6917KlWt6Bvo4Jdyihz1PZIjTyku9SV3FQIlFtAIQ9vJyxukUUUri2eQj6VFGcSLG6ddRaI9UKH38MNgYAMlAcvt3BlLYkQihWl5xraLOkj93dRmQbPnoeRKKmxV75pj3Zcdb_BNk2Z3ikOHK7UqgBP0N75-o77_xTA4cD8cvd3GPdkLWjO5pU3b-urigYuF973-sKFMX3J7bWIc6NTnwAEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: مسیر تشییع تغییر نکرده؛ مسیر همچنان از شرق به غرب است
🔹
ما تلاش می‌کنیم از نزدیک‌ترین نقطه مثلا در میدان انقلاب پیکرهای شهدا را در مسیر مردم قرار دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/447369" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4df8d732.mp4?token=aRjonA3jiWoKwKafzF8rcGyYoPYR5NB1_qSntyAT1YoVkbzLA_JHmD28U8NSFyEU6xkLmbfTfOOBGN7RPDR56W374P3Zyw1d1CyX6_A2w0OncK-FjSjWhk-SygdAt0Q3t9nBJvKp2wrSdJuX1x2f8fF_JbaEs5jA9I-HgECE73UId0s5FlanSaCxiEODkn6_N4vlq4jtyoAiIqzqWeatHdfooC4e25ZmtPvIEvxwtb7Ih9zA39rItBiUiwhPmb0ze71MyNiuqZ9ix4HDBTgK0KG5VJ9-IaRavr2J4R6Jo5qbpLSKgGvYzOIUYtCkU9ld8fU7leBTVqWnMcLubw9asQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4df8d732.mp4?token=aRjonA3jiWoKwKafzF8rcGyYoPYR5NB1_qSntyAT1YoVkbzLA_JHmD28U8NSFyEU6xkLmbfTfOOBGN7RPDR56W374P3Zyw1d1CyX6_A2w0OncK-FjSjWhk-SygdAt0Q3t9nBJvKp2wrSdJuX1x2f8fF_JbaEs5jA9I-HgECE73UId0s5FlanSaCxiEODkn6_N4vlq4jtyoAiIqzqWeatHdfooC4e25ZmtPvIEvxwtb7Ih9zA39rItBiUiwhPmb0ze71MyNiuqZ9ix4HDBTgK0KG5VJ9-IaRavr2J4R6Jo5qbpLSKgGvYzOIUYtCkU9ld8fU7leBTVqWnMcLubw9asQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم در متروی تئاترشهر
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/447368" target="_blank">📅 07:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تمام ایستگاه‌های مترو در مسیر تشییع باز هستند
🔹
شرکت بهره‌برداری متروی تهران: تمامی ایستگاه‌های واقع در مسیر مراسم باز هستند، اما در صورت افزایش حجم مسافران، ممکن است برخی ایستگاه‌ها به‌صورت موقت بسته شوند.  @Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/447367" target="_blank">📅 07:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fe1c7d45.mp4?token=chAwvNPFN0uV3knS7SL45BZLGE7s6v3VgeO6D1oG1six_QsJJjVT49ySjyusAJMrhC7aBW2i272011azVXfTEbcFG3hvTYHqIDext0Z64wtFTZTPSn9kRIQudcMpoaC8tV6Tm6z8leFO8OG5PNTNKkoSPXREY1wQhCet4lJScgTkzW8mq2r3rhyFNpJAzdQvexkVoMwXT_ocvsJMgZfabV7FBvU8_gdLnU3RImEwFgXGuttkz2kSrzG2Ez5pJgr-q2fMeqEyzMn4KA40KTJrluImOw_fuqT4r8IMMsutycDua0Fw02CHY4pgDTGqh5PQS2aQKrP8wAYr7K6Hwz4kCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fe1c7d45.mp4?token=chAwvNPFN0uV3knS7SL45BZLGE7s6v3VgeO6D1oG1six_QsJJjVT49ySjyusAJMrhC7aBW2i272011azVXfTEbcFG3hvTYHqIDext0Z64wtFTZTPSn9kRIQudcMpoaC8tV6Tm6z8leFO8OG5PNTNKkoSPXREY1wQhCet4lJScgTkzW8mq2r3rhyFNpJAzdQvexkVoMwXT_ocvsJMgZfabV7FBvU8_gdLnU3RImEwFgXGuttkz2kSrzG2Ez5pJgr-q2fMeqEyzMn4KA40KTJrluImOw_fuqT4r8IMMsutycDua0Fw02CHY4pgDTGqh5PQS2aQKrP8wAYr7K6Hwz4kCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌ها پرچم انتقام است
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/447366" target="_blank">📅 07:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/624ee95af3.mp4?token=hLuKx1CwYEtv6vTioLER9qb6wmrpseCveilHQDbQBY0Mnr_EnzvsN2lm7ENeazH-vkSaWsChoziz_M6DKvVnugjrfjy-LChLF9IIY24kMFWpDMDZ1Rma7tPQslo3f8F18lttLPEdTi6cWHUxqWN9S9VKmNHXk1_GSKqaMQQms7eTXi0YvCwfwPHm8254Qbd_tqGodDccpcpzRefVIOgiQT1flacRoRFw5cK_LEYnO1hrpSF_Nyep1EJD1LIyXIRjCacGuKdfJ9fU9LZ7hz5XcX6ODB32EgCX-2t9Sf5FIrUvBOBUvQY6A6sVJb9J_1NlzviEisRpRS1rucqJylxiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/624ee95af3.mp4?token=hLuKx1CwYEtv6vTioLER9qb6wmrpseCveilHQDbQBY0Mnr_EnzvsN2lm7ENeazH-vkSaWsChoziz_M6DKvVnugjrfjy-LChLF9IIY24kMFWpDMDZ1Rma7tPQslo3f8F18lttLPEdTi6cWHUxqWN9S9VKmNHXk1_GSKqaMQQms7eTXi0YvCwfwPHm8254Qbd_tqGodDccpcpzRefVIOgiQT1flacRoRFw5cK_LEYnO1hrpSF_Nyep1EJD1LIyXIRjCacGuKdfJ9fU9LZ7hz5XcX6ODB32EgCX-2t9Sf5FIrUvBOBUvQY6A6sVJb9J_1NlzviEisRpRS1rucqJylxiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون حضور مردم در چهارراه آیت، خیابان دماوند
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/447365" target="_blank">📅 07:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
اسیر صلابت آقا شدم
◾️
یکی از موکب‌داران مراسم تشییع رهبر شهید در تهران، از حال‌وهوای خود در این روزها سخن گفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/447364" target="_blank">📅 07:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8e9c793b.mp4?token=t2iK5d8cb66kY1AQrx7MCu3tWGcIl5iKzXWog_kSJgJAzIDSHp-puQ-X3iKxK7nqx1sewsg86jngMFBeJJoOMN0X84zriBBef46vx8kkCpi1yp1v7B-CXjjThE8rKxqoQIQMYCSbSFxOWiUzNZKr9pu4bY5c2aUDcFQVeLyuHz0yVctknzcMKTNTbm9fmnHVi42v4JB4L_C1tFw6SeHHySdCuY-3QTGNPyP83BdZkX0sE88V5lAxVWJ7iOORap4E_wz97JRLPElgtjw2gXud0Z2onzm98cVRTO3KW9UEHg3gw3MFhGSYOe1vGbbZOTrkkpy7aolEe8IIiF5PtA20eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8e9c793b.mp4?token=t2iK5d8cb66kY1AQrx7MCu3tWGcIl5iKzXWog_kSJgJAzIDSHp-puQ-X3iKxK7nqx1sewsg86jngMFBeJJoOMN0X84zriBBef46vx8kkCpi1yp1v7B-CXjjThE8rKxqoQIQMYCSbSFxOWiUzNZKr9pu4bY5c2aUDcFQVeLyuHz0yVctknzcMKTNTbm9fmnHVi42v4JB4L_C1tFw6SeHHySdCuY-3QTGNPyP83BdZkX0sE88V5lAxVWJ7iOORap4E_wz97JRLPElgtjw2gXud0Z2onzm98cVRTO3KW9UEHg3gw3MFhGSYOe1vGbbZOTrkkpy7aolEe8IIiF5PtA20eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آذربایجان جانباز، خامنه‌ای‌دن آیریلماز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/447363" target="_blank">📅 07:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447354">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKK9s8-yN_r6-u0lTlloCORJ49x9oUV2F0DnLyLCOFglrOaLRDUCZFBPbhtYRirOcLssQW_0jyL4yeh96F5uc2yU9EyhbYdww02gcibsRoHcOalPAkkLFBftHLmQ0psbhPsMDxD28Faic1n4VWeQch4wgefSgNScNqDzxjSGyZjMYHDdDXZDNIyNUA-Imgh2JOR4jTSiz-x39aLqfdXx3afuk_UlNqVhLORFKp4g-ChEf72Oblfx_I6_1nVxfcgPFsj8kt6ZRM_gZLJyix-xIxjKmddN8mKcMFIopokz8pq2xENpZN4CsZLdeThwbcbzWO1-ZM3QHybiRh9JbI4ldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTMjbjBWkbT5UAolDpwWRR8dLnOvpe42JWXZzNK9nxH2D9-2yTG_nkq0_UAMaqnhAVHljAqpL5U38nJzaOtKZdJ2HZUfzgROwmRPgf-vm1xDB05X2xAJXbtAmfhQrgiJL3wQDD0LbZ4mpdCMOPHdBQgpPDV4LPcejW6TjXCVOkT7efutIRHdW8GM7nyvRyfPuLj9YPdm7nTLeO6lSFtRARZmX06qOPSy-sfo4gG75X4YyXPv2VOektP71Q9zmn920feWNO_l0w-ZOIoo7eIf0L_5liJuLh5SzQmWwOP1_Q891EGW8NVjsC2tevJbV6H6BocUjdG3GGE0q_GO6kTevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoW9NljlLqqsjdSBNM_Qn3pnx2ykkElkFme3T-Wca_s9kdozmF4xcsGOLbhEaWxo1fOfgGBtlE8SJcxYNKqqxgpxBxVsMiA9g_Eoddvy6qOVqr8Ha38C5q9ctk4yY_8q8grk3wSqecpFD4ulDQKRoP8oxSdGZ-a6P0lfi56YdlugiHefq5YDqUjNtN4PjEL87XXjX_-Ozla7Fccc-KQBT4P1axJoKBgVXWwGYNkgW1TGe_RuddpR5qx1szDf8ueBR_obvahgaog5dQlHTLeORZt7bTVvybBcwUv9oYTti7PL6wPxhS42VFMDdwzeJMy-uDImwO-DaOEml3TB9bTMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXhLmUrltHpPTdVVf_j29aDCQZJtA9G1C10v0u-ItuwJTFd-PfjpBsw5puNuW0drhkQuVrqz4xeYVpGl7zkHXQg1eR0LojjS18NehFHFgQRa5exZxS7n69m1Nzj1sQCoBDbNy-60Ymqx6TntDqj-K5rV3Ktqh54LPep937KAYHLyvTx6CLS5kFdWZhcnokH3J0MzoO4m3zxjDo55Rw7EHxuB5RZkA6Pqqwqx7coUVKv0ZG8V_AdQnGE7tIDM4Olr5KbIFRTXpsjdp6hxQST2H2flsKgqBVNRXy6oyUeLdDI1rnbzSca8Ziul5R-iXwDII1GC-gvG2spip_LQQhHkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eP2cfq4XChf_0M0GZ9HHmX4mnLqCDBlP0LzPdUq5FqoGLUGyYq8BQrZCUB8vb2ZjlFyzBKCnMhXk9QD7NupH6EbvZMsaaalVYd_Exo36zqc6jBy3sJC3W9MCem6o8KghvV7Qe6o4-7OpaYr8xfX1LEqs5OkyyTiTReqJviI7SWyLgezpFDRA5NKvY-oERo1TskVsbkc1Vy-TtmGfKJmEb5ozKLizxQrnUU3SjWhgp3WN945DFj18N7JFrckTSkgRGz1vdRZcJ3RS_h4uMCvX_26IyVBDjdrF73K92Yjv-JZd-FnrTDR4ARPPtNzO4X_lEhVlmK-SRZUC7T_K1TniHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuxyeoGdooMxvmsZ7SLgyBczbQmIkaqkIN5-c52BZTlRrCzRDfQfw7wzG2oWL6y2N2tnAPBCa7dQ8XDHVFsZEFNsV7VsfXtS0Ma7Ve4vpVNpeQfNeMVe7Nxny7eIWB8Io2KP5EB78EfRDLsy8A-uuxwRBkZIDiYq8rdCyWmahpJt_pkBjaNrOCxK9Qxebg0TE7d8znTg7gwECgxY-t7DeEZe38nyrhc4K3hGIXgcSaviwYsdNXPprWloKxsW1RF7uFsEgDDtjCoQOckvuoXC5twy6bR9rMEWuQazARzBPCJOH9xdk2LFidUSVYQ2oq50sgvygHIbA3651ZNjVJYswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7btAn9OGb8SG_fQaB9Xug3GfJA3uf0kYSyU41gZdnETOWPLAOrkBywnsFrTm71od9mGkLUfUYIGwq3ctWASQ_MtVJFwk8olcLFmrfuetM3Tof4HQTB5f2ZjdbTed_SMUKThVKxJOffkH5yNw3scjSuf3SQZOsTDoSQmphSaHxWzKi-GahEar8TIUwskrdZEmZ0u2wemdiTRQOOsGUhWFzDXIopM25qHE-0U7EyjQ6T0Gn6Wjrx0WbMx-05Ga91fuc-QOWZIH5IaM4cf34EaINLytAkxab3LyAe-nGLuR15EnvrUugnLjWGTRX3CzAATaTEBlkc76fEhRfhnrYxNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGb9qL2ANHygIpz-Hz4mD8YmiLAfYzbtYFM7fJQAnFjFZV7fZ7fsrO3nR5BMRT8lIwLwQFPL62QOxXvtnbRURptxRB3-2ipJzrWo06gDp5-nLRCA2sRB2ohOJIXSnzT4tOhASnday97tQB5Y806z3MyaLj87AmuixHzptlkqMUv3mJdVXlMwawn9ki6-MBbuGNeXhsN_RPMoeBq0TGzblXSPYl30VQ0tpOuZ8T3ZfK5BfzMqGWFBdU_Sv9_h5XiTTDqSS36r7VWItDKvBT2oPEI2EA61n8PEnexSPY3PGKQnYrRbmlJEviYlf455EL2kigZl5_PiQhWZWrL8dx5hYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fv-_erl9cuATfahY9Rr9l7GhVCakhf8FePk6FwkGaY7lgulg2tyw3sB3RY8wwNSz9SKyRi0HMKMniujBuS5Jho3FcXpUui7fN3O9CPlGA6jw4oHMlTlYMAzbJPu9VvE3xbTdDiM14OHNmTd6CZqfvaasCqA8AvK67GaDiXAXTgmu8Eau8YBqACAfs9vAgpnZKePJAIsN3XWIL1juJ12Sq_d_JMbHwgyJPO1Aw4p5JdHaXWkitXJ9Y32sfcwpOk3PpEtG8PzejIst12RHbIWS1aG77CQJ5xdXwVU7nKDRHiIdbPeUtBpAdMwPeaXfKajHiP8JzqZauCWxlTda-vYnLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یالثارات الحسین(ع)، یالثارات الخامنه‌ای
◾️
مراسم بدرقه و تشییع رهبر شهید انقلاب
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/447354" target="_blank">📅 07:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d381a31e.mp4?token=ePdcasfi_VoRevNSrpW0DFcfbdDpzxNIKWPucb-aMwxAxQGhbDYlHQiSo3_XThGMnBwhiRfU8WkMSKdvxMY7pzG1tE-edCacth_RYP759H6x-FsjXNPX11F6E5S_pqO_8l2K5607sSVE2coxAgg16HOf3lQAFBIhaKldOuqg3xqodheeMjgqr60fSjMvEBKmE9JDovQgk_Vw8q-nCCf82fXXnFBWqcmaqieUESKUOI3g9N9WMhNI3Pz5s-uu-iSr17VLuqhjnIBHlKEBYa8z5H-iLkNEFOqn13BF22nOUuKfVHPSOVEYSkyZd6xZieyfcdepFH_nMM6TG_wMhSosFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d381a31e.mp4?token=ePdcasfi_VoRevNSrpW0DFcfbdDpzxNIKWPucb-aMwxAxQGhbDYlHQiSo3_XThGMnBwhiRfU8WkMSKdvxMY7pzG1tE-edCacth_RYP759H6x-FsjXNPX11F6E5S_pqO_8l2K5607sSVE2coxAgg16HOf3lQAFBIhaKldOuqg3xqodheeMjgqr60fSjMvEBKmE9JDovQgk_Vw8q-nCCf82fXXnFBWqcmaqieUESKUOI3g9N9WMhNI3Pz5s-uu-iSr17VLuqhjnIBHlKEBYa8z5H-iLkNEFOqn13BF22nOUuKfVHPSOVEYSkyZd6xZieyfcdepFH_nMM6TG_wMhSosFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با توجه به حضور گسترده و پرشور مردم در محدودۀ مترو دروازه‌دولت، سیستم‌های مه‌پاش جهت رفاه حال مردم فعال هستند.
🔹
هم‌اکنون، دمای نسبتاً مطلوب و هوای مطبوعی در این محدوده جریان دارد و تردد برای زائران تسهیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/447353" target="_blank">📅 07:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447351">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601d07abd.mp4?token=dalISB_0vdaeANKFUr_CnJ_KlY09nNMK0PCo_UYx2Z0LgO1NovxjDzn7RGrxBIR3PiCWrXpOtyzcQO1U8wIs0_tecc5tLz4N_e9E4mFZH1Mqm9jxG6tXyoAyqmkmy0LUmspw2tG4feMcKCKwDjYR_rvQKIK9BSv-2VxUXbXSKa75DCsQyvLtEgdHoGW2smbtRbc7DKiBe7oREmN4WmVS2AMPnwNTVUVPS6NFh7Cv1MCvK5urQ1WWbpy5v8X3kLWNatC9AM3tamY7arrnXXu-dDTA1MAyT52lDWD0ChknEbdO7GgTvQzPhTjgZfLX1_AQh_lfchnJBbZO_0ApZBCLBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601d07abd.mp4?token=dalISB_0vdaeANKFUr_CnJ_KlY09nNMK0PCo_UYx2Z0LgO1NovxjDzn7RGrxBIR3PiCWrXpOtyzcQO1U8wIs0_tecc5tLz4N_e9E4mFZH1Mqm9jxG6tXyoAyqmkmy0LUmspw2tG4feMcKCKwDjYR_rvQKIK9BSv-2VxUXbXSKa75DCsQyvLtEgdHoGW2smbtRbc7DKiBe7oREmN4WmVS2AMPnwNTVUVPS6NFh7Cv1MCvK5urQ1WWbpy5v8X3kLWNatC9AM3tamY7arrnXXu-dDTA1MAyT52lDWD0ChknEbdO7GgTvQzPhTjgZfLX1_AQh_lfchnJBbZO_0ApZBCLBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزله و هوسۀ عشایر عرب خوزستان در سوگ امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/447351" target="_blank">📅 07:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a8c2c68a.mp4?token=AWNMAWEoMYCdvRYaofnturYw-q_eKvVHvmHGVtDvVLCCbJPoBltKMoEScqA5gaQHnuaFo1w530ycwaw4meJDHFiT2xIbRrYmn4MeVPtIKJ5TFgczCxkpRBecpy2DcOpn0_NZnJcqGHXT8TcGE1Gmn7Ex76Si_GNwaJKVqP99jF4Q2mO6g6g4QvmDL86SiSkbV9-qJAisMK6n98SWtVcUJOAwCN58zGhEYkO7Hz5sDCp9SFIYmeOFJ8qzLaUZfjNcjyEEYz6yHriTPtw2A4Gnv6NAfD1ExZ4JWrVpjG6aaRKEUYqGR5cxu5CRQjHMIXEioH75foT1QsM-JdsOW2hgHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a8c2c68a.mp4?token=AWNMAWEoMYCdvRYaofnturYw-q_eKvVHvmHGVtDvVLCCbJPoBltKMoEScqA5gaQHnuaFo1w530ycwaw4meJDHFiT2xIbRrYmn4MeVPtIKJ5TFgczCxkpRBecpy2DcOpn0_NZnJcqGHXT8TcGE1Gmn7Ex76Si_GNwaJKVqP99jF4Q2mO6g6g4QvmDL86SiSkbV9-qJAisMK6n98SWtVcUJOAwCN58zGhEYkO7Hz5sDCp9SFIYmeOFJ8qzLaUZfjNcjyEEYz6yHriTPtw2A4Gnv6NAfD1ExZ4JWrVpjG6aaRKEUYqGR5cxu5CRQjHMIXEioH75foT1QsM-JdsOW2hgHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل عظیم مردم در ساعات اولیه بدرقۀ رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/447350" target="_blank">📅 07:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367cf4053d.mp4?token=n5EDZceBZAhBlA6Jj7XurJ_5_7gqux5tP-zN7mAnh1hcjkjoIbhpyt5DEzAhgQnsiggK_PJV6ZgFRMXVAnC40gW3oJlZqbMWNrliyFTxDr0tirg5jXLxadtOQgspfgVJbbYe7CvQZ18zP0i02UUcXESdcGDR3SIrsU-gQ9K24vZlk0Wevr3_HvNA8BxoOnpoqv6PojzCKCfanzYEFjSF07qVwOBIZW3U3Yvwp44ubfA42X9BsLVPHwmcaIZEQigoe9R-S5K1FJgjxRhWikXVmh6dPAZXOsYmAo2pK7EWmovnXxZjjjCDYcq3Kyi5TT3WJIE3oVzeJrZELFaQ4PVwog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367cf4053d.mp4?token=n5EDZceBZAhBlA6Jj7XurJ_5_7gqux5tP-zN7mAnh1hcjkjoIbhpyt5DEzAhgQnsiggK_PJV6ZgFRMXVAnC40gW3oJlZqbMWNrliyFTxDr0tirg5jXLxadtOQgspfgVJbbYe7CvQZ18zP0i02UUcXESdcGDR3SIrsU-gQ9K24vZlk0Wevr3_HvNA8BxoOnpoqv6PojzCKCfanzYEFjSF07qVwOBIZW3U3Yvwp44ubfA42X9BsLVPHwmcaIZEQigoe9R-S5K1FJgjxRhWikXVmh6dPAZXOsYmAo2pK7EWmovnXxZjjjCDYcq3Kyi5TT3WJIE3oVzeJrZELFaQ4PVwog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از خیل جمعیت با پرچم‌های سرخ یالثارات الحسین در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/447349" target="_blank">📅 07:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447339">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHjS7hc59M7_VPoHw6zRFtmHA-RGMTo_TEcp6maGtrCpuFNY4MfGp686ZsFXfXIyPS33zDtV_Jo7AkoJ3vi9fsA9BT7a6-ytDzwfc4pna90YhybhAD8m4fxQ5gxXDDBAUECWFSy6vYuSJ7Dm2cbfudL4LoeUR4NLahESyrHCiyfeiOgtYAoe1URthaMdFEQ8bb_cnAiwlmqDM1w8OnY11FcEFg4dt2TXaHj8fY-aUVIo4MpIZ7Ku79qyjvWzny3RFX3QbumITwtPg5Gwghgn7q8h9ef98Fa1d_IB72E07RnmsrcU2BLA-thHr1HvqlQWqEXYoHAFLavDmL8k8wgvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DE7QScq8VuVyOkWenIca3ynfe8SqvtBxZtvDXsIsvSLpebEW1zpv0YKNZOHGqNVjgMQMvcmXPujuxon736llhjfHsaFHAJ2ipCOQ3O2CZEZQ_795X2Y6K41g9vL1NAKOTzOXJwZh6vTepwUy_lUSQuQHU3kcx1OXxGAZJpyvsF9FLAj6kH3uOCk7tb2wEbB5vKTMs5xeEQFX4pjIbbUGk5zrbNyUgogTVDbuFjmJuIIAIWt-2SC4O2W2I2ccuIbHASbjnKIwcM4a1yrYo16O3ZRYyh1AmK_CQuUTMRKFEy99KDvwpBxBLL6blR6n3z7Z70xIsbOWrTDdTt8TzqWa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-VqoQAIMPKt9DVcRdntZR2E3jljgZ746_jlnWKAlFCx2TG8QXsdwL_udRiVbFiloZO9c00-oXQzVWDAxxGS3XfadyTDMnnAmjdVKpxgca1lA3v0GWMRiu41gHwvg8wIP-aQt2ROrz_BThkFQSvdQ8y7JqWBQe1PXrpwk9FTx-4hy3zKu3VwKJRTOmGShYgcndZ3pNk0SF1X6o0UkS2eLK79Xyb0IeAn_YsFV2lgkgQiBlM5XLY8c-wvclT-9KcYcgkyLQrVsMQrTbH_pVOuHXDXNii1QYtzgjdn4S6lZ0z8uCvpNKh9Tf-BfTbqCjCmbaDfnCELmh90cuRN-yR2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbHywZhCs8O071ouvTA_jdHWfrUzjH78jpU57yXnEZUHp7bqN5M6UUQ_zfFIgreo4A3aaby6itLbLkIcjBI9a7Cl8hgBMZf88QLoD3r3ruSyi4lI7nTTy-BFjBuduGDaFXhn1cCEbn1SkzRUxrD4zaVnpnYTUkZYktEevBdFqEauKs3fTzcF15Fepr2BWoLXRxh5PBn-Mwd64pMcwHjBjaU0_lEMDo63yyt41TZaltx7tTi3M-JqtBx6Jb2-lTguuxCaCPnpra3V1hO0CKxt50BHOx8IcD6WwY9uPBhaS9yWB2o_xmYf40l9aGZD_Ij4sgYyHfcW_Yk2dyU9KaPJ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUCY0ADw-Aajmxfq1jr3qWKqeBxX0stmn_cLrYq-O5K_ek9sAeWstwaYSlF4IwVIMR1fZShJBMNC5HO3tOshCH5NxVcnWsgvN0FBHepF7p8Fdwi4nPchPzMi1FT13m6e038yVj5OEeHCN_lx8aRIJZVXFZNwL7lrtp1Iu4svIAo7lwLvN-kGLUi0YT3XHTSc3LlBg4RCBHTG0dn7jXD466Db2hyi3UUAaVRcKrhy4CvaIqH5mEO1htmgvH_iId66Xkjt-xb74EZs7uuxm-_ZA9D6wCMNG6TYxiYld1K3Kdq6F-xLMtm7m4WyGHqs7IuXQk70CcpZym7x6GP_o6FZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rY-xJYgXRbyIFqIDPS2doM07M3ZbZtW2vfGRwuOKgle3sUoXOoTv0160UndFul1dPs5Gv9v4xgONgIl_Zfh0fEmLYNtTRDvp7IggdJMODlU2vOSQyIIvZ1BSk2OrQjMOBde_7elpN_S_na8jr95RH_9k3GWPNxbJDZJ9k90pk78wJmuFjbJU1T4GhF2Ci_-0ReHcHsF82Oq7_umSdZr1slARyGoqEUP6ynWvTD8mrtD1GKvkTLuEXKsZzBSgxNNSXHds0PHOaaynBWXP9aF7dAJnmmxW_bB7kWhOnoMVsuG2QKtz-BgCh_fH_I_JYfmuyf9IkM41TI-USOAbXMtqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooqpOIXTo_M8Ta4vuwf7zlkGV4O90Www-XO-oR_4GO1vtfxpFH3b31tdhERKw8pfGT-RaEtQU200nPHJj7EMyl-qNjcQyipnXh-130qU-iFf4WY0ba3GwC9mfMyJRS_EabWXEnInqilYZLiFmm1SHK-JbQsZBpllvuro1MQnBUOLdqlWJ35bUQxMLf2EawoXQkZF2NzMjrRsg4TCisKiYm6huJ24Jy-WgEPaP9Tn3DQI0hwjLYXaAfb_6k5OUWl3-96hTkjOf6Xi3vIrWuau-JHjoSE4uvEVsEv-1uREajUUa3150hk24nnGUkGRGe6BrYcaUZoE0-re65IF9h9Uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJBr3q6nlbnrPH0wvkvwkF3X9D_DYaIq0UJF4Re1vkyqs1WNay_--sntz1u0ZBEY3bq5qSQChMs8Y56nJAY3Ow1o6YaFSYI03iCXf9_lnYpfPqYcDvBZW5lCZKXukElI8c-4bXXHzkni_Hg-KCF_RZ3va2EECFZHUhUCTGC-5HcpFRE993rBABgwjvTxsVdLsdyK-csD9mkuG4bRevIWVvWo0QYt6vQG_ngsrpbriqXSGWfm1c4s3Ix-ZYcIu2lqukIpYc6MBdkklr8uVfHSr7oqD6iXuLVonboYKIhhYahv-jgSlt0bx8KrYLBcblTVtliHImf5HHv9Ur1GaYWhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjSe3xwoJWF6Wjo58T_ubSTNLFMcEIpi4ie9KYi23K4pdBGg03K2DrPMaKx1cgDWF30b1voIMkajv6c0pB_NT2QSmL0yGZnIlJXj70KsefPGl13qHlNvKj_yCoa1-3ozSz7sud_LvnTgk-LQG9zftUTETolYFuUbkkcOr5e5dbLzJJVAxq9A7x0LMgLj3ofAopsjSaIVkVZuF6yDqOr65rj94P7-TDcncnjdmpxkY_HflgA44VrlwI4nFoQqmAl5VRbaJ5nOt56NlTRxmVO77EGjW8QurenzFZw_FYP9JlPVXj1PQ4UgbAE8I190V5m-D03kVxMTO2IH5eC5vrf74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfGeVLvhRce3TymsCN1kCpsq07XYOsgG5ZfpoEjJsjYSQJBamqXDbtL4Up0cz9yMT1qnz4lKFgDvvpMFjueG0YobfSouKic0x-Qwmich-uK2ogp5f4jyaj2OvhxlkssjCykLTlZoqKqEs4gwJrhdWgwsxhIuZehOIoy6EiyIjx8oY9c_w68ztNDcT76c6vviV6-BIKc83lzMwqpre8Egr9Za6U-CrsJZfzl1Y5LqK7MmWE9j8ZqIG99vMtVAyYwp4cdKXZNf4CF_FSk6aCpGTylqXxomQbZfRBQaMs_mVSipH-0p6pEpKtLn-TFGuQ3T1PW8Vxro36L1jC3cY24b5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ما خون‌خواه امام شهیدان هستیم
◾️
ساعات اولیۀ مراسم بدرقۀ رهبر شهید انقلاب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/447339" target="_blank">📅 07:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2ac4fc5d.mp4?token=LpGUd5UDiFtZekBCsdJmY0jkQMfNVQcsWGKI3ynWeg3-eIo9weXZ507aE7FOSn9AEPiKZt6jnSW7eqIR_xOfAx8Rk-GbB7rRKI144I7_41-K5ePILwQ_H4tW62fPGu2ro27CJJPg0QNkqGmGUYwizPzIvWUH4R-ZTbr1sYAusMR0QvFpENa9-yHjL0bzAwnleGOTyFLAz8qy5noPAKElE4C9TD8chB9QvvZdp1lGhyQ89cHYMQgrtUtb_3loayN_F-nJl4NJmKdHTgeNXqP5aRgZUNERpXCJoNXtgf62ZXxAqbXEB7_D6ZeRN-M07eLh1qL6brYyuSwKgZRASYF57A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2ac4fc5d.mp4?token=LpGUd5UDiFtZekBCsdJmY0jkQMfNVQcsWGKI3ynWeg3-eIo9weXZ507aE7FOSn9AEPiKZt6jnSW7eqIR_xOfAx8Rk-GbB7rRKI144I7_41-K5ePILwQ_H4tW62fPGu2ro27CJJPg0QNkqGmGUYwizPzIvWUH4R-ZTbr1sYAusMR0QvFpENa9-yHjL0bzAwnleGOTyFLAz8qy5noPAKElE4C9TD8chB9QvvZdp1lGhyQ89cHYMQgrtUtb_3loayN_F-nJl4NJmKdHTgeNXqP5aRgZUNERpXCJoNXtgf62ZXxAqbXEB7_D6ZeRN-M07eLh1qL6brYyuSwKgZRASYF57A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روحانی اهل سنت: حرف و عمل رهبر شهید یکی بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/447338" target="_blank">📅 06:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447337">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/447337" target="_blank">📅 06:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1P3FWSymMAZvVIGEYfnHKRuqdsTl27NhtiNXaZKBsoQn978wCT9QASrCedHCbupVC7ig7DiF7roqRmlgqexgM5swkIoZr0oXn1-4vQYl_4pZFkMmln-o5kTHKq2JKFm0mMoff7gtQdkcn9M3dQwTEhiDgv9qHIBCXDf81c8KlL-Xuucab3RAYMtpz3dak-w11nNvDho1pVO948Fjylw8GUR-L_MVKhhDyia3NKWrEk0z0cvrQ_M8i-sl23FeZtTcGEDsm1J-nyAv1AfbSHWa8aLqBJ1UEVN3iq_VUw2w9xW7fhboxyyjdLDnm4xbDqoDLq0RiclvisuzY-rLhrlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
مردم غیور ترکمن هم خود را با پرچم سرخ انتقام به تشییع آقای شهیدشان رسانده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/447335" target="_blank">📅 06:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
خیل انبوه عزاداران و خون‌خواهان قائد شهید امت در چهارراه ولیعصر(عج)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/447334" target="_blank">📅 06:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5c64b1a1.mp4?token=ZCa2IBqEFUOZknu2dBgHBEengKDAiAB6qE_RY44NsWi326bRY63chngI2KjKcCPWQyZ2Yq9Q6unCKjL-A_pCT2LYwTQ3e7PjMbr_kXx0oL9MNgGJw_ort1NbmSrI3ps2ic6CEgoee27FLOCEkg1IofwRKhqHI7Gn0mD0NEqzhoS_2AbZZKNaHeaxJLmCiIucdngXRk-xDbr3qRIZgCy-b9KRtxFbV-F-x3TkUjNX5Luih_Nz7lw3ZnHDQRRtE4XnQ0fe-qfslRMeEDKFD2neVH_cD7RxJg1OBbjzrtKDTgDERtX22VAbPEU63Tc6dklsE_XvfEgVYtGKbnbu77W9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5c64b1a1.mp4?token=ZCa2IBqEFUOZknu2dBgHBEengKDAiAB6qE_RY44NsWi326bRY63chngI2KjKcCPWQyZ2Yq9Q6unCKjL-A_pCT2LYwTQ3e7PjMbr_kXx0oL9MNgGJw_ort1NbmSrI3ps2ic6CEgoee27FLOCEkg1IofwRKhqHI7Gn0mD0NEqzhoS_2AbZZKNaHeaxJLmCiIucdngXRk-xDbr3qRIZgCy-b9KRtxFbV-F-x3TkUjNX5Luih_Nz7lw3ZnHDQRRtE4XnQ0fe-qfslRMeEDKFD2neVH_cD7RxJg1OBbjzrtKDTgDERtX22VAbPEU63Tc6dklsE_XvfEgVYtGKbnbu77W9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور باشکوه مردم در دروازه‌دولت در بدرقۀ شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/447333" target="_blank">📅 06:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f48c054e.mp4?token=E1O99ZzOfcHA05XyuT2UJo8UBg1UkuqixBvhIFo9hGgyn5C7aIH7wS-LXfwsvoxFDV-1PEs4AEN6jdkZrXe0OOTOXKtAHbvLb53BwsSughsKyK1I7m-SW8fMBhBCbfbX64onhGNRjBi0WOCQpC25mrZrgvFtr5p9AnfC9Ubffb2Xpdo1zSrLo-BbeqhNgU-fWquebF2WhSvzE-IShpqFdUQx7EBwtFZuV7nIn_gXOekxGNi2iHdw2Jv4VENa1JXUK7dGaT-l_GpBE35LNI7bnwonJAlptgiG-Sui8uC-xnUGFYN9OghTf0JTy4WmJq_PgICu7d3jhunlDeJ4PE-7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f48c054e.mp4?token=E1O99ZzOfcHA05XyuT2UJo8UBg1UkuqixBvhIFo9hGgyn5C7aIH7wS-LXfwsvoxFDV-1PEs4AEN6jdkZrXe0OOTOXKtAHbvLb53BwsSughsKyK1I7m-SW8fMBhBCbfbX64onhGNRjBi0WOCQpC25mrZrgvFtr5p9AnfC9Ubffb2Xpdo1zSrLo-BbeqhNgU-fWquebF2WhSvzE-IShpqFdUQx7EBwtFZuV7nIn_gXOekxGNi2iHdw2Jv4VENa1JXUK7dGaT-l_GpBE35LNI7bnwonJAlptgiG-Sui8uC-xnUGFYN9OghTf0JTy4WmJq_PgICu7d3jhunlDeJ4PE-7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه آمده‌اند، با پرچم‌های سرخ انتقام
◾️
قابی از حضور مردم در مراسم تشییع رهبر شهید انقلاب در میدان امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/447332" target="_blank">📅 06:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28907d739d.mp4?token=W176tCe6Qf-fcYFrgG-nCNSxDT5ApyABMhvObAJ8dEVvFnTtGq4BZYf9DE4zwN7B8b0hNMJYV5MNYjxJ3nEb7pWQb9AIySJhr8tESSlW9uX8yGfikcdwP7JWtoAgExJOFb5hJEF9l-2zmr8YFBgC9zkjD_siY1HjdzPxu16L6j_Wn6XKF3OQUlZobYgaezOOsXbBt_1buZBqYUSggHBeIqaG81FKDImbnqB2kpOd6tkSL8MU_uch9PASHOjkHpeyLRWt_kJdPeBVD_QNg7szKsnIMK_shsoTr5AG18ArtqMxhopQBv5OwOx-iX9SIYBFOQ5UA8M6Rd7C8rE0yIfdkIKBy3y6u_LHicO0jn_q7yu7-V3No_IkokGp8eN3UpytiSL2W5iRe_JOCZOuIiBQa_wAPF6kGlHUcky7Z3W3iyOwesf78KjZvaAA9ryezlP_ttaL7gQG-vB9QtLD2nEAeB3dCLGMN0AzCLGj-a0ZtQ4u-DpwCxJqAuLP1PKNqKvd6JvD2SwDFCCEqpy9_Dm81emUzhdayNlCM2v9QZyFjtU6q0U6nj2uJx7uGdYlwOdxO5UjfIKY8W5Hjco7p5PWSnV2tOkkPtEPhnYMS1AVOYMFC6ms2NbYWh0QYEAzHZeGj6H2vFfCKI3UtTOMlrxieEAf-AdrKtzCqb2EZ9xhC4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28907d739d.mp4?token=W176tCe6Qf-fcYFrgG-nCNSxDT5ApyABMhvObAJ8dEVvFnTtGq4BZYf9DE4zwN7B8b0hNMJYV5MNYjxJ3nEb7pWQb9AIySJhr8tESSlW9uX8yGfikcdwP7JWtoAgExJOFb5hJEF9l-2zmr8YFBgC9zkjD_siY1HjdzPxu16L6j_Wn6XKF3OQUlZobYgaezOOsXbBt_1buZBqYUSggHBeIqaG81FKDImbnqB2kpOd6tkSL8MU_uch9PASHOjkHpeyLRWt_kJdPeBVD_QNg7szKsnIMK_shsoTr5AG18ArtqMxhopQBv5OwOx-iX9SIYBFOQ5UA8M6Rd7C8rE0yIfdkIKBy3y6u_LHicO0jn_q7yu7-V3No_IkokGp8eN3UpytiSL2W5iRe_JOCZOuIiBQa_wAPF6kGlHUcky7Z3W3iyOwesf78KjZvaAA9ryezlP_ttaL7gQG-vB9QtLD2nEAeB3dCLGMN0AzCLGj-a0ZtQ4u-DpwCxJqAuLP1PKNqKvd6JvD2SwDFCCEqpy9_Dm81emUzhdayNlCM2v9QZyFjtU6q0U6nj2uJx7uGdYlwOdxO5UjfIKY8W5Hjco7p5PWSnV2tOkkPtEPhnYMS1AVOYMFC6ms2NbYWh0QYEAzHZeGj6H2vFfCKI3UtTOMlrxieEAf-AdrKtzCqb2EZ9xhC4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهدی که تمام نمی‌شود...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/447331" target="_blank">📅 06:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1499fca.mp4?token=VYuW3qt4n_-FR4SIY8319KX-lNCfgsbcCDxUUaHMJExdrTCoEwfp-Cz5JK6Kyy7oqaCuq07XVOMakzMyGjI9q7cJCA4_AG4bkJMKrafbzUFdBPnTccMTFZYSKHxqUml3nS6l9cyGMZeCdKEGXEqDVWotkGrW6eATzh6m1ieHWwYyF3yjhwFIDW0jGYjGed6ZyNgDSrunyX1ZdU8SwKZvxUyqrmeek2VL6_jjI8-rTt3hijJwIf6b2L2PUGffBQtx61PF8KBalvirZ-M9zP8DNw-Bs3LpAaEYwfWXSitrdiK0iExQVII7tW1liKUsSaRtDdP-ca43vthdPSIKFueHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1499fca.mp4?token=VYuW3qt4n_-FR4SIY8319KX-lNCfgsbcCDxUUaHMJExdrTCoEwfp-Cz5JK6Kyy7oqaCuq07XVOMakzMyGjI9q7cJCA4_AG4bkJMKrafbzUFdBPnTccMTFZYSKHxqUml3nS6l9cyGMZeCdKEGXEqDVWotkGrW6eATzh6m1ieHWwYyF3yjhwFIDW0jGYjGed6ZyNgDSrunyX1ZdU8SwKZvxUyqrmeek2VL6_jjI8-rTt3hijJwIf6b2L2PUGffBQtx61PF8KBalvirZ-M9zP8DNw-Bs3LpAaEYwfWXSitrdiK0iExQVII7tW1liKUsSaRtDdP-ca43vthdPSIKFueHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ‌بر آمریکا و مرگ‌بر اسرائیل عزاداران رهبر شهید انقلاب در ایستگاه متروی تئاتر شهر
@Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/447330" target="_blank">📅 06:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
مردم عزادار با پرچم‌های انتقام یالثارات الحسین به مراسم تشییع رهبر شهیدشان آمدند
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/447329" target="_blank">📅 06:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تمام ایستگاه‌های مترو در مسیر تشییع باز هستند
🔹
شرکت بهره‌برداری متروی تهران: تمامی ایستگاه‌های واقع در مسیر مراسم باز هستند، اما در صورت افزایش حجم مسافران، ممکن است برخی ایستگاه‌ها به‌صورت موقت بسته شوند.
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/447328" target="_blank">📅 06:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/365c1f58ce.mp4?token=JMB5WCEnRk69-2SYR0J9jaqomTlCNJTKN4MuXsU6YgsGoWikXOh_Gv7wfUJvvDr-BGglDji8YwT01mTPMdds6AZRe1LR6vdgUT0WJy2HbQTTJdXEYLwWHKfr3H3DeaAIHqVnq6z79i0fCxeMglxFBNgdl_icz8i0sE4-Ty9zLXFC-71uF5bcmIzVcS0Ht5kez0cEC39LaWmujv0Xoyo48RDoaW7if2Oz0fLbtg1MvSr-SF8uP0PSitGouhfBUyRhsEovY6kzJCyscdIb1TgAD0tiN-d3dxh26vOMNgEcSWTx1IX0u9elvGA5OdIpwlCYH5E9wMNHSTGFAD7y_5WWlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/365c1f58ce.mp4?token=JMB5WCEnRk69-2SYR0J9jaqomTlCNJTKN4MuXsU6YgsGoWikXOh_Gv7wfUJvvDr-BGglDji8YwT01mTPMdds6AZRe1LR6vdgUT0WJy2HbQTTJdXEYLwWHKfr3H3DeaAIHqVnq6z79i0fCxeMglxFBNgdl_icz8i0sE4-Ty9zLXFC-71uF5bcmIzVcS0Ht5kez0cEC39LaWmujv0Xoyo48RDoaW7if2Oz0fLbtg1MvSr-SF8uP0PSitGouhfBUyRhsEovY6kzJCyscdIb1TgAD0tiN-d3dxh26vOMNgEcSWTx1IX0u9elvGA5OdIpwlCYH5E9wMNHSTGFAD7y_5WWlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری محلی جمعی از بانوان در متروی تهران، در مسیر رسیدن به مراسم تشییع پیکر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/447327" target="_blank">📅 06:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447326">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a088ef3c7.mp4?token=cNErqk5G4o2oOuiGtVkinFNHOns5rnJIof1wsh2EYFJ-77N-4gnHZ839gQwkm0n4yvRarZvDHN0B0H-71wqp9GfXZbpWYeAzKXDF63ymVp_d9j4L8Np5Jvgb_cOPwvAOGJPd3UHeymzNxiDTVsIKXc_urL0qonem4Q2LUvRbm1gg7TJoXSzRV8ZenINjnokKBfwVZqIGhOXBnSwjV-nJtABtn8NM5_-INiji9WDY8vocfs5ICEZ0m3ZfJsfHssn1yLCDrNGTPiyAyB99hitDT0UI9UZBNTMX8UQhSomG1SjDdrPqb1weeFqmx9naDghgKAs13soOhBDSKDzBBtj_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a088ef3c7.mp4?token=cNErqk5G4o2oOuiGtVkinFNHOns5rnJIof1wsh2EYFJ-77N-4gnHZ839gQwkm0n4yvRarZvDHN0B0H-71wqp9GfXZbpWYeAzKXDF63ymVp_d9j4L8Np5Jvgb_cOPwvAOGJPd3UHeymzNxiDTVsIKXc_urL0qonem4Q2LUvRbm1gg7TJoXSzRV8ZenINjnokKBfwVZqIGhOXBnSwjV-nJtABtn8NM5_-INiji9WDY8vocfs5ICEZ0m3ZfJsfHssn1yLCDrNGTPiyAyB99hitDT0UI9UZBNTMX8UQhSomG1SjDdrPqb1weeFqmx9naDghgKAs13soOhBDSKDzBBtj_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای متروی دروازه‌دولت در آستانه آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/447326" target="_blank">📅 06:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33401348d1.mp4?token=RNkHuTaw5J_x_BMTjN91bLJ2CXyyGTgTblCvQPh-sjQNDQ6iY8Fecgvx8OqjWM3ifks4V8MDhH4UmTOCjFLVl6rzzF9kGtopUzLC5l198OwcjAa_eygsrrpS43kyYfhDEw9mYEccMss7fqQBbMgY2nESuT02jO1pRkYqsgUokbNZ7tJi3yMl6USTmxQifa6UCGnOm8RMhP87-FKi64B8ToCD-o4_bCSZFmpbtBEpuMM4yXUWyrLuuv7DrJiTmK2OTB9ESxcfTFICQLVKqoa0Tr8x10cW8NBAQodR_wIjrhsjlXOzsxITDDA6kF4wOHJ3mVmJkd4e8m-EMdRIElTPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33401348d1.mp4?token=RNkHuTaw5J_x_BMTjN91bLJ2CXyyGTgTblCvQPh-sjQNDQ6iY8Fecgvx8OqjWM3ifks4V8MDhH4UmTOCjFLVl6rzzF9kGtopUzLC5l198OwcjAa_eygsrrpS43kyYfhDEw9mYEccMss7fqQBbMgY2nESuT02jO1pRkYqsgUokbNZ7tJi3yMl6USTmxQifa6UCGnOm8RMhP87-FKi64B8ToCD-o4_bCSZFmpbtBEpuMM4yXUWyrLuuv7DrJiTmK2OTB9ESxcfTFICQLVKqoa0Tr8x10cW8NBAQodR_wIjrhsjlXOzsxITDDA6kF4wOHJ3mVmJkd4e8m-EMdRIElTPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های سرخ انتقام در دستان مردم حاضر در چهارراه ولیعصر(عج) تهران  @Farsna</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/447325" target="_blank">📅 06:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447324">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01380449bd.mp4?token=JjGv2GhyTa_OQF13c6hv6_nUhPYjwyXcNFwwGgwbOpu-aSdN14MlRBDlABfV0b0Y3oWihtiOIWoYn64gRlSqz_M8_LyuKBT_3cl6fj4ahcC42FuOttk2byrbzIXeGdr3lJ1orbd_0vt0N23YhhrNlt4-LRvcuwey9u3D92t_sY0Lz32BaUxW0GhpeldUBpvX6VRebBuazko_kWXlDhnK78m9Th_6nte-MOVBXNrE-Ijj3vrJbRRDeqNUC_Gf24GMtDMjaE_HhiAsVp_8TSucY5ZHD7uz_FKqldKh7rfUB4oaNF8SItLv2mwC-40y2RUUAIH1RVB9OiHrOsHEwXbUXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01380449bd.mp4?token=JjGv2GhyTa_OQF13c6hv6_nUhPYjwyXcNFwwGgwbOpu-aSdN14MlRBDlABfV0b0Y3oWihtiOIWoYn64gRlSqz_M8_LyuKBT_3cl6fj4ahcC42FuOttk2byrbzIXeGdr3lJ1orbd_0vt0N23YhhrNlt4-LRvcuwey9u3D92t_sY0Lz32BaUxW0GhpeldUBpvX6VRebBuazko_kWXlDhnK78m9Th_6nte-MOVBXNrE-Ijj3vrJbRRDeqNUC_Gf24GMtDMjaE_HhiAsVp_8TSucY5ZHD7uz_FKqldKh7rfUB4oaNF8SItLv2mwC-40y2RUUAIH1RVB9OiHrOsHEwXbUXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای چهارراه ولیعصر تهران  @Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/447324" target="_blank">📅 06:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447323">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fed9d9e34.mp4?token=ScGMC3pwOYwe3zTPFkPrbnCMVpjKZNneAjVA2BJD0dA6bqxTL1JCRj_PoSHque03KihUV4mWUIjolAuRYPk2d2v0EaJTbT4Wm3OrGJd--pbwhrHTftZyNGn15eKD-fRzSzeCpJs3Tq6BkVND1RK67Myp0PxGirZ6P5yxahvlOfs54w_c9sE-vfZILRa-rZKGjiHpeAtQ_HKs77vvrfreCt2chKgPo5H4B7e1kibowP4jmLlOOTeGy5K_IHp7sQI6RMb6xzx2VIb4yMwsbRTJrTw-D3hq8OZfGoBVOV5-4h-TnyD9Ib7METp7jz20KXqTC8kbSbkSOa_fHrHQ2oxYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fed9d9e34.mp4?token=ScGMC3pwOYwe3zTPFkPrbnCMVpjKZNneAjVA2BJD0dA6bqxTL1JCRj_PoSHque03KihUV4mWUIjolAuRYPk2d2v0EaJTbT4Wm3OrGJd--pbwhrHTftZyNGn15eKD-fRzSzeCpJs3Tq6BkVND1RK67Myp0PxGirZ6P5yxahvlOfs54w_c9sE-vfZILRa-rZKGjiHpeAtQ_HKs77vvrfreCt2chKgPo5H4B7e1kibowP4jmLlOOTeGy5K_IHp7sQI6RMb6xzx2VIb4yMwsbRTJrTw-D3hq8OZfGoBVOV5-4h-TnyD9Ib7METp7jz20KXqTC8kbSbkSOa_fHrHQ2oxYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان انقلاب تهران؛ اندک اندک جمع مستان می‌رسد...  @Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/447323" target="_blank">📅 05:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d420a8f2a4.mp4?token=d28-BECWagsDatXOF90iQyNf5EDuk4ThqUqCQ2W36XbiZ2aHltl69XRYTdvS1QHeuf-ZroHOgr9qZvFykO2hn92ZxJ7HxI1iSMaBSE6F2QWpBZRLLwoTm_w5AfV8H_pqGMchiyAKJMGgtClwSDc9wjyBvniWBr_c-XhZq2xpmN2_W2ed7l4FD4fuRSn8eFMzz1R_fJNjqp1jqESHX3NtJ4SqMWAMY_q7zKQoJAPtm5J--mdtGwOU5NvFK8tGJkZvrrNCBZaAWhIBIk05335nVHE2B798D6atymRN_OpOO2_JkaaLVGopbyXicaDXqMPyMhoYLlSGmBYWX3OkE3eQOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d420a8f2a4.mp4?token=d28-BECWagsDatXOF90iQyNf5EDuk4ThqUqCQ2W36XbiZ2aHltl69XRYTdvS1QHeuf-ZroHOgr9qZvFykO2hn92ZxJ7HxI1iSMaBSE6F2QWpBZRLLwoTm_w5AfV8H_pqGMchiyAKJMGgtClwSDc9wjyBvniWBr_c-XhZq2xpmN2_W2ed7l4FD4fuRSn8eFMzz1R_fJNjqp1jqESHX3NtJ4SqMWAMY_q7zKQoJAPtm5J--mdtGwOU5NvFK8tGJkZvrrNCBZaAWhIBIk05335nVHE2B798D6atymRN_OpOO2_JkaaLVGopbyXicaDXqMPyMhoYLlSGmBYWX3OkE3eQOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سه‌راه تهرانپارس، و مردم منتظر برای آغاز تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/447322" target="_blank">📅 05:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447321">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57253c680e.mp4?token=Bk4d6yXACeb6c8NzYN0EP0XG_fCRhLEskAwOfGdFjTpCRho0TSISCSEdd7Mog1aA9PXpq6ui3MSbvx1lFcewx2m5Vl_tQ4yI0Y5J5fGD0OM7P_FTJDWS3G_vJGzUnrjvD76Wh6TPTpg8ct3YV5Bzr3d3DPCj8dgLC08S9gkXh2Yv76lExo7uGxUgTTTJ5eHU8WEc3DYixudQ1sodNB2WwxmOCdqn_fNY2_mQd4efxXqllZIGXuUJ0yQTSgFMRASzm-aCO5fBPVxmfeCMMGCmHA7EqwPHNvqGXuKeJvl8xNxZpEv31k2Df83sIIfPoupXCHqEzuYl5fotLrx7cF63Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57253c680e.mp4?token=Bk4d6yXACeb6c8NzYN0EP0XG_fCRhLEskAwOfGdFjTpCRho0TSISCSEdd7Mog1aA9PXpq6ui3MSbvx1lFcewx2m5Vl_tQ4yI0Y5J5fGD0OM7P_FTJDWS3G_vJGzUnrjvD76Wh6TPTpg8ct3YV5Bzr3d3DPCj8dgLC08S9gkXh2Yv76lExo7uGxUgTTTJ5eHU8WEc3DYixudQ1sodNB2WwxmOCdqn_fNY2_mQd4efxXqllZIGXuUJ0yQTSgFMRASzm-aCO5fBPVxmfeCMMGCmHA7EqwPHNvqGXuKeJvl8xNxZpEv31k2Df83sIIfPoupXCHqEzuYl5fotLrx7cF63Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی صادقیه و مردمی که همچنان در حال عزیمت به مراسم تشییع پدر امت هستند
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/447321" target="_blank">📅 05:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447320">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-text">📹
#فیلم
| مصطفی راغب قطعه «وداع» را برای رهبر شهید خواند
@rahbari_plus</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/447320" target="_blank">📅 05:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447319">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/359fef61fe.mp4?token=uwehuVab_laqbY2DGdFyTEiF9px_4turFK8_qhxnxv10WsgcqKvvmHaiUeoW0JWxiT2Vo7JsPxlPQNOANi8AXeQ9GpPSIjt3xxnRkfSYaBVjo18IdNzgS8YGYnz1eF7k625lyLl2pAXv1xu37_jlyYCYvpN3h-UQ_p4IqkhERqNntrki2tnQfgZYB0R5megVeLTqvnu7g_qAPklUkPD5NznAX-7KU5mWE-QMtvF81ozgvNk7IdKQ5nVDSKFqsx9jYNn5ujaZL4qfo0sfaI1aENs0GLzQjp90l8RJLpkL2s76OSUoO0bFEuo_wjSGfQR_uPBGzhwV6YwcEd1AeNYpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/359fef61fe.mp4?token=uwehuVab_laqbY2DGdFyTEiF9px_4turFK8_qhxnxv10WsgcqKvvmHaiUeoW0JWxiT2Vo7JsPxlPQNOANi8AXeQ9GpPSIjt3xxnRkfSYaBVjo18IdNzgS8YGYnz1eF7k625lyLl2pAXv1xu37_jlyYCYvpN3h-UQ_p4IqkhERqNntrki2tnQfgZYB0R5megVeLTqvnu7g_qAPklUkPD5NznAX-7KU5mWE-QMtvF81ozgvNk7IdKQ5nVDSKFqsx9jYNn5ujaZL4qfo0sfaI1aENs0GLzQjp90l8RJLpkL2s76OSUoO0bFEuo_wjSGfQR_uPBGzhwV6YwcEd1AeNYpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای چهارراه ولیعصر تهران
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/447319" target="_blank">📅 05:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447318">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d4b48290.mp4?token=tD6UyKJa0D5QAO27pOlNi9eiv_SSpNlbVmNWBnSr-SdqGKS0dUSWOeDalJwAVvPuWBQQYVPwCYYpbt8WmxKt0eEQNQvSPFDEPqxKVhrlTHL2qA3fbaKLNP-8pIwzOEJTokK0h4sHmcx4HBpMRw8v69V5AafkKSlE3oeCwUfdLGSitTaD07Gat5QAwlWezJjfpXRaQ7mTyjSrA_apD_tXJOt12UOYZ7elzT8a8ZR0vp3gG7-xTgKODMuqUipHa6TW5VMdYS2y_x-gKlyftOw_lhzL-u0sXf9MppxRTSgKa-TYMP9mHLlKXbplsjOtPf5Jzkc0fmfm45-Un3RrEGY8XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d4b48290.mp4?token=tD6UyKJa0D5QAO27pOlNi9eiv_SSpNlbVmNWBnSr-SdqGKS0dUSWOeDalJwAVvPuWBQQYVPwCYYpbt8WmxKt0eEQNQvSPFDEPqxKVhrlTHL2qA3fbaKLNP-8pIwzOEJTokK0h4sHmcx4HBpMRw8v69V5AafkKSlE3oeCwUfdLGSitTaD07Gat5QAwlWezJjfpXRaQ7mTyjSrA_apD_tXJOt12UOYZ7elzT8a8ZR0vp3gG7-xTgKODMuqUipHa6TW5VMdYS2y_x-gKlyftOw_lhzL-u0sXf9MppxRTSgKa-TYMP9mHLlKXbplsjOtPf5Jzkc0fmfm45-Un3RrEGY8XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران مهیای بدرقۀ آقای شهید ایران   @Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/447318" target="_blank">📅 05:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447317">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3340c6ef33.mp4?token=XJLeSExK23wZj_n7c4d35AQIsz0ROJ7IWz8jA32c8V_DNqidyJLS_JRWa1_kY2v2qJVdqufe2qWpyxIg0E_4n6dnyMDMckNh0W0gJsknqOexCnKBF2SHDSs4rdTMWqX-0nnov6Fcz0xr-MbiYLJdyJ6NTYSThDy05Bx7IdPkQBXwB_LY-4v-xLRcqXShcs6myUoj1igKmxiat1F0jWnSCAbQ1o7ZzTHkDAZ8qzj6V6ERmk19Av_RTjq3OtzuVpoFIGXYjxPSh3bguwqtkJTxuTfHmoD6Z05CZRYI9IFM0a9omTC47d0Di46BDXjJInnc5LkX00UP7uvZl0SlJxkKEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3340c6ef33.mp4?token=XJLeSExK23wZj_n7c4d35AQIsz0ROJ7IWz8jA32c8V_DNqidyJLS_JRWa1_kY2v2qJVdqufe2qWpyxIg0E_4n6dnyMDMckNh0W0gJsknqOexCnKBF2SHDSs4rdTMWqX-0nnov6Fcz0xr-MbiYLJdyJ6NTYSThDy05Bx7IdPkQBXwB_LY-4v-xLRcqXShcs6myUoj1igKmxiat1F0jWnSCAbQ1o7ZzTHkDAZ8qzj6V6ERmk19Av_RTjq3OtzuVpoFIGXYjxPSh3bguwqtkJTxuTfHmoD6Z05CZRYI9IFM0a9omTC47d0Di46BDXjJInnc5LkX00UP7uvZl0SlJxkKEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران مهیای بدرقۀ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/447317" target="_blank">📅 05:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447307">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOrpGpDsCCwk6mY3-0HOVeGDl1k2orve4Wqyr-5Io2lpYJN3K9OxVJ07oRUynvJDWgEAksjZL7QloreVDNUlmYJEsWzWy1UiiycVy1Mxk61amz2B-zfHae82D9XE06eguEZFBTBo1RSuMw5neBSnJ2bLAph_r8d7m7j7JTgFJlYGpOIN5qJQmDgaHTuU7JD_sc4CR95q7ZrPinOe8tpDnTB54Lob6P6raE1L5UONmKESuuT_weIogcira6NFfWIc76CArzPKV41uIcMl_hLzDzP7ON-sMQPoy5aPB6MLRH1S4UYLQjrw4lhnP8T8VYSDgSufNUCwQq00sgk1zRxVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDINY4LXibireQysU6wjE2c2vYPd5rAUKECIgA0viLviMN7oZubR2nrfzCq6G7Gb7_g_cWMp5mGzYIssVXuZ0C4YbwRSGWfaueqOtH4QBSku0r505T2c5uqUHJQXHuTB9NZYdFW6lcPGiJfL7X8VNntqvxCgG0FIqN6zoq7HuhGNM0I0ACzW1hFOjZqWB1GqqKmeVdz6Wod7KAz2BEBTpDWpeT0IJtsh0OvNteUJ1bGy9wPuIJzqv1E9famXbRv5H-jl-7AANnbDXODvrRJZI5_AzuhNRG6loW-Apx8uF2JWsqdEvSU-vD7iFKQN2eN8lQ55j5KBAznt-IdfPSBOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plZLe4B4ahlgticse0tVrY-BgfkGas5jVip2XvDy2JVcQO_TuBEoFv7eRP9bzQlvQ1pNo04bp_FgAbKcGfh0gPlbDtC8nZqMwep4OwaY_v_yCpyGS6HlBaAbuGqt89YPoGhDzjHhZQvY3m-U-I2f4rCAB6jpkD9_n-eF_b446apf8BOK0NQedn5TB5jY83bODKGcL27V1B7knrFrVKW4CY2VsCdLkdcHGRpU4ZMLvne0SU3NFaj2uaUw5RLyCdw5PsC8HfDo7xPEirTAABFehgAjUI3semuFb7Hfmxm3bLfs663ERpKsnXfNreD3lym2DMn72W4qXatV5LjkL1fE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6DuSHgC24TI7uFWM2LIV8XDDACbdYnBfePOgrPkEvH5Vyi9GhsdtQHFAkTM7rBxCNtkp5KC5tov5xIL35An7-auyvvrvMTA_fST6q9SE-L4d9YDg4VHc4bSkv-21lWcFoKxBVCvrOpykimsyk7AzsB0kwVeIeqR7M5hYrTsFW-FqCfa0C8NLONvOImK77QxlEN32t8Ra7knKkmYEB4f_YoTgMqwxSqGA-vmk4V3KxEZjG_d-1UWYELXfZUNaSa5wh_CWRpE2nKFfbq3b33xbALvPAiGvSrhYl5tmpnjzWK4bOev3-be4mYm_whtIoVwcvP4MUiP5JTfCcwIoJel2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2OzHxZLFNEbGXiqxYQTMwlMuLOe5t82bKgmapErWIgHKP2ynVtIZUczRSgamy7v5oxTe-jH4xE2n780WgZbP83X4oKW0CICoUqi3bePnxsjniobix4q4zB76l71nNHbRk-qRXKD5F1Zr4-EBIkJoFLUnYRZnwk4XbnThuLhlG4zw4paPYeYN-AWU0mluM7vsOS3b7MGefajLheFJx5DhDlLOt5jPaeig0Y5l3hObUWxSh5VRcryWxXwqInD2iEUMCle3mwOmvmg3AIQJHfMJtR4qiFqAniyjcelthbgvgRdM6EeWgOcEOlRUSvH4rKk_LU7qElfYHVATU49HwCaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-FCK1sguJMTjEjLoG4oe39_KeX0el_85H44_x3URoEOMBEusUo6j-echcoOfQF--tNWBSkIIRItViL0_SurRFCLQHo7c4QQnn3cXMEUwfxJzQWUeWotaTPxF1_AS4mvrcSlkRctGu5hS3tbh-2owraFXC_C2XqQ-yPKHzR519OTSERpNZqRPTGzADxnE4ZqjWpaXhyW7fGj4-4U2Os-845aoNRrg1EFKXH8tF_QON9MvLCFqe1BU59LwscUN6Ier9zdVYLAtx1I5tIFpXWdR7AynGKmPyRPN8xKshcALY2-VA5JUmYJt5SlpAv1F6HElWS2VbcrfYDG81T2VSvdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2YJ7PzfRdPK9HbsqgD-jpW1xVLQnFBLO0yAKSIGNTmUi3HlBsBCOBG4NqWtFy7y3mb-6tYU6Ab0Rwx5XQX3fJJ9kR4P28saB-x2JOx0VE5Bdir4mR9iyrHyq7R0ZQWO5dfXx8DRmEcL_JoHCfFwDpDHiuZCvmyx7cntgDDvKJnEnKk8ZAmmpShrnLcy2OqtVG4DjG5kNs-LIAyZqN6CMwyJiA8CSeuYnexrmwoGaitGkIrao0Ctfa-kmam-yq2jodaR5_WB3CHG14GfKkdaaCftsu5qskznHOUXoeLJiqaYYOo4242rYzJxUp-tIs9NbsCnX8fFAIKauoouNgsd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPLLpBqKFaYOPey6Hw0reXBio12p4YBVbR9qrrDxRE0n-tImBxtsXJMDxBZn_h15UzHRfvR-eNrO_kDJN-BmMB6NL1aI7969BLoZFqh9jRcBHGmDnldVmQFid9Tn7Pbz1ffyWzfMvE88fCyAmkoThraPdS2xovrTvPJHsRLYwGsMR4LbpO4nd57AgGcvJ9wOIFs7m1SDhVOIX9ZF_uibsV9j8m5Y5OM89rCrs6y04uHxpMkxz6dD7sy-0vawraYpOt5huPze7JCh--5CbjoIOpSlhm3b0T3tW9fv53RhbKafalNT6do6iVUqmUkrqaDkr-QAj9qEuQCEZ-01aq7GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9lrg7D0RxL_r_TxW4lTe7qlXURUSSxxhVjf14vS-KR4SpT6jgYxDtTRKwjMMSqsctyPnzkpCqFSg-j7eeQVUY8t60wdT7iNnvAvIVp6jwY1GqFstXWNDWg_knCurTXnJbDWu4Bf7QaL2mg_20p0NI2pIJWLTNlryNnqmcUPxuLAntdG6mIp6ayQMVqArLCqSN_6i8zJPBTvSqQhN8o14QuNNFH8v9jVTOn7ir_AfXWsAFNZKVRfTArT9W7DqC3mLhB7qnYBVXnTNltUaYMGQc3FXNcwC0pnD5a4koBrCGHvzNT6E7tNflFgE5BLpTVmUxfVe-FBRL7mU1b_I8_B3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0XGpx24jiDdd0mOwNtk5hy3uAYMzilhX9XF8Mo-Uq_pdcSAxhR4rz8R19-FXM2oBDPyL_oOykyo37gEy4c95Fdkro9LNf_j_33K0ubdbdcl0LkW3DtG3xjIpEqftyDoMHcZbBwAtI7iZt4UZEE-HD63AgkroWKp0APAK5E5A_NaYRT2pLD4jz7wSS9D5frR-l_1iy_zWFgqUz0vmoT2difQycQm85Mv97Grc8lZkyBZYEt2pClG4i4qwNOHjfnJU-y7YCQrF0FzQL3EXXD4EwlDuJO6SIwiUnkQLJm4xGwBYYYYm44tea26rcull6djd5fXtNfTEHvXYW43i0Ic6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آماده‌سازی مسیر تشییع رهبر شهید انقلاب در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/447307" target="_blank">📅 05:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447306">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14a6b8059.mp4?token=iygmKg5vjEMl4tOBfKoTqbVXUqePWu8rK2d11tSvpbAvLVMqYoIgalDVvim7uOF8-Goi-fWZkGmFYVNAsAucddTH6REV5rpMlvk3JBZUvV9k7y6vFpGViQcLdO2dvO8KryerRVQkeQN2cfWlWfK5CdqcaBKOyr5CdIoytd5i09A-MFgtJB2exdOEktfteIPVm6QYn5uz-xqDFkVXnhmJ5f1PW1E5ABdKq6SaUh0CL6inYHfEPVKWVjy3Ii0osIpwscuAd4sa30YQl-GengtWfi4LNjXL-eynapXbNbAu-lIHqH7EFfVjckxxloChhhYiZhGTKu38p9v71Pk8gD2EUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14a6b8059.mp4?token=iygmKg5vjEMl4tOBfKoTqbVXUqePWu8rK2d11tSvpbAvLVMqYoIgalDVvim7uOF8-Goi-fWZkGmFYVNAsAucddTH6REV5rpMlvk3JBZUvV9k7y6vFpGViQcLdO2dvO8KryerRVQkeQN2cfWlWfK5CdqcaBKOyr5CdIoytd5i09A-MFgtJB2exdOEktfteIPVm6QYn5uz-xqDFkVXnhmJ5f1PW1E5ABdKq6SaUh0CL6inYHfEPVKWVjy3Ii0osIpwscuAd4sa30YQl-GengtWfi4LNjXL-eynapXbNbAu-lIHqH7EFfVjckxxloChhhYiZhGTKu38p9v71Pk8gD2EUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی تهران، و مردمی که درحال عزیمت به مسیرهای تشییع رهبر شهید انقلاب هستند  @Farsna</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/447306" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2415cf5901.mp4?token=S7uov_ImEDguszyD7Fl5MwkFII1ZBbuQAUlEp1ILUXBI2qIARfZkDgQD9DV7hO0_msuaaE7BnFOySHRbhtV87rmYFE4qaA1dJNiA_5hAY3TeetBcYkyRI3o5tlmboQPISwepLZSnxFRPE9PHyZhbUfHKzZzStMUocS0KkR1FTPcafJpkRGFdhOSgxq7RJShT3Gmt9IBJwR4G1uHQ-XZFZrTYkJDr1zZofmIVkGhHPSKa408YlpPNHDb2komRAoOlXR9HROubYm-KV8vApAE6jFdCjmUSqGmOkxTJS8cDl78HJ79ECyArhqsqGkZsXUxTSVhdWEKMXhiDNxF4KvuW1WqX678dblRHh1WY_mW-wI6mswdkytNh5rw68j9PT5Y7725s6yJOFSjNzp0YXLCfkvWYjNL61MuFaPlNdPJZ0RY_0zh_QCnEOjMlV2vmuNiK2eIW6LHOlYrGfeoLeoCAidaNVfJ0tANPNXDpmTEcH1DUWgSMDBhXOIRNhpUEccMfEfQ6YfwK3YEOaPvKGF2UNcH5QauMrGfUer57_GEU1N8hPMMoA4C0N643KvewN3ocYOVf_yiM1DYHC8wVx7BZQ4QyXUjVS26JqcHWLtPv3jjh8kkjC77gCKbnA_XSc9hsu7gT62fUYR9STlOS2Z0-52nC9I5oKWdrzzcDiTo7fg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2415cf5901.mp4?token=S7uov_ImEDguszyD7Fl5MwkFII1ZBbuQAUlEp1ILUXBI2qIARfZkDgQD9DV7hO0_msuaaE7BnFOySHRbhtV87rmYFE4qaA1dJNiA_5hAY3TeetBcYkyRI3o5tlmboQPISwepLZSnxFRPE9PHyZhbUfHKzZzStMUocS0KkR1FTPcafJpkRGFdhOSgxq7RJShT3Gmt9IBJwR4G1uHQ-XZFZrTYkJDr1zZofmIVkGhHPSKa408YlpPNHDb2komRAoOlXR9HROubYm-KV8vApAE6jFdCjmUSqGmOkxTJS8cDl78HJ79ECyArhqsqGkZsXUxTSVhdWEKMXhiDNxF4KvuW1WqX678dblRHh1WY_mW-wI6mswdkytNh5rw68j9PT5Y7725s6yJOFSjNzp0YXLCfkvWYjNL61MuFaPlNdPJZ0RY_0zh_QCnEOjMlV2vmuNiK2eIW6LHOlYrGfeoLeoCAidaNVfJ0tANPNXDpmTEcH1DUWgSMDBhXOIRNhpUEccMfEfQ6YfwK3YEOaPvKGF2UNcH5QauMrGfUer57_GEU1N8hPMMoA4C0N643KvewN3ocYOVf_yiM1DYHC8wVx7BZQ4QyXUjVS26JqcHWLtPv3jjh8kkjC77gCKbnA_XSc9hsu7gT62fUYR9STlOS2Z0-52nC9I5oKWdrzzcDiTo7fg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع آقای شهید ایران «خبر اول» رسانه‌های جهان شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/447305" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447303">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a903d21c.mp4?token=HFmurLbnhSZsmfHFefy8kWs3VuOYxpdSiUc7uq2Xhd86eHcVwA6QVvzgIzfE-Dr9De60NrFywLyjNndJmLU0lj4PEc3ncSIU1PAm8AL95d1uwrWekZq83v8AyLi4e5YNK6k3iBr1-bs1lLFUEvvg7sp7eSoRFKRoaahKvT8PTHBc6FSgXtIfXePSQeXyFCVnOQrsQ8Lk95AGtk40HEOR-F3yj0dA4mHnRKgE5xzqXAH8xl0tr8NwEqNq9Ki8i1SepYEMJtqTSnosNqPWQgKpgAgwrjAk3uEEmllWTuKoXG3jKl3GtY2f_XeoYtTwVH9bgayutlhOE2PkiUYKmLw_CqSyBZhlMfQH5dYEDlArfLjRHl4KCSDGDQ10LY-FvHutW8z0hxlLql7SgGvGfQ80Fs1m5TPBFBWiZ9QoczHFP1PFggBiIGn5Cp495XeOYl7Tf8Epr85Vbud_9jTXRC-VD_TQk1QQtJssO-1Qynbmh1BEWtjaFnR_FJzRxkmou5v-piJ_y1BaS6VKMW6s6x704XXsGjaf-6LU4GCeyaOWRMPWHNjFMeF1LiN5bjrI7T6paHbMaSGQAvQ1TwTGOcT3BO01Dy8ZbPEklznjalZswX_KmVUDWQeP1K4X_HmebetaqQrp6dlTiZ0XyiY48GCt61c63Ss63sALi5wy-GOl5PM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a903d21c.mp4?token=HFmurLbnhSZsmfHFefy8kWs3VuOYxpdSiUc7uq2Xhd86eHcVwA6QVvzgIzfE-Dr9De60NrFywLyjNndJmLU0lj4PEc3ncSIU1PAm8AL95d1uwrWekZq83v8AyLi4e5YNK6k3iBr1-bs1lLFUEvvg7sp7eSoRFKRoaahKvT8PTHBc6FSgXtIfXePSQeXyFCVnOQrsQ8Lk95AGtk40HEOR-F3yj0dA4mHnRKgE5xzqXAH8xl0tr8NwEqNq9Ki8i1SepYEMJtqTSnosNqPWQgKpgAgwrjAk3uEEmllWTuKoXG3jKl3GtY2f_XeoYtTwVH9bgayutlhOE2PkiUYKmLw_CqSyBZhlMfQH5dYEDlArfLjRHl4KCSDGDQ10LY-FvHutW8z0hxlLql7SgGvGfQ80Fs1m5TPBFBWiZ9QoczHFP1PFggBiIGn5Cp495XeOYl7Tf8Epr85Vbud_9jTXRC-VD_TQk1QQtJssO-1Qynbmh1BEWtjaFnR_FJzRxkmou5v-piJ_y1BaS6VKMW6s6x704XXsGjaf-6LU4GCeyaOWRMPWHNjFMeF1LiN5bjrI7T6paHbMaSGQAvQ1TwTGOcT3BO01Dy8ZbPEklznjalZswX_KmVUDWQeP1K4X_HmebetaqQrp6dlTiZ0XyiY48GCt61c63Ss63sALi5wy-GOl5PM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی تهران، و مردمی که درحال عزیمت به مسیرهای تشییع رهبر شهید انقلاب هستند
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/447303" target="_blank">📅 04:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447302">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d332d41043.mp4?token=EVDduzgPyiaFQdlYF63sseGdrPt8ITKble6gHT_LZ83gfsePDamPQPEudgOEA55w21yyL7ftK8ZK1k1Y6vzvpN5R-vcV4stiZPNd5rwki8-CR0wscf3SLSspAov0Me2XA91PHYocEtHkr_LLA4SDpD-AuSqMfE4YSUcgHYy7H7ufQyPRNYXkfEz4w7fv68XQ5JuMUIebdLpnRNbkA-HihxbTL6rBrHPdr5iG5b7ZWbCD5hhKAm_Ltm4CHTd_Ri5z7VmKrnSPThcYiigHuOTgXERLBlXy01fiYe-RSCDNs71NrD3UWUTLCvPzt-JfCC4_X692CrdyMar58C8Xl016Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d332d41043.mp4?token=EVDduzgPyiaFQdlYF63sseGdrPt8ITKble6gHT_LZ83gfsePDamPQPEudgOEA55w21yyL7ftK8ZK1k1Y6vzvpN5R-vcV4stiZPNd5rwki8-CR0wscf3SLSspAov0Me2XA91PHYocEtHkr_LLA4SDpD-AuSqMfE4YSUcgHYy7H7ufQyPRNYXkfEz4w7fv68XQ5JuMUIebdLpnRNbkA-HihxbTL6rBrHPdr5iG5b7ZWbCD5hhKAm_Ltm4CHTd_Ri5z7VmKrnSPThcYiigHuOTgXERLBlXy01fiYe-RSCDNs71NrD3UWUTLCvPzt-JfCC4_X692CrdyMar58C8Xl016Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معجزۀ خون در روزهای بعد از شهادت آقا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/447302" target="_blank">📅 04:34 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
