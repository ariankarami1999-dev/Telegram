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
<img src="https://cdn4.telesco.pe/file/SxWGQ8aUqoXq7GWuNQ2FH0uR8mtAS546-6l3pTqyYUBIZHuaWFl4s93Hdgkb7Qsrb4XHoFvJt8H5i08BmQf-Qad4pH59szfkmJL3V0eqajM60J8bkFjIGoTVOE6fCXDGWBm_nVCFeOXqdcnelu3FbiMhNlNLe5UeldiIGNajx_PkpgPS2w8S2csFRYU8OTBYM0Co-lAM3Q2i5U94ta21flDGBL9azlq_F63gzGpqzIYZpJXZ-0ezZtr_jyQ3LEXY2HQAi1F3TEdHXl1MxJySM4bkYaWYkqClPHSyxouJyGK-tGaaxkpDrSHrCS3eAiIxjPkUX7iNei6nQkhcjvSZ_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اطلاق</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/77634" target="_blank">📅 09:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">المتحدث باسم الحرس الثورة الإيراني: للمرة الألف، أثبتنا أن السماء فوق الأراضي المحتلة والمنطقة تخضع لإرادتنا وتحت سيطرة صواريخ الحرس الثوري الإيراني المدمرة للمجال الجوي.</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/naya_foriraq/77633" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏تعليق جميع الرحلات في طهران حتى إشعار آخر</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/naya_foriraq/77632" target="_blank">📅 09:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">القوات المسلحة اليمنية:  في إطارِ التصدي للعدوانِ الأمريكيِّ والصهيونيِّ على محورِ الجهادِ والمقاومةِ في إيرانَ وفلسطينَ ولبنانَ والعراقِ واليمنِ، ورفضاً للمشروعِ الصهيونيِّ الساعي لإقامةِ إسرائيلَ الكبرى تحتَ مسمى الشرقِ الأوسطِ الجديدِ، وسعياً منا إلى كسرِ…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/naya_foriraq/77631" target="_blank">📅 09:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">القوات المسلحة اليمنية:  في إطارِ التصدي للعدوانِ الأمريكيِّ والصهيونيِّ على محورِ الجهادِ والمقاومةِ في إيرانَ وفلسطينَ ولبنانَ والعراقِ واليمنِ، ورفضاً للمشروعِ الصهيونيِّ الساعي لإقامةِ إسرائيلَ الكبرى تحتَ مسمى الشرقِ الأوسطِ الجديدِ، وسعياً منا إلى كسرِ…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/naya_foriraq/77630" target="_blank">📅 09:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/77629" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/naya_foriraq/77629" target="_blank">📅 09:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f0389b66.mp4?token=na5XQtgoIoesITo_hGqIRXOWOoeGZHirAyOTdgGWZ9zWKXC_UITZpIi762pSizONcmHWU1PuJ7BVF5ccGotj2KEgkg5cJqNjM4y1tGN6h68UsFYfLE_sL7Ju0k1aagrRB54UL5AIa5n2lgn8GEvyPG-Pq6f0ANOrTlmrK1hQ7tMPawfX-h3_3i2vjYZi7pJ3xohzwrMOt_uMWIhxJZmO-mb-x4u-GA0FYcNIQnXVVurTqWhdJ4-Y8RwbSV10hiiD8BLk4fILb9rk6msdVNaw7NBPWJuDbOfOsAPJbINs_8CxO0h7cCKOR9af0FUWQJWpS6Ak4KZoMeLXsz59xQ0vMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f0389b66.mp4?token=na5XQtgoIoesITo_hGqIRXOWOoeGZHirAyOTdgGWZ9zWKXC_UITZpIi762pSizONcmHWU1PuJ7BVF5ccGotj2KEgkg5cJqNjM4y1tGN6h68UsFYfLE_sL7Ju0k1aagrRB54UL5AIa5n2lgn8GEvyPG-Pq6f0ANOrTlmrK1hQ7tMPawfX-h3_3i2vjYZi7pJ3xohzwrMOt_uMWIhxJZmO-mb-x4u-GA0FYcNIQnXVVurTqWhdJ4-Y8RwbSV10hiiD8BLk4fILb9rk6msdVNaw7NBPWJuDbOfOsAPJbINs_8CxO0h7cCKOR9af0FUWQJWpS6Ak4KZoMeLXsz59xQ0vMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اليمن سيَسرق أمانكم ، يا صهاينة.</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/77628" target="_blank">📅 09:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77627">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">القوات المسلحة اليمنية:  في إطارِ التصدي للعدوانِ الأمريكيِّ والصهيونيِّ على محورِ الجهادِ والمقاومةِ في إيرانَ وفلسطينَ ولبنانَ والعراقِ واليمنِ، ورفضاً للمشروعِ الصهيونيِّ الساعي لإقامةِ إسرائيلَ الكبرى تحتَ مسمى الشرقِ الأوسطِ الجديدِ، وسعياً منا إلى كسرِ…</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/naya_foriraq/77627" target="_blank">📅 09:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">القوات المسلحة اليمنية:
في إطارِ التصدي للعدوانِ الأمريكيِّ والصهيونيِّ على محورِ الجهادِ والمقاومةِ في إيرانَ وفلسطينَ ولبنانَ والعراقِ واليمنِ، ورفضاً للمشروعِ الصهيونيِّ الساعي لإقامةِ إسرائيلَ الكبرى تحتَ مسمى الشرقِ الأوسطِ الجديدِ، وسعياً منا إلى كسرِ الحصارِ الظالمِ والغاشمِ الذي يفرضُهُ العدوُّ الأمريكيُّ على شعبِنا وشعوبِ المحورِ الحرةِ والعزيزةِ في لبنانَ وغزةَ وإيرانَ، وفي إطارِ مبدإِ وحدةِ الساحاتِ ومواجهةِ الأعداءِ، ورداً على العدوانِ الصهيونيِّ على لبنانَ وإيرانَ وغزة، قامتِ القواتُ المسلحةُ اليمنيةُ بإطلاقِ دفعةٍ صاروخيةٍ استهدفت أهدافاً حساسةً للعدو الإسرائيليِّ في منطقةِ يافا المحتلةِ وقد حققت أهدافَها بدقةٍ بفضلِ الله.
وفي هذا السياقِ تؤكدُ القواتُ المسلحةُ على الآتيِ:
أولاً: نعلنُ حظرَ الملاحةِ البحريةِ بشكلٍ كاملٍ وتامٍّ على العدوِّ الإسرائيليِّ في البحرِ الأحمرِ، ونعتبرُ أنَّ كلَّ تحركاتِ العدوِّ أصبحتْ هدفاً عسكرياً لقواتِنا المسلحةِ من لحظةِ إعلانِ هذا البيانِ.
ثانياً: نؤكدُ أنَّنا سنواجهُ التصعيدَ بالتصعيدِ، وإنَّ عملياتِنا العسكريةَ ستكونُ متصاعدةً بما يواكبُ الأحداثَ والمعركةَ والاشتراكَ مع محورِ الجهادِ والمقاومةِ.
ثالثاً: نؤكدُ على حقِّ شعبِنا وشعوبِ أمتِنا الحرةِ في مواجهةِ العدوانِ الأمريكيِّ الإسرائيليِّ، وأنَّنا لنْ نقفَ مكتوفي الأيدي أمامَ الحصارِ الظالمِ على شعبِنا وشعوبِ محورِ الجهادِ والمقاومةِ في فلسطينَ وغزةَ وإيرانَ ولبنانَ والعراقِ، وإنَّ كلَّ محاولاتِ العدوِّ ستبوءُ بالفشلِ بإذنِ اللهِ، وإنَّ عملياتِنا مستمرةٌ طالما استمرَّ العدوانُ والحصارُ علينا وعلى محورِ الجهادِ والمقاومةِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
﻿</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/naya_foriraq/77626" target="_blank">📅 09:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تفعيل الدفاعات الجوية في كرمانشاه</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/77625" target="_blank">📅 09:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏إذاعة الجيش الإسرائيلي: استمرار تبادل الضربات مع إيران متوقع لعدة أيام</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77624" target="_blank">📅 09:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حدث أمني جنوب القدس المحتلة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77623" target="_blank">📅 09:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حدث أمني جنوب القدس المحتلة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77622" target="_blank">📅 09:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تصاعد الدخان من مصنع كارون في ماهشهر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/77621" target="_blank">📅 08:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">إلغاء كافة الأنشطة والتجمعات وإغلاق المؤسسات التعليمية في جميع أرجاء الكيان الصهيوني</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77620" target="_blank">📅 08:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تفعيل الدفاعات الجوية في كرمانشاه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77619" target="_blank">📅 08:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هيئة البث الإسرائيلية: انتقال مستشفى سوروكا بالنقب للعمل داخل الأماكن المحصنة لاستقبال حالات الطوارئ فقط</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77618" target="_blank">📅 08:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية خلال الساعات القادمة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77617" target="_blank">📅 08:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKyatQS-LzvZ5K_gtjIjyii-LowoZ5fPtP6gt8fWzb722JFVph_llf2wI5fzET7QI4n-FoYf9TC5hIT6mBmx1xcig6nqWsg4c0gj4SO25QL3E1sbCqpnvQKSyvrnYyzFu9z2iRG6Ycwga6yLEr3_1cC6woToDnAhcOhlnK_D2rgPpYC_D4P6vaAxoO1JWbDEKRkAoDlB7vBGlii2ENe0h0tybVVeCYJ3XOqzDZY9Hg5LFAZ3OwLqQJvBg8r-MiLQ8hWU6KoKdKetTMmEvD6zQUE0fDCpLjHWF-RIEGZA0iIGPQBy6dX9FEmUG_ZnLmS-vPdjrPCrtkMdACi2X3JW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrQAjRCBUi6SQayZrnuGMOvTCcYvpEFVnpz5ygNIs4EqNVtbrSEnvjVXr2xV7t0yFEO-t9EHdHDpAE0AF5ZIQ7AyrrPhauHk9bpiYOBhLIOtN8BNSRs7PUgoW25rJD9n5OgRoD0JEYefDb3uZ91eV0HNcaNBy2My2YaftnTQpbS-y3fC6kaDsv8QNWUinHOiFOtn_Ho97vNe95-YRgor_KPUC80PHhML0lPGFo-kMIpOCvL_9F4iqScp_aXyzjB2ydNRGMGHAH6trL0URAp-oZy54klBZUTt21FjsuvTcc9ym_QdgdKqzwjbenCr3HISk1uFWX6XMF2xxvih-9RYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtDACLMFvilSbGJ1tcvRSapwpgOOYwESBB0jnLKiF54Mq67Ha11RcuMLu4bL7mil3J2ZC92kyt-yyUbMKqUOgLknfWH7Od0e84K_KhKLGt3hfA1yUD9UeY3-G9AxRbLOScIB7yFH32-tF0gG17PDG37N8nE92Yk7BUQry2s3cX7iKU89X9haGs6ZgWqNQlwIjJMLui9Nh1oyOWWnZAqN0FPYC-1jexOFHTTpV_3ixnkfWvrq5D808yF7cK3KxCVqC32n-_cG7B4TGsRNETAtFUgBRZMSjqCZboeKztONFlwvQp0etgCwf12vxnWLayQOSvbVLjoeNlyomgz06Txuig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إعلام العدو: بدأت مستشفيات الشمال بنقل أقسام الطوارئ إلى الملاجئ المحمية تحت الأرض رمبام حيفا/زيف صفد/ مركز الجليل نهاريا/مستشفى الوادي العفولة/ مستشفى مائير كفار سابا.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77614" target="_blank">📅 08:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">إعلام العدو: الجبهة الداخلية تطلب فرض قيود جديدة في مطار بن غوريون شرق تل أبيب</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77613" target="_blank">📅 08:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">إدارة العلاقات العامة بالحرس الثوري الإيراني:
بتوكل على الله تعالى واستعانة به، أطلق مقاتلو القوات الجوية التابعة للحرس الثوري الإيراني، قبل دقائق، عملية نصر بالرمز المقدس "يا حيدر كرار"، وهدية لشهداء حرب الأيام الاثني عشر، مستهدفين المراكز الحيوية لقاعدتي نواتيم وتل نوف الجويتين الاستراتيجيتين.
جاءت هذه العملية ردًا على العدوان الصاروخي للكيان الصهيوني القاتل للأطفال على عدة مواقع رادار في ثلاثة مناطق من البلاد.
تميزت سرعة الاستجابة لعدوان جيش الكيان الصهيوني وتوسيع نطاق الأهداف التي استهدفتها المجموعات العاملة في هذه المرحلة.
جميع الوحدات القتالية والعملياتية للحرس الثوري على أهبة الاستعداد لتنفيذ عمليات استقصائية واسعة النطاق على جميع الجبهات، وقد أعدت خطط عمل تتناسب مع سيناريوهات العدو.
والنصر من عند الله العلي القدير الحكيم.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77612" target="_blank">📅 08:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">إخلاء جنود إسرائيليين مصابين من جنوب لبنان اثر تعرضهم لحدث أمني على أيدي رجال حزب الله.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77611" target="_blank">📅 08:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">إعلام العدو: بدأت مستشفيات الشمال بنقل أقسام الطوارئ إلى الملاجئ المحمية تحت الأرض رمبام حيفا/زيف صفد/ مركز الجليل نهاريا/مستشفى الوادي العفولة/ مستشفى مائير كفار سابا.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77610" target="_blank">📅 08:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77609">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpGjXac_C_NnUtFfodEgTgw_3przfcfIqGYUNIISSiVzag3-4ZW3DrNsd8Ps2Y2XWHXqSEpf8R8s0nauuWtMC3Y-8KT0VZX7RBIi1bdhZSca7luJgieVTo7t2LzZtCAEl59nVQT9yV-9F9Iu0z3WTlRvKneZesKyoxsVBVtx_OxOLNvV-2gLgyuh2H0YOxQ0iII5FWBsgyCLLOYWuQS3ppoycsTqS5q1Vsu2sKpPyiZjse3J0wXukRmsnUjbDl8c-gobIWbfQUQdSsbjcBgzKiMYB-MLIDijZ-2osA5Q5yS62k-b28dz_wIbXLlQqE3MW0UiZCJ8hk6D9kf6qQUMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد الدخان من مصنع كارون في ماهشهر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77609" target="_blank">📅 08:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8aec20646.mp4?token=N0eHtc32pFaWS1lqeIW67XNYEkJQS2SdsoupWczr0SSKyeiU-0EMEQYYOdEyTjbDh_fVQit4Bw2KVAQ1q84VV23p2XGCkWBQbyJXRH3MtFMTS_Bspesf9k6TLmD-TKQOtHqZOY7gqUIXyWdKZxgtqcjL4j_XG4eG6y7V9UWZWNaKR42SU9zqdotCeaZYbHOzU0mu9oK4T7aDKg0yqbKqTFmntN4o2CkvETOYMEy6LH9aT93fZ7-3vecDI63SVIE2M-YMY1WPxTPA1lI9s0kpy3NSQyuI5uk7LKN7smijIf0jmsM0D2GRr9JtMrVV3wXPJI-4PaQ2G1h7dX9Q14QwAozlB5S4eBEEXmOMs4_yxj6dwoYnbxksQfNOF37QpHiBY9Zl55UwKkS4kTz1Hpm_DDNOvqXNXL4_ty1diAgrrTWAw1csT--0Qg3FQWAuqi9RY_X8HN5q5cguDW8LyeV2mjR66c-meN3CJ4PReLWYs6Hdr_ZxxckfmzkrtnxH0-x4I-E2VZsufwVaj-4Tg2rW_VQ2-qnLfH_AUBtP3-isdwQOA49cNrg0sGSrvR2eyoTBTX6HneNw-ijOW5f_PX7pfKcPTTRRzVOEE71kKsTg2lbhlbBA3Uv1Pt_bQlORytbtbcWMyniDQ2k65Qaa9cxXJ9HdU39-tHHkUBp2KUEMrlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8aec20646.mp4?token=N0eHtc32pFaWS1lqeIW67XNYEkJQS2SdsoupWczr0SSKyeiU-0EMEQYYOdEyTjbDh_fVQit4Bw2KVAQ1q84VV23p2XGCkWBQbyJXRH3MtFMTS_Bspesf9k6TLmD-TKQOtHqZOY7gqUIXyWdKZxgtqcjL4j_XG4eG6y7V9UWZWNaKR42SU9zqdotCeaZYbHOzU0mu9oK4T7aDKg0yqbKqTFmntN4o2CkvETOYMEy6LH9aT93fZ7-3vecDI63SVIE2M-YMY1WPxTPA1lI9s0kpy3NSQyuI5uk7LKN7smijIf0jmsM0D2GRr9JtMrVV3wXPJI-4PaQ2G1h7dX9Q14QwAozlB5S4eBEEXmOMs4_yxj6dwoYnbxksQfNOF37QpHiBY9Zl55UwKkS4kTz1Hpm_DDNOvqXNXL4_ty1diAgrrTWAw1csT--0Qg3FQWAuqi9RY_X8HN5q5cguDW8LyeV2mjR66c-meN3CJ4PReLWYs6Hdr_ZxxckfmzkrtnxH0-x4I-E2VZsufwVaj-4Tg2rW_VQ2-qnLfH_AUBtP3-isdwQOA49cNrg0sGSrvR2eyoTBTX6HneNw-ijOW5f_PX7pfKcPTTRRzVOEE71kKsTg2lbhlbBA3Uv1Pt_bQlORytbtbcWMyniDQ2k65Qaa9cxXJ9HdU39-tHHkUBp2KUEMrlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منازل المستوطنين بعد هجوم إيراني</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77608" target="_blank">📅 08:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1145e5120.mp4?token=KPmSKP_bO65BPg0x4kdhNV56dmfywgmpQ5BDu9mZWLdEcWHq5tNsAM3JR0wH12ctITRewF1YAb0hY9ZtCl7eSJB0XNdI381gEvvISz7GUGsOXo1ZBRGHXYw8fv2Uj_QFASAgnkSHO_N1o1dTz5t1ix8IYG3Kn2t4rA_yYSDdlYdCKM9uvhbu4Iely24t-FZOqerBqpEmo_PpXJaFi3vxpTSiI2H8LkpamGX3YB1MycUCGYoYl0wz9JFHntEERj7bzdxpFoPoFbZ5HkzVKIYU4ImCX66IUKnhbENjKjAv9oiOmQX_AUlaLt7EbyVKHdW7m8GrvMFDB4ncbElI4hxL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1145e5120.mp4?token=KPmSKP_bO65BPg0x4kdhNV56dmfywgmpQ5BDu9mZWLdEcWHq5tNsAM3JR0wH12ctITRewF1YAb0hY9ZtCl7eSJB0XNdI381gEvvISz7GUGsOXo1ZBRGHXYw8fv2Uj_QFASAgnkSHO_N1o1dTz5t1ix8IYG3Kn2t4rA_yYSDdlYdCKM9uvhbu4Iely24t-FZOqerBqpEmo_PpXJaFi3vxpTSiI2H8LkpamGX3YB1MycUCGYoYl0wz9JFHntEERj7bzdxpFoPoFbZ5HkzVKIYU4ImCX66IUKnhbENjKjAv9oiOmQX_AUlaLt7EbyVKHdW7m8GrvMFDB4ncbElI4hxL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محافظة خوزستان الإيرانية: هجوم إسرائيلي على شركة كارون ماهشهر للبتروكيماويات تسبب بأضرار في منشآتها</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77607" target="_blank">📅 08:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77606">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciGscHzdrmnNnzifyEjhG6QNEM8ERdbo3H3oJBtlA081ZQLaVoC1omRg928fCLxhBq2RUCXFlPjB9VeNQGNyF9Adx-qcSQZ_1_V2YcJOBZnaLo-RabwPguj6tS8q0PMb-Dpm6-3s3cAFYQs02TENchn8IXAvLtOdWtvhB0wkmSqJZbnToxUgswEB1csAD7QDSrqEMmECTEnleAolGu2vL9ucuXLPbP72o0h_fKknO-2PJRHVpgP3AE0BA6NHFTJb6UJKo4Kwn1qMxHdp4bsru_st6DSEfshgFj7W_UnBWQjvurizf-sTfO99Engfjo9K6Zr8qY0Bs5zBUEISO0XEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيناتور كريس مورفي:
لقد كانت هذه الحرب مُذلّة لترامب وللقوة الأمريكية عمومًا. وعندما أعلن ترامب أنه سيتصل بنتنياهو ويطلب منه عدم الرد، ثم رد نتنياهو في غضون ساعات، تضاعفت الإهانة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77606" target="_blank">📅 08:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiYSgD-hGPcmu_qJeN21P7L-KXHxDVnk0w53EVdIE1mFrTBncS_3eHIzK4MRFTrRT426yX9jAfTu1nVmTPOKYEJBbFaUVaKM3WkQ2afaHTwxGUqGn7dQZ9aiZIDl4Zr_EW6n2LlZ5G25VhN2ZNjQSsA0D07XDrzXIMdQSxhGcDgcl58U1IgnWSRzqiW1Kh9oFGMRA9t8eC-MBfATukTZYSDxxPgxICXlwKPRsN7hQYuWgzQsDarjX5BdgWNSRolyU_qowXN1f9tRu7Aiv8HnXCD9EQc0IG9eYNsuQJXZiuGFynqheySqZOtOpkayqZ4kqWgCfppvXawEyQfNjHoPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظة سقوط الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77605" target="_blank">📅 08:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1318de51.mp4?token=Bp24VXl-uUcJZFZqAxw2kAS8qJCl1sP1uknqka4Qy350jOuFF84Be7rlZ308b8UUVtZIzT6OnSJRBuP96iuQqjkF-CJ3e8_hyquoy3Q_p6aWdlebbnC0Lu5jtPaBVkJx9itXZSonctG5Ifh6AOrcr4k2ZkoaeyJRyCd2wZiKQTkpmJ2SMpq3wc_Ma2BaAdb6vEP8pzEuWeYcy5tYz5O0emSFpbwdfsun1345FwGGhPZ3qqx7_UcVkcymF_AbGp9YdWWkvgyujzMbqDUiELSdRamUOGhV9uRRtosWW4VHvyoD1Y5rnSnUbV_xjYlBT7I0BYEhfeeEIvL6MV75VguiJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1318de51.mp4?token=Bp24VXl-uUcJZFZqAxw2kAS8qJCl1sP1uknqka4Qy350jOuFF84Be7rlZ308b8UUVtZIzT6OnSJRBuP96iuQqjkF-CJ3e8_hyquoy3Q_p6aWdlebbnC0Lu5jtPaBVkJx9itXZSonctG5Ifh6AOrcr4k2ZkoaeyJRyCd2wZiKQTkpmJ2SMpq3wc_Ma2BaAdb6vEP8pzEuWeYcy5tYz5O0emSFpbwdfsun1345FwGGhPZ3qqx7_UcVkcymF_AbGp9YdWWkvgyujzMbqDUiELSdRamUOGhV9uRRtosWW4VHvyoD1Y5rnSnUbV_xjYlBT7I0BYEhfeeEIvL6MV75VguiJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة قصف مستوطنة "إيتمار" قرب نابلس جراء القصف الإيراني اليمني المشترك.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77604" target="_blank">📅 08:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/838333eeb3.mp4?token=bFKT4khL8vkPgih82yPQAmRhSPxGgC1QBYQInqs9OHYrfjr7euCeoBBgim6WEN0lHib-HCadt3qnijxPrj59YEt_SrhMl8RAImxMBhjJZ3T0g_TuAXbyXX-jdpP3W2oNAuwZBG7KOEJDE516nxaR_54yXKU_BuCfb2wDVyCP8w9MnokjfSDooncMulLQj_B4_UGFfctjfN_Cq4_VZbMtwc_jk7p-dVdCbxpSKhJAuxJ0NtNaTTf_Sjb035--gFMTli2rjhQPlCGfCMxNcGMUG2WhzA22NYQeOqiKWpA6kc8WvyViXOQMTMcxM6mc_tdJEBLotFfsYWiFFnUVol44ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/838333eeb3.mp4?token=bFKT4khL8vkPgih82yPQAmRhSPxGgC1QBYQInqs9OHYrfjr7euCeoBBgim6WEN0lHib-HCadt3qnijxPrj59YEt_SrhMl8RAImxMBhjJZ3T0g_TuAXbyXX-jdpP3W2oNAuwZBG7KOEJDE516nxaR_54yXKU_BuCfb2wDVyCP8w9MnokjfSDooncMulLQj_B4_UGFfctjfN_Cq4_VZbMtwc_jk7p-dVdCbxpSKhJAuxJ0NtNaTTf_Sjb035--gFMTli2rjhQPlCGfCMxNcGMUG2WhzA22NYQeOqiKWpA6kc8WvyViXOQMTMcxM6mc_tdJEBLotFfsYWiFFnUVol44ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد جديدة من السقوط في منطقة شومرون شمال الضفة الغربية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77603" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYWH9f_XcfeM8xn3mvHKb8hzPzsA54f8GWyEIQn6udqnwqEc55aAP7GMZjt1Mp-EfYhhfOzkAfqbw6uigW4mwSUBDEMTR53vKLvmKaYI0F2ybTlsM-Na5Chp4e9jXASzj8sMg53azCIPPgao25t6qBfSjZem9mixFNd9b7xxSdc7BESvSqzvAbSxk2Gdb6KpbE-_8oNjguiP6vc2SRMNY3YUvyw2CeGZ300sE8BoWRuy0dG9FP7NDsaTKFCZUKnfrHgIiQhrLLsEEA-ZjA343a4JlsvWpFXR-2LuOKeEbuMMSLu09xzmA-RGraZwTtC16-lzSUlMScKe8CA5lHjWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهيد علي لاريجاني : اقلیم پارس را غم از آسیب دهر نیست
‏تا بر سرش بود، چو تویی سایه خدا</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77602" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">إعلام العدو: الإيرانيون انتقلوا إلى إطلاق رشقات صاروخية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/77601" target="_blank">📅 08:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">محافظة خوزستان الإيرانية: هجوم إسرائيلي على شركة كارون ماهشهر للبتروكيماويات تسبب بأضرار في منشآتها</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77600" target="_blank">📅 08:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c8a0094bf.mp4?token=gAfczImukvrcRX18_TxJziY8GbXXbjG1p37cvd0ehlFjlylxkZN3YJ22ZmV-5bxxyqscQyVxi196jjZdGIKoVy_qEOBt0dnnbwW0LS19AXBGXKPBE7lDdP2sdERQCOUjse4WJ5QN0TFvEWOtFZL77qn-etPgGalqD0y2A3I7oto3YT0_WQM7hgjXBMMKb3C2ti-nTmA0VN7jsl2ExBlWR5h0x8RFnlQwvWaFDbX_rBSK-WEx_s0KosS3I0kEyDz2bUdBLT_-9PcVElSYwXqLRNglqri4zSz_gVuZZ-zVnl0rt_XQGPtbj0Y6sJaHQXq2llw147bzLJAI0_irE-1sPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c8a0094bf.mp4?token=gAfczImukvrcRX18_TxJziY8GbXXbjG1p37cvd0ehlFjlylxkZN3YJ22ZmV-5bxxyqscQyVxi196jjZdGIKoVy_qEOBt0dnnbwW0LS19AXBGXKPBE7lDdP2sdERQCOUjse4WJ5QN0TFvEWOtFZL77qn-etPgGalqD0y2A3I7oto3YT0_WQM7hgjXBMMKb3C2ti-nTmA0VN7jsl2ExBlWR5h0x8RFnlQwvWaFDbX_rBSK-WEx_s0KosS3I0kEyDz2bUdBLT_-9PcVElSYwXqLRNglqri4zSz_gVuZZ-zVnl0rt_XQGPtbj0Y6sJaHQXq2llw147bzLJAI0_irE-1sPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواتف بالأردن تتلقى تحذيرات بشأن القصف الإيراني على اسرائيل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77599" target="_blank">📅 08:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77598">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رشقة ضخمة الان</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77598" target="_blank">📅 08:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77597">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مسؤول إيراني: تضرر مصنع كارون للبتروكيماويات في خرمشهر جراء ضربة صاروخية إسرائيلية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77597" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77596">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صواريخ جديدة من إيران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77596" target="_blank">📅 08:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77595">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">إعلام العدو : الإيرانيون عادوا بكل قوتهم.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77595" target="_blank">📅 08:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">إعلام العدو : مجلس إقليمي شومرون: 3 منازل في شومرون تضررت من إصابة قريبة بصاروخ إيراني</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77594" target="_blank">📅 08:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77593">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyrhgBestFO0MLOo8eDZDHgnbcpfq2D4hnyqTDAnHuOi4y35_ds-Uimxod2n3zYeUN2uc14q8xC2Vqs_40jEnhjhSr89HgNTAmsNZqMzNAAXmt730IJMPtTDlhPelh2HQpt7sESNZj5jHGWcy7l5lS_v_QZNC4bMfBFOE0Na1bwdBdfddTYxl19nKgv0nAjrl5q_rkIboMjGklXvrh9ipJ1lknlIj4xpIh3S5_GoNjn7sfPVcXqwhWoC4HDy2wY6Z2Op7U9I7JG0l8W-AuBa1BaN6SVe2n3MOUpnczCJ5FEPKHbEh93QW9kp2vcxiNxLOcMGA26Aynv2Iyw39GPlTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من السقوط قرب قاعدة عسكرية بالضفة الغربية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/77593" target="_blank">📅 07:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77592">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صواريخ جديدة من إيران</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77592" target="_blank">📅 07:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77591">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ebba21fa.mp4?token=Y6lWZxgPC6LxRXkjpQvKxeZ3AmP49uuq6JzhxvTMPovENZASS8jOBjl5cnAfmVWJ2iCmZGCWY1fxoieVyEqlQBL0p4y6WTrHF3M3yLqvrz-1E0hOOP8qCpcCDySsEY1XYis1zWdCHV4UY_Jo5vDRHitrAspdLx75qQca_ASkNbe0KoH1vlYxW3c8B5w-VkOaH2XpiBJ-1EME5VFBoQodHl11aa66km4qZiCWY799Xd1BB2rgjC0Ygm4a48dh5dOcOx_RNS-5ap4ou8JUCDRuPQD6XKwJ7tXFyBlI7Ljk_nd4dkfBe5oKcVih5I3rYUZ2v0Ll6UkQQj1LjjZ-vJ57mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ebba21fa.mp4?token=Y6lWZxgPC6LxRXkjpQvKxeZ3AmP49uuq6JzhxvTMPovENZASS8jOBjl5cnAfmVWJ2iCmZGCWY1fxoieVyEqlQBL0p4y6WTrHF3M3yLqvrz-1E0hOOP8qCpcCDySsEY1XYis1zWdCHV4UY_Jo5vDRHitrAspdLx75qQca_ASkNbe0KoH1vlYxW3c8B5w-VkOaH2XpiBJ-1EME5VFBoQodHl11aa66km4qZiCWY799Xd1BB2rgjC0Ygm4a48dh5dOcOx_RNS-5ap4ou8JUCDRuPQD6XKwJ7tXFyBlI7Ljk_nd4dkfBe5oKcVih5I3rYUZ2v0Ll6UkQQj1LjjZ-vJ57mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من السقوط قرب قاعدة عسكرية بالضفة الغربية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77591" target="_blank">📅 07:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77590" target="_blank">📅 07:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية خلال الساعات القادمة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77588" target="_blank">📅 07:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77587">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عمليات إطلاق إضافية إلى بئر شيمش وبيت شيمش</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77587" target="_blank">📅 07:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpXxIUc7nOz-lJYOILjBzn_pTtykmMCic3cMnM0RL4uYlkia7xnPri7X9QzhsmpR0VoNooIyHQd8ZcNxcKuYTcEOKaaTurok5zL0UPF_ftNp2iTkLdHVQvIDG9Nh-YgxH30g0a3YdMlyoUsLNRDqtLbT5g-fEtxEJ1gX5xM6c4_oVMSrLBzGaaoiWgdCrSItWYm9jLL2BLv9LnmMnq02B9Gp21FvYdBIO8ES7iMlO1YkxXdiNNXstH87PWRRR_EajW9k3sL4jUkQe6pmcjBEi7El__GIA3psyu22oOGM4OhpImAbyqM2koE94lcCtxR_9gNWPX6LpYRU5TdkDvYXTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الموقع العسكري المستهدف</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77586" target="_blank">📅 07:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGpV8rRHukgaDfvsqw71eOi_v6JgtntTvUXS84Si0RKdL8EETciATIxmGtyy25Ns_pJVP61F1e99Eemg-XewwKqbPfrMGXz0CJwuqv6SsXUvZLM7jxU_zzB_ph1Piwyvl56ejf73IrsOAum_Qs02oFnDnvhGY-BWfCv8icbeJUUHqheUcd265ToRRl9iF6xEJ7M5OQDzK4WES3dsh0nCFqBztZQerIpkP3v8xqLSnelF0w70sVjNgqOXi4kK7CaArdmQZF8DvDMvzAR7uzksUVcIEnKITlYKjNK-ABRiFd7xTYiKg9ygIU6yg3lCahPLzQ4_I0VSOYDSwyEkib4toA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ ‏سقوط مباشر كبير داخل موقع عسكري بالضفة الغربية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77585" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عمليات إطلاق إضافية إلى بئر شيمش وبيت شيمش</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77584" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77583">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9d5992f6.mp4?token=TPEozM9PXyil78KVoQHlkwFyS6tbVRudBrHKpnL03blRb81oMOPMSPM5fxrDQ8FZRObetrp6b3-vsij88draWMF8G-tH_Tl_G1TNqWEGY_t5oFrhTCczVPz4yw-kpO2Af-ZP26zXvN9IGYCgX5UkyNj5rrd51adv89pzmdrLf-GqY_W_rpGFfEdwgqeucrJ8orD7_OdCga3wLrcu4cs77fgC0gTTHsWFPHHxNdvu1YaHvWbcVOYMxd1iQKcfOYwTm-itz5Hrhm8wGSW6yg_QU0e5JAqLa2u-BHYaAvGJ1shlxcAHCAzWNmbuCCbnFjWLrCv02WYQxye2EVG-Cg318Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9d5992f6.mp4?token=TPEozM9PXyil78KVoQHlkwFyS6tbVRudBrHKpnL03blRb81oMOPMSPM5fxrDQ8FZRObetrp6b3-vsij88draWMF8G-tH_Tl_G1TNqWEGY_t5oFrhTCczVPz4yw-kpO2Af-ZP26zXvN9IGYCgX5UkyNj5rrd51adv89pzmdrLf-GqY_W_rpGFfEdwgqeucrJ8orD7_OdCga3wLrcu4cs77fgC0gTTHsWFPHHxNdvu1YaHvWbcVOYMxd1iQKcfOYwTm-itz5Hrhm8wGSW6yg_QU0e5JAqLa2u-BHYaAvGJ1shlxcAHCAzWNmbuCCbnFjWLrCv02WYQxye2EVG-Cg318Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات تحاول اعتراض الصواريخ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77583" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77582">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ecbaa6e4f.mp4?token=rWwpOF0dPx8th11GMhgQ7wwcS2uQtfFeOb9cOdeAcMYT_jbCej8b-qhK5ccvLFNLbWwasBc2rSDNZnVFSpHvgg8270cEQ-RJh5yGYQFaBhDhnv1lmCzqxYcmXWH-v1PmnGf4lDxEOWIGNN-Uvhl0dZi3qHdM7-GUY-2SeBDSihi1ELLmHMiaESkf8tJYDOAavFVtZz1Za1ocR-dlQ2XY048YDOQsaaHTRvXqtaKTmd0kFVAr1CEavyF9W8IzWKmxtHT3w4eLjRjdHJVq-RLwfhuN4XTzNeZuVIdtekVxbJWxI-AJ9qz8xkZ3VuOANnmzFd9y3sBwmifjX9nD-cAeQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ecbaa6e4f.mp4?token=rWwpOF0dPx8th11GMhgQ7wwcS2uQtfFeOb9cOdeAcMYT_jbCej8b-qhK5ccvLFNLbWwasBc2rSDNZnVFSpHvgg8270cEQ-RJh5yGYQFaBhDhnv1lmCzqxYcmXWH-v1PmnGf4lDxEOWIGNN-Uvhl0dZi3qHdM7-GUY-2SeBDSihi1ELLmHMiaESkf8tJYDOAavFVtZz1Za1ocR-dlQ2XY048YDOQsaaHTRvXqtaKTmd0kFVAr1CEavyF9W8IzWKmxtHT3w4eLjRjdHJVq-RLwfhuN4XTzNeZuVIdtekVxbJWxI-AJ9qz8xkZ3VuOANnmzFd9y3sBwmifjX9nD-cAeQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‏سقوط مباشر كبير داخل موقع عسكري بالضفة الغربية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77582" target="_blank">📅 07:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77581">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77581" target="_blank">📅 07:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77580">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات منطقة ديمونا جنوب فلسطين المحتلة</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77580" target="_blank">📅 07:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77579">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f437852b.mp4?token=YlnhP1aNhxcryHTXJQbPrfO9p4pp0cCAJznQupmhcMklhSaETANzv8N8gaOmitYg0bp-cqpGd9WkIMxhpkKchfk2bDgJcMv7V4btPF7e4IL7YpXdN737G4OH9r0ThlAPoixkNRpwxXSMkX80UQ7urgkG_WvjlmuwsbUG8wIDtqorhGQDgi0GcX4ztbaiaZ-tZwZ6GqVe1_eMVa6OgLyKW2BIVcKDVuUqNVLbadYidstFuopPj6fHKN8sn3RQ89gtFG73lDwqkDxpqmWJlr_zcPRkboATy1-dONEwkUqmw8vgKgMWYRJpRJokm3I4EZXBu8PSPo0GFdZ4RgOp8ONDJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f437852b.mp4?token=YlnhP1aNhxcryHTXJQbPrfO9p4pp0cCAJznQupmhcMklhSaETANzv8N8gaOmitYg0bp-cqpGd9WkIMxhpkKchfk2bDgJcMv7V4btPF7e4IL7YpXdN737G4OH9r0ThlAPoixkNRpwxXSMkX80UQ7urgkG_WvjlmuwsbUG8wIDtqorhGQDgi0GcX4ztbaiaZ-tZwZ6GqVe1_eMVa6OgLyKW2BIVcKDVuUqNVLbadYidstFuopPj6fHKN8sn3RQ89gtFG73lDwqkDxpqmWJlr_zcPRkboATy1-dONEwkUqmw8vgKgMWYRJpRJokm3I4EZXBu8PSPo0GFdZ4RgOp8ONDJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفارات الإنذار في القدس المحتلة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77579" target="_blank">📅 07:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77578">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b9133fb6.mp4?token=nmLI2g4NKayI8KRWeAw8RfD6sfq0ElJPgrJDj8AgRY9vi9rcj2qe7X4jZfz-yRVel6aP8dASh6tUgb7OgKTBm10ZgTULxC6m1g-Oc5Hdexck-nd_MlsRjEzYTNDEmtNqgEkFEj-X9JYtiC0xoF2qAgzrZlSDOWikUwfVkALM_pkn2yMP3oVxolP6jQ1MQVJIoL3CWG_PGbcoNSH9gK8K6U9U_EzTdBT9V1H2xivv_Li2l21GtDWKRnWLmbmCPT9pDx3STs63NQeuhl1f5r0UKbzGgrEwwYuUADz2pWqo1GZJ6BbmP6rXujpoVrTkcSpzz9bQOXLpOxKDPUUUR_zhEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b9133fb6.mp4?token=nmLI2g4NKayI8KRWeAw8RfD6sfq0ElJPgrJDj8AgRY9vi9rcj2qe7X4jZfz-yRVel6aP8dASh6tUgb7OgKTBm10ZgTULxC6m1g-Oc5Hdexck-nd_MlsRjEzYTNDEmtNqgEkFEj-X9JYtiC0xoF2qAgzrZlSDOWikUwfVkALM_pkn2yMP3oVxolP6jQ1MQVJIoL3CWG_PGbcoNSH9gK8K6U9U_EzTdBT9V1H2xivv_Li2l21GtDWKRnWLmbmCPT9pDx3STs63NQeuhl1f5r0UKbzGgrEwwYuUADz2pWqo1GZJ6BbmP6rXujpoVrTkcSpzz9bQOXLpOxKDPUUUR_zhEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">3 انفجارات تهز القدس المحتلة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77578" target="_blank">📅 07:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77577">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات ضخمة في القدس المحتلة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77577" target="_blank">📅 07:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات ضخمة في القدس المحتلة</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77576" target="_blank">📅 07:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ايران لا تترك حليف لها
حتى لو كلفتها حرب وجولة مفتوحة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77575" target="_blank">📅 07:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77572">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZf2hp97ok6px-LS7C-rBJKZ4OUVxhKb9Ire07fIKE9hQ9l6ty05M0ubFIQuqhGjRPHdf7_n9RjUzsh_4NwrKERy4AwphOGKhJxGyfYdXfkMbswrfBDyLjo2tvSOIpZpS6pJuQgWWoEzvxS3mpSk3FnF-mDj1KWK_uLb6YBLIksNsWLjyta56sFQ5qerbKqfDAshxcQSL8rfUBA-Gxa-stHYLwvKByjdwVijANvsCoaPTQBeYUjHKfbSVe6HNAsSJkVMiYvatGLA6OJaJ6H9q2iLY--gey2MMNNrpvwLf0ZjiOctFDYUB4p98rCo7M_-EOyCUFRpWONjPVRglfdFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQuXCRlOr8NxwA8GL5SC8kJ5bBvJ6E_mUKGts0cW74dLuXCfNm_LQEFyLoLpztgq9OK4S0uvOHIVPxAXyjkWMVHalRc9496RkQ_btLpghYIAHhbKh3GEXJq52NFF3W6fxo5nxL3rg38oCSFQcZfkhsCU0FClhrK9rC5cp7LE4nQK8chEUOxTXnIVXV8Eeyeps_H4vXsc0rRzsLw3AbZ-S0f2_j9yR9STLehsLSjJjnuFqsY-Hs-JZ1ZN6wQk_1GelAzlPOU3C6ri-FtGQdEEhWho8sC6tQD5RI7h8DNzl0P7TmQVip699PK0yFuIyTzJus2p35Wl0pDviVzrSFPHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FpX2wODUiBS170Jfh7V7XKmvrshi8Kp-19eNtl-2yyh9_Wot0akSYXc3x-VzM39MYYKglQb5PmKrF3dukTbKbuxt_ieZrVQ1NT6x3iz6YG4eGZ_GLfKq6fxAJQTkfCR657xyQfVSNEYKYVIbkY_FTlEjzF9n4e7icl6HQxrLeK-4qiG5X6LBGD3m2D1KNfMZjqB4oiIaIZYy_B5vdcBJmHUoUf68Sf1-ObGMyO0iGFPT5Tl_qo3S7rKSWdErUidPYlKHmZ6nBkAfvQEg4nm_77cN389GfC5soWQ6UnktqbP1dVw2AMrGrWOvKjgckZ8QgFdoeVChjpGV94mIUsjW6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من إطلاق صواريخ إيرانية نحو الكيان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77572" target="_blank">📅 07:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اندونسيا زلزال بقوة ٧.٧ على مقياس ريختر</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77571" target="_blank">📅 07:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات ضخمة في القدس المحتلة</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77570" target="_blank">📅 07:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77569">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOLXjB02igxz6en4KR6p7r3TbAsWY6hvUM1xCDXeN0QxdGn4db3TT0tG8_bZHerRt73m0WK4rZyyBx--IrkOmSCI2VVi79sk-cQYKELx3ezMs0zLp-IanfcCQI48qNYiltEYTz2DC28xnL_LAOb19A2SjGf9lGvh3BiT3bRqdpg590lv-b4AEos7x1w17bIohJfHhn0PIzcELkEm6gkcNdk0Q5Az4hKC5Oo6KK2ZhHG8cpfK4dkA_5UKJ1pmD35Qyn7PYcLDZEt6ZfHePf-r8Kcky05gh68pz7Ry2L9RmOzuKv6boDyz_QwzcWC_V3NZTTUWjrBanS5RZK7S4QYbDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من إطلاق صواريخ إيرانية نحو الكيان</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77569" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رصد إطلاق صواريخ من إيران نحو الكيان المحتل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77568" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77567">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رصد إطلاق صواريخ من إيران نحو الكيان المحتل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77567" target="_blank">📅 07:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رصد إطلاق صواريخ من إيران نحو الكيان المحتل</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77566" target="_blank">📅 07:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رصد إطلاق صواريخ من إيران نحو الكيان المحتل</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77565" target="_blank">📅 07:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6af6f4c7f.mp4?token=LKdOeKlmWPa0kHNovLbzVutZ0TX2-DTmHDSNeP9hPoErmGVoAEg8GUbYtK0cQmpsCS22gKsRKY-PfjJCORnEBE9Pso6-DES7-5YybRnCNL72cN7WstLjUIeN1-1XcxDjT9lPyPUl9TMw2kTTe1XYRxvxm_xgquQ8BYHPPIXSwY_2aVq6e1wZs4rcoi5YROsEiAncZvt70pR-uiIhr1Noxy_aV-BlVSmWHDblNhJhHSNicVTAKYzSNaXDZ8r62lgH_MuZy5_gigmiihfAojlb8rMU3gjmR35pB6Vsqv5OR04BS9fmpUvo08zl37m49yc3S-TEqV96dX2BZJrDc1joRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6af6f4c7f.mp4?token=LKdOeKlmWPa0kHNovLbzVutZ0TX2-DTmHDSNeP9hPoErmGVoAEg8GUbYtK0cQmpsCS22gKsRKY-PfjJCORnEBE9Pso6-DES7-5YybRnCNL72cN7WstLjUIeN1-1XcxDjT9lPyPUl9TMw2kTTe1XYRxvxm_xgquQ8BYHPPIXSwY_2aVq6e1wZs4rcoi5YROsEiAncZvt70pR-uiIhr1Noxy_aV-BlVSmWHDblNhJhHSNicVTAKYzSNaXDZ8r62lgH_MuZy5_gigmiihfAojlb8rMU3gjmR35pB6Vsqv5OR04BS9fmpUvo08zl37m49yc3S-TEqV96dX2BZJrDc1joRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاعدة سويحان الجوية في مطار أبو ظبي تعمل كمركز تمركز لطائرات الهليكوبتر التابعة للجيش الأمريكي التي تشارك في الحصار البحري لإيران.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77564" target="_blank">📅 07:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏إعلام العدو: الجيش الإسرائيلي في حالة تأهب تحسبا لإطلاق إيران صواريخ إضافية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77563" target="_blank">📅 07:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77562">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOYltaaiuhPVWqgxJIqbMZpuHO4Q3DFas2PFxXVeEnRh6be08g3LRxWIP62baNnPSV6db3WgFtGK-CcN8g3TDyMpGQ4AmfTJGiqIPvlHdfRvR9Ga-VhgQNEcRWAd1JFxMm68YJblwT-MveEKG4ju1_8lhx0LnjI4LPSFUXsuorrQ_b-UEPmJZT6mD-PdUM6ePm9g8qw3TlbP2gcijZTfaej_j2FBPda9NnSTa61n4bRT-qT7ki7DR4i6e0JS6QxKfZ-NJ7UOa-UBXwfJwD-6h00svFU-IBVhqG3wWQwT-QK8Z8Pqi3Px1JUEvrOf3Gx03d-i-dbHGcZf1qClE-bO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط جوي أمريكي لطيران إرضاع جوي قبالة سواحل جزيرة قشم</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77562" target="_blank">📅 07:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77561">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDoES7M7q1tCkXSA4nR0RQq1xhLbybT-s3pAzjUJQiYhQ0RSG7focDsO_SwifRSbLrWFkPi7IHyfodTANtZzWLnwKtS2vRn3DAUiOcWPApFZxHOcNn8JvlJzQYaonZjqjxkDYKqyTPFPdnMH5k7EL61MZQ0D72V-2K73W3AS3DCzjDAKCCNd-b3T9ZIfenInQkqnGB12FyWm7rZ3_iCbX6u0ri2xVVd0EavxX3gMGaw20t1OjuU-eJxitgPSe-JF-pBbZFkwLTaRou0QSx-HxPzkJBYEDRJAcoMfIKku3WiNDYPc7QcXBCFzJbLov-XzC-yu38iYvxPbh4o4mKUzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القيادي في حركة أنصار الله</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77561" target="_blank">📅 07:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77560">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5OSB1Groxc3OJX881_gPmP79n6WCXw_ZU59hxxvLNA6qMhk52zLe67a5AEl9aXaeELrODqQufZfCNJEKVYgCReHNs74u5e-0D-4NfdQnxsBs4bbnRtNmn4pzKV6v80h0SYDsqKyGdLOJ_Op-lGUNibPchvjjxKSycs2y13plUQPtfa-mTp3xeP2HI_xJGf3mz9OeRMoTDKJnkeA1cysdWa86cI6KtDU4p47k-P7P4CN-SKK9Yjw9_qa0P9FZk5vTfOSIS7htvjYsufgqILJUNm3OuNihrTcXfj1F1mkV1crotbBTurUPL3IlhKTCYRuw0EvSIlHslia4V0mfRVVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو بعد ما نشره جيش الاحتلال: هناك إهمالاً أمنياً بعد تضليلهم وجه الجندي وترك اسمه ظاهرا إلى أي مدى يمكن أن يكون المتحدث باسم الجيش الإسرائيلي غبيًا؟
يبدو أنه لا حدود لغباءه! أمن ميداني ممتاز</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77560" target="_blank">📅 07:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77559">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWVzE2UMrzcV4Ei2TO5I0TeO7blPyJQqewOIWsQQm_4VFYOAYLyObttgQfY9HrIPGfQx6OTDHeuV--T80-gq4ssQCi3x_KVOceyvwSVZnMNzJt5k90d2JlG3iX-6duOzXMZZh95Kmc4GcTBrqLIFm0m6LgoJysizJ8DmSCblChdneIbS514S8Dm28eUGuhG0MjPTN6LCqLp5yBtGiWiRJul6LHJHBN64FCW8-cfX04V_Bkv1LtZuMxqXxOqIXuDKpHv09Sq5fqtuUXOajpfnd3dtRlvkJ4i2BzbsInkHjVVdFWRENluFWIcfb0MbdvWKEn-yVUPwTZlPC37gYeP64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القيادي في حركة أنصار الله</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77559" target="_blank">📅 06:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77558">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">إعلام العدو : بعد الضربات على ايران: تم إلغاء شهادة نتنياهو اليوم.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77558" target="_blank">📅 06:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77557">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmVLEK16yuOIsNfonmIJXPtMa-ECmIwcFqOlBCpexbv3YNwN8w2vK8xfC8mzXNuTpXRKc6Z-32nh7oNIPQdIs7be8DaBztaHtfOhAN5F_J85fp-P7g9iexnlN5UapU8bjYGbowNOs5GphxuG-RXuhIVxViacwWpxKblBTW1hES2XPWFfcyAawZWpYyswTGeOLdIoaw1fohhMWwey_EU_xlyNuVsBDZ1MDwdgFI6YKshBqtuZZweCHpipRR20N8jKb2-ddH-464r4OspWTJtxDMBMo0nJz0tobxI6XAxrmNYOjXuCWrR6daBc0OWpXcAYLsMDY_9j4m4LVeXEe0bsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السفير الإسرائيلي لدى أمريكا حول القصف الإيراني:
أطلقت إيران 11 صاروخًا باليستيًا على إسرائيل اليوم. يمكن لكل واحد من هذه الصواريخ أن يدمر حيًا بأكمله ويقتل المئات. لن تتسامح أي دولة محترمة في العالم بمثل هذا الهجوم، ولن تتسامح إسرائيل أيضًا.
إذا أطلق حزب الله النار على إسرائيل، فسيتم ضرب مراكز قيادته في ضاحية بشدة. هذا ليس له علاقة بإيران.
لقد سئم الجميع من هذا النظام الإيراني المجنون.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77557" target="_blank">📅 06:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77556">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">إعلام العدو: إغلاق المجال الجوي مؤقتا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77556" target="_blank">📅 06:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5KYDeEkrQs61XC0ciIPK-NQ1KQ7qcQUyl3AG6cTwQki2UIYM70WpLd7rRgNjS1f7MSTRCJO7Vyx4b8yK4x1Q8rDkYUOsb1Q6iO1KQCqLRcES8vC4ZKnyDGWpInvSQo8vRdAXZOF3oKaYOMHRyt7oQpq2Uc-PAsS56gPGapVpJHuFai0fea9u3pMuGApOY_aoiva8NINeMeA_eWhTGviVQJe6uwkvF5rQHvpjsFcDxkvw5zsrv7vTssQc8UfO7CrnR_N8M10xOvEXzgh3WZhtmBSFzQq7qUq_dmlitAAHBIO29ypE3_eOcKPCMhZeiDTFvCIMYyqxSVZARmZq3Yvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر حول "الانتخابات المزورة" في كاليفورنيا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77555" target="_blank">📅 06:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77554">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">إطلاق صواريخ من إيران باتجاه الكيان المحتل</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77554" target="_blank">📅 06:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77553">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">إطلاق صواريخ من إيران باتجاه الكيان المحتل</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77553" target="_blank">📅 06:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGoQIly3wjxRUyumtHD9HqLKuRfNKGJ3vtPg-d7ihiRQQgBvxQQteA1Y_IWA0wYZxd31suJNPe_ll9BEWkeSAWB30iNFt1pfDhHF2UYpYnkBAdqrHgNa8ecpiOfaNAmubuzFaw2xVFQALGqMY10OmihVi3E-P9r06_PTJBQ5yS8_yW-vcR1QanlBAYcIOx33AfgDaxFwD8euQfk0soa5-igsw-3exFbZQupc_bIh1KebdzDEVhLSBQEKY2j_0TvxP3rJw0npND7zL7b4G6MTpAdMASizeqUKd89haPwvO93bMTep3MdJPEK1buLTkigQc14pG09IasG3_CjPRmbi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو: إغلاق المجال الجوي مؤقتا</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77552" target="_blank">📅 06:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77551">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">إعلام العدو: إغلاق المجال الجوي مؤقتا</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77551" target="_blank">📅 06:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77550">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تل أبيب والقدس المحتلة تحت مرمى صواريخ رجال أبوجبريل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77550" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77549">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/77549" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77549" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77548">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اليمن تدخل المعركة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77548" target="_blank">📅 06:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اليمن تدخل المعركة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77547" target="_blank">📅 06:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77546">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صواريخ يمنية نحو الكيان الصهيوني</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77546" target="_blank">📅 06:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77545">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اليمن تدخل المعركة</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77545" target="_blank">📅 06:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77544">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77544" target="_blank">📅 06:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اعلام العدو يتحدث عن رصد رشقة صاروخية قادمة</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77543" target="_blank">📅 06:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اعلام العدو يتحدث عن رصد رشقة صاروخية قادمة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77542" target="_blank">📅 06:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
مسؤول عسكري أمريكي:
الجيش الأمريكي لم يشارك في الضربات الإسرائيلية على إيران.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77541" target="_blank">📅 06:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
انفجارات في السعودية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77540" target="_blank">📅 06:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">من العدوان الذي طال مدينة أصفهان الإيرانية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77539" target="_blank">📅 06:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
انفجارات في السعودية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77538" target="_blank">📅 06:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409b3e3d81.mp4?token=shZlmsathsu9tQZiDAID0AOwG1yCk32rebyU7aOxc6reI7l6IPIt3S1ovF2jEbAHvu-DzJUKSOtDK-cbOxKHdWSxVvRpTLPSUhJlLcXi6U4sI0cki-cOa_0vS5F83pLJe0Olm4a-vAQDX5yke6DYGiZT1HJoUHL2c4Q2q-7PxjzaTtHWnLe4-nDNHTkY3Nlppf_DYQwzjYKqdehCGAM05paumtzbcI8MLsNy2gkaqK9dAmLa-5AGtrAUWXGOeIG4Yw9g86StFVrPYQ31tq36nooEa2CmwvX0YChciQBonsMZf0qqbcMivB9hg9Nh0sTQek_6SljMdvE9mXDbq_sFM5NSoSNv9pv9VtaHaWIri_y3_ijtSyFMLvEhrK-OTRrRn3hr41OZtsLqvn3dcFmpPnduAbhmJ7Q2EVp261KfMCjA5yc5IRii759beHCRFOn5WYviYbEtE4jglRPNks5wVpL_mJzWJ9v_OpK4Qv4_Z9t1KqyOQnfSPqwz2oXKi9vaA5fOoMMyGUUCIFYXSdM_dl861srrhscsMkBJOrPQmohQvNkBOEarNKmx50RuQvXK6l3nOvwglOCrxbIi5xokxGdG8Dc4p7ejjcj3EkbSwSx9_uU-xgcRYiX4XNy2k5M4YJNhUD7GQju_Xvmz-DvLkDgi5S_BvFc5jAxHJH_Hrs4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409b3e3d81.mp4?token=shZlmsathsu9tQZiDAID0AOwG1yCk32rebyU7aOxc6reI7l6IPIt3S1ovF2jEbAHvu-DzJUKSOtDK-cbOxKHdWSxVvRpTLPSUhJlLcXi6U4sI0cki-cOa_0vS5F83pLJe0Olm4a-vAQDX5yke6DYGiZT1HJoUHL2c4Q2q-7PxjzaTtHWnLe4-nDNHTkY3Nlppf_DYQwzjYKqdehCGAM05paumtzbcI8MLsNy2gkaqK9dAmLa-5AGtrAUWXGOeIG4Yw9g86StFVrPYQ31tq36nooEa2CmwvX0YChciQBonsMZf0qqbcMivB9hg9Nh0sTQek_6SljMdvE9mXDbq_sFM5NSoSNv9pv9VtaHaWIri_y3_ijtSyFMLvEhrK-OTRrRn3hr41OZtsLqvn3dcFmpPnduAbhmJ7Q2EVp261KfMCjA5yc5IRii759beHCRFOn5WYviYbEtE4jglRPNks5wVpL_mJzWJ9v_OpK4Qv4_Z9t1KqyOQnfSPqwz2oXKi9vaA5fOoMMyGUUCIFYXSdM_dl861srrhscsMkBJOrPQmohQvNkBOEarNKmx50RuQvXK6l3nOvwglOCrxbIi5xokxGdG8Dc4p7ejjcj3EkbSwSx9_uU-xgcRYiX4XNy2k5M4YJNhUD7GQju_Xvmz-DvLkDgi5S_BvFc5jAxHJH_Hrs4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني: صواريخ إيرانية جاهزة للإطلاق الفوري في حال رد إسرائيلي. إن كمية مناسبة من الصواريخ الإيرانية جاهزة الآن للإطلاق الفوري على قائمة أوسع من الأهداف في الأراضي المحتلة في حال رد الكيان الصهيوني على إيران. إذا ردت إسرائيل، فستكون الجولة القادمة…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77537" target="_blank">📅 05:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy1rjdjQxC_9FmGhhyFA5WN-WxDe4glAlgteaJHCbFm6AaKozMkbXHPBdLBmKsG8OW9hEZgMXq25KJJm93tthdbrs92-SKThMj4XaVjEfhmW9h8t_H_ay0S917-NA0fBM4AK7kI5ZRaT5HybpOp6Dh4MbiEDdFiefDSw8SqZGy0ic_zPjTYT28yMqZl5WnaKcXbbhog-mH18wwJShAuhR7a9FVHzECJOoCLaQJFLcjsiqF68R3bm-TC7QMqkehp84m0wZySxQUMnohrDVatw0wZ3L8k9Ko4acWuvwR03U6AVRPW-jUqNMzgK_zB6_qN1D2jAddb0YncvSLAEJaiweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3 انفجارات في اصفهان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77536" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">إعلام العدو: سلاح الجو الإسرائيلي استهدف أكثر من 10 مواقع بما في ذلك أنظمة دفاع جوي وصواريخ باليستية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77535" target="_blank">📅 05:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الحرس الثوري الإيراني: أن العدو الصهيوني هاجم أهدافًا على أراضينا باستخدام صواريخ باليستية تُطلق من الجو.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77534" target="_blank">📅 05:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">لايوجد عدوان على مدينة شيراز حتى الان.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/77533" target="_blank">📅 05:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الاصوات التي تسمع في سماء المدن العراقية نتيجة عملية إطلاق صواريخ نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77532" target="_blank">📅 05:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مشاهد متداولة لانفجار في اصفهان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77531" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الاصوات التي تسمع في سماء المدن العراقية نتيجة عملية إطلاق صواريخ نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77530" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
