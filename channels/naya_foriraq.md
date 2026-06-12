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
<img src="https://cdn4.telesco.pe/file/hp1D4-5FQEEJ4vY-1-jVRnPNpQwRMvtarPgPeFIhlVotFQ0FGNZPFoYeBPjkCrxHPDBsEmJ2AmwRTQl5vsCfFMn5ja--C_khFhq9jgsxO8jQmL5h4fPAfmKwI3_4fpwNJ0c7FmrbMJ2bUsS-PNAxRI65OWqfn4oEpT7rcnpWoipUAvELm5sddhKhcWrvwZSZHChJTrglDeOFxeoBrDkYNxsNtvtarkuK8s4k5gP3deYEnLuuMo7dNNb_bE9zzHGDwr0OIxq00003sPe9xzeG_UvmKW-uo4stA9Xa-LUR7t-5UpfrWUzQdsAosNxEu84GBxCAJh5qdw7U_aGY9W5pww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 260K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 17:28:34</div>
<hr>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📱
خلل يضرب تطبيق الفيسبوك في العراق وعدد من دول العالم يتسبب بتوقفه.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/naya_foriraq/78520" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr80r-pP-DWepUdXveK0aqbitxQfQ8TsyduOeUY3gnM8jNhiSbza0-dhcMsegClZEA4HCjNpWUGLtyhXVZvqnqLpitztzOqBTcpV23f2BGP11c4qm1WRuOZaRYGuDERsHNVoLCIF_zi5DmzYWbxgHv3-S-h_HxZxWZUKW46SECkcaFxJGGr35esqU5D8a_wdXxQb_9E23g2SHDqdFmWrityOEfU4z9lK-9XPu5YzZaCefk4sMO-b3b98gY1R63GWPF4ckB_AcgYgFTvqtfbyElfwXoqyxHnBwXH4N8HhxDrOx7fpE8y54afWdb14V4O9BcKRdILnQtL7DGYnSn1EPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب مغردا:
الشروط التي سربتها إيران إلى وسائل الإعلام الكاذبة لا علاقة لها بالشروط المتفق عليها كتابيًا. ما قالوه، بما في ذلك بيانهم الضعيف والمثير للشفقة بشأن وجود اتفاق، لا يمت للحقيقة بصلة. أشخاص غير شرفاء للغاية في التعامل معهم. لا يوجد معهم شيء اسمه التعامل بحسن نية. أمر مذهل! كما أن هجومهم الذي تم رفضه تمامًا بطائرات بدون طيار الليلة الماضية على السفن الهندية المغادرة لمضيق هرمز غير مقبول على الإطلاق. من الأفضل لهم أن يضبطوا أوضاعهم، وبسرعة!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/naya_foriraq/78519" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية جرّافة (D9) تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/naya_foriraq/78518" target="_blank">📅 17:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
جهاز الامن الوطني العراقي يعلن إحباط مخطط لاغتيال رئيس جهاز الأمن الوطني وعدد من الضباط كانت تقف وراءه خلية مرتبطة بما يسمى "التجمع الوطني العراقي للتحرير والتغيير" إحدى واجهات حزب البعث المحظور بعد جهد استخباري شمل الرصد والمتابعة والاختراق.</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/78517" target="_blank">📅 16:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
اخلاء 3 جنود من جنوب لبنان.</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/78516" target="_blank">📅 16:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📰
‏مصدر غربي لرويترز: من المرجح أن تستضيف جنيف مفاوضات الاتفاق بين واشنطن وطهران.. إيران تتمسك بموقفها المطالب بإنهاء القتال في لبنان</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/78515" target="_blank">📅 16:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مصدر مُقرّب من الفريق الإيراني المُفاوض:
إنّ الادعاءات التي أطلقها ترامب وبعض وسائل الإعلام الأجنبية بأنّ "الاتفاق قد تمّت صياغته النهائية ومن المُقرّر توقيعه في جنيف يوم الأحد" عارية تمامًا عن الصحة، في الأساس، لم تُستكمل بعد عملية المراجعة واتخاذ القرار في إيران، وبالتالي فإنّ الإعلان عن يوم الأحد ومكان جنيف يُنفى تمامًا.</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/naya_foriraq/78514" target="_blank">📅 16:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📰
‏
مصدر غربي لرويترز:
من المرجح أن تستضيف جنيف مفاوضات الاتفاق بين واشنطن وطهران.. إيران تتمسك بموقفها المطالب بإنهاء القتال في لبنان</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/naya_foriraq/78513" target="_blank">📅 16:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇱🇧
كتلة «الوفاء للمقاومة» التابعة لحزب الله:
المفاوضات المباشرة التي انزلقت فيها السلطة لردم هوة العداء للكيان الصهيوني أدت إلى مزيد من الانقسام الداخلي بين اللبنانيين، الإصرار على المضي في هذا الخيار يشكل مكابرةً غبيةً تصبح معها المفاوضات انتحاراً سياسياً مجانياً لن يحقق شيئاً، الحل يقتضي عودة السلطة عن خياراتها العدمية هذه والابتعاد عن خطاب التحريض والكراهية وعن استعداء غالبية الشعب</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/78512" target="_blank">📅 15:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBEmiylFhxph2RrFQVlAREJWPFu65KlSn3aG-ZItU4qnxN81mJURG0jYMe4AT5LG2RL_4Vn9eh3AthhmcbejDPJRVhi6cAoYrWKcD7i5r79yV35zWfPsTk7fUIVC9ulI3XzcCJbbU4MUk9fMvY4Fk1I9U5-xfeIr9c6xYSYBLAxHL9cZCnwbAFf12ztvXJIXMaCPvdtyFgqwDx3sJOPdtOLXq_Pq1r8cPZEIFCoYKF2l_fjqWG31jy-tZQWpBxvRdLcvyXOBwImWqQXJco4-oXzAhnZR4gfTAGxqypzWvQWtjEC_gsuF8nHUGjEzB7GuxJt1INdQVkqq6VbIUgG7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
اكثر من 100 الف مشارك الان في مسيرة الفروخ (المثليين) وسط تل ابيب.</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/naya_foriraq/78511" target="_blank">📅 15:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📰
شبكة CNN:
مصدر إسرائيلي مطلع يقول إن إسرائيل تضغط على الولايات المتحدة بعدم الإفراج عن أصول إيرانية مجمدة كجزء من مذكرة التفاهم</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/78509" target="_blank">📅 15:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية تصدّي المقاومة الإسلامية بتاريخ 05/06-06-2026 مربض المدفعيّة المُستَحدث التابع لجيش العدو الإسرائيلي في بلدة العديسة جنوبيّ لبنان بصاروخٍ نوعي ومسيّرات انقضاضية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/78508" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
‏نتن ياهو:
إيران تسعى لتدمير دولة اليهود وأنا أكرس حياتي لمنعهم من القيام بذلك ولن تمتلك إيران سلاحا نوويا في عهدي</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78507" target="_blank">📅 15:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وكالة إرنا: النص الحالي لا يشمل عبارة "تمديد وقف إطلاق النار" بل إنهاء الحرب تماما بكل الجبهات.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78506" target="_blank">📅 14:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وكالة إرنا: على عكس ما يتداول إعلاميا فإن إيران لن تلتزم بإعادة أوضاع مضيق هرمز لما كانت عليه.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78505" target="_blank">📅 14:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
وكالة إرنا حول تفاصيل الاتفاق المحتمل بين إيران والولايات المتحدة: تم إعداد نص اتفاق إنهاء الحرب بعناية فائقة ودقة متناهية ولا مجال لأي تفسير تعسفي أو تهرب من الالتزامات من جانب أي من الطرفين في هذا الاتفاق، لن يتم التوصل إلى أي اتفاق بشأن الملف النووي في…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/78504" target="_blank">📅 14:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
وكالة إرنا حول تفاصيل الاتفاق المحتمل بين إيران والولايات المتحدة:
تم إعداد نص اتفاق إنهاء الحرب بعناية فائقة ودقة متناهية ولا مجال لأي تفسير تعسفي أو تهرب من الالتزامات من جانب أي من الطرفين في هذا الاتفاق، لن يتم التوصل إلى أي اتفاق بشأن الملف النووي في مذكرة التفاهم الحالية ولن تقدم إيران أي التزامات جديدة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78503" target="_blank">📅 14:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اعلام العدو الصهيوني:
تنازل امريكي جديد لايران.. الولايات المتحدة تمنح شبكة beIN Sports إعفاءً من حقوق بث مباريات كأس العالم في إيران.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78502" target="_blank">📅 14:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📰
فاينانشال تايمز:
تقييمات المخابرات والدبلوماسيين الغربيين تعتقد أن طهران احتفظت بجزء كبير من ترسانتها من الصواريخ ومنصات إطلاقها وبنيتها التحتية السرية. ويُقال إن العديد من المنشآت أُعيد فتحها أو إصلاحها في غضون ساعات أو أيام.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78501" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
وكالة مهر الايرانية للأنباء تنشر بنود الاتفاقية التي سيتم توقيعها
:
1- وقف فوري ودائم لإطلاق النار على جميع الجبهات، بما فيها لبنان
2- التزام الولايات المتحدة بعدم التدخل في الشؤون الداخلية لإيران واحترام سيادة الجمهورية الإسلامية الإيرانية
3- رفع الحصار البحري بالكامل
4- التزام الولايات المتحدة بسحب قواتها من محيط إيران
5- إعادة فتح مضيق هرمز خلال 30 يومًا بالتنسيق مع إيران
6- تعليق العقوبات المفروضة على بيع النفط والمنتجات البتروكيماوية، ومنح إيران حق الوصول الكامل إلى مواردها المالية
7- تقديم الولايات المتحدة وحلفائها خطة لإعادة إعمار إيران بقيمة لا تقل عن 300 مليار دولار
8- 60 يومًا من المفاوضات للتوصل إلى اتفاق نهائي قائم على الملف النووي والرفع الكامل للعقوبات الأولية والثانوية، وقرارات مجلس الأمن الدولي. مجلس محافظي الوكالة الدولية للطاقة الذرية
9- إعادة تأكيد التزام إيران بموجب معاهدة عدم انتشار الأسلحة النووية بعدم إنتاج أسلحة نووية
10- خلال المفاوضات، تعهدت الولايات المتحدة بعدم زيادة قواتها في المنطقة وعدم فرض عقوبات جديدة على إيران.
11- الإفراج عن 24 مليار دولار من الأموال الإيرانية المجمدة خلال فترة الستين يومًا للمفاوضات النهائية، على أن يُتاح نصفها لإيران قبل بدء المفاوضات.
12- إنشاء آلية مراقبة لتنفيذ الاتفاق.
13- سيتم إقرار الاتفاق النهائي بقرار من مجلس الأمن الدولي.
14- لن تبدأ المفاوضات النهائية قبل الإفراج عن نصف الأموال الإيرانية المجمدة، وتعليق العقوبات المفروضة على النفط الإيراني، ورفع الحصار البحري. وسيقتصر الاتفاق النهائي على مصير المواد المخصبة وتخصيبها، ورفع العقوبات، وخطة إعادة إعمار الاقتصاد الإيراني، مع استبعاد مناقشة برنامج الصواريخ الإيراني ودعم جماعات المقاومة نهائيًا من جدول الأعمال.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78500" target="_blank">📅 13:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
وكالة تسنيم عن مصادر:
لم يتم بعد اعتماد نص الاتفاق حتى الآن من قبل الجهات المختصة في إيران. حاول ترامب خلال الأيام الأخيرة بدء الضغط والتهديد والإجراء العسكري، ومن خلال وسيط قطري الضغط من جهتين لتغيير مواقف إيران، لكن في النهاية لم تقبل إيران التغييرات الجديدة</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78499" target="_blank">📅 13:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
مشاهد من المحفل التأبيني السنوي لذكرى مجزرة سبايكر في محافظة صلاح الدين شمال العراق.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78498" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📰
بلومبرغ تقول انه قد يتم توقيع الاتفاق بين طهران وواشنطن في جنيف يوم الأحد المقبل.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78497" target="_blank">📅 13:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وسائل اعلام خليجية عن مصادر:
إيران هي من طلبت توقيع الاتفاق مع أميركا في دولة أوروبية لمنحه طابعا دوليا.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78496" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇩🇪
إلغاء رحلات من مطار هامبورغ في ألمانيا وإخلاء المنطقة الأمنية حوله بعد على العثور على طرد مشبوه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78495" target="_blank">📅 12:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYkAlDP6gwmv4Gi38zi-8vS2JZ3MFuWRzvnNSmgVytghfymRnQbAZH2sKajOsOJgjWT-DVGFbik6QOxIodFmZNbggnJX6Ao4I2YveJF9etylH-2hjwrLeJaaHcO0mV-njcn4_dIMQrY0czbHyKkFR3MwKksTfjHEcBKdnVOqmvKilDWaeABDERMd5pgvIhSvdpT2wRRe-OD8WchwAun3zEYciwcZNli-9xdL5aXlzmgh5hhfbpRk22PRijVv374LecB2zrAk7VOd14w8VL-325wFf7O8CWLM3_BuSe-uA2hE8KunlrOhJr85xOk6yok071nzscALR2u5CsCDPDEN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية في كريات شمونة دون تفعيل صافرات الإنذار</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78494" target="_blank">📅 12:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/631780cade.mp4?token=YDATppCAR_1JVLa6zs4zvMG53ogNCVI35GndxRUC1RS5zlFTquIrEzuwqgmIm948LEhbDgFvDNxMdc_BYYQV2AJ1ZvIgm7SxV9oErHq6oQ5jbkln7DGx3o5DcCEbgwmsv-wB82g1gAlRveYzUgnDTHVB8FJHdcwaes3z0Obj5v2JcBQ-z4Lzl2ceuZk-TH4tlTVQy65pb8O4P1ey8szdYxkNd_Wu_yhCmOjdIsR9xDuVK4txb2Jf_T3BSIgQScf3emzZzyWfwXf6oWfSWncZGvUn3ewz1G2p7sD2NVFLdsz9WnSl96cudcIEax4bBRxjklCyoqOIiOTRlyePgsFJyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/631780cade.mp4?token=YDATppCAR_1JVLa6zs4zvMG53ogNCVI35GndxRUC1RS5zlFTquIrEzuwqgmIm948LEhbDgFvDNxMdc_BYYQV2AJ1ZvIgm7SxV9oErHq6oQ5jbkln7DGx3o5DcCEbgwmsv-wB82g1gAlRveYzUgnDTHVB8FJHdcwaes3z0Obj5v2JcBQ-z4Lzl2ceuZk-TH4tlTVQy65pb8O4P1ey8szdYxkNd_Wu_yhCmOjdIsR9xDuVK4txb2Jf_T3BSIgQScf3emzZzyWfwXf6oWfSWncZGvUn3ewz1G2p7sD2NVFLdsz9WnSl96cudcIEax4bBRxjklCyoqOIiOTRlyePgsFJyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية في كريات شمونة دون تفعيل صافرات الإنذار</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78493" target="_blank">📅 12:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78492" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78491" target="_blank">📅 12:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxhNr7LrlyzGFA20TXwzWW-OD8GTYZ-tgoML6s0a31ck329rdeYjlacJegxZzOCVqYaXsu8V2HBe3BbjRqw92M4KNlYpSNrlXfUm62swOFOOrzh1BVZ-UL-tp2E1rH1R9lbUWLUMaxK5WgAVHkeOZeGJPzEN5wbAtrA-h0hxQullr2Q0kR6t3bHA8nfL4KuvFxdSvyP8f9l_ezGCt97aYgC_MAyY1G5YWwGR9ZeoVf1mPIGHQvYcCBQqzhzVHuxHyN6uXo5xBUY4RMWrkKrcxx2_seYi4wFYbZoQIen07kkUrG0KmKfvWf9ou7JPG3r3qezi-NsqNhoYQjN8A_fM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
🏴‍☠️
سلسلة من الغارات الصهيونية استهدفت بلدة البياض في قضاء صور جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78490" target="_blank">📅 11:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇹🇷
🇸🇾
مصادر إعلامية تابعة لحكومة الجولاني: ازدياد الخلافات بين الجولاني وداعميه.. أردوغان يطالب الجولاني بعدم الرد على ترامب والدخول في معركة لبنان دفاعاً عن إسرائيل.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78489" target="_blank">📅 11:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPVV2R60NHzAKLN59xix09vFOJFMQ6pU_B5vVWGbnQoJ0NJur2IHPpwur3DNPxS3UsE_SiLKPwIWETeSOZCowRbTey2KrWgtTUl6avBALEEM3NDeVxLmHCzucsIyUJJkhCPzZqMi0xc5VPayxA-MZkV-n9C08iW9s92MJG4IYgJTDfYqJtBK3sWeDpCiCb_tTIBWSR87kJmGzXu0ahY5CSPhufcKTjLJoX1f3SadRoCo_Lyi4QvtIVIRNKhYPHdsisdAzQWAGwNepxp9isUR2HWMS1Gsor68fZZQmL_AqLmvEXS2_hVVh57h1ulu78Hf18apZSxjHzjGNxuOUhjSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الخارجية الأمريكية لمواطنيها : لا تسافرون للعراق الوضعية داچه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78488" target="_blank">📅 11:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇹🇷
🇸🇾
مصادر إعلامية تابعة لحكومة الجولاني: ازدياد الخلافات بين الجولاني وداعميه.. أردوغان يطالب الجولاني بعدم الرد على ترامب والدخول في معركة لبنان دفاعاً عن إسرائيل.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78487" target="_blank">📅 10:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن مصادر: نتنياهو قال إنه أكد لترمب تفهمه لسعيه لاتفاق مع إيران لكن يجب ألا تكون إسرائيل الضحية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78486" target="_blank">📅 10:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e8806f6a.mp4?token=gk2wtEcetPkbGjKf1QuqvDlxM4AQmqb5WBGVM3VDrar7IeeOGJ0jeRBktxWgZoERH0e5BO2culfITO4zy1Mxi2WIiKHgEKujmAX0jKphypqLpTbk_MqbYNt4wOQzG6UVNdLm71asTesISXilOCHm89bCsOAjbgts0vaHCfSgrCKosg3odAoDlU1kzLvAI1zn3ONp2dLwr_QKYZPfqGw28a6dyAMtV12-d-7IRIsg1aL1xtjk4y-NKnTcz8hbVWohMoIcanVOibG_0QDzIPIRcsubtzaEFx85ZgPW60awSgeb8HnfxA-0Mp3illbXkZuBYxLUEFmBx6tD8V0oCehRTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e8806f6a.mp4?token=gk2wtEcetPkbGjKf1QuqvDlxM4AQmqb5WBGVM3VDrar7IeeOGJ0jeRBktxWgZoERH0e5BO2culfITO4zy1Mxi2WIiKHgEKujmAX0jKphypqLpTbk_MqbYNt4wOQzG6UVNdLm71asTesISXilOCHm89bCsOAjbgts0vaHCfSgrCKosg3odAoDlU1kzLvAI1zn3ONp2dLwr_QKYZPfqGw28a6dyAMtV12-d-7IRIsg1aL1xtjk4y-NKnTcz8hbVWohMoIcanVOibG_0QDzIPIRcsubtzaEFx85ZgPW60awSgeb8HnfxA-0Mp3illbXkZuBYxLUEFmBx6tD8V0oCehRTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من المحفل التأبيني السنوي لذكرى مجزرة سبايكر في محافظة صلاح الدين شمال العراق.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/78485" target="_blank">📅 09:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: الجيش ليس قريباً من حسم المعركة مع حزب الله</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78484" target="_blank">📅 07:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📰
أكسيوس عن مصدر: مذكرة التفاهم بين واشنطن وطهران ستمدد وقف إطلاق النار لمدة 60 يوما بما في ذلك بلبنان
مذكرة التفاهم بين واشنطن وطهران تتضمن إطارا للتعامل مع مخزون إيران من اليورانيوم المخصب
ستجرى مفاوضات نووية بين واشنطن وطهران خلال فترة وقف إطلاق النار.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/78483" target="_blank">📅 07:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صفارات الانذار تدوي في مطلة شمال اسرائيل بعد اطلاق رشقة صاروخية من حزب الله.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/78482" target="_blank">📅 05:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9CqOTwmt7Xi58fKvEKsAKFiFq2UHDg0XKBzlJLmB7GrwvTN45gY9QfSnmLs6J1vUvCw_wS5ANCS95YL8P3i4gXG_L5Vqs-tWFzmv9vtQm5HLX9QANHzi5grXryM4kd6Wa2rHOeX2obs2XLwabL8LA8LzGeOtW4iebuvpI_0Ng5to5qbvqQoR01PMPyzG-T8WPvJ74ckjNARn7mmAHKgIxlCQLqeB81DeECYyfdbkZSgZmCGCnUDwItLufEGL0iByIeS0Ksf6aqqRZmpMmDR1t53SYaaWFGWOQSJSrnD739FIfR-1Nw5X9QRCA_jKNNV6D5WCzKIv0X8n7syK6tWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SE9GaSpb96rTEdG46UUHoYhqmylxhfCV0mqxJsA_2sLDfmvPz0rStpOCWwnlRNT5taZW7OnGrhlYxxF2Q6MQ_CRHH0wq6vpxoRAy53J_TEskCVXeXb-LwT8eQ6yiTzidqQ-aFMdWEKdM3721Eb-tvIVkSLxk_HB8UskJV2R6ZV4-D8BVtByvhoa_zsSWu8tV3nQWQuro-sLNLMSXKrrlJHP3dxypEctiaXJJNrEqzMI4nTothD2zcKHrRm0-S4Uawrk7EkUzf8daxL3YzmYoYvjh-QAh99zj-1f5xvpaOis6S3PPf1UVloLbRU5F1LewT7GYnZUVDbdlKciLTChlmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
الخارجية الهندية: 3 سفن هندية تعرضت لهجمات نفذتها البحرية الأمريكية.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/78480" target="_blank">📅 04:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
زلزال يضرب مدينة كهنوج الايرانية بدرجة ٤.١.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/78479" target="_blank">📅 02:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
الحرس الثوري الايراني يمنع مرور سفينة من مضيق هرمز كونها لا تمتلك تصريح مسبق.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/78478" target="_blank">📅 01:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الاصوات المسموعة في سيريك سببها اعتراض سفن في مضيق هرمز.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/78477" target="_blank">📅 01:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdS4fQA6WKaIwKKA5CBetfgdmWXXHchGdTsBA_OYJxFiaQppqe0tkS49zjgsOonreJmjm5m6e2xSa8e-mpIZNhHxs-NxabJVmAn6XnmGURjFeWoWR-fWRj9D6Aj-SZV48SlUI94YFIgRhF-SqeXpU0_KeJ74I5g2PWaeIvTIz-cEgQIZSl9CpTRKz86NFcKivf5GBaXRXFCanuLEZm8HZgmw6WPDeMdhyRdmfKwRBsRa6r7HEsB_lieLq4o9s4_-g73x0WuH4J3-Cct48TSlA_IuTYwCpN2Hw7M8l93KH6fbRgHjjPo6zbm5Gm1D9l9OWJ_wXqOjb8euDfRTKNPBDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرئيس الأمريكي ترامب:
هذه هي الأسلحة التي نستولي عليها من الكارتيلات المكسيكية. إنهم يقتلون آلاف الأمريكيين كل عام! الرئيس دونالد ج. ترامب.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/78476" target="_blank">📅 01:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3yCNITkP3b8ysO6QZPxK1aOXFhI67fwSBJARkASAxtrfp0L7HaLuaqeTyv8UUmnliYxMC02U-ZXx71juExCH0rU4yhSRWGBLSJSElDlUmdT98XCcTvg_LOmqyi7mkkMo72HNxhwc0JQBuLhl6EJr2xUXfb7L1TF56z-PWKbi34XFpQfyndwbQcr2XicSdYcuCEZ69LGkUQbKgWGExNwVffAzFDf0SqyEqhweZ8F4UAac75-qUYYxgqEEyAhp1n0hu37KdYRCM-D9jseV02ceYoI45K0FEcN7EZSvoTs74P51FWkQWebQvnxzjNnS_FR1ctsEhDSvXxTjTjMZKe8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة حربية من نوع F-35 تطلق نداء استغاثة فوق ابو ظبي لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/naya_foriraq/78475" target="_blank">📅 01:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات مستمرة في سيريك من الممكن تصدي لسفن لم تلتزم بقوانين الحرس الثوري.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/78474" target="_blank">📅 01:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
انباء عن انفجار في سيريك الايرانية.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/78473" target="_blank">📅 01:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
انباء عن انفجار في سيريك الايرانية.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/78472" target="_blank">📅 00:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLv_E-4NeWiXiWDud8MXnK4T0WFqMapUObWfPzdjgPwMxmXR4izyupBYkns1bWWYQAHVXfx4_tclvtN3zrjsSTU1zKg7IMKA10y_LUqOCk0Po1FsU8ymKghaXjU-p-oDWeP69G3oocjdAZj5-DotGcD0i5vOtQnIwErh4xvzcyPmXk0TFcogz6hYomd8w47Q-nvPWJALxEzA01t3_jIojuxvuOlIq-Geq6fz5P1v08_lwDaCL8OPV7__rmBD6nMSKUImsfAcxTNJfF37W7UBFGndf1fcC7gmKxbcJZM80SYVqTWvl5SjLzTKVziKqsjswjAIp5eahdVKlvyw0kfZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إسماعيل بقائي:
إن الهجمات الأمريكية الوحشية على السفن التجارية الهندية، والتي أسفرت عن مقتل ثلاثة مواطنين هنود على الأقل، تُعد دليلاً واضحاً على سياسة أمريكا المستمرة المتمثلة في السطو المسلح والقرصنة الحكومية.
‏نتقدم بأحر التعازي إلى عائلات وأصدقاء البحارة الهنود الذين سقطوا، ونقدم خالص تعازينا للشعب والحكومة الهندية.
‏يجب على المجتمع الدولي محاسبة الولايات المتحدة على سلوكها الخارج عن القانون، والذي لا يزال يهدد السلام والأمن العالميين ويعرض حرية الملاحة للخطر.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/78471" target="_blank">📅 00:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭐️
أكسيوس عن مصدر:
نتنياهو لم يكن لديه أي إشعار مسبق وفوجئ عندما أصدر ترمب بيانه الأولي بشأن الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/78470" target="_blank">📅 00:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: الاتفاق مع واشنطن لم يصبح نهائيا بعد.  روايات الجانب الأمريكي هي لإظهار أن إيران تراجعت عن مواقفها تحت الضغط والتهديد.  نص التفاهم جاهز تقريبا.  الوسطاء ناشطون الآن وباكستان وقطر فاعلتان في الوساطة.  إيران أثبتت أنها لا تتهاون في ما حددته…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/78469" target="_blank">📅 00:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: قلنا سابقا إن أكثر نصوص الاتفاق كانت محسومة لكن الجانب الأمريكي كان يريد إضافة مطالب جديدة.  المراجع العليا ستقوم ببحث جميع بنود أي تفاهم محتمل وسنعلن موقفنا في وقته.  ما يجري الحديث عنه بشأن زمان ومكان توقيع الاتفاق تكهنات إعلامية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/78468" target="_blank">📅 23:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
قلنا سابقا إن أكثر نصوص الاتفاق كانت محسومة لكن الجانب الأمريكي كان يريد إضافة مطالب جديدة.
المراجع العليا ستقوم ببحث جميع بنود أي تفاهم محتمل وسنعلن موقفنا في وقته.
ما يجري الحديث عنه بشأن زمان ومكان توقيع الاتفاق تكهنات إعلامية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/78467" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
على الرغم من أن إسرائيل ليست طرفاً في المذكرة، فقد أعربت عن تقديري لالتزام ترامب بأن أي اتفاق نهائي سيشمل إزالة المواد المخصبة، وتفكيك البنية التحتية للتخصيب، والحد من إنتاج الصواريخ، وإنهاء دعم إيران لوكلائها الإقليميين.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/78466" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/994003fdaa.mp4?token=lMHbEQvVEg5tSodCsKs28_Hdzd5i94arxqiN0wB4qP-mltBolReQEGAw7imdZEwO8qRVE7Dix3Xte8SOa1UYmc5iXmQ7MetNJjVAQ6zEgIgz3Q1owFee8vbKLQiEDbDaCg24LMSGw6TFop8yA5jDWQKmOL94W0qPnsdiDwgx0gk-KmbsbiyEO2eapDBLAYNcwdVK93gop_S91xcuErdVkt3g4fFc41PaKrf-tuT2TrGmZa7PAJ5ZaKF7hQARddzfc1DyNNstkULEoZjbs4YPkFqgMi8thr2fdfqosfHO-H1EuIn7IT19dZVHN1sawLhJTjJbV9aaP54p8LFESUpuWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/994003fdaa.mp4?token=lMHbEQvVEg5tSodCsKs28_Hdzd5i94arxqiN0wB4qP-mltBolReQEGAw7imdZEwO8qRVE7Dix3Xte8SOa1UYmc5iXmQ7MetNJjVAQ6zEgIgz3Q1owFee8vbKLQiEDbDaCg24LMSGw6TFop8yA5jDWQKmOL94W0qPnsdiDwgx0gk-KmbsbiyEO2eapDBLAYNcwdVK93gop_S91xcuErdVkt3g4fFc41PaKrf-tuT2TrGmZa7PAJ5ZaKF7hQARddzfc1DyNNstkULEoZjbs4YPkFqgMi8thr2fdfqosfHO-H1EuIn7IT19dZVHN1sawLhJTjJbV9aaP54p8LFESUpuWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لا أريد تحديد مهلة للتوصل إلى صفقة مع إيران.
😆</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/78465" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf0cf36cd.mp4?token=D1lsWgCXYWF5SL4PMMqjPgDVLP8TJMV81dgdiLHnJRWSXiWO0I-g4ZEGsK_zbXAviSv28C3-ts2JZqx8dSIrLVMdsk-gsbIw0A4xX_WHj1BK7suRlAkm3sryb-ozFU_ah8PrDi0wegjfFfTTzqrrUPG_7BG0-PT4_DpiwkbWwXP5Zw9XZxAgN7mN0JSw7rAHZToX_yKoj2RBTjEtwaPXjOn9I0Y53mRfAWylxisEEiko4QK0Z-0PxKx0d_75459ABTMKHR_0Ie9I2jMD7NMROFVOSlQtychUNW9G1Q70hk1NKqYkzZJy3CKyDog4LYzVzUN0kSufqDjqswjfe6zMOxPoULYDs_jerZ-mbMe3T9G_rn5pnmPBv8nDigLbyjPT8boECo3ZRQORb8nIBKdj6oc0y7aI4WcV1dwPwEotWrBhvEQ-qrDlPISPMiOcNPVgya3DVbyceWNmjzITdzWYB8G3qhyLRMmuoXwr4jRVk7XGFV7D4JWG5pyUxVqVjck0ohGz5rFiL08AUAJmjjEpPm5voPfNYhdrVqA-Fg8d78sZ2vNFymwzg_X1-ykP8BjPlVjEP7RYGZIrfMGRbIW7ZyKpZ8VLYTFVq97ljcj3CeBZHO8CfHFnlVxUR29cZqUydZClWzk4OM32MVQPlFSaWWVUrbdt5F1_RGVgdAId59w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf0cf36cd.mp4?token=D1lsWgCXYWF5SL4PMMqjPgDVLP8TJMV81dgdiLHnJRWSXiWO0I-g4ZEGsK_zbXAviSv28C3-ts2JZqx8dSIrLVMdsk-gsbIw0A4xX_WHj1BK7suRlAkm3sryb-ozFU_ah8PrDi0wegjfFfTTzqrrUPG_7BG0-PT4_DpiwkbWwXP5Zw9XZxAgN7mN0JSw7rAHZToX_yKoj2RBTjEtwaPXjOn9I0Y53mRfAWylxisEEiko4QK0Z-0PxKx0d_75459ABTMKHR_0Ie9I2jMD7NMROFVOSlQtychUNW9G1Q70hk1NKqYkzZJy3CKyDog4LYzVzUN0kSufqDjqswjfe6zMOxPoULYDs_jerZ-mbMe3T9G_rn5pnmPBv8nDigLbyjPT8boECo3ZRQORb8nIBKdj6oc0y7aI4WcV1dwPwEotWrBhvEQ-qrDlPISPMiOcNPVgya3DVbyceWNmjzITdzWYB8G3qhyLRMmuoXwr4jRVk7XGFV7D4JWG5pyUxVqVjck0ohGz5rFiL08AUAJmjjEpPm5voPfNYhdrVqA-Fg8d78sZ2vNFymwzg_X1-ykP8BjPlVjEP7RYGZIrfMGRbIW7ZyKpZ8VLYTFVq97ljcj3CeBZHO8CfHFnlVxUR29cZqUydZClWzk4OM32MVQPlFSaWWVUrbdt5F1_RGVgdAId59w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: عملية جزيرة خارك لم تعد مطروحة الآن.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/78464" target="_blank">📅 23:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db4faddc2.mp4?token=OWsfCjT96J4TnmXz_PwWEWEo9I4unG5DYoOn5bCzCZvRQhG1qIshFDZIsTyTYZZsUr_exxJt95gPFhHaKTFL5J2wzmpxu9_tBk31rzJXBfdRE257yTuD36ueuVIqzWFACC_epeCK93foPU1DSs7G0Hn1vtYRkctorh8d1zYw3I7ZkGusWdmsVj9IKm9YiZQSSFoRo3QvEO4bbg3Pwevask139qm_u7Jtoi05cJCufT0b1PDCrGjpWf6M5-m1FqKUCaklgxpXDfaWVfK-x9ZuuG5udOkdwjnYRD5c67FmKM1h7ZXjARdCvkms79ElyxKLzPgkNS4nXZJT6ShkBiwQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db4faddc2.mp4?token=OWsfCjT96J4TnmXz_PwWEWEo9I4unG5DYoOn5bCzCZvRQhG1qIshFDZIsTyTYZZsUr_exxJt95gPFhHaKTFL5J2wzmpxu9_tBk31rzJXBfdRE257yTuD36ueuVIqzWFACC_epeCK93foPU1DSs7G0Hn1vtYRkctorh8d1zYw3I7ZkGusWdmsVj9IKm9YiZQSSFoRo3QvEO4bbg3Pwevask139qm_u7Jtoi05cJCufT0b1PDCrGjpWf6M5-m1FqKUCaklgxpXDfaWVfK-x9ZuuG5udOkdwjnYRD5c67FmKM1h7ZXjARdCvkms79ElyxKLzPgkNS4nXZJT6ShkBiwQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: وجدنا إيران عقلانية، وستتوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/78463" target="_blank">📅 23:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">المراسل: ما مدى ثقتك في أن هناك توقيعًا سيحدث في نهاية هذا الأسبوع مع إيران؟  ترامب: سيكون ذلك قريبًا — ربما في نهاية هذا الأسبوع.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78462" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3173a00b9.mp4?token=VGqZJhP0uBxTSZJtNwJ35F-lNgRYFB1vTconbjZxppj627k2atMMGWsn2eJP7Chi7Y8g6cCkIq-CCXn9HVe4d5vgehYr1V_utpAXrMMwuDwJm8WJ3q547p5qRqHMk2Kwv0mElTQaBaybAIm7j8zLIiWFrgNS8bAckThyf9LzD6Q2PmSnBfAikesM9vEImB-Rf5OUMYfqDVr0FZNYtZD9CYr2clhwsiGgxU52gAzYRMLh3dGEnUjQbGsPVKvO2CTGzk6Jy8PQtummWx8EQHOwbTFetnen-LvM4XihN_AQ-t45IkD641BPFMB-KRvro-_JFOp3ZnQ6ulyNFUnaqw_9uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3173a00b9.mp4?token=VGqZJhP0uBxTSZJtNwJ35F-lNgRYFB1vTconbjZxppj627k2atMMGWsn2eJP7Chi7Y8g6cCkIq-CCXn9HVe4d5vgehYr1V_utpAXrMMwuDwJm8WJ3q547p5qRqHMk2Kwv0mElTQaBaybAIm7j8zLIiWFrgNS8bAckThyf9LzD6Q2PmSnBfAikesM9vEImB-Rf5OUMYfqDVr0FZNYtZD9CYr2clhwsiGgxU52gAzYRMLh3dGEnUjQbGsPVKvO2CTGzk6Jy8PQtummWx8EQHOwbTFetnen-LvM4XihN_AQ-t45IkD641BPFMB-KRvro-_JFOp3ZnQ6ulyNFUnaqw_9uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الولايات المتحدة سترفع الحظر عن إيران بمجرد توقيع الاتفاق.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78461" target="_blank">📅 23:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
‏ترامب: تم إبلاغي أن مرشد إيران وافق على الاتفاق.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78460" target="_blank">📅 23:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8be63313a.mp4?token=SmPQmMujRKfbSA2vhgIKkyV1LT5DIHpZXnoPTfiJ8wFtpspoC3a9tj3_Vde_zDsue3xwUGfPGR3R9e4Ny8rMM6kxpZxs9NwwXKJqGUwQq7OvB8cDSUULXcaJr6ieBPt1WV0p0fXUn-V8JC8sQb4HCphEWAopEHJvVW8yg9ejAyZaf-cqU1liAMeQUBxEOTH_6wr2DjMfmHrVGnAT8jlTcK8dgFpFtdGNy9ByAfcDhTtvBtPognqPzIFfM4lq9Utp5vuqVI9of1lcEctpVw_tcqyri6BeYsyuC-7Zm0TcmCpjvYFSlL4EHDHvaAFEh1Et5M9cF47H-HgDeN_y5IHPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8be63313a.mp4?token=SmPQmMujRKfbSA2vhgIKkyV1LT5DIHpZXnoPTfiJ8wFtpspoC3a9tj3_Vde_zDsue3xwUGfPGR3R9e4Ny8rMM6kxpZxs9NwwXKJqGUwQq7OvB8cDSUULXcaJr6ieBPt1WV0p0fXUn-V8JC8sQb4HCphEWAopEHJvVW8yg9ejAyZaf-cqU1liAMeQUBxEOTH_6wr2DjMfmHrVGnAT8jlTcK8dgFpFtdGNy9ByAfcDhTtvBtPognqPzIFfM4lq9Utp5vuqVI9of1lcEctpVw_tcqyri6BeYsyuC-7Zm0TcmCpjvYFSlL4EHDHvaAFEh1Et5M9cF47H-HgDeN_y5IHPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: تم إبلاغي أن مرشد إيران وافق على الاتفاق.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78459" target="_blank">📅 23:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابة ميركافا تابعة للجيش الإسرائيلي في محيط بلدة طير حرفا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/78458" target="_blank">📅 23:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭐️
وزارة التربية العراقية تنفي تأجيل موعد امتحانات السادس الإعدادي أو تسريب الأسئلة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/78457" target="_blank">📅 23:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامب: لن أتمكن من حضور مراسم التوقيع، وفانس سيكون حاضراً في توقيع اتفاق إيران.  توقيع الاتفاق مع إيران قد يتم قريباً، ربما خلال عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78456" target="_blank">📅 23:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb7b99701.mp4?token=Rje9y-qOMUQDLBQLUh71FLawQ75amkOo0KsA7ejrLQ-E5JhjRRHypDL6LPHcqYa5iF3TRsu-UOj0AiVSxWTe8zqLxwEeMp8oK-E5pYJ8y93GvOedruobMDu8WzrRakdI8TmMibEUN48AeG7gMOMEfbyAXK6qzR36gOkAfpd4wKI-PdiotQM1IoOp7ttBp068urvFWSfS2DNdtXxE1jSJ6rC4uATMfn-iOgoJlM93Z7wNHSMBKTxOlxpp_PoB_iEn3uYCRLxQFXOkKKWgOzA0O9fRHHRqlCMmpgXlZGgww-N7UeE32sbpvbyTP2HvWoJWdagfSv0N96pBzWKyig6S0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb7b99701.mp4?token=Rje9y-qOMUQDLBQLUh71FLawQ75amkOo0KsA7ejrLQ-E5JhjRRHypDL6LPHcqYa5iF3TRsu-UOj0AiVSxWTe8zqLxwEeMp8oK-E5pYJ8y93GvOedruobMDu8WzrRakdI8TmMibEUN48AeG7gMOMEfbyAXK6qzR36gOkAfpd4wKI-PdiotQM1IoOp7ttBp068urvFWSfS2DNdtXxE1jSJ6rC4uATMfn-iOgoJlM93Z7wNHSMBKTxOlxpp_PoB_iEn3uYCRLxQFXOkKKWgOzA0O9fRHHRqlCMmpgXlZGgww-N7UeE32sbpvbyTP2HvWoJWdagfSv0N96pBzWKyig6S0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد أن زعم جيشه أن المضيق مفتوح.. ترامب: سيفتح المضيق فور توقيع الاتفاق.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78455" target="_blank">📅 23:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامب: توصلنا إلى اتفاق يمنع إيران من امتلاك سلاح نووي.  تحدثت للتو مع نتنياهو.  وثائق إيران في مرحلة نهائية تقريباً.   تحدثت للتو مع قادة قطر والإمارات والسعودية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78454" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3470ffac2.mp4?token=D8Bi3oWeKDMz55wczI0vNhEDPA03tOOjDtl5iTxLmfRAEC-coh6yvi_87ZLaGQtzGIf2PgrwA2zt5IQCnCtNrOk4QY4S9bz0dkM6PuIDfcF52OlWJGzDj8WCkybTOCmrt445wtBib2WmCizoDpZDL4N3169W04d1dsXu3mlNaKxPVGg1an1FHHQu8ljmvKhTAxIlqcwwChNEHOwlKbDgpGynmjEwOYCOxXbGCfRMDgo-WPw_yxR1wz_QE0Z4vN_gPD1SVM5qrvcdgME7E7qIwAUa5UjMNsMXpyvFKzD7hfDR-L5hQJqk5ALIFbAbhPUlLQWQ7DhdUUriCB52zHVAPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3470ffac2.mp4?token=D8Bi3oWeKDMz55wczI0vNhEDPA03tOOjDtl5iTxLmfRAEC-coh6yvi_87ZLaGQtzGIf2PgrwA2zt5IQCnCtNrOk4QY4S9bz0dkM6PuIDfcF52OlWJGzDj8WCkybTOCmrt445wtBib2WmCizoDpZDL4N3169W04d1dsXu3mlNaKxPVGg1an1FHHQu8ljmvKhTAxIlqcwwChNEHOwlKbDgpGynmjEwOYCOxXbGCfRMDgo-WPw_yxR1wz_QE0Z4vN_gPD1SVM5qrvcdgME7E7qIwAUa5UjMNsMXpyvFKzD7hfDR-L5hQJqk5ALIFbAbhPUlLQWQ7DhdUUriCB52zHVAPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: قريباً توقيع اتفاق مع إيران.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78453" target="_blank">📅 23:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامب: التسوية مرهونة بالتوصل إلى اتفاق خلال الأيام المقبلة، وتوقيع اتفاق إيران قد يتم في أوروبا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78452" target="_blank">📅 23:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب: توصلنا إلى تسوية عظيمة للصراع مع إيران.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78451" target="_blank">📅 23:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b447a8a70.mp4?token=tlidqusT07yW24Bq9CVLI3E8MtxmpaovRZ6Z1W48B79oMwTLk6q47ktvrfuLZ2mp7cE184l0D5Z9QbTQkCFI5HQtntut8mlJCrjHvxC_0K1ANBJ2GiZhLBzgtTsL_ZcNT7ZA35Y5sJ01iyrwceUkvi183Me1F9B_0PO3BjCpg1BrrXaQ_FdpYfNyFFSRRfculmJZnG-O3CyaPekvp-WNrDYnHf5I4IEKmowMNTh31WbPOc0Ugz8ImUIn-0iAfHYQsUy94mF_SrKWp4A3UiW_iarVMkrwaxfn2TO6TmNaMqeWlusU7OcVVyVWtCCp3MzJ4a15ZDhk4VNFwlNpuusCTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b447a8a70.mp4?token=tlidqusT07yW24Bq9CVLI3E8MtxmpaovRZ6Z1W48B79oMwTLk6q47ktvrfuLZ2mp7cE184l0D5Z9QbTQkCFI5HQtntut8mlJCrjHvxC_0K1ANBJ2GiZhLBzgtTsL_ZcNT7ZA35Y5sJ01iyrwceUkvi183Me1F9B_0PO3BjCpg1BrrXaQ_FdpYfNyFFSRRfculmJZnG-O3CyaPekvp-WNrDYnHf5I4IEKmowMNTh31WbPOc0Ugz8ImUIn-0iAfHYQsUy94mF_SrKWp4A3UiW_iarVMkrwaxfn2TO6TmNaMqeWlusU7OcVVyVWtCCp3MzJ4a15ZDhk4VNFwlNpuusCTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: توصلنا إلى تسوية عظيمة للصراع مع إيران.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78450" target="_blank">📅 23:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRYdLyBpibsi8fDuwqyy_otwA3_EzFC1LoHEyd1QAqVrnWASJQl2LBOu7hgnewDuEwNFjppxD4LWfJ0Dz2YtkuXYgCzvSdtYR1WxbPz9JsmvqpBnFn9KBH5A8CIxLIuOCwhvO2NT9O469_N-gx0Gpon3nQF118itwb-qkg_ax-6_Qt-Rv1o4Zq3v8QpDcXo9x6y43qJUn_rqEqJUUXpCcw-fUJZJG11-pw61KDViQBWQho-QNwT1wkpfcGljK4tLt7sL1Tck6n3R6LQbyneM35S81fqDZe3--qeWIZcziSmOEtIWCh6XsIoTulm9VzrcU8orkwXEUZSqBFBSHdes0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية "إسماعيل بقائي":
‏لقد تحطم جيشه في ليلة الأحداث. ‏من كان صالحاً في موقف السلام، فإنه يقرع طبول الحرب.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/78449" target="_blank">📅 22:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭐️
نيويورك تايمز: قبل إلغاء الضربات المخططة على إيران يوم الخميس، تحدث ترامب إلى الوسطاء الباكستانيين، الذين أخبروه أن لديهم "اتفاقًا" مع إيران.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/78448" target="_blank">📅 22:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن إسقاط مسيرة صهيونية من طراز "هرمز 450" بصاروخ أرض جو في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78447" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#رياضي
⭐️
انطلاق بطولة كأس العالم 2026 بمواجهة المكسيك وجنوب أفريقيا.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/78446" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭐️
سي إن إن عن مصدر مطلع: إيران نقلت عبر وسطاء قطريين في وقت سابق أحدث مسودة للاتفاق المقترح مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78445" target="_blank">📅 22:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
في الجيش الإسرائيلي يقولون بأن حزب الله يستعمل محلّقات مفخخة عبر الألياف الضوئية بمدى 20 كم.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78444" target="_blank">📅 22:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78441">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkbxUE89wYl5bPIwbOrYflRUIWOf27npFNImZ0-huufDPB3hS3qZMrWhLrZ-eq7hLO1UVtrd9jvR0fbyOBT-T-XRIZc3JOOkxkzvx6hh5i8mq64cw2krJw6BBl8rE5eSYYwiIcqlcIvHVUA_T3wZBxTeAdoB_C9DSdLET8fszwYWIOI4gaVjwB8635m_UvYdL-4GDWLUU6LoBxlBF9YrVtkhEHr2-B9x-bmLcSIqa8uPDN0FNlgBfYLXJ_cuxm0feyx0k20ctZbv-p3FJlQcZdPOqHuhaWFBns5EUOOf_saKP7AGx8n_4FzZZB_bHJSvRcFFiz5oaELoESOQT8nIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_bH_F5r_zejgH8T3sV8cgXnSm_FJctUuuS80YgUQbzyHgjQklNNyKI50I1jrkOV63OjTdpqnDaAiziZXlX5_mjJ9N11EQMNE2hsbVkAfBtU_xbOOabvSgEvG00tsnZ_P4t74KT44lrdY9vHmKmbJkKDmbPBkqo5Pofeb2qOIQgQrG-76dX8kYSXWkNlLEKZHf1SrlSc1g9UpWUUaEinAWdjeU2XYf_pz6mRQILWI4K0Yu6qc_4We5LgdMk025csBBaC_fRVJew6pXaex4m3o8NKkIy1zdHpXGIPrpSE4AAZ9qGKPq2oQJ1CwvBELFO4zv1aHZwCXvHOUYgEB_HEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sejCGtgp0kA6C7s6I2-JzsMAQUJ9HQsa0sE_fMyP3WsRWYkMNJUdj55d9qhkN5GV_8LYLFb5cZ0zgSzw0MNAAhpJuQ86Hy6Y63IREjuSStKe7PquQyrbvsp-hGTSWO3BUwOJ8VNppgng_GZ-6m4GpnUWz_qyc-25cU4exhYm3QbWLJ1ZFPODaGsebZa7gtK8io4aGnFEfr5O46zf5ZqX04bZ3IiSIES-bdXxXmZ49sqnp00V2ud5XRpuZgmOyA9bQZByfukSDPScgmywpyIibTx1QPvWSO9xFF6H4RN5jtG80gdeM6J-1GrswyhbAFJnCHzwE_VrhCVIeRaUrO11hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
خلية الإعلام الأمني العراقي: ضربتان جويتان تستهدفان مفرزة إرهابية تضم قيادياً جنوب بهرز في ديالى.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/78441" target="_blank">📅 22:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78440">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭐️
سي إن إن عن مصدر مطلع:
إيران نقلت عبر وسطاء قطريين في وقت سابق أحدث مسودة للاتفاق المقترح مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/78440" target="_blank">📅 22:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78439">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-SEwXQEtEwOWY1xXz_9H9mB-kNnmivG8oqEMN4kzY-EoNYejgPxlHIlsmjO5tzSgMjPtPc2HqcUUZxMoe1HaZhw1EqrA_Up3wvZdGIOmL5Z3Chotac9v8V4MF-VuJARJiZUytrvpKvTXfpPztDWb9js8PvC9xBnOF9IefdpiLaMskI0UDxT6xNC7mLDH2OSA4Wc6V43kc9sKhmMIkD-4HAanhVV8WE3QTTbHucTL2MNcY8blt7QgWuv4f0iT7kftoelXp2CYBuoy1fBWThak2JBlQP9KjhiNbqu_Qh1jSsf-pcuy6AIlpPVWEulPvLSEfMoWRBidqnWpqVrdywZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
عصابات آل خليفة في البحرين:
القبض على 3 أشخاص إثر قيامهم ببيع ملابس عبر مواقع التواصل الاجتماعي ، مطبوعا عليها صورا وشعارات تحريضية ، تتضمن تمجيدا لعناصر إرهابية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/78439" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78438">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
ترامب: واستنادا إلى حقيقة أن المناقشات مع جمهورية إيران الإسلامية قد رفعت إلى أعلى مستوى من القيادة الإيرانية وتمت الموافقة عليها، فقد ألغيت، بصفتي رئيسا للولايات المتحدة الأمريكية، الضربات والتفجيرات المقررة ضد إيران هذا المساء. تمت الموافقة على المناقشات…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78438" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78437">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
أمين سرّ مقرّ تشييع قائد الثورة الإسلامية: لا توجد أيّة خطط لإقامة مراسم الجنازة في الخارج، وجميع الترتيبات جارية داخل البلاد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78437" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78436">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
الإعلام العبري: في إسرائيل يوجّهون التعليمات ؛ لا نعرف عن ماذا يتحدث ترامب، نحن مندهشون. في إيران ينفون ؛ ترامب ادعى مؤخراً 38 مرة أن هناك اتفاقاً. حتى يتم نشر بيان رسمي من إيران - يجب اعتبار هذه التصريحات كذباً.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78436" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78435">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
ترامب: واستنادا إلى حقيقة أن المناقشات مع جمهورية إيران الإسلامية قد رفعت إلى أعلى مستوى من القيادة الإيرانية وتمت الموافقة عليها، فقد ألغيت، بصفتي رئيسا للولايات المتحدة الأمريكية، الضربات والتفجيرات المقررة ضد إيران هذا المساء. تمت الموافقة على المناقشات…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/78435" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية تصدّي المقاومة الإسلامية بتاريخ
02-06-2026
لمحاولة آليات وجنود جيش العدو الإسرائيلي التقدّم باتجاه بلدة حدّاثا جنوبيّ لبنان بصليةٍ صاروخيّة وقذائف المدفعيّة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78434" target="_blank">📅 21:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏الكويت تبث مشاهد للحظة القصف المركب الذي استهدف مطار الكويت واسفر عن اضرار جسيمة</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/78433" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني:
نحن على أهبة الاستعداد للردّ بحزم على أي خطأ من جانب العدو.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/78432" target="_blank">📅 21:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
ترامب: واستنادا إلى حقيقة أن المناقشات مع جمهورية إيران الإسلامية قد رفعت إلى أعلى مستوى من القيادة الإيرانية وتمت الموافقة عليها، فقد ألغيت، بصفتي رئيسا للولايات المتحدة الأمريكية، الضربات والتفجيرات المقررة ضد إيران هذا المساء. تمت الموافقة على المناقشات…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/78431" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامب يتراجع عن قصف ايران وتدميرها للمرة الألف بعد ان قصفها في التواصل الاجتماعي لمدة ٩٩٩ مرة</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/78430" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هههههههههههه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/78429" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78428">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNWVOPWrxLHe7K2K3l8bEnGPAnKVwTFJAnYAtQwWnXWOTHFNmzikXwfIcVvk50Hr4JKVV6OetgbXzFfIqI-2kGCrmeToZOz9i_g-JITOeAgCD81wVwO81_av6u9K5yDuJmIEUX-YNeMTjFAdzN_AkbonHgKp53TX1-7-CLUcMbT0tlMYG-xGsYwLrjVbWzvXe4oT_UP_WMJezi4gYT4W8uE3v4oKBd9aRV0RdkAFjCRK4g6q1Wwi8kiruo_XwUWvpSDW_td6BbBrP4tJbMbk0APcKGQ2uITF_gWiwtR8bBb5W51bzBH9sEr0WCZnWAE52yzSGNo7Tiekw1hu-AzVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
واستنادا إلى حقيقة أن المناقشات مع جمهورية إيران الإسلامية قد رفعت إلى أعلى مستوى من القيادة الإيرانية وتمت الموافقة عليها، فقد ألغيت، بصفتي رئيسا للولايات المتحدة الأمريكية، الضربات والتفجيرات المقررة ضد إيران هذا المساء. تمت الموافقة على المناقشات والنقاط النهائية، في كل من المفهوم والتفصيل الكبير، من قبل جميع الأطراف المعنية، بما في ذلك الولايات المتحدة وإسرائيل والمملكة العربية السعودية والإمارات العربية المتحدة وقطر وتركيا وباكستان والبحرين والكويت والأردن ومصر وغيرها. سيظل الحصار البحري ساري المفعول والتأثير الكامل حتى يتم الانتهاء من هذه الصفقة - سيتم الإعلان عن وقت ومكان التوقيع قريبا.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78428" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78427">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
وزارة الدفاع الإيرانية:
أي خطأ من جانب العدو سيُقابل بردٍّ يفوق الخيال.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78427" target="_blank">📅 20:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
انتشار فرق وعجلات الإطفاء والقوات الأمنية الأمريكية في محيط مبنى البنتاغون.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78426" target="_blank">📅 20:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
قائد المقر المركزي لخاتم الأنبياء:
من جهة، تتحدث الولايات المتحدة عن الاتفاق والتفاوض، ومن جهة أخرى، تتصرف بخبث. هذا التناقض الصارخ بين سلوك الولايات المتحدة وخطابها هو السبب الرئيسي لانعدام الأمن في المنطقة، وقد عرّض أمن التجارة والاقتصاد الدولي والدول للخطر، ولا سيما مضيق هرمز.
‏ إن قادة الولايات المتحدة، بسبب افتقارهم إلى الفهم الصحيح للأمة الإيرانية الشريفة والشجاعة وقواتها المسلحة القوية، عالقون في حلقة مفرغة، والأكاذيب المتكررة للولايات المتحدة هي إحدى علامات ذلك.
‏ لا يمكنهم أبداً التعويض عن إذلالهم وهزائمهم المتتالية في الحرب مع إيران الإسلامية أو إخفاء نزعتهم الحربية من خلال الدعاية والحرب الإعلامية.
‏ نحذر من أنه إذا حاولت الولايات المتحدة شن هجمات ضد إيران البطلة مرة أخرى، فسوف تتلقى رداً أشد من ذي قبل، وستصبح نيران الحرب أكثر انتشاراً واتساعاً، مما يتسبب في انعدام الأمن في المنطقة.
‏ بالنظر إلى التهديدات الأمريكية الأخيرة ضد البنية التحتية النفطية الإيرانية، يُعلن أنه إما أن تكون صادرات النفط والغاز متاحة للجميع أو لن يتمكن أحد من القيام بذلك.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78425" target="_blank">📅 20:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
أمين سرّ مقرّ تشييع قائد الثورة الإسلامية:
لا توجد أيّة خطط لإقامة مراسم الجنازة في الخارج، وجميع الترتيبات جارية داخل البلاد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78424" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي يزعم:
لا يزال مضيق هرمز مفتوحًا للعبور.
تم إنشاء مسارات آمنة للسفن التجارية التي تعبر مضيق هرمز.
المسارات متاحة لجميع السفن التي لا تنتهك الحصار المفروض على إيران.
عبرت مئات السفن في الشهرين الماضيين.
القوات الأمريكية في حالة تأهب للدفاع ضد أي عدوان إيراني.
إيران لا تسيطر على مضيق هرمز.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78423" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd5e6ba15.mp4?token=iRkyDtz2AD3lRAcBnGT4lFDk0uZBdPyLUfomwlvkHDyQDowJAP12QPtTSBlxfpTak03FoDKFKNFDdqGoBtkM5TVwWrxnGS6lO7cQ7vg6IA_vLEVHLDafmu-ETJpBvIdoMeT8-5V9oiX60PKU1Dpl9ZLT5czBGAJcD8urQGbAQgtwT5h7Abm5giN2KGvZbKYdrdPr02-5vsnxNYNHuenCM9L1YTAV3SjXT-mhs4PPcLe_kvNZ3O05ldCUFf61hZX4ARg21kKZJD6K0PRSQ8ytta5BqJOiu-GZUZbZuW7bYIWwDhRXrqqgx6tAToccReUe08FgHLyTQhYZQN33q9bSvasq0Z7Kr6cECnrl0Ug6k0SKV9E-5mjbx-Jqt6AbTrwOme_mlUR4lfumoBVJgPH8bsdzZKEYzqqnPsoypsN-OFns2RFu-V-RbnI8lN9BqGA9_j0XOlF6G6oC45PagBiXvKkHfqnDuvvdMTuZJ7bZZH2KIG1gksw6CFAKVJkitrDEnftNRm0mvzFjOO2dvleLAQgxYNdyE1EyX8dS8myKvCx1ztpDmG57brQF9LaHRx1e59QgQg-b_OWyUIoo4qekw1l-5nXgCInnwX-726OxBB2St-wjoj7aUoUFvqueYGPtrmO_5H-6UwpOqleMaMcc49f1zrnfPusgzN3dMUDim8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd5e6ba15.mp4?token=iRkyDtz2AD3lRAcBnGT4lFDk0uZBdPyLUfomwlvkHDyQDowJAP12QPtTSBlxfpTak03FoDKFKNFDdqGoBtkM5TVwWrxnGS6lO7cQ7vg6IA_vLEVHLDafmu-ETJpBvIdoMeT8-5V9oiX60PKU1Dpl9ZLT5czBGAJcD8urQGbAQgtwT5h7Abm5giN2KGvZbKYdrdPr02-5vsnxNYNHuenCM9L1YTAV3SjXT-mhs4PPcLe_kvNZ3O05ldCUFf61hZX4ARg21kKZJD6K0PRSQ8ytta5BqJOiu-GZUZbZuW7bYIWwDhRXrqqgx6tAToccReUe08FgHLyTQhYZQN33q9bSvasq0Z7Kr6cECnrl0Ug6k0SKV9E-5mjbx-Jqt6AbTrwOme_mlUR4lfumoBVJgPH8bsdzZKEYzqqnPsoypsN-OFns2RFu-V-RbnI8lN9BqGA9_j0XOlF6G6oC45PagBiXvKkHfqnDuvvdMTuZJ7bZZH2KIG1gksw6CFAKVJkitrDEnftNRm0mvzFjOO2dvleLAQgxYNdyE1EyX8dS8myKvCx1ztpDmG57brQF9LaHRx1e59QgQg-b_OWyUIoo4qekw1l-5nXgCInnwX-726OxBB2St-wjoj7aUoUFvqueYGPtrmO_5H-6UwpOqleMaMcc49f1zrnfPusgzN3dMUDim8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إجلاء أشخاص من عدة طوابق في البنتاغون</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/78422" target="_blank">📅 19:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/216e6c3a98.mp4?token=aEOIwGTsqeGbDE3xufHEXHidBd5y2kCQ6xCaflwRZOM7riVTHZWjALS4QGVVk0GDAtWGcg6IeMmDlwIoNVBHI8SCZzmBobClDyk2DrEEW-zKIjfdHFq_1IfFHYMgxXMQW48qhbjlNGhlk_RMoN7L4HRqsull-BnbqakKDXekTZ4l_M2NfaUasBqxz_K-203Ib55mSV8SRfFY0IbuGWy7sRVTcjuaIWCvXiY1KGqRlwcpbLLvya8JEjJSQreh2k7CAuxKPt6_T_UhnSfeMBcxy2ipZdKbHejMYSI4PPmGGlAJrGUZX7rrORCD-cJdrn2r6vzoaq6eLeIv3Kbkfkr9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/216e6c3a98.mp4?token=aEOIwGTsqeGbDE3xufHEXHidBd5y2kCQ6xCaflwRZOM7riVTHZWjALS4QGVVk0GDAtWGcg6IeMmDlwIoNVBHI8SCZzmBobClDyk2DrEEW-zKIjfdHFq_1IfFHYMgxXMQW48qhbjlNGhlk_RMoN7L4HRqsull-BnbqakKDXekTZ4l_M2NfaUasBqxz_K-203Ib55mSV8SRfFY0IbuGWy7sRVTcjuaIWCvXiY1KGqRlwcpbLLvya8JEjJSQreh2k7CAuxKPt6_T_UhnSfeMBcxy2ipZdKbHejMYSI4PPmGGlAJrGUZX7rrORCD-cJdrn2r6vzoaq6eLeIv3Kbkfkr9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
السلطات الصهيونية تقرر إيقاف حركة القطارات مؤقتًا بسبب حالة الفوضى واقتحام متظاهري الحريديم للسكك الحديدية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78421" target="_blank">📅 19:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8-Ux9GVNR1WCsUUKvWj7kUdyGOKgvZbvMy9NrEQCr9-8ijSAZgEyUN3fqXfcTQx6Xgrs4kl0O7Hs76Ti_lWz_fNmRIC4NsbABKXWTODeXlYV4qg8Svns8sSbkLNwj0ZIgYYvajRyxb5QuHYsiyGM-0wfIHTzIL3Nuv4ygTKqh1JMFwE3Gp2QsTycXY4R8HcEWf8T1a57_0drZDGxrg3z7F9JNekGA1aIPvP9qUW2hhgRXfUwp6LmW6IJ13JJUYpLiX9AoA384uDwAm5cFi7cl-a6flPnTYWGKZnicsh1T-TKW0TPcRv5qlFjPszcZajaczD40UHSIan8I4iO49BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
ستعيد الاستراتيجيات الخاطئة والقرارات المتسرعة ضبط مجلس الإدارة بأكمله نحو الأسوأ، وتفجر البنية التحتية للطاقة والأسواق وتخلق مستنقعا لا نهاية له ستظل عالقا فيه لسنوات.
سترى إيران مختلفة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78420" target="_blank">📅 19:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3857e4ec6.mp4?token=Wixlvc_iE_hxugL5RWWSD1ZzKzdwlImTp38eKoQdou23UtRt3Tg7LGG3cl_vJ7Sxzx_BdJ8xeqILSgv4lsrhFywIpBr4uevHln_bNwPb7cl9hDjF5HnfCTawu8iSfkmlv8bnQfQsdRoZ5ClxVdlBIW5_jJTgBXGBh7uWGSKChPt52eWFcvomIuQUG5Z2Nmcvld799Wo-yD12neqxQS5rrVnFXY8of0SXB-6EzMqLYD1s69J2AmyQmTbUdQsXqk6gc-txotSG5vq9OCdRsZ7MEM3PhpR_AS6nM00-u_faySIvjpltQgQkwKJLCg5eKOWmalo5c_HSrP7W4pGSclXbpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3857e4ec6.mp4?token=Wixlvc_iE_hxugL5RWWSD1ZzKzdwlImTp38eKoQdou23UtRt3Tg7LGG3cl_vJ7Sxzx_BdJ8xeqILSgv4lsrhFywIpBr4uevHln_bNwPb7cl9hDjF5HnfCTawu8iSfkmlv8bnQfQsdRoZ5ClxVdlBIW5_jJTgBXGBh7uWGSKChPt52eWFcvomIuQUG5Z2Nmcvld799Wo-yD12neqxQS5rrVnFXY8of0SXB-6EzMqLYD1s69J2AmyQmTbUdQsXqk6gc-txotSG5vq9OCdRsZ7MEM3PhpR_AS6nM00-u_faySIvjpltQgQkwKJLCg5eKOWmalo5c_HSrP7W4pGSclXbpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
خلية الإعلام الأمني العراقي:
ضربتان جويتان تستهدفان مفرزة إرهابية تضم قيادياً جنوب بهرز في ديالى.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/78419" target="_blank">📅 18:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38df04259a.mp4?token=BM3wX-VDMydmWjFJzd3feAA5zHNI_J9pw36jvD0aUyyBe8UaKs98ksuLLZvdVPwnhiF6jO4Puq6MOIVnmSm6OQpZN3j5qhcD7v45qzqAOcmAEcZBk7vOFqSXSZOP7utNKdxp_wgNCrUIL4wwD4r1OslXWNq9ZFIMIWO9LdM6tY5mgptRFB6xUEYreF2-UJyw6ZSJxLsC3_jBVZtimnWg4SDpdDh4h3ebBMW5OH5xOUmUdNvXNHHzFpbTKfSY0SEmTP1fw8ydYlaCZ-cfz1gvNEJPv_IqgcRlGsQCvzwXHNBjUAVfAuCeOgHxXCkgRYpnqDBnU8xhN9aWOCV8KykgBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38df04259a.mp4?token=BM3wX-VDMydmWjFJzd3feAA5zHNI_J9pw36jvD0aUyyBe8UaKs98ksuLLZvdVPwnhiF6jO4Puq6MOIVnmSm6OQpZN3j5qhcD7v45qzqAOcmAEcZBk7vOFqSXSZOP7utNKdxp_wgNCrUIL4wwD4r1OslXWNq9ZFIMIWO9LdM6tY5mgptRFB6xUEYreF2-UJyw6ZSJxLsC3_jBVZtimnWg4SDpdDh4h3ebBMW5OH5xOUmUdNvXNHHzFpbTKfSY0SEmTP1fw8ydYlaCZ-cfz1gvNEJPv_IqgcRlGsQCvzwXHNBjUAVfAuCeOgHxXCkgRYpnqDBnU8xhN9aWOCV8KykgBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات مسيرة تستهدف مواقع المعارضة الكردية الايرانية في قضاء قوشتابا بمحافظة أربيل</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/78418" target="_blank">📅 18:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في جنوب إيران</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78417" target="_blank">📅 18:48 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
