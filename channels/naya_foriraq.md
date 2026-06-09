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
<img src="https://cdn4.telesco.pe/file/PGqyEqUtd610dwLFnQxhjIAX8EZDXSSnPsmic5sQp4kiXpSxBFjnoLFjOZna8MCyfIlIijoEg8AMlvqfBAGLBwD-WedCcKluuXbRpS1-IpWmAD04ONSs3wfoKYwLntoqxOqOg1rGbMZj6FqWoppj-w7VryBayZSoSN9NV4YtYbmtCJnbweab0h6ZVDmf-ZTnCKzciRV5cn9xpa4GtaXlMWNP1HWjwhdxXMna5gjLinBLcHQR0Q4RHHWXzgSmD-wtBfTzesCGUeLZDKb8olSrl0iX4sRVdypmLYKgxsrFji2MOw4b9DXMDRyvnbnG622dV3PtoQVyaTbhdgfkWILkJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
قادمة من اقليم كردستان..
هيأة المنافذ الحدودية تحجز 13 شاحنة في محافظة كركوك تحمل بضائع مستوردة تم تزوير الباركود الخاص بها الى محلي.</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/naya_foriraq/77869" target="_blank">📅 13:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77868">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
الوساطة الأميركية بشأن أوكرانيا متوقفة حاليا.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/naya_foriraq/77868" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
وكالة إرنا:
بعثة إيران أكدت أن الوكالة الذرية هي التي أوقفت التفتيش بالمنشآت النووية عقب العدوان على إيران، إيران تعد مشروع القرار الأمريكي الأوروبي ضدها في مجلس محافظي الوكالة الذرية مسيسا واستفزازيا.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/naya_foriraq/77867" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bawIlm0zBYWaD0wt6ibWQyW9t4N3wrXDebRTpREci4Qp4AZscKE318tQuwIoJ6is39D22y8RHtkTUdWZc1YdkijazsLOjkm7r9xaspZfTSU8PR1ZmhwEEgN9uAvt22EhjwS58snYht-cHsLDsv6g5eM4yXduhPKS1by5EuZrJ7ruwD_aK63dcu0cspOVjYlmiyFal03C09KWkY_LJFAZgG7q4yGrN1AA_fWIQlbZHeky1Y0m2BeKkezXl5NN8ML099UbLH4txFYKTqQRKYOFaGoJSNVoVGOpSqcvlS_0N8N2bdJdRao-UACP7o7JYE1n-U0m4wQlrozlZEyND3rQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
الشيخ اكرم الكعبي يحيي الجمهورية الاسلامية وابطال اليمن على تأديب الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/naya_foriraq/77866" target="_blank">📅 13:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لجنة تحقيق رسمية للأمم المتحدة:
السلطات الإسرائيلية متورطة بشكل مباشر في هجمات المستوطنين التي أدت إلى قتل وإصابة وتهجير فلسطينيين في الضفة الغربية، في حين أن قوات الأمن الإسرائيلية توفر الحماية للمستوطنين. وأكد التقرير أن السلطات الإسرائيلية سمحت لهجمات المستوطنين من خلال دعم مالي وعسكري، في ظل أجواء من الحصانة من العقاب التي خلقتها أنظمة القضاء وإنفاذ القانون.</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/77865" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇱🇧
بيان صادر عن حزب الله حول الرد الصاروخي الإيراني على الكيان الصهيوني:
إنَّ الرد الصاروخي الإيراني على الكيان الصهيوني دفاعًا عن شعبنا اللبناني هو رسالة التزام أخلاقي وسياسي وميداني من الجمهورية الاسلامية اتجاه لبنان بعدما تمادى هذا العدو بغطاءٍ كامل من الإدارة الأميركية في ارتكاب جرائمه ضدَّ بلدنا، وعاود استهداف الضاحية الجنوبية، في إطار خروقه المستمرة  لاتفاق وقف النار بما يؤكد استخفافه بكلِّ الاتفاقات الدَّولية، ولذلك جاء الرد الايراني للتأكيد أنَّ مصلحة استقرار المنطقة ودولها هو بذل كلِّ جهد ممكن كي تُصان الاتفاقات وأن يلتزم بها العدو الصهيوني قبل غيره، وهذه هي الرسالة التي أرادت إيران أن تبعثها بوضوح وقوة إلى كل المعنيين بجهود دعم الاستقرار في منطقتنا. وقد تزامن مع الدعم المشكور من حركة أنصار الله في اليمن في إطار العمل المشترك لردع الكيان الصهيوني وإفهام الإدارة الأميركية أنَّ دعمها للعدوان الصهيوني على بلدنا سيطيح بكلِّ الاتفاقات التي تسعى إليها خصوصًا في ظلِّ إصرار الجمهورية الإسلامية على تضمين أي اتفاق معها وقفًا شاملًا لإطلاق النار في كل الجبهات وبالأخص في لبنان، كمقدِّمة لفرض انسحاب العدو من أرضنا اللبنانية وعودة النازحين وإعادة الاعمار وإطلاق الأسرى.
إنَّ هذا الدعم الإيراني لحقوقنا المشروعة، وتحمُّل تكلفته الماديَّة والسياسيَّة يؤكد مرَّة جديدة أنَّ ايران هي من تساند لبنان وليس العكس، وذلك انطلاقًا من مبادئها وقيمها الإنسانيَّة، ومن عمق العلاقة التاريخية بين الشعبين اللبناني والإيراني، فإيران كانت على الدوام تريد الخير لبلدنا، وأسهمت في دعم مقاومته  لتحرير أرضه وفي إعادة إعمار ما هدَّمه العدوان الصهيوني، وموقفها المشرِّف إلى جانب لبنان يستحق من سلطته الشكر وليس التنكُّر والإساءات المتعمدة  استجابة لإملاءات خارجية، فكلِّ الأصوات المدفوعة بتلك الإملاءات  لن تؤثر على صدقية هذا الموقف الإيراني الشجاع والوفاء النادر في زمن تغليب المصالح على المبادئ، فالاتهامات الباطلة التي صدرت عن بعض جهات السلطة ضدَّ الدَّور المشرِّف لإيران الساعي إلى وقف العدوان الصهيوني على لبنان، مرفوضة بالكامل لأنَّها تجافي الحقيقة وضدَّ مصلحة لبنان،  فالتهجم الظالم على إيران بما في ذلك البيان المشترك مع العدو والإدارة الأميركية ضدَّها هو خارج عن كلِّ قواعد العلاقات الديبلوماسية واصطفاف مرفوض ومدان، ولم يخدم سوى العدو الصهيوني.
إنَّنا ندعو السلطة اللبنانية إلى اغتنام الفرصة المتاحة وتصحيح علاقتها الرسمية مع الجمهورية الإسلامية بما يخدم مصالح الدولتين، والاستفادة من هذا الدعم الإيراني من أجل تحقيق أهدافنا الوطنية خصوصًا على ضوء تشكُّل المظلة الإقليمية الجديدة المنبثقة من مفاوضات إسلام آباد، وبذلك تتمكَّن الدولة في لبنان من خلال مفاوضات غير مباشرة مع العدو، ومستندة إلى تلك المظلّة وعوامل القوّة التي تشكلها المقاومة وصلابة الموقف الشعبي وثباته والتفاهمات الدَّاخليَّة من تحقيق مطالب شعبنا في تحرير أرضه وعودة النازحين وإعادة الإعمار وصون السيادة الوطنية.
إنَّنا في حزب الله وباسم شعبنا وعائلات شهدائه والصامدين والنازحين وباسم كلِّ حرٍّ وشريف في وطننا نقدِّر عاليًا هذا الوفاء من قبل ايران ونحيي شجاعة هذا الموقف النبيل للولي الفقيه ولرئيس الجمهورية والحكومة والبرلمان وللجيش والحرس الثوري ولأبناء الشعب الايراني على وقفتهم المشهودة إلى جانب حقوقنا المشروعة وقضيتنا الوطنية، وهي الحقوق التي سنواصل الدفاع عنها من خلال مقاومتنا البطولية حتَّى تحقيقها مهما غلت التضحيات ليبقى شعبنا على أرضه يعيش بعزَّة وكرامة وحريَّة.</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/77864" target="_blank">📅 12:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">إطلاق صاروخ أرض جو على طائرة حربية صهيونية جنوب لبنان
وإسقاط مسيرة فوق جبل الريحان الآن</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/77863" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8a2MXVivfeBhZmt-n8t4LYsD9IkC5GaKzdAnD9sc7-6FgrP-8P_bunA_Flzs8xJlkyLeESVl-fS7uhue5twE-WWIB41TQFt6aOQRu2W0zW8vAOm8m02wIV7TMt3BWkTqbwA-xEpJZsBtRSH1vcrC0cxqxoNe04jxbzEOgCAvKq_CUld8XvFuRE_dV8elfNst5_CF6zTpTwGJd2Q_kltS58YXVwZGgoa7RZu2GcHh6_zt2qjX-eAvglAKygXQus7sWq3uPVdbXhbAw5mMGDfxKnlQtN0ZtigR5TTJd-5FonSVcw4fnkkun6nkkn5LZHVkaVw-e0icZfPLc0ettvy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف صهيوني لسيارة على طريق المصيلح جنوبي لبنان</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77862" target="_blank">📅 11:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adf9e6a56.mp4?token=ZH6IuNOzu6xoGqn1e3HOlgCudoFOqyNSHe812lCUBpFIQFrvD9arShZofyIa17OtgPK2aC4fE8Hs35nRyQU7kBtD6rKfB_M53e0T0km2Hn95UFqE1VGS8LZVMcTuMgEV94KdRh9unZ7R7fWjYaR_KslN0S6H3uvPCYn7QGHwsxJlhWuu7rznLjRH075SYKs4RfDho3kwlwuNiMg2Xs7PWPGUYzw_8vjoNPFoQfX__bq3rgkIUzoTf6wGRF7_VUjQw2uWj0xREfWJzHOIE99RsL5YNO-WkDadK-CQns6Q2O1NjkaWutqjHKiBST30zrk67uVAnVL9FoEcBmrS_DOpaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adf9e6a56.mp4?token=ZH6IuNOzu6xoGqn1e3HOlgCudoFOqyNSHe812lCUBpFIQFrvD9arShZofyIa17OtgPK2aC4fE8Hs35nRyQU7kBtD6rKfB_M53e0T0km2Hn95UFqE1VGS8LZVMcTuMgEV94KdRh9unZ7R7fWjYaR_KslN0S6H3uvPCYn7QGHwsxJlhWuu7rznLjRH075SYKs4RfDho3kwlwuNiMg2Xs7PWPGUYzw_8vjoNPFoQfX__bq3rgkIUzoTf6wGRF7_VUjQw2uWj0xREfWJzHOIE99RsL5YNO-WkDadK-CQns6Q2O1NjkaWutqjHKiBST30zrk67uVAnVL9FoEcBmrS_DOpaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترامب ظهر على الكاميرا أثناء عزف النشيد الاميركي، يتعرض لهتافات استهجان عالية في قاعة الغناء اثناء حضورة لنهائي مباريات احد الرياضات.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77861" target="_blank">📅 10:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbc31aabd.mp4?token=V3fRKX9YvetEdnNUfgc9mdSJzgp1coo2OIbvFV447dmzMAjgwr9aqOIz3C74H2O5TbdhLgEiJ_JPtxNiE3sQjCVjMG1KNWkOha7MygojtsKnIjwyxke8byFfJeGL3aDsszRg-iF7J2owDA-aF-uYuDvzMk-8mOP6o0o7xuR5dF2Ue7PuZWzbVqES_zt_oUOkYOqDU_kRtyvZrIfrl-dqzlB6XPcX7i3NilWDQoao68Qrgo2D5yozthEFH3fnS8jpoMF_ZPKVe9vEyk1A9HUWgRVSTtc73WovcFObAC2lWLRQ1gm6gmSQbaExoTSGbAqht5a7GHyXq5fNou1mss6tXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbc31aabd.mp4?token=V3fRKX9YvetEdnNUfgc9mdSJzgp1coo2OIbvFV447dmzMAjgwr9aqOIz3C74H2O5TbdhLgEiJ_JPtxNiE3sQjCVjMG1KNWkOha7MygojtsKnIjwyxke8byFfJeGL3aDsszRg-iF7J2owDA-aF-uYuDvzMk-8mOP6o0o7xuR5dF2Ue7PuZWzbVqES_zt_oUOkYOqDU_kRtyvZrIfrl-dqzlB6XPcX7i3NilWDQoao68Qrgo2D5yozthEFH3fnS8jpoMF_ZPKVe9vEyk1A9HUWgRVSTtc73WovcFObAC2lWLRQ1gm6gmSQbaExoTSGbAqht5a7GHyXq5fNou1mss6tXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل طلبت من نتنياهو ألا يرد؟  ترامب: لا، قلت افعل ما هو صحيح، لكنني أريدك أن تتوقف بأسرع ما يمكنك لأنهم يجب أن يتوقفوا.  كان ذلك يتعلق بلبنان ويجب أن يتوقف. نريد أن ننهي ذلك.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77860" target="_blank">📅 10:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ab89cd65.mp4?token=hUNki83OzULepjtNHstYUpf6tBpqS4BDde0xQ0Qw-DUBxo0ZZegAtwP8XmKElCHJZW2nLJqZkDYRtzxgRR5sWAjFPBW0TpLzib3Ot5sZNF55KlSY3yLwRxWANT3qtVx-CES6uiHQoYoTrac1MUxE0tUNuHUa_Fta6OCQgh1LQFXfc4c_SS3r3Xr9i9V-yw4kNr224aZBSyVQYMmLX7NVPBN16THIJKa0oSyNcoXH29gvX9nLgB1YwIApzINVfIGKbpbr_TTZ5Hx2dbKrcGVQg93Yvmtj9hqxn1WxBGm0huvkgc8hw54zNM5h5LGrYBuux0tvf97hZsfiudpnMYom-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ab89cd65.mp4?token=hUNki83OzULepjtNHstYUpf6tBpqS4BDde0xQ0Qw-DUBxo0ZZegAtwP8XmKElCHJZW2nLJqZkDYRtzxgRR5sWAjFPBW0TpLzib3Ot5sZNF55KlSY3yLwRxWANT3qtVx-CES6uiHQoYoTrac1MUxE0tUNuHUa_Fta6OCQgh1LQFXfc4c_SS3r3Xr9i9V-yw4kNr224aZBSyVQYMmLX7NVPBN16THIJKa0oSyNcoXH29gvX9nLgB1YwIApzINVfIGKbpbr_TTZ5Hx2dbKrcGVQg93Yvmtj9hqxn1WxBGm0huvkgc8hw54zNM5h5LGrYBuux0tvf97hZsfiudpnMYom-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب بشأن إيران:  إذا ذهبنا وقمنا بالقصف، وهو ما يمكننا فعله بسهولة كبيرة إذا أردنا، وقضينا أسبوعين أو ثلاثة أسابيع أخرى في القصف، فلن يتبقى لهم أي شيء على الإطلاق.   لكن لن يظل المضيق مفتوحًا لأشهر. اه، إذا قمنا بالقصف، فستُقتل الكثير من الناس. من يريد أن…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77859" target="_blank">📅 10:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامب بشأن إيران:
إذا ذهبنا وقمنا بالقصف، وهو ما يمكننا فعله بسهولة كبيرة إذا أردنا، وقضينا أسبوعين أو ثلاثة أسابيع أخرى في القصف، فلن يتبقى لهم أي شيء على الإطلاق.
لكن لن يظل المضيق مفتوحًا لأشهر. اه، إذا قمنا بالقصف، فستُقتل الكثير من الناس. من يريد أن يفعل ذلك؟ أنا لا أريد ذلك.
وسيكون لدينا - سيكون لدينا وثيقة موقعة تكون في الواقع أقوى من القصف.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77858" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs1kH1gh91eR57CxwzlJRqB4y6aerfBWd1OcfY0gdwywoAyjgOwIly8cp6-fsuqWAhc8T7Q-IoZ54lhoIca6Na2q3HJ3KR9ySKeq1-5I0qrg4teR_S9x259hphsLIolIpoGib9lMxmocLKXuWXb8vGVnqwA3rY_YmGLohu3sP4G5Oy0smbBGME-KCWlYho1NbBFwke0jrSOM6VDCY200IYj6fG3uEZsao0OtKTRsYQ-L5l6A1ctj5glOiomlmU4TmdCU1EMbCfAeJj1eVLu_ZgG0B24RnqmoRyLPoB8jRhq0yvJyVthoTwIIm8CUvMwjJwvcRHw0bVE0q5i_ZivZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
سي إن إن: كم مرة ادعى ترامب أن الاتفاق مع إيران "بات وشيكًا"؟
- أعلن دونالد ترامب منذ بداية المواجهة مع إيران ما لا يقل عن 37 مرة أن التوصل إلى اتفاق "أصبح قريبًا"، إلا أن هذه التصريحات لم تترجم حتى الآن إلى نتائج ملموسة على أرض الواقع.
- ويرى محللون أن هذا النهج يمثل "استراتيجية فاشلة".
- ويعتبر أن ترامب، من خلال المبالغة في الترويج وتكرار الوعود غير المدعومة بنتائج، أضرّ بمصداقيته الدبلوماسية.
- كما أنه بات عالقًا في محاولة الحفاظ على صورة "صانع الصفقات الكبير"، بهدف طمأنة الأسواق المالية وإظهار نفسه بمظهر القائد القوي، إلا أن تكرار هذه الوعود جعل المراقبين الدوليين والرأي العام أقل اكتراثًا وأكثر تشككًا تجاه تصريحاته.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77857" target="_blank">📅 10:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇱🇧
🏴‍☠️
تجدد الغارات الصهيونية على المساكن في قضاء صور جنوب لبنان</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77856" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">إذاعة الجيش الإسرائيلي: لدينا قيود على الهجوم في بيروت ولكن ليس على العمليات في جنوب لبنان</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77855" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVzIJ6D22GztOqic162ifWZ9WHvtmNC_1UY-YGxMfaQYCHHgxJN1BeITjloN3eFrCovEq_pcA1WVuKFtw_JetM-00Hv8Q83ax8lN_nrKbWbJ_DcH2-in3C5PaKwBbQodvy866uR3yRSC2a7q6aiPbS_GGNnYFpji3fRzRVWiAm_c4hxB7sP9uhNwLw7k3tAGO0jOhV44Wph3zpZjsgl_ZuIDFEgsHwEcPfk50XjlTcdQB0pPAD5k1TZhDqwQXaUeuTqd7eLtK5I9uF09kAPgC92k2BKbGXskm1kAUfbzRiyGAt45QsKcn_6WUt0WMmiLGpgM-m7phrIfTCxpkwFZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انفجار عبوة ناسفة في سيارة بالقرب من حي بالاشيخا من موسكو.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77854" target="_blank">📅 09:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203541429e.mp4?token=cCAS_bStt_9e5qfyjkPxLNeTJvK4HPwFXbCt2vmTX_Lcgm7PHNvo5M8gZWYSkrFMU0R-lJ-fxhMRzFkJl6k8UbVzEok3JbuLp_RL2YSRhaSQrn-9lye4lFcZJL57Lpr9KRYtQZEaIL61XPvTp_b4NUX7IAKehAXPdx8C-44JlqaNAuYzHazxbAugNx1ouuNfhEEZ_muHzMyjOsRCiv6hgrp_cHvOTuPuS2x7GcKySTMcSPL6DtVEKQ7FJjBgu5juEB3T9deIQycqpdQW3tw-8rnR879A_QenbYUzWvppRntm8FhZgGIiZcOevDvNBnjEmScW97KCDEQLeoBez_Hsew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203541429e.mp4?token=cCAS_bStt_9e5qfyjkPxLNeTJvK4HPwFXbCt2vmTX_Lcgm7PHNvo5M8gZWYSkrFMU0R-lJ-fxhMRzFkJl6k8UbVzEok3JbuLp_RL2YSRhaSQrn-9lye4lFcZJL57Lpr9KRYtQZEaIL61XPvTp_b4NUX7IAKehAXPdx8C-44JlqaNAuYzHazxbAugNx1ouuNfhEEZ_muHzMyjOsRCiv6hgrp_cHvOTuPuS2x7GcKySTMcSPL6DtVEKQ7FJjBgu5juEB3T9deIQycqpdQW3tw-8rnR879A_QenbYUzWvppRntm8FhZgGIiZcOevDvNBnjEmScW97KCDEQLeoBez_Hsew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثار الغارات الصهيونية صباح اليوم على بلدة دير قانون النهر في قضاء صور جنوب لبنان</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77853" target="_blank">📅 09:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67efdca0ce.mp4?token=mkM_gojHqtLoKT9EsJ_FqEUuF63n-YS-5POq-wJMDzJDoUo4ehMcL1yD3PFOlO83hdBL6NtZqZSLA_AMVM4SAOG2nFpgLIJGTuAcaLXZgTwpntoADiVQmfxa8G5gX80pqZApNLhFKrAREac0OwR2S_Qkg0K5OA5aHBPJjQ55lK8co4yy8kjRk1B8-09WPxopmQaRTijEw8LOAdVlrz21oRZfQc_QViiQDjVOQkIulYnqwFgGJFDlManKnlreKMkPxbwigAAzXj6VlDELNxpvW3t9Lu3jALAcJb-XVn3AqWkjCxxbECpYtE89iU1OGLUlJFgKMiKax0k3WJ-uGpzY0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67efdca0ce.mp4?token=mkM_gojHqtLoKT9EsJ_FqEUuF63n-YS-5POq-wJMDzJDoUo4ehMcL1yD3PFOlO83hdBL6NtZqZSLA_AMVM4SAOG2nFpgLIJGTuAcaLXZgTwpntoADiVQmfxa8G5gX80pqZApNLhFKrAREac0OwR2S_Qkg0K5OA5aHBPJjQ55lK8co4yy8kjRk1B8-09WPxopmQaRTijEw8LOAdVlrz21oRZfQc_QViiQDjVOQkIulYnqwFgGJFDlManKnlreKMkPxbwigAAzXj6VlDELNxpvW3t9Lu3jALAcJb-XVn3AqWkjCxxbECpYtE89iU1OGLUlJFgKMiKax0k3WJ-uGpzY0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثار الغارات الصهيونية صباح اليوم على بلدة دير قانون النهر في قضاء صور جنوب لبنان</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77852" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترمب: تحطم مروحية أباتشي أميركية قرب مضيق هرمز أمس الإثنين وإنقاذ طاقمها</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77851" target="_blank">📅 08:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: المحاولة الإسرائيلية للفصل بين إيران وحزب الله تواجه صعوبات كثيرة وما حدث بأمر من ترامب</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77850" target="_blank">📅 07:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
‏إعلام أميركي عن نائب ترمب:
لن نتورط بحرب طويلة الأمد مع إيران.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77849" target="_blank">📅 04:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64615b9230.mp4?token=D34gPxi7XeF9QMced66FynUwwucbHJU2uzmUty25TLJ-nntMnzjYu2LOdw3oRE6D7-Y-KFz55lQ8oIsBOxTb-_z3SnKzjZlatR3vQ7U9MSh_gYXlw9DERWa-VfQLfsVVc8sEdNYX96a9YewzAShki1oEyC04BLoWoiYlTwjLLfo9m8Q5qy_VRKdxRpsMq9tgVOP--Hp5lR5fglMvE8qZo67Sbu3dojjWr1Ltp25b7Ud_S4PzfASs8mDGDMhHxMmyQSJos3Lu040C5LtdAoGfLKZx5XctGLSfRjsMlA52e_-4UhbfisGMZafmBBqUmvjaAy1DSzZU6RjSzYZ7fyr-SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64615b9230.mp4?token=D34gPxi7XeF9QMced66FynUwwucbHJU2uzmUty25TLJ-nntMnzjYu2LOdw3oRE6D7-Y-KFz55lQ8oIsBOxTb-_z3SnKzjZlatR3vQ7U9MSh_gYXlw9DERWa-VfQLfsVVc8sEdNYX96a9YewzAShki1oEyC04BLoWoiYlTwjLLfo9m8Q5qy_VRKdxRpsMq9tgVOP--Hp5lR5fglMvE8qZo67Sbu3dojjWr1Ltp25b7Ud_S4PzfASs8mDGDMhHxMmyQSJos3Lu040C5LtdAoGfLKZx5XctGLSfRjsMlA52e_-4UhbfisGMZafmBBqUmvjaAy1DSzZU6RjSzYZ7fyr-SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترامب ظهر على الكاميرا أثناء عزف النشيد الاميركي، يتعرض لهتافات استهجان عالية في قاعة الغناء اثناء حضورة لنهائي مباريات احد الرياضات.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/77848" target="_blank">📅 04:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLjgGhZC0LtFDZjJeauttZxPM7wpvjkysiAZUG48eE1_VOvkRMmYln6mnHVNJSgxe7eVs9S8aQ4nOmsYwE9DwbwQV8DSdz-8uZTqaXfP6xXPxKHxkbmqWUwmxVWiSL5AMGzyD0mGq3gjpe39sVgDwiwYwjgYFUJVK9Zz7rZ9TsdLYiaChHpcW0WHmxOWXyGUextM5S1YCxXzG8oPA-sm5_qOYT4toAHJRIP8GVqRpl1W3do99vv_lpaZ0o6E2tGKaZLo1O6WTwDpLw7JpKtaTy_bnOdejEnWBmm8OsNGUBMk3I39kPmIHl0O77E7UbEaJ_h9H4mw5Ab4Dpww71WATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏شهدت نهاية هذا الأسبوع عمليات نقل نفط سرية كثيرة بين السفن في الشرق الأوسط. ليس هذا نفطاً إيرانياً، بل نفط قادم من دول الجوار العربي لإيران. وهذا سبب آخر لعدم وصول سعر برميل النفط إلى 200 دولار حالياً.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/77847" target="_blank">📅 03:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
عقد الإطار التنسيقي اجتماعه الدوري في مكتب سماحة السيد الحكيم، بحضور السيد رئيس مجلس الوزراء، لمناقشة الملفات المدرجة على جدول الأعمال.
وبحث المجتمعون الشأن الحكومي، وقدم السيد رئيس مجلس الوزراء رؤية متكاملة لمعالجة الأزمة الاقتصادية، وعددًا من الحلول التي حظيت بدعم الإطار التنسيقي، ولا سيما المقترحات الخاصة بمعالجة أزمة الكهرباء، وتفعيل قوانين العمل والضمان الاجتماعي دعمًا للقطاع الخاص.
واتفق الحاضرون على إعداد ورقة باسم الإطار التنسيقي تتضمن أهم الملفات الوطنية، وطرحها ضمن ائتلاف إدارة الدولة للاتفاق بشأنها.
كما أكد الإطار التنسيقي وقوف جميع القوى السياسية خلف الحكومة نيابيًا وسياسيًا وإعلاميًا من أجل إنجاح برنامجها الإصلاحي، واتفق على ضرورة الإسراع في إكمال الكابينة الوزارية في أقرب وقت ممكن.
الإطار التنسيقي
الدائرة الإعلامية</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/77846" target="_blank">📅 02:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
تعليق رحلات مطار الإمام الخميني بالعاصمة طهران حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77845" target="_blank">📅 01:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
النائب الأول لرئيس البرلمان العراقي يدعو الحكومة إلى وقف تحويل الأموال لإقليم كردستان لحين إجراء التسوية الكاملة للمستحقات</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/77844" target="_blank">📅 01:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
ترامب بشأن إيران
: نحن نتفاوض الآن، وإسرائيل لن تعود إلى الحرب مع إيران</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/77843" target="_blank">📅 01:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
زلزال بقوة ٥ درجات يهز أجزاءً من محافظة هرمزكان الايرانية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/77842" target="_blank">📅 01:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff02235e2.mp4?token=DheqfoRNaAvQCaPf5gsdkLrso6QN3FYnRSzSFfDg7jtp31eb1RDC-vGx0zZgkr-nIJjuxa2Z9n0jnrrKMJ7cYMldlgUoaRuhf2eTj-Qo1Vpwo-rb8jffFUg5Yw_JB5KntbuDUfu7djz7qQqqbWmqlBgiwgtMHZHA2V6GBukh8kHr-3pniCxdGcs60CguCwd4Xzv5gh3Gquc4E0ilSJrIHYPVoU0om5WyzuHp2WTRHNh9Xs1z7JUJUYmbSsyYLHs9HhcBadd6_1D8gt_s429VZ8xCmi9rSEf-Z41uIHIQUSjYy_yWjW2jE7Xy1rjvVwRj-5hLfYMYB0avTe_dn9YQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff02235e2.mp4?token=DheqfoRNaAvQCaPf5gsdkLrso6QN3FYnRSzSFfDg7jtp31eb1RDC-vGx0zZgkr-nIJjuxa2Z9n0jnrrKMJ7cYMldlgUoaRuhf2eTj-Qo1Vpwo-rb8jffFUg5Yw_JB5KntbuDUfu7djz7qQqqbWmqlBgiwgtMHZHA2V6GBukh8kHr-3pniCxdGcs60CguCwd4Xzv5gh3Gquc4E0ilSJrIHYPVoU0om5WyzuHp2WTRHNh9Xs1z7JUJUYmbSsyYLHs9HhcBadd6_1D8gt_s429VZ8xCmi9rSEf-Z41uIHIQUSjYy_yWjW2jE7Xy1rjvVwRj-5hLfYMYB0avTe_dn9YQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
😆
محولة كهربائية في محافظة ميسان جنوبي العراق تحاول الانطلاق نحو الجولان للمشاركة بالقصف على المحتل في فلسطين.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77841" target="_blank">📅 01:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇱🇧
🌟
المجد لسلاح المقاومة المفاوض الوحيد للشعوب المستضعفة في المنطقة ..</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77840" target="_blank">📅 00:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4d39775b.mp4?token=N5Sj2MVYUYtG8jlUscZuCz-yw0mbrJKd6ZtIZL-dm-yTC0CHUojQgshqdn3SXlVPCi-W-vufQrtH7t_l3NOHKJ7UI9HRN2FMwD7m2DSwQYndJdvFp6eQNS9MjGgmnxIvS1bm8tfz2O3tzf85BwYSoCfSMmU-9krpdlYB441wdnoql9SH1d97ByknwOkmw0_NwxOkROHR6JbfoCNAq1agVcYlsH6OhmasnBXlNF2Td6jDagK2JEmF9H0wma4r2KNi-aj0RiNGSlnvPngBoB9wP2-OWBGwSTaowA8aZbqnbm6S1HMId2GFIDRW97YF8v-TwzU5-O_YBkmOEC7XGJR_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4d39775b.mp4?token=N5Sj2MVYUYtG8jlUscZuCz-yw0mbrJKd6ZtIZL-dm-yTC0CHUojQgshqdn3SXlVPCi-W-vufQrtH7t_l3NOHKJ7UI9HRN2FMwD7m2DSwQYndJdvFp6eQNS9MjGgmnxIvS1bm8tfz2O3tzf85BwYSoCfSMmU-9krpdlYB441wdnoql9SH1d97ByknwOkmw0_NwxOkROHR6JbfoCNAq1agVcYlsH6OhmasnBXlNF2Td6jDagK2JEmF9H0wma4r2KNi-aj0RiNGSlnvPngBoB9wP2-OWBGwSTaowA8aZbqnbm6S1HMId2GFIDRW97YF8v-TwzU5-O_YBkmOEC7XGJR_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اخرى لانطلاق المضادات الارضية لمحاولة التصدي للمسيرات فوق ايلات</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/77839" target="_blank">📅 00:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e745845fbf.mp4?token=b49TwsOnsVfypBZfxzS9CCDi5AIZPw9K6oX0WJ8NDbpMWEOXyDIL6o4DHVsQ2MmaLHhL_gxZT3VpJ5rJrgaFuWOVW6zC9nRzSl8tVYEHtTj7YLW1a8rush74z3it4UT7o5i9sX9KD-RtsaYBZRhMDyB1u-hDASXBWFw1XwyOcAZgTNLeuY7TlIwEbZgKCAxifBOrjv3wLxFGKy5SqVJbRa2hcjzsio97L3l_Q6vyE_BF4r2cGG4Y2t7hprdGAKG5RH2HnQJBVwFBUlqE9I8eLCBBlDHi4ehVXLxPDnuAxUgHbPnKGweTHFX23RbWRcSeySUqwXr0PuY3tS3eeThNfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e745845fbf.mp4?token=b49TwsOnsVfypBZfxzS9CCDi5AIZPw9K6oX0WJ8NDbpMWEOXyDIL6o4DHVsQ2MmaLHhL_gxZT3VpJ5rJrgaFuWOVW6zC9nRzSl8tVYEHtTj7YLW1a8rush74z3it4UT7o5i9sX9KD-RtsaYBZRhMDyB1u-hDASXBWFw1XwyOcAZgTNLeuY7TlIwEbZgKCAxifBOrjv3wLxFGKy5SqVJbRa2hcjzsio97L3l_Q6vyE_BF4r2cGG4Y2t7hprdGAKG5RH2HnQJBVwFBUlqE9I8eLCBBlDHi4ehVXLxPDnuAxUgHbPnKGweTHFX23RbWRcSeySUqwXr0PuY3tS3eeThNfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات المضادات الارضية تنطلق لتصدي للمسيرات القادمة من اليمن في ايلات</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77838" target="_blank">📅 00:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17295a8332.mp4?token=mtx8-2_d0j0dku09oa2jCF9N2eIndF8J6gVs5Q6UYrOq4J13QAStfb7H6nKn-vi_t3HKNbC4_kZAXQo2COZ-aZkFBly150w5kYjT5XYoq5oFcJU8QSNOszuyW9D4IQ3Hx21r3RLsX2OtaWUJVYZJLvn-jWnm_ja-cQ4c_zqkj7IUbj7sRSKmK9P-FaLyfB1hX3By7Hi_kUOnFnaaAUzI_NpvF7hxOIE8gKQDS3A7nozQUw4_vhuAvx1fkGBRyntRJje6rLixqR48_F2g0btTCtYYusznIZ8RGE7YlYiulTvW2PhF-6aoYj4HZlM2M6uvR1ayRO3uwnk9oF2FGsJWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17295a8332.mp4?token=mtx8-2_d0j0dku09oa2jCF9N2eIndF8J6gVs5Q6UYrOq4J13QAStfb7H6nKn-vi_t3HKNbC4_kZAXQo2COZ-aZkFBly150w5kYjT5XYoq5oFcJU8QSNOszuyW9D4IQ3Hx21r3RLsX2OtaWUJVYZJLvn-jWnm_ja-cQ4c_zqkj7IUbj7sRSKmK9P-FaLyfB1hX3By7Hi_kUOnFnaaAUzI_NpvF7hxOIE8gKQDS3A7nozQUw4_vhuAvx1fkGBRyntRJje6rLixqR48_F2g0btTCtYYusznIZ8RGE7YlYiulTvW2PhF-6aoYj4HZlM2M6uvR1ayRO3uwnk9oF2FGsJWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الصهيونية تحاول التصدي للمسيرات القادمة من اليمن فوق ايلات</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77837" target="_blank">📅 00:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcd9f0ba7.mp4?token=kEQTu3nFntx-n-eVmslGTODfn2SmtYKAIkEDEWWfdFnksL02y_QHL3wo0kWWDfN5HTI8-JqIutD7Zwi0Kbi1yLmzYL1yojhE4hbFwtspbSmevBtwNnCH49bp1Xs-ZeRj_s8wVtjvS0x2aaNUGAv19FbPBumACGxqZA8lN8iIj6c4HP_x9KE_ueyOZMabd0koIjoyUBykIT5biuIcIDcvtAtT6j7NueF8Ef7xEy6CBHPUwF6bbMnQ4D4ThCHWWWDDDZn6XbEf5WEryBjnZlpVoDNO0UVIIo0nHIfgJ0Cy6TZDsNZbT9dz_TlEifKuVA1BPlJhZdTx-_hfsGJBzQXTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcd9f0ba7.mp4?token=kEQTu3nFntx-n-eVmslGTODfn2SmtYKAIkEDEWWfdFnksL02y_QHL3wo0kWWDfN5HTI8-JqIutD7Zwi0Kbi1yLmzYL1yojhE4hbFwtspbSmevBtwNnCH49bp1Xs-ZeRj_s8wVtjvS0x2aaNUGAv19FbPBumACGxqZA8lN8iIj6c4HP_x9KE_ueyOZMabd0koIjoyUBykIT5biuIcIDcvtAtT6j7NueF8Ef7xEy6CBHPUwF6bbMnQ4D4ThCHWWWDDDZn6XbEf5WEryBjnZlpVoDNO0UVIIo0nHIfgJ0Cy6TZDsNZbT9dz_TlEifKuVA1BPlJhZdTx-_hfsGJBzQXTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مسيرة من اليمن تدك معاقل اليهود في ايلات</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77836" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">طائرة مسيرة فوق مستوطنة ايلات جنوب فلسطين المحتل.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77835" target="_blank">📅 00:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
‏الأدميرال براد كوبر قدّم إحاطةً للجنة الدفاع في مجلس النواب حول أولويات العمليات العسكرية الأمريكية في الشرق الأوسط، على أن يقدّم إحاطةً مماثلةً لمجلس الشيوخ غداً.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77834" target="_blank">📅 00:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يخترق شمال فلسطين المحتلة وصافرات الإنذار تدوي.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77833" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77832">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يخترق شمال فلسطين المحتلة وصافرات الإنذار تدوي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77832" target="_blank">📅 00:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77831">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭐️
هزة ارضية تضرب الحدود الإيرانية العراقية بالقرب من مدينة حلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77831" target="_blank">📅 00:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77830">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCLgTEZ9H4AG_MwkjgUTpPTnticwW6NXzzlGP3CNcGMCJX7iSTAUqvd7CJKoHm8T78-63kpuFPmlWAmGGAejHpeaN-BC2MmrgtXT4-SUzstWrO0YNSLoW0qEOz6pBbPeXfxaX9oXyLFbVtqoJZgDeTv8B7IuaWbmlxTpzFHbtJIzgERIpr4Z7lzfiJJ4q11BYQoELFPMClNCgHVw_zVwq6MEeGjsgCnAHGMJXgYArhByghByNhhGc9kBd0HJtgkwzD4nxjh45sdiMaiquKlbU3KY_tqtE29yATTN2_qHOutuScHytE4mZvwnvlkIVOmoUUYBj9UU0A-Ne_uVA0miWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد القوة الجوفضائية لحرس الثورة الإيراني "السيد مجيد الموسوي":
حافظوا على وجودكم في الشوارع ما دام قائد الثورة يشاء، واسعوا جاهدين، من خلال ربط الميدان والشارع والدبلوماسية، إلى إبعاد العدو عن مسرح مساعيه اليائسة، واستعادة كرامة إيران والشعوب الحرة وسلطتها.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77830" target="_blank">📅 00:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77829">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
مسؤول إيراني:
لايمكن التوصل لأي اتفاق إذا لم يتم الإفراج عن أموالنا المجمدة ورفع العقوبات.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77829" target="_blank">📅 23:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭐️
سماع دوي انفجار في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/77828" target="_blank">📅 23:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سند المرياني يكشف عن كارثة كانت قد تحدث على غرار سرقة القرن و الجميلي</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77827" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77826">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLLD-85mL0jQqS38jDLlEdk8HZSvxt2Gwr-EZdwICQWawHP3xCK9HcgpwaYuSTl9CW_9dSQlXo7RV6ESdEmsda--g2T5G_hmH4oDnwcUJuJ13bDKVvUlD9veb1YoKOjWrJktbzQ4rk_TDFSk-AOuqp-m4VeCRi9Zu0SxlL9E15-6Yw9XMxpky0jLhxvH65hl-aUKEcQeQhfAVUYQCZaY4cRuPpkaxLrXwFNFYUBPAC8T11wbG3LvkDUp57H2B6FKSNUiO5hvLCLSBQFDk4dvUd8EWFO-4Ghmhw17-y8RGnHIgQTCGwIZSkHDCnb1FrCKqIn3A-BjeInxzkzqJ806xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سند المرياني يكشف عن كارثة كانت قد تحدث على غرار سرقة القرن و الجميلي</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/77826" target="_blank">📅 23:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f2de4e02e.mp4?token=h83I2P_OQBYTrGC9xpeWA1BONFxrFjIEp35jVnDmsemopQzHhII07AIaz9UHuqKBoeUVay1qqzUPI8gIBeeC_C0r8Rw7AHHG4K8t6QLZncALyhjHJmliSWfTvNPy2R8oZBurWEVlhNyqybcWyqBPgh48YP6jjvisLNBBDib3Vmz4_kpgMgNTMN0QyN5NTHJz0BEmaa6GKXdjrFIDmCePqZTBLkHAYXlutraoiyaej94DEhF3FZv38O_hLyO6YeNUvbbMcc-3ps3uaSNqou6UmVAfY6XRMHQerEaFxtWcPBN0B4h5nJmSR76inWYBoLGkKcqXimhE7oOhLpEPABsDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f2de4e02e.mp4?token=h83I2P_OQBYTrGC9xpeWA1BONFxrFjIEp35jVnDmsemopQzHhII07AIaz9UHuqKBoeUVay1qqzUPI8gIBeeC_C0r8Rw7AHHG4K8t6QLZncALyhjHJmliSWfTvNPy2R8oZBurWEVlhNyqybcWyqBPgh48YP6jjvisLNBBDib3Vmz4_kpgMgNTMN0QyN5NTHJz0BEmaa6GKXdjrFIDmCePqZTBLkHAYXlutraoiyaej94DEhF3FZv38O_hLyO6YeNUvbbMcc-3ps3uaSNqou6UmVAfY6XRMHQerEaFxtWcPBN0B4h5nJmSR76inWYBoLGkKcqXimhE7oOhLpEPABsDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
إطلاق صواريخ اعتراضية نحو جسم مشبوه بالإضافة إلى تحليق مكثف للطيران المروحي في سماء إيلات.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/77825" target="_blank">📅 23:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15678c4648.mp4?token=NxNY8Xbc5oflK4xNkLaLbmTsgk9qqMB6fhbmywBqPEF1JHrV4G_e9zgKKcmEnGx722DdglYOgkoG3VKaS4ZYkNJcaPsnpwc5D6SyEjO0JBbRyHCCcRXTuHeyQQWYWr1cwMm7NCyCca3LSZ5szUHCtMs8m_Ap0-W1m78wnO5O31gj7EUJDsf2o8C4Vcgf8Msgw5ITq-g51sXmhd3Wk29A-8lIb7M-sXlwor7Ynj27ug08C57jEE9TwO3iTz3Y2wNzj3XdLYYSGbXMFhcrnMOPERE9ZXgopt7d5lnIrewW1g92S7rtmD4N3OSu-n9hIow-OqFT3_RmurOnRmxoLogyVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15678c4648.mp4?token=NxNY8Xbc5oflK4xNkLaLbmTsgk9qqMB6fhbmywBqPEF1JHrV4G_e9zgKKcmEnGx722DdglYOgkoG3VKaS4ZYkNJcaPsnpwc5D6SyEjO0JBbRyHCCcRXTuHeyQQWYWr1cwMm7NCyCca3LSZ5szUHCtMs8m_Ap0-W1m78wnO5O31gj7EUJDsf2o8C4Vcgf8Msgw5ITq-g51sXmhd3Wk29A-8lIb7M-sXlwor7Ynj27ug08C57jEE9TwO3iTz3Y2wNzj3XdLYYSGbXMFhcrnMOPERE9ZXgopt7d5lnIrewW1g92S7rtmD4N3OSu-n9hIow-OqFT3_RmurOnRmxoLogyVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ الباتريوت الأمريكية تحاول صد الهجوم في سماء سوران بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/77824" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb8864df0.mp4?token=qEKg523bgEwuJfE3z27JzQYMZhjukGXSvtB7C5q-YELrQRSlsL1REE_iadnZXWBrLPzee54fmkAtNcEFckh3GohKI1bmhIwgcWlyv7BfMhAWZCB5fpug6XuF2AhM0IPIr6WXo9ooHK9RBeVpZ38atNFIBk1534ZJQYXViwTkpC9B2juH8HqaUE8-d0rcqXf8aXv44NdNCogv9UrsGFIAIic9BMaJsHs3QzsJPVinFOGGsw9quNM3FlP52xqKC6CNpVZ2VraEYcn7MRSSChQtrP0TQsFcL8WThQ7VqmC8pAWHr2Y3xJbO7XMstO8tKYHVzwbegJ_wF-qNn50doYhj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb8864df0.mp4?token=qEKg523bgEwuJfE3z27JzQYMZhjukGXSvtB7C5q-YELrQRSlsL1REE_iadnZXWBrLPzee54fmkAtNcEFckh3GohKI1bmhIwgcWlyv7BfMhAWZCB5fpug6XuF2AhM0IPIr6WXo9ooHK9RBeVpZ38atNFIBk1534ZJQYXViwTkpC9B2juH8HqaUE8-d0rcqXf8aXv44NdNCogv9UrsGFIAIic9BMaJsHs3QzsJPVinFOGGsw9quNM3FlP52xqKC6CNpVZ2VraEYcn7MRSSChQtrP0TQsFcL8WThQ7VqmC8pAWHr2Y3xJbO7XMstO8tKYHVzwbegJ_wF-qNn50doYhj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالتزامن مع الإنفجارات ،طيران حربي كثيف يجوب سماء محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77823" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a03fe0ac73.mp4?token=tI48SsluGiWsJaaa8wcuqS0MSrR7y4kp58XJlvrLhOMP2YSP3LcbjBqZKjtJXiXCCXaBp_fIW5NCDYIYGZ3lFav1w3JY7_UbwZbU1V9trjJcpsKCcEJmA4AIKRPfr2LyTmG1taz-ud6yuf-aawcoXl2IcdLwvub20izxuhWnzpUJtW89ATNGmXb-MDlpzd4-4JEDejTG8Gnvx1e3T53nz2nitkMQsdMbrp0dNvxAZ-0Mlx7IGnZ64mkA9r0m4TeLRyeenUr1hSaws1kByI1zfosmyM9pe8YT80lnCB1F4pI-7MPM_ntCiehL0oZjKuls7QuxfulhTLbGlDb5MfRFsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a03fe0ac73.mp4?token=tI48SsluGiWsJaaa8wcuqS0MSrR7y4kp58XJlvrLhOMP2YSP3LcbjBqZKjtJXiXCCXaBp_fIW5NCDYIYGZ3lFav1w3JY7_UbwZbU1V9trjJcpsKCcEJmA4AIKRPfr2LyTmG1taz-ud6yuf-aawcoXl2IcdLwvub20izxuhWnzpUJtW89ATNGmXb-MDlpzd4-4JEDejTG8Gnvx1e3T53nz2nitkMQsdMbrp0dNvxAZ-0Mlx7IGnZ64mkA9r0m4TeLRyeenUr1hSaws1kByI1zfosmyM9pe8YT80lnCB1F4pI-7MPM_ntCiehL0oZjKuls7QuxfulhTLbGlDb5MfRFsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تشعل سماء قضاء سوران في محافظة أربيل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77822" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc5defa8b.mp4?token=WuUhHnLLMSb5kaTuKXzvju0WVG9cX1OCjBpOaAaTwSaQJ14vEUlKToBzSTXV7LUApQUFd6-r1kr13_nTOYvKCZ_h6809AvNmaFTweoE11125B9L3l9FWWQ11JADAuBh_wrQa0ubbopiuu1w-TpmSWQ3zO-nyc77pdCE2l656qlKnXbFOTmsVOjJQTKeOK9U3kcMMGD9ot_O-scXKTBu7lFV3HE4JlP0Kyw9VeKMhC5bNjH7bqlqUf2TKSE9wT-9RpKS5j6_rDA5VDUKaEPNOjeci9-pILegmvbV784yMsnVopLicY1dXh5uRLbfVkJd98WcDPchhp6eHNkHLc8wNhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc5defa8b.mp4?token=WuUhHnLLMSb5kaTuKXzvju0WVG9cX1OCjBpOaAaTwSaQJ14vEUlKToBzSTXV7LUApQUFd6-r1kr13_nTOYvKCZ_h6809AvNmaFTweoE11125B9L3l9FWWQ11JADAuBh_wrQa0ubbopiuu1w-TpmSWQ3zO-nyc77pdCE2l656qlKnXbFOTmsVOjJQTKeOK9U3kcMMGD9ot_O-scXKTBu7lFV3HE4JlP0Kyw9VeKMhC5bNjH7bqlqUf2TKSE9wT-9RpKS5j6_rDA5VDUKaEPNOjeci9-pILegmvbV784yMsnVopLicY1dXh5uRLbfVkJd98WcDPchhp6eHNkHLc8wNhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ تتجه نحو مقرات المعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77821" target="_blank">📅 22:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b65e5bfd.mp4?token=gwfNntGW7pLkGC6rUA-DxyR16rzLv4_5Rxb7J_btExKh_MXgZcEzxpxhLFOTKil4RDj7adjCIhvo82B8W5IRufOBUPP5dV4Zo0d7KIcwu-glPPTCHCQSK_nhefTgC2XWXj-BA-czRouXLsuAkr0afU2iHXXrfS1BWYKjCCIIz7aRdt4HVwA-UXiThTb4oitat5uX9xcll7qTWnmzq74qeHPxv9AFW6g6CA4DeCteNRfB_H1PWKTjfG3neioJZBOAnXxnULrvfHSMQet_2I08QlROHl_prHiRPrb6CNzV86B3DtRpa-SmzxwTp2NVnkLDHEAOwE0_2kAgXgpJ4TrTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b65e5bfd.mp4?token=gwfNntGW7pLkGC6rUA-DxyR16rzLv4_5Rxb7J_btExKh_MXgZcEzxpxhLFOTKil4RDj7adjCIhvo82B8W5IRufOBUPP5dV4Zo0d7KIcwu-glPPTCHCQSK_nhefTgC2XWXj-BA-czRouXLsuAkr0afU2iHXXrfS1BWYKjCCIIz7aRdt4HVwA-UXiThTb4oitat5uX9xcll7qTWnmzq74qeHPxv9AFW6g6CA4DeCteNRfB_H1PWKTjfG3neioJZBOAnXxnULrvfHSMQet_2I08QlROHl_prHiRPrb6CNzV86B3DtRpa-SmzxwTp2NVnkLDHEAOwE0_2kAgXgpJ4TrTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ تتجه نحو مقرات المعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77820" target="_blank">📅 22:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5c84ad1e9.mp4?token=luHIkyirrPGRxdJ7fKZHDFB6Ne88E1p4iYqvrGT1IR4peDlFxsWRDIiSlGH3B9_aHDM9RmuI4zjLWxWW4IPym0d9YGWTNo-nXbDNpDL1zAW_mmYTDR8T2MoK0uCr-BVjjHxQ3Cx3YyGt98toLWzCsDdZTpo6g7kdeFpi6Jq2iVGGEE1P1zu_YytKf33M0V6i4iGxAsr0PWL5Vdv1vNYWPEC2Q_9U0W46q0cxV2J87q2_OjNswmMVJ79RUb2DXC9cnK0MovI_sZdWRYH__tlWWI0PJ3I8ZKfypjRBHn0zd3GqrgybdGId7Zlf_pDwpJmov5KfNPuOujG7aUmV_JwhhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5c84ad1e9.mp4?token=luHIkyirrPGRxdJ7fKZHDFB6Ne88E1p4iYqvrGT1IR4peDlFxsWRDIiSlGH3B9_aHDM9RmuI4zjLWxWW4IPym0d9YGWTNo-nXbDNpDL1zAW_mmYTDR8T2MoK0uCr-BVjjHxQ3Cx3YyGt98toLWzCsDdZTpo6g7kdeFpi6Jq2iVGGEE1P1zu_YytKf33M0V6i4iGxAsr0PWL5Vdv1vNYWPEC2Q_9U0W46q0cxV2J87q2_OjNswmMVJ79RUb2DXC9cnK0MovI_sZdWRYH__tlWWI0PJ3I8ZKfypjRBHn0zd3GqrgybdGId7Zlf_pDwpJmov5KfNPuOujG7aUmV_JwhhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مقرات المعارضة الكردية الإرهابية في قضاء سوران بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77819" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a0bb5b0b.mp4?token=b8mYxQq4DhX9oKCZBElh-uuPla5VNcYDsVm33vzaCmWICjTCugoIR-vf7mvUqj6vfldAe7iYDBz1J1wWaLp5y9k3Ge9Ol4kLVMTHkgzBUoAwu3HmdCaCoajL47gNYeRZ1xK9CfWNUo_dQD3chJhw2QQam0b0b_TR2utFzTAEnHstNioOB37x_7t9yAxsbXPN-6f0FunWho7CmiQVC20A183-sWAvQ3TOglL4Huswup0RHJzlMaMse2OpRMD6aPQPaXbVJNZPG4plZS9l6sjTE_D-z0sodPfe31kTa5CMnuzXxms6aPZbtdYDjaJXKIb5S94sy-hFt0Miwgb5rWaZrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a0bb5b0b.mp4?token=b8mYxQq4DhX9oKCZBElh-uuPla5VNcYDsVm33vzaCmWICjTCugoIR-vf7mvUqj6vfldAe7iYDBz1J1wWaLp5y9k3Ge9Ol4kLVMTHkgzBUoAwu3HmdCaCoajL47gNYeRZ1xK9CfWNUo_dQD3chJhw2QQam0b0b_TR2utFzTAEnHstNioOB37x_7t9yAxsbXPN-6f0FunWho7CmiQVC20A183-sWAvQ3TOglL4Huswup0RHJzlMaMse2OpRMD6aPQPaXbVJNZPG4plZS9l6sjTE_D-z0sodPfe31kTa5CMnuzXxms6aPZbtdYDjaJXKIb5S94sy-hFt0Miwgb5rWaZrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء قضاء سوران</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77818" target="_blank">📅 22:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6edd1eb9.mp4?token=udo12Ax6SkelMdGrxPvYgbCT95f-aPbPIQv_1B9bOeW_RWqkkiecjpoAA4vq4AZ4QB5pNqkN2cNvXO814qB5xde5jbIIRKt3VI45I-XXhvFO_ulFkRqaHDnluhiZ3iT_9QfXdxp31z-kKjV9z1Lb6w7QIqasUKUJ6TYXe5MGxRAQTIGJjGWsaSgLpZME_q4MGfG_aOmVVXQjdORGU4dPMNR5clYJtXylxy7xRP5uqbm1Pe8BbwqpdhZMLGjuf2zn0AU1hrOg6s1kceXBBonNA4XBmCwAHBZ1yop4Xrl5E5gRN1NYvS1IvhBVPfCudbTcdOivCMRDJEoisO5H8txUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6edd1eb9.mp4?token=udo12Ax6SkelMdGrxPvYgbCT95f-aPbPIQv_1B9bOeW_RWqkkiecjpoAA4vq4AZ4QB5pNqkN2cNvXO814qB5xde5jbIIRKt3VI45I-XXhvFO_ulFkRqaHDnluhiZ3iT_9QfXdxp31z-kKjV9z1Lb6w7QIqasUKUJ6TYXe5MGxRAQTIGJjGWsaSgLpZME_q4MGfG_aOmVVXQjdORGU4dPMNR5clYJtXylxy7xRP5uqbm1Pe8BbwqpdhZMLGjuf2zn0AU1hrOg6s1kceXBBonNA4XBmCwAHBZ1yop4Xrl5E5gRN1NYvS1IvhBVPfCudbTcdOivCMRDJEoisO5H8txUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77817" target="_blank">📅 22:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوي انفجارات في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77816" target="_blank">📅 22:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
حدث أمني في قاعدة "فورت ستيوارت" العسكرية بولاية جورجيا الأمريكية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/77815" target="_blank">📅 22:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
ترامب:
يجب على قائد الأغلبية في مجلس الشيوخ، جون ثون، أن يطرد فوراً البرلمانية، التي تعامل الجمهوريين، وكل ما يدافعون عنه، بشكل فظيع! تم وضعها هناك من قبل قائد الأغلبية في مجلس الشيوخ آنذاك، هاري ريد، وباراك حسين أوباما، هل أنا بحاجة إلى أن أقول أكثر من ذلك؟ إنها بقايا سيئة من ميتش ماكونيل (رجل أثبت أنه غير مخلص للغاية لجون ثون!)، الذي قرر الاحتفاظ بها لأنه كان يحب إعطاء تريليونات الدولارات للديمقراطيين، لكن بالنسبة للجمهوريين، بما في ذلك الجدار، حيث اضطررت في نهاية الأمر إلى "الالتفاف حوله" لبناء أكثر من 1000 ميل، وإغلاق حدودنا المفتوحة، لم يعط أي شيء! هي معروفة باسم المتعصبة اليسارية المتطرفة التي تخدم الديمقراطيين، وليس لديها أي احترام للجمهوريين أو الأيديولوجية الجمهورية. في الليلة الماضية، على سبيل المثال، حكمت ضدنا بشأن مقترح كان سيتم اعتماده بسهولة، وكان يجب أن يتم اعتماده، من قبل أي شخص آخر. لدينا كل الحق في تغييرها، ويجب أن نفعل ذلك، على الفور. طالما هي هناك، لن نحصل أبدًا على قانون إنقاذ أمريكا الذي نحتاجه بشدة، والذي يجب أن يتم اعتماده ووضعه موضع التنفيذ الكامل!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77814" target="_blank">📅 21:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_46c90Iz4ci62AIfh59YIRq1Kc0FpPEEsv1ZvjKDgITdnqI6Dd0URzHzmbnDHKU5NTfSaQEcmhv3H2pvTu1m-iT6nNS9-ipjCZQXn94l0keFXzTedytJAa5kniK8PbRr0Yf-vrrmMbgpXK4qYwhAzjMDHI_oDKN-EMaf1f8s8Vgu9nAuZEc_M-VDWgJF9_OslE_icvWkI098TTn3Lh_FLBzl3_-R-j3vPTQUaVcdtDD_ITRRn18Jc3C_RW3tVwL7iLJxBMqN-t3iCNMgA4QPDFsXDjsy6v60sJZSToidLRgGRQfKK_ax0OVMtwJhmxz8vmMT2_hSuY0vTUThMkPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇱🇧
"زينب سليماني" كريمة الشهيد القائد الحاج قاسم سليماني تنشر صورة لوالدها والشهيد الأقدس السيد حسن نصرالله مع عبارة "معا إلى الأبد".</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77813" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWkakkM6f-lVRz8qU728w21E5977x-LWXv1X3A2Ym-ddbNJCIre_swVa2ZENiHDxv17OkMnoe5EEJAFYmiLf1eetMfMEkl_Nr3ihNZK9ZHVLlkIX9T_0amjejFwLS4Wfwn3zISqzdizf4aLgW1pIwkmoBADy7jjHyMIGH8CwoFqyLjzHo_WmOj508AQ49hX7rGM8uN_Be4aqTZmrT6yJzPufgGCrqEXh5MX_mAIAhCybFDTpB3_O-_jbEjBvfzigBrXAng9p0nysU7C9EXUS2_HwZnPb9pgeCYp0SsWrekRxU5G2gr1X3xz4buZLTWFTJEOHfh5E1UaJ9gKkXoR1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري الإيراني اللواء "إسماعيل قاآني":
من مضيق هرمز إلى باب المندب، ومن الخليج الفارسي إلى البحر الأحمر، سيُقام حزام مقاومة أمني جديد. إنّ التحرك السريع والحاسم للجنود اليمنيين الأبطال يُظهر ذكاء جبهة المقاومة. وإذا لزم الأمر، سيأتي غيرهم. إنّ شرور الكيان الصهيوني وأمريكا في هذه المنطقة ستُقابل بردٍّ من جبهة المقاومة الموحدة. إنّ المقاتلين بلا حدود يُراقبون معابركم. استمروا في الهجوم، وسيُطبقون عليكم.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77812" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKeFP5LxvgwdqCIebAsvAWdlOsXc5u0TjAolhA4cXjt86gEUAGQQwSVR4Rl-K2Mf9xYBIWvHNZKrrEKThsDDqrQsndddvepWtVKPqv3Veqw7LVxsQNNp5Wa86FAvb153mhdJwmnUXrISuoXdfr-oVMKnt07rcPbhgJ4jGtSojdRTSEbzDeKJ_87dLIa7p_iowxSYUPv1t_6hj9q4vhS10frNIzPNI4FzEnbK0dnXrgUueyQ5gEhT9YFgPlErxoS6C-3No3cNGROs5GboJdrEk8evkcG80_J01-7E0cWJK7Xf-6I-QDPq4Dizw-CgckjXQ2YvVVyqhm1cyj-udV-CzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQ0Mz1lOwHg41uGd1f66NZRRqwBuQdHa3Sw_pISpRw5ji8nLNGgRXORcpWeYKJeId38LnkBaa36v3KOKq_fVHhah7XU9MP8WwDuKkhKk8ASxW5AQwIpQyg_Wf1H6N11aTnMkBDwThd7nUjHLgGc-gbY4htq127vSs3CWJDjrtFDiX53jZ6ybpr9CSu4sW7sSYiNjNzpQ7A6cUI78UpD5mVZ98OmquM7gHD8sUYE_HRa5WbRsjLgV2yZdwY0T3ctUHbyQEoEbzacu1iPswoEyvTgUmabor6QIfqsVL-utYhBFyTC1OIjKCihAxzZGHLdjUWbi97odJKLtmTP-OI3EQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtgbwDKc6FTbH8u-DwwO3TByPerJX4m70if5eBPi0RKIaGD9P4oDP8k_neV4W063_Un_NnIiUq-_8S7hkTvHtE68ew-8LZxWXlHtX2CTkxrx1bANVKL8G_Zlqg4LNsoxQzqozeKJJH6d0nfyJf4MkrnouxG-hiadBgtwMMikbnN5CngTPrzdAQ520IiHOMLWkt2CTkLa4Ip87jr7xDCggFXKeQGbyMBOz7fpPu-7qF5wSRaQTT5e1RH7m0pdFj3P0qAACN09PBCy6ZJKgBgXN-1bMAD0QkYHQdTZ_5RKSOwluZAocPkGPwhpxRc9VPTFsfqrzBwtBwG3-yuMm6UQcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصدر من الحرس الثوري لنايا   تم اطلاق ٨٣ صاروخ و عدد من المسيرات على شمال فلسطين المحتلة استهدف مطار رامات داويد و عدة نقاط في الجولان و الجليل</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77809" target="_blank">📅 21:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
قاليباف: هدف المفاوضات هو إنهاء الحرب وإرساء أمن مستدام، وليس تطبيع العلاقات مع الولايات المتحدة.  نحن لا نريد أن نتقدم بالاستسلام ولا بالشعارات، بل يجب أن نبحث عن نصر مُهندَس بقوة وعقلانية إيرانية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77808" target="_blank">📅 21:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
قاليباف: لا الدبلوماسية تمنع العمليات العسكرية، ولا العمليات تمنع الدبلوماسية؛ إن المجال العسكري، ومجال الدبلوماسية، ومجال التواجد الإعلامي، ومجال خدمة الشعب، كلها عناصر متكاملة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77807" target="_blank">📅 21:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
قاليباف: كان انتهاك وقف إطلاق النار والحصار البحري سببًا للتوترات الأخيرة. أؤكد للشعب الإيراني أننا سنواصل من الآن فصاعدًا الدفاع عن حقوق الشعب الإيراني بكل قوة. إن تصريحات الرئيس الأمريكي بشأن مذكرة التفاهم تخالف بنود الاتفاق، مما يدل على أنهم لا يسعون…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77806" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
قاليباف:
كان انتهاك وقف إطلاق النار والحصار البحري سببًا للتوترات الأخيرة.
أؤكد للشعب الإيراني أننا سنواصل من الآن فصاعدًا الدفاع عن حقوق الشعب الإيراني بكل قوة. إن تصريحات الرئيس الأمريكي بشأن مذكرة التفاهم تخالف بنود الاتفاق، مما يدل على أنهم لا يسعون إلى وقف إطلاق النار ولا إلى الحوار، وكان ينبغي علينا الرد بحزم للدفاع عن حقوق الشعب الإيراني، وقد قامت قواتنا المسلحة، بفضل الله، بواجبها على أكمل وجه. أؤكد لكم، أيها الشعب الإيراني، أننا سنواصل من الآن فصاعدًا الدفاع عن حقوق الشعب الإيراني بكل قوة، وبقيادة وتوجيه المرشد الأعلى لعصرنا، وبتوفيق من الله، سنحقق نصرًا آخر لإيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77805" target="_blank">📅 20:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏴‍☠️
مسؤول في جهاز الأمن الصهيوني: العودة إلى قتال مكثف مع إيران مسألة وقت ليس طويلاً، قد يكون في الأيام القادمة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77804" target="_blank">📅 20:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f1fcee3c7.mp4?token=uncZqPqG-UsplYjK9viffzrXdZVievETAPoPnML6pb0mnmCCEdEpSqksBCXJORZ3_QgZ9Eu9MVzDv9VbE_-LQzcKUhnJnHC7YG_VAdGt3HfZjWAfT-oRxb2d-Pxoc-1nq3oGq3h9jkI4u4ZNuJgPjuhjGfL7hlMVRstZbEF6fJbxz_c8irDH0lWqbJPIfJ7GmoxlpW8Jr3HF_oU6OKfVypzpQQVd2MDSo2w-fP8T503l5uV_nmYXIXFjtdRwx5RntMCDgKh8uw-B8UKjedevB-OlNd7OXjKsuWZ8PCEJs9mblWX8_tf_Sz2ICWbGCMfBkDIzY9y0vocF7Ykni1a8Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f1fcee3c7.mp4?token=uncZqPqG-UsplYjK9viffzrXdZVievETAPoPnML6pb0mnmCCEdEpSqksBCXJORZ3_QgZ9Eu9MVzDv9VbE_-LQzcKUhnJnHC7YG_VAdGt3HfZjWAfT-oRxb2d-Pxoc-1nq3oGq3h9jkI4u4ZNuJgPjuhjGfL7hlMVRstZbEF6fJbxz_c8irDH0lWqbJPIfJ7GmoxlpW8Jr3HF_oU6OKfVypzpQQVd2MDSo2w-fP8T503l5uV_nmYXIXFjtdRwx5RntMCDgKh8uw-B8UKjedevB-OlNd7OXjKsuWZ8PCEJs9mblWX8_tf_Sz2ICWbGCMfBkDIzY9y0vocF7Ykni1a8Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير يحلق في سماء محافظة ديرالزور السورية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77803" target="_blank">📅 20:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
مسؤول في جهاز الأمن الصهيوني:
العودة إلى قتال مكثف مع إيران مسألة وقت ليس طويلاً، قد يكون في الأيام القادمة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77802" target="_blank">📅 20:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
ترامب:
قلت لبينيامين نتنياهو إنه من الأفضل أن يكون حذراً جداً فيما يفعل لأنه قد يجد نفسه وحيداً أمام إيران قريباً جداً
في ليلة الأحد عاد نتنياهو إليّ متأخراً وأبلغني أنه قرر الهجوم
الإسرائيليون أعطونا تحديثاً عندما كانت الطائرات في طريقها إلى إيران، وأنا تصرفت لتقليل نطاق الهجوم
خمس دول من المنطقة تواصلت معي وطلبت مني الضغط على نتنياهو لعدم الهجوم، اتصلت ببينيامين ووافق</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77801" target="_blank">📅 20:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da6f82aa3.mp4?token=qFCTMCNrNOnQ3yW8uJsthsPBjRUvP8Kp1tLteEcAmVkkLWuHp0ilYpxFtx1FNG63DrtTal5wGb-FWOJw0a-cYLZAUGtR-agxAtdVHg1QZI73bGwX9b6DYNgIrsKfbCoVvzgv7PsIKCSTn16uswRwV3gig-lKydQynEH_qH17GBLphYpug3s5ptscKEEJ_6T3eq7fyrG5Nfb1BPYoNz2-pNvd-SBGcvKOGYH0keojAxTRh-0H-H9KHEDfdAmBtuavs6OqTD_O5y3Qck7WAVDiajj62XC3S-Z2HGX2flIbygbWkRbrJDzMNLNtYYjgquFCDcoBicpD4VCC6THZARia_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da6f82aa3.mp4?token=qFCTMCNrNOnQ3yW8uJsthsPBjRUvP8Kp1tLteEcAmVkkLWuHp0ilYpxFtx1FNG63DrtTal5wGb-FWOJw0a-cYLZAUGtR-agxAtdVHg1QZI73bGwX9b6DYNgIrsKfbCoVvzgv7PsIKCSTn16uswRwV3gig-lKydQynEH_qH17GBLphYpug3s5ptscKEEJ_6T3eq7fyrG5Nfb1BPYoNz2-pNvd-SBGcvKOGYH0keojAxTRh-0H-H9KHEDfdAmBtuavs6OqTD_O5y3Qck7WAVDiajj62XC3S-Z2HGX2flIbygbWkRbrJDzMNLNtYYjgquFCDcoBicpD4VCC6THZARia_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من الغارات الإسرائيلية على مرتفعات مليخ بجنوب لبنان.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/77800" target="_blank">📅 20:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يزعم:
سلاح الجو يحاول إعتراض طائرة بدون طيار أُطلقت من اليمن.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/77799" target="_blank">📅 20:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الاصوات التي تسمع في سماء المدن العراقية نتيجة عملية إطلاق صواريخ نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77798" target="_blank">📅 19:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏هيئة بحرية بريطانية: لا تقارير عن تأثير بيئي بعد استهداف ناقلة نفط هندية قبالة عُمان</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/77797" target="_blank">📅 19:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8pcrEtKU8OioH_ZxTCQ1neDaTphASeWmPGKsCu0Lpy5YkbzjNjSaR8MlX5HG8BZbxioC-dtNqDCZx3cGkq05Hf-dttw5qIdT_hXT6GJWFqDbOPtjYGmlfBDbG5inVEGc5oQCZAyVJw4fGgIadHVMlxHoe_WLPQUVbicro2DiOXER2TY-fLalqf6c52i9M1g8_g8UyJB7iembW4m0a5p7RvCfrE7VeHwdweSyQlziBq0OzG6E0G0bX5mLb9AAPJ4yde_pm1UPu73ItLqSChZ76lQ2Z8NRAKoP_wWdfBrsDKUzki2lx0DGSwhxFhbsrWcvLxVrQxYznHOtLiR3Llh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
من المستحيل أن يخسر سبنسر برات جولة الإعادة في لوس أنجلوس بعد التقدم الكبير الذي حققه. دولة من العالم الثالث. انتخابات مزورة! الآن سيعملون على الرجل العظيم ستيف هيلتون. لن تكون هناك نتائج، على الأرجح، لمدة أسبوعين، وفقًا للمسؤولين.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77796" target="_blank">📅 19:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
أطلق الجيش الأمريكي اعتراضيات الدفاع الجوي في محاولة لتخميد أحدث وابل إيراني من الصواريخ الباليستية الموجهة إلى إسرائيل يوم الأحد، حيث تسعى طهران إلى إعادة رسم الخطوط في الصراع المتوقف والدفاع عن حزب الله في لبنان.
أطلقت الوحدات الأمريكية في المنطقة الصواريخ الإعتراضية دفاعا عن النفس. هناك عدة مئات من الأفراد العسكريين الأمريكيين في إسرائيل، وكثير منهم يديرون الخدمات اللوجستية في مركز مراقبة وقف إطلاق النار في غزة في جنوب إسرائيل.
إن المسؤولين العسكريين الأمريكيين لا يزالون يراجعون ما إذا كانت محاولات الاعتراض فعالة في إسقاط أي صواريخ واردة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77795" target="_blank">📅 19:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
هيئة الطيران المدني الإيراني:
عاد المجال الجوي للبلاد إلى وضعه الطبيعي، وستُستأنف عمليات الطيران وفقًا لإشعارات الطيران الصادرة (NOTAM).
مع توفير الظروف الآمنة والتنسيق اللازم مع الجهات المعنية، رُفعت قيود الطيران، وتعود أنشطة الطيران في البلاد إلى طبيعتها وفقًا للخطة الموضوعة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77794" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
كان الجيش الإسرائيلي على وشك تنفيذ طلعة جوية هجوم كبيرة على إيران في الساعات الأخيرة - تشمل عشرات من مقاتلات سلاح الجو التي كانت على وشك الإقلاع نحو إيران، لمهاجمة أهداف في جميع أنحاء إيران. هذه الطلعة الجوية الهجومية الواسعة - لم تُنفذ بالطبع.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77793" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPjK2sUfipZPjiODc9VkScmPVvjVpWknXtkA1aEcVkmazTEagr3Y5Nkeo90fLK3qi7Zw1I0mD1DR5d98X9scIlsTqkOLANWEvsZz1ev31jZSvLq7x22GFoZcuQZqSOBnQ91g8J9tN6hzBJBPB_sISOX6tE71M_2Ptxgkmt8SbIwkLqVF-fFnslBXbotUNbiDMtJqDU3svMvDvHI1VTF4wCqV_MKmEDR7_ZImyvGrIPvOY1ozSgtMjrGsMeI35q0MMndtnRybU7fTLkEAJ_Nhu_b4DPs1Gnz6zuUHyK_HYjbaIg9k_FMbOw0SMaXJXiQXP2oMAloMYLmP7pBHNHPxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية "إسماعيل بقائي":
من يبني "سلمه" من "الفوضى" يقنع نفسه بأنه سيصل إلى السيادة على البشر. لكنه يبقى غافلاً عن الحقيقة الأولى والأكثر حتمية: صانع الفوضى هو دائماً ضحيتها الأولى.
‏إنّ الرجل الذي لا يرى قيمةً في الوفاء بالتزاماته أو الحفاظ على السلام، بل يزدهر بالفتنة والخداع والصراع الدائم، يحكم على نفسه بعملٍ شاقٍّ لا ينتهي. عليه كل يوم أن يُشعل نارًا جديدةً ليُغذي القديمة. ليس هو سيد الأزمة، بل أسيرها؛ ولا يُمكن وصف أي أسير، مهما كان ظله مهيبًا، بأنه قويٌّ حقًا.
‏إنّ مُثيري الفتن ليسوا في الحقيقة بناة السلطة، بل هم أسرى القوى التي يُطلقونها. فمتى ما استيقظت هذه القوى، لا تُفرّق بين حليف وعدو، ولا بين اليد التي استدعتها والأرواح التي تلتهمها.
‏تأتي هزيمتهم النهائية في اللحظة التي يدركون فيها أن السلاح الذي صنعوه لإخضاع الآخرين قد أفلت من قيوده وأصبح له إرادة خاصة به. في تلك الصحوة المريرة يكمن ضعف قوتهم الحقيقي، وبداية سقوطهم المحتوم.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77792" target="_blank">📅 19:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77791">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
قيادة الجبهة الداخلية الصهيونية تعلن عن رفع القيود في جميع المناطق - باستثناء مستوطنات الشمال القريبة من الحدود.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77791" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
ترامب:
أعتقد أن الولايات المتحدة وإيران تقتربان من اتفاق يمهد الطريق لمفاوضات طويلة الأمد.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77790" target="_blank">📅 19:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOOUV9jQAU92ItXfmWAwyOTapLQJ1CpDGFBDkhLhN4UmcSWRF7yDF05aNzuBvK-E-C2Ze_8R6rx5YKD-ERAREGW4T_q9JfaoFz5RlrEWKgWB2mbRL30K4sOhv_LC0LrCoEOvXIHdCVzFG57PDighI37Pg-cXtuCtcvYtrBW0b26Xl5kEfAIUpazNo25-nBOgQE5MUB0xS2xW8mRkAHins8i_QqiQ5cSMPwdwVV9UActHcbSD9XZYElXuNpbXc528c5M0yZ0Ohugi5M4kYXd10iS4pmyV-pxhCwJnmcfiEX1RxsWnWhqz4JthbNM4uFqkCmmTj1FG9uPtqnaCIVMwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
قيادة الجبهة الداخلية الصهيونية تعلن عن رفع القيود في جميع المناطق - باستثناء مستوطنات الشمال القريبة من الحدود.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77789" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزارة الدفاع السعودية: صفارات الإنذار التي تم إطلاقها في وقت سابق من اليوم كانت احترازية نتيجة إطلاق صاروخ باليستي من اليمن اختفى بالقرب من الحدود، ولا تزال التحقيقات مستمرة لمعرفة تفاصيل هذا الإطلاق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77788" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab44a945d.mp4?token=ShKrKu6YmtLAkbaE6QQN1lkHdkHkg2uBCV7chJDY3pXCd7MHDikAdC3_Q1unj9NzBifMeikGzwCTTa9FDrgKmhm-8c9cdeQVl2MHVZ7Y-TAXYuSMX7HMemlSbUeZ621vMkuoG2yZ-rFac6gcMsCR1cMJ9STRZ105mwQt9cJwF8esAUiRfCjptetNXuUheC_x-IAhcMXJUU3klc92WpYFcB2c-BzyEBsvngO3arUTTzV_O6GubZ2x16nNLxU0gwF9MyutKQEtWNecQlMy5zqEfyAvKbllQzztihWQqQ6Iwjs2xaObW4nnm3dquIGUabUbwlvKx21XAhTKUsO5kPc-Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab44a945d.mp4?token=ShKrKu6YmtLAkbaE6QQN1lkHdkHkg2uBCV7chJDY3pXCd7MHDikAdC3_Q1unj9NzBifMeikGzwCTTa9FDrgKmhm-8c9cdeQVl2MHVZ7Y-TAXYuSMX7HMemlSbUeZ621vMkuoG2yZ-rFac6gcMsCR1cMJ9STRZ105mwQt9cJwF8esAUiRfCjptetNXuUheC_x-IAhcMXJUU3klc92WpYFcB2c-BzyEBsvngO3arUTTzV_O6GubZ2x16nNLxU0gwF9MyutKQEtWNecQlMy5zqEfyAvKbllQzztihWQqQ6Iwjs2xaObW4nnm3dquIGUabUbwlvKx21XAhTKUsO5kPc-Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارات معادية على بلدة كفرتبنيت بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77787" target="_blank">📅 19:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">طيران مسير من لبنان يخترق الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77786" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">طيران مسير من لبنان يخترق الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77785" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtfWZC9JkhR2s8GXmselZt8pYgqtC3kibzaMpq2iZe2Os6TzEfbk5TjDSEBjMuT59xsJDN_kLWtwjG4Gp3HKGWBxkABy-WzraIEvbxlGwHCAdMLrrksAvLxlpKA63kljyxqR1Dyd2kNLRbEkDZiJ08D1l2muU1A44R7tyvBZbLIA9wlcxVic0f1EnUZZINW0wBZg33Lbj76bykQZxU1a4q_P7lPHuqjQsQ7jfkuFAFMj-Q_oA8cdnUNvMi1HFAz9rufhcOQFGE0U04KlwBobfwvarxxSbr7mf2lNP6SAwXTy4Kra7tKAZFaDuZKf7ZnER9XpNUrNXFw_yOB_1uS1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش الإحتلال يصدر إنذار إخلاء في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77784" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔵
الناتو ينهار …
أفادت التقارير أن ألمانيا وفرنسا أوقفتا مشروعهما المشترك لتطوير مقاتلات الجيل القادم FCAS/SCAF بعد فشل شركتي داسو وإيرباص في التوصل إلى اتفاق بشأن شروط التعاون، حيث خلص ميرز وماكرون إلى أن البرنامج لا يمكن أن يستمر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77783" target="_blank">📅 18:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77781">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91dc65254.mp4?token=oLzhxVupxpMY1y2pR1q8VgqUFAt-OYP7FO7ThPZ1nXI1Mb0F9tBq6BiT5LDnBfJAZ3QUd2Rjel7-ra8QuFmov0J5RW2L62vBA3TBl1z8yVuNgYpYC_QEuAaQyNznJlmPWrFXOJ4iK0Nz1-ROJP1Qfp2_K6U1HJeOF4T4YqVxFB3spzoelUpfXg7dgInJ2eb5FKl7vmMynsNWXQWXVn1Tuvq3bkPcvDhREn8E97sQtwxbBAR6ft5WruAwYph87LC59QM2R59fJZugl8I4leI5POmZ-GKhhgSWgqXZk4yUcBZMJmRyo_5m3mizZsIRuKqqEOaZGXq65jT4VCCqFoVoDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91dc65254.mp4?token=oLzhxVupxpMY1y2pR1q8VgqUFAt-OYP7FO7ThPZ1nXI1Mb0F9tBq6BiT5LDnBfJAZ3QUd2Rjel7-ra8QuFmov0J5RW2L62vBA3TBl1z8yVuNgYpYC_QEuAaQyNznJlmPWrFXOJ4iK0Nz1-ROJP1Qfp2_K6U1HJeOF4T4YqVxFB3spzoelUpfXg7dgInJ2eb5FKl7vmMynsNWXQWXVn1Tuvq3bkPcvDhREn8E97sQtwxbBAR6ft5WruAwYph87LC59QM2R59fJZugl8I4leI5POmZ-GKhhgSWgqXZk4yUcBZMJmRyo_5m3mizZsIRuKqqEOaZGXq65jT4VCCqFoVoDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كلمة للنتن ياهو بعد قليل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77781" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77780">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏مسؤول أمني رفيع لاعلام العدو: المستوى السياسي أصدر تعليماته بوقف العملية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77780" target="_blank">📅 18:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">كلمة للنتن ياهو بعد قليل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77779" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دك سفينة هندية بمسيرة قبالة بحر العرب</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77778" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJbM_sIPS30C35TkQhWqvWkFDJlwkT_PRbMOIwErSDUA1qkv9Alm2eph3IvcYkmoOTIWV73R8l4LfZ3i_hEJeDUcX1oBqKhxtBW1lv3c0ZusUFQ4ZaplYL9EoIwRRDO4MHGx1yyKvfccQzXss18Qb0PgRsNb1pUfrNo2-Kh6N1VVAE6XUpf7umBKN_bgMf1wR7q2f4R-obMv2uJ1yARDpnZ1l3P8cjJ-Pbr1xfbezFqB2RAW06DNjFbQnefIwshka4dFQK0IhuYyk17fJ-fvczgrz6Yu6ezs3vvKs9v5iMohb8_8GL-1xQmcHLBz8pPVmSH__hzlK9atvd1pO-FYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
لقد عطلنا معادلة وقف إطلاق النار على الورق وانتهاكاته المتكررة على أرض الواقع. طالما لم تكن لديك إرادة حقيقية لبناء الثقة، فسيكون رد إيران هو نفسه.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77777" target="_blank">📅 18:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏وزير الحرب الصهيوني: أي محاولة إيرانية للربط بين لبنان وإيران ستُواجه بقوة كبيرة</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77776" target="_blank">📅 18:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏وزير الحرب الصهيوني: أي محاولة إيرانية للربط بين لبنان وإيران ستُواجه بقوة كبيرة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77775" target="_blank">📅 18:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
القوات المسلحة اليمنية:
مشاهد من إطلاق دفعة صاروخية على أهداف حساسة للعدو الإسرائيلي في منطقة يافا بفلسطين المحتلة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77774" target="_blank">📅 18:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصاروخٍ موجّه.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77773" target="_blank">📅 18:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCdgCCLbyW4bJuUrt09BsNaz1tHJTT1wQBvuF6bxKSzqNdJI2JPuwT026c48-MwpW3_416A99hZXdGS5Es05NebQvF-gJkrU4eOgcBiUSkTEtWPBqhOy3eBO9Ok5f4HTDB5n3iODVhNdzHgpGddGiYnkCzLDWvY1zoYZlqZxHBrmD34vnZ4GOSENRz7fauwV0SQoaBGv4oV_A2RfPDJFTPxZyDBATxEBDiOAtRlHQC7SfWpdH26M7WfNYvT4HJ2bRAyRFW1GVNROQ2g4HT0rJ_RRDCgdsMldCyxvUAkwjYsGiY4Z0dRjNAFSNmTwEcMsK_zr6jq7HrD10bpNzSAuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمين المجلس الأعلى للأمن القومي
الايراني
:
إذا ارتكب التحالف الشيطاني أي خطأ، فستكون المنطقة جحيماً له
سبعة وأربعون عاماً ومئة يوم من المقاومة، من ساحة الحرب إلى ساحة المدينة، ومن ساحة المدينة إلى ساحة السياسة والدبلوماسية، غيّرت النظام الأمني العالمي.
ابحثوا عن التهديد الموثوق في مكان غير واشنطن وتل أبيب!
إذا عاد التحالف الشيطاني الصهيوني-الأمريكي وارتكب أي خطأ، فستكون المنطقة جحيماً له!
السلام على شهداء الضاحية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77772" target="_blank">📅 17:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77771" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozlsc7Ih120SrTCEclom0VLdOLtp6v7_Hw63M53lGFGNXdCLFs5ixHOIWkDW8-AOHnSfVjtLN-BX6O-__5vxbNM6C1DNUkRF9kNtJPWzbfJrmYMkXQqLerDvwXEbMV0dzy2GH43UqiZrw6ooF2Ygqo5gvLrbE2JywG90c0lsSU_Op5J4O1Z2LaTf5kNb40cITrAEbKiF3rNgstRhn_O4gpdONN5ah1baoN8iVSnHFFmc-JaxPShkrv-ggRev7G8EnAsQhKakCGBCNklar7Xo-OyGhOnxKxDfT54MHII13YwOtgZvGU9A6qkv6zubTJZ_2U-JCDh8Tc0Wv62ZKauIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسيرة صهيونية تستهدف سيارة في محيط مركز الصليب الاحمر اللبناني عند مدخل صور الجنوبي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77770" target="_blank">📅 17:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77769" target="_blank">📅 17:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سي إن إن عن مسؤول أمريكي:
لم نعترض اي صاروخ ايراني ليلا.. لا صحة لمزاعم إسرائيل بأن الولايات المتحدة اعترضت صواريخ باليستية إيرانية أطلقت باتجاه إسرائيل.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77768" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزارة الدفاع
السعودية:
صفارات الإنذار التي تم إطلاقها في وقت سابق من اليوم كانت احترازية نتيجة إطلاق صاروخ باليستي من اليمن اختفى بالقرب من الحدود، ولا تزال التحقيقات مستمرة لمعرفة تفاصيل هذا الإطلاق.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/77766" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
