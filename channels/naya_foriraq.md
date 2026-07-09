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
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
القائم بالاعمال الامريكي في بغداد:
نتشاور مع الحكومة العراقية لدعم خيارات العراق لبناء المرونة فيما يتعلق بإنتاج الكهرباء على المدى القصير.
لعد جنرال الكتريك شجانت تسوي من 2003 ولليوم ، يومية موقعين عقد وياها وضخ فلوس ونفس الطاس ونفس الحمام
😄</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/naya_foriraq/82211" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb52071cdf.mp4?token=QkCTA7AllPCjmEeS4IzLLB1XbfxFxRYjAP9XoTz3yw-EAxBWUmdspeXy4uwQeWvHCXqJFHZeiM9vt4vRN-m_ZGuTTPDD6WhBg6OT7XPTJa4CRY8fVl0gTO6PXdC9wcvjD9Y6sE0SaN2cpkJh-lK1B-FJ7De255KocZIjNYuB7PuAe-HQPuELC-4ljqxmH9O7O32nd71_HPBU7snU9yHBhznrOJZi4_C_nnwTjlOcL-WMirb5ed3H7lFxAopA-xb-5uz2RssTLsIRftiAsQXcezLXjlPcmHOMLie6D_8nij6LxgNTKpW0H75o5xZ8pHb9IYVdSet8FwmmyHxRTttZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb52071cdf.mp4?token=QkCTA7AllPCjmEeS4IzLLB1XbfxFxRYjAP9XoTz3yw-EAxBWUmdspeXy4uwQeWvHCXqJFHZeiM9vt4vRN-m_ZGuTTPDD6WhBg6OT7XPTJa4CRY8fVl0gTO6PXdC9wcvjD9Y6sE0SaN2cpkJh-lK1B-FJ7De255KocZIjNYuB7PuAe-HQPuELC-4ljqxmH9O7O32nd71_HPBU7snU9yHBhznrOJZi4_C_nnwTjlOcL-WMirb5ed3H7lFxAopA-xb-5uz2RssTLsIRftiAsQXcezLXjlPcmHOMLie6D_8nij6LxgNTKpW0H75o5xZ8pHb9IYVdSet8FwmmyHxRTttZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔰
كما قال الشيخ أكرم الكعبي: سلاحنا وديعةُ الإمام الحجة (عج) وقد تجلت آثار هذه الوديعة في مشهد الوفاء المليوني الذي شهدته النجف في وداع الإمام الخامنئي (رض)
#قوموا_لله
#كونوا_احرارا
ً</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/naya_foriraq/82210" target="_blank">📅 17:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏وزير الطاقة التركي: نخطط لتوقيع اتفاقية مع العراق بشأن خط أنابيب لاستمرار تصدير النفط لـ12 شهر اخرى.</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/82209" target="_blank">📅 17:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مطار النجف الاشرف الدولي يعود للعمل امام الرحلات التجارية بعد الإغلاق المؤقت</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/82208" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
بيان لحرس الثورة الاسلامية:
بسم
الله
قاصم
الجبارين
«
فَمَنِ
اعْتَدَىٰ
عَلَيْكُمْ
فَاعْتَدُوا
عَلَيْهِ
بِمِثْلِ
مَا
اعْتَدَىٰ
عَلَيْكُمْ
»
لقد ذكرنا في البيان السابق أن تكرار العدوان سيوسع نطاق ردنا ليشمل قواعد العدو الأخرى في المنطقة، وفي المرحلة الثانية من الرد على اعتداءات الجيش الأمريكي القاتل للأطفال، قمنا بتحويل هذا التهديد إلى فعل
دكّ مقاتلو القوة الجوفضائية التابعة للحرس الثوري في تمام الساعة 14:20 من بعد ظهر اليوم مركز قيادة وسيطرة العدو في غرب آسيا وقاعدة العدو الجوية في الأزرق بالأردن بـ 10 صواريخ باليستية
في حال تكرار عدوان الجيش الأمريكي الإرهابي، لن تكون بقية القواعد الأمريكية في المنطقة في مأمن من نيراننا الكثيفة
وما
النصر
إلا
من
عند
الله
العزيز
الحكيم</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/82207" target="_blank">📅 16:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643cebc914.mp4?token=fJnjJy-D1XxPrUJNPli149cXUkSNglIUqRihCyo9idr6UvqBCmfxCZu6TWT3v9zPQkZ_O7jdDlUmXNAfizC6W49ATV6s3eeXWu1-Xrm12Xfx6sXoYl4VcAHRF-cmmJ9elSGWvO6UUq4znniERvEm9fZOQDLJwHWI8inQqTMluBf2F0L3nSRy5ZT8Bpf74BLLcRhATnPtT9mbHvRXT_Ejsv3x0Dt9sQ4A-qtATFuKITu0KZd0cZ2sbazqJd_hyFGqFmH1-68Qv7N5rEPoBWbMeDrBEv-aNY4bkE1c1_loN74_1H0N4BoQzzmAZ4m7DkzUsobSrupUUu2yzCtCif88eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643cebc914.mp4?token=fJnjJy-D1XxPrUJNPli149cXUkSNglIUqRihCyo9idr6UvqBCmfxCZu6TWT3v9zPQkZ_O7jdDlUmXNAfizC6W49ATV6s3eeXWu1-Xrm12Xfx6sXoYl4VcAHRF-cmmJ9elSGWvO6UUq4znniERvEm9fZOQDLJwHWI8inQqTMluBf2F0L3nSRy5ZT8Bpf74BLLcRhATnPtT9mbHvRXT_Ejsv3x0Dt9sQ4A-qtATFuKITu0KZd0cZ2sbazqJd_hyFGqFmH1-68Qv7N5rEPoBWbMeDrBEv-aNY4bkE1c1_loN74_1H0N4BoQzzmAZ4m7DkzUsobSrupUUu2yzCtCif88eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
لحظة تدمير طائرة MQ9 الامريكية بواسطة الدفاع الجوي الايراني.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/82206" target="_blank">📅 16:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇩🇿
شركة سوناطراك الجزائرية: حادث في مصفاة أرزيو.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82205" target="_blank">📅 16:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قطر توقف زيادة إنتاج الغاز الطبيعي المسال بعد الهجوم على ناقلة النفط في مضيق هرمز</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82204" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الانبياء المركزي:
هذا الحزن والغضب سيستمران في طريق الثأر لقتلة القائد الشهيد، القوات المسلحة ستعمل، بدعم الله والشعوب المسلمة، على محاسبة منفذي ما وصفها بالجرائم الإرهابية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/82203" target="_blank">📅 16:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82202">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزارة الخارجية العراقية:
وفاة أحد الصيادين العراقيين الذين تم اعتقالهم من قبل خفر السواحل الكويتي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/82202" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
مجلس النواب العراقي يُصوت على إعفاء رئيس الهيئة الوطنية للاستثمار حيدر مكية من منصبه واحالة الملفات إلى هيئة النزاهة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/82201" target="_blank">📅 15:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82200">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7-Wck-hf77HL5cmQObwM1SZ7sErfT53hyq72pWRE0xHkNSc91I_Arigiwyt6P-GRK1C734dAoHD_P-OCjX09RPfYY6M_0bf6rEJd7V1MnC3exB9u-oX2OcGDzSi0kTHyYMQOjEozV6LTlEf_St-ZPHACO2U_ZR8JA01CL4Y-3jHkSdniQ2KsOmsoqwAjQHSkWRUXeopv9snbWzrjoxNhwudxpdMmNoR1aMeuVI22Ic_e5RcikttdvN8yQsa7jkL_cS-EBZIuf0T_xA8Nu5bRI91t0zv0dKPUTbypupqYn0l1vZkpR1kdI-yI7I9dH74cSbVNY0iFA_z4QZ3iesDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي يعلن إلقاء القبض على أحد تجار المخدرات الدوليين ينتحل صفة "إعلامي حربي" كما تم ضبط ما يزيد على 111 ألف حبة من نوع كبتاجون بحوزة متهم اخر في محافظة ذي قار</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/82200" target="_blank">📅 15:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82199">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
‏
القيادة المركزية الأميركية:
ضربنا أكثر من 170 هدفا في إيران خلال اليومين الماضيين</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/82199" target="_blank">📅 15:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇬🇧
وزيرة الخارجية البريطانية:
إيران ترغب في بقاء مضيق هرمز رهينة لديها</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/82198" target="_blank">📅 15:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCnlDfXaUMi5CKZBR9BgccdsihCFoOFixn6y2pFcZi8-lUHVjq37r3WvfyuLnA2CnNACZrIkM8diAnZiAqRZb-mWAtrzpcBST4ZVHTKW4yIDEZqIiDz1k19008KI6dUKh-9Y3eGMdsmd428zTKa1jfOiGhv6aVfuU_YoiFTjDzATkcclrwInNAbPLD12YXlDhkbyqdKmQrbvEUxuAlM3U7lFvadP5w7h_2HharAx99qKcOxKndKxbpyDAgv1PBiEHYtjY3TmXVkTiVXAvEYP3f2spzdb-pUDrqzPWVxnZ_DtzBR37ZSlzO4VWOZ_sXQJCVWDSqFDJ2GHwcPzCfx8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر إيراني مطلع: تحليق طائرات مقاتلة تابعة للقوات المسلحة الإيرانية لتأمين سماء مدينة مشهد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/82197" target="_blank">📅 15:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله اكبر
اطلاقات جديدة ضخمة من ايران</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/82196" target="_blank">📅 15:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اللجنة المنظمة لمراسم تشييع قائد الثورة في العراق: الإحصاءات الأولية غير الرسمية تشير الى مشاركة اكثر من 10 ملايين شخص في التشييع.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82195" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16f8a8793.mp4?token=eWMqntsCx8zSWHZ-eYa5lxFQHAbS73zeP49iZ_YGksedOy7WUXyu_BTwKMzeTiFFEvzCqL_nyTgv6C6gEf-0bZ1LOa9kp3yrvN-l_WXCk3qAmj4fokvN3hFcOJwd-LRrQx-ABqb9HwawO9_AMridQw3ZvkhJnhLR-u-mvYnFiMyO5_ZnagXwT3zHlk8QaNpbKTGvq0xS34V3ordynfrTgwTwAajxYOxlrkhiAY-4eo4jrnkFn7NnF_fUECq3imRJhvQO5p3UDDFRSjIRxXZ10FIWxaUgAGA5iYzJt3T_jsMjHDvfenkCB2W6JJ4tTXGnBevvANUUGqN5nT9Bnqby3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16f8a8793.mp4?token=eWMqntsCx8zSWHZ-eYa5lxFQHAbS73zeP49iZ_YGksedOy7WUXyu_BTwKMzeTiFFEvzCqL_nyTgv6C6gEf-0bZ1LOa9kp3yrvN-l_WXCk3qAmj4fokvN3hFcOJwd-LRrQx-ABqb9HwawO9_AMridQw3ZvkhJnhLR-u-mvYnFiMyO5_ZnagXwT3zHlk8QaNpbKTGvq0xS34V3ordynfrTgwTwAajxYOxlrkhiAY-4eo4jrnkFn7NnF_fUECq3imRJhvQO5p3UDDFRSjIRxXZ10FIWxaUgAGA5iYzJt3T_jsMjHDvfenkCB2W6JJ4tTXGnBevvANUUGqN5nT9Bnqby3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الخارجية القطرية ندين الاعتداء الإيراني على الاردن
#مبلاش
افتكر انا قلتلك مبلاش</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82194" target="_blank">📅 15:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اطلاقات اضافية من ايران باتجاه القواعد الامريكية في الاردن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/82193" target="_blank">📅 15:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بحرية الحرس الثوري بشأن مضيق هرمز: بسم الله الرحمن الرحيم
🔹
تحية للأمة البصيرة والشجاعة التي أظهرت، بحضورها المذهل وتشييعها لملايين من شهيد القائد في إيران والعراق، أن هذا هو الزمان الذي ينتهي فيه جبروت القوى، وأن هذا القرن هو عصر هيمنة إرادة الأمم.
🔹
وتحية…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/82192" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoKWyCsG_-ymplio2EJ2jzSLirbJeGbUC-ATUGiht5DqAZAMc-6Ww2606tbEPnj1rFVsIGAJPSm4SwjG99NepXn-r85KzkoP6MatTeBAf56aTnWo4zwGMyN1WpnTnoi6iIIh5fy3ddE4nQqdI0mMsxSEI1vuvneC15NGGIVU9le7LeIRV1lz24Ruawf5_i-dmkeYpBf__D3GWr1bcDOsUjultlGV3cvpA444r1oQ3tAcXSQ1YqBadmloCw95cthWJPBiZ3TsG0qmLHk6qGMp5Et32WQ9HvB8AbE1ncak9SZ6Ofew4CSfVM_MV-NusIbiKtj2x7ksiXhwCVD0N_4d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحرية الحرس الثوري بشأن مضيق هرمز:
بسم الله الرحمن الرحيم
🔹
تحية للأمة البصيرة والشجاعة التي أظهرت، بحضورها المذهل وتشييعها لملايين من شهيد القائد في إيران والعراق، أن هذا هو الزمان الذي ينتهي فيه جبروت القوى، وأن هذا القرن هو عصر هيمنة إرادة الأمم.
🔹
وتحية للمقاتلين الشجعان في الإسلام الذين أثبتوا، برد فعلهم القوي على انتهاكات الجيش الأمريكي الذي يقتل الأطفال، أن مصير المعركة لا يحدده امتلاك الأسلحة، بل قوة الإيمان.
🔹
المقاتلون الذين، خلال الأسبوعين الماضيين، عززوا سيطرتهم على مضيق هرمز وأمنوه، وبإعادة فتحه تدريجياً، رفعوا قدرة المرور إلى حوالي 50٪ من حركة السفن قبل الحرب، وهم بصدد زيادة قدرة حركة السفن التي تحصل على تصريح من قوات البحرية التابعة لحرس الثورة الإسلامية لعبور المسارات المحددة من قبل الجمهورية الإسلامية، مع الالتزام الصارم بقواعد الأمن.
🔹
نعلن مرة أخرى أنه لا يحق للأجانب أي حصة في هذه الأرض وفي مضيق هرمز. إن مغامرات الجيش الإرهابي الأمريكي وتدخله في تحديد مسارات المرور، بالإضافة إلى أنه سيواجه رداً قوياً منا، يعيق أيضاً عملية إعادة الفتح التدريجية، ويعرض مصالح الدول التي تستفيد من مضيق هرمز لخطر كبير.
قوات البحرية التابعة لحرس الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/82191" target="_blank">📅 15:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله أكبر
انفجارات تهز قاعدة موفق السلطي الجوية في مدينة الزرقاء مجددا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/82190" target="_blank">📅 15:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/82189" target="_blank">📅 15:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/82188" target="_blank">📅 15:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROxM2tW70tcnEluqA511X328Cq4cnfl8xDkbMh-YwfuD6HHRnGtEApdqSUxDsvLosmD8BVMmxIbAki2T-apRwy83dzBqm6zK6519_SbNSIKf0z1ctpdAWYymC4H4xZEPUy4VMxS71RDCMvIAJLOLAfmq7WhaD3MUXGJPESAliLpbSKdMtSQJGfaXcnacJNL4k2Kpmf-nDHF0kSngjEpBhSMGwtxqr7FKui1PPkwzSETTQEZxGh63v48Ub5XFLnzHByVl7hTpPs4qOKgVzYSPQ0iLWM5YUuj94jiEPAT54iSOpFXWQwxraqb5EtNW80QkTEVnSlHEFHPA6GrJz10W8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد نايا.. الإعلام الإيراني</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/82187" target="_blank">📅 15:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">احتراق طائرة أمريكية مقاتلة من طراز F 16 بظروف غامضة في مطار عسكري باليونان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/82186" target="_blank">📅 15:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82185">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مصدر إيراني مطلع: الأنباء حول إنفجار في شيراز غير صحيحة والصور المتداولة على الإنترنت قديمة وتستخدم كجزء من الحرب النفسية للعدو.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/82185" target="_blank">📅 15:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سماع دوي انفجار في كرمان</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82184" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انباء عن غلق الاجواء السورية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82183" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">توقف شبه تام لحركة الملاحة في مضيق هرمز</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/82182" target="_blank">📅 14:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات عنيفة تهز أربيل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/82181" target="_blank">📅 14:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات عنيفة تهز أربيل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/82180" target="_blank">📅 14:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نائب محافظ هرمزغان الإيرانية: في الهجمات العدوانية التي نفذها الجيش الإرهابي الأمريكي على الرصيف التجاري والصيادي في سيريك، استشهد 3 أشخاص وأصيب 15 آخرون.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82179" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏الجيش الأردني يدعي اعترضنا وأسقطنا 8 صواريخ إيرانية اخترقت أجواء البلاد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/82178" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">احتراق طائرة أمريكية مقاتلة من طراز F 16 بظروف غامضة في مطار عسكري باليونان</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82177" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوي صافرات الإنذار بقاعدة فكتوريا بالقرب من مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82176" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82175">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مصدر إيراني مطلع: تحليق طائرات مقاتلة تابعة للقوات المسلحة الإيرانية لتأمين سماء مدينة مشهد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/82175" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82174">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78ce8a7b3.mp4?token=kIElEe__eDgeZFtVRG_bJp7PRYIvnmCmqbNN4wz4MkFcfMpihXocpS_T5SNldyYo_Y90n3kxQTQ_9KFQ-7rv-RuSEIuD4e8BazBJSvxxT_rbw1Q397vvR79-QxQHC-o8vPYTruu3CxbplL0duDOvnFJ-gTPbWHGfe_aOmTUwRBVzwxHWxt28Yj6yjTZVsUY5CFtDNCDKGQG5FM9AiC8u150-aeBGKnX3zDVlixSKGbRkYHHiLLZ159r8DP-CAjL8FMFqwSytUa9l0ct_L-bl78zonoO3x1-_Ax5ZyojXV91tIXSPrW5xXmaXky8YzpYTc9PlvijSTtKu8sO2vE1CSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78ce8a7b3.mp4?token=kIElEe__eDgeZFtVRG_bJp7PRYIvnmCmqbNN4wz4MkFcfMpihXocpS_T5SNldyYo_Y90n3kxQTQ_9KFQ-7rv-RuSEIuD4e8BazBJSvxxT_rbw1Q397vvR79-QxQHC-o8vPYTruu3CxbplL0duDOvnFJ-gTPbWHGfe_aOmTUwRBVzwxHWxt28Yj6yjTZVsUY5CFtDNCDKGQG5FM9AiC8u150-aeBGKnX3zDVlixSKGbRkYHHiLLZ159r8DP-CAjL8FMFqwSytUa9l0ct_L-bl78zonoO3x1-_Ax5ZyojXV91tIXSPrW5xXmaXky8YzpYTc9PlvijSTtKu8sO2vE1CSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اضافية من الاردن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82174" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82173">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235cd514d2.mp4?token=nk-uJY3TdSMgxV9hPdWzLYoySPx6Fnytp-hCP_UFz3qF-VsjRlSnPKk3_7bgsFvp2my3CLerJqxaC6ZNgJ7vBSIfjK015r4evGFJgpAmr0CwIyHMYDuPUJN_GDp-0MvU9lNihx4OhTK6U6fnHmQTbltANUH0Mg_TTnGQiFafiMxq7i1GdcUYEGu1imQtVMjqmvKG-3wlXtp57w4qTOtQMgOgPIw61yzgDeg0-7ACeH3LrhGtUISA3ZtawhTVP4Fd4qX1m7p3i0SOjUYhIDxZnEtU2WQCgNG_aFk06bqP0G2yaRVC1-g55WnuDCcqVmHipjFCCPspy7C2szX7dxFaXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235cd514d2.mp4?token=nk-uJY3TdSMgxV9hPdWzLYoySPx6Fnytp-hCP_UFz3qF-VsjRlSnPKk3_7bgsFvp2my3CLerJqxaC6ZNgJ7vBSIfjK015r4evGFJgpAmr0CwIyHMYDuPUJN_GDp-0MvU9lNihx4OhTK6U6fnHmQTbltANUH0Mg_TTnGQiFafiMxq7i1GdcUYEGu1imQtVMjqmvKG-3wlXtp57w4qTOtQMgOgPIw61yzgDeg0-7ACeH3LrhGtUISA3ZtawhTVP4Fd4qX1m7p3i0SOjUYhIDxZnEtU2WQCgNG_aFk06bqP0G2yaRVC1-g55WnuDCcqVmHipjFCCPspy7C2szX7dxFaXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اضافية من الاردن بعد الهجوم الصاروخي الايراني على القواعد الامريكية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/82173" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82172">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الأردن تزعم التصدي للصواريخ الايرانية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/82172" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzTiswhoLDMJnHqpqulrBH1ipjRvz3pYbeFiWsODUIl6PeT2xlF4xMjElYeeQkm3pBG6ZJBGzzfo8lSagMZCrVKYRguUXp1DrM7lopZaKQ0IRolmLFSveA5G3gGFiJrQBHJ8Aqc03zJ4H6ODV9iT6OyYiu3DR07aox2aDYRNhPOdD3WAHbTwZ8M5WcpZ_Mx77cGNYDAgyDrXTZjZxP2NnDZfKK8P943AE-xU9MQwhL3HAAGlp3GgVOYp2F7SSt_WJ2JXnffh9R0V7W5FLTbpz7R8_RDBW6YznzKGWOzsmR5Hb4cA5djyeMs0Sol28wxCi-oaOv8aYXRxMd584SZDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة قادمة من إثيوبيا تفشل في الهبوط في مطار بن غريون بسبب القصف الإيراني للأردن.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/82171" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طائرة قادمة من إثيوبيا تفشل في الهبوط في مطار بن غريون بسبب القصف الإيراني للأردن.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/82170" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82169">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طائرة قادمة من إثيوبيا تفشل في الهبوط في مطار بن غريون بسبب القصف الإيراني للأردن.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/82169" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82168">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf2f9620d.mp4?token=DY2uu4JqBIegs2MteCico3vK9UtDrXXJPz43NiweTTgfYiHseOFzkeP0uOBrlJvCI_SLGMT7-2tUzlP-injYAspbMYMdBlHPUQMZnpHsIJfTVJvhrmqSpzbdKTvDNciyQ5Wx8Efo5tBcW49ilrW3SbhN3foKzft1rFRqs9ipWhpPxg3ZhFEAcwmV50qjjXZDkLcHX8myys-U_68b4GkjQUpAn9zxGR-IB6H-qDUTwh67ZQETBs2Kmp1lQxtSd49RLBBhpEXsIto8Mv2pb6IqxTFBupi0qNalj-vEbdHBPM8RlSFikRZhMtCmXFpZ5ApmKI8lHiBukBiD48i3mYvJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf2f9620d.mp4?token=DY2uu4JqBIegs2MteCico3vK9UtDrXXJPz43NiweTTgfYiHseOFzkeP0uOBrlJvCI_SLGMT7-2tUzlP-injYAspbMYMdBlHPUQMZnpHsIJfTVJvhrmqSpzbdKTvDNciyQ5Wx8Efo5tBcW49ilrW3SbhN3foKzft1rFRqs9ipWhpPxg3ZhFEAcwmV50qjjXZDkLcHX8myys-U_68b4GkjQUpAn9zxGR-IB6H-qDUTwh67ZQETBs2Kmp1lQxtSd49RLBBhpEXsIto8Mv2pb6IqxTFBupi0qNalj-vEbdHBPM8RlSFikRZhMtCmXFpZ5ApmKI8lHiBukBiD48i3mYvJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ ايرانية في سماء الاردن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/82168" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82167">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">توقف مؤقت لمطار عمان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/82167" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82166">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انباء عن دوي انفجارات في اربيل</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/82166" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82165">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09e5e5081.mp4?token=ZVLsQcwnjx0yZObueBvubV8xyLLCnXduPFAXZZy7O09MqGdrQjTblEpod4IaL82dAMq85A6ig1LhqynwYUXt4z5vxqh44ZYxP8EKTqCFntaWwVtbHaMBTBmeF_6rVDVwBa6VLdfpfhDqj6kfzynik-BtbbOjAVpqtmSi42UAt7Bspwc4cniJtuxfScW-4YRa8gEWoJprc6NgXc47fAucgJGMPNU7xiIEkC4pYbVGN-U6JRbUz4s1_e3S-omKuoRMZP7k90DPm4t4tQwrG6gvK3K27HeqRZo8EbVvS1T7oeawkLKnmH0pYrhwaLwPONggyY_VaDbvfPkRmTi3p9WAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09e5e5081.mp4?token=ZVLsQcwnjx0yZObueBvubV8xyLLCnXduPFAXZZy7O09MqGdrQjTblEpod4IaL82dAMq85A6ig1LhqynwYUXt4z5vxqh44ZYxP8EKTqCFntaWwVtbHaMBTBmeF_6rVDVwBa6VLdfpfhDqj6kfzynik-BtbbOjAVpqtmSi42UAt7Bspwc4cniJtuxfScW-4YRa8gEWoJprc6NgXc47fAucgJGMPNU7xiIEkC4pYbVGN-U6JRbUz4s1_e3S-omKuoRMZP7k90DPm4t4tQwrG6gvK3K27HeqRZo8EbVvS1T7oeawkLKnmH0pYrhwaLwPONggyY_VaDbvfPkRmTi3p9WAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ ايراني في سماء الاردن يتجه لهدفه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/82165" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82164">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293667c56d.mp4?token=MT-bUAxsY1PC99aQ1gJFc-9I3qo0Aw1DUtMfT8BqULJea37ydHsZgJj8wNDagAkHaOviQQhTUUWFqa-iJewuR8ROn_IRZAjkXjqyN8KGDOwN1C1_klAcvM0YJOZxN7hbRt6w4F1FvozNcP6mPJON01G1O3MkE_Vt7IZY_AsGvvrcDBd8DTGzlcgpC86sR51chSKxd0h2b0yaAG-1ywmAxNX1bG7KT4vlxMZIOPbebyx7qz90V5Bit--Pfr_zHY0J3nMDXx6rP8KCiEdk4inDamUXaGZed_T8rSOsrJ624KOSTKlPbDxSpfWPpVRmyAlqhCDx6LmhSwdb71QtFdizCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293667c56d.mp4?token=MT-bUAxsY1PC99aQ1gJFc-9I3qo0Aw1DUtMfT8BqULJea37ydHsZgJj8wNDagAkHaOviQQhTUUWFqa-iJewuR8ROn_IRZAjkXjqyN8KGDOwN1C1_klAcvM0YJOZxN7hbRt6w4F1FvozNcP6mPJON01G1O3MkE_Vt7IZY_AsGvvrcDBd8DTGzlcgpC86sR51chSKxd0h2b0yaAG-1ywmAxNX1bG7KT4vlxMZIOPbebyx7qz90V5Bit--Pfr_zHY0J3nMDXx6rP8KCiEdk4inDamUXaGZed_T8rSOsrJ624KOSTKlPbDxSpfWPpVRmyAlqhCDx6LmhSwdb71QtFdizCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الاردن تعج بالصواريخ الايرانية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/82164" target="_blank">📅 14:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82163">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بلا توقف الصواريخ الإيرانية اتجاه موفق السلطي بالأردن</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82163" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82162">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوي صافرات الإنذار بقاعدة الحرير الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/82162" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82161">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">السفارة الأمريكية في الأردن لرعاياها :  احذروا صواريخ ومسيرات إيرانية في السماء</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/82161" target="_blank">📅 14:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82160">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6dd456da.mp4?token=pjDT3QEJjYkxNm0vxTg2u0GYQRKy-W2gr7eBbuD6Zj4KJUrWZI-nYIYYzR3K_6cjK_Z7rZTkKJvGPaK-DYkPlwqAJ5FLGDIf6yEh1_IlHmtmvSFeiV7YAPAshThDnU0AtrvNTCZQR_X2UBVe9VRlhssJW9IwEEvkI2oNuFrLD6b2nAQOhyZGQCGrhD24qdWCruX2ujEtZC9Fymj741T3k5icmN-Dyn1h82CGG984oASJqFi5MeMT3LwfNqL9lPNMVh-lE0YFCuhP8sCt7ES-Jeg90oFjrGihdhcGh8oKdDYzetgZfjq-WKKZMXbrmGwqFMad9Kgw_0OC0kXAw1yl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6dd456da.mp4?token=pjDT3QEJjYkxNm0vxTg2u0GYQRKy-W2gr7eBbuD6Zj4KJUrWZI-nYIYYzR3K_6cjK_Z7rZTkKJvGPaK-DYkPlwqAJ5FLGDIf6yEh1_IlHmtmvSFeiV7YAPAshThDnU0AtrvNTCZQR_X2UBVe9VRlhssJW9IwEEvkI2oNuFrLD6b2nAQOhyZGQCGrhD24qdWCruX2ujEtZC9Fymj741T3k5icmN-Dyn1h82CGG984oASJqFi5MeMT3LwfNqL9lPNMVh-lE0YFCuhP8sCt7ES-Jeg90oFjrGihdhcGh8oKdDYzetgZfjq-WKKZMXbrmGwqFMad9Kgw_0OC0kXAw1yl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء مدينة الزرقاء الاردنية بعد الهجوم الصاروخي الايراني على القاعدة الامريكية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/82160" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82159">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">موجة صاروخية أخرى الان</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/82159" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82158">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/82158" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e5f936b55.mp4?token=QvGIxFDqaozXnWc69zKBgZeBzioY4XRR4NH1iy4I0irUHrYISJVWo5H2f3fd3-JdLcUES-X-oCW5B8JH-o3H6gNjzFwwWc4qSjVwZaShiUnKiitYiKac0b95IP_ob5G7bggpOH7kGR2FVgtOH5CHHC1YzPm6poGaEg2ulrK1veGZZ5Sm88Vyogelu0tYRHsFlTV0aNYhtp0B13_NpaEjJzhUikFWR1i6ChMpmxfuYdPHKcKjm47UYHtys_U0kRGQslWLPN59gt9RBOFi6Xw2gbK7_7U7TKINeMGv5qssXtChyec0iRwQVV5GEuoyKeJe57CaZlDQoRaD5ddfWQmRQwVBBHDz9Rcy3_vl-eZgJ0k64sO4mEaA7lxMaQV6UYKQKu0iPCS2ph3HG13Gh2ShIqLC-zL0L5hRPArARlfZF2VfW-LOFWbFePxSp8H5rfjusDUA_b_oSI0gc91doUFKSQWxeA_iIYu4-kcTJIZeZZMKctuQHgjmBNLOsO-S6D9hHVijLYoJQamnr91OKsEeOFKBTLEudS_NjzOG5QvSHWezC4SkjvA3IVyKJc-yIOp2ydnR9pb-vcOf_4N8K0zwimDdA0JhI1bnE538SImICTE_T4p0Sghl5m-rxPce3VMyWwNoHkb-dRGxRZkky4DDM5mUZMnCBX3giVCsSXtMtYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e5f936b55.mp4?token=QvGIxFDqaozXnWc69zKBgZeBzioY4XRR4NH1iy4I0irUHrYISJVWo5H2f3fd3-JdLcUES-X-oCW5B8JH-o3H6gNjzFwwWc4qSjVwZaShiUnKiitYiKac0b95IP_ob5G7bggpOH7kGR2FVgtOH5CHHC1YzPm6poGaEg2ulrK1veGZZ5Sm88Vyogelu0tYRHsFlTV0aNYhtp0B13_NpaEjJzhUikFWR1i6ChMpmxfuYdPHKcKjm47UYHtys_U0kRGQslWLPN59gt9RBOFi6Xw2gbK7_7U7TKINeMGv5qssXtChyec0iRwQVV5GEuoyKeJe57CaZlDQoRaD5ddfWQmRQwVBBHDz9Rcy3_vl-eZgJ0k64sO4mEaA7lxMaQV6UYKQKu0iPCS2ph3HG13Gh2ShIqLC-zL0L5hRPArARlfZF2VfW-LOFWbFePxSp8H5rfjusDUA_b_oSI0gc91doUFKSQWxeA_iIYu4-kcTJIZeZZMKctuQHgjmBNLOsO-S6D9hHVijLYoJQamnr91OKsEeOFKBTLEudS_NjzOG5QvSHWezC4SkjvA3IVyKJc-yIOp2ydnR9pb-vcOf_4N8K0zwimDdA0JhI1bnE538SImICTE_T4p0Sghl5m-rxPce3VMyWwNoHkb-dRGxRZkky4DDM5mUZMnCBX3giVCsSXtMtYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الايرانية في سماء الاردن وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82157" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات تهز الأردن مجددا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/82156" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82155">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوي صافرات الإنذار بقاعدة التوحيد الثالثة الأمريكية في العاصمة بغداد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82155" target="_blank">📅 14:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82154">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صواريخ توم هوك استهدفت محيط محطة بوشهر</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82154" target="_blank">📅 14:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82153">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">موجة مسيرات نحو البوارج الأمريكية في مضيق هرمز</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/82153" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82152">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوي انفجارات في بوشهر الايرانية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/82152" target="_blank">📅 14:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82151">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الحسينيون العراقييون أبناء ابا الفضل العباس مستعدون للمواجهة مع أمريكا
من سرباز جنرال سليماني</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82151" target="_blank">📅 14:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82150">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">AUDIO-2026-03-17-02-59-01</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/82150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82150" target="_blank">📅 14:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82149">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوي انفجارات في بوشهر الايرانية</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/82149" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82148">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فصائل المقاومة عراقية تستعد للتصعيد القادم في غرب اسيا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82148" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82147">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a8af4149.mp4?token=A_p7pi_XBNPu7hey2F9f2CS2HppQAp68E8yUU3Vhycfpnp71ANaZrOBqiWyMOwdZYNcd4yFws_WSnLloxIxkkiy0I_0CBfndZlcPHav-Q3ucYLcxUhTvrYfDj6_Sj31eSy3f_B1DooplEwW9yvYPvS1uGHeYgDmxS2xf4n-dR713xqe9S3jMPNzHYgPHslAGL1KbHj4qCQnPwH-EUdGQlaW1Al1-EhWEZMBI79wa7r6dxgBWj9go1i6UOjZKl0hyhq_pVPedOPH02vlPmqKzKyr6I-2wh0wpCU5p9eB9VBHsmhzMFOEiAeK-noijlXVmOqi8VbeSPtgxAnKmHwlaMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a8af4149.mp4?token=A_p7pi_XBNPu7hey2F9f2CS2HppQAp68E8yUU3Vhycfpnp71ANaZrOBqiWyMOwdZYNcd4yFws_WSnLloxIxkkiy0I_0CBfndZlcPHav-Q3ucYLcxUhTvrYfDj6_Sj31eSy3f_B1DooplEwW9yvYPvS1uGHeYgDmxS2xf4n-dR713xqe9S3jMPNzHYgPHslAGL1KbHj4qCQnPwH-EUdGQlaW1Al1-EhWEZMBI79wa7r6dxgBWj9go1i6UOjZKl0hyhq_pVPedOPH02vlPmqKzKyr6I-2wh0wpCU5p9eB9VBHsmhzMFOEiAeK-noijlXVmOqi8VbeSPtgxAnKmHwlaMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من سماء الاردن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/82147" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82146">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Homayoun Shajarian - Iran e Man (همایون شجریان و سهراب پورناظری…</div>
  <div class="tg-doc-extra">Melodifa</div>
