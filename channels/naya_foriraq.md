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
<img src="https://cdn4.telesco.pe/file/KbteY4qQzX364hZpKecS82tCojVcWe9zjkVDtcoN_rC3Kjf9zpdqtfD7e1hssJiT2A6sCfQP3BlC_97u1PJTDq57O7SwDpqfc_BhNx0NfdkqMe1WPsRV7Bmr2clmJ4yDJQtOL18KArR-Pfxvb4Tl7kGWMBeKzk4JPKYz5dQmfLjK6mwOAU6qQlvsOYtcRGm_tCmu0jm4RdGf2aFz96lr4SUAgVuE3UhoOf5q2zDiJAIIaMdODAIhys2CZS51-2kpQDAI8YM1XqBtGHP2xAgemElLvHpVmpxD-ulylKqc9H-aQ4VRArDkP4j59vK7U2uW_Zjwp7yFu8lv51dGbIfJWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-79015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f917cdfbc3.mp4?token=OBIZGE2ZTHCXiOBNaNHDrE9Te4-CC8X2G4VNYEAl0MI8vFzCkeuY3_7lP2SrVBt-9ADykmtqBonBiypBkjWnf6BHoKXQ434oYH3VuudcP0YV-RDptAnvlzNx2yoCVzhLxtY3OPJATCMh14TsRIkeu-vGFXwv_DDTD86sWNImkoF5HB1a5_RDLwB7q5QWasJyJGKjO0E-WkuLVe7sD_CEOUP-McwIwP9tTHxk3SgLvUAqaL8KPkwLijc8IzQlFuaiVKhff2fbP23kIugj2igW-mZ3TPVWxXALtvtVDLZKLDnm3q2vrsTIm3Q_3Hfw-ufbUyjSBkjnMBVpmusr2toXZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f917cdfbc3.mp4?token=OBIZGE2ZTHCXiOBNaNHDrE9Te4-CC8X2G4VNYEAl0MI8vFzCkeuY3_7lP2SrVBt-9ADykmtqBonBiypBkjWnf6BHoKXQ434oYH3VuudcP0YV-RDptAnvlzNx2yoCVzhLxtY3OPJATCMh14TsRIkeu-vGFXwv_DDTD86sWNImkoF5HB1a5_RDLwB7q5QWasJyJGKjO0E-WkuLVe7sD_CEOUP-McwIwP9tTHxk3SgLvUAqaL8KPkwLijc8IzQlFuaiVKhff2fbP23kIugj2igW-mZ3TPVWxXALtvtVDLZKLDnm3q2vrsTIm3Q_3Hfw-ufbUyjSBkjnMBVpmusr2toXZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تواصل فشلها في تنظيم كأس العالم:
اشتباكات عنيفة بين جماهير الجزائر والارجنتين في ميدان التايم سكوير بنيويورك.</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/naya_foriraq/79015" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
إسرائيل طلبت الاطلاع على مذكرة التفاهم مع إيران لكن أميركا رفضت.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/naya_foriraq/79014" target="_blank">📅 16:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaGQXPpp5_GX6JaZYOSlUS2uqNPdUETIMtWAKdjqbV9uwiFV0NOk3n-i7ZgURmWXGhfLm6yfmfneETor1ALetW4oq6nsaxDpR7KWjHyg2CIfqf7tzH-oJxUMjeJb0kSnYGkv_ffi_YbANFY5OOrSHpxqaxgStHEPzP4rUKlczjH4mW2FnBgWAk2pKkSitKUe6DKP5Y-_5GusdoaAeCQVfcb-pnyQ9fROLA09A-jNFpV25QaS-g8evbwaOSBZ4KiaqZAG8ZbaTJ583rC9k3pqvTXZdF7DyTqebw2XFgJcCgfb3kPxkRE37rq7Z9GjvWGVa4m1RfGAIC97GHB9TnQIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اليمنيين ينتفضون في صنعاء تجاه اساءة ترامب لمكة المكرمة وسط صمت من قبل نظام ال سعود</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/naya_foriraq/79013" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
الكابينت المصغر سيناقش اليوم طلب امريكي بالانسحاب من لبنان لحين توقيع الاتفاق مع ايران.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/naya_foriraq/79012" target="_blank">📅 16:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c2863c31.mp4?token=iIspL3RulPI8d52ID1SrRcSoCcPUjdxfOeast7biiaLSbcdowGywtEH_de1rpmpf1ZLJgSI9Sa8yHkN0d4X7KC-lE8gZjFo8I9qxLBJQ1CuxAFI5S3IKQ6rrpbksPWl_SpuGIJdK9UAlwCw0AfV-ICt7xdclhGK0ttAdcjWioB2xJ_VjX0eduI0e87UY9z5a9Qqwgoe8o5nQCsmJ50JotHhN3Iv8F-3ffInU9ez8h6MR8D0Qv4f_nQlsHqrVodRkC9nPEB1yQlyEtXGZkKlKy5n7L11HmryUKlkRj_qRpciMH_lSjk5-BboXDy1i_dj4P-pifN-wkmhATISnol8kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c2863c31.mp4?token=iIspL3RulPI8d52ID1SrRcSoCcPUjdxfOeast7biiaLSbcdowGywtEH_de1rpmpf1ZLJgSI9Sa8yHkN0d4X7KC-lE8gZjFo8I9qxLBJQ1CuxAFI5S3IKQ6rrpbksPWl_SpuGIJdK9UAlwCw0AfV-ICt7xdclhGK0ttAdcjWioB2xJ_VjX0eduI0e87UY9z5a9Qqwgoe8o5nQCsmJ50JotHhN3Iv8F-3ffInU9ez8h6MR8D0Qv4f_nQlsHqrVodRkC9nPEB1yQlyEtXGZkKlKy5n7L11HmryUKlkRj_qRpciMH_lSjk5-BboXDy1i_dj4P-pifN-wkmhATISnol8kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية تستهدف منطقة دار المعلمين في بلدة النبطية الفوقا جنوب لبنان</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/naya_foriraq/79011" target="_blank">📅 16:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامب: سأرسل اتفاق إيران إلى الكونغرس لمراجعته.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/naya_foriraq/79010" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامب: سنناقش اتفاق إيران مع وسائل الإعلام في غضون أيام قليلة.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/79009" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رسالة حجة الإسلام والمسلمين الأمين العام لحزب الله سماحة الشيخ نعيم قاسم إلى رئيس مجلس الشورى الإسلامي الدكتور محمد رضا قاليباف:
بسم الله الرحمن الرحيم
جناب رئيس مجلس الشورى الإسلامي الدكتور محمد رضا قاليباف أيَّدكم المولى ورعاكم.
السلام عليكم ورحمة الله وبركاته
تعجز الكلمات عن تعبيرنا بالشكر الكبير للمواقف القوية والداعمة للبنان وشعبه ومقاومته لإلزام الكيان الإسرائيلي بالوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات بما فيها لبنان، ربطًا بوقف الحرب على الجمهورية الإسلامية الإيرانية، كبندٍ أول وأساس للاتفاق بين إيران وأميركا. فقد حوَّلتم بارقة الأمل الوحيدة والفاعلة في كف يد العدوان الإسرائيلي الأميركي على لبنان إلى حقيقة أثبت للعالم بأنَّ إيران نصيرة الحق والمقاومة والمستضعفين، ولو احتذى طريقها آخرون لما تجبَّرت أميركا وإسرائيل، ولما بقي الاحتلال الصهيوني جاسمًا على أرض فلسطين والقدس.
قلنا دائمًا بأنَّ إيران أعطت حزب الله والمقاومة ولشعب لبنان كلَّ شيء ولم تأخذ منه شيئًا، هي أُعطتنا لخياراتنا، لقوتنا من أجل تحرير أرضنا، لبلسمة جراحات مجتمعنا ومساعدته. والآن تبذل إيران الدم، فتتصدى بقصف الكيان الصهيوني ردًا على قصفه لضاحية بيروت الجنوبية، وتتحمل تبعاته التي تنذر بالحرب عليها مع عظيم التضحيات. سأقولها صادحة: إيران أيقونة العزة والشرف.
أشكركم بإسم حزب الله ومقاومته الإسلامية، بإسم المحبين من الشعب اللبناني الذين يرغبون أن نوصل شكرهم إليكم، بإسم الشهداء وفي مقدمهم سيد شهداء الأمة السيد حسن نصر الله(رض) والجرحى والأسرى، بصفتكم كبير المفاوضين مع فريق عملكم المباشر ومنهم وزير الخارجية الدكتور عباس عراقجي، راجيًا إيصال الشكر والامتنان إلى القائد آية الله السيد مجتبى الخامنئي(دام ظله) الذي غمرنا باهتمامه، وأحيى فينا بركات ورعاية الشهيد الإمام الخامنئي(قده)، ورئيس الجمهورية الدكتور بازكشيان المحب للمقاومة، وحرس الثورة الإسلامية الإيرانية هذه القوة النورانية التي قلبت المعادلة ببأسها، والجيش والنخب وكل الفعليات الرسمية والشعبية.
وأخص بالذكر الشعب الإيراني العظيم لقد رأيناهم في ساحات المدن الإيرانية وسمعنا مطالبهم في بذل مهجهم لإنقاذ المقاومة وشعبها. شكرًا لكم. شكرًا لإيران الوفية. والسلام عليكم ورحمة الله وبركاته.
الأمين العام لحزب الله نعيم قاسم
01 محرم 1448 هـ
16 حزيران
2026</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/naya_foriraq/79008" target="_blank">📅 16:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامب: سأعقد مؤتمرًا صحفيًا حول الاتفاق الإيراني.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/naya_foriraq/79007" target="_blank">📅 16:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامب: سننشر نص الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/naya_foriraq/79006" target="_blank">📅 16:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇱🇧
الأمين العام لحزب الله سماحة الشيخ نعيم قاسم يلقي كلمة في افتتاح المجلس العاشورائي المركزي يوم غد الاربعاء الساعة 6 مساءً.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/naya_foriraq/79005" target="_blank">📅 16:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامب: العلاقة الجديدة مع ايران باتت طبيعية وأعتقد أن الأمور ستتقدم بسرعة</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/naya_foriraq/79004" target="_blank">📅 16:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامب: بدأت السفن في العبور عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/79003" target="_blank">📅 16:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامب: مضيق هرمز سيفتح بالكامل بحلول يوم الجمعة</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/naya_foriraq/79002" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامب: مضيق هرمز سيفتح بالكامل بحلول يوم الجمعة</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/79001" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مكتب التحقيقات الفيدرالي يزعم احباط هجوم بالمسيرات والقناصة على البيت الأبيض</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/79000" target="_blank">📅 15:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
مستشار حكومي عراقي:
عدم إقرار الموازنة لن يؤدي إلى توقف صرف رواتب الموظفين أو المتقاعدين أو مستفيدي الرعاية الاجتماعية، هذه الرواتب تعد من النفقات الأساسية التي تلتزم الدولة بتأمينها بموجب الأطر القانونية والمالية النافذة.</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/78999" target="_blank">📅 15:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHxkZ3dH46p7v8yOxmqOudkAAf194gjFyW_0clVmmjrOqXjTMCWErmYkDIj_fheXAnf0gCxKDGj9CepcJN01T4W646mwrxxEQk0cZWSwTrl-iILZc-thcy1IsI1_ft-Ii-jmb3pfOiTfY1Y5_K3GidyaX83BCc4QKQr8n11qjt0sk11dIHy758LJFvH542dZKtYlh7fnAlpQbbDpQ2ZP2ypt4yJYqjmcpTHg9S0DgIZ8PXffaSzEH4w2Lhsacs1PIG_R6WatiUekLwzFUiOOaq-NCcKdPQhKucgFBcCm2FynHAbN15593RrKORommiyw-UQrakrvC6Zop1UBrI1HXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"سنعيد الامن الى الشمال وسنصنع الامن"</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/78998" target="_blank">📅 15:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇹🇷
‏وزير خارجية تركيا: كانت هناك مساع إسرائيلية لإفشال الاتفاق بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/78997" target="_blank">📅 15:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏
زيلينسكي:
ترامب منفتح على دعم أوكرانيا بصواريخ للدفاع الجوي.</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/naya_foriraq/78996" target="_blank">📅 15:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامب: لو لم أكن موجوداً لما كانت هناك إسرائيل</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/naya_foriraq/78995" target="_blank">📅 14:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇹🇷
‏
وزير خارجية تركيا:
كانت هناك مساع إسرائيلية لإفشال الاتفاق بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/78994" target="_blank">📅 14:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af5f6a955.mp4?token=XuHALCKhUuKU_88tRnSi_9SgPy95V9xwlocy7HSvnNquchnpS6W-Kp906wjb6S-OrBSBPQsbTpZ5c0j7fQYK3Sszv7hUCLdSscLlCTnm8nCIIL8WJz1xEOu-Dat_XCg3q0L8fXIxgw9_Wuqj5O7X5TuO7CxFSzPjYtZrnC5flWyrUmbKuZ4y2jbIr8iVRpOAj-KokTW9Nk3wISN54am6tArWgtmdIe6UUTGtJhODnu23mO0VUq9ydR9p2uI2oAqUzdIct6dIG7GeB8jwzriS2lVeu3OhkN5Io7C7-AyyAFEQD9RfpktybdT0X5_kL4nvDo5fjmfjbIjGutleQAkzJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af5f6a955.mp4?token=XuHALCKhUuKU_88tRnSi_9SgPy95V9xwlocy7HSvnNquchnpS6W-Kp906wjb6S-OrBSBPQsbTpZ5c0j7fQYK3Sszv7hUCLdSscLlCTnm8nCIIL8WJz1xEOu-Dat_XCg3q0L8fXIxgw9_Wuqj5O7X5TuO7CxFSzPjYtZrnC5flWyrUmbKuZ4y2jbIr8iVRpOAj-KokTW9Nk3wISN54am6tArWgtmdIe6UUTGtJhODnu23mO0VUq9ydR9p2uI2oAqUzdIct6dIG7GeB8jwzriS2lVeu3OhkN5Io7C7-AyyAFEQD9RfpktybdT0X5_kL4nvDo5fjmfjbIjGutleQAkzJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رئيس وزراء النرويج يخاطب لاعبي المنتخب النرويجي: "احلموا بأحلام كبيرة، واذهبوا واسحقوا العراق"!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78993" target="_blank">📅 13:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامب: إذا لم تستطع إسرائيل إنجاز الأمر في لبنان دون قتل الجميع، فيجب على سوريا أن تقوم بذلك</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/78992" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78991">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏ترامب: لم يعجبني هجوم إسرائيل على بيروت قبيل توقيع اتفاق إيران</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/78991" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78990">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامب: أنا لست غاضبًا من نتنياهو.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78990" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78989">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏ترامب: أقترح على إسرائيل أن تترك سوريا</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/78989" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78988">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامب: إذا هاجمت إسرائيل لبنان، فقد يبقى الاتفاق قائمًا.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78988" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامب: كنا نريد الذهاب إلى إيران للحصول على اليورانيوم المخصب لكن هذا لم يتم</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/78987" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78986">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
ترامب: يجب على روسيا أن تبرم اتفاقًا.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/78986" target="_blank">📅 13:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78985">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامب: تم الانتقال إلى المرحلة الثانية من صفقة إيران.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/78985" target="_blank">📅 13:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78984">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd979693a6.mp4?token=Fgewr1fzbWksDJzy85acz0OLOi2Vj9Fqz_18zglalzZ3ltcQqPniHZn34gkLRmoCcqX7zmNSF3yc0jgxVpyaLFJoVAoUdSbZRb1T6c1A61WbtZOC9f2xbMWNPtYQ_16fOWzmbGwnxhiFXcEPIcu8VV7PRBjyrIekkwvTDOIe5zwoV5Uh3EyMdhNQNY5_BlgPEnUhpevCzwo_ZylC25N_pZXHweP3xOA1---L8X6vNYQK2m4da7_GGFRUrEB6yslaqJnghgrA3WNxynbyeZBttrve6mx076XZtaRuseg1HNyMPJqRxWyK3f2cCAkABv_sO3q3W6nm_XHwTvR6BAqtcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd979693a6.mp4?token=Fgewr1fzbWksDJzy85acz0OLOi2Vj9Fqz_18zglalzZ3ltcQqPniHZn34gkLRmoCcqX7zmNSF3yc0jgxVpyaLFJoVAoUdSbZRb1T6c1A61WbtZOC9f2xbMWNPtYQ_16fOWzmbGwnxhiFXcEPIcu8VV7PRBjyrIekkwvTDOIe5zwoV5Uh3EyMdhNQNY5_BlgPEnUhpevCzwo_ZylC25N_pZXHweP3xOA1---L8X6vNYQK2m4da7_GGFRUrEB6yslaqJnghgrA3WNxynbyeZBttrve6mx076XZtaRuseg1HNyMPJqRxWyK3f2cCAkABv_sO3q3W6nm_XHwTvR6BAqtcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#بالفيديو
⭐️
اندلاع نزاع بين حماية النائب خالد العبيدي وعناصر حماية وكيل وزير الداخلية في مدينة الموصل.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/78984" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78983">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامب: تم الانتقال إلى المرحلة الثانية من صفقة إيران.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/78983" target="_blank">📅 13:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr60uowLXRp-hz5OgQ3UdHZq76iHK8_iFxe4kKesdcdjS4iC3J-bFUeANmVpCsQvjqomU_UHM_SQ_fqnjwQR5yqIp1Qg3elQ6Xeb_kOHXnNlDXEJVxf0f6kyiEu9Yx4W8zuRqCdG52-Keoo6OoOwZzsYNbaE_2_EqC3enINOSrF17_ko4YfIX35_fIlhLT1qrxOifDMKqJhtnXtTM4gySHYvBymeCKmyHPoZMyLMa4EYpwcJKgKW87hinT2yh4q0L7vYgHImtN_6cqsjv0i4WZK4iTVtTXRRfNGMTgN6JupoqRrzDCBqFUQRBZUoNKiLzo_m8ZnutCu5qKvlGDLdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المبعوث الامريكي توم باراك يبلغ قادة اقليم كردستان العراق أنهم سيسحبون قواتهم من أربيل والاقليم في شهر التاسع من العام الحالي.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/78982" target="_blank">📅 12:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euuxFV11RqNWdiKHR3iu4etNHhp3cin99TJHxvZG-jSeDF18CfzyD96ndm5db9Z0kJIFmD4_BT2vUqz2wf5NbptWuTJIRr5yY8xTV_k_oG8uuR1y3-oPl-aXkQRLvuS6IuMI46wZZZAXRPU4A6engG3sXmM7ISpiudnGz01G53uUqdvUtbuzsSDTGHTFz9SRFceEZSJ7c9qQnFXuLP2r-yJgpFy3lam6UTDGFabO3nCi7eLvSM_iy79VIubrBkNBZc5veFlLkiC7b9FPqUXuNwqARk7W7L6KLeEvNaWpwaIZcGiHzbHBExalu15dUH341w70g0zFptoyPXleb-Cufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78981" target="_blank">📅 12:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-06-2026 تجمّع لجنود وآليات جيش العدو الإسرائيلي في بلدة القنطرة جنوبيّ لبنان بصاروخين نوعيّين.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/78980" target="_blank">📅 12:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني: واشنطن تعهدت بالنيابة عن حلفائها بأن الحرب ستنتهي في كل الجبهات، بند بمذكرة التفاهم يؤكد صراحة إنهاء الحرب والعمليات العسكرية بكل الجبهات منها لبنان.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/78979" target="_blank">📅 12:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني:
واشنطن تعهدت بالنيابة عن حلفائها بأن الحرب ستنتهي في كل الجبهات، بند بمذكرة التفاهم يؤكد صراحة إنهاء الحرب والعمليات العسكرية بكل الجبهات منها لبنان.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/78978" target="_blank">📅 12:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc27dffdc2.mp4?token=qopE5VceYdb5Dbk9SxXpu2HijpsNESw7z_oN8paCkuoU02UdN6K_MY0alnRIxo6E-H7qu2tdryf594oFH8al_Bjf02_CekwJIZDezBenStWGVFr2cfOQRyZfanq-agRk5tqyQWOqGfdtURqSTT4uqgi189QjhMv6zQ5xpDeOSbHNoZHB0yi6z0iaKIJYkaqm-eZuyGw2sPo9m7epPK8sweaNgvYZG9fJP-N2NdoifGE7hqF_SOoguAQL2h0Zp33S8uUwTvn2nzKRz9eI1NqXGVisZgNdcIQijqLVm_U2u5ncloGRKW9Z4iLtnXgneU3vk9CQiImtO7vlelPuR-KFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc27dffdc2.mp4?token=qopE5VceYdb5Dbk9SxXpu2HijpsNESw7z_oN8paCkuoU02UdN6K_MY0alnRIxo6E-H7qu2tdryf594oFH8al_Bjf02_CekwJIZDezBenStWGVFr2cfOQRyZfanq-agRk5tqyQWOqGfdtURqSTT4uqgi189QjhMv6zQ5xpDeOSbHNoZHB0yi6z0iaKIJYkaqm-eZuyGw2sPo9m7epPK8sweaNgvYZG9fJP-N2NdoifGE7hqF_SOoguAQL2h0Zp33S8uUwTvn2nzKRz9eI1NqXGVisZgNdcIQijqLVm_U2u5ncloGRKW9Z4iLtnXgneU3vk9CQiImtO7vlelPuR-KFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مرور ناقلة النفط الخام الإيرانية الأولى "ديونا" المحملة بالنفط خارج الحصار الأمريكي.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78977" target="_blank">📅 12:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLbUS8PMxU1cJ0kodBD-jJvmORYkY4dO1UEIywl8U27eNuAMi2GHihAMjRi-6Ko32v04VC0O5lvBsDWFebhJGfQQMXZHj8xcn0rRLRblr0S2pk0_UtGY-AiqPLLDGDA3ROxCrAPmEpZ28lyjnFZd91_1lAhsC3JnB-VJCzXwQmfmOQGjlAO8wivddM7Ks_BTJvQ1XyuwMUHG03pQi7dj-xQWynuBpMKSB64BPMLhrftmtztaRva8Gf3kAFuQQnO-CnWLcWgtKg9OZpo0LWRFUME7IwWRn-DO2jkV5oWvq1GoTW-dixC4Qo2_ruTzj3VsLK3oJCSdjxZ99RdslGavdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مرور ناقلة النفط الخام الإيرانية الأولى "ديونا" المحملة بالنفط خارج الحصار الأمريكي.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/78976" target="_blank">📅 12:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc22d2744.mp4?token=PJ_Wzd6glHuQeemMnJidjR8nYwIuIhtLc9m84RuoTE5JARArQqHHZN9s2lemCqLyxGpXVwpUEUtGziw4PHahk8VEw1TUZCfZ_8RQmwVonslWoifsa30IqcFPrsxsPX9jTJMIfnDRxAkMmFwRV6jwDRCD3rZWN2ANebtYgHuLCDahSSiVaWeXxcXAtD5IKwOm9Flj6oi-Kp5VBO23OC0CXqNQy7XpoR_P1lcMUxm5hD7X32Mbb16T5Mi5_iJN8C-boIlRmO28EpZLX_Xh38r-lpTlGLYhZgCXqK77XR2tANgWNkxlr8y3EYUM538tAmLhLSAAcKMdtOt5EwuWvUe66Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc22d2744.mp4?token=PJ_Wzd6glHuQeemMnJidjR8nYwIuIhtLc9m84RuoTE5JARArQqHHZN9s2lemCqLyxGpXVwpUEUtGziw4PHahk8VEw1TUZCfZ_8RQmwVonslWoifsa30IqcFPrsxsPX9jTJMIfnDRxAkMmFwRV6jwDRCD3rZWN2ANebtYgHuLCDahSSiVaWeXxcXAtD5IKwOm9Flj6oi-Kp5VBO23OC0CXqNQy7XpoR_P1lcMUxm5hD7X32Mbb16T5Mi5_iJN8C-boIlRmO28EpZLX_Xh38r-lpTlGLYhZgCXqK77XR2tANgWNkxlr8y3EYUM538tAmLhLSAAcKMdtOt5EwuWvUe66Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد من إطلاق صواريخ اعتراضية من مستوطنة المطلة شمال الكيان المحتل لاعتراض صواريخ حزب الله.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78975" target="_blank">📅 11:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7652e2bde8.mp4?token=L-sseXeiYOIYla0uX3kUs4aWr7H6_dTEBzn-t0233WDplbdAN3MsGdpHzPBQf6xOaTJL71D7hzGNAgpWjfseS9RP70uLBPBPNNeqkN2kEl9hpVRuuFuWojiddleEgj8fUYqNnfbeYuf2oOn0nUnqhtDMxLCSS5agzDPmPIWqu4ld7BdzVqi8-9gVipNs1bWix1RjcX5fX99l4b3m4CQ4pub8pJM3qiI0oK3gXoS4UnU6nE0ZQxHudM1BUVDNqkz1zPOiOBwhhkDQqe3zUnSCroQcpOXhI0tZOFeYjwgGcRAGlOOmeLl8cs8vc0ZVJ1c1wcZDH_QRNvb7giZBmivPL44tLYytmESWLQtTc_H3kvmX5wNfbITvAJUBjQIX4gIHz9G4oRUljH7XNXMzx1QzxzIdyH6woheVugrAPTMCDf59Zos4Fp3DozxloIWpGtDe4bqtVz2ird4fmQbOT-EzQ1dGc7DwOAxqewwO2VFNqGZnOqkfEtSsWZ2fwkCy0yszwCMrTCNPXzldA0QStHF0-5C2ULG_XohhKLIwRgrCwTvPP666sFM-IUlzxFLMcKcf5ZLVc9U_Ny_wg9MF3pTs1lVIoBvRayTnU7kRP0nVwO-mbjmXW6b9ex9uOtIVSQQpttOWLKJqrEyFL_y-KaYLwsJOwoIpZpUMZxgE1bLLEcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7652e2bde8.mp4?token=L-sseXeiYOIYla0uX3kUs4aWr7H6_dTEBzn-t0233WDplbdAN3MsGdpHzPBQf6xOaTJL71D7hzGNAgpWjfseS9RP70uLBPBPNNeqkN2kEl9hpVRuuFuWojiddleEgj8fUYqNnfbeYuf2oOn0nUnqhtDMxLCSS5agzDPmPIWqu4ld7BdzVqi8-9gVipNs1bWix1RjcX5fX99l4b3m4CQ4pub8pJM3qiI0oK3gXoS4UnU6nE0ZQxHudM1BUVDNqkz1zPOiOBwhhkDQqe3zUnSCroQcpOXhI0tZOFeYjwgGcRAGlOOmeLl8cs8vc0ZVJ1c1wcZDH_QRNvb7giZBmivPL44tLYytmESWLQtTc_H3kvmX5wNfbITvAJUBjQIX4gIHz9G4oRUljH7XNXMzx1QzxzIdyH6woheVugrAPTMCDf59Zos4Fp3DozxloIWpGtDe4bqtVz2ird4fmQbOT-EzQ1dGc7DwOAxqewwO2VFNqGZnOqkfEtSsWZ2fwkCy0yszwCMrTCNPXzldA0QStHF0-5C2ULG_XohhKLIwRgrCwTvPP666sFM-IUlzxFLMcKcf5ZLVc9U_Ny_wg9MF3pTs1lVIoBvRayTnU7kRP0nVwO-mbjmXW6b9ex9uOtIVSQQpttOWLKJqrEyFL_y-KaYLwsJOwoIpZpUMZxgE1bLLEcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: سنطرح الملف النووي وإلغاء الحظر في المرحلة النهائية من المفاوضات  إعلان نهاية الحرب أهم ما حدث في المرحلة الأولى من الاتفاق وتم إعلانه صباح الاثنين  جولة جديدة من المفاوضات بين أميركا وإيران ستبدأ في سويسرا يوم الجمعة  البدء الرسمي…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78974" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني:
سنطرح الملف النووي وإلغاء الحظر في المرحلة النهائية من المفاوضات
إعلان نهاية الحرب أهم ما حدث في المرحلة الأولى من الاتفاق وتم إعلانه صباح الاثنين
جولة جديدة من المفاوضات بين أميركا وإيران ستبدأ في سويسرا يوم الجمعة
البدء الرسمي لتنفيذ مذكرة التفاهم سيكون يوم الجمعة
نهاية الحرب في لبنان موضوع ملزم لنهاية الحرب مع إيران
سنناقش الملف النووي والعقوبات خلال فترة المفاوضات التي تستمر 60 يوما مع واشنطن</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/78973" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59974eb34.mp4?token=S5WZlpxBV5t00x_F57Z27elcDgLQ-AWzNzolIIwShr5WHPwyRcWyhCkBqlhdtmIzJdG6engfz0f04z58hWQ7LXXHkVIi7g8-b-iTq-4uoVjrt2YHNUCTIgiQVDO30h4afZiCpaDchCRIkc3Fxr84M-uVD4nluE3LIAlOjQa5Z1yiTXbRa8kgtPfICgD5ZoSh9lMqukWloJULi0narnfmX6cLAEjnljhCbUDrwPaE-_6KCM3z520ZZYBjyPF4TTUnngweV4YcHAr0DuAaZoaBYpiu_DmSFWX0Zck6_j9_5DHSkZ6w6DKSaAEVtzb8LOIZVaGLCquOb_l_sOFISsIADg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59974eb34.mp4?token=S5WZlpxBV5t00x_F57Z27elcDgLQ-AWzNzolIIwShr5WHPwyRcWyhCkBqlhdtmIzJdG6engfz0f04z58hWQ7LXXHkVIi7g8-b-iTq-4uoVjrt2YHNUCTIgiQVDO30h4afZiCpaDchCRIkc3Fxr84M-uVD4nluE3LIAlOjQa5Z1yiTXbRa8kgtPfICgD5ZoSh9lMqukWloJULi0narnfmX6cLAEjnljhCbUDrwPaE-_6KCM3z520ZZYBjyPF4TTUnngweV4YcHAr0DuAaZoaBYpiu_DmSFWX0Zck6_j9_5DHSkZ6w6DKSaAEVtzb8LOIZVaGLCquOb_l_sOFISsIADg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇱
الجيش الأمريكي يبدأ بإجلاء طائرات التزود بالوقود المتمركزة في مطار بن غوريون حيث تمثل حوالي 20% من الطائرات المتواجدة حالياً في الكيان.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/78972" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📈
بورصة ICE في لندن: ارتفاع أسعار الغاز في أوروبا بنحو 1% لتستقر عند حوالي 512 دولارا لكل ألف متر مكعب</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/78971" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2de826483.mp4?token=rIaXc8QgioQugoBgl1upgAS9TWffEwDr-uPA23r0_LdHptvCRd2xpLW6zyxLbbKsoA92QP0ZWS0yw17r8cI8iFjGhrS1lwNiACUqSOskNTK9WiaC8l1RgWhTj39hpKuMIEGjsHuMuiYi_Vhmrh9gC82wUBpJVCwJCnpoTeNmOj9VKMPbFhWsKAhOgPDakDpPdo3a_MfWPUDC9H84M3GnOP-zNWT8R12Y7hfncXn58jGDec_2Y-K7WtSisQi8VktU4FmTQVt_42cwx65fLn25cNmQx0Sx1Ih5x9Dv8sW6j9VYsNKvXLTVWJ4O6r94fQSgbYfAoNddfotJgBb_-tahlG4fw55gwuo-3Ycjv0j465dJL3OuEBNzz-LCwuEln-LhAU--mDMApwxmbwfm9eZAxff_DHbe0VhUMePyoIF2MkrSPOdV0HWbVPHZmErfM9wlAVpZ8daFS2XN1c9ro1zWR1WFxoSj0YNebfzXZY46aePkPGjLas1scG3uvKfGPL44PeBvfKW8PdS2vK342J290PMl9JFlv9jxYCCqdLJ3nEfFMecYkkYm-ZaBPsBvDjh3aaSVMpuRB_8s3JnLeUHU7Hm1ztzBsxrhR-uUWbJBbsY01Vv8jUxhY_-oxDDK0ixgJ8VOQyg3d_A9nsA4hp7leySnDIXw6KrZULMtO7sYdOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2de826483.mp4?token=rIaXc8QgioQugoBgl1upgAS9TWffEwDr-uPA23r0_LdHptvCRd2xpLW6zyxLbbKsoA92QP0ZWS0yw17r8cI8iFjGhrS1lwNiACUqSOskNTK9WiaC8l1RgWhTj39hpKuMIEGjsHuMuiYi_Vhmrh9gC82wUBpJVCwJCnpoTeNmOj9VKMPbFhWsKAhOgPDakDpPdo3a_MfWPUDC9H84M3GnOP-zNWT8R12Y7hfncXn58jGDec_2Y-K7WtSisQi8VktU4FmTQVt_42cwx65fLn25cNmQx0Sx1Ih5x9Dv8sW6j9VYsNKvXLTVWJ4O6r94fQSgbYfAoNddfotJgBb_-tahlG4fw55gwuo-3Ycjv0j465dJL3OuEBNzz-LCwuEln-LhAU--mDMApwxmbwfm9eZAxff_DHbe0VhUMePyoIF2MkrSPOdV0HWbVPHZmErfM9wlAVpZ8daFS2XN1c9ro1zWR1WFxoSj0YNebfzXZY46aePkPGjLas1scG3uvKfGPL44PeBvfKW8PdS2vK342J290PMl9JFlv9jxYCCqdLJ3nEfFMecYkkYm-ZaBPsBvDjh3aaSVMpuRB_8s3JnLeUHU7Hm1ztzBsxrhR-uUWbJBbsY01Vv8jUxhY_-oxDDK0ixgJ8VOQyg3d_A9nsA4hp7leySnDIXw6KrZULMtO7sYdOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدث أمني عند معبر حشمنوئيم في محيط رام الله الضفة الغربية بسبب إطلاق نار على مركبة</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78970" target="_blank">📅 09:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78969">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
رئيس مستوطنة المطلة قرب الحدود مع لبنان متحدثاً عن نتنياهو: إنه منفصل عن الواقع، أدعوه للمجيء إلى هنا لرؤية الدمار عن قرب.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78969" target="_blank">📅 09:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a58183f17.mp4?token=mEbdMLJpTVQ0aF8N4iJrjqxfVLpu_C5C2nPz5_kx3YHdr4EBPItImGMFevgsMA-m_-YQgS3st7cAtQ92Hlp3gvJ9u-ohW57s2HJSlp3Vhz0gSZxc8Z4OrIYcSaZev-1a3wbjxM1_YF80AqMpneWyvww-zNQHE4g-xAbQuylQ2Ic3P_0-j2KBpbO3xxVFn5Ko4lHiTn387TEJY13nRdCuJlgRGtMdnanWTk9aTwXwp6PL3VGuWVFaUYkJSU5fqYe0jWW4X2GExuvJdS5KmL4PhnTKlGpey8sGKF8AsaBRp-D1rU8SSe-xkj9AtMo_Ghw9lBP-LnjzBt8RiZx1_pIxc5HxtYWc72J_j8OprHJHA28R3owm0ON0DJ68eqT1ZG8mMOQNwMPjwUNMRbtTNaQ7qKITOU-H4E6X2NaL2UyjOoSgQH8e-w8Jcgntuo-9T12l18bbmcDKvaIjW6E2D8eCR6mJ8Y0y5S3PJaGLZFbn151CwgDfaYJx4e-TFEF1Sh44aotbVS3zU06VXn1QlwMLowVIrx1dmIX08-PmdKqMJwkMDJtJkiy7UPOSnyfcu1T02bcbv61D6Z4Z5ixZsTrBnKlRoEN_HJ_trPsv_ksqlluhDKf8YwcMlFaVHk9OxWFbUxAGSBTY0Ix2bkl0QKwKCVPSEy7kjnUYH_LdemeuEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a58183f17.mp4?token=mEbdMLJpTVQ0aF8N4iJrjqxfVLpu_C5C2nPz5_kx3YHdr4EBPItImGMFevgsMA-m_-YQgS3st7cAtQ92Hlp3gvJ9u-ohW57s2HJSlp3Vhz0gSZxc8Z4OrIYcSaZev-1a3wbjxM1_YF80AqMpneWyvww-zNQHE4g-xAbQuylQ2Ic3P_0-j2KBpbO3xxVFn5Ko4lHiTn387TEJY13nRdCuJlgRGtMdnanWTk9aTwXwp6PL3VGuWVFaUYkJSU5fqYe0jWW4X2GExuvJdS5KmL4PhnTKlGpey8sGKF8AsaBRp-D1rU8SSe-xkj9AtMo_Ghw9lBP-LnjzBt8RiZx1_pIxc5HxtYWc72J_j8OprHJHA28R3owm0ON0DJ68eqT1ZG8mMOQNwMPjwUNMRbtTNaQ7qKITOU-H4E6X2NaL2UyjOoSgQH8e-w8Jcgntuo-9T12l18bbmcDKvaIjW6E2D8eCR6mJ8Y0y5S3PJaGLZFbn151CwgDfaYJx4e-TFEF1Sh44aotbVS3zU06VXn1QlwMLowVIrx1dmIX08-PmdKqMJwkMDJtJkiy7UPOSnyfcu1T02bcbv61D6Z4Z5ixZsTrBnKlRoEN_HJ_trPsv_ksqlluhDKf8YwcMlFaVHk9OxWFbUxAGSBTY0Ix2bkl0QKwKCVPSEy7kjnUYH_LdemeuEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماهير العراقية تشعل الأجواء في ولاية بوسطن الأمريكية قبل ساعات من بدء المباراة بين منتخبنا الوطني والنرويج.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78967" target="_blank">📅 09:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حدث أمني عند معبر حشمنوئيم في محيط رام الله الضفة الغربية بسبب إطلاق نار على مركبة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78966" target="_blank">📅 09:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4be2373.mp4?token=KtpWEg15_xxreh_Jr-AOJOZ6_Q6q9zDT3GU9ysZUV7oUX-96GSA3vuKFndVEif_d7dEeRW_1IgUrLx5Vt6T8xyEBYi_d3SYwzDgyikOujIhU3_EeNlkSjeH284MH39vIvHKiscqkwIZbBvDJsxlAp8Li9uhLMLAKl541jv0FMZNBrZcQd6wG9egWl0jG3fuFbWEo9DaQSv37xaET0I8KaqzIm7tgY5aWGanEjVFfY7FTHfNTNehjbRIgac-j7RBMEfwy_Z6kqa9lgdRZYkLzjAnUvBpZPsxC3LlRITJI1Qc8YKPVrrtaRT75gEBPvjM15S0NX7_edRKwrP09Lc5vnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4be2373.mp4?token=KtpWEg15_xxreh_Jr-AOJOZ6_Q6q9zDT3GU9ysZUV7oUX-96GSA3vuKFndVEif_d7dEeRW_1IgUrLx5Vt6T8xyEBYi_d3SYwzDgyikOujIhU3_EeNlkSjeH284MH39vIvHKiscqkwIZbBvDJsxlAp8Li9uhLMLAKl541jv0FMZNBrZcQd6wG9egWl0jG3fuFbWEo9DaQSv37xaET0I8KaqzIm7tgY5aWGanEjVFfY7FTHfNTNehjbRIgac-j7RBMEfwy_Z6kqa9lgdRZYkLzjAnUvBpZPsxC3LlRITJI1Qc8YKPVrrtaRT75gEBPvjM15S0NX7_edRKwrP09Lc5vnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فكرة رفع علم الأسد في بطولة كأس العالم كانت حلما لترامب ونتنياهو لكن الأحلام حين تتقاطع مع السياسة غالبا ما تستيقظ على واقع لا يشبهها وها هو علم الجمهورية الإسلامية الإيرانية علم (الله اكبر) يزين ملعب لوس أنجلوس.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78965" target="_blank">📅 05:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29d91e814.mp4?token=jFiI9z3VmgGEJhbjm7BzrEsU-xG-rM7oFL_3xDso3x_rnfR3nLlH3yJ6u0Zd1RmONCTFkjq0RK_36s4y6-RrdDg3mdYzQS3TVeIh6xpiqp_OKlhwedGiRMlC8_8dgrgmiPCMMAGx8vOTU0N1bs9dfcY_koXvqf4bRwNR2MXyGQq0IRZ7z6sewnVP7ZQFsE7KpddwUPSHXMdHzAsHogL1TsYQkM1-wGg9GZto44DwTNeaHp8CQVHrVkQPGAoLLbUxg3bcoKd6DadkYXn80acS6f25EBNPTmWIWJtB4JbGWra4sUG2HuJU_NL6RbBHO5Q2cVnTmc97QX3E9iUI8vRqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29d91e814.mp4?token=jFiI9z3VmgGEJhbjm7BzrEsU-xG-rM7oFL_3xDso3x_rnfR3nLlH3yJ6u0Zd1RmONCTFkjq0RK_36s4y6-RrdDg3mdYzQS3TVeIh6xpiqp_OKlhwedGiRMlC8_8dgrgmiPCMMAGx8vOTU0N1bs9dfcY_koXvqf4bRwNR2MXyGQq0IRZ7z6sewnVP7ZQFsE7KpddwUPSHXMdHzAsHogL1TsYQkM1-wGg9GZto44DwTNeaHp8CQVHrVkQPGAoLLbUxg3bcoKd6DadkYXn80acS6f25EBNPTmWIWJtB4JbGWra4sUG2HuJU_NL6RbBHO5Q2cVnTmc97QX3E9iUI8vRqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بداية مباراة المنتخب الايراني و المنتخب النيوزلندي.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78964" target="_blank">📅 04:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrGSIz15SKFDdj1gJXwJBjig5cSZwKBlD4Obz1VYM2w8iAu6o_WHnODHr5TydCluxM4EeGf32qWbNLNkFfNBXZeU-lTDFzs0sv94vp6qH7Z3jEcK8gIftzgK7PRXfwYOXMfcJCOEtOMzLuZs4if1ZUuXmcjltrCf1HZvf0GoQe1GnPILlLY7p6nilNo0bf0C4Y7RHpDRKfP-EvbFtM-lC4f8n_eT2WPxu4TvgGuFtDMDoZa2m8TIsxwf1a5DbP9SWv7WtpL3qUA4udV4ED-zTurDKgxxSkZB4QqpPtTjs_g4W89VrSCBeodM9XjOV27RsamUjDi7DV4dLjBguxO7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:وافقت إيران على عدم امتلاك سلاح نووي أبدًا! كما أن قصة دفع الولايات المتحدة 300 مليون دولار لإيران هي أخبار كاذبة، نشرها الديمقراطيون!!!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/78963" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئيس المرصد الوطني للإعلام "خالد السراي": أبو آلآء الولائي رجل شجاع ومقاوم والإطار التنسيقي أساء له ولم يدافع عنه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/78962" target="_blank">📅 01:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMphCccjRJEcUh1jzr71AkNuzhR__4VgeCsg8U2_QG5g48XrwVuuFeuPYoVbRq6ffttDNyu7BEiZAh3fANUC4j_HW1_6WCy_CcdiT0Bg97V7tCccSZG0ut_Akln4Q0ySb8mnmopt04bNpME_3jSqZNbI_oCEs3JpnhImznwFvmwi746WYpOErcDuFgn8JdeKiOppYvmh3Ba7716j9-TeyvpwDJpI0ipc0jTBeGH_N2ZpzsDwZ7jMjPCckKBAT2Cf0ujJ6VzkDCeBd4b0c0-YzX_p2YfBwC1pB7-48xYrqksOEzF-d110WtDqo8afFpEOWHNhaCl87uHnLF9eIJj-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحطم إحدى أهم القاذفات الاستراتيجية في سلاح الجو الأمريكي، من طراز B-52 ستراتوفورتريس، بعد إقلاعها مباشرة، فيما لا يزال مصير أفراد الطاقم مجهولًا حتى الآن.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/78961" target="_blank">📅 01:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصدر امني لنايا
...
🌟
🇹🇷
الجيش التركي سمح بعودة سكان 25 قرية في منطقة باتيفا بمحافظة دهوك شمالي العراق ضمن إجراءات تنظيمية شملت فرض قيود على حركة السكان.
🤔
و تضمنت الشروط منع التجوال من الساعة 6 مساءً حتى 7 صباحاً وتقييد الحركة داخل القرى وحصرها بالطرق المحددة من قبل القوات التركية إضافة إلى تنظيم شراء المواد الغذائية بكميات محددة لكل عائلة!!؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/78960" target="_blank">📅 01:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22131f5c0.mp4?token=SnQOOjMNBAKrq0UnMV9WAxRtDdry1ADuA7tsW_unCwGdume3ASaXVEvJO6i66wfS6wh2O2pRHKqTBz6iZ5H91YXafEQ7cMGs_OJG_DuFngRYesPzyt2k4pXD_60iYHk-f0FqODvDJhHuX7jahVD6569echMMNJQ33DjunVFl93l0RKIElM3uztVFbZUtJZreXlfjVRVgwLlocsFhExcZGPXN1Zg3QWutX0m0-h39TLwo5DHhJTP-VoLOL135ezjNxovNTaNwNFZtWnGFKcKDQ70BS3dYKWQfHclvFmlaFqQQFr9T2Li8aEoyEf3HR1pOCq2wH_t2LaxS-4_0xNZq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22131f5c0.mp4?token=SnQOOjMNBAKrq0UnMV9WAxRtDdry1ADuA7tsW_unCwGdume3ASaXVEvJO6i66wfS6wh2O2pRHKqTBz6iZ5H91YXafEQ7cMGs_OJG_DuFngRYesPzyt2k4pXD_60iYHk-f0FqODvDJhHuX7jahVD6569echMMNJQ33DjunVFl93l0RKIElM3uztVFbZUtJZreXlfjVRVgwLlocsFhExcZGPXN1Zg3QWutX0m0-h39TLwo5DHhJTP-VoLOL135ezjNxovNTaNwNFZtWnGFKcKDQ70BS3dYKWQfHclvFmlaFqQQFr9T2Li8aEoyEf3HR1pOCq2wH_t2LaxS-4_0xNZq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هروبًا من المحسوبية وتدهور الأوضاع المعيشية في إقليم كوردستان العراق،
لجأ شاب كردي إلى ألمانيا لكن رحلته انتهت بالقبض عليه وترحيله إلى بغداد بعدما وقع في اشتباك مع الشرطة الألمانية أثناء اعتقاله</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/78958" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
الاعلام الايراني:
تم البدء بتنفيذ رفع الحصار البحري الأمريكي المفروض على إيران، حيث عبرت ثلاث ناقلات نفط وسفينتان تحملان سلعاً إيرانية أساسية "مرتا" عبر الحصار البحري الأمريكي.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78957" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7cdxKlKBohHESKxumFinUW7kxnm_jhD7yLrKNhkX3GdxdNHN-PYtzmga77TqGohTIHGDj_kWOloTWW0I1bsiqnjXkvzhgWot-8ZTzJ1EdYlIJHF8YI5sfK9VNvRZqJP_avMUBYHeJMYG_vwwgzZUJ2sLDxFKLRQZuoTdQr_CZK-DQ3GZfQuRSpX0jARzowkQl7kn8HDXfbPxuiH8DE74QRz-rqUA4P2KfInxUFI1Cpcl5ZixMaWgjQ33J97zV_Y0W-H6uwGPM15i-muLVgZPkzbi5f95Zo-7lrlU-Sm1q0-uXe1_wmfsu3PA0H-uR6fPTElC1sEsWsOQXYRAoh1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
في ظل تعثر السياسة الخارجية الاميركية واقتراب الانتخابات النصفية للكونغرس لجأ الإعلام الرسمي إلى استخدام البروباغندا لترويج لإنجازات استثنائية لإدارة ترامب رغم أن العديد منها يندرج ضمن المهام الاعتيادية للإدارات المحلية ورؤساء البلديات.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/78956" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilZg1XrhX_MD3sGOiiSy2MVezbuhJNMfvkzJpnJ1LPGLz216mfOa99-pd0t-UiJfI9h0j8OjkGnAUXkCHpN0YF-X2dvDJQ59KCo_BIQP4Gd-lFK5DTx_1N3p9UNVGWSUw76aOY0cVReatGcr1WeKyDN8JXiDtQFS1COgCwB_FBOL3DAO7UCvDTGcHSHuyGcqntKBnOdpJojKgqQxUs3EbBBtVzJlhyTC1vbkrdmgPkYPZNFp8gTDcA3hruV_cmzi32apbs-I03-jR64jDlxwPkmhDZ0CW14NH8f1Yl4BQCvgbLmgLnPXqQpROJVc_OngLVDo7aNKOlcG-8i28rYHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الحاج ابو الاء الولائي:
وإنا على العهد باقون وعلى النهج ثابتون(لن نساوم).</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78955" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الطائرة التي سقطت لها قدرة على حمل القنابل والرؤوس النووية   وشاركت بهجمات على المنشاءات النووية الإيرانية …</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78954" target="_blank">📅 23:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
‏عقب تحطم قاذفة B-52 لاسباب مجهولة، أعلنت قاعدة إدواردز الجوية إغلاق المطار وتحويل مسار جميع الطائرات القادمة، كما علّقت جميع تصاريح الزيارة غير التجارية حتى إشعار آخر، لتكريس موارد القاعدة بالكامل لعمليات الاستجابة للطوارئ والتعامل مع تداعيات الحادث.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78953" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb2aab1af.mp4?token=gsGnLol9x-I_9onKDFGeREu_DQxl82700CBn5O1Z0B89qQsyIrIiljrWM_om_RL_qv_2zn75_KR8HemyizPmOSXNdemkl9mms4lv8a0F4T5RIVm6RGRYvlhvt4wO5TF59QYQzzljPqlHusNEZbbbkhcbMMgJHs4xuEhAqLMQQVMEE2U_IPOE2kTTXQmxU2lDVIgnAyhjuF5NnVkA5WQRLzjOtphTh_aH_qn0LXNqBoImrSFk8xTkgxiB-6SIKdJFJAJSSKiMUDguVvUR_IM1nSCvnfFIAohBrt-i3-_ThxcKeCLxf9AgK5Nmx-HP73oQMf_Uyr4xaD60giR-xMLQKq6O0wqfX1e3cnYk7p8VyeXseV-fcwQ1E02n8h-F6guM88_Kkig0AWoZ2ybz2yd6sLhJZqSXsa2EvyUYkYDhc6ZFBa41CXD93t6CWp8LzpsbeKU5P9RQywmuORHz1Bcu1BP6lu7QCfunGot5tAizncwjnqfngdftzOAxUIw0__WSMnlCNfUbf_zbSTCG6Y2TemmWo6DdkQQi4cL8Rg8a67u9-C6vUX9DXDTgTDUPKJWTyLgvpM9POfncuIopVWvM3MOqIsRMv-sldGIgnBs7ZrwBZ4lMVTM1eWuHQnj8jPV7yoM_mhCD1deCBUDmvfolp9Gg2ffiFm6ARy4ype63Aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb2aab1af.mp4?token=gsGnLol9x-I_9onKDFGeREu_DQxl82700CBn5O1Z0B89qQsyIrIiljrWM_om_RL_qv_2zn75_KR8HemyizPmOSXNdemkl9mms4lv8a0F4T5RIVm6RGRYvlhvt4wO5TF59QYQzzljPqlHusNEZbbbkhcbMMgJHs4xuEhAqLMQQVMEE2U_IPOE2kTTXQmxU2lDVIgnAyhjuF5NnVkA5WQRLzjOtphTh_aH_qn0LXNqBoImrSFk8xTkgxiB-6SIKdJFJAJSSKiMUDguVvUR_IM1nSCvnfFIAohBrt-i3-_ThxcKeCLxf9AgK5Nmx-HP73oQMf_Uyr4xaD60giR-xMLQKq6O0wqfX1e3cnYk7p8VyeXseV-fcwQ1E02n8h-F6guM88_Kkig0AWoZ2ybz2yd6sLhJZqSXsa2EvyUYkYDhc6ZFBa41CXD93t6CWp8LzpsbeKU5P9RQywmuORHz1Bcu1BP6lu7QCfunGot5tAizncwjnqfngdftzOAxUIw0__WSMnlCNfUbf_zbSTCG6Y2TemmWo6DdkQQi4cL8Rg8a67u9-C6vUX9DXDTgTDUPKJWTyLgvpM9POfncuIopVWvM3MOqIsRMv-sldGIgnBs7ZrwBZ4lMVTM1eWuHQnj8jPV7yoM_mhCD1deCBUDmvfolp9Gg2ffiFm6ARy4ype63Aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
العراقيون يطلقون وسم #الله_يستر  على مواقع التواصل الاجتماعي ؛ كون كاتب المنشور في موقع X قد كانت آخر نصائحه لمارك سافيا الذي يعتبر أقصر عمر مبعوث أمريكي في تاريخ امريكا ..</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/78952" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رويترز : تحطم طائرة بي-52 ستراتوفورتريس تابعة للقوات الجوية الأمريكية يوم الاثنين بعد فترة قصيرة من إقلاعها من قاعدة إدواردز الجوية في كاليفورنيا، حسبما أفادت القاعدة.  ‏"أرسلت فرق الطوارئ إلى موقع الحادث فوراً والوضع مستمر"، حسبما قالت القاعدة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78951" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc8a91edc.mp4?token=eAmu1Dbbx8q_8eptPF4TjXtpUYB8oJDAtLqefkTpKReRHr7LuYTVABZzttZyoR9s2Rmh5LhqzQ1Lef_Xst5qtYtGJ3zXiW_tm9SlkZDSH2ljxM0m29hvyjRbUQGUMlLl5-9I4tjkZddJ7xWr8uu-yy-FZMxCSJWqfYJPJ-H1FrNVB5WyDxpouvZM0feOkN-Rw1uFjl-PRJvj6iu3vBs2twRCJX2AsSm-dnkfWgL7Vn8dHM1EaowR06Ucd9kgnmpbiaVYJpdz-wY5aG3K6p7RuWtqZXdp8NsRmR1lnjzsPRq4l6nzUpQ82pN0BxirIKUpv5YgageA4I4tYtkFo6a92Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc8a91edc.mp4?token=eAmu1Dbbx8q_8eptPF4TjXtpUYB8oJDAtLqefkTpKReRHr7LuYTVABZzttZyoR9s2Rmh5LhqzQ1Lef_Xst5qtYtGJ3zXiW_tm9SlkZDSH2ljxM0m29hvyjRbUQGUMlLl5-9I4tjkZddJ7xWr8uu-yy-FZMxCSJWqfYJPJ-H1FrNVB5WyDxpouvZM0feOkN-Rw1uFjl-PRJvj6iu3vBs2twRCJX2AsSm-dnkfWgL7Vn8dHM1EaowR06Ucd9kgnmpbiaVYJpdz-wY5aG3K6p7RuWtqZXdp8NsRmR1lnjzsPRq4l6nzUpQ82pN0BxirIKUpv5YgageA4I4tYtkFo6a92Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني الإرهابية تقتحم مدينة تدمر بريف حمص السورية وتقتل عدد من الشبان وتحرق ممتلكاتهم تحت عنوان الشبيحة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78949" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_zljPd5wjWgGv2s2EpkIMBh5DvYzd0shiixeY9F3gVy66ivcg4vKp1TpzmFeSQIEBc8PwTSq3NAy1vwDRYmQ4cwT2EEXL5zOLAHAHDAsaI0l02GrGBOj0sqyo6KPwiwq5yJsPWHsfIGz4Yckfmb7DxA_9vcAr35RWVxBCkhsbGcojMLKTov4Q4bhC7LF0uodRuGfouAB11VTrB5exnvuf9PJpTdUrKyVocAKViPKyPO7AuUi2dh8zCLFW5N6zSTEntVCatGEbt2ybJojc0ulehkOJlNozetx-31wP_Q6T8o7Ogx33oxfAegnjBNMqA2rXr6W6-JWufLY-4B6btVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
العراقيون يطلقون وسم
#الله_يستر
على مواقع التواصل الاجتماعي ؛ كون كاتب المنشور في موقع X قد كانت آخر نصائحه لمارك سافيا الذي يعتبر أقصر عمر مبعوث أمريكي في تاريخ امريكا ..</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78948" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18ec03199.mp4?token=DptkWLYUADHe4F-IfPEdPnmliRBNR_aLm6JBhj8VYXSKzbhl7OLuj8qiUa5b4SCtcWCrE1SDthb6eKxQTNNkoqIKGqGlEdexB_mBYomjowgetBR1MZ_26GY0HWB-a4R7MBhyMA6ZCCZ181nA3wgZEvlwKFSPLbCl0xdwHIT_AeZH2cmUs-wgPPUvMdybbvunO0MEOXbfgBIemTfmiAjBamMgzT8oLO4K0GJFJK214Yo378WsO_S2barxV3RUfx4LQjbR-91WigOJg7jDYzO_GGHgy8dCyihgZLsbbVT4TFK1PmaO9j5HPNCqCBlNdFdc7Z4pCb_--EU8NOIjNO1qHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18ec03199.mp4?token=DptkWLYUADHe4F-IfPEdPnmliRBNR_aLm6JBhj8VYXSKzbhl7OLuj8qiUa5b4SCtcWCrE1SDthb6eKxQTNNkoqIKGqGlEdexB_mBYomjowgetBR1MZ_26GY0HWB-a4R7MBhyMA6ZCCZ181nA3wgZEvlwKFSPLbCl0xdwHIT_AeZH2cmUs-wgPPUvMdybbvunO0MEOXbfgBIemTfmiAjBamMgzT8oLO4K0GJFJK214Yo378WsO_S2barxV3RUfx4LQjbR-91WigOJg7jDYzO_GGHgy8dCyihgZLsbbVT4TFK1PmaO9j5HPNCqCBlNdFdc7Z4pCb_--EU8NOIjNO1qHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78947" target="_blank">📅 22:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41580de098.mp4?token=OPfUOv8efYpU9-iG6U1Uc4WXR8hSS_o0_qV6seENbQJYuTSFpUMAk_LYH0YynJlm-UlvqhN0lV5H09tVw-wZLZvd7kvyNdZpYrReURrCnZS3RynztedD8Um6sbb_gpnjTDsXoKVHv14N4A8rYWjyK8YdtvDxFiRV21sllF6gybq_M6RIHsqXzL1X7XwRDuacDQc4f979rFuSzsukp67JoTAvrGu1ceAOLt3t-xekLjUvFXM88IUdMTVor4x3SlfCcFgLEriWCkPEvLDuRMuYF31Jl2r10vsz4hA7l3303nUJLe2QS-lGjAQGN008R3nILcj9Reptnab2v5-lAfaoSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41580de098.mp4?token=OPfUOv8efYpU9-iG6U1Uc4WXR8hSS_o0_qV6seENbQJYuTSFpUMAk_LYH0YynJlm-UlvqhN0lV5H09tVw-wZLZvd7kvyNdZpYrReURrCnZS3RynztedD8Um6sbb_gpnjTDsXoKVHv14N4A8rYWjyK8YdtvDxFiRV21sllF6gybq_M6RIHsqXzL1X7XwRDuacDQc4f979rFuSzsukp67JoTAvrGu1ceAOLt3t-xekLjUvFXM88IUdMTVor4x3SlfCcFgLEriWCkPEvLDuRMuYF31Jl2r10vsz4hA7l3303nUJLe2QS-lGjAQGN008R3nILcj9Reptnab2v5-lAfaoSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحطم إحدى أهم القاذفات الاستراتيجية في سلاح الجو الأمريكي، من طراز B-52 ستراتوفورتريس، بعد إقلاعها مباشرة، فيما لا يزال مصير أفراد الطاقم مجهولًا حتى الآن.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78946" target="_blank">📅 22:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTrZrLKdlJ_Wm3qqmrZdA5dmb6gPGyF4YRXu8oAA2SOTP3d8w2RTHFCyU9Ki4sqr1XeuXobyO76rbm6cOPBIpA_UG9sqk41ZAXkATZYirvbyKO2AoUg5XHC5y0nSEsXB0eY73_W6cSHKosC6CpvFri9qI5PHip2xpnWjr8i37KLOb6uecl2vJyhcpSmH-m_Hy_qAIzK8RckytmMTVlk9eEq7Se8zzbGULkYjDPwZXAyQouoATNIkxROEcXOHsDVGrdAKqXjeu_S2RkZ07AM9j-ubVlHsCGgllbkqPEJC6-Eeqmw2-eSiCUJy0_iiitkjGdD1dJfI6wIU_-zRRuv3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0694a202.mp4?token=m2XTGsFgHMsbh3jz_RCisP0WCKmqVxCP3qf2H3cDR6kMmj08zH2uc0Cr4qzEWypD9qTu_ut04pntWcpP19bpVMz2NUrvpF5cJamEcaaXbvnx06FFovGb3ayGM9l2j3xE3173yrBrnKy8Say1MHN97YhuG6aIx5YISyTdKKemp5kIZXoY1XAmI5j3mAAdGPRkrPsk3wkpVdwjyhQR63cFyrMJf-8oEhVLMezUYKVpvJGx1JxWy8nZL0sjfRV6DwpWqsQ3FQqxOI2KqfMGBYP0GbCL3-NwqFLlVUC_mgFLImWpaPhP5SrKHy_i5-MI1DUnpkKeoPmSZQdhbNDAGzDIXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0694a202.mp4?token=m2XTGsFgHMsbh3jz_RCisP0WCKmqVxCP3qf2H3cDR6kMmj08zH2uc0Cr4qzEWypD9qTu_ut04pntWcpP19bpVMz2NUrvpF5cJamEcaaXbvnx06FFovGb3ayGM9l2j3xE3173yrBrnKy8Say1MHN97YhuG6aIx5YISyTdKKemp5kIZXoY1XAmI5j3mAAdGPRkrPsk3wkpVdwjyhQR63cFyrMJf-8oEhVLMezUYKVpvJGx1JxWy8nZL0sjfRV6DwpWqsQ3FQqxOI2KqfMGBYP0GbCL3-NwqFLlVUC_mgFLImWpaPhP5SrKHy_i5-MI1DUnpkKeoPmSZQdhbNDAGzDIXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حطام طائرة B-52 في ولاية كاليفورنيا</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78944" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7_6L1ypO_-jMVvoAENXjyK68tOkGhBXQ5Vj5toR2aveOXix0ydvj9NtenZKMKr9BnIsfLDn_CVeUDHw0jpJj5J66manaMxA2F3bpO6O_rU1D57FEakcC9UZtgDMKHOqROLo7tZVvKbySc3oEvIHEzLW2rUkM_CtI87W20vfFe2U96lwQ3eC_ia5BFCZSaOMuXhb-N_2WiqXFqX_iHcD9ZjAS3NUnBMuXy93encTdsdVN2FnDaYkjS_eAF3SANPms7vgRwWoRbhUEBCbfUjs_ABHubzdlLqw_Uw1KTjDyMrI3l50_dfRfo9e06cl4Pb-tGr_gJvQizTvMdWQH00paQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
طائرة قاصفة شاركت بقصف ايران من طراز B52 تسقط في امريكا !!!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78943" target="_blank">📅 22:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78942">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcsIdV7cmINoIstVx7ua2L1zAdY2gOGmR29zmahxq-N7fSooG6y82wqrYLeFDTIRnV77YXjw-njhHjhRPTZxJQ9tqUhxwaVf1eiEj7lF7bzokfmSRs5DywZlVZhYVPfgGaQ-EJGJ10toe5td9QTxSku2k2TQ5BsC5lyQatuI3PKlI9UG4hoaporam965bq_mXosKZAEUb37SSroD8XUGs6E9hIbG-OQHQUbFqo1O0B4p1WFdl4sZcQE03_bTP5z8d99-sUiuMXcrfY056FKDng5zPJXmc5h5YFtVpMHXoP7zj0O0yVFlWmrmR74r7qOgIGt0pP6yeD1ABAttPOUPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78942" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78941" target="_blank">📅 22:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">إغلاق مدخل العتبة العسكرية في محافظة سامراء !</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78940" target="_blank">📅 22:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مالك تطبيق تلغرام :
تريد حكومة المملكة المتحدة حظر وسائل التواصل الاجتماعي للأطفال دون سن 16 عامًا. بموجب القانون الجديد، سيتعين على جميع مستخدمي وسائل التواصل الاجتماعي في المملكة المتحدة "إثبات" أنهم فوق سن 16 — باستخدام بطاقة هوية أو مسح للوجه أو بطاقة مصرفية. يتم اعتقال الآلاف في المملكة المتحدة بالفعل بسبب منشورات سياسية كل عام.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78939" target="_blank">📅 22:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !   السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !   ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78938" target="_blank">📅 22:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !   السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !   ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78937" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !
السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !
ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78936" target="_blank">📅 22:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aeb08e28.mp4?token=OMqG4k7ABYkQ26QSnaHOZZzherT_1cqgGI124HALD0W2JcANYXl00eQZqSSW6myicIGBoos7JTbgsNxjgyvjhqGlfjROs90UwqaqoiHcpnKyjdNk4HuojCweLIopaMHQaLK-Vg5UHjZzC0TYNd85jO3lZf_Kz7cY_KdsMWjHOIrwXk4K2k-jwHHcLjh6130LJqJ47Tr07Fx7X53ToonXG1nY26rPl11CiHmHqE8VTPZXvgxo2HxxPGruGXvq0_tXzwJYwr5HLXKMDywj8y7OMO7ZhJhuCJbRrMoG3nNsJHdLQENNoLgc_ZQK54k36Xi4mKin4WmQThOGhLMbFFmm3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aeb08e28.mp4?token=OMqG4k7ABYkQ26QSnaHOZZzherT_1cqgGI124HALD0W2JcANYXl00eQZqSSW6myicIGBoos7JTbgsNxjgyvjhqGlfjROs90UwqaqoiHcpnKyjdNk4HuojCweLIopaMHQaLK-Vg5UHjZzC0TYNd85jO3lZf_Kz7cY_KdsMWjHOIrwXk4K2k-jwHHcLjh6130LJqJ47Tr07Fx7X53ToonXG1nY26rPl11CiHmHqE8VTPZXvgxo2HxxPGruGXvq0_tXzwJYwr5HLXKMDywj8y7OMO7ZhJhuCJbRrMoG3nNsJHdLQENNoLgc_ZQK54k36Xi4mKin4WmQThOGhLMbFFmm3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
وزارة الداخلية البحرينية التابعة لعصابات آل خليفة تصدر قرار منع مشاركة بحق عدد من الرواديد الحسينيين في مراسيم العزاء بشهر محرم الحرام: الرادود عيس الغبص الرادود حسين الأسدي الرادود يوسف القصاب الرادود محمود الشهابي الرادود سيدجلال البلادي الرادود سيد حسين…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78935" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe6cd6ef1.mp4?token=Yz7kU630qZKnYVDwQlZqajB2SpGwaHjTG_DVvzFxlm_o4BItNjns58MRTcfHuTG7DN7UeHPg-fu3bgCk56_6u46Ii1nqX6cNTFQr3C4otLwZDk3iusLxFM_WED5PC4q2rEAJx_jkeECxi_b1hynSW1LGSnWVJeIMa9OKM5sQtsS2JrxgFgEnOEJ7O9bshrBEOrD-Pj5c48yv4ehX0APDbTGJk-cf_zbln9g4OmU1JiYdxHejU0EM1JDkFWj_lGDGdJA-ifQBwEPLeqj4z8-AVFGWjp43Xkx1Z26H2aKV71uujId45oe7tzXXGrcBFb6XsBB1QIAZ3BnbfuxQsqpJ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe6cd6ef1.mp4?token=Yz7kU630qZKnYVDwQlZqajB2SpGwaHjTG_DVvzFxlm_o4BItNjns58MRTcfHuTG7DN7UeHPg-fu3bgCk56_6u46Ii1nqX6cNTFQr3C4otLwZDk3iusLxFM_WED5PC4q2rEAJx_jkeECxi_b1hynSW1LGSnWVJeIMa9OKM5sQtsS2JrxgFgEnOEJ7O9bshrBEOrD-Pj5c48yv4ehX0APDbTGJk-cf_zbln9g4OmU1JiYdxHejU0EM1JDkFWj_lGDGdJA-ifQBwEPLeqj4z8-AVFGWjp43Xkx1Z26H2aKV71uujId45oe7tzXXGrcBFb6XsBB1QIAZ3BnbfuxQsqpJ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: ترامب رئيس الولايات المتحدة، أنا رئيس وزراء إسرائيل - أنا أدافع عن مصالحنا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78934" target="_blank">📅 21:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتن ياهو: لست متأكدا من تفاصيل الاتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78933" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🏴‍☠️
🇺🇸
نتن ياهو: ‏هناك خلافات بيني وبين ترامب.. العلاقة مع ترامب شراكة وليست محل تنافس أو فرض قرارات</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78932" target="_blank">📅 21:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏نتن ياهو: أنا سأنتصر في الانتخابات المقبلة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78931" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتن ياهو: لم أقل إن أحد أهداف العملية هو إسقاط النظام الإيراني. قلت إن الهدف هو "تهيئة الظروف للشعب الإيراني".  لا تحلف مصدكيك وداعة حايط المبكى
😄</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78930" target="_blank">📅 21:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏نتن ياهو: أحيانا لا أتفق مع ترامب في الرأي</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78929" target="_blank">📅 21:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
الخطوط الجوية العراقية تعلن تفعيل خدمة الصعود الإلكتروني وإختيار المقاعد قبل موعد الرحلة عن طريق التطبيق الالكتروني.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/78928" target="_blank">📅 21:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتن ياهو: هناك من يريد تقزيم الإنجازات التي حققناها</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78927" target="_blank">📅 21:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتن ياهو: دمرنا أسلحة نظام الأسد وسنظل في المناطق الأمنية مهما تطلب الأمر</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78926" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏نتن ياهو: سنبقى في المناطق العازلة في لبنان وغزة وسوريا.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78925" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتن ياهو: قتلنا نصر الله ومنعنا اجتياح الجليل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78924" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتن ياهو: الأمر لن ينته مع إيران بعد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78923" target="_blank">📅 21:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتن ياهو في محاولة لترضية الداخل الغاضب: ألحقنا ضررًا اقتصاديًّا هائلاً بإيران سيستغرقها سنوات للتعافي منه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78922" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">#ترفيهي  ‏نتنياهو: لقد حققنا الكثير وأبعدنا مع أصدقائنا الأميركيين خطر التهديد النووي لإيران.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/78921" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبية لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78920" target="_blank">📅 21:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#ترفيهي
‏
نتنياهو:
لقد حققنا الكثير وأبعدنا مع أصدقائنا الأميركيين خطر التهديد النووي لإيران.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/78919" target="_blank">📅 21:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇱🇧
حزب الله في اول بيان له اليوم:
ردا على خرق العدوّ الإسرائيليّ لوقف إطلاق النار، وبعد رصد قوّة تابعة لجيش العدوّ الإسرائيلي مؤلّفة من جرّافة ودبّابتَي ميركافا تتقدّم من حمى أرنون - الكمّاشة باتّجاه منطقة المعبر في أطراف بلدة كفرتبنيت عند الساعة 18:15 الإثنين 15-06-2026، تصدّى لها مجاهدو المقاومة الإسلاميّة بالصواريخ الموجّهة ومحلّقات أبابيل الانقضاضيّة ما أجبرها على التراجع.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78918" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
إن الشروط التي قبلت بها الولايات المتحدة في مذكرة التفاهم الخاصة بالمفاوضات مع إيران، وفي حال التزام الطرف الآخر بتعهداته، يمكن أن تُرسّخ مكانة إيران بوصفها أحد الضامنين لمستقبل لبنان في المحافل الدولية. كما أن إنهاء الحرب، وإلزام الكيان الصهيوني باحترام سيادة لبنان ووحدة أراضيه والعودة إلى الحدود الدولية، يُعدّ إنجازًا مهمًا لإيران ومحور المقاومة.
وإذا تمكنت الولايات المتحدة من إجبار إسرائيل على تنفيذ هذه الالتزامات، فسيشكّل ذلك نقطة استراتيجية بالغة الأهمية، إذ سيُضطر هذا الكيان للمرة الأولى إلى قبول قيود يفرضها عليه حليفه وداعمه الرئيسي. أما إذا رفض تنفيذ هذه الالتزامات، فقد يكون ذلك بداية شرخٍ ذي دلالة بين الركنين الأساسيين لمنظومة الهيمنة.
وكما أشار القرآن الكريم:
﴿بَأْسُهُمْ بَيْنَهُمْ شَدِيدٌ ۚ تَحْسَبُهُمْ جَمِيعًا وَقُلُوبُهُمْ شَتَّىٰ﴾
سورة الحشر، الآية 14</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78916" target="_blank">📅 21:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴‍☠️
🇺🇸
نتن ياهو:
يمكننا شد الحبل مع الأمريكيين، لكن لا يجب أن نمزقه.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78915" target="_blank">📅 21:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRdasE1e0zAD7ZweXTLNoJm-e5FoPAiah7pwh8r25T29OC2zW2OxuQtDwiK0hiUy3qGowGI6Vc1FXHYKnyU9sPNmuBAhsXGBxxr9OJWUjIPtOPeLXjMEoIZsOJqLUSAwq4s4jr8DI_t0lVzzEt_qlcgPRcAwJqMSW6B-WqX1OGRZfu6tirbUiFTcTpaIZI_5mHtyESWqKnHZIlyor54e1YjE9LQ6RnMul0o_JeNO8856KyIsHJXO3_Jb2H3zNx-duoMog2-igei3mgq2FsYx4ShOs1ez6zA5_GgzwYDFTkCphx7fVuvMW6DBcpWtu7Q3f-GZoRFI-UoKqE7bKZDvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان: ‏إن مذكرة التفاهم التي تم تطويرها هي نتيجة أشهر من الحوار والمتابعة المستمرة في هذا المجال، وإذا تم تنفيذ جميع أحكامها بشكل صحيح، فيمكن اعتبارها وثيقة فخر للبلاد. ‏أرى أنه من الضروري أن أشكر إخوتي، الدكتور قاليباف، وعراقجي،…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/78914" target="_blank">📅 21:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMZrUJv7ug6wURBJ5sNFVcYy3ev1zzQltSggh32V1h5uJXvOK68HGIz9f7cCiHgQI8frtUslE6k4U5DUGPLDNihYSdkjW0K76IUekd3TPEL-q3PO97eg-YeIxQXg_gFTxJrmrOSV8lFjx7y0JS5vNC5o9BICmaqSaudXA_CbrDFO1vrZjUWieOOiBVhyRzPv2eyaQon3_Qc2dc3j9wbbFDZIoURTPNjNbZq2b5NXGRnc3yXhgrZDQ1GB9VtWQOgEjMzSnVUk65bnG98GTE5eiF0lqIelRR0qD5SRzsylBFoibIXVy9B6tKrLI8d3WUvm2zo5x_5TUtUpCclQQdxCNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:‏ بعد مناقشات مكثفة، أيدت أغلبية أعضاء الحرس الثوري الإسلامي نص مذكرة التفاهم لاختبار مدى جدية الولايات المتحدة في احترام حقوق الشعب الإيراني على أرض الواقع. وكان لتوجيهات المرشد الأعلى الدور الأكبر في إدراج بنود تحمي المصالح…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/78913" target="_blank">📅 21:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYaWspO1_bywIy5_w35X8t1sWigTW5TRXAxX62n541QHP05Sn7bfLoyXqQo87EK9125vivgImAa2M7SbHxKVqzaEwNkfI4BE_iDtJrJoBmdgHMZm3ZEl6I9rC8lFLJ_NANJr_CbZPp9LWmjAHgSMGioer0rIR207Hnc0BP21d8SpDisgz1Jyz9enfX_9uigAOxZo7LZGlptuZO2HcBE7KMjxzpxa9UmIemOuOBmNDOgeFcWDDlbqtBP5fpC5nO9NtWVMrhrNLDqEsHjaRwPPlmtMvITU4By0iI0g668qr2nni4XSiU_wATYgZu-1CGU7pFA6467F5v2ZvBHOfqu91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:‏
بعد مناقشات مكثفة، أيدت أغلبية أعضاء الحرس الثوري الإسلامي نص مذكرة التفاهم لاختبار مدى جدية الولايات المتحدة في احترام حقوق الشعب الإيراني على أرض الواقع. وكان لتوجيهات المرشد الأعلى الدور الأكبر في إدراج بنود تحمي المصالح الوطنية الإيرانية، ونحن ممتنون لذلك.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78912" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
لدينا تاريخ من نقض الوعود، وعدم الوفاء بالالتزامات، وإلغاء الاتفاقيات، وكل هذا حاضر في أذهاننا، لذا فإننا نبني خطة التفاوض وننفذ التفاهم الذي تم التوصل إليه على أساس انعدام الثقة والتجارب السابقة. وفي الوقت نفسه، نسعى جاهدين لخلق أكبر قدر ممكن من الانفتاح الاقتصادي للبلاد في هذا المسار. من الطبيعي ألا نفوّت أي فرصة في السياسة الخارجية، لكننا في الوقت نفسه لا نعتبر أي فرصة أمراً مفروغاً منه.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/78911" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
