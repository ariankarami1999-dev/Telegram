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
<img src="https://cdn4.telesco.pe/file/T79fQy2xNdf7XKe8mAFLIQI13Kaqkg-E3s4XLQsSocZ8jYGdVXmaYs6rozGWqliSxBcEpC6Vscnv7svcaN8hmo8JXwNrt-1_halc0Px1SgRsO28oGFMFYR7pMzX08jeSxtG5m2V2wVg-JKFZ5wSxROtGXsBSihPye-_tKjZnhX5Zqsy9khLOGpjHi6nWy2Zh8kwad72TgI3aKAHfhWLF1SO4gfX9qzI-1WMd8UkjknU9RTt9KgZWGoMQ8_oIPCs50ebjkBNPUA2yaLsUxgzy5igXgbSq-gXN1iJx7PgSytaxYeIugpKexZorKtSZ9WlOkBD29qUvrB7dYjc1ucmuzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 269K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 13:01:50</div>
<hr>

<div class="tg-post" id="msg-88548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
🇺🇸
دوي صافرات الإنذار بالسفارة الأميركية في بغداد وسط حالة من الرعب تصيب سكان مجمع بغداد رزدنتي الملاصق لمجمع السفارة !</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/naya_foriraq/88548" target="_blank">📅 12:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88547">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1481148818.mp4?token=t22N30PBKFlS5lxBhiSf23Iwj8JgZm5Hd_Ktdw9P1A4QG1zbe_MRULQL8MmHIvzhEXkRS04xICtj7qlo6xAGqzHo1okd7GX12yH3q5WS-l3kHQbohTR3QFg-81D2SSs4_Liop_khcnn5FSLJRJ9LWt5QGUXKEx9nTK5Kh4qyolldsVw-Ly6Hrm87C8SQ2Wu9V1OBVYMlWLw9w5_nxLCQlnRCS2QoBApQ22MBv6cZ41UAX3xxfqi6v3XTuCG5OxuGF8Mz5zbPWNl-ktWit0HGdvLeivl9NuUkblAE36MfAKGX-8ta4Hb2igNwIAs69qx6XFbpbmyPdMZXxIBqsurHTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1481148818.mp4?token=t22N30PBKFlS5lxBhiSf23Iwj8JgZm5Hd_Ktdw9P1A4QG1zbe_MRULQL8MmHIvzhEXkRS04xICtj7qlo6xAGqzHo1okd7GX12yH3q5WS-l3kHQbohTR3QFg-81D2SSs4_Liop_khcnn5FSLJRJ9LWt5QGUXKEx9nTK5Kh4qyolldsVw-Ly6Hrm87C8SQ2Wu9V1OBVYMlWLw9w5_nxLCQlnRCS2QoBApQ22MBv6cZ41UAX3xxfqi6v3XTuCG5OxuGF8Mz5zbPWNl-ktWit0HGdvLeivl9NuUkblAE36MfAKGX-8ta4Hb2igNwIAs69qx6XFbpbmyPdMZXxIBqsurHTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حادث سير مروع في محافظة أربيل شمالي العراق ؛ مقتل 6 وإصابة أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/naya_foriraq/88547" target="_blank">📅 12:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر قالیباف:  دور إيران والعراق في إرساء النظام الإقليمي حاسم.  لقد أطلقت أمريكا حربًا ضد إيران بهدف الإطاحة بالنظام الإسلامي وتوسيع هيمنتها في غرب آسيا والعالم الإسلامي، ولكن بفضل دماء الشهداء وبجهود الشعب الإيراني الشجاع وجهود…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/naya_foriraq/88546" target="_blank">📅 12:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر
قالیباف:
دور إيران والعراق في إرساء النظام الإقليمي حاسم.
لقد أطلقت أمريكا حربًا ضد إيران بهدف الإطاحة بالنظام الإسلامي وتوسيع هيمنتها في غرب آسيا والعالم الإسلامي، ولكن بفضل دماء الشهداء وبجهود الشعب الإيراني الشجاع وجهود جبهة المقاومة، لقد منيوا بهزيمة واضحة، وأقر بذلك العالم أجمع.
إن انسحاب القوات الأمريكية المتحالفة من العراق هو مصدر فخر تاريخي للحكومة والشعب العراقي، ونأمل أن يتحقق هذا الانسحاب بشكل كامل من الأراضي والجو العراقي.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/naya_foriraq/88545" target="_blank">📅 12:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇱
نتنياهو: لا يمكن التوصل إلى اتفاق دبلوماسي مع إيران.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/naya_foriraq/88544" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔻
إعلام العدو:
من يتوقع أن ترفع إيران الراية البيضاء فهو مخطئ، فهذا ليس من أيديولوجيتهم، وليس في حمضهم النووي، وأعتقد أن ما يفعلونه حاليا، هو أنهم يستعدون سرا للهجوم الكبير الذي يريدون شنه ضد الولايات المتحدة وضد حلفائها في المنطقة قبيل انتخابات التجديد النصفي.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/naya_foriraq/88543" target="_blank">📅 12:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇱
نتنياهو:
لا يمكن التوصل إلى اتفاق دبلوماسي مع إيران.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/naya_foriraq/88542" target="_blank">📅 12:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4 ريختر تضرب قضاء بنجوين في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/88541" target="_blank">📅 11:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
مناطق شرق مضيق هرمز وشمال المحيط الهندي وبحر العرب وبحر عمان تخضع لسيطرتنا العملياتية.
السفن تخضع لمراقبتنا قبل وصولها لمضيق هرمز بمئات الكيلومترات ويمكنها العبور إذا حصلت على إذننا.
قواتنا البحرية لم تسمح لسفن العدو العسكرية بالاقتراب من سواحلنا.</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/naya_foriraq/88540" target="_blank">📅 10:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
رويترز:  انخفضت صادرات قطر من الغاز الطبيعي المسال بنسبة 96٪ بعد إغلاق مضيق هرمز بشكل فعال، حيث تم تصدير 18 شحنة فقط مقارنة بـ 509 شحنة في العام السابق.  فقدت قطر ما يقرب من 24 مليار دولار من عائدات الغاز، بينما تساهم زيادة صادرات الغاز الطبيعي المسال الأمريكية…</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/naya_foriraq/88539" target="_blank">📅 10:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
رويترز:
انخفضت صادرات قطر من الغاز الطبيعي المسال بنسبة 96٪ بعد إغلاق مضيق هرمز بشكل فعال، حيث تم تصدير 18 شحنة فقط مقارنة بـ 509 شحنة في العام السابق.
فقدت قطر ما يقرب من 24 مليار دولار من عائدات الغاز، بينما تساهم زيادة صادرات الغاز الطبيعي المسال الأمريكية في سد جزء من هذا النقص.
في الوقت نفسه، تبلغ مستويات تخزين الغاز في أوروبا أدنى مستوى لها في هذا الوقت من العام، مما يزيد من خطر ارتفاع الأسعار مع اقتراب فصل الشتاء.</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/naya_foriraq/88538" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
في مظهر غير حضاري..
ساحات الإحتفال بالمولد النبوي الشريف بمحافظة أربيل شمالي العراق تتحول إلى مكب للنفايات!!</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/88537" target="_blank">📅 10:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
الإعلام الأمريكي:
تم إخلاء يائير نتنياهو سرًا من ميامي قبل عدة أشهر، وذلك بعد اكتشاف خلية إيرانية كانت تراقبه في اللحظات الأخيرة.
تم تهريبه بسرعة كبيرة لدرجة أن أغراضه بقيت خلفه، بعد تقديرات تشير إلى أن الخلية الإيرانية كانت بالفعل "موجودة" في منطقة ميامي.</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/88536" target="_blank">📅 09:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
🇮🇷
إن بي سي:
تسببت الهجمات الصاروخية والطائرات المسيرة الإيرانية في أضرار بمليارات الدولارات لمواقع الاستخبارات الأمريكية ومعدات المراقبة في جميع أنحاء الشرق الأوسط.
لقد كشفت هذه الهجمات غير المسبوقة عن نقاط ضعف في دفاعات القواعد الأمريكية وأجبرت المسؤولين على إعادة التفكير في كيفية حماية المنشآت الحساسة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88535" target="_blank">📅 01:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88534">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
🇸🇦
مسؤول في الإدارة الأمريكية:
إدارة ترامب أحالت إلى الكونغرس اتفاقاً مع السعودية بشأن الطاقة النووية المدنية.
ترامب لا يزال يعتقد أن الاتفاق النووي مع السعودية لن يتقدم إلا إذا انضمت السعودية إلى اتفاقيات ابراهام و اعترفت بإسرائيل.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88534" target="_blank">📅 01:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88533">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2ae12376.mp4?token=pkqqpJrGPqkY6xYhBHhJ0jUH6PHAMp4vqieCtwU_ZbuPj936aPZKROFtdnS0h-9cQcs1hMzYrUbE8gz1VLa1d3dLLt1SCiOusGUlQuHamctujEoEzNp4eIoIPEggtz3fhPS7ym7G3rfDboRmuG6ve3eb75aJhwpPlZ-ZUCMGhfVXEy9jdIC2Q80mEfMkXROl6UrDOA-mWV92uvgHgQdnavAexxiYjB6Uf5AC_SSMypj4DaV5s4E9lAH_En4Qxg732BvjK3m86saN1B2QrER3XgBw-YfBs5l3X3StO74PaaJ8Zk9RT2TqzSQT6bfp3sC9vRE2MAqnaIGrzA91--dr1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2ae12376.mp4?token=pkqqpJrGPqkY6xYhBHhJ0jUH6PHAMp4vqieCtwU_ZbuPj936aPZKROFtdnS0h-9cQcs1hMzYrUbE8gz1VLa1d3dLLt1SCiOusGUlQuHamctujEoEzNp4eIoIPEggtz3fhPS7ym7G3rfDboRmuG6ve3eb75aJhwpPlZ-ZUCMGhfVXEy9jdIC2Q80mEfMkXROl6UrDOA-mWV92uvgHgQdnavAexxiYjB6Uf5AC_SSMypj4DaV5s4E9lAH_En4Qxg732BvjK3m86saN1B2QrER3XgBw-YfBs5l3X3StO74PaaJ8Zk9RT2TqzSQT6bfp3sC9vRE2MAqnaIGrzA91--dr1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الولايات المتحدة
: تحطمت مروحية في ولاية كنتاكي تابعة للجيش من طراز UH-60 Black Hawk، وكان على متنها أربعة أشخاص.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88533" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88532">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
صرح وزير الخارجية ماركو روبيو لعدد من نظرائه الأجانب في الأيام الأخيرة بأنه "في الوقت الراهن" لا يُتوقع أن تشنّ الولايات المتحدة ضربات جديدة ضد إيران، وأن تُركّز على الضغط الاقتصادي.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88532" target="_blank">📅 01:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88531">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ff577c2b.mp4?token=uQLtyuRmySRAlO9ZOPfYH1rEA0aMi_hJ1J8i-ld_illGwgQk4HekbGZ2C2EuXJxARpF3exmWgtZ5g1HB-CPwifmRof6ZjIXchdIulbTCmN1TCyCPby2tqX80iUriWTmOENdW1X8wAti2QNDZiZrMNKNTaP6offSx1uudna0NcQdzMwghTQZ84higyy4yecXgDCu8pME9puJ_G54RGYV4Y6nItTZJE14F0guHVU342CgBdnQM3KGwCTa2lRgdAGdTMRTBOZ9s9HC9NgcluvKFmZdcoiFm4dnSsD_ZuiQ_ht37OgY8ZBp5aB6qm5Vt4EFjqvdynU5WH9p3XvffZ-I5fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ff577c2b.mp4?token=uQLtyuRmySRAlO9ZOPfYH1rEA0aMi_hJ1J8i-ld_illGwgQk4HekbGZ2C2EuXJxARpF3exmWgtZ5g1HB-CPwifmRof6ZjIXchdIulbTCmN1TCyCPby2tqX80iUriWTmOENdW1X8wAti2QNDZiZrMNKNTaP6offSx1uudna0NcQdzMwghTQZ84higyy4yecXgDCu8pME9puJ_G54RGYV4Y6nItTZJE14F0guHVU342CgBdnQM3KGwCTa2lRgdAGdTMRTBOZ9s9HC9NgcluvKFmZdcoiFm4dnSsD_ZuiQ_ht37OgY8ZBp5aB6qm5Vt4EFjqvdynU5WH9p3XvffZ-I5fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88531" target="_blank">📅 00:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88530">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd76295dc.mp4?token=iQxpkfgVsNL1MAQ1cvdmEKprnkA77Eslok6POEJAdNnNQ-KrZgFCxM6w1KfZOpIpkslgaLt6nVbxmSwWpLixbPWeXEVZSt35gQ60Zh7U2vdrI1znGERVLT4rAJee8FchoEdTLp5suxrAzbkRu7HfNp6Vuz4d3hNG43fjsRQwYa_6H4igX25JOBfYKlSpQFeNrjpHOV8PaZdALSrUQt51veOC5nH2g7WSJYsCj78klgMgYVBvyw5y9afAk8P92EqLsiSvVAr5eErvMo-sX5WI-Tkwy-_37LStD-nVqBkWNXRFIU9JmixXn4BZlWNEW_LrjH2D6l6RYPxrRnuo5kq8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd76295dc.mp4?token=iQxpkfgVsNL1MAQ1cvdmEKprnkA77Eslok6POEJAdNnNQ-KrZgFCxM6w1KfZOpIpkslgaLt6nVbxmSwWpLixbPWeXEVZSt35gQ60Zh7U2vdrI1znGERVLT4rAJee8FchoEdTLp5suxrAzbkRu7HfNp6Vuz4d3hNG43fjsRQwYa_6H4igX25JOBfYKlSpQFeNrjpHOV8PaZdALSrUQt51veOC5nH2g7WSJYsCj78klgMgYVBvyw5y9afAk8P92EqLsiSvVAr5eErvMo-sX5WI-Tkwy-_37LStD-nVqBkWNXRFIU9JmixXn4BZlWNEW_LrjH2D6l6RYPxrRnuo5kq8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
صفارات الإنذار في كييف</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88530" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88529">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
حاملة الطائرات يو إس إس أبراهام لينكولن قد غادرت منطقة مسؤولية القيادة المركزية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88529" target="_blank">📅 00:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88528">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cneEcUhVAZXnz_3LhK1ZIeNglgqdRGbhCqSKZZW-iua5XuKi0MMRfjzhSjWdz1O2iTVF0xDf88KJ9b4XxcSMPNVsHb7k_2qeGLjC9Of5OsDb7bLu5ac1N2FVs6lAgTl_2LLwOOJM1g58ia_iz86-UGNznH8zp3qNqGJ7-M8xbej4mojKZJuVIqREyGfzEJrtDuStEauUr4npoXRyEkjegmFkNLbmzKIhFRwRb2oHT5ANbL1sOMigIfi7bPzAzAP-NmrwgROlHEGq15P_vSEmMHVHLXDYPPq4JtAl2SXF6CkDog5LsJ8_b9GFofQ0HHYyPTYxx7e4a0GCUpE6vRHJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
المعاون العسكري للمقاومة الاسلامية حركة النجباء الحاج عبد القادر ااكربلائي:
من مهازل الدنيا ان تقوم دولة الارهاب العالمي بازالة اسم اخر من قائمة الدول الراعية للارهاب؛ فالان اصبح الارهاب نفسه فيها دولة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88528" target="_blank">📅 00:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88527">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇦
صفارات الإنذار في كييف</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88527" target="_blank">📅 00:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88526">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtQoJXwrAQAbDb4Koyr1AGE04mW1ZX7BrxzOoJnEcDHY3y40BwKU9QP68PPJKEzoS_HHHyERoR25f7EFQqT1qtGMweDb_lZwiLQuL3g-QwMWSEFPZuL_1opTZWLfwbUHFMlU6HBI-F_QwqLe7usajKpglTEsP5t6CEpRTJu8XVjlVYKBwFsZ5qZl0GPhPm6Pg-KooU51dq-tkHg7YaHDVE-NGen1yKJsC85Dx-maJ6A47D-BbgSGdNcuFHZ6Dg5MMBa21pOhs8-cfQmxahDtkpwVwDGVA3hyxwSavxnJZ709BZOvvoeOYKKxyw6nD5GSGrAER9AUBRBI-KSH4A6mcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رويترز
: الخدمة السرية على علم بفيديو يبثه التلفزيون الحكومي الإيراني يناقش مؤامرة محتملة لاغتيال ابن ترامب
ناقش مقطع فيديو مدته ثلاث دقائق بثه التلفزيون الحكومي الإيراني مؤامرة محتملة لاغتيال بارون ترامب، البالغ من العمر 20 عاما، مدعيا أنه كان يتم مراقبته ويزعم أنه تم تقديم مكافأة قدرها 10 ملايين دولار مقابل قتله.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88526" target="_blank">📅 23:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88525">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي :
‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88525" target="_blank">📅 23:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88524">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
المقاومة الاسلامية كتائب حزب الله:
بسم الله الرحمن الرحيم
ببالغ الاستهجان والرفض القاطع تلقينا نبأ صدور حكم جائر بحق مفتي سوريا الشيخ الدكتور أحمد بدر الدين حسون، في خطوة تمثّل استمراراً لمنهجية استهداف الشخصيات الإسلامية التي طالما دافعت عن وحدة الأمة وسماحة الدين الحنيف.
لقد كان المفتي طوال مسيرته رجل اعتدالٍ بكل ما تعنيه الكلمة؛ وقف سداً منيعاً أمام مشاريع التفرقة المذهبية والفتن الطائفية، وكرّس خطابه لإعلاء قيم التسامح والتعايش السلمي ووحدة الصف السوري والإسلامي.
إن مساعي النيل من القامات التي ناهضت التطرف والمنهج الوهابي إنما تعكس الرغبة في إسكات أي صوت يدعو إلى الاعتدال وتجاوز الأحقاد، لا سيما أن الحكم الصدر من قبل سلطة طائفية يرأسها من تلطخت يداه بالدماء، حيث لا زالت الذاكرة تحتفظ بخطاباته الطائفية واعترافاته بتنفيذ عمليات إجرامية بحق الأبرياء لا لشيء إلا أنهم يخالفونه في التوجه الديني، (وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنقَلَبٍ يَنقَلِبُونَ).
المقاومة الاسلامية
كتائب حزب الله</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88524" target="_blank">📅 23:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88523">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الاعلام الاجنبي يتداول:
أفادت مصادر عسكرية باكستانية ومصادر أمنية إيرانية أنه تم التوصل إلى اتفاق لوقف إطلاق النار بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88523" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88522">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOFYHgvwpPofl4JVJaHxmibOYi5OLCgX1lOJZAzK-LbTjGWRBlnSKM7LcUry6bxR0J2-ag5wILIijJMyz6Dck3smv1pVJIazXgfk2AR_jrrIhk-KPOhSgALoTc-esNYzq4eNNJ1L2iZteM8XjJDJxqHstmayaXPv7fjDf-wuGO60johj8wuqbj9nBhjWbTzq8fgLMeSz2CvNJZ3iqZ4dX3Isexnq9LdKCJSaBDyDx_ErABnPRqA4VSFDumMrNnyGmQ5unGb8QJPL320V4Ud0hRTFO757KThP0jGuFyBp6AbD23sNM3eZMq9e9M4UFB5Z0vYuodXS6D71tilR-LxcnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي
:
إن التزام إيران بالسلام والاستقرار يقابله دبلوماسية راسخة مع جيرانها. وقد تم التأكيد خلال المحادثات مع الضيوف الباكستانيين والعمانيين على الحلول الإقليمية.
‏يُعد الإطار المقترح للممر الجديد، وإزالة الألغام المشتركة، والإدارة المستقبلية لممر هرمز مثالاً على ذلك.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88522" target="_blank">📅 22:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88521">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4dilOd5pWcsilL00gSjqNERYrtoKOlqbnUBZBApRoSOZDURLmhlgNDGX7jN6bHYyr0oGA9oktn3-mqeKgnri7C4QPgzY5bifq11qfWp7j3bcM5qdpKsN5MmFiiINrM6T4788H-3CgKr1GlOTYHiy2UN-fdQyO0RHpW0CaBCrPR0b3FJziaXBQC5T4QWmNf_7hc_O4p86ip8Q0_J-xcgPIRzcpWRYm0CWiBQAUD5X8eJiydCMHW8hTxeVVHIgHPRdZiKt12iwknI3OaH49j-kMYJQ837-Pv-dOeOHQ8P2-fEIXaGSq105KZ2j1cakPmrWqV9TF1Q7HSdZKbtPeu57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليبياف‏
: هو: "يوم النصر الاقتصادي".
‏ثم قال هو نفسه بعد خمس ثوانٍ: "[هههه] لماذا أرغب في تفجير النظام المالي العالمي؟"
‏سيدي، هذه ليست نورماندي، هذه ليلة ارتجال وقد نسيت نصك الخاص.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88521" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88520">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇹🇷
‏وقع زلزال بقوة 4.2 درجة في أديامان جنوب تركيا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88520" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99461fe9fa.mp4?token=jPdFxkIY-s87feiL72OA4Mvy-P58up3u3bQzGZSt2l2pYMIrlEBlgZyzOrdgg-PAdx7S9h_m34sBZSzwu79w20Cc6xh6lqooiZ9W71DH0r4tKrUFqGgKqgoUuCg5xl02xsfeafLScuoWyyX3hpBP_JMEPClz4RGi9pLv-cOhJz2KIRU3Hl-gYoX-ilnSYU_s2KAfEFcfLJsS-kln4ghkUOPi-ZrvRvB3ViDwBGCPuF1U9te3tMdZzcabWoRUzEuncmM7Om2TJN6GM7QORwv1gIxGPIORIzPJiV7AhlHRyHs9tAy6rddxVKFyGIBv5slH7EGkV7thyWOM1MyYHMZmcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99461fe9fa.mp4?token=jPdFxkIY-s87feiL72OA4Mvy-P58up3u3bQzGZSt2l2pYMIrlEBlgZyzOrdgg-PAdx7S9h_m34sBZSzwu79w20Cc6xh6lqooiZ9W71DH0r4tKrUFqGgKqgoUuCg5xl02xsfeafLScuoWyyX3hpBP_JMEPClz4RGi9pLv-cOhJz2KIRU3Hl-gYoX-ilnSYU_s2KAfEFcfLJsS-kln4ghkUOPi-ZrvRvB3ViDwBGCPuF1U9te3tMdZzcabWoRUzEuncmM7Om2TJN6GM7QORwv1gIxGPIORIzPJiV7AhlHRyHs9tAy6rddxVKFyGIBv5slH7EGkV7thyWOM1MyYHMZmcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مظلوم عبدي يعلن حل تنظيم قوات سوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88519" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
ضبط 36 كغم من حبوب الكبتاجون وإلقاء القبض على المتاجرين بها، بعد تنفيذ كمين محكم أسفر عن الإطاحة به بالجرم المشهود.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88518" target="_blank">📅 21:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52c9cb6e3.mp4?token=SVUrepZSUMxCDTvx5PFjiw6ehQnZeDUQ7ijFcLqd3_kUVsWstmq4kZlRCKgH092D7zxavxghf-adZ52zvD6QghsSCNego_DuzR3-ggoyzc7BrgI5vXc8xujCcu763maKDcTYihsCjmcPOI1jvNHayOJKQ2NJKBvWY_1nQsXaNX4rJ12JdVH3APq5BZTsJmMVLVWP4YFP3jBS0jU7PvjKJ9cRGd-0CUVF0cUo_qVyKrHByV7EYy0DwshBwfFO4UZKmTTkLOyJTJejU7psfSEj1fOwTLwb9Uw7l8oiD_fQdWuDB2iUUB5-a_VJSkJLBkYZZ-Le6MMEjdsd00gLkwaCHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52c9cb6e3.mp4?token=SVUrepZSUMxCDTvx5PFjiw6ehQnZeDUQ7ijFcLqd3_kUVsWstmq4kZlRCKgH092D7zxavxghf-adZ52zvD6QghsSCNego_DuzR3-ggoyzc7BrgI5vXc8xujCcu763maKDcTYihsCjmcPOI1jvNHayOJKQ2NJKBvWY_1nQsXaNX4rJ12JdVH3APq5BZTsJmMVLVWP4YFP3jBS0jU7PvjKJ9cRGd-0CUVF0cUo_qVyKrHByV7EYy0DwshBwfFO4UZKmTTkLOyJTJejU7psfSEj1fOwTLwb9Uw7l8oiD_fQdWuDB2iUUB5-a_VJSkJLBkYZZ-Le6MMEjdsd00gLkwaCHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇱
رئيس تركيا أردوغان حول إسرائيل وسوريا: نحن لن نتوقف عن دعم جيراننا لمساعدتهم على النهوض، لمجرد أن الشبكات الإجرامية التي لديها دماء الأبرياء على أيديها مستاءة من ذلك.  السياسة الخارجية لهذا البلد يتم تحديدها حصريًا وبشكل كامل من قبل الشعب التركي.  لا يمكن…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88517" target="_blank">📅 20:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c8b533d3.mp4?token=F4RRMDLSmCETyQGYZnl2fjt5P5hmA-LA1nvU9B52q-vBr_6r_RZSKCQYy1_IG-zJOrHJ2eKDeH5d0kPKZysjZH-BOmB9dWhl2zhH4mGl3fNDwPu6E54zJc17tjG9skbLDcZMiUw1M3jcDPsKByHfxG8XqzbwHctZLu9CaGf91xcpwJuuzrE2sQNFIohk4Ybm2qWVda0uiUtq3FCLurVr-FdPY7hfCWOGz4sLZYXWh2C3Dl-tkZpGp38eW44Xu0szKlhNkvfOc2sY0kzWyVLocLBRgF5CReV6D1vu4Y5sFXPrDW1F0LdebhpHIBPxO18JzE3fuAiMoyPhuj07L1xkxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c8b533d3.mp4?token=F4RRMDLSmCETyQGYZnl2fjt5P5hmA-LA1nvU9B52q-vBr_6r_RZSKCQYy1_IG-zJOrHJ2eKDeH5d0kPKZysjZH-BOmB9dWhl2zhH4mGl3fNDwPu6E54zJc17tjG9skbLDcZMiUw1M3jcDPsKByHfxG8XqzbwHctZLu9CaGf91xcpwJuuzrE2sQNFIohk4Ybm2qWVda0uiUtq3FCLurVr-FdPY7hfCWOGz4sLZYXWh2C3Dl-tkZpGp38eW44Xu0szKlhNkvfOc2sY0kzWyVLocLBRgF5CReV6D1vu4Y5sFXPrDW1F0LdebhpHIBPxO18JzE3fuAiMoyPhuj07L1xkxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
وزير الحرب الصهيوني في سوريا:  لن نتحرك من جبل الشيخ ومن المنطقة الأمنية ما دامت هناك تهديدات جهادية على إسرائيل. الرسالة إلى الرئيس السوري واضحة - عندما تستيقظ صباحا في القصر بدمشق، وتنظر إلى الأعلى نحو جبل الشيخ وترى الجيش الإسرائيلي - فأنت تعرف أننا…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88516" target="_blank">📅 20:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88515">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owg_9G5esK2B1zjYqEr4R0Ybe4rij5ASbpuGiZ5q2a4FJLxcPU6AbAmMNONYQIxqlxNTKQu2sMG_56EqvkT7jq3d5OaGYuB4tBfnVccWL8Utf_zHeAjrC3Tqr6wLU3HM0qJoJGOIpj6uEFJwOIAME8NT_CD46CNyTc4J-wHggIV04BrcJMSdpK9kjmobqNO4hu2p-cxEx-1myCYZ5hvJAe4ITls-AxTu5uWGQigNWmJa3dWHMAtsnsjpw54DmhR60Wb_yFyzMTFPChopxrb0XTqZgz5Ddjsri0P_HspaQLc05Dy6Hr6J3KrLn5-u-Qp3GuEUG4Vu1bLyCDbn07k0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يعيد نشر تقرير
: أمريكا على وشك تحقيق ثروة طائلة في منطقة الشرق الأوسط والخليج.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88515" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88514">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇱
وزير خارجية الكيان:
سنطرد ممثلي هولندا من مركز الدعم الدولي لغزة بسبب تحركات حكومتهم المعادية
لإسرائيل
.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88514" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88513">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQoMlXpGS6ojIguwek6kCMRqi_7DVriNWzlzSVjFR1CvONAYDVdzZ-TfztRQ2OcVPJcnchsG1kATArrgAxyD-BZpXQ2Gbwu7ZbxyutwPW5PozpTsdsE3G--ZsuwweyBBAwqgfs2J1XBA16anBPLY5aqT9kopDEMpJGIiv7pLElDq6RMqjjQQazuV-4qoXmWtGSjtGusq6v7fSlNgeiQAddQ4UkG9cTduQpoz0j1-L9p0-zdIL_DaU5zCMZTELlLmoqrI0y0nWiFG85WyK9YvBUV05s_cHzl8jtVEQ_A9gx3MxjLEGH3aK2mOymPa-9pNU8RgSh4i5u_JPuExhDMtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
بيان ايراني عماني مشترك
:
أجرى معالي السيد بدر بن حمد بن حمود البوسعيدي وزير خارجية سلطنة عمان مشاورات بناءة مع نظيره الإيراني الدكتور السيد عباس عراقجي خلال زيارة العمل التي يقوم بها إلى الجمهورية الإسلامية الإيرانية.
ركزت المشاورات على الأهمية التي يوليها البلدان لاستئناف الملاحة الآمنة عبر مضيق هرمز مع الحفاظ على سيادتهما وحقوقهما السيادية. وناقش الوزيران إطاراً مرحلياً من شأنه أن يوفر أساساً عملياً وقابلاً للتطبيق للمضي قدماً، في ضوء الوضع الراهن في المضيق، الناجم عن الحرب الأخيرة وتداعياتها الكارثية.
يتضمن الإطار المقترح إنشاء ممر ملاحي مشترك مؤقت عبر مضيق هرمز، واتفاقية لتنفيذ مشروع مشترك لتطهير المضيق من الألغام. وستستمر المفاوضات الفنية بين الجانبين بهدف الاتفاق على ممر ملاحي دائم، وإدارة المضيق مستقبلاً، بالإضافة إلى آلية لتبادل معلومات إدارة حركة الملاحة، وتوفير الخدمات البحرية والأمنية اللازمة.
وفي هذا الصدد، أكد الجانبان على أهمية إجراء محادثات مشتركة مع دول المنطقة المطلة على مياه خليج فارس. كما أكدا على ضرورة الالتزام بالقانون الدولي المعمول به واحترام الحقوق السيادية للدول الساحلية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88513" target="_blank">📅 19:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUu8EfUpbbQjCYRncQPI_Y8rwwb-kgkKjBXpoFWgvwGTIo_LB0BlmVs6mirTqf8purfh3PhnfWq1aqo_HOq39IsdgXpwLy_ePclYgRUiXGBbTHSB7Lyfib2sNdDLebvrT9niCU_FChYSVFAxUyoFpQkW5s2XKuT_Fnen8ZBI4H5cudlgUPBdrh5K49ekXUcVfe8rF4utkDbh1laCgvUMfVqrTLeWCYm21EGS8KJGHrdU4GuWMiNtgQuDlXPkrQFTjW_FrPOrdlZHfrDZmt4w677oQ5qH_PDf87OkxtjFvYxxG1i7CG8LRa_dBAaFk2WCjDfrKNY6kGnCNkAsLFuxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
المتحدث باسم الخارجية الايرانية
:
‏
الولايات المتحدة: "يوم النصر الاقتصادي".
‏أولئك الذين يفضلون الظهور بمظهر "الخاضعين كالظلال" يقولون: "هذا جيد".
‏لكن انتظر on. هذا ليس جيداً على الإطلاق.
‏عندما يعلن أحد المتنمرين أن على كل بنك وشركة وميناء وحكومة أن تختار بين إطاعة أهواء واشنطن أو مواجهة الانتقام الأمريكي، فإن الأمر لم يعد يتعلق بإيران فقط.
‏يتعلق الأمر بتدمير أهم القواعد الأساسية للقانون الدولي وميثاق الأمم المتحدة - أي احترام المساواة السيادية وحق تقرير المصير لجميع الدول.
‏لن تقبل أي دولة محترمة تقدر سيادتها ومصالحها الوطنية بتطبيع مثل هذا الفوضى العارمة والتنمر الممنهج.
‏تُعد كندا من بين الدول التي بدأت بالفعل في استيعاب هذا الدرس...</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88512" target="_blank">📅 19:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f3771f51e.mp4?token=mq9hXplmQFOx1TbN_Y4lEuk-CFP4ahqMqZtUOOD3EE7DIBVtts3p-HopYLb479TTxbDO0PfuTnUmUZqULNra9-QgY-1gHx34XAtlXHlLJGa9tp5e82S1iGsQ56PSVyNWL5BmFC-bFqFYYkVHK_L7aOfOYmaQjBj3g2MDDOriD_FCdrqPc2l8fLgRctW4CLrZib8qkGHBTt0XBhZ9SADLx5I8Y1YGWIPXQvRjE7Ha51kdYU4nn7yGeKlbtAsa15sgYMJEavveC-iJIZDJDFoXuRXv8f5BTL8OXi0PzQtn41vRPIYpdXBD7AU2jWJ5eBAlXKfesEAKZY6yeedVhWA-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f3771f51e.mp4?token=mq9hXplmQFOx1TbN_Y4lEuk-CFP4ahqMqZtUOOD3EE7DIBVtts3p-HopYLb479TTxbDO0PfuTnUmUZqULNra9-QgY-1gHx34XAtlXHlLJGa9tp5e82S1iGsQ56PSVyNWL5BmFC-bFqFYYkVHK_L7aOfOYmaQjBj3g2MDDOriD_FCdrqPc2l8fLgRctW4CLrZib8qkGHBTt0XBhZ9SADLx5I8Y1YGWIPXQvRjE7Ha51kdYU4nn7yGeKlbtAsa15sgYMJEavveC-iJIZDJDFoXuRXv8f5BTL8OXi0PzQtn41vRPIYpdXBD7AU2jWJ5eBAlXKfesEAKZY6yeedVhWA-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد كبيرة من ميليشيات البرزاني تدخل قضاء خبات ضمن محافظة اربيل لاقتحام منازل الهركية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88511" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88510">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زلزال بقوة 4.9 ريختر يضرب افغانستان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88510" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇱
🇸🇾
وزير الحرب الصهيوني في سوريا:  لن نتحرك من جبل الشيخ ومن المنطقة الأمنية ما دامت هناك تهديدات جهادية على إسرائيل. الرسالة إلى الرئيس السوري واضحة - عندما تستيقظ صباحا في القصر بدمشق، وتنظر إلى الأعلى نحو جبل الشيخ وترى الجيش الإسرائيلي - فأنت تعرف أننا…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88509" target="_blank">📅 18:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇨🇦
🇺🇸
‏
كندا تصعد الحرب التجارية مع امريكا
- كندا تفرض رسوماً جمركية تتراوح بين
15% و50%
على منتجات أميركية بقيمة تقارب
20 مليار دولار
.
- كندا تضاعف الرسوم على
منتجات الصلب الأميركية
من
25% إلى 50%
- الحكومة الكندية تعلن عن حزمة دعم بقيمة
7.5 مليار دولار كندي
لمساعدة الشركات والعمال المتضررين من الرسوم الأميركية الجديدة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88508" target="_blank">📅 18:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c487d787a0.mp4?token=mRwsF34AdaADUcQnU_de6Z2us9ZxOHBRhVuzca361nW_IAaLC-SlHeLDBM9qu00p9RBFr8LFg-Nk8RGOVOTphgFkRECgYYYdGj7v_sSm68yy_o2dsEsQvAJhJ2LxE_-eyPujCWKriDieuMm31dvePLeYoTsJO-ud52QJyToeBvQSsGPolz-7Wt4PxlCBS5gnu7nwnRM8hUDkNZTA7C3iz5dFx1vwheXU26MPFEYme7fuFa5HZ7RnooZ7WPQb0QIByPfUkeWBVeCOqdBG8DyXYtgoqsdV7YHZMxmkR7vLj34PeGqHJ2Sy0PSn7H7-uqxpQn71wf9cdQqP5wiWj_7e9i3NP3rbVY3JGRHBJlrhBGLd-IaPCinoMM9SOrkKLZaB4CCEJEdYcQaiK7Fl7XcMhPJrC-C69RxFFNAG7xkcR5AnQ-Q_SXLcTWa3H23WeZ-7HH0I-fsoxkO_ajLBm7MjfAeF6kDHmrMenA2sOWW5JV_Y3K6OtXa8jjnwCEG9-GGPk6aKs3VLswwQYBYOi__qfdokNbGk5oEjVdIrUtAcFkCuIaxztlbSRSQy_ELQEsy4tTVcjJnie-WWkCi42XNYTY-jqDgUyObEKBJbrQ-BR2ZgUwolSyypxFliURnmymb8p5PHwmMQg26zlJ5mmmGoE_eulp5jByKgocqSPW2-_BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c487d787a0.mp4?token=mRwsF34AdaADUcQnU_de6Z2us9ZxOHBRhVuzca361nW_IAaLC-SlHeLDBM9qu00p9RBFr8LFg-Nk8RGOVOTphgFkRECgYYYdGj7v_sSm68yy_o2dsEsQvAJhJ2LxE_-eyPujCWKriDieuMm31dvePLeYoTsJO-ud52QJyToeBvQSsGPolz-7Wt4PxlCBS5gnu7nwnRM8hUDkNZTA7C3iz5dFx1vwheXU26MPFEYme7fuFa5HZ7RnooZ7WPQb0QIByPfUkeWBVeCOqdBG8DyXYtgoqsdV7YHZMxmkR7vLj34PeGqHJ2Sy0PSn7H7-uqxpQn71wf9cdQqP5wiWj_7e9i3NP3rbVY3JGRHBJlrhBGLd-IaPCinoMM9SOrkKLZaB4CCEJEdYcQaiK7Fl7XcMhPJrC-C69RxFFNAG7xkcR5AnQ-Q_SXLcTWa3H23WeZ-7HH0I-fsoxkO_ajLBm7MjfAeF6kDHmrMenA2sOWW5JV_Y3K6OtXa8jjnwCEG9-GGPk6aKs3VLswwQYBYOi__qfdokNbGk5oEjVdIrUtAcFkCuIaxztlbSRSQy_ELQEsy4tTVcjJnie-WWkCi42XNYTY-jqDgUyObEKBJbrQ-BR2ZgUwolSyypxFliURnmymb8p5PHwmMQg26zlJ5mmmGoE_eulp5jByKgocqSPW2-_BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تواصل اقتحام منازل الهركية في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88507" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه باعتماد البطاقة الوطنية الموحدة في الانتخابات المقبلة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88506" target="_blank">📅 18:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW0V-K8YN3Qo60i9wPVmUwXfhaqui2DbGDWAPA3tUwxjsSi5byoDf1QIyJYEkduNEXHfBl8gywjqVlOXXpdEL__Wh0Gx1u1JSgAA2HDlYyNDFF_G0lvV-cd8bsS4pmNbU5qHS11SIjjuBkeppRYlJkvg68UDBXyVfxlvZkXDWw2Nec730h80M0fsmEqwjID6vkG0zd8YaPQTQAyizTsJSqHdMCzZcj_ZMFkLcaBb9HgrDA8Sg-7X4xAVzMDNHH6exYtqO2CQn3QS9I4F0T0Nw1ICHEnA2-U0B0TuS1UCgVZ2w8n11Q7qEJ4hZRSpoGMvVewJhjx3V4nKCRGH15PAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
ترامب يزعم:
لقد أُبلغتُ للتو من قِبل البحرية الأمريكية بإزالة جميع الألغام و/أو تفجيرها في المياه الدولية لمضيق هرمز. وقد تم إخطار إيران بأن أي سفينة أو قارب يزرع ألغامًا جديدة سيتم تدميره فورًا وبشكل منهجي. ومن خلال قوة الفضاء، نراقب كل شبر من المضيق، كما نفعل أيضًا مع موقع بيك آكس ماونتن والمواقع النووية الثلاثة الأخرى التي تم تدميرها بالفعل. هناك سياسة عدم تسامح مطلق مع زرع الألغام سارية المفعول بالكامل.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88505" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي يطيح بمنتحل صفة تمكن من الوصول الى مسؤولين وشخصيات رفيعة من بينهم رئيس الوزراء العراقي والتواصل معهم وتحقيق مكاسب شخصية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88504" target="_blank">📅 17:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88503">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtCIn55hBxVOyV0wnAQEzmHUC6pJ1c5UXHs0OmagIwFLFkpNNYyNurBmCQt5r5BkvYq7-K405tehtzkSyMDNpt8BxpmWjPf53vmqqWA6LQ8jx4C0N9SXYJABdPhk7n1rz1aGKfDK_eefSSRBmGo5tUqSZMt0KLkrH1VKwogUTIW4DGK2CyZsOIvzFWThvG525MKgIRKC9xw1kBtm380tq2hT8zLqiR8qi4_C9CqJ8DhVbVZ5EUnOlv_KcVLSIsw56AhyZWrb0ixGDZYBXWDiK1l0hxIEHGPFlI1vva1tCHjFI10BnPjrA2fPICsXhDq2Pg1RAFFIGTodcJKYQyOEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ترامب:
على مدى السنوات العشر الماضية، خسرت الولايات المتحدة، في المتوسط، 60 مليار دولار سنوياً مع كندا. كفى!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88503" target="_blank">📅 17:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88502">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb337cec2.mp4?token=dhNCMLCQONyTlhkPRY-Gog_Y1AwhmuizoxFHj-7qENkBgTuCE1oK_zP3Wfm3g3MxT-AWNFLb8dPWWTvn6KgKqnheKPz-KdpeIkcqZyov42ubGso-XEnE4Cvhm_Jy11X_DDyB_07fTGjxNB0gM10H4u7KXODeNb1gcoTgC6paInGHseH7dJZc7Xp5tnyhfwyEmlDB8dYK8laUqSrZqupyP_6e16o8smYPIb0Ho02ejhDzr10Nvd-DUNV3L1o_GouPveleb_tf3QRblTax0jtU2QOYDgR4gP9Ad9HASp3DYO5SPG7f1fAy554uCPTyxmfvJMhI9bWGjZQj_UxdSm5s_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb337cec2.mp4?token=dhNCMLCQONyTlhkPRY-Gog_Y1AwhmuizoxFHj-7qENkBgTuCE1oK_zP3Wfm3g3MxT-AWNFLb8dPWWTvn6KgKqnheKPz-KdpeIkcqZyov42ubGso-XEnE4Cvhm_Jy11X_DDyB_07fTGjxNB0gM10H4u7KXODeNb1gcoTgC6paInGHseH7dJZc7Xp5tnyhfwyEmlDB8dYK8laUqSrZqupyP_6e16o8smYPIb0Ho02ejhDzr10Nvd-DUNV3L1o_GouPveleb_tf3QRblTax0jtU2QOYDgR4gP9Ad9HASp3DYO5SPG7f1fAy554uCPTyxmfvJMhI9bWGjZQj_UxdSm5s_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تدفع باعداد كبيرة الى مناطق انتشار الهركية في محافظة لاربيل لتفتيش منازلهم بشكل اجباري وبدون مذكرات قانونية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88502" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88501">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB0rT98IauvyxfHDu9zn9PZebVgDfHOnAWE6citk48Pehk5ltbZpwpJe564ROj2yQ30BAkWRAVd-S7vpSNTv2KzDr2CcnAFNgBK95ZZ-oSsiX7oiebT0EUegcxunNANBwd0Y5Z7JZMLcMAwmsyFReoNyaKbw2SZihOIL5Xw-m5_nt7PHsPfwuRlrWWn39ERNmvMVdrCNHB6a6s5MeI3p9-RsjOtNSOX7dhjSSltk5U_Md0R3H9Zl5Y9jT0rIeY0N66ppUE49CIhGWoYHupcyy3KrZhsUAlPYLoC9LDEY-SoeW6xGlIEr2ItpX_8i3Bi_IPQe98NEwS_w0NBJL3tA8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب الترجمة بتصرف " كندا ٥٦ لسنوات طويلة وجانت ناصبة علينا "</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88501" target="_blank">📅 17:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88500">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSXTgXEIZgo-VkIPv9GEVRZpTtRCeSvG__Fy3ERgnPWLwhk88BeJSFNyalSaUlzqP6icSv6I80uu1yXP9UlS1hMmyE7rTOSBsD9ZJXy0khAbIi0Tgoyx5cLiqCd3Lrs5GXa9uXDfETFu-_44mS1CQXB5HzL9IT9fUQ2akA00HYbkIcloHlNRapweQ4Zh2gvCd3PljJMvE4B7L8FxpMPSoV_1alYklb54-jAljwHfEbyHHdp4g7IoQV0vI30sYjRmMGCakyzFB6oLTXg8g9zA1QIPb94TeOqYz-DFq8i8hS8rD_epogiXdGOMy_eaKt7UoFsgkA-tjRva744XweWBHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب للمرة الألف
لن أقوم بالمشاركة مع كوريا الجنوبية في اي تمارين عسكرية مجددا واستفز كوريا الشمالية ؛ كوريا الجنوبية رفضت المشاركة بالهجوم على ايران .</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88500" target="_blank">📅 17:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88499">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
🇾🇪
السيد عبدالملك الحوثي:
- في الوقت الذي يَحرِم المعتدي السعودي شعبنا العزيز من ثروته الوطنية ويُغلق عليه المطارات، يفتح أجواء بلاد الحرمين وأجواء مكة والمدينة لليهود الصهاينة
- النظام السعودي المعتدي العميل للصهيونية يتحمل كامل المسؤولية لكل ما يترتب على استهدافه لشعبنا
- أدعو شعبنا العزيز إلى الاستعانة بالله والتوكل عليه وتكثيف جهوده حتى يستعيد حقوقه المشروعة ويدفع عن نفسه الظلم الذي تمارسه مملكة قرن الشيطان بدون حق ولا مبرر</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88499" target="_blank">📅 16:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88498">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
🇸🇾
وزير الحرب الصهيوني في سوريا
:
لن نتحرك من جبل الشيخ ومن المنطقة الأمنية ما دامت هناك تهديدات جهادية على إسرائيل. الرسالة إلى الرئيس السوري واضحة - عندما تستيقظ صباحا في القصر بدمشق، وتنظر إلى الأعلى نحو جبل الشيخ وترى الجيش الإسرائيلي - فأنت تعرف أننا هنا لحماية بلداتنا وحدودنا. تحركنا ضد محاولة تركية للتمركز في سوريا، بما يعرض المصالح الأمنية لإسرائيل للخطر، وأوضحنا الأمور بصورة واضحة وسنتمسك بها في المستقبل أيضا.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88498" target="_blank">📅 16:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88497">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f511c9c4.mp4?token=gDt0bjtCCrGq7dmduy9GKTjOy7bVFJuuev0gmqIemiyAgedh8T73a4t7fJAD4VM3d3AcoCIo45RGldfpM_DpyRH8UWZ_hjtuIilvGK1Fnr5AQl2eFsjLwBpkIVfr0MTAkl2O6YOL9Py537lT-nvVkoUlecr8fQAzY2dNN3qINPjrZV_m711U9_SYbBjiswzjbZom8fQ4asgrm4Ays9_oc-8Ww7ubtZBibY_Vux_JYb-g1s4zkiJc783uXQaJUdFApJpWJtLavbLdGbeSQsuf4o_4iTrl2QlQibsRSc75SU0Lg84KceYM1r1EOkNnH-nNcaqOM2L3cpIPGnjGoGhtmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f511c9c4.mp4?token=gDt0bjtCCrGq7dmduy9GKTjOy7bVFJuuev0gmqIemiyAgedh8T73a4t7fJAD4VM3d3AcoCIo45RGldfpM_DpyRH8UWZ_hjtuIilvGK1Fnr5AQl2eFsjLwBpkIVfr0MTAkl2O6YOL9Py537lT-nvVkoUlecr8fQAzY2dNN3qINPjrZV_m711U9_SYbBjiswzjbZom8fQ4asgrm4Ays9_oc-8Ww7ubtZBibY_Vux_JYb-g1s4zkiJc783uXQaJUdFApJpWJtLavbLdGbeSQsuf4o_4iTrl2QlQibsRSc75SU0Lg84KceYM1r1EOkNnH-nNcaqOM2L3cpIPGnjGoGhtmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تقتحم منازل الهركيين في محافظة اربيل بدون مذكرات قانونية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88497" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a53977ec45.mp4?token=b-Wnkcd8Dx7CaxCgLLWy-q9arg4gc7LacxNVLrk6bGU1sekUdMfSXPkTx5k2tOH1rhnW24othumGLJXW3W4pkoAQg4Fak3KgfNgRpvBln-vudcl7ZRIuQ8V-UILUSVblcUtollqHpTN6SWthxicL1VRFA-TKBMsb0Pb_ubyHb4_rL_M6ZLKOrT8AD_jxehSzwiimFCZDkJ0gJ86sQfUX23vgXchKkV7TLOVScjTouBRmPdN2h2i_rCYKnHadylT5ss-pa9ekD-aUxQV7wRTkCh7NO6QCYuVckQaFWIx4axLRoHhklBmzOF5AeYsDvdMEMSvSorEjxcaLqR0idHwPrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a53977ec45.mp4?token=b-Wnkcd8Dx7CaxCgLLWy-q9arg4gc7LacxNVLrk6bGU1sekUdMfSXPkTx5k2tOH1rhnW24othumGLJXW3W4pkoAQg4Fak3KgfNgRpvBln-vudcl7ZRIuQ8V-UILUSVblcUtollqHpTN6SWthxicL1VRFA-TKBMsb0Pb_ubyHb4_rL_M6ZLKOrT8AD_jxehSzwiimFCZDkJ0gJ86sQfUX23vgXchKkV7TLOVScjTouBRmPdN2h2i_rCYKnHadylT5ss-pa9ekD-aUxQV7wRTkCh7NO6QCYuVckQaFWIx4axLRoHhklBmzOF5AeYsDvdMEMSvSorEjxcaLqR0idHwPrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تقتحم منازل الهركيين في محافظة اربيل بدون مذكرات قانونية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88496" target="_blank">📅 16:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
شركة JGC اليابانية المنفذة لمشروع (FCC) في محافظة البصرة العراقية تبلغ العاملين وإدارة المشروع بأنها تستعد للعودة الى الموقع واستئناف أعمال المشروع تدريجيا اعتبارا من مطلع شهر أيلول المقبل.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88495" target="_blank">📅 15:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇾🇪
🇾🇪
‏اندلاع اشتباكات ومواجهات عنيفة بين انصار الله ومرتزقة السعودية في جبهة كلابة شمال شرقي تعز.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88494" target="_blank">📅 15:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngIofFzEjUKceUqCc5jYvHTF7zfH4lkrn3cl1jGmEhfXcNypVHt5vnmZzxLgO03iaFNYes95bsLZ4pteawotyH9sPnBNbYeAcjbZJvW848UcoCM0bKw9XEjlPxwF2sQ8d_LIOljL3YYSh9udKeY_QgasDS53on4oTBgTiUDc99KBH0P-HSE0xNHzM2IBJCUrVM3zLj06h6KHM45jpH5Z_m9R8kO-xd7nkUJJwjlzT2jysyiY3dWVhNA0ucYiGBFKATGmAa7nsxgCF2a9VryW5kt4MlAeXZ549756RnOHZ6_uh6fhJE5k47oPy333n_eanb1txmNmZeaFBSh7y8nAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
ترامب مجددا:
الجمهورية الإسلامية الإيرانية الفاشلة لا تدفع رواتب قطاعات واسعة من جيشها، وفي الوقت نفسه تقتل المتظاهرين، حتى في غير أوقات الاحتجاج، بمستويات غير مسبوقة. إنها أزمة إنسانية ذات أبعاد كارثية، ويجب إيقافها فوراً.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88493" target="_blank">📅 14:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d51a41e3b.mp4?token=qJyCEiWg8PfA1_liWFMmdqYjgu09W2VphNNvHqMgcNpD756WCFXeBgvg-QYWKJu2mpI18yB13tlWqG3SCMXBWhzcRrsWZZHwAZVh76uJej_-i65ID64cZVFjrEL6E5SOBEwU5oV1kx8kxuD-bJskLX35_hE_nlO9GY43nql5Tr8zCFflfpWB8m6GmrdRwCdKqP2JtAV_-4VIY6gFBy9Ur6BnVP1Nv01QUxJNBvGgLdny3MUdeuyxX1tCLP9aJZHjt17w5Lbz34cheuojt9WqET2ZECvCRZhayVKow4oGImheP48OmzmIK4-dbkybqYIPlOENW4h80UtqRb8nETAy8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d51a41e3b.mp4?token=qJyCEiWg8PfA1_liWFMmdqYjgu09W2VphNNvHqMgcNpD756WCFXeBgvg-QYWKJu2mpI18yB13tlWqG3SCMXBWhzcRrsWZZHwAZVh76uJej_-i65ID64cZVFjrEL6E5SOBEwU5oV1kx8kxuD-bJskLX35_hE_nlO9GY43nql5Tr8zCFflfpWB8m6GmrdRwCdKqP2JtAV_-4VIY6gFBy9Ur6BnVP1Nv01QUxJNBvGgLdny3MUdeuyxX1tCLP9aJZHjt17w5Lbz34cheuojt9WqET2ZECvCRZhayVKow4oGImheP48OmzmIK4-dbkybqYIPlOENW4h80UtqRb8nETAy8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بعدسة نايا |
حشود غفيرة تحتفل في العاصمة اليمنية صنعاء بمناسبة المولد النبوي الشريف</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88492" target="_blank">📅 14:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDAtuhwDIrjb0EHrzhBMBSaB_wKz2ZfZsif437qxCEqe3eXcTdMlZfacOSHxVDBbx-_Ctne5HYLwJkS1LzIEVI7HyhPuzYNJo1cj8gv2WAMgjCv23t_uPRyCrd-TQxIIm-DNPUyyYIC_ZuA0BC6cMmHQu_1BpBzp5JJ8TdbOGs5SqrNFlIz4bKEL3hLlKVBjoQ0OTAioqnuiiiToCRgbgoyVxVrcwFifEajR9CCuOOGckd2wp7_x9WcFGTdDPGKszWUfGjzQKkBPewQBXBR2QvLHUirC7_x3jg1f9W3LFpbU8827GKntDWAGwdl8ked36vgmaHXD215vxe4derqexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
تدرس الولايات المتحدة بجدية تغيير اسم بحيرة أونتاريو إلى بحيرة أمريكا، إذ لا نتوقع استمرار تعاملاتنا التجارية مع أونتاريو.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88491" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88489">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BktD-4bRTvSPTBXvjkYxIY4eae5oP6fD1Pzw4uB8gwHGZNeOwu792wCVpxznV0x1SF0kDq9aXr48SBlXKwhLNrsUGisTReSidFVZ8L2_TzjuX6UkBBVSLTeDxF7Z94jx1o62hULA9Ljk5E3MBnbwu1xqjdDSKi-H5p5VqrxanjaExGqRM9INCp-_dSexkAS_LHe_9CJMhDr8VtHn-azeu8JaI17Sykl224gCgKoA9DLZk0F4y2MnXvbh3h_x_YVe1h-rHanS9ELCpHC48R5Y_JNOHRLxbY1T-pyeYLJ1xTrmCYqMANeJFwHyf-cpj4yXMFPNdGi_Hs9_naYLxhmW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGP-zz65dWUi80a0VCLf6WfjqptB3x6uypljaRSk61DjwZAnDt0xIoi8J9txWUXz2BBPV0XqOv9b_OkGiNIK7PLlHHW7krGDCms_5PZssie00jIDWc5w2IJR8nS_GHzglqjGDXglL3rW-NgKJ7RTh5cvOz_3q5CMW5N3sfT93y68qPq-ND4so7_6zbrZl51anpAGVsIb5QKUVMagFbFRggIA2PVKNqw4kT5nxAxB5d6-BOqEYNNAjX7h2koMY-leOxqUKWlRXuyUED7JQtfsnEqeTuI4Q7pGJmx_2MaIAF3EzCkc62cDvhMWtH92hs01wnW1M8BVsMb1aUH4-vXGFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
ضبط (1004) هاتف من نوع آيفون 17 برو ماكس مخبأة داخل إحدى الشاحنات في سيطرة الشعب ضمن العاصمة بغداد في محاولة لإدخالها خلافًا للضوابط.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88489" target="_blank">📅 14:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEBz2l7b7XT-cgkdeLMG390Q7VMUVrT-AlfLEAZbYe96zqo0Nol-zc_9IR71Zseyi43aeetSPhJ4UtWPvO6E_8gqrcM_Jd85op6neqdK3P2apcsbAGcMk-6qtjhfAdUYnTwAEAFQSpb2G3kPP5UXR441yfXF8wmzoGOGDXhEfVqdidbz_84bBAyKN0Ihga1ngiqKn1SaZygDvYiccbRgP1GCRQCiePq8EycmAd0ev4OgcqZnvrX945fVufgwhteXdCJW-agjbX381rpn6991gAGEdbutgAd28PDl2Iz1KSF9wm1QRRNlrkRANbFDC29YQ5xhRQfeRyNID2gEwOqWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تحالف العزم:
مثنى السامرائي ليس أول زعيم يُعتقل قبله نيلسون مانديلا اعتُقل 20 عاماً.
غدروك يا شبل الاسد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88488" target="_blank">📅 14:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇨🇳
🇺🇸
فايننشال تايمز:
‏حذرت الصين من أنها سترد على أي توسع كبير للعقوبات الثانوية الأمريكية التي تستهدف الشركات الصينية، وذلك بعد أن أعلنت واشنطن عن إجراءات جديدة ضد الشركات التي تتخذ من هونغ كونغ مقراً لها .</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88487" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
‏
نيويورك تايمز:
واشنطن تعيد دبلوماسييها إلى سفاراتها بالشرق الأوسط.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88486" target="_blank">📅 13:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇱
🇸🇾
إعلام العدو:
وزير الحرب كاتس زار سوريا هذا الصباح.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88485" target="_blank">📅 13:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88484">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
🇵🇰
وصل قائد الجيش الباكستاني "عاصم منير" إلى العاصمة الإيرانية طهران، للقاء المسؤولين الإيرانيين.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88484" target="_blank">📅 11:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88483">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee375b397.mp4?token=AmCZYZw5OAgdozHcikFFK2q1T9qokMbGp44VOK9UOz3BbNLE8jTfm2GFwJHfw-94w9YM9JQte55AYifc7zMILhTBxOnZulE538P5a0-Kpkbqq9JkI0AhB76qSSa6yv3ijqNCLexzdvW8A9Awdqpf77AZyv-0CqEe0F-mDQjw2I1oubmD9691Xw506bQ6nW-b3r5Mh_IrRoAYU48Ok0bRBUDUZHsDXW4Y13mxzObRzaYXV7M3hA4zr4n7PYy0XAw5HkbOYJN1ZkkVoFVOPy40m5-kNAxzwlosvx_jNNzi5kpTxVFvvvxP_lUX2PR_yy5pCzgdjv3DxPqQYTkYT_Mb7Ae5t6amJgIlOtnDh9AN431nAF4uWUK7_hY0muE-_XvSloBR6LR00ZzE7xoXhp_dRYMCcAUsIbwnr0B-U1rpNDdCsx99vGEtfGYPn4k6wUAFDLQCEB0OD19kJ6JKLDbYETEKTDn8n6zDkDvB01-WWiH6EFTnAktjU9SacjK_N79ZnLfgxivLPmSB71wpIPMYjLSBPY_Iu41v-6sqEfoZHhj3Ceoku8XuHVBVjz1vCO9m-VIg61DY7y22UfGIbKUnQDrbEWtGJAOCxkWVFdMN30LBIlSNs2kacFOVZxMT9rZI91y1YuK3fg2FdJpVcrdjAF8W_umpEGS3aIKuyVmH1rY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee375b397.mp4?token=AmCZYZw5OAgdozHcikFFK2q1T9qokMbGp44VOK9UOz3BbNLE8jTfm2GFwJHfw-94w9YM9JQte55AYifc7zMILhTBxOnZulE538P5a0-Kpkbqq9JkI0AhB76qSSa6yv3ijqNCLexzdvW8A9Awdqpf77AZyv-0CqEe0F-mDQjw2I1oubmD9691Xw506bQ6nW-b3r5Mh_IrRoAYU48Ok0bRBUDUZHsDXW4Y13mxzObRzaYXV7M3hA4zr4n7PYy0XAw5HkbOYJN1ZkkVoFVOPy40m5-kNAxzwlosvx_jNNzi5kpTxVFvvvxP_lUX2PR_yy5pCzgdjv3DxPqQYTkYT_Mb7Ae5t6amJgIlOtnDh9AN431nAF4uWUK7_hY0muE-_XvSloBR6LR00ZzE7xoXhp_dRYMCcAUsIbwnr0B-U1rpNDdCsx99vGEtfGYPn4k6wUAFDLQCEB0OD19kJ6JKLDbYETEKTDn8n6zDkDvB01-WWiH6EFTnAktjU9SacjK_N79ZnLfgxivLPmSB71wpIPMYjLSBPY_Iu41v-6sqEfoZHhj3Ceoku8XuHVBVjz1vCO9m-VIg61DY7y22UfGIbKUnQDrbEWtGJAOCxkWVFdMN30LBIlSNs2kacFOVZxMT9rZI91y1YuK3fg2FdJpVcrdjAF8W_umpEGS3aIKuyVmH1rY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
هيلاري كلينتون:
لقد أهدرنا الكثير من ذخائرنا في إيران، وبالطبع، أرسلنا الكثير إلى حلفائنا في الخليج. وقد استخدموها للدفاع عن أنفسهم.
لذلك، نحن في وضع صعب لأننا لسنا قادرين بشكل كافٍ على مواجهة المخاطر غير المتوقعة.
إذا قررت الصين التحرك ضد تايوان، حتى لو كنا نرغب في ذلك - ولم يكن من الواضح ما الذي سيفعله ترامب - فسوف نكون في وضع صعب لمحاولة مساعدة تايوان في الدفاع عن نفسها.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88483" target="_blank">📅 11:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88482">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
🇷🇺
🏴‍☠️
تضررت مصفاة نوفوشاختينسك النفطية نتيجة لهجوم شنته القوات الأوكرانية المدعومة من حلف الناتو على منطقة روستوف، وقد أوقف المصنع عملياته .</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88482" target="_blank">📅 10:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88481">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdSx4v4YhDUhojv11KACJD230W1QsTaAOXrkN9TZXxKgLI2sybxk39yw0KjJfKZ6aKy85oPYVl2IN37UQPAIokgZECWE1X8uS_0r3M-K6WXEkIXerizRavnn3Ob5Rnc0_s66Kciv6pO6fHW9xbmeCJ_vmfK5T7M5NOy0k-lJuKpMMGVtcH-RyOGBsVra1M3hRaovUm10IyMcbF6VedgVFbdS7HLs8O_Q74R8hddH1RvNixMNVf31ZO37gxXD4dUF3i4uRpnkGGztHT2wxI4joMtdyYRBvaxRHg0ddREU_pmZbmy9FEpS6iAZNBHA2zgTxM1be1jNb-Yzpdj1T4FASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
🇺🇸
نييورك تايمز :
تستعين الحكومة الإيرانية بمجرمين - من بينهم رجال عصابات روس، وأعضاء من عصابة "ملائكة الجحيم" للدراجات النارية، وحتى مراهقون سويديون - لمهاجمة معارضيها وترهيب الإيرانيين في المنفى ؛ إن استخدام مجرمين محليين، لا تربطهم أي صلة بإيران، يُجبر الحكومات الأوروبية على "زيادة استثماراتها في الأمن الداخلي"، ويُظهر أن "أي مجرم قادر على إحداث فوضى عارمة" في مجتمعات الشتات. كما تُصعّب هذه التكتيكات على المحققين ربط المؤامرات بالنظام الإيراني</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88481" target="_blank">📅 08:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88480">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
🇺🇸
"
وول ستريت جورنال"
: قبل أيام قليلة من إصدار أوامر بشن هجوم على إيران، تلقى ترامب تحذيرات صريحة من أجهزة الاستخبارات حذّرته من أن اغتيال خامنئي لن يؤدي إلى إسقاط النظام، بل سيؤدي إلى صعود قيادة أكثر تطرفًا وصلابة، والتي ستعمل على تسريع تطوير الأسلحة النووية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88480" target="_blank">📅 08:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88479">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPeDkbqpAnljkiZ2QE52Ry_Ahp1iqM17mLhRXGrrNXfwAwbVEt6-q3a2LPzjnGDTaRaN84rv-KxepGn_AL5deiK7kJUAYmrnVfbRMlwfMXfdyKhHKqfWgUYYQQucT5H1x1jBJJ1tIzjAUxpi6YyBYkcX41ba3r4ovQ0gFck5doe1FU65EgVEFMz0z6PeMaxW1-Xrnz4sX_E9t_h9yOMBJOdNIFCZ8mywv4CqEym0Ki1RRc0FJ_O1nz98Ace2x8c13zQDVpJEG-eEMTL7r_TzGjNFp9wvQLOE-UMACdS80dHywGhO3Ec4fUth8O8JciQUx8J6Sc2yO-RFcdsNO-oiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🔻
‏إستهداف ناقلة نفط بمقذوف حربي على بعد 9 أميال بحرية شمال شرق سلطنة عمان.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88479" target="_blank">📅 01:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88478">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3dbea05a2.mp4?token=C3EKGXMNxmBXrEXHLFoDjqZBtRKX3q-PV6JO87k6xq39ed9NNq0CIG0f9BLthGsMr-YfVE9pc4lVREVLUwD8yuYjCnoBH9kAIFpNwwifOM7cEVeil2Ch9auF9AY1IYUfHg5CtODQWDb_KfXuEM57aWqRuHUu2b5Ov4TiVLP-bGKrtVu2HY2JS5zm1_h6l-hycV5n2NYhKHdqTXpS2e2UkwRuYFRDJLoROJuU10G5GYavcYLZ-xM4MESyTfqHUQ6D5fQ9eI8lDJoGXbdYjw6VmGCJFs9Vmf91KgcFbSHuEkBvCFofFKIS4QyLkNs6yuGWlcLquysb6NRVbnwtwaaq93fYBgwUvIfO8PTvKF29OhqDmCvTTqQlGJ-i_OeTslqgE7k_Kmn2mbq-YbKyVzvy2T2_Mf-6YIreoO9g2eZolbOj8AZ_gn1ZIWDzQs3jrwY3uSxfzAenxowURJUoPah4iDpzaqvVMYpAhxGYy9wLWoC6KWdO5vimophdsBpOUUcHTBLdbxOGBii56cbplpPeJTJtELL5JgzXHGYKQ9WYE-1A2F-pTR4WgvCEiJL4MA2UQ22L6LbnZK2JHTsxLY3vNCSM4CSC1ueLodAQR1PvdhEgMPZBCm9dIXrjLphS1I8vKZnzlGvmhb4ohFZUPNMT8C36Xdz_O9TNq4bmoKdQGC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3dbea05a2.mp4?token=C3EKGXMNxmBXrEXHLFoDjqZBtRKX3q-PV6JO87k6xq39ed9NNq0CIG0f9BLthGsMr-YfVE9pc4lVREVLUwD8yuYjCnoBH9kAIFpNwwifOM7cEVeil2Ch9auF9AY1IYUfHg5CtODQWDb_KfXuEM57aWqRuHUu2b5Ov4TiVLP-bGKrtVu2HY2JS5zm1_h6l-hycV5n2NYhKHdqTXpS2e2UkwRuYFRDJLoROJuU10G5GYavcYLZ-xM4MESyTfqHUQ6D5fQ9eI8lDJoGXbdYjw6VmGCJFs9Vmf91KgcFbSHuEkBvCFofFKIS4QyLkNs6yuGWlcLquysb6NRVbnwtwaaq93fYBgwUvIfO8PTvKF29OhqDmCvTTqQlGJ-i_OeTslqgE7k_Kmn2mbq-YbKyVzvy2T2_Mf-6YIreoO9g2eZolbOj8AZ_gn1ZIWDzQs3jrwY3uSxfzAenxowURJUoPah4iDpzaqvVMYpAhxGYy9wLWoC6KWdO5vimophdsBpOUUcHTBLdbxOGBii56cbplpPeJTJtELL5JgzXHGYKQ9WYE-1A2F-pTR4WgvCEiJL4MA2UQ22L6LbnZK2JHTsxLY3vNCSM4CSC1ueLodAQR1PvdhEgMPZBCm9dIXrjLphS1I8vKZnzlGvmhb4ohFZUPNMT8C36Xdz_O9TNq4bmoKdQGC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
تنفرد نايا بنشر اللقطات الاولية لاعتقال الحاج ابو جعفر التميمي القيادي بالحشد الشعبي من العاصمة بغداد على يد عجلات تحتوي عبارة INSS في اشارة لجهاز الأمن الوطني العراقي</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/88478" target="_blank">📅 01:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88477">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
🇺🇸
رويترز :
أعلنت قوات مشاة البحرية الأمريكية في سيول، يوم الاثنين، إلغاء مناورة إنزال برمائي مشتركة مع كوريا الجنوبية كانت مقررة الشهر المقبل، وذلك بسبب القيود المفروضة على القوات الأمريكية جراء الحرب مع إيران. وأضاف متحدث باسم كوريا الجنوبية أن الحليفين ما زالا يجريان مشاورات بشأن استئناف مناورة "سانغ يونغ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88477" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88476">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8050a036ac.mp4?token=FZp28xLGXfFMJsMJfAqt1K3zTwil5ltNOQKuhj8bBdW_pOQN5Pj8NIgErrVq4iUqtmqDrRN6lvQH48DE5CAXbmX9Rd0EYsCIjxTESP70eMURmVGUFKvtt2Xrj5qzHBOrJjkJ5D4g679kpefto0O696UVja8vVrt-5oARZw-ma2MPGq-XHpmY6sMC_QWN1H1WCVqB6REWTKojwRxdbCom0rGPltMPn0LGArm2O7fUw4V0Mp49R8B5cxiqVI2qM6HFLcnEIIN7hOfpWKiEmev1jfQ7oY7PxoNJmj7D14XseTkopWjMbwu-Q0nM_EfySS1DLmNdSp-pS82fnkVeM1Ymzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8050a036ac.mp4?token=FZp28xLGXfFMJsMJfAqt1K3zTwil5ltNOQKuhj8bBdW_pOQN5Pj8NIgErrVq4iUqtmqDrRN6lvQH48DE5CAXbmX9Rd0EYsCIjxTESP70eMURmVGUFKvtt2Xrj5qzHBOrJjkJ5D4g679kpefto0O696UVja8vVrt-5oARZw-ma2MPGq-XHpmY6sMC_QWN1H1WCVqB6REWTKojwRxdbCom0rGPltMPn0LGArm2O7fUw4V0Mp49R8B5cxiqVI2qM6HFLcnEIIN7hOfpWKiEmev1jfQ7oY7PxoNJmj7D14XseTkopWjMbwu-Q0nM_EfySS1DLmNdSp-pS82fnkVeM1Ymzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لولا دماء بلال الوحيلي و شيخ ياسر عاتي الكعبي   لكانت الجرف الان ولاية ارهابية داعشية سلفية ..  شكرا حميد</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/88476" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88475">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1kLtZ2zV_AdNK_88FxLDWEi3EWi4b-l0pADpni0BCaLM5fkdI0hEQQVqXwQCe1aLBPnYFhXYhfLLPb99bLwoR4TB20ShUJ82fDEBXppogUL--eb0MGMEoMiy769OjmOjaYXaStlXeitNWHJrp68vuwtNIMPoTuIWioLaGNPBXX9m3ruP5sPuSsSsO6btw87WpSz1DcQgwI3lzWLte4B28H8JJGjvQFp1m8L0XoZbGuvB7MyurN1K3cNJkkZG7CYGhqgZU9Zi8eAB-gHIZtnQzs0UrjYS_KxfnmH19t72HssE_HLQAR2obR2hELqG1ownVNp2QQUFzkEY6a1zdM_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
الخارجية الاميركية تعيد نشر:
مكافأة 10 ملايين دولار لمن يدلي بمعلومات عن قائد الحرس الثوري و4 قيادات أخرى.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/88475" target="_blank">📅 23:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88474">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
وزير الحرب الاميركي ‏هيغسيث:
لا يستبعد استخدام القوة العسكرية في مضيق هرمز أو أي مكان آخر، لا تزال إيران تمتلك بعض القدرات.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88474" target="_blank">📅 23:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88473">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845b8cd8b7.mp4?token=pFZBEHZK5X4Aoiiq1C-0gt3iCg5EnU0CS2fnNxa9pe52rWD_cCD3ACbuF2CiBtV0M6xU5VN2halWrkpYB8a88TkApr9FDm8s5FlTB4YrnWoiT4jM8QWe8rhKt2iYbpExVKXVxisSDmLcj00ex1xpyZ4nsXNBanDVlR_Z2ddk0RqDjpqqDUHE0LbySsaq21f9TXFYd-CxHed03u6yWI97aN04rCV3CUixqJ60zCj2HgsgDqiD_swZFltC84xgv6RYGVDi5i2VJH6FVPYTGIlAEa2A9IiGkugoM0iMlIjmSshhvobE1UW7VU-dfUVl3iFxo1QSIku1DIdKqKUHgY4_mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845b8cd8b7.mp4?token=pFZBEHZK5X4Aoiiq1C-0gt3iCg5EnU0CS2fnNxa9pe52rWD_cCD3ACbuF2CiBtV0M6xU5VN2halWrkpYB8a88TkApr9FDm8s5FlTB4YrnWoiT4jM8QWe8rhKt2iYbpExVKXVxisSDmLcj00ex1xpyZ4nsXNBanDVlR_Z2ddk0RqDjpqqDUHE0LbySsaq21f9TXFYd-CxHed03u6yWI97aN04rCV3CUixqJ60zCj2HgsgDqiD_swZFltC84xgv6RYGVDi5i2VJH6FVPYTGIlAEa2A9IiGkugoM0iMlIjmSshhvobE1UW7VU-dfUVl3iFxo1QSIku1DIdKqKUHgY4_mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب الترجمة بتصرف " كندا ٥٦ لسنوات طويلة وجانت ناصبة علينا "</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/88473" target="_blank">📅 21:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88472">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9654cfd2.mp4?token=ZFn9PqnzK7q_y0XfDT6jEhI3M9BdHlLA-5Gv17FAOseAng2SUVTl3vLxjxPYv14o5GfWZ8mVyrEpjN3wpeWZJUaoTKOv5ralAd3iwBiV_Br98uz2fcslqYpkr2jqbUHFINs6hIH_mBbqPuWAEImOcNnGkRwpMsdY6D7He-9py9mTf6qhIp9pOQ7YjwiQlUgBuyv6tXnsf1D2MTEEvfr3s_VtbqHqTBaOibZRdBjOmi9FqCFkXir-oTFtHMgBYdJ7IpFmyVemy2OeHKkGu68kpagyC0S7KIOhqQLV0SAwyc5qwXYrDURF-7SreRFeqkk0RC8JGzlQc2pntYpZtHmdbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9654cfd2.mp4?token=ZFn9PqnzK7q_y0XfDT6jEhI3M9BdHlLA-5Gv17FAOseAng2SUVTl3vLxjxPYv14o5GfWZ8mVyrEpjN3wpeWZJUaoTKOv5ralAd3iwBiV_Br98uz2fcslqYpkr2jqbUHFINs6hIH_mBbqPuWAEImOcNnGkRwpMsdY6D7He-9py9mTf6qhIp9pOQ7YjwiQlUgBuyv6tXnsf1D2MTEEvfr3s_VtbqHqTBaOibZRdBjOmi9FqCFkXir-oTFtHMgBYdJ7IpFmyVemy2OeHKkGu68kpagyC0S7KIOhqQLV0SAwyc5qwXYrDURF-7SreRFeqkk0RC8JGzlQc2pntYpZtHmdbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
العاصمة اليمنية صنعاء تحتفل بمناسبة مولد النبوي (صلى الله عليه وعلى آله وسلم).</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88472" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88471">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇸🇦
🇮🇷
بيان سعودي فرنسي:
باريس والرياض تدعوان إيران إلى استئناف تعاونها الكامل مع الوكالة الدولية للطاقة الذرية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88471" target="_blank">📅 21:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88470">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88470" target="_blank">📅 20:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88469">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c955d03b1b.mp4?token=crtiuK82g-Lo4Ri601miqex92pta4pzlVLtHaD6gMH3BaO-HW9UMRzx-3j0__jImz1FNeniSRMF0bnPs6s5479YqF9KvJPQjdZOIGnTMsNHAY7vzZ1oECg-2Hc_mAUgrrdd7UoqRWv_QEkbOK89EiJ_lP4N98Lx55QmlRnLFVpmauyDIXLWd7Yx61W3vt7Ag21VL8bgl2fzBCmp3MOI6nYElBJerADz-IdHWOmYcsZQDNX7HxBHGjKRa5kZyfUciW-GcaHzYcdv_14NhBAZxAP-Oa6G8rjL7jdhVv47sG_7OdYXyDzb1mzZKpVAgkiSyLx3x-1TbKhkoF2A8Fdm9-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c955d03b1b.mp4?token=crtiuK82g-Lo4Ri601miqex92pta4pzlVLtHaD6gMH3BaO-HW9UMRzx-3j0__jImz1FNeniSRMF0bnPs6s5479YqF9KvJPQjdZOIGnTMsNHAY7vzZ1oECg-2Hc_mAUgrrdd7UoqRWv_QEkbOK89EiJ_lP4N98Lx55QmlRnLFVpmauyDIXLWd7Yx61W3vt7Ag21VL8bgl2fzBCmp3MOI6nYElBJerADz-IdHWOmYcsZQDNX7HxBHGjKRa5kZyfUciW-GcaHzYcdv_14NhBAZxAP-Oa6G8rjL7jdhVv47sG_7OdYXyDzb1mzZKpVAgkiSyLx3x-1TbKhkoF2A8Fdm9-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأميركي:
نطلق الهجوم الاقتصادي على إيران، توقف التراخيص العامة التي كانت تسمح ببعض التحويلات المالية إلى إيران - بيان وزارة الخزانة،أي عدو يسهل غسيل الأموال نيابة عن إيران، سيتم استبعاده من نظام الدولار الأمريكي،حان الوقت لقادة العالم للاختيار بين الرخاء والعزلة وبين السلام والإرهاب وبين أمريكا وإيران.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88469" target="_blank">📅 20:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88467">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHl8KywXt-c2tbJqdo-1xdj3MsGPROTi_wnKIuAoEXIvkmcUuREgaigUv4v9HQP-ilv7ivlSLJM49_CGJSfdl8slznkM3xlmn-k4BTwBAUyirUaGSoILrPv2HnXpLHb31O8YiyyM3xyoOLXyrB2U6YbPNqdNkWpYg-JfjrKfRjb5yrleeJ6HAnAGesz7fb6hP2oKEJK6GifLcJJocSll0hrJh-oWmpj87RVXPqaVAry6bsbfKfe5nPn4Xk2dNzLUdn1uTx1ZaZyiECNyAJqqhIbhotKWauNsaQxWk1nE4ulug2CxeYzu-9aF1vVasJDzd1K0HG2g53qZYhCPPMpLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_ZAl_26s_Elk9Jeo-94SaOKJgewgvzpCxtm_g1yh4EajSrq9fUXLXFiDqnoghk95_l3un5O0D2V6BMzbz4SGm0LaJXTLFY5XGp6fCECkrpXpz-xawwE5E1ikoOPsDsg7NYx9QyAx7cFfS2orfMg5-ZhxuhPLQcTgTmdCourm6NL53yHK4DdITfDIhQ5iBPgnjZQSeRDhynlDD9YZ35p5EPRp83B7s_2_2TqamRkfZAZvq1sRCxjEO_q-FJRy0opQZqzhDRO2uE1hOHJdBNUn_ii32SSy2xUuH74uDh-5r7LzdL4sx9yMQnZwruYVxXrsjjYDONb-HgIY9JYQZmulQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇰🇵
ترامب يعيد نشر صور قديمة تتعلق بلقائه مع رئيس جمهورية كوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88467" target="_blank">📅 20:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88466">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6dnL65VuL86mo0KqwZcs3XaZM6DONeoo4gX6qKyMOi_mq6lpTDPowQiShVugVTXb1jFPRWKQg_Gd5Y_7YhwmOUQPgwXxIBko2jYYKVbzc3p7hEoMml4Ink3FG4nXMNZmF-Rsy3n_l3jM00lM4B6OTOXj2qGnA4650TTqi6VQxA9PnG1h5dlb3zmDUlFHQC7j3f8KmUqSBmao4rJDO2yBrHXaEY1tBv2u3UR_p3aAWynQVAYZBYUUN4p43l5_Wmjr31H_P_fcZtRGQsxW1zcsZ4mvcazQghe7q9GGFbt7DEHGo3siVgm8DgMgPZa1BJ25jjwes32PG97o5kJbQqA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف:
يدرك الأمريكيون أن لا أحد سيصدق هراءهم؛ فأمريكا ليست في وضع اقتصادي يسمح لها بتقييد علاقاتها مع الدول الأخرى أكثر من ذلك.
‏أعلن شركاء إيران التجاريون، سواء في وسائل الإعلام أو من خلال إرسال رسائل إلينا، أنهم لا يعترفون بهذه التصريحات في أي مكان.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88466" target="_blank">📅 20:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88465">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMMpX_IEe1IaXfGzjYXdt7Beg4wCQesXhMv_h69Bi7eg0HxwXk4aKV25nv3O4i_3er7nLwxBCJSlO9jl_TIFwYcElA_bF_mSbHJe6SL_evI6JG23JJqch1HRi0cXzNSAv1I-FeYCK6y5vd_SRWzr8y2JxCxgQIam-SdrdcpdldepYv9_DXw_Im47pfSIpMZmVDWyTiMEMjTurR10kQ3z0XYZFS6cVwY9uti9yU8GrCGt5q62GP7oPpjgpRDh_7Ky6wuixDCEy2HYa2MPzfB24t3THEZ3WbdWARUTjMPYcAPdTCBH0egC657bDj02JCbc9vC8I8JLp8vZ2ECeVDV_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88465" target="_blank">📅 20:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88464">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇱
🇮🇷
نتنياهو
: حاولت إيران اغتيال أحد أفراد عائلتي.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88464" target="_blank">📅 19:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88463">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88463" target="_blank">📅 19:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88462">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b5c9408c.mp4?token=OVOcmGTdXAu-2fHL4CclpaGoZ72z5oVwX7SrYeRgaVFq0dWYuDt6bgMLqdGEVQ1wvZWnWK5LodbDj9JVLFyOIpDkbTCiJUia7HJ0RMSiD84c0avBCR_2UuEhNq7t2NRWKm4coxPruNRxr8Z3e4ZPKWKRLagtSNOTkZWmkSPn5Y2Iu0PRaWXp6_bHSCCGW2_eVC8NQ3xX4kfd9v1fZgBbIemK72jJzQUCd3VaxtANXmsGI7Fl3doIzUqAsp5Jv67QgP7l51aEwv_SfOq274fzsL5oZwCrX9w0kpxrlna9fZQOA84lvjKw_iP_jG4ZaJ3vzLZoeh6qvrtYU7mWlQw-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b5c9408c.mp4?token=OVOcmGTdXAu-2fHL4CclpaGoZ72z5oVwX7SrYeRgaVFq0dWYuDt6bgMLqdGEVQ1wvZWnWK5LodbDj9JVLFyOIpDkbTCiJUia7HJ0RMSiD84c0avBCR_2UuEhNq7t2NRWKm4coxPruNRxr8Z3e4ZPKWKRLagtSNOTkZWmkSPn5Y2Iu0PRaWXp6_bHSCCGW2_eVC8NQ3xX4kfd9v1fZgBbIemK72jJzQUCd3VaxtANXmsGI7Fl3doIzUqAsp5Jv67QgP7l51aEwv_SfOq274fzsL5oZwCrX9w0kpxrlna9fZQOA84lvjKw_iP_jG4ZaJ3vzLZoeh6qvrtYU7mWlQw-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏صور الاقمار الصناعية تظهر قيام القوات الأمريكية بزيادة عدد طائرات التزود بالوقود المتمركزة في الإمارات تدريجيا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88462" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88461">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يوافق على منح فرصة امتحانية واحدة لطلبة الثالث المتوسط والسادس الإعدادي (بفروعه كافة) الراسبين بما لا يزيد عن (4) مواد للعام الدراسي (2025- 2026)، على ان يؤدوا الامتحان ضمن دور خاص تحدد اللجنة الدائمة للامتحانات العامة موعده لاحقاً.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88461" target="_blank">📅 19:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph0pCNc2xDSVI60MhRA5-85vMDYTHwU15c1KwJDlYijRw3W8-llCModus5p6cMUgtMtd-zjFAcZhPo_Pf_qiiCjlKdyRkhv1xYNwMAGCv1wJ53_WcEB7NRrGR3A_cqXzWWnb6CgDaTG4RAcTY-qLl3fH2rPbSN072PoSSZuLz6ObIwA3Fj841FZNBctTRSPwOfZYBy6T7habWgMmciPvSCF7ZYFsmPEsIEcfeu3ovDbnu09CgerBGyBUnHqVg81fPjcE9YnhxLwfr7TK5gnDbRw2EKyscwZvi3jxCCKVEP59XLCvfZj3DNqRhd7WMQ2JxgKeVoRxarCCQN0WqnicPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي مصطفى سند:
بعملية نوعية وبالتعاون مع جهاز الأمن الوطني، فككنا الآن واحدةً من أكبر الشبكات التي تُهرّب الإنترنت (المدمج) والفضائي غير الرسمي، وتعيد بيعه للمواطنين والشركات، وتمت مصادرة الأجهزة واعتقال مدير الشبكة الواقع مقرها في العاصمة بغداد (الأعظمية)، كما تم رصد شبكات أخرى سيتم تفكيكها واعتقال افرادها تباعاً.
وتتجاوز المبالغ المهدورة للانترنت المدموج والفضائي غير الرسمي، اكثر من 100 مليار دينار بالسنة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88460" target="_blank">📅 18:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇫🇷
الرئيس التنفيذي لشركة توتال إنيرجيز عن ارتفاع تكلفة الشحن:
نشتري براميل النفط من الخليج بسعر يتراوح بين 50 و60 دولارًا، بينما تضيف تكلفة شحن البرميل عبر ناقلات النفط العملاقة عبر مضيق هرمز حوالي 10 دولارات. وهذا يعني أن تكلفة الشحنة الواحدة تصل إلى حوالي 20 مليون دولار.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88459" target="_blank">📅 18:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88458">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88458" target="_blank">📅 18:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88457" target="_blank">📅 18:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الامين العام للامم المتحدة ‏غوتيريش: توقفت حركة النقل تقريبًا في مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88456" target="_blank">📅 18:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88454">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88454" target="_blank">📅 17:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trBZ7ry_xZPPgFbahsiQGUowIhV2t6WmKGjUULKJmVqb5JVHPnTIc8kMW9TIcQfVxHZFUXUKtkbmGuhIdbCtRzbc0G8sSWkefn9rus5j9CGzsNzasfrYmDT_BveS5PTTxOKUYLEaoEFOUm6w8RN1TBNLReDa7l-n9qHygTQp2MW4V5Fg7E3iJWy-2DBiWx16R8mdwBClZqziM74vZcf-640eaTqU8cRXemaC1lgQFJONqe845b1-CuEOG5PQfAHLhiDKaReYOa0_Q1iidk8m3h821NaGEGPmyNbVEDtOQB3KLC2TWUig5JUr980P1ljWDCi5G3AbX6CqwzI9Avh3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPTGk6h-2Jpb45nF1g7P4WnGuvdwppUXmfzLIrfO3eP0zZ85QusniVvghWtxGy04S932tlOIYybYxAS7e26rH_DxaSuf400nBWM5fZxQSEk2hfxHXEjM99h6tVJNhZZHm8uPm4piVBp3iXJaK3aRRKA_iLA2ouWGYXeFxWeIsVFGyKte4_02woaxQxNaN8bCs2YDoRyvyuECs7EDaWkHz08kuEbJlSPyu1_yLgbuW8ZfpSNvccj3ImdXwGCG6Ma8QHmRzHERfhax6odB8RekY2TNeHStie-lRM5uHJRxOTfpvdPeFDBwK2mVKUPIdoi3x5Jcje72lsYx-WRYlC-tCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد ضربات من أنصار الله في اليمن   مستودعات أسلحة العدو السعودي ومرتزقته تحترق في منفذ الوديعة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88452" target="_blank">📅 17:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef5880eec.mp4?token=HGsFwI3-Pj95fhKOItAPhpOQLqeUIt3UQd-PdgZr3a_nxOZDYAzQmMMFj0VAPYbpJUXJ0-sPqabweQLcHvaFwvvIvv6rkvrZwCSAjAUngXbqgV5BYIAkIg0L7r6lCimYcqa_KJprfCeTNvlu7TWLwOhb0rVt15ddJ-1xF4jLRtth03a6SuOeI4HQz83koDKpH0qk4Nf4mTnph10KdsY3Wv5mrj5MXp2ZtA32ro7EMfBaZUMY2ddD8ZlWEe2W35YMvYzngb9HyGrD4q6yU-qxWwjPT4ieOZi8zStGSvdQOv0BAk43UZo_209V9l1xVOB1FxsRN60lfiUkIaT4zYArAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef5880eec.mp4?token=HGsFwI3-Pj95fhKOItAPhpOQLqeUIt3UQd-PdgZr3a_nxOZDYAzQmMMFj0VAPYbpJUXJ0-sPqabweQLcHvaFwvvIvv6rkvrZwCSAjAUngXbqgV5BYIAkIg0L7r6lCimYcqa_KJprfCeTNvlu7TWLwOhb0rVt15ddJ-1xF4jLRtth03a6SuOeI4HQz83koDKpH0qk4Nf4mTnph10KdsY3Wv5mrj5MXp2ZtA32ro7EMfBaZUMY2ddD8ZlWEe2W35YMvYzngb9HyGrD4q6yU-qxWwjPT4ieOZi8zStGSvdQOv0BAk43UZo_209V9l1xVOB1FxsRN60lfiUkIaT4zYArAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد ضربات من أنصار الله في اليمن
مستودعات أسلحة العدو السعودي ومرتزقته تحترق في منفذ الوديعة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88451" target="_blank">📅 17:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmwJiRwvJw5wOaXQYAZt9KWbTkTwG1IWb6WZWp9QXBG0-a5ny4KjWmIxcXJxf-VmTX3_s0lAKDanhctoKmfwfUjoW7Fk7_pxbQ4ID-6LWJ-ftYhrYvPUNcsxKqagm0RK6wqv1GSIeKMv5EJR-WWVIF84YID7eTv3lJqb9O7itvFUU-AOTXLlMPyTdCAKHSTz70B4etWFZMOPk8V2bVEKej-bqHth6YXr709-n6q2yEKmJ6oUKB1kYGY41cZLdVgIyzTzq4oX7-SrMkEtwd2b97BXyecqy9AVa6AJR9TtmyvWe5V6kZ9Lx_etR9JeIHyF86mx95xJzsQB-g5tx1VxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب الترجمة بتصرف " كندا ٥٦ لسنوات طويلة وجانت ناصبة علينا "</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88450" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c68e0f99.mp4?token=hlsugf0gYaDPOoVKyldhqu2nJp3W2fd2Caob_Stu3kxBYtCXo6I-e80IaRZDqWHgimZmX8XFTTttby8YzWkBNT4vkbxibyhm0ApGiGZeWn8y_ideEycXCB-H7i-JI7ac3RbjqPfMOjn3NfdUAYZQZB3XaMZrta2fx0OHpoKyWZiSlBhuvy20Wvha_-QhL819MlpCtQjnOKEFuQDRrIehuTUXYdE5zDfepoyh0KNzS_EtdNcri7nCiB3X7JEZ8qbTN8LVZU4sLZbtq86qJIh4MLYl420_UDwtZUwXPZwYtrD-NllhXwbkLaUFAndl1deww1r1tN57zkADLVNC5MhNng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c68e0f99.mp4?token=hlsugf0gYaDPOoVKyldhqu2nJp3W2fd2Caob_Stu3kxBYtCXo6I-e80IaRZDqWHgimZmX8XFTTttby8YzWkBNT4vkbxibyhm0ApGiGZeWn8y_ideEycXCB-H7i-JI7ac3RbjqPfMOjn3NfdUAYZQZB3XaMZrta2fx0OHpoKyWZiSlBhuvy20Wvha_-QhL819MlpCtQjnOKEFuQDRrIehuTUXYdE5zDfepoyh0KNzS_EtdNcri7nCiB3X7JEZ8qbTN8LVZU4sLZbtq86qJIh4MLYl420_UDwtZUwXPZwYtrD-NllhXwbkLaUFAndl1deww1r1tN57zkADLVNC5MhNng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوة من فوج مغاوير الرابع تتجه نحو الجسر المعلق</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88449" target="_blank">📅 16:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc052bc00.mp4?token=Yize57tKseAk8tMxVHP6zSX2Pee3_oUw6WGq0KGnuMWhKsYYVqmOAkqq80PQP69nAY_eu72NYxCQYh1jquti7tH0CKRJ6uec26VB1qo70lNX-o65aIWRfvxHffbjOcBPJz5Mc-HLKMORUOxb0WuBB09UQ7o3fYEPt4XkBoLogEuNcPH98P5_6lYw72nv4fyn4I2TS2w4ZB64sJkXVCmZJIkD9F5Lg_NQU6kfSiRQfR-IVkCMFnAkJlcTNeSitbFFm_x65uB7aaQajORZ1aWcBu3nYHzDxOR4hfv9FuFEegRkMFGlEBkwWFvbG7-1NId5uhC75xjVYXsFzUIbY36zxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc052bc00.mp4?token=Yize57tKseAk8tMxVHP6zSX2Pee3_oUw6WGq0KGnuMWhKsYYVqmOAkqq80PQP69nAY_eu72NYxCQYh1jquti7tH0CKRJ6uec26VB1qo70lNX-o65aIWRfvxHffbjOcBPJz5Mc-HLKMORUOxb0WuBB09UQ7o3fYEPt4XkBoLogEuNcPH98P5_6lYw72nv4fyn4I2TS2w4ZB64sJkXVCmZJIkD9F5Lg_NQU6kfSiRQfR-IVkCMFnAkJlcTNeSitbFFm_x65uB7aaQajORZ1aWcBu3nYHzDxOR4hfv9FuFEegRkMFGlEBkwWFvbG7-1NId5uhC75xjVYXsFzUIbY36zxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني   انتشار قوات سوات الداخلية لاول مرة بالقرب من مداخل المنطقة الخضراء بالجادرية وطلب إسناد من الشرطة الاتحادية من جهة المسبح إلى فلكة الحسنين .</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88448" target="_blank">📅 16:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
مصدر امني   انتشار قوات سوات الداخلية لاول مرة بالقرب من مداخل المنطقة الخضراء بالجادرية وطلب إسناد من الشرطة الاتحادية من جهة المسبح إلى فلكة الحسنين .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88447" target="_blank">📅 16:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مصدر امني يوضح لنايا   قطّع طريق مطار بغداد الدولي على خلفية زيارة قائد الجيش الألماني للعراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88446" target="_blank">📅 16:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne6rumFq-S-yJBsUX_SMTzD1P_gJqjnWZBEHlcA9S7KwGmSPHQTV30hgfFt2eqalUf6aOdAHxs3kcvk5VStxMXDExhGHxVoaGDFyTi3I10xiKq3KjN2m07fRBtbTpL4L-EDm-Hemi-Gq7802SWonw3GSkdEEWlWfbtopIms8KC4D4eK4z-HGUuJyl0DR-vRHM9NaxMCaZpzYI5MpHUsvMFxXVs_XnNDSXeTrAHYYbj-gqmWyWvw-CJ13ZvfBR2GUhSXjmulcUchWx-ZJ1ULVBohkHc9ir6XGk4WJ_79VSo8yrZ4xlUTR9pD8KAzFdsTjymt2dJPYCxnCtevpgeFOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القوات الامنية العراقية تضبط (428,794) قطعة من الأدوية البشرية المهربة وغير المفحوصة في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88445" target="_blank">📅 16:29 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
