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
<img src="https://cdn4.telesco.pe/file/SxWGQ8aUqoXq7GWuNQ2FH0uR8mtAS546-6l3pTqyYUBIZHuaWFl4s93Hdgkb7Qsrb4XHoFvJt8H5i08BmQf-Qad4pH59szfkmJL3V0eqajM60J8bkFjIGoTVOE6fCXDGWBm_nVCFeOXqdcnelu3FbiMhNlNLe5UeldiIGNajx_PkpgPS2w8S2csFRYU8OTBYM0Co-lAM3Q2i5U94ta21flDGBL9azlq_F63gzGpqzIYZpJXZ-0ezZtr_jyQ3LEXY2HQAi1F3TEdHXl1MxJySM4bkYaWYkqClPHSyxouJyGK-tGaaxkpDrSHrCS3eAiIxjPkUX7iNei6nQkhcjvSZ_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
قاليباف: هدف المفاوضات هو إنهاء الحرب وإرساء أمن مستدام، وليس تطبيع العلاقات مع الولايات المتحدة.  نحن لا نريد أن نتقدم بالاستسلام ولا بالشعارات، بل يجب أن نبحث عن نصر مُهندَس بقوة وعقلانية إيرانية.</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/naya_foriraq/77808" target="_blank">📅 21:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
قاليباف: لا الدبلوماسية تمنع العمليات العسكرية، ولا العمليات تمنع الدبلوماسية؛ إن المجال العسكري، ومجال الدبلوماسية، ومجال التواجد الإعلامي، ومجال خدمة الشعب، كلها عناصر متكاملة.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/naya_foriraq/77807" target="_blank">📅 21:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
قاليباف: كان انتهاك وقف إطلاق النار والحصار البحري سببًا للتوترات الأخيرة. أؤكد للشعب الإيراني أننا سنواصل من الآن فصاعدًا الدفاع عن حقوق الشعب الإيراني بكل قوة. إن تصريحات الرئيس الأمريكي بشأن مذكرة التفاهم تخالف بنود الاتفاق، مما يدل على أنهم لا يسعون…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/naya_foriraq/77806" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
قاليباف:
كان انتهاك وقف إطلاق النار والحصار البحري سببًا للتوترات الأخيرة.
أؤكد للشعب الإيراني أننا سنواصل من الآن فصاعدًا الدفاع عن حقوق الشعب الإيراني بكل قوة. إن تصريحات الرئيس الأمريكي بشأن مذكرة التفاهم تخالف بنود الاتفاق، مما يدل على أنهم لا يسعون إلى وقف إطلاق النار ولا إلى الحوار، وكان ينبغي علينا الرد بحزم للدفاع عن حقوق الشعب الإيراني، وقد قامت قواتنا المسلحة، بفضل الله، بواجبها على أكمل وجه. أؤكد لكم، أيها الشعب الإيراني، أننا سنواصل من الآن فصاعدًا الدفاع عن حقوق الشعب الإيراني بكل قوة، وبقيادة وتوجيه المرشد الأعلى لعصرنا، وبتوفيق من الله، سنحقق نصرًا آخر لإيران.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/naya_foriraq/77805" target="_blank">📅 20:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴‍☠️
مسؤول في جهاز الأمن الصهيوني: العودة إلى قتال مكثف مع إيران مسألة وقت ليس طويلاً، قد يكون في الأيام القادمة.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/naya_foriraq/77804" target="_blank">📅 20:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f1fcee3c7.mp4?token=cot6Z0JFbM2q8rAxPPQRiRwFu6lhvrBjlpXlQkW1JT6QKME8yvkAMUGoh7nNwfR7_Ud0cC96mzcPTI0pZ16H5ceppVZ4Y6VJiYSc-sMA8CZaXoKUOszPbUCMyGJS0Z1WWGLdFKAgjXghykHoUvSurmZNwJtQTCGipsPYbYF2GcCrOa8JaSvEAedczEUOQ9jHrW-nVsiuvjtClaxC85IzRZ6tgNTpDb4PCWu8_2RD-cfqLZD-mWsJWhrRyqx5Y0A5y1a5WqLHOagn2XBzNXwZzVsxY2wTSo3hzKAOXsM6vQeaAKRNqp9PoEPx8OAfjwqXG5ybMe8tBUo6b4MharBj-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f1fcee3c7.mp4?token=cot6Z0JFbM2q8rAxPPQRiRwFu6lhvrBjlpXlQkW1JT6QKME8yvkAMUGoh7nNwfR7_Ud0cC96mzcPTI0pZ16H5ceppVZ4Y6VJiYSc-sMA8CZaXoKUOszPbUCMyGJS0Z1WWGLdFKAgjXghykHoUvSurmZNwJtQTCGipsPYbYF2GcCrOa8JaSvEAedczEUOQ9jHrW-nVsiuvjtClaxC85IzRZ6tgNTpDb4PCWu8_2RD-cfqLZD-mWsJWhrRyqx5Y0A5y1a5WqLHOagn2XBzNXwZzVsxY2wTSo3hzKAOXsM6vQeaAKRNqp9PoEPx8OAfjwqXG5ybMe8tBUo6b4MharBj-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير يحلق في سماء محافظة ديرالزور السورية.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/naya_foriraq/77803" target="_blank">📅 20:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
مسؤول في جهاز الأمن الصهيوني:
العودة إلى قتال مكثف مع إيران مسألة وقت ليس طويلاً، قد يكون في الأيام القادمة.</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/77802" target="_blank">📅 20:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
ترامب:
قلت لبينيامين نتنياهو إنه من الأفضل أن يكون حذراً جداً فيما يفعل لأنه قد يجد نفسه وحيداً أمام إيران قريباً جداً
في ليلة الأحد عاد نتنياهو إليّ متأخراً وأبلغني أنه قرر الهجوم
الإسرائيليون أعطونا تحديثاً عندما كانت الطائرات في طريقها إلى إيران، وأنا تصرفت لتقليل نطاق الهجوم
خمس دول من المنطقة تواصلت معي وطلبت مني الضغط على نتنياهو لعدم الهجوم، اتصلت ببينيامين ووافق</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/77801" target="_blank">📅 20:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da6f82aa3.mp4?token=vVzxUOoFNXV-AzsYXUwZjfFZE0vA8A7bjIEu_maCeD1wWWFR9So92-BCTudVS0Ohq-80Hic19AGLZAKz2iOy1RRV4FROH7tzzimet1TWHM9E05WWH8vfKTVKiMz9f3OH8Hg3uvVqgqG_9BU6yLWn2iDUwJJ5RxCL7Nd6ZroGX-vD68DqKU34wJNxxUgj4dcFIKwgNq2HNKjqgwGoVEXVVQEwEapGnTnZCFQZKk6KA8bAaU35_E4FuB3DT4xqech_NdKwslBfDpN6D7iEl9CNkd_nitE35qqctj7XiXCG-MDm1pNP2OZq5lhfyUV6NoZwKS7ETdjMUHrJ4Kj3uZJK6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da6f82aa3.mp4?token=vVzxUOoFNXV-AzsYXUwZjfFZE0vA8A7bjIEu_maCeD1wWWFR9So92-BCTudVS0Ohq-80Hic19AGLZAKz2iOy1RRV4FROH7tzzimet1TWHM9E05WWH8vfKTVKiMz9f3OH8Hg3uvVqgqG_9BU6yLWn2iDUwJJ5RxCL7Nd6ZroGX-vD68DqKU34wJNxxUgj4dcFIKwgNq2HNKjqgwGoVEXVVQEwEapGnTnZCFQZKk6KA8bAaU35_E4FuB3DT4xqech_NdKwslBfDpN6D7iEl9CNkd_nitE35qqctj7XiXCG-MDm1pNP2OZq5lhfyUV6NoZwKS7ETdjMUHrJ4Kj3uZJK6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من الغارات الإسرائيلية على مرتفعات مليخ بجنوب لبنان.</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/77800" target="_blank">📅 20:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يزعم:
سلاح الجو يحاول إعتراض طائرة بدون طيار أُطلقت من اليمن.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77799" target="_blank">📅 20:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الاصوات التي تسمع في سماء المدن العراقية نتيجة عملية إطلاق صواريخ نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77798" target="_blank">📅 19:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏هيئة بحرية بريطانية: لا تقارير عن تأثير بيئي بعد استهداف ناقلة نفط هندية قبالة عُمان</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77797" target="_blank">📅 19:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwLR_sPBAphiWT691XxYLp6SKBSsXbOp9ibSW-SH2FfsCSYo2INPyzn3NFr3lsmapEu6eaHMkRwAytETEG-QyE-3t2ybnyLa9-oYYFoEHJkUtoNqZYasftzIFeH0Kqvt4B84LPeiT2uPE3fYzxrhKLJDvrj-1SuJsrXPMb_Ir6p339-Zv_tsEh9d7MKLO0pyA5X44WrseSgi_N7lYSU582Mugw3lHoYfdi_19Fk7rN2In8l07UCae6XMMTRHhyMTVIZQ_euyWlSl9MSogZeg2SyLn3RhX0S-LxQZQwxxZQjT-4hfhJlSSPrVfmQZYh_7SrJBtdgmJpjVmIt0NvlVqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
من المستحيل أن يخسر سبنسر برات جولة الإعادة في لوس أنجلوس بعد التقدم الكبير الذي حققه. دولة من العالم الثالث. انتخابات مزورة! الآن سيعملون على الرجل العظيم ستيف هيلتون. لن تكون هناك نتائج، على الأرجح، لمدة أسبوعين، وفقًا للمسؤولين.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77796" target="_blank">📅 19:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
أطلق الجيش الأمريكي اعتراضيات الدفاع الجوي في محاولة لتخميد أحدث وابل إيراني من الصواريخ الباليستية الموجهة إلى إسرائيل يوم الأحد، حيث تسعى طهران إلى إعادة رسم الخطوط في الصراع المتوقف والدفاع عن حزب الله في لبنان.
أطلقت الوحدات الأمريكية في المنطقة الصواريخ الإعتراضية دفاعا عن النفس. هناك عدة مئات من الأفراد العسكريين الأمريكيين في إسرائيل، وكثير منهم يديرون الخدمات اللوجستية في مركز مراقبة وقف إطلاق النار في غزة في جنوب إسرائيل.
إن المسؤولين العسكريين الأمريكيين لا يزالون يراجعون ما إذا كانت محاولات الاعتراض فعالة في إسقاط أي صواريخ واردة.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77795" target="_blank">📅 19:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
هيئة الطيران المدني الإيراني:
عاد المجال الجوي للبلاد إلى وضعه الطبيعي، وستُستأنف عمليات الطيران وفقًا لإشعارات الطيران الصادرة (NOTAM).
مع توفير الظروف الآمنة والتنسيق اللازم مع الجهات المعنية، رُفعت قيود الطيران، وتعود أنشطة الطيران في البلاد إلى طبيعتها وفقًا للخطة الموضوعة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77794" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
كان الجيش الإسرائيلي على وشك تنفيذ طلعة جوية هجوم كبيرة على إيران في الساعات الأخيرة - تشمل عشرات من مقاتلات سلاح الجو التي كانت على وشك الإقلاع نحو إيران، لمهاجمة أهداف في جميع أنحاء إيران. هذه الطلعة الجوية الهجومية الواسعة - لم تُنفذ بالطبع.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77793" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAjQrO4ZpWxt6_44WhXb8tzH4dcaSQMNRG6u37RyGBtVRZO4QNBuX-uefUYmDabil05XNAuqQmcbF20TTwaXQ5cPDP2SlWAlV5sJlBFTREJN6EyaRYYOdmYH0_zQ-DWCI_B0i-nRg8W7BpXCvq9sNe8xybH8bGqZcnxFuy06NkCEUT2Tav6pQEVH5AX0jzcI1EnEga_GkVbFOzfnzhrjb1vrlJHiV66TX4quXSD6Wrg2K67-p5ABEbyqNQZsWl1LaDlsP9EG7XgbZKMVlzOyO8aLWm9waXCYQ0KeU7Xyl20Dou4RIDQU6zaLt9FKvt1k6n1OEcu7t6esxDC18vG46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية "إسماعيل بقائي":
من يبني "سلمه" من "الفوضى" يقنع نفسه بأنه سيصل إلى السيادة على البشر. لكنه يبقى غافلاً عن الحقيقة الأولى والأكثر حتمية: صانع الفوضى هو دائماً ضحيتها الأولى.
‏إنّ الرجل الذي لا يرى قيمةً في الوفاء بالتزاماته أو الحفاظ على السلام، بل يزدهر بالفتنة والخداع والصراع الدائم، يحكم على نفسه بعملٍ شاقٍّ لا ينتهي. عليه كل يوم أن يُشعل نارًا جديدةً ليُغذي القديمة. ليس هو سيد الأزمة، بل أسيرها؛ ولا يُمكن وصف أي أسير، مهما كان ظله مهيبًا، بأنه قويٌّ حقًا.
‏إنّ مُثيري الفتن ليسوا في الحقيقة بناة السلطة، بل هم أسرى القوى التي يُطلقونها. فمتى ما استيقظت هذه القوى، لا تُفرّق بين حليف وعدو، ولا بين اليد التي استدعتها والأرواح التي تلتهمها.
‏تأتي هزيمتهم النهائية في اللحظة التي يدركون فيها أن السلاح الذي صنعوه لإخضاع الآخرين قد أفلت من قيوده وأصبح له إرادة خاصة به. في تلك الصحوة المريرة يكمن ضعف قوتهم الحقيقي، وبداية سقوطهم المحتوم.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77792" target="_blank">📅 19:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77791">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
قيادة الجبهة الداخلية الصهيونية تعلن عن رفع القيود في جميع المناطق - باستثناء مستوطنات الشمال القريبة من الحدود.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77791" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
ترامب:
أعتقد أن الولايات المتحدة وإيران تقتربان من اتفاق يمهد الطريق لمفاوضات طويلة الأمد.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77790" target="_blank">📅 19:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1w44ixgOaUEi47XmPpxreckNBvxr6Kd5YJsGh0akJpjd4b57RGWuEUpvF-PYa7xvAGQnhSqLx2r8fUqRz2E_CXWYvFQJrXfK7sTMZkeEH0U-EZq3Y7ErCCQ9-UTlFQZurPZ1tjNHDKGCo4ptpEABib2m4y1xSymNRabS0eACoiZ9trz8NGFBem9Px-ytpwWkrlCWUdfo6Z-1rZuQrNEFgb-DNbFOQ9NMoLBQJgcxi9oiBNgZ4V_Kpz0QqgxrCKCWoYD1ACRc1g7ZP2FWBPpSIJdYuMHYgYvotU4ZrVqNo2KWvauaL_Gc7MHecng2M_RMEKktJ_XnXiraEWbnUaruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
قيادة الجبهة الداخلية الصهيونية تعلن عن رفع القيود في جميع المناطق - باستثناء مستوطنات الشمال القريبة من الحدود.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/77789" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارة الدفاع السعودية: صفارات الإنذار التي تم إطلاقها في وقت سابق من اليوم كانت احترازية نتيجة إطلاق صاروخ باليستي من اليمن اختفى بالقرب من الحدود، ولا تزال التحقيقات مستمرة لمعرفة تفاصيل هذا الإطلاق.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77788" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab44a945d.mp4?token=l_iYYb2HsYBlovFlp56ojduUpYFUNNhw7fN7cIrDsvuNkVcbKYvq2MPXiPrBId3jihf9U6g5uJy59bTm80UZj67aUzQFm_kQRQjHj91LkTAOjGuagR2JnDRmuHXLa_4nGwyTOFD4G1BHdvhqv4oaL8T2cVdZigQLedqT6ficoo_4UoomsWbEHiBbg3S-fDdPmXsooq46aWO9omXas6Tdu3ikmbwZilOu9fQSwTFbsrpLNLv1Toh5ypRFklYYkOlHSDvzS9L7uYmwd0buky6RG5aDwQL1XxipbHRedwBtn1Z2ZvgApe4L1Xgvgfsh3N5G9VOY44xIf0tdofDJpbVR-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab44a945d.mp4?token=l_iYYb2HsYBlovFlp56ojduUpYFUNNhw7fN7cIrDsvuNkVcbKYvq2MPXiPrBId3jihf9U6g5uJy59bTm80UZj67aUzQFm_kQRQjHj91LkTAOjGuagR2JnDRmuHXLa_4nGwyTOFD4G1BHdvhqv4oaL8T2cVdZigQLedqT6ficoo_4UoomsWbEHiBbg3S-fDdPmXsooq46aWO9omXas6Tdu3ikmbwZilOu9fQSwTFbsrpLNLv1Toh5ypRFklYYkOlHSDvzS9L7uYmwd0buky6RG5aDwQL1XxipbHRedwBtn1Z2ZvgApe4L1Xgvgfsh3N5G9VOY44xIf0tdofDJpbVR-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارات معادية على بلدة كفرتبنيت بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77787" target="_blank">📅 19:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">طيران مسير من لبنان يخترق الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77786" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">طيران مسير من لبنان يخترق الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77785" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqLqHM9ofLCq-KGi9El3Kd2aO6Ct28FtydleIv0GCbV2_ooqnsA2UUPGut69skh2LftH2zzUc2z3FmyMRCe6Utqw633hQgC6sCA2AV7Mss2eoNdR-jHf7T6bf-B-LLaStOSv3YuPWAS45gf2tTBUS1fouQp6v1JKzenEmH474WP9Zi2TFvJ1WNDLudzQunXymlp6CaTXTml1M3EL-m8ODguX05qwbtnyItlJjYkhs0Nlyjofe2se50zNvhldTrzBhlk5o8e8EtNDXJkvXLaulDY_s28irtLa-EkEtsEiDxCcsaWBkv37LbfdzbzhLDATagyJAWe5ASQDXxOtBBXxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش الإحتلال يصدر إنذار إخلاء في جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77784" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔵
الناتو ينهار …
أفادت التقارير أن ألمانيا وفرنسا أوقفتا مشروعهما المشترك لتطوير مقاتلات الجيل القادم FCAS/SCAF بعد فشل شركتي داسو وإيرباص في التوصل إلى اتفاق بشأن شروط التعاون، حيث خلص ميرز وماكرون إلى أن البرنامج لا يمكن أن يستمر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77783" target="_blank">📅 18:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91dc65254.mp4?token=oLzhxVupxpMY1y2pR1q8VgqUFAt-OYP7FO7ThPZ1nXI1Mb0F9tBq6BiT5LDnBfJAZ3QUd2Rjel7-ra8QuFmov0J5RW2L62vBA3TBl1z8yVuNgYpYC_QEuAaQyNznJlmPWrFXOJ4iK0Nz1-ROJP1Qfp2_K6U1HJeOF4T4YqVxFB3spzoelUpfXg7dgInJ2eb5FKl7vmMynsNWXQWXVn1Tuvq3bkPcvDhREn8E97sQtwxbBAR6ft5WruAwYph87LC59QM2R59fJZugl8I4leI5POmZ-GKhhgSWgqXZk4yUcBZMJmRyo_5m3mizZsIRuKqqEOaZGXq65jT4VCCqFoVoDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91dc65254.mp4?token=oLzhxVupxpMY1y2pR1q8VgqUFAt-OYP7FO7ThPZ1nXI1Mb0F9tBq6BiT5LDnBfJAZ3QUd2Rjel7-ra8QuFmov0J5RW2L62vBA3TBl1z8yVuNgYpYC_QEuAaQyNznJlmPWrFXOJ4iK0Nz1-ROJP1Qfp2_K6U1HJeOF4T4YqVxFB3spzoelUpfXg7dgInJ2eb5FKl7vmMynsNWXQWXVn1Tuvq3bkPcvDhREn8E97sQtwxbBAR6ft5WruAwYph87LC59QM2R59fJZugl8I4leI5POmZ-GKhhgSWgqXZk4yUcBZMJmRyo_5m3mizZsIRuKqqEOaZGXq65jT4VCCqFoVoDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كلمة للنتن ياهو بعد قليل</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77781" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏مسؤول أمني رفيع لاعلام العدو: المستوى السياسي أصدر تعليماته بوقف العملية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77780" target="_blank">📅 18:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">كلمة للنتن ياهو بعد قليل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77779" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دك سفينة هندية بمسيرة قبالة بحر العرب</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77778" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxGBIaazsJhbay2y_FaM3_nxp2u1yW_NDx-Zl8SL498TU_2FVS5EZwtZTh9z0NJXoRjd2rzctCQ97RxNZvw-QsDzcWwNf_mZR0xifAuDCkPL_av2kH9NHPqIgBiYDT_WyKZvow3MYIzektHx1AatsXTtxdh15YzOjbxDvJnFWUkFWbiPrma0d9G1VwmNT69pTAEuVhmMyxN-b-SUQrugSA6z85wiprFb_usnclNY5YzIqPKhH5PB7Iwvu4IziX5qemsnsEgCqQsoKJMfc8a_3Qg1Y402WZUxGFj1tDh3Pl8SpVP-Zm6E3wz7y5DdjH7InNJIOxaNkJrNmnlwRa2z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
لقد عطلنا معادلة وقف إطلاق النار على الورق وانتهاكاته المتكررة على أرض الواقع. طالما لم تكن لديك إرادة حقيقية لبناء الثقة، فسيكون رد إيران هو نفسه.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77777" target="_blank">📅 18:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏وزير الحرب الصهيوني: أي محاولة إيرانية للربط بين لبنان وإيران ستُواجه بقوة كبيرة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77776" target="_blank">📅 18:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏وزير الحرب الصهيوني: أي محاولة إيرانية للربط بين لبنان وإيران ستُواجه بقوة كبيرة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77775" target="_blank">📅 18:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
القوات المسلحة اليمنية:
مشاهد من إطلاق دفعة صاروخية على أهداف حساسة للعدو الإسرائيلي في منطقة يافا بفلسطين المحتلة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77774" target="_blank">📅 18:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصاروخٍ موجّه.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77773" target="_blank">📅 18:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCdgCCLbyW4bJuUrt09BsNaz1tHJTT1wQBvuF6bxKSzqNdJI2JPuwT026c48-MwpW3_416A99hZXdGS5Es05NebQvF-gJkrU4eOgcBiUSkTEtWPBqhOy3eBO9Ok5f4HTDB5n3iODVhNdzHgpGddGiYnkCzLDWvY1zoYZlqZxHBrmD34vnZ4GOSENRz7fauwV0SQoaBGv4oV_A2RfPDJFTPxZyDBATxEBDiOAtRlHQC7SfWpdH26M7WfNYvT4HJ2bRAyRFW1GVNROQ2g4HT0rJ_RRDCgdsMldCyxvUAkwjYsGiY4Z0dRjNAFSNmTwEcMsK_zr6jq7HrD10bpNzSAuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمين المجلس الأعلى للأمن القومي
الايراني
:
إذا ارتكب التحالف الشيطاني أي خطأ، فستكون المنطقة جحيماً له
سبعة وأربعون عاماً ومئة يوم من المقاومة، من ساحة الحرب إلى ساحة المدينة، ومن ساحة المدينة إلى ساحة السياسة والدبلوماسية، غيّرت النظام الأمني العالمي.
ابحثوا عن التهديد الموثوق في مكان غير واشنطن وتل أبيب!
إذا عاد التحالف الشيطاني الصهيوني-الأمريكي وارتكب أي خطأ، فستكون المنطقة جحيماً له!
السلام على شهداء الضاحية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77772" target="_blank">📅 17:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77771" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INTv7YtwOcYlUigktHT-884hvG9kcxCdae7Go7rw6qoFloYgiDn_khaeQTdH5U6E9Zs1wSLwR439kQXJlv6SdGHp45p1pj50-EdseYTRMkSouODTFmrT4IQHT2uDY_kKqPoKRT2j3x3xsGNwmuPl6nSoBTrtDtxvPe0UZJrdWRKhMzkA8WY-CFoJzywpoeb8JF-FRdXJ7lAX-BheXFFOv5kwcdZcRUFa6Trr6AD-jtSSwNR2BbXUDqay4Zz-rOlEMOLeOEievLIFGwEfZNnRDWu7iAkGiocpRATk2YcNp-wxC6QhdbMy7QJwF0qbuwmvzBIAO_zH1QBWowX0k3M1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسيرة صهيونية تستهدف سيارة في محيط مركز الصليب الاحمر اللبناني عند مدخل صور الجنوبي.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77770" target="_blank">📅 17:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/77769" target="_blank">📅 17:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سي إن إن عن مسؤول أمريكي:
لم نعترض اي صاروخ ايراني ليلا.. لا صحة لمزاعم إسرائيل بأن الولايات المتحدة اعترضت صواريخ باليستية إيرانية أطلقت باتجاه إسرائيل.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77768" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارة الدفاع
السعودية:
صفارات الإنذار التي تم إطلاقها في وقت سابق من اليوم كانت احترازية نتيجة إطلاق صاروخ باليستي من اليمن اختفى بالقرب من الحدود، ولا تزال التحقيقات مستمرة لمعرفة تفاصيل هذا الإطلاق.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77766" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YhHfo0XyQq-oP9sb_TX462i_WMQwTUPOeTdeeiLkQWQW889qHnAUcj6eyFS4B9HBJfxauCxQmemSe4a7nF70pEVCDJ9c5sT0H_PcaY-YbFhdVaCMHbizTQZwC008GawlJ0nzNjSEpPOdW1d2pzEJcVvYIV3hqz0IHyG65IvHdkn7gUocGWorNgp5zfWSoW8heE647v9Zh3XJX3pwHIOkCZJELdHTN0GDH6dBbIAMfQM9kKeqlVsfaJcTpDBhsC-fh5V65ePwK-prOlver-EU3N14_OB9DldrIJyAc73kjGryNPxv_MxfosPoK_1MK7AqIrjpFDKuOFN3gGEJlz1ALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIkCjK56JHukG0AGm0b4kNiWubvTVIkLUzh3zYUsajvDaZBiu5BYZeu8OP71TRNFCepwRiLh1pcBEm-ZvOTjyQkqNE6iYnsO2--ukHZxFkG0SU7JMZNebWPF_f9siP_vi7bJQCDftqgozW_HYG3ELbByBWi51oTEzyOrl0UgJtgYPhhQbiMBupeK_O_ozp9U3uFEKg6OyhDHwdqyErJnFJnhsRkj5e9tPHhBqA6mb_V23y89TG5wuIi2JCyJCzfCJrFMn_uROXmcdI6tf7HDKgtbHH5RaP-DtHut_c3Vyi5EjanXPnD9bwG0NoAyA_BquCaX99tqVjrZqSdFbmuaLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هيئة الإعلام والاتصالات العراقية تقرر وقف (برامج الجريمة) التي تتضمن استجواب المتهمين أو عرض تفاصيل الجرائم ومحاكاتها مؤكدة أن هذه البرامج تنتهك قرينة البراءة وتؤثر على سير العدالة وتشكل خطراً مجتمعياً وتربوياً</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77764" target="_blank">📅 17:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اعلام العدو عن مصدر إسرائيلي:
المجلس الوزاري المصغر قرر وقف الهجمات على إيران واستمرار العملية العسكرية في جنوب لبنان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77763" target="_blank">📅 17:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
رئيس شعبة الاستخبارات العسكرية الإسرائيلية السابق "تامير هيمان": الرد الإيراني على استهداف الضاحية كان الاختبار الأول لقيادة مجتبى خامنئي، فقد أوفى بوعده بضرب "إسرائيل" بالإضافة إلى توجيه رسالة ثقة للشعب الإيراني.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77762" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📱
شركة "واتساب" تعلن إحباط حملة اختراق وهجمات تصيّد نُسبت لشركة السايبر الإسرائيلية "NSO"، والمنصة تتوجه إلى محكمة فدرالية بطلب لفرض عقوبات على الشركة الإسرائيلية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77761" target="_blank">📅 17:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
رئيس شعبة الاستخبارات العسكرية الإسرائيلية السابق "تامير هيمان":
الرد الإيراني على استهداف الضاحية كان الاختبار الأول لقيادة مجتبى خامنئي، فقد أوفى بوعده بضرب "إسرائيل" بالإضافة إلى توجيه رسالة ثقة للشعب الإيراني.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77760" target="_blank">📅 17:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏الطيران المدني السوري: استئناف الحركة الجوية والعمليات التشغيلية في مطار دمشق الدولي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77759" target="_blank">📅 16:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqwhBFodsCz97cCCjnbION7tqgZDW6Qqrb-RZHLZdVvhD5GlEYDUFv3m0eRpekNaj_pjZ5jCGx2xGaSOF37HY9t4gWd3qK8nOLHh_IbESPNSH0HmO97xK7l9J29oe3eIhzOih1_ajBjrP28sXihglOX7083I-7YSbcqPTof__qUchj-GdFTG5YspWeCCUANyWl4KkWut8gLoG4cDL0bJ9v6_cMtTCSrOYWL8jwjhDe4pbq1Y-fZQaQ2xIhIlPlfbRXoCT1xmKOID17NCSsKrxZbMKpAFWb1Ks2PpJVR9QWebbNIXhR_hXVM8UQAQIc-7i0ocLSBo9dyVLoVYUqFRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في ضوء التطورات الأخيرة، نشير الى ما يلي:
أولاً: إنّ الأجواء العراقية تتعرض لانتهاكات متكررة من قبل الكيان الصهيوني الغاصب، في ظل غياب موقف عراقي رسمي واضح وحازم يرتقي إلى مستوى المسؤولية الوطنية، ويصون سيادة العراق التي لا تُحفظ بالبيانات والشعارات، بل بالمواقف العملية والإجراءات الرادعة.
ثانياً: من حقّ الشعب العراقي أن يسمع إدانة صريحة لا لبس فيها لكل انتهاك يستهدف سيادة بلده، وأن يشهد تحركاً جاداً يحفظ للدولة كرامتها وهيبتها ويؤكد احترام حدودها ومقدراتها الوطنية التي لا تصان بالتجاهل او (التغليس).
ثالثاً: نؤكد أننا في سرايا أولياء الدم على أتمّ الجهوزية والاستعداد، وأن جميع إمكاناتنا قائمة ومهيأة لاستئناف أعمالنا فوراً إذا ما أقدم الأمريكيون على التدخل أو المشاركة مجدداً في أي اعتداء أو تصعيد يستهدف بلدنا أو شعوب المنطقة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77757" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">السفير الأمريكي في بيروت:
المنطقة التجريبية جنوبي لبنان ستكون مفتوحة لأبنائها تحت حماية الجيش ولن تتعرض لقصف إسرائيلي، كل ما يحصل في واشنطن يصب في صالح لبنان وإسرائيل ستنسحب وستعيد الأراضي والأسرى</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77756" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بريطانيا تنصح
بعدم السفر إلى
إسرائيل
تماما</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77755" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اعلام العدو عن مسؤول إسرائيلي:
المعركة الكبرى القادمة مع الإدارة الأمريكية ستتركز حول مواصلة فصل الجبهات، ومنع الربط بين مفاوضات طهران-واشنطن وبين جبهة لبنان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77754" target="_blank">📅 16:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
إذاعة جيش العدو:
غير واضح ما إذا كانت إسرائيل ستقبل بمعادلة "الضاحية والرد الإيراني".</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77753" target="_blank">📅 16:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اعلام العدو عن مسؤول إسرائيلي: الجيش سيوقف إطلاق النار في إيران ولكن ليس في جنوب لبنان</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77752" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
الشركة الإيرانية للمطارات والملاحة الجوية:
عقب إصدار هيئة الطيران المدني إشعارًا رسميًا للطيران (NOTAM) يفيد بإغلاق المجال الجوي الغربي للبلاد، تم إلغاء جميع الرحلات الجوية من مطارات البلاد ولن تُسيّر حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77751" target="_blank">📅 16:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نيويورك تايمز عن مسؤولين عسكريين إسرائيليين: نتنياهو أصدر تعليمات للجيش بوقف الاستعدادات لشن هجوم آخر على إيران</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77750" target="_blank">📅 16:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئيس منظمة الطوارئ الايرانية:
14 اصابة بالعدوان الصهيوني على البلاد منهم من مدينة ماهشهر بمحافظة خوزستان، وواحد من طهران. لا يزال شخص واحد يتلقى العلاج في المستشفى، بينما غادر 14 مصابًا بعد تلقيهم الرعاية الطبية اللازمة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77749" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اعلام العدو: تم رصد ثلاث عمليات إطلاق صواريخ أُطلقت من لبنان. تم اعتراض بعض الصواريخ وسقط صاروخ آخر بالقرب من قواتنا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77748" target="_blank">📅 16:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ايران تفرض معادلة مفادها
الضاحية بيروت امام قصف تل ابيب
اماً المعادلة التي فرضها عون هي عمل صحن كبة نية ..</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77747" target="_blank">📅 16:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الدفاعات الصهيونية تحاول التصدي للهجوم الصاروخي لحزب الله على مستوطنات الشمال</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77746" target="_blank">📅 15:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اعلام العدو عن مسؤول إسرائيلي رفيع:
بناءً على طلب ترامب - إسرائيل توقف الهجمات على إيران. الهجمات في جنوب لبنان ستستمر في الأيام القادمة بكامل قوتها. سنقصف أيضًا الضاحية إذا استمرت الهجمات على مستوطناتنا ومواطنينا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77745" target="_blank">📅 15:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
🏴‍☠️
السفير الاميركي في لبنان مدافعا عن اسرائيل:
هاجمت الضاحية بالامس بسبب ضربات الحزب باتجاه المستوطنات الشمالية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77744" target="_blank">📅 15:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مصدر أمريكي لـCBS:
الجيش الأمريكي لم يشارك في الهجمات على إيران، وترامب لم يأمر بأي عملية دعم للدفاع عن إسرائيل من هجمات الصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/77743" target="_blank">📅 15:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b316f312.mp4?token=lsAV3KmVAB3ED62K2r8XzMohOruWXha0TozZ20eD4RP15Ixuqpholh4o3d_B5MB0KW_8u9haHOkRIcdC0Fb1WvbVcc_UfkerWYp-2p_ABo1Xk-fNxLFX9e17diRsdKwKsdZvSBYU1n46B4aKAgeOGsPOR8elqOlnHSx6ncAmlzhCTagF-ghnPEXtpPcPuTY2GD94N5MZ_T_Pp9bwTDv5Xxcy5a7KMUGKfH0kISPv4xtKfny3joFTkmtPXsY0GVq8WOKUSPXQMtPOERPwuVf3zfQ5-JfhQ2Oh4cgsjpaoKjEhwWz6uDu1PxQVgjkLg9I4Q-JsKD1rmXibWyOsrj_e3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b316f312.mp4?token=lsAV3KmVAB3ED62K2r8XzMohOruWXha0TozZ20eD4RP15Ixuqpholh4o3d_B5MB0KW_8u9haHOkRIcdC0Fb1WvbVcc_UfkerWYp-2p_ABo1Xk-fNxLFX9e17diRsdKwKsdZvSBYU1n46B4aKAgeOGsPOR8elqOlnHSx6ncAmlzhCTagF-ghnPEXtpPcPuTY2GD94N5MZ_T_Pp9bwTDv5Xxcy5a7KMUGKfH0kISPv4xtKfny3joFTkmtPXsY0GVq8WOKUSPXQMtPOERPwuVf3zfQ5-JfhQ2Oh4cgsjpaoKjEhwWz6uDu1PxQVgjkLg9I4Q-JsKD1rmXibWyOsrj_e3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكثر من 5 صواريخ تدك مستوطنات الشمال</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77742" target="_blank">📅 15:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صفارات الإنذار تدوي في كريات شمونه ومحيطها بعد هجوم لحزب الله</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77741" target="_blank">📅 15:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صفارات الإنذار تدوي في كريات شمونه ومحيطها بعد هجوم لحزب الله</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77740" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قائد الجيش الإيراني: نحذر بأن أي اعتداء من جانب إسرائيل تتحمل مسؤوليته الولايات المتحدة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77739" target="_blank">📅 15:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏اعلام العدو عن مصدر إسرائيلي: نتنياهو يقول إن الاتصال مع ترمب كان "توافقيا" بالمواقف</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77738" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
وكالة تسنيم:
معادلة جديدة لإيران.. إيران وافقت على وقف إطلاق النار بمعادلة جديدة وبشرط؛ حيث أعلنت إيران أنه في حال استمرار اعتداءات إسرائيل أو استمرار جرائم إسرائيل وأمريكا في لبنان، لن يقتصر الأمر على بيروت فقط بل حتى جنوب لبنان، وسيُستأنف الأمر مجدداً وسترد إيران برد أقوى.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77737" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDRDSd5-lEqomaNf0wDvAQJKpRXKLYMqsW-Qa4t2va0epDW5HelUtZ9eK5UTP8M987q3_dxZWKhKGYhQaAUAzqA1vVoNLOIJBfUC23kZGtzMVD75s0pve6jPwZNXly7GRgn66J1YJEkSu-9lf3sBv1ki0a3fI-o0vAHZ4dP01VdNbaJ_Joy3EipN_pmiHpft6ezPFPwkurYamsHfbfCHy2rWSih4h-V6-K0FNka1eTuUyVcd3Bhs9DQpnnlmtpChflVN3Ctha8aGYWK3E2mlyFUZs73cknGzYRTdV-HlrBZdShEx1EAMPtlzPr4c6vA2-8JRKTB7PozoK6A37AuXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غارات صهيونية على جنوب لبنان</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77736" target="_blank">📅 15:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سلطة الطيران المدني العراقي تعلن إعادة فتح الأجواء العراقية أمام الرحلات الجوية من وإلى جميع المطارات العراقية واستئناف الحركة الجوية فيها</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77735" target="_blank">📅 15:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f58b1745.mp4?token=jFP1uW9JSXlG63p3mmHk3PV7Cl1H1wiwlvUQLRIfL7ajeggbznjnnSEU9nz632yHbzeLlUqC0qsEFVvNbafrjW5g0L70zSYBEhPy8oM2k4OrJM_4J-K7g0RbX6V8xLFt8iDuVJ7dXWCHYU-ylbtfZVknj923aJy2sugY_MxaEn8wDGV7cPfJiFkmahztYabFLoZNvxas_2Et3BjT-H4_T99rvMrCe-Pn-j7gtFUtSbNTdwjFevsIJO59rPYt1-eaS_ibxMWtlmcJcSBGCl64LB2nX30elqT22B67vEsMFfFZYSPHrUX1RQUQSO9ktrPID6ezfMwhJtfyHKZvOLo_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f58b1745.mp4?token=jFP1uW9JSXlG63p3mmHk3PV7Cl1H1wiwlvUQLRIfL7ajeggbznjnnSEU9nz632yHbzeLlUqC0qsEFVvNbafrjW5g0L70zSYBEhPy8oM2k4OrJM_4J-K7g0RbX6V8xLFt8iDuVJ7dXWCHYU-ylbtfZVknj923aJy2sugY_MxaEn8wDGV7cPfJiFkmahztYabFLoZNvxas_2Et3BjT-H4_T99rvMrCe-Pn-j7gtFUtSbNTdwjFevsIJO59rPYt1-eaS_ibxMWtlmcJcSBGCl64LB2nX30elqT22B67vEsMFfFZYSPHrUX1RQUQSO9ktrPID6ezfMwhJtfyHKZvOLo_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77734" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77733" target="_blank">📅 15:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU_LA3xYbMUBCmk3glOB1OM3AG64S21vYGzymfEHHPrw8RMtTtK-q53aOYSSr7eUELymhhnCLho3slILnMA-zvKVgxJ7kVWbxxDf65eW7l4cgRJDUb0IBGW7X0XcBbzZhXrBRnGAStTgROgpFGfFVrbYu38VQj6bd_DKeB443TIubxM6nYGMRNxR186FubbTu_DRvHKHejW3wtaivOuemQErd3SOwESyynRpzXWpsjNS10w929UvudinCvOQr9UTFSUNuNgyVYVr9i4iHG_6W3xczFcpwzW8oiLeAvTdTNETAWF5TFwCKkNcm0ixlJPq_RJ5KhCzp7mDfUrmvSTTAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة اماراتية تهبط في مطار مهرآباد الايراني بعد حصولها على تصريح خاص رغم ايقاف المطارات الايرانية منذ صباح اليوم.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77732" target="_blank">📅 15:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77731">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
🏴‍☠️
اتصال هاتفي بين ترامب والنتن ياهو</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77731" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1_dzMA70EzWRLBu8K13GdhuLfWEoQ30Hd6NGcGcAmvXDNoTcSxX_gb6PlF0Z5FMDmydUQVNNAVi6R03q6Uiz29n2uAKxEUE6vl27vkrAKvOsAgv9kC2RbheRvRqQTRlqcQ4qL1-eFMdX4WEc-qKGwCgVE4uEzGxKRnR7TjnuMtnnnr3jiEWytlvkxcRmNnWrmn6y0y2tFxA3TvX1q4HMF-zpIsmAMCebGyG9Oc7r2_ECstQPnQWI8edHOlLoBRKSSavDpR12pSMuSsZovJJS0XLK0MNHTAekWPzCda2TU7da-P3_Zq4odJaBXMfewVCO3o49ZksCG3hXcmtJy2edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
أولويتنا هي الأمن القومي وسلامة الشعب. سندافع عن حقوق الأمة بكل حزم ولن نتراجع أمام أي تهديد. الدبلوماسية والدفاع هما ركيزتا القوة الوطنية؛ لم نتخلَّ عن ساحة المعركة ولا عن طاولة المفاوضات. بإذن الله، بالوحدة والعقلانية، ستجتاز إيران هذا الاختبار بشرف.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77730" target="_blank">📅 15:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سلطة الطيران المدني العراقي تعلن إعادة فتح الأجواء العراقية أمام الرحلات الجوية من وإلى جميع المطارات العراقية واستئناف الحركة الجوية فيها</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77729" target="_blank">📅 15:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اعلام العدو:
يبدو أن: في ساعات المساء من المتوقع أن تعلن قيادة الجبهة الداخلية عن العودة إلى الروتين الكامل في الجبهة الداخلية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77728" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اعلام العدو: كانت معادلة إسرائيل هي إطلاق حزب الله النار على الشمال - هجوم في الضاحية
تحاول إيران تغيير ذلك إلى هجوم في جنوب لبنان - هجوم إيراني على إسرائيل
الإيرانيون استجمعوا الشجاعة ويشعرون بالتفوق</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/77727" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
القيادة المركزية لمقر خاتم الأنبياء المركزي يعلن وقف عمليات القوات المسلحة
في أعقاب الاعتداءات والأعمال العدوانية التي نفذها الكيان الصهيوني في جنوب لبنان ومنطقة الضاحية، بدعم من الولايات المتحدة، قامت القوات المسلحة القوية التابعة للجمهورية الإسلامية الإيرانية، في إطار دعم الشعب اللبناني المظلوم، بتوجيه رد مؤلم لهذا الكيان.
ردٌّ كان ينبغي للكيان الصهيوني وحلفائه أن يستخلصوا منه العِبر والدروس.
وبناءً على ذلك، يُعلن وقف عمليات القوات المسلحة؛ مع التأكيد على أنه في حال استمرار الاعتداءات والأعمال العدوانية، بما في ذلك في جنوب لبنان، فإن إجراءات أشد وأقسى وأكثر حسمًا من السابق ستكون في الطريق.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77726" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">📰
أكسيوس عن مسؤول أمريكي:
واشنطن لم توافق على الضربات الإسرائيلية على إيران وأبلغت نتنياهو بضرورة إنهائها</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77725" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اعلام العدو:
إسرائيل والولايات المتحدة أرسلتا رسالة لإيران: لن تكون هناك هجمات أخرى إذا لم تطلق إيران النار مجددًا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/77724" target="_blank">📅 14:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رئيس الوزراء البريطاني ‏ستارمر: على جميع الأطراف العودة إلى وقف النار، يجب منح المفاوضات بين أميركا وإيران فرصة للنجاح من أجل سلام دائم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77723" target="_blank">📅 14:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
🇺🇸
السفير الأميركي في لبنان:
إذا أوقف الحزب هجومه على إسرائيل فهي لن تستهدف الضاحية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77722" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
النائب الأول لرئيس البرلمان العراقي يدعو الحكومة إلى وقف تحويل الأموال لإقليم كردستان لحين إجراء التسوية الكاملة للمستحقات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77721" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴‍☠️
وزير التربية والتعليم الإسرائيلي:
استمرار تعطيل المدارس غدا الثلاثاء.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/77720" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ما يسمى بـ"المدير العام للوكالة الدولية للطاقة الذرية رفائيل غروسي": المطلوب من إيران الوفاء بتعهداتها والامتناع عن النشاطات غير المشروعة</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/77719" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عضو الكابينت زئيف إلكين:
ترامب يريد الهدوء، لكنه يدرك أننا لن نقف مكتوفي الأيدي إذا واصلت إيران مهاجمتنا</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77718" target="_blank">📅 14:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvT9q-v7tB1CzyGiYaVGJo0HkJyN_Ca9mneHUYbabLxHl6nfmorPCZLA2mmzRYZgZah56BXZ5vUKH2X1gaHBytX6gx7yJoCfijbKFll43n30Uw_-loJ0vUaVpVxLu3QfbQc8cciiwnqDRsdb7s8-bRLHfid-zwt56BgSWKGBxO_AHi2ZKYyA4Cae2dZRVBuWm2bIwcLJC6oU-lyEQL1Ehy_LxedeEMljUdTtCmZ6AjksKznIzOIeWzfUdUAuJV-mUdvMN4jxF2ttuFHv4aL1I3LBsSj3zpT1SfbpsE6qx4cICVTe03P49RWhG-16NWumuwkvL4ciFtZpB0R5uKfkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: يسعى كلا الجانبين، إسرائيل وإيران، إلى وقف فوري لإطلاق النار! المفاوضات النهائية بشأن "السلام" جارية، مع مراعاة احتمال عرقلة الجهل أو الغباء لها. سيظل الحصار قائمًا، وبكامل قوته وفعاليته، حتى يتم التوصل إلى "اتفاق نهائي". يجب أن تسير الأمور بسرعة.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/77717" target="_blank">📅 14:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">المتحدث باسم جيش العدو: النظام الإيراني يحمي وكلاءه في لبنان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/77716" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نقلا عن إعلام العدو ستجتمع الحكومة الصهيونية هذا المساء في الساعة التاسعة.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/77715" target="_blank">📅 13:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حركة حماس:
نثمن عالياً الرد الإيراني واليمني على الكيان الصهيوني جرّاء جرائمه بحق لبنان وشعبه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/77714" target="_blank">📅 13:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">إذاعة جيش العدو:
منذ حوالي الساعة 7:00 صباحًا، لا توجد معلومات عن هجمات أخرى نفذت في إيران خلال الست ساعات الماضية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/77713" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77712" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f3eaf5f3.mp4?token=kf3f4GYFLwyL_RpeH-tjgDjvwKD8l8dBxw-77X1LV0uC_F3b6-TDKru8y_nQMdapEttIrNRz4-S4ti7KOR4ARwoVMU4k2RuGQeJADVaBTBEgKiV5O-Upf7qz5ah8S47ZH9E8lMvHLNetg4mXqBE6Bu1KKKhcQBOTPAoxpnL-pwpyGIE927hTM1vupJF8jvqAElt1NkwJnhN-EsvgEmLQLYahVtS7gMoVe8iA5qg1Fy2cuq9mfeDvyPsKkRJvXsLzWl2TMlraopOcv4dN4RKi4cV-uWAAQPrAXOX31Dtai4soF6NqcRTqeNT5Y-mPHaE0zo58NUSaSA-m9ApIYsLIlIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f3eaf5f3.mp4?token=kf3f4GYFLwyL_RpeH-tjgDjvwKD8l8dBxw-77X1LV0uC_F3b6-TDKru8y_nQMdapEttIrNRz4-S4ti7KOR4ARwoVMU4k2RuGQeJADVaBTBEgKiV5O-Upf7qz5ah8S47ZH9E8lMvHLNetg4mXqBE6Bu1KKKhcQBOTPAoxpnL-pwpyGIE927hTM1vupJF8jvqAElt1NkwJnhN-EsvgEmLQLYahVtS7gMoVe8iA5qg1Fy2cuq9mfeDvyPsKkRJvXsLzWl2TMlraopOcv4dN4RKi4cV-uWAAQPrAXOX31Dtai4soF6NqcRTqeNT5Y-mPHaE0zo58NUSaSA-m9ApIYsLIlIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لبنان لن يصبح لقمة سائغة للصهيونية أبدا وأبدا
الإمام الشهيد القائد علي الخامنئي</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/77711" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77710">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دك سفينة هندية بمسيرة قبالة بحر العرب</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77710" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77709" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">المتحدث باسم مقر خاتم الانبياء:
- كما وعدنا، أثبتت القوات المسلحة الإيرانية الجبارة، بما فيها الحرس الثوري الإسلامي وجيش الجمهورية الإسلامية الإيرانية، أنها في ذروة استعداداتها الدفاعية والهجومية، تحركت بسرعة ودقة، مما جعل العدوين الأمريكي والصهيوني يندمان على ما فعلاه.
- في الموجة الجديدة من العمليات ضد أهداف مهمة وحساسة في الأراضي المحتلة، تلقى العدو ضربة قاضية من القوات الإيرانية الجبارة، حيث سددت ضربات قوية وموجهة وذكية ومدمرة.
- على أمريكا المجرمة والكيان الصهيوني الوحشي أن يعلما أن إيران قوية شامخة، وأن قوى المقاومة الشريفة في المنطقة ستصمد في وجه أي ظرف وأي تهديد، ولن تستسلم أبدًا للأعداء المهزومين، وإذا استمر العدوان والشر، فسيكون الرد أشد قسوة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/77708" target="_blank">📅 13:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIy4O-MznsmDzXI21eIGQOgdf-dRfoparxW9m23Gx91BhvwChgXQ454fTZZaAncJMAibS7VJQBa5L_mMNaBvWke0dvGgBFpIj7l6bsVe9-eoqvN1Qclsu6rw0h9Roi3VnweFjls350_9F9TYArrfRLioJIDFdAfrcUiQ6jUu8yLx17rcynbE-8qoJ7bZf3b6qDUsugg3orqiBh1DUEucNBMcOv5fs2Wew5ruBe1ksPxdCw54_wxxKhSHPh0m3cEugunxS2Ty9g5fbzTpKO1KywanERbBdRBnYSM7Vve5eRaskU91N3Ex5ebJqsoyAW7S0mbyMvbBuMG0jNDtEFNhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Bab Al mandab are close soon</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/77707" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77706">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxjvesDsUTyBGYAPxlgDdV-ap3k6iabc0j2xuLPSqx8PIS5CgPv62CuezE1gLARNSI18QwMB2Y08vsDsCCWZRisU_8f40M_BPAMXuJSo9c2cRp_xGb1HDOrIRdt6RJVoR6cNcrg5JmW_6pVuZCGuJFi3J61rBWdfWFswhV0Y6LOh5dQxrKVJRk0t2ELyemm_WOj7G_PiLKyHVWpTpV1bTUvhkaz9NhNM96kJuO9znv388Ujpvn2ZgAhP9Dth66O5PKd9uIuysCBoRIQs_eUyCl4fwfJmNM3tpSwz03BFJsM_G5chLWpbflhRHdO61nNT24mDS8P0wx8VQrx2BVoRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
التخوف حاليا في ايران ودوائر القرار العسكري هو إذا ما قرر الجيش الكويتي الدخول بالحرب .</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/77706" target="_blank">📅 13:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77705">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
القائم بأعمال وزارة الدفاع الايرانية:
الكيان الصهيوني بات اليوم أقرب من أي وقت مضى إلى الأفول والانهيار، لن نتراجع لحظة واحدة عن مسار الدفاع عن مصالح البلاد وأمنها حتى معاقبة المعتدي</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/77705" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
