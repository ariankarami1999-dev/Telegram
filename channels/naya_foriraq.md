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
<img src="https://cdn4.telesco.pe/file/FXi-aLiJUnzbmwAVwmdgR_u0OlQUW3LjpWqTzckKzWnA5WnaUiFBVUR33zGOrXc6HNTk8rru46K6xUtwVuZuxSp5mqGc1jmSyg0aTwAZqk7Z4uNqw1hgfc0pW_yfcH3w3jSmlan7Rdw8BAPoWZpRhxsWHdon1fNZ07UhWesOpDbiYrGdwCTGaId9I6oFZdALxcGAFvHkuEHmoAtwefagiQnj8cvKj6axjJn5-NOJIBgyXJHBxtYPJoN94BSRIf4EWgnHX7YSfKAIyiSuXQvV_jL9aq9FwlLqIRYy1_I9vT26ujeSVM_ZlrrTZ9wYHaqoARb-C8OKggcQsFGj0VrZHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-91581">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk1u6ukAQKKBuMYz_sfB5NrGUXwRSLg7ynWuSD2gIuh6UdUj7MX1_dw1-4QKP4mImh6pAftX50tuHEXatYfBUQ7GcmjK9Au1EYD8CcCKYDAbidqrel48iNyGok9SZOCmVX90u_Xdk-qn1Rj3k7Wi_IboYlKbqQiz_fcrexL6StN2tzXY1Ptz1gtQ9qRvlD2xk6UyxnqHva_lTgTPVmcKXv3Zg9cmnpdpL1IgxRxQqyHejvR3DKtlBMi-mJr5vy5bi6n3IyTkIxxDsAvO-Bh1WBDmV2t7_A8bU3xhPjD5S31D_cpfrvva1qCGLDdnjtlKGgAdE9ZFrd4N5EQ2W9QxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
اطلاق صواريخ من ايران.</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/naya_foriraq/91581" target="_blank">📅 20:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91580">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
🇮🇶
الخارجية الأميركية:
نريد رؤية عراق ذي سيادة ونزع سلاح وكلاء إيران فيه.</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/naya_foriraq/91580" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91579">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
يفيد بأن رئيس دولة الإمارات محمد بن زايد، حذر نتنياهو قبل السابع من أكتوبر بأن حركة حماس كانت تستعد لشن هجوم كبير.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/naya_foriraq/91579" target="_blank">📅 20:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91578">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">إعلان
📣
🇮🇶
🔻
🇱🇧
*تجديد العهد..نرفع الصوت..لن ننسى الشهداء*
موعدنا غداً السبت ٢٠٢٦/٩/٢٦
الساعة ٣ عصراً الى الساعة ٦ مساءً
المكان بغداد - ساحة التحرير</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/naya_foriraq/91578" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91577">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇷🇺
🇺🇦
بوتين
: كانت روسيا مستعدة لاستئناف المفاوضات مع كييف بعد الانتخابات، ولكن أوكرانيا حاولت استهداف موسكو وهاجمت مراكز الاقتراع.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/naya_foriraq/91577" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91576">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQaWZc2SS9SMdRqQxlLiLsIJ-bUN0pl6cd89tcwKZGslWJdeEbKN9p6vAYnhAmO3okr0kJJXn1ZTwZabHtbkoGFMW8IBJeN3x9AwFBZdV03k_1JQArHZj5claNj7kAb5FTf-3juLCiEY21WgtAaT_JeqF5VusRIeTPjs22IX_nfI_NOZG-6duhweQOU0oKPrRNmApjblO1u0nHCTp5D_WUyCt43VBPU_zJGqMT-Aad3ndfg6o9PR-3TZ08RiG-6kPGUN9kyzMkO9xUqEW5YcHUampw6gZqR628PwG3dpy1FMh2JDUc8L6dlOYXzR8-f5Z_n9DggO52mEVjHJ_aN3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏مفتي السعودية الى قوات التحالف التي تضم اجانب من الديانة المسيحية
😆
: ‏اعلموا أنكم تقاتلون عدوًا، قد أفسد في البلاد، وفرَّق العباد وخرج على ولاة أمره ورام شرًا بمقدسات المسلمين ولكنّ اللّه تعالى لهم بالمرصاد.</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/naya_foriraq/91576" target="_blank">📅 20:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91575">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
اطلاق صواريخ من ايران.</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/naya_foriraq/91575" target="_blank">📅 20:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91574">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
‏
مسؤول إيراني رفيع المستوى لوكالة رويترز:
سيظل مضيق هرمز مغلقاً، ولن تُجرى أي محادثات نووية مع الولايات المتحدة حتى يتم تلبية شروط إيران، إيران لن تقدم أي تنازلات بشأن برنامجها النووي.</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/naya_foriraq/91574" target="_blank">📅 20:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91573">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
معاون الأمين العام لحركة النجباء للمعاونية الإعلامية حسين الموسوي:
طهران هي التي سمحت للنفط العراقي بالعبور الآمن من مضيق هرمز فهل هذا هو رد الدين والشكر العملي؟، طهران التي ما زالت أياديها البيضاء تطوق العراق هي التي فتحت حدودها للتجارة العراقية ومخازن أسلحتها للدفاع عن العراق.</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/91573" target="_blank">📅 20:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
رئيس وزراء العراق الاسبق السيد عادل عبد المهدي:
اغلاق المطارات العراقية خطأ كبير.. وتنازل عن السيادة الوطنية ..
والتضحية بمصالحنا الوطنية ومستقبلنا
والتراجع افضل من الاصرار على الخطأ.</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/91572" target="_blank">📅 19:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
وزير الخارجية العراقي: التفاوض مع قيادات الفصائل بشأن تسليم السلاح مستمر.</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/naya_foriraq/91571" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
وزير الخارجية العراقي:
التفاوض مع قيادات الفصائل بشأن تسليم السلاح مستمر.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/91570" target="_blank">📅 19:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 14 غارةً جويةً وصاروخاً من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران، استهدفت محافظات تعز وعمران ومأرب وصعدة.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1032 غارةً وصاروخاً.</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/91569" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
🇨🇳
ترامب طلب من الرئيس الصيني التوقف عن دعم إيران.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/91568" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇮🇶
وكالة تسنيم بخصوص تعليق الرحلات الجوية بين النجف والجمهورية الاسلامية:
كما سبق وأعلنت إدارة مطار النجف، فإن القرارات من هذا النوع تقع ضمن اختصاص سلطة الطيران المدني ووزارة النقل العراقية.
في هذه الحالة، كان رئيس الوزراء العراقي علي الزيدي قد وجّه مكتبه بإصدار قرار حظر الرحلات الإيرانية؛ إلا أن هذا الأمر لم يكن يقع ضمن نطاق صلاحيات مكتبه.
وبناءً على ذلك، وبصفته رئيساً للوزراء، أصدر الزيدي أمراً لوزارة النقل بتعليق الرحلات الإيرانية، موجّهاً الوزارة بإبلاغ مطار النجف بهذا القرار.
في العراق، تُعد المسائل المتعلقة بعمليات الطيران في المطارات مسؤولية حصرية لسلطة الطيران المدني ووزارة النقل.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/91567" target="_blank">📅 19:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
قوات الاحتياط بالجيش الأمريكي تضع الأسس لعمل عسكري محتمل حول كوبا.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/91566" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي
: ساعدت صور الأقمار الصناعية ودعم المعلومات الاستخباراتية المقدم من جهات صينية إيرانَ في تهديد السفن في مضيق هرمز وشن ضربات دقيقة على قواعد عسكرية أمريكية في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/91565" target="_blank">📅 18:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
🇾🇪
التلفزيون اليمني:
- تم بحمد الله طرد تحشيدات تابعة لعدو السعودي حاولت استهداف جبل نمان وما جاوره في مديرية الوازعية.
-
مصرع وإصابة عشرات القتلى والمصابين في أوساط التحشيدات التابعة للعدو السعودي قرب جبل نمان وما جاوره بالوازعية
-
إسقاط 3 طائرات مسيرة وإعطاب عدد من الآليات التابعة لتحشيدات العدو السعودي قرب جبل نمان وما جاوره
بالوازعية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91564" target="_blank">📅 18:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئيس الوزراء العراقي خلال كلمته في الامم المتحدة: نؤكد تمسكنا بحقوقنا المائية المشروعة والعادلة وندعو إلى إدارة مشتركة لموارد المياه وفق مبادئ التعاون والقانون الدولي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91563" target="_blank">📅 17:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
رئيس مجلس محافظة النجف الاشرف:
نأمل من الحكومة الاتحادية عدم الموافقة على تنفيذ العقوبات الامريكية في مطار النجف الاشرف الدولي المتعلقة بحظر الطيران الايراني لما له من تداعيات اقتصادية على المحافظة ومعاناة كبيرة للطلبة والمرضى والتجار والزائرين.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91562" target="_blank">📅 17:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">صحيفة فاينانشيال تايمز: الحوثيون ابلغوا الاتحاد الأوروبي بأنهم لن يستهدفوا السفن الأوروبية في البحر الأحمر، مؤكدين أن حملتهم تستهدف السعودية وليس إعاقة الملاحة الدولية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91561" target="_blank">📅 16:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اردوغان: تركيا لا تكن أي عداء تجاه الشعب الإسرائيلي أو تجاه أي مجتمع آخر</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91560" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04466eb95.mp4?token=dtwKcDvcNj-trQF0UUiEaVGbyaG4Ue07cHQd4j0_Gsw7-4J7hrMLOrgmLeNGahxB1yN4UjTN0XqnfNo697AhHbIVhQYka45ltUyIKuUGegw9jxojLygaU_DMb0_jw2cFZnNk7gy9O5Q2kr6Zk1rWYDtK2hrJVW5zYexDxthNGn1VlltDLQCejEE4XGMI1qr6g2Y6fo2dAm9cMT0D8_nPkwY9va_m5Gj40axPd7xDF7jT0xMxy9yagjXqPYJ12oOOOHHDDRKVfDen1-dfxcurDER5guMAVdU2F7D3xcHNQkSfNQBC2dnXxSa2QEPJnhwhhzoDx9Y_YwZbkpt7tIVEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04466eb95.mp4?token=dtwKcDvcNj-trQF0UUiEaVGbyaG4Ue07cHQd4j0_Gsw7-4J7hrMLOrgmLeNGahxB1yN4UjTN0XqnfNo697AhHbIVhQYka45ltUyIKuUGegw9jxojLygaU_DMb0_jw2cFZnNk7gy9O5Q2kr6Zk1rWYDtK2hrJVW5zYexDxthNGn1VlltDLQCejEE4XGMI1qr6g2Y6fo2dAm9cMT0D8_nPkwY9va_m5Gj40axPd7xDF7jT0xMxy9yagjXqPYJ12oOOOHHDDRKVfDen1-dfxcurDER5guMAVdU2F7D3xcHNQkSfNQBC2dnXxSa2QEPJnhwhhzoDx9Y_YwZbkpt7tIVEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الخارجية الباكستانية: باكستان والسعودية وتركيا تدين الهجمات التي تستهدف مكة المكرمة والمرافق السعودية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91559" target="_blank">📅 15:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الخارجية الباكستانية: باكستان والسعودية وتركيا تدين الهجمات التي تستهدف مكة المكرمة والمرافق السعودية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91558" target="_blank">📅 15:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تسقط الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91557" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تنها در برابر دشمن ایستاده‌ایم؛ این چه اسلامیست؟
به نام اسلام، و به نام محبت و ولایت علی بن ابی‌طالب(ع)، همان پیوندی که دل‌های ما را به یکدیگر گره زده است؛ و به نام ملت غیور و حسینی عراق، ملتی که تشییع «رهبر شهید» برای آنان نه صرفاً یک مراسم، بلکه صحنه‌ای آشکار از ابراز محبت و وفاداری به ایران بود.
با این حال، اگر قرار است در برابر دشمن تنها بایستیم، این پرسش همچنان پابرجاست: این کدام اسلام است که در آن، همبستگی و یاری متقابل تنها در شعار باقی بماند؟
از همین رو ما ملت عراق، خواستار توقف فوری جریان گاز ایران به عراق و مطالبه بی‌درنگ بدهی‌های مالی عراق به ایران، که بیش از سه میلیارد دلار برآورد می‌شود، هستیم.
همچنین باید معافیت عراق از محدودیت‌های مربوط به صادرات نفت از مسیر تنگه هرمز لغو شود و نفتکش‌های عراقی نیز، در چارچوب این سیاست، همچون منافع آمریکایی مورد برخورد قرار گیرند.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91556" target="_blank">📅 15:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh8-XvJlvBYAzofGK7_B7L3Ne_2ji2ZTxsqRscID0j_PZdMV9RoK5Y9b-60zzp7vezSSrG6qsPFTDnfWH3-zztOCslH8HdqIxYO9e5q0jemX7WDYVGW6UyDzY3EFNigGCVpIRMfP8--Msf7sirwWqpw6IYBlfmJh-ZIIysM0HA1-y_jPTbHHbvOesdxfwu1pNEUtOeyjupAv244fNF2a3oU_RqdBnbQhsbmYMpZsCrqYJhn6kWYKpZ2xQKLLKHdiHIB84CJ7gyHvrAD9bytDVbZkcp8PEd48uxxgWOR-ZLcqQ1qQb3GInGb7o6wkP1C43nLOuLWXcWhk2UkLTcax_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ناشط إعلامي إيراني يخاطب الإطار التنسيقي الشيعي في العراق:
إلى متى تريدون أن تحنوا رؤوسكم أمام أمريكا؟! هذا الطريق ينتهي إلى المسلخ، لا إلى السلام والاستقرار</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91555" target="_blank">📅 15:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3CuMLZYbQ9pLCm3s9F-t1xvFEV3_JrQcSVBx2Y-VBoFJGK2hT0B7h8vRFu_B9J9KhgU0vNzgRHwY6yBp0r0IN3NGY7XoSR9Y7t-s2VFTc-e8gT1L7IMGkrkq0x125O0spqdzOPS2ZfzXFRvHX2itsP8BS86p7NAnQLLLURL9nTHCaKPl_fK0CqQjC-D0pmwBIOt_HZ-NIR1uCuwX49sVd3p1boHU5USroDUrlQYNMb82EMV1gP2AM5hu_j6FqyIgs-uf57lkp2UyEc9IVW9uoPrFmzELsQ8jVUYA3bFBUeys8_L47t9odFhVe5HkwWsZYDIkeV1IcDu7OTY_M_mJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية في الشمال</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91554" target="_blank">📅 14:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91553">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سماع دوي انفجارات في شمال الكيان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91553" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91552">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سماع دوي انفجارات في شمال الكيان</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91552" target="_blank">📅 14:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91551">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtFOIgd4unPcCjN-udSZ83APkZ__0WlhO5BCp1KwehwJW1BQgUdSGqPnrgdqJIqs4mc_sWdFI6xV0p9DUCkD7rbaFsadazzw9dMSkHDn-M81deh2yJCfDqtnMqa9Ya3AbqdLST6422eUVV1HlaLoI2khSZ7gU0wtCfobZ9ueUYOkOdDK3TXykeHSUdXqQ8ty2UtbrLsXNYaZPJ3W91CvB4hFnhdIpnXNKBt9uFpSBYm-z8SozKtZp3FBlJHU-o9v5bQCcmzcdBgdOKv4qUSVgKtsnGCkW-t4nKnEQ91uK4t1-VuEJzT8574OsHHy3ssIs_QD0Yne90hVdB__c_fCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستشار قائد الثورة
،
محمد مخبر:
التحالف مع أمريكا في تنفيذ سياسات عدائية سيبقى محفورًا في ذاكرة الشعب الإيراني، على الرغم من أن استراتيجيتنا في هذا الشأن واضحة: إما أن يكون الطيران في المنطقة متاحًا للجميع، أو غير متاح لأحد. إذا لم تتمكن إيران من الطيران وتلقي الخدمات الجوية، فلن تتمكن أي دولة أخرى في المنطقة من ذلك أيضًا.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91551" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91550">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
‏
رويترز:
مطارا أربيل والسليمانية علقا الرحلات الجوية الإيرانية بداية من اليوم.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91550" target="_blank">📅 13:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91549">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
نائب رئيس البرلمان العراقي يهدد العراق:
دول الخليج لن تصمت طويلا على تكرار استهدافها.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91549" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
خلية الإعلام الأمني:
إخلاء معسكر بعشيقة سيكون تدريجياً وفق جدول زمني متفق عليه.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91548" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91547">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
🇮🇶
المدير التنفيذي لمطار الإمام الخميني:
حاليًا، لا يمكن إجراء رحلات إلى النجف، ولم يتم اتخاذ قرار جديد بشأن استئناف هذه الرحلات.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91547" target="_blank">📅 12:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91546">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
مسؤول أمني أوروبي:
الوضع في البحر الأحمر أصبح أكثر صعوبة وهذا يخلق مخاطر على الاقتصاد العالمي وعلى عملياتنا.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91546" target="_blank">📅 12:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91544">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ-D6R-1q7rxSxdr77dt75hY9917XURyhpq3wv3A6SU1PFImZrSYItP2pn4Kl3j-M9KufnhzcoTuhb9iGKxyzDhIui04hNTTzvTackim-mL_VK9H-sZL_7bdFPPrhTQUrhi7VIcgjUDtBz0qZfia3e5pnQCNI-nWVuTSKxuyxOlPtDIYBVdkHbqbzkdFlOe4PdA4MrWMI2jwjtRcPKNW38vht6zjZDFmPsk9e-Bx2cQ8KGcEmMjgkymJ0f6zC0VPGCdimu-UvsUhAYqR14qAFg2HED2_Pqx1u0DgB4oPfhuyvTuHmNbvQCi3g2twgpWOo1puIwBk_YSqTK3TT3fIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b93922a090.mp4?token=vwANXYB5rkv4zLeMAwbdgGtm-K8-QIaKaZ_UfcLTTlXLFgK90By2cmpxWwsSezVQl6HTyTVVJylZ3IBcyFo_6hejeh9jki_CMzjZTCzC1jzo1WFgBXNLo9PS6dgaSXQWYrnmwcMf4NVH2CBiee_Tf1ssf3nJjgBM5BtnihoevFh4E9izuQ1exW_tC2V4868jF5wpwyaODho-g6ztG3anxWsClP_kE9GOQBVNmrdiO2sBAnheBjhISrSa9E9om-ueY7fcID0UC6mbIj-mnh7qOAesDeG5P-IPUJebr91SaWE1Y9aOEW4jK0CS93qlonoR-NGR7r-hASXg31YjxzVD6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b93922a090.mp4?token=vwANXYB5rkv4zLeMAwbdgGtm-K8-QIaKaZ_UfcLTTlXLFgK90By2cmpxWwsSezVQl6HTyTVVJylZ3IBcyFo_6hejeh9jki_CMzjZTCzC1jzo1WFgBXNLo9PS6dgaSXQWYrnmwcMf4NVH2CBiee_Tf1ssf3nJjgBM5BtnihoevFh4E9izuQ1exW_tC2V4868jF5wpwyaODho-g6ztG3anxWsClP_kE9GOQBVNmrdiO2sBAnheBjhISrSa9E9om-ueY7fcID0UC6mbIj-mnh7qOAesDeG5P-IPUJebr91SaWE1Y9aOEW4jK0CS93qlonoR-NGR7r-hASXg31YjxzVD6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
خاص لنايا.. مشاهد لهبوط الطائرة الإيرانية التابعة لشركة معراج القادمة من العاصمة طهران في مطار النجف الدولي.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91544" target="_blank">📅 11:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
🇮🇱
إعلام العدو يبث مشاهد حصرية للحظة وقوع قوة من الجيش الإسرائيلي في كمين لحزب الله عند تلة علي الطاهر وسقوط إصابات.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91543" target="_blank">📅 10:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91542">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f871abc343.mp4?token=OoBhDL6Yh1BBkcoaj7tmNI2u3tRvdpEdwHLhAkQuK1poBScxdXxJA_40E5GWMwGAirIUdFq05Pn4L6MzX7kAmHcddPfrXxwx3k1xMfEo0RwAES5Sevs6OHliJFguwbO_n66UiWTehgZ1dN99hYsyVBZyiPRy0Pp99wlp-_yLz6sfU8EVztdP2az53zvWKI1vHBg5Kp3EaZ05O6VNtzZhTQ2blUDbFXWWhsigXJ6fwDAaYqan0RMHcLN1F4AArdwIaDq1w1qcbObaG5x9ToVDqrKQezZPaGc7_eI-z2AZUH-vUousND4OQa-bAH2C7zQFBXOezwJYYsJL__y-y3MGzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f871abc343.mp4?token=OoBhDL6Yh1BBkcoaj7tmNI2u3tRvdpEdwHLhAkQuK1poBScxdXxJA_40E5GWMwGAirIUdFq05Pn4L6MzX7kAmHcddPfrXxwx3k1xMfEo0RwAES5Sevs6OHliJFguwbO_n66UiWTehgZ1dN99hYsyVBZyiPRy0Pp99wlp-_yLz6sfU8EVztdP2az53zvWKI1vHBg5Kp3EaZ05O6VNtzZhTQ2blUDbFXWWhsigXJ6fwDAaYqan0RMHcLN1F4AArdwIaDq1w1qcbObaG5x9ToVDqrKQezZPaGc7_eI-z2AZUH-vUousND4OQa-bAH2C7zQFBXOezwJYYsJL__y-y3MGzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
40 ألف دراجة نارية تشارك في مناورات "فدائيين إيران" بالعاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91542" target="_blank">📅 10:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91541">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb4938f06.mp4?token=GPRTI4pR9v1uclmaYRKSmCbjAValhPo1TiYX2tVA4Vg4t4-UK0_yT2P-TKOsQkvM6si9hEaWwxEe6I2BaDSUwtciC9BjDl8G9Auej4jOs-0I3o5BA17i3x4uYyMPnTNu6Lf5GFbvDdAkrjukKMUhRyYKp1wtmbyd5uc3owMuYo2tFKq1fP1bRfAwsC7ck48Yi1JCDgC8FPS_hECmDASHeucTfHDgV27O3lGuCF2Yt8ckY8G7vXwI7ipXOCuYxvFtw80uMFvqOrQWW3IFk4z-Cmo5rmhlk2EgS-ZyonS6GSx_R2h5PZ9zQmBSaYrdK7OWDtnHClbLjg8-IkuhGvdaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb4938f06.mp4?token=GPRTI4pR9v1uclmaYRKSmCbjAValhPo1TiYX2tVA4Vg4t4-UK0_yT2P-TKOsQkvM6si9hEaWwxEe6I2BaDSUwtciC9BjDl8G9Auej4jOs-0I3o5BA17i3x4uYyMPnTNu6Lf5GFbvDdAkrjukKMUhRyYKp1wtmbyd5uc3owMuYo2tFKq1fP1bRfAwsC7ck48Yi1JCDgC8FPS_hECmDASHeucTfHDgV27O3lGuCF2Yt8ckY8G7vXwI7ipXOCuYxvFtw80uMFvqOrQWW3IFk4z-Cmo5rmhlk2EgS-ZyonS6GSx_R2h5PZ9zQmBSaYrdK7OWDtnHClbLjg8-IkuhGvdaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
على الرغم من إعلان إیقاف حركة الطيران بين مطار النجف وإيران.. طائرة قادمة من العاصمة طهران تحط في مطار النجف الدولي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91541" target="_blank">📅 09:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXTUcpCNuSEzgPRLAcYROjpKQ6BTeRvkT9u7_M1kSYGd-JpO7Ky0URwoveMLd1SdUIT6wc45RYzkBdHajauuTHY7OQPWlA5d1b0AMiuwIggZj4tfhWqRC15zS_fBoeGhTqV1-8RXFU5IJHCDD4MA_JRCzYfWT2kYnPz00EXM-i5cSr_C_p3zcOEDh1ew_fFykLRnKeWixkiwYm3XHQKQnlHob_zpLykRnNVyIBYrH7k_K17Al5-S9OUyIgDkQ_yW681XREJ44VwJ6Mq_c9gUpBlw1vVBWu-OX3G7GfiB19llimp4-lR45O9d-fxjOnhY14MwZO5PA99qs1JHLSSJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91540" target="_blank">📅 09:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91538">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrlOIp0fO94K2YU-DjGs-_QVf7vndQjgr48nTM_2b4DCg9lsaqRR9Qu0wI7EFsh3vJqruSil4RO3D2rFJbS_ydQsW_yg_PfoK-UdGbdIKnq-9Xdw_OMKQve14h7XNBlR8btpWBJ1SA7l6YMeTazsbOOwVGas88GXm-qhTRgP6T7eldYb0_3QIv0pnJEnlP8ZhRuI7CWZvxYzZHBm_cDJHL3go8vOKz3nYYHOALNOqcCB4Ol7mEfyedqIKyxQweSwLcxslol_nVxnK2HXraFvHBIUrcySUn8tuXQ8CEyBVs6BIvODATovBGELn4wT99w8VtTlaLJYuEg2Gpe_17gmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-fymRgLoYVpa9mfvrwDjdNPI84h7RG2vldtneBc2qx4NKGLk-llQosR8pe_5gHIC0fqRvibSH9rmAH0H5e6MY0wzZHuc-IvqyCoEFb_B8GcGruzlPLm0f_ogahG5DL1rAZaMkKoiYkLI6FA6hWFkA6au6VzSQsBMmlWMvHHKxyUH_u2ikuSOuVfmGnmzbcOcu4VJ2BQrp5JGqjwYklxnuruLc3yKILK393q6OwYOw62kRa4SrIqHYZiFvpTBtgVP3BgpmB6Hd6tXEKly5EvEXQ-HRiJDHImex_q0TAxToYCuaAetduy9vroaiyprXoeXm6BGJhgWsQZmEWJBixkKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني يعلن رسمياً عن مقتل جنديين وهويتهما إثر إنفجار مسيرة في قطاع غزة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91538" target="_blank">📅 08:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇷🇺
انفجارات عنيفة تضرب مدينة فورنيج الروسية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91537" target="_blank">📅 04:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91536" target="_blank">📅 02:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91535" target="_blank">📅 02:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
بزشكيان
:
-انصار الله مسؤولون عن أفعالهم ولا يتلقون توجيهات منا
-سنتخلى عن اليورانيوم المخصب بنسبة 60% في إطار القانون الدولي ومعاهدة عدم الانتشار
-سنلتزم بكل ما تنص عليه التزاماتنا بموجب معاهدة عدم الانتشار النووي</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/91534" target="_blank">📅 01:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c28a1313b.mp4?token=Gt4S01oOMM9itzUy5pK9sYv5XW9T2xgWZIIkanKYAcV55THJCH4Z-1uqw2t3O7R16GfTHnIJjgf3BC2M_gpY7odx257qxcgEvYEFUg4UrViE_xtj82Mc1BwGBUS_G-wfKeYLHIuZcg5BvwO26QlawAfj4Dt_refG5gxzH4SSEmBxznExZpu5oAzbXzBHGe9-0RjZ7g5dGRn0ppO9BmR63zzeoT2CkVqEDLJwvpYWdpKF9F5Qqo2h5TEM5IILKBPZ7tXkhl4OUsojUwPg723j6WiQ1rn8p1Z_nQY4kIsvy2887LOurdFHlFsN9wP1vfOOR5WGzlUyxPn1r2EbGRFFCCJXbd4WbPCe_P0ypVFTvEHYNtfZoDYXX6Df3s2mhzJEyjC-fPivjZazQK7OYtaJGlt-VXZ5ZmjZZX9IXE9edalZBw5HAkTaIpngZf64E6FUUX9qW-QqQ-JA8eisfIkv1cVD5IddgMpAEeGJfZSYsyD_cwHG9AfunWl-kZy9pR8E8V72oJ5E7JswYq68zCfYYrHKGWXZGX8vcgfl-m_7bGeQws_Etms_X4MxpCqQdJfsmFeSdr5WgFx8srI1FGE4v99FzUaIttRRcw7dO9DViWnm_wHoQFeRRWUnGu-PWwyNfvo8tX0luSUXw3Jprn91NMBe90HsMwMYKpTkWQb8s6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c28a1313b.mp4?token=Gt4S01oOMM9itzUy5pK9sYv5XW9T2xgWZIIkanKYAcV55THJCH4Z-1uqw2t3O7R16GfTHnIJjgf3BC2M_gpY7odx257qxcgEvYEFUg4UrViE_xtj82Mc1BwGBUS_G-wfKeYLHIuZcg5BvwO26QlawAfj4Dt_refG5gxzH4SSEmBxznExZpu5oAzbXzBHGe9-0RjZ7g5dGRn0ppO9BmR63zzeoT2CkVqEDLJwvpYWdpKF9F5Qqo2h5TEM5IILKBPZ7tXkhl4OUsojUwPg723j6WiQ1rn8p1Z_nQY4kIsvy2887LOurdFHlFsN9wP1vfOOR5WGzlUyxPn1r2EbGRFFCCJXbd4WbPCe_P0ypVFTvEHYNtfZoDYXX6Df3s2mhzJEyjC-fPivjZazQK7OYtaJGlt-VXZ5ZmjZZX9IXE9edalZBw5HAkTaIpngZf64E6FUUX9qW-QqQ-JA8eisfIkv1cVD5IddgMpAEeGJfZSYsyD_cwHG9AfunWl-kZy9pR8E8V72oJ5E7JswYq68zCfYYrHKGWXZGX8vcgfl-m_7bGeQws_Etms_X4MxpCqQdJfsmFeSdr5WgFx8srI1FGE4v99FzUaIttRRcw7dO9DViWnm_wHoQFeRRWUnGu-PWwyNfvo8tX0luSUXw3Jprn91NMBe90HsMwMYKpTkWQb8s6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
العراق يستورد أول شحنة بنزين عبر المواني السورية باتجاه المعابر الحدودية</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/91533" target="_blank">📅 01:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAk9DnZRRGA0FtRk9QRyzt8hAbijuUwaAOqIHjA3eubJxA6iThFBRs8RFNv-Wq1Wm7EkXvYvZqIZSnpjfT8foL_OIT8IQ2TEDqLKRFtpOEiM0yebeoOlUOJpFFnqK8ZcLIdHdF8flBYobD8Ag9HRiAOoEIeY9hd3pImAMxoCdXoSaI7vUNPMs0TGBOLempIpU4iLSKEVn-xLDVphLAsC4JjXVPTpzmtMqEhA0p-qiHgKyR5z89RiEO6KdEys6C-aj27XnBHvz3PVzSqVtGm9kOhVYoZ4OztrN8QIe5xajKHYRWsisnfmZHvYy2AxG4yL0OonN4Kl0QE0eUAnvVOZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lemijTVTji0TmLVF3vLZDOqbV-VfHH4eK4hYypPjENn_x4adyjJfdkhuLDct2SSyEfHkXPXppkxzjCGUkp_krMjifxxFLsHSNClY5ytRcAQOOP6-mHkGHfa0SMTESzdnq3CB2yfMfv_8Q69bg8ljVgVnwJAv_9tThu8tZP0iyjwXdNIJsbPP9ukjyvb-cExvUt12sWsyp5kEFsaU7UIQGvMs8TwH2VuJtxb2SDwHlpwcttin6xUi2I__chdxwH2cl1lnh19DsikfVOXd7jFOtW0FKSfNLPdJqHQeSllCnjKqSkzyepbqkrOgTzIIbjMJqFeIwW3nheai701tLIWOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8edDrZU7PsvwIA5hWBUGJNJhE4HRrtWxjqEz5y1uag14k75FA9lh2w5vtrs8r5dGKNAspLvSUOjVps7eEfPPN-v8U28_GxUfBLftRRowlwcygVZgwK58bgXD3OF8syuXkso52XpDSuy825E1yVn6Xmdegx3egex4-hV5cssaPGrg6LOXKSP0UHznQYuyy5PLpAFzs9CdDC9f5dC668laltpv1p2TkgxY8IbkfHjRL4OqM2XGgZERzFonygqhOObk2srbUxkZsbw-lWDewvEWR7wj2zTtDU1VzgNAnY7Gc7SmwmgaRVw0Ra5IeHvVmWXd6WBH_Vg9cVt_Ezzl3_9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TI_hkSjnusGVRG26roB73Wty5WXrqLQqWbnkstOEPKrUwv1EVJiHQypSgbf_85jUnbNO5sR2L54Llp9JYi-0hUuvrStNyCWomxCRb3TfhWyh5RZ_C9p6Tas6czdbMFU0dcgSf8HR-704YTnIrr1KaS8oO_SG8E2b6sCYEFOnfaQDHZszo4ETVIfc4OB2_P-_rXREEeEqOaGHT9p2uO_RLf2c4mrosq-GJn0y9rUsh_nwji_cvg0V0yPssi6j3dV-U9JpghsnGbUrLr0z7XRtcDFVlRMZxeDXcFHQk7oH3fv0j3u9nr6fnxCuSb3RNXiyhlwTFJQoWG5BAS_rKzuQQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇸🇾
بعد فصل مناهج العرب والأكراد في سوريا..
نظام دمشق يبدأ بتوزيع المناهج الكردية الجديدة على الطلبة في شمال وشرق سوريا وتتضمن المناهج الجديدة أجزاء منها خرائط وتصورات لما يُسمى بـ"كردستان الكبرى" تشمل أجزاء من الأراضي العراقية إلى جانب أراضي من دول أخرى.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/91529" target="_blank">📅 00:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
🇺🇸
رفض مجلس الشيوخ الأمريكي قرارًا يهدف إلى تقييد صلاحيات الرئيس دونالد ترامب فيما يتعلق بإيران، حيث بلغت النتيجة 49 صوتًا مقابل 50.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91528" target="_blank">📅 00:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91527" target="_blank">📅 00:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
🇺🇸
صواريخ كروز من طراز شهيد ابو مهدي المهندس باتجاه سفن معادية بمضيق هرمز</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91526" target="_blank">📅 00:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91525" target="_blank">📅 00:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇾🇪
مستشار عسكري من انصار الله لوكالة فرانس برس إن اليمن سيهاجم المصالح الأمريكية في الشرق الأوسط إذا تدخلت واشنطن عسكرياً في اليمن دعماً للسعودية أو حاولت السيطرة على مضيق باب المندب، واصفة إياه بأنه "خط أحمر".
‏وقال المستشار إن اليمن "سيغلقون باب المندب تماماً أمام السفن الأمريكية" وسيعتبرون أي مصالح أمريكية حولهم أهدافاً.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91524" target="_blank">📅 23:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPB4wpztDLGCazgoH4lEqnj4QKGdOf9xlVu-yJsTvcyO6B9VVekaPl_xRyOsuzFr5j5XvDrhAVNHBJ0ABGIFUxdRIHFU1DR7Y4xIa7Mte7WXFb7hGHtlpsz1bc2Q4q8NHMds-GN6pSlQwFx2Q02ywZQOZbDpz69fprqNtMXKLiYQSPchSXSuA2ipBu9Tq-NOTKSgOy_zIISQEl-jRpQUKlrC_JYTcehtGOvfNit-kMxBWu5p-T_hp4vnHb5R8VkqvBYNQ2o5CnCdgQBNY8sqLpsDD8c1QKCv1HvKJr-EXUCxalhXhxG7HJU8MnPLhpJ3pqzxNag4x_awXWe10jdd3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏
مفتي السعودية الى قوات التحالف التي تضم اجانب من الديانة المسيحية
😆
:
‏اعلموا أنكم تقاتلون عدوًا، قد أفسد في البلاد، وفرَّق العباد وخرج على ولاة أمره ورام شرًا بمقدسات المسلمين ولكنّ اللّه تعالى لهم بالمرصاد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91523" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
القوات الامنية ترصد طيران مسير مجهول يحوم حول مزرعة شخصية مهمة في منطقة ابو غريب جنوبي العاصمة بغداد .</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91522" target="_blank">📅 23:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b3ff01b6.mp4?token=agrNhBj3nbZrSSIfT0c2ArzuQ262VrIi37Ke8CughOQjNTrTmqJ8fBt-y64l6G5J-M1tSMoKF7uyKw_VEophjnaLKXwNvO4u2K4aB8IzN8gkOLyKMGquaFzZfVZcZfubJ1PeP1YYNGffQp3uEno6zrlStX1n5yxD7qQQJyr_3TTJObU3bpLkB5KZc_Qd4oE5uMP40W_S-QdCEU_mp3IrwumEuxnCJ0Pr7AdUruQGkMLy1TvW_HWFvgBdpk93Ut9jbUqnCL3rIgDw7UvW-G_emeGpfVpYi5tzAiKO6vas76z9meinSvKFgpTPJLi0AHfGjSKZG6tXHmTjULrJ-Q2ZxEUz8AJ9eOGZJL6a47iyZ7Sn93wiHfirkCgA2XJbSIWg1q5UOgNHoWq7HRZBYJrmw8FwYO0MxetE4GJcwj93ZeJ01b6WnXfe_YTkPm_nkcN7qWlYIp0QaUJWuQjBmQVrTi-FFI_44TdeaJZK52XBO0RqJB8xJvJ-heNqNlPuj7LlsCZVAuI2C4uKuZP14QEEgF8HoYVuh5wd5-9Id6uBkafXh9Wmi2x7ItoXho1W7FlhOM9mspnmS68pVNiXGZsfJZUSiJYfdTZJ0HNXxFGFlVkQkd-Lto2_EBffGKqir2zOMFFr1qjQd1cYDA2qlgXlR2SgVufdPCY0XqM5IVXwPc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b3ff01b6.mp4?token=agrNhBj3nbZrSSIfT0c2ArzuQ262VrIi37Ke8CughOQjNTrTmqJ8fBt-y64l6G5J-M1tSMoKF7uyKw_VEophjnaLKXwNvO4u2K4aB8IzN8gkOLyKMGquaFzZfVZcZfubJ1PeP1YYNGffQp3uEno6zrlStX1n5yxD7qQQJyr_3TTJObU3bpLkB5KZc_Qd4oE5uMP40W_S-QdCEU_mp3IrwumEuxnCJ0Pr7AdUruQGkMLy1TvW_HWFvgBdpk93Ut9jbUqnCL3rIgDw7UvW-G_emeGpfVpYi5tzAiKO6vas76z9meinSvKFgpTPJLi0AHfGjSKZG6tXHmTjULrJ-Q2ZxEUz8AJ9eOGZJL6a47iyZ7Sn93wiHfirkCgA2XJbSIWg1q5UOgNHoWq7HRZBYJrmw8FwYO0MxetE4GJcwj93ZeJ01b6WnXfe_YTkPm_nkcN7qWlYIp0QaUJWuQjBmQVrTi-FFI_44TdeaJZK52XBO0RqJB8xJvJ-heNqNlPuj7LlsCZVAuI2C4uKuZP14QEEgF8HoYVuh5wd5-9Id6uBkafXh9Wmi2x7ItoXho1W7FlhOM9mspnmS68pVNiXGZsfJZUSiJYfdTZJ0HNXxFGFlVkQkd-Lto2_EBffGKqir2zOMFFr1qjQd1cYDA2qlgXlR2SgVufdPCY0XqM5IVXwPc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنية  بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {ذَ ٰ⁠لِكَۖ وَمَنۡ عَاقَبَ بِمِثۡلِ مَا عُوقِبَ بِهِۦ ثُمَّ بُغِیَ عَلَیۡهِ لَیَنصُرَنَّهُ ٱللَّهُۚ} صدقَ اللهُ العظيمُ  يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَه الإجراميَّ على…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91521" target="_blank">📅 23:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6411165378.mp4?token=XD2TmHR-gY0bqAafKBiAHWzXQerqKOyKg86CIA5zzHhsOjAaAn2r0zawHk3R-WuitSGZEeQOqEwy-TI9reZ6JWxzWO2wKp-dMtmiWcy3sp1GZDKubEbCGkYz1KNSCGPTmcnNpNcW_dwodV7uuWXzTioglq5L3dvTdkblQjF7sFkbdQYZXRE5KNpGGX2aK7pTya7I50urg1ObUtfDRgTV91fKUFh8sNWYJwIFtQeuHBXTuCwgzFzksVXoy7WP4XQFGpYq2iIap9sQJAuWpBSWm-2DYGi4QqABXDgm7E3uyXE7aP9TlseVHvZpDJbAUYO-5L_zivO3C-WFOdRJNZD46g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6411165378.mp4?token=XD2TmHR-gY0bqAafKBiAHWzXQerqKOyKg86CIA5zzHhsOjAaAn2r0zawHk3R-WuitSGZEeQOqEwy-TI9reZ6JWxzWO2wKp-dMtmiWcy3sp1GZDKubEbCGkYz1KNSCGPTmcnNpNcW_dwodV7uuWXzTioglq5L3dvTdkblQjF7sFkbdQYZXRE5KNpGGX2aK7pTya7I50urg1ObUtfDRgTV91fKUFh8sNWYJwIFtQeuHBXTuCwgzFzksVXoy7WP4XQFGpYq2iIap9sQJAuWpBSWm-2DYGi4QqABXDgm7E3uyXE7aP9TlseVHvZpDJbAUYO-5L_zivO3C-WFOdRJNZD46g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تاكر كارلسون:
القطريون أعطوا ترامب طائرة. وما الذي حصلوا عليه في المقابل؟ لم يحصلوا على شيء.
لم تدافع الولايات المتحدة عن قطر. نقلت الولايات المتحدة بطاريات نظام "ثاد" من الخليج إلى إسرائيل.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91520" target="_blank">📅 23:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91518">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e96b19f5.mp4?token=MufwuzkqKgrFpZdV-X8G19vOnGaXWjJ-itDq4uQI0R_vrmC198x7dwSNtnj7AlIecwEIgbIdIO3wWDwIgQcRRgSXRMui7ff3sr4QxK6xCHJOAKjvfPFpWn_Bd__o7_lROg2ilBvpmyl8JrR05HbZJDWWdYBIYbEPwtnWD7avUbWGiOJhrVvdlS-shqX4qyaK_NkK8jtYRpvEfVKpaSpGhqjKTHeaQz0lTkhz3JTv4j-srm8BxgK93wklAlTHVp2aRsa4IbaCUDZLbo2tiG5g-WC8qw4s9ITj92C5dmqZtG5xe_0qI1E5kMIhdsN_3icK4CWGVthW3GXhxsZUz8B4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e96b19f5.mp4?token=MufwuzkqKgrFpZdV-X8G19vOnGaXWjJ-itDq4uQI0R_vrmC198x7dwSNtnj7AlIecwEIgbIdIO3wWDwIgQcRRgSXRMui7ff3sr4QxK6xCHJOAKjvfPFpWn_Bd__o7_lROg2ilBvpmyl8JrR05HbZJDWWdYBIYbEPwtnWD7avUbWGiOJhrVvdlS-shqX4qyaK_NkK8jtYRpvEfVKpaSpGhqjKTHeaQz0lTkhz3JTv4j-srm8BxgK93wklAlTHVp2aRsa4IbaCUDZLbo2tiG5g-WC8qw4s9ITj92C5dmqZtG5xe_0qI1E5kMIhdsN_3icK4CWGVthW3GXhxsZUz8B4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
أنباء عن اندلاع اشتباكات مسلحة وتحليق طيران حربي في أجواء الحدود الباكستانية الأفغانية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91518" target="_blank">📅 22:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91517">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
الأمين العام لحلف الناتو
: الحلفاء الأوروبيون مستعدون للهجمات الهجينة الروسية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91517" target="_blank">📅 22:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91516">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنية
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {ذَ ٰ⁠لِكَۖ وَمَنۡ عَاقَبَ بِمِثۡلِ مَا عُوقِبَ بِهِۦ ثُمَّ بُغِیَ عَلَیۡهِ لَیَنصُرَنَّهُ ٱللَّهُۚ} صدقَ اللهُ العظيمُ
يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَه الإجراميَّ على شعبِنا من خلالِ حصارِه الظالمِ وشنِّ الغاراتِ الجويةِ العدوانيةِ والتي بلغت منذُ بدءِ التصعيدِ وحتى مساءِ اليومِ 1018 غارةً جويةً وصاروخًا من خلالِ طائراتِ F15 وتايفونَ أقلعتْ من قاعدتي خميسِ مشيطٍ والطائفِ والعدوانِ الصاروخيِّ من نجرانَ وجيزانَ استهدفَت محافظاتِ مأربَ وصعدةَ والحديدةَ وتعزَ والجوفَ والبيضاءَ وخلَّفت شهداءَ وجرحى بينهم نساءٌ وأطفالٌ وتسببت بخسائرَ في البنيةِ التحتيةِ المدنيةِ.
وفي إطارِ الردِّ على هذا العدوانِ نفذتِ القواتُ المسلحةُ اليمنيةُ بعونِ اللهِ تعالى عمليتينِ عسكريتينِ نوعيتينِ الأولى استهدفت هدفًا حساسًا في عاصمةِ العدوِّ السعوديِّ الرياضِ
والأخرى استهدفت شركةَ أرامكو في ينبعَ، وذلك بعددٍ من الصواريخِ الباليستيةِ والمجنحةِ والطائراتِ المسيرة، وحققتِ العمليتانِ أهدافَهما بنجاحٍ بفضلِ اللهِ.
إنَّ استمرارَ العدوِّ السعوديِّ المجرمِ في شنِّ غاراتِه على شعبِنا وبلدِنا لن يثنيَ القواتِ المسلحةَ اليمنيةَ عن ممارسةِ حقِّها المشروعِ في الردِّ المباشرِ والمناسبِ على هذا العدوانِ فكلُّ اعتداءٍ سيتمُّ الردُّ عليهِ وكلُّ تصعيدٍ سيُقابَلُ بمثلِه وما مصيرُ المعتدينَ المجرمينَ الظالمينَ إلا الهزيمةُ بإذنِ اللهِ تعالى.
مستمرونَ في فرضِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 13 ربيع الثاني 1448هـ
الموافقُ 24 سبتمبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91516" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91515">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db132f7e43.mp4?token=Xu1ZVSNJSFFIJA1O8ygT3bQc68IGdC5tN2TTUfH3yRFtVipUy6cI8CEZkHjrRQnvooviXfoZ6c_OGgTOq1QN7mRutuuLMfl1lParjPhhOpVamYc0gqSBZhhvhIQ2AuJeJUCgvWNCtQ0dy2YdN0tBHJQcXsRZQB9_Vb2Twm-LLeYTwXOMRsic5ort2ujYeOTnEkBmmHQheP9KmjtFNFr95Qe3KEFkKvy9abSmQPk0pkeyTRw3P0SyCaukiVVqulK2vQmcra6gIKkgjLjAu42TQ1eZ6VTeh_WqjTDkJk_xRKpCO_o2-iLdIxod3jcNNncxUx88HKxAUTEzzlojU7R6cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db132f7e43.mp4?token=Xu1ZVSNJSFFIJA1O8ygT3bQc68IGdC5tN2TTUfH3yRFtVipUy6cI8CEZkHjrRQnvooviXfoZ6c_OGgTOq1QN7mRutuuLMfl1lParjPhhOpVamYc0gqSBZhhvhIQ2AuJeJUCgvWNCtQ0dy2YdN0tBHJQcXsRZQB9_Vb2Twm-LLeYTwXOMRsic5ort2ujYeOTnEkBmmHQheP9KmjtFNFr95Qe3KEFkKvy9abSmQPk0pkeyTRw3P0SyCaukiVVqulK2vQmcra6gIKkgjLjAu42TQ1eZ6VTeh_WqjTDkJk_xRKpCO_o2-iLdIxod3jcNNncxUx88HKxAUTEzzlojU7R6cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صورة الحاج قاسم سليماني تتوسط قاعة الجمعية العامة خلال كلمة نتنياهو.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91515" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91514">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9932ce34eb.mp4?token=Rxm-lWmBXsB9WL_2vJLkj3d7AZvipVkQfCvtqb2EFDeTYCjXvRuGgg-XGFAM2bxguu270Cqh0LMnVKE5bcB28h1wJYgRH9xEm1-aoz6kJuVzlR2BipxlHUX4TpwDULdUHQInQPVMOd0d4h_9N2jmaalDwRiLW1vixtzSbAlxa7QVEuW_70z-bQf6QPqWc6iw3lzBuiN0qMcE_ByHWLohi0yywnILZlMrKuJTr33TKiIROh07HvNRCBojnz9WgzsmGGKP9wz-IIII4a2YI7jR3vJgNxzMiczuL4p9LcgibeGjbeuPK_sRsf41ACDVBYUFCZX2XsDI7-LsaVsDODvisQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9932ce34eb.mp4?token=Rxm-lWmBXsB9WL_2vJLkj3d7AZvipVkQfCvtqb2EFDeTYCjXvRuGgg-XGFAM2bxguu270Cqh0LMnVKE5bcB28h1wJYgRH9xEm1-aoz6kJuVzlR2BipxlHUX4TpwDULdUHQInQPVMOd0d4h_9N2jmaalDwRiLW1vixtzSbAlxa7QVEuW_70z-bQf6QPqWc6iw3lzBuiN0qMcE_ByHWLohi0yywnILZlMrKuJTr33TKiIROh07HvNRCBojnz9WgzsmGGKP9wz-IIII4a2YI7jR3vJgNxzMiczuL4p9LcgibeGjbeuPK_sRsf41ACDVBYUFCZX2XsDI7-LsaVsDODvisQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇱
صورة لطاولة الوفد الإيراني خلال خطاب نتنياهو في الأمم المتحدة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91514" target="_blank">📅 22:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04338c831a.mp4?token=aObyYwZg_fwMPnwIb-_JgMn2zjMjjaeUvdGde2IDABc_S2wlPRJc-d3re6x0gnzyKb7XvUvMUICA1GMtgkCjhDDc5JnCmO8wanF7qigcjGZlWyb0H4dmt-C-fh0YCH_mEp1DGcG3iHdUCIe3_gMwNrirqf_ktCwmzUYjely-yK8RApT0B-fBmWuGqs9HD07cffrOn-H7K9zzrQ75sqy_uXT9Zhtd_iTuy7RgvqqVVCQv6kN9yN1heW9svGgFo9l07bPHT-TwUMH3YtJ2z0jLzpU2QXtwM0YvCMVoHQgY3ALuxTuyL1TcirgBGAP7k8W_qi_ArFgxVMgIntNAYoJ_uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04338c831a.mp4?token=aObyYwZg_fwMPnwIb-_JgMn2zjMjjaeUvdGde2IDABc_S2wlPRJc-d3re6x0gnzyKb7XvUvMUICA1GMtgkCjhDDc5JnCmO8wanF7qigcjGZlWyb0H4dmt-C-fh0YCH_mEp1DGcG3iHdUCIe3_gMwNrirqf_ktCwmzUYjely-yK8RApT0B-fBmWuGqs9HD07cffrOn-H7K9zzrQ75sqy_uXT9Zhtd_iTuy7RgvqqVVCQv6kN9yN1heW9svGgFo9l07bPHT-TwUMH3YtJ2z0jLzpU2QXtwM0YvCMVoHQgY3ALuxTuyL1TcirgBGAP7k8W_qi_ArFgxVMgIntNAYoJ_uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏يلوح نتنياهو بجهاز النداء ويقول: "لقد وجهنا ضربة قوية لحزب الله في لبنان".</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91513" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
ماكرون
: "سنرسل وسائل عسكرية وجنود لحماية طريق البحر الأحمر.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91512" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91511">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية النوعية داخل العمق السعودي، في تمام الساعة العاشرة مساءً، بعد قليل.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91511" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91510">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUI93CSgv6ccYere_b2jJ7qeF_kIeKdufJTbrwXbkBoIH372qyHyjVsls2fYfbQ7yoQsD28qM4J7xwEpE2dm0hHUvPANxMGskW6qTkEnzfqGx7MZrm0zacJCwQx_wYh-S3750FzONpf4NYEhfdHw5cwyPfLJvfYsN-DcIpKF0iOu4TQup4pr5nm_1MHzccttTbZ5vEEey-t1k8ttVyZZ8CiXk0yq4104WDnKbw92a8cAokVoEKfu8iguxYZ8zh0M6WeX_JoHQabXU5BDWsEZLDlMWzXAA5CQx6CtirBPCC-xghWhHfMcBbUphT0pDbFL-Qud0wtRpTHbGjD_Bb3tpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
‏يلوح نتنياهو بجهاز النداء ويقول: "لقد وجهنا ضربة قوية لحزب الله في لبنان".</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91510" target="_blank">📅 21:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91509">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfGbiPYJJA8aWXpG_eCyFgTCwAAexD5BoynlUkDckGG1R_53xEQjIbCNpgZuSsq_8XuduCAsp-xPiET0LVQJ13RMC6ZpX0eWHuvwla7SsUH1bV8usDBwYtfnjvSEoH0siuE47oPoPIwhAX_-vaeZqbtQTs4nCVpThH28QV85GojSn9p9z-ZIS-qdQY2z5whoaB0aXGSXywmLRunXz2u9I3UUb4w5EijFjx8UmsGRIc9RfC7bLLidx8rpGvoGc_fj_uy9C9FSC9Q3TWrz-K_Oi8FwOSmjLMMCG2Ff01IbuknS5B8u-p0_PUBAgooyREqj-gOMfWumtL74CzF1MvYKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
‏نتنياهو: "على مدى السنوات الثلاث الماضية، كان جنودنا البواسل يقاتلون على سبع جبهات: حماس، وحزب الله، وإيران، والحوثيين، والميليشيات في العراق، والميليشيات في سوريا، والفلسطينيين".</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91509" target="_blank">📅 21:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇱
🇸🇾
نتنياهو: ‏يا سيد الشرع، يجب أن تعلم أن اليهود كانوا موجودين في مرتفعات الجولان منذ أيام موسى.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91508" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇱
‏نتنياهو: إذا كان هناك أي جبناء آخرين لم يغادروا القاعة بعد، فليغادروا الآن.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91507" target="_blank">📅 21:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f823df4c8.mp4?token=FWOL66P6GUjG908JQDLtoLn5B1ugi--Ni5EuDiyUwuONrQosaA9jx-vrrhmGDPk7iq4zgV5A6qUuCp2544pXyNEk1O5OAtZH7eJ-K1tk3c5v-Qlnc6tc_ttlSWH77MylqE9ApVslq60idG5tDUIL3VqA7xN46I8vyxryAk_xfdXvhEF0kHtg1hU583gCEu36jcDz2MsNJmemERbBArLQUw-c6eHh_kbUoJ4auCT2Tv9kJyDt_petW2adjWyZ_DQjw35Mg_m4C9xStS2a4SoEkFp0ZNpCjuTpXFGbpC1KR4wc84DDOjbBbEG9pzCG1iKcnm_VOulXkyc5HCKHFa6mSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f823df4c8.mp4?token=FWOL66P6GUjG908JQDLtoLn5B1ugi--Ni5EuDiyUwuONrQosaA9jx-vrrhmGDPk7iq4zgV5A6qUuCp2544pXyNEk1O5OAtZH7eJ-K1tk3c5v-Qlnc6tc_ttlSWH77MylqE9ApVslq60idG5tDUIL3VqA7xN46I8vyxryAk_xfdXvhEF0kHtg1hU583gCEu36jcDz2MsNJmemERbBArLQUw-c6eHh_kbUoJ4auCT2Tv9kJyDt_petW2adjWyZ_DQjw35Mg_m4C9xStS2a4SoEkFp0ZNpCjuTpXFGbpC1KR4wc84DDOjbBbEG9pzCG1iKcnm_VOulXkyc5HCKHFa6mSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏نتنياهو: بعض قادة دول التي انسحبت وفودها شكرونا سرا على إنهاء البرنامج النووي الإيراني.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91506" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91505">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
‏انسحاب وفود عدة دول من قاعة الأمم المتحدة عند صعود نتنياهو للمنصة لإلقاء كلمته.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91505" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ca26a1b3.mp4?token=OAA3ZycGAc9DcxJHltk7r5OpGLiZh_zK2kFce4RONva5lH1MlPNCUiUJHZbOwMW1Y4lF3i3kSs9PnvZ43jN_JCqSkfi-2RBOMD3VZ-KUiGo5VuQvBIbl71bHZaHMrjTmnehgry2D8Nf58WJW-7uo31svhfGCepvSuAbGP8jWAmYlQYjVqk7J-g39nHImZl7v8YUyP_e-WyPEMc6Jk8vAvwgcfgJkILXKkeZ-CKGcIb-ywXda7xRlNJbOhkSM6bG3nOUqyZ5-M253WO6puxyZntJva6SKjFtcSesKETH319cyo3Q7xES9YQkqjp_A5lTcFIBgHxH3hc9B7xgJ9F_56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ca26a1b3.mp4?token=OAA3ZycGAc9DcxJHltk7r5OpGLiZh_zK2kFce4RONva5lH1MlPNCUiUJHZbOwMW1Y4lF3i3kSs9PnvZ43jN_JCqSkfi-2RBOMD3VZ-KUiGo5VuQvBIbl71bHZaHMrjTmnehgry2D8Nf58WJW-7uo31svhfGCepvSuAbGP8jWAmYlQYjVqk7J-g39nHImZl7v8YUyP_e-WyPEMc6Jk8vAvwgcfgJkILXKkeZ-CKGcIb-ywXda7xRlNJbOhkSM6bG3nOUqyZ5-M253WO6puxyZntJva6SKjFtcSesKETH319cyo3Q7xES9YQkqjp_A5lTcFIBgHxH3hc9B7xgJ9F_56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏انسحاب وفود عدة دول من قاعة الأمم المتحدة عند صعود نتنياهو للمنصة لإلقاء كلمته.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91504" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxB7RUUmqc78saS301BSlMQRD_iRDzDtONJwJN_-Pe79Kb_hRRjS0lxPONek-YUzwpoLZlgUzYzAgDxFvbJTYMkfQfx5r-Isi60M3QV35IndXMIFuGCM0qNGWENgXyFtb0qFgymJlZidVBOKEv_1EgpLoM_aTFzh2f6rjzmaMJ7no2xjnLtUSApa-W_SYxE0DKXRunZCkhbCKCHOa69CBES5COf6OdZ5BbOWLN9p2oIr3p48xm16i2Qw0b8nDgpQUC-sRB3xfYokdpMIPJkh6ffWRJsCQl1-kB55RrCHWqqgA5yCPQE-Es-wFvEwmcbqP00kLtuTGxDw67-Qcupj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر بخصوص المنشورات المسيئة لآل الصدر الكرام.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91503" target="_blank">📅 21:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
🇺🇸
العراق والولايات المتحدة يوقعان اتفاق تسليم موقع الدعم الدبلوماسي المسمى ب قاعدة فيكتوريا داخل مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91502" target="_blank">📅 21:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91501">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/naya_foriraq/91501" target="_blank">📅 21:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
🇮🇷
🇨🇳
الاعلام الغربي:
الرئيس الصيني دعا  الرئيس ترمب إلى حلِّ الخلافات مع إيران في "أقرب وقت ممكن.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91499" target="_blank">📅 20:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91497">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIXXjfv97Q6sUliTjfUbE6p8b-LzAwTI0O2Ha9ypQefIsCaHXHT2OQ_NGvkz8dr5O9qqb0UcEffq5YShAocU4XHo88KAeeYiXdQRGpIDBzmMA1FWDoZSxZS1DfHWy9hGkKlY0FgzLIQ1Zr4aSjwxDNU74SBg6gTaxkZik0Tp8ni785NhU8P7bXln5ShHPYjPcY1wegG_dQ2-7sjmAhy7oloEQpEL-i_PM9mqYawHvIDuQAlzBd8JleiKhUiKpX93Z54Jp7RE8b3iRygbll27yoH5nX1y8FCG1ZWd-tQUHnsIVU92c6jFDDmhlk2sIvdCUJh_TU3tcoaRVmUDTj15LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb07d95383.mp4?token=LG55Zk1WEZomaJv02Sd0XH6SbC_KpYMGtObzGkS5lxlapDL6CJ2Z0LqZ6npDIdhZzQ4KfM4w9M7l9hlYGXMBGMmxAg6AN02UA_P3x_AiB_TUaZ07VsqLVIoodyU9jl0fL62nqf8XiriELg86IacyLoZ-ySOsJw8xnH07BllZkHtyJ_JZ1XovY3xu-5SH4wfcYWapXlPhdSdepreSGuXBhdOhSv8iBnEHd7dxPvE4BLXFseMH12OONLrEWrKThdy_LIiq2TJNPRKTiHwwc4g1EqSgmSPAaJ30LWntrHvY-CL8le7V77x8lM0EIJBns0oIupN2k71c0CnJxSpjH0__GEP4HGQcRxsJ-Pi2wIe821qEgQgvvtYi1-CNN8KXw9ZUFFpf4pkInZ62GEGJo4EXkWWh8WS7aLoOM6UTu2Ap6fzDRn2l2OPTiBalKSe2GLT0ebyTHS0UgEA9ZimzoGRc5XPoKnu_bLNQZOs0V4J8O23QWZEiv_4Nc2hXNIlPwib9reZtS7oenI-zEWFD0lNOR3cjygqhG7M2ObU8bGA0kQ2gAz3n0Tt1Apmz49EKIqtGWXVdyBb_R3RylfAmh0yWKedmTby8LV1LaMcbFOd4cXFWgRpcVp52xC51myHgq6ReLSshBcOQBYs6UTd_nMNZ9ahPHb3S6vV5HNMhMSB5YGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb07d95383.mp4?token=LG55Zk1WEZomaJv02Sd0XH6SbC_KpYMGtObzGkS5lxlapDL6CJ2Z0LqZ6npDIdhZzQ4KfM4w9M7l9hlYGXMBGMmxAg6AN02UA_P3x_AiB_TUaZ07VsqLVIoodyU9jl0fL62nqf8XiriELg86IacyLoZ-ySOsJw8xnH07BllZkHtyJ_JZ1XovY3xu-5SH4wfcYWapXlPhdSdepreSGuXBhdOhSv8iBnEHd7dxPvE4BLXFseMH12OONLrEWrKThdy_LIiq2TJNPRKTiHwwc4g1EqSgmSPAaJ30LWntrHvY-CL8le7V77x8lM0EIJBns0oIupN2k71c0CnJxSpjH0__GEP4HGQcRxsJ-Pi2wIe821qEgQgvvtYi1-CNN8KXw9ZUFFpf4pkInZ62GEGJo4EXkWWh8WS7aLoOM6UTu2Ap6fzDRn2l2OPTiBalKSe2GLT0ebyTHS0UgEA9ZimzoGRc5XPoKnu_bLNQZOs0V4J8O23QWZEiv_4Nc2hXNIlPwib9reZtS7oenI-zEWFD0lNOR3cjygqhG7M2ObU8bGA0kQ2gAz3n0Tt1Apmz49EKIqtGWXVdyBb_R3RylfAmh0yWKedmTby8LV1LaMcbFOd4cXFWgRpcVp52xC51myHgq6ReLSshBcOQBYs6UTd_nMNZ9ahPHb3S6vV5HNMhMSB5YGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
دخان مجهول في سماء محافظة كربلاء المقدسة وسط العراق.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91497" target="_blank">📅 20:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91496">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXLZ-FVCtU9kT7-ZJd_0fekkl9LkPxWcbGrAtsNuQ23IODRLVN1c32BwvMgECE4I1MUIkXs6eNF5HMLo9OAVNVnHF2BMK72ZU_CfSk8e2fVxErtxMHAbxNURSb6zEuxylP0R_zrtQWwGL08IAmY_G2IDO5EHA3ygWlBAq55PFK853Z5ge00c0SD6v7wG9FGn4p8Fbc8J-UBMrDJCaWb3CG227aAOqVxG7H184gxN5puB4WJ6Rtf0NlKfZxkxiRKnYbXWs6as0P-aYwSy_KHJ4t_O3Nyf9P0xRF_W6zsCQCvpDeos9iyBooXhdvaVhpQeBkDHlGppTJax8BGRlil_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد للطائرة المسيرة السعودية التي تم اسقاطها بالحجارة في صعدة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91496" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91495">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
انباء عن اطلاقات صاروخية من عدة مناطق في الجمهورية الاسلامية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91495" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91494">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
‏
رويترز:
إن شركة فيتول اشترت ​ما لا يقل عن ‌25 مليون برميل من الخام العراقي في سبتمبر أيلول.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91494" target="_blank">📅 20:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91493">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6dSIKiq_QjeUqgHlP7_j9_lDZnc6PlYJFcXmlTSiZ2TMBvcIZPZ2FPjYFx7bkhv4dobWnhiJl1FVDM_ExVS2Brjye6e3aKO8BOAXIu_gFSFemE8n__49RUbLu4zGFS38Qc2PkJdh9hG9slrSXvZLMtdbmGwyXo_mW0Fk_HraCS_g4z4ASHNjZb0crhlQDml6kU-9IHbLE-yNjlOpE-xo4mddetkBzByErDCFE3-Pbh7KdlfQjW8M6rnauhjRJLDyCeFE6NyClCLEm_6uwJoRrUAIoM1G4PGK1OHrGdeVJcsYQSd49ZQjvJyEg8dSUPU7mvBA7mEUCE_xJlJWcSc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مئة يوم على عمر الحكومة العراقية بين إخفاقات و تحسن ببعض الملفات</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91493" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91492">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyYXSJfqmIf7skDlWDJFf9u6qSDoJcKcIvOLUes2RvpQmUJ8gK_ICrm5FEBPsgZ8SIJCK674PJ8Olzz0J1_vXJC01Qur5QESeyRmFZuuJ_rjzYq2A1FhIHPmmpGUVVRIYypcoVmpMPzrvMC0NTw-odxN_fXxTVTOvLfcc0YlX5_27j5pwI9SP3mLN-TlrjvWQuQ_CqjYiwYPjFLc_nIUAHalZKttKo4f2sOITWaWqrozKnIK4dhcG9fQOaxadDBKBI6IPOVikVj0wPDv1WWpaQrovpfUAQ-22kEvBJFun4I3jDlpkv0gfkszi-dcA8bULi57AzyBNKmZmwAJUy8Fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
تهانينا لأمريكا على تحقيقها نسبة 5.1% خلال عشر سنوات
🎉
. ما شاء الله. فلنحتفل: لقد وصلنا إلى أدنى مستوى لنا بعد عامين.
‏هل أردتَ إعادة إيران إلى سبعينيات القرن الماضي؟ ألم يخبرك أحد أن إيران ليست مكانًا للهواة المتغطرسين؟ سنعيدك إلى أسعار السبعينيات، بالإضافة إلى ارتفاع أسعار البنزين، ونقص الديزل، وارتداء البناطيل الواسعة من الأسفل. استمتع بالحنين إلى الماضي!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91492" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91491">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي يصرح بخصوص الاتفاق الاميركي الايراني الجديد:
المفاوضون الأمريكيون والإيرانيون في نيويورك يستكشفون مسارًا تدريجيًا للخروج من الحرب، يتضمن إعادة فتح طهران لمضيق هرمز، ورفع واشنطن لحظرها الاقتصادي على إيران، وفقًا لمصادر مقربة من المفاوضات.
أصبح المضيق هو نقطة التفاوض الرئيسية في الجهود الرامية إلى إنهاء الصراع الذي يشهده منذ حوالي سبعة أشهر بين الولايات المتحدة وإيران، حيث تسعى إيران إلى تخفيف الحصار الأمريكي الذي يعيق اقتصادها، بينما تسعى واشنطن إلى ضمان حرية الملاحة للسفن في طريق الإمداد النفطي العالمي الذي تمنعه حاليًا طهران.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91491" target="_blank">📅 19:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91490">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇷🇺
🇺🇦
أوقفت مصفاة كويبيشيف النفطية في روسيا عمليات تكرير النفط منذ يوم 22 سبتمبر، وذلك في أعقاب هجوم بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91490" target="_blank">📅 19:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91489">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610cfa459d.mp4?token=cWuy1wSZIstVC6WXQlK63lOkeDHkvW9RqbKPHQXOFn-kEwwkCfSJ9lKDEPUNpijATwye_qa9ZyanOEFSV7EVS4f-TiYoCheGVYfbZkoixn0e9SFAxuxGv6MyV5RZQ9yEp81N2lNG-UdaSgI0Et5Mw6WVpO5X6zEmI9QAjvZyssNSr4-ZfK5w9qwOI4cYxiOopk4AJvEtmH1aEznDj4cRcpy5zhYzi44J3Ttmmlhn9ZZw5ITKoa4MVKjC6ZjMw3JJgSQm4xWGw2KE2iYyIaqONZZ43NIK07Yiva0k6JuQMOBMQ7Zib7N50qlYRuIPnz6B2XJEvA6bATz2EqznbUUkmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610cfa459d.mp4?token=cWuy1wSZIstVC6WXQlK63lOkeDHkvW9RqbKPHQXOFn-kEwwkCfSJ9lKDEPUNpijATwye_qa9ZyanOEFSV7EVS4f-TiYoCheGVYfbZkoixn0e9SFAxuxGv6MyV5RZQ9yEp81N2lNG-UdaSgI0Et5Mw6WVpO5X6zEmI9QAjvZyssNSr4-ZfK5w9qwOI4cYxiOopk4AJvEtmH1aEznDj4cRcpy5zhYzi44J3Ttmmlhn9ZZw5ITKoa4MVKjC6ZjMw3JJgSQm4xWGw2KE2iYyIaqONZZ43NIK07Yiva0k6JuQMOBMQ7Zib7N50qlYRuIPnz6B2XJEvA6bATz2EqznbUUkmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
كادر قناة cnn سمح لهم بالدخول الى البيت الابيض بعد قرار المنع الصادر من ترامب.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91489" target="_blank">📅 19:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQnfcM_imGPxWLrAmURj8yfvKyix2qSZU7lBcoC4DjC5tvGNHUX4f4CIVni81eMm-7t7LbkL8zHGmy8VdczmfMEUhf86-1UnfB3B4zllqDSOTLmZyLrVV_jhM9uqbtNpvcaAqcX0T0g6v5YA_gYhrIl8ORrJ7JS4rMpWkWSi5Rrp954Do0Wb54DXghPaLPhNBK14oJurtitf1TTeQCfu_x8DFozbtS6cJ5vvSzPthpSQ27skxCIbm5DwTcy4B8-wB1n8n158D_Cg_Zz_GemT1dB3kjLZb5eHZtu7qyAWROAJhvc0x-3v2ltzKNyMtDcBjQ1DcTqX8AX8QiMkHGYmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
النفط يعاود الارتفاع سريعًا ليتجاوز سعر البرميل 107 دولارات.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91488" target="_blank">📅 19:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇸🇦
رويترز:
تعمل السعودية على إعادة تدفق النفط الخام عبر خط أنابيب «الشرق-الغرب»، بعد توقفه في 11 سبتمبر إثر هجمات بطائرات مسيّرة، فيما لم تُستأنف بعد عمليات التصدير عبر الناقلات من ميناء ينبع على البحر الأحمر.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91487" target="_blank">📅 19:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6CVemFgNpxMbFi5fs9g4ehnJYt2aQ2lBymeY9D1CaJAQa26V7a1KrKFRGtOMB77f7j0N5qWpeBokxiyLobwdWY3GUIt4Q6vYt2umLfdlaKkiIG7H66wtwH6-Cur9u7eB_l6STLjFW1ZAQCbKe5lwh8c95J12XV5ZZzu0mU1iqYU4hpDuMZ6DolEFAAhyvZTv6PzaRvNfUb0hcVfawfg8S-9H_bzbO7fYJOApU0pl5-w45vkKm79iNcmMYil36uP6v2k-YWsa0aFIJyP-uvL8WIwPtes3uLpAOPoLxyfkvhT32Q9rFJx6NxWcxuLY8ko8D_2UE_5hRMwbdAiX9Te0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
استنفار في المستشفيات لاستقبال عدد من الجرحى في صفوف الجيش السعودي، إثر القصف اليمني المستمر على القواعد التي ينطلق منها العدوان.
بدري على الحوثي
يلمس اراضيك
😆</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91486" target="_blank">📅 19:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
كتائب حزب الله تصف الشركات المساهمة في إحكام الحصار على إيران بلا كرامة وتدعو إلى كسره عبر  دعم المنتجات الإيرانية وتشجيع تبادلها.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91485" target="_blank">📅 19:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
كتائب حزب الله تصف الشركات المساهمة في إحكام الحصار على إيران بلا كرامة وتدعو إلى كسره عبر  دعم المنتجات الإيرانية وتشجيع تبادلها.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91484" target="_blank">📅 19:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3038b2edc.mp4?token=P1kms9sYJIbuxFVoZRXTlMpPnNheRDRMQEe-vGxZKHzl6lJBhuAlfpiZnKVhYxF9JEhyaCiCjfDSNlvDZ4dCh5UuBQhtwD74c8PP72cRIC2SNpWmdLPjSH3aOET2mmIUgJpTrsBuhvoVgu78jvSIWUdQCuc6Y1YHDOx1GhOJLKV__AwCjaqSIvWcG7ZeFPnbNJsqu6akckAodgfl1QB5ww5oI4Hq1vTYtRi0vM2wybFmvj27TobLhelck8_NC9FXx-XQPofGuwBtWnPPuBFRpTGYQ9a2QAcVUTvqidflRYujw8Nj1SUgg4Wt_8k975i-SVMCkrAzlKKHRgrGwZqFgUQHTCBd6pe02liKBgEVxghWz0NWguMGRJVPtGLrBzJM3ZBwWqj2YHPW-RmfUe_ocE3FxOrOnbD9F7CbtJh5kN6Df7qov2hyPZIuPWhj7paf5ywQfrbK7wgdstvYgquiwXpqZg9bnAfZAy_w0A01T_PgOVdSOEuunSocXfabrzEZoxNhCNWoKcHAJCJTS5U5MwTZt_OH-GQxq2nAwGFqfvYy2q0tOqs3QkXMshWEtk9OL3LNUMB--sz1l2O9MgCF3AT4bbTwiri0eVn5-4fSBssKeU9KnaCKRVLqHBLORICsNc0JHKtcszW80cWN_ANNnxeNwzZmV1Ghdu__gON-CHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3038b2edc.mp4?token=P1kms9sYJIbuxFVoZRXTlMpPnNheRDRMQEe-vGxZKHzl6lJBhuAlfpiZnKVhYxF9JEhyaCiCjfDSNlvDZ4dCh5UuBQhtwD74c8PP72cRIC2SNpWmdLPjSH3aOET2mmIUgJpTrsBuhvoVgu78jvSIWUdQCuc6Y1YHDOx1GhOJLKV__AwCjaqSIvWcG7ZeFPnbNJsqu6akckAodgfl1QB5ww5oI4Hq1vTYtRi0vM2wybFmvj27TobLhelck8_NC9FXx-XQPofGuwBtWnPPuBFRpTGYQ9a2QAcVUTvqidflRYujw8Nj1SUgg4Wt_8k975i-SVMCkrAzlKKHRgrGwZqFgUQHTCBd6pe02liKBgEVxghWz0NWguMGRJVPtGLrBzJM3ZBwWqj2YHPW-RmfUe_ocE3FxOrOnbD9F7CbtJh5kN6Df7qov2hyPZIuPWhj7paf5ywQfrbK7wgdstvYgquiwXpqZg9bnAfZAy_w0A01T_PgOVdSOEuunSocXfabrzEZoxNhCNWoKcHAJCJTS5U5MwTZt_OH-GQxq2nAwGFqfvYy2q0tOqs3QkXMshWEtk9OL3LNUMB--sz1l2O9MgCF3AT4bbTwiri0eVn5-4fSBssKeU9KnaCKRVLqHBLORICsNc0JHKtcszW80cWN_ANNnxeNwzZmV1Ghdu__gON-CHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇺🇸
استعراض اميركي خلال حضور الرئيس الصيني في الولايات المتحدة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91483" target="_blank">📅 19:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaPeI2OB0s3fkQVF7A5DVBBFrn4PSioybAe6b7L3xWFkL46-h_t3ssJGZswWuccxMuDtx1uz1_cOfhEFurh8qn7b22MthEK1qQfaV4UvHT9SW8V74HBO_-bqbn4iqwMs2W3Vx_4vRxjqWbqZFRJF4q8a_k3ompiuK6vJIggcvnnNS-gS27sS5jndyMpanO9fYPN6spMRF_MtGf9EqhNPwCTF-vZOgiJC1mfsAzRYPlnlwq8ohTd4Ed9quPyE2RulUqw6wWqKQ4-n1OiLcx_xJJqn04kE1x8dm-qQBJCTdBcH0N6I5DC7AzYkpemvEr71maZIlFEJpHIN_duI-CCejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انفجار جسم مجهول اخر في سماء العراق.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91482" target="_blank">📅 18:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
🔻
تعليق رحلات شركات الطيران الإيرانية من وإلى الإمارات بدءا من اليوم وحتى إشعار آخر.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91481" target="_blank">📅 18:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjuRqNVXAyKn4_1_H6k8PDvQeQUtWeFrWcKmnnPKDwleesUMO5NIFUOl8MG3iM48PIk2vVHTmoaSXIy_lzOE8LXjHJ9KtehxHEbSgTqrFA7P5XOlgyYkIfFbI0EF4MA5RptF4IhxmpAlDt8PC68J9tSPJSyiAZSKisSKKAyE0GWmN4QXcPDGE7P0hQCmzywinNyxA5YxaAoN6U5WF9VPYcFPuRdBZMGwOAHo1DezqHiBumJhdba4kunEghl9lBaMueasTZMQHg2V8lBlkphYifhm6Eml4CROA4hHYHFqQcv_-Tfdj71PlOOp_r512zJCZFGJ9sZaqgGZr3uFcuO0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إستمرار إرتفاع أسعار النفط حيث تجاوز سعر البرميل 106 دولار.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91480" target="_blank">📅 18:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية في تمام الساعة 5:50مساءً، بعد قليل.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91479" target="_blank">📅 18:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية في تمام الساعة 5:50مساءً، بعد قليل.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91478" target="_blank">📅 17:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏رئيس السلطة الفلسطينية محمود عباس يبدأ كلمته في الامم المتحدة عبر الفيديو بعد عدم منحه تأشيرة للمشاركة في اجتماعات نيويورك</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91477" target="_blank">📅 17:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
تبادل وزراء الخارجية الإيراني والأوكراني وجهات النظر حول كيفية حل مسألة الهجوم الأوكراني في يوليو على سفينة إيرانية في بحر قزوين.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91476" target="_blank">📅 17:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91475">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇱
مسؤول صهيوني:
إسرائيل تتابع الأنشطة الإيرانية في منشأة تحت الأرض بالقرب من نطنز وتقدر أن جولة جديدة من القتال قد تحدث مع الولايات المتحدة او بدونها.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91475" target="_blank">📅 17:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91474">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgItg9EECop-TPjnb3Cbs-YVH3P8o3F-wpEyFgo64Px2aGIAG5quTreQUsrNAo5i5aTsfknlML3Cz_GYTKHaGaXS-OEYDjXGCaK24zH-Xi0dVIgujhcVGnUJvyJ15ACQZyAVa2ePK92SZVSEV2Q8FrUE4GdmPOWFJsllrzyUcHlSCtROSvwUXBjq72oVlSO0hmTLk3IasHejfp1hJwJnQJrbJE-Cs4alazuVehwAMpNmaBSl6Fr5NJIVlPbvkoEEtRhFrF4PzdYPgJbUTjX0mvNG2IXgrD-edhkuk3xxOgIs2o8wZNvM-jwZSDcrdTY52quba36SMKitRuEhdDHRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحشد الشعبي يحبط مخططا ارهابيا لاستهداف مواقع عسكرية في محافظة الأنبار غربي العراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91474" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
