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
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
القيادة المركزية لمقر خاتم الأنبياء المركزي يعلن وقف عمليات القوات المسلحة
في أعقاب الاعتداءات والأعمال العدوانية التي نفذها الكيان الصهيوني في جنوب لبنان ومنطقة الضاحية، بدعم من الولايات المتحدة، قامت القوات المسلحة القوية التابعة للجمهورية الإسلامية الإيرانية، في إطار دعم الشعب اللبناني المظلوم، بتوجيه رد مؤلم لهذا الكيان.
ردٌّ كان ينبغي للكيان الصهيوني وحلفائه أن يستخلصوا منه العِبر والدروس.
وبناءً على ذلك، يُعلن وقف عمليات القوات المسلحة؛ مع التأكيد على أنه في حال استمرار الاعتداءات والأعمال العدوانية، بما في ذلك في جنوب لبنان، فإن إجراءات أشد وأقسى وأكثر حسمًا من السابق ستكون في الطريق.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/naya_foriraq/77726" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📰
أكسيوس عن مسؤول أمريكي:
واشنطن لم توافق على الضربات الإسرائيلية على إيران وأبلغت نتنياهو بضرورة إنهائها</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/77725" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اعلام العدو:
إسرائيل والولايات المتحدة أرسلتا رسالة لإيران: لن تكون هناك هجمات أخرى إذا لم تطلق إيران النار مجددًا</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/77724" target="_blank">📅 14:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئيس الوزراء البريطاني ‏ستارمر: على جميع الأطراف العودة إلى وقف النار، يجب منح المفاوضات بين أميركا وإيران فرصة للنجاح من أجل سلام دائم</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/77723" target="_blank">📅 14:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴‍☠️
🇺🇸
السفير الأميركي في لبنان:
إذا أوقف الحزب هجومه على إسرائيل فهي لن تستهدف الضاحية</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/naya_foriraq/77722" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
النائب الأول لرئيس البرلمان العراقي يدعو الحكومة إلى وقف تحويل الأموال لإقليم كردستان لحين إجراء التسوية الكاملة للمستحقات</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/naya_foriraq/77721" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
وزير التربية والتعليم الإسرائيلي:
استمرار تعطيل المدارس غدا الثلاثاء.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/77720" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ما يسمى بـ"المدير العام للوكالة الدولية للطاقة الذرية رفائيل غروسي": المطلوب من إيران الوفاء بتعهداتها والامتناع عن النشاطات غير المشروعة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77719" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عضو الكابينت زئيف إلكين:
ترامب يريد الهدوء، لكنه يدرك أننا لن نقف مكتوفي الأيدي إذا واصلت إيران مهاجمتنا</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77718" target="_blank">📅 14:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff9HcZ1HdWyRXAZOdxOKwqmqmQsGuwFPdgH7Yj8YG4yr4h38j0t1NLbZ2qaMOnnoUoivQdCZ0sqs3Nyl1rj1k8oDutDValkWJ-KGSBm9G9HWlWRgn57IOSaUF6uoeejAdhK6b7oQcnysJxLSjrM54j0Fgi7UfSTTLh90Q06-sVgdkbqXoqKXr0k2U8cPzkYmVGo_vgQzMW9h7vPrhqScBPyY0-95_mOTgBWvWXPu06lwLY8-rbmfiOabef0x1BMstrwawP2D8JRgSpWCXGbluhJCcG2IzvDeakxAJqVeB7GwzdDIeYGpx0CJp4EVSvfFgNOHrziuwfaihMhwS1nYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: يسعى كلا الجانبين، إسرائيل وإيران، إلى وقف فوري لإطلاق النار! المفاوضات النهائية بشأن "السلام" جارية، مع مراعاة احتمال عرقلة الجهل أو الغباء لها. سيظل الحصار قائمًا، وبكامل قوته وفعاليته، حتى يتم التوصل إلى "اتفاق نهائي". يجب أن تسير الأمور بسرعة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77717" target="_blank">📅 14:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">المتحدث باسم جيش العدو: النظام الإيراني يحمي وكلاءه في لبنان</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77716" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نقلا عن إعلام العدو ستجتمع الحكومة الصهيونية هذا المساء في الساعة التاسعة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77715" target="_blank">📅 13:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حركة حماس:
نثمن عالياً الرد الإيراني واليمني على الكيان الصهيوني جرّاء جرائمه بحق لبنان وشعبه.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77714" target="_blank">📅 13:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">إذاعة جيش العدو:
منذ حوالي الساعة 7:00 صباحًا، لا توجد معلومات عن هجمات أخرى نفذت في إيران خلال الست ساعات الماضية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77713" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77712" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f3eaf5f3.mp4?token=j_-IRLVguDIFv0rWGruRTDoa4EWssCPZThlaGUF3_foMadculLl23QiXhUbL159hbfBQwNW9JUza5lenOOGPRu2Bub-4eS7yfIYYyRNYOQ2bMieh4QQTP9kUO6CA-V_n5YhXxeiuPBFLm1hQ2jfRFYPSGz_sojEGJ9j36AHYXqDrq5b4S-SmUHvwmazx9fDZfOjynewHw3HyWMfgUUXavlgTGbisD_3M9-731ixLdB8hUkijTgmprO68vTkoNppP9kuHX1qYDreeD5WKsSP96CWD103yT5DLtI4fbIrdza6_ecE76P5vBvfa7YTtmqNw7hcRZLQFZNfQtEVjINNz5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f3eaf5f3.mp4?token=j_-IRLVguDIFv0rWGruRTDoa4EWssCPZThlaGUF3_foMadculLl23QiXhUbL159hbfBQwNW9JUza5lenOOGPRu2Bub-4eS7yfIYYyRNYOQ2bMieh4QQTP9kUO6CA-V_n5YhXxeiuPBFLm1hQ2jfRFYPSGz_sojEGJ9j36AHYXqDrq5b4S-SmUHvwmazx9fDZfOjynewHw3HyWMfgUUXavlgTGbisD_3M9-731ixLdB8hUkijTgmprO68vTkoNppP9kuHX1qYDreeD5WKsSP96CWD103yT5DLtI4fbIrdza6_ecE76P5vBvfa7YTtmqNw7hcRZLQFZNfQtEVjINNz5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لبنان لن يصبح لقمة سائغة للصهيونية أبدا وأبدا
الإمام الشهيد القائد علي الخامنئي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77711" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77710">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دك سفينة هندية بمسيرة قبالة بحر العرب</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77710" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77709" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">المتحدث باسم مقر خاتم الانبياء:
- كما وعدنا، أثبتت القوات المسلحة الإيرانية الجبارة، بما فيها الحرس الثوري الإسلامي وجيش الجمهورية الإسلامية الإيرانية، أنها في ذروة استعداداتها الدفاعية والهجومية، تحركت بسرعة ودقة، مما جعل العدوين الأمريكي والصهيوني يندمان على ما فعلاه.
- في الموجة الجديدة من العمليات ضد أهداف مهمة وحساسة في الأراضي المحتلة، تلقى العدو ضربة قاضية من القوات الإيرانية الجبارة، حيث سددت ضربات قوية وموجهة وذكية ومدمرة.
- على أمريكا المجرمة والكيان الصهيوني الوحشي أن يعلما أن إيران قوية شامخة، وأن قوى المقاومة الشريفة في المنطقة ستصمد في وجه أي ظرف وأي تهديد، ولن تستسلم أبدًا للأعداء المهزومين، وإذا استمر العدوان والشر، فسيكون الرد أشد قسوة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77708" target="_blank">📅 13:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odxl-FBjdMCBjHadfg6jbG7vge90_6A5xVWKbQDGv9s1pGiJBajSDlEo06pTVckMuxdvz4WRGP9VkVDNhL0B0bOKwZb2Dz-Ir7z6ft70Pyf8HvQCBUwClrtT6ngbtUDzEEdEAfw7_20dNXoKWtb3l2MNW3m5RbWk67jmEJfLJg73Rh5qMxuiTZ9ceqwBL82jy1Ogybh_TxqCyjHFaMDt0rR5tYCdaQ-9SkLvoatExONb-iySouWAG96KD3BCc5Kd9h3073Q2m2ApsGCLwkie3kR9Po5NBVpswhp9IZUlaK-0eSRF6Gf_PD2XvIBYpC-Rw374Denqdh36EV4FXomy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Bab Al mandab are close soon</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77707" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77706">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR2tKVcrR-J89lkK1yKZYjoQ4WM900BEER1Ec9CgoVZNBAUVlyU7Jn6GK5_bOPQ06VFmhT3gUgHL2V3_mdaJpCnpPiBQE402w4-OTBx7XHDIrkmg17G6_YGKVanftMp5fywATWkY3GMKmr6J3JrxU8U7sAOdoUi13j8RkQg3Dp5TL--OGalZht2vlXIoyGVcLnX5LI18YP1rZVzweFBy7NtBwdqswmbhZpn4VTuCLJcqdokikvck0D2slw8qujBWPxYW6p1dWTrxYNSHx1H9VkNL0OsUA_h0166OAZnF1mUaZZBvEqgZno0NbCBLFI2osDTGWddNRncxei1ku3-kDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
التخوف حاليا في ايران ودوائر القرار العسكري هو إذا ما قرر الجيش الكويتي الدخول بالحرب .</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77706" target="_blank">📅 13:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77705">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
القائم بأعمال وزارة الدفاع الايرانية:
الكيان الصهيوني بات اليوم أقرب من أي وقت مضى إلى الأفول والانهيار، لن نتراجع لحظة واحدة عن مسار الدفاع عن مصالح البلاد وأمنها حتى معاقبة المعتدي</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77705" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77704">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60051ef060.mp4?token=Xt4oNXi-aXYLUyBFhjAYid1_NUgJNq6AWGb0xFYqqyBvkd2GqjG1f7nRCPp2797E4H5tIP4yd0R9eA9s5qkMtz7VUHIqH2Pcd_-vsHE0kcDz_vL9igN4qxVsY30CxOoU7XM00TsAZIlTjyOKgumaLA8SYLNL6gAH6CV0CKu1-mbJWIzLiYgD0VjeV1xgZHkgCAgvWCh4kwK0b4VHppRyymqZuxxXmZAA7WN8tLh7pz4bHxk1DzklDzzdgdi7uD5L2R723ZExiTcgSeiheeObQK9MY4NDJGbtUWiaBJLTOPMvUInzuQX9FO2ltFp9hk8MncldGk3amHrAcd3XvuNCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60051ef060.mp4?token=Xt4oNXi-aXYLUyBFhjAYid1_NUgJNq6AWGb0xFYqqyBvkd2GqjG1f7nRCPp2797E4H5tIP4yd0R9eA9s5qkMtz7VUHIqH2Pcd_-vsHE0kcDz_vL9igN4qxVsY30CxOoU7XM00TsAZIlTjyOKgumaLA8SYLNL6gAH6CV0CKu1-mbJWIzLiYgD0VjeV1xgZHkgCAgvWCh4kwK0b4VHppRyymqZuxxXmZAA7WN8tLh7pz4bHxk1DzklDzzdgdi7uD5L2R723ZExiTcgSeiheeObQK9MY4NDJGbtUWiaBJLTOPMvUInzuQX9FO2ltFp9hk8MncldGk3amHrAcd3XvuNCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">48 ساعة لم يطلق حزب الله اي صاروخ او مسيرة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77704" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77703">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تدمير طائرة مسيّرة معادية غرب طهران</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77703" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnPfX9udDqCXQN5-_BA93Wi-Vi2aTO4wi5TiyDqVVw5KMUJMWJ9BxKe0CcoXdbnxw_TyXNm6LDPrM3yJPIaJpaDZC92dgkreuihItPtzDSmnfpBau3OnQU4Sdw6R50njoAVzYV8jbscubMjJnlNhLn0TC3xzMkT8DSLB0__wH3L3dc8rIG_j90Vp14YU2nOhZJ8uryTqRZhmEcKlSZj0ESaxQuCYPLWTNQWJc92YoEmI2Gt4bmppzHc4WRNgRUBAlbhl66pSBkeWuoivcHqrUcRE_t5einQiBhLgi7EQVQpmSHZfQiwUP1FBnZ22F8GRSog1GD_r556tsW2GlC-zgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب : يجب وقف إطلاق النار فورا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77702" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77701">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مسؤول أمني إيراني: تصريحات ترامب حول عدم مشاركة أميركا بالهجوم الصهيوني على إيران لا تتوافق مع الحقائق المعروفة</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77701" target="_blank">📅 12:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77700">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مروحيات أردنية تحلق في اجواء شمال الأردن استعداداً للتصدي لاي مسيرات ايرانية تقترب من الأجواء وتحاول مهاجمة اسرائيل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77700" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مسؤول أمني إيراني: تصريحات ترامب حول عدم مشاركة أميركا بالهجوم الصهيوني على إيران لا تتوافق مع الحقائق المعروفة</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77699" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">يبدو ان أخلاق العرب والمسلمين المبنية على نصرة المظلوم و الوقوف بوجه الحاكم الظالم فقط لدى ايران الصفوية وعراق الرافضة ولبنان شيعة جبل عامل وانصار الله في اليمن …</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/77698" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جيش العدو:
قد تنضم الجماعات الوكيلة في العراق إلى الحرب.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77696" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏴‍☠️
جيش العدو يوجّه تعليمات للصحفيين العسكريين: الاستعداد لعدة أيام من القتال على الأقل.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77695" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
وكالة فارس:
إيران استخدمت في هجماتها الليلة الماضية على شمال الأراضي المحتلة صواريخ من الجيل الأخير من نوع خيبرشكن. تصل سرعة هذا النوع من الصواريخ الباليستية أثناء الغوص إلى حوالي 9 ماخ، مما يجعل تدميرها بواسطة أنظمة باهظة الثمن مثل نظام تاد وبيكان أمراً صعباً للغاية. تم استخدام مزيج من صواريخ عماد، قدر إف، وخيبرشكن في هجمات إيران يوم الاثنين.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77694" target="_blank">📅 12:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
جيش العدو الصهيوني:
من
وجهة نظرنا نحن في استمرار لعملية زئير الأسد - في يومها الثاني والأربعين، بعد توقف دام شهرين. لدينا فرصة لتعزيز الإنجازات. ليس لدينا معادلات. الإيرانيون يحاولون تقييدنا بمعادلات - لكننا لن نسمح لهم بخلق واقع جديد في الشرق الأوسط، عندما تتاح فرص للهجوم في الضاحية في بيروت - ستُستغل هذه الفرص</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77693" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77692">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شركة Wizz تعلن عن إلغاء جميع الرحلات إلى إسرائيل على الأقل حتى الغد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77692" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">إسقاط عدد من المسيرات الصهيونية في سماء طهران</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/77691" target="_blank">📅 12:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3T_UIcDi3goGbaSQxYPJ-Lujh_RLsjpZrpv_M5xbJ6JKwIz7pzg_Mc1O91LUXxRzQZABxkNUo8zO4RAuepOWMfAmaTM57zOqAn742eKoEyoJ0Sl1JcZoTwmmW80fruCTNhWp6fANxWoVzvh3TU_wkdMI5RQD8EMta_oZP5w1gp8BgDBjOrqi60-uNXMk9_oJ6jEXF6_uwC1bFLHTcGB9HMeVovlONr3_rpmtSfFacf_Wil3Zth3T0HGhBNfSrHJKZCK2X6Sqkm_OF2TAVQ2A7tJhXa9HHzSGIc-1_5desuAZaDtw2FjqLRaVlw6FNZzHtHymvHL6WN5cNvJnqjGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسقاط عدد من المسيرات الصهيونية في سماء طهران</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/77690" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">"
⭐️
If you have a verified Telegram account with a blue checkmark, we kindly ask you, our esteemed subscriber, to support our channel by promoting the link and sharing updates on the channel."
في حالة تمتلك حساب تلغرام موثق بالعلامة الزرقاء نطلب منكم عزيزنا المشترك دعم رابط قناتنا بعمل تعزيز لغرض نشر حالات على القناة
⭐️
https://t.me/boost/naya_foriraq</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77689" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c63c93fb.mp4?token=oq338G26J8JFUZZODnpwFju9qnQerRX9wrPndb9MjJAxmerapL4EAizQWuL-Y_CQwNxfpn8uP4s1R94Y5vy4v7XQb67NFAVXrZrTTRLywjIcbm6hWug4YFgexysZzUMnLmXjEfy2Hou_Kyib8kiPtiX-r_FeMRkGMqtgTk9nK0xL4bGQXDL8puveR-hTz5gEx4KKU2VuZ1WNuqU9XlKNWQk2m7Ojq0NqAQYnuuMaThmaHHH0Gx5Vx6gnNfRPBCnMhq1yN6KJ1OOXS0ZwErqImV9lltdjkLw8bsKCNb5fg8MzB11oLEVYH5P8cmxtrsWa0oiDmkiGV0d3aAVZrML-Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c63c93fb.mp4?token=oq338G26J8JFUZZODnpwFju9qnQerRX9wrPndb9MjJAxmerapL4EAizQWuL-Y_CQwNxfpn8uP4s1R94Y5vy4v7XQb67NFAVXrZrTTRLywjIcbm6hWug4YFgexysZzUMnLmXjEfy2Hou_Kyib8kiPtiX-r_FeMRkGMqtgTk9nK0xL4bGQXDL8puveR-hTz5gEx4KKU2VuZ1WNuqU9XlKNWQk2m7Ojq0NqAQYnuuMaThmaHHH0Gx5Vx6gnNfRPBCnMhq1yN6KJ1OOXS0ZwErqImV9lltdjkLw8bsKCNb5fg8MzB11oLEVYH5P8cmxtrsWa0oiDmkiGV0d3aAVZrML-Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إسقاط عدد من المسيرات الصهيونية في سماء طهران</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/77688" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77687">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عدوان صهيوني على كرج وطهران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/77687" target="_blank">📅 12:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الهند تنصح رعاياها بمغادرة إيران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/77686" target="_blank">📅 11:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77685">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">إعلام العدو: ‏استهداف مطار شيراز</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/77685" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77684">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هجوم على نقطة تفتيش للباسيج في كبودهارهنك بمحافظة همدان غربي إيران.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/77684" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77683">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">إسقاط مسيرة صهيونية في طهران</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/77683" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77681">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c3d2c5467.mp4?token=N3XbBoaT5J11LTUp28Al9dD24W88WruXu783h7z8tEDyp3LLt59RCvnnt3eTz0RH_hWvwSjceJyQq7lTknV9Pfnbbb3bBzKeQKW4TlrddYY_8o5XiqqamNue7iWi4qndHYGFj63gHWQJiOwGI6xVqdp2sc753jCexJFm7RvCXDE7NqVbV1vxV9GRX4uICLsRKlwjDxDWKt_548j5V8ff14HEVtFinywYDNbR_ANwgLiOODVc_mx1wQZxBupJoHZHmezO693RXa0J17XJU9izjqFZipW65AJnAvdLbNSZD-6NCZYH8GMq8YHdzbUFEjwjnfkPPYs5Z6nlhoVxmoalxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c3d2c5467.mp4?token=N3XbBoaT5J11LTUp28Al9dD24W88WruXu783h7z8tEDyp3LLt59RCvnnt3eTz0RH_hWvwSjceJyQq7lTknV9Pfnbbb3bBzKeQKW4TlrddYY_8o5XiqqamNue7iWi4qndHYGFj63gHWQJiOwGI6xVqdp2sc753jCexJFm7RvCXDE7NqVbV1vxV9GRX4uICLsRKlwjDxDWKt_548j5V8ff14HEVtFinywYDNbR_ANwgLiOODVc_mx1wQZxBupJoHZHmezO693RXa0J17XJU9izjqFZipW65AJnAvdLbNSZD-6NCZYH8GMq8YHdzbUFEjwjnfkPPYs5Z6nlhoVxmoalxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في أصفهان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/77681" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تفعيل الدفاعات الجوية في طهران</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/77680" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوي انفجارات في أصفهان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/77679" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">إطلاق مسيرات من اليمن باتجاه الكيان المحتل</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/77678" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الدفاعات الصهيونية تسقط صاروخ إيراني في محيط قرية زبيدة بريف القنيطرة السورية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/77677" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b3165a7b.mp4?token=s4phfFDbAxNh1TKcvYjtQvaHffmgwEVkQu3YZfvXLcPG0KK2ZyIQL8DoM7EmN_-BBwGy1nsKGUFGqfGEuv4WD9y4yPNsDSqaRgIIp4JuLBP5MrEgNRc_0EEV4jS572DvniG7DqYbMkwAEFvuPz9YE2qx8CveU4SqYcLm_kGu1NqWuZcEhT3JA4jT2mPioKrFHV4my8gVkRODKQRifXN9_q9hgJjQFiSXMSGiQHk5W2oPdHpWmncWeGDi82bUqJrEjnojwsLTFxR1O8HsZYe3EzBAsAWotPXbxs3x0_HW8wy5hSTpxTL77Rs0tUojVJtG1xLm690pJTpN3idxgtV3Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b3165a7b.mp4?token=s4phfFDbAxNh1TKcvYjtQvaHffmgwEVkQu3YZfvXLcPG0KK2ZyIQL8DoM7EmN_-BBwGy1nsKGUFGqfGEuv4WD9y4yPNsDSqaRgIIp4JuLBP5MrEgNRc_0EEV4jS572DvniG7DqYbMkwAEFvuPz9YE2qx8CveU4SqYcLm_kGu1NqWuZcEhT3JA4jT2mPioKrFHV4my8gVkRODKQRifXN9_q9hgJjQFiSXMSGiQHk5W2oPdHpWmncWeGDi82bUqJrEjnojwsLTFxR1O8HsZYe3EzBAsAWotPXbxs3x0_HW8wy5hSTpxTL77Rs0tUojVJtG1xLm690pJTpN3idxgtV3Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في أصفهان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/77676" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تفعيل الدفاعات الجوية في طهران</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/77675" target="_blank">📅 11:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmMSVyfWggyztOPSjb5Hz1mPECa5YjjmmwxFHUoFbhj-92VejAn1EQrxKhhAg5_yFqkWN0YoBVwW3bhR8Tt2wUETpLU3nn9NfW-Oi7GkpylQfoDaEdgPEvPh0gQ7ur94q9gAADkh_7uhv8lnUPV5QKkb5p9ahjIqKrp1YEtbKhBR9nbg8EeUNemF2eiUoNTn9-jY7kd2EYxdlSg0YGpiMUedf7D3mgJUSpGw-V1ufjhieYPCKZ8YOJps37U4GVagDuxowdhG1ToixqYFX7_kAqe3HrjNJXjC_E34yBhcQ1b39RdTCkO80L-SJHJkDTEqvdxJn8twKKSeIsyis8nuvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الجوية في طهران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77674" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏مكتب نتنياهو: لن نقبل بمحاولة فرض النظام الإيراني معادلة جديدة</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77673" target="_blank">📅 11:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">المتحدث باسم وزارة الخارجية الإيرانية: ردا على التقرير الكاذب الذي زعم استهداف إيران للمملكة العربية السعودية،  "قواتنا المسلحة تُعلن بوضوح عن أي هدف تهاجمه. لم نُصدر أي بيان بهذا الشأن. لطالما حذّرنا من عمليات التضليل."</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/77672" target="_blank">📅 11:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تفجير حافلة مبيت لإرهابي الجولاني في مدينة إدلب السورية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/77671" target="_blank">📅 11:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصادر: بدء تحميل الناقلة HELGA بمليوني برميل من النفط الخام عبر ميناء البصرة النفطي</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/77670" target="_blank">📅 11:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">العلاقات العامة للحرس الثوري الإيراني:
بعون الله تعالى، ردّ مقاتلو القوات الجوية للحرس الثوري الإسلامي، ردًا على عدوان العدو الصهيوني الأمريكي على إحدى الصناعات البتروكيماوية، شنّوا هجومًا صاروخيًا على صناعات مماثلة في حيفا قبل دقائق.
نحذر: إنّ العدو الصهيوني، باستهدافه أهدافًا مدنية وصناعات نفطية، قد بدأ لعبة خطيرة، سيشمل نطاقها جميع أهداف الطاقة في المنطقة، وعواقبها على الاقتصاد العالمي تقع على عاتق أمريكا، المحرض الرئيسي في هذا المجال.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/77669" target="_blank">📅 11:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مصدر من الحرس الثوري لنايا   تم اطلاق ٨٣ صاروخ و عدد من المسيرات على شمال فلسطين المحتلة استهدف مطار رامات داويد و عدة نقاط في الجولان و الجليل</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/77668" target="_blank">📅 11:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77667">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">المتحدث باسم الخارجية الإيرانية: الحديث عن مصادرة أصول إيران يندرج في إطار الحرب النفسية والدعائية وهي مزاعم مضحكة ولا يمكن القبول بها</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77667" target="_blank">📅 11:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77666">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصدر من الحرس الثوري لنايا
تم اطلاق ٨٣ صاروخ و عدد من المسيرات على شمال فلسطين المحتلة استهدف مطار رامات داويد و عدة نقاط في الجولان و الجليل</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/77666" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr5lD3dkIB4o3Ig8YhG7pLk1Ks0wkYAyWBCk-sHyG24-gR67OKTDhzIV2pVSdHZN70S5jXRxvWTz3UGi-ZTdo6tyLFQ1Eydadbr5wFaFFxCrPzGduVDFP6UHbVLLTc9KOivcCfrERilN_R2PA7bNvpddScF-KyrQCfgYUuyr-g8vOv4BwsJmGQpO0QQKFyjZX8aCDK2a-msNKhM7X6ffhgXgPXZSKzxBB7uWQud3JPW327uU6Nz5N1ZK2_gW2Ixz2rbeJ4qK9ms0CYUM7UBykM_21JRTCI4exFvPJsSF_SF-wh_XV7MGrhubpNgzAxX3lMQx6uAx5-pKXLr7rZ5BSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إيلون ماسك حول إيران: من المثير للاهتمام أن تعرف أن اسم مضيق هرمز مأخوذ من أهورامزدا، الديانة الزرادشت</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/77665" target="_blank">📅 10:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">إعلام العدو ؛ سمح بالنشر :
سقط صاروخين شمال البلاد
لا يسمح بنشر مكان وتفاصيل أخرى</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/77664" target="_blank">📅 10:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إطلاق جديد من إيران نحو الكيان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/77663" target="_blank">📅 10:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbiD84tf76OswnootKD_tq3fvUqBNZ8rWqPQ2mJEk9dOkwJRH-3t9gu_bEtX56mQCPGGGd66HhT06yYv6q7_UULVg7mAkWIEsyqMSEtxRwtcpOmKFZPg80tpEebj3ffdlIpOafkTX1_G0DF7ANZn_mfqmuMlwpUgo6VTnBPUYYJTK3xiKB3Q6eS6plmbNLB2fJhFoTAsJKU5idHn_IYexLdEZM1twlsi17JncuVS1143xuTpQ614DM20kLT_9DnrhRK1_gyjSmPsyQPcrhxvu8xF2w4IYZ9BWK6FHNvIm8IzYDzetXiaNcvrU67OrVZh_6UYepsanUXyOdE-FC7qxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخطوطة الشهيد موسوي حول مصير الكيان الصهيوني نُشرت لأول مرة
الكيان الصهيوني يتخبط في مستنقع الانحدار. لقد بنى أمنه على انعدام أمن الآخرين.
لقد جاء إلى هنا لتعزيز أمنه عن طريق نقل انعدام الأمن. دخان هذا الفعل يملأ عيون من أُجبروا على قبوله.
سيندمون على ذلك يوماً ما، ونأمل ألا يكون الوقت قد فات.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/77662" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏تعليق جميع الرحلات في طهران حتى إشعار آخر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77661" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayhHAi9qw2Rbh66vR1WlSioZ-HKDxC9Tl9Qw0Y72wdOARSB5AQUNnU8SAxfbcwWtzq2AMn923bOANeQJMnXbSqN_NTOA8KAmsBcWeNACxr82Bm9CCW8NnzBUFW8VUVEXH5w_pYQkxrDzKmMl3llZRugxDMKYGfDn3-XFB54vrGseYAbn1SOWE_v39Lb1HdwDIZaA8VlCQl5LR1aoUj386O8VSn-MMmmz7C8OohXTwu70rTHCp1kqYllBgBSG2n9i1Gr9XBwAxTwPkjpQCmqP1LyrlJeh8lC6dlSbFXREdPMscNg2panyppzePiR460oyFcrFllDa67oF6YgJqAYBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماء تل أبيب بفعل الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77660" target="_blank">📅 10:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏الاتحاد الأوروبي: سنطبق اليوم عقوبات على إيران لعرقلتها حرية الملاحة</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/77659" target="_blank">📅 10:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">المتحدث باسم لجنة الأمن القومي في مجلس الشورى: مستعدون للرد وقوةُ جاهزيتنا تفوق ما كانت عليه في 28 فبراير ولن نصمت حتى اللحظة التي يندم فيها العدو</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/77658" target="_blank">📅 10:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616a50f56.mp4?token=WSE54zmdAVDxgDH0aQlHyNFJgIJjzE_gMDdauZ8DXO-_Jjwpd4GZoxyYqjdGOxm87tOHJHI6zrBQ0YG3swOSXkVJAVHLSCIK0h6DC1qneohpqiolyq7pd16iyQ-wuS7PvHwR5EYGHrkTDDhBqjetie4CSxdeDpbIefcXVd83VhXXOGK6DRxuv67U8UpeTosqWwxAxE4EQLZ83D3luNsaof3DWPPkgA_XbgPxeMZnGCK-ZhzslXqRjFj5LpQA-9_uJXxP9HJ72HFk2kEQVgzlhR6ADP1F-yv_SYbqW3fGJVkPPnouKJRkDXoX5u0j70Sb0Bb34ZDGOHnrxS0exKpMSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616a50f56.mp4?token=WSE54zmdAVDxgDH0aQlHyNFJgIJjzE_gMDdauZ8DXO-_Jjwpd4GZoxyYqjdGOxm87tOHJHI6zrBQ0YG3swOSXkVJAVHLSCIK0h6DC1qneohpqiolyq7pd16iyQ-wuS7PvHwR5EYGHrkTDDhBqjetie4CSxdeDpbIefcXVd83VhXXOGK6DRxuv67U8UpeTosqWwxAxE4EQLZ83D3luNsaof3DWPPkgA_XbgPxeMZnGCK-ZhzslXqRjFj5LpQA-9_uJXxP9HJ72HFk2kEQVgzlhR6ADP1F-yv_SYbqW3fGJVkPPnouKJRkDXoX5u0j70Sb0Bb34ZDGOHnrxS0exKpMSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الشباب بجبشيت لما يسمعوا رشقة من ايران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77657" target="_blank">📅 10:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">منظمة الطيران المدني الإيرانية: إغلاق جميع المطارات في غرب البلاد حتى إشعار آخر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77656" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75e1beecc.mp4?token=jRm8CSaBqIkam1THyvAtF2lN5QULd5Dj_UeNUPvuXaXqmOSr5fNo_sD0d4uJv8582otAb7hC1p9cNx5sdiNhJ2N_riapdu0MqIvKm8n3pHZGgB0FBSGUsC2eFS7DQbSOsYqEZViDN9RPZxpzqguiZhRKGN1VI6SkBcp_uAGk5yl1pupDGWpDXRS9Q4tStys79xbAzqMk70vRkk0L4BeczO_6V5nw4gRwiYIZlxhoGj6cvPz2LopoF29WExoPO3RMZJJlkogt3hGoSmEUcUaKNQXDT0VMJXNQy00U3QSpf17MT2xvaJsMyuafTCRAkBqIUuLbYzUkJPGzMwlcF2GEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75e1beecc.mp4?token=jRm8CSaBqIkam1THyvAtF2lN5QULd5Dj_UeNUPvuXaXqmOSr5fNo_sD0d4uJv8582otAb7hC1p9cNx5sdiNhJ2N_riapdu0MqIvKm8n3pHZGgB0FBSGUsC2eFS7DQbSOsYqEZViDN9RPZxpzqguiZhRKGN1VI6SkBcp_uAGk5yl1pupDGWpDXRS9Q4tStys79xbAzqMk70vRkk0L4BeczO_6V5nw4gRwiYIZlxhoGj6cvPz2LopoF29WExoPO3RMZJJlkogt3hGoSmEUcUaKNQXDT0VMJXNQy00U3QSpf17MT2xvaJsMyuafTCRAkBqIUuLbYzUkJPGzMwlcF2GEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء تل أبيب بفعل الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/77655" target="_blank">📅 10:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAV_NvZgB7Xu0P0ua9mD9NeAqmxlwO6TX54VoYXuGzJBiy_hWm_3thu4p2hZpvCBfX4VOzyf_T1zc66ZikiGsr3qkSu8CZavFk_i2A1Xvo3SnvuCcjGJ62dqT57kwNnOJslGL9rSu-TtKtPxJHESJL3jPLFfsKn22iuc04VCYIRlx4daViMhM01gk_c4g6KS0aq9usaXwO95bPI4zNC5P00MPsRE07mGYk38cA_x1rB_Z4IBvy_fO5PFKtKhdO4Dcj4WzSb95tGGjyIwoRgETrOw5LeSuyhmZh9AiKaDPCRUbHyjDhaoCoHEfzSx1ogpwTyfoXxmcf6rpV6tFGq7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران في مطار تل ابيب بسبب القصف الإيراني …</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77654" target="_blank">📅 10:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">طائرة جناح صهيون تستعد للمغادرة خشية استهدافها</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77653" target="_blank">📅 10:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/880c2daf2a.mp4?token=X4UPPFIaMhqPY7zz3MF5pn5LUHYNXF42eYCdmKUbDDazxHPg5PKBpBE0ZupuD-AmRlrdATm9BL9Vosks9fmyj49WzBPvsYFsagBJ3TEfRh0JOWyg4sGiU9ZTTuDGhNArcbXLtehOI2oq2yjp2DmEAZZ4gEd2tpYF5-tRF1FS3caHf9UQnaZwBh7RVoeHyG91CZAPazBtdVJPDkMkCd8Gkrnx_GdfDvQ7p8OO_1bFVfi8CtUmBtNYyevmRq_w4eL0BZonGUUc49LXJXOfBfO98huY6BM-K_0eCHE34T2xRwG-33sf3vtn_AQMj7b3TpUw3lrREevaEYTeqFGkwmMZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/880c2daf2a.mp4?token=X4UPPFIaMhqPY7zz3MF5pn5LUHYNXF42eYCdmKUbDDazxHPg5PKBpBE0ZupuD-AmRlrdATm9BL9Vosks9fmyj49WzBPvsYFsagBJ3TEfRh0JOWyg4sGiU9ZTTuDGhNArcbXLtehOI2oq2yjp2DmEAZZ4gEd2tpYF5-tRF1FS3caHf9UQnaZwBh7RVoeHyG91CZAPazBtdVJPDkMkCd8Gkrnx_GdfDvQ7p8OO_1bFVfi8CtUmBtNYyevmRq_w4eL0BZonGUUc49LXJXOfBfO98huY6BM-K_0eCHE34T2xRwG-33sf3vtn_AQMj7b3TpUw3lrREevaEYTeqFGkwmMZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إخلاء ركاب من طائرة إل عال أثناء إنذارات في مطار بن غوريون</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77652" target="_blank">📅 10:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8663b96e.mp4?token=eVs96wMOR07jNfJpXpe_yckunQ5yEzxKe066C9T1J2aEqQnBGJWdPIY9S6FwtBNLQ32zKUxF95UIkFD4BbxNKRWpb_axdM0_OujXBnduJcRfc9UHypT-f62Z6qGkFwzQDXTImJwDjNNRo9w86noVDLLT9IzAg7AmTUaUwJwQ3tsZrkowMPMkLTeH6hBlQudko-nHj3tQbtAq_7-waSa7m2YqJcIYfTuiRAR1oalFONdn4rjbhaQ6Q9tY4R-5TOP7kn3Ewo6qoqgZQzbOhH_rK5svnoEqbUP3w0FMp5C2wQ0gfR1W0rRwH_kLFHJnbUnUXfi4EYzsab8TQHxS_cnELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8663b96e.mp4?token=eVs96wMOR07jNfJpXpe_yckunQ5yEzxKe066C9T1J2aEqQnBGJWdPIY9S6FwtBNLQ32zKUxF95UIkFD4BbxNKRWpb_axdM0_OujXBnduJcRfc9UHypT-f62Z6qGkFwzQDXTImJwDjNNRo9w86noVDLLT9IzAg7AmTUaUwJwQ3tsZrkowMPMkLTeH6hBlQudko-nHj3tQbtAq_7-waSa7m2YqJcIYfTuiRAR1oalFONdn4rjbhaQ6Q9tY4R-5TOP7kn3Ewo6qoqgZQzbOhH_rK5svnoEqbUP3w0FMp5C2wQ0gfR1W0rRwH_kLFHJnbUnUXfi4EYzsab8TQHxS_cnELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء بيت شيميش</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/77651" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZzW_NDLaFXj969nKeXA1NMZ3F5ycPGeKLqj-ttIYVOng8PXMy2aUlMebS4cDfRLQxFDvJjG_FCp4Bl1zt_jL6iJdCCU9oknjbwZkANbOyo_6B5wGYjren3tsrHrrsa8Y6uruInpqEQZeccjI0ZaU6ubFxCRxCwTibH2g-0PqXxXUtdXSHvxnC_MNE2ir-UG0SbogWc_NiXmWB90NLKwOg034Cbf7GL3Yb0XuSHFbEmjffS4DHtxNNOtLztrEqYg4UybIBngbwv406uvTdBpnDZTKFti35t2fZV2gcV5CzOP-9zJdESV8wXmiXQAJzhemPkmlfJGv1sGxVANKuNARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط في بلدة في الشمال الشرقي.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77650" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7ogYTlrPbMdIZS0oxIDnM3wtiZIaRVfjC6RFkdy9X0KI3vBoYoExjIjZb4hOPE4hVAsMNoOtqfg1zxr_cHLW04MGgxXlfVKez0rXw5Z48uWeaTl2PiU7zhmO_dQTIpU0Dd847vdqB-FCO6WqSmTUwKAMAmxl9WtHxVp0JMgzYJFkruOy5Xawl1NuXwNkK8qa9zA0jMpXxkQEL9kVF8nYp0rP-nweeWk7IoBy3XA-1XhjuWw5pUD4L2IrX3RlhacBGkfJyrDxHYdft8o_rx7NzKC8mXG-Yc2wFNEYp01IlP1ckAXbpOq0fI_RrYG47hYHsNNOfvj7itWT-3ChP8pjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الدفاعات الجوية تحاول اعتراض الصواريخ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77649" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سقوط مباشر حيفا المدينة الصناعية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77648" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03dff10ca.mp4?token=Fkp4fLbR1nJInQspTzFemSXUfzdKTf2xo8CULk9fZrAx_Ojnzcw3S6pMdwWwvjmohoM9gfA-uRKyPF0yJrBTcHfTOLt5VM7HtDfHNvVTORCD4XtDVUZv6vfb6EG2Zp3PHxB9kF67OIOzAHOCu9gCM8749WxTTCk6YtpNf442HGKRxdQTQ_ZD5KgfvFGIxSqatc3Sa-NNrL5hxp877R2Nfa4ufXBcqcf8jPkF3c1JVq-2p2d_NgtU8eoSRHPPpvt592IpioFdD83ywc0Cw-mtT7C8EQaZv3AFA3T5jEYVzAG1g5P_wBCrS_5bHAKtMtZJ9ewgVM28fb0gUIDXQG6Hrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03dff10ca.mp4?token=Fkp4fLbR1nJInQspTzFemSXUfzdKTf2xo8CULk9fZrAx_Ojnzcw3S6pMdwWwvjmohoM9gfA-uRKyPF0yJrBTcHfTOLt5VM7HtDfHNvVTORCD4XtDVUZv6vfb6EG2Zp3PHxB9kF67OIOzAHOCu9gCM8749WxTTCk6YtpNf442HGKRxdQTQ_ZD5KgfvFGIxSqatc3Sa-NNrL5hxp877R2Nfa4ufXBcqcf8jPkF3c1JVq-2p2d_NgtU8eoSRHPPpvt592IpioFdD83ywc0Cw-mtT7C8EQaZv3AFA3T5jEYVzAG1g5P_wBCrS_5bHAKtMtZJ9ewgVM28fb0gUIDXQG6Hrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إيقاف جميع القطارات في الكرمئيل.
‏</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77647" target="_blank">📅 10:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f97cdb5c2a.mp4?token=UVHD34H40DVkXYISDc7GtGCLl8uc0uT8OgRZ4wSwOknQuBUIkXeFoRnUZQSgWyL0HisuACeS5ZoyROMUy0mRoQVgWNnE4qEFAB7QX6RJX1C_LKbDAMFDzKOJlNY-eBsx59RvZkqUB9lQMB4e_uKLO65rI4fQ9xDU_IjuNt2yHCoJuIFq4EzCYghaJdYG7Wugq0JQbxQoTnvDL-nWyN-oHBUGj5BnYlR5SXVmM8IFr81TJNXa6IHmzon6bNyPSjgz39jWp-RhOtNGLHue1fvEUo4V5v8RLYknphSjIpwsKCy9VXXRbsqpxR-Ckj2LCQIfGyjqGJKFzwfP93uTcsLUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f97cdb5c2a.mp4?token=UVHD34H40DVkXYISDc7GtGCLl8uc0uT8OgRZ4wSwOknQuBUIkXeFoRnUZQSgWyL0HisuACeS5ZoyROMUy0mRoQVgWNnE4qEFAB7QX6RJX1C_LKbDAMFDzKOJlNY-eBsx59RvZkqUB9lQMB4e_uKLO65rI4fQ9xDU_IjuNt2yHCoJuIFq4EzCYghaJdYG7Wugq0JQbxQoTnvDL-nWyN-oHBUGj5BnYlR5SXVmM8IFr81TJNXa6IHmzon6bNyPSjgz39jWp-RhOtNGLHue1fvEUo4V5v8RLYknphSjIpwsKCy9VXXRbsqpxR-Ckj2LCQIfGyjqGJKFzwfP93uTcsLUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إيرانية في طريقها للكيان</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77646" target="_blank">📅 10:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات في الكريوت حيفا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77645" target="_blank">📅 10:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارات تهز الجولان المحتل</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77644" target="_blank">📅 10:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QturE0cmrjsr4B9HzHSL-SBobJxb5IYXh1vjJ_Beb53XLwzjxFF75059DAOe5NzncrrxvznSx8KRswnY_aU2ezH6Z1-OIvmG9qoJuWVvSJevDRGjt6LzKopqSTFY3-yMokrWdX6EX5kWwBWjCSltsM0vEEgvYkW9AEapO0vzL77yOEoLh5P8EoEt7qSFW5CGHfqluB3oY5L6vmckc0oIK4fN_yEWwYvUK1_jTQaMOZU-wHJkmY1qf_wrJhRX4I0N79_dKPzyi9rjOlJkh1CU_N22G6JJTmTzLFfIhisKIYHEc9-wNYjNCZNL-pWpJtOWccaYWgcyQ_CMuh7E5pQ6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية في طريقها إلى الكيان</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77643" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d51976385.mp4?token=Qlm9IKCthILC_viQxUzxOW8u30ZBZBCaoCW-620ovARBdQ4RqwfNZr2T_PHCZOCgTcn5ocqIZp8AZKoJ4hmWaCb3j_NVuyZS1Iw2ysViOBzbJ8taSludRocHKi_PLgTna4pKbbCRBi3bfxEU7crfaFPKuFKJLuPE1otw_4bv-vhIXP26BLOu4cUyrbzgpPvys4Z9sZA4tw5ih-drfSvE9OOanQ2lgvX3O9L8_T9W4zWu4McW_uJDH41s4acUxLZv4sdL53Ezeqv6L8DGcTyjhmd_smrVdv3dat5p0Me5ESLj35-VjOQwOyFviZIkHv8sXo4kUcqIMCKTa5w6K71Vqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d51976385.mp4?token=Qlm9IKCthILC_viQxUzxOW8u30ZBZBCaoCW-620ovARBdQ4RqwfNZr2T_PHCZOCgTcn5ocqIZp8AZKoJ4hmWaCb3j_NVuyZS1Iw2ysViOBzbJ8taSludRocHKi_PLgTna4pKbbCRBi3bfxEU7crfaFPKuFKJLuPE1otw_4bv-vhIXP26BLOu4cUyrbzgpPvys4Z9sZA4tw5ih-drfSvE9OOanQ2lgvX3O9L8_T9W4zWu4McW_uJDH41s4acUxLZv4sdL53Ezeqv6L8DGcTyjhmd_smrVdv3dat5p0Me5ESLj35-VjOQwOyFviZIkHv8sXo4kUcqIMCKTa5w6K71Vqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
Ebrahim Zolfaghari is Back!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/77642" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات تهز الجولان المحتل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77641" target="_blank">📅 10:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تفعيل صفارات الإنذار في الأردن</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77640" target="_blank">📅 10:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSuPU76h-d0Br-HCcvGWrZMFEOzvHBIRLWDkNK80mY97s7o4t4kvAQKfgnqjoHd0G0cJfzUt-22Mdvj95KdgxLMkowcXKh5qau493lqlCrFIUghWmxJPNCc_tdeSFj58tD_W7FVql5sJ3-vpDcw-4c5RwgY0_pvi6PYhfQ3TVvL1Y3NmFc5JfH6YDa_D_hVndMOanq0Dhx9LlEh9Uk82r2882FdcfZOcA6zi-kTJg2FPasolIuGCGxgw7m7cQIYqVa9kCnnSIHwrVRn6Ms9CEci_dYAX80W0AGmMW4CkZvJ14pFBA_68n8TOjUkvHNEwN96t4zHrUqtEScDD9YkRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية في طريقها إلى الكيان</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77639" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اطلاق موجة صواريخ إيرانية نحو الكيان المحتل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77638" target="_blank">📅 10:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">إعلام العدو: أنباء عن إطلاق مسيّرات يمنية باتجاه إسرائيل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77637" target="_blank">📅 10:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اطلاق موجة صواريخ إيرانية نحو الكيان المحتل</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77636" target="_blank">📅 10:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اطلاق موجة صواريخ إيرانية نحو الكيان المحتل</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77634" target="_blank">📅 09:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">المتحدث باسم الحرس الثورة الإيراني: للمرة الألف، أثبتنا أن السماء فوق الأراضي المحتلة والمنطقة تخضع لإرادتنا وتحت سيطرة صواريخ الحرس الثوري الإيراني المدمرة للمجال الجوي.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77633" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏تعليق جميع الرحلات في طهران حتى إشعار آخر</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/77632" target="_blank">📅 09:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">القوات المسلحة اليمنية:  في إطارِ التصدي للعدوانِ الأمريكيِّ والصهيونيِّ على محورِ الجهادِ والمقاومةِ في إيرانَ وفلسطينَ ولبنانَ والعراقِ واليمنِ، ورفضاً للمشروعِ الصهيونيِّ الساعي لإقامةِ إسرائيلَ الكبرى تحتَ مسمى الشرقِ الأوسطِ الجديدِ، وسعياً منا إلى كسرِ…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/77631" target="_blank">📅 09:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">القوات المسلحة اليمنية:  في إطارِ التصدي للعدوانِ الأمريكيِّ والصهيونيِّ على محورِ الجهادِ والمقاومةِ في إيرانَ وفلسطينَ ولبنانَ والعراقِ واليمنِ، ورفضاً للمشروعِ الصهيونيِّ الساعي لإقامةِ إسرائيلَ الكبرى تحتَ مسمى الشرقِ الأوسطِ الجديدِ، وسعياً منا إلى كسرِ…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77630" target="_blank">📅 09:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77629" target="_blank">📅 09:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f0389b66.mp4?token=na5XQtgoIoesITo_hGqIRXOWOoeGZHirAyOTdgGWZ9zWKXC_UITZpIi762pSizONcmHWU1PuJ7BVF5ccGotj2KEgkg5cJqNjM4y1tGN6h68UsFYfLE_sL7Ju0k1aagrRB54UL5AIa5n2lgn8GEvyPG-Pq6f0ANOrTlmrK1hQ7tMPawfX-h3_3i2vjYZi7pJ3xohzwrMOt_uMWIhxJZmO-mb-x4u-GA0FYcNIQnXVVurTqWhdJ4-Y8RwbSV10hiiD8BLk4fILb9rk6msdVNaw7NBPWJuDbOfOsAPJbINs_8CxO0h7cCKOR9af0FUWQJWpS6Ak4KZoMeLXsz59xQ0vMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f0389b66.mp4?token=na5XQtgoIoesITo_hGqIRXOWOoeGZHirAyOTdgGWZ9zWKXC_UITZpIi762pSizONcmHWU1PuJ7BVF5ccGotj2KEgkg5cJqNjM4y1tGN6h68UsFYfLE_sL7Ju0k1aagrRB54UL5AIa5n2lgn8GEvyPG-Pq6f0ANOrTlmrK1hQ7tMPawfX-h3_3i2vjYZi7pJ3xohzwrMOt_uMWIhxJZmO-mb-x4u-GA0FYcNIQnXVVurTqWhdJ4-Y8RwbSV10hiiD8BLk4fILb9rk6msdVNaw7NBPWJuDbOfOsAPJbINs_8CxO0h7cCKOR9af0FUWQJWpS6Ak4KZoMeLXsz59xQ0vMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اليمن سيَسرق أمانكم ، يا صهاينة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77628" target="_blank">📅 09:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77627">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">القوات المسلحة اليمنية:  في إطارِ التصدي للعدوانِ الأمريكيِّ والصهيونيِّ على محورِ الجهادِ والمقاومةِ في إيرانَ وفلسطينَ ولبنانَ والعراقِ واليمنِ، ورفضاً للمشروعِ الصهيونيِّ الساعي لإقامةِ إسرائيلَ الكبرى تحتَ مسمى الشرقِ الأوسطِ الجديدِ، وسعياً منا إلى كسرِ…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77627" target="_blank">📅 09:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">القوات المسلحة اليمنية:
في إطارِ التصدي للعدوانِ الأمريكيِّ والصهيونيِّ على محورِ الجهادِ والمقاومةِ في إيرانَ وفلسطينَ ولبنانَ والعراقِ واليمنِ، ورفضاً للمشروعِ الصهيونيِّ الساعي لإقامةِ إسرائيلَ الكبرى تحتَ مسمى الشرقِ الأوسطِ الجديدِ، وسعياً منا إلى كسرِ الحصارِ الظالمِ والغاشمِ الذي يفرضُهُ العدوُّ الأمريكيُّ على شعبِنا وشعوبِ المحورِ الحرةِ والعزيزةِ في لبنانَ وغزةَ وإيرانَ، وفي إطارِ مبدإِ وحدةِ الساحاتِ ومواجهةِ الأعداءِ، ورداً على العدوانِ الصهيونيِّ على لبنانَ وإيرانَ وغزة، قامتِ القواتُ المسلحةُ اليمنيةُ بإطلاقِ دفعةٍ صاروخيةٍ استهدفت أهدافاً حساسةً للعدو الإسرائيليِّ في منطقةِ يافا المحتلةِ وقد حققت أهدافَها بدقةٍ بفضلِ الله.
وفي هذا السياقِ تؤكدُ القواتُ المسلحةُ على الآتيِ:
أولاً: نعلنُ حظرَ الملاحةِ البحريةِ بشكلٍ كاملٍ وتامٍّ على العدوِّ الإسرائيليِّ في البحرِ الأحمرِ، ونعتبرُ أنَّ كلَّ تحركاتِ العدوِّ أصبحتْ هدفاً عسكرياً لقواتِنا المسلحةِ من لحظةِ إعلانِ هذا البيانِ.
ثانياً: نؤكدُ أنَّنا سنواجهُ التصعيدَ بالتصعيدِ، وإنَّ عملياتِنا العسكريةَ ستكونُ متصاعدةً بما يواكبُ الأحداثَ والمعركةَ والاشتراكَ مع محورِ الجهادِ والمقاومةِ.
ثالثاً: نؤكدُ على حقِّ شعبِنا وشعوبِ أمتِنا الحرةِ في مواجهةِ العدوانِ الأمريكيِّ الإسرائيليِّ، وأنَّنا لنْ نقفَ مكتوفي الأيدي أمامَ الحصارِ الظالمِ على شعبِنا وشعوبِ محورِ الجهادِ والمقاومةِ في فلسطينَ وغزةَ وإيرانَ ولبنانَ والعراقِ، وإنَّ كلَّ محاولاتِ العدوِّ ستبوءُ بالفشلِ بإذنِ اللهِ، وإنَّ عملياتِنا مستمرةٌ طالما استمرَّ العدوانُ والحصارُ علينا وعلى محورِ الجهادِ والمقاومةِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
﻿</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/77626" target="_blank">📅 09:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تفعيل الدفاعات الجوية في كرمانشاه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/77625" target="_blank">📅 09:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏إذاعة الجيش الإسرائيلي: استمرار تبادل الضربات مع إيران متوقع لعدة أيام</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/77624" target="_blank">📅 09:02 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
