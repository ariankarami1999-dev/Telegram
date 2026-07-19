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
<img src="https://cdn4.telesco.pe/file/KEpbMtAUAUHx6xRkQ1PyrR0B7qORyftpajmtBDAZ0omrbrEbEJN231C-04sbKzH9SjwPqvuhtyI1Q3grPBOadhweWZKgpZUUY7GhiL_zr-yUF56K5oeNOHYCmhCBwVrElfmyyNswuvjJWfrIDW8v1myjFhKwORrLgc1x7jHg6lL6PWed0iq9p4AvmnKw4Lm-Oh6XK8T4qpoN9zYF0pWm89MiY9EPgRh48oY0JwinTSm7cVE2zUTEAlieYQSJ0ro4f742eqOOtd7O4xQxIi5zpGhiaUUZ_Skx8S5fdAMFpjVaJLIwOjjqT6wXbolZybvbRWiJXu9y4C4zSV-o7fw2gA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 08:44:01</div>
<hr>

<div class="tg-post" id="msg-84134">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية:
نفذت جولة جديدة من الضربات ضد إيران في 18 يوليو عند الساعة 11:30 مساءً بتوقيت الساحل الشرقي للولايات المتحدة (ET)، وذلك بتوجيه من القائد الأعلى للقوات المسلحة (رئيس الولايات المتحدة).
وخلال الليلة الثامنة على التوالي من الضربات الأمريكية، نجحت قوات القيادة المركزية في استهداف منشآت المراقبة الساحلية العسكرية والدفاعات الجوية الإيرانية، والقدرات البحرية، ومواقع تخزين الصواريخ والطائرات المسيّرة، وذلك في إطار مواصلة إضعاف القدرات العسكرية الإيرانية.
كما استهدفت الأصول العسكرية الأمريكية قوات تابعة للحرس الثوري الإسلامي الإيراني، والتي تقول الولايات المتحدة إنها شنت هجمات على أفراد من القوات الأمريكية في الأردن يوم 17 يوليو</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/84134" target="_blank">📅 07:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84132">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/84132" target="_blank">📅 06:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84131">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/84131" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84130">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هزة أرضية بقوة 5 ريختر تضرب محافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/84130" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84129">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عدوان أمريكي على مدينة شادكان بمحافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/84129" target="_blank">📅 06:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84128">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3d146914.mp4?token=vpRN8yTGSGE-mQENRuTy8X27vi5aXHdi05G70q6RBgLuCQKH3zJBA1wrP4Xp_SwtV-YkOlveqq1AwUG23UsiMlGmgx25UTHBFTEGGJWbO5kxKkqDmeeQfzpfmQ4yBIucYuOaQu6AcK6XcXjGrLf3eCFlRDX0FP1pkouDrgcDdHjEwUrlGsrRSIlTmAFJ_SrLk4-7oxPJw1LGrrucWQssT0BvKkIi1RntMX9Bn7cEH61vetaoh5hiIGCLsAXSt0G38HRLz_8EX3LcODaNiQ2U0NbbeTbstzIySSf5F4kELPtfaIAPH0UgZovSTqMsOvzhkrD01WxAb2oI5sf__HvLSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3d146914.mp4?token=vpRN8yTGSGE-mQENRuTy8X27vi5aXHdi05G70q6RBgLuCQKH3zJBA1wrP4Xp_SwtV-YkOlveqq1AwUG23UsiMlGmgx25UTHBFTEGGJWbO5kxKkqDmeeQfzpfmQ4yBIucYuOaQu6AcK6XcXjGrLf3eCFlRDX0FP1pkouDrgcDdHjEwUrlGsrRSIlTmAFJ_SrLk4-7oxPJw1LGrrucWQssT0BvKkIi1RntMX9Bn7cEH61vetaoh5hiIGCLsAXSt0G38HRLz_8EX3LcODaNiQ2U0NbbeTbstzIySSf5F4kELPtfaIAPH0UgZovSTqMsOvzhkrD01WxAb2oI5sf__HvLSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
ردًا على التعديات المتكررة للعدو، واستشهاد مواطنين أعزاء، والهجمات على الجسور والبنية التحتية والمناطق المدنية، استهدف الجيش الإيراني، قبل ساعات، في المرحلة السادسة عشرة من عملية "البرق"، مخزنًا للذخيرة تابع للجيش الإرهابي الأمريكي في معسكر العدي، ورادار "باتريوت" ورادار جوي تابع لهذا الجيش المتجاوز في قاعدة علي السالم في الكويت، بهجمات مكثفة من طائرات مسيرة انتحارية.
🔺
يعتبر معسكر العدي إحدى القواعد المهمة للجيش الإرهابي الأمريكي في المنطقة، ويقع على بعد 104 كيلومترات من حدود الجمهورية الإسلامية الإيرانية، وهو أحد المراكز الرئيسية لدعم وإعادة تنظيم القوات الأمريكية، وتؤثر أي إعاقة لعمل هذه القاعدة بشكل كبير على عمليات الدعم التي يقدمها الجيش في المنطقة.
🔺
كما تعتبر القاعدة الجوية "علي السالم" إحدى القواعد المهمة، وهي المركز الرئيسي للنقل الجوي وبوابة دخول القوات العسكرية إلى منطقة غرب آسيا، وتلعب دورًا محوريًا في الاستراتيجية العسكرية واللوجستية للجيش الأمريكي المتجاوز في المنطقة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/84128" target="_blank">📅 06:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84127">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هزة أرضية بقوة 5 ريختر تضرب محافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/84127" target="_blank">📅 05:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84126">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
تحذير من قائد مقر خاتم الأنبياء المركزي للعدو الأمريكي الماكر:
بسم الله الرحمن الرحيم.
🔹
على خطى القائد الشهيد للأمة وشهداء إيران الإسلامية الكرام وجبهة المقاومة، نجدد العهد مع القائد الحكيم والعبقري للثورة الإسلامية، والقائد الأعلى للقوات المسلحة، آية الله السيد علي خامنئي دام ظله العالي، بأن نضع نصب أعيننا الرسالة الصريحة والمضيئة له في الحفاظ على آمال الثورة، والوحدة المقدسة، والتلاحم الوطني في القوات المسلحة، وأن نسخر كل قدراتنا وجهودنا لتعزيز التآزر والوحدة والتكامل بين القوات المسلحة، والشعب، والمسؤولين المخلصين في القوات الثلاث، لضمان مصالح الشعب الإيراني والدفاع عن حقوق الشعب والأمن الوطني.
🔹
مع الالتزام بأوامر وتوجيهات الزعيم العالي والقائد الأقرب إلى قلوبنا، نذكر الشيطان الأكبر والعدو الجنائي والمخادع الأمريكي، بأن أي محاولة للتحرش أو التسلط أو التوسع أو العنف ستواجه برد قاطع ومدمر من قبل مقاتلينا المؤمنين والشجعان والأقوياء في القوات المسلحة، وسوف نفرض عليهم تكاليف أثقل من حروب العدوان الثانية والثالثة.
🔹
إن القوة الدفاعية لبلدنا العزيز هي من ناحية، دعامة قوية للأمن والسلام للشعب الشجاع والنبيل من الجنوب إلى الشمال، ومن الشرق إلى الغرب في أرض إيران المجيدة والواسعة، ومن ناحية أخرى، هي بيئة لخدمة ونشاط المسؤولين المخلصين في البلاد لتحقيق الرفاهية والسعادة للشعب الشريف.
🔹
إن معسكر العدو، بعد سلسلة من الهزائم في الحرب العسكرية، سعى إلى إثارة الفتن والانقسامات بين الشعب والمسؤولين، لأن هزيمة الشيطان الأكبر، أمريكا الجنائية، تعتمد على التماسك الداخلي، ومواجهة هذه المؤامرة الشيطانية التي تهدف إلى إحباط العدو أمر ضروري وواجب على الجميع.
🔹
بمساعدة الله تعالى، وعناية مولانا صاحب الزمان (عجّل الله تعالى فرجه الشريف)، وبإرشاد قائدنا العزيز، سنحافظ بكل قوتنا وإمكانياتنا على التماسك النابع من النهضة غير المسبوقة والتاريخية للشعب المخلص، في تأبين الإمام الشهيد للأمة وحرائر العالم.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84126" target="_blank">📅 05:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84125">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ed277d98.mp4?token=UUOmtc9KqfhZeCPbeDF_AvPXnqwiwtCytnK5VjuNShlgsJhpxgzXNC3qnypavLeK9hFJ_UkR40N_suHeqPDDfgiHpnR4NfZ2mYNpsgdft9Qt5cS0rw7Aq4h4h7nlI0DKFKyoAZzhimAtV5d3Bn5-hvFehUv7sDl1OinFAXpOKi7ls5Moe94wQlK7mTZnmpgKLS3sMTuTUHousikTzDrjO2_DtruD6gGyx80XZ94XubTrzalEm-hHh9Mlh0OQgs1AkonkkIC9Drw8neFdbH3OpFhktFmq65rYHIE0wcPggamQMR2sCsJhKZezzuqKI5oydzsNT2pU__5aEVHgKRtwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ed277d98.mp4?token=UUOmtc9KqfhZeCPbeDF_AvPXnqwiwtCytnK5VjuNShlgsJhpxgzXNC3qnypavLeK9hFJ_UkR40N_suHeqPDDfgiHpnR4NfZ2mYNpsgdft9Qt5cS0rw7Aq4h4h7nlI0DKFKyoAZzhimAtV5d3Bn5-hvFehUv7sDl1OinFAXpOKi7ls5Moe94wQlK7mTZnmpgKLS3sMTuTUHousikTzDrjO2_DtruD6gGyx80XZ94XubTrzalEm-hHh9Mlh0OQgs1AkonkkIC9Drw8neFdbH3OpFhktFmq65rYHIE0wcPggamQMR2sCsJhKZezzuqKI5oydzsNT2pU__5aEVHgKRtwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Kuwait , Bahrain, Jordan now</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84125" target="_blank">📅 04:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84124">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عدوان على جزيرة قشم</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84124" target="_blank">📅 04:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84123">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a872fc771.mp4?token=kOoCOkBogP1Qz3Uq5QiHJszYeZ9DQczqO5kgkU6vZYOU2y2egJf9P8eRA3-_jmJZpEaea65Ps8ICzy6B6IgrBmTYH1IvjlqUzLdiu3uJjoHlh9bkyq5QZSVzR67GKXbzM1Y01-coRIpB7DTh46pJvSYi8qadSwchkxNoT-EqMSeAmr2LIN-JEu5tAy2mD9WCPERMe8WrVJJadMYpE-buyOf_VLIX06IoDws0XA9Piaf6YYPCh4gyCqrLMaF4d1S142gTzQMYHABU-hSHWn4sDm3d8W0uOiZbi-07i_-Rgy38-KqWGjGrccuvUJ2-6RXgSpTs3jcf8woi8U3ZGtQunA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a872fc771.mp4?token=kOoCOkBogP1Qz3Uq5QiHJszYeZ9DQczqO5kgkU6vZYOU2y2egJf9P8eRA3-_jmJZpEaea65Ps8ICzy6B6IgrBmTYH1IvjlqUzLdiu3uJjoHlh9bkyq5QZSVzR67GKXbzM1Y01-coRIpB7DTh46pJvSYi8qadSwchkxNoT-EqMSeAmr2LIN-JEu5tAy2mD9WCPERMe8WrVJJadMYpE-buyOf_VLIX06IoDws0XA9Piaf6YYPCh4gyCqrLMaF4d1S142gTzQMYHABU-hSHWn4sDm3d8W0uOiZbi-07i_-Rgy38-KqWGjGrccuvUJ2-6RXgSpTs3jcf8woi8U3ZGtQunA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The peoples of the Persian Gulf today.</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/naya_foriraq/84123" target="_blank">📅 04:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84122">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سماع دوي إنفجارات في الكويت بالقرب من الحدود العراقية وأنباء عن عملية إطلاق صواريخ تجاه أراضي الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/84122" target="_blank">📅 03:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84121">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات في بندرعباس وجزيرة قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84121" target="_blank">📅 03:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84120">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الهدوء الذي يسبق العاصفة ؟!
ام اعادة ترتيب أوراق لدى الطرفين ؟!
هدنة غير معلنة تدخل بها احد الدول ؟!
الساعات القادمة توضح اكثر الوضع المقبل</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84120" target="_blank">📅 03:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84119">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374ee63a17.mp4?token=XC_YZdyikDZKL6Kv2qylpwpETPH8xlCFS7d1lvu7WeuZXfQzU9Wxl4UzmDHSq0x08WnsXQOLODeA2fkRWjQgZrA2xpE-q4gvfwdVvU2it7U0lrzUXo6YRYkZXBXtZ0QjWFWlCn9MpNQQjHSDh7BU4r1Q1rau-adk3a2SsRj0E-q6hy0Ja5tiI-85q4iSEad7vOc5cTa2IQYX9idimsELQUckuYR8c6sg9cHa-NwtvbNILmg-1l-kqCYwutOGjhcbFzpiFh2xmrThpZfLCLugdDIOkni7E8j_0nltAnErRxBeTKZ4-hlceDae5uVY-Kk_-TF7IhoJptmnzloei8gFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374ee63a17.mp4?token=XC_YZdyikDZKL6Kv2qylpwpETPH8xlCFS7d1lvu7WeuZXfQzU9Wxl4UzmDHSq0x08WnsXQOLODeA2fkRWjQgZrA2xpE-q4gvfwdVvU2it7U0lrzUXo6YRYkZXBXtZ0QjWFWlCn9MpNQQjHSDh7BU4r1Q1rau-adk3a2SsRj0E-q6hy0Ja5tiI-85q4iSEad7vOc5cTa2IQYX9idimsELQUckuYR8c6sg9cHa-NwtvbNILmg-1l-kqCYwutOGjhcbFzpiFh2xmrThpZfLCLugdDIOkni7E8j_0nltAnErRxBeTKZ4-hlceDae5uVY-Kk_-TF7IhoJptmnzloei8gFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج الوضع عن السيطرة في أعزاز بعد استنفار أبناء المدينة لصد إقتحام عناصر عصابات الجولاني الإرهابية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/84119" target="_blank">📅 03:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84118">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b8eb9b9d.mp4?token=DR2QpGzax5Ix6ndpZ2irA6OgxVbMNRSHShGRElayL93LKFT47LhFl8Mp-pnUkgJygjqHIwHAv9MCG6zDNZUpcKk_uo76-iCo7UZ4hGN56uOuU-FVpj1d2nf6odHBIL6ygMobeByJ4vU0EwNacei7qNv3I1AdzZj-BHco4hxmX75gU5nLwn_DjwKJhPmG5MJ2ET1EWfiko5hMDcYJNG9Xb8Tb9Di2ybtABLiZ03iW3Xmba3c4emVTSpVZFjKNiwnAvzweIQk3uCTAUM0mUq9O1GUy9oe40Kfjux105vU4pywJnc4w-evDl9U0AOLNzt69_7JNLfglMv5J5T5eB1b0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b8eb9b9d.mp4?token=DR2QpGzax5Ix6ndpZ2irA6OgxVbMNRSHShGRElayL93LKFT47LhFl8Mp-pnUkgJygjqHIwHAv9MCG6zDNZUpcKk_uo76-iCo7UZ4hGN56uOuU-FVpj1d2nf6odHBIL6ygMobeByJ4vU0EwNacei7qNv3I1AdzZj-BHco4hxmX75gU5nLwn_DjwKJhPmG5MJ2ET1EWfiko5hMDcYJNG9Xb8Tb9Di2ybtABLiZ03iW3Xmba3c4emVTSpVZFjKNiwnAvzweIQk3uCTAUM0mUq9O1GUy9oe40Kfjux105vU4pywJnc4w-evDl9U0AOLNzt69_7JNLfglMv5J5T5eB1b0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عجلة في منطقة كلار بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84118" target="_blank">📅 03:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84117">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">أنباء عن دوي إنفجارات جديدة في أربيل</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84117" target="_blank">📅 03:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84116">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a3a31de26.mp4?token=Xh8ac90q_QrXv_VmaBArfuSs4BMoIlKpV8Wjdp7fO0FFN3LylvNOZIbr3WfelBf95c2D2h0dH1-1FMECrLCJu3vs0gpvmTig-uDFc9ofw3Rj2MzviIVE8tGVDgCFT24K3Gx8A3q72_5KQB0Fn-5DkR93Xy8CSbo--NF9wBkvk2_caGuIYM78ezq-r5uRTxL7UQ6dQh8bgFd7frV-QMP_MYWYwO0kQd_DcgOez5iU6aVewHc15G0lGIDH4qoehpoMDCmiflemznGaFlV3-1OWQYfBA_n4a_evKm6LggrCtJe5A37kiuLNpnSxhLwU9ULuwzE7YAy-JSTto0Qn7GKXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a3a31de26.mp4?token=Xh8ac90q_QrXv_VmaBArfuSs4BMoIlKpV8Wjdp7fO0FFN3LylvNOZIbr3WfelBf95c2D2h0dH1-1FMECrLCJu3vs0gpvmTig-uDFc9ofw3Rj2MzviIVE8tGVDgCFT24K3Gx8A3q72_5KQB0Fn-5DkR93Xy8CSbo--NF9wBkvk2_caGuIYM78ezq-r5uRTxL7UQ6dQh8bgFd7frV-QMP_MYWYwO0kQd_DcgOez5iU6aVewHc15G0lGIDH4qoehpoMDCmiflemznGaFlV3-1OWQYfBA_n4a_evKm6LggrCtJe5A37kiuLNpnSxhLwU9ULuwzE7YAy-JSTto0Qn7GKXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاول مرة لم ينطلق اي صاروخ من الكويت حتى اللحظة باتجاه ايران ؟!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84116" target="_blank">📅 03:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84115">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لاول مرة لم ينطلق اي صاروخ من الكويت حتى اللحظة باتجاه ايران ؟!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84115" target="_blank">📅 03:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84114">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2aeddf6b9.mp4?token=dFbny34ySGwGfEEBFBwxQ-mhcNSj95xXK19IO0q3Rr3k3dDSXPi6oltjGQjmNbB_DoQlebdCFDktLHlezW3_cL7koFPRlClXkCGz1UD-UZO1d9O8Y9XC5brObnPlvcAS6F8DePQaHD6s0a0BRQUzm9blFxka7Ghfdu0ux_3e3_zoBh6bOn-CgPy-pvlrERtiE92FHdX6rs2WA55csRh1zu0SYor_9oTBTq0LRvSmKXiTw-sugabvJzcboQ-hxuSGp3tpRYedYoROCOvUpKXNbsVElJOWTFa74WBlwwmGF-AHGEnMBSLCcTBsuBywB7-skCgnIXVA_JiU7hJzDJkRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2aeddf6b9.mp4?token=dFbny34ySGwGfEEBFBwxQ-mhcNSj95xXK19IO0q3Rr3k3dDSXPi6oltjGQjmNbB_DoQlebdCFDktLHlezW3_cL7koFPRlClXkCGz1UD-UZO1d9O8Y9XC5brObnPlvcAS6F8DePQaHD6s0a0BRQUzm9blFxka7Ghfdu0ux_3e3_zoBh6bOn-CgPy-pvlrERtiE92FHdX6rs2WA55csRh1zu0SYor_9oTBTq0LRvSmKXiTw-sugabvJzcboQ-hxuSGp3tpRYedYoROCOvUpKXNbsVElJOWTFa74WBlwwmGF-AHGEnMBSLCcTBsuBywB7-skCgnIXVA_JiU7hJzDJkRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر لنايا   تدمير طائرة من طراز F15 E نتيجة الهجوم الإيراني على قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84114" target="_blank">📅 02:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84113">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مصدر لنايا
تدمير طائرة من طراز F15 E نتيجة الهجوم الإيراني على قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84113" target="_blank">📅 02:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84112">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇷🇺
مجددا الجيش الروسي يدك أهداف للبنديرين في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84112" target="_blank">📅 02:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84111">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مصدر إيراني: لا وجود لعدوان على محافظة أراك الإيرانية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84111" target="_blank">📅 02:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84110">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d8e8f1b2.mp4?token=M6PjloVahEU7tTVorfjeH24XMPViz-0mpQfvLP8-DY8JulMfTtpnMGcZFWIcthQVGXrJ3zJ-AoXac09SLG9cS_XfF4tUPlzpZV_ZY-RvAy1vQIxkCJFq_eqOIkYYnMSIDW-nRSR1QOcr9DfY_S6fqvRwYOk3DoGYhMMATNMP6dDW-OB0OPelEDWtDFxgd379B76AtaWz-djZvVDIHmFZNLItMSCtDwd0maVqfU7Abd8y6xVlrImbAyju0KiVb4AVTZLuQ4TpAEwrzMrdInkiDlzkAscTN9tucD1hEeeI3T0wUAtd4bAMkivOwdPfnLGhHIZCA0-lwNfUE8Cuvjryow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d8e8f1b2.mp4?token=M6PjloVahEU7tTVorfjeH24XMPViz-0mpQfvLP8-DY8JulMfTtpnMGcZFWIcthQVGXrJ3zJ-AoXac09SLG9cS_XfF4tUPlzpZV_ZY-RvAy1vQIxkCJFq_eqOIkYYnMSIDW-nRSR1QOcr9DfY_S6fqvRwYOk3DoGYhMMATNMP6dDW-OB0OPelEDWtDFxgd379B76AtaWz-djZvVDIHmFZNLItMSCtDwd0maVqfU7Abd8y6xVlrImbAyju0KiVb4AVTZLuQ4TpAEwrzMrdInkiDlzkAscTN9tucD1hEeeI3T0wUAtd4bAMkivOwdPfnLGhHIZCA0-lwNfUE8Cuvjryow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مايسمى "الجيش الوطني الكردستاني" الإرهابي يعلن عن تعرض مقراته في أربيل والسليمانية إلى هجوم واسع.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/84110" target="_blank">📅 02:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84109">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b7743d603.mp4?token=ZcFmz7oQVAh6TiIVOLmqtYHTu-Z6LI8_-lZFME6MXvwNjN3I2pgq1f968ItL8dDaAxyuIk1sZvrThwV2PteAzTNu9SnPh837nrxVKj_vxbnvQd5Y0EbupGsY95wszvByTAwR30hnBGg7pM2vPAgolAFdadyeu4KkMJbseU_1S27GgP4iduFxGhHnGZ5CR-dFvr9S7H_ogIsTS_DqYuBQw9BcA5SJkKRo8_8i7gWJJaQrZC_CepUkBUwrJl2EDmv3C0yz9FRQ_-Cf97mzeZUXXCb7_o6G9HD2QGzD7fms1YdwyfYuqCVavY87CPa5Pz5kf1cUmC5pcyi767hGHmzfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b7743d603.mp4?token=ZcFmz7oQVAh6TiIVOLmqtYHTu-Z6LI8_-lZFME6MXvwNjN3I2pgq1f968ItL8dDaAxyuIk1sZvrThwV2PteAzTNu9SnPh837nrxVKj_vxbnvQd5Y0EbupGsY95wszvByTAwR30hnBGg7pM2vPAgolAFdadyeu4KkMJbseU_1S27GgP4iduFxGhHnGZ5CR-dFvr9S7H_ogIsTS_DqYuBQw9BcA5SJkKRo8_8i7gWJJaQrZC_CepUkBUwrJl2EDmv3C0yz9FRQ_-Cf97mzeZUXXCb7_o6G9HD2QGzD7fms1YdwyfYuqCVavY87CPa5Pz5kf1cUmC5pcyi767hGHmzfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعزيزات عسكرية ضخمة تابعة لعصابات الجولاني الإرهابية تصل مدينة أعزاز في محافظة حلب السورية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84109" target="_blank">📅 02:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84108">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
🇺🇸
وول ستريت جورنال :
التقارير تعلن عن تضرر عدد من الطائرات الأمريكية، المأهولة وغير المأهولة، جراء الهجوم الإيراني على قاعدة موفق السلطي الجوية في الأردن، والذي أسفر أيضاً عن مقتل جنديين أمريكيين وإصابة آخرين. وقد تم نشر مئات من الأفراد الأمريكيين وعشرات الطائرات مؤقتاً في القاعدة لشن غارات جوية على إيران. ويعكس هذا الهجوم تركيزاً متزايداً على استهداف الأصول الجوية الأمريكية مع استمرار تصاعد حدة الصراع.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84108" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84107">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb5d1ee13.mp4?token=j0GwvjjcV_WLVn0r0LSeYw2Vdpa3a9J5t2W2w6RovYQbaOsWttR96NkOWr8Q3gidFyrXzSnzJos0KDJmE7_UobeHHfLBsyVTagHXDhZQK_TlnhLlPq1LJJshNOakvllgMjqhpSWk9Jk3KoeHNeZ0KqLx9K2kP1ugmnWI-XY8VMl2D0xcplJ1_tZu51J2ANwHQiOzwjWA8W3UTB4R8EaLeFWLB9J-2fgM-tq8L485KbB7NOB6b2_G0ZUkom9I1UEXOs9LRQPA0agvzcJHlPZSv_JiH9YtnPtbi-7J1o5OnOVOZo_jkGILo3-zzXN1WI40t8coYrQQnLXrZh7ezhXe6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb5d1ee13.mp4?token=j0GwvjjcV_WLVn0r0LSeYw2Vdpa3a9J5t2W2w6RovYQbaOsWttR96NkOWr8Q3gidFyrXzSnzJos0KDJmE7_UobeHHfLBsyVTagHXDhZQK_TlnhLlPq1LJJshNOakvllgMjqhpSWk9Jk3KoeHNeZ0KqLx9K2kP1ugmnWI-XY8VMl2D0xcplJ1_tZu51J2ANwHQiOzwjWA8W3UTB4R8EaLeFWLB9J-2fgM-tq8L485KbB7NOB6b2_G0ZUkom9I1UEXOs9LRQPA0agvzcJHlPZSv_JiH9YtnPtbi-7J1o5OnOVOZo_jkGILo3-zzXN1WI40t8coYrQQnLXrZh7ezhXe6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إتساع رقعة الإشتباكات في مدينة أعزاز بمحافظة حلب السورية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84107" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84106">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84106" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84105">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8s2ELqTulT3mfWVbFOd9hUwU_37UBOggxjZzbEGiSAK1DO-EBBKsH2e-SWXSDvn_qAX9rmj4Yjjcnz1f4BE73JdOQLDcgRcrwbJ6UvQ_Pz2Gkx_nKPnceYDAaMrnbUZk3-QgDXRbHccPJN1XywBTxIYGXS3wC93OAhbaZDyU5cL4Wscsyd4PauZ4cmfO7x8Gf4tF9afv22KzkTzXiT--6dffrHR59WlCSm4nrMMM6tpmn8jVNpK_88YUY4i3vAmZgPdZnSr5Jmm-h6y-GhFlvH4pxMf6ti0Mr08Rbbh7PhsAaKpfnzB12GWybXXFfk_y1ig5qt_pRdJa2mtwJ4Ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الدفاعات الجوية الأردنية ترفع أقصى مستويات الخطورة</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84105" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84104">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47edf26487.mp4?token=WV_eqILTajm3IK1MbFUdXHMDMeSyr-_3Ji9IjYxiYOqYTdOgsIb-PEhg81Rz1X57l_nYe6jLc6-VQ9ebmtvGoMMiqmEafQpuSdW_v1rpken7N-Wrk5yEkMqiDF-JQcSYTRwPpPPu2KGDy7-PMrgPlmP4aoBjA8YLjk6VknV6jD_ctrkx-mKhslPmt19eFA_YZzvq04xKwe492d13_dppfN82LL8phBn5Ymv2FsDiFStso587jF4I1A8oXZ1jyUaYy8miZqduN77QzNvtelrR41F3cmxh4bMjoaKMM7bdZfRgApjtGpPJWvohV2SgOCqW75uTi8FP06BTRTUA7Bukzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47edf26487.mp4?token=WV_eqILTajm3IK1MbFUdXHMDMeSyr-_3Ji9IjYxiYOqYTdOgsIb-PEhg81Rz1X57l_nYe6jLc6-VQ9ebmtvGoMMiqmEafQpuSdW_v1rpken7N-Wrk5yEkMqiDF-JQcSYTRwPpPPu2KGDy7-PMrgPlmP4aoBjA8YLjk6VknV6jD_ctrkx-mKhslPmt19eFA_YZzvq04xKwe492d13_dppfN82LL8phBn5Ymv2FsDiFStso587jF4I1A8oXZ1jyUaYy8miZqduN77QzNvtelrR41F3cmxh4bMjoaKMM7bdZfRgApjtGpPJWvohV2SgOCqW75uTi8FP06BTRTUA7Bukzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إتساع رقعة الإشتباكات في مدينة أعزاز بمحافظة حلب السورية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84104" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84103">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭐️
مايسمى "الجيش الوطني الكردستاني" الإرهابي يعلن عن تعرض مقراته في أربيل والسليمانية إلى هجوم واسع.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84103" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84102">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQLxhFM8oFSUoSmVuZoQGAFW7wpss8GNCQzZ5z0fACmt8u1g5haIYtg48zQDWSo-gV2haV4gzchvmigNYlTYFEykCHMC1ZsMfb6zE58PNh-Dt00WOskf6ceCwnSPWk0HPvnUXBp3Y-qMZGpPl55OpB7NAdZ7iDAYEea-KQkgYZTWq5EpEtupSKKLqzoXmzPep5EuJgUrtdeebIzVp-ZlHo1qnWW4Zitw1KpCEzfUpLV3g7T5tJnx2h2dbOLwdNp313aKo67KTte5t8HeM2Vga57joMejavyxq4_-kqH32X9zrQhr7YN-BnqSY8iG9UlsM0FZC2t6gROJp4kjr3j2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواطنة كويتية تطالب بالعطلة وتعطيل الدوام بسبب صفارات الإنذار نتيجة العدوان الإيراني القققاشم .</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84102" target="_blank">📅 02:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84101">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات ضخمة في العاصمة الأوكرانية كييف</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84101" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84100">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سماع دوي انفجار مجهول في محافظة الموصل شمالي العراق</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84100" target="_blank">📅 02:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9c455424.mp4?token=RC62oEL5YXceBdJWyfdMOHpp5B6J3QTaLUv67R2fIxHSSsVlcY2A8YQQR_W6FAsZsNGAkZLHT4TGWkGzPuiz869ze0JEXt7nVIFomy4RjteJ3MVHKYMXXjD9GiSn47vg2vveifzb1cdk-jg73M-z37gh_hkmy32vYsnpjeYKaiQ49yxNo0D-JjnXkmgNHDGBvYxD7RitG5T1Qlai6EATUoqhr8JgMwHBK4bwa9212pyLf1D3ZE3isR1_-skDYV060zWZ7uCs9-0hfjrBFyfvNwvPr1Y5EfWdzyxTQ3iX_1pFK4rigamOAZQ2I6riB-yWx4g3xXd5mS5d9baKjxhJ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9c455424.mp4?token=RC62oEL5YXceBdJWyfdMOHpp5B6J3QTaLUv67R2fIxHSSsVlcY2A8YQQR_W6FAsZsNGAkZLHT4TGWkGzPuiz869ze0JEXt7nVIFomy4RjteJ3MVHKYMXXjD9GiSn47vg2vveifzb1cdk-jg73M-z37gh_hkmy32vYsnpjeYKaiQ49yxNo0D-JjnXkmgNHDGBvYxD7RitG5T1Qlai6EATUoqhr8JgMwHBK4bwa9212pyLf1D3ZE3isR1_-skDYV060zWZ7uCs9-0hfjrBFyfvNwvPr1Y5EfWdzyxTQ3iX_1pFK4rigamOAZQ2I6riB-yWx4g3xXd5mS5d9baKjxhJ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالتزامن مع الهجمات الأمريكية على ايران
التلفزيون الكويتي يشغل إشعار ترفع معنويات المواطنين امام العدوان الإيراني القاشم على الكويت " يا كويت لا تخافين يا كويت "</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84099" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e601fc632.mp4?token=hALVgyU6xG-jMhs5HhfsQ3mQ5kt0yxuC384S2glGPWpTwddZ7A9z0hnwLrrsMrCIW933ecIBOhUiRbAZF4RsDKifaU54spIQ4VZQJrDz4QFPHGNTf4Cps-kbM-_hP_6EHbA4bIbStw3epyKP77YnjMK-Z3ANbTSL1AuFmc6nCte-XxJyHGi0dgikOYD-ifNFA4UbTjMh6Wv51HKwu22Inx_Ec5Mn3T0Yq-Xe3rkCPhxYroYN3vU-6GVYtLFbO63HC93f8NpBY5MHWAYnuS-4DjzHspMHu8BUcNX6_MDRbvD8DzadKI4qGiHUl5BiQMaT6T6nhGOHn0qAgx7KlyOPpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e601fc632.mp4?token=hALVgyU6xG-jMhs5HhfsQ3mQ5kt0yxuC384S2glGPWpTwddZ7A9z0hnwLrrsMrCIW933ecIBOhUiRbAZF4RsDKifaU54spIQ4VZQJrDz4QFPHGNTf4Cps-kbM-_hP_6EHbA4bIbStw3epyKP77YnjMK-Z3ANbTSL1AuFmc6nCte-XxJyHGi0dgikOYD-ifNFA4UbTjMh6Wv51HKwu22Inx_Ec5Mn3T0Yq-Xe3rkCPhxYroYN3vU-6GVYtLFbO63HC93f8NpBY5MHWAYnuS-4DjzHspMHu8BUcNX6_MDRbvD8DzadKI4qGiHUl5BiQMaT6T6nhGOHn0qAgx7KlyOPpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطيران المسير الانتحاري يطال مقرات الانفصاليين في محافظة دهوك شمالي العراق</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84097" target="_blank">📅 02:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">طيران حربي أمريكي يحلق بكثافة في سماء البحرين</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84096" target="_blank">📅 02:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726e103f3f.mp4?token=YlnHUzkMDehLSaUQev7IM2to-bPMTND-p1pFaW-fz9i_kTybD5U-HxzUnpkngc1DaQk3WZ49nhaZN8WPhrNVrHPwklv6uZbwsyxHo3D_JGugnYFTFiWZuZvJl8qpwx0CbBo4sKC3Xe1j8eXosLo1J5r6E-buvFV-y5BbBdEbFrAYcrEPlKTRzAYxokumwLKecQAUCzcblM_A49_m4tE77Rgou_O3SK9c0Gfand7DMnKvPx3jiw-caQPe68VpiWueH-YRplexMGV83eYqA60xwiXkK7osfH9s3Icr-WisHJwt2RcMvWX7JUnzpKVZNPzcCpdy4ZR1TyVzquXPr2QKsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726e103f3f.mp4?token=YlnHUzkMDehLSaUQev7IM2to-bPMTND-p1pFaW-fz9i_kTybD5U-HxzUnpkngc1DaQk3WZ49nhaZN8WPhrNVrHPwklv6uZbwsyxHo3D_JGugnYFTFiWZuZvJl8qpwx0CbBo4sKC3Xe1j8eXosLo1J5r6E-buvFV-y5BbBdEbFrAYcrEPlKTRzAYxokumwLKecQAUCzcblM_A49_m4tE77Rgou_O3SK9c0Gfand7DMnKvPx3jiw-caQPe68VpiWueH-YRplexMGV83eYqA60xwiXkK7osfH9s3Icr-WisHJwt2RcMvWX7JUnzpKVZNPzcCpdy4ZR1TyVzquXPr2QKsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطيران المسير الانتحاري يطال مقرات الانفصاليين في محافظة دهوك شمالي العراق</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84095" target="_blank">📅 02:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84093">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تصد هجوم على مدينة هرمزعان</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84093" target="_blank">📅 02:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84092">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fcffa621b.mp4?token=c1txCLtZg2RI7GR42XQ-Y6g6_19VKRRUSheL-GHY1w9lZ_wV3HceOQIWO4PIuN5-9MBPogZe0qV2D5p9i0HeyniOlK8oWM4M0AnFgL7Pat9-KajErfXKrLlGPRJvqdWGG79yxrdLtOTkM1_pYYKNE2qzhIJ0d6FOA8xiyzjKirKQrP8N9jFwg2S_2m08M2xpfZ_6lGGPJwprsTRVrh90dsoNiGA53pBeNHPM4ki3uVDfgXWdp3HhIZSTGveESIOc5urlKkIOHd5Jkbmr6RPZXawpXTKwDIaGGHBr0_982CwXH2pYFk6VQD5wSUUGOQIHi5nWOUIqD0re6e_3spvjFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fcffa621b.mp4?token=c1txCLtZg2RI7GR42XQ-Y6g6_19VKRRUSheL-GHY1w9lZ_wV3HceOQIWO4PIuN5-9MBPogZe0qV2D5p9i0HeyniOlK8oWM4M0AnFgL7Pat9-KajErfXKrLlGPRJvqdWGG79yxrdLtOTkM1_pYYKNE2qzhIJ0d6FOA8xiyzjKirKQrP8N9jFwg2S_2m08M2xpfZ_6lGGPJwprsTRVrh90dsoNiGA53pBeNHPM4ki3uVDfgXWdp3HhIZSTGveESIOc5urlKkIOHd5Jkbmr6RPZXawpXTKwDIaGGHBr0_982CwXH2pYFk6VQD5wSUUGOQIHi5nWOUIqD0re6e_3spvjFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجمات جديدة واستمرار تفعيل منظومة السيرام الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84092" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84091">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الجيش الأمريكي: ‏ بدأت القوات الأمريكية اليوم، في تمام الساعة السادسة مساءً بتوقيت شرق الولايات المتحدة، شنّ غارات جوية جديدة على إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الغارات إلى تقويض قدرة إيران على تهديد الملاحة التجارية في مضيق هرمز،…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84091" target="_blank">📅 02:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84088">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d2c62fd5.mp4?token=UJfSpJfLRkzdfUJ2S2AbNQ4yXFajxLQWYSO_eK0yDch9qmBTjJDR8jgJZwRjQM-FHKPApV6-2CFa6wHyUlSnbOCEnH0zv_0vwPf7Zrnbc_OOMVkWZc0f1ADokhBrwRf8GldORWVd8AdPAyfvdj7GCFfs_ztmb_7UbZISiNjsyPLCyveYfjhtc0KipaSr34lgajBuKccptXfPh-q70sxy5BpmTj0wRXCFKe61x01snsPqzHDtXRXWPsGKgFeLmSyLtUTudxuokBOw2Q-cDZumtuiBilnGoDjUY3yNfvm6jb31iO_EbeJ56BlSVtU2mvhrttPKt8j23h6VVLWPnxCGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d2c62fd5.mp4?token=UJfSpJfLRkzdfUJ2S2AbNQ4yXFajxLQWYSO_eK0yDch9qmBTjJDR8jgJZwRjQM-FHKPApV6-2CFa6wHyUlSnbOCEnH0zv_0vwPf7Zrnbc_OOMVkWZc0f1ADokhBrwRf8GldORWVd8AdPAyfvdj7GCFfs_ztmb_7UbZISiNjsyPLCyveYfjhtc0KipaSr34lgajBuKccptXfPh-q70sxy5BpmTj0wRXCFKe61x01snsPqzHDtXRXWPsGKgFeLmSyLtUTudxuokBOw2Q-cDZumtuiBilnGoDjUY3yNfvm6jb31iO_EbeJ56BlSVtU2mvhrttPKt8j23h6VVLWPnxCGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار محاولة التصدي</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84088" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84087">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5bfaab8b.mp4?token=LyscgWvWY3He7NgOm0s5iQ5DRA2xpgfXLzShkSpvC4IfjgEUGUBEwfj-1qcGz_Adv-D0M4Z4hVi-5Bp6GbmokNrnsAfFemr35CrkKu3eXWEtZXKEn0O0nlBl6vlUNHr39GroT0E563GxUAM3EfXuPw_qWoOBHOB1KIeYF3JMkqkU1TU9ztfXWYrOAiTxt9dP0M5wJaRU_FEoveYfTVRIeB2XiMD0R5op0iw40TfPJLb2P1E3gKOE46H_BrLQd0O6WMmUGaSmEeQ-asgYGj86Ca8MgX667bZ1drgvpcuNnUxwLsDX5loN3gqovdYhfiHIF2n46j4USgwccmsUjpikrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5bfaab8b.mp4?token=LyscgWvWY3He7NgOm0s5iQ5DRA2xpgfXLzShkSpvC4IfjgEUGUBEwfj-1qcGz_Adv-D0M4Z4hVi-5Bp6GbmokNrnsAfFemr35CrkKu3eXWEtZXKEn0O0nlBl6vlUNHr39GroT0E563GxUAM3EfXuPw_qWoOBHOB1KIeYF3JMkqkU1TU9ztfXWYrOAiTxt9dP0M5wJaRU_FEoveYfTVRIeB2XiMD0R5op0iw40TfPJLb2P1E3gKOE46H_BrLQd0O6WMmUGaSmEeQ-asgYGj86Ca8MgX667bZ1drgvpcuNnUxwLsDX5loN3gqovdYhfiHIF2n46j4USgwccmsUjpikrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابات مباشرة تدك مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84087" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84086">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اصابات مباشرة تدك مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/84086" target="_blank">📅 01:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84085">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الجيش الأمريكي: ‏ بدأت القوات الأمريكية اليوم، في تمام الساعة السادسة مساءً بتوقيت شرق الولايات المتحدة، شنّ غارات جوية جديدة على إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الغارات إلى تقويض قدرة إيران على تهديد الملاحة التجارية في مضيق هرمز،…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/84085" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84084">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTD3mdfa9540cLZD-jlv0jtEa6KmrQUc_50kabiQObftEoheDHn_vGl6--2OW54eNln473N9G8ns5W0F8I53rNNXwk5DOEYsqlMtjGc7RY1SLcLBSxNCwRhpxnTtl1sIAxsiedGAuZxF6C8NxWSjlswyak5fAaMh_s9ojwMIyqSZlgl0anthGyICfvdiNIJTqISqxrSy7JHT_r5NtqvNclcssY50iRoearmdG9GYrrir5QEE0oOcUtgyTNshUSoEnl3SBAF_PrZdnZQMdPVatFrUxPP6x4QgzOPpXPqOZmw8U8V7vkvZhiGtF5MYoLs-VYEYmp5xPIKVXlTJHRjlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
Trump said months ago that Iran has no radar, no communications, and basically few to no missiles and missile launchers left. What's all this panic? Just go home and relax. Trump destroyed Iran back in March.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/84084" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84083">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9fba2651.mp4?token=j18PQ9IuoPvuNjGamyDVw3dvkfM9TERBM-OaW6elfZtfR5wLEaQ_C08Bk52CDg3XR1EyT4W5DEKJbfErZ1wyMupY-tVBpmWtQOsJLAWo6YbI5yyAhOg290EDj8eBCln65w0bx0R6Ki_mii4h6XDc1aPfhy0PSWl5DiKFYcy7l7Z8qam6RqxrNEhRadB1VpYQKTyOqUijSCewMVMqePYNwXeCQK2FankNl_0L2apgnk8VCjkrpUEkJucXEoinEL22xNuYaP8FkDGj5qaBMm2GkiWop74y6VPN-wrj0jRVISUE3pRawb5vP4eb8xVqTe8FBb1AZUh3xF3CcuyiLDG0hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9fba2651.mp4?token=j18PQ9IuoPvuNjGamyDVw3dvkfM9TERBM-OaW6elfZtfR5wLEaQ_C08Bk52CDg3XR1EyT4W5DEKJbfErZ1wyMupY-tVBpmWtQOsJLAWo6YbI5yyAhOg290EDj8eBCln65w0bx0R6Ki_mii4h6XDc1aPfhy0PSWl5DiKFYcy7l7Z8qam6RqxrNEhRadB1VpYQKTyOqUijSCewMVMqePYNwXeCQK2FankNl_0L2apgnk8VCjkrpUEkJucXEoinEL22xNuYaP8FkDGj5qaBMm2GkiWop74y6VPN-wrj0jRVISUE3pRawb5vP4eb8xVqTe8FBb1AZUh3xF3CcuyiLDG0hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابة مباشرة والنيران تشتعل في مرتفعات خليفان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/84083" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84082">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/84082" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84081">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8926a4c0e.mp4?token=dkRoRaDqBQ-k4UrMw4Ju6wx5ejPhC-lUgRA-YsL9XY9ULauskCGPzMzN2Pc2Q1A9o-Gfmpo703EDXYGu4bLo4f5QBr3ZfQkmL--staNovvyYwZ0BHNkYF8ffTTnQnlPCtw48AzWb-Y0KQUixuHS0_ZizRLUob4YtDw7YxDQWNWcP5pkLuchzW4PejTVHPHHpBjoG5hx23wUKudsWbCjVaI8lbgaGwFUm4SMy10rTaCl_t9zUGS087VG2rKkj9xhQpASFzgkFHEArSJA7TYT218-l-hP0Q07cj0BtiOu42RrQRCX8yKW7Ie-PsLg9ORGwZfQcVl4lXLetS-s6apcKJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8926a4c0e.mp4?token=dkRoRaDqBQ-k4UrMw4Ju6wx5ejPhC-lUgRA-YsL9XY9ULauskCGPzMzN2Pc2Q1A9o-Gfmpo703EDXYGu4bLo4f5QBr3ZfQkmL--staNovvyYwZ0BHNkYF8ffTTnQnlPCtw48AzWb-Y0KQUixuHS0_ZizRLUob4YtDw7YxDQWNWcP5pkLuchzW4PejTVHPHHpBjoG5hx23wUKudsWbCjVaI8lbgaGwFUm4SMy10rTaCl_t9zUGS087VG2rKkj9xhQpASFzgkFHEArSJA7TYT218-l-hP0Q07cj0BtiOu42RrQRCX8yKW7Ie-PsLg9ORGwZfQcVl4lXLetS-s6apcKJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النيران ترتفع من مرتفعات خليفان</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/84081" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84080">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اصابة مباشرة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/84080" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84079">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf6625b3b.mp4?token=gMzEDzbS_S8SQmhTCSvdsuCCul_fuVxcILt2kJCmbLRuC62XkVFeqxaeX-1YHgrp68g3df0LaCQH-fAjw08f7xdJGzebVTO5X9YLk2_-43OLMSz_uncoqXt_HalmVcp6-E7I5vd7-JSUK7NLDHW6oleyB99W5UZLOR1d7HTC14M9m819BxU5ilwM8Y54s8CrdOdsgvmrqKAuztAigI9K2Vp9Wc-GcvCDenJmLTXdqRVK2iL9K4gWc8dBmKNHFUDgtNqpCdNFvbFR1iTg4anS0Pw3bpBQTshj9WI206EnJSp_cpJ_4EQ8XWi_0zomFmliRY944kIfsURCi_uPdkqBrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf6625b3b.mp4?token=gMzEDzbS_S8SQmhTCSvdsuCCul_fuVxcILt2kJCmbLRuC62XkVFeqxaeX-1YHgrp68g3df0LaCQH-fAjw08f7xdJGzebVTO5X9YLk2_-43OLMSz_uncoqXt_HalmVcp6-E7I5vd7-JSUK7NLDHW6oleyB99W5UZLOR1d7HTC14M9m819BxU5ilwM8Y54s8CrdOdsgvmrqKAuztAigI9K2Vp9Wc-GcvCDenJmLTXdqRVK2iL9K4gWc8dBmKNHFUDgtNqpCdNFvbFR1iTg4anS0Pw3bpBQTshj9WI206EnJSp_cpJ_4EQ8XWi_0zomFmliRY944kIfsURCi_uPdkqBrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مرتفعات خليفان بمحافظة اربيل شمالي العراق التي تضم قاعدة الحرير الاميركية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84079" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84078">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a68e1d05.mp4?token=WL5qC1aC9GDd9MumuXgbSkkI0o8ZPbLTISB4E3of0p0PCyjCaRhoti2Qwp0RxPIqXYyMoWmI4VN9XpD6lvggldVzAP733rYTn0m0Gwadq6C-xtDF6B1pJ2b0xXhdkdoTSsyF7ZwWZbFR1T1BVDsOAs2yXZtysLgrdLM-Rhx92yhYltfXC_3fTTYgseTVJiQ9xA5_2qmauPpx_NDwb_ugyMshWuQNP2lIrFnaF5jFDKG-IJD3ukqXcjfoHh8plC4eK_z6BfVGTW77V8p7Ciel2v2cRIFvKxQHRJ955eGp-Rogfo3H-JbDPNxeAon_5bgMTzUYuWuHs29uUybTdhcJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a68e1d05.mp4?token=WL5qC1aC9GDd9MumuXgbSkkI0o8ZPbLTISB4E3of0p0PCyjCaRhoti2Qwp0RxPIqXYyMoWmI4VN9XpD6lvggldVzAP733rYTn0m0Gwadq6C-xtDF6B1pJ2b0xXhdkdoTSsyF7ZwWZbFR1T1BVDsOAs2yXZtysLgrdLM-Rhx92yhYltfXC_3fTTYgseTVJiQ9xA5_2qmauPpx_NDwb_ugyMshWuQNP2lIrFnaF5jFDKG-IJD3ukqXcjfoHh8plC4eK_z6BfVGTW77V8p7Ciel2v2cRIFvKxQHRJ955eGp-Rogfo3H-JbDPNxeAon_5bgMTzUYuWuHs29uUybTdhcJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ ومسيرات تنقض على الاهداف المعادية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/84078" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84077">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d074ad9a.mp4?token=CXBCw3pG6LE21UPaslAw42QdkX_yPyg4TgBkc5kquAwADiwMYSQBHSOSRjRfhBh2IHuMOStHK05DWdEqhas_nvI_WG4oiEhq427i5rGjRE1qoCkTGGhf5XSZVRL2JaARW8g6UzvTzm04hvZo8Me25FqqPwSkiZiP3smUgKLVBUBKIa3yHBmassvFzygbYh-_fWNvqG1BLjJczFQHiqD2f5PIWyaHTUmSBkWBUX7UjznkDNwxff4oR1cS5vxzBOkPfK9O8mgd2w9Y3HoKkCT-NXo0AD7oNMyZoYvmGzfuiG4Fsq4FbXFZqMHfDg3dYRf6URpxsdI-02_oYVZqTaifaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d074ad9a.mp4?token=CXBCw3pG6LE21UPaslAw42QdkX_yPyg4TgBkc5kquAwADiwMYSQBHSOSRjRfhBh2IHuMOStHK05DWdEqhas_nvI_WG4oiEhq427i5rGjRE1qoCkTGGhf5XSZVRL2JaARW8g6UzvTzm04hvZo8Me25FqqPwSkiZiP3smUgKLVBUBKIa3yHBmassvFzygbYh-_fWNvqG1BLjJczFQHiqD2f5PIWyaHTUmSBkWBUX7UjznkDNwxff4oR1cS5vxzBOkPfK9O8mgd2w9Y3HoKkCT-NXo0AD7oNMyZoYvmGzfuiG4Fsq4FbXFZqMHfDg3dYRf6URpxsdI-02_oYVZqTaifaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة يشهدها اقليم كردستان العراق حيث أماكن تواجد القوات الأمريكية ومقرات إرهابيي المعارضو الكردية الإيرانية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/84077" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84076">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات تهز السليمانية مجددا</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/84076" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84075">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">استهداف مرتفعات خليفان بمحافظة اربيل شمالي العراق التي تضم قاعدة الحرير الاميركية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/84075" target="_blank">📅 01:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84074">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c486bb3616.mp4?token=THzQyyUHolfbydSMbfSn8rg48ytWnPc7nOEZaPZkwMwtZOI90iynLbH9ownJJw62BFNIlJFnzKJ4ysLE7VLAtJvvwcQKg1Z_xkjQSGN3-kYtJMHviQPPbNryP6scAPxJ1M1Mwdxe5SE7QxM1Fq55wKSbN1tTDIwQnR7TwIUzfC674Ldv35QyuZS58AgDc9ltRLtAu95phe104Op0lf78jcmkcfxozv43ImxB1HD4AJrRR-Tvtds6B5qRXMAvW6VG0OVap8RlFOi3mEFZJdSfoGW2wWwA4MyabtN1tMDyWoo9KVkFQlAqEdp3tnBSy4KvvArDAqCNchavIQpHPKVq7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c486bb3616.mp4?token=THzQyyUHolfbydSMbfSn8rg48ytWnPc7nOEZaPZkwMwtZOI90iynLbH9ownJJw62BFNIlJFnzKJ4ysLE7VLAtJvvwcQKg1Z_xkjQSGN3-kYtJMHviQPPbNryP6scAPxJ1M1Mwdxe5SE7QxM1Fq55wKSbN1tTDIwQnR7TwIUzfC674Ldv35QyuZS58AgDc9ltRLtAu95phe104Op0lf78jcmkcfxozv43ImxB1HD4AJrRR-Tvtds6B5qRXMAvW6VG0OVap8RlFOi3mEFZJdSfoGW2wWwA4MyabtN1tMDyWoo9KVkFQlAqEdp3tnBSy4KvvArDAqCNchavIQpHPKVq7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة يشهدها اقليم كردستان العراق حيث أماكن تواجد القوات الأمريكية ومقرات إرهابيي المعارضو الكردية الإيرانية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/84074" target="_blank">📅 01:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84073">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اربيل مجددا اصوات انفجارات</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/84073" target="_blank">📅 01:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الجيش الأمريكي:
‏
بدأت القوات الأمريكية اليوم، في تمام الساعة السادسة مساءً بتوقيت شرق الولايات المتحدة، شنّ غارات جوية جديدة على إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الغارات إلى تقويض قدرة إيران على تهديد الملاحة التجارية في مضيق هرمز، ومعاقبة قوات الحرس الثوري الإسلامي التي شنت هجمات على جنود أمريكيين في الأردن الليلة الماضية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84072" target="_blank">📅 01:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84071">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هجمات تطال القاعدة الجوية الأمريكية قرب مطار أربيل</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84071" target="_blank">📅 01:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84070">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اربيل مجددا اصوات انفجارات</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84070" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=cKimJqNO40-m6LSt72Zzo7slpoagHryTZre-B0R6mInnV5ArYm0fkuLxlenEdCD-hB1SxgbExoz7An_-jj6O-lBFmD39ZbpWLoP-t1q6NM2maVVHImc31tmLW0utMrnPx2D0z8PLHplORYPIv0S5eAwVWPwu-tc5qY8ZuCadAeJOCw2hZurEmJywmJlNMpsDQH01F2vK95i14fS1VXdt35BwJIPTxJuEmcqwu-Iyte3tPOdTis89RNBOVCHxbn_G2L_WdBMswYid40LKnK74O-QGU5DNFC9nWBdztHALet02Ds2xoWSuioyXRNdc30QKBw-uOWiQba0XA7l0Utzaug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=cKimJqNO40-m6LSt72Zzo7slpoagHryTZre-B0R6mInnV5ArYm0fkuLxlenEdCD-hB1SxgbExoz7An_-jj6O-lBFmD39ZbpWLoP-t1q6NM2maVVHImc31tmLW0utMrnPx2D0z8PLHplORYPIv0S5eAwVWPwu-tc5qY8ZuCadAeJOCw2hZurEmJywmJlNMpsDQH01F2vK95i14fS1VXdt35BwJIPTxJuEmcqwu-Iyte3tPOdTis89RNBOVCHxbn_G2L_WdBMswYid40LKnK74O-QGU5DNFC9nWBdztHALet02Ds2xoWSuioyXRNdc30QKBw-uOWiQba0XA7l0Utzaug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء محافظة أربيل تشتعل وسط تفعيل منظومة السيرام وهجوم إيراني واسع</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/84068" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اصوات انفجارات عنيفة في تقاطع قادر كرم بين كركوك وسليمانية</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/84067" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ef38c4d2.mp4?token=OU3RA4jToLb9NaKKMO9TCjB2dRCR9DTmTYXqDl5TUrTLT3FFEEC4sxdOAReedM-0cnJ0wMQzY5eczQGksB3XJZxEZWutZD0IHSZ9qKVlcMdKexAAbK8l-Yaiu_7T2CeG7RKhBQgars-mmlr2OJ2gShZeZftwxq56alNCVyy7EPg1Ou-29e52-pkXH9Cbl0997ACL2-6iCTlGBnLg-1sA-t95LvaA4djw5pnvOv5lr7xJ1IdIid1ASd8IWkOHyUXysYcxKdAvmG77wwG9sgILRbcrO9iR_75eTegq6N7xow4as5dl9qA8LUW21yTmu2o-WwedLGmv52DVLfDN9va96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ef38c4d2.mp4?token=OU3RA4jToLb9NaKKMO9TCjB2dRCR9DTmTYXqDl5TUrTLT3FFEEC4sxdOAReedM-0cnJ0wMQzY5eczQGksB3XJZxEZWutZD0IHSZ9qKVlcMdKexAAbK8l-Yaiu_7T2CeG7RKhBQgars-mmlr2OJ2gShZeZftwxq56alNCVyy7EPg1Ou-29e52-pkXH9Cbl0997ACL2-6iCTlGBnLg-1sA-t95LvaA4djw5pnvOv5lr7xJ1IdIid1ASd8IWkOHyUXysYcxKdAvmG77wwG9sgILRbcrO9iR_75eTegq6N7xow4as5dl9qA8LUW21yTmu2o-WwedLGmv52DVLfDN9va96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/84066" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/84065" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84062">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBF7Kphaoa11pJfwEoL1ffNnFVNoHM_YnOxZ3K1BPpmwyhZvB4HD2YldxCVz8VD0XJ6LDziPq0FK_OndDjFo2qi6Ek5Jws-Op9zpi1FTpScD5PhBqcLaTZYZ2LOnhEy9-6j1zNs_WOcnLYSpZ4jsEwXeEToneSBdAhm44yMw4Gt_YTR5raebd558qnf0AKI6mCkjHl8JVlpmeOGuMvEvFTYrp-Eh0zEoPHLlI1DFC7VGhUCcerasIWe7i5zrqrppPyOOUKobLpTQC4m-9JiR0vVzjW1C55_na5rMS_nBgqU9sCLoz0i3_q3TyMNst96D-5EbFLkYDBsn4k5ICSJzXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4197f5de8.mp4?token=CNxmkwhBbK7FRxac7PF6bV6VldRcIjoZ-UiIQzDXp55ZvYXDSA8BjegYw6zTtbUyJEz4vHLNfeFvt8Iv8yhWuU0vs0NU9hLoygG7v-zZfaahDaLDvEr6FZN_RMKli01CW4vFlZbWDFDmPqbiD5gxyycijinC3Z_vvItXBsj0tkvw6x-GIMpj0TnB2a5y0CB56L1XQibNSoKH_K2WGY7Fc3hNhZFnUmv1AARQahYnld4-FYiYcFsV133JVAtBpMLMee_tyrD_fbOujGKEDsrvmYl8-coxFY7-PyvGGLu7hLq76lXEKN7cT36_p5cNz0jtLItZ2wHBNXZt_hAC44faZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4197f5de8.mp4?token=CNxmkwhBbK7FRxac7PF6bV6VldRcIjoZ-UiIQzDXp55ZvYXDSA8BjegYw6zTtbUyJEz4vHLNfeFvt8Iv8yhWuU0vs0NU9hLoygG7v-zZfaahDaLDvEr6FZN_RMKli01CW4vFlZbWDFDmPqbiD5gxyycijinC3Z_vvItXBsj0tkvw6x-GIMpj0TnB2a5y0CB56L1XQibNSoKH_K2WGY7Fc3hNhZFnUmv1AARQahYnld4-FYiYcFsV133JVAtBpMLMee_tyrD_fbOujGKEDsrvmYl8-coxFY7-PyvGGLu7hLq76lXEKN7cT36_p5cNz0jtLItZ2wHBNXZt_hAC44faZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/84062" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84061">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اصوات انفجارات عنيفة في تقاطع قادر كرم بين كركوك وسليمانية</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/84061" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84058">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac91c700b7.mp4?token=CuziVxFnsAD3CBqsM9rcYywyz_P-xwpKKB1b7Kta1HrAW0R8c1hwqJOKVfZDLj0jypDi22GGh3mcn72gbzjLPmFJXfg72XuFe_I45XP132OO3T6CafxD5hKFxLZ0Nnuv4JTMJvGqxdEJiYf95Ohdtu0kvukbqIGTYsM_JKYbqQORBXIODg6sltAABzNInTpGmjELCjhV0_4M-688upo-pBZapEtRWuVVVC-4j35P34XFElGXBSZG_gJ3q_-bdNK77kXg9Bb2CA4D6H4IJi8HFOPpFGd7kXs7xCz94kBq3_Mr3UWBT2kF24CdPJgXlKZUZF3smWLQS2sXoRn9J2hafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac91c700b7.mp4?token=CuziVxFnsAD3CBqsM9rcYywyz_P-xwpKKB1b7Kta1HrAW0R8c1hwqJOKVfZDLj0jypDi22GGh3mcn72gbzjLPmFJXfg72XuFe_I45XP132OO3T6CafxD5hKFxLZ0Nnuv4JTMJvGqxdEJiYf95Ohdtu0kvukbqIGTYsM_JKYbqQORBXIODg6sltAABzNInTpGmjELCjhV0_4M-688upo-pBZapEtRWuVVVC-4j35P34XFElGXBSZG_gJ3q_-bdNK77kXg9Bb2CA4D6H4IJi8HFOPpFGd7kXs7xCz94kBq3_Mr3UWBT2kF24CdPJgXlKZUZF3smWLQS2sXoRn9J2hafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات هي الاعنف في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/84058" target="_blank">📅 01:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84057">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51e0d7ccf.mp4?token=Tfilmqd7sKZrhTJFw67IjBVG_IjjKHtwpWIVze1lc1KZFCCwVwqsvIM3eW491f1FLBYWkPgFCqYlrmrGy6K9vrw60KQY6nB5tgu1AU6q9zU2oU99XHI3L3ZV9aeS7LQ-W9bjz2DWivc536jcoHHsKMLNwHp9DEz4pcFRtIl17ID8SIBOJuQdjDs40RmbfCkfU6jtX_Pueb49wMK1LesFPYNtpcj5BzzsUBCbPfTAZL2w_34LQXK32IIT4qU8tksMUYscpJmwdQmpGn6tFNWPfoX5zPbQ4nnUXGaxoM6GrerJIE9G8Mssfo47gp857ML-BA7vWGBBF6xrN_ROzSMdtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51e0d7ccf.mp4?token=Tfilmqd7sKZrhTJFw67IjBVG_IjjKHtwpWIVze1lc1KZFCCwVwqsvIM3eW491f1FLBYWkPgFCqYlrmrGy6K9vrw60KQY6nB5tgu1AU6q9zU2oU99XHI3L3ZV9aeS7LQ-W9bjz2DWivc536jcoHHsKMLNwHp9DEz4pcFRtIl17ID8SIBOJuQdjDs40RmbfCkfU6jtX_Pueb49wMK1LesFPYNtpcj5BzzsUBCbPfTAZL2w_34LQXK32IIT4qU8tksMUYscpJmwdQmpGn6tFNWPfoX5zPbQ4nnUXGaxoM6GrerJIE9G8Mssfo47gp857ML-BA7vWGBBF6xrN_ROzSMdtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات هي الاعنف في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/84057" target="_blank">📅 01:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84056">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca653221e.mp4?token=XlRdMtpxvE9GlhhCi9xxtfUJH6hl_AG1qbhslEghLD7HinJhDQF0bZeL59fq0MTI1aaClaWBG69qFXYGkQ5on6UJniYJVseQdQkJ8xW7SPihxCaO-xECDWDgyKQ_GjmJUSHE9UfKfIQQLqd66LH33UbZDszz8A8fd7yRWBkQLG8CcA30Bged8xxnnmdGxmLyXXa_r4EK_NyWoRONPABAQ9uqr6NTUhmWeqwiVNtJKNwEFbfKKHsrTpLMOnTAMatcuwkKIJCsp0RnMNtEWsrcnodBHX8Mu8tZ3SFbXaa4vz4LW37ChUB_34vidZHLffZm24_hQQcuFkBPUQeTxFAHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca653221e.mp4?token=XlRdMtpxvE9GlhhCi9xxtfUJH6hl_AG1qbhslEghLD7HinJhDQF0bZeL59fq0MTI1aaClaWBG69qFXYGkQ5on6UJniYJVseQdQkJ8xW7SPihxCaO-xECDWDgyKQ_GjmJUSHE9UfKfIQQLqd66LH33UbZDszz8A8fd7yRWBkQLG8CcA30Bged8xxnnmdGxmLyXXa_r4EK_NyWoRONPABAQ9uqr6NTUhmWeqwiVNtJKNwEFbfKKHsrTpLMOnTAMatcuwkKIJCsp0RnMNtEWsrcnodBHX8Mu8tZ3SFbXaa4vz4LW37ChUB_34vidZHLffZm24_hQQcuFkBPUQeTxFAHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنون يوثقون عمليات مستمرة لمنظومة السيرام وسط أربيل</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/84056" target="_blank">📅 01:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84055">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa58189a6.mp4?token=qsGfmYaojkm_nEotyXHFV87aKZdPdkg--Q-CGRleZVJH0Dre9aV6lrVvLa_FHHA1e119Zya98pBgXYjc7Mw8eygm6sVckGsf8unaI4SacxknLVWtR33WWNQi4jh-_77fgp7ZswytPJhOkvpmv5jpv2Emy7zfqd3efdflqOroJVd-5ACOCfFp2Ggilv4JeLeH-oOQ9Wjhy51OhSBH8bUbt9Qz-j9IP1X5l_hB8tlXAbgYneGx-qpdMUnwTWsPotvvJl7e1JWou8cQOuJDkCX7tvEBefMUBUYACKA-VXV0RGHOzWoMqZRAzu_qxIm0JhJTySG6UWqHKCXE2jS_7x5ndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa58189a6.mp4?token=qsGfmYaojkm_nEotyXHFV87aKZdPdkg--Q-CGRleZVJH0Dre9aV6lrVvLa_FHHA1e119Zya98pBgXYjc7Mw8eygm6sVckGsf8unaI4SacxknLVWtR33WWNQi4jh-_77fgp7ZswytPJhOkvpmv5jpv2Emy7zfqd3efdflqOroJVd-5ACOCfFp2Ggilv4JeLeH-oOQ9Wjhy51OhSBH8bUbt9Qz-j9IP1X5l_hB8tlXAbgYneGx-qpdMUnwTWsPotvvJl7e1JWou8cQOuJDkCX7tvEBefMUBUYACKA-VXV0RGHOzWoMqZRAzu_qxIm0JhJTySG6UWqHKCXE2jS_7x5ndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالة من الرعب تصيب سكان محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/84055" target="_blank">📅 01:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84054">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd197e3d35.mp4?token=YW5d2fEO-gOLLhV0xkqY1gTengBk2F7HSNvzHFzhoVmicZT9PC_GpIP0Y8fNWhYHrv7WSv9CgRIUC1vN9SG48K75O5lpUoZzap_OiCMODQxoEkD-7Ydtk5Zwlk7LMp79b60ToX-cJPiypRrMbbO1aFnj88ucDZK8aUVREfGslVjqFmKKJPyzZntjLeUaQbbIFWu17iD9326GPAK0RZZrA405T54RNLYEEMHhYAmUKlPt2bGlo94jjDk8Zfd_NoNEb8mCu4J7DTzZAITj1MjycspYanEYw3ZpFecYwSXkXbnO7xLoWzregn4ZoVCinLNRQstcAYDbLhn-zQV6weBokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd197e3d35.mp4?token=YW5d2fEO-gOLLhV0xkqY1gTengBk2F7HSNvzHFzhoVmicZT9PC_GpIP0Y8fNWhYHrv7WSv9CgRIUC1vN9SG48K75O5lpUoZzap_OiCMODQxoEkD-7Ydtk5Zwlk7LMp79b60ToX-cJPiypRrMbbO1aFnj88ucDZK8aUVREfGslVjqFmKKJPyzZntjLeUaQbbIFWu17iD9326GPAK0RZZrA405T54RNLYEEMHhYAmUKlPt2bGlo94jjDk8Zfd_NoNEb8mCu4J7DTzZAITj1MjycspYanEYw3ZpFecYwSXkXbnO7xLoWzregn4ZoVCinLNRQstcAYDbLhn-zQV6weBokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدد من الأصوات نتيجة العمل العشوائي لمنظومة السيرام الأمريكية في أربيل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/84054" target="_blank">📅 01:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84053">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88f7ce6e89.mp4?token=vxix61dsBPkzUS17dIpeOZ3pgcCQFe5Tp-XqbcnFr7Pvc9Kq8kuZE8ZBOX_qtnf1T6uSR2bBhrOuMmxLJ2EuQI-ce-DHJ21OqguElf3Mx2J6HF_DMBsyCBWqvDIkz51JBYpLYPH1skYUZ03rmof4YuaTHLdAubiPNYHgeoQ5of6e3Cr0S1cPXoz74Vm_7uYBdCNInGgqg7fd1Mug6B2T9U37TKqwHnyvC9Z93BzD8aqO3Kq2DRzOJh7MUnUUwi3RUkdGOtMcgE5yAqTyJ6dvshfLEN7UWWohlCqcvMtc_eUrGw8IHKyz01CE2jhL3QLGC03tKNzT-DXS3iWdIBKiFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88f7ce6e89.mp4?token=vxix61dsBPkzUS17dIpeOZ3pgcCQFe5Tp-XqbcnFr7Pvc9Kq8kuZE8ZBOX_qtnf1T6uSR2bBhrOuMmxLJ2EuQI-ce-DHJ21OqguElf3Mx2J6HF_DMBsyCBWqvDIkz51JBYpLYPH1skYUZ03rmof4YuaTHLdAubiPNYHgeoQ5of6e3Cr0S1cPXoz74Vm_7uYBdCNInGgqg7fd1Mug6B2T9U37TKqwHnyvC9Z93BzD8aqO3Kq2DRzOJh7MUnUUwi3RUkdGOtMcgE5yAqTyJ6dvshfLEN7UWWohlCqcvMtc_eUrGw8IHKyz01CE2jhL3QLGC03tKNzT-DXS3iWdIBKiFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات جديدة في سماء أربيل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/84053" target="_blank">📅 01:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84052">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e272f194.mp4?token=S61X6z33AisFqLKBV9JWvh_lV90vzmjK7_N6Edj8dZ748XTN70fuGRN5Qrchd-ugb9lI6zte6AAvBrlG-5bms7rpkTD49jBlMTAPnXx1lfE-aQY6mBTelJizuyuPDJfi_F-1WTt722cWykxSMXUlMA7pwDMiSeVJa9b1uVoO8RXb7IepeyxPpr4bovNmdURJi45CZDUSGU0GEglTbck47lGCvxBLZv01MJc8dphzcRSo_OBhIYWzuumYaUfHZ6P0vMR-TvmUxGkr-EnkKhPE_wvoZp94Q6ob8A6T6eBeeCjgymIypWuycg9nbi9a640GTXTDVzA29KSxY79LAM-aHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e272f194.mp4?token=S61X6z33AisFqLKBV9JWvh_lV90vzmjK7_N6Edj8dZ748XTN70fuGRN5Qrchd-ugb9lI6zte6AAvBrlG-5bms7rpkTD49jBlMTAPnXx1lfE-aQY6mBTelJizuyuPDJfi_F-1WTt722cWykxSMXUlMA7pwDMiSeVJa9b1uVoO8RXb7IepeyxPpr4bovNmdURJi45CZDUSGU0GEglTbck47lGCvxBLZv01MJc8dphzcRSo_OBhIYWzuumYaUfHZ6P0vMR-TvmUxGkr-EnkKhPE_wvoZp94Q6ob8A6T6eBeeCjgymIypWuycg9nbi9a640GTXTDVzA29KSxY79LAM-aHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهود عيان يتحدثون عن هجوم غير مسبوق على عاصمة اقليم كردستان العراق</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/84052" target="_blank">📅 01:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84051">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d68492ad.mp4?token=rzIGbCiHBEc9OhQoH0ITdYDr_77morsBt6QCFwNmtgeMh-2tp59Ck5hZHYIrVjcH_fbaOcefmUJTWsxo7yq-kn1Ued63D14LRacnMUT32XrNCwQ1tYKDL2lgClZ6p9UPv6Hjo3YVGFkIfwGmguBFzbD9C3JI2hg6tfrXpFXqJBdUn5-CvUCN4O36Tae0GasEVHj1Tc2kq1eI__f4a_bPy40sNvxo8QibE0vThAlM_cihhHwj6XSID0MAvihjSDUVsPdA2d5_z8TBayzs4DlEjw9Hvo7FSD5DHxTnMsSM-J94z2aR3LD8iDjLdyih0VWglx5pZ4gAzSCx8kgLkRX8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d68492ad.mp4?token=rzIGbCiHBEc9OhQoH0ITdYDr_77morsBt6QCFwNmtgeMh-2tp59Ck5hZHYIrVjcH_fbaOcefmUJTWsxo7yq-kn1Ued63D14LRacnMUT32XrNCwQ1tYKDL2lgClZ6p9UPv6Hjo3YVGFkIfwGmguBFzbD9C3JI2hg6tfrXpFXqJBdUn5-CvUCN4O36Tae0GasEVHj1Tc2kq1eI__f4a_bPy40sNvxo8QibE0vThAlM_cihhHwj6XSID0MAvihjSDUVsPdA2d5_z8TBayzs4DlEjw9Hvo7FSD5DHxTnMsSM-J94z2aR3LD8iDjLdyih0VWglx5pZ4gAzSCx8kgLkRX8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء أربيل نتيجة هجمات إيرانية</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/84051" target="_blank">📅 01:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84050">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f6a72c3b.mp4?token=I3H6Ru_qWuTcZ_XpNY9VDxdhnZeJ3mmzvXdmL4jxrDJEfhIfaD6r9YrvDo8ovJ16DkYs8qGgr4LckypV_OKP41x3jqAV0MNmzi6cGx-RcoXp0y9gGDHt62ZW1EkvvrjY2Df9r5zDkvFTyxUembqinSUm5roiJpjiBFVw9qKhGLqlWR0YuCpGHMqbaK491iRBIpm-Lkfm6PQjTaj5XPXxBFgG-RKKltg0reGE1tczCh_8s07HGuhzSms65ngPqGjoDIWcS5IXHKp6NQ3CrAJy2EqADm_qDpggRimesg3a3CEgM-ZFm42Wa5vxt5V_xItXC-Ch7uXywcBeFegXS8SJ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f6a72c3b.mp4?token=I3H6Ru_qWuTcZ_XpNY9VDxdhnZeJ3mmzvXdmL4jxrDJEfhIfaD6r9YrvDo8ovJ16DkYs8qGgr4LckypV_OKP41x3jqAV0MNmzi6cGx-RcoXp0y9gGDHt62ZW1EkvvrjY2Df9r5zDkvFTyxUembqinSUm5roiJpjiBFVw9qKhGLqlWR0YuCpGHMqbaK491iRBIpm-Lkfm6PQjTaj5XPXxBFgG-RKKltg0reGE1tczCh_8s07HGuhzSms65ngPqGjoDIWcS5IXHKp6NQ3CrAJy2EqADm_qDpggRimesg3a3CEgM-ZFm42Wa5vxt5V_xItXC-Ch7uXywcBeFegXS8SJ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اخرى تظهر استمرار رشقات منظومة السيرام الأمريكية في أربيل</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/84050" target="_blank">📅 01:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84049">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9e66b991.mp4?token=NuOqIZ0Wv2yWLsE1g63Od0Sl8y68Gb2hph2w1jITbP4xlU7ITJNIwJsmQshraP0wxX4eTwMcszJ53MjqJ97ycHcae_hlIEQ2CNCraq4HYrGVFglmASv5D9LPGA1R2E5gx8xgw9sLWlgfY5zsWOeMberxoSA0vkfGwU5GPmwa1nnbZkZvlbojBWlbCV20aua_yjJwUuzWfrlN6jMF_elkI0FQyoq-4s9yHTqPxhZpn8jXAbxah325yBSrZPREsDwIkhsh6Lrjl907DSRZhMsE1jqWer9GaGzaKtJRPoeJlwuzeaZFsRv93ybh3unKY9BDuqP-gb793f2Rbct1ZZhJhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9e66b991.mp4?token=NuOqIZ0Wv2yWLsE1g63Od0Sl8y68Gb2hph2w1jITbP4xlU7ITJNIwJsmQshraP0wxX4eTwMcszJ53MjqJ97ycHcae_hlIEQ2CNCraq4HYrGVFglmASv5D9LPGA1R2E5gx8xgw9sLWlgfY5zsWOeMberxoSA0vkfGwU5GPmwa1nnbZkZvlbojBWlbCV20aua_yjJwUuzWfrlN6jMF_elkI0FQyoq-4s9yHTqPxhZpn8jXAbxah325yBSrZPREsDwIkhsh6Lrjl907DSRZhMsE1jqWer9GaGzaKtJRPoeJlwuzeaZFsRv93ybh3unKY9BDuqP-gb793f2Rbct1ZZhJhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات من منظومة السيرام الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/84049" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84048">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d962d086.mp4?token=Z8nSBrSbPU0uHWCWLPG8Xwu9mrtVY_8LCRS8o1Y3XvpRtHDR7Wmyno6HHc-WuRUaVwvAKmz3akpHCNdWmQOdj77OJylBjgsEyD7BLQ94oSCA_HPtkrXB57h-fDxAk4jLQUdoxXb_zIxUYPkeRG6UblIrSUSMWirAxPFJFLltUOSEiVOYU_NeSgfqySc7YuEpjZPLWLjSnCcS4awFJxO6Fh7zJYDvMzrVVEMeFzjly_TSHQw9gKcz4cgvKFCl4m-WGT6T9Cu_H9xtfiuvG98JBfGjnrsX8EH3ce-S54V-mlq7xuf_WBzrfJzlW13HAJkHOQvX7XV1h8LsId476y4Knw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d962d086.mp4?token=Z8nSBrSbPU0uHWCWLPG8Xwu9mrtVY_8LCRS8o1Y3XvpRtHDR7Wmyno6HHc-WuRUaVwvAKmz3akpHCNdWmQOdj77OJylBjgsEyD7BLQ94oSCA_HPtkrXB57h-fDxAk4jLQUdoxXb_zIxUYPkeRG6UblIrSUSMWirAxPFJFLltUOSEiVOYU_NeSgfqySc7YuEpjZPLWLjSnCcS4awFJxO6Fh7zJYDvMzrVVEMeFzjly_TSHQw9gKcz4cgvKFCl4m-WGT6T9Cu_H9xtfiuvG98JBfGjnrsX8EH3ce-S54V-mlq7xuf_WBzrfJzlW13HAJkHOQvX7XV1h8LsId476y4Knw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الأمريكية لا تتوقف عن العمل</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/84048" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c3c9c371.mp4?token=d8ALyNeTf3W0LErQ6EW13hVeWohMQzsTRcHHxZy11LDw25zekqs21YoE6UvvV2GVpo_1b2z7EbLDGWf1VPqu2tg2r1VKkq-irjcewE2Bs0H5_wJuBkTY98ZmPOoaLYEiztnvu46h_xYgr_p0PH61M6Ge-MRJ-VfKWjShLBP0sRxG5L3JlJCNVRZ6RdnrIUJ7AIEaC-gPxJvdET_-F5Qbi3uAE3BsUD1bMMVYUXDII9kSOt1dj5EnvchA485i1T-QGZizr24o6778W-FtW_K9-ALkmN0zwNCU5KWO8SBG_Lczv9oQjhq1PrujiXuPvUXvV7lbtOHP8ovsFwfTE85UfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c3c9c371.mp4?token=d8ALyNeTf3W0LErQ6EW13hVeWohMQzsTRcHHxZy11LDw25zekqs21YoE6UvvV2GVpo_1b2z7EbLDGWf1VPqu2tg2r1VKkq-irjcewE2Bs0H5_wJuBkTY98ZmPOoaLYEiztnvu46h_xYgr_p0PH61M6Ge-MRJ-VfKWjShLBP0sRxG5L3JlJCNVRZ6RdnrIUJ7AIEaC-gPxJvdET_-F5Qbi3uAE3BsUD1bMMVYUXDII9kSOt1dj5EnvchA485i1T-QGZizr24o6778W-FtW_K9-ALkmN0zwNCU5KWO8SBG_Lczv9oQjhq1PrujiXuPvUXvV7lbtOHP8ovsFwfTE85UfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تسمع من مختلف مناطق أربيل</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/84047" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84046">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cd878a2.mp4?token=ATLT48-hhzz0BG1QkYKPI4BajlmROSbjqAqRRiTAkzQH30lTfzY4JgSeo-bileG-uj_idGIwbHs97ndTIJETLKRLY-ReETfoykzeCg45MfaN5LsqPRfVAM4xlZPhVlmDaDgNA6YT6s2ITI026-KCp8Pmd-QoDzslgIOZ86wA97sluEx44powZ_NWDHMt2B0PMikPLE1K7iOEc6A1KccHquZRRw02kHhXovYNsKkOAArk_lPQPNKlBqSIvr9I9b4P9axSYe6v4-9688pWRUFYa_7a0r36Nk9s16NjlZ3ZOgUI6mihmxq2V2q3l1o6E6zJIEJZedJ3l-5t4N2JBJSF9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cd878a2.mp4?token=ATLT48-hhzz0BG1QkYKPI4BajlmROSbjqAqRRiTAkzQH30lTfzY4JgSeo-bileG-uj_idGIwbHs97ndTIJETLKRLY-ReETfoykzeCg45MfaN5LsqPRfVAM4xlZPhVlmDaDgNA6YT6s2ITI026-KCp8Pmd-QoDzslgIOZ86wA97sluEx44powZ_NWDHMt2B0PMikPLE1K7iOEc6A1KccHquZRRw02kHhXovYNsKkOAArk_lPQPNKlBqSIvr9I9b4P9axSYe6v4-9688pWRUFYa_7a0r36Nk9s16NjlZ3ZOgUI6mihmxq2V2q3l1o6E6zJIEJZedJ3l-5t4N2JBJSF9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة السيرام في سماء أربيل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/84046" target="_blank">📅 01:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84045">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c5324770.mp4?token=Kh8uB4_LlWwz7CrrptmAXsjiEe02SgA76HTTIP5XpNtktP-7Oajm-1tZi4qSaMFtSeqKej969Pd4AW1d3Q4Fm0DoMoNUIeWJBggZC5mKk3G7hkuCDNFNGUxYjmwqVQOd8n2dOH94R22_WbTOIFpFCvZo539L92XjmiU_Wx3HEPdd3saUAAH-h7pxBcDj0tYJSfEUFjZ4HThRTfu9syxK8e_uAbGhQdmADmAyIw_qguSuhdzTkSmdiD-qWeBtidS4-Mjye7RHGuEO1FGHz_3wjRFv52naElQoBJOjK6yXnMJ9vd48OBpSaHhcscj0s6xgE8LeS55jJ2u9F26pi7OObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c5324770.mp4?token=Kh8uB4_LlWwz7CrrptmAXsjiEe02SgA76HTTIP5XpNtktP-7Oajm-1tZi4qSaMFtSeqKej969Pd4AW1d3Q4Fm0DoMoNUIeWJBggZC5mKk3G7hkuCDNFNGUxYjmwqVQOd8n2dOH94R22_WbTOIFpFCvZo539L92XjmiU_Wx3HEPdd3saUAAH-h7pxBcDj0tYJSfEUFjZ4HThRTfu9syxK8e_uAbGhQdmADmAyIw_qguSuhdzTkSmdiD-qWeBtidS4-Mjye7RHGuEO1FGHz_3wjRFv52naElQoBJOjK6yXnMJ9vd48OBpSaHhcscj0s6xgE8LeS55jJ2u9F26pi7OObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة السيرام في سماء أربيل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/84045" target="_blank">📅 01:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84044">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de9926e24.mp4?token=Gzf3KlXRvlqJqwNnvnR_k6W9bidlPT80pp9O6-BU6ebGGM2cGTiSUd0BdNpKGcqJf1YoVTV3ixLIU8j3XegDFay6X8fluBXeHV6Do24dqDyhY0duPtQ8UyC-hl8xXKpAXIQhrWDDak7sbX0HoIOCoNQIuJdxcorHMpXyJqjNT_f-2gN_T4-zI87wVfV1MeR1Ctfc2aALZpfcPYNmZXe2iVm60l0n1P5I8Mk4gHBVF6NUN_hXF-I72AsJ6qddD1MANr5eqybgJEip43HXI5vLEWBksWmgp4x1FdP9kqDZyY7PFNNWjGXhB3hG6xvT63Pa2RidqsJ5Xs22UujR_i-Mwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de9926e24.mp4?token=Gzf3KlXRvlqJqwNnvnR_k6W9bidlPT80pp9O6-BU6ebGGM2cGTiSUd0BdNpKGcqJf1YoVTV3ixLIU8j3XegDFay6X8fluBXeHV6Do24dqDyhY0duPtQ8UyC-hl8xXKpAXIQhrWDDak7sbX0HoIOCoNQIuJdxcorHMpXyJqjNT_f-2gN_T4-zI87wVfV1MeR1Ctfc2aALZpfcPYNmZXe2iVm60l0n1P5I8Mk4gHBVF6NUN_hXF-I72AsJ6qddD1MANr5eqybgJEip43HXI5vLEWBksWmgp4x1FdP9kqDZyY7PFNNWjGXhB3hG6xvT63Pa2RidqsJ5Xs22UujR_i-Mwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات لاتتوقف في أربيل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/84044" target="_blank">📅 01:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84043">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0992f4548.mp4?token=E-Il7Og992a4yruG1Zb_SVt0sIJSaEggNiFADUKR0pj0MdG1VSL5VuQOEV5MVL9S2SfdZLe7VGSGDBny3TlL9slGa7BHMsHdb7Roder8zvggUXnhKyr7F7LDD9wnL3QS8O-e_gvAl3qo8Vw6GB1RLYlSIGZ3xBuztz1t4qedjiPdTHmfYEQx5qirqHByW-tPOxDJO1PhGh2Z3hwxhpU7W6ONMPVZVQCqFpDmUlZ9XUQ38xt8ztI-j34xYdZKhMSD8223laGEdcmwLhti7fu89OsJiXlldezqrz_zTKicQNOsw3XJxZtE5NbUTIJX2dtnlExhwFxJ1K5S-LcOd5pPmWjmIgjisSo7lJ5jq0pcN-CgNZHmPv1M7-8BSFOVC9KbF3eDtgyo817KwizdarOrFrw4F9HmHLVbuLGCAf6mAAF3wLKp5eGG-KSO858aGk6MvwL_cksDtG9RUWhC_OnaODpzeBaA5UGXBuA-2On44byoAAdftTqxBGO0aFFe5lXaM25R9Rfxgb9FgFJugVTXIG0ZSEF-EUcrUw417pFjSeugKzX7Yd6bWV49Xsjxh6eW2fywGgZOv-kyfvbtkJfNVXBsUzOBP7Ujy4ziPdu4a-YSy8GR3GcXO7ep1kOxm3g3QZpbP0poLk9wzxjVKgBWTi3uV0F0hNwlbCL-0iWcO14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0992f4548.mp4?token=E-Il7Og992a4yruG1Zb_SVt0sIJSaEggNiFADUKR0pj0MdG1VSL5VuQOEV5MVL9S2SfdZLe7VGSGDBny3TlL9slGa7BHMsHdb7Roder8zvggUXnhKyr7F7LDD9wnL3QS8O-e_gvAl3qo8Vw6GB1RLYlSIGZ3xBuztz1t4qedjiPdTHmfYEQx5qirqHByW-tPOxDJO1PhGh2Z3hwxhpU7W6ONMPVZVQCqFpDmUlZ9XUQ38xt8ztI-j34xYdZKhMSD8223laGEdcmwLhti7fu89OsJiXlldezqrz_zTKicQNOsw3XJxZtE5NbUTIJX2dtnlExhwFxJ1K5S-LcOd5pPmWjmIgjisSo7lJ5jq0pcN-CgNZHmPv1M7-8BSFOVC9KbF3eDtgyo817KwizdarOrFrw4F9HmHLVbuLGCAf6mAAF3wLKp5eGG-KSO858aGk6MvwL_cksDtG9RUWhC_OnaODpzeBaA5UGXBuA-2On44byoAAdftTqxBGO0aFFe5lXaM25R9Rfxgb9FgFJugVTXIG0ZSEF-EUcrUw417pFjSeugKzX7Yd6bWV49Xsjxh6eW2fywGgZOv-kyfvbtkJfNVXBsUzOBP7Ujy4ziPdu4a-YSy8GR3GcXO7ep1kOxm3g3QZpbP0poLk9wzxjVKgBWTi3uV0F0hNwlbCL-0iWcO14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الأمريكية تستخدم منظومة الافنجير للدفاع الجوي قرب شقلاوة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/84043" target="_blank">📅 01:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84042">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تفعيل منظومة الباتريوت في أربيل</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/84042" target="_blank">📅 01:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84041">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d8ee3662.mp4?token=Syf65VuIXFmUNUbBRebUjs1oouqcrtv5HYJ0ziEc6m13D7-uI8tGtaQoKSVYJhLs6EP3p1_LU0_mMuG4Eg5VnYUGleceNlJKoAFTPtMSOvP6zPFlM4INYBpslTLSCYu9QxRDwHWcGFHWWdHg6hK0JQeiwlyPjjrbqkFiiGj4XSZ4vbqEn3o62mHR_VsHHCfm5hQbtfhJp9JQWIaJCAOwwlYhAWR-6vVfffdBHdxYXrfazmndis2hX8ULa2VsqknEVvAD8pR6zc3ArZc1yxREiLA7TFpZvxJWXjjZlOL0D6HcDBc9LfVLbDooSq_yyrpyyb_COCmiIVrps-j6BJv7lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d8ee3662.mp4?token=Syf65VuIXFmUNUbBRebUjs1oouqcrtv5HYJ0ziEc6m13D7-uI8tGtaQoKSVYJhLs6EP3p1_LU0_mMuG4Eg5VnYUGleceNlJKoAFTPtMSOvP6zPFlM4INYBpslTLSCYu9QxRDwHWcGFHWWdHg6hK0JQeiwlyPjjrbqkFiiGj4XSZ4vbqEn3o62mHR_VsHHCfm5hQbtfhJp9JQWIaJCAOwwlYhAWR-6vVfffdBHdxYXrfazmndis2hX8ULa2VsqknEVvAD8pR6zc3ArZc1yxREiLA7TFpZvxJWXjjZlOL0D6HcDBc9LfVLbDooSq_yyrpyyb_COCmiIVrps-j6BJv7lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تشعل سماء أربيل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/84041" target="_blank">📅 01:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84040">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a480946d4f.mp4?token=XjOV2madpaM2vfYntxXDCi_Cl5J3aLzSZjYxaABLhV7USGthMvtKuQOZ28PY4W7I7Eqm8K95i6FWc6p0iDU_WVjeW4IV38ifFQRUq9t5DTjme9D6ZvIJGUySshQW2nt-6DBueGeg_d3wBJnJnoL8M2G70_NzYTVvS-ViJ1VeXRm9kUbrBvZhVja-Y86X7w8SexwIBdEqzG5Qmf6TZoDv9Q4Bhn_cZXU3pWDwUGEPQ3INI0MBzH5uZyUPEs_6x7B_NBkmuoc6rju5x2g_umdhZgz2VGS5AWI8yTX9CtQPZfZDhapKWiopK9wyzYl9o9D8dyRpJ5BeLEGNUur3n54REA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a480946d4f.mp4?token=XjOV2madpaM2vfYntxXDCi_Cl5J3aLzSZjYxaABLhV7USGthMvtKuQOZ28PY4W7I7Eqm8K95i6FWc6p0iDU_WVjeW4IV38ifFQRUq9t5DTjme9D6ZvIJGUySshQW2nt-6DBueGeg_d3wBJnJnoL8M2G70_NzYTVvS-ViJ1VeXRm9kUbrBvZhVja-Y86X7w8SexwIBdEqzG5Qmf6TZoDv9Q4Bhn_cZXU3pWDwUGEPQ3INI0MBzH5uZyUPEs_6x7B_NBkmuoc6rju5x2g_umdhZgz2VGS5AWI8yTX9CtQPZfZDhapKWiopK9wyzYl9o9D8dyRpJ5BeLEGNUur3n54REA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منظومة الباتريوت تحاول الاعتراض في أربيل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/84040" target="_blank">📅 01:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84039">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1dbfb7138.mp4?token=OTg9YK8-VPUNo2IQuZpBahAJHneIgLXsUD_qeqIErxSnWDbiloTu3Qs4bDTzTMj0VRaifenQZZzYarJc01THu-ZeAqwSOngWGPT_8pnizfdEUNtY_F8gSNRe7PqBifTfgO3tmtfWzyj-odGTAphV2ngYJCyiYEeZqceQgFn1zskMxCcXawu1jIiwpkSTg0iCvxttombtKEY5IpHxlcBCgyVKIXLDDbyftbC1jugbPh-yyMDQTOcgQV3PGKM7SwVQnHlpecOqVndOO8SZ6qAdbbbXes8u6TlUQ1XO37g410AvMmUj56W4h8I4kBEKh3u2veKLcDCHr1yug701BzeCjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1dbfb7138.mp4?token=OTg9YK8-VPUNo2IQuZpBahAJHneIgLXsUD_qeqIErxSnWDbiloTu3Qs4bDTzTMj0VRaifenQZZzYarJc01THu-ZeAqwSOngWGPT_8pnizfdEUNtY_F8gSNRe7PqBifTfgO3tmtfWzyj-odGTAphV2ngYJCyiYEeZqceQgFn1zskMxCcXawu1jIiwpkSTg0iCvxttombtKEY5IpHxlcBCgyVKIXLDDbyftbC1jugbPh-yyMDQTOcgQV3PGKM7SwVQnHlpecOqVndOO8SZ6qAdbbbXes8u6TlUQ1XO37g410AvMmUj56W4h8I4kBEKh3u2veKLcDCHr1yug701BzeCjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة الباتريوت في أربيل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/84039" target="_blank">📅 01:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84038">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تفعيل منظومة الباتريوت في أربيل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/84038" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84037">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الطيران المسير يستهدف القاعدة الامريكية ومقرات المعارضة في أربيل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/84037" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84036">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات عنيفة تهز أربيل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84036" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84033">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee64ee42df.mp4?token=VW806WBpoyT2rQOxQXjEGxpEBfv0UPDN8xBdQrRAQT4IHirzmoZ16rHiYl6h1AzjtfO-AY7i5T6PETolmOgYBICdxDbzMDXFQ-hdaoWoPMs9-PzmmBujvde8nYZ_e4u6ffza15BzZcpoRT2-7aDTuMeIs5FUNj4EJFjeTKfH2z7CNxem5LVGGRKoLZZkF8KUjvMulYaNDIURoqElcqD3J20NIDIGTnMMpGNn8OuYnJJrPUUzNFbFFXPWfbIvFrAP6sK2GuvNfDVTwSUZPEO4-BU7EkYlvEhkrMPimPWyBqTiIuChuPdt2ng3NAuocX08UjzzJ0WM0c8Hgn80K4nHgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee64ee42df.mp4?token=VW806WBpoyT2rQOxQXjEGxpEBfv0UPDN8xBdQrRAQT4IHirzmoZ16rHiYl6h1AzjtfO-AY7i5T6PETolmOgYBICdxDbzMDXFQ-hdaoWoPMs9-PzmmBujvde8nYZ_e4u6ffza15BzZcpoRT2-7aDTuMeIs5FUNj4EJFjeTKfH2z7CNxem5LVGGRKoLZZkF8KUjvMulYaNDIURoqElcqD3J20NIDIGTnMMpGNn8OuYnJJrPUUzNFbFFXPWfbIvFrAP6sK2GuvNfDVTwSUZPEO4-BU7EkYlvEhkrMPimPWyBqTiIuChuPdt2ng3NAuocX08UjzzJ0WM0c8Hgn80K4nHgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارك مسلحة عنيفة تشهدها شوارع مدينة أعزاز نتيجة خلافات داخلية بين عصابات الجولاني الإرهابية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/84033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84032">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات عنيفة تهز أربيل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/84032" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84031">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84031" target="_blank">📅 01:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84030">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات تهز أربيل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84030" target="_blank">📅 01:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84029">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd841dc7a.mp4?token=OtQtTWtUU7KYUEZyeQG2yk6LzbDa3hM6Mb0ciZbC51eP9M7HXrNEefKo6dz1JURHT_frodKbnMGN8URrWeJps_fW3tc2HGNf2-d9cbCg-eCUxijtB5nVoHhjtpeKxbg9Z0V4WNk12nYtJdexVcLaD9l1-YC7NVmNrMwjdxWZAPvrEzEXEfzLT8Kz29Q01xWo39UvCxO3ZD5qmcj80GxNs-rHUCBQQXkTzh7SAhP0uH2QuuukopwN1jyuG4nEXV8y2OcYir3sCNoTUU4lHNTxDaMVXwOjIUMjAr-csVdpcN9OxEV7Lqk3YsQKMwjV1aeWLgxSwABq9Rp69vU3ve7ILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd841dc7a.mp4?token=OtQtTWtUU7KYUEZyeQG2yk6LzbDa3hM6Mb0ciZbC51eP9M7HXrNEefKo6dz1JURHT_frodKbnMGN8URrWeJps_fW3tc2HGNf2-d9cbCg-eCUxijtB5nVoHhjtpeKxbg9Z0V4WNk12nYtJdexVcLaD9l1-YC7NVmNrMwjdxWZAPvrEzEXEfzLT8Kz29Q01xWo39UvCxO3ZD5qmcj80GxNs-rHUCBQQXkTzh7SAhP0uH2QuuukopwN1jyuG4nEXV8y2OcYir3sCNoTUU4lHNTxDaMVXwOjIUMjAr-csVdpcN9OxEV7Lqk3YsQKMwjV1aeWLgxSwABq9Rp69vU3ve7ILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
🇺🇸
مواطن كويتي يتوسل بالحكومة الكويتية بتخفيض ساعات العمل حفاظا على ارواح الموظفين ، يذكر ان الكويت تعرضت لاعنف هجوم منذ أيام القزززو العراقي القاشم عليها ..</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84029" target="_blank">📅 01:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84028">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5f72fe7a.mp4?token=fGbGg0a4erjpea6p26STenSjAioL_-0L05eFWqtscvKNG0XVlX4VyhFcGirhuEF72kd3Lb96t95UBI8eN5nXA2Zha6dyD4tw2uscYfWZRO8b_5SdQxKw3HVNzcQq6k568iuXibl83Y6rwMsGnfrpbgRxcBI8XJDyxaZ0Yls7v8Qou_k1P1aBz_K_omeUP7msnk09MLevfxn2FZizNq32bTEGttT122MLY1X3w1YpWTAvNEDT8iZAi4zGXzUtzuFbeyFhlTy3vd0wmiCaDO6IJKbAHVx-zwVRgx8bvnEjG0IIoAR1as-ZSiNpGGGsD8LfPlSAF8S_HD4U4s73MXpwcXTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5f72fe7a.mp4?token=fGbGg0a4erjpea6p26STenSjAioL_-0L05eFWqtscvKNG0XVlX4VyhFcGirhuEF72kd3Lb96t95UBI8eN5nXA2Zha6dyD4tw2uscYfWZRO8b_5SdQxKw3HVNzcQq6k568iuXibl83Y6rwMsGnfrpbgRxcBI8XJDyxaZ0Yls7v8Qou_k1P1aBz_K_omeUP7msnk09MLevfxn2FZizNq32bTEGttT122MLY1X3w1YpWTAvNEDT8iZAi4zGXzUtzuFbeyFhlTy3vd0wmiCaDO6IJKbAHVx-zwVRgx8bvnEjG0IIoAR1as-ZSiNpGGGsD8LfPlSAF8S_HD4U4s73MXpwcXTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة بين عصابات الجولاني ومسلحين في مدينة أعزاز بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84028" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84027">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrhvkSs0ER664C7paIf13-0HB85JEY4Cv86Ps5NkfqFIoUUN_e0H5YJ2Vlaae60GFgNX1O1O_whuvJrGb85h-fH3XlKvHaaFKqxbmp9XijRiG_PE-8s_A-G3VHF7oPaFCUWt-hKuVokm9RQgWtaNqhiUrqeOBCGuA8iyReTPmTkqAGMswsB5AK0PVx5OSt8vTn-Qofym73dcOHUtu5ZTtZvnpbxoCU_i9acN9edb0KUNH9WQG2vvupjtzuCYiv7g_FaAcdcCkZHbP_UjhhgGQt5Ti76IIZjLvxWdTis0LPP0dMkl3lNhMV30WPJU9Hh0E8p4vnvwzo9-nZwUEPqLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇺🇸
مواطن كويتي يتوسل بالحكومة الكويتية بتخفيض ساعات العمل حفاظا على ارواح الموظفين ، يذكر ان الكويت تعرضت لاعنف هجوم منذ أيام القزززو العراقي القاشم عليها ..</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84027" target="_blank">📅 01:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84026">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8e8f0181.mp4?token=Qd853wnbWfMEFsX3rtloUdDvbrPQTQPYZA17GlVQsEUMOoI3eCDSW6gPzFp6qmdAom2mH91ztlbOZMNAtbY9mEOmCJCSxj9dyR_y9GpStGYzcYACJ8Irvq1MlhctzYgiFj5crChYOm8MY94ZBdjyFWX3lqVbJzs6V48lXGnaRnBgfdmTFgzWWJPoxf2OXGOuklso8BDJKg266DijiIAPzqgBbt2BUT8DF63ZiEkbZ3OQNwRYdbenI7NlKK5skBTYGJpce_63voBC7sIFfLVfRcnhy00YtUWZN5_14OHPYe1w59Yb57g3PzI9ZJ8GKBIrIw-jPd11OxoGSQOekAr5HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8e8f0181.mp4?token=Qd853wnbWfMEFsX3rtloUdDvbrPQTQPYZA17GlVQsEUMOoI3eCDSW6gPzFp6qmdAom2mH91ztlbOZMNAtbY9mEOmCJCSxj9dyR_y9GpStGYzcYACJ8Irvq1MlhctzYgiFj5crChYOm8MY94ZBdjyFWX3lqVbJzs6V48lXGnaRnBgfdmTFgzWWJPoxf2OXGOuklso8BDJKg266DijiIAPzqgBbt2BUT8DF63ZiEkbZ3OQNwRYdbenI7NlKK5skBTYGJpce_63voBC7sIFfLVfRcnhy00YtUWZN5_14OHPYe1w59Yb57g3PzI9ZJ8GKBIrIw-jPd11OxoGSQOekAr5HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
توتر أمني كبير وإشتباكات مسلحة عنيفة في مدينة أعزاز بمحافظة حلب السورية.
😆
Trump want to use them against HB</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84026" target="_blank">📅 01:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84025">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
🇮🇶
مصدر امني لنايا
قوة امنية عراقية كبيرة تنتشر من سيطرة جسر ديالى باتجاه سيطرة اللج في محافظة واسط تضم قوات من جهاز مكافحة الارهاب و الرد السريع ؛ مهنة القوة مسك الفضاءات الخارجية ومنع اي عملية إطلاق محتملة ..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84025" target="_blank">📅 01:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84024">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/84024" target="_blank">📅 01:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84023">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O97hxx087W3K7TUUvY5GQdUcbMeWTaIuHvjJM9Ti-gNKHNclQ67Ix2qoUXPm1_LHrlmrGJ7gyU0Z5MopVuno4Bj8U9vYUdCf8aZPHI5iL2bdY0omPhMgxYLzU8XRTECLRZK9NEdvwZu_1PGtaK0KmWDBHab7b8jCZrcHO1uFI1wOo2tj0GsocMEu8tNE3V88I-AVR0k6JuoLT6OElT3GZNKZ_VyzQ3L_wlcKQrkbun39AkvheFQiQwAZSAiK9eB0rGE8PRIuiI9ggScTSh83jJ1fNn-PG1gvPmSXP0oRJai0o9H7RKwTeIsuYmkd61aia2hn6ZP8N023PKTN_qOOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
صدای نایا، این‌بار به فارسی
کانال رسمی نایا رسماً راه اندازی شد
همین حالا عضو شوید
👇
🔻
t.me/naya_press</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84023" target="_blank">📅 01:12 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
