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
<img src="https://cdn4.telesco.pe/file/PKIxG6ZM3HudFY182CK-sG05fmF2EnsNv-12DWwwi3CWr6F9EajkSo7ou64ycKjfQ89TURVlkn_2adoyimoZZ_04TtXUNQvl4kp2CbPiW6TvsDQInbzHRu4aJAd6JGDOquK6cUdOQxJPswBKaA_41cMVhheekAoJJGtsQN787l6O3-ItqjyAemEF-PYM_FH9BidStDs13d1MVq7iJuWKTgBjs9I7xSWCgTIXQZ6hRGPvgmZXF1LdXE-F4YzT_LvUeR6QMr6IJBsc-Lrh09jScd-XDNvvr8NqD3moti6aqDO3nL-g5GW2L6nPPn4d5VYT6rqD4J9lively7k5fqd47Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-81094">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية:
‏مقتل ما لا يقل عن 14 جندياً مدعوماً من السعودية وأصيب 23 آخرون في هجوم شنته حركة أنصار الله على مواقع في حيس، جنوب الحديدة، تضمن الهجوم نيران القناصة والطائرات المسيرة وقذائف الهاون كما سيطرت الحركة لفترة وجيزة على المواقع.</div>
<div class="tg-footer">👁️ 252 · <a href="https://t.me/naya_foriraq/81094" target="_blank">📅 17:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81093">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 535 · <a href="https://t.me/naya_foriraq/81093" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">البحرية الامريكية تعلن مقتل احد عناصرها</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/naya_foriraq/81092" target="_blank">📅 17:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سقوط مروحية امريكية في بحر العرب</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/naya_foriraq/81091" target="_blank">📅 17:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/naya_foriraq/81090" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/naya_foriraq/81089" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
لجنة مراسم التشييع:
ستبدأ مراسم تشييع جثمان القائد الشهيد يوم غد في طهران عند الساعة 6:00 صباحًا. يشمل مسار الجنازة شارع دماوند، وساحة الإمام الحسين (عليه السلام)، وشارع انقلاب، وساحة انقلاب، وشارع آزادي، وساحة آزادي، وطريق لشكري السريع.</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/naya_foriraq/81088" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4l6oKRH0N_qCZHXS5LAnO61kMR6Tf5fp8roWLun4pPR647goR-1eFgsKsm6SkGR43EGUEz-Hk8BkOu4M8jeSOOxp4XPIy-h_ozKZczOSzDjI6Q0s2-FDs2uYzPEryzEXx9Tf3CX-GBc0oPipvABviIXdxJA7w-MZDUho8I17wboXtXL4HJSqtfxms8DWg20UJdBjCTvD8YY0NDXcOmaISnBa4Ier-K9tpZVL7xvli2XQeL6RsypPQzB3c-WK-yLpnSGuVOPn0M68LkBd2aDgNpBKAEfvQlD0rhar8nhYZJKkQzqu6xAKrBSqJSfU_XrWBxmSgoQDHB0YyOLnpgr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحن، الشيعة، نعاقب قتلة زعيمنا.
من مصلى الامام الخميني في العاصمة طهران</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/naya_foriraq/81087" target="_blank">📅 17:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81086">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">متداول:
قوة من النزاهة تدخل مصفى بيجي وتعتقل ثلاث اشخاص (مهندس منهل ، احمد النامس ، زياد الراوي)</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/naya_foriraq/81086" target="_blank">📅 17:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81085">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
اشتباكات مسلحة في ابي الخصيب ضمن محافظة البصرة جنوبي العراق بين قوة من جهاز الامن الوطني وتاجر مخدرات تسفر عن إصابة 3 منتسبين من الأمن الوطني.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/naya_foriraq/81085" target="_blank">📅 17:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81084">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
رئيس المحكمة العراقية الجنائية:
- نحو 3300 أمر قبض غير منفذ بحق أزلام النظام السابق من المتهمين بجرائم ضد الإنسانية داخل العراق وخارجه
- عدد المحكومين من أزلام النظام السابق بلغ 160 محكوماً بينهم 26 نُفذ بهم حكم الإعدام ونحو 270 مفرجاً عنهم
- حكم الإعدام بحق صدام حسين كان عن قضية الدجيل فقط في حين أن هناك جرائم كثيرة مُرتكبة توقفت الإجراءات بشأنها بعد تنفيذ الحكم
- المتهم سعدون صبري أُدين بقتل الشهيد السيد محمد باقر الصدر
- بعض الاعترافات الواردة ذكرت مسؤولية طاهر جليل الحبوش عن جريمة اغتيال الشهيد السيد محمد محمد صادق الصدر
- صدور حكم الإعدام بحق المتهمين بقتل مقلدي المرجع الشهيد السيد محمد صادق الصدر والمصلين في صلاة الجمعة بمدينة الصدر
- ثبتنا باعترافات المدان عجاج بارتكاب عمليات اغتصاب لنساء ومقابر جماعية
- رئاسة الجمهورية لا تملك صلاحية تعديل أو تخفيف أو إلغاء أحكام الإعدام الصادرة عن المحكمة الجنائية العراقية العليا
- جميع أحكام المحكمة الجنائية العراقية العليا غير مشمولة بقوانين العفو العام
- إجراءات الحجز على أموال المتهمين تتوقف عند وفاة المتهم</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/naya_foriraq/81084" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81083">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">متداول
اطلاق سراح معاون مدير مصافي الجنوب منتصر حالوب بعد أيام من اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/naya_foriraq/81083" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81082">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محافظة الديوانية تعلن تعطيل الدوام الرسمي يومي الاربعاء والخميس لإتاحة الفرصة أمام الجموع المشاركة في مراسم تشييع جثمان الشهيد القائد سماحة آية الله العظمى السيد علي خامنئي (قدّس الله سرّه)</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/81082" target="_blank">📅 16:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81081">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d08e53336.mp4?token=cG7VFLzbS6PrxvIyMJvlsmEOkNiGyOv-mNo-lzq3XX1blF7M2w1C2kcNo-nPr5scWy-UIJLwt__oewOQicPMOCLMlSWeBB-1cGAlu1WoGPxaxwu5nwa2TExLfXdEHqgxwVEIsyLU9s8DrV1uv75q6zbs2KAItS0MClnqh_PXhMbcxFfc-uz97EUTIE4mCAYHhkrWNKT7gBQ-_SIO8UifyOBuB3v0Wt1-wHIw_1Pg8VckRrEjHbP4jNZLa4mKNTk9PsRTy_yFaSK64IokRoTGTHmAsjX9C38BvPRdYh-Ve9PDxhYNeEvkaRhnabQSu3xs6blyTzndYy0LWlAEHk8FFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d08e53336.mp4?token=cG7VFLzbS6PrxvIyMJvlsmEOkNiGyOv-mNo-lzq3XX1blF7M2w1C2kcNo-nPr5scWy-UIJLwt__oewOQicPMOCLMlSWeBB-1cGAlu1WoGPxaxwu5nwa2TExLfXdEHqgxwVEIsyLU9s8DrV1uv75q6zbs2KAItS0MClnqh_PXhMbcxFfc-uz97EUTIE4mCAYHhkrWNKT7gBQ-_SIO8UifyOBuB3v0Wt1-wHIw_1Pg8VckRrEjHbP4jNZLa4mKNTk9PsRTy_yFaSK64IokRoTGTHmAsjX9C38BvPRdYh-Ve9PDxhYNeEvkaRhnabQSu3xs6blyTzndYy0LWlAEHk8FFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار امني وعسكري في محافظة اربيل شمالي العراق على خلفية اعتقال خورشيد الهركي زعيم قبيلة الهركي الكردية</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/naya_foriraq/81081" target="_blank">📅 16:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81080">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11259c8a0b.mp4?token=D9T_ANknpMvf4cbWCZKgeHopNvE6QTDcpfSRD8PlhjGP7J98BgdzQ4OHilroPnZSEjyXyTVt7uZc0D1NLnCSrZKHesFaZyt_aCZ9Vt32tDcH2tIZjsmT6TWNnz6VZcdXSRnhl1sNFfDjzsPT92K55zfBXNR0ffHVpn60yuFu4i52YqvgG55VXm7lduzv4yX1vS-7Qf62OcECwbxKmDTj0A-Bcs_dnW2B-Egz2c3mk6F5-R-j6v2KfkU8XPKu-sLsHlajypA4DbZ3zAryO3arntGOmIX4UVccMNw4l7-osR4-eV2W-ef0EPwpENjlHIQxta49sIScSnOjyl5g-HHkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11259c8a0b.mp4?token=D9T_ANknpMvf4cbWCZKgeHopNvE6QTDcpfSRD8PlhjGP7J98BgdzQ4OHilroPnZSEjyXyTVt7uZc0D1NLnCSrZKHesFaZyt_aCZ9Vt32tDcH2tIZjsmT6TWNnz6VZcdXSRnhl1sNFfDjzsPT92K55zfBXNR0ffHVpn60yuFu4i52YqvgG55VXm7lduzv4yX1vS-7Qf62OcECwbxKmDTj0A-Bcs_dnW2B-Egz2c3mk6F5-R-j6v2KfkU8XPKu-sLsHlajypA4DbZ3zAryO3arntGOmIX4UVccMNw4l7-osR4-eV2W-ef0EPwpENjlHIQxta49sIScSnOjyl5g-HHkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار امني وعسكري في محافظة اربيل شمالي العراق على خلفية اعتقال خورشيد الهركي زعيم قبيلة الهركي الكردية</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/naya_foriraq/81080" target="_blank">📅 16:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🫡
قيادة العمليات المشتركة العراقية: طائرات F-16 العراقية تنفذ ثلاث ضربات جوية ناجحة ودقيقة استهدفت ما تبقى من أوكار ومخابئ العصابات الإرهابية في الحدود الفاصلة بين المركز والإقليم من جهة قضاء الدبس</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/naya_foriraq/81079" target="_blank">📅 15:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">طيران الجيش يواصل التحليق فوق مواقع يختبئ بها عناصر تنظيم داعش في محافظة كركوك بعد سلسلة غارات جوية على خلفية استشهاد عنصر من جهاز مكافحة الارهاب</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/naya_foriraq/81078" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81077">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356bbb9ab8.mp4?token=r54iswxwk7tIYkK4XqU5-YlydR-Yg2LCdt4FSJzSiv_qDwuthWn626sBEEO3kaxD2KqqfhLZSk0Z0Xb3tRtUKwCzi82uGuCF3oFRLAclNL3CrrGFQNQiM4CQY4squAXGxgrIsPJIq_Htk3G_vt5yTJtBgXk3IAA0bgEBLHSbDfnadH2F9b9XeVcPpH32vlhjzbt98F0Rq8q1mYTAHjDqVQfSzrPOqXx4Yn9j7qLbeYhuQSc0XdMTKdnO_6SZrReGavwDG6qtiFvzqxgYJAIT7jUfYBA_-Ezra7bVzNvChlaOPwsCUiE_YkBwEkmss--LW5BRNS4HX-P8nCcHGUax8Tus6fAAo9lgkM1yNMdmqaoO4ycWOQsWgCewsqmgZV8dPDePK2CyZL-wp6PqbUqgkmW4kbPnXEkEb5tw04zN0koNb6aXDI8Pr34pVkrXosI8W3Bd4yX4J0fxcmBtkvHzUVxHS34Zx4RUUWggu58_lIa3NAS9pe7KRoYfoB1AhbMYtxoOsa7_V8y_TzveD0veX4bfNrbNgA9H9IXwkPTpDxtz2yfUeGoTBBN_WIrqu_RfDm5FKMykKQaaVdjO6vNqSEI6ZkY8AbKmua1CHGqbJ3c5mtcjK2JHXKTMr1dCM4bckgGq6oA6uBkD_ElGPu4BLLMzY7Bbir_Z3yBx3Y8Q3VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356bbb9ab8.mp4?token=r54iswxwk7tIYkK4XqU5-YlydR-Yg2LCdt4FSJzSiv_qDwuthWn626sBEEO3kaxD2KqqfhLZSk0Z0Xb3tRtUKwCzi82uGuCF3oFRLAclNL3CrrGFQNQiM4CQY4squAXGxgrIsPJIq_Htk3G_vt5yTJtBgXk3IAA0bgEBLHSbDfnadH2F9b9XeVcPpH32vlhjzbt98F0Rq8q1mYTAHjDqVQfSzrPOqXx4Yn9j7qLbeYhuQSc0XdMTKdnO_6SZrReGavwDG6qtiFvzqxgYJAIT7jUfYBA_-Ezra7bVzNvChlaOPwsCUiE_YkBwEkmss--LW5BRNS4HX-P8nCcHGUax8Tus6fAAo9lgkM1yNMdmqaoO4ycWOQsWgCewsqmgZV8dPDePK2CyZL-wp6PqbUqgkmW4kbPnXEkEb5tw04zN0koNb6aXDI8Pr34pVkrXosI8W3Bd4yX4J0fxcmBtkvHzUVxHS34Zx4RUUWggu58_lIa3NAS9pe7KRoYfoB1AhbMYtxoOsa7_V8y_TzveD0veX4bfNrbNgA9H9IXwkPTpDxtz2yfUeGoTBBN_WIrqu_RfDm5FKMykKQaaVdjO6vNqSEI6ZkY8AbKmua1CHGqbJ3c5mtcjK2JHXKTMr1dCM4bckgGq6oA6uBkD_ElGPu4BLLMzY7Bbir_Z3yBx3Y8Q3VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اطلاق النار على المتظاهرين ضد تردي الكهرباء في قضاء قلعة صالح ضمن محافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/81077" target="_blank">📅 15:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
رئيس اركان جيش العدو:
منطقة البوفور هي منطقة استراتيجية حيوية مليئة ببنية تحتية لحزب الله بتمويل وتوجيه إيرانيين، قامت على مدى عقود ببناء شبكات أنفاق تحت الأرض في هذه المنطقة لتهديد مستوطنات الشمال. يجب على الجيش اللبناني الوفاء بالتزاماته بموجب الاتفاق والعمل على تطهير المنطقة من مسلحي حزب الله.</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/naya_foriraq/81075" target="_blank">📅 15:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇸🇾
في اول جلسة له..
ما يسمى بـ"مجلس الشعب السوري" يعلن تأجيل جلسته يوم غد بسبب زيارة ماكرون وعدم قدرة نظام الجولاني على تنظيم الزيارة واقامة الجلسة.
بارعين بس بالتفخيخ
هيج سوالف صعبة</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/naya_foriraq/81074" target="_blank">📅 15:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
الشيخ همام حمودي:
من حق الشعب ان يتساءل: أين كانت النزاهة الحكومية والرقابة المالية والمتابعة البرلمانية من جرائم نفط الشمال التي تجلت اليوم؟ فهناك تقصير واضح.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/81073" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-rK2baRKzXlZpzjZ5_SLbfE4oHm0DE1RxpHLExDncyRFut5SlYMKDcV4zt3hgC8P8SM-2Hq0t7gIK8Cy7fx4HuPlRnEa7_hugJdpUwIzUNmkcr4Yf7x5m_Z_ceozRb8uz6XHUnwvyeXfM3J7RvhgfE5_qQjkxD2W79-KXyoXooC1HUpw7kdf1em3a8smpf0BebHVrMM4AMOKwkoUZwhmHpSI_dOF-aZk0XJ1XwcxP3XUkjO8g4iL8f1g43Fh6ogmEIg75hTO-IUWPQWUmGVuwaeqfqBPJWxJehV2eUnSP_oTZQPOyQ9mZW5jNpO2luSMXOUymwu17jK9wi0rKvz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارة الامريكية في بغداد تقول ان العراق يمتلك امكانيات هائلة وشركاتنا هي من ستطلق عنان هذه الامكانيات.
وبمعنى اخر العب لو اخرب الملعب</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/81072" target="_blank">📅 14:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81071">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
وزارة التعليم العالي والبحث العلمي العراقية توجه بوضع الإمكانات اللوجستية المتاحة لدى الوزارة وتشكيلاتها في خدمة جهود اللجنة العليا المشرفة على مراسم تشييع جثمان قائد الثورة.</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/81071" target="_blank">📅 14:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81070">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لحظة وصول جثمان قائد الثورة الشهيد لإقامة صلاة الجنازة.
#قوموا_لله</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/81070" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81069">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acfd2392b1.mp4?token=XN1_DENLQwK2SanUVlqB_JaCK6ZF20adrysDS_Vh-AlvwzqbRVKREjnEOj73opiJmrCJZgiCAheonTs5HBW8NA4cTggeyBaWQ7V27pkBEQxeLLcOI7mw7Yy9f58FpGVUaY6sYRWHxKgxLGOW-2EWf1aKt2jt4t_WxLshk_Cbx6XEqpMNvsi8LI9IT625tPeGqi7fMlA5n9xY8oNh8-eQZYRfYA5YF_adF32_vN7vG3XWu_DruOXETYisP5AiwQeOuPRWZrifmQeVQS5-UyKOKZ6QVsdQMnWKklW2uHMzYfwysdcZMmidIwa6Z1OyYFVz_ROaGCahUTQcwcXm-cGf0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acfd2392b1.mp4?token=XN1_DENLQwK2SanUVlqB_JaCK6ZF20adrysDS_Vh-AlvwzqbRVKREjnEOj73opiJmrCJZgiCAheonTs5HBW8NA4cTggeyBaWQ7V27pkBEQxeLLcOI7mw7Yy9f58FpGVUaY6sYRWHxKgxLGOW-2EWf1aKt2jt4t_WxLshk_Cbx6XEqpMNvsi8LI9IT625tPeGqi7fMlA5n9xY8oNh8-eQZYRfYA5YF_adF32_vN7vG3XWu_DruOXETYisP5AiwQeOuPRWZrifmQeVQS5-UyKOKZ6QVsdQMnWKklW2uHMzYfwysdcZMmidIwa6Z1OyYFVz_ROaGCahUTQcwcXm-cGf0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران الجيش يواصل التحليق فوق مواقع يختبئ بها عناصر تنظيم داعش في محافظة كركوك بعد سلسلة غارات جوية على خلفية استشهاد عنصر من جهاز مكافحة الارهاب</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81069" target="_blank">📅 14:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81068">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
مقتل عدد من عناصر عصابات داعsh الإرهابية خلال الضربات الجوية للطيران العراقي في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/81068" target="_blank">📅 14:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81067">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQssJSbWlyTfEoL1Znzswq1FhUhlBjTIzYKApr2JLlkJoXZ8EW2_muRv3GTBDmizyi1ISDW0LQHFGg4jDtiqYEMKnLvIl8YqJJNmN_9Wvceb8vlvXX6XhAB07bkRhK28eMeHHX8TCkFHFIUgQrOmluHNaYm3Oh3e9NfyNxJ9XU_7RxArUIhEqRTegErok2hLBlhjEh1kjV_VY7NAKnyD13ku9di2p-bK03beMabREYRv5t89GE9FUkbZ7X6V2g3TvL08uArT2ly3pgZblVEMjE8CY9Q4qveB39a3FWQHquzpIxgwgtnZ_arEaI6m73o0R9OmRoQUcUa79c0wEYRAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قاليباف:
اليوم، شهد الشعب الإيراني الإسلامي الأبيّ الذي لا يُقهر، بصوت واحد، لإمامه المجاهد الشهيد قائلاً:
«اللهم إنا لا نعلم منه إلا خيرًا».
ثم نهض الجميع صفًا واحدًا، وهتفوا من أعماق قلوبهم:
«يا لثارات الحسين (عليه السلام)».</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/81067" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81066">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔻
‏الدول الـ7 في أوبك+ تقرر زيادة إنتاج النفط 188 ألف برميل يوميا في أغسطس.</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/naya_foriraq/81066" target="_blank">📅 13:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUb5uq3VKpfld7bdOA8gyfSYVYsslHRBF9oFrTTy2y_EQyUIv8J6-LqFzSiHbU2dZ3KVMQIA6bUj3IsHzhS56750oTlaRl2lnTEqY3HJAe-8vxjFlc8jxO3xU1jO23YdkIWt1PpS28MjhLwlbelOAEMB3ghjl1MEWTFuGwhnFTH5unN4SUbE7VKHui6FZ_3ZwDfr0eERzw2qzxfDL1rciUfUtPBUWd9RuxP3J1S41obyUnAE3cIZwAjvxllOH4-ttfQVIGicKr244N0bHr3X_VTwy8KbhI8edjrlxWPkvfDNtfGj4cAm4PFwyLK8nD6Rfw_AkRPbEEMgCLNyeXbYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المجلس الأعلى للأمن القومي الإيراني:
راقبوا إيران خلال هذه الأيام القليلة.
هذه هي إيران التي ظننتُم أنكم تستطيعون إضعافها في غضون أيام قليلة!
هذا البحر المتدفق من الجموع، يرفع الآن شعارين خلال مراسم الوداع والتشييع لقائدهم: المقاومة في وجه الأعداء والانتقام لدم القائد الشهيد لإيران.</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/81065" target="_blank">📅 13:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81064">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالقناة الاعلامية المركزية لتشييع الإمام الخامنئي في العراق</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨روابط_المنصّات_الرسميّة_للجنة_الإعلاميّة⁩_2.pdf</div>
  <div class="tg-doc-extra">172 KB</div>
