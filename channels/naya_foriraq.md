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
<img src="https://cdn4.telesco.pe/file/PIfi4sCsFZdCFU5gR3vga28W4EpX-_N-Uq2DrTftr8x8WKU4Yp7BkIhsDNDf6eMbbmxPMiLE_WxFI5wi-TIRDM2yP-eRpJbW3TcaHoVBT79jOFMlWICs0mZLr-KrDzAeUK2Zu9kQiYrr3H_14Z1y-hIrdKVVKKGflcOWcRPf8eOwkC92fykCJHUhQKZp-x3A609YJFeBt9_6WCeV2djpZ3a2RjYh_wJU_c9EMZnz7wTqsKs__FEXAJqxh7YRXCriHjI4qb0NHSfNV2ANYVeaPNzcPR4Hj0vg2jGDmDn9rgeIzDGJzMXD2gzS_JHtYhjXls0Wnpj7LTaH3d-mx6iuFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 269K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-88671">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">المنظمة البحرية الدولية التابعة للأمم المتحدة": نحو 6000 بحار على متن 400 سفينة لا يزالون غير قادرين على مغادرة مضيق هرمز</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/naya_foriraq/88671" target="_blank">📅 16:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88670">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
🇨🇳
موقع ذا إنفورميشن:
الولايات المتحدة تعمل على وضع قواعد للذكاء الاصطناعي للحد من وصول الصين إلى الرقائق الإلكترونية. الولايات المتحدة تعمل على إيجاد بديل لقاعدة الذكاء الاصطناعي الحالية.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/naya_foriraq/88670" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88668">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
🚀
🔵
إعلام غربي :
رصد طائرة مسيرة أخرى في مطار لايبزيغ هاله في المانيا ؛ ويأتي هذا الحادث بعد أسابيع من اكتشاف طائرة مسيرة محملة بالمتفجرات بالقرب من طائرة شحن أوكرانية في المطار نفسه</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/88668" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88666">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/va_nc0jsaZrOMrO7FmVqNvWYsFATub_cxp4fBvjcKgZe7zWFNJuC477MI2Adh5-8dqLglIHBJMNXN1JbTEDQd3zwEhpqvqarIqajRt1eUvb1yvJrDtsISz9p2yURf2IGSK4k24sf9RC89dj5PTE1YMl9MC27p_nxEmqo48wLfuPbURbhkKKJ-enbms9a19M0e9hrUvLkFX--qBKsWhhEKKvhC2tjBVl4rs3a0aFhIGLF6LMLgeCy0wesmHkgG_anLxVCsHKItD8XdgKGhRT39ZUFEFgaCC-bwzULgKyoKjJC4aI_H15Bi3YeoTXzrdi11yRJsXtIgFAftWTaz6H7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCeli5ZIU539Tik2dDSvqgN7GicCi3fBgz9EYVsHFjA2zz_BEr-0ZlR4V3d-pW6fMWuEw_t8SXLVW5GUcdx54NOUIPdWZSmwPkM46SZeMRGpmOm5hgaxKR6Z5j5ESocWxe571MhJwAP-npv4s3LjcFYOdq2hkpciURKkISyVb6KrpZMa3jX5K-HeLSHrZng_5u2jNWdSeyDKahwxdC2fGTbnQO8Fpuc2isbsw79Aef89SJtG3vOzQvQVHehF1LGYq67ZcXMGbdh7p04ttUDbUEoLVrhYXbZE2N--_dTCJhdVoxFpEDQfZIJvQnkjQawbNb7OoMjRpUgQZwoZ5feHKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بيان وزارة الخارجية الايرانية بخصوص العقوبات الاميركية:
بيان صادر عن وزارة الخارجية بشأن الإرهاب الاقتصادي الأمريكي ضد إيران
۱۴۰۵/۰۶/۰۶
في إطار استمرار سياساتها العدائية وغير القانونية ضد إيران، كشفت الحكومة الأمريكية عن موجة جديدة من الإرهاب الاقتصادي يوم الاثنين 2 سبتمبر 1405، تحت عنوان عملية الإقصاء الاقتصادي ضد إيران، وهو ما يرقى إلى مستوى إرهاب الدولة الأمريكية ضد إيران والعالم.
إن إساءة الولايات المتحدة استخدام الدولار كأداة لترهيب الدول الأخرى وإجبارها على اتباع سياساتها التدخلية والمخالفة للقانون الدولي فيما يتعلق بإيران، يُعد انتهاكًا للسيادة الوطنية وحق تقرير المصير لجميع الدول الأعضاء في الأمم المتحدة. وتُمثل العقوبات الأمريكية المفروضة على إيران، بطبيعتها وعواقبها، انتهاكًا صارخًا لميثاق الأمم المتحدة. إذ تنتهك هذه العقوبات مبدأ عدم التدخل في الشؤون الداخلية للدول، ومبدأ عدم عرقلة التعاون بين الدول، وهو مبدأ تم التأكيد عليه، من بين أمور أخرى، في الفقرة (2) من إعلان عدم جواز التدخل في الشؤون الداخلية للدول، القرار 36/103 الصادر في 9 ديسمبر/كانون الأول 1981، و"إعلان" مبادئ القانون الدولي المتعلقة بالعلاقات الودية والتعاون بين الدول، القرار 2625 الصادر عن الجمعية العامة في 24 أكتوبر/تشرين الأول 1970.
إن إعلان الحرب الاقتصادية على إيران هو استمرار للحرب العدوانية التي تشنها الولايات المتحدة والكيان الصهيوني ضد إيران منذ عام ونصف تحت ذرائع كاذبة لا أساس لها، مما يُهدد السلام والأمن الإقليميين والدوليين. جميع هذه الأعمال تُخالف القانون الدولي. وللأسف، فإن لامبالاة وتواطؤ منظومة الأمم المتحدة ودولها الأعضاء تجاه الانتهاكات الجسيمة للقانون الدولي من قِبل الولايات المتحدة والكيان الصهيوني قد أدى إلى تشكيل نمط خطير للغاية من خرق القانون وارتكاب أخطر الجرائم الدولية، مما عرّض الحضارة الإنسانية جمعاء لتهديد غير مسبوق.
تُثبت عملية المقاطعة الاقتصادية بحد ذاتها النية الإجرامية لمصمميها ومنفذيها في إلحاق الألم والمعاناة بالشعب الإيراني وحرمان المواطنين الإيرانيين من حقوقهم الإنسانية الأساسية، ولذا تُعتبر جريمة دولية وجريمة ضد الإنسانية. وتُعد هذه السياسة انتهاكًا صارخًا للقواعد الأساسية لحقوق الإنسان المنصوص عليها في الإعلان العالمي لحقوق الإنسان والعهود والميثاقين الدوليين، وتتعارض مع المادة 1، الفقرة 2، من العهد الدولي الخاص بالحقوق الاقتصادية والاجتماعية والثقافية. كما تُعد العقوبات الأمريكية انتهاكًا مستمرًا لحكم محكمة العدل الدولية الصادر في 3 أكتوبر/تشرين الأول 2018، والذي ألزم الولايات المتحدة بإزالة جميع العقبات والقيود المفروضة على حرية التجارة، بما في ذلك الأغذية والمنتجات الزراعية، والأدوية والمعدات الطبية، ومعدات وخدمات سلامة الطيران المدني الأساسية، والأموال ذات الصلة. وقد خلقت سياسة العقوبات الأمريكية الجديدة وضعًا جديدًا، ومن الضروري أن يتخذ المجتمع الدولي، بما في ذلك أجهزة الأمم المتحدة، التدابير اللازمة لحماية سيادة القانون.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/88666" target="_blank">📅 13:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88665">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0k3TlWXpILtiiu6AxGERnBZ_CuTaz2pn_MqRUbBqx_l9aIe5Nn7Z7ynoEvc_v22Cdxg4d0g3IOhwGZUsnvr3CwExNes5psSIMCkjN-J_ncNtnFm7Hlum5S8Btu7fYyk2ANn873F6syFyj9blCOkSCKOd8hy-KEjYZNHx5yXAhf_2B3yVlzrdbtKVK5F6oaEGLPT5jHhvO__ynlsqWW12Sr14DZRuCid1klE5DYtdjf2NGNexOif4B1VElb8l_j9Bj0g8uXu5W-eSRgQAjiu6fkwClt2FqvgIi5AUrk-VxE2FhMwQtbMkixZXUsMJjzSxmG87uU-n63k6mI5PgWbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف يعيد نشر:
معادلة هذه الحرب واضحة: إما الكل أو لا شيء!
في منطقة لا نبيع فيها النفط، لن يبيعه أحد. إذا لم يُضمن أمننا، فلن تكون أي بنية تحتية آمنة، وأمن المضيق مرهون بغياب القوات الأمريكية. لقد أكدنا مرارًا وتكرارًا أن الوضع في المضيق لن يعود إلى ما كان عليه قبل الحرب.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/88665" target="_blank">📅 12:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88664">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjgiD7eM_hIb13fB3zM8FyH_fzyZE51mJPt42CkSWS6NNN9cTpVcgtXEQbPYcxiN6R4mtVG1J9SJTDMeKqbp_WA-oJgHHq-o0iNrBlHt4F1UZYvkEsv4h7HwpKTTn21SpW17MDKnCJSJ7ftj-NTmNfUWIWLD8BhQTMS0Bb6GuT1zFr5qq-zveBbXQCEdR_3tfJ_wsJjJj-MtBhT6L5tFuVagXWGHF16N2Xmp0TL33TOi8Bn0Nme_n6asHg60rN54Vgzt3oPQsH2dPp6gLcEWx33DGuoccb77R0sllDxldTLUntQJPTAHTC58ts-ly-yEMlLKHf51qMZtg8Y-Kj1DBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
نتنياهو يتوسل لبن غفير لكي يعقد اجتماعات مع سموتريتش حتى لا تذهب الانتخابات نحو المنافسيين:
أدعو الوزير إيتامار بن غفير والوزير بتسلال سموتريتش لعقد اجتماعات يوم الأحد. لا يجوز إضاعة أي صوت، يجب أن نتحد لإنقاذ الكتلة اليمينية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/88664" target="_blank">📅 12:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88663">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇱
إعلام العدو يدعي :
‏أعلنت الشرطة وجهاز الأمن الإسرائيلي (الشاباك) عن توجيه الاتهام إلى مراهقين عربيين، أحدهما قاصر والآخر بالغ، للاشتباه في ارتباطهما بتنظيم داعش والتخطيط المزعوم لارتكاب هجمات إرهابية.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88663" target="_blank">📅 10:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88662">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Ou47A6lt6g3XgH4ZtTKDgP1fZAedaystZx_DXCiPzqhDtzuitsAXUoup_vk2n8oUjjuTynzo6Hasp42KLm6R5pEIUTufptDGSjWEVFmgRgtK4XPwZTumbb3Q2uxoGD8o8dbhHT7ESWo2ERwqIHmWEqVhF2-7TfqN8KD26ctjYGNZMRqe2k4lurDYv_vGvsMmaXSLJ2zTnxVs0GCqwAzYdiXIdf81M0eCkqb0lm293JFKnYW_TYCdhhvBphy45RMO0I6f-5c9dwGwdiZZu66TUMOYcQg2eQrrM7-j3iIxRTYvMTNAoJEmqXyquvLTWCCj28_PK45VE1aB50cqhi_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
أجرينا مناقشات بناءة ومبتكرة مع رئيس الوزراء وزير الخارجية القطري في طهران.
إن إعادة الدبلوماسية إلى مسارها الصحيح ليس مستحيلاً. ويتوقف ذلك على فهم الولايات المتحدة لحقيقة بسيطة واحدة: الضغط لا يجدي نفعاً. يجب على الولايات المتحدة بناء الثقة، والتحدث باحترام، والاعتراف بحقوقنا، والوفاء بالتزاماتنا.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/88662" target="_blank">📅 10:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88661">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
🇷🇺
الاعلام الاميركي: سبقت رحلة مدير وكالة المخابرات المركزية جون راتكليف إلى موسكو معلومات استخباراتية أمريكية جديدة تشير إلى أن الكرملين يرى أن الولايات المتحدة قد ضعفت بسبب الحرب الإيرانية، مما يمنح روسيا فرصة لتصعيد العمل ضد المصالح الأمريكية في أوروبا.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88661" target="_blank">📅 02:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88660">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyzay0vR9BPa__ebfNMv8gICDJ5YaUuhjRVpv_BpJr5dKQQZxsZcT8sTxEU5NFEBb0Ym72HRqG641RwNOR0i-Qx5D-n5F8HkIrzYHb_u-x3mqNhSHXAwTSMsSMnvO-3fxZC_hQ1lCLtOxI2zT5q-KydcY_71KqOTIfK-XAR3f4DSMeFRShpFpI6z2UKtus8hmDLpCU9XE7iiZVK5qkmyJXRJ5R2BQePrBjNlVGHetuwbXPv-3pnSGaaW6VcgGhfenXzVcbDCTD38DtkebgTGzvBwveGarXQQ2vnkiFQjV16bk5ij00C2hKkxckwbTXgczoVhjsYZeenq_lXLVRjxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: قدم جوناثان هانت من فوكس نيوز تقريرا غير دقيق بشكل خاص عن جمهورية إيران الإسلامية الفاشلة. لا أريد أن ألتقي، إنهم يفعلون ذلك. في الواقع، إنهم يتوسلون لإبرام صفقة. يجب على بريت باير تقويم فاشله، من أجل التغيير!.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88660" target="_blank">📅 02:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88659">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rqr2tD8WHg95OmzwyREnlQYqnVU_NSv_ZnSVggSJpJI6AhxklDnXzoK40Sxv9KzHXpfsMik2Kg7uQtC2nFCW7bWzPMfjGqzJxd444gNcr76EWnxvwufgzrh0xeeIBzmwemVuApVa4sy0VE2HIgZcEEiQgMZbvlcN2ADOGkuyz3qxAxrfHLuJGO4KGmFQd32UlRWI2bgOID2SAGHu2g5BCsbcRSXQZ-koO3QV_zVk8S9FQIkSCmziBMO32FilaUz6Kx3LuaoHWiOpBBYB2U-5Ew9LnB11QWOkX5nZklcknbOaLK17GDxQgu4v_7UbyHT-L2xECrGVJuVp6OzvhBvTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: قدم جوناثان هانت من فوكس نيوز تقريرا غير دقيق بشكل خاص عن جمهورية إيران الإسلامية الفاشلة. لا أريد أن ألتقي، إنهم يفعلون ذلك. في الواقع، إنهم يتوسلون لإبرام صفقة. يجب على بريت باير تقويم فاشله، من أجل التغيير!.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88659" target="_blank">📅 01:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88658">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
اشتباكات عنيفة جراء نزاع عشائري في قضاء الجبايش بمحافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88658" target="_blank">📅 01:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88657">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">المراسل: هل وجه مدير وكالة المخابرات المركزية راتكليف تحذيرًا إلى روسيا بعدم مهاجمة أراضي حلف شمال الأطلسي؟  ترامب: لا أريد التعليق على ذلك، لكنهم لن يهاجموا.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88657" target="_blank">📅 01:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88656">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88656" target="_blank">📅 01:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88655">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7lT79m2ii87tM4VgOJKJlloJQZGLVOzR-3FKFSFvuupi_6EuLq7p-iuxU9O2bUCDi6VU_b7SnMhnBVr8RDZpd5gP4vTLxIAGxiI0olh8CRkN4DOLyS1ZRmp93iJtAL_VFBDna29Opuv9by5YCte71kbGzWz7WCfBDC50zfjBBLDoate4TPskufCQW8VnAByXZ6VyhRlSKpFFa83osIQRVB_p5p-NpNi3K21eXGAZolZzSwr2BTmnsqbzYcn1IkEuAZV4rVW26GeDJEYDdcdSoDa9KqpJiiQTsXjtIU1WYBuXlMcPoU98QJ3oVsppsGmTEobnf_uT-N8ciPmvBqh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88655" target="_blank">📅 00:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88654">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
رئيس لجنة الأمن القومي في البرلمان الايراني عزیزی:
لا توجد أي سفينة تعبر مضيق هرمز دون إذن القوات المسلحة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88654" target="_blank">📅 00:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88653">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
رويترز
: زلزال بقوة 6.2 درجة شرق خليج عدن.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88653" target="_blank">📅 00:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88652">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745cf92c81.mp4?token=esIutgBP-uLRWIph1iyOGqFnH80Slq0DKjrbJIs5BsKDytj_KglUw_HVmEVuzJQ6m1he0MM7_AiXhZ11Ao1Kf5hQHRWn4_KrjAxN3DhnFH6Z3XB1yjkBf3nZFP67vWeCnvkAuM1JixnoVrtHfS64GACChxnrtuzuGE7wWwgSg3x_wB2DnB9TZkLlYik89Ln3Vb8HcTeToQUMzKkFjEWsa3S3CQeVPs2c0_cRKkm1I94F2XDIzY7GSdqu78qnILPz3I6iGbHPeH98rsRir3Caz8lsZywOmfu9rGdc2gWTVizOFUjHOxgkDQcjs6jGaDW4mk7AjDv26SKd7WHqOzqssQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745cf92c81.mp4?token=esIutgBP-uLRWIph1iyOGqFnH80Slq0DKjrbJIs5BsKDytj_KglUw_HVmEVuzJQ6m1he0MM7_AiXhZ11Ao1Kf5hQHRWn4_KrjAxN3DhnFH6Z3XB1yjkBf3nZFP67vWeCnvkAuM1JixnoVrtHfS64GACChxnrtuzuGE7wWwgSg3x_wB2DnB9TZkLlYik89Ln3Vb8HcTeToQUMzKkFjEWsa3S3CQeVPs2c0_cRKkm1I94F2XDIzY7GSdqu78qnILPz3I6iGbHPeH98rsRir3Caz8lsZywOmfu9rGdc2gWTVizOFUjHOxgkDQcjs6jGaDW4mk7AjDv26SKd7WHqOzqssQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اشتباكات عنيفة جراء نزاع عشائري في قضاء الجبايش بمحافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88652" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88651">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات عنيفة تهز دمشق</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88651" target="_blank">📅 00:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88650">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏
🇬🇧
أفادت التقارير بأن فرقاطة تابعة للبحرية الملكية ستوفر الدفاع الجوي لقمة الاتحاد الأوروبي المقبلة في دبلن بناءً على طلب جمهورية أيرلندا.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88650" target="_blank">📅 00:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88649">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
هيأة الإعلام والاتصالات تتخذ إجراءات بحق قناتي (أي نيوز) و(الرشيد) بسبب مخالفات لقواعد البث الإعلامي شملت توجيه تحذيرات وإلزام قناة الرشيد بإزالة المخالفة وتقديم اعتذار رسمي فيما قررت منع ظهور السيد عماد باجلان إعلامياً لمدة 15 يوماً.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88649" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88648">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
إدارة ترمب أبلغت الوسطاء مرارا أنها لا  ترغب في العودة لبنود مذكرة التفاهم مع إيران.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88648" target="_blank">📅 22:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88647">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
مستشار رئيس الوزراء للشؤون المالية
: 40 مليون مواطن مستفيدون من رواتب الدولة، فاتورة الرواتب تصل إلى 7.7 ترليونات دينار عراقي شهرياً وتأمينها مسألة إلزامية، سعر برميل النفط في الموازنة سيكون ما بين 50-60 دولاراً، لا توجد أية علاقات مصرفية بين العراق وإيران ولا توجد أية عمليات دفع بالدولار منذ 2011، حجم الغاز الإيراني المستورد حالياً يصل إلى 18 مليون م3 تدعم الشبكة بـ4500 ميغاواط، لا توجد أية تعاملات بالدفع الإلكتروني مع الجانب الإيراني.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88647" target="_blank">📅 21:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88646">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZm56R5oLMGreMiJIf2c6TeFEvM657idtMlciD_Sbb_VnizBwMflX5OAPv3RsftACOoEQ51QsGv5i5C3YWi7jEZXv5ZQRNxBMTBCT8x4HPvLAATb7jtxJSSHkWKdQhFfp62HcgbpsvSpK3zUD2s7mMhFZ2JYBNrkMBlSSXWrOk_1iJqvrGplbYk_Z5Xm-luvbe5ImJqobRr8yrT_G-EDXr5Zs627oM7zS03sLeyIIfqqc32G2AEgQPAxJQVv5o4AIOx_pargHJLhS0CREPKR5mIdKlGoZoJCZ0BitaO2V09chI05tNengZQsMMgFvhyPU9QO6JMgV6KoHvDIt3bUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏ناقلة غاز البترول المسال الأخرى، "سيجيت" الخاضعة للعقوبات الأمريكية، تعبر مضيق هرمز عبر الممر الذي حددته إيران.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88646" target="_blank">📅 21:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88645">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2e6046c.mp4?token=FMnP82OCZJOeyE915i_4Xkgbxc1RYZivFFcxzwr2LVP9JXFZJ7JoQpRo4CiXBQ1EhkzcuydtVrM9_1trn1ESZP_Grm8hgkl6R94T57B9uu0qhCf-7j89jhJzQVk56xbF1fdBz6ap7E6KXxp7B3k2T4qVgkETsQIOe0BGutyeYnCTwdptkc0Og6s63JX4rQnQtyvDt4V-yHRmHk_O16bDrMGn2tRmcy9SZPSFbYcjowMKdDCkstwC4fkrAsyCHk5ho8I_164HU29MkndG5QU6wtk85hQIRtPOQOY5fKKE9gWvnxaGZIVwDDxYMA52q0xT_ho8jLORX40qVZyJBqhXlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2e6046c.mp4?token=FMnP82OCZJOeyE915i_4Xkgbxc1RYZivFFcxzwr2LVP9JXFZJ7JoQpRo4CiXBQ1EhkzcuydtVrM9_1trn1ESZP_Grm8hgkl6R94T57B9uu0qhCf-7j89jhJzQVk56xbF1fdBz6ap7E6KXxp7B3k2T4qVgkETsQIOe0BGutyeYnCTwdptkc0Og6s63JX4rQnQtyvDt4V-yHRmHk_O16bDrMGn2tRmcy9SZPSFbYcjowMKdDCkstwC4fkrAsyCHk5ho8I_164HU29MkndG5QU6wtk85hQIRtPOQOY5fKKE9gWvnxaGZIVwDDxYMA52q0xT_ho8jLORX40qVZyJBqhXlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88645" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88644">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/497a3df8c4.mp4?token=YSrcDRRlfPkIG6eGPMH4ZZvYYncIOPG07viu4547NHfmF3zIxvOgBCrjbmjG2uEIHQCEC-pZuBCbeDAxVrRri2DtZq4TH4JqzbBcyFK26E0BEKjHu22M1IR_bJFUG7qv8MQ_F2tHyXaBmDnUIpZPulf859W-mVLl7Rl2dELWS14_X3ABOASWB24qk43Y0m2XN_i8oAwwv6D6LaRrKoF00rfsqOMKY5u88AAXwqA_z1OCiz6kYiI2dCZjjx3RQdkDFLvgJuPcfK_k_KmagOrQ_9svFkFClPvIJPxCwSVWLIzhBxFYY-vKHzwZ6-tAECeooDNQhSiBNu4392ABZsrm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/497a3df8c4.mp4?token=YSrcDRRlfPkIG6eGPMH4ZZvYYncIOPG07viu4547NHfmF3zIxvOgBCrjbmjG2uEIHQCEC-pZuBCbeDAxVrRri2DtZq4TH4JqzbBcyFK26E0BEKjHu22M1IR_bJFUG7qv8MQ_F2tHyXaBmDnUIpZPulf859W-mVLl7Rl2dELWS14_X3ABOASWB24qk43Y0m2XN_i8oAwwv6D6LaRrKoF00rfsqOMKY5u88AAXwqA_z1OCiz6kYiI2dCZjjx3RQdkDFLvgJuPcfK_k_KmagOrQ_9svFkFClPvIJPxCwSVWLIzhBxFYY-vKHzwZ6-tAECeooDNQhSiBNu4392ABZsrm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: بوتين لن يهاجم أراضي الناتو، لقد تصرفت روسيا بشكل جيد للغاية فيما يتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88644" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88643">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ae436795.mp4?token=S5rM_T_7lrkSqYYaFqpiXCsUJeVEWYiS8u2Gg1gBLNH6IreEyoqaW3ccdtiuXxYBjFWk7FKqT9pF-N1H-fXY8J0QYVz-gZ7jI5AVSEQxt6c7JL3p3dWmBvgBtmThfbTOznBIWvNEZl6uCY9pQvLUrM6gQ_jA5EmUtF0eXSmYDnAiZWITr1nvgmQXWsJ1pniKDlUCL6xXf3JuOATGFNvoMEELxoxtgaO28qUEcuDmzzo8uNtJfVEI1VGukw9EptOmd9ZVaEUz5tHfIbzHWrvie8SwkMAbNVe-9ITx6BTtaIi8nQthvxPml7gLJUjSUDsLPwhV1-M9btRQctoJD1QrfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ae436795.mp4?token=S5rM_T_7lrkSqYYaFqpiXCsUJeVEWYiS8u2Gg1gBLNH6IreEyoqaW3ccdtiuXxYBjFWk7FKqT9pF-N1H-fXY8J0QYVz-gZ7jI5AVSEQxt6c7JL3p3dWmBvgBtmThfbTOznBIWvNEZl6uCY9pQvLUrM6gQ_jA5EmUtF0eXSmYDnAiZWITr1nvgmQXWsJ1pniKDlUCL6xXf3JuOATGFNvoMEELxoxtgaO28qUEcuDmzzo8uNtJfVEI1VGukw9EptOmd9ZVaEUz5tHfIbzHWrvie8SwkMAbNVe-9ITx6BTtaIi8nQthvxPml7gLJUjSUDsLPwhV1-M9btRQctoJD1QrfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: بوتين لن يهاجم أراضي الناتو، لقد تصرفت روسيا بشكل جيد للغاية فيما يتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88643" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88642">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db380e2cda.mp4?token=U9kHx7K7d1pcC15YTqQKt48MUeBJmiAO6Cez2skeci5g31535XDXJBgU0orA6Nr4SqUc2mMwFI8DNZ_UYA-R4oP6HNPVfPms_w4yPJTGFTvT0EYR1SJTBUgZnh0dCM0SS0iSmULhRPTD4Q-NkUwGOovx5gssi6YXscA4oWtfGiqK3KETSUrEzSSjGn9WDHcZLL-bx6L3pciLg8yUDNZr9vBl_Dkt20eCFovAEP_C_DlEK21M9ZSmO3Q0WU_lCDPQ_Eee2fB2e8pNXJ0DyVm_BaA-E9Hl3Jwkqq7sAQzyCNRJshd7tYxL4V5YJy4K91952zhJrdChHXzhjecpFQWK2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db380e2cda.mp4?token=U9kHx7K7d1pcC15YTqQKt48MUeBJmiAO6Cez2skeci5g31535XDXJBgU0orA6Nr4SqUc2mMwFI8DNZ_UYA-R4oP6HNPVfPms_w4yPJTGFTvT0EYR1SJTBUgZnh0dCM0SS0iSmULhRPTD4Q-NkUwGOovx5gssi6YXscA4oWtfGiqK3KETSUrEzSSjGn9WDHcZLL-bx6L3pciLg8yUDNZr9vBl_Dkt20eCFovAEP_C_DlEK21M9ZSmO3Q0WU_lCDPQ_Eee2fB2e8pNXJ0DyVm_BaA-E9Hl3Jwkqq7sAQzyCNRJshd7tYxL4V5YJy4K91952zhJrdChHXzhjecpFQWK2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي عن ترامب: غير قلق على الإطلاق" بشأن احتمال قيام روسيا بمهاجمة حلف شمال الأطلسي (الناتو).</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88642" target="_blank">📅 21:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88641">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c2bbd3a1.mp4?token=gaJgBqiLEMApd0M6HK3fwZLKmC6RywrqPRmQBr2M4l29XS3O7gBWUFslguHXIZ3hHXU-DT5_AiNCek0P9Lk_fCUuc4aX7eEjrI3wxsFLWp7W9nS8kuzZNFsHunVCS6icT4bX3cb3Oj848frYpiAL6gV9LjV6xf3ZsnuAMtzziZqVQHRHq7nP9HMtrc7bBzz0CH6qMyCFMZa8KXp7xZK2OExWIYtNJvDGO0cAvEVDi36i3eMdDhSUOSMhPU6yUAiE9NHJths6L_HpLg4HAMtpASHp_uw5CastMUFF3Q_L35T68v5M0ekdTlN1wjygTivL20Q09Kv_p4Pw2f1wLFPNtl899u1MtnL9N1v_5q-yoUFVsHg_xVLX7OHNspx3KnczVuLWaNvR7-5fJaVyaFyO13tWEqTVRgD5gP1yPJof0X-eMByqoBrGktTf4LzRhsQYZuAa00QEzp4LpMOjFtKrbjo3FljYhxYKxE6VkJQNW0iJOi2c4CZ1mgxfLcKH-bqbitygz5tOcVIKucpBTwjkullRs0E5ktYtj_rsV0JtK9UbgIXNm4iBqJzACYpt59Lu5MCLREz692xXnqa8xfOhRVSosHLLdFsZHfS4QKNfnYsJ7Nt24N1yo7bfOFE3KCtYahnkmu5kJWbwW1qb4XGhv3pV3Zk02GJR31fNryDWc0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c2bbd3a1.mp4?token=gaJgBqiLEMApd0M6HK3fwZLKmC6RywrqPRmQBr2M4l29XS3O7gBWUFslguHXIZ3hHXU-DT5_AiNCek0P9Lk_fCUuc4aX7eEjrI3wxsFLWp7W9nS8kuzZNFsHunVCS6icT4bX3cb3Oj848frYpiAL6gV9LjV6xf3ZsnuAMtzziZqVQHRHq7nP9HMtrc7bBzz0CH6qMyCFMZa8KXp7xZK2OExWIYtNJvDGO0cAvEVDi36i3eMdDhSUOSMhPU6yUAiE9NHJths6L_HpLg4HAMtpASHp_uw5CastMUFF3Q_L35T68v5M0ekdTlN1wjygTivL20Q09Kv_p4Pw2f1wLFPNtl899u1MtnL9N1v_5q-yoUFVsHg_xVLX7OHNspx3KnczVuLWaNvR7-5fJaVyaFyO13tWEqTVRgD5gP1yPJof0X-eMByqoBrGktTf4LzRhsQYZuAa00QEzp4LpMOjFtKrbjo3FljYhxYKxE6VkJQNW0iJOi2c4CZ1mgxfLcKH-bqbitygz5tOcVIKucpBTwjkullRs0E5ktYtj_rsV0JtK9UbgIXNm4iBqJzACYpt59Lu5MCLREz692xXnqa8xfOhRVSosHLLdFsZHfS4QKNfnYsJ7Nt24N1yo7bfOFE3KCtYahnkmu5kJWbwW1qb4XGhv3pV3Zk02GJR31fNryDWc0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يعثر على موضوع غير تدمير القوة البحرية والجوية والبرية الايرانية...
وقع  ترامب أمرًا تنفيذيًا "يغير" اسم بحيرة أونتاريو الكندية إلى "بحيرة أمريكا".</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88641" target="_blank">📅 20:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88640">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي عن ترامب:
غير قلق على الإطلاق" بشأن احتمال قيام روسيا بمهاجمة حلف شمال الأطلسي (الناتو).</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88640" target="_blank">📅 20:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88639">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4-c3X0GWjRMpxPkM0FEFYuvRqF31RIyMZPo8boiF2IvisoHcICEYnksGSpdkxC34jMcXDtwYIozhJkfkA5BAiot9JCPt0MIq4E9fHbGnoSO9B1EMD-2wTIXUXrKNa36JAINxgOiG2vfdv3ljWF8rp0VloFfMYS9klDl5idyrT7RqDLvUEEX9Wyy9YcDWSDFFMNNVdZ605J43QGWQcsRjhvz1j6vJJi4CGvumOieBM6pVe1azd5gJH8PLy4HFpT8uF-_5Dp3PbFZ_U8YaWtVohV3WyuJAeU_9twBC_P9vIyTatVqiRGw7yi1vKEitACvjhgjwxII76hMqgwwwjPRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
بدلاً من ضخ مليارات الدولارات إلى وكيلها الإرهابي، إسرائيل، و750 قاعدة عسكرية، كان بإمكان هذه الإمبراطورية الفاشلة إنفاق تلك الأموال على شعبها، لكن لا، سيكون ذلك منطقياً للغاية بالنسبة لهذا النظام.
‏يا سكوتي، يا رجل، مصداقيتك على المحك. افعل شيئاً.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88639" target="_blank">📅 20:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88638">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
أمين مجلس الأمن القومي الإيراني رضائي:
إذا بدأت أمريكا أي عمل ضدنا فستحل كارثة على مصالحها العسكرية والاقتصادية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88638" target="_blank">📅 20:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88637">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da9299db7.mp4?token=ndwrgCaZpwuKzpuHyMgkOTgEbp0XOiNKyc2ctGWo-NrLwaOwsjhM6jwI4yJKOOi95ARksAV_uH4g-GYwWzqJALWQmb_p3rX2j6PcZG4MQrLV8Tjr7v2uyShPQWI9czubL4UMGlcZ4B06hdBAFOIv6tUlRDCM2xurJVEGhbyiAow8i23QPS7jAo-lKjV0AZyGrDm_IoCeXk0TtfXLo58Klt2m3Qdo2DRCNdzv-WEpU-Lgk8Qiqote7R_TeLhEz1RFIJHclZ1FJFngHLgOQqzt3EAPnVFOZJcbAjZ65ccIboSU4MSMUPf7X0H0ugcNLYp8_-uanl2p-_J-1KvRuJLiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da9299db7.mp4?token=ndwrgCaZpwuKzpuHyMgkOTgEbp0XOiNKyc2ctGWo-NrLwaOwsjhM6jwI4yJKOOi95ARksAV_uH4g-GYwWzqJALWQmb_p3rX2j6PcZG4MQrLV8Tjr7v2uyShPQWI9czubL4UMGlcZ4B06hdBAFOIv6tUlRDCM2xurJVEGhbyiAow8i23QPS7jAo-lKjV0AZyGrDm_IoCeXk0TtfXLo58Klt2m3Qdo2DRCNdzv-WEpU-Lgk8Qiqote7R_TeLhEz1RFIJHclZ1FJFngHLgOQqzt3EAPnVFOZJcbAjZ65ccIboSU4MSMUPf7X0H0ugcNLYp8_-uanl2p-_J-1KvRuJLiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد محزنة لواقع الشعب الكوردي في شمال العراق؛
مواطن يمسح شعاراً سياسياً كورديّاً عن سيارته أثناء محاولته تعبئة البنزين في إحدى محطات محافظة كركوك، بعد مطالبة المصطفين معه بذلك، ليستجيب ويمسحه دون تردد.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88637" target="_blank">📅 19:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88636">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
🇾🇪
الجيش اليمني يشن هجوما على جزر بالبحر الأحمر بالصواريخ الباليستية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88636" target="_blank">📅 16:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
وزير النفط الإيراني:
حوالي 40٪ من القدرة الإنتاجية المتضررة في حقل "جنوب بارس" للغاز قد عادت إلى العمل.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88635" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
لا توجد مفاوضات جارية حاليا مع إيران.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88634" target="_blank">📅 16:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇶🇦
🇮🇷
وزير الخارجية الايراني عباس عراقجي يستقبل رئيس الوزراء القطري وزير الخارجية في العاصمة طهران.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88633" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a52181c7e.mp4?token=U3X0tqQ1v93w8Hl2ruztWIPwnYvHJX2eaDcsJoJrCyRHp-M08CIAy22tU2-3Qy6GtrhgXrNmYIEK_pxuy7_eMRsv-6je81YxXN9-xhjkyG3i0oW8aCVg9nKwYcXoszYdUraAi3eAnS6AdAcVANCWe3Rd53TPGqq7pLIMfmZSb2yy14tkZbMQf_-qkN2c68vk-1Lx7d0oBTfplasMaJ9C3YKxE_ZdCadx-M-dx3v8hECvuaSi7Sx_YOsCs3RXvK4IEydTtM7VyBDzhODu3StbrNVCgVL55v0j-E8DUNbqXNvRGvEg6KvlJrR4VbskD_qK9YtJfg7ZyyoNoPkv9QOgSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a52181c7e.mp4?token=U3X0tqQ1v93w8Hl2ruztWIPwnYvHJX2eaDcsJoJrCyRHp-M08CIAy22tU2-3Qy6GtrhgXrNmYIEK_pxuy7_eMRsv-6je81YxXN9-xhjkyG3i0oW8aCVg9nKwYcXoszYdUraAi3eAnS6AdAcVANCWe3Rd53TPGqq7pLIMfmZSb2yy14tkZbMQf_-qkN2c68vk-1Lx7d0oBTfplasMaJ9C3YKxE_ZdCadx-M-dx3v8hECvuaSi7Sx_YOsCs3RXvK4IEydTtM7VyBDzhODu3StbrNVCgVL55v0j-E8DUNbqXNvRGvEg6KvlJrR4VbskD_qK9YtJfg7ZyyoNoPkv9QOgSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
صور الأقمار الصناعي تظهر أن هجمات انصار الله استهدفت قاعدة عسكرية تابعة لمرتزقة السعودية في الوديعة على بعد حوالي 23 كم من الحدود السعودية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88632" target="_blank">📅 14:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ذا أتلانتيك:
يحاول البيت الأبيض إبعاد الحرب الإيرانية عن عناوين الأخبار قبل انتخابات التجديد النصفي. مع استمرار الصراع، وارتفاع أسعار الغاز، وقلق الجمهوريين من خسارة الكونغرس، يتجه ترامب نحو فرض العقوبات والضغوط الاقتصادية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88631" target="_blank">📅 14:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88630">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
المعارضة الايرانية الكردية المسلحة الأرهابية
: الحكومة الإيرانية تواجه عقوبات اقتصادية قاسية.. لن يقتصر دورنا في هذه المرحلة على دور المراقب وسيتم اتخاذ خطوات عسكرية وأمنية وتنظيمية ودبلوماسية. استعدوا ميدانيا</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88630" target="_blank">📅 14:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88629">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47828875e.mp4?token=CaKFIiW6aMpTBHc1t8IjKakDK0c7jZtc69leJHiP97CICSSo0CImTw0ZRxQcvgwZm50b5V7IwUvY-0AdY7BqE8_yrizUFeC-1sUIRwoB31t_CJ1iEzRmc_ycW5jJnfG0MFa1D6Yro0b0cavC1CUOVRYdAFchLSWkuCMmWJXJQGhHf0G-7_63zoBNDDx3lEiUiqO_T3KEhhkIC5RFYiNZMHnwcbG3vujF8so2yeyeC0N3jqEabieRsPPOUhdAo4j1TvpV5jBU1Pvo562RXY5sXSEAuolpNY-kO_RRdO77p9To2s7hsTVMpW4j2zk-6eaLAwYfvGkIBgd5LGWgc8vvcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47828875e.mp4?token=CaKFIiW6aMpTBHc1t8IjKakDK0c7jZtc69leJHiP97CICSSo0CImTw0ZRxQcvgwZm50b5V7IwUvY-0AdY7BqE8_yrizUFeC-1sUIRwoB31t_CJ1iEzRmc_ycW5jJnfG0MFa1D6Yro0b0cavC1CUOVRYdAFchLSWkuCMmWJXJQGhHf0G-7_63zoBNDDx3lEiUiqO_T3KEhhkIC5RFYiNZMHnwcbG3vujF8so2yeyeC0N3jqEabieRsPPOUhdAo4j1TvpV5jBU1Pvo562RXY5sXSEAuolpNY-kO_RRdO77p9To2s7hsTVMpW4j2zk-6eaLAwYfvGkIBgd5LGWgc8vvcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
🇮🇷
وزير الخارجية الايراني عباس عراقجي يستقبل رئيس الوزراء القطري وزير الخارجية في العاصمة طهران.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88629" target="_blank">📅 14:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88628">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4981ae7d7.mp4?token=BkDCHRb8LStlXpZgnsQAUQf7X_FcMlNNt8Oylwb2zKdHmWYjf112lb-f5hnJzzYCyCuKXXsXhht7B8Yz899e06uQogicNtqI-hHs9ld96Qg4848i7vofBwkEWPZ0QjcpBOrjfSv6Pezao38d_yjkwV_D3Rp8TkgSfMQy5Z4Xikb4WDHtcyJfDM1iqWo8h6EF1JxpUw7DyeZLUa8keRFa8fvWKafBobfDvoekOHJ4s--q-c8tvx6rggAoabpAezygEUawH3Fjd3ZbEueZtHuXQTPzc6kNEgOqMFx83N4jfYKQcfhPG6jpT07WHAuUqejnS6vMDLK5HYcMoaeQdKGBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4981ae7d7.mp4?token=BkDCHRb8LStlXpZgnsQAUQf7X_FcMlNNt8Oylwb2zKdHmWYjf112lb-f5hnJzzYCyCuKXXsXhht7B8Yz899e06uQogicNtqI-hHs9ld96Qg4848i7vofBwkEWPZ0QjcpBOrjfSv6Pezao38d_yjkwV_D3Rp8TkgSfMQy5Z4Xikb4WDHtcyJfDM1iqWo8h6EF1JxpUw7DyeZLUa8keRFa8fvWKafBobfDvoekOHJ4s--q-c8tvx6rggAoabpAezygEUawH3Fjd3ZbEueZtHuXQTPzc6kNEgOqMFx83N4jfYKQcfhPG6jpT07WHAuUqejnS6vMDLK5HYcMoaeQdKGBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قوات أمنية كبيرة تتوجه نحو منطقة الدورة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88628" target="_blank">📅 13:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88623">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4Dt88kLFOhstavhQ7BRKi49tShkgNQVRvgOcVJI40RqQ9EVRNZyT4V2-m_i-iMokaUJBhRJFSMsTEFHOb0aEmoIoQPq9a1rqlaW1G8UKfWkKxrW1M5rDYJf0-rQejTAKbKXP-XMsKOWNhKOZ0gPCDc-G6EjSQ7rxxTDewEr6a5SsciSva5WDEex2zULFn1_xdt_igD8EmhSmeBzq0xkpqolZoERidKvX_Kr1bwngfRpvnBLwweqBcBIebm3zZuphKfapGpZGHQJqE3pRqHRzkhoGEvuu6RvsZvXXf27ZYzaIkuNao0hrdPfE5Oh_Q5kVMQ21j_aFhkntDmHxNECRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEUa3MJBCwII73D_yTEK2UuTuR2tJy5Nh30jWoggY8hSny7PFqQzCKMUO4gqqEJQCaZ0WEoTxNzpiYWmf9BXQTuxi2N5Rz40rqCIVYgcFc_vQY69zzVePiYtPq2-F-25EnOaoI1bPFcMh-WE2UumNOp3Mw86puUj1Vuie0PzpjfUfdrdJS7y4DZOo9Tfy21CqSVFlURY8OdNAFADjDGtdrdZ2e2y-Z-cObwf6ca2NnDdsZF2chYDonwEyCNuyiZetyzWhVq8h6Y3zXh1aJETpMYqJr2y5UpMCrzrSsfVMt5Px9JSj4InrmwLENFwWgqZyHrMVpzsKKmRgk3N3quh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBooEtt7I0z1Fb4nZdFfbqwLYfN9MeTIyCkUwhDoBVeIgV4fi1QGaOpPYbRiMeP4zTZbCVYS7Beg8P1meEZxjO5e7QrlY2l-huqAsEYwETuPAYzvnuOn7g_-HZiIHQWZl5E6F0pDNxQk-c6Ya8asEEynAJ3kiT6pajAlp6BfmeXym43xh8zmBKD_Csg81ZhV-OW2FNDxkkcAh0TjKkhUb7dHRuZVX2REXGiEqvrBwW-UldnRsTtFDZyTGmKT-Wa48-GEIs1c_BdUf3xfOokYSIykVt-0j_fv6rbEAM4LuJfInfm-K5Nfmn4YCc5Cgo99Jn6AAvDm24jRWOFSgsWZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaWwFHTtJJHD5fnu8KrZL3y82zSiJ4USfLcULFVizI0OvMu1zpRV2jQ0X65cJPq0sCuWemztvs5ifiJpzeFTXglvukZt8DNeRd9qQmkqiUTy3ksckaGyEQyO96aOomvXO5yLbtAjC3WeeUw-gqCOOfpnTvFPt-Fd80BQkyi73FfAWo52vcyjOrSQuHcY7551XwgXByeoUqnXshuDkVHjG5sKpK6tGwrznpr-EWABqaGwBCBsF_mnVT-rVmpwmRnQgJiOqKr1tu-582VDwRUSL73-hql0KeQUXpxjM2knu6WFzMOf5-v6RnkhjASt6pJ-meiW_cTBMg63ugUxFsDQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiEyKB6qyHRhArVRNYH7twS-rEqY8YR-RSbDOWZNro5V68Kvn29iA63drdhOC0nT8G_0k_CipfXjYcCrndB--WbUqy2y2l7l4R0vw_4PUcKrYUO07OX8lBo0ctizOt0zUa1VYwAMeTbwNoFCHhEanjQbcUgwJrAy14pD-x61occDcCfhRU1-iQAdnlepAOCH3VZy-sHrwe-WrAevVFXoXKLand-1VuoclQp4uqSQpWtVvdhwJIlreW1uVYu1c_4URqhQd9HfsbcPCxvukUqyL8eHkWWb85bnjs-wQxXGEwOeaeRQchJ28RwK6iOl0biMH5sB9jHrgD6FP-7xXm4QwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88623" target="_blank">📅 12:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88622">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:  استشهاد ضابط برتبة عميد وأحد منتسبي شرطة بغداد الكرخ وإصابة أربعة منتسبين آخرين من الشرطة الاتحادية ومغاوير شرطة بغداد الكرخ أثناء أدائهم واجبهم ضمن حملة إزالة التجاوزات في منطقة الدورة ببغداد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88622" target="_blank">📅 12:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88621">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88621" target="_blank">📅 12:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88620">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea96c0728.mp4?token=HSoK230r_-wyXeIXJwv2tRg7LBiUHmgG7-n9R7OePgSYGWa41gkErKM-C_Q8gl95af9JWGIfSN3mH499QBkw6vLENY6_cR-DVnfkKgupfkMlheRQ-0VrGVTacgs9__3r1i23V43C4ZGxdOth3V_QX53t1-McyescAvGyw61c5pSDm3Bmuch-a4gNtmwGK8Qhhap4QnZfuwTH5-wCZdemXLIsbUkH0U8Uz7Dn6l4AnSU-WF_frsAV0wg4y8Dh_QMxxe_Jgc1ZOVmvS9eZL5y0-06r5uUucS1NOLsaLZYT2UlIpBgRJUUx8GQPIXr3pNRhjiB-qt_jT7A98ESx86wxMXcGIDIgTJLoOgqpIMeHUuf_8tZ96nlbMLL658uPm8eFNxtTkXjeq-OI_M5ZAzx8IP32lKTXOARm4rlyWICuNEerZZyfFz9RdkJPZ726S37g16dv2fE5wVuyH_0fFdQGwbjSYABNWyuZhxrxLxfPJHmeb5RQcqUhDtQ9deeHLk6eHDKROcQo4W4tUVaw863nqWlYamY7bS2XW2Qbo04Rq0xP0R_uXNAsTsV0cs05wfD5Ze7-J2SF0KGc5j-prNSiQXPEviUcxxeiHqHfIVxPw-i1oihAVvuhMI5I3MjuGobZUrZMV70LfTnSBYBMd_1QYrwJ81tp2OoHBfpAjPZiy8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea96c0728.mp4?token=HSoK230r_-wyXeIXJwv2tRg7LBiUHmgG7-n9R7OePgSYGWa41gkErKM-C_Q8gl95af9JWGIfSN3mH499QBkw6vLENY6_cR-DVnfkKgupfkMlheRQ-0VrGVTacgs9__3r1i23V43C4ZGxdOth3V_QX53t1-McyescAvGyw61c5pSDm3Bmuch-a4gNtmwGK8Qhhap4QnZfuwTH5-wCZdemXLIsbUkH0U8Uz7Dn6l4AnSU-WF_frsAV0wg4y8Dh_QMxxe_Jgc1ZOVmvS9eZL5y0-06r5uUucS1NOLsaLZYT2UlIpBgRJUUx8GQPIXr3pNRhjiB-qt_jT7A98ESx86wxMXcGIDIgTJLoOgqpIMeHUuf_8tZ96nlbMLL658uPm8eFNxtTkXjeq-OI_M5ZAzx8IP32lKTXOARm4rlyWICuNEerZZyfFz9RdkJPZ726S37g16dv2fE5wVuyH_0fFdQGwbjSYABNWyuZhxrxLxfPJHmeb5RQcqUhDtQ9deeHLk6eHDKROcQo4W4tUVaw863nqWlYamY7bS2XW2Qbo04Rq0xP0R_uXNAsTsV0cs05wfD5Ze7-J2SF0KGc5j-prNSiQXPEviUcxxeiHqHfIVxPw-i1oihAVvuhMI5I3MjuGobZUrZMV70LfTnSBYBMd_1QYrwJ81tp2OoHBfpAjPZiy8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88620" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88619">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYloW-Fq_mbHejX9KhTMo3WUki-tVMb-Im1GG2NKoNP4mMVg3-f7X_bXfDlK3EdH0uQdrZEn27W_uKRjFSVSWpwXxaWllqZGArlWjbz0AUmutXNosa1zypJvgRm56fqIeF63rtfrF-kg4YgYkHoMNXwwIvRQCzfcj8vzgj7NOt78OV6pMg4fW5yg_t_HnOl5ld0ZtDUp0D__UxWLasNQGBPfVCuNKYWj1ZgItcsYrX_gPoXXMazneBTuRW56yNbSTEAZLUOK_KOflcjyZuixnv1HYO9holSQMbHTjzY1gWkXj3oNsJt6VhZGcpewi9hjH8fKD2suMwms5JkwNTBiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88619" target="_blank">📅 12:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88618">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇷🇺
الخارجية الروسية:
قد تتضمن ردود روسيا على الهجمات الأوكرانية باستخدام الأسلحة البريطانية استهداف المنشآت العسكرية البريطانية - سواء داخل أوكرانيا أو خارج حدودها.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88618" target="_blank">📅 12:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88617">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
تحديات عديدة تواجهنا. نحن نطور إجراءات القتال في جميع الجبهات، من إيران إلى لبنان وحتى غزة، ونحن في حالة تأهب عالية في مواجهة التهديدات المتعددة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88617" target="_blank">📅 12:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ea710ed1.mp4?token=bDRvICHbk86xVgIS4xMoQ9yzpo7xaaayAtaVtIfRR4Rh_17Nmm0663VCSBFINfUIuIuVtaJI5UZk8WhCs_hxtqxdW06Fep3oIrMgZby4fayzHm_jPWpcOFMPWdSEiNsJara2P_eIYqFm9PtrXDb_8N_cXwRO5lIhdXHUBNelJdKJHBjMxyvgXeojCpOUdDPUjzoSIG4owsg7HNNqvMHn3ERWrS0WrisYt9lNKbYHqjmKgOIRtLIbJdAi4_dQYY2Rsicb7ELOpkZrHkZLEf12ajqbdncAcQfIpISQNl1sxOykurDwYJ1Y4dO-POuatKvGNmGhyj4GAKTS1rtroZpS5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ea710ed1.mp4?token=bDRvICHbk86xVgIS4xMoQ9yzpo7xaaayAtaVtIfRR4Rh_17Nmm0663VCSBFINfUIuIuVtaJI5UZk8WhCs_hxtqxdW06Fep3oIrMgZby4fayzHm_jPWpcOFMPWdSEiNsJara2P_eIYqFm9PtrXDb_8N_cXwRO5lIhdXHUBNelJdKJHBjMxyvgXeojCpOUdDPUjzoSIG4owsg7HNNqvMHn3ERWrS0WrisYt9lNKbYHqjmKgOIRtLIbJdAi4_dQYY2Rsicb7ELOpkZrHkZLEf12ajqbdncAcQfIpISQNl1sxOykurDwYJ1Y4dO-POuatKvGNmGhyj4GAKTS1rtroZpS5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجمات روسية مستمرة بالطائرات الإنتحارية وإنفجارات كبيرة تهز مناطق في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88616" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88615">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
لا حقيقة لانسحاب قطعات الجيش من منطقة الدوز.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88615" target="_blank">📅 11:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر   هجوم على سفينة قبالة سواحل عمان منطقة خصب بطائرة مسيرة …</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88614" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88613">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
رئيس خلية الإعلام الأمني:
نرصد جميع من يقومون بخطاب الكراهية ونحاسبه وفق القانون.
الحكومة تتجه بخطوات ثابتة لتنظيم السلاح مع الفصائل بالحوار.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88613" target="_blank">📅 11:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88612">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي بالطائرات المسيرة الإنقضاضية يستهدف مصانع أوكرانية في العاصمة كييف والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88612" target="_blank">📅 11:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88611">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
إنقطاع الكهرباء عن منطقة الضجيج في الكويت لأسباب مجهولة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88611" target="_blank">📅 10:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88608">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KW3ZDnIvKqwZRSYjcOMpDfCIjA0oXat885PpxbvYz2WlPPg8l0Rekr9tKw38rgtnkMHIuR-66MBdmFmbvaRIG1g4KxsCYiFlFzfZ1K-GD9DdY06eWMfmr-wZc3j08ygE9Qvu4hkK8SKbCvKCMydN0d6zwGDjsGD29rZgMSKBFSIBjpPTno--F0QC557ibg_wmVNe-oIYXVgfsvGeMsSXokGmwnBi5q857PtUJtXZVpBv1tNyjaCEuOaYDtUupMU6Egq45SX0ZLyPfntJUBcbRopAkeKK8nzj75EdHoPrvLMFGK-U3Mx40K9R2nGJmMsITCfyuUcyoRPM_4Aq99CHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HabX3fhcxxMy1NMG_XoFvEab5SKZqb5gOj7xK-s5LZDdQRzYrnESTtgrCY7AVLJGgI-LbOSqycAq4A2_cwZ-nkuillH6paL0ozgaNAJ1DFAbYE4FWAx1nNNK7RXq7-eHuK_uU9sT6Huts0Ke9Daq2nNnhg5NtjJNi8WyZxO7ssVRK1qtUW7rpBH5g7mh7FpNbCTc-hft8RaDrGKiSm9E7ACItF_nlhX2Z6sDuljDS4VSGBH1exfZqkwbO3OxyS_HI44C5ngUInW3ArQ6pAe_cWP4gBL2XbaImx6phCXZkiOVRhJK7wshIODshXhG3kZC0C3CGiF1R-fSAtV5tuNNxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVD8U4LC_j8E3qJVOOEnb2Q2JO4FISwsApY6YNiMdSm8ndwN-PbYYJPfym5RIxtaLTTWx87tMCRsj9X6Y2ynnDceLOojC9LC6zl2sQDokdcbH5VfYK5pZIEwygF0ueDh98R_0jRtFWrv9pYBxyHpEOdV-6kVqXlmw7cRBDVwLMU4Nhfh7ZfWz88zRcLo1EY-xhDhkuWkv8qayUi8_7WED5UXyGQBcw90vWn2QIpglgSGgtDggLASRQYxvgRnp5WsedXDHHTx5geJM6mWRaMwlf5Uj6lRvYcJC-_HcPt-LbR1ahc-RwGHylv15Ee5ZJD5oNqx2qCnm2VNah9r6YRD4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد تظهر تجمع السفن وتوقفها بالقرب من مضيق هرمز بإنتظار القرار الإيراني لعبورها.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88608" target="_blank">📅 09:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88607">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇷🇺
🇩🇪
دير شبيغل الألمانية
:
‏يُعتبر حزب البديل من أجل ألمانيا، بقيادة المرشح أولريش سيغموند، حزباً موالياً لروسيا بشكل خاص. وفي حال وصوله إلى منصب رئيس الوزراء، قد يتمكن بوتين من الوصول إلى معلومات حساسة للغاية عن الدولة. وهناك بالفعل مؤشرات أولية على ذلك.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88607" target="_blank">📅 09:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88606">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇰🇵
‏
كوريا الديمقراطية:
العداء الأميركي المستمر تجاهنا بات واضحا.
سنرد بسرعة وحسم على الأفعال العدائية.
ندين خطوة الولايات المتحدة لتزويد كوريا الجنوبية بالأسلحة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88606" target="_blank">📅 08:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88605">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي بالطائرات المسيرة الإنقضاضية يستهدف مصانع أوكرانية في العاصمة كييف والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88605" target="_blank">📅 08:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88604">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر
هجوم على سفينة قبالة سواحل عمان منطقة خصب بطائرة مسيرة …</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88604" target="_blank">📅 04:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
🌟
لقطات جديدة من حرب رمضان تُظهر لحظة الإغارة على جسر B1 في كاراج الإيرانية من قبل الطيران الصهيوأميركي.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88603" target="_blank">📅 02:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f0f8deda.mp4?token=M4an8VW3KWNzV35xs1CatqRxBcHoisTOsssDT7Mk83AHwZAZIb4PcERA637TSgjPHj4Cb8tJaa73lUi2zSILduYG-abtWZakxycQqQJdVINeWNgcXSzWN3uM1v1dVa0cHD01ztEkctBe8kgIc2tWC07pXGAR3Eh5msNhDdj_d54-YVhPvR4Zb58sW0-_t5R4KOuIMie81dCkkwiVlzRGV-43DSB_PJlaIfb07IYGijlfYjF7CMUkzonidmFfi6TDKOCw5pQAyMPSy2BuYVM-yoJuVf_DDAOZA28GcVR0KOGv5bUUtK3IZBdFlPegJb3J4c1QlcysxyrGADJOiMvEOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f0f8deda.mp4?token=M4an8VW3KWNzV35xs1CatqRxBcHoisTOsssDT7Mk83AHwZAZIb4PcERA637TSgjPHj4Cb8tJaa73lUi2zSILduYG-abtWZakxycQqQJdVINeWNgcXSzWN3uM1v1dVa0cHD01ztEkctBe8kgIc2tWC07pXGAR3Eh5msNhDdj_d54-YVhPvR4Zb58sW0-_t5R4KOuIMie81dCkkwiVlzRGV-43DSB_PJlaIfb07IYGijlfYjF7CMUkzonidmFfi6TDKOCw5pQAyMPSy2BuYVM-yoJuVf_DDAOZA28GcVR0KOGv5bUUtK3IZBdFlPegJb3J4c1QlcysxyrGADJOiMvEOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
توثيق أخر يظهر لحظة إسقاط الطائرة المعادية في سماء محافظة إب اليمنية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88602" target="_blank">📅 00:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88600">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e7b3f02f.mp4?token=TSZKAgJ-v7s12WwNi4wUtvN0IajCFXagdGvauIk0DzOja-7klwJZMRN5BWVBOdP58StoIAB4NZ5pZehoszyrosFjZ5gUuXt9MS3VD8UA2x-e0Rab2RlxMiq11LeOHYHXkb04iL_D1FuxBVMuKWdj9hd6CsrYqWDUD7eFoBKI7mxmJWagl8Gi9fgF8xNB3ra4C1j5L6QBx53A2VkI5l3JdY_Hc8RtSU98SOo1NGHUpQURCOvkenVc7PsuG8DgUX-GjJ3QxdpmLtfD_cKrLD-f27HD2X5gWr8a7jYQD3Y8Q0ssromuFRH_LVhhmwcMvqCmicW7pVHInWqjphHKg07fFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e7b3f02f.mp4?token=TSZKAgJ-v7s12WwNi4wUtvN0IajCFXagdGvauIk0DzOja-7klwJZMRN5BWVBOdP58StoIAB4NZ5pZehoszyrosFjZ5gUuXt9MS3VD8UA2x-e0Rab2RlxMiq11LeOHYHXkb04iL_D1FuxBVMuKWdj9hd6CsrYqWDUD7eFoBKI7mxmJWagl8Gi9fgF8xNB3ra4C1j5L6QBx53A2VkI5l3JdY_Hc8RtSU98SOo1NGHUpQURCOvkenVc7PsuG8DgUX-GjJ3QxdpmLtfD_cKrLD-f27HD2X5gWr8a7jYQD3Y8Q0ssromuFRH_LVhhmwcMvqCmicW7pVHInWqjphHKg07fFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من إسقاط طائرة تجسسية معادية في أجواء مدينة إب اليمنية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88600" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88599">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
طيران حربي كثيف يحلق فوق محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88599" target="_blank">📅 00:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88597">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6627f1fd9.mp4?token=VwvPV5PNTbfQLCcMWmWzdGYfAYF0hsNNxCfac7CJVuwCtq2kNFhp4bl3vMJI3C3exLec3grEs7qboqjtVIdfuzt1vUwppG_j5uiDzWZmgINlrU5WXsIjDPmna4P_OAz0aBIRq9IvpxHTc3Xk6m9TcMWIRZeH4vNIrq1s6z5gdXdRDrS2bZNIbqM06Xs7W6K6DiKactk-3fHu9kEuuO2JPGJXB5Ex81bIaCkwPFXsXFaRpZOXj3_gWYcuqeuS88zAWn90e_lq0Vxat55uYyzF1uRwppgKP9nSImj0d8XcwjkQv04zwDBY9bMH72EkafhYv_VcGwn_u6oxnr6UFU88yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6627f1fd9.mp4?token=VwvPV5PNTbfQLCcMWmWzdGYfAYF0hsNNxCfac7CJVuwCtq2kNFhp4bl3vMJI3C3exLec3grEs7qboqjtVIdfuzt1vUwppG_j5uiDzWZmgINlrU5WXsIjDPmna4P_OAz0aBIRq9IvpxHTc3Xk6m9TcMWIRZeH4vNIrq1s6z5gdXdRDrS2bZNIbqM06Xs7W6K6DiKactk-3fHu9kEuuO2JPGJXB5Ex81bIaCkwPFXsXFaRpZOXj3_gWYcuqeuS88zAWn90e_lq0Vxat55uYyzF1uRwppgKP9nSImj0d8XcwjkQv04zwDBY9bMH72EkafhYv_VcGwn_u6oxnr6UFU88yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به مقرهای تروریست های تجزیه طلب در اربیل عراق.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88597" target="_blank">📅 00:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88596">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed70602e4e.mp4?token=XkGBuKuUZ6CLpSRe6QAxfksmKvQq5a8NREhIkod_jpgLODROgM_r9l16U-w4uFX6ThGB5bGGvyZQhXCaFKTyCUfg4whbWZueqQZ4VkijsMjbVVtDIbFRpf5nZX4tFNEdlJ6qXSrcg52JjpCnn9N1ZtMgAYAwLWhpWN-e3MCnTr8ejj2jvdnRNBVIxxCa787IQidwQU7geffrncNm7GJRck0-EcfRHxsp5WbWKXVhiHkbtdVvCvgg1wjA65XdyryzeEtYtcwN0Vj_NUuF79Pps_OOzBU0SXZXaM5wvtWSbRBxHpO6lbRGrLnNeNfJy47VA14lbpO9imJyIo5XwQex_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed70602e4e.mp4?token=XkGBuKuUZ6CLpSRe6QAxfksmKvQq5a8NREhIkod_jpgLODROgM_r9l16U-w4uFX6ThGB5bGGvyZQhXCaFKTyCUfg4whbWZueqQZ4VkijsMjbVVtDIbFRpf5nZX4tFNEdlJ6qXSrcg52JjpCnn9N1ZtMgAYAwLWhpWN-e3MCnTr8ejj2jvdnRNBVIxxCa787IQidwQU7geffrncNm7GJRck0-EcfRHxsp5WbWKXVhiHkbtdVvCvgg1wjA65XdyryzeEtYtcwN0Vj_NUuF79Pps_OOzBU0SXZXaM5wvtWSbRBxHpO6lbRGrLnNeNfJy47VA14lbpO9imJyIo5XwQex_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به مقرهای تروریست های تجزیه طلب در اربیل عراق.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88596" target="_blank">📅 00:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88595">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d599cf5e06.mp4?token=h-GCekh5fDfChQOVKodWAOXrPXFiDkHswq6-BZQ1j7-l_y7hQ61gCdLTtFZm-ziMHbWmdBPRwPMRLK9i-zY5yUVuD_wK3DVMkazWBwJ-sECe0zy3UDJsGeKvz3YMoh8parHOhfcbbaL4pdHYbZtqS2ZrIfWOx7EN4SQXREEKgrfzrSKXGMDuw9hRPXN8dKoyeUGSIXgUBFMeWtw-swsA9Vd6NdQ0gZHKq4u0JBm3A_hdZ-ZY5qxr3b6wtGsjBIM7oyAZcSnqGCw-Thc_o1_K2xvC-9NVaxBY7m8_ryBZb4kkJcWR-dWW0yDa5BfDsoPfG4OlKEaPj6AnAJsxu8mjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d599cf5e06.mp4?token=h-GCekh5fDfChQOVKodWAOXrPXFiDkHswq6-BZQ1j7-l_y7hQ61gCdLTtFZm-ziMHbWmdBPRwPMRLK9i-zY5yUVuD_wK3DVMkazWBwJ-sECe0zy3UDJsGeKvz3YMoh8parHOhfcbbaL4pdHYbZtqS2ZrIfWOx7EN4SQXREEKgrfzrSKXGMDuw9hRPXN8dKoyeUGSIXgUBFMeWtw-swsA9Vd6NdQ0gZHKq4u0JBm3A_hdZ-ZY5qxr3b6wtGsjBIM7oyAZcSnqGCw-Thc_o1_K2xvC-9NVaxBY7m8_ryBZb4kkJcWR-dWW0yDa5BfDsoPfG4OlKEaPj6AnAJsxu8mjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقرات الكوملة واليجاك في قضاء سوران بمحافظة أربيل تتعرض لهجوم بالطيران المسير الإنتحاري والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88595" target="_blank">📅 00:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88594">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f044086b32.mp4?token=o3MfYBJPCNGKIyjVhVW0-K7v7sX2_SsHnvyLltLYlnT6IZvgkiUaSOdL5BboOJw7yKoBli_mOW9Mren0KXchToTetTRbq0YdjpTIln39zoiSQLFxNZAtIB35DnkEVGCElNf-jZu-eNl_ywOHNj68WKXNJ3EcKckWwTx53Hw9ckEyHx9GU6-X79z1fnFUTkREmUeXOL7kZ8115OGeK9zRIelY4fOLk3bEmEyymLsyt9UCl2rPNpWQBb04w2M50heRzAyQXR8UiRBeO-kuvtfl2Rg2TGGB20excHOmOWz5deu0jkptyY7Ogwy42xnAcpinXyDj7E17rekE19FNxjPFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f044086b32.mp4?token=o3MfYBJPCNGKIyjVhVW0-K7v7sX2_SsHnvyLltLYlnT6IZvgkiUaSOdL5BboOJw7yKoBli_mOW9Mren0KXchToTetTRbq0YdjpTIln39zoiSQLFxNZAtIB35DnkEVGCElNf-jZu-eNl_ywOHNj68WKXNJ3EcKckWwTx53Hw9ckEyHx9GU6-X79z1fnFUTkREmUeXOL7kZ8115OGeK9zRIelY4fOLk3bEmEyymLsyt9UCl2rPNpWQBb04w2M50heRzAyQXR8UiRBeO-kuvtfl2Rg2TGGB20excHOmOWz5deu0jkptyY7Ogwy42xnAcpinXyDj7E17rekE19FNxjPFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطيران المسير الإنتحاري يطال مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88594" target="_blank">📅 00:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88593">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJT9Gg9Ro99gf_xgu154Fx68DR_iAFGkir_4O5W1T_fssrgyGd36GuBTI2p8-m-GBtUoxg-NF6xytpnUOQC-UnxIubYNFC8xSTPbdYIMN2-Gn0ADRcLg417F0Whc2h1_zPtAtCNWlYdYE4pCnzA1piaDfyAr1Wckz-1m9d3R9DgyLQRsG2i57u0-4O9o4Q1eWJz3HeMKCM6gNED4XmMiZSwnsyhZ8nGIa4vbKnhQMOqX0iWGfaXLIpJjZ0-s3TXYhoo4iPRnzQkCyt3QWuLSXWNjGG-z6zdiXOjzSEfOQLjZVDuGQjg5rLMikMSoE0NuDSz4sLdpm81chJsNIOaCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد النيران واعمدة الدخان من مقرات الإنفصاليين في محافظة أربيل جراء استهدافهم بالطيران المسير الإنتحاري</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88593" target="_blank">📅 00:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88592">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eff45189c.mp4?token=Gxukr9IxT-MCyMBmoYg6CwxChUTff2om1KeFeV9zXENbyhJNeP25YrlfJ7RoXAzeSUf8w0_UWtRN_CDgsDnoUc9yQmIfXqE148gR5ioYHenNleV16GY6BSUh-gxVAq-IO0A1NFnfgdLT4zd9KVDcK1ZM2WN4iWisuJcSpy4CqNhmt66yo3nJ9tjpg43_HUiFGbn49H7VKgmTLxyPeATe7Bp97EzIfHQ8Y1_IW8G5d_n6cFg_Z8MepmYPrqKyp1BPowCKGsD4vzaQA-5y_2skQd7JI1ZqDOVhVVUdRwYSzU1nTTGddCkOf3kpQT_-ax6c-k2fe7IiNusfbLMnm6cMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eff45189c.mp4?token=Gxukr9IxT-MCyMBmoYg6CwxChUTff2om1KeFeV9zXENbyhJNeP25YrlfJ7RoXAzeSUf8w0_UWtRN_CDgsDnoUc9yQmIfXqE148gR5ioYHenNleV16GY6BSUh-gxVAq-IO0A1NFnfgdLT4zd9KVDcK1ZM2WN4iWisuJcSpy4CqNhmt66yo3nJ9tjpg43_HUiFGbn49H7VKgmTLxyPeATe7Bp97EzIfHQ8Y1_IW8G5d_n6cFg_Z8MepmYPrqKyp1BPowCKGsD4vzaQA-5y_2skQd7JI1ZqDOVhVVUdRwYSzU1nTTGddCkOf3kpQT_-ax6c-k2fe7IiNusfbLMnm6cMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
دوي إنفجار عنيف في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88592" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88591">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tftL43Q1fcjFt2i0NhA080RGy4lFQQ73Rs3MqYfkjF2q5BdYnW5bufwwka4hH6leDXkEZKPSKM5CQp2ylycLwiIqM_ZBLePfCd7NHu0mGip0ChcsI3txCvzAjE5H6Wq0olt8vmuFDyuvk7sgQW7tX8Ao0-Kh-jDbo6SLbaAp_V0-rzQ7UWlJARw-2cba58gy-VmtLgBhPeNc9qFzD5eFhR1i62VvuDbWXg9KNAOQAyrCuLh4VcACbDcplknD6Ju1BtUpCt4QKPQVxnr2Kmr9cU20k8XN96aIn2oK5AUGMhDYWGy88OuEZ0EX_ZqFoVh4qnztNbwsbknCY3VtTTxfIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
دوي إنفجار عنيف في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88591" target="_blank">📅 00:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88590">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
الاستهدافات طالت ميناء المخا وبعض المواقع التي تتخذها المليشيات الموالية للسعودية ملاذا لهم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88590" target="_blank">📅 23:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc95e1665a.mp4?token=jEL44yDJrYieErtnKZjl_WNSfzQ7MEPQX6_0x4C3Fdn167g30jdnMwTVeGS8gxlwgVPBmH1wNjv4kOfZ1EdXhejWwdZ8uE5-TKfpifu3cTMWtPctpa2i59zIm8ng3g8M5opJHX9cdQmrWyjDG-rEb-d8Itu67SPIU5-0qwi6Lby1K7IY5Nq-6lwGsUsz9aYrsiYl8KD9-eilIdRh9-fxnk8KoAqj3tRevkwOd3rLprjLS53yMgrbdDwbAgr29eLPZ1beYFNOxp2HnCtSYYMXjOsAwzHFCA4U3wYKtvWuAtPPW2fbXQ6vfUJldOeqXofArXzq55pFTAva4pdj0PO3WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc95e1665a.mp4?token=jEL44yDJrYieErtnKZjl_WNSfzQ7MEPQX6_0x4C3Fdn167g30jdnMwTVeGS8gxlwgVPBmH1wNjv4kOfZ1EdXhejWwdZ8uE5-TKfpifu3cTMWtPctpa2i59zIm8ng3g8M5opJHX9cdQmrWyjDG-rEb-d8Itu67SPIU5-0qwi6Lby1K7IY5Nq-6lwGsUsz9aYrsiYl8KD9-eilIdRh9-fxnk8KoAqj3tRevkwOd3rLprjLS53yMgrbdDwbAgr29eLPZ1beYFNOxp2HnCtSYYMXjOsAwzHFCA4U3wYKtvWuAtPPW2fbXQ6vfUJldOeqXofArXzq55pFTAva4pdj0PO3WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
صواريخ انصار الله تستهدف المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88588" target="_blank">📅 23:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
صواريخ انصار الله تستهدف المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88587" target="_blank">📅 23:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
الاستخارة تقترح بابتعاد العامري و تجلب حظوظ للفريجي العائد بقوة والمبعد قصرًا من اخوة يوسف ، اخوة يوسف يلوحون بالاستقالة بعد عودة الفريجي من سرير الموت..الأخير أسم عابر لحزبه وصاحب علاقات إقليمية ومحلية تجعل اسمه ناقوس خطر على الجميع .. من جهة اخرى أربعة وكالات استخباراتية استلموا منصبهم في فترة الشمري سيتم تغيرهم ..</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88586" target="_blank">📅 23:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7f179854.mp4?token=RnyFY_5X2TOhf3jaV2xUnqEoNPyljdOC8BSgzPq2r5ZVGKJamEprrO3CwWMW53Txkj7vPpDBSXdvmg-xELwvz3AXHbbgzy2YitCrbG0F19kCCTGAlm-9Jk3MoG36qXtSMGn6gt1ZJCk8O9ZpaJVUnFzN5gQ2nEt4rOYgDI4tQ1Lk7kcajDpUgelvmx3vZ81DwN1YV2vkbqneyFbIM4D4JZchMNp9f1kzC9-VrxZBHXHyJCO3U2_UiqXqfrXt7B67O5iEhK7XI6kBC34xmgouhWeDku-aOBMT6yyAZDMzAx5NqfY3nSbxQ92cQKOM19kT_c4ct9R1AOcQHQaByYCTv1B9xpA7IdSPCeHyeseHCO9qHR1g8OzbSnxw93SxpdavyKEpdSkFbVRUi1II2x4ucpCa8cKgxkVQBfomSVPh2OjDVtBze17Cp4paw0uXQskDWJgH28oUFuew6KssCEPV6LqJRGp5eJTWL-tVKy6W1QmRUf1UPPIoFsAoGWEep-om8dRk_SDxBexIB5_rAYIRESvX_2Y97kAMFEL2X3TAphxp1naE6rWGhArZnZhSsrfm8qayfM63t5LMUCtUA1snjFmHw-3VzfkowvPz87MWtpMovbtEk5cAodyGU7EwnD_Sf-dkRjzWXF0Jx_Eu9D379aZ6HKCMqnKrzcaq8EtMbdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7f179854.mp4?token=RnyFY_5X2TOhf3jaV2xUnqEoNPyljdOC8BSgzPq2r5ZVGKJamEprrO3CwWMW53Txkj7vPpDBSXdvmg-xELwvz3AXHbbgzy2YitCrbG0F19kCCTGAlm-9Jk3MoG36qXtSMGn6gt1ZJCk8O9ZpaJVUnFzN5gQ2nEt4rOYgDI4tQ1Lk7kcajDpUgelvmx3vZ81DwN1YV2vkbqneyFbIM4D4JZchMNp9f1kzC9-VrxZBHXHyJCO3U2_UiqXqfrXt7B67O5iEhK7XI6kBC34xmgouhWeDku-aOBMT6yyAZDMzAx5NqfY3nSbxQ92cQKOM19kT_c4ct9R1AOcQHQaByYCTv1B9xpA7IdSPCeHyeseHCO9qHR1g8OzbSnxw93SxpdavyKEpdSkFbVRUi1II2x4ucpCa8cKgxkVQBfomSVPh2OjDVtBze17Cp4paw0uXQskDWJgH28oUFuew6KssCEPV6LqJRGp5eJTWL-tVKy6W1QmRUf1UPPIoFsAoGWEep-om8dRk_SDxBexIB5_rAYIRESvX_2Y97kAMFEL2X3TAphxp1naE6rWGhArZnZhSsrfm8qayfM63t5LMUCtUA1snjFmHw-3VzfkowvPz87MWtpMovbtEk5cAodyGU7EwnD_Sf-dkRjzWXF0Jx_Eu9D379aZ6HKCMqnKrzcaq8EtMbdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
" السالفة المحد يكدرلها الكتائب تسويها"
قليلة التداول جانب من اشتباكات ابناء العراق الغيارى من مسافة صفر في احد قواطع المسوولية للدفاع عن الوطن والأرض ..</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88585" target="_blank">📅 22:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmQq64UFPu5S_2DZ6C7clVdbgTav4gxIkSv1kFWHfcQom6B0nUinfHMh5g-pGdSiR0Keni-Ret8HQ3gm1KDnTYYJMfFIX9yuNHzn0xAy6_Sebr_JNlY0vXlWuYx8a3K1p0P_dh5Cv6tRdwDH862HqXpo-lojiinKAlscCV9SdJp5KpYzFVahxLlruFwhU8u1eow7qGjtdD6zKcYw0OkK7Jx4VgeDBhSbKcMwe-h970hJR0bxY_eric9U7sQgIxpA2wn1XlREFyjZfGcsKmI6z1Fnna0F8riLWja5cm3-EDH7ht_vsvgrNeuCe3iL37Bi5413jGTN817iAA34GJUAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية بقائي:
أرسلت أمريكا حاملة الطائرات الأمريكية "يو إس إس أبراهام لينكولن" إلى المنطقة لبسط نفوذها.
بعد شهور من الحرب - وأكثر من 200 يوم دون توقف في أي ميناء - تتجه الآن إلى تايلاند لراحة واستجمام الطاقم.
المهمة: مشروع القوة.
المهمة الحالية: مشروع العطلة.
"أنا متعب يا رئيس."</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88584" target="_blank">📅 22:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
اليوم، نُحيي ذكرى الأبطال الأمريكيين الثلاثة عشر الشجعان الذين قُتلوا بشكل مأساوي قبل خمس سنوات على يد إرهابيين جهاديين أشرار في كابول، أفغانستان. كانت هذه الكارثة نتيجة انسحاب جو بايدن الفاشل تمامًا من البلاد، والذي ترك جنودنا البواسل عُزّلًا، وسمح لحركة طالبان بإطلاق سراح آلاف الإرهابيين والمجرمين المتعطشين للدماء المحتجزين في سجن باغرام. كانت هذه واحدة من أبشع الفظائع في تاريخ أمتنا، ولن ننسى أبدًا أنها كانت نتيجة عدم كفاءة جو بايدن والديمقراطيين الذين كانوا في السلطة."
‏خلال حملتي الانتخابية لعام ٢٠٢٤، التقيتُ بعائلات ضحايا حادثة بوابة آبي، وهم أناس رائعون ووطنيون عظام، تجاهلهم الحزب الديمقراطي تمامًا ولم يحترمهم. وعدتهم بتحقيق العدالة عند عودتي إلى البيت الأبيض، وقد فعلنا! ألقينا القبض سريعًا على العقل المدبر الشرير المسؤول عن مقتل جنودنا، وكان ذلك من أعظم شرف لي كقائد أعلى للقوات المسلحة. بارك الله أمريكا، وبارك الله عائلات ضحايا حادثة بوابة آبي. لن ننساكم أبدًا! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88583" target="_blank">📅 22:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رويترز
: يبدو أن إيران وعمان تتجهان نحو ممر ملاحي مؤقت بعد ما يقرب من ستة أشهر من الحصار. وفي الوقت نفسه، تظهر واشنطن علاماتها المؤقتة على وقف التصعيد، وتعيد الموظفين الدبلوماسيين بهدوء إلى السفارات في جميع أنحاء الشرق الأوسط.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88582" target="_blank">📅 22:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRA0y3e0ws4ZhTKhHqZgnvkycHSIvCkyRzp5fQwyDffAZVKMvgvrsvs0tYWwRAvtsUrhhOFSnLG1nbghd6d-Ynu53RC8CeRskeJQh4n1b3IBOwlskwxaUx_O0UnwHcfwc_nomVaS8Tb02guMbblFj_w1Vy6cAEjKNq_oeyJ2Qo4OW9TgN7dbmIOOzhOP6LuVGX6oGZTXAPEt1_vXHcrznF82VmGL2KGAAuorSwP5AxZXD_tJPO0aOjY6AMMytqxJ6dxYxTBubAz3VBS6BRV-v06HbtKBJbcWAELOuJ10ngFiLklfWtZpi19Z5G5OwcqQoFo9BVAfOlfwkM3sSBqzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
قاليباف
: نرحب بالبيان المبدئي للصين الذي يرفض العقوبات غير القانونية المفروضة على إيران.
تقوم الشراكة الاستراتيجية الشاملة بين إيران والصين على الاحترام المتبادل، والتعاون المثمر للطرفين، والرؤية المشتركة لعالم متعدد الأقطاب. هذه العلاقة لا تحتاج إلى موافقة أحد.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88581" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
القائد العام وجه بتشكيل لجنة لتحديد شكل العلاقة مع التحالف الدولي بعد انسحابه، عملية انسحاب قوات التحالف تسير بوتيرة متسارعة وفقاً للجداول الزمنية المرسومة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88580" target="_blank">📅 21:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3nZhyLDWrTekI0uz76k0M31ftVMvwpi2uQYRGYcWJogk3AtO7Sdo7l4XoL3RNr3VPp6InMihLjRP8Ozo-l_NmUErLjhZc5hgecrpLOJZsSt57AP9OOjtG2lvg9cjIJs1UKUOAUcGzgS8JPFExqW35CxGSxGV_s4vZSEUPV-6oLDmYxpjquLRRyZm72BVL6ApnDz8_eoQAtz3f0cou-h8C9-fjs4PNHaz4NdFWTuwVZ9QCN94GCNf9-0PfsHgCFfYZlKQG1qFCWis9sN8o8xrbEeE5Q05hLAfllSP-wTBrMmwyPRZmImVoAsjvThzaJA8DWWEhL22IfOXfMrI654hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء يلغي الأمر الولائي الخاص بشركة كورك ويُبقي قرار هيأة الإعلام والاتصالات بإيقاف العمل مع الشركة قائماً.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88579" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
‏
وزير الطاقة الأميركي:
رغبتنا قوية في إنهاء البرنامج النووي الإيراني عبر المفاوضات.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88578" target="_blank">📅 20:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88577">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIyYgTYlG6YXbsbM-8dy0ObOLM9QXrvW6j_amnYI0IjqYuEi6VRRaUy3zOVOBA5e8uB6L0Q8IdnBM04hfU2CFyOZpR2OcDjtPA0zi6jg9cGKGSlDB1My47hrfOTctTn3rfWfk59HC0AY6C-HX4rAK2pbCp0s0ENwi3PandV6Kyic-CvgZ5oiFhCziBrVcNyf_pTFndl-Oxp4_WFUNOFNd_xRVnINoAtuQurcFYPIIrj0es-HxNCTYiC__ClnJLksQVAY1iqMJeN8Nn2b3Jo5V0vnOj4zwo86wW27WxzCY4sqtt6-PwtxTLfoyhs_Fm_sxQ1LUhNRWSWgNFDEf6dZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: اكتملت المهمة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88577" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
🏴‍☠️
إعلام أمريكي : ‏بوتين يسعى لتصعيد الحرب في أوكرانيا بعد وصول المحادثات إلى طريق مسدود .</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88576" target="_blank">📅 19:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVXp-wsMl-pJzLzvDuQbrfAPG7qOlvibaHmIXMC38ZSnOiUs-OW5TfmIOz1FDz-z9UyKlrKt5RKiO053ktJzDqSJVdF9ZsadBA0NxTXcPQavzSMD1phL4UN5c-kHTgAC8-zl4PDeo-ceuxwWHiVXHUBpw1TzWFhqhjxWTmXauSN1XiWh1BSouMrYJghn16IcMrj4ZYe0mcG0ADkbJo6xAPnyJK17LG6PKabaslDMcMKqxZLKgQJ_s7yw9usSZiCJBI9iMeuSazRym_pvkLgAN1Rjzh8Sl5s8K2yiyJAszxpaH8ewk6LpXJzqA2c0i802KnbtwTcctbF8ngIbbUzeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
سفينة نفطية هندية باسم "HAANA" كانت تنوي العبور عبر المسار الجنوبي لمضيق هرمز المعروف باسم "الممر العماني"، ولكنها تراجعت بعد تلقي تحذير من حرس الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88575" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
وكالة الطاقة الذرية الايرانية:
‏إيران لا تزال في حالة حرب، ولم يتم تأمين مواقعها النووية للتفتيش.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88574" target="_blank">📅 18:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88573">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCKl9VZsjfFQRV28y6YnCtpXz3G6CZtJPav_LYS6V4-88T0BRcDRzs6XhKxFbxV_-fx1BTT85ZsJPgRVzAmPC9VVBIcF1myqqruKAztAfjnbZm9MFujvXHc-sjLr5r8_ykX2jNU-x1GqES8vkyoaxCr86JOAMSiNiSMlZSxhS4gRdW-VGlgJ858fC_15NXw2xe_2OIMdKV958cSj4U9XuuXXie6F6mP6SOFGApEhPYi5Zk3qUMEJroUzAC8nOCKWoe4NQR4bWp7ueKr7UTk4MzoYcahK91TV8_MBq2vcLIYLZpUcRGdKkMWpALao_Xlb4U7NXTsh3BmxKx-L7L2E0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای سربازِ روح‌الله، ما در (نايا) همواره از تو شنیده‌ایم ومی‌آموزیم که علی علیه السلام فرمود:
به جانت سوگند، آدمی چیزی جز گوهرِ دینش نیست؛
پس مبادا دینداری خویش را به اتکای نَسَب و تبار واگذاری.
نگر که قرآن چگونه «سلمانِ پارسی» را تا اوجِ والاآرمانی بالا کشید،
و چگونه شرک و کفر، «ابولهبِ» والاتبار را به خاکِ مذلّت فروفکند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88573" target="_blank">📅 18:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adIWCA8NL0l0BAlHokviTziAiuvUcUY9JGnav4B_nfDT5CLVMbwlrk1ypOUiqSkwFY1t5vEuX8nmo6hsHyMAsqqmhOKPHTi_OIY0Ft7zfMMt-8xitc5zXRXzTYej3YPPoANh2DlrsKpYXamyuM_yzpHzeJejaKAhLDxFLudYdaj3qZEAM8uFvFmvD5xHfIjoudV6e1aB6HMwB02xVo4N2xN60D1exfv4RsVI6DmHLenN7FJEfeoTkBubmlF8Jn_s5Vayk_VaGRKTUU2iR4PhsNGd4LpM6qonkRNmI6SaVmNK326W2npL_5N-SBv2YVNt0Zo4bLz4r29PuzZnhpySOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش السلطة اللبنانية الذي ينزح مع النازحين في كل حرب يزعم: إيقاف سوري أثناء محاولته تهريب قذائف صاروخية إلى الأراضي اللبنانية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88572" target="_blank">📅 18:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e4021968.mp4?token=A2TmdoDY_eDQQxmYVbBnOxc0T3ih02Gj1o-whkaNiCMl_mFTaqCZrZoW7yuaGSfFMk3Fvys4zufzbWoETE8waD0-9XYMBzG2gKbtiQHdj4DR-r5bQpKz40FE_P_-PBREeRrotQIFWYQZkzbqSaKmOrhzwQscY9_T1EwycgskpD-dbWyGEHZStXARB5rqHjTmrcFC4cPWhGQZ27pjfiQ_CdwJCS9IQlGhW2JtODjhrTiGuqfDaYfNOKgFnoq7qnIPDqIdZL7898j8ZRqqm24dgM-ne7ZvFnhN3RtRekiv5xCJhiw1_H6HWCMQ4LRP5R9bTS-L-gC_qG2Y7FZ6ghPkUbEGGc8wh1zFQ_8vKwby096JexnGYBR8vBpU-Yw_v_GoWfepxrbGJe_QaqGwPOgIMltCIERi3uZRHtFuMCSPDvFL2L7aFN43JwulVaFtWMo5_WpTGX0n1Lu7PIJ4mXexh25-ZUNDQSmABs61wxavixYeQQKVsuF5UBsebrRNBg3GzGDUM0Q441-N9gh9FQOvVEIUCugkNrZRTwvud1xVbEuC1Nd1Q14bCZco1HKW1KQa8lRXUqzaI50HOi8HGiHokFSgx_6EBd55jXkZgoSaNxCbaFxMX4RS8s-2IQxAAYAhRw-bSfTCgVDYjw9zabIb194KaXc4R-4A1AbbJaHeujU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e4021968.mp4?token=A2TmdoDY_eDQQxmYVbBnOxc0T3ih02Gj1o-whkaNiCMl_mFTaqCZrZoW7yuaGSfFMk3Fvys4zufzbWoETE8waD0-9XYMBzG2gKbtiQHdj4DR-r5bQpKz40FE_P_-PBREeRrotQIFWYQZkzbqSaKmOrhzwQscY9_T1EwycgskpD-dbWyGEHZStXARB5rqHjTmrcFC4cPWhGQZ27pjfiQ_CdwJCS9IQlGhW2JtODjhrTiGuqfDaYfNOKgFnoq7qnIPDqIdZL7898j8ZRqqm24dgM-ne7ZvFnhN3RtRekiv5xCJhiw1_H6HWCMQ4LRP5R9bTS-L-gC_qG2Y7FZ6ghPkUbEGGc8wh1zFQ_8vKwby096JexnGYBR8vBpU-Yw_v_GoWfepxrbGJe_QaqGwPOgIMltCIERi3uZRHtFuMCSPDvFL2L7aFN43JwulVaFtWMo5_WpTGX0n1Lu7PIJ4mXexh25-ZUNDQSmABs61wxavixYeQQKVsuF5UBsebrRNBg3GzGDUM0Q441-N9gh9FQOvVEIUCugkNrZRTwvud1xVbEuC1Nd1Q14bCZco1HKW1KQa8lRXUqzaI50HOi8HGiHokFSgx_6EBd55jXkZgoSaNxCbaFxMX4RS8s-2IQxAAYAhRw-bSfTCgVDYjw9zabIb194KaXc4R-4A1AbbJaHeujU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عبوة ناسفة في صحراء محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88571" target="_blank">📅 18:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حدث امني في صحراء الانبار</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88570" target="_blank">📅 18:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حدث امني في صحراء الانبار</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88569" target="_blank">📅 18:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88568">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
🇨🇳
الولايات المتحدة: عرقلنا قراصنة صينيين اخترقوا وكالة ناسا والاحتياطي الفيدرالي والمعاهد الوطنية للصحة ومجلس الشيوخ.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88568" target="_blank">📅 17:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88567">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🇨🇳
الولايات المتحدة:
عرقلنا قراصنة صينيين اخترقوا وكالة ناسا والاحتياطي الفيدرالي والمعاهد الوطنية للصحة ومجلس الشيوخ.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88567" target="_blank">📅 17:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏امريكا تفرض عقوبات على موقع مجموعة العمل الفلسطينية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88566" target="_blank">📅 17:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88565">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامب: ليس لدى كندا أي شيء نحتاجه وحان وقت الاستغناء عنها لتعليم كندا أنكم لا تستطيعون فعل هذا بعد الآن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88565" target="_blank">📅 17:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88564">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامب: ليس لدى كندا أي شيء نحتاجه وحان وقت الاستغناء عنها لتعليم كندا أنكم لا تستطيعون فعل هذا بعد الآن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88564" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88563">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74978db9a.mp4?token=D5AfvwZgOnUDujh49g8_0UPlB9dhi1MIg1H8ufivyFkNAZIpMmffC0Wxu2uXurmDwzr61Winh0QhEPpAy4fbmaip6L9k-ruvvDNBeAOYJR5moGeClcfYX1EPx_lCX-xutsBRNdqKPxN_jDfLZB6S4Bp2NqwNVh5EI_Wxoh4HlYknw2d42hce48NlNJz0_bp6JAIBoaRgLnbhZW6bVofbWD0K9yEqpaE82N5QLfeFOzBF9eFd0Frk2xBZECE5ineycbIksHfe2z-2wLrEvZ9Tdpk2fJb7ulxcNXeEGmsz0efshGebvr7iylBGzU8pggOxoFCTmIUhpxJ6TEHcf8Csp4mREUQH426Xegcyr2PxcNyIiOU3NwDieb5-b1xpFM_Z8KSuLF6t6iTr2qIztR8h5DNkyE_MT6Ndd9zazPgo25RoH00cJ4t4z1GMexaTzW8OdorN_gyFuyqz2ZvjrxKkzBpgGpL_pw5LdiR7E_ssI28WV3mLN0pBoR54vAzmQzW1hwiZe40v2ZZamnhq9WYeTxT1gNvmIc8k34K5BC-nfXFhyFlH4gWAfl4Ba6VPsu9EB8EDynqZ82gi51RgYymznu5CBFrkX0dzVEwN1TNpZwYZoeINADnJMWvofifxa0vli3x2qrUalJZ7yXm24oo7rwAIjZAk5cnIBF-Y_hgCR7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74978db9a.mp4?token=D5AfvwZgOnUDujh49g8_0UPlB9dhi1MIg1H8ufivyFkNAZIpMmffC0Wxu2uXurmDwzr61Winh0QhEPpAy4fbmaip6L9k-ruvvDNBeAOYJR5moGeClcfYX1EPx_lCX-xutsBRNdqKPxN_jDfLZB6S4Bp2NqwNVh5EI_Wxoh4HlYknw2d42hce48NlNJz0_bp6JAIBoaRgLnbhZW6bVofbWD0K9yEqpaE82N5QLfeFOzBF9eFd0Frk2xBZECE5ineycbIksHfe2z-2wLrEvZ9Tdpk2fJb7ulxcNXeEGmsz0efshGebvr7iylBGzU8pggOxoFCTmIUhpxJ6TEHcf8Csp4mREUQH426Xegcyr2PxcNyIiOU3NwDieb5-b1xpFM_Z8KSuLF6t6iTr2qIztR8h5DNkyE_MT6Ndd9zazPgo25RoH00cJ4t4z1GMexaTzW8OdorN_gyFuyqz2ZvjrxKkzBpgGpL_pw5LdiR7E_ssI28WV3mLN0pBoR54vAzmQzW1hwiZe40v2ZZamnhq9WYeTxT1gNvmIc8k34K5BC-nfXFhyFlH4gWAfl4Ba6VPsu9EB8EDynqZ82gi51RgYymznu5CBFrkX0dzVEwN1TNpZwYZoeINADnJMWvofifxa0vli3x2qrUalJZ7yXm24oo7rwAIjZAk5cnIBF-Y_hgCR7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏سأمنع منعاً باتاً تطبيق الشريعة الإسلامية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88563" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88562">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd317e66d.mp4?token=OqhAW24-apmyTSKDfM_ky00fCXs6u_bJlxDPgEorRFq_EQUXKM740XZcb1rz-Fpo6wcnkovx7h77VZUbNN7jeqI7uQ58wxL5ehubFdNir_YFuyUj_NvRA6yD2eQWQ2JqTap9_uxJ50QKNBS4w5DBZblx9X3NJqayKd8ymaJ2cFEEWyfttuwQS0XsnWlXH_eaj6yri3dMOeUe3sI9hxed_yLN7YjWTy2RXJ_HxaBR9LQO-CT5E1--NngXaUmzJqUeDNN1ZSqWNmtJfajdaceAr9pAP4-tGa2H-fZngReYbX-U8iXYvOkURX5M5D8__KV2pEhnXAN-BiFvqV_9EorGqTdNi6SyCUa9WkM7XjHccB5gOLH2y1yZazUqqh_aDR1xEmVpGHiS5_0e4I-IukZ5bzvV_xa-Try_3AzeHc7N0VXGMWan_AvyCwcKNHN_sMRFztwvHMIooxObphJdXrE5qj3Os-R2hzFYNbAk_ZcBWOxR0UbfVx8Ge9T4EzZ9_yzJotYeYfZgL8j0bC7mw1BTJ2UjzqmFWFoQOnw0f3yJIkNJptJ73mZ0-hSAMsfZSibcp5HKX73k4-udW9uvyFheKDlMcqNdyBkSbNh00tlnGbVUL0G9Chb5or5agw-nt12i6godXccVrPC_4D19yVsmlqXV-mQuY6sjA9lftqeQXvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd317e66d.mp4?token=OqhAW24-apmyTSKDfM_ky00fCXs6u_bJlxDPgEorRFq_EQUXKM740XZcb1rz-Fpo6wcnkovx7h77VZUbNN7jeqI7uQ58wxL5ehubFdNir_YFuyUj_NvRA6yD2eQWQ2JqTap9_uxJ50QKNBS4w5DBZblx9X3NJqayKd8ymaJ2cFEEWyfttuwQS0XsnWlXH_eaj6yri3dMOeUe3sI9hxed_yLN7YjWTy2RXJ_HxaBR9LQO-CT5E1--NngXaUmzJqUeDNN1ZSqWNmtJfajdaceAr9pAP4-tGa2H-fZngReYbX-U8iXYvOkURX5M5D8__KV2pEhnXAN-BiFvqV_9EorGqTdNi6SyCUa9WkM7XjHccB5gOLH2y1yZazUqqh_aDR1xEmVpGHiS5_0e4I-IukZ5bzvV_xa-Try_3AzeHc7N0VXGMWan_AvyCwcKNHN_sMRFztwvHMIooxObphJdXrE5qj3Os-R2hzFYNbAk_ZcBWOxR0UbfVx8Ge9T4EzZ9_yzJotYeYfZgL8j0bC7mw1BTJ2UjzqmFWFoQOnw0f3yJIkNJptJ73mZ0-hSAMsfZSibcp5HKX73k4-udW9uvyFheKDlMcqNdyBkSbNh00tlnGbVUL0G9Chb5or5agw-nt12i6godXccVrPC_4D19yVsmlqXV-mQuY6sjA9lftqeQXvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الايرانيين غير محترمين</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88562" target="_blank">📅 16:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88561">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17c3fa946.mp4?token=C78od-FymX8MTLanG46dArJ2so1bxD3dzcRdfQ-potookfAL-SYmCIxr4HxRP0AsIWKHg5mY3IYjqKvpuFcXpplfYu1JDc_YnzYLEh2nCHr9FyCgRruoNRgWSFpWe9mEN-J13h6pGd6TISj2zeoNGg3NUxhLMFQBjOZOSk0PWDHOVw-hCo7CxZJchdK8JJXxpuzK-Sx2zIovwB6sXXlgNl0qlZ2DsHBqFF0GeyulTcAA5pXAxXQ1uVwxFTQWOtgWq7XdPH2J0AFKfXpsfp53VYJvWmTcP5sXwJMrX0-lUXQMzkGkLVShCjYoF2U4y_6dywywz10UcQZPfnwlm75srIJ9nr7R8UWkiFK4BJ4XCOERPnG-rviptdWWP_shkrIxDVgQwotDjcG4yeSbR9Ihqw_vvJTW5QbVGrLkA88OFhMFbqnQpuwHkXbqRw2x9zKET5Z-rK6ei7FoQqPxJ2IZ7j7Ve-lA6peP5aSbRIzXSoj_Vs8xy-eqWLqVDgrkGVeURX82lU7m3mmZVMvrtV6pRTqoQP205aZFIPj0udHsxYpIbNAv16_UuhmM5IHx8bjhTSdjhF_2KxhrulzAPgj5rJ_iXHM5dVsW2iwC6GDvQaOTD9TsXTK2egS-arRYa2V7gVO2fX3yzYhUAdB-vX9lb19b2pYSNOzZ-HRrHs0kZHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17c3fa946.mp4?token=C78od-FymX8MTLanG46dArJ2so1bxD3dzcRdfQ-potookfAL-SYmCIxr4HxRP0AsIWKHg5mY3IYjqKvpuFcXpplfYu1JDc_YnzYLEh2nCHr9FyCgRruoNRgWSFpWe9mEN-J13h6pGd6TISj2zeoNGg3NUxhLMFQBjOZOSk0PWDHOVw-hCo7CxZJchdK8JJXxpuzK-Sx2zIovwB6sXXlgNl0qlZ2DsHBqFF0GeyulTcAA5pXAxXQ1uVwxFTQWOtgWq7XdPH2J0AFKfXpsfp53VYJvWmTcP5sXwJMrX0-lUXQMzkGkLVShCjYoF2U4y_6dywywz10UcQZPfnwlm75srIJ9nr7R8UWkiFK4BJ4XCOERPnG-rviptdWWP_shkrIxDVgQwotDjcG4yeSbR9Ihqw_vvJTW5QbVGrLkA88OFhMFbqnQpuwHkXbqRw2x9zKET5Z-rK6ei7FoQqPxJ2IZ7j7Ve-lA6peP5aSbRIzXSoj_Vs8xy-eqWLqVDgrkGVeURX82lU7m3mmZVMvrtV6pRTqoQP205aZFIPj0udHsxYpIbNAv16_UuhmM5IHx8bjhTSdjhF_2KxhrulzAPgj5rJ_iXHM5dVsW2iwC6GDvQaOTD9TsXTK2egS-arRYa2V7gVO2fX3yzYhUAdB-vX9lb19b2pYSNOzZ-HRrHs0kZHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🌟
ترامب:  لا أعتقد أن السيد مجتبى قد مات. لقد أصيب بجروح خطيرة للغاية، في الجانب الأيسر من جسده، في الذراع، والساق، وقد أصيبت كل هذه المناطق بجروح خطيرة. ولكنني لا أعتقد أنه مات. إذا كان قد مات، فهم يقدمون عرضًا جيدًا جدًا، لأنهم يتحدثون باستمرار عن العودة…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88561" target="_blank">📅 16:52 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
