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
<img src="https://cdn4.telesco.pe/file/oO-Io2zz8vx2YQ3OGKIx_zt-LEDfmTadNxBwh_mhw_v0TjrF3JLb7wFBAFxQ1g4pSIvzY4G2caYkNEc_aXuRM-t-Gyw8tDpLER34bkp8pPhhbayimLRqrNrzg61ShwaWl4GFPyQqgE9yg0o-Q3k5MKdHOW3EP0sOJTynjpxj6YXeJmuoFdoIowAei8_4FD-5YydbLauPkqDLmTY_9Np3J7KY1Ad_MNQQudNyKhI3eDzJFkGtn1ATnTENWl-sv9Oc4MdTIcNsaKR0dqMpF6irl_SFPblooVZrA3iFfx_lYQIWsKLFX60RebdvVUa-ufPbwo-UuG1C9yqnmAP--A3YqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 17:36:18</div>
<hr>

<div class="tg-post" id="msg-80953">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqOl-US87Abm8duuql7z1LH7u9Uvd-lSvewVU355zMo4DUVJYfcr5WFCxfSTruC9EkGnilfOnwYg6pyJyDx9kV-qKEkvVTC0ydIfD-15PS_1eLYW7BNcwpAnV56LQ97eiutxKqw8dk0RAfZp1n3O3Cx2Sz56b7f894zGfMQT6sArxccioXAzGU0ZZzZBTLjdZKzUSjIhNqPLUbY8pwskf11kCgh9uC5TXu2tTjkle5qi6hFdPSF0ivBz8eXIl-x37sSkYJ3M36B5DP_kY2rx9Ko0U2F-pBflT1SeoO_oDbezMk49HFOoKqpc5ZUAJFfUr5i2opLXZpcRxEwW_JSd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
في غضون ساعات قليلة، أغلق الحرس الثوري الإيراني الممر الملاحي المدعوم من الولايات المتحدة تماماً، لا تعبر أي سفينة تجارية المياه العمانية لعبور المضيق.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/naya_foriraq/80953" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80952">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721fa47854.mp4?token=Jz77bC5kckI_7V5kQzrkcJd_T8leyHVVXCpfeAcMeeCWAeqVzfSUqPnjJaIo5il2eK4BVlSHbIqdVSSQWa5A06VivpQ36g-NsXJ_gshBbxt_L7SC0owg-ekiuhimTXHTjxuUizwyVF3wXMevW5ZXfxq4pFTOjeTlbXiW94ItnnnUp5FNJXLWnGVmhoZWckQS_IP8X_wJOTHkrgdEmGpfJkRfOP5bI1eITshuc0dR4iSObPOVuv0RTlmw4c44HbH6TRM92jyRXEsRodYakerLfjSPLR6w55sIuN0i0qq45tHwsQ8cVOlmSuR3xZmk-7qgQlnF15D8K3QGZXkD5n99tJxIhgHRVM8z0rBGofpgMTd9YhxU-dv2cVrJtOS0j-IBMiQkNH5ZJ9G7tVlCnmSd6BZt3MMd6hfq3bR9FdBPh95Qb6QiDh_q6QsgeVg78ArrJ3AXaA34bJ01y31GRqLkueFKwIWnl-LBwvD4v9zPNmjjrQTu-KGoGXqSSI4_9X4r36HLZDQMJr9Yp_VaB_Icbf2spzHXvK6OrE4mzewyJ87BvVue3cg719QEt2EThdygdyqL4_oIXpjvppAp-Ma7vKPBKyWMEAvbEfgggOmwHksbnJM99H6La6OyT5nWUTUgclJNozOnn_AWtydik7tlDKomOsJyJ-X1bvbSNEh05es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721fa47854.mp4?token=Jz77bC5kckI_7V5kQzrkcJd_T8leyHVVXCpfeAcMeeCWAeqVzfSUqPnjJaIo5il2eK4BVlSHbIqdVSSQWa5A06VivpQ36g-NsXJ_gshBbxt_L7SC0owg-ekiuhimTXHTjxuUizwyVF3wXMevW5ZXfxq4pFTOjeTlbXiW94ItnnnUp5FNJXLWnGVmhoZWckQS_IP8X_wJOTHkrgdEmGpfJkRfOP5bI1eITshuc0dR4iSObPOVuv0RTlmw4c44HbH6TRM92jyRXEsRodYakerLfjSPLR6w55sIuN0i0qq45tHwsQ8cVOlmSuR3xZmk-7qgQlnF15D8K3QGZXkD5n99tJxIhgHRVM8z0rBGofpgMTd9YhxU-dv2cVrJtOS0j-IBMiQkNH5ZJ9G7tVlCnmSd6BZt3MMd6hfq3bR9FdBPh95Qb6QiDh_q6QsgeVg78ArrJ3AXaA34bJ01y31GRqLkueFKwIWnl-LBwvD4v9zPNmjjrQTu-KGoGXqSSI4_9X4r36HLZDQMJr9Yp_VaB_Icbf2spzHXvK6OrE4mzewyJ87BvVue3cg719QEt2EThdygdyqL4_oIXpjvppAp-Ma7vKPBKyWMEAvbEfgggOmwHksbnJM99H6La6OyT5nWUTUgclJNozOnn_AWtydik7tlDKomOsJyJ-X1bvbSNEh05es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">٨ تمّوز... موعدُ أطفالِ العراقِ للوفاءِ للسيدِ القائدِ الشهيد...
بعدَ سبعينَ عاماً من الشوق.
إرفع قبضة يَدَكَ | أَنشِدْ قُوموا لله | وَاحْمِلْ رايَتَكَ
🚩
🚩
🚩
#قوموا_لله</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/naya_foriraq/80952" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80949">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce101f4641.mp4?token=IJq5sFIDSypAEnJD5ZEhv4Ilm4eCNM-s08lVx7pjBImElgPBrqV6pQHOq2IEXlKlggwowl42vmsVBaxiIzrZhd4OTgg9xlFwx8fA1Tt7pjAImLWOe1Qbr31rDdg2hvOwrH8TgW-L5XDKhzJXX6h-WVjAvzuGtQug-gQnZMdfzp-HkVOlvDKQAYwgMpIO791SMXPZ6mD094b-7m3_hF5BBdYmDUZL_jcBCdSizUy5Q_VLeanjEmSm7h_75Vl86_BqW_88aaSGtPi7h1PCA0LEVV1hhe9JlKdT3MfQmYW5pb6SVHGA-_W1_MiPuY2-0qyzy5vobc-yGuS7nWJoCaLU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce101f4641.mp4?token=IJq5sFIDSypAEnJD5ZEhv4Ilm4eCNM-s08lVx7pjBImElgPBrqV6pQHOq2IEXlKlggwowl42vmsVBaxiIzrZhd4OTgg9xlFwx8fA1Tt7pjAImLWOe1Qbr31rDdg2hvOwrH8TgW-L5XDKhzJXX6h-WVjAvzuGtQug-gQnZMdfzp-HkVOlvDKQAYwgMpIO791SMXPZ6mD094b-7m3_hF5BBdYmDUZL_jcBCdSizUy5Q_VLeanjEmSm7h_75Vl86_BqW_88aaSGtPi7h1PCA0LEVV1hhe9JlKdT3MfQmYW5pb6SVHGA-_W1_MiPuY2-0qyzy5vobc-yGuS7nWJoCaLU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
كل بقعةٍ في إيران تهتف الموت للأميركان.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/naya_foriraq/80949" target="_blank">📅 17:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80947">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tckCTWEWiHUb2CL_9L4qHctX7kyu-p-hm96oz06aFH42U9h6T1yyszerZ7R1J807LpzTPb6fXipPNE9dXEmGmt4wFQhlXhRhKy1yOTBn2jHp6GngqQOWYW1gtlKVH2Fqd8H5mYb3JIbODXUQH0HTBGVCEsrD4TQIaKm-hZoRTIhe4HtJEN-Q4nm4lyV-pTC_l6IfDbsKdS5R60UfHcy8BQVxfXC4yfPz6U8ZncFLixUViRHjRMBgfddswf1I2A5BJWa4nF03IUJI2z6F8uPTYhJEtaGzQChLL0VzBpYSFGjHIE5JdfOEm8KlYhJ7TCAXDYXxvi5FUcF2L41vpDXYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الإرهابي الذي قتل خلال الإشتباكات مع القوات الأمنية العراقية في كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/naya_foriraq/80947" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
أعلنت وزارة العدل العراقية استرداد أكثر من 25 مليون دولار من أموال العراق المنهوبة خلال العامين الماضيين، مؤكدةً مواصلة إجراءاتها القضائية لاستعادة الأموال والأصول المهربة في الخارج.</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/naya_foriraq/80946" target="_blank">📅 15:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80945">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPLQv02PFDmzElnSV9xDXXd0KHoWkwBZSAfTtEKC9q2cXKx2ecYumt03612joH51jOgsWp-ACmDzF-wA4xYsrhcbM1ynkR0d1cylzuIV9zHHc217H1pSn5xXoDbvUF-eTutCH-ziNjQBA7IA1GGUGdNM9LFZ-UZJGtMIM_rTG1BZ8pk7srLZrnQKlK0s4xS2ICu9CG5pH_Qdfc-CdSxdfvXshhx9gxLBJI7o8mJuohiHsapTDk8KwVMMpivq-mMg1CR6F8dt_GfSCl6WFbki7_Uc5R8aFoLcB8djgcQdfZDzE-CT0CZdntuG4AaHXzqNWizq86HL_Rc3IAtv7KcmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
القوات الامنية العراقية تطيح بتاجر  للمخدرات بحوزته 14 ألف حبة كبتاجون في بغداد</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/80945" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80944">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0532608c1e.mp4?token=KNDBbpBXl1V_7DQIjzl81TIaYnCL84EDTltauCKheSdk6Dbi_RW5QFklRsZ1axUGTWuEbEV16g7ih1E2xNfhaixPQSS38w044cyvtI-rb8cmzJAP3fteWZ6CteAJTn1rRxK7F_0UCWHPL-kDnJZsxKeChrZcMG7UT5SY5skRhh_2677S_59gcBC2uf-KpVNvsoVrs1E5OHFDnAUlWVw2sQ6pCBh_-tEgpJxokIkLMas3BCBr45-nhPzLfH_yHAWaMKfWAsrX8LQmWdv538qmT7auTiNzodosvJLeAH_ZiGCOTCkB-W7CtnjXwDjs-92FfMwpgcN-2-QM-BqqXo5Qnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0532608c1e.mp4?token=KNDBbpBXl1V_7DQIjzl81TIaYnCL84EDTltauCKheSdk6Dbi_RW5QFklRsZ1axUGTWuEbEV16g7ih1E2xNfhaixPQSS38w044cyvtI-rb8cmzJAP3fteWZ6CteAJTn1rRxK7F_0UCWHPL-kDnJZsxKeChrZcMG7UT5SY5skRhh_2677S_59gcBC2uf-KpVNvsoVrs1E5OHFDnAUlWVw2sQ6pCBh_-tEgpJxokIkLMas3BCBr45-nhPzLfH_yHAWaMKfWAsrX8LQmWdv538qmT7auTiNzodosvJLeAH_ZiGCOTCkB-W7CtnjXwDjs-92FfMwpgcN-2-QM-BqqXo5Qnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
كل بقعةٍ في إيران تهتف الموت للأميركان.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80944" target="_blank">📅 14:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نايا - NAYA
pinned «
جمهورنا العزيز..  القناة الوحيدة المعترف بها من اللجنة الإعلامية العليا بخصوص التشيع المركزي هي على الرابط أدناه   https://t.me/KhameneiMediaIQ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80943" target="_blank">📅 13:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80942">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جمهورنا العزيز..
القناة الوحيدة المعترف بها من اللجنة الإعلامية العليا بخصوص التشيع المركزي هي على الرابط أدناه
https://t.me/KhameneiMediaIQ</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80942" target="_blank">📅 13:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80941">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
المتحدث باسم الدفاع المدني الإيراني:
لم يتم الإبلاغ عن أي حوادث حتى الآن خلال مراسم وداع السيد القائد الشهيد.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80941" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80940">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
سيقيم صلاة الجنازة على جثمان الإمام الخامنئي في طهران آیة الله سبحاني (حفظه‌الله) ؛ في قم: آیة الله مکارم الشیرازي(حفظه‌الله) وفي مشهد آیة الله نوري الهمداني(حفظه‌الله).</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80940" target="_blank">📅 13:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80937">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lygn6Gpft4LY3PeEYLERmRv8bLdlU_GTq0dESAAll3-h6JjKxtewraDm-yaegCUntzbBeg80J3pPLo9iPNyAO-Y1hwNuxmdKJCqM28HFLmLKygD43ziGtK3RGIDEHB4OVa-WXqk-Ummviw-zDnXmU6ODVyYqguvg69lbbT79L6M8BIXE2iTLOf2Ce271E5AiWL2iM6zraEQIYHNqirp1cuhVLuwDjbW4nhqEMAhhuQwId80aOINEz3oq-dtVoK5qH5KB-c3csdAQqR7_c_I50L7W8rA4LW2VvJuQIwXZr4W1ic7tiAtvnJ5_lnmk0-zhd4mVKAi6siuvI7wFpSzT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdff87be6.mp4?token=lmrIYrwIZpLSInJAAygbwV0rcZEhZexiJ5EEeJKk6OWRD6qVJ1aLnXT4UMA7iuHXxr8y5PNPgFx9Dw88mv12NkF1tyn4OljI_4FhLuGhkssLhUOXhlObL0kJcLKXuAmre4rDZbl2R1sgfC8exqT7s6MVKhThXtvrzi3q2O-d5ta1HVowLoLum1IYUXkLNsHFJHvqdILQ2CXearbRQ_JGa-CxIT8g6lA5Meso9lulZ06NlaNv6C18e4IIKi-4_DfjR2WW7zAxAGVjG3wglxcMdMTCQ_kXppKH3o-seXSmZp-Uj--pSYckqL7sqV7P1RCIkZ_pc_HpSq9z1kwN4XiUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdff87be6.mp4?token=lmrIYrwIZpLSInJAAygbwV0rcZEhZexiJ5EEeJKk6OWRD6qVJ1aLnXT4UMA7iuHXxr8y5PNPgFx9Dw88mv12NkF1tyn4OljI_4FhLuGhkssLhUOXhlObL0kJcLKXuAmre4rDZbl2R1sgfC8exqT7s6MVKhThXtvrzi3q2O-d5ta1HVowLoLum1IYUXkLNsHFJHvqdILQ2CXearbRQ_JGa-CxIT8g6lA5Meso9lulZ06NlaNv6C18e4IIKi-4_DfjR2WW7zAxAGVjG3wglxcMdMTCQ_kXppKH3o-seXSmZp-Uj--pSYckqL7sqV7P1RCIkZ_pc_HpSq9z1kwN4XiUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
في العاصمة الإيرانية، قام المنظمون الروس بإقامة خيمة خاصة لاستقبال جميع المواطنين والضيوف من روسيا، الذين جاءوا لتوديع الشهيد الإمام خامنئي وأفراد عائلته.
على القماش الأبيض للخيمة، مكتوب باللغتين الفارسية والروسية: "الأتباع المحبون للشهيد من روسيا".</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80937" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80936">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M45Q-7SEEwMskZTXi5zJOHVX177pkEpqd9DZy_hqySM2WHV44uP-jcs2AHcn9_5J3j56BRku-_5wOqLMuTVJm_UKCoFOXI8B8Ej9ffshr45H8x3Q4_SoqjbaHZPIuFk8lsMWoSCEHYdrAVs8YL14xmIHmC3QsJktiHRJMEdg-kJMVujTDuothLLH4APurXjdhTIG5t45dmTwRq5nevEm8jSi1L3Cpt0x6601aoiAA-7cwjnUsg84H4eXUcdKCJqrWYHeepkWwKXEKraGOtWoaWl3M52CHe5D7vxDjBa7KbCw6oMf9kBMGyquBMHpM5VNloDJyt4DV_u4CQxpehUtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئيس العراق : بعد الانتهاء من ملف الفساد سنتجه إلى "سلاح الفصائل والملف الأمني مع تركيا"</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80936" target="_blank">📅 12:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80935">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
معاون رئيس أركان هيئة الحشد الشعبي لشؤون العمليات، ياسر حسين العيساوي:
اكتمال الاستعدادات التنظيمية الخاصة بمراسم تشييع آية الله العظمى السيد الشهيد علي الخامنئي (قدس سره)، والمقرر إقامتها يوم الأربعاء المقبل في محافظتي النجف الأشرف وكربلاء المقدسة.
الخطط شملت محافظتي النجف الأشرف وكربلاء المقدسة، وجرى إعدادها بالتنسيق بين تشكيلات الحشد والقوات الأمنية والجهات المعنية، إلى جانب وضع خطط تنظيمية وخدمية بديلة لضمان انسيابية مراسم التشييع، والاستعدادات تعكس مستوى عالياً من الجاهزية والإمكانات المسخرة لإنجاح المناسبة.
مراسم التشييع تمثل رسالة وفاء لدماء الشهداء الذين ارتقوا جراء العدوان الصهيو-أميركي.
العراق يتشرف باحتضان هذه المناسبة واستقبال المشاركين فيها، لما يمثله الشهيد السيد علي الخامنئي من مكانة دينية وإسلامية كبيرة.</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/80935" target="_blank">📅 12:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80934">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8fo5ThK6gn2jEHcSoyXkvXORE4tdmTY4i9robs08zkTv4LWMjDDk2fFMiVSgI1D6XBph3p6uxvzHhzFFZrBeYIEjtkPO2VTsmcNit7srdZNuFfiMOh8GIi1ZY50-kUMyMfHYw71_eLUKnnKRyFcq8qKQbBGdEpK5Dc9gfR1OXEKl4NU5a0Qz_WWIXZxhbRU9nbbtb3A593yEBWK9JT0AUqa2zyBVlvzU60E5ygQ0tCA-F7wEElUFkzl8C8LcfEEEuMbPPzizTKenm79BHbF42YvLuRpf4lkMbm2oypMoJ_vY8zCNoXcxf8ClPo-6c8-c-iuRr0dAu_6XN6zGWQo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80934" target="_blank">📅 12:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80933">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt8HTY4JijYmVmuRRkCmIpw9QNfhUC1nZO1d9L6-belWdJ5rybUmD3dxEJvLN7hkx3jczQaUhgPSSqsSrK6QzLsqufzEtHDJlfuS8WY1lNRydsUqbfXvul57_1Es-NYMXjVZy2BpwxcJKqmhro2JX8KsMYAz6i1sOEL9rOu4I9ofs9DiNcYJ7uY-V00mX8UNnWbATAKreXFXTmRhwwBXpPZuOAD6EFv7imW8BbmeyVdwXAb7hN0J0t6u6Zfm6osgM9XyZiKziCV_rJCV2Np_xI6zD8EW6OlXOEGsgwVkxquxncUXr7nGdQVZTJ1Et_vLQiwYURZir1F5O6c1m5Mh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
عمليات الفرات الأوسط بالحشد تعقد اجتماعًا لاستكمال خطة مراسم تشييع الشهيد السيد الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80933" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">المرثية التاريخية للشاعر الفلسطيني البارز تميم البرغوثي في رثاء قائد الثورة الإسلامية الشهيد.
#قوموا_لله</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80932" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80931">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15cbaa4687.mp4?token=BvQsUjQzrzxWiPz3PRs4I1T9YnFkYg7Ul0rlAEnOm0ikA9s1WdFsuZ2T_7qKPtLtr0h9PlZ4biM4WX5KBcz7pME9iAhTNjxXXphPq_ZM40eiHZ80l5oUOpyWm1xfvR3_czJD36C94ueMxmDbkrUNRoe31xRV_AL-Df3cWFeXSB4J-q5Hd-XZOz2qKEYN_J7ocbDqde8PrYqq50UPvoyNM2kp0SYjokP15XVrXBnIC2wTj9LEwE4LD4Y-ZhhNg6ctZ1i6apqIarW6YSGZsP15FNsH5MbFcUrcKALF2ORdDG1khZkIi8VijU1IYsxnmoqPVm7v9jHc6484MKLIm_uu4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15cbaa4687.mp4?token=BvQsUjQzrzxWiPz3PRs4I1T9YnFkYg7Ul0rlAEnOm0ikA9s1WdFsuZ2T_7qKPtLtr0h9PlZ4biM4WX5KBcz7pME9iAhTNjxXXphPq_ZM40eiHZ80l5oUOpyWm1xfvR3_czJD36C94ueMxmDbkrUNRoe31xRV_AL-Df3cWFeXSB4J-q5Hd-XZOz2qKEYN_J7ocbDqde8PrYqq50UPvoyNM2kp0SYjokP15XVrXBnIC2wTj9LEwE4LD4Y-ZhhNg6ctZ1i6apqIarW6YSGZsP15FNsH5MbFcUrcKALF2ORdDG1khZkIi8VijU1IYsxnmoqPVm7v9jHc6484MKLIm_uu4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
في حادثة أخرى.. عصابات داعsh الإرهابية تقدم على إختطاف مواطن في منطقة التون كوبري بمحافظة كركوك شمالي العراق، وتقتاده الى جهة مجهولة.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80931" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80930">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80930" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80929">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭐️
رئيس الوزراء العراقي "علي الزيدي":
سنعالج ملف الفصائل المسلحة بطريقة حكيمة ومقاربة عراقية تضمن منع إراقة الدماء.
‏أميركا شريك استراتيجي والعراق يقرر علاقاته وفق مصالحه الوطنية.
‏العراق سيقيّم احتياجاته الأمنية بعد انتهاء مهمة التحالف الدولي.‏
العراق سيحدد ما إذا كان سيعقد اتفاقيات أو مذكرات تفاهم مع أميركا أو غيرها.‏
سنعالج الملفات الأمنية العالقة مع تركيا وإيران وفي مقدمتها "حزب العمال وسنجار".</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80929" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80928">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
جانب أخر من التشييع الرمزي لقائد الثورة الإسلامية، في نيجيريا.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/80928" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80923">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rN7WwXkL9S_QxFA3fWrC8UWzJBoK8e1LMlqbfjC4Yh9zwKvIA5EIJ2CFxi2GEMsZDzfBm4LWYzzojYrr6E9YiXOGWJldiwxIB-GsIfO4skv-7czjf0tsHCpgQgQ_gdu9u6mphqShiTFeIIkMeh2CIX8-lCqWy-9qES75WFlnWJkI4XjihhfXck9RAeLL9u2cYFJ4vVbMvx3TySUENX4_RnP8b_TwgUB04SCb19lG86CLcMc1GGt1_xMo94gbKQmJQEuP1HBpXMY4TQaca96OvTqyksjFZ__9jeVv7ySNA_UcXcqFr5bMtTXzjrJxrr5U4w1gbxbT4W5AsAsePncAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxdYW80rybzMVadlHErks1HPsDro8pRS278QzZMcsT4VLGnhPkEWOS-mwibGQUsXfWP9_Fcu_bLfUX56PAqdFKOnkQGWleN9PdKcdPoyOekJCE56omyEmPzfRYoxIr4Qb-eg6X8gs-XhQkSF4u94wg8BGSOscPxVMejlJG2d0R6jU3B3X3XvydUhwKaaFERSzpXfygieJnOvR1OIHOHIB4_oQxe4YvY_cuGkgKb717n8uZO-DymTHB0AutkTq8sWtEbOOZBxwoZFGup-FEPoakeh5x4Ga8Ag5X22XObtf_gEloQTgTcdrAWnNta_TlZzLEAAJ0n4jNFuQVUfL9IEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zvd2Z7LFug3xtDMEBWtMPUHuG8DOcEZWbVSyUBSIM9HjUl1rWa_408WoseO6inpuRLdTmhwZ4CuVVBxA9DgALwaxfJtTLDgfwC1kiQR2EJMaLNUcKmMvukNcYlhZdNBJOS2wYnf3A-W8BcKGVOc5gF9EQTj1jd8_GgwFZS1Qdyv0888pCdw691jnmgqzhCbXO_cIQR9VSzdXT2P5TJdsNs4ogSPxrr-hFLbQmcn5psFFegpkAV3_6-udTNHDIUdS7peK02bwe3EaMC6RVpl3OJFRD7uWj3S3kx23BJHdgQ6plUEqTuYjAgr_xyMN8WqzZ205DSMWgP05FzuDezD7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg2RaBPfs61eyI2d3wb-S36ZsQxHoWfxPhYwAs1d7vD4iqwezeVYck2w6ulvdg4mTEKVmm24mVe39zJo98tZRsKXl7e5zI36zZIA-pVAnLkD6-5nAiP31QxvbLZOzVFH0xqb6nqSdOJuuYQqrP1A8vP-7mmunu4dNZ7P-WCuC4NAEi2qgnPojlND-UrTy98vxI3q_kqD6sQp2-uBECznbbZa7yY9tzgC-nup77K63FLaMI0IuSwEsotyOJpoSXgz4Sjv3qoA8BHVLcGNqQv5_lPjQ5jtX6qE-dZRu0NZtywwI6TlzjLZLakb7QymWWRyu6cso9GGFHQKyQCRj14H4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68d37552a.mp4?token=kWN00JUbNCFSUbRFO4KwYZrCWLcymoQOGm-nRp3pAd16RvHkkRZ8M61RVirhbAWT1GX-UZadOap4UigIw84iUZbHLG6HLH6h1hwkG7HfIc8Bz_H6c55apMBB9uI3dkPTUyZfw8s9OEen2Tgxqyx3R7CHDFAbJCOcZ-UZPvkMkzmo4S7TwVUUXBdTMZvzeTkYAYYvll2Y5uPhRCavs8yh3eOAlQwZ9T8r93Ijrag54LH26slYNr57RuEsvwN3-XQKrEm4y1S8e-NQCA2z_velnLMzSB3BQaFrO1o-cQPMn9tFLq334SZk5rpir-2g0Q-YWVo_Y9DJB4atC9qNj3FaNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68d37552a.mp4?token=kWN00JUbNCFSUbRFO4KwYZrCWLcymoQOGm-nRp3pAd16RvHkkRZ8M61RVirhbAWT1GX-UZadOap4UigIw84iUZbHLG6HLH6h1hwkG7HfIc8Bz_H6c55apMBB9uI3dkPTUyZfw8s9OEen2Tgxqyx3R7CHDFAbJCOcZ-UZPvkMkzmo4S7TwVUUXBdTMZvzeTkYAYYvll2Y5uPhRCavs8yh3eOAlQwZ9T8r93Ijrag54LH26slYNr57RuEsvwN3-XQKrEm4y1S8e-NQCA2z_velnLMzSB3BQaFrO1o-cQPMn9tFLq334SZk5rpir-2g0Q-YWVo_Y9DJB4atC9qNj3FaNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على طريقة خدمة زوار الإمام الحسين.. المواكب الحسينية تقدم الخدمات للمشاركين في مراسيم توديع قائد الثورة الإسلامية بالعاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/80923" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80922">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsEQPDQM0ntULBupv9Pe2Wvdf9KkqFeRkZFrpuEdYn0l1t0cAPdTh1ES2j3iiS9mmU080KSl4m9qMLC2fN3qJvjCBp9zJ_kY13Dm_7nIcgl1i1IyF45p1wGWrromfkRkOXGWwjVvkLaFqR9M805TOOfFqrQuZDN289U7L26YxL6S8k7mBj_8CuiTDSHVaPovlPngiTPX9w3_a-KC8VD77aN_5qdjnwFgL7LK4do3akk38dhHT73vUP8-HciYvpMvJIIlvjzrGBoLyDoKvxr9WTnAFS1798bZed3W-RrCkkQdrOls5JHAn5S1Ym586FUtqN4fMx7BGM0_TSY5k595zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
إرهابيي ماتسمى "وحدات حماية شرق كردستان" الإنفصالية تعلن عن هوية عناصرها الذين تم قتلهم على أيدي القوات الأمنية الإيرانية في مدينة مهاباد بالقرب من الحدود الإيرانية العراقية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80922" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80921">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80921" target="_blank">📅 11:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
غدا الساعة 6 صباحاً بتوقيت طهران ستقام صلاة الجنازة على جثمان الشهيد المجاهد الإمام الخامنئي والشهداء من عائلته في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/80920" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80919">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyFq6G7B7WUn0gecCivWeceM1t_9aL3iyH2-ubBQhFqwZ2ysIcuXh8Co5ZRoWaeGJ_swEst2ewr3qCAl69G80jLAwRR-1AKf62nK6w1KFMdXedBqJxtHuEcyCKvSsWO79aGuQipI0tkRWdnq-a5qxu3O2uZml-GcIQd52grNvr7070-MVvnPlSjD1-yzAMiBA8cRnJpldWMB9WSKJx9TxD97OQtTWang_j9klHF1UyIhP3GB9m3R3LSaRZDsw4P4iZ2Q48U4CPbKX8QMmjz5PwUFXVJAUuefLUJt_FyUUapQacUw8UbN8j9SKW5D3KADx3sBlVTkhIaOivfyW5o_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لازالت الجموع الغفيرة تتدفق نحو مصلى الإمام الخميني في العاصمة الإيرانية طهران للمشاركة في توديع جثمان قائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80919" target="_blank">📅 10:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80918">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15fb197939.mp4?token=WKUvJBa75C6tSYxETPreeiFnUxYWs8xa393GUdyblvl2C4YGYEWcoz-x9Io5Md8U_fl8CEKbqhaHclDCKSS62SCyyCxGsg5tcgvnjh34bHcIpS-sdxsjKY3Mq5WkJFzpgU3_RiYzZO_39APZ-Mbos3_N2agHTz_OM76rHTSlQhagx6KGAJ7KqpCTGgyoG6KriGC0RhI3h8kirOBh80SwZ2eZQu9G7JargU0GewQIUvI9J-cwC6wGpQVcexAihQk9x9AofqJDSWQ48J7cJ0qPauj0ryjiqvqO5rQoDJ-yFqy2Mqy46vpF62lFPn-ZrDtlfUHMRpBldv7N_5n88LAlMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15fb197939.mp4?token=WKUvJBa75C6tSYxETPreeiFnUxYWs8xa393GUdyblvl2C4YGYEWcoz-x9Io5Md8U_fl8CEKbqhaHclDCKSS62SCyyCxGsg5tcgvnjh34bHcIpS-sdxsjKY3Mq5WkJFzpgU3_RiYzZO_39APZ-Mbos3_N2agHTz_OM76rHTSlQhagx6KGAJ7KqpCTGgyoG6KriGC0RhI3h8kirOBh80SwZ2eZQu9G7JargU0GewQIUvI9J-cwC6wGpQVcexAihQk9x9AofqJDSWQ48J7cJ0qPauj0ryjiqvqO5rQoDJ-yFqy2Mqy46vpF62lFPn-ZrDtlfUHMRpBldv7N_5n88LAlMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الموت لأمريكا"</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80918" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80917">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368ae0ed53.mp4?token=OEgCk-GtSLro1Ilp9LEujEU3kiAN3Y6brOf0GEwKYPNVjIs0ED927I9L-V-GWMroV74nOBojiDLrVBTUOq_HDlXpCkGo4i1DlC42kjTlM8GeofLS3dW1yFPFYTVh_ZcbBFEWMwnyjnDMqrYiAzMXsoNnnBI1a_T3hRcOwqKCaXAM8SFPuUA7PuvGIvsL9v2yqSGsSf9NWyeBj0Vokm2HMrtfmn-QbzrJCPMDeqgMdzKFi5mqU2xLw3c75aA19nJD02oWG9ivUtQuqz6Cz5wf9V1sE9mylu1OR8PuXZL8LwKJUYdfJvNPbcOZ2ZlEjIrrUPtVdptj5rIIRrSUBKln30UM8AH9x0JOXQCg9NgihwgGYI949wglvL6T0Y0FWcuqI7FN7oTI7Og2aLAtjiEF8846O3IJl1lzmGNoaaQEucOV-368p1Xe3FKEk4eRQwumDVqXSKpgOwM290p0EMUG63kwevTs5eIzF-bv4UlxiYPx1aUYAouHw6fQRB13ykYTU53pVrpBWxxd0LjLfPrt1YBDlbprBWSc0bt1kmyvGs1oOKFnxh9D_DvSfUg3g2UUzc5x_QCN0qJK0g-FdTNLhNJvUgmjIYFD1BgLV-uWgsveylfcLMF-wjXZMFqLRXjQMKFPjQcNRiX-Hrr_xKDy9rjb-h7bY0cSKpnS0vTCAm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368ae0ed53.mp4?token=OEgCk-GtSLro1Ilp9LEujEU3kiAN3Y6brOf0GEwKYPNVjIs0ED927I9L-V-GWMroV74nOBojiDLrVBTUOq_HDlXpCkGo4i1DlC42kjTlM8GeofLS3dW1yFPFYTVh_ZcbBFEWMwnyjnDMqrYiAzMXsoNnnBI1a_T3hRcOwqKCaXAM8SFPuUA7PuvGIvsL9v2yqSGsSf9NWyeBj0Vokm2HMrtfmn-QbzrJCPMDeqgMdzKFi5mqU2xLw3c75aA19nJD02oWG9ivUtQuqz6Cz5wf9V1sE9mylu1OR8PuXZL8LwKJUYdfJvNPbcOZ2ZlEjIrrUPtVdptj5rIIRrSUBKln30UM8AH9x0JOXQCg9NgihwgGYI949wglvL6T0Y0FWcuqI7FN7oTI7Og2aLAtjiEF8846O3IJl1lzmGNoaaQEucOV-368p1Xe3FKEk4eRQwumDVqXSKpgOwM290p0EMUG63kwevTs5eIzF-bv4UlxiYPx1aUYAouHw6fQRB13ykYTU53pVrpBWxxd0LjLfPrt1YBDlbprBWSc0bt1kmyvGs1oOKFnxh9D_DvSfUg3g2UUzc5x_QCN0qJK0g-FdTNLhNJvUgmjIYFD1BgLV-uWgsveylfcLMF-wjXZMFqLRXjQMKFPjQcNRiX-Hrr_xKDy9rjb-h7bY0cSKpnS0vTCAm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الموت لأمريكا"</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80917" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80915">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiLQUP1muG187dvg3YMz2ePkqPw3shGtqQU4FRvWU4p_eu4iBGiBK5vRQU5RAArOT_xc7XFJo6Yfc2tp3ak9DhDDtnOxKme0sgmijWqsLWeYy5a0crQtGr69apwsGvEyjxNAZw2Ao1wQfuKRVfjp4GmR0DIzz2iSIW4SR9dPJ2zMdt4R-ysPt0pbTFWpZ_EqhG_W7YfhOja6XR8yq46K0n6SdCxp1rjmeAo-DQh-HvHEke5uhUdPB2GLW20b2B6f9ZOyAH5xpwGjjEOp7iOY51lqRljfUnDvOe76nuGD1mEMie_Ngzwr_XEMHcvBxbZropcBNa62BJ8Bb8RRnHIn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpykl1F58E5cVLtPNDLLerwMuJGF-NRiCt-6Sn9W_J0nX-XCgkVu6ZGxYpF2xpHob_dBVSGmihI1TJUXIGZhsnAr97mCcqslLKDnIu-fGPGDp6XkXa2NXDFhB4nCpZ6hzTy02hpObMFUQQ2vGh_ldBw34c33bqtn9AqNHsDxtolJMXjaiMdlst3ZmzyXGv0UTaS39t3dxjr2_CxITn8ddnKbbvnRdGfWlcD6Iu9arEGJAl6MPODVBiovxBe2Hv7y99R57RtHcqXN3WcTBxMn896U1WvO3RN2hiyPEq5no5wZSexaq2Ak-zKoyMddcZb8EP5VubcCvUPlR7IxVMjabQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
من مصلى الإمام الخميني في طهران.. محور العزة والمقاومة يودِّع قائده الحكيم الشجاع الشهيد.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80915" target="_blank">📅 09:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80911">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t80QycNRPq2qPMYmAqH0UfEKmA_jDpEwmTaMpU-dkuEKuvivxJ8ldHMlIytEr2krm9tOvtIzj4VpO8Pmbz-q1JomMdIAPADXHQqXtMaW1nA-A2XwxWd194NANav9mI0RflLLqBOptkFyJD4WsSLthwd-pxFD696N2yAXqe5-ofHPU7q6F01V9HY3VAWW8oQdWu2F7uY7CWh9fHu0NHrCeHle55X832DmPmUy8tsQxftDOjH7o6NaqL5pmw5YXyijNmcLyX-RQoigwkVqC39wxQdAo6yF8W2IDVfjShN6KUjXe_KtGu_FfE38BZGMAcQStOA1wb41isJ_Zbva7NTMcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdIayw_10LlEwQGCUAZ1DpeXTms4whMnWpz8C7I2lw6HfaHXA82yF1pQdIrH6tuAyxHzRsWKH0lIK5CNO6SDhNhkUx8EGe3pEdzgUB5SjBOCbtbGdQ11Zf9PE_F1f9VJLkWdnF3K2iPnr38V_ZjQ17C0itk8SWmulfbC-7WhaG0m_T1qBAyYPks1rRo27PuZQ7rPNu6QRGj-c2-AMl7eAkFv00lGHa-HyUsBGE8sRXh4IhMEmhqqRxnvCGDI6GV8mSLYLDdIElRPFkvnILAgshrahGimTyfFn2ObeqXXOywB6kKMJyHmcuOWrxa3uENXIWahpU29YsRPp1h74EnudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-bgW-LDqJx9rlAAiGoVSHiEvWwNXS5S4yMC38e5jfPKQy6X_W2z2Rwvbzw5R8aU8_wd6Rwd5XWCbpNGu-4YIg3TYZSS3EQS3XKxT5IT8s90k4SIurgvy3nitxm-dEWImCjk4ssIlZdP6X5sqMuF_5QpcPJZ_g4e134a4J0uA81kjGvDieePGsa2xN3FB7DB7Qo3hmlxW3pHVbchvUAHzk1pdep1-TjJLt2BSGYKQxgZDvkiEkrvE_D3Of6Oj1KlOH_b64ge1rCvB1vOtZj8x5Sl-_VkBq1WV2wLz9ikjg6VQg_HPNkWBIMVy8C0BftLjdTgNnMUXxRyBq3_AS1tYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIykLzyx-TW3o0DeVE10FBw2eLU0t2wE8i_W5eM-hGPrJ2d9f10n5sMVAvA6KcPFLwKR2xM0cxlg0STp52X9mhQX8v5nygNjDS0R3uL-QUrKr7hcrDB1FcE4ssoq7NtFDiyPqaz_KYe573UmS5qF3QjwILFy0sSt8NlunEJWSkzxP1P8FLy_yGpel6hbqfLOTRiUS0gFEm1r-8aWWni4QLdeLpwBSkPrWvuR9RReRotRHwysRDsXTngDZCjkVm2Y7IC4bF1eTBj89OnrhSwZ_oWAo79PZydB1T8d290NJlupkQO3st1-bdYnPOzHjllANo58nHDesY2cZSTFfYCL2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">أقيم في نيجيريا مراسم رمزية لتشييع جثمان قائد الثورة الإسلامية الإمام الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80911" target="_blank">📅 08:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80910">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2ba6faf1.mp4?token=UWokhg4aY7CS6r-oJQOeaOh4Y3xa2OugjgqL7ZYqsnKncinXblNdReJ3TYqpfj93NNOqTys_mipVVrop7ID8tKb9fRPkOvj1340Di7uaDwK5lmdaU2z5-wc6FA-cxw7y3x2RjmKC1L0YDa9llCducdikoHJER5RfMd8c_P5t1d8iHAxO52OK5TCe-dy-Tsezs_J1-Gi5vNhyhnya1pFskuFoKNZcfl0z3wMaMGy2YheXkqRz60nT91zHH1o8ViBrgmLy3GsVSmrnewSoiXq0Cw2wwlAZTgQr_quTIU1kyZUZ2Oz1Z0DQC--59pTXWll3Hvlxgdjxo6g66MPeUo0vBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2ba6faf1.mp4?token=UWokhg4aY7CS6r-oJQOeaOh4Y3xa2OugjgqL7ZYqsnKncinXblNdReJ3TYqpfj93NNOqTys_mipVVrop7ID8tKb9fRPkOvj1340Di7uaDwK5lmdaU2z5-wc6FA-cxw7y3x2RjmKC1L0YDa9llCducdikoHJER5RfMd8c_P5t1d8iHAxO52OK5TCe-dy-Tsezs_J1-Gi5vNhyhnya1pFskuFoKNZcfl0z3wMaMGy2YheXkqRz60nT91zHH1o8ViBrgmLy3GsVSmrnewSoiXq0Cw2wwlAZTgQr_quTIU1kyZUZ2Oz1Z0DQC--59pTXWll3Hvlxgdjxo6g66MPeUo0vBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود الغاضبة في مصلى الإمام الخميني تطالب بالإقتصاص من الرئيس الأمريكي المجرم ترامب.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80910" target="_blank">📅 08:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80909">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnlwgjbaRWjZwx8JEwo8kiAym6ty-VkGlrXT2ShOEMIq-8FizxHEliJGrYJbaN_CE9oiegyNq99OE7WJNCwKUCH5e2sO-hq0axuY6HMLElCQQ95x8yor3WINdENkqheNPCUbxx4kA5kmNeRTGHJPUZtn5kqVAAv7IzyASqQi9i2UNWybo6pWEBGdZn0_wjCQGZp8QEBhCUlE3vouXepJgIerw4wKslRDAoFq1CoGZmJQgMt_jhUlW0NY_MVjoUZIhIv9M-7Ui9SEPp_6K8mEfzou_0qObs58eL9IE-fkxw9p3Dw8F40FmnWGV5quNDtvf-z95yXqnZM8BcRB0hdPPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجموع الغفيرة في مصلى الإمام الخميني بالعاصمة طهران تنادي بالثأر لإمام الأمة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80909" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80908">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211d83b2cb.mp4?token=a4IJBZz5sSv-jJLtyzR0qP622m56H2J5L3YGGg5wNAJ2R7o0sL8pSpFR-_q-Bq_xfCaPXuVphzDtSAjEUPF37Kvr_PVI8HlaH6hLHDMHCjoFVnpeEsdrD3krhA84qbXdCIva5txpN0_O80s8dOjejPd62WUrS24SciXAVw-p0TdK_NG0u1GpV47oCVQ8szM1GlLJjUbnlYyD3iPCkn3D7hFMXuzl5z0cd34zzFSxesEA3l5PGjurCXw3Ed8YgpepdfoS-wJN3yDIIZfUhfVzp1lsXKTQaTw-mqRSqHcswqrg13rzXCx8kbkZVqtCDznzhRZSYLc5A3O4tkZyKBoLa0j3AppL35u4BS0zzCTNqRwJoCyddVuHdk-epS2utBX8bHJkKVTLPIwPiXKh59WqROwpgyVy-kOJ83JxKh6W4eIgOHVAiVYaA0fWr6lvGZgpjF3D6VBnm2PY5KVP2yeaZiL6QAGaZhD8wbv3bJkhwsW0dS7uVTLY6NGckwYKImrHD7waaCImORCRgvskt5nnlYQ-iIYbqlxnuXFEnBAsUD_xdLcK1jiOE8vF-1qbQCBpcPRdFfk7RU6PhdWBl74S0jczx6iKFLHjCsisPwqwyIvZH3Rp6ok8EKhSRuBk76xs16FEjqBea6ozfHzJrq12QTzrDOlENJm-f5VoYeVQu_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211d83b2cb.mp4?token=a4IJBZz5sSv-jJLtyzR0qP622m56H2J5L3YGGg5wNAJ2R7o0sL8pSpFR-_q-Bq_xfCaPXuVphzDtSAjEUPF37Kvr_PVI8HlaH6hLHDMHCjoFVnpeEsdrD3krhA84qbXdCIva5txpN0_O80s8dOjejPd62WUrS24SciXAVw-p0TdK_NG0u1GpV47oCVQ8szM1GlLJjUbnlYyD3iPCkn3D7hFMXuzl5z0cd34zzFSxesEA3l5PGjurCXw3Ed8YgpepdfoS-wJN3yDIIZfUhfVzp1lsXKTQaTw-mqRSqHcswqrg13rzXCx8kbkZVqtCDznzhRZSYLc5A3O4tkZyKBoLa0j3AppL35u4BS0zzCTNqRwJoCyddVuHdk-epS2utBX8bHJkKVTLPIwPiXKh59WqROwpgyVy-kOJ83JxKh6W4eIgOHVAiVYaA0fWr6lvGZgpjF3D6VBnm2PY5KVP2yeaZiL6QAGaZhD8wbv3bJkhwsW0dS7uVTLY6NGckwYKImrHD7waaCImORCRgvskt5nnlYQ-iIYbqlxnuXFEnBAsUD_xdLcK1jiOE8vF-1qbQCBpcPRdFfk7RU6PhdWBl74S0jczx6iKFLHjCsisPwqwyIvZH3Rp6ok8EKhSRuBk76xs16FEjqBea6ozfHzJrq12QTzrDOlENJm-f5VoYeVQu_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجموع الغفيرة في مصلى الإمام الخميني بالعاصمة طهران تنادي بالثأر لإمام الأمة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80908" target="_blank">📅 08:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80907">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f580f185a.mp4?token=rgitaro6B3gu33nwpK23Oag47OUb5WALKTiwq5PPlP80Bf4CZHM9g-jZPgNcWKN0X1j6YtCT9eJ3YTApZx5ssLS5fliuIlZ8sVFaY0NbUKJ4tEZR2q0ldFPiUkrT31kiG_55aq4_jfTohycU9YxAXJBsLKRkPF2-Gf0yQSNc953oV-r7BuZpr8Tcm91sUoKO9rfnDHgVqpKggNJN_MZX0otQvSVD8uNkBnorxPzyVZiUGwThEko_CVFr46y7VXxOE7Y8JCnqqa8lpu17sSRaA8-9HFv_XTdDC-tH3R3j_ctnasoKt90O06BVpiT87Xs4Qv_OdF0z0Q96FVPpo0Ff0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f580f185a.mp4?token=rgitaro6B3gu33nwpK23Oag47OUb5WALKTiwq5PPlP80Bf4CZHM9g-jZPgNcWKN0X1j6YtCT9eJ3YTApZx5ssLS5fliuIlZ8sVFaY0NbUKJ4tEZR2q0ldFPiUkrT31kiG_55aq4_jfTohycU9YxAXJBsLKRkPF2-Gf0yQSNc953oV-r7BuZpr8Tcm91sUoKO9rfnDHgVqpKggNJN_MZX0otQvSVD8uNkBnorxPzyVZiUGwThEko_CVFr46y7VXxOE7Y8JCnqqa8lpu17sSRaA8-9HFv_XTdDC-tH3R3j_ctnasoKt90O06BVpiT87Xs4Qv_OdF0z0Q96FVPpo0Ff0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجواء حزينة تخيم على مصلى الإمام الخميني خلال توديع جثمان الإمام الخامنئي الشهيد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80907" target="_blank">📅 07:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80906">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59c23d54d.mp4?token=l9cTqyqiZrGZ9EdkSBClvetv_TSE_NtdLufFZYq5qjwaSbk4WZlUdKscFa_j8jkXiVxCmxya61rLfupADBapfN70lJZMkVMX_nyJ4d9x6vW1hAcJASkohxDgfuA_V5AQexZnFc44CsdlMUnE7j711iZY9Wa4x7pOnmAbtKZWPswAgYu7juBx7ktAXNntcQ5p70cXH5rpuWgSNaFAyFd5Rs0T8UsoSrH37d-DQOGeiok5WgLtZEWHWOvvWgvdS1nARnbfjlKXJfx7RXyg-SfuIeLOwIhoWIbALsoUaWe5oqEUZxuFpqf4V9kliQuSZFmk5fjnuKWVgVp9F6SSdB1Dfr-9JLKOHsKQLSnfqOpImbgODWJl7jHWo4-B2ilYeDC9tLQr1tLlRYat9738S9YVIht2ck9v0maTGdK4tyakxivZXVhg6ycYaCSUneF2N1LH3YpxCdK0NukvNdWz-UiIMA-SHZk8m6EwPiaFmhkVuT2VG0u2skizewyX7HnD-aIT35Xn0moYDBwg55KqE7uWWd6qq1tKWUCo_O9nX6Lfe7m2co58NA4w_t3f3onSwVr4J4fQmfZE-wZicypFOqHkU0JAfEaLIjoEcQc4ogvQ0G1rHhKj7JI77zRbbkNKzGwd5ORgepReJTNiQs_3ZO-cFryFxRIIqsIzZ3aSbiAX9W0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59c23d54d.mp4?token=l9cTqyqiZrGZ9EdkSBClvetv_TSE_NtdLufFZYq5qjwaSbk4WZlUdKscFa_j8jkXiVxCmxya61rLfupADBapfN70lJZMkVMX_nyJ4d9x6vW1hAcJASkohxDgfuA_V5AQexZnFc44CsdlMUnE7j711iZY9Wa4x7pOnmAbtKZWPswAgYu7juBx7ktAXNntcQ5p70cXH5rpuWgSNaFAyFd5Rs0T8UsoSrH37d-DQOGeiok5WgLtZEWHWOvvWgvdS1nARnbfjlKXJfx7RXyg-SfuIeLOwIhoWIbALsoUaWe5oqEUZxuFpqf4V9kliQuSZFmk5fjnuKWVgVp9F6SSdB1Dfr-9JLKOHsKQLSnfqOpImbgODWJl7jHWo4-B2ilYeDC9tLQr1tLlRYat9738S9YVIht2ck9v0maTGdK4tyakxivZXVhg6ycYaCSUneF2N1LH3YpxCdK0NukvNdWz-UiIMA-SHZk8m6EwPiaFmhkVuT2VG0u2skizewyX7HnD-aIT35Xn0moYDBwg55KqE7uWWd6qq1tKWUCo_O9nX6Lfe7m2co58NA4w_t3f3onSwVr4J4fQmfZE-wZicypFOqHkU0JAfEaLIjoEcQc4ogvQ0G1rHhKj7JI77zRbbkNKzGwd5ORgepReJTNiQs_3ZO-cFryFxRIIqsIzZ3aSbiAX9W0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء مراسم وداع الجماهير بوضع نعش القائد الشهيد السيد علي الخامنئي وأفراد أسرته على منصة الوداع في مصلى الإمام الخميني بطهران.</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/80906" target="_blank">📅 07:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80905">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0629f1b9.mp4?token=UnYVicFF7jfEetpwZOpa5k6eq3bHgXGzxBB72ZC2iptiW4Bpbhogp1D4P3wrsNeQ-7N8B3v-WzL3KtRNQh0G5KNk26tukNaRMQd3_4SeyJC93mNHBIUyv3nGmXAdzatYVtuYFTDRzFJwmmimpsbAET-0-OvFe2-HSm5ztGnX3kItDDTUN_gZeTwMd8Qh1Z_LSoSkmxz8QWrZ10rbC9y-T4jN3m7gkhvT3MagzgRGAW5K1tG3T5dF9goVLOVAnn71_FaB_wBcHWTY3X8IdOXOl_l-IiRr5Yo-iTbKkpZuMGTDVHocwkBP0a0SxGCJ4PaFqNtu6iSKK11mEdac358k8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0629f1b9.mp4?token=UnYVicFF7jfEetpwZOpa5k6eq3bHgXGzxBB72ZC2iptiW4Bpbhogp1D4P3wrsNeQ-7N8B3v-WzL3KtRNQh0G5KNk26tukNaRMQd3_4SeyJC93mNHBIUyv3nGmXAdzatYVtuYFTDRzFJwmmimpsbAET-0-OvFe2-HSm5ztGnX3kItDDTUN_gZeTwMd8Qh1Z_LSoSkmxz8QWrZ10rbC9y-T4jN3m7gkhvT3MagzgRGAW5K1tG3T5dF9goVLOVAnn71_FaB_wBcHWTY3X8IdOXOl_l-IiRr5Yo-iTbKkpZuMGTDVHocwkBP0a0SxGCJ4PaFqNtu6iSKK11mEdac358k8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ای پسر فاطمه منتظر تو هستیم.. مصلى الإمام الخميني في العاصمة طهران يعج بالحشود المعزية.</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/80905" target="_blank">📅 07:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80904">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5b973972.mp4?token=K7U9RPoCO6s0RyO1PklTrNFqunPcUIf-xAwP5EMs5dVXTV60fwh8ZeaTVOfl1u8QAJ2dAdkX6sxiJlQEACsFHCWch2SY1T4L7w1BnTIwUQ4tHOdEA4aDLNy5qg_5UyOcLUyXbZuBOue1zfi8y6brZqESFPctjuY5uSD_2AaJLTr1GtmUdBBzKUIJkXO6pmc3wanZ97brBB143OPDBnbIVZWQa69Pr9fFcnCzYQdWDS1s48KK3ws75U3oP2skj8O4KA3l9DNbflvMdJI4YDIm_v6yRy1QXErJeqKUGb_UVA-upBBRoWKcBAnaxG1LVQQ5MKG95y1EBYoqE9Z9R7Tvnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5b973972.mp4?token=K7U9RPoCO6s0RyO1PklTrNFqunPcUIf-xAwP5EMs5dVXTV60fwh8ZeaTVOfl1u8QAJ2dAdkX6sxiJlQEACsFHCWch2SY1T4L7w1BnTIwUQ4tHOdEA4aDLNy5qg_5UyOcLUyXbZuBOue1zfi8y6brZqESFPctjuY5uSD_2AaJLTr1GtmUdBBzKUIJkXO6pmc3wanZ97brBB143OPDBnbIVZWQa69Pr9fFcnCzYQdWDS1s48KK3ws75U3oP2skj8O4KA3l9DNbflvMdJI4YDIm_v6yRy1QXErJeqKUGb_UVA-upBBRoWKcBAnaxG1LVQQ5MKG95y1EBYoqE9Z9R7Tvnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عَزف النشيد الوطني للجمهورية الإسلامية الإيرانية في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/80904" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80903">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c94673ef37.mp4?token=U6dNFO7gnM2q0_VeZvB07ncMnGrDtbpBeoWIyMLPdqp-QnVK3a_ehiwTS7tfkvikCBE88e_T5jGgzat3XtvrnQhO4F1b1KonTbB287Tv9hdJSCXsppLhWQU_mTIMVH_5jOVycxGHtDsGZuOVFfdg4zwlEpTtPIPSJtq0CqJqvD7ctxWnvBoXDKMFT6zeBqjhvKr10gKUyHI2QrZluywS2AIuvHK6AGxiVq7HeazZ92MarYhJLuV8B7gM_h0iw2Sq0e86-qtjCpfkOJjHJlBM3Iq5XDKcdX5XiSYklLnvqsOu56IOiV8HOwX7cgVrlwOQTg7wK5tEjtZ6qqfwM_tH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c94673ef37.mp4?token=U6dNFO7gnM2q0_VeZvB07ncMnGrDtbpBeoWIyMLPdqp-QnVK3a_ehiwTS7tfkvikCBE88e_T5jGgzat3XtvrnQhO4F1b1KonTbB287Tv9hdJSCXsppLhWQU_mTIMVH_5jOVycxGHtDsGZuOVFfdg4zwlEpTtPIPSJtq0CqJqvD7ctxWnvBoXDKMFT6zeBqjhvKr10gKUyHI2QrZluywS2AIuvHK6AGxiVq7HeazZ92MarYhJLuV8B7gM_h0iw2Sq0e86-qtjCpfkOJjHJlBM3Iq5XDKcdX5XiSYklLnvqsOu56IOiV8HOwX7cgVrlwOQTg7wK5tEjtZ6qqfwM_tH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من مصلى الإمام الخميني في طهران.. محور العزة والمقاومة يودِّع قائده الحكيم الشجاع الشهيد.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/80903" target="_blank">📅 07:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80902">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boF62TQEm9yeTNbRskKe7py7iLza2BxWM99PZ1jAyVAVh4IDh1zhliJRasCowh1mM0JQJ0M87hkj8BXo-n4Mq-gsmECVhE1VQwJEcoZxWiIhABLNIvW31UpozBGa1u748S6E87deY9bx8gso-5MgaVnu5RyCp16m7qO7q5YI3q4OkV6rGXvgfuysZDjEDaCCWhuNuEPMrwZA089QbwgoXg4QzvFXPCTWfJWfy2XsJ4xRyC_imQcfs35nCJUPSclz6sTVQvcEW2X-1AfNsjy9jKeGf0mcT5Ik5MlpBxSzIhK2ol-E6yaJ20UBNKoXJIni_YURrkre-ClDZJCypBMljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
إيران والعراق، لايمكن الفراق.. العلم العراقي يرفرف في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/80902" target="_blank">📅 07:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80901">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZany8LEpf-RR50A9SkFhtID23f066sEYpC5VZ3jVk4DkZb5sQN0IX1YJFovXRABZcosNj6MgtlXKiYjX-DQrEdOO-kiufVwbEbCtDnGMQg8munhfKK-_wm70_uGGEJBhK1EyQxqdD0yYGdFXPvmMfoIgAObfJroIImXkiHyeSF77tmpfy_yEkYa4bf3SbNYRW50J91CD7Emz9dy8vQnJbOSBetRlqx9aNkIHcuZWiE91v6nwXIOCWHGzltw83pEWZ9kPQX1PCVdyytixwYBzykKqU1YXPbL7nHlh-gYD_QY7tF6Ncu9WF37eECloRWAplM3UQfqFePEVpHtrZ1uXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پرچم سرخ انتقام.. راية "يالثارات الحسين" ترفع على قبة مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/80901" target="_blank">📅 07:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80900">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd46b31465.mp4?token=qoa7PxA8nZtc2LH0HOl1RwudKPvHjRYkSagyb8koV6YYf0gt_DP_x1tX7edIivjt1mrpTFgrd3EMM7f243V3nIt57mJBGCsOhnomXcFJ6xs4SP7guCAH8ugwdUXfoZURg5d9Sq22gkjhs7EpO4nqB9Kr6KGvAXrocT5pmerC8htX7ChNL0GgJXuDJrjI3Wapu8O0uxCITQ0v68CFuUXItPME27FvTVbPDG9cey6rqtQL4nddLtK3HBX9D4vyYALDHU6jvp7dDfcO5UjwOaoCsIWAEyZZMGAphtD175wHBsehM-PH5Yp6OujkJZORJ8nWX-czsodpTsKtmpLWCztl_af2Y7B7vsD7JUZciMZVxzA6D7fT4S74zRb-CaJxdOn7b7EsqjZdHhGJDBJACcDNFfru79lwwIv4N4XMnBGBDmVojylfkAuHk9lySqwq8C-vqwcg6BCEmzp3eb9fNIBapXpaZJDigmy9wGv3rdBMFA-hixkjRcm_Q3USZhkkVLRaoHeLXO985QMO0abh8zMn-bnCmLZmETImz1nZ9zUEVXh6ojhJHSK4B3KJ1tpLg22MYbkfe_dbqe3RNcD6ukcyeaNWH_O_7uSw9Hhnhp48M56UJ0gW5PEkJL4KwC06w9YPqldMbYSO92xKb-gES7JFo8-ygNaLwNwZNvn-l--3Apo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd46b31465.mp4?token=qoa7PxA8nZtc2LH0HOl1RwudKPvHjRYkSagyb8koV6YYf0gt_DP_x1tX7edIivjt1mrpTFgrd3EMM7f243V3nIt57mJBGCsOhnomXcFJ6xs4SP7guCAH8ugwdUXfoZURg5d9Sq22gkjhs7EpO4nqB9Kr6KGvAXrocT5pmerC8htX7ChNL0GgJXuDJrjI3Wapu8O0uxCITQ0v68CFuUXItPME27FvTVbPDG9cey6rqtQL4nddLtK3HBX9D4vyYALDHU6jvp7dDfcO5UjwOaoCsIWAEyZZMGAphtD175wHBsehM-PH5Yp6OujkJZORJ8nWX-czsodpTsKtmpLWCztl_af2Y7B7vsD7JUZciMZVxzA6D7fT4S74zRb-CaJxdOn7b7EsqjZdHhGJDBJACcDNFfru79lwwIv4N4XMnBGBDmVojylfkAuHk9lySqwq8C-vqwcg6BCEmzp3eb9fNIBapXpaZJDigmy9wGv3rdBMFA-hixkjRcm_Q3USZhkkVLRaoHeLXO985QMO0abh8zMn-bnCmLZmETImz1nZ9zUEVXh6ojhJHSK4B3KJ1tpLg22MYbkfe_dbqe3RNcD6ukcyeaNWH_O_7uSw9Hhnhp48M56UJ0gW5PEkJL4KwC06w9YPqldMbYSO92xKb-gES7JFo8-ygNaLwNwZNvn-l--3Apo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
المجرم ترامب:
منحنا إيران مهلة أسبوع لوقف العمليات لإقامة مراسم جنازة من منطلق لطفنا.</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/80900" target="_blank">📅 07:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80899">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8b978849.mp4?token=hxRzcHx0ZGHRb1pwuV2JlXb3_l7U7CjGEbbTQtd4n7EbnxnjPg1smkpYIuecUt-Z6x38ap_tZFJopz7bTd6PIUChS_lQ-x9KW2f1jeVd2umY7Q1QNYXxLixv1GPQ7esgcRcFwiind9wfOiN2hyFNuyf6a3okyuAy-caTFsOYQAsjje2-muRVEm3ULmsHAQFGkX94sj9_J53eaFwlDphf-6UjIed_IMV9KfDstfsXUndIPl1gOUyFv9X6dJ1MKSInKlFTckfEHGDopKm5jevH5REgBswd82iLELNiZyfPkNIcmGXBLjPFm0FUWG_B2jQrwXBAGFJlfMNGiZVtNBRRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8b978849.mp4?token=hxRzcHx0ZGHRb1pwuV2JlXb3_l7U7CjGEbbTQtd4n7EbnxnjPg1smkpYIuecUt-Z6x38ap_tZFJopz7bTd6PIUChS_lQ-x9KW2f1jeVd2umY7Q1QNYXxLixv1GPQ7esgcRcFwiind9wfOiN2hyFNuyf6a3okyuAy-caTFsOYQAsjje2-muRVEm3ULmsHAQFGkX94sj9_J53eaFwlDphf-6UjIed_IMV9KfDstfsXUndIPl1gOUyFv9X6dJ1MKSInKlFTckfEHGDopKm5jevH5REgBswd82iLELNiZyfPkNIcmGXBLjPFm0FUWG_B2jQrwXBAGFJlfMNGiZVtNBRRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رايات "يالثارات الحسين" ترفرف في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/80899" target="_blank">📅 06:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80898">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350b75f432.mp4?token=OYa7wj5gLBWOcSiQZ8tgd8v1q6Y8uXKU-Ij9CJ83qyGeyWZuYGxPlYWEsbDHfKW70EpHVtu6vEeuMwg9nJUcBSKw2DX5H_SncPLqyTILvHdoUpBrFnWZW3V0H4KlPcIxiRIgYtDvTar-TJGacp1nQY0PKqvmk82ucBfizPSLWuh4zUEbsNE-tqEvgipHuojjwNrQmj4VBHIumDmhyV4BRad-6t0TZU1XhcEsOon5Tr7Dq0fu3GLM3NWDD28pTasfxitM0dpmDsOyc7yq--o_D0TyLvJKeMz9jayJA1GOHm1Ev-UJcPhhf9LZmfUEaveR4lk0uYEgcqZufceeOnAMlaECKgaPS0fT8Rf6qN4OlLgd8cSmLFCknJJFMngrGEJb8iCUTAcFgBCmsmnqsBFfI6_uJaCOix_zXfnN0NCNlr-KAs9RqvZnKRG8m7fBESi6aH7ohGu3AeC4CRSHrNHAJfXeJmsJsnIRtnnDhOK4zgEa6PcJnGiQ40T-OQqfScC3_10M4BNncMFF5inXDG6g6Za3bDMLJFKezYeZRG7aqoSWz04NW_ZxiEStAt9EZt3wOqCPkLpW9DCcW1tR5LGESD1i2SfbFfa9QX8vtTFuqctfPvNJwqmDBBpSl7y9N5v4CVsJp1Xg9_B2UeJmYxhZ1gBcILiNksXIhAoDZ_2xKNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350b75f432.mp4?token=OYa7wj5gLBWOcSiQZ8tgd8v1q6Y8uXKU-Ij9CJ83qyGeyWZuYGxPlYWEsbDHfKW70EpHVtu6vEeuMwg9nJUcBSKw2DX5H_SncPLqyTILvHdoUpBrFnWZW3V0H4KlPcIxiRIgYtDvTar-TJGacp1nQY0PKqvmk82ucBfizPSLWuh4zUEbsNE-tqEvgipHuojjwNrQmj4VBHIumDmhyV4BRad-6t0TZU1XhcEsOon5Tr7Dq0fu3GLM3NWDD28pTasfxitM0dpmDsOyc7yq--o_D0TyLvJKeMz9jayJA1GOHm1Ev-UJcPhhf9LZmfUEaveR4lk0uYEgcqZufceeOnAMlaECKgaPS0fT8Rf6qN4OlLgd8cSmLFCknJJFMngrGEJb8iCUTAcFgBCmsmnqsBFfI6_uJaCOix_zXfnN0NCNlr-KAs9RqvZnKRG8m7fBESi6aH7ohGu3AeC4CRSHrNHAJfXeJmsJsnIRtnnDhOK4zgEa6PcJnGiQ40T-OQqfScC3_10M4BNncMFF5inXDG6g6Za3bDMLJFKezYeZRG7aqoSWz04NW_ZxiEStAt9EZt3wOqCPkLpW9DCcW1tR5LGESD1i2SfbFfa9QX8vtTFuqctfPvNJwqmDBBpSl7y9N5v4CVsJp1Xg9_B2UeJmYxhZ1gBcILiNksXIhAoDZ_2xKNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصلى طهران شارف على الإمتلاء قبيل بدء مراسيم صلاة الجنازة وتشييع جثمان الطاهر لقائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/80898" target="_blank">📅 06:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQVRY2g0zi4c2e0Esr8b8bXGCdkrQzMrWfPB0vn0YU1gossgmgphgoQcTWDMNc9j6rYtf6kMJkIGvy_yr6_VufOZvkl9Wr-OfnQvaVgyLSqyYv5GXcag6MEFLSwnMVRbJS4qhwtzKsqKKZowSC9xevb_kFTFq8G89prMUQWoZgPgPdh4lDXmmBIKj3Fqbo19Turt0BfYWeq_NeDnZm5zR6I9s6x-q0BySj5ruc9oeUiozvT-rB9LL0Bl2enJYPb1_FA4EZHhV5xUgCBWtEzqN8Vdx9HEKKLGJCEfMZu60IPAxW8f8v4JURc16WJjl4tLA2yYBjgoZbxBLh77zpFa3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGicGdP3YUXGhAu7xLi0y7hLKMcw7tY0_W9asxyQgoLDMVwUw7fDxUbKYFc67jowUapTbKPbhN1sKEWP3Z5t2BcsuCeBe9gI8b5QxYF832b9jYMUBgM-Cen2sq8oCpqhi9ZzcfihEjCNCu_sv9r_gBR8JeK14naPY9m67mczKcWDOgWn-OpxFF4Yjv5LYqKRe2VXpGH1SiwA0d6QVokLbgcn7wZTSfyXeC2rrSHpXQuhhFm4IOe8_QPlYaPgArtl-cvpwxG6WcM4_OIk2YTbdBmoUcREzz5xO--8zWDz5tV0HOfRyw44dvgL3TRuT812lIIVBAJGRhbLSBlMgnRu5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4136e83b6.mp4?token=bg5hJ9uhG1KhVCqiXxekWftDuCwhtel4KGzyWWs-pXz9S3VxJOih2axNf8hKGF9bMGWD-alnpCElXPZY3ek6H68kOocfQx6LmvC77r6kLsGPtdKPMYpJxuy9O6HmNZpuxg33ourYofOYBjZ7nLYreVq0rQ1nbElD3FpYj2zPYGz9YDKOSLBr8MeXSkQvUIjcYEvXNdZtujuWuCCXMCnUFjGa_CeB3s7Q1KIkLE1r8n8c4WnFjHjWTqszOMcXl02y4mUhdcR0rNoWf6_yA2fAhhMJZ59J0LwllZFxrGSVUEu1fItPs5CcKfkGcMZmc6JRSPsFUNtoSgrCO1whYE0-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4136e83b6.mp4?token=bg5hJ9uhG1KhVCqiXxekWftDuCwhtel4KGzyWWs-pXz9S3VxJOih2axNf8hKGF9bMGWD-alnpCElXPZY3ek6H68kOocfQx6LmvC77r6kLsGPtdKPMYpJxuy9O6HmNZpuxg33ourYofOYBjZ7nLYreVq0rQ1nbElD3FpYj2zPYGz9YDKOSLBr8MeXSkQvUIjcYEvXNdZtujuWuCCXMCnUFjGa_CeB3s7Q1KIkLE1r8n8c4WnFjHjWTqszOMcXl02y4mUhdcR0rNoWf6_yA2fAhhMJZ59J0LwllZFxrGSVUEu1fItPs5CcKfkGcMZmc6JRSPsFUNtoSgrCO1whYE0-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
إيران والعراق، لايمكن الفراق.. العلم العراقي يرفرف في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/80895" target="_blank">📅 06:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80894">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYAtmbFiqXi8FvUVMKIHo8J0lobI5KS4DRRu_O7pcT09Wfp5IlYPS915jUEdXTqIMW9-VDXJXqxRvkdvMsMunyzF6xt-9MWxzlh-_75H6gdLgG3fcobojrbfo_RfXhDP7BmGhBppKSGBURASZ8sGdi9XP-6OVR-t1rYQU20_wg6bY2fs_HVOSK1CNy9XM_gAt0dpUP33Dgs7hEjB2uJQr9Y9pd3XG2Z2lZLc0J1pQIFRcV8SkStlAZIKyvSuvlyf0rzjmnt6Soga01FbknS8dXemZeWaONupBsVwX_-GKMH_56bgAZ1Ez2krz0wBD5nXdaOlfzxVfCrBXRc8LqamAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الآلاف من عشاق الإمام الشهيد يستعدون لإقامة صلاة الجنازة وتشييع الجثمان الطاهر في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/80894" target="_blank">📅 05:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80893">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d4462b1d.mp4?token=nCqTmqVKQMkLDgkxDqE5Ya3zuNOOpcEK8DafoMvAT0JSv_qh9IhvkUAEUfVvw2rZcjILD1S-x_bhky-WMW33hPVqo6fsW8r3QVnbEv0tzmuJYFtvXtOvSsHH7fad_WhlXaX_HNsM66zQDkJqXEmfpJapUEdkVCNNAVx0KuCYW_wY4NuON47T7XrixN6f1V_MJNO1tnoAGchnD3d2LMMUOpsw3lB8YJsHIIacIzife4AEkvZHqAfWibmM4ZdI8-TV21qkUsUbzwy0nx_fwk2wXuUd4YMMBG6kjE13qQoBP2z41rAkjOQVB1By02WQ5CjtUvBwaRLqnItJgHKcPaAPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d4462b1d.mp4?token=nCqTmqVKQMkLDgkxDqE5Ya3zuNOOpcEK8DafoMvAT0JSv_qh9IhvkUAEUfVvw2rZcjILD1S-x_bhky-WMW33hPVqo6fsW8r3QVnbEv0tzmuJYFtvXtOvSsHH7fad_WhlXaX_HNsM66zQDkJqXEmfpJapUEdkVCNNAVx0KuCYW_wY4NuON47T7XrixN6f1V_MJNO1tnoAGchnD3d2LMMUOpsw3lB8YJsHIIacIzife4AEkvZHqAfWibmM4ZdI8-TV21qkUsUbzwy0nx_fwk2wXuUd4YMMBG6kjE13qQoBP2z41rAkjOQVB1By02WQ5CjtUvBwaRLqnItJgHKcPaAPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الآلاف من عشاق الإمام الشهيد يستعدون لإقامة صلاة الجنازة وتشييع الجثمان الطاهر في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/80893" target="_blank">📅 05:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80892">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9d564211.mp4?token=Zyrxqydi_v_Ot2YpKnTB-r40ouA_VQRoN210AIS9NZg99Y6hf8MnR48egKmd9PhnufnqJQz8VXJzI56InX8DuKpdWZM3o8FAqKwpuoT_zJf33hfQwPQzlBmCulEJ9t9oN0EC5tOQ4uCUlql8lGU-uIsJRN5UjB4zVvaZSyQ68NVyNqf9rDWmajp1eHYl2H0sDRTdxf2wvTUG79Usr7_bh1cYE7bqc4L78PhEwPBwDOR-VTxss7_ny3KPKa4ihb3R4bzrkTf-Zhhq9qfRw30t_F1cqgpHIzbrGYQSbFzi2Im8GIu91MEzbiOWlf3nKxoTetQqraYDx2Oh4Z9nLAudOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9d564211.mp4?token=Zyrxqydi_v_Ot2YpKnTB-r40ouA_VQRoN210AIS9NZg99Y6hf8MnR48egKmd9PhnufnqJQz8VXJzI56InX8DuKpdWZM3o8FAqKwpuoT_zJf33hfQwPQzlBmCulEJ9t9oN0EC5tOQ4uCUlql8lGU-uIsJRN5UjB4zVvaZSyQ68NVyNqf9rDWmajp1eHYl2H0sDRTdxf2wvTUG79Usr7_bh1cYE7bqc4L78PhEwPBwDOR-VTxss7_ny3KPKa4ihb3R4bzrkTf-Zhhq9qfRw30t_F1cqgpHIzbrGYQSbFzi2Im8GIu91MEzbiOWlf3nKxoTetQqraYDx2Oh4Z9nLAudOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مباشر من مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/80892" target="_blank">📅 05:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80891">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgepij0w74SZtaygZOdf-7gQopqMNGYu7ZDNyGbhn0jJY33Li47BQN2HSJCIYHrU44Tdt9JkZf_mJ9CMhCed0F3K7_XnAOMDjQ2NdNOe-16q6bk6iOgrLFdIanrgmTz-kwLlD7lWVV-RGDXjQUdQfMo3IXj7HTnI7kQr9WPPaY-Qe-UGQlZis4soCfHrIUQN_O9r5cYX8NZh0ncUBeclx-9o3ofZrhyXOe66wM_EQjk-3NKRU9KmlQC3KytHwotIthFMwiLj2ldSRmhGpO990IAd22IRN9T9h6dbPePsXGnZR5hLSO-nyToWiLYW9efxBDedAIcUswAmSKCnucmt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رايات "يالثارات الحسين" ترفرف في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/80891" target="_blank">📅 05:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80890">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX7qLI6tgEEr2zjZDN7nXwrSwiwtKmmR83Y1vBt5yf2GUTfo_kDejnTUQm-4A_3xmZPfNsmhhEYtxLGuOqwIMG_ISkdqMW1VRJ2am62IJqaSFGKZM0-1_IMrKYJOVTGsbgbVkAUktdGEH4S3T4pFF4RVkJODBZfWk27-mkbN2FDHtGEX2TDr2AfTDzX7jKygjjwKqUgH8_YIRQ7CWx9rInqMPO4DdAqgiGsYLHQ2-RVsrAnkqdU8ju_LCTthJg7VRpOfPbavmpIlMCfHZD1Vdin6_vxuz2BqiJ-wUheFcdkUpPtwoueLdt5QPKJ1mnm_DGGdFw-ShyvH0_InihU9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعة ويبدء الحدث الأكبر.. الحشود المعزية تستمر في التوجه نحو مصلى طهران.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80890" target="_blank">📅 05:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80889">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7d3170cd.mp4?token=TgHXwfm0oVPT-UV4xMWsXAAsBhLz0yxx72-_zCXSW68VFwtsBWjuXBoiZ8k5KqO6ZHIMvLwntP7ptOQgYEC_g5TPbP0IN5CQL9fEfV6ouHF8WsiLH7mSwij7LLG6NTxAOhVLXlMgcAx9UaGfWJcw098wRrsFNgrksiH9NZbFzLkER0SmBQXSyEPxZfmLzv_LFGpliLHbLKbXWWDwOaJbrqpgnXa8aHTa0sPodN3j4jggxDWgsQ4JLdbtkSkTc4K1PSHc37d_JSH159TrSxD6Hcqmw9ZWs3AxxHmDrAOjoGqQSc6gzXQBJq2i1KOjsYJ_g2U3CfOr_bMYlNe4KYlcGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7d3170cd.mp4?token=TgHXwfm0oVPT-UV4xMWsXAAsBhLz0yxx72-_zCXSW68VFwtsBWjuXBoiZ8k5KqO6ZHIMvLwntP7ptOQgYEC_g5TPbP0IN5CQL9fEfV6ouHF8WsiLH7mSwij7LLG6NTxAOhVLXlMgcAx9UaGfWJcw098wRrsFNgrksiH9NZbFzLkER0SmBQXSyEPxZfmLzv_LFGpliLHbLKbXWWDwOaJbrqpgnXa8aHTa0sPodN3j4jggxDWgsQ4JLdbtkSkTc4K1PSHc37d_JSH159TrSxD6Hcqmw9ZWs3AxxHmDrAOjoGqQSc6gzXQBJq2i1KOjsYJ_g2U3CfOr_bMYlNe4KYlcGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار "الموت لأمريكا" يرتفع من مصلى طهران قبيل بدء مراسيم تشييع إمام الأمة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80889" target="_blank">📅 04:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80888">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724637f597.mp4?token=gl4UJgsRXzEiTBfrriScyBkxXgTIqwQbjeavCW3f_zFGhf4xnXpuS9XdIdEbGzdaruGq54uM-os7IvNcio6qGf0Y2_dN3b3R0L49OaHlCIOMIvc90YxLGJd1X3kigyKt4hx6TUSqRwV5Ll50ZCtZt7iP0k-qR0hWKtK2ShPStA8wwittzSGHwOIiJUykWPzfh7MpXcjXoJkW2gJAuGmUWdpQmH8W1i3pVU67XhMUx008V8GShHf-Rb1rc4Tj0FOOkqyZNyJ1l70oeUuHJ2lrekVE-rabGv0hkoH6-I_uYlKADtf9BdGWJl_wTFL8rjz9qaKNfN-7CwR4yz7xUjB7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724637f597.mp4?token=gl4UJgsRXzEiTBfrriScyBkxXgTIqwQbjeavCW3f_zFGhf4xnXpuS9XdIdEbGzdaruGq54uM-os7IvNcio6qGf0Y2_dN3b3R0L49OaHlCIOMIvc90YxLGJd1X3kigyKt4hx6TUSqRwV5Ll50ZCtZt7iP0k-qR0hWKtK2ShPStA8wwittzSGHwOIiJUykWPzfh7MpXcjXoJkW2gJAuGmUWdpQmH8W1i3pVU67XhMUx008V8GShHf-Rb1rc4Tj0FOOkqyZNyJ1l70oeUuHJ2lrekVE-rabGv0hkoH6-I_uYlKADtf9BdGWJl_wTFL8rjz9qaKNfN-7CwR4yz7xUjB7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنا مصلى طهران حيث ينتظر العالم أجمع بدء مراسيم تشييع الإمام القائد الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80888" target="_blank">📅 04:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80887">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgQc4vCa8ttJ9RkBjzJg_Cmly13qTVPaq4xzc9ee9vt1QthlLDpgAgGBNHTJ8Gez3l_XAJ9fNlkdbh8UvoqifhINtsLTS3DY4gBlBguyPMkG5XDIHASSS17yHZt8XKpo3SxcXtxaCcWxp7xs7akXlMyRfPDhydR8-RMtCpBdF6EoxUd4Q9XtUdSjNgucKiktmS8zaXhvG6dxEXIo-zic7rcN0mTDej1XsNJGnOc-XFxg1wsS4agDwEHr__czzugO2sz8HUPxYStFVDqFu2D1k8CzLNfKgd7CvGhPGbtiMCxr95dUKfseDpUVOn06_1LgJo1_piJIDhPfi3YeU_oM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرق میکنه با خانوادت شهید شی یا با خانوادت فرار کنی.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80887" target="_blank">📅 04:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80886">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6baa49ce.mp4?token=TIQ_YlyC80Elb03sP5PynReMShiZQSRxBdQ67rmDSOWsihO4zz8kFH0KHlMDsWorqvRRpWA7y5d-_wWy55q1pEh83lPrkZMtNyH_PWWyxRyKDO6cXGp0DR2nUXE0XLIacJ7lJzRaKCJ3q6tkmuzLVQrehCDffRBgaj9HgTTDpkv7bp2g9_GvRNDd91HlPb2GZN8_t9OTWL5Z2ufA6t9PsYLaDAafwoSH2y0Gccp0jPI6NBnqa7uvfZBDczvcJunIpdzRWnuzXC4r_tyfFERDi3wxd4f0LsBDPvfBXl0CdazcLJVxojFtRWCi8PnXEZlPQTiENSZ0IqpdioML9MZSjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6baa49ce.mp4?token=TIQ_YlyC80Elb03sP5PynReMShiZQSRxBdQ67rmDSOWsihO4zz8kFH0KHlMDsWorqvRRpWA7y5d-_wWy55q1pEh83lPrkZMtNyH_PWWyxRyKDO6cXGp0DR2nUXE0XLIacJ7lJzRaKCJ3q6tkmuzLVQrehCDffRBgaj9HgTTDpkv7bp2g9_GvRNDd91HlPb2GZN8_t9OTWL5Z2ufA6t9PsYLaDAafwoSH2y0Gccp0jPI6NBnqa7uvfZBDczvcJunIpdzRWnuzXC4r_tyfFERDi3wxd4f0LsBDPvfBXl0CdazcLJVxojFtRWCi8PnXEZlPQTiENSZ0IqpdioML9MZSjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح الأبواب الشمالية لمصلى طهران.</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/80886" target="_blank">📅 04:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80885">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
توافدت جموع غفيرة من مختلف الإثنيات والقوميات والاعراق إلى المصلى للمشاركة في تشييع الإمام الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/80885" target="_blank">📅 04:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80884">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS7NLTGQn9Ki_yX4-fkWITmsW8nxZUy_QSboT6f1gE5mbm8CetS-O7Jkj3YUOIZPf14m0uhlyMkuKZQsB4LuS_SdSuC2id1o7BNmUXfvq_4JCfGSwCzfV3MnKoZkwFm4xBQn3NGezlo68bXL1TL3toGZ2uSLgr9b0IC3666abFbkz41xYQcEUGLUNEcAzD00JUc7WM2acLUJc6uj6fWqrKzl3Ymo5SWWbEiocbnwCNjLmHkh4B7ecBK3nLFezm6f0nP_h8pgHuFy_GY3xYwUpj4pcG3oL7SxEQ2tjaYzx94MVlvnQCWHc_iZmSMJXCJV6372kZRZ8_u1qbNzidJrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بدأت جموع المعزّين بالتوافد إلى المصلى.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80884" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80883">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e25fbbbe.mp4?token=QMEl6E_snXCFT6KUDR6pcjzwJWGHJWtLKOFaySJT6HAp7dkHshg-BS4Ce_y6B66HTu9SAdrs_7DE3XgaF0fZ-yql2Kvv5wvShQg8mzOXFUcmduANQPWxrW5zJzmrf7vZguFfQBrQ4_cAEzYzj_IXIRXl_sVS8ejCZL6RyN9muY2hhcR13dyDERWL9UEJCByEDwPhmGst5k7EFcWM-J_QIGa5f4AHlevHyxp1JzLh0TH_jfMqKBYmYY38_PKHCWjv8hPzoBlwzgWrCYU1Ok_xfBYVZ4r12xcHgNqPpEowZfUw2w_nltRc8ahslJ0e-VjUIuA1PI9KvriPPVjWDMJiZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e25fbbbe.mp4?token=QMEl6E_snXCFT6KUDR6pcjzwJWGHJWtLKOFaySJT6HAp7dkHshg-BS4Ce_y6B66HTu9SAdrs_7DE3XgaF0fZ-yql2Kvv5wvShQg8mzOXFUcmduANQPWxrW5zJzmrf7vZguFfQBrQ4_cAEzYzj_IXIRXl_sVS8ejCZL6RyN9muY2hhcR13dyDERWL9UEJCByEDwPhmGst5k7EFcWM-J_QIGa5f4AHlevHyxp1JzLh0TH_jfMqKBYmYY38_PKHCWjv8hPzoBlwzgWrCYU1Ok_xfBYVZ4r12xcHgNqPpEowZfUw2w_nltRc8ahslJ0e-VjUIuA1PI9KvriPPVjWDMJiZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إزالة الأرصفة الجانبية ومحطات النقل والحواجز المؤقتة بالكامل، لتوسعة الطريق وجعله سالكًا لاستقبال مواكب التشييع.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80883" target="_blank">📅 03:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80882">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmAafbyk3-WkkaYoS6d0jZWdABT6aVjfpihCJOBmsz1ip_ga07Dkr62PRUB4Rk_F9KJKWVVKOyU7kVgLuE0C4QbL0bGew5v5FSYPnh_CtriJ7tlWkkvQSyfUz9tM85fZoNScecj4bRAN25FIJUcfPHByu3tV0kdhSSWN9EcH5XhmDz53NxS-3yw2utkD0L_U_lCd-j-355r0cuoB50d-OY2aV5GpSOjF-w19cy5wAC0z0Zhg4NeYV891M4vnS6AQF8FHzV4Q0-xnotxy4zIfXVZOhujRRGvYMzboOI9NQYt85LE4W0ybyw3YteMWLD7zYDNSO5NYFRf0d6Hi1pdcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
من المصلى توافد المعزّين بانتظار مراسم تشييع السيد القائد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80882" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80881">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11361885ff.mp4?token=UlGSMRYX2jCP7Z26_HZqPfEBNLLNRvHi8VP2sp3LjgEINyynQWHDif6qjm4UHwIHRLRncYsQBhJo3JyaWcxnFKGBRF2ASjWzvniR9HDBFhnX7Oh5tHkQySxX2HJHRsOF7iOof47PhvP7yecXPdE5xs-MOk7wpeU-ZFs7tdOgSgXsi_gS4UC7p7Nc8xSy94L0-8E3Bwzwkrf54aOKRoU8jtTzC2apsib-nPOqZD0b5TSkLmehG4HySQEUUFuutd0agkAXJ1U6ShaKLyShDyMTYOFxC6PTPXJTQcxqP5wl275OhkfhiHGs9ZSIO0fXNgLLfgCAEfL6hYVaW-V2jboT3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11361885ff.mp4?token=UlGSMRYX2jCP7Z26_HZqPfEBNLLNRvHi8VP2sp3LjgEINyynQWHDif6qjm4UHwIHRLRncYsQBhJo3JyaWcxnFKGBRF2ASjWzvniR9HDBFhnX7Oh5tHkQySxX2HJHRsOF7iOof47PhvP7yecXPdE5xs-MOk7wpeU-ZFs7tdOgSgXsi_gS4UC7p7Nc8xSy94L0-8E3Bwzwkrf54aOKRoU8jtTzC2apsib-nPOqZD0b5TSkLmehG4HySQEUUFuutd0agkAXJ1U6ShaKLyShDyMTYOFxC6PTPXJTQcxqP5wl275OhkfhiHGs9ZSIO0fXNgLLfgCAEfL6hYVaW-V2jboT3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أجواء مصلى طهران، قبل ساعات من بدء مراسم وداع قائد الأمة.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80881" target="_blank">📅 03:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80880">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80880" target="_blank">📅 03:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80879">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOqfVi1AQCda82eo5s2MXE_0LVs42pX8oNLAd1ptcGedgVXRozydaty1Jvii90KQ4zYMGVe678fFOAkis72J5wmglxCx5_bzA098rJmrK-ZfJ9e1zueAL1Awy8jZ5vVGA2GRxsmP9_OfCB1xLcg25nrOduSa_htGGQp6USDi3NfUB1Mmqzn7yFYRXYQO-9moz6aJraKV26vAW2yaTZXM4ua1kB7-9Sj95WcNspa7R3MpPv2CeqdNHPXD9W9PtHugzhrbl2tQ0xOBXs21ZQ2t8l4P854l83Lxt11sXwmMj8TF2e3W8tFMaKi1CnXzEDoi7G4DYx55YTodbOn1-a8L5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ج
مهورنا الكريم ؛؛
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80879" target="_blank">📅 03:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80878">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3b269ce8.mp4?token=UYaMtx_M_d44PSRvmeUq-FUhjjGMyQu0G5nje_v6Onjwifr-sZpfl2ChQgudbPswthA6pyqLDc8yLYXn517EX_DVQ2h0g_dFYGe0q9K_ijRF1SDaEXbhNnBYf-3qSk7j6TjQaxnL5i3iuxZbvRNBfxIXEQ5vQ3vW43BVGPyhcsukS7PjjgyhSuKHJpVjbgis8oUJvlQbBY75KY-l_ZKeruyByzx1UmyJu4llfiBaM5vVrDYEgeN3wboNvmLCMBbmvSFQhv7PID1Mrpp9iq9Ovmie-3-QFwAODeJzCRjitRjxUMjUqmyIekwQ1PmfoHPvkfZ4UQ4LiIofKjKvqkn3sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3b269ce8.mp4?token=UYaMtx_M_d44PSRvmeUq-FUhjjGMyQu0G5nje_v6Onjwifr-sZpfl2ChQgudbPswthA6pyqLDc8yLYXn517EX_DVQ2h0g_dFYGe0q9K_ijRF1SDaEXbhNnBYf-3qSk7j6TjQaxnL5i3iuxZbvRNBfxIXEQ5vQ3vW43BVGPyhcsukS7PjjgyhSuKHJpVjbgis8oUJvlQbBY75KY-l_ZKeruyByzx1UmyJu4llfiBaM5vVrDYEgeN3wboNvmLCMBbmvSFQhv7PID1Mrpp9iq9Ovmie-3-QFwAODeJzCRjitRjxUMjUqmyIekwQ1PmfoHPvkfZ4UQ4LiIofKjKvqkn3sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ثأرك جمرةٌ في قلوب المؤمنين لن تنطفئ وذكراك ستبقى حاضرةً في الوجدان يستلهم منها الأحرار معاني الصبر والثبات كجدك الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80878" target="_blank">📅 02:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80877">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114b80e11f.mp4?token=BWN8IUnRie4G8xCnvrn1VGdcvnEefV6TVqDdS8jsfdXQEdnIBOti9ydUcQTtFe-PPg2zKHG0gGOJaBqhrpacUiGo5gdaWwLFEJ41G2DVsT1d05TZNTdrvbDUQQoOiwc2LohtGpqj1uz_AGBiulHNgeDOcqelOJGMV1CYOJETjpPC_og1ur_uDrp6jV1O-Q6xXTQVAIoLT5z9PoXIv193hSGegmh4eJzfWDGcz3btfD1KC7gVIeENt6Fz9n2alvTVZ5n-XXWqNyVpz9vTbZga86l_iOFrjtzAOAGY00GoMTWegFKt0eVp1vBMC-TgHFdi03G32MVN5OPxslWgu-dxiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114b80e11f.mp4?token=BWN8IUnRie4G8xCnvrn1VGdcvnEefV6TVqDdS8jsfdXQEdnIBOti9ydUcQTtFe-PPg2zKHG0gGOJaBqhrpacUiGo5gdaWwLFEJ41G2DVsT1d05TZNTdrvbDUQQoOiwc2LohtGpqj1uz_AGBiulHNgeDOcqelOJGMV1CYOJETjpPC_og1ur_uDrp6jV1O-Q6xXTQVAIoLT5z9PoXIv193hSGegmh4eJzfWDGcz3btfD1KC7gVIeENt6Fz9n2alvTVZ5n-XXWqNyVpz9vTbZga86l_iOFrjtzAOAGY00GoMTWegFKt0eVp1vBMC-TgHFdi03G32MVN5OPxslWgu-dxiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ثأرك جمرةٌ في قلوب المؤمنين لن تنطفئ وذكراك ستبقى حاضرةً في الوجدان يستلهم منها الأحرار معاني الصبر والثبات كجدك الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80877" target="_blank">📅 02:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80876">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a191d7a6.mp4?token=dCXr4MFiRO_ISRy-3vyOrlWZ0NntLjyGT3krHQuVL5ehH4d_MN0EeN3RUFuF51eDxVMQzv0TXnhy4YIBgeyPy5dj6pHdgbZVbGfhArGoKtHcNEs3b7tREnaOEGby8PlRp92Fk4GSHWzXi7_C8FVUWO_fcsrIDuvjn2Wc67JJJ4t6uflXdHy_m4aRIcjm1UsjC9rj1e7_1a5WVPwJbrKck9_lNjP3X0iQa-4Afrxar_a-TtCbMq9se3BGQ0q5ZSRfLSA333K5TSnE3-WVfvQ5ejCR1O_LoMMW4oI39iKfMyCzF4RU3JzVtGcDul2PeoHqpSpCBL7Ahr0YcyLfK4Bt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a191d7a6.mp4?token=dCXr4MFiRO_ISRy-3vyOrlWZ0NntLjyGT3krHQuVL5ehH4d_MN0EeN3RUFuF51eDxVMQzv0TXnhy4YIBgeyPy5dj6pHdgbZVbGfhArGoKtHcNEs3b7tREnaOEGby8PlRp92Fk4GSHWzXi7_C8FVUWO_fcsrIDuvjn2Wc67JJJ4t6uflXdHy_m4aRIcjm1UsjC9rj1e7_1a5WVPwJbrKck9_lNjP3X0iQa-4Afrxar_a-TtCbMq9se3BGQ0q5ZSRfLSA333K5TSnE3-WVfvQ5ejCR1O_LoMMW4oI39iKfMyCzF4RU3JzVtGcDul2PeoHqpSpCBL7Ahr0YcyLfK4Bt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصورٌ كان يوثّق مراسم العزاء على السيد الولي في مصلى طهران اليوم لم يتمالك نفسه فترك الكاميرا وانهمر بالبكاء تأثرًا برحيل امامنا السيد الولي.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80876" target="_blank">📅 01:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
مجلس محافظة واسط يصوت على تعطيل الدوام الرسمي يوم الاربعاء المقبل وذلك لاتاحة الفرصة أمام المعزين للمشاركة في تشييع شهيد الأمة آية الله العظمى السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80875" target="_blank">📅 01:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d4d82aac.mp4?token=qBBo7iABubu8luJizRDxVJKhn-fkFVGjXNJGwO4BUb-iyQh5H0NhIjWi0w_IDxJdznRJCgQe98mTSiRbYSV7KuhczTldRTmgFoutBDNLUZvU3EOIBBkHIQkGUrJtFNeIIUm3bk4J90lAk8cCl90H3uzSbtzbcZSUR2NgqFy_plx5swYOyfq8-LDI2O52y7WuNEjY3HRkwfPmgu0bRaRsaAjAQlHr1ZYVDdBuQRMqFSCebRqk7st2TD7IVIX4BpeXaanSR-1-FfOpmafFUXg_PNH0cqDFQVe0QWDju8YcOXqlzwLTOJQ4T9Qjz7FRM25AMVVETXWv242ULwtlPlVnwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d4d82aac.mp4?token=qBBo7iABubu8luJizRDxVJKhn-fkFVGjXNJGwO4BUb-iyQh5H0NhIjWi0w_IDxJdznRJCgQe98mTSiRbYSV7KuhczTldRTmgFoutBDNLUZvU3EOIBBkHIQkGUrJtFNeIIUm3bk4J90lAk8cCl90H3uzSbtzbcZSUR2NgqFy_plx5swYOyfq8-LDI2O52y7WuNEjY3HRkwfPmgu0bRaRsaAjAQlHr1ZYVDdBuQRMqFSCebRqk7st2TD7IVIX4BpeXaanSR-1-FfOpmafFUXg_PNH0cqDFQVe0QWDju8YcOXqlzwLTOJQ4T9Qjz7FRM25AMVVETXWv242ULwtlPlVnwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بهذا الوفاء لقائد الأمة، انتصرت إيران</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80874" target="_blank">📅 00:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in4rShlKBsgnSZYxzSEnKCiUOR7rt1Y2mLLWB8GP-1ukhHKnyeWPfaViaQAXDYtAyOHvnEfNii8k3uKtq8EFTt9622WxpUMgRPrL9HZmXOULWFpxiIL0_I1k5qBH-wMApGeO5lWda4D0WhzeecPkBqwi65Xgm3Oac7CWqk3nBpMy51KNZL0JNqbbPSrqlIEIr8yD-8aWopINMZURy8MtQ_B3BxBTGI-ojappzcpwqmyxluvgFW1eDrGhXY5IwMLrc93COoEHC--MhSSKCRoDsp5c8R22IsLclmejBrTgNfmVqzcqNxwTl0Ogkf6BXu9PFjGXJKbkEFkIPNn1cDEjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اللواء وحيدي يزور مصلى طهران للاطلاع على الاستعدادات الخاصة بمراسم توديع جثمان السيد القائد.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80873" target="_blank">📅 00:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
‏زلزال بقوة 5.5 درجات يضرب قبالة سواحل وسط تشيلي.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80872" target="_blank">📅 00:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eff78cbb38.mp4?token=T0YbE4icw08j0LgmVaZQyupG51SRZsjEZxX22bcqIqIk0O8rL1BVFiR-06xE81MlU8Gw6aX7bv6iN6gSIaxtWbmSUHfRcMOUFDps7eZSExoHP6_NadLKGdMWHaj1HbrijZsO-P_a2OAE_xtW2hnvL2FH4PrOSNDqFaELoc4gzQ_juJx2g8XFOzvZLZGZHk63r6rB9Yoq1WV4wJfvQhaQBGZZVDobV1Zt7Eo-sBCK4z9RDl07ROZN4lpq1htJjI-cKp_LQrAdkZBAkoaqzXxGnYCByP51ULLEsXjIfgNcmeDuI4LPblLrl8PXtFgG6HFpgkq5lyFOWSCwYkmF4F20S4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eff78cbb38.mp4?token=T0YbE4icw08j0LgmVaZQyupG51SRZsjEZxX22bcqIqIk0O8rL1BVFiR-06xE81MlU8Gw6aX7bv6iN6gSIaxtWbmSUHfRcMOUFDps7eZSExoHP6_NadLKGdMWHaj1HbrijZsO-P_a2OAE_xtW2hnvL2FH4PrOSNDqFaELoc4gzQ_juJx2g8XFOzvZLZGZHk63r6rB9Yoq1WV4wJfvQhaQBGZZVDobV1Zt7Eo-sBCK4z9RDl07ROZN4lpq1htJjI-cKp_LQrAdkZBAkoaqzXxGnYCByP51ULLEsXjIfgNcmeDuI4LPblLrl8PXtFgG6HFpgkq5lyFOWSCwYkmF4F20S4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
الشعب الذي وصفته بالشعب العظيم سيُشيّعك على أكتافه ويحملك بكل وفاء ويطوف بجثمانك الطاهر في رحاب مرقد الإمام علي وأولاده الأطهار.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80871" target="_blank">📅 00:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">أنشودة
#قوموا_لله
له بصوت البحريني محمد غلوم..
🏴
#باید_برخاست
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80870" target="_blank">📅 23:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Occ7GG4ZnJsCnDdfsReOwaicg9QXsG5BI9mvuFqCVOGm6CpNs9gZsnpfdjVhuOQaDrUoHFBGmse454njuDDfiQiV9WYJ4UizBRoAx-vPzui3_1nlB5GTdPtEuoQueL35nLQXGU65qiAd4HHcghhu0tDUl22jsraerLG9-1SjJvyeL3KD8ZnYLi_BHZA8gUqXqwOWn-XM0Ee1kwVjwKWR_MlT37vJ0ojhlIs6jfkcpkCIL15q1O-HOL7HcEy2Yf5SokG_dS_oSLrPCvNwxsrnwnbA8OnGwiLrMT38TDFTv-POTSb4E5KXIITAPcV110LDw5eJyqeWXlv-9oOpQQ6Tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الرجال الأشاوس الذين لم يتمكنوا من حضور مراسم تشييع السيد الولي لبقائهم على أهبة الاستعداد خطّوا عبارات وفاء للشهيد القائد على الصواريخ الباليستية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80869" target="_blank">📅 23:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9b039651.mp4?token=sW8gZ_aF9I079vVk2mL7gnwUjO8zpq_8_hEL6ZABMFMmGos7cgjEC0KnBSkn3byiO4Ij7oy0fTSII1VJyyEj5RD8rEU4aRWHO3baE73K-ZxQt5ZaOU6bAj4nWvxW9rF5zzdZosMcwCLCQLPBHu2pWjYJUfilV_3NJRqsy8Ugdg8ruoeQBAnnUTduRs8lv-DXRtNadcYmt_3baUdbkEuxwEK_GvubjDBpwlJYYbNKzwlnYxUTqNGSZ04SfzFUzd5D-Rm6gdytBlJYyS5X6wrbqsq0TG-ivYhi-gQ7YYR1OypUWMcJHswrF9PJRUsxER2-85H-Pk5u02jBqqMjvlkZJxQw464jhCU_MpGxp55RqXbFecre0nQs2Tt4qUYlbLr5u4qXoCl-9HJxP0TzaT6KG248nq5ysAYfwUgT9LC_Rhdz5vs3QHN7JmSDhB0xE40R8CPaNXAtFOSzSol-gufU0lcfnGYSjmU6RlG5agMd3aJQSVc63LeLFb_NLhHEQAsCAjN7MkqyJ2dg7cR2ZlXolj_LIcC5kmS20TKVvWTDjeOpTaOHbPft3wif1TEh3fbxWL08FaAurt7E7Vsv6Cxceyf3zlSox31IhQWHJXUZXIypN1fjVa_kOlCRpI94wCa0qdhAtpQ-Z2SGmwuzHP--CKpYp0ukUDh7moffeSMD_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9b039651.mp4?token=sW8gZ_aF9I079vVk2mL7gnwUjO8zpq_8_hEL6ZABMFMmGos7cgjEC0KnBSkn3byiO4Ij7oy0fTSII1VJyyEj5RD8rEU4aRWHO3baE73K-ZxQt5ZaOU6bAj4nWvxW9rF5zzdZosMcwCLCQLPBHu2pWjYJUfilV_3NJRqsy8Ugdg8ruoeQBAnnUTduRs8lv-DXRtNadcYmt_3baUdbkEuxwEK_GvubjDBpwlJYYbNKzwlnYxUTqNGSZ04SfzFUzd5D-Rm6gdytBlJYyS5X6wrbqsq0TG-ivYhi-gQ7YYR1OypUWMcJHswrF9PJRUsxER2-85H-Pk5u02jBqqMjvlkZJxQw464jhCU_MpGxp55RqXbFecre0nQs2Tt4qUYlbLr5u4qXoCl-9HJxP0TzaT6KG248nq5ysAYfwUgT9LC_Rhdz5vs3QHN7JmSDhB0xE40R8CPaNXAtFOSzSol-gufU0lcfnGYSjmU6RlG5agMd3aJQSVc63LeLFb_NLhHEQAsCAjN7MkqyJ2dg7cR2ZlXolj_LIcC5kmS20TKVvWTDjeOpTaOHbPft3wif1TEh3fbxWL08FaAurt7E7Vsv6Cxceyf3zlSox31IhQWHJXUZXIypN1fjVa_kOlCRpI94wCa0qdhAtpQ-Z2SGmwuzHP--CKpYp0ukUDh7moffeSMD_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد الحشود المعزّية إلى ميدان انقلاب وسط العاصمة الإيرانية طهران للمشاركة في مراسم التشييع الرسمية للسيد القائد.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80868" target="_blank">📅 23:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
رسو ناقلة نفط عملاقة في ميناء البصرة جنوبي العراق وأخرى تصل غداً لتحميل 2 مليون برميل من النفط الخام.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80867" target="_blank">📅 23:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11a685fe4.mp4?token=Lx9PRq_ivv-MMYtkD4j-alARPSpqobGoIf8JyArWtj6b7oWmR3PdBA__boZKf2yFnA43bb1k5X2FuVCAB4R5Eb-__NGj5mC05k6PXdwUvxlNTT1suvM9i_5sire4GKxNwsy9j4Ax0qUt3JgH57Zq_KkVLJ9tofspn-HftkoEWQ7xGQlFDmXD9_WnA2wOxhTjrnDR3FJ7zF0EugVgPUrTwmmt_iEbUJTm2xKtfJM6cGDxTuc8omymaZFL5tZZhMJ8GOPBcTPvFyFl2Q-7JKc2Pk0aRTMNtRLj3hjDA-U1D6tO_Hz4IaGxlyNmE6VgPaIuHvoyJRN1NxeGSxmujChxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11a685fe4.mp4?token=Lx9PRq_ivv-MMYtkD4j-alARPSpqobGoIf8JyArWtj6b7oWmR3PdBA__boZKf2yFnA43bb1k5X2FuVCAB4R5Eb-__NGj5mC05k6PXdwUvxlNTT1suvM9i_5sire4GKxNwsy9j4Ax0qUt3JgH57Zq_KkVLJ9tofspn-HftkoEWQ7xGQlFDmXD9_WnA2wOxhTjrnDR3FJ7zF0EugVgPUrTwmmt_iEbUJTm2xKtfJM6cGDxTuc8omymaZFL5tZZhMJ8GOPBcTPvFyFl2Q-7JKc2Pk0aRTMNtRLj3hjDA-U1D6tO_Hz4IaGxlyNmE6VgPaIuHvoyJRN1NxeGSxmujChxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد الحشود المعزّية إلى ميدان انقلاب وسط العاصمة الإيرانية طهران للمشاركة في مراسم التشييع الرسمية للسيد القائد.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80866" target="_blank">📅 23:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU-nilv98ttOc3ZOC-3m89HHIkWurb4MDUomgFZLnne65A2c73qQrFXwODHReu7B9EQn7RgVqDoSaV3bbN5dsPIO2rc1n_pXbIdaxtu6WCoOZ2Qc-fSKwPYWO7leorRUX9kr4FybZlKkOrm897S1eYdYNcgbAd9SfD8exqQ1BEbFtiEQzDSJ0P3uZLVX0DQtLwq2tsdQcqyi_KMsDb4JeAGdRNexu9fFTwcoF1XQmERKweB3KPNfjNtYqDd29P5rPmXf6azzd9CXx6wkMGBvBRwVcGLAte_Kt9cTvO6K7vp9EO1BQN7UJDfuwNpq5m83CQ5J5NreEoJwEzgNkbgS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتلاكن روحي وروحك مثل الماي ولاگه الماي</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80865" target="_blank">📅 23:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔻
العاصمة العراقية بغداد تعلن تعطيل الدوام الرسمي، يوم الأربعاء الموافق 8 تموز 2026، بمناسبة مراسم تشييع السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80864" target="_blank">📅 23:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
من ميدان انقلاب وسط العاصمة الإيرانية تجمهر المعزّون بانتظار انطلاق مراسم التشييع الرسمية للسيد القائد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80863" target="_blank">📅 23:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
‏
ماكرون
: حاملة الطائرات شارل ديغول ستعود إلى  فرنسا بعد توقيع أميركا وإيران مذكرة التفاهم.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80862" target="_blank">📅 23:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
من ميدان انقلاب وسط العاصمة الإيرانية تجمهر المعزّون بانتظار انطلاق مراسم التشييع الرسمية للسيد القائد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80861" target="_blank">📅 22:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5f5e2fab.mp4?token=g6VBeLaHGfFcC3gvs2uIE3nntMdCEEN_btbi3ba3XypWW4RlaKijMq00t9cwOZ13aXniG-GpeDuR4t4H80vd43gbhO5abOIoAPSEkG7IWRf1KmNdNOubxsRQLmfxuso8EZ7Q7__Ic9SALChViX-OQKgNywKKsnKuQcw646cgl4ac7P42Ger0jtQKAL81_0_0KxkvwiPsjJf-Q2jKhzqQUsAbuadsMnLSV7K6Y4tMHIoEDntQjQfYhE4Gq6-xs1s8NtY0ecoZb7AirDrjD6MWX70lJQPTyltepc0rcfXNLV_-XtQLHjUb5VCkm49eQk7bhgkNF9HsFMPlc5bjdVXKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5f5e2fab.mp4?token=g6VBeLaHGfFcC3gvs2uIE3nntMdCEEN_btbi3ba3XypWW4RlaKijMq00t9cwOZ13aXniG-GpeDuR4t4H80vd43gbhO5abOIoAPSEkG7IWRf1KmNdNOubxsRQLmfxuso8EZ7Q7__Ic9SALChViX-OQKgNywKKsnKuQcw646cgl4ac7P42Ger0jtQKAL81_0_0KxkvwiPsjJf-Q2jKhzqQUsAbuadsMnLSV7K6Y4tMHIoEDntQjQfYhE4Gq6-xs1s8NtY0ecoZb7AirDrjD6MWX70lJQPTyltepc0rcfXNLV_-XtQLHjUb5VCkm49eQk7bhgkNF9HsFMPlc5bjdVXKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عصابات الجولاني تدعي احباط محاولة تفجير عبوة ناسفة زُرعت داخل حافلة في حي الورود بريف دمشق، حيث تم تفكيك العبوة ونقلها إلى مكان آمن، دون تسجيل أي أضرار أو إصابات.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80860" target="_blank">📅 22:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1485646dca.mp4?token=rIh48CabCjM4GmiO4kARhncR8StLWrX0nYMTm5cePnOHpWxhr7JJHDx_SNelg3aMj30RawM1HlGMGHKt5N9eCxN74wJ2aqgV9rcp-veS3MnL6WSD4MJzQNbk5chkl63iIJ5iIn-Ijqypss9qFjduvU51LDSBRvOIfMHQMH_PTZAcp61ecadVN9DjJa0MpuxicHTpLas-eY512x0qyY_TG99VYg4KW0hqM4gSGMlRq48ZLoUphirggM86v14TXX0zcbmhmpIBq6Ag4-z9OdWSQ2yvDsDP_oHMNL65ptnpTECJKXNf92KkMUI7jukKtr95GK-fD8nU3LjY3tXJoTxyBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1485646dca.mp4?token=rIh48CabCjM4GmiO4kARhncR8StLWrX0nYMTm5cePnOHpWxhr7JJHDx_SNelg3aMj30RawM1HlGMGHKt5N9eCxN74wJ2aqgV9rcp-veS3MnL6WSD4MJzQNbk5chkl63iIJ5iIn-Ijqypss9qFjduvU51LDSBRvOIfMHQMH_PTZAcp61ecadVN9DjJa0MpuxicHTpLas-eY512x0qyY_TG99VYg4KW0hqM4gSGMlRq48ZLoUphirggM86v14TXX0zcbmhmpIBq6Ag4-z9OdWSQ2yvDsDP_oHMNL65ptnpTECJKXNf92KkMUI7jukKtr95GK-fD8nU3LjY3tXJoTxyBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
يالثارات الحسين.. من اللقاء الأخير للجندي الشجاع الوفي وقائده الشهيد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80859" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
تعطيل الدوام الرسمي ليوم الأربعاء المقبل في "محافظة ذي قار" بمناسبة تشييع السيد الشهيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80858" target="_blank">📅 22:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80857">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي:
يا أمةَ الوفاء لرموزها وعظمائها،
يا من تؤدّون للكبير الجليل حقَّه حيًّا وميتًا،
إنَّ سيدَ الزمان، ووليَّ أمرِ الشرف، والشهيدَ قادمٌ إليكم،
يريدُ أن يودِّعكم عند أجداده الطاهرين.
قادمٌ في يومٍ تاريخيٍّ سيُذكرُ حتى قيامِ الساعة،
فقوموا لله،
وانهضوا بالسوادِ والغضب،
وشيِّعوه جموعًا تغطّي أرضَ العراق،
وابكوه بحرقةٍ تصلُ الأرضَ بالسماء.
فخيرُ السادةِ الكبراءِ
له حقٌّ على خيرِ الأوفياءِ .</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80857" target="_blank">📅 22:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlhQHk9KUONktJkufRwx2pqhes81yk0kTW41WcBv2IYGRl4MeTya6_tLDGE78tA6pwa9aKxk56sjBMuIoJdSjkJlS4kJTTgDuNHbS3B0FTKTjPMHIP6pD7YoRw2c6QQT4d_OpOFfa1TsMHwEiJkbotSLMRb1fWvmJJhapz_d1mmeZd1AmVlwvy5BxlnJx3q9kKAQrNKeVd_LgN0dtSjL_efcX5j3Mqe5pV18c6NMuNeBaKRCr4GQ-iiXM3FEnMim8QPDntkVgTOzzlvOIWTSmW-GvaCQDVdyERl6wrC_RBRGoAXMOFPp-WhMa12Vsy49wz9yMSy1QzXCUtvqFSZ3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
تخيّل أن يكون لديك نحو أربعين مليون مواطن يعتمدون على برنامج قسائم الطعام، ثم تصف دولة أخرى بالجوع. هذا ليس تصريحاً، بل مجرد إسقاط. احتفظ بنصائحك بشأن برنامج المساعدة الغذائية التكميلية (SNAP) لنفسك.
‏مواردنا، خياراتنا. انتبهوا لمعدلات سوء التغذية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80856" target="_blank">📅 21:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80855">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6312fc9623.mp4?token=jnTe9-t_-kzVY6urN8edJHD-_2Sx2E4pOa1HSWC-wgwVb_xcHTiOJiQ9cPlaqb94ugLMTavtxEH4JX6vUMxTRRq7Vx7DT3Hon3_AciRtl-B1-kS0sJhl0TC3JButSFdGlb8qq1RRDMAeoAdOWTyqgZSEW65XUmtqN4apKB0XmGF7FyminxBV2vVL3T3z7-s4youCH8YBlaurFKrwFN8E0Upe4PmZ-5AoMMXvuZxpd6hvELqntOdcqH863kLsiZMp-0mhwByoJbN2JPHGctYZSNxdIt8LGNuQCgCujDvZWg7WSJgdvNTaRx52bEH2uG_ejfFpaQ6bUSuav2AHrGfHag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6312fc9623.mp4?token=jnTe9-t_-kzVY6urN8edJHD-_2Sx2E4pOa1HSWC-wgwVb_xcHTiOJiQ9cPlaqb94ugLMTavtxEH4JX6vUMxTRRq7Vx7DT3Hon3_AciRtl-B1-kS0sJhl0TC3JButSFdGlb8qq1RRDMAeoAdOWTyqgZSEW65XUmtqN4apKB0XmGF7FyminxBV2vVL3T3z7-s4youCH8YBlaurFKrwFN8E0Upe4PmZ-5AoMMXvuZxpd6hvELqntOdcqH863kLsiZMp-0mhwByoJbN2JPHGctYZSNxdIt8LGNuQCgCujDvZWg7WSJgdvNTaRx52bEH2uG_ejfFpaQ6bUSuav2AHrGfHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قائد قوة الجو فضاء في الحرس الثوري يودع جثمان الشهيد القائد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80855" target="_blank">📅 21:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f5f36a01.mp4?token=GEbWGwcUgV9WAOjKJ054JgEnQdO4DpXYjYDB5nhvA2jp_0pBXnoEJr9ddsN9-IiT24eJzi_XDcz5lnYPM-CZMAsLkHdlhXdqpmewGd_PUwZ0yVT7l1jNzZmjer7MwZTx-qXpnbE0Q0RKyDVCLdcL_DBInob53ks2TlEeNZkGGN-waZyqs57-nTW7scyPGHgJ_h5LJUjfWGyDr-rmjIHtHu4nT2YIXZi75RkzXRvkJVL4hPqJzxKaJu0JtJ_Gsrfo_WT4Ua2kivR0uh1YODTDPy7o1PrLtQCLhIBx8ZR_O6UraTHUDNvo7Hmgz-WwfGF03qbP_FuIyu1I78AxwBGuRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f5f36a01.mp4?token=GEbWGwcUgV9WAOjKJ054JgEnQdO4DpXYjYDB5nhvA2jp_0pBXnoEJr9ddsN9-IiT24eJzi_XDcz5lnYPM-CZMAsLkHdlhXdqpmewGd_PUwZ0yVT7l1jNzZmjer7MwZTx-qXpnbE0Q0RKyDVCLdcL_DBInob53ks2TlEeNZkGGN-waZyqs57-nTW7scyPGHgJ_h5LJUjfWGyDr-rmjIHtHu4nT2YIXZi75RkzXRvkJVL4hPqJzxKaJu0JtJ_Gsrfo_WT4Ua2kivR0uh1YODTDPy7o1PrLtQCLhIBx8ZR_O6UraTHUDNvo7Hmgz-WwfGF03qbP_FuIyu1I78AxwBGuRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول جثمان الإمام الشهيد إلى مصلى العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80854" target="_blank">📅 21:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
‏
رويترز:
أكبر مشغل لشبكات الكهرباء في الولايات المتحدة PJM يعلن حالة الطوارئ بعدما بات غير قادر على تلبية متطلبات الطاقة المتوقعة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80853" target="_blank">📅 21:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7bd3a15e.mp4?token=T_GZ0JxnxoKqULQe3_dryAP9KEBRc-V1YMc7VuskT11kx6565JmhurqQMvZL4tvI6Lq6BHLm_2PbY4kYtKHhe8LMSu03Nlw_28y_X8IUy5QTv2O9CVRXBWNh60-IxDIOolQQkT6W838xRcPblxoEIF2Vw6fRTLQWY9EBwWtqaKER9lTiv5eDqhCy6bnva1zoqch-Zrmok17m2eMSECMD8rbbgTWtgVrXPZIqHSu0Ny9des5Gd8igK63YF602w0Vl-4U87vWAihi6OYwsXrLHGftQCIUF16-GGpcPmPJsHsEtDNGHIGwIBw3XOBLstwmuQq75PikUAK20MPGwI46G1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7bd3a15e.mp4?token=T_GZ0JxnxoKqULQe3_dryAP9KEBRc-V1YMc7VuskT11kx6565JmhurqQMvZL4tvI6Lq6BHLm_2PbY4kYtKHhe8LMSu03Nlw_28y_X8IUy5QTv2O9CVRXBWNh60-IxDIOolQQkT6W838xRcPblxoEIF2Vw6fRTLQWY9EBwWtqaKER9lTiv5eDqhCy6bnva1zoqch-Zrmok17m2eMSECMD8rbbgTWtgVrXPZIqHSu0Ny9des5Gd8igK63YF602w0Vl-4U87vWAihi6OYwsXrLHGftQCIUF16-GGpcPmPJsHsEtDNGHIGwIBw3XOBLstwmuQq75PikUAK20MPGwI46G1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
لقاء بين رئيس إقليم كردستان العراق والرئيس الإيراني الدكتور بزشكيان:   بزشكيان: سعى المعتدون إلى تمزيق إيران، إلا أن الشعب الإيراني ازداد وحدةً وتماسكاً. أحبطت حكمة إقليم كردستان المؤامرات التي استهدفت حدودنا الغربية.نحن مستعدون لتوسيع التعاون التعليمي والثقافي…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80852" target="_blank">📅 21:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
🌟
مصدر إيراني مطلع:
مسؤولين أمريكيين كباراً شنوا، على مدى الأيام الخمسة الماضية، حملة واسعة النطاق لثني الدول عن المشاركة في مراسم تكريم القائد الإيراني الراحل. ووفقاً لما ذكره دبلوماسيان عربيان -اشترطا عدم الكشف عن هويتيهما- فقد ناقش ماركو روبيو الأمر شخصياً مع نظرائه من خمس دول عربية على الأقل. وتشير التقديرات إلى أن ما لا يقل عن 13 دولة -بما في ذلك ثلاث دول من أوروبا الشرقية، وخمس دول أفريقية، ودولتان عربيتان في منطقة الخليج الفارسي، ودولتان رئيسيتان في شرق آسيا- قد قررت عدم حضور مراسم تشييع القائد الإيراني، وذلك بسبب الضغوط التي مارستها الولايات المتحدة.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80851" target="_blank">📅 21:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80850">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVH7SrnB9inAkukxH-zBbOUCgbEJCNhCHo4dZp9E8zb5Ern56tl2pYtd9UKZUY7EpDCnC-29aP09vODOIw9tC0-7dPHwp39pLrZ2khrCkcAmJ5R0ciNXMDpzTMZV2KrDp7Snpj_HA-yIMh45n46RRn1LbDB6b8EEN4oNSktxcUNMbNuQCs0-ZxNvgrsjektH7fQYCRFQM34XX4lmhX3w0cAjaIT4C0DU1lrrDb-K7S6mOVXQsYKOebLO5aKBRsQLxyvdah4BuVe5rLU2Z56L_vDGhEQcLuT1vxdQcMnynEVKLL4hJ6U85Atm5kxnEegChviRfdNjzE9u-9Raexk2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد قوة الجو فضاء في الحرس الثوري يودع جثمان الشهيد القائد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80850" target="_blank">📅 21:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80849">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a6c4365c.mp4?token=IzAroPuP3ainbfsTpXr0EvTK9WLJRaYy7uRN6sqI7wOlUBrBKaGShLbBDzTgo5Xi3RmK2oC-2mt11gvUZIHfXn8IK7Oi9wL_-U2D1oLvezI-mre9UA_qVXQdoNjX-RlKZsO9NmdozkbJc9tjU1phNz7ZTwX3PP3YRmoXqm7vTVV5TgCwVUS3JydIkrR45KBKx7YwLEFBO5rQwL8x9I3XI9SsLJoypEfcPidghR00pBj_KjUTeYDWdsXyzTN_cTmeC0ffpdyHQzbJirbXxtsNXZgF6LU3k86fuYE87Wepom3-K2tPQDzw45Hy5rYnyGem2g3qxsLWfGTV3l2jqa6ArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a6c4365c.mp4?token=IzAroPuP3ainbfsTpXr0EvTK9WLJRaYy7uRN6sqI7wOlUBrBKaGShLbBDzTgo5Xi3RmK2oC-2mt11gvUZIHfXn8IK7Oi9wL_-U2D1oLvezI-mre9UA_qVXQdoNjX-RlKZsO9NmdozkbJc9tjU1phNz7ZTwX3PP3YRmoXqm7vTVV5TgCwVUS3JydIkrR45KBKx7YwLEFBO5rQwL8x9I3XI9SsLJoypEfcPidghR00pBj_KjUTeYDWdsXyzTN_cTmeC0ffpdyHQzbJirbXxtsNXZgF6LU3k86fuYE87Wepom3-K2tPQDzw45Hy5rYnyGem2g3qxsLWfGTV3l2jqa6ArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول جثمان الإمام الشهيد إلى مصلى العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80849" target="_blank">📅 21:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80848">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
تعطيل الدوام الرسمي ليوم الأربعاء المقبل في "محافظة ذي قار" بمناسبة تشييع السيد الشهيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80848" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80847">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شوارع بغداد عاصمة العراق العظيم تستعد لأكبر حدث بالتاريخ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80847" target="_blank">📅 20:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80845">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lgS3kymp4_f8nTWNgwYoLkqcqRogzG8IH-b9yo0gHxxRyBxk07hrb5ng3B1KgakkZm9g-oPDOH_M7YSQ0eLXnqzZ1W0niwHzx9GhM9GevFUobIINXVh1SFLMzoFRTgdOr-LrFlJ0Ss_9t3hjvH7HK50yfU4L9C84JkbsQzKckQVs3tipnhPDDEWnCpE1h3ySqhkSIkkMwzj2EWtaqFlho1Keu72aFhJXzBKRysARH3D5mHPOpUYdUOdrfOa567KyQX5wS_D9PgAenLrNWy8bIdje--FAZJLMM9Vp-yc1SzdbNbj5LUz7SIigYzg2Gn1M9gZXTJ5SevdsZnGxHgemzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6FeUCNeaZQHM-V5XSFmDTmm1IKRcplRxFHF6JBdhAW_X1QTbAE6Lm7-0MvVi0_J7R6GRhB75fWWW5WwVxCioQLQbR_mMxHGKHwHwbvwIuog4wlN9RKXnu5CoMXKGBZO0OPKLizZbiXarxQt5gbLuPHDOU48rXtUDrRFx8w1Idk7-esCZOzg8DPc6zyfjypMVBqki2Gcm87eLpCol5ACjZK_yc2Esy6uspUNSb3Pz-5W4bomBMNoKVAOYoEHb0T736tlz4ZsnWibyO2lTvhY3ziRrigA7X4q5_CRpaWuzb4FHAa_rVgDXi2XNT1Cvv810qu_DaQ2Hmvcy-Le_sdxVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدء توافد الجموع نحو مصلى العاصمة طهران للمشاركة في تشييع قائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80845" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80844">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184bff16c0.mp4?token=n7Kb3vog2kHTTQjAaWWLP0-zyV2vSdYSOAJLkcj_Ad__HLZI80h2tRqDtufeGWRJXiDP7Zi1N74fD-Rx1YMsSqLwbeuF1pLaW2_roSImqe8B6Nooo62H4Ujjecqzh9G-j1xb-SG8HLc6B5Yb3Sr3rTyShaDjnwiN69Xwht9Wjsrwduh7WgfTOuFGXONmqq_zmjxJhrv-OQw6JadWgbc1YnNLkzcJug61DNx86DiM7wCylyyYOK273PyEk0EwrRhZZdNysO-ddkwo5DgJg46difNAIuloGR1erGPoPVzooF9Qk8sFNX60L-JeHXJ-gXfzeDjN-6uZcpNX4S1Y8KyTfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184bff16c0.mp4?token=n7Kb3vog2kHTTQjAaWWLP0-zyV2vSdYSOAJLkcj_Ad__HLZI80h2tRqDtufeGWRJXiDP7Zi1N74fD-Rx1YMsSqLwbeuF1pLaW2_roSImqe8B6Nooo62H4Ujjecqzh9G-j1xb-SG8HLc6B5Yb3Sr3rTyShaDjnwiN69Xwht9Wjsrwduh7WgfTOuFGXONmqq_zmjxJhrv-OQw6JadWgbc1YnNLkzcJug61DNx86DiM7wCylyyYOK273PyEk0EwrRhZZdNysO-ddkwo5DgJg46difNAIuloGR1erGPoPVzooF9Qk8sFNX60L-JeHXJ-gXfzeDjN-6uZcpNX4S1Y8KyTfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء توافد الجموع نحو مصلى العاصمة طهران للمشاركة في تشييع قائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80844" target="_blank">📅 19:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80843">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">هذه أيام الـعـراق التي يعرفها العالم..
🏴
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80843" target="_blank">📅 19:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80842">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭐️
لقاء بين رئيس إقليم كردستان العراق والرئيس الإيراني الدكتور بزشكيان:
بزشكيان: سعى المعتدون إلى تمزيق إيران، إلا أن الشعب الإيراني ازداد وحدةً وتماسكاً. أحبطت حكمة إقليم كردستان المؤامرات التي استهدفت حدودنا الغربية.نحن مستعدون لتوسيع التعاون التعليمي والثقافي والعلمي والاقتصادي مع الإقليم.
نيجيرفان بارزاني: شكل استشهاد القائد الإيراني خسارة كبيرة للشعب الإيراني والمنطقة. نعتبر إيران داعماً وحليفاً ثابتاً لنا. لم نكن يوماً -ولن نكون- جزءاً من أي مخطط يستهدف إيران. عبّر الرئيس عن تقديره لموقف إقليم كردستان المتسم بالتعاطف والمسؤولية تجاه التطورات الأخيرة، وشدد على توسيع التعاون العلمي والثقافي والاقتصادي.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80842" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80841">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYVh7v_MpdpyPRua0U-ru7olqOJq0as7idLzBJIxy-ey2zjtvSmcdt5aErIfkQlPViYBrcfyaQjxthjvOOGJUt1FgDPH1Yix9guk7nemk7oeRrQdIxOipUfvvZ0k6HasRRs4AWhDNayg_TBgpe4rOOFFXA2wICu0GO-53bOdYg3joQjOrB4NS6RWWUuqDp95RBSVKq0vQGJWxF-3k_GIFvbcL8DksN02YCVajURB-dCdsZBTRLI_JO6yQxKjvo4fKHVkXIFYNHD-junuzRJ4khXDF5b8jlIennHBjDHZWeWkmOoSrMAQYTX9SVjHmEDBmr6BUgDswD1pgWzwOvTVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتري مدفيدف مبعوث الرئيس الروسي يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80841" target="_blank">📅 19:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80840">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtHnTGAVFgEqIKPXDHeA_0YF5sPANba3IKhZiE9ywUCe3fMXHnu9ajWdTsCdTVJKd2EdPKRlCzpKyrnk4WadhJIoIQs-oZKOe5Lhgs-2JAhVqC9AAbAaKtzwjyX76VkQnDgRDfxqu0wgTZcqxhRAA57Pd6Kfn8fkKUJWtSbHoFG7mxBks-81SFh03ksmZyYBMvxWRTx11-3AqoIYkCsaz_YkO_LQnJmWT4GxIsgClcy5B9tPRqTLMqvP4-Td3kodTHLz9NsYJBeVPgNq9gf2T1Q4gK-XxG_CjJsQO4JMm_U7QBFjT5B3EvMOo0OQkOi4KQFIi26MQDZ-98chxuFGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
قائد فيلق القدس"اللواء إسماعيل قاآني" يستقبل الوفود العراقية المشاركة في توديع قائد الثورة الإسلامية بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80840" target="_blank">📅 19:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80839">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50999e9b32.mp4?token=eRWo2YtUJbcHY5iVl_rch5OOFqLxyA88XNOvDHJNKt2Y8g8V7bEuDLMda70qj68a-R9Kj07Ma7oXkp3i84UDdc-7CaukI8FAfoxWjL059NcZSrwSa1rDmkEfAt6YnV8a9K5OFACkUjQT702aNuZAuAqueGY7PJ_eMGrYQUYqB_i6hhMYxwyRq4cdJP8LEIKtFb-Ipgl7RIVBuaKbEYMkndWoOIsy4123BgonKQEbSFMUS_o2VkXP_Q9qLc0A1R204N_H9AAFpWdSS17n3JwCT1auNjnWH5IJV6E3Zqqqu0ywgzmAtWERYZEhzgRj72XFtYe-5TZB8OYbgs5PUtZpuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50999e9b32.mp4?token=eRWo2YtUJbcHY5iVl_rch5OOFqLxyA88XNOvDHJNKt2Y8g8V7bEuDLMda70qj68a-R9Kj07Ma7oXkp3i84UDdc-7CaukI8FAfoxWjL059NcZSrwSa1rDmkEfAt6YnV8a9K5OFACkUjQT702aNuZAuAqueGY7PJ_eMGrYQUYqB_i6hhMYxwyRq4cdJP8LEIKtFb-Ipgl7RIVBuaKbEYMkndWoOIsy4123BgonKQEbSFMUS_o2VkXP_Q9qLc0A1R204N_H9AAFpWdSS17n3JwCT1auNjnWH5IJV6E3Zqqqu0ywgzmAtWERYZEhzgRj72XFtYe-5TZB8OYbgs5PUtZpuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق من الإستعدادات النهائية لمصلى العاصمة طهران ومحيطه الذي سيستقبل غدا مراسيم صلاة الجنازة والوداع للجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80839" target="_blank">📅 19:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80838">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
الحرس الثوري يتمكن من قتل إرهابيين 2 في مدينة تفتان بمحافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80838" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
