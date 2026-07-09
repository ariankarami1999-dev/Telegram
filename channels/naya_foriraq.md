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
<img src="https://cdn4.telesco.pe/file/ZrO6_-f3fU_izCZHTjD1mPUgrQOpC7KWpforSbIOXgRnXO86xVurZ5CABgvvEXhdutQxq3QJ8wx-ZXu5g4HsNRptCi4eqHNhxP-sZddinVE7uFaq0CDAd-cgTSUQ7UtCIHuR8InOlIukOo0d_SuWecAD2HMlZ3Nya6IzpYCcnLb5t0G_JCUi1b4AEshXowvGkAyubCPk5xNJUxon_QXUeQWNWfeOysAsU3Rd4VqHeecsV1t5RX1CjvH-iA6Vl2wC3ZL5CNOuPRrCOYBADI2xa6qwoTZv19Dp7Epz-OB8--o-0e_SVQysDu9CAV14rUDe_UCs6xnTgGTulnN1VTN9WA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 08:59:38</div>
<hr>

<div class="tg-post" id="msg-82090">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترفيهي.
‏ترمب: الإيرانيون اتصلوا بنا وأبلغونا أنهم يريدون إبرام صفقة</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/naya_foriraq/82090" target="_blank">📅 08:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82089">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f643b446.mp4?token=XGT5Qo0BvBeBD9uQ5TFMLQe85EQID6XJ2EFKeHZAPWG5V2jft6LVQhrerQYsAmz_wwRSLpqYT0FlRkkV-i1cuu0YHf422a5DzB2m3oN8jsQW0-nT5x4gF7V10AgdOKK7OXQ2_l86qTLxYHDDsqTJ0ccru_Mq57VrhNlrPLnZ5OB-pTGtseoxKrSfmURfW2IC932hUclt8K7QI24qR_mE9fSt0g6IZ541EFmW34hxPMMLZ386iAcOKG4niHR0yxNVeIxFZPlULGMT9OKJ4Wa5K_uFLtoHB1eL75ujT1ePOt4U0ob1-etHGhqmBrkHMT4pKFL3LMJTjuuvDfCLsp9kNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f643b446.mp4?token=XGT5Qo0BvBeBD9uQ5TFMLQe85EQID6XJ2EFKeHZAPWG5V2jft6LVQhrerQYsAmz_wwRSLpqYT0FlRkkV-i1cuu0YHf422a5DzB2m3oN8jsQW0-nT5x4gF7V10AgdOKK7OXQ2_l86qTLxYHDDsqTJ0ccru_Mq57VrhNlrPLnZ5OB-pTGtseoxKrSfmURfW2IC932hUclt8K7QI24qR_mE9fSt0g6IZ541EFmW34hxPMMLZ386iAcOKG4niHR0yxNVeIxFZPlULGMT9OKJ4Wa5K_uFLtoHB1eL75ujT1ePOt4U0ob1-etHGhqmBrkHMT4pKFL3LMJTjuuvDfCLsp9kNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من وصول الجثمان الطاهر لشهيد الأمة إلى مطار النجف الأشرف لإجراء عملية العودة للجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/naya_foriraq/82089" target="_blank">📅 08:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82088">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇶
🇮🇷
نقل الجثامين الطاهرة للإمام الشهيد وعائلته إلى مطار النجف الأشرف، لإجراء عملية العودة إلى الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/naya_foriraq/82088" target="_blank">📅 08:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f083bea4b.mp4?token=sLzT60OEalcDHbSOgc_4ODVpJKPIP9dvN5lrvoUOSUvPFnSPWVaDZtzmRLKdhFuQBrTO-0Z52qESL17GmMWRvFm2fCSsHnHAModSuFnBBAysIAaazB5JKdoC5zbxniVu8l3qVCzcP_fR-y_HPW5E1bB8Ib6HDDYuyd7v8OtgXCCffbvQl4F6J0kD9dEnScjuj9VzN7QGq96ljEnBMlwUCfuYg_vvD9SgTZe8Fr7pZsuJRqezQiize9p7PKV8tIjV7mmH532KqPJlJu9hXYsVjObtE5NTsn4bipjl_MVOtXricAV6vZSsKih9tCH4wWxWR7GKSbVN1e92CTqYZdtwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f083bea4b.mp4?token=sLzT60OEalcDHbSOgc_4ODVpJKPIP9dvN5lrvoUOSUvPFnSPWVaDZtzmRLKdhFuQBrTO-0Z52qESL17GmMWRvFm2fCSsHnHAModSuFnBBAysIAaazB5JKdoC5zbxniVu8l3qVCzcP_fR-y_HPW5E1bB8Ib6HDDYuyd7v8OtgXCCffbvQl4F6J0kD9dEnScjuj9VzN7QGq96ljEnBMlwUCfuYg_vvD9SgTZe8Fr7pZsuJRqezQiize9p7PKV8tIjV7mmH532KqPJlJu9hXYsVjObtE5NTsn4bipjl_MVOtXricAV6vZSsKih9tCH4wWxWR7GKSbVN1e92CTqYZdtwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي كانت تحمل الجثمان الطاهر للشهيد القائد الإمام الخامنئي تعود بعد انتهاء مراسم التشييع.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/82080" target="_blank">📅 07:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82079">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcbe55b635.mp4?token=ZQI7oir107F4PxUTJg-KqUjIsrKfb3XQR1ETTsxTOnCyGDnvHXGpy_2Ya-cwM8by7sqIFEHo8J7NIW2mzdwBmezYZJWFuyqbn2shhNoT5UfbAHelAwYNt5duT5gj-BvKzKRzb6MAO2xknaWG_PJnCyxY4DJspHNRQpy5bk5wkR_SRjyo9fqTRqvLF9IxIkNb6bLjFSygog4sbM6cJLvCRjn7WU1S9B6ewOIJc7PX8VW_G4xqPeSXX0bNQYQyeipgsO68NcF18K97hsAQjThc8aM9Wa7JfWD8usgsx-37wA_2kweMXVH2ok_qiqd1tWI4UsS1lBC9q2Hmtw3QTrJmeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcbe55b635.mp4?token=ZQI7oir107F4PxUTJg-KqUjIsrKfb3XQR1ETTsxTOnCyGDnvHXGpy_2Ya-cwM8by7sqIFEHo8J7NIW2mzdwBmezYZJWFuyqbn2shhNoT5UfbAHelAwYNt5duT5gj-BvKzKRzb6MAO2xknaWG_PJnCyxY4DJspHNRQpy5bk5wkR_SRjyo9fqTRqvLF9IxIkNb6bLjFSygog4sbM6cJLvCRjn7WU1S9B6ewOIJc7PX8VW_G4xqPeSXX0bNQYQyeipgsO68NcF18K97hsAQjThc8aM9Wa7JfWD8usgsx-37wA_2kweMXVH2ok_qiqd1tWI4UsS1lBC9q2Hmtw3QTrJmeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
طيران إستطلاع يحلق في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/82079" target="_blank">📅 07:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82078">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭐️
بلومبرغ:
حركة الملاحة عبر مضيق هرمز شهدت اليوم توقفا شبه تام.
التحركات الملحوظة في مضيق هرمز اقتصرت إلى حد كبير على مسار معتمد من إيران يقع قرب الجانب الشمالي.</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/82078" target="_blank">📅 07:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82077">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
نائب محافظ خوزستان الإيرانية:
إستشهاد 3 وإصابة أخرين في محيط مدينة الأهواز جراء العدوان الأمريكي على المحافظة.</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/82077" target="_blank">📅 07:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08523c5b6e.mp4?token=tE3gcXeqRa9N51YAXfHQl6kYMOZ7CuUhvzOH0g6JWs_Tc6YJEr9lwAUdm_mv1I9KbzIXFoehYx1G-ONCcCZ60B15BKNqJ0xt3M7O_N5MGtV5c42ivCT1vLUQNwzaqld8PXVsTx0P5aN0lyIkjPFoQBSOWeYZ-ZfGE69FfNIaUQQNShSqCmAE7F6k_u0C__EyAqiQTNQbVriwqLg4kwramF0ktLHvhPLamS7-5FgfLIuxvGEDoTygFxfEpYoEK4YjKy637TlKretdhplcP1cObXJBxov1NZsA47C3XsY0hS0Bv8qyRVJ14fuUfuZCd-d9-OSIkN1-m52h1DubuJlcHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08523c5b6e.mp4?token=tE3gcXeqRa9N51YAXfHQl6kYMOZ7CuUhvzOH0g6JWs_Tc6YJEr9lwAUdm_mv1I9KbzIXFoehYx1G-ONCcCZ60B15BKNqJ0xt3M7O_N5MGtV5c42ivCT1vLUQNwzaqld8PXVsTx0P5aN0lyIkjPFoQBSOWeYZ-ZfGE69FfNIaUQQNShSqCmAE7F6k_u0C__EyAqiQTNQbVriwqLg4kwramF0ktLHvhPLamS7-5FgfLIuxvGEDoTygFxfEpYoEK4YjKy637TlKretdhplcP1cObXJBxov1NZsA47C3XsY0hS0Bv8qyRVJ14fuUfuZCd-d9-OSIkN1-m52h1DubuJlcHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
القيادة المركزية الأمريكية:
القوات الأمريكية استكملت جولة أخرى من الضربات ضد إيران.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82075" target="_blank">📅 06:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugcx9BLCzoqKCEmnlNpPq03jgQlze1JKdA5OxKRm0VNDWKsict7gY8Y3droMy_eA-WZQOEO15kTDsh0Pk__bB5MTbT89Ym7cI2vLOxjMgS6lFTNgPHwCsLJ6xQSOfe2pGna3Fe9jrWD6z8_BUS9V6v6qe-eSxXUP6sx8V-y-URZwRbdcUHsPQL0C1GPwq3HjTktiPDAcl1ggaoyeH7Pdt3NJYqGPsahm6Z-2vtNW3xKd6r9CMrSYiBnNxNk-eIuWMU7PAfI8qmv-QG39ctTsS4uZSDofkgMjpHw4xtEG0sbi1yQlpBTYqI6S_X9HwF1XsPpmrItkneP92liWRuiZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عقب الهجمات الإيرانية على القواعد الأمريكية..
أسعار النفط العالمية ترتفع مجدداً لتلامس 79 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82074" target="_blank">📅 06:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
مسؤولين أمريكيين:
مدة الحملة الجديدة وشدتها تعتمدان كليا على الخطوات المقبلة التي ستتخذها طهران.
الإيرانيون بدأوا بإطلاق النار وقررنا أن الوقت قد حان للرد عليهم بقوة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/82073" target="_blank">📅 05:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
بسم الله قاسم الجبارين
"قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ"
أيها الشعب الإيراني الشريف، أيها الشعب العراقي الكريم والمجاهد؛
أحسنتُم أيها الناس المؤمنون والبصراء والوفيون، الذين أظهرتم للعالم مكانة الولاية الإلهية وحب الشعب العميق المتبادل مع القائد الإسلامي، على غرار أمير المؤمنين (ع)، من خلال إدراككم للظروف وتشييعكم الذي لا مثيل له في تاريخ العالم. كما ذكرتم بشعاراتكم أن تكلفة الاعتداء على المرجعية والولاية الفقيه للمسلمين ستكون باهظة للغاية.
على الرغم من أن هذا التشييع المهيب، وخاصة التشييع العاشق الذي استمر 23 ساعة في حرارة شديدة، في أرض العراق الحبيبة، قد أثار الرعب في قلوب المستكبرين المقيمين في القصور، ودفعهم إلى رد فعل متسرع على هذا الاستعراض الشعبي. إلا أن أمريكا، التي تخرق الوعود، وبخلاف جميع الالتزامات، هاجمت مرة أخرى العديد من المناطق في محافظات الجنوب الساحلي لإيران، وفي خطوة مناهضة للشعب، هاجمت جسرين في المحافظات الشرقية المؤدية إلى مدينة مشهد المقدسة، وذلك بهدف طمس أخبار هذه البطولة التي لا مثيل لها وإخفاء هذا الحدث الملهم عن أنظار العالم. ولكنها تغفل عن أن هذه الجرائم ستوقظ الناس في جميع أنحاء العالم وتجعلهم أكثر تصميمًا على لعب دور في مكافحة الشيطان الأكبر.
لن يترك مقاتلو الإسلام تجاوزات الجيش الأمريكي الذي يقتل الأطفال دون رد.
في المرحلة الأولى من الرد العقابي ضد الأمريكيين المخالفين للعهود، قام مقاتلو القوات البحرية والفضاء التابعة للحرس الثوري، في عملية مشتركة باستخدام الصواريخ والطائرات بدون طيار، بعد ساعات من هجمات العدو وفي مناطق مختلفة من البلاد، بتدمير البنية التحتية والمرافق الهامة في قاعدتين استعماريتين احتلاليتين أمريكيتين في "عريفجان" و"علي السالم" في الكويت، و"جفير" و"شيخ عيسى" في البحرين.
يحذر الحرس الثوري الإيراني الجيش الأمريكي الذي يقتل الأطفال بأنه في حالة تكرار التجاوز، فإن ردودنا القوية ستتوسع لتشمل القواعد الأمريكية الأخرى في المنطقة.
"وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِ اللَّهِ الْعَزِيزِ الْحَكِيمِ"</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82072" target="_blank">📅 05:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f592daf67c.mp4?token=P-aDi9zgLmtMs55_dHFMVgMsEJSuynDhSL_KLdFiSSX47ux2xK-wtsZeZgePzBUr-uJjaiCCI6gkOUFjPiI5e9mFceavwy2d0u60tmjd4cQck6roqgU40woJtEd33r7ycySSOu8ZUw2ljHnoWdQzuqI99cwNRI_Pt62Cg4nBkf2I70sHuDQKvxuPuNlQwlpXbkmrXzgXR6m7e-SlWbtsKGivagWJ3NlIuZOlmxruncL-AabrO0zdRYwoVzy10AyJcwgBvsN00ZCQd9ufV-kfUn1toyTYzDxx_nQXmjEwIqPZKMCNcpTaFdhSlYeiX0gFJlQr9doLDGKOh3gLVklEKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f592daf67c.mp4?token=P-aDi9zgLmtMs55_dHFMVgMsEJSuynDhSL_KLdFiSSX47ux2xK-wtsZeZgePzBUr-uJjaiCCI6gkOUFjPiI5e9mFceavwy2d0u60tmjd4cQck6roqgU40woJtEd33r7ycySSOu8ZUw2ljHnoWdQzuqI99cwNRI_Pt62Cg4nBkf2I70sHuDQKvxuPuNlQwlpXbkmrXzgXR6m7e-SlWbtsKGivagWJ3NlIuZOlmxruncL-AabrO0zdRYwoVzy10AyJcwgBvsN00ZCQd9ufV-kfUn1toyTYzDxx_nQXmjEwIqPZKMCNcpTaFdhSlYeiX0gFJlQr9doLDGKOh3gLVklEKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
انتهاء مراسم تشييع جثمان إمام الأمة الشهيد السيد علي الخامنئي رضوان الله عليه في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/82071" target="_blank">📅 05:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فشل منظومة الباتريوت الأمريكية أمام الموجات الصاروخية الإيرانية والإنفجارات تهز الاسطول الخامس الأمريكي وأعمدة الدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/82070" target="_blank">📅 05:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933c11a63c.mp4?token=PIr6YKhWzCbYy9TEBgPyu2gE7OfhQkTQrnq1JtQ_kp2N-YtMMS3JY3X1SAbeaP6APY2vx2AZ_3xB3e6ZavTy0mYK9AvXwFZdSITvCloqf5VUaqCXi3l51hd2ItkuryHfMy7ZRf8qlhjxL4XE1_uLCIPv3IrypYpB1sIvqGPSDiysmW4lfYtXBiVfWxNAEY8sNOsW2WDfqTk2piMQK1Y8vcM_rhfXW3AEvaa7PYTAvh7BXnce-a_DnfqEvu6iDiLTfb1madtnGub9Ac68sRr88oTUTlUq0j_TjdGOux2awS3IA1m8nxthFAb03_GsX0zddGwJL93iY9AnMRFfSRpoMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933c11a63c.mp4?token=PIr6YKhWzCbYy9TEBgPyu2gE7OfhQkTQrnq1JtQ_kp2N-YtMMS3JY3X1SAbeaP6APY2vx2AZ_3xB3e6ZavTy0mYK9AvXwFZdSITvCloqf5VUaqCXi3l51hd2ItkuryHfMy7ZRf8qlhjxL4XE1_uLCIPv3IrypYpB1sIvqGPSDiysmW4lfYtXBiVfWxNAEY8sNOsW2WDfqTk2piMQK1Y8vcM_rhfXW3AEvaa7PYTAvh7BXnce-a_DnfqEvu6iDiLTfb1madtnGub9Ac68sRr88oTUTlUq0j_TjdGOux2awS3IA1m8nxthFAb03_GsX0zddGwJL93iY9AnMRFfSRpoMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تنقض على الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82068" target="_blank">📅 05:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e12390c92.mp4?token=tZxV70ES_hY2bFDxt0Mtbw7JoAS1tU6-4B0XryZfiGdJRz3krotSp24P0MYIdVN1Y62OhCwSvFGyODpbSTINOncY-zHh3xVQxsCoCwvHj5T1cXEW3e_SIW8azstj1c9K_omTC6lORkb9C4nAEWLsrIfwXwc6lQV_iT7XXyspp_F8YLpTsmsUrsYJCZP1_4YP4iFkrBNALYKtVjgmCgz2kP3Lclw24fHuX-UX1yJN5yzqu9Rz50G-NcVjeUOrtk8ojJLN_hB-gVagDQiq4UneQz1DAHpOEpcPznebmaMOKH60COUDwj17JTPED9OZMakqxoA7keQsr-2pDxXwgHGCmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e12390c92.mp4?token=tZxV70ES_hY2bFDxt0Mtbw7JoAS1tU6-4B0XryZfiGdJRz3krotSp24P0MYIdVN1Y62OhCwSvFGyODpbSTINOncY-zHh3xVQxsCoCwvHj5T1cXEW3e_SIW8azstj1c9K_omTC6lORkb9C4nAEWLsrIfwXwc6lQV_iT7XXyspp_F8YLpTsmsUrsYJCZP1_4YP4iFkrBNALYKtVjgmCgz2kP3Lclw24fHuX-UX1yJN5yzqu9Rz50G-NcVjeUOrtk8ojJLN_hB-gVagDQiq4UneQz1DAHpOEpcPznebmaMOKH60COUDwj17JTPED9OZMakqxoA7keQsr-2pDxXwgHGCmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تنقض على الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/82067" target="_blank">📅 05:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd047d9403.mp4?token=pDs-NttP_BjZ1ulmGI0gCZceo2aQOs1M6RVZI9qH9XrgUUOlVvlpS_rvJIJch0_1yuKSIoUqo3-oWLRN5BXJckV-t_OetpnQ_VouPcRysSc4o3kNkJP5RXKNbx2_h4Ae4inqNNFz34I3yXbCagqoUewunKDICOqvij8IPY3JXFAXhKDXswYS-q8GJX-UyazfFlo7g3jrTqSyGY4OXaGruuqeZt9Mp9fmJ0v47_WutVXkSE6-0bv6Lwp271hcdFiGPl0ez2_AV4V9Vk3E0lrc887qyTEOliUWNxCxHGFZO2gtF4OeL_otFM-Lkezr-wQ6eac2swsakQBc1hdjrCqsxRe4SeCfObcwRX4QlTJTiA8hgx7iTnoXfTp9I4-JK3J2gBTBt7AAhjs9WHbTMcCqx0MlsnNxnve0ZQa08sG2Ug_w_aGOKB4gyVRwyY7Aoi7_TdIPPaWzr1JOeUpleaN6SnTiKCT_zz_2jS7SNKNAEKLkIYzZ1i1lD8u0HVZ_1r5Rw28grNN0Fv9he78L2shyuuOpIi_qdYjzSbjnshyfsL2jfg0sghaxH7L9Pt769iiFFKC0Yhw1U0cg9sYqYzLzWmqgTs2Ujcai93-y4gnl_K0Nxm9J5lX6pbrmD8L7UUM7ZU_JjgHpqAjZMGlSGESXPd6tSExnJ9kjMkwriz-BkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd047d9403.mp4?token=pDs-NttP_BjZ1ulmGI0gCZceo2aQOs1M6RVZI9qH9XrgUUOlVvlpS_rvJIJch0_1yuKSIoUqo3-oWLRN5BXJckV-t_OetpnQ_VouPcRysSc4o3kNkJP5RXKNbx2_h4Ae4inqNNFz34I3yXbCagqoUewunKDICOqvij8IPY3JXFAXhKDXswYS-q8GJX-UyazfFlo7g3jrTqSyGY4OXaGruuqeZt9Mp9fmJ0v47_WutVXkSE6-0bv6Lwp271hcdFiGPl0ez2_AV4V9Vk3E0lrc887qyTEOliUWNxCxHGFZO2gtF4OeL_otFM-Lkezr-wQ6eac2swsakQBc1hdjrCqsxRe4SeCfObcwRX4QlTJTiA8hgx7iTnoXfTp9I4-JK3J2gBTBt7AAhjs9WHbTMcCqx0MlsnNxnve0ZQa08sG2Ug_w_aGOKB4gyVRwyY7Aoi7_TdIPPaWzr1JOeUpleaN6SnTiKCT_zz_2jS7SNKNAEKLkIYzZ1i1lD8u0HVZ_1r5Rw28grNN0Fv9he78L2shyuuOpIi_qdYjzSbjnshyfsL2jfg0sghaxH7L9Pt769iiFFKC0Yhw1U0cg9sYqYzLzWmqgTs2Ujcai93-y4gnl_K0Nxm9J5lX6pbrmD8L7UUM7ZU_JjgHpqAjZMGlSGESXPd6tSExnJ9kjMkwriz-BkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/82066" target="_blank">📅 05:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/82065" target="_blank">📅 05:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/82064" target="_blank">📅 05:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHnlBe2xj3TZz-fPYDJlU9VZAIuvWL5HrN4iwx1KHhb_nwKhVV8lsKapcL-pdjDC8QLMVKiZSG_irsN-LEUy0f4sENnmMuHepzUWDNGO0PNasrnez4oug908a0nz3lQPIvTWQAWkUoq6a7Lj6kRiO_-lMHmmrUT_Q7zR6tL-gr-73W7U1Qf9qT9Wte2rH8HREo_B7xPNSf3CgWQpauO1nf1WWn491DWfno4rRBjZBBBdXTpcqILkI0DjAqHFAjfOstNn4swJ4Ho5nV8kxoBpG7F1G_eLN63Y58-vdeIixiYiSkYgtNV5uyfspbckZr_Zy07UFrU_g2vy6d1a-AQ85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
أمريكا لم تتعلم بعد أن البلطجة ونقض العهود لن تكون بلا ثمن وسأقولها بوضوح إذا ضربتم فستتلقون الضربات.
لا تتحركوا يدا و رجلًا عبئًا فستغرقون أكثر مضيق هرمز يفتح فقط بـ «الترتيبات الإيرانية » لا بتهديدات أمريكية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82063" target="_blank">📅 05:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a0d0b72f.mp4?token=DLWcM8GekXppXqGqGPFi0cZqzvaGGU82xBB-XEpyqInsjDSSY-ddXImEgI8sJZO0x8IMlMXLym1kqXGluX_sqTS2Jc8iDlwXqhZM6qKwOURCQ3nfzPpE6jDUbTt0kMSXJ7jgXzFgjddtzsOD2dnhluw6UUwCoXSN6vgvu5CsgEml76rYNLwMe6xzauOccAW46e4iF8Ry5AwwF9VUF1GTgY2Up0FH8W_QvlXDrKyGRbrKN6rOgAkEiNVB02tGqFeECh8jfm37F_hxn_WeBUeWKS0HTwqchmsm5dHsHj3536H3RoY-djz-6_aE-ju91OrgnPuFMvdnE_1u5lSMM-JRDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a0d0b72f.mp4?token=DLWcM8GekXppXqGqGPFi0cZqzvaGGU82xBB-XEpyqInsjDSSY-ddXImEgI8sJZO0x8IMlMXLym1kqXGluX_sqTS2Jc8iDlwXqhZM6qKwOURCQ3nfzPpE6jDUbTt0kMSXJ7jgXzFgjddtzsOD2dnhluw6UUwCoXSN6vgvu5CsgEml76rYNLwMe6xzauOccAW46e4iF8Ry5AwwF9VUF1GTgY2Up0FH8W_QvlXDrKyGRbrKN6rOgAkEiNVB02tGqFeECh8jfm37F_hxn_WeBUeWKS0HTwqchmsm5dHsHj3536H3RoY-djz-6_aE-ju91OrgnPuFMvdnE_1u5lSMM-JRDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يُحمل نعش السيد الولي على الأكتاف، وكأن الأرض ترفض أن تمشي خطواته الأخيرة إلا في أعالي المجد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/82062" target="_blank">📅 05:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">يُحمل نعش السيد الولي على الأكتاف، وكأن الأرض ترفض أن تمشي خطواته الأخيرة إلا في أعالي المجد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/82061" target="_blank">📅 05:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الجثمان الطاهر وهو محمول فوق اكتاف العراقيين في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/82060" target="_blank">📅 04:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82059">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42c4a64eed.mp4?token=gXJpNqjRn4-cIsAJUfZFO2L51iBPm9dyu6yyRj2tbHQ4HqxTVZ2MMbcWfSnUXKPGyQz16OU-unvagSzD4U-P9I4HgP5Q5bPm4YTjsv-Ny6ErD4_t7IdL2mHbNue-yiTFTNRshO_z2b2jq_3xMNLThINYAIY3DE_N5eFxAlKBV5DI-FYgWtjNPQN2lG0TOpC48ZeOlRrDC66EhI_8v1AVdanmLLDG0oYvnzGoE78Z5b1up2iXnkSts7BAwlB0K15vnIp5pVY5V8k-e-ZTLF21D3JrMMbYKY1_4x5zOsoHTQluUO26W-LTvqEwd_-TKtehHhPxPWIYohT_HsKpHl3yGY3tFPm55dcAzl0wFKwuqcht3u4-1wxDF9HL9uENXYWRga00968hG6bbWR5YZlptU2Wc-BjFEBn7iQlotC4oCHP6aoc3llW_7Eq18IwGsjCjLMW7fsS4CQaGJou2H75qbOvJ6v1xXxkH2zUdV5fqj16Sdb9G8gsX7NXz2VIp64-8UAD4dbN_MlUvkZwtJ23SGFHj6g1A2QSpnZqziLVohf_S977BCnhAljzunWOu9KKdkbm_Ieg1O01PhH4FkUzPWGwdKdtNU87cW_CHMQvfUiQ3_WT-VFuD-UafeV9lYuD0AI_pjvia5y6RhoRXXUXUiiub3tQeqAiwPlrc2TIxX5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42c4a64eed.mp4?token=gXJpNqjRn4-cIsAJUfZFO2L51iBPm9dyu6yyRj2tbHQ4HqxTVZ2MMbcWfSnUXKPGyQz16OU-unvagSzD4U-P9I4HgP5Q5bPm4YTjsv-Ny6ErD4_t7IdL2mHbNue-yiTFTNRshO_z2b2jq_3xMNLThINYAIY3DE_N5eFxAlKBV5DI-FYgWtjNPQN2lG0TOpC48ZeOlRrDC66EhI_8v1AVdanmLLDG0oYvnzGoE78Z5b1up2iXnkSts7BAwlB0K15vnIp5pVY5V8k-e-ZTLF21D3JrMMbYKY1_4x5zOsoHTQluUO26W-LTvqEwd_-TKtehHhPxPWIYohT_HsKpHl3yGY3tFPm55dcAzl0wFKwuqcht3u4-1wxDF9HL9uENXYWRga00968hG6bbWR5YZlptU2Wc-BjFEBn7iQlotC4oCHP6aoc3llW_7Eq18IwGsjCjLMW7fsS4CQaGJou2H75qbOvJ6v1xXxkH2zUdV5fqj16Sdb9G8gsX7NXz2VIp64-8UAD4dbN_MlUvkZwtJ23SGFHj6g1A2QSpnZqziLVohf_S977BCnhAljzunWOu9KKdkbm_Ieg1O01PhH4FkUzPWGwdKdtNU87cW_CHMQvfUiQ3_WT-VFuD-UafeV9lYuD0AI_pjvia5y6RhoRXXUXUiiub3tQeqAiwPlrc2TIxX5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النعش الطاهر في رحاب ابي فضل العباس(ع).</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/82059" target="_blank">📅 04:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9c41aff5.mp4?token=qv9HyYbmTn35-jbxT-qkXQYoDHD8YrnIOV0JpZEmcQBwd4-qufzq4PYs9bbc4GfnhzPBULS1xnt2lxCSDPS5dHPJSHmPz58VotHaZ2Kk6j7SCMkrOwBxY8kdx0QYymJY-5iROu8SW9BZ-BPmC_4-OMhiny2Z-1RPcrKbe3Tf5uFGzdN1WBicaDNCIqopIFxM5r4eDIfYyrh8S_FjHgHu3l1g0vLrK6FetYTL3emWlq7zXzZUFMihl6xslAE3akW_F1_2uPwI6di7zQTdpcUPv3szRrdAkJbAaep6Kp3GivlvagnXVpm-pLYsX5RiiHgz8-uEh_LAuH5c45_WRRrjDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9c41aff5.mp4?token=qv9HyYbmTn35-jbxT-qkXQYoDHD8YrnIOV0JpZEmcQBwd4-qufzq4PYs9bbc4GfnhzPBULS1xnt2lxCSDPS5dHPJSHmPz58VotHaZ2Kk6j7SCMkrOwBxY8kdx0QYymJY-5iROu8SW9BZ-BPmC_4-OMhiny2Z-1RPcrKbe3Tf5uFGzdN1WBicaDNCIqopIFxM5r4eDIfYyrh8S_FjHgHu3l1g0vLrK6FetYTL3emWlq7zXzZUFMihl6xslAE3akW_F1_2uPwI6di7zQTdpcUPv3szRrdAkJbAaep6Kp3GivlvagnXVpm-pLYsX5RiiHgz8-uEh_LAuH5c45_WRRrjDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر في حضرة قمر العشيرة اباالفضل العباس</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/82058" target="_blank">📅 04:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82057">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908c896fda.mp4?token=LY3AgQ4c2Z-1xORW0VStvvGQthcbH1wAd_XVDmcaThApIE-tf_exmDTsHhoKpl36fsbh_lUgH-S7lXDMwksAR4n78ZTHpxFoBEEDpdP55ZVw_8yR3lIfp_4wV_0pi7_oSzGLB2BppcbCdgnfKLF3tkUXlWD5BWtORQq2hq5pZK7-U9sZgW0L3KGWNPY3CPTUhoUjMErh15jBPTfpSvT8KhiZf7WoKLE4rwlyEnx8PHoahgDvehdv_vQXL_ZzyxENYsq5epBoU7usHtLAEzWrpmm-togQ9c42zS_O_Z6qTO-mhvv4GmNd9slkDUzZu9D2k1_Z-6K3E_ZOaKtGtnRNziGhpI--HmMMd_8BZI6_sl2HMWXB70wC7ddYIYiimjwkjjsLRA744YbNYTVv2o8jY4uUN7P2zGM3L_9LTWW0h4IZloGwXXrPsdE1hKXEnI8l0kSjxw_8WJO_PCWgqEOzaycsX3RFdqTUgkmh6ThNjTm-QCWEJSWr1fdx045XL0fiMXQgMiOD1j2fr7Wi0his6l1FqDguOar9O1CkdOsGQu2wHJ9nFKi8AbSK4USoBu52T3tkvDATBrqt3YaeoU42uIfjvvndMy_ZC_8PaKsrx8ZR6nYO-38bttl3acYGR0jdpAbDd_GDGE4S4pwC8n_evTBRdKE2dHsLanAxacC6eS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908c896fda.mp4?token=LY3AgQ4c2Z-1xORW0VStvvGQthcbH1wAd_XVDmcaThApIE-tf_exmDTsHhoKpl36fsbh_lUgH-S7lXDMwksAR4n78ZTHpxFoBEEDpdP55ZVw_8yR3lIfp_4wV_0pi7_oSzGLB2BppcbCdgnfKLF3tkUXlWD5BWtORQq2hq5pZK7-U9sZgW0L3KGWNPY3CPTUhoUjMErh15jBPTfpSvT8KhiZf7WoKLE4rwlyEnx8PHoahgDvehdv_vQXL_ZzyxENYsq5epBoU7usHtLAEzWrpmm-togQ9c42zS_O_Z6qTO-mhvv4GmNd9slkDUzZu9D2k1_Z-6K3E_ZOaKtGtnRNziGhpI--HmMMd_8BZI6_sl2HMWXB70wC7ddYIYiimjwkjjsLRA744YbNYTVv2o8jY4uUN7P2zGM3L_9LTWW0h4IZloGwXXrPsdE1hKXEnI8l0kSjxw_8WJO_PCWgqEOzaycsX3RFdqTUgkmh6ThNjTm-QCWEJSWr1fdx045XL0fiMXQgMiOD1j2fr7Wi0his6l1FqDguOar9O1CkdOsGQu2wHJ9nFKi8AbSK4USoBu52T3tkvDATBrqt3YaeoU42uIfjvvndMy_ZC_8PaKsrx8ZR6nYO-38bttl3acYGR0jdpAbDd_GDGE4S4pwC8n_evTBRdKE2dHsLanAxacC6eS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الهجوم الصاروخي الإيراني والانفجارات لاتتوقف في الكويت</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/82057" target="_blank">📅 04:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7bfce01ad.mp4?token=jhgtUcjFXbxx4dhSBQx4JGLBnfw8gU_Y34a7DFOubiJaatHu2Cvn6smLbr3QpM4b4gTrvD3r1TvCvU84KTFaFLL9YFgFd7Qtgho-wDyKhfA8LG9L_-ZEvVzv-RJPYcuMblWt5GWPALLSUzSKkBnUn4hhIAya4Hj8pk4zPY7sjoGeMhXzFuGDX_dpllStzeTuctr8o8tZdtYvmOZQgFadmuzD0n89tO0hcMcXiJ790EGA0Co6GJreq7n5G1inQu0AULoxIMvuPRtvEcUD6ncTp_AIqRRubol7qPUl9J09xZrx177-rIuNw6hrJdCAKYzd7W0sQVZsIEhfMCohOWFXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7bfce01ad.mp4?token=jhgtUcjFXbxx4dhSBQx4JGLBnfw8gU_Y34a7DFOubiJaatHu2Cvn6smLbr3QpM4b4gTrvD3r1TvCvU84KTFaFLL9YFgFd7Qtgho-wDyKhfA8LG9L_-ZEvVzv-RJPYcuMblWt5GWPALLSUzSKkBnUn4hhIAya4Hj8pk4zPY7sjoGeMhXzFuGDX_dpllStzeTuctr8o8tZdtYvmOZQgFadmuzD0n89tO0hcMcXiJ790EGA0Co6GJreq7n5G1inQu0AULoxIMvuPRtvEcUD6ncTp_AIqRRubol7qPUl9J09xZrx177-rIuNw6hrJdCAKYzd7W0sQVZsIEhfMCohOWFXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النيران تشتعل في مقر الاسطول الخامس في البحرين</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/82056" target="_blank">📅 04:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/952d76b6ba.mp4?token=Fnw04u1XDTaCyWL5otaoIdVk-yqsSt7Cdn9q2-zG_7e-QxUrs6hxYgZUL67xrz4Fj77HVIDjiQMBHBdJokJbazKMZvMR-s1ZouPk6lC-jxmbZJ582spPybuV8-X38-CwsbFry7zLSoVvIHHEEiS3Jyrl2u0KOBYM51niPrLDtu5KZPUCrQ19TYK_A6zhhdspvlr6hltHp_DiZHHbshKtq_tqMxcS1Ftil7XZj0ZEnZIjrT35HCKP0a30pVwVUW8ngpAkyTzTQ6hmvauwDROIfUHfrOdsfkN7gg78Vbt3knTO8jKvq6Fpf5pTyAq0HfKwiUMm5MrND-d_rY5SeZLWhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/952d76b6ba.mp4?token=Fnw04u1XDTaCyWL5otaoIdVk-yqsSt7Cdn9q2-zG_7e-QxUrs6hxYgZUL67xrz4Fj77HVIDjiQMBHBdJokJbazKMZvMR-s1ZouPk6lC-jxmbZJ582spPybuV8-X38-CwsbFry7zLSoVvIHHEEiS3Jyrl2u0KOBYM51niPrLDtu5KZPUCrQ19TYK_A6zhhdspvlr6hltHp_DiZHHbshKtq_tqMxcS1Ftil7XZj0ZEnZIjrT35HCKP0a30pVwVUW8ngpAkyTzTQ6hmvauwDROIfUHfrOdsfkN7gg78Vbt3knTO8jKvq6Fpf5pTyAq0HfKwiUMm5MrND-d_rY5SeZLWhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النعش الطاهر وهو في طريقه الى مرقد ابي فضل العباس عليه السلام</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/82055" target="_blank">📅 04:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7baeaf7644.mp4?token=WNIzUn-U5nXZ3AhiOMkDvapuFAsfFPC5J3VjY3sCqGpU8mVlZ083rqSIJb9X8BHgf7UUTim18LNJVY7Pe2tllo-3rh6mgxyGvvd4uFT-XrA_0dapsbpyjX3W0ClTsX_OVXcwWX40NRLBrGnijCmP2XCX4Fz7-XGISQMfHJyzKL5DsCxtGZHLEih9bfSxgq3S6dapFGugvfNiIh3yz8X6drlAGVhtg6l6jAg1N4uNxDavsXL92e6f_smZhPxNINoByRi4eLTk28T6wOLFRv3txm8hBMLoUughunwUFehF76EnnOarS7pfRDaI4TcPylF9ff5q81f4mcyuuPe897bXTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7baeaf7644.mp4?token=WNIzUn-U5nXZ3AhiOMkDvapuFAsfFPC5J3VjY3sCqGpU8mVlZ083rqSIJb9X8BHgf7UUTim18LNJVY7Pe2tllo-3rh6mgxyGvvd4uFT-XrA_0dapsbpyjX3W0ClTsX_OVXcwWX40NRLBrGnijCmP2XCX4Fz7-XGISQMfHJyzKL5DsCxtGZHLEih9bfSxgq3S6dapFGugvfNiIh3yz8X6drlAGVhtg6l6jAg1N4uNxDavsXL92e6f_smZhPxNINoByRi4eLTk28T6wOLFRv3txm8hBMLoUughunwUFehF76EnnOarS7pfRDaI4TcPylF9ff5q81f4mcyuuPe897bXTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس العزاء في حضرة ابي الفضل العباس للشهيد القائد السيد علي الخامنئي(رضوان الله عليه)</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/82054" target="_blank">📅 04:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158858e2ca.mp4?token=XdHskOWTBDumiibn6A6OFfjBmTGdedspSV8JY90-6HdV9N_wUOso2pHBRZbqCZEmS5SyGLC-J2hcWR_kV2Jj8wTwaw-UzEO4mdOg1dTiWp6YG56XrBIo2Yq_AMudYDlMUJI_2HEBQba4Od16gwuY4U5Qc-XxjRmx99HNYuS66bF3lu1MeDxjCyeFxNRHqTGbuw9laQ5wMDWbT9cLXkUQ6s4WIQYAuEeMfmr2NbMoiMkB-n6nXX52KGEp8NfErvA50Rd51poj064dRHDnHPoIfOEW1nXw4126WalHhorVdQyhbdCj-QYxrGpzipFHc5ohm6DGl99FQwcI5CeeNCz6JaNsR5DZpA4hDttU97tcFrU_0Sj2gaNYl7Fa7WE4Bz0HPThrq8XgEFK5KuanMwEEYMN1QnBrc6Wcv3dAiNgV1YJJsx2ZcAOrLu5UqVkVP4XBxaXN8H0pspbH1i1HYvSHyQeaMApUAmWxPKO7D1Y0Ok34RQtkJlkcLguKSe1OjB5-Z4f8OvH75fBSPPBiVsLicQyZiJ57QA8hYnEJAgKHZgMpuyFs7PkiWkMfs6H3gsa3LEtGqBhfAMHwh5c3FXF8OzNdy0h3WV1NF1x0o4fj3EPEEsR1zTd3Jf159O_-FGjSk_1pi8wVRVX5ERtZrxRbSyruMJAFh86fLTHmLYHzePs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158858e2ca.mp4?token=XdHskOWTBDumiibn6A6OFfjBmTGdedspSV8JY90-6HdV9N_wUOso2pHBRZbqCZEmS5SyGLC-J2hcWR_kV2Jj8wTwaw-UzEO4mdOg1dTiWp6YG56XrBIo2Yq_AMudYDlMUJI_2HEBQba4Od16gwuY4U5Qc-XxjRmx99HNYuS66bF3lu1MeDxjCyeFxNRHqTGbuw9laQ5wMDWbT9cLXkUQ6s4WIQYAuEeMfmr2NbMoiMkB-n6nXX52KGEp8NfErvA50Rd51poj064dRHDnHPoIfOEW1nXw4126WalHhorVdQyhbdCj-QYxrGpzipFHc5ohm6DGl99FQwcI5CeeNCz6JaNsR5DZpA4hDttU97tcFrU_0Sj2gaNYl7Fa7WE4Bz0HPThrq8XgEFK5KuanMwEEYMN1QnBrc6Wcv3dAiNgV1YJJsx2ZcAOrLu5UqVkVP4XBxaXN8H0pspbH1i1HYvSHyQeaMApUAmWxPKO7D1Y0Ok34RQtkJlkcLguKSe1OjB5-Z4f8OvH75fBSPPBiVsLicQyZiJ57QA8hYnEJAgKHZgMpuyFs7PkiWkMfs6H3gsa3LEtGqBhfAMHwh5c3FXF8OzNdy0h3WV1NF1x0o4fj3EPEEsR1zTd3Jf159O_-FGjSk_1pi8wVRVX5ERtZrxRbSyruMJAFh86fLTHmLYHzePs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82053" target="_blank">📅 04:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94395aaffb.mp4?token=ToDnWRKW1s2hSJi0kji6vjfbgPMwzUdl952NuVw1Y_W3lu7CglnA5HFOEWkh34cC1SbKcMAaPZGKxG64GIzOp1ANYfoubQfeQQIddV78krlzWXNw7YDZ3mfC1vDWhKXyb9si2A7UDiSAN8zfZf_TLXCU-x_12HfEG5FT9rpGXwMLspfIm5F_aTtOcy2TYXltO_96eYFZQW6GvRXe85XZHIU2hhxRxgWXfWIoyt7PaXPRaJqYj_UTMF_qaSlNLemmz7QGHVV5LpEbaZ4RQ2UuJoNoVjtNK99rZsO_Ku4grNR2bR66YY3NbOzR7RAdfy5QAw-pK7f3YDMbRTJfO2CiKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94395aaffb.mp4?token=ToDnWRKW1s2hSJi0kji6vjfbgPMwzUdl952NuVw1Y_W3lu7CglnA5HFOEWkh34cC1SbKcMAaPZGKxG64GIzOp1ANYfoubQfeQQIddV78krlzWXNw7YDZ3mfC1vDWhKXyb9si2A7UDiSAN8zfZf_TLXCU-x_12HfEG5FT9rpGXwMLspfIm5F_aTtOcy2TYXltO_96eYFZQW6GvRXe85XZHIU2hhxRxgWXfWIoyt7PaXPRaJqYj_UTMF_qaSlNLemmz7QGHVV5LpEbaZ4RQ2UuJoNoVjtNK99rZsO_Ku4grNR2bR66YY3NbOzR7RAdfy5QAw-pK7f3YDMbRTJfO2CiKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملايينُ المعزّين يحتشدون في رحاب أبي الفضل العباس (عليه السلام).</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/82052" target="_blank">📅 04:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcdc0d6ec.mp4?token=sXFWbGqetx4S4wJgNFB1k2Rdzf_IcIUa6vjF1L9zntegZ2B-l1zxa8AHvNBZ_mDjlgwa2SSLIok5U1pXwgzQXaPLGzMxPIOiDeIju0sBIJn87v-yWITY55Fxh-6M_KC-M1S4JDyptd643QAjgVMPVPhp3hNkLMwXMTPnZEp-wbuUq9faJaMxNyN54H_VxyYc3tkQUORqVCEHqZTfiahBqnuzCqak9lOmWVJdUSEaUnjja2abp3hXB-FjhDqhjSdlZAKMPsYQ8N6rvHAaL2Y_mMOps7Be3QRLyQwBD2mEJsLZcK8TcOXvgdYB6aagmNpao0GENZqLxfw8eMFNXxc-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcdc0d6ec.mp4?token=sXFWbGqetx4S4wJgNFB1k2Rdzf_IcIUa6vjF1L9zntegZ2B-l1zxa8AHvNBZ_mDjlgwa2SSLIok5U1pXwgzQXaPLGzMxPIOiDeIju0sBIJn87v-yWITY55Fxh-6M_KC-M1S4JDyptd643QAjgVMPVPhp3hNkLMwXMTPnZEp-wbuUq9faJaMxNyN54H_VxyYc3tkQUORqVCEHqZTfiahBqnuzCqak9lOmWVJdUSEaUnjja2abp3hXB-FjhDqhjSdlZAKMPsYQ8N6rvHAaL2Y_mMOps7Be3QRLyQwBD2mEJsLZcK8TcOXvgdYB6aagmNpao0GENZqLxfw8eMFNXxc-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة جديدة تنطلق الان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/82051" target="_blank">📅 04:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله أكبر
موجة جديدة تنطلق الان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/82050" target="_blank">📅 04:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1d0YfKR1Jv59idunYNgcbiZq4caaJBTdQn32tWYtTBFOznebLkclKgm8jQhFfPG-vPzSkbOPupzAfVv_KM9u8qEGG8ua9BnbkQwFAfIn5Z61LxaaFpGk9VJyyvpCIQ96JiZg6QhtevvJ-efJrL08nM1ZjIokhGANfLePNpRUAOvnFZf_UMvu8PAYPOMXWFraLgy6QEJP0ycRepB5GWkxSDnwCyPGRw3pO2epy150w4ORaMKCAkGTd34atVMaP91H7iqtOX5v3Unt2iaERd4BSpvGubEZDmug5N9hDeaaU7TSbZgXjU1oWIWxrzY5LnF2ur2mYSLULrbZde8B3gOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏تم تحويل مسار جميع الرحلات الجوية المتجهة إلى الكويت.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82049" target="_blank">📅 04:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNxRXVqxGvnqOvL7btCvGNhKriiKLny3-SDAEt8EOIGf1eBglFno6RiGLSevfU92QUPVSGAGlphEbCM72wt8Q5N3qVAAqebF0hSghYwEzqqqXWTQSy2sPWLmB0LeRHNffbUq1C2mTcl3BAtVAYGUd7YFjb-ZC62Hs2-9fEuXBr8Ueb-74Lso0nnIqzzEh5qkjzpqTVcuE3K2-gqwkOAVvtaoeOLGzQ1TQfODP6n6VeGeyaB_xkNLthP8dHSXQcQ47zg75pWkFag1DPqqX6PhVSCwwgKycqQOlgg0_eoNpfpNE6kI1k5uupN22axATt_CctrtC_4s0UEoOvq4AwbiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشقة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82048" target="_blank">📅 04:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148135709f.mp4?token=gOvj5GtM_ESWgcPOExVt_2SiMnDPhxgDjqV4ekoqKeHtKnDVPQ3wLegvFpJPb5I83fwItLM66vBc0TAOascYHLoEALyjz1U6g1J8ei3fdR62rPZV6J8893JpKdC1T37IzDBrTow-JaZNsijAorSHwTM7cfYx8exgBqKIXHedlT-wxGPFLtMLF13NAvxDtK97YxQ_Yecjl4_GDfx7Tq9EgBXGkGkWFWPHqnEEzNPKK4SmhyACJBQvN08MuJ12Q29CJEYcSeoZ49bYs1Zh7A7ww-ekgC0Tsow4w1ykPlP61Uyv-jPlfDbzse7x8SYByJday6E34iT6PYHQjS9GK45HOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148135709f.mp4?token=gOvj5GtM_ESWgcPOExVt_2SiMnDPhxgDjqV4ekoqKeHtKnDVPQ3wLegvFpJPb5I83fwItLM66vBc0TAOascYHLoEALyjz1U6g1J8ei3fdR62rPZV6J8893JpKdC1T37IzDBrTow-JaZNsijAorSHwTM7cfYx8exgBqKIXHedlT-wxGPFLtMLF13NAvxDtK97YxQ_Yecjl4_GDfx7Tq9EgBXGkGkWFWPHqnEEzNPKK4SmhyACJBQvN08MuJ12Q29CJEYcSeoZ49bYs1Zh7A7ww-ekgC0Tsow4w1ykPlP61Uyv-jPlfDbzse7x8SYByJday6E34iT6PYHQjS9GK45HOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82047" target="_blank">📅 04:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8FdM6YSc9OWwc3gwdOqo_RKz9OHK1Gn1aiK4TuzMQaRxwVaRIyjG7aodmXKxMOe7y33QLLWmZMHYfbctB7L0z1jG4q_az0zAl8RjQIqTGQ9oc6sQy3xMcMORxeGmGiDluoRdl06pmCtxUmXWRRhjYTyk4gWXHvAs28T_DOURodRDiSgfS4231QckwqnTmFf0RtNd5QxaYFIJ8eYrPJu1MR82ql116ioxLAY7S9o2d3wuokC3PjoD3co81jp7982zzBaFo3_2mMMJnKYO36VDj03Aw0fOSVfSuxmyXKvP8xXInVNlLNsktQYeOfNf3DskPwSwnzqAT_QdxHponpy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشقة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82046" target="_blank">📅 04:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e201c67a.mp4?token=J6O_Gqj-0HOPxb0jlnvzI3itujsENDL2Vxlq4LAptf7ir7WZaRbVJ8bCTZq_qLuc3ciukgbTQi1wdogeVR1zIo2ixsYAcVRQnV3kocc0UueWNLMetVrw6X-pE6ZXUEpT4WTd9qS8MvGGLsBZJoW2qTDwdUNjSILX7WGUmIbUd5hzGcrIRfMt-_03W1Qz4MBKni1585zprNG6RX-fY6vpkz15ytW8MYU7W6dlPCHcp2RrRBBtfYcvI7h1rayPHH6vA6xWfoJqlHY-oYNhqgUt331VGmLZgGrNxS4BMccXb71XwbgkHNYX6cK-DkZQVOYOmaQErF2HsYdTg9jXl21tlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e201c67a.mp4?token=J6O_Gqj-0HOPxb0jlnvzI3itujsENDL2Vxlq4LAptf7ir7WZaRbVJ8bCTZq_qLuc3ciukgbTQi1wdogeVR1zIo2ixsYAcVRQnV3kocc0UueWNLMetVrw6X-pE6ZXUEpT4WTd9qS8MvGGLsBZJoW2qTDwdUNjSILX7WGUmIbUd5hzGcrIRfMt-_03W1Qz4MBKni1585zprNG6RX-fY6vpkz15ytW8MYU7W6dlPCHcp2RrRBBtfYcvI7h1rayPHH6vA6xWfoJqlHY-oYNhqgUt331VGmLZgGrNxS4BMccXb71XwbgkHNYX6cK-DkZQVOYOmaQErF2HsYdTg9jXl21tlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تستهدف الكويت وصافرات الإنذار تدوي بإستمرار</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/82045" target="_blank">📅 04:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd19fdf906.mp4?token=G4UmuQT9SmNJ5xzgCFzU95u6_-CyAGzLAIqfhrqHmQhSrhgF3EudoSiSs73PnuGx2IB6PvtJpgnIjIM7uM6mnR0iOPCbpEJ-_21skL_hacXxFFdXjtwKSBt6ZyVdRC55fGASQOzeMryFQjxyNNnurmFPNjSpTWyzZTkqB2uYRkyIs_LyAJwZiZ5VAfO8c4Y5b8LKrM3Iz0EAd9-hTPGQpd79NZk3zOSihTd6UYhAyvCzt9jWvymVysFjxjdheaAVuSvlJgOc34ucD-SjzD0jZV_bCAT-o35MONsmCXgoV5_mxsftxk0vepMs-PFJhgDfEcAtZQZ4vRSOTtwiILezLRxJMe_9w2QA6hY6AOtCy6rylsOKWIQodEEJY44S23tlcOWxmWFzwm-4NTc_k6c9Nvbq9jGnlwzEnJQ95VeMptmUmn1TzTLfq7m_cT7BeuiC60w_3yGF1TpN8BMFmncFBGDjCaGhZ7KrRxNBhBiL51AdaaQzlVKkgUMAzXrTUX0_dgtj7Iq1BrUdQoGkR2E5lorpZDS881-pQbT9bzV11wqs0XEwR5DIc3w8n_gdN6flq35HkMH_wqLkRVq9cSNV5ekkZano0O-yCCPpaHkYBvY-vqX4sSREltvv8k0QqLxj8uZLcMnU7Q8JcG3MYMmlr9jLj2dZvS1eempdSoQ6kpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd19fdf906.mp4?token=G4UmuQT9SmNJ5xzgCFzU95u6_-CyAGzLAIqfhrqHmQhSrhgF3EudoSiSs73PnuGx2IB6PvtJpgnIjIM7uM6mnR0iOPCbpEJ-_21skL_hacXxFFdXjtwKSBt6ZyVdRC55fGASQOzeMryFQjxyNNnurmFPNjSpTWyzZTkqB2uYRkyIs_LyAJwZiZ5VAfO8c4Y5b8LKrM3Iz0EAd9-hTPGQpd79NZk3zOSihTd6UYhAyvCzt9jWvymVysFjxjdheaAVuSvlJgOc34ucD-SjzD0jZV_bCAT-o35MONsmCXgoV5_mxsftxk0vepMs-PFJhgDfEcAtZQZ4vRSOTtwiILezLRxJMe_9w2QA6hY6AOtCy6rylsOKWIQodEEJY44S23tlcOWxmWFzwm-4NTc_k6c9Nvbq9jGnlwzEnJQ95VeMptmUmn1TzTLfq7m_cT7BeuiC60w_3yGF1TpN8BMFmncFBGDjCaGhZ7KrRxNBhBiL51AdaaQzlVKkgUMAzXrTUX0_dgtj7Iq1BrUdQoGkR2E5lorpZDS881-pQbT9bzV11wqs0XEwR5DIc3w8n_gdN6flq35HkMH_wqLkRVq9cSNV5ekkZano0O-yCCPpaHkYBvY-vqX4sSREltvv8k0QqLxj8uZLcMnU7Q8JcG3MYMmlr9jLj2dZvS1eempdSoQ6kpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تدك القواعد الأمريكية في الكويت ومنظومة الباتريوت تحاول الإعتراص</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/82044" target="_blank">📅 04:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الصواريخ الإيرانية تستهدف القاعدة الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/82043" target="_blank">📅 04:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قسماً بدماء الشهداء سيكون الرد مزلزل الليلة</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/82042" target="_blank">📅 04:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ca3aad42.mp4?token=DZQlK3KRfU7978KitSmOiX80GexQwXnaCSXvxWK2MwnxL1h2cd_g7hRJvxmNYh_q19EBgaUXcwbe_H_X2vNiBk71TBMQp7Se6uMijfh9WzuPduVMr0uBxFc5pHos9reSPTOw89GPQEvxMoW14Mmit-tB2oRYiQWLMACi1phmno7QXHfZWb2ZxjpPx082ZI0SRuDUC2Uzkr9NMqygTUiWH8qSmxeVijJ2mb2al-jauvd7JMude_qIylnBsmnQfblPYiF3ff5n3rmjSGSDJ5oatYzjGXMcBpTnGOSesh4cjJxYKLi-GBCykdim6UwFCq9y79szSXD4O3xXmlupQB-xyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ca3aad42.mp4?token=DZQlK3KRfU7978KitSmOiX80GexQwXnaCSXvxWK2MwnxL1h2cd_g7hRJvxmNYh_q19EBgaUXcwbe_H_X2vNiBk71TBMQp7Se6uMijfh9WzuPduVMr0uBxFc5pHos9reSPTOw89GPQEvxMoW14Mmit-tB2oRYiQWLMACi1phmno7QXHfZWb2ZxjpPx082ZI0SRuDUC2Uzkr9NMqygTUiWH8qSmxeVijJ2mb2al-jauvd7JMude_qIylnBsmnQfblPYiF3ff5n3rmjSGSDJ5oatYzjGXMcBpTnGOSesh4cjJxYKLi-GBCykdim6UwFCq9y79szSXD4O3xXmlupQB-xyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الكويت تحت رحمة الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/82041" target="_blank">📅 04:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6f21cb1c7.mp4?token=KMwn_Kxg_sLDAGRSE9l6rydAQMC2ODfEc9CbCedIRc45wijdh2E_Ys3yjw6xxijg7j8UuPlA6DusYtXY3uU9-2JlAJgu8052UqUryil81P2F05AOtAPsTEbpkdaSrwOU-T3SvLeRZBE9oLvgz5bamMu70KOTYPrsFdmDkVAmXEFMqVoFv6ViM505vNunQkj_2yz5ORR6C19Lw3lDyNOoSYWB0YhHJ4MvmU4jWNeyArgfXjhfsXkC4hn6VJF6JKxwd8-Xe-2X0GJN7sCtUkhYl452TqnECTIux0ppSjkFgmWpYFROMk2D4S_QKPBMbXFHMJcXzEPyFxCNKYDJ9OybQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6f21cb1c7.mp4?token=KMwn_Kxg_sLDAGRSE9l6rydAQMC2ODfEc9CbCedIRc45wijdh2E_Ys3yjw6xxijg7j8UuPlA6DusYtXY3uU9-2JlAJgu8052UqUryil81P2F05AOtAPsTEbpkdaSrwOU-T3SvLeRZBE9oLvgz5bamMu70KOTYPrsFdmDkVAmXEFMqVoFv6ViM505vNunQkj_2yz5ORR6C19Lw3lDyNOoSYWB0YhHJ4MvmU4jWNeyArgfXjhfsXkC4hn6VJF6JKxwd8-Xe-2X0GJN7sCtUkhYl452TqnECTIux0ppSjkFgmWpYFROMk2D4S_QKPBMbXFHMJcXzEPyFxCNKYDJ9OybQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر   سقوط صاروخ مباشر على قاعدة الاسطول الخامس بمنطقة الجفير</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82040" target="_blank">📅 04:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad997e7fe.mp4?token=uS_wqP60Dl93-qj50GrGESmwZDp0khsr3bXeGT64hvsBSqQJSNmIT2rwqQjDUCUtX1QY1JN_dmHe8ZeHtnz5_fy--37Ql9ncEfQNq6jKdVhkmjraEbAV-Q5xdxzoe9xBBH2kMxsyDREjPZiD1A-G3spSS8Wf881rMRLskw54FANHkolR7KnybcGlnlmK4hc-kav-NGAE0R4BQwB2QlofQgVPfgiL9r4NS-8nAHlzYV1nInQr8M77jFPJlSw7tDaxA23Mv2rcXuLc54zSbeTQKybIeZGvv07zIjqH9YgrhezbyQ2MefyG98cBRShvVYHlA45C-H1t2_7xMvl4XnkcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad997e7fe.mp4?token=uS_wqP60Dl93-qj50GrGESmwZDp0khsr3bXeGT64hvsBSqQJSNmIT2rwqQjDUCUtX1QY1JN_dmHe8ZeHtnz5_fy--37Ql9ncEfQNq6jKdVhkmjraEbAV-Q5xdxzoe9xBBH2kMxsyDREjPZiD1A-G3spSS8Wf881rMRLskw54FANHkolR7KnybcGlnlmK4hc-kav-NGAE0R4BQwB2QlofQgVPfgiL9r4NS-8nAHlzYV1nInQr8M77jFPJlSw7tDaxA23Mv2rcXuLc54zSbeTQKybIeZGvv07zIjqH9YgrhezbyQ2MefyG98cBRShvVYHlA45C-H1t2_7xMvl4XnkcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  انفجارات تهز الكويت مجددا</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/82039" target="_blank">📅 04:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82038">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d64941bf.mp4?token=O9BEJFdCsz7NaUM4voo2bfybtT_p6suFxs0GFGWzVtmRx6Ljiskt_Mp6-CgU2-lbEKgwZ45Dfz24TXXgokHt_7qaE7tNOiBamfxy_s0-JM68zyq54boZrx5f2jNo-4ZDCLLNum8Aji_uImdLCvmKd6KAKoHNP4Gtw3AmcxXqYifCRPiZyF-_SgH3UuBNYkQvjMXJY88NEEyt1W96JIy8n-gmZAhSXwrHECWZKzRRPlCgrl171AR4JyuquO9wILEclp3NnqEvjuMRMuAh6qr7kISbDjcNbN1fTVb63gucD7Mk2XDiuxb1VrJC-ZZiAcCBPaLYtZCr3CRgBPoHB08lBaRuBtTnUirgFocdwgeMw1MRs01cqmVEu17b5_Uj0MZJR-Pux2zmKTneRiw6bGc2KbuQCd_vrYYKPVnGdXGVzDxSysBWBklzAoyIDkiER6llyW2KjM77k4ijU9s9runbRl3MgYAc-dckuNxsgofuvlq9Goltdxo8WibMRRlBJqzKVJ66jVcoLOKayNHBeQIYa0MrOeDiMAjBJDW-rhK6a70sbj0Md61Z4nWDhORfmz2aT0o4KslEiV05fynAZOySAMefzXUBnVFEcZkshQVUcat_qQqtwtwi5hEHjFq0BX83uUJ-PnxhHlM0xgQ_sP0k8Go3ia1WkJ0QiRjDD7bRtMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d64941bf.mp4?token=O9BEJFdCsz7NaUM4voo2bfybtT_p6suFxs0GFGWzVtmRx6Ljiskt_Mp6-CgU2-lbEKgwZ45Dfz24TXXgokHt_7qaE7tNOiBamfxy_s0-JM68zyq54boZrx5f2jNo-4ZDCLLNum8Aji_uImdLCvmKd6KAKoHNP4Gtw3AmcxXqYifCRPiZyF-_SgH3UuBNYkQvjMXJY88NEEyt1W96JIy8n-gmZAhSXwrHECWZKzRRPlCgrl171AR4JyuquO9wILEclp3NnqEvjuMRMuAh6qr7kISbDjcNbN1fTVb63gucD7Mk2XDiuxb1VrJC-ZZiAcCBPaLYtZCr3CRgBPoHB08lBaRuBtTnUirgFocdwgeMw1MRs01cqmVEu17b5_Uj0MZJR-Pux2zmKTneRiw6bGc2KbuQCd_vrYYKPVnGdXGVzDxSysBWBklzAoyIDkiER6llyW2KjM77k4ijU9s9runbRl3MgYAc-dckuNxsgofuvlq9Goltdxo8WibMRRlBJqzKVJ66jVcoLOKayNHBeQIYa0MrOeDiMAjBJDW-rhK6a70sbj0Md61Z4nWDhORfmz2aT0o4KslEiV05fynAZOySAMefzXUBnVFEcZkshQVUcat_qQqtwtwi5hEHjFq0BX83uUJ-PnxhHlM0xgQ_sP0k8Go3ia1WkJ0QiRjDD7bRtMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة جدا تهز الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/82038" target="_blank">📅 04:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات عنيفة جدا تهز الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/82037" target="_blank">📅 04:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/82036" target="_blank">📅 04:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله أكبر
انفجارات تهز الكويت مجددا</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/82035" target="_blank">📅 04:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82034" target="_blank">📅 04:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/82033" target="_blank">📅 04:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c47de886.mp4?token=v03CyrtdzcYNlEUS1WmaedBchSFappeVLhF49EVCbvAnqOyy2_sYFOLSG7bulCFi39RBogVBpRlO-vrQabcvtLQAJkd2RbvA1a0trCQYBJGRsV28kCgyEpCvSi3n3S3EYoe7_Tl84c4e5KmhHqz4O5ByCPp1bN1ygAH64XibyiCukhEQRFDhmH6ro0GtsSM5pTTAj6UklUsWndwRi-1pRUg6gNPLPiSpGklXeyG5tmXfJC7XO5O728XVhjWxx_eKnvuDgsD9eMtkNCPzkN0mYJnzE7wHRZDvx20IO6oE8xA5LoQWn57ZJAIz8nGcmoSLUtsMDg87-dOggrixMOP_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c47de886.mp4?token=v03CyrtdzcYNlEUS1WmaedBchSFappeVLhF49EVCbvAnqOyy2_sYFOLSG7bulCFi39RBogVBpRlO-vrQabcvtLQAJkd2RbvA1a0trCQYBJGRsV28kCgyEpCvSi3n3S3EYoe7_Tl84c4e5KmhHqz4O5ByCPp1bN1ygAH64XibyiCukhEQRFDhmH6ro0GtsSM5pTTAj6UklUsWndwRi-1pRUg6gNPLPiSpGklXeyG5tmXfJC7XO5O728XVhjWxx_eKnvuDgsD9eMtkNCPzkN0mYJnzE7wHRZDvx20IO6oE8xA5LoQWn57ZJAIz8nGcmoSLUtsMDg87-dOggrixMOP_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملايينُ المعزّين يحتشدون في رحاب أبي الفضل العباس (عليه السلام).</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/82032" target="_blank">📅 04:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82031" target="_blank">📅 04:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صواريخ إيرانية تنطلق نحو القواعد الامريكية في دويلات الخليج الفارسي</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/82030" target="_blank">📅 04:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253e3928b7.mp4?token=g5Lih0rUabbYVLymgc6DStLT3HNmJ2E2YyoNES6D8nRSeqmuVlsewu8NHgvcIlLfp9hSkO4mjp0C9FMMW6s9cVKZce9ryjgaGkLfVMwNnvv7EcmFsNuY-MpCTaoqPhJsz2vlVEW58vRIhJdAPu44tNWfl-Cx5YmOrJ-KImDlu1znh_gSGrJ3YKR51znYX7TxuyQAEEDYyoBz54Y1_KiBN3B7Q2Sa9l4C88WuGm0DE4gLC-5Kqi_S91NFkalqFrN1I5MmwDNTNnfJ8pzoEwYi8bRMy6m161hlpEmxILkaCVarlzUCwZyyDHl92eeSBgV2IxASXOo3Y1FNBFRT8x797w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253e3928b7.mp4?token=g5Lih0rUabbYVLymgc6DStLT3HNmJ2E2YyoNES6D8nRSeqmuVlsewu8NHgvcIlLfp9hSkO4mjp0C9FMMW6s9cVKZce9ryjgaGkLfVMwNnvv7EcmFsNuY-MpCTaoqPhJsz2vlVEW58vRIhJdAPu44tNWfl-Cx5YmOrJ-KImDlu1znh_gSGrJ3YKR51znYX7TxuyQAEEDYyoBz54Y1_KiBN3B7Q2Sa9l4C88WuGm0DE4gLC-5Kqi_S91NFkalqFrN1I5MmwDNTNnfJ8pzoEwYi8bRMy6m161hlpEmxILkaCVarlzUCwZyyDHl92eeSBgV2IxASXOo3Y1FNBFRT8x797w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إيرانية تنطلق نحو القواعد الامريكية في دويلات الخليج الفارسي</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/82029" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc790dac33.mp4?token=lXMDSkwaLf47pNmEgJMk-uaPt4EokJxwp5kFZy0isgCt8VDY-7sofa6qXtOTAsDkyoFSBTc7GLX9q-so4YO5DRXDeiScxgacavCeRbKE1DIU5ikRWD7zlGvaZpb_ps72UDXQwlsUS6NyyFRDEk4kf8naq3wlp_AextRhhKWCZge1tLy10D5UnD1IdREqQjlbDXvRJelEKcH0uTaCJETXWJ9dxt8COuwJKc5iBoBhEclfk2udwlYhML8Lk_yohBtYL2oO43CU_JjthoiehuEi94q_iF7rokZSyqnJeY33rgH7FN4scbaeanLIGGDaMVJycRPTI3YTEdvtTegVAbHI4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc790dac33.mp4?token=lXMDSkwaLf47pNmEgJMk-uaPt4EokJxwp5kFZy0isgCt8VDY-7sofa6qXtOTAsDkyoFSBTc7GLX9q-so4YO5DRXDeiScxgacavCeRbKE1DIU5ikRWD7zlGvaZpb_ps72UDXQwlsUS6NyyFRDEk4kf8naq3wlp_AextRhhKWCZge1tLy10D5UnD1IdREqQjlbDXvRJelEKcH0uTaCJETXWJ9dxt8COuwJKc5iBoBhEclfk2udwlYhML8Lk_yohBtYL2oO43CU_JjthoiehuEi94q_iF7rokZSyqnJeY33rgH7FN4scbaeanLIGGDaMVJycRPTI3YTEdvtTegVAbHI4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في سماء البحرين</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/82028" target="_blank">📅 04:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7109ebd34d.mp4?token=WjLv-9coaiiLzerMg3K-ezouqISWmeAXyI4WO7mA32-xZnzD15pShy-lJrw_E2drDKrVXfaAPBDi_EoWuJnDG_-uln3jGkVKn_BzXS4A5upx7fb9-luLuovD0-Cbqod40eIOqrE6Lcfy7_geROe2JMjMewrmRD6ZsrxhfIbiZMdjbSdZaRpRXwnGwXXV7NDNUynjAQj1bLyQQXsVRgO9Ec1baxX8Y2gKTNuRA5ElJR5nzfW7abscQ8b-wXX1U7rxZST9-Xh_4B6zRMPgrFu_QccO4pgTr1hA5t5ZW1e0DdwacyheoBMO8Iv-xQm8tk6BI7DTCB73SbJgXvuBvxUNOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7109ebd34d.mp4?token=WjLv-9coaiiLzerMg3K-ezouqISWmeAXyI4WO7mA32-xZnzD15pShy-lJrw_E2drDKrVXfaAPBDi_EoWuJnDG_-uln3jGkVKn_BzXS4A5upx7fb9-luLuovD0-Cbqod40eIOqrE6Lcfy7_geROe2JMjMewrmRD6ZsrxhfIbiZMdjbSdZaRpRXwnGwXXV7NDNUynjAQj1bLyQQXsVRgO9Ec1baxX8Y2gKTNuRA5ElJR5nzfW7abscQ8b-wXX1U7rxZST9-Xh_4B6zRMPgrFu_QccO4pgTr1hA5t5ZW1e0DdwacyheoBMO8Iv-xQm8tk6BI7DTCB73SbJgXvuBvxUNOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/82027" target="_blank">📅 04:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWQY3wStGqkmEPlKPzqTfJqIs2wQHe1MVTph-7tWcNrzhHorQVCAOam7Hs_9R1oDdJ6Go0cll1_um78ITdJnFFj3SG1bQYTiWuo0rrXqtpSywkx2BxfeUFLzlwhvNBqYrjR-qqEUZyPMqeRQymj4MgKkerl-3uJE3NCrjnfuQJJM2xpJ3DmGzISF6iAZFdPMuOPFcA4Zj3lH49NhHGorqy0vQMMsVp2jW0lFspRH6zKf7RVPYJ6SEoPwobmc4GeYR4WgFf2P0qZ3kakkh6U0Wa6fFK4QFUeDd1qzN7p4YvuiESvw39qqJ01bWtPW29mVdwEM0Ba5dDQCiUUrXG-6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم صاروخي كبير يطال القواعد الأمريكية في دويلا الخليج الفارسي</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/82026" target="_blank">📅 04:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7ce27842.mp4?token=vllkwpkapR3-s4rePSP3hzbX3QBFs8cQwta0G_p0CFAQDe6lqOewf_FwzMZR3-qe8FE-5D7nAgU96BPgbjXy64RHU2sstglALg-tDP5dpEVLXfmYHA1tuN06ProkvtpYl5ARMtC5rV7oI81-1K1VnV9JWG4PyqnUuy6sTHDS5Y8KhfTBNz-lgFgt3_esHfVF9onxQcAiXWUhYMWJ0PbuVLLxBhKizimyyfv9eUKrEIeL_iCeSDDAUPwUKErRhWEgDcKlKZnwSYX4gogJinEW8W0PKlsIEFB17OxgKad6XsESBW36MAn2gQeuS47RofHeqNvZhkIPX1QxpO8cGjsilA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7ce27842.mp4?token=vllkwpkapR3-s4rePSP3hzbX3QBFs8cQwta0G_p0CFAQDe6lqOewf_FwzMZR3-qe8FE-5D7nAgU96BPgbjXy64RHU2sstglALg-tDP5dpEVLXfmYHA1tuN06ProkvtpYl5ARMtC5rV7oI81-1K1VnV9JWG4PyqnUuy6sTHDS5Y8KhfTBNz-lgFgt3_esHfVF9onxQcAiXWUhYMWJ0PbuVLLxBhKizimyyfv9eUKrEIeL_iCeSDDAUPwUKErRhWEgDcKlKZnwSYX4gogJinEW8W0PKlsIEFB17OxgKad6XsESBW36MAn2gQeuS47RofHeqNvZhkIPX1QxpO8cGjsilA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي كبير يطال القواعد الأمريكية في دويلا الخليج الفارسي</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/82025" target="_blank">📅 04:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قسماً بدماء الشهداء سيكون الرد مزلزل الليلة</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/82024" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الداخلية القطرية: مستوى التهديد الأمني مرتفع وعلى الجميع الالتزام بالمنازل والأماكن الآمنة</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/82023" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات في الاسطول الخامس بدولة البحرين</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/82022" target="_blank">📅 04:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3399905af.mp4?token=uGcTCgursSvCwvBA5i4tM5z9fh26LNUy3F3YvzbqFmJ6zLuOnB8VVdkdZqtjm-BMB2sj2rlZrakQxvQQ2oHqdj65eyuFTQMJKjUt-ICkJ5RjIdBmMv2sNkQt7sXFR_LTFPUW-u0dYEupeIW8fxe-RLnLjGOBywn4HFAptubMVGRZQ5iay4rIpIKTJK-sjcqBkHQ7Tm2yls_16UZyxNJUZSfrpcYrzrVtYtScm49neNBCaxr2FwWY9eSoWgCmQC5SKHrUbPJcl4Cr1k9i9r_uV7quOMVmHJdKBoapdknZG6Sm7XHwgpQKuaPQw1_TbqWaWVjxGHFx613xEsFq3X4v7S1W5QZSDnNCT2ca1tBtAAMuoZbt3e50i6UWx-Voy9FFAKMEipioje-wa7B4KQ8fbfIO5fQEDPG2W3QtYSAuGV1Y572XdD2sQFW3mf06D9LkMf8iU2O8WomOeqGQP2UTjiTTCzgy7F-ZCIh0u4MyL3zUnVBlcHQE_ehsUg6GyCMlmpXp0hNmBhom8aLf3RNtaLhA8PPVKjqSq3dT-E6snF4qDkRfn8NgRwNU7jAt8dJL8jGrfyOl6kuXixyIvdU2qOcYr2c0tRl7g5fXy4CsIhHgUk0sSeTDwVxaU_3nGrfjyb8kf_Am4LFkc8UZIAw75qSvFevkwTHlhlucLVEo8aI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3399905af.mp4?token=uGcTCgursSvCwvBA5i4tM5z9fh26LNUy3F3YvzbqFmJ6zLuOnB8VVdkdZqtjm-BMB2sj2rlZrakQxvQQ2oHqdj65eyuFTQMJKjUt-ICkJ5RjIdBmMv2sNkQt7sXFR_LTFPUW-u0dYEupeIW8fxe-RLnLjGOBywn4HFAptubMVGRZQ5iay4rIpIKTJK-sjcqBkHQ7Tm2yls_16UZyxNJUZSfrpcYrzrVtYtScm49neNBCaxr2FwWY9eSoWgCmQC5SKHrUbPJcl4Cr1k9i9r_uV7quOMVmHJdKBoapdknZG6Sm7XHwgpQKuaPQw1_TbqWaWVjxGHFx613xEsFq3X4v7S1W5QZSDnNCT2ca1tBtAAMuoZbt3e50i6UWx-Voy9FFAKMEipioje-wa7B4KQ8fbfIO5fQEDPG2W3QtYSAuGV1Y572XdD2sQFW3mf06D9LkMf8iU2O8WomOeqGQP2UTjiTTCzgy7F-ZCIh0u4MyL3zUnVBlcHQE_ehsUg6GyCMlmpXp0hNmBhom8aLf3RNtaLhA8PPVKjqSq3dT-E6snF4qDkRfn8NgRwNU7jAt8dJL8jGrfyOl6kuXixyIvdU2qOcYr2c0tRl7g5fXy4CsIhHgUk0sSeTDwVxaU_3nGrfjyb8kf_Am4LFkc8UZIAw75qSvFevkwTHlhlucLVEo8aI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82021" target="_blank">📅 03:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجارات في الاسطول الخامس بدولة البحرين</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/82020" target="_blank">📅 03:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4mZvYDK3dYB_wbNQd61aCw6h6X2PlRCQ3impP92niTPvTbxzu2p5G6K4uUeWOGCOsw3bignDYG2o-05wH_2M1lbKV429xnJtq02h_K97GhpMhM5Y7n1hzRUw5ModAdqJlHfNMXLyVxUvUpYK2pm2XBD-0QVfO7XvBCph4oWKoGvh81zg19CXYTH5BKVVrmRiHHjEjG82xHWcibxANOklXe10Kd_-sxAUYyc4qU-KTvWr0k9k98uoN6AEkvAhltqJotEL3hcJpXOVD8r9NKCaj0b8bRqwGajnO5KOFtGop_hWIPetHsz_ColP0AfKunFb3WOLP0ydebi3hjv6TK82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYCwRpCl2hWdr5Z9vWclJpCX1bRxQWQD_prL74VGjhNsBvXtxsmV5c2A-7mrW6dcCBeFm0G3RZk1rK9G1VZUNl57jfp3T9zIbugXuvY3PmhlX8klRYVEGqgufkY8_r1bCYwy667VxnrZ0hP2mwlS4BN07wTPpdcHUmOfXHQe0eZJ7GgZfpuJCUBJ6azb7fEm7VtUSdko8sBjWrsHbzFdWS0svUgRDwahjytR8_IpCC-pSEEF6eSVf0oTiVm4NVP6lczqhOYTN3NKNDNXep1Zv1kHLF1ZRwlzuikGTSU_xUq8nkI6QgQVPOFpP2uN9kWVzabr6yS0ZgN9SyWFOPBRhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0lY1fZ-21SyGCZ47hMe0okRy_qVafUTB6VdP8gGI6Z9KRCfH5oN7f7f7f66iGySob5yBcXI3kILkUS0-NH73AuAkYRIFHV367_Lzs08fZt4bPWTFzJ0QUr_cbgEY6sfSYcySqY-hQ0yh2pJurD0Q3FumcxwI_xBbGGRGXpXqXw-x3pgfQE0XKofx-tKBgeCess27_nCgf2G5XZaVg4TOH6unOkVoVnRU6tk99TFeukkJ3rmo1Rdb335XvkqBR9yvtdyh7tUkMYRql1GO3xm2ruRpqo5uFhwc4rzBXugayG7ktBIFSx1AATqcK8Hg4MUIoDeuf3Q8Py1vYGeRvXqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGZrskt1q6qJZhzEYQDCCysg4mbipJ3e_LiqlT878-4UvH7SxMG9ljTrK39rVLPd3TUtxxUjWDj7Gi_YYotAqPpC-JGeLwI_RwWyOv4bW8RV_beEuFlfn8RCaetl8sDrRrsskSJqF9mQ_aVly-E4_n-RJtxdxbFdZKXHuk9_i2vhKn_osF6e_fyAEx_uc6VHBeKEs_W8IT7QLp6haqla9bKSjwVYpxwPQJ3jFiO0V5YIZBvN7O117LWb8WUcL973NQJjz_2RmAVXnSNbGzkMJjTUGvPmJDc8fhnOvX6vDuCYBng2nqkw1rVyIudCtaiV6YESIFrez8KrO6fx3jpNsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النعش الطاهر من بين الحرميين الشرفيين باتجاه حرم ابي فضل العباس(ع).</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/82012" target="_blank">📅 03:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e77f3dcf6.mp4?token=bYHgBts0yfVrwnxU9JznpYLa1D4w9BqzyL6aNVOWRpde_k048fy5o0D2dEUen2vjYZdLan4FFxFxqR7TPluB6sZNVroQGW1yh183UtiBoLcLzuAnCcY_y2xw5oGkf4g1jTzcdo0ru5XJsNBY8uBs5j70o7ZvW2ZIAuOeLcN_kHjLoK-M36GWqgrOfbUBI2bmVunFEKw_Ou2iRAvOA_7FHw7GWSILOJtUdLU2sZlC31R-V7l__rTVQICLpOQiEPXTMTqHk5GzSMI-GudRoBxlmNnNYmjmgsIZVsC3H8ckzwQUbj9OhmUZALtY401wru-C_mPwOLWarHJDNXmpD5Allx3wfT7XdB56J623eL2EQrMFFKVzkIr4pgwuG5ohFkfO3BihoBJfGjBUYKnlDT-vhkusTHxqaKpUS04oz_O_Z9iefmqon5v6NGzDAsB6Z8tkskQCYYDIsXD-PTze5ZXbBxEN5ZUn0gxrz_477-dZg5eSA_rVE8zxiB4oy-SdVPXPkOoPdzWHUiBF2odK2JPIHhzsWbTrEL_1LF9oizVAYL7w3mk-vWQiP-KhAndPSojVtsybya35sQn487wz61R9MYHHv80qIZyKxHNCpfrf6ch8CIsr22_QFXimSnIuE1j-Gx8AhqUAulwOLAaXNsKVU3ImpnhjilQws4EB7AIPGSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e77f3dcf6.mp4?token=bYHgBts0yfVrwnxU9JznpYLa1D4w9BqzyL6aNVOWRpde_k048fy5o0D2dEUen2vjYZdLan4FFxFxqR7TPluB6sZNVroQGW1yh183UtiBoLcLzuAnCcY_y2xw5oGkf4g1jTzcdo0ru5XJsNBY8uBs5j70o7ZvW2ZIAuOeLcN_kHjLoK-M36GWqgrOfbUBI2bmVunFEKw_Ou2iRAvOA_7FHw7GWSILOJtUdLU2sZlC31R-V7l__rTVQICLpOQiEPXTMTqHk5GzSMI-GudRoBxlmNnNYmjmgsIZVsC3H8ckzwQUbj9OhmUZALtY401wru-C_mPwOLWarHJDNXmpD5Allx3wfT7XdB56J623eL2EQrMFFKVzkIr4pgwuG5ohFkfO3BihoBJfGjBUYKnlDT-vhkusTHxqaKpUS04oz_O_Z9iefmqon5v6NGzDAsB6Z8tkskQCYYDIsXD-PTze5ZXbBxEN5ZUn0gxrz_477-dZg5eSA_rVE8zxiB4oy-SdVPXPkOoPdzWHUiBF2odK2JPIHhzsWbTrEL_1LF9oizVAYL7w3mk-vWQiP-KhAndPSojVtsybya35sQn487wz61R9MYHHv80qIZyKxHNCpfrf6ch8CIsr22_QFXimSnIuE1j-Gx8AhqUAulwOLAaXNsKVU3ImpnhjilQws4EB7AIPGSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر لشهيد الأمة في منطقة بين الحرمين حيث تحيط فيه رايات المقاومة الإسلامية متوجهاً إلى حرم الإمام العباس عليه السلام.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/82011" target="_blank">📅 03:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24ac4fcf4.mp4?token=DHqOvj8ZjcRWxiCVeeV1T-q4xRD1WVXqiK4WORid7rRxFCr-n0TKgnJIYoYnWwWalM-Q5Tkauc8uvXDq2rwBBWaXUdpfo_k2aR796YbtVxIqwZiGiYrlL8w8tm5Py7ZZreKpynXPbqtbFubjHryRg7i18QEmihmpGxoWAFC339qOOG3mXdLFCO4oT8BtjwAjS6sf_fzqFCXIxqeNE5owGZxCujCUu0PV74A1VmlcLFk9_toZh1iIHIsJAgDSNty7wspG2H9xlP0OOpE_6SKU8SFJI7F14kMXn2gztbPVT1sAH9-Iqutp8_c-jzqMDwOjUmJGkfY0f4QxydgP03EyXUBwqiP7zHq0vHdxX0josWBwlFp8t5SrCNzfKJbeFVLajFWUlmWnxHXQ93C4zJWcmI8aJEYfs8819OjS_-wXUEJROmK0CKpCjG6jsgkfTf0oyz_QI6idMThjRmJFGCG9XUA0zsYGUXgGvADRIIz0-EsvVSW3qVKB6H3x2eEizoTx0aXVur1FJLjwok6wjmGgjCgl5HY_damVkZlcx7UyD0dcN1e8GGep42vds41YSHx3XusJZBYhbLOOVq654H-wITWJNAmuYNiHacVEmbKK7O4lQDrxH8UHtutVbGBjB4ewF2aIE7OHhX9C0DqPJz69M4NgXDh76DdT4Bpn-bLCFRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24ac4fcf4.mp4?token=DHqOvj8ZjcRWxiCVeeV1T-q4xRD1WVXqiK4WORid7rRxFCr-n0TKgnJIYoYnWwWalM-Q5Tkauc8uvXDq2rwBBWaXUdpfo_k2aR796YbtVxIqwZiGiYrlL8w8tm5Py7ZZreKpynXPbqtbFubjHryRg7i18QEmihmpGxoWAFC339qOOG3mXdLFCO4oT8BtjwAjS6sf_fzqFCXIxqeNE5owGZxCujCUu0PV74A1VmlcLFk9_toZh1iIHIsJAgDSNty7wspG2H9xlP0OOpE_6SKU8SFJI7F14kMXn2gztbPVT1sAH9-Iqutp8_c-jzqMDwOjUmJGkfY0f4QxydgP03EyXUBwqiP7zHq0vHdxX0josWBwlFp8t5SrCNzfKJbeFVLajFWUlmWnxHXQ93C4zJWcmI8aJEYfs8819OjS_-wXUEJROmK0CKpCjG6jsgkfTf0oyz_QI6idMThjRmJFGCG9XUA0zsYGUXgGvADRIIz0-EsvVSW3qVKB6H3x2eEizoTx0aXVur1FJLjwok6wjmGgjCgl5HY_damVkZlcx7UyD0dcN1e8GGep42vds41YSHx3XusJZBYhbLOOVq654H-wITWJNAmuYNiHacVEmbKK7O4lQDrxH8UHtutVbGBjB4ewF2aIE7OHhX9C0DqPJz69M4NgXDh76DdT4Bpn-bLCFRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من توجيه النعش الطاهر الى حرم ابي فضل العباس (ع)</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/naya_foriraq/82010" target="_blank">📅 03:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f8450f5f.mp4?token=CcgKz8Gl0Gy99XjiD6LLgZWmZfa5cJxLXR0B0Y28t2jFziIc1OCmKPR4AO-6jaFA3H8JFekfdSNO2X0O-1F5FJoJDvD3gkzIAXNKK66isoIJve-NmjuTIGLdW3nhZNk4NB_ctrIlv4T7-mq42jZwDeapYo6FqJHMOgu0hyR59JbPtW_4j5Sh8xx8LGYM5F9mP85fHIyv2lCvwpMyhCCossDslcABE1QcUn-SB0YS2v_ZrATmxg8cAEfbdxz2-RvUHwcVTASpklCji9ZRJ4NWFouCV9JeP2N5xZu6IM5vf99aTUdaYfVZcN7Dmu8i7NNtU7sU-NePNUAPVdIwnfsgT44w-5_giaTIJt34J3T-FPiFISwYk0DC2-33XlML56h7yZ0gWKQ-Jfkl1aDA4U2Z40r0AuZSBwLUL0lfa1sZrE4zpyRNWattpxHt60Dua6sVPfRsT_3oOthbrlDvxQI75bOPTrZNgC2Jw0whPM2IwHdGegW3Nif14KYrXYTkQhrnX3LhuquX_Cu7XKylLI6UwJOY_wn9uC_0CAlCIdSIeMH8mZ15QBdZPnyCgvW7zl20E2lE8OmxNnQlBzBu--cONZVhf_dcWRSC0KGw2-eshu5m9fCKLGQ_d2A68h5tAmTewqdj5SVryzPdw0dASKuaA2dBaKew5vVupJo8XSVxeg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f8450f5f.mp4?token=CcgKz8Gl0Gy99XjiD6LLgZWmZfa5cJxLXR0B0Y28t2jFziIc1OCmKPR4AO-6jaFA3H8JFekfdSNO2X0O-1F5FJoJDvD3gkzIAXNKK66isoIJve-NmjuTIGLdW3nhZNk4NB_ctrIlv4T7-mq42jZwDeapYo6FqJHMOgu0hyR59JbPtW_4j5Sh8xx8LGYM5F9mP85fHIyv2lCvwpMyhCCossDslcABE1QcUn-SB0YS2v_ZrATmxg8cAEfbdxz2-RvUHwcVTASpklCji9ZRJ4NWFouCV9JeP2N5xZu6IM5vf99aTUdaYfVZcN7Dmu8i7NNtU7sU-NePNUAPVdIwnfsgT44w-5_giaTIJt34J3T-FPiFISwYk0DC2-33XlML56h7yZ0gWKQ-Jfkl1aDA4U2Z40r0AuZSBwLUL0lfa1sZrE4zpyRNWattpxHt60Dua6sVPfRsT_3oOthbrlDvxQI75bOPTrZNgC2Jw0whPM2IwHdGegW3Nif14KYrXYTkQhrnX3LhuquX_Cu7XKylLI6UwJOY_wn9uC_0CAlCIdSIeMH8mZ15QBdZPnyCgvW7zl20E2lE8OmxNnQlBzBu--cONZVhf_dcWRSC0KGw2-eshu5m9fCKLGQ_d2A68h5tAmTewqdj5SVryzPdw0dASKuaA2dBaKew5vVupJo8XSVxeg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توجه الجثمان الان نحو حرم اباالفضل العباس عليه السلام</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/naya_foriraq/82009" target="_blank">📅 03:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68689a2ee.mp4?token=uyS7ivaCkiW-T7ZKYhtffHF9mU7C03YL6cImoMBnE_sHhlAil-VJrXXIsf27YiO34UtWdHzP5kie5zOeN5YJr1ZLzoind3sfx1hAAHOyQxF3CmgQ3M4zIGx5BP6b4B73sFnUgJMRnvT-e6SYU403EotbRgJNz7IrZs2BBC4WK2K0s6cnTPKTFHwnc2-kYTRwTPnn8t25SWu2_25PbF4uu6z2ODH1hjtdVtaVyukiW8QhYj7C5zYei-7QHpD8mK_do5fU4u_c1-OFQAdDyLbM_jMT_UGHDLZ7pSgkEEZKn5lm5L6dnZiuhnCUwQPZC8CCNBq3FKna2H73MIAyFnHRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68689a2ee.mp4?token=uyS7ivaCkiW-T7ZKYhtffHF9mU7C03YL6cImoMBnE_sHhlAil-VJrXXIsf27YiO34UtWdHzP5kie5zOeN5YJr1ZLzoind3sfx1hAAHOyQxF3CmgQ3M4zIGx5BP6b4B73sFnUgJMRnvT-e6SYU403EotbRgJNz7IrZs2BBC4WK2K0s6cnTPKTFHwnc2-kYTRwTPnn8t25SWu2_25PbF4uu6z2ODH1hjtdVtaVyukiW8QhYj7C5zYei-7QHpD8mK_do5fU4u_c1-OFQAdDyLbM_jMT_UGHDLZ7pSgkEEZKn5lm5L6dnZiuhnCUwQPZC8CCNBq3FKna2H73MIAyFnHRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توجه الجثمان الان نحو حرم اباالفضل العباس عليه السلام</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/naya_foriraq/82008" target="_blank">📅 03:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الجثمان الطاهر لازال في حرم الإمام الحسين عليه السلام</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/82007" target="_blank">📅 03:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894a77b4d.mp4?token=WMbP5oTBkElTL8L6EbbzkuevjhFtvDA7W8CqrCA69E4CazgSAFX1ua2fazzEnaT4uu24LYxtpR2-cLBISvnwSImIgfA_8-ZFwalOT-1UtkvQzSjpvNYexkAHbmLsEups1FBaBwgRgIADom3CaAoMCFPDOHJhi1Ihk_99RZvQO1t2WtDgztgUBSWuhADmZt94L8-wZBFXTVE9vHHVSka2OHXPyfXgFSv2TNiOftEbwOd41nLscSXycQtxhuxQFsxAO5S3FOidCOaBpXIVbbFITfA7c6Ki39zJtZuZvNpC2R0BuOW5CCTM9Hb1wyBsfqtsW1MNJH0zo62MElvp7vGFDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894a77b4d.mp4?token=WMbP5oTBkElTL8L6EbbzkuevjhFtvDA7W8CqrCA69E4CazgSAFX1ua2fazzEnaT4uu24LYxtpR2-cLBISvnwSImIgfA_8-ZFwalOT-1UtkvQzSjpvNYexkAHbmLsEups1FBaBwgRgIADom3CaAoMCFPDOHJhi1Ihk_99RZvQO1t2WtDgztgUBSWuhADmZt94L8-wZBFXTVE9vHHVSka2OHXPyfXgFSv2TNiOftEbwOd41nLscSXycQtxhuxQFsxAO5S3FOidCOaBpXIVbbFITfA7c6Ki39zJtZuZvNpC2R0BuOW5CCTM9Hb1wyBsfqtsW1MNJH0zo62MElvp7vGFDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتيجة للتدافع الشديد والكثافة البشرية، تم توجيه النعش الطاهر بالعودة إلى حَرم الإمام الحسين (ع)، لعدم إمكانية المضي به وإدخاله إلى ضريح الإمام العبّاس (ع).</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/82006" target="_blank">📅 03:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82002">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-RLOxauJzPhVF9nlAIZ5I0-rkXd8E8oLoTX6S3F6yUBVFRZS8EBxGo-sw_ajPo_N1JWE517QsVzsqbLEfUR50PRb7GDeGtTQWCQRFex57Iadl_7b6mUcXYRL13mQilN047ytaJCoSnqLW-QsgVioEjMXcH9tamA5qzxyjxsXBNaxWhDoTX4RPAB6yAn73j3sQPkaq5zOgpm0aCrt7K4qoMuvoI6aaTf6jGwYVLVU7c83o-yTwbkldVEjA8-PG4E60edDDx_xSM1L9-1IFhNpnT3khD2dUOdKAHMUf3ykk-zAetL8sc45BKyu0u1KSTHYTHAz68B7YeeX8iquxtVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVoDOwSpX4_QvoNeQX3M1SrZh80CYCYL67NW_8dcxIk9REjbSOxLVUZuQjP2lq_LhbyBZP9VAmlhxvcEqbswudhTpKssAXQN7e1B_aEUCriWOisELWyRs4SWRzEyzixNG1UERujUC7ImsaltbI2JCZ6c5tv11BI7EiuZx_q8K4KNpX0tc_6Fz92gcIGuDoZ8ywnHqg0uCGWpWMgXjQpE4YH4RfcOhgdHLuL5FlvEhy-X_X_V5973kPUUquoWDCk5zyzUr1QVNMyOgxuiy-1yzQbyZMVleTjXqJhkm5JMZqjr2JH5dfH3PDiDNST9xewbQ3x5rqpJ0vV2NOqPF-BVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLRcJdKvoc2frCkP2zT8RU2E9QX45Wp9cLKRPQHhoM6bEZmnJatqVDGe3j0pQ4ftk37_6tlQ20EDX0r6QtCf0sf-FT0sFeLsBHnlwEgC5WHkL1Wm4M1eyG4szcDI96LEbpRW8clEyLDgODMLvugGgJUJ94Hq7bZqjbI1CQYfHx4M9tJavyZVg0GEqrZLk2dWgZHkHor1Ws0WLvPAnEpBBSHgMXYEaby8F7yNAnJSgU1HeQ8U2Y6i-jjrC7EDNbVtEqpoqjRRMFFsAlqnBBtdgz4ya0aLGF-N8Gl3c7SLnL_aQ-bDoEIfitryMxxLD7828_ghtJe5cU6PZZqA1UJlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggzGilN73LLLsFtgk25Wciy0hTGSOKfQMv78NscKg1Re0PORKwEc7rrexFr9bjTkmKm4uTEzWbHWCAAc2K9_pkUvkJyLTwfn9quiXV90SFdf0j3wqDT2HqxLXHiEtNkjOmtyGqUrneCe2u3_uYdukxNi7mOPDPg9v1rv7-3vYDVhpBAdehcXybeJV6QEAfHLVjPbvvNHW8xVFItdlIYwAubltxFZLPJ9V1SmdVNHxMFDezywpzpQx6F9aLFqeLtHkQk0G5EJBwtbqq69lZPeAR9ZFizr33K1CJwfDj9KCScYOg21accY2PlA4wC6gc279I-JJwSE3lX8IPY30nyLog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حشود هائلة في منطقة بين الحرمين الشريفين</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/82002" target="_blank">📅 03:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82001">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بث صوت القائد الشهيد الولي  السيد الخامنئي في صحن الإمام الحسين عليه السلام وهو يُسلّم على سيد الشهداء</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/82001" target="_blank">📅 03:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82000">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b07576336.mp4?token=ge77vEO_HkNijsWFKhSeG9XM8KAclEYHCGDqCh1sJl7qyRGM5zHFnZBAoskYmyIkiSum4-VMf_pnZ38u3O__15eNq96lHeIQM05gbniVRIhpoEB2-Lmwj8MIpCO5L94evr_vUXmqwhuwED1pabI5RPhtibZwjLEz2ntvwEJB2N0uStEaKxTSlXybrmx6zlMLQgdzYb5NxWQdlHx6vRdy1U6DhnNk1peSI6oRcl-qLABeOVxhSiq-dKUkX0sBQSRNjhUAW7rL54DJegyHHnFF8E_8Q-SdlQgijl3gBr59IXIfF2mkVQLDJWquLvOrxhxOXgxpWOZQhpUn4e5D0uD4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b07576336.mp4?token=ge77vEO_HkNijsWFKhSeG9XM8KAclEYHCGDqCh1sJl7qyRGM5zHFnZBAoskYmyIkiSum4-VMf_pnZ38u3O__15eNq96lHeIQM05gbniVRIhpoEB2-Lmwj8MIpCO5L94evr_vUXmqwhuwED1pabI5RPhtibZwjLEz2ntvwEJB2N0uStEaKxTSlXybrmx6zlMLQgdzYb5NxWQdlHx6vRdy1U6DhnNk1peSI6oRcl-qLABeOVxhSiq-dKUkX0sBQSRNjhUAW7rL54DJegyHHnFF8E_8Q-SdlQgijl3gBr59IXIfF2mkVQLDJWquLvOrxhxOXgxpWOZQhpUn4e5D0uD4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان قائد الثورة الشهيد يتجه لحرم ابي الفضل العباس (ع)</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/82000" target="_blank">📅 03:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81999">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">توثيق يظهر تعرض جسر في مدينة آق‌قلا بمحافظة غلستان شمالي إيران إلى قصف أمريكي.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81999" target="_blank">📅 03:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81998">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بث صوت القائد الشهيد الولي  السيد الخامنئي في صحن الإمام الحسين عليه السلام وهو يُسلّم على سيد الشهداء</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81998" target="_blank">📅 03:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81997">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5kGUn9bEgVcEtxQiiQ4mbXvCztBkepePQMvIjB7xbRcA592j91LHdkxQ1CEdYeTMGa3Z5N7dcMDAdZKXYmoEF6r-g_ZGzWkVu5FbPTDj-5UWm1-6kW2YPSoIgZU5lztRdawlh-WEUAHe_4pBIBGGHNHU8dWWqXgfNlJj1Z331SK3U0wl4cjUMc14o7soZZCrV3g6v0C_2nGOPKn6b0kM2f4LtiNoJj4uBB3jgDcBj4rxWUflGiktZzhcQb8E2gsPmJovsWlOjDjsmnczSU_sZ8rYzPyZatqwxu_6Ub8NeVPUdnOej17DbA-G3B3PCig-kGbX8SCpuTbrctJUGWCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظة دخول جثمان قائد الثورة للامام ابي عبدالله الحسين (ع)</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81997" target="_blank">📅 03:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81996">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c86d070d3.mp4?token=qrV6E1auclliwldtoBpEQhAQMfAibKZWmJUWxVkRfaZvOYsWf07KAUDMQzoKt2jvJa5fqlAMau_HA2rjs8614CgcSzSrMTJTKat3P-9g2KhQ2c2RK_VWahUrSb8eMEFUlaFHbXCzNQCzjPLU8unZB1x8rTnHGdMvJxdFtR5XIVIXiK0jTvDuZAo8FCMIwlfdNFqImu-z1RDWXAJ0MukgJ0Bo-exx3I5B-z12GkUv06BOUvjpg26XQeEALj5IH7kYyD_A6V7z0mpvCB7_kciZ7zEyDHOzTeyXI-vY5daEaE2wISFcEiUlBu64tQpV06bEViSXiE87qfQzeigWvQU-EqM14kYzgWMwltvyyafOdLj26klhyBFXV0U4KR7Gigf32JUBuujPd8PwxHTjp_toig0FnGj-s8ijEgsl4Q90f3StgxriKgwMWnYW0J-VDh7dZ_idQSqPppOM-U72ci6H05NCQ8X5ixSWqfqDMbjDKOgpI2gom_ALo9UUe4wVM_bc2HMNxLC05LFRxx3hiEz19lqx_lQ4AA6p2n1ILiqdukKo0W26LrV6ltd7DjEb1w57DZnL4xXujhF6P3wviBLNQd6iTh8ZUEz10vuTwuNC-gfuMbZ8ejNP2coz3U4rhD0iRzjt6S1TClurbdfzle7mbo-I_M_yztM89y6H_x2W-A8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c86d070d3.mp4?token=qrV6E1auclliwldtoBpEQhAQMfAibKZWmJUWxVkRfaZvOYsWf07KAUDMQzoKt2jvJa5fqlAMau_HA2rjs8614CgcSzSrMTJTKat3P-9g2KhQ2c2RK_VWahUrSb8eMEFUlaFHbXCzNQCzjPLU8unZB1x8rTnHGdMvJxdFtR5XIVIXiK0jTvDuZAo8FCMIwlfdNFqImu-z1RDWXAJ0MukgJ0Bo-exx3I5B-z12GkUv06BOUvjpg26XQeEALj5IH7kYyD_A6V7z0mpvCB7_kciZ7zEyDHOzTeyXI-vY5daEaE2wISFcEiUlBu64tQpV06bEViSXiE87qfQzeigWvQU-EqM14kYzgWMwltvyyafOdLj26klhyBFXV0U4KR7Gigf32JUBuujPd8PwxHTjp_toig0FnGj-s8ijEgsl4Q90f3StgxriKgwMWnYW0J-VDh7dZ_idQSqPppOM-U72ci6H05NCQ8X5ixSWqfqDMbjDKOgpI2gom_ALo9UUe4wVM_bc2HMNxLC05LFRxx3hiEz19lqx_lQ4AA6p2n1ILiqdukKo0W26LrV6ltd7DjEb1w57DZnL4xXujhF6P3wviBLNQd6iTh8ZUEz10vuTwuNC-gfuMbZ8ejNP2coz3U4rhD0iRzjt6S1TClurbdfzle7mbo-I_M_yztM89y6H_x2W-A8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر يدخل للمرقد المقدس للامام ابي عبدالله الحسين (ع)</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81996" target="_blank">📅 03:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81995">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الجثمان الطاهر يدخل للمرقد المقدس للامام ابي عبدالله الحسين (ع)</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81995" target="_blank">📅 03:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81994">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">لحظة دخول الجثمان الطاهر لحرم الامام الحسين (ع)</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81994" target="_blank">📅 03:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81993">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be745cc3bb.mp4?token=XM9lPoePFQnVh8R5y0EC-H-WJOortUcsZ2osuydbD1Es28lmYhIDBdpcmt9HoxE4Zp_yN2PXg9__k52LWzwofyK5zOT78UCdutsYRi8DUCKEZIPjiArWL_aR3olVBF-iv51L0b1dZrYAumu7bjvqalUDCMyiI-3x1rHaO6Wpl37_AuhEW7FmqUkUn2solrMjz-gZJieSzmsr28aiTMv2Gn2VxJsxlznH20_EH-S7VUqsVNUWR08Z01tLETUGl9fqJq3zmAkzoNfaRo5n9WQ6Mog88RtmYOJL0PCA1UGGqjiWqvI6GWEWIV07UPbx1gSTGjA-eDvkh7o-pAz5S7cCYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be745cc3bb.mp4?token=XM9lPoePFQnVh8R5y0EC-H-WJOortUcsZ2osuydbD1Es28lmYhIDBdpcmt9HoxE4Zp_yN2PXg9__k52LWzwofyK5zOT78UCdutsYRi8DUCKEZIPjiArWL_aR3olVBF-iv51L0b1dZrYAumu7bjvqalUDCMyiI-3x1rHaO6Wpl37_AuhEW7FmqUkUn2solrMjz-gZJieSzmsr28aiTMv2Gn2VxJsxlznH20_EH-S7VUqsVNUWR08Z01tLETUGl9fqJq3zmAkzoNfaRo5n9WQ6Mog88RtmYOJL0PCA1UGGqjiWqvI6GWEWIV07UPbx1gSTGjA-eDvkh7o-pAz5S7cCYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ صلاة الجنازة على جثمان قائد الثورة الشهيد في حرم الامام ابي عبدالله الحسين بامامة الشيخ عبدالمهدي الكربلائي</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81993" target="_blank">📅 03:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81992">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بدأ صلاة الجنازة على جثمان قائد الثورة الشهيد في حرم الامام ابي عبدالله الحسين بامامة الشيخ عبدالمهدي الكربلائي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81992" target="_blank">📅 03:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81991">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fac953f0.mp4?token=gmZ39vlG9-Wzgth1s5VUhKjlgP6RWpU5p-k22IWzB2WiNb3uhPW21j3n8dXZa-llN6VlaLhwrlr_bA4rzntRSlRjBZaYjKh0JJO65jPYbTcepB_35Z9343lekQYG8PprZVrgMbW1t5mcsEVnxpMn8LcKqyRFMnLIkj7iNZ2kEpv92Eg1TktUwNL31phP3Nxh1gO1vb2ZJaOKWdkhsSbDKmkf3QVz5xybt88rNNxKh7w17jE7G1A906jGKi7oIGWDYSpkc9KxPT3Drqp7tCPWk1zcFm1b0LKkD77mCKrV4ATVOtbyx7l1XavhatV2KF-5W-f2FFgtA63fSlk4iy2Z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fac953f0.mp4?token=gmZ39vlG9-Wzgth1s5VUhKjlgP6RWpU5p-k22IWzB2WiNb3uhPW21j3n8dXZa-llN6VlaLhwrlr_bA4rzntRSlRjBZaYjKh0JJO65jPYbTcepB_35Z9343lekQYG8PprZVrgMbW1t5mcsEVnxpMn8LcKqyRFMnLIkj7iNZ2kEpv92Eg1TktUwNL31phP3Nxh1gO1vb2ZJaOKWdkhsSbDKmkf3QVz5xybt88rNNxKh7w17jE7G1A906jGKi7oIGWDYSpkc9KxPT3Drqp7tCPWk1zcFm1b0LKkD77mCKrV4ATVOtbyx7l1XavhatV2KF-5W-f2FFgtA63fSlk4iy2Z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أنباء عن عدوان أمريكي على مدينة گلستان شمال إيران.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81991" target="_blank">📅 03:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81990">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیکر آقای شهید در حرم حضرت عشق اباعبدالله الحسین</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81990" target="_blank">📅 03:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81989">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b446e40bc7.mp4?token=veu0GDvJmm8p-xbteWiJGdcPbie0BGp_H_22FJC2Ey8nu7AlMFLkzSWOU841AkK2QIMeMKojQuA_itv6f_IQC2zJqipfSwG6QuCAy7rG9wd_h7hzt9QgjEjbjtn4nXeANQNF-p0ShGN-iT6zyDNGCl_pS9b94DejSvMR4L4nTqP-SX4scPGZDRMpKchRH4y5JhEU0U33GNqaKhHb2Tdm5hT2Itgd1JbWIoT2_PrOm6A5C2NsijuqVYY1EXSz7YsFRqHJ2Dln_fFw7EsIElhSAlex6pLmHoxB9JfWDUcBS_pPQEmQqa6DLdqpW6_MrAxkVIuKSjbMuMYMMgbNESraDZlhex9Fge_hofcYM2cPTkyRLsbf9rXQwZNXgxEp9ihc1RaeVMjKUW7owweu3HrSQ5ltQD20HZyKPZRK4HcPxQT_zIRktzn3MNnSZ-rSjjQoQ2qP-xj6icl0BdGvoOJUta-zXubNkr_yvjvLuqzUsEkvaGZL9NjgWHhSvrB9PKitUpCwFLFi3Bb-zs7tfrtyJS-YnxGGqgU5Gsk_A1Y3F_yskYN29_Wr7OmqPQ6sjJBmMwSKkSov5bNet8aBwA0isjkKe5U5_URUm1s7k86yRI6M8IQXfv7-IJPUDZ3HnXJOO95-KER2nufzvbRgNE1cJjEDkGl3MY0D7DALFZyxx88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b446e40bc7.mp4?token=veu0GDvJmm8p-xbteWiJGdcPbie0BGp_H_22FJC2Ey8nu7AlMFLkzSWOU841AkK2QIMeMKojQuA_itv6f_IQC2zJqipfSwG6QuCAy7rG9wd_h7hzt9QgjEjbjtn4nXeANQNF-p0ShGN-iT6zyDNGCl_pS9b94DejSvMR4L4nTqP-SX4scPGZDRMpKchRH4y5JhEU0U33GNqaKhHb2Tdm5hT2Itgd1JbWIoT2_PrOm6A5C2NsijuqVYY1EXSz7YsFRqHJ2Dln_fFw7EsIElhSAlex6pLmHoxB9JfWDUcBS_pPQEmQqa6DLdqpW6_MrAxkVIuKSjbMuMYMMgbNESraDZlhex9Fge_hofcYM2cPTkyRLsbf9rXQwZNXgxEp9ihc1RaeVMjKUW7owweu3HrSQ5ltQD20HZyKPZRK4HcPxQT_zIRktzn3MNnSZ-rSjjQoQ2qP-xj6icl0BdGvoOJUta-zXubNkr_yvjvLuqzUsEkvaGZL9NjgWHhSvrB9PKitUpCwFLFi3Bb-zs7tfrtyJS-YnxGGqgU5Gsk_A1Y3F_yskYN29_Wr7OmqPQ6sjJBmMwSKkSov5bNet8aBwA0isjkKe5U5_URUm1s7k86yRI6M8IQXfv7-IJPUDZ3HnXJOO95-KER2nufzvbRgNE1cJjEDkGl3MY0D7DALFZyxx88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ورود پیکر رهبر شهید انقلاب به حرم مطهر امام حسین علیه‌السلام</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81989" target="_blank">📅 02:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81988">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadf8ee7e4.mp4?token=XZcbPCEL48E80gYDjjsbyLBFdNf7cxbdiqVJrWl9gwdua0OwUzcYKgxRKY6y0Lfj_q5z6Kgzh6nKlNveEVlDJNS77AXaBOpEzRjEU82P68jj1MFsYWqaH9izozee2eiDtfmSTYC58gSYiVhjBOfkSFsLEFmVy55D3apxEtnxFl_Nweinccak1QNXETDkpf5fYJhVdnX9W_jE_TNIskvSNVajH0PNFFjH-abSi7d_j9ZFVn61nO961HSbi3cSbb9P1baJad84f5tdybpCVb7btUeM1NGoJkmreMkZOTEoovGWq0U30HK-d4UtSIBVYG0GW5a4ICVHoHJ-7t6Yav6MVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadf8ee7e4.mp4?token=XZcbPCEL48E80gYDjjsbyLBFdNf7cxbdiqVJrWl9gwdua0OwUzcYKgxRKY6y0Lfj_q5z6Kgzh6nKlNveEVlDJNS77AXaBOpEzRjEU82P68jj1MFsYWqaH9izozee2eiDtfmSTYC58gSYiVhjBOfkSFsLEFmVy55D3apxEtnxFl_Nweinccak1QNXETDkpf5fYJhVdnX9W_jE_TNIskvSNVajH0PNFFjH-abSi7d_j9ZFVn61nO961HSbi3cSbb9P1baJad84f5tdybpCVb7btUeM1NGoJkmreMkZOTEoovGWq0U30HK-d4UtSIBVYG0GW5a4ICVHoHJ-7t6Yav6MVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ورود پیکر رهبر شهید انقلاب به حرم مطهر امام حسین علیه‌السلام</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81988" target="_blank">📅 02:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الجثمان الطاهر لشهيد الأمة يدخل إلى حرم الإمام الحسين عليه السلام</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81987" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1990f3b593.mp4?token=gLzVY8IIv7eJkk8mFyFm5Yz7mo0O0Ge-KDCfTrP5-DJRp-sfjBIvxTPlQDHWM7-jb9D2cdBqOl8HXmxIpodO3pbB5QaQbo-d7u9kas5GKSKaHUIiRslM0XweewvhpWmp93a9cH8-ZsTa7lig2g6sjgT8UhIpV_nPhhm3PWuLBBKMznHO2wbGCsQQ0N7p_XPsdiJ8LNRKoTHxeZ6coRdkeuUoFb7Rh5e0GjdhoJebB0_0WK4bqUTp9yDhKk2bmVGpkOcDk-xMkLNLwBINRxHUuyfz8kwBkOGr7rNpb3wzZj8Ft8tqUsSB36sMsXxk5r5AJMBb992imJkcGoeYS0E5TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1990f3b593.mp4?token=gLzVY8IIv7eJkk8mFyFm5Yz7mo0O0Ge-KDCfTrP5-DJRp-sfjBIvxTPlQDHWM7-jb9D2cdBqOl8HXmxIpodO3pbB5QaQbo-d7u9kas5GKSKaHUIiRslM0XweewvhpWmp93a9cH8-ZsTa7lig2g6sjgT8UhIpV_nPhhm3PWuLBBKMznHO2wbGCsQQ0N7p_XPsdiJ8LNRKoTHxeZ6coRdkeuUoFb7Rh5e0GjdhoJebB0_0WK4bqUTp9yDhKk2bmVGpkOcDk-xMkLNLwBINRxHUuyfz8kwBkOGr7rNpb3wzZj8Ft8tqUsSB36sMsXxk5r5AJMBb992imJkcGoeYS0E5TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان انتظار چندین ساله.. پیکر مطهر رهبر انقلاب به حرم آقا اباعبدالله الحسین رسید.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81986" target="_blank">📅 02:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وصول الجثمان الطاهر إلى حرم الامام الحسين</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/81985" target="_blank">📅 02:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جثمان الإمام الشهيد بالقرب منطقة بين الحرمين الشريفين.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81984" target="_blank">📅 02:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6eed9650.mp4?token=F7lnc7Ce7J48QmP_cotsYiJgnqm8VbajmtnbWj9T1s-H0DdLF6IJg6tLIvzetsBNLXyhg7yKSRI4fIpz0jdtdHuL_vjOykjYAHhgluGGMMxT_sSHfJKHgHx_lSav9OhuRh5imDHx35Bt-B3k4Vm-_kf-WYY5xYo45602vpKFYGYPYfkXT3X9oToR2XLjJm_RGciKoY-GXvDdFggxiSLozWe8Ji7s9Ul6InEfLNK6D-7-boMuPlJI4zZNoBxyMJ0Ms03vPpik4xKWcEtOgy4n29yf0JPpVTg_pTQ4CRjdRFYOjKR4f5qOZh9MVgxgxQLv9N7kPyPINI4GWARN_h8V4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6eed9650.mp4?token=F7lnc7Ce7J48QmP_cotsYiJgnqm8VbajmtnbWj9T1s-H0DdLF6IJg6tLIvzetsBNLXyhg7yKSRI4fIpz0jdtdHuL_vjOykjYAHhgluGGMMxT_sSHfJKHgHx_lSav9OhuRh5imDHx35Bt-B3k4Vm-_kf-WYY5xYo45602vpKFYGYPYfkXT3X9oToR2XLjJm_RGciKoY-GXvDdFggxiSLozWe8Ji7s9Ul6InEfLNK6D-7-boMuPlJI4zZNoBxyMJ0Ms03vPpik4xKWcEtOgy4n29yf0JPpVTg_pTQ4CRjdRFYOjKR4f5qOZh9MVgxgxQLv9N7kPyPINI4GWARN_h8V4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر على مقربة من حرم الامام الحسين واخيه العباس عليهما السلام</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81983" target="_blank">📅 02:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0958e4251e.mp4?token=SpB_rDzkhIdtvWUBi83QG0U2D_j3IgTFXcRzt285w0tVUYyebj1g3SU-jlnPxvOOJsr7G1p0JDeAnoWnB_KKhr9IIbj1fwCoV1gibadiYwUa5PQWrRpTNSSc7OUzOHpmYBChuCg0WIUTiB4qoZ0x1k3GmOfNBxY-HQtqNUB6G4JOPOO9vc900G0qGA6MCrvjbzTa3ZDqyRto8j6VONClkhlvkcqlmbowGcDXR034hQmu3VztLFOJOedhyvigk7-T7dAueP5GSlk7FW_N1j_HDElO9dyloyUrCVgvu8n7SjAnwQVQ_QZXrct2rGFMv_6D_YsaLoDFQMmPHOffBXQTLI-upxW1yIND4S-uDDflWR2AL8yZ-Hwh09rR9Bq6fdhgUwr0CRjcPb4rVS_WL_0pmp9Tkv0wqi4Na5Va88xzeh4Bzlwp4dzxfjCeUaTxhmVEPWE87aBeWG5p74LPTPzREot1btI1z2xJiLgEhwgddAhzIPdavJUz8DSjG0MWJSXqemvrh3lXmsLKv0Ag4zDLYZ1M8iUi_xzX0N99HbQ_gJgFEXO2DSDKRuKA75vXU-1PxdDoPIh60-wJzva2kGQgkCKh3aDx-Ib4XFeBm2JwwPbqY1PBYiyYuS1-bimkuIIt0MUFr22IXNJXnVz8euL0Gz-etVRjGOdmjjwFZQtQgm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0958e4251e.mp4?token=SpB_rDzkhIdtvWUBi83QG0U2D_j3IgTFXcRzt285w0tVUYyebj1g3SU-jlnPxvOOJsr7G1p0JDeAnoWnB_KKhr9IIbj1fwCoV1gibadiYwUa5PQWrRpTNSSc7OUzOHpmYBChuCg0WIUTiB4qoZ0x1k3GmOfNBxY-HQtqNUB6G4JOPOO9vc900G0qGA6MCrvjbzTa3ZDqyRto8j6VONClkhlvkcqlmbowGcDXR034hQmu3VztLFOJOedhyvigk7-T7dAueP5GSlk7FW_N1j_HDElO9dyloyUrCVgvu8n7SjAnwQVQ_QZXrct2rGFMv_6D_YsaLoDFQMmPHOffBXQTLI-upxW1yIND4S-uDDflWR2AL8yZ-Hwh09rR9Bq6fdhgUwr0CRjcPb4rVS_WL_0pmp9Tkv0wqi4Na5Va88xzeh4Bzlwp4dzxfjCeUaTxhmVEPWE87aBeWG5p74LPTPzREot1btI1z2xJiLgEhwgddAhzIPdavJUz8DSjG0MWJSXqemvrh3lXmsLKv0Ag4zDLYZ1M8iUi_xzX0N99HbQ_gJgFEXO2DSDKRuKA75vXU-1PxdDoPIh60-wJzva2kGQgkCKh3aDx-Ib4XFeBm2JwwPbqY1PBYiyYuS1-bimkuIIt0MUFr22IXNJXnVz8euL0Gz-etVRjGOdmjjwFZQtQgm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر على مقربة من حرم الامام الحسين واخيه العباس عليهما السلام</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81982" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35b34c365.mp4?token=Hky6j9V-cpU5BZ1Q40tBaaVoIbHg7JOVjNDVORrUWbvj2-P6gR1vO61qWCBtDzoMB_a3Kz_7xrYOMMQe0ZX4adtveHijoVcQgOBqIOaW2sq8V7N-Lm4pw5C2lilOZRvPzXMt8st2epag9WHFG26zGnf7jGexRiS9HbSdQJTe21ye-HUSQq62vjzTmUfS6rDHxxovKGnl6SzNnIPy9Bs8dX-KLnRNSrOCzyAAPB_hfZMjX-sPQtSXx2DM9clbSiiXDBBPmF-FRQWdszm67ad2hbBtiLfQZoYdMb8l_NccJICk7GstA3zWx9C2pcCDMX7SKuC2kidst0pOkWnKd_ls9RKUGsjXMuQMaJ9tF1E8fQgX8csxkcZojxBpeC44jP8GIZ6q1XYApxTlho6Rj7zmtqHzPNnnXI4cIZlueTSqMFbrEiJwNiRCd74nNwhSvTfL177RxMGkm-aD_k6K1hE47vsCTwEgf45WZ4Tr0Re6oCwJdQfG4AnVw2oIEiDGJ3Gh_Ix_B8tydQ5ksiuXY2V6JUTbYFcpwdKz8OWU5GkETVyrycYzp_MjR236Wr6VAGUJGsIXOU74tSN7AE8qubAu1D7JpDjHNKaKLMCfQEgy0D0KNZOYq2npa9W3H_5PjZ3AYXofAN5pEfDEwsCvk1Sayl6tfeo8-umluLLYkYsxRIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35b34c365.mp4?token=Hky6j9V-cpU5BZ1Q40tBaaVoIbHg7JOVjNDVORrUWbvj2-P6gR1vO61qWCBtDzoMB_a3Kz_7xrYOMMQe0ZX4adtveHijoVcQgOBqIOaW2sq8V7N-Lm4pw5C2lilOZRvPzXMt8st2epag9WHFG26zGnf7jGexRiS9HbSdQJTe21ye-HUSQq62vjzTmUfS6rDHxxovKGnl6SzNnIPy9Bs8dX-KLnRNSrOCzyAAPB_hfZMjX-sPQtSXx2DM9clbSiiXDBBPmF-FRQWdszm67ad2hbBtiLfQZoYdMb8l_NccJICk7GstA3zWx9C2pcCDMX7SKuC2kidst0pOkWnKd_ls9RKUGsjXMuQMaJ9tF1E8fQgX8csxkcZojxBpeC44jP8GIZ6q1XYApxTlho6Rj7zmtqHzPNnnXI4cIZlueTSqMFbrEiJwNiRCd74nNwhSvTfL177RxMGkm-aD_k6K1hE47vsCTwEgf45WZ4Tr0Re6oCwJdQfG4AnVw2oIEiDGJ3Gh_Ix_B8tydQ5ksiuXY2V6JUTbYFcpwdKz8OWU5GkETVyrycYzp_MjR236Wr6VAGUJGsIXOU74tSN7AE8qubAu1D7JpDjHNKaKLMCfQEgy0D0KNZOYq2npa9W3H_5PjZ3AYXofAN5pEfDEwsCvk1Sayl6tfeo8-umluLLYkYsxRIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر لقائد الثورة الإسلامية يقترب من منطقة بين الحرمين الشريفين</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81981" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSzvXLi7NRCkCAzinRuEoLH_G1rJ3X8XoxhRof67IprIpZ91gfGxM9hSB42ACE9VQjzatD2debQis6pehOYY5Xcnak6QGMtlQFYv5GjODn9exEW1XnnTH6JvEf0KjYvXu9dj7x1x28MYXAl2jCuTRICl1Je0PAiR5GhWISfKBLO7G1_wlv7DKW5goK9ASgJz3R1ryvt5Q4QPPId9gukiFRy43Lyo2l5Vid5ckAnRcte_i-PLWdXHYmUypm0lMbVczAoJBBfEsQhWwIY3QO_hjED4DZG5XqA16GE-VNWvPF3zCuZNm01W7z47eLW8QADSB8X6fDcvm6QCCQYc_GIvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفع لافتة "نحن سنقتل ترامب" في مدينة مشهد المقدسة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/81980" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیکر مطهر آقای شهید به نزدیکی حرم سالار شهیدان حضرت اباعبدالله رسید.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81979" target="_blank">📅 02:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">أنباء عن عدوان أمريكي على مدينة گلستان شمال إيران.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/81978" target="_blank">📅 02:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088855cdd4.mp4?token=bzENjVole7Fd34sqjv6wA0O-Rw5jarqrGBh0lLu5MowRnZPu30W-9FnAMWBta2zDL4Nc5fbDcaPB9uZgOXLqNRZXkrb-nFRiSMyWeJpslMihCJUKpdrpzPnJKsz2mp2VAaxbauPHz5ZJ-NfbXWRXzsaLP2YSPvs7jhT8fXKV4SyyX24k0vU1RkrDC9KnpDGF8_3Q7TQEqC4NL73sl8jIQWDFl4BGo6JMIzDeNyTYpuQsisbgAHUZjMyoISmMhcG-qUQNMP_M1HIQwSWSMKcWm9mTD15CjB9mxnGmghTyCg54mNDn6xRF8zCjWivcCC-wbe2OUNGF4oq4guA1D6hvzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088855cdd4.mp4?token=bzENjVole7Fd34sqjv6wA0O-Rw5jarqrGBh0lLu5MowRnZPu30W-9FnAMWBta2zDL4Nc5fbDcaPB9uZgOXLqNRZXkrb-nFRiSMyWeJpslMihCJUKpdrpzPnJKsz2mp2VAaxbauPHz5ZJ-NfbXWRXzsaLP2YSPvs7jhT8fXKV4SyyX24k0vU1RkrDC9KnpDGF8_3Q7TQEqC4NL73sl8jIQWDFl4BGo6JMIzDeNyTYpuQsisbgAHUZjMyoISmMhcG-qUQNMP_M1HIQwSWSMKcWm9mTD15CjB9mxnGmghTyCg54mNDn6xRF8zCjWivcCC-wbe2OUNGF4oq4guA1D6hvzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على مدينة جغادك بمحافظة بوشهر الإيرانية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/81977" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">من العدوان الأمريكي على مطار مدينة إيرانشهر في محافظة سيستان وبلوشستان جنوب شرقي إيران.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/81976" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وصول نعش الشهيد القائد السيد علي الخامنئي إلى شارع باب القبلة قرب مرقد الإمام العباس (عليه السلام).</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/81975" target="_blank">📅 02:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامب: لسنا بحاجة إلى مساعدة بشأن إيران</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/81974" target="_blank">📅 02:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامب: لسنا بحاجة إلى مساعدة بشأن إيران</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/81973" target="_blank">📅 02:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a56fe3728.mp4?token=FsRf4YVLtrDV0DQZrSU9Fdx9J33OiJwSvtUVmgrRXHIBUeBVlzteN2mWT43I4NvA3Kq6O4KNIyt83hXOpKar-UOFYz1lkWjoKa4mTi4vzP7Ym-p19M_9xIj1PuArThZOXXKPal6nJQduULRJA5IyKUiVQGrdBgZcrHYxtPPmjInIcjlQVs_NIpj_EXgAOxXDc3M34_c9iY3jesQ2DcmdIiizjnrHTStCNI_7G27PcBQ81rc8IUKcNjGSRwBPihknO0D7pk3vVLR8LSJprwjXgvEI_OHUHOpHTkUdRZrlKZizZPdv1PD9FvceClAuWMxOEkT9MCRNs1WGkBRFqiQvM0nObs4nnxm9xz1m3QLc-YZ8oqOYVnWApqzqc4fpQcSC6fa8VMYYPBBCSq2P4PqFTfQcgIpZn3NqzA-o8WmpKUKR7oKwAVVJAzFQBHtudoOSNUXH0urG2Sesdsnvj0b2St4B5flMIS1dtxBEr5jggKg-gdgWvWpl5qsV1wY8PWFi6y4zufeanxnxuGbIywtxMSUqyUwUAuGqBJnjT6iQVB6MTiJ5jvp4ulOIoDCdHNSul65oL2CNufoBPP7a1y16iREZUx68X43NpxRmsEIZiM5dwbR1pDj7ZTUCgP5kJkBpqL2tx7AqR-wDH2ExIQSrMzTGbrSwgnnoC2TNCGNDMHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a56fe3728.mp4?token=FsRf4YVLtrDV0DQZrSU9Fdx9J33OiJwSvtUVmgrRXHIBUeBVlzteN2mWT43I4NvA3Kq6O4KNIyt83hXOpKar-UOFYz1lkWjoKa4mTi4vzP7Ym-p19M_9xIj1PuArThZOXXKPal6nJQduULRJA5IyKUiVQGrdBgZcrHYxtPPmjInIcjlQVs_NIpj_EXgAOxXDc3M34_c9iY3jesQ2DcmdIiizjnrHTStCNI_7G27PcBQ81rc8IUKcNjGSRwBPihknO0D7pk3vVLR8LSJprwjXgvEI_OHUHOpHTkUdRZrlKZizZPdv1PD9FvceClAuWMxOEkT9MCRNs1WGkBRFqiQvM0nObs4nnxm9xz1m3QLc-YZ8oqOYVnWApqzqc4fpQcSC6fa8VMYYPBBCSq2P4PqFTfQcgIpZn3NqzA-o8WmpKUKR7oKwAVVJAzFQBHtudoOSNUXH0urG2Sesdsnvj0b2St4B5flMIS1dtxBEr5jggKg-gdgWvWpl5qsV1wY8PWFi6y4zufeanxnxuGbIywtxMSUqyUwUAuGqBJnjT6iQVB6MTiJ5jvp4ulOIoDCdHNSul65oL2CNufoBPP7a1y16iREZUx68X43NpxRmsEIZiM5dwbR1pDj7ZTUCgP5kJkBpqL2tx7AqR-wDH2ExIQSrMzTGbrSwgnnoC2TNCGNDMHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر للشهيد السيد علي الخامنئي يقترب من الحرمين الشريفين في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/81972" target="_blank">📅 02:02 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
