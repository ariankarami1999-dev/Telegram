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
<img src="https://cdn4.telesco.pe/file/CJ_OdKKohqS8V1etGgC3YcFRRbann5prs7RKI6J7VT1sMsbVQnPkRH9Ob__jRK_7uhVoAabhTZNnYoZBNdwf2KAxspIdj1rCFNhLGTtrDZbE8Pud_VaP4Ey33LrRNesabaCnt90OQj98dat2xLxuamhPwVYJoZOCMRoFxqkRp9JnzxxslRYY4ks-UDniIcq17gfxx6JYygvjPw-bWzToLoLjcBRYFP5Znk1DgYmB1_QDUyeGBgqBnYkwJxK2ip6Hcmvbno9zNlKNUgrZyPDAUok_xgGtymdZHThiSf8Pi9uOMTnfpIc9TWqEAO5f884NCmmuJ0RKFytGatt0OVDc7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 03:30:22</div>
<hr>

<div class="tg-post" id="msg-77256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
وكالة يونهاب
الكورية
: أعلنت كوريا الشمالية عدم التراجع نهائياً عن وضعها كدولة نووية، وتعهدت بعدم التسامح مطلقاً مع أي تهديدات.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/77256" target="_blank">📅 00:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febee0c094.mp4?token=s2oulauRgcveKB64M_nXSWhhCyp7MJulCiu5VMIzhozyMiKhFb-lR7fmzbT8hqDVOtR3CeN_wZuIEX2lAf7VURIlb4cNE8yQYA1V9cHWIQtdZptPrxgnPNiXySANo16bhAEksosF5S-BSeStKXWoP56JMZcnhqtT-_I9RfKpV09BrgKk6PNUbJaxSWlbh5lJ-Rue5tnCxBu_BYVZAvMIVgIeydSnVyeFPZn63YoLXcNf7Kzt3y9G88g5mLQyVaWnaLJI0pj-WhFgTW4UCyhu8IxFLX_4WEIM_x-4q4LbbYUxGQ9L0p70pRjK_neArqhL--wICesey1jLvvx6uIGa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febee0c094.mp4?token=s2oulauRgcveKB64M_nXSWhhCyp7MJulCiu5VMIzhozyMiKhFb-lR7fmzbT8hqDVOtR3CeN_wZuIEX2lAf7VURIlb4cNE8yQYA1V9cHWIQtdZptPrxgnPNiXySANo16bhAEksosF5S-BSeStKXWoP56JMZcnhqtT-_I9RfKpV09BrgKk6PNUbJaxSWlbh5lJ-Rue5tnCxBu_BYVZAvMIVgIeydSnVyeFPZn63YoLXcNf7Kzt3y9G88g5mLQyVaWnaLJI0pj-WhFgTW4UCyhu8IxFLX_4WEIM_x-4q4LbbYUxGQ9L0p70pRjK_neArqhL--wICesey1jLvvx6uIGa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الله يلعنكم ويلعن شرفكم".. الاعتداء على السائقين الاردنيين في سوريا وطردهم من قبل انصار الجولاني</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/77255" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رويترز
: ‏واشنطن ستتيح أصولا إيرانية لدول الخليج لدعم إعادة الإعمار وإصلاح الأضرار التي تتسببت بها إيران</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/77253" target="_blank">📅 00:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcnc0882Bp_KDXmeVqPD5aaFu8PxFKuKyv3z619_epgnwIhzp3U-vjRQDV0Ok64DYXF_tcPDWJnz0nTUpRbO7NaxJFKCpGcAa4GT6g0VDjBJVbdwRQMzIVDE-K9Ia-mdJh3RP5i4cNNGKhQQkIvtKDZfwBqn_Yl_JQc1fF09N-XYRo-nrrNdZi1QNtWwfsewn16tCEffO-lyo5IR-ldRlMvF0RPAZZ6y5zviRKgEGFr127_YyDc0VxVQTsfPhT91-XtHMCVwjEkNeavIHg64yVmVXxTMtfC0sxFw5p4H3OKKMHn254esowP48vxlAQbNqfQvwVDC6WANMCENazBrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
متداول: أختفاء تذاكر مباريات العراق في المونديال البالغة 1,408,000 مليون دولار
وثائق تكشف شراء 3150 تذكرة لمباريات العراق أمام النرويج وفرنسا والسنغال في كأس العالم، بقيمة إجمالية بلغت 1.408 مليون دولار من منحة FIFA المخصصة للمنتخبات المتأهلة.
وبحسب الوثائق، تم تسليم التذاكر إلى إحدى الشركات دون عقد رسمي، ما أثار تساؤلات بشأن مصيرها ودعوات لفتح تحقيق عاجل لكشف ملابسات القضية والجهات المستفيدة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77252" target="_blank">📅 23:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRHzNc3Ss8GQUpfD4c7XUjuIEODt__qtrIAOhAQT2OthhX0V48DF2MHemhYhWA2ybQb_l7qNYmoJv4V6X09TajZB2_4CCO4fNM-Yxjy_ByWbfszMQNC2sKwslGTlx1CQZAeQ4wB6BKFeYiLqwM52Hx-ltDtjYaU_z-jfjnW0hWaSpgT8yrTsRgT3aebq5WmN7nOo4_6m0otU1VY6PvFoey1-i2i64wWAnT4A21PsZDmd9kn18rlRBDhX07vZeipHtVf1UumNu0RsF5IBSgIwSlw964lE4KecAFWRmKSNbEiNRKaZvKDyTek5AAWx6VW0ZythdIgidMwo7UJZEK6LNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بيان لمحافظ كركوك محمد سمعان اغا من القومية التركمانية يقول فيه انه بحث مع اردوغان في اسطنبول "أوضاع التركمان وسبل دعم حقوقهم واستحقاقاتهم السياسية"!
مراقبون: هل بحث اوضاع التركمان وحقوقهم واستحقاقاتهم السياسية يكون في بغداد ام اسطنبول؟</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77251" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏴‍☠️
جنود جيش الإحتلال الذين قتلوا اليوم بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/77250" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
🌟
وزير الداخلية الباكستاني في اجتماع مع وزير الداخلية الايراني في طهران:
أنا هنا لتسليم رسالة خاصة من المشير الفريق أول عاصم منير، رئيس أركان الجيش الباكستاني ورئيس الوزراء شهباز شريف، إلى آية الله السيد مجتبى خامنئي، المرشد الأعلى للثورة الإسلامية، بشأن الوضع الراهن.
وزير الداخلية الايراني:
أُثني على الدور الفاعل الذي تقوم به باكستان، الدولة الصديقة والشقيقة، في الوساطة لتهدئة التوترات بين إيران والولايات المتحدة.
يُخصص جزء من زيارة وزير الداخلية الباكستاني لمناقشة القضايا الثنائية، بما في ذلك أمن الحدود، ومكافحة المخدرات، ومكافحة الإرهاب.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77249" target="_blank">📅 23:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdBFeu8-l_zFE2zHmJR-bkU4KkKO3JElttEHkiiYi6DX2yx5ASM9hIJofRzm_ugCrBPhyjGkgNjAeluT2WJPsa6vgnw__GGWmry6mSSeQY5r2u-z6QiU_60vm-U9ZQ2df8qSe622y7gFzSYTky0U4hraxd_vqRTsM30FxbMYfcviE01Fvh54D_haMECwGZGnGVcGL1nrel6B6cckiukeVCPO1vTBwE-C8xbFr5ZFd1vwYPm7TVAAnspgFat4NobCA2stinFdmulxNcVDsRXmemSGg1w0_zB5UlUjJ_9HAlGSbeoAXUHoWAO4h486oOLRe8m_AwyK85Pevzhg5sDfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
اكتمل العمل بالكامل! قام الوطنيون الأمريكيون العظماء، ومعظمهم من ولاية أوكلاهوما العظيمة، بالإضافة إلى دوغ بورغوم، وزير الداخلية، بتفقد السطح الأزرق الداكن المعقد للغاية، ولكنه قوي، لبركة الانعكاس، قبل غمرها في مياه نظيفة وجميلة. تم افتتاحها في الأصل عام 1922، لكنها لم تعمل بشكل صحيح أبدًا - والآن تعمل! شكرًا لك أيها الرئيس ترامب، شكرًا لوزارة الداخلية - والأفضل لم يأتِ بعد مع ممشى ترامب في نصب لنكولن التذكاري، وقوس النصر، الذي سيكون، إلى جانب قاعة رقص البيت الأبيض، عند اكتماله، أعظم مبنى في واشنطن. الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77248" target="_blank">📅 23:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137470719c.mp4?token=rc3ojUdgVF-nDD_pmxXEI6L8KL6cKXYIb7Np-xlweEJe4GlYc6_f0s-MJWX3gYagH2KtIlznmanD0dE-fkleTV2HSMqt_MBkxB8DYm3v9uIl2XJsuncwuHWbOl8oT6DS9XzZvMkR7p27a8Pm3JNs16yzHWKBeT0V7hdnjkaHIHcnxpzRYTFu1IXn1xlC8lZS-Y6fz59T2jYcUHIyyFXnDBRQ5EyfpF5vJYKt6FxR2rq0J96Ad9JntqU6dEVTJojBNHNryy-ecf7mGzMNGOUhafaP-D6JLR1JnXo3mHYnI8puYYvrJKETRDuKBP6aY7FbA8Y1swDzs03q73HFUF5Gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137470719c.mp4?token=rc3ojUdgVF-nDD_pmxXEI6L8KL6cKXYIb7Np-xlweEJe4GlYc6_f0s-MJWX3gYagH2KtIlznmanD0dE-fkleTV2HSMqt_MBkxB8DYm3v9uIl2XJsuncwuHWbOl8oT6DS9XzZvMkR7p27a8Pm3JNs16yzHWKBeT0V7hdnjkaHIHcnxpzRYTFu1IXn1xlC8lZS-Y6fz59T2jYcUHIyyFXnDBRQ5EyfpF5vJYKt6FxR2rq0J96Ad9JntqU6dEVTJojBNHNryy-ecf7mGzMNGOUhafaP-D6JLR1JnXo3mHYnI8puYYvrJKETRDuKBP6aY7FbA8Y1swDzs03q73HFUF5Gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
وزير الخارجية العراقي فؤاد حسين:
لجأنا إلى طباعة 25 تريليون دينار لمواجهة الأزمة المالية، والبلاد قد تواجه كارثة مالية إذا استمرت الحرب.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77247" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🤙
وزارة الدفاع الروسية تعلن أن دفاعاتها الجوية اعترضت 339 طائرة أوكرانية مسيّرة فوق عدة مناطق بما فيها موسكو خلال آخر 13 ساعة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77246" target="_blank">📅 22:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f2362693.mp4?token=GWHjfqqds3FciIhacFSDTsegJ-JNajzXeYfAThPJjurD3PFNDqEj_XUcf9LCygMJ_p1IKJsrC_RPg98X9_w8OhkHKToP8b2qeily9U9J6-HBspD_4GO21TGs41iP_84WOObVoYAFmwQmnv3rJqZccglL8Agif2tzPTMDqAJA55rSsLOas4GQbBe-Y3I1g8iRFQc0asylCNHQpkt_kzuKaJnsR86yIjmHy-I9dGx69MntN3HYFWmjPletp_rc51RyseMbSLqctbMbO60oG5RFOtfxWxx4aMZaXCpz-0ffopzQ0qS6D8xNbE7TTYJq99zWHajH6nhRY7GJsVX3AFEHKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f2362693.mp4?token=GWHjfqqds3FciIhacFSDTsegJ-JNajzXeYfAThPJjurD3PFNDqEj_XUcf9LCygMJ_p1IKJsrC_RPg98X9_w8OhkHKToP8b2qeily9U9J6-HBspD_4GO21TGs41iP_84WOObVoYAFmwQmnv3rJqZccglL8Agif2tzPTMDqAJA55rSsLOas4GQbBe-Y3I1g8iRFQc0asylCNHQpkt_kzuKaJnsR86yIjmHy-I9dGx69MntN3HYFWmjPletp_rc51RyseMbSLqctbMbO60oG5RFOtfxWxx4aMZaXCpz-0ffopzQ0qS6D8xNbE7TTYJq99zWHajH6nhRY7GJsVX3AFEHKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النائب الكردي السابق علي حمه صالح:
هل يمكنكم إخبار بغداد أن 50 ألف برميل شهريًا المخصصة للتكرير المحلي حولتها الاحزاب الكردية إلى تجارة وهرّبوها إلى تركيا بواسطة ناقلات تركية! يتم تكرير 40 ألف برميل نفط يوميًا في مصفى لاناز ونقل الديزل والبنزين إلى تركيا بواسطة ناقلات تركية، محققةً ربحًا شهريًا يقارب 60 مليون دولار! والباقي يكرر في مصفى كار. جزء منه يُباع بـ 750 دينارًا. والآن، رفعت الشركة سعر البنزين التجاري إلى 1075 دينارًا للتر. أين ذهبت الأموال؟ حوالي ٨٠ مليون دولار شهريًا، أي ما يعادل ١٢٠ مليار دينار لمصفاتين... يا للعجب! يُظهر هذا الفيديو مصفاة لاناز، حيث تنقل ناقلات تركية الديزل والبنزين إلى تركيا</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77245" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77244">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوي انفجارات جديدة في جزيرة خارك</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77244" target="_blank">📅 22:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77243">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsBfkijiHE7KxPq1sibweBHvTO2meAqsg4HP8Jm-l7lRau6jP5J218zJfodeKYSQfAE9VLWQ0D44iChWKgLA5DCppSSN3NPXVRLe3Kapm_t0atGoSCXpqeBGd7gAAgeMXqN4p17Ga4JgPk_EwisCK88-BPXOxEz85UoK1P3TdSCkFKvI_5p40d_rcNmqVhOh8bBq3cMj3u4fPifZxlsN8Nl_E9dC_nFCPUIw03RyKhy8_xOemukfNalIi7J3NZmTbzqvi3EJUfa6JQ4J5ykpYWMeT2xQ8Xz6phJ-kIaW0aiwcJzIdV7RAn2Fm3fouVVBlsCHFA5IY_LYCOrytAvrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: مقتل جندي من وحدة إيغوز متأثراً بجراحه التي أُصيب بها يوم الخميس في جنوب لبنان.   مقتل جندي من لواء جفعاتي يوم أمس.  إصابة 4 جنود إسرائيليين بجروح متفاوتة اليوم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77243" target="_blank">📅 21:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
وزير الداخلية الإيراني يتسلم من نظيره الباكستاني رسالة من قائد الجيش عاصم منير إلى قائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77242" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمعت في جزيرة خارك هي نتيجة تفجير ذخائر من حرب رمضان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77241" target="_blank">📅 21:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e387c11b4d.mp4?token=bNeN2B_WDuxqAWPncEyfQVk1doFsOt43jVg0WuKOoL30Wu0Ju7m95Pdxy0YzgpQgynhjQhXat_es22QONJrGW2Z9IpNp6nOD2Vd5yjSKZ9G4x_ey9WGCjBGDY8vzghuWLYOd3n1PU63rIgj-2KZd6wddE1P9g6DU0tSMnZ9eRRYdqIjwWc8_NT7gOpnXNlE-L6F3fcEdPCz6aGvq5l6YB5ks569pHaC_xZ9bjpK9g-JrOFyNL1bQw245Ql57px8InlZHGH7e69aABxMQtt22b4Krr_dH_7MeNeAqhQq0MhbKwd50WrTPyKGoz3sk_8Jm5twpPpUvfzI7Bk3AWay9SIhk8BdoJ1V1hRu_sVBvy2hCIWMRWdJNJ8dgptX5p0oXJXXmg3TrXEcup8hlhIxvNpSi1w9MeefxDsZ6L-C0uvunsfnPae-rPpNqDqrRQHmM4QpCYyX0eAsrFF0SdhmHql8MUz1OhjXr6tvagTt3gtXHMf0xMcKWpOalHQZhWFVUXHMKgL5pxvYqGwfZnoOWsKWixS9aEbnHzKIEVMWnelykWdvv0eeokh9-r9nb6UXoxBpHuSghmBUPtga3uIsS82tQ1o9PDBcrSgdwZCjQz2yrw57IyPKos6pKYqkKEJi3trmm1SGt2v-42I8CCmcmgCmkaew454DWehIP-MzKg8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e387c11b4d.mp4?token=bNeN2B_WDuxqAWPncEyfQVk1doFsOt43jVg0WuKOoL30Wu0Ju7m95Pdxy0YzgpQgynhjQhXat_es22QONJrGW2Z9IpNp6nOD2Vd5yjSKZ9G4x_ey9WGCjBGDY8vzghuWLYOd3n1PU63rIgj-2KZd6wddE1P9g6DU0tSMnZ9eRRYdqIjwWc8_NT7gOpnXNlE-L6F3fcEdPCz6aGvq5l6YB5ks569pHaC_xZ9bjpK9g-JrOFyNL1bQw245Ql57px8InlZHGH7e69aABxMQtt22b4Krr_dH_7MeNeAqhQq0MhbKwd50WrTPyKGoz3sk_8Jm5twpPpUvfzI7Bk3AWay9SIhk8BdoJ1V1hRu_sVBvy2hCIWMRWdJNJ8dgptX5p0oXJXXmg3TrXEcup8hlhIxvNpSi1w9MeefxDsZ6L-C0uvunsfnPae-rPpNqDqrRQHmM4QpCYyX0eAsrFF0SdhmHql8MUz1OhjXr6tvagTt3gtXHMf0xMcKWpOalHQZhWFVUXHMKgL5pxvYqGwfZnoOWsKWixS9aEbnHzKIEVMWnelykWdvv0eeokh9-r9nb6UXoxBpHuSghmBUPtga3uIsS82tQ1o9PDBcrSgdwZCjQz2yrw57IyPKos6pKYqkKEJi3trmm1SGt2v-42I8CCmcmgCmkaew454DWehIP-MzKg8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لن تبقى لكم دبابات.. إستهداف دبابة ميركافا تابعة لجيش الإحتلال الإسرائيلي واحراقها في بلدة يحمر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/77239" target="_blank">📅 21:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtPK7gSPxLbEYp5ApH2Ll6uR_APuhQI3eMaPnFDngvU0CaKBiY7c1pJpAExaUIVAglw728Zbamf4j1YAF1R13tDdkszOW8eG9S25FdRpKL6cxqhpauxI9dwEOxLFQKuMdwXVtZaE7JQ4Rwr4GkaHWBV8FQaK-RAl3hu4npvsBsoFl3-vsY8y19NT8NOjCOjxy9E0GL90LQFzwGOXmhUZK6IX5lJCQrMJRXS_z3WmAeL3rK9dohjX2OOn1nyDqbGck60eWl0_dFJ9ZnWs3whCFsevQR-RtDBWusNCPsaMBV1rf4jHlAryilvxb7lwUZ6aes2KSX-HNe91Gc292oxhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
مكتبة باراك حسين أوباما، في غضون 10 سنوات، عندما تنضج تمامًا!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77238" target="_blank">📅 21:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمعت في جزيرة خارك هي نتيجة تفجير ذخائر من حرب رمضان.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77237" target="_blank">📅 21:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77236">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae2fa5b33.mp4?token=kxUB5gOXipy7ZLmWv_d5QM_Gybpra2O7IGlcEFh2mMWsEIY3eN0RhrzA2RWLdp0gHG-SpEXyk47Wbs3hcBB3p8ETqli_SXIPgcsgVbcSsOeL0W3RLV8YRbT5soW-8ENa-xLPm73fhO9VYh6uJ8ekM_S-OG7zVA8PLu-tuysIYpHMGZTmlLLz-zq9QQaM8Q-7Lali5YO11ZZAtSFwYQKDXo7uYQJkFBsLhOREjioMID2UXanfXSPmQjoNikVAEP-DM5faPzjGz0dPBFiXgejTnqsAObwEG6B8YIbU445q1JE22BQfgwCB4K6unq1MrBY3clUs8-8oIzZiDhQA9Aq3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae2fa5b33.mp4?token=kxUB5gOXipy7ZLmWv_d5QM_Gybpra2O7IGlcEFh2mMWsEIY3eN0RhrzA2RWLdp0gHG-SpEXyk47Wbs3hcBB3p8ETqli_SXIPgcsgVbcSsOeL0W3RLV8YRbT5soW-8ENa-xLPm73fhO9VYh6uJ8ekM_S-OG7zVA8PLu-tuysIYpHMGZTmlLLz-zq9QQaM8Q-7Lali5YO11ZZAtSFwYQKDXo7uYQJkFBsLhOREjioMID2UXanfXSPmQjoNikVAEP-DM5faPzjGz0dPBFiXgejTnqsAObwEG6B8YIbU445q1JE22BQfgwCB4K6unq1MrBY3clUs8-8oIzZiDhQA9Aq3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لن تبقى لكم دبابات..
إستهداف دبابة ميركافا تابعة لجيش الإحتلال الإسرائيلي واحراقها في بلدة يحمر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77236" target="_blank">📅 21:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77235">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من سلسلة استهدافات المقاومة الإسلامية لجيش العدو الإسرائيلي بتاريخ 02-06-2026 عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77235" target="_blank">📅 21:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77234">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b8f677c3.mp4?token=FUznvZg_AMOEPesEaPc8FR48VhRPyqK6HeARgy1dnT2HpUuCpElDycWmAkYgAoxk7e-P5LtQPrkIwECckLk4ZnlMdT--8xoJaU7RF9JMP238bXoPf9NVghk977RPq7vEFZY4kNVpE5gav_pua07VQeE478tsRGS01UPOxRlLekpnjVUBY7-i8I20kh0XfeT4BH8-c8rGgAoWjJaPALpD-3anp4YrDmkeHhuAzd3msC_kFCCeKptheYmjyuaXnE_LKj4orqoTXZM_XgzyT_uvGLhqjotN3MsL92htB8SdYXPVU34XeRX9A6GKOn-ouLRuvfq9n3A-zwOVMkoCaSzmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b8f677c3.mp4?token=FUznvZg_AMOEPesEaPc8FR48VhRPyqK6HeARgy1dnT2HpUuCpElDycWmAkYgAoxk7e-P5LtQPrkIwECckLk4ZnlMdT--8xoJaU7RF9JMP238bXoPf9NVghk977RPq7vEFZY4kNVpE5gav_pua07VQeE478tsRGS01UPOxRlLekpnjVUBY7-i8I20kh0XfeT4BH8-c8rGgAoWjJaPALpD-3anp4YrDmkeHhuAzd3msC_kFCCeKptheYmjyuaXnE_LKj4orqoTXZM_XgzyT_uvGLhqjotN3MsL92htB8SdYXPVU34XeRX9A6GKOn-ouLRuvfq9n3A-zwOVMkoCaSzmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الطيران الأمريكي يحلق بإرتفاع منخفض في سماء محافظة الموصل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77234" target="_blank">📅 20:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77233">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
مقتل جندي من وحدة إيغوز متأثراً بجراحه التي أُصيب بها يوم الخميس في جنوب لبنان.
مقتل جندي من لواء جفعاتي يوم أمس.
إصابة 4 جنود إسرائيليين بجروح متفاوتة اليوم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77233" target="_blank">📅 20:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e712cb5fd9.mp4?token=rcZccOyX2MSyGxGI2-YoJdFOO-3BPwS8HD21NXGgDGpqN7pliWxt-YuZHQdtBJnwrlnPLky3oQEr37L0cg7FgMnn4POagXiUhUiOoa7U8aMKXMfabggE5ALtLoBJaIzDkI0TQhUIcJ_YbNTE578QFeMQ2vUB1DKR_eASU1PptpkQvrBrBnq4OZUHU08z-O3WcjpxeBWjFHrChY5tgoh3XrYsf3fB6gyKzgFVHUzHD53pXiyGwfu6LGt2xPqBtQpIoKN5oHPoRJk5i9AupUBa6bxGh4QwWJYVtdHMUi7gy1073guM73yCInM2q9_pqRWkDk9CyN7QhZuaKd1tHS6rMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e712cb5fd9.mp4?token=rcZccOyX2MSyGxGI2-YoJdFOO-3BPwS8HD21NXGgDGpqN7pliWxt-YuZHQdtBJnwrlnPLky3oQEr37L0cg7FgMnn4POagXiUhUiOoa7U8aMKXMfabggE5ALtLoBJaIzDkI0TQhUIcJ_YbNTE578QFeMQ2vUB1DKR_eASU1PptpkQvrBrBnq4OZUHU08z-O3WcjpxeBWjFHrChY5tgoh3XrYsf3fB6gyKzgFVHUzHD53pXiyGwfu6LGt2xPqBtQpIoKN5oHPoRJk5i9AupUBa6bxGh4QwWJYVtdHMUi7gy1073guM73yCInM2q9_pqRWkDk9CyN7QhZuaKd1tHS6rMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من الغارات العنيفة للطيران الحربي الصهيوني على وادي برغز بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77232" target="_blank">📅 20:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77231">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث أمني صعب تحت الرقابة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77231" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">النجباء …  اصحاب الأقدام الثقيلة
ربما يسمح بالنشر …</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77230" target="_blank">📅 19:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d433ebbbdf.mp4?token=O-W1tmAa3BuaTQSwR22oI7g7BMmZ3o42dOKfFDulS3jVONtPy7NqBBjE423stvJTiQlDkLU1n4vHsjWwOpcQLIy4FD0pbgkNbCNK5FBtjkl-1Fusy0RkqQ9RMFjGTVihrjrx9d1XonrX_-rlV2P4u8vLl5jz92Yy0DwoipYYWSAdQcH1Pn6jFe4-jtDQ4vTuq_dUE-Pg-YrK7qX3fe3YMw79CfWdnmbSLgHtn5irMmSTaMPywjAWcbGyOcIp_Bnt6oDmXc0bqkJhwQpw700R077TYwqFP1_VrMZjutzcLADhnn2J_KSrOeTwage2MyZN2CGsiAt_q0LoDvTMN5LYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d433ebbbdf.mp4?token=O-W1tmAa3BuaTQSwR22oI7g7BMmZ3o42dOKfFDulS3jVONtPy7NqBBjE423stvJTiQlDkLU1n4vHsjWwOpcQLIy4FD0pbgkNbCNK5FBtjkl-1Fusy0RkqQ9RMFjGTVihrjrx9d1XonrX_-rlV2P4u8vLl5jz92Yy0DwoipYYWSAdQcH1Pn6jFe4-jtDQ4vTuq_dUE-Pg-YrK7qX3fe3YMw79CfWdnmbSLgHtn5irMmSTaMPywjAWcbGyOcIp_Bnt6oDmXc0bqkJhwQpw700R077TYwqFP1_VrMZjutzcLADhnn2J_KSrOeTwage2MyZN2CGsiAt_q0LoDvTMN5LYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الله يلعنكم ويلعن شرفكم"..
الاعتداء على السائقين الاردنيين في سوريا وطردهم من قبل انصار الجولاني</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77229" target="_blank">📅 18:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77228">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220a777030.mp4?token=UTKS1VZKkobS241i7aT6zTfXfxVMf3pQupFilDOpB6CH6Op9cze4rGAmTaM7asqMQqcfSTGs9aB60huFINpt4JOHNiv6c-SEXPYhYThWWL4MeS_VgSfchOsOZgaCux0bNLKKJ6so9lq58VpZWk6pdYKo9PLdtqPFdLPOJfys8Q4PmBhx3oUuNy90wJKkdlqCPaEYeVVqYIyHjvM9LLQSuT2n-m9eEkkirPASY_i5RZuN43OdvcxEftC-nbMSTGfgH2NSA8GRmE06KziZtX36XWLpmx7aF-yL_HNp1qQhvuvD6ffFTOY8-qhLA9GIgRKqb97bExs4o0qWiqqXttL3uo0mTBNwnKS2jYjOlzQLomFLZZJPJR9TQJBDYWTPDDIuMKwTH7e0pmN1TYim2OWA0VTNycJikdrdcsF4ID2_ILnw1_bOX1zPlgO31CgcG3-eTF0hKWsaNz_kdQHKZX7XC_VRE7YbLjGKbULtKbU-muY8wBFekwx7cDqysDu2v4IyZvK-EqKjEryPcoHvINMjzYKcQ7x62PFYLj7KOnw1EmUeLCnxRfTDtch5zEFRp3KzxS4FyCSFLTSyUmzuKEeuW4gz_c4nt5RldedAEX670VgJmJEK3oHhKDYVtZ83BToEBkMh-NhMklZLB_7uiOCNPwTR5KB4EPi4AYtygM1cztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220a777030.mp4?token=UTKS1VZKkobS241i7aT6zTfXfxVMf3pQupFilDOpB6CH6Op9cze4rGAmTaM7asqMQqcfSTGs9aB60huFINpt4JOHNiv6c-SEXPYhYThWWL4MeS_VgSfchOsOZgaCux0bNLKKJ6so9lq58VpZWk6pdYKo9PLdtqPFdLPOJfys8Q4PmBhx3oUuNy90wJKkdlqCPaEYeVVqYIyHjvM9LLQSuT2n-m9eEkkirPASY_i5RZuN43OdvcxEftC-nbMSTGfgH2NSA8GRmE06KziZtX36XWLpmx7aF-yL_HNp1qQhvuvD6ffFTOY8-qhLA9GIgRKqb97bExs4o0qWiqqXttL3uo0mTBNwnKS2jYjOlzQLomFLZZJPJR9TQJBDYWTPDDIuMKwTH7e0pmN1TYim2OWA0VTNycJikdrdcsF4ID2_ILnw1_bOX1zPlgO31CgcG3-eTF0hKWsaNz_kdQHKZX7XC_VRE7YbLjGKbULtKbU-muY8wBFekwx7cDqysDu2v4IyZvK-EqKjEryPcoHvINMjzYKcQ7x62PFYLj7KOnw1EmUeLCnxRfTDtch5zEFRp3KzxS4FyCSFLTSyUmzuKEeuW4gz_c4nt5RldedAEX670VgJmJEK3oHhKDYVtZ83BToEBkMh-NhMklZLB_7uiOCNPwTR5KB4EPi4AYtygM1cztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
27-05-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77228" target="_blank">📅 18:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77227">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابة ميركافا تابعة لجيش الإحتلال الإسرائيلي في بلدة زوطر بجنوب لبنان بواسطة محلقة إنقضاضية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77227" target="_blank">📅 18:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏴‍☠️
🇱🇧
نيويورك تايمز":
رصد ذخائر "فوسفور أبيض" فوق مدينة النبطية خلال عملية إسرائيلية للسيطرة على "قلعة الشقيف".</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77226" target="_blank">📅 18:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKx--9YNSbaVcUjA4jZmJJaKfCRnUmqzjxe-BfVclvLM0DcXPByQLtk6MY8MOB9k1SHTkykUEz95hCr046U7oLt-5Os3R3DOlCfWWvaV6jCt1uxLQYwVXC-Lq2c2wPSBPVcd5-snAb_kW3vlAvfygvmnkDpgLQbaCibLTWoZo2WFSsNQv3viRt2vKOA0-rE8AbPI5zFI_Dx8aJZHMTGM6MqPzCY1OdwYP3T-90JNDxdlDaeWpKQmxTaCiKysFQvHO-_LcOpDetjEbD6_g60IgE4-OV16pEs2MnSgPGPUtJogs_ebqtqQXwgHltRgmayN6yfq4PSm07Au27Mee7Bjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالكاتوغرافي
أهداف في دويلة الكويت قاعدة علي السالم الأمريكية تم دكها بصواريخ الحرس الثوري بهذا الأسبوع وجاءت الصور من المواقع المستهدفة لتبين حجم دمار شامل داخل القاعدة ..</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77225" target="_blank">📅 17:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77224">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇳🇿
الرئيس التنفيذي لشركة طيران نيوزيلندا:
يجب على شركة الطيران تحديد أولويات التكاليف والأسعار وتوحيد الرحلات الجوية إذا ظلت أسعار الوقود مرتفعة، قامت شركة الطيران بتعويض 25 ٪-40 ٪ فقط من تأثير تكلفة الوقود من خلال التحوط ورفع الأسعار</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77224" target="_blank">📅 17:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏رئيس لجنة حصر السلاح في العراق: الحشد الشعبي سيتخذ قرارات بحق من يرفض تسليم السلاح</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77223" target="_blank">📅 16:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رئيس لجنة حصر السلاح في العراق: كافة التشكيلات داخل الحشد الشعبي سترتبط حصرا بقيادته وبعض الألوية قد لا تبقى بمكانها وسيتم نقلها. أي تشكيل خارج القوى العراقية الرسمية سيعتبر خارجا عن الدولة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77222" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئيس لجنة حصر السلاح في العراق:
كافة التشكيلات داخل الحشد الشعبي سترتبط حصرا بقيادته وبعض الألوية قد لا تبقى بمكانها وسيتم نقلها. أي تشكيل خارج القوى العراقية الرسمية سيعتبر خارجا عن الدولة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77221" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKIGFvO_RlAeTJObM5fhqlGfpyOm1URhh_hYFIlsVIhzphOpfBDOjUF7kggauswkJ6gZH4f6K-DKt_OW2o6LFQglcIpPnwgcZUtXtO9lF1chKeQtxmW-VkujtKz7ts8Pf5nMzGnZ3NIc_aG7WUPbVxzQmOMIvuPQkXJlZbqpfBGEjo9cT1iWmGu3TQ1NlyVLB_VItKElia9KLkql_i5BkMryx4udwrM_PPDNKFmtRexx5EL8QQaK16JpfGHEDb11HC_yhdohk2edC4wIZ3CCQCpXlgkhk8Y_a-BHI5wUuXsg9X8U3eBr4OSDEbv68HKI0M9PDyr8h23AEm9tQS3YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بيان لوزارة الخارجية للجمهورية الإسلامية الإيرانية بشأن الانتهاك المستمر لوقف إطلاق النار من قبل الولايات المتحدة
- تدين وزارة الخارجية للجمهورية الإسلامية الإيرانية بشدة الاعتداء العسكري من قبل الجيش الإرهابي الأمريكي في الساعات الأولى من صباح يوم السبت على منشآت الرادار والمراقبة الساحلية في منطقة سيريك وجزيرة قشم، والتي تكمن مهمتها في حماية أمن حدود البلاد وأمن الملاحة في الممرات المائية الدولية، باعتباره انتهاكًا واضحًا لوقف إطلاق النار واعتداءً عسكريًا على السيادة الوطنية والسلامة الإقليمية للجمهورية الإسلامية الإيرانية
- هذا الإجراء، الذي يأتي في سياق السلوك العدائي والاستفزازي المستمر من قبل النظام الأمريكي تجاه الجمهورية الإسلامية الإيرانية، يدل على تجاهل كامل من قبل السلطة الحاكمة في الولايات المتحدة للمبادئ الأساسية للقانون الدولي وميثاق الأمم المتحدة. وقد ردت القوات المسلحة القوية للجمهورية الإسلامية الإيرانية، في إطار الحق الطبيعي في الدفاع المشروع وبحذر وحزم وقوة كاملة، برد مناسب وفعال على هذا الاعتداء العدواني، ولم تسمح بتحقيق الأهداف الشريرة لمخططي هذا الاعتداء
-يثبت الانتهاك المتكرر لوقف إطلاق النار من قبل الولايات المتحدة مرة أخرى أن هذا البلد لا يملك فقط إرادة لتقليل التوتر والعودة إلى مسار الاستقرار، بل إن أفعاله المغامرة تعرض أمن المنطقة لمخاطر جدية، وتقع مسؤولية جميع الآثار والتبعات الناجمة عن هذه الأفعال غير القانونية وأي تصعيد محتمل للتوتر على عاتق الحكومة الأمريكية.
- تؤكد وزارة الخارجية للجمهورية الإسلامية الإيرانية، مع التشديد على الحق الطبيعي والمشروع للبلاد في الدفاع عن نفسها استنادًا إلى المادة 51 من ميثاق الأمم المتحدة، أن الجمهورية الإسلامية الإيرانية ستدافع بكل قوتها وباستخدام جميع إمكانياتها عن سيادتها وأمنها ومصالحها الوطنية. وعلى هذا الأساس، تدعو وزارة الخارجية الدول الإقليمية إلى احترام مبدأ حسن الجوار والالتزام بالمبدأ الأساسي في القانون الدولي القاضي بعدم السماح للأطراف المعتدية باستخدام أراضيها ومواردها لتصميم وتنفيذ أعمال عدوانية ضد الجمهورية الإسلامية الإيرانية.
- كما تطلب وزارة الخارجية من الأمين العام للأمم المتحدة ومجلس الأمن والهيئات الدولية المسؤولة الأخرى أن يتخذوا رد فعل فوري وفعال تجاه استمرار الانتهاك الواضح لوقف إطلاق النار والإجراء غير القانوني من قبل الولايات المتحدة، وأن يمنعوا تطبيع الانتهاكات المتزايدة لميثاق الأمم المتحدة والإجراءات التي تهدد السلام والأمن الإقليمي والدولي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77220" target="_blank">📅 16:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1c68742e0.mp4?token=JSXhQvAeltWeSx--TmXIqMDx36opstXz9txXpt-p2EUIH9i_vdynyQYfF3csLkP0ezEPmtNA4tWn-dM2O0GI_2daEs_ohHHXKfTV0XEGu5O4gzpFAxHK3g3z8mLC9IaF5mPhtIfgzOQrviLguCNbpEoiHn3HnaXWfp-CFzgH6yHk4-xjNgXqM-zfZ-NNb4Qv5sAGSaMmhCK0C0vunetF0dHQdVItim8ZyF0HXqsVeb9IUwJijwggLUF2xxlbAPsXYuO24Z4xUVx2JXLQ0mo1S4G-SFvWLZle5aubg6H1otj6V5crDd-Jm2tFHjOFfaTKSZYye4J4FGy4u-TpIb5mOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1c68742e0.mp4?token=JSXhQvAeltWeSx--TmXIqMDx36opstXz9txXpt-p2EUIH9i_vdynyQYfF3csLkP0ezEPmtNA4tWn-dM2O0GI_2daEs_ohHHXKfTV0XEGu5O4gzpFAxHK3g3z8mLC9IaF5mPhtIfgzOQrviLguCNbpEoiHn3HnaXWfp-CFzgH6yHk4-xjNgXqM-zfZ-NNb4Qv5sAGSaMmhCK0C0vunetF0dHQdVItim8ZyF0HXqsVeb9IUwJijwggLUF2xxlbAPsXYuO24Z4xUVx2JXLQ0mo1S4G-SFvWLZle5aubg6H1otj6V5crDd-Jm2tFHjOFfaTKSZYye4J4FGy4u-TpIb5mOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إذاعة جيش العدو:
الجيش الإسرائيلي هاجم اليوم عن طريق الخطأ مركبة تابعة للجيش اللبناني - بعد أن ظن أنها مركبة لمقاتلي حزب الله - وقتل بالخطأ ضابطين وجندي من الجيش اللبناني.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77219" target="_blank">📅 15:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
وزارة النفط العراقية تنفي إيقاف ناقلة نفط خام من قبل القوات الأمريكية قرب مضيق هرمز نتيجة دفع مبالغ لجمهورية ايران الاسلامية بالمقابل لاغراض العبور</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77218" target="_blank">📅 15:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77217">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🐦
رئيس المجلس التنفيذي لحركة النجباء الشيخ ناظم السعيدي:
لا يصح استحضار موقف المرجعية بشأن حصر السلاح بيد الدولة بمعزل عن بقية مطالبها المتعلقة بمحاربة الفساد، واعتماد الكفاءة والنزاهة، ومنع التدخلات الخارجية، وترسيخ سلطة القانون وبناء المؤسسات الوطنية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77217" target="_blank">📅 14:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جيش العدو يبرر الهجوم على الجيش اللبناني: المركبة التي رصدناها جنوب لبنان تحركت بصورة مشبوهة تجاه قواتنا وتلقينا كذلك مؤشرات أن حزب الله سيطلق النار على جنودنا من نفس المنطقة. نجري تحقيق بوجود ضابطين وجندي من الجيش اللبناني داخل المركبة</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77216" target="_blank">📅 13:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77215" target="_blank">📅 13:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77214" target="_blank">📅 13:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 28-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77213" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77212">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
‏
نائب رئيس قيادة العمليات المشتركة العراقية:
أحبطنا عدة هجمات نحو دول الخليج واعتقلنا متورطين بالهجمات على دول المنطقة وتوصلنا لخيوط مهمة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77212" target="_blank">📅 13:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جيش العدو يبرر الهجوم على الجيش اللبناني:
المركبة التي رصدناها جنوب لبنان تحركت بصورة مشبوهة تجاه قواتنا وتلقينا كذلك مؤشرات أن حزب الله سيطلق النار على جنودنا من نفس المنطقة. نجري تحقيق بوجود ضابطين وجندي من الجيش اللبناني داخل المركبة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77211" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
إعلام سعودي عن مصادر: ترمب أبلغ الوسطاء أنه لا مفاوضات أكثر من 60 يوما وأنه على إيران الرد سريعا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77210" target="_blank">📅 12:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: سقوط طائرة أمس الجمعة في منطقة كفار باروخ في مرج بن عامر بسبب غير معروف قد يكون خللاً فنياً.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77209" target="_blank">📅 12:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77208">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGET8NulWCh43kl3tl6OPchrrDSZNsVg5BRRjV5sMGHy-Sef0RgHR2MDQM6QSFzhcRxI-sOsaGKuBUwLjpqfj-Kcrt4bSfqpUN2IY-awcAw7O8yI9ettQhrZIdjreEtwR-zKv8JRqC_z-HyzbKUEsHOfvqgrLr7QvAkRe8Oz5_ZPltIxYKVEfXvWrUO_ZaxibF91iuTo2ZZAwGzyFOAe9aCU8rIJhKHnoiw7zgvxRsjuVZbAe4tz5boCwvDj5j4ie43neigVsaQI56orRnAPaorf73F8zKI7wTAyL7fbhF_-i6-NCrrEBBrv3RNGxt6Mm29-lGo5tV5QWKVxhL2a9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«أَمَّا بَعْدُ، فَإِنَّ الْجِهَادَ بَابٌ مِنْ أَبْوَابِ الْجَنَّةِ، فَتَحَهُ اللَّهُ لِخَاصَّةِ أَوْلِيَائِهِ، وَهُوَ لِبَاسُ التَّقْوَى، وَدِرْعُ اللَّهِ الْحَصِينَةُ، وَجُنَّتُهُ الْوَثِيقَةُ. فَمَنْ تَرَكَهُ رَغْبَةً عَنْهُ، أَلْبَسَهُ اللَّهُ ثَوْبَ الذُّلِّ، وَشَمَلَهُ الْبَلَاءُ، وَدُيِّثَ بِالصَّغَارِ وَالْقَمَاءَةِ، وَضُرِبَ عَلَى قَلْبِهِ بِالْأَسْدَادِ، وَأُدِيلَ الْحَقُّ مِنْهُ بِتَضِيعِ الْجِهَادِ، وَسِيمَ الْخَسْفَ، وَمُنِعَ النَّصَفَ»من خطب امير المومنين ع</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77208" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#ترفيهي
‏الرئيس اللبناني جوزيف عون يهدد اسرائيل: لن نتهاون بحماية أرضنا وشعبنا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77207" target="_blank">📅 12:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: احتلال "البوفور" (قلعة الشقيف) هذا الأسبوع استُخدم لإعلانات الغطرسة ومحاولة لإعادة تسويق المعركة العرجاء في الشمال</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77205" target="_blank">📅 11:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49f8ce9de.mp4?token=WjnQKQe0MmdDm1HVJ4pZDH1iPlCybnEouZCnEo2Q-4y7TLaSzajHDxE7ZwanQU0b2m9z2IMuqCcF3iL-6CLITlQnWj8PTBkghx6JnY5PW0Wt6RwfNIuRaHrlKjO9BycDQtirtqSB4E1LLrr22KDOhQZtEPTZpk1xIP8gIzo2spK32TFrhpi4PDVPHiKnzVlBjxEPXbYv7TH8cD6uZbjlDA4U735I4m4oSIND5iH2Nv2l7PphTKAMX-nnd8rlXlFCiN845orWeoZ6ZK8tju_9enjpHQKLemeWI12NMTRLhFDwRAtSGp5fQbyrUxGbpeZi63XBVKMG9j83p9A8mSLoyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49f8ce9de.mp4?token=WjnQKQe0MmdDm1HVJ4pZDH1iPlCybnEouZCnEo2Q-4y7TLaSzajHDxE7ZwanQU0b2m9z2IMuqCcF3iL-6CLITlQnWj8PTBkghx6JnY5PW0Wt6RwfNIuRaHrlKjO9BycDQtirtqSB4E1LLrr22KDOhQZtEPTZpk1xIP8gIzo2spK32TFrhpi4PDVPHiKnzVlBjxEPXbYv7TH8cD6uZbjlDA4U735I4m4oSIND5iH2Nv2l7PphTKAMX-nnd8rlXlFCiN845orWeoZ6ZK8tju_9enjpHQKLemeWI12NMTRLhFDwRAtSGp5fQbyrUxGbpeZi63XBVKMG9j83p9A8mSLoyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇱🇧
عدوان صهيوني غاشم استهدف منزلاً مدنياً في بلدة السكسكية جنوب لبنان وإصابة عدد كبير من الأشخاص</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77204" target="_blank">📅 11:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea91a214b0.mp4?token=mqplPwdUs-TfWAhm52tif_vkqoziR0lWI6nhYVy3WlGv-5YlDRYiJywuQZm7iCWD7uo5Xu-kRpL1hNNdjYzlnVJMb_hkJeb5DjDcJtgXYSJrKenedZo79FaxJf8a85Uql56aP3SgU7dj8i59L9PbYfSNa1_hOaErpGIk4LVXxJVA4eWgg7ai-pZb2d68kS5cYzG3Dx1RyiajgJBVoOCgsBI2aD1vDSibc-Cc7ohDnovueAbqNejJUbGjY3kWJXpJdnRjIhWqGlrFkNZ4bZ9QbmcyynXfEOUX6fBgVnMOWr6RxJBLbQ4G8gjfGgp6jiycoEmYAmzCeTWPwWQdAu-DmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea91a214b0.mp4?token=mqplPwdUs-TfWAhm52tif_vkqoziR0lWI6nhYVy3WlGv-5YlDRYiJywuQZm7iCWD7uo5Xu-kRpL1hNNdjYzlnVJMb_hkJeb5DjDcJtgXYSJrKenedZo79FaxJf8a85Uql56aP3SgU7dj8i59L9PbYfSNa1_hOaErpGIk4LVXxJVA4eWgg7ai-pZb2d68kS5cYzG3Dx1RyiajgJBVoOCgsBI2aD1vDSibc-Cc7ohDnovueAbqNejJUbGjY3kWJXpJdnRjIhWqGlrFkNZ4bZ9QbmcyynXfEOUX6fBgVnMOWr6RxJBLbQ4G8gjfGgp6jiycoEmYAmzCeTWPwWQdAu-DmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المُتحدث الرسمي بإسم كتائب سيد الشهداء الشيخ كاظم الفرطوسي
: سـلاح المخازن للمخازن، السـلاح الحر للأحرار ونحن نتحدث عن سـلاح حر  يقاوم ويدافع ويشارك ولا نتحدث عن قطع صدأت من التخزين</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/77203" target="_blank">📅 10:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77202">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
مشاهد من عملية اليوم التي نفذتها القوات الجوية التابعة للحرس الثوري الإيراني ضد قواعد أمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77202" target="_blank">📅 10:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77201">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇧🇭
الخارجية البحرينية: ندعو إيران لفتح مضيق هرمز كاملا وبلا قيود أو رسوم
ندعو إيران للكف الفوري عن الاعتداءات غير المبررة والجنوح للسلام
أوامر ثانية
😆</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77201" target="_blank">📅 10:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77200">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660122eaff.mp4?token=Tb-oGOqzlLKlgBOq60dblcwP470ERlDxxlXXqjWVXYYmm66zLTAmFOyxMeM561GQSDTxvModDVoH9wP0KHkgJeX2y1OvyB55wKYEJ1Dj3mZKiYQD7UrPaw5pfQ_fgOuUBXnBmxh-2mSEH5g6UiuM-29Hhr34XUOqV1qnKoVeLd-YmerT4o5PqXcnfDcQIj-wsGJkPhpB_fSNLf7w_fXm-YZpE1fSlf7YYyarK82yd77UnFNXS3adRcd2gbS-khM477rlHhRoZwBefhS2pM4UHB3WYH2xP8SVX0RPbNYvs4YEpJ6DeiAr9Jnqedkbe96teDv2stFHGpn9B1P2puliwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660122eaff.mp4?token=Tb-oGOqzlLKlgBOq60dblcwP470ERlDxxlXXqjWVXYYmm66zLTAmFOyxMeM561GQSDTxvModDVoH9wP0KHkgJeX2y1OvyB55wKYEJ1Dj3mZKiYQD7UrPaw5pfQ_fgOuUBXnBmxh-2mSEH5g6UiuM-29Hhr34XUOqV1qnKoVeLd-YmerT4o5PqXcnfDcQIj-wsGJkPhpB_fSNLf7w_fXm-YZpE1fSlf7YYyarK82yd77UnFNXS3adRcd2gbS-khM477rlHhRoZwBefhS2pM4UHB3WYH2xP8SVX0RPbNYvs4YEpJ6DeiAr9Jnqedkbe96teDv2stFHGpn9B1P2puliwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
قوات الاحتلال الإسرائيلي تقتحم مدينة القنيطرة السورية وتقوم بتفتيش المنازل واعتقال عدد من السوريين المدنيين.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77200" target="_blank">📅 10:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77199">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6721967c09.mp4?token=jWxTe6yVUfiv4MpPtOJbls8q9TwPhtn6aPj5n7qtCXJcLO3WDEQfNaAO1Pn1MQn09a0iJWSFDNp8pSVetUPKkVhNLiQE8-mGKsyJR3jnTQUeVHE4vtbe2lJr8pNu4KZRy3o73dEQZTsQXRhyz8Nty4WSya81yZicAr8D6tTK3--5R33h_LQnnNCuFkv91TbHaS-U81yGja4B67NrDeMgIlVUWX_zRwu-qPVrDQBoC9XEq5TKHbxdOXYYYRu8bZLr082qXexKUIISOEYsfCo1aTXYSfb7Uq2HZm5PudHKXM1Di5ZCUdzoDhnMZxfxprVZRA1S5kX3V89a8KPuz5oOkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6721967c09.mp4?token=jWxTe6yVUfiv4MpPtOJbls8q9TwPhtn6aPj5n7qtCXJcLO3WDEQfNaAO1Pn1MQn09a0iJWSFDNp8pSVetUPKkVhNLiQE8-mGKsyJR3jnTQUeVHE4vtbe2lJr8pNu4KZRy3o73dEQZTsQXRhyz8Nty4WSya81yZicAr8D6tTK3--5R33h_LQnnNCuFkv91TbHaS-U81yGja4B67NrDeMgIlVUWX_zRwu-qPVrDQBoC9XEq5TKHbxdOXYYYRu8bZLr082qXexKUIISOEYsfCo1aTXYSfb7Uq2HZm5PudHKXM1Di5ZCUdzoDhnMZxfxprVZRA1S5kX3V89a8KPuz5oOkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مقتل إرهابي من الجنسية الروسية يتبع للعصائب الحمراء اثر اشتباكات مسلحة داخلية بين عصابات الجولاني في مدينة إدلب.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77199" target="_blank">📅 10:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77198">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075fca2b78.mp4?token=uDssHspRtjV9zHDwZC2-VavnmV4ARUfe4l9RsHug0x_2DYQ-bLoBNUX0El7ep28kBHLZ-dzxnCTqhzUCJrDk0Lww_CAjlXu0CDg6y4P2b2xIKPNYWCSH-WLp8MnAIXMILGrq3Hn8jQBZUd30fdG8leFWLMM5zPwnFzIHYsOx_QYLmdaEUuO6CDyoPJf44mJ-ohM6UxsBdbCsgoUxVWQapu_YICpatWV-rp_rB5l0RLODl_B81UADXgGEUul0cFCzx4wKpEH06FlXqYEwxcubO-WUukOk9WnhZlhE8dmUPXI5rMo0IBccoMczyvRV5_nkeGNAS3i38qANmT_ZeNDq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075fca2b78.mp4?token=uDssHspRtjV9zHDwZC2-VavnmV4ARUfe4l9RsHug0x_2DYQ-bLoBNUX0El7ep28kBHLZ-dzxnCTqhzUCJrDk0Lww_CAjlXu0CDg6y4P2b2xIKPNYWCSH-WLp8MnAIXMILGrq3Hn8jQBZUd30fdG8leFWLMM5zPwnFzIHYsOx_QYLmdaEUuO6CDyoPJf44mJ-ohM6UxsBdbCsgoUxVWQapu_YICpatWV-rp_rB5l0RLODl_B81UADXgGEUul0cFCzx4wKpEH06FlXqYEwxcubO-WUukOk9WnhZlhE8dmUPXI5rMo0IBccoMczyvRV5_nkeGNAS3i38qANmT_ZeNDq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
جولة حصريه وخاصة لكادر قناة نايا   من مضيق هرمز حيث تظهر عملية سيطرة واضحة على المضيق من قبل دوريات وزوارق الحرس الثوري في ايران .</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77198" target="_blank">📅 09:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c96b58fbf.mp4?token=i_hJPCGxnPOBw_addej9DI3Cmcz8td86Pwsigrm8ycmy3a1I_cRYOAAMYMDRBcKxZ2XNJlZqVJujkV-2BkCkv7ZfDP_pTmxVRLu3gdJCvDnHMbtScyYEAcqZi3IEsQwvByytG0PGJb0WSIJV_k2b7x3ZTswaHimBT6j7DUcpXl7D9-aMPS02iNBuqSrL3XqS8-LDN1T9MLWZreSwmk-pqag2LGZ2VDof75ZPXkpULy6oqspaev5FAq881MTiEw06RxdjZbZXj3E9SjOkK16i2-hWDPVg7zKt599Jf7qp2wrO6D_VApImPacSkrxhDzy_HbAVvf0HHQD0nG96_oVnAqj8c11ESlHwm7Uv_tdMnhJroFgKIy4pNvFf2OHWIhOYqznVkMe10ftnZUWcVS0jDT3FoE9RpNRqeRdNnEHhrMCoBkXxzG2sRXAUqRsc2G5BTwdEEjBGhWhypoCNlTvoE2Fw5flray3eaOUGx4ghcZ_1uQ43vHBV76sdJYUl1xIwbdsrnjrJg_Y6q8o9I7_zKXh_95BBeAeQs5WguEkzVm0EcurW2U5Bupiu5Ler5lpxbyMb34pe-oaE6J2n6uMhVCHPQnhvU1r5qy_TZ90N-y9ZBSr0oj2jRt2g8Rimc4mRq_039zYOT17vLp6on50OjRfqtgvBvF9o-NkznONg5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c96b58fbf.mp4?token=i_hJPCGxnPOBw_addej9DI3Cmcz8td86Pwsigrm8ycmy3a1I_cRYOAAMYMDRBcKxZ2XNJlZqVJujkV-2BkCkv7ZfDP_pTmxVRLu3gdJCvDnHMbtScyYEAcqZi3IEsQwvByytG0PGJb0WSIJV_k2b7x3ZTswaHimBT6j7DUcpXl7D9-aMPS02iNBuqSrL3XqS8-LDN1T9MLWZreSwmk-pqag2LGZ2VDof75ZPXkpULy6oqspaev5FAq881MTiEw06RxdjZbZXj3E9SjOkK16i2-hWDPVg7zKt599Jf7qp2wrO6D_VApImPacSkrxhDzy_HbAVvf0HHQD0nG96_oVnAqj8c11ESlHwm7Uv_tdMnhJroFgKIy4pNvFf2OHWIhOYqznVkMe10ftnZUWcVS0jDT3FoE9RpNRqeRdNnEHhrMCoBkXxzG2sRXAUqRsc2G5BTwdEEjBGhWhypoCNlTvoE2Fw5flray3eaOUGx4ghcZ_1uQ43vHBV76sdJYUl1xIwbdsrnjrJg_Y6q8o9I7_zKXh_95BBeAeQs5WguEkzVm0EcurW2U5Bupiu5Ler5lpxbyMb34pe-oaE6J2n6uMhVCHPQnhvU1r5qy_TZ90N-y9ZBSr0oj2jRt2g8Rimc4mRq_039zYOT17vLp6on50OjRfqtgvBvF9o-NkznONg5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
جولة حصريه وخاصة لكادر قناة نايا
من مضيق هرمز حيث تظهر عملية سيطرة واضحة على المضيق من قبل دوريات وزوارق الحرس الثوري في ايران .</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77197" target="_blank">📅 09:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">📰
قناة NBC News: البنتاغون يشعر بقلق متزايد من أن إسرائيل تكثف نشاطها التجسسي ضد الولايات المتحدة، وقد تم رفع مستوى التهديد إلى أقصى درجة</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77196" target="_blank">📅 09:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeIKoKAeILfs9VPLHbmQ7N5QJxOxlJCbw6jDie_DZVJ5GcgkG5LVSH_YRUcp9ec7YPxD7I5Hv7Y1LNQ6lHgC4qapdgIpRU7s8MTpaykuPLM-aIy4nUBGQOsejib30nHSOz5rbeHCx7sKuTqiRREyGnuOdxUKEBSKcm3sQyaf1q53Z_pM1d2M-k--htBcjH4JYytb2HmPdZXEGdnjnv3BmwByDVxrfii0qpo761L6St5g3jMPJdCsoCOHBvQ2eh69fpihIzjs0RjqqL5a3q_IBBAhSmZ8MVx0_UBOMJfYjr8i4srr-OPp592o3jFc0HjN0kCEKCtDoTOjwxaZ7AeKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWmlNOnqvv4mkpfDjn0gRntIquyv3JQnpIzp0HynM0jSrQgW9oJH479NwTcWhzTnxU_IHm9fgVIlP1yYA6jsayWFkNopZmax2vJApGRpYvwfB6ARIbmAg4W0kex0gvxyUGWzIHsEhuA6ZnJSeWf2VhPdl22c5lPuLlkigcJcI5c7HW7OQDlhhN2PILbgZVLP1gXlm4I-4obiaJ_hXw_-sZ1exzYwKgT-cFC32rivbmZZ78MT_U15xG2UmucCrGF-t8hVzGFtuOGjDpUOxj4bL78CQi8YmAZ-qJZ6SmOcECPCd2JOsA4wbPAdXcK6az8FRjF_dwp3TX9n45xCA1o8OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صور للأقمار الاصطناعية توضح استئناف تحميل النفط في محطة جزيرة خرج البحرية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77194" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e1b8f880.mp4?token=Qeic4aYru7dFqAm193XRiasT6A_Qe8NO6ENEnoYqhqmGTRCx55-vyASW0BwPHAhh5jGW3jzLjYZeIcLrQlWYsLYYCLg2I3tUPpA1DDH5ZnZ_jhbYnON9FZhbmb0H1Rs4EGNlH-DFkEpQtv-_bLogH-4nqrWQ3EBgT3V-A9FwcgL6wP3NvSAZvakz30h0Q5PGODD1KsDJiJijQjMtEP7D3S07wuWCLiAsq0AbeXLjP9W_j3nEeg8GYG6_yoCixHCmkr9foIUCrR3co9TJ84_hQZU7Oy7n7Sp9qWCPArRx8RpziQnz-ID2gOJ_FH62Fb4g0Rx7TKT19idmYOiwRPQYE4sFgbckDlPNbCjrhr1uxa8p-MYz1YDv-AcGbrdf8KzY4dFH44F0CBH3YyTQ4xLySiCkRXJyuQ5tYTCRWavYRCUlbwm1mz8xAbf_FWFlu2EmkBgqjQ8RYvNLOrWCzu3aGvRc8LFkujcbH9ogX4lzvACkhUG7TPsDfY7QYR66jpjMSYr_JWM-rBwD4ESGoBYeOewWcXnYEuQAkRzE_3XjXfPZPQfSk-fEtPdZlixMEM3_6vGLmqNPfsjqqUyRrPW8VeBoMaaxve8Qxa0loPntOe0oFl03SWqPFRTr3CEueq-Z9YBPp58CAJVXfJxLIqpVD5fHNQJrnQ-XVLzSP20jK5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e1b8f880.mp4?token=Qeic4aYru7dFqAm193XRiasT6A_Qe8NO6ENEnoYqhqmGTRCx55-vyASW0BwPHAhh5jGW3jzLjYZeIcLrQlWYsLYYCLg2I3tUPpA1DDH5ZnZ_jhbYnON9FZhbmb0H1Rs4EGNlH-DFkEpQtv-_bLogH-4nqrWQ3EBgT3V-A9FwcgL6wP3NvSAZvakz30h0Q5PGODD1KsDJiJijQjMtEP7D3S07wuWCLiAsq0AbeXLjP9W_j3nEeg8GYG6_yoCixHCmkr9foIUCrR3co9TJ84_hQZU7Oy7n7Sp9qWCPArRx8RpziQnz-ID2gOJ_FH62Fb4g0Rx7TKT19idmYOiwRPQYE4sFgbckDlPNbCjrhr1uxa8p-MYz1YDv-AcGbrdf8KzY4dFH44F0CBH3YyTQ4xLySiCkRXJyuQ5tYTCRWavYRCUlbwm1mz8xAbf_FWFlu2EmkBgqjQ8RYvNLOrWCzu3aGvRc8LFkujcbH9ogX4lzvACkhUG7TPsDfY7QYR66jpjMSYr_JWM-rBwD4ESGoBYeOewWcXnYEuQAkRzE_3XjXfPZPQfSk-fEtPdZlixMEM3_6vGLmqNPfsjqqUyRrPW8VeBoMaaxve8Qxa0loPntOe0oFl03SWqPFRTr3CEueq-Z9YBPp58CAJVXfJxLIqpVD5fHNQJrnQ-XVLzSP20jK5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القيادة المركزية الأمريكية: اعترضت القوات الأمريكية عدة صواريخ باليستية وطائرات مسيرة إيرانية أطلقتها باتجاه مضيق هرمز ودول الخليج المجاورة.  أطلقت إيران سبعة صواريخ باليستية باتجاه الكويت والبحرين بعد ساعات من إسقاط القيادة المركزية الأمريكية (سنتكوم) أربع…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77193" target="_blank">📅 05:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77192">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
🇮🇷
الحرس الثوري الإيراني: بسم الله الرحمن الرحيم من اعتدى عليكم فاعتدوا عليه كما اعتدى المعتدون. في تمام الساعة الواحدة والنصف من صباح اليوم، قامت أربع ناقلات نفط معادية، بتحريض وتوجيه من الجيش الأمريكي المعتدي، ودون تنسيق أو مراعاة للتحذيرات الصادرة عن القوات…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77192" target="_blank">📅 05:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
🇮🇷
العلاقات العامة للحرس الثوري الإيراني: في أعقاب عدوان الجيش الأمريكي الإرهابي على جزيرتي سيريك وقشم، تم قصف قواعد العدو في المنطقة بصواريخ جوية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77191" target="_blank">📅 05:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAaPuBv4K6NcbJOWbnapSviZrfvEiMlZ42pV65u4JVEAI3tpD1PMC8Ld0e-hl5nv9PFKNH3tc6kQeiERQil06LHtfZUyBUyz0nEBTEeTRwHUnarvY3iAXnT5BmXbJ4GetA53Dt9VSr4TTNHF2IW2-dXJ8980xHXGheDmgHvzK40Y-vXCM7UiGOkOx8oBrGcX4AWyXeXS9spOceijVi829BEdfrLsC-VorPtnuO02JTFrhRHR-qZORgiC8ZEAPv5_3IYTYikz0GayMz67mVrPtzYKR-RI3nY3zAbBTvazk-x0I_31yrAmCdqQJuaGO70YGDQQUqsEdfT3cgJE_hmbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ألا وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة والذلّة، وهيهات منّا الذلّة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77190" target="_blank">📅 05:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
🇮🇷
العلاقات العامة للحرس الثوري الإيراني:
في أعقاب عدوان الجيش الأمريكي الإرهابي على جزيرتي سيريك وقشم، تم قصف قواعد العدو في المنطقة بصواريخ جوية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77189" target="_blank">📅 05:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDUh3UlGa0hcTJ2kNiato1H963To9gpsmlRDCY4vDVr0f_-0K5gfV2FRFGRXv4G2bRA3S0I1H-GTvj70AAQg597M8up66Z7ZpwLmPJpVuVw-X47eGt21sRRZkZ0NAEA6aqQi3oMfZ9Ebty8qxeYoyq4Yq5xMxMyTrolf5PQrAYoQfb_-Zh-K7glPITIBsXGMV_CCUoSkaeYf7LvSSu_7x2hz2QL2e1jwjZUkZKl13wVcSddjXArCHfyo6tkRQrh5zB0_5uuYNR5PzLnWgyCwxqu1XFukiaJv6zlnyolf2qR9a-KCy3jKUzebi7GvxrrT1bWvVxd8mr6HtEvFpP-vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ألا وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة والذلّة، وهيهات منّا الذلّة
.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77188" target="_blank">📅 05:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMjYLwxGkvqSbOVLJlIXOCe2Yogd_NEHEd3I4V6fp0yFPQShtkm9Qa9sAvDDuHz9ZSbC4BOq-aRQV5o_7kp_ZhIxIflJCAiAU_ZboZH_hmVml-8oCM15ziGErJk1xqV2alTPweelaiOnWehX64PsdNBNKKOMwZxC8LLQ3xtoaDQwrCaYPpU31e92knnUi_HPPkAZfPGNmZ58qZ84j9yHo_JdcOifLvzdC88HQqRdN1HVMWvOr4yWpfcEfnikuB0g2Yn8UTP32zKtvo4Z07YT-cI5qr06OaswtaDwiG72RPsVOWOxOHfOcW_RVo0WYjlYmSkbqL7hwJdD0HI0npiifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جميع الطائرات التي تريد ان تهبط في الكويت تغير مسارها بأمر من الصواريخ الايرانية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77187" target="_blank">📅 05:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c57c76ee8.mp4?token=MKzg7t0YDWqEGQVI7t_XH9bULSR81oQfb10sQuLJnBPEv95fEyZL2tg9xWasOVjAgqE1llaOcqXubG7MNpFsGJv2xn-F7PgNEK6jZBGsiI07p6nhcniJVdDzBbDoFGlRmvygdTMudXA6wXjPRoqbP9kU4EejbWxEpkZoFkKwGGYBatDqO_YtSuoqIjybPAbg97mt4Fw8W2VSODR0XheYiUaVegQjZdzb0zAKKaDrxW8KPs77Bac1M_wuELDHvN8Il3Dh72NEfaBV6p2mBC0G4n-iHUdgqJTJV2qbzkXbJqCXP31ROuwGqFkB37udLyF0wtzx7MHopaZkXAltmCoIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c57c76ee8.mp4?token=MKzg7t0YDWqEGQVI7t_XH9bULSR81oQfb10sQuLJnBPEv95fEyZL2tg9xWasOVjAgqE1llaOcqXubG7MNpFsGJv2xn-F7PgNEK6jZBGsiI07p6nhcniJVdDzBbDoFGlRmvygdTMudXA6wXjPRoqbP9kU4EejbWxEpkZoFkKwGGYBatDqO_YtSuoqIjybPAbg97mt4Fw8W2VSODR0XheYiUaVegQjZdzb0zAKKaDrxW8KPs77Bac1M_wuELDHvN8Il3Dh72NEfaBV6p2mBC0G4n-iHUdgqJTJV2qbzkXbJqCXP31ROuwGqFkB37udLyF0wtzx7MHopaZkXAltmCoIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي إيراني عنيف ومنظومة الباتريوت الأمريكية تحاول الاعتراض في سماء البحرين</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77186" target="_blank">📅 05:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded6a8a118.mp4?token=ZLP7ea_7dfO6ucE-4Yn5Ve6Av6GvX1TytQAQWhcsQ4temkA8hV9OXWQ5A8Jp6m2fDrSNF36GyrHRJzgBN8heKxnGY20Q1ZBw-8vTSw4zr6wYyozN1TBUtofHXDdf78rktpTTzQznaRG1Pifug3twlX0xYXSUpz4hFqmnisUfXTqsAI4a2uxf3cVpsUvmsMMnJr_T7ovuVbFRVT09QV6kHEW4sSebVgUKRcYQGXpkWYa06PRCwSZVszqtLw7NrIvP8MkdWiZWhAX66Z1YU1Ey46kbz1Z93Jur66R_2K8yhikn5DHyPwASDUqaaOoHovGpG40qi5ouzw_Z2WAOreJ4Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded6a8a118.mp4?token=ZLP7ea_7dfO6ucE-4Yn5Ve6Av6GvX1TytQAQWhcsQ4temkA8hV9OXWQ5A8Jp6m2fDrSNF36GyrHRJzgBN8heKxnGY20Q1ZBw-8vTSw4zr6wYyozN1TBUtofHXDdf78rktpTTzQznaRG1Pifug3twlX0xYXSUpz4hFqmnisUfXTqsAI4a2uxf3cVpsUvmsMMnJr_T7ovuVbFRVT09QV6kHEW4sSebVgUKRcYQGXpkWYa06PRCwSZVszqtLw7NrIvP8MkdWiZWhAX66Z1YU1Ey46kbz1Z93Jur66R_2K8yhikn5DHyPwASDUqaaOoHovGpG40qi5ouzw_Z2WAOreJ4Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء البحرين تشتعل بالصواريخ الايرانية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77185" target="_blank">📅 04:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQF42_NzpgOC3fLZrFU8Y3QlaTHYzbRGYoWQrS9nBYTD7kYil7ALejxSvkIepm8L5MIkNHVEo1KrmZ6Aue8bXTKLZMvIP33qwmB8i9uh8MF8ChMnI86b8WyCDSnzggr-knC_rbx4FVSb_K7nCXRsJILCmRhGPO2MJGQ7h15HrpU2hz-GoeAtFFADqG1Vd_4qu5zx0iM8AZMrYYaOXYeMllbKnssVCmQ7hddyglUyuhMZJxjmo6CFOhWTISi6aQ4chsa4Nhsat6wNbFW_K7VniNlBaOk7P_lKl9oDnTf2Q3nXPFCDDkW_68-Tzy7kgpfM6hgzunTJ3LAol9oOC_V0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdO3Ql1WwSUsfsHg1b20ccr1QbB8Fnc-gL08Qcj6Y5viTFS9IeWkT8paAAzGZkmG2N79ZNLc3malVAqqrJuM-M8_cPS4ENIcPejas0zbFDjj6J1K42tDN-7dPnB-Cj_QiD-umjup4_Ifduz5dV_AJEyXsxH9_mqwSlnNFKG3QMTk6pAESaFw6bBAfi-zLbiQiZD06LhoALiH5K4YKvJgPT__nj-geUDwHhM0374Mvnsuxx88xXxKiW1SQIrd1dq-za4QoYW1b7RA6jRyLZ3g61kGJA8sR0Wpdh-W5cBBeYGtHYdyhgfnvxPp6axUuZkJHmXMI9fY_yxtbkHDZc2bZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تدك الاصول الامريكية في دويلة الكويت</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77183" target="_blank">📅 04:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5af5fb49.mp4?token=Jpt3qU1-sYtCVzw4AJF3Fp0ZbjgfzmdmtfklKMDycZ7HTihsGSDlRmPF0-HGrrAGo61-GGuFJ5gatoV9j5B33eEFClo-7_jGDbmDPf1K9kRAhQbYyHF-wdpU046gD63hdOliCaAx1RRnKmJsSDJ2TeignpaWomH9K0tkZjfpQwX1KKZ3dEQ5kAzUpgOTs1mkSJObP9yq7O8DVf-TD0nzogdEAWFWfjZa_ANlYGAmLyrLPfvcM8hxCu8rsjwDkzVILM90OeCSY18wkl3TgcYujoxgweucFjY75Iu5njo4X2hZUXwWXAm_Nzrl33nnZDtiqcpozinDapy8SDj6XEW_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5af5fb49.mp4?token=Jpt3qU1-sYtCVzw4AJF3Fp0ZbjgfzmdmtfklKMDycZ7HTihsGSDlRmPF0-HGrrAGo61-GGuFJ5gatoV9j5B33eEFClo-7_jGDbmDPf1K9kRAhQbYyHF-wdpU046gD63hdOliCaAx1RRnKmJsSDJ2TeignpaWomH9K0tkZjfpQwX1KKZ3dEQ5kAzUpgOTs1mkSJObP9yq7O8DVf-TD0nzogdEAWFWfjZa_ANlYGAmLyrLPfvcM8hxCu8rsjwDkzVILM90OeCSY18wkl3TgcYujoxgweucFjY75Iu5njo4X2hZUXwWXAm_Nzrl33nnZDtiqcpozinDapy8SDj6XEW_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في البحرين</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77182" target="_blank">📅 04:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXpPnYfcC2AP5mVb-Df4C-VPdbnA5iFGHD6Q1qgLvcn9iDE9IOK51WD77dbs1_pybCWjBmHTyF_HYa0fGUnhlQ_9XGN-5HdlIcRZmGSCCwaIcp7K7Surt3bdb_9Y7JbqyuBpFk5ccpoQy89DDeH3qWfm9o22GYnILqL_o0uAzWZEk3Eso8ishWdRu0I47oveVSPuOg1gwd9whhxVmibXOucgbxLag1r_s1wP3NBk22Rc83E5hBktsZV_LmeqY6zW1-1B1VNiotjnDwZbC-vJNlh2L-zsm5R5nb-2HHIhJ15YsdyQcnri97VxwwjG1YChlwdPXZVapN__S4ddbNv6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDhHb5ALSD5hyZr7k3tLpvLzpXwOQbFVYrhX0s0W3QFuh5WuElD8hzS7VVs71SVFMdM0AQ3YQgBoWR9Gca5Xk9zoFzglAxOEY0XX39YBCYU9MZW6o5ukHu7gG_g9Ce2EJs5s_dkWvYx_HqrIG1FZT5WvoPiDTANTLur1Pu_hUwid56U8jnEwqdVITcJzCOtyc_ChOjkFjsBFCFHnMzMK0l1j4S3mt_4DcJc5QeZ53F7q6c30lIRuGYwIhj_y2TTo6euGj5fLyJFLa1ZbyxF0o1-ykFWf3hqvZtJ1rJIcFKwLCTw3MAkVKPnHu34BRxuWd_Oisu_YbrxHs6Ab1X1W3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQMkPbqmxzFrj7hBsF042yTI2Wzfah-MsAjFVtMTQBB6PGE6XpAuXuYyu47YFW5b3huXOLLg1CZ9M7VHSCm-XbOuEB4FC1fiikqX9obsarR0BWaf3fCLB8tmkUJQQoyOiqJKFGaaCSlgyto5joxuDogLkEf_Lm37k7OOvSwkH260tQH3Jh7ukgr27j8rqWcQOCXH5T5spDP-3K1cM3J4ow3G6jXCaZTCxNFBnyFsL-pSwkeW5X_z5Hh_nAdEmgISK-6YBFKT7VpU1uMOwSIcgTnflW8KIhGTZJuDUqe3XczJVm_GEccKliDgt82-RWXdKd__4QOvPb6uWP-r6UJoIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مطار الكويت الدولي يستهدف بشكل مباشر</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77179" target="_blank">📅 04:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مشاهد من تفعيل صافرات الانذار في دويلة الكويت نتيجة هجوم بالصواريخ والمسيرات من قبل ايران على قواعد الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77178" target="_blank">📅 04:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af66abc0c.mp4?token=COw51bG8yGN8HgHBaPcL8kmUCL2v5fOV1uTtrYNMdp4A0QitCVrGb4A2s6KC48eP8x1cjcm3lpT2T2qrQaf-yZfaYyjd3fbgBoR0d42x9EcPn1gqkFa90zRvGUp-FqZ1KclM_86jGnJzfVw6_tmJkj8LT-x3weF6CUftuZek5aQHTaCLBXw7Tw6h0aSTJNtRhQWrU327T79sBUV-EVGcXZRhsm5aU9KyKxVyZxVQ2CWJxugL-bUOL738vIwq5C-usDob903BSHohFhChdrCZWPp0fIu2O_GbzSGaWOUCEKD_pMqno03VbaciKAw7wgiNsMAl2t_7jD5Us_0U_8O5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af66abc0c.mp4?token=COw51bG8yGN8HgHBaPcL8kmUCL2v5fOV1uTtrYNMdp4A0QitCVrGb4A2s6KC48eP8x1cjcm3lpT2T2qrQaf-yZfaYyjd3fbgBoR0d42x9EcPn1gqkFa90zRvGUp-FqZ1KclM_86jGnJzfVw6_tmJkj8LT-x3weF6CUftuZek5aQHTaCLBXw7Tw6h0aSTJNtRhQWrU327T79sBUV-EVGcXZRhsm5aU9KyKxVyZxVQ2CWJxugL-bUOL738vIwq5C-usDob903BSHohFhChdrCZWPp0fIu2O_GbzSGaWOUCEKD_pMqno03VbaciKAw7wgiNsMAl2t_7jD5Us_0U_8O5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية التي دكت الكويت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77177" target="_blank">📅 04:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c5e77fd3.mp4?token=OowpvVmXOWITXr1gQb5_rAr1tgqp2O7-ep_7HoaGMpIKT-76rfeKceFrlpHbUXPtINWjYf3K6yyIC1C1qGEVNyiWbbCE5V-PDw56skYuMJza3zYDH8s4STTWRWssjVSCa2s0KdPMHmcW9LHcnp77gvv9yzPxJvFU5DWk_YPuIihLCKSG3lMg5uqVXSV354FfCkesxUv4bBVaFM42J9DIqh_1F3k_WfcjZZt50Atl2HqhzBgfHvgwqRKQdLpfrz4AgNCclDMZfYHMeighwCqmWlCNQCKY8cyRgq9MTI_xZ6c5olbwi0elsMkU-BoDB3JmUP2lW9q6ycD3LVfgtO_VVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c5e77fd3.mp4?token=OowpvVmXOWITXr1gQb5_rAr1tgqp2O7-ep_7HoaGMpIKT-76rfeKceFrlpHbUXPtINWjYf3K6yyIC1C1qGEVNyiWbbCE5V-PDw56skYuMJza3zYDH8s4STTWRWssjVSCa2s0KdPMHmcW9LHcnp77gvv9yzPxJvFU5DWk_YPuIihLCKSG3lMg5uqVXSV354FfCkesxUv4bBVaFM42J9DIqh_1F3k_WfcjZZt50Atl2HqhzBgfHvgwqRKQdLpfrz4AgNCclDMZfYHMeighwCqmWlCNQCKY8cyRgq9MTI_xZ6c5olbwi0elsMkU-BoDB3JmUP2lW9q6ycD3LVfgtO_VVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية التي دكت الكويت</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77176" target="_blank">📅 04:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77175" target="_blank">📅 04:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77174" target="_blank">📅 04:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPgm1U5jcSMs2pXNnBZcp5IprxnPFZjYrzCe_h0HhxF2V7v4NgoX4lVv_jmSO0j0jOxxeB4TDGuOgLr2sslYcTrK9nSgiJs7sna8IPPvKQp0HPZ_2r7OUv3N6T3ODoEbzh4XrZG7yXgX8OhWegjM0MjZiSETi946A5ME4QDuJ2FKMqR36boVX_2njuTKw7LH2AUomuGRrCo2297PAJELpQ1zn-Mk2iVymE4Yo_sVh14TjQyNdiPnl6CQYvrTY-JiFj9itO42wNntlHhJlbKUIsw0Va3JK7_kZb4nXvyDG-nUnlm7QkezSXA0kijtWyNAHSVpqE87bxDUOQqoNSCbBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77172" target="_blank">📅 04:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77171" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هجوم جديد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77170" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هجوم صاروخي يدك دويلة الكويت وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77169" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17be2d7041.mp4?token=M2PYVuHEAqbz1LtSjKCS5wL6R4kfDWW1o57jOGrg369l0aiC8dad1F5QJRdJFdG3iryi1Ow0lsYYjkzFwX9r1BXGh222-5AsQL6T-jIP_8gCYJEtuifGeTiiAEuB9oD7LS4DKfnpKqJC5wC9ZfuEJbt-giElxd6G4wjEl3K3kR7HmIQLAkCY4cxrNbdEG3gpSYDVeq_EixNvh7kPcdWQZz2-PYpBV8F14ZdvabuJ1HJQSsictU4NdE1beuK4SWwo_CU33gdVj128uYoamgNdOvVVR4xbWnb3xZk9sT7u3dtMgKvzdeHVzc8cz6caTKiCZAR3eKkE8oIXeZSXByI3GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17be2d7041.mp4?token=M2PYVuHEAqbz1LtSjKCS5wL6R4kfDWW1o57jOGrg369l0aiC8dad1F5QJRdJFdG3iryi1Ow0lsYYjkzFwX9r1BXGh222-5AsQL6T-jIP_8gCYJEtuifGeTiiAEuB9oD7LS4DKfnpKqJC5wC9ZfuEJbt-giElxd6G4wjEl3K3kR7HmIQLAkCY4cxrNbdEG3gpSYDVeq_EixNvh7kPcdWQZz2-PYpBV8F14ZdvabuJ1HJQSsictU4NdE1beuK4SWwo_CU33gdVj128uYoamgNdOvVVR4xbWnb3xZk9sT7u3dtMgKvzdeHVzc8cz6caTKiCZAR3eKkE8oIXeZSXByI3GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي باستمرار في الكويت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77168" target="_blank">📅 04:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b0024f3f1.mp4?token=AjosyY-Hl9g1o5KHiGnt34FP0QoTwSXWhrVFKixd2VOmc_teVR_E7YjW0TkDS7uoxq89CeEN6yn0U5HjMRVNhGqySG07rp8pAQq71_qHvgNcUyOGOGBbHJ0Rz4PX3mX4G6tyLGf4SZavqNEx_sHtC7a4Op_J__1RfUuW-dvboOnVC333xc2_icWDqXIZx3k4lqR4z1IUpJtkz5qikixsDHVGDyz6ex5tdx9UbIqkbym8MBPiM-zTmNFdj9lKO9zjqQ6dDjEfk-70b9K_BHDfPV4JVyqFHvNkFT6Lbj6HmL7kLIgh5yid5lYzrVouL4XumHnbu-b8tw1p92nAr5koJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b0024f3f1.mp4?token=AjosyY-Hl9g1o5KHiGnt34FP0QoTwSXWhrVFKixd2VOmc_teVR_E7YjW0TkDS7uoxq89CeEN6yn0U5HjMRVNhGqySG07rp8pAQq71_qHvgNcUyOGOGBbHJ0Rz4PX3mX4G6tyLGf4SZavqNEx_sHtC7a4Op_J__1RfUuW-dvboOnVC333xc2_icWDqXIZx3k4lqR4z1IUpJtkz5qikixsDHVGDyz6ex5tdx9UbIqkbym8MBPiM-zTmNFdj9lKO9zjqQ6dDjEfk-70b9K_BHDfPV4JVyqFHvNkFT6Lbj6HmL7kLIgh5yid5lYzrVouL4XumHnbu-b8tw1p92nAr5koJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي باستمرار في الكويت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77167" target="_blank">📅 04:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صافرات الانذار تدوي باستمرار في الكويت</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77166" target="_blank">📅 04:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوي انفجارات عنيفة في دويلة الكويت  نتيجة لهجمات صاروخية وطيران مسير</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77165" target="_blank">📅 04:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوي انفجارات عنيفة في دويلة الكويت  نتيجة لهجمات صاروخية وطيران مسير</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77164" target="_blank">📅 04:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سماع دوي انفجارات في ميناء سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/77163" target="_blank">📅 03:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77161">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1795e9070.mp4?token=Yd_U3hZjXPMUfy-oE8uFIyW0IfnQmn3O9OhgDkrWKtn-ZsZPiE-DsNQnmivJ5AMnhLOTi2HETsICswDoFidPCzwN__xxu-1MrbUAb_FvrI6dblZ8Jb3Yu4OKh6HY48CaRtK1Savj3HdVImYN0Fd9hKxNhZtE-nL_3dT4pWtnyVzQyExAxrgAzKpB_Im_EqVWzL1os329nP4eeKoCxB1a8nMAV_cpVMJOqQOlzpYYU30HJKxOpFDEugmD0179LlfvVLgHwZHZdB5BSctWYtyJOmep1iUe8TNhu65GP-krWX0BfDRgW7NUXx_fokUD0dAS1khDYlpgXOP4zBbCPNMEmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1795e9070.mp4?token=Yd_U3hZjXPMUfy-oE8uFIyW0IfnQmn3O9OhgDkrWKtn-ZsZPiE-DsNQnmivJ5AMnhLOTi2HETsICswDoFidPCzwN__xxu-1MrbUAb_FvrI6dblZ8Jb3Yu4OKh6HY48CaRtK1Savj3HdVImYN0Fd9hKxNhZtE-nL_3dT4pWtnyVzQyExAxrgAzKpB_Im_EqVWzL1os329nP4eeKoCxB1a8nMAV_cpVMJOqQOlzpYYU30HJKxOpFDEugmD0179LlfvVLgHwZHZdB5BSctWYtyJOmep1iUe8TNhu65GP-krWX0BfDRgW7NUXx_fokUD0dAS1khDYlpgXOP4zBbCPNMEmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
مشاهد حصرية تحصل عليها نايا لسفينة شحن تابعة لشركة أميركية "أريستا" (Arista)، محتجزة في مضيق هرمز من قبل الحرس الثوري الإيراني، بسبب مخالفتها قوانين وتعليمات العبور في المضيق.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77161" target="_blank">📅 03:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77160">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVFsb8TQOZi_nlKl-EAKeCAZPRH_v0IxvzvHq_jqTe9u125WzwAMFwudFWWE3ss79XzPsLVT_rqS1sR42Cjom89EVsp-g1CUvjP1SNmRXsl-VzNEEfC8GZG1US39fIeayTtiQy1iByahYsr9U8ZOj9OV6dNS_ePIhFTeXX0W7GGJXA87isnQWpcLGbOsg65wh_ZBRHW0TQY-NvNWQxZSCdSIRDAQsNy3_OXYPib2tbTBFFtkc4uh7OS7lKcVeSX8Z5NLhFK86IA6eQQo2g19VwUzW60owLoJaNrcFNcxCrzax07QqcDzgMPbOf1bUZMEiYddUgh4eefdLjM87G_JOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:
على الرغم من أفضل جهود الحزب الديمقراطي الكاره لأمريكا، والذي بذل قصارى جهده لتدمير الولايات المتحدة الأمريكية خلال السنوات الأربع الطويلة لإدارة ترامب، فقد وجد أكثر من 172,000 أمريكي وظائف في شهر مايو وحده! وكالعادة، قلل 100% من اقتصاديي بلومبيرغ (الذين يبدو أنهم يدخلون المراحل "النهائية" من متلازمة كراهية ترامب) من شأن اقتصادنا. على عكس نتائج انتخابات كاليفورنيا المزيفة، فإن هذه الأرقام لا تستغرق شهورًا وشهورًا "للظهور تدريجيًا" (مرروا قانون إنقاذ أمريكا!). يقولون دائمًا "أمطار أبريل تجلب أزهار مايو". حسنًا، هنا في "أكثر" دولة حرارة في العالم، في كل من أبريل ومايو، إنها تمطر وظائف!
الرئيس دونالد ج. ترامب
نمو الوظائف يضاعف توقعات السوق في مايو
التغير</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77160" target="_blank">📅 03:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77159">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16be68b8e5.mp4?token=gHKzcGteQWNzoe0ae4zrmOIaExFSqBLx6fHjx6hit28x6YdYfuDPGIcsNPfcDa4n2LoN228lABbZoKNm_GUOwdHTwt9INejZaKZ3yoIoA5vI7TkQWYTDRjZGpGHblvQ_hBfh0AsHXRdHKWCvkT5HzRwRnf00SGeTZ4Sw0yOrQxSv-BUPOLanOcZ_wy0bM8UZ3HZGr7NEsxzae6lgAT69vyLH-AhV9YuYuNHinDT3jtNmkuz8ddazl3zuV39btI9di9tUoLTajfkIP2SaD2n_7NJr_MjrpSnOpWy3j1XK_PTkuP-l_de3In-cEgM1ow6n0KFoENMCm8AeETQ-E5Pfhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16be68b8e5.mp4?token=gHKzcGteQWNzoe0ae4zrmOIaExFSqBLx6fHjx6hit28x6YdYfuDPGIcsNPfcDa4n2LoN228lABbZoKNm_GUOwdHTwt9INejZaKZ3yoIoA5vI7TkQWYTDRjZGpGHblvQ_hBfh0AsHXRdHKWCvkT5HzRwRnf00SGeTZ4Sw0yOrQxSv-BUPOLanOcZ_wy0bM8UZ3HZGr7NEsxzae6lgAT69vyLH-AhV9YuYuNHinDT3jtNmkuz8ddazl3zuV39btI9di9tUoLTajfkIP2SaD2n_7NJr_MjrpSnOpWy3j1XK_PTkuP-l_de3In-cEgM1ow6n0KFoENMCm8AeETQ-E5Pfhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
مشاهد حصرية تحصل عليها نايا لسفينة شحن تابعة لشركة أميركية "أريستا" (Arista)، محتجزة في مضيق هرمز من قبل الحرس الثوري الإيراني، بسبب مخالفتها قوانين وتعليمات العبور في المضيق.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77159" target="_blank">📅 02:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77158">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: قبل لحظات، أسقطت قوات القيادة المركزية الأمريكية أربع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه كانت متجهة نحو مضيق هرمز. وشكّلت هذه الطائرات تهديدًا مباشرًا لحركة الملاحة البحرية الإقليمية. وعلى إثر ذلك، شنّت القوات الأمريكية…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77158" target="_blank">📅 02:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77157">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: قبل لحظات، أسقطت قوات القيادة المركزية الأمريكية أربع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه كانت متجهة نحو مضيق هرمز. وشكّلت هذه الطائرات تهديدًا مباشرًا لحركة الملاحة البحرية الإقليمية. وعلى إثر ذلك، شنّت القوات الأمريكية…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77157" target="_blank">📅 02:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77156">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تشتبك مع أهداف معادية في سماء خليج فارس</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77156" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77155">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac7876255.mp4?token=SJK0KFQbjdLMhq1vWVD8bTen-hE2B3pDJkuac1wEF5-zFIarRQbrNrn0YstxrzAPW-oXL_-2FDJln3GC8qlUTiJA-uJVbMQqLiCBK64Ik3mNizE3HZ8VquQ70gyy_D6oYDzqQpb31Ny7DRokGij3BMT8S9FCSVI0nUV0-Z-sgl-eGUKMm61cnuRKketrATD0k0PwuJlEaGdysvd38kdMe_OTvSxBM1KbKqFDTRrD6ITOriC9CkwSLmbLGDSiUkfQoOQd0IpnJHQ5bMuxbrYwe9UOsJ9wSUo1qeaHzy3FmS2infT8Yt2Q7h8OIRjVwVeGtiCaNho95NfS_vJtbDo8Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac7876255.mp4?token=SJK0KFQbjdLMhq1vWVD8bTen-hE2B3pDJkuac1wEF5-zFIarRQbrNrn0YstxrzAPW-oXL_-2FDJln3GC8qlUTiJA-uJVbMQqLiCBK64Ik3mNizE3HZ8VquQ70gyy_D6oYDzqQpb31Ny7DRokGij3BMT8S9FCSVI0nUV0-Z-sgl-eGUKMm61cnuRKketrATD0k0PwuJlEaGdysvd38kdMe_OTvSxBM1KbKqFDTRrD6ITOriC9CkwSLmbLGDSiUkfQoOQd0IpnJHQ5bMuxbrYwe9UOsJ9wSUo1qeaHzy3FmS2infT8Yt2Q7h8OIRjVwVeGtiCaNho95NfS_vJtbDo8Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا  معالجة طيران مسير مجهول كان يستطلع أهداف في مصفى بيجي بواسطة مدفع رشاش عيار ٢٣ ملم  .</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/77155" target="_blank">📅 02:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77154">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77154" target="_blank">📅 02:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
‏
الخارجية الأميركية:
الموافقة على بيع الكويت أنظمة مضادة للمسيرات بقيمة 1.98 مليار دولار.
حتى تزيد سردية النيران الصديقة
😂</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/77153" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">إعلام رسمي إيراني : الأوضاع في جزيرة خارك آمنة وهادئة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77152" target="_blank">📅 01:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79719e65e4.mp4?token=p9YBBcfekFyRvSeRADXdtE6kRwzaloBUiUuV6YUYfbbH3hYLwVTvOcIg93zBUDbOx2mjYk7SK4YarK2rVUzzgcer2QWVU0hyawF8jz31TgEpW-MuBD7Dy75vGquazI1GleFGoUfYnU5EL2JNU57VsmgrkTAEtkFIuF2CMWQ0E_IsS6qkwQl2bYJJBG8VS0wrLPgQik6kgJCVIoUIS4wTQ7Gi6suLlVQnaAe5eCi7E337-_ED1lTR-N7oJX9RE9koHx8qex6PZYxkdjXmexd6kLDy307UHO0YiyAs3dSZupQVJ6XHUGQVlsP_EXUy917ItLgxZGSHq11I-LvW1rr-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79719e65e4.mp4?token=p9YBBcfekFyRvSeRADXdtE6kRwzaloBUiUuV6YUYfbbH3hYLwVTvOcIg93zBUDbOx2mjYk7SK4YarK2rVUzzgcer2QWVU0hyawF8jz31TgEpW-MuBD7Dy75vGquazI1GleFGoUfYnU5EL2JNU57VsmgrkTAEtkFIuF2CMWQ0E_IsS6qkwQl2bYJJBG8VS0wrLPgQik6kgJCVIoUIS4wTQ7Gi6suLlVQnaAe5eCi7E337-_ED1lTR-N7oJX9RE9koHx8qex6PZYxkdjXmexd6kLDy307UHO0YiyAs3dSZupQVJ6XHUGQVlsP_EXUy917ItLgxZGSHq11I-LvW1rr-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/77151" target="_blank">📅 01:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
قصف جوي عنيف يهز محافظة صلاح الدين العراقية غربي العراق</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77150" target="_blank">📅 01:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تشتبك مع أهداف معادية في سماء خليج فارس</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77149" target="_blank">📅 01:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🐦
سي ان ان:
إيران أطلقت طائرات مسيرة متعددة باتجاه مضيق هرمز؛ القوات الأمريكية اعترضت 3 على الأقل.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77148" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
