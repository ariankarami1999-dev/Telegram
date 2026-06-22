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
<img src="https://cdn4.telesco.pe/file/lMl5g51ZY1kgEnTdTS-wh39DZmgxhu1bClatYheJGlI7A7osp3pR45yBA4A_3MHFpSXa5ZHKtIF2Ndci_7HXVYqHuNYt4zEUZmbo4uFRlCi9Q9KYng1l072B9cYOP55cVCHaQba2PH8GiaoG0sLQyfDimVEdF3o0qFs_0wL90pk4VHj4b-SBT0pdQNUNAm_ulDuZ0bZY0U3wwLjknqWxrP_QlqCqFS55jCP8XHa8O3xAAq8Scyjte8cLOfChDU7tTsBSMe9dQybye4Wp52ziXK6c8sJTtHqASsg7Lp5t0R6lyqFzKnGDLs7eaL4Q51SWWwut5vv5e2iq3tf8hstuIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-79616">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">محافظة الديوانية تعلن تعطيل الدوام الرسمي يوم غد الثلاثاء بمناسبة ذكرى استشهاد أبي الفضل العباس (عليه السلام)</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/naya_foriraq/79616" target="_blank">📅 16:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79615">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
القضاء العراقي:  ارتفاع حصيلة الأموال المضبوطة بقضية وكيل وزارة النفط لشؤون التصفية عدنان الجميلي والأطراف المتورطة معه لتصل إلى (10) ملايين دولار أمريكي و(31) مليار دينار عراقي. الجهود المستمرة أسفرت يوم أمس الأحد عن ضبط ما يقارب (20) مليار دينار عراقي كانت…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/naya_foriraq/79615" target="_blank">📅 16:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79614">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏴‍☠️
‏انقطاع واسع النطاق للتيار الكهربائي في الكيان الصهيوني عقب حريق في محطة لتوليد الطاقة في مدينة كرميئيل.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/naya_foriraq/79614" target="_blank">📅 15:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79613">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بيانات تتبع السفن:‏
ناقلتان صغيرتان للنفط الخام، تقل حمولتهما عن مليوني برميل، تبحران عبر مضيق هرمز إلى خليج عُمان فيما ‏دخلت ناقلتان عملاقتان إلى الخليج عبر مضيق هرمز لتحميل أربعة ملايين برميل من النفط، إحداهما متجهة إلى ميناء البصرة العراقي</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/naya_foriraq/79613" target="_blank">📅 15:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79612">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4dac33f4.mp4?token=tLpYTf4gEs3OkFgpZTak0h_4Euq3DRkPK0GpAH32pZQ2PyK_7YEAOJHkh2WuLH8D2pT36HdqFLa0zwyWkSaYB0E26Q2jGdFQUmfO7E05028Bez1b4Fu7hsTq1tmpm_r0a1dkSjMSnJtyMpdFREneezizzlkDmScfCZAR2D8xGtUFVrAKz2BiNAr3qEBjw4ioNK21T5vgNe0gLStet1FGGiHDj3ecB25lPbGuUv_6Z4WL87iYDMKn0-QffdIx2OA0Brg38uuZ50wM5UGX2W-mvD7mB12vlXFd_6iCS4TpB8B32imRmSZBq7NhTjBAGLwtUuf_NeL71JRO97JdVHnTazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4dac33f4.mp4?token=tLpYTf4gEs3OkFgpZTak0h_4Euq3DRkPK0GpAH32pZQ2PyK_7YEAOJHkh2WuLH8D2pT36HdqFLa0zwyWkSaYB0E26Q2jGdFQUmfO7E05028Bez1b4Fu7hsTq1tmpm_r0a1dkSjMSnJtyMpdFREneezizzlkDmScfCZAR2D8xGtUFVrAKz2BiNAr3qEBjw4ioNK21T5vgNe0gLStet1FGGiHDj3ecB25lPbGuUv_6Z4WL87iYDMKn0-QffdIx2OA0Brg38uuZ50wM5UGX2W-mvD7mB12vlXFd_6iCS4TpB8B32imRmSZBq7NhTjBAGLwtUuf_NeL71JRO97JdVHnTazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
انقطاع التيار الكهربائي في محافظة السليمانية شمالي العراق بعد اندلاع حريق في محطة شواركورنا لتوليد الطاقة.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/naya_foriraq/79612" target="_blank">📅 15:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79611">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الكيان الصهيوني يقرر نشر 50 جندياً من أصول إثيوبية على أرض صوماليلاند</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/naya_foriraq/79611" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79610">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تعيين المقدم "ج" قائدًا للكتيبة 52 بعد مقتل السابق على يد حزب الله.</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/79610" target="_blank">📅 15:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79609">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏قطر: قضايا مثل الملف النووي بين واشنطن وطهران قيد المراجعة</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/79609" target="_blank">📅 15:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79608">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
المفاوضات الجارية تُتابع بعزة واقتدار وفي الإطار المحدد من قِبل سماحة قائد الثورة.</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/naya_foriraq/79608" target="_blank">📅 15:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79607">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسعار صرف الدولار في بغداد ترتفع:
100 دولار = 159 الف دينار عراقي</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/naya_foriraq/79607" target="_blank">📅 15:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">#ترفيهي  فانس: لقد أنشأنا آلية يتم بموجبها استخدام الأصول الإيرانية التي سيتم رفع تجميدها لشراء المنتجات الأمريكية وإثراء المزارعين الأمريكيين.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/79606" target="_blank">📅 14:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏فانس: كوشنر يعمل مع القطريين لوضع آلية موافقة أمريكية على الأصول الإيرانية غير المجمدة.</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/naya_foriraq/79605" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79604">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏فانس: أردنا وضع آلية تسمح لنا، في حال رفع التجميد عن الأصول الإيرانية، بالحصول على موافقة على تلك العملية، وسيتم توجيه الأموال لشراء منتجات أمريكية.</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/naya_foriraq/79604" target="_blank">📅 14:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79603">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترفيهي  ‏فانس: إسرائيل تقول إنها لا تملك مصلحة إقليمية في جنوب لبنان</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/naya_foriraq/79603" target="_blank">📅 14:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79602">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فانس: أحرزنا تقدماً جيداً جداً بشأن لبنان وأنشأنا آلية لفض الاشتباك.</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/naya_foriraq/79602" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79601">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فانس: قد يزور مفتشو معهد مهندسي الكهرباء والإلكترونيات إيران في أقرب وقت اليوم</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/naya_foriraq/79601" target="_blank">📅 14:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79600">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فانس: هدد الإيرانيون بالانسحاب، لكننا كنا نتفاوض حتى الساعة الواحدة صباحاً، لذلك لم ينسحبوا.</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/naya_foriraq/79600" target="_blank">📅 14:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79599">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏فانس: سأعود إلى الولايات المتحدة اليوم، لكن الفرق التقنية ستواصل المحادثات</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/79599" target="_blank">📅 14:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79598">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
القضاء العراقي:
ارتفاع حصيلة الأموال المضبوطة بقضية وكيل وزارة النفط لشؤون التصفية عدنان الجميلي والأطراف المتورطة معه لتصل إلى (10) ملايين دولار أمريكي و(31) مليار دينار عراقي. الجهود المستمرة أسفرت يوم أمس الأحد عن ضبط ما يقارب (20) مليار دينار عراقي كانت مخبئة في إحدى المزارع، بالإضافة إلى إحباط تهريب (5) مليارات دينار عراقي في إحدى المحافظات كما تم ضبط وحجز (70) عقاراً، و(21) عجلة حديثة، إلى جانب مصوغات ذهبية تقدر بنحو (3) كيلوغرامات</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/naya_foriraq/79598" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79597">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏فانس: ستستمر المحادثات الفنية في الأسابيع والأيام القادمة</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/naya_foriraq/79597" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79596">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏فانس: نريد وضع آلية لعودة مفتشي وكالة الطاقة الذرية إلى إيران</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/79596" target="_blank">📅 14:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79595">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فانس: وضعنا آلية من أجل تفادي التصعيد وإطلاق النار</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/naya_foriraq/79595" target="_blank">📅 14:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79594">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فانس: لقد أحرزنا تقدماً جيداً للغاية وعملنا آلية لضمان استمرار فتح مضيق هرمز</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/naya_foriraq/79594" target="_blank">📅 14:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79593">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فانس: لقد أحرزنا تقدماً جيداً للغاية وعملنا آلية لضمان استمرار فتح مضيق هرمز</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/naya_foriraq/79593" target="_blank">📅 14:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79592">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-06-2026 مركز قيادي مُستَحدث تابع لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/naya_foriraq/79592" target="_blank">📅 14:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79591">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
قائد الدفاع الجوي الايراني:
القوات المسلحة الإيرانية في حالة تأهب بنسبة 100% ونحن جاهزون لأي سيناريو من جانب العدو. اليوم، تواصل وحدات الدفاع الجوي العملياتية في جميع أنحاء البلاد صمودها في الدفاع عن سماء إيران الإسلامية المقدسة. وهذه الشجاعة والحماس لدى أفراد الدفاع الجوي المخلصين مصدر إلهام للشعب الإيراني النبيل.</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/naya_foriraq/79591" target="_blank">📅 14:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79590">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📰
سي إن إن عن دبلوماسي:
تنفيذ مذكرة التفاهم بين طهران وواشنطن عاد لمساره الصحيح.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/79590" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79589">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">محافظة ميسان تعلن تعطيل الدوام الرسمي يومي الثلاثاء والاربعاء</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/79589" target="_blank">📅 13:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79588">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">محافظة واسط تعلن تعطيل الدوام الرسمي يومي الاربعاء والخميس</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/79588" target="_blank">📅 13:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79587">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
🌟
مكتب الشهيد اية الله العظمى السيد علي الخامنئي (قدس سره) يكشف عن تفاصيل التشييع في العراق وايران:
عقد صباح اليوم (الاثنين) 22/6/2026، إيمان عطار زاده، المتحدث باسم لجنة عروج  الإمام المجاهد الشهيد آية الله العظمى السيد علي الخامنئي، مؤتمرًا صحفيًا استعرض فيه تفاصيل مراسم الوداع والتشييع والمواراة لقائد الثورة الإسلامية الشهيد في إيران والعراق، وجدّد التأكيد على شعار المراسم ورمزها، معلنًا برنامج التشييع في طهران وقم ومشهد والنجف وكربلاء، ومشيرًا إلى المشاركة الشعبية الواسعة والحضور الدولي المرتقب في هذه المناسبة.
عُقد صباح اليوم (الاثنين) المؤتمر الصحفي لإيمان عطار زاده، المتحدث باسم لجنة عروج الإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، بحضور حشد من الصحفيين المحليين والأجانب في رواق كشوَردوست بجوار موقع استشهاد الإمام الشهيد.
وفي معرض شرحه لشعار مراسم تشييع الإمام المجاهد الشهيد، قال المتحدث باسم اللجنة: إن مراسم الوداع والتشييع والمواراة ستُقام تحت عنوان «شهيد إيران» وبشعار «يجب أن ننهض»، وإن رمز المراسم هو قبضة اليد المضمومة المستوحاة من رسالة قائد الثورة الإسلامية آية الله السيد مجتبى الحسيني الخامنئي، إذ قال إنه عندما زار الجثمان الطاهر للإمام المجاهد الشهيد كانت قبضة يده اليسرى مضمومة.
وأضاف إيمان عطار زاده: أما في الفضاء العربي فسيكون شعار المراسم «قوموا لله»، وهذا الشعار هو امتداد لشعار «القيام لله» الذي وصفه قائدنا العزيز (أدام الله ظله) في الذكرى السنوية لرحيل الإمام [الخميني]، في 4 يونيو/حزيران من هذا العام، بأنه الأساس الذي يقوم عليه نهج الإمام الخميني الكبير والخامنئي العزيز.
وأشار المتحدث باسم لجنة عروج  الإمام المجاهد الشهيد إلى أن هذه المراسم لا تخص الشعب الإيراني وحده، وقال: من بلدان جبهة المقاومة إلى أقصى أنحاء العالم، يرفع أحرار العالم وأنصار الحرية الشعار الإلهي «قوموا لله» مستلهمين ذلك النهج نفسه.
وقال المتحدث باسم لجنة وداع وتشييع ومواراة الإمام المجاهد الشهيد آية الله الخامنئي: ستُقام أيضًا مراسم لتقديم التعازي من قبل المسؤولين الرسميين في مختلف الدول، والشخصيات السياسية، والنخب، والشخصيات الدينية والمذهبية والنهضوية والجهادية من مختلف أنحاء العالم، على أن تعلن وزارة الخارجية تفاصيلها لاحقًا.
وأضاف المتحدث باسم لجنة عروج الإمام المجاهد الشهيد أن مراسم تشييع القائد الشهيد ستبدأ يوم السبت 4 يوليو/تموز في طهران، وبعد يومين من مراسم الوداع ويوم واحد من التشييع في طهران، سيُشيّع الجثمان الطاهر للإمام المجاهد الشهيد يوم الثلاثاء 7 يوليو/تموز في مدينة قم المقدسة، ثم يُدفن يوم الخميس 9 يوليو/تموز، الموافق لليلة استشهاد جده الإمام السجاد (ع)، بعد تشييعه في مشهد المقدسة، إلى جوار المرقد الملكوتي للإمام الرضا (ع). وستُقام الصلاة على جثمانه في جميع هذه المدن.
وأضاف إيمان عطار زاده: نظرًا إلى الطلبات المتكررة من أبناء العراق، والقبائل، والعشائر، والنخب، والعلماء، والشخصيات السياسية والثقافية والدينية في هذا البلد، ستُقام مراسم تشييع الجثمان الطاهر للإمام المجاهد الشهيد يوم الأربعاء 8 يوليو/تموز، الموافق لـ23 محرم الحرام، في مدينتي النجف الأشرف وكربلاء، على أن تتولى الحكومة العراقية الإعلان التفصيلي عن برنامج المراسم.
وفي خلال هذه المراسم ستُودَّع جثامين الشهداء الدكتور مصباح الهدى باقري (صهره)، والسيدة بشرى الحسيني الخامنئي (كريمته)، وزهراء حداد عادل (زوجة قائد الثورة الإسلامية آية الله السيد مجتبى الخامنئي)، وزهراء محمدي الكلبايكاني (حفيدته)، إلى جانب جثمان الإمام المجاهد الشهيد.
وأشار إيمان عطار زاده، المتحدث باسم اللجنة، إلى الطابع الشعبي لهذه المراسم، وقال: وفقًا لتقديرات مختلف المؤسسات، فإن حجم الرغبة في المشاركة في هذا الحدث لا يمكن مقارنته بأي مراسم أُقيمت في السنوات السبع والأربعين الماضية. ولذلك فإن الجماهير المؤمنة هي أصحاب هذه المراسم، وقد أعلنوا استعدادهم عبر مبادرات مختلفة، مثل مبادرة «كل بيت موكب»، أو عبر وضع الحسينيات والمساجد في خدمة الزائرين لاستقبال المشاركين في مراسم التشييع في مدن طهران وقم ومشهد.
وأضاف عطار زاده أن مختلف المؤسسات الوطنية سارعت منذ الأيام الأولى التي أعقبت استشهاد الإمام المجاهد الشهيد إلى تسخير جميع إمكاناتها، عبر حالة تعبئة عامة، من أجل إقامة مراسم الوداع والتشييع والمواراة واستضافة الوافدين من داخل البلاد وخارجها.</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/79587" target="_blank">📅 13:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79586">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الرئيس اللبناني ردا على ترامب الذي يتدخل بالشأن اللبناني ويرغب بادخال سوريا لمحاربة حزب الله بدلا من اسرائيل:
"نرحب بأي مساعدة لإنهاء الحرب لكننا نميز بين المساعدة وبين التدخل في الشؤون الداخلية، إن بلدنا ذو سيادة ولا أحد يفاوض عنه".
لا دقيقة هذا يقصد ايران اللي تريد تنهي الحرب ببلده
وادخلته ضمن البند الاول
😄
.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79586" target="_blank">📅 13:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79585">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDuUx8eTQ-5zg82WlnNGS2w0jA_AmvqPOFcK5QL2fUfN-fm7w0_RphOPMmbsxjjv-cgffcXxGLqlZkLJwZFDB0yqn_3IXDaTdkjE-6SjemwHurd9p4vMX-dsgFCZCPGZkpgnfuQ0iuO8XC74asewvyP9rU_jnnWNpQTK3NcAtK69mZihq4GE89gJ6_0MXSr5D7-EyV2DCM_AcoT9g9KyKqiHgqmpdBNzZ4X21O2mYahhRnLSQfuCZPA2Mt4GOU3ghWP4nh23e-t1RQJw_BltiScuwzlozCk5dDHksWImQd4-tagmSAN8fjShoQ3giVle0zQIZkunji7BGZo8T6IRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارة الدفاع الكويتية تعلن عن رماية عسكرية قبالة سواحل العراق في الأيام المقبلة !</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79585" target="_blank">📅 13:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79584">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
سي إن إن عن مصدر إسرائيلي: إسرائيل تدرس الإعلان عن انسحابات رمزية من أراض تحتلها جنوبي لبنان.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79584" target="_blank">📅 13:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79583">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
مصدر محلي لبناني لنايا: جيش الاحتلال بدأ بالانسحاب من ارنون ومحيط علي الطاهر_ الليطاني جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79583" target="_blank">📅 13:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79582">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d909870b7e.mp4?token=Hzcsfok5fQAl6q5Hd1CyOR9Am1JCsOgOa1Fq5_sWkDb7ZbH0N2oFJFtmjU7SupE-Fjnu3rbjq6pzT08OjVJD3JeghBWg0-wPo9bZJNgp3bR02zhV0YJ2rU4fjClRBC_dVoS0EJNtvyRBfEUPz8gQzmzte-Db1qYjJpID2MzayaveTt1IiuIITO1gMrJmn7UPYxOq3UPFD1lGqxpIwnbyIJcSYME57PW6m0F3GwvsjuhwdS57PXbV94dq9T9h5CZHQfZ5X4q8oorJliNlaXn4hhAmcCHDKvGI7fLlo1FsolnwKf9stW7i0OnxLRe9tZNOOF3G7fX3ULQqeXT107vo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d909870b7e.mp4?token=Hzcsfok5fQAl6q5Hd1CyOR9Am1JCsOgOa1Fq5_sWkDb7ZbH0N2oFJFtmjU7SupE-Fjnu3rbjq6pzT08OjVJD3JeghBWg0-wPo9bZJNgp3bR02zhV0YJ2rU4fjClRBC_dVoS0EJNtvyRBfEUPz8gQzmzte-Db1qYjJpID2MzayaveTt1IiuIITO1gMrJmn7UPYxOq3UPFD1lGqxpIwnbyIJcSYME57PW6m0F3GwvsjuhwdS57PXbV94dq9T9h5CZHQfZ5X4q8oorJliNlaXn4hhAmcCHDKvGI7fLlo1FsolnwKf9stW7i0OnxLRe9tZNOOF3G7fX3ULQqeXT107vo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🙃
🇬🇧
هجمات صاروخية عنيفة تتعرض لها مدينة فورنيج الروسية من قبل أوكرانيا على ما يبدو هجوم بصواريخ شدو البريطانية .</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79582" target="_blank">📅 12:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
رئيس وزراء باكستان: تم الاتفاق على خريطة طريق نحو اتفاق نهائي خلال 60 يوما وإنشاء لجنة عالية المستوى لتوفير الإشراف السياسي</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79581" target="_blank">📅 12:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb9EjYYlzBhw4tOH7KhrJ9xBYuxQIeiVLeC0TA7PxQx_nuksOK4NLfsH8eUnW0MaRWjXoo_pOXWVAEfloLFeiUk1DqNR0Vobftvu4usb-btatb9RGWIyc288tSlU9dFJH6wQBHwiv6aEqiMmzuqqD48f-zDiTCUqL3Y5YCwbt1Fy0sf0yV1Jcfz3xy3Jwwq0tJsDWMjPixIOPqsg5HAcJQCtshOVor0pfcNZ4XtyLnKN4lDOTiN34uGDYleENKPxRMEYVOBKV-Q2Xxu3t3rOVNyUdxg3DV_7-JWH1TYyn_UM_fCOPNB8iPTWLozuCcEjzpoTKR4nEaBJrUf3WBdGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🙃
🇬🇧
هجمات صاروخية عنيفة تتعرض لها مدينة فورنيج الروسية من قبل أوكرانيا على ما يبدو هجوم بصواريخ شدو البريطانية .</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79580" target="_blank">📅 12:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
مصدر محلي لبناني لنايا:
جيش الاحتلال بدأ بالانسحاب من ارنون ومحيط علي الطاهر_ الليطاني جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79579" target="_blank">📅 12:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a10ac227.mp4?token=bLcdGCvLu5VnfuVZTmL3KPzabDx5fmWU8uuDkR_JjiokFP6pN4l_U9uwtZP2McBRThzgsFMQ-KRhf1PP69lzj2zu8x9-Wq8uwoNOAId7ONb1cpP_qMMHPgg_6lVgevdIoJ9P7xgjwJWBfUnGLTnP04JBYrtWSZDDL9Ifjey50DNCQNXBd9xIZ1WjHfeLfpJ4pzn_RLA27z_7mQm_0lhXpqh92k2uz77Fb9zGynCtLqm0xyHa_yCZ45gB41f7Pg4XTvn9ooTFl3vI660ce-noEBx1nrPsj5Ns5d2tFiEfLa2reJUZKFynwPVSOzrunjKIz9I_x8peSTpTSGCa5AsxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a10ac227.mp4?token=bLcdGCvLu5VnfuVZTmL3KPzabDx5fmWU8uuDkR_JjiokFP6pN4l_U9uwtZP2McBRThzgsFMQ-KRhf1PP69lzj2zu8x9-Wq8uwoNOAId7ONb1cpP_qMMHPgg_6lVgevdIoJ9P7xgjwJWBfUnGLTnP04JBYrtWSZDDL9Ifjey50DNCQNXBd9xIZ1WjHfeLfpJ4pzn_RLA27z_7mQm_0lhXpqh92k2uz77Fb9zGynCtLqm0xyHa_yCZ45gB41f7Pg4XTvn9ooTFl3vI660ce-noEBx1nrPsj5Ns5d2tFiEfLa2reJUZKFynwPVSOzrunjKIz9I_x8peSTpTSGCa5AsxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
4 غارات صهيونية استهدفت عدة عجلات في مدينة غزة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79578" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI4HcPaKcAT8H5IdLUq0KDoXdodKtm0bMaBHGx2VupJBoGxHApp3a9HQxgbh1PbmyAt4PvPBGsfafGXu9-g09TmgF0y6nRgsUUEPFm-YpbdQAXCkmNjjUXUVRa_uq0Mi7Fcnn7B3o58dbcWSyHV1vgx45abkCM3KIAspxCB0iPSDk_JsDrgm16Z8W3FftrP2EjsePWOlb2jGth8RrQj3Iarmyp_3HE_rPSB-NP3cPsf24kRjNq-5zSveDUaZqZyuY-Q5ccBXVDy3FmiHAPppPYD_quozlUZkO3rISvrbbmL2-SwB1i7rj_ia5rX49StdJobVDZm8Bg7qg-2QLGyAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الوفد الإيراني يغادر مقر مفاوضات سويسرا متجهاً إلى طهران بعد نحو 18 ساعة من المحادثات والمشاورات المكثفة
بعد نقاش مفصل.. تم اتخاذ تدابير حول بيع النفط الإيراني وإصدار التراخيص لصادرات النفط وتجميد الأصول الإيرانية
خلال الاجتماع الرباعي عرض الوفدان الأميركي والإيراني موقفيهما بشأن الملف النووي ولم يندرج ذلك في إطار التفاوض</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79577" target="_blank">📅 10:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79576">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
🌟
عمدة طهران يعلن تشييع سماحة السيد الشهيد علي الخامنئي (قدس سره) في العراق يوم 8 تموز.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79576" target="_blank">📅 09:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
موقع "زمان إسرائيل": إيران انتصرت على الولايات المتحدة و"إسرائيل".
إسرائيل في وضع مروع إنها تُدار من بعيد من قبل رئيس الولايات المتحدة، والحكومة موجودة على الورق فقط</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79575" target="_blank">📅 08:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇶
⚔️
محلل سياسي مقرب من الحلبوسي  يتهم كتائب حزب الله وراء الهجوم على الحلبوسي
والصحفية منى سامي ترد : حزب الله ما يدز مسيرة مجرقعة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79574" target="_blank">📅 08:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
وزارة الداخلية القطرية: نتج الحادث عن عطل فني أثناء التشغيل بأحد المصانع في منطقة رأس لفان الصناعية، وأسفر عن عدد من الإصابات، دون وقوع أي تسريب يشكل خطراً على سلامة الأفراد، فيما تواصل الجهات المختصة التعامل مع الحادث.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79573" target="_blank">📅 05:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f4af9e46e.mp4?token=L05EGBAlX02umlp8X2CYRT2oBufdgcSAjQiCqrKN0GAwGLC92YbRD3SRpJSprsKu36IBm2l68jRva7u4uv7WntGItEqtlZI94jPmLbunMB1DspiUqNSkh-iImpoy_trWf1OoIkNS6aLpAUWvggomhREjeR_Jqb4bspK32FjQ6REiuv5aVCNy4UQsRyVuCvgxpECArJYZRB0FZAp8O-QYH0m3Md644--y2gnvAT1LWeo6sC2PaMCq4H4DDgu0cdL9JO46onXkxEnBl6EIZJ1W1cKK35pwhl020u5LCmHlvt-Ec9Z8bP5h9scjY8czQZREm8jucY9MKmB4lC-EC2lIwStCvyeVxlBFAlcmxUceh0Br0SL2kdeElLMUzdJESjOOeqVJgo5xQ2NXTr0gNLxlq6zEF97hlNsO2V4EnvlB6Unnz3zgdHNDBNtJAL4wQjVmXSn7zh5VOiyhhElTDLaap6lP_chCSdcjzN3ijpYJuI7NaMEHhNA6UQAtjsJa8j24tl5X6Unf1ga1jus-aKif2DqWZVqLgULRZpegOKBrYUHsPTDWkSXwbTISzGH83InqYKARCV8fos_ehbxcmQ2hIo-6HTnjooLMfztw1dlEHbYdlUIlijQkrAb19A_e62oYxoXPTFvQZ3c5Y6Gvh95Lkf5vmZ8_JtJeXVBQmkVbJ5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f4af9e46e.mp4?token=L05EGBAlX02umlp8X2CYRT2oBufdgcSAjQiCqrKN0GAwGLC92YbRD3SRpJSprsKu36IBm2l68jRva7u4uv7WntGItEqtlZI94jPmLbunMB1DspiUqNSkh-iImpoy_trWf1OoIkNS6aLpAUWvggomhREjeR_Jqb4bspK32FjQ6REiuv5aVCNy4UQsRyVuCvgxpECArJYZRB0FZAp8O-QYH0m3Md644--y2gnvAT1LWeo6sC2PaMCq4H4DDgu0cdL9JO46onXkxEnBl6EIZJ1W1cKK35pwhl020u5LCmHlvt-Ec9Z8bP5h9scjY8czQZREm8jucY9MKmB4lC-EC2lIwStCvyeVxlBFAlcmxUceh0Br0SL2kdeElLMUzdJESjOOeqVJgo5xQ2NXTr0gNLxlq6zEF97hlNsO2V4EnvlB6Unnz3zgdHNDBNtJAL4wQjVmXSn7zh5VOiyhhElTDLaap6lP_chCSdcjzN3ijpYJuI7NaMEHhNA6UQAtjsJa8j24tl5X6Unf1ga1jus-aKif2DqWZVqLgULRZpegOKBrYUHsPTDWkSXwbTISzGH83InqYKARCV8fos_ehbxcmQ2hIo-6HTnjooLMfztw1dlEHbYdlUIlijQkrAb19A_e62oYxoXPTFvQZ3c5Y6Gvh95Lkf5vmZ8_JtJeXVBQmkVbJ5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إيران تجلس إلى طاولة المفاوضات من موقع القوة، وتعمل على ضمان مصالحها وحقوق حلفائها بالتوازي مع مسار التفاوض.
🇮🇷
الحليف الذي لا يترك حليفه
❤️
ما تذل شيعة علي</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79572" target="_blank">📅 05:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
🌟
🌟
‏بيان مشترك صادر عن قطر وباكستان بخصوص لبنان: اختُتمت الجولة الأولى من المحادثات رفيعة المستوى، المنعقدة في إطار مذكرة التفاهم الموقعة في إسلام آباد، بمشاركة ممثلين عن الجمهورية الإسلامية الإيرانية والولايات المتحدة الأمريكية، إلى جانب الدولتين الوسيطتين،…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79571" target="_blank">📅 05:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
عراقجي
: أسفرت الوساطة الدؤوبة التي قامت بها باكستان وقطر عن إحراز تقدم كبير في إنهاء الحرب في لبنان. كما تم تعليق الحظر المفروض على صادرات النفط والبتروكيماويات، ورفع الحصار البحري، والإفراج عن بعض الأصول المجمدة، وتنفيذ خطة رئيسية لإعادة إعمار إيران وتنميتها الاقتصادية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79570" target="_blank">📅 05:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
🌟
🌟
‏
بيان مشترك صادر عن قطر وباكستان بخصوص لبنان
:
اختُتمت الجولة الأولى من المحادثات رفيعة المستوى، المنعقدة في إطار مذكرة التفاهم الموقعة في إسلام آباد، بمشاركة ممثلين عن الجمهورية الإسلامية الإيرانية والولايات المتحدة الأمريكية، إلى جانب الدولتين الوسيطتين، دولة قطر وجمهورية باكستان الإسلامية، والتي عُقدت في منتجع بورغنشتوك بسويسرا.
سادت أجواء إيجابية وبنّاءة أعمال اليوم الأول من قمة بحيرة لوسيرن، حيث أُحرز تقدم مشجّع، شمل إنشاء آلية لمواصلة المحادثات الفنية.
واستناداً إلى مذكرة التفاهم، اتفقت الأطراف على إنشاء لجنة رفيعة المستوى تتولى الإشراف السياسي على جهود الوساطة، على أن يرفع كبيرا المفاوضين تقارير دورية إلى اللجنة، إلى جانب قيادتهما لمجموعات عمل متخصصة تُعنى بالملف النووي، والعقوبات، وإنشاء مجموعة عمل للمتابعة وتسوية النزاعات، بما يضمن التنفيذ الفعّال لمذكرة التفاهم، فضلاً عن النظر في المسائل الأخرى ذات الصلة.
اتفقت اللجنة رفيعة المستوى على خارطة طريق تهدف إلى التوصل إلى اتفاق نهائي خلال 60 يوماً، بما يمهّد للبدء الفوري في جولة جديدة من المحادثات الفنية. كما تم إنشاء قناة اتصال بين الأطراف للفترة المنصوص عليها في الفقرة الخامسة من مذكرة التفاهم، لتفادي الحوادث وسوء الفهم، بما يضمن العبور الآمن للسفن التجارية عبر مضيق هرمز.
واتفق الطرفان على إنشاء مجموعة عمل لتفادي التصعيد، تضم الطرفين والجمهورية اللبنانية، وبتيسير من الوسطاء، بهدف ضمان الالتزام بوقف العمليات العسكرية في لبنان، وفقاً لما نصّت عليه مذكرة التفاهم. ومن المقرر أن تتواصل المحادثات الفنية طوال ما تبقى من الأسبوع في منتجع بورغنشتوك، لمناقشة جميع القضايا ذات الصلة.
وسيواصل الطرفان الوسيطان بذل قصارى جهودهما لضمان استمرار المفاوضات في أجواء بنّاءة، وصولاً إلى اتفاق نهائي.
وتعرب دولة قطر وجمهورية باكستان الإسلامية عن خالص تقديرهما للولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية على التزامهما المتواصل بالحلول الدبلوماسية، وسعيهما إلى التوصل إلى تسوية سلمية للنزاع.
كما يشيد الطرفان الوسيطان بالدول الشقيقة والصديقة على دعمها المتواصل وإسهاماتها القيّمة في المفاوضات الجارية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79569" target="_blank">📅 05:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aae27ce1f.mp4?token=eCAA7wAnIEo9FDRzJ7UNucxV1Pe5puFD8sWmwO385a-iiSa7xeNPLpYu-tGy0U7Tt657THnvpYpJDnVViCnAlWSlg0P7HYT2CEuK3FK1fiWPUTM2KlOXfLN19n6BdXiUznUUI3M3A1w1jJE2pR2fIHGaQ4xNKSIYRwZY76htydNAmCMivS9bEInoYIdTf5adNKcmsdjsA-wS2Jb84h3fGUP3tPtJc4tVZUTO6eh4it7NEbrqZfwG9NqhlP70clzHiQtPRJFvB5cPqU3ElpNMWlGcgjjdxCMBEOty-EAM5_DHSSY_m2bWDv3e44j9fQY7-Jqf_Wj7zi1wDE4epNQYaqUdxuiWEGfGV0bcwJMLs0hsM0U8KPLkL16rWVFNJKpppbcTwwpxzxZJBpVsuAHyUK1EEnzqKyUk9tGR_qlewqfRlgt8zs7OMBAR07ydMKtwqFwh67aklIPMxa04IvIfGXoUxbpzt1NOu-tfOxXZhxAFv5s-JGQwKo7S4Yr2qhXrlYEEkKXyd8ZA7Cj5hmfLwvUVaIuYJ1kQOe5SEiU8iFS9GCUFg1LlehjddUK18h-w4J4LkQ6wqFlvFrOEJGlLt_TpcWIe6RzpbP9S_BRFoStswTZVaw8_-FRH5EJAKpeD_cCh2qhxI61k2ECrxKuKNm0bDBxBpjO1TwwZ2b_pKYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aae27ce1f.mp4?token=eCAA7wAnIEo9FDRzJ7UNucxV1Pe5puFD8sWmwO385a-iiSa7xeNPLpYu-tGy0U7Tt657THnvpYpJDnVViCnAlWSlg0P7HYT2CEuK3FK1fiWPUTM2KlOXfLN19n6BdXiUznUUI3M3A1w1jJE2pR2fIHGaQ4xNKSIYRwZY76htydNAmCMivS9bEInoYIdTf5adNKcmsdjsA-wS2Jb84h3fGUP3tPtJc4tVZUTO6eh4it7NEbrqZfwG9NqhlP70clzHiQtPRJFvB5cPqU3ElpNMWlGcgjjdxCMBEOty-EAM5_DHSSY_m2bWDv3e44j9fQY7-Jqf_Wj7zi1wDE4epNQYaqUdxuiWEGfGV0bcwJMLs0hsM0U8KPLkL16rWVFNJKpppbcTwwpxzxZJBpVsuAHyUK1EEnzqKyUk9tGR_qlewqfRlgt8zs7OMBAR07ydMKtwqFwh67aklIPMxa04IvIfGXoUxbpzt1NOu-tfOxXZhxAFv5s-JGQwKo7S4Yr2qhXrlYEEkKXyd8ZA7Cj5hmfLwvUVaIuYJ1kQOe5SEiU8iFS9GCUFg1LlehjddUK18h-w4J4LkQ6wqFlvFrOEJGlLt_TpcWIe6RzpbP9S_BRFoStswTZVaw8_-FRH5EJAKpeD_cCh2qhxI61k2ECrxKuKNm0bDBxBpjO1TwwZ2b_pKYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترند يشعل الرأي العام العربي،
بعد أن زعم ناشط عراقي، بحسب روايته، أنه وضع أنواعاً من السحر أمام موقع دخول المنتخبين العراقي والفرنسي بالولايات المتحدة بهدف التأثير على لاعبي المنتخب الفرنسي.
خوفك لا ينكلب السحر على الساحر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/79568" target="_blank">📅 03:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuBYww0V-LrhIQJHZ0kGAb63GT_Io8E2U1oWHBpYK0_rTkhe3NUh0GmBPEmzSjysQ1NS052YQbedeb0_H2OPFgKw8bhSSE8oAHmtNb641D4FwHuKIErZTkmqKYRM3_7weZZ3ADCizPRthoNoeJIV7PTZqI3azjWFOyC6Gqi2SoIgBzQrnnFro-xDR6s5EHXMKP3LqTrNuq9tTdunJfyWEekYbj3t1sZsEu4K678jf4ygmunhBo2iXC9Q2AssPKRRWO6FAc_ecWtTk5FpIhXYCSsZTInbKr8l9jH69A2Xm66w9Vzy0jabE0Lj7u1MTdHH7ukwxAp5D3HwN-LVB0gWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رسالة خاصة من المنتخب الايراني في غرفة الملابس إلى الإيرانيين وشعوب العالم أجمع
أحيا المنتخب الوطني مجددًا ذكرى شهداء ميناب المظلومين في لوس أنجلوس، وكتب:
من إيران القديمة، التي يعود تاريخها إلى آلاف السنين، إلى إيران المتحضرة اليوم، ظلت روح إيران حية وقوية.
جئنا إلى لوس أنجلوس بشرف، وتنافسنا بروح الفروسية، ونغادر هذه المدينة بكل فخر.
لوس أنجلوس، نشكركم على كرم ضيافتكم.
ونشكر جميع الإيرانيين الذين دافعوا عن إيران بكل قلوبهم وأصواتهم وأرواحهم خلال هذه الدقائق الـ 180.
نتمنى السلام والاحترام والصداقة بين جميع شعوب العالم.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/79567" target="_blank">📅 01:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwl5GmUM5xVnOe4FktQNPsf4zk1nZVUWxXkkpw57pM04phsV5BB_CNHd-avF0i2cW92RxOJvWvMHqgQCwOf-8ajm6bxtWbf--TKuijpe9zmmoYbDTOdk-ZjIsWEWJGW_NVUoxN3KrAEfna2MIlDZvfB0rcvMe6jBiLIFtmYLyse5lNUefFWBlsstd-Kdcgnc_Gpk24xDfPI_lZiBK-w29DdmvILPFYDNOzupHThFbXXmLnrUrpTuestORJ3ElDr0_IMGtmKzoq9rCej31dEkS4HjqrOXFHL8mhwCrGldqfkgpnGCS0HOkbcc2ztJXwWmHxG8SmrUp-Wv0epqe8l7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دفاع مقدس</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/79566" target="_blank">📅 01:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌟
‏مسؤول أميركي: التركيز في سويسرا انصب على آليات لتجنب التصعيد في لبنان.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/79565" target="_blank">📅 01:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bctBepCL7SgfGS9z5HmlErJCIrfGB77kQqvDjB95FQyOcWtdwhS2h_9q-Ad4hcx6yRXmhs03gpV_hMjKfzKXmlB0VvwWd1XjkPqhpnfjdvRNl7bJaE0rwYpOsGVvUndU9N0vwzkW0R68fvSMhr3r5oyMa5JMBQJRk56KMnM6NioVJ5rmoJ1DbORskVqBcwG2ZzN01NwedMq6WZUvH09B2xtAUkt70bSrxbl1sXtbJhpGOnTPWAmIw8GhKYqmdlCwQ3GDd6Tsop3S5TqkupxcbGKxgQFYUTDu_fmjjKBfejfyA7U1IrbiZXqVGj8ofOTItwWNd3i1w3pQHCOdJ4R3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
العراق لاول مرة   مبادرة تدخل حيز التنفيذ الان من وزارة الاتصالات العراقية برفع سرعة النت بمعدل ٢٠ بالمئة على ان تبقى نفسى الأسعار بالقيمة السوقية  …  برأيك هل سيحقق سند الوزير الإنجاز كما حققه كنائب سابق في البرلمان ؟!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/79564" target="_blank">📅 01:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-text">"
⭐️
If you have a
verified
Telegram
account with a blue checkmark, we kindly ask you, our esteemed subscriber, to support our channel by promoting the link and sharing updates on the channel."
في حالة تمتلك
حساب تلغرام موثق بالعلامة الزرقاء
نطلب منكم عزيزنا المشترك دعم رابط قناتنا بعمل تعزيز لغرض نشر حالات على القناة
⭐️
https://t.me/boost/naya_foriraq</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/79563" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbh6eAcbASOw9D894PTm7Dkmnkg3nqniFMUTP37nDDVMtRAq1tYqiDP5x-a6EPp7Qt9z6h7uh9l2QfHY3hhfE5XuflocatRyUeqPZ0yh88_VM8mlw6nrA2KAIobKkI_Had5lHl0ch7YA1GKPrTRKYaZEXkLFxVemLEUv3BwKlawrj1w4ewAV5bzeMSfxs41DDb4KLJKh_5kjp6vPSbP5RLlj6qOEbxFUgvsL7mWmV_j8oXO9lC-WrYUi8gP1s0h1JYfhXT9mB02zR6zOtTYm_l1CUTfAuCFz3V-Bbv2H5_OVbDK8Bu8mTjPqVDBX_dp5PRUskRqqydSnA39s3fT5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقع ميم مشهور على تطبيق اكس يصف صمود الحارس الإيراني بصمود ايران في مضيق هرمز ومنع بلجيكا من العبور نحو الثلاثة نقاط ..</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79562" target="_blank">📅 00:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1GHPbTQaODP2duEsodZPrllRjbGr1dsn-mx6WKk_WWqSm8XFsl2_fmTg6R8cyurAOK0gJ58VdqIwSdYZSyo8_6PMTeHrvI-YH6Cf2qE2DprXsm83Xod6lcC6AFkIJJvUJD5YhQn0l26DAugLANPpiNRGb5aLKM-AI5SS0c_XnjmUDQlIOjA1ihkCFduvezqmXZt3MkZihJmFG0etYLSgn0805SDdsnuYcnxhBJmo9djKMUA8Yce7pLxZBx8QK2CrIQKGkYeBaSBcvdiB-DYyVZy_0Hg4_-sFGBbpn2o8XGdSTQ-Oxp_BpOMwpGOKZKRBIRz-3_hXdDfDjusJSExXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
اهدای پرچم گنبد حرم مطهر حسینی برای تجلیل و بدرقه پیکر پاک امام خامنه‌ای
در اقدامی استثنایی و سرشار از نمادها و مفاهیم معنوی، آستان مقدس حسینی پرچم متبرک گنبد حرم مطهر امام حسین(ع) را برای تجلیل و بدرقه پیکر پاک امام خامنه‌ای اهدا کرد.
سید علی بزرگوار، فرزند خراسانِ عظیم؛ ملت عراق تو را نه بر دوش‌ها، بلکه بر دل‌های خود حمل خواهد کرد. چگونه چنین نباشد، در حالی که تو قهرمان تهران هستی و از «دروازه دوم خیبر» سخن گفتی</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/79561" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEtmPELCvwP_8WUqZsjpnHLM7EeyR40AUnCpvUD1rWvyzKFVX9jJ0BMoh7VzaKg-0akKraxZWmlppVyyb93bbotN8lbnS19NGoTdL2IIpxfJmHMlL299u2Vi-k7IFKNMsxc0ufwrif3Cw4HoHHXlVECwL5F8qphkfA24bGk8I1SRxxUS9sK-PZki68tUivvqnMjk0OyFXJU2QkIYhw_abGIzgNWS1fzYQW6KxiZNeU05M_6h4EPe7434HU88V0zJ0ZeFCMay_sKe25qXzcAJK-iDoKhrEJaWYtnpEwPc9fJo8OPxjmNDjeaCxcTBLIU6qKoSy1JNaQB7OuslELCZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دفاع مقدس</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79560" target="_blank">📅 00:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الغاء الهدف الايراني بداعي التسلل</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79559" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3wLQMU0aIZcnsFd1mKFyraI1OeEH7u9e7A-WFVMiRpy-7TU57tnQaR52DX-T9OmIm63kO6jAycqYA4wU682SmiqlGvGUXF7pzSzvltGgTrj5leQvEjfxg6TazMsA4Se4KzFzXUQHcX7B8Z9Lj2E8J-Myi2bOhc5iBA6uua9Wdzo-WjWUoMIEfisTbfzxDrKMCfCKH4cNu6BlkcjVMw26DYUlb8d_bG4QcTcgpfNtqisio5GPMlB40QMo2wV37NXVKmHOd47MpaSXYhqoF9gQwPxW6oK0b9GgRr00rHKbQFapTr7qaFrYyPRBfq853Xdacm8eO5_3JeMxeEeSM9tbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
العنوان الرئيسي في صحيفة نيويورك تايمز الفاسدة والفاشلة: "ما الذي تغير بعد ما يقرب من 4 أشهر من الحرب؟ المحللون لا يقولون الكثير." حقا؟ انتهى جيشهم، وذهبت قواتهم البحرية، وذهبت قواتهم الجوية، ومنصات الإطلاق والصواريخ والطائرات بدون طيار وتصنيعها، قد اختفت تقريبا، وذهبت المجموعتين الأولين من القادة، وتضخمهم بنسبة 250٪، واقتصادهم مكسور، ولا يتم دفع رواتب جنودهم، ومضيق هرمز مفتوح، والنفط يتدفق، والولايات المتحدة. سوق الأسهم والوظائف في مستويات قياسية. هذا ما تغير، أيها الجبناء الفاسدون وغير الأخلاقيين، وأكثر من ذلك!!!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79558" target="_blank">📅 00:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">طرد لاعب بلجيكي بالبطاقة الحمراء بعد تدخّل عنيف على أحد لاعبي إيران.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79557" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79556">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الغاء الهدف الايراني بداعي التسلل</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79556" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79555">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌟
استمرار اشتعال النيران داخل محطة الغاز بقطر مع عجز تام للدفاع المدني لاطفائه.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/79555" target="_blank">📅 23:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
دبلوماسي أمريكي: المحادثات مستمرة في سويسرا حتى الساعة ونقاش جدي بشأن مختلف جوانب الاتفاق.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79554" target="_blank">📅 23:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F21TlbLXSLdX0uLsPZYkXjvQ7vR53WGd6619Q_am7sLnjHKpdGjYq278_QJq2sZe40wk3CfrUM4ZbhgM0aaL6P-Tdp7cxndY8rjPSq2LjoWjGjtPt24T6RYaDU8IJfOfdSZ5qoXcziMpMOJTc3w_YqjltoLa6aOg-zGB8SYP4eQ-RJioCfQS86h8c14m5Yw07BLptv9GYpB16mjeQnfrp2zr117tVyLlHARdk2y4xckQOB6ILel5eKMv-0CLJgSgmgCuOWxYhk_aIOccyLNB1ZKizAWOWZkfehneR3DGtY4gNeTl0elxRiG3FVH0wkYv3ooCGfQx5K__I8agFK3FyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من أرض الولايات المتحدة، خيبر شكن يهز شباك بلجيكا معلناً الهدف الأول لإيران</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79553" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
دبلوماسي أمريكي:
المحادثات مستمرة في سويسرا حتى الساعة ونقاش جدي بشأن مختلف جوانب الاتفاق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79552" target="_blank">📅 23:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ac74e6ac.mp4?token=otyV9EVsD6pUQ637ZMw7mX_NMU5ZEdBqjetbpBAgXrwjMYNo6DhdVp-_t9mETspyRYT8zejU6ta3A9g30PiOMnT8hppDdve22YoElY7d8RD5N1uSgENZSMbRAlJfbfAHEBu8iflTVMS5NLxOm5Dvag2PwZlcEZ5L_dCpVkVqB64QGi0Ay7E6zERv-Bdls0p9ge0qjzt55oWkdfzUXgUkx0x2AW5woMi2SIBodGvIfyKB6si8DgLZzBtmAzKkYZB7DVvV99yBGgj0stM-Eu9VzUMu4Zkw3m-V09EhoOCq2LrHFHGixw4lyawRWnrHz1pMRt-6qxwwi8_CgkP5uASJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ac74e6ac.mp4?token=otyV9EVsD6pUQ637ZMw7mX_NMU5ZEdBqjetbpBAgXrwjMYNo6DhdVp-_t9mETspyRYT8zejU6ta3A9g30PiOMnT8hppDdve22YoElY7d8RD5N1uSgENZSMbRAlJfbfAHEBu8iflTVMS5NLxOm5Dvag2PwZlcEZ5L_dCpVkVqB64QGi0Ay7E6zERv-Bdls0p9ge0qjzt55oWkdfzUXgUkx0x2AW5woMi2SIBodGvIfyKB6si8DgLZzBtmAzKkYZB7DVvV99yBGgj0stM-Eu9VzUMu4Zkw3m-V09EhoOCq2LrHFHGixw4lyawRWnrHz1pMRt-6qxwwi8_CgkP5uASJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اللحظات الاولى للانفجار الحاصل في محطة الغاز بالدوحة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79551" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4w8ZuN_nusafeULEDjUeJD1AEyQz5kfuByqfY69dkKP61CkyRLLVq3taYwstiiu0skPhh7vW_uHUIK6z8ARhyyTuspMVdK3WQ4kvJvrLyLjLNekSbPI8Sd6xCfyZRJZeftpGrDxi0lM3ziW8M0lHo6psAJRpXkBcwd8fLy2rjM2OVlxG2_0i5EnGmSnpBAFIB_Wt7a4uyDmJRiSJmfkddqY75o9OODQbBqc4PK0IaKHHeMn_x1TEHAJdnWTQcghzP1MRR2NubFPrnVoryCfe53lf7c8TT2oyru_g2QsqpU6JKKO0wKxg0i9xmUIt3wPugKokWV9PQsDfmRq1u7rrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاني:
أيها الجنود الصهاينة المعتدون والإرهابيون، لقد تكبّدتم خلال أقل من أربعة أيام 100 قتيل وخسارة بشرية! إذا لم تنسحبوا من جنوب لبنان بإرادتكم، فإن ملحمة عام 2000 ستتكرر مرة أخرى؛ ذلك العام الذي فررتم فيه من هذه الأرض بذلٍّ وهوان.
واليوم أيضًا، إذا أصررتم على العدوان والاحتلال، فستُطردون منها بالذل والهزيمة</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79550" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6731b513eb.mp4?token=KQ0e4A0-CBiur_0CDra7RIpBZeT69tCpXv15d5TOxRd8lnehq3MHN8vwqaRf3UlwGKhrvmulbv43OpAi6m4yvRTKI7MCRJXaSFi_bg7j5YWYIXujrws82K5RhZOXt0uGxdlT6p9ZhBmXmcqrReP7ryrJb0DYutoY7xidVcjLC0dTxFKFJg5v5aYpYOTPTxdZnZvt9WAUGBOgCkpY5qCoXe9K7kTmc4wRfI40Lw8sV4zoH0EN1jnGobVdDu7mO4m3g2YHpKjSm2Qr6ITbToFtGDs39R4qkBdcmZr9sDusGp_woM8veND6fv3NJCshZnZ1BWJ9hInRl8x_O0wDsayR-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6731b513eb.mp4?token=KQ0e4A0-CBiur_0CDra7RIpBZeT69tCpXv15d5TOxRd8lnehq3MHN8vwqaRf3UlwGKhrvmulbv43OpAi6m4yvRTKI7MCRJXaSFi_bg7j5YWYIXujrws82K5RhZOXt0uGxdlT6p9ZhBmXmcqrReP7ryrJb0DYutoY7xidVcjLC0dTxFKFJg5v5aYpYOTPTxdZnZvt9WAUGBOgCkpY5qCoXe9K7kTmc4wRfI40Lw8sV4zoH0EN1jnGobVdDu7mO4m3g2YHpKjSm2Qr6ITbToFtGDs39R4qkBdcmZr9sDusGp_woM8veND6fv3NJCshZnZ1BWJ9hInRl8x_O0wDsayR-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اللحظات الاولى للانفجار الحاصل في محطة الغاز بالدوحة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79549" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79547">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLitAVyuMuVOYdLDVQy8_vl0BKttkZ8uYy7b7441KLIvmWANqa37-YUAmouDZ9eZ23PvyhG9Ak2w9x8OlCKzpxTv_cSr84JB6GWQa4vkRooTtw4oI1Ql_5g9lDYiZ0bIYWCevGoHXRAEh8Vi-ZQb7vCrxRGPbzYZ5IYmDDJCjqkm_N_ifZlxkdtuiWnxFn61PqDbLxgxgOo0y6EkaQhDncl4YcmYvTy3v7QbUMmnz-66Xykt_XOsDlHrVbT6zAnKGuIcelRWHxUhsr6-aDOMuGFlt6oTtE8mdbm9fMVemll5oAkyARO_aDsOy_-mX_U-PXLpajZci0JEZAZ2rGGXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBdyRskH7EZu20eXsuPtMwOzfKwEsQW0daK82KWKVt_mqiUazL1FKZrCHTEVIdlwQuNU3MhuGoyZa2jfrjCZNe2yyPuS1XeN6dbIJtYpHLzmvOUkTyVYFvOJtiz_1j9L70qpXXtAHlRjPBEBwtfsR8BEX2iIukcKkDAwCJcrFaNH9jcelJ89MAuDPJP8R9odqdHcyaK0Fffa1lNVKDEJIJs3jPu6GaUKEINwdsFqtgAn6A5EuHAz43GMD_fQMhE0cKYBY558S-hkMETmk-jxqkNpV72pCCE3oToaxFVZ8R-H3oK-Md2NZD6Vh4FODhOruTIKiMsCiZL7P9FA_vWrZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
انفجار قوي مجهول في احد المصانع بمنطقة رأس لفان الصناعية بالدوحة القطرية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79547" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
انفجار مدوي في العاصمة القطرية الدوحة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79546" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79545">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBuJAzd1_7VxVVde5kowfJwNKzWFfgptTSjZBVKq__bFmQ5E1CcirwkUkSseE1aFeXb2DpzHFkllpivuK4CfY8iWR8WmXc8piFS_3xq9WAPYzOa6nMDbu6laMbQh0-CCNFFi2SMhnuCjIU_Y6PBt77k_AKvRlUFf65eK8igue8KidCqLqvmdizJDI3vqN4Tqcerzekawsi1SNwZb_PUHrYF9s4xYgXo17pWNmVBWZ72sPbcJtOVn_qnEDPhPbGBdNvoSYpnZ8-sysbHir5w03Qc1khsStluwFqJKGThLelkHUAO3-peW-40rNiRbYH_CDSHNjlF5wxtY2PXImdcYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
انفجار مدوي في العاصمة القطرية الدوحة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79545" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79544">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🌟
انفجار مدوي في العاصمة القطرية الدوحة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79544" target="_blank">📅 23:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79543">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuHVCQZ3tRt4YtYDBOpkVdnC8-QhxynlDVWAnzMETrHF7g2CspD39ZIA3KxQEabSiKVlEsXuCVFhnMbrzcy9eb80lpx4KulRkkz-Gd2CZHaB6qco5bph2hrfnSbSgMWoIv-v_bk2VHaypc8Hc-QoM-ikYnzb9mcJdzNoeBcbhF0kkHIAk7PZ5yleY1LCluTs0NRTCkpep2XeS-FzNeOQAoB9EsWTkpRfBOTE0Kd6ef4w-0k2DH2_vH1YARPEeZsjtReBBAEoWgCaV2T3rAQ3CVbVSSlQhwBm8lWDAxZW4qrVMwuW4s_hBF6bjl2MgbtlF-9Q9VG3iV79EqiU3LHo3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:
بعد إنفاق تريليونات الدولارات على حلف شمال الأطلسي، لن تفكر إيطاليا ورئيس وزرائها حتى في المشاركة في جمهورية إيران الإسلامية وتهديدها النووي الخطير للغاية.
على مدى عقود، ندافع عنهم، ولكن عندما يتم اختبارهم، فإنهم ليسوا هناك للدفاع عنا، وبقية العالم. ليس جيدا!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79543" target="_blank">📅 23:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79542">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466ae28e94.mp4?token=lTd_n94f-X_O99V9T9-Y8S1L07MlVFKvAx7n9lFT4RNdWmB5zOWIqbAhigaz2tuk5JnwT_emqW5XPEgHjMCZCMBXNTiFPgyujzAxE6Dm9NJY7LvOcVCWbSAhU8P93AdSq016_rFEu21RBvnJISPSzScQMaPBLZmgNTa9OZm3cdbi6x4jdKeLOuPSUMcaFLbUN6w9_pP8rsmh-lBYqW9RFuyTSyKNj-2-s1o66zaJFIgqb4fd-p3WQ0Ko0QRK39fSVSWWKlKVhDJzXfsW1w0yiJTI-rUSHvbewpxvEpl69qINLjxZBbjo4_hVvOhk4WAfdSy-eiwDl2RpYLwMDOB0XUGmdMy9Rl64xp7OLtbQG6ssQhbVVMWiJMbk0hEgMu6WVjXCU4fq227brNspOB24-p5gBHorg1-nkOVeOUTQcUFI-n2a1zyiBvTS9hTTmEPbRA2XDoBUWEZuuz-ugjrvNq789RsYkBNqR0EofkNgyrud3pSO59XC0jL98cRgPkSsu0jJvaQFo1tM1TYZ804Rkg0cNuf57t5NuR-UXswXmeBaiM0YSVBtAvjhXCrIwlzlp5Nqjcf9ipowP4oIJZN1TQ5NyLUGgDibyhWcerJWtWey83JyQzZb80DAMbEHLqQn_P6af8ILV-p4pc11jnkc9S9LuPegyDExyz6kXnY1c48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466ae28e94.mp4?token=lTd_n94f-X_O99V9T9-Y8S1L07MlVFKvAx7n9lFT4RNdWmB5zOWIqbAhigaz2tuk5JnwT_emqW5XPEgHjMCZCMBXNTiFPgyujzAxE6Dm9NJY7LvOcVCWbSAhU8P93AdSq016_rFEu21RBvnJISPSzScQMaPBLZmgNTa9OZm3cdbi6x4jdKeLOuPSUMcaFLbUN6w9_pP8rsmh-lBYqW9RFuyTSyKNj-2-s1o66zaJFIgqb4fd-p3WQ0Ko0QRK39fSVSWWKlKVhDJzXfsW1w0yiJTI-rUSHvbewpxvEpl69qINLjxZBbjo4_hVvOhk4WAfdSy-eiwDl2RpYLwMDOB0XUGmdMy9Rl64xp7OLtbQG6ssQhbVVMWiJMbk0hEgMu6WVjXCU4fq227brNspOB24-p5gBHorg1-nkOVeOUTQcUFI-n2a1zyiBvTS9hTTmEPbRA2XDoBUWEZuuz-ugjrvNq789RsYkBNqR0EofkNgyrud3pSO59XC0jL98cRgPkSsu0jJvaQFo1tM1TYZ804Rkg0cNuf57t5NuR-UXswXmeBaiM0YSVBtAvjhXCrIwlzlp5Nqjcf9ipowP4oIJZN1TQ5NyLUGgDibyhWcerJWtWey83JyQzZb80DAMbEHLqQn_P6af8ILV-p4pc11jnkc9S9LuPegyDExyz6kXnY1c48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏وزير الأمن القومي الإسرائيلي بن غفير
:
إذا طلب ترامب من نتنياهو مغادرة لبنان، فيجب أن يكون الجواب: "سيدي الرئيس، لا".
‏وليس فقط رفض مغادرة لبنان، بل أيضاً رفض عبارات مثل "لا تضربوا هذا المكان" أو "لا تضربوا ذاك المكان".</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79542" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79541">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">من أرض الولايات المتحدة، خيبر شكن يهز شباك بلجيكا معلناً الهدف الأول لإيران</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79541" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79540">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">من أرض الولايات المتحدة، خيبر شكن يهز شباك بلجيكا معلناً الهدف الأول لإيران</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79540" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79539">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79539" target="_blank">📅 22:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd0d08c52c.mp4?token=cA0pHdX0Uzc2bGGwaTLUzMPzcm8eYUr95hpxAoLQ4vX5izy5Ljm871cqz-DmNcluuEYHrYuVyebb8WKjehsD9RbdjyNgk8jBlsiyKklE5qH3xPWAJVQ0j8HTBIePEs9ADT7KwJ3VRgKmSa32DXw46nHJmY7PNnEXHm_Z29HAx4MM92Dnsfjlt4glMrC2MbH1U1des-T_-DObIJuUk3V9gCd6eCjn7FibGXV2Tav6cfnW6zG0tncFqUAM16mnDJMD0mqgoq9ZX5euO3ff3y3BonxFUAFv1A_BOcdAuCkZ6NiCHFubM9GES_PJWGUvD4z8giCUpMPbnvpI6r82lX5RUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd0d08c52c.mp4?token=cA0pHdX0Uzc2bGGwaTLUzMPzcm8eYUr95hpxAoLQ4vX5izy5Ljm871cqz-DmNcluuEYHrYuVyebb8WKjehsD9RbdjyNgk8jBlsiyKklE5qH3xPWAJVQ0j8HTBIePEs9ADT7KwJ3VRgKmSa32DXw46nHJmY7PNnEXHm_Z29HAx4MM92Dnsfjlt4glMrC2MbH1U1des-T_-DObIJuUk3V9gCd6eCjn7FibGXV2Tav6cfnW6zG0tncFqUAM16mnDJMD0mqgoq9ZX5euO3ff3y3BonxFUAFv1A_BOcdAuCkZ6NiCHFubM9GES_PJWGUvD4z8giCUpMPbnvpI6r82lX5RUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من أرض الولايات المتحدة، خيبر شكن يهز شباك بلجيكا معلناً الهدف الأول لإيران</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79538" target="_blank">📅 22:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fe95c6bf.mp4?token=UfnUVNl_kOXOkfa1s-jZdLogbWXtk21yhKWdxFM3fOwcrtOlyutSH0D7bB6N282qdNqRUK-GtrmGj8rcohOSEw8DmOkY4LHyV81iG5_O3YLjNG0LdnxWmuvn66oR1kWf8Tk_B5ExWoNYokpvR0t4i1ri6_Pmkvs-1G4VpeetqPKnKpTt7QCItRhDODq0-r2JQWvg9Z3J9N85UObtzfnfr5jdgjRaf2-HQZfhWOeIICduBK1_tA-Adhi5wY7bReJVaUpyVgWjkOdNGf9C8DjoT363Hjxbl2joEZtLEE4qoBH8DT7RzDwNeOvAmgJJLm9AT4lsWZjRjgecNWYXVL2a4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fe95c6bf.mp4?token=UfnUVNl_kOXOkfa1s-jZdLogbWXtk21yhKWdxFM3fOwcrtOlyutSH0D7bB6N282qdNqRUK-GtrmGj8rcohOSEw8DmOkY4LHyV81iG5_O3YLjNG0LdnxWmuvn66oR1kWf8Tk_B5ExWoNYokpvR0t4i1ri6_Pmkvs-1G4VpeetqPKnKpTt7QCItRhDODq0-r2JQWvg9Z3J9N85UObtzfnfr5jdgjRaf2-HQZfhWOeIICduBK1_tA-Adhi5wY7bReJVaUpyVgWjkOdNGf9C8DjoT363Hjxbl2joEZtLEE4qoBH8DT7RzDwNeOvAmgJJLm9AT4lsWZjRjgecNWYXVL2a4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترفيهي من جديد  الجولاني للشيعة في لبنان: هذا المكون أحوج ما يكون بحالة إنقاذ في لبنان وليعلم الله اني حريص على هذا المكون والحزب لا يمثل الشيعة</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/79537" target="_blank">📅 22:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e886f49876.mp4?token=fAtMQHkLZ5yzCgEBMcsyncNAs7oGJaivVaz824mzKU5_7bnxOq6nxILwt5emIF9Ci6cCG0Yz7S_U3o52g7pQ3gw4xqM6KHphAeui1G_GmqiFqYSZz3AVRCA7fQT7G686Bu5VNADDJLjaNw9EFBMvNqMkfJRzykhTiWoIgYTrG66P9X0XIbyifzK8e63l5wrfaer3je39XaP2v_wK5Q1_4MLSmo_wwNmqfgokSkyWosJmLTEsO_JlQssAncNcAfHwluYn-LFChvae5UDmFwS2qQK8WFeB9N0IuJN_b_RGEUWdAeKJCRND54jSPsd1IQ8NQAp9YyLR864_F77Vm6nYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e886f49876.mp4?token=fAtMQHkLZ5yzCgEBMcsyncNAs7oGJaivVaz824mzKU5_7bnxOq6nxILwt5emIF9Ci6cCG0Yz7S_U3o52g7pQ3gw4xqM6KHphAeui1G_GmqiFqYSZz3AVRCA7fQT7G686Bu5VNADDJLjaNw9EFBMvNqMkfJRzykhTiWoIgYTrG66P9X0XIbyifzK8e63l5wrfaer3je39XaP2v_wK5Q1_4MLSmo_wwNmqfgokSkyWosJmLTEsO_JlQssAncNcAfHwluYn-LFChvae5UDmFwS2qQK8WFeB9N0IuJN_b_RGEUWdAeKJCRND54jSPsd1IQ8NQAp9YyLR864_F77Vm6nYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
من ملعب لوس أنجلوس بُثّ شعار الفيفا باللغة الفارسية،قبيل انطلاق مباراة المنتخب الايراني مع نظيره البلجيكي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79536" target="_blank">📅 22:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الحرب الإيرانية_ الأمريكية فيها عبث وليس فيها أهداف ؛ ليست من مصلحة إيران وامريكا استمرار الحرب وإسرائيل جزء من امريكا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79535" target="_blank">📅 22:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e1bfb39.mp4?token=eAuI2JhdF10_dKqzQ3kMs-89yR7mbR-ulg7AlcrAUfPqyouEdKbkpI5yot2tFhLEUgQhrfz8WT5SBxOkktEbvxa7wAPoiHRrRAD_D0rBAitvkOxk51Ax-EDSQB_QY8yadLLguA8vrFW-dQvOOm2jJfYCgB5yJSgoQ8us3uxv7XvT76emXkJ2BM7KQSU7g_iiomK3raGrw9ttTzS7KKQlQMBQorUCLoV3dGAbxf_ww9NVTsfMOTh-CLshrwVdxO-BuxQkSiiiOZgFjpvQrWzkFsoemfN4skfOmR3RdCy1ncwZsROO1J8H_Gt_Jpq1K96kDgmTTmVSEXI7afU6ec0zeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e1bfb39.mp4?token=eAuI2JhdF10_dKqzQ3kMs-89yR7mbR-ulg7AlcrAUfPqyouEdKbkpI5yot2tFhLEUgQhrfz8WT5SBxOkktEbvxa7wAPoiHRrRAD_D0rBAitvkOxk51Ax-EDSQB_QY8yadLLguA8vrFW-dQvOOm2jJfYCgB5yJSgoQ8us3uxv7XvT76emXkJ2BM7KQSU7g_iiomK3raGrw9ttTzS7KKQlQMBQorUCLoV3dGAbxf_ww9NVTsfMOTh-CLshrwVdxO-BuxQkSiiiOZgFjpvQrWzkFsoemfN4skfOmR3RdCy1ncwZsROO1J8H_Gt_Jpq1K96kDgmTTmVSEXI7afU6ec0zeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: حزب الله متعدي على الدولة اللبنانية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79534" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5468982523.mp4?token=RJ8b2F7WG14lDsjpxyQLUIh2b--km0YMmuQTrVHDKzX8eb_QzPnL_PUj2kNA6SYceRH8TTVq4Nn3T9FmKhpskkT9g8Zyux2OhTo3rYfLkqumVMupi411yjDLAmVwDFpAfL0qck29UugRdfT2j1jgcbxa_vMvbKv4oD2IJRnktmEPsezDHSCc6DaPzYLYCW1-mv5rC0qFdKCvMFXyvV10uiTwwbCf12m3EtSmaUh3XPCVj9mmq_0CQwOXDnwvTfIh0k-XDZW7PizlN-WwA1OQXduVjEobhtgsCbkQAiUlZAy2Ex82vOeT1spEVOceJOZm3DR3uod2_4lnSozLPC2jwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5468982523.mp4?token=RJ8b2F7WG14lDsjpxyQLUIh2b--km0YMmuQTrVHDKzX8eb_QzPnL_PUj2kNA6SYceRH8TTVq4Nn3T9FmKhpskkT9g8Zyux2OhTo3rYfLkqumVMupi411yjDLAmVwDFpAfL0qck29UugRdfT2j1jgcbxa_vMvbKv4oD2IJRnktmEPsezDHSCc6DaPzYLYCW1-mv5rC0qFdKCvMFXyvV10uiTwwbCf12m3EtSmaUh3XPCVj9mmq_0CQwOXDnwvTfIh0k-XDZW7PizlN-WwA1OQXduVjEobhtgsCbkQAiUlZAy2Ex82vOeT1spEVOceJOZm3DR3uod2_4lnSozLPC2jwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترفيهي من جديد  الجولاني للشيعة في لبنان: هذا المكون أحوج ما يكون بحالة إنقاذ في لبنان وليعلم الله اني حريص على هذا المكون والحزب لا يمثل الشيعة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79533" target="_blank">📅 22:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79532">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
مدرب المنتخب العراقي أرنولد:
مستعدون لمواجهة فرنسا ولدينا قناعة بقدرتنا على تحقيق الفوز.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79532" target="_blank">📅 22:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79531">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ced46cbc.mp4?token=m_EY0AAnDEWPqT5R5_JwiOm4Kb0LayT__w63ZiyNS6ToVVjP05Pfdh8Rz3c8QB4tMWsEPCFUZECzrEco1PcjYkY1RBXmuBxjlnxKcwPxu9quJauRTlMBUWY8bLbhHmOkpn6PoH2s0Ubu-BgIxoI6ieBGfwDsFKWOC3EoJurk2WQ4hzmd8_oUnZrrmhjv6Waa4AlwRKuv-XNGvfQN_vA9a1Yq80QL9pXY0OawoH3xIllowutXd3v16lkSGP19ouMrK3KRBBg5tbdwv68RznpqVshmEBr2b6H-gAcJjmsII0PWjpw0q07BvAVWVEJk4nPkVjxstsMcLq05tuE65A4WnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ced46cbc.mp4?token=m_EY0AAnDEWPqT5R5_JwiOm4Kb0LayT__w63ZiyNS6ToVVjP05Pfdh8Rz3c8QB4tMWsEPCFUZECzrEco1PcjYkY1RBXmuBxjlnxKcwPxu9quJauRTlMBUWY8bLbhHmOkpn6PoH2s0Ubu-BgIxoI6ieBGfwDsFKWOC3EoJurk2WQ4hzmd8_oUnZrrmhjv6Waa4AlwRKuv-XNGvfQN_vA9a1Yq80QL9pXY0OawoH3xIllowutXd3v16lkSGP19ouMrK3KRBBg5tbdwv68RznpqVshmEBr2b6H-gAcJjmsII0PWjpw0q07BvAVWVEJk4nPkVjxstsMcLq05tuE65A4WnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجولاني: على الرغم من جرحنا من حزب الله مستعدون للجلوس مع حزب الله على نفس الطاولة والحوار معه</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79531" target="_blank">📅 22:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79530">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a08c992c.mp4?token=VMjX9EyepxrCLTmFgBKrwgZLAO4JMWi00dgrXK9avxsiWoq461oTk9SVSIlvwj1C_cMfhigRL5v3FBd5z36fkc354GeLDrf07e-nrMjExJCa6fDBc6WnEWh3UJ1izU7t0TXgtBczvWNtAM_FneWoFPO1ElP4WHwRYTJWMcWXmygfgou_D6CW3V2RcfgMvfK6doF8ahBZ3rUD2yKFVc3hptGxZieoVgBpkI9VOFgH4PWeRWJkYLffZUwpT5hhVBymfrYKwJFhYUFhIiWsAMqYrnvY6VfRVwF4PKRLvwUDAn0fFdNWlKY8rKhj1iZzbtxLWMa5O5I59x6um_s_dgIiaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a08c992c.mp4?token=VMjX9EyepxrCLTmFgBKrwgZLAO4JMWi00dgrXK9avxsiWoq461oTk9SVSIlvwj1C_cMfhigRL5v3FBd5z36fkc354GeLDrf07e-nrMjExJCa6fDBc6WnEWh3UJ1izU7t0TXgtBczvWNtAM_FneWoFPO1ElP4WHwRYTJWMcWXmygfgou_D6CW3V2RcfgMvfK6doF8ahBZ3rUD2yKFVc3hptGxZieoVgBpkI9VOFgH4PWeRWJkYLffZUwpT5hhVBymfrYKwJFhYUFhIiWsAMqYrnvY6VfRVwF4PKRLvwUDAn0fFdNWlKY8rKhj1iZzbtxLWMa5O5I59x6um_s_dgIiaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي_آخر
🇸🇾
الجولاني يمد ايديه إلى لبنان لمنع الحرب الأهلية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79530" target="_blank">📅 22:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a9f04017.mp4?token=LwIuC9RT27Yq5zbqMIPVHOC08dtO_g6YTo9VGk8BcQyPlr7ELIG9y2fk1UAOFErOMw-Ax1-dE51nXt64gN0yGC-9ITQwAdFcaw5Ms8lHPnwLfP1vXMeOMSFplfiL23yAwjFXF60_UHIhe4QxVjfiM-TCddqoAkz86ljHHr6rJ2j2piFgNeA00A4tVcyaiTjBlyfpT1Y87LNLvN1qCp6Q108Bk6O331_lZZVmHUpP_UHsN_9EEcNjbZ-eQ5EgROwS0AiKhEdRiSBVqhnH9QvD6mRT31Masu2u1mRxGS4HXNJCzJZcOwfU_TUR4VA4s4V1W5jJiujhv0QgLSiRm_y3QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a9f04017.mp4?token=LwIuC9RT27Yq5zbqMIPVHOC08dtO_g6YTo9VGk8BcQyPlr7ELIG9y2fk1UAOFErOMw-Ax1-dE51nXt64gN0yGC-9ITQwAdFcaw5Ms8lHPnwLfP1vXMeOMSFplfiL23yAwjFXF60_UHIhe4QxVjfiM-TCddqoAkz86ljHHr6rJ2j2piFgNeA00A4tVcyaiTjBlyfpT1Y87LNLvN1qCp6Q108Bk6O331_lZZVmHUpP_UHsN_9EEcNjbZ-eQ5EgROwS0AiKhEdRiSBVqhnH9QvD6mRT31Masu2u1mRxGS4HXNJCzJZcOwfU_TUR4VA4s4V1W5jJiujhv0QgLSiRm_y3QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي_جداً  المكون الشيعي يجب أن يطمئن في لبنان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79529" target="_blank">📅 21:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
نتنياهو: حققنا إنجازات عظيمة ولن نتخلى عنها. سنبقى في منطقة الأمن في جنوب لبنان طالما دعت الحاجة. وبالنسبة لإيران، مهما كانت التطورات السياسية، لن أسمح لإيران بالتسلح بأسلحة نووية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79528" target="_blank">📅 21:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287dedba32.mp4?token=E1sj_8XInFz15vaaaQ5jUcAOyJWGohjbHen5YvYqvGo30mpiRWsCahLX_u7bvNEST_S4MF0WSE82SbhWthWyl-myP1F9FJ3RNZM14BO85y3GopugIDFIlciWjDxq_Eq3gh23DoNA9-gKdnWZ0ehqu9KiRBsf-brIRxl67Zt31rGGg9R-269YU7DDS2a57m8KP6NucmdUz_-JrMj_7UbsyWyOwo0d5MrytDAHzyKlo9cbTKxfHNTMkCjqzQfXWp0xAPukswL0kMoiEWg0AtgTFHXZ4Ne5eAJnK5O12BMxXiCDd-RsEXXI66RmafH_5e3UR0FcVH9KA3yCYD-wWp5oDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287dedba32.mp4?token=E1sj_8XInFz15vaaaQ5jUcAOyJWGohjbHen5YvYqvGo30mpiRWsCahLX_u7bvNEST_S4MF0WSE82SbhWthWyl-myP1F9FJ3RNZM14BO85y3GopugIDFIlciWjDxq_Eq3gh23DoNA9-gKdnWZ0ehqu9KiRBsf-brIRxl67Zt31rGGg9R-269YU7DDS2a57m8KP6NucmdUz_-JrMj_7UbsyWyOwo0d5MrytDAHzyKlo9cbTKxfHNTMkCjqzQfXWp0xAPukswL0kMoiEWg0AtgTFHXZ4Ne5eAJnK5O12BMxXiCDd-RsEXXI66RmafH_5e3UR0FcVH9KA3yCYD-wWp5oDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجولاني يوضح السبب: حزب الله ينتشر على الحدود السورية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79527" target="_blank">📅 21:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79526">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef06d5c084.mp4?token=svmkWYJR8eyelCurQU5KL1qNfugghehcHPDYTr9GHPR4K9Mm6kCsT34QRyeph-9zCycD1CrZDeFp9l3lsC9CopQu8fGt5KvOOxcES03FHx9E_VqFIE-Ohw6bhYpwuH8kM_h4BZSahCg4hmDcPWo1WWW3uvnwdoA7nxlNojRIt2JldzTfU_HjSp3u85w6pyv2y3-Kkf4-i4MxaLnbszw9YxTzPoA4-sGiGBVTgVNzidalBT2irKxaYlg7MWPDdVEE-xwy9IWtVAFP1atMuqJEWzq8u9mJSDwGmpTKVZiS12jExaVd1__DFz3WolDOFz6Ai9Dh3h5XT7byJ3l86ad4jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef06d5c084.mp4?token=svmkWYJR8eyelCurQU5KL1qNfugghehcHPDYTr9GHPR4K9Mm6kCsT34QRyeph-9zCycD1CrZDeFp9l3lsC9CopQu8fGt5KvOOxcES03FHx9E_VqFIE-Ohw6bhYpwuH8kM_h4BZSahCg4hmDcPWo1WWW3uvnwdoA7nxlNojRIt2JldzTfU_HjSp3u85w6pyv2y3-Kkf4-i4MxaLnbszw9YxTzPoA4-sGiGBVTgVNzidalBT2irKxaYlg7MWPDdVEE-xwy9IWtVAFP1atMuqJEWzq8u9mJSDwGmpTKVZiS12jExaVd1__DFz3WolDOFz6Ai9Dh3h5XT7byJ3l86ad4jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: لن تروا سوريا في لبنان.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79526" target="_blank">📅 21:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=B2h0cwnv85t6fcfbC9DLHUHG-ETd0b04_5bwQLdJcgkZZDlZtzsCXk8OsAUOskQW4JLZpW6Swk3Wu2lbW20b5WI2-NaaEHhg8WiUaoTZFQDsRvtg3j-Lwmpv89gSeblxma1i0vCRpM-5ccV4NMSmU2MykxmHpaUwx68iTQ23h596o_9fFWliataWPXJs8TrxR5wJZtwdH2PdGkBIKChGRdk1yP8oy-jz3wb5cBTNxMXsRxByDJd-1Regsp2kDoe_ZBVyCM78ko2hxQpuCD3Qfd1KX3JeFS3erFVbKsFY6-zDxrZwXe1YTaxsY7rqWK2E959BKE_79V1i85fXD_ItjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=B2h0cwnv85t6fcfbC9DLHUHG-ETd0b04_5bwQLdJcgkZZDlZtzsCXk8OsAUOskQW4JLZpW6Swk3Wu2lbW20b5WI2-NaaEHhg8WiUaoTZFQDsRvtg3j-Lwmpv89gSeblxma1i0vCRpM-5ccV4NMSmU2MykxmHpaUwx68iTQ23h596o_9fFWliataWPXJs8TrxR5wJZtwdH2PdGkBIKChGRdk1yP8oy-jz3wb5cBTNxMXsRxByDJd-1Regsp2kDoe_ZBVyCM78ko2hxQpuCD3Qfd1KX3JeFS3erFVbKsFY6-zDxrZwXe1YTaxsY7rqWK2E959BKE_79V1i85fXD_ItjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: لن تروا سوريا في لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79525" target="_blank">📅 21:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: إسرائيل أبلغت أميركا بإمكانية الانسحاب من مرتفعات شقيف جنوبي لبنان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79524" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10cb16136.mp4?token=N5pbxPqzEh4SowiztDb2wYxZHNeTGZ1UeO0qsIasKhfWud7bBrt8GcFEInjHWQoY7BjNJwPFz6TL0GcvH2ERhJuE7dC33MbvtfCyk3F6n9X3wgnZpBYzysMFQ6P2jQOUpRHmKxG_rBDPo3IJRkM4diOdnn4PS0VpSzNE71RxBiBKzxwckeSWqfTMx74x4R607ACJl3bMPj9N69C-crTKdAU19ZylVB7cQfU87oH3tQyS4fJaRX1673rQL3YGZZknKMdtgYWLKU3YxhZ0QPCKBbuH9yRXk9tMKdy0ZGOnE3sZE8LXLN4nPDb5UlsvuCqFAw5tcGM9AUq6zqN9dgWWbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10cb16136.mp4?token=N5pbxPqzEh4SowiztDb2wYxZHNeTGZ1UeO0qsIasKhfWud7bBrt8GcFEInjHWQoY7BjNJwPFz6TL0GcvH2ERhJuE7dC33MbvtfCyk3F6n9X3wgnZpBYzysMFQ6P2jQOUpRHmKxG_rBDPo3IJRkM4diOdnn4PS0VpSzNE71RxBiBKzxwckeSWqfTMx74x4R607ACJl3bMPj9N69C-crTKdAU19ZylVB7cQfU87oH3tQyS4fJaRX1673rQL3YGZZknKMdtgYWLKU3YxhZ0QPCKBbuH9yRXk9tMKdy0ZGOnE3sZE8LXLN4nPDb5UlsvuCqFAw5tcGM9AUq6zqN9dgWWbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: لن تروا سوريا في لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79523" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇸🇾
الجولاني: لن تروا سوريا في لبنان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79522" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭐️
أكسيوس: الوفد الإيراني لم يغادر والمحادثات لا تزال مستمرة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79521" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79520">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aaa354e4a.mp4?token=UaW6hxQZ3vAD80F3NEs9wDJWsB8o_-8OX2eHGMCAtqQPxOMKBuflJK36kz5nkZkrhrzWLre6lCqvyTvp-8a08h6Bm1YlpX9kalAOR4Col26nC3Vf6lC0TDbCzMM4gG60RmnwRYY8Hc7Z0FJVchNYIRXtRz4xjujS0vmct3BTZDIK49SWQAohoZ0gThfsevYdIYc4Qpqnfpt2USQQ5u4475fTal0EkgAYJBTc348nCMBPF9DjUhkfnwrRHNR25lb0L1JNtvu9tHLkqkoe29Qu2OzKI2ybQPif20qDS3mBAoRB3LdFeKHyyKgdrBdUbHb2lDTNcUeW0X38R3-14UuvbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aaa354e4a.mp4?token=UaW6hxQZ3vAD80F3NEs9wDJWsB8o_-8OX2eHGMCAtqQPxOMKBuflJK36kz5nkZkrhrzWLre6lCqvyTvp-8a08h6Bm1YlpX9kalAOR4Col26nC3Vf6lC0TDbCzMM4gG60RmnwRYY8Hc7Z0FJVchNYIRXtRz4xjujS0vmct3BTZDIK49SWQAohoZ0gThfsevYdIYc4Qpqnfpt2USQQ5u4475fTal0EkgAYJBTc348nCMBPF9DjUhkfnwrRHNR25lb0L1JNtvu9tHLkqkoe29Qu2OzKI2ybQPif20qDS3mBAoRB3LdFeKHyyKgdrBdUbHb2lDTNcUeW0X38R3-14UuvbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
دوي إنفجار مجهول وإرتفاع أعمدة الدخان في محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79520" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
رئيس الشاباك السابق رونين بار وزوجته شاركا في مؤتمر أمني في الإمارات بمشاركة كبار المسؤولين من العالم. خلال الزيارة تم تلقي تحذير أمني غير عادي، وبناءً عليه تقرر إجلاء الزوجين فورًا من الدولة إلى إسرائيل.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79519" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
إسرائيل
أبلغت أميركا بإمكانية الانسحاب من مرتفعات شقيف جنوبي لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79518" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الإيرانية:  إن الجمهورية الإسلامية الإيرانية عازمة على متابعة تنفيذ التزامات الطرف الآخر بدقة وجدية. يُعقد اجتماع اليوم في سويسرا لمتابعة تنفيذ بنود مذكرة التفاهم بشأن إنهاء الحرب. ووفقًا للمادة 13 من مذكرة التفاهم، فإن بدء المفاوضات…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79517" target="_blank">📅 20:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
عضو في فريق التفاوض الإيراني:  تم الانتهاء من مسودة الإعفاء المؤقت من العقوبات المفروضة على النفط الإيراني.  كانت قضية لبنان محورَ مفاوضات اليوم، وحظيت باهتمامٍ أكبر من أي قضية أخرى في الاجتماعات الثنائية والمتعددة الأطراف والرئيسية.  لن تدخل بنود مذكرة…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79516" target="_blank">📅 20:32 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
