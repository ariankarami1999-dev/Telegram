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
<img src="https://cdn4.telesco.pe/file/BmCTUcrabdTrpcjKLd0_GrR-Y2ZaWa7NbIXqmXOKND7PTUYW5VVZj_w2fOkGmzFf3v9x78k4QFLdk6xQUf_jUcG0xPqqrH3eHFGhnQCvlR3L2k21QxCQ6rca5-9xBrx-EGMa-GE6uIirPwBGu39ieFmn0PLupRSM7pbxNU3AMlcaJYjF4jfUUzni-lukD5w4HRS0gl-LzRGPMJaJzg1QrknzCgjLkI2oERLxGQphOXp8rYOTbnaiPNKqrhfCdNTdByxP9SvFzj0SGKcj4dOxRWJ4zVlq8L5IkCjSERi0NA25avgrrnqyBA-jNH9c5xvsAXR8lfIIdQfF-wc3tUIvdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 04:37:41</div>
<hr>

<div class="tg-post" id="msg-448576">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
صابرین‌نیوز: موشک‌های ایرانی، پایگاه الأزرق در شرق اردن را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/farsna/448576" target="_blank">📅 04:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448575">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/934748e258.mp4?token=TUmwADwwq5X8m-yS-jsJbml7-NrkqaQ4GP9AywiQjzYScpE8a-bQ6z18LEDtEjZ7kVXMV9Li9XskN_HE4jgzXTy2G-wso8-Xgk9br-wX6Wkf1Gkt3f3tBujrWIgAFtGqFDTqINuHIvGF-62whtKMTVdziOvY2T41hj1KPBUdQhEsUcOqOmFGbFV-_4kpbxLuVT-rMSeFJ3px633LLSF-EPT39MS4t8868GI5x0LJ-e8X9dLZ3OMLOAy83qnPA2jWpfiB7JqUevGfllRDwbDhTNTM-K-pptCy9hizluoGv0cSqFbWL11sweQga_F2yjuZkQs0pWhuzIJdOiNgId9Jswzhp_aZMI5CIJ9LRcjOzramKSwkHc-eYmW_hMvNO1jZX7TGPzgW9-cF4Rtd9vN85YtnXtoVipwsS5JetbP20BuS0OObJg4Hpg9ZlROSgW1leUvkOV9JjAltRpqC6fRpPgQT_aRG9y3FEmSOAaVNtRIc5EwNGPkWkLSqnRcw0Iyjpi5_gXm40Td1vwnp7O7QbrWM5f7fr2Q32aoeq9AHDh7u7v0O_pMt2-VA4BUYx_s9Slgc5d4z_u8m0bSi5H88G3VLyXwk9JUjlohfkrJz82jXHMbZ2_xQhvxzz4gsF6Gq57lOKemL61cFM87fWDIkc_tktQWXf974ekV-mbhjcyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/934748e258.mp4?token=TUmwADwwq5X8m-yS-jsJbml7-NrkqaQ4GP9AywiQjzYScpE8a-bQ6z18LEDtEjZ7kVXMV9Li9XskN_HE4jgzXTy2G-wso8-Xgk9br-wX6Wkf1Gkt3f3tBujrWIgAFtGqFDTqINuHIvGF-62whtKMTVdziOvY2T41hj1KPBUdQhEsUcOqOmFGbFV-_4kpbxLuVT-rMSeFJ3px633LLSF-EPT39MS4t8868GI5x0LJ-e8X9dLZ3OMLOAy83qnPA2jWpfiB7JqUevGfllRDwbDhTNTM-K-pptCy9hizluoGv0cSqFbWL11sweQga_F2yjuZkQs0pWhuzIJdOiNgId9Jswzhp_aZMI5CIJ9LRcjOzramKSwkHc-eYmW_hMvNO1jZX7TGPzgW9-cF4Rtd9vN85YtnXtoVipwsS5JetbP20BuS0OObJg4Hpg9ZlROSgW1leUvkOV9JjAltRpqC6fRpPgQT_aRG9y3FEmSOAaVNtRIc5EwNGPkWkLSqnRcw0Iyjpi5_gXm40Td1vwnp7O7QbrWM5f7fr2Q32aoeq9AHDh7u7v0O_pMt2-VA4BUYx_s9Slgc5d4z_u8m0bSi5H88G3VLyXwk9JUjlohfkrJz82jXHMbZ2_xQhvxzz4gsF6Gq57lOKemL61cFM87fWDIkc_tktQWXf974ekV-mbhjcyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب در حرم حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/farsna/448575" target="_blank">📅 04:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448574">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
وقوع انفجارهای مهیب در کویت
🔹
صابرین‌نیوز: علاوه بر بحرین و قطر، پایگاه‌های نظامیان تروریست آمریکایی در کویت نیز هدف حملات هوایی ایران قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/farsna/448574" target="_blank">📅 04:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448573">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2d1ebda.mp4?token=p9u6gT2bXLrlKT2g9wGE-6sSm1KmB488mTPpgibaKukfiUfOrgWu_3Id5rb3Klx-0EBdw2vazXi2_QlmiCs-dK4k1wmZ7fd7jFqTRRzyonz1N8v6iSj6HV47cFs7ZE08UBpzTUeCLjAjs1qb7JRuu7Li0jwYOAAmaIP31YTVN-MXVssYND0469rnS8uba_WkWEYw7zLy7D8x9v4GnUJkMvtI6cS6VEyGnyMeYTTx_fgmMfGFyIEeXE9UhfKO0TitOrGq3m6L0pCgFfoDOHJUWdsEoztJjWjPszK8_Ic7IA51sVJhJBTKMqgWTO3C14Nitiy3TDF_0JEDoj6leAKxDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2d1ebda.mp4?token=p9u6gT2bXLrlKT2g9wGE-6sSm1KmB488mTPpgibaKukfiUfOrgWu_3Id5rb3Klx-0EBdw2vazXi2_QlmiCs-dK4k1wmZ7fd7jFqTRRzyonz1N8v6iSj6HV47cFs7ZE08UBpzTUeCLjAjs1qb7JRuu7Li0jwYOAAmaIP31YTVN-MXVssYND0469rnS8uba_WkWEYw7zLy7D8x9v4GnUJkMvtI6cS6VEyGnyMeYTTx_fgmMfGFyIEeXE9UhfKO0TitOrGq3m6L0pCgFfoDOHJUWdsEoztJjWjPszK8_Ic7IA51sVJhJBTKMqgWTO3C14Nitiy3TDF_0JEDoj6leAKxDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
فعال‌شدن آژیرهای هشدار در بحرین و قطر
🔹
منابع محلی از به‌صدا درآمدن آژیرهای حملۀ هوایی در بحرین و قطر، بعد از شلیک موشک‌های بالستیک از ایران خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/farsna/448573" target="_blank">📅 04:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448572">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23460b6fc2.mp4?token=XhGI91ZQIUGhgctZZUkYq1lE5LYBYoxn1tp2jJ93emo243Qd7G5WnTKVGGYKqSJ1pG5bopFmxM9fO54mb9-4PqzWJfACFeBV7Jo38HOXBJovF_cbbN1sQBlXN5lF0R6vnWSoswMDNDQJlQC0MyS5rlQdW-SomdYBEtuaC_ZTFl7kIdKA0OFE8jGbzxmO9crt7S5R3le_JCBdD441dNqIFeCYIxr4m_ugPC7Eb134__cDnVTuJ3Q2zD_8av8Wy7gD4zUBhFjJ7OR3AFxjX6sIfIWTFdYhV8xOZjZuG6w1QT-42ruKcTLuGXA04fRTtm8SG5VlZjs0LfbeedDZOdDn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23460b6fc2.mp4?token=XhGI91ZQIUGhgctZZUkYq1lE5LYBYoxn1tp2jJ93emo243Qd7G5WnTKVGGYKqSJ1pG5bopFmxM9fO54mb9-4PqzWJfACFeBV7Jo38HOXBJovF_cbbN1sQBlXN5lF0R6vnWSoswMDNDQJlQC0MyS5rlQdW-SomdYBEtuaC_ZTFl7kIdKA0OFE8jGbzxmO9crt7S5R3le_JCBdD441dNqIFeCYIxr4m_ugPC7Eb134__cDnVTuJ3Q2zD_8av8Wy7gD4zUBhFjJ7OR3AFxjX6sIfIWTFdYhV8xOZjZuG6w1QT-42ruKcTLuGXA04fRTtm8SG5VlZjs0LfbeedDZOdDn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی باشکوه از وداع با پیکر امام شهید در حرم حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/448572" target="_blank">📅 04:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448571">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
وقوع انفجارهای مهیب در کویت
🔹
صابرین‌نیوز: علاوه بر بحرین و قطر، پایگاه‌های نظامیان تروریست آمریکایی در کویت نیز هدف حملات هوایی ایران قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/448571" target="_blank">📅 04:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448570">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f456a0004.mp4?token=Zba3Zuz9_Y5UkILkKT3lwu1jcS3vUWfmEkv1zTmMmKy0RcpuYGzwr2DFjDc4b1uk4ErcKpIX0_ArDrhx1KXbg4z3PvfXsq1BBD_AaWAiE5OSCztfSyCP6D3UaJ34Gqi55wPDbs69oMgxy6J_m04Dd5o9qBdQQDuQ7BfHpMw8iQD4wk31NI4h8s3Qw5vy88UZb_TXc4gWQZF3Yasbb419xkmMjYuniG_YXHP6LLKqY9R5YOOZUU-xT971JuCK2kd605ZI2gpFS90vf0ipG3BwQSlMeQDPYsmoedol8NlEcudwBg8eAodKCvwf6N6MgAGLXatP-X-l3oae6j14d6CXMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f456a0004.mp4?token=Zba3Zuz9_Y5UkILkKT3lwu1jcS3vUWfmEkv1zTmMmKy0RcpuYGzwr2DFjDc4b1uk4ErcKpIX0_ArDrhx1KXbg4z3PvfXsq1BBD_AaWAiE5OSCztfSyCP6D3UaJ34Gqi55wPDbs69oMgxy6J_m04Dd5o9qBdQQDuQ7BfHpMw8iQD4wk31NI4h8s3Qw5vy88UZb_TXc4gWQZF3Yasbb419xkmMjYuniG_YXHP6LLKqY9R5YOOZUU-xT971JuCK2kd605ZI2gpFS90vf0ipG3BwQSlMeQDPYsmoedol8NlEcudwBg8eAodKCvwf6N6MgAGLXatP-X-l3oae6j14d6CXMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش سید احمد الصافی، تولیت آستان حضرت عباس برای رسیدن به نزدیکی پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/448570" target="_blank">📅 04:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448569">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJAc9-jKwb3Qq32Lr5t-IAifkPBcPSQONl6EOJvNpnQ57KaHeTPf0957bUmhxfaCST4_VGJNcgxRB_xjXLSWw0HP9DiIBWDrwlfFWQ43qEkqRVDAglF0W8ByuueoBLdQ7acb-L0wgWgihKpQrx5E8-X2u3NTSCyAfn_m38zSNTnzhNMyr-7ypd7jttg-CL9XpcGlC4ZM6Iv3-uWaBRV1gDqSwi4F38KRp15ozZoQhvq7QFtkVZ3MInu0MQA5taS4xNX4qLy_9KQ6YR5mPXxBvlnDeMYQ8r2bRxWx24DXHFLaJpksD580O0-Pazv2NMsRSwinCRyYWjpbztafqlv9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصاویری از بدرقۀ رهبر شهید انقلاب در حرم مطهر امام حسین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/448569" target="_blank">📅 04:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448568">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693ba173db.mp4?token=OpRLhq2DcWLgI_Iu7hejCqyfXDx7Ng3DFlvgCN5yFppQFlDONMM_Me_zGn5hQU7zxpchOVvbDWlGLvqnagul2r-uNJYpvtlmkCXT7vg1VCQpfHfXtJHUJblMDAY4gdR374H2TP3pJrdjyU-Lr5ikZU7ZmfIrNCgQlojRK1LVCJZA3jJdho1weNDobVb4wEnUBW6SugL4c4QzoLxLmsqFoPOCO-GgPkm_afbh-iqoZUkBbW2bm0Eq7Y-LQQ5Bn45xktj_2gE4vBGHfYE-BFWA3WJqYUZtQCmlYfuFa-UV5wY8RD8AK7TNiv0XseK6usMi0ZiF9AIzj57nvyCQnqkjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693ba173db.mp4?token=OpRLhq2DcWLgI_Iu7hejCqyfXDx7Ng3DFlvgCN5yFppQFlDONMM_Me_zGn5hQU7zxpchOVvbDWlGLvqnagul2r-uNJYpvtlmkCXT7vg1VCQpfHfXtJHUJblMDAY4gdR374H2TP3pJrdjyU-Lr5ikZU7ZmfIrNCgQlojRK1LVCJZA3jJdho1weNDobVb4wEnUBW6SugL4c4QzoLxLmsqFoPOCO-GgPkm_afbh-iqoZUkBbW2bm0Eq7Y-LQQ5Bn45xktj_2gE4vBGHfYE-BFWA3WJqYUZtQCmlYfuFa-UV5wY8RD8AK7TNiv0XseK6usMi0ZiF9AIzj57nvyCQnqkjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال عزاداران عراقی در حرم حضرت عباس(ع) از پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/448568" target="_blank">📅 04:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448567">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
فعال‌شدن آژیرهای هشدار در بحرین و قطر
🔹
منابع محلی از به‌صدا درآمدن آژیرهای حملۀ هوایی در بحرین و قطر، بعد از شلیک موشک‌های بالستیک از ایران خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/448567" target="_blank">📅 04:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9658ab1bf6.mp4?token=uRyCJAmORi_rLJMQv-X65exMm4-yNnhqi0WqWfaxvUGlRGms7IKhdheccFPnkNhZjg5qYHs2b4S-qMJjYe2zg0fo5nMG17aOxV_t_dc_yWrdzsJterXBl-OMdrUOMllNnSebgxkC1JlPuJoNRL8GOqvEquySM4a2TFaPdYqHCBrXrLcyPeJIeUp4KVAOEaGiB9oS3xU70-VY0OqYG7CRMGL3GPvTUegWFbvPj4LJ2l-uUF0ptKSf2tjZhVqOd4VQ5S_LXv662EH4PP_EM9S2sioycSvmmybqFnxWIbhbfimMcU-jhkAmkkksJqCKpKpLegp20w2zrlSU-EAMcAeAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9658ab1bf6.mp4?token=uRyCJAmORi_rLJMQv-X65exMm4-yNnhqi0WqWfaxvUGlRGms7IKhdheccFPnkNhZjg5qYHs2b4S-qMJjYe2zg0fo5nMG17aOxV_t_dc_yWrdzsJterXBl-OMdrUOMllNnSebgxkC1JlPuJoNRL8GOqvEquySM4a2TFaPdYqHCBrXrLcyPeJIeUp4KVAOEaGiB9oS3xU70-VY0OqYG7CRMGL3GPvTUegWFbvPj4LJ2l-uUF0ptKSf2tjZhVqOd4VQ5S_LXv662EH4PP_EM9S2sioycSvmmybqFnxWIbhbfimMcU-jhkAmkkksJqCKpKpLegp20w2zrlSU-EAMcAeAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب وارد حرم حضرت عباس(ع) شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/448566" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
وزارت کشور قطر با اعلام سطح بالای تهدیدات امنیتی، اعلام کرد تمامی شهروندان و ساکنان در منازل و نقاط امن بمانند.  @Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/448565" target="_blank">📅 04:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
برخی منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/448564" target="_blank">📅 04:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
برخی منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/448563" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448562">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eb617d67.mp4?token=g1JRMGGQy6KXVZ_vVEdPD88vSdfJ9rlJ8gKm7bSPYA8oAniNdNoGE2RcVMdHJQ-Z0Mk8Sfsc__IWM0mbLzA63RAqZRccHMEI2gaqewdsITzK5gEu9ipqB8nr8Tr9cNbZkM_J7p8fokdCANKC5FzGJIDDw5b8xCxLHKsydN_g5IHccBFl1ODUBscvoCca7AgfjjcsAOPvwXibEgH8Hs17Xi01-cmTYVtBqL88HEh9_8WvLRGM7PicFJjEdjV8XsthW9vtY1myUswgyXpsDOhDa-ehyG2eErrvDiBZS9YHPTsMI_cIQCP6jgRfpehQpKlF_Z9_rPoMWbG8l-gnVfcPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eb617d67.mp4?token=g1JRMGGQy6KXVZ_vVEdPD88vSdfJ9rlJ8gKm7bSPYA8oAniNdNoGE2RcVMdHJQ-Z0Mk8Sfsc__IWM0mbLzA63RAqZRccHMEI2gaqewdsITzK5gEu9ipqB8nr8Tr9cNbZkM_J7p8fokdCANKC5FzGJIDDw5b8xCxLHKsydN_g5IHccBFl1ODUBscvoCca7AgfjjcsAOPvwXibEgH8Hs17Xi01-cmTYVtBqL88HEh9_8WvLRGM7PicFJjEdjV8XsthW9vtY1myUswgyXpsDOhDa-ehyG2eErrvDiBZS9YHPTsMI_cIQCP6jgRfpehQpKlF_Z9_rPoMWbG8l-gnVfcPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
◾️
به‌دلیل ازدحام شدید جمعیت در بین‌الحرمین، پیکر رهبر شهید انقلاب به حرم امام حسین(ع) بازگشت.
◾️
تشییع پیکر رهبر شهید به سوی حرم حضرت عباس(ع) پس از اقامۀ نماز صبح ادامه خواهد یافت.  @Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/448562" target="_blank">📅 03:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGsZSfn12MNfwnZn3nWgsDAWylT70HopixDcBfiNZPAW0j_7ubAcIS6GGPzJWkUMabvuXImEHMzgkqHZtQnCxy2ZcC3FRXu2EI3JL-CPExa0w5OI0U8KhL-kvHheCQ7hnifK_GCTAdZHhFcyKWN8WWqLAPkXyjE0Xiw7JxUzG5ArsUZIs_tMksjV2vR7vi9i1jiJUe3jorPjU316A7jRCD08dA_aSzJeEorDEAPv-hC3wFNL8d5cP0yXl0DM2vyuYnNIloMLpi9-IcriwSpSi4NtO1VS-aEngwjfP4ZI-BE4EBkumXE6dqaoxmU9I-6U1gd1ptWhXxcsKvQLblSv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله آمریکا به دو پل خط آهن در ایران
یک مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفت که نیروی هوایی این کشور، دو پل راه‌آهن در ایران را بمباران کرد که اولین حملات به زیرساخت‌های غیرنظامی این کشور از زمان برقراری آتش‌بس است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/448561" target="_blank">📅 03:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب از باب الشهدای حرم امام حسین(ع)،‌ رهسپار حرم عباس(ع) شد  @Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/448560" target="_blank">📅 03:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7id4PABJF_W_DFeF6q_ei_2NhPMyXoMNLHGq0KNC32m13lRx6mvlSrAxyG1KaxMsfhygZeMoC9Ga_KA1rQIlDa-j85yO3BMUU0plooXZsM1wBPnOtlUoIGgRlCY5jODdXj38vQtD-xKIx42k_RrLvDGaFxLClXxKmqvaLT1MAcFFzgrc7boy-vdXd4tK5XrazOZTczTyr0H8UKu0y92lOMINEucnFGqq0Zk1WmEP7w9G26GvSeOFxXt-Ow2T1vpwKchVnLBpcHJmrAvx8-YSz56l3cQF5rrW0PvyFIo_bHLHAI3ENNO8TDvlM1W8wjwRlN1sX2FPmjEzgnvamUmQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9qgrNdGf0jaTKvU0NgqbP4V7LkU313YnU3vEL97ABVLDH7SvkIrf5dc4qM4F1XwmtPq__hSDLa8CQDRTqdFVoPl7j4rrnGnGE09N93b7exhGthSyYhl9LGn17mwKw204Low6tM-WB1mC_XuGnJ_fi8LYE-pAGF1QizfJCnuKjeBgtdjcG0TxbqRVKDatuhZSO8VW70PuocBwK1B4Ee3Kh1eG9tuvywEEEK4NvP1uemg1xcqGEuCZikTEfbl_u7XKJs5QLG4igzaoJ-UL-QC4nCRsLUrUmVW5_zrJDXQuco6Z9Kro3oIEv8wVipipLqGl_5kveekC4CTtlpA9d2Dlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4AyCchUZLgrloR87bKmAkosgg4PaXEYGNZ58fmmyWNzII5l2FcE7nwpehSDI25j7D7t5XXoJICSh11TOU5rwWrQMeplORbh3YS_Hhj_zEZNWFy9INFPAI7tdAp2iURHXD4YXN8330ExLHSen2TwJFExNbvk2wmDFr3RtzSf01VvhZJyAJ2auALNip7t4yYoh0XuYncn-5XwRFrsXztCstS67zpuLtic_8jG2Kt6c3hiNHnVgZZpRIKIxMZdC0GCPqaqRo7031y-b1rwwiQpmcTBtIx7wsi_IZ7QlmtO4FPtyx9a1ipyVFcEh68Miurx0glnyNpmkzFTwmU4katZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzMR9bJMsQTld4H0jK2FUAehM5rIyEgY4OionAc3fAh7TM-MPVSyCJ3zOYIAeG6-_m75H-t6SvPwZUKu4sPShuEhnuw5DoJ0ilQ20UZ1MUA1HyibX17afDBpqbOTVhiDH1sxRVxx-veseQBksgHghFASF-Oh1ZFLwhdKThRNdMtJff2S4hN2WzvN5d7GRTrnKNltK9CNQRdPdnbEjntr2qssq2-PipSgTw1x0Eb3HuOzXqy-bg93DbeTP1ItxtOMZexWCbbu_InNqMsHE83MhtsQbuXab8mdIz-lWLQZUNVtTBC7KKWFY3G-Bjl7BkA9WkfC7D2L5Ep8rzOozbCc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9hVZeAv-SnVA2glvW7LxmKVwTME5WUdM5QBI8Ogpn1KYGPZ07KL4TgUtifISc4-hp2e0x6yuqpvtlDzfT8a95XufJSwZ9oYKNDg0T44NAQ2FbyaDYBzDXSBz280Mpfv5ShKvvzrwiUNxHYJ8p0jLDWKy_5EhnId0aGzSK0HFgUiFgGw2bp5W2ADNrI2i9lGBTWuTcBmawZZ4qf1ZBkpMdYXLoiYFXc1gr4aqTQWLQkQOhyKQvvTBJ0CmAUBKzyvnb04OFeBurEmWrFZLWEXC_t4alIGvgJtino6ihnC0itwTL3oXWuUr2zxkmlqa5RUnK9UlFkFzwhpkn5sivstXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kt-2O7fFr2Gn6qXDSymiiSiqqOHBuDIKQpTSIrSyY-TgT9uXaB1Veua32SU9eGHcdPfIH51eO1RUwP62CwCIbAN_EsMkWifcOtehQoCtkpFq58rv8NQ6JLtVSrwUXKVXSbKAWK5lgu92nNVYbGNqNoCdSQKifALyAYrec3K3hBE3b7XLH7VRrLkPRGWLfw3mydsARv1lRmyfH60wqa9BI8Zm9OUUaAewCnVva90PhtSoC3Bk8ZrGzFbRIFTwKZ_uU7FdwBwqJvXCXo3UuzU6SXZ7_cG23oYuVggjr-uqCcQHsueMqxkj2nPK6u_9YcRnHPSZUfdBZtf_NawT6Z7gTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بدرقۀ رهبر شهید انقلاب در حرم مطهر امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/448554" target="_blank">📅 03:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVBVYnOl4SqSvqx1-KXp8sec0c5azuCMEI_GiFGDWbhoBpMKhhmcV2ycRKLAxdx4ksgvERwr_It6DGZaDgDLeR7JB7-6LKHoiPvCpgEci290Ciiht-DGbnPEmgMfC38giqIwFFFQkMSZ5z_KuUo_1Cr_SmMjBtYe7E-oKezEk1qsxTJ0hia7Y8qZkJiGgKUauvBK4x-cmRPuRbgFoUjBLtlclnLa7Zxd8Zf-weAVbamVd-kCid6eCZAoRTJ83YG3ii3TGO3gdFO-iQ7tkd3GqAgHvqnhVWWnr5ujoMB3R89VxrpfgLhltLiB1d2lLmPCppP5W8E2el6K51SnKPj19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: منتظر سیلی سخت ایرانی‌ها باشید.
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/448553" target="_blank">📅 03:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946390c5b4.mp4?token=S4nRpZLemECs6CkDqgJKB7hWwejtpiPEBoo38dH0SkOHb_66yuHxnmfZ8ZsqIoqoTGKAXTOiK3G8K2I35HGY0EpQrUE5xqp1wyl44lq0itP5exhAoXf73KGIKVYaIQy1sqi2paIOljvS0I_Nd70lKigCldCZPjhEd9MpccXSFl3l4wKCdkoX2rA6ko-PKLWSZ3F7URcyBCdLfo5zkF3cGM1giYxZWVRRMR2TXAQgTXSda-Wp-ST3QJymhjHfJS17yd9KKRI3rZYsbKUNpfQXV02TfH5TL9AYfzjV7k1k9tIBZcw4ZFbl7heBUHwV8qvysH6hPlXdVgoqV2s7TsRCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946390c5b4.mp4?token=S4nRpZLemECs6CkDqgJKB7hWwejtpiPEBoo38dH0SkOHb_66yuHxnmfZ8ZsqIoqoTGKAXTOiK3G8K2I35HGY0EpQrUE5xqp1wyl44lq0itP5exhAoXf73KGIKVYaIQy1sqi2paIOljvS0I_Nd70lKigCldCZPjhEd9MpccXSFl3l4wKCdkoX2rA6ko-PKLWSZ3F7URcyBCdLfo5zkF3cGM1giYxZWVRRMR2TXAQgTXSda-Wp-ST3QJymhjHfJS17yd9KKRI3rZYsbKUNpfQXV02TfH5TL9AYfzjV7k1k9tIBZcw4ZFbl7heBUHwV8qvysH6hPlXdVgoqV2s7TsRCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب از باب الشهدای حرم امام حسین(ع)،‌ رهسپار حرم عباس(ع) شد
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/448552" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448551">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
دقایقی پیش مردم آق‌قلا صدای چند انفجار از محدوده این شهر شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و هنوز دربارۀ این انفجارها جزییات رسمی منتشر نشده است.
🔹
برخی منابع محلی از اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/448551" target="_blank">📅 03:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e08f738a.mp4?token=ALrJi2JsqSTol1KQOiyOn1FiyQI9yjv7OfH57AJRNK8_FechxRpK-b7ihw0XZ0u-sTIQL9rAZz27JzrB9O9z0FLvDCkr0KcBNj9aA9zgRoChPphtvoYIAX6QDtSrtQ8Q5sD-jP1sHUxg-Ah_Dzy-Ysrz32ogChPjofBycmlbVxAeWOqpnlkbdTRCJmc1uUs0_ZD5yPOzIWDpJFpd4PK1JA9Pr9AJUsCk0zVJfHTSvB62FQPT0qnlBXjxpRWtws8iZENpk_6Sga4lm4pOGrL5daphRr_-FbjCi_lMYWd10UtyWCO-X7b7xfofr3uNX4nk1_KBGy5DmejTxmbAUBiK3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e08f738a.mp4?token=ALrJi2JsqSTol1KQOiyOn1FiyQI9yjv7OfH57AJRNK8_FechxRpK-b7ihw0XZ0u-sTIQL9rAZz27JzrB9O9z0FLvDCkr0KcBNj9aA9zgRoChPphtvoYIAX6QDtSrtQ8Q5sD-jP1sHUxg-Ah_Dzy-Ysrz32ogChPjofBycmlbVxAeWOqpnlkbdTRCJmc1uUs0_ZD5yPOzIWDpJFpd4PK1JA9Pr9AJUsCk0zVJfHTSvB62FQPT0qnlBXjxpRWtws8iZENpk_6Sga4lm4pOGrL5daphRr_-FbjCi_lMYWd10UtyWCO-X7b7xfofr3uNX4nk1_KBGy5DmejTxmbAUBiK3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طواف پیکر رهبر شهید انقلاب بر ضریح حضرت سیدالشهدا، امام‌حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/448549" target="_blank">📅 03:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b29e540c3.mp4?token=CJjPdoWdVNicrsQLJufWtFaD0ZuVULEEYwOswhcergHZ2vi2rFLV1fugSebi5MD5i3OYCbC_AkJao2ElndDCmHE5YOMCabslqEdyWWeYROHgKD96_6aGqjs41UbKfgwqCPIeWtJB-MCT6SlcwyLNuFi19m5e9ZS1StSYk9QeVU8rnWieqjr7It23o9csqewr64JOtR7malerBT3W5e4pD9B4UbBHwKO0-H8EppMwvF57KT6cGm6NjHcYonFLH6-Ho6T_2bVVI1JjAqCbuIrhYotj1KfRQ9Qxd7R9dZXaqQ6M6Cpy5uOpI9Bl0odeTN8z_4ln68mc9P4Ds2NNBeJTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b29e540c3.mp4?token=CJjPdoWdVNicrsQLJufWtFaD0ZuVULEEYwOswhcergHZ2vi2rFLV1fugSebi5MD5i3OYCbC_AkJao2ElndDCmHE5YOMCabslqEdyWWeYROHgKD96_6aGqjs41UbKfgwqCPIeWtJB-MCT6SlcwyLNuFi19m5e9ZS1StSYk9QeVU8rnWieqjr7It23o9csqewr64JOtR7malerBT3W5e4pD9B4UbBHwKO0-H8EppMwvF57KT6cGm6NjHcYonFLH6-Ho6T_2bVVI1JjAqCbuIrhYotj1KfRQ9Qxd7R9dZXaqQ6M6Cpy5uOpI9Bl0odeTN8z_4ln68mc9P4Ds2NNBeJTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی و عزاداری عراقی‌ها، در وداع با رهبر شهید انقلاب در حرم امام‌حسین علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/448548" target="_blank">📅 03:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a3c37a50.mp4?token=As2yljzdDaRu4IRfC7U4s68GZRVR9pZU_hICjoXxRPtWXQzFWYTnBAuEqY2mIQ6qPeeVLaxcZ6XqmXS4kJcR_VKjVUyzH_oqSpIutP-cRUDSrk03mLyCSTDTXBTRQ0eJDvroN9KQNeW4rxpPzl3HBZsjwBMGX3LEF3d-va6Xz3vorFCA86sHN4p-c2497Y4m0ETW3gYz_872pbmYUZ0sKUKzHDxb-i4AMVdVrpXEwez1pR_6jcuBbmfYRc7B8l6aTlKtAHAxFjejvOvC8GMoXmDfC_GcGoQmi0Nw7rDbZJIdXMDgiFYOqCh4CYGPJrxgRdgklGcRtmUYZI5braawxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a3c37a50.mp4?token=As2yljzdDaRu4IRfC7U4s68GZRVR9pZU_hICjoXxRPtWXQzFWYTnBAuEqY2mIQ6qPeeVLaxcZ6XqmXS4kJcR_VKjVUyzH_oqSpIutP-cRUDSrk03mLyCSTDTXBTRQ0eJDvroN9KQNeW4rxpPzl3HBZsjwBMGX3LEF3d-va6Xz3vorFCA86sHN4p-c2497Y4m0ETW3gYz_872pbmYUZ0sKUKzHDxb-i4AMVdVrpXEwez1pR_6jcuBbmfYRc7B8l6aTlKtAHAxFjejvOvC8GMoXmDfC_GcGoQmi0Nw7rDbZJIdXMDgiFYOqCh4CYGPJrxgRdgklGcRtmUYZI5braawxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌های گریان مردم مشهد در انتظار رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/448547" target="_blank">📅 03:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c49b46eb.mp4?token=h4aU6tpiotibphoYmbT7LemV-8gg5g0yz_cSpUTDWmUzhtjETbw6yZ1GRavFg5R2GlxbuqyC6Gn0xvqyI2PqWesmBZRUB1TmTeK2CBpK6Fdw5kApJVyqYQIooYRAGisQhLhvX53G30aenooDFbhiVQ6xp8EIlR0zhm_QJ1Ig29KFXOX4i4mgGLi8vPq3HvPh3FsQc3PDSqdB90pnPDj7QkUEn_jpwNDyAKKMS-nBHRdfkX-y_qWGHUcG9KifS9UWINFsgkIlOs2PfiZymNErmfTpOLwJpUGxsX_uHHQoHxrnjpoz4bSHYP6aLltUWIrwxuOWgs3VU_NzWHqfy7ScAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c49b46eb.mp4?token=h4aU6tpiotibphoYmbT7LemV-8gg5g0yz_cSpUTDWmUzhtjETbw6yZ1GRavFg5R2GlxbuqyC6Gn0xvqyI2PqWesmBZRUB1TmTeK2CBpK6Fdw5kApJVyqYQIooYRAGisQhLhvX53G30aenooDFbhiVQ6xp8EIlR0zhm_QJ1Ig29KFXOX4i4mgGLi8vPq3HvPh3FsQc3PDSqdB90pnPDj7QkUEn_jpwNDyAKKMS-nBHRdfkX-y_qWGHUcG9KifS9UWINFsgkIlOs2PfiZymNErmfTpOLwJpUGxsX_uHHQoHxrnjpoz4bSHYP6aLltUWIrwxuOWgs3VU_NzWHqfy7ScAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر مطهر امام مجاهد شهید در حرم مطهر اباعبدالله(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/448546" target="_blank">📅 03:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751494424f.mp4?token=ekYTQ2068IPgcIwyNBfyJOAJz_lJlqJzDLlzwZiDXh47Fvc3IWXfcE8Rw656V6or28C__SivYukgCrBAfFZVZcgY_wRhM1MX4JH0WY9IWnDnQDCuDAXmlARNsnQ6FkUuSXqC_51QKzaS4fqm4WRw9QCBDyc2QW8GQuj_se3aytWP4x4uVW271VP4-s8zqAu_0_k7h4qxqfv-FTdiXIMQrXcxt4cMRNGgtXrNjDe1xcT46Lz0jnG4x80dH9bNtz7xxhjtaJfKQpxq66_ur0vm_7OjoOBs2eNqmxmchM0PqTP5_ONvT2V0DzkhiHpek17ANQhzgo-hlkWOqopdTSs0zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751494424f.mp4?token=ekYTQ2068IPgcIwyNBfyJOAJz_lJlqJzDLlzwZiDXh47Fvc3IWXfcE8Rw656V6or28C__SivYukgCrBAfFZVZcgY_wRhM1MX4JH0WY9IWnDnQDCuDAXmlARNsnQ6FkUuSXqC_51QKzaS4fqm4WRw9QCBDyc2QW8GQuj_se3aytWP4x4uVW271VP4-s8zqAu_0_k7h4qxqfv-FTdiXIMQrXcxt4cMRNGgtXrNjDe1xcT46Lz0jnG4x80dH9bNtz7xxhjtaJfKQpxq66_ur0vm_7OjoOBs2eNqmxmchM0PqTP5_ONvT2V0DzkhiHpek17ANQhzgo-hlkWOqopdTSs0zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای مشهد مقدس، ساعت‌ها پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/448545" target="_blank">📅 03:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f4fd72e.mp4?token=jXbRS0rEemtP_qHedxZv38KDd2WBge--w86VB5wWRIwtTWyzZUFZYuYktG8-Fwsw8XBt5YigpVyNLJrYTuX4OgNEAaEprcuLMj3CPfz8uH3TveIFKCRYIthm5IE3pHQblvR8dlMPa31RnU9EpD3RqAwN3PwYHyQ3xsqZpJ8-DWLNYTl257fB3rXNmWUsCErYogRsLzjRb6EtEpaIa7rUpT9IWmc5NDqWENrZ1QsfAUOLWtO8BQxXwUA4V_H5CDSdjfULze0cMbXpTXXE-_xovAUnkqkc1M59AerJ3whOCrd99hr-UPkRk1EEu5wG-o1jf9dBXjsPW_QqME-5SHTr-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f4fd72e.mp4?token=jXbRS0rEemtP_qHedxZv38KDd2WBge--w86VB5wWRIwtTWyzZUFZYuYktG8-Fwsw8XBt5YigpVyNLJrYTuX4OgNEAaEprcuLMj3CPfz8uH3TveIFKCRYIthm5IE3pHQblvR8dlMPa31RnU9EpD3RqAwN3PwYHyQ3xsqZpJ8-DWLNYTl257fB3rXNmWUsCErYogRsLzjRb6EtEpaIa7rUpT9IWmc5NDqWENrZ1QsfAUOLWtO8BQxXwUA4V_H5CDSdjfULze0cMbXpTXXE-_xovAUnkqkc1M59AerJ3whOCrd99hr-UPkRk1EEu5wG-o1jf9dBXjsPW_QqME-5SHTr-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله جوادی آملی: مردان الهی اهل انتقام هستند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/448544" target="_blank">📅 03:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448542">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yp8xCaEYwZfabWiIOXuac0dGj_65L0u_Mm2sPcLJi-BmrceOkbq_GhtDnyW8q2JVyvseMo_RuLU69fqIr6xz-eS5fc5S4cEZxpDaTHZQeV6KyUegqTc3KEsx54wyUjn2SxKp6YKO_-1ICH4Al-pNpfnbAlscif2cWKJAI8kJh5AgNG1WBQdXBpulro3Cpq3m6cPfSPPpzasvSjLIDuKABcwAM8bhSNhTI61U5VlD0rX5cpKkzcKZlKjvqCSsigTWkRx51NLYhDaeSVZQW7PG2X3xUeFgqgAERWpiiwJFhTtgNOd7z0IBwwbQk2aF9-VqLbuQg8-0VgM5RRv9hgbVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiPYzNJiYH_BmAI1eDqDV6B62bUhLpIi3DN2l2zRwpL1ZGU44ryt9VbK_b6UjHWy5SPO9M9U6xLjrU7_bGT8F4XlI9rDVT_2GLfbq4f-f2j0z0su5SfT7iTTKWpG9m0i6sfVYyg0cEF09ucWFULlc3aVEiTFzdj1SZlbJ3QHeBmcspVWAthFxgx72gENJOfC1pK4d6FKVMGNwTD6cTuF5fhZ8eo8SgIyTTdH0RnO7_Ry7xdNL1ZRkcOOo4XyFYjTPTphOeK0mAIvipE22qb719_JJmeVQj4d_CcvvKQzr78bdnofAnIY9tB1G1lI-CQnOUK6P7R0otOHP1ADi8hNqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از لحظۀ ورود پیکر رهبر شهید انقلاب بر دستان مردم عزادار به حرم مطهر سیدالشهدا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/448542" target="_blank">📅 03:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed101adfb2.mp4?token=RBHaIGXYw42J-8oR-tK5Lo--LUT18CjYixTU5yMSv3kZiSk1qVteIDvGqHKvtrB-0VB-t_4C0ZtS0glYxEy9YV-Dg3ELD7UIJMAd5UKW31FC5_apBEpYB9N3RXAnAFxOOJQDR88AA9NpDq1ZEH1BPL1monP0WUzIAyRFSnSYBKLFmQ-waIlRhpl6YGxJA8SoKDfOYGQUgWb0wQUa2xzT5QjdBgN4UQTiZnD6k8x0X-XyYuFkeW6oVzAYuxah4r8xpzF8hs8G3hAHCX6iCOYfS6bWjRtZeGCeqhHNFxP7wz0xX2iPh4Jk_kwgdtG3lzqKzhtczcV62YKyUiegxqM2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed101adfb2.mp4?token=RBHaIGXYw42J-8oR-tK5Lo--LUT18CjYixTU5yMSv3kZiSk1qVteIDvGqHKvtrB-0VB-t_4C0ZtS0glYxEy9YV-Dg3ELD7UIJMAd5UKW31FC5_apBEpYB9N3RXAnAFxOOJQDR88AA9NpDq1ZEH1BPL1monP0WUzIAyRFSnSYBKLFmQ-waIlRhpl6YGxJA8SoKDfOYGQUgWb0wQUa2xzT5QjdBgN4UQTiZnD6k8x0X-XyYuFkeW6oVzAYuxah4r8xpzF8hs8G3hAHCX6iCOYfS6bWjRtZeGCeqhHNFxP7wz0xX2iPh4Jk_kwgdtG3lzqKzhtczcV62YKyUiegxqM2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فی امان‌الله در پناه ابی‌عبدالله
◾️
پیکر مطهر امام مجاهد شهید پس از ساعت‌ها تشییع در کربلای معلی هم اینک در حرم امام حسین(ع) بر دستان مردم عزادار در حال تشییع است.
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/448541" target="_blank">📅 02:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448540">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55902132cb.mp4?token=W4_QNPYge0xotEIZ6KoS3652Rmye-DxhJ191szpe3RP5BgytWmL_MleAYB-8W450-ju0kTh1zkUytvg8ktQZBGqnCOXhKteCS53IAchJeJFTBePQkHDtF1emYgSYCadtuDz25VwG0Sew64iaXdXHiFfH8jANSWbg7KtfcrY_bjIAI415ErAEpeCVMcI-PPsY85P3s86YXe0TmpgYHEIq8GZO8QujhVU0sJFouTe1ALDYBx8FkhMn5RAclb4Zp7D6RvR1chyE8ZQx86d8tO2TJ08owJ2ykgOJUqunPhY8Oe2LNLgGAYe-ZqWRcSip2pw5sw310W_57Ji8vP8FVwhzdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55902132cb.mp4?token=W4_QNPYge0xotEIZ6KoS3652Rmye-DxhJ191szpe3RP5BgytWmL_MleAYB-8W450-ju0kTh1zkUytvg8ktQZBGqnCOXhKteCS53IAchJeJFTBePQkHDtF1emYgSYCadtuDz25VwG0Sew64iaXdXHiFfH8jANSWbg7KtfcrY_bjIAI415ErAEpeCVMcI-PPsY85P3s86YXe0TmpgYHEIq8GZO8QujhVU0sJFouTe1ALDYBx8FkhMn5RAclb4Zp7D6RvR1chyE8ZQx86d8tO2TJ08owJ2ykgOJUqunPhY8Oe2LNLgGAYe-ZqWRcSip2pw5sw310W_57Ji8vP8FVwhzdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السّلام علیک یا سیدالشهدا...
◾️
پیکر مطهر امام مجاهد شهید پس از ساعت‌ها تشییع در کربلای معلی هم اینک در حرم امام حسین(ع) بر دستان مردم عزادار در حال تشییع است.
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/448540" target="_blank">📅 02:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448538">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ccfcc8d8d.mp4?token=vb5znCFCytNBPtTU5tLRTt_N-N-UFoQtlLc-b-nF_U9DDLshj6p6ZyG2EcSAgQ4BJYRwFwe9TeWHm7KS4x4aGzmjxG_PhEYMtK3WZqwdhzvl3lPZwSvQZ2_yneskTBaXKAKS4c2T0O3L_kQMOkyw31BNH-xOp-iTKWOxYGQK0EPpL48IlAV1ylnixoIJqwUE5GmiyXqnKHXSNGoyhqyKZUvxfZQAJbwLiOhh5u1k3hObVleNbGCeV0cTj41m96OU2ZyWk914CYzIwQwlJORdg6x91iAoye3l-zRgRhsXkrNfrD76QvRFrGBx-EQ79mIM7mY4Q6HVUfgB5Lqfglvd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ccfcc8d8d.mp4?token=vb5znCFCytNBPtTU5tLRTt_N-N-UFoQtlLc-b-nF_U9DDLshj6p6ZyG2EcSAgQ4BJYRwFwe9TeWHm7KS4x4aGzmjxG_PhEYMtK3WZqwdhzvl3lPZwSvQZ2_yneskTBaXKAKS4c2T0O3L_kQMOkyw31BNH-xOp-iTKWOxYGQK0EPpL48IlAV1ylnixoIJqwUE5GmiyXqnKHXSNGoyhqyKZUvxfZQAJbwLiOhh5u1k3hObVleNbGCeV0cTj41m96OU2ZyWk914CYzIwQwlJORdg6x91iAoye3l-zRgRhsXkrNfrD76QvRFrGBx-EQ79mIM7mY4Q6HVUfgB5Lqfglvd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب بر دستان مردم عزادار وارد حرم مطهر امام حسین علیه‌السلام شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/448538" target="_blank">📅 02:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448537">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
دقایقی پیش مردم آق‌قلا صدای چند انفجار از محدوده این شهر شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و هنوز دربارۀ این انفجارها جزییات رسمی منتشر نشده است.
🔹
برخی منابع محلی از اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا خبر می‌دهند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/448537" target="_blank">📅 02:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d6ca89ba.mp4?token=PL-HQwhVjmXHyME0jtmFVjEgxj6zKXjsMVJgVhX0xJuxVMjWVywRY3s5qyMBbYtpKK2F9oeZgLJKHrpv68secB0r_c0CM0v49t9iDyUUzMXyR7d85QokauA3VsmX4rBxupB13M3eeyGKgPkmuOuZKaRjPrCgCOM5YRgMK0e0p9tKzz1qpfTLW_CmHuTvReCOPONNznMVBEHZ45GTnFPxcx5O8USwOFe7Vt8lvwQvR_JMzLY_4pi9MkcCVKVydS0Dl7e3qLVyUTZGQyGTI6yRJu84TNn568onJScB1mjaYNUZHrYab4pOUsI78R2Hmw03ZQja7QutxCAp4UuP2sMEmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d6ca89ba.mp4?token=PL-HQwhVjmXHyME0jtmFVjEgxj6zKXjsMVJgVhX0xJuxVMjWVywRY3s5qyMBbYtpKK2F9oeZgLJKHrpv68secB0r_c0CM0v49t9iDyUUzMXyR7d85QokauA3VsmX4rBxupB13M3eeyGKgPkmuOuZKaRjPrCgCOM5YRgMK0e0p9tKzz1qpfTLW_CmHuTvReCOPONNznMVBEHZ45GTnFPxcx5O8USwOFe7Vt8lvwQvR_JMzLY_4pi9MkcCVKVydS0Dl7e3qLVyUTZGQyGTI6yRJu84TNn568onJScB1mjaYNUZHrYab4pOUsI78R2Hmw03ZQja7QutxCAp4UuP2sMEmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
پیکر مطهر امام شهید به حرم سیدالشهدا(ع) رسید
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/448536" target="_blank">📅 02:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42934e17ad.mp4?token=Jgx869YTMeqLAg1uCGWnBPi1S7QYwbDz-HMKzY6NRdVOaWV_vlUIWE0s0CSKP5gqDVE7RwUaOni9JHe13UcWSt9Tau_E5QRiLamUHpyn_RFPnUHjGXk327XfZuCUx79awVWaoRsx8rnVZwxqNtWRu3snj8Y22kFlrWcx8rmvjf2nbNWkREsEGu1tqVq7_3FWDhItvjOYsJk6BiikcHuQLGHBGFyxyXYUcTOxHyfXGA8fn_JGoT-jvT1BDiCZsy_U_9INKV88PslsXp-lnZdh4UwYjE4QY25lZlzmBj5U9i5jvwKEfb_0wQUtOZ2pIzOqD5l7s2wG2AVhEw05nHQ0gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42934e17ad.mp4?token=Jgx869YTMeqLAg1uCGWnBPi1S7QYwbDz-HMKzY6NRdVOaWV_vlUIWE0s0CSKP5gqDVE7RwUaOni9JHe13UcWSt9Tau_E5QRiLamUHpyn_RFPnUHjGXk327XfZuCUx79awVWaoRsx8rnVZwxqNtWRu3snj8Y22kFlrWcx8rmvjf2nbNWkREsEGu1tqVq7_3FWDhItvjOYsJk6BiikcHuQLGHBGFyxyXYUcTOxHyfXGA8fn_JGoT-jvT1BDiCZsy_U_9INKV88PslsXp-lnZdh4UwYjE4QY25lZlzmBj5U9i5jvwKEfb_0wQUtOZ2pIzOqD5l7s2wG2AVhEw05nHQ0gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان یک عمر دوری…
◾️
امام مجاهد شهید، حضرت آیت‌الله سیدعلی حسینی خامنه‌ای بالاخره به زیارت کربلا رفت.
◾️
هر وقت صحبت زیارت امام حسین(ع) در کربلا می‌شد می‌فرمود: گر چه دوریم، به یاد تو سخن می‌گوییم؛ حالا امروز آقای شهیدمان به زیارت ارباب شهیدشان رفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/448535" target="_blank">📅 02:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448534">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100b7e3f69.mp4?token=EEn2ohSWJ9AUbwhzc8L0NjwvfjeLaR6JND3HIE41sCv_o6BuWEatyniTWwbPBT3JryzwIGI2mWent4wbzwY3-yD_6DkhF_pnNt5muSG0KmUEc_FzWoonQPDs1c1lYBNJRRAxaqFaWDcc9LgiRxF1_uMJ4NP_z-OfirowxN5F5tz8kNlPJtYbcU34eL_pmAr-O3vgaiBswAY4nJx1cUqQY22yJzUdZko2h3xX9HWnbPD0V0TQxHE9aJe8L5uDqHhz0qFiS9r_DmEWVMlcvluKYX-sH-ZUiyrNLde1oWgD3xVMq551ji2SsQ0osVn5kFdtVmdL4NLZQuP_WN3mutWaNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100b7e3f69.mp4?token=EEn2ohSWJ9AUbwhzc8L0NjwvfjeLaR6JND3HIE41sCv_o6BuWEatyniTWwbPBT3JryzwIGI2mWent4wbzwY3-yD_6DkhF_pnNt5muSG0KmUEc_FzWoonQPDs1c1lYBNJRRAxaqFaWDcc9LgiRxF1_uMJ4NP_z-OfirowxN5F5tz8kNlPJtYbcU34eL_pmAr-O3vgaiBswAY4nJx1cUqQY22yJzUdZko2h3xX9HWnbPD0V0TQxHE9aJe8L5uDqHhz0qFiS9r_DmEWVMlcvluKYX-sH-ZUiyrNLde1oWgD3xVMq551ji2SsQ0osVn5kFdtVmdL4NLZQuP_WN3mutWaNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش صدای سلام قائد شهید امت به حضرت سیدالشهدا(ع) در بین الحرمین، لحظاتی پیش از ورود پیکر مطهر امام مجاهد شهید.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/448534" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448533">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b563cb680.mp4?token=O3DdLAEjtJbuQ5-NZ6-bdXooZvZEHKsRpga81mI2_H9COjN6eHEhjXk9VxImMIhM7DUabVHLj2T7JQ2ADgdpHhkWdbZlD328AH-rxicz6q6ETwpzjSBoqKaNHdAmEZKqTd2bb4nvfEDxHwaLP2cofCeiGZp3uGSXSuEpnS17HvcYLSaRawDVkA1wr0ou10mWyi0R_x0pRc1onuCbtbvTroCtyrGOMzv76A4y6iDHqtBdDPTZ5W3za_HH_tZF2pR0y884e2NsxqpbtB7TWBSfRxqlumd5xfVrgT7w4-2LOaVGQHsA7Ed8NWA0qhDihfZqMEmu2ClKnkM3hduU9-_hJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b563cb680.mp4?token=O3DdLAEjtJbuQ5-NZ6-bdXooZvZEHKsRpga81mI2_H9COjN6eHEhjXk9VxImMIhM7DUabVHLj2T7JQ2ADgdpHhkWdbZlD328AH-rxicz6q6ETwpzjSBoqKaNHdAmEZKqTd2bb4nvfEDxHwaLP2cofCeiGZp3uGSXSuEpnS17HvcYLSaRawDVkA1wr0ou10mWyi0R_x0pRc1onuCbtbvTroCtyrGOMzv76A4y6iDHqtBdDPTZ5W3za_HH_tZF2pR0y884e2NsxqpbtB7TWBSfRxqlumd5xfVrgT7w4-2LOaVGQHsA7Ed8NWA0qhDihfZqMEmu2ClKnkM3hduU9-_hJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقا به حرم سیدالشهدا رسید
◾️
پیکر مطهر رهبر گرامی انقلاب در آستانه ورود به حرم مطهر سیدالشهداء علیه‌السلام است. و پایان ۶۹ سال فراق...
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/448533" target="_blank">📅 02:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448532">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ00oJ9BMSm0muzfEn62cquc5HHdKKYCiM3l1CGnEXZBoM6nj_YGoMIHUbJDJu91aql0Jt1-AUhzgc3WtHH_jBU0f0o2hxpbuCZOSqkVsK68GPyBfDvldQ0pSdqgiIMxwr_EaJ0jYXB072n5-6b2PlbSUd0B4PN3CMZK3P0tlq01RDJHHaqxIHLiH5-zAXy9zs3-pjgPH5IZDHIYnDvp4Via0r8VoRWLiVVoQerxYAuDGMGS08l2W7wvRBpqsRypZeJWmsqaB5Q5lIWyvDSZPn7Yviv9uSArZO6Rsq3J0JZFhl_vaqeVfTQ7PlgZEhQpRbTvPS-N8_DoJwR6s0IcaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
#طرح
|
قوموا لله
▪️
تا دقایق دیگر ورود پیکر مطهر امام مجاهد شهید، حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به بین‌الحرمین و پایان ۶۹ سال فراق
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/448532" target="_blank">📅 02:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91504895e9.mp4?token=KOK8J7gmfUJ-NBMblVaMHuppUxkwqBWJtBI9lu8hEYPIi-nqs3zQ1qkGk6-j93PJBQDUMF7_9YJ4yf1YaT0LeYamWw-G7h1Tl17H0kRtmfrv9cYrz80i-Nxk9GEp2m2ylaJdCqRKmHGsla498iKRNuQwheWTPv0p3AMIgLL3qqniVSD0Rb0lePCFrQsCRrOwTLj0Dp8sbqqrWHt7SkIsQLEukFeTTpTC7q3jfo8MCThsoIdqP2Ir1OocKOs7RaCOQO-UkbA5ssYhohSb5QMaZsnRLRF_ka5YskiiRKFONSYzIGta4d-R2t3NLumxutR74jmcc1_mIeI_flxmGMi-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91504895e9.mp4?token=KOK8J7gmfUJ-NBMblVaMHuppUxkwqBWJtBI9lu8hEYPIi-nqs3zQ1qkGk6-j93PJBQDUMF7_9YJ4yf1YaT0LeYamWw-G7h1Tl17H0kRtmfrv9cYrz80i-Nxk9GEp2m2ylaJdCqRKmHGsla498iKRNuQwheWTPv0p3AMIgLL3qqniVSD0Rb0lePCFrQsCRrOwTLj0Dp8sbqqrWHt7SkIsQLEukFeTTpTC7q3jfo8MCThsoIdqP2Ir1OocKOs7RaCOQO-UkbA5ssYhohSb5QMaZsnRLRF_ka5YskiiRKFONSYzIGta4d-R2t3NLumxutR74jmcc1_mIeI_flxmGMi-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دوباره توهم پیروزی نظامی بر ایران را تکرار کرد
🔹
رئیس جمهور تروریست آمریکا در گفتگو با خبرنگاران حین پرواز از ترکیه به آمریکا، ادعا کرد: «ما از نظر نظامی بر آنها پیروز شده‌ایم. آنها دقایقی پیش با ما تماس گرفتند و بسیار مشتاق به امضای توافق هستند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/448531" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448530">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
شهادت یک نفر در حملۀ آمریکا به ایرانشهر
🔹
فرماندار ایرانشهر: در جریان حملۀ دشمن به ایرانشهر، مردم صدای چهار انفجار شدید را شنیدند.
🔹
پس از بررسی دقیق مشخص شد اصابت پرتابۀ دشمن به بخشی از ساختمان تأسیسات پرواز و ساختمان ایستگاه هواشناسی فرودگاه ایرانشهر خسارت وارد کرده است.
🔹
در اثر این حملات خالد قادری نیروی کشیک ساختمان هواشناسی مستقر در فرودگاه ایرانشهر به شهادت رسید.
📝
جزییات بیشتر از میزان خسارت متعاقبا اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/448530" target="_blank">📅 02:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef98b3d0ee.mp4?token=ukZZzItpIxlgnxoisZ5UomxJWOqjiRRq-oq0qHHzqDNQBTD81wsVF5hYHuQnHga71NH6osaHhGh0kfDkVcdbGbfgg4gwFzz2FpUTMkna1sTQb7hNE3lSGIZg93xTMF7ogBBOBpgUbCtzwh-MfC8ZPL1ROL2_WS8vTwgw5TbXVohezqN306vAGiWODfsSvkFQOtVJ8vk89Tkd01D02lKWN7gauqI3cA974P1aa0UOjTU1Wrg4mVALFIBZnSONGC6XDy3joN-D4Bjt-bWY6ZEndksAHqHYF3PKf26x3O6-hKFqzcbbhdifoJ9G3qsl4t-ty7iRtEB8GrBLyghhItMwSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef98b3d0ee.mp4?token=ukZZzItpIxlgnxoisZ5UomxJWOqjiRRq-oq0qHHzqDNQBTD81wsVF5hYHuQnHga71NH6osaHhGh0kfDkVcdbGbfgg4gwFzz2FpUTMkna1sTQb7hNE3lSGIZg93xTMF7ogBBOBpgUbCtzwh-MfC8ZPL1ROL2_WS8vTwgw5TbXVohezqN306vAGiWODfsSvkFQOtVJ8vk89Tkd01D02lKWN7gauqI3cA974P1aa0UOjTU1Wrg4mVALFIBZnSONGC6XDy3joN-D4Bjt-bWY6ZEndksAHqHYF3PKf26x3O6-hKFqzcbbhdifoJ9G3qsl4t-ty7iRtEB8GrBLyghhItMwSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید به خیابان باب‌القبله رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/448527" target="_blank">📅 02:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb3e36225.mp4?token=WP5sPbtbgEGWjr0DkXBdF5P4xRpf-u4ec0oueZMf82_OF2Nq_PXwctawYY47oZDvgpTbf0bFjKrgRW1iK4HA89OQ6Va3BDgFZsPa4yEYGPjtmnb8I05sRZvds10DVNfKrBE-7onzBiVAhqtyzLG1pQUo22S6okdGXsEOWSL11hmUm6dm5Vodc8--NqBFlryM_e_wSJGl-_N0zfj4Rj8Gysoj_rzqZiVJ9zKFHQDGGDyKV60UQwZP029aW4dVpsiLM1aEmi2BteiUyYkZBjeNFKghL7bjzi9v5-21MjZJ4MmFkoOqLkqbvLnHnurt7V1v6ZHVSdnPidHU2Ei2FX9g8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb3e36225.mp4?token=WP5sPbtbgEGWjr0DkXBdF5P4xRpf-u4ec0oueZMf82_OF2Nq_PXwctawYY47oZDvgpTbf0bFjKrgRW1iK4HA89OQ6Va3BDgFZsPa4yEYGPjtmnb8I05sRZvds10DVNfKrBE-7onzBiVAhqtyzLG1pQUo22S6okdGXsEOWSL11hmUm6dm5Vodc8--NqBFlryM_e_wSJGl-_N0zfj4Rj8Gysoj_rzqZiVJ9zKFHQDGGDyKV60UQwZP029aW4dVpsiLM1aEmi2BteiUyYkZBjeNFKghL7bjzi9v5-21MjZJ4MmFkoOqLkqbvLnHnurt7V1v6ZHVSdnPidHU2Ei2FX9g8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مردم عزادار در جوار پیکر مطهر رهبر شهید انقلاب در نزدیکی بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/448526" target="_blank">📅 02:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNuFf86ChudoJLFUTt-pkqkG9QSt2XbSGZHdchPs9rkfaQVC6bJOTCteLRIcm4QZX6kFBNfDCeKjVsORXUQEGHR442fhPyQB1PKYEbTCCOqj4jA91nD0oW6DDnXCB3yYvy3-rx0cnPcQ-bPneveffcdtrbKBfSYI7Ib9_NTipsU5s66jkhmv3E7IxVfwS-iXRSbTr3ZNOP9EQe446shFOFkH9hIv9_Oqibc5PnNIhCU9ZWMQJ3wPPOge7sR1SwVv5axomCZ8ujfQXLqeZunp-el72vwtMQYulh5NjrHzKiNc61zALAOVplmtmqAKvXIW9E6stJbWMCFaH7R87Z91vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U07DevSbLXt1O9Pls8TtDPD_B0AYwVxcEfEx0d1qQMLzFE8wEtbtzIrOwqcgGnMvoTaMNISwlKD1DdqWEa6yC-EyLbDOzP0wACR4ETF6OaYQ-fODPTOjaDLyWeuOsnwGA04jXl42TADDosRtcTCd4aKVQKB3_nF8OUSntmYkqBkxMQ7QFISmyrlfGZ5lWEqMlv_nac70xqktKlONIUUtdsgvrGGdR-bZ26xL_E0fWUKCg-RHPX_alwJLIr2AV4-p0OOzEfBFi1SVD8JK2fj3g2ekoKOxfo4G06dGbQndZ5W5qZh0ksRRNSvdwReWKFFp6ijwbgObwsbJM7EiRJIDiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moti4ltX0su1WG6wZp4F8rWxYZlUqpC2une_weEnOQowncV1W2kje6-u2i-HIyDB9LT_rwDW3qhAXAIajS6O8OQZckURLgRg6OMB3vZlb3kROGMos6lYuFXsMMw8EOT3EPA_vwpow7xGOe8pvQvRMytzKDQsAobPOa_OfAu8xzOu2nJ8wit70ktaJqYDMfhvlNkUaHwhi_1orm80YmuyjWblgpkQlkHgltyDsRRHajOvrLB4wLg43wf58i0jZ0MwEfiVuLq_5nszNQS1YxQhzcP37G-JTVwJKCi2r-h6hxsLmB0Pw9xwUjcpxdjhx1i3BjdxMo6lDY2MUEyX3W0FkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-CF6W1eOyvhxPFkP2y9gVVVXevqPVhfC4txc5JAIWdcAhmdQo6kvhzkG5PXMLL7sYzpbeCgtGukKMEgd-_a2Hfk1PvRopqhQYtOi5bA87CaNeQ7TiAA7B02RT7eHfBnnvczOE-gWHKJ3UknFbDTKUUE76nzzEMrgoxOaGXTkned0Si7J07Dlv1LU2hocsQ8F1LXN5hbZ3RN7JgoNwbtB_8DbAb2LmaxCiHLfpJF8qcDaFpxk7mL6K2U0KG5An0E4fWjl4I9TIbjC0MDWpHnc3Ps7XRyOBzzJBeIv4GxF76IqBPlDkZPR91A7kPsZEesbHKP_QPIoUHkFkAfU-Vu2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱۸ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/448522" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448514">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTqKSVN6DO2WCBvRRX16ka3hJLYV-DmkSBD0u2jJvfEPBuXhYd-fjLRGOTJgpuNvgnxXbo-eJaIbyIIQR8DbtRt-a9obHhlgVBjA7qQDX5ViOqDzKt1oiDzbZ5hzDcDauLq3xJCGRGTgkMWnJ45_0D1i5klbZQLHFq_CuzLQjXu70n7L2CY4XaJxAeGUAU0KEjIQ8zdHTCaen_4rwXkAte5FZaF3oLgNChGJ4Ct7GZeAHcjWLz4SGwqdGAihd5ykRk2yRXp7pwKXgc2dAkXoFL_70Rum-JZfadlsfee0WD8sl9oNhiAA1mhYlX0hqXXzu6sGy0nMGLD4C7Gml6EgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csSAsBvv5BXIIdywgfPyyxIEriixbBWuJ1E8N1NtOBesb8MiSWX1dODXKrAYjMbYQAaet33e7FQn3_oZP8AoC0qJasCBl4Q3K-r3AWQje-KKl-Lo2DgBYEvy5TFinG6N0MxyI97QroVzsh7OJd--LfMwUPFLIZxqDnf8rlAqjgn0xBUs5rWN0F5NU80VXJCWOP5dbVeH0yL7AWS1ncJXgGrbkxMq3mFMUDtCu07x9EtDRCiWQj1QGoTxt1mk5T_cUzCiyNG43hIreiuJBbrmjfThKniURdNP8R6uTK2S2a4eBqBEyJqVPr-fNXxzDtpoHzSD9e5fDThRCdLRtFZnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l96WdQT66BVvkYMBB_ylqHMgtYxysr2HS4jSK0H_aasVRVrm-efpPPPrww10pOCPEyXIAExFOXYW06nYLxXmcWFHNIXTthqUCPcp73ZL8841h6pTNL-n5tPrakGEicoL60k5u9jAUARpgpzW8uM98AkemtWcNZ8pOwE7xIg2H2V9UaGL4YvOnwPKZEXgxfyopRgUNtP10BY10x5U8LS0FYo0UP-dMHsv5f1NCyqqMZFXHHsGE6ZLxuEdscWWg6LDzEU58tpgB9F-EE_9kblz1Vx25Qul2YpSa4vIzhsgiKGm6K7-980T51BeV7DyPZgnGGlGRTSELsdzp8Xyj9568g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4JQBM-5OZWP5DXKJuFIxGMwEKg77HimltE0gbkR2cwIknCsq44oDGmr-ZKNUZceI9kGzDYPlGdRYOuScMOxxavD741ntk6uHBsVaY3dZe_MeNVRM3jP_gV4zOjg9CmBDHEQaerq0DNhds5rm-9UmjYIWkwRoW4Qbmfgt3jtgsZWd77GYvQaZxxfrAdNAH9vkYWKD35J0fn8LR-lSIgRO3JZ1oJ8cJBK3RmBN58nmNunFZy5VbaOGRPJbELYwPqDxWIEi2BG7RDHG0zLztrMIeRI-agbeLqzq3e06r0GPfbHiTIjU3lutlvLtRf-uVO7TMuJIlVXd92jAZMSqT5PkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOlh9ztVc_O0Z8uEA14Yfm1_2mVVpqh5vHn4AEs7Y-xUF5e9Lc1doc0DDjl-aSaeadhiGvcrTLdiEKkGLPNNYPRYw6vxxWC5sHqxGPL1A2Az4v88yaq5sN3DZU4_OYjqHbObEh_1IxvIYy0D-fn9WLKKACjExAOiwHgtX8Sq7PxhBju-_j5B77MDSXo6szDqu_U1I_fflaZIe28JLNu7bJ8SvcmdIbPhdoiwaTNKj9BkGN0dyxcNmXcYSrucBihpiaZP69UMQaGRGQSxlL6tvKi7pQTxU7u4FESNRzh2l5iG03ERRw5zJw62LnRAhaKE-FcLZWn2V-EUqZic_3Or9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tX8Ie16Zi_SpfKPZr15P2mFly_CK6vnPB9fwnysoGuWMJ6Wghqit2pBBVvcilrP8WfZF_ihdOAwwf4JGUDISx3vwilpAyuon5aGs80WpOEvYlqYprbHYe54mcNN2Fh8vCW_OvGMs_4_VxrqqVbxDAbZycOBrwePKrXqd2e-cM5ploh853itz3V2NprahEiRqjECVQ5QmSUsGp-PTCdjqIZO02ncO0Ra275xPaLeGBGJ93F1coemRo0scRyU5zFXrizozAsFo0x83o1T2x76XXRMANIRL-ITX5UlT_MPo6-I8g-zxbnSFDYdrF-VNKWjIUTeB3wTesZmhyz5JFU3xIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tp3hjgqzAIdN3g7sPRxMoPr4T6iWmPUc8CMAloECPmV0l2Dfe1Zc8R7FzCbxnx2xVLstJIepc3PULnkrdtG6lV4lRV5RmYWbjklAl9LmxCCzq2HMImlVg1QxMOVqQCgSmBbFZ0Zc_F08hQd57R6gMLC5VJi-CaWW-bP28Cujz0Vsm3F-aaFtjMSsLsv1qva18_i5rUoH4WQsDnLRWOcN9nBAhII_8IFcj2YxSbA3RbW2CPPcouPSSiWlrTeyIXKeZkrRB62kTnDKpq4xGJmRlFbOkqRE9sLWRm0HRKWu-zY6rtWdavvs1CeUmW5WRqNvTij7SgAjD4IjDNUUbW2uJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FGPlPyiPIrK6f7FAxDXpfNnh_zT5Ovu22M7ENnuIyKTgH0lbb-1zjdVj8eVJB4I0Cstku0JReSwKKbs38aVRZPe3jHPeZIBOnx6M_6AeoriSGTeM8SMhTM40afV1aQWx7s0l7rYrOODaBhMktbQAT9lnCmoWTqbnbLNHOu9jqSBsF8dGrajY4z7rZBEcmjZkvlSQx_pHdd2DBjVZj_aZSHLzWieU--mJZDpf7aexQZ1Z9YtEaM09EMPtQf3YFHgnjRUDH9EGBs6kAWw7CVx1726b4WUtrZkQW7hICimlNnKU5QRBQZjpV9UcUg2XhxFYWtfFCL5WeY0wVyAsgWdKPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/448514" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ktLv6Sbx-hPm08JLOW-Hkl2KX08OzHE5RAP4uqCsSvReZx8OVWzEEtJy4n5Jz3PKKIcz10u6mzGl6-8oMfLs5yZvzrmHxTaIzKalK8xqSjDFNras493nMX0oJ2f7YuIJc9pIlINSuSR5fSpcBUxAc2c2EMHfqJt9rhDqI0GO6cwBKjxrsddlOC7JO50ROmk27e2j_zjIOEwigUOWwFJBosfn8Jvwc8QKyA9WzZ4kj-RilpcwqE1ZH38BCpZnZJXJLLOFwZIaKvzRFPJrbn7ES0l07grrhH3garBe9LcY0JIB0Ij1TTtfRfGppbxrZmILaJ57klcrC1GOUZR-x6qoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKD_ITNgHIhvlrGXxlpvvbO6r3w-aW31uAsGAbBNZHhZMTrcwiZmA61821P3zxt1ExYgN914YhChWr9Ew5wZlzSMrtHi5-bNhl2DAqBY6B80KLh_CbmNk87ZI2JhtDZyc7wJGuMotOkQuBWzhzX6pw2ve8oIxCOnP8qRninCcuKVY582ce9NpZz62G-s40scRQhCbD2_h1aHcoKAVB_68ioGXEK1Q0_cYKwhwloUSsBs93yJvTno-4_7bv4GffVFxJE2sCK53DvPs2e_YPbegVa4ZmAJvQD2qf8kMDiz8htrWGtk7-AYE3WUPeWTVS0nhZHUFejxTg2fdINFI4uaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kobii7Dq6dUI3vkPMNZbLodoeIB5ra_BSCPrwxZ-9N-zOYg-0VEIt43gcAdnZ6HGoL894XsA6-M9eIh-X3wqnrNYWUyP63RHzr4XfJglyylvqoztVR4UpGvqFAjCzAIApOBn_UdSCYuZdAaNmApEQirlgVxHKs3zeKTyFP1GZmIkwN3D9FrACMGYsopglrvf98dwLRo3CzouqtkeH0ooDk1AliHL8DTOBMF9yA0MfZCPM5UQYtv_9UwLt_2Bz_zXYTNqAmAtNfzk6O_OGnbwucD399TFYOswUGuarDDrHfbAxChQ7gEmNttKndjqekHuJsC1XgGPaj-FiiJfvRl5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7Ov7gncSBUDPQYDTfhnklFtBNTUciVGFSpNDaGd-d698hL9LFs3vgLdMVPalwLZXYP5Q5H9sDMiMYYKl_yKLQIQNh06mIrUKG1ap9aIssrD5mHQPKJ8oBkmx-wfOOkecKj366KK3XcxVD-rakc0BvwEbb4a_1dONErbYpJaE4GbBv95_ZQnuKCI-w_bcS8HU9msdEdiKLWnlQ3-N-KyeCr2j93b0NZasybMPBui5gv-rOsj05Y0C03Il813LtnsKqxReRac0-80wP7XDdM5sKs9rGcrnbk3x_WuKlRpxI75tkOw_Wf_u_UuN8M2rUSRGHbdC8fIMB_i9BFDuFejew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzH_qYz5sCQEbyexofglnGHOUDl8axRdppEHHMD_E_4R5OM8MlUdJofQOpZZY17m2hHIFozfGrNzmSUSDAZzHVs4sg97vYtX5HBWRfr9zURBYND89umet2W_zd1MWOAehvKP2X9qSAjC03CqTp5y4wI-nVRG3DyIVPPfhKvcTM3JVSVR73g9RXowNJyD-piSwzv9aaHQBi0jECT3htlJEp_vHOIBzKt_1EypShQStZDItDG8yWNWYCWiIe7Xo-DB_w8H-k-bBOLhXHVDrs55RkOESTmF-0tDrBZeKhavJDAL9XG8aJvTa6exo6nYAse_Jes3pS_IYo0UFNgiur79fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم عراق در بین‌الحرمین منتظر پیکر مطهر رهبر شهید انقلاب هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/448509" target="_blank">📅 02:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a278106e.mp4?token=eVLkh_8Tal46pmkOacrnBC1zLe8vYCQa-3xQS4Um3kmnj4bBXUpMrNsIGTrgFdovznlUtYVsks98JpSFHCm5Zl48qZ54foJt0BPRSiZ60CzpWj7lQFK43uojTc0WU6TE9Ho88_mtHS6yKlAL_bnl2qMsDnPT1B-ALjTuwqxi_IpAIWyPqmA67V0TUCAN0zdIEVsnAQ1IqpxBNExDVQ7IbEccl5LK8KKHFUiejQD5wFRyZ4C08xjV7e-1zVFYX2xGyhFVZfl-XoIfC6FwBm7RPYwYNRqHQ43IUorFLW9j2D229V1adAPh6sHEqGEjGIqVY-eX_BduHDfVOs91_rommQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a278106e.mp4?token=eVLkh_8Tal46pmkOacrnBC1zLe8vYCQa-3xQS4Um3kmnj4bBXUpMrNsIGTrgFdovznlUtYVsks98JpSFHCm5Zl48qZ54foJt0BPRSiZ60CzpWj7lQFK43uojTc0WU6TE9Ho88_mtHS6yKlAL_bnl2qMsDnPT1B-ALjTuwqxi_IpAIWyPqmA67V0TUCAN0zdIEVsnAQ1IqpxBNExDVQ7IbEccl5LK8KKHFUiejQD5wFRyZ4C08xjV7e-1zVFYX2xGyhFVZfl-XoIfC6FwBm7RPYwYNRqHQ43IUorFLW9j2D229V1adAPh6sHEqGEjGIqVY-eX_BduHDfVOs91_rommQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خامنه‌ای جانباز شهید به سمت حرم عباس(ع) می‌رود
◾️
هم‌اکنون انبوه عزاداران عراقی در شارع‌العباس(ع) پیکر مطهر امام مجاهد شهید را به سوی بین‌الحرمین بدرقه می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/448508" target="_blank">📅 01:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2bcb646e.mp4?token=ayLSTiy0pp1Ljg0BDSoJm_abXFBcUrZAm3ojar744kajAZetRnjSEMyrn8fo9gWTeLPqLOhbSSMBB-JYET-MVjkeoE78qQucLUEQKvihkKe4Kh7gII3LOV0yBNQawE8iVOor9ByqZRxhijP9ADEcAYnmV7kLQZLc5U0YNC2Z1qh12t-jxKQu2Jplm1uHTkoERUp-ooCOx-0NMXi6wPcslIwOAoivz6xB2NO-TJPaVdfIpMATlu7cIjsSRHyMRQrcJLIkxUm5A8sDEenoDHn49AkYLRNqcV7I_fTmsZSIA7gFUB3Q9NfoqHOHN4I5k2KFzivoAFHl0wqLJt7k1n2B8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2bcb646e.mp4?token=ayLSTiy0pp1Ljg0BDSoJm_abXFBcUrZAm3ojar744kajAZetRnjSEMyrn8fo9gWTeLPqLOhbSSMBB-JYET-MVjkeoE78qQucLUEQKvihkKe4Kh7gII3LOV0yBNQawE8iVOor9ByqZRxhijP9ADEcAYnmV7kLQZLc5U0YNC2Z1qh12t-jxKQu2Jplm1uHTkoERUp-ooCOx-0NMXi6wPcslIwOAoivz6xB2NO-TJPaVdfIpMATlu7cIjsSRHyMRQrcJLIkxUm5A8sDEenoDHn49AkYLRNqcV7I_fTmsZSIA7gFUB3Q9NfoqHOHN4I5k2KFzivoAFHl0wqLJt7k1n2B8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان امام‌رضا(ع) مشهد، ساعت‌ها پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448507" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">واشنگتن: آتش‌بس با ایران متوقف شده است
🔹
یک مقام آمریکایی بامداد پنجشنبه به شبکه «سی‌ان‌ان» گفت که آتش‌بس بین واشنگتن و تهران «حداقل به‌طور موقت متوقف شده است».
🔹
سی‌ان‌ان به نقل از این مقام آمریکایی گزارش داد: «وضعیت با ایران همچنان ناپایدار است و احتمال حملات بیشتر، فراتر از آنچه اعلام شده، وجود دارد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448506" target="_blank">📅 01:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643200c4cf.mp4?token=G5NDECN4bYQsTxItzcZegwfIIfhngt8jnaua0m2642L3hK1VIPPkMIlgZQodhW9gaHhbdZeeQK0yoUZ4I41Gu-OpJ-2_e5bVigb04VCBVs5xhKaMxzfGg0mRTHXQmq3iiaKan9IS9VDNEsbtr838oYIJo7evtJGc6uiy2ZjovcC_LQnBRHL8DF2deDgCfwW87JXUDT71dpzb4pPBnpmTBDUcUBmNjoDTeO3tHG7-_2rUjVBppCXLLnh3qxln2aanyvL6m9vZqYT60OeWUHR8dNw9-H2uPUwp0nZ5lu8IYRugCChsBje1hzYt8nitLKbJGDUKkNqVj_9qJe61-rPgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643200c4cf.mp4?token=G5NDECN4bYQsTxItzcZegwfIIfhngt8jnaua0m2642L3hK1VIPPkMIlgZQodhW9gaHhbdZeeQK0yoUZ4I41Gu-OpJ-2_e5bVigb04VCBVs5xhKaMxzfGg0mRTHXQmq3iiaKan9IS9VDNEsbtr838oYIJo7evtJGc6uiy2ZjovcC_LQnBRHL8DF2deDgCfwW87JXUDT71dpzb4pPBnpmTBDUcUBmNjoDTeO3tHG7-_2rUjVBppCXLLnh3qxln2aanyvL6m9vZqYT60OeWUHR8dNw9-H2uPUwp0nZ5lu8IYRugCChsBje1hzYt8nitLKbJGDUKkNqVj_9qJe61-rPgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین قاب مشترک از پیکر رهبر شهید انقلاب با گنبد حرم مطهر حضرت ابالفضل العباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448505" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0Q-_Un3IyEjb-unZbdRme9BGmUqLbSRcZ8QxM6kQy6QWzw4aK_d7NuUG8NFhUaKsw69iLOLGML1jok_xRNusB5upeAb1Ocb_SpLSi4Ar0Vsm6v8QCWPXA8nfkOIHdhMfKq-miSKF5WrRIuqTqokgzW4FxgakmPrCMxl30TrBFgYkA5dRp9i3flcnWn59HvqPsd2Zy5AKdOayGrASBayZLPXW-Af2Y0wt8aax9lhR9ACtsejEuZw_yDIVPI2Ynih0G1eek2Kou-qT9dVvsRNz3MAk2CCvRjx_Qw47FNDTLHx_jxVp_85P3zWhDITL0z3t7Rdk1eflAd3QEWykf76LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویری که ترامپ با نام حملات امشب استفاده کرده، مربوط به جنگ ۱۲ روزه و حملات به انبارهای نفت شهران است.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448504" target="_blank">📅 01:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9043fa28a.mp4?token=qUf-YQM86USkFPkp9VPcVYTbnXLwJhiIONx8lliTnTRjobDc9ikwaXSJEKY6-_3qZljslr22BMppX1udWIJTY1dEauUFtyqyXtNZVyxFKxZHZ7JR2aPKOiI-TnWRfIEbWVKgy8md467rKZG_lZibmppE77qB8chY6LQdUILGHvp1f06F0Zig5DXUp9gHhWGXcoasI31avmhTdR60Y7eaVUm6BY8oNHifixmpUK-m772kE3a8r02m0IBpLSjnuhUxmJGE6VacRXbYy_8ewwPuXOA9zz6RzKXJCN9GWT3MWTu0Ewc7-u0NA6QSJzeGxvRycHsPfVIPOXrTTGsTppAZQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9043fa28a.mp4?token=qUf-YQM86USkFPkp9VPcVYTbnXLwJhiIONx8lliTnTRjobDc9ikwaXSJEKY6-_3qZljslr22BMppX1udWIJTY1dEauUFtyqyXtNZVyxFKxZHZ7JR2aPKOiI-TnWRfIEbWVKgy8md467rKZG_lZibmppE77qB8chY6LQdUILGHvp1f06F0Zig5DXUp9gHhWGXcoasI31avmhTdR60Y7eaVUm6BY8oNHifixmpUK-m772kE3a8r02m0IBpLSjnuhUxmJGE6VacRXbYy_8ewwPuXOA9zz6RzKXJCN9GWT3MWTu0Ewc7-u0NA6QSJzeGxvRycHsPfVIPOXrTTGsTppAZQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مشهد، ساعت‌ها مانده به آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448503" target="_blank">📅 01:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای ترامپ دربارۀ تجاوزات امشب به ایران
🔹
رئیس جمهور آمریکا بامداد پنجشنبه مدعی شد: «این پاسخی به حمله دیروز تهران به کشتی‌ها است. اگر دوباره اتفاق بیافتد، اوضاع بسیار بدتر خواهد شد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448502" target="_blank">📅 01:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
حملۀ آمریکا به برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار
🔹
محمدسعید اربابی، مدیرعامل سازمان منطقه آزاد چابهار: در جریان حملۀ ساعتی پیش آمریکا به چابهار، برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار هدف قرار گرفت و آسیب دید.
🔹
در این حملات یکی از انبارهای منطقه آزاد چابهار نیز هدف قرار گرفته است.
🔹
در حال حاضر خدمات‌رسانی و اجرای عملیات تخلیه خودروهای موجود در انبارها تداوم دارد.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448501" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68eb3526c9.mp4?token=k4JN1QDPVYI88WHcDYauNTPFdI5xV9CC5Tol89GZ6XJLQt4Ash4B4oE5pf9aSJ5qH-uSD_2T7cQ0oNoOkxgmwo8qzaaJVJwV35WEhNK0tUqWvDDEQVmz7p6A4l8BZRiuwx0j_qB33_6xrx6peLRWlPjgCZCCaPY9oQp_Wrg2tLnT2VMFJq1NX5QyLEh_x8CrkUc9OEIF8puXhanbLcBLB7HKCzocHM5tFbyDP2PHuqjqwHQxLEHYKqOOyI5uTZLXD7jiwxyFs-hjghzxhrKUHjGEU0d4mvbWrmsEb4pY_3Dby8sXhMdmzDev40iXRtAW485IHuuRcVXEb0zK7MApQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68eb3526c9.mp4?token=k4JN1QDPVYI88WHcDYauNTPFdI5xV9CC5Tol89GZ6XJLQt4Ash4B4oE5pf9aSJ5qH-uSD_2T7cQ0oNoOkxgmwo8qzaaJVJwV35WEhNK0tUqWvDDEQVmz7p6A4l8BZRiuwx0j_qB33_6xrx6peLRWlPjgCZCCaPY9oQp_Wrg2tLnT2VMFJq1NX5QyLEh_x8CrkUc9OEIF8puXhanbLcBLB7HKCzocHM5tFbyDP2PHuqjqwHQxLEHYKqOOyI5uTZLXD7jiwxyFs-hjghzxhrKUHjGEU0d4mvbWrmsEb4pY_3Dby8sXhMdmzDev40iXRtAW485IHuuRcVXEb0zK7MApQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیام و تشییع میلیونی پیکر رهبر شهید انقلاب در شارع‌العباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448500" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
در جریان حمله آمریکا به چابهار، ترکش‌های پرتابه‌های دشمن به بیمارستان امام علی(ع) این شهر اصابت و به بخش‌هایی از آن آسیب وارد کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448499" target="_blank">📅 01:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f8fb26f.mp4?token=EQuQEsBH-oBLUMZLchxlAnKfwECT1nGs3zz3t2c6aa4fo0ZYimYlPcqSj4UJwoK0r9lpM5F1ZT86BYfphUN1cA7hxpvJyFsNqMWChdQSEKUWNOBguuw46qn7QtQ6Up7VGgnbTekWP8PZHQz-04oZ7WEQNx8EAb7ajLKv3az1XRQr2rBkYodg4RHy7xAeAfMiUdCDymgZjOHzahsUZa8IQdAueeOlHPWWxpiNm-Kh2wmyYSg04k2l33aUeLKI2kiDgeQJ8e7H2Gb4ii_4_bAHpxDZE9xCzQX-FC3AoKLVDiQjvnVqT40P29_FRN5HD_BjeOlWaPoX1b9H4hB6HQBVfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f8fb26f.mp4?token=EQuQEsBH-oBLUMZLchxlAnKfwECT1nGs3zz3t2c6aa4fo0ZYimYlPcqSj4UJwoK0r9lpM5F1ZT86BYfphUN1cA7hxpvJyFsNqMWChdQSEKUWNOBguuw46qn7QtQ6Up7VGgnbTekWP8PZHQz-04oZ7WEQNx8EAb7ajLKv3az1XRQr2rBkYodg4RHy7xAeAfMiUdCDymgZjOHzahsUZa8IQdAueeOlHPWWxpiNm-Kh2wmyYSg04k2l33aUeLKI2kiDgeQJ8e7H2Gb4ii_4_bAHpxDZE9xCzQX-FC3AoKLVDiQjvnVqT40P29_FRN5HD_BjeOlWaPoX1b9H4hB6HQBVfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر رهبر شهید انقلاب در شارع‌العباس(ع) در حال حرکت به سوی بین‌الحرمین است.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/448498" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281365467e.mp4?token=IggJxsqdWThmkA9arLKB9ERZF92toJVy85JhR5v081auFchuB7iXn8rcIXQ5h3BfZNo4BTugXBd5TErdAJll8WdQCFBabBmITqk54HJbpma6vFja3HOWitirVVeWO7P8fHUd_qR31am1cKwph761Ua3gawbaATlkd8jcbQm8sWIWePkA90uko78uoycpIzKTDk9y42muFQk6wdGA6_lPeolS_JvhNUJXZzsBWzan71xsiwOViThp47R5NrE6Ma8g6LA0p9JMhp5kT1f2996QCs6ApyhGb_VUFKayzi24UEe23mFS5_K07ybVrBB0nNhvCcTUiGFA96SltYPW6cBYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281365467e.mp4?token=IggJxsqdWThmkA9arLKB9ERZF92toJVy85JhR5v081auFchuB7iXn8rcIXQ5h3BfZNo4BTugXBd5TErdAJll8WdQCFBabBmITqk54HJbpma6vFja3HOWitirVVeWO7P8fHUd_qR31am1cKwph761Ua3gawbaATlkd8jcbQm8sWIWePkA90uko78uoycpIzKTDk9y42muFQk6wdGA6_lPeolS_JvhNUJXZzsBWzan71xsiwOViThp47R5NrE6Ma8g6LA0p9JMhp5kT1f2996QCs6ApyhGb_VUFKayzi24UEe23mFS5_K07ybVrBB0nNhvCcTUiGFA96SltYPW6cBYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال عراقی‌ها از پیکر مطهر رهبر شهید انقلاب در شارع‌العباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/448497" target="_blank">📅 01:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e1f66af0.mp4?token=OVlL_0fHSR74R7kcvrI_-yXlLMZlqjExTkXYuNttb5puwLS0nJ24M6DYWySNlQ5bpHKi2HCKdCqMOEYMmme6CtDNbp6u9icneJ6AvV1EhKMPa-NvE8-x9cC8C_A1s36xKZq7hWXLUC_Svsep_Ysw2wn2elYjcjFoQHNiTFh6uH7u2P2t610x3-8iGV88LidSDw3dlnxW8MAhms_MHMbEgd06zSLieLtek7nKodvan7NaWRPXNl2PzMIbWdxSPuuYBo89YJllQ5rtzQg9UqPCrrBkHnhrO0JXUspDDy73aehNpC0CsphP2Hn0CpWfq7hBLWFBt_aL2Fi_kWHuUe-4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e1f66af0.mp4?token=OVlL_0fHSR74R7kcvrI_-yXlLMZlqjExTkXYuNttb5puwLS0nJ24M6DYWySNlQ5bpHKi2HCKdCqMOEYMmme6CtDNbp6u9icneJ6AvV1EhKMPa-NvE8-x9cC8C_A1s36xKZq7hWXLUC_Svsep_Ysw2wn2elYjcjFoQHNiTFh6uH7u2P2t610x3-8iGV88LidSDw3dlnxW8MAhms_MHMbEgd06zSLieLtek7nKodvan7NaWRPXNl2PzMIbWdxSPuuYBo89YJllQ5rtzQg9UqPCrrBkHnhrO0JXUspDDy73aehNpC0CsphP2Hn0CpWfq7hBLWFBt_aL2Fi_kWHuUe-4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق بیش از ۱۰ ساعت است که حتی در خیابان‌های فرعی، منتظر پیکر رهبر شهید و مشغول عزاداری‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/448496" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRr0kL9ovNIEdANaaFgFuQs0HC9UUyrL9v2v-6fzcDRSVWKZKzcsbRi4o0r14Dv0UoRFc5CFuxd4ju5t7_qMO-gCCDA_D3EWxN_fvEMqWUKMY9TtmSOCWIRVM8pBOP9EDEAkh-rHbabLp-V22Y9_SrBN2FFKX672IJN4mUSsC_FIv34u07YtXeJ6QrJGCtpZO6ng5Sxw8n9v5Gv9ShN1IgzJUfTHF1svOhlm3JBTkdpMH57jJt-DiQv6AjF7k9iqNKU3l6p6WZTBmXCRkW9tjprTzjv-1xrZHdNSH0PhGnOql1qpqgIVp5T0fH1tgqBM56uJbCi1qBPfw00lNhRrqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: دشمن و همدستانش به‌شدت تنبیه خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/448495" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9793440cc1.mp4?token=Aw2ZdmEaQQhHdJfgcWVcFkCKdv3fvRJFebv-8jkgtqkorSkuJOMT6o20AviPTJxe_zf13XLTZXjkdHqDgdgbUD_7OoroAOi8z02uaA5G1QYMnLwbTBLclfAZxYGJ5jUFkGYI-1A4BX9T8uYYGazieyG3qANdkVQgmKKchhKnV0EZ87vL5F5KfIZJtHf4dcSvjK2D1gQPXh8Ixko0ANKdi9nlrDxWzjXp_k-zBQzecDWOoaNX9a2OGwLrpzN3wRkKmih2x66PEzU2aX5mxqcEA05vgtbJw1j6lnX-9utEyCUMp0-Iw9WRztyNWsAAVAqfGepVNYo12D3bTKAxw5GM5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9793440cc1.mp4?token=Aw2ZdmEaQQhHdJfgcWVcFkCKdv3fvRJFebv-8jkgtqkorSkuJOMT6o20AviPTJxe_zf13XLTZXjkdHqDgdgbUD_7OoroAOi8z02uaA5G1QYMnLwbTBLclfAZxYGJ5jUFkGYI-1A4BX9T8uYYGazieyG3qANdkVQgmKKchhKnV0EZ87vL5F5KfIZJtHf4dcSvjK2D1gQPXh8Ixko0ANKdi9nlrDxWzjXp_k-zBQzecDWOoaNX9a2OGwLrpzN3wRkKmih2x66PEzU2aX5mxqcEA05vgtbJw1j6lnX-9utEyCUMp0-Iw9WRztyNWsAAVAqfGepVNYo12D3bTKAxw5GM5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت عراقی‌ها در تشییع رهبر شهید انقلاب در شهر کربلا
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/448494" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117965e108.mp4?token=dM9g25lQxnGcRzKwKMBZrPsYToHeMlIbuLhfyLK4uyHqS1uuPajPqRRP1K4EeW3Z62JOMNXgzHSyYYaW8ScUW9hT5erRNGx-yTjFz91BAyHhWt3q5D9jxGAhb0KcRTDtlDl15xcbF0cZbPYX1tIoIm1CPOZgup6Ix1wB8TOtA8-W288ueI8xjWr0o-Wu0sp8JZZYtgKvTelsHOCoVxivdIv0FfuSZp6vSqtr857RAaNefUZjOo0HzaCji4W9IQyTTENyZDU3BNm0-UodS1d9xHBpnRkVCjCMpOHiKMKux_V3E2kvEcOPEY7sbdmL0VFywv_mmeqMzHNuSDNA94JIjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117965e108.mp4?token=dM9g25lQxnGcRzKwKMBZrPsYToHeMlIbuLhfyLK4uyHqS1uuPajPqRRP1K4EeW3Z62JOMNXgzHSyYYaW8ScUW9hT5erRNGx-yTjFz91BAyHhWt3q5D9jxGAhb0KcRTDtlDl15xcbF0cZbPYX1tIoIm1CPOZgup6Ix1wB8TOtA8-W288ueI8xjWr0o-Wu0sp8JZZYtgKvTelsHOCoVxivdIv0FfuSZp6vSqtr857RAaNefUZjOo0HzaCji4W9IQyTTENyZDU3BNm0-UodS1d9xHBpnRkVCjCMpOHiKMKux_V3E2kvEcOPEY7sbdmL0VFywv_mmeqMzHNuSDNA94JIjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب، با استقبال مردم عراق وارد شارع‌العباس(ع) شد  @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/448493" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
🔸
چغادک در حملات روز گذشته ارتش تروریست رژیم آمریکا نیز هدف قرار گرفته بود.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/448492" target="_blank">📅 00:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90accfc73.mp4?token=MCZgi_4PPr77FMMXIpoSRWcg-BL2qwX8ECX5vC4ktQW3UdAzdUDlT9M4lCfo9RD7IsGhmbeETS9Tdi-bxPXUVWOdpmrjwwXpeKKjVqI8vi31n1W4EhOSvJ9v9IqNy_4rjtauzW8YGe2OOpXvgmkGGF-c465ITDH7Lxei8xg9-jhKv3PbtmepeHvUfDz9c_5u3Jur4l7S9bgSaIdvICc3OAxwvMs6AWOHxbct1T_EEV9prLdNOmIz49lDcfFR-47E68q52hC1gl4VHhzB-It-3fIbN6TkyqhfZEGQ5NQ5-TcU3O_9riAbEvnnP1G7IGmCL50iJQcaw0YTTE28GTw4pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90accfc73.mp4?token=MCZgi_4PPr77FMMXIpoSRWcg-BL2qwX8ECX5vC4ktQW3UdAzdUDlT9M4lCfo9RD7IsGhmbeETS9Tdi-bxPXUVWOdpmrjwwXpeKKjVqI8vi31n1W4EhOSvJ9v9IqNy_4rjtauzW8YGe2OOpXvgmkGGF-c465ITDH7Lxei8xg9-jhKv3PbtmepeHvUfDz9c_5u3Jur4l7S9bgSaIdvICc3OAxwvMs6AWOHxbct1T_EEV9prLdNOmIz49lDcfFR-47E68q52hC1gl4VHhzB-It-3fIbN6TkyqhfZEGQ5NQ5-TcU3O_9riAbEvnnP1G7IGmCL50iJQcaw0YTTE28GTw4pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب در مسیر حرم اباعبدالله(ع)  @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/448491" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c96062094.mp4?token=u1ymD_PIvpMHd6uH4pirH4PpCqZqA8CdyGzLOLKDvmcZnSAQ80fVZiAt2uamxBsKzJAsZBMNVtH2HPLAWLJ4fqCAZxGIuUkYBENq5hqTFqtgWB5_0UlqRs0xA1WmjGXoXD6EEse8d63l5DXCNTfbFW6JVvJ7ZOU3lHoXBFztspJjED39bgKy-6lAsQC9pzf0zY2-q1JmThT-fXUBukBh68kemyQwQ0cVs3sObTVSqWVdIQfrO2Pb7NEAJz1785EtM3i61GnQ8WvnTF-2R-gB4o8tgt0XB87g6Ejl3DsFnnS8bRYjE7K3TfApig-VCMr0vilOspEjWs69X-Jk2ry1-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c96062094.mp4?token=u1ymD_PIvpMHd6uH4pirH4PpCqZqA8CdyGzLOLKDvmcZnSAQ80fVZiAt2uamxBsKzJAsZBMNVtH2HPLAWLJ4fqCAZxGIuUkYBENq5hqTFqtgWB5_0UlqRs0xA1WmjGXoXD6EEse8d63l5DXCNTfbFW6JVvJ7ZOU3lHoXBFztspJjED39bgKy-6lAsQC9pzf0zY2-q1JmThT-fXUBukBh68kemyQwQ0cVs3sObTVSqWVdIQfrO2Pb7NEAJz1785EtM3i61GnQ8WvnTF-2R-gB4o8tgt0XB87g6Ejl3DsFnnS8bRYjE7K3TfApig-VCMr0vilOspEjWs69X-Jk2ry1-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار از جزیرۀ بوموسی
🔹
دقایقی پیش ساکنان جزیرۀ بوموسی صدای ۳ انفجار در این جزیره شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقباً اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/448490" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار از جزیرۀ بوموسی
🔹
دقایقی پیش ساکنان جزیرۀ بوموسی صدای ۳ انفجار در این جزیره شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقباً اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/448489" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
صدای انفجار در چابهار و کنارک هم شنیده شد
🔹
دقایقی پیش مردم در چابهار و کنارک هم صدای چندین انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست. @Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/448488" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LGzcI8vrkfUfWDFI41BcWNktXwyVwPKD7fSohw2-WRMDD__TSUWtkzvfVkXRVQc77oqEScUHjjapLSYcG-eSJBJ8IpEuXOO6GxiR5V82chnCinnHo0tCBGhF_W6smUxW9jRARPOf7MESh7C4iwbUOMgAPjzqB9xkERsvxODOalGxDRsZ1Z8Juvdwcou6bS7wPueCP77oJt_gQ4Lud8nPvPOIr6utYMvIoFsXfSGB4wpCAjV1IchkwQ8RJvRoOZLgMcAYS6VTXutYgLl5mbj_baYvA_u1nVUUBhKxyBike12fTGYJT6xuSjLxb9mffZUcQi8WVp5ZB-AM_26R59xUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKNb3Rj6h1FyyUdMTqN6cwZZjv8pALzpkyDVXgXTqYBRjeeRZEtcmtzlhrkCAFMvt7z-ZxjJtmQEVXCfy5zKCWlN6HfxQw6W3hP3b-2HGuOSh3PQR-TGAh2nKCd5GcYwCX1TUXaENkIeGfWJ02CGuyyHYlyU_QYHtLzbDYp3oHo0CmBbbaqT1hvJ1r_03sre-bqC-yhdPlFCYBpatfJE6vpNwJ7LplDBi3w-h00Todi1y1NsCBKlQT_gpZeMC7n7GIs69t9g3XpFS5pqrLzFiK_e_9lD6Uj8rcNX6GmI59QxD15WVU3d5R8O2s8kzXfcBRu9NtONzzbGpUbZc1KbGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXGL-ZvlBZ-ldPV9IRUahAJjnObKQc8bpUwWhgUBK8_KLD40YDjaF1xehqV4mtOvwILLBFp08DYoj0x9vhKJjrPE18rEmVVrZnEOWSpk8_gCnLWccXyMQmpurmSY4suXuAsOWVaMWQkeXBdfGKiy6tavTK3BduBL-HG6xzH1I0vqQuyBlomUmKCNGTpt7UOmRoO3Yj8xCefiLGCgKtTSzrpc8xtgsNgeAYg4KcvdsipMeG8bLr-DvCHUXyvUSrzeHkvHTyYIryVEqF_udomunaAFgRfNcKAwDdV_jZ2H2X95_O8PHboSdVi_QXma5dwERZDb8ASse9bC3ev2hL3F_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWyANOaIUY6-zIQvIya7VE_sEu7yA23jyuRT4lKQhfpdEEA3S7TX7LyAz2opGCg0hP8D0FDNZYT6FMIiu1aZyXweOrMQGHObjnqMztTD9dFFmxSghJ2Ta_i8NmwgY1JSL_bKoTsKrZw9Gsb6eyezXDTibncIMNmLyakrGVno-ae2WVAGPRp9wsNtzUetRgqA9FIm5PYcjplOwsXJ4t0C8upzB9MIakewB7lDxFd5TnIOycuW6OqD5tzj2-l2mgoWgTufNMfAN40mvXEomwbT59GatXWkR-2_vrIqxTyGmI0KZbundZFF-fgehhvFKjbQgTCJ8h6jmSuDU_qZEkewrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFoeNV4CCO2KMIPQMdfj9G82bJvRt_IsUgPKKf2OWvH59-NegSiUXjVX4rZmL1dzcqahdkN5SZb7loVTTEWs0xd4c-8UkjJ5Mr4D6-tW04Sdppjerm7EfX2JsxgDYczQsTZCoXH7K5T9cYsni6Ox8qyEWx-4l0GD7lcba62rFWLxpjpnK9HwxRbJyRpWTdO4CMtqAYirCxsO3EypbIKHLgQVnP44LBoqc7y1_3c2YLrCsbEDp9Cq5sF8jsSND4cbddbj7CsXA2So-ulf-0wj58ZvggbJ-WxOVtrE3AHQvuxSyBKib3VMh2oJH7gJMhFO9khIIM4ihNRvgTKk_4Q6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g74yH7rHlJIJL6TMjuenbNtB4Mq2qsGG4_YTf8aJ4_xMzW1gv0nUOb6sEVlZ_0Yvgrxa7KOQOkPUwnggLr4svs-TzMTjJJtAl12Q74kNerVPTCtnP3CfOvF6S0fZdBeAP4q7LiOxh9iY5zqdO-QYk4pa_HlPLZdvCLzw3xxmT3AAK3wMp6HOuW_tw9B279X710nrPBBnzjobS_5wdAs19MXFGcs4sYWDWhUUJH8b-0JHMH2wiKOF3Z45lhgc9CJCM2pzP5T0ePZOOyI_Gqj1qpyk2i_JUj_M5ljSuSWyQc8FoAP_A-GH5BO6HjVLebTpaFPFgUFRN-If_E9NywHC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9ng8YeB0P7P0bu3ZnDln83CDqNtN-peMFbWvDSzk9YcV15hr3dngHQB8dhRdoSoy-cxEBuiUtd8FWjkAAPhiqU3V_wDPt42Q3ekcGvbKxfh_DiLzi2T5e14kFw2VxL0m1Qyi_ZV_0UBJah3OuTpp_wP2GzHWO0eSbJcvZ5VW9FQTz9rBjIy2MDcHRCnxVfNCa4nhC4g1h2YgcYXnSvS6rfnAP7bioLbA1xaPzpCS3Un17iZ6u8pRrMU_CEYB7ShXpFgC2qIgioMO9GSsFrZXJolkAOkhOg6pqV4tmElMoikA-K_iyToNjj4RjfIOE2g5QKydyWAie15kak1Xxnw8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مشهد در تکاپوی تشییع رهبر شهید انقلاب
عکس: مرتضی مطهری‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/448481" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbf1069a5.mp4?token=fSaaDtY_UseFdUHJ3okAnWBjk07FSa7n0CgdrtTKozdMPM-APRIhmTrtXwO4mrPGrRhhaRNbD-WadB5FSvFaWpZsHhS5sAq7k1BpFBnZmCp8i7ZJJLSfJtdr_zFowxh-sP_M1Rg4whY-1KXuibnL_QR_Ailc1I6GC16fXm18QuV8zWsyNm8i2nxZ_QpUd6PlNfys3fRy4G1JCqvZsiCbGiP7ysw0KGkKFbpTAWy7d9d1C3abRu9-fALjn0N7-py8QpMAE0lxOkEH7OsXo0l53dBv_I-82ka18Q2NxsJqhgExQlcqQ4VBJ8irGHy9Rls0RHf6MN9GEujiuNCrcoxFUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbf1069a5.mp4?token=fSaaDtY_UseFdUHJ3okAnWBjk07FSa7n0CgdrtTKozdMPM-APRIhmTrtXwO4mrPGrRhhaRNbD-WadB5FSvFaWpZsHhS5sAq7k1BpFBnZmCp8i7ZJJLSfJtdr_zFowxh-sP_M1Rg4whY-1KXuibnL_QR_Ailc1I6GC16fXm18QuV8zWsyNm8i2nxZ_QpUd6PlNfys3fRy4G1JCqvZsiCbGiP7ysw0KGkKFbpTAWy7d9d1C3abRu9-fALjn0N7-py8QpMAE0lxOkEH7OsXo0l53dBv_I-82ka18Q2NxsJqhgExQlcqQ4VBJ8irGHy9Rls0RHf6MN9GEujiuNCrcoxFUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیام کربلا در پاسداشت خون امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448480" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8fe21e57.mp4?token=M_BGNCRhshlzBX7TijpiFZSkc_lLvTCrs_5a_KeSxykhHSz3U3jxDiYGSJjw2fhXMb_PKmoVH7uVpog7mfeD3MNftAHDq5PObUVcHCQef7_L_VGZTHQtGIgtYsFlKhW1JXkircMYLAV2nUj4xwQ2lhJliVQC-HZtNoD-OQN2KwXSrNnLigNMdRJiWwux1zJJFuOwtqb1eniNCplgz-KeQLFY9Fbvt6DEPCRXVreo0bDKwSci0mnvG35-TgLLMSg1q2jq4eR-F8rqyiOpQ09IXjzpBvoE4YUgZKn3EDsDb7Sew81oKzAj7Z6jPdm05L_N-0YVyvp33DTNMdGusVFicg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8fe21e57.mp4?token=M_BGNCRhshlzBX7TijpiFZSkc_lLvTCrs_5a_KeSxykhHSz3U3jxDiYGSJjw2fhXMb_PKmoVH7uVpog7mfeD3MNftAHDq5PObUVcHCQef7_L_VGZTHQtGIgtYsFlKhW1JXkircMYLAV2nUj4xwQ2lhJliVQC-HZtNoD-OQN2KwXSrNnLigNMdRJiWwux1zJJFuOwtqb1eniNCplgz-KeQLFY9Fbvt6DEPCRXVreo0bDKwSci0mnvG35-TgLLMSg1q2jq4eR-F8rqyiOpQ09IXjzpBvoE4YUgZKn3EDsDb7Sew81oKzAj7Z6jPdm05L_N-0YVyvp33DTNMdGusVFicg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فدای جان پاکی که جان‌فدای ما شد...
🔹
نماهنگ «آه از آن اسفند» با صدای علیرضا افتخاری و شعری از محمدمهدی سیار.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448479" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448478">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b02a9986.mp4?token=oAhSaMh9u8zattwWDNCo99LXh8WCiZJkXTF2EN0uvGU4lKtrRwyf4qrvAR7IpyCnyB1QX_X3Sz1EUzKte6UdtjO7Zje0uUVGCk8Qh7WZkCSzCMpbt88yCASKJlT1rijhoON4MkGPjturzEtqUqWsO_bbyX4yc-uL4s_kDTaS-khJkQjDHsMf4nVhESUfJCENTh4m1lZ0OlARTnstGecykFT-f7KKCmfgtHI8UNQ5XHgdlRiJhIk_oEyLkQDSs8_LiGPeibYvqnzp0SlENObSDs0yoneGSB3kdwl5SOtEFlpFcSGsOR3ZhrqXDxk4Ll4scGtqg1qvTs5uxUW3zs4KJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b02a9986.mp4?token=oAhSaMh9u8zattwWDNCo99LXh8WCiZJkXTF2EN0uvGU4lKtrRwyf4qrvAR7IpyCnyB1QX_X3Sz1EUzKte6UdtjO7Zje0uUVGCk8Qh7WZkCSzCMpbt88yCASKJlT1rijhoON4MkGPjturzEtqUqWsO_bbyX4yc-uL4s_kDTaS-khJkQjDHsMf4nVhESUfJCENTh4m1lZ0OlARTnstGecykFT-f7KKCmfgtHI8UNQ5XHgdlRiJhIk_oEyLkQDSs8_LiGPeibYvqnzp0SlENObSDs0yoneGSB3kdwl5SOtEFlpFcSGsOR3ZhrqXDxk4Ll4scGtqg1qvTs5uxUW3zs4KJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب در مسیر حرم اباعبدالله(ع)  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448478" target="_blank">📅 00:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448477">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxDoG_w7mNmWiTQXziENZ-eJpExUVwPVGLT_a1NinM3WT5sU41i19pIySOHDJqGQs3958J1cY88qt9laEZx2_vXyIwGO0UigjTzT6pkA3J5t54U-4iaUAQ8RRE9zkwwAXUl8YqJoqVRTjv8E4qBk5WrRaWmIxSM_K8X7JMGgDceGFGGC57qclBkg0akOdWIZ72X6svXX81LxqMY7SFTKwm2VPuuVrKdKjYSREMHy_jTAwqpRAec0GJDOfvtbuV6W8pxD41eSOl-CAI1vGGKQ-YO9mzqytVBN54nD37_qqy3YxCRAJItJq5os1bIAx4aV68pdYtdZPLxBWGbxS-_LlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قدردانی سردار قاآنی از ملت شریف عراق در پی تشییع باشکوه رهبر شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/448477" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448476">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
رویترز: قیمت نفت خام برنت با ۵.۲ درصد افزایش، به ۷۸.۰۲ دلار در هر بشکه رسید.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/448476" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448475">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
صدای انفجار در چابهار و کنارک هم شنیده شد
🔹
دقایقی پیش مردم در چابهار و کنارک هم صدای چندین انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست. @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/448475" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448474">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad76bbcd64.mp4?token=sxKncaH60yl7XRhAcxV56Vjm6cxYJ69BraDOeyRr1w5CHD2L0n03ATqE_9Nq6GoB2hYw07OuW2zrVrFYoHO9tZLIykXr1gq4OyeITw7aTzUgOa4PWKE-hj-Ya5gG1I_Pr7kp_CBLY8BQoLUEz1QLhVyJPtAYgCGY_QZcamQetvIkA6hib-jqyT6hiR6nfl23TN85l1j5kPML4NS_KFkqLyu5WESu0uVNLqFnVsAx7-p-hvu3DIuvggzELVWS9jE7_IM_coOSfMAW8EARojZ_boWWO5A4eClxKZjZog2jOlfCxdFV0zBmvZDoK98f7bvncHigbs69E3QoSKyDZ5i-hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad76bbcd64.mp4?token=sxKncaH60yl7XRhAcxV56Vjm6cxYJ69BraDOeyRr1w5CHD2L0n03ATqE_9Nq6GoB2hYw07OuW2zrVrFYoHO9tZLIykXr1gq4OyeITw7aTzUgOa4PWKE-hj-Ya5gG1I_Pr7kp_CBLY8BQoLUEz1QLhVyJPtAYgCGY_QZcamQetvIkA6hib-jqyT6hiR6nfl23TN85l1j5kPML4NS_KFkqLyu5WESu0uVNLqFnVsAx7-p-hvu3DIuvggzELVWS9jE7_IM_coOSfMAW8EARojZ_boWWO5A4eClxKZjZog2jOlfCxdFV0zBmvZDoK98f7bvncHigbs69E3QoSKyDZ5i-hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضای مردم پای طومار «ترامپ را بکشید
»
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/448474" target="_blank">📅 00:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448473">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQgzW7SpyW-Wd6BwwUSX6jhimyKb9ShpyIpnOKa2SjBxdgneQlkQ-EMasQ9nIPNo91ImjXBk-I4OWfX5CIQWZJQvXPvFX-cEeRifSb7JgbIX9Sd-AeyppXS2aKhGfkKPLejeGSNxS_e4BXwkwi-mkbEH71s7iUqN17d7vMlMb5LFSJL7GrtxAjEFd0CJ6MDwkh1gZOsQeRj9mz1O17EXO-EKxNur9jdmtDWIqzvqo5j1hJnDCpAqvKrQ3TK9wd_piRzUNk_LiYEEyJ-Z46gjimIMynaHQ7i1PrTDlE2M4UfeUFcX6dswbtHbvHI_Y4rIdec1hoLtL86gekOzMRoK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| پنجشنبه ۱۸ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/448473" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448472">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9198ef1eb4.mp4?token=HpfAyVcff3AWk7hCsu92Ww6NnEkyH4Lsh4gDVGPp6PjHxE3RbG-mOOnfL1bYbFCkivf6xjj7pGoCtTxbWcR0DI3BUxT1PkXJzRsm3WQc1VFQUkXDGEmCfqU3mmtFvSqmqyYIToSxgOyUnxTaWHBvfHSfQqRa79jq9kr8e5Mo0JyyKo9tcMDbwhIFSL_t-ybJAh0BLBifSQKc5YNf5nySzmlK_pla2Xg8NZ-d8qffn0WZ6o7cDMqj5JUBspPQdj4ii67o6pY7BRpsUHdZ56seIq0JAq3OEHEpVYMvKy7_UEVWb3y0VmY8N_l26WxvIzyjKOAHo9Y-UXtaWjmLp3f8Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9198ef1eb4.mp4?token=HpfAyVcff3AWk7hCsu92Ww6NnEkyH4Lsh4gDVGPp6PjHxE3RbG-mOOnfL1bYbFCkivf6xjj7pGoCtTxbWcR0DI3BUxT1PkXJzRsm3WQc1VFQUkXDGEmCfqU3mmtFvSqmqyYIToSxgOyUnxTaWHBvfHSfQqRa79jq9kr8e5Mo0JyyKo9tcMDbwhIFSL_t-ybJAh0BLBifSQKc5YNf5nySzmlK_pla2Xg8NZ-d8qffn0WZ6o7cDMqj5JUBspPQdj4ii67o6pY7BRpsUHdZ56seIq0JAq3OEHEpVYMvKy7_UEVWb3y0VmY8N_l26WxvIzyjKOAHo9Y-UXtaWjmLp3f8Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب در مسیر حرم اباعبدالله(ع)
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/448472" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448471">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayRaA-RCWYaCbhdhiuDmq13YKnyeeJkR8GrRvBEplTaPx023_cUd8zmcAddKJCHhktSvkG-aw3CEJ4mPLNF7dy3Bn0nHZxDKU010ChfiZjEd7CsLgL2cV99dOLV-5yzbag9d1TJ88DWKOzYf4uhW-dyyTe6UnW8CgDn4D_wpjTI0iGEfPol2c_3k7xJURcfJEu-SXuRFKerFQ5DV6fHMpcs4aTwtAtWxaZRhJttLh5Mrfp3fP4fXQQhgmHj9OaUV-BMR6BP-__VjliLO8rSFXbTiYFMURvDDd1jmnOKa2NYqPaqd6zE6QPLs7feWQdas7QRLgn4Tp6vbVreH2T_V2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آمریکا نقض دوباره آتش‌بس با حمله به ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که در واکنش به حملات ادعایی ایران به کشتی‌های تجاری در تنگ هرمز، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است. @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/448471" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448470">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جنوب کشور
🔹
حوالی ساعت ۱۱:۱۵ صدای چند انفجار در بندرعباس و سیریک به گوش رسیده است.
🔹
همچنین صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است.
🔸
شب گذشته هم نیروهای تروریست ارتش آمریکایی به چندین نقطه…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/448470" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448469">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2186adbf.mp4?token=XF-AwmLUwk65EV135XkIsdOuH23r3nElPDo891Sb_pBwY4TYLtofKGxRZiureJX7R4TG-eIvzRqlXJ8TXPrSkPaPhhYYIdfbZ3oFD6KZjv9hRGTcom6LOg43J8E3ugTDu9AT3bxUOKbwAgjtRamM5oYtL1ujCVhpDLMEEAZQVlX0A9xvf06GLKKM79Za9FJFqRTTzMAUqNvwmY51eoMRjkaOrkzHGqPfNRG0trV7ObRQ6wJSteBMw_49Mcm-wPBKOPo6TAb2JnqxteKyVUQWGiJNWIesr0qs0ZHv3gOeQhmiJDTSLFpkeuRO3CrZizMZ-omIy2IOJt6iYMzIOODuZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2186adbf.mp4?token=XF-AwmLUwk65EV135XkIsdOuH23r3nElPDo891Sb_pBwY4TYLtofKGxRZiureJX7R4TG-eIvzRqlXJ8TXPrSkPaPhhYYIdfbZ3oFD6KZjv9hRGTcom6LOg43J8E3ugTDu9AT3bxUOKbwAgjtRamM5oYtL1ujCVhpDLMEEAZQVlX0A9xvf06GLKKM79Za9FJFqRTTzMAUqNvwmY51eoMRjkaOrkzHGqPfNRG0trV7ObRQ6wJSteBMw_49Mcm-wPBKOPo6TAb2JnqxteKyVUQWGiJNWIesr0qs0ZHv3gOeQhmiJDTSLFpkeuRO3CrZizMZ-omIy2IOJt6iYMzIOODuZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تراکم جمعیت در اطراف خودروی حامل پیکر رهبر شهید در نزدیکی حرم امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/448469" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448468">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جنوب کشور
🔹
حوالی ساعت ۱۱:۱۵ صدای چند انفجار در بندرعباس و سیریک به گوش رسیده است.
🔹
همچنین صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است.
🔸
شب گذشته هم نیروهای تروریست ارتش آمریکایی به چندین نقطه…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/448468" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448467">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تغییر ساعت مراسم تشییع رهبر شهید در مشهد
🔹
ستاد تشییع رهبر شهید: با توجه به استقبال کم‌نظیر مردم عراق از پیکر مطهر امام شهید، ورود پیکرهای مطهر به مشهد مقدس با تأخیر همراه شده و از همین رو مراسم فردا در ساعت ۱۴ برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/448467" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448466">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جنوب کشور
🔹
حوالی ساعت ۱۱:۱۵ صدای چند انفجار در بندرعباس و سیریک به گوش رسیده است.
🔹
همچنین صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است.
🔸
شب گذشته هم نیروهای تروریست ارتش آمریکایی به چندین نقطه در استان‌های جنوبی حمله کردند که با پاسخ نیروهای مسلح ایران مواجه شدند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/448466" target="_blank">📅 23:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448465">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee8e83406.mp4?token=ko3e1AjAQszDUrF-vOOfuUksyDXhqZeu4a2EdqE4DBxOzbvk4dasAkaRWBWn32Q4YR0aZ0rTaBbALHl-LPt0Bn6m1ZhIWaoaw8VCg4-1SxvDmmVf0lYG_PmNIMNNASnoVtKk3fGA4CtgOCqSUKdSn2KtVWONax_UdJp5jRhraPGqNDpNSeLaQG0aVHypkD1OjyHg3lpCZjfivWic-FpjBFCtfU26LrlVxDBU7sz442nXz-dw_rhs0HuqDUm0G72HlGJGgJ4kv9FdQsm9MtavKaqdMKgF14JpGpbQFypkcIcU6tlr-imGf_eBxodqSyixN17xt_84BiC9Nrn9LGj3aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee8e83406.mp4?token=ko3e1AjAQszDUrF-vOOfuUksyDXhqZeu4a2EdqE4DBxOzbvk4dasAkaRWBWn32Q4YR0aZ0rTaBbALHl-LPt0Bn6m1ZhIWaoaw8VCg4-1SxvDmmVf0lYG_PmNIMNNASnoVtKk3fGA4CtgOCqSUKdSn2KtVWONax_UdJp5jRhraPGqNDpNSeLaQG0aVHypkD1OjyHg3lpCZjfivWic-FpjBFCtfU26LrlVxDBU7sz442nXz-dw_rhs0HuqDUm0G72HlGJGgJ4kv9FdQsm9MtavKaqdMKgF14JpGpbQFypkcIcU6tlr-imGf_eBxodqSyixN17xt_84BiC9Nrn9LGj3aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از حرکت پیکر مطهر رهبر شهید به سمت حرم امام حسین(ع) در میان انبوه جمعیت
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/448465" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448464">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de0aadf74.mp4?token=NjF1OHBiQosc8wLxH0GKSSVxioXCgdKfSjOyAhVViHRNGArSsVr1hBHqU_dR04xM4tVlcNOLbwEG2pC7r4ZHd1GUgIcs0VPPpCC98gD8fJyFcRTHk_x5ldmg0fq9feQA_q1lLbFjY-sT2ih9RK991KZ0fDrg4uEHcitqB-KQu0wGeroBESBAvGZ2PXTpLsMUBQkBAK95PX1AHG7RFbwG25KevmharbbyAyF869BNDUb1Ko71d4glAu-TXlXH3g1dyafxgUqSEUgDgT6viVDUl8d-UrcJKM-7ht22lyuE8hQDaFhAH_TRDkSCxyNJkcNF8yl5BXEPsOK8WHEszVrImw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de0aadf74.mp4?token=NjF1OHBiQosc8wLxH0GKSSVxioXCgdKfSjOyAhVViHRNGArSsVr1hBHqU_dR04xM4tVlcNOLbwEG2pC7r4ZHd1GUgIcs0VPPpCC98gD8fJyFcRTHk_x5ldmg0fq9feQA_q1lLbFjY-sT2ih9RK991KZ0fDrg4uEHcitqB-KQu0wGeroBESBAvGZ2PXTpLsMUBQkBAK95PX1AHG7RFbwG25KevmharbbyAyF869BNDUb1Ko71d4glAu-TXlXH3g1dyafxgUqSEUgDgT6viVDUl8d-UrcJKM-7ht22lyuE8hQDaFhAH_TRDkSCxyNJkcNF8yl5BXEPsOK8WHEszVrImw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر رهبر معظم انقلاب بر فراز دستان مردم عراق در استقبال از پیکر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/448464" target="_blank">📅 23:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448463">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiQweoxCSBEWOOLqlj7yHuHomIxFcseUsE_5eaKXhmYFrHok78mrimRIzRH4E7emLoSlrrYsOgUVTUFhXvLulnL7vsiXfoT5_cglnFmzx97P4Q8b3Z-lQPI6p34qtYqWbn6dDKzkHMiiVYMbwgm09XF7WTWyrZt0OAsq_Tzfi5QZU_ggYheH4E5tBOoIi8LiWm12O4Y5l3Yb-qzBrx7P6lidufAr8FmKQ-5IBBeg1sy_suXktUSIg0UfPS3s8juLvZo03egW-0uLUIzeH_KsXs0t3dmF2yUkddx8uUA5x1oaXIlSAB5kLkYHJKshSDNFgXN4EW-51NbunkkypV5JbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: تشییع امام شهید آیت‌الله خامنه‌ای قیامی الهی است
🔹
شیخ نعیم قاسم: ما امروز به مناسبت تشییع پیکر امام مستضعفین گرد هم آمده‌ایم؛ باید برای خدا برخاست که این تشییع، خود یک قیام، یک حرکت و یک انقلاب است.
🔹
امام خامنه‌ای یگانه عصر خود و رهبری استثنایی در دوران معاصر بود که نظیرش در تاریخ کم‌مانند است، ایشان ولی‌امرِ امت و نایب امام غائبِ معصوم، امام مهدی (عج) و بنیان‌گذارِ پایه و اساس تمدن اسلامی معاصر بوده است.
🔹
امام خامنه‌ای مرشد، حامی و مربی بود؛ رهبری که در دریای جمعیت، مردم را به سوی رهایی از بت‌های مادی‌گرایی هدایت می‌کرد.
🔹
ایشان سیاستمداری کارکشته بود که ابعاد امور را در سطح جهان درک می‌کرد؛ او مردی بود که با شجاعت، عزم، عزت، اعتماد به نفس و توکل بر خداوند متعال، استوار ایستاد.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448463" target="_blank">📅 23:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448462">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi72nmew1ZUN0ZgkmHAljN8AJ2Vmq4Qh4z2s65jF0lbOnsQ0ibFhYgU4b_nS_lmWYE1to602SHow5VJvvzSn1NKxnXWllB55A69JQsbC69Y2kGS2s01Z0NcCuUlWH0JeTCytrG5ay2slAcpeouyxvFilqCGSeQplT3DCv6qSuBmyTTbqCgIYXkL5r-ckyddYn9CfZ6pW_fgqz2CG3XoLN0UiYiGLI97lzoqcojs1DztVmyGtNDvgVsWWHh-IKu8SaD1PHeDDsqoqEVs-Wi8rpxfx-SZqtG3-KqQwVgF2Gd85afqCApOaPvRbrAGqJzfg3uIpU0y6EtxI6hklPIqpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
زائر اِرباً اِرباًی امام حسین(ع)
🔹
دست‌نوشته زائر عراقی برای رهبر شهید: از فضیلت کسی که پیاده به زیارت امام حسین(ع) می‌آید شنیده‌ایم؛ پس حالا فضیلت کسی که اِرباً اِرباً به زیارت او می‌آید چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448462" target="_blank">📅 23:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448461">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
فریاد خون‌خواهی بروجردی‌ها در ۱۳۰ اجتماع مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448461" target="_blank">📅 23:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4f9ee59.mp4?token=cvh3eK-b5nczfk-nrO3rKVn0bNBOEPNjTO6Xlu3uFYsixM_J3ae7Gec5jVrEsqvGAVRXMPGZ1bXKEE54jGqO7LqG47GBBS94PWV5waJz1oJ5ymcDu9CK2ZpB96aqiPZVEX3QI4Q_0qnXhBxRSDvjtvjT6XGqMw7gldh94tWVARQr12D7GjXJAuEM-TNhn8glbH2sne13TKU-qJmP9lfqDbhtbtmApEp1BFb8Z9B2P9n4tS0GV8jGlVd_TaLNWFHy_kp_3ud7KnXz415fY41C5uFz1P1Xf9r4J9_y0-Gt2fOQUWoEiWaCJAfxvCxET0EZXNGd2HE0yhZxh6___hIUew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4f9ee59.mp4?token=cvh3eK-b5nczfk-nrO3rKVn0bNBOEPNjTO6Xlu3uFYsixM_J3ae7Gec5jVrEsqvGAVRXMPGZ1bXKEE54jGqO7LqG47GBBS94PWV5waJz1oJ5ymcDu9CK2ZpB96aqiPZVEX3QI4Q_0qnXhBxRSDvjtvjT6XGqMw7gldh94tWVARQr12D7GjXJAuEM-TNhn8glbH2sne13TKU-qJmP9lfqDbhtbtmApEp1BFb8Z9B2P9n4tS0GV8jGlVd_TaLNWFHy_kp_3ud7KnXz415fY41C5uFz1P1Xf9r4J9_y0-Gt2fOQUWoEiWaCJAfxvCxET0EZXNGd2HE0yhZxh6___hIUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب به عمود ۱۳۲۵ رسید
🔹
کمتر از ۱۳۰ عمود دیگر تا رسیدن پیکر رهبر شهید انقلاب به پایان مسیر مشایه و قرارگرفتن پیکر پاک ایشان در برابر گنبد و بارگاه حضرت ابالفضل العباس(ع) فاصله وجود دارد. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/448460" target="_blank">📅 23:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jzd5Ru9G5aLnOblS5nGm4Qv2DJrFZbVxJSP8LDwapNQqc1Rzp_y7KFLkx0W6Ene20nTa1vBRE3Vt2rbEQK1jLkHzNVi2jXhKXLMA7W6TvcLbqmVIxLrodwaFILXbpsg3IHJ4YtvqsD0V_IFvkbl2u9alXl6wHC6UWfjATJbsBvVO_q2DL2_vAt67NFYtwPxmb2EKIGF0yXbwfN8GrspZBePqbKHnuO71ZCH_q-jJNswMoM1ASpmYFgRMJsEdiu0wjehT_oTbBnaAWc6f6qHWDaIKaLF5OhVrrr9RnRt9Htdi_nIudZfxo2han_WoGl-9tz65l2md-uOY3rR8VZptyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLNxoxiqWZIlAP0epC5inoOPwVmm-JWYoqI_Ti1wNEbnVWhwRyjOkr9f9uFeIcTc8IUBuOIGFc_bzUR14oFdJdp1fXZ27q2u9m8XP5sr64sYkXg-ccZ1k7NGQf1YkeQ1SdBxKt4Lfm7w1Ep9G6yX4gQBan00iSpnwEP9HF2p0a_KISkOWAvRSgjzmhSPhFN7EOuGZTtNc_5BDMfA1DBZb_Nxv_cD1zX2OHd7StjpXyPrmD0ZtTv_VctuRIkkcWaEIZBq1RnNTIEIoSG3WXAZW1Mgkzdn-jxaIHlbAIItXe17vxasbNl3ub19Kbac2OkJkUS_Wa6rRs_oKrhYjv3ztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdEjnRjQWQjSEoS65jhW768fl4_6Yd-6sbOiDSiIzEzdkujvDRCCOZLnrMpQFeCO40-VX__unoMUot-rpr3cd_WQFvaiWMdQw6o1vOQ0VXmUKO3s9sPlbFnPWG5rtT4p0Xh9uaxYtgJpTPCLZB77E9HDVvmHI9EATmiRZhCQQiXTXCS3XFciXMDQOyaJ3Als-2sDzpaZsXiPRbYFqhzFJUq9RRzl666813XMDDtxgCrjfb_45DJ0gCa8yEBjkmExE7i5-U9pf4i3QCX43C9f1zCYL403YuBiXYCPa26bkJDitmkgORcDgqgBDdNwtM0NObV3hhnF26NUwkjwkVHX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZUDghAmfsEI7FOE3rcFnLI5A6S-eh93J3Y9DXTAPsg7cCAsxAxaVPfK7_Fn3jkGvJsrUdmRtOIQooyWIVkL7Zrva-5pOfAxL09pbmfwX9nW00KSw54MVIeyXhqrGSRYyIMg0E6q2Y2KfQ6jhFtSTWudqFP6s9vnaQVlLB6lafko7i2Hh8mugcjpqipDvtEFr2QmPY-A6hJW7D7D8FYbfXnJzQxoNImzDFr09AVSDMGUP_w_zkHXtAOXzFbi4SsRxF46ni1EBZdTVlmOg8H7BnOgGoct9h_QUG6QPPA2O_2YYrTlphuwLO8tHfL1osuR3pdpomO2yAV_EDg1NtbZKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تشییع رهبر شهید انقلاب در کربلای معلی
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448456" target="_blank">📅 23:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448455">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008000a807.mp4?token=fWRy8Oo0A78YBPEI9zxK91UqK-eXY0Socw4ECfM-rvb6bDkLOEQ8-dRdTd4zkVU5AM-UrGhPvF_Vf0FZ_RuMVLylHdcyG6-nbGJxm-xSE5yrIvCzGP3Z4_uLAQLErwGv1VzJE9tHKHoVBb-PIqmBDrzHWXjLM160QjqlOTJsE6IuY_IvBzW4eUk5mhLB9E3Km-yVWVSMCf5wj2h4-8_ZxBcPKcMVWWsqC4n4HErLbhnAUGbNpgDk7sKC6MLX_y8RMZsxv23nK-FqvVDg_tGiegwDriIp6tS_95iN-mqj6NpwvYwG1enJYtvTMOt84DLpYfJShwrRBkpVUGL6eBjbYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008000a807.mp4?token=fWRy8Oo0A78YBPEI9zxK91UqK-eXY0Socw4ECfM-rvb6bDkLOEQ8-dRdTd4zkVU5AM-UrGhPvF_Vf0FZ_RuMVLylHdcyG6-nbGJxm-xSE5yrIvCzGP3Z4_uLAQLErwGv1VzJE9tHKHoVBb-PIqmBDrzHWXjLM160QjqlOTJsE6IuY_IvBzW4eUk5mhLB9E3Km-yVWVSMCf5wj2h4-8_ZxBcPKcMVWWsqC4n4HErLbhnAUGbNpgDk7sKC6MLX_y8RMZsxv23nK-FqvVDg_tGiegwDriIp6tS_95iN-mqj6NpwvYwG1enJYtvTMOt84DLpYfJShwrRBkpVUGL6eBjbYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خونخواهی ۱۳۰ شب در گرگان برافراشته است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448455" target="_blank">📅 23:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448454">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12a187cbb.mp4?token=KBvNSCKeT6LoRng3LQW9nHxgIAVoP6rt2h5XINuTMxIXUzlREWNbMmuJ12KH1ueFV9hnkUTzTCkdzeaaSE0RIyK2itjgQY_bX4nkjuQOKcCPUrV-aWYPBzJmqHDyyCA9LefGfAFPw6J0EneiqFfQxUC_f0J1oYsa-ewTFcmzqJfh447VG7jPuG2_P21ZfnZxkvAxD3HuDRch2gT_-uAr3bf0FC6KFZ5MzLGzkpkxWB1li2yGCJuvolpBBXlRtPBfv98jeu1Pvp24gossMHcJubAs57mzZJmwuyRhAUsLL98W7lIIlYsZOqSIWbZ8dW1jAS_gSywunVssj5by9Jvkyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12a187cbb.mp4?token=KBvNSCKeT6LoRng3LQW9nHxgIAVoP6rt2h5XINuTMxIXUzlREWNbMmuJ12KH1ueFV9hnkUTzTCkdzeaaSE0RIyK2itjgQY_bX4nkjuQOKcCPUrV-aWYPBzJmqHDyyCA9LefGfAFPw6J0EneiqFfQxUC_f0J1oYsa-ewTFcmzqJfh447VG7jPuG2_P21ZfnZxkvAxD3HuDRch2gT_-uAr3bf0FC6KFZ5MzLGzkpkxWB1li2yGCJuvolpBBXlRtPBfv98jeu1Pvp24gossMHcJubAs57mzZJmwuyRhAUsLL98W7lIIlYsZOqSIWbZ8dW1jAS_gSywunVssj5by9Jvkyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ از ایستادگی مردم ایران به جنون رسیده است
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448454" target="_blank">📅 23:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448453">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2607292543.mp4?token=ckYWgMe4tO0wz41yX-lRfWj__5rrJXAInp_nD9bXXafU63PSyU8gXMD2xVZZW2I4FCdRt7OBFlAEhN9woweAT2rMeL3DjrA34uf5bToto-PtGTyfnQSyW13L21ynjPPwt1syW3UMvLh5JRR8VlCcGBcWHTSz4qCCSkua7-87juzYPRFEdvzTtdoYhFncNm9nOAr8SYfHMz7YTBlK84fyavwdYOCwmnpSQd-UhQgsf2JeWgiBF9ubBteyUqq3iu-APxKzJVPxDDgu8SdyA7nyQiVd1rZMA5_3ZKrL9OZawcoXqtUf1ohv9HwiQszpvlvhKkC7BOlo2sQNOMt6vhVumnVxceMraAUE1X8FKvK957Q0HtGvlO5_og-QaegpxwvOhCdgH7eDOBU_Kzvi7vg8CCqzoHlPG5w1g4qxCqGwYio9S0HKeGBdnJq-43mziMJz4jXOZ7o4Ps1RwCstO8wv76V4ogFXhkGNP-rzlEiAvwgyHm-QoZfwGzQMgJndPnKfm6oIadQa2nA6b6z-ATy0VXXbkKGD2_3-1Em73FHBhzok0g5PqYJULgbjhg8pjLDl-8p48skA0mdlR3zb4gpldrLZVa0x3iEhQ7iNNNRk6PmQOjmmqJZoJsO_lNEU5lcPrSrOeqtu3KeSSZEVegqjVgEjxV-QaJbppPufwoxtOK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2607292543.mp4?token=ckYWgMe4tO0wz41yX-lRfWj__5rrJXAInp_nD9bXXafU63PSyU8gXMD2xVZZW2I4FCdRt7OBFlAEhN9woweAT2rMeL3DjrA34uf5bToto-PtGTyfnQSyW13L21ynjPPwt1syW3UMvLh5JRR8VlCcGBcWHTSz4qCCSkua7-87juzYPRFEdvzTtdoYhFncNm9nOAr8SYfHMz7YTBlK84fyavwdYOCwmnpSQd-UhQgsf2JeWgiBF9ubBteyUqq3iu-APxKzJVPxDDgu8SdyA7nyQiVd1rZMA5_3ZKrL9OZawcoXqtUf1ohv9HwiQszpvlvhKkC7BOlo2sQNOMt6vhVumnVxceMraAUE1X8FKvK957Q0HtGvlO5_og-QaegpxwvOhCdgH7eDOBU_Kzvi7vg8CCqzoHlPG5w1g4qxCqGwYio9S0HKeGBdnJq-43mziMJz4jXOZ7o4Ps1RwCstO8wv76V4ogFXhkGNP-rzlEiAvwgyHm-QoZfwGzQMgJndPnKfm6oIadQa2nA6b6z-ATy0VXXbkKGD2_3-1Em73FHBhzok0g5PqYJULgbjhg8pjLDl-8p48skA0mdlR3zb4gpldrLZVa0x3iEhQ7iNNNRk6PmQOjmmqJZoJsO_lNEU5lcPrSrOeqtu3KeSSZEVegqjVgEjxV-QaJbppPufwoxtOK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق پیکر رهبر شهید را گلباران کردند
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448453" target="_blank">📅 22:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448452">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7afb780c08.mp4?token=H6DDGuGflWfxDaKre8c1vEE_kk4bfHrXX6Pji1z2MPgodvQ6eJypJdpddAEkWtI1P38fGIl_szfni0cz7JjqWRTeYu4hlBmLXck9tWUod21_ghbwrtjrHA9avZX_dhAl6rQsdolJmAj9jokc2lPHYQxnD7evx00TwRW-sgKcVGWbxyFe9zr8P1jCpZUV9veFsJ58xLD_0m72LbPK5u2gkGovJoU0CYVB1-WlMXqOzAPthm0eUPJhy7rzFaT2I0bmfR_9LzwdwKV0ZItbXO5y5m2HP2xXm_jHdG2XxSzzMby6abHGejuWzcvjs9i51VkP1XHBCViOmQq-BJSeWfbZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7afb780c08.mp4?token=H6DDGuGflWfxDaKre8c1vEE_kk4bfHrXX6Pji1z2MPgodvQ6eJypJdpddAEkWtI1P38fGIl_szfni0cz7JjqWRTeYu4hlBmLXck9tWUod21_ghbwrtjrHA9avZX_dhAl6rQsdolJmAj9jokc2lPHYQxnD7evx00TwRW-sgKcVGWbxyFe9zr8P1jCpZUV9veFsJ58xLD_0m72LbPK5u2gkGovJoU0CYVB1-WlMXqOzAPthm0eUPJhy7rzFaT2I0bmfR_9LzwdwKV0ZItbXO5y5m2HP2xXm_jHdG2XxSzzMby6abHGejuWzcvjs9i51VkP1XHBCViOmQq-BJSeWfbZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشق و علاقۀ عجیب جوان سرباز به رهبر شهید: ساعت‌ها کنار جاده ایستاده‌ام تا شاید حداقل ماشین حمل پیکر رهبر شهید را ببینم!
🔹
تابه‌حال نتوانستم ایشان را ببینم.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448452" target="_blank">📅 22:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448451">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کربلا پنج‌شنبه تعطیل شد
🔸
کربلا به دلیل ادامهٔ حضور جمعیت‌های میلیونی برای شرکت در مراسم استقبال و تشییع پیکر رهبر شهید، فعالیت اداری در این استان را برای فردا تعطیل اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448451" target="_blank">📅 22:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/468085ec2d.mp4?token=e7FiObVHAnK8lbze4YTEv3Af52hcoNlJwoRqmyCiVJGDWxRyO5arD9clpI0ajAJ4UZO5xAXpsnjZeBylOsXZBHJVIqIch8cfB6QE1_q4b-NYFoG63QeKF2dmvDQh0pa2rFN6jQoBqWg6oS1xr3yl7nsA8fOPeFzzLe5ESi9zV3Tgd2me0QRsEb6k1ipG7cHOYVnz64I3PJz7-_fSupo3uiTaXPDZ2mnB2YQP8-XTCmdG6_wg8Uny7pvaT8y56ivc2wl0ttAwWU2mNBVM0fCYRe8QjTOby-u7M8oY7f0246mGf8kFPsZfN9O3wSuQzc7phSS4nvFU94cKjWJxzzVPrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/468085ec2d.mp4?token=e7FiObVHAnK8lbze4YTEv3Af52hcoNlJwoRqmyCiVJGDWxRyO5arD9clpI0ajAJ4UZO5xAXpsnjZeBylOsXZBHJVIqIch8cfB6QE1_q4b-NYFoG63QeKF2dmvDQh0pa2rFN6jQoBqWg6oS1xr3yl7nsA8fOPeFzzLe5ESi9zV3Tgd2me0QRsEb6k1ipG7cHOYVnz64I3PJz7-_fSupo3uiTaXPDZ2mnB2YQP8-XTCmdG6_wg8Uny7pvaT8y56ivc2wl0ttAwWU2mNBVM0fCYRe8QjTOby-u7M8oY7f0246mGf8kFPsZfN9O3wSuQzc7phSS4nvFU94cKjWJxzzVPrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌چه در تشییع رهبر شهید رخ داد، در قاب رسانه‌های ضدایرانی جا نشد
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448450" target="_blank">📅 22:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20b5cebaef.mp4?token=pIkvDlNw5TEKs80yWoa6sEc98OYuhnTGbVPWxWABmxo97ZaOmf4dWFvT0EBMqYcWt5fMrFXMi98SHd14lD_bAjQi4bc03SQ0WTYjZcFdqzO4bWqQbAFS9O3zahGdPWL8dywrv-w9w-Wm-FqaVmLos2SBppbtlAYCnzQ95jsF7Ej3z90jNQMrA6haNzNDGdufCYWtZSOq3HnG09KUg1Hjmkqcls_WB6JlWYjUhqONh9gLYwTGLNTAVvMatniv_M8ihPwSnv-eRdw5TNPk_6aWceI4zHsKWU73EWdm8yzXF8AFDUkJ5wRHTMJnOi3o4VzGDTpLlXkUHJ5pI4yB9r8yhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20b5cebaef.mp4?token=pIkvDlNw5TEKs80yWoa6sEc98OYuhnTGbVPWxWABmxo97ZaOmf4dWFvT0EBMqYcWt5fMrFXMi98SHd14lD_bAjQi4bc03SQ0WTYjZcFdqzO4bWqQbAFS9O3zahGdPWL8dywrv-w9w-Wm-FqaVmLos2SBppbtlAYCnzQ95jsF7Ej3z90jNQMrA6haNzNDGdufCYWtZSOq3HnG09KUg1Hjmkqcls_WB6JlWYjUhqONh9gLYwTGLNTAVvMatniv_M8ihPwSnv-eRdw5TNPk_6aWceI4zHsKWU73EWdm8yzXF8AFDUkJ5wRHTMJnOi3o4VzGDTpLlXkUHJ5pI4yB9r8yhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درسی که شب گذشته به آمریکای کودک‌کش دادیم
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448449" target="_blank">📅 22:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5m2xwtPtyQDTD0zl6z7Mb8m3h3iDLBNjrfK8qBKje8LqGd8dhlaveHOMSF19eDnJmICo67vhAgFVO6pvfmWVo5coWtqReLkaOyZIYS0kfzIdIkTNDlEN_fTp8CE9NNxWR2dKQIwd2N4dfr6aAxLgqbo4tj6EB5QTA58kqv6MSdjqdFqztepJZgcQ9240-sbNX62-0dd_Lrbd-4vhSzSI9ydgSSgZM94esQvN9eLWQUiVuXfevdkKWtPuresuwnEnJ6Zy-ZxRKedi7CQuz6j7SNzoz2WoXvfj8oMSc-1vRx15fmbDyAyllG9jQKJBrNrVv7lLQ0uBZI3LBbEUzCZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دستخط عاشقانهٔ رهبر شهید انقلاب در وصف امام حسین (ع
)
بسم الله الرّحمن الرّحیم
این حسین کیست که عالم همه دیوانه‌ى اوست‌
این چه شمعی است که جانها همه پروانه‌ى اوست‌
🔹
اى شعلۀ فروزان، اى فروغ تابان، اى گرمابخش دل‌هاى خلایق!
تو کیستى با این شکوه و جلال، با این شیرینى و دلنشینى، با این هیبت و اقتدار، با این‌همه لشکر دل‌به‌همراه، با غلغله‌ى فرشتگان که در کنار موکب تو با آدمیان رقابت میکنند؟ تو کیستى اى نور خدا، اى نداى حقیقت، اى فرقان، و اى سفینةالنجاة؟ چه کرده‌‌اى در راه خدایت که پاداش آن خدائى‌شدنِ هر آن چیزى است که به تو نسبت میرساند؟
🔹
بنفسى انت، بروحى انت، بِمُهجَةِ قلبى انت، و سلام الله علیکَ یومَ وُلِدتَ و یوم اُستُشهِدتَ مظلوماً و یوم تُبعَثُ فاخِراً و مَفخَراً.
۹۳/۲/۲۹
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448448" target="_blank">📅 22:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a329c47e75.mp4?token=tzCp2nGsWTNADhy-HKfc90BIw5fpTv70zyBQ2eOeiGKjwG7SWRfgiGi0YP8881CWtZW_LGKa89sg-9UBbjZtwfsZWnhCKeQn4YCEKP4hz1sN36O5__eSgSI4giB-5VuckuIVSRqtfilqnSq5Efd7kJdGKOqYfg9k5dQP7w-Ka4u5lWT_G0U88r2i-hsCKUkzvVIM3DA4l4IIfag_V70-tXER78k22FlFWM8gDPnp1bbDSRL-qi8Qky4dhYx7f1xc2rP5ZqJUD7LKykNkyBvKHLQdTm3rk52dnbkpgfQp7-imZIGOwI4k086piz34rxzmVZ-U-dWF69eyuhUMiDvs0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a329c47e75.mp4?token=tzCp2nGsWTNADhy-HKfc90BIw5fpTv70zyBQ2eOeiGKjwG7SWRfgiGi0YP8881CWtZW_LGKa89sg-9UBbjZtwfsZWnhCKeQn4YCEKP4hz1sN36O5__eSgSI4giB-5VuckuIVSRqtfilqnSq5Efd7kJdGKOqYfg9k5dQP7w-Ka4u5lWT_G0U88r2i-hsCKUkzvVIM3DA4l4IIfag_V70-tXER78k22FlFWM8gDPnp1bbDSRL-qi8Qky4dhYx7f1xc2rP5ZqJUD7LKykNkyBvKHLQdTm3rk52dnbkpgfQp7-imZIGOwI4k086piz34rxzmVZ-U-dWF69eyuhUMiDvs0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کربلا صحنۀ وداع عاشقان با رهبر شهید شیعیان جهان شد
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448447" target="_blank">📅 22:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_UyClSnFG2bTBZ16p-RErsX8FuNHCzPbc4YlyAwGM23CYQb-E07WQO3po2Vdjt-u5s5G2rzv5ksW00WqhtziLiyrcHmqRIKgoEADZ_tMhfhWhveJkX71T08EO92y_TiT8ysA7IFOToZAvBdM78Y285BVivghTeR_C5ugY0O43570uHU0OAgzNwbA3CtiRodempO_Mpub3NVWpnfVnPpBO9NkaHYQ7gIVwUOmZdKTUuWdC6qbFV5nY-06WHrqA6it4IMcHbM0l8KjY576YoUaacaNP15PD5vIc3EkkMLxGVFRKc4b5zEHoEE6rlJfVhT_V2VCBozeTfeETNv1GE7jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: فاصلهٔ ایران با سلاح هسته‌ای، اراده است نه فناوری
🔹
مدیرمسئول روزنامۀ کیهان در پاسخ به سوالی دربارۀ توصیه عده‌ای پیرامون تغییر دکترین هسته‌ای ایران، به فارس گفت: جمهوری اسلامی از دانش و توان فنی ساخت سلاح هسته‌ای برخوردار است و فاصله ایران با تولید…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448446" target="_blank">📅 22:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ab5a8965.mp4?token=bVwgq6SB4heT-MFy7uCIv3HJ4lTFHVFdd5ElDJhoP0UVDPkj66ymJrp7RiVF6wFEFyRUVP_TiDSTm88wJyT3ba8B9xAz--CkEZd1-G1BQVtWONDenFftOwdudSYlgW0TJVisEL6MytJNINMmBEv6T2ue-c1ejxUOehyf7JQr9rjYwpr_RQrgLWtXz6bJ1ewdzia-a2DkoQKU7p2RFPtgH_Yc2qyRjL7Afu33AQSstZil6S8Bk16zg4fJ5FsS8GDyvSEAwU2N48DzpRROm0TRNIk_lyt4rhsNNdsDZKo5uqgTKv0UehXapLPo0oabfMC2-xwkq0eN7qAgeYiCgqvdPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ab5a8965.mp4?token=bVwgq6SB4heT-MFy7uCIv3HJ4lTFHVFdd5ElDJhoP0UVDPkj66ymJrp7RiVF6wFEFyRUVP_TiDSTm88wJyT3ba8B9xAz--CkEZd1-G1BQVtWONDenFftOwdudSYlgW0TJVisEL6MytJNINMmBEv6T2ue-c1ejxUOehyf7JQr9rjYwpr_RQrgLWtXz6bJ1ewdzia-a2DkoQKU7p2RFPtgH_Yc2qyRjL7Afu33AQSstZil6S8Bk16zg4fJ5FsS8GDyvSEAwU2N48DzpRROm0TRNIk_lyt4rhsNNdsDZKo5uqgTKv0UehXapLPo0oabfMC2-xwkq0eN7qAgeYiCgqvdPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزوی ۳ ماه پیش از شهادت رهبر شهید انقلاب اسلامی که اکنون برآورده شد...
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448445" target="_blank">📅 22:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4066b49a.mp4?token=pfSWkWsQaTx7POFC9C3gXjJhOaIZWNG-Ph13TaBsR3Zz9l0-r2kGqi-B6pSXVy3drnEYTKOc7Hy42dw7GschioDdhux_4pMeFuvQiJHHxK7DWdncYqn3Wv_e8zWNrWJzfieS1JEo0bHPCwzkMvpVOc7CTVeCQtrapogEoPAMXa42ILMyCygotFHYjIZ6RSjEmlpehHK9jLD1C4J6tzPHhlYMPffTCHgtnAFFj6stiG0kpMjT-o5OdBz0Bm0EhO2LCkrjViWpwvc4hCWsC7p7m7naKxs3RO4Ib-8F6VVY6pPJKIzRbh8tvBtq6kjfH2MA-P1jHYAgxUta7HCaSA0lY6kDFj8ZPPjGgHO0ZfTuoBPEdRmpV-9H97ix2aKtKzEW3kJuK6n55iXnneWM6Yp3s6ulTCrWNqqVwFjcRFdrHv1WgrfTVoJE7ASUntMgsaJjucdZAWd24LP8hNxaqkQEHsA0_zH5TKNrg6AXIel4agWNHpuR2vVfJ3kQT7W437-B-mRxCw_5DTm19hnHUklr3u03hhMdnhIs7MLrmI6NXsfYIb7pG4pp2Iav85oP2LDB2NGD6lTMapZnVxZ1UQthQotCqXuyQoor_zQpeCRL5CM2ZBezyElMWlMq6SmkTNlPkuDQb9i7Ea_A9V78x2t1gRCc_NY4eca3-hgnfolUo38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4066b49a.mp4?token=pfSWkWsQaTx7POFC9C3gXjJhOaIZWNG-Ph13TaBsR3Zz9l0-r2kGqi-B6pSXVy3drnEYTKOc7Hy42dw7GschioDdhux_4pMeFuvQiJHHxK7DWdncYqn3Wv_e8zWNrWJzfieS1JEo0bHPCwzkMvpVOc7CTVeCQtrapogEoPAMXa42ILMyCygotFHYjIZ6RSjEmlpehHK9jLD1C4J6tzPHhlYMPffTCHgtnAFFj6stiG0kpMjT-o5OdBz0Bm0EhO2LCkrjViWpwvc4hCWsC7p7m7naKxs3RO4Ib-8F6VVY6pPJKIzRbh8tvBtq6kjfH2MA-P1jHYAgxUta7HCaSA0lY6kDFj8ZPPjGgHO0ZfTuoBPEdRmpV-9H97ix2aKtKzEW3kJuK6n55iXnneWM6Yp3s6ulTCrWNqqVwFjcRFdrHv1WgrfTVoJE7ASUntMgsaJjucdZAWd24LP8hNxaqkQEHsA0_zH5TKNrg6AXIel4agWNHpuR2vVfJ3kQT7W437-B-mRxCw_5DTm19hnHUklr3u03hhMdnhIs7MLrmI6NXsfYIb7pG4pp2Iav85oP2LDB2NGD6lTMapZnVxZ1UQthQotCqXuyQoor_zQpeCRL5CM2ZBezyElMWlMq6SmkTNlPkuDQb9i7Ea_A9V78x2t1gRCc_NY4eca3-hgnfolUo38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از مراسم حزب‌الله برای رهبر شهید انقلاب در ضاحیه بیروت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448444" target="_blank">📅 22:31 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
