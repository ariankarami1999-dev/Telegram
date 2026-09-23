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
<img src="https://cdn4.telesco.pe/file/lsya6yL8n8co6Az2uGlWP48M9GVxSIr7rgeAB56H-qdUfWeRAsYOjZirgNEwULNqc731Lb0goyscV-_zBxx5IKqXYxIUluEqbum08o_9ZlKnpMxiFxuA_3Mh0lPe3YnwajZedLteIGVVV-pLxYnVIPWQd1PRHsNCw2zSS4tH9WHflKztVKLDbwIkEjTWDga7nwEIGzvx0vM8_Gj4tdNn0Hazrx7AFeAQPHItnxui_SmIBq8LltxFJZAFvHpNXEx8_BmdiM7sXhuXAcPeJC9X8Px3i2RZLG66I3pug5nM9XfIqpGVg4sapqnM7CgzmYzHmnkBgLc-oeCHjnuIH7RyMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-91329">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
‏طائرة تابعة لـ"إيران إير" تهبط في اسطنبول رغم سريان الحظر الأميركي.</div>
<div class="tg-footer">👁️ 630 · <a href="https://t.me/naya_foriraq/91329" target="_blank">📅 13:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91328">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggbYH0s-pBslmJXdRF_8RHkEZis8IoBFMYQYiOutQiR5-a7yekrt8pNCslaGj3iB-ejrkWkewsgZvLZriLeU1cJg2wVdjW2nrufKSk46FDA6KaGWFsJXTVxwXtmC4DpidnVhQsmdVt8NrCWw8Q4sijw3DfeH4UXMVZOzbOthGrEqhoYpRGhIgP-PIUGmefhjB7XMR4aJL53jUSZhKOcgTgI3kcdmQHNPGCyLkhJwd3SYqlymImCu9OQiXzTtPMrD40z_cYKPVckAnFNbJzG9zaYida5yaIFMx4SQZFOyZoqiqeU_mWiIQTWlMiS4-F83RVPib1HUXjINW4qbzIavow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء العراقي:
السجن 7 سنوات بحق النائبة عالية نصيف بعد ادانتها بتهم فساد</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/naya_foriraq/91328" target="_blank">📅 13:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
اكسيوس:
ما يسمى بلجنة السلام تكشف عن خطة إعادة إعمار غزة بقيمة 2.45 مليار دولار وسيتم عرضها على الاعضاء يوم الاربعاء
علما ان غزة تحتاج مئات مليارات الدولارات لاعادة الاعمار ان لم تكن تحتاج اكثر من تريليون دولار!</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/naya_foriraq/91327" target="_blank">📅 12:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91326">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
🇸🇦
عدوان سعودي يستهدف محافظة الحديدة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/91326" target="_blank">📅 12:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91325">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
🇮🇷
🇨🇳
الاعلام الاوربي:
هبوط طائرة تجارية إيرانية في الصين رغم العقوبات الأميركية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/91325" target="_blank">📅 12:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91324">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇷🇺
جهاز الأمن الفيدرالي الروسي (FSB) :
تم اعتقال أحد سكان موسكو بتهمة التخطيط لتفجير سيارة في موكب مسؤول روسي رفيع المستوى.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/91324" target="_blank">📅 12:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c2099f8c.mp4?token=tgJSlatgbza-RDaeTEYotp02oBfxidumVhq5_9KZO6d5mgSN_z-JbuGhBw2ZVHwM8eqsXqH78nj-w9eWEBpk2Oh3UKIxAyJXXW8j0csgTYyghw8V_YnDMUlO4sjbjKCeFxKP_3eBjdlsU4nIlzFjZtM9rjzDlAR6TzzvyaIMH3UTdVRwGkEWQFUoKowfZHf0TAgnEzuzNAfDOuI322sxZQH7mlqsKOwXzx8AuYgfnHY0FeEuKdhOvFJTBEJMyZx62ddWS8Kanl_OSB83WlFMI_rfTdLesi4N-B5mzGR7itpbo176CSLBzcsyyZa74VrzbeWh5w16e5SC7jQQbzl1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c2099f8c.mp4?token=tgJSlatgbza-RDaeTEYotp02oBfxidumVhq5_9KZO6d5mgSN_z-JbuGhBw2ZVHwM8eqsXqH78nj-w9eWEBpk2Oh3UKIxAyJXXW8j0csgTYyghw8V_YnDMUlO4sjbjKCeFxKP_3eBjdlsU4nIlzFjZtM9rjzDlAR6TzzvyaIMH3UTdVRwGkEWQFUoKowfZHf0TAgnEzuzNAfDOuI322sxZQH7mlqsKOwXzx8AuYgfnHY0FeEuKdhOvFJTBEJMyZx62ddWS8Kanl_OSB83WlFMI_rfTdLesi4N-B5mzGR7itpbo176CSLBzcsyyZa74VrzbeWh5w16e5SC7jQQbzl1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇷
الأمين العام لحلف الناتو، حول إيران:
لماذا كان من الضروري تدخل الولايات المتحدة لإزالة القدرات النووية الإيرانية؟ ولماذا ينظر الجميع الآن مرة أخرى إلى الولايات المتحدة فيما يتعلق بحركة أنصار الله في البحر الأحمر؟
لأن الأوروبيين بطريقة ما لم يمتلكوا القدرات الكافية للقيام بذلك بأنفسهم. هذا هو "الفناء الخلفي" لأوروبا، وليس "الفناء الخلفي" للولايات المتحدة.
في المستقبل، فإن ما ستحصلون عليه من حلف شمال الأطلسي (الناتو) الأقوى هو أن الأوروبيين يمكنهم الاعتناء بـ "فنائهم الخلفية" بأنفسهم.
فناء الخلفي يقصد به ان هذه المنطقة هي منطقة نفوذ حيوي لاؤروبا وليس لامريكا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/91323" target="_blank">📅 11:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
🔻
تم صرف رواتب الحشد الشعبي.</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/91322" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صحافة غربية
📰
‏
🔻
فايننشال تايمز: بحسب تحليل، يدفع سائقو السيارات الأوروبيون 40% أكثر مقابل الديزل مقارنةً ببداية عام 2026. ويعادل ذلك حوالي 30 € إضافياً لخزان وقود سعة 50 لتراً
💶
.
🇺🇸
مجموعة جرائم إلكترونية تُعرف باسم شايني هانتر سرقت أكثر من 2 تيرابايت من البيانات من أنظمة مكتب التحقيقات الفيدرالي، بما في ذلك المعلومات الشخصية لآلاف العملاء والمتقدمين للوظائف.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/91321" target="_blank">📅 11:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91320">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
مصدر عراقي لنايا
محكمة جنايات الكرخ تصدر حكماً بالإعدام بحق المدان محمد عبد المجيد خلف الطائي، قاتل العميد هشام محمد طلاع والمفوض خالد عباس لفتة، عن جريمة استهدافهما أثناء أداء الواجب في منطقة الدورة جنوبي بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/91320" target="_blank">📅 10:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7c3165ca.mp4?token=i9UgrKtp0S4F5dvYtZ27pBpxeD9m_f9OkvzMOBfhcNFmvexcUuN9udy2RfXeO1S3C82lo16ISe8gupb_Iq9ZDOP3vypOkr6rul6QEMR760GadLm3a0EUarxymecGC6tQrIJ2RILMAqtND3ViJHlblOv5opYeM2yrriFmj07Cpp860BDoZc2pyezoegqg598mq7yZlWILm8v5j0nTit7WPRCVEU7TTSxoQ39vffqkw79wEI2BUIjtoPu6m9EfqPa8zTDq5zvH74OCYSIp2pqVB79_tN0uwseTpq0UsM5Ps9kkCY7w91lMRbNevYrypjA1S60Bbrh0m4c_qd-zTgNihpyJd-ckHNk0b77yhg5nvU1Nf50f1b_FzAqlRdryFVy6RS9rteK7vD3r7UhNzQP-2svzOjhgXuV3mCULcwqbqMkwP_pZnjOloZP7Z2Xm4YxNSfaX7IdhKf_TrK-BUNLH3Vpe52ixs6bnj0hM5lQEqpniPXBJVDMo2fJYBzgx5QFBN8kyY8-gkrVYWGIUMZRrs5SbxEkd8VNu8CA8xduAyC9ltb4EZTddW_re0300nxDZeNPQZE6BxMrBco4VvK5KdbWG7SiHkxl016Z--Ohoponp2dI03dUE4spWa1J_FvjmRoppZbr57-GkHLSboIDNBHy0FCeRFRDaKRHLtW0qVlE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7c3165ca.mp4?token=i9UgrKtp0S4F5dvYtZ27pBpxeD9m_f9OkvzMOBfhcNFmvexcUuN9udy2RfXeO1S3C82lo16ISe8gupb_Iq9ZDOP3vypOkr6rul6QEMR760GadLm3a0EUarxymecGC6tQrIJ2RILMAqtND3ViJHlblOv5opYeM2yrriFmj07Cpp860BDoZc2pyezoegqg598mq7yZlWILm8v5j0nTit7WPRCVEU7TTSxoQ39vffqkw79wEI2BUIjtoPu6m9EfqPa8zTDq5zvH74OCYSIp2pqVB79_tN0uwseTpq0UsM5Ps9kkCY7w91lMRbNevYrypjA1S60Bbrh0m4c_qd-zTgNihpyJd-ckHNk0b77yhg5nvU1Nf50f1b_FzAqlRdryFVy6RS9rteK7vD3r7UhNzQP-2svzOjhgXuV3mCULcwqbqMkwP_pZnjOloZP7Z2Xm4YxNSfaX7IdhKf_TrK-BUNLH3Vpe52ixs6bnj0hM5lQEqpniPXBJVDMo2fJYBzgx5QFBN8kyY8-gkrVYWGIUMZRrs5SbxEkd8VNu8CA8xduAyC9ltb4EZTddW_re0300nxDZeNPQZE6BxMrBco4VvK5KdbWG7SiHkxl016Z--Ohoponp2dI03dUE4spWa1J_FvjmRoppZbr57-GkHLSboIDNBHy0FCeRFRDaKRHLtW0qVlE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇺🇸
🇮🇶
🇾🇪
وزير الخارجية الأمريكي
ماركو روبيو يزعم
:
"
كتائب حزب الله" العراقية هي المسؤولة عن الهجمات بالطائرات بدون طيار التي استهدفت خط الأنابيب الذي يربط بين الشرق والغرب في السعودية في وقت سابق من هذا الشهر.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91319" target="_blank">📅 10:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91318">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6Nknfbh7QcWxD7NfMr1YQ_eQ9j4m_eeo1njT8Mju3V4-aft4nlb7ut4QfuwzhVLDAHlfSQ3TRdQu-KAQ96ASHxRsDt-5Bn-jILTmgDG2JesRBe6o8swhyBUx2F_SoU3suKjcvLYgrPNtCW0b4vQ77N89zXfEtU5ZvNo68xLgTFVWJWagsP1-C6G1kR3dmf_bMwwHbnLffiyTzMwDmRHnoKwyxDCskys0N0KtlohAxkbHVB3q5vzhMSSw7r5KvH3-Bqk7-xQUEMyTAa97bi2oj8j0ETb-8axZ7kMl2tL_C8Sf9zjFXahT18fpusaUFccudk5QtYepZGS9zm2QBC5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقع فلايت رادر : يوكد ما انفردت به نايا   توقف الملاحة بمطار الرياض الدولي</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91318" target="_blank">📅 06:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91317">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
🇮🇷
‏ستيف ويتكوف:  خضنا محادثات مطولة مع الوفد الإيراني عبر وسطاء.  ‏الوسطاء أتموا بنجاح جولة مناقشات بين أميركا والوفد الإيراني نأمل أن تكون بناءة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91317" target="_blank">📅 06:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91316">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية في أجواء  المخا بمحافظة تعز، وقد تم استهدافها بسلاح مناسب.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91316" target="_blank">📅 05:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91315">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇦
🇺🇸
زيلنسكي:
الولايات المتحدة ستسعى للتوصل إلى اتفاق لوقف الهجمات على البنية التحتية للطاقة. حياتنا أهم من أسعار الطاقة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91315" target="_blank">📅 04:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91314">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇦
🇷🇺
إنفجارات عنيفة تهز العاصمة الأوكرانية كييف نتيجة هجمات روسية بالطائرات المسيرة الإنقضاضية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91314" target="_blank">📅 04:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91313">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9064f0220.mp4?token=aN2wepKPJevhNzMWouDexZSfMUzBkhJ7EN_3btFMgQHdyjpNXNwrZD_T7xxp6wWqVX82gKEigQIQXVetnJwarfmIYEth1UZjQ2tEMZkPUe0psTvoG8mgZOxZSAsC2K-lir5MaXz_28RHmElZ7vCu58M5P-n_itztARKQS7Oc1iZv3HQNXQT6jPJVjh6ofB5UrN-S8Jb1_aFigNI0ReROE7lQltkGP5-NCmAuNk3Er1mvxCxS7S6WM1fcffMQ-wavuTx2cE8OHaaIO92eAHFtwO-pjUB0YVxBkiGvcB9fMr5yUzm8Ej1wlVWJ1KD2XU7FQ4T6RI3vxeF6hRPN2z63ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9064f0220.mp4?token=aN2wepKPJevhNzMWouDexZSfMUzBkhJ7EN_3btFMgQHdyjpNXNwrZD_T7xxp6wWqVX82gKEigQIQXVetnJwarfmIYEth1UZjQ2tEMZkPUe0psTvoG8mgZOxZSAsC2K-lir5MaXz_28RHmElZ7vCu58M5P-n_itztARKQS7Oc1iZv3HQNXQT6jPJVjh6ofB5UrN-S8Jb1_aFigNI0ReROE7lQltkGP5-NCmAuNk3Er1mvxCxS7S6WM1fcffMQ-wavuTx2cE8OHaaIO92eAHFtwO-pjUB0YVxBkiGvcB9fMr5yUzm8Ej1wlVWJ1KD2XU7FQ4T6RI3vxeF6hRPN2z63ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏
رئيس الوزراء البريطاني:
نحن نقف إلى جانب إسرائيل في مواجهة التهديدات المستمرة، بما في ذلك التهديدات القادمة من إيران، التي تستهدف إسرائيل والشعب اليهودي في جميع أنحاء العالم.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91313" target="_blank">📅 03:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91312">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/747a67a438.mp4?token=cpUy9Sf-924T98I4GhhOJbQWGLVipf8da4OMWEFwhKoB0C_1csRLSspTdnMnXEp3XD7P6uQBxDnNtZtUIiaUvemyzuWlWwmzI6HgqM3oh9hZgvEiZ524a3GaqxxAgXV_XrObnncvg3zHxxdg_l84M-r4NyDf7Iw0pbcnbXkgJxz-bZj8vqOTgPZCGSvARRtouLNszLc2w4hBbubQ3Za450ubLrKJiCY9KrbGS7xytw-yhz3QzyK-nLJwSxIEKxvZIEni_KieZy0myLkLTqQG2scWl1nirvT7IoHXE0BPLBwZNa7nzOZG-CdDpQ64bZcJTx2Ju0hDQWf14Rs_eC-LEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/747a67a438.mp4?token=cpUy9Sf-924T98I4GhhOJbQWGLVipf8da4OMWEFwhKoB0C_1csRLSspTdnMnXEp3XD7P6uQBxDnNtZtUIiaUvemyzuWlWwmzI6HgqM3oh9hZgvEiZ524a3GaqxxAgXV_XrObnncvg3zHxxdg_l84M-r4NyDf7Iw0pbcnbXkgJxz-bZj8vqOTgPZCGSvARRtouLNszLc2w4hBbubQ3Za450ubLrKJiCY9KrbGS7xytw-yhz3QzyK-nLJwSxIEKxvZIEni_KieZy0myLkLTqQG2scWl1nirvT7IoHXE0BPLBwZNa7nzOZG-CdDpQ64bZcJTx2Ju0hDQWf14Rs_eC-LEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية عن انسحاب انصار الله من المخا وباب المندب واخلائهم العاصمة صنعاء والاتجاه الى صعدة بعد هذا الفيديو</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91312" target="_blank">📅 03:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91311">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
ستيف
ويتكوف:
خضنا محادثات مطولة مع الوفد الإيراني عبر وسطاء.
‏الوسطاء أتموا بنجاح جولة مناقشات بين أميركا والوفد الإيراني نأمل أن تكون بناءة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91311" target="_blank">📅 03:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91310">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇱
🇸🇾
الجولاني يكشر انيابه: الجولان هي أراضٍ سورية تقع تحت اعتراف الأمم المتحدة. لا يوجد أي نقاش حول هذه الأراضي ومن هي الجهة التي تملكها.  والقنيطرة ودرعا وريف دمشق والسويداء؟؟؟ https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91310" target="_blank">📅 02:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91309">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">توقف العمل بمطار الرياض الدولي نتيجة هجمات اصحاب الأقدام الثقيلة أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91309" target="_blank">📅 02:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صنعاء بعيدة الرياض اقرب
اخوة نورة معكم ومعنا بحر من الدم</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91308" target="_blank">📅 02:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات عنيفة تهز الرياض الان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91307" target="_blank">📅 02:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91306">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91306" target="_blank">📅 02:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91305">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات عنيفة تهز الرياض الان</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91305" target="_blank">📅 02:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91304" target="_blank">📅 02:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c6dca259.mp4?token=RkiFcmq9UBFG3u1yDMQVyZonwKKWqB7qYI5gfAmwcftjN1ombs6tFB6GkU4z9hrHkBV4gzsq7p54yF9u8LtJGXwS4EmO5xj-LXkTSQ8CDQE23ZT1kzPKxvNqqL3GS1eykhu2kiwyV2fvRLdlsNxtXYjD18284VvjX5bI-novCp_DPZ1mcD_h7_Cvjppc5OH20OQfGFDxZgWWO4Jf85phAJM9Hh3fcLIyssLnHc5W192Y8VGaO3G_SBghYcBWR5xvGYkt1Zc1QvIqJFmut63d6-rP4ipJHnatGk9f8aOyc4W2H6pLNY2Qg08_U5U7aYeW7UrGsCx721ejign53eiHkiEhzre45dbqqcL1XeNx6dtUzhlaR3nOJy51_CgAYkdA5E9u0qwpczlHw8XyaEyyT_muG32OCbHym6-0xkha-96GHpeh0Ak4dLPbPv_78Qdo6I__qUeO1aXU02xPVjCKBvGkY1RYjOpggnm-pUSPREYa2EOHyFAE9eAkd8G50_aj5Xt9h5APIsmmBDV7eWZjhvN6uJS3wL1PhP_KmF0sK2LSmGiYNFhIpV-5to4rbQTvkrUozsHapl8DFnQkQRCH4W7nWHfri26KXDT2IAnjw-j-U41BOuvo98IBc2sBKBMycqO_VAl9Y717s0C1UTWDCLiEKC51ls0yBXAYsyf2whQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c6dca259.mp4?token=RkiFcmq9UBFG3u1yDMQVyZonwKKWqB7qYI5gfAmwcftjN1ombs6tFB6GkU4z9hrHkBV4gzsq7p54yF9u8LtJGXwS4EmO5xj-LXkTSQ8CDQE23ZT1kzPKxvNqqL3GS1eykhu2kiwyV2fvRLdlsNxtXYjD18284VvjX5bI-novCp_DPZ1mcD_h7_Cvjppc5OH20OQfGFDxZgWWO4Jf85phAJM9Hh3fcLIyssLnHc5W192Y8VGaO3G_SBghYcBWR5xvGYkt1Zc1QvIqJFmut63d6-rP4ipJHnatGk9f8aOyc4W2H6pLNY2Qg08_U5U7aYeW7UrGsCx721ejign53eiHkiEhzre45dbqqcL1XeNx6dtUzhlaR3nOJy51_CgAYkdA5E9u0qwpczlHw8XyaEyyT_muG32OCbHym6-0xkha-96GHpeh0Ak4dLPbPv_78Qdo6I__qUeO1aXU02xPVjCKBvGkY1RYjOpggnm-pUSPREYa2EOHyFAE9eAkd8G50_aj5Xt9h5APIsmmBDV7eWZjhvN6uJS3wL1PhP_KmF0sK2LSmGiYNFhIpV-5to4rbQTvkrUozsHapl8DFnQkQRCH4W7nWHfri26KXDT2IAnjw-j-U41BOuvo98IBc2sBKBMycqO_VAl9Y717s0C1UTWDCLiEKC51ls0yBXAYsyf2whQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
الجولاني يكشر انيابه:
الجولان هي أراضٍ سورية تقع تحت اعتراف الأمم المتحدة. لا يوجد أي نقاش حول هذه الأراضي ومن هي الجهة التي تملكها.
والقنيطرة ودرعا وريف دمشق والسويداء؟؟؟
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91303" target="_blank">📅 01:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPeS3HgA_svLKLJOkLCPOz10EYkBv6zxQCtoYBsMZSXzoSbP8iAeerpuS9fIKUn1Lvkiinjc7UZkPku5zvOvM-HCT0nuyNqry_ZQnA0MISYBhg0TrrQv6fWzoO5UNsv3PTlbQ9eYNzMhpJBvlQIMgWNnhPWSxNsxOwz2jeTvbDVmMUxR-GQFmH27pqQndEvaYV5cIr83b5gbYz9M89Z7kaDWT_rn0GsY8K4QYM6QntYvC95erTEHEcEgIsifqzmW4PuaPtqpfZfYzVVBrJUt9mIBL8GMG2v0aU8QOB1Vi_6zxRVg_7VdvZ5qQVMm07mM7f1qphkC9BGbAPTq8SHFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصحك راجع التاريخ واتمعن بماضـــــيه
مطارك ياهو حول بيه بيام الكفائــــــــيه
شلون ترد الزاير شتگل للعباس</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91302" target="_blank">📅 01:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
إشتباكات صاروخية بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91301" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOIoGn3e35biJ8up9KZ2Len7ku0XnpVIpx6QnSOs7INR1NkSO4V0TdH-yrQ14bsUPI6iIiG3_mKjW34BXS7HwbeYzS-w0Dbg7HY6yOgrYWn-eU6BlkhDUuhtrI8CpbYTpkhWc7WPZaXhIoOTPIa0VdlAg6lAqZcnZYtswdqmjqSvqU1Lk3p-zJ6cshn-IYcrojDjKZLU7jnZsQBhGhwXiQ4Hp24UZqfCLM1N-NmANsQh77pzhK-3yT7SxNdtrUwORid_rRqKda6KbbLfPDJMoOtEkC9OwaKCcFTPP4CFDYtx6o275ergR3b-Kne-MTkMeXyqLEVCxN71qGC-1TrWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تنخفض لتصل الى 97 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91300" target="_blank">📅 01:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
إشتباكات صاروخية بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91299" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
خلية الاعلام الامني العراقي:
مناقشة تسليم السيطرات الأمنية في المحافظات المذكورة إلى قوات وزارة الداخلية وخروج قوات الجيش والحشد الشعبي من داخل المدن وفق ترتيبات وآليات يجري تحديد تفاصيلها بما يضمن انسيابية العمل الأمني واستمرار حفظ الأمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91298" target="_blank">📅 00:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
شرطة نيويورك:
تم فحص الطرد الذي يوجد امام مبنى الامم المتحدة والتأكد من عدم وجود أي شبهة جنائية في مدينة نيويورك.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91297" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f63dc50f21.mp4?token=Q49dVKnm_NWsWgLyKb2MXabhfVUsq9TdRkNpJmxj0Gk6tZqREzl8Y-MdTe5C8NdFPZ6QXPh88Ztx25MKfIWufOPEvklGqnxaZifJjr87sphx8-__9Se6c8Ynq65i8do-9vhTJaArs3QWZMc3kmqIqCr40LaBnk3O7G4eNEqWPfEce5JzuacAQIkgSn7azOVidljRzORBMcyV_xQDBTJrXTdHV-1vD90_BJxpJQt4WtdJU-ama0HuAqWkvehKl8WlqBH6DdLaDCbxJeFr56bETtN4byQZ_DP8moUqpyL285oaJZh3X8KbpY2A-BqixVNMzWt01iKrxiZwHoeDK7D2hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f63dc50f21.mp4?token=Q49dVKnm_NWsWgLyKb2MXabhfVUsq9TdRkNpJmxj0Gk6tZqREzl8Y-MdTe5C8NdFPZ6QXPh88Ztx25MKfIWufOPEvklGqnxaZifJjr87sphx8-__9Se6c8Ynq65i8do-9vhTJaArs3QWZMc3kmqIqCr40LaBnk3O7G4eNEqWPfEce5JzuacAQIkgSn7azOVidljRzORBMcyV_xQDBTJrXTdHV-1vD90_BJxpJQt4WtdJU-ama0HuAqWkvehKl8WlqBH6DdLaDCbxJeFr56bETtN4byQZ_DP8moUqpyL285oaJZh3X8KbpY2A-BqixVNMzWt01iKrxiZwHoeDK7D2hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
الاعلام السعودي ينشر:
علموا أولادكم أننا أقدم دولة في الشرق الأوسط.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91296" target="_blank">📅 23:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇱
اعلام العدو:
تفعيل انذار امني قرب الحدود الاردنية خوفا من عملية تسلل نحو الاراضي الفلسطينة المحتلة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91295" target="_blank">📅 23:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية:
كمية النفط المصدرة في شهر آب وصلت إلى 70 مليون برميل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91294" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
إن التصريحات العدائية والتهديدات المتكررة التي يطلقها رئيس الولايات المتحدة الأمريكية ضد إيران، والتي تأتي في سياق استغلال منبر الأمم المتحدة لتبرير العدوان وخلق حالة من عدم الاستقرار والنهب في العالم، هي في الواقع مجرد أداة للدعاية الداخلية، ولا تستند إلى حقائق ميدانية.
إن هذه التصريحات تعكس الجمود الاستراتيجي للولايات المتحدة في عدوانها ضد الشعب الإيراني.
إن تكرار الادعاءات والتهديدات التي لا أساس لها، في ظل تدهور الجيش الأمريكي، ليس دليلًا على القوة، بل هو دليل على اليأس الاستراتيجي.
إيران الإسلامية لطالما كانت ركيزة الأمن في المنطقة، وخاصة بالنسبة للتجارة الحرة والدولية؛ في حين أن الولايات المتحدة، بحضورها غير المشروع وغير القانوني والمتجاوز في منطقة غرب آسيا، هي مصدر تهديد وعدم استقرار. وتسعى، لتعويض سلسلة الهزائم المتتالية في أعمالها العدوانية ضد إيران والنهب البحري، إلى أسر الاقتصاد العالمي.
إن خطاب رئيس الولايات المتحدة الأمريكية لا يغير حسابات القوة، ولن يعوض أبدًا مكانة هذا البلد المتدهورة في النظام العالمي الجديد، ولا الهزائم المهينة التي تكبدتها الولايات المتحدة في الحرب ضد إيران وجبهة المقاومة.
إن القوات المسلحة القوية والفعالة في إيران الإسلامية، التي تستفيد من تجارب الدفاع المقدس في الحرب الثمانية سنوات والحربين المفروضتين، مستعدة تمامًا لتقديم ضربات أقوى وأكثر تدميرًا وغير متوقعة للمعتدين وقادة الولايات المتحدة وإسرائيل.
إن شاء الله، سيقوم رئيس الجمهورية الإسلامية الإيرانية بنقل رسالة الشعب الشجاع والقوات المسلحة البطلة وقوة إيران التي لا تقهر إلى العالم في منتدى الأمم المتحدة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91293" target="_blank">📅 23:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/91292" target="_blank">📅 23:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVO8OsfUlSndAg_lWVRr2rkULJIADXE28Bx8PV8q71zcpQtmIsvmcwNJNcOsz0I7WQtCAi3K4jxRXKnRifIPSZx4YklUPfevRx1Cd8NpGOtc1YP6RiAs-B5jYpAMOZz-yTjSCWZeNjd_Do_ChrRYskudr2rnhgj-H2n-FKuLYQT2MTtBi93fj3UCxoQydZSa194u_eu2OAZ3o6Yxd8vHteICLLh8iwFsoLmqfSJ5IGrmhPfcdIH5Gfo9j-vFGws1yZUBVuprTWd2v1knOI2ltFuGAwTt2FRIFXyFakP2OBro8nalgjOx_nO5HN9r4HAsMryeVCrLD6Qtb0T0LTm2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91291" target="_blank">📅 23:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c14b8577.mp4?token=GXdBy9ntOxBfyU7JIyM8_UtecT9gHQ9kc4l63VhMfPL6lVwTY2a8Cu_A6htu1t828qpvDaX8EYIopMcFpL172Hgr3BXQ7jyQspKnT16uksvY-okN7T5RgiYY0L07PolIMzjL5foAw-tzWhRfJ5p5qFM6GOORH4KnDkN_2lF6C4UvobfmQWFZsNm9yqFCu_uPYh45XJ6KoT5ybl1nmz4LahuDUDyMBHPdr3Sccx5zmiHTv-ss-QWZVKmkeakorBdGYD7m01CLgxdU5KQrQXsNCjbn6_Tciwxu5SHNGea87MGFsYoELQPhaYrzz0AWoEOUfNP-ZN-rb5JN1Qe8YVgm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c14b8577.mp4?token=GXdBy9ntOxBfyU7JIyM8_UtecT9gHQ9kc4l63VhMfPL6lVwTY2a8Cu_A6htu1t828qpvDaX8EYIopMcFpL172Hgr3BXQ7jyQspKnT16uksvY-okN7T5RgiYY0L07PolIMzjL5foAw-tzWhRfJ5p5qFM6GOORH4KnDkN_2lF6C4UvobfmQWFZsNm9yqFCu_uPYh45XJ6KoT5ybl1nmz4LahuDUDyMBHPdr3Sccx5zmiHTv-ss-QWZVKmkeakorBdGYD7m01CLgxdU5KQrQXsNCjbn6_Tciwxu5SHNGea87MGFsYoELQPhaYrzz0AWoEOUfNP-ZN-rb5JN1Qe8YVgm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني: إبلاغ شروط إيران لفتح مضيق هرمز كان السبب في قبول طلب فيتكاف لعقد هذا الاجتماع.  تم إبلاغ الموقف الإيراني القاطع لممثل الولايات المتحدة خلال هذا الاجتماع.  رفع الحصار البحري بشكل فوري، وسداد جميع الأموال المجمدة لإيران بشكل فوري، وإنهاء…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91290" target="_blank">📅 23:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
ترامب: مسؤولون أمريكيون اجتمعوا مع وفد إيراني في وقت سابق لمدة ثلاث ساعات، كان الاجتماع مع إيران مثمرًا جدًا، ومن المقرر عقد اجتماع آخر في المستقبل القريب.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91289" target="_blank">📅 22:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91288">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#هام
النجباء تهدّد مبعوثَ ترامب:
🔻
ستحمل مشروعَ نزع السلاح معك إلى القبر!
Al-Nujaba Threatens Trump’s Envoy:
🎬
You will take your disarmament project to the grave
‼️
Message from the Iraqi Resistance to Tom Barrack: You and your boss, Donald Trump, should realize that Iraq is not the Plaza Hotel</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91288" target="_blank">📅 22:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
من أُحد إلى علي الطاهر
قد تتغيّر الوجوه، وتتبدّل ساحات المواجهة،
لكن الطريق واحد: أن تبقى واقفًا حين يريدك الجميع أن تنكسر.
من بين الغبار والركام، ومن قلب كل امتحانٍ قاسٍ، يولد الثبات من جديد.
ليس لأن الطريق سهل، بل لأن التراجع ليس قدرًا.
﴿فَاسْتَقِمْ كَمَا أُمِرْتَ وَمَنْ تَابَ مَعَكَ وَلَا تَطْغَوْا ۚ إِنَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ﴾
🔻
انتاج نايا على التلغرام
#حسن_مات_كالحسين</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91287" target="_blank">📅 21:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
ترامب: مسؤولون أمريكيون اجتمعوا مع وفد إيراني في وقت سابق لمدة ثلاث ساعات، كان الاجتماع مع إيران مثمرًا جدًا، ومن المقرر عقد اجتماع آخر في المستقبل القريب.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91286" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
ترامب
: مسؤولون أمريكيون اجتمعوا مع وفد إيراني في وقت سابق لمدة ثلاث ساعات، كان الاجتماع مع إيران مثمرًا جدًا، ومن المقرر عقد اجتماع آخر في المستقبل القريب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91285" target="_blank">📅 21:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
🇺🇸
جيش الاحتلال الأميركي ينشر صورة لمنظومة فالانكس للدفاع الجوي بالشرق الأوسط.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91284" target="_blank">📅 21:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
انفجار عبوة محلية الصنع امام احد المنازل في محافظة ذي قار جنوبي العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91283" target="_blank">📅 21:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igpJCR6bT--jmM9cKGwwQ9MZwCdNwQ_mYePfKEsZ31yopnRPBv3_b_YcDbb-eyUVHT3x8xlK-RfltjMM-ZkX806sG3RbKhUDjhuoFSyugqV6K974UxJtxFBKaGgbfEiG50hY6zCEVlN72KrQEGuy6b-IfKiuQe5xkul1PvlorD1MTw6ClPi191tOkOXCJIqqkYCdE8wq3uGw2LIfFKuc8sC4nvVsaIii6KLQfLAYPT1w79Ngp1bKMKprdR_3NM-A0h1DHjuSTSwODg8UtI3NdYDw1_jOoVbPRpMFgpdLKSN6bqdYB-hzx-5C86bmeeLLMT2_Ly81A0cjlsE006FL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
المتحدث بأسم المقاومة الاسلامية كتائب سيد الشهداء:
هل غلق المطارات امام الطيران الايراني يشبه منع الماء عن عيال الحسین ع ؟!!!!
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91282" target="_blank">📅 20:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
🇮🇶
المبعوث الاميركي:
نزع سلاح الفصائل أمر مهم للعراق والعراقيين.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91281" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3ddfe5aa.mp4?token=pIGC3KHxOBNmo01uO_7UnA99Cnr8btdMzWjxvwECySdV0kyLmMII7SCeYp2OwqH9pdHtFLFwATGeGAkAxj8y9VOOa5uW2bMmgqn1T_ewjKsNVI-cIB5j4XAATgNjvZ7hiQgNR_QZsaRl1lEOvQnf1sMm5_UjOIFCRx9srUdxIYARB3jHAHauEmcJoepfSgItSn7VP5b_y0zU1NygMh_OfqH341TA-q0uIne2F_gsVCP4_5oMdjYuW2Y8KsJobR8vTfskGlfmHz40w9Rmw6gDDCthu26dtzY1V3fDNaW73ByezZ9f5i_94OAHjS_IYvxlU1ReTJWz9tOT1TNP2nGglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3ddfe5aa.mp4?token=pIGC3KHxOBNmo01uO_7UnA99Cnr8btdMzWjxvwECySdV0kyLmMII7SCeYp2OwqH9pdHtFLFwATGeGAkAxj8y9VOOa5uW2bMmgqn1T_ewjKsNVI-cIB5j4XAATgNjvZ7hiQgNR_QZsaRl1lEOvQnf1sMm5_UjOIFCRx9srUdxIYARB3jHAHauEmcJoepfSgItSn7VP5b_y0zU1NygMh_OfqH341TA-q0uIne2F_gsVCP4_5oMdjYuW2Y8KsJobR8vTfskGlfmHz40w9Rmw6gDDCthu26dtzY1V3fDNaW73ByezZ9f5i_94OAHjS_IYvxlU1ReTJWz9tOT1TNP2nGglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇸🇾
أثناء كلمة أردوغان مؤسس سوريا الجديدة، يظهر فيديو مصور أن الجولاني يتجاهل كلمة مؤسس دولته وهو يتصفح الإنستغرام.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91280" target="_blank">📅 20:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fea0ab54.mp4?token=EL77gK8gN7KtZqWE0XVoGlTpS4MIAmT_AInYgsekcEhT2DgR2cB-xLJPNQn0wKShVMJdlIC1vsm3V9nntlx8BsrdwjYfNl9ukDbHSW95nFBUlqfdnVF5g2MAZkScKP3VLCIWAlBw6ScZvmys4n4gOA33EEbkU3nqXQqbQ5gWPGsFjTrtSKETDcPF8Iv3hD41SbimjCdVQbP3X7itj4GIbDaod6HaxpZuMpkLsbqLhAwdCf_fQ35F5djeJfJmP19ZLxecy7aF_ypM54FE58Sg3wKJsgsB79WLQF2Tj3J1v6i132zvTAMijtLbxpfV0HkbKS6mogeX5wpfqTe7EEQ_dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fea0ab54.mp4?token=EL77gK8gN7KtZqWE0XVoGlTpS4MIAmT_AInYgsekcEhT2DgR2cB-xLJPNQn0wKShVMJdlIC1vsm3V9nntlx8BsrdwjYfNl9ukDbHSW95nFBUlqfdnVF5g2MAZkScKP3VLCIWAlBw6ScZvmys4n4gOA33EEbkU3nqXQqbQ5gWPGsFjTrtSKETDcPF8Iv3hD41SbimjCdVQbP3X7itj4GIbDaod6HaxpZuMpkLsbqLhAwdCf_fQ35F5djeJfJmP19ZLxecy7aF_ypM54FE58Sg3wKJsgsB79WLQF2Tj3J1v6i132zvTAMijtLbxpfV0HkbKS6mogeX5wpfqTe7EEQ_dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏بريطانيا تستدعي القائم بالأعمال الإسرائيلي بسبب المشروع الاستيطاني E1، وتعلن أنها ستفرض عقوبات ردا على التوسع الاستيطاني الإسرائيلي.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91279" target="_blank">📅 20:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش العدو الاسرائيلي:
قبل قليل وصل 14 مواطنًا إسرائيليًا إلى منطقة ألوني هباشان واجتازوا الحدود إلى داخل الأراضي السورية.
مو مشان شي مشان صحتك يا غالي
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91278" target="_blank">📅 20:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامب: سنبني قاعدتين عسكريتين رئيسيتين في غرينلاند</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91277" target="_blank">📅 20:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 19 غارة جوية من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، استهدفت محافظات تعز والجوف ومأرب وخلفت شهداء وجرحى بينهم أطفال ونساء ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا العزيز 936 غارةً وصاروخاً.
‏إن المجازر التي ارتكبها العدو السعودي المجرم بحق أبناء شعبنا ستكون عواقبها عليه وخيمة بإذن الله وقوته.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91275" target="_blank">📅 20:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي في البرلمان الايراني:
السفن المخالفة التي تعبر مضيق هرمز ستواجه بالإضافة إلى دفع غرامة تعادل 20% من قيمة حمولتها- إجراءً يقضي بالحجز المؤقت على السفينة لحين سداد الغرامة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91274" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الولايات المتحدة والدنمارك وغرينلاند يوقعان اتفاقية بخصوص غرينلاند بدون تاريخ انتهاء</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91273" target="_blank">📅 19:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇱
بن غفير:
خطتي لمنصب وزير الأمن تشمل تشجيع "الهجرة الطوعية" لسكان قطاع غزة واعتقال قيادات السلطة الفلسطينية داعمة الإرهاب ونزع سلاح السلطة الفلسطينية وتغيير تعليمات إطلاق النار ودعم الجنود ورفع رواتبهم ومنحهم أراضي مجانا.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91272" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91271">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">غرق سفينة كانت تقل شباب اكراد عراقيين من مدينة رانية في البحر الأبيض المتوسط كانوا يحاولون الوصول الى اوروبا بسبب تردي الوضع الاقتصادي في اقليم كردستان</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91271" target="_blank">📅 19:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">غرق سفينة كانت تقل شباب اكراد عراقيين من مدينة رانية في البحر الأبيض المتوسط كانوا يحاولون الوصول الى اوروبا بسبب تردي الوضع الاقتصادي في اقليم كردستان</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91270" target="_blank">📅 19:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الملك الاردني: إذا كان لدى أي شخص أدنى شك في أن الأزمة في منطقتنا تظل محصورة فيها فما عليه سوى النظر إلى فواتير الطاقة والمواد الغذائية للأسر العادية في مختلف بقاع العالم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91269" target="_blank">📅 18:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
اليابان تخفض مستوى تحذير السفر إلى 9 محافظات عراقية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91268" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cdd28462e.mp4?token=f7-coSM_GOHTalqSWfg5uUYmyRMdGZYVL9LYBsD9QbiitT1s33fn2MLzUG4XpJ7pLXpu8a_K0fIcaNf3o9jBDLDbEhSaTXKdzsievGafajnGR7eh3n1WQZhamnb2iblMl2gkUcwsc0o7F_ucFhd4ri9zTVL4GiwWWfh2LLB_dLd2iWAcvVGMSa3sjjn_LFY0tgaXWRMpRfHHDohwMZrKqz-kJehOHleopDqNBgc3AqxtFxTU8drAgQi-miv_6jsDAceujkHqWM6IZmYJII8DofGSrxIqVRnr6rYlUmC-InvkEeFZQs6P7ofW4ut72eTFBSPGl-gAgoRwaPMG1bsiral4JwTwlm5-NLVA0FfPCFLoTwjFaMM11vlX78heyeFUFaFMfz4uT2YocHI_NMW-YwQ0yR6SDibZNBoWxkUOu9bwumAZ47a-QwLg0qgzUlUMyQxSeMwjm3rRoAtxfh8TCZhMbKq3xrVKjMvWfu0yZRapbuCdRFdwAntPwNL-ONEo9k_WFiGxMDXdJSW1_AQX77Kdld-x7OH27BWZNJovpwK1mFeswp56a-S4gPkQsZ_bTKrKHKVBujHqe2-XOktjCplQqVaHNRlHIDvpNtkzBi45XazOkyGyNE7l4d5jXBzgppdkchEN915NYNpAKlMiHEKiSLrR-T4wjYyNBgCYtic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cdd28462e.mp4?token=f7-coSM_GOHTalqSWfg5uUYmyRMdGZYVL9LYBsD9QbiitT1s33fn2MLzUG4XpJ7pLXpu8a_K0fIcaNf3o9jBDLDbEhSaTXKdzsievGafajnGR7eh3n1WQZhamnb2iblMl2gkUcwsc0o7F_ucFhd4ri9zTVL4GiwWWfh2LLB_dLd2iWAcvVGMSa3sjjn_LFY0tgaXWRMpRfHHDohwMZrKqz-kJehOHleopDqNBgc3AqxtFxTU8drAgQi-miv_6jsDAceujkHqWM6IZmYJII8DofGSrxIqVRnr6rYlUmC-InvkEeFZQs6P7ofW4ut72eTFBSPGl-gAgoRwaPMG1bsiral4JwTwlm5-NLVA0FfPCFLoTwjFaMM11vlX78heyeFUFaFMfz4uT2YocHI_NMW-YwQ0yR6SDibZNBoWxkUOu9bwumAZ47a-QwLg0qgzUlUMyQxSeMwjm3rRoAtxfh8TCZhMbKq3xrVKjMvWfu0yZRapbuCdRFdwAntPwNL-ONEo9k_WFiGxMDXdJSW1_AQX77Kdld-x7OH27BWZNJovpwK1mFeswp56a-S4gPkQsZ_bTKrKHKVBujHqe2-XOktjCplQqVaHNRlHIDvpNtkzBi45XazOkyGyNE7l4d5jXBzgppdkchEN915NYNpAKlMiHEKiSLrR-T4wjYyNBgCYtic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الكوبي يغادر قاعة الجمعية العامة للأمم المتحدة أثناء كلمة ترامب</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91267" target="_blank">📅 18:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامب: كوبا ستسقط. الحرية قادمة إلى كوبا.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91266" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامب: نحن نعمل بشكل وثيق جدًا مع قادة روسيا وأوكرانيا، وسنحقق ذلك. أعتقد أن هذا الأمر سيحدث بشكل أسرع مما يتفهمه الناس. لقد انتهى الأمر.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91265" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الوفد الكوبي يغادر قاعة الجمعية العامة للأمم المتحدة أثناء كلمة ترامب</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91264" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌟
🇺🇸
ترامب:  لدي قرار كبير يجب اتخاذه. هل سيتم التوصل إلى اتفاق مع إيران يسمح لها بإعادة البناء وخلق دولة أكبر بكثير مما كانت عليه من قبل، ربما واحدة من أعظم الدول في الشرق الأوسط أو حتى في العالم؟  أم هل سأدمر الجمهورية الإسلامية وأفعل ذلك بسرعة، دون إعطائهم…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91263" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزارة الطاقة السعودية:
تعليقًا على ما ذكره معالي وزير النفط العراقي، باسم محمد خضير العبادي، ورئيس مجلس الإدارة والمدير العام لشركة تسويق النفط العراقية "سومو"، المهندس علي نزار الشطري، خلال جلسة مجلس النواب العراقي، بشأن قيام المملكة العربية السعودية بشراء 25 ناقلة نفطية وربط ذلك بارتفاع تكاليف نقل النفط العراقي، أوضحت الوزارة أن المملكة لم تقم بشراء الناقلات الـ25 المشار إليها، وأن هذه المعلومة غير صحيحة، مؤكدةً أن هذا التوضيح لا ينتقص بأي حال من حق المملكة الكامل في اتخاذ ما تراه مناسبًا من قرارات تجارية واستثمارية، وفقًا لاحتياجاتها ومصالحها
‏الارتفاع الحاد في تكاليف نقل النفط يعود إلى عوامل تختلف عما أشار إليه وزير النفط العراقي والمدير العام لشركة "سومو"، ومن بينها التصعيد العسكري في المنطقة، والهجمات الإيرانية المعلنة على السفن، والاضطرابات في حركة الملاحة عبر مضيق هرمز، وما ترتب على ذلك من ارتفاع حاد في مخاطر الشحن وتكاليف التأمين، وتراجع أعداد الناقلات المستعدة للعمل في المنطقة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91262" target="_blank">📅 18:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب: سنحيي الذكرى الثالثة للهجوم الذي وقع في 7 أكتوبر في إسرائيل. لقد قام إرهابيون مولتهم إيران بتعذيب وتشويه وقتل 1200 مدني بريء، بمن فيهم العشرات من الأمريكيين. وقد احتفل المرشد الأعلى الإيراني بهذه المجزرة ووصفها بأنها "خدمة للإنسانية".</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91261" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eed65c16.mp4?token=rkGsGtFznvOtr7Nh4K2U8onBhP7LMUCGeP5qSdFKh8qIskKqjYLcXK3CaIgG0yI-9sd9cfmro8_9dPeluv5GRJ9j7xXoMnm0cAP434J_yT9QkPuplxAKyzGEpx0Isyiow7I7S6qr5Adk6rpLA6uxEP5hO9aOrjbBeeu5bzcp-PwYt6iQ1ms0fX98iEsKNYroUuYAqqW0DptuYFeXc2mPYvkKhCc30AVVfIIv6EeODj36-_ne7NYkM1FxuiHyQs_Pg5_in-_BmrNyULGGNUcxF1q3wqRW7_AkB0Pat9AklZaLE51y-Zb0DILE2n1NJWFoaJZqglsK93QAGI3o0EpZS1lTOxej_NyWE6tqlBSOtVSTgPy3P7LfhT8HJBjH59ciRImYJaf5KL54hDEhrMLgOMWs46pPkTD4_DOHrJ9yMiPbQsMOfYrCWGwWQ9tIi0i5PQDQ4AS9b0m39DRT92SMKLc00qRjjBIcgJfeCizfff8rALba7zL-ZuYMOKU28BsR1SWkdN5CdJS4eM0At-ZLPR9fA2oHCJHzCpdZBsB0fnqB_C7ta_zBCJOK3Tqq5EfTo3e9GbqUYcQgSswBW_xyMw_mkJmo_bYNoxfDd9JGr0cgS7Q93ctSsIwx0GKPtWMcyT9GtbQRg-yrOmL45_LtNHyl_OBU_VfuXsyxEWKPEzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eed65c16.mp4?token=rkGsGtFznvOtr7Nh4K2U8onBhP7LMUCGeP5qSdFKh8qIskKqjYLcXK3CaIgG0yI-9sd9cfmro8_9dPeluv5GRJ9j7xXoMnm0cAP434J_yT9QkPuplxAKyzGEpx0Isyiow7I7S6qr5Adk6rpLA6uxEP5hO9aOrjbBeeu5bzcp-PwYt6iQ1ms0fX98iEsKNYroUuYAqqW0DptuYFeXc2mPYvkKhCc30AVVfIIv6EeODj36-_ne7NYkM1FxuiHyQs_Pg5_in-_BmrNyULGGNUcxF1q3wqRW7_AkB0Pat9AklZaLE51y-Zb0DILE2n1NJWFoaJZqglsK93QAGI3o0EpZS1lTOxej_NyWE6tqlBSOtVSTgPy3P7LfhT8HJBjH59ciRImYJaf5KL54hDEhrMLgOMWs46pPkTD4_DOHrJ9yMiPbQsMOfYrCWGwWQ9tIi0i5PQDQ4AS9b0m39DRT92SMKLc00qRjjBIcgJfeCizfff8rALba7zL-ZuYMOKU28BsR1SWkdN5CdJS4eM0At-ZLPR9fA2oHCJHzCpdZBsB0fnqB_C7ta_zBCJOK3Tqq5EfTo3e9GbqUYcQgSswBW_xyMw_mkJmo_bYNoxfDd9JGr0cgS7Q93ctSsIwx0GKPtWMcyT9GtbQRg-yrOmL45_LtNHyl_OBU_VfuXsyxEWKPEzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أعتقد أننا سنتوصل إلى اتفاق مع إيران بعد انتخابات التجديد النصفي.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91260" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏ترامب: علي أن أتخذ قرارًا كبيرًا بشأن فيما إذا كنت أود إبادة إيران أو السماح لها بالاستمرار والازدهار</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91259" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامب: لقد صنعوا صاروخاً قادراً على ضرب أوروبا، وكانوا فخورين جداً بذلك. آمل أن يدرك الأوروبيون ذلك. كان هدف إيران هو إكمال قنبلتها النووية خلف هذا الدرع الصاروخي الباليستي التقليدي.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91258" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7587284f78.mp4?token=kRHX72Q4U3xSJjhYBu44CmSz4ip6Ahop00p5v96boewiUJGix-SnExRqbo3x1KIHCS-gN3a93cYDUtwWA25fc5AWsQH9idP-EnE0M-UaguwmXdZVMezjPfenwy-VCaOinmWsPBFx6U8YCz6YTFTbJrf75SmgDMiIB7lQZ5HHJJMsbNn8LNpzVpAEfr7QdGWAspI7kB5CR0sj9tJS2ehhNaS_6sOnoMNRqnQd85As7R18R1J8-EdrnFMir31_PeNG4P4XiZoVQNXvuV5H74O5Z8ZsK4PGqaBGSqsKLRb5qYc2_uNcSbAOYgeYeFYzojyQmshzdgpuyZZiiir_48kdfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7587284f78.mp4?token=kRHX72Q4U3xSJjhYBu44CmSz4ip6Ahop00p5v96boewiUJGix-SnExRqbo3x1KIHCS-gN3a93cYDUtwWA25fc5AWsQH9idP-EnE0M-UaguwmXdZVMezjPfenwy-VCaOinmWsPBFx6U8YCz6YTFTbJrf75SmgDMiIB7lQZ5HHJJMsbNn8LNpzVpAEfr7QdGWAspI7kB5CR0sj9tJS2ehhNaS_6sOnoMNRqnQd85As7R18R1J8-EdrnFMir31_PeNG4P4XiZoVQNXvuV5H74O5Z8ZsK4PGqaBGSqsKLRb5qYc2_uNcSbAOYgeYeFYzojyQmshzdgpuyZZiiir_48kdfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أدعو إيران إلى إبرام صفقة</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91257" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامب يبدا باسطوانة دمرنا البحرية الايرانية وسلاح الجو والصواريخ والمسيرات</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91256" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامب: هدف إيران كان استكمال السعي للحصول على قنبلة نووية ولو نجحوا لبثوا الذعر والموت إلى ما لانهاية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91255" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏ترامب: دعونا إيران للتوقيع على اتفاق لكنها رفضت</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91254" target="_blank">📅 18:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e8def986.mp4?token=l08toiWxN0sRKnuvXzmyty7eiD_sEN35ecrsGVc81CxzxkSxz70YfiOUhqFhNgaaggixYM88CaYLkIrFvogAV89bFsbJ8ooLPNZPbsYvBjlmWFRxd7S_LujbIz3uNCM0ruCcNQahBMg7h8vCeV74VlcG4ArjAjT2u1F-cRFpFiYZbVuKh1VO1FFI8mCQy0NtJ-6My7Fa3Skby0TX8SzkuXtxei2UiYnkt2hISztUGLYkq08dh1wVM8eiaBfD37_EzG7Dxceszn8VTSpxWtkPiwJ86PO53aUGEK_bUKZdjT2moo0vyL391LUAg-jgKv-FEnTUae9ogXhrIFXwf8z14A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e8def986.mp4?token=l08toiWxN0sRKnuvXzmyty7eiD_sEN35ecrsGVc81CxzxkSxz70YfiOUhqFhNgaaggixYM88CaYLkIrFvogAV89bFsbJ8ooLPNZPbsYvBjlmWFRxd7S_LujbIz3uNCM0ruCcNQahBMg7h8vCeV74VlcG4ArjAjT2u1F-cRFpFiYZbVuKh1VO1FFI8mCQy0NtJ-6My7Fa3Skby0TX8SzkuXtxei2UiYnkt2hISztUGLYkq08dh1wVM8eiaBfD37_EzG7Dxceszn8VTSpxWtkPiwJ86PO53aUGEK_bUKZdjT2moo0vyL391LUAg-jgKv-FEnTUae9ogXhrIFXwf8z14A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: تستمر إيران في تطوير أسلحة باليستية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91253" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ترامب: إيران هي الراعي الأول للإرهاب في العالم</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91252" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏ترامب: إيران هي الراعي الأول للإرهاب في العالم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91251" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تحطم طائرة مقاتلة امريكية من طراز F-16 في قاعدة سبانغدالم الالمانية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91250" target="_blank">📅 17:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اكسيوس:
عدة دول وسيطة تتواصل مع الولايات المتحدة وإيران لترتيب اجتماع رفيع المستوى.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91249" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91248">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
🌟
ترامب:
من الآن فصاعدًا، لن تسمح الولايات المتحدة بوجود أي تهديدات لأمريكا في أي مكان في نصف الكرة الغربي.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91248" target="_blank">📅 17:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91247">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الامين العام للامم المتحدة غوتيريش:
ما يسمى وقفا لإطلاق النار في الشرق الأوسط ليس أكثر من إطلاق نار لكن أقل حدة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91247" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91246">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد إضافية من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91246" target="_blank">📅 16:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
مسؤول امريكي لـCNN:
أخبر ترامب مستشاريه بأنه يرغب في لقاء مسؤولين إيرانيين يحضرون الجمعية العامة للأمم المتحدة في نيويورك إذا كانت الظروف مناسبة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91245" target="_blank">📅 16:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91244">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز مضيق هرمز بعد استهداف حرس الثورة لسفن مخالفة</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91244" target="_blank">📅 16:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91243">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
مصادر حكومية عراقية:
لا قرار الى الان بمنع الطائرات الإيرانية من استخدام المجال الجوي للبلاد او الهبوط بالمطارات العراقية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91243" target="_blank">📅 16:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91242">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6lwNHOBWy-2M5U9jdSx_-XVigyWwoGujuAVY3eT4lPcAIOi4hRLYsCbT1sMqkAUU6RoDQUMZGofV3yioglETLZn0-MG74pfBRbGp5QG18WzpHTAwivBPTZLu_gFVCXyqCFBlQ0um_p5_qUdBiM36WMoj8seFiEzh3KmoHlmKU15lji5H8JuwkAfrmhRDnDoAp34s8Fo2Y21NSI_gVLyCYrsO8Kx_C4HUl3fXozfs_6y1NyZ5bQ1lNEdyf2cm7XsWDDoLe-e3E4OAebjY4Vjmv4iGxLWsYC_nyNkYIOS8Q0QrFNKGfoFrWF-zg1_heqN7KhbIzQH_evSpYKGZoGplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توقف تقني لطائرة الرئيس الإيراني في الجزائر أثناء توجهها لنيويورك</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91242" target="_blank">📅 15:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
دول الخليج تخطط لإخبار ترامب بتجنب أي تصعيد مع إيران، من المتوقع أن يجتمع قادة الخليج مع ترامب في نيويورك يوم الثلاثاء.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91240" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icG_HRma9X0zumpp4HFQVturyZ-IJmLMxFmYwvHP6omf_rL7y9DSTGvne0-SAi2Y41lYHkkKEIs6kOXDeyd1zam3mUXzfICroPni3_sszoW2iO05n5FHRH7LLhP3mPq_uwWw9tKzDgyun6TJDfUIHM7b-tnPFoyS8SqF_BMupXF5ouyJebUuHwXTQPH-2GDfRC3bKd-s12qnaRvnrXPhT6n413wTY1QY6Y0bD5jmDmZBMf3uYQrc1SWmgzZKHgu7RTmiluA6pEJiY9oD2FXHB3SBAvXZdL1luslBmOfIS-ull2YUGwA_DmUmcbmUNBZcOZ7AoVagMUV1g8LUlbG3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
المعاون الجهادي للمقاومة الإسلامية حركة النجباء عبد القادر الكربلائي:
المقاومة باقية، والحشد باق رغم أنف ترامب المجرم وسمساره الصهيوني باراك، فلن ننثني ولن نتراجع، وسنبقى حماة الوطن والسيادة والمقدسات حتى النصر أو الشهادة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91239" target="_blank">📅 15:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCuqc8ldBvKMeAB3kH9kzJa0q3tRFl1brKVlaoozOQZ5QXap6MZ9DEiI10uE_9S__uxcdC8MjXDaE10TH8emBoCJxN74ouubJ3C7uPxk0nqByzL8dmECVhfJm2TtfUB-u5mcJvxlBPYGm00ohPtGO-FVlQ3ZRzdBIs4k1ha9VNwDV9YSE1Y0ztmFqOehD7g-yCMtFd-BrH6lo-Y3kyUWaEvV9L_kdnHtGTpDhH3P4N6hnnRNb5rXkcx45-HBq428SpPTBtCcdflgeQDHhhL6WUtaSuXUpIUpKnpJxvWPLNPzsqygvsowuqqmHU_pI44C93KNfHkWXy7w-jBN3C2IGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
ترامب:
الجبناء والخونة سيحبون أن يقولوا إن الولايات المتحدة تعاني من نقص في الذخائر. هذا ليس صحيحًا.
لدينا كمية من الذخائر تفوق ما يمكننا تصوره استخدامًا، ونحن نقوم الآن بزيادة هذه الكمية إلى مستويات لم نشهدها من قبل.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91238" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed350d7bc2.mp4?token=CYljdw8BwOkt_rUFUO_QsdT89MnJ4FYJt3puGDAMrAlPRh_HqO_krkRt5_Sp_nmaL3jDsrTT8OM8iQXUoQ4fTy6niwkWkbk04uKJ3SvMBNnfaXD9z2UlPr4BAeuASPbECtv5IzapUMucfdXwBOBXWQM9xXZb8cbQea4cj1a-6jkmz7PWsE5w7X_hA_nr7op1Icv_8tnFTAarSPRc4ZPGNUmQTij6KlGylJnCYkTDt1FdfSDIwfuBDdZUI2EbWGlTut3v0fnoLogYu6bJ4eVZM8T2ZvJis3HXh308YZUb1vrYjqDBBOTbo8ubmr4B6fXyOCPd_BB_f7SO3h89cxGwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed350d7bc2.mp4?token=CYljdw8BwOkt_rUFUO_QsdT89MnJ4FYJt3puGDAMrAlPRh_HqO_krkRt5_Sp_nmaL3jDsrTT8OM8iQXUoQ4fTy6niwkWkbk04uKJ3SvMBNnfaXD9z2UlPr4BAeuASPbECtv5IzapUMucfdXwBOBXWQM9xXZb8cbQea4cj1a-6jkmz7PWsE5w7X_hA_nr7op1Icv_8tnFTAarSPRc4ZPGNUmQTij6KlGylJnCYkTDt1FdfSDIwfuBDdZUI2EbWGlTut3v0fnoLogYu6bJ4eVZM8T2ZvJis3HXh308YZUb1vrYjqDBBOTbo8ubmr4B6fXyOCPd_BB_f7SO3h89cxGwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتن ياهو يهاجم ممداني:
عارٌ عليكم، يا سيد مممداني. عارٌ عليكم لدعمكم لوحوش حماس الذين ذبحوا شعبنا. عارٌ عليكم لإثارة الفتن والاضطرابات ضد اليهود في نيويورك. سأتوجه إلى الأمم المتحدة. سأقول الحقيقة عن جنودنا الأبطال، وسأقول الحقيقة عنكم.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91237" target="_blank">📅 14:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي: لا أعتقد أن هناك أي ترتيبات حالية لاجتماع بين ترامب ورئيس إيران ولكن ترامب منفتح على الاجتماع مع أي شخص.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91236" target="_blank">📅 14:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91235">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي:
لا أعتقد أن هناك أي ترتيبات حالية لاجتماع بين ترامب ورئيس إيران ولكن ترامب منفتح على الاجتماع مع أي شخص.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91235" target="_blank">📅 14:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا مشاهد إضافية من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91234" target="_blank">📅 14:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
🇵🇰
‏
مصدر دبلوماسي إيراني:
باكستان لم تحسم قرارها بشأن تعليق رحلات شركات الطيران الإيرانية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91233" target="_blank">📅 13:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">السعودية تعلن استئناف تشغيل خط أنابيب النفط الذي يربط بين شرق السعودية وغربها</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91232" target="_blank">📅 13:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
🇺🇸
مسؤول إيراني رفيع المستوى:
- طهران ترحب بعودة الدبلوماسية إذا اتخذت الولايات المتحدة خطوات ملموسة.
- وفد إيراني موجود في نيويورك بصلاحية كاملة لإحياء الدبلوماسية مع الولايات المتحدة
- تم تسليم مقترح إيران إلى الولايات المتحدة عبر وسطاء في السادس عشر من سبتمبر.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91231" target="_blank">📅 13:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇹🇷
🇮🇷
شركات الطيران التركية "طيران تركيا"، و"بيغاسوس"، و"إيه جت" تلغي جميع رحلاتها إلى إيران اعتبارًا من 21 سبتمبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91230" target="_blank">📅 13:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91229">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
قائد القوات البرية العراقية:
القائد العام كلف رئيس أركان الجيش الفريق أول الركن عبد الأمير يار الله بإدارة ملف سنجار وفرض السيادة الأمنية الكاملة وأي مسلح غير عراقي يجب أن يغادر سنجار ولا يمكن قبول وجوده</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91229" target="_blank">📅 12:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91228">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اوكرانيا: استهدفنا مصفاتي نفط في أوفا وسمارا داخل روسيا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91228" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
