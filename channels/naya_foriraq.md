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
<img src="https://cdn4.telesco.pe/file/rSAJnzovQOWwBShyF_UUYH62ory1JlnyCpjX8AqOQNdCc3WMwrllLHmckeRrfcDo7_VxDrGcMZtisT66MFJ_L9_jF_xjJ8iS80Ao_3qf8EKWg54PnE7CfqyWp1SS0cEt2Q4Wj2yuitpZ62l4CQkwy89sFyBnhlpJlmdNkKlZUmdWQ5C4j0jJc8EfjTfDcxydLTYD1XfaSoZofMcfo9UQ9YcIDzY4x0UnHpnOZageSsxIMqc87_SMlnT0Kqyv2z4c1k86M51VyPEHsy19LN1XpsrAQFS4xs634jdvhakKDxTZURDCw3G_HMC48yFIuFu9kNKeH_0molNrE4vZmenJ0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
<hr>

<div class="tg-post" id="msg-80416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA0jxAXYUq256kMYJhujUaJG-QqB23uEzlfHE25eGr4MI_zDsDG7oadftAjH1jykf1myp_gig46gTPDbs7iLSdbh_do9TICrwObJrZrjkZGM71ce4crZWPnt-khkKb2cO8-l5UwUwXZktao1CaI_GLKsJgZg0ph1ARkxVaLXxxb1hMelCSrLfu6_Asn42g1iEhDACF3LaGP6Ir9en6M6bT0ZnK9bAaJRLrD0mu__G8qUmKiTsYTKHiIfyRby5NDLO2JHaZz1CwnMvUDf4yO3vZQYWJK6qfWvQqlmA_hZJgN_LQOgFkgNV9SdljzQa1iUGVUNnKt4CjkAIe2BzQQxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/80416" target="_blank">📅 20:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭐️
المنظمة البحرية الدولية:
تم إبلاغنا أن الممرات التي قدمناها ليست آمنة.
علقنا إخراج السفن العالقة في مضيق هرمز بعد الهجوم على ناقلة نفط.
ننتظر موقفا إيرانيا بعد الهجوم للسماح لنا بإخراج السفن من هرمز.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/naya_foriraq/80415" target="_blank">📅 20:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
اجتماع الغد الذي سنشارك فيه في الدوحة سيركز على موضوع الإفراج عن أموالنا المجمدة وإيقاف الحرب في لبنان.
البند 13 واضح بأن بدء مفاوضات الاتفاق النهائي رهن بتنفيذ بنود أهمها وقف الحرب على لبنان.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/naya_foriraq/80414" target="_blank">📅 20:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
🇮🇷
اللجنة العليا المعنية بتنظيم مراسم تشييع جثمان الشهيد القائد السيد الخامنئي في العراق:
تؤكد اللجنة العليا المعنية بتنظيم مراسم تشييع جثمان الشهيد القائد السيد الخامنئي، رضوان الله تعالى عليه، أن جميع المواقع والمنصات والوكالات التي تدّعي تمثيل اللجنة المكلفة بالمراسم هي جهات غير رسمية، وما يصدر عنها لا يتعدى كونه توقعات أو اجتهادات أو معلومات مسرّبة غير معتمدة.
وتوضح أن الجهة الوحيدة المكلفة بهذا الملف هي هذه اللجنة، وأن الناطق الرسمي المخوّل بالتصريح بشأن هذه المناسبة هو الفريق سعد معن حصرا.
وسيصدر بيان تفصيلي عن توقيتات ومراسيم واماكن التشيع (في النجف الأشرف وكربلاء المقدسة) من اللجنة الإعلامية المشكلة رسميا برئاسته.
اللجنة العليا لمراسم تشيع جثمان الشهيد القائد السيد الخامئني رضوان الله عليه
٣٠ حزيران ٢٠٢٦</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/naya_foriraq/80413" target="_blank">📅 19:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a935b97b50.mp4?token=KBCiFy3MPli4ciWD7cUxmbUhbzAMIZRQNMeRlyALVYn-O8cgXSxpsQY8jqTBBLbgEQlaAqv83aCALbaMPY8d8c_lhsVmIyzMVyHF-SiMRPNtLae7vmwZOQ5sbpbcQXk46KeyRZVGf1JfVtcOdKWnbrcAUaXK64igT7nsu-o2ngWy4qQ549JIRI7iaFN_hQLi9Oaoi0MUw0uNCnFelVy8pUazOoQjYrrc1qo9UrTDAykmJt_k-CzqXm-U7bzyXGAygR0KR7YppH-S7bwzuGGsqbuxvZo9FODRQZpCSmGXjVSSe2MeYTRi_U8H1ayur-osveqvchmH-_FoMNcAHHsqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a935b97b50.mp4?token=KBCiFy3MPli4ciWD7cUxmbUhbzAMIZRQNMeRlyALVYn-O8cgXSxpsQY8jqTBBLbgEQlaAqv83aCALbaMPY8d8c_lhsVmIyzMVyHF-SiMRPNtLae7vmwZOQ5sbpbcQXk46KeyRZVGf1JfVtcOdKWnbrcAUaXK64igT7nsu-o2ngWy4qQ549JIRI7iaFN_hQLi9Oaoi0MUw0uNCnFelVy8pUazOoQjYrrc1qo9UrTDAykmJt_k-CzqXm-U7bzyXGAygR0KR7YppH-S7bwzuGGsqbuxvZo9FODRQZpCSmGXjVSSe2MeYTRi_U8H1ayur-osveqvchmH-_FoMNcAHHsqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
استمرار عملية تجهيز مصلى طهران لإستقبال الجثمان الطاهر لقائد الثورة الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/80410" target="_blank">📅 19:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80409">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قوة امنية تطوق منزل معاون مدير عام مصافي الجنوب في منطقة الجمعيات بمحافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/80409" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭐️
‏رئيس البرلمان العراقي "هيبت الحلبوسي": لن ندخل في توترات مع محيطنا العربي من أجل إيران.  ‏أكدنا في السعودية أن العراق جزء لا يتجزأ من العمق العربي.</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/80408" target="_blank">📅 18:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKi-2TsS-hI-H1C0Qb3FblflH-kPKLDDjVZSdnIIKaBNIFX8w9Gn2ooGbihMqGywqrtsKInJrWtjO3xrIb4Aci1QIq7WXl5sJVuC4yjU_20pGCHXIVO_xEBhGVypl7eQmrlGqM2QegskOdZj8xpI-Dd-adFad997OCET0fe4ApexX5rxPVxYUei9mY9DeTT9lp2AIwI8ADhSHeJS1BzYRdXrxv_SW5ZKiaTW67kPD4pMW3fCU0N7QFgJ2G2MFAuqcLi6p_-K5wGV4_cYGFQFoEVEK-1jD4tltB2IwGTfFxqVIwaHBSjlmjh8k39PFCVAwjuUC3JolgOP-eXCRf4VmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
«انتصار كبير: المحكمة العليا الأمريكية أصدرت حكمًا ضد مشاركة الرجال في الرياضات النسائية. يا للعجب! هذا ينهي هذا الوضع السخيف تمامًا!»</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80407" target="_blank">📅 18:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
‏
رئيس البرلمان العراقي "هيبت الحلبوسي":
لن ندخل في توترات مع محيطنا العربي من أجل إيران.
‏أكدنا في السعودية أن العراق جزء لا يتجزأ من العمق العربي.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80406" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
إعلام العدو:
"ألقت الشرطة وجهاز الأمن العام الإسرائيلي (الشاباك) القبض على مواطن أمريكي للاشتباه في تجسسه لصالح إيران".</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80405" target="_blank">📅 17:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">من عملية تجهيز مكان وضع الجثمان الطاهر لقائد الثورة الشهيد السيد علي الحسيني الخامنئي في مصلى طهران.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/80404" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80403">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭐️
نيويورك تايمز:
بعد الحرب الأمريكية الإيرانية، اقترحت عُمان نظامًا جديدًا تدفع بموجبه السفن التي تستخدم مضيق هرمز رسوم خدمة، حيث تدير إيران وعُمان هذا الترتيب.
تقول عُمان إن الدفعات ستكون طوعية وستساعد في تمويل خدمات الملاحة والأمن والبيئة، بينما أشارت إيران إلى أن الرسوم يجب أن تكون إلزامية.
تعارض الولايات المتحدة أي رسوم على المرور، مشيرة إلى أن المضيق يجب أن يظل حرًا كما كان قبل النزاع.
أصبح الاقتراح قضية رئيسية في محادثات السلام الجارية بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80403" target="_blank">📅 17:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho0Tmjl1euPVn3PMWWtww5-DRzStetcfx1s0iYpUzhuVRO_C2Kee8Dosg2hjt5auLhYxVA2JupiDAbycyEXocwXTS8WYnz3sePEIARV7x9IzrZQuK-fjOK41BM91bn3-O0UqXYAI4LS90YPGJQ2FyTlF7rX9uTMCqRuvMl1eS5ptmIrn39ODrlf1MJkqTlhICldFvY4vVW_ASW_kEgyrwW6e20rQwXl4GyCL3k83zVbzH7qbnF4DhKLbt6xuIgzKU0tXhwImcAwkKVfNRA5ZtL2v4Q97H81TzRR2qfvcLaY45dXrGu0Eoa1J7T0u0tORMCFlYAaAfCn5j4ifLnJjeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
نتنياهو ووزير الحرب كاتس زارا اليوم "الحزام الأمني" في جنوب لبنان بعد توقيع اتفاقية التفاهمات.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80402" target="_blank">📅 17:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80401">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2JX93LpGC-fMiw_JC5rXxNVusevxvpIxf5Nji94ZGRzTgd1y9X3VHFazwxvRd9Yn0BmtAhxv93uuz27npAFU5rYRNw83zNxMLZeah6vZ-nfApYY6smP5vuEkojwcT8hSIgBFhhDXSL34JDQZj7sbILtZsNPNPtZE6RVmrveG0HI-NtfWsUTQVUSrt7hEqaGb8sCgy2vRXned0DAYXg_WL052udllJyk7uCQeG69wBKhuT5_z11iisjGonYIIAuCy5k114d8QPeH09ij7P1no1ezqvzYlxVaRpIciwoNg6cjoWMgzLh_RCN76oqTo3L_2AI4E2SXPnO2OrhCl_YJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة امنية تطوق منزل معاون مدير عام مصافي الجنوب في منطقة الجمعيات بمحافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80401" target="_blank">📅 17:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80400">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjHFSxJJhZ9fgDXzUUg50VIHmPBfWjCkeA2WHtsGKeQRM63w7e3ta4DKOxW7f_bGakltECGe_dXLlrWn4ucCGvaFc30EO24AkK5CcGEW52B-0J7IsVedN2yfvEXpXpim9I0WTYt-3dqyEMZgLcinVGNlBTzmFSiqh_Z24aNcgMu0OEMyMt7PBl63aSS5r01n4pzBSMmT4X6LkNIvskFUTJDGd9lu6DvKkhpZJQS_m78niCsrYK2yuJ-2at3xmjuI9dHXudOFCo3TmFisqEW0dw0qdQgD4gUkvPi4_XOSR310coYOrdAPI2Um5mex_A2sp8ud-7j3Z1RyCp24ShJ7fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة من بغداد تداهم مديرية بلدية محافظة الديوانية وتعتقل مسؤولين بارزين فيها</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80400" target="_blank">📅 17:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80399">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزارة التعليم العالي العراقية توافق على منح خمس درجات لمعالجة حالات طلبة المراحل الدراسية المنتهية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80399" target="_blank">📅 17:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80398">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc24e9d2ba.mp4?token=rvHDcWZrOmrr3ARMKhevKG5_C74xCumYA-uT95Q4gptawPUd7MKYtkvywSVwmOt8_dcN6K2KbSH-NUT2Xc4wThavvMiy0AMSQaOfQSvdY8_kYjnEF6ij7K9SLzaQzSPJCA9tJgJHkkyTkdF6OL5PMmsnmns0uEdmYHqlPxrkj8mCbRrz2p0gAYtjkZqmePNko1Fz0tVuV-wAd1oV8wN2UPQeUF_sxbEQMvL3lkbFr5aK7TrIgyKT5Og8jtFSnddLiFkNpU7Gf6dKzxQTWdoY6LmDueCuYi32634fk8r_Bl09LgvCF3xFa7sgwo4LWnN7DYhFnPScX2Oc8rbkH0hmkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc24e9d2ba.mp4?token=rvHDcWZrOmrr3ARMKhevKG5_C74xCumYA-uT95Q4gptawPUd7MKYtkvywSVwmOt8_dcN6K2KbSH-NUT2Xc4wThavvMiy0AMSQaOfQSvdY8_kYjnEF6ij7K9SLzaQzSPJCA9tJgJHkkyTkdF6OL5PMmsnmns0uEdmYHqlPxrkj8mCbRrz2p0gAYtjkZqmePNko1Fz0tVuV-wAd1oV8wN2UPQeUF_sxbEQMvL3lkbFr5aK7TrIgyKT5Og8jtFSnddLiFkNpU7Gf6dKzxQTWdoY6LmDueCuYi32634fk8r_Bl09LgvCF3xFa7sgwo4LWnN7DYhFnPScX2Oc8rbkH0hmkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية في محافظة البصرة جنوبي العراق تلقي القبض على (مرتضى زوير) برفقة أربعة من أبنائه على خلفية تهم تتعلق بالتزوير وتم ضبط بحوزته على 30 ختم يُستخدم في عمليات التزوير إضافة إلى كميات من الاموال</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80398" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80397">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جيش العدو الصهيوني: تم إرسال طائرتين مقاتلتين تابعتين لسلاح الجو قبل قليل باتجاه طائرة مدنية في البحر الأبيض المتوسط ​​بعد ورود بلاغ عن فقدان الاتصال بها.</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/80397" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80396">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اعلام العدو: عقب الحادث، لم يُسمح لطاقم الطائرة بالهبوط في إسرائيل، ومن المحتمل أن يعودوا أدراجهم ويهبطوا في بلغاريا.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/80396" target="_blank">📅 16:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80395">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اعلام العدو: طائرة كانت في طريقها إلى إسرائيل في الجو ضغط الطيار على زر الاختطاف ثم ألغاه، الطائرة غيرت مسارها من وارسو إلى قبرص وتم ارسال طائرات مقاتلة</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/80395" target="_blank">📅 16:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80394">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اعلام العدو: انباء عن اختطاف طائرة</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80394" target="_blank">📅 16:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80393">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اعلام العدو:
انباء عن اختطاف طائرة</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/80393" target="_blank">📅 16:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80392">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73908e4ec3.mp4?token=QidtqWHiAbb7nomb3GIGnU-NpDvr2lynmK1Au1Nr4tP9BSkwn_xBkcUeg3KIrljGB8dFIU45nb73GYMAk5FhAB8HTlcM9r-SIR3sTG-bZu0LsaOZ7FYEQ2Bv-NkJaKxBnCLYZlWNzOTzgW-6kLSbCijUPZj8BbHvltihuWj4Pc4W35xNrvK6g1PeVnwcWws7s8zTUFkFpKpt2n8_And5bWt0ZpFV2Fn7tpznmDhr7BkgHiMtYDkYituvrLhYTy3RxXAHCE1Z2YXpuIzqIF2hrXvC87Y0GHr4-tOUoTwBgEH0KkVufDw5O_xHjImyUc-w84lnORnGl06bwMib2Y5V_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73908e4ec3.mp4?token=QidtqWHiAbb7nomb3GIGnU-NpDvr2lynmK1Au1Nr4tP9BSkwn_xBkcUeg3KIrljGB8dFIU45nb73GYMAk5FhAB8HTlcM9r-SIR3sTG-bZu0LsaOZ7FYEQ2Bv-NkJaKxBnCLYZlWNzOTzgW-6kLSbCijUPZj8BbHvltihuWj4Pc4W35xNrvK6g1PeVnwcWws7s8zTUFkFpKpt2n8_And5bWt0ZpFV2Fn7tpznmDhr7BkgHiMtYDkYituvrLhYTy3RxXAHCE1Z2YXpuIzqIF2hrXvC87Y0GHr4-tOUoTwBgEH0KkVufDw5O_xHjImyUc-w84lnORnGl06bwMib2Y5V_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من عمليات هدم بيوت الشيعة وتهجيرهم التي قامت بها عصابات الجولاني في قرية المزرعة بريف حمص السورية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80392" target="_blank">📅 16:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80391">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
عرّاب تهريب المخدرات يقع في قبضة مفارز مديرية شؤون المخدرات، وبحوزته 32 كغم من مادة الكبتاغون قرب منفذ عرعر الحدودي ضمن محافظة الأنبار، كان يحاول تهريبها إلى إحدى دول الجوار.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80391" target="_blank">📅 16:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80390">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">متداول  الافراج عن النائب السابق محمد الصيهود السوداني لأسباب صحية بعد ان تم اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80390" target="_blank">📅 16:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80389">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
هيئة المنافذ الحدودية العراقية:
إلزام الشركة العامة لموانئ العراق بعدم السماح بمرور أي شخص غير مخول، ومحاسبة المتواجدين في البوابات في حال حدوث أي خرق أمني أو حالات سرقة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80389" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80388">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
وزارة التعليم العالي العراقية توجه بالإيقاف الفوري لتسلم جميع الطلبات المتعلقة باستحداث الجامعات والكليات الأهلية فضلا عن إيقاف طلبات فتح الأقسام العلمية الجديدة فيها اعتباراً من اليوم الثلاثاء.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80388" target="_blank">📅 16:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80387">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
مديرية المرور العامة العراقية:
منع سير المركبات الكبيرة على الطريق السريع (محمد القاسم) ابتداءً من مطلع وزارة المالية ولغاية منحدر قرطبة/ الباب الشرقي ذهابا وإيابا، وذلك بسبب الأضرار التي لحقت بالطريق نتيجة الحريق الذي اندلع صباح هذا اليوم في منطقة النهضة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80387" target="_blank">📅 15:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80386">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CujHDQ5en5AJsZ1eFTnpGN_4zpm-K4UIpI-VnaV_DiXxcH629CR8bEmy1GVTXFrh9MDiOI4YFkJcBKPxGUtPUIoeziFuuE9SJLgN3RoSOggLuG3rqhZyLyE17E1LoWE4iT-0Gpdii964eRQQp6bxwjRnjhOuwRtkSWSAgcLmrkIDBNPYSMa8r_Tu4fNbAPhXk98Lf-ctBXrrveOTVWDS-xXhC8PQOb6lJlUaKSIQoes30I_hDm7tU8P1ZUCvY4ECHiUoHjH83nwFtc-L6XmTXsB_v2ZOyPJw4dr9YAeGza08mLeid5YYjdUHBBY9qLWVNqPP4zY3J4HkYInjAMde0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متداول
الافراج عن النائب السابق محمد الصيهود السوداني لأسباب صحية بعد ان تم اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80386" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80385">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
قوة أمنية عراقية تلقي القبض على زوج أحد أعضاء مجلس محافظة الديوانية بتهمة التلاعب والتزوير بوثائق.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80385" target="_blank">📅 15:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80384">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
الخارجية الايرانية لغروسي: توقف عن إصدار البيانات السياسية وركز على أداء واجباتك المهنية كرئيس لهيئة الرقابة النووية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80384" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80383">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfa-gUtOFczu7XI_2VFxnH54qRFHl35RrMA4UPX9PhQClxwmSxPmtDGyfPgR9Hfy4_q1n6Dhv50KCNwagA1LIZofXJCEe7LIylY1itT4K7jKNEf6Vlj20_UtM-Z5bKRvoFbLo233rL-jwN1wlxY77Xj7H8z4ut5Ogy111cB2J0oYppciRs-r_GOutXO3ixw54mUQWJF9xViC56dref7cN5FhJHiIc9eFvM41GNIJK1EpicwXfRUiG33BkoBQJcvAfoA6iE2YsXQ1tnxPcWp4GHfY74MXoy3oWIGc2v1XQKrR5u2E9KuJlD1aUHzWaTteU2Yyd4DHbEIqhbywrdFj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الاستخبارات العسكرية العراقية تعتقل تاجر  للمخدرات بحوزته 4 كيلو من حبة الكبتاجون في محافظة الأنبار ما يعادل 23 الف حبة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80383" target="_blank">📅 15:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80382">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
الخارجية الايرانية لغروسي:
توقف عن إصدار البيانات السياسية وركز على أداء واجباتك المهنية كرئيس لهيئة الرقابة النووية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80382" target="_blank">📅 15:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مصدر:
رفع الحصانة عن ثلاثة نواب عراقيين جدد تمهيدا لاعتقالهم.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80381" target="_blank">📅 14:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80379">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1wLEBgnkSBqtV8rCW6NtR1ZsEs5N8vc7xQXR1SkBfLFNeaeioS74xzTA9CQ5ejUsT_t_SFogOBAfXpAmRWaEjHfazsElqwPEnzEx_4Z_c8gcMQce8GGb_5HuTz3lJ69Do7D1Ntk4kGsG4NLoRLrimd7xO9oPf1OkbxhJ2WENwqsYC-rGM0QG7O4JsmMh2qLtvhuVRG6VtaAPcQ-ZYke8zPCUX2w3c0xwYWw84dNBb0zCpbVnH8qxE4VcaFhf5SJNkHC2S2aURdqU_FCPxiyrlwnZD2hYp9Wdfcu9YgZYnP5G9fZrAhOXSiikkrP2rFSeGL3KHzQHATBJWbra-5CHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6om5deynzRSpZhEBGyZS7H4ha_oR68Wd7_YmeLQ3ekC0dJSDdtixwBOng9X35klcf9-ue9c7d9tSZaKly41C-oTbCrgQ9_v0WdeTq3c-4O1_U5QyqMRWDYeEJoou-vtbM-nKamDK-D2Avzxn_qJSebD3l5F5f5rz_x7lYd9uiw5jbpOob2Dc2Jp4ivMxdGzOdDVHjy9oX1oLqyu8maZMLxsPEgvJsIR4z8vPiHMM-pgICFyfM9fUIRg5cylarOdo5WSqOHvvKgdoid5Jb3BIcLnW8TjGvEHMKRbe7irz14aaROpZ5L5bMk3gr27Y7koI13Vp0Yip9O324S8X1pQgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
متداول: القوات الأمنية تضبط 11 قارورة مملوءة بالأموال كانت مخبأة داخل منزل يعود لوكيل وزارة النفط الموقوف (عدنان الجميلي) في حي القضاة بمدينة تكريت مركز محافظة صلاح الدين شمالي العراق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80379" target="_blank">📅 14:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80378">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
دخول قوة أمنية كبيرة لمدينة النرجس السكنية في محافظة البصرة جنوبي العراق وإغلاق البوابة الرئيسية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80378" target="_blank">📅 14:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محكمة الكرخ تُصدر حكمًا بحق النائبة عالية نصيف جاسم
أصدرت محكمة الكرخ المختصة حكمًا مدنيًا بإلزام النائبة عالية نصيف جاسم بدفع تعويض مالي إلى المشاور القانوني في وزارة الداخلية حسين يوسف التميمي على خلفية ما انتهت إليه المحكمة من ثبوت المسؤولية المدنية عن الأضرار الناجمة عن العبارات التي صدرت بحق المدعي عبر وسائل الإعلام والتي رأت المحكمة أنها ألحقت ضررًا بسمعته ومكانته الوظيفية ومركزه الاجتماعي بسبب تنفيذه واجب اصولي وفقاً لقرار قضائي بإلقاء القبض على ابن شقيقها بالجرم المشهود .
ويأتي هذا الحكم عقب صدور حكم جزائي في ذات الوقائع والذي منح المدعي الحق في المطالبة بالتعويض المدني عن الأضرار المادية والمعنوية التي لحقت به نتيجة تلك الأفعال .
ويؤكد هذا القرار أن القضاء العراقي يمثل الضمانة الدستورية لتوفير الحماية القانونية للمكلفين بخدمة عامة أثناء تأدية واجباتهم الرسمية وترسيخ مبدأ عدم الإفلات من المسؤولية عن أي إساءة أو تجاوز يقع بسبب تنفيذ القانون أو تطبيق القرارات القضائية .</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80377" target="_blank">📅 14:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80376">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏الخارجية القطرية: لا لقاء مجدولا بين ويتكوف وكوشنر والإيرانيين في الدوحة اليوم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80376" target="_blank">📅 14:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80374">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzzTm2rop7OmgZDhaDtxaAAcR0HF2bE-09N7aDRh0yCRTbOumYtIKBfT178CSPq5rsb41J8pRsO1Vf17eFh_YVZeYmIxv1I1xpDE3_yHa6-aYoHEtwNESsaAp28ERDttu9sn2jSYNLhlc_QzGVDnrR8aeqw1TDkwygzgnoXx-rgsV1jTR_sOQlkHGj76iPnANmovtpP_AJpoU_D2KXRHJRVzAXROeluy1WW5RS78NGvxow19-foaqeZRsjSqY9JKpU5EJLoJEKtiQ4m8fPhtcrmS51OVCRDsoOKOjqnLn5X8LwV2HvuGjBlUxauk_nCxIg_mllqvUGpQvouljxLTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZP9HtRjutQ9oMPyiaMEA-CkHm9eddeETNsy71bm81ArmQ7a6x5sYi3fbT7bdcU98SYXPUNw6svsmSWb5AFcBCJwhXMQir2EfVtFX757oizUH1eaXUCEkbSKIoJosj2kyTtz-Zz2Vrc2zZDqqC28FOe0QfhbU36gwhQRb8z8w-cDjlz2J7kGjF-Z5oKoVdXe8q5oIicZRvRmaO8J3aPVMiFhqY7M5ATcFTF84qdE9WM1P9UsdI-GctRUYJmL1RkRim1-qTl0xTVmN9MVciyrRL2lqhsY4wmmaUUi-r1pCuUgRnz0kRWfvM1JtyExSCiexCYL8C_gg0bFLzHdzjhOdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
دخول قوة أمنية كبيرة لمدينة النرجس السكنية في محافظة البصرة جنوبي العراق وإغلاق البوابة الرئيسية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80374" target="_blank">📅 13:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80373">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
متداول:
القوات الأمنية تضبط 11 قارورة مملوءة بالأموال كانت مخبأة داخل منزل يعود لوكيل وزارة النفط الموقوف (عدنان الجميلي) في حي القضاة بمدينة تكريت مركز محافظة صلاح الدين شمالي العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80373" target="_blank">📅 13:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80372">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5XBu-Bcp2aCY_Gn2Q3xVa2Xgoqkk52fXwSam8_7D__LUpsVBS_vK2780hybOA1_50YYdbUxyZ7e22g4rc2zS9Ih8PYudUm0UL3lNxUo3Lwn71jXcCYI7y9lp9S5AwtJMQaGLPPuJR-a20gsm13iu1BcyD7JdH1torGFem7QduEIBvWtaE8MkzQp7b0N8JRNpKX0cxkjwpyrEnY_2r5HgHg7PA8Tp8N4uKH9X0RDLOnZplZq1bdxRgVK-FKcF3d5B3qF3FFCLw170PoYjvKtPsUYoJ-21XJaUpqa8yAyM1POlbQ-HEtq_76Xw3Rcd1-e3Acr7XL5ifs3-U3LuCE4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوات من جهاز مكافحة الارهاب العراقي تقتحم منزل في مجمع زيتون بمحافظة اربيل وتعتقل صاحب المنزل الذي يعتقد انه مسؤول حكومي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80372" target="_blank">📅 13:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80371">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
القضاء العراقي يصدر
احكاماً بالسجن لمدة عشر سنوات بحق ثلاثة مدانين يعملون في ديوان محافظة ديالى اقدموا على اختلاس
مبالغ مالية مخصصة لتعويضات الشهداء والجرحى من خلال تنظيم 301 صك وهمي وتحويل الأموال من حساب التعويضات إلى حساب السلف التشغيلية الخاص بديوان المحافظة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80371" target="_blank">📅 12:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80370">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24675f9dc6.mp4?token=L_KqvVQBLLnNX9sIEz9ArmMmfzGTM_5hLZQc89uLms67gh1RRYzltI7WOSoi7wcBNLJFP1G5p9970lce6Bt9hpw8hKRQtA_JfTOl4ExPu57na3pGFIBlfJoD_HYH4EERL6nwrXrbIEEY6KuEncpaCx443Ww7kPl_fvQbQ_438N4xGTAEiH1LHaEPYsNo_G3pgZZz9EiqraN6WQP5BsrAdjks7yKDmzwgOOwupIW8woE5PTPR1YBF7P7-2p4zvLYmG2rHCCw8DXuwelPdGMDbk9sc77fRXWBnRu2UZyBIwIwSg2eU9AX5vg5TscCg0heZ-q-n94YKn5o1dP7bC_0x-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24675f9dc6.mp4?token=L_KqvVQBLLnNX9sIEz9ArmMmfzGTM_5hLZQc89uLms67gh1RRYzltI7WOSoi7wcBNLJFP1G5p9970lce6Bt9hpw8hKRQtA_JfTOl4ExPu57na3pGFIBlfJoD_HYH4EERL6nwrXrbIEEY6KuEncpaCx443Ww7kPl_fvQbQ_438N4xGTAEiH1LHaEPYsNo_G3pgZZz9EiqraN6WQP5BsrAdjks7yKDmzwgOOwupIW8woE5PTPR1YBF7P7-2p4zvLYmG2rHCCw8DXuwelPdGMDbk9sc77fRXWBnRu2UZyBIwIwSg2eU9AX5vg5TscCg0heZ-q-n94YKn5o1dP7bC_0x-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عصابات الجولاني تعتقل عدد كبير من النساء الشيعيات في قرية المزرعة بريف حمص بسبب قيامهن بتصوير عمليات الهدم التي طالت القرية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80370" target="_blank">📅 12:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80369">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في بافيه مقاطعة كرمانشاه الايرانية،شهيدين كحصيلة اولية من الحرس الثوري.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80369" target="_blank">📅 12:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80368">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
مراسم تشييع جثمان الشهيد السيد علي الخامنئي في العراق:
▫️
يصل الجثمان الطاهر للسيد الخامنئي وعائلته عصر يوم الثلاثاء المقبل الموافق 7 تموز، قادمةً من مدينة قم المقدسة إلى مطار بغداد الدولي
▫️
في مساء اليوم ذاته {الثلاثاء} يتجه الجثمان إلى مدينة الكاظمية…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80368" target="_blank">📅 11:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80367">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f940aab8e8.mp4?token=fyB1x6jhgiC8tNDZ02-kuWCNCyw786UqT_jRzXrjffnzfNPIoBgy-qJSTd-Nqi3xHKp1IV4Z3caP8czvf68N8kdtYfyL6B3FJBLFPNO7ysRe_uEcu3AKU6l74pRSnoxHnQODhOxjgZNpY8jNcn7BErCrHittn0T1RirvPmmWZvPZ9HtG6BwEOH936rpL5VIfK_KQzAlnqeS1V76DFfB-U-sykULOzPOol3tccTzGfz445pBD2vvYjA-NtDsx3dqLIAjrMoVKh4g13Dt8gnxgbZ5ZjcRzHRfIypgJBYNT-BFemVxl5pQaSCMkuwNLQXkfVlp_HNuEtRwuUiMJBod_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f940aab8e8.mp4?token=fyB1x6jhgiC8tNDZ02-kuWCNCyw786UqT_jRzXrjffnzfNPIoBgy-qJSTd-Nqi3xHKp1IV4Z3caP8czvf68N8kdtYfyL6B3FJBLFPNO7ysRe_uEcu3AKU6l74pRSnoxHnQODhOxjgZNpY8jNcn7BErCrHittn0T1RirvPmmWZvPZ9HtG6BwEOH936rpL5VIfK_KQzAlnqeS1V76DFfB-U-sykULOzPOol3tccTzGfz445pBD2vvYjA-NtDsx3dqLIAjrMoVKh4g13Dt8gnxgbZ5ZjcRzHRfIypgJBYNT-BFemVxl5pQaSCMkuwNLQXkfVlp_HNuEtRwuUiMJBod_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مراسم تشييع جثمان الشهيد السيد علي الخامنئي في العراق:
▫️
يصل الجثمان الطاهر للسيد الخامنئي وعائلته عصر يوم الثلاثاء المقبل الموافق 7 تموز، قادمةً من مدينة قم المقدسة إلى مطار بغداد الدولي
▫️
في مساء اليوم ذاته {الثلاثاء} يتجه الجثمان إلى مدينة الكاظمية المقدسة حيث تُقام مراسم التشييع الشعبي
▫️
في صباح يوم الأربعاء الموافق 8 تموز تبدأ مراسم التشييع الشعبي في كربلاء المقدسة
▫️
بعد عصر الأربعاء يتجه إلى النجف الأشرف حيث تُقام أولًا مراسم التشييع العلمائي في صحن السيدة فاطمة الزهراء (عليها السلام) تليها مراسم التشييع الشعبي انطلاقًا من الصحن المطهر وصولًا إلى ساحة الشهيدين الصدرين
▫️
بعد إنتهاء مراسم التشييع في النجف ينتقل الجثمان من مطار النجف إلى مشهد المقدّسة حيث يقام التشييع الأخير والدفن قرب ضريح الإمام الرضا {ع} يوم الخميس 9 تموز.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80367" target="_blank">📅 11:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80366">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d338d557b.mp4?token=GPXuC2QkJQu8_vwz1HgbGOLJFSqB4kH0wRI9VGtfrrmBTXJG1oEggSoL82dj7xdAZF1u2V072h883nmVtsad6QQh2PongSU6-ZffkKc5oof--n3P_4l7BVqM4TEqJnQD3G5O3g84qf3cKToYOkuPdxYH2EU8-tMr6CKUJDSx8RUfw4godWzuTySn2js68KP7lN8t92zWaKI-u65DYYOIwmYIkSkE7VbMoUrNwwXAycJqSofwZvgzKMHSei_WHb7LwP1JdnDJKicbEkwDlwipO-5yRpuaCqw4TknH-fFyHHKWuruGkflBsLVboEK1vBPNh1dKXLuYqfyp_8DxDaI7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d338d557b.mp4?token=GPXuC2QkJQu8_vwz1HgbGOLJFSqB4kH0wRI9VGtfrrmBTXJG1oEggSoL82dj7xdAZF1u2V072h883nmVtsad6QQh2PongSU6-ZffkKc5oof--n3P_4l7BVqM4TEqJnQD3G5O3g84qf3cKToYOkuPdxYH2EU8-tMr6CKUJDSx8RUfw4godWzuTySn2js68KP7lN8t92zWaKI-u65DYYOIwmYIkSkE7VbMoUrNwwXAycJqSofwZvgzKMHSei_WHb7LwP1JdnDJKicbEkwDlwipO-5yRpuaCqw4TknH-fFyHHKWuruGkflBsLVboEK1vBPNh1dKXLuYqfyp_8DxDaI7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اسرائيل تدبك في الجنوب السوري وعصابات الجولاني تهدم بيوت الشيعة وسط سوريا.. لليوم الثاني على التوالي تشهد قرية المزرعة الشيعية في مدينة حمص عمليات هدم واسعة لمنازل الطائفة الشيعية بهدف التهجير القسري وإخراجهم من بلدهم.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80366" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a6b70b88.mp4?token=j82Z2VB5smTbYCSbez7WIpzKsspn8V9kREaWFCpbqYbKzlIifOgmQeOBwh46WotXnEtkVBREUw2cKeITdGi93rVKxC5ELeQcIiPHYHHEUZZH3wnhDbhOZXFYFx2-Fa9ht6RbwCYYcpC50Ao9CrNecBdd1irqJUviJA3Yb_nb5DUg7lXrGCjvM0IqkOvO5Grtainyob5bLDV2RHNmHxcfWrxj6z0bkqBJ0c0Kx_qC4EvRZVwWsI1iYlIzFS-zTxnS-ddyVomaEpSORIZCSSe_bJj3KFlo6QbhFtR1CuL7aqXpfP3G5oRt7Tyvq5TGIDnilE3mZwg2smWxkMDo3hnYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a6b70b88.mp4?token=j82Z2VB5smTbYCSbez7WIpzKsspn8V9kREaWFCpbqYbKzlIifOgmQeOBwh46WotXnEtkVBREUw2cKeITdGi93rVKxC5ELeQcIiPHYHHEUZZH3wnhDbhOZXFYFx2-Fa9ht6RbwCYYcpC50Ao9CrNecBdd1irqJUviJA3Yb_nb5DUg7lXrGCjvM0IqkOvO5Grtainyob5bLDV2RHNmHxcfWrxj6z0bkqBJ0c0Kx_qC4EvRZVwWsI1iYlIzFS-zTxnS-ddyVomaEpSORIZCSSe_bJj3KFlo6QbhFtR1CuL7aqXpfP3G5oRt7Tyvq5TGIDnilE3mZwg2smWxkMDo3hnYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تقوم بهدم جميع منازل قرية المزرعة الشيعية بريف حمص بالدبابات والجرافات وتوجه سكان القرية بالذهاب إلى إيران أو الضاحية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80365" target="_blank">📅 11:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
ميناء أم قصر العراقي: استقبلنا 80 سفينة في حزيران بينها بواخر عملاقة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80364" target="_blank">📅 11:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80363">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5dfj3eJ28XNaWOqLlMrxTLuPNiHnaXjoUgaT8Nzif7zbBO1F5yYL8AUTwz1uE-3A8JjxNKrY0aG4tTsTpbP6FEdMGPJ8bFMXP8T63gcuEMyKF4g5PQcPjqU-VvorbWMX4vDXNUX0uHnyjIFWNH5zIRXuxBPVuPradsaMaYt7ktUZC9KRkabSHuhycLcnW8L_hXMLwVJa0vGm5DrZhrPNr4VsjVPXIGTVlXEeGKmLU71WEVxb0gg5ec5wLNWw8hZd89BK4oCEXgcf_TRgN-R9ubYZGLJsvGcp5IFKXgB36bNxao7P8BDTl242p2ir94u4XEGnAi6BOlFUMm36ozePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إعلام كردي: توحيد قوات البيشمركة شمال العراق ولم يعد هناك شيء باسم القوات السبعين والثمانين، وسيطلق عليها قيادة المنطقة الأولى والمنطقة الثانية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80363" target="_blank">📅 10:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80362">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
رئيس لجنة الأمن القومي بمجلس الشورى الإيراني: مضيق هرمز الاستراتيجي جزء لا يتجزأ من السيادة الوطنية الإيرانية وإدارته هي مسؤولية طهران وحدها.
لا تُضمن السيادة اللبنانية بنزع سلاح المقاومة بل بإنهاء الاحتلال والعدوان.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80362" target="_blank">📅 09:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80361">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeASh2Ka_pyNPeCTaD-lciGkZyOvZDBb-b_Y6bjV77MlG7PUIXTOQIIX-DamzqrBGs6EFJH0P5NNDhF6kVqOO3qSDGUTE5ZtSBK1kZh6fY4oed52Aa0VtU98uk4Rkd_kvWraVHsK1iEi4l3EIgjlEly_Mqb2jhr1rBe2dVgtJx3HbF5XWC56zjVXWZZ8vh_waQKMeYSazYt5hGtk57UWyAtJKlOjQZ_HhIiQ2TQurZguxCDXhjMgrE6LcHMwKnmjTz0s9QRCMK-8c5HcS3Y6pP6dIIaHj-sP4xzdfBLFsu7usKS0od1yRm1iOdep1WWEPb3bDs5JLWUyzopCFqBWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Despaseto</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/80361" target="_blank">📅 02:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80360">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في بافيه مقاطعة كرمانشاه الايرانية،شهيدين كحصيلة اولية من الحرس الثوري.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/80360" target="_blank">📅 01:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80359">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a452ae09.mp4?token=Cqzx-FjYC4gLlZ04vgSqbQdC8p94jyYkASXtGW-FjTvYoYQViRHHNjLfc1Go6Nvlk0nxTlJQ60hbzRrwLskE-3Um1IxJxt1qFFDraLLH5veBhgAVQgMYL452z4cM-T_WGqCJiqia3tZBV9U6kilPgkJGtaYsqND3Ma0kg0C3iEgMwmgFXsvReG5gsxMFz-sB1NvBa7KVEFokvXVdDW_JXaQZvd15hVQJG_6fEPqOVUTzD-oOg_hLCMy_u2nRY4qb1EKGlkOe62qcqhfDsUPL5i9BLz4DkZvEPk0bVrf1iuo78pi7L-dZB6I7d9EYS_Ek1UHYS7jM895liOGvtg7nmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a452ae09.mp4?token=Cqzx-FjYC4gLlZ04vgSqbQdC8p94jyYkASXtGW-FjTvYoYQViRHHNjLfc1Go6Nvlk0nxTlJQ60hbzRrwLskE-3Um1IxJxt1qFFDraLLH5veBhgAVQgMYL452z4cM-T_WGqCJiqia3tZBV9U6kilPgkJGtaYsqND3Ma0kg0C3iEgMwmgFXsvReG5gsxMFz-sB1NvBa7KVEFokvXVdDW_JXaQZvd15hVQJG_6fEPqOVUTzD-oOg_hLCMy_u2nRY4qb1EKGlkOe62qcqhfDsUPL5i9BLz4DkZvEPk0bVrf1iuo78pi7L-dZB6I7d9EYS_Ek1UHYS7jM895liOGvtg7nmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
توثيق من تجهيز موقع المصلى لاستقبال الجسد الطاهر للسيد علي الخامنئي، استعدادا لإقامة المراسيم جماهيرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/80359" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80358">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGFwHjBk-rxWrfAoGbNHN39IxOw6DZH8MbRBYjg3xVLLg69_uwN6pIUQVRl64ck4xDAtGLKgM81D7OWg6Ji27AMMWfr8l1kZEIIltqMrt-_SaxxOnYlCfLXqZFbClRnE6DNpgCHbM1EVAKN79Ui-Q-eOyN7K7dfAqpgmQSCjWH-hayxrDLVv_j1EgKu4tMiexjIcZa7gcn5m_nrBuiYJDJmCTs4jElxK0lq2Jb8_1-rAP9hR_SBBhKNGsa_JZn1qZ6C7cT_XxTIe2u1u_h6dewVCTrh-XyrF8UtoHGjOVJ88KknPE1Eyw8wW1LIZfvvfOmaYikagOmm-GkBRkJfpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
وزارة الاتصالات العراقية:
الاتفاق مع شركة فايبر إكس على توفير الإنترنت المجاني على طريق بغداد - كربلاء خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/80358" target="_blank">📅 01:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
انفجار في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/80357" target="_blank">📅 00:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80356">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
انفجار في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/80356" target="_blank">📅 00:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مداهمات في منطقة زيونة شرق العاصمة بغداد للمرة الثانية تطال منزل وكيل وزير النفط</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/80355" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80354">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
اندلاع اشتباكات مسلحة في قرية يارمجة بمحافظة كركوك، شمالي العراق، بين قوة مسلحة والجيش العراقي.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80354" target="_blank">📅 00:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4zu4LDcNZDywQz1TrkyYx16Q0NPNiuTYRRefGZr1OBqypHrzjO5Ryak469dmVfgoo8XDVwdw_KeK-DYFHZoSbDvjgk6KfRrlex_nule1YXKx9b1EZn6CRf4__m2jpAh8T8VrnxujLa1rDPlHlgjjyJbBMDvOaz553GuQQ0a-dZ_8bmlcP7FQ4K7qoksNox4caCgDm1etx0yjx_ra5zBbo6-xuDIXbbpxfbnVd6vjUSdTLt6HHuSBPk94RohfotNAy7C3OPkPiImz7H8WWXkORu-SFBX9W0GYl2a6Pqepqt5b6Cr5jEg-19EjsBd3oil0A9xKOUOIR9zBEOX-wnHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
توثيق من تجهيز موقع المصلى لاستقبال الجسد الطاهر للسيد علي الخامنئي، استعدادا لإقامة المراسيم جماهيرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80353" target="_blank">📅 00:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80351">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9cjQbBKWndOIiVKZwqp2JzXlWLR3VaJF9KlmMUSVR_RdQ2PgjElP7duzHuIZe41rSW9eERVlkBI0ZFqpGsQHV33nqtc6MNres37W4BV6A2PHvYTty33AdwAHKL5k5eBUJWp2ozxFfXfgGUlMc4sA_qghZIstNzXCRRAec95pAlJXwlGx1N5rO0zeSPQE0dhMX1qF0Ck20ipAFAjmb_DPa7qBlQ58JnBo2QzCZ-w4UfcuRzHm3i96MRDLJx54M-weNJdDdtRGc8Q9L24S0BPHQUgGqLsaaTueSEEl7Ap7YR4DJDUylMixkgcsYMY1k1O-LOgf7IkHeG3EVQFDg-LHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7da4bff7.mp4?token=BCjp9NfiqItgYyZ_X-kgTPnxKhNXlV3MlOpCIifFTH1KaDEMrBSmmCiPJRbBtcnFx41GjIJr0wiBOv-IZL5AQzravga0noRSdGX2fr2Bfcpi_7OCZWruOzPyl5tfd6ryGUHiJ8Ume6jYfCAGITtPgGjtFQH9FCwLtfO7K6xAA15TaREXCr7U1moayhyc-595S6xxhJVsZoLnVmWSMKvPGf8OSlBOpgaMMV8bLYsVjJ0af0e24e_Xqn86oUoC6kS33MxR2bmQ63xBqEteMokkes0AFpf5ThVcz1lfwIgFqc9CLht0MCmqM1tiTsV6wVLeA5tROCXvSqz4xQed5E9R1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7da4bff7.mp4?token=BCjp9NfiqItgYyZ_X-kgTPnxKhNXlV3MlOpCIifFTH1KaDEMrBSmmCiPJRbBtcnFx41GjIJr0wiBOv-IZL5AQzravga0noRSdGX2fr2Bfcpi_7OCZWruOzPyl5tfd6ryGUHiJ8Ume6jYfCAGITtPgGjtFQH9FCwLtfO7K6xAA15TaREXCr7U1moayhyc-595S6xxhJVsZoLnVmWSMKvPGf8OSlBOpgaMMV8bLYsVjJ0af0e24e_Xqn86oUoC6kS33MxR2bmQ63xBqEteMokkes0AFpf5ThVcz1lfwIgFqc9CLht0MCmqM1tiTsV6wVLeA5tROCXvSqz4xQed5E9R1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏شرطة موناكو: انفجار كبير إثر عبوة ناسفة ثلاث ضحايا كحصيلة اولية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/80351" target="_blank">📅 00:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a4a7c7ec.mp4?token=KFQCiw8xCqbNoNQT_HnNcPBqsodoGt1J8nSyxkVNvJdI9gNkjOhi9yT1GesO6igIaAwl5fRjamTn2U9hfdY-cKdHMiro_jwDuScF1YFx2YxoF3cIfbP3cwpqDEQ14tbSMeTLN2W8wT5bFDy0NBG5qA2gjYlDzY3hkrAyFTuxK0R6YoSLT0LgXO7bAC05C8H_uugdBHnmyRW2Jm7GEIFVYT8XwmG3s2T2qJjOeMPIRipzA8lOS_SFQitPeHYUJlsS6hu3sUHfQ3sbT43nK7Ah_lqgXXkhTdoGBJga2ta1ay_mzQZZkB8SckCO6uKb30ctUO8SSvi0Nsx1Nu89DjTr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a4a7c7ec.mp4?token=KFQCiw8xCqbNoNQT_HnNcPBqsodoGt1J8nSyxkVNvJdI9gNkjOhi9yT1GesO6igIaAwl5fRjamTn2U9hfdY-cKdHMiro_jwDuScF1YFx2YxoF3cIfbP3cwpqDEQ14tbSMeTLN2W8wT5bFDy0NBG5qA2gjYlDzY3hkrAyFTuxK0R6YoSLT0LgXO7bAC05C8H_uugdBHnmyRW2Jm7GEIFVYT8XwmG3s2T2qJjOeMPIRipzA8lOS_SFQitPeHYUJlsS6hu3sUHfQ3sbT43nK7Ah_lqgXXkhTdoGBJga2ta1ay_mzQZZkB8SckCO6uKb30ctUO8SSvi0Nsx1Nu89DjTr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
في الوقت الذي تلاحق به عصابات الجولاني الشيعة في حمص وتهدم بيوتهم وتهجرهم إلى الضاحية وطهران على قولهم.. جيش الاحتلال الإسرائيلي يبث مشاهد للرقص والدبكة من وسط المدن التي تدعي حكومة الجولاني أنها واقعة تحت سيطرتها.
نشوف اليوم ينزل بيان إدانة ولا تبع مبارح بيكفي
🙈</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/80350" target="_blank">📅 00:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
‏
الرئيس الإيراني:
سنلتزم بمذكرة التفاهم إذا التزمت بها أميركا.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/80349" target="_blank">📅 23:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80348">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
‏
شرطة موناكو:
انفجار كبير إثر عبوة ناسفة ثلاث ضحايا كحصيلة اولية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80348" target="_blank">📅 23:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba122719bb.mp4?token=N7ngRGdfLIzUNNZ2V0vH8M_AHjpNEBwAo0-_QepNl54T50KpJGhAMUWwF1ohMZzXmxNqz6MxsToSCAPMkiLiKq8E0i92hsWE9mA-fmJAek1AjUOJ0KFJKL4B5Up47aDRieZMVQdn6YwOS7OkxjpDCVuPo1nze74ur4pdh8xm4ys7f7S6pmFvwGHddGC3KwJ5B6AApYgoOy_Rif1oKJp4P6uRZEreqy14qoOT1F2sJslRxd-mcx7cA4hXX4yPqKyzeNfzORcZ-pM-j3JAgq9bXYhw-DfxZEAYIZfpelgucHuUTE3xtVp-nG1O64aQZnzmNPfHJU7iyP_fa-YSZbR1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba122719bb.mp4?token=N7ngRGdfLIzUNNZ2V0vH8M_AHjpNEBwAo0-_QepNl54T50KpJGhAMUWwF1ohMZzXmxNqz6MxsToSCAPMkiLiKq8E0i92hsWE9mA-fmJAek1AjUOJ0KFJKL4B5Up47aDRieZMVQdn6YwOS7OkxjpDCVuPo1nze74ur4pdh8xm4ys7f7S6pmFvwGHddGC3KwJ5B6AApYgoOy_Rif1oKJp4P6uRZEreqy14qoOT1F2sJslRxd-mcx7cA4hXX4yPqKyzeNfzORcZ-pM-j3JAgq9bXYhw-DfxZEAYIZfpelgucHuUTE3xtVp-nG1O64aQZnzmNPfHJU7iyP_fa-YSZbR1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تحليق مكثف للطائرات المسيّرة في سماء العاصمة بغداد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80347" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ec5551c0.mp4?token=bw_YtbNCnYadPtFq1M6-P1fZKCb4fstfNJXloB27i6RAIMDlpwQ35Bn6yAjlOI6Mnm8xsS5afvkVBIuSbqbpJWrBTkuMVe2_PeZryBekAZApvsmIgPQ1FTvfdGMgoJM58j9B9WLBXoJPIeD5lGNn5zQd5U9-SPOr8fby6KQ_wzDPcQvMFLhU8LTTKB7oFDslcrHob2FjAMXdZVLWNtVEwgQ2-91P4A0xdiTi2LzHb3PrnfVDBFX0vy6KYhWzzsaO1103vjC0L8e-qMQnFCtrzL6OH5SEgp2B3e3yAS5oZUwgFgZ5jNIrpRaUde72CB8_2cjDpDUQjPLCnlWH2nhrjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ec5551c0.mp4?token=bw_YtbNCnYadPtFq1M6-P1fZKCb4fstfNJXloB27i6RAIMDlpwQ35Bn6yAjlOI6Mnm8xsS5afvkVBIuSbqbpJWrBTkuMVe2_PeZryBekAZApvsmIgPQ1FTvfdGMgoJM58j9B9WLBXoJPIeD5lGNn5zQd5U9-SPOr8fby6KQ_wzDPcQvMFLhU8LTTKB7oFDslcrHob2FjAMXdZVLWNtVEwgQ2-91P4A0xdiTi2LzHb3PrnfVDBFX0vy6KYhWzzsaO1103vjC0L8e-qMQnFCtrzL6OH5SEgp2B3e3yAS5oZUwgFgZ5jNIrpRaUde72CB8_2cjDpDUQjPLCnlWH2nhrjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد توثق دخول قوات الأمم المتحدة (UN) إلى قرية عابدين في ريف درعا.
جولاني وينك بدنا البانجان مجقجق باللبن
😂</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80346" target="_blank">📅 23:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
المحكمة الجنائية الدولية تفتح تحقيقًا مع مسؤولين كبار من الإمارات العربية المتحدة ودول مجاورة، بتهمة المساعدة والتحريض على ارتكاب جرائم وحشية في إقليم دارفور السوداني.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80345" target="_blank">📅 22:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
الإطار التنسيقي يدعو جماهيره إلى المشاركة الواسعة في تشييع الشهيد علي الخامنئي في الأراضي العراقية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/80343" target="_blank">📅 22:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
مسؤول أمريكي:
دورنا يشمل استخدام قوات أمريكية على الأرض في لبنان وإسرائيل
عون وينك السيادة عم تبكي
😫</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/80342" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80338">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yf3Dp1T7MDDEt6W7_8HIJ_8YXqpXk_oBkq-uZvQ8JSZy4Bq1LgohD33SmuM6gui_J4Y0L4PQM9hXSEBfnWbxOENepTuVU-Olrs2IjK2--MUaP-uQxqHjBv850kjooSblfiX8B0UyBEf70g1bS73flLffVWF5vxwaIWYhUZpg16jQkuhMyxcAiU_ttWnFSeJlM5YHGL7_vYexVUawnTta18CgaIkUn1vphKVngEbnOPkQQ5WOOXyRRlfWHBIwhZoePFJoGTsyxD8ILh5wf6W1c2YcUIn53907mFDcXp4PzVTV2QGRbTzEsKtz6ZJxgYC_3l2ojVOtKHCrKg-sEXkdmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPkpc8wud0Y5EAEJlZoQj-4_X5hAMJ_Dpg7hiTr04LZ_JLGbz1ckUFHH1jGemdNUc2dJaklqSzNLfIICqHpB7PQP0qMBSqIdX6R6frsJH1W0OD5_Oy7pP3Vcg2MQ7QhGU6NcbqGbJbLrkN4rK-rrOoUpUPeL_vEY6BGouDH91bYWe7P7B8acCFVuZg7tmG2wn1yKKjmf8rtxi9tsTGEW6QNkLj7QhmhyxfJVaL8DDRSNjVWN83ugdVT8fFoUgdBsNZ6042ElQq6u9Z5iwLoTf4TxcaxeiXY8knSgdDukurtL88sEY-3-cia-1gDWeDb2uwzUB9AIritXdYeLS-Ooew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYdVo_hDPrwXQeeqCIigX8C6kIeDagpyeIfpigwekWr21nKoJS8kj-qYtRFLpwgG95zKjbMvhk1HvDjQyyUkM5i3jrNUIMHTqYsetiCzsATuaATcaK3boltQPx0MEF8HqPqyliiPJzHbfRJCx_cw9cjFKS62rCIicya52yuQRy6xg74elpmzQN9QMcypurD2DBxa7qInaCZS8nmDuvaB9_ZdGCxMenVHCXdilx3GxoQbbCEj4Ae1-y1X0i9HKc0sp3fOgyxZ6rtMkUVAM3dJ_MBy3IBIypq7YskDNjYPWFABIHl2KYdN9oNhMdxdf11TUs88hhrzT-8QsHtPBRD4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-hr2CTe9_M9jeC5_Gsu_yDdT4t46xUahn3aj1tQbsTI1zxYFC4e2YrQCoogD9_FOA3wbkbh9loji0cL5Fx5IxGgtCvF0BpDi3NBKGQNmv95YTGGUG6Ln_c61XFURNfTTcxM2_uV4_ca2XIkOjIDv0jSn10oCy18LE2SbNxRwb8Av4zUbMaM2xMyb3Yo5lIqAVJjlK7vafH2C6S5o7hhtci76QnTr5gmUVYU7NOdwzfPg1_Vs8rZBwvW48aIMsFpOYxDifvhPkoRtvU83Byy7MlMABOtUIUaJLFaD0AaSh9vtie47Z311GRAlqjpOfIjRkoKylrdCuKJ6iLX9mTK_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
مجلس القضاء الأعلى: التحقيقات مع وكيل وزير النفط لشؤون التوزيع تسفر عن ضبط 11 مليون دولار و4 مليارات دينار</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/80338" target="_blank">📅 22:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
🔻
مجلس القضاء الأعلى:
التحقيقات مع وكيل وزير النفط لشؤون التوزيع تسفر عن ضبط 11 مليون دولار و4 مليارات دينار</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80337" target="_blank">📅 22:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية إسماعيل بقائي:  وفد خبراء إيراني يتوجه إلى الدوحة لمتابعة تنفيذ التفاهمات.  زيارة الممثلين الأمريكيين إلى قطر لا علاقة لها بزيارة الوفد الإيراني.  لن نعقد أي اجتماعات تفاوضية على أي مستوى مع الجانب الأمريكي في الأيام المقبلة.…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80336" target="_blank">📅 22:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a3817a74.mp4?token=lRUEu_5ybghrgiBNbk6LaYQhIr85n1IkX0XQxkunuCi2BzoUDTZC-IbqKthohzN9Po_03wumtEpF-lj3q7d-5VrOLGYr1IuGyX12Uqw02QUrAHhmv6J1F8Zfe91WFU-cwPnP8ihnBWW1gQPfPUm6-N6HerBmx7C9WiQLJj36_c0n2J54tXfvfMu31sVg5sL5t4Vl7BqfFRJi9ZZE6eIapih1GcIyx4ueEb_WBF8X9Jlv7Gq20ImstGbP-9ppOIkG94beBb2ISe8adH6uoJRcZoXIQVS-N70PipYxdWzOd01pbTdUavPyBGMPDlWekHwjGpFVox-vB8aaPCDsz6Hvyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a3817a74.mp4?token=lRUEu_5ybghrgiBNbk6LaYQhIr85n1IkX0XQxkunuCi2BzoUDTZC-IbqKthohzN9Po_03wumtEpF-lj3q7d-5VrOLGYr1IuGyX12Uqw02QUrAHhmv6J1F8Zfe91WFU-cwPnP8ihnBWW1gQPfPUm6-N6HerBmx7C9WiQLJj36_c0n2J54tXfvfMu31sVg5sL5t4Vl7BqfFRJi9ZZE6eIapih1GcIyx4ueEb_WBF8X9Jlv7Gq20ImstGbP-9ppOIkG94beBb2ISe8adH6uoJRcZoXIQVS-N70PipYxdWzOd01pbTdUavPyBGMPDlWekHwjGpFVox-vB8aaPCDsz6Hvyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مروحي يجوب سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/80335" target="_blank">📅 21:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭐️
هجوم إرهابي يستهدف عجلة في مدينة سراوان بمحافظة بلوشستان الإيرانية ؛ إستشهاد شخص وإصابة أخر كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80334" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">البيت الأبيض: ويتكوف وكوشنر سيحضران في اجتماع الدوحة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/80333" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUVzFGuIBiG8jouGUlffGlDrCLJrQ_ZHc7Bhf9u9L2EFdJquUEE6Htwoqr5NihRet5LJdbuNmwGvYxx7uhe-lq-MpssCi1kdK0KbsuvnZjUcRVvJLFnqz9V-ED9tTMKhAaDUhsprgEJ3MwIn6nohL2aUz12moAsNjA-_UwM3gVttkGlhASvNqp3F_FCk4FItDGARr5GvHS_K-B-cotHyImIUyFQxbsx-X-2lq_9Ja0ktBgNPwxB9k4qft4rZpdOij-uojdZmjG2QHw0XrmjLUFPGbmH4LdpZUHx17wMHnLsRzWm98bbZG097VuQBG3yNZlchIr2CGBE7zNhDVbsWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
قيادة الحشد تبحث الاستعدادات للأربعينية ومراسم تشييع السيد الشهيد الخامنئي.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80332" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تحليق طيران مروحي إسرائيلي بأجواء عدة مناطق في حوض اليرموك.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/80331" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اعلام العدو: تم تفجير عبوة ناسفة استهدفت مقر القيادة الميداني لنائب قائد لواء الكوماندوز في جنوب لبنان. هناك مصابان من جنود الاحتياط في الوحدة. أحدهما في حالة خطيرة، والآخر في حالة متوسطة، وقد جرى إجلاؤهما بواسطة مروحية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/80330" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80329">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية تحذر فرانسا:
إيران وحدها ستتولى عملية إزالة الألغام من مضيق هرمز بحسب مذكرة التفاهم.
لن تشاركنا أي دولة في نزع ألغام مضيق هرمز ولن نسمح بذلك من حيث المبدأ.
الوضع في مضيق هرمز حساس ومعقد وننصح فرنسا بشدة بعدم تعقيده باستفزازاتها.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/80329" target="_blank">📅 20:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزير الخارجية العراقي فؤاد حسين يلتقي الارهابي ابو محمد الجولاني</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80328" target="_blank">📅 20:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80327">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
🇮🇷
مسؤول أمريكي:
أوضحنا لإيران أننا لن نفرج عن أموالها المجمدة إلا إذا تحقق تقدم في الملف النووي.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80327" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzLb_04Jfi15BfXObrChlnOYFUV0-pRYSDZcBL9ws5_kDDhiu41piI8eEuDrxehJUY5kOgktWLcDspG6tryB7wP-X5aNig9FZsg-1p_jiDIeq1nm_XnuzmVsT1TL20qjXOT_pvM002zFhc8TTm0k1-UZWqKkYlJnNGN84rgI4eDbYEu8qUJnzY1Lwz7KnE9QyJwPJJBv38U2qU-cAkARC78Qt9TP_vjcy2UvpMMHBcTxWTlAbtvJowZ61nl3zY_1u8dIfygddP5qsx4n491CBH5AunqKlW-Ut5og9K0lQbW1Rq5rQy--NHc9eeX-MX_Xr5Tpo20FX1e1WeKziPgsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب:  «انتصارٌ كبيرٌ قبل لحظاتٍ في المحكمة العليا، في قضية سلوتر، حيث تمّ تأكيد سلطة الرئيس في بلادنا لعزل مسؤولي السلطة التنفيذية والمعينين في الوكالات، أو الممثلين، بموجب المادة الثانية. لقد سعى رؤساء الولايات المتحدة إلى هذا القرار منذ زمنٍ طويل، ويعود…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80326" target="_blank">📅 18:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80325">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الاسرائيلي:
نتجهز لمعركة جديدة مع إيران في اي لحظة يمكن ان تحدث ولن ننسحب من لبنان.
اندلاع الحرب مجددا مع إيران قد يحصل إذا قرر ترمب أن المفاوضات استنفدت أو أن تهاجم إيران إسرائيل.
معادلة هجوم حزب الله على مستوطنات الشمال تساوي الهجوم في الضاحية لا تزال قائمة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80325" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80324">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIt-ZXJ1PkHBEUT_Uj1A87eQIAbhCd2tVOYqX5DTXT5Mc2k11_aIJ1Es-c4vufZL0qIqjFPRyM1MC3bsL8F4qpAtoEWBmQJnrDW335j5AlbS77xT-mmhLnkSvebdQx_2u86j2nFpagkL732BIIrZMYxw24dlJwaYy36REhYrR0wbUEGOi-7PZlE9kUCeHg72KDMPMicSIooqE7DKiT5y_PI7jjtqIQVBTW7UZoND1bkwiXGfg5b1_y0cbS28ScTuyDNJwPeBTP_aMVwpEGXlYBaMD6HKdSNlTpqb0XYZ6LrpqtS-MCaSVyuCrZgy5jik9AkSqDbOzPEF9OiICacxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
«انتصارٌ كبيرٌ قبل لحظاتٍ في المحكمة العليا، في قضية سلوتر، حيث تمّ تأكيد سلطة الرئيس في بلادنا لعزل مسؤولي السلطة التنفيذية والمعينين في الوكالات، أو الممثلين، بموجب المادة الثانية. لقد سعى رؤساء الولايات المتحدة إلى هذا القرار منذ زمنٍ طويل، ويعود تاريخه إلى ثلاثينيات القرن الماضي. إنه لشرفٌ عظيمٌ لي أن أكون الرئيس الحالي الذي حقق هذا الحكم التاريخي وغير المسبوق، وهو أحد أهم الأحكام التي صدرت على الإطلاق فيما يتعلق بصلاحيات الرئيس. شكرًا لكم على اهتمامكم بهذا الأمر!»</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80324" target="_blank">📅 18:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قد يغرد …</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80323" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80322">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
وزارة المواصلات القطرية:
حرصا على السلامة العامة، تهيب وزارة المواصلات بجميع ملاك ومستخدمي الوسائط البحرية، بما في ذلك قوارب النزهة، وقوارب الصيد، والدراجات المائية، وسائر الوسائط البحرية المماثلة، التوقف مؤقتا عن الإبحار وممارسة الأنشطة البحرية، اعتبارا من تاريخ صدور هذا التعميم وحتى إشعار آخر.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/80322" target="_blank">📅 17:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80321">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
العثور على جندي بالجيش الإسرائيلي مقتولاً في وسط البلاد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80321" target="_blank">📅 17:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80320">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزارة التربية العراقية تعلن استرداد أكثر من 73 مليون دينار لخزينة الدولة في صلاح الدين بعد متابعة دقيقة لملفات التقاطع الوظيفي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80320" target="_blank">📅 17:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80319">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئيس الوزراء العراقي:
يوم 30 أيلول المقبل سيشهد خروج قوات التحالف بشكل كلي.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/80319" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80318">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
احسان العوادي رئيس اللجنة العليا لتنسيق مراسم تشييع قائد الثورة الإسلامية الشهيد في العراق:  لسماحة آية الله العظمى الإمام الخامنئي (قدس الله نفسه الزكية) مكانة رفيعة ومتميزة وقدم هذا القائد العظيم خدمات خالدة لأمن العراق وعزّته وللعالم الإسلامي، أنّ إقامة…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80318" target="_blank">📅 17:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80317">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
احسان العوادي
رئيس اللجنة العليا لتنسيق مراسم تشييع قائد الثورة الإسلامية الشهيد في العراق:
لسماحة آية الله العظمى الإمام الخامنئي (قدس الله نفسه الزكية) مكانة رفيعة ومتميزة وقدم هذا القائد العظيم خدمات خالدة لأمن العراق وعزّته وللعالم الإسلامي، أنّ إقامة مراسم تشييع سماحته في العراق والعتبات المقدسة تمثّل شرفًا تاريخيًا للشعب العراقي، أنّ الحكومة والشعب العراقيين لن يدّخرا أي جهد لإقامة مراسم تليق بهذه المناسبة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/80317" target="_blank">📅 17:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80316">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏وزير الحرب الصهيوني: الجيش اللبناني لن يتحول فجأة إلى أسود تهاجم حزب الله.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80316" target="_blank">📅 17:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80315">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFYQ-lOSDmpwEtESs9HvLjJqqMWoExxgjKKvv-H0K_DahqT1NZsDlZBWOGia_32zWgHzDgGQGWVPoZE_knFaul3unrYSN36UskLGNtb9JfL0zT_96rCjQ8I7vVzbAy9710OdV2fsdYiETi85ksqaiIfrNino0wJVFcxfaaIRVOKBoGI4ywX9uj2Hw2lIbtoaCxcSAJB3UhgfU2XSLvYhu2ICGeMQotnMJ-yTWgoJBrC3M97BsZ3TGPEe-Hkzp3BtgKGS9ADD0pnZRpXwqETqF5AL8Difqi7VxM2jem3Y3PoimsUxRaHs8hugXkduEqDTq5o5YRPcGCf_8XxoRG39WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية العراقي فؤاد حسين يلتقي الارهابي ابو محمد الجولاني</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80315" target="_blank">📅 16:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80314">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏وزير الحرب الصهيوني: حزب الله عزز وجوده في الجنوب بسبب ضغط ترمب على نتنياهو</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80314" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80313">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
وزير الحرب الصهيوني:
حزب الله عزز وجوده في الجنوب بسبب ضغط ترمب على نتنياهو</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/80313" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80312">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760337d8fc.mp4?token=O61619eUAk6USSahFwksBJS1_yoqhOGH4X6ptfs9yzsWbTmoCum3Lfw_bG1SNKODQ4oHPSw7c-0iv9xrj1eLJmixVlZfWuX9hLxVIe42NOlplCR5AZIvNOH2GNJDqvP5jafuw6l6PlPKksL-9xPBoNrD4_aMVBLno7tE7qM3650sbbaR1XHh1yjYeelD1KmB8CYjX6so3LBgtPwpiVxx-lTfTLTh4Z6gMA-lqtZGER-UKXFYobXfwWsKGJFX1Sf0ojpi6gRMuOTLyNG-gDQ91kUTQ2APpkHn5fJGO6W6kMuSXVrsbFhEX-Xw-_0trt1PL_lGJTcRihtKIqs0Xy1pnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760337d8fc.mp4?token=O61619eUAk6USSahFwksBJS1_yoqhOGH4X6ptfs9yzsWbTmoCum3Lfw_bG1SNKODQ4oHPSw7c-0iv9xrj1eLJmixVlZfWuX9hLxVIe42NOlplCR5AZIvNOH2GNJDqvP5jafuw6l6PlPKksL-9xPBoNrD4_aMVBLno7tE7qM3650sbbaR1XHh1yjYeelD1KmB8CYjX6so3LBgtPwpiVxx-lTfTLTh4Z6gMA-lqtZGER-UKXFYobXfwWsKGJFX1Sf0ojpi6gRMuOTLyNG-gDQ91kUTQ2APpkHn5fJGO6W6kMuSXVrsbFhEX-Xw-_0trt1PL_lGJTcRihtKIqs0Xy1pnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تقوم بهدم جميع منازل قرية المزرعة الشيعية بريف حمص بالدبابات والجرافات وتوجه سكان القرية بالذهاب إلى إيران أو الضاحية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80312" target="_blank">📅 16:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80311">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
🇮🇷
وزارة الخارجية العمانية:
عقدت اللجنة المشتركة العمانية الإيرانية اجتماعها الأول في مسقط بشأن مضيق هرمز لتبادل وجهات النظر حول إدارة المضيق مستقبلاً والمسائل ذات الصلة.
ناقش الجانبان سبل تعزيز التنسيق بشأن القضايا المتعلقة بمضيق هرمز بما يتوافق مع المصالح المشتركة للبلدين وسيادتهما، مؤكدين التزامهما بالقانون الدولي، واستكشاف أطر التعاون في مجالات الملاحة والخدمات البحرية، انطلاقاً من كونهما دولتين تتشاركان المضيق، وفي ضوء التفاهمات الثنائية والدولية القائمة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80311" target="_blank">📅 16:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80310">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
زعيم المعارضة الصهيونية لابيد:
لن يشكل نتن ياهو حكومات في إسرائيل بعد الآن.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80310" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80309">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34c356325e.mp4?token=tq-zUVanG7-k9O-_ojuyBczq0eEKg8o22Ed2f8ThOUeGEkQUMoZ3Y_K7CjAX12s2YJGjcAEfGwImYrkpeyXWBo4HxgiiQ9PtoZWDgL68G1AS01XFJ8h-Yf2vzflAhF3DD1fWwPnn5u8rdITpJjUVImeOTI31X9Jyu6JKQfzV25dE5AX8LZA2EF49dYyp0YMFzNOjf5qSl070OOjdk_yvrgd97ddhyDTc9sXKLeXFrR5uGidj5UG9G5Y76FHg1rYc2bqJSf-ddkS8UEbW25Z_juRVRZKoCn7vFXMT8BcfvPBlH78ZtvJg4nRCZxw97woYM1-qqXpg-TAvpLSO392bb2LwjYJx55VstgJWkkPfcX-IiVPaDKeli7QZUMRheZ5Mmv-ChrfQz5a3PHJRP4fiZcAF460vws6P5T0W7OmLTgnSQYWsCofOFhpb1ZUZ7aNbWWcQCNP_lbXMS2abfTDa7_FWcVpwUFDgUe6nh874d5mElmMkYvIWgUqzSEB-KZNvU2jmJix0FZFzNbDkOjfftBNyfDXi6czqenKLELbt65vU76KGpHpPI2oTu34-NkNTQkORiXMGhOHtES1mIXQvnNXFIOIJoz7U7DkWw6rvq6s0P1yYOMEAkjl-11oWS6FLIGD7m60QexzyUoFsa_uLk3RSpjYmAWFQJmfu2qXf-es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34c356325e.mp4?token=tq-zUVanG7-k9O-_ojuyBczq0eEKg8o22Ed2f8ThOUeGEkQUMoZ3Y_K7CjAX12s2YJGjcAEfGwImYrkpeyXWBo4HxgiiQ9PtoZWDgL68G1AS01XFJ8h-Yf2vzflAhF3DD1fWwPnn5u8rdITpJjUVImeOTI31X9Jyu6JKQfzV25dE5AX8LZA2EF49dYyp0YMFzNOjf5qSl070OOjdk_yvrgd97ddhyDTc9sXKLeXFrR5uGidj5UG9G5Y76FHg1rYc2bqJSf-ddkS8UEbW25Z_juRVRZKoCn7vFXMT8BcfvPBlH78ZtvJg4nRCZxw97woYM1-qqXpg-TAvpLSO392bb2LwjYJx55VstgJWkkPfcX-IiVPaDKeli7QZUMRheZ5Mmv-ChrfQz5a3PHJRP4fiZcAF460vws6P5T0W7OmLTgnSQYWsCofOFhpb1ZUZ7aNbWWcQCNP_lbXMS2abfTDa7_FWcVpwUFDgUe6nh874d5mElmMkYvIWgUqzSEB-KZNvU2jmJix0FZFzNbDkOjfftBNyfDXi6czqenKLELbt65vU76KGpHpPI2oTu34-NkNTQkORiXMGhOHtES1mIXQvnNXFIOIJoz7U7DkWw6rvq6s0P1yYOMEAkjl-11oWS6FLIGD7m60QexzyUoFsa_uLk3RSpjYmAWFQJmfu2qXf-es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المحلل البحريني جعفر سلمان المقرب من العائلة الحاكمة الذي كان وقد وصف العراق بـ"جمهورية موز" يقول في لقاء انه لولا الامريكان لكان الخليج لقمة سائغة امام الجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80309" target="_blank">📅 16:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80308">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هيئة النزاهة العراقية: السجن لمدير عام الهيئة العامة للضرائب الأسبق وزوجته عن جريمة غسل الأموال. الحكم تضمن تغريمهما أكثر من (32) مليار دينار ومصادرة عقارات وأموال داخل العراق وخارجها ومصادرة (22) عقاراً في بغداد وتركيا باسم المدانة وبدلات إيجارها ومخشلات ذهبية عائدة لها ومصادرة الأموال المودعة في البنوك التركية والكويتية العائدة للمدانة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80308" target="_blank">📅 16:14 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
