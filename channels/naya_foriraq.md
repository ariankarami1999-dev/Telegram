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
<img src="https://cdn4.telesco.pe/file/eG0qZKvaRMxbfxvlzPD7B7QePsfp_FTONuD7ef_SMyAcQMiWDpOmm31T6QpFetXOOA73qRU74z7TvgVEK89LvFFHkPIcWhg6dXYQj3wU8kSVr7KWp1SO-BUGNOiNy_nbKY7fpM8GZbrptiXObpGVsAq5Yokg4E1qZ5lZ12stXTfgISsILcuf4QMGXDTdH_ir0bDPdXLKCUl4MOqxc4kA2cLHgK-VYyjw4Yca3I0sjtZnCdOLvDolm1cn4IXWQQBlbGjY7_RrdAla4iiIymU12yB9m0zCABw1MQITpf-N34h9HVZf6rFWKqSzUgSZVUmTu6LNzwtDJ9uTpGfuw8qZAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-79773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
وزير الخارجية الباكستاني:
التفاوض بين واشنطن وطهران يدور حاليا بشأن البرنامج النووي والأرصدة الإيرانية ولبنان ولن تكون هناك رسوم عبور لمضيق هرمز أو أذونات وتصاريح.</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/naya_foriraq/79773" target="_blank">📅 13:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حدث أمني في أنقرة</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/naya_foriraq/79772" target="_blank">📅 12:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79771">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حدث أمني في أنقرة</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/naya_foriraq/79771" target="_blank">📅 12:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79770">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇫🇷
أ ف ب: رصد إصابة أولى بفيروس إيبولا في فرنسا.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/naya_foriraq/79770" target="_blank">📅 12:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79769">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5943b6171.mp4?token=FNGvHXoNUnlHyycwX3fgNalVJ6UbWkYPFl2Yk6FOCK79zHrgdfCzLTSY_b8n17EWPWzx2_NI3U2U1tiE-SxUlPXqbTGHvj-jECSEZv7zwN_0fMdV-7WzHk-M2-48bYXLGWPLqh0BkptgKnDtdDu1rxQ03yalo2olpxn6qPmYVba2y0mvCfiDc-DitULOjnma1YfJUXdBIGamGIRC-vtFScCyxvy8Gm7r3PLjnIY_xdxrrGmTCh6jJ6RnCu_q8mCcbmRVTt5tjoBQaI3fKNKM9r70x0C_GYmbx1h6tsaLaFafblJKQ4DhsUt9UZIVIIS2gycrPuCG896AU3t-T-0nUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5943b6171.mp4?token=FNGvHXoNUnlHyycwX3fgNalVJ6UbWkYPFl2Yk6FOCK79zHrgdfCzLTSY_b8n17EWPWzx2_NI3U2U1tiE-SxUlPXqbTGHvj-jECSEZv7zwN_0fMdV-7WzHk-M2-48bYXLGWPLqh0BkptgKnDtdDu1rxQ03yalo2olpxn6qPmYVba2y0mvCfiDc-DitULOjnma1YfJUXdBIGamGIRC-vtFScCyxvy8Gm7r3PLjnIY_xdxrrGmTCh6jJ6RnCu_q8mCcbmRVTt5tjoBQaI3fKNKM9r70x0C_GYmbx1h6tsaLaFafblJKQ4DhsUt9UZIVIIS2gycrPuCG896AU3t-T-0nUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
قصف أوكراني يستهدف مواقع في شبه جزيرة القرم الروسية
أوكرانيا تتلقى دعم من بريطانيا وفرنسا وألمانيا وباقي دول الناتو</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/naya_foriraq/79769" target="_blank">📅 12:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79768">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇹🇷
هزة أرضية بقوة 4.9 ريختر تضرب سواحل ولاية موغلا التركية.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/naya_foriraq/79768" target="_blank">📅 12:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇸🇾
خلف البدلات الأنيقة والخطابات المنمقة والصور اللامعة التي جسدها الجولاني تقف حكومة لا تتردد في إرسال أبنائها إلى نبش القبور وارتكاب افدح صنوف الظلم ثم تتحدث عن القيم والأخلاق بوجه لا يعرف الخجل ؛ حيث يظهر الفيديو لحظة نبش أحد القبور واستخراج جثة أحد الأشخاص بحجة انتمائه للشبيحة في قرية عربين بريف دمشق.</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/naya_foriraq/79767" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79766">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🛫
الاتحاد الأوروبي بشأن الطيران: نصحت شركات الطيران بتجنب التحليق فوق إيران والعراق ولبنان، وتوخي الحذر في بقية أنحاء المنطقة.</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/naya_foriraq/79766" target="_blank">📅 11:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79765">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYq9_No27ZNuGJdoElK5eePkmqIh0pCs5HBpcwj6mrMBwYm02sPMvEtmHwzITK2UgMyE9RWsR-rP3jlyvXn0YZpZVlX2OvFCktPXcwaD5bofxg8Oimq3Rjry4vfa4IFgtUozsdo8xLTpjPhYPTogtrvBeNMNXNP-sO-agPFPUSFIGILuE2ZTeb7qWWKpJ8RKhFuxHJhoKi073mF6H1l474YkG_riTcMPX96szo2wnuM89MY7r_sNrislYUq1mP0gJhiT3pAQnhLsw7wIFVQsvrmSroTOck6nX8X5sVGXqsYZWPgDiHrobLOsj3--MI2C-bLOCSPiIpH1pJGzp8KCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
غضب واستياء شعبي واسع في شارع الكفاح كعبة المواكب الحسينية في بغداد بعد صدور توجيهات تقضي بتضييق ومنع نزول المعزّين إلى الشارع حيث يُعد هذا الشارع أكبر وأهم حاضنة للمواكب الحسينية في العاصمة وشاهداً على أضخم التجمعات العزائية ؛ الأمر الذي أثار موجة من التساؤلات حول القرار الغير مألوف بحق شارع ارتبط اسمه بالشعائر الحسينية لعقود طويلة ؛ متسائلين عن أسباب هذا الإجراء وما إذا كان يمثل بداية لسياسة التضييق على المواكب الحسينية والشعائر الدينية.
🔻
نسخة منه إلى القائد العام للقوات المسلحة</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/79765" target="_blank">📅 10:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
🇰🇵
مشاهد بثها الإعلام الكوري للزعيم كيم جونغ أون أثناء حضوره حفل تدشين السفينة الحربية تشوي هيون في مدينة نامبو الساحلية، وهي إحدى السفينتين الحربيتين من فئة 5000 طن ؛ حيث أكد أن البحرية ستمتلك أسلحة نووية وستُكلف هذه المدمرة بمهمة الدفاع عن الساحل الغربي للبلاد.</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/79764" target="_blank">📅 10:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qovjdFBJowfbnooNlM4O5nw5T9ief0kdqLfMnVfC6grTecEkUB9WnqqPITQidNLduBG2sidG6frzNlP_A5XYlF78o--6J0AvVAnrDtdPy_SPCy87La9qtNIbpeQy-f6l2f8Dcdkay2L65He1UiCW165771LruT3oNfLj_OCbgqORzqQ6bp2C1Hp_PIW45eHP-qpXTksOVaqpjzA49KUjg29OGuMn6VnfrdXCI3PfaY8D82NigxboBwI_SpvcXkpUN_eKY1YRZWVuyMhoYXVPNBfthwoDBB-1sIUCWLNUhKUG39pWwEUb9Pr-kGQTI8CBJ8wFVmKFfsnQi8zRjmDKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
شركات النفط الكبرى لا تخفض أسعارها في محطات الوقود بما يتماشى مع الأسعار المنخفضة بشكل حاد التي تدفعها مقابل النفط.
هذه الأسعار تنخفض بسرعة كبيرة! بمعنى آخر، يتم "ابتزاز" العملاء.
لقد أوعزت إلى وزارة العدل أن تبدأ فورًا في التحقيق في هذا الأمر. يجب أن تبدأ أسعار البنزين في الانخفاض بسرعة أكبر بكثير مما أراه!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79763" target="_blank">📅 09:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zli9DFUqBFr17v_NMmj4a2P3YmranS0zK5YzRXRSz9tkkKF2gs_W8O7OfeaOp6AqIOirlitEUpkZta4PDVFrZlaujMW6v5XP2q4kZ2qtpf44UjerQdewgmlV9vupejg_6dStPW7BKdyKOS1R9G8XfuK11thmY-UjbPUTxhqCL-Qjqj_AmQ25Zpen1HE0ioEOG_K7Isu-8bpDYaVsFRoREmzuGW0r5qSUbUl4qnHoB2GRoCYFVZUIKr3Co3znN4sYpcxopg96fouiztDGxwLhxEuXgkgkrcJG7dfZ7NjmibrdBxx13VnrsaY17zaL0OccUR8qT3-TYZiKJpXpPTtI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
إذن، إيران على وشك السقوط، مستعدة للهزيمة، مستعدة لتقديم أي شيء تقريبًا، ولأول مرة منذ عقود، تحترم الولايات المتحدة ورئيسها، أنا، ويقرر مجلس الشيوخ الأمريكي التصويت على قانون صلاحيات الحرب في توقيت سيئ وبلا معنى، ليخبروا الراعي الأول للإرهاب في العالم أن الولايات المتحدة لا تحب ما أفعله بها، ويجب أن أتوقف، وبذلك يكونون قد قدموا العون والدعم للعدو. أربعة جمهوريين خاسرين صوتوا مع الديمقراطيين، وسألت إيران شعبي: "ماذا يعني كل هذا؟" لقد جعل هؤلاء السيناتورات مهمتي أكثر صعوبة، لكنني سأنجزها، بطريقة أو بأخرى، لأنني دائمًا ما أنجزها!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79762" target="_blank">📅 06:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9319476213.mp4?token=dTV_sn-n4wBmDaX7b4CQg5l5NdFFE_-LZNuaa2V8JOkd-BQzbYX3kmLZ5oNOxE3QPBUy4jQJUYoRx-BBiDy2Pjs63Akxt1uVDSXAVZ5sYUapYEWZginlSSA76-FoF4okPmrcT8ED3nWSbT3CpZO2zdeOM9Pcla5jv4l1t1PUV5jrD9gzC_e_YuXmqgbNU6W4ltxwO2paxn0lEekBMFZJmzGGF-3iChsgR0uJZ8zZwwdZI2o7dwI0auzzQE1mq8F-DSsZp9U1upC2w5FIxcIgbK0bY200ZFoJ07qkKNVQdJFfFXAfzHfValz58e6mU0hwsqtEY0ym4k8go3MB81AtxwhC08xCegRsoZgs-DLy2BrodgHgONmlfQcF9_8C3RJZhiGY2lWi9gh49Mq48qPFXjaWm-Ib--dETAAavq8zOeGRx3M0rnpRfJHdVxUOTANkxhk_mYYFgnv2B0E2BCPuaQvCewTS4edMPE6vDupcMiGucPv3pAAXJBhpJWIepUGR8FpYMUB87Ry6BUy4xYLMcBBq8nkgFvON5e9Qcac3fapgcIvxzIeLxrjMdk1HtpB3A7jn97GB1YZza_UnaV1cf01uEX4umGMp-JTHLbHN4Ig0m8KR5LidK_IlNP281W9StYUqe2yynEeckOjlTccj_efU0MAccEkCZ8usIJmmPIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9319476213.mp4?token=dTV_sn-n4wBmDaX7b4CQg5l5NdFFE_-LZNuaa2V8JOkd-BQzbYX3kmLZ5oNOxE3QPBUy4jQJUYoRx-BBiDy2Pjs63Akxt1uVDSXAVZ5sYUapYEWZginlSSA76-FoF4okPmrcT8ED3nWSbT3CpZO2zdeOM9Pcla5jv4l1t1PUV5jrD9gzC_e_YuXmqgbNU6W4ltxwO2paxn0lEekBMFZJmzGGF-3iChsgR0uJZ8zZwwdZI2o7dwI0auzzQE1mq8F-DSsZp9U1upC2w5FIxcIgbK0bY200ZFoJ07qkKNVQdJFfFXAfzHfValz58e6mU0hwsqtEY0ym4k8go3MB81AtxwhC08xCegRsoZgs-DLy2BrodgHgONmlfQcF9_8C3RJZhiGY2lWi9gh49Mq48qPFXjaWm-Ib--dETAAavq8zOeGRx3M0rnpRfJHdVxUOTANkxhk_mYYFgnv2B0E2BCPuaQvCewTS4edMPE6vDupcMiGucPv3pAAXJBhpJWIepUGR8FpYMUB87Ry6BUy4xYLMcBBq8nkgFvON5e9Qcac3fapgcIvxzIeLxrjMdk1HtpB3A7jn97GB1YZza_UnaV1cf01uEX4umGMp-JTHLbHN4Ig0m8KR5LidK_IlNP281W9StYUqe2yynEeckOjlTccj_efU0MAccEkCZ8usIJmmPIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجارة البحرية البريطانية: وردت أنباء عن سيطرة أشخاص غير مصرح لهم في السواحل الصومالية على سفينة شحن تم تحويل مسارها إلى داخل المياه الإقليمية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79761" target="_blank">📅 03:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">توقف سكك الحديد في عموم المانيا بسبب اضطرابات في الراديو الرقمي للسكك الحديدية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79760" target="_blank">📅 01:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79758">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عاشوراء عهدٌ متجدّد؛ أن نبقى ثابتين على الحق، أقوياء في الموقف، أوفياء للمبدأ، ما بقينا
عاشورا پیمانی همواره استوار است؛ اینکه تا زمانی که زنده‌ایم، بر حق استوار بمانیم، در موضع خود نیرومند باشیم و به آرمان و اصول خویش وفادار بمانیم
Ashura is a renewed covenant: to remain steadfast upon the truth, strong in our stance, and faithful to our principles for as long as we live</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79758" target="_blank">📅 00:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79757">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
مجلس محافظة ذي قار يعلن تعطيل الدوام الرسمي يوم غد الأربعاء .</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79757" target="_blank">📅 00:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
العتبة الحسينية المقدسة:
لن نسمح بأي شكل من أشكال الاعتداء أو التجاوز على كرامة الزائرين مهما كانت الأسباب.
وفيما يتعلق بالحادثة  التي شهدتها مدينة كربلاء المقدسة مؤخراً والمتضمنة تجاوز عدد من الأشخاص على مجموعة من الزائرين، فإن الجهات المختصة سارعت إلى إحتواء الموقف بشكل فوري واتخاذ الإجراءات اللازمة لمنع تفاقمه، كما تؤكد العتبة الحسينية المقدسة أنها لا تسمح بأي شكل من أشكال الاعتداء أو التجاوز على كرامة الزائرين مهما كانت الأسباب.
﻿</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79756" target="_blank">📅 23:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭐️
على غرار سياسة آل خليفة المتصهينة في محاربة الشعائر الحسينية..
حكومة آل صباح في الكويت تجبر مؤسسي "حسينية آل ياسين" على إيقاف جميع فعالياتها الحسينية وإغلاقها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/79755" target="_blank">📅 22:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">المتحدث باسم وزارة الأمن الداخلي الأمريكية:  الولايات المتحدة تخفف القيود المفروضة على المنتخب الإيراني المشارك في كأس العالم، مما يسمح للفريق بالسفر قبل يومين من مباراته القادمة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/79754" target="_blank">📅 22:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
خرق صهيوني جديد لوقف إطلاق النار..
مسيرة إسرائيلية استهدفت سيارة على طريق الخردلي بجنوب لبنان من دون أن تصيبها.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/79753" target="_blank">📅 21:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79752">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5161524b76.mp4?token=U_7InbNLNz_EUrJdOWwuuW1P4QfKDqhPSQySJiwrLE2rXvi3c-gY_TUhkG-ijh2KMra_U5aisJSdGtp6LKsxRPHfnrAP7_yfG4txJZORyyWtyRr4CzR60hl1ymjCt-fyuaO3Xju1H0SIDmV1j34LJ1sj-Tw3OgGyOcCIcquP0E5FU0kUHlhkj73pkTDMinX_g_qb8U-eLZUTl540XSqduT7XWRvpOoFUHufOWUDSEzC2cFSVkZJwVoiZDIhv96Zkcftg3Yj8RwowdMaLD_nD-FcCz-5Ieu_UOWysq12aZhGGXtIZfTrUazgD8XPleF4COWuuq6jotKW-Z2quiUmfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5161524b76.mp4?token=U_7InbNLNz_EUrJdOWwuuW1P4QfKDqhPSQySJiwrLE2rXvi3c-gY_TUhkG-ijh2KMra_U5aisJSdGtp6LKsxRPHfnrAP7_yfG4txJZORyyWtyRr4CzR60hl1ymjCt-fyuaO3Xju1H0SIDmV1j34LJ1sj-Tw3OgGyOcCIcquP0E5FU0kUHlhkj73pkTDMinX_g_qb8U-eLZUTl540XSqduT7XWRvpOoFUHufOWUDSEzC2cFSVkZJwVoiZDIhv96Zkcftg3Yj8RwowdMaLD_nD-FcCz-5Ieu_UOWysq12aZhGGXtIZfTrUazgD8XPleF4COWuuq6jotKW-Z2quiUmfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب: نعمل على اتفاق رائع بعد أن تم القضاء على كل شيء في إيران وهي ليست في موقف تفاوضي جيد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79752" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏ترامب:  لن يُسمح لإيران بامتلاك السلاح النووي.  ‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.  ‏هناك تراجع في أسعار النفط.  المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79751" target="_blank">📅 20:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79750">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236a2e1e8d.mp4?token=c1-nXptQcNS6WARvEIQtoBTRqqZfuSLRbaRUE3eW87zjKIGqqpR3L-up4Xr6RWGK8qs5TO2W9kk1IAwX3PzupzHdH1-QHeJEh9hNMjRXFNFU7M8q4_laa9vKr8X6raoirJK-cUnSPoaSpgFujWMce4t2itIEuKSSU4XurK8GT6Fw7RXgGhqyAVEc5TGDEQd0q-SjUh6Kl-g6ilrNc0tSoSAAo8_1d0AMV8mnTOpREYp82gn6I1rRc-bAcuan0_K2DYE1b-Y476OjA7CuAXJFSkRruV3L33Suxr7N1teUGvb_O8jLSy9x3YMSNAuawFI3iSpyjATFnkxB_y6QtwMf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236a2e1e8d.mp4?token=c1-nXptQcNS6WARvEIQtoBTRqqZfuSLRbaRUE3eW87zjKIGqqpR3L-up4Xr6RWGK8qs5TO2W9kk1IAwX3PzupzHdH1-QHeJEh9hNMjRXFNFU7M8q4_laa9vKr8X6raoirJK-cUnSPoaSpgFujWMce4t2itIEuKSSU4XurK8GT6Fw7RXgGhqyAVEc5TGDEQd0q-SjUh6Kl-g6ilrNc0tSoSAAo8_1d0AMV8mnTOpREYp82gn6I1rRc-bAcuan0_K2DYE1b-Y476OjA7CuAXJFSkRruV3L33Suxr7N1teUGvb_O8jLSy9x3YMSNAuawFI3iSpyjATFnkxB_y6QtwMf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل: يقول الإيرانيون إنه لا توجد زيارة مقررة للمفتشين. هل هذا جزء من اتفاقكم؟  ‏
🌟
ترامب: إنهم مخطئون. إنهم مخطئون. وهم يعلمون أنهم مخطئون. لو كانوا على صواب، لكنت ألغيت الاجتماعات فوراً.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79750" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d953889d0d.mp4?token=LzBGBw2N_imMfDV5hsHChxK_sdXgLAhIYgXM928hxle8vgfJwK3cnat67-mrJMbpFm8ULnPiM51ipudMNfB6sTMt3x_BLXHLZopqEYYNidMyv7RmlXKrF7BWX2Zk-Zs0pgINOaJwjH5UHwjvxgIJ0opnuQT7cSt1amyVudb9AdK3OQaxPFO98rotYO0WmWFWtky2mtv2YcZ7ZnmRNKrU9d_q09YqHH8zMy0b2xvX8YefRx8vYJZjkiWIo9Ty9GiYbC58boOuNf8ITlUmLHS5pkicl7cXEb1Y6BneXMI1Os-83n8fCH9nVMmXt9VpUSc20gH307lxXbhAC-7E3MQz3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d953889d0d.mp4?token=LzBGBw2N_imMfDV5hsHChxK_sdXgLAhIYgXM928hxle8vgfJwK3cnat67-mrJMbpFm8ULnPiM51ipudMNfB6sTMt3x_BLXHLZopqEYYNidMyv7RmlXKrF7BWX2Zk-Zs0pgINOaJwjH5UHwjvxgIJ0opnuQT7cSt1amyVudb9AdK3OQaxPFO98rotYO0WmWFWtky2mtv2YcZ7ZnmRNKrU9d_q09YqHH8zMy0b2xvX8YefRx8vYJZjkiWIo9Ty9GiYbC58boOuNf8ITlUmLHS5pkicl7cXEb1Y6BneXMI1Os-83n8fCH9nVMmXt9VpUSc20gH307lxXbhAC-7E3MQz3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب:  لن يُسمح لإيران بامتلاك السلاح النووي.  ‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.  ‏هناك تراجع في أسعار النفط.  المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79749" target="_blank">📅 20:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏ترامب:
لن يُسمح لإيران بامتلاك السلاح النووي.
‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.
‏هناك تراجع في أسعار النفط.
المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79748" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79747">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c3f6bff2.mp4?token=pOH0vJojg5bqKjfh7CiNtvAd_BLPTQSHnzHlPQr4bXBzZ3qmDMUZFskwMwKmgwJB0MiTbyL-0zGtKXDuh9Cp4ZHR8gUuB4_H8yRPlrcLexN9p0UxpmtBtzJmFfBv-OtkciC9v1Tnyj9gKK9KwDAc8fF_KyzrvKPH5fuzZHAmbjCLDBhYyCvNrfjYIA5Kn4xmnS0oHMcZq-guoTjbnEcpA2xnxlAvQFNo2ybQ3LxJc1kPAAnoL2mTHE2rvvOheFrxeEOUYIE8zQhm9Rbks3wf9S2hmwdNUZZOcztah0aWXn9_oqBquNvqRcLpmEJkOo4CN4RihACfqg14_e31szpUzbauqvl0ZQUzBhj8ZjeUDBOCE75hglW1nnP1jGK0zEh-jRXl6x2MPH3UP5SPLDy5VvhclaEHJNRdwotIYhYpDAKyyGw8KJorB2IQCNh7svKdZDBfxSxdbYq8xNsd8-6Fqe58p3ISe2DMyFLQuOcUkGc2JA9OgyuzV4W0pz3WQ37wQ3D7gcHRrfNNXQe6yUAhGXGC8mbwDS69hOLKvI5MBRJhHjCd_cQ2TfkN5ZUXDNKCIeYkBEyfBRO5hgoTkFBync2QHFO3o-YuSOHwl6M9Gd4cUt6vkC65AK4lO815ioDXPo_gZ2YrW8qYVp7RAzDrp0bulfpM_WbYxX9lU2ZPCbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c3f6bff2.mp4?token=pOH0vJojg5bqKjfh7CiNtvAd_BLPTQSHnzHlPQr4bXBzZ3qmDMUZFskwMwKmgwJB0MiTbyL-0zGtKXDuh9Cp4ZHR8gUuB4_H8yRPlrcLexN9p0UxpmtBtzJmFfBv-OtkciC9v1Tnyj9gKK9KwDAc8fF_KyzrvKPH5fuzZHAmbjCLDBhYyCvNrfjYIA5Kn4xmnS0oHMcZq-guoTjbnEcpA2xnxlAvQFNo2ybQ3LxJc1kPAAnoL2mTHE2rvvOheFrxeEOUYIE8zQhm9Rbks3wf9S2hmwdNUZZOcztah0aWXn9_oqBquNvqRcLpmEJkOo4CN4RihACfqg14_e31szpUzbauqvl0ZQUzBhj8ZjeUDBOCE75hglW1nnP1jGK0zEh-jRXl6x2MPH3UP5SPLDy5VvhclaEHJNRdwotIYhYpDAKyyGw8KJorB2IQCNh7svKdZDBfxSxdbYq8xNsd8-6Fqe58p3ISe2DMyFLQuOcUkGc2JA9OgyuzV4W0pz3WQ37wQ3D7gcHRrfNNXQe6yUAhGXGC8mbwDS69hOLKvI5MBRJhHjCd_cQ2TfkN5ZUXDNKCIeYkBEyfBRO5hgoTkFBync2QHFO3o-YuSOHwl6M9Gd4cUt6vkC65AK4lO815ioDXPo_gZ2YrW8qYVp7RAzDrp0bulfpM_WbYxX9lU2ZPCbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79747" target="_blank">📅 20:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79746">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bd43a7e5.mp4?token=GnSVN98YrKocRu5HgPyJwSMTex_qOfFlGD1C1ev0-fWtoNZN6PxyXYONZL9uuitqBjuyTE1BWyP2q15arWcfgJKx24EdZEkk4OJDzkecIfTIgcwtUrfntOKJoEsTrepzELOx7BN809yJa4eRsQWhr7LmbOeutyb7TXjUtdNpNwjdzJjuzqbanmSf7Z0hMtH4e2GxSs3zaP5lWr8eurnWQGY4jSZZDpwVTnEp5ObN8_D-F2iM1-BAvRwu2vlNMWGjpdhEMXPBMMe37Lts1UNoPgkFxmTVHQ_YiQ93La5wL9fPFP6wr_CXD_IehtXzRh1Z3_qutthfWR_LhM83Isnrww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bd43a7e5.mp4?token=GnSVN98YrKocRu5HgPyJwSMTex_qOfFlGD1C1ev0-fWtoNZN6PxyXYONZL9uuitqBjuyTE1BWyP2q15arWcfgJKx24EdZEkk4OJDzkecIfTIgcwtUrfntOKJoEsTrepzELOx7BN809yJa4eRsQWhr7LmbOeutyb7TXjUtdNpNwjdzJjuzqbanmSf7Z0hMtH4e2GxSs3zaP5lWr8eurnWQGY4jSZZDpwVTnEp5ObN8_D-F2iM1-BAvRwu2vlNMWGjpdhEMXPBMMe37Lts1UNoPgkFxmTVHQ_YiQ93La5wL9fPFP6wr_CXD_IehtXzRh1Z3_qutthfWR_LhM83Isnrww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
‏رئيس الوزراء الباكستاني شريف:  أبلغوا رسالتي إلى القائد الأعلى بأن إيران تمكنت من تحقيق وقف إطلاق النار ومذكرة التفاهم بكرامة.  ‏أعتقد أن إيران ستتحول قريباً إلى واحدة من أسرع الاقتصادات نمواً في العالم.  ‏لا تتضمن مذكرة التفاهم هذه أي ذكر للصواريخ الباليستية،…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79746" target="_blank">📅 20:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79745">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dllgGiza6sIsgclnYtyOnnym8r7JdwoudyNOzyn8zqxTFjJ7_lV0Jey1K5pV6Zdrdq965AxXMGwDTCf9YOuuQbdvXwHy7v8ikBLuBvdEf9iTSejyTZxeydg5kWSEvwdT_xEpXiQCYIvomYkbmLEVEdy2U5D7tRnuqq_zCFAvbLJokhREdpc7ZylZHJrh6clC1tAOcFgLDI2tCDcyraNQ2IyRPeYtR9UFCi87QMJS5cW0NWplEiA031UXBpfFQK8R0yoZzhm90rms1PS2A3JbZqpOsT0_xB3BATGwvIJeSb5JmM7EWn6OPJQhB6siNkhbr2s2Xgz2uwaVtarn87ytww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد زلزال هيكلة وزارة النقل العراقية ؛ هل انتهت أيام شاكر الزبيدي في الوزارة ؟!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79745" target="_blank">📅 19:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79744">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/680209a07d.mp4?token=Ud_5GA-AFmCWpnqPIvRB1ziOOwOIgQ3hDOSHl0GZLKnz8NyB7R7jbCqcnsZbl2q033kCEczdNcAQFnSIz-OfJ6KZcppkyvw6dyun4m58MiDqiOsWm3hNWTW5Mbms-u5DxHMTm15FS9ScS09VGDCzogdhKeymFKG4hjzLulfZ3QNtrO9yRC728S27Tb2_viMh_3xbOcGDqMBHvbzVaIEnTjS_F2yLVPx8JvVw8pTiAFvxADaIxDmHLb2qM5YIMfOpw6Dgb0w5YZ0EOZ58hCBHpsuU2vfvV5YoUj1mCFlTrXlL_u11rx_K1Xex3fYQc9vYA4xmYROrYHDP-m1B9_DrlZrSa1a7sS9jK7FTNoXKj_IDrh7tRI850wnHvuENynpoCLk-4rD8S6mRt41FMQoadUfuvMM7Vn8mc4K-d8zhakwWE9eDueF2NjFJ49OM-TCgtebbprKFYivE3Zsk57OkrSA7mM58DqSZO9cxfNWr-rNIM-eUnkote_nZcpnLW0DN3GynRBbHfqQrG8CECOzoO15Oei1AuV8ukkhBXzqiFnmjQgbPOaIi54l6uN_k2VonKOebKlEqZE6wMmp4jLd6qy0RBbfYwuBI4XRgPnsPz2k7JPPPI8v75xPwk_IEmPQTximc6IuO-yQb6T0mrJ0bT29fuLKJ0OqbX_unU1OOQ0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/680209a07d.mp4?token=Ud_5GA-AFmCWpnqPIvRB1ziOOwOIgQ3hDOSHl0GZLKnz8NyB7R7jbCqcnsZbl2q033kCEczdNcAQFnSIz-OfJ6KZcppkyvw6dyun4m58MiDqiOsWm3hNWTW5Mbms-u5DxHMTm15FS9ScS09VGDCzogdhKeymFKG4hjzLulfZ3QNtrO9yRC728S27Tb2_viMh_3xbOcGDqMBHvbzVaIEnTjS_F2yLVPx8JvVw8pTiAFvxADaIxDmHLb2qM5YIMfOpw6Dgb0w5YZ0EOZ58hCBHpsuU2vfvV5YoUj1mCFlTrXlL_u11rx_K1Xex3fYQc9vYA4xmYROrYHDP-m1B9_DrlZrSa1a7sS9jK7FTNoXKj_IDrh7tRI850wnHvuENynpoCLk-4rD8S6mRt41FMQoadUfuvMM7Vn8mc4K-d8zhakwWE9eDueF2NjFJ49OM-TCgtebbprKFYivE3Zsk57OkrSA7mM58DqSZO9cxfNWr-rNIM-eUnkote_nZcpnLW0DN3GynRBbHfqQrG8CECOzoO15Oei1AuV8ukkhBXzqiFnmjQgbPOaIi54l6uN_k2VonKOebKlEqZE6wMmp4jLd6qy0RBbfYwuBI4XRgPnsPz2k7JPPPI8v75xPwk_IEmPQTximc6IuO-yQb6T0mrJ0bT29fuLKJ0OqbX_unU1OOQ0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
🌟
من جرائم العدو الصهيوأمريكي في حرب رمضان..
توثيق جديد يظهر لحظة تنفيذ غارة على مدينة لامرد في محافظة فارس الإيرانية؛ ماأدى إلى إستشهاد عدد من المدنيين أثناء مرورهم بالقرب من مكان القصف.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79744" target="_blank">📅 19:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd98c729d.mp4?token=NzCwTJ4LlKFb5TYs-hVt0SdYx3u6e49mXedLf-SZcaFLFORuM2CXpyMaQPI10m49I1f3P7tayS904r78xtbInrYJGSuhNgpoz4Wx9Od2vMCIcGdqt5V2hjX5zc-TR44jIsOIUZznhOHatq2FKVJLEC7oENUN5z-a3aYGOr4ORELoajqszkc30SYOCDWrANQk5DCT927DduizLESGmOqcoN-H94pCTUvuX0F1ZJttgDFpMXp8JjYN2FDYpAOQzmxdgk9KoLOYFxz9pYY0m_anM-U58hg7enp83PXfSt2xV_mDZe9vniAxV9dW21MRuQwes6-GTGA7AdbopvWibJUVQgFFPjkk9Nf-IcxbkxeCR9KtsOPE2_nnQE-jX5GvXw5Q_DFrhIW8Hdfyqmcny1uATqxt8tjsnO1azzDBuosdt-5c0hIrDw5WDRP6vGbYGWLi3hiQjwq3wcZiMZKyViZFVnA-9OKni9RLKJ0tnKLLwH5OjwCk32ax7HhV3Rb8B8YB1biVO7GHmzJ_Sue8mlydY-2p7trT0l4fGHTe_j-WuqdLFjFRNekLcnBLdjNS2mk3Bt5XVK3Zwyg3BHTkhKp8opPNpDfXdMpkbhpuZLem6XkKmGSiArC91v0dvgn3URAl2o-Rjt9x8ggiIt8PSbw0X1nXFVlsFBaa2DA-f2bBZv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd98c729d.mp4?token=NzCwTJ4LlKFb5TYs-hVt0SdYx3u6e49mXedLf-SZcaFLFORuM2CXpyMaQPI10m49I1f3P7tayS904r78xtbInrYJGSuhNgpoz4Wx9Od2vMCIcGdqt5V2hjX5zc-TR44jIsOIUZznhOHatq2FKVJLEC7oENUN5z-a3aYGOr4ORELoajqszkc30SYOCDWrANQk5DCT927DduizLESGmOqcoN-H94pCTUvuX0F1ZJttgDFpMXp8JjYN2FDYpAOQzmxdgk9KoLOYFxz9pYY0m_anM-U58hg7enp83PXfSt2xV_mDZe9vniAxV9dW21MRuQwes6-GTGA7AdbopvWibJUVQgFFPjkk9Nf-IcxbkxeCR9KtsOPE2_nnQE-jX5GvXw5Q_DFrhIW8Hdfyqmcny1uATqxt8tjsnO1azzDBuosdt-5c0hIrDw5WDRP6vGbYGWLi3hiQjwq3wcZiMZKyViZFVnA-9OKni9RLKJ0tnKLLwH5OjwCk32ax7HhV3Rb8B8YB1biVO7GHmzJ_Sue8mlydY-2p7trT0l4fGHTe_j-WuqdLFjFRNekLcnBLdjNS2mk3Bt5XVK3Zwyg3BHTkhKp8opPNpDfXdMpkbhpuZLem6XkKmGSiArC91v0dvgn3URAl2o-Rjt9x8ggiIt8PSbw0X1nXFVlsFBaa2DA-f2bBZv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
‏
رئيس الوزراء الباكستاني شريف:
أبلغوا رسالتي إلى القائد الأعلى بأن إيران تمكنت من تحقيق وقف إطلاق النار ومذكرة التفاهم بكرامة.
‏أعتقد أن إيران ستتحول قريباً إلى واحدة من أسرع الاقتصادات نمواً في العالم.
‏لا تتضمن مذكرة التفاهم هذه أي ذكر للصواريخ الباليستية، ولم تكن مطروحة على الطاولة أو جدول الأعمال مطلقاً. الجانب الإيراني لم يرغب في مناقشتها.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79743" target="_blank">📅 19:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660a35f99.mp4?token=VR1G5pExxJeV0iL8R1X2yt_ZXunXU_Ehbsu1QV0xJGnHspCtc6bNsOkcsvGLiA0wQesy9mZ_3ss5lgyOL6JhCTyWDqCheev7HMkj3d6z4NDN20H5xvKrNDNSI3PWVcB6EuRBBBraK3dyX0zKSBCQTEk0RORntuKrGfbBi3mjg_XM5wy_fXKbMkzY8GnaxYeDQT8pXG-0TPJqcMp_ARiRCySJtqalJq5VQRmTTlBzlGsHc1xki01EBqX67uhDPyT3tKbFJWoX3XnQRtYewTtfepaIPmyujrnH1G5u5ROh_CBQIlyCtAgk1CyxiNePJYFnUPYmTkTc4kpV1rghwmqiJCTQ4CQhBb-lw76YYowr3UQLwWAQamdHjpp1UoGy2N9EV58fIfibJpBA4WlpAyXtFJohvsZGLRDUAzstt9Egot7DRXbQvz1shiEUNP7o_PVwo12G7UP3dgxibiup4Y4s-1Xk09Lh440c_d2szK--diU-vMvybd8NswsqsR8Oe4syB-ZIBzwEGYU4iU_asj4WXWMrIsbGtsjxVyMyfQC4NT0_oHYEphCNg3zmeCMIKKP4o60YyDqqctlQEk33Mk-KahgwgXXxH1X1ILz0Iw6x6el7II3phUG9idSi38xe3QLy0ZRAPMY7iKAgEDncFTZXzbYQed-JdwuL991B0ym5-AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660a35f99.mp4?token=VR1G5pExxJeV0iL8R1X2yt_ZXunXU_Ehbsu1QV0xJGnHspCtc6bNsOkcsvGLiA0wQesy9mZ_3ss5lgyOL6JhCTyWDqCheev7HMkj3d6z4NDN20H5xvKrNDNSI3PWVcB6EuRBBBraK3dyX0zKSBCQTEk0RORntuKrGfbBi3mjg_XM5wy_fXKbMkzY8GnaxYeDQT8pXG-0TPJqcMp_ARiRCySJtqalJq5VQRmTTlBzlGsHc1xki01EBqX67uhDPyT3tKbFJWoX3XnQRtYewTtfepaIPmyujrnH1G5u5ROh_CBQIlyCtAgk1CyxiNePJYFnUPYmTkTc4kpV1rghwmqiJCTQ4CQhBb-lw76YYowr3UQLwWAQamdHjpp1UoGy2N9EV58fIfibJpBA4WlpAyXtFJohvsZGLRDUAzstt9Egot7DRXbQvz1shiEUNP7o_PVwo12G7UP3dgxibiup4Y4s-1Xk09Lh440c_d2szK--diU-vMvybd8NswsqsR8Oe4syB-ZIBzwEGYU4iU_asj4WXWMrIsbGtsjxVyMyfQC4NT0_oHYEphCNg3zmeCMIKKP4o60YyDqqctlQEk33Mk-KahgwgXXxH1X1ILz0Iw6x6el7II3phUG9idSi38xe3QLy0ZRAPMY7iKAgEDncFTZXzbYQed-JdwuL991B0ym5-AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
محافظة السماوة جنوبي العراق تخرج عن بكرة أبيها في عزاء الإمام العباس (عليه السلام) باليوم السابع من شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79740" target="_blank">📅 19:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a83af36368.mp4?token=vOOhzHgqF58BchVjcswCHpHnkSjF2jiemhsVzJjMbHr3iD19KhxjDQd7iZVSqTylV6QGf40PRhV6Olb5qUTazIdTHzi51z6M9Lc1fxu0mJYxmabnXYUcaFdlvOhra7oA04paP3SdyPWf3cozQfajtRTCjnNFhprfroRLJx6Lw2XrUAJhyDjQmKoRU342kwuIglZ3ygDm95yuAatWQMeskcnX0ZCaWo5TjlQFtYKbmEzAKX2RZZiwwCu4JR-5R3Ohb8Tv4DGIvowi7hVrH5RFudFefuMk9Ka-3jU8JNrWqhBY1-BoWxs0CIjAnwIxw22nDf3uo9nCoUQUdfKkFa4z2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a83af36368.mp4?token=vOOhzHgqF58BchVjcswCHpHnkSjF2jiemhsVzJjMbHr3iD19KhxjDQd7iZVSqTylV6QGf40PRhV6Olb5qUTazIdTHzi51z6M9Lc1fxu0mJYxmabnXYUcaFdlvOhra7oA04paP3SdyPWf3cozQfajtRTCjnNFhprfroRLJx6Lw2XrUAJhyDjQmKoRU342kwuIglZ3ygDm95yuAatWQMeskcnX0ZCaWo5TjlQFtYKbmEzAKX2RZZiwwCu4JR-5R3Ohb8Tv4DGIvowi7hVrH5RFudFefuMk9Ka-3jU8JNrWqhBY1-BoWxs0CIjAnwIxw22nDf3uo9nCoUQUdfKkFa4z2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
طيران حربي أمريكي يحلق بكثافة وإرتفاع منخفض في سماء محافظة ديرالزور السورية بالقرب من الحدود العراقية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79739" target="_blank">📅 18:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFe_TQBioNl7ovoS5DrQnj8XaPrhFLVsQZsCNXFBEvzzDiCYsHh7B8VoDif4vn0gguehmD6f9fr2DOzbvPk8y4NIh2GcANEr2Yv_cTz9oKvJd2fzUQRVxXIUXafdyeeeUBok7tSl3sUiGDVGGjJHoCzG441aY0JSjayN_5tiTIki9LGSDk3MNX4mKcUKmooeRSeVjOAXsJMofd9m6Y8H_kpJ3CwBcCvoMJFe41ENl1zpiLgsYB0DNiV_S9sIv-fN_uihMcHopu6E74v3qWfyN0ces1vIh4i_uzOGSkGNuv1VTJhNVyhA-fPMmv2vSX7GvgTKkecDZzWVZ2D3mPEZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
أُلقي القبض على ستة أشخاص، ووُجّهت اتهامات لسبعة آخرين، بسبب الأضرار التي ألحقوها ببركة المياه العاكسة الجميلة في بلادنا. الشقّ الذي يبلغ طوله 350 قدمًا، والذي أحدثه سكين حاد جدًا أو شفرات حلاقة، هو في الواقع عبارة عن جروح عديدة على امتداد 350 قدمًا. لقد كان عملًا متعمدًا وإجراميًا، ولا بدّ أن يكون أحدهم قد بذل جهدًا كبيرًا، ربما في جنح الظلام، لإحداث هذه الحالة. كذلك، قُطعت المنطقة الصغيرة في قاع البركة ورُفعت بقوة عن السطح، تاركةً حوافًا خشنة وغير مستوية. ويجري استبدال المساحات الكبيرة من العشب. على أي حال، حتى قبل إصلاح تلك المناطق، فإن بركة المياه العاكسة في أبهى صورها. سنقوم بتفريغ بعض المياه، إما قبل أو بعد الرابع من يوليو مباشرةً، لإجراء الإصلاح الدائم.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79738" target="_blank">📅 18:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5GqvHDOgMvIX2mciPeaS0F5FQsHbOzPHEHkpYxpPWK5u1U1NpTLINuOD0TOchQ8SID7F-7CmYUoq0rqOgXrZ2Kh2YHdhmFKjyDNzU4lD_9QAMHldVCJDISDMzReKOvg29rdEw5gMGHgFLCfMJrGwehzhuxoRyhqjAPNwfkSyJf9A7OAH8aQgXgirABligv52DZgY8lavxb5XxWAjcJeAjxqeRviQf32iMowxTFAg49BVj7ghqME6fqC-CHwdagFpbCsweJf2sDFD9hAUIF5e41ucSaxD6lPdgtzYQHZ4FoUc-uY5vCO43270twE8GG-3TxinWUxXm8CRYQIts13OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
طائرة أمريكية تطلق إنذار الإستغاثة (7700) فوق الأراضي الفلسطينية المحتلة بعد عودتها من أجواء غرب العراق.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79737" target="_blank">📅 18:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇷🇺
‏
بوتين:
روسيا مستعدة لمحادثات السلام مع أوكرانيا على أساس مؤتمر إسطنبول 2022.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79736" target="_blank">📅 18:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8GkHQeaHk9EN-1uG0_p-jMw5bS8E86AyvdqH_0g3MamURN5LOIgUYpJWKVzMryHILFz7NZcZtWexF_TFgiTM80gldJhLMjHSTeRp7Y6lKaYNwSBf5QE9D_JnHUzJYabRgsj2C8gWdbzw00bYYm8ziyvq0H9Aj0I9koyU5xYCLen2s7guTcL7n9WpKEzTChqdbRQoUzrpETI5szRHCKJdi-wv7PU7ptQToqSzBbLATJox0XZ3Ra1QkFH1JOUNH1AE2zgKxyGIhoDz8so_stYb6ujqc1jyfWR1AxIp-2teLtZF9zJe6Fo3hlaATUg4-mb9DwdxYJL8W5MzOB_fxcQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نجل الشهيد تنكسيري قائد البحرية في الحرس الثوري، ينشر صورة لقبضة والده المشدودة بعد إستشهاده؛ مع عبارة "
قسماً بهذه القبضة المشدودة، لن تسقط الراية على الأرض
".</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79735" target="_blank">📅 17:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79734">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">في الذكرى السنوية الأولى لاستشهاد القائد الشجاع السيد حيدر الموسوي (رضوان الله عليه)، أحيت المقاومة الإسلامية كتائب سيد الشهداء هذه المناسبة الوفائية، استذكارًا لمسيرته الجهادية الحافلة بالعطاء والتضحية، واستحضارًا لمواقفه البطولية التي سطّرها في ميادين الدفاع والجهاد.
وقد شهدت مراسم الإحياء حضورًا شعبيًا كبيرًا، تجديدًا للعهد مع الشهداء الأبرار، وتأكيدًا على أن دماءهم الزكية ستبقى نبراسًا للأحرار ومنارةً للأجيال في طريق العزة والكرامة.
المجد والخلود لشهدائنا الأبرار، والرحمة والرضوان للقائد الشهيد السيد حيدر الموسوي، ولجميع شهداء طريق الحق.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79734" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE3fYA5AsW0yZBjcDmV41xAUyWVMOBpjqnfbyEQIZkjThRZbV_GGxYFrLSN1KWiexta-xOgaMpLuR_SrdrmoOD_W7Zro6oW0-KWQ-EY14De9jlWj0OFn7GIe-p5duI1UKInCAG3WR3wKSucDW9HKh7VB3bm6wMJCElK2mvO5UvpiY6IIBiHuDiiHHJxXUuIDM_Kcyl3gYX1Qu2yQqe-rDIDsVEsl7jzYdNoyCM-tivsoMfw37__w6WK60Ro0oMSTANIqhbkHN-Au-NsGGphXhoDK9Nm3NhPIulHue1r4U982If5QuZmV25xwgJQmmnD6uk-RhnjosmA5z0_bHB_HZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا: هبوط طائرتان من طراز AH-64 مروحية في مطار واشنطن داخل قاعدة التوحيد الثالثة في العاصمة العراقية بغداد ولأول مرة قوات الـ FBI الأمريكية تنتشر على جسر المقابل قيادة العمليات المشتركة لتأمين القوة التي هبطت قبل قليل.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79733" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
ناقلة تحمل اسم (Kiara M) ترسو في ميناء البصرة النفطي العراقي لتحميل 2 مليون برميل بعد عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79731" target="_blank">📅 16:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مصدر لنايا:
هبوط طائرتان من طراز AH-64 مروحية في مطار واشنطن داخل قاعدة التوحيد الثالثة في العاصمة العراقية بغداد ولأول مرة قوات الـ FBI الأمريكية تنتشر على جسر المقابل قيادة العمليات المشتركة لتأمين القوة التي هبطت قبل قليل.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79730" target="_blank">📅 16:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌟
🇸🇾
محادثة بين عنصر من عصابات الجولاني وعنصر في قوات حرس الحدود العراقية.
ابو زهراء يروح يمين يخاف لا يفجر نفسه ويلحكه، يروح يسار ويلحكه، كافي يا اخي اعتقني
😄</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79729" target="_blank">📅 16:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioAD6-WoaXKg8Lo11dcA3ELYWL-PunItuzFqq91OKd6EABgxvv2fesYxP9m36UwyrFbeHlKDf519KmZhFcK0eskd6MnswEIEioJDazYJ7Pik_prmjQOH4uWT9kAOuea0HxceTLmH924g4959VFm6EDiJs8VGCjzRourbaInVEHC0hf_23rh_gqeFahGYGYWOUI52VmNAJ_UpXlYE7KN8EnRbKBXIrrlCAdhI9a1KK2ufGIHKbAtyZ61Jcn9cWRkrqA7FT4jdiQgz4Tb3cf-AbiNgWqAgflIShhXDsya4NpJuGumc-F27MmxQrGtivBRQKfiUeCRGOi5s2lvg0J2hFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
القضاء العراقي:
اعترافات وكيل وزير النفط لشؤون التصفية تطيح بمحافظ صلاح الدين الأسبق وارتفاع حصيلة الأموال المضبوطة في القضية إلى (98) مليار دينار و(11) مليون دولار</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79728" target="_blank">📅 16:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp_ex4fTWEhlfiTXlQ99Z8s3jXLTgVL7-XSY2-S3slOY9BzNxP1Aaoh3slqXvgHgz8M1wkNGnnNfqza7CUkYomMLtM0-ZQPrDJzzAR2-zhYHz3HR_jDbU8qu6_msgBA5E4PM-DrokWM00CyDukiqYYnCtr3NuUlJI1KcJnK__NOsDWu1VVA5pNhtEfjCe8KAwxVdz9u5FMEYGgSeyGsZMTqW5V5JvpwzwSY5pox79yE8s8PPCioSh1aYx6EV3uCa53HBdnoZQV8oQEY-0CoMemhp1taIsZL1r65ypZpLaGVS4dA7orGHJApXbyeObGLiD0hdEug53bZw9L0qd-tpQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
إلى أمة المقاومة أمة الشجعان والشرفاء، وإلى أبناء العراق كافة
ندعوكم للمشاركة في تشييع الشهيد علي (محمد عبد الرحمن) ابن لبنان الأبي، لبنان التضحية والصمود الذي ستتشرف أرض العراق باستقباله واحتضان مراسم تشييعه اليوم الثلاثاء في محافظتي النجف الاشرف وكربلاء المقدسة
النجف الأشرف - شارع الطوسي
الساعة العاشرة مساءً
كربلاء المقدسة - باب قبلة أبي الفضل العباس (ع)
الساعة الواحدة ليلاً</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79727" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 17-06-2026 تموضع قوة تابعة لجيش العدو الإسرائيلي في أطراف بلدة كفرتبنيت جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79726" target="_blank">📅 16:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R71EBdv5TPjbVY_xwSwpOEMC7UmSQJKXvV1mg8Rk0wgAggcUaVWRhvI8Kv6O8H9d-_JK9M1J6Gfho612KJ5Q1aB3oFjGbscnX4m4yVpbfGmMsS7I42UP_9MIaunzud_oKiBRyhvXRbNeteYFdeYC7DlZU-Pq359MrQ6pfYSMP6Q_pLOchVvnSr7Gp2f2reBNNb5Jv_wY49tsMgLvRmw5yv0u8fVm0Rs62GMcfTAzdsvQrGGoH1_T797FZmdT_vyBQUIKPxNpzbyx2CH5u10PB-RlVopM0qJhj05_GFxqgdV3XTeg3rhVOnjna-RLK1CCyLwIsFDxkTX7k3ID_Cq85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لجنة المحتوى الهابط تتخذ إجراءات قانونية بحق زينة العبيدي لنشر محتوى مسيء للآداب العامة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79725" target="_blank">📅 15:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDw6MEZMw3tBMwkICziR9AApDi_FyXwWpNEF5HFixo57ZFhuDgeuqOJ0tP5Z9QMlt-HU-dJZX7hQhBu7LfGcXrgj6hY_zK3o_9rGvP1UB1aMwPMDonPu0l16UsSJo8xqOFtdIUYBrT0DK5mkwNdgXs1EMr06yr2jV8F8_LNx4ZOng9fIWgXeeXXWTX0JGhnzAYOWjOilmP50m2Zf-LN4yQ6Ll693IM4aqeiKnU0Qf_VdUAL59zzft_BOKr2luoQGvXSdKynEHI_cC1_Uzas8-wtLOAQcoZ7f3Q5BuNX0uD0K9wICxV3YEj8VUIKgTg4kljU8dgqUgnaY_mLhT6eKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
تدفقت 19 مليون برميل من النفط من مضيق هرمز أمس، وهو رقم قياسي غير مسبوق. أسعار النفط تتراجع، والعالم مكان أكثر أمانًا بكثير!!!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79723" target="_blank">📅 14:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79722">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuZ47fo0jFEZgB2bsNzLT6t9ojJy35OYdbfDrbXxb-Wtpp2iyRRmGDum23Q1k_LEcDKNQkuKFrwcJGgYZMGxXJPPem8xzttMVHr12etQQ0UGZp8wL-qFpo3ga-DQ4Ask4leCwJ6tcYdyGOhgVJnBJciQOQMzIzjjCRCGYji-ok-hvyhNedtnlEejcyNcsGX1mXFJwyLUjgt1_emhy60pMSa4J8U9ItNCoLvXbzj4FwptPnfWmyFYwIOOmDj_MRXohvWp4UUTPCA8gjJDN3VVq3N1O5RChoDxQbxBMv8le3c8CQxW-J2-8TA3J0eZkHTfj7b3J3SXDDJnT1lcLz7WMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
على الرغم من احتجاجاتهم وتصريحاتهم الكاذبة المخالفة، بالإضافة إلى حملة التضليل الإعلامي التي تبذل قصارى جهدها لتهميش انتصار الولايات المتحدة، فقد وافقت إيران بشكل كامل ونهائي على أعلى مستويات التفتيش النووي لفترة طويلة (إلى ما لا نهاية!). هذا سيضمن "الشفافية النووية". لو لم يوافقوا على ذلك، لما كانت هناك مفاوضات أخرى! بناءً على هذا، وعلى تنازلات أخرى كبيرة قدمتها إيران، وافقتُ على إبقاء مضيق هرمز مفتوحًا، دون فرض حصار بحري إضافي. مع ذلك، ستبقى جميع السفن في مواقعها تحسبًا لإعادة فرض الحصار، وهو أمر يبدو مستبعدًا للغاية في هذه المرحلة. الأموال و/أو العقوبات التي تُفرج عنها وزارة الخزانة الأمريكية تُودع في حساب ضمان تحت سيطرة الولايات المتحدة، وستُستخدم لشراء المواد الغذائية والإمدادات الطبية، حصريًا من الولايات المتحدة، بما في ذلك الذرة والقمح وفول الصويا من مزارعينا الأمريكيين العظماء. هذه مواد تحتاجها إيران بشدة." هذه أزمة إنسانية، وأشعر بضرورة تقديم المساعدة الآن، قبل فوات الأوان. المحادثات تسير على ما يرام! شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79722" target="_blank">📅 14:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79720">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0_dLzNfo9MewEj2XRgLcZUzZgTB8Qyisw2ITvZy0XG9lPvzPQFSG9lndBdLLmG6e_urXoD05d-crWGC--6dxCE_-9atAm4U6rZzavRDVcqdwzLYYJq06rex2A9a8i2QUXlEoYKfoDTXuLexmBKJWlyzmLzqH4q8jONJgIoaLKnH5fppxx1hqMscoAtZamyJNZqW4GCYQfEM5GV5QjE--1Vyq_lw55QtlZ6t2RzfzF1y7FtMLgNZ4sIdPowGUm_F-x2srnFk0B-JxydG6bXVAIQalEeskKDgMA-EDWWLjfGqTFtGXAaIQXyffMyxzLRUlfHZaXdgBxdp-qEYzLvI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtvpyarfGmhQTOoixCKxvVjgxQxt8AwtNXyI1hIwpNO_212pgmvHPYawfc-lMYhPY-nzeu-rrvx-9vr9mp8h3dCj_H7uxvMiGwFAWE-1mgrYA74h_r2hSlOS-IF_nGJYnOkfseVDWoFIFnOeZrNpYJ395L0Mi0cPiHSTkEpU_Ne4S9kVAlBPJ-Wo65M1VeG1VxtS4JGMDtVOPW3VM8rkC5fD3whd-MJLhyQSegRtfHB9jsyZ99L2a2eNF_2pjS0t4e4bsZX5AENyG-a6bF_kjnYwaKNM4lFWPAjNlrACGuHduvNChI7pu0t2ij3qc6o80HmBszVBFnurNR6SCcvJuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفينة تجارية سورية تتعرض لقصف في ميناء أوديسا الأوكراني ما أدى الى مقتل كامل طاقمها</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79720" target="_blank">📅 14:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79719">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
🌟
بيان مشترك ببن الجمهورية الاسلامية الايرانية وسلطنة عمان حول مضيق هرمز:
- أكدت سلطنة عُمان وجمهورية إيران الإسلامية بوصفهما الدولتين الساحليتين المطلتين على مضيق هرمز التزامهما بضمان المرور الآمن عبر المضيق وفقًا لأحكام القانون الدولي ذات الصلة، مع التأكيد على سيادتهما وحقوقهما السيادية على مياههما الإقليمية في مضيق هرمز.
- اتفق الجانبان على مواصلة الحوار حول هذه المسألة من خلال فريق عمل مشترك بين وزارتي خارجية البلدين، بهدف التوصل إلى اتفاق بشأن إدارة الملاحة في مضيق هرمز مستقبلًا، والخدمات المقدمة في هذا الشأن، والتكاليف المرتبطة بها، وفقًا للمعايير الدولية.
- اتفق الجانبان أيضًا على إجراء مباحثات مع الدول الساحلية في المنطقة ومع أي جهات أخرى ذات صلة.
- اكد الجانبان على ضرورة أن تحترم جميع الترتيبات المتعلقة بمضيق هرمز سيادة الدولتين المطلتين على المضيق وحقوقهما السيادية احترامًا كاملًا.
- جددت سلطنة عمان والجمهورية الإسلامية الإيرانية التزامهما بالحفاظ على مضيق هرمز كممر مائي آمن ومفتوح للملاحة الدولية، وأكدتا أهمية استمرار التعاون لتعزيز السلامة البحرية وحرية الملاحة والاستقرار الإقليمي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79719" target="_blank">📅 14:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79718">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlgPJb-DmeqrvJE0ffAoDzBjBONgkRvU3O7qbv7qXTVox7UGvIMAuGwGOurlVcUVD8Oo0KZlhilSKCmrdLjvZmjhpfvx2kLuTTuG-ebRGtqfiApC4LbOVMUcrfDYl3Vcvvkxa_g6_okrgHdHdVH9LYG4nZnQ0fNlhdux5BwY8Pm_xOVU8TbhmvB42WB78sqk7DLKdSMkeWMF4-1G8vEZt3u_FDy8A0HDuERIDdAIBZ_6qNrvoTw8qi-7N0VJjBeyFqYL1tW6DhopxzUjouNtLsMA4rwx_iX30WPrb-T1hjudKLEXCAzKifj9aU9UGjby2eia4ZJhnhl3lcqDRAyTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواطنون يناشدون أهل الرحم بضرورة حصر السلاح المنفلت داخل المكاتب الحكومية
نعم نعم للإصلاح</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79718" target="_blank">📅 14:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79717">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">محافظة النجف الأشرف تقرر تعطيل الدوام الرسمي يوم غد الاربعاء باستقناء الدوائر الامنية والخدمية والامتحانات الوزارية للصف السادس العلمي والأدبي والمهني.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79717" target="_blank">📅 14:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79716">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtFG7r6OoWdCWbyQUKBcWW3pgHvO7-BNqBCB6A6h6oLF4uCDTDTpB9lOZsBbJbtAQR1xPV2hYYsxKWYOEyFO7-pu6Ob2Gc7lzqYGtBpzkLLrFE8pmC2n1iA4k34aO-JzTVkjKO4IIQRWORxoRFZS73hGQxsel2b6riHpEszBRczo_hg7WD4S2LoSJx3t7bXK_ReKg-roM7GVPiplpDi4c3lSx_NvmQLyxK2pEdRiI1D6iLdmhmPbkjXLlCpcFFo1hyiWZM1_wIxfyHXPHp2wct-qQm7VrdaLlUv5Qb1zZAitJXJGUQn3_1XrnY-ok7ktiCX375NBd4QRIgcEg9BjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الاتصالات العراقي مصطفى سند يعلن اعادة القضاء العراقي 85 مليار دينار كانت مختلسة الى حساب وزارة الاتصالات.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79716" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79715">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh8LRPkvEpmi1mQVh7YK2pILCNmm6T8rNKXNaqXFwwZUlx4jJx1KdYVVVTNeRMHen6Urul5MvtRzZqnsmlQhbLXVkSGguCaJ3qdHfc-ned6MWaVGVlZ8pZP-uf4Rc6b2qN4DYTCjhzJ26SLe6onGpt7l0TtrM_gEmlolqjGBHUT6ql9Ho4DVwQO31ltv9UU0z5MBDiEo_vO7BYzIodtOoOPPmPQ3k-w2-oiwFs1Nb6BfnRUUDsUdVoTj6JdpAeMKNrHg7RbB4LLr2801j1IMmCZa2wnAjtWE2GcDTl4irgcBQ02jIDKJVrGKn0-cMvJGzfJl6GOIwPxaVGmv0wZvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
‏وصول الرئيس الإيراني إلى باكستان</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79715" target="_blank">📅 13:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79714">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
مجلس القضاء الأعلى العراقي:
ما تم نشره في موقع (قناة الدولة الفضائية) التي تزعم رصد مجلس القضاء الأعلى (65 زيارة) للمتهم الموقوف وكيل وزير النفط لشؤون التصفية (عدنان الجميلي) من قبل مسؤولين ووزراء ونواب وقادة فصائل ومديرين عامين ورجال أعمال هي معلومات غير صحيحة لا علاقة للقضاء بها</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79714" target="_blank">📅 13:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79713">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
وزارة العدل العراقية:
رد دعوى قضائية بقرار صادر من المحكمة الاتحادية العليا الأمريكية وتجنب العراق دفع 53 مليون دولار ضد شركات أردنية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79713" target="_blank">📅 13:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
وزارة التربية العراقية:
اعلان نتائج الثالث المتوسط الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79712" target="_blank">📅 13:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79708">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هيئة النزاهة العراقية: الحبس الشديد خمس سنوات بحق يزن مشعان الجبوري لاقترافه جريمة النصب والاحتيال، المدان أوهم مُشتكياً بقدرته على ترتيب لقاء مع رئيس الوزراء واستولى على (41) مليار دينار</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79708" target="_blank">📅 13:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79707">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
مصادر إعلامية:
وزير الخارجية الإيراني عباس عراقجي يزور بغداد يوم الأحد المقبل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79707" target="_blank">📅 12:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79706">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
منصة كبلر للملاحة البحرية: 36 سفينة عبرت مضيق هرمز أمس في أعلى معدل حركة يشهدها المضيق منذ أول مارس</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79706" target="_blank">📅 12:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌟
الرقابة النووية: العراق مؤهل لإنشاء محطات نووية لإنتاج الطاقة الكهربائية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79705" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc16091f2.mp4?token=NnLHQo2R5Ps9x2dzKfKaqy3IU2buYJxkLnhkCQc-W_NE_TqINRh8-5BOaJU14aqrOvk2GJrRaK2ct0xwm0p_X7dWio4l3lc2wiXFKGEhrHF3Wfun8ZEhcwQ0zDE70baOf5gqAzFiPIbA9s4IvW3NHbOh-VrO7vb-SiloyDXgZx75M8jUHeBWu4qaHQ9tWCaZBgG23SxXHAvRyGQyVjYEv9nsY_B37BzrYTuzocu66SMqG_MfbymP05zJh-tk6u-l_ZFTGMropDRX4dvcLZXrrcN1rzutLAwmot4HjfO07TzJq19TorVASGxqxjjIfn4W9uETtzR5vdHc4xMyJYMPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc16091f2.mp4?token=NnLHQo2R5Ps9x2dzKfKaqy3IU2buYJxkLnhkCQc-W_NE_TqINRh8-5BOaJU14aqrOvk2GJrRaK2ct0xwm0p_X7dWio4l3lc2wiXFKGEhrHF3Wfun8ZEhcwQ0zDE70baOf5gqAzFiPIbA9s4IvW3NHbOh-VrO7vb-SiloyDXgZx75M8jUHeBWu4qaHQ9tWCaZBgG23SxXHAvRyGQyVjYEv9nsY_B37BzrYTuzocu66SMqG_MfbymP05zJh-tk6u-l_ZFTGMropDRX4dvcLZXrrcN1rzutLAwmot4HjfO07TzJq19TorVASGxqxjjIfn4W9uETtzR5vdHc4xMyJYMPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بن غفير حول قتال سوريا ضد حزب الله: لا سمح الله. هذا شر يحل محل شر آخر ؛ جلب داعـSh بالقرب من حدودنا - وهو داعـSh حقيقي اغتصب الناس وقتلهم وذبحهم - هو تهور تام.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79704" target="_blank">📅 11:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79703">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaWVImawg0pyzKykU3MrCJmLzf4gIGIUP0wi_39Tl6_DY46Mx18gynyDhJ_RZ3QwDIPPQicMZh23NdSnBZaDnC8Yeof1iiuwB4fz1m9sXkgogENqrtU7Tvz6TM-JBuDAUcWc8BnkbJd0CubJUVb2Ldch0VfJIjO8eGu-n7rGwVbWdMqDxmv3oZum1dyaO13WzNhlc3yuA3r0BOmfGEySTxPcpyW4WwYe3171Inys4OiR8h_FbU2lLJlLC17iyQ5EyCV7RbE7-ihRFvuQ28pA2Egyy00CDXnPQIacfjQ0D8L7lGJvxnPP79vOGiisAuvMYdYIPapZVxDRt18kYqAGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الموقع الرسمي لنادي ريال مدريد يثخن ويتشمت بالعراق بعد تسديد مهاجمه ممبابي على العراق وفوز فريقه الفرنسي ليلة البارحة على منتخبنا الوطني …</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79703" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79702">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
لم نجر أي لقاء مع مدير الوكالة الذرية في سويسرا ولا خطط لتفتيش منشآتنا النووية التي قصفت ولا ننوي السماح لمفتشي الوكالة الدولية الذرية بزيارة المواقع النووية
الأموال الإيرانية المحررة نحن من سنتخذ القرار حول صرفها ولا قيود في هذا الإطار
إيران تحاول المضي قدماً لتحقيق أهدافها
الالتزام بوقف الحرب في لبنان جزء من مذكرة التفاهم والولايات المتحدة تعهدت بذلك
سوف يتم التفاهم على مزيد من التفاصيل في الأيام المقبلة</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79702" target="_blank">📅 11:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79701">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏴‍☠️
إذاعة الجيش الإسرائيلي: عدم انسحابنا من لبنان يشمل منطقة الشقيف حتى تفكيك حزب الله بالكامل
يعني عنجد رح تفككوه
😄</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79701" target="_blank">📅 10:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79700">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42f7ae6a5.mp4?token=LbOlVS4yPkV7eGHILizF759Nn9lFLspDX_JzZFpzbHE2mIgQ_kIQYyiNOLj30DZqeaKWUsQ7SRyv7umX_pAKNqHwpdEyYj_pTExgNaJq__wMw3gpjpQY7ehTIyJOPXAMFsiLmKUcJK5OVhgnDZzhntJhMS8AK3dbMvjR3jRE0KoAVEC2IZhWr_sxn9O4WDoa3Xa7bVRQmINZhk9RJYUPVa_YPgitmOAVBjBOPVM5tL-ewSt1kXzLev-ybuGgPHT5-gR3nwXdk_NxR4dnuT5aC3jfiHic9LzvNkjzxijql9fIZUEEr1c1EaF-KHNDc0j2YQX8nV0Cl46vbAibl8qdRQxx24E3afMrh3eL5yPYmgUYVmzejtVFFxXN57vFFU3SFH5adBlSF1cZff9zaBwH2PnVBAS3u6v3hBrB-oPMEmLhkMXYvhfNbW1cE3VAZcRXJGLvRHdUi7o-PGUOJ7mZd2z5ytPAoJguuX-jEOuzRikIxti_MFDukMAOu9MhWmdAmtLDkz6RJzSb-VlKxRNXynQ2op0uP8ftx-wDr6YZVgCr7VC6SZS3alNGTT69HsZ92Qesf_j_I7ZTHX_74p1JaZVwnTzVxes1vTiqWoV0gIGQGM1_5kT2fZgMZ9QcEs6CdYpfuakS0tr8PURXGyqkXlKLNzLAfkENIenDD634Ouc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42f7ae6a5.mp4?token=LbOlVS4yPkV7eGHILizF759Nn9lFLspDX_JzZFpzbHE2mIgQ_kIQYyiNOLj30DZqeaKWUsQ7SRyv7umX_pAKNqHwpdEyYj_pTExgNaJq__wMw3gpjpQY7ehTIyJOPXAMFsiLmKUcJK5OVhgnDZzhntJhMS8AK3dbMvjR3jRE0KoAVEC2IZhWr_sxn9O4WDoa3Xa7bVRQmINZhk9RJYUPVa_YPgitmOAVBjBOPVM5tL-ewSt1kXzLev-ybuGgPHT5-gR3nwXdk_NxR4dnuT5aC3jfiHic9LzvNkjzxijql9fIZUEEr1c1EaF-KHNDc0j2YQX8nV0Cl46vbAibl8qdRQxx24E3afMrh3eL5yPYmgUYVmzejtVFFxXN57vFFU3SFH5adBlSF1cZff9zaBwH2PnVBAS3u6v3hBrB-oPMEmLhkMXYvhfNbW1cE3VAZcRXJGLvRHdUi7o-PGUOJ7mZd2z5ytPAoJguuX-jEOuzRikIxti_MFDukMAOu9MhWmdAmtLDkz6RJzSb-VlKxRNXynQ2op0uP8ftx-wDr6YZVgCr7VC6SZS3alNGTT69HsZ92Qesf_j_I7ZTHX_74p1JaZVwnTzVxes1vTiqWoV0gIGQGM1_5kT2fZgMZ9QcEs6CdYpfuakS0tr8PURXGyqkXlKLNzLAfkENIenDD634Ouc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇶
محافظة الناصرية تحيي ذكرى استشهاد أبي الفضل العباس عليه السلام.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79700" target="_blank">📅 09:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هدف ثالث للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/79697" target="_blank">📅 04:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هدف ثاني للمنتخب فرنسي</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/79696" target="_blank">📅 03:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هدف أول للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/79695" target="_blank">📅 03:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
🇫🇷
المباراة تستأنف الساعة 03:00 فجراً بتوقيت بغداد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/79694" target="_blank">📅 03:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
الشوط الثاني لمباراة منتخبنا الوطني ونظيره الفرنسي سيتم استئنافه عند الساعة 2:50.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/79693" target="_blank">📅 03:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03589363ac.mp4?token=HuCmjP93SKHrmX0szJp6h_7f1kmG_9Ee6juCeptQZPqgSbgf3RyxzTdj5tW7ka5_-LiY7Le57KlgTvlH20-6w2ZbDZZGYsAgFTj46EeZlPJAwVcn5O4qt4cnjr-0eeRP6w2TuLmlvfm45c9O6tZ1zGSrO7bxvWVZ2Qgatt2Gc9UIoWggmV-C7aWHgQyxPvxrfpwNAs1KFczUyzQ6GgHdeEAh8VEyomeYPFAgHkmzbJKaJLJYNGA3Xvps3VgmYfy9Qk59QpOj3P8JJehQPC_HMV0dRq0n19Y5NblAW0DFDbZC2M6p0Hqku_LNWfno971BWjWTspv9mXCPYy3F1_MDcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03589363ac.mp4?token=HuCmjP93SKHrmX0szJp6h_7f1kmG_9Ee6juCeptQZPqgSbgf3RyxzTdj5tW7ka5_-LiY7Le57KlgTvlH20-6w2ZbDZZGYsAgFTj46EeZlPJAwVcn5O4qt4cnjr-0eeRP6w2TuLmlvfm45c9O6tZ1zGSrO7bxvWVZ2Qgatt2Gc9UIoWggmV-C7aWHgQyxPvxrfpwNAs1KFczUyzQ6GgHdeEAh8VEyomeYPFAgHkmzbJKaJLJYNGA3Xvps3VgmYfy9Qk59QpOj3P8JJehQPC_HMV0dRq0n19Y5NblAW0DFDbZC2M6p0Hqku_LNWfno971BWjWTspv9mXCPYy3F1_MDcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇫🇷
تحضيرات لدخول لاعبي المنتخبين إلى أرضية الملعب من أجل إجراء عمليات الإحماء قبل انطلاق المباراة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/79692" target="_blank">📅 03:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9f786227.mp4?token=Iv5p24MV-Hpa8abdxuotc1VFeZkZ1TzdJMlYlRnao1D1ED4sSIwWL2UAbVsTlBH3CFTeyYKL0hgpS_Gi9dVmWSXjAzPvKgknuhyH03do-l_15QlfbyW8y1ENhhhK8R9rEERd4sl5gG39hCfFVI7BBD6cxZ_cV4rFnpQTLaN6ccJ7gDs6swLjPvmNoRyP9eo1qxCPJyDwCXa0vr9RMAcrK0sa2tUYJo1a2Qf39gYFGeNyk19Xkk_EKfPX7TY2iO5CfXOddzZkHME5MbFSZBFeXIavcdJ-WRwVR_4k0COl4QulN30o65JmOK-eYkwXtoLqzXRiCiFhUi3q3XpEhIFlqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9f786227.mp4?token=Iv5p24MV-Hpa8abdxuotc1VFeZkZ1TzdJMlYlRnao1D1ED4sSIwWL2UAbVsTlBH3CFTeyYKL0hgpS_Gi9dVmWSXjAzPvKgknuhyH03do-l_15QlfbyW8y1ENhhhK8R9rEERd4sl5gG39hCfFVI7BBD6cxZ_cV4rFnpQTLaN6ccJ7gDs6swLjPvmNoRyP9eo1qxCPJyDwCXa0vr9RMAcrK0sa2tUYJo1a2Qf39gYFGeNyk19Xkk_EKfPX7TY2iO5CfXOddzZkHME5MbFSZBFeXIavcdJ-WRwVR_4k0COl4QulN30o65JmOK-eYkwXtoLqzXRiCiFhUi3q3XpEhIFlqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الشوط الثاني لمباراة منتخبنا الوطني ونظيره الفرنسي سيتم استئنافه عند الساعة 2:50.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79691" target="_blank">📅 02:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592498269d.mp4?token=DcNYEF49XGo6Ez_R2JetnhtlHIr_lfwi-ZG2Jl0twJZAh40J-wIlI1F7meXZcKHAG4KkPDgyxn27QLYBKLbdkK8trZyrZyfcG8g5quvrhDO1AXDdUj9_CqSHR-nesZsZraxsJlszEjKDC5nSCEmsdDnZ3bYol10GCa6XOUM0cpiuLpki8UWnA032eV-3Q2Nd5EDjUSXgPY5PUvAWmLab8O1mpdshJoPWfQ4UNvOaaph4dDeYGJMIV_tHpjZWelcds4mTkct1fsSbRR6PDbUmqqAYFGci3CYSjmwJRCRweqNnK8vwCeqJ3lY9r5r2sCSZwAtFXW3Xd73vaatZ-7OlVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592498269d.mp4?token=DcNYEF49XGo6Ez_R2JetnhtlHIr_lfwi-ZG2Jl0twJZAh40J-wIlI1F7meXZcKHAG4KkPDgyxn27QLYBKLbdkK8trZyrZyfcG8g5quvrhDO1AXDdUj9_CqSHR-nesZsZraxsJlszEjKDC5nSCEmsdDnZ3bYol10GCa6XOUM0cpiuLpki8UWnA032eV-3Q2Nd5EDjUSXgPY5PUvAWmLab8O1mpdshJoPWfQ4UNvOaaph4dDeYGJMIV_tHpjZWelcds4mTkct1fsSbRR6PDbUmqqAYFGci3CYSjmwJRCRweqNnK8vwCeqJ3lY9r5r2sCSZwAtFXW3Xd73vaatZ-7OlVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الشوط الثاني لمباراة منتخبنا الوطني ونظيره الفرنسي سيتم استئنافه عند الساعة 2:50.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79690" target="_blank">📅 02:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
🇫🇷
تمديد جديد موعد انطلاق الشوط الثاني تأجل إلى 2:20 صباحا بتوقيت بغداد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79689" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNS-5OynZ_LEi0Nl6o-W2Ky46S-xa3NfrEU_q1tLGbaCihSSfWK0RSokKLo9ru2Js9_G0QRZ_uG9XnhfjK4IN2stn1fPBIFFFvV6kQ0Y82Hk6ijEMi6VzAw5nxycBQO2Oqx5PK-CyBaZBND6korWLFbnF_tVI57P-7d-FkcOCB2d0-aMHf_4eNs_Eum7kHFeRA5GqmULcr54ke2dvSmyTdaBRQy8GqF2bOIycDQzZbnvtW-QV88jOPuz5-ajJ9nLWSUwI098HTr5fmcYnhOYT1jCsBmv_XRpLWuCDwPP0p3oWlnxJAJaACyUqxturqaZl226C_mOfFR06YNH999Ozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
🌟
أبد والله لن ننسى حسينا،
راية الإمام الحسين (ع) حاضرة في مباراة منتخبنا الوطني.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79688" target="_blank">📅 02:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ستستأنف مباراة فرنسا والعراق ساعة 2:00</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79687" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79685">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqtaJH8n7xzPMq277jexy5fCvh5M0cIXx9kUF4pJz3PqHvJ4lEb1-tVXsPL6U1JJevC4Cghl0vBOHi50srBWKwoqWRnBld6ga4OIYLx9AAgpZB99xDiOQY6v4leKN5uvIqSsYlYKMo6rHShouKyof9HzW2KYVkN-C7OieXbVPMcspknn6c943hEDPGdP3Kq8etegj4MXYbIpZ0Lzt7i07LJitNnxiILvrZs7xZIvQRB6uiaRLXhmvh72Q6ALwIuDaFNyYdHEQBvyuSho6euEbv0Jf7y9iYJFn8Wst58X19-OAsUlpgtf75czPYVa9zFRRJMv-8ZyPhdjC4yOYhOEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
انطلاق مباراة منتخبنا الوطني أمام نظيره الفرنسي.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79685" target="_blank">📅 02:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7459db2f.mp4?token=sgkRGyyWppViaL0J8rMjghvkVfoVXDiekvhToRklALFdCWgbWE8TibABJPigww5H1i44y2Tj6wls3XWr3nzT6HhRrsb7BL1XQHGJ7b3xKD0I4aKsyKd8YWZ83dddHbqx6nCrzqsLTnnABIz7GDJvd1h22ns2BcODpCBuR5s0YjUSoSiRPi1cjMJow3X_lSN8umkkUpJpA6oTMZCPCti4dMD9Jyg1oCh0KBSbIzXkf7rYGvlqi8Kjzw4d7raRM-xXKt1iwIVT_ay1lVugVhar7oGSmTZQ21xQKWgf0F7DoNDS_B34hallpjHH_uiwEZ-TsaQAr3nsYnjTl62EQdrmXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7459db2f.mp4?token=sgkRGyyWppViaL0J8rMjghvkVfoVXDiekvhToRklALFdCWgbWE8TibABJPigww5H1i44y2Tj6wls3XWr3nzT6HhRrsb7BL1XQHGJ7b3xKD0I4aKsyKd8YWZ83dddHbqx6nCrzqsLTnnABIz7GDJvd1h22ns2BcODpCBuR5s0YjUSoSiRPi1cjMJow3X_lSN8umkkUpJpA6oTMZCPCti4dMD9Jyg1oCh0KBSbIzXkf7rYGvlqi8Kjzw4d7raRM-xXKt1iwIVT_ay1lVugVhar7oGSmTZQ21xQKWgf0F7DoNDS_B34hallpjHH_uiwEZ-TsaQAr3nsYnjTl62EQdrmXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج معظم الجماهير بسبب شدة الامطار</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79684" target="_blank">📅 01:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2c91accd.mp4?token=Sx3Lggthi3oqoVfzcF4QqEpb0krSk3PFhJU0h05mTokzFbYVzV5_iPaMTUlj3E8mB38DoWdrpqtqEyB0r2bOlki7sgJdFDqNtg4ZZ_CzRLcH8E9GVPCXwgkrO9jFTSz-VxJxkR1TtKbEODTgHMti3DxC2L0xCk_ep0X1_f5Gv8fRdHd_VQ_7fDmhkKxkjf3kGwha8sdyncYtMK8wVChBtDkSQ6bsVdYaRgyZoafWRnza-r6_7lTFm6yrpFJ2nP2sfQx7sb3FRdRNa8Hr0TkllMgEbfQnIkhDv-l1rqaOjXKrAfSDSy5d3gyEO_foYwznE5ngHXIEQMBr1SUUN-2QiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2c91accd.mp4?token=Sx3Lggthi3oqoVfzcF4QqEpb0krSk3PFhJU0h05mTokzFbYVzV5_iPaMTUlj3E8mB38DoWdrpqtqEyB0r2bOlki7sgJdFDqNtg4ZZ_CzRLcH8E9GVPCXwgkrO9jFTSz-VxJxkR1TtKbEODTgHMti3DxC2L0xCk_ep0X1_f5Gv8fRdHd_VQ_7fDmhkKxkjf3kGwha8sdyncYtMK8wVChBtDkSQ6bsVdYaRgyZoafWRnza-r6_7lTFm6yrpFJ2nP2sfQx7sb3FRdRNa8Hr0TkllMgEbfQnIkhDv-l1rqaOjXKrAfSDSy5d3gyEO_foYwznE5ngHXIEQMBr1SUUN-2QiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترند يشعل الرأي العام العربي، بعد أن زعم ناشط عراقي، بحسب روايته، أنه وضع أنواعاً من السحر أمام موقع دخول المنتخبين العراقي والفرنسي بالولايات المتحدة بهدف التأثير على لاعبي المنتخب الفرنسي.  خوفك لا ينكلب السحر على الساحر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79683" target="_blank">📅 01:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ستستأنف مباراة فرنسا والعراق ساعة 2:00</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79682" target="_blank">📅 01:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
🇫🇷
تمديد استراحة بين الشوطين لمباراة منتخبنا الوطني ونظيره الفرنسي 30 دقيقة بسبب سوء الأحوال الجوية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79681" target="_blank">📅 01:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbD1Bc_TPK0Q4xiqqQaHd9Oh7dmLzVPoFLOZa7NGhPurBMV1Pj0AUZ-pdVFW8yJfO3FK6A703is9lMuJ-kIyNCRVryHxCTWsfAwgwG8m9gByQwPRp-sVObZTbvghOOgVNmj6_guttNK-WwrRo59CqsNrcGj1rMTGt39c1hEsq7eo8P_C8Fx2p3jCyHWONh-x9rOyCTRZVFNGQZMg0KaDZuSlQIVP80C2tqM0Eg6LMgKzSf-J_-ZoK4rTQGKfOxxPwP-c80HoHzzswUD8p7rTBlVVrSWGE7jT6_W41emb0I9fS9YJh4DSfZs14m6_VbZT9GzYIrKevKl_PwTfo-VaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج معظم الجماهير بسبب شدة الامطار</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/79680" target="_blank">📅 01:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc252ab75.mp4?token=MmkzERmxszQC443RE_wTZD0RDvbfSk9MV6tPpzvBQmI67denczyvSTdtH1Ns44WpYfUhC7UgckV_1zB56uCtcTVdy-p4g7EBKgPSMHk0FFg8QQO1CBxGQ54rPJ3LuPq233AXWxGQwrF8E4ctDXHIqlqDvzAJAEkSXNB9ZZteK5gfiulttgBo91ocl9UOd7zHi-PkdY9czUOJQhkR6_Uo-Ffp5OoNT1P7xQNJOpTWbOZS74SyQicYT5X9kOI0zorc0DqGH5sV8EXZg0GHgdOqMHIbD423d3vSn1tOrnNcn_wnQG6m8FZWzCASufGoi4YY3r5eRe7nHBvvRNAWUGF3Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc252ab75.mp4?token=MmkzERmxszQC443RE_wTZD0RDvbfSk9MV6tPpzvBQmI67denczyvSTdtH1Ns44WpYfUhC7UgckV_1zB56uCtcTVdy-p4g7EBKgPSMHk0FFg8QQO1CBxGQ54rPJ3LuPq233AXWxGQwrF8E4ctDXHIqlqDvzAJAEkSXNB9ZZteK5gfiulttgBo91ocl9UOd7zHi-PkdY9czUOJQhkR6_Uo-Ffp5OoNT1P7xQNJOpTWbOZS74SyQicYT5X9kOI0zorc0DqGH5sV8EXZg0GHgdOqMHIbD423d3vSn1tOrnNcn_wnQG6m8FZWzCASufGoi4YY3r5eRe7nHBvvRNAWUGF3Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇫🇷
انتهاء الشوط الأول بتقدم فرنسا على منتخبنا الوطني 1-0.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79679" target="_blank">📅 01:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هدف أول للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79678" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هدف أول للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79677" target="_blank">📅 01:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مجلس محافظة المثنى يعلن تعطيل الدوام الرسمي في المحافظة اليوم الثلاثاء</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79676" target="_blank">📅 00:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
انطلاق مباراة منتخبنا الوطني أمام نظيره الفرنسي.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79675" target="_blank">📅 00:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
انطلاق مباراة منتخبنا الوطني أمام نظيره الفرنسي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79674" target="_blank">📅 00:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3459228578.mp4?token=fgXUUqsKVWtANoRJpCltn4uN4RLTE2LLn9jGWdiQnN9mkZs9m0_F6yix7NXzOtbv8HrYH8HjR3HGlyRqKOm0aFScSwG0l703bph67WgP2a7FjU03olGwujStwRtRZIzBfa4QBWU7X9rkKhZD7wAgQRIJZOHQ3RfKRpr-_kyWcIK_2t2TwXy8Lo7K2ulaZ9zolPdSWu92wwN07mRKcnUJ25U7M5NDYIwLW3CKBKkJSa5_bIVOSdHoqbC2Ke2Q1BdWAzAx1Xl-DGkEGvpSNqs4SoPPhbtCf8YZSQlXUGwamAbePhFO_pWovmTk0WS7zCCPOD3s8QoIC_dsnC3XhYZQAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3459228578.mp4?token=fgXUUqsKVWtANoRJpCltn4uN4RLTE2LLn9jGWdiQnN9mkZs9m0_F6yix7NXzOtbv8HrYH8HjR3HGlyRqKOm0aFScSwG0l703bph67WgP2a7FjU03olGwujStwRtRZIzBfa4QBWU7X9rkKhZD7wAgQRIJZOHQ3RfKRpr-_kyWcIK_2t2TwXy8Lo7K2ulaZ9zolPdSWu92wwN07mRKcnUJ25U7M5NDYIwLW3CKBKkJSa5_bIVOSdHoqbC2Ke2Q1BdWAzAx1Xl-DGkEGvpSNqs4SoPPhbtCf8YZSQlXUGwamAbePhFO_pWovmTk0WS7zCCPOD3s8QoIC_dsnC3XhYZQAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
مشاهد من مدرجات الملعب الذي يحتضن مواجهة المنتخب العراقي ونظيره الفرنسي، قبل انطلاق المباراة المرتقبة ضمن منافسات كأس العالم 2026.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79673" target="_blank">📅 00:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏محافظ المركزي الإيراني: طهران "غير ملزمة" بشراء منتجات زراعية أميركية وفقا للاتفاق</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79672" target="_blank">📅 00:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4670db6896.mp4?token=c7pOvcriDMh-_kpArgvcqY6KU2EnSh35gcoDjBw1l3Ay5HUiztSnt7BxLbz_afib6tcejCWoZdnMxf_Ox0s-uWk8yYeqXxEUftAL1GxPwVPhwSTszpXyLzclLafEgRCtl_eOgCIkuF75gMCpBZ7YyCyp92YhP_Fa_8fc7a5koa5WmvUzoQVl58iW4F48Hevd1K17g6BKYBgcFipnsbnOrL9phHInW-_bxoseE9DbTFoQjAEz00oEAwi0ii1hPSILQjLWgNJ9irAaxOzFFZBUUXTrEj0qCUf28rWvpEDF4IfCBcAg0uw-au5x7ZkCZLo2ZShUrtWUOe3_Itj4hAZoBXD-BQrWVVXo-s6WmuYGsRW1D1NE_Txez7rk9kdPLjpvuwT3cgf8Dxx9fWjzuDx6wYLZA4j-8GZkk80AOwd4jD2p_j-VpW87_CFdWwWIs66JohvaXB5O3BcXjdP8goEf4zNg_IwR8SJzC6fu0Dq9cShUqbKULlyp5Tl6a3GKDkGwO4IfExf_YwpZiDp7Iu5fgd1AjLzDO0Kgf3ZZkEePCA57BworoT_zA0TNxrVXqG412V4EDS8O5UVMVCDYi0Km3IWOiv9yuCnyoOmbwHzXTdW0UnnpV2Z7KP2T8SWVZlTZJ8EolpVB-WqhX762ysn2X6D2gEvqS65xk9-O3Cporq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4670db6896.mp4?token=c7pOvcriDMh-_kpArgvcqY6KU2EnSh35gcoDjBw1l3Ay5HUiztSnt7BxLbz_afib6tcejCWoZdnMxf_Ox0s-uWk8yYeqXxEUftAL1GxPwVPhwSTszpXyLzclLafEgRCtl_eOgCIkuF75gMCpBZ7YyCyp92YhP_Fa_8fc7a5koa5WmvUzoQVl58iW4F48Hevd1K17g6BKYBgcFipnsbnOrL9phHInW-_bxoseE9DbTFoQjAEz00oEAwi0ii1hPSILQjLWgNJ9irAaxOzFFZBUUXTrEj0qCUf28rWvpEDF4IfCBcAg0uw-au5x7ZkCZLo2ZShUrtWUOe3_Itj4hAZoBXD-BQrWVVXo-s6WmuYGsRW1D1NE_Txez7rk9kdPLjpvuwT3cgf8Dxx9fWjzuDx6wYLZA4j-8GZkk80AOwd4jD2p_j-VpW87_CFdWwWIs66JohvaXB5O3BcXjdP8goEf4zNg_IwR8SJzC6fu0Dq9cShUqbKULlyp5Tl6a3GKDkGwO4IfExf_YwpZiDp7Iu5fgd1AjLzDO0Kgf3ZZkEePCA57BworoT_zA0TNxrVXqG412V4EDS8O5UVMVCDYi0Km3IWOiv9yuCnyoOmbwHzXTdW0UnnpV2Z7KP2T8SWVZlTZJ8EolpVB-WqhX762ysn2X6D2gEvqS65xk9-O3Cporq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
نزول لاعبي منتخب الوطني الى ارضية الملعب لاجراء الاحماء قبل انطلاق المباراة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79671" target="_blank">📅 23:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4619fb40.mp4?token=vW4mU9jeSZXIlsDmW3YODX8s3hw-sFN9gGjCID4CBCviDN0BPH720m2t8ofAckxwsdvSrztXsiSW1np49ZUs8Bc-kUDrxRRzXJXkGpKel2_MhksA6WVFCwzNRA_2CE6xpYSy_YFGVcQ02hpPUXpmosL9tFM6DxuMBcrg-kX-ZVYhGbDQjQ3aROyglknNKOA4TG7lyREWWs8ksltI9HNJvbdw_FTStfd4Nj4rw9v2Xxn2Q9eqvk4ALA1QaM2T1KYhsv0mAppoiZmvvD5PZ5Dqdvy8joumFaR9LyyaY8fp9oDMvAfAj7C2LOgipjNNtFLkhG_mq-xPyAAs3cmLWlm33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4619fb40.mp4?token=vW4mU9jeSZXIlsDmW3YODX8s3hw-sFN9gGjCID4CBCviDN0BPH720m2t8ofAckxwsdvSrztXsiSW1np49ZUs8Bc-kUDrxRRzXJXkGpKel2_MhksA6WVFCwzNRA_2CE6xpYSy_YFGVcQ02hpPUXpmosL9tFM6DxuMBcrg-kX-ZVYhGbDQjQ3aROyglknNKOA4TG7lyREWWs8ksltI9HNJvbdw_FTStfd4Nj4rw9v2Xxn2Q9eqvk4ALA1QaM2T1KYhsv0mAppoiZmvvD5PZ5Dqdvy8joumFaR9LyyaY8fp9oDMvAfAj7C2LOgipjNNtFLkhG_mq-xPyAAs3cmLWlm33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترمب
: مضيق هرمز مفتوح بالكامل،والأموال الإيرانية المجمدة التي سيفرج عنها ستستخدم حصرا لشراء المواد الغذائية من المزارعين الأمريكيين.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79670" target="_blank">📅 23:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda743fbcd.mp4?token=g1D9CMW0R6fFpigUZ5VtQt_ukXn4wVO734IydvxFk9oUH-SQhlmY1fMX50rAXKGtMWT10dQwN5GsZyaQiwaisMfJU2Kvex7EEkNtev_IuWWurdJ4C81B1NrSTz5NQ3oTfb-Pv7N91eVFfD9omOF2vNWyUDE5oAElTkSKs64vFF3GNksn9S4S2dAuR62EgbZ5AH11pTsEAaSj9qkZbv6TSUK03V5hRBDtD-vtRL6jhCyb0TGlahazl9I3flsOPxsdU37HPUMWwRb2D9alWIZ4YRFGNpr8WGQe5svmyyyfZc1S1293CczRTjs-sCLIf8YIoF5AIHUPV766TJCJJN2QLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda743fbcd.mp4?token=g1D9CMW0R6fFpigUZ5VtQt_ukXn4wVO734IydvxFk9oUH-SQhlmY1fMX50rAXKGtMWT10dQwN5GsZyaQiwaisMfJU2Kvex7EEkNtev_IuWWurdJ4C81B1NrSTz5NQ3oTfb-Pv7N91eVFfD9omOF2vNWyUDE5oAElTkSKs64vFF3GNksn9S4S2dAuR62EgbZ5AH11pTsEAaSj9qkZbv6TSUK03V5hRBDtD-vtRL6jhCyb0TGlahazl9I3flsOPxsdU37HPUMWwRb2D9alWIZ4YRFGNpr8WGQe5svmyyyfZc1S1293CczRTjs-sCLIf8YIoF5AIHUPV766TJCJJN2QLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
تشكيلة المنتخب العراقي لمواجهة المنتخب الفرنسي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79669" target="_blank">📅 23:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paA6AP0SHqjBFMU0Z942TRizrdiXl0bsZsl_KbWtXdjxXjDUY1wR1586Lx1aNqr6YXyfyPEECY1SKezvajzHmGPWwuoF4MbSVFR4eSDgkGLkDNjP3N8nkfN-qIkMLYw_JaIOMcXe8A7sO0OK_1jPmHBTfJwfwjc3gGI2FeBPw8Pjy-K_IhBdjQCgwzzT0PADb9cU_jcsvI_ND0xdHik4cBLZCQMIa_hqS0TiuDwSOpG4Bb2qyWvVLFH1T4LUs3FcgQZnC6V-XL6k4-_jqB3yPk7N5tDuGdo2wnRsoeonFe4fxY0StRC1Pch4kYfCsw6dDWI8eUHDUpXayolX7yVp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
تشكيلة المنتخب العراقي لمواجهة المنتخب الفرنسي</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79668" target="_blank">📅 23:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
‏خفر السواحل الأمريكي يعلن تحطم مروحية من طراز MH-60 جاي هوك في ألاسكا، وفرق الإنقاذ تستجيب للحادث.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79667" target="_blank">📅 23:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79666">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5ad36da0.mp4?token=mvyHIcvZ5iw3jJG37Xhv9R-SF6FunPxkkmmu7W24wMnQlPdcLFKplD5NcfzlEItgh-oU6VVAfd0jYSn8JtfuOkwznz9MewlrcDRFj4hg6UMNJi3_vNsTc7gwTHR80Dx6CcP5hsg6kF4CjDC5zxMDYUR0_L5hPHmSBcTRjondqZMUfeF5_mFeY4_a3jpZ56SjjYKxkBnRTYBTIm2sifazU2YdCEb4-limFvhDSQ-gjo8lykcwLmXciLOywzVVzHMXz8fRXdAaPg1gDZgeJVTkuwlkUWdpl0raIqs6cKBidaDSXCWsjDsBg-cKmRKIQ6yZvNDCK5VUoz4DEtDuHxN6Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5ad36da0.mp4?token=mvyHIcvZ5iw3jJG37Xhv9R-SF6FunPxkkmmu7W24wMnQlPdcLFKplD5NcfzlEItgh-oU6VVAfd0jYSn8JtfuOkwznz9MewlrcDRFj4hg6UMNJi3_vNsTc7gwTHR80Dx6CcP5hsg6kF4CjDC5zxMDYUR0_L5hPHmSBcTRjondqZMUfeF5_mFeY4_a3jpZ56SjjYKxkBnRTYBTIm2sifazU2YdCEb4-limFvhDSQ-gjo8lykcwLmXciLOywzVVzHMXz8fRXdAaPg1gDZgeJVTkuwlkUWdpl0raIqs6cKBidaDSXCWsjDsBg-cKmRKIQ6yZvNDCK5VUoz4DEtDuHxN6Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
خلال زيارة بافل طالباني لإحدى الكنائس الكلدانية في محافظة السليمانية، وجّه إعلامي تابع للبرزاني سؤالاً له بشأن تشكيل الحكومة أثناء مغادرته، ليردّ عليه بانفعال قائلاً:
"مو وقت هذا الكلام يا حيوان".</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79666" target="_blank">📅 22:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79665">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d275b950.mp4?token=WTynJRJKQ7emlB-BhdvrfYrr5oJYsdSYF22mN8FseMzGdOdk1bhGriXogjXN0j689KsQSouzlv232wy95f4bTYK3Qj8yd18F2jUXKD8g4LKoEalU8su7UvlqnekJSJvyg8GYhwnG63UbtPJPbEHcaxeWwWgJKS4vaRETo27T-l1-xpxz7E5XBQCefKS6oiQ1oEb2xCTWc95ZmoUvNhbnJMen31OHWSGn9DgBEFt1qE4EY4zrtq6zdc7pm8T2PFwsx9OYT0qbkxN6oinDopc1GEgtkDyG58iejAEUtbHPmuF-wL6MSmoWi4PSz2CAoujkvEzIucWFn6x5pHRT_urC1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d275b950.mp4?token=WTynJRJKQ7emlB-BhdvrfYrr5oJYsdSYF22mN8FseMzGdOdk1bhGriXogjXN0j689KsQSouzlv232wy95f4bTYK3Qj8yd18F2jUXKD8g4LKoEalU8su7UvlqnekJSJvyg8GYhwnG63UbtPJPbEHcaxeWwWgJKS4vaRETo27T-l1-xpxz7E5XBQCefKS6oiQ1oEb2xCTWc95ZmoUvNhbnJMen31OHWSGn9DgBEFt1qE4EY4zrtq6zdc7pm8T2PFwsx9OYT0qbkxN6oinDopc1GEgtkDyG58iejAEUtbHPmuF-wL6MSmoWi4PSz2CAoujkvEzIucWFn6x5pHRT_urC1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سمح لجماهير المنتخبين الفرنسي والعراقي بدخول للملعب بصورة طبيعية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79665" target="_blank">📅 22:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79664">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev64tCaceYXp5LuBXMx50oVrA_mFcjKuhFB5E2HfeChFk-Ct0E7wyf4k06uSckxvu0waPoXo7Lf0vD07HaeyurXseyc3cf_zQbCbzy8cOPUEBivutjda8MNDJ4iASDNm0pPyRU7tCgDnk8aZEwa9t2yB2sV639Srxqlqk5f2b8qQx3P9CVCHvXc95RfDfRCHC5SqoF1exCcBeSE5aLUgm3AkyGs6ddrN9pn2A18ByHDIW7vMKCq0Jupp9dgA38DN6buvQw4Yx8NzXc8Lw44nncNtjFwVW427E8dgfhBCRRmBWq6CwseehDzSXGEKp_4Ko2bs4ycbgfmW5HWNbwntZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد جاسم : المباراة بين العراق وفرنسا قد تتأجل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79664" target="_blank">📅 22:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭐️
عاصفة جوية تأخر فتح أبواب ملعب مباراة العراق وفرنسا.  يبدو أن مفعول إبراهيم الخلاني قد جاء بنتيجة
😆</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79663" target="_blank">📅 22:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbb558716.mp4?token=FUwohtS1uudjAYgSBI6-MoaWUrlzPLXbx-6kSVFp6PSxPTJPvGtreloiXFDH11RI_qn4u1KjpvHwXQSjpJUvrhzI-PSYcDDxfY1jZNWisel2AWv6oURK3oQwTLo2yf6Xteowyv0Dh5wCkBhFEFhlH4vlwrDWhZKS2qfDIUAYz9l_Yp9XEkEX55q1S4K8auPFSTtN7dAri0E9TJRsnvwWm6f_Qh7aBc4EXBmBJ8XOXG5kdhrWmtmNr87hI0bk-oOZM2mZuTobaIMZqXPgAhnk7ZPfNIws5ovX4a3Krr6_gMoYjPKuiPnoFIlYYnRt37WCOYwfeG2AubvbYHmsrsYKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbb558716.mp4?token=FUwohtS1uudjAYgSBI6-MoaWUrlzPLXbx-6kSVFp6PSxPTJPvGtreloiXFDH11RI_qn4u1KjpvHwXQSjpJUvrhzI-PSYcDDxfY1jZNWisel2AWv6oURK3oQwTLo2yf6Xteowyv0Dh5wCkBhFEFhlH4vlwrDWhZKS2qfDIUAYz9l_Yp9XEkEX55q1S4K8auPFSTtN7dAri0E9TJRsnvwWm6f_Qh7aBc4EXBmBJ8XOXG5kdhrWmtmNr87hI0bk-oOZM2mZuTobaIMZqXPgAhnk7ZPfNIws5ovX4a3Krr6_gMoYjPKuiPnoFIlYYnRt37WCOYwfeG2AubvbYHmsrsYKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات الأمن الكندية تحاول إخلاء محيط المركز اليهودي في مدينة مونتريال الذي تعرض إلى هجوم مسلح وسط إستمرار الحدث الأمني.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79662" target="_blank">📅 22:31 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
