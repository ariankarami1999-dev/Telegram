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
<img src="https://cdn4.telesco.pe/file/LUASdlT7F9V-VpKjga_7eOaoUVoFFFaaLe2DvMB0M16pNZPreWf575JDsKXpWN4qF_T8pCpPLzP0U6oAVaJMd7SX2kqxZjMwGraFm9rcBhqXyGCT_UxDbB_LU8Bud9wX-VBlUGwAAfCq2RdXrqvQySRJSODfMD8PIGFG1eSftmXbV2nClofwJRtYi7_s6Q4POhHoZYC7uDs9I-b7CqUYT2Bbu3FEi0pquMu8eHplRiEp_iGumVUTOufzMBH0gIK7kDQrNunfI1zqgwiKSCMQVJztsa6FMa2Zs9nV8iuvC2ki7rgJmGnvWNZYpQnJPvI07x8OUV0kPqaS3byK2XKoWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-80333">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">البيت الأبيض: ويتكوف وكوشنر سيحضران في اجتماع الدوحة.</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/naya_foriraq/80333" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80332">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnl733bVDhXZFdH43FFPq9p_kCI2SP2QYiHjj_nc39SzbOuzOMwjpjDhVrnwI0YfgZk7fQesB-nPbreN5gkMs5yCpiqhgIoToQOaOuO0BxoEPhINU9kygM_anlZfBcSJZ02zdJt8Ng3VW8UNo2xXb9LPv7PFdLcVRYt5aDi8aN5HL4DSF2vzMcpkWgAPW7WCc6pI48wKs_a83ztgDyb7RbKCeimsHeB2AFvmXjRaM1-DzvLQib5-1gkrAPat4cjUakMdJmmyG3PQUHwPCwtIUMy8_McwPaIO9Rm35eVZLmkDroxfvyeFGHH4Nxk46BUn09Rn7c6MJe0oQgixLR6VGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
قيادة الحشد تبحث الاستعدادات للأربعينية ومراسم تشييع السيد الشهيد الخامنئي.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/naya_foriraq/80332" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80331">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تحليق طيران مروحي إسرائيلي بأجواء عدة مناطق في حوض اليرموك.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/naya_foriraq/80331" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80330">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اعلام العدو: تم تفجير عبوة ناسفة استهدفت مقر القيادة الميداني لنائب قائد لواء الكوماندوز في جنوب لبنان. هناك مصابان من جنود الاحتياط في الوحدة. أحدهما في حالة خطيرة، والآخر في حالة متوسطة، وقد جرى إجلاؤهما بواسطة مروحية.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/naya_foriraq/80330" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80329">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية تحذر فرانسا:
إيران وحدها ستتولى عملية إزالة الألغام من مضيق هرمز بحسب مذكرة التفاهم.
لن تشاركنا أي دولة في نزع ألغام مضيق هرمز ولن نسمح بذلك من حيث المبدأ.
الوضع في مضيق هرمز حساس ومعقد وننصح فرنسا بشدة بعدم تعقيده باستفزازاتها.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/naya_foriraq/80329" target="_blank">📅 20:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80328">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزير الخارجية العراقي فؤاد حسين يلتقي الارهابي ابو محمد الجولاني</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/naya_foriraq/80328" target="_blank">📅 20:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌟
🇮🇷
مسؤول أمريكي:
أوضحنا لإيران أننا لن نفرج عن أموالها المجمدة إلا إذا تحقق تقدم في الملف النووي.</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/naya_foriraq/80327" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80326">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndWeowgaHO_7XA2b5ho0GpOflW-lQAb5B16_xSCefdchjoYARF2Voo4QRo9On2T4pbuyND6n0ICvJ9zxeeR0i2ycvxhJAGCABWs5-oMM_rsf0MNq5CY1ZFHwH9SdCP9Z3PwVUsZSPMlQSf3A9BnQqHxL0Smt0xYdhnIjyDdvF1s7EqVsiM-sHzV9RD3Uk7r2LBx760Yt8xSC1HyOa-errel48fvuC0Br32a1hl0FAHvHZsbzQBhzD8EfwiZ7Wwhfq4bOlBzmMF7oS6dimkoeKzC8WeLLQoB_e6nLceTCUzgoeO1ihkmX8ufY7-IW8_ZqZ_ozxn4Tla0joId5xLyeFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب:  «انتصارٌ كبيرٌ قبل لحظاتٍ في المحكمة العليا، في قضية سلوتر، حيث تمّ تأكيد سلطة الرئيس في بلادنا لعزل مسؤولي السلطة التنفيذية والمعينين في الوكالات، أو الممثلين، بموجب المادة الثانية. لقد سعى رؤساء الولايات المتحدة إلى هذا القرار منذ زمنٍ طويل، ويعود…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80326" target="_blank">📅 18:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80325">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الاسرائيلي:
نتجهز لمعركة جديدة مع إيران في اي لحظة يمكن ان تحدث ولن ننسحب من لبنان.
اندلاع الحرب مجددا مع إيران قد يحصل إذا قرر ترمب أن المفاوضات استنفدت أو أن تهاجم إيران إسرائيل.
معادلة هجوم حزب الله على مستوطنات الشمال تساوي الهجوم في الضاحية لا تزال قائمة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80325" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80324">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXvhifz-DJIwMPg5hjPSzHMppWeD623HDJWQjvEIXiIeSqPUtlx8qkxN2iMpQNH0RG7G52EA08HUzVegIocdSi9I0tpDaOwCaZQkWthkYaHOjRdxatHAzleJMvbxUbFuANPSA2AkKNjxzpNVPOeWhaQp8-PjyFdjOx3xhs1rHMYo90a7WhTK87yf0EJn0euCHpqDyhTckxLeF1-jYV7yuUfTGtzjaZWVFnfNgIzaWLhuouwlxTnhPCfstIi2Pms8btsS6rVPpc3PiT9CervrwgQDzB6l40rQTuh_wN3qrZpCVI115o3RF19Aqm-mMiJG9DHVBhQKxjpJrhrwHis3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
«انتصارٌ كبيرٌ قبل لحظاتٍ في المحكمة العليا، في قضية سلوتر، حيث تمّ تأكيد سلطة الرئيس في بلادنا لعزل مسؤولي السلطة التنفيذية والمعينين في الوكالات، أو الممثلين، بموجب المادة الثانية. لقد سعى رؤساء الولايات المتحدة إلى هذا القرار منذ زمنٍ طويل، ويعود تاريخه إلى ثلاثينيات القرن الماضي. إنه لشرفٌ عظيمٌ لي أن أكون الرئيس الحالي الذي حقق هذا الحكم التاريخي وغير المسبوق، وهو أحد أهم الأحكام التي صدرت على الإطلاق فيما يتعلق بصلاحيات الرئيس. شكرًا لكم على اهتمامكم بهذا الأمر!»</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80324" target="_blank">📅 18:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قد يغرد …</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80323" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌟
وزارة المواصلات القطرية:
حرصا على السلامة العامة، تهيب وزارة المواصلات بجميع ملاك ومستخدمي الوسائط البحرية، بما في ذلك قوارب النزهة، وقوارب الصيد، والدراجات المائية، وسائر الوسائط البحرية المماثلة، التوقف مؤقتا عن الإبحار وممارسة الأنشطة البحرية، اعتبارا من تاريخ صدور هذا التعميم وحتى إشعار آخر.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80322" target="_blank">📅 17:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
العثور على جندي بالجيش الإسرائيلي مقتولاً في وسط البلاد.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80321" target="_blank">📅 17:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارة التربية العراقية تعلن استرداد أكثر من 73 مليون دينار لخزينة الدولة في صلاح الدين بعد متابعة دقيقة لملفات التقاطع الوظيفي</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80320" target="_blank">📅 17:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رئيس الوزراء العراقي:
يوم 30 أيلول المقبل سيشهد خروج قوات التحالف بشكل كلي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80319" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80318">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
احسان العوادي رئيس اللجنة العليا لتنسيق مراسم تشييع قائد الثورة الإسلامية الشهيد في العراق:  لسماحة آية الله العظمى الإمام الخامنئي (قدس الله نفسه الزكية) مكانة رفيعة ومتميزة وقدم هذا القائد العظيم خدمات خالدة لأمن العراق وعزّته وللعالم الإسلامي، أنّ إقامة…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80318" target="_blank">📅 17:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80317">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
احسان العوادي
رئيس اللجنة العليا لتنسيق مراسم تشييع قائد الثورة الإسلامية الشهيد في العراق:
لسماحة آية الله العظمى الإمام الخامنئي (قدس الله نفسه الزكية) مكانة رفيعة ومتميزة وقدم هذا القائد العظيم خدمات خالدة لأمن العراق وعزّته وللعالم الإسلامي، أنّ إقامة مراسم تشييع سماحته في العراق والعتبات المقدسة تمثّل شرفًا تاريخيًا للشعب العراقي، أنّ الحكومة والشعب العراقيين لن يدّخرا أي جهد لإقامة مراسم تليق بهذه المناسبة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80317" target="_blank">📅 17:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80316">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏وزير الحرب الصهيوني: الجيش اللبناني لن يتحول فجأة إلى أسود تهاجم حزب الله.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80316" target="_blank">📅 17:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80315">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0C-w0qQnSL2-29exCdmz7pqqMq1AzsaUnrBuej9vJHoSoUCwql2rkP_EXnTRE7yDoJOc3Sb3DCIls8HAuDwVph6dlvFakkaHF3lKqVgiMQ1-l6u9yjUWwzWJkB0yBB1PeM8Zn7eROLucJT3FvU5Vff683MNRZjxqG1KSPOXJjV6Af6_R8UfiduWvPi0j5bRXDB6KjsMoyFKzUvqupcbGnbkEAKbM3zipXGLI_OL0bZJI8n1vQG_uS8MLDbxKgUAv8YSkT6JvAC-YNPRQe1B8N_s8aPapqR-ByyKBGGg8Hrm-Az4SFfMm-quuaZ0tWcQAfGI0CZHCgeChme68-kT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية العراقي فؤاد حسين يلتقي الارهابي ابو محمد الجولاني</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80315" target="_blank">📅 16:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80314">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏وزير الحرب الصهيوني: حزب الله عزز وجوده في الجنوب بسبب ضغط ترمب على نتنياهو</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80314" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80313">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏
وزير الحرب الصهيوني:
حزب الله عزز وجوده في الجنوب بسبب ضغط ترمب على نتنياهو</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80313" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80312">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760337d8fc.mp4?token=gSt8guwwBpUERGboDqZ72n-IOhFttOl4JaMpvtq60xmWqP2hB4DnKgKu46iSR6LrYwcyfL5bkEqLqYfYVt1fNrMErUWj2JbhWT1bpc3Xl4-lDBQ6fad8-A4PsJw8yJhlVhQNhLBwNwDOFoRIkkSUdjbRbb13Q93N5FoREaQEK1sQLvPY-OI8syvqouwKcX7R6Y0rm_13K1uKjXHzargr6yWU-AzjN6DXAey1H1s6lu8VaviQWkNd7lKrFGEI-56kFD5Ap5h2uccoGe7_PM6lyklogB14Zy6JLK0Fj0z0nKK2vtulOZDwmp1CICHJbb-3wDzaHB9phimSi8FEqlnD1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760337d8fc.mp4?token=gSt8guwwBpUERGboDqZ72n-IOhFttOl4JaMpvtq60xmWqP2hB4DnKgKu46iSR6LrYwcyfL5bkEqLqYfYVt1fNrMErUWj2JbhWT1bpc3Xl4-lDBQ6fad8-A4PsJw8yJhlVhQNhLBwNwDOFoRIkkSUdjbRbb13Q93N5FoREaQEK1sQLvPY-OI8syvqouwKcX7R6Y0rm_13K1uKjXHzargr6yWU-AzjN6DXAey1H1s6lu8VaviQWkNd7lKrFGEI-56kFD5Ap5h2uccoGe7_PM6lyklogB14Zy6JLK0Fj0z0nKK2vtulOZDwmp1CICHJbb-3wDzaHB9phimSi8FEqlnD1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تقوم بهدم جميع منازل قرية المزرعة الشيعية بريف حمص بالدبابات والجرافات وتوجه سكان القرية بالذهاب إلى إيران أو الضاحية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80312" target="_blank">📅 16:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80311">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
🇮🇷
وزارة الخارجية العمانية:
عقدت اللجنة المشتركة العمانية الإيرانية اجتماعها الأول في مسقط بشأن مضيق هرمز لتبادل وجهات النظر حول إدارة المضيق مستقبلاً والمسائل ذات الصلة.
ناقش الجانبان سبل تعزيز التنسيق بشأن القضايا المتعلقة بمضيق هرمز بما يتوافق مع المصالح المشتركة للبلدين وسيادتهما، مؤكدين التزامهما بالقانون الدولي، واستكشاف أطر التعاون في مجالات الملاحة والخدمات البحرية، انطلاقاً من كونهما دولتين تتشاركان المضيق، وفي ضوء التفاهمات الثنائية والدولية القائمة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80311" target="_blank">📅 16:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80310">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
زعيم المعارضة الصهيونية لابيد:
لن يشكل نتن ياهو حكومات في إسرائيل بعد الآن.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/80310" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80309">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34c356325e.mp4?token=DBzOwLpK3DLLp07bBvpsVI3dsZXpJjcF6Zt_WHrow3oHh48GjXmRS9OmlnYmI_rdSF0PLXv7H0W8Zauh7qV9H_eRfr3_gOZyxOFraXJlmVqhQZbC-qzFxWWoOvHTIPo4XbuJgJf76pLCW175SqMJ-eJ2HGJrp2XHqDmVETzIQNKHVG9tJtlIDJJiKwH5y7XuWCL5nqY6kHNkWOOOBi5Nwmi-G23I4U1f8a_Lj-zpj9as9Cr5Set16rggPUrmGbqKvEYYBCS8xgrU9RzU5FvLj-1BRUJlbuDfEKl6Mh0Rbbsc-UUnX8LGqBMI_IuFsDs7K44StyW0rYlFNNVZ7JJvfo7s3y08k9VWKId6ZcyXKMZIZhM_X3hR7gIzOnd97NI6Hee7z-xR5R2iwhDaoU6LMD_VESLPYXKKN-IqqLt7mvgWqP08Ix0xHYu-oLBO2SW3yWGkMm8H9pCy490i-frdU1nuOFewruJy76tqa0IQcPMJHak9dd9u5nriXRN2hazvNbUwxNqS8OOmRDxXE-PsPfIk7xnEENgp5VqjR_6vuuaUQt-uY_4X9hiESAYeRoKSHjfPYOmJzqyo7UCb7SQCIsxKIw0yb692q4I1EzdZFArIJYxM9NqyE968SU_aIXEkt5n7LerGWrOV0DypDlM3X_bJsV4S_tp_LZS_L3EAI6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34c356325e.mp4?token=DBzOwLpK3DLLp07bBvpsVI3dsZXpJjcF6Zt_WHrow3oHh48GjXmRS9OmlnYmI_rdSF0PLXv7H0W8Zauh7qV9H_eRfr3_gOZyxOFraXJlmVqhQZbC-qzFxWWoOvHTIPo4XbuJgJf76pLCW175SqMJ-eJ2HGJrp2XHqDmVETzIQNKHVG9tJtlIDJJiKwH5y7XuWCL5nqY6kHNkWOOOBi5Nwmi-G23I4U1f8a_Lj-zpj9as9Cr5Set16rggPUrmGbqKvEYYBCS8xgrU9RzU5FvLj-1BRUJlbuDfEKl6Mh0Rbbsc-UUnX8LGqBMI_IuFsDs7K44StyW0rYlFNNVZ7JJvfo7s3y08k9VWKId6ZcyXKMZIZhM_X3hR7gIzOnd97NI6Hee7z-xR5R2iwhDaoU6LMD_VESLPYXKKN-IqqLt7mvgWqP08Ix0xHYu-oLBO2SW3yWGkMm8H9pCy490i-frdU1nuOFewruJy76tqa0IQcPMJHak9dd9u5nriXRN2hazvNbUwxNqS8OOmRDxXE-PsPfIk7xnEENgp5VqjR_6vuuaUQt-uY_4X9hiESAYeRoKSHjfPYOmJzqyo7UCb7SQCIsxKIw0yb692q4I1EzdZFArIJYxM9NqyE968SU_aIXEkt5n7LerGWrOV0DypDlM3X_bJsV4S_tp_LZS_L3EAI6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المحلل البحريني جعفر سلمان المقرب من العائلة الحاكمة الذي كان وقد وصف العراق بـ"جمهورية موز" يقول في لقاء انه لولا الامريكان لكان الخليج لقمة سائغة امام الجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80309" target="_blank">📅 16:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80308">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هيئة النزاهة العراقية: السجن لمدير عام الهيئة العامة للضرائب الأسبق وزوجته عن جريمة غسل الأموال. الحكم تضمن تغريمهما أكثر من (32) مليار دينار ومصادرة عقارات وأموال داخل العراق وخارجها ومصادرة (22) عقاراً في بغداد وتركيا باسم المدانة وبدلات إيجارها ومخشلات ذهبية عائدة لها ومصادرة الأموال المودعة في البنوك التركية والكويتية العائدة للمدانة</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/80308" target="_blank">📅 16:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80306">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHLNLpIk9SpYLrOdQqHkGKM72GdOiQoCqCo9wzfT6AunRQuN3ogRSy97DUrY7mo6oMgJyCRu4Z86xQOxQZzywKPF-rKURC6a2uZaUadD69juett0CVt03uYTYm7P1HzsvE2fnrdI3L6DLfuUnodlw9wgabko3-6ZiVV_pLLR_XPbON7st3HdDutI3imhZ9B40ypalsrKxwGImFgpFLqmdztbUuCUatJn9FzbC8CssVBJp0ctOOBxIOxVBwj0KJaxWKwXHgH8AKIfHpvhDTMbrIa8l6FFHRcK_bXIAWBlwU5GndjOKLLIpoxV0TqhuYu7ZOiMkMbl-CdK0GmlGQBzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-TLfnrQLDB4G8sulIFmd1cTtcwCzELdcABAihwXPK_raVbhuPAZhM1MB7LJfqmFb4aJjwij-1Y2Gdw0UHt0yUdmQsEUo02LTyxlZJVNp0yFbJyjuSksegynzoCOyAypN7mKgwlfch-hls9CNwOHDliLYHvGBiekL2uHSl5XFllyZ17tGQSsVE5nQZ_slllAz15eYGJsIXU2gD1caC1JBZm1O0kKw_5sPllcBr4MGM0-gPx7ONiY6ss14Pr_P1mItefHKFetTHVQbe6JIe_g23HbdkdHvzbh55Osd430uk6I7OwXcQid46Pj4DahGQm6wKmZqyqPELk9JQOZda42_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندلاع حريق داخل جامعة الانبار غربي العراق وفرق الدفاع المدني تستنفر</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80306" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80305">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قوة امنية من بغداد تصل محافظة ذي قار للبحث عن رئيس لجنة توزيع الأراضي في المحافظة بعد ان وزع 1500 قطعة ارض مقابل اموال ثم ولاذ بالفرار</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80305" target="_blank">📅 15:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80304">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رئيس الوزراء العراقي: نسعى إلى آلية تقسيم مُنصفة ولا تجحف حق العراق والعراقيين في منظمة أوبك</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80304" target="_blank">📅 15:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80303">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">البيت الأبيض:
ويتكوف وكوشنر سيحضران في اجتماع الدوحة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80303" target="_blank">📅 15:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80302">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اعلام العدو: حزب الله استهدف مقر بداخله كبار ضباط الجيش الإسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80302" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80301" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80300">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رئيس الوزراء العراقي: زياراتنا المقبلة ستكون إلى تركيا وإيران والسعودية بعد واشنطن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80300" target="_blank">📅 15:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80299">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇩🇪
الشرطة الألمانية:
مقتل خمسة أشخاص في إطلاق نار في ستاد، شمال ألمانيا.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80299" target="_blank">📅 15:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80298">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80298" target="_blank">📅 15:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80297">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
إطلاق رواتب مجاهدي هيئة الحشد الشعبي.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80297" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqBl71aoRGD8rJ9wqsWyFZ-dRWvUCM1z7XGbZUe1JkBRhhhYn5EpaibcRVVV2HkfJ1BF81cu21hsC8snhsDnuH1G_BjeMFL_VYmPrMH6Zen4i17uXgPkIsx9Ip8wSseFemeuErwUi0yWvAfclUXd9F9W_aNxRY4EcmewRKwKf4VXoi_1zmJBtCYYpsgp6zXefRvk-1XAACrm1ONdEK71f2lIq-1wBCwluzmhaoDOKp4UzT2a6rfLBmvPwHnmbLeYqz6z7kzfwrRKtEgpHr-4smxvE9NqsK9nZAJjZH7ikobPSTB3-QuBA4gz7ftzQYJBV8LPKoyp3qtN2Q_XXAZEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Upk5xSj0QBxh5GwErf_qA4XEYhVGtOqPNk2mAb7Ef5HWF4G8vnc7uFqKvhCyr86deNeND7dauEN-TMG76uhZ_9WCmwEHD8sP5yconCeW7txNCwmS8IHkuCyoCNsn9840ywnXzOT_a_DCF9CZu68kGmutmPcw8GtJ77XK6upgGnKd4gtH3m9oE7nJV6MN_G4MqlyPEbz2MdM0JXIpUi3F40avfwSO1ORxIPacVBzvxbm-RLfQhPav9fVMSMsr0OUtjG5_KaNmrn3_bqJEngMINIE6coja1oYnDC28UKE-2gMYUKtdko6iPVP_vl5ZpRa-Prx-8KKAygcizzSPM2SRkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تضرم النار في مقام الشيخ ناصر الحكيم التابع للطائفة العلوية في قرية العريضة بريف حمص الغربي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80295" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80294">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مصدر في هيئة النزاهة العراقية: النواب الثلاثة المعتقلين في أربيل ضُبطت بحوزتهم أثناء عملية الاعتقال مبالغ مالية تُقدر بـ10 ملايين دينار، إضافة إلى 15 قطعة سلاح متنوعة من بينها مسدسات وبنادق من نوع M4.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80294" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80293">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مصدر في هيئة النزاهة العراقية: النواب الثلاثة المعتقلين في أربيل ضُبطت بحوزتهم أثناء عملية الاعتقال مبالغ مالية تُقدر بـ10 ملايين دينار، إضافة إلى 15 قطعة سلاح متنوعة من بينها مسدسات وبنادق من نوع M4.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80293" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
‏
إيدو نوردن، رئيس ديوان نتن ياهو:
‏ينبغي أن تكون هناك دولة واحدة بين نهر الأردن والبحر الأبيض المتوسط.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80292" target="_blank">📅 15:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnfLVRxv21D3mH2CX_4HzDIWZqiJ6Um2GHojORqCJ0W4bidVNMEEzlINeUpqjDFO-gM9yq8_dEPfEFT9soD9WRPbApMC_pphL4njaC4OTpXQgnnQzr9Ah3FkPwf_x1zacLU9gd_djZYe8kMYvUUQT2mQC7EfhTrn93hJ7y9Zo2aUJDFmAevBr6MV_lpHVv_Y41xnErhIn624TU5M2i4-Golk6tWm3MR_Iz43zPukfPoi5mQTm4F9XVQI00tPRzrstAHXJhUZ4LnP3FeH4EX9-wjmgeNJPnWHvzE7jhhIh6PC_WaLgUhUqX_qwW_eOUMYL0gpvZR59S7A4vvUBn7HTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
إيران طلبت عقد اجتماع. سيعقد غداً في الدوحة!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80291" target="_blank">📅 15:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
اطلق حزب الله صاروخ أرض-جو باتجاه طائرة مقاتلة تابعة لسلاح الجو</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80290" target="_blank">📅 14:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">المجلس الوزاري للاقتصاد في العراق يقرر تشكيل لجنة مشتركة برئاسة هيئة المنافذ الحدودية الاتحادية وممثلين عن الجهات المختصة في الحكومة الاتحادية والإقليم لغرض إجراء مسح كامل للشريط الحدودي وزيارة المعابر والمنافذ غير الرسمية في الإقليم</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80289" target="_blank">📅 14:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80288">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d54f652a6.mp4?token=G342QdVstxXsNeDwDcp4dREnUIqHRESlhPbrWDBBDZvBUdUUZMkperxN2RfOJUPfrzF5ds08rApUuYnhP3CADoHr3F8osXGx8S5XnEYwB1456_S_XFak3YNDqC9KJNDHnWVcWQCNOBDwTfrMgmRjI3wuwnoo8Ip9WCgnx5c8BQkObLAd804b_LNnShHoCrvCmyfS_ykywV7h9rNNZ05m796hShz-95bA6_ZkJOrUBl5poWbTtLcs8_0PznBJ0D35sxgQxw07AhMNX6oGCoTvP0r3UlvJ-nmYfZa94CU89sNl6W5JgZjS-ThvreaXZrpFqnKrIWTNkTIqfjcOCNggQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d54f652a6.mp4?token=G342QdVstxXsNeDwDcp4dREnUIqHRESlhPbrWDBBDZvBUdUUZMkperxN2RfOJUPfrzF5ds08rApUuYnhP3CADoHr3F8osXGx8S5XnEYwB1456_S_XFak3YNDqC9KJNDHnWVcWQCNOBDwTfrMgmRjI3wuwnoo8Ip9WCgnx5c8BQkObLAd804b_LNnShHoCrvCmyfS_ykywV7h9rNNZ05m796hShz-95bA6_ZkJOrUBl5poWbTtLcs8_0PznBJ0D35sxgQxw07AhMNX6oGCoTvP0r3UlvJ-nmYfZa94CU89sNl6W5JgZjS-ThvreaXZrpFqnKrIWTNkTIqfjcOCNggQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من عزاء بني اسد والقبائل العراقية في كربلاء المقدسة في ذكرى دفن الاجساد الطاهرة بعد ثلاث ايام من واقعة الطف الاليمة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80288" target="_blank">📅 14:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80287">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
‏
ترامب:
أعلى نسب تأييد في استطلاعات الرأي على الإطلاق. حتى أعلى من يوم الانتخابات، 5 نوفمبر. هذا على الرغم من حقيقة أن إيران لن تمتلك سلاحاً نووياً!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80287" target="_blank">📅 14:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80286">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080fa0dd58.mp4?token=uB9R__JTx6TRPz5fGKuTcTpmVu9GrwDNulWNKeCyUBFWQzwasz4dts6LzZqLuFzGc6wD6mptu1WokGQ4TeSHCCdtcgUbyUmJlvb_eSAwr25Ms0dd67oIgoWR3YWrcO25ipENy6eCmiLzsySL4T340GaNmMaC1LEMuwpGnLQUYm3EWhPselRaqSsY19x6IhU7G-sqcXVeJeqflP4I6jIlQ-bYVt-XXFFbd2UxZKVg2-HYu3FU5NLKW9rnsFHvraurhmj_-EyBqAQ4XnKwQiHZ99Ni2ruY7k89tZiYoBk4PjPa2lqj__rKrn6sLH4m30oZitqRzWYSDkoW5LgUta72Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080fa0dd58.mp4?token=uB9R__JTx6TRPz5fGKuTcTpmVu9GrwDNulWNKeCyUBFWQzwasz4dts6LzZqLuFzGc6wD6mptu1WokGQ4TeSHCCdtcgUbyUmJlvb_eSAwr25Ms0dd67oIgoWR3YWrcO25ipENy6eCmiLzsySL4T340GaNmMaC1LEMuwpGnLQUYm3EWhPselRaqSsY19x6IhU7G-sqcXVeJeqflP4I6jIlQ-bYVt-XXFFbd2UxZKVg2-HYu3FU5NLKW9rnsFHvraurhmj_-EyBqAQ4XnKwQiHZ99Ni2ruY7k89tZiYoBk4PjPa2lqj__rKrn6sLH4m30oZitqRzWYSDkoW5LgUta72Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار كركوك الدولي شمالي العراق وانباء عن حريق كبير في محيطه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80286" target="_blank">📅 14:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80285">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: الاعترافات التي التي أدلى بها المتهمون تقود لشبكات أخرى على مستوى الأسماء والأموال، سردية مكافحة الفساد لا تشبه سابقاتها وحماية المال العام مسؤولية لا تتأثر بالأشخاص أو الظروف</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80285" target="_blank">📅 13:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80284">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: سيتم التعامل وفق القانون مع من يتخلف عن تسليم سلاحه قبل نهاية سبتمبر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80284" target="_blank">📅 13:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80283">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: رئيس الوزراء وجه وزارة المالية بإنشاء حساب لإيداع الأموال المستردة من المتورطين بالكسب غير المشروع</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80283" target="_blank">📅 13:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80282">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: إلقاء القبض على 21 متهما متورطا في ملفات الفساد في عملية صولة الفجر</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80282" target="_blank">📅 13:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80281">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: إلقاء القبض على 21 متهما متورطا في ملفات الفساد في عملية صولة الفجر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80281" target="_blank">📅 13:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80280">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
هيئة النزاهة العراقية: تمكنا من حجز كميات كبيرة من الأموال في الخارج</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80280" target="_blank">📅 12:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80279">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a162cc92.mp4?token=Rr1ph-KZyKixe6FK2XBj9nHWd6hXaPIqBEW04xnmBZGFUQRU0PczPE9rdZIYeto6dTCjuzhKN923sMttNN-OtyHO5DVbYREkxFP5OU9ZULbitdeXq7-K73x3MgKp-k6in7iguGH22298_tFG4xO805q0sByj9RIzIwgDiDEPzEg3qWmc91Px2PtV5qE7kaEpKF4f5g2rJtZZ66bvk9cgXhNgD2gIlnfgXTSPnM4jPLvPEiETXEgU4_CGUhvbuVFf8X0YZ93TqhJqRAElcaNTkkEWVt4BesFvZF3p70hDb7EUN9xDiIx9WF-L6HaezRL1esUTZJu-UmcNdq704qUgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a162cc92.mp4?token=Rr1ph-KZyKixe6FK2XBj9nHWd6hXaPIqBEW04xnmBZGFUQRU0PczPE9rdZIYeto6dTCjuzhKN923sMttNN-OtyHO5DVbYREkxFP5OU9ZULbitdeXq7-K73x3MgKp-k6in7iguGH22298_tFG4xO805q0sByj9RIzIwgDiDEPzEg3qWmc91Px2PtV5qE7kaEpKF4f5g2rJtZZ66bvk9cgXhNgD2gIlnfgXTSPnM4jPLvPEiETXEgU4_CGUhvbuVFf8X0YZ93TqhJqRAElcaNTkkEWVt4BesFvZF3p70hDb7EUN9xDiIx9WF-L6HaezRL1esUTZJu-UmcNdq704qUgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قوة أمنية من بغداد تقتحم بلدية بعقوبة بمحافظة ديالى وأنباء عن اعتقال موظفين ومهندسين من داخل البلدية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80279" target="_blank">📅 12:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f80ffc4.mp4?token=TjKR3V1Ba-GvdW4L7GJlZ251ly7puySAo1tInMMvPPdwIXTMQQktXtheOApdxXguTJ_cmdHlSjX35pue0R3n4OlT0iC3uVMy_UlLJsSLZDtzrfYmRfuLFVrLo7CP_hD5fOhc6cfghPZ9bCGWx_C5__CTGIzvBys41PngYmSpTL1KHonEiaQiXblgX6iZsy50xuep8FhErjYOZ0jYU7tcwSrJakTfA6ZVSD_vZyRyRKR7_e-IPkZUNuN093kPR8LwNPsNfoIGrNPsM58jwUuxhNc8rYEOGa38OSSNqKvck3r2L1TqeqgEbDBmHpuo1bUwkCb9cxHyUY1apP50dlN5XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f80ffc4.mp4?token=TjKR3V1Ba-GvdW4L7GJlZ251ly7puySAo1tInMMvPPdwIXTMQQktXtheOApdxXguTJ_cmdHlSjX35pue0R3n4OlT0iC3uVMy_UlLJsSLZDtzrfYmRfuLFVrLo7CP_hD5fOhc6cfghPZ9bCGWx_C5__CTGIzvBys41PngYmSpTL1KHonEiaQiXblgX6iZsy50xuep8FhErjYOZ0jYU7tcwSrJakTfA6ZVSD_vZyRyRKR7_e-IPkZUNuN093kPR8LwNPsNfoIGrNPsM58jwUuxhNc8rYEOGa38OSSNqKvck3r2L1TqeqgEbDBmHpuo1bUwkCb9cxHyUY1apP50dlN5XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق ضخم جداً يلتهم معارض النهضة وسط العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/80277" target="_blank">📅 11:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYGwwe1biYwfpgxylal9hlaNsBP9bvof2PhS7u8u-ZmGoLa3zwtBE1XwoPMlrOOWUKLwzuqnALaY7h4Dr04FeW4ibDuehwPzSbpntrRYBa3FPrkD4hl-kSKKAB6b-MrfKB1Sqzt8OCk_EyyoKkvAEusV2U8Z4ZwLhMvL1dxw7-21j9i7NbSBEK2DlCCnNGDSlTxK9iRIL-vjzOVJK40EEFbJKLtsFabp-98j9oB8gQIxhXLputAx_G9fBtyilGXZ1_0RCIViXKsMfPobXg3gNxlM43dumdPec2M8ghaspZFSCYsCspvjRKwch49M_ds9iQA3Y5sF8Q7qXc-qsdGooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يوجه آئمة صلاة الجمعة لوقفة سليمة يوم الجمعة ترفع فيها رايات الإمام الحسين وأعلام العراق دعماً لحملة الاعتقالات ضد الفاسدين في العراق.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80276" target="_blank">📅 11:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tClQQ2teBLGZJ5j0Bxte_23Z1lmqN69B7-7MkB9937ZEb9sjAeDCU85TFIAbOcPV6RwZlQHPa-ZQEzc77GNZT7nLT-i1DHStgEDXPwydhWHj-rXajBKNwP91k69svAYuA-fm8PIMVo6uDxNUe3nxwe7YCOdrRIxVg7mBp4UabDVcypNjOmdGoJ37vfVVXF7qBChBNpGUDTEzTTTy_o3u0tgv5kmsYDI82iDYmQ4d-ehLh8e1zQHegNdORyoshlz_xfzx4M47E58zM-OlvcXoG_jtkJQhsyy6KMTswMIHzaHN8Y5c5Qkw8BlhhPbXYxHTHkUxi9Y4uc7-v7pM3LMzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الجيش اللبناني يغلق طريق النبطية الفوقا ويمنع دخول الأهالي إليها بعد تكرار الاعتداءات الإسرائيلية حيث تعد هذه الخطوة أول خطة استراتيجية تم تطبيقها من قبل الحكومة اللبنانية لتحرير الجنوب.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/80275" target="_blank">📅 10:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c76cd22f.mp4?token=C9E6QIVXFK6lqhpgEmPHG5fuMXL3x8w55mfILVVKsGXoRp40KncqG7XHPCYPdO46P0eRbZDqS_5Vb5TQR6abW8usTusz8u54_BBzkN-PdTKh33YkwqqJeq2qWTjbIpqODRC5bYgFwetmlvVJwF02obu1vY_txUDER19ZxG9OpKwOIQNBvoAXttUwUcM-uR4wZZqQ2aTlD2ctr-UlIuzbb2-2lgzULKLxlv6m2t_SepPaPebw78WE1WNXi5aWrZCWygQleDFCYDvlq16laHwrDjgwmEXkMcpIBJUOzLst1RpSQd_klZ4-iO2L7vzUGZAu1PQ_yd_7VWAsJBfpfLdA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c76cd22f.mp4?token=C9E6QIVXFK6lqhpgEmPHG5fuMXL3x8w55mfILVVKsGXoRp40KncqG7XHPCYPdO46P0eRbZDqS_5Vb5TQR6abW8usTusz8u54_BBzkN-PdTKh33YkwqqJeq2qWTjbIpqODRC5bYgFwetmlvVJwF02obu1vY_txUDER19ZxG9OpKwOIQNBvoAXttUwUcM-uR4wZZqQ2aTlD2ctr-UlIuzbb2-2lgzULKLxlv6m2t_SepPaPebw78WE1WNXi5aWrZCWygQleDFCYDvlq16laHwrDjgwmEXkMcpIBJUOzLst1RpSQd_klZ4-iO2L7vzUGZAu1PQ_yd_7VWAsJBfpfLdA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قوات أمنية تصل إلى محافظة كركوك شمال العراق لليوم الثاني على التوالي لتنفيذ عمليات الاعتقال بحق مسؤولين متهمين بقضايا الفساد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/80274" target="_blank">📅 10:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQGySPdDXkM_qOSwX2LL5xUFxW2RyMVJANYSHcNH3hfgh5gmqd77bIvPSnjxldzZHxc87ty4tHs7E-bb832Zqh0T9P4O-Wb8RvoNQf1lu-vw7s1IJ6xjWlU3vvoyCVpYs1YG0-El79rYcyx3HJE8G4_sUY7D3j2LnKHDNoqQZXL2WsDGfCP64SCZR0YVZcKMd4y0vwM__U0vrZsl0JyVpNUw-hR9a5Fj-cdw8gCMDwMaMbgJnj-jcoCtG937mn3RuCMt64tRx4c4-Qa_7M44PlKln7EhWYUT4IgKhXlMaZ9jxFu1RAuRGkehAWCvoOWZgVS3V-UFE17RbQoF7ob7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
القوات الامنية تضبط شخص بحوزته مليارين في سيطرة قضاء قلعة صالح بمحافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/80273" target="_blank">📅 01:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
مجلس الوزراء يقر مبادرة المليون قطعة أرض سكنية كمشروع وطني لتوزيع الأراضي المخدومة على المستحقين في جميع المحافظات، باستثناء إقليم كردستان.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/80271" target="_blank">📅 01:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80270">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
رئاسة الوزراء العراقية: ما جرى من صولةٍ ضد الفساد هي مرحلة أولى، والوضع بات من غير الممكن السكوت عنه.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/80270" target="_blank">📅 01:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f416360a.mp4?token=Grj40m_Kfr7_Ab27bddAjdotlIM-eWHJZVwhR99Cov2IA77Oq5iMc6r2AoXgWIa45vJd3zoNzZwqIPL5-3lKp5dSyNQHppeJDjGHFEpuI_TnPZIY5gcY1_dRPdW5WbnNfrzVSzQXixbaI-srfD9dubL6Q2rRCNG1pQhJV7_CkQ7zxy8abLfJDxfLeP-No8aVAYfwrgyGHRuoR4b5ne11PvcKSNiLtT68RjZhG51OgmRFF-h1kDn6USzjAvjBCe1n1MjL8OEyELOjjAbCm47pw8GvFvgq16OptQ9qbCS-rLMBxGN7Y1BUfOtrWEawQ_zG_4vCwR284MI3ml0LiHnkcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f416360a.mp4?token=Grj40m_Kfr7_Ab27bddAjdotlIM-eWHJZVwhR99Cov2IA77Oq5iMc6r2AoXgWIa45vJd3zoNzZwqIPL5-3lKp5dSyNQHppeJDjGHFEpuI_TnPZIY5gcY1_dRPdW5WbnNfrzVSzQXixbaI-srfD9dubL6Q2rRCNG1pQhJV7_CkQ7zxy8abLfJDxfLeP-No8aVAYfwrgyGHRuoR4b5ne11PvcKSNiLtT68RjZhG51OgmRFF-h1kDn6USzjAvjBCe1n1MjL8OEyELOjjAbCm47pw8GvFvgq16OptQ9qbCS-rLMBxGN7Y1BUfOtrWEawQ_zG_4vCwR284MI3ml0LiHnkcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انتشار واسع للقوات الامنية في محافظة واسط العراقية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/80269" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
رئاسة الوزراء العراقية:
ما جرى من صولةٍ ضد الفساد هي مرحلة أولى، والوضع بات من غير الممكن السكوت عنه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/80268" target="_blank">📅 01:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
استمرار القصف العشوائي الصهيوني على قرية عابدين بمحافظة درعا السورية وسط نزوح معظم أهالي القرية.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/80267" target="_blank">📅 01:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
انباء متداولة عن انعقاد مؤتمر لهيئة النزاهة الاتحادية بعد قليل.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/80266" target="_blank">📅 00:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tscpi55i41Tvs_0PujUgjRXJq-K9Pap-lSHYbm1oQ_wBHZJ3IVbcxAx_UbYwRl9S6Ptxz8Balh_0FgHos8fU8S1hCOFCmCQjMCDy0JyJMV-x-qJ4X0BRuUCGCDRgEES4TRM8SR1Xk1Tr2HKbwAASI6LTOsO4gw1wsutSkNEH-tRgFGXj1jSl8o0OoBsN_C1QmIy6CT4-gruUet8MJ1BFPAhOMXpJXmUw1VEFyIWMhJY82SE01nPkPDKf1xAc4uHfVWRZ1t2ZmVeQdUAbdl9Tg9ldK9g5hVm_j9yOJGdVqDQsnOM4PDXtvGTeATqTmCQrAAVPwkkawNq2NwWxcH9Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
انباء متداولة عن انعقاد مؤتمر لهيئة النزاهة الاتحادية بعد قليل.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/80265" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d422bceb1.mp4?token=R3vHmdFWi4PRi2t0XF9Jo_ddMUKZzEakryP8qs6vYx7Ma1U-pIooiehOdpgwxqP4Aeg6gj6_6ru9z5VeccyzMWrVYYmnYOZFIme19DJ7V-mjeJu5Q9e4A5RXjOEHvpLr-AiXtuNs60ik_uP2NYw0VrjbwKcYgTqvmIGm1UNmpludzr8mUuVdMBEH6Uj_dg5GmTFD1pVwOuLnZZnJd7VKg5uchixJ_ioOdsBRTEGPmLoK7Z2iyiPH9OIUW9zBzhrtG_PHqvRpDk2bajfH7ey1XvfO0gIY4Nu852hMcKogjZtuRONS7xVAejTJuIZ5D_6jv_N89bmIrzOdSJDN8FuOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d422bceb1.mp4?token=R3vHmdFWi4PRi2t0XF9Jo_ddMUKZzEakryP8qs6vYx7Ma1U-pIooiehOdpgwxqP4Aeg6gj6_6ru9z5VeccyzMWrVYYmnYOZFIme19DJ7V-mjeJu5Q9e4A5RXjOEHvpLr-AiXtuNs60ik_uP2NYw0VrjbwKcYgTqvmIGm1UNmpludzr8mUuVdMBEH6Uj_dg5GmTFD1pVwOuLnZZnJd7VKg5uchixJ_ioOdsBRTEGPmLoK7Z2iyiPH9OIUW9zBzhrtG_PHqvRpDk2bajfH7ey1XvfO0gIY4Nu852hMcKogjZtuRONS7xVAejTJuIZ5D_6jv_N89bmIrzOdSJDN8FuOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أربيل تسلّم 8 معتقلين إلى هيئة النزاهة العراقية في سيطرة آلتون كوبري بينهم أعضاء مجلس النواب محمد المياحي، وأشواق الجبوري، وزياد الجنابي، إضافة إلى 5 موظفين كبار في الحكومة</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/80264" target="_blank">📅 00:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
الاعلام الاميركي:
اتفقت الولايات المتحدة وإيران على وقف الهجمات المتبادلة في مضيق هرمز وعقد اجتماع يوم الثلاثاء في الدوحة.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/80263" target="_blank">📅 23:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdb22e6ee.mp4?token=mjy8DC36pH5fP4Nomzkve1Pi51cWsjAy-2zP14de4DPg3MXAgPxrpTiAW8VgTT_pmV-q7ffSN_uJ4paQHAoDSqVtjhoN2fDJb_urfNNQvyGAARDh3khQIpoZ7zhu3raWPtE64jiq-DpBXQYeXQKCHkVKI32dAwiHaebTIi4HOTiqQfo0jC82aIqBkL_x3ZmGmPmJT82cpggxUH39Cl9KBzYFRGYLFWxfLk598L0p4-4SDVdHZy8AfIcy_INuIyWiRWMZVmYH7Hohgkzj_FP1efKCoCJ-2NoLNX4HuOZ69eCSsNI3Vzh5RkCAxdZcsPiFgNo37xyNiuztQusvLV7Brw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdb22e6ee.mp4?token=mjy8DC36pH5fP4Nomzkve1Pi51cWsjAy-2zP14de4DPg3MXAgPxrpTiAW8VgTT_pmV-q7ffSN_uJ4paQHAoDSqVtjhoN2fDJb_urfNNQvyGAARDh3khQIpoZ7zhu3raWPtE64jiq-DpBXQYeXQKCHkVKI32dAwiHaebTIi4HOTiqQfo0jC82aIqBkL_x3ZmGmPmJT82cpggxUH39Cl9KBzYFRGYLFWxfLk598L0p4-4SDVdHZy8AfIcy_INuIyWiRWMZVmYH7Hohgkzj_FP1efKCoCJ-2NoLNX4HuOZ69eCSsNI3Vzh5RkCAxdZcsPiFgNo37xyNiuztQusvLV7Brw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار القصف العشوائي الصهيوني على قرية عابدين بمحافظة درعا السورية وسط نزوح معظم أهالي القرية.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/80262" target="_blank">📅 23:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80261">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc497ecbb1.mp4?token=j_TXJKaJJDp1I0BKIRfYrHVbmIq_AZjvovlJ4X1dOeJIC5ecCTmkUx6BnZFXIBlCM_sKNriHL5RCt5CO-XLKqGpcqVleLNL-GcAa4h9ksm1K3jLP1eUX-X2VZPO2-KH4pyvYOARLwGB6lLat9Ir1252h1zI7GwVr6CTrpanXXwSUKcnNO12iQkcsnAC5rmWuo9lC0_IylouhN7VXDqXYP1OgJtoDLP8jRz3TjErqr5C7HonDFojLK21kyREvz42ZPNX_ZA3CuZdbWIsW-7yHXlPkkaVF75WDtOPJCvhHkcg_mTu1h1usntWMQiRiz43Ngj5qvHm3E1LKvJiHKk8L0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc497ecbb1.mp4?token=j_TXJKaJJDp1I0BKIRfYrHVbmIq_AZjvovlJ4X1dOeJIC5ecCTmkUx6BnZFXIBlCM_sKNriHL5RCt5CO-XLKqGpcqVleLNL-GcAa4h9ksm1K3jLP1eUX-X2VZPO2-KH4pyvYOARLwGB6lLat9Ir1252h1zI7GwVr6CTrpanXXwSUKcnNO12iQkcsnAC5rmWuo9lC0_IylouhN7VXDqXYP1OgJtoDLP8jRz3TjErqr5C7HonDFojLK21kyREvz42ZPNX_ZA3CuZdbWIsW-7yHXlPkkaVF75WDtOPJCvhHkcg_mTu1h1usntWMQiRiz43Ngj5qvHm3E1LKvJiHKk8L0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار القصف العشوائي الصهيوني على قرية عابدين بمحافظة درعا السورية وسط نزوح معظم أهالي القرية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/80261" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febc059431.mp4?token=qKdf0qkXfj-f2my9rNOU2UR83MW1pXq83R_K-3LZGQY8VmUmCdBTfmzU2IvHMR21j1qrOwiFa7q9-0-_mJaRdFM-sSZF62HepLG8-MyoV4Xph0MF_T5XZBYDN7t37WOOZEO_B3X9pc7cnD8mMec9dvG5Vc4PYWUu8SL1Dbe33tZBFNSh2dRtsGIjcPGAPCJP2kYFOULG5cEsS7alL3tCRp1hiin95sBvltbhi72meYSIRddkbJlVH68BxMytPPBiqznuMUBMzjUgdwpHqjNCuIjm4k4-WeJdS1tXQ_FqKRxfx5TvMiY_3_ABbjZCOfosBp6u4exPsvT8rb9af23UiVWQSrYSYGrbz5M0zayrniHSfOGeFL2Q5Jcf7Bz14ryfKsf6G4EHnwpwOIc8C2M_yDLXVBrYioAPVpbP0Abago1aALUfMy1GvFaHpvZML5O_gKz6vl7IbbxEotYo2ri2aXcnXm-qpdPHIlYW4bZBBH_CUB0ZS4gZ9-cm86U0BQidWxUM83RVzxpA1tUEofTYks6inWGrN4ZbwwANj2ddhnUvGPSP2HRTYVo6x59jVHok3AJPpUvlZMdD5NaJ1ZkyRc5FkvtqwljJw2fhgyYwbnWEc-RoKUErUbm4AluMqeUobwQ0IrY8vR125sOgudqbiL3EpM7ob-zDtqVNAeOTjrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febc059431.mp4?token=qKdf0qkXfj-f2my9rNOU2UR83MW1pXq83R_K-3LZGQY8VmUmCdBTfmzU2IvHMR21j1qrOwiFa7q9-0-_mJaRdFM-sSZF62HepLG8-MyoV4Xph0MF_T5XZBYDN7t37WOOZEO_B3X9pc7cnD8mMec9dvG5Vc4PYWUu8SL1Dbe33tZBFNSh2dRtsGIjcPGAPCJP2kYFOULG5cEsS7alL3tCRp1hiin95sBvltbhi72meYSIRddkbJlVH68BxMytPPBiqznuMUBMzjUgdwpHqjNCuIjm4k4-WeJdS1tXQ_FqKRxfx5TvMiY_3_ABbjZCOfosBp6u4exPsvT8rb9af23UiVWQSrYSYGrbz5M0zayrniHSfOGeFL2Q5Jcf7Bz14ryfKsf6G4EHnwpwOIc8C2M_yDLXVBrYioAPVpbP0Abago1aALUfMy1GvFaHpvZML5O_gKz6vl7IbbxEotYo2ri2aXcnXm-qpdPHIlYW4bZBBH_CUB0ZS4gZ9-cm86U0BQidWxUM83RVzxpA1tUEofTYks6inWGrN4ZbwwANj2ddhnUvGPSP2HRTYVo6x59jVHok3AJPpUvlZMdD5NaJ1ZkyRc5FkvtqwljJw2fhgyYwbnWEc-RoKUErUbm4AluMqeUobwQ0IrY8vR125sOgudqbiL3EpM7ob-zDtqVNAeOTjrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع اشتباكات بين مقاومين سوريين وقوات جيش الاحتلال الإسرائيلي في محيط بلدة عابدين بريف درعا الغربي.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80260" target="_blank">📅 23:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80259">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaPu_hJqxeiDe0EFKJIpocU_x_ZlXPSQlQr9tRFhKa00rAWP0bwKBKNCNEH8xAIQN7nhfUe2H0KOIWyJL4LAZvxZOB_G2zgGhcm8WBUpny2rd8QraL0TSrmYwnMygAukeln8ors67jEAsatWWuXh43UiGUbZyZjO1TDKBmCrIeVDTPosiwrhUxIG8i2TYb-iiRM0shvA66yPagHHhXwdxMN3_5yKkzdWTwCdU-7SuI7rUWTTaJK7nhFxeDJJNBIJrzNdDh1aZLwBmEBSmB7qO4hFRRaU48zvLpr6CKZYgE_sr2NsQcmOLiP1P6mWJcgMAKj62PK5jc6vqDwdbdaKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اندلاع اشتباكات بين مقاومين سوريين وقوات جيش الاحتلال الإسرائيلي في محيط بلدة عابدين بريف درعا الغربي.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/80259" target="_blank">📅 23:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80258">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMEKqzL96BisA_sUQwUZ0j_cnZKXTWKZWvojPVqoJf0mMcO_WZ7bE9K4ceTugKrjytUaa3Dk-F2_A2LGuJZjbO6WeoE-xsWGworCQx-ubh9ZkwAm4OGd9DwhP09xDsMxpBo1WsVlcj_WJIWR0BmF8r1opNM8uccTpIrYRAPSTQ3BQT75fTWPSB_DWav4pSmhlS1JrANxzUvc0rVnMIgu0Z9pzb6uc8Y6zAXxhtEz_iV-uPr7lDgiyIAVAoAToZKqEaczoDXTPLk_zM9TqBf0zp9B-i9-GgcIHct139PE6RqShfCh61v_cGnpFzMLWDs5grkj8Dwu06q_QmeI_KBdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الاعلام السعودي:
اعتراض صواريخ فوق شمال الأردن.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/80258" target="_blank">📅 23:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80257">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee392353a.mp4?token=FTPI8WcKct6JgbcELDeCCTOViJ9fClKGyB75K91LXcMiCyO0cutSNKW8PeX3xcRcZGSKaV-BVdqkAAv7AlyJyDYCK8kAha_UgDCYHujEgUaPafEO8MhcAkNTiZqiJs_YG9pIuQO0QMo2lRw_BIdSJBdPZAxH7QcySWC3ZDARzGlLgvvQu5RwZkbq-FmmQd460B3PhyZrb9__ERFC8d-i6i2cm4jmOGzPr7YAcYuhTXhl2jmVH-ZR4PXlR_JWccQYuCsFBz02uulU6L-eWQef9J5nzjFfCP4kUyXhr1sZalo9TupP531HyNi80RxMKRFDz-naM_z_tNX4Qrsww81ZbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee392353a.mp4?token=FTPI8WcKct6JgbcELDeCCTOViJ9fClKGyB75K91LXcMiCyO0cutSNKW8PeX3xcRcZGSKaV-BVdqkAAv7AlyJyDYCK8kAha_UgDCYHujEgUaPafEO8MhcAkNTiZqiJs_YG9pIuQO0QMo2lRw_BIdSJBdPZAxH7QcySWC3ZDARzGlLgvvQu5RwZkbq-FmmQd460B3PhyZrb9__ERFC8d-i6i2cm4jmOGzPr7YAcYuhTXhl2jmVH-ZR4PXlR_JWccQYuCsFBz02uulU6L-eWQef9J5nzjFfCP4kUyXhr1sZalo9TupP531HyNi80RxMKRFDz-naM_z_tNX4Qrsww81ZbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع اشتباكات بين مقاومين سوريين وقوات جيش الاحتلال الإسرائيلي في محيط بلدة عابدين بريف درعا الغربي.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80257" target="_blank">📅 23:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8WBP7l93oroJD28T_5kvo4YE3zZHVmz9voOgXn2JMPvhRdwENE37GP_w_UA-EWhMense8N45-MGHDokHKPjqewQUfcLQmzLZy62Xe86iF2dNVIihRassSIOUid7rViuj8lsvOlVM_wQ0J50tiylEP7UC2Ic3GT6biOtAWW9M9uJnwKqqy81ByOXvp77VcYqFMvQSgRWqDM6oNlVLgYzmai_s3BrZVnDQF8uw4TkOTwlmFnUuSxHOywPLH_2U9oOEX_mwFXGWryU0ckiwqRp1yWiYM4Qws7k-BJJ5HZziG5ItyvnLrGnmm5DEymezkekS5pTgNKnjr0q9PYYtpYeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
استيفاء مبلغ (2500) دينار من جميع الداخلين إلى العراق عبر منفذ حاج عمران في محافظة اربيل تحت مسمى "دخولية العراق" ما أثار تساؤلات بشأن السند القانوني لهذا الرسم والى خزينة اي برزاني تذهب هذه المبالغ
الله يديم الرخص
بالفين ونص دخولية بلاد الحضارات
😄</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/80256" target="_blank">📅 23:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e2ec824e.mp4?token=L8km_Q_DvfWK34NACRag6_jOx8JJoRo40y8dZ6Cdcpxr4OwFD1CSFipI1hhp1brL6KkrQVR3Sx_nU2QFUP9RRdjbD5Nn-PEH0T8cosMH04ETfz6cfkd2vqcNCnbEsEq8wOJSGy4vJEj3snMwuOXk2STJI7N1IdTg76eGCwBwokgDSlIG2HQe3kiPJ7Xkod-tZuQbgQjvHHjdAsHVmzxMq73cbqlOG5dDG5VtFUcbnh28VCTjrp745JlaWF1E5j7WxJQ8XttWbjNtipxfZ_ocDDbtqB3ZB2UFj9tOUo6npUmz2L0dcsjwljPE1EBhdSMaqqOeFF6BDIs73N5UP9fPcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e2ec824e.mp4?token=L8km_Q_DvfWK34NACRag6_jOx8JJoRo40y8dZ6Cdcpxr4OwFD1CSFipI1hhp1brL6KkrQVR3Sx_nU2QFUP9RRdjbD5Nn-PEH0T8cosMH04ETfz6cfkd2vqcNCnbEsEq8wOJSGy4vJEj3snMwuOXk2STJI7N1IdTg76eGCwBwokgDSlIG2HQe3kiPJ7Xkod-tZuQbgQjvHHjdAsHVmzxMq73cbqlOG5dDG5VtFUcbnh28VCTjrp745JlaWF1E5j7WxJQ8XttWbjNtipxfZ_ocDDbtqB3ZB2UFj9tOUo6npUmz2L0dcsjwljPE1EBhdSMaqqOeFF6BDIs73N5UP9fPcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أربيل تسلّم 8 معتقلين إلى هيئة النزاهة العراقية في سيطرة آلتون كوبري بينهم أعضاء مجلس النواب محمد المياحي، وأشواق الجبوري، وزياد الجنابي، إضافة إلى 5 موظفين كبار في الحكومة</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/80255" target="_blank">📅 22:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80254">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئيس تحالف عزم مثنى السامرائي</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/80254" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭐️
إعلام العدو يزعم: إطلاق صواريخ من إيران نحو الأردن.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/80253" target="_blank">📅 21:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80252">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭐️
إعلام العدو يزعم:
إطلاق صواريخ من إيران نحو الأردن.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/80252" target="_blank">📅 21:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80251">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
قاضي تحقيق محكمة جنايات مكافحة الفساد المركزية:
أن التحقيقات في قضية المتهم (عدنان الجميلي/ وكيل وزارة النفط لشؤون التصفية) قد بدأت في الشهر العاشر من عام 2025، إثر تلقي المحكمة مجموعة من الإخبارات التي تتضمن قيام عدد من المرشحين بصرف مبالغ مالية طائلة لدعم دعايتهم الانتخابية مستغلين موارد الدولة، وبدعم من شخصيات نافذة في الحكومة السابقة. ولأهمية ودقة هذه الجريمة، استمرت جهود جمع الأدلة والمعلومات عدة أشهر، وعقب إلقاء القبض على المتهم المذكور، كشفت مجريات التحقيق عن تورط مجموعة من أعضاء مجلس النواب في استغلال موارد الدولة للدعاية الانتخابية، والانتفاع من العقود الحكومية بصورة مباشرة أو بالواسطة للحصول على عمولات ومنافع شخصية لأنفسهم ولغيرهم، الأمر الذي اقتضى إجراء التحقيق معهم واتخاذ الإجراءات القانونية بحقهم. وبناءً على طلب المحكمة ومفاتحة مجلس النواب، رُفعت الحصانة عن النواب المتهمين من قِبل رئيس مجلس النواب العراقي الحالي، استناداً إلى الصلاحيات الممنوحة له بموجب أحكام المادتين (63/ثانياً/ج) و(7/رابعاً) من قانون مجلس النواب العراقي رقم 13 لسنة 2018، والمادة (11/ثانياً/3) من قانون العقوبات العراقي رقم 111 لسنة 1969 المعدل، والمادة (20/ثالثاً) من النظام الداخلي لمجلس النواب العراقي. وفور ورود كتب رفع الحصانة، وبالتعاون مع هيئة النزاهة الاتحادية وجهات إنفاذ القانون، وبإشراف مباشر من رئيسي مجلس القضاء الأعلى ومجلس الوزراء، جرى الشروع بتنفيذ أوامر القبض الصادرة بحقهم وتوقيفهم، حيث تم ضبط أموال ومبرزات جرمية تثبت ارتكابهم ما يخالف القانون، في حين لا يزال قسم منهم هارباً، علماً أن التحقيقات في هذه القضية مستمرة على ضوء الأدلة، وسوف تتخذ الإجراءات القانونية بحق شخصيات سياسية وأشخاص آخرين خلال الفترة القادمة تزامناً مع تطور مجريات التحقيق.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/80251" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80250">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d2b6622c.mp4?token=unCz4qWfDI4wDqWL52E9A7cW2wjLCiYBgYnt8FWu5t9OJ8u43eaodC6VRKIssL9uSh8dR-kGsKbXuf61hObTofRpLhfRfclbTecLdREoNr1rqRnTHDKg3OZHTEGWhGlLpm6YAFzjOG5N7XSmzx78KHFI4eYgd7DqkuZuBRbx0TBPcDeK_5AV8umZ9kKgfLtxaUB_iCMZ_Ep8KsyH8RJRkJ9rfzYWz9TckicW2ZDEjSK67i4IFGcqdJGgPTUql2AavtdTHuOdmMEX1vAjXiwCjEozevTXd0Odc5jxn2navr6G9JFiVYEsYjoYR-vH9sSj7baH_KkP7Fe4UaXbhgoUBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d2b6622c.mp4?token=unCz4qWfDI4wDqWL52E9A7cW2wjLCiYBgYnt8FWu5t9OJ8u43eaodC6VRKIssL9uSh8dR-kGsKbXuf61hObTofRpLhfRfclbTecLdREoNr1rqRnTHDKg3OZHTEGWhGlLpm6YAFzjOG5N7XSmzx78KHFI4eYgd7DqkuZuBRbx0TBPcDeK_5AV8umZ9kKgfLtxaUB_iCMZ_Ep8KsyH8RJRkJ9rfzYWz9TckicW2ZDEjSK67i4IFGcqdJGgPTUql2AavtdTHuOdmMEX1vAjXiwCjEozevTXd0Odc5jxn2navr6G9JFiVYEsYjoYR-vH9sSj7baH_KkP7Fe4UaXbhgoUBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اندلاع اشتباكات بين جيش الإحتلال الإسرائيلي وأهالي منطقة حوض اليرموك بمحافظة درعا السورية،ماأجبر جيش الإحتلال الصهيوني على الإنسحاب من المنطقة.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/80250" target="_blank">📅 21:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
التحذير الذي نقله كبار المسؤولين في شعبة الاستخبارات والقيادة الجنوبية إلى رئيس الأركان زمير الأسبوع الماضي:
الجناح العسكري لحركة حماس يعيد تنظيم صفوفه استعدادًا للحرب من جديد. وتقوم حماس بإنتاج مئات العبوات الناسفة والصواريخ المضادة للدروع شهريًا، كما تجند مقاتلين تتراوح أعمارهم بين 18 و22 عامًا، وبدأت مؤخرًا بإجراء تدريبات لعناصر وحدة "النخبة"، وتحاول تهريب طائرات مسيّرة ووسائل اتصال من سيناء، وتعيد تأهيل البنية التحتية تحت الأرض في أنحاء قطاع غزة.
الموقف الذي نقله الجيش الإسرائيلي إلى الأمريكيين هو ضرورة العودة إلى القتال، إلا أن الأمريكيين يعارضون ذلك، ويرغبون في الإبقاء على الوضع القائم وفق الاتفاقات، مع السعي إلى مواصلة تنفيذ رؤية الرئيس ترامب ومجلس السلام.
وقال الضباط لرئيس الأركان: "حماس قوية على الأرض، ولا أحد يشكل تهديدًا لها، والمنظمة ليست مستعدة للتخلي عن السيطرة على غزة."</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/80249" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
هيأة الإعلام والإتصالات العراقية:
الامتناع عن تداول أسماء أو معلومات غير مؤكدة أو غير صادرة عن جهات رسمية.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/80248" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80247">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/526853f2ac.mp4?token=Rraadpn_WQYmFum9QGIdtkKvdO1s6c5KDJ1q9k-n1bI7OFUtLMYL4Tu6wsh2Y4qF9g3KI8lYv0p2xRTZ3T1QLku6aV7zFOM_Zif1ZfzKrmb_ZtVAo-22xibsMi-GQ5GZ3pzMLJK6flZN2Lk9TbQ8hJMwHpJpPoZ0DzMDXRFPzpu8IRdDtYHXlK2Lqn1Wd0yp3Fr0Nfxv-kPqXMrmqhWhcP3hWSYgX5TAUGYXZY1XnM7NWtH4enXWIY5qSpJrzD_x3aLj_kCbErWMVi1Ir1rahk2niPfLvHs9Hgw5ksZmCXXVJIWiEiw6DhEAtWRzYzs1vZy4L4nw8ecY7YFw4s53kWuc6KHGowQ7a9ynlLkV0ZSpFhYq0BnJWuy7-KzpKrlBRT8dXDUnD8o1RO1k0WO0HBqeWd8eKSiVtbirL6xXJk2ZvNzUor6fBcv1tWkNK5oJiLzNp-jYZxRvzkUhpz_1lqJvJnuq68M3FbD0Af2VM_tD5GADu_GFUPmnbu2LLYBZzDMPjOiNndTnsIfQh3zxzyz256TZJaX0jvFJuY34AyVM7TZcQ14FFpAlC4tW69g_4-YIp6XXzUyiT8cieouov1v8aQJKdBYgfu17crnSj05DJkkRd_-bXGsM593ov1un-Y4qyP5Va8j55uB7yCoeKDhkW-uw9w0dK0fS2p9oESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/526853f2ac.mp4?token=Rraadpn_WQYmFum9QGIdtkKvdO1s6c5KDJ1q9k-n1bI7OFUtLMYL4Tu6wsh2Y4qF9g3KI8lYv0p2xRTZ3T1QLku6aV7zFOM_Zif1ZfzKrmb_ZtVAo-22xibsMi-GQ5GZ3pzMLJK6flZN2Lk9TbQ8hJMwHpJpPoZ0DzMDXRFPzpu8IRdDtYHXlK2Lqn1Wd0yp3Fr0Nfxv-kPqXMrmqhWhcP3hWSYgX5TAUGYXZY1XnM7NWtH4enXWIY5qSpJrzD_x3aLj_kCbErWMVi1Ir1rahk2niPfLvHs9Hgw5ksZmCXXVJIWiEiw6DhEAtWRzYzs1vZy4L4nw8ecY7YFw4s53kWuc6KHGowQ7a9ynlLkV0ZSpFhYq0BnJWuy7-KzpKrlBRT8dXDUnD8o1RO1k0WO0HBqeWd8eKSiVtbirL6xXJk2ZvNzUor6fBcv1tWkNK5oJiLzNp-jYZxRvzkUhpz_1lqJvJnuq68M3FbD0Af2VM_tD5GADu_GFUPmnbu2LLYBZzDMPjOiNndTnsIfQh3zxzyz256TZJaX0jvFJuY34AyVM7TZcQ14FFpAlC4tW69g_4-YIp6XXzUyiT8cieouov1v8aQJKdBYgfu17crnSj05DJkkRd_-bXGsM593ov1un-Y4qyP5Va8j55uB7yCoeKDhkW-uw9w0dK0fS2p9oESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اندلاع اشتباكات بين جيش الإحتلال الإسرائيلي وأهالي منطقة حوض اليرموك بمحافظة درعا السورية،ماأجبر جيش الإحتلال الصهيوني على الإنسحاب من المنطقة.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/80247" target="_blank">📅 20:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80246">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
‏قطر تعلن عن مقتل شخص إثر إصابته بشظايا ناجمة عن العمليات العسكرية بالمنطقة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/80246" target="_blank">📅 20:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7354f35590.mp4?token=dQTnwQnYOwBYXSnFXncNzmOyiPJDgDOO1OSZWd05Zujqf_QDL_SKVJpsltdxfZOlavlv5OmiP1udbTETzVFIwCbEsE0stLab9pHNy-xTUBY1LooL1N-EgsWb8bBnR-0ChLHCBO_-AvF3IRIBrThoN-bLWgGSUFSnvFX0Je__gCFIYJH60W8I-bmjn5Y82Oo-JvjLEl2NR1MbrkWyGds3wZx8KCaLbIQhOwT6z_HPA9UGIpsaraK_sjH-CxtZcVAfjLJAlpet1tFoj2PF5xILyqfGEQlrNf1fErwI1AG1ROf5QG6YGIKRqQAIeToGc3S26YCs-lkZRocx3NMlHlNAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7354f35590.mp4?token=dQTnwQnYOwBYXSnFXncNzmOyiPJDgDOO1OSZWd05Zujqf_QDL_SKVJpsltdxfZOlavlv5OmiP1udbTETzVFIwCbEsE0stLab9pHNy-xTUBY1LooL1N-EgsWb8bBnR-0ChLHCBO_-AvF3IRIBrThoN-bLWgGSUFSnvFX0Je__gCFIYJH60W8I-bmjn5Y82Oo-JvjLEl2NR1MbrkWyGds3wZx8KCaLbIQhOwT6z_HPA9UGIpsaraK_sjH-CxtZcVAfjLJAlpet1tFoj2PF5xILyqfGEQlrNf1fErwI1AG1ROf5QG6YGIKRqQAIeToGc3S26YCs-lkZRocx3NMlHlNAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات أمنية إضافية تصل إلى محافظة كركوك لتنفيذ عملية الإعتقال بحق مسؤولين متهمين بقضايا فساد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/80245" target="_blank">📅 20:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce546b894b.mp4?token=MjnUJsk8rrzzV6_dkBn6HQVic8EIDVQASbSmwHHrB6ZykHJc6bDhAOUz7gqmk2LXdt4gVYS67jAtPtEWMMV4Ceizx-lP_6v5dMefn_Aruu26zS0Ld25mZeI76zhOMaKVitCKFCOWLjgaLXQMrqDqG-iDwHX1OEeeqsinQbzYNpTDkJTJ1uIZe_hacMVZvsjYFxql3S6qBFg8942zSIYNK6xJkemDtwpsGYbNveSquBUoZxVa83Kj6rl_wEAIIGyhwIl3c4K9V7FMDb5tlocciPDWYU-9hMIXT-1rIRNMvhT5OMSHLSyGAU-K9tan2LdaPNlNk25XdbAaCUm7lkuAZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce546b894b.mp4?token=MjnUJsk8rrzzV6_dkBn6HQVic8EIDVQASbSmwHHrB6ZykHJc6bDhAOUz7gqmk2LXdt4gVYS67jAtPtEWMMV4Ceizx-lP_6v5dMefn_Aruu26zS0Ld25mZeI76zhOMaKVitCKFCOWLjgaLXQMrqDqG-iDwHX1OEeeqsinQbzYNpTDkJTJ1uIZe_hacMVZvsjYFxql3S6qBFg8942zSIYNK6xJkemDtwpsGYbNveSquBUoZxVa83Kj6rl_wEAIIGyhwIl3c4K9V7FMDb5tlocciPDWYU-9hMIXT-1rIRNMvhT5OMSHLSyGAU-K9tan2LdaPNlNk25XdbAaCUm7lkuAZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
سوريا الجولاني..
سائحة أجنبية تتعرض للهجوم والتحرش في إحدى ساحات محافظة حلب السورية.
اوه ماي كاد
😆</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/80244" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
زلزال بقوة 5.3 ريختر يضرب الصين.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/80243" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
🌟
وول ستريت جورنال:
توقف محادثات كانت مقررة هذا الأسبوع بين واشنطن وطهران في سويسرا بسبب تجدد القتال.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/80242" target="_blank">📅 19:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
مصادر:
وصول قائمه بأسماء مطلوبين من محافظة الموصل بتهم فساد من الهيئات التحقيقه في بغداد الى رئاسة محكمة استئناف نينوى لتنفيذ اوامر القاء القبض بحقهم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/80241" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80239">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16897205e.mp4?token=IXmmM9Lru4cCvNcdXwdXCC53n9e9H5Jo-F8SSJLXOS2svxopkQ6Inlc_8rJPPc3svbUtbB_MNeO6r0jc-uLpPk2tHcLYYrmAs3XPHnwOy6-URAVNMxLLEB6LGajtAiUxwy563jmM-mBe0DPFQtJH5FWK60w18A2ZG_hMknLK9hUsuBux5yrI9OGMP5oeqFMEsydpakz2PReuqMXr7q-Bp63pGirJYG6KF40PvTt7BGqfe-YDbBMaFBrat_jtp1yQnUjrr8xOcnHSV96XjYrTKS_geIrtm2ZOFjfE6Xh0jSrA8FWgF6lA7-j5L9Ey6hBGIkwy-hU8Lc2wI41ZL61M5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16897205e.mp4?token=IXmmM9Lru4cCvNcdXwdXCC53n9e9H5Jo-F8SSJLXOS2svxopkQ6Inlc_8rJPPc3svbUtbB_MNeO6r0jc-uLpPk2tHcLYYrmAs3XPHnwOy6-URAVNMxLLEB6LGajtAiUxwy563jmM-mBe0DPFQtJH5FWK60w18A2ZG_hMknLK9hUsuBux5yrI9OGMP5oeqFMEsydpakz2PReuqMXr7q-Bp63pGirJYG6KF40PvTt7BGqfe-YDbBMaFBrat_jtp1yQnUjrr8xOcnHSV96XjYrTKS_geIrtm2ZOFjfE6Xh0jSrA8FWgF6lA7-j5L9Ey6hBGIkwy-hU8Lc2wI41ZL61M5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات أمنية إضافية تصل إلى محافظة كركوك لتنفيذ عملية الإعتقال بحق مسؤولين متهمين بقضايا فساد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/80239" target="_blank">📅 19:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80238">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6992ed5645.mp4?token=b_2BMnbZkgQG4jB7cq-9GmsFDtrhzVOlz6Y_hZ-lYU5lLzo9on45UHPAEuahJChxPSx5eccnKxaf-vLsYCH1X9qBcvReRnFRXbcxnMJ3y_wrdD9BqHepNjdx1gcReVB51umLUbfr55ckQF8cURKUuG4T0caF-I77YnUtHGZzUm9y8Ym5jcW1D5hUF0qdIc-oopV9r--4LTANUgKF3JuMJYmMx4Rw4sPIOPzqDxrx1lcrMuzNZRLuBdaFEcF4iD-MeYrJzLLjktUK4ExeolgT3clHjbWHvsTJ9BQAZpVeVTXc4hY1YM7pmTSToaHzBNM4DZCkMvkLwVjjxYJ2li5oMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6992ed5645.mp4?token=b_2BMnbZkgQG4jB7cq-9GmsFDtrhzVOlz6Y_hZ-lYU5lLzo9on45UHPAEuahJChxPSx5eccnKxaf-vLsYCH1X9qBcvReRnFRXbcxnMJ3y_wrdD9BqHepNjdx1gcReVB51umLUbfr55ckQF8cURKUuG4T0caF-I77YnUtHGZzUm9y8Ym5jcW1D5hUF0qdIc-oopV9r--4LTANUgKF3JuMJYmMx4Rw4sPIOPzqDxrx1lcrMuzNZRLuBdaFEcF4iD-MeYrJzLLjktUK4ExeolgT3clHjbWHvsTJ9BQAZpVeVTXc4hY1YM7pmTSToaHzBNM4DZCkMvkLwVjjxYJ2li5oMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
آليات تابعة للقوات الأمنية تدخل إلى محافظة كركوك شمالي العراق، خلال عملية مداهمة وإعتقال عدد من المتهمين بقصايا فساد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/80238" target="_blank">📅 19:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80237">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
‏
السفير الأميركي بالأمم المتحدة:
صبر ترامب على إيران بدأ ينفد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/80237" target="_blank">📅 19:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80236">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd870c00f1.mp4?token=Dpu_pPpymiuU3LdsGTToSfTCH6CVXwvUB8pBCWCnqDccDKE62_VbZfgjPrMgKd3uFE_3wJPCERyNA0ArpRwx4lA2riUPD3Gt8LS1BD9WYu6wh1vHuUA3REI36Kaj22Wvp115UYodnjqTp_oLs5cXLNWRSni9VLCbBvP3C26xVNUEmZePmXKL2pCYbIY84czfAOzrNY5ixLMMl3ra1BV-QSbxcvzQx7N7ZhLRdf6p34piyOxqYgxurP-3U0kW1-SerzHLUpfWkcnc_q-Ak_Qmq66XDyHC3mDGMMva5MeEzTxz8gj0_pg2sxS10E8D8IwmaQMINotD2nbJmd-0e5FxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd870c00f1.mp4?token=Dpu_pPpymiuU3LdsGTToSfTCH6CVXwvUB8pBCWCnqDccDKE62_VbZfgjPrMgKd3uFE_3wJPCERyNA0ArpRwx4lA2riUPD3Gt8LS1BD9WYu6wh1vHuUA3REI36Kaj22Wvp115UYodnjqTp_oLs5cXLNWRSni9VLCbBvP3C26xVNUEmZePmXKL2pCYbIY84czfAOzrNY5ixLMMl3ra1BV-QSbxcvzQx7N7ZhLRdf6p34piyOxqYgxurP-3U0kW1-SerzHLUpfWkcnc_q-Ak_Qmq66XDyHC3mDGMMva5MeEzTxz8gj0_pg2sxS10E8D8IwmaQMINotD2nbJmd-0e5FxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي:
سيتم تشييع جثمان قائد الثورة الشهيد في العاصمة بغداد وثلاث مدن دينية عراقية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/80236" target="_blank">📅 18:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80235">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🇹🇷
نتنياهو حول تركيا:
بالكاد يمر يوم دون أن يدعو أردوغان إلى تدمير دولة إسرائيل.
نأخذ هذه الكلمات على محمل الجد، لأنه إذا كان هناك شيء واحد تعلمناه من تاريخ شعبنا، فهو أنه عندما يقول شخص ما إنه يعتزم تدميرك، يجب أن تأخذه على محمل الجد.
نأخذ هذه البيانات على محمل الجد، وسنلفت انتباه أصدقائنا الأمريكيين إليها أيضًا. نحن لا نتجاهلهم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80235" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80234">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9469bcbd41.mp4?token=HdBSseDSG4Z4k6YHe8finUKJJ_8b_OOma255gQ4hBS37rAt-fIY1NrEumVA1WoBpJIjJXvbXh33k5Yy40mvRC7zrqQWOzlygZ3BRIhWHIHFHIEl7foil4Tank46i1KWQ1AJlAx1UjuJSid6eLEfC65IyM3ir2m1PwtyfGKpzohUaEaxRKlbcJcZDYNsQcg6iixbXCGFW7zHyMu4cgs4ftSaTrKcJA3P71R9r8vymAreZEr1u-5TJjEYPRyiAGWLZ7R6EqlEl4-RxS-xNE9D7SCm-MjFbYLqG-jjV2CESJ_l0Xp0t8DhIw127hhrS-1Pj9u-IoT7JrlwYDdSFvbcQzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9469bcbd41.mp4?token=HdBSseDSG4Z4k6YHe8finUKJJ_8b_OOma255gQ4hBS37rAt-fIY1NrEumVA1WoBpJIjJXvbXh33k5Yy40mvRC7zrqQWOzlygZ3BRIhWHIHFHIEl7foil4Tank46i1KWQ1AJlAx1UjuJSid6eLEfC65IyM3ir2m1PwtyfGKpzohUaEaxRKlbcJcZDYNsQcg6iixbXCGFW7zHyMu4cgs4ftSaTrKcJA3P71R9r8vymAreZEr1u-5TJjEYPRyiAGWLZ7R6EqlEl4-RxS-xNE9D7SCm-MjFbYLqG-jjV2CESJ_l0Xp0t8DhIw127hhrS-1Pj9u-IoT7JrlwYDdSFvbcQzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
آليات تابعة للقوات الأمنية تدخل إلى محافظة كركوك شمالي العراق، خلال عملية مداهمة وإعتقال عدد من المتهمين بقصايا فساد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/80234" target="_blank">📅 18:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a2bae77b.mp4?token=fLALv4YX9azivZuIWCYa513Ho_t2VTuMkXu0MCP9IwEPX4nbR3BBwKSPAblWhMM9ZVHHPwjV64IF75B1EmAMSzFVVZh3wOszBx7BaRnPyvu-gcBJp5pAPpgPlLaQDkr8SlPEcMfkvwsF6dE17rSMYLr2tsAKAv-aqM2UTMmM4po8WnSaIeH34SbuHpKrcU9QLzHDrTlXZabUsUwOGMlklhb_Ar2B2gHexzHiSVaK0bziG13rtED7UXusx8nvi_3wPQ6GbuEpsPc_8Taj08jX9RysO57r0HT1jOpHQEow_42YnM1eSKHjiSVRP6BBh83yR3oUJ725m54JxzwV62_Mjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a2bae77b.mp4?token=fLALv4YX9azivZuIWCYa513Ho_t2VTuMkXu0MCP9IwEPX4nbR3BBwKSPAblWhMM9ZVHHPwjV64IF75B1EmAMSzFVVZh3wOszBx7BaRnPyvu-gcBJp5pAPpgPlLaQDkr8SlPEcMfkvwsF6dE17rSMYLr2tsAKAv-aqM2UTMmM4po8WnSaIeH34SbuHpKrcU9QLzHDrTlXZabUsUwOGMlklhb_Ar2B2gHexzHiSVaK0bziG13rtED7UXusx8nvi_3wPQ6GbuEpsPc_8Taj08jX9RysO57r0HT1jOpHQEow_42YnM1eSKHjiSVRP6BBh83yR3oUJ725m54JxzwV62_Mjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
عناصر الأمن تتجول داخل منازل المسؤولين الذين تم اعتقالهم خلال عملية المداهمة التي تجري من ساعات ليلة البارحة في العاصمة بغداد ومدن عراقية أخرى.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80231" target="_blank">📅 18:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f955f596.mp4?token=GcXVT1kh_F8JJj3WFbWoBZlTYdO415VTROp3s_8RIN5eeJ_ez1q4dFN6nwYMwlpad5gPBUwCQedChFgvIdU60z1k9oNLTu5k37DS8hltFKDe5HnQgOLPdIRJ7Uj4WQYK0aaxdA7vekOCQBq1PECVaFQDogP5qHtFpgDkcHCB1z7MP8l07tI0ILGql94h7LBbpZwc5i84aIyfOtGII3JKA62IqZK71rmqIZ9aSP6HhB-O4W0tUxZ3BNo1HJ1dAS3sWwRu88hpxNJv_Y5KHIAteV940YLoJi_D7-oyFAF4CeXylnqyPwWbTjHKM7X914WGI0h_ckvACUV8Q___djPdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f955f596.mp4?token=GcXVT1kh_F8JJj3WFbWoBZlTYdO415VTROp3s_8RIN5eeJ_ez1q4dFN6nwYMwlpad5gPBUwCQedChFgvIdU60z1k9oNLTu5k37DS8hltFKDe5HnQgOLPdIRJ7Uj4WQYK0aaxdA7vekOCQBq1PECVaFQDogP5qHtFpgDkcHCB1z7MP8l07tI0ILGql94h7LBbpZwc5i84aIyfOtGII3JKA62IqZK71rmqIZ9aSP6HhB-O4W0tUxZ3BNo1HJ1dAS3sWwRu88hpxNJv_Y5KHIAteV940YLoJi_D7-oyFAF4CeXylnqyPwWbTjHKM7X914WGI0h_ckvACUV8Q___djPdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
حريق كبير طال أحد فنادق محافظة أربيل شمالي العراق،؟والدفاع المدني يحاول السيطرة.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/80230" target="_blank">📅 18:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مداهمات في مناطق الكاظمية والعرصات الهندية و الكرادة و البكرية والدولعي طالت مكاتب زياد الجنابي و عالية نصيف و حسن الخفاجي وهند العباسي و مدهمة ومصادرة خيول تابعة لعالية نصيف</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/80229" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd16156d3.mp4?token=g2tPEFUFsconrS8yCukLz7YfT3TFjKYiVbWVtFl5aCItUMboP1Za1ZkHE7BWJkqI6dj-74Yhwsv2wju9vU7DuoQcOp53PbCijHlqZOzyhoozQtf1vmx9U85ulJLArvSJLhF3dDgsiCr_utvOoJa2P1-RjyAE070dk-4yLWcmh8OWzpU2gW_U07QV4lK8Sw9Z6fhlQMjFJwtFI-sJJVFvQB7lXGIdEhDTAWq57mvAnqT4jwTBWgEDrk4lztLVdUkgySGFkxyplGPS69sOp7w7tlAd0Ki_1fdei_8PoUKPntdXRTs3WH6YQOP01vM0Y_WZGnJUfEXjlOlaJk2IcaAzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd16156d3.mp4?token=g2tPEFUFsconrS8yCukLz7YfT3TFjKYiVbWVtFl5aCItUMboP1Za1ZkHE7BWJkqI6dj-74Yhwsv2wju9vU7DuoQcOp53PbCijHlqZOzyhoozQtf1vmx9U85ulJLArvSJLhF3dDgsiCr_utvOoJa2P1-RjyAE070dk-4yLWcmh8OWzpU2gW_U07QV4lK8Sw9Z6fhlQMjFJwtFI-sJJVFvQB7lXGIdEhDTAWq57mvAnqT4jwTBWgEDrk4lztLVdUkgySGFkxyplGPS69sOp7w7tlAd0Ki_1fdei_8PoUKPntdXRTs3WH6YQOP01vM0Y_WZGnJUfEXjlOlaJk2IcaAzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تحلق طائرات الهليكوبتر التابعة لقوات مكافحة الإرهاب وقوات الأمن الكردية في سماء محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80228" target="_blank">📅 17:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مداهمات في مناطق الكاظمية والعرصات الهندية و الكرادة و البكرية والدولعي طالت مكاتب زياد الجنابي و عالية نصيف و حسن الخفاجي وهند العباسي و مدهمة ومصادرة خيول تابعة لعالية نصيف</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/80227" target="_blank">📅 17:47 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