</div>
<a href="https://t.me/naya_foriraq/81064" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">جمهورنا الكريم..
نضع بين أيديكم روابط المنصات الإعلامية الرسمية المعتمدة من قبل اللجنة الإعلامية العليا لمراسم التشييع لمتابعة التغطية والبيانات والمستجدات أولًا بأول</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/81064" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81063">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a75ce7c26.mp4?token=B0sNF29GlGcFLH8ThwxBZbdQVAUKaTYklu23ky-QTT2SehIF2yEV87qraUVgQAtns0sYEBNUqZ77jsN6ZCaQxvBij_ifAz9v45JDCED_6znF9XTcHbo0OR44k6tvoUkpM1dK9berwRLvBgdlME3mGuUeiqbo-ZNga0KnTomRpxbpeLZUU4TekN_ATIGtstOFwEdw8Z2pAU1Nx15uugBPbUhjHO4vFytBUSONidCReIPe5JtNo9jOgZncOSObZgjOisptdBwY9OowGyzECRZdWnv1we07ZuAIvn3WndsxmJeu-jpmXYaLnzHj7BbDZAbxwHNCZZqnqGA_5Cn2m7B87g10z_wYLkQBw8qx2pWCClAkKvd-dEFkK2xlzLZLfbNQV2OVdBvHaPQWBJ0ovGBo3JYbBH8oDDZyPzfU7vtkGsni5jozKaYKOkeEitipISvEPydeH14BJLw9JubaGgEsKfaWJkJvuRMzz93cGD4k7nr8uBLNo4gso3d4hSskCmiwaxEJNJvWbiBnbobKRYGkFLS2rKAtyQjKv05DKrtybhgj2QS3c6dXE6yI56LxwriN7RBhkQoyzC91dH19SB8U-pS2tQXfVb6cQ_DacTkVMklR5OhlgtU0v_nE1z2uftf19SZN7vDrhNxQzmuOT115GhEnDzquUzZif-KZMEofPNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a75ce7c26.mp4?token=B0sNF29GlGcFLH8ThwxBZbdQVAUKaTYklu23ky-QTT2SehIF2yEV87qraUVgQAtns0sYEBNUqZ77jsN6ZCaQxvBij_ifAz9v45JDCED_6znF9XTcHbo0OR44k6tvoUkpM1dK9berwRLvBgdlME3mGuUeiqbo-ZNga0KnTomRpxbpeLZUU4TekN_ATIGtstOFwEdw8Z2pAU1Nx15uugBPbUhjHO4vFytBUSONidCReIPe5JtNo9jOgZncOSObZgjOisptdBwY9OowGyzECRZdWnv1we07ZuAIvn3WndsxmJeu-jpmXYaLnzHj7BbDZAbxwHNCZZqnqGA_5Cn2m7B87g10z_wYLkQBw8qx2pWCClAkKvd-dEFkK2xlzLZLfbNQV2OVdBvHaPQWBJ0ovGBo3JYbBH8oDDZyPzfU7vtkGsni5jozKaYKOkeEitipISvEPydeH14BJLw9JubaGgEsKfaWJkJvuRMzz93cGD4k7nr8uBLNo4gso3d4hSskCmiwaxEJNJvWbiBnbobKRYGkFLS2rKAtyQjKv05DKrtybhgj2QS3c6dXE6yI56LxwriN7RBhkQoyzC91dH19SB8U-pS2tQXfVb6cQ_DacTkVMklR5OhlgtU0v_nE1z2uftf19SZN7vDrhNxQzmuOT115GhEnDzquUzZif-KZMEofPNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات مسلحة إضافية تنتشر عند مداخل قضاء خبات وبالقرب من منزل خورشيد الهركي بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81063" target="_blank">📅 12:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81062">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
الإعلام الأمريكي:
حادث إطلاق نار في نيويورك خلال احتفالات عيد الاستقلال الأمريكي، أسفر عن إصابة ما لا يقل عن 8 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/81062" target="_blank">📅 12:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81058">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bq8KsDhL5CJ9SeHr9Lo1YhkZTw29JGOLdnyTV8Tcvj-xSktjyEO80t2GO-DRZ0gAMM1E3TCkLrl2HHzCWOyrwVSLjSmPld0yqPBhVzNIuI6OKpH8wxX3nLgbEUSJGa-FmQdtsSElhOQamKnWgPIdt05oy1Ap_TAAvnvc8ZUkcdOCGP7rcR0oTdBmiQ_XvyJjqAVn7erLE46K74DRs5SLpvWwVL8sKee2W6kZJ5monEDEwVxNdntBVtz7MaaODDWbJ0XBOTKbxttvHyEr2L6c3yUoeNh3IBYMV7Fw4AZH6wVAZne5j5WuOaWd1LWZ86W2Yiypl3vJDpV3WNPcY7kELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvUDubqCL0U-9zpWyy296fTn7zyJ3m5YW1T6dXja0dDEed3_Fa88gKcCIPCGwC3pwp6EVxgS2UCi7p7jnJKcn7fiKM5vs7_zfI8ps-ybxdSg6CTl0nP5tHJq6TMqNH5cL2dpp5-h7gDQJHlphoy_4qYVM131t9oOP3bEtmqt9D4lDC6pvj8TQu-fRZkbYVmWlO0UdWtbDFQcoCviN0hziN_xPNrCFhGqPZY5fkLpTw-nb-6C6CMFVzce0-CpXEGNrDWEe79z7ZYg4-cBSeSmjUbeo9o-BFQbGwFB9PFehTrnrIHNeR9syxsaBc2gkZz0taHEHkjACXIrwxoVWq43yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cawCP44W73VZxQ1V2wLM1OX15b5DZsClRbcypWduEO7SXKvgSwYcc94FKKGF4b7IRoWAOO1nztd7T-rJPGyV6HbuKpVgjDq51kfUZvOQc3pWSQyrMNveiCS8h20blVZd6je-C17dpdWrChb4qcqawY1SHSBI_dyoa-8I7z1b0Zaxu8SCYFCNSb-VtW1YtB0meGrkHav6rSAUCxha3feFtAIG808LaPE0xv__69OV2Cm8uOjhfNAjh7KQaybaT48CfjYRQwONMkpYPNbKcLYfW3fGljT3YuDVL-3J33mkRf1oEIfroo1wj_lA97FgtR61os8CghWnMBbDHqaQrSZuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kticemf4C1YOfloNTwxWt0A3O47kTHlLRInm3jbos_M6vvKYwa-PhOolpn_PmrSABd7vjNr6_1EOUUmT7qyDzxonThDKxcCvOBIDsgLXWQhSr21exUmUVVr_GpXyAryNCoKysmne722SnVyEP02yohnCFg2oMw277WYZwdTBDf8NvgI2ureK3Dy92pfdGUJdtAo1oyircIltADGxQkuIdeDiQ9vADybUdS1Jze1W0u_e-OFEyzHKSGtMQtRxkJL_qbQCyzMj-SEMiuUN3D4LWGsvtKeemNPlVvKdmiaEvyJmaMroPCEXY389LH175YDCv4AoQqCTNWJ4M3DxE5ex6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
أضرار كبيرة في منزل "خورشيد هركي" بعد إقتحامه من قبل مسلحين تابعين لحزب الديمقراطي الكردستاني خلال عملية إقتاله وعدد من أبناء عشيرته بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81058" target="_blank">📅 12:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81057">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVpfxCzXw1_YLV8sxoPioVdXyLnm8_uR76eSISaAusXtrl0VRslBk7vq9CQwW0esZBUG5anUWKuLVfDmn0UfR5pBF6a3a8ZnHuC43w5PiLZoITaz_PLgYg82u71TgBEUMgrJNXLfdvZirnr2UNmGdKvueEOvXI-aTNPH6dkL7KNr2yH9MztzH8dByYvvpAmE9W4YdUvPeXpu89J0DeOqhYL3UGjG0MMlDmSkR-LBmnQUaAB8aNXnDOLl99_DzF7gyGN2BN2MDBmIkugpsc1Hlgt_YNDv4oYm-OUg-uM4zu9RbWSdKUzSGGQLyB8SsMa2PbYZq5Whm7WNgHQL7vWyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم على سفينة قبالة سواحل الحديدة في اليمن</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/81057" target="_blank">📅 12:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81056">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوي انفجار قبالة سواحل ميناء الحديدة في اليمن</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/81056" target="_blank">📅 12:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81055">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوي انفجار قبالة سواحل ميناء الحديدة في اليمن</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/81055" target="_blank">📅 12:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81054">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
جهاز مكافحة الإرهاب: استشهاد المقاتل الشهيد الملازم اول (حسن خضير زغير) الذي نال شرف الشهادة دفاعا عن وطننا الغالي اثناء الاشتباكات مع عصابات داعsh الارهابي في محافظة كركوك.</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/81054" target="_blank">📅 12:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81053">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
عقب إستشهاد منتسب في القوات الأمنية.. الطيران الحربي العراقي يقصف مضافات لعصابات داعsh الإرهابية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81053" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81052">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82316eee4.mp4?token=medfkbI_MmtewGbvxt_4rGpz2kfkoxj7uEoOqlmGcKjsjDs9mop79yUyPo3f2HkKY-dFD1lRX9bTYx2Vit1rvBeyJmTMkhMR4eiCjIMLjxxyL_c6bxqMA-rtx_a03JOzGx_KvaQTUJs8IbVk63MVizuZOT1gHA_Uw4IeG2gViGbzIQOVFZ7BQ1ghUPzyivM9qFrJw3DPWZ1doiVY-s-NR5bwU_QikuyTXmDnBSpEiIuujlC1jhNdSlvzOZT3BTk_czvFcyWlZtHE7hkjlYYbipAPNQGcXPI0GjJWUorAN-A9-ZxvBGxB_DvHrxQFKsGE9A6HBBRpI5g52R9Vy37R9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82316eee4.mp4?token=medfkbI_MmtewGbvxt_4rGpz2kfkoxj7uEoOqlmGcKjsjDs9mop79yUyPo3f2HkKY-dFD1lRX9bTYx2Vit1rvBeyJmTMkhMR4eiCjIMLjxxyL_c6bxqMA-rtx_a03JOzGx_KvaQTUJs8IbVk63MVizuZOT1gHA_Uw4IeG2gViGbzIQOVFZ7BQ1ghUPzyivM9qFrJw3DPWZ1doiVY-s-NR5bwU_QikuyTXmDnBSpEiIuujlC1jhNdSlvzOZT3BTk_czvFcyWlZtHE7hkjlYYbipAPNQGcXPI0GjJWUorAN-A9-ZxvBGxB_DvHrxQFKsGE9A6HBBRpI5g52R9Vy37R9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عقب إستشهاد منتسب في القوات الأمنية..
الطيران الحربي العراقي يقصف مضافات لعصابات داعsh الإرهابية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81052" target="_blank">📅 12:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81051">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
زلزال قوي يضرب مقاطعة بستك في غرب محافظة هرمزكان جنوبي إيران.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81051" target="_blank">📅 11:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81050">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌟
أماكن وتفاصيل وسائل النقل المجانية لنقل مُشيعي الإمام الخامنئي من جميع المحافظات إلى النجف الأشرف وكربلاء المقدسة:
محافظة بغداد:
- النهروان
الحجز والاستفسار: 07813838567
- الشعلة – الرحمانية
للتواصل: 07709248650
-الشعب – الحسينية – بوب الشام
الحجز والاستفسار: 07727114505
- بغداد الجديدة – الأمين – المشتل – العبيدي – النهروان – الكرغولية
التسجيل والاستفسار: 07737264563
- الزعفرانية
مكان الانطلاق: قرب جامع الصدرين، مقابل حلويات الحمداني.
موعد الانطلاق: الأربعاء الساعة 10:00 صباحًا.
الوجهة: كربلاء المقدسة.
المتكفل: محمد العسكري.
---
محافظة البصرة:
- قطارات سكك حديد العراق
مكان الانطلاق: محطة قطارات البصرة.
الوجهة: كربلاء المقدسة.
موعد الانطلاق: الثلاثاء 7/7/2026 الساعة 8:30 مساءً.
المتكفل: رضا محمد الهاشمي – مدير سكك المنطقة الجنوبية.
- مكتب النائب أبو تراب التميمي
نقل مجاني من البصرة إلى النجف الأشرف وكربلاء المقدسة.
للاستفسار:
07705500886
07832775556
- تجمع تقاطع المعارض – قرب سنتر مهدي
موعد التجمع: الثلاثاء الساعة 7:00 مساءً.
المتكفل: أبو كيان.
للتسجيل والاستفسار:
07725800010
07801401020
---
محافظة نينوى:
- مدينة الموصل
الحاج أبو رقية: 07740926267
- قضاء تلعفر
السيد بهاء الموسوي: 07718255424
- سهل نينوى
الحاج أبو فاضل: 07704863222
- الموصل – تلعفر
الحجز والاستفسار:
07502906786
07503253470
---
محافظة الديوانية:
- قضاء الحمزة الشرقي: 07853995550
- مدينة الديوانية
الحجز والاستفسار: 07830966317
- الديوانية – الشنافية – السدير – الحمزة
سيد علي: 07828989246
سيد علاء: 07811194705
---
محافظة ديالى:
- خانقين
الحاج أبو رضا: 07701909645
كاك كاروان: 07700921834
- مناطق مختلفة في ديالى
الحجز والاستفسار: 07737400051
---
محافظة المثنى:
منتظر/ 07825516717
كمال / 07822527997
جعفر / 07831445477
امير /  07815574897</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81050" target="_blank">📅 11:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81049">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
محافظة بابل تقرر تعطيل الدوام الرسمي يومي الأربعاء والخميس المقبلين بمناسبة تشييع السيد الشهيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81049" target="_blank">📅 11:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81048">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
سنرد بحزم وقوة على أي خطأ يرتكبه العدو.
نستفيد من فرصة وقف إطلاق النار لتعزيز قدراتنا القتالية ولا نضيع لحظة في سبيل ذلك.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81048" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81047">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3893914609.mp4?token=kP5CKOz1C9nvlNsmMwRVRbVSsHBIkRU6TLBk8rgeSNGwz27lJ4Zn6F7F3oBtLjfvg-TjJqwq9Wm4mVADf3H7898jgMQg_3EwK9hpa6uziCxghlWFFkm3sLvHSYEwaohoIdqurLlM-ZYsQvtI7rUW2Cr4wE9miiDMCdzfaEkbH1xlTlW_GeFgmO-GeFJz-drfTrAEhDQaEmpIlf-FMWn63oi3iRmiaQbzKX2gMxotWyGBTggtOJVFhO56H_UQXYrDLkbKt3nXkijy9mFSqm19rtPsO4_ciVbx6hEkVdrTIF56-nQgZ-1kikEsg6jds6JIrAkcT-Q00liKrWCMuwvmM5uM_lyZwSFN9ooJwtsw5-OcEieTRyGiB7-vvtixevGbZqptyCprqHpfAFs80MHj8bZUYVGbYN9gDFZXe-PQSEbUi-ydmZ_clNYm1gsTzne_i8YX_3HfxEPryy8Mn0inMrwBFWXmHhYlrMIZmYfJ_HbwDUCrVuQkLiKZfdYUnQbzRry-vWhGIW7V1kQdcBVU1DT2AruNis-wu_C7zkbpaSfAJNCzmXtxs9Z0ycJTxyzhTVgI9LUy-kn-OFp3l2BAC9MIJe2lvrO_0DSNQSvUg_k5kQ5dSiPBioqaDhup7C0w5E1jg5g_HUFCvvhEx70TZmF3-qgDakOoEEPBBwDO0Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3893914609.mp4?token=kP5CKOz1C9nvlNsmMwRVRbVSsHBIkRU6TLBk8rgeSNGwz27lJ4Zn6F7F3oBtLjfvg-TjJqwq9Wm4mVADf3H7898jgMQg_3EwK9hpa6uziCxghlWFFkm3sLvHSYEwaohoIdqurLlM-ZYsQvtI7rUW2Cr4wE9miiDMCdzfaEkbH1xlTlW_GeFgmO-GeFJz-drfTrAEhDQaEmpIlf-FMWn63oi3iRmiaQbzKX2gMxotWyGBTggtOJVFhO56H_UQXYrDLkbKt3nXkijy9mFSqm19rtPsO4_ciVbx6hEkVdrTIF56-nQgZ-1kikEsg6jds6JIrAkcT-Q00liKrWCMuwvmM5uM_lyZwSFN9ooJwtsw5-OcEieTRyGiB7-vvtixevGbZqptyCprqHpfAFs80MHj8bZUYVGbYN9gDFZXe-PQSEbUi-ydmZ_clNYm1gsTzne_i8YX_3HfxEPryy8Mn0inMrwBFWXmHhYlrMIZmYfJ_HbwDUCrVuQkLiKZfdYUnQbzRry-vWhGIW7V1kQdcBVU1DT2AruNis-wu_C7zkbpaSfAJNCzmXtxs9Z0ycJTxyzhTVgI9LUy-kn-OFp3l2BAC9MIJe2lvrO_0DSNQSvUg_k5kQ5dSiPBioqaDhup7C0w5E1jg5g_HUFCvvhEx70TZmF3-qgDakOoEEPBBwDO0Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
لحظة وصول القوات التابعة لحزب الديمقراطي الكردستاني والتي اعتقلت خورشيد هركي وشقيقه وعدد أخر من أبناء عشيرته في قضاء خبات بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81047" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81046">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d0ed1436.mp4?token=pNo-3_MmNeIGhl5_bILoH3Y0gSFEDeWpP6eSWfl1Dutg9P_YPYhELh5JouExzBuYBKGQDlMzaqz9cpHJyjPXXKCkFBuD8PQ4u-Y2_uiDTQYECgyH4dWsTZevOZJEL4ouax1QGbYZPcl1698XAcW0ds_1J9QjrMvA7RfJbFfoJejb0V78Wsj5hnOAlPnVWPrmt2pFAHD6tj07dcMXkbmDMfEp-oOjgL9aXeyWHcpBW7PPvd1RXRv-SnZMZXwB0K5YrmHzj6Uv0OBAs_fE2KSkSf2O8_oMc95TDazOBfGbvNfre7tevwzJU_vfRFCeUDIi8UZmkW-dmPvs4Jk3KbyFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d0ed1436.mp4?token=pNo-3_MmNeIGhl5_bILoH3Y0gSFEDeWpP6eSWfl1Dutg9P_YPYhELh5JouExzBuYBKGQDlMzaqz9cpHJyjPXXKCkFBuD8PQ4u-Y2_uiDTQYECgyH4dWsTZevOZJEL4ouax1QGbYZPcl1698XAcW0ds_1J9QjrMvA7RfJbFfoJejb0V78Wsj5hnOAlPnVWPrmt2pFAHD6tj07dcMXkbmDMfEp-oOjgL9aXeyWHcpBW7PPvd1RXRv-SnZMZXwB0K5YrmHzj6Uv0OBAs_fE2KSkSf2O8_oMc95TDazOBfGbvNfre7tevwzJU_vfRFCeUDIi8UZmkW-dmPvs4Jk3KbyFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد ساعات من انتهاء صلاة الجنازة على جثمان الإمام الشهيد، لا تزال الحشود الغفيرة تتوافد إلى مصلى الإمام الخميني لتوديع قائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81046" target="_blank">📅 10:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81045">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dcfb8b54c.mp4?token=uOT3tHpM8MxAHtivaYSoyB8rNAnMR9Y1rtuQr4trVYkjNTj0l1McLIohEM61ybGAEt1eHEDEt9R6S82nOXhknA1QgozoO1KeW-Xfx3GqVT4cuqDfh6enWSIxxII_LQZAMDNIYjHP4WWLlAQAURzj5j_4fWNxv4f1-jhZjR21sCiSjxKvVsEd4E1eeSYJ_moOqMlWDBkmU-o3d99yJo73ftkOUrgLZz_0ZiFdKXFApE15o-Q_J-Var5Us-nuLPFc_nZdyoqZDjpwqdNgrZ-wuuXw8oSqKZGl1fgxP7URLHXNkoAkv1I-vvhwKPQ3x0PYWtUhKlJ141Xqn5K6yJotugA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dcfb8b54c.mp4?token=uOT3tHpM8MxAHtivaYSoyB8rNAnMR9Y1rtuQr4trVYkjNTj0l1McLIohEM61ybGAEt1eHEDEt9R6S82nOXhknA1QgozoO1KeW-Xfx3GqVT4cuqDfh6enWSIxxII_LQZAMDNIYjHP4WWLlAQAURzj5j_4fWNxv4f1-jhZjR21sCiSjxKvVsEd4E1eeSYJ_moOqMlWDBkmU-o3d99yJo73ftkOUrgLZz_0ZiFdKXFApE15o-Q_J-Var5Us-nuLPFc_nZdyoqZDjpwqdNgrZ-wuuXw8oSqKZGl1fgxP7URLHXNkoAkv1I-vvhwKPQ3x0PYWtUhKlJ141Xqn5K6yJotugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هكذا استُقبِل القائد العام للحرس الثوري اللواء "أحمد وحيدي" من قبل الحشود الحاضرة في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81045" target="_blank">📅 10:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81044">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ce08a411.mp4?token=KOYjTxjc2SojGDmVVGeGaSF9yn5TMSMGgwf8mulM6wktOvOctP6ItTBXPQLVonVbZ-oiXrdsLsaqPK3RnnjUu50RDYy1fI_CxvsRGWNVsJQOHrfuBJhJD9WfW4pT225eVxcFAxeB6MRYZFn1iHYYBOecgyRQ3C2ddkh6X3nsixMyeRV4l9V527fK5-ngtsdshWBmI_JL9oFEt6ngdJp-sTpLj6O4T8lhmT_SLEBcezF2inUcYj0StYG9uMwOYxK0StPgltxyetPOFOejN2YUOZN_JOc5cjCdgp7h7ec8YeXtWwyqBl4PDIgn_9oBbBuzbahO8n0Oi30PWCLsE-riSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ce08a411.mp4?token=KOYjTxjc2SojGDmVVGeGaSF9yn5TMSMGgwf8mulM6wktOvOctP6ItTBXPQLVonVbZ-oiXrdsLsaqPK3RnnjUu50RDYy1fI_CxvsRGWNVsJQOHrfuBJhJD9WfW4pT225eVxcFAxeB6MRYZFn1iHYYBOecgyRQ3C2ddkh6X3nsixMyeRV4l9V527fK5-ngtsdshWBmI_JL9oFEt6ngdJp-sTpLj6O4T8lhmT_SLEBcezF2inUcYj0StYG9uMwOYxK0StPgltxyetPOFOejN2YUOZN_JOc5cjCdgp7h7ec8YeXtWwyqBl4PDIgn_9oBbBuzbahO8n0Oi30PWCLsE-riSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
عشيرة الهركي تعلن الإستنفار والتوجه نحو منزل خورشيد الهركي في قضاء خبات بمحافظة أربيل، عقب إعتقاله من قبل قوات تابعة لحزب الديمقراطي الكردستاني.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81044" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81043">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اللواء وحيدي في صفوف المصلين على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/81043" target="_blank">📅 10:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81042">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197834fec.mp4?token=NQHkcIt_PUbcF-R2bZsen9rv3wwVhmPimY12GSQ0cNMcWweJoDD9ziZr4s7SDWjmmkxwWAiPzp8Dk1brYFDcpO-bXMuNB_-LPvOeGTB61C04VLIurdYw1fY1UYPHGNfDLcCoHH6qGIwoGFTQ1KBlSWH2CLS8k0XLVeCGOkOzpAH0Odhuu_LFu_JanPh2gwHeu2Kka3qFCAIRnbehvf30eCASzXHDlDyjysxC8IKy0GjXYpwTKuyWLIqWyb8m-WUQ74hQ--4OieeM_WZ0wXLNH5TRthQrplqHKcRU69yHbceOTHXebgfmlZ_493jsSX2GKzclv6fiZDtTSVUxJlLdAiJsODk5HfUw-8Prov9fe1NnmTZpijkaU-6PWAxU4-lsdLUdZWPDic7HpjcX7kwMRAo07VeCYCRGWxIhURU70THuXk7gBoV43B5dmCBJY377UBYFLOj8PPgUR9qaCmdsg2yCKkm6pOYK7Agu5mSBoirv9qCS6Bh0jAVQkcOKhYTIp2z3oxzePTj-bnEWpjzP579J5kyAIPy_l0-7UCuMWOmJpVNwcIEm_RfH4H2Haf-T3W_qsgFS65xBlxnw9Z3bA7aq-Al5Jtl_yrG6s1u-8qSVjAAZGWgsCWjRjmYiaJhN_ijHNssHFrPflJ4fMcq0q-axS08KhJlG22astb1pu0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197834fec.mp4?token=NQHkcIt_PUbcF-R2bZsen9rv3wwVhmPimY12GSQ0cNMcWweJoDD9ziZr4s7SDWjmmkxwWAiPzp8Dk1brYFDcpO-bXMuNB_-LPvOeGTB61C04VLIurdYw1fY1UYPHGNfDLcCoHH6qGIwoGFTQ1KBlSWH2CLS8k0XLVeCGOkOzpAH0Odhuu_LFu_JanPh2gwHeu2Kka3qFCAIRnbehvf30eCASzXHDlDyjysxC8IKy0GjXYpwTKuyWLIqWyb8m-WUQ74hQ--4OieeM_WZ0wXLNH5TRthQrplqHKcRU69yHbceOTHXebgfmlZ_493jsSX2GKzclv6fiZDtTSVUxJlLdAiJsODk5HfUw-8Prov9fe1NnmTZpijkaU-6PWAxU4-lsdLUdZWPDic7HpjcX7kwMRAo07VeCYCRGWxIhURU70THuXk7gBoV43B5dmCBJY377UBYFLOj8PPgUR9qaCmdsg2yCKkm6pOYK7Agu5mSBoirv9qCS6Bh0jAVQkcOKhYTIp2z3oxzePTj-bnEWpjzP579J5kyAIPy_l0-7UCuMWOmJpVNwcIEm_RfH4H2Haf-T3W_qsgFS65xBlxnw9Z3bA7aq-Al5Jtl_yrG6s1u-8qSVjAAZGWgsCWjRjmYiaJhN_ijHNssHFrPflJ4fMcq0q-axS08KhJlG22astb1pu0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصلى الإمام الخميني بعد إقامة صلاة الجنازة على الجثمان الطاهر لقائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81042" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81041">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قوات مسلحة تابعة لحزب الديمقراطي الكردستاني التابع بمسعود بارزاني تحيط بمنازل عشيرة الهركي في محافظة أربيل</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81041" target="_blank">📅 09:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81040">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انتشار كبير لمكافحة إرهاب إقليم كردستان في محيط منزل خورشيد الهركي بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81040" target="_blank">📅 09:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81039">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قوات تابعة مكافحة إرهاب كردستان العراق تعتقل عدد من أبناء عشيرة الهركي في محافظة أربيل.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81039" target="_blank">📅 08:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81038">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/naya_foriraq/81038" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81037">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81037" target="_blank">📅 08:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81036">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a710a25bde.mp4?token=In7Ykcug0Y_CYCMlsakhg1UmyDDLEYcM_cB_XHg1X1qygWfn5lhC-nrEVbA5_5B9b9Pt8YtMjSws2yBqVrGP1k5_JI2CT94BP6VIsLazoz-Na1ZgzH4WBFoRRtDOprDbPOKqW5ml5F05c_x4vL2taNLyvzfvlyMH4BlT72Zk4fmxrme2VROpQ6kxwI39-5k_QwRBzvFdtc7NLQd2_1cPsmK3zFxXj9zxDdZxONj0hFOiRzTMpso5XykUohb9CVYn5H0JUeXSkMk3tDMRQAfMigesy2YXSRhzw2XgVzVnYbiBA16vHIKC66QEdBENm75NJCaXfCCEbB0Vhw4bE59Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a710a25bde.mp4?token=In7Ykcug0Y_CYCMlsakhg1UmyDDLEYcM_cB_XHg1X1qygWfn5lhC-nrEVbA5_5B9b9Pt8YtMjSws2yBqVrGP1k5_JI2CT94BP6VIsLazoz-Na1ZgzH4WBFoRRtDOprDbPOKqW5ml5F05c_x4vL2taNLyvzfvlyMH4BlT72Zk4fmxrme2VROpQ6kxwI39-5k_QwRBzvFdtc7NLQd2_1cPsmK3zFxXj9zxDdZxONj0hFOiRzTMpso5XykUohb9CVYn5H0JUeXSkMk3tDMRQAfMigesy2YXSRhzw2XgVzVnYbiBA16vHIKC66QEdBENm75NJCaXfCCEbB0Vhw4bE59Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصلى الإمام الخميني بعد إقامة صلاة الجنازة على الجثمان الطاهر لقائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81036" target="_blank">📅 08:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81035">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9f781ff5.mp4?token=g8vObci7yTj9x8iTgKJKv5863J5JmImJOC_b2C2BYk8HQD1z12_Ma4CO90nDgdxH_jfMjQm3Z8B541gOVbFFBiJfGMdsmBDlnoH-FIu0gBDQ5FDY1574vE3_p0TFm6powmeAEkXNj1Pj9SUnbUEkzGUlhgK4Z4bK8ESbc_KMABAECEzgRRoQdDEPYx5i5c5aZtqnV0ePzdSN-JFXNkU_J-IQaeC5XXf7b3o4vn2wHEWJN74P-za1HLlRnTSprVuJkdw3Rva7XWqXWNQNUMO1L0_tJy8cVPfoN9FPTpLghXZ1I4b1svczY1HasJ4hRhZPE-_Eeh-_6zQ9BpRNxVRx4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9f781ff5.mp4?token=g8vObci7yTj9x8iTgKJKv5863J5JmImJOC_b2C2BYk8HQD1z12_Ma4CO90nDgdxH_jfMjQm3Z8B541gOVbFFBiJfGMdsmBDlnoH-FIu0gBDQ5FDY1574vE3_p0TFm6powmeAEkXNj1Pj9SUnbUEkzGUlhgK4Z4bK8ESbc_KMABAECEzgRRoQdDEPYx5i5c5aZtqnV0ePzdSN-JFXNkU_J-IQaeC5XXf7b3o4vn2wHEWJN74P-za1HLlRnTSprVuJkdw3Rva7XWqXWNQNUMO1L0_tJy8cVPfoN9FPTpLghXZ1I4b1svczY1HasJ4hRhZPE-_Eeh-_6zQ9BpRNxVRx4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای پسر فاطمه، تسلیت تسلیت.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81035" target="_blank">📅 08:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81034">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf4gYCIHda8ArRu3bGHfPS_o72RRVEj3g4cwt-HJhQvhHYAvMmEYHFK97zgcTRXpI693ZFNS65eyzvGF8vrTja5R2HzN3ddtKmLjSduM_2HmtI29zgEMg07wbtBCsFecdGdB2dn_yFErr10JNNN8DtP_uxQylfZwryn_WGu0jXs0X7J9AVoUrOP_gA_YCEiOz7aQNF83-GXRgZbizecCytJBKoBwhIhrrNma8f8oxFuQBhOeiVxSTRCblkgNjnEvm_gzIdp8XLqUJP3Rup-jcz22LTGUT1Y_4sEMzdQTXnw2somOatuRU10xJw0FnBhmbPwsAJ6DnnO_vZ2AD4KaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يالثارات الحسين</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81034" target="_blank">📅 08:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81033">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10526db91.mp4?token=bJHRpggm1fDkd_EEE2TJr0Gho7DQbX5Lp1Xx5eNLn1V0WsrMD8n36xPzTzunFePfd8AbMF-QMkPsw288-24ilZhLgEYBZVa4K8boHtvgGcgnxEM7K5Y3buvsdJS_aGixz2PDxLvERue0pidhdVw8CM3L8kMqER1l1kz6hFTiHgiPIJrHSsMkY0zuEAAtHzoKvkNAnrSrIAMgHL3Q7FFxgJJMtP1hKk8rj25iHwqzwFfptVYhCCFySctvL68vWFgU4ilVTxti8pVfh-wJcAWzJv9AaZxFhNFETI1YfgLJeQSt_MvXowKO7kDpMqTfiDGcpyU1q-jDlmUQlqxWp69hpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10526db91.mp4?token=bJHRpggm1fDkd_EEE2TJr0Gho7DQbX5Lp1Xx5eNLn1V0WsrMD8n36xPzTzunFePfd8AbMF-QMkPsw288-24ilZhLgEYBZVa4K8boHtvgGcgnxEM7K5Y3buvsdJS_aGixz2PDxLvERue0pidhdVw8CM3L8kMqER1l1kz6hFTiHgiPIJrHSsMkY0zuEAAtHzoKvkNAnrSrIAMgHL3Q7FFxgJJMtP1hKk8rj25iHwqzwFfptVYhCCFySctvL68vWFgU4ilVTxti8pVfh-wJcAWzJv9AaZxFhNFETI1YfgLJeQSt_MvXowKO7kDpMqTfiDGcpyU1q-jDlmUQlqxWp69hpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللواء وحيدي في صفوف المصلين على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/81033" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81032">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مقطع فيديو كامل لإقامة صلاة الجنازة على جثمان الإمام المجاهد الشهيد، آية الله العظمى السيد علي الخامنئي، وذلك بواسطة آية الله جعفر سبحاني.</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/81032" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81031">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مقطع فيديو كامل لإقامة صلاة الجنازة على جثمان الإمام المجاهد الشهيد، آية الله العظمى السيد علي الخامنئي، وذلك بواسطة آية الله جعفر سبحاني.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/81031" target="_blank">📅 08:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81030">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2eeb37e5f.mp4?token=SmNtJwSmoS-QOpidlbz0IpraUIf9JN2h9fSqw2UD6waQoxdw5uaj71VATnDawuiQXDbApg46LwrvhZUlOZ0wC0d7DMrV4xxOWM3UgUYz9xOR0eQbW82E3SoLv3FqFwlT7dRd8KSXYe6iuNdI6yY-Xd54KzwfNOwTpYJ-1r-e8jL1wP05Z5JFZbiUPEpj3ae71EJ8ZoNdKye_Z56ip20_uIYMnXs_jPU9tHZhRCj-xInGdSFD_PMTn0_UK5pxKhp_RRcsNVMv_Eqjj8vhLA34sIFCo7vX87oYfluVAc1NfEwZTh0qouoz_gP5qVnt6CTFEqVAHeNpk8dk6ftVC2rYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2eeb37e5f.mp4?token=SmNtJwSmoS-QOpidlbz0IpraUIf9JN2h9fSqw2UD6waQoxdw5uaj71VATnDawuiQXDbApg46LwrvhZUlOZ0wC0d7DMrV4xxOWM3UgUYz9xOR0eQbW82E3SoLv3FqFwlT7dRd8KSXYe6iuNdI6yY-Xd54KzwfNOwTpYJ-1r-e8jL1wP05Z5JFZbiUPEpj3ae71EJ8ZoNdKye_Z56ip20_uIYMnXs_jPU9tHZhRCj-xInGdSFD_PMTn0_UK5pxKhp_RRcsNVMv_Eqjj8vhLA34sIFCo7vX87oYfluVAc1NfEwZTh0qouoz_gP5qVnt6CTFEqVAHeNpk8dk6ftVC2rYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتهاء الصلاة على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/81030" target="_blank">📅 08:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81029">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انتهاء الصلاة على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/81029" target="_blank">📅 08:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81028">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">أقامة الصلاة على جثمان حفيدة القائد الشهيد</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/81028" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81027">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df0b8e849c.mp4?token=Ic-ZCAWVVxImvTBLy-4XIeZKj9F280ac9mlEkL9aWRdopvmZIOWCsgGDhzBme9iOrylqsVJYTAOlZOr6wTh7vOJf_CJWn8Ecf4cFAOBfv6phf1AzCU_wm6Lv3Q9tH0JPEzWfQCzRGAWmLS7sdvHzz_Ik_0Lfh6STe3WNAblO-3hEqRbnokPxXASA6tJ_jOhGfiwb90aWs5SdQGRTWN6_HNt7AFCZq9bD3Y70XghuWu-AtGoMQN0g5Xr8sGovG7oLvZZ1MGGvj14SjyrmWAJiDAbZZV-oiMPIamCaLi3jLknNjvkWHbXC6x4pTJxROywI5iHaUp8gXDk_8MIbm9GkOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df0b8e849c.mp4?token=Ic-ZCAWVVxImvTBLy-4XIeZKj9F280ac9mlEkL9aWRdopvmZIOWCsgGDhzBme9iOrylqsVJYTAOlZOr6wTh7vOJf_CJWn8Ecf4cFAOBfv6phf1AzCU_wm6Lv3Q9tH0JPEzWfQCzRGAWmLS7sdvHzz_Ik_0Lfh6STe3WNAblO-3hEqRbnokPxXASA6tJ_jOhGfiwb90aWs5SdQGRTWN6_HNt7AFCZq9bD3Y70XghuWu-AtGoMQN0g5Xr8sGovG7oLvZZ1MGGvj14SjyrmWAJiDAbZZV-oiMPIamCaLi3jLknNjvkWHbXC6x4pTJxROywI5iHaUp8gXDk_8MIbm9GkOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أقامة الصلاة على جثمان حفيدة القائد الشهيد</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/81027" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81026">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6dc481a81.mp4?token=Gh5YkoopXC2msEz-3Ixkq086-uU5qdd7Al_LSnWlD69JkjPDCqbezSAkzek9g2Mumr_0fr6eOUcaoAjSAy-y6zcn_ClgSiz_RenWSWvjvrvT-UgjDSs2mRau1kEJ6vy1KPaHYjoxA1dd75M27EmvdVqjdhBprfwbpDoo-42OvwLv4_gAMgHs9JxnipCiUwiHV4xolr4Ou0KFU3zzMx78LePgzQfoeWXHyu35uJRnes4GiyXs6C7jTRJLUyZRIBUGwYUiTgGbebmgsCUKuvpwbJ_wC9A6_jm2ED19kIAWonvYQHTcwNlti1MtQ3SQMDP1hWF3qs35Tb-wMuLNpWl9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6dc481a81.mp4?token=Gh5YkoopXC2msEz-3Ixkq086-uU5qdd7Al_LSnWlD69JkjPDCqbezSAkzek9g2Mumr_0fr6eOUcaoAjSAy-y6zcn_ClgSiz_RenWSWvjvrvT-UgjDSs2mRau1kEJ6vy1KPaHYjoxA1dd75M27EmvdVqjdhBprfwbpDoo-42OvwLv4_gAMgHs9JxnipCiUwiHV4xolr4Ou0KFU3zzMx78LePgzQfoeWXHyu35uJRnes4GiyXs6C7jTRJLUyZRIBUGwYUiTgGbebmgsCUKuvpwbJ_wC9A6_jm2ED19kIAWonvYQHTcwNlti1MtQ3SQMDP1hWF3qs35Tb-wMuLNpWl9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أداء صلاة الجنازة على جثامين عائلة القائد الشهيد</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/81026" target="_blank">📅 08:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81025">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bac6feba4.mp4?token=VJEQQ0EuK59lVCAtk2WjO6MIvKyuhIzfgnfdhhVd1V4uTWLtUh7-f0UTfXXt6PUrrnc8XYo8CgZ0zp5vywiI8jVKuBDencLcng6QhK7U32aSHmtzrrSJHJDYgSVSr8YWiGKW_qrWjFQZ3CKbT7gOgKDxDJfYVbeY12L0wJBkj0LR2uk2M_nWWB_n9GufdjCp_uL1bJLC_XYgnw5W96oqmJFi0PpiPYUGh2A7jZdFPPts_o5Lm_eHmi6vPLH-dexs4SYZ4KoTonJVfXhUg6ifxADo-GV1m10Vcip6abOP5xf6ZPUlEOvGTY03BSIJW4ELxTTO6Vu4qJoTmONSiZceKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bac6feba4.mp4?token=VJEQQ0EuK59lVCAtk2WjO6MIvKyuhIzfgnfdhhVd1V4uTWLtUh7-f0UTfXXt6PUrrnc8XYo8CgZ0zp5vywiI8jVKuBDencLcng6QhK7U32aSHmtzrrSJHJDYgSVSr8YWiGKW_qrWjFQZ3CKbT7gOgKDxDJfYVbeY12L0wJBkj0LR2uk2M_nWWB_n9GufdjCp_uL1bJLC_XYgnw5W96oqmJFi0PpiPYUGh2A7jZdFPPts_o5Lm_eHmi6vPLH-dexs4SYZ4KoTonJVfXhUg6ifxADo-GV1m10Vcip6abOP5xf6ZPUlEOvGTY03BSIJW4ELxTTO6Vu4qJoTmONSiZceKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الآلاف يقيمون الصلاة على الجثامين الطاهرة في مصلى طهران</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/81025" target="_blank">📅 08:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81024">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc9uZ_Oyu8PKRHxn72uxHkFj6oOKX_NbWNP8dCy71JIUyF73g4uAP8PEJ7Vn89IV3ddHp-ThGc6OLH8Bc2V-WfRTCHU7ZZvfEwDgE37fkRsWax1VpUXkJ6eEnaVfVvwvs48qfEVCVY9RfaWih0nzzYdnPtSNSrcAfxvUAy2-10aDiDZU-GqWtzx5Kjw5YwyhdiBisVEvH_mdzjNn4kFMJkktdbf4BNtGMDVSqPGASY38DkO1fOXbNABtodroXzFPb4qDaIIolMcBSkahn0W3j2hOb6pY8rzMyiSR56ks5IdzOKQ0oWVRqJhQ5vZ6vvhT5F_oBs17K90gHKL5hw-ITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصلاة على جثامين شهداء عائلة الإمام الشهيد</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/81024" target="_blank">📅 08:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81023">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الصلاة على قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/81023" target="_blank">📅 08:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81022">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2b942b32.mp4?token=rrQZB2sXSXjqj56uzyLfBc2vgS_sbH-ezBisFJuyZ6-DU6AR4geuiHAqy76ZE-73CbJpMh78tuYQ0e5RkBfDaNEG2Bt9G2tbAVxQib4d3nbTMw8xNSYKWuobsz-TyQypm8VtuNBxNvK2uC96Cl23uYsg-0N6nbiGngUYhspPgmfNTDdvbWA-HV2KRXzO8-N2s6H0SwA1BXHZIMxDLI9ljO5nyEFLim7jBl9REx0pIMjP3HEJOAqRkzl1E6NTo2zN3Y7wxILcLvT_KaxkQgOnp1M6p92JqbyUyE-hkUIhCXs3aFuoIiiD_tet04ZI7n6lZsuybPlHRQX8FRhMutt31A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2b942b32.mp4?token=rrQZB2sXSXjqj56uzyLfBc2vgS_sbH-ezBisFJuyZ6-DU6AR4geuiHAqy76ZE-73CbJpMh78tuYQ0e5RkBfDaNEG2Bt9G2tbAVxQib4d3nbTMw8xNSYKWuobsz-TyQypm8VtuNBxNvK2uC96Cl23uYsg-0N6nbiGngUYhspPgmfNTDdvbWA-HV2KRXzO8-N2s6H0SwA1BXHZIMxDLI9ljO5nyEFLim7jBl9REx0pIMjP3HEJOAqRkzl1E6NTo2zN3Y7wxILcLvT_KaxkQgOnp1M6p92JqbyUyE-hkUIhCXs3aFuoIiiD_tet04ZI7n6lZsuybPlHRQX8FRhMutt31A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصلاة على قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/81022" target="_blank">📅 08:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81021">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466cfde4ec.mp4?token=U-4nTOD1MPTef4CFQMnARcx1SYmgfM_Fx5PqmI_6Kemu0XE7n1gB2Fe_nSQFUGdp89u9t7dJZf8Op6dAgklCUQEXd9TnYA_act6MOtS0yYjklWYG9hCAN1rDFoTvYhQvCfOLk6mxoWbHjGmofiBPCZbOlL560D4TnOt0P5FkddpIN4tU6DdRs2nzf7OI12jNwK2YTmAVlye2h0OcgWbT0mVBktmndLK-4kj_xNf5JgBt_5wwoD1KEm7z_gOlJAwU2vYNqSylGLQjXY5gGw_nESptLHMTpKi0CKS2Znfe91AVU48prjzY8zBFfNMSXom9EUEUWu3Tf1vzYC0xlaya9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466cfde4ec.mp4?token=U-4nTOD1MPTef4CFQMnARcx1SYmgfM_Fx5PqmI_6Kemu0XE7n1gB2Fe_nSQFUGdp89u9t7dJZf8Op6dAgklCUQEXd9TnYA_act6MOtS0yYjklWYG9hCAN1rDFoTvYhQvCfOLk6mxoWbHjGmofiBPCZbOlL560D4TnOt0P5FkddpIN4tU6DdRs2nzf7OI12jNwK2YTmAVlye2h0OcgWbT0mVBktmndLK-4kj_xNf5JgBt_5wwoD1KEm7z_gOlJAwU2vYNqSylGLQjXY5gGw_nESptLHMTpKi0CKS2Znfe91AVU48prjzY8zBFfNMSXom9EUEUWu3Tf1vzYC0xlaya9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الصلاة على جثمان الشهيد القائد</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/naya_foriraq/81021" target="_blank">📅 08:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81020">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0JxJ7RqvZ50V-eyGaxw_Z98cRgTdMhOUnjQuL9uUkZSfGsUecifR2wk4m5iQDp3GJ7UJDYa_Qx5rULQUxY5t_ylTCfAPeJK84RIxT349kiqG76_dIQkO-WhyIYsUIGFGek7qonGcJk07xV504pX99EvU-90uMYhzysfhI_SmtavPk6SXV6xUmWSrFOJ9H_3HpnsoqgMF64GmMvAVgO28qNhUA7UU_b6xx1e5x2cg7hB5aaVvIgStpd8gVNAcImVLZlNKMtu26oT1GF4fqZJQ_D5qTdo5AHOwYSfm7Gg5jsUhzdyhYhrFsrNyS7VFc9hfkgu6NQgHcL-2eqvju2tIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدء الصلاة على جثمان الإمام الشهيد</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/81020" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81019">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رفع نداء "الصلاة الصلاة" على جثمان الشهيد القائد</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/81019" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81018">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b29f1eb22.mp4?token=Q7LcdIo4Jr2jlbachFuxVPA420bvK5fsFzyZmcmUJ9yw7CuKsLWXQ5tJdgeiDx7nueCooWjDbkmq0bjIL-S3u3SUXnOaXGQ5vfNAyXP5zbHZ2seuiNpMhXzVAGV4A7SnTZtlLI_qOvbDnEZwT3wLg-mMLJLX9sIFb9J4AczyWoaeRc1NHTSp59v_XMLc02oVLrLv08u1gsA_CE8efn4G4vRw3IRXdKlE-87IXiC3R6aBbVW3UFkrZQfAUzpKO3a_GcmAseAhqQoWU5MVQ9gxLAg2ej6vlhHcH4fmvbsmxvhvDAts7rukKQ_85Ak5RXMY3MU6Wxu0RHVnhacKwxpW6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b29f1eb22.mp4?token=Q7LcdIo4Jr2jlbachFuxVPA420bvK5fsFzyZmcmUJ9yw7CuKsLWXQ5tJdgeiDx7nueCooWjDbkmq0bjIL-S3u3SUXnOaXGQ5vfNAyXP5zbHZ2seuiNpMhXzVAGV4A7SnTZtlLI_qOvbDnEZwT3wLg-mMLJLX9sIFb9J4AczyWoaeRc1NHTSp59v_XMLc02oVLrLv08u1gsA_CE8efn4G4vRw3IRXdKlE-87IXiC3R6aBbVW3UFkrZQfAUzpKO3a_GcmAseAhqQoWU5MVQ9gxLAg2ej6vlhHcH4fmvbsmxvhvDAts7rukKQ_85Ak5RXMY3MU6Wxu0RHVnhacKwxpW6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بأي ذنب قتلت</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/81018" target="_blank">📅 08:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81017">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">العلماء والقيادات الإيرانية حاضرة لإقامة الصلاة</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/naya_foriraq/81017" target="_blank">📅 07:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81016">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85d4a8db8.mp4?token=kMqatPIaoOv22HoUi37kIVzZuVSrMyFmkssaAKJX-FC2phnY3pTU9s0CZxaNh5KD6JKJlC2qHvF1OMom_30O7zTDn2w2Pz2JfLXVl7K7kkrhi1Sq96Dfo1BRjL2W_V4ZittXMh4v82euAw5t7YvxGrlyoK23Tdxs5RVLQzgumVO84pv3de6rh9pZnQG-LXHjsRj58LJbwXs5mJg1WpEH3JYnSOYgpwNa4SNtfypQwaTC4Yiv6-emoUkgvNuB151cWkZkCrzriQvIXF3HWNTR_VgZtEeqrIiYTVqnLmgQyLKkorBUalVQu04hrKsV4PgabyxqX5SdW_Jl_fXHk2uqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85d4a8db8.mp4?token=kMqatPIaoOv22HoUi37kIVzZuVSrMyFmkssaAKJX-FC2phnY3pTU9s0CZxaNh5KD6JKJlC2qHvF1OMom_30O7zTDn2w2Pz2JfLXVl7K7kkrhi1Sq96Dfo1BRjL2W_V4ZittXMh4v82euAw5t7YvxGrlyoK23Tdxs5RVLQzgumVO84pv3de6rh9pZnQG-LXHjsRj58LJbwXs5mJg1WpEH3JYnSOYgpwNa4SNtfypQwaTC4Yiv6-emoUkgvNuB151cWkZkCrzriQvIXF3HWNTR_VgZtEeqrIiYTVqnLmgQyLKkorBUalVQu04hrKsV4PgabyxqX5SdW_Jl_fXHk2uqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العلماء والقيادات الإيرانية حاضرة لإقامة الصلاة</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/naya_foriraq/81016" target="_blank">📅 07:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81015">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746ceaf248.mp4?token=NPVWWNecNe8zCp9HtmhLk-_4oYRmhU0YYHXDaVmdMA6hdlDrup6r-BBc-nJ3gIPyU1dLf5e7XeqWzPFbDb-QPrJhIIPO30hOokxtOmPOuaGNdFiruxb5oOlgtG_cXNwztWQECpgk5qyGxCCbvK32LVIuRwpE9lKnv1jAG2TO_zEpsIgnhQHyfL8PhInxxne4XJEHGtO7rMgSSy2nfmEb0NisU_l1GqJirddASAsA7Fl5mBspxuY9icfHrkpIowHusmGFgLlVlFi6kxh1FFzy1mI0U17Ce6m2zz3P0RxQQCPJiKxN22eqhUWEAJSVYCqVcFdxPseNsyIOqDKNQBUkGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746ceaf248.mp4?token=NPVWWNecNe8zCp9HtmhLk-_4oYRmhU0YYHXDaVmdMA6hdlDrup6r-BBc-nJ3gIPyU1dLf5e7XeqWzPFbDb-QPrJhIIPO30hOokxtOmPOuaGNdFiruxb5oOlgtG_cXNwztWQECpgk5qyGxCCbvK32LVIuRwpE9lKnv1jAG2TO_zEpsIgnhQHyfL8PhInxxne4XJEHGtO7rMgSSy2nfmEb0NisU_l1GqJirddASAsA7Fl5mBspxuY9icfHrkpIowHusmGFgLlVlFi6kxh1FFzy1mI0U17Ce6m2zz3P0RxQQCPJiKxN22eqhUWEAJSVYCqVcFdxPseNsyIOqDKNQBUkGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وصول أبناء قائد الثورة الشهيد والقيادات الإيرانية إلى مصلى الإمام الخميني لإقامة صلاة الجنازة على جثمان الإمام الخامنئي.</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/81015" target="_blank">📅 07:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81014">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e3bc9a09.mp4?token=KK0aiBy_o_dqGsEkVdzSNa-J6S8xocN5N-5vQeIRHQHQPcteIJK18gbMZkbcMYgqClNJBs-__pVelLKUtqVt67n_DIHnxfE97zhtaxNf6IYN_LDOs7TC1pQtGx3YnYrdjQfwzbhN0JbZph9EIOLdbah-D8zUN1u5NbhwliN2xWteMzwgXrfsleF3tJAd8GAXl6cPmnVFJv0uSZGC7nh-Oy0cSuY8wclxNeBPQsciVEv98EtBPo0YrulwY4iK3tPppDbFmTVMjGRcC8JTf5VOsmHmh7EO_DeTF0i2o1r6rRvomh0raxJzpdDWM5SpCce1pIwnbtsu8IZDodVOXWBKOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e3bc9a09.mp4?token=KK0aiBy_o_dqGsEkVdzSNa-J6S8xocN5N-5vQeIRHQHQPcteIJK18gbMZkbcMYgqClNJBs-__pVelLKUtqVt67n_DIHnxfE97zhtaxNf6IYN_LDOs7TC1pQtGx3YnYrdjQfwzbhN0JbZph9EIOLdbah-D8zUN1u5NbhwliN2xWteMzwgXrfsleF3tJAd8GAXl6cPmnVFJv0uSZGC7nh-Oy0cSuY8wclxNeBPQsciVEv98EtBPo0YrulwY4iK3tPppDbFmTVMjGRcC8JTf5VOsmHmh7EO_DeTF0i2o1r6rRvomh0raxJzpdDWM5SpCce1pIwnbtsu8IZDodVOXWBKOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رجال أبوجبريل يدخلون إلى مصلى الإمام الخميني في العاصمة طهران.</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/81014" target="_blank">📅 07:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81013">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cc6541ca.mp4?token=Wt_633Da42OXzgGFuI8zE9K_k13uee3n_IgkrQrXzwZJvhtmFXyNFM5qENqMwTWkH1QJhqg0Kk6NWkoeAl-8NGpJU-YfCKXu7FpDHhZYdB8FfgyXx9_RLijftPNkeInyAnmTHrMy6Y5G3mK5iJ2ucAf-PymF4V8e5K16S3kOOwEPzbXsGkDiGdYYV2V2o6NoNTudjuZc-j5xdG4tlwbfNt5LPY14uE53EUXIrK04uqBP2xmluhei3452c6KXAFxtag9w2d3qwKMfyKaWgK9oGs11vA3jybVy0ysGTOvfHafnWefPDNtST1bzw46ZPijnvKpebgbBW8ug0E_egR59mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cc6541ca.mp4?token=Wt_633Da42OXzgGFuI8zE9K_k13uee3n_IgkrQrXzwZJvhtmFXyNFM5qENqMwTWkH1QJhqg0Kk6NWkoeAl-8NGpJU-YfCKXu7FpDHhZYdB8FfgyXx9_RLijftPNkeInyAnmTHrMy6Y5G3mK5iJ2ucAf-PymF4V8e5K16S3kOOwEPzbXsGkDiGdYYV2V2o6NoNTudjuZc-j5xdG4tlwbfNt5LPY14uE53EUXIrK04uqBP2xmluhei3452c6KXAFxtag9w2d3qwKMfyKaWgK9oGs11vA3jybVy0ysGTOvfHafnWefPDNtST1bzw46ZPijnvKpebgbBW8ug0E_egR59mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عزف النشيد الوطني الإيراني في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/81013" target="_blank">📅 07:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81012">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62994becf.mp4?token=octFfi7WEZj4MfoNf0gUfvmJnbEOE3nWB9HSL_Q6JBR288aFl0HKVQUx1-Dd_pCYMvilxbMMtMV06fP0H_PpdzG3cZXmauDzIcXANO0bBpdXW49wGS7vqwRReo07Igo0Yz0sB7BkG62jmBaqARlxSoEGpOOZp3cvPw7YwoIN6G1fXzV03sz1p5FgiklFuprp-WON4azT4psrt61WsKdljF06d4WvEByjb5JYwowISg2wcQMKkLrUlNqCaOVz8WLWEp5C41lDnNEN9dAA9z8RVYggQwGh-mHC0BC7XlTJlsdUj1F9z8wRycSxEl8AjhO_FIGFUbBchlffNWVc6V1gV3eYJm6JR7YpRHXpSu7vVcipFqQWkc_wNVK9TqJA2ejHnCydKOs089AdWTYDzNp2ZDSxbVUN80LNcz4lC4MFQcbDwYij4sZtK6yG3-sOPFFmXt1DDcIE-wiT5T6jIk5zikqfjT4XIJd1swp0RaMc117Fo27bxV0Y-1MZxcB2EwWCtzMkamuyQvVCm_6owhy6ejc2cBEmQyPoA0t5myFpCnO3OWAhHt5O5RKr3y1PcanYEHsz9CgdRaTvFNpGJAr3qgGCIjQlgng-7xjB_Y9DnZcdnydnHLTdPsBRVTkYB8NZerS9tQwcpXP9kTZYFj6Khrd1iy8W_88GkkSSg05GI1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62994becf.mp4?token=octFfi7WEZj4MfoNf0gUfvmJnbEOE3nWB9HSL_Q6JBR288aFl0HKVQUx1-Dd_pCYMvilxbMMtMV06fP0H_PpdzG3cZXmauDzIcXANO0bBpdXW49wGS7vqwRReo07Igo0Yz0sB7BkG62jmBaqARlxSoEGpOOZp3cvPw7YwoIN6G1fXzV03sz1p5FgiklFuprp-WON4azT4psrt61WsKdljF06d4WvEByjb5JYwowISg2wcQMKkLrUlNqCaOVz8WLWEp5C41lDnNEN9dAA9z8RVYggQwGh-mHC0BC7XlTJlsdUj1F9z8wRycSxEl8AjhO_FIGFUbBchlffNWVc6V1gV3eYJm6JR7YpRHXpSu7vVcipFqQWkc_wNVK9TqJA2ejHnCydKOs089AdWTYDzNp2ZDSxbVUN80LNcz4lC4MFQcbDwYij4sZtK6yG3-sOPFFmXt1DDcIE-wiT5T6jIk5zikqfjT4XIJd1swp0RaMc117Fo27bxV0Y-1MZxcB2EwWCtzMkamuyQvVCm_6owhy6ejc2cBEmQyPoA0t5myFpCnO3OWAhHt5O5RKr3y1PcanYEHsz9CgdRaTvFNpGJAr3qgGCIjQlgng-7xjB_Y9DnZcdnydnHLTdPsBRVTkYB8NZerS9tQwcpXP9kTZYFj6Khrd1iy8W_88GkkSSg05GI1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
قتل ترامب في أعناقنا.. الحشود الغفيرة في مصلى طهران تهتف للثأر من قتلة الإمام الشهيد.</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/81012" target="_blank">📅 07:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81011">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e131c24.mp4?token=YdIOQSAgnoEtIMrVLOlXyQST691JPYCQan6vB_torGJA1EZ5pGxMlviHglgi3xp90rzaB3SgFJt48lYcl4wTufM8_gkH-OcMgVjmPE2tDlK_368cCTvBWFYtncB2bPITYpu7gbLtORUhLKlVXOYcW00xzyrPOdxYQ5bg_u6RuVM37hjHZjZkJjIVMUhnDYasdR0f-JPr5S5XpImVHby_UkJ5Qh0xpJcuLALn6Uc1nAYPNVaRfdNpOwyOdhtop4a7iT0yY7WtjA5phuZi3PhFxJfn26DvBrt-N7QJutJoxMmW0JK1WnnVdBBp8RhB2vgdb1MxkzUbDNfY3KQqoKAv8DaCGBS1TkttGfRgOTB7fjdIbiJKansqZU2Bo8JxIw8_4r3GkO61zZOlW4S4mlBWbgVhfRNnRKTf57U36XbDWqbUIoFz-B2HUevGO5xJH78BYBxdyasHbU0_jJfzLEZyrjiNl8j5pdKaetIsu0zXtUwtbNi2BKo_PKJu5M0HxKn2ScoLqJyEivqiIfQ0aZ4eKV_LNqUdXR_1NbJF-ilkH0GeZUZEupPuwBaXfPipXvLZGIzIwdAwSuEHtCQrHN4h-tyh4cbRfsAHCKx1u59HnefsEo7DiS0XEhATU4RdrCG16kyq-wzkWDxZHyLtrLVQp14T5nTI5PVT3yFuonFO-HE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e131c24.mp4?token=YdIOQSAgnoEtIMrVLOlXyQST691JPYCQan6vB_torGJA1EZ5pGxMlviHglgi3xp90rzaB3SgFJt48lYcl4wTufM8_gkH-OcMgVjmPE2tDlK_368cCTvBWFYtncB2bPITYpu7gbLtORUhLKlVXOYcW00xzyrPOdxYQ5bg_u6RuVM37hjHZjZkJjIVMUhnDYasdR0f-JPr5S5XpImVHby_UkJ5Qh0xpJcuLALn6Uc1nAYPNVaRfdNpOwyOdhtop4a7iT0yY7WtjA5phuZi3PhFxJfn26DvBrt-N7QJutJoxMmW0JK1WnnVdBBp8RhB2vgdb1MxkzUbDNfY3KQqoKAv8DaCGBS1TkttGfRgOTB7fjdIbiJKansqZU2Bo8JxIw8_4r3GkO61zZOlW4S4mlBWbgVhfRNnRKTf57U36XbDWqbUIoFz-B2HUevGO5xJH78BYBxdyasHbU0_jJfzLEZyrjiNl8j5pdKaetIsu0zXtUwtbNi2BKo_PKJu5M0HxKn2ScoLqJyEivqiIfQ0aZ4eKV_LNqUdXR_1NbJF-ilkH0GeZUZEupPuwBaXfPipXvLZGIzIwdAwSuEHtCQrHN4h-tyh4cbRfsAHCKx1u59HnefsEo7DiS0XEhATU4RdrCG16kyq-wzkWDxZHyLtrLVQp14T5nTI5PVT3yFuonFO-HE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من مصلى الإمام الخميني.. "أين نصر الله أينَ ليتَهُ في الحاضرين".</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/81011" target="_blank">📅 07:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81010">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من مصلى الإمام الخميني.. "أين نصر الله أينَ ليتَهُ في الحاضرين".</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/81010" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81009">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b4c155b1.mp4?token=KPW4DCJL5Y5Is__QR7WDnibSfR8ygaMlqIzH4vkdAX1Dc5xpctBY_kJRnqdLhC8PmtJH0hBLTFJdBLb30bXPCOODADxJP3hcJ4le9prxMV0lZSynuZPQkenEfZ9PJpxAKVXV-WIx4uvmOYXiOT-8S-24IOeOpZ6J8v-O2neoiaj6KbKY8Z5D2vKSgi5q2mjxGb2nclmqil7fauXivJeeQ05FMkl5SwrsrmtSLJQMNd8SqCi0dfF_RUfgnhM7TZme9KXPzFeUtpQkOOwveK-vOXh0357aE4D_pu12eWN0YpipEVItHG753gVsqluM5ANqR2v-cH2UR1Hw3YdnOAoy9YKJUU8AC2Q8Up-vYy6UKlhPB1hv9OV7tlhkPWaAIN3Z3g0XNP1nbuCrqoW8wvJWuOPv8xaiHwS1NF6l7E8LiUfmipEJZ6O_66vPS33-ekaNWnf4CkFJpBlaG3zl5kDIBilMIKJ7x2WTEPJZ2XEdZl3QYuR60qNxVOGW51Rfh7lwwCp6_c8HAkvAi0yckxClhqBJsf-H6X2IH6RfgYIZUU06WX6_XfZ6EyDseymi2PBr5TMu098Jl1rAFPopr_Tyhz6jEwLuXo0speSQJRNRqJhf9mlxL3GXL_re7JbKVQXkxE_wip9afZpx5Kj0qUFGw25M6u3F5mhhZBiwhvBqDOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b4c155b1.mp4?token=KPW4DCJL5Y5Is__QR7WDnibSfR8ygaMlqIzH4vkdAX1Dc5xpctBY_kJRnqdLhC8PmtJH0hBLTFJdBLb30bXPCOODADxJP3hcJ4le9prxMV0lZSynuZPQkenEfZ9PJpxAKVXV-WIx4uvmOYXiOT-8S-24IOeOpZ6J8v-O2neoiaj6KbKY8Z5D2vKSgi5q2mjxGb2nclmqil7fauXivJeeQ05FMkl5SwrsrmtSLJQMNd8SqCi0dfF_RUfgnhM7TZme9KXPzFeUtpQkOOwveK-vOXh0357aE4D_pu12eWN0YpipEVItHG753gVsqluM5ANqR2v-cH2UR1Hw3YdnOAoy9YKJUU8AC2Q8Up-vYy6UKlhPB1hv9OV7tlhkPWaAIN3Z3g0XNP1nbuCrqoW8wvJWuOPv8xaiHwS1NF6l7E8LiUfmipEJZ6O_66vPS33-ekaNWnf4CkFJpBlaG3zl5kDIBilMIKJ7x2WTEPJZ2XEdZl3QYuR60qNxVOGW51Rfh7lwwCp6_c8HAkvAi0yckxClhqBJsf-H6X2IH6RfgYIZUU06WX6_XfZ6EyDseymi2PBr5TMu098Jl1rAFPopr_Tyhz6jEwLuXo0speSQJRNRqJhf9mlxL3GXL_re7JbKVQXkxE_wip9afZpx5Kj0qUFGw25M6u3F5mhhZBiwhvBqDOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْراً</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/81009" target="_blank">📅 06:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81008">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6862495e50.mp4?token=YUpijnoIp2YFeiKa5diy2QkDUJf3TRgVYXOQ2Jp3s0IDaKJcKHxaKLWwmNWBso1O2jYpRtvgZiuh365yCFUSIkFNmblnUL40qd9Af98tPsD0AWLH99sheBgXz7UOtWR667c_TQo_7kZTVEKDkjTxqWZEW61XGuSwRpPcpgqlUqrr_kBzxQ9HaXX33CGNeZ_bLo_87nP0bT4bth4m2gSGerOso0g3VKPPNjRwDlBQ2zOW0bgi-pDJ__mx6zekghuIyTLmNP5TYIGtwlRnl9yEwn2wBWUDqsGt-phN4k80SR1m1xwfAAlPlDf6g89EXTad-DCPSizPlj0aCogZ_s-Yhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6862495e50.mp4?token=YUpijnoIp2YFeiKa5diy2QkDUJf3TRgVYXOQ2Jp3s0IDaKJcKHxaKLWwmNWBso1O2jYpRtvgZiuh365yCFUSIkFNmblnUL40qd9Af98tPsD0AWLH99sheBgXz7UOtWR667c_TQo_7kZTVEKDkjTxqWZEW61XGuSwRpPcpgqlUqrr_kBzxQ9HaXX33CGNeZ_bLo_87nP0bT4bth4m2gSGerOso0g3VKPPNjRwDlBQ2zOW0bgi-pDJ__mx6zekghuIyTLmNP5TYIGtwlRnl9yEwn2wBWUDqsGt-phN4k80SR1m1xwfAAlPlDf6g89EXTad-DCPSizPlj0aCogZ_s-Yhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هتافات "الموت لأمريكا" باللغة الإنجليزية في مترو مصلى طهران.</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/81008" target="_blank">📅 06:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81007">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07ba323bb.mp4?token=EfbX6pk166sgV2ZPD3R15aUdWdlhznWasvbdq9ZrWes_ebzTGtfYTO-FOOpI8ARzS2xZw8nCoLqJZX__0e5hVdLE-BYXg2cfh7sipYbia-a1mbhGcgOkNUJ1nB-1l33fTieHGi8JK7AqQC9HNK02K4uDAzItQk-EyGGs4371XdRnGUzzBh2OZhjLokUDhOw_G0uXrkHLL8AgNnMTiCv0MdKs-S-kEo0fVOVVyrMndPgEFUFuD0MbTU8WDRm3rB9BlbUi22mVzQlGK1zVlRs2J-Pt3ahvG-6OJereZS8Y07eFWmlOZGk4Xe1oAYK7s8aTnZSTo7sO5v2fsxkXx4zhHw-akL_mGz8hGmb25pvJ3ybRkL1AJmvOSyflXiooRxRNAenPQCZ656lklLHYORiSbzMOoKoQbeD8OXkh-OJpRzzAUrMkTAkTItrQOu41CGsMZugIvqhhupj1Mvm9QfQDnQmcYQveU9eKF8iMDzd-wUoVRKWIvJK1VOTooF1ibEYxI44VBfQaWeoFOBjCz5wfxgrkGN-uovtgtRFF0tu6mdmR6b3ujbMF47BgN36VddHrTXgBM14OOniqCMJ3Gfs2vCvis41GdAbThjqXP3MSHRP5xZLJ0Ss3ofxgXx5vMYGUXfst7tl_xaGTsmOg7VSO5ne3seZT6PVv9cvp-QBOC4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07ba323bb.mp4?token=EfbX6pk166sgV2ZPD3R15aUdWdlhznWasvbdq9ZrWes_ebzTGtfYTO-FOOpI8ARzS2xZw8nCoLqJZX__0e5hVdLE-BYXg2cfh7sipYbia-a1mbhGcgOkNUJ1nB-1l33fTieHGi8JK7AqQC9HNK02K4uDAzItQk-EyGGs4371XdRnGUzzBh2OZhjLokUDhOw_G0uXrkHLL8AgNnMTiCv0MdKs-S-kEo0fVOVVyrMndPgEFUFuD0MbTU8WDRm3rB9BlbUi22mVzQlGK1zVlRs2J-Pt3ahvG-6OJereZS8Y07eFWmlOZGk4Xe1oAYK7s8aTnZSTo7sO5v2fsxkXx4zhHw-akL_mGz8hGmb25pvJ3ybRkL1AJmvOSyflXiooRxRNAenPQCZ656lklLHYORiSbzMOoKoQbeD8OXkh-OJpRzzAUrMkTAkTItrQOu41CGsMZugIvqhhupj1Mvm9QfQDnQmcYQveU9eKF8iMDzd-wUoVRKWIvJK1VOTooF1ibEYxI44VBfQaWeoFOBjCz5wfxgrkGN-uovtgtRFF0tu6mdmR6b3ujbMF47BgN36VddHrTXgBM14OOniqCMJ3Gfs2vCvis41GdAbThjqXP3MSHRP5xZLJ0Ss3ofxgXx5vMYGUXfst7tl_xaGTsmOg7VSO5ne3seZT6PVv9cvp-QBOC4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لبيك ياحسين</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/81007" target="_blank">📅 06:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81005">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFU8rlgySUcimdcx2cyD3wSAElAw-5RXeahi51BJ7jHhzIGiDQ06FBk-KW8hj-G1vQUieksZuMXZmlW5unMpqKz59Yd92SCANZIfu-NeTsCtIEaAxBMu9kHweHKe1f0XD-939fgVRcRP4StT64Pd-FRPvLJIM4WQXhqQ7Q-XofKN1ibAiE-EanwRVs7SS6uI92Nn1eg58xvM3aOYluGdXDviEafDtTkiYK4tavto-02QrRx8ONVPUlE0JmtQbLqddhZNNe_S1pyP9EELyfFEP7xoHy6zUGRyzkdKS6XpTJWAAbvSVrH-xxFUrP9Pc_jjpEM85wd0z8-ca9hxDZpiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJw0YOXsGySK70ob55jjYMHrQRlVyr7NdteVlWVMDrFBaQQyviL9BV_t1vc7hDX3qND7cQQpJKUAf6p-UVTSSZEZYhB4TI_2jQHFBX8WBj7WZLjEB_TVe2UA-A_wuoM7oKOB48zuezu6GiC_s9VlYGJ1fY1-CnKVYT2PwwRkXtcGRkBAVobE9001SZmV8hhNkuDBHVIdKmg19iYQfw4Ob_yW1War8AKc3nquTp68roxdywejwPLT3AYW2yw6zZPyFCths82fVBf9zShdY-7ZijdOGOlRN-YpIGiUZ7Yo3jFpZruOv0KSSDgPTtbyYPhlx3ashWmUXjXUhJuXLkFgOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرچم‌ سرخ انتقام تا نابودی اسرائیل برافراشته می‌ماند.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/81005" target="_blank">📅 06:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81004">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ca7ed0e3.mp4?token=o4rIebDQ1ynxdbq3IFbhj-UjVXjxnsobsUUH0wKpb576ditmhd4TGjkWubBN606k_ropnFau-1QZQuhVbaYSqIGep_HCdh5rUr7sGHQWebv3u2os0HeojPpaYRUXUzP8hPQukVFWlwGNv3tiFDaMgbENrl0BPcq7-4LMfz-w67QpHd9iguFp7r8gZ7BwRuYMVYLtnubMTko1WilSGvPVNNvZ6CsDlb2K-qtZNZ0MSQ-TNblTjLaH5tqbXMAjsk2DSO2Fe0qf8BZxJLVwssX2fGdbJ3huuNTkvBs_Q2IIwAPqCX7mAJrzncqgHBO-QOYOLET--x0a3y30dBhSYVXG1pdWGWKSzV2_Y7dAiNKXvQFGQ33LqIT1o29oVLYVyKsdhsVyLQgIbHoeWC7igMyt4YlUAaoTNQENBQacD2C1MXwieQsJ_DEnJIeQMEYdGl3qXBCIYj43-DiotJmaif5-W5GSqGYRFt7tFTNFTMbdbr-RT0YOKMoHIdUuFJJWr6c9OOCk-TTLkwrEUACKbtbdENtltjDX0MIT-vDFm5rMKo64nAWJsl0z3pJFFEge6bF13f8VlrW-Gj4SZaSH4XSmS5nhY7fp4QlPQl5AFl8NNKoijQ6fNLrDFFGYv2MNblp-Z00mRT8c24yPpPu8prtV1fH_eEu8HZsDQfHfSrmE4Ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ca7ed0e3.mp4?token=o4rIebDQ1ynxdbq3IFbhj-UjVXjxnsobsUUH0wKpb576ditmhd4TGjkWubBN606k_ropnFau-1QZQuhVbaYSqIGep_HCdh5rUr7sGHQWebv3u2os0HeojPpaYRUXUzP8hPQukVFWlwGNv3tiFDaMgbENrl0BPcq7-4LMfz-w67QpHd9iguFp7r8gZ7BwRuYMVYLtnubMTko1WilSGvPVNNvZ6CsDlb2K-qtZNZ0MSQ-TNblTjLaH5tqbXMAjsk2DSO2Fe0qf8BZxJLVwssX2fGdbJ3huuNTkvBs_Q2IIwAPqCX7mAJrzncqgHBO-QOYOLET--x0a3y30dBhSYVXG1pdWGWKSzV2_Y7dAiNKXvQFGQ33LqIT1o29oVLYVyKsdhsVyLQgIbHoeWC7igMyt4YlUAaoTNQENBQacD2C1MXwieQsJ_DEnJIeQMEYdGl3qXBCIYj43-DiotJmaif5-W5GSqGYRFt7tFTNFTMbdbr-RT0YOKMoHIdUuFJJWr6c9OOCk-TTLkwrEUACKbtbdENtltjDX0MIT-vDFm5rMKo64nAWJsl0z3pJFFEge6bF13f8VlrW-Gj4SZaSH4XSmS5nhY7fp4QlPQl5AFl8NNKoijQ6fNLrDFFGYv2MNblp-Z00mRT8c24yPpPu8prtV1fH_eEu8HZsDQfHfSrmE4Ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم‌ سرخ انتقام تا نابودی اسرائیل برافراشته می‌ماند.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/81004" target="_blank">📅 05:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81003">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e165ad798d.mp4?token=fnMp15fLCURm23UOMGmOzVtf_ahIDeZHtpnV9tMY-b0eJtBdcNlTW5pdJlh1VQ42g9jx2QQgm6RwGk2TjChNonfCGJ4lAgMTU_zQkg8q4BNhXDNn8NL_bkYWu8dJUUrfkEnHbIZIBhnfTBMvFv8hj9lprsVLkoUFvbGhoRwjP5P4siRdJUyo4din0rcmrju4LGnE6LC9h-wBiKEx_ToqgXql0FCi9LBKTnRoeeFqQfFMsoF7DQ2GLucjM09PyV0hMrBArb-rj-f-SeZibaswVFcDBLJboXDM_Wc7YcU5x6k3DiLMp-qYsv0OzeOB6tBVVAdPTKtKCgIdqL_atPHEvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e165ad798d.mp4?token=fnMp15fLCURm23UOMGmOzVtf_ahIDeZHtpnV9tMY-b0eJtBdcNlTW5pdJlh1VQ42g9jx2QQgm6RwGk2TjChNonfCGJ4lAgMTU_zQkg8q4BNhXDNn8NL_bkYWu8dJUUrfkEnHbIZIBhnfTBMvFv8hj9lprsVLkoUFvbGhoRwjP5P4siRdJUyo4din0rcmrju4LGnE6LC9h-wBiKEx_ToqgXql0FCi9LBKTnRoeeFqQfFMsoF7DQ2GLucjM09PyV0hMrBArb-rj-f-SeZibaswVFcDBLJboXDM_Wc7YcU5x6k3DiLMp-qYsv0OzeOB6tBVVAdPTKtKCgIdqL_atPHEvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أجواء مليئة بالحزن تعم مصلى الإمام الخميني قُبيل إقامة صلاة الجنازة على جثمان الإمام الشهيد (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81003" target="_blank">📅 05:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81002">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d616b39370.mp4?token=NB9KaxMOJrXzUf_bE-1eW__PO-FulwJcaxgM8qGu6ANIBxDzH482r7T8MHSBdqtIeUjXJj1PfZHXcDGssq2DUbE8cacNqddxr1_7Z_eUFmXG0cOWHJLiQHyc51Dll8g00gxg0q3LSuKDXoBW8d50XZhCWuvv3m_7RhZKMK4A3QQ0-Uf5-iOFponPDl3WaKzk2E1cjRRIMMepIGEVms5ygOef559UrbIOHfFqWdTRsZ_7UFRfGa-p_94D7MCMVtZP4kAlfwTkOgU7TfsjYsdhC6hAHB2pEZqGjR8jiGrH993qwybPE82MmBv9aUN9rKmlKK5MZAjpMUVPkjcsPJ2N8XV4DX0gzcf3su6cohUqprN3FgEHqZLslNxWyPrdL2zKaUGD6SIpiuJTQcPZLwIEaIbHoG2xYlkPPMIp4pPMpjN0DVCQslNV-Cd2v26nmZfQkqAaOPRnsPKkY7JLJlHAvKmmEZDBbHfElxi7KeXDX_tHc9shP09_Utdi7Yf9wqcK4ky_fzqmTeegXDSAG0a2MJAlAaOc_sRiVOW6b_sxze82lSh-hnVY6YRUjEkvEamMZIKwB0iibb3Yda4cbyuy3oUGNuTsfl1l0D5qD_9tX43IyG264jhWJBqJrEHl2OWY1BgUNMkR4l5IYJhURTAsjPobDJkUJHqh0E4Fh3Yxbwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d616b39370.mp4?token=NB9KaxMOJrXzUf_bE-1eW__PO-FulwJcaxgM8qGu6ANIBxDzH482r7T8MHSBdqtIeUjXJj1PfZHXcDGssq2DUbE8cacNqddxr1_7Z_eUFmXG0cOWHJLiQHyc51Dll8g00gxg0q3LSuKDXoBW8d50XZhCWuvv3m_7RhZKMK4A3QQ0-Uf5-iOFponPDl3WaKzk2E1cjRRIMMepIGEVms5ygOef559UrbIOHfFqWdTRsZ_7UFRfGa-p_94D7MCMVtZP4kAlfwTkOgU7TfsjYsdhC6hAHB2pEZqGjR8jiGrH993qwybPE82MmBv9aUN9rKmlKK5MZAjpMUVPkjcsPJ2N8XV4DX0gzcf3su6cohUqprN3FgEHqZLslNxWyPrdL2zKaUGD6SIpiuJTQcPZLwIEaIbHoG2xYlkPPMIp4pPMpjN0DVCQslNV-Cd2v26nmZfQkqAaOPRnsPKkY7JLJlHAvKmmEZDBbHfElxi7KeXDX_tHc9shP09_Utdi7Yf9wqcK4ky_fzqmTeegXDSAG0a2MJAlAaOc_sRiVOW6b_sxze82lSh-hnVY6YRUjEkvEamMZIKwB0iibb3Yda4cbyuy3oUGNuTsfl1l0D5qD_9tX43IyG264jhWJBqJrEHl2OWY1BgUNMkR4l5IYJhURTAsjPobDJkUJHqh0E4Fh3Yxbwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
بعدسة نايا | المواكب العراقية في طهران تستنفر لخدمة مشيعي قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81002" target="_blank">📅 05:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81001">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd7aa532cd.mp4?token=Asa23_131JWVg4RnrVo_zHJwWsILHfJ4_5fPmczO7m99bK1Bi71j6D9X4Ux8Nhj5seqlN9eJ6Pb3tTcZAUq2mMHLJdBoV8XYB2LELe5r4Mm33v2xxcjbVfO9A70jn37X0RqGMGARXzt5atKhzde5DseKIl_Fdis5MQi-pNpgJz5wLQ03pAG9_LEwENr4Uz7q2ieHTLFb7okc2hW3eLulFWZDL_E9QxNxDYss-XbvOey-eqbsJdJixwD5Q7_dhEoJ2sQRV6hv9pLRcue1BfAaTUcJc2FF6wqvE2iPAhIia2YkoIy6DINbvSfwmVV_Fd_7E3A7X7dZ9XNge7ls990SSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd7aa532cd.mp4?token=Asa23_131JWVg4RnrVo_zHJwWsILHfJ4_5fPmczO7m99bK1Bi71j6D9X4Ux8Nhj5seqlN9eJ6Pb3tTcZAUq2mMHLJdBoV8XYB2LELe5r4Mm33v2xxcjbVfO9A70jn37X0RqGMGARXzt5atKhzde5DseKIl_Fdis5MQi-pNpgJz5wLQ03pAG9_LEwENr4Uz7q2ieHTLFb7okc2hW3eLulFWZDL_E9QxNxDYss-XbvOey-eqbsJdJixwD5Q7_dhEoJ2sQRV6hv9pLRcue1BfAaTUcJc2FF6wqvE2iPAhIia2YkoIy6DINbvSfwmVV_Fd_7E3A7X7dZ9XNge7ls990SSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
بعدسة نايا |
المواكب العراقية في طهران تستنفر لخدمة مشيعي قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/81001" target="_blank">📅 01:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81000">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eda2a08b1.mp4?token=KuYU4_KsFrS_FC1wC-9pTMS1UEU6iEj2Dg1rMnFU3n1B3uW8w74mH9CeAxVBFX_zmAqimM2RspHCBfvtQqkRr_NUaCJAOQ9v5R2UpKiyYb33-G7zfInrmi2pgPGfZzkrLpB_E6NGVRtK1q7YLX2WdlTYNnLhg1F1d__SpxDhJICSd8TaUToHYWg1LAz8ttSIJniWl3m6RTueAG5WCk632pweIhYHsgZcdbwRa5Sluc8EbrdZZ6yIp-cBNK6-0cxx4zbMrU8Zj9RXeMzptH99_rkqQ_pmdQmjGcntNC8M9_a_GoGeppZf7jm7dFrUPlzpB9fWObSGkYSzVHjY35SG2oERG5Wz8MRhI71tW5jseFbKWcVFYriQOzeITyTwCLXf1l4qPf3ykol6XpMI6Ypz_qrRndytPTkOeB6MnezxpA9pw260mkRK8P8S-v06Qhw8ptWfRKoixr7_bgTyqz_OL--Ehqzrd5kRzy5zh3W1pMli4_w9UEwSAzS8CputAeLVabQx99wOz7XyztNcajlUMwMpSJTzwUWVMpOqmpLf7ZiKOxbldIp0IU1-zM3YuTFOywh-MmD29fFbonW58M1SobcDdGiEsmI7YnJS94rLsnHA3ltHKCkX3zdYQciRAu4oYnsmHKl02xmhStFIvyq3kdlJsx2eqD7eLt9r-GuDC0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eda2a08b1.mp4?token=KuYU4_KsFrS_FC1wC-9pTMS1UEU6iEj2Dg1rMnFU3n1B3uW8w74mH9CeAxVBFX_zmAqimM2RspHCBfvtQqkRr_NUaCJAOQ9v5R2UpKiyYb33-G7zfInrmi2pgPGfZzkrLpB_E6NGVRtK1q7YLX2WdlTYNnLhg1F1d__SpxDhJICSd8TaUToHYWg1LAz8ttSIJniWl3m6RTueAG5WCk632pweIhYHsgZcdbwRa5Sluc8EbrdZZ6yIp-cBNK6-0cxx4zbMrU8Zj9RXeMzptH99_rkqQ_pmdQmjGcntNC8M9_a_GoGeppZf7jm7dFrUPlzpB9fWObSGkYSzVHjY35SG2oERG5Wz8MRhI71tW5jseFbKWcVFYriQOzeITyTwCLXf1l4qPf3ykol6XpMI6Ypz_qrRndytPTkOeB6MnezxpA9pw260mkRK8P8S-v06Qhw8ptWfRKoixr7_bgTyqz_OL--Ehqzrd5kRzy5zh3W1pMli4_w9UEwSAzS8CputAeLVabQx99wOz7XyztNcajlUMwMpSJTzwUWVMpOqmpLf7ZiKOxbldIp0IU1-zM3YuTFOywh-MmD29fFbonW58M1SobcDdGiEsmI7YnJS94rLsnHA3ltHKCkX3zdYQciRAu4oYnsmHKl02xmhStFIvyq3kdlJsx2eqD7eLt9r-GuDC0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا | حشود غفيرة تتوافد عبر المترو باتجاه مصلى الإمام الخميني للمشاركة في مراسم تشييع السيّد الولي</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/81000" target="_blank">📅 01:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80999">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a596566298.mp4?token=JgOdpAWveN89A_VLnUvtPE6dXVzYu2D_1U4IOJQDWQdGwKs1syJoXxOx3W6nYnkwYGFZ6f7-SUpJWtiH8OM-xmgTZHuLV28koKS3P4BaOEROu2-Hf3e4INMWrgBsiiRJ4i2esnHSmGjdhM3ujqwJs2_Gh13-RmlhTJYfA0phC9Pd7gzCOD7adOk7DtVfdyIzF8OJnCdi7MlC5t78HEwoqJjn1rdurnFpVrnNl2a34EVhUDnmoFv3iw21DYoLsg6x1ftPVi6CuxwJh7UNlbG4KQQ3NEmRaHAJerpC82rCg6PtpaOUY5UOXTZjOnloTzqyoUnJV4qj5ATPRxb0Xni_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a596566298.mp4?token=JgOdpAWveN89A_VLnUvtPE6dXVzYu2D_1U4IOJQDWQdGwKs1syJoXxOx3W6nYnkwYGFZ6f7-SUpJWtiH8OM-xmgTZHuLV28koKS3P4BaOEROu2-Hf3e4INMWrgBsiiRJ4i2esnHSmGjdhM3ujqwJs2_Gh13-RmlhTJYfA0phC9Pd7gzCOD7adOk7DtVfdyIzF8OJnCdi7MlC5t78HEwoqJjn1rdurnFpVrnNl2a34EVhUDnmoFv3iw21DYoLsg6x1ftPVi6CuxwJh7UNlbG4KQQ3NEmRaHAJerpC82rCg6PtpaOUY5UOXTZjOnloTzqyoUnJV4qj5ATPRxb0Xni_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
"ياعلي مدد"..
توتر امني تشهده مدينة السلمية في ريف حماه الشرقي بعد قيام عصابات الجولاني باختطاف عدد من ابناء الطائفة العلوية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80999" target="_blank">📅 01:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5noxvQSX4FYhTFdcyzJAfNsI1-hwIAYKOhKg03u3tsW-0R9s4bEl0e7bR7w70jwA7yuYqenDISLE5vFSk3YS6QZ_5aQKWF4UmUU2zmfbxNTpNs68YZJq0TvYmgQ64qUsnrZWPbxTxYcW4OdD1RJjHghnEvAoTLlR2cQGEWZK0CfGeEoNtLrFE8zvAaWPCyZ505bYQfLGWbJMOOfsZtpCDDtmfJ1YC-wvdinp3d9Sxc578-tS9v0ZiZ9WOAC9vBq65YozrxSubHuPuH1pPUUryBHd-N2_D1x9OgC2TH8N5Sr8Mqg6LuoWLs8ge24r0X_ocY7MdEtiRGElPS5tNc7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ac2ad5e5.mp4?token=LuW-9ZrT0ohE-wwGQ4sMxGGBFe2UZWeZE4qCAsNuCu8XovnVXNY5zE1kBuhJw0QEz-e3iH8--yk4Pp6hoDjLYynwFY3Q3YY1M9kuLlaubm_uy6HC14XuhFWODfXcFqYgn82lkdocJDIGaSWUED3-fuxAo92edzo3FQKcq4ysi6mx-KeUZhok1jKmWzkgdJp0P0ZJxoL1u9NlTaMzdZErtLEqMeYy5A_oj83Dj1nPnn0cflanyPhMd8bfJSjWkW6uwMLXGdFhwOhFo1Nsmw47AoCmUH0x1IOzVYfpBkOkvUFLRpqfo-9juqb1sLkqLVgtqLJiu0rxDYbUS-4Q7gTYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ac2ad5e5.mp4?token=LuW-9ZrT0ohE-wwGQ4sMxGGBFe2UZWeZE4qCAsNuCu8XovnVXNY5zE1kBuhJw0QEz-e3iH8--yk4Pp6hoDjLYynwFY3Q3YY1M9kuLlaubm_uy6HC14XuhFWODfXcFqYgn82lkdocJDIGaSWUED3-fuxAo92edzo3FQKcq4ysi6mx-KeUZhok1jKmWzkgdJp0P0ZJxoL1u9NlTaMzdZErtLEqMeYy5A_oj83Dj1nPnn0cflanyPhMd8bfJSjWkW6uwMLXGdFhwOhFo1Nsmw47AoCmUH0x1IOzVYfpBkOkvUFLRpqfo-9juqb1sLkqLVgtqLJiu0rxDYbUS-4Q7gTYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا |
حشود غفيرة تتوافد عبر المترو باتجاه مصلى الإمام الخميني للمشاركة في مراسم تشييع السيّد الولي</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80995" target="_blank">📅 00:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808640a81.mp4?token=pzYXAKCMArGZ5ec1hR4QK986qpfbYKo6jl0ElCSqgIy-RaKHhfQU3N3ebAy2o1vjP8uxzrwAmsJurmxBELIUj13mjB2I-X1YWSFXtgB9rzAuDpE-EIjRQr4JlnVowkHRUTFZk2lR5_VewKWOoYQ7SQjfUO_bn-VKZgwWt8nrlpSJD6cwStl0NA836D76MXee0sFZFVZdaACP6USseSVEnmklsEMemunjgublcArfHCvNRHZ37WbyEXc3AHFdvJcWlokpPMrjb-PC1ILuTF88I-HnBiSM11jHTh4yUG4zHujPKh2-kt3WFv_fFYRFGdSBZkin_alFffms0Sg7DATKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808640a81.mp4?token=pzYXAKCMArGZ5ec1hR4QK986qpfbYKo6jl0ElCSqgIy-RaKHhfQU3N3ebAy2o1vjP8uxzrwAmsJurmxBELIUj13mjB2I-X1YWSFXtgB9rzAuDpE-EIjRQr4JlnVowkHRUTFZk2lR5_VewKWOoYQ7SQjfUO_bn-VKZgwWt8nrlpSJD6cwStl0NA836D76MXee0sFZFVZdaACP6USseSVEnmklsEMemunjgublcArfHCvNRHZ37WbyEXc3AHFdvJcWlokpPMrjb-PC1ILuTF88I-HnBiSM11jHTh4yUG4zHujPKh2-kt3WFv_fFYRFGdSBZkin_alFffms0Sg7DATKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
وفود جماهيرية من حركة انصار الله اليمنية تشارك في مراسم توديع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80994" target="_blank">📅 00:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e739239b93.mp4?token=NzkYxgCnXunK-53G9QCpnwDzpGrIRml3W2gbcNAchcVQegzGPX9XU4hbg8P0RF-mqtmxYcBGaz6QgyGeqplDCNAAnxrVOGuWkCBQwMsX87aODaB6mPUd4da5G3qAicuystr4QIH4V0YCX2HaV2YomuxnSw3COlGgNIzsv1MqClcTp8biHjkwO4zRAG8TnIYHH90zWgc1jTr_wTSdotnkKl51EegT_Ot7zQJdOg4pjP2knUYW8pyFuQoBxtGrH1UU4MvsAXQTnfgHuTTDsXoQqnNbxXdqPP7x9-RsAAiQ9Tq-SsMdnf4PYx4Fpw8PDtJ8vSjDTDvTVu7mS22BxzOYgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e739239b93.mp4?token=NzkYxgCnXunK-53G9QCpnwDzpGrIRml3W2gbcNAchcVQegzGPX9XU4hbg8P0RF-mqtmxYcBGaz6QgyGeqplDCNAAnxrVOGuWkCBQwMsX87aODaB6mPUd4da5G3qAicuystr4QIH4V0YCX2HaV2YomuxnSw3COlGgNIzsv1MqClcTp8biHjkwO4zRAG8TnIYHH90zWgc1jTr_wTSdotnkKl51EegT_Ot7zQJdOg4pjP2knUYW8pyFuQoBxtGrH1UU4MvsAXQTnfgHuTTDsXoQqnNbxXdqPP7x9-RsAAiQ9Tq-SsMdnf4PYx4Fpw8PDtJ8vSjDTDvTVu7mS22BxzOYgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح ابواب جديدة في مصلى الإمام الخميني بسبب توافد حشود غفيرة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80993" target="_blank">📅 00:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80991">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d71ccc51.mp4?token=A8gvv1W3J2ZgbhaqY7Keax5kDneCaSONmTABc1En-v3Y4QYkbPLS2PJfv2eF0bXaVN0jWKuFDE1JlXXxc8EOR5Sjs9oBq2gTZHtVaDBg-6QKADq6Oc1NuU7EfxFXl-ep-UKxh9uNa5zLf25cHGZYE40513okhc3wN9H1vFZQb3xFJmqrdnZnhDlCMcTuT6AtNQFNHZHg7fYEUt1eZkiX4FwaG-MN5t2XPVZlLbBnCVuXQPhGtuXJosPheSbsLDcgeSJL2qHmpVEz7-1CgWJtoMwg1tjc3lswL8knj-53XlJNZ3u1tZ9BygSCfYEwpiFYTAk8FC8nFX8MV8lJPoqjcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d71ccc51.mp4?token=A8gvv1W3J2ZgbhaqY7Keax5kDneCaSONmTABc1En-v3Y4QYkbPLS2PJfv2eF0bXaVN0jWKuFDE1JlXXxc8EOR5Sjs9oBq2gTZHtVaDBg-6QKADq6Oc1NuU7EfxFXl-ep-UKxh9uNa5zLf25cHGZYE40513okhc3wN9H1vFZQb3xFJmqrdnZnhDlCMcTuT6AtNQFNHZHg7fYEUt1eZkiX4FwaG-MN5t2XPVZlLbBnCVuXQPhGtuXJosPheSbsLDcgeSJL2qHmpVEz7-1CgWJtoMwg1tjc3lswL8knj-53XlJNZ3u1tZ9BygSCfYEwpiFYTAk8FC8nFX8MV8lJPoqjcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات كردية تعتدي على العلم العراقي في محافظة اربيل بالتزامن مع قيام الجيش التركي بتعذيب شباب اكراد داخل الاقليم وتهجيره للمواطنين الاكراد من منازلهم وتجريفه للغابات واقامة المعسكرات.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80991" target="_blank">📅 00:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80990">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
مجلس الوزراء العراقي يقرر إضافة (25) ألف برميل من النفط الخام إلى الاتفاقية العراقية الصينية وفتح حساب لها لضمان سد وتسديد الالتزامات المالية للجانب العراقي للمحافظة على موقف العراق الائتماني واستمرار تمويل المشروعات من الجانب الصيني</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80990" target="_blank">📅 00:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80986">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-U8aiMvgA3y-MjcgKjubjLeFuivsVQBXYzJxuZ0FjjVhv7IgIJT6tuaHWKRuRhpXa3ZTgDkcAe-TzPDqG-jhe7yja9VZ4dt8mJau_g8BZ1SIMmRaISrV1vXNeNmp0H_-ihWD-BHvSCpEYIJv_K6FpC44kCKDRRqiSg6erjOdez5_rynaA6nnGSGlmN0WO3jk-ddNR-NvF4qfaB2XVBpC5-J5nSLd1b9ESv9_aw1FUDSgaKKOBy-aGZcJBeB1TXaBFQS1nRtCdTSC4wxX_SasEcxj5UPgWVPkQnyk4FLEE_csxPynDgN_JWxv1pEfLYgHph0kA8mR-IU7VsYS-zSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b91b0b8e.mp4?token=pERwmjVpSPMRvd6LW6wJMiJnUDXH4WRdIudEW4aN55NP3aW1ylOLnt6bV3kzQ09mgHG7bFA6nCQdoptTqEZqPc1sc_2GS2S9Yuw6rgLw5hSNtPom0YavryMPfAiXp2gsPL3FyxF_kZhDZvBwo23KMuW2HOEAcLc2blYdhsQHFTuN5BNkOPub9rP9H4ol6qPxCWyULmFgVbq7zyC-RQQHcZ1sp9lyfI4lvr9O0kYjJmWJ0MGgR6vMaKsjkIt17vg90Ol6ei0aYx8xv8O6NnTgOtXka70HgCJbxOqMXxIB82y7uM1pVViVhnrhkhe9u7e0hOo8jzOPFNNs6TWaMYSFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b91b0b8e.mp4?token=pERwmjVpSPMRvd6LW6wJMiJnUDXH4WRdIudEW4aN55NP3aW1ylOLnt6bV3kzQ09mgHG7bFA6nCQdoptTqEZqPc1sc_2GS2S9Yuw6rgLw5hSNtPom0YavryMPfAiXp2gsPL3FyxF_kZhDZvBwo23KMuW2HOEAcLc2blYdhsQHFTuN5BNkOPub9rP9H4ol6qPxCWyULmFgVbq7zyC-RQQHcZ1sp9lyfI4lvr9O0kYjJmWJ0MGgR6vMaKsjkIt17vg90Ol6ei0aYx8xv8O6NnTgOtXka70HgCJbxOqMXxIB82y7uM1pVViVhnrhkhe9u7e0hOo8jzOPFNNs6TWaMYSFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا |
حشود مليونية تواصل القاء نظرة الوداع على قائد الثورة الشهيد في طهران.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80986" target="_blank">📅 23:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80985">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🌟
محافظة المثنى تعلن تعطيل الدوام الرسمي يوم الأربعاء المقبل لإفساح المجال أمام أبناء المحافظة للمشاركة في تشييع الجثمان الطاهر لآية الله العظمى سماحة السيد الشهيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80985" target="_blank">📅 23:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80984">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصار الله محمد الفرح:
إصرار السعودية على تجرع الخسارة يدل على أن قرارها ليس بيدها وأنها مدفوعة ولا تراعي مصالح شعبها ولا تهتم لأمنها وطموحها، السعودية تبدد أموالها في شراء التافهين في اليمن ولبنان وتراهن على شخصيات لا تملك وزناً ولا احتراماً وتريد أدوات ومرتزقة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80984" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80983">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">طلب_العشائر_والقبائل_العراقية_تشييع_جثمان_قائد_الثورة_الشهيد_بالعراق.pdf</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/naya_foriraq/80983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#بالوثائق_للتأريخ
🇮🇶
🇮🇷
العشائر والقبائل العراقية تقدمت بطلب رسمي إلى قائد الثورة الإسلامية السيد مجتبى الخامنئي لإقامة مراسيم تشييع جثمان والده الشهيد السيد علي الخامنئي (رضوان الله عليه) على أرض العراق العظيم؛ وتعاهده على مواصلة السير على نهج الإمام الشهيد والتمسك بالمقاومة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80983" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
