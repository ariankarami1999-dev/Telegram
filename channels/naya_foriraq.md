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
<img src="https://cdn4.telesco.pe/file/vIAMeLrxnEoQr4blOGj5skNGhODp_FqsqZrBssMCiSTmO4HfE7mkTN-reJ8GiXFUMCzNwywCxYLBneCXdr-xuCMz-gI7zzSK1oGig4eQS6TlJUQDBdz6KfJH3f4_dAU8PbKWZ1AeNb9AB82r5zOzdBF-8xnRBThxgv45DuSwnf-rQlG4FXnyO2IHwpNT_94KUh6vgvnbEHKkiuSOx7GCR0VDqINKED4FsTfLbjO_2YiQQ5p8SZRhoqe_p67ECvXaPno4Gn-ORoQwonV_WFzXtwHyivTzdjb1uZWuFreGkv-XB_5mt1kLpXqrmqKSnkS3GJZHVjcJSw0O4BbwuQgb3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 05:21:29</div>
<hr>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
الحرس الثوري:
في استمرار لعمليات استهداف الأنظمة والرادارات الدفاعية الأمريكية في المنطقة، تم استهداف وتدمير رادار إنذار مبكر، ونظام رادار للدفاع الصاروخي، ورادار من طراز FPS117، ونظام دفاعي من طراز "باتريوت"، ونظام اتصالات عبر الأقمار الصناعية تابع للقوات الجوية الأمريكية، وذلك في قاعدة أحمد الجابر في الكويت.
🔹
بهذا التدمير للرادارات، يجب على العدو أن يكون مستعدًا لمواجهة هجمات أكثر قوة وتدميرًا من الطائرات المسيرة والصواريخ.</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/naya_foriraq/84557" target="_blank">📅 05:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84556">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7ca1cead.mp4?token=vUYB4Ar3kU2403R8xdkhbe9bhsV0rrzORhufX2g-CX1EoYxKbL8csQHZP6Zt9ZbBIfOfAGzFAIyfREYTZJNJz_N0Vm7mZeuY9gRSgzlQ7XrLaI0p1K10BhbecDgQVdZwUTTlhpX6Gv4H8AQ4TKwWjKNu0oDgZ-bKNLRt6jSEvsyYA1aKPDvKUYJ_M4_a_bBCXYl75DFqUfbOB3fFui2lPAcHdDAldkBRVp1DxTccLIbXr3cvn7LQ8itH2h0hKUBNuETGOswJGGOU3bii3TjcspkU83AWrMA7wY-UfxQu1nwvYOIluzevVBb7pIBBghoMGNzuvv4jR3QUTYUg5sPr3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7ca1cead.mp4?token=vUYB4Ar3kU2403R8xdkhbe9bhsV0rrzORhufX2g-CX1EoYxKbL8csQHZP6Zt9ZbBIfOfAGzFAIyfREYTZJNJz_N0Vm7mZeuY9gRSgzlQ7XrLaI0p1K10BhbecDgQVdZwUTTlhpX6Gv4H8AQ4TKwWjKNu0oDgZ-bKNLRt6jSEvsyYA1aKPDvKUYJ_M4_a_bBCXYl75DFqUfbOB3fFui2lPAcHdDAldkBRVp1DxTccLIbXr3cvn7LQ8itH2h0hKUBNuETGOswJGGOU3bii3TjcspkU83AWrMA7wY-UfxQu1nwvYOIluzevVBb7pIBBghoMGNzuvv4jR3QUTYUg5sPr3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
تامبا، فلوريدا - أنهت القيادة المركزية الأمريكية (سنتكوم) جولة جديدة من الضربات ضد إيران في تمام الساعة التاسعة مساءً بتوقيت شرق الولايات المتحدة، يوم 20 يوليو/تموز. استهدفت القوات الأمريكية مراكز القيادة العسكرية الإيرانية، والقدرات البحرية، ومواقع إطلاق الصواريخ والطائرات المسيّرة، وأنظمة الدفاع الجوي، بهدف تقويض قدرة إيران على مواصلة مهاجمة السفن التجارية العابرة لمضيق هرمز. وتستمر حركة السفن التجارية عبر هذا الممر البحري الدولي الحيوي. ومنذ مطلع مايو/أيار، ساهمت قوات سنتكوم في تسهيل عبور ما يقارب 900 سفينة تجارية و450 مليون برميل من النفط الخام. ولا تزال القوات الأمريكية على أهبة الاستعداد لمحاسبة إيران على عدوانها غير المبرر على البحارة المدنيين الساعين إلى عبور المضيق بحرية وعلانية.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/naya_foriraq/84556" target="_blank">📅 04:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84555">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
الحرس الثوري:
في إطار استمرار عمليات الردع التي ينفذها مقاتلو الفضاء التابعون لحرس الثورة الإسلامية، وفي سبيل تمهيد الطريق لإزالة العوائق التي تعيق العمليات الجوية والصاروخية الواسعة في المرحلة الثانية من الموجة الرابعة والعشرين لعملية "النصر 2"، استهدف الليلة موقع راداري بعيد المدى، ومركز اتصالات وأنظمة استقبال الأقمار الصناعية، ورادار دفاعي للصواريخ تابع للجيش الأمريكي الذي يقتل الأطفال، والمتمركز في الكويت، بصواريخ وطائرات مسيرة، وتم تدميره.
🔹
بالإضافة إلى ذلك، تعرض مبنى مخصص لطائرات مسيرة من طراز MQ9 في قاعدة علي السالم للقصف، وتم تدمير عدد من الطائرات المسيرة أو تعرضت لأضرار جسيمة.
🔹
عمليات الردع التي ينفذها أبناؤكم مستمرة. نرجو الدعاء.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/naya_foriraq/84555" target="_blank">📅 04:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84554">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
‏
الخارجية الأميركية:
تنبيه عالمي: نظرًا لتصاعد التوترات في الشرق الأوسط، لا يزال الوضع الأمني ​​معقدًا مع احتمال حدوث تصعيد غير متوقع.
ينبغي على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي الحذر واليقظة الشديدة، والاستعداد لاحتمال إلغاء الرحلات الجوية، وإغلاق المجال الجوي بشكل دوري، واضطرابات السفر المحتملة. يُرجى متابعة التنبيهات الأمنية الصادرة عن السفارات والقنصليات، والسلطات المحلية، والأخبار للاطلاع على آخر المستجدات. كما يُنصح الأمريكيون الموجودون خارج الشرق الأوسط بإعادة النظر في السفر إلى المنطقة أو عبرها.
تعرضت المنشآت الدبلوماسية الأمريكية، بما في ذلك تلك الموجودة خارج الشرق الأوسط، للاستهداف. وقد تستهدف إيران والجماعات الداعمة لها مصالح أمريكية أخرى في الخارج أو في مواقع مرتبطة بالولايات المتحدة والأمريكيين في جميع أنحاء العالم.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/naya_foriraq/84554" target="_blank">📅 04:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الله أكبر  البحرية الإيرانية تطلق صواريخها نحو اهداف في الخليج الفارسي</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/naya_foriraq/84553" target="_blank">📅 04:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔻
الحرس الثوري:  قبل ساعات، تعرضت سفينتان نفطيتان متورطتان، كانتا تحاولان التسلل عبر مسار خطير في جنوب مضيق هرمز، بخدعة من قبل الجيش الأمريكي القاتل للأطفال، للانفجار وأشعلت فيهما حرائق واسعة، مما أدى إلى توقفهما. فرق الإنقاذ والإغاثة تعمل حاليًا على إخراج…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/84552" target="_blank">📅 04:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
الحرس الثوري:
قبل ساعات، تعرضت سفينتان نفطيتان متورطتان، كانتا تحاولان التسلل عبر مسار خطير في جنوب مضيق هرمز، بخدعة من قبل الجيش الأمريكي القاتل للأطفال، للانفجار وأشعلت فيهما حرائق واسعة، مما أدى إلى توقفهما. فرق الإنقاذ والإغاثة تعمل حاليًا على إخراج طاقم هاتين السفينتين من المنطقة.</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/84551" target="_blank">📅 04:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
🇮🇶
🇮🇶
انفجارات عند الحدود العراقية الإيرانية سمع دويها في محافظة السليمانية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/84550" target="_blank">📅 03:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
🇨🇳
‏
الخارجية الأميركية:
على الصين وقف استهداف أفراد البحرية الفلبينية في بحر الصين الجنوبي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/84549" target="_blank">📅 02:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">استهداف سفينة بالقرب من مضيق هرمز بواسطة قذيفة ماأدى إلى اندلاع حريق فيها.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84548" target="_blank">📅 02:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
وزير الطاقة الأمريكي حول إيران:
الرئيس ترامب يريد إنهاء النزاع باتفاق سلمي لكن الأمر يتطلب طرفين.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84547" target="_blank">📅 02:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
مسؤول أميركي:
إذا قرر ترمب توسيع الحرب فالضربات ستشمل طهران ومواقع نووية.
‏إسرائيل قد تشارك في حرب إيران إذا قرر ترمب توسيع نطاقها.
عمليات نشر طائرات عسكرية إضافية في الشرق الأوسط تحضيرية في انتظار القرار النهائي من الرئيس ترمب.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84546" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA304UoNWkD7XQ9Bpz-S43TtgyiBT1KEOT2LwXQy37PejkS1AnUWsboWz8s0shSzUYupYY8rpAkPnNneL7056WnXrAzaoDP9K29PWwBHzQodHjAyl41T9L-Vn3u5zW8Mq5t_xOBYkH9TFSugh2Ns3qZ-kIzAmBoIOzDnexcbkUsDAoad7Scn8umcPY5AClu2vUyUSYhuayoXWonzLWFv5Z6OwsDEltxBTfsSK_cLdgK7aKl4Bz_eQ0dX_z4fKyO5yCVz614El_qw_604IWfB4Z_imUcTkuelodnHUmEFQ4a7qG_TMUYcK1p2J3FldstXbO_tVAvFtH5TfH-EAKqsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
أجريت محادثة جيدة جدا مع رئيس وزراء المملكة المتحدة الجديد، آندي بورنهام. ناقشنا العديد من الموضوعات، بما في ذلك العلاقة المتميزة التي كانت لدينا مع المملكة المتحدة. سنلتقي في المستقبل غير البعيد من أجل الموضوعات ذات الاهتمام المشترك.
لدى رئيس الوزراء مهمة كبيرة أمامه، لكنه سيكون قادرا على القيام بذلك، وبالطبع الولايات المتحدة الأمريكية. سأكون هناك للمساعدة! ناقشنا نفط بحر الشمال والتجارة والتحالف العسكري وإزالة الألغام من مضيق هرمز والعديد من الموضوعات الأخرى. كانت المكالمة مثيرة للاهتمام، وسارت على ما يرام. تمنيت لرئيس الوزراء بورنهام، حظا سعيدا وتوقعا!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84545" target="_blank">📅 01:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d23af963b.mp4?token=qPDUu8zZYhUG2Ym7dHUZL62XfHi0Ux7B711BeCMOd_OvngfXyLCrH7N6GB6p0nwmtl5Z9QMbDCeeuDOXph4Pld0vOGzVX24ceUq5fWoS6Va-7y7vV3b3AxGEkuiHRI_54AksJAjcbBb4OGVRhJZLgzp_KfCwin742sZ_5r4LQawC1SyPlh2nKYpFcjfnnoM8b2fN_0fuhLdkhVz1snf6bMZBq74nNEZSiWKpkdaYk70kuIJixctJXMiDVqrQQDOrvYk5sj7ZwMQkTqyyTKdLsM7dpLkmlDQyIP8p4tdapICWeo5EzlOfZ1GpKsQ5mnrC-v0cSAAVULC5QOK6CjGRuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d23af963b.mp4?token=qPDUu8zZYhUG2Ym7dHUZL62XfHi0Ux7B711BeCMOd_OvngfXyLCrH7N6GB6p0nwmtl5Z9QMbDCeeuDOXph4Pld0vOGzVX24ceUq5fWoS6Va-7y7vV3b3AxGEkuiHRI_54AksJAjcbBb4OGVRhJZLgzp_KfCwin742sZ_5r4LQawC1SyPlh2nKYpFcjfnnoM8b2fN_0fuhLdkhVz1snf6bMZBq74nNEZSiWKpkdaYk70kuIJixctJXMiDVqrQQDOrvYk5sj7ZwMQkTqyyTKdLsM7dpLkmlDQyIP8p4tdapICWeo5EzlOfZ1GpKsQ5mnrC-v0cSAAVULC5QOK6CjGRuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
ردًا على الهجمات الصاروخية التي شنها "الشيطان الأكبر" على مناطق في بلدنا، وفي المرحلة الثامنة عشرة من عملية "صاعقة"، استهدفت القوات البرية للجيش، باستخدام صواريخ أرض-أرض، أنظمة صواريخ "هيمارس" التابعة للجيش الإرهابي الأمريكي المتمركزة في قاعدة "عريفجان" في الكويت.
🔹
"هيمارس" هو نظام صواريخ متنقل يتميز بقدرته على التحرك بسرعة واستهداف الأهداف الأرضية، واستهدف هذه الأنظمة يؤدي إلى إلحاق الضرر بطبقات الهجوم والدفاع وتقليل القدرة الصاروخية للعدو في جرائمه العدوانية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84544" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الله أكبر
البحرية الإيرانية تطلق صواريخها نحو اهداف في الخليج الفارسي</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84543" target="_blank">📅 01:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGgJrTuNO0N_Fc7IYwDHC6c-iFmUTRnYmD9aQSLYZ_C7sEhQhPU0NSfM6q9DXT96QPXGXViJER1G-Qb3w3vQfmVVW-SbUN_6aYot6-xODcBPTqxO8PjmJuV8dcu3SpAIfUv1YSUk5273nF6SJivAxw6OydVdnY8ETLVcKOcja3h6PgmSsSQB-AYGQcMawo1hrZ8EmA4d4K5bfhqU2YsiTu-h9NC9Nc3KSfHJN4I4412pXLbQ54CpKuLigyywxo0jW7SGIHp3_U6osfF2zSipFSFzc8fEhBzQM0w6GRsnw6etUJ0ADaswGFb2U4-MXzhj6ra2vGlwrWTmkOzNzR4acQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بالقرب من شواطئ عمان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84542" target="_blank">📅 01:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حدث بالقرب من شواطئ عمان</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84541" target="_blank">📅 01:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84540">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سماع دوي انفجار في ميناء لنكة جنوبي إيران</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84540" target="_blank">📅 01:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عدوان جديد على مدينتي كنارك وتشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84539" target="_blank">📅 01:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84537">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇶🇦
قطر للأمم المتحدة ومجلس الأمن الدولي:
إيران استهدفت الناقلة القطرية الركيات أثناء عبورها قرب مضيق هرمز يوم 7 يوليو 2026.
وزارة الدفاع القطرية أعلنت تعرض الدولة لهجمة صاروخية يوم 12 يوليو 2026.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84537" target="_blank">📅 01:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">إنفجارات في محافظة أصفهان الإيرانية</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84536" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12176828e.mp4?token=JrNK8FRbCma14dNE7bvzL1DTZLgMwJI6SJpz1EWS7Kdn8MnlnbzkfQGCx4DQ_UNxMqFJRhdxpOdRER5Y4rH-t8qzA23FwzdNST5t2Q75T1iaMeqbj1o1hT4Q7Gzg__PCuPLDZTdDfp-SHbD8WTorRrVMfhwrL3binkSKGsnA2-V9VLjvleNCteBgyGhw-K14Tf4C1kxA1GV9tEFYfirr7ghN87gh-T3YnZJ9UE2FvCeQj9Rk-4Ev6BAq4AriN9ibf5OzHIn6ckr5M_pzkbBiL-2tITY7dv2CAUabcmj5GNeakppIo2q1l5gkSF62ufuRruRMtg-WaQY6_6MBsnUiHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12176828e.mp4?token=JrNK8FRbCma14dNE7bvzL1DTZLgMwJI6SJpz1EWS7Kdn8MnlnbzkfQGCx4DQ_UNxMqFJRhdxpOdRER5Y4rH-t8qzA23FwzdNST5t2Q75T1iaMeqbj1o1hT4Q7Gzg__PCuPLDZTdDfp-SHbD8WTorRrVMfhwrL3binkSKGsnA2-V9VLjvleNCteBgyGhw-K14Tf4C1kxA1GV9tEFYfirr7ghN87gh-T3YnZJ9UE2FvCeQj9Rk-4Ev6BAq4AriN9ibf5OzHIn6ckr5M_pzkbBiL-2tITY7dv2CAUabcmj5GNeakppIo2q1l5gkSF62ufuRruRMtg-WaQY6_6MBsnUiHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة العدوان الأمريكي الغاشم على ميناء تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84535" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84534" target="_blank">📅 00:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84533" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a66581210.mp4?token=OT1VBFbumrYqj30mcFdfvlRu69Hwyk1YhOHhqs8MqsaMJySsS6mJtA0xbGwCXAXX1VmmA3DgWIylybjQuvQB6xQZVj0DuYkUoerCWrjK3DkNISajkLvUbyRTiMKP90tOOIK8qyOeHnplZzd2iXD4FjIGypUc5_wU9T1CM1-waQSGE9eOyWetb1LspuN6rMW24BdsHiNteSfupZiZqj_Qmv17qh4Clf7ey51j_kdHRhK6YQhPc3Aw3b4ESgeu9pRbVMuu5Kjab9KsEcVomxR92SMC67dMq9qCE60UWAZ6Ys4y9DCBBVowsj8yhdvxuNuqflAkkDoxhRoB9_D3-h8MfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a66581210.mp4?token=OT1VBFbumrYqj30mcFdfvlRu69Hwyk1YhOHhqs8MqsaMJySsS6mJtA0xbGwCXAXX1VmmA3DgWIylybjQuvQB6xQZVj0DuYkUoerCWrjK3DkNISajkLvUbyRTiMKP90tOOIK8qyOeHnplZzd2iXD4FjIGypUc5_wU9T1CM1-waQSGE9eOyWetb1LspuN6rMW24BdsHiNteSfupZiZqj_Qmv17qh4Clf7ey51j_kdHRhK6YQhPc3Aw3b4ESgeu9pRbVMuu5Kjab9KsEcVomxR92SMC67dMq9qCE60UWAZ6Ys4y9DCBBVowsj8yhdvxuNuqflAkkDoxhRoB9_D3-h8MfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان على كنارك وقشم وسيريك وتشابهار</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84532" target="_blank">📅 00:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86bb21e994.mp4?token=GbOI2IjA9tRvL3x6fTkIZgtqoj0Z3YBfKJU_GBAhiDoKj7MLE9F3Ayz7u9NR_r9sr7lTCKBAwxr_ZB-xBU3JbX3b6kAd4HHSE7cIitipDcjlzy-oo46TkdPU8-iIfshxvWFLJAfkqN-eqEKeC9zX8nBCYLGgDCpSTF3wrgLEFP9GpHpJ2pppXHEIcuKh1GeYsN1JrgipQ97K0y3TAY03DuJZs-hE0M_1550fapXa6yYOVImag30bua3vZ9mV-dKKdasL7OCCU3NZy35NUSEMCfMez5KnuOiRt4qO9nplm3qvW86lBypZ7wrXielsMo_qjT8VBIvJMgZRrt31edlbEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86bb21e994.mp4?token=GbOI2IjA9tRvL3x6fTkIZgtqoj0Z3YBfKJU_GBAhiDoKj7MLE9F3Ayz7u9NR_r9sr7lTCKBAwxr_ZB-xBU3JbX3b6kAd4HHSE7cIitipDcjlzy-oo46TkdPU8-iIfshxvWFLJAfkqN-eqEKeC9zX8nBCYLGgDCpSTF3wrgLEFP9GpHpJ2pppXHEIcuKh1GeYsN1JrgipQ97K0y3TAY03DuJZs-hE0M_1550fapXa6yYOVImag30bua3vZ9mV-dKKdasL7OCCU3NZy35NUSEMCfMez5KnuOiRt4qO9nplm3qvW86lBypZ7wrXielsMo_qjT8VBIvJMgZRrt31edlbEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في كنارك جنوبي إيران</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84531" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سماع دوي انفجار في ميناء لنكة جنوبي إيران</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84530" target="_blank">📅 00:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تفعيل الدفاعات الجوية في كنارك جنوبي إيران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84529" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجارات في مدينة شيراز الإيرانية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84528" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الولايات المتحدة ستفرض رسوماً جمركية بنسبة 50% على البضائع الكندية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84527" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">إنفجارات في محافظة أصفهان الإيرانية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84526" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
العميل وإبن الشاه الهارب "رضا بهلوي" يقول إن التدخل الأجنبي في إيران "ضروري":
يمكن لهذا التدخل أن يساعد بالفعل في إنقاذ المزيد من الأرواح التي [قد تُفقد] لولا ذلك.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84525" target="_blank">📅 00:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8b4dd13a.mp4?token=t61vb-UCkS1FFD6GSiyyvt8c76ZlsAl-SpWdAzYSA_jugD8sIGsh3l6iyshhx6dhzLkhsjaSbp6OO67hFLpuaLKiUAZyRVQDZBqnbPbrfakHcTimwomePF892NXp2ZYnCXuS66qNOxvCSDa9ZM4_jg9lV7lsbs3CwJjZA1VfOqFGL8hLpBuuyn5wo_uwMgK_jllyQxDYx_WFyKJ8UtrOZOgGrZfjIzUzwubr6YvPN_c1-kxmixF5-oMhbfGI-YkjG2Uy6DrV7FKnibFD1258ANBKiHqRZHiyYWGqadTLNNmqId28hM0sZ449D0Vedv81y8hqzt-3ur2W-7-ZL3WW9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8b4dd13a.mp4?token=t61vb-UCkS1FFD6GSiyyvt8c76ZlsAl-SpWdAzYSA_jugD8sIGsh3l6iyshhx6dhzLkhsjaSbp6OO67hFLpuaLKiUAZyRVQDZBqnbPbrfakHcTimwomePF892NXp2ZYnCXuS66qNOxvCSDa9ZM4_jg9lV7lsbs3CwJjZA1VfOqFGL8hLpBuuyn5wo_uwMgK_jllyQxDYx_WFyKJ8UtrOZOgGrZfjIzUzwubr6YvPN_c1-kxmixF5-oMhbfGI-YkjG2Uy6DrV7FKnibFD1258ANBKiHqRZHiyYWGqadTLNNmqId28hM0sZ449D0Vedv81y8hqzt-3ur2W-7-ZL3WW9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لقطات حصرية و اولية من قاعدة موفق السلطي في الأردن اثناء تساقط الصواريخ الإيرانية عليها بفشل واضح لمنظومة الباتروبت.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84524" target="_blank">📅 00:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjLiwsf40HXk5onCZ9p1kjGTSxb_5yhXyzjGltsR_G1ElBk5XayzioadRS8sEiknOAv9jbB_7WN2a5oDVp00JuchpJNfk7i4pkOW7nVXwNvrDGeI7GOOqeJTUb4QCbB6pRPPjUlWP3fmEkq9Oyt54JkIXN410KOIuJo17bsi_rZWE5tZwRad7cGs-YoWjUp2Xx4uJ1JATrT8-8DV6xqCxRkvQzjSKPcYux1fkdug2I6muwgmfqp6Tg2pKneYqaAXF3a-zGTNC2CMPmTKyOhg37ezZY2jy0-eXGiA2ugSYJGVBZi_Bt7iIsg7j-qPWKq0_OGY0MNYvsV3rXz-Y2rcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار الانفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84523" target="_blank">📅 00:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-G_iy9HlbOv6XFUtqnzBs1WiT0R0USeaVGsc5tYPP3S4Oe5ScSu_RdCvI4G_X3R2v9PByQvEEV4ViAq4xedCqv_0lRvCWj0S5HSdn2Cr_LJenTHobnWhTP3JRGs971sJfB6WDALO8s0hHUfd8lzuzMFsZR94jLSsVbe1q6X4mfw2FxamAo5WBEep_OWCL7n_S0CHaovC1Ruh43FAt7jMSEjCiZt7mQNwa0W-gPLNPMh1cUAA1ZJKwl4QN2ngGj9XtziLDnbD2SQncWxXT-WpeHdU-1ueZgNKBnkF-q9LHg5D_1GtodWleA2LXjHfT8jRDRRJDBDIRb3BUWTEePTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النفط يلامس سعر ٩٠ دولار للبرميل الواحد ، مع توقعات بارتفاع أسعار النفط بعد إغلاق مضيق باب المندب من قبل أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84522" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
🇮🇷
القيادة المركزية الأمريكية : بدأت القوات الأمريكية اليوم، في تمام الساعة الرابعة مساءً بتوقيت شرق الولايات المتحدة، جولة جديدة من الضربات الجوية ضد إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الضربات إلى إضعاف القدرات العسكرية الإيرانية التي…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84521" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">معارك بحرية في بندر عباس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84520" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
🇮🇷
القيادة المركزية الأمريكية : بدأت القوات الأمريكية اليوم، في تمام الساعة الرابعة مساءً بتوقيت شرق الولايات المتحدة، جولة جديدة من الضربات الجوية ضد إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الضربات إلى إضعاف القدرات العسكرية الإيرانية التي…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84519" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
الإطار التنسيقي يعرب عن دعمه لنتائج زيارة رئيس الوزراء إلى واشنطن ومساندته للحكومة في تنفيذ الاتفاقات والتفاهمات التي جرى التوصل إليها</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/84518" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5zqGssS7Bu_h1AKI5KAA64z6atSfmFd6tiooN3X5OzwVASfQnRiixKUlwg6aMZSmsnKPxNNeRaUqfOM82LlDywKcYpNYWP0STv4GO0qRwR0xgr-DvlrkDqkgECPHpTXPXU6TBIAg-g0iOfF7sRv4s0lbmu3TgTbdRGc2oCOybuF0oy5aVYWLtV9t5Kj8TY8xmU2vZryG0DV1S6CK11vvTvchuuVmRxhZ7bT-AktivIe_Ouv2-QBlOtKzoAVVc-uSC4-qclqgrlkt4urnBoLhpFj9g-0RfgIFHl_CqfY9H4dh7TjS1RBQpfFwmdsxBQ50ZNtoFxQaoQCQV5eo2q4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
لأول مرة منذ القزو العراقي القاشم
مواطنون كويتيون يطالبون الحكومة بايقاف شاشات الإعلانات في شوارع الكويت بسبب استهلاك الطاقة الكهربائية، يذكر ان الكويت تعاني من نقص حاد بالطاقة نتيجة القصف الإيراني القاشم</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84517" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84516">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/birGcqjUoomcUG4CyHl7rofVNmuzHwhPxaFIGKHtPUOYjkfxlgbALimfiNoEeWPUFIs_EsIA6KeY0tnTSO9w_P4eyrm-qs4Atf7WvbF-epu0aPShOK8sBqLssqxlalvFExVcSAEGFBEaOBh_PgtlCGcKCPckn7kiMDh_8h1stKebPxLEr2toMA4OBhln4o6WAIDFWYmDZvcJKq6TXlPadlQolWJfekZ1SdpodDIAqpzrYxjoSC5mUtcUmbCVCXnX0YlskJt4_hkCiWSIHxjoxoWBVQuCuiPtTEWbuxclkLPaxUtJIrb9phhjy286YGdgOK9Yu0hjTY-y-Q7cfQ3g9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
مواطن كويتي يتحدث عن القصف الإيراني : ايران تقصفنا على مدار ٢٤ ساعة ليل ونهار</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84516" target="_blank">📅 23:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84515">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUUdYazug7TTy2sE9sdDV5w2bZcdrwbYmT-hEWyPA3iMsG_EhjwXaOrM26ZEnZgNldv1fTLHlv1_aWVSz1GFul6y1En37lbCW__F4UrmzZtoU4iiFhWcx2VS_uKDXf9miJYdoodVx2JJ81-CNSlRQcRHveVPhthxWwIoNUS_MO8e9hj_cjzKt-9nhwZ4Wakef8emOmu6cv94TA_FHGcwii6H91Bnk9qDhVsL5srg4mJ2R0-GkvWJBc4xSZ1xXZVTFHzxJenkMt9NIkFxw0GiZUPxl-G0CVr0Q_fmVlUgx38c-QgHzmPsSWs0gZI0-bUy_j2tDQ-JpzcesaZmsx1Kqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اضطر الموقع الرسمي للمنتخب الإسباني لاستخدام الذكاء الصناعي AI ومسح صورة تواجد ترامب اثناء الاحتفال بكاس العالم ..</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84515" target="_blank">📅 23:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84514">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بوشهر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84514" target="_blank">📅 23:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84513">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
🇮🇷
القيادة المركزية الأمريكية : بدأت القوات الأمريكية اليوم، في تمام الساعة الرابعة مساءً بتوقيت شرق الولايات المتحدة، جولة جديدة من الضربات الجوية ضد إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الضربات إلى إضعاف القدرات العسكرية الإيرانية التي تستخدمها لمهاجمة السفن التجارية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/84513" target="_blank">📅 23:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84512">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/84512" target="_blank">📅 23:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84511">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
السعودية
: ندين بشدة ما تطرقت له الحوثي بشأن حظر الملاحة البحرية على المملكة.
اضرب ارامكو
😆</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84511" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84510">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84510" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84509">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
قال مسؤولون أمريكيون إن ما يقرب من 100 جندي أمريكي أصيبوا في هجمات إيرانية على قواعد متعددة في الشرق الأوسط هذا الشهر.
‏تعرض بعضهم لإصابات دماغية رضية، لكن 96% منهم عادوا بالفعل إلى العمل.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84509" target="_blank">📅 23:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84508">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
🇮🇷
اكسيوس :
مسؤول أمريكي يؤكد إمكانية إجراء محادثات لوقف إطلاق النار مع إيران ..</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/84508" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84507">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cdb4e63c4.mp4?token=Y_676zQDzSlEpjaZfjdS2zMg1rcSNErhVPkwHYJz4lmw14ABlU5SUtlTTyMpchT4T6VuWyrAxrxkQJiPMEsBK3iK0epYKp--0qkwk_84eXFaJpzqfLo5ODz4eQHwBunBDQYZsXv5BVxQMCCopW45pmb_3gKaaztVJIJSf6rtm28ovAv9jXdKByQ5Jv_hhKLzxwgTGOD-tXDzYcaepWt4gIY-xM2ARvdBHRDWpjOCUwVTJM9iVTaOgit8QrqB_CrTqtjSUz8vtRT9JSb9TxDjGk66PB_g0YNmGACuZCAmrh4_Bw1TtSkxyvM0I-3ljIcVLvV4aFLZBI9VCDCc7pwOYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cdb4e63c4.mp4?token=Y_676zQDzSlEpjaZfjdS2zMg1rcSNErhVPkwHYJz4lmw14ABlU5SUtlTTyMpchT4T6VuWyrAxrxkQJiPMEsBK3iK0epYKp--0qkwk_84eXFaJpzqfLo5ODz4eQHwBunBDQYZsXv5BVxQMCCopW45pmb_3gKaaztVJIJSf6rtm28ovAv9jXdKByQ5Jv_hhKLzxwgTGOD-tXDzYcaepWt4gIY-xM2ARvdBHRDWpjOCUwVTJM9iVTaOgit8QrqB_CrTqtjSUz8vtRT9JSb9TxDjGk66PB_g0YNmGACuZCAmrh4_Bw1TtSkxyvM0I-3ljIcVLvV4aFLZBI9VCDCc7pwOYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
مواطن كويتي يتحدث عن تعرض طائرة عسكرية كويتية إلى هجوم إيراني كادت ان تسقط !!!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/84507" target="_blank">📅 22:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84506">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpYIZMkgK2na27BN2t4KcOp3KQWTYRb71hTuWk8-TMsRqMHjOxQeXVWp88gQ7KtGiN8AFXlufqw0JnYeaferSZvpzhdlyptdVmCMrN6MGgxYQI1taOqL3_k-TdFp9T_4H9BwBuOEfEAkycQAGF9Lq0UULFtcq7e1EBL_n5dJAo8cIdpK8H_0ZViD6rciSw9f4Rq9mrP8VB3iLT4pmNDGoVpDeiiWnlNvPdAGPnoejqwaF4FPtUMZ_5-D-ZA0NDL98BeKqYbQ_1LJGl5O25GTeEaGrJAyYKlDhJoY_bfKD9baFrXjdFlC-mJN2jZR_oHqrYznO4wmUVcxNzAKmoWpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
كتائب حزب الله في العراق تبارك لانصار الله قيامهم بالحصار على السعودية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84506" target="_blank">📅 22:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84505">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjPPK5g0wabe_7ZMywxcR37QVtE5SOhJiiSJK6zPIKGcS0-KLHPxNPzOMDTL_QWIv7jg8viOSDTdxgecHCZOzR6GBh7qhvlXLhl8DScgSA7KN0CIXlFqRBVZzg05Mz6gaMg5N2frS7vA-HbDRXj2HFYNarZv7pZyiNEXH8N03vqiTXYbU5uhXQEwcE4dY77HfphDX4k-vhDzFVTf-CSe-ciQAKsqi9DBcO5lX_SlD1JZynwmyGtDQOrvzuaUdLdOb8ADE1CWNp6gPX9xpvNsXUQgC8XCF6CngYzoz9ywd0tVSnzj5kXk1x4YfEbuCQPaiFjAazaRt0vYRQq9weNyFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
مواطن كويتي يتحدث عن تعرض طائرة عسكرية كويتية إلى هجوم إيراني كادت ان تسقط !!!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84505" target="_blank">📅 22:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84504">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4708281409.mp4?token=st51fxrKBf-HEvcu5XA-u5IlxiPhnK6OmWR6rYqFs7HhvcJlJOELaooNmasRETBehMVXHqQbf75ZFUFZjmKvufXFXOg9moSWNMABL_NUk1BpgoSVlxXkOU6ly4oFsN8r96BTNfTOxjQKUDEs8mElKUm7-qxd4TQqmcKT53xVwWfR-QBVuQ6mt8_3S79cLOLsny5fs1TQ7DGR8gPvtKfGwHmG7uP1J5wJz3YMwcyMEX-breGo4YKn-Iehxgs44BxEfEp9ZQy1vUf19Xb7MtvRuZvXQ7Nd30mWRDN8QXGUt1ww8enAEV2mgU2fNj812LBo1TxzRSihpyHv364bBlWKHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4708281409.mp4?token=st51fxrKBf-HEvcu5XA-u5IlxiPhnK6OmWR6rYqFs7HhvcJlJOELaooNmasRETBehMVXHqQbf75ZFUFZjmKvufXFXOg9moSWNMABL_NUk1BpgoSVlxXkOU6ly4oFsN8r96BTNfTOxjQKUDEs8mElKUm7-qxd4TQqmcKT53xVwWfR-QBVuQ6mt8_3S79cLOLsny5fs1TQ7DGR8gPvtKfGwHmG7uP1J5wJz3YMwcyMEX-breGo4YKn-Iehxgs44BxEfEp9ZQy1vUf19Xb7MtvRuZvXQ7Nd30mWRDN8QXGUt1ww8enAEV2mgU2fNj812LBo1TxzRSihpyHv364bBlWKHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴
🔻
قاعدة برج ٢٢ تحت غضب رحمة صواريخ الحرس الثوري</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/84504" target="_blank">📅 22:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84502">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UF4rgnFmgWSlskCHMHOh39eJaAYsc6E6JsWYr_K38fkZoMWGbquyG5MsXFozrFwQDqigoCrqRTXCodtwUL3Jj9Oadjw0ky3BamGHS4UibTC2WaF2I5TWOC3w_d0BKTBa9V5VWzTFK4o0NwvcXWX_oWoRpPWp4FkzvWjA9gQNLUJwZdhIhDae3t2oi_4YlsxqSujL0RNh099iUXh1ljqBsqOjSX5TJhCr1V4Ez4xKHpx8ss5CeY26xMobkp1Xpp2ssvSqiqpmHs13DXS_PhC8QGVeQ8wR8vy8SRz9mNhS1tA1YSYw1seAzzZSCJ4p23dVq7BGndia0gzQmJmuk1__Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asFDLsRckbMTESLeD3JYM2qkTSzFg2zULjJ3FPrkgrdHM5AMcVW0Bqj9Re77JLlqpE6PNKbrGS2oUc5eQblXqSPXR2a684tOsJCfyZVfj0T1g__qqYMH51dm7rsl_gtKCwNAez7jJgY7wr4h1is4maHNpQd96_ABkgoLvm3hF1bRRHdR2pFFZjhdyusIvZAfxt-BB2M_50FakM88KnXIzlUF2coIC4cUPZ0t6NW4WOwJrB6tnIG5GMPpKJquSsOBFIrZ1Ue5gTXX8tGqPtb9K_MkcrIBVorv1SbIhC1_vvoFUzF6f5s1S85CKtDyKnf1NRqi6MLQqpxfo3oAdiM7YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اثناء انطلاق الصواريخ الايرانية نحو اهدافها</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/84502" target="_blank">📅 22:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84501">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYERH8RhLXv-fq4DDS-4NH3nhGojDA59s3olpAl36xVjsMv8NgHrGxOBbsNKQ8S5aCJ3hyynTOkEktCgTProHO-Vz6CMAjqV5LtQacL9kjEyQT0urMqRESmTYWvNdJzH_cmIPn0go65TT3WHIAKwHJSk_4iJe3AKy5B9ksLXmPwghefih6xIH-sFZIJpHWPOLDHyJcwRMR4vqq6Vp1M5bBq80BsegGqOwgro663f9xAGvblD8fWy-HY9FAr8SFVZEP9JIRjdCFMJKuWEVt7S3gk9BPNr5mWjDsgtayEF26j-Mm8fr-DS3bnvEdwQZAqSWYRYWNKStMhOp-0YuIWoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تم اعتراض وتدمير صاروخ كروز أمريكي معادٍ في سماء جنوب محافظة كرمان.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/84501" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84500">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">استهداف قاعدة الحرير في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84500" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84499">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">أعلنت الخطوط الجوية الفرنسية تعليق رحلاتها إلى دبي والرياض مع استمرار الحرب في الخليج.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/84499" target="_blank">📅 22:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84498">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تايلر جيمس فيهان من هاواي القتيل الثالث الذي قُتل بصاروخ ايراني بقاعدة موفق السلطي بالاردن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/84498" target="_blank">📅 22:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84497">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d6a551d.mp4?token=i9MGxi0YIwEJJThbJ2OdDFrf2RbCtEA44ObSMs30VVA512GiRMkcoCRwLZHK0xOxba0DFihm-ieNJ6oa4WjFJ7nk-r-7o514DCbkAucT3EY2qZ0AGmjwY6btn_bnHNIJ_VzdzHgvnbeMEMv1tfKAS305tMvDoWmYQC8ehMj9TzFyKoJcS2avB-DqeYEi44tsZHVqXkQQiZGT6jzlHiYAPYmt3hWXaMlB8Uc_YmKmJGiTrszDL2BL1vq8z_YjsvK4D05FXb0PQpSpRF6Tdvwv0NDdrPioZ8k1lHYTGcFfJ8V-XEGbbmlO31ESiwFBIn-g0ToCdUdwhfZa-3irl39xeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d6a551d.mp4?token=i9MGxi0YIwEJJThbJ2OdDFrf2RbCtEA44ObSMs30VVA512GiRMkcoCRwLZHK0xOxba0DFihm-ieNJ6oa4WjFJ7nk-r-7o514DCbkAucT3EY2qZ0AGmjwY6btn_bnHNIJ_VzdzHgvnbeMEMv1tfKAS305tMvDoWmYQC8ehMj9TzFyKoJcS2avB-DqeYEi44tsZHVqXkQQiZGT6jzlHiYAPYmt3hWXaMlB8Uc_YmKmJGiTrszDL2BL1vq8z_YjsvK4D05FXb0PQpSpRF6Tdvwv0NDdrPioZ8k1lHYTGcFfJ8V-XEGbbmlO31ESiwFBIn-g0ToCdUdwhfZa-3irl39xeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
مشاهد جميلة مصورة بعدسة عراقية من انطلاق صواريخ الايرانية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/84497" target="_blank">📅 22:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84496">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c5ba4b30.mp4?token=JBqEsoC0OgsS4tAjzclHVs3h3rkFUoWtW6IjP5qYauEpuWNEroM667e8b0iXod5oAEVAqGD9o-IfO3vKHvpXBBPv40B0aYuGm7BFeQBDM6sq8x4aLgkAaORR61iemsgdsfb-pCgi7-WW-B_DZFlM1OCbr603gURV2njGl0XsYaeklOGEKlox4LjJimShTuvB3fbDOVwiZEZ2P3deIbWj2VBF2tA7aSVpD3mJ_dnsBFmVKKxAIQic6kXauukA7frPLH5lGk7NamGX0IsAXJUJP5MV2wgmLvbO9bYWRepNWoHL8SPW2OLHOctqRW8N7G559zs6lmF_tyDE09Ugq0EzHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c5ba4b30.mp4?token=JBqEsoC0OgsS4tAjzclHVs3h3rkFUoWtW6IjP5qYauEpuWNEroM667e8b0iXod5oAEVAqGD9o-IfO3vKHvpXBBPv40B0aYuGm7BFeQBDM6sq8x4aLgkAaORR61iemsgdsfb-pCgi7-WW-B_DZFlM1OCbr603gURV2njGl0XsYaeklOGEKlox4LjJimShTuvB3fbDOVwiZEZ2P3deIbWj2VBF2tA7aSVpD3mJ_dnsBFmVKKxAIQic6kXauukA7frPLH5lGk7NamGX0IsAXJUJP5MV2wgmLvbO9bYWRepNWoHL8SPW2OLHOctqRW8N7G559zs6lmF_tyDE09Ugq0EzHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84496" target="_blank">📅 21:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84495">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84495" target="_blank">📅 21:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84494">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtqwk2VxvEDyJfO-aRMf9QTdUdzZQnwjCtJ0h6R8vUDg6JMhJKJfefPO6TEV3RsRDBbjZ0YdF3py2mASaWwhUzQ_NZVJlu3PzD5vaVh5G1TVxq2QVN9ChBZFk29M1qEBb9uZY52831_PvOjS59MgLRPhL2SgIItRdBptbGnKyhZzLf8krPS4aJZJaMU3Ru8hM7S7U-ASvYIntf19nrrJz-QXcAfCRJxDJEMgKyb3HskUErftQIeYcwy9PfOK6EqRCBCzlvmJGLcYlO0QO4aphh7hD4EC7T64Pn5hEtUBYqww5WDJH6CvQHoEsr1nRnPEvu4-KlLPnpA3xrlAaPXRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأردن تتدعي : اعتراض وإسقاط 3 صواريخ قادمة من إيران استهدفت أراضي الأردن</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84494" target="_blank">📅 21:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab6ef0aca.mp4?token=nWdny3_k9h61Q3apEWicLLgSSA0rRBYPpZKYQRlE8cy6EtLUgw2CCm3UTsZf04YmKTgxPsUN1C4H79FA6Fs5F6uph4PMec7aCFsB0-MmBwCQ4LNjl6DrxJOz_Tv7Mos2uLr0909KpIZFwuo2z7IaAW5RSWILc9OYKNcfNl0S_aK662AqMMufFPYF8S8EDVRYD7NGoIjo7m4iE3N6V8JhkfRnjsMmw63QfJLup2G6Eb2KTMRl5OPnQ6e4wNsZ_0tEyXX5ufAnkmsOAUptLAtph7VdC01sSadybfPsugPY6TEUI9MtleywSP3DnXhpO84Ssp0mZXSGCknpiRcFMxfMdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab6ef0aca.mp4?token=nWdny3_k9h61Q3apEWicLLgSSA0rRBYPpZKYQRlE8cy6EtLUgw2CCm3UTsZf04YmKTgxPsUN1C4H79FA6Fs5F6uph4PMec7aCFsB0-MmBwCQ4LNjl6DrxJOz_Tv7Mos2uLr0909KpIZFwuo2z7IaAW5RSWILc9OYKNcfNl0S_aK662AqMMufFPYF8S8EDVRYD7NGoIjo7m4iE3N6V8JhkfRnjsMmw63QfJLup2G6Eb2KTMRl5OPnQ6e4wNsZ_0tEyXX5ufAnkmsOAUptLAtph7VdC01sSadybfPsugPY6TEUI9MtleywSP3DnXhpO84Ssp0mZXSGCknpiRcFMxfMdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق العديد من الصواريخ الاعتراضية من قواعد الاحتلال الاميركي في الاردن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84492" target="_blank">📅 21:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84491">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqCHJ2XaeHoVQV-TiVPYF1r7s1dsTVV0QHyqzHCG9DOz2g88mB-npdFXpMlcCxEkRqEkkyg2Ab21F38rv8GTtcx7WrbKQTNMu2nk3fnJyfmovkLwg-L5rMHnUUBuv1IAHa_rp4WSPBJt4vzcU8aXn95gRKNcmhmJ2PF1vrvn0kVjWVsLSTdLHWKKm2OLbW7tfV-qxhY5fKRRHmK8QPDuXKcpE7Z9YI0_Tz9dcib7A50VUnV-Aa1K1jc1ejnULULZjLqSKPTJcSrI7dvqfoTHxPCm7Y_GuUoqO-jAIuBg7k79sAtIESCR6Ujpr6U_ORjVa2BnaV83pmpa35oD_S7gBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
نایا 10K شد
از اینکه عضوی از خانواده نایا هستید، سپاسگزاریم.
@Naya_Press</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84491" target="_blank">📅 21:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84490">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8929456f8.mp4?token=KMsczyGyb2Kq4fwx0EmZ0XTn7KnytDIUvaREOY00KA_JPyZdW4bQO714J1LZuUJNtp9VE6UrlsD8GCp-vjbkQJQT99F15DEMFX0kcJ7dmz9XGSc8cDM95JnSaJhfidNYKMtLQ1A2WhgmPOwOnyOsn2fDaTE-dke_9WXAqkCY3pBNUDsozZVapib7sP4-QqViWouvKsSZDa-9WZtsBjtOFCzT5VEq7-X8Yim_PhIPncJ8ChMkZN1qzM3jA0cIyaHs-O1qOhquP3afgBQwcodHlD4jMvB7VTMVIBTcV4YeJqSUmgJilITwPr5naPlTElCFDDTCKJ6jOGRS5GSlmtS2kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8929456f8.mp4?token=KMsczyGyb2Kq4fwx0EmZ0XTn7KnytDIUvaREOY00KA_JPyZdW4bQO714J1LZuUJNtp9VE6UrlsD8GCp-vjbkQJQT99F15DEMFX0kcJ7dmz9XGSc8cDM95JnSaJhfidNYKMtLQ1A2WhgmPOwOnyOsn2fDaTE-dke_9WXAqkCY3pBNUDsozZVapib7sP4-QqViWouvKsSZDa-9WZtsBjtOFCzT5VEq7-X8Yim_PhIPncJ8ChMkZN1qzM3jA0cIyaHs-O1qOhquP3afgBQwcodHlD4jMvB7VTMVIBTcV4YeJqSUmgJilITwPr5naPlTElCFDDTCKJ6jOGRS5GSlmtS2kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متتالية في عموم الأردن بلا توقف نتيجة القصف الإيراني</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84490" target="_blank">📅 21:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84489">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">يا قائم ال محمد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84489" target="_blank">📅 21:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84488">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0bbf054c.mp4?token=WA4_VfCC62ARb7Nc8ICvCUnEIdmIaYcPo52CwBqcL1JNSKpOOmJQ_emf4qnJ5p7OG9Z-KUw_4eEDEWgduURglD17-iRB7THYHhACnSxsSMuY7kin2j_Ga5Jr6fu3MCCJOdUnXKjZn7N2Qe6GG7WfRMB3DtrKYJ6LV4oCV6-VyWbkP5fciMOCu3PMx--HEdC92Mp0Oadyuc7O5MI8RadXBmaavdbNap2_B0LW3rXq7hGgaIKhn1-HMJj8nAExCV7iLubwuPSNVbtjmEiGr4FqIgBr6Ki-fzet0TCFk9lESzayab8PqZxUbhFmIamQsvXvGIu056GrSCxlkH0sSu_VEy9vKgR278LkH0PKG34geN4dCcE3959YiVV9qlf5EzdJFFuyf_9QS66g5LrysddXQH_t_cQc7hUgSfq9zG50YQE5oAK4bHRrrQKQshMEpbfUeQeGc2WADhVwF6Tpk7lh1TMAFd7SUjnufaW6FM0ZBn-5Vnv88ASJbrD66dXHzpMkbC0KEDUIzgnSaomvGoynEYctcpBi2maTuQKcjk0DzzQBNtqpDDEEOQ9Ibl5hB95UMtB206zTTE3yUM52DgBDGMPBDOH_MO2oSKhNyHolMHZgv1Gx-dqx9s6qop8rp86lmIEi7Wrwc4PFWstdUnqgJEUJ7NrDsMrkw5X0WHzpfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0bbf054c.mp4?token=WA4_VfCC62ARb7Nc8ICvCUnEIdmIaYcPo52CwBqcL1JNSKpOOmJQ_emf4qnJ5p7OG9Z-KUw_4eEDEWgduURglD17-iRB7THYHhACnSxsSMuY7kin2j_Ga5Jr6fu3MCCJOdUnXKjZn7N2Qe6GG7WfRMB3DtrKYJ6LV4oCV6-VyWbkP5fciMOCu3PMx--HEdC92Mp0Oadyuc7O5MI8RadXBmaavdbNap2_B0LW3rXq7hGgaIKhn1-HMJj8nAExCV7iLubwuPSNVbtjmEiGr4FqIgBr6Ki-fzet0TCFk9lESzayab8PqZxUbhFmIamQsvXvGIu056GrSCxlkH0sSu_VEy9vKgR278LkH0PKG34geN4dCcE3959YiVV9qlf5EzdJFFuyf_9QS66g5LrysddXQH_t_cQc7hUgSfq9zG50YQE5oAK4bHRrrQKQshMEpbfUeQeGc2WADhVwF6Tpk7lh1TMAFd7SUjnufaW6FM0ZBn-5Vnv88ASJbrD66dXHzpMkbC0KEDUIzgnSaomvGoynEYctcpBi2maTuQKcjk0DzzQBNtqpDDEEOQ9Ibl5hB95UMtB206zTTE3yUM52DgBDGMPBDOH_MO2oSKhNyHolMHZgv1Gx-dqx9s6qop8rp86lmIEi7Wrwc4PFWstdUnqgJEUJ7NrDsMrkw5X0WHzpfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متتالية في عموم الأردن بلا توقف نتيجة القصف الإيراني</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/84488" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84487">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
🇺🇸
طيران بريطاني من طراز تايفون يحاول التصدي للهجوم الإيراني على الأردن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84487" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84486">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=B2aOBhxb8jeuWc5AdMXowJ8RF5w9Rg89Bj81k-c9jUX5QieBuPwY0EcUJec6GUvjkx4iEtxls0gn1YHXJEObKd9ov_U7Nn4boT3gdyVpmbxK9Q6V_QMlvCYHk28cPeVHOubk7xcI7GxMe0_3IZsnOUmTwnZgPmhZVdzHADEo4wJzAzEEDZ856lmkFlCFTBkxBJBigDYPVeJsRhTGDPMBXWlXOzP3c7XvCVSdsR2egDrneWIxRiO7cV3Hj-YCFvcz6kEBAnza4Ftl5r9wxxM76ENrc3TwvZc5FUeG25hshkvOlk_WqE3OhMe9pLIUewSE2rugTSxAmSysbWf_yTd7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=B2aOBhxb8jeuWc5AdMXowJ8RF5w9Rg89Bj81k-c9jUX5QieBuPwY0EcUJec6GUvjkx4iEtxls0gn1YHXJEObKd9ov_U7Nn4boT3gdyVpmbxK9Q6V_QMlvCYHk28cPeVHOubk7xcI7GxMe0_3IZsnOUmTwnZgPmhZVdzHADEo4wJzAzEEDZ856lmkFlCFTBkxBJBigDYPVeJsRhTGDPMBXWlXOzP3c7XvCVSdsR2egDrneWIxRiO7cV3Hj-YCFvcz6kEBAnza4Ftl5r9wxxM76ENrc3TwvZc5FUeG25hshkvOlk_WqE3OhMe9pLIUewSE2rugTSxAmSysbWf_yTd7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية تتوالى بالانطلاق من قواعد الاحتلال في الاردن</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/84486" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84485">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10e9679e1.mp4?token=rw0HgJ9dtq5IoXASTtz2lmuVlhAcZHYWdYuurBR57SFexPCY25IOtD_sOU705l080e89FNR8dROjFjchYJO9Qi29WujWudZ5kZlbypZZoRTdzWt3-j4Dig0tuLMs24cC2aYePZ_atkrs_Cx3OFQlNl647hmY1x2thakrLwYoClJdO30ionhudbjtNViabMFVHMnwvuX5sPM1B6kVwEh_XNCzKTV1uQ4ZKlldEa4apFYyMqHuc4EoT1Sb1yxSBa9F-sQkRcAlX5ocF0_DdyqBSx6VNZq_LlBeymVQNT_wbaxB2Df7bF43uQVuwgyEyA09BQqjiTGB9FXG0drz5zjDNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10e9679e1.mp4?token=rw0HgJ9dtq5IoXASTtz2lmuVlhAcZHYWdYuurBR57SFexPCY25IOtD_sOU705l080e89FNR8dROjFjchYJO9Qi29WujWudZ5kZlbypZZoRTdzWt3-j4Dig0tuLMs24cC2aYePZ_atkrs_Cx3OFQlNl647hmY1x2thakrLwYoClJdO30ionhudbjtNViabMFVHMnwvuX5sPM1B6kVwEh_XNCzKTV1uQ4ZKlldEa4apFYyMqHuc4EoT1Sb1yxSBa9F-sQkRcAlX5ocF0_DdyqBSx6VNZq_LlBeymVQNT_wbaxB2Df7bF43uQVuwgyEyA09BQqjiTGB9FXG0drz5zjDNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية تتوالى بالانطلاق من قواعد الاحتلال في الاردن</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84485" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84484">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">إعلام أمريكي : مسؤول أمريكي يقول إن زيادة القوات والطائرات في الشرق الأوسط مقيدة بأضرار المعارك، محذراً: "ليس لدينا ما يكفي لمواصلة العمليات بأمان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84484" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84482">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1e42363f.mp4?token=IEz9DPbpy5conwdfOt-MVRLXAsxeGa4PVigEDweaPQjwuY8FkYeUfSfsydsLW0v-uEJt1_PQ86Nl6EQw1oYNmW4TB8lsd3CoWjZbrPQxkew-Y8hFaVnyz8zoZbj4hRyRlZOmJ3qX0hWneQ1RUGKdni5NJCRKAJ7F0xQ6RR11e-8PxlCf9sJ4gwXdScRrMkpVYqX5tICpGYRu_AmnR7nxgQE0quMigP87s4T1E9X-db7dEGMhD85BAB_NUbFBqnbgfBNYHwVFFhp3w4kXMexC3_u6SUZzFWxbXsfXkBhLG58r_43fXWi1-7lnJ4kdj1faOcw6HM0om-4KzaQ5A5zVCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1e42363f.mp4?token=IEz9DPbpy5conwdfOt-MVRLXAsxeGa4PVigEDweaPQjwuY8FkYeUfSfsydsLW0v-uEJt1_PQ86Nl6EQw1oYNmW4TB8lsd3CoWjZbrPQxkew-Y8hFaVnyz8zoZbj4hRyRlZOmJ3qX0hWneQ1RUGKdni5NJCRKAJ7F0xQ6RR11e-8PxlCf9sJ4gwXdScRrMkpVYqX5tICpGYRu_AmnR7nxgQE0quMigP87s4T1E9X-db7dEGMhD85BAB_NUbFBqnbgfBNYHwVFFhp3w4kXMexC3_u6SUZzFWxbXsfXkBhLG58r_43fXWi1-7lnJ4kdj1faOcw6HM0om-4KzaQ5A5zVCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الرعب تدوي في عموم الأردن</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84482" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84481">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC0Z2-zcyNkzKSzdo5UBNiYhVbdLpP927Vj-Gfj8ZhICuNdFH_GmlhGLKX0_3LZTZVPPHTUt4w5W6uJELaRDJCXe0SJA12cqph62NZmwb-bK9CRYM1taMVgUKTuQB0Irb2yNsApmCwkiJzFP_QaRNVed15RWw3oUr-Pd8dwbJDarB1592pHlo4OJGZWpmxZ2RCMFdx6UfCe_3735LdJjgVHaysB6Ck0wGdWi1Jz-DlxldvS8TBr7BD4FIW0nNsn4PjvfzB6xSTgzjUM56LrU5IfcTHYg579EisIrDhpc-fPwC6B6eqQrUfJty-b-gY_Gwl6dghs-mNZvt5Audd4Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثناء انطلاق الصواريخ الايرانية نحو اهدافها</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84481" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">يا قائم ال محمد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84479" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84478">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8882bd7598.mp4?token=in22o7GVf32I2CzwoDhRXmghAIGSOfTDyVFaNpmmhPW-fWPmBeHSPHpSyD2ZK9vVnQ7mK0UJKFg5B5mn3Wl04lKQgQs3z1XaD51OiqTdJOOtiJ9eCABNcTTU8YHvJqhtqJjpNU8CdLLthbzlJeQbfZQKKy_9uqxu9cUvfZlgiSpEF6fhumxa7WSKIaN03vie0cCbI2ECxWVj1eOGHTiF6Gp3H3MYKybVYUx39qMzOG0WPhM623jJOfNv8eivp1UwT-oJb5dKkLm1IeI-_ZVWRd-3lvGu8pAK8A3jXYD1ZH85IV4GflCszWshV1OH2xtulqI2kaK2MQmq3EfYHO1wbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8882bd7598.mp4?token=in22o7GVf32I2CzwoDhRXmghAIGSOfTDyVFaNpmmhPW-fWPmBeHSPHpSyD2ZK9vVnQ7mK0UJKFg5B5mn3Wl04lKQgQs3z1XaD51OiqTdJOOtiJ9eCABNcTTU8YHvJqhtqJjpNU8CdLLthbzlJeQbfZQKKy_9uqxu9cUvfZlgiSpEF6fhumxa7WSKIaN03vie0cCbI2ECxWVj1eOGHTiF6Gp3H3MYKybVYUx39qMzOG0WPhM623jJOfNv8eivp1UwT-oJb5dKkLm1IeI-_ZVWRd-3lvGu8pAK8A3jXYD1ZH85IV4GflCszWshV1OH2xtulqI2kaK2MQmq3EfYHO1wbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفارات الانذار تدوي في جميع انحاء الاردن</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84478" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84477">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbb776333.mp4?token=sBl-YMj4LUIbyqzddGAamOhhIxGpyjNp9DbfXYJzI_Kj_cRwL5b0vHFGzAehwr_-yttqm74QfDNJ6AE279CMikNqhLVsBQNcc4O3iSAfeMNrEQiX9W6njZOmgQR6c1O4fg_ks7jKV5TxZjFgO3hVUqrouPAdGmSdiXsEP9wbb5ZVrRlvbORkrEkUjTMsMg8lDgcaLEWv3IWTvRBL2gueq7a3eSX7_p7dxCLsIvEf5uszsslMaOpD23d8BcXb_wRE98Td5ppnnKp5S8C5U-wE_wnto1Xf6bU-itsphcGx1kIpVHRoF_2ZPR7tEpdKsh4K0-I1PnRJbTS5NGOEddheuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbb776333.mp4?token=sBl-YMj4LUIbyqzddGAamOhhIxGpyjNp9DbfXYJzI_Kj_cRwL5b0vHFGzAehwr_-yttqm74QfDNJ6AE279CMikNqhLVsBQNcc4O3iSAfeMNrEQiX9W6njZOmgQR6c1O4fg_ks7jKV5TxZjFgO3hVUqrouPAdGmSdiXsEP9wbb5ZVrRlvbORkrEkUjTMsMg8lDgcaLEWv3IWTvRBL2gueq7a3eSX7_p7dxCLsIvEf5uszsslMaOpD23d8BcXb_wRE98Td5ppnnKp5S8C5U-wE_wnto1Xf6bU-itsphcGx1kIpVHRoF_2ZPR7tEpdKsh4K0-I1PnRJbTS5NGOEddheuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية تنطلق من قواعد الاحتلال الاميركي في الاردن في محاولة منها للتصدي للصواريخ الايرانية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84477" target="_blank">📅 21:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84476">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=nj942LwyIgzwmtcAUktWE3ti72C6QTNXXIANZb8UmWBM1dacre_wj3LFDfEqAZ4hI5xFLwTmaZ8gd_K-MbvNQmtM6Ac6GXY-LttOTY3DUS_SMUo74yt4FkDPoEW3U4Ohhn4TUS8K37su7srPwtl5KzI0qYuqtqKWpBzqbqDcOgsp-Z-8a16Exsgtfb1fQsezubpl9zW1-uWPAQrGPVE0yDLkeqvdtCg3Drpohu9-hmTno2UzS6ToWdD7plBdEouOKFKgPz7qpGuRTYyETFYo6B4Xd0icBvlytjLzoQJFvrcsUFsyRtw4wUfBujbkEJ9L94QgSaS-2dicTQaNmrM0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=nj942LwyIgzwmtcAUktWE3ti72C6QTNXXIANZb8UmWBM1dacre_wj3LFDfEqAZ4hI5xFLwTmaZ8gd_K-MbvNQmtM6Ac6GXY-LttOTY3DUS_SMUo74yt4FkDPoEW3U4Ohhn4TUS8K37su7srPwtl5KzI0qYuqtqKWpBzqbqDcOgsp-Z-8a16Exsgtfb1fQsezubpl9zW1-uWPAQrGPVE0yDLkeqvdtCg3Drpohu9-hmTno2UzS6ToWdD7plBdEouOKFKgPz7qpGuRTYyETFYo6B4Xd0icBvlytjLzoQJFvrcsUFsyRtw4wUfBujbkEJ9L94QgSaS-2dicTQaNmrM0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية تسمع في الاردن</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84476" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84475">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84475" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84474">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شاهد ١٣٦ بالميدان .. الان باتجاه قواعد غرب اسيا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84474" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=Lswqwt57sLuJAU3AA5JwUzkraU72lXtnz-wWQj7jaoipHxIF1_IgbP4AYabGz1waKSDDNo5vqLQyDffsQVdjkk0k3uiRfHHZC3s_94CwnrL2lCWLhqS7tCY3CQfSxrljP9sOa17IzjCTEF8kUzgSqvSk34Uhfr102beb79TbpRcIZ3coUwvEVccW2nt-vI0i7ob7uzoCnfNgR5f71tqy54ZAurlCFzA2ybVOoXojDi7qPqZ-KNR7TQ_6dQaAt4rfj-sMigZW9WGz5SyLe1RbA8zJY6bUG50Fuj-0mV9cv-UVQRkOTs7Rz4ByczB4qjJ8qcL1CWOfkA4QrPsB-l-XbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=Lswqwt57sLuJAU3AA5JwUzkraU72lXtnz-wWQj7jaoipHxIF1_IgbP4AYabGz1waKSDDNo5vqLQyDffsQVdjkk0k3uiRfHHZC3s_94CwnrL2lCWLhqS7tCY3CQfSxrljP9sOa17IzjCTEF8kUzgSqvSk34Uhfr102beb79TbpRcIZ3coUwvEVccW2nt-vI0i7ob7uzoCnfNgR5f71tqy54ZAurlCFzA2ybVOoXojDi7qPqZ-KNR7TQ_6dQaAt4rfj-sMigZW9WGz5SyLe1RbA8zJY6bUG50Fuj-0mV9cv-UVQRkOTs7Rz4ByczB4qjJ8qcL1CWOfkA4QrPsB-l-XbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهد ١٣٦ بالميدان .. الان باتجاه قواعد غرب اسيا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/84473" target="_blank">📅 21:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">يا قائم ال محمد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84472" target="_blank">📅 21:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84471">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe61c52d0c.mp4?token=Ysm4TKBcRMzw-ZnOFEamNTU6FVqpwkkUinl4gcV-GJORzu3fj56B5ejuy_akqV79DWV1nhefAtZba_Viro5PI-x1wjBuQf-k5yHNDbt1Pc7iqPglvvUofwmR5enE-Sxsx3vVtDz7-jgNZKcpQ0b7kXqnY41y3h3ouRhp_Vsz3UjMM88LlSEqYUPUS91E19FVz-sQEimYFoCDGQytdKF0JhBHul8vkMA3kpVamYvmYTE-9FdKrwnjVN_zWGNUG9PGWwv1dGKzgIz4dy8j0u9tXRFX5xJao7Ywd8JihgqXQKx5dpmZGXnvEzQl8QbHWTJEsTqws2RmwCcvkNH9iDPc4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe61c52d0c.mp4?token=Ysm4TKBcRMzw-ZnOFEamNTU6FVqpwkkUinl4gcV-GJORzu3fj56B5ejuy_akqV79DWV1nhefAtZba_Viro5PI-x1wjBuQf-k5yHNDbt1Pc7iqPglvvUofwmR5enE-Sxsx3vVtDz7-jgNZKcpQ0b7kXqnY41y3h3ouRhp_Vsz3UjMM88LlSEqYUPUS91E19FVz-sQEimYFoCDGQytdKF0JhBHul8vkMA3kpVamYvmYTE-9FdKrwnjVN_zWGNUG9PGWwv1dGKzgIz4dy8j0u9tXRFX5xJao7Ywd8JihgqXQKx5dpmZGXnvEzQl8QbHWTJEsTqws2RmwCcvkNH9iDPc4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اطلاق المسيرات نحو قواعد العدو الاميركي</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/84471" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84470">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بسبب مزاعم عن نقص حاد في عناصر الجيش الكويتي بعد مغادرة عدد منهم البلاد بحجة قضاء عطلة الصيف خارج الكويت، فتح باب التطوع للانضمام إلى الجيش الكويتي حيث لجأت السلطات إلى من تم سحب جناسيهم واعادة تجنيدهم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/84470" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84469">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9oNS-hPLRn_R4BWYJpmLSG8GE5Ds12CEL04mYXQI-xThJPJhTEBAjlkCwnaipzrHzwPW5ZM_1Ft49FUQvlvr5U9S2sDKVaw3WbRGfZ6hZSeY5E7wfwv_jJcgLrO7NAX5naN1AMTKSmA4Gu-wYK-pmHlcMsMKOzaN3cLSWPjz2nuKtomDuuPajliauoWo6rnXnGYfR8IAj4ora4b0-32zv1MiBiM2NPrDl0WTOYDbs4st1mijv5N0pMP-RgekMlqg2WfnKVbS1fXbWy4GLok3KaSUzag-5FEv0u7jbqDvUD5da_vHfcIJFekFeBSJvqqmkcRfdy5ie89Yd34vnTCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسبب مزاعم عن نقص حاد في عناصر الجيش الكويتي بعد مغادرة عدد منهم البلاد بحجة قضاء عطلة الصيف خارج الكويت، فتح باب التطوع للانضمام إلى الجيش الكويتي حيث لجأت السلطات إلى من تم سحب جناسيهم واعادة تجنيدهم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/84469" target="_blank">📅 21:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84468">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2G742n7xUqbMAVa5KuQBKWuB796Q73OCvZCyQxi8jdgHYg7-v9zbGDUTolf7AcN-atk_bW7PMhfWmJLwddZo4LE1XHyfLDpNNptU8lAPzV4QNOreWmcXBi2-Cy0TRFfJ_BzDg4t6eC1SsRl287KbgiQRX3k76cJjHmQ1jfQmJbVLnJEUDp0gf1mdaVCT0ic3qE-bNjfI53IGaHoYCiOlENM9NxyGCcV5vUx2BKmAsPzdMNMbMySyJ-VBo-j8yTgTpsKr0MRbr6trdeelVP8QPV1iBt8q__Hiz8ZypEWHcQgfrQ8U7uwT4kuze9voFcgH4aDoNc_JUjLiY3wYCDoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏هيئة البحرية: بلاغ عن واقعة على بعد 17 ميلا بحريا شرق دبا في الإمارت</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/84468" target="_blank">📅 20:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84467">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/84467" target="_blank">📅 20:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84466">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
خلل تقني يضرب تطبيق فيسبوك.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/84466" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84465">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تايلر جيمس فيهان من هاواي القتيل الثالث الذي قُتل بصاروخ ايراني بقاعدة موفق السلطي بالاردن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/84465" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84464">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
مصدر أمني لنايا  تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/naya_foriraq/84464" target="_blank">📅 20:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84463">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0TCY_pb6TBHEgWEnPxFIShCgVEHYStKx9_-aWwDxzUCUqW9GCHa4FVh_IURb5X8a7m-n6_yZvMBybcwpkqxGZib2HA5yfxynJIcBNJB1jkCnjrah55x3_Wix3lTtYNW_zp7oSmjv0ufki_CqP37h8-sfXpxTOE5YDR9kE6qSCiiKjGs0WVUa5a4gvbJtmHH51cKQAjQyFOqXRkWwJ5jKWPJ4BWnws0421t-V6QS0j-emZwppTBCcqxESq9ra9S1BMRbXHtPbMqQn_v7oEuBu3zy9GK1Vnq3H8gyQVCD05xpJKdJTOLirGpk3cFAM_V6mxzN9Ipkl9sPhO-u2JoDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
‏من المرجح أن تكون السفينة "شين وي يانغ" التي ترفع علم سنغافورة أول اختبار حقيقي لحصار أنصار الله البحري على السعودية، حيث أنها متجهة إلى ينبع.
‏يبدو أنها عطلت جهاز الإرسال والاستقبال الخاص بنظام التعرف الآلي (AIS)، ولم تظهر تحديثات الموقع منذ ما يقرب من ساعة.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/84463" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84462">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
مصدر أمني لنايا  تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/84462" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84461">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAX7Pwk9wvIkCzGz6dM79rcuWcoqwcWpSRJ6FLyy4pDovrC3mrxHpvJoIC-nplyBACoB87n9Z2NwEB_KGqTjOvTzPa-x7Wk17BD8iW5gH2KKkRw9YJ7qWqxGDbd5K_B48APhX4Pg0n9a63bTou1M4RT5mEvdYvLmzxgmrGneEssNTKa4cp34VFrjWItTNZgMLMkQeTmjFDIh5L7FoKYu1Tihrm5VZQkjqZnk2fmUZ3KeG-HGXkNOx3tPoJfFzV_llV1H0jls2ymFKVcNgGZIhMidvOjCVo3wJTzrVbPEt-TaCLLe9YzGtruJOPgm-1g9hn5SirXoE2DvaHT_lmmUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ترامب:
لن يُعتقل بنيامين نتنياهو، بأي شكل من الأشكال، أثناء وجوده في الولايات المتحدة الأمريكية. إنه يُحارب الجمهورية الإسلامية الإيرانية، التي قتلت مؤخرًا 52 ألف متظاهر بريء، وأمضت السنوات الـ47 الماضية في قتل الجنود الأمريكيين وغيرهم. الوحيدون الذين يجب اعتقالهم هم من قادوا إيران إلى هذه الدوامة غير المسبوقة من الموت والدمار، وهو أمر كان ينبغي على الرؤساء السابقين معالجته منذ سنوات! الرئيس دونالد جيه. ترامب»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/naya_foriraq/84461" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84460">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
الأمم المتحدة:
تهديدات انصار الله باستهداف الملاحة البحرية قد تؤدي لتصعيد إقليمي أكبر.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/84460" target="_blank">📅 20:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84459">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
مصدر أمني لنايا  تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/84459" target="_blank">📅 20:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84458">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP1RyQvC15ICrs0IoI6sZnFFzr-6rCoA6Ypf8UAIDhddJUS_UhCb-PF-DY4PtQXx8nHnU3OUg3p9nx7L5BsWMYK-CqSA-HZNIUTwL9Zod89snQYId9rYAnBvtt88kB3sLQlBjxgWQ8Ei0Fu1Dv1IryHONtAJUaV2dS2s2pxMYGSOxsQgI3DbjItFjD326I6vaUbIqHmjgGf_TEqzLGCPDTaX4kMpMddUypbjRloHf9u4QGSNf6ZsMR1kmUGgzf584g5ag3vqxY7U8DRwyIxNVrtvXmOyWI1_j4EnMI3pV8Ryt51PxIefldA_NIndNpD58eWUBlxDvh0gXF6rQ5Ky_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كون العوز يفشل
ترامب كلما قتلت ايران جندي امريكا سوف يزداد دفعها الثمن .</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/84458" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84456">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
مصدر أمني لنايا
تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/naya_foriraq/84456" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84455">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IatWxGBkmFGKjcQ3fX0jvGtBh4e2aDG5R-uZQtD7zTO5EQQVw10852SUMvJkFdKriMrLMArvthf9nDe8p8nJsqjB_psfkeSoIMskLkRK6iJBChluYUdHRH37QSiy4S6teNUiw_iDrNr8SpEjgSUD5uy0p8TOUchsvXvggkXrPA5SM4KDj8U1G37fFud6CQ0IbhNODJIOe4OS3kenbVgc0-ZpEylC3iEdr675QYe0avCIyJMDIV9hPCJLon9HQ584wrKHunik1Mdifk2QmjMNwmJI7Gawbkm327BIFUYG4MQenO7Uo0puaDxH7JkDR1C7k8mhIB7onopr6WAKEKKspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
هيئة البحرية:
بلاغ عن واقعة على بعد 17 ميلا بحريا شرق دبا في الإمارت</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/84455" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84454">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veGh7O8jN7_eUiqiGrLVg1BWi35FTaOl53wNQIHuj1NlXpsaYpDSUdBqS41Y2gN8IDJDEFIxt3frGCr9zVY3uhAyYK4kGf9ihklBvX5SevNgi-i7qzMegqjPJF8Y-tDwhzzMh0kqFFNg2HIL1b9hdgM70uuAjHpCWJAyLMEjTkMAJz1qwg7BWhHvdp33y5yb_imJsLBZRaOzhytFJtodoUZe-FWi7l8Jmys0uNhEGoghVPKBywDXKIck6pwAPBkuUiMNVVnA6_ZzUxSZ0X4A-QCmZvogsbJ1imhSzpJbXIfxPHjPPpR2KG78sWa6o3HrjAXtwX4_gtJqDpgwx1D0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/84454" target="_blank">📅 19:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3cc01cd85.mp4?token=Nn4o2Df4aooaBpg23CNYGP0qQmdNPhOYFP9T-AaPMmpij_uvjM3CjAFCnXbEQlopC-URsaUA311C7cwtDMDhRCGMGsORbeoxsj0mGbwIsRxJqy42B81D-RG6MWqe77-ldSnJjggYa6JBS5zAnfSJsVohIjseytO0QijgZQP29gEXKGa15UHIlRCDvx-UAEBRGTI3_tLs4yRltR7brdEK3CLSplkMu84OTps4nhC25H9HUfNrH-xc8A_iaViJNs1ao-IuhKaPOOwddGewQbC98pU5PxgBAXhLoXWftGYMYdc8ML98UJcxhe2OY2C4uQZT7MSRF0U8shvzBEKj7dg8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3cc01cd85.mp4?token=Nn4o2Df4aooaBpg23CNYGP0qQmdNPhOYFP9T-AaPMmpij_uvjM3CjAFCnXbEQlopC-URsaUA311C7cwtDMDhRCGMGsORbeoxsj0mGbwIsRxJqy42B81D-RG6MWqe77-ldSnJjggYa6JBS5zAnfSJsVohIjseytO0QijgZQP29gEXKGa15UHIlRCDvx-UAEBRGTI3_tLs4yRltR7brdEK3CLSplkMu84OTps4nhC25H9HUfNrH-xc8A_iaViJNs1ao-IuhKaPOOwddGewQbC98pU5PxgBAXhLoXWftGYMYdc8ML98UJcxhe2OY2C4uQZT7MSRF0U8shvzBEKj7dg8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ فتاح ١١٠ البالستية يتبختر في سماء خليج فارس</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/84453" target="_blank">📅 19:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1bbZxmrS1WZRduLt8TQVdazzqnUBWSP7rL3vuj8ITtvk9OSQIKxoWoBmZN0eLgPdEfOiY7vXMDZxuaSLG4_L-foNJCDlRvQYM6uK_cKXC9siA0oQDeiSxWoUyNVpwNgDL13bnO9-EaIs19lePZ5FnSu5OjZ1t71HC3gb2VA5vqZ6WvUzS1tzWsMHO7GAL0VrmNZxb6Iah3ICAICSZOk8ryPMWVP7HsBr5BPoXigSkEDOC6keRnjKEl_4EsWbYC9sFjTE7MycO4jc-J3wRnCWfgYljLBe8Z5ratDXAbwNzOHnxbtxJGcZVfneC55n8c-mO49lQ2ZPCGcpUod0X1T4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صاروخية إيرانية اتجاه القواعد الأميركية في غرب اسيا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84452" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
