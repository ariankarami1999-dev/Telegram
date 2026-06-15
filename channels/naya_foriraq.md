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
<img src="https://cdn4.telesco.pe/file/Nxc5PnsBH-3as0en9R9lWgoNNF4q3ygeTCzYcMOCZ3BDboQVCMVW61nn9gEqrzHj-DgNIyswWW2A4MAKRtYItMU8TmmNzC-UJggTC-vDTSHUBo4Bm1Y3pDjn8T0gSucoNDet4-Bgalvx2fAK3lcqCWeHbYEDVB06aRVP45HTFRw03tXJi_IHWKCFWOGQ3UlDda3aznGdbzsZAJ03J7GpwnP7JDNNf4lJ3d7wVIhyq5fmNeMYaPxwwv7x3XzJnDKlm8W6eNDK2_7AA2lFGQP05CBkl1PVUSEI9GifmL8xz_52eFYB-OnDQpi4cbnHEMZfHrPDCShj4oM9JAW41bjl-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !   السيد مقتدى الصدر اعزه الله دعى لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !   ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/naya_foriraq/78938" target="_blank">📅 22:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !   السيد مقتدى الصدر اعزه الله دعى لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !   ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/naya_foriraq/78937" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !
السيد مقتدى الصدر اعزه الله دعى لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !
ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/naya_foriraq/78936" target="_blank">📅 22:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aeb08e28.mp4?token=OMqG4k7ABYkQ26QSnaHOZZzherT_1cqgGI124HALD0W2JcANYXl00eQZqSSW6myicIGBoos7JTbgsNxjgyvjhqGlfjROs90UwqaqoiHcpnKyjdNk4HuojCweLIopaMHQaLK-Vg5UHjZzC0TYNd85jO3lZf_Kz7cY_KdsMWjHOIrwXk4K2k-jwHHcLjh6130LJqJ47Tr07Fx7X53ToonXG1nY26rPl11CiHmHqE8VTPZXvgxo2HxxPGruGXvq0_tXzwJYwr5HLXKMDywj8y7OMO7ZhJhuCJbRrMoG3nNsJHdLQENNoLgc_ZQK54k36Xi4mKin4WmQThOGhLMbFFmm3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aeb08e28.mp4?token=OMqG4k7ABYkQ26QSnaHOZZzherT_1cqgGI124HALD0W2JcANYXl00eQZqSSW6myicIGBoos7JTbgsNxjgyvjhqGlfjROs90UwqaqoiHcpnKyjdNk4HuojCweLIopaMHQaLK-Vg5UHjZzC0TYNd85jO3lZf_Kz7cY_KdsMWjHOIrwXk4K2k-jwHHcLjh6130LJqJ47Tr07Fx7X53ToonXG1nY26rPl11CiHmHqE8VTPZXvgxo2HxxPGruGXvq0_tXzwJYwr5HLXKMDywj8y7OMO7ZhJhuCJbRrMoG3nNsJHdLQENNoLgc_ZQK54k36Xi4mKin4WmQThOGhLMbFFmm3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
وزارة الداخلية البحرينية التابعة لعصابات آل خليفة تصدر قرار منع مشاركة بحق عدد من الرواديد الحسينيين في مراسيم العزاء بشهر محرم الحرام: الرادود عيس الغبص الرادود حسين الأسدي الرادود يوسف القصاب الرادود محمود الشهابي الرادود سيدجلال البلادي الرادود سيد حسين…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/naya_foriraq/78935" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe6cd6ef1.mp4?token=Yz7kU630qZKnYVDwQlZqajB2SpGwaHjTG_DVvzFxlm_o4BItNjns58MRTcfHuTG7DN7UeHPg-fu3bgCk56_6u46Ii1nqX6cNTFQr3C4otLwZDk3iusLxFM_WED5PC4q2rEAJx_jkeECxi_b1hynSW1LGSnWVJeIMa9OKM5sQtsS2JrxgFgEnOEJ7O9bshrBEOrD-Pj5c48yv4ehX0APDbTGJk-cf_zbln9g4OmU1JiYdxHejU0EM1JDkFWj_lGDGdJA-ifQBwEPLeqj4z8-AVFGWjp43Xkx1Z26H2aKV71uujId45oe7tzXXGrcBFb6XsBB1QIAZ3BnbfuxQsqpJ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe6cd6ef1.mp4?token=Yz7kU630qZKnYVDwQlZqajB2SpGwaHjTG_DVvzFxlm_o4BItNjns58MRTcfHuTG7DN7UeHPg-fu3bgCk56_6u46Ii1nqX6cNTFQr3C4otLwZDk3iusLxFM_WED5PC4q2rEAJx_jkeECxi_b1hynSW1LGSnWVJeIMa9OKM5sQtsS2JrxgFgEnOEJ7O9bshrBEOrD-Pj5c48yv4ehX0APDbTGJk-cf_zbln9g4OmU1JiYdxHejU0EM1JDkFWj_lGDGdJA-ifQBwEPLeqj4z8-AVFGWjp43Xkx1Z26H2aKV71uujId45oe7tzXXGrcBFb6XsBB1QIAZ3BnbfuxQsqpJ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: ترامب رئيس الولايات المتحدة، أنا رئيس وزراء إسرائيل - أنا أدافع عن مصالحنا.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/78934" target="_blank">📅 21:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نتن ياهو: لست متأكدا من تفاصيل الاتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/naya_foriraq/78933" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
🇺🇸
نتن ياهو: ‏هناك خلافات بيني وبين ترامب.. العلاقة مع ترامب شراكة وليست محل تنافس أو فرض قرارات</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/78932" target="_blank">📅 21:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏نتن ياهو: أنا سأنتصر في الانتخابات المقبلة.</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/naya_foriraq/78931" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتن ياهو: لم أقل إن أحد أهداف العملية هو إسقاط النظام الإيراني. قلت إن الهدف هو "تهيئة الظروف للشعب الإيراني".  لا تحلف مصدكيك وداعة حايط المبكى
😄</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/naya_foriraq/78930" target="_blank">📅 21:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏نتن ياهو: أحيانا لا أتفق مع ترامب في الرأي</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/naya_foriraq/78929" target="_blank">📅 21:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
الخطوط الجوية العراقية تعلن تفعيل خدمة الصعود الإلكتروني وإختيار المقاعد قبل موعد الرحلة عن طريق التطبيق الالكتروني.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/naya_foriraq/78928" target="_blank">📅 21:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتن ياهو: هناك من يريد تقزيم الإنجازات التي حققناها</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/naya_foriraq/78927" target="_blank">📅 21:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتن ياهو: دمرنا أسلحة نظام الأسد وسنظل في المناطق الأمنية مهما تطلب الأمر</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/naya_foriraq/78926" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏نتن ياهو: سنبقى في المناطق العازلة في لبنان وغزة وسوريا.</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/naya_foriraq/78925" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتن ياهو: قتلنا نصر الله ومنعنا اجتياح الجليل</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/78924" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نتن ياهو: الأمر لن ينته مع إيران بعد</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/78923" target="_blank">📅 21:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتن ياهو في محاولة لترضية الداخل الغاضب: ألحقنا ضررًا اقتصاديًّا هائلاً بإيران سيستغرقها سنوات للتعافي منه</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/naya_foriraq/78922" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#ترفيهي  ‏نتنياهو: لقد حققنا الكثير وأبعدنا مع أصدقائنا الأميركيين خطر التهديد النووي لإيران.</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/naya_foriraq/78921" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبية لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/naya_foriraq/78920" target="_blank">📅 21:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#ترفيهي
‏
نتنياهو:
لقد حققنا الكثير وأبعدنا مع أصدقائنا الأميركيين خطر التهديد النووي لإيران.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/78919" target="_blank">📅 21:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇱🇧
حزب الله في اول بيان له اليوم:
ردا على خرق العدوّ الإسرائيليّ لوقف إطلاق النار، وبعد رصد قوّة تابعة لجيش العدوّ الإسرائيلي مؤلّفة من جرّافة ودبّابتَي ميركافا تتقدّم من حمى أرنون - الكمّاشة باتّجاه منطقة المعبر في أطراف بلدة كفرتبنيت عند الساعة 18:15 الإثنين 15-06-2026، تصدّى لها مجاهدو المقاومة الإسلاميّة بالصواريخ الموجّهة ومحلّقات أبابيل الانقضاضيّة ما أجبرها على التراجع.</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/naya_foriraq/78918" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
إن الشروط التي قبلت بها الولايات المتحدة في مذكرة التفاهم الخاصة بالمفاوضات مع إيران، وفي حال التزام الطرف الآخر بتعهداته، يمكن أن تُرسّخ مكانة إيران بوصفها أحد الضامنين لمستقبل لبنان في المحافل الدولية. كما أن إنهاء الحرب، وإلزام الكيان الصهيوني باحترام سيادة لبنان ووحدة أراضيه والعودة إلى الحدود الدولية، يُعدّ إنجازًا مهمًا لإيران ومحور المقاومة.
وإذا تمكنت الولايات المتحدة من إجبار إسرائيل على تنفيذ هذه الالتزامات، فسيشكّل ذلك نقطة استراتيجية بالغة الأهمية، إذ سيُضطر هذا الكيان للمرة الأولى إلى قبول قيود يفرضها عليه حليفه وداعمه الرئيسي. أما إذا رفض تنفيذ هذه الالتزامات، فقد يكون ذلك بداية شرخٍ ذي دلالة بين الركنين الأساسيين لمنظومة الهيمنة.
وكما أشار القرآن الكريم:
﴿بَأْسُهُمْ بَيْنَهُمْ شَدِيدٌ ۚ تَحْسَبُهُمْ جَمِيعًا وَقُلُوبُهُمْ شَتَّىٰ﴾
سورة الحشر، الآية 14</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/naya_foriraq/78916" target="_blank">📅 21:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴‍☠️
🇺🇸
نتن ياهو:
يمكننا شد الحبل مع الأمريكيين، لكن لا يجب أن نمزقه.</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/naya_foriraq/78915" target="_blank">📅 21:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8wzFKkPU00w6B0-mOkiImOC8YgiieYQvp6DT41YQVcKo_W1Sntgi8X44zrkAH4yszTOocrCGj72Wj2wGykxrkbz7DZzTNLKQ9JhHAy6kum1JPVLhTBikL2nLQd9YfFKH9JEG7i7Ajn_bT-KkAAa3PcVGntTUlNxsj-AWNDl82aRKMdBFyQ-e48L_1EqVRoWs6Sx-Wy88qvgNQySl7EadQfHKKoRUUylW55MD_F70q_JI0HeRfafgMNGyLgBhWl1uk4KzLXqucMSHsLNQAXSipD3xBGSw2ZfBeR2loz5BY1EDTgsAo-Zf0hiYS52YOYQzO70ovemz3SioV14myikZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان: ‏إن مذكرة التفاهم التي تم تطويرها هي نتيجة أشهر من الحوار والمتابعة المستمرة في هذا المجال، وإذا تم تنفيذ جميع أحكامها بشكل صحيح، فيمكن اعتبارها وثيقة فخر للبلاد. ‏أرى أنه من الضروري أن أشكر إخوتي، الدكتور قاليباف، وعراقجي،…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/78914" target="_blank">📅 21:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofWnvbEmeCYj50pbN_rltgX2tcwpl9-5hohvGTAzXBCWqOXkhHvYBJePgXQPY12nNLc2t6mVw4XbIdCbsZKmbpV1e9B8DRrQKL4Z0BJ5Eh395FVVzeJaC304C7oqKHknPJNKdWPQh2jP44Tp-pLY8vPlGa50lT6UzrDjARvAYFx3mrW9-OdKx3IdopcnRkbVVFxjkwY24aHabvXEqnto3l8NGhEFvAyHu4cHJWgaaOFjeRkt7HSR8wUNDSuGI_jrG-UVtY3MzFZYH28mAl_DOKBTVsopiWqwJb7UAT6xZefygQmwLzoc3fFDGuWj9HHDzoYKe8iRJlWQfcqv4cZXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:‏ بعد مناقشات مكثفة، أيدت أغلبية أعضاء الحرس الثوري الإسلامي نص مذكرة التفاهم لاختبار مدى جدية الولايات المتحدة في احترام حقوق الشعب الإيراني على أرض الواقع. وكان لتوجيهات المرشد الأعلى الدور الأكبر في إدراج بنود تحمي المصالح…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/naya_foriraq/78913" target="_blank">📅 21:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBWS9Jzpz4QfWPF2TRzx8S_KD4hB7xMQPdWvKod5pH6mtO7XDeN0tfv_Rj7LbMXK155sNjd97C10n-WNLpzyqadH5bFecnprttvaMzHXNVojYo3_fS_gSLvYyVQUmXEybO8lYdm8Su-zIMx_PQ8nzoIZumcFRdK28zZl7dGtWGj70RCtPfTASGWGbQ0s0L25L73impVDKV1FwAiy1SGAslu7ZrUkCHWIvfFSTofc5aaC1-kzh9Tbwnpr9ZqmdPgNHiuXXaua1jB96mwbdcxgTNX_XLKajP2BM4_Nn1Kim_lnHUyU8fuxe_cTX1X2DVCxiGSkm_nceQjEU4WRyVmP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:‏
بعد مناقشات مكثفة، أيدت أغلبية أعضاء الحرس الثوري الإسلامي نص مذكرة التفاهم لاختبار مدى جدية الولايات المتحدة في احترام حقوق الشعب الإيراني على أرض الواقع. وكان لتوجيهات المرشد الأعلى الدور الأكبر في إدراج بنود تحمي المصالح الوطنية الإيرانية، ونحن ممتنون لذلك.</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/78912" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
لدينا تاريخ من نقض الوعود، وعدم الوفاء بالالتزامات، وإلغاء الاتفاقيات، وكل هذا حاضر في أذهاننا، لذا فإننا نبني خطة التفاوض وننفذ التفاهم الذي تم التوصل إليه على أساس انعدام الثقة والتجارب السابقة. وفي الوقت نفسه، نسعى جاهدين لخلق أكبر قدر ممكن من الانفتاح الاقتصادي للبلاد في هذا المسار. من الطبيعي ألا نفوّت أي فرصة في السياسة الخارجية، لكننا في الوقت نفسه لا نعتبر أي فرصة أمراً مفروغاً منه.</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/78911" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏴‍☠️
🇺🇸
بن غفير يلغي زيارته إلى الولايات المتحدة بعد مماطلة السفارة الأميركية في منحه تأشيرة.</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/naya_foriraq/78910" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PptYk_xOM6E5cwZAgb_yHWmF07xuWrqaCjhGgEFmKMbmNezgxJZky3wgdZisBq7RW8cjI7hHB8J2eYeyzbvi9db1LV7Vj3-o9ERT6NQa8j8bute7jtN8Hkb8m_q2H21m1bmm16dU2Tu63WHVUVikRbK1LbgMte-zxTkej4svNwl9KbgDApo3_crT9CmqFgJL6WdU5qC8YT2R6fsyfZIuxopSTj0LXwXJWpxFwkmT22tpVXsMFgoz8Y3vddijiSPk5Q01iARx1n6X6_bIZzFFUCBwlXTP3vB6VmRWvOAsiXPkMVeDkmzjeX6H0YOo5dG1Nm5BbWLR7FxkgXruzH52qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفع الرايات العاشورائية في مدينة النبطية جنوبي لبنان تزامنا مع عودة اهل الجنوب</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/78909" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعلام العدو:
محادثة متوترة بين نتنياهو ونائب الرئيس الأميركي حول لبنان، فانس طلب من نتنياهو انسحابا تدريجيا من لبنان.</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/naya_foriraq/78908" target="_blank">📅 20:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 ناقلة جند تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبية لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/78907" target="_blank">📅 20:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
- الجيش الإسرائيلي سيقلص نشاطه بمنطقة الخط الأصفر في لبنان
- المؤسسة الأمنية وجهت رسالة إلى المستوى السياسي بانه من الصواب التوصل إلى اتفاق الآن مع الحكومة اللبنانية</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/naya_foriraq/78906" target="_blank">📅 20:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اعلام امريكي:
احتياطي النفط الأمريكي يصل إلى أدنى مستوى له منذ 43 عامًا.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/78905" target="_blank">📅 20:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🛐
مكتبُ السيد السيستاني يعلن أن يوم غدٍ الثلاثاء هو المكمّل لشهر ذي الحجة ويوم الأربعاء هو الأول من شهر المحرم الحرام لعام 1448 للهجرة</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/78904" target="_blank">📅 20:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a751e7c4.mp4?token=S0faOBaqM8kDvIuH4Kief-vhqwguECqIuqEvqsZGPuyBCzMx8AlvgJQ1JSkylkjpqC5fA_qNtSHhPOJUnWsBErvP2O1jYgUm1YlI9qsPi2qkL4KijBqyBKig7XjVf5oXaOYziSbg3811OTigOwwJMZ0BcFz4WMofElz5nV3PGqw4YYkAbpw_otiIVJ7SniyTNPIv1s1AsFh4LiZhEN5RHGg0cxLUt7eZkoMW4x_hyxS-qTb4U3OKV4qCvq_D0f5fyY6h1-WNb27rEM6l2XwPXY-tZQeibVzSLP_Y6BPfkl_tPM-pwzT4MlmrkaV6Od7-s24A2tW9bud4eM6A6IirhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a751e7c4.mp4?token=S0faOBaqM8kDvIuH4Kief-vhqwguECqIuqEvqsZGPuyBCzMx8AlvgJQ1JSkylkjpqC5fA_qNtSHhPOJUnWsBErvP2O1jYgUm1YlI9qsPi2qkL4KijBqyBKig7XjVf5oXaOYziSbg3811OTigOwwJMZ0BcFz4WMofElz5nV3PGqw4YYkAbpw_otiIVJ7SniyTNPIv1s1AsFh4LiZhEN5RHGg0cxLUt7eZkoMW4x_hyxS-qTb4U3OKV4qCvq_D0f5fyY6h1-WNb27rEM6l2XwPXY-tZQeibVzSLP_Y6BPfkl_tPM-pwzT4MlmrkaV6Od7-s24A2tW9bud4eM6A6IirhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
الرئيس التركي اردوغان:
لم تتحقق خطط تحريض الأخ على أخيه هدفها. ‏لقد فشلت محاولات إشعال نيران جديدة من الخلاف بين الأتراك والعرب والأكراد والفرس. ‏بالطبع، لن ننسى أبداً الدمار المروع الذي حلّ بمنطقتنا، ومأساة الأطفال الأبرياء الذين قُتلوا في ساحات مدارسهم، والاستهتار الصارخ بالقانون الدولي. ‏لكننا نعتقد أن هذه الحرب العبثية، التي أودت بحياة آلاف المدنيين، بمن فيهم أطفال أبرياء، قد وصلت الآن إلى نهايتها.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/78903" target="_blank">📅 20:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏المراسل: هل ستحاول حضور حفل التوقيع يوم الجمعة؟  ‏ترامب: حسناً، الأمر يعتمد. جيه دي سيتولى الأمر - كان من المفترض أن يتولى هو ذلك في الأصل. ربما سأكون قد رحلت بحلول ذلك الوقت. ‏سنبقى حتى وقت متأخر، لذا قد أشارك، وقد لا أشارك.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/78902" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b513c34ac.mp4?token=DvtjaDvV3OTBBY8xYl9uSeoyI7CACY5XuGS4Y_RymRgMX-mbRrR6lyJcWww_rLx0zF3x4sZ-xIg11Py1EDUBgBVuGD2OhpGyQeFALL5ScoWbkRKvMPmoxXJKVbAXTDW-75deJOYLLgHTqcf13PaYtsiCUOfWrC2AzC80KRmKtApJytHJ_fjFW8ZD7B265wnGSv11Bl4K3-WvB9Ojq6954yS_8FQymHxfgVM13yOhhRvcixto-qR5dFmfeZVRQSRnJxL5-kQTUMcQFtGyKJ15uVhR_Kt3eMDNUwiA8Ltmq8iMHNE8TdgL633irsrOclBU5tIq1oSRo8PYnh6lS1jt706lExUnpbTK6Y6AF9kp7_jQbCsGr-HBshLj9zv6JR_aJ4KD8qgaEOhEJFOPen9H2-QCEi0UGGLtcaAXtCP5E7sgHOfcyRZiZURkE5M0XAZzyMkjIeWcKqXRHnxKt0MS5jC9gQVe0rCWgw3mK04IegLUB9XWQt0EFa6Sv9Ei9iBE0fSEgRJ0B6V6Bly3Trn6Hllr4ANwH4MJd3YwX21Q0-dPSb-jP3TPVTKivVrdvXgimyb8GBChzfWMjg-P8wyOmTwngZy2jdvT0zWJR_ZgkpK7Y99tcpYhgM2I5-F5T0r6Okzo23IgA3jqFf5Szql5iQyWdj_WtbFe_SPHKyGLh00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b513c34ac.mp4?token=DvtjaDvV3OTBBY8xYl9uSeoyI7CACY5XuGS4Y_RymRgMX-mbRrR6lyJcWww_rLx0zF3x4sZ-xIg11Py1EDUBgBVuGD2OhpGyQeFALL5ScoWbkRKvMPmoxXJKVbAXTDW-75deJOYLLgHTqcf13PaYtsiCUOfWrC2AzC80KRmKtApJytHJ_fjFW8ZD7B265wnGSv11Bl4K3-WvB9Ojq6954yS_8FQymHxfgVM13yOhhRvcixto-qR5dFmfeZVRQSRnJxL5-kQTUMcQFtGyKJ15uVhR_Kt3eMDNUwiA8Ltmq8iMHNE8TdgL633irsrOclBU5tIq1oSRo8PYnh6lS1jt706lExUnpbTK6Y6AF9kp7_jQbCsGr-HBshLj9zv6JR_aJ4KD8qgaEOhEJFOPen9H2-QCEi0UGGLtcaAXtCP5E7sgHOfcyRZiZURkE5M0XAZzyMkjIeWcKqXRHnxKt0MS5jC9gQVe0rCWgw3mK04IegLUB9XWQt0EFa6Sv9Ei9iBE0fSEgRJ0B6V6Bly3Trn6Hllr4ANwH4MJd3YwX21Q0-dPSb-jP3TPVTKivVrdvXgimyb8GBChzfWMjg-P8wyOmTwngZy2jdvT0zWJR_ZgkpK7Y99tcpYhgM2I5-F5T0r6Okzo23IgA3jqFf5Szql5iQyWdj_WtbFe_SPHKyGLh00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ‏رفع العقوبات عن إيران يرتبط بسلوكها</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/78901" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 29-05-2026 جندي من جيش العدو الإسرائيلي في موقع مسغاف عام شماليّ فلسطين المحتلّة بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/78900" target="_blank">📅 19:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395c3841b8.mp4?token=vRoARWXpAdSYc3F_BhwyRLp1QSO7V4r9S78q3WnZIams6AETVjlO7dM8iUizWadwY436CqjrGAetx2zMPe_CDtDluSUGWcrNB28IQI5grZ1EQSdzQQlKTeWJ7yrqeDWq5U6QQ-MdC4x_iqOGJsvA1dvhLks6UPQBNISGQEF5eeAvFACmBo7maxLELnQAZJbTUYKjoMh13kWSyUNFIARwTfYBsaueY1qlCL1b39pBWefgNBgGWDBYBTeMIVo_Ja4bGn9bq1gb2Ndu2qFwZu2cuIE0J6ph5_SYBumTABR3izhDPZTmKBSBm47ZxfTGgSOBGxbMCN7XUd_9T3Cuf-WR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395c3841b8.mp4?token=vRoARWXpAdSYc3F_BhwyRLp1QSO7V4r9S78q3WnZIams6AETVjlO7dM8iUizWadwY436CqjrGAetx2zMPe_CDtDluSUGWcrNB28IQI5grZ1EQSdzQQlKTeWJ7yrqeDWq5U6QQ-MdC4x_iqOGJsvA1dvhLks6UPQBNISGQEF5eeAvFACmBo7maxLELnQAZJbTUYKjoMh13kWSyUNFIARwTfYBsaueY1qlCL1b39pBWefgNBgGWDBYBTeMIVo_Ja4bGn9bq1gb2Ndu2qFwZu2cuIE0J6ph5_SYBumTABR3izhDPZTmKBSBm47ZxfTGgSOBGxbMCN7XUd_9T3Cuf-WR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سننشر بنود الاتفاق قريبًا جدًا، بعد يوم الجمعة بفترة قصيرة.</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/78899" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامب: سوف يحضر جي دي فانس حفل توقيع الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/naya_foriraq/78898" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامب: أعتقد أن نص اتفاق إيران سيُعلن قريبًا جدًا.</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/78897" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامب: نريد علاقات طيبة مع إيران وإذا لم يتحقق ذلك فسنعود للحرب وآمل ألا يحدث ذلك</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/naya_foriraq/78896" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامب: سيتم فتح مضيق هرمز بشكل كامل يوم الجمعة</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/78895" target="_blank">📅 19:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامب: وقعنا مذكرة التفاهم مع إيران وتم فتح مضيق هرمز جزئيا</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/78894" target="_blank">📅 19:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامب: وقعنا مذكرة التفاهم مع إيران وتم فتح مضيق هرمز جزئيا</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/78893" target="_blank">📅 19:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78892">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي لرويترز: قواتنا ستحافظ حاليا على تموضعها بالشرق الأوسط وأي خفض لها سيتم عند توقيع اتفاق نهائي.</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/naya_foriraq/78892" target="_blank">📅 19:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حزب الله يطلق رشقة صاروخية باتجاه عدد من الآليات الإسرائيلية حاولت التقدم باتجاه بلدة كفرتبنيت</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/78891" target="_blank">📅 19:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
رئيس الوزراء الباكستاني:
سنستضيف حفل توقيع الاتفاق بين ايران والولايات المتحدة في جنيف يوم الجمعة.</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/78890" target="_blank">📅 19:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏مسؤول امريكي لرويترز: مستعدون للنظر في خطوات مع إيران لم نكن لنوافق عليها في الماضي.</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/naya_foriraq/78889" target="_blank">📅 19:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حزب الله يطلق رشقة صاروخية باتجاه عدد من الآليات الإسرائيلية حاولت التقدم باتجاه بلدة كفرتبنيت</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/naya_foriraq/78888" target="_blank">📅 19:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مسؤول أمريكي رفيع المستوى: تسمح الاتفاقية بإعادة فتح مضيق هرمز على الفور ورفع الحصار الأمريكي على إيران.</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/78887" target="_blank">📅 19:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📰
مسؤول أمريكي رفيع المستوى لرويترز: وقع ترامب وفانس مذكرة التفاهم، وقام رئيس البرلمان الإيراني بالمثل.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/78886" target="_blank">📅 19:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📰
مسؤول أمريكي رفيع المستوى لرويترز:
وقع ترامب وفانس مذكرة التفاهم، وقام رئيس البرلمان الإيراني بالمثل.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/78885" target="_blank">📅 19:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78884">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE7Mm1CxDcbqD0nE8reGFE-YMiwSWisQCwi30kMy5PhuHaU7EwKBlCar-eYuKFPQ2eJs6byP980tWKj5FdA1BFl7FCIsBz4zMlb8kHGjnGYFjZxrPP1ra6ieVbA3wIserbYQuf5lNUwlyCUpbMcRWndynPNE0NnQw_bS0Euqo19Cv34dZziBOjVdy2wcR2-A4Ky4bEy4hNXK9D4pID11UVBszJkvNLaRjGAL21DqEfIuGUOxUN-JY9otcK37G7OetGRv9IT-gqYvcLLPWf_cjVLzQKPV0ONu2AKdkskAHwpY0UAOoENmJ4LWDbCwuYBPmWQPp297WZad5gpDSmU2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
كانوا ينوون قتل هذه الأمة وتدمير هذا البلد والاستسلام، خطت إيران خطوة طويلة نحو النصر النهائي. أرادوا ذلك لكنهم لم يستطيعوا. سنقف، وفي النهاية، ستنتصر إيران، بفضل الله.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78884" target="_blank">📅 19:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78883">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اعلام العدو:
وصلنا إلى وضع غير مقبول على الإطلاق أصبح فيه لإيران "حق نقض" على حرية العمل في لبنان وهذا واقع عبثي وغير مقبول.</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/78883" target="_blank">📅 19:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78882">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الجيش الإسرائيلي يعلن مقتل وإصابة 45 ضابطاً وجندياً على جبهة لبنان، خلال الـ3 أيام الماضية فقط.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/78882" target="_blank">📅 18:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78881">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مصدر أمني:
الجيش يقلص عملياته في لبنان وينتظر قرار المستوى السياسي</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/78881" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78880">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هجوم بقاذفة ار بي جي على سفينة نفط</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/78880" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78879">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حدث امني قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/78879" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78878">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حدث امني قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/78878" target="_blank">📅 18:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78877">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhs6mCWX9K1DY8ciajwbugEiYBqkibXpUZq72js8IDFOmWQsnws9_LyVqnwgiQYS9enUckGDxnxFfF9cbkNgtsic9uw1n98kFxPYZlwTzbO5L3e_NOq4OJZ7D90dgGK0JWKs89yyJ2f1QT2MKFssXcGNT_oSzK1Yew8wjmH6DOjpIJZwuU-DDG1-fY5_M8__tCI7VpNSC1CDWI1U7BXLYXAlDdNOYSKCe5Gz-GFpgehb5JtZWdWDKP9EJjTlu6tmlTTIbJTutjvcuEdE2pH-n7CFJUDRSPuT09vigqejw4UD6hv2fGtgx6FHRSTdrUgbjEV8bOn1gO4HbOMma4hg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
متابعة جوية |
أظهرت بيانات موقع Flightradar24 تحليق طائرة الاستطلاع الأمريكية MQ-4C Triton التابعة للبحرية الأمريكية (OVRLD02) في أجواء الخليج الفارسي ، وتُعد الطائرة من أبرز منصات الاستطلاع والمراقبة بعيدة المدى المستخدمة في جمع المعلومات ومراقبة التحركات البحرية والجوية علما ان الطائرة انطلقت من قاعدة موفق السلطي في مملكة البندورة المعروفة بالأردن …</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/78877" target="_blank">📅 18:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78876">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">لَن نَغِيب عَن المَيدان ...</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/78876" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78875">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
الجيش الأميركي:
حصار موانئ إيران ما زال ساريا في انتظار استكمال الاتفاق وعلى السفن المتضررة من الحصار عدم السعي للعبور.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78875" target="_blank">📅 17:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78874">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو:
حتى هذه اللحظة، بالمناسبة، لم يكلف رئيس الوزراء نتنياهو نفسه عناء التعليق على الاتفاق أو التحدث إلى مواطني "إسرائيل" في يوم مهم كهذا. لم يصدر حتى بيانًا مكتوبًا قصيرًا. مرت 17 ساعة منذ إعلان ترامب عن التوصل إلى الاتفاق.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78874" target="_blank">📅 17:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78873">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇸🇾
إشتباكات مسلحة عقبها انفجار في منطقة الإنتفاضة بمحافظة الرقة السورية ؛ وأنباء عن تفجير انتحاري لعنصر من عصابات داعsh الإرهابية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78873" target="_blank">📅 17:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78872">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭐️
دوي إنفجار في منطقة شقلاوة بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78872" target="_blank">📅 17:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78871">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭐️
دوي إنفجار في منطقة شقلاوة بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78871" target="_blank">📅 17:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78870">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7610c404c3.mp4?token=QJEMfFgVIj9FuzyFSidJ-L-_WUx2O7NGryb6tZh7I0cdFG2JyYE27sPgYFQPGFnyNRi-tZrb7YMr7wnMHYn4dct-zZmlE-tqJRIJMdyulNrQctt8WXFhPs53Stgrhl2BmbO9NX7uY2lsiP0d3F7TaYSdnTfgPsScNIx5Yv1I4RgVbSf-JboFZ16FSTGlhZzFtG_Ih7h6c1kUwyw6nfp9GL6rir3zK2OHr6C4TzGmSAGpTwgTL8lvXYJwOkOsEnMvzf0MxbHveGnIh8Oc40BpRHobc1A32viOCDp-g25kLRRnk_1oYwSSWLYhEpR6Aq7kTP1nWljWX1oaCs7PEaKSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7610c404c3.mp4?token=QJEMfFgVIj9FuzyFSidJ-L-_WUx2O7NGryb6tZh7I0cdFG2JyYE27sPgYFQPGFnyNRi-tZrb7YMr7wnMHYn4dct-zZmlE-tqJRIJMdyulNrQctt8WXFhPs53Stgrhl2BmbO9NX7uY2lsiP0d3F7TaYSdnTfgPsScNIx5Yv1I4RgVbSf-JboFZ16FSTGlhZzFtG_Ih7h6c1kUwyw6nfp9GL6rir3zK2OHr6C4TzGmSAGpTwgTL8lvXYJwOkOsEnMvzf0MxbHveGnIh8Oc40BpRHobc1A32viOCDp-g25kLRRnk_1oYwSSWLYhEpR6Aq7kTP1nWljWX1oaCs7PEaKSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
دوي انفجار يهز محافظة الرقة السورية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78870" target="_blank">📅 17:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78869">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭐️
دوي انفجار يهز محافظة الرقة السورية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/78869" target="_blank">📅 17:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78868">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a6747efc.mp4?token=B3MTCc-DQVJM0Vo3oFFSGOZnr2PZIonL1OIGQXD2FkJLoiaYuuh0qRXYAihFb-cOFd0ZvJrUkhrRHtTSpFvPoQpfoU-dmE7XQClBo8lKkxuSe33mhTXFeaKODQ7byO_YdXkBzbLa9U7IvuJGJ2_0ZgJBEXRLrp2DvUtHMIZOd7xlz4D82BMCux16eUNSSu1IJYXmf6mU8KjUQttP1eb1tDy8MLCwFS5TMY9HimIX1DXagfZ4DE_jZMhpcZO0GR5Xx8Dd-vCfEawLWKbuCqYXkUb1aQ1uEeJogfs_xpebC2LEjl9ANzYSbxL9yeh_8xoCSFLki1ddgORUxmt1ZUYFOZ2VY_yaVe1kLd2wIOay2SMd-qNHl_ym-Oz0yDmvhTiQjW5KQW35roMI4uAh11wf1s4GvK4asebTqKRGAMwaa9hIeNMo0i-zXD1IBTURxo_wXralUpoSe2ilA7HXK6T5oSJvbVkkBk-zFXYQuINPLZxjZ_c0oh-9RrUkE6GoMmGx0EhbcNXS2VQjhmysvnqt1enyg3Th06Wg71VWaELrv6rLRmG66N5k0R0YXHJ6uWoULMmu55p5ykTQ-47u83XRMpdB5eTBbNn9MN4ti2xBn67xYLsFo1c9tOA9F47o8OIrUyPXAu1F-iVnwc8XeDOMyaSBVwE0sZ0Luk6zikqcOM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a6747efc.mp4?token=B3MTCc-DQVJM0Vo3oFFSGOZnr2PZIonL1OIGQXD2FkJLoiaYuuh0qRXYAihFb-cOFd0ZvJrUkhrRHtTSpFvPoQpfoU-dmE7XQClBo8lKkxuSe33mhTXFeaKODQ7byO_YdXkBzbLa9U7IvuJGJ2_0ZgJBEXRLrp2DvUtHMIZOd7xlz4D82BMCux16eUNSSu1IJYXmf6mU8KjUQttP1eb1tDy8MLCwFS5TMY9HimIX1DXagfZ4DE_jZMhpcZO0GR5Xx8Dd-vCfEawLWKbuCqYXkUb1aQ1uEeJogfs_xpebC2LEjl9ANzYSbxL9yeh_8xoCSFLki1ddgORUxmt1ZUYFOZ2VY_yaVe1kLd2wIOay2SMd-qNHl_ym-Oz0yDmvhTiQjW5KQW35roMI4uAh11wf1s4GvK4asebTqKRGAMwaa9hIeNMo0i-zXD1IBTURxo_wXralUpoSe2ilA7HXK6T5oSJvbVkkBk-zFXYQuINPLZxjZ_c0oh-9RrUkE6GoMmGx0EhbcNXS2VQjhmysvnqt1enyg3Th06Wg71VWaELrv6rLRmG66N5k0R0YXHJ6uWoULMmu55p5ykTQ-47u83XRMpdB5eTBbNn9MN4ti2xBn67xYLsFo1c9tOA9F47o8OIrUyPXAu1F-iVnwc8XeDOMyaSBVwE0sZ0Luk6zikqcOM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😚
إعلام روسي: تحطم قاذفة روسية استراتيجية من طراز "توبوليف 22" في منطقة "إيركوتسك" .</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78868" target="_blank">📅 16:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78867">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7I9InM5BsWexT2KJL1hOl0F3qzQMeZ3IUhz4jruM4jUxPqG2vgtW454X_E5gZnTfr8wtqW8qN_yD-0S7FLa13elzH0WCrS06-4RkD_oWmmWnGqCN0W_dMBXmm7CgZPCWx90xAy9f4G4YuI9C3F_rorGL1qA5AH5ONhm1sy-s4KbYIS7uTYgemxrpBohuWRrSbvDQXfsOoFauv3DGwcth3m43Z1V2KUOt0fUe96os0eMahcQLkjOEvOAaUlU7SkZ1vq0h4i5SDGsUlKHRcsR6YemlUcoFzBzlIzkwv6__Si1Abv8tAMwryofOSfaBanmWgaU33Zwn61kEtspR_Nt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
«بدأت السفن بالتحرك، وكثير منها محمل بالنفط، خارج مضيق هرمز. وهي تسلك الطريق السريع الجنوبي، وهو آمن تماماً وخالٍ من العوائق. وهناك طرق سفر أخرى أيضاً!»</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/78867" target="_blank">📅 16:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78866">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لن يكون العراق امريكياً
و نستذكر هنا وحدة الساحات نستذكر بطولات مفارز ابو حسين الحميداوي والكعبي والولائي والغراوي و ال…. مجهول في الأرض والمعروف في السماء أبناء بني هاشم أستاذه عمايرجي ؛ هنيئا لمن وقف بمعسكر الحسين والتاريخ لن يرحم لمن خذل الحسين ووقف إما في معسكر عبيدالله او اختار الوقوف على التل والمشاهدة من بعيد ؛ والله لتغربلن والله لتمحصن ؛ رجعنا لجنوب لبنان خاوة ؛ وخسارتنا فقط دماء طاهرة على طريق الحسين مثل السيد القائد وعزيزنا تنكسيري ولاريجاني …
جميع حقوق النصر محفوظة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78866" target="_blank">📅 16:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78863">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
رداً على تصريحات الرئيس الأمريكي بشأن إزالة المواد النووية المخصبة، الخارجية الإيرانية: لقد جربوا ذلك مرة واحدة ورأوا النتائج، فهل يريدون تجربته مرة أخرى؟</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/78863" target="_blank">📅 16:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78862">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxGiMuUJZOM1wU3SbGOwlD4DnhSsRPuvmfPMK2AtLuX-9cg-AVNIBTFHRoGtBMsPEihJmxSXhFtQd0ZaDuDVmZJ9YpgaT2p8_Y3JGJyMySDoanjJF36OHnMQhrKUxM-2CQu35C1dVZ--LkzG3SpxMs2h-XAayJfO7DjS1_k7i0eKlZ40k-owrcCvxqTgkODdqhh8Dbw_vI_UqX6oFvQicxVfOoc_45qL5Lij5ukHAYNY0ZMi08o0cutww-RFsCwJElsSSd8rzHSlWMJwbuBqZJ6i-LNtUma0MYwAumKEgYgTDK6RbVxLr5jD7VLSTRjLnVut0fS8UpDf9Awe4fgOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
عصابات آل خليفة في البحرين تحكم بالسجن 10 سنوات لاثني عشر مواطن لتأييدهم الجمهورية الإسلامية الإيرانية في مواجهة العدوان الصهيوأمريكي.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78862" target="_blank">📅 16:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78861">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله:
بسم الله الرحمن الرحيم
"وَلَيَنصُرَنَّ اللَّهُ مَن يَنصُرُهُ ۗ إِنَّ اللَّهَ لَقَوِيٌّ عَزِيزٌ"
صدق الله العلي العظيم
يبارك حزب الله للجمهورية الإسلامية الإيرانية، قيادة وشعبًا، الإنجاز الكبير بالتوصل إلى مذكرة التفاهم بينها وبين الولايات المتحدة الأمريكية، والتي أفضت إلى وقف شامل لإطلاق النار على كل الجبهات ومن ضمنها لبنان. وإن هذا الإنجاز العظيم جاء ثمرةً للصمود الأسطوري والثبات الاستثنائي والتضحيات الجسام التي قدمها الشعب الإيراني العزيز وقيادته الحكيمة متمسكين بالخيارات الوطنية التي تحفظ كرامتهم وسيادتهم واستقلالهم.
وفي هذه المناسبة العظيمة، يتوجه حزب الله بالتحية والتقدير إلى سماحة قائد الثورة الإسلامية الإمام السيد مجتبى الخامنئي (دام ظله)، الذي قاد هذه المرحلة بحكمة وشجاعة وبصيرة قلّ نظيرها، وإلى رئيس الجمهورية والحكومة الإيرانية، وإلى القوات المسلحة الباسلة من حرس الثورة الإسلامية والجيش والشعب الإيراني الشقيق، معربًا عن بالغ الامتنان لمواقفهم الثابتة إلى جانب لبنان وشعبه ومقاومته، وإصرارهم على أن يكون لبنان حاضرًا في أي تفاهم يؤدي إلى وقف الحرب ويحفظ حقوقه، وتحملوا لأجل ذلك أعباء الحصار والعدوان، لتؤكد الجمهورية الإسلامية مرة جديدة أنها حقًا نِعمَ السند والحليف القوي والوفي.
كما يتوجه حزب الله بالتحية لكل الدول التي شاركت وساهمت وساعدت وواكبت جهود إزالة العقبات من أجل إنجاز هذا الاتفاق، مؤكدًا أن على لبنان أن يحسن الاستفادة من هذه المظلة الإقليمية والدولية لتحقيق سيادة لبنان وتحرير أرضه في إطار الوحدة الداخلية.
ونتوجه بالتحية الكبرى إلى أهل الشرف والعزة والإباء، إلى أهل المقاومة الأوفياء، واهلنا النازحين تحية لصبرهم وتحملهم وصمودهم، وتحية لتضحياتهم ولكل ما قدّموه في مواجهة هذا العدوان الهمجي، وقد أثبتوا بحق أنهم شعب أبي وأنهم أشرف الناس كما وصفهم سيد شهداء الأمة سماحة السيد حسن نصر الله.
والتحية إلى قيادة المقاومة ومجاهديها الأبطال البواسل، درع الوطن الحصين وسياجه المنيع، الذين بذلوا دماءهم الزكية ومهجهم الطاهرة في سبيل عزة وطنهم وكرامة أهلهم، وخاضوا ملاحم بطولية حيث رأى العدو الإسرائيلي بعض بأسهم، وأذاقوه مرّ الهزيمة.
إننا إذ نؤكد أن ما تحقّق هو مقدمة لاستكمال مسار التحرير الكامل لأرضنا، وعودة أسرانا إلى وطنهم وأهلهم، وعودة جميع الأهالي، لا سيما أهالي قرى المواجهة في الحافة الأمامية إلى قراهم وبيوتهم، وإعادة إعمار ما دمّره العدوان. ندعو أهلنا الصامدين إلى التريث، وانتظار توجيهات المعنيين بشأن العودة الآمنة إلى قراهم وبلداتهم، حرصًا على سلامتهم وتفاديّا لأي مخاطر قد تنجم عن خروقات العدو الإسرائيلي المحتملة.
إن على العدو الإسرائيلي أن يفهم أن لا عودة إلى ما قبل الثاني من آذار، وأن المقاومة التي كانت وما زالت العين الساهرة على حماية الوطن وشعبه، لن تقبل بأي عدوان يستبيح سيادة وطنها ودماء أهلها. وستبقى المقاومة متمسكة بحق لبنان المشروع والثابت في الدفاع عن أرضه وشعبه وسيادته حتى تحقيق الانسحاب الكامل وعودة الأسرى.
ومن هنا نؤكد أن هذه المرحلة تستوجب من السلطة وجميع القوى السياسية اللبنانية العودة إلى وحدة الموقف الوطني لتحقيق الأهداف التي يجمع عليها اللبنانيون والتي تكمن فيها مصلحة لبنان وحفظ سيادته وقوته ومنعته في مواجهة أطماع العدو الإسرائيلي. ومن الحكمة مراجعة كل الحسابات والمسارات التي سارت عليها السلطة، والاستفادة من هذه التجربة وما سبقها من تجارب مرّ بها وطننا لبنان، والابتعاد عن الأوهام والرهانات الخاسرة، والإقرار بأن الموقف اللبناني الموحد والاعتماد على الأصدقاء الحقيقيين هو السبيل الأمثل لصون المصالح الوطنية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78861" target="_blank">📅 15:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78860">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: إن مسألة الثأر لشهداء الشعب الإيراني مسألةٌ دائمة، ولا يمكن لأحد أن يتجاهل أو ينسى الجريمة الشنيعة التي ارتُكبت بحق هذا الشعب. لذلك، سيظل هذا مطلبًا دائمًا ومستمرًا.  لا شك أن الدبلوماسية والتوصل إلى تفاهم مع الطرف الآخر لإنهاء الحرب…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78860" target="_blank">📅 15:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78859">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: إن مسألة الثأر لشهداء الشعب الإيراني مسألةٌ دائمة، ولا يمكن لأحد أن يتجاهل أو ينسى الجريمة الشنيعة التي ارتُكبت بحق هذا الشعب. لذلك، سيظل هذا مطلبًا دائمًا ومستمرًا.  لا شك أن الدبلوماسية والتوصل إلى تفاهم مع الطرف الآخر لإنهاء الحرب…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78859" target="_blank">📅 15:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78858">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇩🇪
قائد سلاح الجو الألماني:
أن ألمانيا مستعدة "للقتال الليلة" ودفاعها عن "كل شبر" من أراضي حلف شمال الأطلسي (الناتو) إذا شنت روسيا هجومًا.
الناتو قد يضرب أهدافًا، بما في ذلك كالينينغراد وشبه جزيرة كولا والبحر الأسود، إذا اضطر للدفاع عن نفسه.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78858" target="_blank">📅 15:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78857">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: إنهاء الحرب في لبنان جزء لا يتجزأ من مذكرة التفاهم.  احترام سيادة لبنان وسلامة أراضيه جزء من الاتفاق المؤقت مع أمريكا.  سنستخدم، حيثما اقتضت الضرورة، جميع الأدوات الاستراتيجية لضمان تنفيذ التزامات الأطراف المقابلة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78857" target="_blank">📅 15:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78856">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تجدد القصف مدفعي الإسرائيلي على النبطية الفوقا في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78856" target="_blank">📅 15:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78855">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
الحصار على موانئ إيران لن يرفع إلا بعد توقيع الاتفاق يوم الجمعة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78855" target="_blank">📅 15:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-06-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78854" target="_blank">📅 15:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭐️
قصف مدفعي من قبل جيش الإحتلال الصهيوني على جبل علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78853" target="_blank">📅 14:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78852">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
🇮🇶
مستشار السفير الإيراني في بغداد:
من المتوقع حضور 600 ألف زائر عراقي للمشاركة في مراسيم تشييع جثمان القائد الشهيد.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78852" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78851">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78851" target="_blank">📅 13:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78850">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐️
عصابات آل خليفة في البحرين تحكم بالسجن 10 سنوات لاثني عشر مواطن لتأييدهم الجمهورية الإسلامية الإيرانية في مواجهة العدوان الصهيوأمريكي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78850" target="_blank">📅 13:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78849">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxNS-I-sGVoXSCs06VIZxfUkOwogJU8aMNHGiu4ja-KuZn28euT26XBDdQ4d7ikJcNvnwQizBu0j4-zbl6n-9wvwQNpMeg1hGtr-bBn9CcoNy18uTzrJzbQ3cIqvIZmdILPVndUOzjoUCaedK0yr8iNoI9Lku8MIULK0JmSG3nYYaIFSRSNQ7fyIwG4UHvzOXp_TCcVsmrEO-zUCLxQ3olq-VmXNBnOBua0S2pxdDLCoi7Mo5X0VNf_lsPU0pTjFTiDGZT5sMEZnWqVOaO1x6_kzZm7iy1LbNLnq7KuEK5Z0VhBDuSpJ08JGItgGaP1LeR4s8rj57czpfscmybYPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: مقاتلون من قوتين مختلفتين على الحدود الشمالية: توقفت كل الأنشطة، بما في ذلك دخول المنازل التي يُشتبه في كونها مخازن أسلحة، ويتم الدخول إليها بإطلاق النار. عاد الشيعة إلى القرى التي كانوا يتجنبون العودة إليها حتى الآن، وتم حظر العمل ضدهم.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78849" target="_blank">📅 13:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78848">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
🌟
الأرض لأهلها.. البدء بفتح الطرقات في بلدة زبقين بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78848" target="_blank">📅 13:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78847">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4745391d5.mp4?token=Ai7KpHUwg_bnkPjQ0wKmkOy8T8KySaq00Hctcr6Z4CJoXn1CRe3hY5z42pfuQoPdb9R7Q4tf99-RNDbJheuiy4Gk6J_SRt0vPRtGfQ4eGaIHMdP_qoV8I2FK2yPXoeb7hMdPKYaGOBGW11NVs9ix9RGJwTPld05iDGUsomDtN8WWN60fccFTOJ6Da039Pi2dmdwmSr8eyGGsTO_7WZhHUphuNrG19XjEM_cKN4H_61V7mgJwJIwFWiB3kyiMTPGuvM5agSuetN3Bmun9zTbPA-8BGEOG5cSTwv583A68rx1ok4whT-pdtOUUW9sQUDRovDeHCmP9-ISARdQ_EboLig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4745391d5.mp4?token=Ai7KpHUwg_bnkPjQ0wKmkOy8T8KySaq00Hctcr6Z4CJoXn1CRe3hY5z42pfuQoPdb9R7Q4tf99-RNDbJheuiy4Gk6J_SRt0vPRtGfQ4eGaIHMdP_qoV8I2FK2yPXoeb7hMdPKYaGOBGW11NVs9ix9RGJwTPld05iDGUsomDtN8WWN60fccFTOJ6Da039Pi2dmdwmSr8eyGGsTO_7WZhHUphuNrG19XjEM_cKN4H_61V7mgJwJIwFWiB3kyiMTPGuvM5agSuetN3Bmun9zTbPA-8BGEOG5cSTwv583A68rx1ok4whT-pdtOUUW9sQUDRovDeHCmP9-ISARdQ_EboLig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش اللبناني يغلق الطرق المؤدية إلى النبطية وإلى قضاء مرجعيون ويمنع سكان المناطق من الدخول إليها بسبب تمركز الاحتلال الإسرائيلي.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78847" target="_blank">📅 13:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78846">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6_fb_fMmzG6iakoouYDxEV7onXrnrS2QUI3AnDqEL7SLp7Qe2ZaGCU1PUQL29r4qeMGDa09OHhGKuIaRKfFzSE_II21_o-UWu8tU1FNWRHMt194_5f09UFteFg7z8beCl_A9d43g7L80ER1z8UWG6af7bYgeR8AMnDvUQ3vtuDqOujVa5tvMydLHdhZxso9toBTI3rTd_cqvs2J1AR_KGgQqkehr6db6MHsQ43WaW14hgwXwkBWDv9_M6UvxAbDW3Jgdq8C0slmNKsJ8vvDOiZc8qj4_FhO0ol9hig3cm7Yf306MfW6TcDKBzE0GkqnA7gbNRz-vml5_gwVCvcc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون حمايات ولا درع وعبر المطار المدني..
توم باراك يصل بغداد:
يسعدني ويشرفني العودة إلى بغداد، للقاء فريق السفارة الأمريكية المتميز بقيادة القائم بالأعمال جوشوا هاريس. سألتقي اليوم برئيس الوزراء الزيدي لأبلغه دعم الرئيس ترامب لحكومته، ولمناقشة شراكتنا في مسار جديد نحو علاقة أمريكية عراقية قوية ومثمرة للطرفين.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78846" target="_blank">📅 13:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78845">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZewQr_gY6zpmcF7onkq5L5QXu6tuQSJvcOsXI21wx5Q3iXPtWhco4pcvUYuKmYG1lxDiY1NKxujGwkd_zQxegcGHtHn10BzZppj0FO0K-Dk2bAFWvclkjwRl6kOkxoVUH9g1ItQFgjQl6eF560VWVl7rDAu5JvDQ5fxRGzmLeJeFjULy2BQ_rFcBb0-oiFwJqUqneYLzl36J5S20xpyI5MEWuni96UpL1u0LCYqDAtqdbcONI1rpiFBGOCj_mEL75HAgPSE68HyrV4SL2wMHur1YoJxmoKe7Vod1xbROodps283IZ1tgVPyt3NEPJJ6ProL-GBc9gfgM6yUc9niGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا يمكن المرور على موسى الدقدوق او نعيه كمقاتل او قيادي عادي او ذكر جيفارا او اي مقاتل اممي آخر دون تذكار فارس العبوات الارتجالية ومهندس المجاميع الخاصة و كاسر هيبة الجيش البريطاني بالبصرة وتلميذ عماد مغنية وفيلسوف نظام حرب الشوارع بأزقة شوارع الداخل والگيارة…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78845" target="_blank">📅 13:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78844">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCODU0t9k1jBY0rxHMQ_Qo_Ef-KfUJQAPl5nrxfOcCuqsIIaURhcVD4sElB1S-fgjb5j1uB-WQMBfAb8Eifl21V5ARLyBdWpZrs53mb9DpTYZQYb51MVP8npCbvsEv5yM07PUF3FzDab2HbM8zGVFkItKlJ0dMJgLQ0kT5oBnwE49nRJGCcv0sSj4ZVM3L6foer1-d8WzhHtw50r30SNgxFfMIqr9Hc62b3S4fpOfOvqzsSO8PnvHugsp6pSji1Z0b7dpiFAFE_3Zg5_gspu8U6vaj0Dp-yJfEUuF4NJhTPvGdPu50bikRBuoAvkHx2jd1QLNOkxcSSNTEhgTP8cZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
قصف مدفعي من قبل جيش الإحتلال الصهيوني على جبل علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78844" target="_blank">📅 12:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78843">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8hhAiSDrOVOqSf7Qk8cwdiqppiy1vMwE-j47OyW_PWTkuraD62gx_5tfVKX0VJOF14DWMLSn7h-QX75VABv3ffLKUo2Z9G4bt_C96mhW0JpucDOA6GEPQw1NOMlzsv4AV4bDDyEJ4BFpRiFJJjEKcca9T_-JJLCxNhB1Dl5A9MLFPecN2KGByCfWJ1aWx3sfW_bK9gVdQyBwVFDtHfTggBGEXYzOJvRpeKh-A-hu7f290U6kgvZn9mDLIt3wyOEQicHqyTf3EYpkp7nuq2JNxYb4TDK1k8gIXQkkAMoaAK46yzzbsYWyI2uAJk6gAgvrRtaEAOtMBmNXyElilu_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
العراق لاول مرة
مبادرة تدخل حيز التنفيذ الان من وزارة الاتصالات العراقية برفع سرعة النت بمعدل ٢٠ بالمئة على ان تبقى نفسى الأسعار بالقيمة السوقية  …
برأيك هل سيحقق سند الوزير الإنجاز كما حققه كنائب سابق في البرلمان ؟!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78843" target="_blank">📅 12:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78842">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lClc1YopieTpvkTLKisXSFDEcPWAGRYLpjDmV7YzlbJqdfMisVkzg3t4_fYFG544mGW_QT1-jAQEmOtSQ6GkyVl11ymhHoE3C9ZXtftu1jYoBrKE-YxTHwiEAr_Vm515Cp78UWw52TW4WlykI3ScINB_tNkfBs0KjBIlxzicUhktXQrX-QIORqF4d_lRr415c3rh1L9JzzewhZ_voqfSGghJmkmnYKPSnITkIzaZC37Ro9Oc7xveTBl65iCPlAULad4W7kWzcJ6tR8f1w3gJF9-xzoECbfwytAXu5IZQg5uxpW6y8n980vQMMQHWGR1IUeSYDAc8W--_hrozck1_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
المؤشرات الرئيسية في بورصة تل أبيب تهبط بحوالي 1.5%، على عكس الاتجاه العالمي.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78842" target="_blank">📅 12:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78841">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1b94cb48.mp4?token=hdguw0DzBHDWrUB-hQ8QUJBRSU06nYnyDJhlAtgcFWLBtZf7jOVJApBk91pKLXlDBtLmenOgD_hC_tF5dZdq8DsJ1RjWzoRY6SMD9wB-qoxiYvnOqhc_BTWoTQ2GJ4aYUWa-B4pDgfN9LHiLoy6W9hsPy5ri2b5curYeIlwDPoD4kefuI5YdmbhkBRAPTg4EzsE13YYtwHMvjIaYjbDQbUbet42AL9rvVuA0QzxnitfhKIuuMgF29bUG8-tzI3A5pvv8c-r-R7bfN5hioXubPKeHwmrY1G-mHMqr62uDv31OKejy1dTl-ngTUaEQemKLX3m6ac8kXqzxSDAPM66e9If6jiALEcmyPZQUjaOOE_4l7nOM7-Vy3o_ds4Hc0mFs72YTfYg24Z4i014SL7F4d1Bh9L0KnK08aBrAMK0Bzmo2hAaSTfNqByUKIP9uIWWBpxu42SPlS3FHjxgX5x1esZnxiR96Z2zV7CY2G8gdXzSpaLuQ0p9i9_AdVR0hem1oH0DDyy1GZTwEIgW5wqwQsX2SROjw-MTp2tJJL8uIG1GeWNEZf9iS1u_PE33Eo596QyPBY8fBFXEwdPgYOkegU4dbZgX5pRKtK538q4khZQFFnDtx-CXSLtkJzXmL4fXolceM5wV01eEahwQ_dmZvk0lGT7y0yaixFy-X2IEEfmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1b94cb48.mp4?token=hdguw0DzBHDWrUB-hQ8QUJBRSU06nYnyDJhlAtgcFWLBtZf7jOVJApBk91pKLXlDBtLmenOgD_hC_tF5dZdq8DsJ1RjWzoRY6SMD9wB-qoxiYvnOqhc_BTWoTQ2GJ4aYUWa-B4pDgfN9LHiLoy6W9hsPy5ri2b5curYeIlwDPoD4kefuI5YdmbhkBRAPTg4EzsE13YYtwHMvjIaYjbDQbUbet42AL9rvVuA0QzxnitfhKIuuMgF29bUG8-tzI3A5pvv8c-r-R7bfN5hioXubPKeHwmrY1G-mHMqr62uDv31OKejy1dTl-ngTUaEQemKLX3m6ac8kXqzxSDAPM66e9If6jiALEcmyPZQUjaOOE_4l7nOM7-Vy3o_ds4Hc0mFs72YTfYg24Z4i014SL7F4d1Bh9L0KnK08aBrAMK0Bzmo2hAaSTfNqByUKIP9uIWWBpxu42SPlS3FHjxgX5x1esZnxiR96Z2zV7CY2G8gdXzSpaLuQ0p9i9_AdVR0hem1oH0DDyy1GZTwEIgW5wqwQsX2SROjw-MTp2tJJL8uIG1GeWNEZf9iS1u_PE33Eo596QyPBY8fBFXEwdPgYOkegU4dbZgX5pRKtK538q4khZQFFnDtx-CXSLtkJzXmL4fXolceM5wV01eEahwQ_dmZvk0lGT7y0yaixFy-X2IEEfmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية ناقلة جند تابعة لجيش العدو الإسرائيلي في بلدة عيناثا جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78841" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78840">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هجوم على سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78840" target="_blank">📅 12:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78839">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هجوم على سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78839" target="_blank">📅 12:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78838">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📈
الذهب يستمر بالارتفاع منذ إعلان الاتفاق بين إيران وامريكا حيث ارتفاع 3% منذ ساعات الصباح الأولى ليسجل 4,343 دولارا للأونصة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78838" target="_blank">📅 12:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78837">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd22030f1.mp4?token=fLZ5RT9noaWrmouSyLjrstywHco6qKPCd2nj7gBf4rKAVQLEP-tz7KxMLE5nDqizMAmkKlcTVU9nwSXxT7HCkYhc8L4PjJy7TGBMZEoQI4MmfRcJ6n2nSyUxjw5qsL65HsuaxC1mgu60PWdKmwnV5GKTC7maB_N-Epc_bxAq9NsX8eMr9LvTYbpkZooNQwf_rGpzhuU1hX56fJFT-bwNlDdt_HIwKVBDwdbwAqTMeztBH8l6YsLdOeXUof6x40YaL9RpJRCVWl0vKMMhiUaKWunUpA-QesJo6U2SOubFYrxfPT1b_DTim2To2qeb3rWy9qK10ymKXilbg33CHFUQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd22030f1.mp4?token=fLZ5RT9noaWrmouSyLjrstywHco6qKPCd2nj7gBf4rKAVQLEP-tz7KxMLE5nDqizMAmkKlcTVU9nwSXxT7HCkYhc8L4PjJy7TGBMZEoQI4MmfRcJ6n2nSyUxjw5qsL65HsuaxC1mgu60PWdKmwnV5GKTC7maB_N-Epc_bxAq9NsX8eMr9LvTYbpkZooNQwf_rGpzhuU1hX56fJFT-bwNlDdt_HIwKVBDwdbwAqTMeztBH8l6YsLdOeXUof6x40YaL9RpJRCVWl0vKMMhiUaKWunUpA-QesJo6U2SOubFYrxfPT1b_DTim2To2qeb3rWy9qK10ymKXilbg33CHFUQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يتركون خلفهم دباباتهم وآلياتهم المدمرة على جانبي الطرقات قبل انسحابهم من الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/78837" target="_blank">📅 11:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78836">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRDtR8lZ0MfD1dDmDSAXM1BKxOJt1MUodrKMld5TFe30Ov-DBFSKzsXZBFQtyXO9X1yti5LOHLUjTT7UD79MY2n9t0vFaHaZui2sZUQH1p_DpcJELhcUX6BKgvYFGmdZJhkDrYhsDfHEf0l2Lu1DmWLzk8MV8Sn-tdBrsRLuF_MSZ9YSVHwvUnT9yMR3UYAwu-ijY19uebEURvPWsYvBOa20md72um4aRi1TWsGQtnimNkwAKhwgOWSvWvqQ8z_K5h-Ll9uO3eS15razHDSqDQsK84uiWUw402DeqFk-aRl7Ioa31JU9t59eNCXRaMRaDi5Qofvn0bsJ7d7ddTqUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بعد اتفاقية إيران وامريكا خام برنت يستمر بالهبوط حيث وصل سعر البرميل الواحد إلى مايقارب 82 دولار لأول مرة منذ أكثر من 3 أشهر.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/78836" target="_blank">📅 11:07 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
