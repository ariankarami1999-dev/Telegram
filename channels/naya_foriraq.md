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
<img src="https://cdn4.telesco.pe/file/AEtT6i2ibv15nY7YHNL6PJh8l4bOzoqNPlS510C03Hb2pKJ4WsTkbwGEO3o5E8KbzZ90NQKuHnxlxZZUS4cohKGoHhD8JXa1JyF9sRT8rXkMaA07KH8rlyHDmzC-MpVqA5i7BRmwYyTzRBYH9sUyzWpqPqCrvz5XUqzP_LxYRqoAF08CXHBYyQwnWo1Uz-7JtwoZxVeFLOZnSCYGUqzZ9SivXBF_4VBb_iDr6F8P3gL5c5gdh0SGJt0L32rb_t_8Unignp7Vr2ixmjW5Fyaoz1T0PgPD4h_satXK7jArkZ4hJUKcPiSsbckBBWqAQcK3CRouOi_dqHK1z0TGs9bouw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 260K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صافرات الإنذار تدوي في غلاف غزة</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/naya_foriraq/78681" target="_blank">📅 13:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78680">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزارة الخارجية اللبنانية:
تقدمنا بشكوى إلى مجلس الأمن ضد إسرائيل لاستهدافها آلية عسكرية للجيش واستشهاد عسكريين ولرشها مبيدات الغليفوسات فوق قرى جنوبية حدودية.
تقدمنا بشكوى وسنواصل التفاوض المباشر معهم
😄</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/naya_foriraq/78680" target="_blank">📅 13:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78679">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
مهدي محمدي، المستشار الاستراتيجي لرئيس فريق التفاوض يكشف عن تفاصيل مذكرة التفاهم الإيرانية الأمريكية
- في الخطوة الأولى، يتضمن جدول الأعمال وقفًا تامًا للعمليات العسكرية ضد إيران ولبنان، ومنع أي عمل عسكري جديد. كما يتعين على الجانب الأمريكي تقديم الضمانات اللازمة لمنع تجدد التوترات
- بناءً على الإطار الذي نوقش، سيتم الإفراج عن جزء من الأصول الإيرانية المجمدة مع بداية تنفيذ الاتفاق، وفي الوقت نفسه، ستبدأ عملية تعليق بعض القيود والعقوبات الاقتصادية للسماح بزيادة التبادلات الاقتصادية ومبيعات النفط.
- يُعدّ تسهيل حركة السفن التجارية الإيرانية وتخفيف القيود البحرية أحد المحاور الرئيسية للاتفاق. ويهدف هذا البند إلى إعادة التجارة البحرية الإيرانية إلى وضعها الطبيعي وإزالة العقبات أمام النقل الدولي.
- لا تتضمن المرحلة الأولى من الاتفاق، في النص قيد التفاوض، القضايا النووية. ووفقًا لهذا الإطار، يجب أولًا تنفيذ الالتزامات الأولية للطرف الآخر والتحقق منها، ثم تنتقل المحادثات بشأن القضايا النووية إلى المراحل التالية.
- في المرحلة النهائية، تمّ النظر في رفع العقوبات الأمريكية الأولية والثانوية، فضلًا عن توفير آليات للتعويض عن الأضرار الناجمة عن الحرب والضغوط الاقتصادية وإعادة إعمارها. ويُعتبر هذا البند من أهم مطالب إيران في عملية التفاوض.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/naya_foriraq/78679" target="_blank">📅 13:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78678">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60e8157bf.mp4?token=oMnvqfcdNoKI9sbEofijDr68vCmDrHGgD_LwkD0knhPqa_mUgHzycErkEEDEK-zEi8XRWlwMOlM6dCn4G3zsmIVUe1hlnQeo1m8F8CKuphDttz0E7ni2SNq2Apu7FI50zKLWsBukJafuQRLB9MF1Q9IiOg9lQyRBN5BFvlVCc8QxrMq40Vf5JM5yUjH6oMzT41AqyhdBJkITOTOmOErhx62w-w6qvtjFikcFD3T3oeoPf3HIN1X0I7b5j74NbPZ4UH5STWBtwhiQCXNLk27qA-8GV1NoZlcsfKTQIllt-5t-JGcQOAr7qO0kCKEWkmrmIoNCyfRZBXhUgEetOMrxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60e8157bf.mp4?token=oMnvqfcdNoKI9sbEofijDr68vCmDrHGgD_LwkD0knhPqa_mUgHzycErkEEDEK-zEi8XRWlwMOlM6dCn4G3zsmIVUe1hlnQeo1m8F8CKuphDttz0E7ni2SNq2Apu7FI50zKLWsBukJafuQRLB9MF1Q9IiOg9lQyRBN5BFvlVCc8QxrMq40Vf5JM5yUjH6oMzT41AqyhdBJkITOTOmOErhx62w-w6qvtjFikcFD3T3oeoPf3HIN1X0I7b5j74NbPZ4UH5STWBtwhiQCXNLk27qA-8GV1NoZlcsfKTQIllt-5t-JGcQOAr7qO0kCKEWkmrmIoNCyfRZBXhUgEetOMrxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
وزارة الدفاع البريطانية:
هذا الصباح صعدت القوات البريطانية على متن ناقلة نفط روسية في القناة الإنجليزية كانت تساعد سرًا في تمويل حرب بوتين في أوكرانيا.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/naya_foriraq/78678" target="_blank">📅 13:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 08-06-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة الناقورة جنوبيّ لبنان بمسيّرات انقضاضيّة.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/naya_foriraq/78677" target="_blank">📅 13:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78676">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏴‍☠️
‏مسؤول صهيوني: لانتوقع نجاح المفاوضات لكن لا نتوقع عودة الحرب
طلبنا من واشنطن عدم تقييد عملنا العسكري في لبنان</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/naya_foriraq/78676" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78675">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">إعلام العدو: للمرة الثالثة هذا الصباح مسيرة إصابة هدف عسكري شمال البلاد خط المواجهة</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/78675" target="_blank">📅 12:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📰
وكالة فارس عن مصدر مقرب من فريق التفاوض: قرار طهران النهائي بشأن مذكرة التفاهم لا زال قيد المراجعة القانونية والسياسية والتقنية
إيران لم تعلن بعد قرارها النهائي بشأن مذكرة التفاهم المقترحة</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/78674" target="_blank">📅 12:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
تسلل طيران مسير من جنوب لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/78673" target="_blank">📅 12:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴‍☠️
تسلل طيران مسير من جنوب لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/78672" target="_blank">📅 12:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🤺
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية موقع بلاط المستحدث التابع لجيش العدو الإسرائيلي جنوبيّ لبنان بصاروخٍ نوعي.</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/78671" target="_blank">📅 11:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
🇸🇾
عملية أمنية لوزارة الداخلية العراقية في الأراضي السورية أسفرت عن إلقاء القبض على 9 تجار مخدرات وضبط 200 كيلو من المخدرات كانت معدة لتهريبها نحو العراق.</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/78670" target="_blank">📅 10:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📰
وكالة "تسنيم" الإيرانية: وفد قطري يزور مجدداً طهران للاطلاع على المستجدات المتعلقة بالعملية الدبلوماسية لإنهاء الحرب وعقد مشاورات مع المسؤولين</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/78669" target="_blank">📅 10:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce906e638.mp4?token=Lw8ALdXmWIWY7vXGp1VvUV8NEg4evbaxcb2v5ETS9L4_FJUQNH52kzSyk7ZpxmSoRc1QFfE6WpIgc0peW_57tpQZhQkTSAs8CV-S62Peqd2XLhpYW0OpFHPcYbzAMF-ZhMF3Z2uD1i7YZl1uJITVQur4MguG9lsI7Zu3G8TrwK-GwbI3QEHh5CGyEWvo1S83M8qYRk583Or3fP577tpUNkGCWJVROH2xoZQWNQRZPy31U13sFhOzm8pzs5g38H_ZXnxjWiu4CdARiGdV1L-Roa90W0DrOpkkIvUH1_21PANLF3BNFumKi0ZCURVtoO_EvPWsiwQC89muYowVi3jNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce906e638.mp4?token=Lw8ALdXmWIWY7vXGp1VvUV8NEg4evbaxcb2v5ETS9L4_FJUQNH52kzSyk7ZpxmSoRc1QFfE6WpIgc0peW_57tpQZhQkTSAs8CV-S62Peqd2XLhpYW0OpFHPcYbzAMF-ZhMF3Z2uD1i7YZl1uJITVQur4MguG9lsI7Zu3G8TrwK-GwbI3QEHh5CGyEWvo1S83M8qYRk583Or3fP577tpUNkGCWJVROH2xoZQWNQRZPy31U13sFhOzm8pzs5g38H_ZXnxjWiu4CdARiGdV1L-Roa90W0DrOpkkIvUH1_21PANLF3BNFumKi0ZCURVtoO_EvPWsiwQC89muYowVi3jNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد مباشرة لحركة السفن في مضيق هرمز الذي يقع تحت سيطرة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/78668" target="_blank">📅 10:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">إعلام خليجي: اجتماع افتراضي لوفدي أميركا وإيران بحضور الوسطاء من باكستان وقطر
الاجتماع الافتراضي سيشهد التوقيع على مذكرة التفاهم بحضور فانس وقاليباف</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/78667" target="_blank">📅 10:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇬🇧
🔥
وزارة الدفاع البريطانية: قوات بريطانية تداهم ناقلة نفط تابعة للأسطول المظلل في القناة صباح اليوم.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78666" target="_blank">📅 09:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzjnU19cVF5bY8sYuOeGK8e2T-4mYCW_Gl4rFUAkqtg_SXs6wWzC0eSW5G6WJPTUquhGFzfoyJFnhTRANSS_o8NohyIq_f1ZkHfbBdW5J0bg2GVmqIubQQa3QzOQe79GNvCE-bB3wNFqJe8vnKIXGDb8uNuupMNfRZZ3qAJbx--326ujQHRojcIMEbVBNVosF3FTSsE8x7gs02C-0Lvt2NV5vvgWAPhYa5n1VJj3e3O3xY7bEwcQDjnFLtfvmhqOwbuCV5SM9RAYYeDgcsWoUhK_4vzIftQai9zrHXWaiXvI9z8ssuuRxCRLt2Z7e6bOn90NRHR7Tno5upgQcMj6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو: بشكل أولي السقوط في شلومي داخل مهبط طيران وقاعدة مستحدثة واشتعال النيران.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/78665" target="_blank">📅 09:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: انتهاك واضح لوقف إطلاق النار.. انفجرت طائرتان مسيرتان في "الأراضي الإسرائيلية".</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/78664" target="_blank">📅 09:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b72a1bd7.mp4?token=rALEZw1hz6lWC3bNOvU_V7tR3lIY6vtEHj6PQzyZxRJW8lIG-Xqoozf0HsxjMG13JOJnA40ELSppzZZFfpuOPSVHvOcW4NbKlXjfRSY17VrhFpTs4S0Nk-7P9PAxeDTP5BrEOvv4C9op8FvXZ-TQKxZql3Hyp2jyjNx6HKu21nf67bAXVmZLGUa044IIcqutGvPKyIuhFi1Tj1w5XkTNpfQLPaUuDULDa-Rm-PEqdIVwLZDdQxbXLgRJQCvc1UB_XnrOV3spKF-j1rC7YLxKkqIJuw_8_jCE73aM1fXqJl3982BTqq0eaHyl6PGAvH35S7t7vwitWqVzZj2VR2OMxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b72a1bd7.mp4?token=rALEZw1hz6lWC3bNOvU_V7tR3lIY6vtEHj6PQzyZxRJW8lIG-Xqoozf0HsxjMG13JOJnA40ELSppzZZFfpuOPSVHvOcW4NbKlXjfRSY17VrhFpTs4S0Nk-7P9PAxeDTP5BrEOvv4C9op8FvXZ-TQKxZql3Hyp2jyjNx6HKu21nf67bAXVmZLGUa044IIcqutGvPKyIuhFi1Tj1w5XkTNpfQLPaUuDULDa-Rm-PEqdIVwLZDdQxbXLgRJQCvc1UB_XnrOV3spKF-j1rC7YLxKkqIJuw_8_jCE73aM1fXqJl3982BTqq0eaHyl6PGAvH35S7t7vwitWqVzZj2VR2OMxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
تسلل طيران مسير من جنوب لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/78663" target="_blank">📅 08:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78662">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
🏴‍☠️
🇺🇸
إعلام العدو: إيران هي المنتصرة الكبرى بلا منازع والولايات المتحدة و"إسرائيل" تجران أذيال الخيبة والهزيمة</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78662" target="_blank">📅 08:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78661">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🏴‍☠️
تسلل طيران مسير من جنوب لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/78661" target="_blank">📅 08:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚠️
🇮🇶
سقوط طائرة مسيرة مجهولة العائدية على منزل مواطن بحي الإعلام غرب العاصمة بغداد .</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78660" target="_blank">📅 03:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚠️
🇮🇶
اشتباكات عنيفة في أطراف ناحية البشير جنوب محافظة كركوك العراقية بين عصابات داعش وقوات جهاز مكافحة الارهاب ..</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78659" target="_blank">📅 03:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgXcQ8sUvpLcL626aUMP5hRTqfsZ_WzIBi8pE2Cj1I55G8gXZyp3moKC5NePDmEH1wkKBMpo_956CQY_1SuW8-aJYmvAuhLyUfx2G2b_7Se24dF_bjIXc4bPOTMKCbZ3cG6iCcGkqEedipRHYxF807cjOlKgq0JOmogO9oI3aE8R3pjapC5VkZETe6h56x9UvOHJ9vVmuX2ci_6lFToQgJMR-X6B5s47-Dm-3m3XS75oPWRKD3m6-ClzS2Smb4-0D43ZAzd-WIj_rO7Tv5xTvm9qio-vgWKtfnUU17Zd5W3IVqTU3Ebhm60CEQjzwQN9yRvcywWSOzXclZE6jN4m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في الوقت الذي لا يملك فيه المواطن الكوردي مسكناً يؤويه، يمتلك حكامه عقارات في واشنطن.
دولة جورجيا مستأجرين مبنى في العاصمة الأمريكية واشنطن لتكون سفارتهم في أمريكا
وبحسب احد الوكالات الكوردية مبنى السفارة هي ملك ل منصور مسعود بارزاني.. ومنصور أهدى المبنى بشكل تطوعي سنه كامله مجاناً للسفارة.
عائلة البارزاني الحاكمة في إقليم كوردستان العراق تحاول بشتى الطرق تحسين صورتها وبناء علاقات دوليه لمصالحهم الشخصية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/78658" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxbJbmolZDznao-g1UzLo7gZ0XVcdpDG5hhMH0VMjZeu1xb5QpQV85ehik3XtQRtS63vQVijKiI9rzWjG-127jDuM86TncHXZSjC8Sc8gEwoC71QBj-ASfhN8YyLkitY21mDtuUqJXsKzLOJRAxhnXxRrjjPCgWy7admKE55K6aoFtSS3xvRfIx4YmpbdPsMPA4ykyrSlZ7wltSMr1DW9IHPMH11_9jiDbntnwalMzb57hqByslHZG0F9Z7nQl1KDSi1Bai3dutxmUpew5942fcjG-XlXTuPZGkyu6EN0QeLNclpnXBArLNaclFOOoE3tJTKcZc0GH3IXE82-dSvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الاتصالات مصطفى سند
: قرارات جريئة خلال أسبوعين شملت إلغاء مشروع السكك، وإلغاء مشروع تطوير مطار بغداد، وسحب يد مدير الموانئ وإحالته إلى التقاعد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/78657" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2214529b91.mp4?token=uZvolXBWu6nl2f-3JRC7Hp1uLVv1qO6poGBLImlzmvSL8VHq6O5hD465HwoVIRZjL3pDRblmnhvTJkH9V3EsZ41wos93UaRYOZ1qR9IoeFbw08l4gfLP1DZQ6Q-JiYzJUQFlDIgD2zfXyPiZhZDfuX8nlIlB5pIr5LD5TQuaSWwGa5iRDDbz4s7tFLpfKKB8wO8VN-RVzLgx0vSniZ_d28_MlB6xWibK-sp2jnNWYmxpLpctLdy8orWKOydAjP7DOzKZez5bmiN3mFjyG_ouqaojbYregfsmWa0u1ZYxyrDT_K2Z7qXAGzWzzQF9th-O2-IYvMXJH57eJ2fzlX7VKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2214529b91.mp4?token=uZvolXBWu6nl2f-3JRC7Hp1uLVv1qO6poGBLImlzmvSL8VHq6O5hD465HwoVIRZjL3pDRblmnhvTJkH9V3EsZ41wos93UaRYOZ1qR9IoeFbw08l4gfLP1DZQ6Q-JiYzJUQFlDIgD2zfXyPiZhZDfuX8nlIlB5pIr5LD5TQuaSWwGa5iRDDbz4s7tFLpfKKB8wO8VN-RVzLgx0vSniZ_d28_MlB6xWibK-sp2jnNWYmxpLpctLdy8orWKOydAjP7DOzKZez5bmiN3mFjyG_ouqaojbYregfsmWa0u1ZYxyrDT_K2Z7qXAGzWzzQF9th-O2-IYvMXJH57eJ2fzlX7VKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
من مستوطنة المطلة قبل قليل اثناء رشقها بصواريخ حزب الله وتفعيل الدفاعات الجوية للعدو.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/78656" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سماع دوي انفجارات في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/78655" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سماع دوي انفجارات في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/78654" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOXp5FswvOYVjvVtgKyYfsR0nTGVHuEl-toDkuz_wGakBtGbFnuPjQcV2RnwvzheAsLRZ1L71-Dw1hlQa_Bj6hioeKuW53zTv9bGSM6wE5eVTwFjXMWuMI_uJbypdAlLLFldsi7VfmigIJ1pnkFYJ9kG_PrdVPPBNq9WVAAq71q9Rky7j3nSruxOaA7CMt_2tiBIJ8IccJa1Zq4mA4Ci7J9I7b6WiO_KQ8SjYq-_BnSEd1BDYk17F8eypJyyzyzlbJwn-YX-eVa17MLe2TWyYFk1YP9bKA0C6w9P3fpnLrjkbILnzBLPfoNH7wWu0NQcZMhS0u-ExwMrM8bSAg8ang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير الاتصالات يعلن عن توفير ٥ شاشات عملاقة لبث مباريات المنتخب الوطني العراقي في كاس العالم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78653" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
وزارة الخارجية العراقية تنفي المزاعم بشأن تورط دبلوماسيين أو أفراد من عائلاتهم في قضية الدفاتر الامتحانية التي ضُبطت أثناء محاولة تهريبها عبر مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78652" target="_blank">📅 23:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaa1f4ac3.mp4?token=QBfhNMgqIvex3OszRSgeJJPaqtyZ-_xOpsSO3Q8TcDeDmP86Ynfv-G5TKS_xm_SOnor07slcMt2iiAzq4yy9hhQh0K90HMAQY64SG_5G1Cvj16kiuWJntTmqiZljpZJ_Oz9NWLkJHBFA4iEtEfHyNiTf1NSdsIayFHGXJaN5pwliou89qPEH_tJX5Rzr41KHbQGy6Q9goRYE-fW6GSUZViXx4f6BeCPg33vn0lw13JP1et0vOZJyZfcBzpEIG2u-AB10KBS3HXg8BN_rS8pyNGtkgLCYU3brDvfYndmgVt8VkEeJrsXyjqdM969E89G1zuC6xNLaw60xd0e76b4glnDiOGUjhu-E5GkY0eCg2Bpnn3vpY-As77Rr3DrKv4qfi0WyRbnueM_y5_zH4KU2A10AirwQiiPV-7Adm6XA5yge0peamL5nGttKM0CInB60LnOY6Ey6z5Qg-6NBc8ajVGPIL2u6Ju59wWYK3WFPwPMUrPC1tS3KfTzkA5v1OoYfaUZMxXm_BiS1VZMyKP7JpanC8eiEqOzdpJ9zovgaDJdkQLt5t6ZF7iQjbnpLVPm9lR0p7jvhSn48FoMtO0lI4eUzJf0ICCKtMCUyPOArR1P2QcMO49-B3e3zhhZVdchwygmfCJerBpQHTiHfxUDHUWzqmiS9VFG_UClOGHmOT6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaa1f4ac3.mp4?token=QBfhNMgqIvex3OszRSgeJJPaqtyZ-_xOpsSO3Q8TcDeDmP86Ynfv-G5TKS_xm_SOnor07slcMt2iiAzq4yy9hhQh0K90HMAQY64SG_5G1Cvj16kiuWJntTmqiZljpZJ_Oz9NWLkJHBFA4iEtEfHyNiTf1NSdsIayFHGXJaN5pwliou89qPEH_tJX5Rzr41KHbQGy6Q9goRYE-fW6GSUZViXx4f6BeCPg33vn0lw13JP1et0vOZJyZfcBzpEIG2u-AB10KBS3HXg8BN_rS8pyNGtkgLCYU3brDvfYndmgVt8VkEeJrsXyjqdM969E89G1zuC6xNLaw60xd0e76b4glnDiOGUjhu-E5GkY0eCg2Bpnn3vpY-As77Rr3DrKv4qfi0WyRbnueM_y5_zH4KU2A10AirwQiiPV-7Adm6XA5yge0peamL5nGttKM0CInB60LnOY6Ey6z5Qg-6NBc8ajVGPIL2u6Ju59wWYK3WFPwPMUrPC1tS3KfTzkA5v1OoYfaUZMxXm_BiS1VZMyKP7JpanC8eiEqOzdpJ9zovgaDJdkQLt5t6ZF7iQjbnpLVPm9lR0p7jvhSn48FoMtO0lI4eUzJf0ICCKtMCUyPOArR1P2QcMO49-B3e3zhhZVdchwygmfCJerBpQHTiHfxUDHUWzqmiS9VFG_UClOGHmOT6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف تجمع لجنود وآليات جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78651" target="_blank">📅 23:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfi5CDJCQT0GCtwEZGrkVX_YEX8JMlE2sLzmBwxmyeMjJBQEqOUcATA3lZ13k-Y3HjPGvQAHfrRipghdv0SCASmRzZwKAmq5iZFR9ndtbMZ6zb1hphHImUuWoBn-bWNPM8HBfuKXwgWyuK4YdyMYxTqWVDD4Kjyz4JbFVUEC2wyZLi9HedeHafSABpNUkCMMEmP2sXdQAuTlXMiB9OVCCxEZMu7-yQG6PP_7ItTbbY1VCBqN_NeEbC_YfqZuLxp7og-p1U5IcXbGQV1TMgOm5-WUpAMQJO8mxfGjJGE6MBq-KzTN80zzyiAV1xKhue17eKYyur4rHDcFzlq1u_y97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZFHYjfA6u8_OkbSz0v3_R7xp4QQPaG2Q8psPgF-h-X1gghNuU3E6DAVGzWpIFvvKkjffcN1UWutEKQvZs2DShCdxCp2vb7YCNLY1xGYWF3VMcD0aeT_8MSe1eHPpAg1X5eWCzGrjn9CItKpKE8WE4NpAc7QZizEskgC-EbLTE4xZAWgWoj8evZovMRwAbCg0WBnYVrH37VcXvuMsPG3aO-IWB63m9uBgk96kckRN-03jOi7e65HRxcGomH9ER9WTx5pXG3zcS26vEnJoR_leBimHIuwFlDKWH_bc4BEb5I0H87z2PubPeCK5R4ORUOJ3xNS25RSjXU1xfR_ZH4y8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
🌟
اشتباكات مسلحة عنيفة بين قوات حزب الله المنصورة وقوات العدو الصهيوني عند اطراف بلدة المجدل.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78649" target="_blank">📅 23:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdqRm0nK1qKigpT4CORanoGYLr3xXsVP9OR6jdDW9DjD3T1KdCX0cgR5i4FUmxpWv_xahmeCrShgGu1J7cbPPwmF0H8YdseRww9_YjB1ezjd5cYX-hTlQt2rh5CpKI3w1jnB0vww5aUotFwKnj11D2yVrLfxdXV0UKEW75Y5Ik6Wvs2MLWLIJ6UAVCUYtdAJxGIyAB7aS6okrBtXs3twZ9t0j52AR7idNLS26EH6zcJZMZvn4pteQ3nY0bgqwu9qqQ4q93XkUQfNZwylZ66R18okin_W5igo8yWdHibcZkLhadNaiEE_OfOfNhdj3B_DZhiG_7OZ9_U9O823UCSbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954d8042fd.mp4?token=BuugGdD940pOoOHacUsd3x6KiXhbf_Z__V2B_Iz1wJ2K7t9yeIPyxwbji4-QX7ZMQn6TaeRcC6CXpXmf_P8IhMQTPyhyVyQvnQCLPtdQdq1TsxjIeWAUvTKsngB5ylaDLKvwFYULSSCyO-HCW-ZgO56AuYldQgfsBSVdbwMVdcg3VqEVnZhSzxzv4VzMtaMJbCZrB7yMSDpITww-TQ9cBDO9lmmQknB3Y0yEcmgNLZ47bnPwJjwOmz8r7omrboNuVBQTCXvZTep_8zyfUsu8MsD7azzD0YYisvh-ptmDgWdJ4C0Qba7g6ePJESrUqppIfycX-ZVFzDzUEn79d00UWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954d8042fd.mp4?token=BuugGdD940pOoOHacUsd3x6KiXhbf_Z__V2B_Iz1wJ2K7t9yeIPyxwbji4-QX7ZMQn6TaeRcC6CXpXmf_P8IhMQTPyhyVyQvnQCLPtdQdq1TsxjIeWAUvTKsngB5ylaDLKvwFYULSSCyO-HCW-ZgO56AuYldQgfsBSVdbwMVdcg3VqEVnZhSzxzv4VzMtaMJbCZrB7yMSDpITww-TQ9cBDO9lmmQknB3Y0yEcmgNLZ47bnPwJjwOmz8r7omrboNuVBQTCXvZTep_8zyfUsu8MsD7azzD0YYisvh-ptmDgWdJ4C0Qba7g6ePJESrUqppIfycX-ZVFzDzUEn79d00UWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف آلية تابعة لجيش الإحتلال الصهيوني في بلدة مجدل زون بجنوب لبنان واعمدة الدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78647" target="_blank">📅 23:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfbcbaedf.mp4?token=QVDc528V8lmQHBbIpt_QuJkSNrg-EWhTBXflW5cmsaztw7hk9I9Fb2FrhqS8_yO1aQrDigktQ1dYL3LpmWXOgswYSY-59GuT_q6TrwZkbVnRGI7Fao6RcoHC4pk7GfS98IsVKv9OKBpOFCImTmnoLJVrhSynZe8JFg9KGm-6VcW5_jLKs6gjt8t4BMjZ_WlZbop8kxqUkpz-EZkFah6mkV42kTCVftTwyRcQxzb7c2xTKmqAs6r21uxqAAHldp2HwCTs-9gZjbv000dPZb5rihNGmrnXV8GpRzZwm2p7XCJ46LT-UtX0Dq8uVVYkLnpevUkk3T6qin4_nDMe8iYddVoyJg6Sa9pUF9qReI4_Q1X1qmbwGTpMVygHSdHRYjsOxZ3Nivg8aJ5MLUbfo0B662im0kupY5dj5G2nlxdPwr95Cln9b9TjvJ8iXmGR0195nVOxBCpWpu7Su3CPCuHkBQW2VSb3A7YLgDaPoalwGkNquObAr3iifwHXL-AcoOazTAeTIHxqfOk7ng3C-OigE3SpQQ5YhPZdJRgFYkm2fy5UxHqVq-82H6rkHA4IxN6Zmm-sAf3538Ds6uXCw9FLaJtQkJIZA7vTCEN7MRrRDM7yZj19PPvyaEcLiIBDLWsPGd3mCjx3Ia5sKJNFEEJIzMk1cr8IeA7j40w8rgRxeU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfbcbaedf.mp4?token=QVDc528V8lmQHBbIpt_QuJkSNrg-EWhTBXflW5cmsaztw7hk9I9Fb2FrhqS8_yO1aQrDigktQ1dYL3LpmWXOgswYSY-59GuT_q6TrwZkbVnRGI7Fao6RcoHC4pk7GfS98IsVKv9OKBpOFCImTmnoLJVrhSynZe8JFg9KGm-6VcW5_jLKs6gjt8t4BMjZ_WlZbop8kxqUkpz-EZkFah6mkV42kTCVftTwyRcQxzb7c2xTKmqAs6r21uxqAAHldp2HwCTs-9gZjbv000dPZb5rihNGmrnXV8GpRzZwm2p7XCJ46LT-UtX0Dq8uVVYkLnpevUkk3T6qin4_nDMe8iYddVoyJg6Sa9pUF9qReI4_Q1X1qmbwGTpMVygHSdHRYjsOxZ3Nivg8aJ5MLUbfo0B662im0kupY5dj5G2nlxdPwr95Cln9b9TjvJ8iXmGR0195nVOxBCpWpu7Su3CPCuHkBQW2VSb3A7YLgDaPoalwGkNquObAr3iifwHXL-AcoOazTAeTIHxqfOk7ng3C-OigE3SpQQ5YhPZdJRgFYkm2fy5UxHqVq-82H6rkHA4IxN6Zmm-sAf3538Ds6uXCw9FLaJtQkJIZA7vTCEN7MRrRDM7yZj19PPvyaEcLiIBDLWsPGd3mCjx3Ia5sKJNFEEJIzMk1cr8IeA7j40w8rgRxeU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف
آلية
نميرا قيادية تابعة لجيش العدو
الإسرائيلي في أطراف بلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78646" target="_blank">📅 23:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
اعلام العدو:
في قلب الجدل الآن: ما معنى الاتفاق بين الولايات المتحدة وإيران بشأن لبنان
الإيرانيون يطالبون بالانسحاب الكامل الذي بالطبع لن يحدث
هناك خمسة مواقع للجيش الإسرائيلي في لبنان كانت موجودة في يوم بدء زئير الأسد
تقدم الجيش الإسرائيلي إلى الخط الأصفر في وقف إطلاق النار في أبريل
ومنذ ذلك الحين تقدم بشكل ملحوظ أكثر
إسرائيل ترفض أي انسحاب
الولايات المتحدة ترغب في انسحاب إلى الخط الأصفر
إسرائيل ترفض</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78645" target="_blank">📅 22:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
‏
سموتريتش
: مقابل كل إطلاق نار على شمال إسرائيل يجب هدم 10 مبان في ضاحية بيروت.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78644" target="_blank">📅 22:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKqzoTo-wKfEbvv7YnRC_FDZNkTBq_8fitP0oLBT2d-hfwrwePa2a2u2QQTfVjqpimUAFwERZWZP8OqQlpvARSLD0uAAaqWO-wkQ-8BS65NpMYIzBkcyk-zffWPp8tayl0aEhRSFgJGCKbA3e4htfwWSLMX53D1qR8HxyU3ZsBB2vYo22B4SioVun-y4X01JnRcoVnMhvdFRvOFlBSRKvxqw74KGCeYxvA-ai8njPNyTYTyWTZttlGK-m6xlyqy-zEzMhNCS6lnVQ-KqHT3stHGMgSMMpGgjvsQNrluzH3pDwcTA0vOS7C5LfzP6JdPUNuPTsp66p8uB-8CKkZA-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ همام حمودي خلال ملتقى الحوار: الفتوى إلهام رباني والحشد مشروع مرجعية يجب إبعاده عن الهيمنة الحزبية
- فتوى الجهاد الكفائي إلهام رباني لمرجعية شجاعة، تبلورت فيها رؤية واضحة للمستقبل، صنعت من المأساة أمناً، ومن العسر يسراً، ومن التمزيق تلاحماً ونصراً.
- داعش مشروع صهيوني، وجسدت بما ارتكبته من مجازر في سبايكر وغيرها الوجه الأسود للطغاة كهتلر ونتنياهو وصدام والبعث، ولمدرسة القتل والشوفينية والإرهاب.
- لقد حقق الحشد بتضحياته وشجاعته وقوة إيمانه في غضون ثلاث سنوات انتصارات وإنجازات تدرس الآن في الخارج بعد ان ظن العالم ان المعركة قد تمتد سنوات طوال جداً.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78643" target="_blank">📅 22:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف آليات تابعة لجيش العدو الإسرائيلي في أطراف بلدة يحمر الشقيف جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78642" target="_blank">📅 22:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d51d4374c.mp4?token=R-wM0Bl1HQQCO_MkVLTxpYFoc_uOCsUVVdNCFqYutSPKyJcunVLxc3x8IQBRgOT7ShkgLdZRTqyEt8e3eHYwnGM_dsMX3gRRN1X0ZhIrxp3olwN53CW-K9COR2x5H3_t5Z2HAPC0pswwtjNXHDPgcWPslxbugAxparqkQl95XVs-znyl5QZyEqEHpnXw07kBbqKCDaD1iZBuKRvtxqvj_2uhWZMatpuX0Q1SRV1ReFXBt3A9_277fCCCCZef6k7_p3MgK5ZHliGseXrlI-dmhE1-fW-8nxVyjsNrTiZfgWmypEwLv7Rkg_lnGXz5_hEfBYDKyItxD3tnaL0OqRbSCk4146-p0MmBllBIpdCQVPjtk5CrU6TVczBhX8xLqmmlNwzRcbsezg9uO2A3jIYdVxbxiqbA3EuaZSr4jdz2pY-0FdNjipIwvi8c8IS4cAY6jiXoHDywOYDjFD421rUrkp0nieUweq6uatf2AYGc5H2EGndESRlIQYAAeFfSTZV6GxUcvDyY1VWY1rz20tW0jtGqRZFIvpnlRYaLcHkTDjar5nc96O7iUKnSzS-y5fSmQQeg09I6tPCqWSE-pGu-SCLVjubTZzlQR4s_aC39KfyzIkEJwMlfn64zuyPryTXQlB7SYtmf2KC11V6a9oVzMm8mKyKtDiMwRmJ3NxQSk2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d51d4374c.mp4?token=R-wM0Bl1HQQCO_MkVLTxpYFoc_uOCsUVVdNCFqYutSPKyJcunVLxc3x8IQBRgOT7ShkgLdZRTqyEt8e3eHYwnGM_dsMX3gRRN1X0ZhIrxp3olwN53CW-K9COR2x5H3_t5Z2HAPC0pswwtjNXHDPgcWPslxbugAxparqkQl95XVs-znyl5QZyEqEHpnXw07kBbqKCDaD1iZBuKRvtxqvj_2uhWZMatpuX0Q1SRV1ReFXBt3A9_277fCCCCZef6k7_p3MgK5ZHliGseXrlI-dmhE1-fW-8nxVyjsNrTiZfgWmypEwLv7Rkg_lnGXz5_hEfBYDKyItxD3tnaL0OqRbSCk4146-p0MmBllBIpdCQVPjtk5CrU6TVczBhX8xLqmmlNwzRcbsezg9uO2A3jIYdVxbxiqbA3EuaZSr4jdz2pY-0FdNjipIwvi8c8IS4cAY6jiXoHDywOYDjFD421rUrkp0nieUweq6uatf2AYGc5H2EGndESRlIQYAAeFfSTZV6GxUcvDyY1VWY1rz20tW0jtGqRZFIvpnlRYaLcHkTDjar5nc96O7iUKnSzS-y5fSmQQeg09I6tPCqWSE-pGu-SCLVjubTZzlQR4s_aC39KfyzIkEJwMlfn64zuyPryTXQlB7SYtmf2KC11V6a9oVzMm8mKyKtDiMwRmJ3NxQSk2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-06-2026 المقر المستحدث للواء المدرعات (401) التابع لجيش العدو الإسرائيلي في بلدة دبل جنوبيّ لبنان بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78641" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02861fd01.mp4?token=FJRsBQXofajnLBmM_XybOaWTrs_qQXMtgW97Bvd1g83-ETM4ilocD24zxOORuDsKIaYEGfcCGc0JI-E7LoTWFV4j6LWykP8PA_n6DIAkvRHxLuX9tMnz1PD1_BLAmS09wl87YXQMzfZa3PFR5ZFmTGsLvFiN0EZchkZbYROk4SmrX41bH6YJN3Vs88M7n1wGgnpIj_B4n-3n1-YUOvxaC_McPvXW9CZKdozLRhhkCRbOYhlH1jUPHhrefXHYfRrs-lRbOe_V39EB3RZVqcd4nJwzRyynVT5k5pHwfePfe7Owo3CYirBSDXgZG6VdS4Ha503a08wG_oTmetJnEnMgBXxd-Oho_VphVOVyyhhhdqxFoboEku_nQ0yEU9ibwoLrgZuy7CbilKuVO5vTJYs3fLv0opLyVucYHukfJNGTaQWSEKz1z56G2VvT3wU4V_URnud-WR4BXGrekutl0KLgazvc5KKIGeA6Hd97JW9c1x5Q3yfo9zsy-PhD71HmhvCP9_i2dFd6heRayL7LimlLuPE4oa9b90mqy5TpYsftgvGD_ZsGH6I9hNCcFfewtH9AArtInbmYkZukQ6w0NVr2KHdEFTH-3VMb2B6tFkKbL7HfwtN1VWK45jbaYbNnXfhn1tXLgygaEfhQ53hJoURNElllLAckNKuekTpfjXJegJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02861fd01.mp4?token=FJRsBQXofajnLBmM_XybOaWTrs_qQXMtgW97Bvd1g83-ETM4ilocD24zxOORuDsKIaYEGfcCGc0JI-E7LoTWFV4j6LWykP8PA_n6DIAkvRHxLuX9tMnz1PD1_BLAmS09wl87YXQMzfZa3PFR5ZFmTGsLvFiN0EZchkZbYROk4SmrX41bH6YJN3Vs88M7n1wGgnpIj_B4n-3n1-YUOvxaC_McPvXW9CZKdozLRhhkCRbOYhlH1jUPHhrefXHYfRrs-lRbOe_V39EB3RZVqcd4nJwzRyynVT5k5pHwfePfe7Owo3CYirBSDXgZG6VdS4Ha503a08wG_oTmetJnEnMgBXxd-Oho_VphVOVyyhhhdqxFoboEku_nQ0yEU9ibwoLrgZuy7CbilKuVO5vTJYs3fLv0opLyVucYHukfJNGTaQWSEKz1z56G2VvT3wU4V_URnud-WR4BXGrekutl0KLgazvc5KKIGeA6Hd97JW9c1x5Q3yfo9zsy-PhD71HmhvCP9_i2dFd6heRayL7LimlLuPE4oa9b90mqy5TpYsftgvGD_ZsGH6I9hNCcFfewtH9AArtInbmYkZukQ6w0NVr2KHdEFTH-3VMb2B6tFkKbL7HfwtN1VWK45jbaYbNnXfhn1tXLgygaEfhQ53hJoURNElllLAckNKuekTpfjXJegJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
08-06-2026
آلية قيادة وسيطرة تابعة لجيش العدو الإسرائيلي في أطراف بلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78640" target="_blank">📅 21:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV4XiZBi24LKpuGkJ7MQaxA0MAJ0LYW2dBNQRbyr05VnR9gYWTZ5pPohJQBwjB9efXviszeLguuDfe7Ch7MlYgN5Fb2hOusVE_NafRNZ-vAjafebVKrmjGX5QQvLUB8Ggmh68leXqWdlZVodAj6HRzt3i2w57KgMym__0c1lXjued5UTXaOFVlQfOuKNfw0qMr5gxIpQbI-_0wb8y8Js8UAp6wqbH6QlMXrQQxfTb7wwqXWCnndD2yYcRL2nXWxrQj34CZzDAoGWbwWL7ahGnjT0XIbaeJwyVznmGwVHaT2zyvhKcv0jlAgN6VMg5Fbld6Y-RXWObSrbXx0F2n6Jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر عبر حسابه الشخصي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78639" target="_blank">📅 21:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامب: كانت صفقة باراك حسين أوباما مع إيران، خطة العمل المشتركة المشتركة، طريقا سهلا وجميلا وسلسا إلى سلاح نووي، كانت إيران ستحصل عليه قبل ست سنوات، وكانت ستستخدمها قبل وقت طويل من الآن. اتفاقي مع إيران هو العكس تماما، جدار إلى عدم وجود سلاح نووي! في الواقع،…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78638" target="_blank">📅 21:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78637">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية إسقاط المقاومة الإسلامية طائرة مسيّرة تابعة لجيش العدو الإسرائيلي من نوع "هيرون 1" في أجواء بلدة نحلة في البقاع.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78637" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
الجيش
الإسرائيلي
يستعد لاحتمال وقف العمليات البرية في جنوب لبنان ولكنه لن ينسحب من المنطقة الأمنية في إطار الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78636" target="_blank">📅 20:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78635">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXgxcwbfUlidKuJJ_CR-vxHkYbF3e4o91X2erHUkGM_KqR_NHRcvcRbjYi4eKVF37T-cNDszBAERXo_i59Nz2wq0u2vUkqJ2zeyD9n4eru7Kad6isS4Yn-BUNephR55brrjV4ijLLZFyd2eMOq_QuHxJ9Cvegtv8ImF-X2fdJERMQBKAQD7neNzEPwX8SiRD3s5_-5siqC0k-2Ode3X0ixGiGkeO2mUSfjhccurh2MQmP4L2-Buzc_y0kUdRPUYRzHxlv9A6MzWRe2b0QJISRlxSz4bphArkGlz4sBtCARtuAmQRuEe7PfDAMGERbsm_Ood0nPHyi_cMJU6mQMa9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
كانت صفقة باراك حسين أوباما مع إيران، خطة العمل المشتركة المشتركة، طريقا سهلا وجميلا وسلسا إلى سلاح نووي، كانت إيران ستحصل عليه قبل ست سنوات، وكانت ستستخدمها قبل وقت طويل من الآن. اتفاقي مع إيران هو العكس تماما، جدار إلى عدم وجود سلاح نووي! في الواقع، لم يعودوا يريدون سلاحا نوويا، ولن يكون لديهم سلاح، إما من خلال الشراء أو التطوير أو أي شكل آخر من أشكال الشراء. من المقرر توقيع الصفقة غدا، وبعد توقيعها مباشرة، يكون مضيق هرمز مفتوحا للجميع. علاقتنا مع إيران مختلفة جدا وأفضل من الإدارات السابقة. على عكس مئات مليارات الدولارات من مدفوعات أوباما لهم، بما في ذلك 1.7 مليار دولار نقدا أخضرا وباردا، لن يتبادل أي أموال الأيدي. في الوقت المناسب، عندما يكون كل شيء هادئا، سندخل ونحصل على الغبار النووي، المدفون في أعماق جبال الجرانيت الغارقة القوية، وذلك بفضل قاذفاتنا B-2 الجميلة وطياريها الرائعين، ونمزجه وتدميره، سواء في إيران أو الولايات المتحدة. نتطلع إلى العمل مع إيران، والشرق الأوسط بأكمله، لفترة طويلة في المستقبل. نأمل أن تنجح هذه العملية بسرعة وسهولة وسلاسة. إذا لم يحدث ذلك، فلدينا البديل النهائي، ونأمل ألا يتم استخدامه مرة أخرى! شكرا لك على اهتمامك بهذه المسألة!!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78635" target="_blank">📅 20:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84518f17ac.mp4?token=NnOK36wnmoP2cij_H32Y5szoWtVmjNu5Lt_s6CO_1jeraf9_ZwFOv-39zMciDuAMyp0vwmE85vbSBGDCewKnSHRzvq4ltasfNbIq8sDvSbkJyG2rhLWOvII5J256EJaCaA8WUWKyCzWCKhMMmEPmShwfOkZpQrYRN4GoaLGb1PQYfYClq_FYloVoM_9aeVqwpcp2hO6suE0LGEl_IYYYCYFkP6K1hkEpCH7YXvPBVjNkhqAoIEOMMr_LoQQa0Y5hcaAIfOaFf33PZOJ2eIMuWtzTE0TEdFAARIHyyWY0WPdDILpBg1_9ZHwaWVvu7LlFbQK-WOZ2PjBGbQMTa2hbbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84518f17ac.mp4?token=NnOK36wnmoP2cij_H32Y5szoWtVmjNu5Lt_s6CO_1jeraf9_ZwFOv-39zMciDuAMyp0vwmE85vbSBGDCewKnSHRzvq4ltasfNbIq8sDvSbkJyG2rhLWOvII5J256EJaCaA8WUWKyCzWCKhMMmEPmShwfOkZpQrYRN4GoaLGb1PQYfYClq_FYloVoM_9aeVqwpcp2hO6suE0LGEl_IYYYCYFkP6K1hkEpCH7YXvPBVjNkhqAoIEOMMr_LoQQa0Y5hcaAIfOaFf33PZOJ2eIMuWtzTE0TEdFAARIHyyWY0WPdDILpBg1_9ZHwaWVvu7LlFbQK-WOZ2PjBGbQMTa2hbbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يدكون آلية أخرى تابعة لجيش الإحتلال الصهيوني في محيط بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78634" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
توثيق يظهر توقف العديد من السفن في الخليج الفارسي بعد إغلاق مضيق هرمز من قبل القوات المسلحة الإيرانية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78633" target="_blank">📅 19:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSg6uTE2p3MtJpEOR0JYDj1Nt8ng7bWB3YeHma7_VEby4Tz7W1eE08Jw1CP2jI0f59AJl4-6RdfAkXlOOSjHlN8d_m0BGnXpOq9UyIz89hUsYJbd9VLW_c3SwxPVDChiKSGXv4vXMwvvTJIedU2JFLH71XOLt2_u2m9OUCJu4fcoZ-y9u7WvUy0wrjYbIEjIw3wrylhyXO-TYUuWH3VQSlELCavTgYX9ebkIej-uee86QGP7SRWniTpunjowFMvYFQ-TSmT5xWqFf6bX8ncq5358ufRGzJLbO_KH1lC-bK11R-0p3CtYhCYYkC8pJ_kPz7FSQPX5Hmuq6JXbIG4Bww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف آلية تابعة لجيش الإحتلال الصهيوني في بلدة مجدل زون بجنوب لبنان واعمدة الدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78632" target="_blank">📅 19:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
حزب الله:
ועוד היד נטויה - والحبل عالجرّار</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/78631" target="_blank">📅 19:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
الخارجية الباكستانية:
إسلام آباد ستنظم غدا حفل توقيع إلكتروني عبر تقنية الفيديو على اتفاق سلام أمريكي إيراني.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78630" target="_blank">📅 18:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
يجب أن نتقاضى ثمن الخدمات المقدمة في مضيق هرمز.
يجب إنهاء وجود القواعد الأجنبية والوجود العسكري في المنطقة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78629" target="_blank">📅 18:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مسؤول امريكي لرويترز: سنساعد في إزالة الألغام عند إعادة فتح مضيق هرمز، ويمكن لدول مجموعة السبع المشاركة</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/78628" target="_blank">📅 18:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📰
مسؤول امريكي لرويترز: نعتقد أننا توصلنا إلى اتفاق قوي مع إيران.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/78627" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴‍☠️
مسؤول رفيع المستوى في الإدارة الأمريكية: سيجتمع ترامب مع قادة دولة الإمارات العربية المتحدة وقطر ودول أخرى في الشرق الأوسط في مجموعة السبعة G7</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/78626" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
مسؤول رفيع المستوى في الإدارة الأمريكية:
سيجتمع ترامب مع قادة دولة الإمارات العربية المتحدة وقطر ودول أخرى في الشرق الأوسط في مجموعة السبعة G7</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78625" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
وزير الخارجية الباكستاني في حديث مع نظيره السعودي:
تم تحديد التوقيع الإلكتروني على الاتفاق بين الولايات المتحدة وإيران ليوم غد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78624" target="_blank">📅 17:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ 05-06-2026 آلية هامفي تنقل جنود جيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78623" target="_blank">📅 17:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
🌟
وسائل اعلام:
وفد إيراني يضم وزير الخارجية يصل باكستان غدا.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78622" target="_blank">📅 17:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
🌟
وكالة مهر:
قدّمت قطر خطةً تُتيح بموجبها تقديم 12 مليار دولار لإيران تشمل الإفراج عن 6 مليارات دولار من أصولها المجمدة في قطر و6 مليارات دولار أخرى على شكل قرض أو خط ائتمان.
ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78621" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78620">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d92db5d7.mp4?token=rLpq6kGs_NYVw_BoMc9-YQ9iUQGPVZ7SDgrtpogghDBw2erYCjuTgny-Zv0SLaSwUa0V2L5NsZV4YiIn7CW_LtDnmPrYNYzKvXungYep3Kk5VW9V4YAY7Nb-tLJro0b62hxwlxpioyO--b3uFacCCXreSvXFmke1HqrRYGktzwlHOryU1Lhlg6D4MCDS2-c3tubcdNFU9BMFm2DNhjBsOh5RYZThUJAMXla6rAdYJePDeXRb4dx5RM-IOx0GYyBHAeryib4lqXajmFntYJ4w86X5Kw5IdndavDtntfszypqyg7BVMXwp9_1lrdPIAlBiUcZd9u0mdD-5vPiaEQt8CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d92db5d7.mp4?token=rLpq6kGs_NYVw_BoMc9-YQ9iUQGPVZ7SDgrtpogghDBw2erYCjuTgny-Zv0SLaSwUa0V2L5NsZV4YiIn7CW_LtDnmPrYNYzKvXungYep3Kk5VW9V4YAY7Nb-tLJro0b62hxwlxpioyO--b3uFacCCXreSvXFmke1HqrRYGktzwlHOryU1Lhlg6D4MCDS2-c3tubcdNFU9BMFm2DNhjBsOh5RYZThUJAMXla6rAdYJePDeXRb4dx5RM-IOx0GYyBHAeryib4lqXajmFntYJ4w86X5Kw5IdndavDtntfszypqyg7BVMXwp9_1lrdPIAlBiUcZd9u0mdD-5vPiaEQt8CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
How did China , Russia, North Korea see the war in Iran ?!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78620" target="_blank">📅 16:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حادث غير عادي في أجواء المجر: طائرة إسرائيلية تفقد الاتصال مع مراقبة الحركة الجوية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78619" target="_blank">📅 16:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78618">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حادث غير عادي في أجواء المجر: طائرة إسرائيلية تفقد الاتصال مع مراقبة الحركة الجوية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78618" target="_blank">📅 16:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78617">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: مذكرة تفاهم إسلام آباد تركز على إنهاء الحرب في هذه المرحلة دون مناقشة الملف النووي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78617" target="_blank">📅 16:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78616">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية:
مذكرة تفاهم إسلام آباد تركز على إنهاء الحرب في هذه المرحلة دون مناقشة الملف النووي.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78616" target="_blank">📅 16:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc8c581a7f.mp4?token=VPxF1zUO8V48BWP0fKU4KhqQbmDMkM9L_ye7pKmND3_qtVVxDk_56BrJW3usr-wt4b3XJOoTP13nXj9YIaaSX4gGOUrEHXcLpXM8LEkjZKcGZWXtEP0HdQFF0wLGi2GK76tvewbt1rSEDuB_dFg7K3kDLfIMJqAAO-urRlD9nO1aqAJr59H4SsMEsHhj03bBgAo-FTTb_SItjFKTqLyRwLJsg9XpnEM10czJYzXiSW1UxTBDM_KFriXJjKGn_XRJVS64GDNjwXMONWPOnGatyDZ88dEE7sloHRnZIoN48pSpk6OyfzPORdQbXDhJg7Mnes85dveG2dScnQQuF3FZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc8c581a7f.mp4?token=VPxF1zUO8V48BWP0fKU4KhqQbmDMkM9L_ye7pKmND3_qtVVxDk_56BrJW3usr-wt4b3XJOoTP13nXj9YIaaSX4gGOUrEHXcLpXM8LEkjZKcGZWXtEP0HdQFF0wLGi2GK76tvewbt1rSEDuB_dFg7K3kDLfIMJqAAO-urRlD9nO1aqAJr59H4SsMEsHhj03bBgAo-FTTb_SItjFKTqLyRwLJsg9XpnEM10czJYzXiSW1UxTBDM_KFriXJjKGn_XRJVS64GDNjwXMONWPOnGatyDZ88dEE7sloHRnZIoN48pSpk6OyfzPORdQbXDhJg7Mnes85dveG2dScnQQuF3FZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان صهيوني يطال بلدة كفر رمّان جنوبي لبنان.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78615" target="_blank">📅 16:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231e7d73b7.mp4?token=KTn3OCRZLNTL_so9HJRzm4f8e5pzpDd5-0qG3KhXLk12OAHq31mYPomd_nVx0jVjOxvkXxMyfTTb4_xiT2tJioKZ6P-aZKIbdYTgCoSUi9xAqPaOk2Kwb61LPMZtF6ETZ-OCO4L9nmAf9c8qtS8QhDZdq0idZ5Gl03f045RrpyesnmJ8qfgN6WH7SXirLUuKq4rjx8dlYnDhmtvaN9yYM7Q7AomlOJeNrK_srSWMwZu5JBwjE7x3PCWrfuVnb2oqtvjGtK1clPMtO8_nt0ouAiuz7VJ3DvHHPdC-rD8HtogNmBC0ALwzzaWQZcbtJvOFh_fFyYJSQ2dNnLghqtx4Nl0oMXs4ogbzZ3ViLzeppZ2hSKEJjFKOQE2xh-zQOACLAMu-HUhxpzRikQ_k3GYohtWZdLxYfI3QMjDUhIxnZj5QqXpJOyJgZGULz0z21S0sRKLlYDIGMEfgNC-gypbBKPBVD34pZKKuOd0zDMG6C696aWXZgpfXxcLUF7RboOLk99cSi7Xq4HkKB-NZvipL9JJngEUsCHv-gOF3zhqwmTGTKnHZMZM5H830EWfLNt2AoYXb-npyS3DWWs3YA19poJV3wQi7hSkeZdMdVy22m24LPUUzU4J8h_KmFI1Wg3soZjG-rEOKy65Ho_-njN2Nh76_1vg5yGEJVIfqgKizko8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231e7d73b7.mp4?token=KTn3OCRZLNTL_so9HJRzm4f8e5pzpDd5-0qG3KhXLk12OAHq31mYPomd_nVx0jVjOxvkXxMyfTTb4_xiT2tJioKZ6P-aZKIbdYTgCoSUi9xAqPaOk2Kwb61LPMZtF6ETZ-OCO4L9nmAf9c8qtS8QhDZdq0idZ5Gl03f045RrpyesnmJ8qfgN6WH7SXirLUuKq4rjx8dlYnDhmtvaN9yYM7Q7AomlOJeNrK_srSWMwZu5JBwjE7x3PCWrfuVnb2oqtvjGtK1clPMtO8_nt0ouAiuz7VJ3DvHHPdC-rD8HtogNmBC0ALwzzaWQZcbtJvOFh_fFyYJSQ2dNnLghqtx4Nl0oMXs4ogbzZ3ViLzeppZ2hSKEJjFKOQE2xh-zQOACLAMu-HUhxpzRikQ_k3GYohtWZdLxYfI3QMjDUhIxnZj5QqXpJOyJgZGULz0z21S0sRKLlYDIGMEfgNC-gypbBKPBVD34pZKKuOd0zDMG6C696aWXZgpfXxcLUF7RboOLk99cSi7Xq4HkKB-NZvipL9JJngEUsCHv-gOF3zhqwmTGTKnHZMZM5H830EWfLNt2AoYXb-npyS3DWWs3YA19poJV3wQi7hSkeZdMdVy22m24LPUUzU4J8h_KmFI1Wg3soZjG-rEOKy65Ho_-njN2Nh76_1vg5yGEJVIfqgKizko8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاوةُ جزءٍ من وصية الإمام الخميني على لسان القائد الشهيد للثورة الإسلامية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78614" target="_blank">📅 15:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 05-06-2026 تجمّع لجنود جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78613" target="_blank">📅 15:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اعلام العدو: طائرة بدون طيار مفخخة سقطت في موقع عسكري مستحدث في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78612" target="_blank">📅 15:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اعلام العدو:
طائرة بدون طيار مفخخة سقطت في موقع عسكري مستحدث في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78611" target="_blank">📅 15:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2rF19QhDBxbb2GyEZ_UaLp2ieKs535p4UdBaqOtTqHa81Ur3iqI65Sqby3323r3izzEpF99eF7v-RxQ3K2MsdRqyl5OmT3W8sb025UkabowMsnvdDCaimpGYMvXeXvykaJXiW6x_aIP-WacoEcY3KgXgf1yG3vJ6T3qHy1lsCllIP7lT7Me5Nz7WSJm6R0qaKch9M9aHT6ALSsryDoD1sCWbTwt1_c0wTdQIiJe1B_xa8E4yJdI7VSD76maa0N9Rl6NPdh1aKdjJcIMSksjHuSoHzZ1UgA2N0prEI1SaoW7lsYkiZhbGAVL_ZaZ15mcjrke_7pgfXfv23V8J0pQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">١٣/٦/٢٠١٤
🇮🇶
اعظم يوم بتاريخ العراق المعاصر ؛ ذكرى تاسيس المؤسسة الأكثر عطاء في العالم انهم قوات الحشد الشعبي اليد الضاربة للشعب العراقي .</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78610" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">استهداف سفينة في بحر عمان</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78609" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78608">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رئيس الوزراء الباكستاني: توقيع الاتفاق بين ايران والولايات المتحدة سيكون الكتروني.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78608" target="_blank">📅 14:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">استهداف سفينة في بحر عمان</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78607" target="_blank">📅 14:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رئيس الوزراء الباكستاني:
توقيع الاتفاق بين ايران والولايات المتحدة سيكون الكتروني.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78606" target="_blank">📅 14:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce9584a4b.mp4?token=RHVKYFVsce2480G0B7kzN5lqH1xLxorBSc0rOIYglKx1TqQkoUubYCMRn3n2FZtKGbUFDVXB47w_duJKzB9ilpxjyM9zprJPGevMJekr6yxdZk_-egnt_KfxOqqzj20Wu_PIme5JseG20c0-kJiWjP42Ndu2D0zpdRgNbXwscv56ITORjCqvSjPxFOkybVbZJQG3wOeUjGWUQNpShkLYkoQHJDZkeHEInT99yRxahV3WkuHSFM3Y4su6kHBZR2rryQIFiMKeCkjUe1Zr-AnW6uWxrmIy6eehvWzuhf7BsTulE5k2iAYOJvI9Dccc96dgFYdVMFD-LZFtgAX6t8D7BJL7PuqEHG5NJQsQvljhNxSqBIsDvsTZPzO_ZL3Fm9oHjS2WOTuCnFIACr1Ua67Kq0mzZX3olETyFex58VlQGIR_CwlgWMD7x-56YIBgsAifY8VCZ2loKFRftZZBTQW6Oyrw3f2X_BkbPpYkL3iuCXyaa2gUXdcQ4WFqg6oHPttPUB-S_Mn7-FRCIfYR3WJ0kp-EAnLWnFSLztIZrdVyPUmhjZMYLah_aC5arHVNOnCeDnAZ9iClDOH26lUKDeTm9iIQ2I_azl5LXL7_dPWQgnXNF2Z7NkUStJGmCStG-HirPHDYDHPehZuNy0mC6VjrMX8zhiwUYG_s_LGxMLBSwIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce9584a4b.mp4?token=RHVKYFVsce2480G0B7kzN5lqH1xLxorBSc0rOIYglKx1TqQkoUubYCMRn3n2FZtKGbUFDVXB47w_duJKzB9ilpxjyM9zprJPGevMJekr6yxdZk_-egnt_KfxOqqzj20Wu_PIme5JseG20c0-kJiWjP42Ndu2D0zpdRgNbXwscv56ITORjCqvSjPxFOkybVbZJQG3wOeUjGWUQNpShkLYkoQHJDZkeHEInT99yRxahV3WkuHSFM3Y4su6kHBZR2rryQIFiMKeCkjUe1Zr-AnW6uWxrmIy6eehvWzuhf7BsTulE5k2iAYOJvI9Dccc96dgFYdVMFD-LZFtgAX6t8D7BJL7PuqEHG5NJQsQvljhNxSqBIsDvsTZPzO_ZL3Fm9oHjS2WOTuCnFIACr1Ua67Kq0mzZX3olETyFex58VlQGIR_CwlgWMD7x-56YIBgsAifY8VCZ2loKFRftZZBTQW6Oyrw3f2X_BkbPpYkL3iuCXyaa2gUXdcQ4WFqg6oHPttPUB-S_Mn7-FRCIfYR3WJ0kp-EAnLWnFSLztIZrdVyPUmhjZMYLah_aC5arHVNOnCeDnAZ9iClDOH26lUKDeTm9iIQ2I_azl5LXL7_dPWQgnXNF2Z7NkUStJGmCStG-HirPHDYDHPehZuNy0mC6VjrMX8zhiwUYG_s_LGxMLBSwIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على ذمة اي نيوز
سجلت محافظة المثنى ضمن اكثر المحافظات فقراً ؛ ٣٦ مليار من واردات بلدية المثنى وتم تسجيلها من ديوان الرقابة المالية تسرق من رئيس هيئة الاستثمار بالمحافظة بعد بقائه منذ ٩ أعوام  .</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78605" target="_blank">📅 14:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-06-2026 تجمّع آليات وجنود جيش العدو الإسرائيلي في بلدة القنطرة جنوبيّ لبنان بصاروخٍ نوعي.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78604" target="_blank">📅 14:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f58e3487.mp4?token=YnLs0s-xeJX89WiA2nmksFY_IEUPjLlsKqQEJzTJhY5UHQ68wxVt8cF67ThAi0Xp5W6eqfHCnxsRwsKDXEI3AcVqkIrBX_nvQBfzPbj2_nrpWapIfRZyqzBkLbPJq9bvMjbUa76V4g4ZfnwDV8fN9MBu3E98x8lZng2qjFduqdOVrYKDkkQfuJ676SoHceEdOip_9v_zh__VpGJSvz-vvXSr1a2XeDXtTHa_toPiN4ir7aybXArF9XqVlRBoUHNeEFdvzq29xbKSK04_WTjuvv_z4t7cdBhnQseMayVjgRboK8tcLACX2uHgxbDxfixBwMNoMNjH-r35QZGNi44shQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f58e3487.mp4?token=YnLs0s-xeJX89WiA2nmksFY_IEUPjLlsKqQEJzTJhY5UHQ68wxVt8cF67ThAi0Xp5W6eqfHCnxsRwsKDXEI3AcVqkIrBX_nvQBfzPbj2_nrpWapIfRZyqzBkLbPJq9bvMjbUa76V4g4ZfnwDV8fN9MBu3E98x8lZng2qjFduqdOVrYKDkkQfuJ676SoHceEdOip_9v_zh__VpGJSvz-vvXSr1a2XeDXtTHa_toPiN4ir7aybXArF9XqVlRBoUHNeEFdvzq29xbKSK04_WTjuvv_z4t7cdBhnQseMayVjgRboK8tcLACX2uHgxbDxfixBwMNoMNjH-r35QZGNi44shQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">١٣/٦/٢٠١٤
🇮🇶
اعظم يوم بتاريخ العراق المعاصر ؛ ذكرى تاسيس المؤسسة الأكثر عطاء في العالم انهم قوات الحشد الشعبي اليد الضاربة للشعب العراقي .</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78603" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78601" target="_blank">📅 13:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">To Zendei (Echoes Of An Eternal Life)</div>
  <div class="tg-doc-extra">Ehsan Yasin - Ehsan Saeedi</div>