</div>
<a href="https://t.me/naya_foriraq/82146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#شاركها</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/82146" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82145">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات تهز قاعدة موفق السلطي الجوية في الزرقاء</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82145" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82144">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">القوات البريطانية طيران من طراز تايفون في الأردن تشتبك الان مع سرب مسيرات إيرانية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/82144" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82143">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82143" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82142">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/82142" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82141">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=kIDzTgpmqJEyzJxZccZAE2cAI92ZSUciBWpHbNWxFqvORm3Bg5TsvageXbGEiqmVEKwfO2tnZZFaO5w4PeI5SGG5UZf2pvdxpqM00UQ8b7wEqokZP73QmoR-2HEWc3MAGqLKJodUJcXyCb8uL6j0Z1uxhaGl48nXVltG45nO0BOf3Zou119dDZSLq66HeAscRxfa9KAa56DWIyzphWUXRYDEAAWhfF45BQls51L8XvCg36LnCk5g837RxBG3pEJ2OHgQBlct7YtHJy_nu1ZtEUU3bihrSQnY9CvAprbRHY40WsD4tC3FgZ-Pb7WjAMsuD2QFBjilSCBhwHOZeUeKbb9rtMsnojY1SJoICEBBvu2o-uC32EuidxB_Dpvyq6p1xxaOzM1WR7GnjWAi-8X1N9zVBglfORWFDHBfu88iUHTfyoy3G6-IwpFfBont5aBWriZwnceaY6XfJifeZeHc8zhpeg9qkCIPkDGzlj4iV6rIpAjUaz6VOC8v9IGcb3cwnw4Sa6NBu-CrIOUVHtCT7VDGcZMEL6gF4PswHOBcMnVGdl0BZwHLcfIVr3qtEvaBM1dkojw0f8d81Sj1675QgvdpSlTc3pO7ZS2q0VP5-JL1hY-AaLLthZRZiV9i2BfMFiSX3_mq3cgek5aZTlnmwW48Sqym8qvDaPL0mNQlV88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=kIDzTgpmqJEyzJxZccZAE2cAI92ZSUciBWpHbNWxFqvORm3Bg5TsvageXbGEiqmVEKwfO2tnZZFaO5w4PeI5SGG5UZf2pvdxpqM00UQ8b7wEqokZP73QmoR-2HEWc3MAGqLKJodUJcXyCb8uL6j0Z1uxhaGl48nXVltG45nO0BOf3Zou119dDZSLq66HeAscRxfa9KAa56DWIyzphWUXRYDEAAWhfF45BQls51L8XvCg36LnCk5g837RxBG3pEJ2OHgQBlct7YtHJy_nu1ZtEUU3bihrSQnY9CvAprbRHY40WsD4tC3FgZ-Pb7WjAMsuD2QFBjilSCBhwHOZeUeKbb9rtMsnojY1SJoICEBBvu2o-uC32EuidxB_Dpvyq6p1xxaOzM1WR7GnjWAi-8X1N9zVBglfORWFDHBfu88iUHTfyoy3G6-IwpFfBont5aBWriZwnceaY6XfJifeZeHc8zhpeg9qkCIPkDGzlj4iV6rIpAjUaz6VOC8v9IGcb3cwnw4Sa6NBu-CrIOUVHtCT7VDGcZMEL6gF4PswHOBcMnVGdl0BZwHLcfIVr3qtEvaBM1dkojw0f8d81Sj1675QgvdpSlTc3pO7ZS2q0VP5-JL1hY-AaLLthZRZiV9i2BfMFiSX3_mq3cgek5aZTlnmwW48Sqym8qvDaPL0mNQlV88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الايرانية في سماء الاردن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/82141" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82140">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">إصابة مباشرة في الأردن للمجمع الصناعي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/82140" target="_blank">📅 14:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82139">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/82139" target="_blank">📅 14:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82138">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">استهداف بارجة وسفن أمريكية في خليج فارس الان</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/82138" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82137">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6cabe6ace.mp4?token=meqOD4GViRhpKIZHlY0Uu8kWSavIjx-pn-nP0d9WmMtmmqeF4aMsCXX3bNUQSh5Fj-daB1lylVJXzOPK2-FNYE2mmh8k-HJfseyEkmfb_fRbIdRq3u82cfbimShH3j88PPRrTdyTVgdK02NdXQoxzMh0yVfceoz8eTUrvFsLUxdLXSOXP_sMaMkK4D22o3jVHATOuIUFZpHtsGSpknSw7f6LXx6M2TAat5B-6FeaOSjc0cVRMn5Wkb8izkPdxkFcDPxlh3gj5_PJ77nD6kIq-7jz1LslogvVZg1AmlT-jkkuUFDm_lGnWavGWGq1cIiPTvFaJGn-QGJuiwSdE5R0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6cabe6ace.mp4?token=meqOD4GViRhpKIZHlY0Uu8kWSavIjx-pn-nP0d9WmMtmmqeF4aMsCXX3bNUQSh5Fj-daB1lylVJXzOPK2-FNYE2mmh8k-HJfseyEkmfb_fRbIdRq3u82cfbimShH3j88PPRrTdyTVgdK02NdXQoxzMh0yVfceoz8eTUrvFsLUxdLXSOXP_sMaMkK4D22o3jVHATOuIUFZpHtsGSpknSw7f6LXx6M2TAat5B-6FeaOSjc0cVRMn5Wkb8izkPdxkFcDPxlh3gj5_PJ77nD6kIq-7jz1LslogvVZg1AmlT-jkkuUFDm_lGnWavGWGq1cIiPTvFaJGn-QGJuiwSdE5R0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ ايرانية تنطلق صوب القواعد الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/82137" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82136">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">إطلاق صواريخ كروز نحو السفن الأمريكية قبالة البحرين</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/82136" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82135">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/82135" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82134">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات تهز على السالم في الكويت ومنطقة الميناء</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/82134" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82133">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/82133" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔴
الفرار الفرار..</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/82133" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82132">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=AtG0EHkeEVwa4g8rPffqjGO7-JFTBWoBjxSV9ukP4bSMVRWJ-TaSjRMakuDjTb0sFhWcVZPjfp36QLUG78bpwoiBnnD3rr5CENxdgTL-JZZBPN0uyECmJYMk8ns7CrT3vLBkZw0dj-o5NuQed7HuyFKX-l88J_qxGQzVYYxCkPUz620acrBrftbM_0Y59D5XsCFDFCk7S3Fr7cNs-1s3jYAmZrH9xVwFhh9HP2BwWAyns-bHzkxrszV4e7OZYiJHacqHcoVslU6a2gG3gktrEgPRfZsyNXjJlPiODITdA06WKOCdx9fxuQrD1iL0LuJGLQkaVle-6ATjSnYFF8vUNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=AtG0EHkeEVwa4g8rPffqjGO7-JFTBWoBjxSV9ukP4bSMVRWJ-TaSjRMakuDjTb0sFhWcVZPjfp36QLUG78bpwoiBnnD3rr5CENxdgTL-JZZBPN0uyECmJYMk8ns7CrT3vLBkZw0dj-o5NuQed7HuyFKX-l88J_qxGQzVYYxCkPUz620acrBrftbM_0Y59D5XsCFDFCk7S3Fr7cNs-1s3jYAmZrH9xVwFhh9HP2BwWAyns-bHzkxrszV4e7OZYiJHacqHcoVslU6a2gG3gktrEgPRfZsyNXjJlPiODITdA06WKOCdx9fxuQrD1iL0LuJGLQkaVle-6ATjSnYFF8vUNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ايران تبدأ بدك المصالح الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82132" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82131">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انطلاق موجة صاروخية من خيبر شكن الان نحو القواعد الأمريكية في غرب اسيا</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/82131" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82130">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ايران تبدأ بدك المصالح الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/82130" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfvtiP9Wj_0znDk9Unkv9cs2vaHYd70wnwLEB41BlH26zRv40-Nl7MNvaudllbTw69tBNVgd5SV7GCZoDFf7OCM4kSA0OU6iPCB0upcIL7lKiVuYYzaLIHJuns6zNqaG4QH0B2_m5jQPvD6Xh7yHuPoIbsWsFjCcT9zMA8xn7qCP5Ppz4dbed5ycmiXMLgMjG5Hst3cG6l2IbvmLzf9Np9SiX6YF_HJTjTqy_gbuo_enXSTtGNIJ9TmYvJvLYNogmxgT34iyp_TyXoBVdvUPGE-fsxAdWWfr3mu4_xsmM1EPTD7JB69IC70irLD18kOd3L3MYUg_pub1I_74nv80sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/82129" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/82128" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/82127" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/82126" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ايران تبدأ بدك المصالح الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/82125" target="_blank">📅 14:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سماع دوي انفجار في بندر عباس</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/82124" target="_blank">📅 13:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سماع دوي انفجار في بندر عباس</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/82123" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الايراني قاليباف في رسالة شكر للشعب العراقي:
لم يكن نداء الشعب العراقي النبيل والمُشرّف، في الجنازة التاريخية التي لا مثيل لها لقائد الشهيد وصاحب السلطة العليا في العالم الشيعي، إمام المظلومين، سماحة آية الله العظمى السيد علي حسيني خامنئي، الذي كرّس حياته النبيلة لوحدة المسلمين وكرامتهم وفخر الأمة الإسلامية، ولم يدخر جهدًا في الدفاع عن الحق وتحرير مظلومي العالم من هيمنة الكبرياء بقيادة أمريكا المتعطشة للدماء ومنع انتشار سرطان الصهيونية العالمية، مجرد وداع ومراسم حداد، بل كان إعلانًا عن دعم سلوك وأقوال هذا المجاهد الذي لا يُقهر وتعطشه للدماء من أجل هذا الحبيب، والذي وقّع عليه ملايين المعزين في مقابر أهل البيت (عليهم السلام) الكريمة؛ إعلانٌ رسالته الواضحة هي استمرار نهجهم، وصمود جبهة المقاومة، والتأكيد على وحدة المناضلين من أجل الحرية في جميع أنحاء العالم، بمن فيهم المسلمون والمسيحيون، والشيعة والسنة، والعرب والأكراد والتركمان.
إن احترامكم الذي لا مثيل له للسلطة الدينية والسياسية قد جعل كرامة الإسلام والمسلمين أكثر وضوحًا من أي وقت مضى، وأصبح شوكة في خاصرة أعداء الحرية والإسلام، وأظهر للجميع أن إرادة الأمم لا يمكن إضعافها بالإرهاب والتهديدات.
أعتبر من واجبي أن أتقدم بجزيل الشكر والتقدير إلى كبار العلماء والعلماء من الشيعة والسنة والمسيحيين، وإلى أقدس المراقد في النجف وكربلاء، وإلى القبائل الباسلة، والقبائل الدينية، وإلى جميع المشاركين في الموكب الجنائزي، وإلى حكومة العراق وبرلمانه الموقرين، ولا سيما رئيس الوزراء، والمحافظين، وأعضاء مقر النصب التذكاري، وقوات الأمن والجيش، والشرطة، والجيش، وقوات الحشد الشعبي الباسلة، وإلى جميع أبناء الشعب العراقي الذين شاركوا في هذا العزاء الجليل والذكرى الخالدة.
أسأل الله العلي القدير أن يحفظ كرامة واستقرار حدودنا المقدسة ووطننا، وشعب العراق الكريم.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/82122" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei31Lr8aaUF8OR58WG4fzwa73uj3xjpkF2r_k2wdJi_AwBHW-LS3VwriCsCrvP4DNKBfza5x6jg1VEPHK0uAc_CRMvwfnVxVaJiNQFvj8RRF8SeNdt65a3FHbdJIwRR1gVHKIioY2loVVXeP9-RuUgQ8nSkYyU7vJW5kKw2_fkqXb1Gu1o13c7I_fyIBfehFrqJLvsVoQPxwra1DBKMo_qCJQr3ak3TbhJkIP2Z_4hMjgLNS5g0_Q56-G_h5qn0_hqXfq_1TClIFEH_UPB2GDoOWCkhr-OZoKIyNz723O-bYo2vYTm8fzurSMJ4tVCOVAsw1RJVCBWfB4o9h5qoCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس مجلس خبراء القيادة في ايران يوجه رسالة شكر الى الشعب العراقي.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/82121" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
ضبط (51) كيلوغرامًا من حبوب الكبتاغون والإطاحة بمتهمين أحدهما عربي الجنسية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/82120" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مسؤولين صهاينة:
لدينا خطط هجومية جاهزة ضد إيران، إيران تعمل على إعادة تأهيل منظومتي الدفاع الجوي والصواريخ.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82119" target="_blank">📅 13:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dee24868.mp4?token=XxOS_OYhzHzFiJO_rnaAavEdzxkTFz02uMNuClCu9LjmCymAjXJg_EpitBlC4Tea4GOFdRW_LQTe5Re_5GxFEi2W_4bun1M8ud2ibKobTDWgOivVSFZ4LPDTQP7R6horF6ztHuA2lBKhLMipfKcDWwNROqalwNs02KZ1ZfPszM8atBN7bJknN81WXS8UhZzSPrkUo3cjtKv1IAfyOREYAc4wQwWxj8TfYsmv2PJA5eVi-7cv83Ea5BcAjHbw2NUObR83bJ6Qg8ncCYOqUPC_LSQhOxkHoIyxO9Ny-uYQbRSsolNLq4s-j6XGXBGkOdqkekSz7Bp74hYSiwUkdb1l6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dee24868.mp4?token=XxOS_OYhzHzFiJO_rnaAavEdzxkTFz02uMNuClCu9LjmCymAjXJg_EpitBlC4Tea4GOFdRW_LQTe5Re_5GxFEi2W_4bun1M8ud2ibKobTDWgOivVSFZ4LPDTQP7R6horF6ztHuA2lBKhLMipfKcDWwNROqalwNs02KZ1ZfPszM8atBN7bJknN81WXS8UhZzSPrkUo3cjtKv1IAfyOREYAc4wQwWxj8TfYsmv2PJA5eVi-7cv83Ea5BcAjHbw2NUObR83bJ6Qg8ncCYOqUPC_LSQhOxkHoIyxO9Ny-uYQbRSsolNLq4s-j6XGXBGkOdqkekSz7Bp74hYSiwUkdb1l6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
بينما يقوم الجولاني بالامتثال للضغوط الأمريكية من قبل ترامب والاستعداد للتدخل في مواجهة حزب الله في إطار مساعٍ لإزالة سوريا من قوائم الدول الداعمة للإرهاب.. مجندة في الجيش الإسرائيلي برفقة عدد من المجندات يقدن قطيع أغنام على أنغام أغنية سوريا بدها حرية في محافظة درعا السورية حيث كتبت أعلى الفيديو "إرسال وفد من الأغنام والأبقار لتدريب الجنود السوريين على مهماتهم الجديدة."</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/82118" target="_blank">📅 13:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82117">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Loq7BAt088MBAqmzUq4ca28r096x_9ZWeqrOYhwBOBYpiOzx8Wf69MzhCGGNW9GxOyEMyvxpu4wgWZj-hJFc3LDQrcEtLs6WKwTGgel50M_VzcGKt4rQvMBnhEE-GZigx8aTiYCNRfllA1AXhM5I_siPpnUGJX0qPA55xvtTpTGbHw2oJu2IvVIgAX20tQ1fHzTTMiZVdF0VK-TZ-qPI2bTxrtq--QU_DOyJAbTCBRuN8nMtFNAifZCfVeV78Vcq2Q0e6zDxoTzfnaQFkuSCeonOntK-al4FHGqPj6MdbAi86NS-DMZ5KWR9Yl8iKE5xAOhcyAcmUHjerv2q8H9zIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لجنة المحتوى الهابط في وزارة الداخلية العراقية تتخذ الإجراءات القانونية بحق المدعو جاسم العوادي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/82117" target="_blank">📅 13:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82114">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAfoOei-nEDp0svSRdlaxdNgHq_2rJ7028kP4AqEFpxK71sqWK2zBMejIa7OSKDQJuEW2DSFB2bzJnuGSXL40EADQoZ5GGuAiaKhH5YWQ6kXsHv-KOXZOkysKmeJggFBwHNFeXxXzspOujXN5JEFBG_G09QHDuwzXvgf6krooYeyNVSB69e8gt6hwHFb-6Ez5as-tOriGzTE8sWEBwpjEgnTqgoMokMzQHHGc7teqD_VGU1GE_lXleyPyC-Ezp7GvK348Qqq9i3m7r-mUVRr7GEq4hBRNryUkJTYGYxnxIJJNYEBg273nSqQ2nHQBeBsO1__-nB3RsD9E3Tt6IzEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0zdQGoTNlMqPT7piz6D2txahHg_mcU8idDPHJbNtk-RBzxWS62X5R-l7Gs8dh4BnwU7P713vzt6LBAiyXss7hARPjxt1bFePwxsiyXI04ACRSoLpTsCXcbU6CeV8D3KtEbxW2yjIKiU-8fvYS04NgQKQhIYAUVM8Uy3DhBCsmsNoUNuJIFCmwzBLrFIottAk7bU_R94otmcXZb9UH7ugxu4TpCU65h3jlOdQVIDF7pS9RbkRRPZuDlKKFgf9DQDZ-7CSmPejfj9Uylyxa7pvWnEJVg0ZGsH7XBVUCUkNxXQjmBqDGQoW1Cf3_N3J7bTiDti2FraQ9AN5iZETil_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlhIp689-9ukblOsA0uFbRCDhR4qfpCgLkFsGgH9Nz_HjlXACvqaqW5q6MEfIgzS9h_OrF6wigF3EG5dqCTISNtzkEheqLf9rU3i_Bl7HynQzRQ3ZBhmoF5dboatKidyt03O0MpQDB66QgPLk0KFmTLuu32VAO0mm9CxzIJJCPDG1AbjlZRSIiOPCVlexdjhOmgwyPWlLcgijhPwu2m7HhUUi3UodvkheMS6s0SOufEFGpv1iVzq41jxSO6-kaG_awozFKFJCl_NRph6u-1V-lsYD8lq4wF_HWUH6XT-eGGnBWaT_rJqFoyAaD1zBpYAlGmm3iXMLX0-IEEtZWcjCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاأني يصل مشهد قادما من العراق برفقة جثمان القائد الشهيد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/82114" target="_blank">📅 13:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82113">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
🇷🇺
الكرملين بشأن فرض منطقة حظر طيران فوق أوكرانيا: هذا يعني أن حلف الناتو سيعمل في أوكرانيا، سنمنع ذلك.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/82113" target="_blank">📅 13:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82112">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سماع دوي انفجارات في بوشهر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/82112" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82109">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed623cc58f.mp4?token=vraT3sDOFdm8sRSjpgfUEsfygSnmDeWpu1TVzJaLgZwjqlIcxNvrRm5rD6m0Vrwgjt05APoT3XiWjlawEXwX-wCgY1mOrvH1fTwHYsOmTQxTnGya67wXFxDt--dxXTvydljUC6kwLiHSRZxme9LlQmhyw2BQ99oESygl_KHWfXniIncnUCDOkG0j6ZL8I6z5iqTJfPX4eT6CXdVqE0KAnZqmRsV2keNsCSiLHPxYmdG0IIyzww9raiA2KoivRj3kWlJXu4bWtpjFEL2lf4OSfjiquG-L50XfHM1MDmu_dGSsNA4Nl8bZHJEr6n6PL08INH0k9hlyszAOPHp2hluV8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed623cc58f.mp4?token=vraT3sDOFdm8sRSjpgfUEsfygSnmDeWpu1TVzJaLgZwjqlIcxNvrRm5rD6m0Vrwgjt05APoT3XiWjlawEXwX-wCgY1mOrvH1fTwHYsOmTQxTnGya67wXFxDt--dxXTvydljUC6kwLiHSRZxme9LlQmhyw2BQ99oESygl_KHWfXniIncnUCDOkG0j6ZL8I6z5iqTJfPX4eT6CXdVqE0KAnZqmRsV2keNsCSiLHPxYmdG0IIyzww9raiA2KoivRj3kWlJXu4bWtpjFEL2lf4OSfjiquG-L50XfHM1MDmu_dGSsNA4Nl8bZHJEr6n6PL08INH0k9hlyszAOPHp2hluV8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
ميدان انقلاب في طهران..
الشعب الايراني يشكر الشعب العراقي على التشييع المهيب لقائد الثورة الشهيد في العراق.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82109" target="_blank">📅 12:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82108">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
🇬🇧
وزارة الخارجية الإيرانية تستدعي سفير بريطانيا لدى طهران بسبب تصريحات مسؤولين بريطانيين ضد الجمهورية الاسلامية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/82108" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
