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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 15:41:04</div>
<hr>

<div class="tg-post" id="msg-84200">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صواريخ تتجه الى العقبة</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/naya_foriraq/84200" target="_blank">📅 15:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84199">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/naya_foriraq/84199" target="_blank">📅 15:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84198">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">صواريخ باتجاه الاردن</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/naya_foriraq/84198" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84197">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انباء اولية عن اطلاق صواريخ من ايران</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/naya_foriraq/84197" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84196">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انباء اولية عن اطلاق صواريخ من ايران</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/naya_foriraq/84196" target="_blank">📅 15:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84195">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUiFwOHz-yvnhAalnqqMLNmVfMyCMoypBmNNkBI3H9P5V92pgKGuokiEKu7MDPXVWFgRa55m0kfja231lABrLYwuXq0iedYvu9tuYh_AIuBi-jSb7SzlDmrpMM5-jaeHC0Q1iJInFVDtunCcc2Ua7xYAORMsJYwQHYGTwx64FDpI3mCFGdkSHxL_m_Evl0-x3ZJrGYWb8l5EhG6JfwSYOjnw7jycILaMMko3e4TQ6tfrbdIHkSX2WJfkbJVTpVZBQCM8JPIGeIlF9RNTIUFkKwjPno3240XhUqBlAg_i3EgfERdArlSeR1X8nnWkHEZwMIkI-qjvV479d3n7Ri1eTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
‏على الجمهوريين إضافة إيران إلى مشروع قانون العقوبات على روسيا. هذا ما أراده ليندسي، وكان سيحدث لا محالة. هام!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/naya_foriraq/84195" target="_blank">📅 15:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84194">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مجلس النواب العراقي يصوت على إعفاء قائد القوة البحرية وآخرين بسبب تقصيرهم بشأن فاجعة قتل الصياد العراقي من قبل عصابات خفر السواحل الكويتية والاعتداء على الصيادين الآخرين.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/naya_foriraq/84194" target="_blank">📅 15:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84193">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
🇰🇼
مجلس النواب العراقي يُصوت على إضافة فقرة على جدول أعماله قراءة تقرير لجنة الامن والدفاع بخصوص استشهاد الصياد العراقي من محافظة البصرة على يد عصابات خفر السواحل الكويتية.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/naya_foriraq/84193" target="_blank">📅 15:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84192">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
🇺🇸
القضاء الايراني:
لم يتم إطلاق سراح أي سجين أمريكي بالمواصفات التي ذكرها ترامب من سجون إيران. السيدة التي يتم الحديث عنها لم تكن سجينة ولم تتهم بالتجسس. ترامب في وضع صعب للغاية ويحتاج إلى إظهار أي إنجاز. حتى خروج مواطن إيراني-أمريكي من البلاد.</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/84192" target="_blank">📅 15:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84191">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇰🇼
‏الكهرباء الكويتية: محطة للكهرباء وتحلية المياه تعرضت لهجوم للمرة الثانية خلال يومين</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/84191" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84190">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇰🇼
‏
الكهرباء الكويتية:
محطة للكهرباء وتحلية المياه تعرضت لهجوم للمرة الثانية خلال يومين</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/84190" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84189">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقجي: كل شيء بدأ بتصور إيران كدولة ضعيفة؛ حيث ساد الاعتقاد بأن هذه الدولة فقدت قدرتها على الردع في المنطقة، وأنها ستلجأ إلى الردع النووي لتعويض ذلك.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/84189" target="_blank">📅 14:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84188">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
🇰🇼
مجلس النواب العراقي يُصوت على إضافة فقرة على جدول أعماله قراءة تقرير لجنة الامن والدفاع بخصوص استشهاد الصياد العراقي من محافظة البصرة على يد عصابات خفر السواحل الكويتية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/84188" target="_blank">📅 14:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84187">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
مصدر في موانئ البصرة العراقية:
- الناقلة Surename الراسية على أحد أرصفة التصدير ستنهي عمليات تحميل شحنتها البالغة 2 مليون برميل مساء اليوم الأحد
- من المتوقع ان تكمل الناقلة Bahamas الراسية على منصة SPM1 تحميل شحنتها البالغة 2 مليون برميل يوم غد الاثنين.
- الناقلة Nissos Heraclea من المؤمل أن ترسو مساء اليوم الأحد لبدء عمليات تحميل شحنتها البالغة 2 مليون برميل.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/84187" target="_blank">📅 14:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84186">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
🇯🇴
خلاف اردني امريكي  الاردن: لا صحة لما نشرته السفارة الأمريكية بشأن إخلاء مطار العقبة ومينائها</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/84186" target="_blank">📅 14:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84185">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
🇺🇸
منظمة الطاقة الذرية الإيرانية:
حكومة الولايات المتحدة الإرهابية والمجرمة، التي لا تملك طبيعة سوى التسلط وانتهاك القوانين، قامت، في عمل عدواني ومتوحش يتعارض مع القوانين الدولية بشن هجوم على موقع بناء محطة دارخوين النووية - أحد رموز عزيمة واكتفاء إيران العلمي - باستخدام عدد من الصواريخ.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/84185" target="_blank">📅 13:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84184">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏السفارة الأميركية في الاردن: إخلاء المطار والميناء البحري بالعقبة جراء تهديد موثوق</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/84184" target="_blank">📅 13:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84183">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:  منذ يوم الجمعة (قبل الحرب بيوم) كانت الأجواء تتجه نحو الحرب. التقيت برئيس الجمهورية يوم السبت في الساعة 8 صباحًا، وأخبرته أن "الأجواء حربية". كنا عادةً نقدم التقارير للسيد حجازي، وكان هو يرسلها إلى القيادة. التقيت بالسيد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84183" target="_blank">📅 13:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84182">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
منذ يوم الجمعة
(
قبل الحرب بيوم
)
كانت الأجواء تتجه نحو الحرب. التقيت برئيس الجمهورية يوم السبت في الساعة 8 صباحًا، وأخبرته أن "الأجواء حربية". كنا عادةً نقدم التقارير للسيد حجازي، وكان هو يرسلها إلى القيادة. التقيت بالسيد حجازي في الساعة 9، وقدمت له تقرير المفاوضات، وعندما كنت أتحدث عن الأجواء الحربية المشحونة، تعرض المكان للهجوم.
كان المجلس الاستراتيجي للعلاقات الخارجية يعقد اجتماعه الأسبوعي المعتاد في ذلك الوقت، وكان الإمام الراحل موجودًا في مكتبه، كما كان الشهيد شمخاني يعقد اجتماع مجلس الدفاع. كان عقد الاجتماعات المتزامنة في ذلك اليوم أمرًا غير غريب؛ ولكن علم العدو بهذه الاجتماعات كان نتيجة لثغرة استخباراتية، والتي ربما لا تزال موجودة.
كان اجتماع الشهيد شمخاني مع القادة في مجلس الدفاع، ومكتب الشهيد شيرازي، ومكتب السيد حجازي، ومكتب الإمام الراحل، كلها تقع ضمن نطاق مكتب الإمام.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84182" target="_blank">📅 13:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84181">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏السفارة الأميركية في الاردن: إخلاء المطار والميناء البحري بالعقبة جراء تهديد موثوق</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/84181" target="_blank">📅 13:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84180">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1J62FvCisZCdwgOgXiMXvkQLOwzqO5xjyVfUbxDjtdz_wDwkFqO5qNrTskc8vs2yT4jLsyMjzNota04ojCo8z3NiN_1DeKVaK5y5kL5fRONym1-KD7mfWVkHFtwePrYZ7Jz-JYKESByoXluw9IOYOP3oe4Lxd7KK1NWtVYIKLWNto2B-DtWpmVcLmm4iTn78NXqGvXc_MroRjUimgLHTBjQg2PMsiJJCa6Yjbr7SGP6urCCtqJg2KQ8rWHJYTdspRjcty6kviE28B_3LNYr6oncn1iUgq4y9woM_fBzLZ_5b4x3FrQszqUKw86d8Cn3IFYznH31P9rwB-hJblR-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارة موسكو في العراق تهنئ المجلس الأعلى الإسلامي بمناسبة عيد التاسيس !</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/84180" target="_blank">📅 13:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84179">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
🇯🇴
‏السفارة الأميركية في الاردن تطلب من رعاياها عدم السفر إلى مطار ومرفأ العقبة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/84179" target="_blank">📅 13:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84178">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
🇯🇴
‏السفارة الأميركية في الاردن تطلب من رعاياها عدم السفر إلى مطار ومرفأ العقبة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/84178" target="_blank">📅 13:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84176">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVuitNMnfsxiA0sqtLWuOFnTbSy6MQfrodS_oDelW8DfubYpYBYQbVSVUwzQJsQ3psaK49NA4XF0-qhnFlQfEDmEUImual2iMlTQj9f5MeQ_YsDJqPPfqsLivojkyaEeafvsXUXxCDKr6hbvHgLIPWdY-cyNdACr4a66RaFS-m3-FWBjPY6i60-37VVWOGw2A2e2eU3Kl7VgdxT9-gNJGMmBTgnjt3RcjU38a0YT3bQOHMbUavDqhSDNhmxW97qJ0sn-xuvT-ClFLndcXNz0H1zGfShHJjq4vbhHZRLMmlMc2FndPA48ToLPLduL25KpqrMeUPR5iSC8n_rZUvhgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0HudP7-6tcSQVZ0k9BQKbuipCafSvCtay3RH9C_G5sQiVEwdqFYXFhvAN5n99ikbUf8zt5bTZ62ngh6eUhrKmjuR1DizMxPOmW8ZEhCz3x6duCvmruJ3ecHEgQCydcPSa6La7GfudSnoTqy7qopD9bGKsE6rYJ5bi6VE7M7nmP7YvDo4MhVD6NdCXmT-RNoPoJImHlCQfoYUahX4M5hDiDVi6BnKd8J-HpfkkqM4bB5dpNK07YbXH4TFpqLNSl_XY_mdQvYxqsdNLc83FofgLHR25cezIWtmQG4aIx5mvTc1r52NGB-BwcygjbSe7fRaD93n1MYkLMd6I6YZc3Stg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇼
لاسباب غير معروفة..
طائرات كويتية تحلق بشكل دائرة بنفس النقطة.
يمكن اعراض القزو هاي
😄</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/84176" target="_blank">📅 13:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84175">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
قوات حرس الثورة الإسلامية البحرية:
- قبل ساعات، حاولت أربع سفن مخالفة، بدعم من الإرهابيين المدعومين من الولايات المتحدة، وتعطيل أنظمة الملاحة، وتجاهلًا لتحذيرات مركز التحكم في مضيق هرمز التابع لقوات البحرية التابعة لحرس الثورة الإسلامية، تعطيل حركة المرور والخروج من مضيق هرمز عبر مسار غير آمن. وقد تعرضت سفينتان من بينها لحادث وتوقفت في مكانها، بينما تراجعت السفينتان الأخريان عن مواصلة المسار.
- تعلن قوات البحرية التابعة لحرس الثورة الإسلامية أن السيطرة على مضيق هرمز تقع بالكامل في يد هذه القوات، وأن المسار الآمن الوحيد هو المسار المحدد والمعلن. كما تؤكد أن أي كمية من النفط والغاز والأسمدة لن تعبر مضيق هرمز إلا بتنسيق وإذن مسبقين.
- السفن التي تتأثر بإنشاءات العدو الأمريكي وتدخل مسارًا غير آمن، ستتعرض بالتأكيد لحوادث.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84175" target="_blank">📅 13:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84174">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1EQ_6Hcf3rqlPS1nRGFhbBV80ZqyhjnaEYyItVVpaorRWBssjV83junmOVoidTsCIcWKnUlR4WBTqfa0OD7QoAJdydHwZN5ap9vQNzpsNZTFTLtaHNKCKD_AGhVKk7fd-6SV2GzjZ4h0RfdMaH6r1FP9jPLDJPa2KWL7KpvW_sAcys1c_8byG54-noqb72UYEqO8qKkxxA_YeqNizMUSG4guFQb2Lj-KHPYw_3CwcmWVqgxH42nm_wz25LbeuMqjeI8JeHVtBeTHVK0A34vCrT2QrTDHCQtFECKr2DAvEA06dGAt5AG1tGgJmkdHEKebxlwVxM2Ve20YcRRMn9zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
ينبغي لنا أن نعتبر طاعة المرسوم الديني والوطني الصادر عن القائد الأعلى للثورة جزءًا مهمًا من دورنا التاريخي في هذه المقاومة الوطنية وفي حكم البلاد.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84174" target="_blank">📅 12:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84173">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ae58319d.mp4?token=PUaTuUmxboH83FB8LDh4MOn9e88S1Ynou_YjqwlKt0uvPcaKEjI2tM-5pjtIfqBjQlSzQqqIHcL1X4Lsl5W2pEZu0POvNkrdLOLeIe6UsOAqkU-YB-Qbelzvf44a1EpQc9hY1_ON5w3GkePMlpXkM_h6leDgyn1QnL1vlGfc92RWwDDHf-Y5JgKA5Am64UauJDGVRVljkYJYv7dy90LUz6fu0sM6Lpz2SJqOtgag7hbylw53WsuSKrrxnufh54m602_ChopZBjqz2Pt5SowSOnUfRrftvVfufvmN16oXWBm08YEQcsDFGXmxQMbHPbWo4DKe0gqwMWnQieKoBheOoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ae58319d.mp4?token=PUaTuUmxboH83FB8LDh4MOn9e88S1Ynou_YjqwlKt0uvPcaKEjI2tM-5pjtIfqBjQlSzQqqIHcL1X4Lsl5W2pEZu0POvNkrdLOLeIe6UsOAqkU-YB-Qbelzvf44a1EpQc9hY1_ON5w3GkePMlpXkM_h6leDgyn1QnL1vlGfc92RWwDDHf-Y5JgKA5Am64UauJDGVRVljkYJYv7dy90LUz6fu0sM6Lpz2SJqOtgag7hbylw53WsuSKrrxnufh54m602_ChopZBjqz2Pt5SowSOnUfRrftvVfufvmN16oXWBm08YEQcsDFGXmxQMbHPbWo4DKe0gqwMWnQieKoBheOoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر سيء للكويت
🇮🇷
🇰🇼
عضو في لجنة الأمن القومي الايراني: يجب أن تعلم الكويت أن وضعها لن يكون طبيعياً بعد انتهاء هذه الحرب. نعتبر الهجمات التي انطلقت من الكويت هجمات مباشرة، ويجب أن تعلم أننا سنتعامل معها بشكل خاص.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84173" target="_blank">📅 12:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84172">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
إلقاء القبض على متهمين اثنين اعترفا بانتمائهما إلى ما يسمى حركة دين السلام والنور الأحمدية المعروفة بحركة اليماني.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/84172" target="_blank">📅 12:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84171">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇲🇱
مقتل 50 عسكريا بهجوم مسلح في مالي</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84171" target="_blank">📅 12:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84170">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سماء البحرين في هذه اللحظات بعد الهجوم الإيراني</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84170" target="_blank">📅 12:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsk3LQzycNB74N8llN25jdyA9dmce4l5xrmu9z9iGypIrmGmNXAYRKe9ZJOCVNee9RYoMC67e4JpwND_4xs3wtSgjChD5Kc5BKrtGzVCaU1VMUPs-Mf8xtHrmtZvGFIvwWV4A-FI2HGmlmFR2ry8PFYNMVkmIAH12fJo_Rsy1atOBgnouQTLuBBFs0L2Oo7esSYJAn35bfmpUtIjzgx_bMTtScTPxUkVIoniHelgu6f8HF_Fdi620STMo2EbGD7p-iBn6BsM0xE1xA-Yc5ybvL2gm62P4-UmRM4Vih6bmzFR2Xx_sTm99zlCh_1EsePB-gb62adt2NIjF63F1qPCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البحرين: نتعرض لهجوم جوي ضخم</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84169" target="_blank">📅 12:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">البحرين: نتعرض لهجوم جوي ضخم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84168" target="_blank">📅 12:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">البحرين: نتعرض لهجوم جوي ضخم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84167" target="_blank">📅 12:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84166">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df9cce2a3.mp4?token=pmBPgEQnhBqy2VpGw6-3s8bl1ycn9oCaLmQ5LKa1gBCXKeTOUt6Mo9qMH2KSAPR8Uc3Du1akg_PBj3FKdbKOk014UCMMyfoIoEYvTA-ICyYIhhNdNFTWmCZBndA5yPy_zIJu9Fxdc5FeaADuKmud28LAs8zepFM4F4cWG7gcTQOovOBv5CNUcE1b0Pk9bft31tD153qRdDUQZEsf1Q66ohNuJUzn7qdkWou7_hBTlaiTvgNuys7YVFBzs6HcrVPs93FWbxwJRekKBbHDSBCk4C3NRlpl8JtmJHVatlM7D7j56-zKZb4Duy2Qws-QgHxqOfpoVwpM3XrwrX6Nvr_Cuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df9cce2a3.mp4?token=pmBPgEQnhBqy2VpGw6-3s8bl1ycn9oCaLmQ5LKa1gBCXKeTOUt6Mo9qMH2KSAPR8Uc3Du1akg_PBj3FKdbKOk014UCMMyfoIoEYvTA-ICyYIhhNdNFTWmCZBndA5yPy_zIJu9Fxdc5FeaADuKmud28LAs8zepFM4F4cWG7gcTQOovOBv5CNUcE1b0Pk9bft31tD153qRdDUQZEsf1Q66ohNuJUzn7qdkWou7_hBTlaiTvgNuys7YVFBzs6HcrVPs93FWbxwJRekKBbHDSBCk4C3NRlpl8JtmJHVatlM7D7j56-zKZb4Duy2Qws-QgHxqOfpoVwpM3XrwrX6Nvr_Cuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد لتدمير طائرة مسيرة من طراز MQ9 تابعة للجيش الأمريكي الإرهابي، وذلك على يد مقاتلي القوة البحرية التابعة لحرس الثورة الإسلامية في منطقة عسلويّة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84166" target="_blank">📅 12:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84165">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilcfs_Zc2bXT18UcWASophHfqeJ6LS5p9gPL3yCGa5QNNamgOeE75w2gr2F7pshZUfwmd_odqPp3S6vjYxGPxRSf3Xar1Oa0MVFPGVR8ts83t_I81sovY5WBPnNgkUTVdQt_wEjyIEgAIoWWKBZ1L0AOsVp6C7gJyjpOsHhks4q6SUGq6J1PprhD--UHk6T7NU9dEkmy65rFSf_c7SAHUzSkRbOWAszIIiMZErFk6nGGwI5MMAz0-6k_tJ61XeqNdTy7eZCd5eMXeGup7J2Vw384Ulxu-bzZgVEoWh2NKWuknxFRwh16Qsq6uMj2iFamF9_WsehgevFeLsuovpKTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة تزود بالوقود أمريكية تنشط فوق مياه الخليج الفارسي قبالة سواحل الإمارات.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84165" target="_blank">📅 12:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84164">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تجدد الانفجارات في البحرين</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84164" target="_blank">📅 11:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bux6Asw0OrUE1JSES8u6IRnIyEBpP4OYz-eCCLiQYaILntxup83PDC_ecthTTO7skiFh2VmqJDfkn9Q_XHqItCxP1VXVyCSIeCUSpGgOLRRpKtXEyOxhG6x14Iv2_rlUZ91FUtbRLijtbc9rpbzW1NDGfaCKXzkuuiSNRgxLXUC_go-_LG-a90ycQkQUKciJoXKqZ27-T9ZQ4fAeG1S8e2C4GNuRP-3VTfgJOzWKFQSiICtrTJFqj-jV8nawZPlsH54qJuRIjP0muoR3sUMmUVGNADn8DBwg5JJeNvWUDMA75LQRlhuGR3aprv-1jA5ZIeOSWK3RBPh_Scew-qvFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84163" target="_blank">📅 11:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84162" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84161">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84161" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84160">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84160" target="_blank">📅 11:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84159">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwUFDO-un3IV-Qz-0NAAATKARwmiH4GouIzH2S41IVx0cmFLlZvWqX4F-4fkL8wNNGCyepyQaKDA84u6EjtdQ59MWYJ30rSghUouP5sVyeNVN4FRw_Opy3VTpZvH107GR2ER-flli9XeRbWt7iDzP7GlR3OM6z0dO4Mq0_Eftb1vky0MDoeQ-qxxqs-GKacQnQTIhgZ4hnDEMOpMr44iWoCfK0G7_hYG76DlsJF-RINKGYqEl_coTn4pYlcC2cLaHwATThzK_v0mqtwF5HNuaxuQFA3tB38aafIw-_tzER9OEOeIBcOqeVffmrpilAb0lNkCcv_NG8d7clsvw3KfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفارات الإنذار تدوي باستمرار</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84159" target="_blank">📅 11:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84158">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84158" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84157">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84157" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84156">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84156" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84155">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84155" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84154">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84154" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84153">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
مراسل نايا: لا يوجد أي حدث أمني في تشابهار وصوت الانفجار قبل قليل يعود لتفجير ذخائر حربية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84153" target="_blank">📅 10:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84152">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سماء الكويت تهتز اثر الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84152" target="_blank">📅 10:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84151">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سماء العاصمة الكويتية الآن بعد الهجوم الصاروخي الإيراني</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/84151" target="_blank">📅 10:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84150">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQCbmi5FVWK6QmIqtcz_vFqSIwwDZCjf8C7qtQo53j7mJi6cGXQ-boHw3L2uf50oEmY_e1MC07VZx7sYjko-t0QL_X0iBNm6MeovUwKOrv8hDAVtpwge31aHPl-Tl-r0ZfrP8MhPeV6j5hcSEQXOD03sZl3l68id7cKqxI_QSkUBLRwaS2PS_FOHYNGbmouTh1EMErKEwH3_p4C_BuqDcpTWdHpV6K1oFHGC7jVUfQbtApcGm0Q-DHm3XmO7e5HwqQKLkC22w0n1az7wp6nDU4UOf-qxolJio1CyVvSjR3hxBrrxWMEWrmikf4XNkLyYlT_WAeYUGAdKUXPminH85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماء منطقة الجهراء في الكويت</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84150" target="_blank">📅 10:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84149">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nniAbCcMpSSVMtuuGCAMPwerbqLZcwcuZBpQb9O91pPA-JKOIa1lpCXAmQUtHBpwo0IyW9PvmTJ8Xw-B9K35HF1uTXQaavgLQElLwGJy5AR1pJmRkz6y1V7s47WGHfcZMzP3to1ajXJNTzIkMxBnGoQ4R1XyXH9atqkgvzoWNZzZyqs10yYI0m0_DKhTxpEwt9h0qLAnLvZA2YQBruTE8z59OoOfKCcz4S1_OFDa7IUC6GganaBqwpnbhWDny7oSzPKG9JtlCMeXE0zQJZ0XIHazKOVTamglnPAvlCGr6cTyo-KbsUPMWJliR5mSv4fjvbrFWMPfht5LfmanVe3XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماء العاصمة الكويتية الآن بعد الهجوم الصاروخي الإيراني</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84149" target="_blank">📅 10:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84148">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248e6a79d1.mp4?token=JezVMkIdVq-DZW71hZvRtcGBxlDfAk4drHdh5rh1yEbm-FhyU1YK7DVp8kfLeyR2xYsw6btysslr5Btf1xy952O9Ye4S47Q-IyFuYe1_PnnvAOHre2Q94we9AwkMc2psYp6aLlHGiK_KBTPYdb__Bliv_Z-mq-NdJsrSbGyQDxu3AMv0V6e7s68aOwyKswCFhJmgq92t0ApIePXtl0EMMrmkn0cn7iMOpGgRyoUlMCMP7Kvtev-97oTTQOujAUEst1Np785LjOjRDYvCcYHBxAo_ACLDQXNFEEHDsRaHZH8wPiklzHa9b4hp3KzLEfFFkbLBTv7wF5w2TIt9M5I45Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248e6a79d1.mp4?token=JezVMkIdVq-DZW71hZvRtcGBxlDfAk4drHdh5rh1yEbm-FhyU1YK7DVp8kfLeyR2xYsw6btysslr5Btf1xy952O9Ye4S47Q-IyFuYe1_PnnvAOHre2Q94we9AwkMc2psYp6aLlHGiK_KBTPYdb__Bliv_Z-mq-NdJsrSbGyQDxu3AMv0V6e7s68aOwyKswCFhJmgq92t0ApIePXtl0EMMrmkn0cn7iMOpGgRyoUlMCMP7Kvtev-97oTTQOujAUEst1Np785LjOjRDYvCcYHBxAo_ACLDQXNFEEHDsRaHZH8wPiklzHa9b4hp3KzLEfFFkbLBTv7wF5w2TIt9M5I45Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء العاصمة الكويتية الآن بعد الهجوم الصاروخي الإيراني</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84148" target="_blank">📅 10:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84147">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84147" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84146">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/84146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/84146" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">إصابة مباشرة في قاعدة علي السالم بالكويت</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84145" target="_blank">📅 10:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84144" target="_blank">📅 10:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84143">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">صفارات الإنذار تدوي في الكويت اثر هجوم جوي ايراني</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84143" target="_blank">📅 10:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84142">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84142" target="_blank">📅 09:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84141" target="_blank">📅 09:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84140">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84140" target="_blank">📅 09:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84139">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇸🇾
دوي انفجارات في محافظة القنيطرة جنوب سوريا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/84139" target="_blank">📅 09:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84138">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇸🇾
دوي انفجارات في محافظة القنيطرة جنوب سوريا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84138" target="_blank">📅 09:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84137">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خوفاً من اغتيال نتنياهو بالطائرات دون طيران.. وافق الكابينت السياسي والأمني على قرار يحظر استخدام الطائرات بدون طيار الشخصية في إسرائيل لمدة 6 أشهر، وذلك خشية من أن تستخدم إيران هذه الطائرات لاغتيال شخصيات.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84137" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84136">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇱
مسؤول صهيوني: واشنطن رفضت طلبا إسرائيليا للانخراط بحرب إيران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84136" target="_blank">📅 08:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84135">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇱
جيش الاحتلال:
قررت القيادة الشمالية ووزارة الدفاع التخلي عن حماية 11 موقعًا عسكريًا على الحدود اللبنانية، بسبب نقص الميزانية. وهذه خطوة واسعة النطاق اتخذها الجيش الإسرائيلي ووزارة الدفاع في الأشهر الأخيرة، حيث استعانوا بمقاول مدني لتنفيذ أعمال حماية مكثفة في المواقع ضد الطائرات المسيّرة المفخخة (بما في ذلك نشر الشباك واتخاذ تدابير حماية إضافية).
وأفاد مصدر عسكري مطلع على التفاصيل أن العمل توقف في جميع المواقع على الحدود اللبنانية لأن وزارة الدفاع أوقفت دفع مستحقات المقاول. إضافةً إلى ذلك، لم تكن هناك ميزانية لتمويل الحماية في المواقع الـ 11 منذ البداية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84135" target="_blank">📅 08:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84134">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية:
نفذت جولة جديدة من الضربات ضد إيران في 18 يوليو عند الساعة 11:30 مساءً بتوقيت الساحل الشرقي للولايات المتحدة (ET)، وذلك بتوجيه من القائد الأعلى للقوات المسلحة (رئيس الولايات المتحدة).
وخلال الليلة الثامنة على التوالي من الضربات الأمريكية، نجحت قوات القيادة المركزية في استهداف منشآت المراقبة الساحلية العسكرية والدفاعات الجوية الإيرانية، والقدرات البحرية، ومواقع تخزين الصواريخ والطائرات المسيّرة، وذلك في إطار مواصلة إضعاف القدرات العسكرية الإيرانية.
كما استهدفت الأصول العسكرية الأمريكية قوات تابعة للحرس الثوري الإسلامي الإيراني، والتي تقول الولايات المتحدة إنها شنت هجمات على أفراد من القوات الأمريكية في الأردن يوم 17 يوليو</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/84134" target="_blank">📅 07:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/84132" target="_blank">📅 06:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84131">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84131" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هزة أرضية بقوة 5 ريختر تضرب محافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84130" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عدوان أمريكي على مدينة شادكان بمحافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/84129" target="_blank">📅 06:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84128">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84128" target="_blank">📅 06:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84127">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هزة أرضية بقوة 5 ريختر تضرب محافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/84127" target="_blank">📅 05:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84126">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/84126" target="_blank">📅 05:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84125">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ed277d98.mp4?token=UUOmtc9KqfhZeCPbeDF_AvPXnqwiwtCytnK5VjuNShlgsJhpxgzXNC3qnypavLeK9hFJ_UkR40N_suHeqPDDfgiHpnR4NfZ2mYNpsgdft9Qt5cS0rw7Aq4h4h7nlI0DKFKyoAZzhimAtV5d3Bn5-hvFehUv7sDl1OinFAXpOKi7ls5Moe94wQlK7mTZnmpgKLS3sMTuTUHousikTzDrjO2_DtruD6gGyx80XZ94XubTrzalEm-hHh9Mlh0OQgs1AkonkkIC9Drw8neFdbH3OpFhktFmq65rYHIE0wcPggamQMR2sCsJhKZezzuqKI5oydzsNT2pU__5aEVHgKRtwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ed277d98.mp4?token=UUOmtc9KqfhZeCPbeDF_AvPXnqwiwtCytnK5VjuNShlgsJhpxgzXNC3qnypavLeK9hFJ_UkR40N_suHeqPDDfgiHpnR4NfZ2mYNpsgdft9Qt5cS0rw7Aq4h4h7nlI0DKFKyoAZzhimAtV5d3Bn5-hvFehUv7sDl1OinFAXpOKi7ls5Moe94wQlK7mTZnmpgKLS3sMTuTUHousikTzDrjO2_DtruD6gGyx80XZ94XubTrzalEm-hHh9Mlh0OQgs1AkonkkIC9Drw8neFdbH3OpFhktFmq65rYHIE0wcPggamQMR2sCsJhKZezzuqKI5oydzsNT2pU__5aEVHgKRtwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Kuwait , Bahrain, Jordan now</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/84125" target="_blank">📅 04:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84124">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عدوان على جزيرة قشم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/84124" target="_blank">📅 04:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84123">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a872fc771.mp4?token=kOoCOkBogP1Qz3Uq5QiHJszYeZ9DQczqO5kgkU6vZYOU2y2egJf9P8eRA3-_jmJZpEaea65Ps8ICzy6B6IgrBmTYH1IvjlqUzLdiu3uJjoHlh9bkyq5QZSVzR67GKXbzM1Y01-coRIpB7DTh46pJvSYi8qadSwchkxNoT-EqMSeAmr2LIN-JEu5tAy2mD9WCPERMe8WrVJJadMYpE-buyOf_VLIX06IoDws0XA9Piaf6YYPCh4gyCqrLMaF4d1S142gTzQMYHABU-hSHWn4sDm3d8W0uOiZbi-07i_-Rgy38-KqWGjGrccuvUJ2-6RXgSpTs3jcf8woi8U3ZGtQunA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a872fc771.mp4?token=kOoCOkBogP1Qz3Uq5QiHJszYeZ9DQczqO5kgkU6vZYOU2y2egJf9P8eRA3-_jmJZpEaea65Ps8ICzy6B6IgrBmTYH1IvjlqUzLdiu3uJjoHlh9bkyq5QZSVzR67GKXbzM1Y01-coRIpB7DTh46pJvSYi8qadSwchkxNoT-EqMSeAmr2LIN-JEu5tAy2mD9WCPERMe8WrVJJadMYpE-buyOf_VLIX06IoDws0XA9Piaf6YYPCh4gyCqrLMaF4d1S142gTzQMYHABU-hSHWn4sDm3d8W0uOiZbi-07i_-Rgy38-KqWGjGrccuvUJ2-6RXgSpTs3jcf8woi8U3ZGtQunA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The peoples of the Persian Gulf today.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/84123" target="_blank">📅 04:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84122">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سماع دوي إنفجارات في الكويت بالقرب من الحدود العراقية وأنباء عن عملية إطلاق صواريخ تجاه أراضي الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/84122" target="_blank">📅 03:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84121">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات في بندرعباس وجزيرة قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/84121" target="_blank">📅 03:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84120">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الهدوء الذي يسبق العاصفة ؟!
ام اعادة ترتيب أوراق لدى الطرفين ؟!
هدنة غير معلنة تدخل بها احد الدول ؟!
الساعات القادمة توضح اكثر الوضع المقبل</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/84120" target="_blank">📅 03:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84119">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374ee63a17.mp4?token=XC_YZdyikDZKL6Kv2qylpwpETPH8xlCFS7d1lvu7WeuZXfQzU9Wxl4UzmDHSq0x08WnsXQOLODeA2fkRWjQgZrA2xpE-q4gvfwdVvU2it7U0lrzUXo6YRYkZXBXtZ0QjWFWlCn9MpNQQjHSDh7BU4r1Q1rau-adk3a2SsRj0E-q6hy0Ja5tiI-85q4iSEad7vOc5cTa2IQYX9idimsELQUckuYR8c6sg9cHa-NwtvbNILmg-1l-kqCYwutOGjhcbFzpiFh2xmrThpZfLCLugdDIOkni7E8j_0nltAnErRxBeTKZ4-hlceDae5uVY-Kk_-TF7IhoJptmnzloei8gFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374ee63a17.mp4?token=XC_YZdyikDZKL6Kv2qylpwpETPH8xlCFS7d1lvu7WeuZXfQzU9Wxl4UzmDHSq0x08WnsXQOLODeA2fkRWjQgZrA2xpE-q4gvfwdVvU2it7U0lrzUXo6YRYkZXBXtZ0QjWFWlCn9MpNQQjHSDh7BU4r1Q1rau-adk3a2SsRj0E-q6hy0Ja5tiI-85q4iSEad7vOc5cTa2IQYX9idimsELQUckuYR8c6sg9cHa-NwtvbNILmg-1l-kqCYwutOGjhcbFzpiFh2xmrThpZfLCLugdDIOkni7E8j_0nltAnErRxBeTKZ4-hlceDae5uVY-Kk_-TF7IhoJptmnzloei8gFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج الوضع عن السيطرة في أعزاز بعد استنفار أبناء المدينة لصد إقتحام عناصر عصابات الجولاني الإرهابية.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/84119" target="_blank">📅 03:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84118">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b8eb9b9d.mp4?token=DR2QpGzax5Ix6ndpZ2irA6OgxVbMNRSHShGRElayL93LKFT47LhFl8Mp-pnUkgJygjqHIwHAv9MCG6zDNZUpcKk_uo76-iCo7UZ4hGN56uOuU-FVpj1d2nf6odHBIL6ygMobeByJ4vU0EwNacei7qNv3I1AdzZj-BHco4hxmX75gU5nLwn_DjwKJhPmG5MJ2ET1EWfiko5hMDcYJNG9Xb8Tb9Di2ybtABLiZ03iW3Xmba3c4emVTSpVZFjKNiwnAvzweIQk3uCTAUM0mUq9O1GUy9oe40Kfjux105vU4pywJnc4w-evDl9U0AOLNzt69_7JNLfglMv5J5T5eB1b0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b8eb9b9d.mp4?token=DR2QpGzax5Ix6ndpZ2irA6OgxVbMNRSHShGRElayL93LKFT47LhFl8Mp-pnUkgJygjqHIwHAv9MCG6zDNZUpcKk_uo76-iCo7UZ4hGN56uOuU-FVpj1d2nf6odHBIL6ygMobeByJ4vU0EwNacei7qNv3I1AdzZj-BHco4hxmX75gU5nLwn_DjwKJhPmG5MJ2ET1EWfiko5hMDcYJNG9Xb8Tb9Di2ybtABLiZ03iW3Xmba3c4emVTSpVZFjKNiwnAvzweIQk3uCTAUM0mUq9O1GUy9oe40Kfjux105vU4pywJnc4w-evDl9U0AOLNzt69_7JNLfglMv5J5T5eB1b0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عجلة في منطقة كلار بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/84118" target="_blank">📅 03:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84117">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">أنباء عن دوي إنفجارات جديدة في أربيل</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84117" target="_blank">📅 03:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84116">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a3a31de26.mp4?token=Xh8ac90q_QrXv_VmaBArfuSs4BMoIlKpV8Wjdp7fO0FFN3LylvNOZIbr3WfelBf95c2D2h0dH1-1FMECrLCJu3vs0gpvmTig-uDFc9ofw3Rj2MzviIVE8tGVDgCFT24K3Gx8A3q72_5KQB0Fn-5DkR93Xy8CSbo--NF9wBkvk2_caGuIYM78ezq-r5uRTxL7UQ6dQh8bgFd7frV-QMP_MYWYwO0kQd_DcgOez5iU6aVewHc15G0lGIDH4qoehpoMDCmiflemznGaFlV3-1OWQYfBA_n4a_evKm6LggrCtJe5A37kiuLNpnSxhLwU9ULuwzE7YAy-JSTto0Qn7GKXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a3a31de26.mp4?token=Xh8ac90q_QrXv_VmaBArfuSs4BMoIlKpV8Wjdp7fO0FFN3LylvNOZIbr3WfelBf95c2D2h0dH1-1FMECrLCJu3vs0gpvmTig-uDFc9ofw3Rj2MzviIVE8tGVDgCFT24K3Gx8A3q72_5KQB0Fn-5DkR93Xy8CSbo--NF9wBkvk2_caGuIYM78ezq-r5uRTxL7UQ6dQh8bgFd7frV-QMP_MYWYwO0kQd_DcgOez5iU6aVewHc15G0lGIDH4qoehpoMDCmiflemznGaFlV3-1OWQYfBA_n4a_evKm6LggrCtJe5A37kiuLNpnSxhLwU9ULuwzE7YAy-JSTto0Qn7GKXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاول مرة لم ينطلق اي صاروخ من الكويت حتى اللحظة باتجاه ايران ؟!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/84116" target="_blank">📅 03:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84115">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">لاول مرة لم ينطلق اي صاروخ من الكويت حتى اللحظة باتجاه ايران ؟!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/84115" target="_blank">📅 03:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84114">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2aeddf6b9.mp4?token=dFbny34ySGwGfEEBFBwxQ-mhcNSj95xXK19IO0q3Rr3k3dDSXPi6oltjGQjmNbB_DoQlebdCFDktLHlezW3_cL7koFPRlClXkCGz1UD-UZO1d9O8Y9XC5brObnPlvcAS6F8DePQaHD6s0a0BRQUzm9blFxka7Ghfdu0ux_3e3_zoBh6bOn-CgPy-pvlrERtiE92FHdX6rs2WA55csRh1zu0SYor_9oTBTq0LRvSmKXiTw-sugabvJzcboQ-hxuSGp3tpRYedYoROCOvUpKXNbsVElJOWTFa74WBlwwmGF-AHGEnMBSLCcTBsuBywB7-skCgnIXVA_JiU7hJzDJkRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2aeddf6b9.mp4?token=dFbny34ySGwGfEEBFBwxQ-mhcNSj95xXK19IO0q3Rr3k3dDSXPi6oltjGQjmNbB_DoQlebdCFDktLHlezW3_cL7koFPRlClXkCGz1UD-UZO1d9O8Y9XC5brObnPlvcAS6F8DePQaHD6s0a0BRQUzm9blFxka7Ghfdu0ux_3e3_zoBh6bOn-CgPy-pvlrERtiE92FHdX6rs2WA55csRh1zu0SYor_9oTBTq0LRvSmKXiTw-sugabvJzcboQ-hxuSGp3tpRYedYoROCOvUpKXNbsVElJOWTFa74WBlwwmGF-AHGEnMBSLCcTBsuBywB7-skCgnIXVA_JiU7hJzDJkRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر لنايا   تدمير طائرة من طراز F15 E نتيجة الهجوم الإيراني على قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84114" target="_blank">📅 02:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84113">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مصدر لنايا
تدمير طائرة من طراز F15 E نتيجة الهجوم الإيراني على قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/84113" target="_blank">📅 02:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84112">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇷🇺
مجددا الجيش الروسي يدك أهداف للبنديرين في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84112" target="_blank">📅 02:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84111">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مصدر إيراني: لا وجود لعدوان على محافظة أراك الإيرانية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84111" target="_blank">📅 02:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d8e8f1b2.mp4?token=M6PjloVahEU7tTVorfjeH24XMPViz-0mpQfvLP8-DY8JulMfTtpnMGcZFWIcthQVGXrJ3zJ-AoXac09SLG9cS_XfF4tUPlzpZV_ZY-RvAy1vQIxkCJFq_eqOIkYYnMSIDW-nRSR1QOcr9DfY_S6fqvRwYOk3DoGYhMMATNMP6dDW-OB0OPelEDWtDFxgd379B76AtaWz-djZvVDIHmFZNLItMSCtDwd0maVqfU7Abd8y6xVlrImbAyju0KiVb4AVTZLuQ4TpAEwrzMrdInkiDlzkAscTN9tucD1hEeeI3T0wUAtd4bAMkivOwdPfnLGhHIZCA0-lwNfUE8Cuvjryow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d8e8f1b2.mp4?token=M6PjloVahEU7tTVorfjeH24XMPViz-0mpQfvLP8-DY8JulMfTtpnMGcZFWIcthQVGXrJ3zJ-AoXac09SLG9cS_XfF4tUPlzpZV_ZY-RvAy1vQIxkCJFq_eqOIkYYnMSIDW-nRSR1QOcr9DfY_S6fqvRwYOk3DoGYhMMATNMP6dDW-OB0OPelEDWtDFxgd379B76AtaWz-djZvVDIHmFZNLItMSCtDwd0maVqfU7Abd8y6xVlrImbAyju0KiVb4AVTZLuQ4TpAEwrzMrdInkiDlzkAscTN9tucD1hEeeI3T0wUAtd4bAMkivOwdPfnLGhHIZCA0-lwNfUE8Cuvjryow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مايسمى "الجيش الوطني الكردستاني" الإرهابي يعلن عن تعرض مقراته في أربيل والسليمانية إلى هجوم واسع.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/84110" target="_blank">📅 02:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b7743d603.mp4?token=ZcFmz7oQVAh6TiIVOLmqtYHTu-Z6LI8_-lZFME6MXvwNjN3I2pgq1f968ItL8dDaAxyuIk1sZvrThwV2PteAzTNu9SnPh837nrxVKj_vxbnvQd5Y0EbupGsY95wszvByTAwR30hnBGg7pM2vPAgolAFdadyeu4KkMJbseU_1S27GgP4iduFxGhHnGZ5CR-dFvr9S7H_ogIsTS_DqYuBQw9BcA5SJkKRo8_8i7gWJJaQrZC_CepUkBUwrJl2EDmv3C0yz9FRQ_-Cf97mzeZUXXCb7_o6G9HD2QGzD7fms1YdwyfYuqCVavY87CPa5Pz5kf1cUmC5pcyi767hGHmzfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b7743d603.mp4?token=ZcFmz7oQVAh6TiIVOLmqtYHTu-Z6LI8_-lZFME6MXvwNjN3I2pgq1f968ItL8dDaAxyuIk1sZvrThwV2PteAzTNu9SnPh837nrxVKj_vxbnvQd5Y0EbupGsY95wszvByTAwR30hnBGg7pM2vPAgolAFdadyeu4KkMJbseU_1S27GgP4iduFxGhHnGZ5CR-dFvr9S7H_ogIsTS_DqYuBQw9BcA5SJkKRo8_8i7gWJJaQrZC_CepUkBUwrJl2EDmv3C0yz9FRQ_-Cf97mzeZUXXCb7_o6G9HD2QGzD7fms1YdwyfYuqCVavY87CPa5Pz5kf1cUmC5pcyi767hGHmzfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعزيزات عسكرية ضخمة تابعة لعصابات الجولاني الإرهابية تصل مدينة أعزاز في محافظة حلب السورية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84109" target="_blank">📅 02:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
🇺🇸
وول ستريت جورنال :
التقارير تعلن عن تضرر عدد من الطائرات الأمريكية، المأهولة وغير المأهولة، جراء الهجوم الإيراني على قاعدة موفق السلطي الجوية في الأردن، والذي أسفر أيضاً عن مقتل جنديين أمريكيين وإصابة آخرين. وقد تم نشر مئات من الأفراد الأمريكيين وعشرات الطائرات مؤقتاً في القاعدة لشن غارات جوية على إيران. ويعكس هذا الهجوم تركيزاً متزايداً على استهداف الأصول الجوية الأمريكية مع استمرار تصاعد حدة الصراع.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84108" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb5d1ee13.mp4?token=j0GwvjjcV_WLVn0r0LSeYw2Vdpa3a9J5t2W2w6RovYQbaOsWttR96NkOWr8Q3gidFyrXzSnzJos0KDJmE7_UobeHHfLBsyVTagHXDhZQK_TlnhLlPq1LJJshNOakvllgMjqhpSWk9Jk3KoeHNeZ0KqLx9K2kP1ugmnWI-XY8VMl2D0xcplJ1_tZu51J2ANwHQiOzwjWA8W3UTB4R8EaLeFWLB9J-2fgM-tq8L485KbB7NOB6b2_G0ZUkom9I1UEXOs9LRQPA0agvzcJHlPZSv_JiH9YtnPtbi-7J1o5OnOVOZo_jkGILo3-zzXN1WI40t8coYrQQnLXrZh7ezhXe6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb5d1ee13.mp4?token=j0GwvjjcV_WLVn0r0LSeYw2Vdpa3a9J5t2W2w6RovYQbaOsWttR96NkOWr8Q3gidFyrXzSnzJos0KDJmE7_UobeHHfLBsyVTagHXDhZQK_TlnhLlPq1LJJshNOakvllgMjqhpSWk9Jk3KoeHNeZ0KqLx9K2kP1ugmnWI-XY8VMl2D0xcplJ1_tZu51J2ANwHQiOzwjWA8W3UTB4R8EaLeFWLB9J-2fgM-tq8L485KbB7NOB6b2_G0ZUkom9I1UEXOs9LRQPA0agvzcJHlPZSv_JiH9YtnPtbi-7J1o5OnOVOZo_jkGILo3-zzXN1WI40t8coYrQQnLXrZh7ezhXe6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إتساع رقعة الإشتباكات في مدينة أعزاز بمحافظة حلب السورية</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/84107" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84106" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8s2ELqTulT3mfWVbFOd9hUwU_37UBOggxjZzbEGiSAK1DO-EBBKsH2e-SWXSDvn_qAX9rmj4Yjjcnz1f4BE73JdOQLDcgRcrwbJ6UvQ_Pz2Gkx_nKPnceYDAaMrnbUZk3-QgDXRbHccPJN1XywBTxIYGXS3wC93OAhbaZDyU5cL4Wscsyd4PauZ4cmfO7x8Gf4tF9afv22KzkTzXiT--6dffrHR59WlCSm4nrMMM6tpmn8jVNpK_88YUY4i3vAmZgPdZnSr5Jmm-h6y-GhFlvH4pxMf6ti0Mr08Rbbh7PhsAaKpfnzB12GWybXXFfk_y1ig5qt_pRdJa2mtwJ4Ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الدفاعات الجوية الأردنية ترفع أقصى مستويات الخطورة</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/84105" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47edf26487.mp4?token=WV_eqILTajm3IK1MbFUdXHMDMeSyr-_3Ji9IjYxiYOqYTdOgsIb-PEhg81Rz1X57l_nYe6jLc6-VQ9ebmtvGoMMiqmEafQpuSdW_v1rpken7N-Wrk5yEkMqiDF-JQcSYTRwPpPPu2KGDy7-PMrgPlmP4aoBjA8YLjk6VknV6jD_ctrkx-mKhslPmt19eFA_YZzvq04xKwe492d13_dppfN82LL8phBn5Ymv2FsDiFStso587jF4I1A8oXZ1jyUaYy8miZqduN77QzNvtelrR41F3cmxh4bMjoaKMM7bdZfRgApjtGpPJWvohV2SgOCqW75uTi8FP06BTRTUA7Bukzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47edf26487.mp4?token=WV_eqILTajm3IK1MbFUdXHMDMeSyr-_3Ji9IjYxiYOqYTdOgsIb-PEhg81Rz1X57l_nYe6jLc6-VQ9ebmtvGoMMiqmEafQpuSdW_v1rpken7N-Wrk5yEkMqiDF-JQcSYTRwPpPPu2KGDy7-PMrgPlmP4aoBjA8YLjk6VknV6jD_ctrkx-mKhslPmt19eFA_YZzvq04xKwe492d13_dppfN82LL8phBn5Ymv2FsDiFStso587jF4I1A8oXZ1jyUaYy8miZqduN77QzNvtelrR41F3cmxh4bMjoaKMM7bdZfRgApjtGpPJWvohV2SgOCqW75uTi8FP06BTRTUA7Bukzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إتساع رقعة الإشتباكات في مدينة أعزاز بمحافظة حلب السورية</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/84104" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭐️
مايسمى "الجيش الوطني الكردستاني" الإرهابي يعلن عن تعرض مقراته في أربيل والسليمانية إلى هجوم واسع.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/84103" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQLxhFM8oFSUoSmVuZoQGAFW7wpss8GNCQzZ5z0fACmt8u1g5haIYtg48zQDWSo-gV2haV4gzchvmigNYlTYFEykCHMC1ZsMfb6zE58PNh-Dt00WOskf6ceCwnSPWk0HPvnUXBp3Y-qMZGpPl55OpB7NAdZ7iDAYEea-KQkgYZTWq5EpEtupSKKLqzoXmzPep5EuJgUrtdeebIzVp-ZlHo1qnWW4Zitw1KpCEzfUpLV3g7T5tJnx2h2dbOLwdNp313aKo67KTte5t8HeM2Vga57joMejavyxq4_-kqH32X9zrQhr7YN-BnqSY8iG9UlsM0FZC2t6gROJp4kjr3j2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواطنة كويتية تطالب بالعطلة وتعطيل الدوام بسبب صفارات الإنذار نتيجة العدوان الإيراني القققاشم .</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84102" target="_blank">📅 02:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84101">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات ضخمة في العاصمة الأوكرانية كييف</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84101" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84100">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سماع دوي انفجار مجهول في محافظة الموصل شمالي العراق</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84100" target="_blank">📅 02:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84099">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9c455424.mp4?token=RC62oEL5YXceBdJWyfdMOHpp5B6J3QTaLUv67R2fIxHSSsVlcY2A8YQQR_W6FAsZsNGAkZLHT4TGWkGzPuiz869ze0JEXt7nVIFomy4RjteJ3MVHKYMXXjD9GiSn47vg2vveifzb1cdk-jg73M-z37gh_hkmy32vYsnpjeYKaiQ49yxNo0D-JjnXkmgNHDGBvYxD7RitG5T1Qlai6EATUoqhr8JgMwHBK4bwa9212pyLf1D3ZE3isR1_-skDYV060zWZ7uCs9-0hfjrBFyfvNwvPr1Y5EfWdzyxTQ3iX_1pFK4rigamOAZQ2I6riB-yWx4g3xXd5mS5d9baKjxhJ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9c455424.mp4?token=RC62oEL5YXceBdJWyfdMOHpp5B6J3QTaLUv67R2fIxHSSsVlcY2A8YQQR_W6FAsZsNGAkZLHT4TGWkGzPuiz869ze0JEXt7nVIFomy4RjteJ3MVHKYMXXjD9GiSn47vg2vveifzb1cdk-jg73M-z37gh_hkmy32vYsnpjeYKaiQ49yxNo0D-JjnXkmgNHDGBvYxD7RitG5T1Qlai6EATUoqhr8JgMwHBK4bwa9212pyLf1D3ZE3isR1_-skDYV060zWZ7uCs9-0hfjrBFyfvNwvPr1Y5EfWdzyxTQ3iX_1pFK4rigamOAZQ2I6riB-yWx4g3xXd5mS5d9baKjxhJ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالتزامن مع الهجمات الأمريكية على ايران
التلفزيون الكويتي يشغل إشعار ترفع معنويات المواطنين امام العدوان الإيراني القاشم على الكويت " يا كويت لا تخافين يا كويت "</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/84099" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
