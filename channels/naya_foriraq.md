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
<img src="https://cdn4.telesco.pe/file/O3VZugERr3gM7CQiSTcVqj89hixXkwZw9cpdU05JpmpRGBg-Y-60U8JyZs-qratoAIxlg-qVUYkA4iAv8nOZBIeboT950jFN-J1fH-GzRmlK77o0KtipIBru0WjsK_0tGJ1vMLXlza_2F0QXWj0LaiiMAm5DJGeayzoZgXaq4Rul0fukZua2VBNh9TUHiOe0mx5pLRbzU4eUEmkTI_WBv7h8A__92AXbaRZ3EHiIONdZejXNh25DdPisBjcPkR9j6Nb3F-NaFkCI_I5K5IPmu14IGY9cs3o3PDr3nk2gKgXtA7zbUP8kBtcEukYQEXXfTBqMnvOHicqtARUPpWIRaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مصدر لنايا   اغلب الفصائل التي رفضت فكرة النزع بناء على تغريدة ابو مجاهد العساف و الكعبي و الجعفري هي الفصائل الوحيدة التي استخدمت السلاح منذ حادثة يوم المطار حتى الان وبصورة فعالية ميدانية ذات تاثير واضح " عدا فصيل الغراوي " الذي لم يظهر له موقف واضح حتى…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/naya_foriraq/76916" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏴‍☠️
‏
مسؤولين إسرائيليين:
التقديرات بأن إسرائيل ستهاجم بيروت خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/naya_foriraq/76915" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
‏
ترامب:
علاقتي بنتنياهو ممتازة وهناك توافق بيننا في قضية لبنان.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/naya_foriraq/76914" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله حول ادعاءات العدو الإسرائيلي الكاذبة بشأن مستشفى تبنين الحكومي:
يواصل العدو الإسرائيلي إطلاق الأكاذيب والافتراءات، مصوبًا سهام التحريض والتضليل نحو الشعب اللبناني تحت غطاء الحرص عليه وعلى أمنه ومستقبله، وآخرها المزاعم التي أطلقها بشأن مستشفى تبنين الحكومي، في محاولة مكشوفة لتوفير غطاء سياسي وإعلامي لاعتداءاته المتكررة على المستشفيات والطواقم الطبية والهيئات الصحية والمسعفين، والتي تشكل انتهاكًا فاضحًا للقوانين والأعراف الدولية والإنسانية وترقى إلى مستوى جرائم الحرب.
إن هذه الادعاءات المختلقة تُعدّ تهديدًا علنيًا للمستشفيات اللبنانية والمؤسسات الطبية، لا سيما بعد الاعتداء الأخير الذي طال محيط مستشفى جبل عامل، وأدى إلى إخراجه عن الخدمة وتعريض حياة العديد من المرضى والطواقم الطبية للخطر، بما يؤكد النوايا الحقيقية للعدو في توسيع دائرة استهدافه للبنى التحتية المدنية والصحية والحيوية، وتدمير كل ما ينبض بالحياة، وضرب مقومات الصمود، بهدف بث الخوف والضغط على أهلنا الصامدين وثنيهم عن التمسك بأرضهم.
إننا ندعو المجتمع الدولي والأمم المتحدة والمنظمات الدولية والإنسانية والصحية إلى التحرك العاجل وتحمل مسؤولياتها إزاء هذه التهديدات الإسرائيلية الخطيرة للقطاع الصحي في لبنان، وعدم السماح للعدو بتكرار جرائمه بحق المستشفيات والطواقم الطبية على غرار ما ارتكبه في قطاع غزة.
إن هذه الأكاذيب لن تغير من حقيقة أن العدو الإسرائيلي هو المعتدي على لبنان وشعبه، ولن يُفلح العدو في زرع الشقاق وبث الفتنة بين اللبنانيين. وإن المقاومة مستمرة بواجب الدفاع عن أرضها وشعبها، وتُلحق بالعدو الخسائر الفادحة، وتُجرّعه مرارة خياراته العدوانية الخاطئة، وثمن تدنيسه لأرض الجنوب وتدميره للمنازل والبيوت.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/naya_foriraq/76913" target="_blank">📅 20:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بسم الله الرحمن الرحيم  اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.  ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/naya_foriraq/76912" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
علّم الإمام الخميني (رضوان الله عليه) الشعب الإيراني ألا يتراجع أمام البلطجة والهيمنة، واليوم، مستلهمًا من هذا النهج، أظهر الشعب الإيراني في معركته مع أمريكا والكيان الصهيوني أن عهد تهديد إيران دون تكلفة قد ولّى، وأن أي عدوان سيُقابل بردٍّ حاسم وقاسٍ ومتناسب.</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/76911" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بسم الله الرحمن الرحيم  اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.  ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/76910" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا وآلية عسكرية تابعة لجيش الإحتلال الإسرائيلي بمسيرة انقضاضية في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/naya_foriraq/76909" target="_blank">📅 19:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTex9_NlVXtDosRhUdOw5pIRHp41clxDz2LkiEEO111oisGKIEojlyWgxv9ihuNXGYxg65lL5asXOckjLh8W_oxjSRPkQq99jIeqYc-G7AMReqf5i6kt3nkhAbc6o2ykFsffgdG6Qn_3eRx9EvSBEypQKWtLsq302JycdYf6MoXmSHVXUTGT4FY3gAJbe2rBCoGj_-8WK11k-Q5w8faRgOI8Real3BRP8Q_bf2J9U_pUkUtZVP1gPl5LpvygGiGdfsajpOJZXfFJuQohPRjyEdMX0mEIGlwZPiLqpv-IsR2vQU7_sHVBIWD5Qd6Qi2YOFHj4cNu9P7jbNrdmz4a7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.
ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ واستقلالَ قرارِه، ومن أبرزِها:
1ـ إنهاءُ التبعيةِ الماليةِ والاقتصاديةِ التي تقيّدُ إرادةَ العراق.
2ـ وقفُ جميعِ أشكالِ التدخلِ الخارجيِّ في القرارِ السياسيِّ العراقي.
3ـ إنهاءُ أيِّ وجودٍ عسكريٍّ أجنبيٍّ على الأراضي العراقيةِ ومعالجةُ جميعِ التهديداتِ التي تمسُّ السيادةَ الوطنية.
4ـ تمكينُ العراقِ من امتلاكِ منظوماتِ دفاعٍ جويٍّ وراداراتٍ حديثةٍ لحمايةِ أجوائِه وسيادتِه.
5ـ تعزيزُ استقلالِ القرارِ الاقتصاديِّ وفتحُ المجالِ أمامَ شراكاتٍ متوازنةٍ تحفظُ المصالحَ الوطنية.
وعليه، فإنّنا في المقاومةِ الإسلاميةِ – سرايا أولياءِ الدم – نؤكدُ أنّنا سنكونُ من أوائلِ المستجيبينَ لأيِّ مشروعٍ وطنيٍّ حقيقيٍّ لحصرِ السلاحِ بيدِ الدولةِ متى ما اقترنَ ذلك بضماناتٍ فعليةٍ تحقّقُ السيادةَ الكاملةَ وتحفظُ استقلالَ العراق.
كما نؤكّدُ تمسّكَنا بالدفاعِ عن العراقِ وشعبِهِ وقرارِه الوطنيِّ، ورفضَنا لأيِّ وصايةٍ أو هيمنةٍ تمسُّ أمنَه أو سيادتَه أو مصالحَه العليا.
العراقُ أولًا
واللهُ وليُّ التوفيقِ
أبو مهدي الجعفري</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/76908" target="_blank">📅 19:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1af8c7a50.mp4?token=Vn_OwYgIA0GOJGIhk5bouejvis52b-dfCtCaUg77xjHExSV-xrL8IwlVCqYOIC3aCknlPSnxpctGN8GIdOM1eCsGqlWEWGLsBkhxmt9vlb-p0WLP03goJ8eq_tzcLvIVdLPpv4ccT9gc3kCmBK7OfcekjsP9O9tcefjITnnCpexfklEf6D5OIuG9vJzanzJaQ8EYr6K8KaSycYEBuUuB6C01Vp8c0nia85LyqNcwKi1NPdPLQcJ1dh5YzR4vbs55ionJx2jYqZbpus3DNIgxnUBrGKb6DIW3TdwBstyqcN6FChoaHPVfGboGtzLUtLxMuIPRon0HYeE3gzQ6UFLKtZDEvBI2vD43N2Bi4nfx-bPbAhakzRFfnzXWygVA5o21KkOFw-T6tG9FGzNEFqlD2WHXXsauvMvzYd6ZddA7jMa4LEH1szF0ad2eBQxUVzEXobl5O8qOzU37r8oPEZG9NLiP4dHaMC0fHC9ECCRlMDY5Vk7-EdZptP2YSuqnfgCjox-BG-HsEdC7Md_VqLBufQl0eVQ_BBcU8QoGZPEyysXq2F726-mzo81kyAEhozAjeCrUnrSRgXUujb2vOLi-nb7wn9OS5-cqqpfEbqRluuW8brQ1qyFJed1gG5rKO2aOhoyT7OBXPeNYx_bq1rlHHWVmwPXqy-xLJy5nYI6ELjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1af8c7a50.mp4?token=Vn_OwYgIA0GOJGIhk5bouejvis52b-dfCtCaUg77xjHExSV-xrL8IwlVCqYOIC3aCknlPSnxpctGN8GIdOM1eCsGqlWEWGLsBkhxmt9vlb-p0WLP03goJ8eq_tzcLvIVdLPpv4ccT9gc3kCmBK7OfcekjsP9O9tcefjITnnCpexfklEf6D5OIuG9vJzanzJaQ8EYr6K8KaSycYEBuUuB6C01Vp8c0nia85LyqNcwKi1NPdPLQcJ1dh5YzR4vbs55ionJx2jYqZbpus3DNIgxnUBrGKb6DIW3TdwBstyqcN6FChoaHPVfGboGtzLUtLxMuIPRon0HYeE3gzQ6UFLKtZDEvBI2vD43N2Bi4nfx-bPbAhakzRFfnzXWygVA5o21KkOFw-T6tG9FGzNEFqlD2WHXXsauvMvzYd6ZddA7jMa4LEH1szF0ad2eBQxUVzEXobl5O8qOzU37r8oPEZG9NLiP4dHaMC0fHC9ECCRlMDY5Vk7-EdZptP2YSuqnfgCjox-BG-HsEdC7Md_VqLBufQl0eVQ_BBcU8QoGZPEyysXq2F726-mzo81kyAEhozAjeCrUnrSRgXUujb2vOLi-nb7wn9OS5-cqqpfEbqRluuW8brQ1qyFJed1gG5rKO2aOhoyT7OBXPeNYx_bq1rlHHWVmwPXqy-xLJy5nYI6ELjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/naya_foriraq/76907" target="_blank">📅 19:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏴‍☠️
رئيس أركان جيش الإحتلال الإسرائيلي:
سلاح البحرية سيؤدي دورا حاسما في أي مواجهة عسكرية جديدة مع إيران.
قوات البحرية تنشط في ساحات قريبة وبعيدة وتشرف على عمليات لن نكشف عنها حاليا.</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/76906" target="_blank">📅 19:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAchq7l5395rCpmXF_Gl51QKzw79i3MIV5cu0L6HbkBBcYC5SMrlsLyLnw22fKbJ_rUoBOxo8486zCFp9QYcXVGoos5065I9vx6SJPBQCLQa4pzoS1U7wBz3inoV7OZglco3-ytfRJnBjU43aD62Ug6YJd2Qs4oqQt-Ul6KiFR2JoFWLt6xqb2MSa-f-vRWh26F3mbuNaPpgUE-AUHQ1w94bhPaNCLGL5hoDr6nLP5xqR04mXYhjuPfq0_h4KsFHkJ-q1hiMgCJSs1KQjASPjhN07SNaiSeTNfPjyDkQXD9jwglN_NiQd4LvoJnFqE0KjZbRlCQ-7DPNnL6c1P3LSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ماركو روبيو: بعض حلفائنا في المنطقة كانوا متعاونين بشكل عدواني للغاية، مثل الإمارات العربية المتحدة.</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/76905" target="_blank">📅 19:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa386b3d31.mp4?token=OSMCiARzQeI9XzBMeINzcRMD_S87fCwEUhO3draSFsmo5YizZwE2rUE0FCCgxA8lRx7jvYMEtOhjorQ0oXHgF88fHb71mDvENFZHAgFGZtPkdlL5hw4AyyskMA-aQlW9AF6a6p3zsauUmc2b3NY-TGiqnjuJv1QjF0H-0t4sdcOTH9wlWv4cGQyBI3xKfCJOipNRKeN7sP7_jkjRZoFlgAw3R1BJa7isl5_4NlPf-0In7RQlNKcFvEiYZ9qgx0-7YnGblCLRDZD1TTz8YnXQUyJI5jwAAO8vp6F9-VCTQ1CyNwto3whXYYmQGGEYlB3w_BbJ122gM9jp1UT7eoNtFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa386b3d31.mp4?token=OSMCiARzQeI9XzBMeINzcRMD_S87fCwEUhO3draSFsmo5YizZwE2rUE0FCCgxA8lRx7jvYMEtOhjorQ0oXHgF88fHb71mDvENFZHAgFGZtPkdlL5hw4AyyskMA-aQlW9AF6a6p3zsauUmc2b3NY-TGiqnjuJv1QjF0H-0t4sdcOTH9wlWv4cGQyBI3xKfCJOipNRKeN7sP7_jkjRZoFlgAw3R1BJa7isl5_4NlPf-0In7RQlNKcFvEiYZ9qgx0-7YnGblCLRDZD1TTz8YnXQUyJI5jwAAO8vp6F9-VCTQ1CyNwto3whXYYmQGGEYlB3w_BbJ122gM9jp1UT7eoNtFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔳
رئيس مجلس الوزراء الكويتي يطلع على حجم الدمار في مطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.  "امبه سنتكوم ليش چذي"</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76904" target="_blank">📅 18:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
‏وزير الخارجية الأمريكي روبيو: إيران ترد على عبور مضيق هرمز بهجمات إقليمية.</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/76903" target="_blank">📅 18:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
روبيو: منصات إطلاق الصواريخ الإيرانية تعرضت لضرر بالغ أدى إلى تدهور قدراتها بشكل كبير.  واضح واضح
😄</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/76902" target="_blank">📅 18:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a404b9b4.mp4?token=R2d9dRN9zHIe0r9iE3-bComMg5gst0WmLL2TIUAMVeA8460LlkQ7rHttIQheUvOSzLJMGbV6fYoukt97L6xrKRXGSdiSb4kx3FtliJWLjGYfuz5oOajyqmOhXHGZtNi3An7aAWp_OnqdGbvyjMCXlGTjNWlIenLR9aEvcE3fuheZX6JivMdgF7VI3yn5ELMopSTC1gDXjBoMFOQbndYm29GQlk7PVhboQMt8qHLUG95cOAAzZ5-y2eHXGLavP5KAwuKvO9-aVPtH3x7mMqcmeP3CZpwz4iZKboX66F8X_cJT8Kra1EKMwYxQMLHc9Jf98TrpWRNvhKvDOoP8ux80pl1HWBiQuC7r9P33TELTISHNjRemN1OyxKSXPYAoveuJH8OOEDwrs-ABAJlPngxIqKMuWBCH6mm-Q1og1cz1YonzObq42N0lQVoeNVknW2qj7EafL2qP9q0hMiaz-pAKVAyog8nfOSh9ujqDGsKTZ6yrIkz0SPERiejXdzXmm1vgSscKlNe3vif43uIlb-Slzn1y8XdiWyM2N-p4c8ecR1zXtDvi-OtrjRrq48O8o6oZsS-xw36vuCjb88tn2fVwwscGdiCp4Ed8fjEBf-NR3DoU9oursY-ggHPl-jDvQ-IOQHGdFBi7NiDzkLj_qsQHPm1Qza3vYZF7beXiM9uqNdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a404b9b4.mp4?token=R2d9dRN9zHIe0r9iE3-bComMg5gst0WmLL2TIUAMVeA8460LlkQ7rHttIQheUvOSzLJMGbV6fYoukt97L6xrKRXGSdiSb4kx3FtliJWLjGYfuz5oOajyqmOhXHGZtNi3An7aAWp_OnqdGbvyjMCXlGTjNWlIenLR9aEvcE3fuheZX6JivMdgF7VI3yn5ELMopSTC1gDXjBoMFOQbndYm29GQlk7PVhboQMt8qHLUG95cOAAzZ5-y2eHXGLavP5KAwuKvO9-aVPtH3x7mMqcmeP3CZpwz4iZKboX66F8X_cJT8Kra1EKMwYxQMLHc9Jf98TrpWRNvhKvDOoP8ux80pl1HWBiQuC7r9P33TELTISHNjRemN1OyxKSXPYAoveuJH8OOEDwrs-ABAJlPngxIqKMuWBCH6mm-Q1og1cz1YonzObq42N0lQVoeNVknW2qj7EafL2qP9q0hMiaz-pAKVAyog8nfOSh9ujqDGsKTZ6yrIkz0SPERiejXdzXmm1vgSscKlNe3vif43uIlb-Slzn1y8XdiWyM2N-p4c8ecR1zXtDvi-OtrjRrq48O8o6oZsS-xw36vuCjb88tn2fVwwscGdiCp4Ed8fjEBf-NR3DoU9oursY-ggHPl-jDvQ-IOQHGdFBi7NiDzkLj_qsQHPm1Qza3vYZF7beXiM9uqNdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
تجمّع لجنود جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/76901" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8quVXy-FQL5pWA7kWkpAgkeZftEoQfHFYUyn2uqe5Gy7f6XjvAmXA3BNmKiAWNgUMpNHyR5qI81rlRGIcX-2lAfLjCrSt6S7WMcitDGhDoWhMKxUog2Cw-byq64V0gjFkYrfbgcHl_ngJeVW-vyJfDRKQNTw_OJKt7wIzkdrlWLg9E2vN3IcI-nltLV_LcQiH6kDhGt6d5dSGWvPoi2FBld5dnUKV7ldTT_0oyvoOH1OdMZh7zU7c9wci3IMjoNDjKhavtEvDOxq_J2N59QHacS3JmyXKeFFu1r3lrkDuK0G2KIIHKg_RflQmT69HyIb_MheZIMI39QeHzOxIyY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
جيش الإحتلال الصهيوني يزعم إحباط محاولة إدخال أسلحة وذخيرة من الأردن الى الأراضي الفلسطينية المحتلة.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/76900" target="_blank">📅 18:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
الدفاع الكويتية : تعاملنا مع ١٣ بالستي و ١٧ مسيرة قادمة من ايران .</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/76899" target="_blank">📅 18:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sa2Yt5RTN3spCRiz0tLNsTG0DRV9q2Ic8auTV6-8XOucAfF9nbwjVtIVSH7pv4ON-wmWg7E1ytH8Yp5XA6_UoH4rr3Lt5AFa_aBKLsiin1j8UJQRURu9z5qK3NyPEnLpcSQF0U6xPHKvnBPHerOsFRXzKsrA2xLZHL27x9-F-8gTHdNhr_Ks9N98cjE5TKSZoncQIuBYVytXpGQrG5IVvLqv-YQrqnY3d73aPc_Pysvlaizoe6Nz-oyLKKK1uUZbayKp_S8IeumerSkkjXQ9zmsY-ZZ7NHcJViiOczus5vOVuUEpNFpZf6LckyaOO2MXvcw62-sv7epySGrk2FLRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpbS7HIGU3QmwoQZt7pDvYWzfoOBHOgxQMwLsmTGt7NYXqJ4AaQpbSGBsc3rMoqMg0g0l4KCq34mojAT9F6RN-ndzlxQIOmKBoNLxWN7AhxpIne_MJjwTQBoGXYgVMJ47xrl5bLEXlw0ULBnarjVaFrf3j4AB2t4MDcwJlVI_64i_-U-gq3nw7h3t6gU9Z9_ajHWw7e3NMZOOJx6eUnT-6l7bOahy22zs0f8xdDu3060kAV5pGG-fAQOlLIG6XaMjVkPoDm-emjVUuprAnHNnpwsVWi2t2MBwIu8eO8aKBVo9gP0RVJF4haSNd7YcDPEddwM_QkVK_m8tp4bsnd4ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🔳
رئيس مجلس الوزراء الكويتي يطلع على حجم الدمار في مطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.
"امبه سنتكوم ليش چذي"</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76897" target="_blank">📅 17:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21001cb12f.mp4?token=lviEqLuOlyu6XdxaL1CHhI_jFR8XgHU52OCVIWEnWSibHr-ufn7PyIQnu3AKeoiwEOgXy4-RIdTJfIJbEDAPuNamkAmkozCerYzgaDcfQPDTJzUIsCKLuaoVdZrPilJOrDbf2xXCuutTpaUEqMKPecc5Dxlh7dTm5tgoHXrEAkPR8lUij7w9KJb3CF9DcD4k4FQ20nqE5Og7C5I3dqls6Nc5r7gL6K9ohszfrvuJAtZdi4ZCvModp73uLalt9y9jKjlAnzMXfUB6v0cXurqK7gC9G0cGA59uCbEIV8aHXVQRx4qFEx9eKfr4pvvB9DN8e9Nwap1SaWkrlv5S3lM744E2m-2Eyu2BOJXoyQnaggxQwRGuOTsCcf2vpkrFxNf_lFaYRJH5fdKyBLcEqDzJXZYVCq67uUxvuSKPKghJc73_5cQo5kauyovX2mvAkNEt4_rHL-ikPUo8-5ZxaclSx5slhfKC12B-kHOKvFhwlmT22CgrKMk_h6obZLuEHrWsITEmSnxFtzXQKZomkvWyrBq39FlxPq3aD-AP-LLlIWZVrHGDCVEebd2z2K1PkecI0tb6_u39hI-mtU_RXwvx3ev5BjZbo909-cRidZrhew0omYd_GkjIjCSlexs0c7Fx2C8LY9dk8drw7_d9ZELw1A5Xq3V4Crmz011EGZOHGrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21001cb12f.mp4?token=lviEqLuOlyu6XdxaL1CHhI_jFR8XgHU52OCVIWEnWSibHr-ufn7PyIQnu3AKeoiwEOgXy4-RIdTJfIJbEDAPuNamkAmkozCerYzgaDcfQPDTJzUIsCKLuaoVdZrPilJOrDbf2xXCuutTpaUEqMKPecc5Dxlh7dTm5tgoHXrEAkPR8lUij7w9KJb3CF9DcD4k4FQ20nqE5Og7C5I3dqls6Nc5r7gL6K9ohszfrvuJAtZdi4ZCvModp73uLalt9y9jKjlAnzMXfUB6v0cXurqK7gC9G0cGA59uCbEIV8aHXVQRx4qFEx9eKfr4pvvB9DN8e9Nwap1SaWkrlv5S3lM744E2m-2Eyu2BOJXoyQnaggxQwRGuOTsCcf2vpkrFxNf_lFaYRJH5fdKyBLcEqDzJXZYVCq67uUxvuSKPKghJc73_5cQo5kauyovX2mvAkNEt4_rHL-ikPUo8-5ZxaclSx5slhfKC12B-kHOKvFhwlmT22CgrKMk_h6obZLuEHrWsITEmSnxFtzXQKZomkvWyrBq39FlxPq3aD-AP-LLlIWZVrHGDCVEebd2z2K1PkecI0tb6_u39hI-mtU_RXwvx3ev5BjZbo909-cRidZrhew0omYd_GkjIjCSlexs0c7Fx2C8LY9dk8drw7_d9ZELw1A5Xq3V4Crmz011EGZOHGrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب لصحيفة نيويورك بوست: قلت لنتنياهو إنه "مجنون بحق".ويؤكد الشتائم في حديثه مع نتنياهو: لم أكن غاضبًا، لم أكن راضيًا، قلت لبيبي إنه يجب أن يوقف ما يحدث في لبنان.</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/76896" target="_blank">📅 17:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
أنا وترامب نتفق على أنه لا ينبغي لإيران أن تحصل على سلاح نووي.
‏إيران لم توافق بعد على إخراج المواد النووية لكن توجد ضغوط متزايدة.
‏نترك الأمر لترمب بشأن التصعيد العسكري.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/76895" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePqvOp-o8dD-PWQL7t3piDK5w_qsSMcdCC_R2YHdSXcTwtymje0QkiW644vtHEXBjJj3fwilX_JQnBZsBGU2miwpAN_ZFcrunFwGuYybdTPdGKGlhZ2lLuqjtbCUgBGkul40OV1_avKI6VcEyhL4IAgOlnaq_IxfWyDgYuoCOtbz6PpiCQWAxRrNRUuo5xsA2_Xl-SBhSFgYxSD1okkOzrOu1_DGR1dlCHH3hwyvLWPlbcKKzJjfUNyChrNbNHUietTrAv6HiI7DrkjC6YHLZYdp4iHoo2i0m2zZ4Wkt4pvE3LUB9Ktd2zycnse6Jljx4-_uTMyEdQjWdfikKl_VTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إندلاع حريق وإرتفاع اعمدة الدخان من المنطقة الصناعية في نتانيا شمال تل أبيب المحتلة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76894" target="_blank">📅 17:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7jNd7nutbAakxdrJwkKeIruaW-E8E30-ZgoYCkbFpurBKjGgBUVcpsoxZ91hDpoFMus0JV7f-R7ifVYty3idECFPg8E2JQG8wglssJkW4yu9Kg2QWxyIKmEDnf8eytbNXHQMimJbJxc4F4ECbVqrlWSGHVhCzb0oW0D2RUDt6HD-jd2Me1nSmcCZLW3O4Lk4VPnJ_mRXBs3ppulxWaUjqUGndGEUpBo7FnP9Vr-xmyD9TvXx_Y_0IJKjiw1-FSRNuXD9SLLDOHz5F0bjD79PmTgsouQmxIWQjctWuuZ7X03cyb3hygERy05mrZ-Hfl_z7kmG_iRt6B6Qs9XperMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
غارة صهيونية تستهدف بلدة زبقين بجنوب لبنان.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76893" target="_blank">📅 17:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 تجمّع لجنود جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76892" target="_blank">📅 17:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔳
وزارة الخارجية الكويتية:
استدعت الكويت القائم بالأعمال الإيراني، وأعلنت دبلوماسيين اثنين غير مرغوب فيهما بسبب "الاعتداءات المستمرة".</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76891" target="_blank">📅 16:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
الجيش البريطاني: ‏
مقتل 3 أشخاص في تحطم مروحية تابعة للبحرية البريطانية جنوب غربي إنجلترا.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76890" target="_blank">📅 16:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRkV2Ka0iy-aunp9gHq7W_14nBy8SO3pO-h_ja5ER4u-yYDmDjFbVRQJEewn5Lstg0tZ3yZOttMzcoPrr1eON_l6N73H34FmZxa-e7N9aKJyxlijPYY8pnWkga8CElWmjSj4FbaHL_XYkdQTboeHix0CDzvB2J1m8FKT2nD5z_Ya6XaqQJavpemMCrSpVuYhC-lln4ErucZvIcP2J-ROAsWZl_hn5qWuJem7k63vPx3m6cKkYsg8lnj1X1nMNcVBY2EKHH8we9EVr3gV6TH3zzK6TPe--jET-5e-1suqqmL6iOUCPQ-fvj78fsNh9uYg6ihPHx7EUhkKUMkDBAwwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الاعلام الكوردي يتداول ترشيح اللاعب الدولي هوار ملا محمد مستشار رياضي لرئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76889" target="_blank">📅 16:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
الانفجار الذي سُمع دويه في جزيرة قشم الإيرانية ناتج عن تفجير ذخائر حربية غير منفجرة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76888" target="_blank">📅 16:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
حزب الله:
تحليق استطلاعي ليلي بالتصوير الحراري لمحلّقة أبابيل الانقضاضيّة فوق قلعة الشقيف التاريخيّة ومحيطها جنوبيّ لبنان</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76887" target="_blank">📅 16:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz3TMNWYPsDDERx1AoVTbIL8bSuaOZEiuZILarWBGPAECk0kC49KZRFHlUuR2CQbFIqCudtYObPK5jOoTQ2PjLJa_XGsY9yCDg0RzOQhQWTC0042go_iDBM48YuViLbHdBjrd3uWZXQzJDAcaO0JfUeRFUWLU0MhtX-CTh2gDUhkULLNgNhkvuqiQLcMrpPdkdbW3CB96JxHDDT3yUawdbC8Pkv3Wj4SVPrgHMuaXm5d_1s6yrx8ExIJKosKeKXvcSkY3w6PRLxzvf2ZqYF2EoeTo4BSzMk-iolYG6rjl934cs3uzAJUDrDxE4lVxA26Hsr1B0p3uLjHFQOIsYe_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
المقاومة الاسلامية
حركة النجباء:
نؤكد أن موقف المقاومة الإسلامية حركة النجباء ثابت ولم ولن يتغير بخصوص السلاح المقدس المنضبط الذي وجد للدفاع عن عراق المقدسات وشعبه.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76886" target="_blank">📅 15:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
رئاسة الوزراء العراقية تقرر تشكيل لجنة مشتركة تتولى وضع الآليات المناسبة لتنفيذ إجراءات فكّ الارتباط بالحشد الشعبي وحصر السلاح بيد الدولة خلال اليومين المقبلين.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76885" target="_blank">📅 15:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تنويه…
🌟
سيصدر بعد قليل بيان المقاومة الاسلامية العراقية حركة النجباء
.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76884" target="_blank">📅 15:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
الدفاع الكويتية
: تعاملنا مع ١٣ بالستي و ١٧ مسيرة قادمة من ايران .</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76883" target="_blank">📅 15:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad5f20ed9.mp4?token=RaFHHTRbAk01Gc_RHLJS3KF-z0OV9WDCgwQYeESe-6_9aBaFmfq2Eryb6jDzKP9BzrPXhibBAJ0kGq4bM06yBMW6pvaTgPFalfr-qZ0825OFlyNCT4eIN_fTl-PwVjA2mzQCYqAnuHYA7Fp8nIH6XD7ZPbZGe8O39G6_n1hLmTPkN1vtAZnCjEYvsCnLH2BgLlTKU-gbFajPaiwhzNgZ_RUAtMP-MBF465wRkjWbA-whbcTnzBu_rNOKm2VMdKLNbbR-vOuCnJnLbLIF4xZsQfTCVYDmm1reAhMqFcl36n0A7nu5wymdrWViYp6K9ooOx3DWCy8chgUBUpqIB444nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad5f20ed9.mp4?token=RaFHHTRbAk01Gc_RHLJS3KF-z0OV9WDCgwQYeESe-6_9aBaFmfq2Eryb6jDzKP9BzrPXhibBAJ0kGq4bM06yBMW6pvaTgPFalfr-qZ0825OFlyNCT4eIN_fTl-PwVjA2mzQCYqAnuHYA7Fp8nIH6XD7ZPbZGe8O39G6_n1hLmTPkN1vtAZnCjEYvsCnLH2BgLlTKU-gbFajPaiwhzNgZ_RUAtMP-MBF465wRkjWbA-whbcTnzBu_rNOKm2VMdKLNbbR-vOuCnJnLbLIF4xZsQfTCVYDmm1reAhMqFcl36n0A7nu5wymdrWViYp6K9ooOx3DWCy8chgUBUpqIB444nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سُمِع دوي انفجار عنيف في قضاء جومان بمحافظة أربيل شمالي العراق، أعقبه تصاعد أعمدة الدخان من موقع الانفجار.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76881" target="_blank">📅 15:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
🇮🇷
المجلس الأعلى الإسلامي العراقي يطالب بتشييع جثمان الإمام الخامنئي (قده) في العراق .</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76880" target="_blank">📅 15:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3070c474.mp4?token=pUTntlF2arvm7bKFGTYSuFQWmdb8EG3EK6BuqhObFxQkdSZG6PhOTC-5AVULyB2p-aD2SXopAH5cAg_DrTJs8767nt0D2zReO41bfFBfhpIXW5-qcvXdc552wDrMo0xJGrDiLd6obkf-zcE9ZMAhE-J4TW9I9xoa6Iqn5H-o7FRz2f96R1PC-tol3c2LZoYZ4F6_ax6_6vv_3Km9kpi2vybzraLrQFfuTMyvLAQqeEW7Moz5s94v6OTYBMdg78-vDBk7Qox6hVcem9t1nMY198KGvEAXDSqT8_6AWgUkgqTecK159bLy-O7DHXQGYdUnNnDgorUHluAz9QdPCQlO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3070c474.mp4?token=pUTntlF2arvm7bKFGTYSuFQWmdb8EG3EK6BuqhObFxQkdSZG6PhOTC-5AVULyB2p-aD2SXopAH5cAg_DrTJs8767nt0D2zReO41bfFBfhpIXW5-qcvXdc552wDrMo0xJGrDiLd6obkf-zcE9ZMAhE-J4TW9I9xoa6Iqn5H-o7FRz2f96R1PC-tol3c2LZoYZ4F6_ax6_6vv_3Km9kpi2vybzraLrQFfuTMyvLAQqeEW7Moz5s94v6OTYBMdg78-vDBk7Qox6hVcem9t1nMY198KGvEAXDSqT8_6AWgUkgqTecK159bLy-O7DHXQGYdUnNnDgorUHluAz9QdPCQlO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
شرطة أربيل في شمال العراق تعتقل شخصاً بعد قيامه بنفخ بوق يُصدر صوتاً مشابهاً لصوت المسيّرات الإيرانية.
كاكا هاي صوت مسيرة من باب شرجي
😆</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76879" target="_blank">📅 14:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76878">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDSKs7tlhM-KjVnGsOIjD_rpkeSEbsv39d5ELj0fYVpKb6i1yGE5DCqDdlY3CbhWgG1SzEteBqJxMqD1qsp_mjEh8izhDl9HlArbdoDCLlqu7igw7TGkGFIL253G7dfN8IvetI8G2shpohUsArNHNOmdWNitffoT6jb_ZNgnSWBjtqj7yHz98ZjNEMohqFitni2fYCSwUHVfF54dtAaDeTTiy9iaDLrqjgEvdkwZLHZ4LSEQrhpHeJ9iFvGDw3CQvg5aN8J60xPas9r-j9IFMd90xlSiyFTIX-FCcGFEH8bKUBp1011Z5V3ny2UrFt38phDfSptz8jRxiY3a-8U7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
الجيش البريطاني يعلن عن مقتل أحد أفراده  في شمال العراق خلال حادث تدريبي (حسب وصفهم).</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76878" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
الصحة الكويتية:
إجراء 7 عمليات جراحية كبرى عاجلة بعد الهجوم الإيراني، واستقبلنا 63 مصابا.
لا لا
يابة سنتكوم تعترضهن كلهن
😫</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76877" target="_blank">📅 14:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
الانفجار الذي سُمع دويه في جزيرة قشم الإيرانية ناتج عن تفجير ذخائر حربية غير منفجرة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76875" target="_blank">📅 14:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1c8f3530.mp4?token=uOwrUvaekUYOcbciq7Ml13FNB1FvEb07rS-j7NFI23ys0ARPV9Gv5DkHtYPkwsMPpC_35Akva6_PD9YDgYnlh9u-QL6QEfrduB8sSiBIcQOpHzUxPz1FfK6x5FWt9szx2XuE_QB7-O92zukfoxI55NCIvsXtAeBw7rAZhXpkhVOGDgV0_XLFpL7pT7X2jyi-zfa-KA96eKUiMUp2VEx6J5b_5Uy7PxPktFV7IA4Eq7dY6OuDVInn7m1l7WMOXx5p22qwoaSuwiqNlC-Bvk7YmTdZU0k3xakXhmYkYPaHveaTo0IBX_7bAyZu6avmQSGR9VFSyju6Q4FHbH_lYWV_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1c8f3530.mp4?token=uOwrUvaekUYOcbciq7Ml13FNB1FvEb07rS-j7NFI23ys0ARPV9Gv5DkHtYPkwsMPpC_35Akva6_PD9YDgYnlh9u-QL6QEfrduB8sSiBIcQOpHzUxPz1FfK6x5FWt9szx2XuE_QB7-O92zukfoxI55NCIvsXtAeBw7rAZhXpkhVOGDgV0_XLFpL7pT7X2jyi-zfa-KA96eKUiMUp2VEx6J5b_5Uy7PxPktFV7IA4Eq7dY6OuDVInn7m1l7WMOXx5p22qwoaSuwiqNlC-Bvk7YmTdZU0k3xakXhmYkYPaHveaTo0IBX_7bAyZu6avmQSGR9VFSyju6Q4FHbH_lYWV_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
ترامب لنتنياهو في مكالمته الهاتفية:أنت مجنون تمامًا. كنت ستكون في السجن لولاي. أنا أنقذك من الكارثة. الجميع يكرهك الآن. الجميع يكره إسرائيل بسبب هذا.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76874" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2702a18eac.mp4?token=AnrTSN5t5fPoEiV6GX9y3T-EOLQJ5E3pRu9FSoAlBYpUnHMRqcdgdNDLTuTc8VHHO54gcsGhYd4Zwc8OiZ-psOkgG6XtlCjhgv-ERjz9-oZ_nHhrVZmCclUvhGh7M8Nl6F5hW000JBbbl99ahtcYvNdLwiOECqM2rGoxptZbDUzRrCn4gUNF-RTrJGSyllJ9HYO0EfBg1ZlMNp-_zbRsS5FqCd1LDhoQ1LZ2GqyNCHzU-Htdkc9I-AhMb0AKcADQFg_AfOHJKBZGznmYd7wkNDlyZNp9fiet95IpKa5qIH9r_MeS2TT9ghnbsNkT4IeEDlhWmefKTFontsIOAGhUAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2702a18eac.mp4?token=AnrTSN5t5fPoEiV6GX9y3T-EOLQJ5E3pRu9FSoAlBYpUnHMRqcdgdNDLTuTc8VHHO54gcsGhYd4Zwc8OiZ-psOkgG6XtlCjhgv-ERjz9-oZ_nHhrVZmCclUvhGh7M8Nl6F5hW000JBbbl99ahtcYvNdLwiOECqM2rGoxptZbDUzRrCn4gUNF-RTrJGSyllJ9HYO0EfBg1ZlMNp-_zbRsS5FqCd1LDhoQ1LZ2GqyNCHzU-Htdkc9I-AhMb0AKcADQFg_AfOHJKBZGznmYd7wkNDlyZNp9fiet95IpKa5qIH9r_MeS2TT9ghnbsNkT4IeEDlhWmefKTFontsIOAGhUAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترمب
: مجتبى خامنئي منخرط بالمفاوضات معنا وقد ألتقيه في وقت ما، وإيران وافقت على عدم امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76873" target="_blank">📅 13:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ie5bUmQTBNrqO7jF163CznR4vi7wv0RRQtAABXh23ZBD2IvpsU5-XNV-Cx6_lRQjgPgMedtqQqx_xFdEU51wRPqf8guKiLLTI3SWSss7aSJL0za2upODStETpgswlepE35X--n5U8v5ZSbhlCALCZPLGVKfodnYMSqRQ3xq7pGk0SQBUf47hEzVbTexgzbIGj4ejaGHfDptRVkcq57S6cFQjOX6ARd-Cp8fl3RAo6DoXFg6HYiZl3uycbtZwx0KvnRRaMk3wP3m8iQxrQvz_TwqqL8A16DqYR_wITT8dz3PRjKaK6cB2zgUCX50H-p_uGi16ZBo6kIKyZh51tt5x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
نفى المكتب الإعلامي للحاج هادي العامري بشكل قاطع الأنباء المتداولة بشأن تشكيل لجنة برئاسته لمتابعة ملف نزع السلاح.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76872" target="_blank">📅 13:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61caaee40f.mp4?token=GUtCBX1LCGxVwm0VkSh8ReVkaUfm4DRbK637K0u4c7u1k1RGtHdw4RjnvM42sHEWjudUbvZzsaxcxP2eneg7pxIh_b6K78TPt6mqgnf7cYVJ3Ft9FTAmiC2knUocrJ2Zyl1lfp24NtY62NWN--W02Ck1Tjnho2QzvLuIm26LuenmG0lJX70fnHc04c5LMaLGxDPRm-QAlibjswQv0ZMHBGQGM2i9TReyx2GXLIXAId-bUF0ME_eoqGUr-9BvrTZMVjuwjxxRtCY5TJHM7u7f9NTq-Hm3tCAQURlohC6IomjAy-8YhPq6b9Og3B5avyakUp-62Sdf08QSqQP-TpZ8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61caaee40f.mp4?token=GUtCBX1LCGxVwm0VkSh8ReVkaUfm4DRbK637K0u4c7u1k1RGtHdw4RjnvM42sHEWjudUbvZzsaxcxP2eneg7pxIh_b6K78TPt6mqgnf7cYVJ3Ft9FTAmiC2knUocrJ2Zyl1lfp24NtY62NWN--W02Ck1Tjnho2QzvLuIm26LuenmG0lJX70fnHc04c5LMaLGxDPRm-QAlibjswQv0ZMHBGQGM2i9TReyx2GXLIXAId-bUF0ME_eoqGUr-9BvrTZMVjuwjxxRtCY5TJHM7u7f9NTq-Hm3tCAQURlohC6IomjAy-8YhPq6b9Og3B5avyakUp-62Sdf08QSqQP-TpZ8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حالة من الهلع بين المستوطنين في كريات شمونة، عقب انقضاض مسيّرة تابعة لحزب الله على مواقع عسكرية قريبة من المنطقة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76871" target="_blank">📅 13:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951231e9f2.mp4?token=HBUacnbFBEVDYudBVqawVhcyVEDrincEcdpTu4cRlQNc1e15voGlkW3PyAO_YxpPrqjgQcFHxUQiohM9Yi9kCmxjeYc3_4dq4UugGf2NObxqM95-Rn7-4MeBo-y8d1BP4iFUcWib4TdDthXl70eu9NdzjVvjKAgvGit6j_RUJbJB5u_nRndDClwMAOuaHevLliJHNLu0-g8d-A3-E6R78Dr6PK63-AZo2I9Lu5f875peDjLG9FQR-2y-1aZg0udzx6wEsE7YNpJvwNLg3Uc3OUdPBpSHQ9OSO9KHfMmI00w7-_kbSpptMg1GVoCB0VKvuEB_XbbF6OUsFdcfaPQEDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951231e9f2.mp4?token=HBUacnbFBEVDYudBVqawVhcyVEDrincEcdpTu4cRlQNc1e15voGlkW3PyAO_YxpPrqjgQcFHxUQiohM9Yi9kCmxjeYc3_4dq4UugGf2NObxqM95-Rn7-4MeBo-y8d1BP4iFUcWib4TdDthXl70eu9NdzjVvjKAgvGit6j_RUJbJB5u_nRndDClwMAOuaHevLliJHNLu0-g8d-A3-E6R78Dr6PK63-AZo2I9Lu5f875peDjLG9FQR-2y-1aZg0udzx6wEsE7YNpJvwNLg3Uc3OUdPBpSHQ9OSO9KHfMmI00w7-_kbSpptMg1GVoCB0VKvuEB_XbbF6OUsFdcfaPQEDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجزت فرق الدفاع المدني من اطفاء الحرائق المندلعة في مطار الكويت بعد امطارهه بعدة مسيرات ايرانية ليلة البارحة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76869" target="_blank">📅 13:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇯🇴
حكومة البندورة الأردنية تعلن تضامنها مع الكويت والبحرين وتدين اعتداءات إيران
😆</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76868" target="_blank">📅 12:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇰🇼
هيئة الطيران المدني بالكويت: استهداف مبنى ركاب بمطار الكويت بمسيرات وصواريخ إيرانية وتفعيل خطة الطوارئ  استهداف مطار الكويت أسفر عن إصابات وأضرار جسيمة في عدد من مرافقه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76867" target="_blank">📅 12:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 24-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصلياتٍ صاروخية وقذائف المدفعية ومسيّراتٍ انقضاضيّة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76866" target="_blank">📅 12:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇰🇼
الخارجية الكويتية: مقتل شخص وإصابة آخرين في استهداف مطار الكويت
‏اعتداء إيران أسفر عن أضرار بالمنشآت الحيوية بما فيها بعثات دبلوماسية</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76864" target="_blank">📅 12:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d40ecfec.mp4?token=WGNvv1-lNZHfVixgz4b-qvvY0gvNGCC_5CJlAlccxtTU-RQwaTQ6ieHPp1GfaBFJia0x6aOmjn6uO0gwi_AwGlobfhtkBO6txU_pQgp50gpUFlN-C8FZnsOxZ0xiqDpBzZYY4vi_EXzUGC9PygiCYy1rn-yv7yaIAusPHdRCN7T7yZHc4Kl4p6gZGqfIyam3JOeE4z7cSN4w14E5-BTEVRvnQ5NKWpAt_mcwsGogtFsXKb0YXmvtdufto9aFGJsA7B6xuKUqXKuoIp8jHs6L5Pz8UN4a1mvOxC2aA7m66b3b-tmHUxa-uqU9PSrccuQ0hH-QOt8xSQNZbmuAH1Ui_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d40ecfec.mp4?token=WGNvv1-lNZHfVixgz4b-qvvY0gvNGCC_5CJlAlccxtTU-RQwaTQ6ieHPp1GfaBFJia0x6aOmjn6uO0gwi_AwGlobfhtkBO6txU_pQgp50gpUFlN-C8FZnsOxZ0xiqDpBzZYY4vi_EXzUGC9PygiCYy1rn-yv7yaIAusPHdRCN7T7yZHc4Kl4p6gZGqfIyam3JOeE4z7cSN4w14E5-BTEVRvnQ5NKWpAt_mcwsGogtFsXKb0YXmvtdufto9aFGJsA7B6xuKUqXKuoIp8jHs6L5Pz8UN4a1mvOxC2aA7m66b3b-tmHUxa-uqU9PSrccuQ0hH-QOt8xSQNZbmuAH1Ui_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتحدث باسم كتائب سيد الشهداء الشيخ كاظم الفرطوسي :
تسليم السلاح من اجل الحصول على وزارة هو خيانة .</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76863" target="_blank">📅 12:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0a748bed.mp4?token=IvIiiOpTTNZ37s7NQMKSe0CA928YSQAosOrjru3LOfPbaOgvlRPyAkoevp8wfzjdD2AOtOYIOh2XJGBGT99KQaiCGPleqENZ3HMbQfoNihz-qY9ExTZFp_2e2IN4CbyUZ3iomwa22PHiWmiFWjOQmZcAWIUaN8uMlSgG6eB3jWXc4BlDZ3lQkTsWy3vKJrpwf0l9VCB8DlsdwY9ABYJYuwSjShJ0_yOgDH7Idyjl-Jrs7BfjPsfVCCr6KniI8kp0ybIxuS3fYx5H2AAI2PaedJhqv8Z5OH7bTwV_KxaL1ic4EIndG3epTO2QDsqXD5cMNq4-OnCA-oZ3yXlyuegpew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0a748bed.mp4?token=IvIiiOpTTNZ37s7NQMKSe0CA928YSQAosOrjru3LOfPbaOgvlRPyAkoevp8wfzjdD2AOtOYIOh2XJGBGT99KQaiCGPleqENZ3HMbQfoNihz-qY9ExTZFp_2e2IN4CbyUZ3iomwa22PHiWmiFWjOQmZcAWIUaN8uMlSgG6eB3jWXc4BlDZ3lQkTsWy3vKJrpwf0l9VCB8DlsdwY9ABYJYuwSjShJ0_yOgDH7Idyjl-Jrs7BfjPsfVCCr6KniI8kp0ybIxuS3fYx5H2AAI2PaedJhqv8Z5OH7bTwV_KxaL1ic4EIndG3epTO2QDsqXD5cMNq4-OnCA-oZ3yXlyuegpew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد من انطلاق المستوطنين إلى الملاجئ بعد وصول مسيرات وصواريخ حزب الله إلى المطلة شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76862" target="_blank">📅 12:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن رئيس الأركان السابق: لقد أرسلوا جنودنا إلى لبنان كقطيع من البط إلى ميدان الرماية
😆</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76861" target="_blank">📅 11:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04a5b1d9b.mp4?token=WkpmxzYmHOv4HMhBCSDzyuCQPUtTSdSlV1aBZGwbsE6LR8xP1DypD4T1LPB9zzqIgvnXSQ53Bh7-YBcooEFrQyHPSfvMJCvcFrl1QGSI6hLJsFmg33ElfmyCfOD3zjX06nm4T6hwV-nTaSW9jAY2qqUBWq91cSh6QI3HgW4luxzi2U5zPFM-8wE3Ger4oRK6z3hOekY9MjbIIhpGc2R49z9TACk1PwezpMaW8uhByDtrtkqzLXBktAr82gZHNkVXVxw3Cce0uar-emKjZ5j9mjsEnsLRYYe28jMfY-xtfoIRCkehPKSC8vHplTcE05iiHFDwN2_jKT9IyusSVsKYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04a5b1d9b.mp4?token=WkpmxzYmHOv4HMhBCSDzyuCQPUtTSdSlV1aBZGwbsE6LR8xP1DypD4T1LPB9zzqIgvnXSQ53Bh7-YBcooEFrQyHPSfvMJCvcFrl1QGSI6hLJsFmg33ElfmyCfOD3zjX06nm4T6hwV-nTaSW9jAY2qqUBWq91cSh6QI3HgW4luxzi2U5zPFM-8wE3Ger4oRK6z3hOekY9MjbIIhpGc2R49z9TACk1PwezpMaW8uhByDtrtkqzLXBktAr82gZHNkVXVxw3Cce0uar-emKjZ5j9mjsEnsLRYYe28jMfY-xtfoIRCkehPKSC8vHplTcE05iiHFDwN2_jKT9IyusSVsKYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
استهداف صهيوني على طريق صيدا بيروت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76860" target="_blank">📅 11:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇰🇼
مشاهد متداولة لمطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76859" target="_blank">📅 11:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2KAR5-bYX6Yj5pQ8HePEar-Q2qACedq6C7PXOwl9_SYbGv1n2rHHQLCO5XAayXP_ZG45EG5HzHXUb0uI50HPGvHfg_LrlscFcsOqEyyKv-kMk2y5FbXWEFmrkb2kbAV_KYAA89PAQxJDRJSW2DQZVXCPaAPdDuMuWMuna0G7mvX9VVAoSD-XdxK68_XJVRT3BEoFqjzGb_QFZBnwW0dSDPaXoM8pYPvqbyjxHq3gIDRbXNkijbk68mF-r6ZyC4uO5oLUNR0T02Y_NJdP6cg8MdHCQ26VfzFWSRr4clLTC3simTBFoUGzNo_wZsa7Nt7IZoyPnROWf885ZD7GtyAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
صورة تظهر الأضرار الكبيرة في مطار الكويت الدولي التي أُبلغ عنها بعد تعرضه لضربة من طائرات مسيرة إيرانية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76858" target="_blank">📅 10:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fu--B_8qOznzV0xwBCSyVkqFnwR3BOWcQOWD6lH8kvUZK-cjs_sSl3uamhNuaW2gjDayTMjx7FisOPoRA8U9ZBTqXpttJHOYJgKEqcbM3aA64d4gIVHPfYMXuUTqkI62u7nQWIl1res1xX0MVpLl2pMQeFKWOL9Y9PeBHrKgKRlt8UvAMMLH7FfpxNtkkZyXF1J4dWuyTUas8khEG9sxkLRZkbgw0VZfGRpeYt7s03ZmsyjlgdUVrq3Bq4KrVdV9fGFdq3L9LF4lgWySP5Sp4czBr--xzE4AQ9ae4HAT_7VIyupqjTMkfMLcKJN7z75JBXt6dto-XYSxLZWJL0rLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdEGF3YnFDHuksbL3mOIo_oI7NSfGAuc-jImAylCAjzHxQjbk9io2h0y-1pGwqu4c_94tlcXaApMDIaPPGJ9-PZKvF0jArNCqkHfttHRrwmDqvDn9K9alTwW1tr-fW5Cm6L4-n3fY6T73dpWtdS3m00JgHcVJUATyy69y-xt4QTEoOLNTT_XS95hfNNlMW_2sKsaZUCqxr4KfcRft-EM5Q3hOUWlJGSw2y8fMb3bHv3bey87ms9yKxusqK_fbn_RdGx5Ap36NwCP8L9Kynwp61bOIm7Svhla9osWXksF4ACv21EvPCHFejLJsSZXjAtQ2kC5XE6O3ifwraCh1BfaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b244cd39.mp4?token=KtLIUs-Fq2rcmp0BcIPIm7gsvRSeroCNNupyzWp4lhjtZzgGEa1SyqC1PeeMlwoA47h_zDHSCFqONackRokSL-PGNJpJW66I5ifmMj5MuX2CncmDy8dlwtkdZ-Keh0n3yXE6ctpRSg5EXWMPxdcVAxS60whyS97wdl5FqWxlobm30cuzqkhsODwZxd88B04vr9RW_N_jzmkKp-mHgs8zpUnVnLsf3_vHCQcCUc4T61wFVpfrU72BQ_Ntaj6y4cbid5f4sRbAV3kQZ9m0yjw3bRbc2877lL5VsjgZHxn4HbXYhUoVb2iC23xMnoyk0bQpyrzoL_sQItG5RehaV3hdRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b244cd39.mp4?token=KtLIUs-Fq2rcmp0BcIPIm7gsvRSeroCNNupyzWp4lhjtZzgGEa1SyqC1PeeMlwoA47h_zDHSCFqONackRokSL-PGNJpJW66I5ifmMj5MuX2CncmDy8dlwtkdZ-Keh0n3yXE6ctpRSg5EXWMPxdcVAxS60whyS97wdl5FqWxlobm30cuzqkhsODwZxd88B04vr9RW_N_jzmkKp-mHgs8zpUnVnLsf3_vHCQcCUc4T61wFVpfrU72BQ_Ntaj6y4cbid5f4sRbAV3kQZ9m0yjw3bRbc2877lL5VsjgZHxn4HbXYhUoVb2iC23xMnoyk0bQpyrzoL_sQItG5RehaV3hdRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
هيئة الطيران المدني بالكويت: استهداف مبنى ركاب بمطار الكويت بمسيرات وصواريخ إيرانية وتفعيل خطة الطوارئ  استهداف مطار الكويت أسفر عن إصابات وأضرار جسيمة في عدد من مرافقه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76855" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇧🇭
قوة دفاع البحرين: استهدفنا ب 3 صواريخ وعدد من المسيرات الإيرانية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/76854" target="_blank">📅 10:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izc04tDLRLLfAvoAtrlEDsS51fe3hvAmCIDSBFDQusfiAfk6Yofvnw_C0nZ73IAm2GpGeF_QO81584ERXQOtrHqeGBxVt-F6iGL0DySyUfUw2_qaVLsOJCWM9MDe4G5-CvURY9muWPfaKoTAeetFkmxjQldP223cJnZLD3xt6_cvel5YDOk8tmZnpWlRju7M27xQvjjzw-lflMk-vbTOfBAxJ6RHLNwvf06_1wrJTddyoubYcx7ArXBn4ccdm3WvTQwUR86Sk9EwuugbCyweVevljRcG8Rl9bnnCqhWnqLy_Xzg1vbT1HgcYaQHwgsko5f4pi7uoNnNd-dtNLpvTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السلطات البحرينية تعتقل عدد من الشخصيات الشيعية في البحرين وذلك رداً على الهجوم الإيراني على المصالح الأمريكية على أراضي البحرين.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76853" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw3_4JNt4vvZMZxV0vZESztk9MG4Pnp0eM0hAnYCtTl6vQZqcKUBau-QxGyL8OhNefcUwR77jtNXnoo29FInHcWGctHmD_fUpIu2Ezgp8koWhuul-ctHlSXQnOhOeHM7nfMhL-bVpRWeqbtz-pN-2qCqW_YeHoN46J9G9VXLxYs_vhDxpwEqDswnVAa1hVmkMcfV30EJyrRTSpqx8RFuAbg7mqQQaE5V0J5UgbuRjob5SjvcK0HQNsG_boVeVZp6Oci_dtnybqoPExfIH_SAWZiMUztWfbupmUI3rRCEE-9X-qrYXQOPPYEHWJ1cnbdqhXyN1296DoW1o1ox-9I7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة أقلعت من تل أبيب تطلق نداء الاستغاثة وبدأت بالهبوط متجهةً نحو Belgrade.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76852" target="_blank">📅 09:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇰🇼
🇦🇪
الكويت والإمارات تغلق مجالها الجوي أمام حركة الطيران.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76851" target="_blank">📅 09:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇰🇼
🇦🇪
الكويت والإمارات تغلق مجالها الجوي أمام حركة الطيران.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76850" target="_blank">📅 08:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5KsrGEb1MIwm8EUCIRVkMW9WPUmWWXoiOnCS09xGXqEv7QNt4gae_ziaXtseSfYboQkrdMgeCus9TsOPyGmF6w5gKpzUu0fNde4JteE6Zg14PW1NmVlvvmrJsM7WpbSJeDWg7Ug2mQUq4DmkU7kOBe4Ja_WIEKwA05LssLBF6dDRjuWx_F_cI_gevJDX--fOSpD1Veot7HLqB3TADvY0W_xvcAU75-184QRt6CstDQorKQEap-kKEHOKpjYOqlWLVC9yqkV9cdA8Dh-aLf1msQVNJHQmVc-skN5Vx1VI891VqyMT7nNjO4sK7UbJTcRftsRRzKple8s4GagbpubHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🏴‍☠️
طائرة التزويد بالوقود الأمريكية أقلعت من تل أبيب وتحلق الآن فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76849" target="_blank">📅 08:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إطلاق صفارات الإنذار في البحرين.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76848" target="_blank">📅 08:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">إطلاق صفارات الإنذار في البحرين.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76847" target="_blank">📅 08:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b904ffec5.mp4?token=GC0OgVMNT2GKtrUR713tA9CQqIdhC4fp22MOGs2fLk66BNp7rHZpWYrd0bLCbSwa3zvMlGTN55IgZBgh9-skdyuh7Y-c3obVPe364xCV2X2mHZgmDPcNDBpr7EpOVnZ3eUaCNYwx50QOBRtvUTaffnp2FPPOX41aAY0xpRhkZ5R-boicK7dc9yfDBQaAO2-ZIkJuqr5nstYsLey7ucHL4SHCyUjZygauIDp0w6vpCQOhXkdKqlejHlo6MTyTBwkjoYvYrUx0WBgF-W-uznzYyPX1T8ejtssuVyIgdfHuQwAUr2Sn52QReCOoqKG8Iv9uc0y-SkOcnpqxeIcTc7wmOw0CPIKqNtcbmNAaFERUQq0s3sz06zWxoF2ciacseNRZcb6iTWnc2LHSNGq9StCwj_KeRCZNKbE_eTYiytViDRZ_U9lkFZSUA6cgHd721CiuLX1-nPVCdMOSlQuijWzvcC8KMi6dEVyWikncMq-238NZ-ipb7qh1v6NFBYVnuXGDa_4p9-Moi3ghkW8qAMSkNec18mkYkrNO2yeEDkCTBLdahL1Nri1NRhsZg1F9JtAa1RX7qE7NdE0I5XWG14hwgC6iXoMI2bSaQDuY-vf2mKrB-qvp_0cSG_Sdzbm-DNxIgwcphuVjkyBEvZVHDzT2i72ZrPDBmQYoaeJTfxwiGWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b904ffec5.mp4?token=GC0OgVMNT2GKtrUR713tA9CQqIdhC4fp22MOGs2fLk66BNp7rHZpWYrd0bLCbSwa3zvMlGTN55IgZBgh9-skdyuh7Y-c3obVPe364xCV2X2mHZgmDPcNDBpr7EpOVnZ3eUaCNYwx50QOBRtvUTaffnp2FPPOX41aAY0xpRhkZ5R-boicK7dc9yfDBQaAO2-ZIkJuqr5nstYsLey7ucHL4SHCyUjZygauIDp0w6vpCQOhXkdKqlejHlo6MTyTBwkjoYvYrUx0WBgF-W-uznzYyPX1T8ejtssuVyIgdfHuQwAUr2Sn52QReCOoqKG8Iv9uc0y-SkOcnpqxeIcTc7wmOw0CPIKqNtcbmNAaFERUQq0s3sz06zWxoF2ciacseNRZcb6iTWnc2LHSNGq9StCwj_KeRCZNKbE_eTYiytViDRZ_U9lkFZSUA6cgHd721CiuLX1-nPVCdMOSlQuijWzvcC8KMi6dEVyWikncMq-238NZ-ipb7qh1v6NFBYVnuXGDa_4p9-Moi3ghkW8qAMSkNec18mkYkrNO2yeEDkCTBLdahL1Nri1NRhsZg1F9JtAa1RX7qE7NdE0I5XWG14hwgC6iXoMI2bSaQDuY-vf2mKrB-qvp_0cSG_Sdzbm-DNxIgwcphuVjkyBEvZVHDzT2i72ZrPDBmQYoaeJTfxwiGWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الإنفجار الذي سمع دويه في العاصمة الإيرانية طهران، ناتج عن انفجار "خزان غاز سيارة" بإحدى محطات الوقود ولايوجد هناك حادث أمني.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/76846" target="_blank">📅 07:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd089958f6.mp4?token=j_oRFWilZzM7jr_mwqqW10VaHEunhIGBTY0B7oYgafpEyNkLkUqIuA8HB_L8DkDlw9OrYrPWdAZuDmIO1G2IsMj_2AkIkUvBJikCUJeX3X8d0oXbxYd3qycr4prPB2qJiZLKVYeRpE1jlgRDJhearnQH7qfLbK2ynAlCCTifCltCJMgYWvI3eilkUmGEQP_0e6ZIAhhENMKMaG4k_t6Fma78pfU03Oqhm3MSHS5Nzeib7-KeCpPa5k1IJRJxn8aKdJzJto2zzRM6Sh8edBIh7FaObhSm-zQ6sfqahGi4AhJGc5ZBk_zkT61jW7YYyv2JP9_GDXW7zpdtSV6eOGf6Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd089958f6.mp4?token=j_oRFWilZzM7jr_mwqqW10VaHEunhIGBTY0B7oYgafpEyNkLkUqIuA8HB_L8DkDlw9OrYrPWdAZuDmIO1G2IsMj_2AkIkUvBJikCUJeX3X8d0oXbxYd3qycr4prPB2qJiZLKVYeRpE1jlgRDJhearnQH7qfLbK2ynAlCCTifCltCJMgYWvI3eilkUmGEQP_0e6ZIAhhENMKMaG4k_t6Fma78pfU03Oqhm3MSHS5Nzeib7-KeCpPa5k1IJRJxn8aKdJzJto2zzRM6Sh8edBIh7FaObhSm-zQ6sfqahGi4AhJGc5ZBk_zkT61jW7YYyv2JP9_GDXW7zpdtSV6eOGf6Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
هجوم أوكراني على مصافي النفط في مدينة سانت بطرسبرغ الروسية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/76845" target="_blank">📅 07:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇯🇵
‏
اليابان
: ميزانية إضافية بقيمة 19 مليار دولار لمواجهة تداعيات حرب إيران.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/76844" target="_blank">📅 06:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf856cab38.mp4?token=ulXfkZZpwLJBYtlNq5sb6yT6NMGCmePmXUJs0AKDxePtIQS9w47unhWZjJOYyK7Qbyr1yBc1ghxIoQP2jKbH00XbULeYbUqDB21wfaEmwr9uyPhul37AEVic6zHn9KILpPmr6bhwWKVNxds6kkmzhq7EZgRPtnWbf7yQDuEBPzowxweuQO03outzTrKVmavVeX9LGZDYGC7CN09xQ-qFukZnYi8Gsnd8O09-zsBwM4EgG5H0Ud8qUMWxfuShcO67P6yoAW-VPVlERZACT4vSpaoGCXEEi6XziYEIFtUbzP6aLnoki0Png16e0_FIPO2AIqSkgtlFg__Oxen7INxpJL5uB2UlKd_Hx4YSuLIYV9g64AAcuF1CkVEVkqJxGrwsgpZFaovFOFp9YfaMX2MzBmaoUz3ICeh6lSGbfbhFydCR7YjX5lCXfaeb0JDmHBy-5wL563-a7G7owSG91cK8wiE89hROnaKHJnaYFJFGcu-L9qxYiP7l3BoZc5d9fh7cz9KZkTUeAGAhne_Y_Iozfn-erqKi4t6V3QIaDG6nw8zyX4vb9-cccfsohtjdPKK5lksLLrPK-UBJBm3HmBP45P7zgzyqdceu_NRTXUl_K93LjLKPiopfGdfak2BXPlwmGrBCypNshppwnhzHuETA7ZjSgjqqRD6P_iCOX0PdlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf856cab38.mp4?token=ulXfkZZpwLJBYtlNq5sb6yT6NMGCmePmXUJs0AKDxePtIQS9w47unhWZjJOYyK7Qbyr1yBc1ghxIoQP2jKbH00XbULeYbUqDB21wfaEmwr9uyPhul37AEVic6zHn9KILpPmr6bhwWKVNxds6kkmzhq7EZgRPtnWbf7yQDuEBPzowxweuQO03outzTrKVmavVeX9LGZDYGC7CN09xQ-qFukZnYi8Gsnd8O09-zsBwM4EgG5H0Ud8qUMWxfuShcO67P6yoAW-VPVlERZACT4vSpaoGCXEEi6XziYEIFtUbzP6aLnoki0Png16e0_FIPO2AIqSkgtlFg__Oxen7INxpJL5uB2UlKd_Hx4YSuLIYV9g64AAcuF1CkVEVkqJxGrwsgpZFaovFOFp9YfaMX2MzBmaoUz3ICeh6lSGbfbhFydCR7YjX5lCXfaeb0JDmHBy-5wL563-a7G7owSG91cK8wiE89hROnaKHJnaYFJFGcu-L9qxYiP7l3BoZc5d9fh7cz9KZkTUeAGAhne_Y_Iozfn-erqKi4t6V3QIaDG6nw8zyX4vb9-cccfsohtjdPKK5lksLLrPK-UBJBm3HmBP45P7zgzyqdceu_NRTXUl_K93LjLKPiopfGdfak2BXPlwmGrBCypNshppwnhzHuETA7ZjSgjqqRD6P_iCOX0PdlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد توثق لحظة إطلاق الصواريخ من قبل الجمهورية الإسلامية الإيرانية باتجاه القواعد الأميركية في دويلات الخليج الفارسي.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/76843" target="_blank">📅 05:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
فشل محاولة ثانية من المسيرات الإيرانية في مهاجمة قواتنا في الكويت.
الدفاعات الجوية التابعة لنا نجحت في إسقاط عدة مسيرات إيرانية ولم نتعرض لأي ضرر.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/76842" target="_blank">📅 05:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66acdfd3d4.mp4?token=k-EGt4sgPrt9Bydl6kIAa1g6PJ34TlUt3rHyTWcWa6WkXh0gTqdr0QNzo5fZfv1uOGgd-sfZmsfQgXMvMAonPiDQD_TcKKl9Gwt06xOBIVJWeA3cq4ZJFE5pezhVBbUui2RG9le3OTEd1bRkOkIS7Kwo25lVm4ffTAjC0hnqPCEVZYc-6epem4D3fjCs5G_ZRhdg5ui03EAyH5XLr2CpSeDsAQnqiQb29t0CcwlZZx9bpnNIMJZlgJa3HzX2fO5yi2SyKAPsCMiBNl31T-ChgZoSBZ61u6mDylFcTOE9nF5VD7pDY-rEk4QLIAPnaQQ-NroNk2MXSPjZnH7CbsC5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66acdfd3d4.mp4?token=k-EGt4sgPrt9Bydl6kIAa1g6PJ34TlUt3rHyTWcWa6WkXh0gTqdr0QNzo5fZfv1uOGgd-sfZmsfQgXMvMAonPiDQD_TcKKl9Gwt06xOBIVJWeA3cq4ZJFE5pezhVBbUui2RG9le3OTEd1bRkOkIS7Kwo25lVm4ffTAjC0hnqPCEVZYc-6epem4D3fjCs5G_ZRhdg5ui03EAyH5XLr2CpSeDsAQnqiQb29t0CcwlZZx9bpnNIMJZlgJa3HzX2fO5yi2SyKAPsCMiBNl31T-ChgZoSBZ61u6mDylFcTOE9nF5VD7pDY-rEk4QLIAPnaQQ-NroNk2MXSPjZnH7CbsC5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای انتحاری در حال حرکت به سمت کویت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/76841" target="_blank">📅 04:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241cbfcc80.mp4?token=iVxYIzhV6Clhq7ky9N9ic7fPcGTqmpvJFLq8nENvQTfrMy4AwrXU1TGK1kLgohj4mxZ-PuHs8_J3B_WJpukRkaoU-OWC-IJOg4YpokyrwRVxoarMMq0eR-8-4Ro33QNyiN5FtHIuRQINopWPIFkgs8q0gNViLvdHaQT2nYg4nYk14Wu_MGhkWMeBko1az_SH5CmXQ6rM3o9f7aHeMQVC9dq9TwLT7Lep-CO_lBHWC3Xuu7OORBs6Kd-Ii-DZ5ybW6Dkz2YFiHHzIbSTxIuOAAyqmavdXk6vdmd5FpO4x_0oZPPi1zDPXYewiHOT8MpttuQ5ZQ9tb0yvqHYQlSdzOiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241cbfcc80.mp4?token=iVxYIzhV6Clhq7ky9N9ic7fPcGTqmpvJFLq8nENvQTfrMy4AwrXU1TGK1kLgohj4mxZ-PuHs8_J3B_WJpukRkaoU-OWC-IJOg4YpokyrwRVxoarMMq0eR-8-4Ro33QNyiN5FtHIuRQINopWPIFkgs8q0gNViLvdHaQT2nYg4nYk14Wu_MGhkWMeBko1az_SH5CmXQ6rM3o9f7aHeMQVC9dq9TwLT7Lep-CO_lBHWC3Xuu7OORBs6Kd-Ii-DZ5ybW6Dkz2YFiHHzIbSTxIuOAAyqmavdXk6vdmd5FpO4x_0oZPPi1zDPXYewiHOT8MpttuQ5ZQ9tb0yvqHYQlSdzOiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏انفجارات تهزّ مقر الأسطول الخامس الأميركي في البحرين، عقب إطلاق رشقات صاروخية إيرانية باتجاهه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/76840" target="_blank">📅 04:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82785218ec.mp4?token=Jqgvu4WBfW3Jdj_WuRFmVY7I4EOgRJGX6prlhozDN_bNDyiqkZmJmrQzGEkUKRtIJ8GuLeErlBj7J7FVpo1rFEfpr_p-KC9XlJamYhbYfvK74tC7hw0nWixTcCVZvqRBpocokfdvVuGUe1ysphRrGWtoTDmx8kDE5bdmUkIm16POD3fliiybDgOSnBWJWl7zLZ0NaCjS5E5RjASGg_wwev7r4epkm-Ge-cBqFaJPILFAk0q5aCK-4cYRmHYQqvVaNp1OeJ3RUl9J_A7gS57c_U-wgQQAYeOoxfQMhqoHKCA_pNhSGvOuB_XOQA5PTPk1BbkOO18qkOJ-CqbSBTrpig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82785218ec.mp4?token=Jqgvu4WBfW3Jdj_WuRFmVY7I4EOgRJGX6prlhozDN_bNDyiqkZmJmrQzGEkUKRtIJ8GuLeErlBj7J7FVpo1rFEfpr_p-KC9XlJamYhbYfvK74tC7hw0nWixTcCVZvqRBpocokfdvVuGUe1ysphRrGWtoTDmx8kDE5bdmUkIm16POD3fliiybDgOSnBWJWl7zLZ0NaCjS5E5RjASGg_wwev7r4epkm-Ge-cBqFaJPILFAk0q5aCK-4cYRmHYQqvVaNp1OeJ3RUl9J_A7gS57c_U-wgQQAYeOoxfQMhqoHKCA_pNhSGvOuB_XOQA5PTPk1BbkOO18qkOJ-CqbSBTrpig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای انتحاری در حال حرکت به سمت کویت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/76839" target="_blank">📅 04:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyOBVCV4r3XleeVeKe9rh68HcFIgseN4i8V5SfjUSYmygTBzZzGIrM_3M2yNSq6sX5FvxyNpRxvGJTbvza4KJsf8Sna6PDce9ovNwr2SPoH8gsEXD5fE-OPbyl9HMg85uCf7O9ZvCU_weIFzNBoNF51rQUrVBFmTuFsU_zzWw_1_vG0Ic8yaOLgd28sZqRoYo7xl7qf4mz_GgKSfyqBLnbj8h9nxJ-QGg4Pg3flQHNVaV3Zv7FsPpFyKoGYyY7L5ZkHANZ-JDKIuIhKy3G7q8_tj034QvlI5Qu-TU47reNBqJ5i0pliTuY4iENlgwZi1w4CkvzxSV92-NwR8uN0c2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 97 دولار للبرميل الواحد بعد الهجمات الإيرانية على قواعد الأمريكان في دويلات الخليج الفارسي.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/76838" target="_blank">📅 03:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">من الطيران الحربي الذي يجوب سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76837" target="_blank">📅 03:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76836">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8563b797f.mp4?token=UG86OfDRlhI0r1F8UTtmiZfodsJUKGZsJqD7baMAR35VvErBVu9exXQtw0RVOIV7U5Xotc82c6MdIjNebdmt-ifzPokz7NgECEELHe4PzvNqvdX0JJMRzvEXhJopmKsPGHd-oIMQBqA5YHymNNqcqx-zX-BN-RupnPHqzjG-buIUcj68k_PDGW5plkrEMsCByZieEnPielxK3yao3brVKBffj0-J3hOaj4_m3z7qzD8Xkwu0l1_7guXD3Ao_WQ14lM3RmV6tL5Rr3TfmH0W1yD34f6R9aAyG4Hz_u8VhNKeh-4NCxztks29gLnQBYF047uCbqapuZL5PYp6lOgPT0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8563b797f.mp4?token=UG86OfDRlhI0r1F8UTtmiZfodsJUKGZsJqD7baMAR35VvErBVu9exXQtw0RVOIV7U5Xotc82c6MdIjNebdmt-ifzPokz7NgECEELHe4PzvNqvdX0JJMRzvEXhJopmKsPGHd-oIMQBqA5YHymNNqcqx-zX-BN-RupnPHqzjG-buIUcj68k_PDGW5plkrEMsCByZieEnPielxK3yao3brVKBffj0-J3hOaj4_m3z7qzD8Xkwu0l1_7guXD3Ao_WQ14lM3RmV6tL5Rr3TfmH0W1yD34f6R9aAyG4Hz_u8VhNKeh-4NCxztks29gLnQBYF047uCbqapuZL5PYp6lOgPT0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي في سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76836" target="_blank">📅 03:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192564c0d1.mp4?token=XJDllwjkR5eszCoAaCiJwkbL-ztsUprPhvCylsZwZJJMGIFmgkF2S8gH7kxGKBnd8xZU0cYC_clpfo-fJon0HgzFJZZdYLTmXOFOCR0OYdcePIl1fqycxtclK13F0zFRLxqKBdTVtnmR8DU30SestWgbLrUGzoHRddFURrDRmURSV2i7PD8MQXvbGiY4evsOGsI3l3g53mnmq76hK_33btNQf8RlwBazbzc9DcEMGRirxLsCusquwddG4mR9Ssuw0Hq5t1J3lTc5GlVV33QIMZAKjbwt8zxvWlJI_vsRUZdXCzBcCrCqGIxIA84HNImPTp-yHBSkZepJAAfomvx9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192564c0d1.mp4?token=XJDllwjkR5eszCoAaCiJwkbL-ztsUprPhvCylsZwZJJMGIFmgkF2S8gH7kxGKBnd8xZU0cYC_clpfo-fJon0HgzFJZZdYLTmXOFOCR0OYdcePIl1fqycxtclK13F0zFRLxqKBdTVtnmR8DU30SestWgbLrUGzoHRddFURrDRmURSV2i7PD8MQXvbGiY4evsOGsI3l3g53mnmq76hK_33btNQf8RlwBazbzc9DcEMGRirxLsCusquwddG4mR9Ssuw0Hq5t1J3lTc5GlVV33QIMZAKjbwt8zxvWlJI_vsRUZdXCzBcCrCqGIxIA84HNImPTp-yHBSkZepJAAfomvx9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ باتريوت أمريكي يفشل في اعتراض الصواريخ الإيرانية ويعود ليستهدف دويلة الكويت!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/76835" target="_blank">📅 03:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ecc2e200.mp4?token=giUBd6zIvlKVFxGF7TeG7epCiLtQoaYzCaVz0eE16YhPrDMjjTcn22wkUuL1QjoAf2aotwUIIor3Zuw5LhIs2xlHaP623cpcGADO3fhN0pG0mSiPD3e38GU1-K2dtYItw_WTV4bGijOthgajQxDk8Jl4Khgx2tn5sWVtelurp-X9ebykR335TH6GdN3o0UUrSbDYB5vPdBlu4Jqw0VsO0gFnLjcdI045BFo3PA789pwAvZw3aN0XXvm4DqpT67eaydXoByAK5mlfQYsu3QALwoxpzhP0KqJGufy4h6WBkIEUH4AVURWEqYPrB33YgEchCrDo6jPlP6RLltA54tBU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ecc2e200.mp4?token=giUBd6zIvlKVFxGF7TeG7epCiLtQoaYzCaVz0eE16YhPrDMjjTcn22wkUuL1QjoAf2aotwUIIor3Zuw5LhIs2xlHaP623cpcGADO3fhN0pG0mSiPD3e38GU1-K2dtYItw_WTV4bGijOthgajQxDk8Jl4Khgx2tn5sWVtelurp-X9ebykR335TH6GdN3o0UUrSbDYB5vPdBlu4Jqw0VsO0gFnLjcdI045BFo3PA789pwAvZw3aN0XXvm4DqpT67eaydXoByAK5mlfQYsu3QALwoxpzhP0KqJGufy4h6WBkIEUH4AVURWEqYPrB33YgEchCrDo6jPlP6RLltA54tBU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الهجوم الذي طال دويلة الكويت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76833" target="_blank">📅 03:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سماع دوي انفجار قوي في مدينة قامشلي السورية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/76832" target="_blank">📅 03:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">طيران حربي في سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76831" target="_blank">📅 03:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">يبدو ان قطر والسعودية قد تعهدت لايران بعدم استخدام أراضيها بالهجمات على الجمهورية وهذا ما يفسر عدم استهدافهم بالجولة الأخيرة ..</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/76830" target="_blank">📅 03:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fedd33a5.mp4?token=ZpTLDKQEWdhZDskzLkyBBXBgrCqE0NtduOxIg6u49KOrMSWP-FkIEJJMqV-krnBvUz3L6G5f6lYXmcsZ6g41c_lw0sz5K1EFfaQaS3FniJ_xy7qi2dLJTEjvdcspgB_E7kg8ySCugGx-Avjw9eJ3A0lbo-hCi4Rh4_AHH3EdVPrwRUaJ_fA8WQ4QvZ4uHR_7GQMs2uvw2QmOIUOXKFXcNBIEiJ8aCV_tUgzZilmen6rxszihFocBKvHZ5F9peWc96zZqcDUplEdxnMmwNTpKTQfcirFVT3uN0zTFK7GJTX1g7uH3wjK_xtJbl_YQNfbGQFL6xBO-I4S-i2YwLcbrYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fedd33a5.mp4?token=ZpTLDKQEWdhZDskzLkyBBXBgrCqE0NtduOxIg6u49KOrMSWP-FkIEJJMqV-krnBvUz3L6G5f6lYXmcsZ6g41c_lw0sz5K1EFfaQaS3FniJ_xy7qi2dLJTEjvdcspgB_E7kg8ySCugGx-Avjw9eJ3A0lbo-hCi4Rh4_AHH3EdVPrwRUaJ_fA8WQ4QvZ4uHR_7GQMs2uvw2QmOIUOXKFXcNBIEiJ8aCV_tUgzZilmen6rxszihFocBKvHZ5F9peWc96zZqcDUplEdxnMmwNTpKTQfcirFVT3uN0zTFK7GJTX1g7uH3wjK_xtJbl_YQNfbGQFL6xBO-I4S-i2YwLcbrYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق لإطلاق الصواريخ من إيران نحو دويلات الخليج الفارسي</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/76829" target="_blank">📅 03:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkpyOvDcAj0bjAxKjAmAEt-8XfJwA1oZ1gVZIxKGD6NmzpFRo-gN7R0UODxD0VxI2pZYCpmNpeIRM4j3aihH9S3Xv3LuyaYdutUwsHEkeYPTgVuAxSmLPgGALlEgZB3M9CxVqU_vNfPFdYNI8xsgq_NzHwfTbF0Z9g7KIhjK5Vv_t_Kh45jAhhVrw8JcNakOUzEgzRmsb5zgbBkmu5t408gsbj6IbUEXyvO4pupqm6ym1iELjmF4mM6zFHelzsg--4xG5Vz4k3uCCAwJdT2d5xKz_lsoss1vP37rqDANE5zj-7xe9zxYfljzPA_xZg2DIdFBX7xP6tj44dQ2UEcfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها   بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/76828" target="_blank">📅 03:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/540734d971.mp4?token=AHy5JoTDBjKF0H-zUI4PmyRhL27caqeLo2R9e2BlYghj24adtqXF3FPrkVV7JewaXmNPo4j2V-VQZ597gnW46068yF1tmyXvxHsyeRymYySh79H7vNKwI48eD_4_fIHIMlT9MseTuOp0YYMt3YbgE-sfGkKdRAkMtkEkR8b7xXaNeOVkqmk5USPs1UD2IiXc-2N_8uePPd8aRppNdVikm3t0IjC70PO6BXDrHuNEhFDiLxdEScb2lHnjIPLp73bXPCKaTpiYHG0emHtwZL6eAQH764qVF-5kHreQR4srRuE7HH_MWD1fx-CGag2pbOS8abAC213tAP3_JqsGqZ4C9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/540734d971.mp4?token=AHy5JoTDBjKF0H-zUI4PmyRhL27caqeLo2R9e2BlYghj24adtqXF3FPrkVV7JewaXmNPo4j2V-VQZ597gnW46068yF1tmyXvxHsyeRymYySh79H7vNKwI48eD_4_fIHIMlT9MseTuOp0YYMt3YbgE-sfGkKdRAkMtkEkR8b7xXaNeOVkqmk5USPs1UD2IiXc-2N_8uePPd8aRppNdVikm3t0IjC70PO6BXDrHuNEhFDiLxdEScb2lHnjIPLp73bXPCKaTpiYHG0emHtwZL6eAQH764qVF-5kHreQR4srRuE7HH_MWD1fx-CGag2pbOS8abAC213tAP3_JqsGqZ4C9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عجلة في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/76826" target="_blank">📅 03:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
🇮🇷
بيان العلاقات العامة للحرس الثوري الإيراني:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
في وقت متأخر من الليلة الماضية، استهدف الجيش الأمريكي المعتدي ناقلة نفط إيرانية قرب مضيق هرمز بقذيفة جوية، مما أدى إلى إلحاق أضرار بغرفة المحركات.
ردًا على هذا العدوان وانتهاك لوائح مضيق هرمز، استهدفت صواريخ تابعة للحرس الثوري الإيراني سفينة تابعة للعدو الصهيوني الأمريكي، وهي سفينة "بانايا".
في عدوان متجدد، استهدف العدو الأمريكي برج اتصالات تابعًا للحرس الثوري الإيراني جنوب جزيرة قشم بقذائفه الجوية. وردًا على هذا العدوان، تعرضت قاعدته الجوية ومروحياته المتمركزة في إحدى دول المنطقة، بالإضافة إلى مقر قيادة الأسطول الخامس الأمريكي، لهجوم بصواريخ وطائرات مسيرة تابعة للقوات الجوية للحرس الثوري الإيراني.
لقد حذرنا سابقًا من أنه في حال وقوع عدوان، سيكون الرد مختلفًا وأشدّ، وقد تصرفنا وفقًا لذلك. كان ينبغي أن تكون هذه الردود درسًا لنا.
نؤكد مجددًا أن زعزعة أمن مضيق هرمز ستُكلّف الجيش الأمريكي المعتدي ثمنًا باهظًا.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76825" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7f9af40f.mp4?token=cNFNTR75yJfd0TkW6VhyV4NtVwKoLTuWxcJb07YxHNC7yKCQ7Lu0EzG7RKGbHbp-vCpDnt2iSTJgUHKKxSAv1JOjgzQAnIetkJbB3_4ZOdKx5joRpChoV9EhNn1WbqqynyVz5bwJeJ2oIYn3dEWTS-0tElt00GHplDeIk76R2cQc6OxUehGxJ4ayiwWFYfpR7NmU04dopijk6-UP2Iu0I46EeSjpyj7H0zF1O8lJ8PNseOC_dpUAd9621_Hm9V2ILnQBGj6qgy2IEDzgxSHnJ7Mxbj6UEMpk3ilAug8vrxbOppHeFwOxk4V9IAp-4BsM5IDuALYPFEEoaaX9nTNBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7f9af40f.mp4?token=cNFNTR75yJfd0TkW6VhyV4NtVwKoLTuWxcJb07YxHNC7yKCQ7Lu0EzG7RKGbHbp-vCpDnt2iSTJgUHKKxSAv1JOjgzQAnIetkJbB3_4ZOdKx5joRpChoV9EhNn1WbqqynyVz5bwJeJ2oIYn3dEWTS-0tElt00GHplDeIk76R2cQc6OxUehGxJ4ayiwWFYfpR7NmU04dopijk6-UP2Iu0I46EeSjpyj7H0zF1O8lJ8PNseOC_dpUAd9621_Hm9V2ILnQBGj6qgy2IEDzgxSHnJ7Mxbj6UEMpk3ilAug8vrxbOppHeFwOxk4V9IAp-4BsM5IDuALYPFEEoaaX9nTNBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الهجوم الذي طال دويلة الكويت</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/76824" target="_blank">📅 03:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
‏انفجارات تهزّ مقر الأسطول الخامس الأميركي في البحرين، عقب إطلاق رشقات صاروخية إيرانية باتجاهه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/76823" target="_blank">📅 03:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">القيادة المركزية الامريكية:
نجحت القوات الأمريكية في إسقاط عدة صواريخ باليستية وطائرات مسيرة إيرانية، ونفذت ضربات دفاعية على جزيرة قشم ردًا على محاولات إيران شن هجمات في أنحاء الشرق الأوسط.
أطلقت إيران عدة صواريخ باليستية باتجاه دول مجاورة، إلا أنها لم تصب أهدافها. وسقط صاروخان إيرانيان أُطلقا على الكويت قبل وصولهما إلى وجهتهما أو تحطما أثناء تحليقهما، بينما اعترضت قوات الدفاع الجوي الأمريكية والبحرينية على الفور ثلاثة صواريخ أُطلقت على البحرين.
وقبل ذلك بلحظات، أسقطت قوات القيادة المركزية الأمريكية (سنتكوم) ثلاث طائرات مسيرة هجومية أحادية الاتجاه أطلقتها إيران باتجاه بحارة مدنيين كانوا يعبرون المياه الإقليمية بشكل قانوني. كما نفذت القوات الأمريكية ضربات دفاعية على محطة تحكم أرضية عسكرية إيرانية في جزيرة قشم.
ولم يُصب أي من أفراد القوات الأمريكية بأذى. وتبقى قوات سنتكوم متأهبة وجاهزة للدفاع ضد أي عدوان إيراني غير مبرر خلال فترة وقف إطلاق النار الحالية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/76822" target="_blank">📅 03:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4ap6kmODTLCYolfMXZReEjKlJtuKl_2qPpPBjKoHnZYSYNGpwpv0cDOsLLaXeZANn8MEDkCrjAZJ4cZNsMhU38fMwtb9ZdjKNP9dsbSS86_rcBN3mHNVTtxDpNGx6t3V8dpZkBlLp14B1drC3510siX9-6sffAITZxeQ7UsSyRg8g1se54Ou-5Y3GLQIlRbSUSOSOF3c5_ERm1dgWMmB1TexlaEtfdqcUqacXlU3_ozzBrVQjVYoFMkSyTACtkaqnVN5r_8DmtzMziTdM8PCX17jYdPBTALFbps1KUqoA9lsPBpq6NiAi6fhXQGXF9mHJwrm6Z7j0BYsBQ_BZ0QVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إغلاق المجال الجوي كليا في الكويت</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/76821" target="_blank">📅 02:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76820" target="_blank">📅 02:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/76819" target="_blank">📅 02:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76818">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">توقف صافرات الإنذار في البحرين
رفع التحذير من هجوم صاروخي</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/76818" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76817">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم الايرانية</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76817" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd6NSPq8v8Bp9gVKgOOi5FcCldhzhtfWmbPWqaVYuMqGQAGTgXhj1_xW-HuCg0wFsIB7nDGIG_HJnwfSJURKiFP7lXeyNgabiv8jLdwR-60hrvD023cPrnkz55n89tCKYJPfkCgV2gqAnwAjOnxaTOFkLeLoC-9SRgmMH2OxCvsegXupimL-seg1jINZmari15D9bs6ZjXdGaNpLxOfLmzwlUjhHWLAPWsF2e4eC2Jd7K8AP-27uLzSkD490eznQdzYOw70o_5_WupQSIOh2MmqQ07fU57C5FKjf_K7xibED3pg1viptOXfa3osXvs0CVwo0rwvaQLPwSPHAaiHkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تم إغلاق المجال الجوي للبحرين بالكامل أمام جميع حركة الطيران من الساعة 03:30 بالتوقيت العالمي المنسق حتى الساعة 16:00 بالتوقيت العالمي المنسق، مع السماح فقط بمغادرات محدودة معتمدة مسبقًا.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/76816" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76815" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osyb60m6VqS3jibRbCDsMiQ9zIMwF21M6dP9CkYTOJ7RNsnJhzzU3iDOvre34W1HvJLOrqbkhyq6_TgeXWuHLZ7aI5HzabDSrO49_nYQPXIfu4s-gyfjFaN2IUtWEJXrwsZmBlwX-tfsYAkjJ918FGiBo19X3iuw59_MzP9u3XILa7Hfiyps9CECij36cOs0XL3FgkUdYOzslVuctt45FyKo086qaKhvjtSEpsq48RTbd9-RSD4t7nJPc7LNIO6IT6N-ymj1k1QntCzqCOIVUKFeLbG2wA0aBRNdsUER9dL8EpBiBhBcYzyfMGJGFx0EhhZz29JW8bv4XL4RJGYPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصف نحو مطار دبي</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/76814" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قصف نحو مطار دبي</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/76813" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/76812" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الإعلام الأمريكي : أفادت التقارير أن رجلاً يدّعي حمله قنبلة مربوطة بصدره قد احتجز رهينة واحدة على الأقل داخل فرع بنك تشيس في بيكرسفيلد، كاليفورنيا .</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76811" target="_blank">📅 02:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APs7MZFWNMQyroIKJwDUT5PCX5rdJquq4fYvRw0LMr9Ei3qA4eDVcToJ2jCcPJTIbNoAoVmCNC7PvmkTDuOj6awrsnBJ6vNgOvA8_nDiBTtManLUHzInjIHRxjsv-kCF2FP6J_SDu2hjpfJyefJk7ZAkgZGAiDJGYmv_h5wluIwvEUvusX5BDlms5kAOpsFc0Rt77ayiJot0azedZgcZhEtiWYNhvAoEGvhWABFXqR_sKaHqmV8nbMUUyZlW5pr2jKLDBMhfupjfm-ei9wxE8F_GFElZJ2FDwukrCEouYXC6XH0BPdXFa6_zGIqsmRdX4hJqe7GDTnLaIsRvmXRS2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران في سماء البحرين</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/76810" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defe9d3c1f.mp4?token=neQTruuOub1bXBoA5m5XQolpspICgBQI9szqNEQS_QISlwQjL0HPFDGh_3hRsPdDLFjb8h83T45gxVLcwWo60YEoOmEujF85VLCwh9I3z8avral-6O1vQ_F4aIThLIQantYgaxaKhyOhzXERkJnHQj9nEbE_zbW03cwGJ3JPyCHplWgTDBPfYTcGBfFyFqX3eTQzxUMt2h3itPPRaiFVW3fBc-2GFtEmALk-V84OGy4x-L-db52DWqMWmhWEi895aEqHRQfO-MeYURCGe26ObHkpX0_6Qu2e6JY3j0YrGM5XiDfdCPSAW4xjmclmHjmHEK4t9DbErYZJLJIES4jtDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defe9d3c1f.mp4?token=neQTruuOub1bXBoA5m5XQolpspICgBQI9szqNEQS_QISlwQjL0HPFDGh_3hRsPdDLFjb8h83T45gxVLcwWo60YEoOmEujF85VLCwh9I3z8avral-6O1vQ_F4aIThLIQantYgaxaKhyOhzXERkJnHQj9nEbE_zbW03cwGJ3JPyCHplWgTDBPfYTcGBfFyFqX3eTQzxUMt2h3itPPRaiFVW3fBc-2GFtEmALk-V84OGy4x-L-db52DWqMWmhWEi895aEqHRQfO-MeYURCGe26ObHkpX0_6Qu2e6JY3j0YrGM5XiDfdCPSAW4xjmclmHjmHEK4t9DbErYZJLJIES4jtDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صواريخ جديدة من إيران نحو دويلات الخليج الفارسي</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76809" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4d84fc6b.mp4?token=RwHbFaqiRDUTMdNsErvI6WQqZhVeI3sA-voYeZ3LJtgi5-gmTj6DQvVTzy3Ozytyo0lZDkQ_O377_2kMnWwLgNcT7656XJtmXi2JnxspQIsbYFdgmqR3IixOEpPaxB3UPhRIPPBJ86FplcJW4nNkyzobf3wLfi3mkq_myIYbYYqz2xEDTsjQUymwKKH7hFyO-RO96HbUn1RsNAo3_-xaomRsYQZ7PTdvS9odnqRoYROFgoGk4FInVSK37a0sBqhH012ITlQwuuzCrJK3CwrXOZUQQQFLc1e9whoS1RZNHANyoN4BlzTitIcow6wKLjruKSUNqsgSxqIwxnaPvg4XPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4d84fc6b.mp4?token=RwHbFaqiRDUTMdNsErvI6WQqZhVeI3sA-voYeZ3LJtgi5-gmTj6DQvVTzy3Ozytyo0lZDkQ_O377_2kMnWwLgNcT7656XJtmXi2JnxspQIsbYFdgmqR3IixOEpPaxB3UPhRIPPBJ86FplcJW4nNkyzobf3wLfi3mkq_myIYbYYqz2xEDTsjQUymwKKH7hFyO-RO96HbUn1RsNAo3_-xaomRsYQZ7PTdvS9odnqRoYROFgoGk4FInVSK37a0sBqhH012ITlQwuuzCrJK3CwrXOZUQQQFLc1e9whoS1RZNHANyoN4BlzTitIcow6wKLjruKSUNqsgSxqIwxnaPvg4XPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القواعد الامريكية في الكويت تدك بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76808" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
