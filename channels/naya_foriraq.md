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
<img src="https://cdn4.telesco.pe/file/pMPxmvEYW3MA10h5wfjcznt9GhhcXmnfsQdF5zF6uzIH_7A8-FuwKMAgHMdGimui_4uItFLvZROoritSs_YTKm8XYKFCzamWZF9L9v_6JK6xiYBJ6ETsDzkowSIXW8p59MlF-TSOIKa3CmcNBN80eh7Bj1EMJXXpTlpOD3_H7UOykJjiFGPHWhtANTvEi-1e67PgZn1RYZEdFSV55iOVyIO7H_G3oNiDzf5J8F-qEWR9bNW4PLVbSGRSCKJT2Br6SO9iary3Mi12h8gl5qbPJzUB4XR9eeAaui4hZyqgcRfxA1uDMSo1NcPcL39NrcGRymjEY8QCeU3oxelmysmQxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 19:27:59</div>
<hr>

<div class="tg-post" id="msg-75247">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
🏴‍☠️
مجدداً من لبنان.. الطائرات المسيرة تهاجم مستوطنات الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 458 · <a href="https://t.me/naya_foriraq/75247" target="_blank">📅 19:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/naya_foriraq/75246" target="_blank">📅 19:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75245">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-05-2026
خيمة مُستَحدَثة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/naya_foriraq/75245" target="_blank">📅 19:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75244">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور.. المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/naya_foriraq/75244" target="_blank">📅 18:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75243">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/naya_foriraq/75243" target="_blank">📅 18:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75242">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91423ce81.mp4?token=jgix5QbUFBpwTksZrREezVPtmOauNOmVVhUyDvffEAem466FKsikQzT7iUA-GbCDoG2KJKFbklQpiHiD4OTZHJh7EnFQjM7oBIl2auS7igxC555IvOs0Vj1W_Ph1POaAftpkXQp9fyJm_olxlIyYwK1pMoAG-DBmodEtPTiVFREinX1ySDN3PpA4Rc9hv-7qp_37HOh7Jke_zb5jKc3dXssgkTCM_C3Jl5ypxcObydqek9jZR4S_YdDrLDvp72Ar9TG8IrIVBBK3pph9awfHamIXLtd1RKEVG3g4K5V0Jargx6CCbAAEU-xJBcZ4uj-grpaMBx7p0uVAPQFcZ1wtRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91423ce81.mp4?token=jgix5QbUFBpwTksZrREezVPtmOauNOmVVhUyDvffEAem466FKsikQzT7iUA-GbCDoG2KJKFbklQpiHiD4OTZHJh7EnFQjM7oBIl2auS7igxC555IvOs0Vj1W_Ph1POaAftpkXQp9fyJm_olxlIyYwK1pMoAG-DBmodEtPTiVFREinX1ySDN3PpA4Rc9hv-7qp_37HOh7Jke_zb5jKc3dXssgkTCM_C3Jl5ypxcObydqek9jZR4S_YdDrLDvp72Ar9TG8IrIVBBK3pph9awfHamIXLtd1RKEVG3g4K5V0Jargx6CCbAAEU-xJBcZ4uj-grpaMBx7p0uVAPQFcZ1wtRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
استهداف موقع للجيش الإسرائيلي قرب مستوطنة مرجليوت واشتعال النيران داخله.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/naya_foriraq/75242" target="_blank">📅 18:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75241">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور..
المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/naya_foriraq/75241" target="_blank">📅 18:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75240">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">في خبر غير مهم
وزارة خارجية دويلة الكويت تستدعي السفير الايراني وتسلمه مذكرة احتجاج</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/naya_foriraq/75240" target="_blank">📅 18:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75239">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/naya_foriraq/75239" target="_blank">📅 18:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75238">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تهديد المحلقات يتوسع باستمرار ويوقع خسائر كبيرة في صفوف القوات على الأرض.</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/naya_foriraq/75238" target="_blank">📅 17:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75236">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlyAkEQhsn_UnDBu5LBGOxvVh6gODBK_PpJfJtOFLmvz-d1gls2Y_CG6B8lbPhbZbFMLJay33SSc-YAcOsCh6OsdVgER-BViTk48ftMPJddfXEHlYDKzvmZmWDZP4La7xyI1sG_bvzFJayZF2iDSKBR9vlAPrW_KBsWOLyxDh5OkjHs2fGnZgOyoVlL709x_EUzsDps7Mv0M5hfmb-lpCPOW0omwQB1xSPfDTboJoSh2WuVlwZBl_Q82_rqCbRV0k2BaXgf4DpJ8T6CxWHLQaUmmRvYcs8wcOqsHQ0hE81LtDVN13OL77oNoiOzBZz9IeyfB75vUMxuhmrydqlcwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTVQIEGr4VCQqg4w5nFqZNs7HfR1OvJvBSd2F6w8bk5q6WfdaGbNQlHftxcb33RP3BJaxYefrONGiQH6V0um_3fHRut-1enGB21O1zCkJpVMiWkiakk3-e7yHdNx3DiZUZAxjPXWPFC7AxV6FUv5pzYXg75qOkLoXcV4Lgrbrg_wcgs_KK4AOR6fTZrPr5yOE5H67PA4FrnUx6GGBcCB518xPFFBUvzZStzFyt65oh8Dl6c7D1Esp_NwFoFjSXzQX0kU4uqC1WSWchp1T81u8ap10NjfA6CZCoW3ccTelWQCvNHEQr5S6dXEv2tGWgaEyoQZ6643_mKK41-9sCD16A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇻🇦
🇮🇷
بابا الفاتيكان "ليون الرابع عشر" يمنح أعلى وسام دبلوماسي فخري في الفاتيكان لسفير إيران لدى الكرسي الرسولي محمد حسين مختاري
ترامب يعاين الاضرار
😄</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/75236" target="_blank">📅 17:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75234">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: تفعيل الدفاعات الجوية في الجليل الأعلى بعد هجوم لحزب الله.</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/naya_foriraq/75234" target="_blank">📅 17:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75233">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تفعيل الدفاعات الجوية في الجليل الأعلى بعد هجوم لحزب الله.</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/75233" target="_blank">📅 17:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75232">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇷🇺
‏روسيا تعلن إجراء اختبار ناجح لصاروخ "سارمات" النووي وتؤكد دخوله للخدمة نهاية العام.. بوتين: مدى صاروخ "سارمات" النووي قد يتجاوز 35 ألف كيلومتر</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/naya_foriraq/75232" target="_blank">📅 17:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75231">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامب: نجري اتصالات مباشرة مع مسؤولين إيرانيين ولسنا في عجلة من أمرنا للتوصل إلى اتفاق</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/75231" target="_blank">📅 16:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75225">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hu-tMG5qIHE6l0E4C1FQzBeS7GK08sgc980k_3j9eFTIhZNDypEhT2dXgLqW7gXgnnS4XauF4RuZ7yuXav47vicuBTVYdL6MVYH3lcV0pJ6-pXNKzPCyF9lDDWQthw4-pl9Wqt7Zz9h7LEkYQFBoqFzAD4-Epkufg90ZENosd-WAFQTUzQi_08CjyJQODNhtcMbFipdnZZ277dr-gZrD2QPTmi6rudvMhBLGSjdOtLG-rE8KU5A7OC-p2lPPrzHsmpqh-M4z43bGvvBXpBycDe5oYUzKgLrHoB9HY-P3_cOthe7atbontZaMDZGTE3NgKXi8RQEiWZsse004pa_aTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXAIrQZj1L6rofic-m099OZwY8zqH0Bf383lkjHs3nWg4gPmuHXWJGUHj6hnaW1JsSyFKimJukXzAc6UNzE8CNpmbI-u_KhDlz64b8L9N73lMYd2bFyx1D61c50_L-l-aFHirfRZqIgOZJkCFNdu1V2_NmluZn60D5Dmj6PQPZ0mObBMTjGjXudiT-Gu2KpzjGBaGdQ9Xrr2XfU8w6XEwMAzoa9Lv9R5ZePKklPoW7tI3fhWOug0AF7FL-W7Ru2ns0FNy-dA8r0xQDOdLVB2GcnvxIewZ05cRZo-52EdEOOHjcNmpTzwYliNriRIjvNjLh2hQHGffITWVL95qzKZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcXjXd7CmLXEq-IwgW6cCYIQcHz5gmH9PPGOAoq08hFZYQyrNR2JiGv1QUhxRZqr81SlceB_Mld60-s93mAQqVhUd4eOj1XG7lsacbb0DrRH1NhT81zoUkKui7YUjGfi3-EkdE6GmOzhRPJdrW86JMJOoGJlv8YddRKhQepF_JJEswUUluWTycIkNT-efr2sG91oY34jCdWtjeZPPFtzllCpVjuHvARxWrR9SZ4IXWcMq0ndVAMdtTWRvZZDQaW4twgOXw-r0PNxNc937p94Eec5ZmEzqbZxfBBXCgYGjT1JZNYvBb8TG-oa6zDakX-MfAPU91w52zpEBjT-GeWbeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arR3xdZsYAFzGU1CUqOryRfl37VjQbkIKkhwg-bwcG4YCjZ0ndoXYMVcT8cUB_RLDOTPhM94EVA7RZMB2bEgs6ndLaR1DzwQak_QnmttD4EJBzAeu-ZeHri1tizR3Zt0Iw_yhk36YcB2Ni34iEFLOSdjEy7tyizUZAJtVuTY19ZtBUAVLN392WQmF2xWTrMkXSOHR46G94UiYmSgFPh-kK1TOS1J_qznQeDLl6ge-MmSiWnHM6kfRJhi4ZAnkAh9OldkJgYRLgc5FPA6-_LZh0Cy-VvWG10TQrNeAktktp4TcuzaABRN_ki59_wOVcNHKFvwE3I34P0Pv1cDQ-Twdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvJMcJw_jKfKWFCk-1QT-7xeuOJTxj0nCq06PBqhtR373BhJU1DN2NXPDvvT1HbjKikEPM5A3987hv0UoiLPVxwo3ML2r82iHm0s63RvkI2KKQEhSH3dUW4a8yq-SFvbI8a6yjQkegS8MJR2A1pwLb25f0tYxG_jKhJWEtbOkQAMr0pj6gR2cG0gB3UWelVkXVCo5ecJE3FPYSvkwoW2wvotwoMX0YDfArm8JgR-ODxpoVAFqanF4m7_sgHPRKT8Y9a3cZ_9EVopWpvyqowjl-MulqC9VnHIHlaq1ivJtR_5He75qeo7ONFsuaB2Vtgihc3O3dr6YmimrRxIlzpJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgtD131l3WzhOAh4EISckThFzCHMnlBzBT3oQ-cWMeWC5I8CeY44UQb_yPg2WJh8jrZ2JC4Qk-QV6K3c6-ATzSORyiUYv7mCfHGZYqWJfXNMUb3tysQ9IlUvLicScTaeiEv3yK7K_PwN5ZRM2PTDn7aa_ZQPnIvZdq9EU0Y1M6AfYfgMU5tp4D6Xdkw7GlqQsGABXP0cmjwHdAKFh_ee1zlowbciVNxz2D5YqNyzhGhWVobvOyFza_pf9-dkorh6X4QwlgAilFXJO6_dhh3bFZlKy2udMmuhBidvR80iyXk4q8k1OGvbYFVAGC3zDuoWtKsSmjYQImGttDje7ReqKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماذا حدث في منطقة شنان قرب الاديان لمن هي الـ عجلات العسكرية المدرعة ماذا يفعل الأمريكان بالأحداثية  ‏37R  KV 750018  3478349 ما قصة هبوط هليكوبتر عدد ٦ ونصب خيم أمريكية في صحراء الانبار جنوب ناحية النخيب منطقة شنانه الاحداثيات ‏38R  KV  69654  98230  لماذا…</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/naya_foriraq/75225" target="_blank">📅 16:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR5NXyxHeDTi1CeVdO1iHHEShTfhlwM7u3uMkU20yhoGafJdjlJP9M2kf9zlKr9jqGyH1Faugor1phLHUq3R-9E6vYMGN8iezgA-aWqD57XLXIENc6jK3nhRUajU1mbGEgCRmuX6yo4J3bH-uzjfXXj0QX0ZIYWnIm9TD_WtG1XIjlAQKWo7jd8OYnpFdge8lproZOiniel0uYdgFtMAP_JRtAZaGJJNlTLGZwc7ZdV8YiikqcjyUuWe5Z-hAoj4Y_gdNpYuBHzQeWOFm0M04QCVVgqBddh2pOY2UHlMAnUHDEG08ZQrf0d-UOOJEHz7dQ5ZoXtAuhNXehOy1d76Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي الايرانية:
قد يكون أحد خيارات إيران في حال وقوع هجوم آخر هو تخصيب اليورانيوم بنسبة 90%. سنناقش هذا الأمر في البرلمان.</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/75218" target="_blank">📅 16:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزير الحرب الأمريكي: لن نكشف عن الخطوة التالية ضد إيران لضمان عدم حصولها على قنبلة نووية</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/75217" target="_blank">📅 16:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الرئيس التنفيذي لشركة أدنوك: هناك نقص في مليار برميل على مستوى العالم بسبب إغلاق مضيق هرمز.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/75216" target="_blank">📅 15:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 10-05-2026 منزل يتموضع فيه جنود جيش العدو الإسرائيلي في بلدة طير حرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/75215" target="_blank">📅 15:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: الجيش الإسرائيلي لا يزال يحقق من أين بالضبط أُطلق الطائرة المسيّرة. "من الشرق" - قد تكون اليمن، إيران، أو العراق.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75214" target="_blank">📅 14:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/75213" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75213" target="_blank">📅 14:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هجوم من الشرق يتعرض له الكيان</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75212" target="_blank">📅 14:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">المتحدث باسم جيش العدو: اعترضنا طائرة بدون طيار أُطلقت من جهة الشرق.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75211" target="_blank">📅 14:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519ac44ef2.mp4?token=DyNv4rLYZj25BBc7EQo-hjYikrCWN7BZG8jk08dIyw24PLo3PAa17bzlHKSERW4WNHHykz0nXWXdPap3kIlGBW5zNiq_H1Pl2JNuFZhP40xzjBxKYONQIB7WmTWJYnVpkuMV9NOYP9TrcV4GPab7GktrzhuUT1DW2oi3zfSwrltxz08_4GJoI-soBv9DboShRF6q8dWzJGjApVL_a4U2v9KKTnwpZNSVOZGXbUtnajOk50AYa2U6Nebd9taQ3cLnuNXEfpa9E75_vO7HBbZodF4xj1_QbHmhbGRz-wZ131z3XksOOWDaLEFh2djtB5piNNXQWc10hb0LDIqmlNieVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519ac44ef2.mp4?token=DyNv4rLYZj25BBc7EQo-hjYikrCWN7BZG8jk08dIyw24PLo3PAa17bzlHKSERW4WNHHykz0nXWXdPap3kIlGBW5zNiq_H1Pl2JNuFZhP40xzjBxKYONQIB7WmTWJYnVpkuMV9NOYP9TrcV4GPab7GktrzhuUT1DW2oi3zfSwrltxz08_4GJoI-soBv9DboShRF6q8dWzJGjApVL_a4U2v9KKTnwpZNSVOZGXbUtnajOk50AYa2U6Nebd9taQ3cLnuNXEfpa9E75_vO7HBbZodF4xj1_QbHmhbGRz-wZ131z3XksOOWDaLEFh2djtB5piNNXQWc10hb0LDIqmlNieVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتحدث باسم جيش العدو: اعترضنا طائرة بدون طيار أُطلقت من جهة الشرق.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75210" target="_blank">📅 14:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75209">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رغم التأكيد في بيان سابق
الاعلام الامني العراقي: لم يحدث إنزال جوي ولا صحة لوجود قاعدة في صحراء النخيب</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75209" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75208">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بلومبرج: ‏تطلب قطر من السفن في منشأتها الرئيسية لتصدير الغاز الطبيعي المسال إيقاف تشغيل أجهزة الإرسال والاستقبال الخاصة بها.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75208" target="_blank">📅 12:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75207">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
الأمين العام لحزب الله: لا علاقة لأحد خارج لبنان بالسلاح والمقاومة وتنظيم شؤون الدولة اللبنانية الداخلية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75207" target="_blank">📅 12:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بي بي سي: تجري الولايات المتحدة مفاوضات منتظمة وسرية مع الدنمارك لفتح ثلاث قواعد عسكرية جديدة في جنوب جرينلاند.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75205" target="_blank">📅 11:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0eLTgI1UE2nuCiSPzPZ9MM9Z1QB9Od5E0rumDrWC-pvFWbVgdgNMUmOlfoF_YFsLOWVKtHHSRFhrN5smvFN5T4NZRqK9xvDLm1PTfPPWhDcHqZ9gYPSGGlS0V_-2ogh8nj5J6K0iLiHcghJ1IbFXTWul1EHEB72qbizfX6tPIYcj3mINsn7n_XBc51qdz_603jFE-01lmaBK-JkhMb9QfFFotiN19MTF6lPIt5DxAuT2JV41Ogn_Rk14v39vqMgcnwUBZ6JrPey4mxb4iJ5kn-MZyowACibKf-gbusaiS5yDIfoBMyymgwqdE5WxwK1YLx6i_oLhD5SiIsMaT2wNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
النفط يلامس 106 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75204" target="_blank">📅 10:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية:
دعم الطلبة بإضافة خمس درجات لتلاميذ الصف الخامس الابتدائي وطلبة المراحل المتوسطة والإعدادية للصفوف غير المنتهية، بما فيها الإعداديات المهنية بفروعها كافة
إتاحة فرصة أداء امتحانات الدور الثاني لتلاميذ الصفوف الأربعة الأولى من المرحلة الابتدائية المنتظمين بالدوام (حصراً) والذين رسبوا في امتحانات الدور الأول، بغض النظر عن عدد المواد الدراسية التي لم يحققوا فيها النجاح.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75203" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي في البرلمان: أحد خيارات إيران إذا وقع عدوان تخصيب اليورانيوم بنسبة 90%</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75202" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: إصابة 8 مقاتلين من لواء غولاني في 3 اشتباكات قرب النهر على أطراف زوطر الشرقية جنوب لبنان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75201" target="_blank">📅 10:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇵🇰
الشرطة الباكستانية: مقتل 7 أشخاص بانفجار في سوق شمال غربي البلاد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75200" target="_blank">📅 09:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇱🇧
🇮🇶
لبنان يعفي العراقيين من التبعات المالية والقانونية المترتبة بذمتهم عن تجاوز فترات إقامتهم داخل لبنان خلال السنوات السابقة ولغاية 31/12/2026 وإلغاء إشارات المنع من دخول لبنان على كافة العراقيين المغادرين إلى العراق ليتمكنوا من زيارة لبنان مستقبلاً دون مشاكل.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75199" target="_blank">📅 08:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASqRY_oU_ZT0X_2VYicfEDMchaz6xzVKn8izdtwK1qjM8afRE4yQ1tqlCpQeIu1A9SBCarvl1TpAINjDyCziiGTkbFV-VonHfEUEmgfHpulACIG4aqtzXqb8hN6p-79eyuQflFy-juuRDWOVypg5cdC9iitycNzYR6Rc8cL4cdcV4ydw65XcVJIfCYf5AztGMgJ-R_CQ_9HudH_tf7E976e_ouoQZOXKakgN34i2B6scVIXG52ouPAs19-mvyyNGOlMXVujOwuOg0isAmRB_ekGChsrb4RqzSvcpC047bOdeRVS931UF8fiiQVf6ZTfsz3yxINXn6MXis4DxILc3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد تباطؤ الاتفاق الإيراني الأميركي، أسعار النفط تقفز إلى 105 دولارات للبرميل.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/75198" target="_blank">📅 01:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ivrp3_TdcpZvPRYDvLEZn5me9k7nGSOcPIU8E76X6sz0xTNirBc4QcON6E6AQ62jcU33PUhlBdlAY3wDxH7tywxyTDBoquVtlJI2Sq2kQxNqw2lWzBy77v1AsgJPPMxHyYUWaEL9ToQGyXdzwSkKDxd-lJSzG9oaUzFiOU6388L8N-Uruy6B42xwM4s94lWQeU_uu2F7CxPUzYo6iVs0Q3wosBBtGBlO0xKapaz-lYmNvZMPJTM0ZULSet54Zx-vbv-G1mS8mE-78cNHnl05ewFEfht22uMheWTiqy8vgkkAshUpatCpAO_0dRTvsyumpkz23eaUGbHRvVjHKcSE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب : اني حيل فرحان بزيارتي للصين ، الصين بلد يشك شك وبي خوش قائد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75197" target="_blank">📅 01:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c76991be.mp4?token=lJTNJtsJQyD3TWTcJT7c9ghO3Y7LA2nq-PuZUQW3WeRs2sjYRgKf377_kY4ej0u93NdBG1VBlT-bMKj4KDFFgTvoYFhxsnp44ENifwj_9b1gM2HmfHNuB--taQ87XRv3lhgMhMme65xkqaGdT9z1FDHo9hQccTj8-e8ODn52ZvWJf90_vuPmya6zyRycMxxyegKc7PtyupQhWFWBHUsr8EFZFM1PkD8f8yyge9712__shbS4K9bgtdzv8kZKMCgY67ik0kVwW9OHpHWHELfspTl1kYwSMBNESNdZ5Mqe3BL4JV745x8-O9IB-irP_4XMzXTSxCAfKYuESgrtoawVhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c76991be.mp4?token=lJTNJtsJQyD3TWTcJT7c9ghO3Y7LA2nq-PuZUQW3WeRs2sjYRgKf377_kY4ej0u93NdBG1VBlT-bMKj4KDFFgTvoYFhxsnp44ENifwj_9b1gM2HmfHNuB--taQ87XRv3lhgMhMme65xkqaGdT9z1FDHo9hQccTj8-e8ODn52ZvWJf90_vuPmya6zyRycMxxyegKc7PtyupQhWFWBHUsr8EFZFM1PkD8f8yyge9712__shbS4K9bgtdzv8kZKMCgY67ik0kVwW9OHpHWHELfspTl1kYwSMBNESNdZ5Mqe3BL4JV745x8-O9IB-irP_4XMzXTSxCAfKYuESgrtoawVhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇮🇶
من تل ابيب الى الانبار   تمارس القيادة المركزية الوسطى الامريكية التي يعد جيش الكيان جزء منها ؛ عمليات استطلاع مركزة على مدى ٢٤ ساعة و على مناطق الأمن القومي الصهيوني خط امتداد ، النخيب ، الرزازة ، الخالدية ، الكيلو ١٠٦ ، خط ال H 3 ،  ومناطق الطاش ،…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75196" target="_blank">📅 01:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75195">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارة الخارجية الإماراتية: دويلة الإمارات تؤكد أن حادث اختطاف ناقلة النفط قبالة السواحل اليمنية يمثل تهديدا مباشرا لأمن الملاحة البحرية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75195" target="_blank">📅 01:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75194">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPIENVq8dxNGvo3UVxl2QUPqq_l8-5y_5VaTTNXTlyFX7t0JxbEStGcFdHMbOGBfO3u_qmjF-idRkkANGjlg3XaacAdbg3J0ew-IIwG5yyQM8yHD19bWYc7rCGUCTg3MWAtLmribalnfjD8ttMlaeWIXZB8oxzIGwLp-MvfGPblsht1JQUPcJYE9qyaXbv4VLoby7lhcwSxuuoyfrTmV6rPp5f8JmMJvBTlrOdElIIFOuEeFBgJYDXYNdyCPwuhUzsCk4ayxxIeMWdrBau7oDcamG11eqDR58D25hTmA5flq_C-Vfrld53Qfmc626ttm7RmdaAG2GCE46c_GPrdloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇮🇶
من تل ابيب الى الانبار
تمارس القيادة المركزية الوسطى الامريكية التي يعد جيش الكيان جزء منها ؛ عمليات استطلاع مركزة على مدى ٢٤ ساعة و على مناطق الأمن القومي الصهيوني خط امتداد ، النخيب ، الرزازة ، الخالدية ، الكيلو ١٠٦ ، خط ال H 3 ،  ومناطق الطاش ، عين تمر ، وادي شنان .. الكيان يعتبر هذه المناطق مصادر خطر ستراتيجية كونها مناطق منصات إطلاق صدام السابقة نحو النقب ، مناطق ذات طابع ديني كونها جغرافية نهر الفرات " من النيل إلى الفرات ممر داوود " ، مناطق بعيدة ومفتوحة عن السكان ما يؤمن أمان نسبي امني لقاعدة إدارة عمليات متقدمة .</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75194" target="_blank">📅 01:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75193">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4pVt7cm5xtteYZ3axjraX5zeaQLf40viEjZYreCtKlaFE-Fyj8p7uLRQoRFLxhLMSKHKodRdsa42TIdF5tnyFw4PexgXHMlBj5x1LYtn5c5z6g2S0g1O58m1B7cK5CidJcgryk1Iuh3fJl3sBP1XBYkDN2FvGAfRhrMiu03gWYjJXjEgkYkNhqoqE8oGa4TLZ3_rubEUUiV-bLOquAxmpFqqRb1-sJNd7N-mZKP_EbQEpO-NZ2sfJMNjAG0jcxkEuyauKIYfAMKvM6UTGAyxh6mKqSfKsUQ5FY_Yzuz-LqGGQ5qGT2xXFSl6uV-o9OSdwHAlZrw602N4493cLqWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
لا بديل عن قبول حقوق الشعب الإيراني كما وردت في المقترح ذي النقاط الأربع عشرة. وأي نهج آخر سيكون بلا جدوى، ولن يُسفر إلا عن سلسلة من الإخفاقات. كلما طال أمد مماطلتهم، زادت الأعباء المالية على دافعي الضرائب الأمريكيين.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75193" target="_blank">📅 00:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75191">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTWn5la1RxdL_ihFcOPywpgYEJX99gnZ6Tz5UxydlDWuNbpv_ng2VpvNWI622Io9oefki8MjGkfUDCEKEqGbmnXHtQbJyw2iNhXt34ixd5XsR1DhZ97bHu7q6UwZlFZj5KRAIzgEqHE_b0-o0kzq_yqY_25MTGHnU-ibdOTtOLU6QUj3R4GZFRcLNZkJ-bk6_pstb5t6FZW2jR6nhzfyywyYZ926Bb5IubhmjXiSPqxB5tOJIjc8Nq-7samtMZMWTtzjVZsMnGouCcylTggtmMIBJ804ll3y5CMc6uOyVYTwk8kUkH74zFudYNcHm8TrJYbir7cWieRbKxtYR86mtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبنا العراقي العظيم
هل لديك معلومات عن الأشخاص الظاهرين في الصورة عناوينهم اسمائهم … مكافأة مادية في حالة معرفتك اي شخص ظاهر بالصورة راسلنا عبر البوت …</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75191" target="_blank">📅 00:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75190">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
قامت دولة الإمارات العربية المتحدة بشن ضربات عسكرية غير معلنة على إيران، بما في ذلك ضرب مصفاة نفطية في جزيرة لافان في أوائل أبريل - تقريبًا في الوقت الذي أعلن فيه ترامب وقف إطلاق النار.
أدى الهجوم إلى اندلاع حريق كبير وأدى إلى إيقاف تشغيل المصفاة لعدة أشهر. ردت إيران بضربات صاروخية وبدون طيار ضد الإمارات العربية المتحدة والكويت.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75190" target="_blank">📅 23:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75189">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">طيران مسير من لبنان يخترق مستوطنة مجدل شمس في الجولان الشمالي المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75189" target="_blank">📅 23:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75188">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0682c7b887.mp4?token=KLLAs7pgqG10d8EERcxugR0PpI1-9ew3K-KDnvSm_qiIIEOFqf7o2pGv6QHzyOQ8_E32GG-krfZMjDXEfIEObe4QHw4Pu6WGNxQoVA00kxUamAgRv8C5G8_6NWvMCyL4Vd9IZw8eTaTOepoV48MeN6A74B-pzDMKiJLAFEW1iOeEcP7a2B39dkNP-_PIBh5xOXPKOlB9m7vgedjkvDpkQUha4TAQNmgtpvcVwIUDZKErURWGnZ_Q-wTspTv808RmGKwo39t6GX7VOXQa703w5EqWcILhHkKQWOAtBEGUeCCbjDhNGM2aHxdlIAn9WcgLNOkdeCuTWJdxvrVPb41KPji4VbpXN0_cQOYiJBLaQO55MrUWGM39xUBPvhhQk6nifdh3B9wTOXjPBB8a1GOdksUfu-OEePct-0atrlFuvbTGjSjh622MG86aLzsnxpNbCmdDjHTFYcfHjYfCCOSrSqq-en8_3EnY5hnCRgEOND2686Gmitgd3XIWMl4VEvbQMBhvWg7QNYvBws3KCHqtqQwxKEJYFLbfLsLGiMqcMYE3FySRtpVwbAEXpvTZCwNDZAkpf-SKXFFqqJ4ym2mQE67yP4RZeetbme4SiivsgSsJP0siXGmZw_bwObXdFOjmh_v3X4CexFsFYu5sOuxKvEpeq8QdMoqZQbghSwTadMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0682c7b887.mp4?token=KLLAs7pgqG10d8EERcxugR0PpI1-9ew3K-KDnvSm_qiIIEOFqf7o2pGv6QHzyOQ8_E32GG-krfZMjDXEfIEObe4QHw4Pu6WGNxQoVA00kxUamAgRv8C5G8_6NWvMCyL4Vd9IZw8eTaTOepoV48MeN6A74B-pzDMKiJLAFEW1iOeEcP7a2B39dkNP-_PIBh5xOXPKOlB9m7vgedjkvDpkQUha4TAQNmgtpvcVwIUDZKErURWGnZ_Q-wTspTv808RmGKwo39t6GX7VOXQa703w5EqWcILhHkKQWOAtBEGUeCCbjDhNGM2aHxdlIAn9WcgLNOkdeCuTWJdxvrVPb41KPji4VbpXN0_cQOYiJBLaQO55MrUWGM39xUBPvhhQk6nifdh3B9wTOXjPBB8a1GOdksUfu-OEePct-0atrlFuvbTGjSjh622MG86aLzsnxpNbCmdDjHTFYcfHjYfCCOSrSqq-en8_3EnY5hnCRgEOND2686Gmitgd3XIWMl4VEvbQMBhvWg7QNYvBws3KCHqtqQwxKEJYFLbfLsLGiMqcMYE3FySRtpVwbAEXpvTZCwNDZAkpf-SKXFFqqJ4ym2mQE67yP4RZeetbme4SiivsgSsJP0siXGmZw_bwObXdFOjmh_v3X4CexFsFYu5sOuxKvEpeq8QdMoqZQbghSwTadMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-05-2026
تجمّعًا لآليات وجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75188" target="_blank">📅 23:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75187">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
قيادة العمليات المشتركة:
لا وجود لأي قواعد أو قوات غير مصرح بها على الأراضي العراقية وتحديداً في صحراء كربلاء شرق النخيب والنجف.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75187" target="_blank">📅 23:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75186">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271439eb30.mp4?token=hvqIrIFqAWfx5HLIb0fwJ-IUYBq8rEmRdAQW9QOxNrhKUko95hSVqwANuKVCjqQtWUvM3yQKJySaEJ2ZGZw_wen0Za98OgL1AQy6MQkdDOGNwqQ9U3fPlpXFRl4SZZfzJcKUkagtWo5XkXYMObZZ7UEgtl1ci5MKa8HvDzK2wJiamoLXVTubsef_fn1HiIz7b3BIiFk-dCCgUyzkVHpQvI7SXm8FE8epTKsjDb-F2ImwAQ6WxkjcU0gzFpzAluPoRyjDdjpivl4OgShvHCmUHmrBNUCN-9vxhqYmRYP_y17mw2OEdkMZTfRlD7WdaGTl2D8Ku9DcVGY2oM6BNZC1Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271439eb30.mp4?token=hvqIrIFqAWfx5HLIb0fwJ-IUYBq8rEmRdAQW9QOxNrhKUko95hSVqwANuKVCjqQtWUvM3yQKJySaEJ2ZGZw_wen0Za98OgL1AQy6MQkdDOGNwqQ9U3fPlpXFRl4SZZfzJcKUkagtWo5XkXYMObZZ7UEgtl1ci5MKa8HvDzK2wJiamoLXVTubsef_fn1HiIz7b3BIiFk-dCCgUyzkVHpQvI7SXm8FE8epTKsjDb-F2ImwAQ6WxkjcU0gzFpzAluPoRyjDdjpivl4OgShvHCmUHmrBNUCN-9vxhqYmRYP_y17mw2OEdkMZTfRlD7WdaGTl2D8Ku9DcVGY2oM6BNZC1Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
"لامين يامال" يرفع علم فلسطين خلال احتفالات نادي برشلونة بالدوري الإسباني.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75186" target="_blank">📅 22:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75185">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b0e607ed.mp4?token=aFg9R90NePNq8ZXy1T-I7ljuwhpba3QEvKzoa2LsmzXacei3uFS9T7mpGyhRwmj8Bce68ckc9szeJCRrrQvt8dM013xMltdbR1SumGTWkzFHLEIcnMqFu3ftvvpAdK-4Knmp_FdoRO62EFhl6UoMhFrEKedEbW6J67ZTm0PAl_Ok7i5dIEFvuckDVaSSMSePoFBqtMmIEwlwc2P7MMwMWu5DaUOG85MKEvOvom9Iaj8XouyC4R0v5OhPwZcly7oGjXltRVAyaSTUGXugsU6rlyCLbXiQ0nB7lQ9h5TgmfsqFZ0SVN8nIuqM6SBllFplY98juLL2nUAIkID3n2m8ucmHDzH_x9YzcpvKPX4Cl06uZBAJIvaKzsfWkFEbH730BYqUod2MRyyAIgzmdlx-SoIbzWKPCYJst7S8oeLp7GGDB3BDJEsAYTQPfsp-LRIpVW2oDsk7Xr2Cy5hENumUFmeTGrzMzMwdKakm9Aq83gW8Ge_DUKNTv07QKXhHWORgxnwRJsYX-uCC-NUjRWDE_PIkAH--_cgQkwQ74KUEMJlk5QauWqnUJtVb_WQXNTTAhFSkpp-4mzn9A5D5c5yxutj1Ew9725RaGB36oMeFYlvklIO93hIig8sTyJEmepRf7aYI7dEathHtuCoCmyBfJ-XDX_a5v235rCfoF5QA2dQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b0e607ed.mp4?token=aFg9R90NePNq8ZXy1T-I7ljuwhpba3QEvKzoa2LsmzXacei3uFS9T7mpGyhRwmj8Bce68ckc9szeJCRrrQvt8dM013xMltdbR1SumGTWkzFHLEIcnMqFu3ftvvpAdK-4Knmp_FdoRO62EFhl6UoMhFrEKedEbW6J67ZTm0PAl_Ok7i5dIEFvuckDVaSSMSePoFBqtMmIEwlwc2P7MMwMWu5DaUOG85MKEvOvom9Iaj8XouyC4R0v5OhPwZcly7oGjXltRVAyaSTUGXugsU6rlyCLbXiQ0nB7lQ9h5TgmfsqFZ0SVN8nIuqM6SBllFplY98juLL2nUAIkID3n2m8ucmHDzH_x9YzcpvKPX4Cl06uZBAJIvaKzsfWkFEbH730BYqUod2MRyyAIgzmdlx-SoIbzWKPCYJst7S8oeLp7GGDB3BDJEsAYTQPfsp-LRIpVW2oDsk7Xr2Cy5hENumUFmeTGrzMzMwdKakm9Aq83gW8Ge_DUKNTv07QKXhHWORgxnwRJsYX-uCC-NUjRWDE_PIkAH--_cgQkwQ74KUEMJlk5QauWqnUJtVb_WQXNTTAhFSkpp-4mzn9A5D5c5yxutj1Ew9725RaGB36oMeFYlvklIO93hIig8sTyJEmepRf7aYI7dEathHtuCoCmyBfJ-XDX_a5v235rCfoF5QA2dQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 08-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75185" target="_blank">📅 22:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669465c27.mp4?token=o5rEcBGRZY4tCk8UHCh15FHP_wl8OYRJ9Wzho82EoBkbBK4-nl0kc3OAP0Rut06qFbouJfe0Chrb93JJOvo4Voaw-tZAtZbKn6d-2kePHdA9ZAQMuQj8yjMHEyjhPJblJssHcpbb1Mep6qgzjhRENcHDdRZKD2H-LT0o1nhwaBtZptToEV-GhjBomxoZKyAy_ZghKZ29LWrJAHKqC9jtTrd4ZvWYPjoPzrntKfw7pKyg8OZ8kyVWDyoYrLOMH7UAlJeM9Rb63K3fgbuzCm6j7ORA6iWQluBt7hoFB5pPS0MsyrQIgl61ZSYh7NjsSuVIxsApz7Oc6oIMVuElr26xoEuDnrh2jYZ7c-OZF8g2v8irEhQIeypaJI60HldTEFGM8PHNFTxOq3BsD57Q2kRyJezM8ID7vC8X7WBi_GKWVhsYpIxDB9mVGtHLSSbKvA7u7EaepMaQYmk1P476SWsdXn-0ISJhX6p674tG0dhfLo4cTI2D80ppTxnN5FivRXOObVyXwPvVkEZI7cXvcKZi_9rdTOrgxJ-g4G0RMUvbX_rFmJ84boYbJW0FuH0m9VhJQATa9SRBT27iqZbMvH-tuPTUmAzuBQnkIbCcTXBh6L2H1YUbiWGiEjInWTDqFOMo7-6lAK7F3nMUZS6Gj-08Pe8c6uzgyqcMb1P6ZSgD3qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669465c27.mp4?token=o5rEcBGRZY4tCk8UHCh15FHP_wl8OYRJ9Wzho82EoBkbBK4-nl0kc3OAP0Rut06qFbouJfe0Chrb93JJOvo4Voaw-tZAtZbKn6d-2kePHdA9ZAQMuQj8yjMHEyjhPJblJssHcpbb1Mep6qgzjhRENcHDdRZKD2H-LT0o1nhwaBtZptToEV-GhjBomxoZKyAy_ZghKZ29LWrJAHKqC9jtTrd4ZvWYPjoPzrntKfw7pKyg8OZ8kyVWDyoYrLOMH7UAlJeM9Rb63K3fgbuzCm6j7ORA6iWQluBt7hoFB5pPS0MsyrQIgl61ZSYh7NjsSuVIxsApz7Oc6oIMVuElr26xoEuDnrh2jYZ7c-OZF8g2v8irEhQIeypaJI60HldTEFGM8PHNFTxOq3BsD57Q2kRyJezM8ID7vC8X7WBi_GKWVhsYpIxDB9mVGtHLSSbKvA7u7EaepMaQYmk1P476SWsdXn-0ISJhX6p674tG0dhfLo4cTI2D80ppTxnN5FivRXOObVyXwPvVkEZI7cXvcKZi_9rdTOrgxJ-g4G0RMUvbX_rFmJ84boYbJW0FuH0m9VhJQATa9SRBT27iqZbMvH-tuPTUmAzuBQnkIbCcTXBh6L2H1YUbiWGiEjInWTDqFOMo7-6lAK7F3nMUZS6Gj-08Pe8c6uzgyqcMb1P6ZSgD3qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إنفجار كبير في مصفاة إتش إف سنكلير بولاية أوكلاهوما الأمريكية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75182" target="_blank">📅 22:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
البيت الأبيض عن إيران:
ترامب يضع كل الخيارات على الطاولة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75181" target="_blank">📅 21:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdFMLmO6_Q6L7q5dcVNXbOIUMpxQy0BgRSi6R2qdxTut13utv4AkbQqPt0V0SBPBiacVVSpG1zGs0qameEeVj6feye3qbNlktr_cnqEQ8xX043hKd7WZKhCmxfMgpI6XuGIezennnla_KH2KKqNZo7o3I4dkB8XhnJYhdZTdde8R21tf6jV0FzoR0yEqz6DtRKOlDT1bpWEDpPpr2Vs1UA_q7IkuDlykWv0Knq1syXa2S5IXDGxNebujBdEcFbO05583XDMqwKOVdGt3YPvNh6FmIvtGcl0rxBsY9D9ptaSX6-93DS_EBzJwLgxE06Jr7oMSyuFX_33BYKLCkDJA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني:
‏قواتنا المسلحة على أهبة الاستعداد للرد على أي عدوان بأسلوبٍ يُعلّم الدرس؛ فالاستراتيجية الخاطئة والقرارات الخاطئة ستؤدي حتماً إلى نتائج خاطئة. وقد أدرك العالم أجمع هذا الأمر. نحن مستعدون لجميع الخيارات. سيتفاجأون.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75180" target="_blank">📅 21:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
أكسيوس عن مسؤوليين: ترامب يدرس العمل العسكري ضد إيران في ظلّ "وقف إطلاق النار على حافة الانهيار".  ‏يجتمع ترامب مع فريق الأمن القومي المعني بإيران يوم الاثنين ؛‏سيناقش ترامب مع الفريق سبل المضي قدماً في الحرب مع إيران.  ترمب يرغب في اتفاق لإنهاء الحرب لكن…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75179" target="_blank">📅 21:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-05-2026
المقر المُستَحدَث لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75178" target="_blank">📅 21:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c252d1fee.mp4?token=r8KZ_NdvofK31tbarCa0AuZyp1PuDgxk0GUdqLlG7TJHZJUJyHAvSFtKvK0-Gh8gyK1EEzpsJ-np4IpCC3cHf_1xQLFea1Rp_ZAysHEg-igCXoHnSzJi2HzvP3PcrAOdf-AKD2EhNy6dXiZO96EyZ4CC942S2wrx9qH_wHZtP5xfTJetIn4e5Tjckgy58jAihGBDaG35GgqoC8K79C11-R2mqPpjlNTLjpjVeOL9c6SlI2QfQCFZqgsvNnnKnGdRHdRoqxXKW9Yo3H5lyXv_JuDoGigEvGyeRrNTePEdz82NZ0yaUq49gfgQXapX9F5hB3ttQYH1H_U1wlMSrBuyyHBBAxYr7ctSvuJHH6xZ7chNhK4TIOBRJLOMchAKWRddvFacsLxqclxT1UVWSx9IMqdp3StXRjPWM8uR385Eux62Fx4PaKJHgg4YLAo68QfXT3yfiVFimYP9vmVn5Juw0I1q0cROkWVPqyaWnIIM8AE7WLdX2KDaUhkJqdsy63J-fhpc5h6TauMVqQyxdoWr_wJmarnCkBmUq08qRaZRu_aEFJSLsb_mWJxVFE9I37K53fwApFJAoAOzIVWuhGWdhjbLNvURVW10p2viWy4cuF3ZK8mK4SSUQ6l3Qruc8SihdtgavZYLnbsttDdEKZbzst9l3A2k5iOcZfT1VBJx8B0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c252d1fee.mp4?token=r8KZ_NdvofK31tbarCa0AuZyp1PuDgxk0GUdqLlG7TJHZJUJyHAvSFtKvK0-Gh8gyK1EEzpsJ-np4IpCC3cHf_1xQLFea1Rp_ZAysHEg-igCXoHnSzJi2HzvP3PcrAOdf-AKD2EhNy6dXiZO96EyZ4CC942S2wrx9qH_wHZtP5xfTJetIn4e5Tjckgy58jAihGBDaG35GgqoC8K79C11-R2mqPpjlNTLjpjVeOL9c6SlI2QfQCFZqgsvNnnKnGdRHdRoqxXKW9Yo3H5lyXv_JuDoGigEvGyeRrNTePEdz82NZ0yaUq49gfgQXapX9F5hB3ttQYH1H_U1wlMSrBuyyHBBAxYr7ctSvuJHH6xZ7chNhK4TIOBRJLOMchAKWRddvFacsLxqclxT1UVWSx9IMqdp3StXRjPWM8uR385Eux62Fx4PaKJHgg4YLAo68QfXT3yfiVFimYP9vmVn5Juw0I1q0cROkWVPqyaWnIIM8AE7WLdX2KDaUhkJqdsy63J-fhpc5h6TauMVqQyxdoWr_wJmarnCkBmUq08qRaZRu_aEFJSLsb_mWJxVFE9I37K53fwApFJAoAOzIVWuhGWdhjbLNvURVW10p2viWy4cuF3ZK8mK4SSUQ6l3Qruc8SihdtgavZYLnbsttDdEKZbzst9l3A2k5iOcZfT1VBJx8B0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الغيارى من أبناء الشعب البحريني يشتبكون مع عصابات آل خليفة رفضاً لقرارات إسقاط الجناسي وإعتقال رجال الدين الشيعة بتهمة دعم الجمهورية الإسلامية في حربها ضد العدو الصهيوأمريكي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75177" target="_blank">📅 20:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80335b35d0.mp4?token=WX1liKHbK7K7x2O1RGocSE65Y_XNo5kKg0kuHZzNBzyQbLP2n5axvF5_nfcDYyi0e2WOmH8uVbTTB7jXmYMggV7MSK9JymFXENMX6Xs6Jd5mGueDp09iNmodYWSajt2scp7tGDx2u3HnJTp_QWhh-7lVeyh3rQTC_wtdJAHhUxkUlFrjXs8kVKehbwuaEeHvjZCYP2rIw2-FU4DCS0mNzKxX5HyERSzVihwgJR4tDEiIEH671ThQvfR60qJ0wXdyH_wW5XCNKU049Aeob5s3hLlBqeEhitxmABgfRo5Romxxz3HMLdn8YJNMK0Ib8H4teePyftT3Ndq4IJwKDzkY9Bk1FUDkjPfyN2Ei-MaUVRaQg4N9VLNFbZNZytjYbrx7YjNUB43yLUDepHWTemUMduZ5kvdzOTV-b-opfQkpeuIrPeZsZWPf-zG3P2X7QRwixIia1xrFh9pivghBMm3oCDHOZaj3CitG2W8YatCUVyJKRWjrkt1ZG_C_7beqerj1Fwf_vlFyO0sZwUgMeu2g7ro1j3J2D8k7r_ZEz_4fF5n9NwzWCjQtGizetEhMV7VQcgIxiRdnJFYXmTh1suWtWJRzQUhGatmJMwCN67_lADuP8QoLlODzcKgqOXzWnjlAjjBI6hhYNHRjL9ZneMYEFlxAIeSBx4DDi55n0AXPTw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80335b35d0.mp4?token=WX1liKHbK7K7x2O1RGocSE65Y_XNo5kKg0kuHZzNBzyQbLP2n5axvF5_nfcDYyi0e2WOmH8uVbTTB7jXmYMggV7MSK9JymFXENMX6Xs6Jd5mGueDp09iNmodYWSajt2scp7tGDx2u3HnJTp_QWhh-7lVeyh3rQTC_wtdJAHhUxkUlFrjXs8kVKehbwuaEeHvjZCYP2rIw2-FU4DCS0mNzKxX5HyERSzVihwgJR4tDEiIEH671ThQvfR60qJ0wXdyH_wW5XCNKU049Aeob5s3hLlBqeEhitxmABgfRo5Romxxz3HMLdn8YJNMK0Ib8H4teePyftT3Ndq4IJwKDzkY9Bk1FUDkjPfyN2Ei-MaUVRaQg4N9VLNFbZNZytjYbrx7YjNUB43yLUDepHWTemUMduZ5kvdzOTV-b-opfQkpeuIrPeZsZWPf-zG3P2X7QRwixIia1xrFh9pivghBMm3oCDHOZaj3CitG2W8YatCUVyJKRWjrkt1ZG_C_7beqerj1Fwf_vlFyO0sZwUgMeu2g7ro1j3J2D8k7r_ZEz_4fF5n9NwzWCjQtGizetEhMV7VQcgIxiRdnJFYXmTh1suWtWJRzQUhGatmJMwCN67_lADuP8QoLlODzcKgqOXzWnjlAjjBI6hhYNHRjL9ZneMYEFlxAIeSBx4DDi55n0AXPTw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-05-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75176" target="_blank">📅 20:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
🇮🇷
اللجنة الأمنية العليا العراقية – الإيرانية تعقد اجتماعاً في العاصمة بغداد وتؤكد أهمية تعزيز التنسيق الأمني المشترك، وتشديد إجراءات ضبط الحدود ومنع أي عمليات تسلل أو تحركات للجماعات الإرهابية أو المسلحة التي من شأنها تهديد الأمن والاستقرار في البلدين والمنطقة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75175" target="_blank">📅 20:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
‏ترامب: الإيرانيون حاولوا إعادة بناء قدراتهم في الأسابيع الماضية.  ‏وقف إطلاق النار في إيران على أجهزة الإنعاش.  انتظرنا عدة أيام للحصول على الرد الإيراني وكان يمكن أن يكون جاهزا خلال 10 دقائق.  مقترح إيران قطعة من القمامة ولم أكمل قراءته. الحل الدبلوماسي…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75174" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇦
زيلينسكي:
نحن نستعد لهجمات جديدة، روسيا لا تنوي إنهاء الحرب.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75173" target="_blank">📅 20:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
مصدر مُقرّب من فريق التفاوض الإيراني:
خلافاً لما تدّعيه بعض وسائل الإعلام الغربية، لا يوجد في نص إيران ما يسمح لها بقبول سحب المواد النووية المخصبة.
حدّدت إيران إطارًا زمنيًا مُحدّدًا في خطتها المُقترحة لاستلام أموالها المُجمّدة. أن الولايات المتحدة نصّت في خطتها على الإفراج عن الأموال الإيرانية المُجمّدة، لكن إيران أصرّت على ضرورة الإفراج عنها خلال فترة زمنية مُحدّدة.
إن ادعاء بعض وسائل الإعلام الغربية التي تنشر أخبارًا كاذبة بأن إيران اقترحت تجميد تخصيب اليورانيوم لمدة 15 عامًا ضمن خطتها محض افتراء، وهو مجرد تضليل نفسي.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75172" target="_blank">📅 19:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21e6e3a31.mp4?token=A0f2fhQiUx53MrqTSWPERckICMND5mGvlQ1IdTxHxz8hUXmtPQftFQwu3U-l-v7M8MtonEI2xpxweKFBjMgewiNiChpxG1nR7-52epB3ZfJByTbTrrkdeXYbUT4x8ReGHUnlaMWsoAt8AW1cNtmiaRPJpQ-OCRxd4fT0NxIfsYT8CmiFEjdzfq8_inwVNF6PaV5dYUr-TqwRlafpJU8PS61aWNGIUDBRdzJBApDcklOIIceezjT9zMGKAzj-pq7T840jHaPOAsBeHrpWnI4JucXzk-nNEWFLnXaF9jOYi1AadkcssnSrUCExrHTkpMBFha2G0IUmevKQZ1TQWdHO87eexLI6Tb9dRe778h_zWuGN_HWOIlV8uY1D1VAvs_oSRlCmFWNEcrg15e4SvJBoFEQ5Q4UYUmpajr8sGImFMVVyfMKOal5I9DotKzHaN_i6Gt9lb_0ocL7u9uv7UkKPdmIXkHsHTuX2D-0Ao7a0qBkPhUckn5j9kdElfSc2Z_YzNrHm5RNnXjaJHmpqmR4kMad_NIfaFYE6z0sflFhXHf8hxdgPORMVQnv88bdNaHoAdcAXNU13CXCb4sc8rWH9Bh6XmEoAFaPLmqMLbT3ziy6MyhCS5lybK3N7rmslxfhJKAoZ9uDk3tWPnpmuoziRdRGhupzmq_pFKdWzXIlywfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21e6e3a31.mp4?token=A0f2fhQiUx53MrqTSWPERckICMND5mGvlQ1IdTxHxz8hUXmtPQftFQwu3U-l-v7M8MtonEI2xpxweKFBjMgewiNiChpxG1nR7-52epB3ZfJByTbTrrkdeXYbUT4x8ReGHUnlaMWsoAt8AW1cNtmiaRPJpQ-OCRxd4fT0NxIfsYT8CmiFEjdzfq8_inwVNF6PaV5dYUr-TqwRlafpJU8PS61aWNGIUDBRdzJBApDcklOIIceezjT9zMGKAzj-pq7T840jHaPOAsBeHrpWnI4JucXzk-nNEWFLnXaF9jOYi1AadkcssnSrUCExrHTkpMBFha2G0IUmevKQZ1TQWdHO87eexLI6Tb9dRe778h_zWuGN_HWOIlV8uY1D1VAvs_oSRlCmFWNEcrg15e4SvJBoFEQ5Q4UYUmpajr8sGImFMVVyfMKOal5I9DotKzHaN_i6Gt9lb_0ocL7u9uv7UkKPdmIXkHsHTuX2D-0Ao7a0qBkPhUckn5j9kdElfSc2Z_YzNrHm5RNnXjaJHmpqmR4kMad_NIfaFYE6z0sflFhXHf8hxdgPORMVQnv88bdNaHoAdcAXNU13CXCb4sc8rWH9Bh6XmEoAFaPLmqMLbT3ziy6MyhCS5lybK3N7rmslxfhJKAoZ9uDk3tWPnpmuoziRdRGhupzmq_pFKdWzXIlywfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إعلام العدو:
توثيق يظهر وجود عدد كبير من طائرات التزويد بالوقود الأمريكية في مطار بن غوريون.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75171" target="_blank">📅 19:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
ترامب: لدي خيبة أمل كبيرة تجاه الأكراد الذين منحناهم سلاحا ليسلموه داخل إيران لكنهم احتفظوا به.  ‏يقول الكونغرس إن الأكراد "يقاتلون بشدة". كلا، إنهم يقاتلون بشدة عندما يتقاضون رواتبهم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75170" target="_blank">📅 19:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksHaaeafhw4I9DgeiCEjtaJ5cLoFjbafWD5ko1uM0DkrbHXxixnmgECOo-32GtIpUYOB4EYiom_Vh3wqsCbM5BaT1d9g6KihltmwJd23q5y-WoC8C4IPDT54nCX3aM51puCYn-0lQ97gVhD7cvNfJVN0CfQgmf7_KN3yKcD6VRy6yR8gN1d_cHJnqdfTs9_EJwBjZO5jo97WDc0IFzthU7XXmVHuyl7MhKw5LBjZLczb8uge5ENpW6oZrqIr-7-r0Fvv_tOmiqF17h8jo-k6-9zlGfjpP3mPNu5dkFpOqQJhZNKaS6zb2fHp5JrP2__P5sxXJwp9nSQb_t1nkt_UZm_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksHaaeafhw4I9DgeiCEjtaJ5cLoFjbafWD5ko1uM0DkrbHXxixnmgECOo-32GtIpUYOB4EYiom_Vh3wqsCbM5BaT1d9g6KihltmwJd23q5y-WoC8C4IPDT54nCX3aM51puCYn-0lQ97gVhD7cvNfJVN0CfQgmf7_KN3yKcD6VRy6yR8gN1d_cHJnqdfTs9_EJwBjZO5jo97WDc0IFzthU7XXmVHuyl7MhKw5LBjZLczb8uge5ENpW6oZrqIr-7-r0Fvv_tOmiqF17h8jo-k6-9zlGfjpP3mPNu5dkFpOqQJhZNKaS6zb2fHp5JrP2__P5sxXJwp9nSQb_t1nkt_UZm_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: الإيرانيون حاولوا إعادة بناء قدراتهم في الأسابيع الماضية.  ‏وقف إطلاق النار في إيران على أجهزة الإنعاش.  انتظرنا عدة أيام للحصول على الرد الإيراني وكان يمكن أن يكون جاهزا خلال 10 دقائق.  مقترح إيران قطعة من القمامة ولم أكمل قراءته. الحل الدبلوماسي…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75169" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emgmmWHqKmOGZOiAmIaAEJ6krpEJaWY9QTC1XQLMtt3_zGlFQ6lePkM8aOK1suVDkZYenwNUc2ViSgZ22GWGQ7Mj5JyRYO9EfacweBgltyBTRYNlyyUkPyKoAOMHwy7UJjtZIZ32T1preVXuyHaPB5dR6J1RyoYy64nAn_1TUbn06k_X3rslx8G852kvZAPzwaVzisaJEDEVcHSEv4tuO4Gni4S8gfwtaiMvkdg1NW5-QR3qbWOBNlkyoKUlOKTxtGaOA2IxwJvI1HlJ-r4ppl0r7KkrT2oEWgDQa1sQKv41Hsbmcnpn3SC7SX9Wgw8wdDMUNNao1jOyWSrGHMRCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
الرئيس الإيراني مسعود بزشكيان يقدم شكره للمرجع الاعلى سماحة السيد علي السيستاني والشعب العراقي.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75168" target="_blank">📅 19:14 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8d45e7ce.mp4?token=VoQk9EWgbOpTyjQt4wnyd2kJSaHtn1CUfizPxqJe-OLRBVN2Q73pYn4Obqavh41cSA38rijzppIKnkysbzd666L61Il8l7lGh_PVm8qKj94ZwEYMVa5-hBI4DZkSIKbsqOPbJL4m-cRhyCumMPfJUPGGpTnMxuKJhvCBJVdyM1MlXIPJ3pJ5Cr_rL2cBouhBqGykUw4ZxqAbGqK7q_BgIozXtIiIJEA5OqailFspIh-HUjDkGCyGU6M7Au928fWyPXVzcSNRTsERKcIj4pbT1EtUcqEqrAu9t83ldU2dd22xpQOG3IndiF2J97HguuXxR5u63eBUbaKVI8yXApOX4JsLe27UrZbt5iDhdNj6cjKbONnaZ0G4uHXKxDU4qIynKrpwyThxUl0uZkNsDrhKDCcCAf2tky-smVgSbKS5Q9zSfo_QqkynVFRTP8cdeoV2goCgaRfzYS9VPbfSPsROPPXkulgtQ7IafY28yrcghpXzMYzP-BdRNhm284brk1LhLsVTO_95u8wuFkeUhGkYq44cuwnHbeHcn4D6rzjy1NpRxwP5mWO61xrr99xPEaOVP9A2IVdpSeEwaCLxBSK4Yw7JnHvWEav_iT2Jp7-r4JgY_ZDRMXv1uljVia7ddu8dM1fMDeEzQPQWrUazwRCn-MlOhNgfEtBP-8PrKEPCeDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8d45e7ce.mp4?token=VoQk9EWgbOpTyjQt4wnyd2kJSaHtn1CUfizPxqJe-OLRBVN2Q73pYn4Obqavh41cSA38rijzppIKnkysbzd666L61Il8l7lGh_PVm8qKj94ZwEYMVa5-hBI4DZkSIKbsqOPbJL4m-cRhyCumMPfJUPGGpTnMxuKJhvCBJVdyM1MlXIPJ3pJ5Cr_rL2cBouhBqGykUw4ZxqAbGqK7q_BgIozXtIiIJEA5OqailFspIh-HUjDkGCyGU6M7Au928fWyPXVzcSNRTsERKcIj4pbT1EtUcqEqrAu9t83ldU2dd22xpQOG3IndiF2J97HguuXxR5u63eBUbaKVI8yXApOX4JsLe27UrZbt5iDhdNj6cjKbONnaZ0G4uHXKxDU4qIynKrpwyThxUl0uZkNsDrhKDCcCAf2tky-smVgSbKS5Q9zSfo_QqkynVFRTP8cdeoV2goCgaRfzYS9VPbfSPsROPPXkulgtQ7IafY28yrcghpXzMYzP-BdRNhm284brk1LhLsVTO_95u8wuFkeUhGkYq44cuwnHbeHcn4D6rzjy1NpRxwP5mWO61xrr99xPEaOVP9A2IVdpSeEwaCLxBSK4Yw7JnHvWEav_iT2Jp7-r4JgY_ZDRMXv1uljVia7ddu8dM1fMDeEzQPQWrUazwRCn-MlOhNgfEtBP-8PrKEPCeDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: عدد السفن العسكرية الإيرانية الآن صفر.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75167" target="_blank">📅 19:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8swIklc_KlV2X0E4rJ88acY4w_yCk1dqzlfhkCxWRdwDUn2H2fP_-pTu-sjlq72I8iPF2hmTqt0aSVkMbzC9V8EQ1CBje3JrMxcNzATgOW-JnsEmdKgTy8FIKrl0LTCRPNJlkoZRK4kqmKl16Vzf212A5xwHdQLa1A_bn0nIJ5hxE5-V8hgUzKzyCTEdlbFWDHhRgclgIWqXRuiPCgC_c85tyRlXNxFrV80OuUDqJ8Z_wSs3xr1vgM03-c2wJaGG8O81mo23aj5AQAt5KU1hoEdmq5Wv_WsB6Q45doxfWsISsIsI2dxSl-aA49nQghepQumVudIJCfn9ZnHHAzeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترامب: سألتقي بمجموعة كبيرة من الجنرالات بشأن إيران.  اقتراح إيران غير مقبول ‏ولدي خطة بشأنها.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75166" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
رئيس منظمة الطاقة الذرية الإيرانية:
موضوع التكنولوجيا النووية ليس على جدول أعمال المفاوضات.
التخصيب غير قابل للتفاوض.
أنشطة صناعة الطاقة النووية في إيران سلمية وستظل سلمية.
تم اتخاذ التدابير اللازمة لحماية المراكز والأصول النووية وتطبيقها.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75165" target="_blank">📅 18:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe6bf720a.mp4?token=nN-X_JtOsns9T63uaYedGvhdjwO2eZAqAsRJOAFEypcJ-qEOLx-0mCn5Hy-nJvjvcTEijGnJ06Bv1Kbf0WwGjiZUuoLhTVQ6S77QGCnqU9YGL0fl-j-HKZTA6WQat0Eg2oKtngkDvex48wMbqxlkVkelO2RssyZd5fg1Ao-kszA7n2Jq2nsi3WoXxUeiBoWIYoASdl7h_jr1ERZyMLxgZDK6ubBoEcQNPu4LieB5p4dWOe21oNmLH-Rv91auAgZk0jVbR39S-uxBNIqyO5uS9o7LK7eXIBO9KDwqcggKRGJBpsL5uTXjqpc-QoceOpwCSPmA4p7nOFX93PGPCjxHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe6bf720a.mp4?token=nN-X_JtOsns9T63uaYedGvhdjwO2eZAqAsRJOAFEypcJ-qEOLx-0mCn5Hy-nJvjvcTEijGnJ06Bv1Kbf0WwGjiZUuoLhTVQ6S77QGCnqU9YGL0fl-j-HKZTA6WQat0Eg2oKtngkDvex48wMbqxlkVkelO2RssyZd5fg1Ao-kszA7n2Jq2nsi3WoXxUeiBoWIYoASdl7h_jr1ERZyMLxgZDK6ubBoEcQNPu4LieB5p4dWOe21oNmLH-Rv91auAgZk0jVbR39S-uxBNIqyO5uS9o7LK7eXIBO9KDwqcggKRGJBpsL5uTXjqpc-QoceOpwCSPmA4p7nOFX93PGPCjxHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: سنتعامل مع إيران حتى يتم التوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75164" target="_blank">📅 18:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏴‍☠️
صحيفة "معاريف" العبرية:
حاول حزب الله إسقاط طائرة مقاتلة تابعة لسلاح الجو الإسرائيلي في لبنان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75163" target="_blank">📅 18:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
أ.ب عن مصدر دبلوماسي:
إسلام آباد تحاول ترتيب مذكرة تفاهم لإنهاء الحرب وفتح طريق حوار أوسع بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75162" target="_blank">📅 18:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏ترامب: قادة إيران المتشددون سيستسلمون.  نومة العصر وما تفعل
😄</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75161" target="_blank">📅 18:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75160">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامب: أدرس استئناف مشروع الحرية ولكن بنطاق أوسع لا يقتصر فقط على مرافقة السفن عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75160" target="_blank">📅 18:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75159">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترفيهي
🇺🇸
‏ترامب: إيران قالت إن على الولايات المتحدة إزالة الغبار النووي.  لا نعرف حاليا كيف يمكننا دخول إيران للمضي بإزالة الغبار النووي وسنترك ذلك لمزيد من المفاوضات.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75159" target="_blank">📅 18:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75158">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جيش العدو: أُصيبت آليتان هندسيتان الساعات الأخيرة في جنوب لبنان نتيجة إصابتهما بمحلّقات تابعة لحزب الله. ولم تقع إصابات في صفوف المقاتلين، لكن الآليتين تعرضتا لأضرار، وكانتا تعملان داخل منطقة جنوب لبنان في مهام هندسية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75158" target="_blank">📅 18:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75157">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترفيهي
🇺🇸
‏
ترامب:
إيران قالت إن على الولايات المتحدة إزالة الغبار النووي.
لا نعرف حاليا كيف يمكننا دخول إيران للمضي بإزالة الغبار النووي وسنترك ذلك لمزيد من المفاوضات.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75157" target="_blank">📅 18:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75156">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1955de21.mp4?token=luNdR7TfYasupdtcT5USaQONYbZSlNr4rFjPT2vHONDk8p4fCST7m53cOOwdB2dNv9zElw83GYpwmXr65e4zRTp0HN6DqXUJNbbiS8WGXok9HNPJZQhZJfjoOgcvdCEiTxjC-x4-fj10NgL4h2ikZR3DkLeVMjdmseMSJpVScpv7xtWWCFO6mIWf3HdAc6uIL7WQyugIUQEoHF6-RGuiU0swHHqpQcJg9DlxEWGd7AADQQ8DZVvAB3MgshHTf7Nd43M8TEUunYqCuiryT6b-7Qe4_-P8XN9ALFMUU95YhgQNZv4DKs-T1lNtIkQQh6uQxo2AOu9mCXkaww6o5zpp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1955de21.mp4?token=luNdR7TfYasupdtcT5USaQONYbZSlNr4rFjPT2vHONDk8p4fCST7m53cOOwdB2dNv9zElw83GYpwmXr65e4zRTp0HN6DqXUJNbbiS8WGXok9HNPJZQhZJfjoOgcvdCEiTxjC-x4-fj10NgL4h2ikZR3DkLeVMjdmseMSJpVScpv7xtWWCFO6mIWf3HdAc6uIL7WQyugIUQEoHF6-RGuiU0swHHqpQcJg9DlxEWGd7AADQQ8DZVvAB3MgshHTf7Nd43M8TEUunYqCuiryT6b-7Qe4_-P8XN9ALFMUU95YhgQNZv4DKs-T1lNtIkQQh6uQxo2AOu9mCXkaww6o5zpp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام العدو:
حزب الله يوجه أوامر إخلاء لمستوطني "كريات شمونة" عبر أسطوانة اتصالات هاتفية تلقائية، تتضمن عبارات:
"مرحباً، أخلوا المستوطنة، هي لنا، عندما نصل سنقرر إذا أنتم أسرى أو قتلى"، مع ضحكات في نهاية المكالمة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75156" target="_blank">📅 17:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75155">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
وول ستريت جورنال:
تتفاقم أزمة الطاقة في كاليفورنيا اذ بلغ متوسط سعر البنزين 6.16 دولاراً للغالون وهو الأعلى في الولايات المتحدة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75155" target="_blank">📅 17:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75154">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مدير وكالة الطاقة الدولية: سمعة مضيق هرمز بوصفه ممرا موثوقا لتجارة الطاقة تضررت بشكل دائم</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75154" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75153">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 10-05-2026 جرّافة تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75153" target="_blank">📅 17:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75152">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
ذي أتلانتك عن مسؤول أوروبي:
عدم القدرة على التنبؤ بقرارات ترمب يضطرنا للتفكير بمستقبل أقل اعتمادا على واشنطن</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75152" target="_blank">📅 17:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75151">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjX8Kw3mfs5Wa2G9sbCJ8uFgykcZlls7cFP5iGgiae3I7upITUOnjU9eDg6CfJMt3xOQ-9bDkSyFEL1-QOvnbitdCzMM4KuEKUveTdKQbxA9Owq6-boq7Edyjz50BWYMxn8lE42I6hgz534-baRxpeN2d1m5222oMzo1_uVhGSe74PZhRF5k21PJE8sPh0Om1eY_iEUFDOIqLBVR2oHBWKBTO-Giy9Y3DdTo9AdeUV1ahkzSeyThCxvsfUjHQ4VhFkgQ6PfDgrBpnVpiCtnbQwrqTpSEL-_moPm7_aa5xqvY1sL3C8-73GF0S75EQkAnU6vziyES4KWrfepF5bQPAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
وزير الخارجية الفرنسي يرحب بالعقوبات الجديدة على الاسرائيليين:
"لقد تم ذلك! الاتحاد الأوروبي يفرض اليوم عقوبات على المنظمات الإسرائيلية الرئيسية المسؤولة عن دعم الاستيطان المتطرف والعنيف في الضفة الغربية، وكذلك على قادتهم. يجب أن تتوقف هذه الأفعال الخطيرة وغير المقبولة فوراً".</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75151" target="_blank">📅 17:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75150">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🫡
الموافقة على رفع حجب البطاقة التموينية عن منتسبي القوات الأمنية العراقية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75150" target="_blank">📅 16:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75149">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtUacyOn9a3tuUVjaV8F-3yf4K58gzh4ZcpQDHF2inLY7e9UgVI9wpXtw7Awme_NXrUeeK7RRowTfNXfsaoJf0X_S4_hQdj5XvYuFPD3h4W6BLYVOP3JqvQ1YiubnIBr5SJsYoH8WFDwe8EBBEklzgrkbngdEozzof6eE6rHq3W5c0bGGLtJU0yylhjZXnsa0djB2uqh6AcxXTIYuafXnSLULqqbD8Ys40ciE5qWoucqwTW1qVzx9g_SAeHq3_lNRSQXZ5cXDGw8918elO7yStyIl6t4uTvCZFBn2SxKJXBcJlVOIUN5iQwz46Ydygliwe7Cdxobl_EHSwjfdgFzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الطيران التجسسي الأمريكي لا يزال يؤمن غطاء جوي لموقع القاعدة الاسرائيلية في صحراء النخيب بمعدل ٢٤ ساعة … علما ان حتى اللحظة لا تستطيع اي قوة برية عراقية الوصول للمكان …
😆
فقط تخيلوا ان رئيس الوزراء كان الكاظمي وليس من الإطار ماذا كان حدث إعلاميا</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75149" target="_blank">📅 16:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75148">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3263d2ea6.mp4?token=hAQ6Lf1EuAQERRUoiNkcJAFGikwZkxkLmT0_mRarSnL3KZgNPhSauanOKvFRGG1iijr3GcKAg4c3td3UjhmKLulDrUZko1u4u1_DZ9daRbBlAcMbO_46JB06w8t_yOBn420cLnUR5hatKlCiuQgqQ8565en4b_6z9ml9lJFoO6-H1r5J366VeobQBxKyEWj6Gx--vHSu_Lq0sJAMJ7_cdw4CuZXjis6icvF6vMpxwZ5Gn6GcvcfcKchILvMfNLBNn45wG90yWV9U4Rkj4QWoYIlOHwxC2_UnBa9vsmhCGydjsiAkoA4nNcUr2wkCXRpMGg8I1da3k0YLC12QmqrLeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3263d2ea6.mp4?token=hAQ6Lf1EuAQERRUoiNkcJAFGikwZkxkLmT0_mRarSnL3KZgNPhSauanOKvFRGG1iijr3GcKAg4c3td3UjhmKLulDrUZko1u4u1_DZ9daRbBlAcMbO_46JB06w8t_yOBn420cLnUR5hatKlCiuQgqQ8565en4b_6z9ml9lJFoO6-H1r5J366VeobQBxKyEWj6Gx--vHSu_Lq0sJAMJ7_cdw4CuZXjis6icvF6vMpxwZ5Gn6GcvcfcKchILvMfNLBNn45wG90yWV9U4Rkj4QWoYIlOHwxC2_UnBa9vsmhCGydjsiAkoA4nNcUr2wkCXRpMGg8I1da3k0YLC12QmqrLeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل 4 اشخاص واصابة اخرين من عصابات الجولاني في الحسكة بعد فتح النار من قبل تنظيم داعش على باص لهم</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75148" target="_blank">📅 16:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75147">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم لحزب الله</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75147" target="_blank">📅 16:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75146">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBpaUDdgcyza6dEnzJq6ttTmfqBKZ1TZxmfizIxF3z-xvf5F-Rw9y3XWb_aNEvq4aHFeSfyLHiGJyhM9f_rmet5aUE_WcHuJj9XNeRTABfJw93IYTiZTiQSD50pfUvAaKCQkx0lfsPbeE2wSsZBE3uNzHfHPWFuuQ57faMRdgFYHQHZNjfBZfMkNXSG7wuMyeT6q5hvNz0uvMnxfSpYqNIlsVF0rtUf4x87-eECWCNPKT-sqWi0kCysQhNkb7-B11ga5Hesm7k-7b9dSHM36kVYb77iT6XLRaxTlqeARwIMR9AnW7ST-9dHuV55yE5aKRnrSMrBa4s1DjyZq8y12Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرقيب أول احتياط في الجيش الصهيوني إيتان هود بامس الحاجة الى دعائكم بعدما خضع لعملية بتر ساقه على اثر عملية لحزب الله وقعت قرب قرية الناقورة في جنوب لبنان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75146" target="_blank">📅 15:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75145">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
لجنة الأمن القومي والسياسة الخارجية الايرانية: البحرين والإمارات لا تزالان تسيران في الطريق الخطأ.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75145" target="_blank">📅 15:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75144">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زعيم المعارضة الإسرائيلية يائير لابيد يدعو لحل الكنيست الأسبوع المقبل والتوجه نحو انتخابات</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75144" target="_blank">📅 15:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75143">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
لجنة الأمن القومي والسياسة الخارجية الايرانية:
البحرين والإمارات لا تزالان تسيران في الطريق الخطأ.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75143" target="_blank">📅 15:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75142">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 07-05-2026 آليات تابعة لجيش العدو الإسرائيلي أثناء محاولتها التقدم باتجاه بلدة بيوت السيّاد جنوبي لبنان بالأسلحة المناسبة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75142" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75141">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اعلام العدو:
شبكة وضعها المقاتلون ضد الطائرات المسيّرة تسببت في تعطل مروحية الليلة الماضية في جنوب لبنان. هذا الصباح تم تخليص المروحية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75141" target="_blank">📅 14:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75140">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
🇮🇶
وزارة الخارجية الايرانية:
التقارير المتعلقة بإنشاء الكيان الصهيوني قاعدة عسكرية سرية داخل الأراضي العراقية سيتم طرحها مع بغداد، ما هو واضح من سجل سلوك الكيان الصهيوني في المنطقة أنه لا يلتزم بأي حدود أو خطوط حمراء عندما يتعلق الأمر بضرب دول المنطقة أو إثارة الخلاف بينها أو الإضرار بمصالح الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75140" target="_blank">📅 14:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75139">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">10 نقاط استراتيجية لقائد الثورة الإسلامية بشأن الخليج الفارسي ومضيق هرمز
✏️
انتصار إيران في الخليج الفارسي… ملامح نظام إقليمي جديد
▪️
1. حضور الأجانب الأمريكيين وتموضعهم في منطقة الخليج الفارسي هو العامل الأهم لانعدام الأمن في المنطقة
▪️
2. عجز القواعد الأمريكية الهشة عن تأمين أمنها الذاتي
▪️
3. المستقبل المشرق لمنطقة الخليج الفارسي، بلا أمريكا وفي خدمة تقدّم شعوب المنطقة ورخائها ورفاهها
▪️
4. «المصير المشترك» مع جيراننا في الخليج الفارسي وبحر عُمان
▪️
5. لا مكان للغرباء الأشرار في الخليج الفارسي إلّا في قاع مياهه
▪️
6. سلسلة انتصارات إيران الإسلامية في الخليج الفارسي تمثّل ملامح نظام جديد للمنطقة والعالم
▪️
7. تأمين منطقة الخليج الفارسي عبر الشكر العملي لنعمة ممارسة إيران إدارتها على مضيق هرمز
▪️
8. طي بساط استغلال العدو المعتدي لمضيق هرمز
▪️
9. تحقيق الرخاء لشعوب المنطقة وتقدّمها عبر القواعد القانونية والإدارة الجديدة لمضيق هرمز
▪️
10. إدخال السرور إلى قلوب الشعب الإيراني عبر المكاسب الاقتصادية الناتجة عن الإدارة الجديدة لمضيق هرمز</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75139" target="_blank">📅 13:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75138">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879afac6ef.mp4?token=foVZT320GCugShesVhEZejiemcvIQ_3Bsvd5l5O_JL3QhLRgyKgiy_8XgHgAPPkaa00PNu5bYUyeikeosr5dhwoOPc6BBGnRFPhh8jFC9iRamSqyzRupRcoNdFOu2w4C65hLbXOeGF_Xvk49vXEgl5l60CfEsL6aILJI-GCIBXeClHwZfEYbABHlpXtY2pT8iNTKjdmQZsFTYjjUMhgbHB8Mv1cf5efNeJjRP6ROW0OVGkh3HtrYHN0rhWac3I7rafYWLU-c1H8FOQ0cL4XeqrAwe6RkH3oggZFUSt3HopYYcbB4Le1bNXi0Gi3RSBqtNLanX2rV0QJqz8lHDobjdT81yHFSTc-dcutlidgS52pDBaSanOwygFEC_ESxE09II5BN8subknq9h8m07iGx5XJp2O-iMcsugKVNLzWPfSK4rZ2l9YHXVV-CSkSHqSfd4DX4GfqUutvhqRL32VJOD12Rse_G7tTNQ8Xyc5G5cWjIvEDBeTSGKlWJIoRPHKKNE4y6S_imYHjfS3U_h6DOqv6kwDkOAJ-4r2EYfMYQjZwyA8MRSRQ2QY3uoY_lXQdnWR09Jk0aDlYzEWZkBWZPy8pXxHz54jXhzaFeYAXgWDih5qsImVC56f8b11ykJZwQ5rTTYwA1X5ixGhJgbcRpSwjcdGg6rwYwzvldEsBoHao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879afac6ef.mp4?token=foVZT320GCugShesVhEZejiemcvIQ_3Bsvd5l5O_JL3QhLRgyKgiy_8XgHgAPPkaa00PNu5bYUyeikeosr5dhwoOPc6BBGnRFPhh8jFC9iRamSqyzRupRcoNdFOu2w4C65hLbXOeGF_Xvk49vXEgl5l60CfEsL6aILJI-GCIBXeClHwZfEYbABHlpXtY2pT8iNTKjdmQZsFTYjjUMhgbHB8Mv1cf5efNeJjRP6ROW0OVGkh3HtrYHN0rhWac3I7rafYWLU-c1H8FOQ0cL4XeqrAwe6RkH3oggZFUSt3HopYYcbB4Le1bNXi0Gi3RSBqtNLanX2rV0QJqz8lHDobjdT81yHFSTc-dcutlidgS52pDBaSanOwygFEC_ESxE09II5BN8subknq9h8m07iGx5XJp2O-iMcsugKVNLzWPfSK4rZ2l9YHXVV-CSkSHqSfd4DX4GfqUutvhqRL32VJOD12Rse_G7tTNQ8Xyc5G5cWjIvEDBeTSGKlWJIoRPHKKNE4y6S_imYHjfS3U_h6DOqv6kwDkOAJ-4r2EYfMYQjZwyA8MRSRQ2QY3uoY_lXQdnWR09Jk0aDlYzEWZkBWZPy8pXxHz54jXhzaFeYAXgWDih5qsImVC56f8b11ykJZwQ5rTTYwA1X5ixGhJgbcRpSwjcdGg6rwYwzvldEsBoHao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-05-2026 دبّابة آمر سرية مدرعات في جيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75138" target="_blank">📅 13:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75137">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">أبو عائشة الشيباني: في سوريا ليس لدينا أقليات
😆
نعم الجميع مجبرين أن يكونو من آل أمية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75137" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75136">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جيش الاحتلال: إصابة 3 جنود صهاينة جراء سقوط مسيّرة مفخخة جنوبي لبنان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75136" target="_blank">📅 12:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75135">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6e3e0d14.mp4?token=lU5goTrlQHRssMv_TWf8G1OYrex0k_CB8rtPnqt-LNQ626FSNXfJj5hLOO3CCJufkzIjVW3bccgzLh1XwWXYb-lyV_DAlk46xaomPu1t1X8p39KKdQTjGoKy2xRNsOQcw0RIuo9jTlM3G_UII6-3AkM8FknCNwxaATqZX69BCOQPKY9WIXDFzJz02lU2ZnKuUOiwE_I08l3kbinB1FH7i2vN2U1uCkEUAVr8SIXTXsL198gMjP4WaxE_qJark_w2WjNUGdcdUHxTjldU4w71Va0DgRjYjR1_pbVk0R8ywNVDh5p3_MkdSfLoTydVIPMIolcw_pvSK5Y0M7cp8aaJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6e3e0d14.mp4?token=lU5goTrlQHRssMv_TWf8G1OYrex0k_CB8rtPnqt-LNQ626FSNXfJj5hLOO3CCJufkzIjVW3bccgzLh1XwWXYb-lyV_DAlk46xaomPu1t1X8p39KKdQTjGoKy2xRNsOQcw0RIuo9jTlM3G_UII6-3AkM8FknCNwxaATqZX69BCOQPKY9WIXDFzJz02lU2ZnKuUOiwE_I08l3kbinB1FH7i2vN2U1uCkEUAVr8SIXTXsL198gMjP4WaxE_qJark_w2WjNUGdcdUHxTjldU4w71Va0DgRjYjR1_pbVk0R8ywNVDh5p3_MkdSfLoTydVIPMIolcw_pvSK5Y0M7cp8aaJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتراق دبابة صهيونية بعد استهدافها من قبل المقاومة في بلدة شمع جنوب لبنان</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75135" target="_blank">📅 12:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75134">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzSwjNgcwUqYJLQUJQZULvyailzT7HVDHPfo5yaSqfo-VlYZumVQTfUh9CAKa6cuXjLBEZq_bm5nbHH4iGmYflD2ZxZrsC_jHkd3baE0R-mCfn4qtxkiXVbv0t7-zhQ3cXDQNtHuDcVDNRnLEBBd-XF7gdMGL-TenV7sJ6u8NXFy0PTVGmozilMc0x9y7cH0r6ibtQ16-kXMMZH_vRl3U8WR8Tlb_y0K7soUKaybtlTq3x-DU02pzw5WhhfY3wGmb1s5ALWf1e9X5V-YKmmMXDV5eaDcpT0HGdPwP_Mpi5fFti2nj2XkTref5rWia_QD5brurRxN7ooOUc1mcnFPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
🇮🇶
إحدى نتائج إعادة ترتيب شبكة اللوبي والعلاقات العامة التي قام بها بافل و قوباد طالباني خلال الأشهر الأخيرة بدأت تظهر بوضوح: ترامب أعاد نشر مقابلة لقوباد طالباني يمدحه فيها. واللافت أن قوباد وبافل تبنيا الخطاب نفسه تقريبا، القائم على إطراء ترامب بصورة كبيرة وتقديمه بوصفه “رجل صفقات” قادرا على رعاية تسوية سلمية وإنهاء الحرب. وكما أشرنا سابقا، لم يقتصر تحرك الطالبانيين على التعاقد مع شركة اللوبي الكبرى Ballard Partners، بل شمل أيضا الاستعانة بخبراء متمرسين في العلاقات العامة لتحسين صورتهم وتعزيز حضورهم في واشنطن ولندن. يذكر ان بافل احد ابرز الحلفاء للإطار التنسيقي العراقي المدعوم من ايران !!!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75134" target="_blank">📅 11:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75133">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a336f4b19.mp4?token=sPkuMS_SbVi4lHmtas6Ys42eZiQyXPr7KukPoEhayPdVVKjQT9XqF6z1nVmN9t_u9T8lker2WcCOMNvh7WDlcpySMiiGLw_n86aXmxyv1WdpIUpNu8cH_geBXh8fttIxZw6OvACHAqMPo38afd6iZowIe4OVaqzESaxw1Gx1MRYdd55RAbA-nPMInTtQX_sahFZJjYw5oaxbo7wduAczluHEr01Uxf6_-N1E7c9cUOEXT_Wx_ArG5TzPeP8KZ9cbrZKYjiiHH2LD5dvB0h6c1nM-6KNHA5lwPSPbmLW4QEQXDMD4JBGJScEwWyO38Zahlj6oCj6eQS4k5kMF09UjbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a336f4b19.mp4?token=sPkuMS_SbVi4lHmtas6Ys42eZiQyXPr7KukPoEhayPdVVKjQT9XqF6z1nVmN9t_u9T8lker2WcCOMNvh7WDlcpySMiiGLw_n86aXmxyv1WdpIUpNu8cH_geBXh8fttIxZw6OvACHAqMPo38afd6iZowIe4OVaqzESaxw1Gx1MRYdd55RAbA-nPMInTtQX_sahFZJjYw5oaxbo7wduAczluHEr01Uxf6_-N1E7c9cUOEXT_Wx_ArG5TzPeP8KZ9cbrZKYjiiHH2LD5dvB0h6c1nM-6KNHA5lwPSPbmLW4QEQXDMD4JBGJScEwWyO38Zahlj6oCj6eQS4k5kMF09UjbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استشهاد شاب بعد اشتباك مسلح مع قوة من جيش الاحتلال في مخيم قلنديا شمال القدس المحتلة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75133" target="_blank">📅 10:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75132">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: ردنا على الجانب الأمريكي تتضمن مطالب معقولة ومنطقية وتأخذ مصالح المنطقة كلها في الاعتبار
الصين حليف استراتيجي</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75132" target="_blank">📅 10:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75131">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
رئيس أركان جيش الاحتلال:
"الجيش الإسرائيلي يحتاج إلى مزيد من الجنود فورًا."
الخسائر والإصابات التي يتكبدها الجيش “الإسرائيلي” في لبنان حاليًا ليست مقبولة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75131" target="_blank">📅 10:47 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
