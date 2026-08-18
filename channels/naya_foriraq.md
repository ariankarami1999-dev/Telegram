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
<img src="https://cdn4.telesco.pe/file/Inx2ztDzVVgsf73jZ8rExwmA-v89JafQG7RPLBwq5hVlhx8ezbTC_HoXyY6AX6lv76T8m76bl52XhiDofr5Dv0gtNcEuQFahvfPCzIyojQRDkf6xxWpD26tILV7SC3CWursswFObvyjqhCQzjW0R3C-KafKZCcKZUBuEgmGCvd79tJKoiWPwHkWNYOnIv7eNkqzmotYXcfdiNtPntqIBXIZj2ASUqYOqke2B0vAQoweJ2yy1iPK00L0G98R2f0qtreqR7y2PbXNhWdOLKXWFa4X3TKYKvsRnhbDiG0yQ8SGCWailEbkulOPba4nG5nuFXo9_QQ6Kf88EYO-A2biJJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 10:43:11</div>
<hr>

<div class="tg-post" id="msg-88040">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم بأسراب من المسيرات على مواقع مرتزقة السعودية في مديرية حيس جنوبي محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 413 · <a href="https://t.me/naya_foriraq/88040" target="_blank">📅 10:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88039">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
تم تحديد واعتقال شخص في العاصمة طهران قام بجمع وإرسال صور وإحداثيات لبعض المواقع الاستراتيجية والأمنية في البلاد إلى جماعات معارضة للجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/naya_foriraq/88039" target="_blank">📅 10:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88038">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
إنفجار لغم في بادية محافظة السماوة جنوبي العراق؛ إصابة منتسب حدود كحصيلة أولية.</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/naya_foriraq/88038" target="_blank">📅 10:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88037">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇷🇺
الدفاع الروسية:
دفاعتنا الجوية دمرت 791 مسيرة أوكرانية في أجواء عدة مناطق روسية خلال الليلة الماضية.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/88037" target="_blank">📅 09:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88036">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
تم إطلاق صاروخ اعتراضي نحو هدف في منطقة زرعيت عند الحدود اللبنانية.</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/naya_foriraq/88036" target="_blank">📅 09:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88035">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني:
قالیباف يزور غدًا العراق على رأس وفد برلماني رفيع المستوى، بهدف إجراء حوارات حول التطورات الإقليمية، وتعزيز التعاون الاستراتيجي بين طهران وبغداد، واستكشاف الحلول المشتركة للمساهمة في تحقيق الاستقرار والأمن في غرب آسيا.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/88035" target="_blank">📅 08:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88034">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By6N0LLjdT6chtp48bZ6IcLCwgBJEJCM7f1RIYAVnBSIs75YuxufSLaU0UMGh3di5vb5r9en95Z88b2TrdYlTUm0gYz8Es6LrdKqliG2KaedVOJxXBhliMeofJyE-ckKK8Y7tZkVAJzpWimx0fYMC73ZKWhRvOFSwpy-bFZzGtnRgYgDw0wRZgGVyP-lXrP5SI8SazvngV6ND07M1vMqNf7g9ofP2ijHCRaCdsMx7-B4ozE0bghxzOu_p_kQPGK3p1zL8ttLGxtvciHNd21r1oQ1pX18-VHE5VCBiqSdf16FTx6sE6TkYtknCbC4NH12RVIYWHHCDLS8igG2znYDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جمهور فصائل المقاومة العراقية يريد نسخة عامري الأهوار …</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/naya_foriraq/88034" target="_blank">📅 08:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88033">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇱
🇱🇧
انفجار عبوة ناسفة في الجليل المحتل مستوطنة المطلة اصابة خمسة مستوطنين كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/naya_foriraq/88033" target="_blank">📅 08:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88032">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044201b963.mp4?token=UYs6oWR63JBhkvZeTZcSPjIATiAtHlqMCIbSUA9bJyQlazaE9z-MH7rJN4bKsF4_ExuSK8Pay5NLiPLctq3i4WCSFqpYHgeLbBxeMMRpRtbiCYKKcHsUKc9sM65XJ9aYNpZ4M-2SlJRUPLAdN6HJIUZx99Q5uI4JAmhV_meCnnE2NZ7S24JQPoQPO4MfRfbdFYt0pVu4A5PgZtFteyYLzwJ9l3xqifey4OHYytPJxzB113vlXgyB_p3HRc0F9SF2EkdhLbOkqrEL6yTSLj1nehFM8iVsh6CA33By0wHDqYlpXd9JJesI65VBCVe9RKpWjkufCCQanHtZnfZjZqvMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044201b963.mp4?token=UYs6oWR63JBhkvZeTZcSPjIATiAtHlqMCIbSUA9bJyQlazaE9z-MH7rJN4bKsF4_ExuSK8Pay5NLiPLctq3i4WCSFqpYHgeLbBxeMMRpRtbiCYKKcHsUKc9sM65XJ9aYNpZ4M-2SlJRUPLAdN6HJIUZx99Q5uI4JAmhV_meCnnE2NZ7S24JQPoQPO4MfRfbdFYt0pVu4A5PgZtFteyYLzwJ9l3xqifey4OHYytPJxzB113vlXgyB_p3HRc0F9SF2EkdhLbOkqrEL6yTSLj1nehFM8iVsh6CA33By0wHDqYlpXd9JJesI65VBCVe9RKpWjkufCCQanHtZnfZjZqvMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
نيران لا تتوقف من موقع الحادث وانباء عن قتلى ومصابيين داخل مستودع الوقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88032" target="_blank">📅 01:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88031">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba96102ee.mp4?token=BihqvcyK2duBxF3q0j07dEtI0eCY9ym-a4naotcWzLKf8idQX8Vae5eqKrAG-xoMnT9UuNGOiHAyntlq2qeEPamLZfFVY98kBwJtqR5LKpkRamFliwe6WW4WfDByO38Zgcp9ZfrKZ89w71Val2yFW20xXyeALGE5MH0d6RYjlyK2TuhbHDxinaIaynAYptnWs4Wr33tjB7LfjTOzvEjpEVtfgtOuyu8-0pCFYGmtbs4DVhhryu1ebzehp9BajMSyu9-6XWydCie5wkBuFD-H47HTFz3cqI3Y3js71KieNYYX_JC9U-LdlJTrYhk_reR5BhEKFharqOoamrC3pZ77zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba96102ee.mp4?token=BihqvcyK2duBxF3q0j07dEtI0eCY9ym-a4naotcWzLKf8idQX8Vae5eqKrAG-xoMnT9UuNGOiHAyntlq2qeEPamLZfFVY98kBwJtqR5LKpkRamFliwe6WW4WfDByO38Zgcp9ZfrKZ89w71Val2yFW20xXyeALGE5MH0d6RYjlyK2TuhbHDxinaIaynAYptnWs4Wr33tjB7LfjTOzvEjpEVtfgtOuyu8-0pCFYGmtbs4DVhhryu1ebzehp9BajMSyu9-6XWydCie5wkBuFD-H47HTFz3cqI3Y3js71KieNYYX_JC9U-LdlJTrYhk_reR5BhEKFharqOoamrC3pZ77zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توسع رقعة الحريق بعد اندلاع حريق مجهول في خزان للوقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88031" target="_blank">📅 01:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88030">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d70a886426.mp4?token=YDnz_VvL6skFyKVijU_9r8INWNn0z7klYitzhOtvhJeBYe0w1QyZkrSSwblbYONtmt6xFejO04Rk3xViuMmucpHy62du5Da4f7V89AsBxLnQCrtdwuPr6cSK89xHvQCmJ9JClC2GQX0fSy4UgADVBTWGQEDFjtcpuPdVLFa0oSfL-Dsrg2aS5DxE8WBKB7UROJoyzQb25MYWsNHb9B516u3acJyYBE87-QG54y7q3EKBhIPh4V2-08iJ1UZTfuS2mmknQ0M4KtgrG2QikO14HW1nUIeCgeMWwmuLp6lxpKyzUaRzcU3XPJnl7BrculRC7AEaSLIDdwkCsvk5INuMdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d70a886426.mp4?token=YDnz_VvL6skFyKVijU_9r8INWNn0z7klYitzhOtvhJeBYe0w1QyZkrSSwblbYONtmt6xFejO04Rk3xViuMmucpHy62du5Da4f7V89AsBxLnQCrtdwuPr6cSK89xHvQCmJ9JClC2GQX0fSy4UgADVBTWGQEDFjtcpuPdVLFa0oSfL-Dsrg2aS5DxE8WBKB7UROJoyzQb25MYWsNHb9B516u3acJyYBE87-QG54y7q3EKBhIPh4V2-08iJ1UZTfuS2mmknQ0M4KtgrG2QikO14HW1nUIeCgeMWwmuLp6lxpKyzUaRzcU3XPJnl7BrculRC7AEaSLIDdwkCsvk5INuMdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق خزان وقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88030" target="_blank">📅 01:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88029">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انباء عن سماع دوي انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88029" target="_blank">📅 01:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
🇹🇷
‏
الرئاسة التركية:
أردوغان أبلغ ترمب أهمية مواصلة المحادثات مع إيران.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88027" target="_blank">📅 01:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف: ننتظر من الإخوة الكبار وحكمائهم العمل على تصحيح الاعوجاج الأمني الذي تسبب فيه الرئيس المكلف كي لا تبقى حجة لأحد، ولضمان الاستقرار وصون الكرامة وعدم الانجرار إلى ما يسر الأعداء.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88026" target="_blank">📅 00:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2ulKireePSMk0Yt3e85bh4cVkyHyUI4dQDeY8SrEJXR3Ia7NSCuohA2jBpBfI_eWiSaGIML-pIAK4T4DiW9syV8jze-qS36vQIb9gmCIuJvucECScFf3V9dcHV-EK0bQftEPJDRhLAq6jDJEjCcHbMr69b8H92zTMo3S9vJCxszhpp07r1BN6lPjYU7dYzknJX-JUwTxgrJPI3cgQ4voKTGYvB8OLl9gj3uFsCLs-M3bZLtyYR1DkKS_sCfSGzUlUKVQpSRHCNCPGqbF-FcXnuG6lcqshL3iO6LX3xxhcGhbtlqgUv20tH78EBeww5ptReG6WYF75G531KE_MCWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف:
ننتظر من الإخوة الكبار وحكمائهم العمل على تصحيح الاعوجاج الأمني الذي تسبب فيه الرئيس المكلف كي لا تبقى حجة لأحد، ولضمان الاستقرار وصون الكرامة وعدم الانجرار إلى ما يسر الأعداء.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88025" target="_blank">📅 00:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owebqe0n9r9g-buGrnCI0sq7tGDw17nRh4jSqZ34kZL1PobB5QflwW-TIPZfcgRp0DF8tHOXxPQj8KXAH1LqoSguYi1_ju1jRvM5hBK5G_wubrczDS3HvzFt2jmfmVTbtX2nDnmzPJvTnUjPL_QjUou6KnpQYzg7UP3H4wVFZJf0O9jmvmMEVklNXhS-LZOhtROk_uLkqTfa68UgLZ-Iq5IBmxG1-BxX5SlaaM780adl_DGHEEPCvKD09GypLL3gfPzkB3406_ltb6ljMKqcLeH2idMwxCjxNE2n6gv_NQK2uJP6rBYUlVLmefAVm88AZGyYWMq4SFhOfjoPaV08lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يوبخ ترامب صحفيًا من سي ان ان: اصمت! أنت تتصرف بقلة احترام أمام هذا الشاب. ألا ترى أنها تتصرف بقلة احترام؟ إنه يفهم. اصمت! أنت تنشر أخبارًا كاذبة. اصمت! أنت صحفي مزيف.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88024" target="_blank">📅 00:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88022">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a9f19058.mp4?token=a3Dv5NCh5XCaPjj2PGsn85GE62baz08aEL9dAl3rxxEC90F1xWMIdYwbK-7VnXFQUL3kZ0Pn39UGPFe0aGFmSgHX1c4IjBHv6q-oA8FVEi6wH1226Bu98SqrfKo-p3sRV5f4hl8qWRYBLpfq6GyUBoPcIlPCOp1BoRlDD_Cxyj2GJvxBzy1jKHG1AQtwkMnbYB9Hlnks-Ir5SEhcSK4JoAUomMPlqr2-f_xAMC276MWgdWczuEiewz6lIChIncuAQUFLA_YArnBB8obkMeleSLc9F9Ds5OIHXG_fSDN1cuE2Px9dW9oS7obR6wbshKDfCcxJYR5ylmRfLDe7H24f1o2A8F1bnvo6nbaf4T6HaS2l930N08MJ9Q4ePCXB3kqgV0O_1HlVZU3924c_0e2bqWf1VXVzM3LquaLoYYOJX8c_rPv98EpcZyxnlQE4LJSUWbmbVuJqgc4-bVJXfRkgcgCzmKm2UbPsTQzqq6fsATDGX4O1IHZdEaEorrlwSKajbG7StJcSYK83QecI2nhZnf8rK6946QWM0kfW1AUk-wlWtgWQdHpK1OJyvc3Q8Auhr2H0dvzLUZ8g99RGqOAXY9OYsxG4j8oSi678xxC6ynl9H3rDujWM83mIOTHTBRP0CeEN5-OB09pBxhQWjxVBDG2uNjRl0QI9sLpCA6K5DUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a9f19058.mp4?token=a3Dv5NCh5XCaPjj2PGsn85GE62baz08aEL9dAl3rxxEC90F1xWMIdYwbK-7VnXFQUL3kZ0Pn39UGPFe0aGFmSgHX1c4IjBHv6q-oA8FVEi6wH1226Bu98SqrfKo-p3sRV5f4hl8qWRYBLpfq6GyUBoPcIlPCOp1BoRlDD_Cxyj2GJvxBzy1jKHG1AQtwkMnbYB9Hlnks-Ir5SEhcSK4JoAUomMPlqr2-f_xAMC276MWgdWczuEiewz6lIChIncuAQUFLA_YArnBB8obkMeleSLc9F9Ds5OIHXG_fSDN1cuE2Px9dW9oS7obR6wbshKDfCcxJYR5ylmRfLDe7H24f1o2A8F1bnvo6nbaf4T6HaS2l930N08MJ9Q4ePCXB3kqgV0O_1HlVZU3924c_0e2bqWf1VXVzM3LquaLoYYOJX8c_rPv98EpcZyxnlQE4LJSUWbmbVuJqgc4-bVJXfRkgcgCzmKm2UbPsTQzqq6fsATDGX4O1IHZdEaEorrlwSKajbG7StJcSYK83QecI2nhZnf8rK6946QWM0kfW1AUk-wlWtgWQdHpK1OJyvc3Q8Auhr2H0dvzLUZ8g99RGqOAXY9OYsxG4j8oSi678xxC6ynl9H3rDujWM83mIOTHTBRP0CeEN5-OB09pBxhQWjxVBDG2uNjRl0QI9sLpCA6K5DUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلية الاعلام الامني:
نفذ صقور القوة الجوية بواسطة طائرات F-16 ضربتين جويتين ناجحتين ومباشرتين استهدفتا الموقع المحدد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88022" target="_blank">📅 00:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88021">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXbhZnS-dCKoI7ydR6d6RGvB2QoOMAvHXNYpaBHYpaOaDB26XksuAv9CVy689J5Q1B0-3Zzavg0NI4wy7PZ7vKQnA7Ay91FmArKZxniSMGYw7VqRa2NfzD9XrUTu7YRM4QH3j7vg7EWaviLgqALV7SQ6cEOc5C023VEy6g6o5f9jlLe7HOwWNS7r7ShZbKgE8Y-eNaxeg3qhmysYDt3lIDld_o2hx1KMJPuEKp6vNV0FiLefD51sVsUMzuO_hG4Pu2RPJbLFSyhUwiB5WUCV2o7EFwt1vf5ffRVhYAMyqur3lGvCDenuMR0_RGkFuJyLlm26XS315JrCPRP8UwT2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر:</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88021" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88019">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb50f87ee1.mp4?token=ZSwMXZXOXM9MQbNLqo6o0NuTHw3UYbkMieCugzaLjCmX8ghKUWpW_Gs7k1b5PVZ8f-YeXRKral3-dd5Rkgs3gIwqkR2GySdOSHlqMUODjcfIc1DnHMQomphH8eR_WbueDwqzH6T2L0FJxZo8FcASFFQA7GG3xT_K_vVC3Sx2jj3tXptOy1SIWTdPIbPSGIwR5hED4XOLmh6ae6-zQ288HB0MyNYIYCvgSNp2W6h-gU21LWOWLoR5soLKwcxkHOP2YK4ASVRqeWoTac821PUB1SgJICdu4IirUyNIvx4rPVGyIk7pDdU0AyyiyJU4An728bWFIqYrUl52J1RG5zessw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb50f87ee1.mp4?token=ZSwMXZXOXM9MQbNLqo6o0NuTHw3UYbkMieCugzaLjCmX8ghKUWpW_Gs7k1b5PVZ8f-YeXRKral3-dd5Rkgs3gIwqkR2GySdOSHlqMUODjcfIc1DnHMQomphH8eR_WbueDwqzH6T2L0FJxZo8FcASFFQA7GG3xT_K_vVC3Sx2jj3tXptOy1SIWTdPIbPSGIwR5hED4XOLmh6ae6-zQ288HB0MyNYIYCvgSNp2W6h-gU21LWOWLoR5soLKwcxkHOP2YK4ASVRqeWoTac821PUB1SgJICdu4IirUyNIvx4rPVGyIk7pDdU0AyyiyJU4An728bWFIqYrUl52J1RG5zessw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القوات الحكومية تداهم منطقة العمارات الملح في محافظة ميسان جنوبي العراق بعد اندلاع تظاهرات تطالب بالخدمات</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88019" target="_blank">📅 00:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88018">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سيصدر بعد قليل بيان هام للمسؤول الامني لكتائب حزب الله الحاج أبو مجاهد العساف.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88018" target="_blank">📅 00:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88017">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏
ألمانيا
: هجوم إلكتروني على وزارتين في حكومة ولاية برلين.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88017" target="_blank">📅 23:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88014">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOUxYnC86k3YKNqd1ajJoL5Xo_cVTt0FwVbuVU12fGLyH9uMquwC-VM5_8BRz54zxqwXo_WZkeCfwAj553vZowGK7Kvt4MEblW0fzmNPcyfjpk5OvzQRTaxrC53iyR4nl-YlID9bFmGPY-asGed07TlaS6NuuTwvt6rnA0AVmaIgkMZ6_4DWZ_LZmU8HvXFjVE_MZKK-pWGKEnnHXjrTcZ71lsSuUOOndO128m2PvkF0OzYBzjZ-oLRiYMvgHtaFa-yaBBfH6e1Uj-SqEyA7xYocdW9E-eYBfM662NsoMbOTSzQGeYrzYw2A2ECYK3bpXCjtgtUWR90Gg4q5DNZrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azQirVIbuyzV_-DhJn-xkU1TucxH8JiVDf9TFJOg_jWEOOc9uaZc_GztfbM1QQxgrvWri9IOkrZeee7qiwAuCp_dss4C2t7bdiNIblVpVCfxvYUmPCYGCEHUXuitMozid9mrNT95X6Qv0oJD7ptLo1y7NJXo-iYRRXuojuhYzye_71omMom8r6tVn5hLhEdY-x0IeApCinZiOi6cHiCM8Aqss7zrIoxtACqj5RKKMnZ5FXEilc931DuS_hUeZk7osPaGY8oMaLhROOxAUQbwl9K5-weMNIAOnXtRpVDYUfGuAgLmX0YwuRH-u6YWHg0G8KZPU-P942JJVQBlKD16Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEsFV6t9eJf0MEFeVNAInJS5lnz52j1Cs91iDkJP7ZXq4g1qOwUHJQyjsnKemyZvLjl04qOs34Mkquf0nFQcb69SdYwcLNktshrHbx1SFOHZ3mBPPY8dalYkK3zySvRGUlVGqyqEvfATa2PH_GpI4UwTxyWUOjXmxZNas8J2-3s7EusZi82zv5Vjh5zEmEBpPEwk2x2o1CoOge6LCq4xurI6zaKGLak2lEIUXf17Khv80PsTtE6xvTmG9SgJ_3ChknH3APWFxDC3-cemWFJFmC9dqcLEFilpumJf15ekqDNpuRZy4fiWSi3bVV7Jx47TG9iehE5NpirfyQ9QpptMaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امتناع عدد من الطائرات المدنية عن الهبوط في مطار دبي، واتخاذها مسارات دائرية في الأجواء، لأسباب لا تزال مجهولة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88014" target="_blank">📅 23:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88013">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏كوشنر: محادثاتنا مع إيران إيجابية وفعالة لكن لم نصل لتفاهم بعد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88013" target="_blank">📅 22:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88012">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY0hMvXjQzE9mcNSbPVs6yCa8cCHI2JBwDrtJHr3kwDXKKZkOCUFPG6Y3iVDL-lJHtK2hrSk7B6Y8YvsDZVG4IMb5wB8ha0p2V_2_PfmirFG9LPX2LOuRm7r7knROrElMOPtQdQvxD9zE1S2wuipUAQlNA9fRAYcCb0ShIcGM0L2KZrrM_OzFhF9LlrDz0v7YDc9HXc4O5cO2onc4INV19YCQhd1WYh9xixDscDeSdsz7M0JDlsAc4kWboAIeDM5GGkf3rTamzgpMRBJJxC7S8jVh-fUqBe4YsuwkwA4pnvqeerNZLqxUGYt9OSc4JZvsn6_rpddZkzoB5EJVLahyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رويترز
: العقود الآجلة لخام برنت تصعد بما يعادل 2.65 % مسجلة 90.87 دولارا للبرميل عند التسوية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88012" target="_blank">📅 22:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88011">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt6BxsHWXx53l9hThsJubZZ6sECMgreHaPOwUTUDQKrTB4NnisgjsMQWEC1x5gR13j4a5P_EPFLPTzgCDNkAFOv5kvTQ_2KgJyKCkVN3I0VZ7Sqkk2Qh75irjpIyttpT-lPL8xVK13rye3LoY1mgdKBy_6e8NZGonC5ao7E2dqPC68eXGhFkWqNGZON_8BoP8e1DB0WOigmn4b7B44O7KlUcaUCEeslba4jZqnBPKs3K767qkAWCsPl1wBeDfLaLueoK3mFpOrpn8JwBKqXSpQCZIXsipOxfhxIpNovSrKd_Qxm5kKcy7PQCgeWjQabuTkiuSWeLryLiYKj1SvJkTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي
: لا شيء يبرر الهجوم المتهور على مكتب رئيس الوزراء بارزاني. يجب على الأصدقاء الأكراد توخي الحذر من المؤامرات المفتعلة التي تهدف إلى زرع الفتنة بين الجيران.
لقد حمينا أصدقاءنا الأكراد من صدام وداعش، ونحن ممتنون للأمن الذي وفروه على حدودنا.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88011" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88010">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def859cee1.mp4?token=Ee8N0AZzygQJXZ-10yVAjg20xIx56J1CpsePH4xeCVDsQzji3UgppUXCiIpZyHHD_wj2HSKLbklWwAYXrK-ryeNepb59BHJLPdElZICxAhJ4YJ1vHrYcGpu3ZrNgScXcsncL8Vhe1UkQBwmymo791vHtYUHMbtgLaaBy1IJXatsFfOzeMk4T_7_yqYnuICuLBRXntQydHbKG26Q5HgVQFSda_CiX1s17X_3xdhOl6lXztwbOLpJROfXxAXAWeomPBxc96x2-1y6EkgQKJ41ayZughF5vWWxVWDK2XkVLXtDkltAfm-JBuQ24QsS-pFiFkscZ3quggQa9rFk7SQ8WdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def859cee1.mp4?token=Ee8N0AZzygQJXZ-10yVAjg20xIx56J1CpsePH4xeCVDsQzji3UgppUXCiIpZyHHD_wj2HSKLbklWwAYXrK-ryeNepb59BHJLPdElZICxAhJ4YJ1vHrYcGpu3ZrNgScXcsncL8Vhe1UkQBwmymo791vHtYUHMbtgLaaBy1IJXatsFfOzeMk4T_7_yqYnuICuLBRXntQydHbKG26Q5HgVQFSda_CiX1s17X_3xdhOl6lXztwbOLpJROfXxAXAWeomPBxc96x2-1y6EkgQKJ41ayZughF5vWWxVWDK2XkVLXtDkltAfm-JBuQ24QsS-pFiFkscZ3quggQa9rFk7SQ8WdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يوبخ ترامب صحفيًا من سي ان ان: اصمت! أنت تتصرف بقلة احترام أمام هذا الشاب. ألا ترى أنها تتصرف بقلة احترام؟ إنه يفهم. اصمت! أنت تنشر أخبارًا كاذبة. اصمت! أنت صحفي مزيف.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88010" target="_blank">📅 21:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88009">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452420aca.mp4?token=HC-mAktWj8HdhlwmHMuuzF_dCxsFmWAxuRSarXQfuQfhAWXAIc6ua2dPM1wHdZ1tCasfdMwSyctqL_tzQWTIVmB1wzVeFZrA9zlHGr5w6TzOax02B1_yWGZaQ0rkm8dl2b2nlMW8QDJa9VPxk5NW6qqcf-kpyueOBrQlJWjG1akRsJDOVSjwKMnfy2rqMyyrYpY8zz-uv3393OLv5DwiYmz5lV9VmBmgocOgRTNIRqCR_HZZfM-gkZjDrIiBASlCdbyOP4o3-tIQCdfz5UWn44saLFSjPx4GEfEPwS-0wB_05_7pWiY2pwdFbNMg6jxfuTUOESX59Nd_Rw7f_jhWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452420aca.mp4?token=HC-mAktWj8HdhlwmHMuuzF_dCxsFmWAxuRSarXQfuQfhAWXAIc6ua2dPM1wHdZ1tCasfdMwSyctqL_tzQWTIVmB1wzVeFZrA9zlHGr5w6TzOax02B1_yWGZaQ0rkm8dl2b2nlMW8QDJa9VPxk5NW6qqcf-kpyueOBrQlJWjG1akRsJDOVSjwKMnfy2rqMyyrYpY8zz-uv3393OLv5DwiYmz5lV9VmBmgocOgRTNIRqCR_HZZfM-gkZjDrIiBASlCdbyOP4o3-tIQCdfz5UWn44saLFSjPx4GEfEPwS-0wB_05_7pWiY2pwdFbNMg6jxfuTUOESX59Nd_Rw7f_jhWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: هدوء، هدوء، هدوء. أنتم وقحون للغاية. هدوء. من معكم؟  الصحفي: أنا من شبكة سي إن إن.  ترامب: أنتم تنشرون أخبارًا كاذبة. اهدأوا، اهدأوا، اهدأوا. أنتم صحفي كاذب.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88009" target="_blank">📅 21:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88008">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dd58f45.mp4?token=OolYRq31ooNpIi8kKaYgc9b2BJEcTKHOO93JCOCw-VxlzScoV_wwqDRPbflDIc2n02TEJiG0yfL_F3aKzTz8qcLsdhWwR-Ehz45SEqkLFbx8-cqQcWXKJOA32e43M7FAHFaPm3P7ldkW3tCBDtI2rsYhoMQL-gDgjnh9ELCj6LUYNqI6oxnBMY_DZy1DnPY-hXwQWLNE2zy_Cu-L6H40epm9wnff1QYf9LNOPDsOQBQZ0HkZQPHoIGMhouXrLPVpjg2atRsRz6TAfaXj08XJIhlnV300g9ibtea__iOsFeqANRJjrKi9ZnmgPrDtdyowN7QVuY_1jt3le_iYTjugHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dd58f45.mp4?token=OolYRq31ooNpIi8kKaYgc9b2BJEcTKHOO93JCOCw-VxlzScoV_wwqDRPbflDIc2n02TEJiG0yfL_F3aKzTz8qcLsdhWwR-Ehz45SEqkLFbx8-cqQcWXKJOA32e43M7FAHFaPm3P7ldkW3tCBDtI2rsYhoMQL-gDgjnh9ELCj6LUYNqI6oxnBMY_DZy1DnPY-hXwQWLNE2zy_Cu-L6H40epm9wnff1QYf9LNOPDsOQBQZ0HkZQPHoIGMhouXrLPVpjg2atRsRz6TAfaXj08XJIhlnV300g9ibtea__iOsFeqANRJjrKi9ZnmgPrDtdyowN7QVuY_1jt3le_iYTjugHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: هدوء، هدوء، هدوء. أنتم وقحون للغاية. هدوء. من معكم؟  الصحفي: أنا من شبكة سي إن إن.  ترامب: أنتم تنشرون أخبارًا كاذبة. اهدأوا، اهدأوا، اهدأوا. أنتم صحفي كاذب.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88008" target="_blank">📅 21:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88007">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d95f5147a.mp4?token=M8MqsDec3kPx-T28-bKmPAyQUgAIymcY6RYiMGUUGeJ3plxPOP1lMfgR6tKM12tlT5K-wRqDsh-315hbbNc0F8AWhbjwh3bZYX1g8Go1jkY6CahN_a0G9WJOz16dbYXYoIXtawm_eE2An6e_aXu_1M_q3FkiG3Fr6seX4smdHLewWKuY48lYfTyZrIAL3JDiOsutAqF0IinnTA_uQwl8MyKnWbdOfsVpRh3CmrWBGdWMo9PoLvqcGxDLwWxuKdPrhWjVPtCHk7zB80kR5uM2wfj8b1uY_JThcvPZWYUxwolOSwJfHZnOxX81i4-ZUWk7pptfaq2sVdL8sOf9r1WBwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d95f5147a.mp4?token=M8MqsDec3kPx-T28-bKmPAyQUgAIymcY6RYiMGUUGeJ3plxPOP1lMfgR6tKM12tlT5K-wRqDsh-315hbbNc0F8AWhbjwh3bZYX1g8Go1jkY6CahN_a0G9WJOz16dbYXYoIXtawm_eE2An6e_aXu_1M_q3FkiG3Fr6seX4smdHLewWKuY48lYfTyZrIAL3JDiOsutAqF0IinnTA_uQwl8MyKnWbdOfsVpRh3CmrWBGdWMo9PoLvqcGxDLwWxuKdPrhWjVPtCHk7zB80kR5uM2wfj8b1uY_JThcvPZWYUxwolOSwJfHZnOxX81i4-ZUWk7pptfaq2sVdL8sOf9r1WBwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترمب: سنقوم بإنهاء الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88007" target="_blank">📅 21:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88006">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4d_yw7VlnwJF6vUsUnQCHQtd9Yo4QxM29yMZs4qu-FCz44uqEKk7eKCz-TFp4fsFlkosiBaJHefztY87EbLWxgP0MIxKITrtIHmjs9m9iNqPazr0Rx6n4GlaBMvK8VWhXAiUcnfpJgJ3RgNiFt-ZMMqI2hFQwxbw0k1y2M6UmmAqdbXSv067nhRZkhI3ovaZfeHF6TYl7W2kAK66d7lVUbURXHhdEhD7GBfAyj9x213YC0z10fl0m7VXvwiWkNbNFFMmrmqs5KriF2OkRQMhG7qA9Hto5xIidepPNDIoG05weSo_tbsHa9k6opujwOcDrAE6FEsam7WWx27t4zfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا
العامري في اجتماع الإطار التنسيقي كل بنادق فصائل المقاومة في العراق هي بنادق بدر قبل ان تكون بنادق جهات محترمة بالمقاومة …</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88006" target="_blank">📅 21:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88005">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
ترامب: قال لي رئيس جمهورية كوريا الجنوبية إنه يفضل عدم التدخل في الملف الإيراني.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88005" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88004">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
ترامب
: قال لي رئيس جمهورية كوريا الجنوبية إنه يفضل عدم التدخل في الملف الإيراني.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88004" target="_blank">📅 21:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88003">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOizaZnOyRnv7QitGkfPHxavCH92LBhJQvvHuoLXm_DHXFlMFDFAGIGEkYTU7bN1GIJmd63nMGO1vflu_TeA8-WhWjWqQusZRWB00pG4Ugr_LL02YkiFiX_5CfDyNUMJn6bLPH4b0ccSfCniEl4FH1oOn_gHLowB-NggKrjcf92Ko4kJB9JYIIkYS65v4QCSSh-KqiSDo3MnxVwYxlH5du6YKwUU9DQO8LAH7UAY_gQwNIMTuG88FMznU5twYvBFRxyHP-dZW93mPMuOCsFT2ZMRTDgBSTtJYLFABiyu7hhUqVhO6yB5WxWUB5Jh4OGLmwHr0Kn0fXDaTahh3LTeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وَدَّ الَّذِينَ كَفَرُوا لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةً وَاحِدَةً ۚ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88003" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88002">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7AxmeJNVVG_fDizDbA9wjY-ZWi1C53A0EhFXXMs0iCNny_P33wQOqjPav_vBHi_7QI0ol9kxqpvPz_1ydLq1775BQlbnJauR7jdJNdxZ6wMBnYCaaDRjOf_yzrzTZY6jXItO0mnshmIdYmzWOpXBFgm1veEn260aAAl8RsuicLrlXhiagpik4LGL5gSsOUgsnvfGQoA_eeWVb_zkqFX51P-Zfs7OAuKuglvFpRhCqXCYfYbeClB9v2Z4FMTUFWRmX3WdyquP9rb2dZcDV0QnH_LdGPY_O5wXSmsBcLZG65Q-k15BkNWu6dc2mxkPiOGmWwMFsYqytJ4qaqzphHG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
أكرر قولي على الإخوة في الحرس الثوري عدم ضرب الأراضي العراقية فهذا عين شماتة الأعداء.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88002" target="_blank">📅 21:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88001">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان   العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88001" target="_blank">📅 21:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88000">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPB3Y2kK9-89fmdagBTMbdUct24IdI7Pe74WeOOCDVvvIkYsxSxc37Z16NxYW12QZxiIZadVBQ2lQKmabX27EA_Tj150cAC1Z5L38HY1nsORbBLIhwyLhNSQKYSRsmSqS9ArmNeJlP-3dsaDBx5yqYo5rham7YzMlSLWka27wsiBAMfxjb890Jp9P2CJIlhHU2W6Ytsq9S5gcSFoKI0l7LjDIRTI9wffhE3CloFuufaZpuhkGpq66g4BuLl-J0lMn-32LGzlxlSz3oh2KVTyBU6adNZfCj73EbxcUrZFPEZObr01CzJD0yiBnEc9upxx206kzgQgFgmfchWTHU0d9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد قليل سوف يتم استلام المخطوف إلى أمن الحشد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88000" target="_blank">📅 21:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87999">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/87999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87999" target="_blank">📅 21:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بعد قليل سوف يتم استلام المخطوف إلى أمن الحشد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87997" target="_blank">📅 21:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87996">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان   العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87996" target="_blank">📅 21:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87994">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLdDfIv4W9_D4SBqyWH3QA_PjDO3_dDRd_XxDZ528CXWL65HzfqqT-D_9RYz_xhAu8Tz3bPjWahrQY_gS2dNP2E8tGPISl3PfF0Lm0PrJCh6brrYg9Kg6iQKQe8SUcGMJQ0kx5fIINF3WU0Z5z55ShmbY6fBGiwCsTUsApYaCC9HdPhZTFlypJc8EltfU3hDJEqFFPS7vs2rvX9RumMxtY2dz-7LF1Fyt_ISdx49MGzXPLfE9dQSxZscSZZsxjMiSfVckKYfB8z7zYF1HTlcm5JRvjBfTEsXs1fP81_HL9lsbHEGbAhYOvGBkHANqaSra1q3mBYdzdGabQqOEh3zHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d8b486d.mp4?token=rZLx7o5lf7qgQ-U46tpKcAByoiF47dQ8wiAR5x6LHYKWoxhXeCxWo6FP1adCYNqPEwX9BGUv06lXN_4w1ElOXJngoSlwP76RvoBva6g-r65MBQLK_adqrX-aDT20BodsfAIjKN89i2lgBbgCz-8bPnaiJiHWyvNTzRDVWuK2kLt6a9MalFjVlpH1SXaDdnhoS0lA47p0PeuJSWUkF6Fk_JYV92SOZaxQSygaJen0d_k-wqwjCV8qZaYG2j3l3_uj9lZ8SqzXXcnHkALU7RsZ2mpdR3uf8y8VAfyb7-ByCKOvPIzg81ckm-mX-zYGyuLY4hKg895Miju-TYizWhF_sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d8b486d.mp4?token=rZLx7o5lf7qgQ-U46tpKcAByoiF47dQ8wiAR5x6LHYKWoxhXeCxWo6FP1adCYNqPEwX9BGUv06lXN_4w1ElOXJngoSlwP76RvoBva6g-r65MBQLK_adqrX-aDT20BodsfAIjKN89i2lgBbgCz-8bPnaiJiHWyvNTzRDVWuK2kLt6a9MalFjVlpH1SXaDdnhoS0lA47p0PeuJSWUkF6Fk_JYV92SOZaxQSygaJen0d_k-wqwjCV8qZaYG2j3l3_uj9lZ8SqzXXcnHkALU7RsZ2mpdR3uf8y8VAfyb7-ByCKOvPIzg81ckm-mX-zYGyuLY4hKg895Miju-TYizWhF_sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف سفينة تابعة لمرتزقة السعودية في  باب المندب بعدة صواريخ والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87994" target="_blank">📅 21:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87993">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان   العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87993" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87992">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb1YiZKpAhBRM38Ro--wvwsKjSbbrfZzK2bvvcBoi8UBEylfy_BThycsMMtMoCY87H4gGDV99K8ZlYJUUmaFzqkqQMN7Y71j_HQJA3lCCCe6BDhye4MxaYkEXM9qc-Q8067mbjiBbPwXZ09514jk0Dgt_iR8bpV8BgWy1-WFaSAnWhoPNStPfz3VX2eLib9CT8ObS4M6DqmzWFjoPNghnxjbB11MxWZoPHHBvsB6N1C9ONpnDpf0vegend-ykUmFuML7bpDzno6ewBsZJkUQWjFMWHaSTEmN5t2bpc_IEhHsis-xXNUM_GEEnNJG4N1mcnmfhWp_MsBzxoGneVsy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان
العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87992" target="_blank">📅 20:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87991">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/031b28e167.mp4?token=kdqdZReEY2_ecgCYDHc94rHHtfM-9KvTlaiAjsHn5ioGK2b8-p7qIY-u4JZ6xD2NnvzMlr-SBvGgZUw3VzNhrSfDlHD14xi_gjeC_m2IhUzKdGbBb5u8_fVOWV_FO0HaMNAHd-4lRcsEXXF60iwn-vSWcJdIx5IbDaNXfkDM2oQya67ACJfQwXWAWLLMcGXONyet2usANQOx7T4EYPlbKTcW6EsIdOR39itChT8_SnSaEkNeZH7wDvC_86wFFm03__N0DhhZDgG5BZDRtjn44rqSgM7uJBUSPIElZDNKxPRd7pQ9ITfwKp_xD5Y67aweXCvUGMUVbYMR1EU-iT38rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/031b28e167.mp4?token=kdqdZReEY2_ecgCYDHc94rHHtfM-9KvTlaiAjsHn5ioGK2b8-p7qIY-u4JZ6xD2NnvzMlr-SBvGgZUw3VzNhrSfDlHD14xi_gjeC_m2IhUzKdGbBb5u8_fVOWV_FO0HaMNAHd-4lRcsEXXF60iwn-vSWcJdIx5IbDaNXfkDM2oQya67ACJfQwXWAWLLMcGXONyet2usANQOx7T4EYPlbKTcW6EsIdOR39itChT8_SnSaEkNeZH7wDvC_86wFFm03__N0DhhZDgG5BZDRtjn44rqSgM7uJBUSPIElZDNKxPRd7pQ9ITfwKp_xD5Y67aweXCvUGMUVbYMR1EU-iT38rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مروحي مجهول يحلق فوق العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87991" target="_blank">📅 20:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87990">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الاميركية في بغداد: إن مثل هذا العدوان على حلفائنا الأكراد الموثوقين أمر غير مقبول.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87990" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87988">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjzoofGMM7sq8rlFHz28kfURtGmAtHtW92pfnr4o8iScGIzkyxLVqNds5V6JcEABw-0mcnHoSiVgqbCK8xqJQ86BYhV-5c340rI3QcJAzC89xn5ae28Oe4ttuuwbC9cJ1Z-FSAkpuv3hz3pJESroCmYIKvIyPk8zf5aBs5npSA4LNkgySqV1kjhQXvvBdBM-oIWwToxt4_br7b4eSwZmKNw824N3Sd5bGBwv4GPac0u2uEvpfHiDbjEUHGzVJb-y27Mz5NBJmJ2evprTz5d8hoj1gGeEQsVVHL06uw70WMzXTwxoX3MPw4mRr93WBx7dWnS1I5_JDFYDD4mpfUpmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f99415a6.mp4?token=d7XMae4eAPMNRm0WIZEDb10T5Lvcru1FGlsB_wbkucQxxK5eGpfl2p3xbVBdwsH2O_O9uAxPwBnCPYUjer--J6Fn2CqfWt3y0v8bsUeB4s7Y2_l0dkvuLiQD2u--7NnmtyHxepHYy4IYqLoze_AxmN1MLgC653cfSXfQydx1WQOZiPQTnJhmI5s_E0uFV-r-0h_1Zk2Aaodjb214g8S93gPPwERFxoBWf1qoTMzyC6EaLmi2reNJOMwzaRUMJsG8GigtLSJeUVsPxvQeL3srGSUI0R-mTAn6efkT4BykGZRElOUhvwWsbxm2b1q95Tf3DaPCLSEAyrJcovqXOBmlk4T1HRuinVYS01ut2mft34hAOfNtLnEQOAXZf8_blZleWUPnz5d2n3VpolhY2H-q3pwbndZNLi9LZCt17XkxcUvde8E6zpPZXOx-pwLrdFGdNk9p3_5Bo-dQexXPFM8cBF31cVhXkzBiqobakP_YVZJiYvVtYJmWIzx2k8xKoWFVPhLr6xltN2mi8rvadlB5h5VOD01SUV7YOZIYBhYPZ1-ARAFsj_fbr2fO2wgHYbaTxK2GokYaGwjt80wZFaX3dZJNeO4dIveT8rUjxhA9Zfc6ZkI__8zBrlJeYthH1H1mpCTstUbP1WFdrVLC4JhG97Glqq1RIalCUGCwuqjj7XI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f99415a6.mp4?token=d7XMae4eAPMNRm0WIZEDb10T5Lvcru1FGlsB_wbkucQxxK5eGpfl2p3xbVBdwsH2O_O9uAxPwBnCPYUjer--J6Fn2CqfWt3y0v8bsUeB4s7Y2_l0dkvuLiQD2u--7NnmtyHxepHYy4IYqLoze_AxmN1MLgC653cfSXfQydx1WQOZiPQTnJhmI5s_E0uFV-r-0h_1Zk2Aaodjb214g8S93gPPwERFxoBWf1qoTMzyC6EaLmi2reNJOMwzaRUMJsG8GigtLSJeUVsPxvQeL3srGSUI0R-mTAn6efkT4BykGZRElOUhvwWsbxm2b1q95Tf3DaPCLSEAyrJcovqXOBmlk4T1HRuinVYS01ut2mft34hAOfNtLnEQOAXZf8_blZleWUPnz5d2n3VpolhY2H-q3pwbndZNLi9LZCt17XkxcUvde8E6zpPZXOx-pwLrdFGdNk9p3_5Bo-dQexXPFM8cBF31cVhXkzBiqobakP_YVZJiYvVtYJmWIzx2k8xKoWFVPhLr6xltN2mi8rvadlB5h5VOD01SUV7YOZIYBhYPZ1-ARAFsj_fbr2fO2wgHYbaTxK2GokYaGwjt80wZFaX3dZJNeO4dIveT8rUjxhA9Zfc6ZkI__8zBrlJeYthH1H1mpCTstUbP1WFdrVLC4JhG97Glqq1RIalCUGCwuqjj7XI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
منصة دفاع جوي "باتريوت" أوكرانية، كانت متوقفة في حقل ذرة بالقرب من كييف، وكانت جميع أنظمتها الـ 16 فارغة.
لم تطلق أي صاروخ منذ حوالي 10 أسابيع.
قال كبير المهندسين فيها:
الصواريخ الباليستية تحلق فوق رؤوسكم وأنتم غير قادرين على فعل أي شيء حيال ذلك، وخلفكم، يوجد مدنيون.
لقد ألقى باللوم في نقص أنظمة الاعتراض العالمية على الحرب مع إيران:
لقد صُدمنا من عدد الصواريخ التي أطلقوها - تلك الصواريخ التي كان بإمكاننا استخدامها ضد الصواريخ الباليستية الروسية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87988" target="_blank">📅 20:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87987">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEQWiMRbjUtVGnn-KWui8WtaO8TtsE40h-P_IgFciEyRoBU8TBQh6iQ312jhfewfU8e7AUzSg84t6glt2yylacg_YL5l5-htWoa-2_vsdAt8RAwc7AcduU0Mj5_bTLnWq7Wcux9xAD9evYu8IKOfsyVLBH7_MzjbHxGl2X1WRnJh1Xfm4dQYN9Er_1gfNN1pLDYyLTMWNSbkxQomtnE13zxVJtTP5syaA-SpqFHXOr9mivOmKnKCMgtOsVpEwMjXA_GGiPz7mVdORj91feb1AaXnabNVtZrNOYOSqh99CKNHapdHqhWEgD45aBVjNL2ZCee8Y4tEGASBMRTtk7zivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الاميركية في بغداد:
إن مثل هذا العدوان على حلفائنا الأكراد الموثوقين أمر غير مقبول.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87987" target="_blank">📅 20:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87986">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoozeGV8XoV-QDeXWHzRjrLOlku6kHyitWfGWMcPuTsbvqtR9K0rJpBsM2xTTTJJAmV00rqudQJTxAh-40tox7sL4MzHTb4d79-V9J9nKxMiA8rq3nlIIZ5HX86oiWv9aQbPc7nouy5C-BOf3qXs2HTyt-LW-JG9AKxYsetbgk_lqetfLsz_3FMz4IfFWwHw4kXyeS1xp-QbGac0oAsJB-MZjhANr6dEqrJ7H3VW3PVlpXe3AqHTqiZTpyNF3AmI3qESbwQsHhxM8CfvM90btYlG0q_CD2AfGmkwWQi4nwpsfGONNAt1OR9VeWrVvhvBjBkZJZ1c93qDejVJxwIvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
توم باراك:
نحن ندعم بشكل كامل قيادة رئيس الوزراء في استعادة السيادة الكاملة للعراق وضمان بقاء جميع الأسلحة وقوات الأمن تحت سلطة الدولة العراقية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87986" target="_blank">📅 19:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87985">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الحرائق تلتهم خزانات الغاز في امريكا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87985" target="_blank">📅 19:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87982">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlJQvX0OpVEArV3eaCzFfjayR3e5uUPhr8-WctmDfEPZjj1mgVzkI7GKIvsr0zaRKh-krBs2Um9UYAAYz8P79tr5ki38u1IVoNrVjI2w-sjgWEkTay2cmbgfKWZxMrunT4Vc932tp0Ss1959ALVdSge2hWPA_iZ4I8jao5smL_jIXCDMSAoeGI-sFB2hIz_lnL_m0KnnKTurEAcVo0fb1IPvxfZGMM__dWi-9fIQs2CXoBRYYJs0-hK7IsWmzBmbG6GZUoBeADV-z2K6XYdua6etyOLaSa-DjQQ_qPaA7eNjtGE5Hl2mpbIcYqPXBG1I1TDdD8iTzn0emQnp-mDpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGNZ-fzpQ6js3YX5IteB3zdBIZYq1npp2KkmPFZdcCCh6JiOEAU8qig-t4PZA7pgCN-7j0aZ1jMCDpyIa-bEGV6NzOnax-ohM5xGvdSMxeOBwbEc3zEREe-n54iV39DZGW7MIepWnilVQJtXXmA9atMjdL3rx7g41BT_IN56uGECfAfqj9a6fGFPve1v-ZN832SswbuT9kRu4dgnV4sytk9HVYHq69hFJbIV5rydyGaKzI0pZ4TVY0ndsd2nvIgX0NltQwcCiZWY1CWA0ha9liVR-IQrUgFZJAQDd41SYtGBF_XkyvHhJewK1dfqxIa5L4bu7EcYamrHVcP25mdImg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حريق كبير يلتهم مخزن ضخم للغاز الطبيعي في مدينة غلينبول الامريكية والنظام يبدأ باجلاء السكان من المدينة</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87982" target="_blank">📅 19:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87981">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98bd6e08e6.mp4?token=id0Vz9wD7t8XS0KR3ACjQH04c4yzRQiuYU1odACcMTXZDnrlZ0COBXF1c85-4qG2Q6BEsp-VDYEVhkrC2a2jWvhuxVg6WZTCpGfCDiXXFOarKOqQowl4BmeGk7_TjOp69CPKLL8SNulYm7rsrqSv3vTg7-yBCIBB8MmXdS6j8uAglpIPBN7JRjInSn2NXlMOrMHznNCA0SRzXz-H58dNYzBM46I3fQN1D-RZHKAOfESYu7klOwbkhLSxI18eS-erA5duOUTrtIgUnZ-xjUoOca9DbAaCKb9si0tjVfcj_AWr29Kl_-_VY9b5UNn-pogpmexWRlNndtRcmO_6-6bC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98bd6e08e6.mp4?token=id0Vz9wD7t8XS0KR3ACjQH04c4yzRQiuYU1odACcMTXZDnrlZ0COBXF1c85-4qG2Q6BEsp-VDYEVhkrC2a2jWvhuxVg6WZTCpGfCDiXXFOarKOqQowl4BmeGk7_TjOp69CPKLL8SNulYm7rsrqSv3vTg7-yBCIBB8MmXdS6j8uAglpIPBN7JRjInSn2NXlMOrMHznNCA0SRzXz-H58dNYzBM46I3fQN1D-RZHKAOfESYu7klOwbkhLSxI18eS-erA5duOUTrtIgUnZ-xjUoOca9DbAaCKb9si0tjVfcj_AWr29Kl_-_VY9b5UNn-pogpmexWRlNndtRcmO_6-6bC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الفضلية بالناصرية جنوب العراق تنتفض  على خلفية اختطاف قيادي بالحشد الشعبي من قبل قوة مجهولة " مسؤول وحدة استخبارات قيادة عمليات حزام بغداد " دعوات جماهيرية للتجمهر والاعتصام المفتوح من عشائر الناصرية امام مركز شرطة ناحية القديم الساعة الخامسة والنصف ..</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87981" target="_blank">📅 18:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87980">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
نائب رئيس البرلمان الإيراني: بحر قزوين غير قابل للتفاوض
.
- ستُحال اتفاقية بحر قزوين إلى لجنة الأمن القومي للمراجعة، وسيدرس البرلمان بعناية ما يضمن تحقيق مصالح البلاد على النحو الأمثل.
- بحر قزوين لا يقل أهميةً لدينا عن مضيق هرمز، ولا يختلف عن مضيق هرمز والخليج وبحر عُمان؛ فبحر قزوين شرفٌ لإيران.
- بحر قزوين غير قابل للتفاوض من جميع النواحي، سواءً البيئية أو الاقتصادية أو المتعلقة بالأمن القومي، ويجب ضمان مصالح جميع الدول المطلة عليه معًا.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87980" target="_blank">📅 18:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87979">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KehVjaZD4UgqGtlUu8K3begpPLvFJ0w5FNO0TR8JOPz7mRPbF03TkheXBNmH3mEuxVC7BDuNmLVkGAKye7nygbqCaax5h1m2gnxccIX3qr1Nfk2FLzwQStRU3vhmkILBH8O5nZNBAS6VG9jG5wO9g2bBbmJ_IcCz5GvXSUicsCPuhdS2OBFyswpR9KvQPZsW33aaGZ-mxYxe59hy-6B2KuhQZg0ICybGEdwXvpvFQJdUX-AaAW3domZIzdmon0ybzw2saPvdcdmdAM6Ya_FZkYSdqugIucyEMwhQZ244uMQVKYYd7SWCHwq6S9GaiOHbhkLlgO4Scwl59hopF2F83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
طائرة امريكية تحلق في الاجواء العراقية انطلقت من تل أبيب.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87979" target="_blank">📅 18:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87978">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن لاسباب مجهولة</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87978" target="_blank">📅 18:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87977">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن لاسباب مجهولة</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/87977" target="_blank">📅 18:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87976">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde4f1ad56.mp4?token=DpvzqDzM7GK1TyVhmraqySXk405dDmSZP8iHwOZQu7GGrxprLwfntjNIwIKDfgebSuRWfLhpFCUSc11fpSW2JKGhKnbo-d_IWPfAS8S7B_DvFRlcpL4PJNWMzg09Tk__GMre2Pug3_GIFY4ywOL6O1a06PJ8OlStie90FHgZUdZ46NLg0a3_r--f3E2NcQiDyFkAIILuneCt5PAgHJ-jyd96AaIm2NtFVKFppfCTfGo7dbSm5bnDVVwva9i-RlpUYbs1yyJguY8HJMpucIe1aVOO5GN7ED8VpB-mPsYdnheRlO8mzf2LgKe50uIouOt8gWItALx_fTZxZY2nB0hnyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde4f1ad56.mp4?token=DpvzqDzM7GK1TyVhmraqySXk405dDmSZP8iHwOZQu7GGrxprLwfntjNIwIKDfgebSuRWfLhpFCUSc11fpSW2JKGhKnbo-d_IWPfAS8S7B_DvFRlcpL4PJNWMzg09Tk__GMre2Pug3_GIFY4ywOL6O1a06PJ8OlStie90FHgZUdZ46NLg0a3_r--f3E2NcQiDyFkAIILuneCt5PAgHJ-jyd96AaIm2NtFVKFppfCTfGo7dbSm5bnDVVwva9i-RlpUYbs1yyJguY8HJMpucIe1aVOO5GN7ED8VpB-mPsYdnheRlO8mzf2LgKe50uIouOt8gWItALx_fTZxZY2nB0hnyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوات الاحتلال الامريكي تعيد رفع بالون التجسس في سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87976" target="_blank">📅 18:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87975">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3805200e49.mp4?token=ZQ-d7yHHsCzIrRHqTDgq960WsguTCp_FGUzAtKpPuJx8K3OBx_F4SCsz34_bvpBuDQpiOOYCukrUfhRdNadfj9nYhkk0cP48ur2PPOurUjf5M2TJcW74Jrni3O81Q7JzCgKJotniQN9Klll_4pr88Y3WSL-xXn-jUw-5MNnwJlaLHK9Zp394MD6vZm3cDhv1hWFvl5vjf1uhMhtOIp0GpVkK4k-RCWdq7xEIboUn-lQfjq9G-yLTG2g-LBzWE83oxgZy7c_yfY0IoQOos8EC81WdjwQK_TAYlt_Rco3hdVztSqo5jgOCqjZW85UyRtsPpZPVnhaoQz8B84GpVw8CQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3805200e49.mp4?token=ZQ-d7yHHsCzIrRHqTDgq960WsguTCp_FGUzAtKpPuJx8K3OBx_F4SCsz34_bvpBuDQpiOOYCukrUfhRdNadfj9nYhkk0cP48ur2PPOurUjf5M2TJcW74Jrni3O81Q7JzCgKJotniQN9Klll_4pr88Y3WSL-xXn-jUw-5MNnwJlaLHK9Zp394MD6vZm3cDhv1hWFvl5vjf1uhMhtOIp0GpVkK4k-RCWdq7xEIboUn-lQfjq9G-yLTG2g-LBzWE83oxgZy7c_yfY0IoQOos8EC81WdjwQK_TAYlt_Rco3hdVztSqo5jgOCqjZW85UyRtsPpZPVnhaoQz8B84GpVw8CQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوات الاحتلال الامريكي تعيد رفع بالون التجسس في سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87975" target="_blank">📅 18:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87974">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L62xoZDeaSqOLu9QgoZL_KUBANiQzZolRj5TIa_jjLpNgwa8vyVxhxsIsohdX0rCoF4kopb5AI-5QFbzjZnGWD3GT3f1HJ-mt8U-Qig1yzeTBTorhD-ShHdVAV8oeLt5PzIVPpAU9Gkc5TvIUePuNKu6bTt72jdtqKRMb0cCDCGwZtFM2oaP14RzTGPnSNkU7Wi9hDOvSTm6oVfOdB4tl7Y0rCIyEA3qYzIoyXyJExWs8P-dqPs5Tj44RHsaDgp0Qz7pgp1dfaDOXM0scOhxiJCuIwRVEBhxRfmst4wrp-k1HFTpawtj2nWrRd-A-8tjnP6sA1xdpMZLHP5yCARCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تصدر حزمة عقوبات بحق قناة الفلوجة:
- إيقاف بث برنامج حوار التاسعة لمدة (10) أيام تبدأ من تاريخ صدور قرارنا هذا المخالفته لائحة قواعد البث الإعلامي
- منع الظهور الإعلامي بحق مقدم البرنامج السيد (علي فرحان) لمدة (10) أيام
- فرض غرامة مالية قدرها 25 مليون دينار عراقي لمخالفة البرنامج وحصاد الأخبار لائحة مخالفات الجهات الإعلامية العاملة في العراق</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87974" target="_blank">📅 17:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87973">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">📰
🇮🇶
وكالة رويترز عن مصادر:
خطط العراق لتصدير النفط عبر خط أنابيب يمرّ في سوريا قد تتطلّب 4 سنوات بكلفة لا تقل عن 15 مليار دولار.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87973" target="_blank">📅 17:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87972">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
دبلوماسي في وزارة الخارجية الايرانية:
كانت دول المنطقة أول من عرقل تفاهم إسلام آباد، وبالطبع دفعت ثمن ذلك.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87972" target="_blank">📅 16:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الكويت تقول ‏ان ثلاث مغذيات فرعية من محطة التحويل الرئيسية الرميثية (B) خرجت عن الخدمة .</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87970" target="_blank">📅 16:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scaF_6yrPsen_l_epJMJsYvXeV9M5XM6i6cMUlgg23GelICriKcy8lZT5kIV9t2t7tAsIl3z1QxvwP61lZN_HsjOlEhEsxKK9OSCmI8hU99ZEYJrxUaX3VWurjj7NVkl9bfyvfnOC3elSSGBG3g45cO-Hokd5fsF5xo_DLYDZTCDCWrtr9VMxsrbhr-EkxKH-xzKJIkaaRxCnjwUAqyB4NSgGyErEYbaM_J_WYZdmcUIIyH0nK6No5RuW083MTOfDju1Ugfl-thR8yHAtP_Ka1k8tr7HHhZNffQRDaU4dRrpTEI26J4SudFBZimVNk_pRVZZBfOBuzzDit6lhl2KwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اختطاف المشهور ابو الجود المنتسب بالحشد الشعبي
من قبل قوة امنية مجهولة في العاصمة بغداد بمنطقة البلديات .</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87969" target="_blank">📅 16:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87968">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
الفضلية بالناصرية جنوب العراق تنتفض
على خلفية اختطاف قيادي بالحشد الشعبي من قبل قوة مجهولة " مسؤول وحدة استخبارات قيادة عمليات حزام بغداد " دعوات جماهيرية للتجمهر والاعتصام المفتوح من عشائر الناصرية امام مركز شرطة ناحية القديم الساعة الخامسة والنصف ..</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87968" target="_blank">📅 16:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87967">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYDjfETvPEPubBKsddV9_7N9d-pHsvDu2Mh5QmUKZpuEHYIt4acr-w3IcUvIOX8O5B9-qfTMPT5T-Kub3SjZbb4KnVwMT1mMJxM5KntC8Sq3B89vKDsemBVmLkEZ_i7k47WdBgWy6VdS6LtrtEOS5qajCrZJ2hB7PsEGjotFHAlM_qfGk_JCk4XKStqUXHMZVv7KXNZdLCk3QwNpl8r_HHKXb8Z4VocIZxfgIYp_m8-84IO1CtoUzMFlQrdh4Tf1UJkGNwkUbGNA83_UR7Qc8Lp_8QxfcWoQXTAqRl-Np8c5EFExJPlZ1rEXU__zCVv1QfiEyaTc6CNug7i4V_HP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم على سفينة والاستيلاء عليها قبالة سواحل الصومال</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87967" target="_blank">📅 16:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87966">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87966" target="_blank">📅 16:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87965">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">#ترفيهي  ترامب يزعم: لدينا قناة اتصال سرية مع مسؤولين في الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87965" target="_blank">📅 16:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87964">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=PsvibrA2kJ9lKoL0NjlAHJpvsBiJzNCXxFC7U7ou1IPks2q0a05sEYJBHj-JVRn76jkGCWyoXsI7OgSUDyJiXfKq_x1rG4eW4M2I44hzGhvz-H8ULIln84Z1_nM8DB393ou_20cueqpv23VQPCI-G2ptTphhW0RXqir2gShdY6JDxAkFb6wi5o3Q6C3xYaAa-hfShxyNrap5ZOBVbac8SB9YkcRZ1pUUE7D2UgEDzyWmXqSqnQl0orrQ4UnLD3ZFbyGArXCAlt3o18fnNRrNijc7GJvLmPKla1XqbD8s2NDLULkRpmRLRz-NFCtizSouqs1bwWoGYZPLQlOxeD3X_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=PsvibrA2kJ9lKoL0NjlAHJpvsBiJzNCXxFC7U7ou1IPks2q0a05sEYJBHj-JVRn76jkGCWyoXsI7OgSUDyJiXfKq_x1rG4eW4M2I44hzGhvz-H8ULIln84Z1_nM8DB393ou_20cueqpv23VQPCI-G2ptTphhW0RXqir2gShdY6JDxAkFb6wi5o3Q6C3xYaAa-hfShxyNrap5ZOBVbac8SB9YkcRZ1pUUE7D2UgEDzyWmXqSqnQl0orrQ4UnLD3ZFbyGArXCAlt3o18fnNRrNijc7GJvLmPKla1XqbD8s2NDLULkRpmRLRz-NFCtizSouqs1bwWoGYZPLQlOxeD3X_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَى نَصْرِهِمْ لَقَدِيرٌ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87964" target="_blank">📅 16:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مسؤول إيراني كبير: سيتم نقل الإطار الزمني الذي حددته إيران إلى الولايات المتحدة والدول الإقليمية عبر وسطاء.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87963" target="_blank">📅 16:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مسؤول إيراني كبير: جميع الكيانات الإيرانية ستكون مستعدة لتصعيد التوترات في مضيق هرمز والمنطقة إذا فشلت الدبلوماسية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87962" target="_blank">📅 16:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مسؤول إيراني كبير: حددت إيران مهلة لبضعة أسابيع للتنفيذ الكامل لمذكرة التفاهم من قبل الولايات المتحدة</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87961" target="_blank">📅 16:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87960">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📰
مسؤول إيراني كبير لوكالة رويترز: قررت إيران تحويل سياستها من دفاعية إلى هجومية بالكامل.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87960" target="_blank">📅 16:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📰
مسؤول إيراني كبير لوكالة رويترز:
قررت إيران تحويل سياستها من دفاعية إلى هجومية بالكامل.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87959" target="_blank">📅 15:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">القوات اليمنية: تمكنت القوات المسلحة اليمنية بفضل الله من استهداف سفينة إنزال عسكرية تابعة للعدو السعودي مع أربعة زوارق عسكرية مرافقة لها في البحر الأحمر أمام سواحل المخا، وذلك بعدد من الصواريخ الباليستية وكانت الإصابة دقيقة ومباشرة وأدت العملية إلى احتراق…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87958" target="_blank">📅 15:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87957">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
توجيهات حكومية العراقية بأن يكون عمل الشركات النفطية على مدار 24 ساعة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87957" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87956">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف سفينة تابعة لمرتزقة السعودية في  باب المندب بعدة صواريخ والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87956" target="_blank">📅 15:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87955">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامب: قد أدعم شخصًا ما في الانتخابات الإسرائيلية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87955" target="_blank">📅 15:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87954">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH4szANWQBbsulxh8ps6zTWv4oI9nOU7FRhal-mUBgZrRrfOocrE1O3021b-qBUjfrQW7Ns3NQnWS79dbVcQqJTKA3om0tGlzD7E1HcMh6Zh-Nmz70qPKb3no7Mw_iUM3kxVhMJWQO_p7HWNjS-Euf250xFjKKK1zLjRbkPDW2cerIDn4NjN-STy9Td0UnUa6sb17B6tkIY0VW6SivCkVZL4zypEqcuoZuuh_6HMnBVc708Ec3eYeQM39nu7zT9yfqgdnoLMiMpEsKC19tF3G1d5_6lq1KX1JzJjYLx45GT2uDh3PNCLjvz8KiD1TGXsqiXJZwEwYhKvSaeGvh1ggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
هجوم صاروخي لأنصار الله على سفن معادية في باب المندب.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87954" target="_blank">📅 15:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87953">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhNEhpWz9zLUmgPixnVCqPIVJOzgzAr4XA1xq-qSOfkZGp0e3RLDozkXh6lqatEOnH5Z24Dju4ogEbjktsPfwBEgoEr_n9YFyS6KOsLSbMqJHktyHCjprwn8dnmucKpV_d2LfimBa6h6U5ugs5j3bkfaTeNcianYSWhbnMuIMlwND1Wua4ADJT0uk_HD_0auGVoLpCaGQFj6svKUQuJSgCw7VyulVrCmzQExBPNawE219rVElz156uso7XcToL0DXnEZc9YnirmSws8k523DYBudf882YYwYS1_tAD-ya-obYqzRROgfUdv2V_OMdRGh6DH3n71xAeo1q9Y9S2kAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عبور السفن في مضيق هرمز يعود إلى الصفر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87953" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي يضبط 651 هاتف و341 شريحة هاتف كانت مخبأة في أماكن مختلفة داخل السجون العراقية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87952" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
🇺🇸
‏ترامب يهدد بقصف سلطنة عُمان إذا وقفت في طريق الولايات المتحدة</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87951" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">#ترفيهي  ترامب يزعم: لدينا قناة اتصال سرية مع مسؤولين في الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87950" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#ترفيهي
ترامب يزعم:
لدينا قناة اتصال سرية مع مسؤولين في الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87949" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87947">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObUR2kPpFCDyKPVpoJf7DnyiWqz1vT8MtGRApOeH6cPHTYcn8P5scoAEfUtZZYBZiPqfKA6PhauQ72EzccUZosFwydsFrAhX88ez_huH-yznSPAban7uHXuel4aokVr4yRCmYjNV0IQmRsM3hGpwGj1PS2ahCKCOWAnZnu6HoT_Y6Iy2ewyKJDC6HWWJ9ca7FMoEh_O5V-E1u4QWHq20sn_OZY1ZLMhFoPBaywVDHb0Vm00lpNuIEq75aKeoJPuaSSaz_D020bM232Sxv1NVoiMHb6xmoPewVyMFD2QYh6zGA9C0SHXXQctF26qHlG5ZmGbGEkSPs1l4e_MJdMQpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَى نَصْرِهِمْ لَقَدِيرٌ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87947" target="_blank">📅 14:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87946">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اعلام النظام السعودي:
الموافقة على تمديد فترة الـ60 يوما بين إيران وأميركا.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87946" target="_blank">📅 14:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87945">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b2e069ba.mp4?token=NeFNDbUMLHZQDlLoCrWV4Pt-zcowFp9LnH_0N25YAuQLU-aX5_7XXF9Xs24Z4tiTv6Isep9qQU72hw41OsY_iARa8DIrUcP_YkAb2QTu6I0p3_IhqUwz00CgwcAMGwAPX9YC7EWv9C23drHfp6wyogteJHU8qMskNBx8c-CZ4Gs54MFv5iWRN7ApCYybA_lEE357Cu52hUFHLLYx2jJpPuoXw9UIt3b-VvGcrY8esbyR0Z-L5STgfmOeYaMXz3fQHyJBFfiL0CyrHLCcI0-Sp_3ZfZ7kaylZFOzQUvZsf0bk9qPDm3wb9a6F0Rz2kmv1VudMesFe04-ZYIi8Wg_Dxq89Y2OOgyGmebX__e3im_U5RpiwWPZbGMq4rhqlHxUZokq__jV4UMGpz9Ug-i9G7uUCfFHW7bhie9EyQ2QKtua-AFAYFDsAmtOt7OpODSOqZ9031sNczGDDa5YtRMIbTeegShMuuF5hc-K8YSLr9_5ECPE7O1iE3RW_w2aGcQ3HhpI3YUfwQkDBt-eyuBGqW8U5WbWNs6fcXyx6LGuOkSKqGLJujyXUx4NNThUPl9Lr1GyJGAJxSroUOyUefLOZvAGu7rVaKHjvfg5Dey2nwo-xuYYndbxF68Zmzw9UQk3PfzeFVugyLDeR24jTrPzbGOTplVgebY0oqBfOeYQTQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b2e069ba.mp4?token=NeFNDbUMLHZQDlLoCrWV4Pt-zcowFp9LnH_0N25YAuQLU-aX5_7XXF9Xs24Z4tiTv6Isep9qQU72hw41OsY_iARa8DIrUcP_YkAb2QTu6I0p3_IhqUwz00CgwcAMGwAPX9YC7EWv9C23drHfp6wyogteJHU8qMskNBx8c-CZ4Gs54MFv5iWRN7ApCYybA_lEE357Cu52hUFHLLYx2jJpPuoXw9UIt3b-VvGcrY8esbyR0Z-L5STgfmOeYaMXz3fQHyJBFfiL0CyrHLCcI0-Sp_3ZfZ7kaylZFOzQUvZsf0bk9qPDm3wb9a6F0Rz2kmv1VudMesFe04-ZYIi8Wg_Dxq89Y2OOgyGmebX__e3im_U5RpiwWPZbGMq4rhqlHxUZokq__jV4UMGpz9Ug-i9G7uUCfFHW7bhie9EyQ2QKtua-AFAYFDsAmtOt7OpODSOqZ9031sNczGDDa5YtRMIbTeegShMuuF5hc-K8YSLr9_5ECPE7O1iE3RW_w2aGcQ3HhpI3YUfwQkDBt-eyuBGqW8U5WbWNs6fcXyx6LGuOkSKqGLJujyXUx4NNThUPl9Lr1GyJGAJxSroUOyUefLOZvAGu7rVaKHjvfg5Dey2nwo-xuYYndbxF68Zmzw9UQk3PfzeFVugyLDeR24jTrPzbGOTplVgebY0oqBfOeYQTQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تباينت حركة الملاحة البحرية الأسبوع الماضي، إذ تراجعت عمليات العبور عبر مضيق هرمز 19.5% إلى 95 عملية مقابل 118، مع انخفاضها من 19 عملية في 11 أغسطس إلى ثلاث فقط في 16 أغسطس. في المقابل، ارتفعت عمليات العبور عبر باب المندب 6.7% إلى 254 عملية مقابل 238، مع دخول 150 سفينة البحر الأحمر وخروج 104 سفن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87945" target="_blank">📅 13:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87944">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز المخا بعد هجوم باليستي ومسير لانصار الله على مرتزقة السعودية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87944" target="_blank">📅 13:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87943">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات تهز المخا بعد هجوم باليستي ومسير لانصار الله على مرتزقة السعودية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87943" target="_blank">📅 13:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87942">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
نائب القائد العام للحرس الثوري:
في الحرب الأخيرة، تم إسقاط أكثر من 200 طائرة عسكرية (بدون طيار ومقاتلة) تابعة للعدو.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87942" target="_blank">📅 13:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
إنفجار لغم غربي محافظة البصرة جنوبي العراق، أدى إلى إرتقاء شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87941" target="_blank">📅 13:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87940">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
🇮🇶
نادي إستقلال الإيراني يعلن عن إختياره محافظة البصرة العراقية لإستضافة مباريات دوري أبطال آسيا النخبة.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87940" target="_blank">📅 12:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87939">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
هجوم صاروخي لأنصار الله على سفن معادية في باب المندب.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87939" target="_blank">📅 11:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87938">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تصدر قرار منع ظهور إعلامي بحق أحمد الشريفي ومشعان الجبوري.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87938" target="_blank">📅 11:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87937">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هجمات تطال مقر جهاز البارستن في أربيل</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87937" target="_blank">📅 11:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هجمات تطال مقر جهاز البارستن في أربيل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87936" target="_blank">📅 11:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87933">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6708faef.mp4?token=YaBNMeQfG_lYCthTb97xu83S3KSAFsd0yZri9aXG4cAOVWrMdMaz7HxNuIU2Klg7cVIYsgyn3vJGEnswgue8PMi887D6KCXhjO-qxarzpld-xRXrc89iwvi883UOKhZHF_p90fHHjtYWYH9qHD3Fj50hO6DzTCnmWIVD9VlBuKbvzEA7ZtaflrtyuxMfK0E1sELXS-FYsimDxzxhoCiZxrBlk2bV2on-sF2qJeKmmaEbo6UL0xQzOArzkkFf7TZxxZYT6y9h0HbxPl6TAiD_rrkoLuy_vJbjgdt96ogHqiL25VWrHl5ItV8hENSy5PXR7NQq5dsj9AbxR4lYhMOwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6708faef.mp4?token=YaBNMeQfG_lYCthTb97xu83S3KSAFsd0yZri9aXG4cAOVWrMdMaz7HxNuIU2Klg7cVIYsgyn3vJGEnswgue8PMi887D6KCXhjO-qxarzpld-xRXrc89iwvi883UOKhZHF_p90fHHjtYWYH9qHD3Fj50hO6DzTCnmWIVD9VlBuKbvzEA7ZtaflrtyuxMfK0E1sELXS-FYsimDxzxhoCiZxrBlk2bV2on-sF2qJeKmmaEbo6UL0xQzOArzkkFf7TZxxZYT6y9h0HbxPl6TAiD_rrkoLuy_vJbjgdt96ogHqiL25VWrHl5ItV8hENSy5PXR7NQq5dsj9AbxR4lYhMOwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إنفجار وإحتراق حافلة تقل ركاب صهاينة بالقرب من القدس المحتلة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87933" target="_blank">📅 11:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87932">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  مضيق هرمز سيُعاد فتحه عندما تلتزم الولايات المتحدة بالتزاماتها في اتفاقية إسلام آباد.   ما يطرح بشأن ممر مائي جديد مع عمان يعود إلى فترة ما بعد انتهاء الحرب بشكل نهائي.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87932" target="_blank">📅 11:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87931">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b86b7421ae.mp4?token=m9dz9RH5oI-gXVMn__0XF0kz2OTlma1hJzYq-dkj36qiD_n6rfssI3_lInycs9FzpadRHVuFoJpSvEx4436YMePuSfgTiJePfHd8lyJWFo8rsuzRIgvooue2ytkbGDrCztb-TF87VDRXdT60Igr60xdCel9BrflxwTLrTrXaF-C9jsq7rjkpGy06yZyt8FEfiD5tMHeHTPcENqsjik1pFeVExElSwmw_iiSP0wOqwk_LQjvtG_4a_Phde8D0W_ckmkVF9HIP7FcN7_K5vshPmETjwh7bChSobS5tutDAI2nLN6k6gxzyvoXehEYPSUlug5eVmmwV5TPSvDn0-e5JZIXKBCQe_RciAhsH6DlTJ1_pCVrSIm-HDGsJbwPGOzu5N1REJg5Xg5A_vKhF9GEcb2RYGnBkdlXLXDPiETkxvS_CfGGiwOhXD2--9XgdpbXOk2rF1Cs1jZ7zXma7oQIX9JVPO3oY08dsmEYWCtdNFdCCe7gyDxoE-yZCKMkjSHKA-Qn4xnt87TtZzh9p6JsvVylhiLaR9MNSkblKv5y-Iw5v2_fgPMvrBnrAsMYg-ASxT8vs9kBKlE_r4DfiIDDiozDCnsFbCmdT70d4dR8paoVF_26g3sB9lVTWuXx624lH0XM-YxPWElys7dXqumnTh5gqK1mCdn6e6Se5nMISo_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b86b7421ae.mp4?token=m9dz9RH5oI-gXVMn__0XF0kz2OTlma1hJzYq-dkj36qiD_n6rfssI3_lInycs9FzpadRHVuFoJpSvEx4436YMePuSfgTiJePfHd8lyJWFo8rsuzRIgvooue2ytkbGDrCztb-TF87VDRXdT60Igr60xdCel9BrflxwTLrTrXaF-C9jsq7rjkpGy06yZyt8FEfiD5tMHeHTPcENqsjik1pFeVExElSwmw_iiSP0wOqwk_LQjvtG_4a_Phde8D0W_ckmkVF9HIP7FcN7_K5vshPmETjwh7bChSobS5tutDAI2nLN6k6gxzyvoXehEYPSUlug5eVmmwV5TPSvDn0-e5JZIXKBCQe_RciAhsH6DlTJ1_pCVrSIm-HDGsJbwPGOzu5N1REJg5Xg5A_vKhF9GEcb2RYGnBkdlXLXDPiETkxvS_CfGGiwOhXD2--9XgdpbXOk2rF1Cs1jZ7zXma7oQIX9JVPO3oY08dsmEYWCtdNFdCCe7gyDxoE-yZCKMkjSHKA-Qn4xnt87TtZzh9p6JsvVylhiLaR9MNSkblKv5y-Iw5v2_fgPMvrBnrAsMYg-ASxT8vs9kBKlE_r4DfiIDDiozDCnsFbCmdT70d4dR8paoVF_26g3sB9lVTWuXx624lH0XM-YxPWElys7dXqumnTh5gqK1mCdn6e6Se5nMISo_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تظاهرة حاشدة للخريجين القدامى في منطقة العلاوي بالعاصمة العراقية بغداد للمطالبة بالتعيين.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87931" target="_blank">📅 10:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
هجوم صاروخي لأنصار الله على سفن معادية في باب المندب.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87930" target="_blank">📅 10:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87929">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
مضيق هرمز سيُعاد فتحه عندما تلتزم الولايات المتحدة بالتزاماتها في اتفاقية إسلام آباد.
ما يطرح بشأن ممر مائي جديد مع عمان يعود إلى فترة ما بعد انتهاء الحرب بشكل نهائي.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87929" target="_blank">📅 10:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87928">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
تعطيل الدوام الرسمي في الوزارات والمؤسسات الحكومية كافة يوم الثلاثاء الموافق 25 آب 2026، بمناسبة ذكرى المولد النبوي الشريف (12 ربيع الأول).</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87928" target="_blank">📅 09:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87927">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
أشياء جيدة ستحدث قريبًا جدًا. بعضها قد حدث بالفعل.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87927" target="_blank">📅 09:33 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