</div>
<a href="https://t.me/naya_foriraq/78600" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">أنشودةٌ موسيقيةٌ بلا كلام «أنت حيّ»
هديةٌ قُدِّمت بمناسبة أربعينية الشهادة إلى الإمام الشهيد خامنئي الكبير، ذلك الروح الطاهر السماوي
نغمةٌ تكسر اختناق الدموع المكبوتة طوال هذه الأربعين يومًا…
#شاركها</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78600" target="_blank">📅 13:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/78599" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78598" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🙃
🇮🇷
فضيحة من العيار الثقيل
زلينسكي الذي لم يحمي سماء كييف ولا خاركيف يريد ان يضحك على بعض دول الخليج التي فشلت منظوماتها الأمريكية بالدفاع عن سمائها في المواجهة الأخيرة مع ايران ؛ من خلال التسويق لمنظومات أوكرانية مستخدما تطبيقات الذكاء الصناعي وفديوهات معدلة ف " جيران  " النسخة العكسية عن شاهد ١٣٦ أصبحت الزائر اليومي للقطعات العسكرية الاوكرانية المدعومة من حلف الناتو دون وجود اي حلول ممكنة للتصدي لها كيف سيؤمن سماء البحرين والسعودية ؟!
😆
الحل الأفضل هو اتباع الطريقة الاماراتية دفع أموال لايران و ضمان عدم استخدام أراضيهم كمنطلق للعدوان .</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/naya_foriraq/78597" target="_blank">📅 13:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuQse2ZWw9FQw9E3RLDp4hUwFYp3F2_bq0A2TYhG7RW99Le47RM0ttkh4SO2zTCSMcmTW2r6eVexG4Xfr6zUnf7tuyDbVBgkEhVe5Ctw-wzCKbOrthUG65xPxEFOo5ABkQ_cSD-MHY8py9zsB7kovRrXOIVc1CwFK1EpEkEQIavQpAy4rfquOfMz_1EyL6MJmlc6ayfs34-W_YDMoFLHr5kSVfEyH-uNOQamJ5ZE3mcKdKaryWDxRONorUlbI-R_QJjNH2yKo_tvQ7v819f202OH5mGOjUjMnixb3wlNUtw6-yLq_EtrjGuvtlc3iqzrDZEsE_iJY_DBjHF-1hGVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙃
🌟
صدور مذكرة القاء قبض وتفتيش بحق مهند الزبيدي مدير مدرسة النعمة العراقية في العاصمة الاوكرانية كييف اضافة الى موظف وموظفة في وزارة التربية العراقية على خلفية تورطهم بعمليات تهريب الدفاتر الامتحانية المدرسية الى الخارج.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78596" target="_blank">📅 12:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏نواف سلام: مشكلتنا مع حزب الله هي سلاحه وعليه أن يكون قوة سياسية فقط
من المفترض أن يكون الجنوب اللبناني خاليا من السلاح</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78595" target="_blank">📅 12:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a0766e31.mp4?token=JHW7x6-OGUZ8D6lZPcHVxO7VssQJAmRwRkKUH_l6N9l4Fny6kNKi4cg3RorFHyXchpkwr-KVjLtFyPkn-jJbeCicwOXVdKsbjCgzodBH5ct_Vx4K35LspWfRFCDIrdFJM1blrVwmtV46SDmqcG50yrehPEAyhmm5N6aMO7r2e160YIY0U6KB1z_X9ZUJdbdca3pX4wVsF76fF1rkT7OJ3cOZG6TYK1gKHRJkhnxwzIiqyZG-M_UCZkl_Ll4dsZK3YRQrz_kQB-kCx0-nqyM9Bz6nMNECVuhzq47naU2UNrTV_qfCahwg891V6a2FYz2m8PA3AZyilt6K9MiNzIIybg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a0766e31.mp4?token=JHW7x6-OGUZ8D6lZPcHVxO7VssQJAmRwRkKUH_l6N9l4Fny6kNKi4cg3RorFHyXchpkwr-KVjLtFyPkn-jJbeCicwOXVdKsbjCgzodBH5ct_Vx4K35LspWfRFCDIrdFJM1blrVwmtV46SDmqcG50yrehPEAyhmm5N6aMO7r2e160YIY0U6KB1z_X9ZUJdbdca3pX4wVsF76fF1rkT7OJ3cOZG6TYK1gKHRJkhnxwzIiqyZG-M_UCZkl_Ll4dsZK3YRQrz_kQB-kCx0-nqyM9Bz6nMNECVuhzq47naU2UNrTV_qfCahwg891V6a2FYz2m8PA3AZyilt6K9MiNzIIybg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: السكان والزوار الموجودون على الشواطئ الجنوبية لايلات يبلغون عن سماع إطلاق نار من جهة البحر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78594" target="_blank">📅 12:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📰
تقرير شبكة CNN:  في الأسابيع الأخيرة، زادت إيران بشكل كبير من جهودها لسد الوصول إلى مخازن اليورانيوم المخصب  وفقًا لخمسة مصادر مطلعة على الاستخبارات الأمريكية، تسببت إيران عمدًا في انهيار أنفاق وزرعت ألغامًا عند مداخلها باستخدام متفجرات  وفقًا للمصادر، أصبح…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78593" target="_blank">📅 11:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📰
‏بلومبيرغ: إيران أضافت على الأرجح أسلحة روسية حديثة لمخزوناتها خلال وقف النار</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/78592" target="_blank">📅 11:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📰
تقرير شبكة CNN:
في الأسابيع الأخيرة، زادت إيران بشكل كبير من جهودها لسد الوصول إلى مخازن اليورانيوم المخصب
وفقًا لخمسة مصادر مطلعة على الاستخبارات الأمريكية، تسببت إيران عمدًا في انهيار أنفاق وزرعت ألغامًا عند مداخلها باستخدام متفجرات
وفقًا للمصادر، أصبح الوصول إلى مخازن اليورانيوم المخصب الآن أكثر صعوبة وخطورة ويتطلب وقتًا أطول مما كان عليه قبل شهر فقط</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78591" target="_blank">📅 11:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: توجد فجوة شاسعة بين نظرتنا إلى أنفسنا والصورة التي تُرسم لنا في الخارج ؛ يُنظر إلى "إسرائيل" في الخارج على أنها بلطجي الحي وتُعتبر تهديدًا للاستقرار والسلام العالميين.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78590" target="_blank">📅 10:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🏴‍☠️
تسلل مسيرات من حزب الله نحو المطلة شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78589" target="_blank">📅 09:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad3b3f7e1.mp4?token=Xracuz3G2H3bn9mOnSH5rQl_35ZHkGSVDUK03PNvkQCwsSD6Csy2-EJUNUNcYLdJRdI1JiK9Kt8Jq4pRl7J2Rt1Ai6EDgbZcP2M4oe3eGrOsnrFy7QG8Y1mSz9F2CBhL2n91e8HJ8b4ym-XE8G5LOPQ6lioHC9HdMErH4PxQQzu_puXNe_S6rhV2mUkiHk8ANJtllD_TCn41M6BowMrHsNjBvIFJwLfOaDA_nXVAZKVdaUKZmu9zd_oReo9cpFq_015rbCeTf9bUTVP_Mvg22CiiOQ3e0b5sUQZK3lEk-adhShsZkNkivVA6BRWo84O3HoLlvQvX_hbtb0SVhLz75Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad3b3f7e1.mp4?token=Xracuz3G2H3bn9mOnSH5rQl_35ZHkGSVDUK03PNvkQCwsSD6Csy2-EJUNUNcYLdJRdI1JiK9Kt8Jq4pRl7J2Rt1Ai6EDgbZcP2M4oe3eGrOsnrFy7QG8Y1mSz9F2CBhL2n91e8HJ8b4ym-XE8G5LOPQ6lioHC9HdMErH4PxQQzu_puXNe_S6rhV2mUkiHk8ANJtllD_TCn41M6BowMrHsNjBvIFJwLfOaDA_nXVAZKVdaUKZmu9zd_oReo9cpFq_015rbCeTf9bUTVP_Mvg22CiiOQ3e0b5sUQZK3lEk-adhShsZkNkivVA6BRWo84O3HoLlvQvX_hbtb0SVhLz75Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
عدوان صهيوني على حي الراهبات جنوب لبنان</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78588" target="_blank">📅 08:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9xGIJxwcoWtcYjUORQlIFLIOvDyCrWeg80ln82ipb7fvF-gDvhzctecEzFZ1hhTB0T3seqv6lyN02uJkq9aDqsBNt_mw6IIuN9A5B7V_FS8tlfSlW5Cq6OK0AoYfkTJrYNf9GrJxInPej6nIGGBGDbQvjzbZpB9KPs1otnGY_QewIxVyIPMpY17trfK75GQJdvpFnJcHuRxXmjhzHNthszbH90DbSl5NPOVQ8QBqhSWNr2sW1LEmX9Wd4sOOSi13Oa6ZS8kfbJfQWq9Rz2zoQrGouQfb7wUWUXfAhBa7dKXVtpAbyCBTKI5DPbW5k4JYjLYcT9zp3MU3wfi6Tqe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: هبوط مروحيات إجلاء في مستشفى الوادي العفولة شمال الكيان بعد نقل جنود مصابين من جنوب لبنان جراء تعرضهم لحدث أمني صعب.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78587" target="_blank">📅 07:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📰
وول ستريت جورنال
: محادثات فنية إضافية بشأن قضايا شائكة قد تجري بعد ذلك في إسلام آباد، جي دي فانس سيتوجه إلى جنيف لتوقيع مذكرة التفاهم مع إيران، عودة وفد قطري من طهران الأسبوع الماضي حاملا صيغة اتفاق جديدة شكلت نقطة تحول حاسمة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/78586" target="_blank">📅 04:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186c1827aa.mp4?token=SJxipZvw1Lsc6DLL7OLWJnbRzId5oxFslLWDjU-dz06BrAXarMSYcLo5hQCOFo-XaYyO2fy_V7I_Cg3FW3VkXcWnO56sZwpwdTd8BTKKjMNGe7xgNLPBB70Lora4itTnPbk1fe7wTEehT8_4dKEu3e7xBixvlz4c9cqfewKxjAAN9lX7BMQtzcfHSNsxaojQkh-O23VeSMaJ1vRGjo296MyrvGCFPFFm-Ue7YtpmGWzFqajFdyVcnTppqgjd_tDcTsT2AKKUfwcVNKGKkN2CYsiJsAY5AXxJyusvndVS681QVaAoK61KFmhmEOwofzWVti9yy0z1JYAQWr8MFRcINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186c1827aa.mp4?token=SJxipZvw1Lsc6DLL7OLWJnbRzId5oxFslLWDjU-dz06BrAXarMSYcLo5hQCOFo-XaYyO2fy_V7I_Cg3FW3VkXcWnO56sZwpwdTd8BTKKjMNGe7xgNLPBB70Lora4itTnPbk1fe7wTEehT8_4dKEu3e7xBixvlz4c9cqfewKxjAAN9lX7BMQtzcfHSNsxaojQkh-O23VeSMaJ1vRGjo296MyrvGCFPFFm-Ue7YtpmGWzFqajFdyVcnTppqgjd_tDcTsT2AKKUfwcVNKGKkN2CYsiJsAY5AXxJyusvndVS681QVaAoK61KFmhmEOwofzWVti9yy0z1JYAQWr8MFRcINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب
:
"بتوجيهاتي، نفّذت القيادة الجنوبية للولايات المتحدة ضربةً سريعةً وقاتلةً أسفرت عن إعدام نينيو غيريرو، الزعيم سيئ السمعة لجماعة ترين دي أراغوا، إحدى أكثر المنظمات الإرهابية دمويةً على وجه الأرض. قبل عودتي إلى منصبي، فتح جو بايدن حدودنا الجنوبية أمام ملايين المجرمين غير الشرعيين، وسمح لهذا الجيش الأجنبي باغتصاب وتشويه وقتل مواطنين أمريكيين دون أي عقاب. خلال حملتي الانتخابية، تعهدتُ بطرد هؤلاء الوحوش من بلادنا، وتحقيق العدالة لعائلات ضحاياهم، بمن فيهم الطفلة البريئة جوسلين نونغاراي ذات الاثني عشر عامًا، ولاكين رايلي ذات الاثنين والعشرين عامًا، وعدد لا يُحصى من الأرواح البريئة الأخرى. بهذا العمل، حقق الجيش الأمريكي الانتقام لهم ولعائلاتهم وأحبائهم." في بداية ولايتي، وفيتُ بوعدي بتصنيف حركة ترين دي أراغوا منظمةً إرهابيةً أجنبية، وترحيل آلاف المجرمين الأشرار، وشن حربٍ على عصابات المخدرات التي لطالما شنت حربًا على مواطنينا، بينما ترك القادة الضعفاء أمريكا عاجزةً في موقف دفاعي. وقد تم تنسيق هذا الإجراء بشكل وثيق مع أصدقائنا في فنزويلا، الذين نتعاون معهم تعاونًا مثمرًا. ونتيجةً لذلك، لم يعد لإرهابيي ترين دي أراغوا ملاذٌ آمن في فنزويلا أو أي مكان آخر، وسنجد هؤلاء القتلة المتوحشين وتجار المخدرات في أي وقت وأي مكان، وسنرسلهم إلى قعر الجحيم حيث ينتمون. حفظ الله أمريكا! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78585" target="_blank">📅 04:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
رويترز
: أطلقت الولايات المتحدة صواريخ على العديد من طائرات بدون طيار الإيرانية أحادية الاتجاه أثناء توجهها إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78584" target="_blank">📅 04:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
اعلام العدو:
ترمب أصدر تعليمات بتخفيف العقوبات عن إيران إذا التزمت بالاتفاق.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78583" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2Qlb6ZxWbeGNKT8E71mWlBoH1qLZF_68GoqNWSi7od9oB60niV9tZQDhATKP0n1R_pr3ho4KVwC4TOMHTeaUkd5UgKhG2vBUXQJptSdmVJO9zlcGSUgUSl9olD3oBwReOAn4Ro8p7aDZT2kiIRUAd0CQvNS-hXCwODjQ2Kkbp92mBAHR1PKBzXPRx3HURh9RHmlz2MTzUQsF0X7rJBCh1VzWgyAszFOXQ0k8uboiJKC-0ZF5CKhngqL33H2Nrl1uVROKbMKTF2ihIBzCrjO0F95Yjy5PIO0Jfo6k_WguxqydpWpHEAu8hNPLtc2kE880TTcz18f4msZTC9UBGRQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF93qEFNg8KnA1dFzlPnr_Z5EjNGswEn6c5iDFJGDSdlTl5U1JvrJn2CFO3ftIFplWnML07hraB0ORcQuMFQK6R0ClI0omrusjOhMPscmzdD-pAkzQdBs9GCnHChi_KhN7BbU6OY0qOQnLafA2M8zv4PZB2tnDviZgLOEYqA5GZeRchipD_70DwicdTuktPoitm-0X9DnUaj7NOkHgWYNSsSCIcVz9ZZeFXPMfIideiQbx16RW3nx4Bbn8ijaxumubpP64rTZBuIzCe9V1mSewpnPTBAEzFS3pnuPEJ4GqaA1lLpKpezN4s6CQa3ekqgI3E6SEn9ugUaYDSgyqLI6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
عُثر على جثة في صندوق سيارة متوقفة عند ملعب كالينتي بالمكسيك، وهو ملعب تدريب المنتخب الإيراني.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78581" target="_blank">📅 03:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78580">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇬🇧
🌟
المحكمة البريطانية تحكم بالسجن 29 عامًا على شابين كرديين من شمال العراق بعد إدانتهما باستدراج فتيات قاصرات والاعتداء عليهن جنسيًا في دونكاستر، فيما تواصل الشرطة البحث عن متهم ثالث ما زال فارًا.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78580" target="_blank">📅 02:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78579">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
أكسيوس: نتنياهو وجد نفسه خارج كواليس التفاوض ولجأ إلى الاتصال بحلفاء في واشنطن لجمع المعلومات.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/78579" target="_blank">📅 01:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
أكسيوس: منشور ترمب يوم الخميس الذي أعلن فيه التوصل إلى اتفاق مع إيران فاجأ نتنياهو.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/78578" target="_blank">📅 01:44 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
