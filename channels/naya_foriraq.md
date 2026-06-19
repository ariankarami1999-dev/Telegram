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
<img src="https://cdn4.telesco.pe/file/ILFfzXvlLing9qpJA7wweanoimpDbZivp2PtaP2P0Nry5n_hsRXOEYJ-mbdNiBKSAhn6POjno9GZwE64HlDLhDY2q6MZ2T05G8ZKFitH2Xp9hSZsefFuH7lbAJJixiLgtvT-AGZGGfC0sE-clfpAZbVrGlYfT9wrZ4B-VffFKi8_zoQ2bwXnfmpNUpdxN3L8w6hTUefXGWy058WxVM8z1c_ITnoT5lJwsgzhg1hp8bqXoJ7oxKeIV4zRoenun1OMsLymAGY02Th10yQH2Hd8zT1Ga5WwO2xpQhZdZ4dvoCkT5BDU-bH0GXXcUig3mrvoNZuD51qdOoQGmD4ja-rWaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 21:45:51</div>
<hr>

<div class="tg-post" id="msg-79325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
ترامب: الإيرانيون أشخاص أذكياء جدًا. إنهم نوعًا ما من عبقريين بدائيين، لكنهم أذكياء. كانوا سيفجرون إسرائيل. لولاي، لم تكن إسرائيل ستوجد اليوم.</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/naya_foriraq/79325" target="_blank">📅 21:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
ترامب:
الإيرانيون أشخاص أذكياء جدًا. إنهم نوعًا ما من عبقريين بدائيين، لكنهم أذكياء. كانوا سيفجرون إسرائيل. لولاي، لم تكن إسرائيل ستوجد اليوم.</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/naya_foriraq/79324" target="_blank">📅 21:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
🇮🇷
أوباما حول اتفاق ترامب مع إيران: كان هناك اتفاق توافق فيه إيران على عدم تطوير أسلحة نووية.  هذه الإدارة - أو نسخة سابقة من هذه الإدارة - انسحبت منه، مما أدى إلى قيام إيران بتطوير المزيد من القدرات النووية.  لقد خضنا حربًا الآن، وأنفقنا مليارات ومليارات…</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/naya_foriraq/79323" target="_blank">📅 21:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79322">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncnZxg5Ce3ZYjC2MdA_FtC_C1v5GRGvGobG_guddtyAO3KtfmKLip9QIqR0V0MV_I4r9kF6NxGtlime5qYHJ3i5uQtLlKUhheAeoGuvXKmAY2IbS437CpdN_LXmjlT7nHrQXxx_CO1Eq4LISj8YXhWt3ewkJqVLkTQyT8kCYbaYkepR7y5dANivNwpmHXVJ6kBghObkKRRsfnV0mwHtUqRfcccDwV5ekLZFZNDyyE06mDa9AuhoEbBKHMSwyPFrtxQRQjuTIWMgkJ2RkPwnsCU68rjqtsGSLSZ7IdKdJzEsnpLhfq8BkqvFRW069HT4HJ6Y_c7CYzaH1q1RbS-iyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري الإيراني اللواء قاآني:
بسم الله الرحمن الرحيم
عندما قلنا إن حزب الله يراقب، لم تُصغوا، فوقعتم في الفخ؛ من سيُحاسب على المئة قتيل؟  غزة أيضًا في عاصفة. إذا تحركتم وفقًا لرغبات سياسيكم، فستقعون في العاصفة. كونوا حذرين.</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/naya_foriraq/79322" target="_blank">📅 21:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
🇮🇷
أوباما حول اتفاق ترامب مع إيران:
كان هناك اتفاق توافق فيه إيران على عدم تطوير أسلحة نووية.
هذه الإدارة - أو نسخة سابقة من هذه الإدارة - انسحبت منه، مما أدى إلى قيام إيران بتطوير المزيد من القدرات النووية.
لقد خضنا حربًا الآن، وأنفقنا مليارات ومليارات من الدولارات، وفرضنا ضغطًا هائلاً على جيشنا، ومات الكثير من الناس، ويبدو أننا عدنا إلى المكان الذي كنا فيه قبل بدء الحرب، بل ربما في حالة أسوأ قليلاً.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/naya_foriraq/79321" target="_blank">📅 21:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يسمح بنشر إسم أحد الجنود القتلى في جنوب لبنان وهو "دور بن سمحون"قائد كتيبة 52 ونائب قائد الكتيبة ، بينما لم ينشر أسماء الثلاثة الآخرين حتى الآن.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/naya_foriraq/79320" target="_blank">📅 21:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
🏴‍☠️
جي دي فانس حول الكيان الصهيوني:
إسرائيل
شريك جيد بنفس الطريقة التي تكون بها المملكة المتحدة أو فرنسا شريكين جيدين.  هذا لا يعني أنه سيكون لدينا دائمًا مصالح متوافقة.</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/naya_foriraq/79319" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534464594.mp4?token=ttosRvvsdPnI2JRvTvz9_gn1wu_orFOU_uUWli1wrztpBz46nQQVQbvqMo0YO1al-lI_XxHeyphFo283JUTEDSBorFv5yLydritYFSOI7ceOtsDuDBcBulZrW-1wCWukM7kqpKhMKuh4laLiQ4XVrsjYssA8sqC_ESrClrD1HNSywE7pVFe5vKCOYSHOPLMXu0iKgM9msmbh3t6M7jxLijuloh72Tu2qei0tDQsTNcdj1aset9cvwIb2RngknThNNWtnWen6B3WA1kRjC2rQLfAMH8Oc0W9LCUizVVlnFOZ6bZOyIBV_IdlXXoXHcYXkKS3R1dZwPdP6LGcK-18FDkZaxsEsfmGWX2cMzwViPeWeRtN-XEzmYn_dYyY4FOFUNzKu7uCtBStGxwSqi-uRvvaeA37LXlestf4UZK0vbQzvb9ZVKPE9Vl2DyOq7GAUNKK96PZM98LY92ZsF9_xSJsbD93vPYRhCvYBZyIN_waqLY7rl_nBLE1J2_x2-hKUOJ3HEgx6G8yentItTbsoz7Dm24eLShXJqvwY5jrHNneoSiiwPIO_HIJguDmXTRQQEzgEtsnsYjz32ZQwp8qPWYEj0ol6mzr4UlYKBXCsJCFXcldt_AtzDnH2pHUX2FfbX3F4WYJ3-RR_uBXWwn7g2mEP_tOZZM7IUYUnZucmHA3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534464594.mp4?token=ttosRvvsdPnI2JRvTvz9_gn1wu_orFOU_uUWli1wrztpBz46nQQVQbvqMo0YO1al-lI_XxHeyphFo283JUTEDSBorFv5yLydritYFSOI7ceOtsDuDBcBulZrW-1wCWukM7kqpKhMKuh4laLiQ4XVrsjYssA8sqC_ESrClrD1HNSywE7pVFe5vKCOYSHOPLMXu0iKgM9msmbh3t6M7jxLijuloh72Tu2qei0tDQsTNcdj1aset9cvwIb2RngknThNNWtnWen6B3WA1kRjC2rQLfAMH8Oc0W9LCUizVVlnFOZ6bZOyIBV_IdlXXoXHcYXkKS3R1dZwPdP6LGcK-18FDkZaxsEsfmGWX2cMzwViPeWeRtN-XEzmYn_dYyY4FOFUNzKu7uCtBStGxwSqi-uRvvaeA37LXlestf4UZK0vbQzvb9ZVKPE9Vl2DyOq7GAUNKK96PZM98LY92ZsF9_xSJsbD93vPYRhCvYBZyIN_waqLY7rl_nBLE1J2_x2-hKUOJ3HEgx6G8yentItTbsoz7Dm24eLShXJqvwY5jrHNneoSiiwPIO_HIJguDmXTRQQEzgEtsnsYjz32ZQwp8qPWYEj0ol6mzr4UlYKBXCsJCFXcldt_AtzDnH2pHUX2FfbX3F4WYJ3-RR_uBXWwn7g2mEP_tOZZM7IUYUnZucmHA3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في الأطراف الشرقية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/79318" target="_blank">📅 20:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
🏴‍☠️
إن بي سي: ‏تحدث ترامب مع نتنياهو في وقت سابق من يوم الجمعة وطلب منهم الموافقة على وقف إطلاق النار مع حزب الله.
🇺🇸
ترامب: لطالما عاملت نتنياهو بشكل جيد ويتوجب عليه فقط الهدوء أحيانا وإعمال العقل.</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/naya_foriraq/79317" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
🏴‍☠️
إن بي سي:
‏تحدث ترامب مع نتنياهو في وقت سابق من يوم الجمعة وطلب منهم الموافقة على وقف إطلاق النار مع حزب الله.
🇺🇸
ترامب:
لطالما عاملت نتنياهو بشكل جيد ويتوجب عليه فقط الهدوء أحيانا وإعمال العقل.</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/naya_foriraq/79316" target="_blank">📅 20:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79315">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">أضافت فرقة العمل المعنية بالإجراءات المالية البوسنة والهرسك والعراق إلى "قائمتها الرمادية" للولايات القضائية التي تتطلب مراقبة متزايدة بسبب أوجه القصور الاستراتيجية في أنظمة مكافحة غسل الأموال وتمويل الإرهاب.</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/79315" target="_blank">📅 20:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79314">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
الاستخبارات الأمريكية حذرت الإدارة من أن نتنياهو قد يقوض جهود اتفاق سلام دائم مع إيران.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79314" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79313">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
عملوا على الضغط على سوريا من أجل أن تتدخل من الشرق لتكون كماشة هي و"اسرائيل" من الشمال.
المخطط يتضمن إقفال كل المعابر لمنع وصول السلاح والتقنيات وكل ما من شأنه أن يقوي المقاومة.
المخطط يتضمن فرض حصار مالي شامل وتحريض الجيش ضد المقاومة.
عملوا على الفتنة السنية الشيعية تحت عنوان حماية موقع رئيس الحكومة بالقرارات التي سيأخذها ضد المقاومة.
سقط مشروع إنهاء حزب الله وتثبيت الاحتلال وستخرج
إسرائيل
من آخر شبر من أرضنا.
لا عودة إلى ما قبل الثاني من مارس وإخراج العدو من أرضنا سيتحقق.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79313" target="_blank">📅 19:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79312">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMarnj5zdZSdOJV-xV1cBQmy51YNKpofnc3o3lVEz4m97IZ-xnOizic-R0dgXyE8khzev6NwrhmUN4iUg_UUXlwB1qoUxUmu1K3LgxO0CsmfsRizxACUniy9qKhSfkwIf_eq8dz1DuuPTyeloSjXgavJCg2j41rDcToo3gd3EYnCp-nSLeWxRkPLrV1aNiuKxLdpdJw7U1uoD4wfSMdGz-R0FpN4deCJBG7OV1-Zpfjrt-TOk49bw_1PKZtWN7zSooaioB86PbP6UvXxVoqY76tAL-sMHSkwxWTZ8MEPz8reshVIHl2qXXT1JaPETlBc5WVWN6-gXYDiQahTPx2TFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇹
توتر العلاقات بين الولايات المتحدة وإيطاليا يتصاعد..  ألغى وزير الخارجية الإيطالي أنطونيو تاجاني زيارته إلى الولايات المتحدة الأمريكية عقب تصريحات الرئيس الأمريكي دونالد ترامب المسيئة لرئيس الوزراء الإيطالي جيورجي ميلوني.   تاجاني: "إن تصريحات الرئيس ترامب…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79312" target="_blank">📅 19:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79311">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">"انا وايطاليا لا نتوسل ابدا".. رئيسة الوزراء الايطالية تنشر فيديو غاضب من ترامب بعد تصريحه ان ميلوني توسلت له من اجل ألتقط صورة معها!  جورجيا ميلوني:  يجب أن يتذكر شيئًا واحدًا: إيطاليا وأنا لا نتوسل أبدًا. تصريحات دونالد ترامب ملفقة تمامًا. أشعر بالصدمة بصراحة.…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79311" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79310">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpItC8w2F9WKE1L433c3M8gHpLk3gurD5vq3KbOJ-V3wS8OVxojCz-peq_xAQKkApkgp0ltIAUsi0yKlzR8i4jZzSB84taTDcuwUDyZyUT3eAlBH0UF9WuKkBPKrYmDkXrlo3Hz3DBRAxCSjnuaFnghTtHVoO37gaAcs2rCWrh0zXAxjuiOAd4h1ReymXC18xyjD6xYdfhE8oM4Qf1kVGnKI1xUmKgJZEjam515d0KcnZO1-D7muz1HdQLC0dgvA34enOvOlYx7mja8xCl8RMOCzQOGjkhaCuWB7XdW43MhY_gpFBBJrEQ2JTZ2FjMj7N0AsqiC7_WN7JlO6Y5sbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة  يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.  التاريخ: يوم الجمعة 2026/6/19 الوقت: الساعة الخامسة مساءً المكان: بغداد الصالحية -…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79310" target="_blank">📅 18:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79309">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a3ed5b25.mp4?token=v7Dlxo1sr3VLpFZmY5eZZkfDVKiH4VsK4xF7YQwxAjYmDF4ukiGnudnQCllJNVxApw0-4LApKtitQPSn0rBtGb5Ra4HNEsv2FE7Bqb6T1PW7Z3gM4fFhQvZ6rXHbBvv_fCItTgm6juxJxWIQh9oHWmQGOJ3E8iB1zcUu7wZrrU6LPOb1KWhI5GggpHh_MYv1SDQWMHJgsZIBKmyzwtLGvIuzrfKe2bSwE6owdsZdHqLsfhNGzMh3uNHSiIq_lj8FdDNXR2StjC7ahiEXRW40FDT9Z6F6h32M50nVfoey1zt7nChi7wWY5oeMLEBN0hAy7FG_7D_GbwMQoaKeiYNL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a3ed5b25.mp4?token=v7Dlxo1sr3VLpFZmY5eZZkfDVKiH4VsK4xF7YQwxAjYmDF4ukiGnudnQCllJNVxApw0-4LApKtitQPSn0rBtGb5Ra4HNEsv2FE7Bqb6T1PW7Z3gM4fFhQvZ6rXHbBvv_fCItTgm6juxJxWIQh9oHWmQGOJ3E8iB1zcUu7wZrrU6LPOb1KWhI5GggpHh_MYv1SDQWMHJgsZIBKmyzwtLGvIuzrfKe2bSwE6owdsZdHqLsfhNGzMh3uNHSiIq_lj8FdDNXR2StjC7ahiEXRW40FDT9Z6F6h32M50nVfoey1zt7nChi7wWY5oeMLEBN0hAy7FG_7D_GbwMQoaKeiYNL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوة عامّة  يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.  التاريخ: يوم الجمعة 2026/6/19 الوقت: الساعة الخامسة مساءً المكان: بغداد الصالحية -…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79309" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79308">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭐️
نيويورك تايمز:
وفقًا لكتاب "تغيير النظام"، أشار ترامب خلال اجتماع رفيع المستوى في المكتب البيضاوي قائلًا: "أنا لست معجبًا كبيرًا بأوكرانيا. باستثناء نسائهم. فهن يواصلن الفوز بمسابقة ملكة جمال الكون".</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79308" target="_blank">📅 18:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79307">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
ليس لدينا أي خطط لتفتيش الوكالة الدولية للطاقة الذرية للمنشآت النووية الإيرانية. والخبر الذي نشرته بعض وسائل الإعلام بأن الجمهورية الإسلامية الإيرانية قد دعت الوكالة الدولية للطاقة الذرية لتفتيش منشآتها النووية غير صحيح. إن تفتيش المنشآت التي مُنعت الوكالة من الوصول إليها بسبب الهجمات العسكرية الإجرامية التي شنتها الولايات المتحدة والكيان الصهيوني، سيعتمد على سير المفاوضات ونتائجها.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79307" target="_blank">📅 17:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79306">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
أيدينا على الزناد وآذاننا على أوامر القائد الأعلى للقوات المسلحة، نحن على استعداد لحماية أمن الأمة وكرامتها ومصالحها من خلال التضحية بأرواحنا في حالة حدوث أي إخلال بالواجب من جانب العدو.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79306" target="_blank">📅 17:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79305">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6485ab46f4.mp4?token=fVYlztGr6I4kils6LwulOWXiQUsXUNxBgwe5WA4taMgUQPzfm8ZxLkZAm_lmbn_8luawf8yEq4SSzmg7nICepS3T4haLH_ndxjY_cLzvUBSme2u3jpzjSES4ZSmEhHjc73qCSsTpA3ZxdLXW36bpEq2ECnASu7j8Krcgb7PAPMLUapAjVAqyuuifGFiUKETUNy2mudJaly6QaywCTE6PosWDb_UaQW9jVpWJJhYoIr7lacfJjxOZDs9wkYT8a_fioujbOKyml7kCNGzh_Dpg7fZV7VbiBcjrh3VxmD_ONFL1pvVJ0spnXvpK64OKKBoVA87ss5Kh2DkeTjq0rUpWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6485ab46f4.mp4?token=fVYlztGr6I4kils6LwulOWXiQUsXUNxBgwe5WA4taMgUQPzfm8ZxLkZAm_lmbn_8luawf8yEq4SSzmg7nICepS3T4haLH_ndxjY_cLzvUBSme2u3jpzjSES4ZSmEhHjc73qCSsTpA3ZxdLXW36bpEq2ECnASu7j8Krcgb7PAPMLUapAjVAqyuuifGFiUKETUNy2mudJaly6QaywCTE6PosWDb_UaQW9jVpWJJhYoIr7lacfJjxOZDs9wkYT8a_fioujbOKyml7kCNGzh_Dpg7fZV7VbiBcjrh3VxmD_ONFL1pvVJ0spnXvpK64OKKBoVA87ss5Kh2DkeTjq0rUpWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادث سير عنيف على طريق العمارة - المجر في محافظة ميسان ؛ وفاة وإصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79305" target="_blank">📅 17:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79304">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">طيران مسير يخترق أجواء مستوطنة زرعيت في شمال فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79304" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79303">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
🇷🇺
إيران:
المتخصصون الروس سيعودون قريباً لاستكمال بناء محطة بوشهر.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79303" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79302">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏مسؤول أميركي كبير: نتنياهو وافق بنسبة 100% على وقف النار في لبنان</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79302" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79301">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇱🇧
🏴‍☠️
حزب الله ينشر:
لا مناطق آمنة لـ "إسرائيل"... وسَتَرحَل</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79301" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79300">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
جيش العدو: سنهاجم بقدر ما يلزم، تعليمات رئيس الأركان لم تتغير ولا توجد قيود على القوات في الميدان.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79300" target="_blank">📅 16:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79299">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
سنهاجم بقدر ما يلزم، تعليمات رئيس الأركان لم تتغير ولا توجد قيود على القوات في الميدان.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79299" target="_blank">📅 16:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79298">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e0661b1f.mp4?token=bkRJKIMKFN0g-YKSJT3Bs0ikV7p2krb4uKBU3pJwDp6G44S1WAoEcaQrs1FaQxjlEcPy_jOt6ycWoBiNcIj2fFkViC7vRE92320UVaKi4wFBf01Y97XEytC-rMxA4MB6n90KluzWx6HUmmSCEFcamVCrnAipi1hZxg2sg7CuMTtWqcCvVTE9X2eh2EzKflDGAZexWzhkKyE3PqoukQ7gfM2f6NbdkK7g2W7AcKYpJh0ObX7G7PXqGCUf30rXKkskpXVTfNR7H6sHGLuf4kSqx2beIwFin-FAkU1lQuGI-ESeVJIUfbxl5ns9ecP0GrBeF_sYXPfAvjPLE9JfMKfOUZkv5jOsVRAScghlkyTa5w8opKyQyV6pOrEj2rEXtM5qh0aiU_rU5PVy_sQ9d0jnZBNZq16T80u6nBwuLY5Ok1L9RqdGn1xMyNPcnwseNse3Fht4fWJhqOtRF40M0OVwZxeZMaC2QFtUa6d3qI4s_qAj4-5yMWsoJHDdpMC62g5K0LF-rsBbSDTJKukSWE2m4m9x9b-Op57qYAr5GLvlHOAeB9IciE02AXolr3noi2UBlYN-cJCfmlNwCveAUMstgpXnjug_GGZmR_GpL7FFyxJkUjnEYS_53UgcjmyGkPpu9D9lhYLct_8pljGCV6c9zJyq_aKFOS6yC6EGNJdQfEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e0661b1f.mp4?token=bkRJKIMKFN0g-YKSJT3Bs0ikV7p2krb4uKBU3pJwDp6G44S1WAoEcaQrs1FaQxjlEcPy_jOt6ycWoBiNcIj2fFkViC7vRE92320UVaKi4wFBf01Y97XEytC-rMxA4MB6n90KluzWx6HUmmSCEFcamVCrnAipi1hZxg2sg7CuMTtWqcCvVTE9X2eh2EzKflDGAZexWzhkKyE3PqoukQ7gfM2f6NbdkK7g2W7AcKYpJh0ObX7G7PXqGCUf30rXKkskpXVTfNR7H6sHGLuf4kSqx2beIwFin-FAkU1lQuGI-ESeVJIUfbxl5ns9ecP0GrBeF_sYXPfAvjPLE9JfMKfOUZkv5jOsVRAScghlkyTa5w8opKyQyV6pOrEj2rEXtM5qh0aiU_rU5PVy_sQ9d0jnZBNZq16T80u6nBwuLY5Ok1L9RqdGn1xMyNPcnwseNse3Fht4fWJhqOtRF40M0OVwZxeZMaC2QFtUa6d3qI4s_qAj4-5yMWsoJHDdpMC62g5K0LF-rsBbSDTJKukSWE2m4m9x9b-Op57qYAr5GLvlHOAeB9IciE02AXolr3noi2UBlYN-cJCfmlNwCveAUMstgpXnjug_GGZmR_GpL7FFyxJkUjnEYS_53UgcjmyGkPpu9D9lhYLct_8pljGCV6c9zJyq_aKFOS6yC6EGNJdQfEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انا وايطاليا لا نتوسل ابدا"..
رئيسة الوزراء الايطالية تنشر فيديو غاضب من ترامب بعد تصريحه ان ميلوني توسلت له من اجل ألتقط صورة معها!
جورجيا ميلوني:
يجب أن يتذكر شيئًا واحدًا: إيطاليا وأنا لا نتوسل أبدًا. تصريحات دونالد ترامب ملفقة تمامًا. أشعر بالصدمة بصراحة. لا أعرف لماذا يتصرف رئيس الولايات المتحدة بهذه الطريقة تجاه حلفائه! بعد كل شيء، هذه ليست المرة الأولى التي يحدث فيها ذلك. كل ما يمكنني قوله هو أنني آسفة لأنه لا يبدي نفس الحزم والصلابة تجاه أعداء الغرب، وأعداء الولايات المتحدة، ومع تلك القيادات التي يظهر تجاهها، على النقيض من ذلك، قدراً كبيراً من التساهل والمداهنة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79298" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWTl3QTeTdJHM1BTUeZFUihecewD5LMKaArmU9zJT4l4vmeWRr2_V-hCNtXYK2A_pliFQz97eJt3q8XMijwXd-JPwasbgTKq-PZermWa_IPBXyU45mWbD_Wonno_ihs12H3VEOqOxcCjKGk2uTjHUu7KWrUvG8Zl6NPeTQZAS0hpVh6eDjT1PSY4U_lVzvzuuKOOAH4Jc4QwHWISStGBYJzgZlR3ySKzlamYVtS_S2WTApXkKG_JA2cLzpBHzNNyfnmwUpntpeeKSCNGzVsL_T2vF3fYzn5C7r1WmCL0DphA39s-wyhhhYqw3PFCzmds30sRce6hbMlMH1DEL70t6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مسؤول إسرائيلي: نحن الآن في وقف لإطلاق النار وإذا لم يهاجمنا حزب الله فإنه ليس وقت حرب من جهتنا.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79297" target="_blank">📅 16:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79296">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">العدو الصهيوني يشن غارات على جنوب لبنان في اول خرق لاتفاق وقف اطلاق النار المزعوم</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79296" target="_blank">📅 16:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79295">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وقف اطلاق النار المزعوم من قبل المسؤول الامريكي يدخل حيز التنفيذ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79295" target="_blank">📅 16:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79294">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
وزير خارجية النظام الصهيوني جدعون ساعر يناشد الاعلام الغربي بعد العزلة التي يواجهها الكيان الصهيوني:
تصور الكثير من وسائل الإعلام الغربية إسرائيل كنوع من المشروع الاستعماري، كما لو أننا لسنا السكان الأصليين في هذه الأرض - شعب كان هنا منذ أكثر من 3000 عام وحافظ على وجود مستمر هنا عبر التاريخ.
تصورنا دعاية الجانب الآخر كشكل جديد من أشكال الاستعمار.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79294" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79293">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مسؤول أميركي: اتفاق وقف النار يدخل حيز التنفيذ عند الساعة الـ4 بتوقيت بيروت.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79293" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79292">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏رويترز عن مسؤول أميركي: إسرائيل وحزب الله اتفقا على وقف لإطلاق النار اليوم.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79292" target="_blank">📅 16:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79291">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏
رويترز عن مسؤول أميركي:
إسرائيل وحزب الله اتفقا على وقف لإطلاق النار اليوم.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79291" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79290">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
‏ترامب: لن تحصل إيران على أي أموال ولا حتى 10 سنتات.  والـ300 مليار دولار الي وقعت عليها
😄</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79290" target="_blank">📅 16:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79289">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2xCYrfNv-QY2z7es4AMdqqh5tVeXiPUg_GAoG_ZGHnnEuX7jNXqyAOwjOsyouTnbfEgRfD37er7uQtM4qCFC6U9RpmFazrNQa61nuQ96_x37PsAkIIvb1Cdq-2e8f7ZlljcfGiPM6527h1pskZ4hX8O0F4P04bWzamDuVidgljLckmJknllDecdOl5YZkP_LihhxDbnX7iU-mBqrBQOEkwj7zYW1Qf83_8F6ChzxklGKzXH9JIMR4zfb22ZlKMvMy0Zah6qGc81DmDNf9EZQyPzKTy40px52xVoqXiBcD3VAnlGNd2tGmoYFgncBXl0fhfJGs4lwV4hJvbCD6tjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
لن تحصل إيران على أي أموال ولا حتى 10 سنتات.
والـ300 مليار دولار
الي وقعت عليها
😄</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79289" target="_blank">📅 16:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79288">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مسؤول صهيوني:
إيران تقف وراء الهجوم الليلي لحزب الله الذي قُتل خلاله الليلة أربعة من مقاتلي المدرعات. والهدف هو دفع إسرائيل للهجوم في الضاحية وبذلك تعميق الخلاف مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79288" target="_blank">📅 15:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79287">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpXiSGXaN7kHKQE5pW3z15nTnkqgcyGca7DI6e1rvpZgrkFcMedUNpSXU98cA2_lZUV97jQLyxlTafnlnmvf1ucKD5_K1exOoTrd3R9QS3iF9fuqkAb-5SvDZHo0KfkhrDl_rTHp1_nIsNydd3YD-S41S-pBXqV4yyWcAVS-hqGLk3Xgb3WvZ1ztvo1poiIuZNV6yQoHjM4L4TgGXioaVF74kuXoJ3znNgPEA6Shc8WO7ipYK9tHLHWNHmULs84gy7L6KWgmTs0ikjpYaKy1_CbY1QDsieQKRUjYRx2amMZr2puJ_KKapoo7PY7CQrY9igva_2q1fEfwehKuGwEGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🏴‍☠️
وزير الخارجية الايراني عباس عراقجي يشارك تغريدة بن غفير:
هذا ليس هذياناً صادراً عن مجنون إبادة عشوائي. إنه منشور رسمي علني لوزير الأمن القومي في الكيان الإسرائيلي.
منظومة القتل الإبادية المتمركزة في تل أبيب، تشكّل تهديداً للإنسانية جمعاء. إنها تهدد كل البشر. وليس لها من هدف سوى الحرب الدائمة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79287" target="_blank">📅 15:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79286">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن
مسؤول رفيع في الكابينت
: لا يجب الانجرار إلى سياسة رد فعل. يجب فرض ثمن باهظ على دولة لبنان لكي تمارس ضغطًا على حزب الله.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79286" target="_blank">📅 15:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79285">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق هرمز الإيرانية: لن يتم فرض أي رسوم على السفن التي ترغب بعبور المضيق خلال فترة الـ60 يوما، سيتم السماح بمرور السفن التي تتقدم بطلبات العبور وتلتزم بالمتطلبات.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79285" target="_blank">📅 15:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79284">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق هرمز الإيرانية:
لن يتم فرض أي رسوم على السفن التي ترغب بعبور المضيق خلال فترة الـ60 يوما، سيتم السماح بمرور السفن التي تتقدم بطلبات العبور وتلتزم بالمتطلبات.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79284" target="_blank">📅 15:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79283">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇱🇧
حزب الله ينشر:
אם כבר נסוגים, אז למה שתהייה ההרוג האחרון؟</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79283" target="_blank">📅 15:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79282">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
وكالة فارس:
اغلاق مضيق هرمز قرار يمكن طرحه في إطار قرار المجلس الأعلى للأمن القومي كحل رادع لإجبار أمريكا على كبح إسرائيل. وإلا، فإن انتهاك اتفاقية الاستمرار سيستمر وستتحمل الطرف المقابل تكاليفه.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79282" target="_blank">📅 15:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79281">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📰
‏
سي إن إن:
الولايات المتحدة أبلغت إيران أن إسرائيل "وافقت على ترك الأمر عند هذا الحد" عقب الضربات في لبنان.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79281" target="_blank">📅 15:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79280">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اعلام العدو: الحدث قرب مرتفعات علي الطاهر</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79280" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79279">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
🇱🇧
أبو عبيدة:
نحيّي سواعد مجاهدي حزب الله الذين كبّدوا العدو الصهيوني خسائر فادحة ولا يزالون، في إطار التصدي البطولي للعدوان على لبنان وشعبه وسيادته، وهو حقٌ وواجبٌ كفلته كلّ الشرائع</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79279" target="_blank">📅 15:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79278">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
رسو ناقلتين في ميناء البصرة النفطي حمولتهما تتجاوز مليوني برميل
رسو الناقلة Lucia على الرصيف رقم (1) في ميناء البصرة النفطي لتحميل شحنة تبلغ مليون برميل من النفط الخام كما تم إرساء الناقلة Romania على العوامة الثالثة لتحميل شحنة تبلغ مليوناً و300 ألف برميل من النفط الخام.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79278" target="_blank">📅 15:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79277">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اعلام العدو: حدث امني جديد في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79277" target="_blank">📅 14:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79276">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اعلام العدو:
حدث امني جديد في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79276" target="_blank">📅 14:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79275">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvdEFr_uJbn6EVU0HVP3X9oMKONx8P9WI2ieBMHLQYYKcSjNy3ZHNNqKnnKe_hhPztUiFmzNJ5Q98ojXzrhujAtR8hl8Gxmj-NU-YKgqpQ4BgQ0tHy1UztQB88u__uWW0zF4upFg7R-l-Rzccbmn7GzdMW1OO0oyVAhZIx6exCN4hLh4vg3wLcVZAVyhINe5tDpnY7CoJOlGhbA-1T5fxdZuxZFqpzRvo7Fn_PvScQfA1r4bHMcMXuHcY8gL8DM92v_l-ah9gKlm3NZjE4l-pqJ5Ya5PMcrVaalnOBl-HNwMCtlrCkGz6vxII4C4R8zx-b9gyCe6TMjAjNro76tOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة  يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.  التاريخ: يوم الجمعة 2026/6/19 الوقت: الساعة الخامسة مساءً المكان: بغداد الصالحية -…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79275" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79274">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇱🇧
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة في لبنان - حزب الله:
بِسْمِ اللَّـهِ الرحمن الرَّحِيم
﴿أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَىٰ نَصْرِهِمْ لَقَدِيرٌ﴾‏
صَدَقَ اللهُ العَلِيّ العَظِيم
دحضًا لادّعاءات العدوّ الإسرائيليّ بانتهاك حزب الله لوقف إطلاق النار، تؤكّد المقاومة الإسلاميّة أنّ العدوّ لم يلتزم يومًا بأيّ اتّفاق لوقف إطلاق النار منذ 27-11-2024 مرورًا بـ 16-04-2026 وصولاً إلى مخرجات التفاهم الإيرانيّ الأميريكيّ الأخير الذي أكّد في بنده الأوّل على إنهاء الحرب في جميع الجبهات بما يشمل لبنان.
بل إنّ العدوّ الإسرائيليّ أمعن في خروقاته المتمادية لوقف إطلاق النار مرتكبًا المجازر ومدمّرًا الأبنية السكنيّة والبنى التحتيّة المدنيّة
، واستمر في ممارسة الاعتداءات البرّيّة من خلال محاولات التوغّل والسيطرة على قرى ومناطق لم يتمكّن من الوصول إليها قبل الاتفاق. وبلغ الاستخفاف الإسرائيليّ بوقف إطلاق النار حدًّا صرّح معه رئيس أركان جيش العدوّ، المجرم أيال زامير، قبل أسبوعين بأنّه "لا يوجد وقف إطلاق نار في لبنان"، قبل أن يعاود الناطق باسم جيشه أمس التأكيد على مواصلة نشاط قوّات الاحتلال في جنوب لبنان.
وعلى جري عادته، يلجأ العدوّ، تعويضًا عن عجزه في مواجهة مجاهدي المقاومة، وللتغطية على فشله وخسائره في ميدان القتال، إلى ارتكاب المجازر ضد المدنيّين واستهداف القرى الآمنة، مثلما حصل اليوم في أعقاب تصدّي المجاهدي الباسل لمحاولة تقدّمه باتّجاه تلّة علي الطاهر ليل أمس.
ستبقى المقاومة الإسلاميّة بالمرصاد لأيّ اعتداء، يدافع مجاهدوها بكلّ شجاعة وبروح كربلائيّة حسينيّة عن أرضهم وشعبهم، ويذيقون جيش العدوّ بأسهم، موقعين بين ضبّاطه وجنوده القتلى والجرحى بالعشرات، وفي آليّاته إصابات مدمّرة، وبيننا وبينه الأيّام والليالي والميدان.
﴿وَمَا النَّصْرُ إِلاَّ مِنْ عِندِ اللّهِ الْعَزِيزِ الْحَكِيم﴾‏
الجمعة
19-06-2026
‏
04 محرّم 1448 هـ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79274" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79273">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
سنجعل حزب الله يدفع ثمنا باهظا للغاية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79273" target="_blank">📅 14:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79272">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني:
لن نسمح بإيذاء جنودنا ومواطنينا وأي خرق لوقف إطلاق النار من جانب حزب الله سيقابل برد قوي للغاية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79272" target="_blank">📅 13:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79271">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامب: لولا تدخلي لكانت إسرائيل قد سحقت</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79271" target="_blank">📅 13:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79270">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامب: علاقتي بنتنياهو جيدة ولكن يتعين علينا إبقاؤه متعقلا بعض الشيء</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79270" target="_blank">📅 13:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامب: علاقتي بنتنياهو جيدة ولكن يتعين علينا إبقاؤه متعقلا بعض الشيء</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79269" target="_blank">📅 13:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79268">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGRebmd8DWOSZquAFfh40wvM3djnJhh4qKJH5R_rSzCXMpMij6rd1caedD8-MT1rjWddLEVfUu9sjnKSrq-Oug00O7QKSzunnQSVrsK7SLzHhJ9jA6qez5r_BR1aKf7kcxeoB0Yr7VSA6hrz6Opn6nF5Ac0XujKVaZOZQvqh0rvHjCK-9Psq3bLOftdsxGCemQ1tqttHt3OycOI5oToFr_bn-yrz3X1dsVIOYZmW7-UNhQ-0Vz0GlvhfpxUa4DuUO6G0WP4BSYd0ual1ffq_1epO32dnk5JppnOcZuDEXCvwVO-zNpFIbmW1Afn4IlK2Y1X-Zb1kve1u8EGyrhxJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو يوجه انتقادات لاذعة للرئيس الامريكي دونالد ترامب متهمةً اياه بـ"خداع الإسرائيليين" و"الإضرار بالمصالح الأمريكية والغربية" و"التسبب في إذلال أمريكا" مؤكدة انه كان بإمكانه أن يكون أعظم رئيس على الإطلاق" لكنه "فشل" بدلاً من ذلك.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79268" target="_blank">📅 13:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79267">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
وزارة النقل العراقية:
العراق يتسلم إشعاراً من الاتحاد الدولي للنقل يؤكد تحقيقه تقدماً كبيراً في تطبيق نظام التير
النظام تم تشغيله بشكل كامل وافتتحت 7 مسارات دولية جديدة عبر الأراضي العراقية خلال ثمانية أشهر وشهدت تنفيذ أكثر من (1000) عملية نقل دولي
الإشعار يؤكد أيضاً استمرار اعتماد نظام التير لحركة البضائع العابرة براً عبر الأراضي العراقية</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79267" target="_blank">📅 13:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79266">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌟
🇮🇷
رئيس وزراء باكستان:
الرئيس الإيراني سيزور باكستان</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79266" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79265">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmGbJymaXjmzhIVvPv9-9Xh51so6n-1pYL0cTBFsfw9R0SYDPaElEjbCkCR8j19OQJmYvLxR-Al4eoZEWr5C7uIf5sSsW1ruTdq3Aa9g14Jtpu7CL5CUgPOTIG2Jsfe_pI8BZgWQIGv4ibBSlGEnPUIKOJnfmkR37yYUnfa3ZXLiPeV6pXS8DTUuI5tUS5JP_Quvtegp1SbPsPjjihm3maVdhUPgKWlhk0rh4PnvIQK21CZuOYD-8Yu62Be3PHfZ-7noV_RZQsEvZl1d4WjGOOrOf9ZDq8dnorFP0Un779vflFFX364wPFzE4SE8pvpSYUJgUj4k3eAF1txLYaFtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الغارة الصهيونية على تولين جنوبي لبنان حيث تسببت بشهيدان وعدة جرحى</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79265" target="_blank">📅 13:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79264">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزير الخارجية الباكستاني:
السبب وراء عدم بدء مفاوضات سويسرا  مرتبط بانشغال مسؤولين إيرانيين بطقوس شهر محرم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79264" target="_blank">📅 13:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79263">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42fd214d2.mp4?token=jFGOYIP9QnZ6WabQElDQCcNyM_zCzzy3VYins1MW6lcehmWM4LSWBH6CwpiT6A6a-4teH5M8KyNMKZYc1GCy8yEYln3pYwI97BW54n8ETAS88eEUNy-_hM6CbEm7QdF3368B31oM6bNePQ7SdPfIKUiFFq7BR6A_Rg2CVlw4GEACEJCFiie8VGZabHWrb52ikxDWt8on8BMvJl--MFRws5JTcqOMR6oSnF5BmW0J-0aHrEEJlDbj48KmbZBeZGTcOL6jjkjWsEXJVVDbgoeOPJU_A4nnApWOTYKTZAl_Ea3DRKQs9pqUe8GKsQJTWMOcEQdJg2OxMIfVbjyH1jdu_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42fd214d2.mp4?token=jFGOYIP9QnZ6WabQElDQCcNyM_zCzzy3VYins1MW6lcehmWM4LSWBH6CwpiT6A6a-4teH5M8KyNMKZYc1GCy8yEYln3pYwI97BW54n8ETAS88eEUNy-_hM6CbEm7QdF3368B31oM6bNePQ7SdPfIKUiFFq7BR6A_Rg2CVlw4GEACEJCFiie8VGZabHWrb52ikxDWt8on8BMvJl--MFRws5JTcqOMR6oSnF5BmW0J-0aHrEEJlDbj48KmbZBeZGTcOL6jjkjWsEXJVVDbgoeOPJU_A4nnApWOTYKTZAl_Ea3DRKQs9pqUe8GKsQJTWMOcEQdJg2OxMIfVbjyH1jdu_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مشاهد من الدمار جراء الاستهداف الصهيوني في عين بورضاي بقضاء بعلبك شمال شرقي لبنان</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79263" target="_blank">📅 12:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79262">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9MbGxXE1sXtF9UBTxwjsZU6Q4t0_1KVBkF75zBPnldhhWNmRtGa4jq5GMJsTzlcZiCod7PhGfqTA7pHuUB0ey9d-OqXwOUhFZrkqh13puNDAVmwyAX_aTyPqbkdT-ac-vLG5l8n81W9kD6jrfimDHXJch7DOSwAi_FaUwnDRn_Uk8BvW4o-CBol9LLi_GqaQU4xFPXomZohtEwJ812qyHwPO-kYwIhjlxyQECxmhpFG3danCKlpV7JnKwdixQkQKtbM57oVSul4LcW2rfsa7kmAOR5hGbDRUv9uq2ZEQE5lkPalY6CYJ9l1xXwK0DLe58je2TbnMnGLz-k0nhRHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فايننشال تايمز:
تم تأجيل المحادثات بين إيران والولايات المتحدة في سويسرا بعد أن رفضت طهران إرسال وفد، مشيرة إلى الضربات الجوية الإسرائيلية المستمرة في جنوب لبنان.
وقال ثلاثة أشخاص مطلعين على الأمر إن إيران قررت عدم المشاركة في المحادثات النووية المخطط لها بسبب الهجمات الإسرائيلية المستمرة، مما أدى إلى إلغاء الاجتماع.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79262" target="_blank">📅 12:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79261">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0386d17edd.mp4?token=sbs4Xjz-F4j8p01GYHBSnmM5zQDk6ATKuKAZqOmBrO5NhA0SPSGOleXPpYEvDYOxfgjnr6-FzMdNkB1LpvXh_9qdOHgSAmNhnON94xM19_zVAh7-Y6kbWZ72OG6PnVvZjnG9oXYxkiO2V3lGd2khAW5iTHEK5nUlTDOmjsuMjNvAuNpCRnBGi9_p3WL8Kd_S0BczLyxPCM7LtM_n7JxC1y2pE-SQ2DaQI_dlug03PY0hPMlOa2TsLP6m18oTFxkdMHhzxOEbyWKwdNcFrJHF-yyT3Hu9ujIBRpuYWKRdixN0VkxucRn2NH9ol8GpppCNQiN93z0mZWZ5BWkNgSKhQEE1IzPePIbpD0wnK-UyjNMkbNcJ0jNQJITfojvCOTqQNI-FTm-MX7q7cs7yRcq_sGI9eNwDTKXsUx53Qee_pIaXa9QWwWIZzFy2fZk4XUAZ3g0N7oBYYIQjDOWmJomSy1nzLw-FFiU0mwquI8MjWDQ1DRXTJNL3ZrqaxqcNsuAIIrmp8vhIIKIxPvAuIRmaGj1irat-CdOqf8kVd3wTTaQ9ISFtMhpM-yGb0tcVgUAgjb_dT62H90rFiXE6pd4A5jjhYP9_BgrW7CAZ_PlAruAJ4_2v_WCdse1nuD2K4_xEJ95TM44mUiBb-gZtKqk3LvUq2IbCHOfI-AgVGpoI0U0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0386d17edd.mp4?token=sbs4Xjz-F4j8p01GYHBSnmM5zQDk6ATKuKAZqOmBrO5NhA0SPSGOleXPpYEvDYOxfgjnr6-FzMdNkB1LpvXh_9qdOHgSAmNhnON94xM19_zVAh7-Y6kbWZ72OG6PnVvZjnG9oXYxkiO2V3lGd2khAW5iTHEK5nUlTDOmjsuMjNvAuNpCRnBGi9_p3WL8Kd_S0BczLyxPCM7LtM_n7JxC1y2pE-SQ2DaQI_dlug03PY0hPMlOa2TsLP6m18oTFxkdMHhzxOEbyWKwdNcFrJHF-yyT3Hu9ujIBRpuYWKRdixN0VkxucRn2NH9ol8GpppCNQiN93z0mZWZ5BWkNgSKhQEE1IzPePIbpD0wnK-UyjNMkbNcJ0jNQJITfojvCOTqQNI-FTm-MX7q7cs7yRcq_sGI9eNwDTKXsUx53Qee_pIaXa9QWwWIZzFy2fZk4XUAZ3g0N7oBYYIQjDOWmJomSy1nzLw-FFiU0mwquI8MjWDQ1DRXTJNL3ZrqaxqcNsuAIIrmp8vhIIKIxPvAuIRmaGj1irat-CdOqf8kVd3wTTaQ9ISFtMhpM-yGb0tcVgUAgjb_dT62H90rFiXE6pd4A5jjhYP9_BgrW7CAZ_PlAruAJ4_2v_WCdse1nuD2K4_xEJ95TM44mUiBb-gZtKqk3LvUq2IbCHOfI-AgVGpoI0U0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
سلسلة غارات صهيونية تستهدف بلدة حبوش جنوب لبنان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79261" target="_blank">📅 12:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79260">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">إعلام أمريكي: طلبت إيران ضمانات بأن الأعمال العدائية في لبنان ستنتهي، وفقًا للاتفاق القائم، قبل استئناف المحادثات مع الولايات المتحدة في سويسرا.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79260" target="_blank">📅 12:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79259">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmA2TKg-CafHgTWEQM8qt0FUfnnDnvTo3XrbxgMK-IXSvuIR-8x0cFtBVXgUkeyDNcJK57O97qwBn5OO_yKc4lvpUcnMJXT5I7SUc2Cro_ckF1WeYk4zTyCoe2-ArN7qiDDcizLY7_woZGBTdVsrLZpvG1J_IXqLCaaO_M3M8M4fmGT27_IXJGFteEtvTXp_b4d9F_j2wyQ8VFW7Ol3TKDo1uTjQembUI0_-wj7puxrD1-3OAzdJDbpolvw_GQeufxQ5E6dkOCtobWPwbNMSNaFKQFFQtUR-Y4x5qOUYNe_mEJSuWVdEFN6yepjRmDSr74fDuexR9145nPIg5MU1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش الاحتلال الإسرائيلي يواصل اعتداءاته على المدنيين في الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79259" target="_blank">📅 12:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79258">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4865c13f.mp4?token=n8jYkDA0XHHatWTzqxi9NqRJ4g09hfwgvPGU4hGp2zXRljUQA0BW1EJYswnONn30M7lf3fkZgH-8aEqS1pgqb7b3709vb8xM0V6HiRAQRG-a57KTnMa6F84AUDH_-47WBCRvuPHtpD5f_rbmQ19aDxzmeAHflNVYtb7Qfxh7aaafScSP_q92hX-rgKSVbpAdPBQXCrVu0gQdTv7QxcC7sSnnXRNH4vhu2t_1PZ-GRpuDCmiQGuoCdM0RyWJjrfyi4SKHsNA_ItECnSwfJebAIbWH-_YLy4IZZK3jWdr0F4X48wsgNHCMpXl1uRrhFIBbf4Y234V12II4nDNpZlkmvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4865c13f.mp4?token=n8jYkDA0XHHatWTzqxi9NqRJ4g09hfwgvPGU4hGp2zXRljUQA0BW1EJYswnONn30M7lf3fkZgH-8aEqS1pgqb7b3709vb8xM0V6HiRAQRG-a57KTnMa6F84AUDH_-47WBCRvuPHtpD5f_rbmQ19aDxzmeAHflNVYtb7Qfxh7aaafScSP_q92hX-rgKSVbpAdPBQXCrVu0gQdTv7QxcC7sSnnXRNH4vhu2t_1PZ-GRpuDCmiQGuoCdM0RyWJjrfyi4SKHsNA_ItECnSwfJebAIbWH-_YLy4IZZK3jWdr0F4X48wsgNHCMpXl1uRrhFIBbf4Y234V12II4nDNpZlkmvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇸🇾
وزير الدفاع الإسرائيلي إسرائيل كاتز حول قتال سوريا لحزب الله: نحن نقاتل هناك. لا نحتاج إلى الجولاني. الجولاني، الإرهابي في البدلة، ليس عليه أن يأتي ويساعدنا.  لقد رأينا أساليبه ضد العلويين وما حاول أن يفعله للدروز  نحن نعرف سوريا جيدًا. لن يساعدنا في لبنان.…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79258" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79257">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f858111dd2.mp4?token=s-oMBgGq4nwlkc1vq8Am59H4LLQseHhCet0xjHLy1NI4jRVOfyPmsOjQ2D92duJ3ZLPSaj8h2RPWghrxdiVjauE9ItLRdlno8LyreSMeWAqq7Ss4G8bZ-fqgYmbJGAI0Fe_bE6I2EpkuHRGg9ApHgJ5EkfLm-eTmrWex2D2g53w4h8u711jHV4kSRWeMUzrYu-Sfn7CP6BFBLjaay7RA5oy96jkg5sAKJg7xalKZsHo_yUUOs9fFyFpHd8WBJaICsudsQn6X2eiEDTIjOdk7O0NsKpMvWYAH4X_O_I4OPLVcUv3GfUoGapaCJr1KHh_Z4-n0L5anToovjcsUzWse2rGRf-b-o-YjInLtt4FTjWtZSI_Z3eiITdde__HsV67RDdsXf-IRJfqXM5fzka6Dhzz1AsJlub-x0bfEx6rmlX619EsHHDU7LnE1jT7n1qILKJ6vVlMa0U5bfBQTXRTE5gVEqYk_j7NAmgDVJOGgY52y0GiqWrSlgL2U5h54mlXsq1iLhFS7z7WSdVyjk9EpIuu36ZkbAw2NJI73FaludEnDeQlU3OOYSneWLRJYZAsKza9yRzDrvE-kQdomW8vX7ea18uoKJB1k9bLiynWup2yZUFzs0TpXcO3W_x81GBYVC0mB0mBJIxgp2KPJWVEgHktYw_ATkOWaL7oRRbSp4Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f858111dd2.mp4?token=s-oMBgGq4nwlkc1vq8Am59H4LLQseHhCet0xjHLy1NI4jRVOfyPmsOjQ2D92duJ3ZLPSaj8h2RPWghrxdiVjauE9ItLRdlno8LyreSMeWAqq7Ss4G8bZ-fqgYmbJGAI0Fe_bE6I2EpkuHRGg9ApHgJ5EkfLm-eTmrWex2D2g53w4h8u711jHV4kSRWeMUzrYu-Sfn7CP6BFBLjaay7RA5oy96jkg5sAKJg7xalKZsHo_yUUOs9fFyFpHd8WBJaICsudsQn6X2eiEDTIjOdk7O0NsKpMvWYAH4X_O_I4OPLVcUv3GfUoGapaCJr1KHh_Z4-n0L5anToovjcsUzWse2rGRf-b-o-YjInLtt4FTjWtZSI_Z3eiITdde__HsV67RDdsXf-IRJfqXM5fzka6Dhzz1AsJlub-x0bfEx6rmlX619EsHHDU7LnE1jT7n1qILKJ6vVlMa0U5bfBQTXRTE5gVEqYk_j7NAmgDVJOGgY52y0GiqWrSlgL2U5h54mlXsq1iLhFS7z7WSdVyjk9EpIuu36ZkbAw2NJI73FaludEnDeQlU3OOYSneWLRJYZAsKza9yRzDrvE-kQdomW8vX7ea18uoKJB1k9bLiynWup2yZUFzs0TpXcO3W_x81GBYVC0mB0mBJIxgp2KPJWVEgHktYw_ATkOWaL7oRRbSp4Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇸🇾
وزير الدفاع الإسرائيلي إسرائيل كاتز حول قتال سوريا لحزب الله: نحن نقاتل هناك. لا نحتاج إلى الجولاني. الجولاني، الإرهابي في البدلة، ليس عليه أن يأتي ويساعدنا.
لقد رأينا أساليبه ضد العلويين وما حاول أن يفعله للدروز
نحن نعرف سوريا جيدًا. لن يساعدنا في لبنان. يجب أن يبقى في سوريا، وألا يتدخل معنا، وألا يجعلنا نتدخل معه.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79257" target="_blank">📅 11:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7094431a4b.mp4?token=Y2uyCB-eeaZeLyemNV_7ZXhaCMypiNswbUTIjoGZv9-Arxdo4LrTNa63jHpZcjebCSaJeTT7Bj_iK3nJbiBvxXKWON-RnfMNk8NIrLGE0UEse8rh_pv3jo2-TI19m9WEPeEHeC2QCeWDYw3b8Tb58oUVG-GfNrqOqZqM6Sfpymb98iDIQUjbbnLK21SH3MBtnXZVQQcOh-K9fZO_u-9lVC-vLxe5oPMtDOk4fyZtZRIFjt_O7-ZLFUyeLBWXW1Fd9nnTM-JVVEyXeO6S66gxilRUD4n5ZBqX-TPeNPW_8JSETsgJqIZzvoYSbSIEWmFU-qux8gcrJSKUERoQ_5ppgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7094431a4b.mp4?token=Y2uyCB-eeaZeLyemNV_7ZXhaCMypiNswbUTIjoGZv9-Arxdo4LrTNa63jHpZcjebCSaJeTT7Bj_iK3nJbiBvxXKWON-RnfMNk8NIrLGE0UEse8rh_pv3jo2-TI19m9WEPeEHeC2QCeWDYw3b8Tb58oUVG-GfNrqOqZqM6Sfpymb98iDIQUjbbnLK21SH3MBtnXZVQQcOh-K9fZO_u-9lVC-vLxe5oPMtDOk4fyZtZRIFjt_O7-ZLFUyeLBWXW1Fd9nnTM-JVVEyXeO6S66gxilRUD4n5ZBqX-TPeNPW_8JSETsgJqIZzvoYSbSIEWmFU-qux8gcrJSKUERoQ_5ppgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جيش الاحتلال الإسرائيلي يواصل اعتداءاته على المدنيين في الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79256" target="_blank">📅 11:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8z7A3TTA4qQd3kEWhbVhmPG49_Y8WWfStlibibj5C3kjU4CaSbt9xV3wUWYWEGadV_tCqqzi_Fv_FwiEZRQcyK5ZaLm7SfeiCp0NX1Bd6XBWVhPR3cj4w5aRtKuKaQkFpXvDc1pofx4IcpoQJP45tIBQ92KVXoxpimS-EXf7_GNc0SxbLepFK5Hmad7Jk6CoGd0U20Sbw_H4F9iWD389M4kJH3P5AZwb1UWWNHwQyiOYJXu-cIDP3qwzT04BBz3LCieFEr9C4D-z4hZnLNtcQR7QbPVI_cEl0hLFuzgOfW8EtLD0oRB2rHL_t4tDWnA4n-2OG9CnfIqRcLtxgkmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صواريخ اعتراضية شمال الكيان المحتل جراء رشقة صاروخية من جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79255" target="_blank">📅 11:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5222d6d7.mp4?token=ZYSCTn8MfNROfBEZOYr-tT9UckIX39cGHma6hkV5P-Wl29Jl1Bv0GG63eZrhw9U_EzZZsJ9hUHiQE98fhw8ERpwAV-pV9K2_2vEKd7z0L_byjswWZfxQpsjPRrOV9G20O2sS8D7apkn5gGAk9AStSx9wMvdMd_PibUz3Q7Cp5V9DCTwuWY7Xsc1FlUmxz6tEb7pX04cJigFpoAq41M2uX3UGWZr481qfQe9c0-mR9BNrDRj-qnz7FTZ0f3ZOxkcZFgElp3Kv4v7BFknnGLLbGtTiNk4x0EncAYavws0KQIjntdQSmug31Nof_kanWNS4Ey0YgGtBnOZVqtFtN77q9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5222d6d7.mp4?token=ZYSCTn8MfNROfBEZOYr-tT9UckIX39cGHma6hkV5P-Wl29Jl1Bv0GG63eZrhw9U_EzZZsJ9hUHiQE98fhw8ERpwAV-pV9K2_2vEKd7z0L_byjswWZfxQpsjPRrOV9G20O2sS8D7apkn5gGAk9AStSx9wMvdMd_PibUz3Q7Cp5V9DCTwuWY7Xsc1FlUmxz6tEb7pX04cJigFpoAq41M2uX3UGWZr481qfQe9c0-mR9BNrDRj-qnz7FTZ0f3ZOxkcZFgElp3Kv4v7BFknnGLLbGtTiNk4x0EncAYavws0KQIjntdQSmug31Nof_kanWNS4Ey0YgGtBnOZVqtFtN77q9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇱🇧
جيش الاحتلال يكرر محاولاته للسيطرة على علي الطاهر.. اشتباكات تسمع بوضوح من مسافة صفر بين جنود الاحتلال ومقاومي حزب الله في منطقة علي الطاهر جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79254" target="_blank">📅 10:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79253">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dev8BxiXTJ3QB2E02Ttsl9K-IVFdXUEdaVfFN2rOqZ7-kFbbGfvRNec84WOiMzz3HA7vg5mmtDihugQkafTDYSutoIBk5BO_ofG2JfZNp_GH7l9X3hFs-Q-8r6f7b2_AEQ9ySEu0CYfI8PcyLHEZ4ZpbLdaRl04EefvYVRbJyhbfT24isxlBmrJ6dgT7-iWNy783Ku8mn06RyRXzZXpsFbxmmuk7HvP6c-F2Xi5vdvcLa2bV01NoJEHGdiiVKEcc19O_CHFh-7FxA1fd9vo68HrOII9bd8GOUPdTL0HDc-n27YTputo132iJcEA1FzLNEoJA7jTUfX2nl9CLsHe8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بن غفير يتحدى ترامب ويطالب بحرق لبنان رداً على فشلهم باحتلال مرتفعات علي الطاهر والمجازر الحاصلة بجنود الاحتلال:
مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية. يجب أن يحترق لبنان كله!
‏مع كامل الاحترام للأمريكيين، يجب على إسرائيل أن توضح للعالم أجمع أن دماء أبنائنا وأمن مواطنينا لن تذهب سدى. يجب أن تحترق لبنان بأكملها. واجبنا الأسمى هو حماية مواطني إسرائيل وجنود جيش الدفاع الإسرائيلي، وهذا الواجب يتقدم على أي اعتبار آخر.
‏قلت لرئيس الوزراء، حتى في اجتماعاتنا: مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية دمعة.
‏كفى من هذا التكتيك. في الشرق الأوسط، لا يُحقق النصر بالردود المدروسة والاحتواء، بل يتطلب الأمر حسماً جذرياً. يجب القضاء على الإرهاب.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79253" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79252">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPyIV9u1NUCpU3-lYLjvwsv_I7ouwAS_ijxMuBM8Wywxc4K0DP_Zla41lWtjstLpnYZxaFUfWOMWEOclEZLlcMuRNnKmL17obUNu8wVFTORPr4AWmfvVCiT2Z9AtyqtGIR7519bJ0zkS_-tgk7_4JZCjxUYuPjB48dO-7znw8KONtdOgHiUZc_vlCZ9ZDaHZGT1-5Gsmtl2nqmQ1AB1oXXlS4umEm9745Hja7RLstlbrRcNhR3EhgG8ePiJ7n-1bWx8trsRBfrBoLtygdfitoZFe7gigTEnv69L53xQ7ROmsyC4l-ihMeyroxv2TCFkGF6xefHhm31He8Bt9neia-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بعد فشلهم باحتلال علي الطاهر ؛ رئيس حزب إسرائيل بيتنا يحرض ضد الضاحية الجنوبية لبيروت:
إذا بقيت الضاحية شامخةً بعد الحادثة المأساوية التي سقط فيها أربعة مقاتلين ودُمّرت عائلات، فهذا يُعدّ فشلاً ذريعاً لرئيس الوزراء ووزير الدفاع. جنود الجيش الإسرائيلي ليسوا أهدافاً سهلة في ميدان الرماية. لكلّ أذى يُصيب جنودنا ثمن باهظ لا ينساه الطرف الآخر.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79252" target="_blank">📅 10:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79251">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
🇱🇧
جيش الاحتلال يكرر محاولاته للسيطرة على علي الطاهر.. اشتباكات تسمع بوضوح من مسافة صفر بين جنود الاحتلال ومقاومي حزب الله في منطقة علي الطاهر جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79251" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79250">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c53888f74.mp4?token=RX5-is1HAP-uykFUozXsewvqdv9V5oxKeAfWdgErQRFn4NS_Z4WLdUqYenWn0bRKKzqmfhIB3TpaeyUc55_d2Fq73v6BHmTHA0Z7dEMEpdF1DkBc-YRgoVMrIDn1NxGiet4Ch4h-g-A3NbaSQ8VaIU9feqzHFv33OLkd0ajHijZNmm67IFJiVyxlMHwMBV8X3wE28fiGXiSALGEbVLMzUq60njGh0SDh2F7snN5NQP4PHt4OBCE16QNiXg-Fh6IDuRO_jwRbiQaYEEUxmldTHXQsepcd4wwGJtN7s4OpjlRSuTHja1L2BZlOmSpFLv8-8LtG8yoOYTtR-OpGj27XEQlasveG64lGT3C0_IDpHkGUeaV0jFRrQDesk2xPIg-soR05C8nyPHxxdBDmUG_FV-Ot36xJxZsitrk6LtxsKOT58HD617UMYWA0YpLvY2yQSqd24Fs_7A8uvFaLnxfCRF2FO457nhCP2v_GCKFC8qleqmUTcFLExoy-22JSrjhl_tHLSNmQAfhw2w_3X6hHcZR3XDktNbcx4a0KqrnyOEwHKXFhi-SkQVWKDSbEsbRNASXVBc588e1zsMtwwmVCt21ucbo_o2Q_s_TGXvY1cfYAaIp_L41x0NZxfYo9zhaWRqk0l_4E0EcUuKxD5AfYzZ9r5BIqx4bJQpuSfnXxMBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c53888f74.mp4?token=RX5-is1HAP-uykFUozXsewvqdv9V5oxKeAfWdgErQRFn4NS_Z4WLdUqYenWn0bRKKzqmfhIB3TpaeyUc55_d2Fq73v6BHmTHA0Z7dEMEpdF1DkBc-YRgoVMrIDn1NxGiet4Ch4h-g-A3NbaSQ8VaIU9feqzHFv33OLkd0ajHijZNmm67IFJiVyxlMHwMBV8X3wE28fiGXiSALGEbVLMzUq60njGh0SDh2F7snN5NQP4PHt4OBCE16QNiXg-Fh6IDuRO_jwRbiQaYEEUxmldTHXQsepcd4wwGJtN7s4OpjlRSuTHja1L2BZlOmSpFLv8-8LtG8yoOYTtR-OpGj27XEQlasveG64lGT3C0_IDpHkGUeaV0jFRrQDesk2xPIg-soR05C8nyPHxxdBDmUG_FV-Ot36xJxZsitrk6LtxsKOT58HD617UMYWA0YpLvY2yQSqd24Fs_7A8uvFaLnxfCRF2FO457nhCP2v_GCKFC8qleqmUTcFLExoy-22JSrjhl_tHLSNmQAfhw2w_3X6hHcZR3XDktNbcx4a0KqrnyOEwHKXFhi-SkQVWKDSbEsbRNASXVBc588e1zsMtwwmVCt21ucbo_o2Q_s_TGXvY1cfYAaIp_L41x0NZxfYo9zhaWRqk0l_4E0EcUuKxD5AfYzZ9r5BIqx4bJQpuSfnXxMBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
عدوان صهيوني متواصل منذ ساعات الصباح الأولى يستهدف جنوب لبنان حيث استشهد أكثر من 23 شهيد غالبيتهم من الأطفال والنساء.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79250" target="_blank">📅 10:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79249">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzTr4JalOk7vbKYxHARd3fCuJ7-L4-4oQyssmA2V8fczbMzSWwpXoxl0KNSUGsQHFR8rch5rXs9DbTYSdzREfbzoIycc98Xyr_PPfYeyYkAJeAWz10L504hoC7xq8aFF1VE9gdfdv88P56H0w9XT_INP-lZrK532GLDq_Lh_2Y-HPIhNdJalp107xUBJlgyQ_dENmjbcxBO6NjfLQQx9RaxDGMMfMw6V-hTAGBuNPWMQ8iZPm1FXWCM3cldTmkDfeCC9v1Dr2ZbS-_Xgh0X22X3O9-Z6Pj_iNZMsJQClfvJat3LiyRgUa_Tg9tQtHBri50ZPQ-zUpuhLNK5LCQNASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
الجنوب اللبناني يفتك بجيش الاحتلال ويكبدهم خسائر فادحة خلال ساعات قليلة  جيش العدو سمح بالنشر: إصابة 17 ضابط و جندي إسرائيليين بعضهم قطع أطرافه و2 من الإصابات بجراح ميؤوس منها (موت سريري) بالإضافة لمقتل 5 جنود بينهم قائد كتيبة جراء إصابتهم بصاروخ مضاد…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79249" target="_blank">📅 10:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79248">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📰
نقلاً عن وكالة ‏رويترز : الحرس الثوري شكل خلايا سرية بالعراق لمهاجمة دول الخليج الفارسي
‏رويترز: خلايا الحرس الثوري بالعراق شنت ما لا يقل عن 7 هجمات بالمسيّرات ضد دول المنطقة
خلايا الحرس الثوري العراقية نفذت هجمات في أبريل الماضي ضد ضد الكويت والسعودية والإمارات وأنطلقت من مدينتي البصرة والسماوة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79248" target="_blank">📅 10:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79247">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
الجنوب اللبناني يفتك بجيش الاحتلال ويكبدهم خسائر فادحة خلال ساعات قليلة
جيش العدو سمح بالنشر: إصابة 17 ضابط و جندي إسرائيليين بعضهم قطع أطرافه و2 من الإصابات بجراح ميؤوس منها (موت سريري) بالإضافة لمقتل 5 جنود بينهم قائد كتيبة جراء إصابتهم بصاروخ مضاد للدروع</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79247" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79246">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a5863fe5.mp4?token=M9Ga8a7cgOARydeFewDwXOw8tNkaPD-40pN2QaTADTwz2Y5sO9aPhlYlk3Un33QD8FP237KnAwhHJKR594LjvvWy5sUqabRmUPbuaBr5SMtb7JBUrPHSfcojcCKr54tuU8yByfd5SbnQhWpzumsrd_kI9lnfEVrsHunNKHbFZreyX7-CceLJgY6XZuYVgjWJ5QEyvAD2KD_02gs_hSAummBSqkmhWezRdrq6Jt3YpLo4n61ZCw1jueUJXnMDxhkEEby9EQV70cNm3kj4_nSxxkNZF7S7C3kS3KzF38Uyq832A_3Opb5TBXxjkn-aQfhL3bDvD4YvR44zX_cCwKMcfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a5863fe5.mp4?token=M9Ga8a7cgOARydeFewDwXOw8tNkaPD-40pN2QaTADTwz2Y5sO9aPhlYlk3Un33QD8FP237KnAwhHJKR594LjvvWy5sUqabRmUPbuaBr5SMtb7JBUrPHSfcojcCKr54tuU8yByfd5SbnQhWpzumsrd_kI9lnfEVrsHunNKHbFZreyX7-CceLJgY6XZuYVgjWJ5QEyvAD2KD_02gs_hSAummBSqkmhWezRdrq6Jt3YpLo4n61ZCw1jueUJXnMDxhkEEby9EQV70cNm3kj4_nSxxkNZF7S7C3kS3KzF38Uyq832A_3Opb5TBXxjkn-aQfhL3bDvD4YvR44zX_cCwKMcfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
عدوان صهيوني متواصل منذ ساعات الصباح الأولى يستهدف جنوب لبنان حيث استشهد أكثر من 23 شهيد غالبيتهم من الأطفال والنساء.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79246" target="_blank">📅 09:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79244">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsOK8fe41MBT9EpXh-YAN3BRLvWllm0z29gvEwapeVL2YCg0VrAQTzxKKm62TQAtSxI8Jd6aNLKIveIunIqu72Ego5RfCproHtkhEGArSr4R7D0jxrfG2OU0fE3OR_zmBLCou0jld0LFXKJm2phLMGx7MlWEY2NHM-TzBrA1rEMyTBA7kzbdUEYATocVceTO_pgmXQ2SsvHawdH0Pk4_nDpq7a-QV4GkxhXnssNaaWJVVjBAEN01MnCh-GNuI0gNolgv23Mw-2ulzY1ukEx-WjMQvyYrTqMFULqOTpJqr4cH4oaiq_ZKQsjx_cwGPTctH_5rjvgnH7LgoolfcL0OZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTyT50ZnyX-lfPzEpM7OGm7EcGaj6TCJvdpoCmVRQaFtmnbxySoDuUT2gKGKzEJZjvYP8T_pG6ADAfHmsB8z8DfBcOPB3WGFNelccwyYdftEHbRY37FBaxxh8ie8z2uhE3Rz9XpSttLSjwNAMFtNQ9WklQJZM3Eu7SwM9baIX0zuB6ufqLSsUXh3LYQV6sjZR62c0YbPZIV5yXZa9PCP5YPd0_0OnA72awetLoCh1BSBnwe2rwoy9icyskMdx6BVPSoe8jifGWIvDcdgbTcqdv2DOpmDpr_YUsC0P7NfVU5GqylKba7FQIQcd4w370rTmvA8grMCFN77a3583L4AmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
غارات للطيران الحربي الصهيوني تطال عدة مناطق وبلدات في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79244" target="_blank">📅 06:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79243">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFrz4LGY5e0DyA8nHBlO13SgHl8wxZMLfmAwkf9a9OActwRo1P40SiDEU084A1VffJpOSrPWRaRaKFB9fz72fBhyxTwK_QxFWc8eIKp-yKDKeXPDOtBw2-mo9GUT-Q-awXXc25NvNOuI_NQ3f9tUNMrtuQmEqqzy08GUDQiYxUBrOGhz4p8KwutccvTW_nINYpPjdBWJsZGZDt3gGsAxPnD0TshfkZEMzHAq35zfbA3-4RVqn0vyQPrLX9QGpi57C-U6oK0QGccGShMGCcVLZs3hJgg7p4NWZYF8MyUJOxVYrRawgyWY6kgq1vYqD6vf3wJQ7i9blSLLrPW5Q48OnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة_قائد_الثورة_الإسلاميّة_الموجّهة_إلى_الشعب_الإيراني_بشأن_مذكّرة.pdf</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/79243" target="_blank">📅 05:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79242">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
وزارة النفط العراقية:
- الحقول النفطية جاهزة لاستئناف عمليات الاستخراج
- العودة إلى الوضع الطبيعي ستتم بشكل متزايد حتى بلوغ معدلات الإنتاج السابقة
(سومو) تواصلت مع جميع الزبائن لترشيح الناقلات المؤجرة والمملوكة من قبلهم لتحميل الكميات التعاقدية  من النفط الخام العراقي عبر الموانىء الجنوبية
- ستكون عودة الصادرات بشكل تدريجي استناداً إلى انسيابية مرورها عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79242" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79241">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0819644274.mp4?token=N4c3INwwyHin1nAcQ9hxrBUCxoCaeRPu2KcgK6VeUECt_RhLp-dzRtSY6230wmryTVhS27RDSZddW7vlM3vdScAp_ezk_u1IBLp2SgEa3rc0hs5aWEEsNVXMYEUk2kBWoA6BEkwg9wJju_Ub-8HSZiczPvmjmT0sBkAfm3fr-ffbEok9FL5fN-42TElgplMp1umtJB1epXpUNM8bxhUuBaR6oFPv9PNT_AuzAQWFtR1cKy2sG4HymazjbTXIyND4P-IuaiOfEdvqFas3dFtvWdr_3TPlUZqIKcj1awJSlOKDxiGdhDlZVNPHNljEiZ3Nh4bJ7iaxDDhcFaYi8rH_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0819644274.mp4?token=N4c3INwwyHin1nAcQ9hxrBUCxoCaeRPu2KcgK6VeUECt_RhLp-dzRtSY6230wmryTVhS27RDSZddW7vlM3vdScAp_ezk_u1IBLp2SgEa3rc0hs5aWEEsNVXMYEUk2kBWoA6BEkwg9wJju_Ub-8HSZiczPvmjmT0sBkAfm3fr-ffbEok9FL5fN-42TElgplMp1umtJB1epXpUNM8bxhUuBaR6oFPv9PNT_AuzAQWFtR1cKy2sG4HymazjbTXIyND4P-IuaiOfEdvqFas3dFtvWdr_3TPlUZqIKcj1awJSlOKDxiGdhDlZVNPHNljEiZ3Nh4bJ7iaxDDhcFaYi8rH_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب
:كنت أرغب في منح نفسي وسام الشرف من الكونغرس، لكن قيل لي إن ذلك غير ممكن
😫</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/79241" target="_blank">📅 00:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154f345198.mp4?token=gIVK6ChN6cpQbLrwmgGisWLUTor9EmD9bCyUmRiXHjyiC1DXneSOcgNfTl2Mj1A6MprWAqvEetRBz-HddrfpDGjvMfQ_IMlykwEzOoY7YZW3EVIl1LfuqMUqLGKoGKP2uQ60aw-XK8RkuKvSeqj7tppX_H44aggiQtgSS5ZwgqM11gj7Kl1__pM64Ck2pmY_9nKvQdEru6AMvrrnlFVzrI3sB7MWyYi6FUluGeli21T0PHQ1iyFY0K1QBTUlq9o_eNXABs5Jl_wKW_oike1RSpK2037T1k-51OgujHS5C4FbFLukJt9q4wHqU92TCjsJi1PVfDDdjsbsDuXIFFmGaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154f345198.mp4?token=gIVK6ChN6cpQbLrwmgGisWLUTor9EmD9bCyUmRiXHjyiC1DXneSOcgNfTl2Mj1A6MprWAqvEetRBz-HddrfpDGjvMfQ_IMlykwEzOoY7YZW3EVIl1LfuqMUqLGKoGKP2uQ60aw-XK8RkuKvSeqj7tppX_H44aggiQtgSS5ZwgqM11gj7Kl1__pM64Ck2pmY_9nKvQdEru6AMvrrnlFVzrI3sB7MWyYi6FUluGeli21T0PHQ1iyFY0K1QBTUlq9o_eNXABs5Jl_wKW_oike1RSpK2037T1k-51OgujHS5C4FbFLukJt9q4wHqU92TCjsJi1PVfDDdjsbsDuXIFFmGaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
استنفار أمني واسع في نيويورك لاحتواء الموقف وطمأنة السياح القادمين من مختلف دول العالم.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79240" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79239">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDG24LpPWXj6_F-WRc7OKx4pJYzbaGef04wS2NxlnMmPhiWWLp9ylQcKzLz70B2yV3Z4HvUcCc3MFGAm09lzzaF8EltRPIs1hhdRSFf6nYlJK7W7nDP7cuixAFPUa5PvjUW-tPCkqUvd4a_8BjE_y_gNUt2ik7xzXiw83LTtn067CCCBjxdLGWcOQ6E4M-TdyR6pt4Bh3xMUg29t1gF2VgFyM-B7cJf3i77mAmQ0yfEQBPzcUvgtLpnMcHzvL6Js9G0xxoE6zHSJHSORjj5_9ov681_4IZdsaiXG8ejbMGtF0VXFy-QDhaueFaMYsJifQNYeRdGxUUfgq9F8q9q2oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مشاهد أخرى لفرّ وهروب المدنيين في الشوارع إثر اشتباكات مسلحة عنيفة أثارت حالة من الهلع والخوف بين السكان والزوار</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79239" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8df92df5.mp4?token=VptkQgXuFoSY84FxQiMhxQ8wv3wl5Oh6OhSgz3gvgNZPwwGMSlrxUrN_zCR_1krniViaKB9m5KSd4KIg0UMVf-r63XKcTa4GwpoO8GzaLgQjeD9C_qXQN-tEhgQDK3DvQ3hnznxFZYR8kIpgoE9TvdbvGZ4nQUOKVYXViNFhleWxo2z7EK2W3JerS89iTPTeiNOncSIS6tgCXijWqpXpZ7kLCxyq62EDAfBqBcWS3vjdDrva_LdZZJYTpM-PIgRKi8sWyP_7jPWDjGnaiwkzjy9dKym7xI6IcrjLz0WYijWsZklgl8R5GYY2ZW053TZ9pHx7N-BfKXnwS0BQw28H-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8df92df5.mp4?token=VptkQgXuFoSY84FxQiMhxQ8wv3wl5Oh6OhSgz3gvgNZPwwGMSlrxUrN_zCR_1krniViaKB9m5KSd4KIg0UMVf-r63XKcTa4GwpoO8GzaLgQjeD9C_qXQN-tEhgQDK3DvQ3hnznxFZYR8kIpgoE9TvdbvGZ4nQUOKVYXViNFhleWxo2z7EK2W3JerS89iTPTeiNOncSIS6tgCXijWqpXpZ7kLCxyq62EDAfBqBcWS3vjdDrva_LdZZJYTpM-PIgRKi8sWyP_7jPWDjGnaiwkzjy9dKym7xI6IcrjLz0WYijWsZklgl8R5GYY2ZW053TZ9pHx7N-BfKXnwS0BQw28H-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حالة من الذعر بين السياح القادمين إلى الولايات المتحدة لمتابعة مباريات كأس العالم، عقب اندلاع اشتباكات عنيفة أسفرت عن وقوع عدد من الإصابات والوفيات.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79238" target="_blank">📅 00:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45fd29f.mp4?token=NtW7TuMT6mKdHqfWPbF5EkOMcObPX1XmcVw4wPOf5k7W41qMzpMNkeGTWX4C_QuoK3z2CUVXU9EMc41UHxrAShQy7x7UUsB9_-1YGFzQbpPLGQtQO-M45xf5mf0qksh1OvUYJ6BOA5VO506p_xjVy7aaiNXqmOkblXGj9uWoyOxlNW1-YwJGfAmzA0piZ78wYlPTJxivJ_BQO_hxsQ16gvlqqYvFImGlUI_Oz_uoiqj7NlYZ4aJjmQSJIrSawWC9cSbRvL6QyzT6XKd5ZKMzJe_w5rm_MXPqDCW4S2zrjkEfPtFG8aepi7turQgVyXVTwde9vs2lvs-pufZwgBFr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45fd29f.mp4?token=NtW7TuMT6mKdHqfWPbF5EkOMcObPX1XmcVw4wPOf5k7W41qMzpMNkeGTWX4C_QuoK3z2CUVXU9EMc41UHxrAShQy7x7UUsB9_-1YGFzQbpPLGQtQO-M45xf5mf0qksh1OvUYJ6BOA5VO506p_xjVy7aaiNXqmOkblXGj9uWoyOxlNW1-YwJGfAmzA0piZ78wYlPTJxivJ_BQO_hxsQ16gvlqqYvFImGlUI_Oz_uoiqj7NlYZ4aJjmQSJIrSawWC9cSbRvL6QyzT6XKd5ZKMzJe_w5rm_MXPqDCW4S2zrjkEfPtFG8aepi7turQgVyXVTwde9vs2lvs-pufZwgBFr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إشتباكات مسلحة في منطقة تايمز سكوير بمدينة نيويورك، وسط انتشار أمني واسع في محيط الحادث.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79237" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌟
إشتباكات مسلحة في منطقة تايمز سكوير بمدينة نيويورك، وسط انتشار أمني واسع في محيط الحادث.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79236" target="_blank">📅 00:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79234">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081d58322.mp4?token=t9xtxkG8jT5ayqzTFEXFveBv1ubwIjF2nAgV1nO3GUzmqrG_ds7pTD11lafM8qWKEwYina-aWzFK_W-ELvd1uFTUbbCG0nfCWX8pR_6VLQYSO1KJLgvNCDjatzno3UgIeEq92PlSHJPD6qsr4Wf_hgYaCZ7GG4VJ5h2eIpE4mLJJLbySIe6z_zf6qdT117jHHzUosZVGDrWdejxC5_gx9Fer99GYQywxHz-dctqxbuHI1xF1kGva68-XjW7AiVOR0RhMRdNi0XFAfJld-hCPibHvf8Od7o-TqUUo_RDe7V-pQawisUCdLI5VHxzGtMzhc39M216FG0N3jZ-L9_oglQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081d58322.mp4?token=t9xtxkG8jT5ayqzTFEXFveBv1ubwIjF2nAgV1nO3GUzmqrG_ds7pTD11lafM8qWKEwYina-aWzFK_W-ELvd1uFTUbbCG0nfCWX8pR_6VLQYSO1KJLgvNCDjatzno3UgIeEq92PlSHJPD6qsr4Wf_hgYaCZ7GG4VJ5h2eIpE4mLJJLbySIe6z_zf6qdT117jHHzUosZVGDrWdejxC5_gx9Fer99GYQywxHz-dctqxbuHI1xF1kGva68-XjW7AiVOR0RhMRdNi0XFAfJld-hCPibHvf8Od7o-TqUUo_RDe7V-pQawisUCdLI5VHxzGtMzhc39M216FG0N3jZ-L9_oglQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
قصف صاروخي مجهول يستهدف مواقع لعصابات الجولاني في بلدة الهول بمحافظة الحسكة السورية الملاصقة للعراق</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79234" target="_blank">📅 23:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇫🇷
إعلام الفرنسي:
تشكيلة منتخب فرنسا أمام العراق {فجر الثلاثاء} ستشهد بحد أقصى تغييرين أو ثلاثة في اللاعبين من أجل حسم التأهل للدور المقبل.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79233" target="_blank">📅 22:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سوالف الگهوة
لقاء بعد قليل بين العامري والمالكي لحسم منصب وزير الداخلية … وباقي المقاعد …</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/79232" target="_blank">📅 22:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇫🇷
‏
ماكرون
: الكثير من علامات الاستفهام بشأن الاتفاق..  ولا أعتقد أن الحرب انتهت</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/79231" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79230">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3RdtvbqcmqYyl-w5oVwuDE-NH33O1-eSn4WS6EO_B7VOPAmS7KG3C2PcYDcSs8sv6HqXbdP7c7a7cKD7b_bUfb9K-yIVdj1mi5QRpqAdH2oNtcHk7jQ47Yte5coCP75WdiqHrnkriPGYKrJZNAnupGagkIU567IuRjYVkG8Wb-n54-B9yD_OYg_FaM-8xIOWomCTM_iAkepwG_smkdz4aoTTyceWsPcfqPqDN_5WaGY5fzSzaNnrbZhFlBVVfE6lAiP2AVLvUgQJHAHfPyej0tZ3Cz4PFo8kyNz8Uo0rq9Zp9vvsWbtT69GHkYQ4Lw-dfoqfpxZdbnpRbtiT481wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تلتزم الولايات المتحدة بالسلام، ونشجع الجميع في منطقة الشرق الأوسط على الحفاظ على التزامهم بالسماح لمفاوضاتنا بالتطور بشكل جيد. الأسواق سعيدة بما يحدث مع انخفاض أسعار النفط بشكل كبير، وارتفاع الأسهم بشكل كبير. نتوقع وقفًا كاملاً لإطلاق النار على جميع الجبهات، بما في ذلك لبنان وحزب الله وإسرائيل. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79230" target="_blank">📅 21:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79229">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19519b7ddd.mp4?token=hhxSMtRgtL2tDk4hY6DpvxUMX-lENXnnVnbzZuYbJTdLsZrpPmNJTUMKUlfnH27kIhisMNbxSLjFunYQdi2mh1a8aNwlHq1GCjbUihIiDMHEe28DiJus4zZFwn4O4oM19yXP9dtJF6CF5jCWk4D60BTQPrrF_ofuXYRh9XwARQwbix35e2dM9S18ksy-mb51-wb_-e2MQFJXn0RTVXTv_NORLKXUs08KMxPOm-DkNVzSClkzi6UZNLi-nDEosh2LtTDvM-nR7l-6wbfzpvQ2JYUFHmIuLQIoOxzak29SXgvYC0UKj2cLEDaiqlqCWeCScIztRCl3KFKUOiLd4cy5qYRNsGD9D858w27jgRN2qpTFGqxJyN5rvpywj8Ppr-T35A_IYdftyidgSuUVJ718SI3sR0x7doB9jEWY1p1CMBB-7Lx3OX_fIKZWwSnGKlJ4NaT0QdX51OBeEt8tmjqHgGPHZpiaZfRHGlgVEK572VvN_v2PUwsoOPrM31Mpts-2l2rOTFvjKW9fJMMBgG1oQEjNC4cNBagGzypMqS3yi7FndVFBCZOACZN-HT4g_EPReBZQ_DDvdbfFVyTZd7vH3tFWklLKvlbVpJSNm6VSl_lnV0Kekx9Ki5X4IxFn41o2Fi_DiFD9I4UBfxEqU0GZ6HxskCXYljUyb81YOF7f7XY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19519b7ddd.mp4?token=hhxSMtRgtL2tDk4hY6DpvxUMX-lENXnnVnbzZuYbJTdLsZrpPmNJTUMKUlfnH27kIhisMNbxSLjFunYQdi2mh1a8aNwlHq1GCjbUihIiDMHEe28DiJus4zZFwn4O4oM19yXP9dtJF6CF5jCWk4D60BTQPrrF_ofuXYRh9XwARQwbix35e2dM9S18ksy-mb51-wb_-e2MQFJXn0RTVXTv_NORLKXUs08KMxPOm-DkNVzSClkzi6UZNLi-nDEosh2LtTDvM-nR7l-6wbfzpvQ2JYUFHmIuLQIoOxzak29SXgvYC0UKj2cLEDaiqlqCWeCScIztRCl3KFKUOiLd4cy5qYRNsGD9D858w27jgRN2qpTFGqxJyN5rvpywj8Ppr-T35A_IYdftyidgSuUVJ718SI3sR0x7doB9jEWY1p1CMBB-7Lx3OX_fIKZWwSnGKlJ4NaT0QdX51OBeEt8tmjqHgGPHZpiaZfRHGlgVEK572VvN_v2PUwsoOPrM31Mpts-2l2rOTFvjKW9fJMMBgG1oQEjNC4cNBagGzypMqS3yi7FndVFBCZOACZN-HT4g_EPReBZQ_DDvdbfFVyTZd7vH3tFWklLKvlbVpJSNm6VSl_lnV0Kekx9Ki5X4IxFn41o2Fi_DiFD9I4UBfxEqU0GZ6HxskCXYljUyb81YOF7f7XY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 ناقلة جند تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79229" target="_blank">📅 21:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79228">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">رسالة_قائد_الثورة_الإسلاميّة_الموجّهة_إلى_الشعب_الإيراني_بشأن_مذكّرة.pdf</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/naya_foriraq/79228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رسالة قائد الثورة الإسلاميّة الموجّهة إلى الشعب الإيراني بشأن مذكّرة التفاهم بين رئيسي جمهورية إيران الإسلامية وأمريكا
بسم الله الرحمن الرحيم
أيّها الشعب الإيراني الغيور والوفي،
💬
كما علمتم، فقد جرى توقيع مذكّرة تفاهم بين رئيسي إيران وأمريكا. وفي مسار الوصول إلى هذه المرحلة، بذل المسؤولون المعنيون جهوداً حثيثة دافعُها الحرص وحسن النية، وإن كان الرئيس الأمريكي هو من لجأ إلى شتى أنواع أوراق الضغط، انطلاقاً من حالة العجز لإنجاز هذا الأمر.
💬
كان لي رأيٌ آخرُ بطبيعة الحال، غير أنني أصدرتُ الإذن بذلك من منطلق الالتزام الذي قطعه رئيس الجمهورية الموقّر بوصفه رئيساً للمجلس الأعلى للأمن القومي، نيابةً عن نفسه وسائر الأعضاء، بصون حقوق الشعب الإيراني وجبهة المقاومة، وإعلانه الصريح تحمُّل المسؤولية، حسبما صرّح جنابه، بأنهم لن يرضخوا للطرف الأمريكي إذا ما أراد فرض إملاءات توسُّعية أو المطالبة بالمزيد. ومن هذه اللحظة، سنكون نحن - أي أنتم، أيها الشعب الشامخ، وهذا الخادم الصغير - بانتظار تحقق الشروط المذكورة، بيد أنه من البديهي أن المفاوضات المباشرة التي ستنعقد في المستقبل، لن تعني بحالٍ من الأحوال الإذعان لرأي العدوّ. كلّنا أمل في أن تحفّ دعوات مولانا (عجّل الله تعالى فرجه الشريف) شعب إيران الأبيّ بشتى صنوف النصر والفتوحات.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79228" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79227">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
المركزية الأمريكية: رفعت القوات الأمريكية اليوم الحصار المفروض على جميع الملاحة البحرية الداخلة إلى الموانئ والمناطق الساحلية الإيرانية والخارجة منه
🇺🇸
الخزانة الأمريكية: ‏عقوبات أميركية على 3 أفراد و5 كيانات مرتبطة بحزب الله من عدة جنسيات "سوريا عمان العراق لبنان" وأحد الشخصيات سليمان فرنجية ومحمود قماطي.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/79227" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79226">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
‏الخارجية الإيرانية: تخفيف المواد المخصبة مطروح الآن كخيار لكي نغلق الطريق أمام الخيارات الأخرى نقل المواد النووية المخصبة إلى خارج البلاد خيار غير مقبول لنا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79226" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79225">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📰
رويترز: البيت الأبيض قدم نص مذكرة التفاهم بين الولايات المتحدة وإيران للكونغرس</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79225" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79224">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مصادر إعلامية: معلومات عن وصول أعضاء من الوفد الاميركي الى مقر المفاوضات في منتجع بورغنشتوك بسويسرا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79224" target="_blank">📅 19:42 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
