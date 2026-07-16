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
<img src="https://cdn4.telesco.pe/file/RtosBiRHBQXfuJf3ZjeeT2EgpGzcI_WNTkhjpilfTh0tyFVSZW1NUN1PssDY5DP811ESE2TC41e6UFAetSAPxknH7PkwmA7ZtEC4ri7XNO-8lO9vRVQ8mZPPWu-PWFhiMvXmkIe-RrGbZ0ZDDmbGrCLqdUdQS85w2HHje9HwWo8VnbEHLl2VsI3k5UjV8Onon-7APObhieV7kkZ2tQG-DWUUdbcDTfIO3GLO5PdyHAJk3nnxssuFuZPPlCbsDIfu3Ibg9c2G2JVpzgsRXCTstJ5DkhjaircDuIGty7nB_STLk_8oPW2GOGW-_sztB4V6MpItGe39Si3FVLYAN-5UeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 263K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-83399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25f11c333.mp4?token=rtvLlXh_5X-5nDgh2eWxjIrC4R_PlPQG1LbIxJaCAafHd82d8NuXYji459vdDTodxLGXGANcv5_V3ni7j6ATEHaGUbh7-RdPHKrxt5eC_lH-VCQAL_nYvv8rGEpCdHumpw175lukILs9Kjr7DPGFQaOLgc9TNul41CyvVtHBDiXVOFnux6yb2o5yyLrG6YVCqnSlfGemIxMI8nwq0WG0VqBGyv5p7avfhfGFqLHYINNJlC0Ba7u7v4gukBnfO0lXl2S02GHpEpMQiar4biQaPrZnxVdGbr_Gk813KWrbK-jFskDuOjgL_vRP6AsasO-9E6Weg8hs5hCcUdZ-op9asA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25f11c333.mp4?token=rtvLlXh_5X-5nDgh2eWxjIrC4R_PlPQG1LbIxJaCAafHd82d8NuXYji459vdDTodxLGXGANcv5_V3ni7j6ATEHaGUbh7-RdPHKrxt5eC_lH-VCQAL_nYvv8rGEpCdHumpw175lukILs9Kjr7DPGFQaOLgc9TNul41CyvVtHBDiXVOFnux6yb2o5yyLrG6YVCqnSlfGemIxMI8nwq0WG0VqBGyv5p7avfhfGFqLHYINNJlC0Ba7u7v4gukBnfO0lXl2S02GHpEpMQiar4biQaPrZnxVdGbr_Gk813KWrbK-jFskDuOjgL_vRP6AsasO-9E6Weg8hs5hCcUdZ-op9asA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر تدمير بطارية صواريخ باتريوت امريكية في مطار أربيل بعد هجوم يوم امس</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/naya_foriraq/83399" target="_blank">📅 17:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
اعلام العدو:
المصادقة على توصية للمنظومة الأمنية بالإبقاء على حماية بنيامين نتنياهو وزوجته طيلة حياتهما، لا سيما في أعقاب اغتيال القادة الإيرانيين الذي ضاعف التهديدات الأمنية.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/naya_foriraq/83398" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📰
رويترز:
يتم تجهيز القوات الباكستانية في السعودية للذهاب لمحاربة الحوثيين.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/83397" target="_blank">📅 17:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
السيد عبدالملك الحوثي:
السفير السعودي في لبنان يوزع أموالا مغرية لمسؤولين وشخصيات لبنانية لشراء مواقفهم بالخيانة لشعبهم ومعاداة حزب الله.</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/83396" target="_blank">📅 17:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
لجنة الأمن والدفاع النيابية العراقية توصي بإقالة اللواء مازن عبد الواحد كبيان، قائد القوة البحرية، ومدير العمليات، وإحالتهما إلى القضاء، على خلفية حادثة الصيادين والتجاوزات الكويتية.</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/83395" target="_blank">📅 17:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سماع دوي انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83394" target="_blank">📅 16:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f066b021.mp4?token=K4E9w5L3Egpc_nepgTgDfou4eIlpnoS1NGqJBDSBa0sIk6pRvjO4Q7Mglw1yAYo4fCj4lzrBfjqgqNjMhEIIbUzeBNPgjvMDDD2VKDV_dM0uFJEae1wM4h0tqM7TttmKqx8GG7-cFiROm2Bb04ZKuBAb9froI7fgk_finiSRTNbhgNEtVj1AjwkGg9aYlT3-KM7Fuz8ygS9FrwQMYF0Js-6tI0tBk9Q5d_6kNljI2O5ko_NDzhCFlgSnzZibczPOgBqw-KR2HrOncImebHSZfTAjrvWBG_nUfqNDHIjN1ZtigaTG-82R4EwTGyz5RascoCkLqRb14s0PnnFUoT0C5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f066b021.mp4?token=K4E9w5L3Egpc_nepgTgDfou4eIlpnoS1NGqJBDSBa0sIk6pRvjO4Q7Mglw1yAYo4fCj4lzrBfjqgqNjMhEIIbUzeBNPgjvMDDD2VKDV_dM0uFJEae1wM4h0tqM7TttmKqx8GG7-cFiROm2Bb04ZKuBAb9froI7fgk_finiSRTNbhgNEtVj1AjwkGg9aYlT3-KM7Fuz8ygS9FrwQMYF0Js-6tI0tBk9Q5d_6kNljI2O5ko_NDzhCFlgSnzZibczPOgBqw-KR2HrOncImebHSZfTAjrvWBG_nUfqNDHIjN1ZtigaTG-82R4EwTGyz5RascoCkLqRb14s0PnnFUoT0C5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⚠️
مصدر لنايا  الإمارات شاركت بالهجوم البارحة على بندر عباس وتم استخدام مسيرات إماراتية تحديدا على المدينة الإيرانية بندر عباس ، المصدر اكد لنايا ان الإمارات استخدمت لاول مرة ذخيرة متسكعة من طراز Yabhon Loitering وتم اسقاطها قبل ان تصل للهدف .</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/83393" target="_blank">📅 16:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
⚠️
مصدر لنايا
الإمارات شاركت بالهجوم البارحة على بندر عباس وتم استخدام مسيرات إماراتية تحديدا على المدينة الإيرانية بندر عباس ، المصدر اكد لنايا ان الإمارات استخدمت لاول مرة ذخيرة متسكعة من طراز
Yabhon Loitering وتم اسقاطها قبل ان تصل
للهدف .</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/83392" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83391">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
🇺🇸
دوي صافرات الإنذار داخل السفارة الأمريكية في بغداد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/83391" target="_blank">📅 15:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83390">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
🇮🇶
إغلاق منشآت الإنتاج الرئيسية في حقل كورمور بمحافظة السليمانية شمالي العراق بشكل مؤقت</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/83390" target="_blank">📅 15:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
🇮🇶
إغلاق منشآت الإنتاج الرئيسية في حقل كورمور بمحافظة السليمانية شمالي العراق بشكل مؤقت</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/83389" target="_blank">📅 15:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83388">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
🇸🇾
قيادة العمليات المشتركة العراقية:
​
بعد إحباط عملية تهريب أسلحة وصواريخ عبر الحدود العراقية نحو الأراضي السورية .
​نودّ الإيضاح أنه بتوجيه من السيد القائد العام للقوات المسلحة، تم تشكيل لجنة عليا من الجهات ذات العلاقة والمختصين للوقوف على تفاصيل هذا الموضوع بالكامل.
​كما سيتم التنسيق مع الجانب السوري لمعرفة جميع التفاصيل المتعلقة بهذه العملية ، ومحاسبة المقصرين بما يضمن الحفاظ على أمن واستقرار الحدود المشتركة، ومنع أي محاولات لزعزعة الأمن الوطني.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83388" target="_blank">📅 15:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83387">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇾🇪
🇮🇷
🇾🇪
رويترز: اتفاق بين إيران وانصار الله على إغلاق باب المندب بحال استهدفت أميركا منشآت الطاقة</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/83387" target="_blank">📅 15:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83386">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇷🇺
🇺🇸
نائب أمين مجلس الأمن التابع للاتحاد الروسي:
إن رغبة الولايات المتحدة في السيطرة على أسواق الطاقة أدت بشكل أساسي إلى التدخل في الحكومة الفنزويلية وبذل جهود ضد الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83386" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
🇸🇦
🇮🇶
🇾🇪
السعودية تقرر حظر حسابات عراقية ويمنية وإماراتية على موقع اكس " تويتر سابقا " بسبب نشرها حجم الضربات اليمنية الأخيرة على جنوب السعودية ، حيث أصبحت هذه الحسابات غير متاحة للمتابعة او الظهور داخل السعودية !</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83385" target="_blank">📅 14:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83384">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
الموانئ العراقية:
المسيّرة التي سقطت على إحدى الناقلات خارج نطاق موانئنا، عمليات التفريغ والمناولة مستمرة من دون أي توقف.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/83384" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83383" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83382" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83381" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83380">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
🇸🇦
🇮🇶
🇾🇪
السعودية تقرر حظر حسابات عراقية ويمنية وإماراتية على موقع اكس " تويتر سابقا " بسبب نشرها حجم الضربات اليمنية الأخيرة على جنوب السعودية ، حيث أصبحت هذه الحسابات غير متاحة للمتابعة او الظهور داخل السعودية !</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83380" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83379">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
محكمة جنايات مكافحة الفساد المركزية تصدر حكماً بالسجن لمدة سنتين بحق النائب محمد الكربولي، بعد إدانته بتهمة الرشوة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83379" target="_blank">📅 13:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83378">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇷🇺
😊
🇮🇷
الكرملين نحن مع تواصل مستمر مع ايران</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83378" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83377">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
وقف عمليات تصدير النفط مؤقتا في ميناء البصرة العراقي بعد استهداف ناقلة نفط بمسيرة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83377" target="_blank">📅 13:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83376">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb4f0a18c.mp4?token=QLf0hNyfsV3zOJ6LGEPNybNJv3GKGGO06imTi-1fHUuTuIJxJuUFs-FlkkI7cvnSYMNweZAqfiZhgdksonATethW_KPZTJaVhWH03lDIFRoy_jY39pnrugj3-aHm5sHH_WHASoIrwbKO3B0NPVJPfWqe8R_47Q1ms9w3llm1i5xxkEH9G-3w6MUltMe3Wq2hvqrpU7cBxLbewpJFwzxKzzwJ9ovNeDdsNOQLTRp_9hMRnjGxt4SsKEOuc3vefDvZCDTIeBYzbIDOfcrd2sJuFk83y9kvVfNYrZLEBMRYVe2Fv3tpYe44mHSVt_38Uun2rhWoo36MhT4HUP8QjYZ-6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb4f0a18c.mp4?token=QLf0hNyfsV3zOJ6LGEPNybNJv3GKGGO06imTi-1fHUuTuIJxJuUFs-FlkkI7cvnSYMNweZAqfiZhgdksonATethW_KPZTJaVhWH03lDIFRoy_jY39pnrugj3-aHm5sHH_WHASoIrwbKO3B0NPVJPfWqe8R_47Q1ms9w3llm1i5xxkEH9G-3w6MUltMe3Wq2hvqrpU7cBxLbewpJFwzxKzzwJ9ovNeDdsNOQLTRp_9hMRnjGxt4SsKEOuc3vefDvZCDTIeBYzbIDOfcrd2sJuFk83y9kvVfNYrZLEBMRYVe2Fv3tpYe44mHSVt_38Uun2rhWoo36MhT4HUP8QjYZ-6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
انتشار كثيف أمام منزل خورشيد الهركي زعيم قبيلة الهركي الكردية على خليفة اعتقاله من قبل قوات البرزاني في محافظة أربيل شمال العراق مطالبين بإطلاق سراحه أو إعلان الحرب عليهم</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83376" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83375">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI9fIeeT4au8sTb9BsOOwNRTlyRGeG06xOddiOeMEqtlTLmOWnMP01f5OzEek08gUfIkXq0NmvecR6YQ9a_IR0pLyy0NitYpcKIrll7rMpAqwZEHJprWMQu1Y1meB_stORkYpuvn7EA3NHwEoN3CkayY-FKfyjigGFtpTHpQQxnYFS050aJWyHJDjS1ZZPWCZdzQpT2E0vyZLWvKydLTmHEhZnoiRimeYLcPnAUW6bQt89VgfEjmBO_qgkZVAt_N4Q_nJBCVWcYR0EoSoIbALjxksPYvmUgahqfMFbdcMVyB_oIr4eIwiTgjhvUJWJ6kI22rNKj1yiTNWHLz3Qgpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
صحيفة بريطانية: أنصار الله في اليمن تستعد لإغلاق مضيق باب المندب، وهو ممر بحري عالمي رئيسي. حيث ستعكس هذه الخطوة استراتيجية إيران في مضيق هرمز، وقد تؤدي إلى تعطيل التجارة العالمية بشكل كبير من خلال إجبار السفن على تغيير مساراتها والتحرك حول أفريقيا.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83375" target="_blank">📅 12:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83374">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
سقوط طائرة مسيّرة قرب ناقلة نفط تحمل علم ليبيريا في ميناء البصرة النفطي ضمن المياه الإقليمية العراقية</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83374" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83373">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇸🇾
حكومة الجولاني الإرهابية تدعي إحباط محاولة إدخال ‏شحنة أسلحة نوعية وصواريخ من العراق كانت متجهة لحزب الله في لبنان.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83373" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83372">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
قام أبناؤكم الأقوياء والمجاهدون في القوة البحرية التابعة لحرس الثورة الإسلامية، خلال الموجة العاشرة من عملية «نصر 2» تحت الشعار المقدس «يا علي الأصغر (ع)»، بشن هجوم عنيف على القاعدة الأمريكية في الشيخ عيسى في البحرين، دمّروا خلاله بالكامل رادار كشف ومراقبة المجال الجوي ومحطة ضخ خزانات وقود مقاتلات العدو المعتدي، ولا تزال هذه المعركة مستمرة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83372" target="_blank">📅 11:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83371">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇱
جيش الاحتلال: العثور على جثمان في منتصف حقل ألغام على الحدود مع لبنان الجيش الإسرائيلي يتحقق من التفاصيل</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83371" target="_blank">📅 11:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83370">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات عنيفة تهز العاصمة الاوكرانية كييف نتيجة هجمات روسية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83370" target="_blank">📅 10:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83369">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83369" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83368">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83368" target="_blank">📅 10:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83367">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
قام أبناؤكم الأقوياء المجاهدون في البحرية التابعة للحرس الثوري الإسلامي، خلال الموجة العاشرة من عملية نصر ٢، تحت الاسم الرمزي علي أصغر، وخلال هجوم مدمر على القاعدة الأمريكية في الشيخ عيسى بالبحرين، بتدمير رادار الاستطلاع والتحكم الجوي والمحطة دُمِّرت خزانات وقود مقاتلي العدو الغازي تدميراً كاملاً، والمعركة مستمرة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83367" target="_blank">📅 09:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83366">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:  أيها الشعب الأردني الكريم والنبيل، في الليلة الماضية، ارتكبت القوات المسلحة الأمريكية، في تعدٍ صارخ، هجومًا باستخدام القواعد الجوية الموجودة في الأردن، مستهدفةً مناطق مختلفة في إيران، بما في ذلك محيط مستشفى لعلاج سرطان الأطفال. وقد…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/83366" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83365">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
🇮🇱
وزير الحرب الأميركي يُطلع وزير الدفاع الصهيوني على تطورات العملية العسكرية بإيران ويؤكدان على مواصلة التعاون بشأن الحرب في إيران.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83365" target="_blank">📅 09:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83364">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
المتحدث باسم الجيش الإيراني:
سيظل مضيق هرمز مغلقا ما دامت واشنطن لا تعترف بنظامنا القائم على سيادة القانون
السيطرة الاستراتيجية على مضيق هرمز أصبحت مطلبا وطنيا في إيران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83364" target="_blank">📅 09:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83363">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
أيها الشعب الأردني الكريم والنبيل، في الليلة الماضية، ارتكبت القوات المسلحة الأمريكية، في تعدٍ صارخ، هجومًا باستخدام القواعد الجوية الموجودة في الأردن، مستهدفةً مناطق مختلفة في إيران، بما في ذلك محيط مستشفى لعلاج سرطان الأطفال. وقد أُخرج 121 طفلًا مصابًا بالسرطان من هناك. هذا ليس أول جريمة ترتكبها أمريكا باستخدام القواعد المنتشرة في الأردن. ففي السابق، قُتل 168 طفلًا في هجوم أمريكي على مدرسة ابتدائية في مدينة ميناب. ردًا على هذه التعديات، استهدفت قوات الفضاء الجوي التابعة لحرس الثورة الإسلامية، في الموجة الثامنة من عملية "النصر 2"، تحت شعار "يا زينب الكبرى (س)"، منصة صيانة الطائرات الأمريكية ومركز القيادة والتحكم الجديد الأمريكي في غرب آسيا، الواقعين في قاعدة واسعة في الأزرق بالأردن، بصواريخ باليستية "خيبرشكن"، ودمرتهما.
أيها الشعب الأردني الشجاع، أنتم أكثر من أي أمة أخرى، تشعرون بجريمة أمريكا والصهاينة عن كثب. لا تسمحوا بأن تستخدم الأراضي المقدسة للأردن، التي هي مهد الأنبياء، في هذه الجرائم ضد الأطفال. استخدموا كل ما في وسعكم لضرب مصالح أمريكا، وطهروا أرضكم من الغزاة الأمريكيين.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83363" target="_blank">📅 09:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83362">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇱
هآرتس العبرية: غراهام لم يكن حقًا صديقًا لـ "إسرائيل" بل كان صديقًا لـ "إسرائيل مرتكبة جرائم الحرب"</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83362" target="_blank">📅 08:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83361">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecf157b56.mp4?token=FqQUjrnaGD-WO-lyjt-cxppXIYU6cFPVBClZX5T7dhCzF9vjdOTW9V3mzKqFmywn8Pr7uUt2R243Ye3a9bT5HjmjqrqDar_T8lfN0Q2B5-UfaAEBtgnp71lhRy-92zgDDoZo3kV18nISbkGhCLh828-IetjouEzpoaorPcdd-_MI8ZUbi188OAPdBtWeQT85I_JnBnYIKAPzHWvi2BFbPexBhW6QDI8jPgL8sDryB1C-4zhp0B3DW9SJUaGcqbWdh0VPYY8iGwhQJPC6v07BeQWo0sVmRkxrmuL_BJnjf1KLqNN2bg2MsIoX7mI49cFLkTvjCCaaiKPxyoI4zOgL2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecf157b56.mp4?token=FqQUjrnaGD-WO-lyjt-cxppXIYU6cFPVBClZX5T7dhCzF9vjdOTW9V3mzKqFmywn8Pr7uUt2R243Ye3a9bT5HjmjqrqDar_T8lfN0Q2B5-UfaAEBtgnp71lhRy-92zgDDoZo3kV18nISbkGhCLh828-IetjouEzpoaorPcdd-_MI8ZUbi188OAPdBtWeQT85I_JnBnYIKAPzHWvi2BFbPexBhW6QDI8jPgL8sDryB1C-4zhp0B3DW9SJUaGcqbWdh0VPYY8iGwhQJPC6v07BeQWo0sVmRkxrmuL_BJnjf1KLqNN2bg2MsIoX7mI49cFLkTvjCCaaiKPxyoI4zOgL2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تظهر صور الأقمار الصناعية أضرار كبيرة جداً جراء القصف الإيراني على سطح أحد الفنادق التي يمكث بها قوات الاحتلال الأمریکي في الدقم بسلطنة عمان.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83361" target="_blank">📅 07:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83360">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtfM8Oo1dWkPiSThPnJ2N9-bnnJbboze8s8k0K6E3UdKr9urp-b_u1z4t47t0V_dxaq0lSQuh1ybgnPjkazJb47QNEYWIZjr4YqIn7G8pnITi5soo0d0JmbTlqFcVAUeDgS-0MH-IXqHn1ZT_W9C8uVZHd_OspO_-DtyS6fjqpB9Gglg6msVYngXaScI2JYelLpRTGcaBJ3Me_119HRF-Pa8FcMqfai0XwWM1ZudT4Db_wDU6l4wMT6uflipkzaN_SpV_qd04joaFCTSSg5dhV48OKXdCPzD7Rq0uJKsL03fxq0wfvAGGpzS2XSwe8JU-FOUPTkNah_J4N54J0HErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ناقلة الغاز الطبيعي المسال "مبارز" المملوكة لشركة أدنوك عالقة في نفس المكان بمضيق هرمز باتجاه الطريق العماني منذ الأول من يوليو بسبب تحذيرات الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83360" target="_blank">📅 07:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83359">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
أصوات الانفجارات في خرم آباد كانت نتيجة إطلاق صواريخ نحو المصالح الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83359" target="_blank">📅 07:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83357">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الأردن: تعرضنا لهجوم جوي ب 8 صواريخ استهدفت الأراضي الأردنية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83357" target="_blank">📅 07:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83356">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In3c_6czrefnXHCrbopMwt79VmZlP8_p0RIvLLXlby4PXmHEplrwrON0kG65yPFaK77bjplvH9uWiMd2Ilb4vBHznDdcK00XF5Jevg-pElEqMh2CFFJjKSaPtUPVJGC5G8p3HAU2blzw285mCGeyP-EYyRxV9o9gi-pSLSQDw5iuifF61-NV5A3nESwYQog91QaEC0poBJfbPAOxg3v1-jI2kaUHn9OEH6R4jD5w9a_lCEBVvManoGQm7GM8L2rMpRSx1GLZy9cbcJrUMjj-MFQqjKtgOYerXAgArO9G-owSYjdAUXUgiFZ-irfcZCVs5P2opqFKjtrakGN-VSIANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇴
تحليق طيران الإنذار المبكر الأمريكي بشكل مكثف في سماء العقبة الأردنية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83356" target="_blank">📅 06:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83355">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a1959f42.mp4?token=tXgsAPCAuelGlvxbd19-L1HgUhwz4vhWaTuAM9h8SA1NWY2BXDf8lX45L9IKeMDd2FlvATTaGTOfwf_kBmGCmNK-IfBYrQwqgvVQ9CpeWaEXCEvnsHca-nDzIPyuiqhbhjOWfU3KEuhj5m-ZxOfKesYbhLLFxdCOCcCz51h2Su4zLe-pWwFyBk1XdSGcs6ut6U-EHfk_EOLEUSQAxtmcbpWqdn9oFrVDHPu3xkrhFztRmSP2vN8-9FXaKU_x16Aa2dCKzNvaPztJPyJnjhtYFsDgK6qrhYhSNhjPP8c81wpiH7yurFwNelgR9TrAj3Wc8gl2o3pw5X_ZGRPJktSl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a1959f42.mp4?token=tXgsAPCAuelGlvxbd19-L1HgUhwz4vhWaTuAM9h8SA1NWY2BXDf8lX45L9IKeMDd2FlvATTaGTOfwf_kBmGCmNK-IfBYrQwqgvVQ9CpeWaEXCEvnsHca-nDzIPyuiqhbhjOWfU3KEuhj5m-ZxOfKesYbhLLFxdCOCcCz51h2Su4zLe-pWwFyBk1XdSGcs6ut6U-EHfk_EOLEUSQAxtmcbpWqdn9oFrVDHPu3xkrhFztRmSP2vN8-9FXaKU_x16Aa2dCKzNvaPztJPyJnjhtYFsDgK6qrhYhSNhjPP8c81wpiH7yurFwNelgR9TrAj3Wc8gl2o3pw5X_ZGRPJktSl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
طيران مسير يحلق نحو الأهداف الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83355" target="_blank">📅 06:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83354">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c8fa0dc1.mp4?token=t8PmENCF-IsI4kuK-KOF3HoW6VtK0bQ8ef7dXEkS5-u5GdUyZrHP6_Vr1KmMyQhHW6keaelMb0Ai693xP8EbWsTb_tg-7nfxqh-Asj_GbyZkJt2HXmjgwLDtVW5LQl09hEQ2kloJw8y9FVzkYW9Ed7rI9X-k_5TyOjU1G9Ck7fX_fZBZFqV_6IcVQik3jUa0XrPf887JbFhHMMES2J8cTh0gleSzFRl9qKpcQ_PHqNlhwVZBdBpRx7_J5JGvmFEJeCvyuh_zblhG9P4YKFFHiSkufGM-UNFNMoqu6YfxcGGTVHaLhF888gJQCxGSAyzfRBisv4-6ZMgP1UkLDdvhzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c8fa0dc1.mp4?token=t8PmENCF-IsI4kuK-KOF3HoW6VtK0bQ8ef7dXEkS5-u5GdUyZrHP6_Vr1KmMyQhHW6keaelMb0Ai693xP8EbWsTb_tg-7nfxqh-Asj_GbyZkJt2HXmjgwLDtVW5LQl09hEQ2kloJw8y9FVzkYW9Ed7rI9X-k_5TyOjU1G9Ck7fX_fZBZFqV_6IcVQik3jUa0XrPf887JbFhHMMES2J8cTh0gleSzFRl9qKpcQ_PHqNlhwVZBdBpRx7_J5JGvmFEJeCvyuh_zblhG9P4YKFFHiSkufGM-UNFNMoqu6YfxcGGTVHaLhF888gJQCxGSAyzfRBisv4-6ZMgP1UkLDdvhzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في المرحلة التاسعة من عملية "صاعقة"، وردًا على انتهاكات العدو القاتل للأطفال لمناطق في بلادنا وقاعدة "بمبور" في مدينة "إيرانشهر" الإيرانية، مما أدى إلى استشهاد 7 من ضباط وأفراد الجيش، استهدفت الطائرات المسيرة الإنتحارية التابعة للجيش الإيراني موقعًا راداريًا ثابتًا، ونظام اتصالات، ومخازن وقود تابعة للجيش الإرهابي والعدواني الأمريكي في قاعدة "الأزرق" في الأردن.
🔹
تعتبر هذه القاعدة موقعًا لنشر أنظمة الدفاع الصاروخي، وهي واحدة من أهم المراكز الاستراتيجية والقيادية للقوات الأمريكية المعتدية في منطقة غرب آسيا.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83354" target="_blank">📅 05:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83353">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/931b2b49bd.mp4?token=p-6orqXcepTvBtWwc9e-9m5VNNV53w7nEbzdVa2LVukVdFs30mSNTBog8BCpNC6A1k1ipJkf1PGFBdG_avcsDLkInHENANJvQyZcwtJgJEOAPoRRzOebZR6HnRQ3Ehnx9CBGfA7QcxBzlgbKwRh5eI3rHarR6OYDtWRV6dea0Riuk4xg4uV2UmQOxyZqmPctigo-T-Lp3liCNKarnSYE2dt1b_U_npyacleHPjylr3iu6VXEPbuQ9EdEMWnA92vg0hxwwfU402CE3g7XC1RLuCwFnCAc2SX8jWZDJJdYcL01ZsbMygf7nK3FS-BQg9682yILrX2HFecci7xQJ3JPlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/931b2b49bd.mp4?token=p-6orqXcepTvBtWwc9e-9m5VNNV53w7nEbzdVa2LVukVdFs30mSNTBog8BCpNC6A1k1ipJkf1PGFBdG_avcsDLkInHENANJvQyZcwtJgJEOAPoRRzOebZR6HnRQ3Ehnx9CBGfA7QcxBzlgbKwRh5eI3rHarR6OYDtWRV6dea0Riuk4xg4uV2UmQOxyZqmPctigo-T-Lp3liCNKarnSYE2dt1b_U_npyacleHPjylr3iu6VXEPbuQ9EdEMWnA92vg0hxwwfU402CE3g7XC1RLuCwFnCAc2SX8jWZDJJdYcL01ZsbMygf7nK3FS-BQg9682yILrX2HFecci7xQJ3JPlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
طيران مسير يحلق نحو الأهداف الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83353" target="_blank">📅 05:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83351">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3338462d70.mp4?token=sn3DlEK88Aoy8GU0EMAxqp5Ng3N3l0znODIfSMAEOx-cCYetgAbwxo3yI-aK5PYWnTC_NbG1fHyPwKjqbhRT7ZgSFHwDXKz51n7DM7iJTDGy3Fexl11FE3Q4SR-0LYJLQQ6Cx1GKu3608_SqdFG80kHiGAGPBGjagH8lyjXNG0lCdwvPM1Gpl8EH1ElkNrvyna5FP5fxX90bfmtBOMUIm_47RwecG3kwtJCLyIXU-PHTE0JJ7P7VOBs0bD9d8C8wNgKKysfFzH84V8BlLgfY2gq8H4lPg3yJ6OFeVNKRtt5cGwtbl-Yuz6W7jb1xWrL2IhoysW50HE7F7epthRODBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3338462d70.mp4?token=sn3DlEK88Aoy8GU0EMAxqp5Ng3N3l0znODIfSMAEOx-cCYetgAbwxo3yI-aK5PYWnTC_NbG1fHyPwKjqbhRT7ZgSFHwDXKz51n7DM7iJTDGy3Fexl11FE3Q4SR-0LYJLQQ6Cx1GKu3608_SqdFG80kHiGAGPBGjagH8lyjXNG0lCdwvPM1Gpl8EH1ElkNrvyna5FP5fxX90bfmtBOMUIm_47RwecG3kwtJCLyIXU-PHTE0JJ7P7VOBs0bD9d8C8wNgKKysfFzH84V8BlLgfY2gq8H4lPg3yJ6OFeVNKRtt5cGwtbl-Yuz6W7jb1xWrL2IhoysW50HE7F7epthRODBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تحديث_عاجـــــــــــــــل
🇮🇶
حادث سير مروع في محافظة البصرة جنوبي العراق، يؤدي إلى وفاة 8 وإصابة 17 أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83351" target="_blank">📅 05:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83350">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
حادث سير مروع على طريق زوار الإمام الحسين (عليه السلام) في محافظة البصرة؛ وفاة وإصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83350" target="_blank">📅 05:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83349">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
تم استهداف نظام الإنذار المبكر "C-RAM" في قاعدة علي السالم في الكويت، بالإضافة إلى موقع تجمع الجنود المجرمين في الجيش الإرهابي الأمريكي، بهجمات مركبة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83349" target="_blank">📅 05:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83348">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوي انفجار في محافظة سمنان الإيرانية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83348" target="_blank">📅 05:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83347">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
قبل دقائق، سمع صوت انفجار في منطقة مدينة باكداشت، وقد أظهرت التحقيقات الميدانية والعسكرية أن هذا الصوت نتج عن عمل أنظمة الدفاع الجوي في منطقة بارتشين.
مع التأكيد على نفي الادعاءات التي تروج لها بعض وسائل الإعلام المعادية والتيارات الملكية بشأن وقوع أي إصابات، نؤكد أنه لم تحدث أي حوادث أو إصابات في المنطقة، وأن هذه الأنشطة كانت تهدف إلى الاستعداد وعمل أنظمة الدفاع الجوي.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83347" target="_blank">📅 05:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83346">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682d31258a.mp4?token=EkvEcMztd9SPhw-260FFTgELO0IqpoEmn0O4hip9l_CjoQbtPW8ntvMo3y32jakryAhojVvSRD1nWeKngPiXvP1ZxUJGm9ASBRKCjlA3AWcR1TNLsIEXWw7eTwhUPK3WYtq9OpzkUv8x1o3pwbzQe8_TjD3LpDoAzXzmAVBWL16ojSC9twgXblGP6-gC_TCjY4hdG_phdgMJ5qndAreStkRN_UYZHKJ1V9fZwtZpe-KFiC8yUv7lcmSwoHBtIA0ss7Shyc2eH_2AbRfgDTgd1MsIaNWer3CZnlwvjdx9M7f-jCAq8rTs8-brSq7r0dka8jzglhvfaMYgYl0kksaoNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682d31258a.mp4?token=EkvEcMztd9SPhw-260FFTgELO0IqpoEmn0O4hip9l_CjoQbtPW8ntvMo3y32jakryAhojVvSRD1nWeKngPiXvP1ZxUJGm9ASBRKCjlA3AWcR1TNLsIEXWw7eTwhUPK3WYtq9OpzkUv8x1o3pwbzQe8_TjD3LpDoAzXzmAVBWL16ojSC9twgXblGP6-gC_TCjY4hdG_phdgMJ5qndAreStkRN_UYZHKJ1V9fZwtZpe-KFiC8yUv7lcmSwoHBtIA0ss7Shyc2eH_2AbRfgDTgd1MsIaNWer3CZnlwvjdx9M7f-jCAq8rTs8-brSq7r0dka8jzglhvfaMYgYl0kksaoNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجيش الأمريكي:
تامبا، فلوريدا - أنهت القيادة المركزية الأمريكية (سنتكوم) موجة من الضربات الجوية ضد إيران في تمام الساعة التاسعة مساءً بتوقيت شرق الولايات المتحدة يوم 15 يوليو/تموز.
وشنّت القوات الأمريكية غارات على مراكز قيادة إيرانية، ومواقع دفاع جوي، وأنظمة صواريخ وطائرات مسيّرة، ومرافق مراقبة ساحلية، بهدف تقويض قدرة إيران على تهديد البحارة الأبرياء على متن السفن التجارية العابرة لمضيق هرمز. واستخدمت سنتكوم ذخائر دقيقة لضرب أهداف في مواقع متعددة، من بينها بندر عباس.
وفي وقت سابق من صباح اليوم، شنّت القوات الأمريكية غارات على مواقع الدفاع الساحلي وصواريخ كروز في جزيرة طنب الكبرى، خلال موجة استمرت 90 دقيقة.
ويُحاسب الجيش الأمريكي إيران بناءً على توجيهات القائد الأعلى للقوات المسلحة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83346" target="_blank">📅 04:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83345">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">إنفجار جديد في مدينة خرم آباد غربي إيران.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83345" target="_blank">📅 04:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83344">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699eeb5e81.mp4?token=G4PIuoi2nmNLwx5vleD5Ym9qmuULIgEvASMbis-d1RUTbrth59zz8wpGqJ9JakN4Jwufh7nDgPagNPgA3W_IBhLLwqY4q1ESuO5tnKQF5fVii1FyRmKoHa-BujlbMJ8ugt7kq9XQwFkphsZjkMv-bTK7ZSnzTar1x2BWvfESmKcu9AhNouxeKLQ0Qs0rZgBdnkwdZcbnulahHLUEmXZGvTqZ9N9KurHBa9BRMT2d-5J5r6A7wolnB3o6UufBjIzRiZKQLIcHeCVzXd8Y6ec3QihfnxkdgwZfrP1Ae4oPvt12vomEyai-E1z8-qsXybMQJL-WlxaPfNsuoFM1fg-9FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699eeb5e81.mp4?token=G4PIuoi2nmNLwx5vleD5Ym9qmuULIgEvASMbis-d1RUTbrth59zz8wpGqJ9JakN4Jwufh7nDgPagNPgA3W_IBhLLwqY4q1ESuO5tnKQF5fVii1FyRmKoHa-BujlbMJ8ugt7kq9XQwFkphsZjkMv-bTK7ZSnzTar1x2BWvfESmKcu9AhNouxeKLQ0Qs0rZgBdnkwdZcbnulahHLUEmXZGvTqZ9N9KurHBa9BRMT2d-5J5r6A7wolnB3o6UufBjIzRiZKQLIcHeCVzXd8Y6ec3QihfnxkdgwZfrP1Ae4oPvt12vomEyai-E1z8-qsXybMQJL-WlxaPfNsuoFM1fg-9FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة وصول الصواريخ البالستية الإيرانية إلى القواعد الأمريكية في الأردن وفشل منظومة الباتريوت في إعتراضها.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83344" target="_blank">📅 04:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83343">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1df9afbf.mp4?token=pQMYYV87CNDaSbdqhGx1DJJXpBOU4gnztnrPTobYsrK5o745lJ3ypQ36FVpAZK5glIMHtTHeY0USPSZMCwYxpIWFMuzqZmsKPXJTCGWb_R9HzyF3SFCnBNndy6Uf8OOxr-pRF63PQHd-UcVbvuLVIeykRR94-v6IQxDsKwNOFuC6Ahhtd2-WXemgHB0APR0uoeOYkA1HU1_kX0TBPQinMOYcxbTNYObhfW5EZ1cJhjpCCGO0JwPwQ5NaUCjKt1iS8AqHXSoe8mFl1sa6ay-2xJcoze6n84LIjyzu00MY2ZRDqluHMBcFex_uG_xr50LPv_o1HkmFj5mWp4L7zsNGqrzT4Fb3HdnVfME8BReQ1q3rtbwgdbQd4OcZLNjDR-Qzq80l2AqSfDsUD9GJ73u9MXCr0RKJB9V3-ZHxtQTYXeVgyRTd0wHHbIo1QMsKilr1JAyvXJ-TeplyHFajiNGEMK9JMGmFjVRT4Q91en0q9DsYWPZBW_x2MKF3QkuZzOBIrHextobdkNIS8DiGdZeg_hY7z_9xd0HViUOpoZtN3YE8VKRUKomC5Nw8dv2jYWJhot1m-ssaXis_2Ds9DRdb9HLG5-HOqhGJRK8N9peiy0ZfKkmqjdGdfvFrC6sz9uUZ_FZJKk0Lq2cHA26_h3ZK_RwKrfw7X2SMEcAhAX5iLwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1df9afbf.mp4?token=pQMYYV87CNDaSbdqhGx1DJJXpBOU4gnztnrPTobYsrK5o745lJ3ypQ36FVpAZK5glIMHtTHeY0USPSZMCwYxpIWFMuzqZmsKPXJTCGWb_R9HzyF3SFCnBNndy6Uf8OOxr-pRF63PQHd-UcVbvuLVIeykRR94-v6IQxDsKwNOFuC6Ahhtd2-WXemgHB0APR0uoeOYkA1HU1_kX0TBPQinMOYcxbTNYObhfW5EZ1cJhjpCCGO0JwPwQ5NaUCjKt1iS8AqHXSoe8mFl1sa6ay-2xJcoze6n84LIjyzu00MY2ZRDqluHMBcFex_uG_xr50LPv_o1HkmFj5mWp4L7zsNGqrzT4Fb3HdnVfME8BReQ1q3rtbwgdbQd4OcZLNjDR-Qzq80l2AqSfDsUD9GJ73u9MXCr0RKJB9V3-ZHxtQTYXeVgyRTd0wHHbIo1QMsKilr1JAyvXJ-TeplyHFajiNGEMK9JMGmFjVRT4Q91en0q9DsYWPZBW_x2MKF3QkuZzOBIrHextobdkNIS8DiGdZeg_hY7z_9xd0HViUOpoZtN3YE8VKRUKomC5Nw8dv2jYWJhot1m-ssaXis_2Ds9DRdb9HLG5-HOqhGJRK8N9peiy0ZfKkmqjdGdfvFrC6sz9uUZ_FZJKk0Lq2cHA26_h3ZK_RwKrfw7X2SMEcAhAX5iLwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  إصابة مباشرة لصاروخ إيراني وسط قاعدة الأزرق الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83343" target="_blank">📅 04:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83342">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f70acdd19c.mp4?token=Yrcm_ttKo1PaxvL6INHNhiDujiy7WawdddJRzVKL4LjbDqLP4v4wsU19KrrBxzNFuP4ahXXL5PqKf3sYrGxVefOpVipY88it2JHdfajBwWO89UmOT-hBVDPJAcYftHZgoeA8iPwpK5QjPSMKkqLXiaVLJovt3zxhY-voyRcVpH-e5j4lbbxAGM5LPhdGuyJQv1oUfsHaas7oMgcPSNxLwODaUPgkFzlzr1RsACQF3UM9rrcufmyq6Nk2ALBH0YpT-dPzpAiCNHt8QS3Rdcc5pYMGtCb92BLMMA2ZaY7bQ0V5vOy6flxOHAA85Z8DLFHZ8TkUEJBAUk1YRJOCwG0VQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f70acdd19c.mp4?token=Yrcm_ttKo1PaxvL6INHNhiDujiy7WawdddJRzVKL4LjbDqLP4v4wsU19KrrBxzNFuP4ahXXL5PqKf3sYrGxVefOpVipY88it2JHdfajBwWO89UmOT-hBVDPJAcYftHZgoeA8iPwpK5QjPSMKkqLXiaVLJovt3zxhY-voyRcVpH-e5j4lbbxAGM5LPhdGuyJQv1oUfsHaas7oMgcPSNxLwODaUPgkFzlzr1RsACQF3UM9rrcufmyq6Nk2ALBH0YpT-dPzpAiCNHt8QS3Rdcc5pYMGtCb92BLMMA2ZaY7bQ0V5vOy6flxOHAA85Z8DLFHZ8TkUEJBAUk1YRJOCwG0VQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تخط سماء الأردن متوجهة نحو القواعد الأمريكية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83342" target="_blank">📅 04:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83341">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b485dbfa4.mp4?token=mB0abIz8GfpoUu-ap5xNXFPcFhXO_xhrq61nhKdkEfcUcLW-frPDzWMSL_zp6s3kpUMW8hqw9suBV5mdyLwk2H0tu3aCGJJIKGTfyxW2uEiyqrO-Tj6ls_tC6ivz-Xgr9fo1wxfw8FXwVPPOCj6LatmpHFpBzh3s1dVy8v5ES0JEf58yF5_b2dHrDKkg6_-guseENpMsGf1F1qWDN8WxvUAa2X6AXnRJLH9EwR5XlslUjBRW_lLutC3W4ZS5bYhK3M65_MmrAJou7ATdUUpaAB7uOwwqY_mZpS5gq0aEAydCdH8XHkfc83Yr-sc6vC9fciFcdG4b39eL-PdryET7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b485dbfa4.mp4?token=mB0abIz8GfpoUu-ap5xNXFPcFhXO_xhrq61nhKdkEfcUcLW-frPDzWMSL_zp6s3kpUMW8hqw9suBV5mdyLwk2H0tu3aCGJJIKGTfyxW2uEiyqrO-Tj6ls_tC6ivz-Xgr9fo1wxfw8FXwVPPOCj6LatmpHFpBzh3s1dVy8v5ES0JEf58yF5_b2dHrDKkg6_-guseENpMsGf1F1qWDN8WxvUAa2X6AXnRJLH9EwR5XlslUjBRW_lLutC3W4ZS5bYhK3M65_MmrAJou7ATdUUpaAB7uOwwqY_mZpS5gq0aEAydCdH8XHkfc83Yr-sc6vC9fciFcdG4b39eL-PdryET7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تشعل سماء قاعدة الأزرق الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83341" target="_blank">📅 04:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83340">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66689de9c.mp4?token=sSUv04VCOVesXx7kf-NaIQBzZGEhQdYBq0Kdfjm1mzsIP0sx1aER7boKhM8rI1y84go0w7r1eWSvSI6G4yT9MgRAG61DP0iZ2VQtMDhj0LW7VORnagXAwOTPWAXMO4bYfyzNdcNd0irXLfrX-92WdX82191pRbwSRXYsCrtX9f6B6wavJaxD2bTQzGoVkp65C7mcf9AMXiGgP4k4jbn1qrObSFPeZ6QfK8VCuAWDpIw8UA6ypPDLFsCA2PhQnoFCXwHPMm2Uu4MbUxAf1UjPqRTVdZj9OUcAVzYFS3j3_TV5s7JoZdfNP6XoXjuQ2GfMawJOssMEOpI63TlMMLiAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66689de9c.mp4?token=sSUv04VCOVesXx7kf-NaIQBzZGEhQdYBq0Kdfjm1mzsIP0sx1aER7boKhM8rI1y84go0w7r1eWSvSI6G4yT9MgRAG61DP0iZ2VQtMDhj0LW7VORnagXAwOTPWAXMO4bYfyzNdcNd0irXLfrX-92WdX82191pRbwSRXYsCrtX9f6B6wavJaxD2bTQzGoVkp65C7mcf9AMXiGgP4k4jbn1qrObSFPeZ6QfK8VCuAWDpIw8UA6ypPDLFsCA2PhQnoFCXwHPMm2Uu4MbUxAf1UjPqRTVdZj9OUcAVzYFS3j3_TV5s7JoZdfNP6XoXjuQ2GfMawJOssMEOpI63TlMMLiAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تنقض على القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83340" target="_blank">📅 04:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83339">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d4f9b9d4.mp4?token=C8JU_Q7fIFeL8Tk0y69u8JTPjiM294n0LrmHBnojmeQ7ZZIH2jaP_fROMY_5oD0MmjyN24pxqD3dE6dVYlfqX3lz8MYuE86jd4yZBXUOinueLYUSXghlG8dQy3sRDspEyqufpkWUpIUs8wl3UzsAsMlJQyq5pv019T-FtOsMbls85JLlxB6niyD6k0QsMjnsmxPOgHEX9_wmNr_cxIHscNm3CtSLA8PdKy-y8ITz5SC_BzbSbdwqBBDHrWHEvX5k9o7DJxyAUrhllW2qYVMzVZxOgXZk_Sl8srG1lC8wNSgnLZiorhP5iwRJjj6PvduGu_4M3GokpHaG-mXliS7MxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d4f9b9d4.mp4?token=C8JU_Q7fIFeL8Tk0y69u8JTPjiM294n0LrmHBnojmeQ7ZZIH2jaP_fROMY_5oD0MmjyN24pxqD3dE6dVYlfqX3lz8MYuE86jd4yZBXUOinueLYUSXghlG8dQy3sRDspEyqufpkWUpIUs8wl3UzsAsMlJQyq5pv019T-FtOsMbls85JLlxB6niyD6k0QsMjnsmxPOgHEX9_wmNr_cxIHscNm3CtSLA8PdKy-y8ITz5SC_BzbSbdwqBBDHrWHEvX5k9o7DJxyAUrhllW2qYVMzVZxOgXZk_Sl8srG1lC8wNSgnLZiorhP5iwRJjj6PvduGu_4M3GokpHaG-mXliS7MxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاعدة الأزرق الأمريكية في الأردن تحت مرمى الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83339" target="_blank">📅 04:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83338">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a85f96fd.mp4?token=mDyCTYnFnEsqbjq9Hohu34RvuTtG-Cxx9sY4WnJcNlqBq3jNGixBPUlxcYzMjDzmiehndO8MtT3I40_wkY7iqpSy8PZn6vOzCJZMYGAPnefVEe36DLRRdpadPJmgiMPF8yV9da0SyDFCAqvcXC10J5QDSTqTf2eO857graEnTqtB84_IxmZHamvFWK2Q_hANE5-b5PRmYawxp6Qsq-AaFCE3ZdaU6YhXLv-ExsaO7g19xf551R-94PYP_t1sM8FAIqz_mThclN5fDL3guiEb4gdy_a1hRO7KSs7pFjbe2dHWLxuMr-NX8s4oK01ckfoB9zj_1O1nQI6101cNZXwzRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a85f96fd.mp4?token=mDyCTYnFnEsqbjq9Hohu34RvuTtG-Cxx9sY4WnJcNlqBq3jNGixBPUlxcYzMjDzmiehndO8MtT3I40_wkY7iqpSy8PZn6vOzCJZMYGAPnefVEe36DLRRdpadPJmgiMPF8yV9da0SyDFCAqvcXC10J5QDSTqTf2eO857graEnTqtB84_IxmZHamvFWK2Q_hANE5-b5PRmYawxp6Qsq-AaFCE3ZdaU6YhXLv-ExsaO7g19xf551R-94PYP_t1sM8FAIqz_mThclN5fDL3guiEb4gdy_a1hRO7KSs7pFjbe2dHWLxuMr-NX8s4oK01ckfoB9zj_1O1nQI6101cNZXwzRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تدك القواعد الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83338" target="_blank">📅 04:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83337">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">إطلاق الصواريخ من إيران نحو القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83337" target="_blank">📅 04:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83336">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba26c1e726.mp4?token=bZ55MHJd9wdvriXAtxHSkzQx2Z3rl8sQuBpOIaqxJ6FVogGHLornGVBgP97Tlcj4Kg0uB0GGf-t0aontHq6o9gqFjWAvotW5AKeGq5Dy37C0FdpG_szwn-ZpNR6EaT-I0RHu_1T5b5idlIolUZ3P4GSup9DqRzjpNqG5yIgColIdzc-8NFK5uH8EVnqoi_hscQylyehqfauhKeAQ6g5dysvLEJlSgyW-BisWjZLO3e2Py_h4a0Dj1C92esg9vfGC5Jb8bibwHrx3rEoN4A33NMLDEn720TItdIt9eI0XA7syvfUltvCZdY1JZggRd7WoiJTKD_Pa4YqOGJGmrwFlBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba26c1e726.mp4?token=bZ55MHJd9wdvriXAtxHSkzQx2Z3rl8sQuBpOIaqxJ6FVogGHLornGVBgP97Tlcj4Kg0uB0GGf-t0aontHq6o9gqFjWAvotW5AKeGq5Dy37C0FdpG_szwn-ZpNR6EaT-I0RHu_1T5b5idlIolUZ3P4GSup9DqRzjpNqG5yIgColIdzc-8NFK5uH8EVnqoi_hscQylyehqfauhKeAQ6g5dysvLEJlSgyW-BisWjZLO3e2Py_h4a0Dj1C92esg9vfGC5Jb8bibwHrx3rEoN4A33NMLDEn720TItdIt9eI0XA7syvfUltvCZdY1JZggRd7WoiJTKD_Pa4YqOGJGmrwFlBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاعات الجوية الإيرانية تنشط بقوة بصد الأجسام المعادية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/83336" target="_blank">📅 04:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83335">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c763a60827.mp4?token=FJeLKemKrzgId9xCZzoaHMunD8fjRUOAN7uaZgjG-eR0UBhRDsCDLzhQl5jY_2lTcmiKYUiO5GlL4X9KjxMEqGL4KNgVPzKTLkVECFodtm1PKCBSNnt6WUlLBLkYrfG5O_MfF_SfQ39iUCPp3O9wjoMimzCxYO2bNwG2AGovSPjPMk1anmsV_4JtK4RCU8UqE4uNnegYdZ3k2q1ierjWTQR9nR2GMmm6sYWew350_kL86RlfhhYYfnlGCFjPBi6BABzmxSYGPENDcfUYoyil-gGsRjKWWv1Rprfi__P3u7gVO57yrP1CK1zBUS4s2Adp21YZCrAX_pSYqNGW5olOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c763a60827.mp4?token=FJeLKemKrzgId9xCZzoaHMunD8fjRUOAN7uaZgjG-eR0UBhRDsCDLzhQl5jY_2lTcmiKYUiO5GlL4X9KjxMEqGL4KNgVPzKTLkVECFodtm1PKCBSNnt6WUlLBLkYrfG5O_MfF_SfQ39iUCPp3O9wjoMimzCxYO2bNwG2AGovSPjPMk1anmsV_4JtK4RCU8UqE4uNnegYdZ3k2q1ierjWTQR9nR2GMmm6sYWew350_kL86RlfhhYYfnlGCFjPBi6BABzmxSYGPENDcfUYoyil-gGsRjKWWv1Rprfi__P3u7gVO57yrP1CK1zBUS4s2Adp21YZCrAX_pSYqNGW5olOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجدداً.. تفعيل الدفاعات الجوية في سماء العاصمة طهران</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83335" target="_blank">📅 04:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83334">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">إطلاق الصواريخ من إيران نحو القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83334" target="_blank">📅 04:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83333">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83333" target="_blank">📅 03:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83332">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83332" target="_blank">📅 03:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83331">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🔻
موج جدید حملات ایران
شلیک موشک از ارومیه، تبریز، خرم آباد
@Naya_Press</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83331" target="_blank">📅 03:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83330">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تصد الأجسام المعادية في العاصمة طهران</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83330" target="_blank">📅 03:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83329">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52cad0a2e6.mp4?token=r18ccgMksJBui37Rr633i19T14IZgN_BJ3TESoHXihrZPRpqvXlhp1Sxi8hl6S_znJKO0cJSiDe9jQrGbW4X5mkyABbd7obPHNsrM4-nXyjPwadvjRtoESGt4TFE3A-joBWUTPZMnzMTDB_uY_XT6w6e3FFs5KXCr30ULc5jUrAmMBmN5tCZIfgZyEI7ks5PGIXwKfNI5pU4a5jE5vwrvca1tJ63HygxdwAp0HClqK-cyZ4LSt_n3r8myD8OAzRrqihs5He73wC7SG2rwY19cDNO3LG5YjGs5GzoNOAhkTgcKRqd5bAGhXCccRsXCDciyZnnvnEMvKfbOFAGvMX2ojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52cad0a2e6.mp4?token=r18ccgMksJBui37Rr633i19T14IZgN_BJ3TESoHXihrZPRpqvXlhp1Sxi8hl6S_znJKO0cJSiDe9jQrGbW4X5mkyABbd7obPHNsrM4-nXyjPwadvjRtoESGt4TFE3A-joBWUTPZMnzMTDB_uY_XT6w6e3FFs5KXCr30ULc5jUrAmMBmN5tCZIfgZyEI7ks5PGIXwKfNI5pU4a5jE5vwrvca1tJ63HygxdwAp0HClqK-cyZ4LSt_n3r8myD8OAzRrqihs5He73wC7SG2rwY19cDNO3LG5YjGs5GzoNOAhkTgcKRqd5bAGhXCccRsXCDciyZnnvnEMvKfbOFAGvMX2ojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83329" target="_blank">📅 03:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83328">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">إطلاق صواريخ من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83328" target="_blank">📅 03:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83327">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">إطلاق صواريخ من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83327" target="_blank">📅 03:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83326">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb26ab9da.mp4?token=oOjbk20KX8Faj2ksEhlbUT0X_ia4UFAn8kIc4L6rszPyTgkIKl-xNGUuz9sKdsxug7cn9YJypE0tcu8IbHeYPzLHTMrJ_zXFJmTT8qanK40qVz0wuu6aAW5TBDUogPV5wRvyJ1KRhslQs4jOEUX8HB-e4_7Q83CqHdgcxBUibLpwG_ua3LZ9jgXqpoqIUtrSPd1TyTSRhbrCLzxN3Wm3uU_uCjrVbNaclTvR-mDLeLoH5ZTEMIJezJe4izWMS2JhCjj8UY-JGFEkCQ_MJIgA0bVXJ7QALfwmQHCov5pVhCDXqzm_OEipTb7UTMgAujNqlC4M8dsdkVAYX_dypnHvBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb26ab9da.mp4?token=oOjbk20KX8Faj2ksEhlbUT0X_ia4UFAn8kIc4L6rszPyTgkIKl-xNGUuz9sKdsxug7cn9YJypE0tcu8IbHeYPzLHTMrJ_zXFJmTT8qanK40qVz0wuu6aAW5TBDUogPV5wRvyJ1KRhslQs4jOEUX8HB-e4_7Q83CqHdgcxBUibLpwG_ua3LZ9jgXqpoqIUtrSPd1TyTSRhbrCLzxN3Wm3uU_uCjrVbNaclTvR-mDLeLoH5ZTEMIJezJe4izWMS2JhCjj8UY-JGFEkCQ_MJIgA0bVXJ7QALfwmQHCov5pVhCDXqzm_OEipTb7UTMgAujNqlC4M8dsdkVAYX_dypnHvBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تفعيل الدفاعات الجوية الإيرانية في سماء العاصمة طهران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83326" target="_blank">📅 03:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec835e3b1e.mp4?token=lrx14KLrGRzRKI0whEbNKTtkcGQMbmDAQx3Jx1SY1DxB6on5u_zrEUJLXPkJ7nPJkTYlDJ_kgIYvsuj1pu727QdDh3lbzAt3vpv7TU98aQjiBKABPoABfpqDvvlJ8Fftsf54lcTRVcyaFQB4uWYE-4QbJHJJrHSDXGKpHyz2FpECu6apPEs7wIJuvdjlpAapw5W_uaYte7w-KNcqG9GCR5p65hQINNQF9xQnZdwWVuJdNAlMFAQiUBxJ14fKgMAaLIEibk809S5LJ8JMn_QoBvQFbnH5rZ1ZI2YvK6VDLOsNJyxmqHjvPnkRb07c31HL5PSB4LaAdF1N_5iVl3uMog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec835e3b1e.mp4?token=lrx14KLrGRzRKI0whEbNKTtkcGQMbmDAQx3Jx1SY1DxB6on5u_zrEUJLXPkJ7nPJkTYlDJ_kgIYvsuj1pu727QdDh3lbzAt3vpv7TU98aQjiBKABPoABfpqDvvlJ8Fftsf54lcTRVcyaFQB4uWYE-4QbJHJJrHSDXGKpHyz2FpECu6apPEs7wIJuvdjlpAapw5W_uaYte7w-KNcqG9GCR5p65hQINNQF9xQnZdwWVuJdNAlMFAQiUBxJ14fKgMAaLIEibk809S5LJ8JMn_QoBvQFbnH5rZ1ZI2YvK6VDLOsNJyxmqHjvPnkRb07c31HL5PSB4LaAdF1N_5iVl3uMog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء عن انفجار في باكدشت وسط تفعيل الدفاعات الجوية في العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83325" target="_blank">📅 03:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83323">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e8559dac.mp4?token=rO-j_tmed2etYcNvsQIT3Awjca2tcan3k2j_balI3C1ILHn1OB9atWgRVgloJpfyhn3wD_s-OoprMP_pnezoSUgmXY55IYbibvNVdhKt75NDfLLXWBuRaWrsuvJuK-KalwP6gKAa7MyS9prJtq9KhlDshoPYd-N7ELJwMDhUsavNmbn2e4VjYe0-jTFgJ_xT8lEH5iGcoPLrjGGAjm0W4YpYBW5ncnNsM2-gA2-bWxs_Ie522nWrGJkcbdwXgaovyp5nlCumP5RDegURwtx4-Uuo0dRc_y6piD6rBkV3RcfGspidajF2Z-hS9VorGRg1G8SFP1YRp7MmK9iLfdeeeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e8559dac.mp4?token=rO-j_tmed2etYcNvsQIT3Awjca2tcan3k2j_balI3C1ILHn1OB9atWgRVgloJpfyhn3wD_s-OoprMP_pnezoSUgmXY55IYbibvNVdhKt75NDfLLXWBuRaWrsuvJuK-KalwP6gKAa7MyS9prJtq9KhlDshoPYd-N7ELJwMDhUsavNmbn2e4VjYe0-jTFgJ_xT8lEH5iGcoPLrjGGAjm0W4YpYBW5ncnNsM2-gA2-bWxs_Ie522nWrGJkcbdwXgaovyp5nlCumP5RDegURwtx4-Uuo0dRc_y6piD6rBkV3RcfGspidajF2Z-hS9VorGRg1G8SFP1YRp7MmK9iLfdeeeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مشاهد تظهر مرور "أقمار ستارلينك" فوق الأجواء الإيرانية بالقرب من الحدود العراقية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83323" target="_blank">📅 03:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83322">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مجدداً..
إطلاق صواريخ من الكويت نحو الأراضي الإيرانية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83322" target="_blank">📅 03:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوي انفجار في محافظة سمنان الإيرانية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83321" target="_blank">📅 03:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c77a83855.mp4?token=bcQu_KU4N4W4iCbnzvV6Ju1hn4s9poS4gvmbD-CObwI1thAPFVfH29gD-SzJAmUmig4PGRbHMft54QEzkHlfjv9tNfSVuhd_m5-dZC74WBndzaWRFSYe2e2dk7dR90Duq7lZXOIvJOwFrNmObXh5qsEFc9pI4NW4rFSJu7sO3msxAgTcZwoN_NE85LJpOLXeB9ZvhzdjaP6fNSBQMJkBrQSmGThn1q7lwC0jeS48bOLE4RS6RQNySgvZK8Jdnm31eSpeWKmPb0zOFDBXrIpGxSsdQ1cZrp2e7BsCmi9-zts7b93CC17kdCjFOwps_EgZQMEA0AcYgmUEiXUo3rmnE02Gswka59sv3QZI37bMg45lnBh24ZztCxsJaCQchnngtnYbMQQ9ArZm6bZejbP1TXdeVg633G6kgPp8L38o0uhcYfCH3mJVRJNUkcgKbQrg-5h3H2t3OQOxtbyCcIDMw7y8sqyODYqdfxIbIB0P7nk5atfOK_f46C0Ugqqki5a7vzQu-Fq8BkPKbKo8FOIK6v5gu5fWVQs4hK5C-CuMeky_ZYwsqBSVTy6E2FdSo-FSBFCbptnd1OptUsA0vLo_TBPcs-P5s9vdW8cgIfpbbB17FKWB5KO8aYHxeCfU1uhPEGrkKF6ll7R90W7NxmNh-DMfaXB17UEShhgISIOFPaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c77a83855.mp4?token=bcQu_KU4N4W4iCbnzvV6Ju1hn4s9poS4gvmbD-CObwI1thAPFVfH29gD-SzJAmUmig4PGRbHMft54QEzkHlfjv9tNfSVuhd_m5-dZC74WBndzaWRFSYe2e2dk7dR90Duq7lZXOIvJOwFrNmObXh5qsEFc9pI4NW4rFSJu7sO3msxAgTcZwoN_NE85LJpOLXeB9ZvhzdjaP6fNSBQMJkBrQSmGThn1q7lwC0jeS48bOLE4RS6RQNySgvZK8Jdnm31eSpeWKmPb0zOFDBXrIpGxSsdQ1cZrp2e7BsCmi9-zts7b93CC17kdCjFOwps_EgZQMEA0AcYgmUEiXUo3rmnE02Gswka59sv3QZI37bMg45lnBh24ZztCxsJaCQchnngtnYbMQQ9ArZm6bZejbP1TXdeVg633G6kgPp8L38o0uhcYfCH3mJVRJNUkcgKbQrg-5h3H2t3OQOxtbyCcIDMw7y8sqyODYqdfxIbIB0P7nk5atfOK_f46C0Ugqqki5a7vzQu-Fq8BkPKbKo8FOIK6v5gu5fWVQs4hK5C-CuMeky_ZYwsqBSVTy6E2FdSo-FSBFCbptnd1OptUsA0vLo_TBPcs-P5s9vdW8cgIfpbbB17FKWB5KO8aYHxeCfU1uhPEGrkKF6ll7R90W7NxmNh-DMfaXB17UEShhgISIOFPaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز الكويت دون تفعيل صافرات الإنذار</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83320" target="_blank">📅 03:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوي انفجار في محافظة سمنان الإيرانية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83319" target="_blank">📅 03:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات تهز الكويت دون تفعيل صافرات الإنذار</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83318" target="_blank">📅 03:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495f7f22db.mp4?token=GEe7f4Sn4H40BkVE3iXozETatp5WnlW4fII93qtr6xUoP2OdQvf3iBKNpWbXlhGeug-N4gjKcNoDFFbX8eUnAex1Kg8guJTSbGMsryuuH89QwEfFCIJ_nZ5o0F-UdKa6jyCPoZbbZHoegv--81PY8fFmQ-YvIREDiwlwy0BZcGcqCnvMvuWQj8o3p0MD8BwC4SZ96FhEHI-Xo8zaV8kiHH9i4EVww4wsTmATvbpAt_xnWk7_3uUX-zVipXDewWOsf0fTliRxVCmt-NGzbAkAKIJszuz86VxnyDLKJF1C3TtIm3u1ImQKgVT0lxPuM3lCLGRtrhkYY4p_oEO59zIx8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495f7f22db.mp4?token=GEe7f4Sn4H40BkVE3iXozETatp5WnlW4fII93qtr6xUoP2OdQvf3iBKNpWbXlhGeug-N4gjKcNoDFFbX8eUnAex1Kg8guJTSbGMsryuuH89QwEfFCIJ_nZ5o0F-UdKa6jyCPoZbbZHoegv--81PY8fFmQ-YvIREDiwlwy0BZcGcqCnvMvuWQj8o3p0MD8BwC4SZ96FhEHI-Xo8zaV8kiHH9i4EVww4wsTmATvbpAt_xnWk7_3uUX-zVipXDewWOsf0fTliRxVCmt-NGzbAkAKIJszuz86VxnyDLKJF1C3TtIm3u1ImQKgVT0lxPuM3lCLGRtrhkYY4p_oEO59zIx8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83317" target="_blank">📅 03:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله أكبر  طائرات مسيرة انتحارية جديدة تدخل أجواء البحرين من منطقة السماهيج، الواقعة في شمال شرق البلاد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83316" target="_blank">📅 03:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الهجوم الذي طال القواعد الأمريكية في البحرين هو الأوسع خلال فترة الإشتباكات الجارية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83315" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83314">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين وسط محاولات منظومة الباتريوت الأمريكية إعتراض الهجمات الإيرانية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83314" target="_blank">📅 02:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83313">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a73b95c1d2.mp4?token=V4nodwzYGOpMddueQPDFR7stl5wNXxZUaRaDb6h4RPCoISx32my21bqtvxap7Sb_Yk9hB_rr0n_ceYuV33dt0cn76jX5UYjTXcTwmUqCuV15h1AoLgW4SyStOHfJQneaaT3xfLZPJWWMlA1SyIz0ohM-4eNvrsJuXtT1Sce60OZ-btFp6SS_JV8H193yfgJDGM5ig2SZZ26K9457SLPrj7W33RHMYuFn77DBV6AMYyC24JpqtRWD-W2wzm3JaEyBoVvF3kvtnH5cp_zS90o1PCg4QGYpIantyStTQUeOedVejZeU_AFTidAGEXtIUl68Cf-SyoGjG-6da-_22hI0zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a73b95c1d2.mp4?token=V4nodwzYGOpMddueQPDFR7stl5wNXxZUaRaDb6h4RPCoISx32my21bqtvxap7Sb_Yk9hB_rr0n_ceYuV33dt0cn76jX5UYjTXcTwmUqCuV15h1AoLgW4SyStOHfJQneaaT3xfLZPJWWMlA1SyIz0ohM-4eNvrsJuXtT1Sce60OZ-btFp6SS_JV8H193yfgJDGM5ig2SZZ26K9457SLPrj7W33RHMYuFn77DBV6AMYyC24JpqtRWD-W2wzm3JaEyBoVvF3kvtnH5cp_zS90o1PCg4QGYpIantyStTQUeOedVejZeU_AFTidAGEXtIUl68Cf-SyoGjG-6da-_22hI0zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين وسط محاولات منظومة الباتريوت الأمريكية إعتراض الهجمات الإيرانية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83313" target="_blank">📅 02:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83312">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSFUaJgdpi4SUuwM8VqOM1nZCZ0kVlyPRjvVq2yLjTQXBnECQXGFdFAUrmWLVX4Ln3S0QQLufnWG9ZvkKt9OH7Bg0MJ-XW30OMoawoMhDG65GpkHGAqesrhS7Rkr84oB39c5GV359R-8bt3NglG-VRNWZ9kU7GeRJaY2gm5DsRPzf_vHZnA_8qSZvarPKaenMLmTkk_Jl6wLy1izFXM8XaMXT1WU-T-NPS6KTtFJSr4xmpgQtYKrFMIMI0dBssSFfgPi2aHwkR0JKWxgP7xZ3rm7XMt1RDjRPbbSSmYfiUO0I7lLWUv3lkv84W7mHN78M5acrCr_rKeUy_D-SZHxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سمحت إيران لمواطنة أمريكية، احتُجزت ظلماً في ديسمبر/كانون الأول 2024 خلال فترة رئاسة جو بايدن، بمغادرة البلاد. وهي الآن بأمان خارج إيران، وبصحة جيدة. تُقدّر الولايات المتحدة الأمريكية هذه البادرة الحسنة من إيران!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83312" target="_blank">📅 02:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83311">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔳
هجوم بالطيران المسير الإنتحاري يستهدف الكويت وصافرات الإنذار تدوي.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83311" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83310">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔳
هجوم بالطيران المسير الإنتحاري يستهدف الكويت وصافرات الإنذار تدوي.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83310" target="_blank">📅 02:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83309">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عدوان أمريكي على مدينة بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83309" target="_blank">📅 02:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌟
نائب الرئيس الأمريكي:
تأمين الملاحة بوسائل عسكرية فقط صعب للغاية نظرا لسهولة استهداف السفن بمسيرات رخيصة.
عهد التدخلات العسكرية وإرسال آلاف الجنود لتغيير الأنظمة انتهى وجيشنا لن ينوب عن الشعوب في تقرير مصيرها.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83308" target="_blank">📅 02:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83307">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgxsWTNXTqLMPPPbFa9_d-XzVYetBNOpFE4sebSCplkMA_hu4kePnrB38BiOBo0rSMZ-aubztCniNHNdVnmn9f19BntgkP8gmTsUgDm-twldwF9b4ce87ezq3gMKWdCWLSM9vAvC3AIyFIoEAcpTBVxppPhwVXgL9Nwbr4Iko3HkBjjukVZTwojziz-7toESYKuvO4-GXHPpv9hw2V_OmiOWmg3YYQcK8QG3PI8SSdbQnHeobbSeN0XYL1QfT58K16viXCTc1P0s1is-BwqQtF-vMkOQJoiPs9qUHvV3DExpgbpwIl_w76qCs5ytMTfoWe0Wc5BH5GOMk61blUEjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إستهداف وإسقاط مسيرة معادية في محافظة أذربيجان الشرقية الإيرانية.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/83307" target="_blank">📅 02:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83306">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eddb11da4e.mp4?token=erh68CZpqpK110zO9DyFWXfwsW3YDA01uSF_XTUG0-L-LdAsIoW67FOk9P-3F7oJ1PHabU-YI4W7NQJFYl888-Z98FqlaRwpt25g0ZFt_Av0ZkP57_fVjjJl4JKts0S42Qqs8BD_59DqwPPNnPbjg8thIrX5qaNkmW2KhVxPmWg6PYSzXP3E2tb5SAkHzak2qSh5aTC4W5y6JMWDDZwdTKiSXMOrNoVcnir740VbhD-MF31zqvUQ8QFfNQWGjNlsLZ5PH8We2dgWmr2LKwnSPW36bJ31yhebW9zJDruvZ6yqAj2hYOx30zYb13LUlp27PzEoCeQ6jA_KUExzmJqAGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eddb11da4e.mp4?token=erh68CZpqpK110zO9DyFWXfwsW3YDA01uSF_XTUG0-L-LdAsIoW67FOk9P-3F7oJ1PHabU-YI4W7NQJFYl888-Z98FqlaRwpt25g0ZFt_Av0ZkP57_fVjjJl4JKts0S42Qqs8BD_59DqwPPNnPbjg8thIrX5qaNkmW2KhVxPmWg6PYSzXP3E2tb5SAkHzak2qSh5aTC4W5y6JMWDDZwdTKiSXMOrNoVcnir740VbhD-MF31zqvUQ8QFfNQWGjNlsLZ5PH8We2dgWmr2LKwnSPW36bJ31yhebW9zJDruvZ6yqAj2hYOx30zYb13LUlp27PzEoCeQ6jA_KUExzmJqAGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مصدر أمني لنايا: إطلاق 6 صواريخ من الأراضي الكويتية عبر الأجواء العراقية باتجاه إيران؛ الصواريخ أطلقت ضمن قاطع مسؤولية قيادة القوة البحرية في أم قصر باتجاه الأراضي الإيرانية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83306" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83305">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات جديدة في سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83305" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83304">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عدوان أمريكي يطال سيريك وقشم الإيرانية</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83304" target="_blank">📅 01:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83303">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قصف مستشفى في الاهواز</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83303" target="_blank">📅 01:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83302">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔳
🌟
🇮🇷
الكويت تشارك في الحرب الأمريكية على الجمهورية الإسلامية خلال إطلاق الصواريخ من أراضيها نحو الأراضي الإيرانية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83302" target="_blank">📅 01:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83301">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عدوان أمريكي على مدينة بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83301" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83300">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات عنيفة تهز العاصمة الاوكرانية كييف نتيجة هجمات روسية</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83300" target="_blank">📅 01:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83299">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عدوان أمريكي يطال سيريك وقشم الإيرانية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/83299" target="_blank">📅 01:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83298">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">أقرّ مجلس النواب الأمريكي قانون "إنقاذ أمريكا" بأغلبية 217 صوتاً مقابل 209، مُلحقاً بتشريعات الأمن القومي. وينتقل الآن إلى مجلس الشيوخ.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/83298" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83297">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d7a3a2216.mp4?token=NcLDok8v1_ISBNHdsw4luc87eCH_YqF-wwuoZ-jMsPmlt2HamQpdALuNL5NOqFEaOB_Vb8r0inDHFXN93rwR60QjcvALi9_icX0cLjZBnDXvGok5y_COIs-9nv8IstjM52BhbStzhKTASk8zli4vXYbTdSv71MmfHH_1nDute3i371WHZXJJZpcu1DZ7MGIfVoInupzK9sMjARVy1IoZjX77A0jHlSlmBV6_Yph7Qf2R__mIn65T8pf1PYuOcit95yaKK0Cxmc16GLnHeRwTloviNtwouGI93s6J161kIIg2xwHHFwYc0-7fcSVxWRg5psOY0uJ_wenc0-JI1Gkf9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d7a3a2216.mp4?token=NcLDok8v1_ISBNHdsw4luc87eCH_YqF-wwuoZ-jMsPmlt2HamQpdALuNL5NOqFEaOB_Vb8r0inDHFXN93rwR60QjcvALi9_icX0cLjZBnDXvGok5y_COIs-9nv8IstjM52BhbStzhKTASk8zli4vXYbTdSv71MmfHH_1nDute3i371WHZXJJZpcu1DZ7MGIfVoInupzK9sMjARVy1IoZjX77A0jHlSlmBV6_Yph7Qf2R__mIn65T8pf1PYuOcit95yaKK0Cxmc16GLnHeRwTloviNtwouGI93s6J161kIIg2xwHHFwYc0-7fcSVxWRg5psOY0uJ_wenc0-JI1Gkf9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي أمريكي يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/83297" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
