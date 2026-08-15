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
<img src="https://cdn4.telesco.pe/file/g6lBR9zvbBkS3V9j5qjD_Y9V5HI633-tIq7TkpwbtOTWYSPRUDpYqC2HnBdvi2MKUkWzTwJq8DPfXSV32dfj_XprLxNO1_DeWhlyu5D0lFPttbArCe7IvQFAPVtDPAx1uZ-RBjFu6I2Ad7tQYzAsaMoAYUkwK_yMMFrtqwPRvHAaaawgEwNzW3K3kV2hju4qeTLQ30e9Y3_ml7JocGMYlN8xfTtI_zaVNiyOJYC38MVDfNygR2K7NlEDm_FQOSCAFo9f6XcQNqF6IoA9-mNT48WdT6gapntBpY-YCjNdxFU7g21sIUrOthJerTLSQXZmJPJoOd9vPq09ElMW_MDYuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 20:17:01</div>
<hr>

<div class="tg-post" id="msg-87859">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇱
إعلام العدو:
تعرض دبابة لهجوم في قطاع غزة نتيجة لغم تابع لحماس.</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/naya_foriraq/87859" target="_blank">📅 20:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87858">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هل العالم بوضعه الحالي قادر على فقدان أربع مليون برميل من العراق في حال اندلاع الفوضى ؟!
هل يعلم الإطار التنسيقي ان حجم ضربة لوبيات الطاقة العالمية للعراق الأخيرة الهجوم الأكبر" ضربة السعودية للعراق " كان بسبب فقدانهم نصف مليون برميل فقط من بقيق !
هل لا يرى ساسة العراق افول امريكا بهرمز و وضع قواعدها بدويلات خليج فارس ؟! وبروز نظام الدفع المسبق للسفن المارة بخليج فارس  ؟!
هل ستقطع علينا امريكا الدولار الذي هو منقطع أصلا على العراق منذ ثلاثة اشهر ؟! وتمنع علينا بيع السندات ؟!
ام ستقطع الكهرباء التي هي أصلا مقطوعة منذ ٢٠٠٣ ؟! ويومية هزي تمر يا نخلة اجه جنرال الكترك راحت سيمنز ؟!
متى يعرف قادة الإطار التنسيقي ان مصلحتهم لا ترتبط بامريكا ولا البرتقالي وان مصالحهم الاقتصادية مع احزابهم وخوفهم من المجهول لا يجب ان يكون على حساب سيادة وتاريخ شعب العراق …
كل مشاكل العراق وبروز نظام بشكله الحالي القريب من امريكا وتحت سيطرة الحاكم في العراق والشام " توم باراك " بصورة مذلة يتحملها قادة الإطار التنسيقي ال 11 …. وعليهم اما ان يتولى مسؤوليتهم التاريخية او ينكفوا عن إدارة البلد …</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/naya_foriraq/87858" target="_blank">📅 20:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87857">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM5rR1yTuP5ohMS9MFiprEBlhyQAIxRujCWHlijwGQUBHYGGLBF2IVq4l4ZLumrbNCDLz-hSWQIdIvl-nRzCEP6zp9u_7LI581U_zTHitYQnnmU1yUwAbUKy3GhPBcPHqIjY-WzUnOBVJvxC1WwJeeker4kV3dofjZDyompc7IlxGeUFfxI_VHwpSIvnpBBuUbXF4nu7hysxg13Q_w3yix-btXv7r-i6rzDSxBujlnSnP95uMQBzvoafgsxZ_ZgXA7_N-piGyVadyF7nW60KOG_4PfwuHr3MTOCPU693g8T5a2aA9XV2TQD3lV0rkVRmC567s30gCmoq5xkeFmT5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اول تعليق للبرلمان العراقي
زحمة قناة رسمية تثير الفتنة</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/naya_foriraq/87857" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87856">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huDrGgN4Gvczpj6-f5V0B9hQJ2YtjUlgUqmpj7ybXSqiMSlybYCtffovgR3KzB7T5FUTjDTmsNua4LY7m7W6egD7oplS9B-2LGhRIEvYnBjjagRGAr5Be4LnH6vlpzqRMAxzRJ5JUJCRjujYr2RlpDFFuAARLvWFcf4IsszSDqr-XcrZLtlmBme2LK_PGQ3-qxMtj6kyB8VkBJzpNhAA3Ih-Zx_wlIQLeQOyH2ueReBh5dAqqA6A9K-qNgP1hBmtP2UOzcPHx8etGz_tL5Hyl9agTIlEcB52tuKgbB15hzGOCwXT1GfnFMyVQI6mxegIfNPKO3ZMTiwwvII_gau7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: على الرغم من المظهر غير الودود في هذه الصورة بالتحديد، إلا أن هناك العديد من الصور التي نبتسم فيها، وأنا و Kim Jong Un نتفق تمامًا.</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/87856" target="_blank">📅 19:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87855">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
أعلن المتحدث باسم كتائب سيد الشهداء،
أن الفصائل المسلحة لم تكن وراء الهجوم بالطائرات المسيرة الذي استهدف مدينة أربيل فجر الجمعة.  كما يوجد "شبه اتفاق" لوقف العمليات وتأجيل الرد على الهجمات السعودية.</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/naya_foriraq/87855" target="_blank">📅 18:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87853">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇾🇪
مدير ميناء المخا اليمني يوقف العمليات بعد هجمات الحوثيين.</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/87853" target="_blank">📅 18:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87852">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
رئيس مجلس امناء شبكة الاعلام العراقي: تقرر ان تخضع جميع الفواصل الاعلانية اياً كان مصدرها للفحص والمراجعة من قبل الادارة العليا للشبكة ولجان الفحص المختصة فيها.</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/87852" target="_blank">📅 18:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87851">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇱
مكتب نتن ياهو:
هجوم لحزب الله في "منطقة الأمن" اللبنانية يؤدي إلى إصابة ثلاثة جنود والجيش رد بقصف مقر أصدر أوامر الهجوم ولم نعلم الا لاحقا ان بداخله مدنيين.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/87851" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87850">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRzCl4aOVJxMu2EaQnzDIpbOvY5p3auF4hpbK1shFU54pfjgZN0m5hDYMIrItMzARrAkTn1OWkgntRK9opTptKQ8RxLRtrcm1BInEGupiM-4eeJY8_4361944HzDJ9NboIG3NNp1Ner_2Sy2JlwZT1h0zp2ytdePuIhbE2PcbJMWR0uREaFGLlUqfD-KVc8nXvGzQZC9kPWOVpA7woY7EaxvX4AWunrnB2j42YN3LODPk1Zq_LMHtVb3aQkNyOcQWXtiPL6IHAbEC40XhTildRR4iyPHz4Ol5nVR1cqoWbkdUzOG0WGeq7pSlTEaCSjgcsOMgB0t4i5CCKSdX8dM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئيس مجلس امناء شبكة الاعلام العراقي:
تقرر ان تخضع جميع الفواصل الاعلانية اياً كان مصدرها للفحص والمراجعة من قبل الادارة العليا للشبكة ولجان الفحص المختصة فيها.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/87850" target="_blank">📅 18:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87849">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عشرات الآلاف يقررون التظاهر ليوم غد ايضا احتجاجاً على الدعوات الطائفية في محافظة بابل وسط العراق   المواطنون يطالبون بمحاكمة عدنان الجنابي و شيوخ الفتنة والتحريض .</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/87849" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87848">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
مصادر خاصة بنايا   حراك برلماني لاستجواب رئيس شبكة الإعلام العراقي تمهيدا لاقالته وذلك لدفعه وترويجه الاقتتالات والحروب الداخلية في العراق .</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/87848" target="_blank">📅 17:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87847">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b7ffa1c5.mp4?token=QCdBzcUaLCDVIjF8_taG8ikUBi2F0T0Rh_ZzZWjsz3npRnjr8Z-sdbvzoHSTQYekq5FACQ9grPxdzlVGT1e6h8XfMbGfvGApJdKOe49c5KIXjF8mFfDKPQKTbUrtDMW2PrzZPyNj2kePQgSHe-t5bD-uXCMxxPRIvWK9QvqYnIk9aAuHwZsVPvEm8xS5PXLW7sfHtBEoh-8YNg94gcntgh0u_hqyoc8wq5hDlxV2DjORsxcR1m-R-CjCUA4-qy9PSk_YCQ3DfBUWGeyJ-7yVrnQI6pq0eTH_6PVGozMjHnINnuTPrKKcuyGx_0rO38xMzRRRSCg_N8g7NyakZPtYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b7ffa1c5.mp4?token=QCdBzcUaLCDVIjF8_taG8ikUBi2F0T0Rh_ZzZWjsz3npRnjr8Z-sdbvzoHSTQYekq5FACQ9grPxdzlVGT1e6h8XfMbGfvGApJdKOe49c5KIXjF8mFfDKPQKTbUrtDMW2PrzZPyNj2kePQgSHe-t5bD-uXCMxxPRIvWK9QvqYnIk9aAuHwZsVPvEm8xS5PXLW7sfHtBEoh-8YNg94gcntgh0u_hqyoc8wq5hDlxV2DjORsxcR1m-R-CjCUA4-qy9PSk_YCQ3DfBUWGeyJ-7yVrnQI6pq0eTH_6PVGozMjHnINnuTPrKKcuyGx_0rO38xMzRRRSCg_N8g7NyakZPtYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🔻
الموضوع هو اكبر من المقاومة وسلاحها ، الهدف هو الشيعة وعقيدتهم التي تقف اما المخطط الصهيوني الابستيني ومشاهد ملايين الزوار من الشيعة حول العالم في الأربعينية هي مشاهد مرعبة لأمريكا وإسرائيل ودول الخليج والهدف القضاء على هذه المظاهر لأنها شعلة الحق الوحيدة المتبقية في العالم ..</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/87847" target="_blank">📅 17:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87846">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الرئيس التركي: استمرار الهجمات الإسرائيلية على لبنان يشكل مصدر قلق كبير لنا</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/87846" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87845">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سلاح ما نسلم   مثل ابو حميد ما نصير</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/87845" target="_blank">📅 17:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87844">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c189e3c62.mp4?token=HFPTUmGHU54PhH4_l0Rvprtb41L4BHGeH5xQihJvCqZGFu1j49k-uxBF1yLvM44e78xj_gY4UhG38VXmcCDKXJPoahKcqxdJx7MWE1OXLY3yM7jxXZUoyZaNZ07MxaITrVNXzSkHV78VrRxuwnylXz2gbtFlepAnUbfBs7ykclj-fdN8C100KA3t0ujfZaYzYRLvIdG_we-1v_PK42G_iQe3EwNC7a3TcJwwRRCyeVBuy27G_R3q5pYEYCR5tSoaxa3iPBtAA4i6B6RWljnKMVbPx9cPeK6OS18eXIamTErrP70OlAAThwEWmDyqfgoNsbD5vzs4XAhV9wM0seebOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c189e3c62.mp4?token=HFPTUmGHU54PhH4_l0Rvprtb41L4BHGeH5xQihJvCqZGFu1j49k-uxBF1yLvM44e78xj_gY4UhG38VXmcCDKXJPoahKcqxdJx7MWE1OXLY3yM7jxXZUoyZaNZ07MxaITrVNXzSkHV78VrRxuwnylXz2gbtFlepAnUbfBs7ykclj-fdN8C100KA3t0ujfZaYzYRLvIdG_we-1v_PK42G_iQe3EwNC7a3TcJwwRRCyeVBuy27G_R3q5pYEYCR5tSoaxa3iPBtAA4i6B6RWljnKMVbPx9cPeK6OS18eXIamTErrP70OlAAThwEWmDyqfgoNsbD5vzs4XAhV9wM0seebOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات الآلاف يقررون التظاهر ليوم غد ايضا احتجاجاً على الدعوات الطائفية في محافظة بابل وسط العراق
المواطنون يطالبون بمحاكمة عدنان الجنابي و شيوخ الفتنة والتحريض .</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/87844" target="_blank">📅 17:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87843">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyVJUdg6uv1Ivup652Y80FqohDMY5FSNHZZtNsqgFAYYVi5cmE-y1h4QZROVsB8T8LqmE27NDC-o2B4X8TGsDdb2Hfp4XYgH43n_60M2qpE27xzuf-anaypHnH4majgui84UhkJk2NXGy9YFxA9vmKWkqqaKhdwSwlQaOweGUraZ4EZzpBJ0JVpiCNpT7Mv4uIbr38jckUV0AvXY5ejWa4g47F2H21YgCPMvnbqlP0IIWrnA106JPMYpQvMFcGhJZFb6UE6ikbLwoJnEwzj4qanW4t5p9_oBHteR_WRORHaOviHh7g-hdDMXKWnqimyXep-8t8gr9HP08dAxGCHEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
منصات التتبع:
تواصل أكثر من خمس ناقلات نفط عملاقة عمليات نقل النفط من سفينة إلى أخرى قبالة سواحل الفجيرة، مما يشير إلى أن صادرات النفط الخام من العراق والإمارات والكويت لا تزال تعبر مضيق هرمز. وتدفع بعض السفن رسوم العبور الإيرانية، بينما لا تدفعها الأغلبية.</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/naya_foriraq/87843" target="_blank">📅 17:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87842">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb7dc434c.mp4?token=g0Pjm4Tc58bQX2qQtLKMM0DXONrRiNz7lUvj9KH4jxWn_pZeSMLVk1dID18kvwsyFkHfF8zkibQ5KYK7Je47BAKiGsHaNwR-c4uM8B-kFaE68QAwT8pza_I0kBnil8qzlpyFO82t3QKH9VtibQstR6r7Y138O69pmsqM9I_9q4GA5geCY1_xUk7iHoWmdwD5Hr09bWy2h7qQoS9uuz8uR0KLPYhtQnBNfOuZ5c3k4aDu_ZqRhwCr9Mb-CjHggwkOCI0g64PpN7UQR7zzHe9c7R_0rGBj3Dpu2ozlnfNDY-hcuXfZnt0RVUhCUn-UNcGEeci7T5lNjevRf2bj_myZKKylRpnw29EsilUIjAS1dcJ6_BXAZ8tkZuF-I6Y6p7rXc5W1RZ5c5iATWK0f-S1p1tfbGgrW81lFdfNTsTbfq7IIOmS7YCjWYFnSMW5hsEj9PpADePC3fr2TwE8sE3dzGihTHdfCBxXyKUrWonn7rRYpO7_XDAnTmQMFsWJFIdBTbEmoRkO9kBs04PsVaomjEjrzE_XRR89msj18S4sSEd3KHvc80_zmXRyfcholYrTV89djpBkyjZzbhpOaEe8Rjk_tFoaffPqwLYrhhN6NKaW9FNWGGJMMPuXjmJD4j0bLySX1Mx7PTTJdAzI7COcdL-HKH58hx-fyRUQ9ggRgs1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb7dc434c.mp4?token=g0Pjm4Tc58bQX2qQtLKMM0DXONrRiNz7lUvj9KH4jxWn_pZeSMLVk1dID18kvwsyFkHfF8zkibQ5KYK7Je47BAKiGsHaNwR-c4uM8B-kFaE68QAwT8pza_I0kBnil8qzlpyFO82t3QKH9VtibQstR6r7Y138O69pmsqM9I_9q4GA5geCY1_xUk7iHoWmdwD5Hr09bWy2h7qQoS9uuz8uR0KLPYhtQnBNfOuZ5c3k4aDu_ZqRhwCr9Mb-CjHggwkOCI0g64PpN7UQR7zzHe9c7R_0rGBj3Dpu2ozlnfNDY-hcuXfZnt0RVUhCUn-UNcGEeci7T5lNjevRf2bj_myZKKylRpnw29EsilUIjAS1dcJ6_BXAZ8tkZuF-I6Y6p7rXc5W1RZ5c5iATWK0f-S1p1tfbGgrW81lFdfNTsTbfq7IIOmS7YCjWYFnSMW5hsEj9PpADePC3fr2TwE8sE3dzGihTHdfCBxXyKUrWonn7rRYpO7_XDAnTmQMFsWJFIdBTbEmoRkO9kBs04PsVaomjEjrzE_XRR89msj18S4sSEd3KHvc80_zmXRyfcholYrTV89djpBkyjZzbhpOaEe8Rjk_tFoaffPqwLYrhhN6NKaW9FNWGGJMMPuXjmJD4j0bLySX1Mx7PTTJdAzI7COcdL-HKH58hx-fyRUQ9ggRgs1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافد حاشد لموقع التظاهرة في محافظة بابل</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/87842" target="_blank">📅 17:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">المتحدث باسم الخارجية الايرانية بقائي: لقد تم التوصل إلى اتفاق بشأن خريطة حركة الملاحة بين ايران وسلطنة عمان</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/87841" target="_blank">📅 16:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87840">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da068288c4.mp4?token=UZrr2Go-jUnRVxOReWhG4QlrdLdELCVltk0AwQJt13CAxirOzKbU0D2c7C7KzsCIsZMygX778thdK4NdDs09UcWW4FXm0GXja_iOx5qzjd_jvA_Gn58ztNHBfdjCa-ZfsgDhWnD8lkNTAUid0DNISM_kid5lhp1nwR45yVdW5U7XV57mhcJn7jvm-i4X-VNq3x97tCn1HVb7v-exAjR1VM-D9ydhdan-rmzvlv1gKX2fJVSAXmQ08L-44EiJwqN-mMNR37wUlsSFovzq6LntIG2ZqZi66OzHV7oynNc5bYJttFirTVSDCBprbnXq2N7rJgwJXEbLqYuyPznIuYv66Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da068288c4.mp4?token=UZrr2Go-jUnRVxOReWhG4QlrdLdELCVltk0AwQJt13CAxirOzKbU0D2c7C7KzsCIsZMygX778thdK4NdDs09UcWW4FXm0GXja_iOx5qzjd_jvA_Gn58ztNHBfdjCa-ZfsgDhWnD8lkNTAUid0DNISM_kid5lhp1nwR45yVdW5U7XV57mhcJn7jvm-i4X-VNq3x97tCn1HVb7v-exAjR1VM-D9ydhdan-rmzvlv1gKX2fJVSAXmQ08L-44EiJwqN-mMNR37wUlsSFovzq6LntIG2ZqZi66OzHV7oynNc5bYJttFirTVSDCBprbnXq2N7rJgwJXEbLqYuyPznIuYv66Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلاح ما نسلم
مثل ابو حميد ما نصير</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/87840" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87839">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d027dce5.mp4?token=O_7tyolrFmdWZcyRDl1MkHtHxCQ9flF5jwY1w9wDtUqMJENv6C6bji_M4v9XUkAJL8a1-IJ1DzUmj2zWW5QS1_j1RZjDt0rkM2o_m266xgZDD7WXv1HnbCcl8IQymT7JX3e79Ak78VRIeTa-r7uINBMP_0UPlQVIPp1iMHUKmA-D7HnItQzYJMdNDyrb1pYWT1kukVlnGJWZtS4qCCjgUwopADXCSoNqpV-I96ADeyguP2mcu4Np1hEdrm66EKg3Gj7XefepLA0d3bgahkdUlHJKEcwtQZqvI3YxWknsgeOD263Mz_McK3INmRP8JqejyhaMwikpB-mJa8un4VEYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d027dce5.mp4?token=O_7tyolrFmdWZcyRDl1MkHtHxCQ9flF5jwY1w9wDtUqMJENv6C6bji_M4v9XUkAJL8a1-IJ1DzUmj2zWW5QS1_j1RZjDt0rkM2o_m266xgZDD7WXv1HnbCcl8IQymT7JX3e79Ak78VRIeTa-r7uINBMP_0UPlQVIPp1iMHUKmA-D7HnItQzYJMdNDyrb1pYWT1kukVlnGJWZtS4qCCjgUwopADXCSoNqpV-I96ADeyguP2mcu4Np1hEdrm66EKg3Gj7XefepLA0d3bgahkdUlHJKEcwtQZqvI3YxWknsgeOD263Mz_McK3INmRP8JqejyhaMwikpB-mJa8un4VEYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنين يتوافدون الى موقع الوقفة الجماهيرية في محافظة بابل لادانة عودة الارهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/87839" target="_blank">📅 16:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87838">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏وزارة الخارجية الروسية: شحنات الأسلحة الأمريكية التركية المحتملة إلى كييف ستضر بعلاقات موسكو مع واشنطن وأنقرة، طلبنا من واشنطن وأنقرة توضيحات بشأن مزاعم وجود خطط لتزويد كييف بالأسلحة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/87838" target="_blank">📅 16:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87837">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/87837" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87836">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
اللواء 52 بالحشد الشعبي يتسلم قاطع بسطاملي في آمرلي من الجيش ضمن تنظيم توزيع القطاعات والمسؤوليات الأمنية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/87836" target="_blank">📅 16:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87835">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa80e2a4e.mp4?token=Qoi8nY5ElJMSPQGks95S9C9JdUbNhkYfh4Ae2LiHNA-mDRZOGHj_rHKoZFTyydBrlOtPkPpPD1b5hL2grC2C0kr29WWza4cchyW8cXqsQ8lGbYYI3SO3gMUUR0l6gcOnWeqGj2DGNtYWA2ZXa2iM5oOVpUzagrhCINkuvJP7T1y1fFb2V8vXXHa0DrzrTg590r-tOSsgmQCUieJA8HQQR4dstZ2ESFujCdf8lO5R4qI_3kWrb21fCzm439lgJQbmuLiPr8LOw1mCeMM9UpgI6X3N3erTsmQ9_f1L6nVE-UsIn90Hr18NeC7wf9kTOpHyd7ddtXrJOntb5sE8DvcxrZBLSNmAbBen60E0fo12_0V-jFCrq202tqvVzBjeNntvOOWj0AxgXWVxWfNdBVGZOYM_7KDsHxDipw0aNAKi0faBoavZBDIwy4UHumRpXdxxamZcOH3ozH6QLPaA3uoRzA3biKzC7ODZwrjDhxxHcr56J1v5rDb5tYA0xPjtVuMediGuRvIripjsEafEujnompKIseuEUGN4hC-_2BpZUXyjWX4cpv0c73YPZ-dw-T8JWbhMZNuukePQDzF5xU1Lol5VFVSOfYIgzI7UTN4XCVg4z0oBGFwOfvJ3sGgT-i5Z3pMyEO-5Icw8WICCms8Pnmy_XtRqKu4V7kOu7toi0wo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa80e2a4e.mp4?token=Qoi8nY5ElJMSPQGks95S9C9JdUbNhkYfh4Ae2LiHNA-mDRZOGHj_rHKoZFTyydBrlOtPkPpPD1b5hL2grC2C0kr29WWza4cchyW8cXqsQ8lGbYYI3SO3gMUUR0l6gcOnWeqGj2DGNtYWA2ZXa2iM5oOVpUzagrhCINkuvJP7T1y1fFb2V8vXXHa0DrzrTg590r-tOSsgmQCUieJA8HQQR4dstZ2ESFujCdf8lO5R4qI_3kWrb21fCzm439lgJQbmuLiPr8LOw1mCeMM9UpgI6X3N3erTsmQ9_f1L6nVE-UsIn90Hr18NeC7wf9kTOpHyd7ddtXrJOntb5sE8DvcxrZBLSNmAbBen60E0fo12_0V-jFCrq202tqvVzBjeNntvOOWj0AxgXWVxWfNdBVGZOYM_7KDsHxDipw0aNAKi0faBoavZBDIwy4UHumRpXdxxamZcOH3ozH6QLPaA3uoRzA3biKzC7ODZwrjDhxxHcr56J1v5rDb5tYA0xPjtVuMediGuRvIripjsEafEujnompKIseuEUGN4hC-_2BpZUXyjWX4cpv0c73YPZ-dw-T8JWbhMZNuukePQDzF5xU1Lol5VFVSOfYIgzI7UTN4XCVg4z0oBGFwOfvJ3sGgT-i5Z3pMyEO-5Icw8WICCms8Pnmy_XtRqKu4V7kOu7toi0wo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام امريكي: المنفذ ليس واحد بل عدة مسلحين</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/87835" target="_blank">📅 16:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87834">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxSwK-rYwOBgjBfnvQe-93nAiL6EM6jQaXszOzFrNi3gzTKht5w9jopn0IZ1Q-AJgnLFZdiDPRk8tVc8EXCzDifoL4hH5ufbyvHgD4kPEHuHeDMstu6SAaU--5zWNOCNTKwHN3phdsJQrLnCapSFc__qiSSALAbKXEMfcBTlcxr0lf0tZGE_obVw0BEvYtDQ-B_SusbryA8v4GQHLhrfOzP89iLM3skj12eZXhXsI6yt6w5TRuOnSvE7MDqHyRB5E1ytEBWk44LktsPSNqc9o0BWdNzGyUk0mqWYFMe9ouW5zo3-CZTUawJcc1HYZCsxfxkQP-vHkktIjOLvFFLmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مصادر لنايا
شبكة الإعلام العراقي بصدد انتاج الجزء الثاني عن تسليم السلاح لكن شخصية حميد ستصبح كاكا حمه في اشارة لسلاح مليشيات البيشمرگة ..</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/87834" target="_blank">📅 16:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87833">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اغلاق جامعة ولاية فرجينيا بعد الهجوم المسلح</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/87833" target="_blank">📅 16:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87832">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اطلاق نار داخل جامعة فرجينيا ومقتل واصابة عدة اشخاص كحصيلة اولية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/87832" target="_blank">📅 16:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87831">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حدث امني في ولاية فرجينيا الأميركية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/87831" target="_blank">📅 16:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87830">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حدث امني في ولاية فرجينيا الأميركية</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/87830" target="_blank">📅 16:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87829">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
بيان صادر عن حزب الله:
استيقظ اللبنانيون فجر اليوم على وقع تصعيد عدواني ومجزرة وحشية ارتكبها العدو الصهيوني المجرم بحق المدنيين الآمنين في الجنوب، من خلال استهداف منزل في أطراف بلدة أنصار الجنوبية ومبنى في دير الزهراني، ما أدى إلى ارتقاء إحدى عشر شهيدًا من بينهم أطفال ونساء وسقوط اثني عشر جريحًا، في جريمة موصوفة تضاف إلى سجل العدو الحافل بالمجازر والجرائم وسفك دماء اللبنانيين وتفجير منازلهم وجرف حقولهم ومحو معالم قراهم.
إن هذا التصعيد الإسرائيلي، باستهداف المدنيين وتوسيع دائرة المناطق المستهدفة، يعبر عن رغبة وإرادة رئيس وزراء العدو المجرم نتنياهو  بتصعيد الحرب تعزيزاً لواقعه السياسي الداخلي، وخدمة لأهدافه الانتخابية وإرضاءً لليمين المتطرف. وإن هذا التمادي في العدوان وانتهاك سيادة لبنان تتحمل مسؤوليته حكومة العدو  والولايات المتحدة التي تؤمن الدعم والغطاء لها، فيما يجب على  السلطة اللبنانية أن تبحث عن السبل المتاحة لوقف هذا العدوان وأن لا تصر على الاستمرار في مسار المفاوضات المباشرة المذلة وتقديم الهدايا المجانية للعدو، رغم كل ما يرتكبه من جرائم واعتداءات، وما يعلنه من نوايا عدوانية وتوسعية تجاه لبنان.
لقد آن للسلطة أن تراجع حساباتها مراجعة شاملة بما يحفظ سيادة لبنان وحقوقه، بدل الاستمرار في سياسات تأكّد عجزها عن حماية لبنان وشعبه، وأن تقف موقفًا وطنيًا وشجاعًا ومسؤولًا، وأن تتوقف عن اللهاث خلف المفاوضات التي يجرّها إليها الأميركي، وأن تدرك أن الرهان على الضمانة والوساطة الأميركية هو رهان خائب، فالأميركي شريك للعدو الإسرائيلي في جرائمه ومجازره بحق لبنان. وما التصريح الأخير والوقح والابتزازي للسفير الأميركي في لبنان الذي دعا فيه إلى تسليم سلاح المقاومة، فيما المطلوب منه أن يضغط على العدو الإسرائيلي للانسحاب من المناطق التي يحتلها، إلا تأكيد على أن ما يبحث عنه الأميركي هو مصلحة العدو الإسرائيلي وأمنه على حساب سيادة لبنان وشعبه.
إن على اللبنانيين جميعًا، بكل مكوناتهم، أن يدركوا خطورة النهج الذي تنتهجه هذه السلطة على لبنان ووحدته وأمنه واستقلاله. وإن على العدو الإسرائيلي أن يفهم جيدًا أن اعتداءاته وتجاوزاته ومحاولاته فرض أمر واقع لا يمكن أن تستمر، وستقابل بما يناسبها، دفاعًا عن لبنان وشعبه وسيادته وكرامته الوطنية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/87829" target="_blank">📅 16:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87828">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX78VDFaS_hykjcjZNBdZJ2Ri62S2Eq7M08ubXLLMVed_Dz4HkUI95jzSxqUneGd6aYc8vpWJr5PpMTI5pKl6a_We-_7vfQpM1dEbOQKYS7P29ggA1Xq0vmuUP2KAWCVYoEMsf7y5fe3jztHy3e5aXoLSsCTYJnrxpneGhqN_5uPiXQkGRuURTtKiFMeAnuc7-yL7qStquYaszFeqpHFrTC77TM2ctrC1TAOOKWJbMKaLxs_jRDUd_PpSlsMwxajeW0AGas67fD7jhdICHN7AVUl-Hpp18wYxsx4z0rFzdkJYvlvkdCElpv7NoIfRW7Y4Vr2-5vq1mOBaf78f6-tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشوراء الفرقة الخاصة
نار على أعداء العراق</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/87828" target="_blank">📅 15:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87827">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87827" target="_blank">📅 15:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87826">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLQzhhAV-7LULPFn97kq2S8qcs8gyyP9w23aKOSc-7tFvJ_iX7a_afFA8hcf6cJPOvhJmZXTcug1XdDy3bz-ePBdpK9038zz1X-NZ_DU1pe4Hzn7Gwz7ZtfJh6uNwLCuCWyqgDOWtTns0J_gSfBoy5TuzMSd8TdFpifyIHl07TKuCa5lxKlxYQ63_BFvO6jBnWglAkcVbDgtcBGavYPh4mQIR7mRfWGdG1hFcJ1op1g_gcI_2QbJu0h_TaVkuOl2bLM2Xz0jHeY_hsxpv-I-_PbPhoZ0Zc8p-lDKMYwAuht95OpVWW9JYcbvgiQI0DZdsdGX8bP2wBW1C16i4MfI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لولا دماء بلال الوحيلي و شيخ ياسر عاتي الكعبي
لكانت الجرف الان ولاية ارهابية داعشية سلفية ..
شكرا حميد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87826" target="_blank">📅 15:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87825">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏قصف مدفعي متبادل بين مرتزقة السعودية وانصار الله على جبهة كرش شمالي لحج</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/87825" target="_blank">📅 15:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87824">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زلزال بقوة 6.9 درجة يضرب إندونيسيا، وهو الثاني في يوم واحد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87824" target="_blank">📅 14:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87823">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
الامريكيين ينتجون فيديوهات دعائية بعد ساعات من تداول اخبار عن تعطل مراحيض حاملة الطائرات الأمريكية "لينكولن" واضطرار البحارة للسير في مياه الصرف الصحي على متنها وكيف كانوا يحصلون على طعام رديء. كل هذا دفع البعض إلى القفز من السفينة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/87823" target="_blank">📅 14:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87822">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">السفير التركي في سوريا: اردوغان مغرم بدمشق وسيزور سوريا نهاية العام ومتشوق للصلاة في الجامع الأموي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87822" target="_blank">📅 14:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87821">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
الحشد الشعبي جزء من القوات المسلحة وحصر السلاح يشمل الجهات غير المرتبطة بالمؤسسات الأمنية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/87821" target="_blank">📅 14:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87820">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: تمكنت القوات المسلحة _بفضل الله_ من استهداف تحشيدات وأسلحة تابعة  للعدو السعودي وزوارق حربية تابعة لأدواته ومرتزقته في منطقة المخا، وذلك بعدد كبير من الصواريخ  البالستية وكانت الإصابة دقيقة بفضل الله وقد أدت العملية إلى تدمير الزوارق…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87820" target="_blank">📅 13:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87819">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roeWsZJkOEJbka4BS0DyCohzhQiVvHlXyRVSFBaPp3mQ6qnV-z-oHK-t76O9CuhdWxqTtmdQd9zpf-IIwt3JfPA-koy2MffcPP021ZgYhT9XWbTPO5n1FaLyts23MKPzkyRMnIIGCTyKzzlN0ya3tFBoEA601JYoNnLZA8JBKDCekLn1e9gW4GZPIu9iOI39xKntEcgJOJKcMEqaOqeAaHkixh8IuhvWPxotoXmXeALDRzEdrNbhU4L8qwZ4hAuJZYylEaBHX1wZ0ddX-NXcF1uGk1_kE1-burln_3sUin6NmnXyLpqj8Lksr05bT1GXKbsHHIs-a_3WCG0ICj2I-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مراقبون لنايا
تحويل الإعلام الرسمي إلى منصة تهديد ليس هيبة دولة بل عبث بالسلم الأهلي .. إذا كان المطلوب تطبيق القانون، فليُطبّق بالقانون لا بالوعيد من شاشة الدولة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87819" target="_blank">📅 12:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87818">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8hPak1GSsYCv9M_BVLGnFF7YbJiIrE7A3YPNKoKw8j4vPDFBbNBIoHG8I8-dt-9Umm12IiZ82JWAD8vFtNkj03E2GTv-NGeB29CxyewtrYyjQpMWP81HP4GyoW-G13er9sH-pJZafD0hjRQU3bqd1FpMlnSbvPqN0tno6BU7tgjqGM03f2I1YWw6Yf2BXgIoQo2M6J_Tobv9-LAVSiLg1M1bdtHv5onZjxYkDqm_0rXk7y00lNhGVvc7EoyTp01A0IAQGcwzjp515LmCD2V2X5Opg9Whewzk1GNdAZqovBv6RKYHqsMkmerezWXuLjHnbEhSh4x0WxJ1TIBJBjH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
🇮🇱
إلى أنظار جوزف عون و نواف سلام..
عائلة كاملة إرتقت فجر اليوم جراء عدوان صهيوني غاشم على بلدة أنصار جنوبي لبنان.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87818" target="_blank">📅 12:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87817">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4aa482a54.mp4?token=BgYvonnUsvgqmneqiQTzDB_wuseEWlvIpqkfADI-Hziumcto6KahfLxIQPvI8kj0AuN4TNuKNGJqExtJpDDzU8fjV4FirfyVAMtKIXzVc0WnU19TLJ00xHc5DP95_PVLixAw6Acefly9AdNXUWXYwMal5cno66tL9XcYyjWdxR88H-O4lskl4hR4GKFGgDDGAnfEMO7DfKQC8LWDn_PUjew_m1L_P0lNdcHkPe3KP8KVP661GN_VuFg7yhCKSS_0VFDG0yPki5MqxcEkLlULHawJGBPvPMouy-VS-32gsoLLqAMLiUoAxLs9UbeZE6j63iF0tyfqYlqpufDpXTOj_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4aa482a54.mp4?token=BgYvonnUsvgqmneqiQTzDB_wuseEWlvIpqkfADI-Hziumcto6KahfLxIQPvI8kj0AuN4TNuKNGJqExtJpDDzU8fjV4FirfyVAMtKIXzVc0WnU19TLJ00xHc5DP95_PVLixAw6Acefly9AdNXUWXYwMal5cno66tL9XcYyjWdxR88H-O4lskl4hR4GKFGgDDGAnfEMO7DfKQC8LWDn_PUjew_m1L_P0lNdcHkPe3KP8KVP661GN_VuFg7yhCKSS_0VFDG0yPki5MqxcEkLlULHawJGBPvPMouy-VS-32gsoLLqAMLiUoAxLs9UbeZE6j63iF0tyfqYlqpufDpXTOj_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇱
إرتقاء شهداء وعدة إصابات جراء غارة وحشية من الطيران الصهيوني على منطقة مأهولة بالسكان في بلدة دير الزهراني جنوبي لبنان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87817" target="_blank">📅 12:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87815">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
رئيس السلطة القضائية الإيرانية:
لقد أثبتنا لترامب وتابعيه في الساحة العسكرية أن مضيق هرمز جزء لا يتجزأ من المياه الإقليمية والحدود الإيرانية، وأن أي مغامرة فيه ستقضي على أي قوة متجاوزة ومغامرة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87815" target="_blank">📅 11:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87814">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عدوان سعودي على محافظة صعدة اليمنية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87814" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87813">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7000ddea94.mp4?token=qgISVfznDhSNWgORKjYiY55-G2cjsnHPGlAlAKhmV6I5RhIgtdEZWNYTpGAx5yFAq6-As0gtyIzEp_sFzQDDWSlBYj5g-H0GwDlj_gk_gLJWEHJ7q0aeGT6Lhz5N_Xy_6YWL--ZazBC2ScLiUAjZNt_2xKTNJB_zs6oSIQ0QMzvYX3_BRCcYWc6gutwjbjWks2FVvYaSsAgGzFTmRU8XqKW99Rt4caIMtcYWAIFHau9LbDUv3kmm4tU3t330W_DbzJ9LjNEOPy586J-IX6BhGLRYl06JwQQwyF4yuERk7c5K1YRHXac2FG78G0bcZmBsooIiw7M2t_GSA3NzSmFr_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7000ddea94.mp4?token=qgISVfznDhSNWgORKjYiY55-G2cjsnHPGlAlAKhmV6I5RhIgtdEZWNYTpGAx5yFAq6-As0gtyIzEp_sFzQDDWSlBYj5g-H0GwDlj_gk_gLJWEHJ7q0aeGT6Lhz5N_Xy_6YWL--ZazBC2ScLiUAjZNt_2xKTNJB_zs6oSIQ0QMzvYX3_BRCcYWc6gutwjbjWks2FVvYaSsAgGzFTmRU8XqKW99Rt4caIMtcYWAIFHau9LbDUv3kmm4tU3t330W_DbzJ9LjNEOPy586J-IX6BhGLRYl06JwQQwyF4yuERk7c5K1YRHXac2FG78G0bcZmBsooIiw7M2t_GSA3NzSmFr_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مروحي يحلق بإستمرار في سماء محافظتي أربيل والسليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87813" target="_blank">📅 10:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87812">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نيويورك تايمز:
هاجمت إيران في بداية الحرب القاعدة البحرية الأمريكية في البحرين، مما أدى إلى تعطيل مركز لوجستي رئيسي، وأجبر البحرية الأمريكية على الحصول على الإمدادات من جزيرة دييغو غارسيا، التي تبعد حوالي 3500 كيلومتر عن حاملات الطائرات العاملة بالقرب من إيران.
ساهمت مسار الإمداد الأطول في حدوث نقص وضغوط على متن السفينة الحربية الأمريكية "أبراهام لينكولن"، حيث قضى طاقمها المكون من 5000 بحار ما يقرب من تسعة أشهر في البحر دون توقف في أي ميناء.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87812" target="_blank">📅 10:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87811">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
🇺🇸
القناة الحكومية العراقية تهدد فصائل المقاومة العراقية   نشرت قناة العراقية الممولة من الحكومة العراقية فديو دعائي لاول مرة منذ عام ٢٠٠٣ تضمن لغة تهديد للفصائل المسلحة بالتزامن مع نهاية المهلة التي اطلقها توم بارك بخروج المزعوم للقوات الأميركية في العراق…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87811" target="_blank">📅 10:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7bBAzbXPZP2KluweEdb1_DYFpApUY0XWB-73kmMdsAr1ARwf1lfaBxH3G2EDKJSdkK_bfkxBEeqXZIb2j-kAR7-j_ZmJPSbjcw4lVfPMKMDCs8vjeLsfF2kv3dMRfa3TOvGHBJ-Jx4Qtj4hV-TLsqCqskjx0TEr1rFbiSyXABxJY_V3xZn5v0yfmF0TTydfZfSZatdDE_C1diJIdStoRGgPy2RVZOZDDqm_0IDzYl8z4CG9sTj2eHomUbcI5EHkl-98FS0pj8N-NkWH_rHcP8PT6iuXoijMovk8aDMhEAMx1CwxJ9qVjbE-7SG1adYP3F9e0ZKTG1ZXRmxAwpLrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
القناة الحكومية العراقية تهدد فصائل المقاومة العراقية
نشرت قناة العراقية الممولة من الحكومة العراقية فديو دعائي لاول مرة منذ عام ٢٠٠٣ تضمن لغة تهديد للفصائل المسلحة بالتزامن مع نهاية المهلة التي اطلقها توم بارك بخروج المزعوم للقوات الأميركية في العراق ومهلة الحكومة العراقية ايضا للفصائل بنزع السلاح ؛ المضحك ان القناة الحكومية استخدمت في الفديو طائرة MG 29 الروسية والتي تخضع للعقوبات وتفرض امريكا على العراق قرار بعدم اعادة تأهليها مع ٣٥٠ طائرة اخرى روسية الصنع تحولت لكتلة حديد بمطار التاجي بسبب الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87810" target="_blank">📅 10:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hel6MBFM8WUx2yi9he7Qq2iyM6-l_OpYNzxIIkrRjY2GV0zF0KtzN_06YvYEmMB6b9KEAThuKTLmS6zA7PXV4aPKXy8qwbxpnUinKT6KrM6jxdt7HVifal5fBzPs4guW38L9j8pV_dlsbZkzCSjPTPuky4UqjprHIu8jJDl3HE9-5ESPvrGturSMQ3FzzrBuYVXyUsSRui_k7LGjlfEtmgH_4A4tIRBJ19p14tGHDDEGTUw0F3E_JwMzfyxoJpYiJZX9YkT8_58nBkuMP8k1xoKf_uSSSiP119plgqrBu0zt-N2NS9FtO8rFvG2QpdovZYQo1Kaa6yNA3xU4bhyuSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87809" target="_blank">📅 09:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87808">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87808" target="_blank">📅 09:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87807">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
القائم بأعمال وزير البحرية الأمريكي:
عالجنا عددا من حالات الصحة النفسية على الحاملة لينكولن.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87807" target="_blank">📅 01:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579ffff276.mp4?token=KJIe7CQ8dWLBQORKgv4u8s9ezrp8Oz-1-zPdzLzQIkpbNf0tgyR0YrwftZy0Trlzf7CmouUZd6HkjCcSa5gG7nwpujg7ZU9A54GekYL5hcJwPGwKfVBJ3nW9rPk_TlPUL9NWSqfMGok1l6_P-8_8-NKlhjqIrkwnsHbgn_a9nFhDQDM3a2qWUYN9G3c0Dx4Fy3ZFTAGmp-UlH1PmKHnZJ6zLbXndL2jDbPT_vZDzjUAtE0LbAveh8aIyxCfxu3aNz_bgqX8c85cWwxYzssEPmYdlgJPYpHSyJXL_gbgcejG3LMTjKjGt_gSSjfYI-YJvMFC1fMa7svkc0GVr06POXQAHWq4NSYgLLCm8KQtdCaiptWqY9DCM43N12Pt1aor1Xo7V27MesxRpUJuiDXKzd8bMJKdX5P7zfuZ2igMCyT0a177fqTunidEVBsrTUQ_k5Ms2ei6LvWXF7QIKXdBuAprQrPN2yH3DJDjOgEmcjh07yOEy3HlqZkAejtQdkQqofxLDiS1ghJCNlxWnX2gmqhycDQWVJoadbU_9T9E7v0YXeMWf6mMiqU2ffwkb_TZiDfNAH8JYHUqO18DCWLQb-U2KUkjtOTj_5OgURJZkullTnGNPw1wM-VQ3v4sibB1lFSm7gobPb_OEd5yQ3hKAsT8PJRHSYCWV-QPMPz8RUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579ffff276.mp4?token=KJIe7CQ8dWLBQORKgv4u8s9ezrp8Oz-1-zPdzLzQIkpbNf0tgyR0YrwftZy0Trlzf7CmouUZd6HkjCcSa5gG7nwpujg7ZU9A54GekYL5hcJwPGwKfVBJ3nW9rPk_TlPUL9NWSqfMGok1l6_P-8_8-NKlhjqIrkwnsHbgn_a9nFhDQDM3a2qWUYN9G3c0Dx4Fy3ZFTAGmp-UlH1PmKHnZJ6zLbXndL2jDbPT_vZDzjUAtE0LbAveh8aIyxCfxu3aNz_bgqX8c85cWwxYzssEPmYdlgJPYpHSyJXL_gbgcejG3LMTjKjGt_gSSjfYI-YJvMFC1fMa7svkc0GVr06POXQAHWq4NSYgLLCm8KQtdCaiptWqY9DCM43N12Pt1aor1Xo7V27MesxRpUJuiDXKzd8bMJKdX5P7zfuZ2igMCyT0a177fqTunidEVBsrTUQ_k5Ms2ei6LvWXF7QIKXdBuAprQrPN2yH3DJDjOgEmcjh07yOEy3HlqZkAejtQdkQqofxLDiS1ghJCNlxWnX2gmqhycDQWVJoadbU_9T9E7v0YXeMWf6mMiqU2ffwkb_TZiDfNAH8JYHUqO18DCWLQb-U2KUkjtOTj_5OgURJZkullTnGNPw1wM-VQ3v4sibB1lFSm7gobPb_OEd5yQ3hKAsT8PJRHSYCWV-QPMPz8RUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن إيران: كان لديهم 212 طائرة جميلة جدًا، بعضها تم شراؤها من الولايات المتحدة، وبشكل ذكي، في عهد أوباما. جميع طائراتهم اختفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/87806" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6da41714.mp4?token=Ir8aYFuQcGALrA33RPLnx42v25xDiKtBSVwVEkG7GnG_Fd4WAFJrcrOlm5UT1kilCb_hxCjAQvRKeWirB5_xHa46uh10H-VWBP9Hdwcy_4mDPxapiDI1HHVoEyN66bXGb4aSgBAYrblqVziU3mQbcS38xdZcm5MDoOVD_o53xdxw4PqB2KoXIbDGyKYIXnowJti9GFktIa0dEHHxgDLMyr7Cfbeh85Voyx8c4W20ayy0vuFTrtL-xs7LecVh-S7QxvLlurs_KV6AWk6Z-9PNTrrmZplLUn8UoBTeM_D3-NSeCl-Fm1XUSmOpPuqto3e9gc4lJVNSJOcov6PlEAYo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6da41714.mp4?token=Ir8aYFuQcGALrA33RPLnx42v25xDiKtBSVwVEkG7GnG_Fd4WAFJrcrOlm5UT1kilCb_hxCjAQvRKeWirB5_xHa46uh10H-VWBP9Hdwcy_4mDPxapiDI1HHVoEyN66bXGb4aSgBAYrblqVziU3mQbcS38xdZcm5MDoOVD_o53xdxw4PqB2KoXIbDGyKYIXnowJti9GFktIa0dEHHxgDLMyr7Cfbeh85Voyx8c4W20ayy0vuFTrtL-xs7LecVh-S7QxvLlurs_KV6AWk6Z-9PNTrrmZplLUn8UoBTeM_D3-NSeCl-Fm1XUSmOpPuqto3e9gc4lJVNSJOcov6PlEAYo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/87805" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
الوضع بين الولايات المتحدة وإيران مستقر.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87804" target="_blank">📅 23:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87803">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87803" target="_blank">📅 23:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87802">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba96a06df0.mp4?token=M5P0fRWwEq80Qozd77taeeIbJWQbfnlXAu-CLm0zBBWOkV73FDHqB1fYKDX8hlk_0D8gW9LYJuhpLr94-JuqRiAzmvRFkwpQMsgMAmmSP8vnxxlQUVRNY1nHj_B91vi3L6cvpBttjVcFK_xdcZo4QnARBjTozC-gmaFTWdAh_TcUIQrZN5tssEeEYp7CvmNnrLp8AM7eD0veYlVD8nL1Z3dp2LKDSkDuSfIXXlsIeklz4qiV7qQYNzCdSxaI7lQ5xZgCnlNgvSiySdtVUzXrsoambaUInzfGxvIkjpqhDXBwJI7WZF3TG0SH1_s0L2rJohGOhUlB80Y1ENpfBkjz5DCliryMjwLImi9a_nycHOr2m2-7N98SioGVAYhFQqGyitgOFPFY0GULQuuzR-pH65nRnDq7zIaEE6iTC6t_jGzu0-MyB8M_M37wt1GeCe1wUwlPh7VByc5rmDlpNKWx85mN-79Prlz_f-54S12Gudjv7shaSeSW6HbLDXCAD6ADUQrWts2CChEIabPboAAClETGE5QWo9WfIxZRf_p3Qwjzg0NZ7fiAPBVESjPjxWcxXFzGaBtPB5qIqA6I3RT6pWghvaERJwOyuc95d1oQw5euuWiT-4wzfO5mNQYT4PSTz6_EgPdlF46SVMfRvSGxG-O0xrLrgKfVy0EJhbThWY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba96a06df0.mp4?token=M5P0fRWwEq80Qozd77taeeIbJWQbfnlXAu-CLm0zBBWOkV73FDHqB1fYKDX8hlk_0D8gW9LYJuhpLr94-JuqRiAzmvRFkwpQMsgMAmmSP8vnxxlQUVRNY1nHj_B91vi3L6cvpBttjVcFK_xdcZo4QnARBjTozC-gmaFTWdAh_TcUIQrZN5tssEeEYp7CvmNnrLp8AM7eD0veYlVD8nL1Z3dp2LKDSkDuSfIXXlsIeklz4qiV7qQYNzCdSxaI7lQ5xZgCnlNgvSiySdtVUzXrsoambaUInzfGxvIkjpqhDXBwJI7WZF3TG0SH1_s0L2rJohGOhUlB80Y1ENpfBkjz5DCliryMjwLImi9a_nycHOr2m2-7N98SioGVAYhFQqGyitgOFPFY0GULQuuzR-pH65nRnDq7zIaEE6iTC6t_jGzu0-MyB8M_M37wt1GeCe1wUwlPh7VByc5rmDlpNKWx85mN-79Prlz_f-54S12Gudjv7shaSeSW6HbLDXCAD6ADUQrWts2CChEIabPboAAClETGE5QWo9WfIxZRf_p3Qwjzg0NZ7fiAPBVESjPjxWcxXFzGaBtPB5qIqA6I3RT6pWghvaERJwOyuc95d1oQw5euuWiT-4wzfO5mNQYT4PSTz6_EgPdlF46SVMfRvSGxG-O0xrLrgKfVy0EJhbThWY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران
: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87802" target="_blank">📅 23:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87801">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ca3fdb17.mp4?token=ByLDQH-oVP57z6EK_GT4DEz81mSh9sI9XNAEtpKLK1R1rsaHLHBvYrw8q-seBqNf3m-iln-HquKvmKESRKQL2HzENtD3SGpX8IpHjS_dTvojz0ddUGfzbbL3ytet_voIXz8AYnEe7Ai14S1Jc5hd6EpTQsJXB53FpZmZbwUoebaGcC3Svvg_2CIN17Im9Kcjl5-kTMZVusuPpGgxw-VgHKEdED9P8ElgqBtbahwM77LDER8KVFpDxffAauxsp1NN7ycCxK1EackpcdGEpa0K0QDg4LKm_qa0Ie4vcctsc7KNFAxSar4jZwYhAUFpJTiqO8D09aD6xJanKhX18qaCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ca3fdb17.mp4?token=ByLDQH-oVP57z6EK_GT4DEz81mSh9sI9XNAEtpKLK1R1rsaHLHBvYrw8q-seBqNf3m-iln-HquKvmKESRKQL2HzENtD3SGpX8IpHjS_dTvojz0ddUGfzbbL3ytet_voIXz8AYnEe7Ai14S1Jc5hd6EpTQsJXB53FpZmZbwUoebaGcC3Svvg_2CIN17Im9Kcjl5-kTMZVusuPpGgxw-VgHKEdED9P8ElgqBtbahwM77LDER8KVFpDxffAauxsp1NN7ycCxK1EackpcdGEpa0K0QDg4LKm_qa0Ie4vcctsc7KNFAxSar4jZwYhAUFpJTiqO8D09aD6xJanKhX18qaCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
We are the king of Hormuz</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87801" target="_blank">📅 23:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87800">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
ترامب
: سأضرب إيران اقتصادياً بقوة .</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87800" target="_blank">📅 22:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87799">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
مشاهد من احتراق السفينتين في المخا، بعدما تم استهدافهما من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87799" target="_blank">📅 22:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601d104f1.mp4?token=TW-cIjnES-WRqckaY5LCAbrkuNxh5e1F5Bec4DeTDaEpFJNlnRbqO1Brp-uOiegSm_c4Xcc3RKT21g5hFulQwOnn9p4ie_5oon9SzXleKxcZQwfD9t7z1CojDeyEOr4UhDQecQMdEc6EIaJJ_Lp6_h55CH0uCf0bZUh2obj10encC6R1InsuIcqVwJVhTLjFarcfF79riXxAytXhq3iiTqyW0eb3xa6tRLO3-2gMk1k6W7k7xLwo-VCs5em3fk-mAXzDvPldJ1IXf4eupFKwBLusysB33TB3N6gBTeb-a7_ne9JZnkGDTpIICJK7XsZCM4FHwga3kI009cKbUBU5kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601d104f1.mp4?token=TW-cIjnES-WRqckaY5LCAbrkuNxh5e1F5Bec4DeTDaEpFJNlnRbqO1Brp-uOiegSm_c4Xcc3RKT21g5hFulQwOnn9p4ie_5oon9SzXleKxcZQwfD9t7z1CojDeyEOr4UhDQecQMdEc6EIaJJ_Lp6_h55CH0uCf0bZUh2obj10encC6R1InsuIcqVwJVhTLjFarcfF79riXxAytXhq3iiTqyW0eb3xa6tRLO3-2gMk1k6W7k7xLwo-VCs5em3fk-mAXzDvPldJ1IXf4eupFKwBLusysB33TB3N6gBTeb-a7_ne9JZnkGDTpIICJK7XsZCM4FHwga3kI009cKbUBU5kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية استهدفت سفينتين كانتا راسيتين في ميناء المخا.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87798" target="_blank">📅 22:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تستهدف ميناء المخا من جديد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87797" target="_blank">📅 21:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87796">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789a1d80f8.mp4?token=odC9ljotd-h_xOobshBiqGS8kPmqWPfvEf-WOlDEKBm1FGVGPRzEUM3sD7DucjzF5BbvZvn0zeghwVAdXeVCED0CfdCvurXkjTke57LJ7GUUJCTvY4aZaVF35BFHIoTb7ng_SqJeb6IWH5yipD7XJuvwu0xaFhlPuDfFzlC_GDqO136wpNLvQkpuZfW_aa5Aq-wo5qwwU-4KKS_4Klhl4rUmA6xlr7TVSy8GnGDdcE9Hj_epvMimV_I1IRwm-Q9aUAJ39S0uFWBO8xYPGqZQOyJdOxu2Ug87ebGOHVpvhYOwEpVU2xpvxHttr6cR8ZKmdfZaj5sbA2CjIDQChjmsMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789a1d80f8.mp4?token=odC9ljotd-h_xOobshBiqGS8kPmqWPfvEf-WOlDEKBm1FGVGPRzEUM3sD7DucjzF5BbvZvn0zeghwVAdXeVCED0CfdCvurXkjTke57LJ7GUUJCTvY4aZaVF35BFHIoTb7ng_SqJeb6IWH5yipD7XJuvwu0xaFhlPuDfFzlC_GDqO136wpNLvQkpuZfW_aa5Aq-wo5qwwU-4KKS_4Klhl4rUmA6xlr7TVSy8GnGDdcE9Hj_epvMimV_I1IRwm-Q9aUAJ39S0uFWBO8xYPGqZQOyJdOxu2Ug87ebGOHVpvhYOwEpVU2xpvxHttr6cR8ZKmdfZaj5sbA2CjIDQChjmsMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل
: أفراد عائلات أفراد الخدمة العسكريين قلقون بشأن الظروف على متن السفينة الحربية "لينكولن".
ترامب
: لا، هم ليسوا قلقين.
المراسل
: هل استمرت مهمة الانتشار لفترة طويلة جدًا؟
ترامب
: لا. لا. لا. لم تكن طويلة بما يكفي على الإطلاق.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87796" target="_blank">📅 20:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
انصار الله اطلقو خمسة صواريخ  على ميناء المخا.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87795" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87794">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇱
الاعلام العبري
: أميركا وضعت فيتو على طلب إسرائيلي بقصف أهداف في سوريا.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87794" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87793">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
انصار الله اطلقو خمسة صواريخ  على ميناء المخا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87793" target="_blank">📅 20:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87792">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇾🇪
مشاهد جديدة لميناء المخا وهو يشتعل بفعل الصواريخ انصار الله.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87792" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87791">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1341d9e0.mp4?token=r85eFjenPPODnFQ1Pl5fzYFSZO2QD169bT0jEHKf5Irx9kJsEAhEHawHz_tdIGnsOt-mP6y6UvXJ0eNHpfHYQw3JPYiGf63iQP3aDI79uAVmXVhxEtvtDyJE09Z3yz7HfIHY3YxfoJs2j4W-B9siBGogTTgivwsy_7_8yetCtPdZjQghZdqtsWT_JnU6rSkmC1iPdVSxgy63UHyWnYw4S8T4zye0wXdqdvJ__Ff8yYv5Y6wcoP3uE4BXepdwvnBGWkTbEpIFPxGhzEkUhnvUWteBuNZ83x5BwMrDaywIkLMeNws83rwVCkC28jXu5VYxs4SzDRE3KCl7yra3E66f1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1341d9e0.mp4?token=r85eFjenPPODnFQ1Pl5fzYFSZO2QD169bT0jEHKf5Irx9kJsEAhEHawHz_tdIGnsOt-mP6y6UvXJ0eNHpfHYQw3JPYiGf63iQP3aDI79uAVmXVhxEtvtDyJE09Z3yz7HfIHY3YxfoJs2j4W-B9siBGogTTgivwsy_7_8yetCtPdZjQghZdqtsWT_JnU6rSkmC1iPdVSxgy63UHyWnYw4S8T4zye0wXdqdvJ__Ff8yYv5Y6wcoP3uE4BXepdwvnBGWkTbEpIFPxGhzEkUhnvUWteBuNZ83x5BwMrDaywIkLMeNws83rwVCkC28jXu5VYxs4SzDRE3KCl7yra3E66f1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
قصف صاروخي من انصار الله جديد يستهدف ميناء المخا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87791" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87790">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
استهداف مباشر لميناء المخا معقل تمركز العصابات المنفلتة الغير شرعية في اليمن .</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87790" target="_blank">📅 20:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87789">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefbba7708.mp4?token=XZge0-vf2XOxxUUZSMcGVKfncYrHdu8t5tHft7ue7-lJWZ9Xz0JIuPbhXGmiE5mctRpvaNGsPfslXVrFTKw84R9ZAx9cip1ujXXdGuJJ3D0beMKmB05_w7NNzB6rYch1mFDcuFV2oih1lzlsD-kepsTHaqGwarIgUJ4rXRRWLZkSJbi0-pXqFh1axITwA091Ipb9fIbJjLxeWYfFa3EcGYBc3Vvyc0CuNFAiCCktVpot0Rad4U7pDvZCoQt3Gcf_a-kkPlz3gOQ4dBvvF62_TOW4VBNNsoZ7uhXCnoBf3K5_3TPIgiZMRc_eKseI_rt3Ac8fnAcRWbiOLaHOuS2qpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefbba7708.mp4?token=XZge0-vf2XOxxUUZSMcGVKfncYrHdu8t5tHft7ue7-lJWZ9Xz0JIuPbhXGmiE5mctRpvaNGsPfslXVrFTKw84R9ZAx9cip1ujXXdGuJJ3D0beMKmB05_w7NNzB6rYch1mFDcuFV2oih1lzlsD-kepsTHaqGwarIgUJ4rXRRWLZkSJbi0-pXqFh1axITwA091Ipb9fIbJjLxeWYfFa3EcGYBc3Vvyc0CuNFAiCCktVpot0Rad4U7pDvZCoQt3Gcf_a-kkPlz3gOQ4dBvvF62_TOW4VBNNsoZ7uhXCnoBf3K5_3TPIgiZMRc_eKseI_rt3Ac8fnAcRWbiOLaHOuS2qpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
استهداف مباشر لميناء المخا معقل تمركز العصابات المنفلتة الغير شرعية في اليمن .</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87789" target="_blank">📅 19:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87788">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الشيخ نعيم قاسم:  - من يراهن على الاستسلام إنما يراهن على سراب ولا يعرف المقاومة جيداً بأنها تتحمل وتصبر هي وأهل المقاومة  - اتفاق الإطار الذي ذهبت إليه السلطة اللبنانية ليس لا اتفاقاً ولا إطاراً  - اتفاق الإطار هو إملاءات إسرائيلية بالحبر الإسرائيلي تُوقّع…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87788" target="_blank">📅 19:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87787">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
كلمة مرتقبة للأمين العام لحزب الله الشيخ نعيم قاسم اليوم الجمعة عند الساعة 18:30 بمناسبة ذكرى الانتصار يتناول فيها آخر التطورات.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87787" target="_blank">📅 19:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87786">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0egojGrW-GVO-DRRk5IwbqHmHrKPISlZREk02IeY3JQKvi2811lTfHJ7jPeZIQNCvDhQUTfqZj1-pyLDkntIwsp8geYG78T8k6kilMusGGf_0TjoXU_6W6pjWDStdTooKgXhOHBIng5GAu1mA7UovEtALfr9tecCA9hQg3flNL1GGUhHrB8Z4AH0Ny4YmBybq4_XbXgfrV4t0Kz8a7VHT8REpieLg7Fg-OolKtoRs4Z14n0B_T6wE_kTohno_4v67UFLtOTZwA1rEbdWNPLPwhi3Bfczi7J6-ozFhlsvxDTli9OFOPaR1CW9N0Y1ZlK3mWZs8Uqk8MRxZPSPjkJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇾🇪
وزارة الخارجية العراقية تلتقي ما يسمى بـ"السفير اليمني" التابع لمرتزقة السعودية وتعرب عن تضامن العراق مع الشعب اليمني خصوصاً في ظل تصاعد الأحداث بين أطراف النزاع وما نجم عنها من خسائر بشرية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87786" target="_blank">📅 19:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87785">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
الاستخبارات العراقية تلقي القبض على (23) أجنبياً حاولوا الدخول بصورة غير قانونية إلى البلاد عبر المياه الاقليمية العراقية وباستخدام الزوارق البحرية السريعة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87785" target="_blank">📅 18:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87784">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mitDMLH7kBcNZHqcX6vD76tSuvEn2yyko7Ol7yjixnM6PuHUXwtAVtF8dAcTggAsGdwrXXUW1yzL0pJddy2oOYcz9Fn-Z9FTRrXs-y2KPg62GxDSuQm7JmKlEmSoyNuyd4g83yPRy-BGURY94JritreiW1I-xWYSGbxJFmCEw-2jhJjc_FMUIQ32sEPJISf5dB_QH_T53ei7tvnchyaSchPVI92V2ApIoWES5bkyOVJsnbSp-IkD7QSI_hrNKEeoEq-quhCudH5yDQKrJhjrBFb-lF6vuzuRclequNpv1Xk-zUsBxzNaEnNeKUqPoM7Kz_r14cf3n7tz5JkgGqTZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
طيران مسير مجهول يجوب منطقة البلديات في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87784" target="_blank">📅 18:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87783">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
شرطة البيئة العراقية تكتشف كهفاً في صحراء الأنبار، بداخله نهرٌ يحتوي على أسماكٍ نادرةٍ جداً عمياء بلا عيون.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87783" target="_blank">📅 18:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87782">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
🇺🇸
‏محكمة الاستئناف الأمريكية تقرر ايقاف مشروع ترامب لانشاء قاعة الرقص في البيت الأبيض بكلفة 400 مليون دولار</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87782" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87781">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-5xlbwI3jo6RIr9KMguTQ9I5ip0gp67o5uzMGHmlrX3LAKOZTqhGJDYQRfonxsgMYZd-NJA2WSR65clXB0JQjRdeRG56GW5NkuxNleR8IJCoh2l3ZqVxuy9lLlwYFWYmL-h43jsbqjGGg23b0X1TmEyxYSVAUAOz3ihLSIyWraV5tE_jhE6r9OCpPubk_-t_SFvvjd50gm3nCoCpzQ8z_7UWyV2ElCQ7Cb7avg3AprwA1rFeLdTPkdSW6_0_oH9CqC_1u-yPMrzqWtGzm9F-PZ3JOR--hQJ3zJ7AlrpD5It1mkvoaqSvCvDqg2niL7i21VXinNgx7L4ZRqS9RMVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
منصات التتبع:
شوهدت اليوم ناقلة نفط عملاقة تابعة للشركة الوطنية الإيرانية لناقلات النفط وهي تقوم بتحميل مليوني برميل من النفط الخام في رصيف أزارباد في جزيرة خارك بإيران. ‏رغم أن هذه أول عملية تحميل تُشاهد في الجزيرة منذ نهاية يوليو، إلا أن إيران واصلت تحميل ناقلات النفط في محطات أخرى. ومع ذلك، يبدو أن إنتاج إيران من النفط يتماشى تقريبًا مع إنتاج مصافي التكرير (الاستهلاك المحلي)، مما يعني أنها قد لا تحتاج إلى تصدير كميات كبيرة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87781" target="_blank">📅 16:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87780">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTZR8zL8OeOjDAAejaCKx4V0PdShQr9egpxxdBEKIfTHUiZUq4a5ny00ZVbDnZFvKsQjb4GlBh2ynGXJI1zAoPo4RfI7NncceChZBaEf_CqvcpaQKTCelfPLKSrRg3hvbTZbIFYBGhh-KVeYIbZYwl_oP9kAU9f2tqo53gV_qPLPw4afoi42_JMfwuvuPSxlpbKI3OKMM-SNmM-4pe0bnGTY_YUIFiqSh_7kMPlcDD2wcnTWX-1mIvZunGQgrY7RqMoGlEfNlEl_pZAMnn7Qq63sfi2iYkYGxgNLlFImyc7gGrmzqL9pV11Utzzt-Zy_3JZw_b5VTpRhXwpyepcEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
‏
ترامب:
لقد تعرض نصبنا التذكاري الجميل لحرب العالم الثانية للتخريب بالطلاء. لا توجد إهانة أكبر من هذه لأبطال أمريكا الذين ضحوا بحياتهم في الحرب العالمية الثانية. أولاً بركة المياه العاكسة، والآن هذا. نحن نتعقبهم! من أين يأتي هؤلاء المتوحشون؟</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87780" target="_blank">📅 16:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87779">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارة الخزانة الأمريكية: الولايات المتحدة ستفرض على إيران عزلة اقتصادية غير مسبوقة</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87779" target="_blank">📅 16:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87778">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزارة الخزانة الأمريكية: الولايات المتحدة ستفرض على إيران عزلة اقتصادية غير مسبوقة</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87778" target="_blank">📅 15:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
كلمة مرتقبة للأمين العام لحزب الله الشيخ نعيم قاسم اليوم الجمعة عند الساعة 18:30 بمناسبة ذكرى الانتصار يتناول فيها آخر التطورات.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87777" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اكسيوس:  في الأسابيع الأولى من الحرب مع إيران، كان بعض أقرب مستشاري ترامب مقتنعين بأن ترامب سيدعم نتنياهو في الانتخابات.  في ذلك الوقت، كان ترامب يُطالب بشدة بالعفو عن نتنياهو لإنهاء محاكمته الجنائية.   لكن مع مرور الوقت وازدياد تعقيد الحرب، بدأت مصالح ترامب…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87776" target="_blank">📅 15:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87775">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📰
اكسيوس: تشير غالبية استطلاعات الرأي حاليًا إلى عدم فوز نتنياهو. الرئيس الأمريكي ومستشاروه يدركون ذلك. وحتى الآن، لم يُبدِ ترامب لنتنياهو الدعم العلني الذي يأمل في الحصول عليه، رغم تكرار سؤال الصحفيين له عن ذلك.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87775" target="_blank">📅 15:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87774">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📰
اكسيوس:
تشير غالبية استطلاعات الرأي حاليًا إلى عدم فوز نتنياهو. الرئيس الأمريكي ومستشاروه يدركون ذلك. وحتى الآن، لم يُبدِ ترامب لنتنياهو الدعم العلني الذي يأمل في الحصول عليه، رغم تكرار سؤال الصحفيين له عن ذلك.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87774" target="_blank">📅 15:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87773">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87773" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87772">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87772" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87771">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
‏
رئيس لجنة الإعلام الأمني العراقي:
التحقيقات مستمرة لتحديد مكان إطلاق المسيّرات باتجاه أربيل ولا مؤشرات على إطلاق المسيّرات باتجاه أربيل من داخل الأراضي العراقية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87771" target="_blank">📅 14:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87764">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFnq7AZIn_nTQn9CBRk8JJm_O1tupeFUKRnEFj3XvvJk3JVLbAS4ZSCHj9wXZ174g4VkHdt8mZi3TxaZzr-KlC2u3qGy1vh3TfuNgZNppk9wN__R3E50C0AfdRp5Q-VmsooTZwVmQiCA6XzlDuisWS4bIqIt9fqk8s1hx-_y2W9OhNQoEvv0rTUE60nC1aSCe5MzBHVUCSHI634pJGbOW7wIBXRivqpAgqKdCTs2bzgziar8ugzNJNHMwukyCvgBP1GwyOe3y9oV9PDrOcyxlExE78iwCXMA1vag5-mXggm2fSNDMgvsfiFZnWYst2ePVtBeZOZypvFKAK4IMIdaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfnyzzLYAlDLx_J9DiOJN6ukFTr-7FXIbrGHad-lR13hb0t7e0PKBDHJG_FRzypcg6Dq9dlZDmW9G7hpn-B0hDvNL8a2Gcg7ZaDkSh1smLOJ4EHNBhSMTtpY4jSH8uQFbA2w9P-4t_HP9Cuin2XisnVqL6lXAP_I0uXuFotspiSxHx7WPiyVM4HIwHrInHr2UjCEoL-yrxfTJ6le1Y6CY8BOm2P9fdyIP4-MWfvjl34FacNGeDf3Jw-WV5dM95-pPER3ui1-PrFM_VR7q3pWTKgQEAic4EEunF5HbAgQrdE5iLxGSbgHIambAo2JIRSZG0mysiwhi21o2Al_brq7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUWNsAbbgWI0eY6lWV-wt93Xsc_49iHX2PKyOIEzu7VF5KLnAt1Uw2cqX4l7XvqykxuMaykr46lTVXQ5eUksFPiFxBleES_W-FqAmlkwyzw1JTEZeYmE7LTXVdMv6qhsBCmsiOq_3KslxLBTs3V37BYCE4IHtBB48iDa4Kj2J0nxJ7ZStgM9EdYxXTxMpcUCmkCmerkXQvU655S9tdIsPOgmthctggP-jmClLECDdzMK4U89XxBJbT3LfTld2OHNHDeh4SEN_BP5zHxNobgOs5SWiDV8GoDwv1dvDWWL0QrUWttOvddfAW6tVpYEvt7lHqksOOpMBrEw8fPnyprTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2yRt1uXuozRIupElF3GdVWVZvSlsPIzbczDLp24n33o5hgglZJwYe8M6M17gFUSlyFIk-9BJCIXbBvzpitQQ9QXUcy8C9d6HOX18HZTb9l5Y7EoSYqIwkVT4jb8xqLlpVdBMiLKO9jp63jdG1uurG7KGjQZ55Crgt08xBtFeLQsEQAzuGPPK_z-M_xZ1iL31SIDkT33jHpppPigaoTr9oZrY_Bxwq9VUcdVcOXor0f6KC73fIUwZOXTWmlCgBcVSiogCGuoBelPkei8eK81wspuhR7xGzqijPh7tr2vrgbQi0c7Zc-VxCBY1TWlwsJ2NGZWU6bVH72hYCYiGf5M8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fx8kYnMaHgTcoui12q4m3m6vFQVM2Fd98YQhIfyS1CSsy0fQva0jtKBFODKUYgIbwa_jtLQRSHxbUhuxF6p0Encey7-DySO3-xxHqFUJmECbxwOLURo3v_HeWiNIyqPzJapx2A2B496n3LKmruCbLndNexQ7wjB5px_O43wYXVSM2lOqKkJHIwEr-gPRKITVrsxpX0dYbViLuaDQc4xDprqpbIzpROWXn2yuAdxRuta6O18vOyngk_pCprg7eo4FdqZMafZBGYbwTrKQBcXwYzPIF_UAOT1nnejcspgXTFd5Se9s2fHxaaSuJ1PNxAp06glCi1gPdYzXiEXSoqFXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvDiMVi2FNsKyV-VDYyURvhoj_bb1WVEl_50c716geCh_U7epaCUbvPcGj9-kPM0gt2y98j9jiPBL_cozqmT66vH9Wh8WFfZaibj37xNF-a81CXIZp-CgM0APT6rMTO2dJDssdsxtRb4m1aPy9lbhYwDm9rpqIhGx6bpV4QRV8wV89xuXV-vCZm2vrMAohEVGmXuOk_vBeePDyQCnRJhu8BYNyPWD0F8K379aJ_ZBEb4OHhdFuPJ7iJ6qeBN-SnBCLHV5_KOFZVDtm3VuupGvB5HKdo6MY4M4bAeAIRvVs-NZ4-gxImTcu12nrsbE9igJSuAsi2gi2iQUgLCY2790g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfpJaz2D1_K4MQcJWgZMxCDO6-4khfm58XHRfkV736EpV4l9bUOZqT-b60urmSDPwcn3-YCaTaWDVTQzW8ehHP5sqYJYUffAbzRsLRU_oW-2kDu5moJJUYwi7RPFNbICM-0OIFlBM0W3CbywMQpvopADPC3tfN8x-eGEjzovzPF_BlJ9xf9x3Woti8WnnvwvkCXcAOAuT2ylN5kTbSnNQE703rg1Ca9Y3MM_DzfGI-DzGOfjEFrhMs_TixxETtj_a05XuHSZszF6GfAg0F5H6aJMOsB63yRPAql9IHSLDxHBO9H0rE4uj_TxUX5OQ8fWg4IE9W9qy8Pg-VR61KU6EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صور لطائرات مسيرة وطائرات مقاتلة أمريكية إسرائيلية تم تدميرها بواسطة
الدفاعات الجوية الايرانية</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87764" target="_blank">📅 14:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87763">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مسلحين يهاجمون وزير الداخلية في إقليم بلوشستان الباكستاني في منطقة مستونغ.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87763" target="_blank">📅 14:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87762">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر
🔻
إستهداف سفينة "ناقلة نفط" في مياه مضيق هرمز والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87762" target="_blank">📅 12:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87761">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي
لافروف:
لن يكون هناك هدنة في أوكرانيا. موسكو لا تنوي إيقاف العمليات القتالية على خط التماس الحالي.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87761" target="_blank">📅 12:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87760">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eggGijbe_lwXFmjG_nLh5J2A2NAPPb4bmNljQr4_XVfzM315hNHr9TFK5lOAgAt1grC4dq5hGdD70WPTGJdVvdlRj17WsdTcvJ-Tf0KzwJW1vSVdw6yGc5IATBNOHrceTbco0ENg4J0trhZZDanqvunelVdKv63pkvGGkbH3DdT8_Xe6cGNRPz1fYnlebR1N4EXNgL6pXD1rJUUsQvkYM4YDYzNSn7zqvGqp9o6pS2BjfUVYBygqJdUTE_8cRCc3pGKYhmq_yae2Ox9qJ3W1CIy3145ApHd_9mBS2t-ZuTudOS4AqS3f3ghbK057CZjJRGjaces-L6_xQhuJ5XSnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🔻
إستهداف سفينة "ناقلة نفط" في مياه مضيق هرمز والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87760" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87759">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الشؤون البرلمانية في مجلس النواب الإيراني:
تمت مراجعة مشروع "الإجراءات الاستراتيجية لتأمين مستقبل مضيق هرمز وخليج فارس" في لجنة الشؤون البرلمانية، وبعد الاستماع إلى الآراء، تم اعتماد مبادئه العامة.
أحد القرارات التي تم اتخاذها يتعلق بمنع مرور المعدات والمستلزمات التي تملكها الولايات المتحدة وإسرائيل والدول المعادية عبر مضيق هرمز؛ وذلك لأن هذه الدول استخدمت مضيق هرمز لتنفيذ أعمال عدائية ضد بلدنا، وارتكبت انتهاكات وهجمات غير أخلاقية ضد الشعب الإيراني.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87759" target="_blank">📅 11:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87758">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسية:
استهداف سفينتين كانتا ترافقان سفناً تحمل أسلحة إلى أوكرانيا.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87758" target="_blank">📅 09:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87757">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed4908a7c.mp4?token=nerv3MNwiW_MSDh0twG-5FBiB_YbI0uyqKQPlCK7MCDJ-WSR912lfHQe9BxIXNF_U6Oze2cIcTegx1LP1CGxnZm-0DFng64THgUPkaBoo3Yr8e4fUGyCzb9GzPCEvRpv-bBkzqq-rpuTJplB3681IFu8wf-eFzJCxBvjg0sV-BCGMpOi4SceklH_kgDpa_-Zb2rsL3ze2VV5P-_u9ZVMr9mOGedKO8FqqCL0YikGiAzlYkD7yY6EGiznEjaNzaunpqmeFJSc0QRs9Cm0YmHz59JNltpMdj5z0fGEnvtXVi1nQA1w4ZF_VIdIJ-FNJ7LIOu249Pm5qu52vE5HKdgAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed4908a7c.mp4?token=nerv3MNwiW_MSDh0twG-5FBiB_YbI0uyqKQPlCK7MCDJ-WSR912lfHQe9BxIXNF_U6Oze2cIcTegx1LP1CGxnZm-0DFng64THgUPkaBoo3Yr8e4fUGyCzb9GzPCEvRpv-bBkzqq-rpuTJplB3681IFu8wf-eFzJCxBvjg0sV-BCGMpOi4SceklH_kgDpa_-Zb2rsL3ze2VV5P-_u9ZVMr9mOGedKO8FqqCL0YikGiAzlYkD7yY6EGiznEjaNzaunpqmeFJSc0QRs9Cm0YmHz59JNltpMdj5z0fGEnvtXVi1nQA1w4ZF_VIdIJ-FNJ7LIOu249Pm5qu52vE5HKdgAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  لحظة انقضاض المسيرة الانتحارية والانفجار العنيف في مخبئ للقوات الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/87757" target="_blank">📅 03:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87756">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb53d6775a.mp4?token=FkAPmQQ_CLfJyoEqgv63-jsg4C1RnozxKS6VUpQpdzSYmZAY2nDuWs-FjWT17UIRKNsROV0kjcx1a1DpuueqQxBOxhL1yUJSsXiZn_3eI4SzFj3EB5PNSZSCMXFE-YfYHHeQ0cj4ZJhQEFeBCQUoV7W6yB_jWwutB3QjjSMMdXll8AUCE0cxQjK8EdRPZZT9lGwN3zA65ajdMR6K7F_RwGIV6TVDTXzgdstS4hCg2bsN8t0jRKO-9OsqujfD3boPw5L4pZIKOGU6r5Vj18tk22d8DVPQhbJDFJkEq8x0EIOm3vhBrqiKjbNaDwZokwb37pAJnzrCthTZTon0yvb_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb53d6775a.mp4?token=FkAPmQQ_CLfJyoEqgv63-jsg4C1RnozxKS6VUpQpdzSYmZAY2nDuWs-FjWT17UIRKNsROV0kjcx1a1DpuueqQxBOxhL1yUJSsXiZn_3eI4SzFj3EB5PNSZSCMXFE-YfYHHeQ0cj4ZJhQEFeBCQUoV7W6yB_jWwutB3QjjSMMdXll8AUCE0cxQjK8EdRPZZT9lGwN3zA65ajdMR6K7F_RwGIV6TVDTXzgdstS4hCg2bsN8t0jRKO-9OsqujfD3boPw5L4pZIKOGU6r5Vj18tk22d8DVPQhbJDFJkEq8x0EIOm3vhBrqiKjbNaDwZokwb37pAJnzrCthTZTon0yvb_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تشعل سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87756" target="_blank">📅 03:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87755">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe85afd9a.mp4?token=HGndCi50b3GJ2L6X2foolD6acR8v-xH9mgjn3faT56GA_edNFMUsgMRy-5K-Ze_HE2OT58jaf97qKhPtbJfAYg5zRF2DRNXAhutqWYn94qUs5eI-s6UzTF8HrrJGpEQfH484A1Abxiq7W5rPqVIEVA8lLCjSdC9bSQ9JEyX9fH6ShfubuPuDczfOJFk9jukVTZERIsVtkl9Ah2oyjfPxkgUHgaavMC8saXpDe_tm6EHBUur4S0uNAeI5Iw-xdtcg4H37J5D8sQvYEeXlIC32bV5chW6T7oWXrmoM0zV02gUNa6SFEf0NB43JT7d0NQKrm0h89iq0NypMt8S5_F3T7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe85afd9a.mp4?token=HGndCi50b3GJ2L6X2foolD6acR8v-xH9mgjn3faT56GA_edNFMUsgMRy-5K-Ze_HE2OT58jaf97qKhPtbJfAYg5zRF2DRNXAhutqWYn94qUs5eI-s6UzTF8HrrJGpEQfH484A1Abxiq7W5rPqVIEVA8lLCjSdC9bSQ9JEyX9fH6ShfubuPuDczfOJFk9jukVTZERIsVtkl9Ah2oyjfPxkgUHgaavMC8saXpDe_tm6EHBUur4S0uNAeI5Iw-xdtcg4H37J5D8sQvYEeXlIC32bV5chW6T7oWXrmoM0zV02gUNa6SFEf0NB43JT7d0NQKrm0h89iq0NypMt8S5_F3T7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  لحظة استهداف مخبئ للقوات الأمريكية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87755" target="_blank">📅 03:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4fbc1059.mp4?token=m1krcd68IOsJJW9O--qk4_gnQxyGs_jMNu-Y2rQbQo_tW3IqJ2zR3WF0ftWRgkuRGrPGwjTC405UhRnTHC9q4mjMmpizgkoC9ZHMGFYPYlMNI3JQ3eZhbq848-GMHRFTPmLCTjTdAo_giOIOwskbRgWUuxxxlG5QoBmk6UB8NbOxUkNIpqRLUyprDH7Qj_WDhahl3gC6q5aervMASylIgz1hxpupMto4IVDYf8G9XbBjZpbKg03YqxmAOucQdpL0so7lKzNoD8xsgpGeLS9koeZzJmd5zvAHVbYArJycDQp0kUxQwZBK7ZD6SgRoOb1ulPV1I9KShRbv0qglCL4Owg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4fbc1059.mp4?token=m1krcd68IOsJJW9O--qk4_gnQxyGs_jMNu-Y2rQbQo_tW3IqJ2zR3WF0ftWRgkuRGrPGwjTC405UhRnTHC9q4mjMmpizgkoC9ZHMGFYPYlMNI3JQ3eZhbq848-GMHRFTPmLCTjTdAo_giOIOwskbRgWUuxxxlG5QoBmk6UB8NbOxUkNIpqRLUyprDH7Qj_WDhahl3gC6q5aervMASylIgz1hxpupMto4IVDYf8G9XbBjZpbKg03YqxmAOucQdpL0so7lKzNoD8xsgpGeLS9koeZzJmd5zvAHVbYArJycDQp0kUxQwZBK7ZD6SgRoOb1ulPV1I9KShRbv0qglCL4Owg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف فندق يتواجد بداخله عناصر من القوات الأمريكية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87752" target="_blank">📅 03:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b228489921.mp4?token=NnUCFF-wfF7CAt8DY5usHDGaTizLxpyEdx3qL7YkwaGWMimodC8DScJroHcEIyv3RzV3KJWF4I02zS1ar9okcBdo29-ACGqTHJzMSxu1UuZlZcDTimkxrGKXCCFyaFqc2CvEl-qRNAG6J564rhga_knsHjyA_lv0_fTIaTv1Z8K2vkPCBMRZg3DeJkSspToh71U_KNwyBtzKSglSxrtDoHon-Rm4WZwe5A4nrqUfxh5WwBbPdFkHdJfVB3dN8xhRkdO7mQa_Gm806SwL4owj0ty17yIVJHZ8N6NsIHL7IW6rVJbt3ApebturQaH5WNyZ4FAADkuyS_zKtdJDCURPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b228489921.mp4?token=NnUCFF-wfF7CAt8DY5usHDGaTizLxpyEdx3qL7YkwaGWMimodC8DScJroHcEIyv3RzV3KJWF4I02zS1ar9okcBdo29-ACGqTHJzMSxu1UuZlZcDTimkxrGKXCCFyaFqc2CvEl-qRNAG6J564rhga_knsHjyA_lv0_fTIaTv1Z8K2vkPCBMRZg3DeJkSspToh71U_KNwyBtzKSglSxrtDoHon-Rm4WZwe5A4nrqUfxh5WwBbPdFkHdJfVB3dN8xhRkdO7mQa_Gm806SwL4owj0ty17yIVJHZ8N6NsIHL7IW6rVJbt3ApebturQaH5WNyZ4FAADkuyS_zKtdJDCURPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف أمكان تواجد قوات أمريكية في أربيل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87751" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87750">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e85c067dbd.mp4?token=XX_0z7TIhNCdseZVcUW-4rgIk5L08YAcRfqbBZOYZQNvtIPkRYFD1d8IBC96x1nGCDHcTcreuRUP0OC61JSrwn95FTZFchZ9q2WTY5CLHoLKlsE8syq5LQzOI_YiK_NdfBkqmMnLjLurJQGpvmDvxqHo191FMz92uAvQLbFvli9EzcHlOFV3fBmfbhNMkdLdriWZhdY3OcHrrrDCq2pfWpfBLRlgUysxHDOsRP4STf6Ux_iea_4qnYZdpHTsVtZS3-ZeFybggBLmUvzfF1IASn3kxGMMIvjT4ydnOtkKVqlUjyUcO8MDntaxXIl5cpl_ciMWrZ8oPq6RxJ9L1o5Ffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e85c067dbd.mp4?token=XX_0z7TIhNCdseZVcUW-4rgIk5L08YAcRfqbBZOYZQNvtIPkRYFD1d8IBC96x1nGCDHcTcreuRUP0OC61JSrwn95FTZFchZ9q2WTY5CLHoLKlsE8syq5LQzOI_YiK_NdfBkqmMnLjLurJQGpvmDvxqHo191FMz92uAvQLbFvli9EzcHlOFV3fBmfbhNMkdLdriWZhdY3OcHrrrDCq2pfWpfBLRlgUysxHDOsRP4STf6Ux_iea_4qnYZdpHTsVtZS3-ZeFybggBLmUvzfF1IASn3kxGMMIvjT4ydnOtkKVqlUjyUcO8MDntaxXIl5cpl_ciMWrZ8oPq6RxJ9L1o5Ffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف أمكان تواجد قوات أمريكية في أربيل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87750" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
