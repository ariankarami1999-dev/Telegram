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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 19:46:32</div>
<hr>

<div class="tg-post" id="msg-78753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن استهداف دبابة ميركافا في محيط بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/naya_foriraq/78753" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOCXRWqFAJ9AMORC6VyNfZDEDdyeqWv9-9mN9FkYRYgqn3kZGGNbGSBz-gaRV3aCtTdF4O-wNNdaiqxkdXgpG4IglQ1mZDcfyI9juK1wnn5tv8eNny31rYLNX7SfM1dHGAIYQzkQBbLaMDKj0SZ4NYKmIEIeGbC7olMaUARctAA0poYUb6nWEf_zDkv3WpIBVIxM3d0Tu9WMgUIf8O7gtzM65b7tRudgCqRU1EPwpelHUgOnelPmbwjw-VGg1SAEeVIVha5708iucilHAvoIv2jy1fpSy4BDlwsiiiC9jpkQ7JE1dIE-7pRUj9iiCXI5SWPm7vUjXKs28zxzY-BFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إبراهيم عزيزي:
إن جريمة اليوم التي ارتكبها النظام الصهيوني في الضاحية تثبت مرة أخرى أن أمريكا ضعيفة وغير جديرة بالثقة، وأنها لا تملك حتى القدرة على السيطرة على هذا النظام الزائف.
الجواب مؤكد، وقد قدمته جبهة المقاومة المتحدة.</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/naya_foriraq/78752" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامب: "اتصلوا بي وقالوا لي - سيدي إسرائيل تهاجم في بيروت - قبل ساعة من موعد توقيع الاتفاق. لم أصدق أن هذا يحدث. هذا سيء جدًا".</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/naya_foriraq/78751" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامب: أطلب من إيران عدم إطلاق النار تجاه إسرائيل</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/naya_foriraq/78750" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78749">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامب: "اتصلوا بي وقالوا لي - سيدي إسرائيل تهاجم في بيروت - قبل ساعة من موعد توقيع الاتفاق. لم أصدق أن هذا يحدث. هذا سيء جدًا".</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/naya_foriraq/78749" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامب: لماذا قام بيبي بهذا الهجوم؟ حزب الله أطلقوا وأصابوا في وسط اللا مكان. لم يصب أحد. ثم عليه أن يقوم بهذا الهجوم اللعين وأيضًا في بيروت. هذا أغضبني جدًا".</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/naya_foriraq/78748" target="_blank">📅 19:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
ترامب: تحدثت مع رئيس الوزراء الإسرائيلي نتنياهو، قلت له "ماذا تفعل بحق الجحيم".</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/naya_foriraq/78747" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الإطار التنسيقي:
بيان صحفي
بسم الله الرحمن الرحيم
في الذكرى المباركة لفتوى الجهاد الكفائي، نستحضر بكل فخر واعتزاز الموقف التاريخي للشعب العراقي الذي شكّل نقطة تحول مفصلية في تاريخ العراق المعاصر، حين هبّ أبناء الوطن لتلبية نداء المرجعية الدينية العليا دفاعاً عن العراق وشعبه ومقدساته، ولحماية المنطقة والعالم من خطر الإرهاب والتطرف الذي لم يكن يستهدف العراق وحده، بل كان يهدد الأمن والاستقرار الإقليمي والدولي بأسره.
وإذ نستذكر هذه المناسبة الوطنية العظيمة، فإننا نؤكد أن الوفاء لتضحيات الشهداء يقتضي مواصلة العمل على بناء الدولة العراقية القوية ومؤسساتها الدستورية الراسخة، وترسيخ سيادة القانون، وتعزيز الأمن والاستقرار، وحصر السلاح بيد الدولة باعتباره الركيزة الأساسية لحماية الوطن وصيانة منجزاته وضمان مستقبل أبنائه.
كما نؤكد اعتزازنا بالدور الوطني الذي اداه الحشد الشعبي باعتباره مؤسسة أمنية رسمية تعمل ضمن منظومة الدولة العراقية وقوانينها النافذة، في الدفاع عن العراق ومواجهة التحديات التي تهدد أمنه واستقراره.
وفي الذكرى الثانية عشر لتأسيس الحشد الشعبي نؤكد على دعمه  وتقويته وتنظيمه وصون حقوق شهدائه وجرحاه ومجاهديه ويبقى الحشد مورد الفخر ومرتكز أساس من مرتكزات الامن القومي العراقي مع باقي صنوف قواتنا المسلحة البطلة .
الإطار التنسيقي
الدائرة الاعلامية
١٤/٠٦/٢٠٢٦</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/naya_foriraq/78746" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78745">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
ترامب:
تحدثت مع رئيس الوزراء الإسرائيلي نتنياهو، قلت له "ماذا تفعل بحق الجحيم".</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/naya_foriraq/78745" target="_blank">📅 19:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59874abc6.mp4?token=n2lgfPsr_-NXWjRGSOKfEw5plRy7MXQEG6lWJFdyctKUQyRTR23p68eQ0XKQ1EQCbl7qKn5qpc8xNKQ9dyfrI_RduRt5dxKbGaz9balJ5ZL9eGHs0XMP5-P7rU875M7tUsgSiuZEOnvuiL4S7kA_IToIVNcR2UD5V1vKphgeGj6vAHEh8bsJDuo2GhrgWX_76bDkVcvg0XfwoY_JgGQmwHeONfK5M2KcPFQlfT_oD0oUHrWj8-nZlvE5cDVHNE5Yn0z6DXD5hSayBCQn4u2SqPZLZstTpgb3PG_-GAXeRuUlut-RIU5MFLcOEXW_D5C0mZ-4HwAI03HNiHJKrenedw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59874abc6.mp4?token=n2lgfPsr_-NXWjRGSOKfEw5plRy7MXQEG6lWJFdyctKUQyRTR23p68eQ0XKQ1EQCbl7qKn5qpc8xNKQ9dyfrI_RduRt5dxKbGaz9balJ5ZL9eGHs0XMP5-P7rU875M7tUsgSiuZEOnvuiL4S7kA_IToIVNcR2UD5V1vKphgeGj6vAHEh8bsJDuo2GhrgWX_76bDkVcvg0XfwoY_JgGQmwHeONfK5M2KcPFQlfT_oD0oUHrWj8-nZlvE5cDVHNE5Yn0z6DXD5hSayBCQn4u2SqPZLZstTpgb3PG_-GAXeRuUlut-RIU5MFLcOEXW_D5C0mZ-4HwAI03HNiHJKrenedw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إطلاق رشقة صاروخية من حزب الله تدك كريات شمونة ومحيطها في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/naya_foriraq/78744" target="_blank">📅 19:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
التفاوض لا يعني التنازل عن المبادئ، ولن تخضع الجمهورية الإسلامية الإيرانية لأي نوع من الترهيب أو الضغط غير القانوني. المفاوضات ليست سوى إحدى الوسائل لضمان المصالح الوطنية. وتسعى الحكومة في الوقت نفسه إلى اتباع مسارات متعددة لتعزيز الاقتصاد وتحسين مكانة البلاد.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/naya_foriraq/78743" target="_blank">📅 19:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: الارتباك في الولايات المتحدة:  ترامب ينتقد إسرائيل التي هاجمت الضاحية  وزير حربه يثني على الرد باعتباره متزناً  وزارة الخارجية تضغط على إيران لعدم الرد</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/naya_foriraq/78742" target="_blank">📅 19:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
الارتباك في الولايات المتحدة:
ترامب ينتقد إسرائيل التي هاجمت الضاحية
وزير حربه يثني على الرد باعتباره متزناً
وزارة الخارجية تضغط على إيران لعدم الرد</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/naya_foriraq/78741" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78740">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
مدير شركة سومو النفطية:
لم تستهدف أي ناقلة تحمل النفط العراقي خلال أيام التصعيد الأمريكي الإيراني.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/naya_foriraq/78740" target="_blank">📅 19:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78739">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ae956065.mp4?token=iOnz1jj5R2gZlu0-nD_IoBBCsrH8EbPeJbc9W6DXhMt_eV29dgULmNj0QXBR66caO24-gn1RhhEc1u9azmlfg4XKq-0dvVxMdaxsuHeG9s1Wg1zOHY1w2X3Lys1qJLCrrH27ILTxAGbhtDkpw1nh8_7iujIfnkQULXEfIphDUqTX1PuTBUuS1ewjEOWiKurkmX-K69j51ys0S3BQDdhItmX3elEcrn3VKjWYyrQGNA8vVJtBneaDOudURAyOSB343Ah2NPjsokRipT8ARoGtd_90rtwYWs-rF06AUQ1V7MPaBZHDLhz8ARPoRK4bi4GICLr7cCskolBq5v2sXtq4-iWWy3U4M5ixBLMl7pAF6_IdqJUXEVFJ5UxqP0mdtA6tkUbSsIh4Trs19QiP0rCqVlWbbeeyyTtqdK8v0NeCUvpxaaHPdndmazQHc9th6pF0akET8t99JYfYRkoMGwnrPns99Y6I8ZKNvBpcSKkQ7UCJbLjC6hC10LxHSy3ybSoB3cgD3BLiFdfElcA6NnLsvGZTcoV9-7FN3HVRxXTyKvH_OpE7HM-GcZFzBgtWNDe1GBm1OzdeKaqsZiozrx1CDDrCkwAVpWFEdC3iQYyVO6VTzWJqfSLogfq4RkwyxTg2In1M9ix8sDyjWPaPvo1EW5wG4_YHFS0JSmcLQtjKnCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ae956065.mp4?token=iOnz1jj5R2gZlu0-nD_IoBBCsrH8EbPeJbc9W6DXhMt_eV29dgULmNj0QXBR66caO24-gn1RhhEc1u9azmlfg4XKq-0dvVxMdaxsuHeG9s1Wg1zOHY1w2X3Lys1qJLCrrH27ILTxAGbhtDkpw1nh8_7iujIfnkQULXEfIphDUqTX1PuTBUuS1ewjEOWiKurkmX-K69j51ys0S3BQDdhItmX3elEcrn3VKjWYyrQGNA8vVJtBneaDOudURAyOSB343Ah2NPjsokRipT8ARoGtd_90rtwYWs-rF06AUQ1V7MPaBZHDLhz8ARPoRK4bi4GICLr7cCskolBq5v2sXtq4-iWWy3U4M5ixBLMl7pAF6_IdqJUXEVFJ5UxqP0mdtA6tkUbSsIh4Trs19QiP0rCqVlWbbeeyyTtqdK8v0NeCUvpxaaHPdndmazQHc9th6pF0akET8t99JYfYRkoMGwnrPns99Y6I8ZKNvBpcSKkQ7UCJbLjC6hC10LxHSy3ybSoB3cgD3BLiFdfElcA6NnLsvGZTcoV9-7FN3HVRxXTyKvH_OpE7HM-GcZFzBgtWNDe1GBm1OzdeKaqsZiozrx1CDDrCkwAVpWFEdC3iQYyVO6VTzWJqfSLogfq4RkwyxTg2In1M9ix8sDyjWPaPvo1EW5wG4_YHFS0JSmcLQtjKnCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من يصرّ على العدوان والعبث بالأمن، فلن يجد إلا ردًّا يردعه. وإن لم ينسحب واستمرّ في غيّه، فسنمضي في تأديبه حتى يصبح خائفًا يترقّب، ويحسب لكل خطوة ألف حساب.</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/78739" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUWzaiJ1mmIGsCkvEROBxPRT6MWFbdQJ8pEQtKkWznNpDhvffT5CwPVmb2T3gcvCIGx8V1HoyXoI_bBmmeLMD2dsxeTvNlzVLpEnQmUSAGjMFInnMMt3YbIrww7w1_QLxAjNyBGsM_qBlQhPkjgl1tHpIJqQEWOt6f1uMTe6YiS4yZSwlrBP5ujLVCKj-iSJpRRP1wdzRth4xqpwX_1I01y63Bvqe55YDNECGo2o_wIP0xLJuGIDbxOD7UogiOEbxlvupKoBAg1NVS_m2uPsU_UWawA_b73iEo3EcZo4mNMs_LN7RlfOTzzi0qzxOTium4Nx8Dfi_m3a11r1RAgf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد قوة الجوفضائية في الحرس الثوري السيد مجيد الموسوي:
بسم الله الرحمن الرحيم
يا أيها الشعب الحكيم الغيور، الذي أُرسلتم لطلب دماء الإمام الشهيد، وعقدتم عهداً جديداً مع الإمام الحاضر في سبيل تحقيق المثل العليا للثورة الإسلامية، واستعادة كرامة إيران الحبيبة، تذكروا أن الطاعة ركنٌ من أركان الالتزام. فلا تتقدموا خطوةً ولا تتراجعوا خطوةً، كونوا مع وليّكم. وكما قال الإمام الخميني الجليل، رحمه الله: كونوا نصرةً لولاية الفقيه، فلا يمس وطنكم مكروه. استمعوا لأمر الولاية، وتجنبوا كل كلمةٍ تُهدد وحدتكم المقدسة.</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/78738" target="_blank">📅 19:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
‏مسؤول أميركي: استهداف إسرائيل في الضاحية محاولة واضحة لتخريب الاتفاق.</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/78737" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بمساعدة قطر وباكستان ،يحاول الأمريكيون في هذه اللحظة منع إطلاق النار من إيران إلى أراضي البلاد.</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/78736" target="_blank">📅 18:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بلديات إيلات وتل ابيب الكبرى ونتانيا وحيفا تفتح الملاجئ العامة.</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/78735" target="_blank">📅 18:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78734">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
بلديات إيلات وتل ابيب الكبرى ونتانيا وحيفا تفتح الملاجئ العامة.</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/78734" target="_blank">📅 18:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يهاجم مستوطنة عرب العرامشة بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/78733" target="_blank">📅 18:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78732">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الإسرائيلي:
قبل وقت قصير، تم رصد عدة سقوط لأهداف جوية مشبوهة في أراضي دولة إسرائيل، بالقرب من الحدود مع لبنان. الحدث قيد التحقيق.</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/78732" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزير الحرب الامريكي يتعرض للاحراج مجددا.. وزير الحرب: الرئيس ترامب هو من أجبر إيران على إبرام هذه الصفقة.  الصحفية ‏مارغريت برينان: لم نصل حتى إلى مرحلة مذكرة تفاهم!</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/naya_foriraq/78731" target="_blank">📅 18:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97f97793b.mp4?token=BG5sJK3uxngoLyIH-2vQe8U4qtzJFdL9_-ZLXw8g-8Zb4HeaUo2dinuILVnuLa4nd1_-rY4Oup8T8_H8RqRAyoV548rdhWbG0jB-RfbbAfZtVR8jAGHZCSfCUek0RaO9r7O2Ogdm8o7e8FYvZZ_KFmY08RrwvHmrVEvCwPcokhKLSkw9SvCIX97RRZY5MpIDS61pN_KGsRReTSA82xSvNgGzwfv9v1Pc1Xbdt6kDzn6a01MXA_yS1QLoasD4d830ZwhLi2cnaBR_Ny_SvQl0HBiP9Sx5Bw-qEnMvGk53jXjWCzd3rsM9q-IB4aNH9UBwjwAzsdFM1CwBabzJ2NYX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97f97793b.mp4?token=BG5sJK3uxngoLyIH-2vQe8U4qtzJFdL9_-ZLXw8g-8Zb4HeaUo2dinuILVnuLa4nd1_-rY4Oup8T8_H8RqRAyoV548rdhWbG0jB-RfbbAfZtVR8jAGHZCSfCUek0RaO9r7O2Ogdm8o7e8FYvZZ_KFmY08RrwvHmrVEvCwPcokhKLSkw9SvCIX97RRZY5MpIDS61pN_KGsRReTSA82xSvNgGzwfv9v1Pc1Xbdt6kDzn6a01MXA_yS1QLoasD4d830ZwhLi2cnaBR_Ny_SvQl0HBiP9Sx5Bw-qEnMvGk53jXjWCzd3rsM9q-IB4aNH9UBwjwAzsdFM1CwBabzJ2NYX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحفية تحرج وزير الحرب الامريكي.. وزير الحرب: لقد سيطرنا على مضيق هرمز طوال هذا الوقت  ‏الصحفية: أنت تتفاوض معهم لإعادة فتحه!</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/78730" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴‍☠️
‏
الجيش الإسرائيلي:
بعد تقييم الوضع، تقرر تغيير سياسة الدفاع لقيادة الجبهة الداخلية ابتداءً من اليوم (الأحد)، 14 يونيو 2026، الساعة 18:00 وحتى يوم الاثنين (الاثنين)، 15 يونيو 2026، الساعة 20:00.
‏وكجزء من التغييرات، تقرر السماح بالنشاط الكامل مع حد أقصى للتجمعات يصل إلى 5000 شخص في جميع مناطق البلاد باستثناء خط المواجهة.
‏في منطقة خط المواجهة - نشاط جزئي، دون تغيير في التعليمات.
‏تواصل قيادة الجبهة الداخلية إجراء تقييمات مستمرة للوضع. وفي حال حدوث أي تغييرات في السياسة الدفاعية، سيتم إطلاع الجمهور على آخر المستجدات عبر المنصات الرسمية لقيادة الجبهة الداخلية والمتحدث الرسمي باسم الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/78729" target="_blank">📅 18:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN1ixfUiPy8za-EI4cYWj7cMphU224QbKcYaizzD4jlmasIoUB0zuck_h7aTxXJtouL7CRWjWa4U5FvXeakTXssL26kG0HlYjHkq8UYmazok21Igl16Za7uE7i7v4HhQUgjMtt1Ry00EzFnhsrP_S9sJv679E-vBQBdTC29yc8BcrcvZyrJEtB2UeMltl0SbFVAvgKsbLCA-mKuAtq7DYnhw0dFJWP0OqmTcqO02_B1HwgYHdsO5mKbIyXJLuJGPL1g0uE9whTB1Azwx59pOh5nUCpJDysk60Vwme_mvkIAbTi_UMYIFPocXmPI32OVcMYEfvqPv7CbLYXPcqi5WnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
كان ينبغي ألا يقع هجوم بيروت هذا الصباح، لا سيما في يوم مميز ونحن على وشك التوصل إلى اتفاق سلام مع إيران. لإسرائيل الحق في الدفاع عن نفسها ضد التهديدات، لكن الهجوم الذي ردت عليه كان محدودًا للغاية وغير ذي أهمية، ولم يُصب أحد بأذى أو جرح أو قتلى، ولا ينبغي أن يعرقل هذه العملية المهمة. نحن على وشك التوصل إلى اتفاق من شأنه أن يحقق السلام في المنطقة، بما في ذلك لبنان، وعلى جميع الأطراف أن تقف down. يجب ألا تكون هناك هجمات أخرى من جانب إسرائيل في أي مكان في لبنان، كما يجب ألا تكون هناك هجمات أخرى من جانب أي طرف آخر، بما في ذلك حزب الله، ضد إسرائيل. قد تكون هذه بداية سلام طويل وجميل - فلنحافظ عليه! شكرًا لاهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب"</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/naya_foriraq/78728" target="_blank">📅 18:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a1ae25e1.mp4?token=TA9QM0mM-j_P3nOf6m-WsOxNslWdNe_U63GTfDKJrGMIEE6m8voJTCCReCiDTLxV8bg3xcMwq9ymGFw0NwAIJN-U9KR2jlbY7Itb7gHs31dq2aI0awFaF9Ddg9KqR30u7IMro4edaq2vOH9oqGpUO0G8cbBKjIvHD3FJBAO9h0ES9HbMUa4gUIB4WUgRngYK3NOAh_vaO1lsdnSjjgcpv8ypBwpd1Q-prYqz6qK-HKV5y6Q1jQE0Bzg87rQ2K2VluDXA-ZwjCyxtMVHdlIyLGSGVbFBSJGHX9XaVCk4nB3FKTuLDEhoGdwXgw9IqJUqAXe1Ik8GZB8oknKi0cJpRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a1ae25e1.mp4?token=TA9QM0mM-j_P3nOf6m-WsOxNslWdNe_U63GTfDKJrGMIEE6m8voJTCCReCiDTLxV8bg3xcMwq9ymGFw0NwAIJN-U9KR2jlbY7Itb7gHs31dq2aI0awFaF9Ddg9KqR30u7IMro4edaq2vOH9oqGpUO0G8cbBKjIvHD3FJBAO9h0ES9HbMUa4gUIB4WUgRngYK3NOAh_vaO1lsdnSjjgcpv8ypBwpd1Q-prYqz6qK-HKV5y6Q1jQE0Bzg87rQ2K2VluDXA-ZwjCyxtMVHdlIyLGSGVbFBSJGHX9XaVCk4nB3FKTuLDEhoGdwXgw9IqJUqAXe1Ik8GZB8oknKi0cJpRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي  وزير الحرب الأمريكي: رد إسرائيل على حزب الله اتسم بضبط نفس كبير إدراكا بأننا على وشك التوصل لاتفاق.</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/78727" target="_blank">📅 18:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78726">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الأمريكي: لا أتوقع أن تعرقل ضربات إسرائيل على الضاحية الجنوبية لبيروت الاتفاق مع إيران، إذا أرادت إيران لهذا الأمر أن يصمد فعليها كبح جماح حزب الله</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/naya_foriraq/78726" target="_blank">📅 18:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الأمريكي:
لا أتوقع أن تعرقل ضربات إسرائيل على الضاحية الجنوبية لبيروت الاتفاق مع إيران، إذا أرادت إيران لهذا الأمر أن يصمد فعليها كبح جماح حزب الله</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/naya_foriraq/78725" target="_blank">📅 18:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعلام العدو: حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/78724" target="_blank">📅 17:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اعلام العدو يقول ان
اسرائيل
تتجهز لضربات صاروخية ايرانية بدءا من بعد الساعة 6:00 مساء وربما من اليمن أيضا</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/78723" target="_blank">📅 17:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78722">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اعلام العدو:
حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/78722" target="_blank">📅 17:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دويلة الكويت تسحب الجنسية من 2193 شخصاً وعن كل من أكتسبها بالتبعية من هؤلاء الأشخاص</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78721" target="_blank">📅 17:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اعلام العدو:
تعليمات داخلية لمعظم التجمعات في شمال ووسط البلاد تجهيزات لتلقي صواريخ من إيران بالوقت القريب.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78720" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مصادر:
- يتواجد فريق قطري حاليًا في طهران، وتقوم إيران عبر هذا الفريق بنقل بنودها المطلوبة، بالإضافة إلى التفاصيل الدقيقة التي تنوي تضمينها، إلى الطرف الآخر.
- لم يتم التوصل إلى اتفاق نهائي بعد، أن مسار المفاوضات يتسم بالتقلبات، حتى لو شهدنا جولات متضاربة في عملية التفاوض، فإن الشرط الأساسي لإيران هو أن تُؤخذ جميع بنودها بعين الاعتبار بشكل كامل في نهاية المطاف".
- حتى لو تم تنفيذ جميع آراء إيران، فلن يتم توقيع أي اتفاق بشكل قاطع عند إعلان ترامب
- تجدر الإشارة إلى أن هذه التصريحات صدرت قبل الهجمات الأخيرة التي شنها الكيان الصهيوني على الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/78719" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
المتحدث باسم جيش العدو:
في أعقاب الهجوم في بيروت، يجري رئيس الأركان تقييمات مستمرة مع جميع القادة المعنيين. وفقًا لتقييمات الوضع، نستعد لاحتمال إطلاق نار باتجاه أراضي
دولة إسرائيل
في الساعات القادمة. نواصل الحفاظ على الجاهزية واليقظة لمجموعة متنوعة من السيناريوهات في الدفاع والهجوم ولن نتسامح مع إطلاق النار باتجاه أراضي
دولة إسرائيل
.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/78718" target="_blank">📅 17:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
رفع حالة التأهب في إسرائيل خشية إطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/78717" target="_blank">📅 17:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 05-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78716" target="_blank">📅 17:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴‍☠️
وزارة الخارجية الصهيونية:
النظام الايراني الذي يهددنا يكذب. حزب الله هو من هاجم إسرائيل. لن نتحمل إطلاق النار على أراضينا.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78715" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اعلام العدو عن
تقييم أمني اسرائيلي
: إيران ستطلق صواريخ من أرضها تجاه إسرائيل.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78714" target="_blank">📅 17:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
‏
أوباما عن الحرب الامريكية على ايران:
إنه تذكير بأنه في العديد من مشاكل السياسة الخارجية المختلفة، قد تبدو فكرة أنه يمكننا ببساطة استخدام الترهيب أو القصف للوصول إلى حل جذابة في بعض الأحيان.. قد تعتقد أننا تعلمنا هذا الدرس الآن، ولكن يبدو أننا نضطر إلى تعلم هذا الدرس مرة أخرى بين الحين والآخر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78713" target="_blank">📅 17:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رئيس الأركان الصهيوني:
نتابع من كثب ما يجري مع الحفاظ على أعلى درجات اليقظة والاستعداد في جميع الساحات، لبنان هو مركز الثقل الرئيسي لكننا نستعد لاحتمال تطورات في ساحات أخرى.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78712" target="_blank">📅 17:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طيران مسير من لبنان يهاجم الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78711" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
هاجمنا أهدافا تابعة لحزب الله في الضاحية الجنوبية لبيروت ولن نتسامح مع إطلاق النار علينا</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78710" target="_blank">📅 16:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يلغي مشاركته في مراسم ما يسمى بـ"اتفاق السقف" في مستوطنة كرني شمرون بمشاركة سموتريتش بسبب التطورات الامنية وخشية رد ايراني.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78709" target="_blank">📅 16:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQF24MUODfzFwvzCiCQ_FQHB8nf5e3C-PUkxXrTQxumQOq92o6YNrGQ-N48ylcMKv0v6GqAlS7WjKlljJg6LXmk-O08cCCUAFqQxIbf0k1nl2g0i8yi1Q_dSQ0tJW9whpViDlxJ_KVJfJ5R50o-bTl8F9ddbyNG9RKc2BH6F0M6Ph-komKyCxFnaH2KIO0Bl27k0u_QihiFdvM7SxXKq2u9DbM7YdXfF2VROFY_yGvxBCA2tmSbcX-j_q4LP4i_l8b2gqt3s98nXYoEg9QiyDd09QPPPRw-YP3fRD5z_vJVc-vKITMZouLMc2pG11d8_jhqSguhhuIHd0k3WT5_Eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توجيهات حكومية بإيقاف كافة المشاريع الاستثمارية الخاصة بالسكن في العراق وايقاف منح اجازات الاستثمار للمجمعات السكنية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78708" target="_blank">📅 16:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">طيران مسير من لبنان يهاجم الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78707" target="_blank">📅 16:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📰
فوكس نيوز عن دبلوماسي مشارك في المفاوضات:
هجمات بيروت اليوم تُعرقل إتمام الاتفاق. هذه محاولة إسرائيلية واضحة لتخريب اتفاق الرئيس وجر الولايات المتحدة إلى الحرب مجدداً.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78706" target="_blank">📅 16:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIsXSwPjKMDKfAL6s0t_p2_nhIhdgSV62zhXiKdFRXmjPzFtxEjSrgAAdMCleNMCwn3YVGfi1ZQU_wQPDWH_dKvZ7BK04IA-pNV5CkN_mkmJOOR0x82HDZMZiOICTRDoMHt79vqym-qQZ5RxEYGn6YuyM3c0reWWSNl1yuXnN_5xb3XdliRF40CWwgQX-3p-gyGK10ozpRPy5NUx194zNRsSmH7R04Khsskftr46unsa9DcLH-gaVCwLCMPP-3Ti_dQNKQEIq6e21tv3qgbhIrofnw5ijlXo0_hXt71PZqpj8JwmPu5macTfiDwIkbCazbwn_ktL4P5nyIl0-xinpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
أظهر العدوان الصهيوني على الضاحية مجدداً أن أمريكا إما تفتقر إلى الإرادة للوفاء بالتزاماتها أو تفتقر إلى القدرة على ذلك. لا يمكن كسب أي نقاط بمنح الكيان الضوء الأخضر.
لعبة الشرطي الطيب ضد الشرطي السيئ أصبحت قديمة.
إذا لم تكن لديك الإرادة والقدرة على الوفاء بالتزاماتك، فلا يمكن الحديث عن الاستمرار في هذا المسار.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78705" target="_blank">📅 16:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 10-06-2026 تجمع جنود وآليات جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78704" target="_blank">📅 16:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78703">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6veotxl7dB3RyP7DQgOQ9sO5g61-hf9D5Pt8zNM5eTBV46Xh-NH6Ufa6SfvbvdxHsa_PynqygysJ2XXMb5XTz8qeGfItFM5zOrg6_bhm_LHs4tMUQm-bunUcWtflrokWwmgoLl1XH7RMwBSaipe98I1YkZZSas8IQxJuO3JPOwWfUvA2G0NRduZoVNwdFOz9KO-jId-QBisEkSET-WSfl9XmB7Cm0ldUEU7NwZLx3UrCNvUJFDbmRdjzTMN0EvZ6ANW8LxTZzHbQWEummIHHGjDVlAjtZOtNBLp-HbQOiBYv6TW0shQu0eBznvgcoE6hfdaGTh0zPoIrO0rrgysLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میشه یه آمریکایی با شرف باشی،
‏میشه یه ایرانی بیشرف باشی!
‏شرافت ملیت نمیشناسه...</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78703" target="_blank">📅 15:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
🇺🇸
‏
مسؤولون إسرائيليون:
أبلغنا أميركا قبل تنفيذ ضربات الضاحية الجنوبية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78702" target="_blank">📅 15:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdY6-EF4YRAKozLJlZAtxZsF0ofOW0IaX7FL3KJ_sJ8dtX_b3YA-WVVbYyyrnjQxiaQsZEkxQDG7K9PngatSI91SI49XNxq4Z1Fol49oQBltjv-p5m8a9QfS2bo7Le2OssyYMBSXO6u7jcKaSbGDDv434O7AcczipL8XJ56K9RMz1SEkekZjVTDWsEUdzDupkN68kvofhXepY_92fDAWJMZcrmMGZb0tf7VaK1nr69hWkWfL5WE15cPpMnfhZHr1L5WRTcFRCE9i7M4DZfrAN1giSd-oQPy7PG5dVnndBVqBCFGGfJl1HOE9fQdMH0sXrqkXG3eiL8dKe8rR8HymJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا يمكن المرور على موسى الدقدوق او نعيه كمقاتل او قيادي عادي او ذكر جيفارا او اي مقاتل اممي آخر دون تذكار فارس العبوات الارتجالية ومهندس المجاميع الخاصة و كاسر هيبة الجيش البريطاني بالبصرة وتلميذ عماد مغنية وفيلسوف نظام حرب الشوارع بأزقة شوارع الداخل والگيارة وسوگ العورة ورفيق سجون الاحتلال هاشم الحاج ابو الاء و قيس الشيخ الخزعلي و عدنان الشيخ الحميداوي وموسى الدقدوق ؛ نحن ننعى باختصار فترة الزمن الجميل ولابأس ان نسير قليلا نحو دور اكرم الشيخ الكعبي بإخراج الدقدوق من اقبية بوكا نحو حادثة النادي التركماني و تحديدا بناية الحاسبة المالية في شارع فلسطين يوم خلعها اكرم كما يخلع الأسد الصغير من لبوتها .. وداعا يا دقدوق ولك منا سلاما حيدري بطعم لبيك يا ثار الله وإنا لله وإنا إليه راجعون</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78701" target="_blank">📅 15:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78700">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حزب الله يشن هجوم صاروخي على كريات شمونه شمالي الكيان</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78700" target="_blank">📅 15:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78699">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
الجبهة الداخلية الصهيونية:
رفع مستوى التأهّب إلى أعلى درجة من دون أي تغيير في التعليمات الموجّهة للجمهور حتى الآن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78699" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سوالف الگهوة
وزير الداخلية الباكستاني يتصل بالحكومة العراقية !!!!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78698" target="_blank">📅 14:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78697">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اعلام العدو:
بعد قصف الضاحية الجنوبية لبيروت ضغوط مكثفة من قطر وباكستان لوقف جولة أخرى من القتال والتي من شأنها أن تُفشل المفاوضات</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78697" target="_blank">📅 14:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78696">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-06-2026
نقطة لوجستيّة تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78696" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78695">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b7b68c3b.mp4?token=Z8JxFv7La7xwOfEjqKC-eRogPRJIOYTWDtskdBgcgUheEzW6zLpaL4XaVEH47QhRDiQ-yfSapMVTxY2SCqnejnZqCQDtWiZnyhEqLLLbqoCd2Qr7LDkFlRdOR6AhDn-atWLT-rtT2Om8q17Zf_LgFYJkH2U-GxZK9Kk0JpNSWyM8_GxzojAeb1_xPflmQsnmQCFl7lPd-kqM_QKN7oGYwbwUkmX9vv6K1Y7cc2josWgqB3gto6s_jwPcUSoL5wwp4DkJRA35Al6aKKFqhYMA5TvNyIIUEtWOFqkWVk9783MsKW5Z-9WCt-k2NauTPevNzY1_MGF97wXVxWmFzKMiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b7b68c3b.mp4?token=Z8JxFv7La7xwOfEjqKC-eRogPRJIOYTWDtskdBgcgUheEzW6zLpaL4XaVEH47QhRDiQ-yfSapMVTxY2SCqnejnZqCQDtWiZnyhEqLLLbqoCd2Qr7LDkFlRdOR6AhDn-atWLT-rtT2Om8q17Zf_LgFYJkH2U-GxZK9Kk0JpNSWyM8_GxzojAeb1_xPflmQsnmQCFl7lPd-kqM_QKN7oGYwbwUkmX9vv6K1Y7cc2josWgqB3gto6s_jwPcUSoL5wwp4DkJRA35Al6aKKFqhYMA5TvNyIIUEtWOFqkWVk9783MsKW5Z-9WCt-k2NauTPevNzY1_MGF97wXVxWmFzKMiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء عن غارات على الضاحية الجنوبية لبيروت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78695" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
في أعقاب هجوم بيروت: يستعد الجيش الإسرائيلي للتصدي لأي تهديدات من إيران</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78694" target="_blank">📅 14:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78693">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
بالنظر إلى آخر بيان صادر عن مقرّ خاتم الأنبياء المركزي بشأن اعتبار استهداف الضاحية الجنوبية لبيروت خطاً أحمر بالنسبة لإيران، يُتوقّع أن تشنّ إيران هجومًا على إسرائيل في وقت قريب.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78693" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اعلام العدو:
أهمية الحدث في لبنان، أن إيران هددت سابقا بالرد على أي هجوم إسرائيلي على بيروت.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78692" target="_blank">📅 14:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78691">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الشقة المستهدفة في الضاحية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78691" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXENSf1Vf09qxd-YEeXm6c-kLlPtA0m9hHlj79i79R5cYocxvJLZDGpqYhVTLe2fnZzZWS8N9LdQb12u51McIVF7kTKNgC6yFVKY7Sj5xD2w9UkzwEDxyVeB1tDKvPkzivmIy6n_yoB8CwcYYmOdQrrNdKAH-FKnHF2yoq0_FPC7lauTfOlicwlLpNKfCbItOJzz79UgQUFzxuMFXghqGYEp37u_PZCVTy1rDDizN0rjL3O9pXncn2e3feV2mV92kAJpQArJXvzNwQtBUwkiils27slrytZUDWyUKpWS6BqzSnToNotNdqBmnc95JlNOlCvk1rz0rHhDGxORtrQ4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مكان الغارة في الضاحية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78690" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78689">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f57c16e8.mp4?token=U3GeaKV3A6Z7HbncT8GhXr-EmH0ck85-KKltlv9b12XiDjAw5AzNlA74di6j4tyaiANqwp76mNplLpj6K1nLcOWsu2LXOdtToxWvzzh4OsHA14JO_gh_ioS8IB6NDu-4R2-F4DnGmasrJXrEUBzD1UoR1CtJwvpOEw9xgP42WUcOnI4Yf67v86u3A9QYEwwX6KZnju7mGl0JRqkyJI18q2KavQPRz8Po3fYLNQsi2Z1Ds8TP_4Fe0YQW_b7PwPVhW-I4ziimdlmebsOWmsKAPztxSe09GbvuDy8duWtrESr2JgkPV0osLSolNPc1B-ANGhxZB-OkldC68ZKbIx4RVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f57c16e8.mp4?token=U3GeaKV3A6Z7HbncT8GhXr-EmH0ck85-KKltlv9b12XiDjAw5AzNlA74di6j4tyaiANqwp76mNplLpj6K1nLcOWsu2LXOdtToxWvzzh4OsHA14JO_gh_ioS8IB6NDu-4R2-F4DnGmasrJXrEUBzD1UoR1CtJwvpOEw9xgP42WUcOnI4Yf67v86u3A9QYEwwX6KZnju7mGl0JRqkyJI18q2KavQPRz8Po3fYLNQsi2Z1Ds8TP_4Fe0YQW_b7PwPVhW-I4ziimdlmebsOWmsKAPztxSe09GbvuDy8duWtrESr2JgkPV0osLSolNPc1B-ANGhxZB-OkldC68ZKbIx4RVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من مكان الغارة في الضاحية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78689" target="_blank">📅 14:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78687">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPsbSnNbijHZ4DLscxIlyILF5UlizexIYJuL3EXaOVm1n-ubdiggFSd5c2xYR6YmfMJK5GxveTM9IpHzpO3zxc-gURpDBMkIF4sHuG-PYlOzMQ3zFkYxW3x0Q4E9BSeI-yuBdkimjgF1qcGm7nQxAZfB13vHiLEvujC4Y1x9YqmiWKpgp8TuepaNHpl4aOidTGLHWSEVKJjJgGuRnpusQ3YInl71zXSgfIlDYuCwV6M2CblrRGm7F5-Lw0gKEnM5xcIMt4LIrtKgnBXOfMUctmKh1aQJcLBhAQ1MCcjUd1vCEJ9suXYXrv91q9uG75cx-orYbWdl9CtC5vws1Zw2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZy1ybmEI6lg0JCS5F8L8sOfXpFGIobiEELDDNNbVJ_-StZdRAbbQ-Mgvf6MtkSZic69xK0Bf-mwLsYB1marSSyI7hX7IQ2t7fgxPTD2UP4ikXLnY_bMzDNcdeYB7jPKo6ZUWBRVK0Erb8hFSVj-A1J79FkyuRjX88WIrsoSfwi5td08bpb5tPHTIb3mrM3dj16QY8-iBXHZr7MggzvNYOcwQ1EiW6HXPCFCpmaGGD15KEuVOzlRmgwsRDqi7m7z7BqOf_03V74v4ptNKIv36IpN_xUhFKq1UaKqpO3F2B8rz3kjGxwmped3swb9iw9cLS09Lf4F-y2RtCHqVDJTVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴‍☠️
بيان مشترك للنتن ياهو وكاتس: يهاجم الجيش الإسرائيلي الآن أهدافا لمنظمة حزب الله في بيروت ردا على إطلاق حزب الله النار على الأراضي الإسرائيلية. لن تتسامح إسرائيل مع إطلاق النار على أراضيها</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/78687" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78686">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جيش العدو يهاجم الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78686" target="_blank">📅 14:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78685">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgQsef7EarlkDfl4aDRJz1xWo1xivIOTxRAQtQ8lmawj7TwRLTsNhiYhaoO8qFZf0LOJqY43lETtaFjJMshvGxtKtAxLdfnOCY7qTd0ZmPX0azPe0kH9lNummsLMXf_RSQYUPMBK0sZCUAn7VLVHJJM78yU1TwFh2VKyylG3mVs_SqYVTrWikXlsQNH8awySCCpbfgd8xCRmkqkodjr4ecZrJWMZPMR0qyPABMC8j_DZ4YyjGiquB39cOM7PUxGGELI1zvYw57kSEVp0oiIYoQXye5EhZktssFleEDsGRAJHIWQZkYhLJ3kN_HLqopuRxQeONbCcCNBGyKUX8wqkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء عن غارات على الضاحية الجنوبية لبيروت</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78685" target="_blank">📅 14:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انباء عن غارات على الضاحية الجنوبية لبيروت</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78684" target="_blank">📅 14:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📰
مسؤول إيراني كبير لوكالة رويترز:
في إطار مسودة مذكرة التفاهم، توافق الولايات المتحدة على الإفراج عن 25 مليار دولار من الأصول الإيرانية المجمدة، من بين أمور أخرى من خلال تحويلات مالية مباشرة، وتعاون بين دول المنطقة، وخطوط ائتمان مالية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78683" target="_blank">📅 13:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صافرات الإنذار تدوي في غلاف غزة</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78681" target="_blank">📅 13:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزارة الخارجية اللبنانية:
تقدمنا بشكوى إلى مجلس الأمن ضد إسرائيل لاستهدافها آلية عسكرية للجيش واستشهاد عسكريين ولرشها مبيدات الغليفوسات فوق قرى جنوبية حدودية.
تقدمنا بشكوى وسنواصل التفاوض المباشر معهم
😄</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78680" target="_blank">📅 13:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
مهدي محمدي، المستشار الاستراتيجي لرئيس فريق التفاوض يكشف عن تفاصيل مذكرة التفاهم الإيرانية الأمريكية
- في الخطوة الأولى، يتضمن جدول الأعمال وقفًا تامًا للعمليات العسكرية ضد إيران ولبنان، ومنع أي عمل عسكري جديد. كما يتعين على الجانب الأمريكي تقديم الضمانات اللازمة لمنع تجدد التوترات
- بناءً على الإطار الذي نوقش، سيتم الإفراج عن جزء من الأصول الإيرانية المجمدة مع بداية تنفيذ الاتفاق، وفي الوقت نفسه، ستبدأ عملية تعليق بعض القيود والعقوبات الاقتصادية للسماح بزيادة التبادلات الاقتصادية ومبيعات النفط.
- يُعدّ تسهيل حركة السفن التجارية الإيرانية وتخفيف القيود البحرية أحد المحاور الرئيسية للاتفاق. ويهدف هذا البند إلى إعادة التجارة البحرية الإيرانية إلى وضعها الطبيعي وإزالة العقبات أمام النقل الدولي.
- لا تتضمن المرحلة الأولى من الاتفاق، في النص قيد التفاوض، القضايا النووية. ووفقًا لهذا الإطار، يجب أولًا تنفيذ الالتزامات الأولية للطرف الآخر والتحقق منها، ثم تنتقل المحادثات بشأن القضايا النووية إلى المراحل التالية.
- في المرحلة النهائية، تمّ النظر في رفع العقوبات الأمريكية الأولية والثانوية، فضلًا عن توفير آليات للتعويض عن الأضرار الناجمة عن الحرب والضغوط الاقتصادية وإعادة إعمارها. ويُعتبر هذا البند من أهم مطالب إيران في عملية التفاوض.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78679" target="_blank">📅 13:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78678">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78678" target="_blank">📅 13:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 08-06-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة الناقورة جنوبيّ لبنان بمسيّرات انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78677" target="_blank">📅 13:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏴‍☠️
‏مسؤول صهيوني: لانتوقع نجاح المفاوضات لكن لا نتوقع عودة الحرب
طلبنا من واشنطن عدم تقييد عملنا العسكري في لبنان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78676" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">إعلام العدو: للمرة الثالثة هذا الصباح مسيرة إصابة هدف عسكري شمال البلاد خط المواجهة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78675" target="_blank">📅 12:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📰
وكالة فارس عن مصدر مقرب من فريق التفاوض: قرار طهران النهائي بشأن مذكرة التفاهم لا زال قيد المراجعة القانونية والسياسية والتقنية
إيران لم تعلن بعد قرارها النهائي بشأن مذكرة التفاهم المقترحة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78674" target="_blank">📅 12:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
تسلل طيران مسير من جنوب لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78673" target="_blank">📅 12:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🏴‍☠️
تسلل طيران مسير من جنوب لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78672" target="_blank">📅 12:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🤺
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية موقع بلاط المستحدث التابع لجيش العدو الإسرائيلي جنوبيّ لبنان بصاروخٍ نوعي.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78671" target="_blank">📅 11:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
🇸🇾
عملية أمنية لوزارة الداخلية العراقية في الأراضي السورية أسفرت عن إلقاء القبض على 9 تجار مخدرات وضبط 200 كيلو من المخدرات كانت معدة لتهريبها نحو العراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78670" target="_blank">📅 10:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📰
وكالة "تسنيم" الإيرانية: وفد قطري يزور مجدداً طهران للاطلاع على المستجدات المتعلقة بالعملية الدبلوماسية لإنهاء الحرب وعقد مشاورات مع المسؤولين</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78669" target="_blank">📅 10:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce906e638.mp4?token=Lw8ALdXmWIWY7vXGp1VvUV8NEg4evbaxcb2v5ETS9L4_FJUQNH52kzSyk7ZpxmSoRc1QFfE6WpIgc0peW_57tpQZhQkTSAs8CV-S62Peqd2XLhpYW0OpFHPcYbzAMF-ZhMF3Z2uD1i7YZl1uJITVQur4MguG9lsI7Zu3G8TrwK-GwbI3QEHh5CGyEWvo1S83M8qYRk583Or3fP577tpUNkGCWJVROH2xoZQWNQRZPy31U13sFhOzm8pzs5g38H_ZXnxjWiu4CdARiGdV1L-Roa90W0DrOpkkIvUH1_21PANLF3BNFumKi0ZCURVtoO_EvPWsiwQC89muYowVi3jNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce906e638.mp4?token=Lw8ALdXmWIWY7vXGp1VvUV8NEg4evbaxcb2v5ETS9L4_FJUQNH52kzSyk7ZpxmSoRc1QFfE6WpIgc0peW_57tpQZhQkTSAs8CV-S62Peqd2XLhpYW0OpFHPcYbzAMF-ZhMF3Z2uD1i7YZl1uJITVQur4MguG9lsI7Zu3G8TrwK-GwbI3QEHh5CGyEWvo1S83M8qYRk583Or3fP577tpUNkGCWJVROH2xoZQWNQRZPy31U13sFhOzm8pzs5g38H_ZXnxjWiu4CdARiGdV1L-Roa90W0DrOpkkIvUH1_21PANLF3BNFumKi0ZCURVtoO_EvPWsiwQC89muYowVi3jNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد مباشرة لحركة السفن في مضيق هرمز الذي يقع تحت سيطرة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78668" target="_blank">📅 10:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">إعلام خليجي: اجتماع افتراضي لوفدي أميركا وإيران بحضور الوسطاء من باكستان وقطر
الاجتماع الافتراضي سيشهد التوقيع على مذكرة التفاهم بحضور فانس وقاليباف</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78667" target="_blank">📅 10:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇬🇧
🔥
وزارة الدفاع البريطانية: قوات بريطانية تداهم ناقلة نفط تابعة للأسطول المظلل في القناة صباح اليوم.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78666" target="_blank">📅 09:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzjnU19cVF5bY8sYuOeGK8e2T-4mYCW_Gl4rFUAkqtg_SXs6wWzC0eSW5G6WJPTUquhGFzfoyJFnhTRANSS_o8NohyIq_f1ZkHfbBdW5J0bg2GVmqIubQQa3QzOQe79GNvCE-bB3wNFqJe8vnKIXGDb8uNuupMNfRZZ3qAJbx--326ujQHRojcIMEbVBNVosF3FTSsE8x7gs02C-0Lvt2NV5vvgWAPhYa5n1VJj3e3O3xY7bEwcQDjnFLtfvmhqOwbuCV5SM9RAYYeDgcsWoUhK_4vzIftQai9zrHXWaiXvI9z8ssuuRxCRLt2Z7e6bOn90NRHR7Tno5upgQcMj6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو: بشكل أولي السقوط في شلومي داخل مهبط طيران وقاعدة مستحدثة واشتعال النيران.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78665" target="_blank">📅 09:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78664">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: انتهاك واضح لوقف إطلاق النار.. انفجرت طائرتان مسيرتان في "الأراضي الإسرائيلية".</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78664" target="_blank">📅 09:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b72a1bd7.mp4?token=rALEZw1hz6lWC3bNOvU_V7tR3lIY6vtEHj6PQzyZxRJW8lIG-Xqoozf0HsxjMG13JOJnA40ELSppzZZFfpuOPSVHvOcW4NbKlXjfRSY17VrhFpTs4S0Nk-7P9PAxeDTP5BrEOvv4C9op8FvXZ-TQKxZql3Hyp2jyjNx6HKu21nf67bAXVmZLGUa044IIcqutGvPKyIuhFi1Tj1w5XkTNpfQLPaUuDULDa-Rm-PEqdIVwLZDdQxbXLgRJQCvc1UB_XnrOV3spKF-j1rC7YLxKkqIJuw_8_jCE73aM1fXqJl3982BTqq0eaHyl6PGAvH35S7t7vwitWqVzZj2VR2OMxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b72a1bd7.mp4?token=rALEZw1hz6lWC3bNOvU_V7tR3lIY6vtEHj6PQzyZxRJW8lIG-Xqoozf0HsxjMG13JOJnA40ELSppzZZFfpuOPSVHvOcW4NbKlXjfRSY17VrhFpTs4S0Nk-7P9PAxeDTP5BrEOvv4C9op8FvXZ-TQKxZql3Hyp2jyjNx6HKu21nf67bAXVmZLGUa044IIcqutGvPKyIuhFi1Tj1w5XkTNpfQLPaUuDULDa-Rm-PEqdIVwLZDdQxbXLgRJQCvc1UB_XnrOV3spKF-j1rC7YLxKkqIJuw_8_jCE73aM1fXqJl3982BTqq0eaHyl6PGAvH35S7t7vwitWqVzZj2VR2OMxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
تسلل طيران مسير من جنوب لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78663" target="_blank">📅 08:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
🏴‍☠️
🇺🇸
إعلام العدو: إيران هي المنتصرة الكبرى بلا منازع والولايات المتحدة و"إسرائيل" تجران أذيال الخيبة والهزيمة</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78662" target="_blank">📅 08:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏴‍☠️
تسلل طيران مسير من جنوب لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78661" target="_blank">📅 08:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚠️
🇮🇶
سقوط طائرة مسيرة مجهولة العائدية على منزل مواطن بحي الإعلام غرب العاصمة بغداد .</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/78660" target="_blank">📅 03:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚠️
🇮🇶
اشتباكات عنيفة في أطراف ناحية البشير جنوب محافظة كركوك العراقية بين عصابات داعش وقوات جهاز مكافحة الارهاب ..</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78659" target="_blank">📅 03:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgXcQ8sUvpLcL626aUMP5hRTqfsZ_WzIBi8pE2Cj1I55G8gXZyp3moKC5NePDmEH1wkKBMpo_956CQY_1SuW8-aJYmvAuhLyUfx2G2b_7Se24dF_bjIXc4bPOTMKCbZ3cG6iCcGkqEedipRHYxF807cjOlKgq0JOmogO9oI3aE8R3pjapC5VkZETe6h56x9UvOHJ9vVmuX2ci_6lFToQgJMR-X6B5s47-Dm-3m3XS75oPWRKD3m6-ClzS2Smb4-0D43ZAzd-WIj_rO7Tv5xTvm9qio-vgWKtfnUU17Zd5W3IVqTU3Ebhm60CEQjzwQN9yRvcywWSOzXclZE6jN4m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في الوقت الذي لا يملك فيه المواطن الكوردي مسكناً يؤويه، يمتلك حكامه عقارات في واشنطن.
دولة جورجيا مستأجرين مبنى في العاصمة الأمريكية واشنطن لتكون سفارتهم في أمريكا
وبحسب احد الوكالات الكوردية مبنى السفارة هي ملك ل منصور مسعود بارزاني.. ومنصور أهدى المبنى بشكل تطوعي سنه كامله مجاناً للسفارة.
عائلة البارزاني الحاكمة في إقليم كوردستان العراق تحاول بشتى الطرق تحسين صورتها وبناء علاقات دوليه لمصالحهم الشخصية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78658" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxbJbmolZDznao-g1UzLo7gZ0XVcdpDG5hhMH0VMjZeu1xb5QpQV85ehik3XtQRtS63vQVijKiI9rzWjG-127jDuM86TncHXZSjC8Sc8gEwoC71QBj-ASfhN8YyLkitY21mDtuUqJXsKzLOJRAxhnXxRrjjPCgWy7admKE55K6aoFtSS3xvRfIx4YmpbdPsMPA4ykyrSlZ7wltSMr1DW9IHPMH11_9jiDbntnwalMzb57hqByslHZG0F9Z7nQl1KDSi1Bai3dutxmUpew5942fcjG-XlXTuPZGkyu6EN0QeLNclpnXBArLNaclFOOoE3tJTKcZc0GH3IXE82-dSvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الاتصالات مصطفى سند
: قرارات جريئة خلال أسبوعين شملت إلغاء مشروع السكك، وإلغاء مشروع تطوير مطار بغداد، وسحب يد مدير الموانئ وإحالته إلى التقاعد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78657" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78656" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سماع دوي انفجارات في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/78655" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سماع دوي انفجارات في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78654" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOXp5FswvOYVjvVtgKyYfsR0nTGVHuEl-toDkuz_wGakBtGbFnuPjQcV2RnwvzheAsLRZ1L71-Dw1hlQa_Bj6hioeKuW53zTv9bGSM6wE5eVTwFjXMWuMI_uJbypdAlLLFldsi7VfmigIJ1pnkFYJ9kG_PrdVPPBNq9WVAAq71q9Rky7j3nSruxOaA7CMt_2tiBIJ8IccJa1Zq4mA4Ci7J9I7b6WiO_KQ8SjYq-_BnSEd1BDYk17F8eypJyyzyzlbJwn-YX-eVa17MLe2TWyYFk1YP9bKA0C6w9P3fpnLrjkbILnzBLPfoNH7wWu0NQcZMhS0u-ExwMrM8bSAg8ang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير الاتصالات يعلن عن توفير ٥ شاشات عملاقة لبث مباريات المنتخب الوطني العراقي في كاس العالم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/78653" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
وزارة الخارجية العراقية تنفي المزاعم بشأن تورط دبلوماسيين أو أفراد من عائلاتهم في قضية الدفاتر الامتحانية التي ضُبطت أثناء محاولة تهريبها عبر مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/78652" target="_blank">📅 23:51 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
