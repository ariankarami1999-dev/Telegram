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
<img src="https://cdn4.telesco.pe/file/Ur25_Q7cGH1fH98uesEHtWqvITwn_ZSFBmx4flXlOVQKI2XknxuF1lt2pByp4xL15ZQgxy8nyXxxmZnEk7qDBnK4BCzHKSQanFBubfzZKtem_PTrq9weTvuehU2DDVZIVQ2dQqxZy-TtTZSkRLBVaR0qJp5BDx---nnu7T04MNzhSABhtD-0voz_K2tsL-LFk1UG6PtVdgM864P66QOvtCSi2-f9_Gc9RQTG5BEIvG0g_G03VzFS4bIgPqviVwhGnjueBPAtBrlJs75D3LlASRVVQKx5sk495F9V7z0i6e8FiAwLYlfVc7tGQDwOS9UxFEobRy9K1FK-B1p1JtNFAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 17:50:05</div>
<hr>

<div class="tg-post" id="msg-80228">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd16156d3.mp4?token=pOvXkAPUZL_d_x4JvFP5EOaiNt4g2Z7-YtXpPF8v-sOM45jBwHLOKSnbR6LqzzEO-lqwRnJGVWN9R-OEe4xj34MAERJMFGFHMomCXdDkUWf7FPMOtzfe4DtCjNi2GMCYEPBKqUCzLr7T3Gt2NoL12YFkzxfs1JSax_n45v90b-IILmPnoUmnQb9ZPGCA1BXRaToACRgWxmIDHjmXhwIUst7ggujZZJPI4IyTjMhl5vPorXWD1vfQg5H6Ny7cwcJFb61q-Qpi8QmFxRzciwg5Uq_YialOxT7fUq5WtPQlcYbFddJWdxoRUd231jjexNAQjRIo0HLa0QvEkz0WQSHm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd16156d3.mp4?token=pOvXkAPUZL_d_x4JvFP5EOaiNt4g2Z7-YtXpPF8v-sOM45jBwHLOKSnbR6LqzzEO-lqwRnJGVWN9R-OEe4xj34MAERJMFGFHMomCXdDkUWf7FPMOtzfe4DtCjNi2GMCYEPBKqUCzLr7T3Gt2NoL12YFkzxfs1JSax_n45v90b-IILmPnoUmnQb9ZPGCA1BXRaToACRgWxmIDHjmXhwIUst7ggujZZJPI4IyTjMhl5vPorXWD1vfQg5H6Ny7cwcJFb61q-Qpi8QmFxRzciwg5Uq_YialOxT7fUq5WtPQlcYbFddJWdxoRUd231jjexNAQjRIo0HLa0QvEkz0WQSHm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تحلق طائرات الهليكوبتر التابعة لقوات مكافحة الإرهاب وقوات الأمن الكردية في سماء محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/naya_foriraq/80228" target="_blank">📅 17:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80227">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مداهمات في مناطق الكاظمية والعرصات الهندية و الكرادة و البكرية والدولعي طالت مكاتب زياد الجنابي و عالية نصيف و حسن الخفاجي وهند العباسي و مدهمة ومصادرة خيول تابعة لعالية نصيف</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/naya_foriraq/80227" target="_blank">📅 17:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80226">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فضيحة تهز إقليم كردستان العراق.. ضبط رجل الدين السلفي البارز وأستاذ جامعة السليمانية (عبد اللطيف أحمد) متلبسا بإقامة علاقات جنسية مع طالبات قام باستدراجهن.  أكثر من 10 طالبات أخريات ضحايا له تقدمن بدعاوى قضائية ضده بعد إحالته إلى القضاء للتحقيق في القضية</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/naya_foriraq/80226" target="_blank">📅 17:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80225">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlNbi6FUDEir2CtU-vEgFQ5JQJgs6puyMha6f470YzK_o-SsIXZWuIaTjhhCD23xfLF_Gx72cISIdHPJstrhe8rnwRrkamV3pyKEGfrWeF1MJvmsfGoFmSjXGX_wxbRN9UYl4b5rEuy6pUxho13B4BWYqdPWjyjIZBg4I_F6ymkPD0GKsealEJxwMlr3iS9u5S3Q5CnYqGbAEB0OmiXIJktKIU3huYX2DjC01Onp7MBgin2jl43ipj-rCGlNqThx2AtDxvNPH9S_OTuj-zkGEjauvRlyeSBbaABB5fMPUGwAagDwJokOb28A7sIjL3GhXkgLeuB2LbwVBLMfvFddoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوات جهاز مكافحة الارهاب العراقي تداهم معامل الحديد التابعة للنائبة (امل مرعي) في سليمان بيك التابعة لمحافظة صلاح الدين وتجري بعمليات بحث عن مبالغ مخبئة في الموقع</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/80225" target="_blank">📅 17:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80224">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
قاليباف:
تفاهم واشنطن بين لبنان والكيان الصهيوني مؤامرة وفتنة، والإمام علي (ع) يقول إن الفتنة أسوأ من القتل.</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/naya_foriraq/80224" target="_blank">📅 17:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80223">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn-_OnVb9_jodUmqssY8m9WjruCdMo5CDWDNpS_nW5eTY6LolqNgWml2qcDpIfK7skyCXyb1XFGGqlPrWgNKj13ZW1gHGlVhmvh32N6jPyjdPJPID6zn5gHdFco-TqfG_vBay4Hmz2UIq1DIVXPG9_Eo_r-20HoWIgjlTRUZFhGL-k7NQWrgJR7BrSJXQyPq2DLufbL-q74P7seasbK0LY-ZO0cz4anVPo1Zu_xs0HZ-hruAIHmq_AfAXm5RY6Btie8IdCDSGGmVYmtF8u93vHRiFEM4tIa_KzSJ2LAXu_JLP2fCWrY9Y5f2zo7kbBwJLAcUxiJncJp85WchCIXo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إصابة عشرات عمال البناء بحالات تسمم غذائي بعد تناولهم وجبة غداء من أحد مطاعم مدينة الكرمة في محافظة الأنبار غربي العراق</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/80223" target="_blank">📅 16:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80222">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية:
عمليات الاعتقال مستمرة ضمن خطة مكافحة الفساد.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80222" target="_blank">📅 16:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80220">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URo7AJ3Kn7u-__Ji8rg3NoDxHF95KmHUZ_YvaAdFVlXkzb0evOWQspvld62l0eNMKN5fBaAv_AS7TI2aEeS1TvhX8NgRW8ROxUGs8CA8ba_QKPuMGHJDqkWDfcr55bjN8d45qRsPgrLUsOPQC4hE5kTh6x84NfJKFO7v9n0MQnSoUehkLqPtaPdWNBmAtf1M5Ho4T9bV8jnVHct5rAE_xV0onDRy9vqIP5mxDWUTV6eIxgGCedo2o5_0-AUdkIeFo1wAP4yWUlX-8GQaYPYxsY3Dw4ZE16ipIBYyO5iNGbWZRJYsLfDdH-htf7N67NOwUHuxJOgovKyqqL0Wbi6FAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية تصدر قرار بمنع ظهور (أحمد ملا طلال) في جميع وسائل الإعلام المحلية والأجنبية العاملة في العراق لمدة (90) يوما</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80220" target="_blank">📅 16:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80219">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">القضاء العراقي يوجه بتفعيل الإنتربول الدولي لاسترداد ومحاكمة 50 شخص متهم في قضية سرقة القرن</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80219" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80218">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وكالة الانباء العراقية تنشر اسماء المعتقلين بتهم فساد:
- رئيس تحالف عزم مثنى السامرائي
- عضو مجلس النواب زياد الجنابي
- عضو مجلس النواب بهاء النوري
- عضو مجلس النواب محمد الكربولي
- عضو مجلس النواب عالية نصيف
- عضو مجلس النواب محمد جميل المياحي
- عضو مجلس النواب حسن الخفاجي
- عضو مجلس النواب عبد الرحمن اللويزي
- عضو مجلس النواب مضر الكروي
- عضو مجلس النواب هند العباسي
- عضو مجلس النواب محمد فرمان الجبوري
- عضو مجلس النواب بشرى القيسي
- عضو مجلس النواب السابق محمد الصيهود
- وكيل وزارة النفط لشؤون التوزيع علي معارج
- إبراهيم الصميدعي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80218" target="_blank">📅 15:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80217">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
وكالة الأنباء العراقية:
اعتقال 47 متهما من نواب ومسؤولين بتهم فساد.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80217" target="_blank">📅 15:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80216">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌟
هيئة النزاهة العراقية تعلن مباشرة إجراءاتها الحازمة بصدد تنفيذ مذكرات القبض القضائية الصادرة بحق عدد من المتهمين بالتجاوز على المال العام</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80216" target="_blank">📅 15:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80215">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🌟
هيئة النزاهة العراقية تعلن مباشرة إجراءاتها الحازمة بصدد تنفيذ مذكرات القبض القضائية الصادرة بحق عدد من المتهمين بالتجاوز على المال العام</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80215" target="_blank">📅 15:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80214">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جلسة طارئة لمجلس الوزراء العراقي مساء اليوم في أعقاب حملة مكافحة الفساد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80214" target="_blank">📅 15:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80213">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وكالة الأنباء العراقية: حملة ملاحقة المتهمين بملفات فساد مستمرة وممتدة</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80213" target="_blank">📅 15:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80212">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الافراج عن كامل المتظاهرين ضد الكهرباء المعتقلين في محافظة واسط</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80212" target="_blank">📅 15:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80211">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32cc1d8976.mp4?token=n4QQ2k2_sBzm0HFGLMUp_alKjAN-dMZdFuDStqCSAFbI6C6UOil0CQ3D88q-fHDti0OxSzpewZvG8pRij5wYy2jKDOZPWyagn8o51CQAWPkZbkSeQQtjSpvvx3_FGUblS9CC69kzhLK1JQDv8Pv5ux6dnSJdDQ3Us7ypxfqDEuBiqHfhI4aFqL8C2ryvo0YHKiPn_IRpjKvMcz0vepuRx25TOQGSPi5q7eYCDqff9oOUZKNiMX4gWyxw3TMaIns-2d1w3WSF_WRJY2KX3Cn_0ky9Qaav6S-7UgasULZGHH22YXzt4jEHqkhh28pArZQIPm6G1hgAhh_xGXRVVA82Iq8OMXKWttHIRQXWwjlkCinIN6R_mcu8o8S1HuUn2sR6FFeBfDJ5wIkxDxAlbKFT72Cf41kkDv7MIPw_C-V9AHrBTXK5Ce5USgqxLSk3Rk-i1oZcAC7svzvHXzidbNu0d37bHdVSA8ek89Vsd0mGFGAqPaCPAnZkDcJxUsNxntz_vo-cnWdZ0LemWmAxwDYWKHlYMa0Q9CrzGIfo-GhxXnVrnySro829wtQ6t3hnN3y38at6ypmBu6QwcIb_hJPS89KmvFoDRpzONetY7Rb0hzlqBfG0a1K61IeayFrCbH7fLAyieHQ0EuwS2B-jVCKAnjcCsokmsPaydDxLjilP-0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32cc1d8976.mp4?token=n4QQ2k2_sBzm0HFGLMUp_alKjAN-dMZdFuDStqCSAFbI6C6UOil0CQ3D88q-fHDti0OxSzpewZvG8pRij5wYy2jKDOZPWyagn8o51CQAWPkZbkSeQQtjSpvvx3_FGUblS9CC69kzhLK1JQDv8Pv5ux6dnSJdDQ3Us7ypxfqDEuBiqHfhI4aFqL8C2ryvo0YHKiPn_IRpjKvMcz0vepuRx25TOQGSPi5q7eYCDqff9oOUZKNiMX4gWyxw3TMaIns-2d1w3WSF_WRJY2KX3Cn_0ky9Qaav6S-7UgasULZGHH22YXzt4jEHqkhh28pArZQIPm6G1hgAhh_xGXRVVA82Iq8OMXKWttHIRQXWwjlkCinIN6R_mcu8o8S1HuUn2sR6FFeBfDJ5wIkxDxAlbKFT72Cf41kkDv7MIPw_C-V9AHrBTXK5Ce5USgqxLSk3Rk-i1oZcAC7svzvHXzidbNu0d37bHdVSA8ek89Vsd0mGFGAqPaCPAnZkDcJxUsNxntz_vo-cnWdZ0LemWmAxwDYWKHlYMa0Q9CrzGIfo-GhxXnVrnySro829wtQ6t3hnN3y38at6ypmBu6QwcIb_hJPS89KmvFoDRpzONetY7Rb0hzlqBfG0a1K61IeayFrCbH7fLAyieHQ0EuwS2B-jVCKAnjcCsokmsPaydDxLjilP-0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متداول: قوة امنية عراقية تداهم منزل نائب سابقة متهمة بقضايا فساد في قضاء بيجي ضمن محافظة صلاح الدين.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80211" target="_blank">📅 15:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80210">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وكالة الأنباء السعودية: أسباب تحطم المروحية التابعة لشركة أرامكو غير معروفة والتحقيق مستمر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80210" target="_blank">📅 15:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80209">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
تحطم مروحية تابعة لشركة أرامكو السعودية في رأس تنورة، ومقتل 14 شخصاً</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80209" target="_blank">📅 15:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80208">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
تحطم مروحية تابعة لشركة أرامكو السعودية في رأس تنورة، ومقتل 14 شخصاً</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80208" target="_blank">📅 15:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80207">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
النائب ابو تراب التميمي:
- إذا صارت الإجراءات فقط في ملف عدنان وأُغلق هذا الموضوع من دون فتح ملفات أخرى في وزارة النفط ووزارة الكهرباء وبقية الوزارات، فسنعتبر أن الموضوع كان مستهدفاً فيه السيد السوداني
- الحملة يجب أن تشمل أيضاً مشاريع وعقود الحكومتين السابقتين (الكاظمي، والسوداني)، كثيراً من الشخصيات متهمة بالفساد، وليس موضوع عدنان وحده، من الضروري ألا يُنظر إلى الإجراءات على أنها استهداف لكتلة سياسية أو لشخصية بعينها
- يجب فتح ملفات في وزارات الإسكان والإعمار والتجارة والصناعة إضافة إلى مديرية الطرق والجسور،  هذه المؤسسات تحيط بها الكثير من ملفات الفساد
- استمرار غلق ملفات الفساد أو تسويتها سيؤثر في مصداقية النظام السياسي والعملية الديمقراطية، تدعو رئيس الوزراء إلى إعلان نتائج التحقيقات بشفافية وعدم التهاون مع أي مسؤول، بغض النظر عن انتمائه السياسي أو الجهة التي تدعمه
- أموال الدولة هي أموال الشعب وإن حمايتها تتطلب التعامل بحزم مع جميع ملفات الفساد وعدم السماح لأي تفاهمات أو اعتبارات سياسية بعرقلة عمل القضاء والأجهزة الرقابية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80207" target="_blank">📅 15:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80206">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇫🇷
11 قتيلا بحصيلة أولية لتحطم طائرة مدنية في نانسي شرقي فرنسا</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80206" target="_blank">📅 15:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80205">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA6amF5rGBEzId8BPtYcDPbN4C4jxW76QdifTOqjPDsv1wasz3oBPw3sXDx5m3ZzwQuFwQIm2jejld4Z2PIDxspZInae-T7rw8OYrQKQAk7uCcmdxO2k8vbxB40L8MUFEMMZ4JIE94mw1_XouSjqZKMz3XneUvFSqXmLuRTOoK6rCJVJlB-3ayokEFECRbnVC3QOgMzFSbz2jnCAxADV55rtn88T1islVfeltsVNhWHtAnrr9I2Mtn3UA9gqd2kfT4eUn9Lyh3NNoSaWoRw76oc2CgAirvVuoUufiq4s1Jp9my4ouJJ9_R4zsFY1cULNSdxiLhJ0UosblDenEcCzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متداول / صور من منزل عالية نصيف</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/80205" target="_blank">📅 14:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80204">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رصد تحركات امنية عراقية في محافظة الديوانية جنوبي العراق لاعتقال عدد من المسؤولين المتهمين في قضايا فساد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80204" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0q43_LNU__tCqZGDTcX9pNdwOqTWRLZGBAu_Z_s8kbMk7iM0SW-kPaKe44MhgPsjRov2c_9080NdZRJWLVUne10ZWkRaBTBgpz71tAILz5PXOz9Ex8fiTNteCHk1s35IbqdTliNRoIJ9qJQ9WK37FIm4upgaYmC2riy_HLBG_HdXeyN8pxBDmn0cE6sj-U_IoDtT9vocX2OtwoDEtiHCl9xnsAr5qtwOJykSQokyFu2scevw55OuTlak03y0gOqXuLZwNAMvquyqhegOc_DgtaCpryoI6ym6zGIsZKdfy9wV2-FBd0XyTk34T05pO0Ug32-caQPSzaYs09ccOtLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بيان لوزارة الكهرباء العراقية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80203" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80202">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d65330312.mp4?token=RS0A2wAmlfLqj-e2k6xE8cqU2gTGGtMNvAGVG9gzRw9wVPAF52UvvClir8foJxCqEjBq1pLCMfxkvidsZCHXbQO_biEf5rWn2tjB-LgKBgvtnct_HroGB9HEq-WMuMFPkpsPgqMy9TfoleJtEwF-awsOtY_FbhO93jJzJNIG81W4hetPbB5UkZrU4xw-dXQ2H8HQ0McK6Zv46QdnEStZyrrFDNWsBu2cNd5AL9MGIDzeAmbrcLwyy3Os7t-YQO4G0RLGxog8O8uXC5P2CpghUFAh8JP5ES3hVybw_SvqGOXi6Q3YEZJ3FPEW4M1PeqlkqvjIeZg7yVBe0i_1-M_LMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d65330312.mp4?token=RS0A2wAmlfLqj-e2k6xE8cqU2gTGGtMNvAGVG9gzRw9wVPAF52UvvClir8foJxCqEjBq1pLCMfxkvidsZCHXbQO_biEf5rWn2tjB-LgKBgvtnct_HroGB9HEq-WMuMFPkpsPgqMy9TfoleJtEwF-awsOtY_FbhO93jJzJNIG81W4hetPbB5UkZrU4xw-dXQ2H8HQ0McK6Zv46QdnEStZyrrFDNWsBu2cNd5AL9MGIDzeAmbrcLwyy3Os7t-YQO4G0RLGxog8O8uXC5P2CpghUFAh8JP5ES3hVybw_SvqGOXi6Q3YEZJ3FPEW4M1PeqlkqvjIeZg7yVBe0i_1-M_LMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات سوات العراقية تعزز انتشارها في قضاء الحي ضمن محافظة واسط بحثا عن عدد من الشخصيات المتهمة في قضايا فساد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80202" target="_blank">📅 14:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80201">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
جهاز مكافحة الارهاب العراقي:
نتبع أوامر القائد العام للقوات المسلحة في تنفيذ كافة العمليات لحماية العراق ومصالح شعبه.. سنبقى منتصرين بوحدتنا في مواجهة الإرهاب والفساد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80201" target="_blank">📅 14:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">توقيف الإعلامي حيدر الحمداني في كربلاء المقدسة بعد شكوى رفعتها العتبة العباسية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80200" target="_blank">📅 14:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80199">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">البرلمان العراقي: أمر رفع الحصانة عن المعتقلين وُقّع رسمياً خلال الساعات الـ48 الماضية بالتنسيق مع مجلس القضاء الأعلى</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80199" target="_blank">📅 14:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80198">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رصد تحركات امنية عراقية في محافظة الديوانية جنوبي العراق لاعتقال عدد من المسؤولين المتهمين في قضايا فساد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/80198" target="_blank">📅 14:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80197">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
بعد دقائق، رسالة لقائد الثورة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80197" target="_blank">📅 14:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80196">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
بعد دقائق، رسالة لقائد الثورة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80196" target="_blank">📅 13:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80195">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9a1341dc.mp4?token=dIJ_WCZoIuNFJoB9DizBlki4tIAlicvpnOmQRLogz7o_E0_caYW8OR74NNbTyaqV54fN03iU-PHX4Lcsf0XILJKUE-A1kfgx34fXw3IxsdiamCs2_pP7BOVOR0h_lLmbMt8yG8HtEFkkcy5H_XK6X5VlVoFGmQYkX3pHTWBuouVFVbUhssadhzY01R1o-vuQn2h3G9X1tsSUfntLGHHZenBLOyRVtImU53HnGXVPX-i6kjs2k2v8gA_4vP_dyL_d-TtxEz4jp1d_Z1bRMWWtROHG1Xr2TvZqGrKTKEPSmxZg6IP6TMulZ7m1Yi9_gmuv4Eyg7nshc2L9sur8zKzePw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9a1341dc.mp4?token=dIJ_WCZoIuNFJoB9DizBlki4tIAlicvpnOmQRLogz7o_E0_caYW8OR74NNbTyaqV54fN03iU-PHX4Lcsf0XILJKUE-A1kfgx34fXw3IxsdiamCs2_pP7BOVOR0h_lLmbMt8yG8HtEFkkcy5H_XK6X5VlVoFGmQYkX3pHTWBuouVFVbUhssadhzY01R1o-vuQn2h3G9X1tsSUfntLGHHZenBLOyRVtImU53HnGXVPX-i6kjs2k2v8gA_4vP_dyL_d-TtxEz4jp1d_Z1bRMWWtROHG1Xr2TvZqGrKTKEPSmxZg6IP6TMulZ7m1Yi9_gmuv4Eyg7nshc2L9sur8zKzePw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات من بغداد تنتشر في محافظة واسط لتنفيذ عمليات الاعتقال</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80195" target="_blank">📅 13:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80194">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/836431c75f.mp4?token=d0L4jTJtS2ZBlMsr07W1pxnN_9D5VVKS7SVShGPXWCzV1z7Qy-j4dgg_HfWb9ym_EU1lF3tJFDLW_LyMQieqBlcGzOQ10FZwhmmSeJgOTw4Aw_pPG4vVPEJw40mEkscuq_yYTw8FwC2cXs7Q8OVNhPY9RU_GCjXaTfEOw4gBztBryXVd-CMlBjqrzlyPOIIXyFtd6iYV7gTatdEakL0geKn7Kj0BZa4HbQOUr4Y6IMgQIp9wbrDFesSc5wnnyry-scXlYhOpCie4V2dV9gRDzAg09hZAWq_pEN1AEm6sBusFxqaqnPNtwAEOfQF-W3yDSDBEJ1wjR_q3zuaz1YI3MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/836431c75f.mp4?token=d0L4jTJtS2ZBlMsr07W1pxnN_9D5VVKS7SVShGPXWCzV1z7Qy-j4dgg_HfWb9ym_EU1lF3tJFDLW_LyMQieqBlcGzOQ10FZwhmmSeJgOTw4Aw_pPG4vVPEJw40mEkscuq_yYTw8FwC2cXs7Q8OVNhPY9RU_GCjXaTfEOw4gBztBryXVd-CMlBjqrzlyPOIIXyFtd6iYV7gTatdEakL0geKn7Kj0BZa4HbQOUr4Y6IMgQIp9wbrDFesSc5wnnyry-scXlYhOpCie4V2dV9gRDzAg09hZAWq_pEN1AEm6sBusFxqaqnPNtwAEOfQF-W3yDSDBEJ1wjR_q3zuaz1YI3MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية العراقية تنتشر في قضاء الحي ضمن محافظة واسط لاعتقال عدد من الشخصيات المتهمة في عمليات الفساد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/80194" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80193">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f7136922.mp4?token=ApZQEuACg7HXmEkzNMHq-SMkxTZjKOnOd9IdLupkxwFt88xdk6X_ERv3Jwrrk6ol-KKsTlUMCPqV8HYVV2fSK4oJPIboZw9l8mtwbHKJUN28g1n2waoGayp19FAhRQPIYxvKlJuJKVg-s04D4Clfr8NyrPgxtM3p28ZJRv4eSgsjeP2IZgtAZ4J4iZcQMrA0b9jx4YfHFJ97O7lPwgd2k74tlX81dwxySObJxAmDz9IYufo5Qex8OShfRHQiN_6Gj-g1S83pUoB82HxVrc-lWUuiEJi8Z04G_hl730kvfPNgkz_HKriLi9J530gh10_ncRqZkJcTSsldn5iRGes10A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f7136922.mp4?token=ApZQEuACg7HXmEkzNMHq-SMkxTZjKOnOd9IdLupkxwFt88xdk6X_ERv3Jwrrk6ol-KKsTlUMCPqV8HYVV2fSK4oJPIboZw9l8mtwbHKJUN28g1n2waoGayp19FAhRQPIYxvKlJuJKVg-s04D4Clfr8NyrPgxtM3p28ZJRv4eSgsjeP2IZgtAZ4J4iZcQMrA0b9jx4YfHFJ97O7lPwgd2k74tlX81dwxySObJxAmDz9IYufo5Qex8OShfRHQiN_6Gj-g1S83pUoB82HxVrc-lWUuiEJi8Z04G_hl730kvfPNgkz_HKriLi9J530gh10_ncRqZkJcTSsldn5iRGes10A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية العراقية تنتشر في قضاء الحي ضمن محافظة واسط لاعتقال عدد من الشخصيات المتهمة في عمليات الفساد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80193" target="_blank">📅 13:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80192">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">القوات الامنية العراقية تداهم منازل وزير الكهرباء السابق زياد علي فاضل وتعتقل عدد من اشقائه.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80192" target="_blank">📅 13:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzOMLiiU5B9yhxh1fnKRg8fZC51hrBLq31zbyHLoEAQlCJPXYA5WXaTHrDhxKIV87GQ1wyOgKg_spNjRKKXXADY5ow5jqsYT4c3Kl-Vu06TiS08zwApSP4Amd13lGGApB57G5LwVdNp5G7xihzYKk7HH9sC9gIewXYNPhlsBU7anQCHAR9sfLX8BgOr9Q-N0n0NeOu4DyW2atjdbYkGqoiA9Qfv5Ji3qCqiJD-QG7IDr1681HdQmBBSUFw1OOgNmWMbXmnfpebrSpTJoE6J-C0Ur1h5TUSO0rAbiVoa0B5iU5MirV-zUnJYmmQhkP8QkcEaIrO2J9UVT6190EaZK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش الاحتلال يعلن مقتل جندي في جنوب لبنان يدعى ديفد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80191" target="_blank">📅 13:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80189">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4420469c23.mp4?token=PLWnWDbsPeIRl4gdFOPK1QwIlyaRE4tykLwF1V-bXOa0mC5-1AIPWeAXNB_S0cluHXeTJZ5W1UoFZ6DjcQw8LncDjar3l_WgJaadEFzPCxxjTx52TU-SUwlWbJY3ldp-R8ui94XPSMGbvBOrICo9WjjVGLtqTUiw40IDAaBfNPcHSIP_LaK3FJf-O8iQzSzjgHbPvfbvpECrMv0LEoBt4r0baIdW3NLER5t66-JWqSw2FD4oP9W2nvHin3C9P3d_tyy1VPWg7cwbro2Jz9SRfsYB4Q9SsJEpJknpoAZ3XeW_DnBQkrIV2u1N15P4bfUO5NTgXsLOaEtogPJbYxC0AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4420469c23.mp4?token=PLWnWDbsPeIRl4gdFOPK1QwIlyaRE4tykLwF1V-bXOa0mC5-1AIPWeAXNB_S0cluHXeTJZ5W1UoFZ6DjcQw8LncDjar3l_WgJaadEFzPCxxjTx52TU-SUwlWbJY3ldp-R8ui94XPSMGbvBOrICo9WjjVGLtqTUiw40IDAaBfNPcHSIP_LaK3FJf-O8iQzSzjgHbPvfbvpECrMv0LEoBt4r0baIdW3NLER5t66-JWqSw2FD4oP9W2nvHin3C9P3d_tyy1VPWg7cwbro2Jz9SRfsYB4Q9SsJEpJknpoAZ3XeW_DnBQkrIV2u1N15P4bfUO5NTgXsLOaEtogPJbYxC0AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انفجار سيارة مفخخة في حولون بتل أبيب</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/80189" target="_blank">📅 12:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80188">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa677b1f6.mp4?token=LsRYyf0TH5qCFK5oi__gce7KmLthbwqS88JGgDGvJeqW1nQnootfa_Jn-d503pB2hGo4iB5SLIdnie7K0mWa4TgSztobtVXb61Nx5ADMiP5EORij2C7gXV-lewF4ffBlgtwea8n66pochd6wRnUUiinosRB0QWZ-JbBD_iZWX0Axp9n5gj8WRjgeELZZV88fKT5Y0SraCdGLfcN-TnZTAjQzq5B9_BUyKdsXybSwZj-SuwLgae07vIXu5DKM3FZIi6DEi4ux2e2lmOR4H8O07E4-777ZPWccT-02WfACVMuvXTf_3OyU7I6ALapgfLLmvYpYxGSSE1-7sQqvn1Wgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa677b1f6.mp4?token=LsRYyf0TH5qCFK5oi__gce7KmLthbwqS88JGgDGvJeqW1nQnootfa_Jn-d503pB2hGo4iB5SLIdnie7K0mWa4TgSztobtVXb61Nx5ADMiP5EORij2C7gXV-lewF4ffBlgtwea8n66pochd6wRnUUiinosRB0QWZ-JbBD_iZWX0Axp9n5gj8WRjgeELZZV88fKT5Y0SraCdGLfcN-TnZTAjQzq5B9_BUyKdsXybSwZj-SuwLgae07vIXu5DKM3FZIi6DEi4ux2e2lmOR4H8O07E4-777ZPWccT-02WfACVMuvXTf_3OyU7I6ALapgfLLmvYpYxGSSE1-7sQqvn1Wgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انفجار سيارة مفخخة في حولون بتل أبيب</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/80188" target="_blank">📅 12:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نايا - NAYA
pinned «
مصدر لنايا   اعتقال ٣٧ شخص ؛ ٢٥ شخص داخل المنطقة الخضراء ، ١٢ خارج الخضراء .
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80187" target="_blank">📅 12:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
جيش الاحتلال الإسرائيلي سمح بالنشر: مقتل جندي صهيوني إثر اشتباكات عنيفة مع حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/80185" target="_blank">📅 12:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fd2512544.mp4?token=AN1umLQdgkc0Enf_Lyp1TeNcdQkLoopxmMjDR8FIypH15hYMh2s0iVwG34QYjkxSrOvn4H0mUH_zQnDIy263FavPCEUq_HXOSUp73-DY-7T7ea3OTtTLC3FTgy_1eBmqlyDpZ2EMWOOffvnIdxX2hKQN_6LY-jEmwvuUUpVSm9s4OpiDZugEaI38lgV_y6UF75f8BtETORp4lD2vXTwyC5V0KOIVyToLBVg4ohRpCpvsHOmBRNNi1D3ImeDlO3_ZBYUf2UjdbHaewOaZt6X2tNXrULiZ4oKOH_qCSyV3ueDDtFlN02HNFornXEG2sKcTZBl1HdooJtyvqJsmo0iF3GQBN2kjGuCMPihGFeTVY3cOA1rjrR0ulrZl5ye3cK_9vkwArJmUMkot1mMqZeNqaHrmi1VSlTdPIcKhFUZHlJr_Mdd0AtQGwk0AQ5ph_dkN15k1NFu3NGFaOsRFIDcpeP57RD5juKB8SIfg3w80MtKSWn0zC2zrfNyrjAdI2hq1d7lUzTOZyYfel0rFcYlywTGBpmloOp9-AfVaM7w3yp-Z4T23NJ7CvzmgTXjgwzj0faJ5Ah9CdcGDIZ0ELSkzfnkVMtbt2-hCtFEaC7rvGZOBjUwOcdEVYXidu-0IJ9GApZMy0fju66v1toYiRhOkBzRz5am5tQfpLgoqM_Sqc90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fd2512544.mp4?token=AN1umLQdgkc0Enf_Lyp1TeNcdQkLoopxmMjDR8FIypH15hYMh2s0iVwG34QYjkxSrOvn4H0mUH_zQnDIy263FavPCEUq_HXOSUp73-DY-7T7ea3OTtTLC3FTgy_1eBmqlyDpZ2EMWOOffvnIdxX2hKQN_6LY-jEmwvuUUpVSm9s4OpiDZugEaI38lgV_y6UF75f8BtETORp4lD2vXTwyC5V0KOIVyToLBVg4ohRpCpvsHOmBRNNi1D3ImeDlO3_ZBYUf2UjdbHaewOaZt6X2tNXrULiZ4oKOH_qCSyV3ueDDtFlN02HNFornXEG2sKcTZBl1HdooJtyvqJsmo0iF3GQBN2kjGuCMPihGFeTVY3cOA1rjrR0ulrZl5ye3cK_9vkwArJmUMkot1mMqZeNqaHrmi1VSlTdPIcKhFUZHlJr_Mdd0AtQGwk0AQ5ph_dkN15k1NFu3NGFaOsRFIDcpeP57RD5juKB8SIfg3w80MtKSWn0zC2zrfNyrjAdI2hq1d7lUzTOZyYfel0rFcYlywTGBpmloOp9-AfVaM7w3yp-Z4T23NJ7CvzmgTXjgwzj0faJ5Ah9CdcGDIZ0ELSkzfnkVMtbt2-hCtFEaC7rvGZOBjUwOcdEVYXidu-0IJ9GApZMy0fju66v1toYiRhOkBzRz5am5tQfpLgoqM_Sqc90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
‏وزير الخارجية العراقي: أشكر نظيري الإيراني الذي كان يضع الحكومة العراقية باستمرار بشأن الحرب والمفاوضات  غلق مضيق هرمز كان سبباً من أسباب عدم تصدير النفط العراقي وقد كان له أكثر كبير على الاقتصاد  سنزور طهران لتكملة المحادثات</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/80184" target="_blank">📅 12:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00e129455.mp4?token=JMHli7LcFzZwD9cV-Nt_n6hIlUJ9lhxgx547C-JX4OsRLcn_UUWbBXuGgZpkk64RfMnYfARzWWmwSvobq3Byixpue0tkSGAzMv_igvzlKb86FAKnUhfP77bV5JifhDSQLdq2-Eqxygn3Rct3mL-VpZyw5vzWs_KHjTElMHyIi_RFY_TgbjztKEuCQ9gMRAYIG0JTdT7B98i0tc2tALA0ntVR40jQAyZIbWzcJtRtcPU30TUJLmVIqcMbUoVu_0SCRPfA9b5fliVF8nxFbi16RcwRN87cEnaOh8h-sxLry8L--eCNyHY6hkKXqNnZCrzgg5sZcD_-VvI74U2SVRKpF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00e129455.mp4?token=JMHli7LcFzZwD9cV-Nt_n6hIlUJ9lhxgx547C-JX4OsRLcn_UUWbBXuGgZpkk64RfMnYfARzWWmwSvobq3Byixpue0tkSGAzMv_igvzlKb86FAKnUhfP77bV5JifhDSQLdq2-Eqxygn3Rct3mL-VpZyw5vzWs_KHjTElMHyIi_RFY_TgbjztKEuCQ9gMRAYIG0JTdT7B98i0tc2tALA0ntVR40jQAyZIbWzcJtRtcPU30TUJLmVIqcMbUoVu_0SCRPfA9b5fliVF8nxFbi16RcwRN87cEnaOh8h-sxLry8L--eCNyHY6hkKXqNnZCrzgg5sZcD_-VvI74U2SVRKpF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
لحظة إطلاق صواريخ عملية الحسم الصاروخية والطائرات بدون طيار فجر اليوم من قبل قوات الفضاء الجوية والقوات البحرية للحرس الثوري ردًا على اعتداءات أمريكا.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80183" target="_blank">📅 11:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
🇮🇷
وزير الخارجية العراقي فؤاد حسين يستقبل نظيره الإيراني عباس عراقجي.
🔻
لمشاهدة أكثر اضغط هنا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/80182" target="_blank">📅 11:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مصدر لنايا
اعتقال ٣٧ شخص ؛ ٢٥ شخص داخل المنطقة الخضراء ، ١٢ خارج الخضراء .</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80181" target="_blank">📅 11:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4069bb51f.mp4?token=LQXpjQlMZdJBY1LQnCsKxChOCRAdA9MR5RpNFTK05_SMNVpQNbC_fopR2LE-YxpT-cVK2SljwoWOSnDPb2m-rVeENU7MVsAfHxRrgzUZoESbhbProIlhqluC9HDO0K_t7cKeGx3PuTJOgZr65K20z96KcnnKxwwFJmzOu5PcEe6VoY1rdNcTUhWJQkYSJBoYIv9gVEvbGkKvjJxbUH0z0ZZvQYO4W72L8UKESZ3uVtnrLL5QXahV_0BLhSAzo4x3bRg22n1GA9QP-p-jIC5S85Zwbqtp6W86ijUy2ST-yRHvqQ0yiON3IuiHOtGKZCZFjpGO9ShBgBcIUEUlKUZNCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4069bb51f.mp4?token=LQXpjQlMZdJBY1LQnCsKxChOCRAdA9MR5RpNFTK05_SMNVpQNbC_fopR2LE-YxpT-cVK2SljwoWOSnDPb2m-rVeENU7MVsAfHxRrgzUZoESbhbProIlhqluC9HDO0K_t7cKeGx3PuTJOgZr65K20z96KcnnKxwwFJmzOu5PcEe6VoY1rdNcTUhWJQkYSJBoYIv9gVEvbGkKvjJxbUH0z0ZZvQYO4W72L8UKESZ3uVtnrLL5QXahV_0BLhSAzo4x3bRg22n1GA9QP-p-jIC5S85Zwbqtp6W86ijUy2ST-yRHvqQ0yiON3IuiHOtGKZCZFjpGO9ShBgBcIUEUlKUZNCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سيد عباس عراقجي يزور محل استشهاد الحاج قاسم سليماني و الشهيد ابو مهدي المهندس قبل التوجه الى وزارة الخارجية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/80180" target="_blank">📅 11:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2b16e76c4.mp4?token=KfgM3BrXglaffQDy0QOSJWz8UIlIt8QMXE5-dulViZK3gkIGyXGb2x6p14jTf7nw8fWE_iEc03kwNwRByVt8gcm15q6w0c0XEwwNkdLmCSONVT-le6XAnRG75uyHfHizbiiAyBC28XC8hDRUbgfYtikWFjfiDRSjkEVFL34D2ZlYLZcMVYx0GGpQThDPhcBw8RK5p1RY3GAiS4kK1SQiZ5DE_0-cYJxTnJWvrTw8y710LdwnXvALSsmVB41kGS3COJqM1n4mPxcgVHit4MM8eorumrLaHSVhH_q0n_MzBpLx-5JNSXu0dFIBuJPVX5vmRBHWX8b3ML3EysrXaiD33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2b16e76c4.mp4?token=KfgM3BrXglaffQDy0QOSJWz8UIlIt8QMXE5-dulViZK3gkIGyXGb2x6p14jTf7nw8fWE_iEc03kwNwRByVt8gcm15q6w0c0XEwwNkdLmCSONVT-le6XAnRG75uyHfHizbiiAyBC28XC8hDRUbgfYtikWFjfiDRSjkEVFL34D2ZlYLZcMVYx0GGpQThDPhcBw8RK5p1RY3GAiS4kK1SQiZ5DE_0-cYJxTnJWvrTw8y710LdwnXvALSsmVB41kGS3COJqM1n4mPxcgVHit4MM8eorumrLaHSVhH_q0n_MzBpLx-5JNSXu0dFIBuJPVX5vmRBHWX8b3ML3EysrXaiD33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
مصفاة ياروسلافل الروسية تتعرض لهجوم أوكراني صباح هذا اليوم</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/80179" target="_blank">📅 11:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#ترفيهي
جوزيف عون يدين الاعتداءات الإيرانية التي استهدفت البحرين والكويت ويقدم حلاً للنزاعات كاعتماد الحوار والدبلوماسية.
طيب والاعتداءات الإسرائيلية على لبنان
‼️
ولا اسرائيل منا وفينا
😆</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/80178" target="_blank">📅 10:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اصوات انفجارات تهز الكويت الان</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80177" target="_blank">📅 10:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d313bb45.mp4?token=unLj5C6X44lecTYPGp46d3G1Cvba3ayyj_tXFDCCvbggzCQjyHglb0Cnvbzj9RO_bkIMRtpGcwBAslT5_9V0dKARTxnGh3TDuwauNwt09xuiThgvdBcLqdFwVaZU58Eib6xe_hYeezW23TpkSQMMCH_kOlpJLIGisNfjTHN42LOwAXDCza8cdghnEf7ZkmRcg0jPXXVCki9AYNJmz3-nEdP_InmGxOG-9-VcCO2gLRr3R_Li6FwzmRkwjMMG2_U7Gv2QXy79G2Qplgb73LDU8_PSg9zen9n5p1DMdAQamNRrt-GlIKNwitynOjhSdH175TXhUAz7p24M42_k7_A6HEPzHVBUyPZEK72xXxrP1P33TSYGTl9BeU7Vt0kPmiyxBrTmupPDjuSjDUTizsXY7n1lAnRmQu6M17s0iHwDW6HXBTUkyGpRdluoDlm5f478Dz2rkLCZ8UbYzbl-XmjLmhVCUEo3N4zgMjm592ZxHjfRRl4UhvG4D5UkeHo8v78iH2O8J0I85qbPhc8hqZ_cyaHqxd3BBprO_fFQ1VqkpHQ-gnsp7m8Ek5Hl5L16F2i0egIbzTEjkruccoi6Tcyh49PRmZ9O1GFNu4PWdx7_8H1z9s4GlZSdYKMTccTAjcGMXHorzcNkucG_VFGNGok8Q3C0foXBKDbGAj0QWWYnDRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d313bb45.mp4?token=unLj5C6X44lecTYPGp46d3G1Cvba3ayyj_tXFDCCvbggzCQjyHglb0Cnvbzj9RO_bkIMRtpGcwBAslT5_9V0dKARTxnGh3TDuwauNwt09xuiThgvdBcLqdFwVaZU58Eib6xe_hYeezW23TpkSQMMCH_kOlpJLIGisNfjTHN42LOwAXDCza8cdghnEf7ZkmRcg0jPXXVCki9AYNJmz3-nEdP_InmGxOG-9-VcCO2gLRr3R_Li6FwzmRkwjMMG2_U7Gv2QXy79G2Qplgb73LDU8_PSg9zen9n5p1DMdAQamNRrt-GlIKNwitynOjhSdH175TXhUAz7p24M42_k7_A6HEPzHVBUyPZEK72xXxrP1P33TSYGTl9BeU7Vt0kPmiyxBrTmupPDjuSjDUTizsXY7n1lAnRmQu6M17s0iHwDW6HXBTUkyGpRdluoDlm5f478Dz2rkLCZ8UbYzbl-XmjLmhVCUEo3N4zgMjm592ZxHjfRRl4UhvG4D5UkeHo8v78iH2O8J0I85qbPhc8hqZ_cyaHqxd3BBprO_fFQ1VqkpHQ-gnsp7m8Ek5Hl5L16F2i0egIbzTEjkruccoi6Tcyh49PRmZ9O1GFNu4PWdx7_8H1z9s4GlZSdYKMTccTAjcGMXHorzcNkucG_VFGNGok8Q3C0foXBKDbGAj0QWWYnDRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
وزير الخارجية الإيراني عراقجي يصل إلى العاصمة العراقية بغداد ‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80176" target="_blank">📅 10:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098c093505.mp4?token=RSurP7j4vaf7Kk8vBZWpft7MeEhgbRIlGjh6kk_h2hfKQ8ZllWj9Zn8LHb747fBBvVo4UKnOGL4d4VYf3WoGs_a3fKf4JNrZU4HuCk8JoFl2-Rxlc0lbu9x2juWl7RWcoflbAc5vbcfxUIIinhYjMjR7T24FFOEShBym8BXA8K4W-n6_o1trcUceiSDs8Lf7OrXjjf52IyBlXoCxesYdTAkQ0Qs_DJEv2tjL9XzUx5Tsh5rKKr3WpKj9QVwEPyBLhALUuKNgsp-31JR_gwVDtCkV5AU0hg3CgQpZ9vP4RNFUirxLg3qgKY2rMQIhZiHXs_403OUeYuSsfUTA6RgrRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098c093505.mp4?token=RSurP7j4vaf7Kk8vBZWpft7MeEhgbRIlGjh6kk_h2hfKQ8ZllWj9Zn8LHb747fBBvVo4UKnOGL4d4VYf3WoGs_a3fKf4JNrZU4HuCk8JoFl2-Rxlc0lbu9x2juWl7RWcoflbAc5vbcfxUIIinhYjMjR7T24FFOEShBym8BXA8K4W-n6_o1trcUceiSDs8Lf7OrXjjf52IyBlXoCxesYdTAkQ0Qs_DJEv2tjL9XzUx5Tsh5rKKr3WpKj9QVwEPyBLhALUuKNgsp-31JR_gwVDtCkV5AU0hg3CgQpZ9vP4RNFUirxLg3qgKY2rMQIhZiHXs_403OUeYuSsfUTA6RgrRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
وزير الخارجية الإيراني عراقجي يصل إلى العاصمة العراقية بغداد ‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/80175" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80173">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇰🇼
🇧🇭
الكويت والبحرين: ندين تكرار الاعتداءات الإيرانية "الآثمة"</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/80173" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80172">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN0c1-Ap2nQUicUrEhFyy6FRmAYFaj6UOecheIrsX7AAhOyYaOEWbfyloFvuWUEIEZOp3rnyqWJoCTFBb7gMGD9DR6RdcyH7EIywGykZ31S9iU8L8lrna4e6cmgXdCsIFgITdHgUS7pGZICKXjF6Z3iiIzsCkFafGhZGCZAYO_8knNA9-YdUBd3Nb6tx07VX0NG7q5nJMLHCtY5E0jd-Y8Mzw0hIoLL0azMM17RE83xrofCCFqrDrAt85_zqpc_9pFgQYyZWS1Wh_VtqI97Tth0aWvYerpoaCPmMkxdP8Y3kd04t4a3wguKMObjJ6XyDn_QPaKOI_yYsIwtp1RowFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: قد يأتي وقت لا نكون فيه قادرين بعد الآن على التصرف بعقلانية، وسنُجبر على إنهاء المهمة التي بدأناها بنجاح كبير عسكريًا.
إذا حدث ذلك، فلن تعد جمهورية إيران الإسلامية موجودة!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/80172" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
وزير الخارجية الإيراني عراقجي يصل إلى العاصمة العراقية بغداد ‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/80171" target="_blank">📅 09:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc28dca857.mp4?token=UjVV33miE_N5M_2lrxKFrBcoh3-xHSPFGm1CkBdxaEuNKl82I4i98AiMum4WeQLiUnYDIul2pGZ97m90MBYv3Br1EtrXImu5QP08DuNDdlNkx8vUZIBZdV6pQj2ry73uvjoSrhZBdQymUqYCTJNz5fFVWL1Rk2vTxTWxLfPAVGlSpfy1e68J3z15uyFasR4XixnZfosMuVajF3fQOqUAPB3qxlfGIoJxQgIXmlWD2ZNW5UL1T_SThy2NPV8WQWQuexGaan5eZmcPs8iMUgJsfRzTvj0WDuTtYqpDW8HIPxbj7Xwdeqj7q8gHkrUdIw74jd9qnyHHa1vs_lrNi8zkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc28dca857.mp4?token=UjVV33miE_N5M_2lrxKFrBcoh3-xHSPFGm1CkBdxaEuNKl82I4i98AiMum4WeQLiUnYDIul2pGZ97m90MBYv3Br1EtrXImu5QP08DuNDdlNkx8vUZIBZdV6pQj2ry73uvjoSrhZBdQymUqYCTJNz5fFVWL1Rk2vTxTWxLfPAVGlSpfy1e68J3z15uyFasR4XixnZfosMuVajF3fQOqUAPB3qxlfGIoJxQgIXmlWD2ZNW5UL1T_SThy2NPV8WQWQuexGaan5eZmcPs8iMUgJsfRzTvj0WDuTtYqpDW8HIPxbj7Xwdeqj7q8gHkrUdIw74jd9qnyHHa1vs_lrNi8zkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القطعات الأمنية العراقية تنتشر على طول طريق مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/80170" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامب: إيران لن تمتلك أبدا سلاحا نوويا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/80169" target="_blank">📅 08:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5b7076fa.mp4?token=k8JvIfNXViqiZ8RujGZEsZ1n6QUAgz1sgNw5H0FiEhWrqlHAXjtFpVxhc3NmjylNCE0OP5MYrw_F4504HFeFG4NVf15Z3H7As9YJHghwsx8kfzh86l9eKjKlCFh1spfy4vOJS7TEHVSAFpcDXaW5b-WdpEaQjT0q8Ri2fATz1V6gIjUffr-cqDNeUXTtYGuK_xqqyCJLmuVNDAK0EcoOjmkueu631gfIKx8Qj-dkxfilxBU7jy245Zu8YLQ3l2nj7kdEr4FT1H0u7Iv55s7IbY8r5zloD4hSnZ-K2kzq08eq2ljEuswh1qIZ0CBjUIAEBx-OiVg_W2yakw1o2Q9kZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5b7076fa.mp4?token=k8JvIfNXViqiZ8RujGZEsZ1n6QUAgz1sgNw5H0FiEhWrqlHAXjtFpVxhc3NmjylNCE0OP5MYrw_F4504HFeFG4NVf15Z3H7As9YJHghwsx8kfzh86l9eKjKlCFh1spfy4vOJS7TEHVSAFpcDXaW5b-WdpEaQjT0q8Ri2fATz1V6gIjUffr-cqDNeUXTtYGuK_xqqyCJLmuVNDAK0EcoOjmkueu631gfIKx8Qj-dkxfilxBU7jy245Zu8YLQ3l2nj7kdEr4FT1H0u7Iv55s7IbY8r5zloD4hSnZ-K2kzq08eq2ljEuswh1qIZ0CBjUIAEBx-OiVg_W2yakw1o2Q9kZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القوات الأمنية تنتشر في مدينة الصدر شرقي العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/80168" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80167">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36264bd695.mp4?token=sCudE2j237Vh1fYr5GD2BS1J4uYGXFHOiBpavDwC6LA-KK_Bb61l-dWx0r3baqYEQE6AMLPLU1CzdZMEJBCEBsohq12m5Xi1yhAweY0PtoWh8t_lBbqHIlCmMKKdcfLcqp1Q8OrZNNtxvTyVLgH3WRQiQr_lCSpVkvlNNeBjLn3wHG-CeHuFjZTmt9BbNwD92GcFBh8WpWiI1suH28PoSM4oe695kO72A8za20UwVTqUhAEAxc40U7eKItbxWqZv6cQpr5abDfKNxLYlFlohEykpV-Ns2KhhtxLbDfdQ1vs1_F9tgxmZg3q6_GZUYozHNftHdrd0Xla4szHvzYeCU3bZGB-Odewa6amsZMnGLBah5G9B00L_d4kz-yX0hLo3RZQVSUrF9t83qnFwnC5Vlap9RqY5LsMLaF-dfwyaonX0tsETT04-szHTSHUp0oxMO7aV7ybDW8Ex89x3IF1htfjkHQtTvYkXP9OSinapO5LMBWDgiY5cSwaguAYokk8VqDMHb1ObwzViiGuS8RJT_jA4VWXyowazDsCL5eBJAf-5mcqXS4SJaxjRTjQSL-7LCmIQQXLCm281BLpFLzffxRMG66VhQxlWrKorkOI9xDOE9jjfv5mjBZ59MbKz7WTWWtZYdqbLL3iad3QbSV-PrQMA_VPmu1Zaw8Yqt9rLsR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36264bd695.mp4?token=sCudE2j237Vh1fYr5GD2BS1J4uYGXFHOiBpavDwC6LA-KK_Bb61l-dWx0r3baqYEQE6AMLPLU1CzdZMEJBCEBsohq12m5Xi1yhAweY0PtoWh8t_lBbqHIlCmMKKdcfLcqp1Q8OrZNNtxvTyVLgH3WRQiQr_lCSpVkvlNNeBjLn3wHG-CeHuFjZTmt9BbNwD92GcFBh8WpWiI1suH28PoSM4oe695kO72A8za20UwVTqUhAEAxc40U7eKItbxWqZv6cQpr5abDfKNxLYlFlohEykpV-Ns2KhhtxLbDfdQ1vs1_F9tgxmZg3q6_GZUYozHNftHdrd0Xla4szHvzYeCU3bZGB-Odewa6amsZMnGLBah5G9B00L_d4kz-yX0hLo3RZQVSUrF9t83qnFwnC5Vlap9RqY5LsMLaF-dfwyaonX0tsETT04-szHTSHUp0oxMO7aV7ybDW8Ex89x3IF1htfjkHQtTvYkXP9OSinapO5LMBWDgiY5cSwaguAYokk8VqDMHb1ObwzViiGuS8RJT_jA4VWXyowazDsCL5eBJAf-5mcqXS4SJaxjRTjQSL-7LCmIQQXLCm281BLpFLzffxRMG66VhQxlWrKorkOI9xDOE9jjfv5mjBZ59MbKz7WTWWtZYdqbLL3iad3QbSV-PrQMA_VPmu1Zaw8Yqt9rLsR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من تحرك القطعات الأمنية بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/80167" target="_blank">📅 08:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80166">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxCs5y5WufK8XuifOTPoSmIsjHx2jdGqtAR_XNjSkVvlhRF0mvL35zvuJ9vsGRDIOI1T-BOjEkoVfipdLc8y5s3B3ylfQKBSqoJT7GbwFoHcqJtD4OKZMnEY23tvZ2aTeFG_HVcueitILQdjDux3SGgLvc8-0E6cusmzpWhfO8SFdH5LeQKTlVKi1chy2XBOi9fBjuMmiE7IoE7JI58LajQL_tj1j45EXGZs_w6J1GjNYRfg8EwiIYSbkxqcX03A5w5OLta68DhrISsnEsDQ1H0lgw5OWOfrkgFWJFtV86ck87Y1VNmvJdsXZ0sXjoFsxDDd3Q9ZUeMNWxOfg2wdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
تدين وزارة خارجية الجمهورية الإسلامية الإيرانية بشدة الغارات الجوية التي شنها الجيش الأمريكي الإرهابي فجر يوم الأحد، على عدد من منشآت الرصد والمراقبة على الساحل الجنوبي للبلاد. وتُعدّ هذه الهجمات الوحشية انتهاكًا صريحًا للمادة 2، الفقرة 4 من ميثاق الأمم المتحدة، وانتهاكًا صريحًا للمادة 1 من مذكرة التفاهم بشأن إنهاء الحرب المفروضة ، مما يُظهر أن النظام الأمريكي لا يُولي أدنى قيمة أو مصداقية لالتزاماته، وأن نقض الوعود جزء لا يتجزأ من طبيعة هذا النظام.
إن الجمهورية الإسلامية الإيرانية، إذ تذكر مسؤوليات مجلس الأمن التابع للأمم المتحدة والأمين العام لهذه المنظمة تجاه السلام والأمن الدوليين، تؤكد عزمها على الدفاع عن السيادة الوطنية الإيرانية والسلامة الإقليمية ضد العدوان العسكري الأمريكي، وفقاً للمادة 51 من ميثاق الأمم المتحدة</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/80166" target="_blank">📅 08:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80165">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏴‍☠️
🇸🇾
وسط إنشغال الجولاني وعصاباته الإرهابية بنبش القبور.. جيش الإحتلال الإسرائيلي:
بالأمس (السبت)، قامت قوات لواء عتسيوني (6) تحت قيادة الفرقة 210 بالقضاء على عدد من المسلحين في منطقة الأمن في جنوب سوريا. سيواصل الجيش الإسرائيلي العمل في منطقة الأمن في جنوب سوريا وإزالة أي تهديد على مواطني
دولة إسرائيل
وقوات الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80165" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80164">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات تهز البحرين الان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/80164" target="_blank">📅 07:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80163">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اصوات انفجارات تهز الكويت الان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/80163" target="_blank">📅 07:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80162">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c81df6c5.mp4?token=LIS8vEIKaIwknKG4qfnVewZAIAIZ4RsFFpJlSq243nguB6B55N9KUajRkYEgtBsZIvpYdpWsrtEhb2DaS-uhQSZ7mLPuvc2UJ8S_kgW1lB0fMcimaii875LNrmKDJ-77EnqPHC2zGrQpuotFbZJA0f_j1LoirPuHdHbi7iTP7xtCFseSHXHVn3GlOqkbAqLQ_QIpvo8oNdWaGKRgsOUXncc1W56uKjFG8xdBZLYGZTXciNfLti6czqu2R_GYA9QtxHH0wMiwQTKicsHXQR8Avri1pIWF5tMwhmWBk0XQWUn8ygH1N-siQ0dD78S7xgBx0JXSJrXtAT44soC3jUjzVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c81df6c5.mp4?token=LIS8vEIKaIwknKG4qfnVewZAIAIZ4RsFFpJlSq243nguB6B55N9KUajRkYEgtBsZIvpYdpWsrtEhb2DaS-uhQSZ7mLPuvc2UJ8S_kgW1lB0fMcimaii875LNrmKDJ-77EnqPHC2zGrQpuotFbZJA0f_j1LoirPuHdHbi7iTP7xtCFseSHXHVn3GlOqkbAqLQ_QIpvo8oNdWaGKRgsOUXncc1W56uKjFG8xdBZLYGZTXciNfLti6czqu2R_GYA9QtxHH0wMiwQTKicsHXQR8Avri1pIWF5tMwhmWBk0XQWUn8ygH1N-siQ0dD78S7xgBx0JXSJrXtAT44soC3jUjzVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين الان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/80162" target="_blank">📅 07:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80161">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انفجارات تهز البحرين الان</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/80161" target="_blank">📅 07:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80160">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">استمرار خدمات الانترنيت في العراق على الرغم من تلويح وزارة الاتصالات بقطع خدمة الإنترنت من المصدر مؤقتاً خلال أوقات الإمتحانات الوزارية من الساعة 6:00 صباحاً إلى 7:30 صباحاً،</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/80160" target="_blank">📅 06:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80159">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58da81163d.mp4?token=uF4aZEw8lHOK8EXRwAYa1oMVeYA9oOtZDAQCMf0NBw1KGvSggdGpsTDzE6cDetXJQXkm_yKTxxz7mz3sKn5bA0sLARk-x-dQb0bieuiTc2p6QSGk20FrHdwTbMP1gHrqW6Xl-y-Hr63kTLkbnUbfhPAo0rHWLeXLs-LVb0cfLZQQJpeKoZ4da413roL-BuYF9-ZJlGoxQ7jQqFO72QRHHBSof_AoIVQux400Kok_gdPjauz5GFLA-n5Gm21uP0Xg2y7pfggJl2T8f21CFWUjPpuYvjVe9AUJmrpj0TZTUCptVHmGpzP1psfDGQ-gxcXugNGzKoEa9dKRhqUzxHs9tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58da81163d.mp4?token=uF4aZEw8lHOK8EXRwAYa1oMVeYA9oOtZDAQCMf0NBw1KGvSggdGpsTDzE6cDetXJQXkm_yKTxxz7mz3sKn5bA0sLARk-x-dQb0bieuiTc2p6QSGk20FrHdwTbMP1gHrqW6Xl-y-Hr63kTLkbnUbfhPAo0rHWLeXLs-LVb0cfLZQQJpeKoZ4da413roL-BuYF9-ZJlGoxQ7jQqFO72QRHHBSof_AoIVQux400Kok_gdPjauz5GFLA-n5Gm21uP0Xg2y7pfggJl2T8f21CFWUjPpuYvjVe9AUJmrpj0TZTUCptVHmGpzP1psfDGQ-gxcXugNGzKoEa9dKRhqUzxHs9tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تحركات القوات الأمنية في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/80159" target="_blank">📅 06:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80158">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5o9Xgm02o2GAL5NWLYM4MMpxoR5XtubIAlyIxbSqa0OcHd1sWeBGjPfW_w0bwqvQZr-ghLJ5hpKgmPJrdf4hl-J-OHpr7uuYd8uYzXxV5-pH10XPnnqQ0KqYUaFTFVCKnjnjV_2usgY0aEyhD_-Ogl98cQ6R0C1SVAgIEDuJs0EO6UFbFtzzOXg-x8gauokog-45YygJn7AEJo1vbjgkJvGCTw18GknFA3xKm83JfB6QyeK20-xV_F8mFO7Am3K6EzHFKCB9iSz1TS0jLzr4kS5uRPa6zh3igLyZJM1O-88DdKfzqG_Js0qxSgcKRZ-TTsP5GQo5xQi2iiH5FJZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلل حركة السير بالمنطقة الخضراء</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/80158" target="_blank">📅 06:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80157">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">العملية الامنية لا تزال مستمرة حتى اللحظة .. مع انتشار لأفواج مكافحة الارهاب والفرقة الخاصة وارتفاع عدد المعتقلين إلى ٨ أشخاص بأوامر قضائية</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/80157" target="_blank">📅 06:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80156">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00df836d16.mp4?token=bvZ2-TrUScQVaQ6W7UxeKDkuIR332tSiSZsrdTIbJ88Q2hwwwMTn7lAbzURutpLARk8fm4ckBw6UWYB1H_YDxw-AXA0_2rVbjxNGkJ3p5l6lQ7oy9S79cHGVNvPiCddXSwQOf3SNwZBWVphWjiz6erT0UtTR1ZJ4T--m0rKS-rDzoBuizFNNFdhsSSYnWSJglTr66VehT4MmgVZAsfFGPC25OvCPPIPgSSO9-spj188X9eeu7EZVrIpnc9x1P8Ioge74n8yDL3slzPs5EUPiOm--QqcZIE-vr3tGpH2-NSWYhYW-PvNANfGWlNyjisgmCrXpYmM0dFPNxJ-2sWnOKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00df836d16.mp4?token=bvZ2-TrUScQVaQ6W7UxeKDkuIR332tSiSZsrdTIbJ88Q2hwwwMTn7lAbzURutpLARk8fm4ckBw6UWYB1H_YDxw-AXA0_2rVbjxNGkJ3p5l6lQ7oy9S79cHGVNvPiCddXSwQOf3SNwZBWVphWjiz6erT0UtTR1ZJ4T--m0rKS-rDzoBuizFNNFdhsSSYnWSJglTr66VehT4MmgVZAsfFGPC25OvCPPIPgSSO9-spj188X9eeu7EZVrIpnc9x1P8Ioge74n8yDL3slzPs5EUPiOm--QqcZIE-vr3tGpH2-NSWYhYW-PvNANfGWlNyjisgmCrXpYmM0dFPNxJ-2sWnOKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعادة افتتاح بوابات المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/80156" target="_blank">📅 06:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80155">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/994fd7d7a3.mp4?token=uSaRj8NfBX4VvhbQ2thx135v3H06xlK0bUTScRfa-ys_N85QqtpoGmoUiqpm8KemPfXEl3MMJwJqoIa4hr5KdiHU1fpg23wX3VZBambldsNbVOyuMbVK8QNN5sbBHZJpcQ7zJy_2FlwAO6q3Gievo4OdNFHudIzO3vV3MpGHCxqQNT9ECQ5tcKVx-jGCSDUH6GAJjQQe48AzaUReOYlgHSjYvOblIGlbDKVslXbI1XRGysBTWtcgun2eh5nyMY5-jtg6tUT__JYU2HUwub9n1DcovluZ5YNhBSwlBfIr0VvosP2LwVKO1evlMrlrJvp_HjrgqHYQ6XwlPX_Rf3Y0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/994fd7d7a3.mp4?token=uSaRj8NfBX4VvhbQ2thx135v3H06xlK0bUTScRfa-ys_N85QqtpoGmoUiqpm8KemPfXEl3MMJwJqoIa4hr5KdiHU1fpg23wX3VZBambldsNbVOyuMbVK8QNN5sbBHZJpcQ7zJy_2FlwAO6q3Gievo4OdNFHudIzO3vV3MpGHCxqQNT9ECQ5tcKVx-jGCSDUH6GAJjQQe48AzaUReOYlgHSjYvOblIGlbDKVslXbI1XRGysBTWtcgun2eh5nyMY5-jtg6tUT__JYU2HUwub9n1DcovluZ5YNhBSwlBfIr0VvosP2LwVKO1evlMrlrJvp_HjrgqHYQ6XwlPX_Rf3Y0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجهة المنفذة للواجبات فجر اليوم " جهاز مكافحة الارهاب ، الفرقة الخاصة ، الفرقة المدرعة التاسعة جيش عراقي " ؛ بيان حكومي مرتقب عن العملية العسكرية</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/80155" target="_blank">📅 06:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80154">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/80154" target="_blank">📅 06:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80153">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/80153" target="_blank">📅 05:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80152">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/80152" target="_blank">📅 05:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80150">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سرقة سيارة نوع جكسارة تعود لضابط برتبة عقيد في وزارة الداخلية العراقية .</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/80150" target="_blank">📅 05:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80149">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سيطرات مفاجئة وتدقيق على الأسماء في اغلب شوارع العاصمة بغداد .</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/80149" target="_blank">📅 05:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80148">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قوات أمنية إضافية تنتشر في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/80148" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80147">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
توثيق للحظة إطلاق الصواريخ الإيرانية نحو قاعدة علي السالم الأمريكية في الكويت.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/80147" target="_blank">📅 04:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80146">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b80a9e9cb.mp4?token=tFZ3nAYvEOKryl0iGpFqSC3elzUAxzVgLlgu3vD3UXBBPQQb5OU25Rfs-gp63qKemuJ14xoQmAB_aOEkn3DXSYwXjg2jdH5E-4DpgIb4urpfM5O-fyiYEu9lmVjw2_yrCLYw-TTrnVN-ZZZmPUj4PuWdtaePj5KsCxMc_6lulCw5HLyj700TXDWPD4dHxaip9jENr6kirvAzIybeo5CjleR9sD99x0rSnXlk3KHq5-yquhogXH8ZkEaWWhHdPZM_I4wjyXMsHROT_fX6udpzg9rl35HHQIAgFLtkj0CEzugnIHxKFJWXnhak6jti4ArNqxx4G4iXvmVKRJgzFwxiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b80a9e9cb.mp4?token=tFZ3nAYvEOKryl0iGpFqSC3elzUAxzVgLlgu3vD3UXBBPQQb5OU25Rfs-gp63qKemuJ14xoQmAB_aOEkn3DXSYwXjg2jdH5E-4DpgIb4urpfM5O-fyiYEu9lmVjw2_yrCLYw-TTrnVN-ZZZmPUj4PuWdtaePj5KsCxMc_6lulCw5HLyj700TXDWPD4dHxaip9jENr6kirvAzIybeo5CjleR9sD99x0rSnXlk3KHq5-yquhogXH8ZkEaWWhHdPZM_I4wjyXMsHROT_fX6udpzg9rl35HHQIAgFLtkj0CEzugnIHxKFJWXnhak6jti4ArNqxx4G4iXvmVKRJgzFwxiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إغلاق تام لبوابات المنطقة الخضراء وانتشار دبابات أبرامز بالتزامن مع حملة اعتقالات طالت عدد من السياسين بتهم قضائية</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/80146" target="_blank">📅 04:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80145">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911e440568.mp4?token=UTT6lTpWhV7VBjcqbegUPSLl71IncC-_rJBThX1O-UGk6uD63KW2SxlOrSkIgyyrtuid6zS-dgZ0Cw1fEBFID2KOZ9R9-AflJH_cZGpsW7QoXMz3X6_LsLUm8WomLzvMX3DguvEAu7Ivy4Z1MHXNuMqYZQFhQlUw7WjJIa3XSjlr-JwWA_CN9LemVi2oSHEHJq1krBiPWMUxkTv5HM9TRd1OZwWo0tBGcTd83Zu9q7IGYFm8Bd61EvvL7dEy3X-3qBdh9bxsicUG5SdgzycGcVkkjU8f-17fzO2GBfQ60fbcK8ZBkloVJXu4W4lLQBtWZzT0FQ6_LoPezwLyBWvQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911e440568.mp4?token=UTT6lTpWhV7VBjcqbegUPSLl71IncC-_rJBThX1O-UGk6uD63KW2SxlOrSkIgyyrtuid6zS-dgZ0Cw1fEBFID2KOZ9R9-AflJH_cZGpsW7QoXMz3X6_LsLUm8WomLzvMX3DguvEAu7Ivy4Z1MHXNuMqYZQFhQlUw7WjJIa3XSjlr-JwWA_CN9LemVi2oSHEHJq1krBiPWMUxkTv5HM9TRd1OZwWo0tBGcTd83Zu9q7IGYFm8Bd61EvvL7dEy3X-3qBdh9bxsicUG5SdgzycGcVkkjU8f-17fzO2GBfQ60fbcK8ZBkloVJXu4W4lLQBtWZzT0FQ6_LoPezwLyBWvQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/naya_foriraq/80145" target="_blank">📅 04:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80144">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80144" target="_blank">📅 04:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80143">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a37338d56.mp4?token=FQrW8hsJE6vjTqI1IC22L9KVSACd2MGiSxqJjUCEOOtSTgbcuq3ERFEsB7tyP0G96FgchyGLTtNm9dWqb_TXLmT-MEg9SpSxeTPudl5yA6jivqIiRP60NwNXdtcZYS2p6J0a1Z8lbYJuYFvTLCs_ppMNF7YzNoSG15UoaNjWfrrxp1D7cikUdj4pIS-Z8ATq68I5DgDYDBu3G74IO8RnWLYW2-RKr4nfEe6mwsH4BU7rTGOGkUNGIDkEPCf7wlsqHVUbrdpAOqYwepAUbRL9jnig4SdsF_zDK1xrnTpUoFa4nQUHsCbt0xO8eHkdufPaRXUlaQSBcL0kFN36n_yOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a37338d56.mp4?token=FQrW8hsJE6vjTqI1IC22L9KVSACd2MGiSxqJjUCEOOtSTgbcuq3ERFEsB7tyP0G96FgchyGLTtNm9dWqb_TXLmT-MEg9SpSxeTPudl5yA6jivqIiRP60NwNXdtcZYS2p6J0a1Z8lbYJuYFvTLCs_ppMNF7YzNoSG15UoaNjWfrrxp1D7cikUdj4pIS-Z8ATq68I5DgDYDBu3G74IO8RnWLYW2-RKr4nfEe6mwsH4BU7rTGOGkUNGIDkEPCf7wlsqHVUbrdpAOqYwepAUbRL9jnig4SdsF_zDK1xrnTpUoFa4nQUHsCbt0xO8eHkdufPaRXUlaQSBcL0kFN36n_yOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/80143" target="_blank">📅 04:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80142">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/80142" target="_blank">📅 04:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80141">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/80141" target="_blank">📅 04:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80140">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">توثيق أخر يظهر كثافة الإنتشار الأمني في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/80140" target="_blank">📅 04:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgecF8CdQqkhGeKojyMazcBEuMTkHPwSfXHWS53ER6E3FiVbL2dNE-gDLdaYLLcdsOP2xTnUIQXqllDay23r8T9drXslVFj1RxlBSWdKs_S2K0ExZ1vZQ4XztIiDTHQbVIui6VCxxJyrk5bjnbciHlpVUplReuRNS6n5Q1sP3UmpVUNb___uOHGLw_tcnLDO5b00xVL4Qg08b9QYkfxSWRWTSkJMTP685WBlI2VBd7zqpD4s6U1m7nB6Qu2I_GkqJUBQ1mYmUpQA-rj1i0c2KgMYsfWuTwTfLXg7vs1ji9kY3QMHmUOM--ZXKpaDOF2CUcY2GTkTnx4mK5sa46TezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العلاقات العامة للحرس الثوري الإسلامي: أيها الشعب الكريم لجمهورية إيران الإسلامية؛  خلال عملية صاروخية وطائرات مسيرة مشتركة بين الساعة الثانية والثالثة فجر اليوم الأحد 28 يوليو، أطلق أبناؤكم البواسل في القوات البحرية والجوية للحرس الثوري صواريخ باليستية وطائرات…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/80139" target="_blank">📅 04:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f860d0e2.mp4?token=tzZbd1Wz6grb4KeeY0f5reZzKoxxBvckuAOfs7cJ5urr4F6KGkPuPWXAnLATDz6vIf9Ltx6GFxJ_1K9KDUXfIdPBaWb4l_LD5LVIxFvxx6j5qK0_v3z80tfa1NmuIiATJBVlattqbPvTfPFgbpuE4lNwU5iAFnlOjkOjsvr4FEyxaijuhpf0iW7OH5lQxKImcjoIzRiHkRHeWMd2Rlo9NFXg43byL7HP4IFs0GCSJ-28u0F4HFuq6oLtJmSLNr8Pa8NGjXVQppLmDR7swZ7jJDjWWlqjWBhdlQST1nl7HBAzRSMmwy0cjDf1IltzSdxT38xa3Oh7QyHZ8sAExkGJqxNS6ZUnQxs6AMmZ_cOltcwccbwOUJYpOvGaUscoiBFSIrYy6XAfxtgSqM6eDb-IwWPCZn1qcShKXzjaePOuJpLvk3jwHSURyq7-glmMFLkZ55QaJlu2Jccek9lZnCf9U69lHHBo1NFAj1r94q7Yzucmn7OPl758uAps1Aps3v_WntPTHPSOMDzhx_gKlhTfGDto_EDJXS2mQ8y9vwf1VqUdAq06bTXDcWvqc9NQjecmOo1seTZqC6BtZUDt2sEEK-MYuWW8wThM-kM_GtXVDZQEJyf9ElijtfOpcqaxIOs4ZAV6OuBdPK-_CyHM-0qcj6VzPKjKpA41giMnT18CPhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f860d0e2.mp4?token=tzZbd1Wz6grb4KeeY0f5reZzKoxxBvckuAOfs7cJ5urr4F6KGkPuPWXAnLATDz6vIf9Ltx6GFxJ_1K9KDUXfIdPBaWb4l_LD5LVIxFvxx6j5qK0_v3z80tfa1NmuIiATJBVlattqbPvTfPFgbpuE4lNwU5iAFnlOjkOjsvr4FEyxaijuhpf0iW7OH5lQxKImcjoIzRiHkRHeWMd2Rlo9NFXg43byL7HP4IFs0GCSJ-28u0F4HFuq6oLtJmSLNr8Pa8NGjXVQppLmDR7swZ7jJDjWWlqjWBhdlQST1nl7HBAzRSMmwy0cjDf1IltzSdxT38xa3Oh7QyHZ8sAExkGJqxNS6ZUnQxs6AMmZ_cOltcwccbwOUJYpOvGaUscoiBFSIrYy6XAfxtgSqM6eDb-IwWPCZn1qcShKXzjaePOuJpLvk3jwHSURyq7-glmMFLkZ55QaJlu2Jccek9lZnCf9U69lHHBo1NFAj1r94q7Yzucmn7OPl758uAps1Aps3v_WntPTHPSOMDzhx_gKlhTfGDto_EDJXS2mQ8y9vwf1VqUdAq06bTXDcWvqc9NQjecmOo1seTZqC6BtZUDt2sEEK-MYuWW8wThM-kM_GtXVDZQEJyf9ElijtfOpcqaxIOs4ZAV6OuBdPK-_CyHM-0qcj6VzPKjKpA41giMnT18CPhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات أمنية إضافية تنتشر في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/80138" target="_blank">📅 04:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366e2bae2f.mp4?token=DoEdVNlXPO4v587TJuNE-nohX4-FbYu9FBLtxjLiQ0YelCTqCOJ93N6B6oJRaS8hfAAIap3BymmE8PJ9fNRy6o-QhWtCQhCvO9QU0xHuZAFbCh9R35td8T0QmwCxXSOnHdbwnNhHStED-aDKs2tyUdGp0MbkILQQ_pkrTOwO-_x-f9j_3INiZCRt0eeEbNeH8_odLU4kIrGBbXMW99JYlZ2l_au_Ml00xOsEd2f12PGT0QdwQtI74kSngElSuiP-0iqe4bpatm-N30xs6pHDTn3R_b59HAp5Rey-Z-wN6bsR7LIAkjJYLmtth7vFuaKCEZv2URt_q6RT8oxZpgk1mDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366e2bae2f.mp4?token=DoEdVNlXPO4v587TJuNE-nohX4-FbYu9FBLtxjLiQ0YelCTqCOJ93N6B6oJRaS8hfAAIap3BymmE8PJ9fNRy6o-QhWtCQhCvO9QU0xHuZAFbCh9R35td8T0QmwCxXSOnHdbwnNhHStED-aDKs2tyUdGp0MbkILQQ_pkrTOwO-_x-f9j_3INiZCRt0eeEbNeH8_odLU4kIrGBbXMW99JYlZ2l_au_Ml00xOsEd2f12PGT0QdwQtI74kSngElSuiP-0iqe4bpatm-N30xs6pHDTn3R_b59HAp5Rey-Z-wN6bsR7LIAkjJYLmtth7vFuaKCEZv2URt_q6RT8oxZpgk1mDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أعلنت القيادة المركزية الأمريكية (CENTCOM) تنفيذ ضربات جديدة استهدفت مواقع عسكرية إيرانية، رداً على هجوم بطائرة مسيّرة استهدف ناقلة نفط قرب مضيق هرمز. وأكدت أن الضربات شملت أنظمة مراقبة واتصالات ودفاعات جوية ومخازن للمسيّرات، مشيرةً إلى استمرار حركة الملاحة…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/80137" target="_blank">📅 04:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80136">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الحرس الثوري الإيراني يتبنى الهجوم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/80136" target="_blank">📅 04:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80135">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الحرس الثوري الإيراني يتبنى الهجوم</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/80135" target="_blank">📅 04:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80134">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/80134" target="_blank">📅 03:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80133">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/80133" target="_blank">📅 03:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80131">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fuX_5-sdJGpgK1aqcjc_3Mzs8FlUknLV94n1Y89VuoveS7UOAo3Rubu-Lp65vpg4wQ_VBll6rqYXCS7TMIQIa50GQK2TmHEgoQHuIqwhz8qUes_dFUUJ8x-VUHwjetxhBzfTB4w7gBlzpPmTMc77qRTCDvoJD3jlJlPR8uqOKHN0wBp2sAEWEhkl80ZctY2PjZnXjbraBo1Imsjc6zU9JdsHKD8iKnjuPLVDc2zpb3G5Zzbfkg7zv-i0CH6CGbx1Ww1Cy4-ErgaSdpF3TviUHVkvF8WX79T1_9V224M1WmNkYgc9aja7XO-hgeM23nnVy9Zk6-GG4kY1iAkMSd3JTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApPz49updKW8e0NnQlrXJC6eiMn9J-q0KS_AsjTyCcbNMzh7XNFZTDCTYWy_9F2c9-drpESMKpGaawHl4wp350SAYXNwiLqUEeenPQauRxCUL7G3FRj5SXr_sfoKIQSTL8ns-eYu177e93Ia0t1PZTN1sjfOzBx00NVcYZ5JpLF8_JFFkowi3MfPBUComGlBKhGJyB1BJWcNH0h4qZLb4UGhnqx1DoYgm0C01SLs-BK8qkiQVhlV2HgVeLZTg7w3PafTG0mx9JlUcu50PMq5sySHtQi8A0XkjO7J7zRXKF4O_fNTjI09cb2xgYvgPe1fi4wVDOqE0FVB2jC7nXhEtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صافرات الإنذار تدوي بإستمرار في الكويت عقب هجوم صاروخي وبالطائرات المسيرة</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/80131" target="_blank">📅 03:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80130">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80130" target="_blank">📅 03:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80129">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/80129" target="_blank">📅 03:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80128">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/80128" target="_blank">📅 03:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80127">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71aa5ae7b8.mp4?token=Qh6RpzK29Eez6-ZMQICnLkXDKM03x93btYoaToHu98-s2PbfHb6Zl0_qzc6U8mzd__k5U1hUDSLg8J2Ten4g3rXxPOG0NYSoYWO5LislBBXEoerYv04Kgdh7ErkOT-5B8j_YWPRARXjcVLPDtUrVsPZywUx42s49LS-RXQ1Mq8TQWrd-vyYy3i3AwnY-IJGTFE7qP3eF2cPQF1aku-CP4B6PI20nZ3J7PNELH4YqDfTW46Un4jbK10WV1zzYAx9va9TR3vN9HcsZRnIqZ9paxbVr9ey6b0ylbBa2xiGUk2Rj-C7cutTe0WN7C1CuivHDb_zBGswNpvl4RNfr2GHosA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71aa5ae7b8.mp4?token=Qh6RpzK29Eez6-ZMQICnLkXDKM03x93btYoaToHu98-s2PbfHb6Zl0_qzc6U8mzd__k5U1hUDSLg8J2Ten4g3rXxPOG0NYSoYWO5LislBBXEoerYv04Kgdh7ErkOT-5B8j_YWPRARXjcVLPDtUrVsPZywUx42s49LS-RXQ1Mq8TQWrd-vyYy3i3AwnY-IJGTFE7qP3eF2cPQF1aku-CP4B6PI20nZ3J7PNELH4YqDfTW46Un4jbK10WV1zzYAx9va9TR3vN9HcsZRnIqZ9paxbVr9ey6b0ylbBa2xiGUk2Rj-C7cutTe0WN7C1CuivHDb_zBGswNpvl4RNfr2GHosA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/80127" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80126">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f975085a0.mp4?token=MKKgjkvPL5nWa9mgHG8SOciHBQ13HN2hICxQoUOlTKTe8G59HdX1rPg7oPvOykyxIpFqBHPoWrYvr8-W3EV7IacSsAvHCKTvmEXrE7WbE788qopKAE0lRu9ukxEeMxqXXIctbP3NbCFx-gQB7UemfFrruV0XEf5avswz5rRXBJbwx2WTTOOCNsD1Rw5KKrXgwqlm8wGyUdqEUIX0jcePwzIDMS251dxQQ60bWBtTBxJnw6IinAkudz-NG3xWPJCAtpYIUNP5LlGLxjJtNfBcb4oywzoBJ0M-faXLCGrff5hXanDu-kPVHMAGn-tPfthtQSau1fJqg013SzwfR2Hzuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f975085a0.mp4?token=MKKgjkvPL5nWa9mgHG8SOciHBQ13HN2hICxQoUOlTKTe8G59HdX1rPg7oPvOykyxIpFqBHPoWrYvr8-W3EV7IacSsAvHCKTvmEXrE7WbE788qopKAE0lRu9ukxEeMxqXXIctbP3NbCFx-gQB7UemfFrruV0XEf5avswz5rRXBJbwx2WTTOOCNsD1Rw5KKrXgwqlm8wGyUdqEUIX0jcePwzIDMS251dxQQ60bWBtTBxJnw6IinAkudz-NG3xWPJCAtpYIUNP5LlGLxjJtNfBcb4oywzoBJ0M-faXLCGrff5hXanDu-kPVHMAGn-tPfthtQSau1fJqg013SzwfR2Hzuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبابات ومدرعات تجوب شوارع العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/80126" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80125">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">منظومة الباتريوت الأمريكية تحاول الإعتراض</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80125" target="_blank">📅 03:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80124">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/80124" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80123">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الصواريخ الإيرانية تدك الكويت</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80123" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
