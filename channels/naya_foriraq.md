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
<img src="https://cdn4.telesco.pe/file/mgwJw33Ft-kxdUStciiuPbVSoaMhWAqfTmJ6Lcrw7KO8d4VsYMV_hyr5QfpqLKW8rFR1kaXmPvQXYdKJGn19BJAR41v6E-JKYGKDb2C49jY4rGFxE93v04EYMqGWMT_tCsAkWW4p0b-QmpIkCg10nMHBIbrX24xcoOkHq4vcqFq1tonSctUb5x9YWcm46RFyFv6yNnhLdNoqgurqSPTJvgU6VIJZXHJNye95dgjypudTHNetaYAPTjBC94IARp7p2HqjaQfC-sPKyGx2nx_iLgIhMdn7sgnWTqSWo3ULh30ZyeSQAROHEMHJVG0rH5Plj6YFszCGrQDjgZxfXuvHqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-76970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFrOhG0YTB8dWduq7CnaABp1AZE_u5ORzQZbJxZCVd5w8mOlRdaRG5RhsDq0886Nqeb_T_5VoduS8inHkkgQ_Q6sgLtMvlbwQc8VV3SlEvHiM0DXCEevfkBJsWEp2aATc-Yvgcf5-p6K0YfOPBgFPbgQrk1f8nSxW1k-vZUXlkZqOjP1DG0N7MFpewvQi5jU1c7spK6lqRuEKJ7oLiz0EE5BdhzNkheS9YOaiOY50rqZmZPb-LOOdMM9M4QChNuYPCu0nibGDyxZ7JBFtOpDs5TwlKVbyN-5Svz2jei1FcdFOqFI44tBKbnkW8ocPQopQ2EoM3nk_Pt37J-w58EgoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري الإيراني:
دعم المقاومة في لبنان واجبٌ علينا جميعًا، وإخراج إسرائيل من المنطقة هدفٌ قابلٌ للتحقيق للمسلمين. جوهر مطالب المقاومة هو انسحاب النظام الغاصب إلى ما قبل بدء حرب الأربعين يومًا. سيجني المجاهدون اللبنانيون قريبًا ثمار مقاومتهم الباسلة.</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/naya_foriraq/76970" target="_blank">📅 13:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76969">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVWPkiNOID_Sbjmw5ZfSRpitQ5irRiurcMZzRXkGW9037PRzMPB5ZmCVDdZjMONF4r2RkaQuX3IdKOXRjkpu2NRan8r_DRER6m0qx-QyTJawfSGvLb2x860ix2rqTL3j-t8fE3qFl3m5hWpLnTuKRXBbx7NHW88PYORiX-pCZOHZfPUN-7-BsrKeCQw3FgAxIZmPsiYdkKNVs1yG4arZ5_FRdxwQleqBO75aGF0jF1DKFBs_biJctPbY1h_IgeXuBAqqs2EEwhlkQvNMKJUpSYAvrUEExRdjn10gcWw_cUjOX7LfduJkjQem-DiuXylb5IX5cp2G3-HItCl201mHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/naya_foriraq/76969" target="_blank">📅 13:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76968">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8d0ac34d.mp4?token=lVSmSGhTBG0DEUKIuRlpDBziLXsM1Gsf-iv3AuCReofombBpbP35JizdlmDRPnIMfejoZGKmxW1ULswkgbP20VbU4Vo6oJSma58PXEQ8LT9TxNq8PwrMTCDmFC64eJ1giSvbzZYvZ6qtmCrfzgXYvB4u89-vMpf8olA5pbnbmix0LpsR0ta0Yib_U6XLtc8NSYrCP8sMGwPH_9242TI20-5maFqTURQETZli5m1TuQbhqSL0U6krdE2LJpEEfcz9EUGoD3nU7unY2TcBCQxNQzrIZXW-tL_HPP9eGs1AhGd-w1ghzJ6MYCzHjRwKZDUk5u6-nomDoZd_JbVmxpUn6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8d0ac34d.mp4?token=lVSmSGhTBG0DEUKIuRlpDBziLXsM1Gsf-iv3AuCReofombBpbP35JizdlmDRPnIMfejoZGKmxW1ULswkgbP20VbU4Vo6oJSma58PXEQ8LT9TxNq8PwrMTCDmFC64eJ1giSvbzZYvZ6qtmCrfzgXYvB4u89-vMpf8olA5pbnbmix0LpsR0ta0Yib_U6XLtc8NSYrCP8sMGwPH_9242TI20-5maFqTURQETZli5m1TuQbhqSL0U6krdE2LJpEEfcz9EUGoD3nU7unY2TcBCQxNQzrIZXW-tL_HPP9eGs1AhGd-w1ghzJ6MYCzHjRwKZDUk5u6-nomDoZd_JbVmxpUn6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حديثة توثق لحظة العدوان الامريكي الذي استهدف جسر B1 في الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/naya_foriraq/76968" target="_blank">📅 13:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEVKpe8jSdCUpm3e2tXSami6CGi2wtf56J1GWRxQHL9juYtyLemJTq3d4D2OV7dW7t1QQfwQP8KMqwQNIvsN5rCUSgv7wYPOB3mpQ4GJnII0MGhj6uvEosvUmxcR7r87Yqzf9UHvVc6aAe2Cwtdbh3na591aOs3IzskPEHYjjSVJtruSdO0nnZgvn2wHcMYQX35JqU0BIhr3IyghOCJMPMarHDbNzD9hQcIxPGE9mzQl4AlpdS3bVUotjW0_o0-AlnmHF0KvN0T0HxcCndXITbIZju-DR7fHIBNQcBIVq0urFSyQ4FKTwgwGNVpVmJIOw8V0Jlh8KrlZHC7RHuEp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل جندي أمريكي في قاعدة الحرير اربيل</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/naya_foriraq/76967" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 31-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في بلدات القنطرة والطيبة وفي محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصلياتٍ صاروخي</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/naya_foriraq/76966" target="_blank">📅 12:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏اعلام خليجي عن مصادر: الاتفاق حول الإفراج عن الأموال الإيرانية المجمدة بمراحله النهائية</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/naya_foriraq/76965" target="_blank">📅 12:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇱🇧
اليونيفيل: وفاة جندي وجرح اثنين إثر سقوط قذائف على موقعنا قرب مرجعيون جنوبي لبنان</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/76964" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76963">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 02-06-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/76963" target="_blank">📅 11:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76962">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctLzCShIqKa6wMMvn3_w8-n1WdYvjHnVtUvj3-1Z5FfDvTGI438gHQxqVCsH4v9cyiM1jVK48m3XtFjaMo39NiL78t6TDsTISY_BhlXIJDMEHPkuVI3Sm3ft_NeQ-hajbLvWMAvqBYYBggkMiQwkuKyJwvL84hFlw9-CwPMGHLO1Y8_1LqUKMjpk0Uy_7tYuK5pF3Mvs9pRkTxmbCXu2O5higkvoXN4xilTrHvQ3N9imvvcZE2YtzLljUVr9Y5jIuH_asXiqArucKZ-bRYSp5QCrpjziKYyIv_Z0kMOWyAmdvYCDwWmp-qFhgugUgIfm4mbz5fYRPmXT2clYL7LHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
نظرة من صور الأقمار الصناعية
على الأضرار المدمرة الناجمة عن هجمات الفصائل العراقية البطلة من معسكر فكتوريا التابع للجيش الأمريكي في العراق قرب مطار بغداد الدولي ؛ وقعت الهجمات في مارسو أبريل 2026 بواسطة مختلفة الأسلحة ..</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/76962" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76961">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سرايا السلام تسلم ملفها إلى القوات الأمنية في مقر قيادة عمليات سامراء المقدسة</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/76961" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6b338b2a.mp4?token=uLAZByPlMoIXMHS9K_VlTr2X5MHwfUaZL6HevdHRdPEPuwAa03Ft5hd3fSnpiKKbtftxGEfQzijN-CXhzwJt2HWa0x7q_hF_b2zltD_ik5W-20-OSPqGuXi5uSTa5tpHtce_1Z2z3dvb8_CSqkABjvJoptYNmcYIju_iFjtodwSHLQyIBfRdcRQN2ikjRP2stm8au5Eq1b_pCKd3CLFJKo3Hglmr6vcZkyoduAns7LmfkRRM0v1v1ZY8478YyUpjxS9lHPqrlysnKHkKg4wnL1SlDUF68jL7jFsOshoWcsE1PbgT7AAPC69ONsdzxrGNzuvqhoT2rnYy5i5gbcfhnTP3AG2OlIGbZHh1_xc3288hDs5BK9EWhFWdGi6jcKYApyOB2RUlqW3-iDrXl5RxTBCcYSfuRdoNiuGbX--DQULigpWF2agEpLdLa01AljmnVxd8G0oYGjUCTQWy8aJcMaxrFwIbLxDkV1twYJ4ff9eBuNB6qokASUsItUOB8354NmU3TuxMlPPK4CG7bDxP0PxCnTo189XRqUlbkobIREMRl8irKUlys7ppmAIIpCDsFqvG4cY5qwUq21d63EKJbtbYSpFGzMfep7hCgARUUxt_wRqHCiG8oYvs9dEUtsuK2Q4_m2iftynSPGeKac5mnwWqvx0BIVUDMPLocADrZ-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6b338b2a.mp4?token=uLAZByPlMoIXMHS9K_VlTr2X5MHwfUaZL6HevdHRdPEPuwAa03Ft5hd3fSnpiKKbtftxGEfQzijN-CXhzwJt2HWa0x7q_hF_b2zltD_ik5W-20-OSPqGuXi5uSTa5tpHtce_1Z2z3dvb8_CSqkABjvJoptYNmcYIju_iFjtodwSHLQyIBfRdcRQN2ikjRP2stm8au5Eq1b_pCKd3CLFJKo3Hglmr6vcZkyoduAns7LmfkRRM0v1v1ZY8478YyUpjxS9lHPqrlysnKHkKg4wnL1SlDUF68jL7jFsOshoWcsE1PbgT7AAPC69ONsdzxrGNzuvqhoT2rnYy5i5gbcfhnTP3AG2OlIGbZHh1_xc3288hDs5BK9EWhFWdGi6jcKYApyOB2RUlqW3-iDrXl5RxTBCcYSfuRdoNiuGbX--DQULigpWF2agEpLdLa01AljmnVxd8G0oYGjUCTQWy8aJcMaxrFwIbLxDkV1twYJ4ff9eBuNB6qokASUsItUOB8354NmU3TuxMlPPK4CG7bDxP0PxCnTo189XRqUlbkobIREMRl8irKUlys7ppmAIIpCDsFqvG4cY5qwUq21d63EKJbtbYSpFGzMfep7hCgARUUxt_wRqHCiG8oYvs9dEUtsuK2Q4_m2iftynSPGeKac5mnwWqvx0BIVUDMPLocADrZ-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الضريح المقدس لمؤسس الثورة الإسلامية الإمام الخميني قدس سره خلال مراسم إحياء ذكرى رحيله.</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/76959" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76958" target="_blank">📅 10:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f58636b4.mp4?token=HsJ7s-ZEY6Uu-sbGsrzQuslIi20zsvs69luLMdLUAHU-L1E5sPfgdvYm9LqkBROIWOZlRxZrhdOFibB2ICk_IXsjJAx0uGleoeKYcaQSY0YYdjaayWI-Ht5X5D_d5Jcqn5iRJ6Xec5hAbY3KH5hc_HrES6NYXwfz2ZW2ZX1ohqpA5swdl_Cala4OS4qumMCnCzsIGK_vJhSGDMa1S-11Ac2rPIcZlzK6DWC4JGUBJHo9UDR_802Ss9JGfAGhpfkCdvt8sm19SB0JzevkkoRGrz7sGGtncUY5-0QNlukxiR_9vNhqTkSlIzxeTQ7GwhzHrPKYQUevy9bXznpzSsEvsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f58636b4.mp4?token=HsJ7s-ZEY6Uu-sbGsrzQuslIi20zsvs69luLMdLUAHU-L1E5sPfgdvYm9LqkBROIWOZlRxZrhdOFibB2ICk_IXsjJAx0uGleoeKYcaQSY0YYdjaayWI-Ht5X5D_d5Jcqn5iRJ6Xec5hAbY3KH5hc_HrES6NYXwfz2ZW2ZX1ohqpA5swdl_Cala4OS4qumMCnCzsIGK_vJhSGDMa1S-11Ac2rPIcZlzK6DWC4JGUBJHo9UDR_802Ss9JGfAGhpfkCdvt8sm19SB0JzevkkoRGrz7sGGtncUY5-0QNlukxiR_9vNhqTkSlIzxeTQ7GwhzHrPKYQUevy9bXznpzSsEvsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
انفجار مركبة على الطريق 20 بين حولون وتل أبيب مقتل صهيوني وإصابات عديدة كحصيلة أولية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76957" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: منذ إعلان وقف إطلاق النار، أطلق حزب الله 6 صواريخ باتجاه قواتنا العاملة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76956" target="_blank">📅 09:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏴‍☠️
‏وزير الدفاع الإسرائيلي: الواقع الذي فرضناه بلبنان يقود لاتفاق يحقق أمن سكان الشمال لأول مرة منذ 50 عاماً</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/76955" target="_blank">📅 09:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قناة CBS: مقتل شخص وإصابة 3 آخرين نتيجة إطلاق نار أثناء حفل تخرج مدرسي في مدينة فيرفيلد الأمريكية</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76954" target="_blank">📅 09:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hza0GGNipamKx4cG4TW1SPHDnXtpsANNKQpPaPFUqpyKEgIDGU_HJd0nZNkkLO4LOE_xlBAxcFn6JPVg6ZFa8I7M6PFrM_YXjN7srtMa4_G30eUc4YqYIMI_ptosLVVYUPjtWr5WTFN6BR6Z3CswlUaHO5AIl_gZGzMBV8EhfgFcQgXfJGxrFMrDa-oZDM5jS2xu5J8p2dhGqKKzpK5xFelbBAEb3DRbhCpCf5lg9myrDoCIa2moPLaZ0L9BWYN8RFYRV8zfgjvScZc5WHD3dzOofUyrdZcJNuHTGRWZMJF4aLBOBCvZu2-Do8yurdkbuDtJrsSX9wa-azD2NHqlPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
الديمقراطيون يعودون إلى حيلهم! إنهم يحاولون سرقة انتخابات حاكم ولاية كاليفورنيا التمهيدية، وانتخابات عمدة لوس أنجلوس التمهيدية، من مرشحين جمهوريين عظيمين.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76953" target="_blank">📅 09:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5wutwa-8wJFd8_8bUXF6BiaccMlljvjDoYPNIlhr3tz9CiZX04lKViZh1biZ9nevpu-uPlXipNI20M6KET3ab4VOeHfjn0kLTiOMJnag2tZdvqyWn_AD51V6sHgblqytitiBjFWKZgk3QKCbmZdyEo7etZ1Q4hAAlN5Qmik7YBbYZtmYDLSBvYY8yJk-jJrx0QzG29ehbawPGCloYVvqCaU3QESHe55VY2uGRO761l873ledkhSwBprt8jmNHnJG8SKPVHtfv-SuZU4vw300kxU0tBvW35JPTCzzCnB09-tGQU4UnRFeYAkPxmXDKYICsRbAF20r0xncWR-MJtSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76952" target="_blank">📅 09:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKAzet_dsWkOQ1iEcSvQfsXXzCtnHx4geswmfqh8wagLXI1XDZ_sS-_Q0-UupEysFM3S92hX15oXmmGKONVlDFqhJN2_uCv2wW2betJpm4Lc0V7uil_YREV-lCjHCisE6n59m-9g_OgcG731Kapnpflg6_MpFYfRG1nQDq-KYDUBfktGkMRE6FTgN38RKi_sDjNYnElTlGNX6R24X1bBXaOOObGzJwOwrEkMxwK4mCPhgMMlUbqKhfS9e7h6tqfYEhgPYum1sfYDqCMSCfc0YUXVumOELH6VV4uqqJ7zH4Tq7Cj7iDsY0J5I9eX7_oc2Ec7coDNp45aTRz2VTAKlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
رئيس المكتب السياسي لمنظمة بدر يقدّم قراءة مهمة للواقع العراقي:
على الولايات المتحدة أن تفهم أن نزع السلاح يجب أن يقابله نزع المخاطر.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76951" target="_blank">📅 03:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76950">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
🌟
🌟
البيان المشترك بين الولايات المتحدة ولبنان والكبان الصهيوني
:
عقدت الولايات المتحدة الاجتماع الثلاثي رفيع المستوى الرابع بين ممثلين إسرائيليين ولبنانيين يومي 2 و3 يونيو/حزيران 2026.
ونتيجةً للمفاوضات التي قادتها الولايات المتحدة، اتفقت إسرائيل ولبنان على تنفيذ وقف إطلاق النار. ويشترط وقف إطلاق النار وقفًا تامًا لإطلاق النار من قبل حزب الله وإجلاء جميع عناصر الحزب من قطاع الليطاني الجنوبي.
واتفق الجانبان، بتوجيه من الولايات المتحدة، على الإسراع في إنشاء مناطق تجريبية تسيطر فيها القوات المسلحة اللبنانية سيطرةً كاملةً على المنطقة، مانعةً بذلك دخول أي جهات فاعلة غير حكومية.
ستُمكّن هذه الخطوات من إحراز تقدم نحو اتفاق شامل للسلام والأمن.
وأكدت جميع الدول مجددًا أن مستقبل العلاقة بين إسرائيل ولبنان يجب أن يُقرر من قبل الحكومتين السياديتين. ورفضت أي محاولة، من أي دولة أو جهة فاعلة غير حكومية، لاحتجاز مستقبل لبنان رهينةً.  أكدت إسرائيل ولبنان مجددًا عدم وجود أي نية عدائية بينهما، والتزمتا بمواصلة المفاوضات المباشرة لبناء الثقة، وحل جميع القضايا العالقة، والعمل على التوصل إلى اتفاق شامل بين البلدين.
ناقش الوفدان إطارًا أمنيًا، استنادًا إلى المناقشات التي جرت في البنتاغون في 29 مايو/أيار، يهدف إلى ضمان سيادة لبنان وإسرائيل وأمنهما وسلامة أراضيهما بشكل مستدام. ويشمل ذلك تفكيك الجماعات المسلحة غير الحكومية، ومنع عودتها للظهور.
أدانت جميع الأطراف هجمات إيران على دول المنطقة، والأنشطة المستمرة التي تقوض الاستقرار في جميع أنحاء الشرق الأوسط، سواء من خلال دعم الوكلاء أو أي أعمال عدوانية أخرى.
جددت الولايات المتحدة دعمها المستمر للحكومتين لممارسة سيادتهما. وأكدت مجددًا أن أي اتفاق لوقف الأعمال العدائية يجب أن يتم التوصل إليه مباشرة بين الحكومتين، بوساطة أمريكية، وليس عبر أي مسار منفصل. وشددت الولايات المتحدة على عزمها دعم القوات المسلحة اللبنانية، بهدف تحسين قدراتها وتمكينها من ممارسة السيادة بشكل فعال في جميع أنحاء الأراضي اللبنانية.  أكدت إسرائيل على تصريح وزير الخارجية روبيو الصادر في 2 يونيو/حزيران، والذي أكد فيه أن حزب الله ليس عدوًا لإسرائيل وأمريكا فحسب، بل هو عدو للبنان أيضًا.
وأكدت إسرائيل مجددًا أن أمنها واحترام وحدة أراضيها لا يمكن تحقيقهما إلا من خلال نزع سلاح حزب الله وتفكيك بنيته التحتية في جميع أنحاء لبنان. وشددت على أهمية المفاوضات المباشرة بقيادة الولايات المتحدة لحل جميع القضايا العالقة وتحقيق سلام وأمن دائمين.
وأكد لبنان مجددًا على ضرورة الاحترام المتبادل للحدود المعترف بها دوليًا، والحاجة المُلحة إلى التنفيذ الكامل لوقف إطلاق النار، مع التأكيد على مبادئ وحدة الأراضي وسيادة الدولة الكاملة. والتزم لبنان، بدعم من الولايات المتحدة، بتعزيز قدرات القوات المسلحة اللبنانية لفرض سيطرة فعالة على جميع أنحاء البلاد.
واتفق الطرفان على استئناف المسارين السياسي والأمني ​​خلال الأسبوع الذي يبدأ في 22 يونيو/حزيران، بهدف التوصل إلى اتفاق شامل. ووافقت الولايات المتحدة على مواصلة تسهيل التواصل بين الطرفين خلال هذه الفترة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76950" target="_blank">📅 02:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76949">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c8f003d5.mp4?token=rDf2rZmF3zI2OCxR3ll_xtGHEpMGOqoc_lv__ePd18E7pyywt8PP6lqPrJoPeSo2712YW1Y7GVbTkghmSU4xR3RDGDtcQMzMMdA3h8ZzcH1YA4VuWTgXs5IJ6zjnivpVcPjTyojRdkKo1pzmF_-Y8npxxTfUngpkDCFkn0Pf89LbRrAxJ3vGtC7iB57jM62Qx3pJKMAYiutr1ZBgEWiRx_JQHxKj88_LT3ksvTxUUu2eusbY5oJcaGmIhlcKkQyQa_h-QbbdfdnhI_HN4RZ1RC2-a3s-hLRCxGMvayqtp9_wYLSBwBhSwb5aqIREI7t6MBu9nWX4JWJKJ_4fjrgueQ1emqfO-tkndj7vE1NAdxsVx58hxOWaBDEx_PB0UmvhZs2-jbpzNJuA7m9T6q7EWcaBa1kl693Xi8Kj8WAIV39vIOQRQHZrmpNo7vDW-qsPBKXGqKoJ4jpKeloYhIRzBwIrmHBgZmeO-n97vQj8bDNJyUoayOPD3pFW4mA40mS7v0NolfIKqA77Q9i9FGK4mxe5wl91dS-7Ufm3CdibHBuOKsoPQDxuSMcgbppaeRNN12O7H3WbHeJXO37rZX8xrlATYDFGn4SkVbrJmDEjRAtAom5dpjw-PvW5Ukd1D7jP1mumKRPOuRkVq8PXmv1hX7NZY03W8cx1NGdIBve53UI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c8f003d5.mp4?token=rDf2rZmF3zI2OCxR3ll_xtGHEpMGOqoc_lv__ePd18E7pyywt8PP6lqPrJoPeSo2712YW1Y7GVbTkghmSU4xR3RDGDtcQMzMMdA3h8ZzcH1YA4VuWTgXs5IJ6zjnivpVcPjTyojRdkKo1pzmF_-Y8npxxTfUngpkDCFkn0Pf89LbRrAxJ3vGtC7iB57jM62Qx3pJKMAYiutr1ZBgEWiRx_JQHxKj88_LT3ksvTxUUu2eusbY5oJcaGmIhlcKkQyQa_h-QbbdfdnhI_HN4RZ1RC2-a3s-hLRCxGMvayqtp9_wYLSBwBhSwb5aqIREI7t6MBu9nWX4JWJKJ_4fjrgueQ1emqfO-tkndj7vE1NAdxsVx58hxOWaBDEx_PB0UmvhZs2-jbpzNJuA7m9T6q7EWcaBa1kl693Xi8Kj8WAIV39vIOQRQHZrmpNo7vDW-qsPBKXGqKoJ4jpKeloYhIRzBwIrmHBgZmeO-n97vQj8bDNJyUoayOPD3pFW4mA40mS7v0NolfIKqA77Q9i9FGK4mxe5wl91dS-7Ufm3CdibHBuOKsoPQDxuSMcgbppaeRNN12O7H3WbHeJXO37rZX8xrlATYDFGn4SkVbrJmDEjRAtAom5dpjw-PvW5Ukd1D7jP1mumKRPOuRkVq8PXmv1hX7NZY03W8cx1NGdIBve53UI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الكويت تبث مشاهد للحظة القصف المركب الذي استهدف مطار الكويت واسفر عن اضرار جسيمة</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76949" target="_blank">📅 01:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76948">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دولة الاخ المناضل كيم جونغ اون في كوريا الشمالية تعقد اجتماعًا هامًا لتعزيز ترسانتها النووية .</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76948" target="_blank">📅 00:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وكالة رويترز: الولايات المتحدة ستخفض قدراتها التي تساهم بها في القوات الدائمة لحلف الناتو، والتي تشمل الطائرات المقاتلة، وناقلات الوقود، والأصول البحرية، والطائرات المسيّرة. دول الناتو تلقت تحذيرات بأن التخفيضات قادمة لا محالة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76947" target="_blank">📅 00:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏ ترامب: إذا نجح الاتفاق مع إيران، فربما يستطيع الناس البدء في بناء الشقق والمباني المكتبية في إيران.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76946" target="_blank">📅 00:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1w2d57tE5IzwWp_CJkR5mFdgvcSDJr8to6rgMNbye2cnzL0jRqfOtZo7FJAl_NNgCPLaapwjvtaw4C6ezJ5HfAYyFd2aFsAkMIt5EMM9iDefEvP97WpK-V3NXHb9iYhOcwHlWTxzAKUFoPp_b0EJuqa_pE7GOdBGPEA6qzWlqZL8sthWfhh7mAOUqcdbPxJgVT53DVul2I_627wFM7Qf0U9WeVYbmbiK01h_fYDog8F0bxL9ZX5jg4m9yD-_U0zniaeh-2eSfEHSWrzssx1zFiz1uKOxcYrtAC5cIzeIvyF2mhoK38-cbSiI9B8fgZcMa1u53QWY6GyWCBsEeIXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
إعفاء المتحدث الرسمي باسم وزارة النفط العراقية صاحب بزون بعد تصريحات
مثيرة للجدل طفّي التبريد بالصيف”، التي أثارت موجة واسعة من الاستياء الشعبي والانتقادات الإعلامية، بعد تحميل المواطنين مسؤولية الازمة</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76945" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامب: فتح مضيق هرمز سيكون سريعاً عند توقيع مذكرة تفاهم.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76944" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامب: الحصار له تأثير أكبر من القصف.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76943" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76942">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامب: نسعى للفصل بين قضايا إيران ولبنان وفتح مضيق هرمز والاشتباكات في لبنان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76942" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامب: أريد الحصول على اليورانيوم المخصب من إيران. سنستعيد اليورانيوم المخصب من إيران في المستقبل القريب.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76941" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76940">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏ترامب يهاجم مراسلة السي ان ان كايتلان كولينز: مراسلة فاسدة تقف هنا، لا تبتسم أبدًا. شابة جميلة، لا تبتسم أبدًا. لم أرَ ابتسامة على وجهها قط. أراها واقفة وعيناها تفيضان بالكراهية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76940" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏ترامب: وقف إطلاق النار في لبنان مختلف عن وقف إطلاق النار في أماكن أخرى من العالم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76939" target="_blank">📅 23:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76938">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامب: إيران قريبة من توقيع الاتفاق نظريًا.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76938" target="_blank">📅 23:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامب حول إيران: يمكننا الاستمرار لمدة أسبوعين إلى ثلاثة أسابيع إضافية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76937" target="_blank">📅 23:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76936">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامب: يفضل عدم القضاء على إيران.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76936" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامب يتخلى عن الكويت</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76935" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامب: الهجمات بين إيران والكويت كانت رد فعل متبادل.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76934" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامب: المفاوضات مع إيران تسير بشكل جيد، مفاوضات قد تُعقد في عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76933" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامب: المفاوضات مع إيران تسير بشكل جيد، مفاوضات قد تُعقد في عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76932" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hha3exk2NkGoiBK0cgaLOJ3cgXv6H6rPtAyCE2FFxlqMFm8L7-eAv2UK5hzcjX_ueTYU6eqVPvdvsOgFE8Skpj_m49VrN2CwpIzFPgCIenwGWRnfIvd0HlENIdi1RWHQOSaZQn0_SwYqVdYJu9P2yWP6LwKGPXonVvEHun7QJ6MCJ8uV0S8EvF0VQH-W_M6tsQzZZcBv-N_VhDKTpoune1uQ9FzpJKNhXoZ9wGPWhMr-fkB_VAzGpqRUKiyWdkNK4eIQjb8O2A_w4pJEvoEguJ_U65NTKO_DEBQMh0B2mnVxBWxCtpmv7y849STHfr6e_tRo2AUTvZO3oBxbCQiL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏توم باراك يشيد بالفصائل التي نزعت سلاحها:  نتقدم بأحر التهاني إلى رئيس الوزراء العراقي  على هذه الخطوة الهامة، التي تُمثل حجر الأساس لحكم ذاتي عراقي مُتجدد، قائم على استعادة السيادة، والاستقرار الدائم، ووعد النهضة الوطنية. كما نُشيد بالجماعات التي سيُسهم…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76931" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76930">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb7cd4d19.mp4?token=gA69FVewgL46abjCLxmZkbRH4A1Ee-HAvJbxB02KP5PghuAVoByP-RbHGD1mVxMxj2oLDkG6MNqhxF1QF-7kelXhibNfCiDlGYR7IxhgH93Qc4D4e6EKVyS9mvxavr5o3tiEsx1zEmHtR2uhDxyYfzkHmtIht54rgzcH-zCIQyJyqddRVOJBZdGiiFtBNWezTGwEkdDwcjfPsRDg9D_6g19MHIQvmtqtPcEu4DdozwEVSDbHGmifbvcEylI3RBxS3WXrCFosdWL7nlDJOTzSKyGbsTvUYcyjOg9TmxLXNvvGHndJ3M5-juGtJSD9X_fbiPVAAcC7Ow9rCLVfLDXAgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb7cd4d19.mp4?token=gA69FVewgL46abjCLxmZkbRH4A1Ee-HAvJbxB02KP5PghuAVoByP-RbHGD1mVxMxj2oLDkG6MNqhxF1QF-7kelXhibNfCiDlGYR7IxhgH93Qc4D4e6EKVyS9mvxavr5o3tiEsx1zEmHtR2uhDxyYfzkHmtIht54rgzcH-zCIQyJyqddRVOJBZdGiiFtBNWezTGwEkdDwcjfPsRDg9D_6g19MHIQvmtqtPcEu4DdozwEVSDbHGmifbvcEylI3RBxS3WXrCFosdWL7nlDJOTzSKyGbsTvUYcyjOg9TmxLXNvvGHndJ3M5-juGtJSD9X_fbiPVAAcC7Ow9rCLVfLDXAgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني: استهدفنا قبل ساعات "مركز القيادة والتحكم" المتمركز على متن مدمرة أميركية في بحر عمان</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76930" target="_blank">📅 22:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76929">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استهداف سفينة عسكرية أمريكية بالقرب من المياه الإقليمية الإيرانية في خليج عمان.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76929" target="_blank">📅 22:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76928" target="_blank">📅 22:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">استهداف سفينة عسكرية أمريكية بالقرب من المياه الإقليمية الإيرانية في خليج عمان.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76927" target="_blank">📅 22:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
🔳
المتحدث باسم الحرس الثوري الإيراني:  أظهر تحقيقنا وبحثنا في حادثة استهداف مبنى الركاب بمطار الكويت أن القوات الجوية التابعة للحرس الثوري الإيراني لم تطلق النار على هذا الهدف، وأن تدمير مبنى الركاب كان نتيجة خطأ في أنظمة باتريوت الأمريكية، التي سقطت على…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76926" target="_blank">📅 22:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">💲
📈
العقود الآجلة لخام برنت ترتفع 1.81 دولار لتبلغ نحو 98 دولارا للبرميل</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76925" target="_blank">📅 22:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76924">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
عراقجي:  نحن والأميركيون ندرس النصوص التي تم تبادلها ونعمل على صياغة نهائية.  العودة إلى المفاوضات ستكون مستندة إلى تأمين حقوق الشعب الإيراني ونهاية الحرب على إيران ولبنان وفي المنطقة.  أنقل لكم حقائق أن الأميركيين لمسوا قدرة إيران في هذه الحرب خلال الـ40…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76924" target="_blank">📅 22:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
احتفالات كبيرة في العاصمة اليمنية صنعاء بذكرى عيد الغدير الاغر.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76923" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
إيران الإسلامية لاتتخلى عن حلفائها.. عراقجي: نحن نعتبر لبنان بلداً شقيقاً وصديقاً لنا ولم نسعَ أبداً إلى التدخل في الشؤون الداخلية اللبنانية.  كانت لدينا وجهات نظر وملاحظات بيّناها وحزب الله جزء مهم من البنية السياسية في لبنان.  لبنان جزء لا يتجزأ من الحرب…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76922" target="_blank">📅 21:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76921">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
إيران الإسلامية لاتتخلى عن حلفائها..
عراقجي:
نحن نعتبر لبنان بلداً شقيقاً وصديقاً لنا ولم نسعَ أبداً إلى التدخل في الشؤون الداخلية اللبنانية.
كانت لدينا وجهات نظر وملاحظات بيّناها وحزب الله جزء مهم من البنية السياسية في لبنان.
لبنان جزء لا يتجزأ من الحرب بين إيران وأميركا والكيان الصهيوني ويتعرض للعدوان.
نحن نعتبر أن مصير حرب إيران مع أميركا و"إسرائيل" ليس منفصلاً عن مصير الحرب في لبنان.
هناك ترابط كبير منذ اليوم الأول بين لبنان والحرب على إيران حيث طُرح ذلك في المفاوضات وموضوع نهاية الحرب.
مواقفنا واضحة جداً بأن نهاية الحرب ووقف إطلاق النار يجب أن يكون في إيران وجبهات المقاومة كافة ومن بينها لبنان.
عند وقف إطلاق النار طلبت من رئيس وزراء باكستان إدراج عبارة "لبنان خاصة" عند القول إن الحرب تتوقف في الجبهات كافة.
ما تم في النهاية هو إدراج لبنان في وقف إطلاق النار.
نحن اليوم في المفاوضات التي نجريها للوصول إلى مذكرة تفاهم مع الولايات المتحدة البند الأول فيها هو نهاية الحرب.
في الجملة الأولى من مذكرة التفاهم قلنا إن وقف الحرب يكون في محور المقاومة كافة وأولاً في لبنان.
لبنان دفع أثماناً في هذه الحرب التي فُرضت علينا من قبل أميركا و"إسرائيل".
أصدقاؤنا وأحباؤنا في لبنان تعرضوا لاستهداف من قبل "إسرائيل" وبكل تأكيد مصيرنا واحد حتى نهاية هذه الحرب.
المصير واحد ومرتبط بين إيران ولبنان في الحرب ونهايتها.
إما أن تتوقف الحرب في إيران ولبنان أو لا تتوقف لا في إيران ولا في لبنان.
من أوقف الحرب خلال اليومين الأخيرين هو قدرة المقاومة اللبنانية بالدرجة الأولى وقدرة القوات المسلحة في إيران.
عندما وصل الأمر إلى قوات الكيان الصهيوني بأن تهاجم الضاحية الجنوبية لبيروت اتخذنا موقفاً قاطعاً والقوات المسلحة استعدت للرد.
منذ أيام تنتهك "إسرائيل" وقف إطلاق النار بين إيران وأميركا وفي لبنان لكن هذا الانتهاك قوبل برد من حزب الله.
إن انتهاك وقف إطلاق النار في بيروت هو عدوان وقد أعلنا للأطراف كافة أنه إذا هاجموا بيروت فإننا لن نتحمل ذلك.
قلت لكل قائمة اتصالاتي بوضوح إن نتيجة العدوان على بيروت ستكون عودة الحرب ومن واجبنا التصدي للعدوان.
أتقدم بالشكر لجميع بلدان المنطقة الذين ساهموا بهذا واهتموا وأجروا اتصالات مع أميركا ومارسوا ضغطاً عليها.
في النهاية أميركا منعت الهجوم الإسرائيلي على بيروت بعد الموقف الإيراني والضغط عليها.
في أي لحظة قواتنا المسلحة مستعدة لإستئناف الحرب وضرب "إسرائيل".
قواتنا المسلحة مستعدة لضرب "إسرائيل" إذا اعتدت على بيروت.
المفاوضات تتأثر بالعوامل الخارجية وهذا أمر طبيعي.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76921" target="_blank">📅 21:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76920">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
🔳
المتحدث باسم الحرس الثوري الإيراني:
أظهر تحقيقنا وبحثنا في حادثة استهداف مبنى الركاب بمطار الكويت أن القوات الجوية التابعة للحرس الثوري الإيراني لم تطلق النار على هذا الهدف، وأن تدمير مبنى الركاب كان نتيجة خطأ في أنظمة باتريوت الأمريكية، التي سقطت على هذا المبنى بعد فشلها في اعتراض صواريخ إيرانية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76920" target="_blank">📅 21:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76919">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427e365e60.mp4?token=S6BBAMeCC0juTfHq7RoaqWIHWrCdCvtvIxiiHKdyUl4btbDt5Fn4EhV2DiCzarJGoc8ixDEljzRf0mbWulKUWavVDlrlMp52ba865pworVS-j5tmlUx8hDkoxbC6KddhnSRD4y5qJsU4qMxmJ94tUaaJIm0idxqbLB-F5OPDdS6a9RvfIRm6KZSrTiX1W7OHXN9k0PHnYluzzV8F7_NnJraiWZ3onJ5af4fO0fG6VdXvGBbpHOw7XlhDndC4NpZAHLqVxaDFiy-8n_r_Wykgg-JthM55E09JFmAkSjicgKxrnrpz_EMljccIxc2rUGDURZkOHq9oW0UUHmzDDipEnzef3OghyEJsCDz8xywzDOqr_VcpyJZuH1Y1SkXAJZ916sxKGGShi2I7wjpBO1EObrogneILP6BxirsWdL25wqztZqyjiZm04FI0dKAb3wkOcbVGCAO_RhED5KWtHd9Ne52olQIrhzUqR5mljtSQjU0d-qCnYLI1YBdy_VTKSCv65_wVhWGTw-3fbWErWY9XcEMwj_AleQSHzTGWWrnBoNNLnRj6yXU1s9KwzyvoWhDddJB9YtYm6SbomqHf0Yq2UMgTW2MK4WnbEkn2bM-KxQDXQSaKNIXSDHDL2jeg5tm9rDbhefK4ueD0Lzaa9xmBavI0OJLXRDZBDD9ZZDLIJdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427e365e60.mp4?token=S6BBAMeCC0juTfHq7RoaqWIHWrCdCvtvIxiiHKdyUl4btbDt5Fn4EhV2DiCzarJGoc8ixDEljzRf0mbWulKUWavVDlrlMp52ba865pworVS-j5tmlUx8hDkoxbC6KddhnSRD4y5qJsU4qMxmJ94tUaaJIm0idxqbLB-F5OPDdS6a9RvfIRm6KZSrTiX1W7OHXN9k0PHnYluzzV8F7_NnJraiWZ3onJ5af4fO0fG6VdXvGBbpHOw7XlhDndC4NpZAHLqVxaDFiy-8n_r_Wykgg-JthM55E09JFmAkSjicgKxrnrpz_EMljccIxc2rUGDURZkOHq9oW0UUHmzDDipEnzef3OghyEJsCDz8xywzDOqr_VcpyJZuH1Y1SkXAJZ916sxKGGShi2I7wjpBO1EObrogneILP6BxirsWdL25wqztZqyjiZm04FI0dKAb3wkOcbVGCAO_RhED5KWtHd9Ne52olQIrhzUqR5mljtSQjU0d-qCnYLI1YBdy_VTKSCv65_wVhWGTw-3fbWErWY9XcEMwj_AleQSHzTGWWrnBoNNLnRj6yXU1s9KwzyvoWhDddJB9YtYm6SbomqHf0Yq2UMgTW2MK4WnbEkn2bM-KxQDXQSaKNIXSDHDL2jeg5tm9rDbhefK4ueD0Lzaa9xmBavI0OJLXRDZBDD9ZZDLIJdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
30-05-2026
مستوطنة كريات شمونة شماليّ فلسطين المحتلة بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76919" target="_blank">📅 21:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
‏ترامب: علاقتي بنتنياهو ممتازة وهناك توافق بيننا في قضية لبنان.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76918" target="_blank">📅 21:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRpzpq6J9U1flut63vJTizYohP8VV6QHIXG4aoZcymjwe3DeOJm4lvvv9NJ110qAv8vdRfMVryVqqrDFucbnnzMrltB9-fvIFEV5hk0iOxaVAzhY3AsumyUcjap0YqFekC9V3zPg8J0i-3IGPUt7TwGwDf40ptFULPyWAayOaCf1DSQtfPum8dqOzD2umP-YxTmuOPwt4FpT3dakAAb5wwxDdJJr4AhkwEVRPKWtVZUI6LNE8ORv2UfagQXYNF_zRBddELiXidUaEOTtwUFsNddcoDvuehNh_uymT6TVfUnovpMMYq0qvfckRvRSOETFYqBK8IKZCKhnmf7xsGtK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما حدث البارحة هو سياسة وسلوك ايران الجديد ! لا مزيد من الصبر الاستراتيجي والتغاضي والمراعاة .. إذا فقعت لايران عين ستفقع ايران عينين للعدو .. والعدو هنا هو امريكا واسرائيل ومن يأويهم !!!
من أراد ان يفهم فهم ومن لم يفهم بعد سيفهم رغماً عنه ولكن بتكلفة اعلى .</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76917" target="_blank">📅 21:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مصدر لنايا   اغلب الفصائل التي رفضت فكرة النزع بناء على تغريدة ابو مجاهد العساف و الكعبي و الجعفري هي الفصائل الوحيدة التي استخدمت السلاح منذ حادثة يوم المطار حتى الان وبصورة فعالية ميدانية ذات تاثير واضح " عدا فصيل الغراوي " الذي لم يظهر له موقف واضح حتى…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76916" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
‏
مسؤولين إسرائيليين:
التقديرات بأن إسرائيل ستهاجم بيروت خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76915" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
‏
ترامب:
علاقتي بنتنياهو ممتازة وهناك توافق بيننا في قضية لبنان.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76914" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله حول ادعاءات العدو الإسرائيلي الكاذبة بشأن مستشفى تبنين الحكومي:
يواصل العدو الإسرائيلي إطلاق الأكاذيب والافتراءات، مصوبًا سهام التحريض والتضليل نحو الشعب اللبناني تحت غطاء الحرص عليه وعلى أمنه ومستقبله، وآخرها المزاعم التي أطلقها بشأن مستشفى تبنين الحكومي، في محاولة مكشوفة لتوفير غطاء سياسي وإعلامي لاعتداءاته المتكررة على المستشفيات والطواقم الطبية والهيئات الصحية والمسعفين، والتي تشكل انتهاكًا فاضحًا للقوانين والأعراف الدولية والإنسانية وترقى إلى مستوى جرائم الحرب.
إن هذه الادعاءات المختلقة تُعدّ تهديدًا علنيًا للمستشفيات اللبنانية والمؤسسات الطبية، لا سيما بعد الاعتداء الأخير الذي طال محيط مستشفى جبل عامل، وأدى إلى إخراجه عن الخدمة وتعريض حياة العديد من المرضى والطواقم الطبية للخطر، بما يؤكد النوايا الحقيقية للعدو في توسيع دائرة استهدافه للبنى التحتية المدنية والصحية والحيوية، وتدمير كل ما ينبض بالحياة، وضرب مقومات الصمود، بهدف بث الخوف والضغط على أهلنا الصامدين وثنيهم عن التمسك بأرضهم.
إننا ندعو المجتمع الدولي والأمم المتحدة والمنظمات الدولية والإنسانية والصحية إلى التحرك العاجل وتحمل مسؤولياتها إزاء هذه التهديدات الإسرائيلية الخطيرة للقطاع الصحي في لبنان، وعدم السماح للعدو بتكرار جرائمه بحق المستشفيات والطواقم الطبية على غرار ما ارتكبه في قطاع غزة.
إن هذه الأكاذيب لن تغير من حقيقة أن العدو الإسرائيلي هو المعتدي على لبنان وشعبه، ولن يُفلح العدو في زرع الشقاق وبث الفتنة بين اللبنانيين. وإن المقاومة مستمرة بواجب الدفاع عن أرضها وشعبها، وتُلحق بالعدو الخسائر الفادحة، وتُجرّعه مرارة خياراته العدوانية الخاطئة، وثمن تدنيسه لأرض الجنوب وتدميره للمنازل والبيوت.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76913" target="_blank">📅 20:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بسم الله الرحمن الرحيم  اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.  ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76912" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
علّم الإمام الخميني (رضوان الله عليه) الشعب الإيراني ألا يتراجع أمام البلطجة والهيمنة، واليوم، مستلهمًا من هذا النهج، أظهر الشعب الإيراني في معركته مع أمريكا والكيان الصهيوني أن عهد تهديد إيران دون تكلفة قد ولّى، وأن أي عدوان سيُقابل بردٍّ حاسم وقاسٍ ومتناسب.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76911" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بسم الله الرحمن الرحيم  اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.  ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76910" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا وآلية عسكرية تابعة لجيش الإحتلال الإسرائيلي بمسيرة انقضاضية في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76909" target="_blank">📅 19:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTex9_NlVXtDosRhUdOw5pIRHp41clxDz2LkiEEO111oisGKIEojlyWgxv9ihuNXGYxg65lL5asXOckjLh8W_oxjSRPkQq99jIeqYc-G7AMReqf5i6kt3nkhAbc6o2ykFsffgdG6Qn_3eRx9EvSBEypQKWtLsq302JycdYf6MoXmSHVXUTGT4FY3gAJbe2rBCoGj_-8WK11k-Q5w8faRgOI8Real3BRP8Q_bf2J9U_pUkUtZVP1gPl5LpvygGiGdfsajpOJZXfFJuQohPRjyEdMX0mEIGlwZPiLqpv-IsR2vQU7_sHVBIWD5Qd6Qi2YOFHj4cNu9P7jbNrdmz4a7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.
ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ واستقلالَ قرارِه، ومن أبرزِها:
1ـ إنهاءُ التبعيةِ الماليةِ والاقتصاديةِ التي تقيّدُ إرادةَ العراق.
2ـ وقفُ جميعِ أشكالِ التدخلِ الخارجيِّ في القرارِ السياسيِّ العراقي.
3ـ إنهاءُ أيِّ وجودٍ عسكريٍّ أجنبيٍّ على الأراضي العراقيةِ ومعالجةُ جميعِ التهديداتِ التي تمسُّ السيادةَ الوطنية.
4ـ تمكينُ العراقِ من امتلاكِ منظوماتِ دفاعٍ جويٍّ وراداراتٍ حديثةٍ لحمايةِ أجوائِه وسيادتِه.
5ـ تعزيزُ استقلالِ القرارِ الاقتصاديِّ وفتحُ المجالِ أمامَ شراكاتٍ متوازنةٍ تحفظُ المصالحَ الوطنية.
وعليه، فإنّنا في المقاومةِ الإسلاميةِ – سرايا أولياءِ الدم – نؤكدُ أنّنا سنكونُ من أوائلِ المستجيبينَ لأيِّ مشروعٍ وطنيٍّ حقيقيٍّ لحصرِ السلاحِ بيدِ الدولةِ متى ما اقترنَ ذلك بضماناتٍ فعليةٍ تحقّقُ السيادةَ الكاملةَ وتحفظُ استقلالَ العراق.
كما نؤكّدُ تمسّكَنا بالدفاعِ عن العراقِ وشعبِهِ وقرارِه الوطنيِّ، ورفضَنا لأيِّ وصايةٍ أو هيمنةٍ تمسُّ أمنَه أو سيادتَه أو مصالحَه العليا.
العراقُ أولًا
واللهُ وليُّ التوفيقِ
أبو مهدي الجعفري</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76908" target="_blank">📅 19:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1af8c7a50.mp4?token=Vn_OwYgIA0GOJGIhk5bouejvis52b-dfCtCaUg77xjHExSV-xrL8IwlVCqYOIC3aCknlPSnxpctGN8GIdOM1eCsGqlWEWGLsBkhxmt9vlb-p0WLP03goJ8eq_tzcLvIVdLPpv4ccT9gc3kCmBK7OfcekjsP9O9tcefjITnnCpexfklEf6D5OIuG9vJzanzJaQ8EYr6K8KaSycYEBuUuB6C01Vp8c0nia85LyqNcwKi1NPdPLQcJ1dh5YzR4vbs55ionJx2jYqZbpus3DNIgxnUBrGKb6DIW3TdwBstyqcN6FChoaHPVfGboGtzLUtLxMuIPRon0HYeE3gzQ6UFLKtWC-AOJZJvWuUH9gnjnA5L6i_iIq9WQbf-IxAZGQW_9riXty2OFy1VbqjLBuIihEu-Z48Rff5nLwNt7RRNZDpS9t749xxWcu3i6-QwmQPQ2_Xa-0kkVgMzlD5FahfvGD2VQp1_OHbEFDAEo8cPjoYEaY2hDaXgxkv2TKwKW4QBitwBNh7gl7AOOmmon9o63h967k7ZpVNKSjvAgLE5v4p6GibJl0x2favREiLdALDrvDewhDISZ2Mm83vzdOwKheW4_5fr27yCRBdnt3RMUKU9z2jfhNW8wVHvxR3VYm8y-VY7zXXpoBT04-2jyhC1Y5KseRYqTKWLirMf1JiFAgVvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1af8c7a50.mp4?token=Vn_OwYgIA0GOJGIhk5bouejvis52b-dfCtCaUg77xjHExSV-xrL8IwlVCqYOIC3aCknlPSnxpctGN8GIdOM1eCsGqlWEWGLsBkhxmt9vlb-p0WLP03goJ8eq_tzcLvIVdLPpv4ccT9gc3kCmBK7OfcekjsP9O9tcefjITnnCpexfklEf6D5OIuG9vJzanzJaQ8EYr6K8KaSycYEBuUuB6C01Vp8c0nia85LyqNcwKi1NPdPLQcJ1dh5YzR4vbs55ionJx2jYqZbpus3DNIgxnUBrGKb6DIW3TdwBstyqcN6FChoaHPVfGboGtzLUtLxMuIPRon0HYeE3gzQ6UFLKtWC-AOJZJvWuUH9gnjnA5L6i_iIq9WQbf-IxAZGQW_9riXty2OFy1VbqjLBuIihEu-Z48Rff5nLwNt7RRNZDpS9t749xxWcu3i6-QwmQPQ2_Xa-0kkVgMzlD5FahfvGD2VQp1_OHbEFDAEo8cPjoYEaY2hDaXgxkv2TKwKW4QBitwBNh7gl7AOOmmon9o63h967k7ZpVNKSjvAgLE5v4p6GibJl0x2favREiLdALDrvDewhDISZ2Mm83vzdOwKheW4_5fr27yCRBdnt3RMUKU9z2jfhNW8wVHvxR3VYm8y-VY7zXXpoBT04-2jyhC1Y5KseRYqTKWLirMf1JiFAgVvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76907" target="_blank">📅 19:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏴‍☠️
رئيس أركان جيش الإحتلال الإسرائيلي:
سلاح البحرية سيؤدي دورا حاسما في أي مواجهة عسكرية جديدة مع إيران.
قوات البحرية تنشط في ساحات قريبة وبعيدة وتشرف على عمليات لن نكشف عنها حاليا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76906" target="_blank">📅 19:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jebAbO51v5ydNMWzBIKWUnIEyavwDOfKpLStEOVmhCttrzRQci1be_IrfK8CBYPwlMCxa00y3RsSAXcju0Ls1lrlcCvrQ3hqmNwHATtmDLl0M7M_mD18uh8NoAUd6wmQXhWMgyoRpCfKiz4cNoI590GTNsxcI8lvTrZFz4N9UhsnVf4ZqQ8hE5xddD9-Ktm-a_TXp1qWG6slbanOWrGDaQbyhJg3bFTFGhsKnYfJ7_Dt5u4CBUZnDq333ZWMfLGEL7ExyruWG-1V4Os3SZtom66jK-FxZbtCO4t0EsP-3eQkSC3g5ITRtB6P4ml4Pt-lx_CRe7MDFWyV0XU22HbZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ماركو روبيو: بعض حلفائنا في المنطقة كانوا متعاونين بشكل عدواني للغاية، مثل الإمارات العربية المتحدة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76905" target="_blank">📅 19:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa386b3d31.mp4?token=R0AZDWKpRG_k8V3w17SwbvDtyVcK4HjxwJ6yXJdRDsdNj2nxlSGxkaNa32_-aJJIy7uXeyj5t1x-EKrByKOv__zdKfFcmc6geBykKEYjQxlAy-vYbIrcFPS2FO53es0F2ipyCYN3JFuVUNdRG6HnedzYjOCaL3WDZsiRYS9Iyn7n4xCi-qNlXQvnq4KzrlrtzhdmiMTrSIfd2Z-rti3K0J0LJHrHWATrjUjheJpO5E7uYtKXGraYPgqVaI6YixRbdT5-MwYs_RXapjwEJKVybiD2uv0A6Vd66J2MYo6e92lJxpeazfc3H4CasMaKq5cN98bwTT-8Q3Z7csqm5SojrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa386b3d31.mp4?token=R0AZDWKpRG_k8V3w17SwbvDtyVcK4HjxwJ6yXJdRDsdNj2nxlSGxkaNa32_-aJJIy7uXeyj5t1x-EKrByKOv__zdKfFcmc6geBykKEYjQxlAy-vYbIrcFPS2FO53es0F2ipyCYN3JFuVUNdRG6HnedzYjOCaL3WDZsiRYS9Iyn7n4xCi-qNlXQvnq4KzrlrtzhdmiMTrSIfd2Z-rti3K0J0LJHrHWATrjUjheJpO5E7uYtKXGraYPgqVaI6YixRbdT5-MwYs_RXapjwEJKVybiD2uv0A6Vd66J2MYo6e92lJxpeazfc3H4CasMaKq5cN98bwTT-8Q3Z7csqm5SojrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔳
رئيس مجلس الوزراء الكويتي يطلع على حجم الدمار في مطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.  "امبه سنتكوم ليش چذي"</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76904" target="_blank">📅 18:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
‏وزير الخارجية الأمريكي روبيو: إيران ترد على عبور مضيق هرمز بهجمات إقليمية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76903" target="_blank">📅 18:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
روبيو: منصات إطلاق الصواريخ الإيرانية تعرضت لضرر بالغ أدى إلى تدهور قدراتها بشكل كبير.  واضح واضح
😄</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76902" target="_blank">📅 18:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a404b9b4.mp4?token=SRVpRUz4feGZko6sJtTeMqp9jBZM8ARPvV5QlOgvJSS8KmsNbfYdJ6lPoNBnprSaQv22_ClwchRvz4iMV7D8Z8uB72qYFAgbzaCJa5w_8qAe2jlr1YF9TzbvV_58Gt9cWftzF85rALKKQz3l7vq2VlHd1Ut-Ce7__FQZbDF39EB2YWpergHlYRc19LABiw9LKtAbhEIFhaVkExyF5W2-gecx5UBv9GI48Qzlyyqpz0LgE5LEg_VSxf8nNmVSyqQkPbShPLoufWITxkw9UuM_J6MBKUac6uFEzzKFE0n1Lpou0y6GbUQFlyQKk86R3QRC0NGj1EuxAE9yRjiq9llqcj7UMmXAgpeBNzA_wlmFZihZIDvTRSmH0wn5zLwMYGiQLfafH3DMsJA7VJIOb-3yRiWLJy1b1QJK6amV3G5ld6TnbNocqF8RrY6PpKGdoeYaTSVrh_uy4IORrnkNMqVfUgJqbOTI48Oupt3rvrfLbbjcmO8y0-2e4MTPNtW7KQeeJBYt6lPfpNzRarCf4eBakyTozg64ZapSXzxTt8mTV4zdLHVeRTtl4M5FGCSE4HOwTWtX7nAILoTCxbgsLcmM4upz23Q4gijukNhN2ZwJo7Wr4Q4OYEmP30o6N5oBiDO4CFPv6DdprVHGPwFI4mz9cZnxsIYW8IttGgkxwUK7Qm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a404b9b4.mp4?token=SRVpRUz4feGZko6sJtTeMqp9jBZM8ARPvV5QlOgvJSS8KmsNbfYdJ6lPoNBnprSaQv22_ClwchRvz4iMV7D8Z8uB72qYFAgbzaCJa5w_8qAe2jlr1YF9TzbvV_58Gt9cWftzF85rALKKQz3l7vq2VlHd1Ut-Ce7__FQZbDF39EB2YWpergHlYRc19LABiw9LKtAbhEIFhaVkExyF5W2-gecx5UBv9GI48Qzlyyqpz0LgE5LEg_VSxf8nNmVSyqQkPbShPLoufWITxkw9UuM_J6MBKUac6uFEzzKFE0n1Lpou0y6GbUQFlyQKk86R3QRC0NGj1EuxAE9yRjiq9llqcj7UMmXAgpeBNzA_wlmFZihZIDvTRSmH0wn5zLwMYGiQLfafH3DMsJA7VJIOb-3yRiWLJy1b1QJK6amV3G5ld6TnbNocqF8RrY6PpKGdoeYaTSVrh_uy4IORrnkNMqVfUgJqbOTI48Oupt3rvrfLbbjcmO8y0-2e4MTPNtW7KQeeJBYt6lPfpNzRarCf4eBakyTozg64ZapSXzxTt8mTV4zdLHVeRTtl4M5FGCSE4HOwTWtX7nAILoTCxbgsLcmM4upz23Q4gijukNhN2ZwJo7Wr4Q4OYEmP30o6N5oBiDO4CFPv6DdprVHGPwFI4mz9cZnxsIYW8IttGgkxwUK7Qm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
تجمّع لجنود جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76901" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNtjDZcIpwFKDKljYjZEPjg0GqUIBReGZTaxK9fkDGCKXR-rppHzsl5DU7u8OJb78DhKZ7HVKF2TaN9S7lXgn8oYP6G_U3SvUobXVvGcV7xkL8xcX-boz_tQt9IxQjMLRcN9VVURbHhM2QaaA7gDbME492kU7bBKiY7kXKp2qpBi3Mei0eQSD7So1J6U4tlnypP4ynsTmNkNGg6q0oKHplu1FPvfpVysCitb493hFwEVcne1d8tmP7IQ5aHIiF_KKUcwZLV3jRf8CQnKEuGsw_oDv9xaElM1z-CCGyHNYbq53mMHi0Zxz81JW6x7xDZA09-0drkA5WpnSBKIZJ6CgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
جيش الإحتلال الصهيوني يزعم إحباط محاولة إدخال أسلحة وذخيرة من الأردن الى الأراضي الفلسطينية المحتلة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76900" target="_blank">📅 18:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
الدفاع الكويتية : تعاملنا مع ١٣ بالستي و ١٧ مسيرة قادمة من ايران .</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76899" target="_blank">📅 18:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ie2fgusKmpN3fDebIFgEQkQB7czjtAn-0Lj5GQUiNqqitNpVr4Qi8WjACModvCqymMljlKlQUqrpzs2Q_-Nkr6L3q_k5ta5qCa3Ghb6IA9bi1utOeRZ51V1rp5hr7ERK3zdTgMp_-c1A4fxAtVSzUZkLyA7Pmz3H7_XpDCTQl95HAcIpmyjeiO2KWzAqSiALCz5sTXY2zV4Wek3kjebMhiTy6IQN5UaIa4M1OFhD4mfy5W0HRdDfPd1cnGnpsdTKVdVRJQ6K6uPEuyORsevPpYSvQtWFFWmAXwqBfbZENdycxugdAis1eqPy6jJ_IzI9Wq9_kDhuFblx_Vp19m9uZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cn-i9C1JwTgGuvcqZENWlJnrEPp0GSZlSjMoYPPghlqb8tzq9miy2Cw8zHDgkaGPeKlfWU--dRxAbi6A2FCvSXzqXAZETNLR9nGNmkOev8GCqDwKZRtQ-ZfPXuAyY6TzlyNgZTAvff1pEkf6dE5ac-XSyN0ccWqhsg9yjJFMUu1Wgix7wwIX6bbhbjuzB9arVcvkKuxq1b4O8Vu9ebl40Hh-Odk8YsIpHThJtRh6DKeVpxH3PUZGcralasdo6-tfCpdm9t_-wyOk6jwZes5X4dbxoegGbNrEdyE6hyFcLp-0zRvDsayD8PWTmYJgORln-a3gKWAW2k7iLTejDWBhBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🔳
رئيس مجلس الوزراء الكويتي يطلع على حجم الدمار في مطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.
"امبه سنتكوم ليش چذي"</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76897" target="_blank">📅 17:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21001cb12f.mp4?token=ccOb9gW5aoMTNgQad34if2x0k8270mOpDhuMmce1jMj8kc36EtDRVAr1q14CXzmJ0a2TBejE9A2fnyawGD0qnjCdv_xTkdfpU1EIhQqJgLFS-_kadjK5LnGklFrNw-NdPLo_dVrMg2zW04rNj222wZ55E-V8zdFAM33mHUyxZLoced91y8dVnb8R9_yJ5xTP1eXIwLz6rC3HFmZpM5vkLf_S1r5t0m0QP2jchsJ8ByV-cM6Jjbo2W93t_dLYyte5ewKnp3OGWLr1GzF2buKus5WAhxeWATc4gNvqT5Faon-HayUWONSRqn_9xfeRzeYipgVxaY1VV7Efr4Yb5HoSXw-pL2Y1lJ8E3Gni5JEyxDZvXN1kFwN1G4_AaJPlK7ZVMhYxK5ybxTFBkmCXWsivP06J2nuZSW-ZxZcqgm9D92Fsol3qxIscTCJSGW3bP_lpuS_rzE4Oi9ZqM5YVWNxMKWcXkrCk1zNdjDZ2lxhTXrC9aNhFbFV8qyi2g1yjDNxb16nyFKv0oo3l_rTYoqALp5-maBP9xbu2gWWh6IKXpg32UiDIe1ZTMcoPr-QBQLogE3Tr901ne5bt36ze0412uqIV0gt9neFAm35imng7u7Effuy_-S9mNQyR4_KNbyR6AYY7CGy22ryQe-SHxqil2oNJOV8oRptH0DgLgFDreVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21001cb12f.mp4?token=ccOb9gW5aoMTNgQad34if2x0k8270mOpDhuMmce1jMj8kc36EtDRVAr1q14CXzmJ0a2TBejE9A2fnyawGD0qnjCdv_xTkdfpU1EIhQqJgLFS-_kadjK5LnGklFrNw-NdPLo_dVrMg2zW04rNj222wZ55E-V8zdFAM33mHUyxZLoced91y8dVnb8R9_yJ5xTP1eXIwLz6rC3HFmZpM5vkLf_S1r5t0m0QP2jchsJ8ByV-cM6Jjbo2W93t_dLYyte5ewKnp3OGWLr1GzF2buKus5WAhxeWATc4gNvqT5Faon-HayUWONSRqn_9xfeRzeYipgVxaY1VV7Efr4Yb5HoSXw-pL2Y1lJ8E3Gni5JEyxDZvXN1kFwN1G4_AaJPlK7ZVMhYxK5ybxTFBkmCXWsivP06J2nuZSW-ZxZcqgm9D92Fsol3qxIscTCJSGW3bP_lpuS_rzE4Oi9ZqM5YVWNxMKWcXkrCk1zNdjDZ2lxhTXrC9aNhFbFV8qyi2g1yjDNxb16nyFKv0oo3l_rTYoqALp5-maBP9xbu2gWWh6IKXpg32UiDIe1ZTMcoPr-QBQLogE3Tr901ne5bt36ze0412uqIV0gt9neFAm35imng7u7Effuy_-S9mNQyR4_KNbyR6AYY7CGy22ryQe-SHxqil2oNJOV8oRptH0DgLgFDreVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب لصحيفة نيويورك بوست: قلت لنتنياهو إنه "مجنون بحق".ويؤكد الشتائم في حديثه مع نتنياهو: لم أكن غاضبًا، لم أكن راضيًا، قلت لبيبي إنه يجب أن يوقف ما يحدث في لبنان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76896" target="_blank">📅 17:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
أنا وترامب نتفق على أنه لا ينبغي لإيران أن تحصل على سلاح نووي.
‏إيران لم توافق بعد على إخراج المواد النووية لكن توجد ضغوط متزايدة.
‏نترك الأمر لترمب بشأن التصعيد العسكري.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76895" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePqvOp-o8dD-PWQL7t3piDK5w_qsSMcdCC_R2YHdSXcTwtymje0QkiW644vtHEXBjJj3fwilX_JQnBZsBGU2miwpAN_ZFcrunFwGuYybdTPdGKGlhZ2lLuqjtbCUgBGkul40OV1_avKI6VcEyhL4IAgOlnaq_IxfWyDgYuoCOtbz6PpiCQWAxRrNRUuo5xsA2_Xl-SBhSFgYxSD1okkOzrOu1_DGR1dlCHH3hwyvLWPlbcKKzJjfUNyChrNbNHUietTrAv6HiI7DrkjC6YHLZYdp4iHoo2i0m2zZ4Wkt4pvE3LUB9Ktd2zycnse6Jljx4-_uTMyEdQjWdfikKl_VTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إندلاع حريق وإرتفاع اعمدة الدخان من المنطقة الصناعية في نتانيا شمال تل أبيب المحتلة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76894" target="_blank">📅 17:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7jNd7nutbAakxdrJwkKeIruaW-E8E30-ZgoYCkbFpurBKjGgBUVcpsoxZ91hDpoFMus0JV7f-R7ifVYty3idECFPg8E2JQG8wglssJkW4yu9Kg2QWxyIKmEDnf8eytbNXHQMimJbJxc4F4ECbVqrlWSGHVhCzb0oW0D2RUDt6HD-jd2Me1nSmcCZLW3O4Lk4VPnJ_mRXBs3ppulxWaUjqUGndGEUpBo7FnP9Vr-xmyD9TvXx_Y_0IJKjiw1-FSRNuXD9SLLDOHz5F0bjD79PmTgsouQmxIWQjctWuuZ7X03cyb3hygERy05mrZ-Hfl_z7kmG_iRt6B6Qs9XperMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
غارة صهيونية تستهدف بلدة زبقين بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76893" target="_blank">📅 17:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 تجمّع لجنود جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76892" target="_blank">📅 17:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔳
وزارة الخارجية الكويتية:
استدعت الكويت القائم بالأعمال الإيراني، وأعلنت دبلوماسيين اثنين غير مرغوب فيهما بسبب "الاعتداءات المستمرة".</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76891" target="_blank">📅 16:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
الجيش البريطاني: ‏
مقتل 3 أشخاص في تحطم مروحية تابعة للبحرية البريطانية جنوب غربي إنجلترا.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76890" target="_blank">📅 16:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRkV2Ka0iy-aunp9gHq7W_14nBy8SO3pO-h_ja5ER4u-yYDmDjFbVRQJEewn5Lstg0tZ3yZOttMzcoPrr1eON_l6N73H34FmZxa-e7N9aKJyxlijPYY8pnWkga8CElWmjSj4FbaHL_XYkdQTboeHix0CDzvB2J1m8FKT2nD5z_Ya6XaqQJavpemMCrSpVuYhC-lln4ErucZvIcP2J-ROAsWZl_hn5qWuJem7k63vPx3m6cKkYsg8lnj1X1nMNcVBY2EKHH8we9EVr3gV6TH3zzK6TPe--jET-5e-1suqqmL6iOUCPQ-fvj78fsNh9uYg6ihPHx7EUhkKUMkDBAwwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الاعلام الكوردي يتداول ترشيح اللاعب الدولي هوار ملا محمد مستشار رياضي لرئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76889" target="_blank">📅 16:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
الانفجار الذي سُمع دويه في جزيرة قشم الإيرانية ناتج عن تفجير ذخائر حربية غير منفجرة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76888" target="_blank">📅 16:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
حزب الله:
تحليق استطلاعي ليلي بالتصوير الحراري لمحلّقة أبابيل الانقضاضيّة فوق قلعة الشقيف التاريخيّة ومحيطها جنوبيّ لبنان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76887" target="_blank">📅 16:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz3TMNWYPsDDERx1AoVTbIL8bSuaOZEiuZILarWBGPAECk0kC49KZRFHlUuR2CQbFIqCudtYObPK5jOoTQ2PjLJa_XGsY9yCDg0RzOQhQWTC0042go_iDBM48YuViLbHdBjrd3uWZXQzJDAcaO0JfUeRFUWLU0MhtX-CTh2gDUhkULLNgNhkvuqiQLcMrpPdkdbW3CB96JxHDDT3yUawdbC8Pkv3Wj4SVPrgHMuaXm5d_1s6yrx8ExIJKosKeKXvcSkY3w6PRLxzvf2ZqYF2EoeTo4BSzMk-iolYG6rjl934cs3uzAJUDrDxE4lVxA26Hsr1B0p3uLjHFQOIsYe_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
المقاومة الاسلامية
حركة النجباء:
نؤكد أن موقف المقاومة الإسلامية حركة النجباء ثابت ولم ولن يتغير بخصوص السلاح المقدس المنضبط الذي وجد للدفاع عن عراق المقدسات وشعبه.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76886" target="_blank">📅 15:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
رئاسة الوزراء العراقية تقرر تشكيل لجنة مشتركة تتولى وضع الآليات المناسبة لتنفيذ إجراءات فكّ الارتباط بالحشد الشعبي وحصر السلاح بيد الدولة خلال اليومين المقبلين.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76885" target="_blank">📅 15:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تنويه…
🌟
سيصدر بعد قليل بيان المقاومة الاسلامية العراقية حركة النجباء
.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76884" target="_blank">📅 15:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
الدفاع الكويتية
: تعاملنا مع ١٣ بالستي و ١٧ مسيرة قادمة من ايران .</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76883" target="_blank">📅 15:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad5f20ed9.mp4?token=RaFHHTRbAk01Gc_RHLJS3KF-z0OV9WDCgwQYeESe-6_9aBaFmfq2Eryb6jDzKP9BzrPXhibBAJ0kGq4bM06yBMW6pvaTgPFalfr-qZ0825OFlyNCT4eIN_fTl-PwVjA2mzQCYqAnuHYA7Fp8nIH6XD7ZPbZGe8O39G6_n1hLmTPkN1vtAZnCjEYvsCnLH2BgLlTKU-gbFajPaiwhzNgZ_RUAtMP-MBF465wRkjWbA-whbcTnzBu_rNOKm2VMdKLNbbR-vOuCnJnLbLIF4xZsQfTCVYDmm1reAhMqFcl36n0A7nu5wymdrWViYp6K9ooOx3DWCy8chgUBUpqIB444nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad5f20ed9.mp4?token=RaFHHTRbAk01Gc_RHLJS3KF-z0OV9WDCgwQYeESe-6_9aBaFmfq2Eryb6jDzKP9BzrPXhibBAJ0kGq4bM06yBMW6pvaTgPFalfr-qZ0825OFlyNCT4eIN_fTl-PwVjA2mzQCYqAnuHYA7Fp8nIH6XD7ZPbZGe8O39G6_n1hLmTPkN1vtAZnCjEYvsCnLH2BgLlTKU-gbFajPaiwhzNgZ_RUAtMP-MBF465wRkjWbA-whbcTnzBu_rNOKm2VMdKLNbbR-vOuCnJnLbLIF4xZsQfTCVYDmm1reAhMqFcl36n0A7nu5wymdrWViYp6K9ooOx3DWCy8chgUBUpqIB444nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سُمِع دوي انفجار عنيف في قضاء جومان بمحافظة أربيل شمالي العراق، أعقبه تصاعد أعمدة الدخان من موقع الانفجار.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76881" target="_blank">📅 15:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
🇮🇷
المجلس الأعلى الإسلامي العراقي يطالب بتشييع جثمان الإمام الخامنئي (قده) في العراق .</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76880" target="_blank">📅 15:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3070c474.mp4?token=kUZN4fMm1bMb7e5I6I78s1DvCw0kSqdYrM6z5CPo4UB5q9yYkBjsqZyyTQJ5NPbi7mdRl-7kIHKAyXp1r39-kpZ64ru3Hftpgy81WXACDzAN1061pmQtA7zi8_IBxayNMkQ73EFnir_qkjyb6C1AaI1zniuq8ql6ljwQxGgbKQA139cUXd_2do0kw8CcqXdcq4CrL8pKPcPIaqfT_PGiMK5o3mZmaq3l0meBHagEyuAxjDTcskvvzIaiWt8ai3KxPtFxMZuLG5tIyqqFW-dmb2hAAq7mCCag69yo4wZaL2ikh-lA-le0T-mMAk7qp2FyOqfxsfjIMSGTR9Nkhgy-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3070c474.mp4?token=kUZN4fMm1bMb7e5I6I78s1DvCw0kSqdYrM6z5CPo4UB5q9yYkBjsqZyyTQJ5NPbi7mdRl-7kIHKAyXp1r39-kpZ64ru3Hftpgy81WXACDzAN1061pmQtA7zi8_IBxayNMkQ73EFnir_qkjyb6C1AaI1zniuq8ql6ljwQxGgbKQA139cUXd_2do0kw8CcqXdcq4CrL8pKPcPIaqfT_PGiMK5o3mZmaq3l0meBHagEyuAxjDTcskvvzIaiWt8ai3KxPtFxMZuLG5tIyqqFW-dmb2hAAq7mCCag69yo4wZaL2ikh-lA-le0T-mMAk7qp2FyOqfxsfjIMSGTR9Nkhgy-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
شرطة أربيل في شمال العراق تعتقل شخصاً بعد قيامه بنفخ بوق يُصدر صوتاً مشابهاً لصوت المسيّرات الإيرانية.
كاكا هاي صوت مسيرة من باب شرجي
😆</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76879" target="_blank">📅 14:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDSKs7tlhM-KjVnGsOIjD_rpkeSEbsv39d5ELj0fYVpKb6i1yGE5DCqDdlY3CbhWgG1SzEteBqJxMqD1qsp_mjEh8izhDl9HlArbdoDCLlqu7igw7TGkGFIL253G7dfN8IvetI8G2shpohUsArNHNOmdWNitffoT6jb_ZNgnSWBjtqj7yHz98ZjNEMohqFitni2fYCSwUHVfF54dtAaDeTTiy9iaDLrqjgEvdkwZLHZ4LSEQrhpHeJ9iFvGDw3CQvg5aN8J60xPas9r-j9IFMd90xlSiyFTIX-FCcGFEH8bKUBp1011Z5V3ny2UrFt38phDfSptz8jRxiY3a-8U7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
الجيش البريطاني يعلن عن مقتل أحد أفراده  في شمال العراق خلال حادث تدريبي (حسب وصفهم).</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76878" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
الصحة الكويتية:
إجراء 7 عمليات جراحية كبرى عاجلة بعد الهجوم الإيراني، واستقبلنا 63 مصابا.
لا لا
يابة سنتكوم تعترضهن كلهن
😫</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76877" target="_blank">📅 14:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
الانفجار الذي سُمع دويه في جزيرة قشم الإيرانية ناتج عن تفجير ذخائر حربية غير منفجرة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76875" target="_blank">📅 14:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1c8f3530.mp4?token=Cm7OJP4ZaXdp-rxrOxP3XciQEvd8AO6Qaf7yuxhsK8NDSIF2uX3yuA6rzEecyH16GrLDuTKsT7svdt09YYgAK9tKeWa6owROD5ERHxYfj0PgKXvQ8BJglcaZ42rbY1SAzQNzhIHmhht3mIdyI6BK6BW3N7D38lk7u6w2oyRXZ_426thGoiidleO8aNf0Yr7DzuLM3Gwk9ZJ3L3nYuPgw-RUgtRwRMkFxYXkZotvD67QnWx-yCy_uoyZYFC0Q4osM53rGSVCxJvpVJ8TwBhDqCPTjD2Th3AklhpJ6ONIbLJbOBzfC_hU_AqknRinDgxxek6LefOXHqFq4SSrXb8_WWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1c8f3530.mp4?token=Cm7OJP4ZaXdp-rxrOxP3XciQEvd8AO6Qaf7yuxhsK8NDSIF2uX3yuA6rzEecyH16GrLDuTKsT7svdt09YYgAK9tKeWa6owROD5ERHxYfj0PgKXvQ8BJglcaZ42rbY1SAzQNzhIHmhht3mIdyI6BK6BW3N7D38lk7u6w2oyRXZ_426thGoiidleO8aNf0Yr7DzuLM3Gwk9ZJ3L3nYuPgw-RUgtRwRMkFxYXkZotvD67QnWx-yCy_uoyZYFC0Q4osM53rGSVCxJvpVJ8TwBhDqCPTjD2Th3AklhpJ6ONIbLJbOBzfC_hU_AqknRinDgxxek6LefOXHqFq4SSrXb8_WWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
ترامب لنتنياهو في مكالمته الهاتفية:أنت مجنون تمامًا. كنت ستكون في السجن لولاي. أنا أنقذك من الكارثة. الجميع يكرهك الآن. الجميع يكره إسرائيل بسبب هذا.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76874" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2702a18eac.mp4?token=ByrdxCyz37mGnSYxD9Vsau2pqI9PyF8ahrWDZXr9WQVRuW85VneqLWWlsgseT0lWu_obhPsJBQeFs5V9a9oL3gpzpTc73ZXSRLeoddIev3q0-v5XORJCWb7wBHIx8RWxBxSiqDFmNTLaLi03kpvp8NdfeNMPeLHUWagWPcHKlSGhZJEm_UL_KQ0F-B3yMjMyUp7Sk9Ca59cZD39B7kZIBji_8z1McZkeHlBUc8TzBd3RrfevHChS5VpnOGXNggN8ImWs6oq_5mj5TWEeHXa4I7SXfm-jkeqcmiaz87QaqpAnStZoDk2ROJQg3rPazeRqs75fbTTpxE55N0yseopHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2702a18eac.mp4?token=ByrdxCyz37mGnSYxD9Vsau2pqI9PyF8ahrWDZXr9WQVRuW85VneqLWWlsgseT0lWu_obhPsJBQeFs5V9a9oL3gpzpTc73ZXSRLeoddIev3q0-v5XORJCWb7wBHIx8RWxBxSiqDFmNTLaLi03kpvp8NdfeNMPeLHUWagWPcHKlSGhZJEm_UL_KQ0F-B3yMjMyUp7Sk9Ca59cZD39B7kZIBji_8z1McZkeHlBUc8TzBd3RrfevHChS5VpnOGXNggN8ImWs6oq_5mj5TWEeHXa4I7SXfm-jkeqcmiaz87QaqpAnStZoDk2ROJQg3rPazeRqs75fbTTpxE55N0yseopHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترمب
: مجتبى خامنئي منخرط بالمفاوضات معنا وقد ألتقيه في وقت ما، وإيران وافقت على عدم امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/76873" target="_blank">📅 13:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avURv0AoW1PRtidz5wCkZpXva0SdeiTMF2H4SrY8p4-XBwiydcKEiUmaLJLphgC4b8Pw0hY5Z2AmlN9QPqUF3hZlY6P10Yo1cVIaSewwp0lDohlM65Kci7W-hb1H6fKyP11Tz-ESi9ncr2YKLCGJccEaypy7vWFfVy-TMwdt-5edcbXhaKWzSewWsLgpTDGmaDsMHPDMCwqLNab2bsdj3AeEVpqHl7kh0nwXJ0umc1apuwvVsn869STx5Ssf3MuHSIaEFUqKGhuCNkBOocz3U7ojabk9XMEd3ZorBukTozh5bCqRM_aydz08TebFHmoAK0okmuGPlZ1FQ0ZDjcScUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
نفى المكتب الإعلامي للحاج هادي العامري بشكل قاطع الأنباء المتداولة بشأن تشكيل لجنة برئاسته لمتابعة ملف نزع السلاح.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76872" target="_blank">📅 13:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61caaee40f.mp4?token=X2hduciXaCTZ30v95ud3c_EBDFYIB8dLdu6kcivKzDQWnKP2zPVootezChgfjywkxs5xBEy1J76vSMZxpaygUlK-dqdh8Gf7fVG7kNh8Tcllmc_v5b0qT2REpsz3uOPBcMlySFb0QBT88Iv3wkl6vDtJEiEbC0gcKUQJCBGq_X8SSKa0kr1p8OMu2ziA0KrJizEUQ4F8oIpoLdRXoZVBQ8ySuHl1dX1Nk1tPEE9PpUXrzrCzhl1ueI-hDNfhhrCzZ3QX8WZP4FpGlRPelka0nbrEtCJyXOWdWVW_a8AdClcYePHW8rgKftRg_wr4t_8qHeulr1rZv1KDuQKUQrjSBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61caaee40f.mp4?token=X2hduciXaCTZ30v95ud3c_EBDFYIB8dLdu6kcivKzDQWnKP2zPVootezChgfjywkxs5xBEy1J76vSMZxpaygUlK-dqdh8Gf7fVG7kNh8Tcllmc_v5b0qT2REpsz3uOPBcMlySFb0QBT88Iv3wkl6vDtJEiEbC0gcKUQJCBGq_X8SSKa0kr1p8OMu2ziA0KrJizEUQ4F8oIpoLdRXoZVBQ8ySuHl1dX1Nk1tPEE9PpUXrzrCzhl1ueI-hDNfhhrCzZ3QX8WZP4FpGlRPelka0nbrEtCJyXOWdWVW_a8AdClcYePHW8rgKftRg_wr4t_8qHeulr1rZv1KDuQKUQrjSBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حالة من الهلع بين المستوطنين في كريات شمونة، عقب انقضاض مسيّرة تابعة لحزب الله على مواقع عسكرية قريبة من المنطقة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76871" target="_blank">📅 13:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951231e9f2.mp4?token=I_x5QmGQ2fLMSjKDm_pTH6Va0X_pXV3hVlvNks-ZMuQAJoYfxqXJlbpOYBoueESjaPvImvKcSL-4awWl9ktEMBAvoml83Cpm0Lios1iUVxtJrcmf6xQiLwltH94uTrM3SeFY_4P0_hUT3j0De7yisoHYAXrJbQdOLTMIdlJGog9QrH0JYAUldznYixiHXLwg94uClggM_NAAp3Bk7W0qHv4VHjdcnJi7qkynizWJwxOau0tPjnmJKEePN--wD-UYuWGk82gj2YTMQLwP0Svbbk4_jpctjvtM5UeZ14FAWY3PpTMnHwrTwDmqnaynXlDYG17pTrvQ8YQdGsXRUT_wig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951231e9f2.mp4?token=I_x5QmGQ2fLMSjKDm_pTH6Va0X_pXV3hVlvNks-ZMuQAJoYfxqXJlbpOYBoueESjaPvImvKcSL-4awWl9ktEMBAvoml83Cpm0Lios1iUVxtJrcmf6xQiLwltH94uTrM3SeFY_4P0_hUT3j0De7yisoHYAXrJbQdOLTMIdlJGog9QrH0JYAUldznYixiHXLwg94uClggM_NAAp3Bk7W0qHv4VHjdcnJi7qkynizWJwxOau0tPjnmJKEePN--wD-UYuWGk82gj2YTMQLwP0Svbbk4_jpctjvtM5UeZ14FAWY3PpTMnHwrTwDmqnaynXlDYG17pTrvQ8YQdGsXRUT_wig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجزت فرق الدفاع المدني من اطفاء الحرائق المندلعة في مطار الكويت بعد امطارهه بعدة مسيرات ايرانية ليلة البارحة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/76869" target="_blank">📅 13:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇯🇴
حكومة البندورة الأردنية تعلن تضامنها مع الكويت والبحرين وتدين اعتداءات إيران
😆</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76868" target="_blank">📅 12:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇰🇼
هيئة الطيران المدني بالكويت: استهداف مبنى ركاب بمطار الكويت بمسيرات وصواريخ إيرانية وتفعيل خطة الطوارئ  استهداف مطار الكويت أسفر عن إصابات وأضرار جسيمة في عدد من مرافقه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76867" target="_blank">📅 12:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 24-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصلياتٍ صاروخية وقذائف المدفعية ومسيّراتٍ انقضاضيّة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76866" target="_blank">📅 12:32 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
